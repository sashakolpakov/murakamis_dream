#!/usr/bin/env python3
"""Original full-kernel diagnostics for the all-color first-normal bound.

This checks the endpoint-forced shifted-Jacobi identity using the defining
Newton polynomials. No Newton index or physical first normal is removed.
The all-level inequalities are proved in the companion research note.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from check_edge_kernel_difference_and_endpoint_bound import basis, relative_error


def coefficient_data(n, r):
    theta = mp.pi/n
    s = lambda x: 2*mp.sin(x*theta)
    a = s(r+1)**4/(s(2*r+1)*s(2*r+2))
    ap = a*theta*(4*mp.cot((r+1)*theta)
                  -2*mp.cot((2*r+1)*theta)-2*mp.cot((2*r+2)*theta))
    if r == 0:
        return a, mp.mpf(0), ap, mp.mpf(0)
    c = s(r)**4/(s(2*r)*s(2*r+1))
    cp = c*theta*(4*mp.cot(r*theta)
                  -2*mp.cot(2*r*theta)-2*mp.cot((2*r+1)*theta))
    return a, c, ap, cp


def shifted_rows(n, w, length):
    theta = mp.pi/n
    c0 = 2*mp.cos(theta)
    q0 = -4*theta*mp.sin(theta)
    force = q0/(n*n*(2*mp.sin(theta))**2)
    f, r, defect = [mp.mpf(1)], [mp.mpf(0)], [mp.mpf(0)]
    for j in range(length):
        a, c, ap, cp = coefficient_data(n, j)
        oldf = f[-2] if j else 0
        oldr = r[-2] if j else 0
        oldd = defect[-2] if j else 0
        nextf = ((c0+a+c-w)*f[-1]-c*oldf)/a
        nextr = ((c0+a+c-w)*r[-1]-c*oldr
                 +(ap+cp)*f[-1]-ap*nextf-cp*oldf)/a
        nextd = ((c0+a+c-w)*defect[-1]-c*oldd
                 +(force if j == 0 else 0))/a
        f.append(nextf)
        r.append(nextr)
        defect.append(nextd)
    return f, r, defect


def source_identity_checks(n):
    theta = mp.pi/n
    last = (n-2)//2
    c0 = 2*mp.cos(theta)
    q0 = -4*theta*mp.sin(theta)
    v0, dv0 = basis(n, c0)
    maximum = mp.mpf(0)
    count = 0
    for w in [mp.mpc(".23", ".11"), mp.mpc("-1.13", ".04")]:
        vw, _ = basis(n, w)
        q = mp.fdot(dv0, vw)
        f, r, defect = shifted_rows(n, w, last)
        relation = 2*mp.chebyt(n, w/2)+2
        for j in range(last+1):
            cj = 2*mp.cos((2*j+1)*theta)
            qj = -4*theta*mp.sin((2*j+1)*theta)
            vj, dvj = basis(n, cj)
            direct_f = mp.fdot(vj, vw)
            direct_g = mp.fdot(dvj, vw)
            rhs = q0*f[j]*q+r[j]+relation*defect[j]
            maximum = max(maximum, relative_error(qj*direct_g, rhs),
                          relative_error(direct_f, f[j]))
            count += 1
    return {"level": n, "cases": count, "max_relative_error": mp.nstr(maximum, 12)}


def normal_bound_checks(n):
    theta = mp.pi/n
    count = (n-2)//2+1
    vectors = []
    gammas = []
    for j in range(count):
        cj = 2*mp.cos((2*j+1)*theta)
        vectors.append(basis(n, cj))
        gammas.append(mp.mpf(n-2*j-1)/(4*mp.sin((2*j+1)*theta)))
    largest = -mp.inf
    minimum = mp.inf
    for j, (vj, dj) in enumerate(vectors):
        for k, (vk, dk) in enumerate(vectors):
            kernel = mp.fdot(vj, vk)
            h = mp.fdot(dj, dk)/kernel
            h -= mp.fdot(dj, vk)*mp.fdot(vj, dk)/kernel**2
            ratio = h/(gammas[j]*gammas[k])
            largest = max(largest, ratio)
            minimum = min(minimum, ratio)
    tolerance = mp.power(10, -mp.mp.dps//2)
    assert largest <= 1+tolerance
    if n > 2:
        assert largest < 1
    return {"level": n, "ordered_pairs": count*count,
            "largest_normalized_entry": mp.nstr(largest, 16),
            "smallest_normalized_entry_diagnostic_only": mp.nstr(minimum, 16)}


def jacobi_checks(n):
    length = (n-1)//2
    if length == 0:
        return None
    data = [coefficient_data(n, r) for r in range(length)]
    derivative = mp.matrix(length)
    maximum = mp.mpf(0)
    for r, (a, c, ap, cp) in enumerate(data):
        derivative[r, r] = ap+cp
        if r+1 < length:
            an, cn, apn, cpn = data[r+1]
            off = mp.sqrt(a*cn)*(ap/a+cpn/cn)/2
            derivative[r, r+1] = derivative[r+1, r] = -off
            rho = off/mp.sqrt((ap+cp)*(apn+cpn))
            m = r+1
            bound = mp.mpf(m*m*(8*m*m-3))/(4*m*m-1)**2
            assert 0 < rho <= bound
            maximum = max(maximum, rho/bound)
    eigenvalues = mp.eigsy(derivative, eigvals_only=True)
    assert eigenvalues[0] > 0
    return {"level": n, "matrix_size": length,
            "smallest_eigenvalue": mp.nstr(eigenvalues[0], 16),
            "largest_offdiagonal_ratio_to_proved_bound": mp.nstr(maximum, 16)}


def symbolic_inequalities():
    u, h = sp.symbols("u h")
    rho = (1-4*u*h)*(2-h*(3-2*u))/(4*(1-h)**2)
    r0 = (2-3*h)/(4*(1-h)**2)
    assert sp.factor(rho-r0+u*h*(3-6*h+4*u*h)/(2*(1-h)**2)) == 0
    assert sp.factor((rho-sp.Rational(1, 2))*4*(1-h)**2
                     -h*((1-6*u)-2*h*(1-6*u+4*u*u))) == 0
    m = sp.symbols("m")
    assert sp.expand((4*m*m-1)**3-m*m*(8*m*m-3)**2) == 3*m*m-1
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    mp.mp.dps = args.precision
    symbolic = symbolic_inequalities()
    source = [source_identity_checks(n) for n in range(2, 17)]
    bound = [normal_bound_checks(n) for n in range(2, 33)]
    jacobi = [jacobi_checks(n) for n in range(3, 25)]
    tolerance = mp.power(10, -args.precision//2)
    assert all(mp.mpf(r["max_relative_error"]) < tolerance for r in source)
    record = {
        "status": "pass",
        "scope": "Full original normal identity and all-color upper bound; "
                 "no lower bound for the coherent color sum.",
        "precision_decimal_digits": args.precision,
        "symbolic_algebra_checks": symbolic,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "basis_dependency_sha256": hashlib.sha256(
            Path(__file__).with_name(
                "check_edge_kernel_difference_and_endpoint_bound.py"
            ).read_bytes()
        ).hexdigest(),
        "source_identity": source,
        "mixed_normal_bound": bound,
        "jacobi_derivative": jacobi,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({
        "status": "pass",
        "source_identity_cases": sum(r["cases"] for r in source),
        "mixed_normal_pairs": sum(r["ordered_pairs"] for r in bound),
        "jacobi_matrices": len(jacobi),
        "max_source_identity_error": mp.nstr(max(
            mp.mpf(r["max_relative_error"]) for r in source
        ), 12),
        "output": str(args.output),
    }))


if __name__ == "__main__":
    main()
