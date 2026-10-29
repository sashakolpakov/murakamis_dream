#!/usr/bin/env python3
"""Audit the principal-root color bound and the regularized ADO period.

Compares a positive path trace with the actual highest-weight cut,
then checks the polar subtraction on exact actual Laurent cut states.
No geometric asymptotic or volume-conjecture assertion is made.
"""

from functools import cache
from itertools import product
import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_finite_sum_annihilator import field, cut_matrix_dense
from audit_kashaev_ado_pointing import color_matrices
from audit_adequacy_algebraic_periods import cable


DIAGRAMS = ((2, [(0, 1)]*3),
            (3, [(0, 1), (1, -1)]*2),
            (3, [(0, 1)]*3+[(1, 1)]))


def path_model(level, length):
    theta = np.pi/level
    mu = np.sin(np.arange(1, level)*theta)/np.sin(theta)
    paths = [(0,)]
    for _ in range(length):
        paths = [p+(a,) for p in paths for a in (p[-1]-1, p[-1]+1)
                 if 0 <= a <= level-2]
    indices = {p: j for j, p in enumerate(paths)}
    size = len(paths)
    generators = {}
    for i in range(1, length):
        U = np.zeros((size, size), dtype=np.complex128)
        for column, p in enumerate(paths):
            if p[i-1] != p[i+1]:
                continue
            for middle in (p[i-1]-1, p[i-1]+1):
                if 0 <= middle <= level-2:
                    following = p[:i]+(middle,)+p[i+1:]
                    U[indices[following], column] = np.sqrt(mu[p[i]]*mu[middle])/mu[p[i-1]]
        generators[i] = U
    return paths, np.array([mu[p[-1]] for p in paths]), generators


def path_period(level, color, strands, word):
    if color == 1:
        return 1.0+0.0j, {"path_dimension": 1, "projector_trace": 1.0}
    n = color-1
    length = strands*n
    paths, weights, U = path_model(level, length)
    size = len(paths)
    eye = np.eye(size, dtype=np.complex128)
    q = np.exp(1j*np.pi/level)
    delta = q+1/q
    for i, e in U.items():
        assert np.max(abs(e-e.conj().T)) < 1e-12
        assert np.max(abs(e@e-delta*e)) < 1e-11
        if i+1 in U:
            assert np.max(abs(e@U[i+1]@e-e)) < 1e-11
    P = eye.copy()
    for block in range(strands):
        block_projector = eye.copy()
        for r in range(1, n):
            ratio = np.sin(r*np.pi/level)/np.sin((r+1)*np.pi/level)
            block_projector -= ratio*(block_projector@U[block*n+r]@block_projector)
        P = P@block_projector
    assert np.max(abs(P-P.conj().T)) < 1e-11
    assert np.max(abs(P@P-P)) < 1e-10
    dimension = np.sin(color*np.pi/level)/np.sin(np.pi/level)
    trace_P = np.dot(weights, np.diag(P))
    assert abs(trace_P-dimension**strands) < 2e-9
    elementary = {i: np.exp(1j*np.pi/(2*level))*eye
                  -np.exp(-1j*np.pi/(2*level))*e for i, e in U.items()}
    for value in elementary.values():
        assert np.max(abs(value.conj().T@value-eye)) < 1e-11
    cabled = cable([(i+1)*s for i, s in word], n)
    B = eye.copy()
    for crossing in cabled:
        element = elementary[abs(crossing)]
        B = B@(element if crossing > 0 else element.conj().T)
    assert np.max(abs(B@P-P@B)) < 2e-10
    writhe = sum(sign for _, sign in word)
    value = (np.dot(weights, np.diag(P@B@P))/dimension
             *np.exp(-1j*np.pi*writhe*n*(n+2)/(2*level)))
    return value, {"path_dimension": size, "projector_trace": float(trace_P.real)}


@cache
def crossing_entries(dimension, level, color, kind):
    """Actual finite R entries, with the common Cartan scalar removed."""
    q = mp.exp(mp.pi*mp.j/level)
    x = q**(color-1)
    rho = q-1/q
    integer = [mp.mpf(0)]+[(q**j-q**(-j))/rho for j in range(1, dimension)]
    factorial = [mp.mpf(1)]
    for j in range(1, dimension):
        factorial.append(factorial[-1]*integer[j])
    evalues = [mp.mpf(0)]+[integer[a]*(x*q**(1-a)-q**(a-1)/x)/rho
                                   for a in range(1, dimension)]
    result = {}
    for sign in (-1, 1):
        for a, b in product(range(dimension), repeat=2):
            start = a if sign > 0 else b
            maximum = min(a, dimension-1-b) if sign > 0 else min(b, dimension-1-a)
            ec = mp.mpf(1)
            transitions = []
            for k in range(maximum+1):
                if k:
                    ec *= evalues[start-k+1]
                scalar = rho**k/factorial[k]
                if sign > 0:
                    c, d = a-k, b+k
                    scalar *= q**(k*(k-1)//2)*ec*x**(-c-d)*q**(2*c*d)
                    output = (d, c)
                else:
                    scalar *= (-1)**k*q**(-k*(k-1)//2)*ec*x**(a+b)*q**(-2*a*b)
                    output = (b-k, a+k)
                if abs(scalar) > mp.mpf("1e-65"):
                    transitions.append((output, scalar))
            result[sign, a, b] = transitions
    if kind == "ordinary":
        pivotal = [x*q**(-2*a) for a in range(dimension)]
        twist = x
    else:
        pivotal = [x**(1-dimension)*q**(2*a*(dimension-1)) for a in range(dimension)]
        twist = x**(1-dimension)
    return result, pivotal, twist


def actual_period(level, color, strands, word, ado=False):
    dimension = level if ado else color
    entries, pivotal, twist = crossing_entries(dimension, level, color,
                                               "ado" if ado else "ordinary")
    total = mp.mpc(0)
    for closed in product(range(dimension), repeat=strands-1):
        initial = (0,)+closed
        paths = {initial: mp.fprod(pivotal[a] for a in closed)}
        for position, sign in reversed(word):
            following = {}
            for state, old in paths.items():
                a, b = state[position:position+2]
                for output, scalar in entries[sign, a, b]:
                    new_state = state[:position]+output+state[position+2:]
                    following[new_state] = following.get(new_state, 0)+old*scalar
            paths = following
        total += paths.get(initial, 0)
    return total*twist**(-sum(s for _, s in word))


def positive_trace_checks():
    mp.mp.dps = 80
    records = []
    for level, color in ((3, 2), (4, 2), (4, 3), (5, 2), (5, 3),
                         (5, 4), (6, 2), (6, 3), (7, 3), (8, 3)):
        for strands, word in DIAGRAMS:
            path_value, report = path_period(level, color, strands, word)
            actual = actual_period(level, color, strands, word)
            assert abs(path_value-complex(actual)) < 3e-8
            bound = (mp.sin(color*mp.pi/level)/mp.sin(mp.pi/level))**(strands-1)
            assert abs(actual) <= bound+mp.mpf("1e-60")
            records.append({"level": level, "color": color, "strands": strands,
                            "crossings": len(word), **report,
                            "actual_cut_equals_positive_trace": True,
                            "quantum_dimension_bound": True})
    uniform = []
    for level in (2, 3, 4, 5, 6, 8, 10):
        for color in range(1, level):
            for strands, word in DIAGRAMS[:2]:
                value = actual_period(level, color, strands, word)
                bound = (mp.sin(color*mp.pi/level)/mp.sin(mp.pi/level))**(strands-1)
                assert abs(value) <= bound+mp.mpf("1e-55")
                if level <= 6:
                    ado = actual_period(level, color, strands, word, ado=True)
                    assert abs(ado-value) < mp.mpf("1e-55")
                uniform.append({"level": level, "color": color, "strands": strands,
                                "absolute_value": mp.nstr(abs(value), 18),
                                "bound": mp.nstr(bound, 18)})
    return records, uniform


def add_poly(destination, source, modulus, shift=0, multiplier=1):
    for exponent, coefficient in source.items():
        key = exponent+shift
        destination[key] = (destination.get(key, 0)+multiplier*coefficient) % modulus
        if not destination[key]:
            del destination[key]


def multiply_poly(a, b, modulus):
    result = {}
    for exponent, coefficient in a.items():
        add_poly(result, b, modulus, exponent, coefficient)
    return result


def evaluate(polynomial, point, modulus, derivative=False):
    if derivative:
        return sum(c*e*pow(point, e-1, modulus) for e, c in polynomial.items()) % modulus
    return sum(c*pow(point, e, modulus) for e, c in polynomial.items()) % modulus


def actual_laurent_period(level, prime, q, strands, word):
    Q = q*q % prime
    factorial = [1]
    for j in range(1, level):
        factorial.append(factorial[-1]*(1-pow(Q, j, prime)) % prime)
    entries = {}
    for sign in (-1, 1):
        for a, b in product(range(level), repeat=2):
            start = a if sign > 0 else b
            maximum = min(a, level-1-b) if sign > 0 else min(b, level-1-a)
            transitions = []
            for k in range(maximum+1):
                gaussian = factorial[start]*pow(factorial[k]*factorial[start-k] % prime, -1, prime) % prime
                poch = {0: 1}
                for r in range(k):
                    poch = multiply_poly(poch, {0: 1, 2: -pow(Q, 1-start+r, prime)}, prime)
                if sign > 0:
                    exponent = -a-b-k
                    scalar = (-1)**k*pow(Q, a*b+(a-b)*k-k*(k+1)//2, prime)*gaussian % prime
                    output = (b+k, a-k)
                else:
                    exponent = a+b-k
                    scalar = pow(Q, -a*b, prime)*gaussian % prime
                    output = (b-k, a+k)
                local = {}
                add_poly(local, poch, prime, exponent, scalar)
                transitions.append((output, local))
            entries[sign, a, b] = transitions
    writhe = sum(s for _, s in word)
    global_power = (level-1)*(writhe-strands+1)
    result = {}
    for closed in product(range(level), repeat=strands-1):
        initial = (0,)+closed
        paths = {initial: {global_power: pow(Q, (level-1)*sum(closed), prime)}}
        for position, sign in reversed(word):
            following = {}
            for state, old in paths.items():
                a, b = state[position:position+2]
                for output, local in entries[sign, a, b]:
                    new_state = state[:position]+output+state[position+2:]
                    add_poly(following.setdefault(new_state, {}), multiply_poly(old, local, prime), prime)
            paths = following
        add_poly(result, paths.get(initial, {}), prime)
    assert all(exponent % 2 == 0 for exponent in result)
    return {e//2: c*pow(Q, -e//2, prime) % prime for e, c in result.items()}


def exact_polar_checks(level, strands, word):
    prime, generator, q = field(level)
    Q = q*q % prime
    F = actual_laurent_period(level, prime, q, strands, word)
    M = generator
    x = -pow(q, -1, prime)*M % prime
    cut = cut_matrix_dense(level, prime, color_matrices(level, prime, q, x), strands, word)
    assert evaluate(F, M*M % prime, prime) == int(cut[0, 0])
    colors = {}
    P = {}
    inv_N = pow(level, -1, prime)
    for j in range(1, level):
        z = pow(Q, j, prime)
        value = evaluate(F, z, prime)
        color_x = pow(q, j-1, prime)
        positive, negative, _, _ = color_matrices(j, prime, q, color_x)
        pivotal = np.diag([color_x*pow(q, -2*a, prime) % prime for a in range(j)]).astype(np.int64)
        ordinary = cut_matrix_dense(j, prime, (positive, negative, pivotal, color_x), strands, word)
        assert value == int(ordinary[0, 0])
        colors[j] = value
        for r in range(level-1):
            add_poly(P, {r: (pow(z, -r, prime)-z)*value*inv_N}, prime)
    difference = F.copy()
    add_poly(difference, P, prime, multiplier=-1)
    low = min([0]+list(difference))
    dividend = {e-low: c for e, c in difference.items()}
    quotient = {}
    while dividend and max(dividend) >= level-1:
        exponent = max(dividend)-(level-1)
        scalar = dividend[max(dividend)]
        add_poly(quotient, {exponent+low: scalar}, prime)
        add_poly(dividend, {r: 1 for r in range(level)}, prime, exponent, -scalar)
    assert not dividend
    R = quotient
    assert evaluate(F, 1, prime) == (evaluate(P, 1, prime)+level*evaluate(R, 1, prime)) % prime
    fourier = sum(pow(Q, j, prime)*evaluate(F, pow(Q, j, prime), prime)
                  for j in range(level))*inv_N % prime
    assert fourier == evaluate(R, 1, prime)
    for j, color_value in colors.items():
        z = pow(Q, j, prime)
        derivative_S = level*pow(z, -1, prime)*pow(z-1, -1, prime) % prime
        expected_R = (evaluate(F, z, prime, True)-evaluate(P, z, prime, True))*pow(derivative_S, -1, prime) % prime
        assert evaluate(R, z, prime) == expected_R
    y = generator
    S_y = sum(pow(y, r, prime) for r in range(level)) % prime
    polar = sum(colors[j]*pow(pow(Q, j, prime)-1, 1, prime)*pow(Q, j, prime)*inv_N
                *pow(y-pow(Q, j, prime), -1, prime) for j in colors) % prime
    assert evaluate(P, y, prime)*pow(S_y, -1, prime) % prime == polar
    return {"level": level, "strands": strands, "crossings": len(word),
            "Laurent_support": [min(F), max(F)],
            "actual_dense_cut_and_all_ordinary_colors_match": True,
            "exact_polar_division_and_wall_jets": True,
            "weighted_cyclic_trace_equals_regular_period": True}


def main():
    path, bounds = positive_trace_checks()
    print(json.dumps({"positive_path_comparisons": len(path), "uniform_color_bounds": len(bounds)}), flush=True)
    polar = [exact_polar_checks(n, b, word) for n in (2, 3, 4, 5, 6)
             for b, word in DIAGRAMS[:2]]
    result = {"scope": "Exact source regularization and polynomial polar bounds; no geometric volume theorem.",
              "positive_path_trace_comparisons": path, "uniform_color_bounds": bounds,
              "actual_Laurent_polar_decompositions": polar}
    Path(__file__).with_name("regularized_kashaev_period_results.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"polar_decompositions": len(polar), "all_checks_passed": True}), flush=True)


if __name__ == "__main__":
    main()
