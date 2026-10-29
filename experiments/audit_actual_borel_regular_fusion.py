#!/usr/bin/env python3
"""Actual Borel regular fusion, R transport and retained divided cap source."""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_two_cut_ports import balanced_data, word_matrix
from audit_high_color_first_normal_r_degree import root_field
from audit_semicyclic_carry_braiding import positive, negative, transported


def inv(A, p):
    return np.array(sp.Matrix(A.tolist()).inv_mod(p)).astype(np.int64)


def powers(A, N, p):
    out = [np.eye(len(A), dtype=np.int64)]
    for _ in range(N):
        out.append(out[-1]@A % p)
    return out


def alg_product(a, b, N, central, p):
    out = np.zeros(N*N, dtype=np.int64)
    for degree, j in itertools.product(range(N), repeat=2):
        av = int(a[degree*N+j])
        if not av:
            continue
        for d, k in itertools.product(range(N), repeat=2):
            bv = int(b[d*N+k])
            if bv and k == (j-d) % N:
                total = degree+d
                index = (total % N)*N+k
                out[index] = (out[index]+av*bv*pow(central, total//N, p)) % p
    return out


def right_regular(a, N, central, p):
    columns = []
    for k in range(N*N):
        unit = np.zeros(N*N, dtype=np.int64)
        unit[k] = 1
        columns.append(alg_product(unit, a, N, central, p))
    return np.column_stack(columns)


def fusion(N, p, Q, xs, phis):
    b = len(xs)
    I = np.eye(N, dtype=np.int64)
    Fs, Ks = [], []
    for x, phi in zip(xs, phis):
        F = np.zeros((N, N), dtype=np.int64)
        for j in range(N-1):
            F[j+1, j] = (1-pow(Q, j+1, p)) % p
        F[0, N-1] = phi*pow(N, -1, p) % p
        Fs.append(F)
        Ks.append(np.diag([x*pow(Q, -j, p) % p for j in range(N)]).astype(np.int64))
    f = np.zeros((N**b, N**b), dtype=np.int64)
    K = np.array([[1]], dtype=np.int64)
    for k in Ks:
        K = np.kron(K, k) % p
    xprod = 1
    for x in xs:
        xprod = xprod*x % p
    H = K*pow(xprod, -1, p) % p
    for i in range(b):
        term = np.array([[1]], dtype=np.int64)
        for j in range(b):
            value = np.diag([pow(int(a), -1, p) for a in np.diag(Ks[j])]) if j < i else Fs[j] if j == i else I
            term = np.kron(term, value) % p
        f = (f+term) % p
    total, prefix = 0, 1
    for x, phi in zip(xs, phis):
        total = (total+pow(prefix, -N, p)*phi) % p
        prefix = prefix*x % p
    fp = powers(f, N, p)
    assert np.array_equal(fp[N], total*np.eye(N**b, dtype=np.int64) % p)
    assert np.array_equal(H@f % p, pow(Q, -1, p)*f@H % p)
    tails = list(itertools.product(range(N), repeat=b-2))
    columns = []
    for tail in tails:
        for a, j in itertools.product(range(N), repeat=2):
            second = (j-sum(tail)) % N
            state = (0, second)+tail
            index = 0
            for value in state:
                index = index*N+value
            seed = np.zeros(N**b, dtype=np.int64)
            seed[index] = 1
            columns.append(fp[a]@seed % p)
    C = np.column_stack(columns)
    Ci = inv(C, p)
    # Independent regular-algebra action check.
    identity = np.zeros(N*N, dtype=np.int64)
    identity[:N] = 1
    f_alg = np.zeros(N*N, dtype=np.int64)
    f_alg[N:2*N] = 1
    left_f = np.column_stack([alg_product(f_alg, np.eye(N*N, dtype=np.int64)[:, k], N, total, p)
                              for k in range(N*N)])
    left_H = np.diag([pow(Q, -(a+j), p) for a, j in itertools.product(range(N), repeat=2)]).astype(np.int64)
    copies = len(tails)
    assert np.array_equal(Ci@f@C % p, np.kron(np.eye(copies, dtype=np.int64), left_f) % p)
    assert np.array_equal(Ci@H@C % p, np.kron(np.eye(copies, dtype=np.int64), left_H) % p)
    return C, Ci, total, H, f, Ks, tails


def verify_relative(R, C, Ci, N, central, p):
    relative = Ci@R@C % p
    copies = len(R)//(N*N)
    one = np.zeros(N*N, dtype=np.int64)
    one[:N] = 1
    for source in range(copies):
        vector = np.zeros(len(R), dtype=np.int64)
        vector[source*N*N:(source+1)*N*N] = one
        image = relative@vector % p
        for target in range(copies):
            a = image[target*N*N:(target+1)*N*N]
            block = relative[target*N*N:(target+1)*N*N, source*N*N:(source+1)*N*N]
            assert np.array_equal(block, right_regular(a, N, central, p))
    return relative


def physical_cap(O, Ks, N, p):
    b = len(Ks)
    result = 0
    for closed in itertools.product(range(N), repeat=b-1):
        weight = 1
        for i, state in enumerate(closed, start=1):
            weight = weight*pow(int(Ks[i][state, state]), 1-N, p) % p
        column = 0
        for state in (0,)+closed:
            column = column*N+state
        for first in range(N):
            row = 0
            for state in (first,)+closed:
                row = row*N+state
            result = (result+weight*int(O[row, column])) % p
    return result


def frobenius_word_cap(relative, C, Ks, N, central, p):
    """Equation (7a), without conjugating the source by C inverse."""
    b = len(Ks)
    tails = list(itertools.product(range(N), repeat=b-2))
    one = np.zeros(N*N, dtype=np.int64)
    one[:N] = 1
    total = 0
    for source, s in enumerate(tails):
        input_unit = np.zeros(N**b, dtype=np.int64)
        input_unit[source*N*N:(source+1)*N*N] = one
        image = relative@input_unit % p
        for target, _ in enumerate(tails):
            a_ts = image[target*N*N:(target+1)*N*N]
            cap_density = np.zeros(N*N, dtype=np.int64)
            for degree, j in itertools.product(range(N), repeat=2):
                second = (j+degree-sum(s)) % N
                closed = (second,)+s
                weight = 1
                for i, state in enumerate(closed, start=1):
                    weight = weight*pow(int(Ks[i][state, state]), 1-N, p) % p
                column = target*N*N+degree*N+j
                value = 0
                for first in range(N):
                    row = 0
                    for state in (first,)+closed:
                        row = row*N+state
                    value += int(C[row, column])
                value = value*weight % p
                cap_density[(N-1-degree)*N+(j+degree) % N] = value
            product = alg_product(cap_density, a_ts, N, central, p)
            total = (total+int(product[(N-1)*N:].sum())) % p
    return total


def nilpotent_actual_case(N, strands):
    p, _, q, _, _, K, _, plus, minus = balanced_data(N)
    Q, x = q*q % p, int(K[0, 0])
    C, Ci, central, H, f, Ks, _ = fusion(N, p, Q, [x]*strands, [0]*strands)
    assert central == 0
    local = []
    for slot in range(strands-1):
        for sign, R0 in ((1, plus), (-1, minus)):
            R = np.kron(np.kron(np.eye(N**slot, dtype=np.int64), R0),
                        np.eye(N**(strands-slot-2), dtype=np.int64)) % p
            assert np.array_equal(R@H % p, H@R % p)
            assert np.array_equal(R@f % p, f@R % p)
            relative = verify_relative(R, C, Ci, N, central, p)
            assert physical_cap(R, Ks, N, p) == physical_cap(C@relative@Ci % p, Ks, N, p)
            assert physical_cap(R, Ks, N, p) == frobenius_word_cap(relative, C, Ks, N, central, p)
            local.append((slot, sign))
    if strands == 3:
        word = (1, -2, 1, -2)
        W = word_matrix(word, plus, minus, strands, N, p)
        relative = verify_relative(W, C, Ci, N, central, p)
        assert physical_cap(W, Ks, N, p) == physical_cap(C@relative@Ci % p, Ks, N, p)
        assert physical_cap(W, Ks, N, p) == frobenius_word_cap(relative, C, Ks, N, central, p)
    return {"N": N, "strands": strands, "actual_free_Borel_copies": N**(strands-2),
            "literal_signed_R_relative_right_multiplications": len(local),
            "original_pivotal_highest_Whittaker_source_retained": True,
            "explicit_general_word_Frobenius_cap_formula": True,
            "all_halfCartan_R_lines_retained": True}


def frobenius_and_cap(N):
    p, _, q, _, _, K, _, _, _ = balanced_data(N)
    Q, x = q*q % p, int(K[0, 0])
    F = [1]
    for j in range(1, N):
        F.append(F[-1]*(1-pow(Q, j, p)) % p)
    cap = np.zeros(N*N, dtype=np.int64)
    values = []
    for a, j in itertools.product(range(N), repeat=2):
        value = 0
        if j+a < N:
            value = pow(x, 1-N-a, p)*pow(Q, -(j+a), p)*F[j+a]*pow(F[j], -1, p) % p
        values.append(value)
        cap[(N-1-a)*N+(j+a) % N] = value
    gamma = N*pow(x, 2-2*N, p)*Q % p
    assert np.array_equal(alg_product(cap, cap, N, 0, p), gamma*cap % p)
    # Compare every marked cap basis value to the ORIGINAL pivotal cut.
    C, Ci, _, _, _, Ks, _ = fusion(N, p, Q, [x, x], [0, 0])
    for k, value in enumerate(values):
        z = np.zeros(N*N, dtype=np.int64)
        z[k] = 1
        assert physical_cap(C@right_regular(z, N, 0, p)@Ci % p, Ks, N, p) == value
    for central in (0, 2):
        # Frobenius duality is independent of the central norm, including zero.
        for a, j, c, k in itertools.product(range(N), repeat=4):
            d = np.zeros(N*N, dtype=np.int64)
            z = np.zeros(N*N, dtype=np.int64)
            d[(N-1-a)*N+(j+a) % N] = 1
            z[c*N+k] = 1
            product = alg_product(d, z, N, central, p)
            top = int(product[(N-1)*N:].sum()) % p
            assert top == int(a == c and j == k)
        cyclic_f = np.zeros((N, N), dtype=np.int64)
        for j in range(N-1):
            cyclic_f[j+1, j] = 1
        cyclic_f[0, N-1] = central
        fp = powers(cyclic_f, N, p)
        for a, j in itertools.product(range(N), repeat=2):
            z = fp[a].copy()
            z[:, [k for k in range(N) if k != j]] = 0
            assert int(np.trace(cyclic_f@z)) % p == (central if a == N-1 else 0)
    return {"N": N, "all_actual_cap_basis_values": N*N,
            "primitive_cap_density_gamma": int(gamma), "flat_Frobenius_Gram_cases": 2*N**4,
            "divided_trace_polynomial_identity_including_zero_norm": True}


def semicyclic_case(N):
    p, eta = root_field(N)
    q, Q = pow(eta, 2, p), pow(eta, 4, p)
    x = int(sp.primitive_root(p))
    inputs = [2, 3]
    output = list(transported(N, p, q, x, *inputs, 1))
    C, Ci, central, _, _, _, _ = fusion(N, p, Q, [x, x], inputs)
    D, Di, central_out, _, _, _, _ = fusion(N, p, Q, [x, x], output)
    assert central == central_out
    factorial = [1]
    for j in range(1, N):
        factorial.append(factorial[-1]*(1-pow(Q, j, p)) % p)
    gauge = np.array([factorial[i]*factorial[j] % p for i, j in itertools.product(range(N), repeat=2)], dtype=np.int64)
    gi = np.array([pow(int(a), -1, p) for a in gauge], dtype=np.int64)
    scalar = pow(x, N-1, p)*pow(eta, -(N-1)**2, p) % p
    R = scalar*gauge[:, None]*positive(N, p, q, x, *inputs)*gi[None, :] % p
    Rinv = pow(scalar, -1, p)*gauge[:, None]*negative(N, p, q, x, *output)*gi[None, :] % p
    assert np.array_equal(Rinv@R % p, np.eye(N*N, dtype=np.int64))
    relative = Di@R@C % p
    relative_inv = Ci@Rinv@D % p
    one = np.zeros(N*N, dtype=np.int64)
    one[:N] = 1
    a = relative@one % p
    assert np.array_equal(relative, right_regular(a, N, central, p))
    assert np.array_equal(relative_inv@relative % p, np.eye(N*N, dtype=np.int64))
    return {"N": N, "input_F_centres": inputs, "transported_F_centres": output,
            "coproduct_F_norm_preserved": int(central),
            "genuine_holonomy_R_relative_right_multiplication": True,
            "anchored_scalar_and_corrected_wrap_retained": True}


def characteristic_zero():
    I = sp.I
    eta = (1+I)/sp.sqrt(2)
    R = sp.Matrix([[eta, 0, 0, 0], [0, 0, 1/eta, 0],
                   [0, 1/eta, 2*I/eta, 0], [0, 0, 0, eta]])
    F = sp.Matrix([[0, 0], [2, 0]])
    K = sp.diag(I, -I)
    f = sp.kronecker_product(F, sp.eye(2))+sp.kronecker_product(K.inv(), F)
    u0, u1 = sp.Matrix([1, 0, 0, 0]), sp.Matrix([0, 1, 0, 0])
    C = sp.Matrix.hstack(u0, u1, f*u0, f*u1)
    relative = (C.inv()*R*C).applyfunc(sp.simplify)
    # Basis e0,e1,f e0,f e1; right multiplication by f e0 has this one arrow.
    radical = sp.zeros(4)
    radical[2, 1] = 1
    assert (relative-eta*sp.eye(4)-radical/(2*eta)).applyfunc(sp.simplify) == sp.zeros(4)
    g = [-I, I]
    ptr = lambda O: sp.Matrix(2, 2, lambda c, a: sum(g[t]*O[c*2+t, a*2+t] for t in range(2)))
    assert ptr(sp.eye(4)) == sp.zeros(2)
    assert ptr(C*radical*C.inv()) == 2*sp.eye(2)
    assert (ptr(R)-sp.eye(2)/eta).applyfunc(sp.simplify) == sp.zeros(2)
    normal = F*0  # Direct actual coproduct source in equation (13).
    A, B = sp.kronecker_product(F, sp.eye(2)), sp.kronecker_product(K.inv(), F)
    ghost = A*B/2
    assert (sp.ones(1, 4)*ghost*u0)[0] == -2*I
    return {"actual_N2_R_unit": "eta I+(eta^-1/2) f e0", "actual_cap_I": "0",
            "actual_cap_radical": "2", "original_nonzero_period_from_radical": "eta^-1",
            "selected_Q_normal_fused_carry": "-2i"}


def main():
    regular = [nilpotent_actual_case(N, 2) for N in range(2, 7)]
    regular += [nilpotent_actual_case(N, 3) for N in (2, 3)]
    caps = [frobenius_and_cap(N) for N in range(2, 6)]
    semicyclic = [semicyclic_case(N) for N in (2, 3, 4)]
    result = {"status": "pass", "actual_regular_fusion_cases": regular,
              "actual_frobenius_caps": caps, "genuine_semicyclic_transport": semicyclic,
              "characteristic_zero_source_and_radical": characteristic_zero(),
              "scope": "Actual non-naive Borel relative word/source transport and divided central-F trace; no geometric source identification or volume theorem."}
    output = Path(__file__).with_name("actual_borel_regular_fusion_results.json")
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "pass", "actual_regular_fusion_cases": len(regular),
                      "actual_Frobenius_cap_levels": len(caps), "genuine_semicyclic_transports": len(semicyclic),
                      "results": str(output)}, indent=2))


if __name__ == "__main__":
    main()
