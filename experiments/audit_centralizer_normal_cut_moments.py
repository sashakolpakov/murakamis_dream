#!/usr/bin/env python3
"""Exact normal Cech, vertical-current and finite paired-moment identities."""

import json
from pathlib import Path

import sympy as S


def zero(x):
    assert S.cancel(x)==0


def normal_residue_and_clutch():
    eta,v,a,X,T,ep,V,ap=S.symbols('eta v a X T eta_prime V a_prime',nonzero=True)
    b=S.Symbol('b')
    records=[]
    for h in range(7):
        P=b**h
        north=-P.subs(b,-a/eta)/(eta*(1-eta*v))
        zero(S.residue(north,eta,0)+(-v*a)**h)
        delta=-(((1-X-T)/X)**h-(-T/X)**h)/(X*(1-X))
        Xi=0
        for r in range(1,h+1):
            for k in range(r):
                Xi-=S.binomial(h,r)*(-T)**(h-r)*S.binomial(r-1,k)*(-1)**k*X**(k-h)/S.Integer(k-h)
        zero(S.diff(Xi,X)-delta)
        assert S.denom(S.cancel(delta)).subs(X,1)!=0
        current=P.subs(b,-a/eta)/(1-eta*v)
        north_res=S.residue(current,eta,0)
        zero(north_res-(P.subs(b,-v*a)-P.subs(b,0))/v)
        south=(P.subs(b,-ap/ep-1))/(1+ep*V)
        south_res=S.residue(south,ep,0)
        zero(south_res+(P.subs(b,V*ap-1)-P.subs(b,-1))/V)
        # Convert the south residue one-form dV to its north dv coefficient.
        converted=-south_res.subs({V:1/v,ap:v-v*v*a})/(v*v)
        zero(converted-north_res-(P.subs(b,0)-P.subs(b,-1))/v)
        records.append({'moment_degree':h,'actual_normal_residue':True,
                        'explicit_global_Cech_primitive':True,
                        'both_vertical_current_endpoint_residues':True})
    f=S.Function('f')(v,v*a)
    P=(b+1)**3
    current=P.subs(b,-a/eta)*f/(1-eta*v)
    derivative=S.diff(current,a)
    fT=S.Subs(S.Derivative(S.Function('f')(v,T),T),T,v*a).doit()
    rhs=-(S.diff(P,b).subs(b,-a/eta)*f-eta*v*P.subs(b,-a/eta)*fT)/(eta*(1-eta*v))
    zero(derivative-rhs)
    return records


def trow(N,j,h):
    return (-1)**h*S.rf(j+1,h)/S.rf(N+1,h)


def exact_paired_current_map():
    b,t=S.symbols('b T')
    records=[]
    for N in range(2,10):
        n=N-1
        C=S.symbols(f'C0:{N}')
        for h in range(8):
            P=b**h
            for j in range(N):
                actual=N*S.binomial(n,j)*S.integrate((-t)**h*t**j*(1-t)**(n-j),(t,0,1))
                zero(actual-trow(N,j,h))
                reflected=sum(S.binomial(h,k)*(-1)**(h-k)*(-1)**k*trow(N,j,k) for k in range(h+1))
                # P(-1-b)=(-1-b)^h.
                zero(reflected-trow(N,n-j,h))
            lhs=(h*sum(trow(N,j,h-1)*C[j] for j in range(N))/N) if h else 0
            rhs=P.subs(b,0)*C[0]-P.subs(b,-1)*C[-1]
            rhs+=sum(trow(n,j,h)*(C[j+1]-C[j]) for j in range(n))
            zero(lhs-rhs)
        records.append({'source_dimension':N,'all_degree_test_Toeplitz_beta_moments':True,
                        'actual_Weyl_reflection':True,
                        'literal_paired_current_endpoints_and_degree_shift':True})
    return records


def covariant_symbol_map():
    t=S.Symbol('T')
    records=[]
    for N in range(2,9):
        n=N-1
        for h in range(n+1):
            Q=lambda j:(-1)**h*S.ff(j,h)/S.ff(n,h)
            symbol=sum(S.binomial(n,j)*Q(j)*t**j*(1-t)**(n-j) for j in range(N))
            zero(symbol-(-t)**h)
            if h:
                for j in range(n):
                    lower=h*(-1)**(h-1)*S.ff(j,h-1)/S.ff(n-1,h-1)
                    zero(lower+n*(Q(j+1)-Q(j)))
        records.append({'source_dimension':N,'covariant_symbol_and_degree_lowering':True,
                        'kept_separate_from_dual_Toeplitz':True})
    return records


def main():
    result={'normal_residue_global_clutch_and_current':normal_residue_and_clutch(),
            'actual_finite_dual_current_map':exact_paired_current_map(),
            'distinct_covariant_quantization':covariant_symbol_map(),
            'scope':'Actual framing normal/source moments and endpoints; no transverse critical-field or selected-cycle descent.'}
    out=Path(__file__).with_name('centralizer_normal_cut_moments_results.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'all_checks_passed':True,'moment_degrees':len(result['normal_residue_global_clutch_and_current']),
                      'dual_source_dimensions':len(result['actual_finite_dual_current_map']),
                      'output':str(out)},indent=2))


if __name__=='__main__':main()
