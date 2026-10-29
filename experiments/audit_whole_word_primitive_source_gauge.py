#!/usr/bin/env python3
"""Exact whole-word primitive source gauge and ordered meridian clocks.

Tests original words before diagonal source extraction. No single
sector is declared a knot invariant or a selected geometric period.
"""

import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_source_fourier_twisted_traces import algebra
from audit_actual_borel_regular_fusion import fusion, inv, right_regular
from audit_actual_two_cut_ports import balanced_data, word_matrix
from audit_all_strand_cauchy_cap import tail_blocks
from audit_kashaev_ado_pointing import color_matrices


def shifted(a, N, multiplier, p):
    return np.concatenate([a[k*N:(k+1)*N]*pow(multiplier, k, p) % p
                           for k in range(N)])


def core(N, x, p, q):
    Q = q*q % p
    one, f, H, u, v, J, mul, power, inverse, nu, tau = algebra(N,p,Q,x)
    uq, vq = shifted(u,N,Q,p), shifted(v,N,Q,p)
    g = mul(v,vq)
    gi = mul(u,uq)
    C0 = H*pow(Q,-1,p) % p
    C1 = mul(C0,J)
    assert np.array_equal(mul(mul(gi,C1),g),C0)
    gp = shifted(g,N,q,p)
    gpi = shifted(gi,N,q,p)
    D, Di = mul(gp,gi), mul(g,gpi)
    Ap = mul(u, shifted(v,N,q,p))
    Bp = mul(shifted(u,N,q,p), v)
    assert np.array_equal(D,mul(Ap,shifted(Ap,N,Q,p)))
    assert np.array_equal(Di,mul(Bp,shifted(Bp,N,Q,p)))
    assert np.array_equal(mul(D,Di),one)
    for i in range(N*N):
        a = np.eye(N*N,dtype=np.int64)[:,i]
        b = mul(mul(v,a),u)
        c = mul(mul(gi,b),g)
        assert np.array_equal(c,mul(mul(uq,a),vq))
        assert tau(mul(C1,b)) == tau(mul(C0,c))
    return one,u,v,uq,vq,g,gi,C0,C1,D,Di,mul,tau


def clock_case(N):
    p,_,q,_,_,K,_,_,_=balanced_data(N)
    Q,x=q*q%p,int(K[0,0])
    one,u,v,uq,vq,g,gi,C0,C1,D,Di,mul,tau=core(N,x,p,q)
    C,Ci,_,_,_,_,_=fusion(N,p,Q,[x,x],[0,0])
    T=right_regular(uq,N,0,p)
    Ti=right_regular(vq,N,0,p)
    I=np.eye(N*N,dtype=np.int64)
    f=np.zeros(N*N,dtype=np.int64);f[N:2*N]=1
    z=x*right_regular(f,N,0,p)%p
    Da=np.diag([pow(Q,a,p) for a in range(N) for _ in range(N)])
    Dj=np.diag([pow(Q,j,p) for _ in range(N) for j in range(N)])
    denom=(I-z)%p
    Anew=(I-Q*z)@Da%p
    Jnew=inv(denom,p)@Dj%p
    assert np.array_equal(Ti@Da@T%p,Anew)
    assert np.array_equal(Ti@Dj@T%p,Jnew)
    assert np.array_equal(Anew@Jnew%p,Da@Dj%p)
    Up=Ti@Ci@Da@C@T%p
    assert np.array_equal((I-inv(Up,p)@Anew)@z%p,
                          (I-Q*Anew)@(I-Jnew)%p)
    return {"N":N,"field":p,"all_algebra_basis_cases":N*N,
            "exact_primitive_clock_equation":True}


def whole_word_case(N,strands,word):
    p,_,q,_,_,K,_,plus,minus=balanced_data(N)
    Q,x=q*q%p,int(K[0,0])
    one,u,v,uq,vq,g,gi,C0,C1,D,Di,mul,tau=core(N,x,p,q)
    S,ys=tail_blocks(N,p,Q,[x]*(strands-1))
    r=len(ys)
    tail_frame=np.kron(np.eye(N,dtype=np.int64),S)
    C,*_=fusion(N,p,Q,[x,ys[0]],[0,0])
    common=np.zeros((N**strands,N**strands),dtype=np.int64)
    labels=[0] if strands==2 else [lam%N for lam in range(r)]
    for lam,j in enumerate(labels):
        for a in range(N):
            for k in range(N):
                physical=C[:,a*N+(k-j)%N].reshape(N,N)
                for head in range(N):
                    common[head*r*N+lam*N:head*r*N+(lam+1)*N,
                           lam*N*N+a*N+k]=physical[head,:]
    common=tail_frame@common%p
    common_i=inv(common,p)
    physical=word_matrix(word,plus,minus,strands,N,p)
    relative=common_i@physical@common%p
    T=np.kron(np.eye(r,dtype=np.int64),right_regular(uq,N,0,p))
    Ti=np.kron(np.eye(r,dtype=np.int64),right_regular(vq,N,0,p))
    changed=Ti@relative@T%p
    source_before=source_after=0
    for target in range(r):
        for source in range(r):
            block=relative[target*N*N:(target+1)*N*N,
                           source*N*N:(source+1)*N*N]
            a=block@one%p
            assert np.array_equal(block,right_regular(a,N,0,p))
            b=mul(mul(v,a),u)
            c=mul(mul(gi,b),g)
            newblock=changed[target*N*N:(target+1)*N*N,
                             source*N*N:(source+1)*N*N]
            assert np.array_equal(newblock,right_regular(c,N,0,p))
            if source==target:
                source_before=(source_before+tau(mul(C1,b)))%p
                source_after=(source_after+tau(mul(C0,c)))%p
    assert source_before==source_after
    # Conjugation applies to the product of every actual factor,
    # without removing any off-diagonal tail channels.
    product=np.eye(N**strands,dtype=np.int64)
    for letter in word:
        factor=word_matrix([letter],plus,minus,strands,N,p)
        transformed=Ti@common_i@factor@common@T%p
        product=transformed@product%p
    assert np.array_equal(product,changed)
    return {"N":N,"strands":strands,"word":list(word),
            "all_common_frame_blocks":r*r,"correct_primitive_sector_source":int(source_after)}


def omitted_adapter_witness(N):
    p,_,q,*_=balanced_data(N)
    Q=q*q%p
    x=-3*pow(q,-1,p)%p

    def word_at(xx):
        data=core(N,xx,p,q)
        one,u,v,uq,vq,g,gi,C0,C1,D,Di,mul,tau=data
        R,_,_,_=color_matrices(N,p,q,xx)
        fac=[1]
        for a in range(1,N):fac.append(fac[-1]*(1-pow(Q,a,p))%p)
        diagonal=np.kron(fac,fac)
        diagonal_i=np.array([pow(int(t),-1,p) for t in diagonal])
        R=R*diagonal[:,None]*diagonal_i[None,:]%p
        C,Ci,*_=fusion(N,p,Q,[xx,xx],[0,0])
        a=Ci@R@C%p@one%p
        b=mul(mul(v,a),u)
        return data,b

    data,b=word_at(x)
    shifted_data,bs=word_at(q*x%p)
    one,u,v,uq,vq,g,gi,C0,C1,D,Di,mul,tau=data
    gs,gsi=shifted_data[5],shifted_data[6]
    correct=mul(mul(gsi,bs),gs)
    untransported=mul(mul(gi,bs),g)
    assert np.array_equal(correct,mul(mul(Di,untransported),D))
    good=tau(mul(C0,correct))
    wrong=tau(mul(C0,untransported))
    assert good!=wrong
    return {"N":N,"M":3,"field":p,"correct_source":int(good),
            "without_meridian_adapter":int(wrong)}


def symbolic_boundary():
    A,J,d=sp.symbols('A J d',nonzero=True)
    z=1-d
    D=J-A*J*d+(A-1)*d*d
    U=A*z*d*d/D
    V=J*D/(z*d*d)
    assert sp.cancel(U*V-A*J)==0
    assert sp.limit(U/d**2,d,0)==A/J
    assert sp.limit(V*d**2,d,0)==J**2
    e,s=sp.symbols('e s')
    shifted=1-sp.exp(2*sp.pi*sp.I*e)*(1-e*s)
    assert sp.limit(shifted/e,e,0)==s-2*sp.pi*sp.I
    return {"primitive_boundary_U_valuation":2,
            "adjacent_quantum_divisor_retained":True}


def main():
    clocks=[clock_case(N) for N in range(2,9)]
    words=[whole_word_case(3,2,(1,1,1)),
           whole_word_case(3,3,(1,-2,1,-2)),
           whole_word_case(4,3,(1,-2,1,-2)),
           whole_word_case(3,4,(1,-2,3,1,-2,3))]
    witnesses=[omitted_adapter_witness(N) for N in range(3,7)]
    result={"status":"PASS","clocks":clocks,"actual_words":words,
            "meridian_adapter_witnesses":witnesses,"symbolic":symbolic_boundary(),
            "scope":"Whole actual primitive source component, exact ordered clocks and meridian transport. No sector selection or knot-volume estimate."}
    Path(__file__).with_name('whole_word_primitive_source_gauge_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({"status":result['status'],"clock_levels":len(clocks),
                      "actual_words":len(words),"meridian_adapter_witnesses":witnesses}))


if __name__=='__main__':main()
