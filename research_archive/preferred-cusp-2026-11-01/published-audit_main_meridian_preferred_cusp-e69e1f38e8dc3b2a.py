"""Exact local identities for the Conway preferred-cusp formula.

These finite rational identities do not replace the global face-pairing,
peripheral-path, homology, or hyperbolic-completion arguments in the note.
Requires SymPy; no private files or network access are used.
"""
import argparse
import json
from pathlib import Path
import itertools
import sympy as sp


def run_geometry_checks():
    E, R = sp.symbols("E R", nonzero=True)
    a, b, c = sp.symbols("a b c", nonzero=True)
    checks = []

    def equal(name, left, right):
        if isinstance(left, sp.MatrixBase):
            assert all(sp.cancel(t) == 0 for t in left-right), name
        else:
            assert sp.cancel(left-right) == 0, name
        checks.append(name)

    def projective(name, left, right):
        flat_left, flat_right = list(left), list(right)
        i = next(i for i, x in enumerate(flat_right) if x != 0)
        equal(name, left*flat_right[i], right*flat_left[i])

    def frames(E, R):
        return [
            sp.Matrix([[0, E*R], [E-1, 0]]),
            sp.Matrix([[-1, 0], [0, E-1]]),
            sp.Matrix([[0, -E*(R-1)], [E-1, -(E-1)]]),
            sp.Matrix([[0, -R*(R-1)], [E-1, -R*(E-1)]]),
        ]

    def white(E, R):
        return [
            sp.Matrix([[1, 0], [0, E]]),
            sp.Matrix([[1, E-1], [0, E]]),
            sp.Matrix([[E-R, R*(1-E)], [E-1, 1-E*R]]),
            sp.Matrix([[R, 0], [1-E, E*R]]),
        ]

    def affine(name, matrix, slope, shift):
        projective(name, matrix, sp.Matrix([[slope, shift], [0, 1]]))

    X, W = frames(E, R), white(E, R)
    S = sp.Matrix([[0, -E*R], [1, -1-E]])
    A = sp.Matrix([[R, -R], [1, E*R-1-E]])
    B = sp.Matrix([[R/E-1-1/E, R], [-1, R]])
    mu = [(W[(j-1) % 4].inv()*W[j])**((-1)**j) for j in range(4)]
    for j in range(4):
        affine(f"meridian_{j}", X[j]*mu[j]*X[j].inv(), 1, 1)

    bp02, bp13 = E/(E-1), (R-E-1)/(E-1)
    bm02, bm13 = 1/(E-1), (R-2)/(E-1)
    for name, word, j, k, shift in [
        ("positive02", W[1].inv()*B, 0, 2, bp02),
        ("positive13", W[2].inv()*A, 1, 3, bp13),
        ("negative02", W[2].inv()*B, 0, 2, bm02),
        ("negative13", W[3].inv()*A, 1, 3, bm13),
    ]:
        affine(name, X[k]*word*X[j].inv(), -1, shift)
    Mp, Mm = W[0].inv()*B, A.inv()*W[0]
    projective("positive_H1_word02", W[1].inv()*B, mu[1]*Mp)
    projective("positive_H1_word13", W[2].inv()*A, Mp.inv())
    projective("negative_H1_word02", W[2].inv()*B, Mm)
    projective("negative_H1_word13", W[3].inv()*A, mu[0]*Mm.inv())

    # Concatenation, including arbitrary signs and reverse traversal.
    bx, bj, by = sp.symbols("bx bj by")
    for di, dj, dk, dl in itertools.product([-1, 1], repeat=4):
        ax, aj, ay = -di*dj, -dj*dk, -dk*dl
        shift = ay*aj*bx+ay*bj+by
        equal(f"chain_{di}_{dj}_{dk}_{dl}",
              -dl*shift, -dj*bx+dk*bj-dl*by)
        equal(f"reverse_arc_{di}_{dj}_{dk}_{dl}",
              -di*(-bx/ax), -dj*bx)

    def norm(q):
        q0, q1, q2, q3 = q
        if q0 == sp.oo:
            M = sp.Matrix([[0, q2-q1], [1, -q1]])
        elif q1 == sp.oo:
            M = sp.Matrix([[1, -q0], [0, q2-q0]])
        elif q2 == sp.oo:
            M = sp.Matrix([[1, -q0], [1, -q1]])
        else:
            M = sp.Matrix([[q2-q1, -q0*(q2-q1)],
                           [q2-q0, -q1*(q2-q0)]])
        Rq = (M[0, 0]/M[1, 0] if q3 == sp.oo else
              (M[0, 0]*q3+M[0, 1])/(M[1, 0]*q3+M[1, 1]))
        return M, sp.factor(Rq)

    def world_frames(q, E):
        M, Rq = norm(q)
        return [F*M for F in frames(E, Rq)], Rq

    Pstar = 1+a-a*(a*b*(1+c)-1-a)/(a*a*b*b*c-a)
    F, RF = world_frames([1, a, Pstar, sp.oo], b*c)
    G, RG = world_frames([sp.oo, Pstar, a*b, a*b*c], a*b)
    O, RO = world_frames([1, a, a*b, a*b*c], a*b*c)
    betas = [
        b*c/(b*c-1),
        -a*(b-1)/((a*b-1)*(a*b*c-1)),
        0, 0,
        a*b*(c-1)/((a*b-1)*(a*b*c-1)),
        (b-1)*(c-1)/((a*b-1)*(b*c-1)*(a*b*c-1)),
    ]
    for name, target, source, beta in zip(
        ["join21", "join30", "externalF0", "externalF1", "externalG2", "externalG3"],
        [G[1], G[0], O[0], O[1], O[2], O[3]],
        [F[2], F[3], F[0], F[1], G[2], G[3]], betas):
        affine(name, target*source.inv(), 1, beta)
    potential = lambda E, R: (E+R)/(E-1)
    correction = -betas[0]+betas[1]-betas[2]+betas[3]-betas[4]+betas[5]
    equal("product_potential", correction,
          potential(a*b*c, RO)-potential(b*c, RF)-potential(a*b, RG))

    T = sp.Matrix([[0, R-1], [1, -1]])
    turn_shifts = [E*R/(E-1), -1/(E-1), 0, R/(E-1)]
    turn_correction = 0
    for j, beta in enumerate(turn_shifts):
        k = (j-1) % 4
        affine(f"turn_corner{j}",
               frames(1/E, 1-R)[k]*T*X[j].inv(), -1, beta)
        turn_correction -= (-1)**k*beta
    equal("turn_potential", turn_correction-potential(1/E, 1-R)+potential(E, R),
          2*(E+1)/(E-1))
    C = sp.Matrix([[1, -R], [1, -1]])
    root_shifts = [R/(E-1), -E/(E-1), -1/(E-1), E*R/(E-1)]
    root_correction = 0
    for j, beta in enumerate(root_shifts):
        k = 3-j
        affine(f"root_corner{j}", X[k]*C*frames(1/E, R)[j].inv(), 1, beta)
        root_correction += (-1)**k*beta
    equal("root_potential", root_correction+potential(E, R)+potential(1/E, R), 0)
    pure = (R-E-2)/(E-1)
    equal("positive_leaf_integer", bp13-bp02-pure, -1)
    equal("negative_leaf_integer", bm13-bm02-pure, 1)

    p = sp.symbols("p", integer=True)
    for eps in [-1, 0, 1]:
        for t0, t1 in itertools.product([-1, 1], repeat=2):
            oriented = -t0*t1
            linking = t0-t1
            n = eps-2*p
            equal(f"filling_integer_{eps}_{t0}_{t1}",
                  -eps-oriented*eps+p*linking**2, -n-oriented*n)

    report = {"method": "exact rational identities and finite orientation cases",
              "checks": checks, "count": len(checks),
              "scope": "local algebra; actual peripheral path and homology interpretation are in the proof"}
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("main_meridian_preferred_cusp_results.json"))
    args = parser.parse_args()
    report = run_geometry_checks()
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"checks": report["count"], "output": str(args.output)}))


if __name__ == "__main__":
    main()
