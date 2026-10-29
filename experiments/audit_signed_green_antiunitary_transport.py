#!/usr/bin/env python3
"""Both original crossing signs, antiunitary phases, and flat Green conditioning."""

import itertools
import json
from pathlib import Path

import numpy as np

from audit_actual_hardy_cauchy_network import HardyNetwork, whole_word
from audit_actual_crossing_green_ground_fusion import gate_clock, ground, green_matrix, shift_ac


def mirror_parameters(H):
    """Exact cyclotomic conjugation at the same finite-field embedding."""
    M = HardyNetwork(H.N, 1)
    N, p = H.N, H.p
    M.Q, M.q, M.x = pow(H.Q, -1, p), pow(H.q, -1, p), pow(H.x, -1, p)
    M.fac = [1]
    for k in range(1, N):
        M.fac.append(M.fac[-1]*(1-pow(M.Q, k, p)) % p)
    M.inv = [pow(f, -1, p) for f in M.fac]
    M.u = [pow(M.x, -k, p)*M.inv[k] % p for k in range(N)]
    M.v = [pow(-1, k, p)*pow(M.Q, k*(k-1)//2, p)*M.u[k] % p for k in range(N)]
    M.diag = [pow(-1, k, p)*pow(M.Q, k*(k-1)//2, p)*pow(M.x, -2*k, p) % p
              for k in range(N)]
    M.diag_inv = [pow(t, -1, p) for t in M.diag]
    M.kappa = pow(H.kappa, -1, p)
    return M


def swap_matrix(N):
    P = np.zeros((N*N, N*N), dtype=np.int64)
    for a, b in itertools.product(range(N), repeat=2):
        P[b*N+a, a*N+b] = 1
    return P


def negative_shift(H, matrix):
    N, p = H.N, H.p
    out = np.zeros_like(matrix)
    for a in range(N):
        for b in range(1, N):
            for c in range(1, N):
                for d in range(N):
                    out[c*N+d, a*N+b] = H.x*int(matrix[(c-1)*N+d, a*N+b-1]) % p
    return out


class SignedGreenNetwork(HardyNetwork):
    def __init__(self, N, M=1):
        assert M == 1
        super().__init__(N, M)
        mirror = mirror_parameters(self)
        P = swap_matrix(N)
        self.gplus = green_matrix(self)*self.kappa % self.p
        self.gminus = P@green_matrix(mirror)@P*mirror.kappa % self.p

    def crossing(self, states, letter):
        N, p = self.N, self.p
        i = abs(letter)-1
        matrix = self.gplus if letter > 0 else self.gminus
        answer = {}
        for state, weight in states.items():
            col = state[i]*N+state[i+1]
            for a, b in itertools.product(range(N), repeat=2):
                value = int(matrix[a*N+b, col])*weight % p
                if value:
                    key = state[:i]+(a, b)+state[i+2:]
                    answer[key] = (answer.get(key, 0)+value) % p
        return {s: v for s, v in answer.items() if v}


def exact_family(N):
    H = SignedGreenNetwork(N)
    M = mirror_parameters(H)
    p = H.p
    P = swap_matrix(N)
    assert np.array_equal(H.gplus, H.plus)
    assert np.array_equal(H.gminus, H.minus)
    # The balancing comparison diagonal is a TOTAL-degree root phase.
    for a, b in itertools.product(range(N), repeat=2):
        ratio = (pow(-1, a+b, p)
                 *pow(H.q, a*(a+1)+b*(b+1), p)
                 *pow(H.x, -a-b, p)*pow(H.q, 2*a*b, p)) % p
        assert ratio == pow(H.q, (a+b)*(a+b+2), p)
    for m in range(N+1):
        Km = P@gate_clock(M, m)@P % p
        Kn = P@gate_clock(M, m+1)@P % p
        Hm = P@ground(M, m)@P % p
        assert np.array_equal((Km-negative_shift(H, Kn)) % p, Hm)
        # Antiunitary transport of the shift itself.
        assert np.array_equal(P@shift_ac(M, gate_clock(M, m))@P % p,
                              negative_shift(H, Km))
        for a, b in itertools.product(range(N), repeat=2):
            column = Hm[:, a*N+b]
            if a+b >= N:
                assert not column.any()
            else:
                assert column[a+b] != 0 or any(column) == 0
                assert all(not value for j, value in enumerate(column) if j != a+b)
    Hzero = P@ground(M, 0)@P % p
    for a in range(N):
        # The first-input axis maps onto every first-output-ground row.
        assert Hzero[a, a*N] == pow(H.x, a, p)
    reconstructed = np.zeros((N*N, N*N), dtype=np.int64)
    for j in range(N):
        term = P@ground(M, j)@P % p
        for _ in range(j):
            term = negative_shift(H, term)
        reconstructed = (reconstructed+term) % p
    assert np.array_equal(reconstructed*pow(H.kappa, -1, p) % p, H.minus)
    nil = P@gate_clock(M, 0)@P % p
    for _ in range(N):
        nil = negative_shift(H, nil)
    assert not nil.any()
    return H, {'N': N, 'full_original_negative_equals_flip_conjugate': True,
               'original_kappa_phase_retained': True,
               'balanced_comparison_is_total_degree_phase': True,
               'negative_clock_Ward_checks': N+1,
               'negative_ground_first_output_support': True,
               'signed_Green_reconstruction_exact': True,
               'same_flat_partial_permutation_shift': True}


def singular_value_checks():
    rows = []
    for N in range(1, 21):
        S = np.diag(np.ones(max(0, N-1)), 1)
        inverse = np.eye(N)-S
        G = np.linalg.inv(inverse)
        actual = np.linalg.svd(G, compute_uv=False)[0]
        actinv = np.linalg.svd(inverse, compute_uv=False)[0]
        expected = 1/(2*np.sin(np.pi/(4*N+2)))
        expinv = 2*np.cos(np.pi/(2*N+1))
        assert abs(actual-expected) < 1e-11
        assert abs(actinv-expinv) < 1e-12
        assert actual <= N+1e-12 and actinv <= 2
        rows.append({'N': N, 'Green_norm': float(actual),
                     'inverse_norm': float(actinv), 'condition_number': float(actual*actinv)})
    return rows


def main():
    families = []
    words = []
    for N in range(2, 11):
        H, row = exact_family(N)
        families.append(row)
        if N <= 4:
            for heads, word in [(3, [1, -2, 1, -2]), (4, [2, -1, 3, 2]),
                                (3, [-1, 2, -1, 2])]:
                words.append(whole_word(H, heads, word))
    result = {'status': 'PASS', 'exact_signed_local_families': families,
              'whole_original_signed_pivotal_sources': words,
              'elementary_chain_singular_values': singular_value_checks(),
              'scope': ('Same balanced flat metric at complete color. Polynomial local '
                        'Green conditioning; no scalar source lower bound asserted.')}
    Path(__file__).with_name('signed_green_antiunitary_transport_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS nine complete original antiunitary/signed-Green families, nine whole '
          'signed original sources and twenty exact chain norm checks')


if __name__ == '__main__':
    main()
