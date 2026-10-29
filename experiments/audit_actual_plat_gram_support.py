#!/usr/bin/env python3
"""Original whole plat source, positive cup/cap rays and actual constraints."""
import itertools
import json
from pathlib import Path
import numpy as np

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_two_cut_ports import word_matrix
from audit_actual_bounded_quantum_meridians import initial_meridians,nielsen_substitution,evaluate


def tensor(xs):
    out=np.array([1],dtype=np.int64)
    for x in xs:out=np.kron(out,x)
    return out


def source_vectors(H,k,marked):
    N,p,x,d=H.N,H.p,H.x,H.N-1
    cup=np.zeros(N*N,dtype=np.int64);cupbar=cup.copy();cap=cup.copy();mark=cup.copy()
    for i,j in itertools.product(range(N),repeat=2):
        mark[i*N+j]=pow(x,j,p)*pow(N,-2,p)%p
        if i+j==d:
            cup[i*N+j]=N*pow(x,-j,p)%p
            cupbar[i*N+j]=N*pow(x,j,p)%p
            cap[i*N+j]=pow(x,j,p)*int(H.pivot[i])*pow(N,-1,p)%p
    u=tensor([cup]*k)%p;ubar=tensor([cupbar]*k)%p
    ell=tensor([mark if r==marked else cap for r in range(k)])%p
    G=[]
    for state in itertools.product(range(N),repeat=2*k):
        v=1
        for r in range(k):
            if r!=marked:v=v*int(H.pivot[state[2*r]])%p
        G.append(v)
    return u,ubar,ell,np.array(G,dtype=np.int64)


def finite_case(N,k,word,marked):
    H=HardyNetwork(N,1);p=H.p;b=2*k;D=N**b
    W=word_matrix(word,H.plus,H.minus,b,N,p)
    Wi=word_matrix([-j for j in word[::-1]],H.plus,H.minus,b,N,p)
    u,ubar,ell,G=source_vectors(H,k,marked)
    out=W@u%p
    old=int(ell@out)%p
    new=int((ubar*G%p)@out)*pow(N,-2*k-1,p)%p
    assert old==new
    assert int(ubar@u)%p==pow(N,3*k,p)
    # Only the assembled integer degree justifies the marked-cap restriction.
    for index,value in enumerate(out):
        if value:
            state=[];t=index
            for _ in range(b):state.append(t%N);t//=N
            assert sum(state)==k*(N-1)
    heads=initial_meridians(H,b);I=np.eye(2*D,dtype=np.int64)
    auxu=np.kron(np.eye(2,dtype=np.int64),u[:,None])
    auxout=np.kron(np.eye(2,dtype=np.int64),out[:,None])
    images=[[j+1] for j in range(b)]
    for letter in word:images=nielsen_substitution(images,letter)
    for r in range(k):
        A=(heads[2*r+1][0]@heads[2*r][0]-I)%p
        assert not np.any(A@auxu%p)
        Aout=(evaluate(images[2*r+1],heads,H,p)@evaluate(images[2*r],heads,H,p)-I)%p
        assert not np.any(Aout@auxout%p)
        assert np.array_equal(np.kron(np.eye(2,dtype=np.int64),W)@A%p,
                              Aout@np.kron(np.eye(2,dtype=np.int64),W)%p)
    total=I.copy()
    for j in range(b):total=heads[j][0]@total%p
    assert not np.any((total-I)@auxu%p)
    assert not np.any((total-I)@auxout%p)
    # Same arbitrary original external line on both exact source evaluations.
    writhe=sum(1 if j>0 else -1 for j in word)
    chi=H.dimension*pow(H.twist,-writhe,p)%p
    return {'N':N,'cups':k,'marked_pair':marked,'word':word,
            'same_original_full_marked_scalar':old,
            'same_scalar_with_retained_external_line':chi*old%p,
            'whole_integer_degree_before_restriction':k*(N-1),
            'exact_cup_and_transported_pair_constraints':k,
            'exact_preserved_total_product':True}


def source_restriction_scope():
    rows=[]
    for N in range(2,9):
        H=HardyNetwork(N,1);p=H.p;u,ubar,ell,G=source_vectors(H,1,0)
        # One bounded degree-minus-one endpoint coupon. This is deliberately
        # outside the conserved whole-word source theorem.
        out=np.zeros(N*N,dtype=np.int64);out[N-2]=u[N-1]
        old=int(ell@out)%p;restricted=int(ubar@out)*pow(N,-3,p)%p
        assert old==pow(H.x,-1,p)*pow(N,-1,p)%p and old and restricted==0
        rows.append({'N':N,'degree_minus_one_coupon_old_source':old,
                     'restricted_source':restricted,'scope_difference_retained':True})
    return rows


def complex_cap_support(N,k,marked):
    q=np.exp(np.pi*1j/N);Q=q*q;x=-1/q;b=2*k;D=N**b;d=N-1
    shape=(N,)*b
    coeff={
        'K':np.array([x*Q**(-a) for a in range(N)]),
        'Ki':np.array([Q**a/x for a in range(N)]),
        'f':np.array([0]+[1-Q**a for a in range(1,N)]),
        'e':np.array([1/x-x*Q**(-a) for a in range(N-1)]+[0])}
    def local(v,j,op):
        t=v.reshape(shape);dims=[1]*b;dims[j]=N
        if op=='f':t=np.roll(t,1,axis=j)
        elif op=='e':t=np.roll(t,-1,axis=j)
        return (t*coeff[op].reshape(dims)).reshape(D)
    def lm(v,j):
        a,c=v
        return (a,-local(local(a,j,'f'),j,'K')+local(c,j,'K'))
    def li(v,j):
        a,c=v
        return (a,local(a,j,'f')+local(c,j,'Ki'))
    def lp(v,j):
        a,c=v
        return (local(a,j,'K')+local(c,j,'e'),c)
    def head(v,j):
        for t in range(j):v=lm(v,t)
        v=li(lp(v,j),j)
        for t in range(j-1,-1,-1):v=li(v,t)
        return v
    cup=np.zeros(N*N,complex)
    for j in range(N):cup[(d-j)*N+j]=x**(-j)/np.sqrt(N)
    u=np.array([1],complex)
    for _ in range(k):u=np.kron(u,cup)
    assert abs(np.linalg.norm(u)-1)<1e-10
    phi=u.copy()
    g=np.array([x**(1-N)*Q**(-a) for a in range(N)])
    for r in range(k):
        if r!=marked:
            dims=[1]*b;dims[2*r]=N
            phi=(phi.reshape(shape)*g.conjugate().reshape(dims)).reshape(D)
    assert abs(np.linalg.norm(phi)-1)<1e-10
    cup_error=cap_error=0.
    for r in range(k):
        for v in (u,phi):
            for aux in range(2):
                initial=(v,np.zeros(D,complex)) if aux==0 else (np.zeros(D,complex),v)
                output=head(head(initial,2*r),2*r+1)
                err=max(np.linalg.norm(output[j]-initial[j]) for j in range(2))
                if v is u:cup_error=max(cup_error,float(err))
                else:cap_error=max(cap_error,float(err))
    assert cup_error<1e-9
    # The proof gives a fixed-diagram commutator bound; this numerical
    # check reports its directly observed N-rescaled value, not a fit.
    assert cap_error<=100/N+1e-9
    return {'N':N,'cups':k,'marked_pair':marked,'exact_cup_numerical_residual':cup_error,
            'top_cap_residual_norm':cap_error,'N_times_top_cap_residual':N*cap_error,
            'top_cap_mean_square_bound_observed':cap_error**2,
            'original_source_polynomial_normalization':N**(k-1)}


def main():
    cases=[(2,1,[1,1,-1],0),(3,1,[-1,1,1],0),
           (2,2,[2,2,2],0),(3,2,[2,2,2],0),
           (2,2,[2,-1,2,-1],1),(3,2,[2,-1,2,-1],1),
           (2,3,[2,4,-3,2,1],0)]
    out={'original_whole_source_and_exact_ket_constraints':[finite_case(*v) for v in cases],
         'marked_restriction_does_not_apply_to_arbitrary_coupons':source_restriction_scope(),
         'complex_positive_cap_mean_square_support':
             [complex_cap_support(N,2,marked) for N in (2,3,4,8,12,16) for marked in (0,1)],
         'scope':'exact original scalar cup/cap rays and separate honest support loci; '
                 'no nonzero overlap measure, exponential overlap or atomic regulator claim'}
    Path(__file__).with_name('audit_actual_plat_gram_support_results.json').write_text(
        json.dumps(out,indent=2)+'\n')
    print('PASS seven ORIGINAL marked plats/exact transported cup and total constraints; '
          'seven coupon-scope witnesses and 12 complex cap mean-square scales')


if __name__=='__main__':main()
