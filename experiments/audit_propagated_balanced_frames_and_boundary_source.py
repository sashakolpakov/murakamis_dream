#!/usr/bin/env python3
"""Original arbitrary-width word in regular propagated balanced frames."""

import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_regular_balanced_fermat_word_source import frames, embed, local_completion
from audit_actual_two_cut_ports import partial


def field_word(n, width, word):
    H = HardyNetwork(n, 1)
    p, Q, x = H.p, H.Q, H.x
    s = pow(x, n, p)
    centers, roots = [], []
    for i in range(width):
        for r in range(1, p):
            c = pow(s, i, p)*pow(r, n, p) % p
            if c not in centers:
                centers.append(c)
                roots.append(r)
                break
        else:
            raise AssertionError('Need more distinct finite-field power centers')
    initial_roots = roots.copy()
    F0, F0i = frames(H, roots)
    current_frame, current_inverse = F0, F0i
    permutation = list(range(width))
    size = n**width
    direct = np.eye(size, dtype=np.int64)
    grid = direct.copy()
    regularity = []
    for letter in word:
        position, sign = abs(letter)-1, 1 if letter > 0 else -1
        old_roots = roots.copy()
        for i in range(width):
            assert pow(roots[i], n, p) == pow(s, i, p)*centers[permutation[i]] % p
        A, B = pow(roots[position], n, p), pow(roots[position+1], n, p)
        assert (B-s*A) % p
        local, outputs = local_completion(H, sign, roots, position)
        assert roots == old_roots, 'Regular propagation needs no per-gate root repair'
        roots[position:position+2] = outputs
        permutation[position], permutation[position+1] = permutation[position+1], permutation[position]
        next_frame, next_inverse = frames(H, roots)
        physical = embed(local, position, width, n, p)
        block = next_frame @ physical % p @ current_inverse % p
        # No adapter is inserted between this block and the preceding one.
        grid = block @ grid % p
        direct = physical @ direct % p
        current_frame, current_inverse = next_frame, next_inverse
        regularity.append((B-s*A) % p)
    decoded = current_inverse @ grid % p @ F0 % p
    assert np.array_equal(decoded, direct)
    actual = np.eye(size, dtype=np.int64)
    for letter in word:
        local = H.plus if letter > 0 else H.minus
        actual = embed(local, abs(letter)-1, width, n, p) @ actual % p
    assert np.array_equal(actual, decoded)
    assert np.array_equal(partial(actual, H.pivot, width, n, p),
                          partial(decoded, H.pivot, width, n, p))
    for i in range(width):
        ratio = pow(initial_roots[i]*pow(roots[i], -1, p) % p, n, p)
        assert ratio == centers[i]*pow(centers[permutation[i]], -1, p) % p
    return {'N': n, 'width': width, 'word': word,
            'all_local_Fermat_charts_regular': True,
            'interior_adapters': 0, 'maximum_boundary_adapters': width,
            'exact_original_operator_and_pivotal_cut': True,
            'central_boundary_ratios_follow_final_permutation': True}


def complex_metrics():
    rows = []
    for n in (2, 3, 8, 32):
        for width in (3, 5):
            q = np.exp(1j*np.pi/n)
            Q, x = q*q, -1/q
            s = (-1)**(n+1)
            centers = np.arange(2, width+2, dtype=float)
            roots = [np.exp(np.log(complex(s**i*c))/n) for i, c in enumerate(centers)]
            initial = roots.copy()
            permutation = list(range(width))
            word = [1, -2, 1, -2] if width == 3 else [1, -2, 3, -4, 2, -1, 4, -3]*3
            for letter in word:
                i, sign = abs(letter)-1, 1 if letter > 0 else -1
                assert abs(roots[i+1]**n-s*roots[i]**n) > 0.9
                factor = x if sign > 0 else 1/x
                roots[i:i+2] = [factor*roots[i+1], factor*roots[i]]
                permutation[i], permutation[i+1] = permutation[i+1], permutation[i]
            U = Q**np.outer(np.arange(n), np.arange(n))/np.sqrt(n)
            for i in range(width):
                F0 = U @ np.diag(initial[i]**np.arange(n))
                Fm = U @ np.diag(roots[i]**np.arange(n))
                adapter = F0 @ np.linalg.inv(Fm)
                ratio = centers[i]/centers[permutation[i]]
                assert np.linalg.norm(adapter, 2) <= max(1, ratio)+1e-9
                assert np.linalg.norm(np.linalg.inv(adapter), 2) <= max(1, 1/ratio)+1e-9
                assert np.linalg.norm(Fm, 2) <= width+1+1e-9
            rows.append({'N': n, 'width': width, 'crossings': len(word),
                         'propagated_regular_chart_and_uniform_boundary_norms': True})
    return rows


def main():
    words = []
    for n in (2, 3, 4, 5):
        words.append(field_word(n, 3, [1, -2, 1, -2]))
        words.append(field_word(n, 3, [1, 1, -2, -1, 2, -2, 1, 2]))
        if n <= 3:
            words.append(field_word(n, 4, [2, -1, 3, 2, -3, 1, -2]))
    I = sp.I
    R = sp.Matrix([[1, 0, 0, 0], [0, 0, -I, 0], [0, -I, 2, 0], [0, 0, 0, 1]])
    one, pivot = sp.eye(2), sp.diag(-I, I)
    R1, R2 = sp.kronecker_product(R, one), sp.kronecker_product(one, R)
    W = R2.inv()*R1*R2.inv()*R1
    source = sp.kronecker_product(sp.ones(2)/2, pivot, pivot)
    t = sp.symbols('t')
    gauge = sp.diag(1, t)
    moments = []
    for j in range(3):
        insertion = sp.kronecker_product(*[gauge if k == j else one for k in range(3)])
        moments.append(sp.expand(sp.trace(source*W*insertion)))
    assert moments == [5*(1+t)/2, (11-t)/2, (-7+17*t)/2]
    result = {'exact_original_words': words, 'complex_metrics': complex_metrics(),
              'exact_connected_knot_radius_sliding_obstruction': [str(x) for x in moments],
              'scope': 'Exact regular open-braid bulk and boundary source; no geometric coefficient assertion'}
    path = Path(__file__).with_name('propagated_balanced_frames_and_boundary_source_results.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(f'PASS {len(words)} exact signed original words with no interior adapters, '
          f"{len(result['complex_metrics'])} propagated metric/boundary families")


if __name__ == '__main__':
    main()
