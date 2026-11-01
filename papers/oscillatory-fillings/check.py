#!/usr/bin/env python3
"""Exact algebra checks for the oscillatory filling formula.

Run: python papers/oscillatory-fillings/check.py --output /tmp/filling-check.json

These symbolic identities do not prove contour estimates, uniformity,
Gaussian asymptotics, H1/H2, nonzero source amplitudes, or a volume theorem.
The negative controls are deliberately incorrect algebraic variants.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="write the deterministic JSON record here")
    args = parser.parse_args()
    if not __debug__:
        raise RuntimeError("Run without -O: assertions are part of this checker.")

    identities: list[dict[str, str]] = []
    controls: list[dict[str, str]] = []

    def zero(name: str, expression: sp.Expr, meaning: str) -> None:
        residual = sp.simplify(sp.expand(expression))
        assert residual == 0, (name, residual)
        identities.append({"name": name, "identity": meaning, "residual": "0"})

    def nonzero(name: str, expression: sp.Expr, meaning: str) -> None:
        residual = sp.simplify(sp.expand(expression))
        assert residual != 0 and residual.equals(0) is False, (name, residual)
        controls.append({"name": name, "incorrect_variant": meaning,
                         "nonzero_residual": sp.sstr(residual)})

    pi, I = sp.pi, sp.I
    n = sp.Symbol("n", real=True, nonzero=True)
    N = sp.Symbol("N", integer=True, positive=True)
    ell = sp.Symbol("ell", integer=True, positive=True)
    r = sp.Symbol("r", integer=True, positive=True)
    delta, v, phi = sp.symbols("delta v phi", real=True)
    H = sp.Function("H")

    # Endpoint conditions for the original finite midpoint function.
    # The unit scalar Gamma_N is omitted from both sides of these identities.
    g = sp.sin(phi) * sp.exp(I*n*N*(phi-pi)**2/(4*pi)) * H(2*sp.cos(phi))
    zero("midpoint_zero_left", g.subs(phi, 0), "g(0)=0")
    zero("midpoint_zero_right", g.subs(phi, 2*pi), "g(2*pi)=0")
    dg = sp.diff(g, phi)
    zero("midpoint_equal_first_derivatives",
         dg.subs(phi, 0)-dg.subs(phi, 2*pi), "g'(0)=g'(2*pi)")
    zero("midpoint_fourier_scalar", -N**-2*N*(I*N*ell)+I*ell,
         "-N^(-2) times N times i*N*ell equals -i*ell")
    zero("midpoint_sine_substitution",
         sp.sin(pi-2*pi*delta)-sp.sin(2*pi*delta),
         "sin(pi-2*pi*delta)=sin(2*pi*delta)")
    zero("midpoint_chirp_substitution",
         I*n*N*((pi-2*pi*delta)-pi)**2/(4*pi)-I*pi*n*N*delta**2,
         "the midpoint chirp becomes pi*i*n*N*delta^2")
    zero("midpoint_spectral_substitution",
         2*sp.cos(pi-2*pi*delta)+2*sp.cos(2*pi*delta),
         "2*cos(phi) becomes -2*cos(2*pi*delta)")
    zero("midpoint_parity_exponent", ell+N*ell-(N+1)*ell,
         "midpoint parity and Fourier endpoint parity add to (N+1)*ell")

    # Pair the two actual endpoints before taking an absolute value.
    # x=pi*n*N*v; the common nonzero source/chirp factor is suppressed.
    x = sp.Symbol("x", real=True)
    sine = -I*sp.sinh(2*pi*v)
    zero("right_endpoint_sine",
         sp.sin(2*pi*(sp.Rational(1, 2)+I*v))-sine,
         "sin(2*pi*(1/2+i*v))=-i*sinh(2*pi*v)")
    zero("left_endpoint_sine",
         sp.sin(2*pi*(-sp.Rational(1, 2)+I*v))-sine,
         "sin(2*pi*(-1/2+i*v))=-i*sinh(2*pi*v)")
    right = sine*sp.exp(-x)
    left = sine*sp.exp(x)
    paired = 2*I*sp.sinh(2*pi*v)*sp.sinh(x)
    zero("paired_endpoint_current",
         (right-left-paired).rewrite(sp.exp),
         "right-left=2*i*sinh(2*pi*v)*sinh(pi*n*N*v)")
    zero("paired_current_has_quadratic_zero",
         sp.diff(paired.subs(x, pi*n*N*v), v).subs(v, 0),
         "the paired current has zero first derivative at v=0")
    wrong_unpaired = sp.diff(right.subs(x, pi*n*N*v), v).subs(v, 0)
    nonzero("unpaired_endpoint_cannot_have_quadratic_zero", wrong_unpaired,
            "using the right endpoint alone as an O(v^2) current")

    # Three integrations by parts: retain the second derivative current.
    lam = sp.Symbol("lam", nonzero=True)
    J0, J1, J2, J3, E0, E1, E2 = sp.symbols("J0 J1 J2 J3 E0 E1 E2")
    expanded = (E0/lam-J1/lam).subs(
        J1, E1/lam-J2/lam).subs(J2, E2/lam-J3/lam)
    zero("three_integrations_by_parts",
         expanded-(E0/lam-E1/lam**2+(E2-J3)/lam**3),
         "J0=E0/lam-E1/lam^2+(E2-J3)/lam^3")
    endpoint_reduced = expanded.subs({E0: 0, E1: 0})
    zero("retained_second_derivative_current",
         endpoint_reduced-(E2-J3)/lam**3,
         "zero values and equal first derivatives leave (E2-J3)/lam^3")
    nonzero("wrong_third_integral_sign",
            endpoint_reduced-(E2+J3)/lam**3,
            "replacing E2-J3 by E2+J3 after three integrations by parts")

    # Exact critical-point identity. Positivity follows from a>0, ell>0
    # and a positive squared modulus, not from sampled twist values.
    a = sp.Symbol("a", real=True, positive=True)
    b = sp.Symbol("b", real=True)
    z = -ell/n/(1+I*(a+I*b)/(pi*n))
    den = (1-b/(pi*n))**2+(a/(pi*n))**2
    claimed_im = ell*a/(pi*n**2*den)
    zero("critical_imaginary_part", sp.im(z)-claimed_im,
         "Im[-(ell/n)/(1+i*(a+i*b)/(pi*n))]=ell*a/(pi*n^2*|denominator|^2)")
    s = sp.Symbol("s", real=True, positive=True)
    zero("positive_twist_form",
         claimed_im.subs(n, s)-pi*ell*a/(a**2+(pi*s-b)**2),
         "for n=s>0 the imaginary part is pi*ell*a/[a^2+(pi*s-b)^2]")
    zero("negative_twist_form",
         claimed_im.subs(n, -s)-pi*ell*a/(a**2+(pi*s+b)**2),
         "for n=-s<0 the imaginary part is pi*ell*a/[a^2+(pi*s+b)^2]")
    nonzero("incorrect_signed_twist_denominator",
            (ell*a/(pi*n*den)).subs({n: -1, a: 1, b: 0, ell: 1})
            -claimed_im.subs({n: -1, a: 1, b: 0, ell: 1}),
            "using n instead of n^2 in the imaginary-part numerator denominator")

    # Explicit quadratic model, including the charge derivative.
    c = sp.Symbol("c", real=True, positive=True)
    Phi = sp.Symbol("Phi", real=True)
    L = sp.Symbol("L", real=True, positive=True)
    zz = sp.Symbol("zz")
    phase = Phi-c*zz**2+I*pi*n*zz**2+2*I*pi*L*zz
    critical = -L/(n+I*c/pi)
    zero("quadratic_stationarity", sp.diff(phase, zz).subs(zz, critical),
         "the displayed critical point solves the quadratic phase equation")
    action = sp.simplify(phase.subs(zz, critical))
    real_action = Phi-pi**2*c*L**2/(c**2+pi**2*n**2)
    zero("quadratic_real_action", sp.re(action)-real_action,
         "Re S=Phi-pi^2*c*L^2/(c^2+pi^2*n^2)")
    zero("quadratic_charge_derivative",
         sp.diff(real_action, L)+2*pi*sp.im(critical),
         "d_L Re S=-2*pi*Im z")
    zero("quadratic_positive_charge_loss",
         real_action.subs(L, 1)-real_action
         -pi**2*c*(L**2-1)/(c**2+pi**2*n**2),
         "the exact quadratic loss from charge 1 to L is positive for L>1")

    # Reflection and parity of the *weighted* original integral.
    zero("weighted_sine_reflection",
         (-L)*sp.sin(-2*pi*delta)-L*sp.sin(2*pi*delta),
         "reflecting charge and coordinate reverses both odd factors")
    zero("reflected_phase", n*(-delta)**2+2*(-L)*(-delta)
         -(n*delta**2+2*L*delta), "the quadratic and linear phases are unchanged")
    zero("reflected_parity_even_difference",
         (-(N+1)*ell-(N+1)*ell)/2+(N+1)*ell,
         "the reflected parity exponents differ by the even integer -2*(N+1)*ell")
    nonzero("wrong_fourier_parity",
            (-1)**((3+1)*1)-(-1)**(3*1),
            "dropping +1 from (N+1)*ell fails at N=3, ell=1")
    zero("source_and_fourier_parity_cancel",
         (N-1)*r+(N+1)*r-2*N*r,
         "raw-source and Fourier exponents add to the even integer 2*N*r")
    zero("unit_charge_factor", 2*(-I)-(-2*I),
         "each coordinate's two unit signs multiply -i by 2")
    nonzero("lost_unit_reflection_factor", (-I)-(-2*I),
            "retaining only one unit charge instead of both loses a factor 2")
    alpha = (3*r+1)/2
    zero("level_power", alpha-r/2-(r+sp.Rational(1, 2)),
         "alpha-r/2=r+1/2 for the face packet")
    zero("gaussian_measure_power",
         r/2-(r-1)/2-sp.Rational(1, 2),
         "the net exponent of 2*pi is 1/2")

    # Basic rectangle orientation: bottom and top both positive left-to-right.
    bottom, top, right_side, left_side = sp.symbols("bottom top right_side left_side")
    boundary = bottom+right_side-top+left_side
    zero("rectangle_orientation",
         boundary-(bottom-(top-right_side-left_side)),
         "bottom=top-right_side-left_side when the oriented rectangle boundary is zero")

    here = Path(__file__).resolve().parent
    paths = [Path(__file__).resolve(), here/"main.tex",
             here/"figures"/"whole-interval.tex"]
    hashes = {
        path.relative_to(here).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in paths
    }
    record = {
        "scope": "Exact finite symbolic algebra only. No contour bounds, uniformity, "
                 "Gaussian asymptotics, H1/H2, actual-source amplitude, or volume theorem is proved.",
        "method": "SymPy exact simplification; all displayed residuals are zero identities. "
                  "Deliberately incorrect controls are required to have nonzero exact residuals.",
        "sympy_version": sp.__version__,
        "source_sha256": hashes,
        "identity_count": len(identities),
        "identities": identities,
        "negative_control_count": len(controls),
        "negative_controls": controls,
        "positivity_scope": "The imaginary-part expressions have positive numerator and "
                            "strictly positive denominator under the stated real assumptions; "
                            "no numerical sample establishes a uniform analytic estimate.",
    }
    payload = json.dumps(record, indent=2, sort_keys=True)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload)
        print(json.dumps({"output": str(args.output),
                          "identity_count": len(identities),
                          "negative_control_count": len(controls)}, sort_keys=True))
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
