#!/usr/bin/env python3
"""Positive quad charts and an exact original geometric torus signature."""

import itertools
import json
import random
from pathlib import Path

import sympy as S

from audit_actual_normal_stationary_period import closure_embedding, inverse, matmul


def rotated(A, B, choices):
    AA, BB = A.copy(), B.copy()
    for j, choose in enumerate(choices):
        if choose:
            AA[:, j], BB[:, j] = B[:, j]-A[:, j], -A[:, j]
    return AA, BB


def quad_transversals():
    rng = random.Random(2601028)
    count = singular = 0
    for n in range(1, 7):
        for sample in range(8):
            raw = S.Matrix(n, n, lambda i, j: rng.randrange(-2, 3))
            A, B = raw+raw.T, S.eye(n)
            # The first case forces B=0; the remaining cases vary all quad types.
            if sample == 0:
                A, B = S.eye(n), S.zeros(n)
            else:
                for j in range(n):
                    for _ in range(rng.randrange(3)):
                        choices = [int(k == j) for k in range(n)]
                        A, B = rotated(A, B, choices)
            assert A*B.T == B*A.T
            shapes = [S.Rational(j+1, j+2)+S.I*S.Rational(j+2, j+3) for j in range(n)]
            tau = S.diag(*[1/(z-1) for z in shapes])
            assert S.simplify((A+B*tau).det()) != 0
            singular += int(B.det() == 0)
            candidates = []
            for choices in itertools.product((0, 1), repeat=n):
                AA, BB = rotated(A, B, choices)
                if BB.det():
                    assert AA*BB.T == BB*AA.T
                    C = BB.inv()*AA
                    assert C == C.T
                    candidates.append(choices)
                    for j, choose in enumerate(choices):
                        if choose:
                            assert S.im(1-1/shapes[j]) > 0
                    break
            assert candidates
            count += 1
    return {"exact_cases": count, "initially_singular_B": singular}


def calibration_identity():
    for n in range(1, 5):
        rho = S.Matrix(S.symbols(f"r0:{n}", real=True))
        theta = S.Matrix(S.symbols(f"t0:{n}", real=True))
        sigma = S.Matrix(S.symbols(f"s0:{n}", real=True))
        gamma = S.Matrix(S.symbols(f"g0:{n}", real=True))
        C = S.Matrix(n, n, lambda i, j: S.Symbol(f"c{min(i,j)}_{max(i,j)}", real=True))
        x, y = rho+S.I*theta, sigma+S.I*gamma
        # Retain pi exactly; no numerical branch calibration.
        polynomial = (x.T*(S.eye(n)-C)*x)[0]/2+((C*x+y-S.I*S.pi*S.ones(n, 1)).T*x)[0]
        bloch_correction = (rho.T*(theta+gamma-S.pi*S.ones(n, 1)))[0]
        residual = S.expand(S.im(polynomial)-bloch_correction-(theta.T*(C*rho+sigma))[0])
        assert residual == 0
    return {"exact_dimensions": 4, "full_boundary_correction": True}


def actual_figure_eight_hessian():
    field = S.QQ.algebraic_field(S.sqrt(-3))
    zero, one = field.zero, field.one
    root = (one-field.convert(S.sqrt(-3)))/2
    mu1 = (one, one, zero, one)
    mu2 = (one, zero, root, one)
    mu3 = matmul(matmul(matmul(matmul(inverse(mu1), mu2), mu1), inverse(mu2)), mu1)
    frame = (field(2), field(-1), field(3), field(-3))
    previous, states = (one, zero, zero, one), []
    for mu in (mu1, mu2, mu3):
        H = tuple(-v for v in matmul(matmul(inverse(frame), mu), frame))
        H = matmul(matmul(previous, H), inverse(previous))
        k, e, f = H[0], H[1], H[2]/H[0]
        states.append((k, e, f))
        previous = matmul((one, zero, -k*f, k), previous)
    initial = list(states)
    word = [(0, 1), (1, -1), (0, 1), (1, -1)]
    maps = closure_embedding(3, word)
    total = [[zero for _ in range(5)] for _ in range(5)]
    for step, (slot, sign) in enumerate(word):
        k, e, f = states[slot]
        l, g, h = states[slot+1]
        a, b = -one/k, -one/l
        c = one/(one-e*h) if sign > 0 else one-k*g*f/l
        if sign > 0:
            constants = [[0, 1, 1], [1, 0, -1], [1, -1, -1]]
            shapes = [b, c, one/a, b*c, c/a]
            vectors = [(0,1,0), (0,0,1), (-1,0,0), (0,1,1), (-1,0,1)]
        else:
            constants = [[0,-1,0], [-1,0,0], [0,0,0]]
            shapes = [a, c, one/b, a*c, c/b]
            vectors = [(1,0,0), (0,0,1), (0,-1,0), (1,0,1), (0,-1,1)]
        assert all(z and z != one for z in shapes)
        local = [[field(v) for v in row] for row in constants]
        for z, vector, epsilon in zip(shapes, vectors, (1,1,1,-1,-1)):
            coefficient = epsilon*z/(one-z)
            for i, j in itertools.product(range(3), repeat=2):
                local[i][j] += coefficient*vector[i]*vector[j]
        for i, j in itertools.product(range(5), repeat=2):
            total[i][j] += sum((local[u][v]*int(maps[step][u,i])*int(maps[step][v,j])
                               for u, v in itertools.product(range(3), repeat=2)), zero)
        if sign > 0:
            d = one-e*h
            new = [(l*d, (d*g+e*(d*l-one/l))/k, k*h/d),
                   (k/d, e/(l*d), l*(d*f+h*(d/k-k)))]
        else:
            d = one-k*g*f/l
            new = [(l*d, k*g, f+h/k-f/(l*l*d)),
                   (k/d, l*e+g-k*k*g/d, f/l)]
        states[slot:slot+2] = new
    assert states == initial
    normal = S.Matrix([[field.to_sympy(total[i][j]) for j in range(2,5)] for i in range(2,5)])
    assert S.simplify(normal.det()) != 0
    angular = S.simplify(-S.im(normal)/S.sqrt(3))
    expected = S.Matrix([[-S.Rational(832683,405769), S.Rational(1,52), -S.Rational(21,8)],
                         [S.Rational(1,52), -S.Rational(9,8), S.Rational(3,8)],
                         [-S.Rational(21,8), S.Rational(3,8), S.Rational(9,32)]])
    assert angular == expected
    assert angular[1,1] < 0 < angular[2,2]
    # Independently differentiate the original two framing coordinates.
    r, s = S.symbols("r s", nonzero=True)
    t = (1-S.sqrt(-3))/2
    F = S.Matrix([[r,1-r], [s,-s]])
    A, B = S.Matrix([[1,1],[0,1]]), S.Matrix([[1,0],[t,1]])
    H = -F.inv()*A*F
    k, e, f = H[0,0], H[0,1], H[1,0]/H[0,0]
    P = S.Matrix([[1,0],[-k*f,k]])
    HH = P*(-F.inv()*B*F)*P.inv()
    h = HH[1,0]/HH[0,0]
    free = [-1/k, 1/(1-e*h)]
    jac = S.Matrix([[S.simplify((S.diff(z,v)/z).subs({r:2,s:3})) for v in (r,s)] for z in free])
    det = S.simplify(jac.det())
    expected_det = 15*(-11*S.sqrt(3)-S.I)/(4*(155*S.sqrt(3)+283*S.I))
    assert S.simplify(det-expected_det) == 0 and det != 0
    return {"exact_field": "Q(sqrt(-3))", "valid_original_framing_slice": True,
            "angular_Hessian_divided_by_sqrt3": [[str(v) for v in row] for row in angular.tolist()],
            "opposite_sign_diagonal_entries": [str(angular[1,1]), str(angular[2,2])],
            "geometric_fixed_radii_torus_not_local_maximum": True}


def main():
    result = {"status": "PASS", "positive_quad_selection": quad_transversals(),
              "calibration": calibration_identity(), "actual_phase_counter": actual_figure_eight_hessian(),
              "scope": "All-positive-triangulation classical proof and original phase signature; no quantum cycle comparison."}
    Path(__file__).with_name("positive_quad_chart_and_actual_torus_signature_results.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
