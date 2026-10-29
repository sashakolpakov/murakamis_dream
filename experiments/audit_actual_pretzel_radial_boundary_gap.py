#!/usr/bin/env python3
"""Supplement exact proof of the equal-height original pretzel endpoint."""

import json
from pathlib import Path

import mpmath as mp


mp.mp.dps = 75
L = lambda z: mp.polylog(2, z)


def G(X, Y):
    return -L(X*X)+4*L(X)+L(1/X)-L(Y/X)


def full_imaginary(X, Y, W):
    return mp.im(G(X, Y)-L(-W*Y)-L(-Y/W)+3*L(Y))


def analytic_case(W):
    W = mp.mpf(W)
    A = W+1/W
    phi = 2*mp.atan(mp.sqrt(A+2)/2)
    Y = mp.exp(mp.j*phi)
    X = (Y-1)/(Y+3)
    interior = full_imaginary(X, Y, W)
    endpoint = full_imaginary(Y, Y, W)
    assert abs(interior-endpoint) < mp.mpf('1e-65')
    assert 0 < abs(X) < 1 and 0 < mp.arg(Y) < mp.arg(X) < mp.pi
    DX = (2*mp.log(1-X*X)-4*mp.log(1-X)
          +mp.log(1-1/X)-mp.log(1-Y/X))
    DY = (mp.log(1-Y/X)+mp.log(1+W*Y)+mp.log(1+Y/W)
          -3*mp.log(1-Y))
    assert abs(DX) < mp.mpf('1e-65')
    assert abs(DY-2*mp.pi*mp.j) < mp.mpf('1e-65')
    t = mp.tan(phi/2)
    derivative = mp.log(((A+2)+(A-2)*t*t)/(4*t**4))
    assert abs(derivative) < mp.mpf('1e-65')
    for k in range(1, 17):
        p = mp.pi*k/17
        y = mp.exp(mp.j*p); x = (y-1)/(y+3)
        boundary = 3*mp.im(L(y))-mp.im(L(y*y))
        assert abs(mp.im(G(x,y))-boundary) < mp.mpf('1e-65')
        actual_derivative = mp.re(mp.log(1-y/x))
        claimed_derivative = 2*mp.log(abs(1+y))-mp.log(abs(1-y))
        assert abs(actual_derivative-claimed_derivative) < mp.mpf('1e-65')
    return {'W':str(W), 'boundary_equals_interior_action':True,
            'required_Y_integer_mark':1,
            'Fstar':mp.nstr(interior,30),
            'rho_star':mp.nstr(mp.log(abs(X)),30)}


def finite_case(N, W):
    W = mp.mpf(W)
    q = mp.exp(mp.j*mp.pi/N); Q = q*q; w = -W
    fac = [mp.mpc(1)]
    for j in range(1,N):
        fac.append(fac[-1]*(1-Q**j))
    tested = 0
    for v in range((N-1)//2+1):
        poch = mp.fprod(1-Q**(-v+a) for a in range(v))
        pair = mp.fprod((1-q*w*Q**a)*(1-q/w*Q**a) for a in range(v))
        original = fac[2*v]/fac[v]**4*poch*Q**v/fac[v]**3*pair
        simplified = (-1)**v*Q**(-mp.mpf(v*(v-1))/2)*fac[2*v]*pair/fac[v]**6
        assert abs(original-simplified) < mp.mpf('1e-60')*max(1,abs(original))
        assert abs(original) > 0
        tested += 1
    return {'N':N,'W':str(W),'literal_nonzero_diagonal_terms':tested}


if __name__ == '__main__':
    analytic = [analytic_case(W) for W in ('1.001','1.1','2','5','20','100')]
    finite = [finite_case(N,W) for N in range(2,25) for W in ('1.1','2','7')]
    report = {'status':'PASS','analytic_branch_and_equal_height_families':analytic,
              'literal_finite_diagonal_families':finite,
              'scope':'Exact boundary countertheorem; no selected-cycle or total-period asymptotic inference.'}
    Path(__file__).with_name('actual_pretzel_radial_boundary_gap_results.json').write_text(
        json.dumps(report,indent=2)+'\n')
    print(f'PASS {len(analytic)} exact phase/branch families; {len(finite)} original finite diagonal families')
