#!/usr/bin/env python3
"""Exact first-slot boundary chart, norm adapter and inverse-pair checks.

The calculation retains physical factors M in every balanced position.
It proves classical/principal boundary identities, not a quantum source map.
"""

import json
from pathlib import Path

import sympy as sp


def main():
    eps, a, beta, c, s, zeta, mi = sp.symbols(
        "eps a beta c s zeta mi", nonzero=True)
    kap = eps*a
    d = 1-kap*beta
    t = d/(eps*zeta)
    r = t-beta*s
    F = sp.Matrix([[r, 1-r], [s, -kap-s]])
    # mi=M^-1; M=mi+kap. Conjugation needs no determinant reduction.
    U = sp.Matrix([[mi+kap-c*beta, kap*beta-c*beta**2],
                   [c, mi+c*beta]])
    Delta = s+kap*r
    assert sp.cancel(Delta-d*(s*zeta+a)/zeta) == 0
    physical = F.inv()*U*F
    k = sp.cancel(physical[0, 0])
    k_expected = (mi+a*(eps*a+s)/(s*zeta+a)
                  -c*d*(1-eps*zeta)/(eps**2*zeta*(s*zeta+a)))
    assert sp.cancel(k-k_expected) == 0
    p = sp.cancel(-physical[0, 1]/(k-mi))
    assert sp.cancel(p-(1-eps*zeta)) == 0
    leading_k = sp.cancel(eps**2*k).subs(eps, 0)
    assert sp.cancel(leading_k+c/(zeta*(s*zeta+a))) == 0
    # M(0)=1, so A_e=M/k has the indicated order-two leading coefficient.
    assert sp.cancel(1/leading_k+zeta*(s*zeta+a)/c) == 0
    assert sp.cancel(F.det()+Delta) == 0
    assert sp.simplify(F*sp.Matrix([1, 1])-sp.Matrix([1, -kap])) == sp.zeros(2, 1)
    # Coefficient of dlog(A_cut) wedge dzeta in epsilon*Omega_cut.
    form = sp.cancel(-eps*sp.diff(r, zeta)/Delta)
    assert sp.cancel(form-1/(zeta*(s*zeta+a))) == 0
    B = sp.symbols("B", nonzero=True)
    dimension = kap*B/(B**2-1)
    whole_form = sp.cancel(dimension*form/eps)
    assert sp.cancel(whole_form-a*B/((B**2-1)*zeta*(s*zeta+a))) == 0

    # Actual prefix dictionary: A_j=M ell_previous/ell_next.
    # At first order M=1+epsilon*a/2 and u_h=h+O(epsilon^2).
    h = sp.symbols("h", integer=True, nonnegative=True)
    M1 = 1+eps*a/2
    U1 = U.subs(mi, 1-eps*a/2)

    def rescaled_b(hh):
        power = sp.Matrix([[1+hh*eps*a/2, hh], [0, 1-hh*eps*a/2]])
        return sp.cancel(eps**2*(F.inv()*U1*power*F)[0, 0])

    bh, bn = rescaled_b(h), rescaled_b(h+1)
    lead = sp.cancel(bh.subs(eps, 0))
    ratio_first = sp.cancel((sp.diff(bn, eps).subs(eps, 0)
                             -sp.diff(bh, eps).subs(eps, 0))/lead)
    assert sp.cancel(ratio_first-s*zeta-a/2) == 0
    # Raw prefix ratio has a/2; physical balanced AC includes M and cancels it.
    assert sp.cancel(ratio_first-sp.diff(M1, eps)-s*zeta) == 0

    A, BB, C, Y = sp.symbols("A BB C Y", nonzero=True)
    minus = C/(A*BB)*(1-A*C)*(1-Y/BB)/((1-A)*(1-C)*(1-Y*C/BB))
    Ap, Bp, Cp = BB/C, A*C, 1/C
    plus = Ap*Bp*(1-Bp*Cp)*(1-Y/Ap)/((1-Bp)*(1-Cp)*(1-Y*Cp/Ap))
    Vminus, Vplus = C/(1-C), 1/(1-Cp)
    assert sp.cancel(Vminus+Vplus) == 0
    assert sp.cancel(minus*plus+Vminus**2) == 0
    assert sp.cancel(minus*plus/(-Vminus**2)-1) == 0

    # The full original dimension polynomial, including completeness value.
    M = sp.symbols("M", nonzero=True)
    power_cases = []
    for N in range(2, 13):
        uN = sum(M**(N-1-2*j) for j in range(N))
        assert sp.cancel((M-1/M)*uN-(M**N-M**(-N))) == 0
        assert uN.subs(M, 1) == N
        power_cases.append(N)
    result = {
        "status": "PASS",
        "symbolic_blowup_and_physical_momentum": True,
        "exact_full_dimension_form_cancellation": True,
        "actual_physical_inverse_pair_atom": "(1-AC)/eps -> s*zeta",
        "raw_prefix_ratio_only": "(1-b_h/b_(h+1))/eps -> s*zeta+a/2",
        "paired_principal_normal_ratio": 1,
        "peripheral_polynomial_levels": power_cases,
        "scope": "Classical framing blowup, actual peripheral factor and paired principal normals. No quantum source/geometric period comparison or volume limit.",
    }
    output = Path(__file__).with_name("resonant_boundary_blowup_results.json")
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
