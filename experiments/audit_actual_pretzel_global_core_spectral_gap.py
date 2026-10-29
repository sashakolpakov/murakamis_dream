#!/usr/bin/env python3
"""Original mixed-source normalization, spectral ellipse, repeated-root blocks."""

import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from audit_actual_two_cut_ports import balanced_data


def field_case(N):
    p, eta, q, *_ = balanced_data(N)
    Q, M = q*q % p, (N-1)//2
    fac = [1]
    for j in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, j, p)) % p)
    diagonal = [pow(Q, -r*r, p)*fac[2*r]*pow(fac[r]**3 % p, -1, p) % p
                for r in range(M+1)]
    count = 0
    for h in range(M+1):
        H = pow(Q, h, p)
        T = (H+pow(H, -1, p)) % p
        actual = []
        for r in range(M+1):
            A = sum(pow(Q, -v*r, p)*fac[2*v]
                    *pow(fac[v]*fac[v-h]*fac[v+h]*fac[v-r] % p, -1, p)
                    for v in range(max(h, r), M+1)) % p
            actual.append(pow(q, h*h, p)*A*pow(diagonal[r], -1, p) % p)
        actual.append(0)
        terminal = (pow(q, h*h, p)*fac[M]**2
                    *pow(fac[M-h]*fac[M+h] % p, -1, p)) % p
        assert actual[M] == terminal
        for r in range(M):
            Z = pow(Q, r+1, p)
            pp = (-pow(Z, -1, p)*(T*Z*Z+1+pow(Q, -1, p))
                  *pow((1-Z)**2 % p, -1, p)) % p
            qq = (-pow(Q, -2, p)*pow(Z, -2, p)*(1-Q*Z*Z)*(1+Q*Z)
                  *pow((1-Z)**2*(1-Q*Z) % p, -1, p)) % p
            assert (actual[r]-pp*actual[r+1]-qq*actual[r+2]) % p == 0
            if r == M-1:
                assert qq == 0
            count += 1
    return {'N': N, 'all_physical_colors_and_indices': count,
            'literal_terminal_source_and_both_parity_wall': True}


def symbolic_classical_identity():
    t, zeta = sp.symbols('t zeta', real=True)
    # t=cot u, zeta=sin^2 chi; Z=(t+i)^2/(t^2+1).
    Z = (t+sp.I)**2/(t*t+1)
    b = -(2*(1-2*zeta)*Z*Z+2)/(1-Z)**2
    target = (t*t-1)*(1-zeta)-2*sp.I*t*zeta
    assert sp.factor(b-target) == 0
    c, z = sp.symbols('c z', real=True)
    ellipse = (1-z)**2+4*c/(1+c)**2*z*z
    assert sp.factor(1-ellipse-(2*z*(1-z)+(c-1)**2*z*z/(c+1)**2)) == 0
    return {'exact_classical_mixed_coefficient': True,
            'ellipse_slack_positive_decomposition': True}


def opnorm(A):
    B = A.H*A
    tr = mp.re(B[0, 0]+B[1, 1])
    det = mp.re(B[0, 0]*B[1, 1]-B[0, 1]*B[1, 0])
    disc = max(mp.mpf(0), tr*tr-4*det)
    return mp.sqrt((tr+mp.sqrt(disc))/2)


def classical(u, chi):
    Z = mp.exp(2j*u)
    c = mp.cot(u)**2
    b = (c-1)*mp.cos(chi)**2-2j*mp.sqrt(c)*mp.sin(chi)**2
    A = mp.matrix([[b/Z, c/(Z*Z)], [1, 0]])
    root = mp.sqrt(b*b+4*c)
    return A, c, ((b+root)/2, (b-root)/2)


def spectral_cases():
    mp.mp.dps = 90
    count, repeated = 0, []
    positions = [mp.mpf(x) for x in ('.0001', '.03', '.1', '.2', '.2499', '.25', '.2501', '.3', '.4', '.49', '.4999')]
    chis = [0, mp.pi/100, mp.pi/10, mp.pi/4, mp.pi/2]
    for t in positions:
        for chi in chis:
            A, c, roots = classical(mp.pi*t, chi)
            rho = max(1, c)
            assert max(abs(v) for v in roots) <= rho*(1+mp.mpf('1e-40'))
            B = A/rho
            for length in (1, 2, 8, 21):
                assert opnorm(B**length) <= length*opnorm(B)+length-1+mp.mpf('1e-35')
            count += 1
    for t in (mp.mpf('.3'), mp.mpf('.4'), mp.mpf('.49')):
        A, c, roots = classical(mp.pi*t, mp.pi/2)
        assert abs(roots[0]-roots[1]) < mp.mpf('1e-40')
        theta = mp.sqrt(c)
        lengths = []
        for length in (4, 16, 64):
            bound = length*opnorm(A)*theta**(length-1)+(length-1)*theta**length
            actual = opnorm(A**length)
            assert actual <= bound*(1+mp.mpf('1e-35'))
            lengths.append({'length': length, 'actual_block_norm': float(actual),
                            'elementary_repeated_root_bound': float(bound)})
        repeated.append({'u_over_pi': float(t), 'chi_over_pi': .5,
                         'repeated_root_modulus': float(theta), 'blocks': lengths})
    return {'all_color_spectral_and_power_cases': count,
            'explicit_repeated_root_contraction_cases': repeated}


def selected_values(N, h, dps=160):
    mp.mp.dps = dps
    M = (N-1)//2
    q = mp.exp(mp.pi*1j/N)
    Q = q*q
    fac = [mp.mpc(1)]
    for j in range(1, N):
        fac.append(fac[-1]*(1-Q**j))
    H = Q**h
    values = [mp.mpc(0)]*(M+2)
    values[M] = q**(h*h)*fac[M]**2/(fac[M-h]*fac[M+h])
    terminal_norm = 1 if N % 2 else mp.cos(mp.pi*h/N)
    assert abs(abs(values[M])-terminal_norm) < mp.mpf('1e-100')
    for r in reversed(range(M)):
        Z = Q**(r+1)
        pp = -Z**-1*((H+1/H)*Z*Z+1+1/Q)/(1-Z)**2
        qq = -Q**-2*Z**-2*(1-Q*Z*Z)*(1+Q*Z)/((1-Z)**2*(1-Q*Z))
        values[r] = pp*values[r+1]+qq*values[r+2]
    return values[:-1], fac, q


def literal_source_checks():
    rows = []
    for N in (8, 9, 16, 17, 32, 33):
        M = (N-1)//2
        for h in sorted(set((0, M//2, M))):
            values, fac, q = selected_values(N, h)
            Q = q*q
            for r in sorted(set((0, M//2, M))):
                A = mp.fsum(Q**(-v*r)*fac[2*v]
                             /(fac[v]*fac[v-h]*fac[v+h]*fac[v-r])
                             for v in range(max(h, r), M+1))
                D = Q**(-r*r)*fac[2*r]/fac[r]**3
                exact = q**(h*h)*A/D
                assert abs(values[r]-exact) < mp.mpf('1e-95')*max(1, abs(exact))
            rows.append({'N': N, 'h': h, 'literal_finite_source_vs_selected_recurrence': True,
                         'terminal_norm': float(abs(values[M]))})
    return rows


def envelope_diagnostics(N):
    mp.mp.dps = max(160, 2*N)
    M = (N-1)//2
    lob = lambda u: mp.im(mp.polylog(2, mp.exp(2j*u)))/2
    G = 2*lob(mp.pi/4)
    envelope = []
    for r in range(M+1):
        u = mp.pi*r/N
        envelope.append(2/mp.pi*(G-lob(u)-lob(mp.pi/2-u)) if 4*r < N else mp.mpf(0))
    rows = []
    for h in sorted(set((0, max(1, N//10), N//4, M))):
        values, _, _ = selected_values(N, h, max(160, 2*N))
        all_excess = max(mp.log(abs(value))/N-envelope[r]
                         for r, value in enumerate(values) if value)
        below = max(mp.log(abs(value))/N-envelope[r]
                    for r, value in enumerate(values) if value and r <= mp.mpf('.4')*N)
        rows.append({'N': N, 'h': h, 'chi_over_pi': h/N,
                     'max_log_source_over_N_minus_old_E': float(all_excess),
                     'max_same_excess_r_over_N_le_point4': float(below),
                     'scope': 'Finite-source diagnostic; asymptotic gap is proved by frozen blocks, not inferred from these rates.'})
    return rows


if __name__ == '__main__':
    symbolic = symbolic_classical_identity()
    fields = [field_case(N) for N in range(2, 19)]
    spectral = spectral_cases()
    source = literal_source_checks()
    diagnostics = [row for N in (32, 33, 64, 65, 128, 129) for row in envelope_diagnostics(N)]
    Path(__file__).with_name('actual_pretzel_global_core_spectral_gap_results.json').write_text(
        json.dumps({'status': 'PASS', 'symbolic': symbolic, 'all_integer_source_families': fields,
                    'spectral_ellipse_and_Jordan_blocks': spectral,
                    'literal_complex_finite_sources': source,
                    'uniform_source_envelope_diagnostics': diagnostics,
                    'scope': 'Global actual low-core envelope and strict macroscopic-color gap, all normal source data; full RP bands remain separate.'}, indent=2)+'\n')
    print('PASS 17 all-color/all-index source families; exact spectral ellipse; 55 block-power cases including Jordan contractions; 18 literal complex sources; 24 source-envelope diagnostics')
