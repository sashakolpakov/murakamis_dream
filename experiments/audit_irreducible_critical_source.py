#!/usr/bin/env python3
"""Exact source trace and whole-presentation diagnostics.

These are algebraic checks of the universal theorem in the linked note,
not evidence that its critical trace quotient exists for the knot.
"""

import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp


def trace_density():
    t, Q, z = sp.symbols("t Q z")
    # Multiplication by theta, theta^3-theta-1=0. This irreducible
    # polynomial has no rational root and discriminant -23.
    theta = sp.Matrix([[0, 0, 1], [1, 0, 1], [0, 1, 0]])
    assert theta**3-theta-sp.eye(3) == sp.zeros(3)
    gram = sp.Matrix(3, 3, lambda i, j: sp.trace(theta**(i+j)))
    assert gram.det() == -23
    moments = sp.Matrix([1, Q-1, t])
    coefficients = gram.inv()*moments
    density = sum((coefficients[i]*theta**i for i in range(3)), sp.zeros(3))
    assert sp.trace(density) == 1
    for j in range(3):
        assert sp.cancel(sp.trace(theta**j*density)-moments[j]) == 0
    norm = sp.factor(density.det())
    assert norm != 0
    density_polynomial = sum(coefficients[i]*z**i for i in range(3))

    mp.mp.dps = 90
    roots = [mp.mpc(str(sp.re(root).evalf(90)), str(sp.im(root).evalf(90)))
             for root in sp.nroots(z**3-z-1, n=90, maxsteps=100)]
    density_function = sp.lambdify((t, Q, z), density_polynomial, "mpmath")
    norm_function = sp.lambdify((t, Q), norm, "mpmath")
    numeric = []
    for N in (8, 16, 32, 64, 128):
        root = mp.exp(2j*mp.pi/N)
        values = [density_function(mp.mpf(1)/N, root, a) for a in roots]
        assert min(abs(a) for a in values) > mp.mpf("0.01")
        assert abs(mp.fprod(values)-norm_function(mp.mpf(1)/N, root)) < mp.mpf("1e-75")
        # An exact finite exponential model tests that all three trace
        # weights occur and the unique largest action is retained.
        actions = (1, 0, -1)
        period = sum(a*mp.exp(N*s) for a, s in zip(values, actions))
        relative = period/(values[0]*mp.exp(N))-1
        assert abs(relative) < 20*mp.exp(-N)
        numeric.append({"N": N,
                        "least_conjugate_source_modulus": str(min(abs(a) for a in values)),
                        "dominant_sector_relative_error": str(abs(relative))})
    return {"trace_gram": str(gram), "discriminant": int(gram.det()),
            "reconstructed_density": str(density_polynomial),
            "density_norm": str(norm),
            "exact_moments_and_trace_normalization": True,
            "physical_arc_and_trace_period_model": numeric}


def faithful_trace():
    r = sp.sqrt(2)
    block = sp.Matrix([[0, 2], [1, 0]])
    theta = sp.diag(block, block, 3, 3, 3)
    eye = sp.eye(7)
    eigenvalues = [r, -r, sp.Integer(3)]
    projectors = []
    traces = []
    for a in eigenvalues:
        projector = eye
        for b in eigenvalues:
            if a != b:
                projector = projector*(theta-b*eye)/(a-b)
        projector = projector.applyfunc(sp.simplify)
        assert (projector**2-projector).applyfunc(sp.simplify) == sp.zeros(7)
        projectors.append(projector)
        traces.append(int(sp.simplify(sp.trace(projector))))
    assert sum(projectors, sp.zeros(7)) == eye
    assert traces == [2, 2, 3]
    return {"faithful_dimension": 7, "primitive_projector_ranks": traces,
            "normalized_weights": [str(sp.Rational(rank, 7)) for rank in traces],
            "all_projectors_exact_and_visible": True}


def exponential_polynomial_order():
    # Derivatives of t^j exp(a t) at zero are falling(r,j)*a^(r-j).
    basis = [(a, j) for a, degree in [(-1, 1), (0, 2), (2, 0)]
             for j in range(degree+1)]
    dimension = len(basis)
    jets = sp.Matrix(dimension, dimension,
                     lambda r, k: 0 if r < basis[k][1] else
                     sp.factorial(r)/sp.factorial(r-basis[k][1])
                     *sp.Integer(basis[k][0])**(r-basis[k][1]))
    assert jets.det() != 0
    null = jets[:-1, :].nullspace()
    assert len(null) == 1
    sharp = null[0]
    assert jets[:-1, :]*sharp == sp.zeros(dimension-1, 1)
    assert (jets[-1, :]*sharp)[0] != 0
    return {"exponential_polynomial_dimension": dimension,
            "confluent_jet_determinant": int(jets.det()),
            "sharp_zero_order": dimension-1,
            "sharp_linear_combination": [str(a) for a in sharp],
            "order_bound_and_arc_independence_exact": True}


def height_and_scope_checks():
    cauchy_cases = 0
    for degree in range(2, 9):
        for height in range(1, 5):
            coefficients = [1]+[(((-1)**j)*(1+(j % height)))
                                for j in range(1, degree)]+[-height]
            H = max(abs(c) for c in coefficients)
            roots = np.roots(coefficients)
            assert min(abs(z) for z in roots) >= 1/(1+H)-1e-10
            assert max(abs(z) for z in roots) <= 1+H+1e-10
            cauchy_cases += 1
    pisot_cases = []
    for N in (2, 3, 4, 6, 8):
        A = 2**N
        coefficients = [1, -A]+[0]*(N-2)+[-2]
        roots = np.roots(coefficients)
        outside = [root for root in roots if abs(root) >= 1]
        assert len(outside) == 1
        alpha = mp.mpf(A)
        for _ in range(40):
            alpha = A+2/alpha**(N-1)
        assert A < alpha < A+1
        contraction = 2*(N-1)/(A-2)**N
        assert contraction < 1
        # Exact Eisenstein data at two; constant term is not divisible by4.
        assert all(c % 2 == 0 for c in coefficients[1:])
        assert coefficients[-1] % 4 != 0
        pisot_cases.append({"degree": N, "large_root": str(alpha),
                            "Weil_height": str(mp.log(alpha)/N),
                            "normal_log_modulus": str(mp.log(alpha)/N),
                            "outside_unit_disk_roots": len(outside),
                            "contraction_constant": contraction})
    # Fixed field and normalized trace do not control level-dependent height.
    r = sp.sqrt(2)
    for N in range(2, 10):
        a = (1+2**N*r)/2
        conjugate = (1-2**N*r)/2
        assert sp.simplify(a+conjugate-1) == 0
        assert sp.simplify(4*a*a-4*a+1-2*4**N) == 0
    return {"absolute_naive_height_root_bound_cases": cauchy_cases,
            "bounded_Weil_height_large_embedding_examples": pisot_cases,
            "fixed_field_trace_one_exponential_height_examples": 8,
            "split_projection_counterexample": {"source": [1, 1],
                                                 "cosource": [0, 1],
                                                 "normalization": 1,
                                                 "first_sector_weight": 0}}


def main():
    result = {"irreducible_moment_reconstruction": trace_density(),
              "faithful_trace_realization": faithful_trace(),
              "physical_arc_order_certificate": exponential_polynomial_order(),
              "height_and_scope": height_and_scope_checks(),
              "scope": "Universal algebraic source theorem; actual knot critical quotient/trace descent and global action gap remain to prove."}
    target = Path(__file__).with_name("irreducible_critical_source_results.json")
    target.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"exact_trace_field_and_moment_reconstruction": True,
                      "faithful_trace_projector_weights": result["faithful_trace_realization"]["normalized_weights"],
                      "exact_exponential_polynomial_dimension": result["physical_arc_order_certificate"]["exponential_polynomial_dimension"],
                      "height_root_bound_cases": result["height_and_scope"]["absolute_naive_height_root_bound_cases"],
                      "output": str(target)}, indent=2))


if __name__ == "__main__":
    main()
