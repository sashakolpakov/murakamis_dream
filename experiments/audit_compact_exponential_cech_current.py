#!/usr/bin/env python3
"""Universal Cech, matrix and finite-source current identities."""

import json
from pathlib import Path

import sympy as S


def zero(expr):
    assert S.simplify(S.expand_power_exp(expr)) == 0


def matrix_family():
    v,u,h,m,p,s = S.symbols('v u h M p s', nonzero=True)
    mu = S.Matrix([[u,(1-u)/v],[v*(u-h),1+h-u]])
    zero(mu.det()-h)
    assert (mu*S.Matrix([1,v])-S.Matrix([1,v])).applyfunc(S.simplify)==S.zeros(2,1)
    target=S.Matrix([[m+s,-(m-1/m+s)*p],[s/p,1/m-s]])
    actual=(mu/m).subs({h:m*m,v:1/p})
    assert (actual-target.subs(s,(u-m*m)/m)).applyfunc(S.simplify)==S.zeros(2)
    eta_n=(1-u)/v
    eta_s=v*(u-h)
    zero(eta_s-((1-h)*v-v*v*eta_n))
    return {'determinant_and_retained_flag':True,
            'actual_inverse_flag_meridian_convention':True,
            'affine_Cech_transition':True}


def exponential_chart_and_normal():
    c,lam,v,a,k=S.symbols('c lam v a k',nonzero=True)
    t=v*a;h=S.exp(-c*lam);u=S.exp(-c*lam*t)
    f=(1-u)/((1-h)*v)
    V=1/v;ap=v-v*v*a
    fs=h*(S.exp(c*lam*V*ap)-1)/((1-h)*V)
    zero(fs-(v-v*v*f))
    j=c*lam*u/(1-h)
    zero(S.diff(f,a)-j)
    # d[-(f-a)dv] has coefficient d_a(f-a).
    zero(S.diff(f-a,a)-(j-1))
    u0=S.exp(-c*t)
    f_normal=(1-u0*(1-k)**t)/(k*v)
    j_normal=(c-S.log(1-k))*u0*(1-k)**t/k
    f_constant=S.expand(S.series(f_normal,k,0,1).removeO())
    j_constant=S.expand(S.series(j_normal,k,0,1).removeO())
    zero(f_constant-((1-u0)/(k*v)+a*u0))
    zero(j_constant-(c*u0/k+u0*(1-c*t)))
    eta=(1-u0)/v
    zero(S.diff(eta,a)-c*u0)
    zero(-S.diff(a*(1-u0),a)-(u0*(1-c*t)-1))
    return {'whole_source_chart_gluing':True,
            'global_identity_current_primitive':True,
            'complete_normal_pole_and_finite_part':True}


def finite_matrix_currents():
    v,a,b,F,V,ap,Fp=S.symbols('v a b F V ap Fp',nonzero=True)
    fa=S.Function('F')(v,a)
    records=[]
    for n in range(1,5):
        for i in range(n+1):
            for j in range(n+1):
                f=S.binomial(n,j)*v**i*b**j*(1-v*b)**(n-j)
                anti=S.integrate(S.expand(f),b)
                current=anti.subs(b,fa)-anti.subs(b,a)
                zero(S.diff(current,a)-f.subs(b,fa)*S.diff(fa,a)+f.subs(b,a))
                # The antiderivative has degree <=N, hence pole <=N.
                assert S.Poly(anti,b).degree()<=n+1
                fs=f.subs({v:1/V,b:V-V*V*b})
                antis=S.integrate(S.expand(fs),b)
                north=anti.subs(b,F)-anti.subs(b,a)
                south=(antis.subs(b,Fp)-antis.subs(b,ap)).subs(
                    {V:1/v,ap:v-v*v*a,Fp:v-v*v*F})
                zero(south+v*v*north)
                # Exact actual support-cone homotopy, including its endpoint sign.
                beta_a=S.integrate(S.expand(f),v)
                beta_a=beta_a-beta_a.subs(v,0)
                beta_anti=S.integrate(S.expand(beta_a),b)
                kb=beta_anti.subs(b,fa)-beta_anti.subs(b,a)
                source_current=anti.subs(b,fa)-anti.subs(b,a)
                zero(-source_current+S.diff(kb,v)-beta_a.subs(b,fa)*S.diff(fa,v))
                zero(S.diff(kb,a)-beta_a.subs(b,fa)*S.diff(fa,a)+beta_a.subs(b,a))
                assert S.Poly(beta_anti,b).degree()<=n+1
            # Exact diagonal finite trace after arbitrary endpoint-preserving path.
            zero(S.binomial(n,i)*S.integrate(b**i*(1-b)**(n-i),(b,0,1))-S.Rational(1,n+1))
        records.append({'matrix_size':n+1,'all_matrix_units_current_and_gluing':True,
                        'actual_relative_support_cone_homotopy':True,
                        'normal_pole_bound':n+1,'normalized_trace_endpoints':True})
    return records


def main():
    result={'matrix_detour':matrix_family(),
            'whole_chart_and_normal':exponential_chart_and_normal(),
            'actual_finite_source_current':finite_matrix_currents(),
            'scope':'Whole compact-current identity; no quantum-clock or geometric-period comparison.'}
    out=Path(__file__).with_name('compact_exponential_cech_current_results.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'matrix_sizes_checked':len(result['actual_finite_source_current']),
                      'all_checks_passed':True,'output':str(out)},indent=2))


if __name__=='__main__':main()
