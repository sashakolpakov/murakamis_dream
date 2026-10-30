#!/usr/bin/env python3
"""Actual joint deficient numerator: finite source, Schur matrix, amplitude.

The written proof supplies the uniform corridor. Matrix samples and
asymptotic errors below are diagnostics, not a numerical proof of it.
"""
import argparse
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_high_color_first_normal_r_degree import root_field
from audit_actual_q_hahn_physical_generic_jet_bound import Jet
from audit_actual_q_hahn_small_channel_generic_normals import (
    source_S, scalar_K, determinant)
from audit_actual_q_hahn_deficient_degree_packet import root_poly
from audit_actual_q_hahn_joint_complex_amplitude import Source


def jet_exp(base, rate):
    return Jet([base * rate**k * pow(math.factorial(k), -1, Jet.p)
                % Jet.p for k in range(Jet.order)])


def exact():
    source_checks = shift_checks = 0
    Jet.order = 4
    for N in range(5, 18):
        p, eta = root_field(N)
        q0 = eta * eta % p
        for generic in (False, True):
            Jet.p = 1000000007 if generic else p
            q = jet_exp(2 if generic else q0, 1)
            # Independent s=q^t and z jets test the rational source
            # identity beyond the original integer degree samples.
            for sb, zb in ((3, 7), (5, 11)):
                s = jet_exp(sb, 3 * pow(7, -1, Jet.p) % Jet.p)
                z = jet_exp(zb, 7 * pow(11, -1, Jet.p) % Jet.p)
                for a in range(1, (N-1)//2+1):
                    actual = determinant(N, q, s, a, z)
                    literal = (z**a * source_S(N, q, a, s/z, s*s)
                               / (s**(2*a)*scalar_K(N, q, a)))
                    assert actual == literal
                    source_checks += 1
        Jet.p = p
        Jet.order = 1
        q = Jet(q0)
        Q = q*q
        for sb, zb in ((3, 7), (5, 11)):
            s, z = Jet(sb), Jet(zb)
            T, U = s*s, s/z
            for a in range(1, (N-1)//2+1):
                R = lambda w: determinant(N, q, s, a, w)
                value = ((Q*U-1)*(U-T)*R(z/Q)
                         +(Q*T-U)*(1-U)*R(Q*z)
                         +(2*U+2*Q*T*U-(1+Q)*U*U
                           -T*(Q**(-a)+Q**(a+1)))*R(z))
                assert value == 0
                shift_checks += 1
        Jet.order = 4
    return dict(original_independent_degree_four_jet_identities=source_checks,
                exact_complex_degree_root_shift_identities=shift_checks)


def matrices():
    checks = positive = coefficient_checks = schur_checks = 0
    worst = 0.0
    mp.mp.dps = 100
    for N in (24, 25, 48, 49, 96, 97):
        th = math.pi/N
        for a in sorted(set((int(.42*N), (N-1)//2))):
            m = N//3
            for sigma in (1/6+.003j, 1/6-.004j):
                C = np.cos(np.pi*(sigma+1/N))
                ds = [1/(math.cos(n*th)*math.cos((n+1)*th))
                      for n in range(a)]
                bs = [0.0]+[math.sin(n*th)/(math.cos(n*th)
                     *math.sqrt(math.sin((2*n-1)*th)
                                *math.sin((2*n+1)*th)))
                     for n in range(1, a)]
                J = np.diag([C*d for d in ds]).astype(complex)
                for n in range(1, a):
                    prod = bs[n]**2*(C*C-math.cos(n*th)**2)
                    if n <= m:
                        J[n-1, n], J[n, n-1] = 1, prod
                    else:
                        edge = bs[n]*np.sqrt(C*C-math.cos(n*th)**2)
                        J[n-1, n] = J[n, n-1] = edge
                    assert bs[n]*math.cos(n*th)**2 <= 1+1e-12
                    coefficient_checks += 1
                D = np.diag(ds[m:])
                E = np.zeros_like(D, dtype=complex)
                for n in range(m+1, a):
                    r = n-m
                    D[r-1, r] = D[r, r-1] = bs[n]
                    ee = (-bs[n]*math.cos(n*th)**2
                          /(C+np.sqrt(C*C-math.cos(n*th)**2)))
                    E[r-1, r] = E[r, r-1] = ee
                assert np.linalg.eigvalsh(D)[0] > 0
                positive += 1
                assert np.linalg.norm(J[m:, m:]-C*D-E) < 1e-9
                for z in (80+30j, 80-30j, -80):
                    M = z*np.eye(a)-J
                    actual = root_poly(N, mp.mpc(sigma)*N, a, mp.mpc(z))
                    # A separate dense pivoted elimination avoids both
                    # the defining three-term recurrence and platform
                    # complex-LAPACK floating-status warnings.
                    lu = [list(map(complex,row)) for row in M]
                    det = 1+0j
                    for k in range(a):
                        pivot = max(range(k,a),key=lambda r:abs(lu[r][k]))
                        assert abs(lu[pivot][k])>0
                        if pivot!=k:
                            lu[k],lu[pivot]=lu[pivot],lu[k]
                            det=-det
                        det*=lu[k][k]
                        for r in range(k+1,a):
                            factor=lu[r][k]/lu[k][k]
                            for col in range(k+1,a):
                                lu[r][col]-=factor*lu[k][col]
                    rel = abs(complex(actual)/det-1)
                    assert rel < 1e-10
                    worst = max(worst, rel)
                    low = M[:m, :m]
                    gamma = J[m, m-1]*np.linalg.inv(low)[-1, -1]
                    S = M[m:, m:].copy()
                    S[0, 0] -= gamma
                    inv = np.linalg.inv(S)
                    rank = np.zeros_like(S)
                    rank[0, 0] = gamma
                    residual = C*inv@D-(z*inv-np.eye(a-m)-inv@E-inv@rank)
                    assert np.linalg.norm(residual) < 1e-10
                    assert np.linalg.norm(np.linalg.inv(M), 2) < .1
                    checks += 1
                    schur_checks += 1
    return dict(joint_finite_determinant_comparisons=checks,
                positive_tail_matrices=positive,
                endpoint_coefficient_bounds=coefficient_checks,
                exact_Schur_trace_identity_checks=schur_checks,
                maximum_matrix_relative_error=worst,
                scope='Finite diagnostics of the exact matrix identities; uniformity is proved in text.')


def ratio_packet(sigma, alpha, z, reference=mp.mpf(80)):
    """Integrate the independently specified exact characteristic/transport."""
    kap = 2*mp.pi*1j
    T = mp.exp(kap*sigma)
    J = mp.exp(kap*alpha)
    C = mp.cos(mp.pi*sigma)
    ca, sa = mp.cos(mp.pi*alpha), mp.sin(mp.pi*alpha)
    disc = mp.sqrt(C*C-ca*ca)
    r1, r2 = C+disc, C-disc

    def data(w, sign):
        U = mp.exp(mp.pi*1j*sigma)/w
        A = (U-1)*(U-T)
        c0 = 2*U*(1+T-U)-T*(J+1/J)
        sw = mp.sqrt(1-w*r1)*mp.sqrt(1-w*r2)
        sd = 4j*T*sa*sw/w
        e = (-c0+sign*sd)/(2*A)
        hp = kap*A*(e-1/e)
        hpp = kap*kap*A*(e+1/e)
        da = -2*U*U+(1+T)*U
        dp = -da*(e+1/e-2)/hp
        h1 = kap*(U*(U-T)/e+T*(1-U)*e+2*T*U-U*U-T*J)
        rho = -(h1+dp*hpp/2)/hp
        return e, dp, rho

    # At the negative anchor, real-parameter reflection has positive
    # coefficients, selecting 0<p<alpha. The same sign continues
    # to the small complex sigma disk.
    sign = max((1, -1), key=lambda ss: mp.im(data(-reference, ss)[0]))
    p0 = mp.log(data(-reference, sign)[0])/kap
    assert 0 < mp.re(p0) < alpha
    ell = mp.log(-z/reference)
    path = lambda x: -reference*mp.exp(x*ell)
    cuts = [0, mp.mpf('.25'), mp.mpf('.5'), mp.mpf('.75'), 1]
    S = p0*ell+ell*ell*mp.quad(lambda x:(1-x)*data(path(x), sign)[1], cuts)
    logA = ell*mp.quad(lambda x:data(path(x), sign)[2], cuts)
    pend = p0+ell*mp.quad(lambda x:data(path(x), sign)[1], cuts)
    return S, mp.exp(logA), pend, data(z, sign)[2]


def numerics():
    mp.mp.dps = 120
    rows = []
    worst = gradient = anchorerr = sourceerr = mp.mpf(0)
    generic_count = anchors = 0
    reference = mp.mpf(80)
    for N in (24, 49, 96):
        q0 = mp.exp(mp.pi*1j/N)
        for a in sorted(set((int(mp.mpf('.42')*N), (N-1)//2))):
            alpha = mp.mpf(a)/N
            for sigma in (mp.mpc(mp.mpf(1)/6,'.003'),
                          mp.mpc(mp.mpf(1)/6,'-.004')):
                t = N*sigma
                hi = N-t-2
                uu = hi/2+1j*N*mp.log(reference)/(2*mp.pi)
                src = Source(N, a)
                f = src.direct(hi/N, uu/N)
                anchor = ((-1)**a/src.central_beta
                          *mp.fprod(2*mp.sin(mp.pi*(hi-r)/N) for r in range(a))
                          *q0**(-(N-1)*uu-mp.mpf(a*a-(N-1)*a)/2)*f)
                err = abs(anchor/root_poly(N, t, a, -reference)-1)
                assert err < mp.mpf('1e-70'), (N, a, sigma, err)
                anchorerr = max(anchorerr, err)
                anchors += 1
                for z in (mp.mpc(80,30), mp.mpc(80,-30)):
                    base = root_poly(N,t,a,z)
                    actual = base/root_poly(N,t,a,-reference)
                    S, A, p, rho = ratio_packet(sigma,alpha,z,reference)
                    rel = N*abs(actual/(A*mp.exp(N*S))-1)
                    grad = N*N*abs(z*mp.diff(lambda w:root_poly(N,t,a,w),z)
                                  /base/N-p-rho/N)
                    assert rel < 30 and grad < 100, (N,a,sigma,z,rel,grad)
                    worst, gradient = max(worst,rel), max(gradient,grad)
                    logz=mp.log(z)
                    if mp.im(logz)<0:
                        logz += 2*mp.pi*1j
                    u=(t-logz/(mp.pi*1j/N))/2
                    assert abs(u)/N<3
                    for direction in (1,1j):
                        eps=mp.mpf('.1')*direction/N**10
                        q=q0*mp.exp(eps)
                        s, zz=q**t,q**(t-2*u)
                        gen=determinant(N,q,s,a,zz)
                        literal=(zz**a*source_S(N,q,a,s/zz,s*s)
                                 /(s**(2*a)*scalar_K(N,q,a)))
                        error=abs(literal/gen-1)
                        assert error<mp.mpf('1e-65')
                        assert mp.mpf(1)/3<abs(gen/base)<3
                        sourceerr=max(sourceerr,error)
                        generic_count+=1
                    derivative=mp.diff(lambda e:determinant(
                        N,q0*mp.exp(e),(q0*mp.exp(e))**t,a,
                        (q0*mp.exp(e))**(t-2*u)),0)
                    assert abs(derivative/base)/N**10<10
                    generic_count+=1
                    rows.append(dict(N=N,a=a,sigma=str(sigma),z=str(z),
                                     N_relative_error=str(rel),
                                     N_squared_gradient_remainder=str(grad)))
    return dict(precision_digits=mp.mp.dps,
                literal_joint_reflected_high_anchors=anchors,
                actual_joint_relative_amplitudes=len(rows),
                genuine_joint_generic_numerator_checks=generic_count,
                maximum_N_relative_error=str(worst),
                maximum_N_squared_gradient_remainder=str(gradient),
                maximum_anchor_relative_error=str(anchorerr),
                maximum_literal_generic_source_error=str(sourceerr),cases=rows)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name(
        'actual_q_hahn_joint_deficient_degree_packet_results.json'))
    args=parser.parse_args()
    result=dict(status='PASS',exact=exact(),matrix=matrices(),calibration=numerics(),
                scope='Actual joint deficient root numerator packet and genuine numerator q-jets. No full generic operator boundary lift or nonzero degree period.')
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    brief={**result,'calibration':{k:v for k,v in result['calibration'].items() if k!='cases'}}
    print(json.dumps(brief,indent=2))


if __name__=='__main__':
    main()
