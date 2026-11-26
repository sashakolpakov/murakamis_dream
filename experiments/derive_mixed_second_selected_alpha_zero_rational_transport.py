#!/usr/bin/env python3
"""Exact canceled second-selection shapes in Q(W), first type three.

This is algebra only: no parameter, interval, root, primitive or source
evaluation. The frozen Rational implementation is loaded after its hash
has been checked; its original main program is never called.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import time


REPO = Path(__file__).resolve().parents[1]
IMPLEMENTATION = "experiments/derive_mixed_second_selected_rational_transport.py"
PINNED = {
    IMPLEMENTATION: "71d5fd6d67229b69aaea53cc9e1c540ceb01a68e7fb0d126d2f8d63e8651470a",
    "notes/research_mixed_second_selected_reference_curve.md": "4a591366418d251cbcfaad5705ff439747a8745cc8e75f64561e70aec3ef5bd5",
    "notes/research_mixed_rational_critical_transport.md": "0cba78ed20d7e98d65414b61a96412a8ee6f3e43b766d7d10f9900ea36a96635",
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


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
            raise ValueError("frozen exact-algebra input mismatch: "+name)

    spec = importlib.util.spec_from_file_location(
        "_frozen_second_selected_rational_algebra", REPO/IMPLEMENTATION)
    algebra = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(algebra)
    # No call to the original main, frozen-map reader, or parameter code.
    Rational, W = algebra.Rational, algebra.W
    started = time.monotonic()
    w = Rational(W)
    E = (1+w)**2/(5*w**2-2*w+1)
    A = (1-(1-E*w)/w)/E
    U = (1-E*A)/(A*(1-E*A)+(1-A)**2)
    Z = (1-A*(1-U)**3/(1-A*U))/U
    V = (1-U*Z)/(Z*(1-U*Z)+(1-Z)**3)
    values = dict(E=E, A=A, U=U, Z=Z, V=V)

    # Independent initial formulas from rational_critical_transport Eq(4).
    A_explicit = ((3*w-1)*(2*w**2-w+1))/(w*(w+1)**2)
    U_explicit = ((1-w)*(1+w)**4)/(
        (7*w**2-6*w+3)*(17*w**3-7*w**2+7*w-1))
    identities = {
        "explicit_alpha_zero_attached_map": A.equals(A_explicit),
        "explicit_alpha_zero_adjacent_map": U.equals(U_explicit),
        "endpoint_E_cross_product": (E*(5*w**2-2*w+1)).equals((1+w)**2),
        "endpoint_auxiliary_original": ((1+w)**2*(1-E*w)).equals(E*(1-w)**3),
        "endpoint_private_original_alpha_zero": (w*(1-E*A)).equals(1-E*w),
        "endpoint_attached_original_alpha_zero":
            ((1-E*A)*(1-U*A)).equals(U*(1-A)**2),
        "endpoint_adjacent_cross_product":
            (U*(A*(1-E*A)+(1-A)**2)).equals(1-E*A),
        "first_retained_cross_product":
            (Z*U*(1-A*U)).equals((1-A*U)-A*(1-U)**3),
        "first_external_cross_product":
            (V*(Z*(1-U*Z)+(1-Z)**3)).equals(1-U*Z),
        "first_index_original": ((1-A*U)*(1-U*Z)).equals(A*(1-U)**3),
        "first_retained_original": ((1-U*Z)*(1-V*Z)).equals(V*(1-Z)**3),
    }
    derivation_times = {"through_V": time.monotonic()-started}
    for beta in (0, 1):
        before = time.monotonic()
        power = 2+beta
        B = (1-Z*(1-V)**power/(1-Z*V))/V
        C = (1-V*B)/(B*(1-V*B)+(1-B)**power)
        values["B"+str(beta)], values["C"+str(beta)] = B, C
        identities["second_retained_cross_product_beta"+str(beta)] = (
            B*V*(1-Z*V)).equals((1-Z*V)-Z*(1-V)**power)
        identities["second_external_cross_product_beta"+str(beta)] = (
            C*(B*(1-V*B)+(1-B)**power)).equals(1-V*B)
        identities["second_index_original_beta"+str(beta)] = (
            (1-Z*V)*(1-V*B)).equals(Z*(1-V)**power)
        identities["second_retained_original_beta"+str(beta)] = (
            (1-V*B)*(1-C*B)).equals(C*(1-B)**power)
        derivation_times["beta"+str(beta)] = time.monotonic()-before
    if not all(identities.values()):
        raise AssertionError("original alpha-zero identity failed")

    maps = {name: algebra.rational_record(name, value)
            for name, value in values.items()}
    # rational_record checks coprimality, reconstructs every exact factor
    # list, and cross-multiplies each derivative against the quotient rule.
    factors = {tuple(factor["coefficients_descending"])
               for shape in maps.values()
               for source in (shape, shape["derivative"])
               for part in ("numerator", "denominator")
               for factor in source[part]["factors"]}
    degrees = [len(coefficients)-1 for coefficients in factors]
    factor_summary = {
        "unique_nonconstant_polynomials": len(factors),
        "maximum_degree": max(degrees),
        "degree_sum": sum(degrees),
        "integer_shift_multiplication_bound": sum(d*(d+1)//2 for d in degrees),
    }
    for name, expected in bindings.items():
        if digest(REPO/name) != expected:
            raise RuntimeError("input changed during exact algebra: "+name)
    result = {
        "status": "exact rational identities proved", "ring": "Q(W)", "alpha": 0,
        "shape_convention": "W positive endpoint sign; E,A,U,Z,V,B,C negative leg signs",
        "shape_order": "E=e, A=a, U=u, Z=z, V=v, B=b, C=c",
        "ordinary_own_type": 4, "beta_candidates": [0, 1],
        "maps": maps, "identity_checks": identities,
        "derivation_seconds": derivation_times,
        "operation_counts": dict(algebra.OPERATIONS),
        "factor_summary": factor_summary,
        "elapsed_seconds": time.monotonic()-started,
        "sympy_version": algebra.sp.__version__,
        "parameter_value_evaluations": 0, "interval_reference_evaluations": 0,
        "primitive_evaluations": 0, "root_solves": 0,
        "finite_source_evaluations": 0, "selected_source_sign_claimed": False,
        "original_alpha_one_main_called": False, "input_sha256": bindings,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as output:
        output.write(json.dumps(result, indent=2)+"\n")
    print(json.dumps({
        "status": result["status"], "elapsed_seconds": result["elapsed_seconds"],
        "record_sha256": digest(args.output), "identity_count": len(identities),
        "factor_summary": factor_summary, "operation_counts": result["operation_counts"],
    }), flush=True)


if __name__ == "__main__":
    main()
