#!/usr/bin/env python3
"""Independent Wick pairing and actual compact-atom first-loop checks.

Uses exp(S/H), inverse Hessian G, covariance -H G.  No finite cap or
global stationary-cycle comparison is inferred by these local identities.
"""

from functools import lru_cache
from itertools import product
import json
from pathlib import Path

import sympy as sp
from sympy.polys.domains import QQ


def symmetric_tensor(dimension, rank, offset):
    return {indices: sp.Rational(offset+sum((j+1)**2 for j in indices)
                                +sp.prod(j+1 for j in indices), 7)
            for indices in product(range(dimension), repeat=rank)}


def pairing_check(dimension):
    y = sp.symbols(f"y0:{dimension}")
    # A genuinely non-diagonal covariance for dimensions two and three.
    hessian = sp.Matrix(dimension, dimension,
                        lambda i,j: (i+3 if i == j else 1))
    g = hessian.inv()
    s3 = symmetric_tensor(dimension, 3, -4)
    s4 = symmetric_tensor(dimension, 4, 2)
    a0, a1 = sp.Rational(5, 2), sp.Rational(-2, 7)
    ad = [sp.Rational(2*i-1, 3) for i in range(dimension)]
    add = sp.Matrix(dimension,dimension,
                    lambda i,j: sp.Rational((i+1)*(j+1)+2, 5))
    vertex3 = sum(s3[ii]*sp.prod(y[i] for i in ii)
                  for ii in product(range(dimension),repeat=3))/6
    vertex4 = sum(s4[ii]*sp.prod(y[i] for i in ii)
                  for ii in product(range(dimension),repeat=4))/24
    amp1 = sum(ad[i]*y[i] for i in range(dimension))
    amp2 = sum(add[i,j]*y[i]*y[j]
               for i,j in product(range(dimension),repeat=2))/2

    @lru_cache(None)
    def moment(indices):
        if not indices:
            return sp.Integer(1)
        if len(indices) % 2:
            return sp.Integer(0)
        first, rest = indices[0], indices[1:]
        return sum(-g[first,j]*moment(rest[:k]+rest[k+1:])
                   for k,j in enumerate(rest))

    def wick(poly):
        result = 0
        for powers, coefficient in sp.Poly(sp.expand(poly), *y).terms():
            indices = tuple(i for i,power in enumerate(powers)
                            for _ in range(power))
            result += coefficient*moment(indices)
        return sp.factor(result)

    direct = a1+(wick(amp2)+wick(amp1*vertex3)+a0*wick(vertex4)
                  +a0*wick(vertex3**2)/2)/a0
    formula = a1-sum(g[i,j]*add[i,j]
                        for i,j in product(range(dimension),repeat=2))/(2*a0)
    formula += sum(ad[l]*s3[i,j,k]*g[i,j]*g[k,l]
                   for i,j,k,l in product(range(dimension),repeat=4))/(2*a0)
    formula += sum(s4[i,j,k,l]*g[i,j]*g[k,l]
                   for i,j,k,l in product(range(dimension),repeat=4))/8
    formula -= sum(s3[i,j,k]*s3[l,m,n]*g[i,l]*g[j,m]*g[k,n]
                   for i,j,k,l,m,n in product(range(dimension),repeat=6))/12
    formula -= sum(s3[i,j,k]*s3[l,m,n]*g[i,j]*g[l,m]*g[k,n]
                   for i,j,k,l,m,n in product(range(dimension),repeat=6))/8
    assert sp.cancel(direct-formula) == 0
    return {"dimension": dimension, "first_loop_exact": str(direct),
            "covariance": "-H*(S'')^-1", "independent_pairing_recursion": True}


def atom_and_original_monomials():
    alpha, L0 = sp.symbols("alpha Li0")
    correction = sp.expand((alpha**2/2-alpha/2+sp.Rational(1,12))*L0)
    assert correction.subs(alpha,0) == L0/12
    assert correction.subs(alpha,1) == L0/12
    assert correction.subs(alpha,sp.Rational(1,2)) == -L0/24
    # The expansion is obtained directly from Li2(e^(alpha H)z)/H,
    # half log(1-e^(alpha H)z), and H Li0/12.
    H, a, b, c, u, mark = sp.symbols("H a b c u mark")
    log_x = u+mark-H/2
    positive = (sp.pi*sp.I*c-(a+b+c)*log_x+a*b+(a-b)*c-c*c/2)/H-c/2
    negative = ((a+b-c)*log_x-a*b)/H
    assert sp.expand(positive).coeff(H,0) == (a+b)/2
    assert sp.expand(negative).coeff(H,0) == (c-a-b)/2
    assert sp.expand(positive).coeff(H,1) == 0
    assert sp.expand(negative).coeff(H,1) == 0
    # Full closed pivot/framing source: n=c0/H-1 and Log x=u+mark-H/2.
    c0,kappa,xi = sp.symbols("c0 kappa xi")
    source = sp.expand((c0/H-1)*kappa*log_x+(c0/H-1)*xi)
    assert sp.expand(source).coeff(H,1) == kappa/2
    assert not sp.expand(source).coeff(H,1).has(xi,u)
    return {"general_atom_H_coefficient": str(correction),
            "both_actual_integer_shifts": "+Li0/12",
            "fractional_half_shift_if_present": "-Li0/24",
            "positive_principal_monomial": "(a+b)/2",
            "negative_principal_monomial": "(c-a-b)/2",
            "no_variable_H_correction_from_original_monomials": True,
            "full_closed_source_H_correction_base_only": str(kappa/2)}


def exact_figure_eight_cap_certificate():
    source=Path(__file__).with_name("figure_eight_first_loop_cap_exact_results.json")
    data=json.loads(source.read_text())
    r=sp.symbols("r")
    pair=data["relative_one_loop_quadratic_pair"]
    a,b=(sp.cancel(sp.sympify(pair[key])) for key in ("a","b"))
    common=(r*r+3)**4*(3*r*r+6*r+7)**4
    assert sp.expand(sp.denom(a)-216*common)==0
    assert sp.expand(sp.denom(b)-108*common)==0
    assert sp.denom(a).subs(r,-2)==216*7**8
    assert sp.denom(b).subs(r,-2)==108*7**8
    # At the other selected cap r=1-t, t^2-t+1=0, both denominator
    # factors are nonzero; neither rational root -2,-4/9 is allowed.
    relation=r*r-r+1
    assert sp.rem(r*r+3,relation,r)==r+2
    assert sp.rem(3*r*r+6*r+7,relation,r)==9*r+4
    assert sp.gcd(common,relation)==1
    residue_sum=sp.simplify(sum(sp.sympify(piece["residue"])
                              for piece in data["pieces"].values()))
    assert residue_sum==0
    assert data["total_valuation"]==data["other_sheet_valuation"]==0
    return {"field": "Q(r)[t]/(t^2-t+1)",
            "s": 1, "selected_caps": ["r=-2","r=1-t"],
            "quadratic_pair_denominators": [str(216*common),str(108*common)],
            "both_components_regular_at_both_caps": True,
            "six_exact_piece_residues_sum": str(residue_sum),
            "source_result": str(source)}


def hermite_relative_endpoint_certificate():
    source=Path(__file__).with_name("figure_eight_first_loop_cap_exact_results.json")
    data=json.loads(source.read_text())
    certificate=data["hermite_primitive_certificate"]
    r=sp.symbols("r")
    domain=QQ.algebraic_field(sp.sqrt(-3))
    field=domain.frac_field(r)
    rr=field.gens[0]
    def lift(value):return field.convert(value,domain)
    def polynomial(expr):
        return sum((lift(domain.from_sympy(coefficient))*rr**power[0]
                    for power,coefficient in sp.Poly(sp.expand(expr),r).terms()),field.zero)
    def derivative(value):
        variable=value.field.ring.gens[0]
        return value.field.new(value.numer.diff(variable)*value.denom
                               -value.numer*value.denom.diff(variable),value.denom**2)
    def at(value,point):
        variable=value.field.ring.gens[0]
        numerator=value.numer.evaluate(variable,point)
        denominator=value.denom.evaluate(variable,point)
        assert denominator
        return numerator/denominator
    t=domain.from_sympy((1-sp.sqrt(-3))/2)
    J=polynomial(sp.sympify(certificate["physical_projection_jacobian_numerator"]))
    V=2+lift(t)-lift(t)*rr**2
    U=4-lift(t)-(lift(t)+1)*(rr+rr**2)
    assert not J-(derivative(U)*V-U*derivative(V))
    polynomial_part=polynomial(sp.sympify(certificate["primitive_polynomial_part"]))
    coefficients=[domain.from_sympy(sp.sympify(value))
                  for value in certificate["primitive_coefficients"]]
    basis=[rr/J**3,1/J**3,rr/J**2,1/J**2,rr/J,1/J]
    primitive=polynomial_part+sum((lift(a)*b for a,b in zip(coefficients,basis)),field.zero)
    pair=data["relative_one_loop_quadratic_pair"]
    z1=(field.from_sympy(sp.sympify(pair["a"]))
         +lift(t)*field.from_sympy(sp.sympify(pair["b"])))
    assert not derivative(primitive)-z1
    cleared=z1*J**4
    assert cleared.denom.degree()==0 and cleared.numer.degree()==10
    assert z1.numer.degree()-z1.denom.degree()==2
    caustics=[2*t-1,-(1+4*t)/3]
    for point in caustics:
        assert not at(J,point)
        assert at(derivative(J),point)
        assert coefficients[0]*point+coefficients[1]
    # Hence G has exact order-three poles at both simple J zeros;
    # its derivative has order four and zero logarithmic residues.
    cap_gap=at(primitive,1-t)-at(primitive,domain.convert(-2))
    meridian_gap=at(primitive,domain.convert(-1))-at(primitive,domain.convert(-2))
    assert cap_gap==(889-125*t)/216
    assert meridian_gap==(1076-991*t)/432
    assert cap_gap==domain.from_sympy(sp.sympify(certificate[
        "two_cap_primitive_gap_G_1_minus_t_minus_G_minus2"]))
    assert meridian_gap==domain.from_sympy(sp.sympify(certificate[
        "classical_centralizer_gap_G_minus1_minus_G_minus2"]))
    invariant=cap_gap/(3-t)-meridian_gap
    assert invariant==(295*t-138)/112 and invariant
    return {"native_algebraic_fraction_field_derivative_certificate": True,
            "physical_prefix_Jacobian_verified": True,
            "J_fourth_clears_denominators_degree": 10,
            "z1_pole_order_at_infinity": 2,
            "primitive_pole_order_at_each_caustic": 3,
            "z1_pole_order_at_each_caustic": 4,
            "both_caustic_logarithmic_residues_zero": True,
            "two_cap_gap": "(889-125*t)/216",
            "classical_centralizer_gap": "(1076-991*t)/432",
            "base_unit_invariant_relative_gap": "(295*t-138)/112",
            "relative_gap_nonzero": True}


def main():
    result = {"status": "PASS", "wick_pairing": [pairing_check(d) for d in (1,2,3)],
              "actual_atoms_and_monomials": atom_and_original_monomials(),
              "exact_figure_eight_cap_certificate": exact_figure_eight_cap_certificate(),
              "hermite_relative_endpoint_certificate": hermite_relative_endpoint_certificate(),
              "scope": "Actual transverse first-loop coefficient. No subprincipal "
                       "finite-cap identification or selected global period is inferred."}
    target = Path(__file__).with_name("wick_first_loop_and_actual_atoms_results.json")
    target.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"status": "PASS", "wick_dimensions": [1,2,3],
                      "actual_integer_and_fractional_atom_shifts": True,
                      "original_Gaussian_color_and_closed_source": True,
                      "exact_figure_eight_two_cap_regularity_at_s1": True,
                      "Hermite_exactness_and_relative_gap": True,
                      "output": str(target)},indent=2))


if __name__ == "__main__":
    main()
