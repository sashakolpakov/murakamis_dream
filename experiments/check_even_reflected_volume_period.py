#!/usr/bin/env python3
"""Compare the reflected spectral period with the eight original cell volumes.

Finite numerical checks supplement the written proofs. Nonintegral values of
k test the continued action only; they are not asserted to define manifolds.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp


def relative(a, b):
    return abs(a-b)/max(mp.mpf(1), abs(a), abs(b))


def critical(k):
    return mp.findroot(
        lambda eta, phi: (
            mp.cosh(2*k*eta)-mp.cos(2*k*phi)-mp.cosh(eta)+mp.cos(phi),
            mp.sinh(2*k*eta)*mp.sinh(eta)+mp.sin(2*k*phi)*mp.sin(phi)),
        (mp.pi/(2*k*k), mp.pi/k-mp.pi/(4*k**3)))


def spectral_period(k, eta, phi, bent=False):
    origin = -1j*mp.pi/k
    endpoint = eta+1j*(mp.pi/k-phi)

    def integrand(displacement):
        if abs(displacement) < mp.eps**mp.mpf(".8"):
            return -4j*k/mp.tan(mp.pi/(2*k))
        a = origin+displacement
        # log1p retains the small displacement from X(origin)=1.
        u = mp.log1p(2*mp.sinh(k*displacement)*mp.cosh(a/2)
                    /mp.sinh((k-mp.mpf(".5"))*a))
        return u*(mp.coth(a/2)-2*k*mp.coth(k*displacement))

    vertices = [mp.mpc(0)]
    if bent:
        vertices.append(mp.mpc(eta))
    vertices.append(endpoint)
    integral = mp.mpc(0)
    for start, end in zip(vertices, vertices[1:]):
        step = end-start
        integral += mp.quad(lambda s: integrand(start+s*step)*step, [0, 1])
    return -2*mp.im(integral)


def bloch_wigner(z):
    return mp.im(mp.polylog(2, z))+mp.log(abs(z))*mp.arg(1-z)


def primitive(P):
    return (mp.pi*P/4+1j*(mp.polylog(2, -1j*mp.exp(-2*P))
                          -mp.polylog(2, 1j*mp.exp(-2*P)))/4
            -mp.catalan/2)


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    records = []
    for value in ("2", "2.5", "3", "4", "7.25", "10", "20", "50"):
        k = mp.mpf(value)
        eta, phi = critical(k)
        assert eta > 0 and 2*mp.pi/(2*k+1) < phi < mp.pi/k
        a = eta-1j*phi
        X = -mp.sinh((k+mp.mpf(".5"))*a)/mp.sinh((k-mp.mpf(".5"))*a)
        lam = -(mp.sinh(a/2)/mp.sinh(k*a))**2
        errors = [relative(abs(X), 1), relative(abs(lam), 1)]
        assert 0 < mp.arg(X) < mp.pi/2

        # Check the transgression away from the stationary point as well.
        for offset in (mp.mpc(0), mp.mpc(".013", ".007"),
                       mp.mpc(".031", "-.009")):
            z = a+offset
            plus, minus = mp.coth((k+mp.mpf(".5"))*z), mp.coth((k-mp.mpf(".5"))*z)
            ua = (k+mp.mpf(".5"))*plus-(k-mp.mpf(".5"))*minus
            uk = z*(plus-minus)
            va = mp.coth(z/2)-2*k*mp.coth(k*z)
            vk = -2*z*mp.coth(k*z)
            errors.append(relative(vk*ua-va*uk, -2*z))

        if k == int(k):
            size = int(k)
            jacobi = mp.matrix(size)
            for j in range(size-1):
                jacobi[j, j+1] = jacobi[j+1, j] = 1
            jacobi[0, 0] += X
            jacobi[size-1, size-1] += 1
            mu = -2*mp.cosh(a)
            errors.append(relative(mp.det(jacobi-mu*mp.eye(size)), 0))
            errors.append(relative((2*mp.re(X)-mu)/(2-2*mp.re(X)), lam))

        t, u = phi-1j*eta, -phi-1j*eta
        r = 1j*k*t-1j*mp.pi
        first, second = mp.tan(t/2), mp.tan(u/2)
        q = mp.sqrt(1+first**2+second**2)
        errors.extend((relative(mp.asinh(first*mp.cos(u/2)), r),
                       relative(mp.asinh(second*mp.cos(t/2)), -mp.conj(r))))
        margin = mp.re(q)**2-mp.re(first)**2-mp.re(second)**2
        assert abs(mp.im(q)) < tolerance and mp.re(q) > 0 and margin > mp.mpf(".5")

        P, Q = r/2+1j*u/4, r/2-1j*u/4
        A, C = 1j*mp.exp(2*Q), 1j*mp.exp(-2*P)
        B, D = (C-1)/(C+1), (A+1)/(1-A)
        shapes = (A, B, -1/A, -1/B, C, D, -1/C, -1/D)
        assert all(mp.im(z) > 0 for z in shapes)
        cell_volume = mp.fsum(bloch_wigner(z) for z in shapes)
        phase = (4*mp.catalan-2*(P+Q)*(mp.atan(mp.tanh(P))+mp.atan(mp.tanh(Q)))
                 +4*(primitive(P)+primitive(Q)))/mp.pi
        action = phase+1j*k*(t*t-u*u)/(2*mp.pi)-1j*(t+u)
        straight = spectral_period(k, eta, phi)
        bent = spectral_period(k, eta, phi, bent=True)
        errors.extend((relative(straight, bent), relative(straight, cell_volume),
                       relative(2*mp.pi*action, cell_volume)))
        maximum = max(errors)
        assert maximum < tolerance, (k, maximum)
        records.append({
            "k": value, "integer_filling": bool(k == int(k)),
            "eta": mp.nstr(eta, 35), "phi": mp.nstr(phi, 35),
            "spectral_period": mp.nstr(straight, 35),
            "eight_cell_volume": mp.nstr(cell_volume, 35),
            "positive_cell_margin": mp.nstr(margin, 25),
            "maximum_relative_identity_error": mp.nstr(maximum, 25),
        })
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    records = run(args.precision)
    source = Path(__file__).resolve()
    result = {
        "status": "pass", "precision_decimal_digits": args.precision,
        "mpmath_version": mp.__version__,
        "script_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "scope": "Finite period, primitive-return, positive-cell and action "
                 "comparisons; no finite check certifies an asymptotic theorem.",
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "pass", "cases": len(records),
                      "maximum_relative_identity_error": max(
                          (r["maximum_relative_identity_error"] for r in records), key=mp.mpf),
                      "output": str(args.output)}))


if __name__ == "__main__":
    main()
