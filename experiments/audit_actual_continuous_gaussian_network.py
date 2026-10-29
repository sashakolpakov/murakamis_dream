#!/usr/bin/env python3
"""Check the original cyclic/Hardy network with ordinary Gaussian moments.

No finite Gamma kernel is used in the whole-word evaluation. Gaussian
dilations are kept as independent monomials until the entire signed word
has been formed, then the exact ordinary-Gaussian moment is applied.
Fibered radius and domination constants are checked separately.
"""

from collections import defaultdict
import itertools
import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_cyclic_hardy_dilog_network import CyclicHardyNetwork, elementary_gates
from audit_actual_two_cut_ports import word_matrix, partial


class ContinuousGaussianNetwork(CyclicHardyNetwork):
    def __init__(self, N, M):
        super().__init__(N, M)
        self.largest_history_array = 0

    def apply_to_histories(self, states, operation):
        groups = defaultdict(dict)
        for (physical, history), coefficient in states.items():
            groups[history][physical] = coefficient
        result = {}
        for history, group in groups.items():
            for physical, coefficient in operation(group).items():
                key = physical, history
                result[key] = (result.get(key, 0) + coefficient) % self.p
        return {key: value for key, value in result.items() if value}

    def dilation(self, states, head, sign):
        c = -pow(self.x, -2 * sign, self.p) * pow(self.q, -sign, self.p) % self.p
        result = {}
        for (physical, history), coefficient in states.items():
            degree = physical[head]
            assert degree < self.N  # Checked, not imposed as an operator cut.
            key = physical, history + (degree,)
            result[key] = (result.get(key, 0) + coefficient * pow(c, degree, self.p)) % self.p
        self.largest_history_array = max(self.largest_history_array, len(result))
        return {key: value for key, value in result.items() if value}

    def word(self, initial, letters):
        states = {(initial, ()): 1}
        signs = []
        for letter in letters:
            i, sign = abs(letter) - 1, 1 if letter > 0 else -1
            states = self.apply_to_histories(states, lambda z: self.Ci(z, i))
            if sign > 0:
                states = self.apply_to_histories(states, lambda z: self.transfer(z, i, self.u, True))
                states = self.dilation(states, i + 1, sign)
            else:
                states = self.dilation(states, i + 1, sign)
                states = self.apply_to_histories(states, lambda z: self.transfer(z, i, self.v, True))
            states = self.apply_to_histories(states, lambda z: self.C(z, i))
            scalar = self.kappa if sign > 0 else pow(self.kappa, -1, self.p)
            states = {key: value * scalar % self.p for key, value in states.items() if value * scalar % self.p}
            signs.append(sign)
        # E exp(sum alpha_s k_s xi_s)=prod q^(s k_s^2), variance 1/N.
        result = {}
        for (physical, history), coefficient in states.items():
            moment = pow(self.q, sum(s * k * k for s, k in zip(signs, history)), self.p)
            result[physical] = (result.get(physical, 0) + coefficient * moment) % self.p
        return {key: value for key, value in result.items() if value}


def phase_checks():
    count = 0
    for N in range(2, 13):
        for M in [1, 3]:
            H = ContinuousGaussianNetwork(N, M)
            for sign in [-1, 1]:
                c = -pow(H.x, -2 * sign, H.p) * pow(H.q, -sign, H.p) % H.p
                for a in range(2 * N + 1):
                    moment = pow(c, a, H.p) * pow(H.q, sign * a * a, H.p) % H.p
                    literal = (pow(-1, a, H.p) * pow(H.x, -2 * sign * a, H.p)
                               * pow(H.Q, sign * a * (a - 1) // 2, H.p)) % H.p
                    assert moment == literal
                    count += 1
    return {'exact_both_sign_gaussian_phase_checks': count,
            'c_s': '-x^(-2s) exp(-s h/2)',
            'alpha_s': 'sqrt(pi)(1+i s)',
            'variance': '1/N'}


def whole_word(N, M, heads, letters):
    H = ContinuousGaussianNetwork(N, M)
    expected = partial(word_matrix(letters, H.plus, H.minus, heads, N, H.p),
                       H.pivot, heads, N, H.p)
    cut = np.zeros((N, N), dtype=np.int64)
    for source in itertools.product(range(N), repeat=heads):
        for output, coefficient in H.word(source, letters).items():
            assert sum(output) == sum(source) and max(output) < N
            if output[1:] != source[1:]:
                continue
            weight = 1
            for j in source[1:]:
                weight = weight * int(H.pivot[j]) % H.p
            cut[output[0], source[0]] = (cut[output[0], source[0]] + weight * coefficient) % H.p
    assert np.array_equal(cut, expected)
    assert H.high_transfer_terms_used == H.high_reciprocal_inputs_seen == 0
    scalar = int(cut.sum()) * pow(N, -1, H.p) % H.p
    external = H.dimension * pow(H.twist, -sum(1 if s > 0 else -1 for s in letters), H.p) % H.p
    return {'N': N, 'M': M, 'heads': heads, 'word': letters,
            'whole_original_pivotal_cut_equal_after_joint_Gaussian_moments': True,
            'finite_Gamma_kernel_used': False,
            'largest_joint_history_array': H.largest_history_array,
            'original_full_period': scalar * external % H.p}


def analytic_moment_checks():
    rows = []
    with mp.workdps(65):
        for N in [2, 3, 5]:
            h = 2j * mp.pi / N
            x = -mp.exp(-h / 2)
            for a in sorted({1, N - 1}):
                for sign in [-1, 1]:
                    alpha = mp.sqrt(mp.pi) * (1 + sign * 1j)
                    c = -x ** (-2 * sign) * mp.exp(-sign * h / 2)
                    integrand = lambda t: mp.exp(-N * t * t / 2) * (c * mp.exp(alpha * t)) ** a
                    actual = mp.sqrt(N / (2 * mp.pi)) * mp.quad(integrand, [-mp.inf, 0, mp.inf])
                    expected = (-1) ** a * x ** (-2 * sign * a) * mp.exp(sign * h * (a * a - a) / 2)
                    error = abs(actual - expected)
                    assert error < mp.mpf('1e-45')
                    rows.append({'N': N, 'sign': sign, 'degree': a, 'absolute_error': float(error)})
    return rows


def fibered_radius_checks():
    rho = mp.mpf(1) / 16
    lam, color_max, Cc = mp.mpf(1) / 3, mp.mpf(3), mp.mpf(9)
    creset = min(rho / 2, rho * rho * lam / 4)
    cstar = creset * rho / (2 * Cc)
    configurations = [(3, [1, -2, 1, -2]), (4, [1, 2, 3, -2, -1, 3])]
    rows = []
    with mp.workdps(65):
        for heads, letters in configurations:
            patterns = [[0] * len(letters), [50] * len(letters), [-50] * len(letters),
                        [(-1) ** j * (j + 1) for j in range(len(letters))]]
            for xis in patterns:
                previous = [mp.mpf(0)] * heads
                processed, accumulated_abs, stages = 0, mp.mpf(0), 0
                for letter in letters:
                    sign = 1 if letter > 0 else -1
                    for gate in elementary_gates([letter]):
                        incoming = [v + mp.log(rho / 2) for v in previous]
                        if gate[0] == 'transfer':
                            numerator, denominator = gate[1:]
                            incoming[numerator] = min(incoming[numerator], incoming[denominator] + mp.log(rho * lam / 2))
                            assert incoming[numerator] - incoming[denominator] - mp.log(lam) < mp.log(rho)
                        assert all(v - R < mp.log(rho) for v, R in zip(incoming, previous))
                        outgoing = [v + mp.log(rho / 2) for v in incoming]
                        if gate[0] == 'Fdiag':
                            outgoing[gate[1]] = incoming[gate[1]] + mp.log(2 / rho)
                            assert incoming[gate[1]] - outgoing[gate[1]] < mp.log(rho)
                        elif gate[0] == 'Gaussian':
                            xi = mp.mpf(xis[processed]); processed += 1
                            accumulated_abs += abs(xi)
                            head = gate[1]
                            outgoing[head] = incoming[head] + mp.log(rho / (2 * Cc)) - 2 * abs(xi)
                            for modulus in [mp.mpf(1), color_max]:
                                log_argument = -2 * sign * mp.log(modulus) + mp.sqrt(mp.pi) * xi + outgoing[head] - incoming[head]
                                assert log_argument < mp.log(rho)
                        elif gate[0] == 'Udiag':
                            assert outgoing[gate[1]] - incoming[gate[1]] < mp.log(rho)
                        for head in range(heads):
                            if gate[0] in ['Fdiag', 'Gaussian', 'Udiag'] and head == gate[1]:
                                continue
                            assert outgoing[head] - incoming[head] < mp.log(rho)
                        stages += 1
                        assert max(outgoing) < mp.mpf('1e-50')
                        assert min(outgoing) >= stages * mp.log(cstar) - 2 * accumulated_abs - mp.mpf('1e-50')
                        previous = outgoing
                assert processed == len(letters)
                rows.append({'heads': heads, 'word': letters, 'gaussian_coordinates': xis,
                             'all_fibered_radius_inequalities': True,
                             'global_linear_log_radius_bound': True})
    return rows


def initial_cyclic_phase_checks():
    rows = []
    with mp.workdps(65):
        for N in [16, 32, 64]:
            h = 2j * mp.pi / N; Q = mp.exp(h)
            for t in [mp.mpc('.03', '.02'), mp.mpc('-.025', '.01')]:
                actual = ((N - 1) / mp.mpf(2 * N) * mp.log(1 - t ** N)
                          - sum(mp.mpf(j) / N * mp.log(1 - Q ** j * t) for j in range(1, N)))
                leading = mp.polylog(2, t) / h + mp.log(1 - t) / 2
                assert abs(actual - leading) * N < mp.mpf('.1')
                rows.append({'N': N, 'argument': str(t), 'N_times_log_remainder': float(abs(actual - leading) * N)})
    return rows


def main():
    words = [whole_word(N, M, 3, [1, -2, 1, -2]) for N in [2, 3, 4] for M in [1, 3]]
    words += [whole_word(2, M, 4, [1, 2, 3, -2, -1, 3]) for M in [1, 3]]
    result = {'status': 'PASS', 'exact_gaussian_phases': phase_checks(),
              'whole_original_words_with_continuous_moments': words,
              'analytic_real_gaussian_moment_checks': analytic_moment_checks(),
              'fibered_torus_and_linear_radius_bound_checks': fibered_radius_checks(),
              'initial_cycle_cyclic_leading_phase_checks': initial_cyclic_phase_checks(),
              'scope': 'Exact original cyclic-dilog/continuous-Gaussian period over fibered tori. Uniform initial-cycle symbols only; no geometric deformation, period noncancellation, or volume theorem.'}
    Path(__file__).with_name('actual_continuous_gaussian_network_results.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': 'PASS', 'whole_original_word_cases': len(words),
                      'real_gaussian_moments': len(result['analytic_real_gaussian_moment_checks']),
                      'fibered_radius_configurations': len(result['fibered_torus_and_linear_radius_bound_checks'])}))


if __name__ == '__main__':
    main()
