#!/usr/bin/env python3
"""Exact whole-word checks for the all-Hardy pole-graph pushforward.

Transfers are bare Laurent multiplication: no lower/upper projection.
Positive factorials retain their FULL negative Laurent coefficients.
Gaussian diagonals act on all signed indices. Original finite sources
are imposed only at the beginning and end of the entire word.
"""

import itertools
import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

from audit_actual_cyclic_hardy_dilog_network import CyclicHardyNetwork, cyclic_coefficients
from audit_actual_two_cut_ports import word_matrix, partial
from audit_actual_borel_regular_fusion import fusion


class BareLaurentNetwork(CyclicHardyNetwork):
    def __init__(self, N, M):
        super().__init__(N, M)
        self.raw_U, self.raw_V = cyclic_coefficients(N, self.p, self.Q, self.cyclic_order)
        self.negative_routes_seen = 0
        self.negative_factorial_inputs_seen = 0

    def diagonal(self, states, head, values):
        result = {}
        for state, coefficient in states.items():
            a = state[head]
            if values is self.fac:
                r = self.N - 1 - a
                if a < 0:
                    self.negative_factorial_inputs_seen += 1
                value = (self.N * pow(self.Q, r, self.p) * self.raw_V[r] % self.p
                         if 0 <= r <= self.cyclic_order else 0)
            else:
                value = values[a] if 0 <= a < len(values) else 0
            if coefficient * value % self.p:
                result[state] = coefficient * value % self.p
        return result

    def transfer(self, states, i, coefficients, raising_first):
        result = {}
        for state, coefficient in states.items():
            for h, value in enumerate(coefficients):
                if not value:
                    continue
                a, b = state[i], state[i + 1]
                a, b = (a + h, b - h) if raising_first else (a - h, b + h)
                self.negative_routes_seen += int(min(a, b) < 0)
                output = state[:i] + (a, b) + state[i + 2:]
                result[output] = (result.get(output, 0) + coefficient * value) % self.p
        return {s: c for s, c in result.items() if c}

    def gaussian(self, states, head, sign):
        return {s: c * pow(-1, s[head], self.p) * pow(self.x, -2 * sign * s[head], self.p)
                * pow(self.Q, sign * s[head] * (s[head] - 1) // 2, self.p) % self.p
                for s, c in states.items()}

    def crossing(self, states, letter):
        i, sign = abs(letter) - 1, 1 if letter > 0 else -1
        states = self.Ci(states, i)
        if sign > 0:
            states = self.transfer(states, i, self.u, True)
            states = self.gaussian(states, i + 1, sign)
        else:
            states = self.gaussian(states, i + 1, sign)
            states = self.transfer(states, i, self.v, True)
        states = self.C(states, i)
        scalar = self.kappa if sign > 0 else pow(self.kappa, -1, self.p)
        return {s: c * scalar % self.p for s, c in states.items() if c * scalar % self.p}

    def negative_branch(self, initial, sign, selected_stages):
        states = {initial: 1}
        operations = [('D', 1, self.inv), ('T', False, self.v),
                      ('D', 0, self.inv), ('D', 1, self.fac)]
        operations += ([('T', True, self.u), ('G', 1, sign)] if sign > 0
                       else [('G', 1, sign), ('T', True, self.v)])
        operations += [('D', 1, self.inv), ('D', 0, self.fac),
                       ('T', False, self.u), ('D', 1, self.fac)]
        stages = {1: (0, 0), 4 if sign > 0 else 5: (1, 1), 8: (2, 0)}
        selected_nonzero = 0
        for j, (kind, head, values) in enumerate(operations):
            if kind == 'D':
                states = self.diagonal(states, head, values)
            elif kind == 'T':
                states = self.transfer(states, 0, values, head)
            else:
                states = self.gaussian(states, head, values)
            if j in stages:
                stage, active = stages[j]
                if stage in selected_stages:
                    states = {s: c for s, c in states.items() if s[active] < 0}
                    selected_nonzero += int(bool(states))
        return states, selected_nonzero


def local_and_negative_current_checks():
    cases, branches, selected, surviving_negative = 0, 0, 0, 0
    for N in range(2, 7):
        for M in [1, 3]:
            H = BareLaurentNetwork(N, M)
            C, Ci, *_ = fusion(N, H.p, H.Q, [H.x, H.x], [0, 0])
            cup = H.C({(N - 1, 0): 1}, 0)
            assert all(min(s) >= 0 and max(s) < N for s in cup)
            for row in range(N * N):
                assert cup.get(divmod(row, N), 0) == int(C[row, (N - 1) * N])
            for source in itertools.product(range(N), repeat=2):
                column = source[0] * N + source[1]
                for sign, expected in [(1, H.plus), (-1, H.minus)]:
                    output = H.crossing({source: 1}, sign)
                    head = np.zeros(N * N, dtype=np.int64)
                    for state, value in output.items():
                        if min(state) < 0:
                            assert state[0] < 0 and 0 <= state[1] < N
                            surviving_negative += 1
                        else:
                            assert max(state) < N
                            head[state[0] * N + state[1]] = value
                    assert np.array_equal(head, expected[:, column])
                    cases += 1
                    if N <= 4:
                        for mask in range(1, 8):
                            states, nonzero = H.negative_branch(source, sign, {r for r in range(3) if mask & (1 << r)})
                            assert all(min(s) < 0 for s in states)
                            branches += 1
                            selected += nonzero
            for a in range(-N, 0):
                for b in range(N):
                    assert not H.Ci({(a, b): 1}, 0)
                    assert not H.Ci({(b, a): 1}, 0)
            assert H.negative_factorial_inputs_seen == 0
    assert selected > 0 and surviving_negative > 0
    return {'signed_original_head_columns_checked': cases,
            'nonempty_negative_current_subsets_checked': branches,
            'nonzero_inner_current_selections': selected,
            'nonzero_negative_outputs_retained_before_original_source': surviving_negative,
            'inverse_fusion_annihilates_either_negative_head': True,
            'bare_current_not_claimed_operator_zero': True}


def whole_word(N, M, heads, letters):
    H = BareLaurentNetwork(N, M)
    expected = partial(word_matrix(letters, H.plus, H.minus, heads, N, H.p), H.pivot, heads, N, H.p)
    cut = np.zeros((N, N), dtype=np.int64)
    negative_outputs = 0
    for source in itertools.product(range(N), repeat=heads):
        states = H.word(source, letters)
        for output, coefficient in states.items():
            assert sum(output) == sum(source)
            if min(output) < 0:
                negative_outputs += 1
                continue  # ORIGINAL finite nonnegative output source, only here.
            assert max(output) < N
            if output[1:] != source[1:]:
                continue
            weight = 1
            for j in source[1:]:
                weight = weight * int(H.pivot[j]) % H.p
            cut[output[0], source[0]] = (cut[output[0], source[0]] + weight * coefficient) % H.p
    assert np.array_equal(cut, expected)
    assert H.negative_factorial_inputs_seen == 0
    return {'N': N, 'M': M, 'heads': heads, 'word': letters,
            'whole_original_pivotal_cut_exact': True,
            'no_intermediate_Hardy_or_head_projection': True,
            'negative_outputs_killed_only_by_original_final_source': negative_outputs}


def pole_forest_jacobians():
    results = []
    for lengths in [[1], [2, 3], [4, 1, 2], [3, 3, 3]]:
        size = sum(length + 1 for length in lengths)
        matrix = sp.zeros(size)
        row = 0; column = 0
        for length in lengths:
            # z_j=root*prod_(e=j)^(length-1)u_e, modulo base-only g factors.
            for j in range(length + 1):
                matrix[row + j, column] = 1
                for e in range(j, length):
                    matrix[row + j, column + 1 + e] = 1
            row += length + 1; column += length + 1
        determinant = matrix.det()
        assert abs(determinant) == 1
        results.append({'head_segment_lengths': lengths, 'logarithmic_jacobian': int(determinant),
                        'each_normal_Cauchy_residue': 1})
    return results


def reduced_radius_cycle():
    rho, lam = mp.mpf(1) / 64, mp.mpf(1) / 3
    logsmall, loglarge = mp.log(rho / 2), mp.log(2 / rho)
    rows = []
    with mp.workdps(65):
        for letters in [[1, -2, 1, -2], [1, 2, 3, -2, -1, 3]]:
            heads = max(abs(k) for k in letters) + 1
            for xis in [[0] * len(letters), [30] * len(letters), [-30] * len(letters),
                        [(-1) ** j * (j + 1) for j in range(len(letters))]]:
                R = [mp.mpf(0)] * heads
                checks = []
                for letter, xi in zip(letters, xis):
                    i, sign = abs(letter) - 1, 1 if letter > 0 else -1
                    old1, old2 = R[i:i + 2]
                    logg = mp.log(9) + mp.sqrt(mp.pi) * xi
                    b = min(old2 + logsmall, old1 + mp.log(rho * lam / 2))
                    checks += [b - old2, b - old1 - mp.log(lam)]
                    a = old1 + logsmall
                    G = max(mp.mpf(0), logg) if sign < 0 else mp.mpf(0)
                    c = max(b + loglarge, a + mp.log(2 / (rho * lam)) + G)
                    checks += [a - old1, b - c]
                    after = c - logg
                    checks += [a - (after if sign < 0 else c) - mp.log(lam)]
                    e = min(after + logsmall, a + mp.log(rho * lam / 2))
                    f = a + loglarge
                    checks += [e - after, a - f, e - f - mp.log(lam), e - (e + loglarge)]
                    R[i], R[i + 1] = f, e + loglarge
                assert all(value < mp.log(rho) for value in checks)
                rows.append({'word': letters, 'Gaussian_coordinates': xis,
                             'all_reduced_cyclic_arguments_below_1_over_64': True,
                             'reset_or_Hardy_radius_inequalities_needed': False})
    return rows


def actual_classical_chart():
    A, J, z1, z2, x = sp.symbols('A J z1 z2 x', nonzero=True)
    K = 1 - (1 - A) * (1 - J) * z2 / (x * z1)
    U, V = A / K, J * K
    zout1 = z1 / (1 - A)
    zout2 = z2 * (1 - J) / (1 - J * K)
    pA, pJ, pU, pV = 1 / z1, 1 / z2, 1 / zout1, 1 / zout2
    assert sp.cancel(pU - (1 - A) * pA) == 0
    assert sp.cancel(pV - pJ * (1 - J * K) / (1 - J)) == 0
    assert sp.cancel(1 - pU * (1 - V) / (x * pV) - K) == 0
    assert sp.cancel(U * K - A) == sp.cancel(V / K - J) == 0
    assert sp.cancel(pU / (1 - A) - pA) == 0
    assert sp.cancel(pV * (1 - J) / (1 - V) - pJ) == 0
    return {'known_actual_fusion_chart': 'fusion_canonical_chart_and_retained_source_wall.md (8)-(9)',
            'head_clock_identification': ['B1=A', 'B2=J'],
            'remaining_head_coordinate_identification': ['z1=1/p_A', 'z2=1/p_J'],
            'rational_fusion_map_and_inverse_exactly_verified': True,
            'literal_five_flag_chart': ['X=x z2/z1', 'Z=B1'],
            'central_X_N_not_specialized': True,
            'geometric_cycle_coefficient': 'NOT established'}


def main():
    words = [whole_word(N, M, 3, [1, -2, 1, -2]) for N in [2, 3, 4] for M in [1, 3]]
    words += [whole_word(2, M, 4, [1, 2, 3, -2, -1, 3]) for M in [1, 3]]
    result = {'status': 'PASS', 'negative_current_and_original_column_checks': local_and_negative_current_checks(),
              'whole_original_words_after_pole_graph_pushforward': words,
              'unimodular_pole_forest_normal_coordinates': pole_forest_jacobians(),
              'explicit_reduced_radius_cycles': reduced_radius_cycle(),
              'actual_classical_chart_identification': actual_classical_chart(),
              'scope': 'Exact original-source Hardy forest residue reduction with all inner currents retained then proved source-null. No geometric thimble coefficient or volume limit claimed.'}
    Path(__file__).with_name('actual_hardy_forest_residue_results.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': 'PASS', 'whole_word_cases': len(words),
                      'signed_head_columns': result['negative_current_and_original_column_checks']['signed_original_head_columns_checked'],
                      'negative_current_subsets': result['negative_current_and_original_column_checks']['nonempty_negative_current_subsets_checked'],
                      'reduced_cycles': len(result['explicit_reduced_radius_cycles'])}))


if __name__ == '__main__':
    main()
