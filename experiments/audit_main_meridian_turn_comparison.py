#!/usr/bin/env python3
"""Reproduce finite checks of the main-meridian turn comparison.

The numerical checks build the complete N^2-dimensional physical tensors
from E,F,K, the coproduct, the checked mixed braiding, and the duality
index formula. They do not use the sparse turn recurrence or its proposed
coefficient matrix. Exact checks use arithmetic in a cyclotomic number
field for the value kernel and the complete Frobenius/radical pairing.

Requires mpmath and SymPy. The saved results distinguish exact identities
from high-precision numerical checks. Finite tests do not prove a uniform
operator bound or an asymptotic statement.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp
import sympy as sp


def kron(a, b):
    out = mp.matrix(a.rows * b.rows, a.cols * b.cols)
    for i in range(a.rows):
        for j in range(a.cols):
            if not a[i, j]:
                continue
            for k in range(b.rows):
                for l in range(b.cols):
                    out[i * b.rows + k, j * b.cols + l] = a[i, j] * b[k, l]
    return out


def max_abs(a):
    return max((abs(v) for v in a), default=mp.mpf(0))


def discrepancy(a, b):
    error = max_abs(a - b)
    scale = max(mp.mpf(1), max_abs(a), max_abs(b))
    return error, error / scale


def module(n, q, displacement):
    """Unbalanced nilpotent basis, with literal physical E,F,K entries."""
    root = -q ** (-1) * mp.exp(mp.j * mp.pi * displacement / n)
    rho = q - q ** (-1)
    Q = q * q
    E, F, K = mp.matrix(n), mp.matrix(n), mp.matrix(n)
    ecoeff = []
    for a in range(n):
        bracket = (q**a - q**(-a)) / rho
        ea = bracket * (root * q ** (1 - a) - root**(-1) * q ** (a - 1)) / rho
        ecoeff.append(ea)
        K[a, a] = root * Q ** (-a)
        if a:
            E[a - 1, a] = ea
        if a + 1 < n:
            F[a + 1, a] = 1
    dual = [(-root)**a * Q ** (a * (a + 1) // 2) for a in range(n)]
    return {"E": E, "F": F, "K": K, "root": root, "e": ecoeff, "dual": dual}


def pair(n, q, left, right):
    eye = mp.eye(n)
    Etot = kron(left["E"], right["K"]) + kron(eye, right["E"])
    Ftot = kron(left["F"], eye) + kron(left["K"]**-1, right["F"])
    Ktot = kron(left["K"], right["K"])
    rho = q - q**-1
    omega = rho**2 * (Ftot * Etot) + q * Ktot + q**-1 * Ktot**-1
    return {"E": Etot, "F": Ftot, "K": Ktot, "omega": omega}


def checked_braid(n, q, s, left, right):
    """Full mixed R: nilpotent transfer, then Cartan, then the swap.

    The Cartan logarithms are alpha=d+s and beta=d-s. They are fixed by
    the actual highest weights; no principal logarithm of a matrix is used.
    """
    d = n - 1
    rho = q - q**-1
    alpha, beta = d + s, d - s
    R = mp.matrix(n*n)
    factorial = [mp.mpf(1)]
    for l in range(1, n):
        factorial.append(factorial[-1] * (q**l - q**(-l)) / rho)
    for a in range(n):
        for b in range(n):
            product = mp.mpf(1)
            for l in range(min(a, d-b) + 1):
                if l:
                    product *= left["e"][a-l+1]
                nilpotent = q ** (l*(l-1)//2) * rho**l * product / factorial[l]
                after_a, after_b = a-l, b+l
                exponent = (alpha-2*after_a) * (beta-2*after_b) / 2
                cartan = mp.exp(mp.j * mp.pi * exponent / n)
                R[after_b*n+after_a, a*n+b] += nilpotent * cartan
    return R


def newton_matrices(n, omega):
    eye = mp.eye(n*n)
    out = [eye]
    for r in range(n-1):
        node = 2 * mp.cos((2*r+1)*mp.pi/n)
        out.append(out[-1] * (node*eye-omega) / (4*mp.sin((r+1)*mp.pi/n)**2))
    return out


def currying(n, A, dual_in, dual_out):
    """T(A)^(j,b)_(a,k)=c_a(in)/c_b(out) A^(d-a,j)_(k,d-b)."""
    d = n-1
    out = mp.matrix(n*n)
    for j in range(n):
        for b in range(n):
            for a in range(n):
                ratio = dual_in[a] / dual_out[b]
                for k in range(n):
                    out[j*n+b, a*n+k] = ratio * A[(d-a)*n+j, k*n+d-b]
    return out


def chebyshev_matrix(n, omega):
    prev, current = 2*mp.eye(omega.rows), omega.copy()
    for _ in range(1, n):
        prev, current = current, omega*current-prev
    return current


def physical_case(n, s, tolerance):
    q = mp.exp(mp.j*mp.pi/n)
    d = n-1
    xmod, ymod = module(n, q, s), module(n, q, -s)
    xx, xy, yx = pair(n, q, xmod, xmod), pair(n, q, xmod, ymod), pair(n, q, ymod, xmod)
    Rxy = checked_braid(n, q, s, xmod, ymod)
    exx = newton_matrices(n, xx["omega"])
    exy = newton_matrices(n, xy["omega"])
    eyx = newton_matrices(n, yx["omega"])
    kappa0 = mp.exp(mp.j*mp.pi*d*d/(2*n))
    r0 = mp.matrix(n*n)
    for k, e in enumerate(exy):
        r0 += kappa0 * (-q)**k * e
    carrier = Rxy * r0**-1
    H = mp.mpf(1) if not s else mp.sin(mp.pi*s)/(n*mp.sin(mp.pi*s/n))
    W = [mp.mpf(1)]
    for k in range(1, n):
        W.append(W[-1]*(1-mp.sin(mp.pi*s/n)**2/mp.sin(mp.pi*k/n)**2))
    scalar = mp.exp(-mp.j*mp.pi*s*s/(2*n))

    checks = []

    def check(name, lhs, rhs, index=None):
        absolute, relative = discrepancy(lhs, rhs)
        if relative >= tolerance:
            raise AssertionError({"check": name, "N": n, "s": str(s), "index": index,
                                  "absolute_error": str(absolute), "scaled_error": str(relative)})
        checks.append({"check": name, "index": index,
                       "absolute_error": mp.nstr(absolute, 12),
                       "scaled_error": mp.nstr(relative, 12)})

    for generator in ("E", "F", "K"):
        check("mixed_braid_intertwines_"+generator, Rxy*xy[generator], yx[generator]*Rxy)
    check("opposite_Casimir_relation", chebyshev_matrix(n, xy["omega"]), -2*mp.eye(n*n))
    check("equal_Casimir_relation", chebyshev_matrix(n, xx["omega"]),
          -2*mp.cos(2*mp.pi*s)*mp.eye(n*n))
    if not s:
        check("complete_carrier_is_identity", carrier, mp.eye(n*n))

    for k in range(n):
        turned = currying(n, exx[k], xmod["dual"], xmod["dual"]) * carrier
        check("fixed_equal_to_mixed_turn", turned, scalar*W[k]/H*exy[d-k], k)
        mixed_turned = currying(n, exy[k], xmod["dual"], ymod["dual"])
        check("opposite_endomorphism_turn", mixed_turned, W[k]/H*eyx[d-k], k)
    return {"N": n, "s_real": mp.nstr(mp.re(s), 20), "s_imag": mp.nstr(mp.im(s), 20),
            "tensor_dimension": n*n, "matrix_identities": len(checks),
            "matrix_entries_checked": len(checks)*n**4,
            "largest_scaled_error": mp.nstr(max(mp.mpf(v["scaled_error"]) for v in checks), 12),
            "checks": checks}


def exact_eye(n, field):
    return [[field.one if i == j else field.zero for j in range(n)] for i in range(n)]


def exact_mul(a, b, field):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), field.zero)
             for j in range(len(b[0]))] for i in range(len(a))]


def exact_inverse(a, field):
    n = len(a)
    eye = exact_eye(n, field)
    aug = [a[i][:]+eye[i] for i in range(n)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if aug[i][j])
        aug[j], aug[pivot] = aug[pivot], aug[j]
        value = aug[j][j]
        aug[j] = [x/value for x in aug[j]]
        for i in range(n):
            if i != j and aug[i][j]:
                value = aug[i][j]
                aug[i] = [x-value*y for x, y in zip(aug[i], aug[j])]
    return [row[n:] for row in aug]


def exact_cyclotomic_case(n):
    """No floating roots or square roots enter these field identities."""
    symbol, z = sp.symbols("root z")
    field = sp.QQ.algebraic_field(sp.CRootOf(sp.cyclotomic_poly(2*n, symbol), 0))
    q, zero, one = field.unit, field.zero, field.one
    d, m = n-1, (n-1)//2
    double_count = m+1 if n % 2 == 0 else m
    nodes = [q**(2*j+1)+q**(-2*j-1) for j in range(m+1)]
    a = [zero]+[2-q**(2*r)-q**(-2*r) for r in range(1, n)]
    polynomial_one = sp.Poly(1, z, domain=field)
    variable = sp.Poly(z, z, domain=field)
    basis = [polynomial_one]
    for k in range(n-1):
        ck = q**(2*k+1)+q**(-2*k-1)
        basis.append(basis[-1]*(polynomial_one.mul_ground(ck)-variable).mul_ground(one/a[k+1]))

    def evaluate(poly, value):
        result = zero
        for coefficient in poly.rep.to_list():
            result = result*value+coefficient
        return result

    E = [[evaluate(basis[k], node) for k in range(m+1)] for node in nodes]
    Ei = exact_inverse(E, field)
    shift = [[one if i == j+1 else zero for j in range(m+1)] for i in range(m+1)]
    L = exact_mul(exact_mul(E, shift, field), Ei, field)
    for j in range(m+1):
        for l in range(m+1):
            target = zero
            if l < j:
                target = (q**(2*l+1)-q**(-2*l-1))*sum(
                    ((q**r+q**(-r))/(q**r-q**(-r)) for r in range(l+1, j+1)), zero)
            assert L[j][l] == target, ("positive shift kernel", n, j, l)

    previous, modulus = polynomial_one.mul_ground(2), variable
    for _ in range(1, n):
        previous, modulus = modulus, variable*modulus-previous
    modulus += polynomial_one.mul_ground(2)
    pairing_count = 0
    for i in range(n):
        for j in range(n):
            remainder = (basis[i]*basis[j]).rem(modulus)
            coefficient = remainder.rep.to_dict().get((d,), zero)
            assert coefficient*((-1)**d*n*n) == field.convert(int(i+j == d)), (
                "complete Frobenius pairing", n, i, j)
            pairing_count += 1

    # A rational xi tests the polynomial identity, without a numerical s.
    xi = field.convert(sp.Rational(1, 7))
    weights = [one]
    for k in range(1, n):
        weights.append(weights[-1]*(one-xi/a[k]))
    for k in range(n):
        assert weights[k]*weights[d-k] == weights[d], ("paired reflection", n, k)
    value_K = exact_mul([[E[j][k]*weights[k] for k in range(m+1)] for j in range(m+1)], Ei, field)
    jets = [[evaluate(basis[k], node) for k in range(n)] for node in nodes]
    jets += [[evaluate(basis[k].diff(), nodes[j]) for k in range(n)] for j in range(double_count)]
    jet_inverse = exact_inverse(jets, field)
    full = exact_mul([[jets[j][k]*weights[k] for k in range(n)] for j in range(n)], jet_inverse, field)
    for j in range(m+1):
        for l in range(m+1):
            assert full[j][l] == value_K[j][l], ("full value block", n, j, l)
        for l in range(m+1, n):
            assert full[j][l] == zero, ("normal-to-value block", n, j, l)
    if double_count:
        Kdouble = [row[:double_count] for row in value_K[:double_count]]
        inverse_Kdouble = exact_inverse(Kdouble, field)
        alpha = [(-1)**d*(2-q**(2*(2*j+1))-q**(-2*(2*j+1))) for j in range(double_count)]
        for j in range(double_count):
            for l in range(double_count):
                target = weights[d]*inverse_Kdouble[l][j]*alpha[l]/alpha[j]
                assert full[m+1+j][m+1+l] == target, ("radical inverse transpose", n, j, l)
    return {"N": n, "field": "Q[root]/Phi_"+str(2*n), "xi": "1/7",
            "shift_kernel_entries": (m+1)**2,
            "Frobenius_pairing_identities": pairing_count,
            "paired_reflection_identities": n,
            "full_jet_matrix_dimension": n,
            "radical_block_entries": double_count**2,
            "result": "all exact identities hold"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("main_meridian_turn_comparison_results.json"))
    parser.add_argument("--max-level", type=int, default=6)
    parser.add_argument("--exact-max-level", type=int, default=8)
    parser.add_argument("--digits", type=int, default=80)
    args = parser.parse_args()
    if args.max_level < 2 or args.exact_max_level < 2 or args.digits < 70:
        parser.error("levels must be at least 2 and precision at least 70 digits")
    mp.mp.dps = args.digits
    tolerance = mp.mpf(10)**(-(args.digits-25))
    parameters = [mp.mpc(0), mp.mpc("0.25", "0.125")]
    numerical = []
    for n in range(2, args.max_level+1):
        for s in parameters:
            numerical.append(physical_case(n, s, tolerance))
        if n in (3, 4):
            numerical.append(physical_case(n, mp.mpc("0.5"), tolerance))
    exact = [exact_cyclotomic_case(n) for n in range(2, args.exact_max_level+1)]
    result = {
        "description": "Independent full physical tensor tests and exact spectral-kernel checks",
        "scope": "Finite reproduction only; not a proof of uniform bounds, asymptotics, or whole-knot estimates.",
        "construction": "E,F,K -> coproduct Casimir; full transfer/Cartan/swap braid; direct currying indices; full-matrix carrier inverse",
        "versions": {"mpmath": mp.__version__, "sympy": sp.__version__},
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "numerical_parameters": {"decimal_digits": args.digits, "scaled_error_tolerance": str(tolerance),
                                 "maximum_level": args.max_level},
        "numerical_physical_tensor_checks": numerical,
        "exact_cyclotomic_checks": exact,
        "result": "all checks passed",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"result": str(args.output), "physical_cases": len(numerical),
                      "physical_matrix_identities": sum(x["matrix_identities"] for x in numerical),
                      "physical_matrix_entries": sum(x["matrix_entries_checked"] for x in numerical),
                      "exact_levels": len(exact),
                      "largest_scaled_error": max((x["largest_scaled_error"] for x in numerical), key=mp.mpf)}, indent=2))


if __name__ == "__main__":
    main()
