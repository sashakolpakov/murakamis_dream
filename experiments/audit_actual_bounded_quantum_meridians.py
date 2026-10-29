#!/usr/bin/env python3
"""Uniform physical-meridian transport via exact actual Nielsen words."""
import json
from pathlib import Path
import numpy as np

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_two_cut_ports import balanced_data,word_matrix


def embed(A,j,b,N):
    out=np.array([[1]],dtype=np.int64)
    for k in range(b):out=np.kron(out,A if k==j else np.eye(N,dtype=np.int64))
    return out


def initial_meridians(H,b):
    N,p,q,Q=H.N,H.p,H.q,H.Q
    _,_,_,E,F,K,_,_,_=balanced_data(N)
    rho=(q-pow(q,-1,p))%p;e=q*rho*rho*E%p
    size=N**b;I=np.eye(size,dtype=np.int64);Z=np.zeros_like(I)
    IA=np.eye(2*size,dtype=np.int64);prefix=IA.copy();pi=IA.copy();answer=[]
    c=(pow(H.x,-1,p)+Q*H.x)%p
    for j in range(b):
        kk,ee,ff=embed(K,j,b,N),embed(e,j,b,N),embed(F,j,b,N)
        ki=np.diag([pow(int(v),-1,p) for v in np.diag(kk)]).astype(np.int64)
        lm=np.block([[I,Z],[-kk@ff%p,kk]])%p
        li=np.block([[I,Z],[ff,ki]])%p
        lp=np.block([[kk,ee],[Z,I]])%p
        G=li@lp%p
        A=pi@G%p@prefix%p
        Ai=(c*IA-A)*pow(Q,-1,p)%p
        assert np.array_equal(A@Ai%p,IA) and np.array_equal(Ai@A%p,IA)
        answer.append((A,Ai))
        prefix=lm@prefix%p;pi=pi@li%p
    return answer


def reduce_word(word):
    out=[]
    for j in word:
        if out and out[-1]==-j:out.pop()
        else:out.append(j)
    return out


def nielsen_substitution(images,letter):
    i=abs(letter);rules={}
    if letter>0:rules={i:[i+1],i+1:[i+1,i,-i-1]}
    else:rules={i:[-i,i+1,i],i+1:[i]}
    out=[]
    for image in images:
        word=[]
        for j in image:
            replacement=rules.get(abs(j),[abs(j)])
            word+=(replacement if j>0 else [-v for v in replacement[::-1]])
        out.append(reduce_word(word))
    return out


def evaluate(images,head,H,p):
    out=np.eye(len(head[0][0]),dtype=np.int64)
    for j in images:out=out@head[abs(j)-1][j<0]%p
    return out


def signed_prefix_case(N,b,word):
    H=HardyNetwork(N,1);p=H.p;head=initial_meridians(H,b)
    images=[[j+1] for j in range(b)];checked=0;maxlen=1
    for t,letter in enumerate(word,1):
        images=nielsen_substitution(images,letter)
        W=word_matrix(word[:t],H.plus,H.minus,b,N,p)
        Wi=word_matrix([-j for j in word[:t][::-1]],H.plus,H.minus,b,N,p)
        W=np.kron(np.eye(2,dtype=np.int64),W);Wi=np.kron(np.eye(2,dtype=np.int64),Wi)
        for j in range(b):
            expected=evaluate(images[j],head,H,p)
            assert np.array_equal(W@head[j][0]%p@Wi%p,expected)
            checked+=1;maxlen=max(maxlen,len(images[j]))
        assert maxlen<=3**t
    return {'N':N,'width':b,'word':word,'original_full_Cartan_prefix_meridians':checked,
            'largest_reduced_Nielsen_length':maxlen,'coarse_initial_bound':9**b,
            'polynomial_inverse_checked':True}


def complex_star_checks():
    rows=[]
    for N in (2,3,5,8,16,32,64):
        q=np.exp(np.pi*1j/N);Q=q*q;x=-1/q
        K=np.diag([x*Q**(-a) for a in range(N)])
        e=np.zeros((N,N),complex);f=e.copy()
        for a in range(N-1):
            f[a+1,a]=1-Q**(a+1);e[a,a+1]=1/x-x*Q**(-a)
        Ki=K.conj().T
        assert np.linalg.norm(e.conj().T-x*f,2)<1e-11
        assert np.linalg.norm(f.conj().T-x*e,2)<1e-11
        assert np.linalg.norm(e,2)<=2+1e-11 and np.linalg.norm(f,2)<=2+1e-11
        assert np.linalg.norm(K@e-Q*e@K,2)<1e-11
        assert np.linalg.norm(K@f-(1/Q)*f@K,2)<1e-11
        assert np.linalg.norm(e@f-f@e-(Q-1)*(K-Ki),2)<1e-10
        mats=[K,Ki,e,f,e.conj().T,f.conj().T]
        largest=max(np.linalg.norm(a@b-b@a,2) for a in mats for b in mats)
        assert largest<=8*abs(Q-1)+1e-10
        rows.append({'N':N,'exact_actual_star_relations':True,
                     'largest_basic_star_commutator':float(largest),
                     'N_times_largest_commutator':float(N*largest),
                     'proved_uniform_commutator_bound':float(8*abs(Q-1))})
    return rows


def main():
    cases=[(N,2,[1,1,-1,1,-1]) for N in range(2,8)]
    cases += [(2,3,[1,-2,1,-2]),(3,3,[1,-2,1,-2]),
              (4,3,[1,-2,1,-2]),(3,3,[1,1,1,2,-1,2]),
              (2,4,[1,2,-3,2,-1,3])]
    out={'actual_signed_prefixes':[signed_prefix_case(*case) for case in cases],
         'complex_flat_star_and_commutator_bounds':complex_star_checks(),
         'scope':'uniform N-independent actual Heisenberg physical-meridian transport; '
                 'compact Gram braidgraph support, not original closure or joint atom-shape support'}
    Path(__file__).with_name('audit_actual_bounded_quantum_meridians_results.json').write_text(
        json.dumps(out,indent=2)+'\n')
    print('PASS 11 actual signed word families/all prefixes and polynomial inverses; '
          'seven actual complex star/commutator scales through N64')


if __name__=='__main__':main()
