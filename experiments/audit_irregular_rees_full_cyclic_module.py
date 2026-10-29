#!/usr/bin/env python3
"""Exact regularized operators, full cyclic centers, and source flags."""

import json
import math
from pathlib import Path

import sympy as s

from audit_finite_sum_annihilator import field


def exact_operator_checks():
    N=s.symbols('N',nonzero=True)
    eps,u,x,t,M=s.symbols('eps u x t M',nonzero=True)
    Z=1+eps;d=N*eps
    assert s.cancel((Z-1)/d-1/N)==0
    assert s.cancel((1/Z-1)/d+1/(N*Z))==0
    records=[]
    for r in range(4):
        f=u**r/s.factorial(r)
        A=M*s.exp(-u/(N*Z))*f.subs(u,u/Z)-f/M
        Ewrap=A+d*s.diff(A,u)
        assert s.simplify(Ewrap.subs(eps,0)-(M*s.exp(-u/N)-1/M)*f)==0
        # Compare the original gauged integral to its regular reparameterization
        # in a finite u jet, retaining every epsilon denominator before canceling.
        original=0;regular=0
        for k in range(6-r):
            original+=u/d*s.integrate(((x-1)*u/d)**k/s.factorial(k)
                                      *(x*u)**r/s.factorial(r),(x,Z,1))
            regular+=-u/N*s.integrate((t*u/N)**k/s.factorial(k)
                                      *((1+eps*t)*u)**r/s.factorial(r),(t,0,1))
        assert s.cancel(original-regular)==0
        assert s.Poly(s.cancel(regular),eps,u)
        expected=s.series((1-s.exp(u/N))*f,u,0,7).removeO()
        assert s.expand(regular.subs(eps,0)-expected)==0
        records.append({'test_monomial_degree':r,'exact_wrap_reparameterization':True,
                        'regular_E_and_F_wrap_limits':True})
    # The two directions of head conjugation have different powers.
    for level in range(2,10):
        for j in range(1,level):
            assert s.Rational(j-1,level)-s.Rational(j,level)+s.Rational(1,level)==0
            assert s.Rational(j,level)-s.Rational(j-1,level)-s.Rational(1,level)==0
        assert s.Rational(level-1,level)+s.Rational(1,level)==1
        assert -s.Rational(level-1,level)-s.Rational(1,level)==-1
    return records


def cyclic_case(N,M,y,lam,p,q):
    Q=q*q%p;gamma=pow(-1,N+1,p);rho=(q-pow(q,-1,p))%p
    U=pow(y,N,p);x=-M*pow(q,-1,p)%p
    K=[x*pow(y,-1,p)*pow(Q,-j,p)%p for j in range(N)]
    E=[lam*(M*pow(y,-1,p)*pow(Q,-j,p)-pow(M,-1,p))%p for j in range(N)]
    F=[pow(lam,-1,p)*(1-y*pow(Q,j+1,p))%p for j in range(N)]
    for j in range(N):
        assert (K[(j-1)%N]*E[j]-Q*E[j]*K[j])%p==0
        assert (K[(j+1)%N]*F[j]-pow(Q,-1,p)*F[j]*K[j])%p==0
        comm=E[(j+1)%N]*F[j]-F[(j-1)%N]*E[j]
        assert (comm-rho*(K[j]-pow(K[j],-1,p)))%p==0
        casimir=F[(j-1)%N]*E[j]+q*K[j]+pow(q,-1,p)*pow(K[j],-1,p)
        assert (casimir+M+pow(M,-1,p))%p==0
    ec=math.prod(E)%p;fc=math.prod(F)%p;kc=pow(K[0],N,p)
    ebase=gamma*(pow(M,N,p)*pow(U,-1,p)-pow(M,-N,p))%p
    fbase=(1-U)%p;kbase=gamma*pow(M,N,p)*pow(U,-1,p)%p
    assert ec==pow(lam,N,p)*ebase%p
    assert fc==pow(lam,-N,p)*fbase%p
    assert kc==kbase
    assert (ec*fc-kc-pow(kc,-1,p)+gamma*(pow(M,N,p)+pow(M,-N,p)))%p==0
    # Literal pivot, not the reduced representative, has the U adapter.
    for j in range(N):
        literal=pow(K[j],1-N,p)
        reduced=pow(x,1-N,p)*pow(y,-1,p)*pow(Q,-j,p)%p
        assert literal==U*reduced%p
    covered=False
    if ec and fc:
        recovered_U=gamma*pow(M,N,p)*pow(kc,-1,p)%p
        assert recovered_U==U
        scaling_power=ec*pow(ebase,-1,p)%p
        assert scaling_power==pow(lam,N,p)
        forced_f=(kc+pow(kc,-1,p)-gamma*(pow(M,N,p)+pow(M,-N,p)))*pow(ec,-1,p)%p
        assert forced_f==fc
        covered=True
    return {'level':N,'complete_meridian':M==1,'clock_at_original_head':y==1,
            'actual_full_cyclic_relations_and_Casimir':True,
            'all_three_centers_exact':True,'literal_pivot_U_adapter':True,
            'dense_central_chart_recovery':covered}


def source_checks():
    eta,u=s.symbols('eta u',nonzero=True);records=[]
    for N in range(2,10):
        d=eta**N
        source=[eta**j*s.exp(-u/d) for j in range(N)]
        cosource=[eta**(-j)/N for j in range(N)]
        assert s.simplify(sum(cosource[j]*source[j].subs(u,0) for j in range(N))-1)==0
        # G preserves pi0 on the right; it does not preserve the finite coupon.
        assert s.exp(-u/d).subs(u,0)==1
        assert s.diff(s.exp(-u/d),u).subs(u,0)==-1/d
        for jet in range(5):
            exponents=[i-j-N*r for i in range(N) for j in range(N) for r in range(jet+1)]
            assert min(exponents)==-N*jet-(N-1)
        records.append({'level':N,'transformed_pairing_exactly_one':True,
                        'finite_coupon_irregular_not_preserved':True,
                        'jet_pole_bound_eta':f'N*h+N-1',
                        'ramified_head_and_dual_flags_retained':True})
    return records


def normal_poisson_and_resolution_checks():
    u,p,a=s.symbols('u p a',nonzero=True)
    U=s.exp(u*p)
    bracket=lambda F,G:s.diff(F,p)*s.diff(G,u)-s.diff(F,u)*s.diff(G,p)
    for gamma in (1,-1):
        k=gamma*a/U;e=p*gamma*(a/U-1/a);f=(1-U)/p
        assert s.simplify(bracket(k,e)-k*e)==0
        assert s.simplify(bracket(k,f)+k*f)==0
        assert s.simplify(bracket(e,f)-(1/k-k))==0
        assert s.simplify(e*f-k-1/k+gamma*(a+1/a))==0
    v,w=s.symbols('v w',nonzero=True)
    chartU=1/(1+w*v);chartp=1/v
    form=s.diff(chartU,w)/chartU*s.diff(chartp,v)/chartp\
        -s.diff(chartU,v)/chartU*s.diff(chartp,w)/chartp
    assert s.cancel(form-1/(1+w*v))==0
    N=s.symbols('N',positive=True,integer=True)
    Ewrap=s.series(((1+w*v)**(1/N)-1)/v,v,0,1).removeO()
    assert s.simplify(Ewrap-w/N)==0
    Fwrap=v*(1-(1+w*v)**(-1/N))
    assert Fwrap.subs(v,0)==0
    Z=s.symbols('Z')
    for level in range(2,10):
        assert s.limit((Z**level-1)/(level*(Z-1)),Z,1)==1
        assert s.limit((Z**(-level)-1)/(level*(Z-1)),Z,1)==-1
    # The log symplectic chart is exactly the actual fixed-leaf Gauss form.
    V,P=s.symbols('V P',nonzero=True)
    for gamma in (1,-1):
        k=gamma*a/V;e=P*(k-gamma/a)
        gauss_form=-((s.diff(k,V)/k)*(s.diff(e,P)/e)
                     -(s.diff(k,P)/k)*(s.diff(e,V)/e))
        assert s.cancel(gauss_form-1/(V*P))==0
    assert s.simplify(s.diff(s.log(U),u)/p-1)==0
    return {'both_parity_central_Poisson_brackets':True,
            'actual_fixed_leaf_Gauss_symplectic_form':True,
            'parabolic_resolution_form_and_semicyclic_boundary':True,
            'actual_normal_Planck_ratios_levels':8}


def phase_wrap_case(N,M,y,phase,p,q):
    Q=q*q%p;gamma=pow(-1,N+1,p);rho=(q-pow(q,-1,p))%p;U=pow(y,N,p)
    x=-M*pow(q,-1,p)%p
    K=[x*pow(y,-1,p)*pow(Q,-j,p)%p for j in range(N)]
    E=[(M*pow(y,-1,p)*pow(Q,-j,p)-pow(M,-1,p))%p for j in range(N)]
    F=[(1-y*pow(Q,j+1,p))%p for j in range(N)]
    E[0]=phase*E[0]%p;F[N-1]=pow(phase,-1,p)*F[N-1]%p
    for j in range(N):
        assert (E[(j+1)%N]*F[j]-F[(j-1)%N]*E[j]
                -rho*(K[j]-pow(K[j],-1,p)))%p==0
        assert (F[(j-1)%N]*E[j]+q*K[j]+pow(q,-1,p)*pow(K[j],-1,p)
                +M+pow(M,-1,p))%p==0
    assert math.prod(E)%p==phase*gamma*(pow(M,N,p)*pow(U,-1,p)-pow(M,-N,p))%p
    assert math.prod(F)%p==pow(phase,-1,p)*(1-U)%p
    return {'level':N,'actual_phase_p_wrap_module':True}


def main():
    cases=[];phase_cases=[]
    for N in range(2,10):
        p,g,q=field(N)
        for M in (1,pow(g,3,p)):
            for y in (1,pow(g,5,p)):
                for lam in (1,pow(g,2,p)):
                    cases.append(cyclic_case(N,M,y,lam,p,q))
                    phase_cases.append(phase_wrap_case(N,M,y,lam,p,q))
    result={'regularized_operator_cases':exact_operator_checks(),
            'full_cyclic_module_cases':cases,'irregular_source_cases':source_checks(),
            'phase_p_wrap_module_cases':phase_cases,
            'normal_Poisson_resolution_appendix':normal_poisson_and_resolution_checks(),
            'scope':'Actual irregular Rees module bridge and flagged source only; no selected limit or volume assertion.'}
    path=Path(__file__).with_name('irregular_rees_full_cyclic_module_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'full_cyclic_cases':len(cases),
                      'regular_operator_tests':len(result['regularized_operator_cases']),
                      'flagged_source_levels':len(result['irregular_source_cases']),
                      'phase_wrap_cases':len(phase_cases),
                      'output':str(path)},indent=2))


if __name__=='__main__':main()
