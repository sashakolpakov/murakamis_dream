#!/usr/bin/env python3
"""Compare the primitive cap lift with original full crossing matrices.

Finite precision diagnostics only. The accompanying research note proves
the identities for every level, including both endpoint parities.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_twist_period_insertion import original_matrices
from check_current_free_aw_crossing_transport import newton_multiplication
from check_rational_word_normalized_cofactor import finite_determinant, submatrix


def error(a, b):
    return mp.norm(a-b)/max(mp.mpf(1), mp.norm(a), mp.norm(b))


def adjugate(a):
    n = a.rows
    out = mp.matrix(n)
    for i in range(n):
        for j in range(n):
            rows = [k for k in range(n) if k != j]
            cols = [k for k in range(n) if k != i]
            out[i, j] = (-1)**(i+j)*finite_determinant(submatrix(a, rows, cols))
    return out


def update(letter, x, k, b, q):
    identity = mp.eye(x.rows)
    if letter == "J":
        return q**-2*x**-1, b, k
    if letter == "+":
        return (-q**-1*k**-1,
                (identity-x)*k-q**-1*identity,
                -q**-2*x**-1*b-q**-1*(identity+x**-1))
    if letter == "-":
        a = x+q**-1*x*k+q**-2*identity
        return a, -q**-1*x**-1, -q**2*a*b-q*(a+identity)
    raise ValueError(letter)


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    words = ["", "+", "-", "J", "J++", "-----J----",
             "J--J---", "--J+++J-"]
    records = []
    for level in range(2, 11):
        top = level-1
        q = mp.exp(mp.pi*1j/level)
        qq = q*q
        eta = (-1)**top
        kappa = q**(mp.mpf(top*top)/2)
        identity = mp.eye(level)
        first, last = identity[:, 0], identity[:, top]
        m, _, _ = original_matrices(level)
        mi = m**-1
        z = newton_multiplication(level)
        ell = z.T
        c0 = q+q**-1
        jmat = mp.matrix(level)
        shift = mp.matrix(level)
        for j in range(level):
            jmat[j, top-j] = 1
            shift[(j+1) % level, j] = 1
        x = mp.diag([qq**j for j in range(level)])
        k = -q**-1*x**-1+(identity-x**-1)*shift
        b = jmat*k*jmat
        base_error = max(
            error(x*k-qq*k*x, (q-q**-1)*identity),
            error(z-c0*identity, (x-identity)*(k+q*identity)),
            error(ell-c0*identity, (qq**-1*x**-1-identity)*(b+q*identity)),
            error(k**level, eta*identity), error(b**level, eta*identity),
            error(finite_determinant(k), 1), error(finite_determinant(b), 1),
        )
        for word in words:
            xx, kk, bb = x.copy(), k.copy(), b.copy()
            w = identity.copy()
            for letter in word:
                xx, kk, bb = update(letter, xx, kk, bb, q)
                w = w*({"+": m, "-": mi, "J": jmat}[letter])
            wi = w**-1
            f, fm = w*first, w*mi*first
            primitive = bb+q*identity
            cap = w*(ell-c0*identity)*wi
            maximum = max(
                base_error,
                error(xx, w*x*wi), error(kk, w*k*wi), error(bb, w*b*wi),
                error((qq**-1*xx**-1-identity)*primitive, cap),
                error(primitive*f, mp.zeros(level, 1)),
                error(w.H*jmat*w, jmat),
            )
            adj = adjugate(primitive)
            maximum = max(maximum,
                          error(adj*jmat, level*q**top*kappa*f*fm.H))
            closing = submatrix(primitive, range(1, level), range(level-1))
            maximum = max(maximum, error(
                eta*finite_determinant(closing),
                level*q**top*kappa*f[top]*mp.conj(fm[top])))
            assert maximum < tolerance, (level, word, maximum)
            records.append({"N": level, "word": word or "identity",
                            "maximum_relative_error": mp.nstr(maximum, 20),
                            "adjugate_entries_checked": level*level})

        two = jmat*m**2
        source = two*first
        cap_two = two*(ell-c0*identity)*two**-1
        green = mp.matrix(level)
        for row in range(level):
            for col in range(row, level):
                green[row, col] = (
                    -q**(-(col-row+1))*qq**(-sum(range(row, col+1)))
                    * mp.fprod(1-qq**r for r in range(row+1, col+1)))
        maximum = max(error(cap_two, b*(z-c0*identity)*b),
                      error(b*source, eta*last), error(green*b, identity),
                      error(green, b**-1), error(source[top], kappa*kappa))
        assert maximum < tolerance, (level, "two-crossing", maximum)
        records.append({"N": level, "word": "two-crossing forced Green",
                        "maximum_relative_error": mp.nstr(maximum, 20),
                        "adjugate_entries_checked": 0})
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=120)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    records = run(args.precision)
    dependencies = ["check_twist_period_insertion.py",
                    "check_current_free_aw_crossing_transport.py",
                    "check_rational_word_normalized_cofactor.py"]
    report = {
        "status": "pass", "precision_decimal_digits": args.precision,
        "scope": "Original full matrices, rational coordinate substitutions, "
                 "primitive polarized cofactor and forced two-crossing Green "
                 "equation. No general asymptotic or noncancellation claim.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependencies_sha256": {
            name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
            for name in dependencies},
        "checks": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"status": "pass", "cases": len(records),
                      "adjugate_entries": sum(r["adjugate_entries_checked"] for r in records),
                      "maximum_relative_error": mp.nstr(max(
                          mp.mpf(r["maximum_relative_error"]) for r in records), 12),
                      "output": str(args.output)}))


if __name__ == "__main__":
    main()
