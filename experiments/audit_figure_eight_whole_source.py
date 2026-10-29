#!/usr/bin/env python3
"""Actual colored 4-plat source contraction and its finite binomial collapse.

Mixed R entries are evaluated from the original E matrices and Cartan
diagonal, independently of the simplified surviving-route expression.
The knot source is a literal highest-weight matrix entry, implemented
with the correct left pivotal trace. No Jones formula is used.
"""

from functools import cache
import json
from pathlib import Path

import sympy as s

from audit_finite_sum_annihilator import field, cut_entry_by_paths


ACTION_WORD=((1,1),(0,-1),(1,1),(1,1))


class MixedEntries:
    def __init__(self,N,p,q):
        self.N=N;self.p=p;self.q=q;self.Q=q*q%p
        rho=(q-pow(q,-1,p))%p
        self.rho=rho
        self.integers=[0]+[(pow(q,j,p)-pow(q,-j,p))*pow(rho,-1,p)%p
                           for j in range(1,N)]
        self.qfact=[1];self.F=[1]
        for j in range(1,N):
            self.qfact.append(self.qfact[-1]*self.integers[j]%p)
            self.F.append(self.F[-1]*(1-pow(self.Q,j,p))%p)

    @cache
    def E(self,x,a):
        if a == 0:return 0
        return self.integers[a]*(x*pow(self.q,1-a,self.p)
                                -pow(x,-1,self.p)*pow(self.q,a-1,self.p))\
            *pow(self.rho,-1,self.p)%self.p

    @cache
    def direct(self,x1,x2,a,b,k,sign):
        """Original coefficient first, then the literal factorial basis change."""
        p=self.p;q=self.q;Q=self.Q
        ec=1
        start=a if sign>0 else b
        color=x1 if sign>0 else x2
        for j in range(k):ec=ec*self.E(color,start-j)%p
        universal=pow(self.rho,k,p)*pow(self.qfact[k],-1,p)%p
        if sign>0:
            universal=universal*pow(q,k*(k-1)//2,p)%p
            out=(b+k,a-k)
            cartan=pow(x1,-b-k,p)*pow(x2,-a+k,p)*pow(Q,(a-k)*(b+k),p)%p
        else:
            universal=universal*pow(-1,k,p)*pow(q,-k*(k-1)//2,p)%p
            out=(b-k,a+k)
            cartan=pow(x1,b,p)*pow(x2,a,p)*pow(Q,-a*b,p)%p
        basis=self.F[out[0]]*self.F[out[1]]*pow(self.F[a]*self.F[b]%p,-1,p)%p
        return universal*ec*cartan*basis%p

    def gaussian(self,n,k):
        return self.F[n]*pow(self.F[k]*self.F[n-k]%self.p,-1,self.p)%self.p

    def pochhammer(self,z,k):
        value=1
        for j in range(k):value=value*(1-z*pow(self.Q,j,self.p))%self.p
        return value

    def formula(self,x1,x2,a,b,k,sign):
        p=self.p;Q=self.Q
        if sign>0:
            phase=pow(-1,k,p)*pow(x1,-b-2*k,p)*pow(x2,-a+k,p)\
                  *pow(Q,a*b+(a-b)*k-k*(k+1)//2,p)%p
            return phase*self.gaussian(b+k,k)\
                *self.pochhammer(Q*x1*x1*pow(Q,-a,p)%p,k)%p
        phase=pow(x1,b,p)*pow(x2,a-k,p)*pow(Q,-a*b,p)%p
        return phase*self.gaussian(a+k,k)\
            *self.pochhammer(Q*x2*x2*pow(Q,-b,p)%p,k)%p


def calibration(N,p,Q,Y):
    value=term=1
    for k in range(1,N):
        term=term*(Y+pow(Y,-1,p)-pow(Q,k,p)-pow(Q,-k,p))%p
        value=(value+term)%p
    return value


def literal_plat(entries,x):
    """All finite paths, actual cups/caps, and D0=g E00 on the fourth leg."""
    N=entries.N;p=entries.p;Q=entries.Q
    xv=pow(x,-1,p)*pow(Q,-1,p)%p
    g0=pow(x,1-N,p)
    # coev_R(x), at dual index N-1 and primal index 0, is exactly N.
    second_cup=N*pow(x,-(N-1),p)*pow(g0,-1,p)%p
    assert second_cup == N%p
    total=0;survivors=[]
    for a in range(N):
        initial=(a,N-1-a,N-1,0)
        first_cup=N*pow(x,-(N-1-a),p)%p
        weight=first_cup*second_cup*g0%p
        paths=[(initial,(),weight)]
        colors=[x,xv,xv,x]
        for position,sign in ACTION_WORD:
            next_paths=[]
            x1,x2=colors[position:position+2]
            for state,route,previous in paths:
                aa,bb=state[position:position+2]
                maximum=min(aa,N-1-bb) if sign>0 else min(bb,N-1-aa)
                for k in range(maximum+1):
                    coefficient=entries.direct(x1,x2,aa,bb,k,sign)
                    if not coefficient:continue
                    out=(bb+k,aa-k) if sign>0 else (bb-k,aa+k)
                    new=state[:position]+out+state[position+2:]
                    next_paths.append((new,route+(k,),previous*coefficient%p))
            paths=next_paths
            colors[position],colors[position+1]=colors[position+1],colors[position]
        assert colors == [xv,x,xv,x]
        for state,route,previous in paths:
            if state[0]+state[1] != N-1 or state[2]+state[3] != N-1:continue
            assert route[0] == 0 and route[2] == a and route[3] == 0
            k=route[1]
            assert a+k<N
            cap1=pow(x,state[0],p)*pow(N,-1,p)%p
            cap2=pow(x,state[2],p)*pow(N,-1,p)%p
            # Full colored Cartan scalar, using the actual unrolled dual lift.
            cartan_scalar=pow(xv,N-1,p)
            actual=previous*cap1*cap2*cartan_scalar%p
            Y=Q*x*x%p
            predicted=pow(Y,k-a,p)*entries.gaussian(a+k,k)\
                *entries.pochhammer(Q*pow(Y,-1,p)%p,k)\
                *entries.pochhammer(Y*pow(Q,-a-k,p)%p,a)%p
            assert actual == predicted,(N,a,k,actual,predicted)
            total=(total+actual)%p
            survivors.append((a,k))
    return total,len(survivors)


def exact_crossing_checks():
    count=0
    for N in range(2,7):
        p,g,q=field(N);entries=MixedEntries(N,p,q);Q=q*q%p
        for M in (1,pow(g,3,p)):
            x=-M*pow(q,-1,p)%p;xv=pow(x,-1,p)*pow(Q,-1,p)%p
            for x1,x2 in ((x,xv),(xv,x),(xv,xv)):
                for a in range(N):
                    for b in range(N):
                        for sign in (-1,1):
                            maximum=min(a,N-1-b) if sign>0 else min(b,N-1-a)
                            for k in range(maximum+1):
                                assert entries.direct(x1,x2,a,b,k,sign) == entries.formula(x1,x2,a,b,k,sign)
                                count+=1
    return count


def topology_and_cartan():
    T=s.Matrix([[1,1],[0,1]]);U=s.Matrix([[1,0],[1,1]])
    image=T*T*U*T*s.Matrix([0,1])
    assert image == s.Matrix([5,2])
    assert T*U.inv()*T == U.inv()*T*U.inv()
    A,N=s.symbols('A N');B=2*(N-1)-A
    labels=[A,B,B,A];orientations=[1,-1,-1,1]
    cartan=0;writhe=0
    for position,sign in ACTION_WORD:
        cartan+=sign*labels[position]*labels[position+1]/2
        writhe+=sign*orientations[position]*orientations[position+1]
        labels[position],labels[position+1]=labels[position+1],labels[position]
        orientations[position],orientations[position+1]=orientations[position+1],orientations[position]
    assert s.expand(cartan-(N-1)*B) == 0
    assert writhe == 0
    return {'rational_tangle_slope':[5,2], 'oriented_writhe':0,
            'full_Cartan_exponent':'(N-1)*alpha_dual',
            'left_trace_coupon':'D0=g E00; Tr(g^{-1} D0 C)=C00'}


def symbolic_binomial_collapse():
    Q,Y=s.symbols('Q Y',nonzero=True)
    def poch(z,k):return s.prod(1-z*Q**j for j in range(k))
    checks=[]
    for n in range(7):
        F=[poch(Q,k) for k in range(n+1)]
        left=sum(Y**(2*k-n)*F[n]/(F[k]*F[n-k])
                 *poch(Q/Y,k)*poch(Y*Q**-n,n-k) for k in range(n+1))
        right=(-1)**n*Q**(-n*(n+1)//2)*poch(Y*Q,n)*poch(Q/Y,n)
        assert s.cancel(left-right) == 0
        checks.append({'n':n,'whole_rational_binomial_identity_exact':True})
    return checks


def main():
    crossings=exact_crossing_checks();cases=[]
    for N in range(2,13):
        p,g,q=field(N);Q=q*q%p
        for M in (1,pow(g,2,p),pow(g,3,p)):
            entries=MixedEntries(N,p,q);x=-M*pow(q,-1,p)%p;Y=M*M%p
            actual,survivors=literal_plat(entries,x)
            expected=calibration(N,p,Q,Y)
            assert actual == expected
            three_braid=None
            if N<=7:
                three_braid=cut_entry_by_paths(N,p,q,x,3,[(0,1),(1,-1)]*2)
                assert actual == three_braid
            cases.append({'level':N,'meridian':M,'literal_plat':actual,
                          'surviving_transfer_pairs':survivors,
                          'actual_three_braid_compared':three_braid is not None})
    result={'topology_and_normalization':topology_and_cartan(),
            'independent_mixed_R_coefficient_checks':crossings,
            'literal_source_cases':cases,
            'symbolic_binomial_checks':symbolic_binomial_collapse(),
            'scope':'Exact all-N figure-eight source identity; prototype for general bridge elimination.'}
    output=Path(__file__).with_name('figure_eight_whole_source_results.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'mixed_R_entries':crossings,'literal_source_cases':len(cases),
                      'actual_three_braid_comparisons':sum(c['actual_three_braid_compared'] for c in cases),
                      'symbolic_binomial_checks':len(result['symbolic_binomial_checks']),
                      'output':str(output)},indent=2))


if __name__ == '__main__':main()
