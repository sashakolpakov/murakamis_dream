#!/usr/bin/env python3
"""Exact rational checks for the private four-puncture edge adapter.

This checks matrix and peripheral identities. It does not identify the
abstract puncture words with an original knot diagram or prove gluing.
Requires sympy; has no private-file dependencies.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sympy as sp


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("all_circle_four_punctured_adapter_results.json"),
    )
    args = parser.parse_args()
    records = []

    def check(name, expression):
        value = sp.cancel(expression)
        records.append({"name": name, "passed": value == 0})
        if value != 0:
            raise AssertionError((name, value))

    def mat(entries):
        return sp.Matrix([[sp.cancel(x) for x in row] for row in entries])

    def mul(a, b):
        return sp.Matrix(
            2, 2,
            lambda i, j: sp.cancel(sum(a[i, k] * b[k, j] for k in range(2))),
        )

    def det(a):
        return sp.cancel(a[0, 0] * a[1, 1] - a[0, 1] * a[1, 0])

    def adj(a):
        return mat([[a[1, 1], -a[0, 1]], [-a[1, 0], a[0, 0]]])

    def matrix_check(name, a, b):
        for i in range(2):
            for j in range(2):
                check(f"{name}[{i},{j}]", a[i, j] - b[i, j])

    M, p, q, X, E, beta, gamma, Q, P = sp.symbols(
        "M p q X E beta gamma Q P"
    )
    m = M + 1 / M
    D = M**2 + M**-2
    h = M - 1 / M
    b = p - 2
    c = sp.cancel((M * X + q / M - 2 * m) / (D - p))
    d = sp.cancel((q - M**2 - 1 + h * c) / b)
    e = sp.cancel(X - 1 - M**-2 - h * c)
    A = mat([[M, 1], [0, 1 / M]])
    B = mat([[1 / M, 0], [b, M]])
    C = mat([[c, d], [e, m - c]])
    AB, BC, AC = mul(A, B), mul(B, C), mul(A, C)
    ABC = mul(AB, C)
    for name, value in [
        ("trace A", sp.trace(A) - m),
        ("trace B", sp.trace(B) - m),
        ("trace C", sp.trace(C) - m),
        ("trace AB", sp.trace(AB) - p),
        ("trace BC", sp.trace(BC) - q),
        ("trace AC", sp.trace(AC) - X),
        ("trace ABC", sp.trace(ABC) - m),
    ]:
        check(name, value)
    F = (
        X**2 + p**2 + q**2 + p*q*X
        - 2*m**2*(p+q+X) + 4*m**2 + m**4 - 4
    )
    check("determinant gives character quadratic",
          (det(C) - 1) * (p - 2) * (D - p) - F)
    S = beta + gamma + m**2
    atr = E + 1 / E
    edge = (atr + beta)*(atr + gamma) - (atr-2)*(atr-D)
    check("source to character identity",
          F.subs({p: -beta, q: -gamma, X: 2 + S*E}) - E*S*edge)
    discr = sp.discriminant(F.subs({p: -beta, q: -gamma}), X)
    check("character discriminant",
          discr - (beta+2)*(gamma+2)*(beta*gamma-2*beta-2*gamma-4*D-4))

    # Parametrize the edge variety rationally, avoiding a quadratic root.
    gam = sp.cancel((2*D - atr*(beta+D+2)) / (atr+beta))
    SS = sp.cancel(beta + gam + m**2)
    subst = {p: -beta, q: -gam, X: 2+SS*E}
    B = B.applyfunc(lambda z: sp.cancel(z.subs(subst)))
    C = C.applyfunc(lambda z: sp.cancel(z.subs(subst)))
    AB, BC = mul(A, B), mul(B, C)
    ABC = mul(AB, C)
    D0 = adj(ABC)
    check("det C on edge variety", det(C)-1)
    check("det D0", det(D0)-1)
    check("trace D0", sp.trace(D0)-m)
    matrix_check("four puncture product", mul(ABC, D0), sp.eye(2))

    zv = sp.cancel(-(1+E*(beta+1))/(1-E))
    zw = sp.cancel((E+gam+1)/(1-E))
    V, T = AB+zv*sp.eye(2), BC+zw*sp.eye(2)
    matrix_check("V A = D0 inverse V", mul(V, A), mul(ABC, V))
    matrix_check("V B = C inverse V", mul(V, B), mul(adj(C), V))
    matrix_check("T B = A inverse T", mul(T, B), mul(adj(A), T))
    matrix_check("T C = D0 inverse T", mul(T, C), mul(ABC, T))
    check("V determinant",
          det(V)-(beta+2)*(beta*E+E**2+1)/(E-1)**2)
    check("T determinant",
          det(T)+(E-1)**2*(E-M**2)*(E*M**2-1)
          *(beta*M**2+M**4+1)/(M**4*(beta*E+E**2+1)**2))

    zvQ = -(1+E*(Q+1/Q+1))/(1-E)
    zwP = (E+P+1/P+1)/(1-E)
    check("v selected auxiliary ratio",
          (zvQ-Q)/(zvQ-1/Q)-(Q+E)/(1+Q*E))
    check("w oppositely oriented selected ratio",
          (zwP-1/P)/(zwP-P)-(P+E)/(1+P*E))

    u = sp.cancel((M**2-E)/(1-M**2*E))
    Winv = mat([[-1/u, (u-1/u)/h], [0, -u]])
    # This is a direct polynomial matrix certificate for the commutator.
    matrix_check("main commutator certificate",
                 mul(T, V), mul(mul(V, Winv), T))
    Lambda = mat([[-u, (1/u-u)/h], [0, -1/u]])
    check("main determinant", det(Lambda)-1)
    matrix_check("main commutes with puncture", mul(Lambda, A), mul(A, Lambda))
    check("main source-flag eigenvalue",
          (Lambda*sp.Matrix([1, -h]))[0] + 1/u)
    check("complete main upper right",
          sp.limit(Lambda[0, 1], M, 1) + 2*(1+E)/(1-E))

    # The actual native complete chart fixes the character branch.
    I = sp.I
    whites = [
        sp.diag(-I, 1),
        mat([[-I, 1+I], [0, 1]]),
        mat([[2+I, -1-I], [2+2*I, -1-2*I]]),
        mat([[-I, 0], [-2-2*I, 1]]),
    ]
    inv = lambda Z: adj(Z)/det(Z)
    An = mul(inv(whites[2]), whites[3])
    Cn = mul(inv(whites[0]), whites[1])
    check("native complete source branch", sp.trace(mul(An, Cn))-(2+8*I))

    # Independent exact fixed-white odd obstruction, on Q=P=1.
    mm = M**2
    Ee = I/M
    L = 1/Ee
    R, SS = 1/(1+M**2), M**2/(1+M**2)
    av, am = I/(M+I), M/(M+I)
    l1, l2, l3 = L/mm, L/mm**2, L*mm
    c2 = sp.cancel((l2*(R-1)/(SS-1)-1)/(R-1))
    c3 = sp.cancel((l3*R/SS-1)/R)
    whites = [
        mat([[L, 0], [0, 1]]),
        mat([[l1, 1-l1], [0, 1]]),
        mat([[c2+l2, 1-c2-l2], [c2, 1-c2]]),
        mat([[l3, 0], [c3, 1]]),
    ]
    Ao = mat([[SS, -SS], [1, SS*(av-1)/am-av]])
    Bo = mat([[(am*(av-R)+R)/av, -R], [1, -R]])
    Rodd = mul(mul(mul(adj(whites[0]), Bo), adj(whites[2])), Ao)
    Rodd = Rodd/Rodd[1, 1]
    target = mat([[M**-4, I*(M**2-1)*(M-I)/M**4], [0, 1]])
    matrix_check("fixed-white odd return defect", Rodd, target)
    Rthird = mul(mul(mul(adj(whites[1]), Bo), adj(whites[3])), Ao)
    matrix_check("third odd return remains identity",
                 Rthird/Rthird[1, 1], sp.eye(2))

    # Full vector-tensor identities, with the eigenvalue hypothesis visible.
    lam, alpha, bet = sp.symbols("lam alpha bet")
    AA = mat([[lam, alpha], [0, 1/lam]])
    BB = mat([[1/lam, 0], [bet, lam]])
    HH = mul(AA, BB)-sp.eye(2)
    KK = inv(mul(BB, AA))-sp.eye(2)
    avec, bvec = sp.Matrix([1, 0]), sp.Matrix([0, 1])
    tensor = lambda a, b: sp.kronecker_product(a, b)
    kt = tensor(KK*avec, KK*bvec)/det(KK)
    ht = tensor(HH*avec, HH*bvec)/det(HH)
    expected_k = -tensor(inv(AA)*bvec, avec)/lam
    expected_h = -lam*tensor(AA*bvec, avec)
    for j in range(4):
        check(f"equal-line inverse-collar tensor {j}", kt[j]-expected_k[j])
        check(f"equal-line forward-collar tensor {j}", ht[j]-expected_h[j])
    BBopp = mat([[lam, 0], [bet, 1/lam]])
    Kopp = inv(mul(BBopp, AA))-sp.eye(2)
    check("opposite-line second coordinate", (Kopp*bvec)[1]-(lam**2-1))

    result = {
        "scope": "Exact rational matrix identities, native complete branch, fixed-white odd-return obstruction and decorated-line algebra; no global topological marking or geometric conclusion.",
        "arithmetic": "symbolic rational functions over Q(M,beta,E), with independent trace variables for the initial determinant identity",
        "checks": records,
        "count": len(records),
        "all_passed": all(r["passed"] for r in records),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"count": result["count"], "all_passed": result["all_passed"],
                      "output": str(args.output)}, indent=2))


if __name__ == "__main__":
    main()
