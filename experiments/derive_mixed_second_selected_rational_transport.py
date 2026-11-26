#!/usr/bin/env python3
"""Derive canceled second-selection shapes exactly in Q(W), alpha=1.

Integer polynomial arithmetic and exact factorization only. No parameter
value, interval reference, transcendental primitive, root or source is run.
"""
import argparse
import ast
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time

import sympy as sp


REPO = Path(__file__).resolve().parents[1]
PINNED = {
    "notes/research_mixed_second_selected_reference_curve.md": "4a591366418d251cbcfaad5705ff439747a8745cc8e75f64561e70aec3ef5bd5",
    "experiments/certify_mixed_endpoint_log_budget.py": "b8306df590b8b4c90e4e230845245658bc5695d8355c6e63779aba50973c75b2",
    "experiments/certify_mixed_next_four_endpoint_budget.py": "079d452389081a400235fd27aa0f0afbb68b91113943cb0eb9250be904b2e11f",
    "notes/research_mixed_second_selected_centered_reference_evaluation.md": "e62b6e2ad427b10fe16944ab9551918e85b8f35d2116bab313216605163dfaea",
    "repro/results/research-mixed-second-selected-centered-reference-diagnostic.json": "368bc80f65b30971f2b742d5f52a71b8bdc2da4cc6b2fc6ba74a0d8a05411719",
}
W = sp.Symbol("W")
OPERATIONS = {"normalizations": 0, "nonconstant_gcd_cancellations": 0,
              "largest_precancellation_numerator_degree": 0,
              "largest_precancellation_denominator_degree": 0}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def poly(value):
    return value if isinstance(value, sp.Poly) else sp.Poly(value, W, domain=sp.ZZ)


class Rational:
    """Canonical coprime integer-polynomial numerator and denominator."""
    def __init__(self, numerator, denominator=1):
        n, d = poly(numerator), poly(denominator)
        if d.is_zero:
            raise ZeroDivisionError("identically zero polynomial denominator")
        OPERATIONS["normalizations"] += 1
        if not n.is_zero:
            OPERATIONS["largest_precancellation_numerator_degree"] = max(
                OPERATIONS["largest_precancellation_numerator_degree"], int(n.degree()))
        OPERATIONS["largest_precancellation_denominator_degree"] = max(
            OPERATIONS["largest_precancellation_denominator_degree"], int(d.degree()))
        gcd = sp.gcd(n, d)
        if gcd.degree() > 0:
            OPERATIONS["nonconstant_gcd_cancellations"] += 1
        n, d = n.exquo(gcd), d.exquo(gcd)
        if d.LC() < 0:
            n, d = -n, -d
        self.n, self.d = n, d

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Rational) else Rational(value)

    def __add__(self, other):
        other = self.coerce(other)
        return Rational(self.n*other.d+other.n*self.d, self.d*other.d)

    __radd__ = __add__

    def __neg__(self):
        return Rational(-self.n, self.d)

    def __sub__(self, other):
        return self+(-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other)-self

    def __mul__(self, other):
        other = self.coerce(other)
        return Rational(self.n*other.n, self.d*other.d)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.coerce(other)
        if other.n.is_zero:
            raise ZeroDivisionError("division by identically zero rational function")
        return Rational(self.n*other.d, self.d*other.n)

    def __rtruediv__(self, other):
        return self.coerce(other)/self

    def __pow__(self, exponent):
        if not isinstance(exponent, int) or exponent < 0:
            raise ValueError("only nonnegative integer powers are used")
        return Rational(self.n**exponent, self.d**exponent)

    def equals(self, other):
        other = self.coerce(other)
        return (self.n*other.d-other.n*self.d).is_zero

    def derivative(self):
        return Rational(self.n.diff()*self.d-self.n*self.d.diff(), self.d**2)


def literal_frozen_maps():
    """Read only integer factorizations from the frozen source AST."""
    tree = ast.parse((REPO/"experiments/certify_mixed_endpoint_log_budget.py").read_text())
    maps = next(ast.literal_eval(node.value) for node in tree.body
                if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name)
                and node.targets[0].id == "MAPS")
    tree = ast.parse((REPO/"experiments/certify_mixed_next_four_endpoint_budget.py").read_text())
    for node in tree.body:
        if not isinstance(node, ast.Assign) or not isinstance(node.targets[0], ast.Subscript):
            continue
        target = node.targets[0]
        if isinstance(target.value, ast.Name) and target.value.id == "MAPS":
            maps[ast.literal_eval(target.slice)] = ast.literal_eval(node.value)
    return maps


def product_from_factors(factors):
    result = poly(1)
    for power, coefficients in factors:
        result *= sp.Poly.from_list(coefficients, W, domain=sp.ZZ)**power
    return result


def factor_record(p):
    coefficient, factors = sp.factor_list(p)
    reconstructed = poly(coefficient)
    rows = []
    for factor, power in factors:
        reconstructed *= factor**power
        rows.append({"power": int(power), "degree": int(factor.degree()),
                     "coefficients_descending": list(map(int, factor.all_coeffs()))})
    if reconstructed != p:
        raise AssertionError("exact factor reconstruction failed")
    return {"degree": int(p.degree()), "content": int(coefficient), "factors": rows,
            "coefficients_descending": list(map(int, p.all_coeffs()))}


def rational_record(name, value):
    started = time.monotonic()
    if sp.gcd(value.n, value.d).degree() != 0:
        raise AssertionError("rational function not canceled")
    result = {"numerator": factor_record(value.n), "denominator": factor_record(value.d)}
    derivative = value.derivative()
    result["derivative"] = {"numerator": factor_record(derivative.n),
                            "denominator": factor_record(derivative.d)}
    # Independent cross-multiplied quotient-rule check.
    if not (derivative.n*value.d**2-
            (value.n.diff()*value.d-value.n*value.d.diff())*derivative.d).is_zero:
        raise AssertionError("derivative identity failed")
    result["factorization_and_derivative_seconds"] = time.monotonic()-started
    print(json.dumps({"shape": name, "degrees": [result[part]["degree"] for part in ("numerator", "denominator")],
        "factor_degrees": {part: [[factor["degree"], factor["power"]] for factor in result[part]["factors"]]
                           for part in ("numerator", "denominator")},
        "seconds": result["factorization_and_derivative_seconds"]}), flush=True)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    bindings = dict(PINNED)
    bindings[str(Path(__file__).resolve().relative_to(REPO))] = digest(Path(__file__))
    for name, expected in bindings.items():
        if digest(REPO/name) != expected:
            raise ValueError("frozen symbolic input mismatch: "+name)
    started = time.monotonic()
    w = Rational(W)
    E = (1+w)**2/(5*w**2-2*w+1)
    A = (1-(1-E*w)*(1-E)/w)/E
    U = (1-E*A)/(A*(1-E*A)+(1-A)**3)
    Z = (1-A*(1-U)**3/(1-A*U))/U
    V = (1-U*Z)/(Z*(1-U*Z)+(1-Z)**3)
    values = dict(E=E, A=A, U=U, Z=Z, V=V)
    identities = {}
    frozen = literal_frozen_maps()
    for name, key in (("E", "e"), ("A", "z"), ("U", "s"), ("Z", "b")):
        expected = Rational(product_from_factors(frozen[key][0]), product_from_factors(frozen[key][1]))
        identities["frozen_"+name] = values[name].equals(expected)
    identities["first_retained_cross_product"] = (Z*U*(1-A*U)).equals((1-A*U)-A*(1-U)**3)
    identities["first_external_cross_product"] = (V*(Z*(1-U*Z)+(1-Z)**3)).equals(1-U*Z)
    derivation_times = {"through_V": time.monotonic()-started}
    for beta in (0, 1):
        before = time.monotonic()
        power = 2+beta
        B = (1-Z*(1-V)**power/(1-Z*V))/V
        C = (1-V*B)/(B*(1-V*B)+(1-B)**power)
        values["B"+str(beta)], values["C"+str(beta)] = B, C
        identities["second_retained_beta"+str(beta)] = (B*V*(1-Z*V)).equals((1-Z*V)-Z*(1-V)**power)
        identities["second_external_beta"+str(beta)] = (C*(B*(1-V*B)+(1-B)**power)).equals(1-V*B)
        derivation_times["beta"+str(beta)] = time.monotonic()-before
    if not all(identities.values()):
        raise AssertionError("original transfer identity failed")
    maps = {name: rational_record(name, value) for name, value in values.items()}
    for name, expected in bindings.items():
        if digest(REPO/name) != expected:
            raise RuntimeError("input changed during exact algebra: "+name)
    record = {
        "status": "exact rational identities proved", "ring": "Q(W)", "alpha": 1,
        "shape_convention": "W positive endpoint sign; E,A,U,Z,V,B,C negative leg signs",
        "shape_order": "E=e, A=a, U=u, Z=z, V=v, B=b, C=c",
        "beta_candidates": [0, 1], "maps": maps, "identity_checks": identities,
        "derivation_seconds": derivation_times, "operation_counts": OPERATIONS,
        "elapsed_seconds": time.monotonic()-started, "sympy_version": sp.__version__,
        "parameter_value_evaluations": 0, "interval_reference_evaluations": 0,
        "primitive_evaluations": 0, "root_solves": 0, "finite_source_evaluations": 0,
        "selected_source_sign_claimed": False, "input_sha256": bindings,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as output:
        output.write(json.dumps(record, indent=2)+"\n")
    print(json.dumps({"status": record["status"], "elapsed_seconds": record["elapsed_seconds"],
        "record_sha256": digest(args.output), "identity_checks": identities,
        "derivation_seconds": derivation_times, "operation_counts": OPERATIONS}), flush=True)


if __name__ == "__main__":
    main()
