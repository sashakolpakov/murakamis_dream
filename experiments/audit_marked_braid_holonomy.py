#!/usr/bin/env python3
"""Audit the actual cut-state boundary, classical braiding, and flag chart.

The symbolic checks derive the holonomy map from the actual crossing
symbols. Finite fields independently check Gauss reconstruction, mixed
braid words, and the exact quantum boundary/source identities. No test
asserts a contribution of a critical branch to an asymptotic period.
"""

import json
from pathlib import Path
from random import Random

import numpy as np
import mpmath as mp
import sympy as sp

from audit_finite_sum_annihilator import field, cut_matrix_dense
from audit_kashaev_ado_pointing import color_matrices, WORDS
from audit_relative_octahedral_period import pochhammer_mod


def symbolic_checks():
    K, L, e, f, g, h = sp.symbols("K L e f g h", nonzero=True)

    def reduce(matrix):
        return matrix.applyfunc(sp.factor)

    def plus(k, ee):
        return sp.Matrix([[k, ee], [0, 1]])

    def minus(k, ff):
        return sp.Matrix([[1, 0], [-k*ff, k]])

    def crossing(z, w, sign=1):
        k, ee, ff = z
        l, gg, hh = w
        if sign > 0:
            d = 1-ee*hh
            return ((l*d, (d*gg+ee*(d*l-1/l))/k, k*hh/d),
                    (k/d, ee/(l*d), l*(d*ff+hh*(d/k-k))))
        c = 1-k*gg*ff/l
        return ((l*c, k*gg, ff+hh/k-ff/(l*l*c)),
                (k/c, l*ee+gg-k*k*gg/c, ff/l))

    z, w = (K, e, f), (L, g, h)
    zp, wp = crossing(z, w)
    recovered = crossing(zp, wp, -1)
    assert all(sp.factor(a-b) == 0 for a, b in zip(recovered[0]+recovered[1], z+w))
    kp, ep, fp = zp
    lp, gp, hp = wp
    assert reduce(plus(lp, gp)*plus(kp, ep)-plus(L, g)*plus(K, e)) == sp.zeros(2)
    assert reduce(minus(lp, hp)*minus(kp, fp)-minus(L, h)*minus(K, f)) == sp.zeros(2)
    assert reduce(plus(lp, gp)*minus(kp, fp)-minus(L, h)*plus(K, e)) == sp.zeros(2)
    casimir = lambda t: t[0]+1/t[0]+t[1]*t[2]
    assert sp.factor(casimir(zp)-casimir(w)) == 0
    assert sp.factor(casimir(wp)-casimir(z)) == 0
    G = lambda t: minus(t[0], t[2]).inv()*plus(t[0], t[1])
    H1 = G(z)
    H2 = minus(K, f).inv()*G(w)*minus(K, f)
    H1p = G(zp)
    H2p = minus(kp, fp).inv()*G(wp)*minus(kp, fp)
    assert reduce(H2p-H1) == sp.zeros(2)
    assert reduce(H1p-H1.inv()*H2*H1) == sp.zeros(2)

    # Independently reconstruct both crossing maps from their phase ratios.
    A, B, p, r, x = sp.symbols("A B p r x", nonzero=True)
    P = lambda t: (1-t)*(1-x*x/t)/x
    z, w = (x/A, P(A)*p, 1/p), (x/B, P(B)*r, 1/r)
    C = 1/(1-P(A)*p/r)
    pout1 = A*r/(C*x)
    pout2 = (B*C/x*(1-A)*(1-x*x/A)
             /((1-A/C)*(1-x*x*C/A))*p)
    target = ((x/(B*C), P(B*C)*pout1, 1/pout1),
              (x/(A/C), P(A/C)*pout2, 1/pout2))
    zp, wp = crossing(z, w)
    assert all(sp.factor(a-b) == 0 for a, b in zip(zp+wp, target[0]+target[1]))
    C = 1-(B/A)*P(B)*r/p
    pout1 = (x/A*(1-B)*(1-x*x/B)
             /((1-B/C)*(1-x*x*C/B))*r)
    pout2 = x*p/B
    target = ((x/(B/C), P(B/C)*pout1, 1/pout1),
              (x/(A*C), P(A*C)*pout2, 1/pout2))
    zp, wp = crossing(z, w, -1)
    assert all(sp.factor(a-b) == 0 for a, b in zip(zp+wp, target[0]+target[1]))

    # The fixed flag selected by the factorial vacuum, at arbitrary color.
    k = x/A
    zz = (k, (1-x*x/A)/x, 1-A)
    assert reduce((G(zz)-sp.eye(2)/x)*sp.Matrix([1, 1])) == sp.zeros(2, 1)

    # Formal multiplicative boundary wedge, including the inverse orientation
    # and the half-sized meridian step (the coefficient 2).
    basis = [sp.eye(9)[:, j] for j in range(9)]
    aa, bb, cc, xx, pin1, pin2, pout1, pout2, longitude = basis
    wedge = lambda a, b: a*b.T-b*a.T
    for sign in (-1, 1):
        U, V = bb+sign*cc, aa-sign*cc
        left = (-wedge(aa, pout2-pin1)-wedge(bb, pout1-pin2)
                -wedge(cc, sign*(pout1-pout2))-2*wedge(xx, longitude))
        right = (wedge(aa, pin1)+wedge(bb, pin2)-wedge(U, pout1)
                 -wedge(V, pout2)-2*wedge(xx, longitude))
        assert left == right
    return {"positive_and_inverse_generating_symbols_derived": True,
            "rational_inverse_checked": True,
            "two_coproduct_factorizations_and_cross_factorization": True,
            "Casimirs_swapped": True, "Hurwitz_rule_exact": True,
            "vacuum_selects_inverse_meridian_eigenflag": True,
            "positive_and_inverse_boundary_wedge_with_meridian_factor_two": True}


def mm(a, b, prime):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2)) % prime
                 for i in range(2) for j in range(2))


def mi(a, prime):
    det = (a[0]*a[3]-a[1]*a[2]) % prime
    unit = pow(det, -1, prime)
    return tuple(v*unit % prime for v in (a[3], -a[1], -a[2], a[0]))


def conjugate(g, a, prime):
    return mm(mm(g, a, prime), mi(g, prime), prime)


def matrix_power_mod(matrix, exponent, prime):
    result = np.eye(matrix.shape[0], dtype=np.int64)
    base = matrix % prime
    while exponent:
        if exponent & 1:
            result = result@base % prime
        base = base@base % prime
        exponent >>= 1
    return result


def lower(z, prime):
    k, _, f = z
    return (1, 0, -k*f % prime, k)


def group(z, prime):
    k, e, f = z
    return (k, e, k*f % prime, (pow(k, -1, prime)+e*f) % prime)


def to_holonomies(states, prime):
    previous = (1, 0, 0, 1)
    result = []
    for state in states:
        result.append(conjugate(mi(previous, prime), group(state, prime), prime))
        previous = mm(lower(state, prime), previous, prime)
    return result


def from_holonomies(holonomies, prime):
    previous = (1, 0, 0, 1)
    result = []
    for holonomy in holonomies:
        raw = conjugate(previous, holonomy, prime)
        k = raw[0]
        state = (k, raw[1], raw[2]*pow(k, -1, prime) % prime)
        assert group(state, prime) == raw
        result.append(state)
        previous = mm(lower(state, prime), previous, prime)
    return result


def crossing_mod(z, w, prime, sign):
    k, e, f = z
    l, g, h = w
    if sign > 0:
        d = (1-e*h) % prime
        di = pow(d, -1, prime)
        return ((l*d % prime,
                 (d*g+e*(d*l-pow(l, -1, prime)))*pow(k, -1, prime) % prime,
                 k*h*di % prime),
                (k*di % prime, e*pow(l*d % prime, -1, prime) % prime,
                 l*(d*f+h*(d*pow(k, -1, prime)-k)) % prime))
    c = (1-k*g*f*pow(l, -1, prime)) % prime
    ci = pow(c, -1, prime)
    return ((l*c % prime, k*g % prime,
             (f+h*pow(k, -1, prime)-f*pow(l*l*c % prime, -1, prime)) % prime),
            (k*ci % prime, (l*e+g-k*k*g*ci) % prime,
             f*pow(l, -1, prime) % prime))


def braid_states(states, word, prime):
    result = list(states)
    for j, sign in word:
        result[j:j+2] = crossing_mod(result[j], result[j+1], prime, sign)
    return result


def braid_groups(groups, word, prime):
    result = list(groups)
    for j, sign in word:
        a, b = result[j:j+2]
        if sign > 0:
            result[j:j+2] = [conjugate(mi(a, prime), b, prime), a]
        else:
            result[j:j+2] = [b, conjugate(b, a, prime)]
    return result


def braid_checks():
    rng = Random(260126)
    records = []
    for prime in (101, 1009, 1237):
        successes = attempts = yang_baxter = inverse_cases = 0
        while successes < 100:
            attempts += 1
            assert attempts < 10000
            count = rng.randrange(3, 6)
            x = prime-1 if successes % 2 == 0 else rng.randrange(1, prime)
            s = (x+pow(x, -1, prime)) % prime
            states = []
            for _ in range(count):
                k, f = rng.randrange(1, prime), rng.randrange(1, prime)
                e = (s-k-pow(k, -1, prime))*pow(f, -1, prime) % prime
                states.append((k, e, f))
            word = [(rng.randrange(count-1), rng.choice((-1, 1))) for _ in range(12)]
            try:
                group_input = to_holonomies(states, prime)
                assert from_holonomies(group_input, prime) == states
                changed = braid_states(states, word, prime)
                assert to_holonomies(changed, prime) == braid_groups(group_input, word, prime)
                assert from_holonomies(to_holonomies(changed, prime), prime) == changed
                left = braid_states(states[:3], [(0, 1), (1, 1), (0, 1)], prime)
                right = braid_states(states[:3], [(1, 1), (0, 1), (1, 1)], prime)
                assert left == right
                yang_baxter += 1
                for sign in (-1, 1):
                    assert braid_states(states, [(0, sign), (0, -sign)], prime) == states
                    inverse_cases += 1
            except ValueError:  # Outside a specified Gauss chart; no identity is tested there.
                continue
            successes += 1
        records.append({"prime": prime, "successful_mixed_words": successes,
                        "word_length": 12, "Yang_Baxter_cases": yang_baxter,
                        "inverse_cases": inverse_cases, "attempts": attempts,
                        "includes_parabolic_and_variable_color": True})
    return records


def quantum_boundary_check(level):
    prime, generator, q = field(level)
    Q = q*q % prime
    rho = (q-pow(q, -1, prime)) % prime
    factorials = [1]
    for a in range(1, level):
        factorials.append(factorials[-1]*(1-pow(Q, a, prime)) % prime)
    assert factorials[-1] == level
    vacuum = np.array([pow(v, -1, prime) for v in factorials], dtype=np.int64)
    covacuum = np.array([v*pow(level, -1, prime) % prime for v in factorials], dtype=np.int64)
    assert int(covacuum@vacuum) % prime == 1
    D = np.diag(vacuum)
    Di = np.diag(np.array(factorials, dtype=np.int64))
    sigma = np.zeros((level, level), dtype=np.int64)
    for a in range(level):
        sigma[a, (a+1) % level] = 1
    multiplier = np.diag([pow(Q, a, prime) for a in range(level)]).astype(np.int64)
    inverse_multiplier = np.diag([pow(Q, -a, prime) for a in range(level)]).astype(np.int64)
    cut_projector = np.zeros_like(sigma)
    cut_projector[-1, -1] = 1
    defect_inverse = matrix_power_mod(sigma, level-1, prime)
    cyclic_F = (np.eye(level, dtype=np.int64)-multiplier)@defect_inverse % prime
    comparisons = []
    for at_kashaev, x in ((False, pow(generator, level+7, prime)),
                         (True, pow(q, level-1, prime))):
        E = np.zeros_like(sigma)
        F = np.zeros_like(sigma)
        for a in range(1, level):
            coefficient = ((pow(q, a, prime)-pow(q, -a, prime))
                           *(x*pow(q, 1-a, prime)-pow(x, -1, prime)*pow(q, a-1, prime))) % prime
            E[a-1, a] = coefficient
            F[a, a-1] = 1
        transformed_E = Di@E % prime
        transformed_E = transformed_E@D % prime
        transformed_F = Di@F % prime
        transformed_F = transformed_F@D % prime
        cyclic_E = pow(q, -1, prime)*(pow(x, -1, prime)*np.eye(level, dtype=np.int64)
                                               -x*inverse_multiplier) % prime
        cyclic_E = cyclic_E@sigma % prime
        wall = pow(q, -1, prime)*(pow(x, -1, prime)-Q*x) % prime
        corrected_E = (cyclic_E-wall*(cut_projector@sigma % prime)) % prime
        assert np.array_equal(transformed_E, corrected_E)
        assert np.array_equal(transformed_F, cyclic_F)
        central_defect = (pow(x, level, prime)-pow(x, -level, prime)) % prime
        assert np.array_equal(matrix_power_mod(cyclic_E, level, prime),
                              central_defect*np.eye(level, dtype=np.int64) % prime)
        assert not np.any(matrix_power_mod(corrected_E, level, prime))
        if at_kashaev:
            assert wall == central_defect == 0
        else:
            phase = pow(q, level*(1-level)//2, prime)
            from_defects = phase*wall*pow(central_defect, -1, prime) % prime
            M = -q*x % prime
            i = pow(generator, (prime-1)//4, prime)
            eta = pow(i, level+3, prime)
            normalizer = (eta*pow(M, level-1, prime)
                          *pow(sum(pow(M, 2*a, prime) for a in range(level)) % prime, -1, prime)) % prime
            assert from_defects == normalizer
        records = 0
        if level <= 6:
            data = color_matrices(level, prime, q, x)
            gauge = np.kron(D, D)
            inverse_gauge = np.kron(Di, Di)
            for sign, old in zip((1, -1), data[:2]):
                transformed = inverse_gauge@old % prime
                transformed = transformed@gauge % prime
                independent = np.zeros_like(old)
                for a in range(level):
                    for b in range(level):
                        maximum = (min(a, level-1-b) if sign > 0 else min(b, level-1-a))
                        for shift in range(maximum+1):
                            if sign > 0:
                                phase = (pow(-1, shift, prime)*pow(x, -a-b-shift, prime)
                                         *pow(Q, a*b+(a-b)*shift-shift*(shift+1)//2, prime)) % prime
                                product = pochhammer_mod(x*x*pow(Q, 1-a, prime) % prime,
                                                         Q, shift, prime)
                                ratio = (factorials[b+shift]*pow(factorials[b], -1, prime)
                                         *pow(factorials[shift], -1, prime)) % prime
                                c, d = b+shift, a-shift
                            else:
                                phase = pow(x, a+b-shift, prime)*pow(Q, -a*b, prime) % prime
                                product = pochhammer_mod(x*x*pow(Q, 1-b, prime) % prime,
                                                         Q, shift, prime)
                                ratio = (factorials[a+shift]*pow(factorials[a], -1, prime)
                                         *pow(factorials[shift], -1, prime)) % prime
                                c, d = b-shift, a+shift
                            independent[c*level+d, a*level+b] = phase*product*ratio % prime
                assert np.array_equal(independent, transformed)
            for word in WORDS:
                cut = cut_matrix_dense(level, prime, data, 3, word)
                paired = int(covacuum@(cut@vacuum % prime)) % prime
                assert paired == int(cut[0, 0])
                transformed_cut = Di@cut % prime
                transformed_cut = transformed_cut@D % prime
                averaged = int(np.sum(transformed_cut)) % prime*pow(level, -1, prime) % prime
                assert averaged == paired
                records += 1
        comparisons.append({"Kashaev_color": at_kashaev,
                            "exact_rank_one_E_wall": True,
                            "cyclic_central_E_defect": int(central_defect),
                            "nilpotent_actual_E_checked": True,
                            "dimension_as_defect_ratio_checked": not at_kashaev,
                            "actual_cut_period_pairings_checked": records})
    return {"level": level, "prime": prime, "vacuum_and_dual_pair_to_one": True,
            "records": comparisons}


def geometric_chart_check(prime):
    """An algebraic geometric-branch calibration, not a volume experiment."""
    u = next(a for a in range(1, prime) if (a*a-a+1) % prime == 0)
    A = (1, 1, 0, 1)
    B = (1, 0, u, 1)
    C = mm(mm(mm(mm(mi(A, prime), B, prime), A, prime), mi(B, prime), prime), A, prime)
    meridians = [A, B, C]
    assert braid_groups(meridians, WORDS[0], prime) == meridians
    chosen = None
    for r in range(prime):
        for s in range(1, prime):
            # The columns sum to the eigenvector (1,0), so the flag is 1 in this frame.
            basis = (r, (1-r) % prime, s, -s % prime)
            groups = [tuple(-v % prime for v in conjugate(mi(basis, prime), m, prime))
                      for m in meridians]
            try:
                states = from_holonomies(groups, prime)
                assert states[0][2] == (1+pow(states[0][0], -1, prime)) % prime
                if any(0 in z for z in states):
                    continue
                start = list(states)
                shapes = []
                for j, sign in WORDS[0]:
                    k, e, f = states[j]
                    l, g, h = states[j+1]
                    a, b = -pow(k, -1, prime) % prime, -pow(l, -1, prime) % prime
                    c = (pow(1-e*h, -1, prime) if sign > 0
                         else (1-k*g*f*pow(l, -1, prime)) % prime)
                    states[j:j+2] = crossing_mod(states[j], states[j+1], prime, sign)
                    if any(0 in z for z in states):
                        raise ValueError("A chart boundary")
                    U, W = (b, pow(a, -1, prime)) if sign > 0 else (a, pow(b, -1, prime))
                    # Five oriented shapes for the balanced crossing octahedron.
                    local = [c, U, pow(U*c % prime, -1, prime), W,
                             pow(c*W % prime, -1, prime)]
                    assert all(z not in (0, 1) for z in local)
                    shapes.append(local)
                assert states == start
                chosen = {"frame_parameters": [r, s], "Gauss_states": [list(z) for z in start],
                          "five_shapes_at_each_crossing": shapes}
                break
            except (ValueError, ZeroDivisionError):
                continue
        if chosen is not None:
            break
    assert chosen is not None
    return {"prime": prime, "Riley_parameter": u,
            "Riley_equation": "u^2-u+1=0", "fixed_braid_point_checked": True,
            "unit_cut_flag_condition_checked": True, **chosen}


def regulator_calibration():
    mp.mp.dps = 80
    u = mp.exp(-mp.pi*1j/3)
    A = mp.matrix([[1, 1], [0, 1]])
    B = mp.matrix([[1, 0], [u, 1]])
    C = A**-1*B*A*B**-1*A

    def D(z):
        return mp.im(mp.polylog(2, z))+mp.log(abs(z))*mp.arg(1-z)

    expected = -2*D(u)
    records = []
    for r, s in ((mp.mpf(2), mp.mpf(3)), (mp.mpc(1, 1), mp.mpf(2)),
                 (mp.mpf(3), mp.mpc(-2, 1))):
        frame = mp.matrix([[r, 1-r], [s, -s]])
        holonomies = [-frame**-1*m*frame for m in (A, B, C)]
        previous = mp.eye(2)
        states = []
        for H in holonomies:
            G = previous*H*previous**-1
            k, e, f = G[0, 0], G[0, 1], G[1, 0]/G[0, 0]
            states.append((k, e, f))
            previous = mp.matrix([[1, 0], [-k*f, k]])*previous
        initial = list(states)
        regulator = mp.mpf(0)
        for j, sign in WORDS[0]:
            k, e, f = states[j]
            l, g, h = states[j+1]
            a, b = -1/k, -1/l
            if sign > 0:
                d = 1-e*h
                c = 1/d
                U, W = b, 1/a
                changed = [(l*d, (d*g+e*(d*l-1/l))/k, k*h/d),
                           (k/d, e/(l*d), l*(d*f+h*(d/k-k)))]
            else:
                c = 1-k*g*f/l
                U, W = a, 1/b
                changed = [(l*c, k*g, f+h/k-f/(l*l*c)),
                           (k/c, l*e+g-k*k*g/c, f/l)]
            regulator += D(U)+D(c)+D(W)-D(U*c)-D(c*W)
            states[j:j+2] = changed
        error = abs(regulator-expected)
        fixed_error = max(abs(a-b) for z, w in zip(states, initial) for a, b in zip(z, w))
        assert error < mp.mpf("1e-65") and fixed_error < mp.mpf("1e-65")
        records.append({"frame_parameters": [str(r), str(s)],
                        "regulator": str(regulator), "error": float(error),
                        "fixed_point_error": float(fixed_error)})
    return {"scope": "Numerical calibration of sign and frame rigidity; no all-knot fundamental-class claim.",
            "expected_two_tetrahedron_period": str(expected), "records": records}


def main():
    result = {"scope": "Exact actual cut boundary and global classical holonomy/critical-locus comparison; no asymptotic branch-selection assertion.",
              "symbolic": symbolic_checks(),
              "braid_words": braid_checks(),
              "quantum_boundaries": [quantum_boundary_check(n) for n in (2, 3, 4, 5, 6, 8, 9, 10, 12, 15)],
              "geometric_branch_calibrations": [geometric_chart_check(p) for p in (97, 193, 601)],
              "regulator_calibration": regulator_calibration()}
    Path(__file__).with_name("marked_braid_holonomy_results.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"symbolic": result["symbolic"],
                      "mixed_braid_words": sum(r["successful_mixed_words"] for r in result["braid_words"]),
                      "quantum_levels": [r["level"] for r in result["quantum_boundaries"]],
                      "geometric_chart_calibrations": len(result["geometric_branch_calibrations"]),
                      "all_checks_passed": True}), flush=True)


if __name__ == "__main__":
    main()
