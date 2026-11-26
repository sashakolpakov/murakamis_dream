#!/usr/bin/env python3
"""Finite diagnostic of the grouped face in regular-support cells (18).

This computes the actual original complete-source value and first-normal
data. It does not replace those data by an asymptotic expansion. A small
fixed batch is repeated at higher precision; no asymptotic or interval
certificate is asserted.
"""
from pathlib import Path
import hashlib
import json

import mpmath as mp


def evaluate(level, digits):
    with mp.workdps(digits):
        N = level
        assert N % 6 == 0
        m, j, n = N // 2, N // 3, 3
        theta = mp.pi / N
        nodes = [2 * mp.cos((2*a + 1)*theta) for a in range(m)]
        sines = [mp.sin((2*a + 1)*theta) for a in range(m)]
        inverse_qprime = [2*(-1)**a*sines[a]/N for a in range(m)]
        sine_factors = [2*mp.sin(k*theta) for k in range(N)]

        # Literal low complete kernel L_N(c_a)=sum_{k<=a} e_k(-2)e_k(c_a).
        complete_newton = [mp.mpf(1)]
        for k in range(1, m):
            complete_newton.append(complete_newton[-1]
                                   * (nodes[k-1]+2)/sine_factors[k]**2)
        values = []
        for a in range(m):
            newton = mp.mpf(1)
            terms = [mp.mpf(1)]
            for k in range(1, a+1):
                newton *= (nodes[k-1]-nodes[a])/sine_factors[k]**2
                terms.append(complete_newton[k]*newton)
            values.append(mp.fsum(terms))

        angles = [mp.pi-(2*a+1)*theta for a in range(m)]
        phases = [mp.exp(1j*n*N*t*t/(4*mp.pi)) for t in angles]
        hvalues = [phases[a]*values[a] for a in range(m)]
        weights = []
        for a in range(m):
            # h'-I(h)' = R' L + R D L - D(R L), with the exact
            # Chebyshev-Gauss differentiation matrix. Its diagonal cancels.
            defect = (1j*n*N*angles[a]/(4*mp.pi*sines[a])*hvalues[a]
                      + mp.fsum(
                          inverse_qprime[b]
                          / (inverse_qprime[a]*(nodes[a]-nodes[b]))
                          * (phases[a]-phases[b])*values[b]
                          for b in range(m) if b != a))
            # eta=-1. The unit carrier C_{N,3} cancels in the requested
            # ratio and in every recorded absolute value, so is omitted.
            weights.append(-N*N*inverse_qprime[a]**2*defect)

        x = (mp.mpf(j)+mp.mpf('0.5')+mp.mpc(0, '0.15'))/N
        row = mp.sin(mp.pi*N*x)/(N*mp.sin(mp.pi*x))
        rows = [row]
        for a in range(1, m):
            row *= (mp.sin(mp.pi*(x+mp.mpf(a)/N))
                    / mp.sin(mp.pi*(mp.mpf(a)/N-x)))
            rows.append(row)

        inserted = weights[j]*rows[j]
        retained = mp.fsum(weights[a]*rows[a] for a in range(j+1, m))
        ratio = 1+2*retained/inserted
        jump = inserted**2*ratio
        # Independent arithmetic expression for the exact grouped jump.
        direct = (retained+inserted)**2-retained**2
        identity_error = abs(jump-direct)/max(1, abs(jump), abs(direct))
        assert identity_error < mp.mpf(10)**(-digits+15)
        return {
            'ratio_real': +ratio.real,
            'ratio_imaginary': +ratio.imag,
            'log_ratio_modulus_over_N': +(mp.log(abs(ratio))/N),
            'third_term_rate': +(mp.log(abs(inserted**2))/N),
            'grouped_jump_rate': +(mp.log(abs(jump))/N),
            'largest_retained_summand_rate': +max(
                mp.log(abs(weights[a]*rows[a]))/N for a in range(j+1, m)),
            'retained_sum_rate': +(mp.log(abs(retained))/N),
        }, +identity_error


def main():
    root = Path(__file__).resolve().parents[1]
    dependencies = [Path(__file__).resolve(),
                    root/'notes/research_pair_regular_support_cells.md',
                    root/'notes/research_trace_normal_defect_positive_form.md']
    report = {
        'status': 'diagnostic_in_progress',
        'scope': ('Actual finite source only; this is not an outward certificate '
                  'or a proof of the grouped-current asymptotic rate. Pointwise '
                  'values do not determine the signed vertical integral.'),
        'parameters': {'n': 3, 'p': 3, 'j': 'N/3',
                       'x': '(j+1/2+3i/20)/N'},
        'quantity': '(F_j-F_{j+1})/(u_{3,j}^2 B_j^2) = '
                    '1+2 A_{3,j+1}/(u_{3,j} B_j)',
        'precisions_decimal': [150, 220],
        'rows': [],
        'sha256': {str(p.relative_to(root)):
                   hashlib.sha256(p.read_bytes()).hexdigest() for p in dependencies},
    }
    output = root/'repro/results/research-grouped-pair-shared-face-diagnostic.json'
    for N in (12, 24, 48, 72, 96):
        first, _ = evaluate(N, 150)
        second, identity_error = evaluate(N, 220)
        with mp.workdps(230):
            difference = max(abs(first[k]-second[k])/max(1, abs(second[k]))
                             for k in first)
            assert difference < mp.mpf('1e-125'), (N, difference)
            row = {'N': N, **{k: mp.nstr(v, 32) for k, v in second.items()},
                   'precision_replay_relative_difference': mp.nstr(difference, 8),
                   'jump_identity_relative_error': mp.nstr(identity_error, 8)}
        report['rows'].append(row)
        output.write_text(json.dumps(report, indent=2)+'\n')
        print(json.dumps(row), flush=True)
    report['status'] = 'diagnostic_complete'
    output.write_text(json.dumps(report, indent=2)+'\n')


if __name__ == '__main__':
    main()
