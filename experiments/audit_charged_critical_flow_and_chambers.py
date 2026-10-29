#!/usr/bin/env python3
"""Actual source radial identity and complete two-anchor critical audits."""

import cmath
import itertools
import json
import math
from pathlib import Path

import sympy as sp

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_global_charged_bridge_flow import setup, graph_blocks


def actual_flow():
    results = []
    for N in (3, 4, 5, 7):
        H = HardyNetwork(N, 1)
        for width, word in ((3, [1, -2, 1, -2]),
                            (3, [1, 1, 1, 2, -1, 2]),
                            (3, [1, -2, 1, 1, -2, -2])):
            S = setup(H, width, word)
            hs = [(N-1)//2]*len(word)
            G = graph_blocks(H, S, hs)
            k, d = G['anchor_count'], N-1
            X = [cmath.exp(.07*(i-k/2)+1j*(.317*i+.073*i*i+.21)) for i in range(k)]
            gradient = [-complex(d)]*k
            incidence, flux = [0]*k, [0.]*k
            edges, bad = [], False
            for block in G['blocks']:
                u, v = block['tail'], block['head']
                for r in range(block['length']):
                    aa = cmath.exp(1j*math.pi*block['alpha_exp']/N)
                    bb = cmath.exp(1j*math.pi*(block['beta_exp']+2*r)/N)
                    L = aa*X[u]-bb*X[v]
                    if abs(L) < 1e-12:
                        bad = True
                        break
                    gradient[u] += aa*X[u]/L
                    gradient[v] -= bb*X[v]/L
                    incidence[u] += 1
                    incidence[v] += 1
                    value = (abs(X[u])**2-abs(X[v])**2)/abs(L)**2
                    flux[u] += value
                    flux[v] -= value
                    edges.append((u, v, value))
                if bad:
                    break
            if bad:
                continue
            delta = [s-2*d for s in incidence]
            residual = max(abs(2*g.real-a-b) for g, a, b in zip(gradient, delta, flux))
            assert residual < 2e-10
            count = 0
            for mask in range(1, 2**k-1):
                I = {i for i in range(k) if mask & (1 << i)}
                internal = sum(u in I and v in I for u, v, _ in edges)
                cross = sum((u in I) != (v in I) for u, v, _ in edges)
                deficit = d*len(I)-internal
                assert sum(delta[i] for i in I) == cross-2*deficit
                cut_flux = sum(value if u in I else -value
                               for u, v, value in edges if (u in I) != (v in I))
                direct = sum(2*gradient[i].real-delta[i] for i in I)
                assert abs(direct-cut_flux) < 5e-10
                count += 1
            results.append({'N': N, 'word': word, 'anchors': k,
                            'all_nontrivial_cuts_checked': count,
                            'maximum_radial_identity_residual': residual})
    assert len(results) >= 8
    return results


def critical_sets():
    z = sp.Symbol('z')
    rows = []
    # Exact unit phases; multiplicities exercise the removed singular criticals.
    for multiplicities in ((1, 1, 1, 1), (2, 1, 1, 0),
                           (3, 2, 0, 1), (2, 2, 2, 2)):
        roots = (1, sp.I, -1, -sp.I)
        P = sp.Poly(sp.prod((z-r)**m for r, m in zip(roots, multiplicities)), z, extension=sp.I)
        M = sum(multiplicities)
        for charge in range(1, M):
            G = sp.Poly(z*P.diff().as_expr()-charge*P.as_expr(), z, extension=sp.I)
            regular = G.exquo(sp.gcd(G, P))
            vals = sp.nroots(regular.as_expr(), n=45, maxsteps=300)
            phases = sorted(float(sp.arg(r)) % (2*math.pi)
                            for r, m in zip(roots, multiplicities) if m)
            chamber_counts = [0]*len(phases)
            max_residual = 0.
            radii = []
            for zz in vals:
                val = complex(zz)
                rr = abs(val)
                radii.append(rr)
                critical = sum(m*val/(val-complex(r)) for r, m in zip(roots, multiplicities) if m)-charge
                max_residual = max(max_residual, abs(critical))
                assert abs(critical) < 1e-9
                ratio_bound = max(charge, M-charge)/min(charge, M-charge)
                assert max(rr, 1/rr) <= ratio_bound*(1+1e-9)
                if 2*charge == M:
                    assert abs(rr-1) < 1e-10
                    theta = cmath.phase(val) % (2*math.pi)
                    for j, left in enumerate(phases):
                        span = (phases[(j+1) % len(phases)]-left) % (2*math.pi)
                        offset = (theta-left) % (2*math.pi)
                        if 1e-10 < offset < span-1e-10:
                            chamber_counts[j] += 1
                            break
                    else:
                        raise AssertionError('critical on excluded zero boundary')
            if 2*charge == M:
                assert chamber_counts == [1]*len(phases)
            rows.append({'multiplicities_at_1_i_minus1_minusi': multiplicities,
                         'charge': charge, 'regular_critical_count': len(vals),
                         'all_regular_radii': radii,
                         'critical_equation_residual': max_residual,
                         'balanced_chamber_counts': chamber_counts if 2*charge == M else None})
    # Balance and regular critical nondegeneracy alone do not select a period.
    assert sp.Poly((z-1)*(z+1), z).nth(1) == 0
    # Same-source Parseval subcase: no opposite-sign chambers; coefficient !=0.
    positive = sp.Poly((z-1)**2*(z-sp.I)**2, z)
    assert sp.simplify(positive.nth(2)-4*sp.I) == 0
    return rows


def sorted_factor_bound():
    rows = []
    for N in range(2, 31):
        values = sorted(2*abs(math.sin(math.pi*j/N)) for j in range(1, N))
        assert all(v+1e-14 >= 2*j/N for j, v in enumerate(values, 1))
        rows.append(N)
    return rows


def main():
    data = {'status': 'PASS', 'actual_radial_and_cut_identities': actual_flow(),
            'complete_univariate_critical_sets': critical_sets(),
            'distinct_root_factor_lower_bounds_N': sorted_factor_bound(),
            'scope': 'Direct identities and complete polynomial root checks; general graph proofs in note, no full clock selection or knot volume limit inferred.'}
    Path(__file__).with_name('charged_critical_flow_and_chambers_results.json').write_text(json.dumps(data, indent=2)+'\n')
    print('PASS actual-source radial/cut identities, complete unit-factor critical sets, balanced chambers and cancellation distinction')


if __name__ == '__main__':
    main()
