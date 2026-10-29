#!/usr/bin/env python3
"""Audit exact quantum longitude insertion and its marked classical action.

The finite identities are checked against the actual dense cut matrices,
including singular local ratios at the Kashaev color. Symbolic transport
fixes eigenflag, longitude, framing, and square-root conventions.
Numerical action checks validate an algebraic logarithmic identity; they
do not assert that the actual period contains a geometric saddle term.
"""

import json
from itertools import product
from pathlib import Path

import mpmath as mp
import sympy as sp

from audit_finite_sum_annihilator import field, cut_matrix_dense
from audit_kashaev_ado_pointing import color_matrices, WORDS
from audit_relative_octahedral_period import pochhammer_mod, root_factorials, rewritten_crossing


def symbolic_transport():
    A, B, p, r, x = sp.symbols("A B p r x", nonzero=True)
    P = lambda z: (1-z)*(1-x*x/z)/x
    z, w = (x/A, P(A)*p, 1/p), (x/B, P(B)*r, 1/r)

    def crossing(z, w, sign):
        K, e, f = z
        L, g, h = w
        if sign > 0:
            d = 1-e*h
            return ((L*d, (d*g+e*(d*L-1/L))/K, K*h/d),
                    (K/d, e/(L*d), L*(d*f+h*(d/K-K))))
        c = 1-K*g*f/L
        return ((L*c, K*g, f+h/K-f/(L*L*c)),
                (K/c, L*e+g-K*K*g/c, f/L))

    def lower(z):
        K, _, f = z
        return sp.Matrix([[1, 0], [-K*f, K]])

    def G(z):
        K, e, f = z
        return sp.Matrix([[K, e], [K*f, 1/K+e*f]])

    def vector(z):
        K, e, _ = z
        return sp.Matrix([e/(1/x-K), 1])

    v1, v2 = vector(z), lower(z).inv()*vector(w)
    H1, H2 = G(z), lower(z).inv()*G(w)*lower(z)
    for sign in (1, -1):
        zp, wp = crossing(z, w, sign)
        out1, out2 = vector(zp), lower(zp).inv()*vector(wp)
        if sign > 0:
            C = 1/(1-z[1]*w[2])
            tau = B*C/x*(1-x*x/A)/(1-x*x*C/A)
            differences = [out1-H1.inv()*v2, out2-tau*v1]
        else:
            C = 1-z[0]*w[1]*z[2]/w[0]
            tau = x/A*(1-x*x/B)/(1-x*x*C/B)
            differences = [out1-tau*v2, out2-H2*v1]
        assert all(d.applyfunc(sp.factor) == sp.zeros(2, 1) for d in differences)

    # Integer, unwrapped state indices fix the apparent square-root factor.
    a, b, k, j = sp.symbols("a b k j", integer=True)
    for sign in (-1, 1):
        c, d = b+sign*k, a-sign*k
        assert sp.expand(-j*c-(j+1)*d+j*a+(j+1)*b-(c-a)) == 0
    return {"positive_and_inverse_eigenvector_transport_exact": True,
            "selected_flag_has_meridian_eigenvalue": "M^(-1)",
            "half_density_is_integer_weighted_position_coboundary": True}


def inserted_crossing(a, b, k, sign, q, x, factorials, prime, shifts):
    """r(x) times the ordered inverse tau product, with all poles cancelled."""
    Q = q*q % prime
    A, B, C = pow(Q, a, prime), pow(Q, b, prime), pow(Q, k, prime)
    start = a if sign > 0 else b
    binomial = (factorials[start]*pow(factorials[k], -1, prime)
                *pow(factorials[start-k], -1, prime)) % prime
    u = x*x*pow(Q, 1-start+shifts, prime) % prime
    atom = pochhammer_mod(u, Q, k, prime)
    if sign > 0:
        phase = (pow(-1, k, prime)*pow(x, -a-b-k, prime)
                 *pow(Q, a*b+(a-b)*k-k*(k+1)//2, prime)) % prime
        extra = (pow(x*pow(B*C % prime, -1, prime) % prime, shifts, prime)
                 *pow(q, shifts*(shifts-1)//2, prime)) % prime
    else:
        phase = pow(x, a+b-k, prime)*pow(Q, -a*b, prime) % prime
        extra = (pow(A*pow(x, -1, prime) % prime, shifts, prime)
                 *pow(q, -shifts*(shifts-1)//2, prime)) % prime
    return phase*binomial*atom*extra % prime


def local_insertion_check(level):
    prime, generic, root = field(level)
    records = []
    for at_root, q in ((False, generic), (True, root)):
        factorials = root_factorials(q*q % prime, level, prime)
        colors = [(False, pow(generic, level+7, prime))]
        if at_root:
            colors.append((True, pow(q, level-1, prime)))
        for ideal, x in colors:
            count = 0
            for sign in (-1, 1):
                for a, b in product(range(level), repeat=2):
                    maximum = min(a, level-1-b) if sign > 0 else min(b, level-1-a)
                    for k in range(maximum+1):
                        c = b+sign*k
                        for shifts in (1, 2, 3):
                            inserted = inserted_crossing(a, b, k, sign, q, x,
                                                        factorials, prime, shifts)
                            shifted = rewritten_crossing(a, b, k, sign, q,
                                                         pow(q, shifts, prime)*x % prime,
                                                         factorials, prime)
                            factor = (pow(x, -sign*shifts, prime)
                                      *pow(q, shifts*(c-a)-sign*shifts*(shifts-1)//2, prime)) % prime
                            assert shifted == factor*inserted % prime
                            count += 1
            records.append({"root": at_root, "Kashaev_color": ideal,
                            "cancelled_local_shift_identities": count})
    return {"level": level, "prime": prime, "records": records}


def inserted_period(level, prime, q, x, strands, word, shifts):
    factorials = root_factorials(q*q % prime, level, prime)
    writhe = sum(sign for _, sign in word)
    total = 0
    for closed in product(range(level), repeat=strands-1):
        initial = (0,)+closed
        coefficient = 1
        for a in closed:
            coefficient = (coefficient*pow(x, 1-level, prime)
                           *pow(q, 2*a*(level-1), prime)) % prime
        paths = {initial: coefficient}
        for pos, sign in reversed(word):
            following = {}
            for state, previous in paths.items():
                a, b = state[pos:pos+2]
                maximum = min(a, level-1-b) if sign > 0 else min(b, level-1-a)
                for k in range(maximum+1):
                    value = inserted_crossing(a, b, k, sign, q, x, factorials, prime, shifts)
                    pair = (b+sign*k, a-sign*k)
                    new = state[:pos]+pair+state[pos+2:]
                    following[new] = (following.get(new, 0)+previous*value) % prime
            paths = following
        total = (total+paths.get(initial, 0)) % prime
    return total*pow(x, writhe*(level-1), prime) % prime


def period_checks():
    records = []
    diagrams = [(2, [(0, 1)]*3), (3, WORDS[0]), (3, WORDS[1]), (3, WORDS[2])]
    for level in (2, 3, 4, 5, 6):
        prime, generator, q = field(level)
        for ideal, x in ((False, generator), (True, pow(q, level-1, prime))):
            for strands, word in diagrams:
                writhe = sum(sign for _, sign in word)
                degree = writhe-strands+1
                assert degree % 2 == 0
                gamma = pow(q, (level-1)*degree, prime)
                assert gamma == pow(q, -degree, prime)
                for shifts in (1, 2):
                    inserted = inserted_period(level, prime, q, x, strands, word, shifts)
                    prefactor = (pow(gamma, shifts, prime)*pow(x, -shifts*writhe, prime)
                                 *pow(q, -writhe*shifts*(shifts-1)//2, prime)) % prime
                    shifted_data = color_matrices(level, prime, q,
                                                  pow(q, shifts, prime)*x % prime)
                    dense = cut_matrix_dense(level, prime, shifted_data, strands, word)
                    assert prefactor*inserted % prime == int(dense[0, 0])
                    records.append({"level": level, "Kashaev_color": ideal,
                                    "strands": strands, "writhe": writhe,
                                    "crossings": len(word), "shifts": shifts,
                                    "dense_shifted_period_equals_insertion": True})
    return records


def trefoil_marking():
    M = sp.symbols("M", nonzero=True)
    a, d = -1/(M*(M*M-1)), M**3/(M*M-1)
    A, B = sp.diag(M, 1/M), sp.Matrix([[a, 1], [a*d-1, d]])
    assert (A*B*A-B*A*B).applyfunc(sp.factor) == sp.zeros(2)
    assert ((A*B)**3+sp.eye(2)).applyfunc(sp.factor) == sp.zeros(2)
    basis = sp.Matrix([[1, -1], [2, -1]])
    meridians = [basis.inv()*p*basis for p in (A, B)]
    prefix, states = sp.eye(2), []
    for mu in meridians:
        G = -prefix*mu*prefix.inv()
        K, e, f = G[0, 0], G[0, 1], G[1, 0]/G[0, 0]
        states.append(tuple(sp.factor(t) for t in (K, e, f)))
        prefix = sp.Matrix([[1, 0], [-K*f, K]])*prefix
    initial = states[:]
    tau_product, x = sp.Integer(1), -M
    for _ in range(3):
        K, e, f = states[0]
        L, g, h = states[1]
        dd = sp.factor(1-e*h)
        C, aa, bb = 1/dd, x/K, x/L
        tau_product = sp.factor(tau_product*bb*C/x*(1-x*x/aa)/(1-x*x*C/aa))
        states = [(sp.factor(L*dd), sp.factor((dd*g+e*(dd*L-1/L))/K), sp.factor(K*h/dd)),
                  (sp.factor(K/dd), sp.factor(e/(L*dd)), sp.factor(L*(dd*f+h*(dd/K-K))))]
    assert all(sp.factor(a-b) == 0 for z, w in zip(states, initial) for a, b in zip(z, w))
    L_intr = sp.factor(x**-3/tau_product)
    assert L_intr == -M**-6
    W = B.inv()*A.inv()*(A.inv()*B*A).inv()
    longitude = W.inv()*A**-3
    assert (longitude-(A*B)**3*A**-6).applyfunc(sp.factor) == sp.zeros(2)
    return {"marked_longitude_word_checked": True, "intrinsic_M_flag_eigenvalue": str(L_intr),
            "inverse_flag_eigenvalue": "-M^6", "purpose": "Fix inverse, sign, and framing; not a volume theorem."}


def local_action(a, b, c, u, sign):
    """Actual balanced leading potential in log M coordinates, plus gradient."""
    X = mp.exp(2*u)
    A, B, C = mp.exp(a), mp.exp(b), mp.exp(c)
    if sign > 0:
        G = a*b+(a-b)*c-c*c/2-u*(a+b+c)-mp.pi*1j*(a+b)
        gradient = [b+c-u-mp.pi*1j, a-c-u-mp.pi*1j, a-b-c-u, -a-b-c]
        shapes = [B, C, X/A, B*C, X*C/A]
        powers = [(0, 1, 0, 0), (0, 0, 1, 0), (-1, 0, 0, 2),
                  (0, 1, 1, 0), (-1, 0, 1, 2)]
    else:
        G = -a*b+u*(a+b-c)+mp.pi*1j*(a+b-c)
        gradient = [-b+u+mp.pi*1j, -a+u+mp.pi*1j, -u-mp.pi*1j, a+b-c]
        shapes = [A, C, X/B, A*C, X*C/B]
        powers = [(1, 0, 0, 0), (0, 0, 1, 0), (0, -1, 0, 2),
                  (1, 0, 1, 0), (0, -1, 1, 2)]
    eps = [1, 1, 1, -1, -1]
    value = G-mp.pi**2/6
    regulator = mp.mpf(0)
    for z, power, e in zip(shapes, powers, eps):
        li, logarithm = mp.polylog(2, z), mp.log(1-z)
        value += e*li
        regulator += e*(mp.im(li)+mp.log(abs(z))*mp.im(logarithm))
        for i in range(4):
            gradient[i] -= e*power[i]*logarithm
    return value, gradient, regulator


def local_euler_checks():
    mp.mp.dps = 80
    largest = mp.mpf(0)
    for sign in (-1, 1):
        for z in [(mp.mpc("0.3", "0.4"), mp.mpc("-0.2", "0.8"),
                   mp.mpc("0.1", "-0.3"), mp.mpc("0.04", "0.02")),
                  (mp.mpc("-0.7", "0.1"), mp.mpc("0.2", "-0.5"),
                   mp.mpc("0.3", "0.7"), mp.mpc("-0.03", "0.06"))]:
            value, gradient, D = local_action(*z, sign)
            error = abs(mp.im(value)-sum(mp.re(x)*mp.im(y) for x, y in zip(z, gradient))-D)
            largest = max(largest, error)
            assert error < mp.mpf("1e-65")
    return {"both_actual_potentials_checked": True, "maximum_error": float(largest)}


def figure_data(M, frame):
    t = M*M+M**-2
    coefficient = t-3
    # Continue the root with negative imaginary part from M=1.
    r = (-coefficient-mp.sqrt(coefficient**2-4*(3-t)))/2
    if mp.im(r) > 0:
        r = (-coefficient+mp.sqrt(coefficient**2-4*(3-t)))/2
    A = mp.matrix([[M, 1], [0, 1/M]])
    B = mp.matrix([[M, 0], [r, 1/M]])
    C = A**-1*B*A*B**-1*A
    w = mp.matrix([1, 1/M-M])
    v = mp.matrix(frame)
    Q = mp.matrix([[v[0], w[0]-v[0]], [v[1], w[1]-v[1]]])
    meridians = [Q**-1*m*Q for m in (A, B, C)]
    previous, states = mp.eye(2), []
    for mu in meridians:
        G = -previous*mu*previous**-1
        K, e, f = G[0, 0], G[0, 1], G[1, 0]/G[0, 0]
        states.append((K, e, f))
        previous = mp.matrix([[1, 0], [-K*f, K]])*previous
    return meridians, states


def figure_action(M, frame):
    mus, states = figure_data(M, frame)
    initial, initial_mus = list(states), list(mus)
    labels, transports, under_counts = list(range(3)), [mp.eye(2) for _ in range(3)], [0]*3
    x, tau_product, first_shifts = -M, mp.mpc(1), []
    for n, (j, sign) in enumerate(WORDS[0]):
        K, e, f = states[j]
        L, g, h = states[j+1]
        aa, bb = x/K, x/L
        if sign > 0:
            dd = 1-e*h
            C = 1/dd
            tau = bb*C/x*(1-x*x/aa)/(1-x*x*C/aa)
            changed = [(L*dd, (dd*g+e*(dd*L-1/L))/K, K*h/dd),
                       (K/dd, e/(L*dd), L*(dd*f+h*(dd/K-K)))]
            over, under = labels[j], labels[j+1]
            transports[under] = mus[j]**-1*transports[under]
            mus[j:j+2] = [mus[j]**-1*mus[j+1]*mus[j], mus[j]]
        else:
            C = 1-K*g*f/L
            tau = x/aa*(1-x*x/bb)/(1-x*x*C/bb)
            changed = [(L*C, K*g, f+h/K-f/(L*L*C)),
                       (K/C, L*e+g-K*K*g/C, f/L)]
            over, under = labels[j+1], labels[j]
            transports[under] = mus[j+1]*transports[under]
            mus[j:j+2] = [mus[j+1], mus[j+1]*mus[j]*mus[j+1]**-1]
        under_counts[under] += 1
        labels[j:j+2] = [labels[j+1], labels[j]]
        tau_product *= tau
        if n < 2:
            first_shifts.append(C)
        states[j:j+2] = changed
    assert max(abs(a-b) for z, w in zip(states, initial) for a, b in zip(z, w)) < mp.mpf("1e-65")
    following = [labels.index(i) for i in range(3)]
    W, i, seen = mp.eye(2), 0, set()
    while i not in seen:
        seen.add(i)
        W = transports[i]*W
        i = following[i]
    assert len(seen) == 3 and sum(under_counts) == 4
    longitude = W**-1  # writhe is zero for this braid
    if abs(M-1) > mp.mpf("1e-30"):
        projector = (initial_mus[0]-mp.eye(2)/M)/(M-1/M)
        projected = longitude*projector
        eigenvalue = projected[0, 0]+projected[1, 1]
    else:
        eigenvalue = (longitude[0, 0]+longitude[1, 1])/2
    L_intr = 1/tau_product
    assert abs(eigenvalue-L_intr) < mp.mpf("1e-60")

    # Five independent, unwrapped flow variables; the two other shifts
    # follow from exact integer closure, not independent principal logs.
    Z = [mp.log(x/z[0]) for z in initial]+[mp.log(c) for c in first_shifts]+[mp.log(M)]
    I = [[mp.mpf(int(i == j)) for j in range(6)] for i in range(6)]
    add = lambda a, b: [u+v for u, v in zip(a, b)]
    sub = lambda a, b: [u-v for u, v in zip(a, b)]
    shifts = [I[3], I[4], add(sub(I[0], I[2]), I[4]),
              add(sub(sub(I[0], I[1]), I[3]), I[4])]
    positions, value, gradient, D = I[:3], mp.mpc(0), [mp.mpc(0)]*6, mp.mpf(0)
    for n, (j, sign) in enumerate(WORDS[0]):
        maps = [positions[j], positions[j+1], shifts[n], I[5]]
        local = [sum(a*b for a, b in zip(row, Z)) for row in maps]
        val, grad, reg = local_action(*local, sign)
        value += val
        D += reg
        for i in range(6):
            gradient[i] += sum(grad[k]*maps[k][i] for k in range(4))
        aa, bb, cc = maps[:3]
        positions[j:j+2] = [add(bb, cc), sub(aa, cc)] if sign > 0 else [sub(bb, cc), add(aa, cc)]
    assert positions == I[:3]
    # Both pivotal trace and residual zero-framing normalization remain.
    kappa = -2  # w-b+1, with w=0,b=3
    value += 2*mp.pi*1j*(Z[1]+Z[2]+kappa*Z[5])-2*mp.pi**2*kappa
    gradient[1] += 2*mp.pi*1j
    gradient[2] += 2*mp.pi*1j
    gradient[5] += 2*mp.pi*1j*kappa
    integers = [int(mp.nint(mp.im(v)/(2*mp.pi))) for v in gradient[:5]]
    stationary_error = max(abs(v-2*mp.pi*1j*n) for v, n in zip(gradient[:5], integers))
    assert stationary_error < mp.mpf("1e-60")
    flat = value-2*mp.pi*1j*sum(n*z for n, z in zip(integers, Z[:5]))
    v = gradient[5]/2
    assert abs(mp.exp(v)-L_intr) < mp.mpf("1e-60")
    R = flat-Z[5]*v
    B = mp.re(Z[5])*mp.im(v)-mp.re(v)*mp.im(Z[5])
    norm_error = abs(mp.im(R)-B-D)
    assert norm_error < mp.mpf("1e-60")
    if abs(M-1) < mp.mpf("1e-30"):
        expected = 2*mp.im(mp.polylog(2, mp.exp(mp.pi*1j/3)))
        assert abs(mp.im(flat)-expected) < mp.mpf("1e-60")
    return {"M": str(M), "frame": [str(t) for t in frame],
            "longitude": str(L_intr), "winding_integers": integers,
            "stationary_error": float(stationary_error),
            "imaginary_flat_action": str(mp.im(flat)), "Bloch_regulator": str(D),
            "regulator_norm_identity_error": float(norm_error)}


def main():
    mp.mp.dps = 80
    frames = [(mp.mpf(2), mp.mpf(3)), (mp.mpc(1, 1), mp.mpf(2)),
              (mp.mpc("2", "0.3"), mp.mpc("3", "0.1"))]
    records = [figure_action(M, frame) for M in (mp.mpf(1), mp.exp(mp.mpc("0.03", "0.02")))
               for frame in frames]
    result = {"scope": "Exact quantum insertion and marked geometric logarithmic action. No global period-selection or volume-limit theorem.",
              "symbolic_transport": symbolic_transport(),
              "local_quantum_insertions": [local_insertion_check(n) for n in (2, 3, 4, 5, 6, 8, 9, 10, 12, 15)],
              "actual_period_insertions": period_checks(),
              "trefoil_marking": trefoil_marking(),
              "local_logarithmic_identity": local_euler_checks(),
              "geometric_action_calibrations": records}
    Path(__file__).with_name("quantum_longitude_action_results.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"symbolic_transport": result["symbolic_transport"],
                      "local_shift_identities": sum(r["cancelled_local_shift_identities"]
                                                    for n in result["local_quantum_insertions"] for r in n["records"]),
                      "actual_dense_period_comparisons": len(result["actual_period_insertions"]),
                      "trefoil_marking": result["trefoil_marking"],
                      "geometric_action_calibrations": len(records), "all_checks_passed": True}), flush=True)


if __name__ == "__main__":
    main()
