#!/usr/bin/env python3
"""Exact Laurent quantum-torus certificate for coupled physical Casimirs.

No q-Racah or skein identities are imported. Every equality is expanded
with Z_i S_i=q^2 S_i Z_i and commuting distinct physical heads.
"""
import json
from pathlib import Path


class P:
    def __init__(self, terms=None):
        self.t = {k: v for k, v in (terms or {}).items() if v}
    def __add__(self, other):
        if isinstance(other, int): other = mono(other)
        out = self.t.copy()
        for k, v in other.t.items(): out[k] = out.get(k, 0) + v
        return P(out)
    __radd__ = __add__
    def __neg__(self): return P({k: -v for k, v in self.t.items()})
    def __sub__(self, other): return self + (-other if isinstance(other, P) else -other)
    def __rsub__(self, other): return -self + other
    def __mul__(self, other):
        if isinstance(other, int): return P({k: other*v for k,v in self.t.items()})
        out = {}
        for a, av in self.t.items():
            for b, bv in other.t.items():
                k = list(x+y for x,y in zip(a,b))
                k[9] += 2*sum(a[2*i+1]*b[2*i] for i in range(3))
                k = tuple(k)
                out[k] = out.get(k,0)+av*bv
        return P(out)
    __rmul__ = __mul__


def mono(c=1, q=0, S=None, Z=None, M=None):
    k = [0]*10
    k[9] = q
    for i,a in (S or {}).items(): k[2*i] = a
    for i,a in (Z or {}).items(): k[2*i+1] = a
    for i,a in (M or {}).items(): k[6+i] = a
    return P({tuple(k):c})


zero, one = mono(0), mono()
q, qi = mono(q=1), mono(q=-1)
rho, delta = q-qi, q+qi


def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(2)),zero) for j in range(2)] for i in range(2)]


def trace(A): return q*A[0][0]+qi*A[1][1]


def mscale(c,A): return [[c*A[i][j] for j in range(2)] for i in range(2)]


def madd(A,B): return [[A[i][j]+B[i][j] for j in range(2)] for i in range(2)]


def certificate():
    L, Li, G, leaves = [], [], [], []
    for i in range(3):
        F = mono(S={i:1})-mono(q=2,S={i:1},Z={i:1})
        E = mono(S={i:-1},Z={i:-1},M={i:1})-mono(S={i:-1},M={i:-1})
        K = mono(-1,q=-1,Z={i:-1},M={i:1})
        Ki = mono(-1,q=1,Z={i:1},M={i:-1})
        lo = [[one,zero],[-K*F,K]]
        inv = [[one,zero],[F,Ki]]
        up = [[K,q*E],[zero,one]]
        L.append(lo);Li.append(inv);G.append(mm(inv,up))
        leaf = -mono(M={i:1})-mono(M={i:-1})
        assert not (trace(G[-1])-leaf).t
        leaves.append(leaf)
    H=[];prefix=[[one,zero],[zero,one]];pinv=prefix
    for i in range(3):
        H.append(mm(mm(pinv,G[i]),prefix))
        prefix=mm(L[i],prefix);pinv=mm(pinv,Li[i])
    A=trace(mm(H[1],H[0]));B=trace(mm(H[2],H[1]));C=trace(mm(H[2],H[0]))
    D=trace(mm(mm(H[2],H[1]),H[0]))
    a,b,c=leaves
    alpha=a*b+c*D;beta=b*c+a*D;gamma=a*c+b*D
    unit=[[one,zero],[zero,one]]
    H2inv=madd(mscale(qi*b,unit),mscale(-qi*qi,H[1]))
    H3inv=madd(mscale(qi*c,unit),mscale(-qi*qi,H[2]))
    hurwitz_B=trace(mm(mm(mm(H[2],H[1]),H[0]),H2inv))
    hurwitz_C=trace(mm(mm(mm(H[2],H[1]),H3inv),H[0]))
    identities = {
        'AB':qi*A*B-q*B*A-rho*(delta*C-gamma),
        'BC':qi*B*C-q*C*B-rho*(delta*A-alpha),
        'CA':qi*C*A-q*A*C-rho*(delta*B-beta),
        'central_DA':D*A-A*D,
        'central_DB':D*B-B*D,
        'central_DC':D*C-C*D,
        'Hurwitz_first':hurwitz_B-(q*gamma-q*B*A-q*q*C),
        'Hurwitz_second':hurwitz_C-(q*alpha-q*C*B-q*q*A),
        'cubic':qi*A*B*C+qi*qi*A*A+q*q*B*B+qi*qi*C*C
            -qi*A*alpha-q*B*beta-qi*C*gamma
            -(delta*delta-a*a-b*b-c*c-D*D-a*b*c*D),
    }
    for name,value in identities.items():
        assert not value.t,(name,len(value.t),next(iter(value.t.items())))
    return {'exact_Laurent_identities':list(identities),
            'formal_independent_meridians':3,
            'physical_trace_terms':{n:len(v.t) for n,v in zip(('A','B','C','D'),(A,B,C,D))},
            'all_remainders_zero':True}


def actual_sources():
    import numpy as np
    from audit_actual_twist_block_factorial_frame import matrices
    rows=[]
    for n in range(2,6):
        for M in (1.,1.05+.02j):
            q,Q,x,fac,Om,R=matrices(n,M);I=np.eye(n);V=np.eye(n**3)
            F=np.zeros((n,n),complex);E=np.zeros_like(F)
            for a in range(1,n):
                F[a,a-1]=1-Q**a;E[a-1,a]=M*Q**(-a)-1/M
            K=np.diag([x*Q**(-a) for a in range(n)]);Ki=np.linalg.inv(K)
            Ft=np.kron(np.kron(F,I),I)+np.kron(np.kron(Ki,F),I)+np.kron(np.kron(Ki,Ki),F)
            Et=np.kron(np.kron(E,K),K)+np.kron(np.kron(I,E),K)+np.kron(np.kron(I,I),E)
            Kt=np.kron(np.kron(K,K),K);D=Ft@Et+q*Kt+np.linalg.inv(Kt)/q
            A=np.kron(Om,I);B=np.kron(I,Om)
            R1=np.kron(R,I);R2=np.kron(I,R)
            R1i=np.kron(np.linalg.inv(R),I);R2i=np.kron(I,np.linalg.inv(R))
            C=R2@A@R2i;lam=-M-1/M;alpha=lam*lam*V+lam*D
            assert np.linalg.norm(R1@C@R1i-B)<2e-7
            assert np.linalg.norm(R1@B@R1i-(q*alpha-q*B@A-q*q*C))<2e-7
            assert np.linalg.norm(R2@C@R2i-(q*alpha-q*C@B-q*q*A))<2e-7
            previous,current=C.copy(),B.copy()
            for ell in range(1,5):
                following=-q*current@A-q*q*previous+q*alpha
                actual=np.linalg.matrix_power(R1,ell)@B@np.linalg.matrix_power(R1i,ell)
                assert np.linalg.norm(following-actual)<3e-6*max(1,np.linalg.norm(actual))
                previous,current=current,following
            if M==1:
                d=n-1
                cup=np.array([n*x**(-b) if a+b==d else 0 for a in range(n) for b in range(n)])
                embedding=np.kron(cup[:,None],I)
                assert np.linalg.norm((D+2*V)@embedding)<3e-7
                # All original marked turns are retained in a four-head plat.
                u=np.kron(cup,cup)
                pivot=np.array([x**(1-n)*Q**(-a) for a in range(n)])
                ordinary=np.array([x**b*pivot[a]/n if a+b==d else 0
                                   for a in range(n) for b in range(n)])
                marker=np.array([x**b/n**2 for a in range(n) for b in range(n)])
                source=np.kron(ordinary,marker)
                word=R2@R1i@R2@R2
                full=np.kron(word,I)
                residual=np.kron(D+2*V,I)
                assert abs(source@full@residual@u)<2e-6
            rows.append({'N':n,'M_real':float(complex(M).real),'M_imag':float(complex(M).imag),
                         'literal_adjacent_twist_automorphisms':True,
                         'all_four_coupled_twist_recurrences':True,
                         'original_complete_cup_total_Casimir_and_marked_source':M==1})
    return rows


def main():
    result={'status':'PASS','certificate':certificate(),'actual_sources':actual_sources(),
            'scope':'Exact bounded physical three-head quantum-character identities; no global selected cycle.'}
    Path(__file__).with_name('actual_adjacent_twist_character_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))


if __name__=='__main__':main()
