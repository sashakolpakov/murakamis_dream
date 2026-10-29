#!/usr/bin/env python3
"""Exact full-jet chirp calibration of the local corridor Gaussian theorem.

The test packets have a known analytic quadratic source. They check the
coherent filling, physical half weight, signed Gaussian phase and density;
they do not infer the actual pretzel source hypotheses from samples.
"""

import json
from pathlib import Path

import mpmath as mp

from audit_actual_coherent_filling_gaussian_chirp import data


def coefficients(N, P):
    q, Q, kappa, nodes, values, derivatives, HD, a, kernel = data(N, P)
    step, aa = 2*abs(P), [None]*N
    for n in range(min(step, N)):
        aa[n] = a(n)
    for n in range(N-step):
        if P < 0:
            aa[n+step] = Q**(n-P)*aa[n]+mp.mpf(2)*P/N*q**(n+step)
        else:
            aa[n+step] = Q**(-n-P)*(aa[n]-mp.mpf(2)*P/N*q**n)
    beta = [(-1)**n*(aa[n]-(aa[n+2] if n+2 < N else 0)) for n in range(N)]
    return q, Q, kappa, aa, beta, a


def recurrence_case(N, P):
    mp.mp.dps = 85
    q, Q, kappa, aa, beta, a = coefficients(N, P)
    assert max(abs(aa[n]-a(n)) for n in range(N)) < mp.mpf('1e-60')
    assert abs(beta[-1]-(-1)**(N-1)*(a(N-1)-a(N+1))/2) < mp.mpf('1e-60')
    return {'N': N, 'P': P, 'exact_all_normal_affine_kernel': True,
            'physical_last_color_half_weight': True}


def survival_case(N, slopes):
    mp.mp.dps = 100
    tau, delta = mp.mpc('.4', '.5'), mp.mpf('.25')
    H = int(mp.floor(delta*N))
    actual, predicted = mp.mpf(N)**mp.mpf('1.5'), mp.mpf(N)**mp.mpf('1.5')
    minimum_amplitude, action = mp.inf, 0
    for p in slopes:
        q, Q, kappa, aa, beta, a = coefficients(N, -p)
        actual *= kappa**(-2*p)*mp.fsum(
            beta[N-h-1]*mp.exp(mp.pi*1j*tau*h*h/N) for h in range(H+1))
        saddle = -tau/(1+2*p*tau)
        critical = mp.pi*1j*tau/(1+2*p*tau)
        minus_hessian = 2j*mp.pi/tau+4j*mp.pi*p
        amplitude = (2*mp.sqrt(2*mp.pi)*(-1j*tau)**(-mp.mpf('.5'))
                     *mp.sinh(2j*mp.pi*saddle)/mp.sqrt(minus_hessian))
        predicted *= kappa**(-p)*amplitude*mp.exp(N*critical)
        minimum_amplitude = min(minimum_amplitude, abs(amplitude))
        action += critical
    error = abs(actual/predicted-1)
    assert minimum_amplitude > 0
    assert error < mp.mpf('.35')
    assert N*error < 80
    return {'N': N, 'signed_fixed_slopes': list(slopes), 'all_sources_and_chirps_retained': True,
            'predicted_nonzero_amplitude_minimum': float(minimum_amplitude),
            'predicted_action': [float(mp.re(action)), float(mp.im(action))],
            'relative_complex_error': float(error), 'N_times_error': float(N*error)}


if __name__ == '__main__':
    recurrence = [recurrence_case(N, P) for N in range(2, 13) for P in (-3, -2, 2, 3)]
    survival = [survival_case(N, slopes) for N, slopes in
                ((64, (5,)), (65, (-5,)), (128, (5,)), (129, (-5,)),
                 (256, (8,)), (257, (-8,)), (256, (5, -6)), (257, (-5, 6)),
                 (512, (5, -8)), (513, (-5, 8)))]
    result = {'status': 'PASS', 'exact_original_normal_source_kernel': recurrence,
              'complete_coherent_local_filling_survival': survival,
              'scope': 'Analytic quadratic packet calibration of the proved conditional/local source theorem; no discarded physical color complement or preferred-volume identification.'}
    Path(__file__).with_name('actual_pretzel_cusp_corridor_filling_survival_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(f'PASS {len(recurrence)} original full-jet coefficient families; {len(survival)} signed all-source corridor asymptotics')
