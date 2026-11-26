#!/usr/bin/env python3
"""Finite identities for the local angular block; no global cut is assumed."""
import argparse
import hashlib
import json
from pathlib import Path
import sympy as s

I = s.I
checks = []


def check(name, value):
    value = s.factor(s.cancel(value))
    if value != 0:
        raise AssertionError((name, value))
    checks.append(name)


def mob(M, z):
    if z is s.oo:
        return s.oo if M[1, 0] == 0 else M[0, 0] / M[1, 0]
    den = s.factor(M[1, 0] * z + M[1, 1])
    return s.oo if den == 0 else s.cancel((M[0, 0] * z + M[0, 1]) / den)


def cr(a, b, c, d):
    if a is s.oo:
        return s.cancel((b-d)/(b-c))
    if b is s.oo:
        return s.cancel((a-c)/(a-d))
    if c is s.oo:
        return s.cancel((b-d)/(a-d))
    if d is s.oo:
        return s.cancel((a-c)/(b-c))
    return s.cancel((a-c)*(b-d)/((a-d)*(b-c)))


def main():
    E, Z = s.symbols("E Z")
    R = Z*(1+E-Z)/E
    Q = (E-Z)/(Z-1)
    W = [
        s.Matrix([[1, 0], [0, E]]),
        s.Matrix([[1, E-1], [0, E]]),
        s.Matrix([[E-R, R*(1-E)], [E-1, 1-E*R]]),
        s.Matrix([[R, 0], [1-E, E*R]]),
    ]
    check("apex W0", mob(W[0], Z)-Z/E)
    check("apex W2", mob(W[2], Z)-Z/E)
    incoming = [
        (Z, s.oo, 1, 1, 0, -1/Q),
        (s.oo, 1, Z, Z/E, 1, -Q),
        (1, Z, s.oo, s.oo, 2, -1/Q),
    ]
    outgoing = [
        (Z, R, 0, 0, 2, -Q),
        (R, 0, Z, Z/E, 3, -1/Q),
        (0, Z, R, R, 0, -Q),
    ]
    for side, data in [("incoming", incoming), ("outgoing", outgoing)]:
        for j, (a, b, c, cm, wi, target) in enumerate(data):
            d = mob(W[wi].inv(), cm)
            check(f"{side} pants ratio {j}", cr(a, b, c, d)-target)
    for j in range(3):
        ti, to = incoming[j][-1], outgoing[j][-1]
        check(f"inverse seam ratio {j}", ti*to-1)

    r, z1, e = s.symbols("r z1 e")
    T = s.Matrix([[0, -r], [1, -1]])
    C = s.Matrix([[1, -r], [1, -1]])
    check("actual C T first apex", mob(C*T, z1)-r*z1/(z1-(1-r)))
    check("actual C T second apex", mob(C*T, z1/e)-r*z1/(z1-e*(1-r)))

    y, z, k = s.symbols("y z k")
    rel = k**2*(1+y*y+z*z)-1

    def on_branch(name, expr):
        num = s.together(expr).as_numer_denom()[0]
        check(name, s.rem(s.Poly(num, k), s.Poly(rel, k)).as_expr())

    kap0 = k*k*(1+y*y)/(1-k*k*y*y)
    kap1 = k*k*(1+z*z)/(1-k*k*z*z)
    on_branch("wire stationarity", kap0*kap1-1)
    on_branch("first ordered metric", kap0-(1+y*y)/(1+z*z))
    on_branch("second ordered metric", kap1-(1+z*z)/(1+y*y))
    ep = (1+I*k)/(1-I*k)
    hs = [(1-k*y)/(1+k*y), (1-k*z)/(1+k*z)]
    for j, (hh, yy) in enumerate(zip(hs, [y, z])):
        zz = (1+ep)/(1+hh)
        check(f"longitude Q {j}", (ep-zz)/(zz-1)-(1+I*yy)/(1-I*yy))
        rr = hh*(1+ep)**2/(ep*(1+hh)**2)
        target = (1+z*z)/(2+y*y+z*z) if j == 0 else (1+y*y)/(2+y*y+z*z)
        on_branch(f"quadrilateral metric {j}", rr-target)

    equator = [s.Integer(0), s.oo, s.Integer(1), s.Rational(1, 2)]
    ap = (1+I)/2
    bp = (1-I)/2
    for j in range(4):
        c, d = equator[j], equator[(j+1) % 4]
        check(f"plus complete shape {j}", cr(ap, bp, c, d)-I)
        check(f"minus complete shape {j}", cr(bp, ap, d, c)-I)

    # Rational enclosures used by the written complex-disk estimate.
    rad = s.Rational(1, 200)
    tan_upper = (rad/(1-rad**2/6))/(1-rad**2/(2*(1-rad**2/12)))
    u = s.Rational(5001, 10**6)
    delta = s.Rational(51, 10**6)
    dk = s.Rational(26, 10**6)
    bounds = {
        "tan": (tan_upper, u),
        "sum squares": (2*u*u, delta),
        "k motion": (delta/((1-delta)*(2-delta)), dk),
        "E motion": (2*dk/(s.Rational(7,5)*(s.Rational(7,5)-dk)),
                     s.Rational(6,100000)),
        "H motion": (2*(1+dk)*u/(1-(1+dk)*u), s.Rational(102,10000)),
        "R motion": (u*u/(2-2*u*u), s.Rational(26,10**6)),
        "cross ratio": ((4*s.Rational(8,100)+2*s.Rational(8,100)**2)
                        /(1-s.Rational(8,100))**2, s.Rational(2,5)),
    }
    for name, (value, upper) in bounds.items():
        if not value < upper:
            raise AssertionError((name, value, upper))

    result = {
        "scope": "Local rational identities and positivity enclosures only; no global topology or short-filling theorem.",
        "exact_identity_count": len(checks),
        "exact_identities": checks,
        "rational_enclosure_count": len(bounds),
        "rational_enclosures": {name: {"value": str(v), "upper": str(u)}
                                for name, (v, u) in bounds.items()},
    }
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path,
                        default=Path("/private/tmp/md-two-octahedron-angular-edge-block-results.json"))
    args = parser.parse_args()
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"identities": len(checks), "enclosures": len(bounds),
                      "output": str(args.output)}, indent=2))


if __name__ == "__main__":
    main()
