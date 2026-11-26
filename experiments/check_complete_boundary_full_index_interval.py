#!/usr/bin/env python3
"""Exact reductions and finite-source checks for all interior boundary indices.

The all-interval statement uses the horizontal maximum and endpoint proofs.
Finite comparisons below are normalization diagnostics, not their substitute.
"""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--dps', type=int, default=150)
    ap.add_argument('--output', type=Path,
                    default=ROOT/'repro/results/research-complete-boundary-full-index-interval.json')
    args = ap.parse_args()
    mp.mp.dps = args.dps
    identities = []

    def check(name, expression):
        assert sp.factor(expression) == 0, (name,sp.factor(expression))
        identities.append(name)

    C,c,s,Ce,Se = sp.symbols('C c s Ce Se', real=True)
    A = (1-Ce)*(C+c)**2+4*C*(C-c)
    D = (C+c)**2*(C-Ce*c-Se*s)-(C-c)**3
    check('horizontal ratio numerator', D-(c*A-Se*s*(C+c)**2))
    vv = sp.symbols('v',real=True)
    check('unique-root equation after c=-v*s',
          (c*A-Se*s*(C+c)**2).subs(c,-vv*s)
          -s*((C-vv*s)**2)*(-vv*A.subs(c,-vv*s)/(C-vv*s)**2-Se))
    check('monotone quotient derivative',
          sp.diff((C-c)/(C+c)**2,c)+(3*C-c)/(C+c)**3)
    check('positive numerator form',
          A-(5*C*C-2*C*c+c*c-Ce*(C+c)**2))
    check('exact midpoint sign', D.subs({Ce:-1,Se:0})-c*A.subs(Ce,-1))
    aa,bb,R = sp.symbols('a b R',real=True)
    check('square-root unit-circle relation',
          (aa*aa-bb*bb-1)**2+4*aa*aa*bb*bb-4
          -((aa*aa+bb*bb-1)**2+4*bb*bb-4))
    check('atan quotient real numerator',
          (1-bb)*(3+bb)-aa*aa-(3-2*bb-(aa*aa+bb*bb)))
    check('atan quotient modulus difference',
          (3+bb)**2+aa*aa-((1-bb)**2+aa*aa)-8*(1+bb))
    jx,jh,ja,jax = sp.symbols('Jx Jh Ja Jax')
    check('upper-half physical entropy identity',
          2*jx+3*jh-jax+ja-(-(-2*jh-2*jx)+jh+ja-jax))
    k = sp.symbols('k',integer=True)
    check('full Gaussian N power', (k-2)+1-sp.Rational(1,2)-(k-sp.Rational(3,2)))
    e,y = sp.symbols('e y',real=True)
    check('reflected lower-alias loss', -2*sp.pi*y+2*sp.pi*e*y+2*sp.pi*(1-e)*y)
    check('left vertical argument bound',
          sp.pi/2-3*sp.pi/2+sp.pi*e+sp.pi*(1-e))
    check('right vertical argument bound',
          -sp.pi+sp.pi*e+sp.pi*(1-e))

    def J(z):
        z = mp.mpc(z)
        return ((mp.pi**2/6-mp.polylog(2,mp.exp(2j*mp.pi*z)))/(2j*mp.pi)
                +1j*mp.pi*z*(1-z)/2)

    def critical(e):
        return mp.atan((1j+mp.sqrt(1-2*mp.exp(2j*mp.pi*e)))/2)/mp.pi

    def action(e,u):
        return -2*J(mp.mpf('.5')-u)-3*J(u)-J(e-u)+1j*mp.pi*e*u

    def curvature(e,u):
        return mp.pi*(2*mp.tan(mp.pi*u)+3*mp.cot(mp.pi*u)
                      +mp.cot(mp.pi*(e-u)))

    lifts = []
    for ee in ('0.49','0.5','0.55','0.7','0.85','0.95','0.99'):
        ev=mp.mpf(ee);u=critical(ev)
        Fu=(2*mp.log(mp.cos(mp.pi*u))+mp.log(mp.sin(mp.pi*(ev-u)))
            -3*mp.log(mp.sin(mp.pi*u))+1j*mp.pi*ev)
        assert abs(Fu)<mp.mpf(10)**(-args.dps+15),(ee,Fu)
        assert 0<u.real<min(ev,mp.mpf('.5')) and u.imag>0
        if ev>mp.mpf('.5'):
            assert u.real>mp.mpf('.25')
        assert curvature(ev,u).real>0
        lam=action(ev,u).real
        endpoint=-J(ev-mp.mpf('.5')).real if ev>=mp.mpf('.5') else None
        if endpoint is not None:assert lam>endpoint
        lifts.append({'e':ee,'critical':[str(u.real),str(u.imag)],
                      'zero_lift_residual':str(abs(Fu)),
                      'real_negative_hessian':str(curvature(ev,u).real),
                      'action':str(lam),
                      'upper_endpoint_gap':None if endpoint is None else str(lam-endpoint)})

    diagnostics=[]
    # The complete Newton product is differentiated by its finite recurrence,
    # never by division through its zero at odd levels.
    for N in (40,41,80,81,160,161,320,321):
        sine=[mp.mpf(1)]
        E=[[mp.mpf(1),mp.mpf(0),mp.mpf(0)]]
        for ell in range(1,N):
            sh=2*mp.sin(mp.pi*ell/N)
            sine.append(sine[-1]*sh)
            fac=4*mp.cos(mp.pi*(ell-mp.mpf('.5'))/N)**2
            if 2*ell-1==N:fac=mp.mpf(0)
            old=E[-1]
            E.append([(fac*old[a]+(a*old[a-1] if a else 0))/sh**2
                      for a in range(3)])
        for target in ('0.49','0.55','0.7','0.85','0.95'):
            j=int(mp.floor(N*mp.mpf(target)));ev=mp.mpf(j)/N
            u=critical(ev);f=action(ev,u);hess=curvature(ev,u)
            phase_step=mp.exp(1j*mp.pi*j/N)
            actual=[mp.mpc(0)]*3;phase=mp.mpc(1)
            for ell in range(j+1):
                common=phase/(sine[ell]*sine[j-ell])
                for a in range(3):actual[a]+=common*E[ell][a]
                phase*=phase_step
            base=(mp.sqrt(2*mp.pi)/mp.sqrt(hess)
                  /(mp.power(2*mp.sin(mp.pi*u),mp.mpf('1.5'))
                    *mp.sqrt(2*mp.sin(mp.pi*(ev-u)))))
            jet=mp.tan(mp.pi*u)/(4*mp.pi)
            for a in range(3):
                predicted=mp.power(N,a-mp.mpf('1.5'))*base*jet**a*mp.exp(N*f)
                error=abs(actual[a]/predicted-1)
                scaled=N*error
                assert scaled<300,(N,j,a,error)
                diagnostics.append({'N':N,'j':j,'jet_order':a,'e':str(ev),
                                    'relative_error':str(error),'N_times_relative_error':str(scaled)})
    color_diagnostics=[]
    # Evaluate the original polynomial away from its complete color.  These
    # comparisons also detect an omitted color-dependent leading amplitude.
    for N in (40,41,80,81,160,161):
        sine=[mp.mpf(1)]
        for ell in range(1,N):
            sine.append(sine[-1]*2*mp.sin(mp.pi*ell/N))
        for re_delta,im_delta in (('0.0005','0.0003'),('-0.0004','0.0002')):
            delta=mp.mpc(re_delta,im_delta)
            w=-2+delta
            t=mp.acos(-w/2)
            shift=t/(2*mp.pi)
            coefficients=[mp.mpc(1)]
            for ell in range(1,N):
                fac=4*mp.cos(mp.pi*(ell-mp.mpf('.5'))/N)**2
                if 2*ell-1==N:fac=mp.mpf(0)
                coefficients.append(coefficients[-1]*(fac-delta)
                                    /(2*mp.sin(mp.pi*ell/N))**2)
            for target in ('0.49','0.7','0.95'):
                j=int(mp.floor(N*mp.mpf(target)));ev=mp.mpf(j)/N
                def derivative(u):
                    return (mp.log(2*mp.sin(mp.pi*(mp.mpf('.5')-u+shift)))
                            +mp.log(2*mp.sin(mp.pi*(mp.mpf('.5')-u-shift)))
                            -3*mp.log(2*mp.sin(mp.pi*u))
                            +mp.log(2*mp.sin(mp.pi*(ev-u)))+1j*mp.pi*ev)
                u=mp.findroot(derivative,critical(ev))
                residual=abs(derivative(u))
                assert residual<mp.mpf(10)**(-args.dps+15)
                f=(-J(mp.mpf('.5')-u+shift)-J(mp.mpf('.5')-u-shift)
                   -3*J(u)-J(ev-u)+1j*mp.pi*ev*u)
                hess=mp.pi*(mp.cot(mp.pi*(mp.mpf('.5')-u+shift))
                            +mp.cot(mp.pi*(mp.mpf('.5')-u-shift))
                            +3*mp.cot(mp.pi*u)+mp.cot(mp.pi*(ev-u)))
                base=(mp.sqrt(2*mp.pi)/mp.sqrt(hess)
                      /(mp.power(2*mp.sin(mp.pi*u),mp.mpf('1.5'))
                        *mp.sqrt(2*mp.sin(mp.pi*(ev-u)))))
                actual=mp.fsum(mp.exp(1j*mp.pi*ev*ell)*coefficients[ell]
                               /(sine[ell]*sine[j-ell]) for ell in range(j+1))
                predicted=mp.power(N,-mp.mpf('1.5'))*base*mp.exp(N*f)
                error=abs(actual/predicted-1)
                assert N*error<300,(N,j,w,error)
                color_diagnostics.append({'N':N,'j':j,'e':str(ev),
                    'color_displacement':[re_delta,im_delta],
                    'critical':[str(u.real),str(u.imag)],
                    'zero_lift_residual':str(residual),
                    'relative_error':str(error),'N_times_relative_error':str(N*error)})
    dependencies=[
        'notes/research_complete_boundary_full_index_interval.md',
        'notes/research_complete_boundary_coefficient_asymptotic.md',
        'notes/research_complete_boundary_complex_index.md',
        'notes/research_mixed_complete_boundary_sum.md',
        'notes/research_uniform_factorial_and_boundary_decay.md',
        'notes/exact_factorial_interpolation_and_complex_contours.md',
    ]
    result={
        'status':'passed','diagnostic_decimal_digits':args.dps,
        'symbolic_identity_count':len(identities),'symbolic_identities':identities,
        'critical_lift_diagnostic_count':len(lifts),'critical_lift_diagnostics':lifts,
        'finite_sum_diagnostic_count':len(diagnostics),'finite_sum_diagnostics':diagnostics,
        'maximum_N_scaled_error':str(max(mp.mpf(x['N_times_relative_error']) for x in diagnostics)),
        'whole_color_diagnostic_count':len(color_diagnostics),
        'whole_color_diagnostics':color_diagnostics,
        'whole_color_maximum_N_scaled_error':str(max(
            mp.mpf(x['N_times_relative_error']) for x in color_diagnostics)),
        'scope':('Exact horizontal-maximum and endpoint reductions for the full '
                 'interior index theorem; physical finite sums above and below '
                 'the midpoint at both parities and ordinary orders 0,1,2; '
                 'the whole original polynomial at small complex color displacements. '
                 'Diagnostics check normalization, not the universal theorem. '
                 'No first-cap or full mixed-word asymptotic.'),
        'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
    }
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:result[key] for key in (
        'status','symbolic_identity_count','critical_lift_diagnostic_count',
        'finite_sum_diagnostic_count','maximum_N_scaled_error',
        'whole_color_diagnostic_count','whole_color_maximum_N_scaled_error')}))


if __name__=='__main__':
    main()
