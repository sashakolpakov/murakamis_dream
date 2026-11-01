#!/usr/bin/env python3
"""Exact finite algebra for Circle patterns and primitive fillings.

This checks the displayed local identities and their conventions. It does
not prove packing existence, global development, holomorphic uniformity,
metric completion, Stokes limits, or the volume theorem.
Run with Python and SymPy; --output writes a deterministic JSON record.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if not __debug__:
        raise RuntimeError("Assertions must be enabled.")
    identities = []
    controls = []

    def zero(name, expr, meaning):
        value = sp.factor(sp.cancel(sp.expand(expr)))
        assert value == 0, (name, value)
        identities.append({"name": name, "meaning": meaning, "residual": "0"})

    def nonzero(name, expr, meaning):
        value = sp.factor(sp.cancel(sp.expand(expr)))
        assert value != 0 and value.equals(0) is False, (name, value)
        controls.append({"name": name, "incorrect_variant": meaning,
                         "residual": str(value)})

    # All eight independent normal-flow coordinates on each tetrahedron.
    vectors = [sp.Matrix([1, 0]), sp.Matrix([0, 1]), sp.Matrix([-1, -1])]
    kinds = {(0, 1): 0, (2, 3): 0, (0, 2): 1,
             (1, 3): 1, (0, 3): 2, (1, 2): 2}
    rvar = sp.symbols("r0:8")
    svar = sp.symbols("s0:8")

    def flow(variables):
        entries = {}
        total = sp.zeros(2, 1)
        for j in range(4):
            faces = [f for f in range(4) if f != j]
            a, b = variables[2*j:2*j+2]
            for f, value in zip(faces, (a, b, -a-b)):
                entries[j, f] = value
            total += (-1)**j * (
                b*vectors[kinds[tuple(sorted((j, faces[2])))]]
                -(-a-b)*vectors[kinds[tuple(sorted((j, faces[1])))]])
        return entries, total

    r, dr = flow(rvar)
    s, ds = flow(svar)
    J2 = sp.Matrix([[0, 1], [-1, 0]])
    J3 = sp.Matrix([[0, 1, -1], [-1, 0, 1], [1, -1, 0]])
    # Geometric dictionary: the positive tetrahedron is (0,infinity,1,z).
    # Its normalized cusp triangles are (0,1,t_j), so side vectors are
    # t_j-1,t_j,1, with constant minus signs irrelevant for derivatives.
    z = sp.Symbol("z", nonzero=True)
    uu, vv = sp.symbols("u v")
    third = [1/z, z, 1/(1-1/z), 1/(1-z)]
    side_logs = [(vv, -uu, 0), (uu+vv, uu, 0),
                 (-uu-vv, -vv, 0), (-vv, -uu-vv, 0)]
    for j in range(4):
        faces = [f for f in range(4) if f != j]
        local_row = (-1)**j*(
            r[j, faces[1]]*vectors[kinds[tuple(sorted((j, faces[2])))]]
            -r[j, faces[2]]*vectors[kinds[tuple(sorted((j, faces[1])))]])
        geometric = sum(r[j, f]*term for f, term in zip(faces, side_logs[j]))
        zero(f"actual_cusp_log_row_{j}",
             geometric-local_row[0]*uu-local_row[1]*vv,
             "the developed cusp side-log sum equals d_j(r)")
        for k, side in enumerate((third[j]-1, third[j], sp.Integer(1))):
            linear = side_logs[j][k]
            expected_log_derivative = sp.diff(linear, uu)/z + sp.diff(linear, vv)/(z*(z-1))
            zero(f"actual_cusp_side_derivative_{j}_{k}",
                 sp.diff(side, z)/side-expected_log_derivative,
                 "actual cusp side has the listed (log z, log(1-z^-1)) row")
    nonzero("wrong_tetrahedron_order",
            r[0, 1]*(uu+vv)+r[0, 2]*uu
            -(r[0, 1]*vv-r[0, 2]*uu),
            "using the (infinity,0,1,z) side table at vertex0 of (0,infinity,1,z)")
    H, zx, zy = sp.symbols("H zx zy", positive=True)
    positive_tetrahedron = sp.Matrix([[0, 1, zx], [0, 0, zy], [H, 0, 0]])
    zero("positive_tetrahedron_orientation",
         positive_tetrahedron.det()-H*zy,
         "(0,infinity,1,z) has orientation + for Im z>0")
    for eps in (1, -1):
        intersection = 0
        facesum = 0
        for j in range(4):
            f0, f1, _ = [f for f in range(4) if f != j]
            intersection += -eps*(-1)**j * (
                r[j, f0]*s[j, f1]-r[j, f1]*s[j, f0])
        for f in range(4):
            rr = sp.Matrix([r[j, f] for j in range(4) if j != f])
            ss = sp.Matrix([s[j, f] for j in range(4) if j != f])
            facesum += eps*(-1)**f*(rr.T*J3*ss)[0]
        omega = eps*(dr.T*J2*ds)[0]
        zero(f"normal_flow_orientation_{eps}", omega+intersection-facesum,
             "mf:normal-flow in all 16 free variables")
        nonzero(f"wrong_intersection_factor_{eps}",
                omega+intersection/2-facesum,
                "halving the twice-intersection term changes the identity")
    for perm in itertools.permutations(range(3)):
        mat = sp.zeros(3)
        for i, j in enumerate(perm):
            mat[i, j] = 1
        residual = mat.T*J3*mat-mat.det()*J3
        assert residual == sp.zeros(3)
        identities.append({"name": f"face_permutation_{perm}",
                           "meaning": "P^T J3 P=sign(P) J3",
                           "residual": "zero matrix"})
    # One explicit row basis with skew pairing -2, retaining symbolic
    # free coefficients, verifies the row-to-tangent inverse factor.
    aa0, aa1, bb0 = sp.symbols("aa0 aa1 bb0", nonzero=True)
    rowa = sp.Matrix([[aa0, aa1]])
    rowb = sp.Matrix([[bb0, (aa1*bb0-2)/aa0]])
    xu = -J2*rowb.T/2
    xv = J2*rowa.T/2
    zero("peripheral_row_pair", (rowa*J2*rowb.T)[0]+2,
         "the actual primitive rows have pairing -2")
    zero("dual_U_vector", (rowa*xu)[0]-1, "a(X_U)=1")
    zero("dual_V_vector", (rowb*xv)[0]-1, "b(X_V)=1")
    zero("dual_cross_U", (rowb*xu)[0], "b(X_U)=0")
    zero("dual_cross_V", (rowa*xv)[0], "a(X_V)=0")
    zero("tangent_reduced_pair", (xu.T*J2*xv)[0]+sp.Rational(1, 2),
         "the dual tangent pairing is -1/2")

    # Original circle and Hessian formulas, with algebraic square roots.
    x, y, b, s0 = sp.symbols("x y b s", positive=True)
    A = x+y
    T2 = b*A+x*y+b*b*s0*s0
    B = A+2*b*s0*s0
    D = A*A-4*x*y*s0*s0
    zero("continuant_discriminant", B*B-4*s0*s0*T2-D,
         "(A+2bs^2)^2-4s^2 T_b^2=D")
    D0 = sp.sqrt(x*y+x*b+y*b)
    angle_gradient = sp.atan(x/D0)/sp.pi
    zero("triangle_off_diagonal_hessian",
         y*sp.diff(angle_gradient, y)+x*y/(2*sp.pi*D0*(x+y)),
         "d_log(y) d_log(x) F=-xy/[2pi D0(x+y)]")
    zero("triangle_scale_kernel",
         x*sp.diff(angle_gradient, x)+y*sp.diff(angle_gradient, y)
         +b*sp.diff(angle_gradient, b),
         "the angle gradient has scale derivative zero")

    # The braid calculation is done in a free group, not sampled matrices.
    def product(*words):
        out = []
        for word in words:
            for letter in word:
                if out and out[-1] == -letter:
                    out.pop()
                else:
                    out.append(letter)
        return tuple(out)

    def inv(word):
        return tuple(-a for a in reversed(word))

    aa, bb, cc = (1,), (2,), (3,)
    state = [aa, bb, cc]
    for index in (2, 1, 1, 2):
        i = index-1
        a0, b0 = state[i:i+2]
        state[i:i+2] = [product(inv(a0), b0, a0), a0]
    pp = product(bb, aa)
    kk = product(inv(pp), cc, pp)
    expected = [product(inv(kk), aa, kk),
                product(inv(kk), bb, kk), kk]
    assert state == expected
    identities.append({"name": "original_threading_word",
                       "meaning": "[2,1,1,2] gives (K^-1 A K,K^-1 B K,K)",
                       "residual": "identical reduced free words"})

    # Generic equal-trace SL2 matrices; identities extend after clearing
    # denominators, including noncentral parabolic points.
    a, b0, c, tr = sp.symbols("a b0 c tr", nonzero=True)
    ma = sp.Matrix([[a, 1], [a*(tr-a)-1, tr-a]])
    mb = sp.Matrix([[b0, c], [(b0*(tr-b0)-1)/c, tr-b0]])
    pp = mb*ma
    hh = pp.inv()-sp.eye(2)
    for i, value in enumerate(hh*ma-ma.inv()*mb*ma*hh):
        zero(f"hurwitz_first_generator_{i}", value,
             "H A=(A^-1 B A)H for H=(BA)^-1-I")
    for i, value in enumerate(hh*mb-ma*hh):
        zero(f"hurwitz_second_generator_{i}", value, "H B=A H")
    zero("hurwitz_determinant", hh.det()-(2-sp.trace(pp)),
         "det(P^-1-I)=2-tr(P)")
    for i, value in enumerate(hh*hh-(sp.trace(pp)-2)*pp.inv()):
        zero(f"full_twist_word_{i}", value,
             "H^2=(tr P-2)P^-1 fixes n=epsilon-2p in the ordered collar")

    J, R0, m = sp.symbols("J R0 m", nonzero=True)
    diagP = sp.diag(J, 1/J)
    diagC = sp.diag(R0, 1)
    for eps in (-1, 0, 1):
        meridian = m*R0*(1/J-1)**(-eps)*diagC.inv()*(diagP.inv()-sp.eye(2))**eps
        zero(f"selected_meridian_eigenvalue_{eps}", meridian[0, 0]-m,
             "the original auxiliary meridian has selected eigenvalue m")
        zero(f"meridian_determinant_{eps}",
             meridian.det()-m*m*R0*(-J)**eps,
             "det meridian=m^2 R0(-J)^epsilon, killed by the literal equation")
    nonzero("double_reflection_is_not_primitive", R0**2-R0,
            "substituting R0^2 for the single-sidepairing ratio")

    t, br, bi = sp.symbols("t br bi", real=True)
    delta = -t/(1+sp.I*t*(br+sp.I*bi)/sp.pi)
    den = (1-t*bi/sp.pi)**2+(t*br/sp.pi)**2
    zero("signed_filling_imaginary_part",
         sp.im(delta)-t*t*br/(sp.pi*den),
         "Im delta=t^2 Re B/[pi |1+i t B/pi|^2], both signs of t")
    p, re, im = sp.symbols("p re im", real=True)
    dd = re+sp.I*im
    U = 4*sp.pi*sp.I*p*dd-2*sp.pi*sp.I
    V = -4*sp.pi*sp.I*dd
    zero("primitive_slope", U+p*V+2*sp.pi*sp.I,
         "U+pV=-2pi i")
    zero("absolute_boundary_correction",
         sp.re(-2*sp.pi*sp.I*p*dd**2+2*sp.pi*sp.I*dd)
         -sp.im(U)*sp.re(V)/(4*sp.pi),
         "mf:boundary-cancel with the original primitive p")
    nonzero("lost_boundary_factor_two",
            sp.re(-2*sp.pi*sp.I*p*dd**2+2*sp.pi*sp.I*dd)
            -sp.im(U)*sp.re(V)/(2*sp.pi),
            "using 1/(2pi) instead of 1/(4pi)")
    rr = sp.Symbol("r", positive=True)
    dx, dt, dy = sp.symbols("dx dtheta dr", real=True)
    original_metric = ((1+rr**2)*dx**2+2*rr*dx*dy+dy**2+dt**2)/rr**2
    tube_metric = dy**2/(rr**2*(1+rr**2))+(1+rr**2)/rr**2*(
        dx+rr/(1+rr**2)*dy)**2+dt**2/rr**2
    zero("tube_metric", tube_metric-original_metric,
         "R=asinh(1/r), X=xi+.5log(1+r^2) give the smooth tube metric")

    here = Path(__file__).resolve().parent
    inputs = [here/"main.tex", Path(__file__).resolve(),
              *sorted((here/"figures").glob("*.tex"))]
    result = {
        "scope": "Finite symbolic algebra only: no packing, development, analytic "
                 "uniformity, topology, completion, Stokes limit, or volume theorem.",
        "method": "Exact rational/polynomial simplification, all free normal-flow "
                  "variables, both orientation signs, all six face permutations, "
                  "and reduced free-group words. No numerical sampling.",
        "source_sha256": {p.relative_to(here).as_posix():
                         hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs},
        "sympy_version": sp.__version__,
        "identities": identities, "identity_count": len(identities),
        "negative_controls": controls, "negative_control_count": len(controls),
    }
    payload = json.dumps(result, indent=2, sort_keys=True)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload)
    print(payload)


if __name__ == "__main__":
    main()
