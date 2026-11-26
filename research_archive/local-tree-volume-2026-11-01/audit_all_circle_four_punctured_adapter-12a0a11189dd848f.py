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

    result = {
        "scope": "Exact rational matrix identities on the regular edge chart; no topological marking or global geometric conclusion.",
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
