#!/usr/bin/env python3
"""Check the original finite kernel's difference defect and endpoint normals.

The rational Newton identity is verified symbolically. Finite-level checks
use the defining Newton recurrence, including every index through N-1.
They are normalization diagnostics, not a proof of interior-node bounds.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp
import sympy as sp


def symbolic_identity():
    q, x, v = sp.symbols("q X V")
    a = -(q*q*x-1)**4/(q*(q*q*x*x-1)*(q**4*x*x-1))
    c = -q*(x-1)**4/((x*x-1)*(q*q*x*x-1))
    lhs = q + 1/q + a + c
    lhs -= a*(q*q*x*v-1)/(q*q*x-v)
    lhs -= c*(x-v)/(x*v-1)
    rhs = q*v + 1/(q*v)
    rhs += q*x*(v-1)**4/(v*(x*v-1)*(q*q*x-v))
    return sp.factor(lhs-rhs) == 0


def basis(n, z):
    theta = mp.pi/n
    values, derivatives = [mp.mpf(1)], [mp.mpf(0)]
    for i in range(1, n):
        factor = 2*mp.cos((2*i-1)*theta)-z
        denominator = 4*mp.sin(i*theta)**2
        derivatives.append(
            (factor*derivatives[-1]-values[-1])/denominator
        )
        values.append(factor*values[-1]/denominator)
    return values, derivatives


def relative_error(a, b):
    return abs(a-b)/max(1, abs(a), abs(b))


def finite_difference_checks(n):
    theta = mp.pi/n
    c0 = 2*mp.cos(theta)
    eta = (-1)**(n-1)
    sine = lambda x: 2*mp.sin(x*theta)
    spectral = lambda x: 2*mp.cos((2*x+1)*theta)
    cases, maximum = 0, mp.mpf(0)
    for x in [mp.mpc(".37", ".05"), mp.mpc("1.2", "-.07")]:
        a = sine(x+1)**4/(sine(2*x+1)*sine(2*x+2))
        c = sine(x)**4/(sine(2*x)*sine(2*x+1))
        vectors = [basis(n, spectral(x+h))[0] for h in [-1, 0, 1]]
        for w in [mp.mpc(".23", ".11"), mp.mpc("-1.13", ".04")]:
            e, ep = basis(n, w)
            kval = [mp.fdot(v, e) for v in vectors]
            kder = [mp.fdot(v, ep) for v in vectors]
            lk = -a*kval[2] + (c0+a+c)*kval[1] - c*kval[0]
            lkp = -a*kder[2] + (c0+a+c)*kder[1] - c*kder[0]
            defect = vectors[1][-1]*(w-c0)*e[-1]
            defect_derivative = vectors[1][-1]*(e[-1]+(w-c0)*ep[-1])
            relation = 2*mp.chebyt(n, w/2)+2
            maximum = max(
                maximum,
                relative_error(w*kval[1]-lk, defect),
                relative_error(kval[1]+w*kder[1]-lkp, defect_derivative),
                relative_error((w-c0)*e[-1], eta*relation/n**2),
            )
            cases += 1
    return {"level": n, "cases": cases, "max_relative_error": mp.nstr(maximum, 12)}


def endpoint_checks(n):
    theta = mp.pi/n
    c0 = 2*mp.cos(theta)
    v0, d0 = basis(n, c0)
    maximum = mp.mpf(0)
    largest_ratio = mp.mpf(0)
    cases = 0
    alpha = mp.mpf(n+1)/(3*(n-1))
    for j in range((n-2)//2+1):
        cj = 2*mp.cos((2*j+1)*theta)
        v, d = basis(n, cj)
        k = mp.fdot(v0, v)
        kx, ky, kxy = mp.fdot(d0, v), mp.fdot(v0, d), mp.fdot(d0, d)
        h = kxy/k-kx*ky/k**2
        target = sum(
            mp.csc(r*theta)**2 for r in range(j+1, n-j)
        )/(16*mp.sin(theta)*mp.sin((2*j+1)*theta))
        gamma0 = mp.mpf(n-1)/(4*mp.sin(theta))
        gammaj = mp.mpf(n-2*j-1)/(4*mp.sin((2*j+1)*theta))
        ratio = h/(gamma0*gammaj)
        maximum = max(maximum, relative_error(h, target))
        largest_ratio = max(largest_ratio, ratio)
        tolerance = mp.power(10, -mp.mp.dps//2)
        assert h > 0
        assert ratio <= alpha+tolerance
        cases += 1
    maximum = max(maximum, relative_error(largest_ratio, alpha))
    return {
        "level": n,
        "double_root_cases": cases,
        "max_relative_error": mp.nstr(maximum, 12),
        "largest_normalized_entry": mp.nstr(largest_ratio, 16),
        "sharp_constant": mp.nstr(alpha, 16),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    mp.mp.dps = args.precision
    assert symbolic_identity()
    difference = [finite_difference_checks(n) for n in range(2, 13)]
    endpoints = [endpoint_checks(n) for n in range(2, 25)]
    tolerance = mp.power(10, -args.precision//2)
    assert all(mp.mpf(r["max_relative_error"]) < tolerance
               for r in difference+endpoints)
    result = {
        "scope": "Exact finite kernel defect and sharp endpoint-row normal; "
                 "no interior-interior inequality or quantum asymptotic tested.",
        "precision_decimal_digits": args.precision,
        "symbolic_rational_identity": True,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "difference_checks": difference,
        "endpoint_checks": endpoints,
        "status": "pass",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({
        "status": "pass",
        "difference_cases": sum(r["cases"] for r in difference),
        "endpoint_cases": sum(r["double_root_cases"] for r in endpoints),
        "max_relative_error": mp.nstr(max(
            mp.mpf(r["max_relative_error"]) for r in difference+endpoints
        ), 12),
        "output": str(args.output),
    }))


if __name__ == "__main__":
    main()
