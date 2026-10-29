#!/usr/bin/env python3
"""Exact off-critical identities and global radial clipping for actual source cores.

The uniform horizontal-lift argument is in the note. These diagnostics do
not bound the compact interior flow's Jacobian or prove a volume bound.
"""

import cmath
import itertools
import json
import math
from pathlib import Path

import networkx as nx
import numpy as np

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_global_charged_bridge_flow import setup, graph_blocks


def cores_from_actual(N, width, word, clocks):
    H = HardyNetwork(N, 1)
    S = setup(H, width, word)
    G = graph_blocks(H, S, clocks)
    q = [N-1]*G['anchor_count']
    factors = []
    for B in G['blocks']:
        a = cmath.exp(1j*math.pi*B['alpha_exp']/N)
        for r in range(B['length']):
            b = cmath.exp(1j*math.pi*(B['beta_exp']+2*r)/N)
            u, v = B['tail'], B['head']
            if u == v:
                if abs(a-b) < 1e-10:
                    return []
                q[u] -= 1
            else:
                factors.append((u, v, a, b))
    if min(q, default=0) < 0:
        return []
    F = nx.DiGraph()
    for j, (u, v, _, _) in enumerate(factors):
        F.add_edge('s', ('e', j), capacity=1)
        F.add_edge(('e', j), ('v', u), capacity=1)
        F.add_edge(('e', j), ('v', v), capacity=1)
    for i, charge in enumerate(q):
        F.add_edge(('v', i), 't', capacity=charge)
    value, flow = nx.maximum_flow(F, 's', 't')
    if value != len(factors):
        return []
    assigned = [next(i for i in (u, v) if flow[('e', j)].get(('v', i), 0))
                for j, (u, v, _, _) in enumerate(factors)]
    R = nx.DiGraph()
    R.add_nodes_from(range(len(q)))
    for (u, v, _, _), i in zip(factors, assigned):
        R.add_edge(i, v if i == u else u)
    components = list(nx.strongly_connected_components(R))
    index = {i: j for j, C in enumerate(components) for i in C}
    for (u, v, _, _), i in zip(factors, assigned):
        if index[u] != index[v]:
            q[i] -= 1
    answer = []
    for C in components:
        if len(C) < 2:
            continue
        vertices = sorted(C)
        labels = {v: i for i, v in enumerate(vertices)}
        FF = [(labels[u], labels[v], a, b) for u, v, a, b in factors
              if u in C and v in C]
        qq = [q[i] for i in vertices]
        assert sum(qq) == len(FF)
        answer.append((qq, FF))
    return answer


def cut(q, factors, I):
    inside = sum(u in I and v in I for u, v, _, _ in factors)
    C = sum((u in I) != (v in I) for u, v, _, _ in factors)
    return sum(q[i] for i in I)-inside, C


def gradient_log(q, factors, X):
    G = -np.asarray(q, dtype=complex)
    for u, v, a, b in factors:
        den = a*X[u]-b*X[v]
        if abs(den) < 1e-13:
            raise ValueError('diagnostic lies on zero divisor')
        G[u] += a*X[u]/den
        G[v] -= b*X[v]/den
    assert abs(sum(G)) < 5e-10
    return G


def log_modulus(q, factors, X):
    return (sum(math.log(abs(a*X[u]-b*X[v])) for u, v, a, b in factors)
            - sum(charge*math.log(abs(x)) for charge, x in zip(q, X)))


def clipped_log_radii(rho, M, s=1.):
    order = sorted(range(len(rho)), key=lambda i: rho[i])
    new = [0.]*len(rho)
    for u, v in zip(order, order[1:]):
        ratio = math.exp(rho[v]-rho[u])
        current = (1-s)*ratio+s*min(ratio, M)
        new[v] = new[u]+math.log(current)
    anchor = new[-1]
    return np.asarray([x-anchor for x in new])


def audit_core(q, factors, seed):
    k, M = len(q), len(factors)
    for mask in range(1, 2**k-1):
        I = {i for i in range(k) if mask >> i & 1}
        e, C = cut(q, factors, I)
        assert 1 <= e <= C-1
    rng = np.random.default_rng(seed)
    worst_derivative_error = 0.
    smallest_large_gap_derivative = math.inf
    largest_modulus_increase = -math.inf
    largest_lipschitz = 0.
    horizontal_error = 0.
    tests = 0
    for trial in range(18):
        order = list(rng.permutation(k))
        gaps = [math.log(M)+.3+.11*j if (trial+j) % 2 else .19+.07*j
                for j in range(k-1)]
        rho = np.zeros(k)
        for j, (u, v) in enumerate(zip(order, order[1:])):
            rho[v] = rho[u]+gaps[j]
        rho -= rho[-1]
        theta = rng.uniform(-math.pi, math.pi, k)
        theta -= theta[-1]
        X = np.exp(rho+1j*theta)
        G = gradient_log(q, factors, X)
        # Check every sorted high cut, including small gaps.
        for j, g in enumerate(gaps):
            I = set(order[j+1:])
            e, C = cut(q, factors, I)
            direct = sum(G[i].real for i in I)
            flux = 0.
            for u, v, a, b in factors:
                if (u in I) == (v in I):
                    continue
                ii, jj = (u, v) if u in I else (v, u)
                flux += (abs(X[ii])**2-abs(X[jj])**2)/abs(a*X[u]-b*X[v])**2
            formula = (C-2*e+flux)/2
            worst_derivative_error = max(worst_derivative_error, abs(direct-formula))
            assert abs(direct-formula) < 2e-8
            assert direct+1e-9 >= (C-2*e+C*math.tanh(g/2))/2
            if g >= math.log(M):
                assert direct+1e-9 >= 1/(M+1)
                smallest_large_gap_derivative = min(smallest_large_gap_derivative, direct)
                # A genuine complex horizontal right inverse, modulo common scale.
                V = np.asarray([int(i in I) for i in range(k)], dtype=complex)
                V -= V[-1]
                denominator = np.dot(G, V)
                H = V/denominator
                horizontal_error = max(horizontal_error, abs(np.dot(G, H)-1))
                assert np.linalg.norm(H) <= math.sqrt(k)*(M+1)+1e-8
        previous = log_modulus(q, factors, X)
        for s in (.1, .25, .5, .75, .95, 1.):
            target = clipped_log_radii(rho, M, s)
            now = log_modulus(q, factors, np.exp(target+1j*theta))
            largest_modulus_increase = max(largest_modulus_increase, now-previous)
            assert now <= previous+2e-8
            previous = now
        target = clipped_log_radii(rho, M)
        assert max(target)-min(target) <= (k-1)*math.log(M)+1e-10
        assert np.max(abs(clipped_log_radii(target, M)-target)) < 1e-10
        # Piecewise differential in the fixed X_k=1 logarithmic gauge.
        step = 1e-6
        A = np.zeros((k-1, k-1))
        for j in range(k-1):
            shift = np.zeros(k)
            shift[j] = step
            A[:, j] = ((clipped_log_radii(rho+shift, M)
                         - clipped_log_radii(rho-shift, M))/(2*step))[:-1]
        opnorm = float(np.linalg.norm(A, 2))
        largest_lipschitz = max(largest_lipschitz, opnorm)
        assert opnorm <= 4*k+1e-5
        assert np.max(abs(A-np.round(A))) < 1e-5
        tests += 1
    return {'anchors': k, 'unit_linear_factors': M, 'strict_Hall_all_cuts': True,
            'sampled_outside_configurations': tests,
            'max_exact_derivative_residual': worst_derivative_error,
            'min_large_gap_derivative': smallest_large_gap_derivative,
            'guaranteed_derivative_lower_bound': 1/(M+1),
            'max_successive_log_modulus_increase': largest_modulus_increase,
            'max_endpoint_log_radial_Lipschitz_sample': largest_lipschitz,
            'max_horizontal_right_inverse_residual': horizontal_error}


def main():
    rows = []
    cases = ((3, 3, [1, -2, 1, -2], [0, 0, 1, 2]),
             (4, 3, [1, -2, 1, -2], [0, 1, 1, 2]),
             (5, 3, [1, -2, 1, -2], [0, 2, 2, 3]),
             (3, 3, [1, -2, 1, 1, -2, -2], [0, 1, 1, 1, 0, 1]),
             (4, 3, [1, -2, 1, 1, -2, -2], [0, 1, 2, 2, 1, 1]),
             (3, 4, [1, -2, 3, 1, -2, 3], [0, 1, 1, 1, 1, 1]))
    for N, width, word, clocks in cases:
        for j, (q, FF) in enumerate(cores_from_actual(N, width, word, clocks)):
            result = audit_core(q, FF, 284710+len(rows))
            result.update(N=N, word=word, original_clocks=clocks, component=j)
            rows.append(result)
    assert len(rows) >= 4
    # Arbitrarily close roots do not enter the radial bound.
    FF = [(0, 1, 1.+0j, cmath.exp(1j*angle))
          for angle in (0., 1e-14, .8, 1.7, 2.4, 3.9)]
    clustered = audit_core([2, 4], FF, 290001)
    data = {'status': 'PASS', 'actual_original_source_strict_cores': rows,
            'arbitrarily_clustered_unit_roots': clustered,
            'scope': ('Uniform proof in note; no compact interior Jacobian/mass bound, '
                      'full-clock critical identification, or knot volume bound inferred.')}
    Path(__file__).with_name('actual_anchor_sublevel_radial_transport_results.json').write_text(
        json.dumps(data, indent=2)+'\n')
    print(f'PASS {len(rows)} actual strict source cores, radial clipping/horizontal identities, '
          'and clustered unit roots; no interior flow mass assertion')


if __name__ == '__main__':
    main()
