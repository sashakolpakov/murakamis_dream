#!/usr/bin/env python3
"""Independent per-crossing Fourier frames, exact wires, and original sources.

Local full-Psi scalar identities are independently checked in the local
kernel audit. Here the full signed NETWORK, its original cut, and a
degree-lowering coupon test the exact operator/gluing assertion.
"""

import itertools
import json
from pathlib import Path

import numpy as np

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_balanced_fourier_crossing_kernel import fold_kernel
from audit_actual_two_cut_ports import partial


def tensor(matrices, p):
    answer = np.ones((1, 1), dtype=np.int64)
    for matrix in matrices:
        answer = np.kron(answer, matrix) % p
    return answer


def frame(N, p, Q, r):
    U = np.array([[pow(r, a, p)*pow(Q, k*a, p) % p
                   for a in range(N)] for k in range(N)], dtype=np.int64)
    inv = np.array([[pow(N, -1, p)*pow(r, -a, p)*pow(Q, -k*a, p) % p
                     for k in range(N)] for a in range(N)], dtype=np.int64)
    assert np.array_equal(U @ inv % p, np.eye(N, dtype=np.int64))
    return U, inv


def frames(H, radii):
    pairs = [frame(H.N, H.p, H.Q, r) for r in radii]
    return tensor([x[0] for x in pairs], H.p), tensor([x[1] for x in pairs], H.p)


def embed(local, position, heads, N, p):
    matrices = []
    i = 0
    while i < heads:
        if i == position:
            matrices.append(local)
            i += 2
        else:
            matrices.append(np.eye(N, dtype=np.int64))
            i += 1
    return tensor(matrices, p)


def direct_adapter(H, old, new):
    N, p, Q = H.N, H.p, H.Q
    ratio = new*pow(old, -1, p) % p
    C = pow(ratio, N, p)
    out = np.zeros((N, N), dtype=np.int64)
    for j, k in itertools.product(range(N), repeat=2):
        z = ratio*pow(Q, j-k, p) % p
        if z == 1:
            out[j, k] = 1
        else:
            out[j, k] = (1-C)*pow(N*(1-z) % p, -1, p) % p
    return out


def local_completion(H, sign, radii, position):
    N, p, Q, x = H.N, H.p, H.Q, H.x
    r0, r1 = radii[position:position+2]
    if sign > 0:
        while (pow(r1, -N, p)-pow(x*r0, -N, p)) % p == 0:
            r1 += 1
        radii[position+1] = r1
        local, _ = fold_kernel(N, p, Q, x, r0, r1)
        local = local*H.kappa % p
        expected = H.plus
        outpair = [x*r1 % p, x*r0 % p]
    else:
        # Mirror positive frames, keeping the two port swaps explicitly.
        xb = pow(x, -1, p)
        while (pow(r0, -N, p)-pow(xb*r1, -N, p)) % p == 0:
            r0 += 1
        radii[position] = r0
        local, _ = fold_kernel(N, p, pow(Q, -1, p), xb, r1, r0)
        permutation = np.array([b*N+a for a, b in itertools.product(range(N), repeat=2)])
        local = local[permutation][:, permutation]*pow(H.kappa, -1, p) % p
        expected = H.minus
        outpair = [xb*r1 % p, xb*r0 % p]
    assert np.array_equal(local % p, expected % p)
    return local, outpair


def word_case(N, heads, word, with_coupon=False):
    H = HardyNetwork(N, 1)
    p, size = H.p, N**heads
    assert size*(p-1)**2 < 2**62
    identity = np.eye(size, dtype=np.int64)
    direct = identity.copy()
    grid_word = identity.copy()
    omitted = identity.copy()
    initial_frame = None
    previous_out = None
    previous_out_inverse = None
    adapter_checks = 0
    for number, letter in enumerate(word):
        position, sign = abs(letter)-1, 1 if letter > 0 else -1
        incoming = [2+3*number+2*j for j in range(heads)]
        local, outpair = local_completion(H, sign, incoming, position)
        outgoing = incoming.copy()
        outgoing[position:position+2] = outpair
        Fin, Fini = frames(H, incoming)
        Fout, Fouti = frames(H, outgoing)
        physical = embed(local, position, heads, N, p)
        kernel = Fout @ physical % p @ Fini % p
        if initial_frame is None:
            initial_frame = Fin
            grid_word = kernel
            omitted = kernel
        else:
            adapter = tensor([direct_adapter(H, a, b)
                              for a, b in zip(previous_out, incoming)], p)
            assert np.array_equal(adapter, Fin @ previous_out_inverse % p)
            adapter_checks += heads
            grid_word = kernel @ adapter % p @ grid_word % p
            omitted = kernel @ omitted % p
        direct = physical @ direct % p
        if with_coupon and number == 1:
            # This lowers total degree by N, so a mere positive-degree
            # source-null completion would NOT suffice to justify it.
            coupon_local = np.eye(N*N, dtype=np.int64)
            coupon_local[0, N+(N-1)] = 1
            coupon = embed(coupon_local, 0, heads, N, p)
            grid_coupon = Fout @ coupon % p @ Fouti % p
            grid_word = grid_coupon @ grid_word % p
            omitted = grid_coupon @ omitted % p
            direct = coupon @ direct % p
        previous_out, previous_out_inverse = outgoing, Fouti
    decoded = previous_out_inverse @ grid_word % p @ initial_frame % p
    assert np.array_equal(decoded, direct)
    cut_direct = partial(direct, H.pivot, heads, N, p)
    cut_decoded = partial(decoded, H.pivot, heads, N, p)
    writhe = sum(1 if k > 0 else -1 for k in word)
    external = H.dimension*pow(H.twist, -writhe, p) % p
    assert np.array_equal(external*cut_direct % p, external*cut_decoded % p)
    wrong = previous_out_inverse @ omitted % p @ initial_frame % p
    return {'N': N, 'heads': heads, 'word': word,
            'independent_local_frames': True, 'exact_adapter_checks': adapter_checks,
            'full_operator_identical': True, 'original_complete_cut_and_external_line': True,
            'degree_lowering_coupon_retained': with_coupon,
            'omitting_adapters_changes_operator': bool(np.any((wrong-direct) % p))}


def complex_metric_checks():
    rows = []
    centers = [2+0j, 3j, -2+0j, -3j]
    for N in [2, 3, 5, 16, 32]:
        index = np.arange(N)
        Q = np.exp(2j*np.pi/N)
        U = Q**np.outer(index, index)/np.sqrt(N)
        for A, B in zip(centers, centers[1:]+centers[:1]):
            r, rp = np.exp(np.log(A)/N), np.exp(np.log(B)/N)
            F, G = U @ np.diag(r**index), U @ np.diag(rp**index)
            transition = G @ np.linalg.inv(F)
            assert np.linalg.norm(F, 2) <= max(1, abs(A))+1e-10
            assert np.linalg.norm(np.linalg.inv(F), 2) <= max(1, 1/abs(A))+1e-10
            assert np.linalg.norm(transition, 2) <= max(1, abs(B/A))+1e-10
            assert np.linalg.norm(np.linalg.inv(transition), 2) <= max(1, abs(A/B))+1e-10
            rows.append({'N': N, 'centers': [str(A), str(B)], 'uniform_frame_and_inverse_bounds': True})
    return rows


def main():
    rows = []
    for N in [2, 3, 4]:
        for coupon in [False, True]:
            rows.append(word_case(N, 3, [1, -2, 1, -2], coupon))
        if N <= 3:
            rows.append(word_case(N, 4, [2, -1, 3, 2]))
    assert any(row['omitting_adapters_changes_operator'] for row in rows)
    result = {'status': 'PASS', 'whole_original_networks': rows,
              'uniform_complex_metrics': complex_metric_checks(),
              'scope': 'Exact complete-color operator/source theorem; all adapters retained. '
                       'No scalar geometric noncancellation asserted.'}
    Path(__file__).with_name('regular_balanced_fermat_word_source_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print('PASS eight exact original signed Fourier networks, including degree-lowering '
          'coupons, independent frames/explicit adapters, and twenty uniform metric checks')


if __name__ == '__main__':
    main()
