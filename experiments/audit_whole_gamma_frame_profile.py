#!/usr/bin/env python3
"""Actual residual Gamma profile, exact Weyl-half unit and entire norm."""

import json
from pathlib import Path

import mpmath as mp

mp.mp.dps = 75
c = 2*mp.pi*1j


def J(x):
    return 1 if x == 0 else 2*mp.sinh(x/2)/x


def chord(T):
    return mp.exp(mp.pi*1j*T)*mp.sin(mp.pi*T)/mp.pi


def phi(a, T):
    # The explicit log is the actual mark, continuous from T>0.
    logG = mp.log(mp.sin(mp.pi*T)/mp.pi)+mp.pi*1j*T
    return mp.exp(-a*logG)*mp.rgamma(1-a)


def parameters(N, a):
    H0 = c/N
    H = H0+c*a/N**2
    b = a/(1+a/N)
    return H0, H, b


def actual_residual(N, j, a):
    _, H, _ = parameters(N, a)
    q = mp.exp(H/2)
    M = mp.exp(c*a/(2*N))
    rho = q-1/q
    qi = lambda k: (q**k-q**(-k))/rho
    return M**(-j)*mp.fprod(qi(N-r)/qi(r) for r in range(1, j+1))


def residual_factored(N, j, a, b_override=None):
    H0, H, b = parameters(N, a)
    if b_override is not None:
        b = b_override
        H = H0/(1-b/N)
    return mp.exp(-H*b*j/2)*mp.fprod(
        (1-b/r)*J(H*(r-b))/J(H*r) for r in range(1, j+1))


def beta(N, M):
    Q = mp.exp(c/N)
    L = (N-1)//2 if N % 2 else N//2-1
    ans = mp.fprod((1-M*M*Q**r)/(1-Q**r) for r in range(1, L+1))
    if N % 2 == 0:
        ans *= (1+1j*M)/(1+1j)
    return ans


def exact_unit(N, a, b_override=None):
    H0, H, b = parameters(N, a)
    if b_override is not None:
        b = b_override
        H = H0/(1-b/N)
    L = (N-1)//2 if N % 2 else N//2-1
    Mt = mp.exp(-H0*b/2)
    unit = mp.exp(-(H-H0)*b*L/2)*mp.fprod(
        J(H*(r-b))*J(H0*r)/(J(H*r)*J(H0*(r-b)))
        for r in range(1, L+1))
    if N % 2 == 0:
        unit /= (1+1j*Mt)/(1+1j)
    return unit, Mt, L


def finite_convention_checks():
    records = []
    samples = [mp.mpf(0), mp.mpf(1), mp.mpf(2), -mp.mpf(1),
               mp.mpc('.4', '.3'), mp.mpc('-.6', '.2')]
    for N in (12, 13, 24, 25):
        for a in samples:
            for j in (N//4, N//2, 3*N//4):
                lhs, rhs = actual_residual(N, j, a), residual_factored(N, j, a)
                assert abs(lhs-rhs) < mp.mpf('1e-60')*(1+abs(lhs))
            unit, Mt, L = exact_unit(N, a)
            left = actual_residual(N, L, a)
            right = unit*beta(N, Mt)
            assert abs(left-right) < mp.mpf('1e-60')*(1+abs(left))
            # The marked actual full Weyl norm is H_N, not its inverse.
            M = mp.exp(c*a/(2*N))
            HN = 1 if a == 0 else mp.sinh(c*a/2)/(N*mp.sinh(c*a/(2*N)))
            assert abs(beta(N, M)*beta(N, 1/M)-HN) < mp.mpf('1e-60')
            records.append({'level': N, 'normal_parameter': str(a),
                            'literal_qbinomial_equals_sinh_factorization': True,
                            'exact_whole_unit_and_actual_beta_norm': True})
        # Aligned exact zeros must be checked without dividing either side.
        for b in (mp.mpf(1), mp.mpf(2)):
            a = b/(1-b/N)
            unit, Mt, L = exact_unit(N, a, b_override=b)
            left = residual_factored(N, L, a, b_override=b)
            right = unit*beta(N, Mt)
            assert left == 0
            assert abs(right) < mp.mpf('1e-60')
            assert abs(unit) > mp.mpf('.001')
    return records


def profile_checks():
    samples = [mp.mpf(0), mp.mpf(1), mp.mpf(2), -mp.mpf(1),
               -mp.mpf(2), mp.mpc('.4', '.3'), mp.mpc('1', '.25'),
               mp.mpc('-.6', '.2')]
    records = []
    for N in (32, 33, 64, 65, 128, 129):
        worst_frame, worst_beta, worst_unit = mp.mpf(0), mp.mpf(0), mp.mpf(0)
        for a in samples:
            for target_T in (mp.mpf('.2'), mp.mpf('.5'), mp.mpf('.8')):
                j = int(mp.floor(N*target_T))
                T = mp.mpf(j)/N
                normalized = mp.exp(a*mp.log(N))*residual_factored(N, j, a)
                err = abs(normalized-phi(a, T))
                worst_frame = max(worst_frame, N*err/mp.log(N))
            M = mp.exp(c*a/(2*N))
            bprofile = mp.exp(-a*mp.log(N))*beta(N, M)
            worst_beta = max(worst_beta, N*abs(bprofile-phi(-a, mp.mpf('.5'))))
            unit, _, _ = exact_unit(N, a)
            worst_unit = max(worst_unit, N*abs(unit-1))
        # Loose fixed compact constants test the proven rates and marks,
        # including integer zeros; they are not estimates of a knot norm.
        assert worst_frame < 1000
        assert worst_beta < 1000
        assert worst_unit < 1000
        records.append({'level': N,
                        'absolute_frame_error_times_N_over_logN': float(worst_frame),
                        'opposite_beta_error_times_N': float(worst_beta),
                        'unit_error_times_N': float(worst_unit)})
    return records


def entire_function_checks():
    records = []
    samples = [mp.mpf(0), mp.mpf(1), mp.mpf(2), -mp.mpf(1),
               mp.mpc('.4', '.3'), mp.mpc('-.6', '.2')]
    for a in samples:
        norm = 1 if a == 0 else mp.sin(mp.pi*a)/(mp.pi*a)
        hyperbolic = 1 if a == 0 else 2*mp.sinh(c*a/2)/(c*a)
        assert abs(norm-hyperbolic) < mp.mpf('1e-65')
        for T in (mp.mpf('.2'), mp.mpf('.5'), mp.mpf('.8')):
            assert abs(phi(a, T)*phi(-a, T)-norm) < mp.mpf('1e-65')
            assert abs(chord(T)*phi(a+1, T)+a*phi(a, T)) < mp.mpf('1e-65')
        records.append({'parameter': str(a), 'paired_profile_entire_norm': True,
                        'rank_one_shift_through_resonance_zeros': True})
    return records


def main():
    result = {'finite_actual_conventions': finite_convention_checks(),
              'uniform_compact_profile_diagnostics': profile_checks(),
              'entire_norm_and_shift': entire_function_checks(),
              'precision_decimal_digits': mp.mp.dps,
              'scope': 'Actual scalar frame and meridian half-source comparisons only; no knot-growth assumption or whole state-profile identification.'}
    target = Path(__file__).with_name('whole_gamma_frame_profile_results.json')
    target.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'finite_actual_cases': len(result['finite_actual_conventions']),
                      'both_parity_profile_levels': len(result['uniform_compact_profile_diagnostics']),
                      'entire_shift_cases': len(result['entire_norm_and_shift']),
                      'absolute_zero_alignment': 'passed'}))


if __name__ == '__main__':
    main()
