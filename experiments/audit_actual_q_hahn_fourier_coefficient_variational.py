#!/usr/bin/env python3
"""Actual positive Fourier coefficients, tilted modes and interior rates.

The uniform theorem is analytical. These checks retain the exact source
normalizer and distinguish its polynomial radius from the reciprocal
determinant coordinate; no graph-phase cancellation is tested.
"""
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from audit_actual_matching_edge_magnetic_energy_profile import (
    positive_polynomials, sine_factorials, center_action,
)
from audit_actual_q_hahn_joint_complex_amplitude import Source
from audit_actual_q_hahn_selected_complex_action import J


def symbolic():
    am2, am1, a0, ap1, rho = sp.symbols('am2 am1 a0 ap1 rho')
    left = (rho*a0+am1)**2-(rho*am1+am2)*(rho*ap1+a0)
    right = rho**2*(a0*a0-am1*ap1)+rho*(a0*am1-am2*ap1)+am1*am1-am2*a0
    assert sp.expand(left-right) == 0
    w, c, C, s = sp.symbols('w c C s', positive=True)
    B = w*w+2*c*w+C*C
    derivative = w*sp.diff(sp.atan(sp.sqrt(B)/s)/sp.pi, w)
    predicted = s*w*(w+c)/(sp.pi*sp.sqrt(B)*(1+2*c*w+w*w))
    assert sp.simplify((derivative-predicted).subs(s*s, 1-C*C)) == 0
    r = sp.symbols('r', positive=True)
    tilt = sp.sqrt(c*c-C*C+r*r)-c
    assert sp.simplify(tilt*tilt+2*c*tilt+C*C-r*r) == 0
    return 3


def slope(tau, xi, y):
    w = mp.exp(y);c=-mp.cos(mp.pi*tau);C=mp.cos(mp.pi*xi);s=mp.sin(mp.pi*xi)
    return xi-mp.mpf('.5')+mp.atan(mp.sqrt(w*w+2*c*w+C*C)/s)/mp.pi


def tilt(tau, xi, lam):
    c=-mp.cos(mp.pi*tau);C=mp.cos(mp.pi*xi);s=mp.sin(mp.pi*xi)
    r=s*mp.tan(mp.pi*(mp.mpf('.5')-xi+lam))
    return mp.log(mp.sqrt(c*c-C*C+r*r)-c)


def checks():
    mp.mp.dps = 90
    polynomials = inequalities = modes = source_values = 0
    max_dual = max_source = max_gradient = mp.mpf(0)
    for N in range(3, 26):
        for j in range(1, (N-1)//2+1):
            for t,p in positive_polynomials(N,j):
                polynomials += 1
                for k in range(1,j):
                    assert p[k]*p[k] >= p[k-1]*p[k+1]*(1-mp.mpf('1e-80'))
                    inequalities += 1
                    w = mp.sqrt(p[k-1]/p[k+1])
                    terms = [v*w**r for r,v in enumerate(p)]
                    assert max(terms) <= terms[k]*(1+mp.mpf('1e-80'))
                    ratio=mp.fsum(terms)/terms[k]
                    assert 1<=ratio<=(j+1)*(1+mp.mpf('1e-80'))
                    max_dual=max(max_dual,ratio/(j+1));modes+=1
        if N in (9,12,17):
            j=(N-1)//2;t=(N-1+j)//2
            p=dict(positive_polynomials(N,j))[t]
            sf=sine_factorials(N);src=Source(N,j);tau=mp.mpf(t)/N
            for y in map(mp.mpf,('-1','.3','1')):
                nu=tau/2-1j*y/(2*mp.pi)
                actual=abs(src.direct(tau,nu))
                predicted=mp.exp((N-1-2*j)*y/2)*mp.fsum(v*mp.exp(y*k) for k,v in enumerate(p))/sf[j]
                error=abs(actual/predicted-1)
                assert error<mp.mpf('1e-75')
                max_source=max(max_source,error);source_values+=1

    rows=[];max_rate=mp.mpf(0)
    for N in (32,65,128):
        for tau0,xi0 in ((mp.mpf('.8'),mp.mpf('.4')),(mp.mpf('.9'),mp.mpf('.49'))):
            t=int(mp.floor(tau0*N));j=int(mp.floor(xi0*N))
            tau=mp.mpf(t)/N;xi=mp.mpf(j)/N
            p=dict(positive_polynomials(N,j))[t]
            F0=J(xi)+mp.re(center_action(tau,xi))
            for frac in (mp.mpf('.2'),mp.mpf('.5'),mp.mpf('.8')):
                k=max(1,min(j-1,int(mp.floor(frac*j))));lam=mp.mpf(k)/N
                y=tilt(tau,xi,lam)
                assert abs(slope(tau,xi,y)-lam)<mp.mpf('1e-80')
                rate=F0+mp.quad(lambda x:slope(tau,xi,x),[0,y])-lam*y
                error=abs(mp.log(p[k])-N*rate)/mp.log(N)
                assert error<5
                terms=[v*mp.exp(y*r) for r,v in enumerate(p)]
                derivative=mp.fsum(r*value for r,value in enumerate(terms))/(N*mp.fsum(terms))
                gradient=N*abs(derivative-lam)
                assert gradient<5
                max_rate=max(max_rate,error);max_gradient=max(max_gradient,gradient)
                rows.append(dict(N=N,t=t,j=j,k=k,log_scaled_error=float(error)))
    return dict(positive_polynomials=polynomials,logconcavity_inequalities=inequalities,
                actual_tilted_mode_bounds=modes,actual_off_lattice_radial_source_values=source_values,
                maximum_mode_ratio_over_jplus1=float(max_dual),maximum_source_relative_error=mp.nstr(max_source,30),
                interior_coefficient_rates=len(rows),maximum_log_scaled_rate_error=float(max_rate),
                maximum_N_scaled_tilt_gradient_error=float(max_gradient),rates=rows)


if __name__=='__main__':
    result=dict(status='PASS',symbolic_identities=symbolic(),numerical=checks(),
                scope='Actual complete-channel Fourier coefficient duality and interior variational rates; no relative coefficient amplitude, boundary uniformity, or original graph phase-cancellation theorem.')
    Path(__file__).with_name('actual_q_hahn_fourier_coefficient_variational_results.json').write_text(json.dumps(result,indent=2)+'\n')
    summary=dict(result);summary['numerical']={k:v for k,v in result['numerical'].items() if k!='rates'}
    print(json.dumps(summary,indent=2))
