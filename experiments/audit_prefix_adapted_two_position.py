#!/usr/bin/env python3
"""Actual prefix ratios, framing trace and local momentum deck law.

Symbolic identities plus an actual figure-eight braid representation;
finite-field sheet tests reconstruct the physical Gauss factors rather
than substituting a developed meridian for them.
"""

import json
from pathlib import Path

import sympy as sp

from audit_finite_sum_annihilator import field


def same(a, b=0):
    assert sp.cancel(a-b) == 0


def symbolic_identities():
    r, s, tau, k, M, k0 = sp.symbols("r s tau k M k0", nonzero=True)
    a, b, c, d = sp.symbols("a b c d")
    F = sp.Matrix([[r, 1-r], [s, -s]])
    J = sp.Matrix([[1, 1], [0, 1]])
    C = sp.Matrix([[a, b], [c, d]])
    Cp = F.inv()*C*F
    ell = d+(a-d)*r+b*s+c*r*(1-r)/s
    same(Cp[0, 0], ell)
    same(s*sp.diff(ell, r), s*(Cp[0, 1]+Cp[1, 0]))
    polynomial = ell.subs(r, s*tau)
    derivative = sp.diff(polynomial, tau)
    delta = c*c+2*c*s*(a+d)+s*s*((a+d)**2-4*C.det())
    same(derivative**2-delta, -4*s*c*polynomial)
    same(sp.trace((F.inv()*J*F)*Cp),
         (1-s)*sp.trace(C)+2*s*Cp[0, 0]+s*(Cp[0, 1]-Cp[1, 0]))
    # Universal quadratic field trace, derived from the infinity residue.
    cu, cv, hu, hv, du, dv, bu, bv = sp.symbols("cu cv hu hv du dv bu bv", nonzero=True)
    cc, hc = cu-k*cv, hu-k*hv
    f2, f1 = -s*cc, cc+s*hc
    v2, v1 = -s*cv, cv+s*hv
    traced = (v1*f2-v2*f1)/f2**2
    same(traced, (cv*hu-hv*cu)/(cu-k*cv)**2)
    B = sp.symbols("B", nonzero=True)
    W = cv*hu-hv*cu
    primitive = (W/cu)/(B*cu-cv)
    same(-sp.diff(primitive, B), W/(B*cu-cv)**2)
    # Generic-meridian twisted reciprocal, retaining BOTH peripheral factors.
    p, t, sigma = sp.symbols("p t sigma", nonzero=True)
    gcut = sp.Matrix([[k0, 1/M-k0], [k0-M, M+1/M-k0]])
    Cwave = sp.Matrix([[0, sigma*(k-1/M)*p], [-sigma*(k-M)/p, t]])
    partner = ((k0-1/M)/(k0-M))*((k-M)/(k-1/M))/p
    same(sp.trace(gcut*Cwave), sp.trace(gcut*Cwave.subs(p, partner)))
    same(Cwave.det().subs(sigma, 1), (k-M)*(k-1/M))
    # All local triangular prefix formulas with exact signed prefixes.
    ap, bp, cp, dp, au, bu0, cu0, du0 = sp.symbols("ap bp cp dp au bu0 cu0 du0", nonzero=True)
    V = sp.Matrix([[ap, bp], [cp, dp]])
    U = sp.Matrix([[au, bu0], [cu0, du0]])
    same(sp.trace(J*(V*U-U*V)), cp*(au-du0)-(ap-dp)*cu0)
    same(-sp.trace((J*U-U*J)*V), cp*(au-du0)-(ap-dp)*cu0)
    same((U-k*V).det(), U.det()+k*k*V.det()-k*sp.trace(U*V.adjugate()))
    for j in (1, 2, 3, 4):
        P0, P1 = (-1)**(j-1)*V, (-1)**j*U
        Km = P1[0, 0]/P0[0, 0]
        Bp = lambda X: sp.Matrix([[X[0, 0], X[0, 1]], [0, 1]])
        Bm = lambda X: sp.Matrix([[1, 0], [-X[1, 0], X[0, 0]]])
        plus, minus = Bp(P1)*Bp(P0).inv(), Bm(P1)*Bm(P0).inv()
        same(plus[0, 0], Km)
        same(plus[0, 1], P1[0, 1]-Km*P0[0, 1])
        same(-minus[1, 0], P1[1, 0]-Km*P0[1, 0])
    # Intrinsic trace-word formulas, including residual centralizer invariance.
    X = sp.Matrix([[a, b], [c, d]])
    same(sp.trace(J*X)-sp.trace(X), c)
    z = sp.symbols("z")
    Z = sp.Matrix([[1, z], [0, 1]])
    transformed = Z.inv()*X*Z
    same(transformed[1, 0], c)
    same(transformed[0, 0]-transformed[1, 1], a-d-2*z*c)
    return {"universal_projector_prefix_discriminant_trace_and_primitive": True,
            "generic_meridian_twisted_momentum_reciprocal_exact": True,
            "all_four_prefix_parities_and_triangular_reconstruction_exact": True,
            "traceword_and_residual_centralizer_marks_exact": True}


def figure_eight_exact():
    u = sp.symbols("u")
    relation = u*u+u+1
    def scalar(x):
        numerator, denominator = sp.cancel(x).as_numer_denom()
        return sp.rem(numerator*sp.invert(denominator, relation, u), relation, u)
    reduce = lambda X: X.applyfunc(scalar)
    A = sp.Matrix([[1, 1], [0, 1]])
    B = sp.Matrix([[1, 0], [-u, 1]])
    C = reduce(B*A.inv()*B*A*B.inv())
    triple = [A, B, C]
    for letter in (1, -2, 1, -2):
        slot = abs(letter)-1
        X, Y = triple[slot:slot+2]
        triple[slot:slot+2] = ([reduce(X.inv()*Y*X), X] if letter > 0
                              else [Y, reduce(Y*X*Y.inv())])
    assert all(reduce(X-Y) == sp.zeros(2) for X, Y in zip(triple, (A, B, C)))
    assert all(reduce(X).trace() == 2 and reduce(X.det()*sp.eye(2)) == sp.eye(2) for X in (A, B, C))
    V, U = reduce(B*A), reduce(C*B*A)
    W = sp.rem(V[1, 0]*(U[0, 0]-U[1, 1])-(V[0, 0]-V[1, 1])*U[1, 0], relation, u)
    assert W == 2*u+1
    cc = sp.rem(U[1, 0]-2*V[1, 0], relation, u)
    tc = sp.rem(sp.trace(U-2*V), relation, u)
    disc = sp.rem(cc**2+2*cc*tc+tc**2-4, relation, u)
    assert cc == u+1 and disc == -3*u-12
    tracecoef = sp.cancel(2*W/cc**2)
    assert sp.rem(sp.together(tracecoef-(2-2*u)).as_numer_denom()[0], relation, u) == 0
    return {"actual_braid": [1, -2, 1, -2], "root_equation": "u^2+u+1=0",
            "exact_irreducible_parabolic_fixed_triple": True,
            "nonzero_actual_prefix_trace_numerator": str(W),
            "nonzero_trace_density_at_s1_k2": "2-2*u",
            "nondegenerate_two_position_fiber_exact": True}


def modmat(X, p):
    return X.applyfunc(lambda x: int(x) % p)


def sheet_cases():
    p = 1009
    u = pow(int(sp.primitive_root(p)), (p-1)//3, p)
    J = sp.Matrix([[1, 1], [0, 1]])
    B = sp.Matrix([[1, 0], [-u, 1]])
    C = modmat(B*J.inv()*B*J*B.inv(), p)
    V, U = modmat(B*J, p), modmat(C*B*J, p)
    ell = lambda X, r, s: (int(X[1, 1])+int(X[0, 0]-X[1, 1])*r+int(X[0, 1])*s
                          +int(X[1, 0])*r*(1-r)*pow(s, -1, p)) % p
    W = (int(V[1, 0])*int(U[0, 0]-U[1, 1])-int(V[0, 0]-V[1, 1])*int(U[1, 0])) % p
    checked = 0
    twisted_density_seen = 0
    for r in range(2, 11):
        for s in range(1, 7):
            ev = ell(V, r, s)
            if not ev:
                continue
            k = ell(U, r, s)*pow(ev, -1, p) % p
            cC = (int(U[1, 0])-k*int(V[1, 0])) % p
            hC = (int(U[0, 0]-U[1, 1])-k*int(V[0, 0]-V[1, 1])) % p
            D = (cC+s*hC-2*cC*r) % p
            if not k or k == 1 or not cC or not D:
                continue
            r2 = (1+s*hC*pow(cC, -1, p)-r) % p
            ev2 = ell(V, r2, s)
            if not ev2:
                continue
            assert ell(U, r2, s)*pow(ev2, -1, p) % p == k
            D2 = (cC+s*hC-2*cC*r2) % p
            assert D2 == -D % p
            local_momenta = []
            for rr in (r, r2):
                F = sp.Matrix([[rr, 1-rr], [s, -s]])
                Fi = modmat(F.inv_mod(p), p)
                Up, Vp = modmat(Fi*U*F, p), modmat(Fi*V*F, p)
                # j=3: actual signed old prefixes P3=-Up, P2=Vp.
                physical_e = (-int(Up[0, 1])+k*int(Vp[0, 1])) % p
                wave = physical_e*pow(k-1, -1, p) % p
                assert wave
                local_momenta.append(wave)
            wave, wave2 = local_momenta
            assert wave2 == pow(wave, -1, p)
            z = s*(k-1) % p
            odd = (pow(wave, -1, p)-wave) % p
            assert odd == D*pow(z, -1, p) % p  # (-1)^(j+1)=+1
            density = k*ev*pow(D, -1, p) % p
            density2 = k*ev2*pow(D2, -1, p) % p
            expected_trace = k*W*pow(cC, -2, p) % p
            assert (density+density2) % p == expected_trace
            if ev != ev2:
                twisted_density_seen += 1
                assert (density+density2) % p
            adapted = density*odd*pow(ev, -1, p) % p
            odd2 = (pow(wave2, -1, p)-wave2) % p
            assert adapted == density2*odd2*pow(ev2, -1, p) % p
            assert adapted == k*pow(z, -1, p) % p
            checked += 1
    assert checked and twisted_density_seen
    return {"actual_figure_eight_sheet_cases": checked,
            "genuinely_non_odd_density_cases": twisted_density_seen,
            "actual_Gauss_momentum_not_developed_substitution": True,
            "reciprocal_deck_and_clock_adapted_even_density_exact": True}


def whole_quantum_prefix():
    checked = 0
    for N in range(2, 10):
        p, _, q = field(N)
        Q = q*q % p
        for M in (1, 2, 3):
            x = -M*pow(q, -1, p) % p
            for j in range(1, 5):
                positions = [(i*i+1) % N for i in range(j-1)]
                signed = (-1)**(j-1)
                for a in positions:
                    signed = signed*x*pow(Q, -a, p) % p
                adapter = pow(q*pow(M, -1, p), j-1, p)*pow(Q, sum(positions), p) % p
                assert adapter == pow(signed, -1, p)
                checked += 1
    return {"actual_whole_q_meridian_prefix_clock_cases": checked,
            "full_q_over_M_factor_retained": True}


def main():
    result = {"status": "pass", "universal_symbolic_proofs": symbolic_identities(),
              "actual_figure_eight_representation": figure_eight_exact(),
              "actual_physical_sheet_and_source_adapter": sheet_cases(),
              "whole_quantum_prefix": whole_quantum_prefix(),
              "scope": "Actual prefix-adapted two-position geometry and inserted orientation observable; no selected-cycle or volume inference."}
    target = Path(__file__).with_name("prefix_adapted_two_position_results.json")
    target.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "pass", "sheet_cases": result["actual_physical_sheet_and_source_adapter"]["actual_figure_eight_sheet_cases"],
                      "whole_prefix_cases": result["whole_quantum_prefix"]["actual_whole_q_meridian_prefix_clock_cases"],
                      "results": str(target)}, indent=2))


if __name__ == "__main__":
    main()
