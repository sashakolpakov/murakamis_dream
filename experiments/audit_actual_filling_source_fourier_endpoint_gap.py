#!/usr/bin/env python3
"""Exact normal-weighted filling split and source-conditioned Fourier decay."""

import json
from pathlib import Path

import mpmath as mp

from audit_actual_coherent_filling_gaussian_chirp import data, fresnel


def normal_split_case(N, P):
    mp.mp.dps = 80
    q, Q, kappa, nodes, values, derivatives, HD, a, kernel = data(N, P)
    H = N//3
    # Operator-valued EVEN physical exterior, not only one scalar value.
    core = {h: mp.matrix([[1+mp.mpf(h*h)/N**2, 1j*mp.mpf(h*h)/N],
                         [mp.mpf(h**4)/N**4, 2-mp.mpf(h*h)/(3*N**2)]])
            for h in range(H+1)}
    direct = mp.zeros(2)
    for h in range(H+1):
        n = N-h-1
        beta = (-1)**n*(a(n)-(a(n+2) if n+2 < N else 0))
        direct += beta*core[h]
    folded = mp.zeros(2)
    central, endpoint = mp.zeros(2), mp.zeros(2)
    for h in range(-H, H+1):
        folded += kernel(h)*core[abs(h)]/2
        for k in range(N):
            y = nodes[k]-mp.pi*1j
            exact = (mp.mpf(2)*(-1)**(N-1)/N**2*values[k]*mp.exp(h*y)
                     *((h+2*P*y/(2j*mp.pi/N))*mp.sinh(y)+mp.cosh(y)))
            if abs(mp.mpf(k)+mp.mpf('.5')-mp.mpf(N)/2) >= mp.mpf(N)/5:
                endpoint += exact*core[abs(h)]/2
            else:
                central += exact*core[abs(h)]/2
    assert mp.norm(direct-folded) < mp.mpf('1e-60')
    assert mp.norm(direct-central-endpoint) < mp.mpf('1e-60')
    # The high derivative is generally present in the actual partial strip.
    normal_endpoint = mp.zeros(2)
    for h in range(-H, H+1):
        for k in range(N):
            if abs(mp.mpf(k)+mp.mpf('.5')-mp.mpf(N)/2) < mp.mpf(N)/5:
                continue
            y = nodes[k]-mp.pi*1j
            normal_endpoint += (mp.mpf(2)*(-1)**(N-1)/N**2*values[k]*mp.exp(h*y)
                                *2*P*y/(2j*mp.pi/N)*mp.sinh(y)*core[abs(h)]/2)
    if P:
        assert mp.norm(normal_endpoint) > mp.mpf('1e-10')
    return {'N': N, 'P': P, 'arbitrary_even_two_by_two_exterior': True,
            'exact_half_color_and_full_normal_endpoint_split': True,
            'retained_normal_endpoint_norm': float(mp.norm(normal_endpoint))}


def residue_case(N, phi, power):
    mp.mp.dps = 75
    delta, sigma, a = mp.mpf('.25'), mp.mpf('.08'), mp.mpf('2')
    H, phi = int(mp.floor(delta*N)), mp.mpf(phi)
    x, y = mp.mpf(H)+mp.mpf('.5'), sigma*N
    packet = lambda z: (1+mp.mpc(z)/(7*N))*mp.exp(-a*mp.mpc(z)**2/N)
    # A non-even source is allowed by the Fourier lemma itself.
    direct = mp.fsum(mp.mpf(h)**power*packet(h)*mp.exp(1j*phi*h)
                     for h in range(-H, H+1))
    def integrand(z):
        cot = 2j*mp.pi/mp.expm1(2j*mp.pi*z)
        return z**power*packet(z)*mp.exp(1j*phi*z)*cot/(2j*mp.pi)
    corners = [-x-1j*y, x-1j*y, x+1j*y, -x+1j*y, -x-1j*y]
    total = 0
    for start, end in zip(corners[:-1], corners[1:]):
        pieces = max(1, int(mp.ceil(abs(end-start))))
        grid = [mp.mpf(j)/pieces for j in range(pieces+1)]
        total += mp.quad(lambda t: integrand(start+t*(end-start))*(end-start), grid)
    assert abs(total-direct) < mp.mpf('1e-55')
    # Exact half-integer side bound, with both signs of Im z.
    distance = min(phi, 2*mp.pi-phi)
    for yy in (-y, -y/3, mp.mpf(0), y/3, y):
        zz = x+1j*yy
        actual = abs(mp.exp(1j*phi*zz)*2j*mp.pi/mp.expm1(2j*mp.pi*zz))
        assert actual <= 2*mp.pi*mp.exp(-distance*abs(yy))*(1+mp.mpf('1e-60'))
    return {'N': N, 'frequency': float(phi), 'normal_power': power,
            'exact_finite_rectangle_residue': True,
            'both_vertical_color_side_currents_retained': True}


def gap_case(N, phi, power):
    mp.mp.dps = 100
    delta, sigma, a, phi0 = map(mp.mpf, ('.2', '.025', '2', '.5'))
    H, phi = int(mp.floor(delta*N)), mp.mpf(phi)
    g = min(a*delta**2/8, phi0*sigma/2)
    value = abs(mp.fsum(mp.mpf(h)**power*mp.exp(-a*h*h/N+1j*phi*h)
                        for h in range(-H, H+1)))
    # Conservative polynomial from the literal contour length and z^r.
    bound = 20*N**(power+1)*mp.exp(-g*N)
    assert value <= bound
    return {'N': N, 'frequency': float(phi), 'normal_power': power,
            'certified_analytic_gap': float(g), 'actual_modulus': float(value),
            'proved_contour_bound': float(bound)}


def charge_case(N, P, H):
    mp.mp.dps = 85
    q, Q, kappa, nodes, values, derivatives, HD, a, kernel = data(N, P)
    core = {h: (1+mp.mpf(h*h)/(7*N))*mp.exp(-mp.mpf(h*h)/N)
            for h in range(-H, H+1)}
    direct = mp.fsum(kernel(h)*core[h]/2 for h in range(-H, H+1))
    def fourier(z):
        return mp.fsum(core[h]*mp.exp(2j*mp.pi*h*z) for h in range(-H, H+1))
    def U(z):
        return mp.exp(2j*mp.pi*P*N*z*z)*mp.sinh(2j*mp.pi*z)*fourier(z)
    deriv = mp.fsum(mp.diff(U, (mp.mpf(k)+mp.mpf('.5'))/N-mp.mpf('.5'))
                    for k in range(N))
    predicted = (-1)**(N-1)*kappa**(-P)*deriv/(2j*mp.pi*N**2)
    assert abs(predicted-direct) < mp.mpf('1e-65')
    assert abs(U(mp.mpf('.5')))+abs(U(mp.mpf('-.5'))) < mp.mpf('1e-65')
    assert abs(mp.diff(U, mp.mpf('.5'))-mp.diff(U, mp.mpf('-.5'))) < mp.mpf('1e-65')
    def charge(m):
        integral = 0
        for h in range(-H, H+1):
            b = N*m-h
            # Exact z-centered Fresnel integral, without tail approximation.
            integral += core[h]*(mp.exp(mp.pi*1j*(b-1))*fresnel(P, N, b-1)
                                 -mp.exp(mp.pi*1j*(b+1))*fresnel(P, N, b+1))/2
        return (-1)**(N-1)*kappa**(-P)*(-1)**(m*(N-1))*m*integral
    for m in (1, 2, 3, 7):
        assert abs(charge(m)-charge(-m)) < mp.mpf('1e-60')
    partial, errors = 0, []
    for m in range(1, 65):
        partial += 2*charge(m)
        if m in (16, 32, 64):
            errors.append(abs(partial-direct))
    assert errors[2] < errors[1] < errors[0]
    assert errors[-1] < mp.mpf('.01')
    return {'N': N, 'P': P, 'H': H, 'exact_complete_normal_total_derivative': True,
            'zero_charge_endpoint_cancellation': True, 'equal_opposite_charges': True,
            'absolute_charge_cutoff_errors': [float(x) for x in errors]}


def paired_vertical_case(N, P, m):
    mp.mp.dps = 85
    H, sigma = N//4, mp.mpf('.017')
    core = {h: mp.exp(-mp.mpf(2)*h*h/N) for h in range(-H, H+1)}
    def fourier(z):
        return mp.fsum(core[h]*mp.exp(2j*mp.pi*h*z) for h in range(-H, H+1))
    def U(z):
        return mp.exp(2j*mp.pi*P*N*z*z)*mp.sinh(2j*mp.pi*z)*fourier(z)
    def V(v):
        return U(mp.mpf('.5')-1j*v)-U(mp.mpf('-.5')-1j*v)
    assert abs(V(0))+abs(mp.diff(V, 0)) < mp.mpf('1e-65')
    def integrate(fn, start, end):
        pieces = max(8, N*(abs(P)+m)//2)
        return mp.quad(lambda t: fn(start+t*(end-start))*(end-start),
                       [mp.mpf(j)/pieces for j in range(pieces+1)])
    direct = integrate(lambda z: U(z)*mp.exp(-2j*mp.pi*m*N*z),
                       mp.mpf('-.5'), mp.mpf('.5'))
    horizontal = integrate(lambda z: U(z)*mp.exp(-2j*mp.pi*m*N*z),
                           mp.mpc('-.5', -sigma), mp.mpc('.5', -sigma))
    current = 1j*(-1)**(m*N)*mp.quad(
        lambda v: mp.exp(-2*mp.pi*m*N*v)*V(v), [0, sigma])
    assert abs(direct-horizontal-current) < mp.mpf('1e-55')
    second_max = max(abs(mp.diff(V, v, 2)) for v in
                     (mp.mpf(0), sigma/4, sigma/2, 3*sigma/4, sigma))
    for v in (sigma/20, sigma/10, sigma/5):
        assert abs(V(v)) <= second_max*v*v
    return {'N': N, 'P': P, 'charge': m,
            'exact_lower_contour_and_paired_vertical_current': True,
            'quadratic_endpoint_zero_not_deleted': True,
            'vertical_current_modulus': float(abs(current)),
            'horizontal_modulus': float(abs(horizontal))}


def central_fourier_case(N, coords):
    mp.mp.dps = 100
    tau, delta = mp.mpc('.4', '.5'), mp.mpf('.2')
    H, r = int(mp.floor(delta*N)), len(coords)
    coords = [mp.mpc(z) for z in coords]
    actual = mp.mpf(N)**mp.mpf('1.5')
    for z in coords:
        actual *= mp.fsum(mp.exp(mp.pi*1j*tau*h*h/N+2j*mp.pi*h*z)
                          for h in range(-H, H+1))
    predicted = (mp.mpf(N)**(mp.mpf(r+3)/2)*(-1j*tau)**(-mp.mpf(r)/2)
                 *mp.exp(-mp.pi*1j*N*mp.fsum(z*z for z in coords)/tau))
    error = abs(actual/predicted-1)
    assert error < mp.mpf('.04')
    assert error <= 10*N*mp.exp(-mp.mpf('.01')*N)
    reflected = mp.mpf(N)**mp.mpf('1.5')
    for z in coords:
        reflected *= mp.fsum(mp.exp(mp.pi*1j*tau*h*h/N-2j*mp.pi*h*z)
                             for h in range(-H, H+1))
    assert abs(reflected/actual-1) < mp.mpf('1e-85')
    return {'N': N, 'ports': r, 'complex_frequencies': [str(z) for z in coords],
            'nonzero_complete_Fourier_amplitude': True, 'relative_error': float(error),
            'all_parity_complex_gaussian_normalization': True}


if __name__ == '__main__':
    normal = [normal_split_case(N, P) for N in range(3, 10) for P in (-3, 0, 2)]
    residue = [residue_case(N, phi, r) for N in (16, 24)
               for phi in ('.6', '3.1', '5.5') for r in (0, 1)]
    gap = [gap_case(N, phi, r) for N in (32, 64, 128, 256)
           for phi in ('.5', '1.7', '3.1', '5.7') for r in (0, 1)]
    charges = [charge_case(N, P, H) for N, P, H in ((4, 2, 1), (5, -3, 1), (6, 2, 2))]
    tails = [paired_vertical_case(N, P, m) for N, P, m in
             ((8, 2, 6), (9, -3, 7), (12, 2, 8))]
    fourier = [central_fourier_case(N, coords) for N in (64, 65, 128, 129, 256, 257)
               for coords in ((mp.mpc('.02', '.01'),),
                              (mp.mpc('.01', '-.01'), mp.mpc('-.015', '.005')))]
    result = {'status': 'PASS', 'original_full_normal_filling_splits': normal,
              'exact_finite_cotangent_source_contours': residue,
              'quantitative_source_conditioned_gaps': gap,
              'combined_source_total_derivative_and_paired_charges': charges,
              'source_endpoint_high_charge_contour': tails,
              'central_complete_complex_Fourier_packet': fourier,
              'scope': 'Exact finite endpoint bound under explicit analytic source hypotheses; no free-exterior operator bound or outside-cusp filling assertion.'}
    Path(__file__).with_name('actual_filling_source_fourier_endpoint_gap_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(f'PASS {len(normal)} full-normal source splits; {len(residue)} exact side-current contours; {len(gap)} analytic Fourier gaps; {len(charges)} total-derivative charge packets; {len(tails)} paired high-charge currents; {len(fourier)} central Fourier packets')
