#!/usr/bin/env python3
"""Actual crossing HS gauge optimization with original paired endpoints.

No scalar knot value is input.  The objective uses the exact moduli of
the original complete crossing coefficients.  Source constraints are
eliminated by a signed union-find, and the remaining log-sum-exp problem
is minimized with an analytic gradient.
"""

import argparse
import json
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.optimize import minimize
from scipy.special import logsumexp


class SignedUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.sign = [1] * n
        self.zero = [False] * n

    def find(self, a):
        if self.parent[a] != a:
            old = self.parent[a]
            root, sign = self.find(old)
            self.parent[a] = root
            self.sign[a] *= sign
        return self.parent[a], self.sign[a]

    def join(self, a, b, sign):
        # Value(a)=sign*Value(b).
        ra, sa = self.find(a)
        rb, sb = self.find(b)
        if ra == rb:
            if sa != sign * sb:
                self.zero[ra] = True
            return
        self.parent[ra] = rb
        self.sign[ra] = sign * sb * sa
        self.zero[rb] = self.zero[rb] or self.zero[ra]


def crossing_support(n, sign):
    logs = np.concatenate(([0.], np.cumsum(np.log(2 * np.sin(np.pi * np.arange(1, n) / n)))))
    indices, weights = [], []
    for a in range(n):
        for b in range(n):
            for e in range(a + 1):
                c = a + b - e
                if c >= n:
                    continue
                indices.append((a, b, c, e) if sign > 0 else (b, a, e, c))
                weights.append(2 * (logs[c] + logs[a] - logs[a - e] - logs[b] - logs[e]))
    return np.array(indices, dtype=int), np.array(weights)


def wiring(width, word):
    current = list(range(width))
    vertices = []
    count = width
    for letter in word:
        i = abs(letter) - 1
        incoming = current[i:i + 2]
        outgoing = [count, count + 1]
        count += 2
        vertices.append(tuple(incoming + outgoing))
        current[i:i + 2] = outgoing
    return count, vertices, list(range(width)), current


def objective_data(n, width, word):
    count, vertices, bottom, top = wiring(width, word)
    union = SignedUnion(count * n)
    for boundary in (bottom, top):
        for pair in range(0, width, 2):
            for a in range(n):
                union.join(boundary[pair] * n + a,
                           boundary[pair + 1] * n + n - 1 - a, -1)
    roots = {}
    mapped = []
    for i in range(count * n):
        root, sign = union.find(i)
        if union.zero[root]:
            mapped.append((-1, 0))
        else:
            if root not in roots:
                roots[root] = len(roots)
            mapped.append((roots[root], sign))
    matrices, logweights = [], []
    for vertex, letter in zip(vertices, word):
        support, logweight = crossing_support(n, 1 if letter > 0 else -1)
        rows, columns, values = [], [], []
        for row, indices in enumerate(support):
            for leg, (edge, a) in enumerate(zip(vertex, indices)):
                column, orientation = mapped[edge * n + a]
                if column >= 0:
                    rows.append(row)
                    columns.append(column)
                    values.append(orientation * (-1 if leg < 2 else 1))
        matrix = sparse.csr_matrix((values, (rows, columns)),
                                   shape=(len(support), len(roots)))
        matrices.append(matrix)
        logweights.append(logweight)
    return matrices, logweights, len(roots)


def evaluate(y, matrices, logweights):
    value = 0.
    gradient = np.zeros_like(y)
    for matrix, weights in zip(matrices, logweights):
        logits = weights + 2 * (matrix @ y)
        normalizer = logsumexp(logits)
        value += normalizer / 2
        gradient += matrix.T @ np.exp(logits - normalizer)
    return float(value), gradient


def optimize(n, width, word, seed=712, iterations=1000):
    matrices, weights, size = objective_data(n, width, word)
    flat, gradient = evaluate(np.zeros(size), matrices, weights)
    rng = np.random.default_rng(seed)
    # At an exactly verified stationary flat point convexity certifies the
    # optimum. Starting there also avoids artificial slow relaxation in the
    # numerous harmless gauge-null directions of a random initialization.
    start = np.zeros(size) if np.linalg.norm(gradient) < 1e-11 else rng.normal(scale=.23, size=size)
    result = minimize(evaluate, start, args=(matrices, weights), jac=True,
                      method='L-BFGS-B', options={'maxiter': iterations,
                                                'ftol': 1e-13, 'gtol': 3e-9})
    return {'N': n, 'width': width, 'word': word, 'variables': size,
            'flat_log_HS_bound': flat, 'optimized_log_HS_bound': float(result.fun),
            'flat_gradient_norm': float(np.linalg.norm(gradient)),
            'improvement': float(flat - result.fun),
            'optimizer_success': bool(result.success),
            'optimizer_message': str(result.message),
            'iterations': int(result.nit)}


def exact_marginals(n):
    support, weights = crossing_support(n, 1)
    p = np.exp(weights - logsumexp(weights))
    marginals = [np.bincount(support[:, leg], weights=p, minlength=n) for leg in range(4)]
    assert np.max(abs(marginals[0] - marginals[2])) < 3e-14
    assert np.max(abs(marginals[1] - marginals[3])) < 3e-14
    assert np.max(abs(marginals[0] - marginals[1][::-1])) < 3e-14
    return {'N': n, 'transpose_and_charge_reflection_marginals': True}


def casimir_data(n):
    from audit_actual_weighted_fourier_plat_energy import data
    q, Q, x, fac, pivot, B, Fhat = data(n)
    F = np.zeros((n, n), complex)
    for a in range(n - 1):
        F[a + 1, a] = 1 - Q ** (a + 1)
    Ecal = -F.conj().T
    K = np.diag([x * Q ** (-a) for a in range(n)])
    I = np.eye(n)
    Ftot = np.kron(F, I) + np.kron(K.conj().T, F)
    Ecaltot = np.kron(Ecal, K) + np.kron(I, Ecal)
    Ktot = np.kron(K, K)
    Omega = Ftot @ Ecaltot + q * Ktot + (1 / q) * Ktot.conj().T
    assert np.linalg.norm(F @ Ecal + q * K + (1 / q) * K.conj().T + 2 * I) < 1e-9
    assert np.linalg.norm(Omega @ B - B @ Omega) < 1e-7
    assert np.linalg.norm(Omega, 2) <= 14 + 1e-10
    rows, values = [], []
    for k in range((n - 1) // 2 + 1):
        h = 2 * k + 1
        node = q ** h + q ** (-h)
        value = (-1) ** k * q ** (k * (k + 1))
        rows.append([node ** a for a in range(n)])
        values.append(value)
        if h < n:
            rows.append([0] + [a * node ** (a - 1) for a in range(1, n)])
            values.append(-value * (n - h) / (2 * (q ** h - q ** (-h))))
    coefficients = np.linalg.solve(np.array(rows), np.array(values))
    polynomial = np.zeros_like(B)
    power = np.eye(n * n)
    for coefficient in coefficients:
        polynomial += coefficient * power
        power = power @ Omega
    assert np.linalg.norm(polynomial - B) < 3e-7 * max(1, np.linalg.norm(B))
    return q, Q, B, Omega


def twist_checks():
    rows = []
    base = 7 + 5 * np.sqrt(2)
    for n in range(2, 11):
        q, Q, B, Omega = casimir_data(n)
        for power in (1, 2, 3, 5, -1, -3):
            matrix = np.linalg.matrix_power(B, power)
            # Proved all-N bound in the note; numerical test is supplementary.
            upper = 32 * n ** 2 * (1 + abs(power)) * base ** n
            norm = np.linalg.norm(matrix, 2)
            assert norm <= upper * (1 + 1e-10)
            rows.append({'N': n, 'power': power, 'operator_norm': float(norm),
                         'uniform_length_independent_exponential_bound': float(upper)})
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--full', action='store_true')
    args = parser.parse_args()
    examples = [(4, [2, -1, 2, 2]),
                (4, [1, -2, 3, -2, 1, 3]),
                (6, [1, -2, 3, -4, 5, -4, 3, -2, 1]),
                (4, [2, 2, 2, -1, 2, 2, 2]),
                (4, [1, -1]),
                (4, [2, 1, 2, -1])]
    levels = (4, 8, 12) if not args.full else (4, 8, 12, 16, 24)
    records = [optimize(n, width, word) for n in levels for width, word in examples]
    for record in records:
        width, word = record['width'], record['word']
        alternating = all((1 if letter > 0 else -1) == (-1) ** (abs(letter) + 1)
                          for letter in word) or all(
                              (1 if letter > 0 else -1) == (-1) ** abs(letter) for letter in word)
        if alternating:
            assert record['flat_gradient_norm'] < 2e-12
            assert abs(record['improvement']) < 2e-7
    result = {'status': 'PASS', 'marginals': [exact_marginals(n) for n in range(2, 33)],
              'optimization': records, 'twist_blocks': twist_checks(),
              'scope': 'Original endpoint-preserving convex crossing gauges; no sharp volume equality.'}
    Path(__file__).with_name('actual_convex_gauge_block_energy_results.json').write_text(
        json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': 'PASS', 'marginal_levels': len(result['marginals']),
                      'optimized_original_networks': len(records),
                      'twist_block_checks': len(result['twist_blocks'])}))


if __name__ == '__main__':
    main()
