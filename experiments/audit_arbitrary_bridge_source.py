#!/usr/bin/env python3
"""Check the arbitrary-bridge sourced contraction, not a volume theorem.

The proof for arbitrary bridge count and word length is in
notes/arbitrary_bridge_source_reduction.md. Tests include exact universal
block identities and genuine Hurwitz derivatives at finite-field cap
solutions with arbitrarily many bridges. The test words are not labelled
as knot examples or used to infer a theorem by sampling.
"""

import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_cyclic_steinberg_lattice import determinant, rank


def equal(a, b):
    if isinstance(a, sp.MatrixBase):
        assert (a-b).applyfunc(sp.cancel) == sp.zeros(*a.shape)
    else:
        assert sp.cancel(a-b) == 0


def symbolic_local_identities():
    a, b, c, d, tau = sp.symbols('a b c d tau', nonzero=True)
    G = lambda k, e: sp.Matrix([[k, e], [(tau*k-k*k-1)/e, tau-k]])
    A, B = G(a, b), G(c, d)
    Ai = A.adjugate()
    C = (Ai*B*A).applyfunc(sp.cancel)
    variables = (a, b, c, d)
    out = sp.Matrix([C[0, 0], C[0, 1], a, b])
    J = out.jacobian(variables)
    # Expand along the two identity rows before forming a determinant.
    # This avoids a large, irrelevant symbolic 4x4 Bareiss expansion.
    detJ = sp.cancel(J[0, 2]*J[1, 3]-J[0, 3]*J[1, 2])
    equal(detJ/C[0, 1]/b, 1/b/d)
    equal(Ai[0, 0].diff(a)*Ai[0, 1].diff(b)/Ai[0, 1], -1/b)

    # q dj=0, q r=I in coordinates on the even inverse class.
    derivatives = [A.diff(a), A.diff(b)]
    dj = sp.zeros(4, 2)
    q = sp.zeros(2, 4)
    for j, v in enumerate(derivatives):
        vi = -Ai*v*Ai
        dj[:2, j] = sp.Matrix([v[0, 0], v[0, 1]])
        dj[2:, j] = sp.Matrix([vi[0, 0], vi[0, 1]])
    inv_variables = (Ai[0, 0], Ai[0, 1])
    for j in range(4):
        vo = derivatives[j] if j < 2 else sp.zeros(2)
        ve = G(a, b).diff((a, b)[j-2]) if j >= 2 else sp.zeros(2)
        if j >= 2:
            ve = ve.subs({a: inv_variables[0], b: inv_variables[1]}, simultaneous=True)
        normal_tangent = ve+Ai*vo*Ai
        q[:, j] = sp.Matrix([normal_tangent[0, 0], normal_tangent[0, 1]])
    r = sp.zeros(4, 2)
    r[2:, :] = sp.eye(2)
    equal(q*dj, sp.zeros(2))
    equal(q*r, sp.eye(2))
    equal(dj.row_join(r).det(), 1)

    return {
        'generic_trace_symbolic_Hurwitz_residue_volume_preserved': True,
        'inverse_pulls_residue_form_to_negative': True,
        'cap_exact_sequence_and_volume_splitting': True,
    }


def symbolic_source_contraction():
    entries = sp.symbols('j0:8')
    J1 = sp.Matrix(2, 2, entries[:4])
    J2 = sp.Matrix(2, 2, entries[4:])
    q0, q1 = sp.symbols('q0 q1')
    q = sp.Matrix([[q0, q1]])
    injection = sp.Matrix([1, sp.Symbol('i')])
    D = q*J2*J1*injection

    # Domain (v,u1,u2), target (e1,e2,n). New domain is (v,e1,e2).
    middle = sp.zeros(5)
    middle[:2, 0] = -J1*injection
    middle[:2, 1:3] = sp.eye(2)
    middle[2:4, 1:3] = -J2
    middle[2:4, 3:5] = sp.eye(2)
    middle[4, 3:5] = q
    domain = sp.eye(5)
    domain[1:3, 0] = J1*injection
    domain[3:5, 0] = J2*J1*injection
    domain[3:5, 1:3] = J2
    target = sp.eye(5)
    target[4, :2] = -q*J2
    target[4, 2:4] = -q
    want = sp.zeros(5)
    want[:2, 1:3] = sp.eye(2)
    want[2:4, 3:5] = sp.eye(2)
    want[4, 0] = D[0]
    equal(target*middle*domain, want)
    equal(domain.det(), 1)
    equal(target.det(), 1)
    b = sp.Matrix(sp.symbols('b0:4'))
    c = sp.Symbol('c')
    transformed = target*b.col_join(sp.Matrix([c]))
    equal(transformed[4], c-(q*J2*b[:2, :])[0]-(q*b[2:, :])[0])

    ell = sp.Matrix(1, 5, sp.symbols('l0:5'))
    value = (ell*domain*sp.Matrix([sp.Symbol('v'), *b]))[0]
    coefficient = ell[0]+(ell[:, 1:3]*J1*injection)[0]+(ell[:, 3:5]*J2*J1*injection)[0]
    constant = (ell[:, 1:3]*b[:2, :]+ell[:, 3:5]*(J2*b[:2, :]+b[2:, :]))[0]
    equal(value, coefficient*sp.Symbol('v')+constant)
    return {'universal_two_stage_chain_map': True, 'both_change_determinants_one': True,
            'inhomogeneous_endpoint_source_and_dual_affine_constant': True}


def inv(A, p):
    assert int(A[0, 0]*A[1, 1]-A[0, 1]*A[1, 0]) % p == 1
    return np.array([[A[1, 1], -A[0, 1]], [-A[1, 0], A[0, 0]]], dtype=np.int64) % p


def chart(A, p):
    tau = int(np.trace(A)) % p
    a, b, c = (int(A[0, 0]), int(A[0, 1]), int(A[1, 0]))
    if b:
        bi = pow(b, -1, p)
        basis = [np.array([[1, 0], [(tau-2*a)*bi, -1]], dtype=np.int64) % p,
                 np.array([[0, 1], [-c*bi, 0]], dtype=np.int64) % p]
        return basis, (0, 1), bi
    assert c
    ci = pow(c, -1, p)
    basis = [np.array([[1, (tau-2*a)*ci], [0, -1]], dtype=np.int64) % p,
             np.array([[0, -b*ci], [1, 0]], dtype=np.int64) % p]
    return basis, (1, 0), -ci % p


def encode(A, v, p):
    _, (i, j), _ = chart(A, p)
    return np.array([int(v[0, 0]), int(v[i, j])], dtype=np.int64) % p


def cap_data(B, p):
    k, n = len(B), 2*len(B)
    H = [v for A in B for v in (A, inv(A, p))]
    injection = np.zeros((2*n, 2*k), dtype=np.int64)
    q = np.zeros((2*k, 2*n), dtype=np.int64)
    M = np.zeros((3, 2*k), dtype=np.int64)
    a = np.zeros((2*k, 3), dtype=np.int64)
    lie = [np.diag([1, -1]), np.array([[0, 1], [0, 0]]), np.array([[0, 0], [1, 0]])]
    for j, A in enumerate(B):
        Ai = inv(A, p)
        for r, v in enumerate(chart(A, p)[0]):
            injection[4*j:4*j+2, 2*j+r] = encode(A, v, p)
            injection[4*j+2:4*j+4, 2*j+r] = encode(Ai, -Ai@v@Ai % p, p)
            q[2*j:2*j+2, 4*j+r] = encode(Ai, Ai@v@Ai % p, p)
        q[2*j:2*j+2, 4*j+2:4*j+4] = np.eye(2, dtype=np.int64)
        for r, v in enumerate(chart(Ai, p)[0]):
            normal = v@A % p
            M[:, 2*j+r] = [int(normal[0, 0]), int(normal[0, 1]), int(normal[1, 0])]
        for r, xi in enumerate(lie):
            a[2*j:2*j+2, r] = encode(A, (xi@A-A@xi) % p, p)
    assert not np.any(q@injection % p)
    return H, injection, q, M, a


def moment(H, p):
    d = 2*len(H)
    variations = np.zeros((d, 2, 2), dtype=np.int64)
    product = np.eye(2, dtype=np.int64)
    for j, A in enumerate(H):
        old = variations.copy()
        variations = np.array([A@v % p for v in old])
        for r, v in enumerate(chart(A, p)[0]):
            variations[2*j+r] = (variations[2*j+r]+v@product) % p
        product = A@product % p
    assert np.array_equal(product, np.eye(2, dtype=np.int64))
    return np.array([[v[i, j] for v in variations] for i, j in ((0, 0), (0, 1), (1, 0))], dtype=np.int64)


def crossing(H, position, sign, p):
    A, B = H[position:position+2]
    Ai, Bi = inv(A, p), inv(B, p)
    out = (Ai@B@A % p, A) if sign > 0 else (B, B@A@Bi % p)
    J = np.eye(2*len(H), dtype=np.int64)
    J[2*position:2*position+4, 2*position:2*position+4] = 0
    for j in range(4):
        v = chart(A, p)[0][j] if j < 2 else np.zeros((2, 2), dtype=np.int64)
        w = chart(B, p)[0][j-2] if j >= 2 else np.zeros((2, 2), dtype=np.int64)
        if sign > 0:
            dv = (-Ai@v@out[0]+Ai@w@A+Ai@B@v) % p
            dw = v
        else:
            dv = w
            dw = (w@A@Bi+B@v@Bi-out[1]@w@Bi) % p
        J[2*position:2*position+2, 2*position+j] = encode(out[0], dv, p)
        J[2*position+2:2*position+4, 2*position+j] = encode(out[1], dw, p)
    new = [v.copy() for v in H]
    new[position:position+2] = out
    old_volume = chart(A, p)[2]*chart(B, p)[2] % p
    new_volume = chart(out[0], p)[2]*chart(out[1], p)[2] % p
    local = J[2*position:2*position+4, 2*position:2*position+4]
    assert determinant(local, p)*new_volume % p == old_volume
    assert np.array_equal(moment(new, p)@J % p, moment(H, p))
    return new, J


def central_order(A, p):
    P = np.eye(2, dtype=np.int64)
    for r in range(1, 2*p+3):
        P = P@A % p
        if not P[0, 1] and not P[1, 0] and P[0, 0] == P[1, 1]:
            return r
    raise AssertionError('SL2 central-order bound')


def actual_plat_case(k, p):
    base = np.array([[1, 1], [0, 1]], dtype=np.int64)
    B = []
    for i in range(k):
        u, v = i+1, 2*i+1
        g = np.array([[1, u], [v, 1+u*v]], dtype=np.int64) % p
        B.append(g@base@inv(g, p) % p)
    H, injection, q, M, a = cap_data(B, p)
    initial = [v.copy() for v in H]
    assert rank(a, p) == rank(M, p) == 3
    assert np.array_equal(M@q % p, moment(H, p))
    assert not np.any(moment(H, p)@injection % p)
    rng = np.random.default_rng(1701+101*k+p)
    d = 4*k
    total = np.eye(d, dtype=np.int64)
    source = np.zeros(d, dtype=np.int64)
    homogeneous = rng.integers(0, p, size=2*k, dtype=np.int64)
    u = injection@homogeneous % p
    Js, sources, moments = [], [], []
    steps = 0
    for edge in range(2*k-1):
        order = central_order(H[edge+1]@H[edge] % p, p)
        sign = 1 if edge % 2 == 0 else -1
        for _ in range(2*order):
            H, J = crossing(H, edge, sign, p)
            b = rng.integers(0, p, size=d, dtype=np.int64)
            source = (J@source+b) % p
            total = J@total % p
            u = (J@u+b) % p
            Js.append(J); sources.append(b); moments.append(moment(H, p))
            steps += 1
        assert all(np.array_equal(v, w) for v, w in zip(initial, H))
    D = q@total@injection % p
    assert not np.any(D@a % p) and not np.any(M@D % p)
    assert np.array_equal(u, (total@injection@homogeneous+source) % p)
    c = q@u % p
    effective_source = (c-q@source) % p
    assert np.array_equal(effective_source, D@homogeneous % p)
    assert np.array_equal(M@c % p, sum((m@b % p for m, b in zip(moments, sources)), np.zeros(3, dtype=np.int64)) % p)

    # Reverse transport independently evaluates every q T_(L:s+1) b_s.
    transported = np.zeros(2*k, dtype=np.int64)
    suffix = q.copy()
    for J, b in zip(reversed(Js), reversed(sources)):
        transported = (transported+suffix@b) % p
        suffix = suffix@J % p
    assert np.array_equal(transported, q@source % p)

    # Independently reconstruct the dual affine functional on each stage.
    # Re-use an explicit covector sequence, without reusing the accumulated source.
    ell_seq = [rng.integers(0, p, size=d, dtype=np.int64) for _ in Js]
    current = injection@homogeneous % p
    value = 0
    for J, b, ell in zip(Js, sources, ell_seq):
        current = (J@current+b) % p
        value = (value+int(ell@current)) % p
    homogeneous_row = np.zeros(d, dtype=np.int64)
    affine_value = 0
    for J, b, ell in zip(reversed(Js), reversed(sources), reversed(ell_seq)):
        homogeneous_row = (homogeneous_row+ell) % p
        affine_value = (affine_value+int(homogeneous_row@b)) % p
        homogeneous_row = homogeneous_row@J % p
    assert value == (int(homogeneous_row@injection@homogeneous)+affine_value) % p
    return {'bridges': k, 'prime': p, 'crossings': steps,
            'endpoint_map_shape': list(D.shape), 'endpoint_map_rank': rank(D, p),
            'gauge_and_global_dependency_ranks': [rank(a, p), rank(M, p)],
            'all_local_moment_and_residue_volume_identities': True,
            'full_source_and_dual_affine_constant_transport': True,
            'test_word_is_not_asserted_to_present_a_knot': True}


def main():
    symbolic = symbolic_local_identities()
    universal = symbolic_source_contraction()
    plats = [actual_plat_case(k, p) for p in (7, 11) for k in range(2, 7)]
    result = {
        'scope': 'Arbitrary-bridge scheme and sourced classical complex reduction. No claim of a full quantum affine-extension comparison or Kashaev volume growth.',
        'generic_trace_symbolic_identities': symbolic,
        'universal_block_source_identities': universal,
        'actual_multibridge_Hurwitz_complexes': plats,
    }
    path = Path(__file__).with_name('arbitrary_bridge_source_results.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'results': str(path), 'exact_symbolic_identity_groups': 2,
                      'multibridge_cases': len(plats),
                      'actual_crossing_derivatives': sum(r['crossings'] for r in plats),
                      'maximum_bridge_count': max(r['bridges'] for r in plats)}, indent=2))


if __name__ == '__main__':
    main()
