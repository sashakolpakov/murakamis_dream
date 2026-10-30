#!/usr/bin/env python3
"""Original Fourier norm, CD center profile and full folded boundary cost.

The proof supplies the uniform and endpoint assertions. These checks
retain actual physical columns, phase and both parities.
"""
import json
from pathlib import Path

import mpmath as mp

from audit_actual_q_hahn_joint_complex_amplitude import Source
from audit_actual_q_hahn_selected_complex_action import J, energy


def sine_factorials(N):
    out = [mp.mpf(1)]
    for k in range(1, N):
        out.append(out[-1]*2*mp.sin(mp.pi*k/N))
    return out


def positive_polynomials(N, j):
    sf = sine_factorials(N)
    a = [mp.mpf(1)]
    theta = mp.pi/N
    for n in range(j+1):
        h = j-n
        b = [sf[h]/sf[k]/sf[h-k] for k in range(h+1)]
        p = [mp.fsum(a[k]*b[r-k] for k in range(max(0, r-h), min(n, r)+1))
             for r in range(j+1)]
        assert min(p) > 0
        yield N-1-h, p
        if h:
            get = lambda k: a[k] if 0 <= k <= n else mp.mpf(0)
            a = [(mp.sin((j+h-k)*theta)*get(k)
                  +2*mp.sin((j-k+1)*theta)*get(k-1)
                  +mp.sin((n-k+2)*theta)*get(k-2))/mp.sin(h*theta)
                 for k in range(n+2)]


def sigma_abs(N, t, j, sf):
    d = N-1
    if 2*j == d:
        return N*sf[t-j]**2/sf[t]**2
    a = 2*abs(mp.sin(mp.pi*(2*j+1)/N))
    return N*sf[t-j]*sf[t+j-d]/(sf[t]**2*a*a)


def norm_from_positive(N, t, j, p, sf):
    return N*mp.fsum(v*v for v in p)/(sf[j]**2*sigma_abs(N, t, j, sf))


def finite_source_checks():
    counts = dict(original_physical_columns=0, exact_unused_nodes=0,
                  full_parseval_norms=0, center_identities=0,
                  folded_determinant_brackets=0, endpoint_cubic_sources=0,
                  even_paired_center_normalizations=0, even_endpoint_sources=0,
                  even_physical_half_step_bounds=0)
    tol = mp.mpf('1e-75')
    for N in range(3, 16):
        sf = sine_factorials(N)
        q = mp.exp(mp.pi*1j/N)
        for j in range(1, (N-1)//2+1):
            src = Source(N, j)
            for t, p in positive_polynomials(N, j):
                physical = []
                for u in range(N):
                    actual = src.direct(mp.mpf(t)/N, mp.mpf(u)/N)
                    z = q**(2*u-t)
                    ct = q**(j*(t+j-(N-1)))/mp.fprod(1-q**(2*r) for r in range(1, j+1))
                    transformed = q**((N-1)*u)*q**(-2*j*u)*ct*mp.fsum(v*z**k for k, v in enumerate(p))
                    assert abs(actual-transformed) < tol*max(1, abs(actual))
                    if u <= t:
                        physical.append(actual)
                        counts['original_physical_columns'] += 1
                    else:
                        assert abs(actual) < tol
                        counts['exact_unused_nodes'] += 1
                actual_norm = mp.fsum(abs(v)**2 for v in physical)
                fourier_norm = N*mp.fsum(v*v for v in p)/sf[j]**2
                assert abs(actual_norm/fourier_norm-1) < tol
                center = src.direct(mp.mpf(t)/N, mp.mpf(t)/(2*N))
                positive_center = mp.fsum(p)**2/sf[j]**2
                assert abs(abs(center)**2/positive_center-1) < tol
                assert actual_norm >= N/(mp.mpf(j)+1)*abs(center)**2*(1-tol)
                assert actual_norm <= N*abs(center)**2*(1+tol)
                counts['full_parseval_norms'] += 1
                counts['center_identities'] += 1
                if 2*j == N-1:
                    c = -mp.cos(mp.pi*(t+1)/N)
                    # Source determinant normalization at the center.
                    R = abs(src.determinant(mp.mpf(t)/N, mp.mpf(t)/(2*N)))*sf[t]/sf[t-j]
                    E = actual_norm/sigma_abs(N, t, j, sf)
                    assert abs(positive_center/sigma_abs(N, t, j, sf)-R*R/N) < tol*max(1, E)
                    assert R*R/(j+1) <= E*(1+tol) and E <= R*R*(1+tol)
                    counts['folded_determinant_brackets'] += 1
                    if t == N-1:
                        cubic = mp.fsum((sf[j]/sf[a]/sf[j-a])**3*q**(j*a) for a in range(j+1))
                        phase = mp.exp(mp.pi*1j*j)*q**(-(j+1)*j)
                        assert abs(center-phase*cubic) < tol*max(1, abs(center))
                        counts['endpoint_cubic_sources'] += 1
                elif 2*j == N-2:
                    R = abs(src.determinant(mp.mpf(t)/N, mp.mpf(t)/(2*N)))*sf[t]/sf[t-j]/src.central_beta
                    factor = mp.mpf(8)/N*mp.sin(mp.pi*(t-j)/N)
                    assert abs(positive_center/sigma_abs(N,t,j,sf)/(factor*R*R)-1) < tol
                    counts['even_paired_center_normalizations'] += 1
                    if t == N-1:
                        actual = physical[j]
                        endpoint = mp.fsum((sf[j]/sf[a]/sf[j-a])**2
                                           *(sf[j+1]/sf[j-a]/sf[a+1])*q**(j*a)
                                           for a in range(j+1))
                        phase = mp.exp(mp.pi*1j*j)*q**(-(j+1)*j)
                        assert abs(actual-phase*endpoint) < tol*max(1,abs(actual))
                        assert mp.cos(mp.pi/(2*N))**j <= abs(actual/center)*(1+tol)
                        assert abs(actual/center) <= 1+tol
                        counts['even_endpoint_sources'] += 1
                        counts['even_physical_half_step_bounds'] += 1
    return counts


def center_action(tau, xi):
    """Independently solve the actual centered source saddle on its branch."""
    target = mp.pi*(tau+xi-1)/2
    if abs(target) < mp.mpf('1e-80'):
        eta = mp.mpf(0)
    else:
        def phase(eta):
            return (2*mp.arg(mp.sin(mp.pi*(xi/2+1j*eta)))
                    +mp.arg(mp.sin(mp.pi*((tau-xi)/2+1j*eta))))
        lo, hi = mp.mpf(0), mp.mpf(1)
        while phase(hi) < target:
            hi *= 2
        for _ in range(340):
            eta = (lo+hi)/2
            if phase(eta) < target:
                lo = eta
            else:
                hi = eta
        eta = (lo+hi)/2
    a = xi/2+1j*eta
    wlog = mp.pi*1j*(tau+xi-1)
    return energy(tau, xi, tau/2, a)+a*wlog+mp.pi*1j*tau*(1-xi)/2


def e_profile(tau, xi):
    return mp.re(2*center_action(tau, xi)-J(tau-xi)-J(tau+xi-1)+2*J(tau))


def derivative_formula(tau, xi):
    c, C, s = -mp.cos(mp.pi*tau), mp.cos(mp.pi*xi), mp.sin(mp.pi*xi)
    return 2*mp.log((s*mp.sqrt(1+c)+mp.sqrt((1-c)*(1+2*c+C*C)))/mp.sqrt(2*(c*c-C*C)))


def profile_and_endpoint():
    v3 = mp.im(mp.polylog(2, mp.exp(mp.pi*1j/3)))
    endpoint = 5*v3/mp.pi
    z = 1j/mp.sqrt(3)
    alpha = mp.mpf(1)/4+1j*mp.log(3)/(4*mp.pi)
    S = -6*mp.re(J(alpha))-mp.pi*mp.im(alpha)/2
    D = mp.im(mp.polylog(2, z))+mp.arg(1-z)*mp.log(abs(z))
    assert abs(mp.tan(mp.pi*alpha)-mp.exp(mp.pi*1j/6)) < mp.mpf('1e-85')
    assert abs(S-3*D/mp.pi) < mp.mpf('1e-85')
    assert abs(2*S-endpoint) < mp.mpf('1e-85')
    derivative_checks = 0
    for tau, xi in [('0.8','0.4'), ('0.9','0.3'), ('0.7','0.49'), ('0.75','0.5')]:
        t, x = mp.mpf(tau), mp.mpf(xi)
        dh = mp.mpf('1e-25')
        actual = (e_profile(t+dh, x)-e_profile(t-dh, x))/(2*dh)
        predicted = derivative_formula(t, x)
        assert predicted > 0 and abs(actual-predicted) < mp.mpf('1e-45')
        derivative_checks += 1
    folded_integral = 2*mp.catalan/mp.pi+mp.quad(lambda t: derivative_formula(t, mp.mpf('.5')), [.5,.7,.9,1])
    assert abs(folded_integral-endpoint) < mp.mpf('1e-80')
    rows = []
    for N in (16, 17, 32, 33, 64, 65, 128, 129, 256, 257):
        m = (N-1)//2
        sf = sine_factorials(N)
        energies = []
        selections = {m, (3*N)//4, N-1}
        for t, p in positive_polynomials(N, m):
            E = norm_from_positive(N, t, m, p, sf)
            energies.append((t, E))
            if t in selections:
                tau = mp.mpf(t+1)/N
                predicted = endpoint if t == N-1 else e_profile(tau, mp.mpf('.5'))
                rows.append(dict(N=N,t=t,rate=float(mp.log(E)/N),limit_profile=float(predicted)))
        full = max(E for _, E in energies)
        p_end = p
        if N%2:
            R_end = mp.fsum(p_end)
            assert R_end**2/(m+1) <= full*(1+mp.mpf('1e-75'))
            assert full <= R_end**2*(1+mp.mpf('1e-75'))
        else:
            R_end = mp.fsum(p_end)*mp.sin(mp.pi/N)
            assert 8*R_end**2/(m+1) <= full*(1+mp.mpf('1e-75'))
            assert full <= 8*R_end**2*(1+mp.mpf('1e-75'))
            incomplete = mp.sin(mp.pi/N)*mp.fsum((sf[m]/sf[a]/sf[m-a])**2 for a in range(m+1))
            rows.append(dict(N=N,incomplete_block_rate=float(mp.log(incomplete)/N),limit=float(2*mp.catalan/mp.pi)))
        rows.append(dict(N=N, operator=('odd_simple_projector' if N%2 else 'even_completed_nilpotent_M'),
                         full_operator_rate=float(mp.log(full)/N), limit=float(endpoint)))
    return dict(source_gradient_checks=derivative_checks,
                endpoint_dilog_constant=float(endpoint), folded_integral=float(folded_integral), rows=rows)


def main():
    mp.mp.dps = 100
    result = dict(status='PASS', finite=finite_source_checks(), profile=profile_and_endpoint(),
                  scope='Actual Parseval and CD energy; complete-chamber profile; full folded norm rate5v3/pi for odd simple and even completed pairs. No global marked contraction, gluing, or independent local maximization claim.')
    Path(__file__).with_name('actual_matching_edge_magnetic_energy_profile_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
