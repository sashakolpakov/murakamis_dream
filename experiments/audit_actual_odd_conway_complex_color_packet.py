#!/usr/bin/env python3
"""Exact finite odd/pure packet coefficients and their marked complex action.

The finite checks compare the actual triangular Newton transport against
the independently normalized terminating source. Numerical asymptotics
are diagnostics of the proved uniform theorem, not a replacement for it.
"""
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from audit_exact_factorial_interpolation import J, sine_factorial
from audit_actual_pretzel_mixed_inner_source_wkb import literal_U, mu, nu_over_mu


def symbolic_shear():
    E, H, K, T = sp.symbols('E H K T', nonzero=True)
    hidden = T*T+E*(H-1)*T-H
    port = K*T*(1+E)**2-(E-T)*(1-E*T)
    target = K*K*(1+E)**2+K*((H+1/H)*E*E+2)+(1-E)**2
    assert sp.cancel(sp.resultant(hidden, port, T)+H*(1+E)**2*target) == 0
    epsilon, v, vx, vs, gx = sp.symbols('epsilon v vx vs gx')
    c = 2*sp.pi*sp.I
    sx, st = epsilon*vx/(c-epsilon*vs), c/(c-epsilon*vs)
    assert sp.cancel(gx+v*sx-epsilon*v*(vx+vs*sx)/c-gx) == 0
    assert sp.cancel(v*st-epsilon*v*vs*st/c-v) == 0
    cot = sp.I*(E+1)/(E-1)
    for eps, expected in [(-1, sp.pi*sp.I*(1+E)),
                          (1, -sp.pi*sp.I*(1+1/E))]:
        assert sp.cancel(-2*sp.pi*cot/(1-eps*sp.I*cot)-expected) == 0
    p, s = sp.symbols('p s')
    peff = p-epsilon/2
    vv = -sp.pi*sp.I*(s-1)/peff
    t = s-epsilon*vv/c
    difference = (-epsilon*vv*vv/(2*c)+c*(t-1)**2/(4*p)
                  -c*(s-1)**2/(4*peff))
    assert sp.cancel(difference) == 0
    return dict(port_resultant=True, exact_implicit_derivatives=True,
                signed_color_Hessians=2, effective_slope_action=True)


def chirp_checks():
    errors=[]
    for N in (8, 9, 24, 25, 63, 64):
        D=N-1
        kappa=mp.exp(mp.j*mp.pi*D*D/(2*N))
        for x in (mp.mpf('.31'), mp.mpc('.37','.008')):
            z=N*x
            chirp=mp.exp(-mp.j*mp.pi*z+mp.j*mp.pi*z*(z+1)/N)
            P=mp.exp(mp.j*mp.pi*D/4)/kappa/chirp
            S0=mp.j*mp.pi*(mp.mpf('.5')-x)**2
            expected=mp.exp(mp.j*mp.pi*(mp.mpf('.75')-x-mp.mpf(1)/(2*N)))
            error=abs(P*mp.exp(N*S0)/expected-1)
            assert error<mp.mpf('1e-45')
            errors.append(float(error))
    return dict(off_grid_and_parity_cases=len(errors), max_error=max(errors))


def finite_coefficients(N, t):
    """Canonical finite continuation, retaining the original kappa mark."""
    D=N-1; M=D//2; r=int(mp.ceil(mp.mpf('.30')*N))
    q=mp.exp(mp.j*mp.pi/N)
    kappa=mp.exp(mp.j*mp.pi*D*D/(2*N))
    sf=[mp.mpf(1)]
    for n in range(1,N):
        sf.append(sf[-1]*2*mp.sin(mp.pi*n/N))
    h=N*t
    gm=sine_factorial(N,r-h); gp=sine_factorial(N,r+h)
    pure=[]; am,ap=gm,gp
    for v in range(r,M+1):
        pure.append(N*N*sf[2*v]/(sf[v]**2*am*ap))
        am*=2*mp.sin(mp.pi*(v+1-h)/N)
        ap*=2*mp.sin(mp.pi*(v+1+h)/N)
    coefficients={0:pure[0]}
    for eps in (-1,1):
        transported=mp.fsum((-1)**v*q**(eps*v*(r+1))
                           *sf[v]/(sf[r]*sf[v-r])*pure[v-r]
                           for v in range(r,M+1))
        coefficients[eps]=(kappa**eps*mp.exp(-mp.j*eps*mp.pi*D/4)
                           *transported)
    u=literal_U(N,r,mp.pi*t)
    actual_factor=(mp.exp(mp.j*mp.pi*D/4)/kappa
                   *(-1)**r*q**(-r*(r+1))*pure[0]*u)
    error=abs(coefficients[-1]/actual_factor-1)
    assert error<mp.mpf('1e-42')
    return r,coefficients,error


def finite_source_checks():
    rows=[]
    for N in (9,10,17,18,31,32):
        for t in (mp.mpc(0),mp.mpc('.006','.002')):
            r,c,error=finite_coefficients(N,t)
            _,negative,_=finite_coefficients(N,-t)
            _,reflected,_=finite_coefficients(N,mp.conj(t))
            even=max(abs(negative[eps]/c[eps]-1) for eps in (-1,0,1))
            schwarz=abs(c[1]/mp.conj(reflected[-1])-1)
            assert max(even,schwarz)<mp.mpf('1e-42')
            # A physical small deficit is tested independently of t=0.
            rows.append(dict(N=N,r=r,t=[float(mp.re(t)),float(mp.im(t))],
                             factorization_error=float(error),
                             evenness_error=float(even),
                             Schwarz_error=float(schwarz)))
        r,c,error=finite_coefficients(N,mp.mpf(1)/N)
        rows.append(dict(N=N,r=r,physical_deficit=1,
                         factorization_error=float(error)))
    return rows


def g(x,t):
    return J(2*x)-2*J(x)-J(x-t)-J(x+t)


def gv(x,t):
    return mp.log(mp.sin(mp.pi*(x-t))/mp.sin(mp.pi*(x+t)))


def selected_action_and_amplitude(x,t):
    oldchi=mp.pi*t
    S=mp.quad(lambda u:mp.log(mu(u,oldchi)),[x,mp.mpf('.5')])
    C=mp.sqrt(mu(x,oldchi))*mp.exp(mp.quad(
        lambda u:nu_over_mu(u,oldchi),[x,mp.mpf('.5')]))
    S0=mp.j*mp.pi*(mp.mpf('.5')-x)**2
    phase=g(x,t)+S-S0
    hidden=mp.findroot(lambda s:s+gv(x,s)/(2*mp.pi*mp.j)-t,
                       t/(1+mp.j*mp.cot(mp.pi*x)))
    sheared=g(x,hidden)+gv(x,hidden)**2/(4*mp.pi*mp.j)
    action_error=abs(phase-sheared)
    assert action_error<mp.mpf('1e-40')
    b0=mp.sqrt(mp.sin(2*mp.pi*x))/(2**mp.mpf('1.5')*mp.sin(mp.pi*x)
            *mp.sqrt(mp.sin(mp.pi*(x-t))*mp.sin(mp.pi*(x+t))))
    bm=b0*mp.exp(mp.j*mp.pi*(mp.mpf('.75')-x))*C
    return phase,bm,action_error


def amplitude_calibration():
    rows=[]
    for N in (24,25,48,49):
        for t in (mp.mpc(0),mp.mpc('.006','.002')):
            r,c,_=finite_coefficients(N,t);x=mp.mpf(r)/N
            phase,bminus,action_error=selected_action_and_amplitude(x,t)
            prediction=mp.sqrt(N)*bminus*mp.exp(N*phase)
            error=abs(c[-1]/prediction-1)
            assert N*error<20
            if not t:
                b0=mp.sqrt(mp.sin(2*mp.pi*x))/(2**mp.mpf('1.5')*mp.sin(mp.pi*x)**2)
                assert abs(bminus/b0-mp.sqrt(mp.sin(mp.pi*x))*mp.exp(mp.j*mp.pi*x/2))<mp.mpf('1e-42')
            rows.append(dict(N=N,r=r,t=[float(mp.re(t)),float(mp.im(t))],
                             exact_source_vs_shear_action_error=float(action_error),
                             N_times_relative_amplitude_error=float(N*error)))
    return rows


def main():
    with mp.workdps(55):
        result=dict(status='PASS',symbolic=symbolic_shear(),
                    continuous_chirp=chirp_checks(),finite_source=finite_source_checks(),
                    selected_complex_amplitude=amplitude_calibration(),
                    scope='Exact local finite transport and canonical marks; complex saddle and whole-source estimates are proved analytically in the note. Global six-leaf normalization is independently audited by the root agent.')
    Path(__file__).with_name('actual_odd_conway_complex_color_packet_results.json').write_text(
        json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status=result['status'],symbolic=result['symbolic'],
                         continuous_chirp=result['continuous_chirp'],
                         finite_source_cases=len(result['finite_source']),
                         complex_amplitude_cases=len(result['selected_complex_amplitude']),
                         max_scaled_amplitude_error=max(row['N_times_relative_amplitude_error']
                            for row in result['selected_complex_amplitude'])),indent=2))


if __name__=='__main__':
    main()
