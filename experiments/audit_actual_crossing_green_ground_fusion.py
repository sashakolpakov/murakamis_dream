#!/usr/bin/env python3
"""Original positive crossing as exact nilpotent fusion-to-ground transport."""

import itertools
import json
from pathlib import Path

import numpy as np

from audit_actual_hardy_cauchy_network import HardyNetwork, whole_word


def gate_clock(H, m):
    N, p = H.N, H.p
    out = np.zeros((N*N, N*N), dtype=np.int64)
    for a, b in itertools.product(range(N), repeat=2):
        states = H.Ci({(a, b): 1}, 0)
        states = {s: c*pow(H.Q, m*s[1], p) % p for s, c in states.items()}
        states = H.transfer(states, 0, H.u, True)
        states = H.diagonal(states, 1, H.diag)
        states = H.C(states, 0)
        for (c, d), coefficient in states.items():
            assert max(c, d) < N
            out[c*N+d, a*N+b] = coefficient
    return out


def pochhammer(H, z, count):
    answer = 1
    for j in range(count):
        answer = answer*(1-z*pow(H.Q, j, H.p)) % H.p
    return answer


def ground(H, m):
    N, p = H.N, H.p
    out = np.zeros((N*N, N*N), dtype=np.int64)
    for a, b in itertools.product(range(N), repeat=2):
        if a+b >= N:
            continue
        coefficient = (pow(H.Q, m*b, p)*pow(H.x, -b, p)
                       *H.fac[a+b]*H.inv[a]*H.inv[b]
                       *pochhammer(H, pow(H.Q, m, p)*pow(H.x, -2, p) % p, a)) % p
        out[(a+b)*N, a*N+b] = coefficient
    return out


def shift_ac(H, matrix):
    N, p = H.N, H.p
    out = np.zeros_like(matrix)
    for a in range(1, N):
        for b in range(N):
            for c in range(N):
                for d in range(1, N):
                    out[c*N+d, a*N+b] = int(matrix[c*N+d-1, (a-1)*N+b])*pow(H.x, -1, p) % p
    return out


def green_matrix(H):
    answer = np.zeros((H.N*H.N, H.N*H.N), dtype=np.int64)
    for j in range(H.N):
        term = ground(H, j)
        for _ in range(j):
            term = shift_ac(H, term)
        answer = (answer+term) % H.p
    return answer


def closed_coefficient(H):
    N, p = H.N, H.p
    out = np.zeros((N*N, N*N), dtype=np.int64)
    for a, b in itertools.product(range(N), repeat=2):
        for j in range(a+1):
            first = a+b-j
            if first >= N:
                continue
            coefficient = (pow(H.x, -b-j, p)*pow(H.Q, j*b, p)
                           *H.fac[first]*H.inv[a-j]*H.inv[b]
                           *pochhammer(H, pow(H.Q, j, p)*pow(H.x, -2, p) % p, a-j)) % p
            out[first*N+j, a*N+b] = coefficient
    return out


class GreenNetwork(HardyNetwork):
    def __init__(self, N, M):
        super().__init__(N, M)
        self.green = green_matrix(self)*self.kappa % self.p

    def crossing(self, states, letter):
        N, p = self.N, self.p
        i = abs(letter)-1
        matrix = self.green if letter > 0 else self.minus
        answer = {}
        for state, weight in states.items():
            col = state[i]*N+state[i+1]
            for c, d in itertools.product(range(N), repeat=2):
                value = int(matrix[c*N+d, col])*weight % p
                if value:
                    key = state[:i]+(c, d)+state[i+2:]
                    answer[key] = (answer.get(key, 0)+value) % p
        return {s: v for s, v in answer.items() if v}


def main():
    families = []
    words = []
    for N in range(2, 9):
        for M in [1, 3]:
            try:
                H = GreenNetwork(N, M)
            except ValueError:
                continue
            for m in range(N+1):
                Km, Knext, Hm = gate_clock(H, m), gate_clock(H, m+1), ground(H, m)
                assert np.array_equal((Km-shift_ac(H, Knext)) % H.p, Hm)
            GG = green_matrix(H)
            assert np.array_equal(GG, closed_coefficient(H))
            assert np.array_equal(GG*H.kappa % H.p, H.plus % H.p)
            assert np.count_nonzero(ground(H, 0)[::N]) >= N
            nil = gate_clock(H, 0)
            for _ in range(N):
                nil = shift_ac(H, nil)
            assert not nil.any()
            families.append({'N': N, 'M': M, 'all_clock_Ward_identities': N+1,
                             'original_positive_crossing_Green_equal': True,
                             'explicit_ground_coefficients': True,
                             'finite_input_nilpotence': True})
            if N <= 4:
                for heads, word in [(3, [1, -2, 1, -2]), (4, [2, -1, 3, 2])]:
                    words.append(whole_word(H, heads, word))
    output = {'status': 'PASS', 'original_finite_head_families': families,
              'whole_signed_original_pivotal_sources': words,
              'scope': ('Exact original local source Ward and nilpotent Green fusion. '
                        'No global geometric noncancellation inferred.')}
    Path(__file__).with_name('actual_crossing_green_ground_fusion_results.json').write_text(
        json.dumps(output, indent=2)+'\n')
    print(f'PASS {len(families)} original finite-head families, clock Ward/Green/ground '
          f'identities and {len(words)} whole signed pivotal sources')


if __name__ == '__main__':
    main()
