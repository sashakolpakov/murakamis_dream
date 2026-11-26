#!/usr/bin/env python3
"""Exact symbolic audit of the original first-three prefix provider.

The provider is imported only after frozen hashes are checked. Only its
generic gradient, Jacobian and Taylor-coefficient functions are called,
with Sympy symbols. No initialization, proposal or interval evaluation
is performed.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import sympy as s


ROOT = Path(__file__).resolve().parents[1]
PROVIDER = "experiments/mixed_second_selected_first_three_external_reference.py"
SPEC = "notes/research_mixed_second_selected_first_three_external_reference_evaluation.md"
THEORY = "notes/research_mixed_second_selected_first_three_extension.md"
ORIGINAL = "notes/research_mixed_prefix_residual_localization.md"
PINNED = {
    PROVIDER: "695ae91ad46581c74419e5ade992d7a233112761b88643199c9690a12b3df1d3",
    SPEC: "564710c4b10719fb0e81312e94289242cdc3857273d9d83b3dd1c965b490394f",
    THEORY: "d488ff98e01cfd5cd077de664c7e3bee3bfeeb735009f8c78f7c0ac60c7ad0e2",
    ORIGINAL: "5590b49394d112be5f5d23e7f20c31225bce8f1c19e6d3fd1dc3aa1ce40f0434",
}
NAMES = ("e", "xi", "a", "u", "z", "v", "b")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def original_log(argument):
    """Split positive rational factors only; no logarithmic branch rewrite."""
    coefficient, rest = argument.as_coeff_Mul()
    if coefficient.is_Rational and coefficient > 0:
        return s.log(coefficient) + s.log(rest)
    return s.log(argument)


def j(w):
    return original_log(2*s.sin(s.pi*w))


class OriginalJ(s.Function):
    nargs = 1

    def fdiff(self, argindex=1):
        if argindex != 1:
            raise ValueError("unexpected primitive argument")
        return j(self.args[0])


def original_phase(q, c, beta):
    """Original localization equation (2), with alpha exactly zero."""
    e, xi, a, u, z, v, b = q
    half = s.Rational(1, 2)
    phase = (-2*OriginalJ(half-xi)-3*OriginalJ(xi)-OriginalJ(e-xi)
             +OriginalJ(e+a)+OriginalJ(u+z)-OriginalJ(u)-OriginalJ(z)
             +OriginalJ(v+b)-beta*(OriginalJ(v)+OriginalJ(b))
             +OriginalJ(a+u)-2*OriginalJ(a)-2*OriginalJ(u)
             +OriginalJ(z+v)-2*OriginalJ(z)-2*OriginalJ(v)
             +OriginalJ(b+c)-2*OriginalJ(b))
    chirp = (e*xi-e*a+a*u-u*z+z*v-v*b+b*c
             +(u*u+z*z-u-z)/2+beta*(v*v+b*b-v-b)/2)
    return phase+s.I*s.pi*chirp, chirp


def zero(expression, label):
    difference = s.trigsimp(s.expand(expression))
    if difference != 0:
        raise ValueError((label, str(difference)))


def directional_zero(expression, predictors, label):
    """An affine-path second derivative is a quadratic polynomial in T.

    Its coefficients depend only on the original coordinate symbols.
    The predictors are algebraically independent, so vanishing of every
    coefficient is exactly the same identity as vanishing of the entire
    polynomial. No predictor or coordinate is specialized.
    """
    polynomial = s.Poly(s.expand(expression), *predictors, domain="EX")
    if not polynomial.is_zero and polynomial.total_degree() > 2:
        raise ValueError((label, "unexpected predictor degree"))
    for monomial, coefficient in polynomial.terms():
        zero(coefficient, (label, "predictor coefficient", monomial))
    return len(polynomial.terms())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    for name, digest in PINNED.items():
        if digest.startswith("PENDING") or sha(ROOT/name) != digest:
            raise ValueError("unfrozen symbolic input: "+name)
    bindings = dict(PINNED)
    bindings[str(Path(__file__).resolve().relative_to(ROOT))] = sha(Path(__file__))
    spec = importlib.util.spec_from_file_location("first_three_symbolic_provider", ROOT/PROVIDER)
    reference = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(reference)
    if tuple(reference.NAMES) != NAMES or reference._STATE is not None:
        raise ValueError("unexpected provider metadata or initialization")
    for name, digest in reference.PINNED.items():
        if name in bindings and bindings[name] != digest:
            raise ValueError("conflicting provider binding: "+name)
        if sha(ROOT/name) != digest:
            raise ValueError("provider binding changed: "+name)
        bindings[name] = digest

    q = s.symbols("e xi a u z v b")
    c = s.symbols("c")
    variables = (*q, c)
    T = (*s.symbols("T_e T_xi T_a T_u T_z T_v T_b"), s.Integer(1))
    forms = {name: s.Rational(constant.numerator, constant.denominator)
             +sum(a*x for a, x in zip(row, variables))
             for name, (constant, row) in reference.FORMS.items()}
    k = {name: s.pi*s.cos(s.pi*w)/s.sin(s.pi*w) for name, w in forms.items()}
    cases = []
    for beta in (0, 1):
        phase, chirp = original_phase(q, c, beta)
        original = [s.diff(phase, coordinate) for coordinate in q]
        provided = reference.gradient(q, c, beta, s.Integer, original_log,
                                      s.sin, s.cos, s.pi, s.I)
        H, fc = reference.jacobian_from_k(k, beta, s.pi, s.I)
        rows = reference.terms(beta)
        if len(provided) != 7 or len(rows) != 7:
            raise ValueError("wrong original gradient dimension")
        if rows[0] != ((-1, "e-xi"), (1, "e+a")):
            raise ValueError("first-three private Taylor row")
        if rows[2] != ((1, "e+a"), (1, "a+u"), (-2, "a")):
            raise ValueError("first-three attached Taylor row")
        coefficient_counts = []
        for i in range(7):
            zero(provided[i]-original[i], (beta, i, "original phase gradient"))
            reconstructed = sum(coefficient*j(forms[name]) for coefficient, name in rows[i])
            reconstructed += s.I*s.pi*s.diff(chirp, q[i])
            zero(reconstructed-original[i], (beta, i, "Taylor gradient decomposition"))
            for n in range(7):
                zero(s.diff(original[i], q[n])-H[i][n], (beta, i, n, "Jacobian"))
                zero(H[i][n]-H[n][i], (beta, i, n, "symmetry"))
            zero(s.diff(original[i], c)-fc[i], (beta, i, "external derivative"))
            first = sum(s.diff(original[i], w)*t for w, t in zip(variables, T))
            second = sum(s.diff(first, w)*t for w, t in zip(variables, T))
            modeled = 0
            for coefficient, name in rows[i]:
                direction = sum(s.diff(forms[name], w)*t for w, t in zip(variables, T))
                modeled -= coefficient*s.pi**2*direction**2/s.sin(s.pi*forms[name])**2
            coefficient_counts.append(directional_zero(
                second-modeled, T[:-1],
                (beta, i, "full affine directional second derivative")))
        cases.append({"alpha": 0, "beta": beta, "original_phase_gradient_rows": 7,
                      "jacobian_entries": 49, "external_derivatives": 7,
                      "taylor_decomposition_rows": 7, "directional_second_derivatives": 7,
                      "directional_coefficient_counts": coefficient_counts,
                      "symmetric_jacobian": True,
                      "taylor_rows": [[{"coefficient": a, "argument": name}
                                       for a, name in row] for row in rows]})
    if reference._STATE is not None:
        raise ValueError("symbolic check initialized the numerical provider")
    for name, digest in bindings.items():
        if sha(ROOT/name) != digest:
            raise ValueError("symbolic-check input changed: "+name)
    record = {"status": "all first-three original-gradient and Taylor identities proved symbolically",
              "alpha": 0, "cases": cases, "identity_count_excluding_symmetry": 154,
              "directional_simplification": "exact coefficients of the quadratic polynomial in seven independent predictors",
              "directional_coefficients_checked": sum(sum(case["directional_coefficient_counts"]) for case in cases),
              "input_sha256": bindings, "sympy_version": s.__version__,
              "original_primitive_branch": "j=Log(2 sin(pi w)); only positive real factor 2 is split",
              "provider_initializations": 0, "root_evaluations": 0,
              "floating_parameter_or_interval_evaluations": 0,
              "finite_source_evaluations": 0,
              "scope": "analytic derivative identities only; no reference existence or scalar signs inferred"}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as stream:
        json.dump(record, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps({"status": record["status"], "identities": 154,
                      "output_sha256": sha(args.output)}))


if __name__ == "__main__":
    main()
