#!/usr/bin/env python3
"""Exact finite algebra for Marked deformations and long fillings.

The identities use independent symbolic parameters, not sampled slopes.
This program does not prove the implicit-function theorem, positivity,
topological gluing, metric completeness, or the Stokes comparison.
Requires SymPy and assertions enabled.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as s


def equal(a, b):
    return s.cancel(a - b) == 0


def projective_equal(a, b):
    aa, bb = list(a), list(b)
    return all(equal(aa[i] * bb[j], aa[j] * bb[i])
               for i in range(4) for j in range(i))


def point(z):
    return s.Matrix([1, 0]) if z is None else s.Matrix([z, 1])


def carries(matrix, z, target):
    a, b = matrix * point(z), point(target)
    return equal(a[0] * b[1], a[1] * b[0])


def derivative(matrix, z):
    if z is None:
        return s.cancel(matrix.det() / matrix[0, 0] ** 2)
    return s.cancel(matrix.det() /
                    (matrix[1, 0] * z + matrix[1, 1]) ** 2)


def whites(e, r):
    return [s.diag(1, e), s.Matrix([[1, e - 1], [0, e]]),
            s.Matrix([[e-r, r*(1-e)], [e-1, 1-e*r]]),
            s.Matrix([[r, 0], [1-e, e*r]])]


def mixed_leaf():
    e, t = s.symbols("E T", nonzero=True)
    z = (1+e)/(1+t)
    r = t*(1+e)**2/(e*(1+t)**2)
    polynomial = lambda q: q*q-(1+e)*q+e*r
    assert equal(polynomial(z), 0)
    assert equal(polynomial(t*z), 0)
    # Reflection of the minus-t flag, not the plus-t flag.
    reflected_minus = ((1+1/e)/(1+1/t)) / t
    assert equal(reflected_minus, z/e)
    assert not equal((1+1/e)/(1+1/t), z/e)
    w = whites(e, r)
    pure = s.Matrix([[0, -e*r], [1, -1-e]])
    odd_minus = s.Matrix([[r, -r], [1, e*r-1-e]])
    odd_plus = s.Matrix([[r/e-1-1/e, r], [-1, r]])
    assert carries(w[0], z, z/e)
    assert carries(w[2], z, z/e)
    assignments = [
        (pure, [z, None, 1], [z, 0, r]),
        (odd_minus, [z, None, 1], [z/e, r, 0]),
        (odd_plus, [z, r, 0], [z/e, None, 1]),
    ]
    for matrix, source, target in assignments:
        for a, b in zip(source, target):
            assert carries(matrix, a, b)
    longitude = w[2].inv()*w[0]
    words = [longitude, pure.inv(),
             odd_minus.inv()*w[0], w[0].inv()*odd_plus]
    q, rho = (e*t-1)/(e-t), 1/t
    multipliers = [q*q, rho, rho*q, rho/q]
    for word, multiplier in zip(words, multipliers):
        assert carries(word, z, z)
        assert equal(1/derivative(word, z), multiplier)
        assert projective_equal(word*longitude, longitude*word)
    assert equal(q.subs(t, 1), 1)
    assert not equal(1/derivative(words[2], z), rho/q)
    # These are algebraic identities; no choice of a logarithm is tested.
    return {
        "apex_roots": 2,
        "white_apex_assignments": 2,
        "shaded_vertex_assignments": 9,
        "primitive_multipliers": 4,
        "commuting_longitude_pairs": 4,
        "negative_controls": [
            "reflection of the plus-t apex",
            "opposite odd-meridian shear",
        ],
    }


def main_meridians():
    e, r = s.symbols("E R", nonzero=True)
    w = whites(e, r)
    corners = [0, None, 1, r]
    expected = [1/e, e, 1/e, e]
    for j, (z, d) in enumerate(zip(corners, expected)):
        for matrix in (w[j-1], w[j]):
            assert carries(matrix, z, z)
            assert equal(derivative(matrix, z), d)
        meridian = w[j-1].inv()*w[j]
        assert carries(meridian, z, z)
        assert equal(derivative(meridian, z), 1)
        assert equal(s.trace(meridian)**2, 4*meridian.det())
        assert not projective_equal(meridian, s.eye(2))
    return {"corner_derivatives": 8, "unipotent_nonidentity_words": 4}


def classical_hessian():
    x, t = s.symbols("x t", real=True)
    v = s.log(s.sin(s.pi*(x-t))/s.sin(s.pi*(x+t)))
    assert s.simplify(s.diff(v, t).subs(t, 0) +
                      2*s.pi*s.cot(s.pi*x)) == 0
    assert s.simplify(s.diff(v, x).subs(t, 0)) == 0
    c, eps = s.symbols("c epsilon", real=True)
    tau = 2*s.I*c/(1-eps*s.I*c)
    gtt = -2*s.pi*c
    chi_t = 1-eps*gtt/(2*s.pi*s.I)
    fcc = gtt/chi_t
    assert equal(chi_t, 1-eps*s.I*c)
    assert equal(fcc, s.pi*s.I*tau)
    assert equal(-2*fcc, -2*s.pi*s.I*tau)
    assert not equal(-2*fcc, -4*s.pi*s.I*tau)
    gx, dv, dt, dx, vv = s.symbols("g_x dv dt dx v")
    df = gx*dx + vv*dt - eps*vv*dv/(2*s.pi*s.I)
    dchi = dt-eps*dv/(2*s.pi*s.I)
    assert equal(df, gx*dx + vv*dchi)
    return {
        "log_sine_derivatives": 2,
        "shear_and_hessian_identities": 4,
        "negative_controls": ["doubled auxiliary Jacobian"],
        "not_checked": "stationary-wire Hessian invertibility",
    }


def signed_filling():
    a, b, r = s.symbols("a b r", real=True)
    tau = a+s.I*b
    chi = r/(tau+r)
    u = -2*s.pi*s.I*chi
    v = tau*u
    assert s.simplify(v+r*u+2*s.pi*s.I*r) == 0
    re_v = s.simplify(s.re(v))
    expected = 2*s.pi*r*r*b/((a+r)**2+b*b)
    assert s.simplify(re_v-expected) == 0
    assert s.simplify(re_v-expected/2) != 0
    # The written proof supplies b>0 and r!=0, so this expression is positive.
    return {
        "slope_equation": True,
        "real_longitude_identity_for_both_real_signs": True,
        "negative_controls": ["lost factor two in real longitude"],
        "positivity_hypotheses": ["b > 0", "r != 0"],
    }


def polarization():
    ur, ui, vr, vi, dur, dui, dvr, dvi = s.symbols(
        "U_R U_I V_R V_I dU_R dU_I dV_R dV_I", real=True)
    # dG = V dU/2; subtracting Re(U)Im(V)/2 gives the volume differential.
    im_dg = s.im((vr+s.I*vi)*(dur+s.I*dui))/2
    regulated = im_dg-(dur*vi+ur*dvi)/2
    differential = (vr*dui-ur*dvi)/2
    assert s.expand(regulated-differential) == 0
    # Copying the opposite polarization without its Legendre term fails.
    wrong = s.im(-(ur+s.I*ui)*(dvr+s.I*dvi))/2
    assert s.expand(wrong-(dur*vi+ur*dvi)/2-differential) != 0
    a, b, p = s.symbols("u v p", real=True, nonzero=True)
    chi = a+s.I*b
    u = -2*s.pi*s.I*chi
    v = 2*s.pi*s.I*(chi-1)/p
    correction = -s.re(u)*s.im(v)/2
    action = 2*s.pi*s.re(s.pi*s.I*(chi-1)**2/(2*p))
    assert s.simplify(correction-action) == 0
    assert s.simplify(correction+action) != 0
    return {
        "polarized_volume_differential": True,
        "critical_boundary_cancellation": True,
        "negative_controls": [
            "opposite polarization without Legendre correction",
            "wrong sign of the filling boundary correction",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.unlink(missing_ok=True)
    if not __debug__:
        raise RuntimeError("Run without -O: assertions are required.")
    here = Path(__file__).resolve().parent
    repo = here.parents[1]
    sources = sorted(here.rglob("*.tex")) + [Path(__file__).resolve()]
    sources += [repo/"papers"/"conway-geometry"/name
                for name in ("main.tex", "assembly.tex", "maps.tex",
                             "completion.tex")]
    sources += [repo/"papers"/"newton-tangles"/"main.tex",
                repo/"papers"/"marked-fillings"/"main.tex"]
    hashes = {str(path.relative_to(repo)):
              hashlib.sha256(path.read_bytes()).hexdigest() for path in sources}
    checks = {
        "mixed_leaf": mixed_leaf(),
        "main_meridians": main_meridians(),
        "classical_hessian": classical_hessian(),
        "signed_filling": signed_filling(),
        "polarization": polarization(),
    }
    after = {str(path.relative_to(repo)):
             hashlib.sha256(path.read_bytes()).hexdigest() for path in sources}
    if after != hashes:
        raise RuntimeError("A pinned source changed while the checks ran.")
    record = {
        "scope": "exact rational and differential algebra in independent symbols",
        "excluded": [
            "topological reconstruction and primitive-curve identification",
            "implicit-function existence or uniform neighborhoods",
            "positive tetrahedra, metric completion and winding",
            "regulator/Stokes comparison or any quantum asymptotic",
        ],
        "sympy_version": s.__version__,
        "checks": checks,
        "source_sha256": hashes,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2, sort_keys=True)+"\n")
    print(json.dumps({"output": str(args.output), "groups": sorted(checks)}))


if __name__ == "__main__":
    main()
