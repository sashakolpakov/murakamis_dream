#!/usr/bin/env python3
"""Reproduce moving-Newton identities and draw their coefficient support.

Run from any directory:
    python3 experiments/audit_main_meridian_newton_algebra.py

Requires SymPy, mpmath and Matplotlib. Rational and cyclotomic polynomial
identities are exact. The bulk-factor evaluations are numerical diagnostics;
the uniform asymptotic statements are proved in the accompanying notes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
Z = sp.Symbol("z")


def pochhammer(a, p, n):
    return sp.prod(1 - a * p**j for j in range(n))


def exact_generic_multiplication():
    """Expand both sides as polynomials, without using the proof recurrence."""
    q = sp.Rational(3, 2)
    y = sp.Rational(5, 3)
    rho = q - 1 / q
    bracket = lambda r: (q**r - q**(-r)) / rho
    shifted = lambda r: (q**r / y - y * q**(-r)) / rho
    factorial = [sp.S.One]
    for r in range(1, 16):
        factorial.append(factorial[-1] * bracket(r))
    basis = [sp.Poly(1, Z)]
    for r in range(15):
        basis.append(
            basis[-1] * sp.Poly(q ** (2 * r + 1) / y + y * q ** (-2 * r - 1) - Z, Z)
        )
    checked = 0
    for i in range(8):
        for j in range(8):
            rhs = sp.Poly(0, Z)
            for k in range(max(i, j), i + j + 1):
                coefficient = (
                    (-rho**2) ** (i + j - k)
                    * factorial[i]
                    * factorial[j]
                    / (factorial[k - i] * factorial[k - j] * factorial[i + j - k])
                )
                coefficient *= sp.prod(shifted(r) for r in range(k + 1, i + j + 1))
                rhs += basis[k].mul_ground(coefficient)
            assert basis[i] * basis[j] == rhs, ("generic multiplication", i, j)
            checked += 1
    return {"identities": checked, "q": str(q), "Y": str(y), "indices": "0 <= i,j <= 7"}


def exact_connections():
    """Direct product expansion checks the connection and its inverse."""
    cases = [
        (sp.Rational(2, 3), sp.Rational(5, 4), sp.Rational(7, 5)),
        (sp.Rational(3, 5), sp.Rational(-4, 3), sp.Rational(6, 5)),
    ]
    checked = 0
    for p, a, b in cases:
        for left, right in [(a, b), (b, a)]:
            basis_left = [sp.Poly(1, Z, domain=sp.QQ)]
            basis_right = [sp.Poly(1, Z, domain=sp.QQ)]
            for j in range(8):
                basis_left.append(
                    basis_left[-1] * sp.Poly(1 - left * p**j * Z + left**2 * p ** (2 * j), Z)
                )
                basis_right.append(
                    basis_right[-1] * sp.Poly(1 - right * p**j * Z + right**2 * p ** (2 * j), Z)
                )
            for n in range(9):
                rhs = sp.Poly(0, Z)
                for k in range(n + 1):
                    gaussian = (
                        pochhammer(p, p, n)
                        / (pochhammer(p, p, k) * pochhammer(p, p, n - k))
                    )
                    coefficient = (
                        gaussian * (left / right) ** k
                        * pochhammer(left * right * p**k, p, n - k)
                        * pochhammer(left / right, p, n - k)
                    )
                    rhs += basis_right[k].mul_ground(coefficient)
                assert basis_left[n] == rhs, ("connection", p, left, right, n)
                checked += 1
    return {
        "identities": checked,
        "indices": "0 <= n <= 8, both connection directions",
        "parameters": [{"p": str(p), "a": str(a), "b": str(b)} for p, a, b in cases],
    }


def exact_cyclotomic_duality():
    """Reduce independently built products in the exact root quotient.

    A root of Phi_(2N) defines an exact number field. Choosing a different
    primitive embedding cannot change a polynomial identity. Normalization
    uses sigma_r^2=prod(2-q^(2v)-q^(-2v)), requiring no floating square roots.
    """
    x = sp.Symbol("x")
    records = []
    for n in range(2, 9):
        field = sp.QQ.algebraic_field(sp.CRootOf(sp.cyclotomic_poly(2 * n, x), 0))
        q = field.unit
        one = sp.Poly(1, Z, domain=field)
        variable = sp.Poly(Z, Z, domain=field)
        cheb_prev, cheb = one.mul_ground(2), variable
        for _ in range(1, n):
            cheb_prev, cheb = cheb, variable * cheb - cheb_prev
        for value in [sp.Rational(1), sp.Rational(5, 3)]:
            y = field.convert(value)
            modulus = cheb + one.mul_ground(y**n + y**(-n))
            plus = [one]
            minus = [one]
            norm = field.one
            raw_plus, raw_minus = one, one
            for r in range(1, n):
                j = r - 1
                cplus = q ** (2 * j + 1) / y + y * q ** (-2 * j - 1)
                cminus = q ** (2 * j + 1) * y + q ** (-2 * j - 1) / y
                raw_plus *= one.mul_ground(cplus) - variable
                raw_minus *= one.mul_ground(cminus) - variable
                norm *= 2 - q ** (2 * r) - q ** (-2 * r)
                plus.append(raw_plus.mul_ground(field.one / norm))
                minus.append(raw_minus.mul_ground(field.one / norm))
            checked = 0
            for i in range(n):
                for j in range(n):
                    remainder = (plus[i] * minus[j]).rem(modulus)
                    coefficient = remainder.rep.to_dict().get((n - 1,), field.zero)
                    result = coefficient * ((-1) ** (n - 1) * n**2)
                    assert result == field.convert(int(i + j == n - 1)), (
                        "mixed duality", n, value, i, j
                    )
                    checked += 1
            row = {"N": n, "Y": str(value), "identities": checked}
            if value == 1:
                raw, derivative = one, one.mul_ground(0)
                norm = field.one
                for r in range(1, n):
                    j = r - 1
                    c = q ** (2 * j + 1) + q ** (-2 * j - 1)
                    dc = q ** (-2 * j - 1) - q ** (2 * j + 1)
                    factor = one.mul_ground(c) - variable
                    derivative = derivative * factor + raw.mul_ground(dc)
                    raw *= factor
                    norm *= 2 - q ** (2 * r) - q ** (-2 * r)
                    rhs = one.mul_ground(0)
                    for k in range(r):
                        m = r - k
                        coefficient = (-1) ** (m + 1) * q**(-m) / (1 - q**(-2*m))
                        rhs += plus[k].mul_ground(coefficient)
                    assert derivative.mul_ground(field.one / norm) == rhs, ("connection derivative", n, r)
                row["exact_logY_connection_derivatives"] = n - 1
            records.append(row)
    return records


def bulk_diagnostics():
    mp.mp.dps = 80
    records = []
    for n in [24, 48, 96, 192]:
        i = j = 2 * n // 3
        k = 5 * n // 6
        h = i + j - n
        factorial = [mp.mpf(1)]
        for r in range(1, n):
            factorial.append(factorial[-1] * 2 * mp.sin(mp.pi * r / n))
        denominator = (
            factorial[i] * factorial[j] * factorial[k - i]
            * factorial[k - j] * factorial[i + j - k]
        )
        front = factorial[k] ** 2 / denominator
        nu = factorial[k] * factorial[h] / denominator

        def mu(s):
            return front * mp.fprod(
                2 * mp.sin(mp.pi * (r - 2 * s) / n)
                for r in range(k + 1, i + j + 1)
            )

        slope = 4 * mp.pi * (-1) ** h * nu
        derivative_error = abs(mp.diff(mu, 0) / slope - 1)
        assert derivative_error < mp.mpf("1e-65"), ("first derivative", n)
        ratio = mp.sin(mp.pi * (k + 1) / n) / mp.sin(mp.pi * h / n)
        row = {
            "N": n, "i": i, "j": j, "k": k,
            "derivative_relative_error": mp.nstr(derivative_error, 12),
            "unit_errors": [],
        }
        for s in [
            mp.mpf(".13"), mp.mpc(".27", ".19"),
            mp.mpc("-.4", ".2"), mp.mpf("1.1"),
        ]:
            leading = (-1) ** h * 2 * mp.sin(2 * mp.pi * s) * nu * ratio ** (2 * s)
            error = abs(mu(s) / leading - 1)
            row["unit_errors"].append({
                "s_real": mp.nstr(s.real, 8), "s_imag": mp.nstr(s.imag, 8),
                "absolute_unit_error": mp.nstr(error, 16),
                "N_times_error": mp.nstr(n * error, 16),
            })
        records.append(row)
    return records


def draw_support(output_dir):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Polygon

    matplotlib.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 11,
        "svg.fonttype": "none", "svg.hashsalt": "moving-newton-products-v1",
        "pdf.fonttype": 42,
    })
    fig, axes = plt.subplots(1, 2, figsize=(11.4, 6.6))
    for axis, varied in zip(axes, [False, True]):
        axis.add_patch(Polygon([(0, 0), (1, 0), (0, 1)],
                               facecolor="#d6eee8", edgecolor="none"))
        axis.add_patch(Polygon([(1, 0), (1, 1), (0, 1)],
                               facecolor="#f8dfba" if varied else "#e7e9ed",
                               edgecolor="none"))
        axis.plot([0, 1], [1, 0], color="#596273", linewidth=1.6, linestyle="--")
        axis.text(.26, .25, "Nonzero products\n" + r"$i+j<N$",
                  ha="center", va="center", color="#174f46", linespacing=1.6)
        axis.text(.73, .72,
                  ("Products can be nonzero\n" + r"$i+j\geq N$") if varied
                  else ("Product is zero\n" + r"$i+j\geq N$"),
                  ha="center", va="center",
                  color="#70440d" if varied else "#495363", linespacing=1.6)
        axis.text(.53, .48, r"$x+y=1$", rotation=-45,
                  ha="center", va="center", color="#374151",
                  bbox={"facecolor": "white", "edgecolor": "none", "pad": 3})
        axis.set(xlim=(0, 1), ylim=(0, 1), aspect="equal",
                 xlabel=r"First index: $x=i/N$", ylabel=r"Second index: $y=j/N$")
        axis.set_xticks([0, .5, 1], ["0", "1/2", "1"])
        axis.set_yticks([0, .5, 1], ["0", "1/2", "1"])
        axis.set_title("Generic meridian displacement" if varied else "Complete meridian: s = 0",
                       fontsize=12, pad=14)
    fig.suptitle("Which Newton products vanish?",
                 fontsize=16, x=.5, y=.97)
    fig.text(.5, .904, r"Products $e_i e_j$ of normalized Newton polynomials",
             ha="center", fontsize=12, color="#4b5563")
    fig.text(.5, .10,
             r"Output indices: $\max(i,j)\leq k\leq\min(i+j,N-1)$."
             "\nThe exact finite threshold is i + j = N; the square shows normalized indices.",
             ha="center", fontsize=11, linespacing=1.5)
    fig.text(.5, .025,
             "Coefficient support does not determine the growth of a knot invariant.",
             ha="center", fontsize=10.5, color="#4b5563")
    fig.subplots_adjust(left=.075, right=.975, bottom=.22, top=.82, wspace=.27)
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = []
    for extension in ["pdf", "svg", "png"]:
        path = output_dir / f"moving-newton-products.{extension}"
        options = {"dpi": 180} if extension == "png" else {}
        if extension == "pdf":
            options["metadata"] = {"CreationDate": None, "ModDate": None}
        elif extension == "svg":
            options["metadata"] = {"Date": None}
        fig.savefig(path, **options)
        paths.append(path)
    plt.close(fig)
    return paths, matplotlib.__version__


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=SCRIPT_DIR / "main_meridian_newton_algebra_results.json")
    parser.add_argument("--figure-dir", type=Path, default=ROOT / "book" / "figures")
    parser.add_argument("--skip-figure", action="store_true")
    args = parser.parse_args()
    result = {
        "scope": "Exact finite algebra checks and numerical bulk diagnostics; no knot-invariant estimate.",
        "versions": {"sympy": sp.__version__, "mpmath": mp.__version__},
        "arithmetic": {"exact": "rational polynomials and cyclotomic number fields",
                       "numerical_decimal_digits": 80},
        "exact_generic_multiplication": exact_generic_multiplication(),
        "exact_finite_connections": exact_connections(),
        "exact_mixed_duality": exact_cyclotomic_duality(),
        "bulk_factor_diagnostics": bulk_diagnostics(),
    }
    if not args.skip_figure:
        paths, version = draw_support(args.figure_dir)
        result["versions"]["matplotlib"] = version
        result["figures"] = {
            path.name: {"sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
            for path in paths
        }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "result": str(args.output),
        "generic_multiplication": result["exact_generic_multiplication"]["identities"],
        "connections": result["exact_finite_connections"]["identities"],
        "mixed_duality": sum(r["identities"] for r in result["exact_mixed_duality"]),
        "bulk_levels": [r["N"] for r in result["bulk_factor_diagnostics"]],
    }, indent=2))


if __name__ == "__main__":
    main()
