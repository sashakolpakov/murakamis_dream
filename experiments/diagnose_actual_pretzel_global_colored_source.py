#!/usr/bin/env python3
"""Original full-source mixed-color tests; no inferred global action gap."""

import itertools
import json
from pathlib import Path

import mpmath as mp


def all_color_nodes(N, dps):
    mp.mp.dps = dps
    d, M = N-1, (N-1)//2
    q = mp.exp(mp.pi*1j/N)
    Q, kappa = q*q, q**(mp.mpf(d*d)/2)
    sine = [mp.mpf(1)]
    for a in range(1, N):
        sine.append(sine[-1]*2*mp.sin(mp.pi*a/N))
    coefficients = []
    for r in range(N):
        row = [mp.mpf(0)]*N
        if r <= M:
            for v in range(r, M+1):
                row[v] = sine[d-v]**2*sine[2*v]/(sine[v-r]*sine[v+r])
        for t in range(1, min(r, N-r)+1):
            row[N-t] = ((-1)**(N-t-r)*sine[t-1]**2*sine[t+r-1]
                        /(sine[2*t-1]*sine[r-t]))
        coefficients.append(row)
    diagonal = [q+1/q-q*(1-Q**v)**2-(1-Q**(v+1))**2/q for v in range(N)]
    off = [-(1-Q**(v+1))**2 for v in range(N)]

    def node(c):
        f = [mp.mpc(1), (c-diagonal[0])/off[0]]
        derivative = [mp.mpc(0), 1/off[0]]
        for v in range(1, N-1):
            f.append(((c-diagonal[v])*f[-1]-off[v-1]*f[-2])/off[v])
            derivative.append((f[-2]+(c-diagonal[v])*derivative[-1]
                               -off[v-1]*derivative[-2])/off[v])
        values = [mp.fsum(a*b for a, b in zip(row, f))/kappa for row in coefficients]
        slopes = [mp.fsum(a*b for a, b in zip(row, derivative))/kappa for row in coefficients]
        return c, values, slopes

    doubles = [node(q**(2*j+1)+q**(-2*j-1)) for j in range(N//2)]
    simple = node(mp.mpf(-2)) if N % 2 else None

    def source(deficits):
        total = mp.mpc(0)
        for c, values, slopes in doubles:
            value, derivative = mp.mpc(1), mp.mpc(0)
            for r in deficits:
                derivative = derivative*values[r]+value*slopes[r]
                value *= values[r]
            total += (4-c*c)*derivative-c*value
        total *= (-1)**d
        if simple:
            total += mp.fprod(simple[1][r] for r in deficits)
        return total

    return source


def rate(value, N):
    return float(mp.log(abs(value))/N) if value else None


def diagonal_case(N, dps):
    source = all_color_nodes(N, dps)
    rows = []
    for s in (3, 5):
        homogeneous = [rate(source((r,)*s), N) for r in range(N)]
        single = [rate(source((r,)+(0,)*(s-1)), N) for r in range(N)]
        rows.append({'N': N, 'dps': dps, 'boxes': s,
                     'deficit_order': 'r=0,...,N-1; actual circle color j=N-r',
                     'all_equal_color_full_source_rates': homogeneous,
                     'one_changed_color_full_source_rates': single})
    return rows


def mixed_sample_case(N, dps):
    source = all_color_nodes(N, dps)
    pool = sorted(set((0, N//12, N//6, N//4, N//2, 3*N//4, N-1)))
    rows = []
    selected = []
    for s in (3, 5):
        maximum = None
        tested = 0
        for deficits in itertools.combinations_with_replacement(pool, s):
            if not any(deficits):
                continue
            value = source(deficits)
            tested += 1
            if maximum is None or abs(value) > abs(maximum[1]):
                maximum = deficits, value
        deficits, value = maximum
        selected.append((deficits, value))
        rows.append({'N': N, 'dps': dps, 'boxes': s,
                     'sample_deficits': pool, 'mixed_noncomplete_cases_tested': tested,
                     'sample_maximizer_deficits': list(deficits),
                     'sample_maximum_full_source_rate': rate(value, N),
                     'complete_source_rate': rate(source((0,)*s), N),
                     'sample_maximum_source_real': mp.nstr(mp.re(value), 45),
                     'sample_maximum_source_imaginary': mp.nstr(mp.im(value), 45)})
    # Replay selected maxima and complete sources, not just a rate fit.
    replay = all_color_nodes(N, 2*dps)
    for deficits, value in selected:
        assert abs(replay(deficits)/value-1) < mp.mpf('1e-80')
    return rows


if __name__ == '__main__':
    diagonal = []
    for N in (24, 48, 72):
        diagonal.extend(diagonal_case(N, max(160, 3*N)))
    mixed = mixed_sample_case(48, 160)
    Path(__file__).with_name('actual_pretzel_global_colored_source_diagnostics.json').write_text(
        json.dumps({'status': 'DIAGNOSTIC', 'all_equal_and_single_changed_colors': diagonal,
                    'mixed_color_samples_with_precision_replay': mixed,
                    'scope': 'Exact original mixed-color polynomials and full Phi2 normals; finite samples do not prove a global off-cusp action gap.'}, indent=2)+'\n')
    print('Saved full-source all-equal/single-color tests at 3 levels and 544 mixed samples, with selected-source doubled-precision replay; no asymptotic gap claim')
