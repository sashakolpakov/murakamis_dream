#!/usr/bin/env python3
"""Intrinsic ADO cut, its centralizer torsor, and meridian chart changes.

All finite-field inputs are the original nilpotent color, crossing,
pivot, and zero-framing factor. Fusion moments and every centralizer
matrix unit are checked independently of the crossing-word tests.
No geometric-period or volume assertion is made.
"""

from functools import cache
from itertools import product
import json
from pathlib import Path

import numpy as np

from audit_actual_peripheral_fusion import inverse_mod, module, tensor_module
from audit_braided_source_groupoid import projector_zero
from audit_casimir_braiding import evaluate, hermite_polynomials
from audit_cyclic_steinberg_lattice import determinant, rank
from audit_finite_sum_annihilator import field
from audit_kashaev_ado_pointing import color_matrices, reduced_period, WORDS
from audit_regular_holonomy_braiding import mm


def casimir(data, p, q):
    E, F, K = data
    rho = (q-pow(q, -1, p)) % p
    return (mm(p, F, E)*rho*rho + q*K
            + pow(q, -1, p)*inverse_mod(K, p)) % p


def modified_dimension(N, p, q, x):
    """Original full ADO factor, in highest-root coordinates x=-M/q."""
    return (-pow(q, N*(1-N)//2, p)
            * (q*x-pow(q*x, -1, p))
            * pow((pow(x, N, p)-pow(x, -N, p)) % p, -1, p)) % p


@cache
def fusion_frame(N, p, q, x, y):
    Q = q*q % p
    left, right = module(N, p, q, x), module(N, p, q, y)
    data = tensor_module(left, right, p)
    E, F, K = data
    columns, colors = [], []
    for j in range(N):
        h = np.zeros(N*N, dtype=np.int64)
        h[j] = coefficient = 1
        for a in range(j):
            denominator = int(left[0][a, a+1])*y*pow(Q, -(j-a-1), p) % p
            coefficient = (-coefficient*int(right[0][j-a-1, j-a])
                           * pow(denominator, -1, p)) % p
            h[(a+1)*N+j-a-1] = coefficient
        assert not np.any(mm(p, E, h[:, None]))
        z = x*y*pow(Q, -j, p) % p
        colors.append(z)
        for r in range(N):
            columns.append(h.copy())
            h = mm(p, F, h[:, None])[:, 0]
        assert not np.any(h)
    H = np.column_stack(columns)
    Hi = inverse_mod(H, p)
    assert np.array_equal(mm(p, H, Hi), np.eye(N*N, dtype=np.int64))
    for index, operator in enumerate(data):
        diagonal = np.zeros_like(operator)
        for j, z in enumerate(colors):
            diagonal[j*N:(j+1)*N, j*N:(j+1)*N] = module(N, p, q, z)[index]
        assert np.array_equal(mm(p, operator, H), mm(p, H, diagonal))
    return H, Hi, tuple(colors)


def iterated_frame(N, p, q, colors):
    H = np.eye(N, dtype=np.int64)
    paths = [(colors[0], ())]
    for y in colors[1:]:
        size = len(H)
        new = np.zeros((size*N, size*N), dtype=np.int64)
        next_paths = []
        for a, (x, path) in enumerate(paths):
            local, _, zs = fusion_frame(N, p, q, x, y)
            leaves = np.kron(H[:, a*N:(a+1)*N], np.eye(N, dtype=np.int64))
            new[:, a*N*N:(a+1)*N*N] = mm(p, leaves, local)
            next_paths.extend((z, path+(j,)) for j, z in enumerate(zs))
        H, paths = new, next_paths
    return H, inverse_mod(H, p), paths


def right_close(A, pivot, p):
    N = len(pivot)
    return np.einsum('abcb,b->ac', A.reshape((N,)*4), np.diag(pivot)) % p


def cut(A, colors, N, p, q):
    b = len(colors)
    weights = np.array([1], dtype=np.int64)
    for x in colors[1:]:
        g = np.diag(color_matrices(N, p, q, x)[2])
        weights = np.kron(weights, g) % p
    rest = N**(b-1)
    closed = np.einsum('arbr,r->ab', A.reshape(N, rest, N, rest), weights) % p
    assert np.array_equal(closed, int(closed[0, 0])*np.eye(N, dtype=np.int64) % p)
    return int(closed[0, 0])


def moment_case(N, color_power):
    p, generator, q = field(N)
    x, y = generator, pow(generator, color_power, p)
    O = casimir(tensor_module(module(N, p, q, x), module(N, p, q, y), p), p, q)
    pivot = color_matrices(N, p, q, y)[2]
    # N propagated columns suffice for all diagonal closed moments.
    columns = np.zeros((N*N, N), dtype=np.int64)
    for b in range(N):
        columns[b, b] = 1
    moments = []
    for m in range(N):
        moments.append(sum(int(pivot[b, b])*int(columns[b, b])
                           for b in range(N)) % p)
        columns = mm(p, O, columns)
    constant = (-N*(pow(x, N, p)-pow(x, -N, p))
                * pow((q*x-pow(q*x, -1, p)) % p, -1, p)) % p
    assert moments == [0]*(N-1)+[constant]
    H, Hi, zs = fusion_frame(N, p, q, x, y)
    left_pivot = inverse_mod(color_matrices(N, p, q, x)[2], p)
    I = np.eye(N, dtype=np.int64)
    dx, dy = modified_dimension(N, p, q, x), modified_dimension(N, p, q, y)
    weights = []
    for j, z in enumerate(zs):
        P = mm(p, H[:, j*N:(j+1)*N], Hi[j*N:(j+1)*N, :])
        right = right_close(P, pivot, p)
        left = np.einsum('abad->bd', mm(p, np.kron(left_pivot, I), P).reshape((N,)*4)) % p
        dz = modified_dimension(N, p, q, z)
        wr, wl = dz*pow(dx, -1, p) % p, dz*pow(dy, -1, p) % p
        assert np.array_equal(right, wr*I % p)
        assert np.array_equal(left, wl*I % p)
        weights.append({'label':j, 'right_cut':wr, 'left_cut':wl})
    return {'level':N, 'prime':p, 'second_color_power':color_power,
            'all_lower_Casimir_moments_zero':True,
            'top_moment_with_full_N_and_sign':constant,
            'all_two_color_projector_weights':weights}


def centralizer_case(N, b, heterogeneous=False):
    p, generator, q = field(N)
    colors = tuple(pow(generator, j+1 if heterogeneous else 1, p) for j in range(b))
    H, Hi, paths = iterated_frame(N, p, q, colors)
    # The density of the selected cut, not a replacement trace on W.
    density = np.zeros(N, dtype=np.int64)
    density[0] = 1
    for x in colors[1:]:
        density = np.kron(density, np.diag(color_matrices(N, p, q, x)[2])) % p
    mask = np.flatnonzero(density)
    in_frame = mm(p, Hi[:, mask]*density[mask][None, :] % p, H[mask, :])
    s = len(paths)
    path_density = np.einsum('arbr->ab', in_frame.reshape(s, N, s, N)) % p
    d0 = modified_dimension(N, p, q, colors[0])
    matrix_units = 0
    for a, (za, _) in enumerate(paths):
        for c, (zc, _) in enumerate(paths):
            if za != zc:
                continue
            expected = (modified_dimension(N, p, q, za)*pow(d0, -1, p) % p
                        if a == c else 0)
            assert int(path_density[c, a]) == expected
            matrix_units += 1
    assert len(set(z for z, _ in paths)) == N
    assert matrix_units == N**(2*b-3)
    return {'level':N, 'strands':b, 'prime':p,
            'heterogeneous_colors':heterogeneous,
            'every_centralizer_matrix_unit_checked':matrix_units,
            'selected_cut_equals_weighted_multiplicity_trace':True}


def complete_residue_case(N):
    p, _, q = field(N)
    x = pow(q, N-1, p)
    O = casimir(tensor_module(module(N, p, q, x), module(N, p, q, x), p), p, q)
    pivot = color_matrices(N, p, q, x)[2]
    columns = np.zeros((N*N, N), dtype=np.int64)
    for b in range(N):
        columns[b, b] = 1
    moments = []
    for m in range(2*N-1):
        moments.append(sum(int(pivot[b, b])*int(columns[b, b])
                           for b in range(N)) % p)
        columns = mm(p, O, columns)
    s0 = pow(-1, N+1, p)*N*N % p
    assert moments[:N] == [0]*(N-1)+[s0]
    gram = np.array([[moments[a+b] for b in range(N)] for a in range(N)], dtype=np.int64)
    gram_det = determinant(gram, p)
    expected_det = pow(-1, N*(N-1)//2, p)*pow(s0, N, p) % p
    assert gram_det == expected_det and gram_det
    eta = pow(-1, N+1, p)*pow(q, N*(1-N)//2, p) % p
    d0 = eta*pow(N, -1, p) % p
    residue_scale = N*pow(q, N*(1-N)//2, p) % p
    assert d0*s0 % p == residue_scale
    for crossing, sign in ((color_matrices(N, p, q, x)[0], 1),
                           (color_matrices(N, p, q, x)[1], -1)):
        assert np.array_equal(right_close(crossing, pivot, p),
                              pow(x, (1-N)*sign, p)*np.eye(N, dtype=np.int64) % p)
    return {'level':N, 'prime':p, 'complete_pivotal_top_moment':s0,
            'Casimir_trace_Gram_determinant':gram_det,
            'confluent_Casimir_pairing_is_perfect':True,
            'retained_ADO_complete_dimension':d0,
            'full_modified_residue_scale':residue_scale,
            'both_actual_stabilization_partial_closures_exact':True}


def elementary_modification_case(N):
    p, _, q = field(N)
    I = np.eye(N*N, dtype=np.int64)
    eye = np.eye(N, dtype=np.int64)
    x = -1 % p
    data = tensor_module(module(N, p, q, x), module(N, p, q, x), p)
    O = casimir(data, p, q)
    actual = color_matrices(N, p, q, x)
    r, _, _ = hermite_polynomials(N, p, q)
    # The displayed expression is regular in the target matrix lattice.
    E = (actual[0]+evaluate(r, O, p))*pow(2, -1, p) % p
    assert np.array_equal(mm(p, E, E), E)
    assert rank(E, p) == N
    for operator in data:
        assert np.array_equal(mm(p, E, operator), mm(p, operator, E))
    closed = right_close(E, actual[2], p)
    scalar = pow(-1, N+1, p)*pow(2, -1, p) % p
    assert np.array_equal(closed, scalar*eye % p)
    c0 = (q+pow(q, -1, p)) % p
    J = mm(p, (O-c0*I) % p, projector_zero(N, p, q, O))
    assert not np.any(J)
    # Its vanishing on the target contrasts with the retained nonzero
    # nilpotent on the original Kashaev module, not with a changed state.
    source_x = pow(q, N-1, p)
    source_data = tensor_module(module(N, p, q, source_x), module(N, p, q, source_x), p)
    source_O = casimir(source_data, p, q)
    source_J = mm(p, (source_O-c0*I) % p, projector_zero(N, p, q, source_O))
    assert rank(source_J, p) == 1
    rho = (q-pow(q, -1, p)) % p
    source_pivot = color_matrices(N, p, q, source_x)[2]
    pole_scalar = pow(-1, N, p)*rho*pow(4, -1, p) % p
    assert np.array_equal(right_close(source_J*pow(4*rho, -1, p) % p,
                                     source_pivot, p), pole_scalar*eye % p)
    return {'level':N, 'prime':p,
            'regular_shifted_color_projector_rank':N,
            'shifted_complete_projector_cut':scalar,
            'original_projector_cut_pole_coefficient':pole_scalar,
            'source_nilpotent_rank':1, 'shifted_nilpotent_rank':0,
            'all_E_F_K_intertwinings_and_idempotence_exact':True}


def embed(A, i, b, N):
    return np.kron(np.eye(N**i, dtype=np.int64),
                   np.kron(A, np.eye(N**(b-i-2), dtype=np.int64)))


def meridian_pair(N, p, q, M):
    x = -M*pow(q, -1, p) % p
    xs = q*x % p
    H, Hi, _ = fusion_frame(N, p, q, x, x)
    Hs, _, _ = fusion_frame(N, p, q, xs, xs)
    P = np.zeros((N*N, N*N), dtype=np.int64)
    for j, r in product(range(N), repeat=2):
        P[((j+1) % N)*N+r, j*N+r] = 1
    last = mm(p, H[:, -N:], Hi[-N:, :])
    return mm(p, Hs, P, Hi), last


def word_matrix(word, positives, negatives, p):
    A = np.eye(len(positives[0]), dtype=np.int64)
    for i, sign in word:
        A = mm(p, A, positives[i] if sign > 0 else negatives[i])
    return A


def meridian_case(N):
    p, generator, q = field(N)
    M = generator
    x = -M*pow(q, -1, p) % p
    xs = q*x % p
    b, size = 4, N**4
    I = np.eye(size, dtype=np.int64)
    actual, shifted = color_matrices(N, p, q, x), color_matrices(N, p, q, xs)
    B = [embed(actual[0], i, b, N) % p for i in range(3)]
    Bs = [embed(shifted[0], i, b, N) % p for i in range(3)]
    Bi = [embed(actual[1], i, b, N) % p for i in range(3)]
    Bsi = [embed(shifted[1], i, b, N) % p for i in range(3)]
    pair, last = meridian_pair(N, p, q, M)
    pair_cycle = np.eye(N*N, dtype=np.int64)
    for j in range(2*N):
        arrow, _ = meridian_pair(N, p, q, M*pow(q, j, p) % p)
        pair_cycle = mm(p, arrow, pair_cycle)
    assert np.array_equal(pair_cycle, np.eye(N*N, dtype=np.int64))
    G = np.kron(pair, pair) % p
    Gi = inverse_mod(G, p)
    U = pow(M, 2*N, p)
    a, c = -pow(M, -2, p) % p, (1+pow(U, -1, p)) % p
    projectors = [embed(last, i, b, N) % p for i in range(3)]
    local = [(a*B[i]+c*projectors[i]) % p for i in range(3)]
    local_inverse = [(pow(a, -1, p)*mm(p, Bi[i], (I-projectors[i]) % p)
                      + projectors[i]) % p for i in range(3)]
    for L, Li in zip(local, local_inverse):
        assert np.array_equal(mm(p, L, Li), I)
    for i in (0, 2):
        assert np.array_equal(mm(p, Gi, Bs[i], G), local[i])
    middle_defect = (mm(p, Gi, Bs[1], G)-local[1]) % p
    defect_rank = rank(middle_defect, p)
    assert defect_rank
    delta, deltas = mm(p, *B), mm(p, *Bs)
    delta_inv = inverse_mod(delta, p)
    charts, transitions = [], []
    Cs = I.copy()
    Ci = I.copy()
    total = module(N, p, q, x)
    totals = module(N, p, q, xs)
    for _ in range(b-1):
        total = tensor_module(total, module(N, p, q, x), p)
        totals = tensor_module(totals, module(N, p, q, xs), p)
    for i in range(3):
        chart = mm(p, Cs, G, Ci)
        chart_inv = inverse_mod(chart, p)
        D = mm(p, Gi, chart)
        Di = inverse_mod(D, p)
        assert np.array_equal(mm(p, chart_inv, Bs[i], chart), local[i])
        assert np.array_equal(mm(p, Gi, Bs[i], G), mm(p, D, local[i], Di))
        for old, new in zip(total, totals):
            assert np.array_equal(mm(p, chart, old), mm(p, new, chart))
            assert np.array_equal(mm(p, D, old), mm(p, old, D))
        charts.append(chart)
        transitions.append((D, Di))
        Cs, Ci = mm(p, Cs, deltas), mm(p, delta_inv, Ci)
    d, ds = modified_dimension(N, p, q, x), modified_dimension(N, p, q, xs)
    f = lambda z: (z-pow(z, -1, p)) % p
    assert ds*pow(d, -1, p) % p == -f(q*M % p)*pow(f(M), -1, p) % p
    records = []
    for word3 in WORDS:
        word = list(word3)+[(2, 1)]
        A = word_matrix(word, Bs, Bsi, p)
        pulled = mm(p, Gi, A, G)
        assembled = I.copy()
        for i, sign in word:
            D, Di = transitions[i]
            L = local[i] if sign > 0 else local_inverse[i]
            assembled = mm(p, assembled, D, L, Di)
        assert np.array_equal(pulled, assembled)
        selected = cut(A, (xs,)*b, N, p, q)
        transported = cut(pulled, (x,)*b, N, p, q)
        assert ds*selected % p == d*transported % p
        # Every chart gives the same full cut, not the same pulled matrix.
        for chart in charts:
            candidate = mm(p, inverse_mod(chart, p), A, chart)
            assert d*cut(candidate, (x,)*b, N, p, q) % p == ds*selected % p
        writhe = sum(sign for _, sign in word)
        normalized = selected*pow(shifted[3], -writhe, p) % p
        original_three = reduced_period(N, p, *shifted, word3)
        assert normalized == original_three
        records.append({'word':word, 'shifted_zero_framed_period':normalized,
                        'all_charts_preserve_full_modified_cut':True,
                        'one_actual_stabilization_preserves_period':True})
    ideal = color_matrices(N, p, q, pow(q, N-1, p))
    ideal_B = [embed(ideal[0], i, b, N) % p for i in range(3)]
    ideal_Bi = [embed(ideal[1], i, b, N) % p for i in range(3)]
    for word3 in WORDS:
        word = list(word3)+[(2, 1)]
        A = word_matrix(word, ideal_B, ideal_Bi, p)
        value = cut(A, (pow(q, N-1, p),)*b, N, p, q)
        value = value*pow(ideal[3], -sum(sign for _, sign in word), p) % p
        assert value == reduced_period(N, p, *ideal, word3)
    return {'level':N, 'prime':p, 'strands':b,
            'specified_two_N_step_meridian_cycle_is_identity':True,
            'pairing_alone_fails_at_middle_generator_rank':defect_rank,
            'braid_conjugated_charts_intertwine_all_total_E_F_K':True,
            'transitions_belong_to_actual_centralizer':True,
            'positive_and_negative_local_source_factors_retained':True,
            'full_modified_dimension_shift_ratio':ds*pow(d, -1, p) % p,
            'whole_word_records':records,
            'actual_ideal_fiber_stabilization_checks':len(WORDS)}


def main():
    result = {
        'scope':'Exact diagnostics of a uniform cut/centralizer theorem; no geometric period or volume theorem.',
        'moments_and_two_color_weights':[moment_case(N, power)
            for N in (2, 3, 4, 5, 6, 9, 12, 15) for power in (1, 2)],
        'all_centralizer_matrix_units':[centralizer_case(N, b, different)
            for N, b in ((2, 3), (3, 3), (4, 3), (5, 3),
                         (2, 4), (3, 4), (4, 4), (2, 5), (3, 5), (2, 6))
            for different in (False, True)],
        'complete_fiber_residue_pairings':[complete_residue_case(N)
            for N in (2, 3, 4, 5, 6, 9, 12, 15)],
        'actual_meridian_elementary_modifications':[elementary_modification_case(N)
            for N in (2, 3, 4, 5, 6, 9, 12, 15)],
        'four_strand_meridian_atlas':[meridian_case(N) for N in (2, 3, 4)]}
    target = Path(__file__).with_name('intrinsic_cut_transport_results.json')
    target.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'result':str(target),
                      'two_color_cases':len(result['moments_and_two_color_weights']),
                      'all_matrix_unit_cases':len(result['all_centralizer_matrix_units']),
                      'matrix_units_checked':sum(r['every_centralizer_matrix_unit_checked']
                          for r in result['all_centralizer_matrix_units']),
                      'perfect_complete_residue_pairings':len(result['complete_fiber_residue_pairings']),
                      'regular_shifted_color_source_projectors':len(result['actual_meridian_elementary_modifications']),
                      'middle_defect_ranks':[r['pairing_alone_fails_at_middle_generator_rank']
                          for r in result['four_strand_meridian_atlas']]}), flush=True)


if __name__ == '__main__':
    main()
