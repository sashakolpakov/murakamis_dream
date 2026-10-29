#!/usr/bin/env python3
"""Exact global two-chart source, endpoint, and whole weighted-dual checks."""

import json
from functools import lru_cache
from pathlib import Path

import sympy as sp


z, w, q, m, U = sp.symbols("z w q m U", nonzero=True)


def coefficient(f, exponent):
    numerator, denominator = sp.fraction(sp.cancel(f))
    terms = sp.Poly(denominator, z).terms()
    assert len(terms) == 1
    (shift,), scalar = terms[0]
    power = exponent+shift
    if power < 0:
        return sp.Integer(0)
    return sp.cancel(sp.Poly(numerator, z).coeff_monomial(z**power)/scalar)


def residue(f):
    return coefficient(f, -1)


def split(f, predicate):
    return sp.expand(sum(term for term in sp.Add.make_args(sp.expand(f))
                         if predicate(int(term.as_powers_dict().get(z, 0)))))


def d_dual(pair, N):
    north, south = map(sp.sympify, pair)
    return sp.expand(z**(-N-2)*south.subs(w, 1/z)-north)


def h_dual(c, N):
    north = -split(c, lambda k: k >= 0)
    south = (z**(N+2)*split(c, lambda k: k <= -N-2)).subs(z, 1/w)
    return sp.expand(north), sp.expand(south)


def middle(c, N):
    return split(c, lambda k: -N-1 <= k <= -1)


def d_source(pair, N):
    north, south = map(sp.sympify, pair)
    return sp.expand(z**N*south.subs(w, 1/z)-north)


def h_source(c, N):
    north = -split(c, lambda k: k > N)
    south = (z**(-N)*split(c, lambda k: k <= N)).subs(z, 1/w)
    return sp.expand(north), sp.expand(south)


def source_operators(N):
    return (lambda f: sp.diff(f, z),
            lambda f: sp.expand(N*z*f-z*z*sp.diff(f, z)),
            lambda f: sp.expand(N*f-2*z*sp.diff(f, z)))


def dual_operators(N):
    return (lambda c: -sp.diff(c, z),
            lambda c: sp.expand(z*z*sp.diff(c, z)+(N+2)*z*c),
            lambda c: sp.expand(2*z*sp.diff(c, z)+(N+2)*c))


def cech_case(N):
    e, f, h = source_operators(N)
    ed, fd, hd = dual_operators(N)
    source = sum((k+1)*sp.binomial(N, k)*z**k for k in range(N+1))
    row = [2*k*k-k+3 for k in range(N+1)]
    dual = sum(sp.Rational(row[k], sp.binomial(N, k))*z**(-k-1) for k in range(N+1))
    assert residue(source*dual) == sum((k+1)*row[k] for k in range(N+1))
    for operator, adjoint in zip((e, f, h), (ed, fd, hd)):
        assert sp.expand(residue(dual*operator(source))-residue(adjoint(dual)*source)) == 0

    c = sum((k*k+2)*z**k for k in range(-N-5, 5))
    assert sp.expand(d_dual(h_dual(c, N), N)+middle(c, N)-c) == 0
    pair = (z**3+2*z+1, w**4-3*w+2)
    assert all(sp.expand(a-b) == 0 for a, b in zip(h_dual(d_dual(pair, N), N), pair))
    for adjoint in (ed, fd, hd):
        # piD=Dmatrix*pi, so the concrete natural-lift residual is a boundary.
        induced = middle(adjoint(middle(c, N)), N)
        assert sp.expand(adjoint(c)-induced-d_dual(h_dual(adjoint(c), N), N)) == 0

    b = sum((k+2)*z**k for k in range(-4, N+4))
    assert sp.expand(d_source(h_source(b, N), N)-b) == 0
    source_pair = (z**(N+3)+z**N+2, w**3+w+1)
    projected = split(source_pair[0], lambda k: 0 <= k <= N)
    iota_projected = (projected, w**N*projected.subs(z, 1/w))
    hsds = h_source(d_source(source_pair, N), N)
    assert all(sp.expand(a-b+c) == 0 for a, b, c in zip(hsds, source_pair, iota_projected))
    dual_pair = (z*z+3, w*w-w+2)
    stokes = residue(d_source(source_pair, N)*z**(-N-2)*dual_pair[1].subs(w, 1/z))
    stokes += residue(source_pair[0]*d_dual(dual_pair, N))
    assert sp.expand(stokes) == 0

    assert sp.expand(fd(z**-1)-d_dual((-(N+1), sp.Integer(0)), N)) == 0
    assert sp.expand(ed(z**(-N-1))-d_dual((sp.Integer(0), N+1), N)) == 0
    # A finite matrix annihilator need not vanish as a cochain operator,
    # but its full action is the explicit nonzero endpoint homotopy.
    annihilator = dual
    for _ in range(N+1):
        annihilator = ed(annihilator)
    assert middle(annihilator, N) == 0 and annihilator != 0
    assert sp.expand(annihilator-d_dual(h_dual(annihilator, N), N)) == 0

    xi = sp.Integer(2)
    infinity = w**N*source.subs(z, 1/w)
    assert sp.expand(w**N*source.subs(z, xi/w)-xi**N*infinity.subs(w, w/xi)) == 0
    dual_clock = xi**-1*dual.subs(z, z/xi)
    assert sp.expand(residue(dual*source.subs(z, xi*z))-residue(dual_clock*source)) == 0
    assert sp.expand(residue(xi*dual.subs(z, xi*z)*source.subs(z, xi*z))-residue(dual*source)) == 0
    transformed_pair = (xi**-1*dual_pair[0].subs(z, z/xi),
                        xi**(N+1)*dual_pair[1].subs(w, xi*w))
    assert sp.expand(d_dual(transformed_pair, N)-xi**-1*d_dual(dual_pair, N).subs(z, z/xi)) == 0

    # Literal Serre trace, not rank-one expectation, on a nondiagonal operator.
    trace = 0
    for k in range(N+1):
        basis = sp.binomial(N, k)*z**k
        D_basis = e(f(basis))+h(h(basis))
        trace += residue(z**(-k-1)/sp.binomial(N, k)*D_basis)
    e_mat = sp.zeros(N+1)
    f_mat = sp.zeros(N+1)
    h_mat = sp.diag(*[N-2*k for k in range(N+1)])
    for k in range(1, N+1):
        e_mat[k-1, k], f_mat[k, k-1] = N-k+1, k
    assert trace == sp.trace(e_mat*f_mat+h_mat*h_mat)

    f_alpha = U*(1+z)**N
    c_pair = sum((1-m)**k*(1+m)**(N-k)*z**(-k-1) for k in range(N+1))/(2**N*U)
    assert sp.expand(residue(c_pair*f_alpha)-1) == 0
    assert sp.expand(residue(c_pair*h(f_alpha))/N-m) == 0
    assert residue(2**(-sp.Integer(N))*sum(z**(-k-1) for k in range(N+1))*f_alpha) == U
    averaged_class = sp.integrate(c_pair.subs(U, 1), (m, -1, 1))/2
    uniform_class = sum(z**(-k-1)/((N+1)*sp.binomial(N, k)) for k in range(N+1))
    assert sp.cancel(averaged_class-uniform_class) == 0
    return {"N": N, "source_dual_contractions_and_Stokes_exact": True,
            "actual_global_operator_residue_and_trace_exact": True,
            "named_north_south_endpoint_homotopies_exact": True,
            "whole_clock_line_factors_exact": True,
            "global_Borel_source_scale_descendant_residues_exact": True}


def whole_actual_uniform_source(N=2, residue_string=0):
    # Actual integral D_(N(N+1)-1), with constant beta gauge, over Q(q).
    r = N
    highest = N*(N+1)-1
    Q = q*q

    @lru_cache(None)
    def gaussian(a, k):
        if k < 0 or k > a:
            return sp.Integer(0)
        if k == 0 or k == a:
            return sp.Integer(1)
        return sp.expand(gaussian(a-1, k)+Q**(a-k)*gaussian(a-1, k-1))

    def symmetric(a, k):
        return sp.expand(q**(-k*(a-k))*gaussian(a, k))

    beta = [(-1)**(N*k*(k-1)//2+k*residue_string) for k in range(r+1)]
    actual_E, actual_F = sp.zeros(r+1), sp.zeros(r+1)
    tau = (-1)**(N*r-1)
    for k in range(r+1):
        index = k*N+residue_string
        if k:
            actual_E[k-1, k] = tau*beta[k]*beta[k-1]*symmetric(highest-index+N, N)
        if k < r:
            actual_F[k+1, k] = beta[k]*beta[k+1]*symmetric(index+N, N)
    expE, expF = sp.eye(r+1), sp.eye(r+1)
    for k in range(1, r+1):
        expE += actual_E**k/sp.factorial(k)
        expF += actual_F**k/sp.factorial(k)
    psi = expF[:, 0].applyfunc(sp.expand)
    c = expE[0, :]
    tilde = sp.Matrix([[sp.expand(c[k]*((1+m)/2)**(N-k)*((1-m)/2)**k)
                        for k in range(r+1)]])
    pairing_unit = sp.expand((tilde*psi)[0])
    assert sp.expand(pairing_unit-1) != 0
    L = tilde.applyfunc(lambda x: sp.integrate(x, (m, -1, 1))/2)
    for k in range(r+1):
        assert sp.cancel(L[k]-c[k]/((N+1)*sp.binomial(N, k))) == 0
    uniform = sp.ones(1, r+1)/(N+1)
    nu, V = sp.expand((uniform*psi)[0]), sp.expand((L*psi)[0])
    assert sp.simplify(nu.subs(q, sp.I)-1) == 0
    assert sp.simplify(V.subs(q, sp.I)-1) == 0
    assert all(sp.simplify(x.subs(q, sp.I)-1) == 0 for x in psi)
    Delta = L/V-uniform/nu
    assert sp.cancel((Delta*psi)[0]) == 0
    K = sp.eye(r+1)+psi*Delta
    K_inverse = sp.eye(r+1)-psi*Delta
    for point in (sp.Integer(2), sp.Rational(3, 2)):
        actual_K = K.subs(q, point)
        actual_inverse = K_inverse.subs(q, point)
        assert actual_K*actual_inverse == sp.eye(r+1)
        assert actual_K*psi.subs(q, point) == psi.subs(q, point)
        assert ((uniform/nu).subs(q, point)*actual_K-(L/V).subs(q, point)) == sp.zeros(1, r+1)
        assert actual_K.det() == 1
    assert (K.subs(q, sp.I)-sp.eye(r+1)).applyfunc(sp.simplify) == sp.zeros(r+1)
    # Both co-sources are represented by the actual global Laurent classes.
    psi_polynomial = sum(psi[k]*sp.binomial(N, k)*z**k for k in range(r+1))
    c_L = sum((L[k]/V)/sp.binomial(N, k)*z**(-k-1) for k in range(r+1))
    residue_error = sp.cancel(residue(c_L*psi_polynomial)-1)
    assert residue_error == 0, sp.factor(residue_error)
    return {"N": N, "residue_string": residue_string,
            "whole_actual_pairing_unit_is_nonconstant": True,
            "retained_weight_beta_integral_is_exact_rational": True,
            "nu_and_V_have_root_value_one": True,
            "whole_rational_unipotent_gauge_and_inverse_exact": True,
            "actual_source_fixed_and_global_residue_pairing_preserved": True}


def main():
    result = {"global_source_cech_cases": [cech_case(N) for N in (2, 3, 4, 5)],
              "whole_actual_uniform_source_comparison": [whole_actual_uniform_source(2, s) for s in (0, 1)],
              "scope": "Exact whole algebraic source localization and retained-weight comparison; no endpoint norm or internal geometric-current theorem."}
    target = Path(__file__).with_name("global_frobenius_cech_source_results.json")
    target.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"global_Cech_source_levels": 4,
                      "whole_actual_divided_source_gauges": 2,
                      "status": "pass", "results": str(target)}, indent=2))


if __name__ == "__main__":
    main()
