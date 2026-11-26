#!/usr/bin/env python3
"""Outward certificate for the original positive (7,7) pair action.

An untrusted numerical candidate is enclosed by a complex rectangular
contraction. All three original edges, logarithmic periods, and the
normalized sine-primitive action are checked on that full box.
"""
import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp
from flint import acb, arb, ctx


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument("--precision", type=int, default=256)
    parser.add_argument(
        "--output", type=Path,
        default=root/"repro/results/research-pair-seven-action.json")
    args = parser.parse_args()
    assert args.precision >= 160
    ctx.prec = args.precision
    mp.mp.dps = 95
    n = 7
    candidate = mp.findroot(
        lambda t: n*t+2j*(mp.asinh(mp.tan(t/2))
                         +mp.asinh(mp.sin(t/2)))-2*mp.pi,
        mp.mpc(".832", "-.235"), tol=mp.mpf("1e-88"))
    center = acb(mp.nstr(candidate.real, 90),
                 mp.nstr(candidate.imag, 90)).mid()
    centers = [center, center]
    radius = arb(2)**(-100)
    error_box = acb(arb(0, radius), arb(0, radius))
    box = [z+error_box for z in centers]
    I, pi = acb(0, 1), arb.pi()

    def periods(t, u):
        return [
            n*t+2*I*((t/2).tan().asinh()
                     +((t/2).tan()*(u/2).cos()).asinh())-2*pi,
            n*u+2*I*((u/2).tan().asinh()
                     +((u/2).tan()*(t/2).cos()).asinh())-2*pi,
        ]

    def jacobian(t, u):
        ct, cu = (t/2).cos(), (u/2).cos()
        st, su = (t/2).sin(), (u/2).sin()
        tt, tu = (t/2).tan(), (u/2).tan()
        dt, du = (1+(tt*cu)**2).sqrt(), (1+(tu*ct)**2).sqrt()
        return [[n+I*(1/ct+cu/(ct**2*dt)), -I*tt*su/dt],
                [-I*tu*st/du, n+I*(1/cu+ct/(cu**2*du))]]

    jac0 = jacobian(*centers)
    determinant = jac0[0][0]*jac0[1][1]-jac0[0][1]*jac0[1][0]
    inverse = [[(jac0[1][1]/determinant).mid(),
                (-jac0[0][1]/determinant).mid()],
               [(-jac0[1][0]/determinant).mid(),
                (jac0[0][0]/determinant).mid()]]
    jac = jacobian(*box)
    defect = [[acb(int(a == b))-sum(inverse[a][k]*jac[k][b]
                                  for k in range(2))
               for b in range(2)] for a in range(2)]
    residual = periods(*centers)
    images = [
        centers[a]-sum(inverse[a][b]*residual[b] for b in range(2))
        +sum(defect[a][b]*error_box for b in range(2))
        for a in range(2)]
    assert all(box[a].contains_interior(images[a]) for a in range(2))
    contraction = max(sum(abs(v) for v in row).upper() for row in defect)
    assert contraction < arb(1)/2

    t, u = box
    branch_checks = []
    for v, neighbor in ((t, u), (u, t)):
        assert 0 < v.real < pi/2 and v.imag < 0
        assert abs((v/2).cos()) < 1
        z0 = (v/2).tan()
        z1 = z0*(neighbor/2).cos()
        assert z0.real > 0 and z1.real > 0
        assert (1+z0*z0).real > 0 and (1+z1*z1).real > 0
        assert z0.asinh().real > 0 and z1.asinh().real > 0
        branch_checks.append({
            "complete_return_argument": str(z0),
            "internal_return_argument": str(z1),
            "complete_return": str(z0.asinh()),
            "internal_return": str(z1.asinh()),
        })

    positive_edges = []
    for left, right in ((t, acb(0)), (t, u), (u, acb(0))):
        aa, bb = (left/2).tan(), (right/2).tan()
        qq = (1+aa*aa+bb*bb).sqrt()
        margin = qq.real-(aa.real**2+bb.real**2).sqrt()
        assert margin > arb(1)/2
        shapes = [(qq+aa)/(bb-I), (qq-aa)/(bb-I),
                  -(qq-bb)/(aa+I), -(qq+bb)/(aa+I)]
        assert all(shape.imag > 0 for shape in shapes)
        for first, second in ((left, right), (right, left)):
            rr = ((first/2).tan()*(second/2).cos()).asinh()
            assert (qq*(second/2).cos()).real > 0
            assert (rr.cosh()-qq*(second/2).cos()).contains(0)
        positive_edges.append({
            "positive_matrix_margin": str(margin),
            "four_original_shapes": list(map(str, shapes)),
        })

    A, B = (t/2).cos()**2, (u/2).cos()**2
    W = (A*B/(A+B-A*B)).sqrt()
    assert W.real > 0 and W.imag > 0
    x = W.atan()/pi
    assert arb(1)/5 < x.real < arb(1)/4 and x.imag > 0
    assert ((pi*x).tan()-W).contains(0)

    primitive_arguments = []

    def J(z):
        z = acb(z)
        assert 0 < z.real < 1
        primitive_arguments.append(str(z))
        # Principal Li_2 is holomorphic under this exponential map:
        # it avoids [1,infinity) throughout 0<Re z<1.
        return ((pi*pi/6-(2*pi*I*z).exp().polylog(2))/(2*pi*I)
                +I*pi*z*(1-z)/2)

    def Jprime(z):
        assert 0 < z.real < 1
        return (2*(pi*z).sin()).log()

    def b(z, angle):
        plus = arb(1)/2-z+angle/(2*pi)
        minus = arb(1)/2-z-angle/(2*pi)
        return -J(plus)-J(minus)-2*J(z)

    def psi(angle):
        return -4*J(arb(1)/4+angle/(4*pi))-4*J(
            arb(1)/4-angle/(4*pi))

    action = (b(x, t)+b(x, u)+psi(t)+psi(u)
              +I*n*(t*t+u*u)/(4*pi)-I*(t+u))
    assert action.real > arb(163)/50
    assert arb("3.2624704255") < action.real < arb("3.2624704256")

    gx = acb(0)
    angular_gradients = []
    return_lift_checks = []
    for angle, neighbor in ((t, u), (u, t)):
        plus = arb(1)/2-x+angle/(2*pi)
        minus = arb(1)/2-x-angle/(2*pi)
        gx += Jprime(plus)+Jprime(minus)-2*Jprime(x)
        bt = (Jprime(minus)-Jprime(plus))/(2*pi)
        r1 = ((angle/2).tan()*(neighbor/2).cos()).asinh()
        lift = bt+r1/pi
        assert lift.contains(0) and abs(lift) < arb(2)**(-80)
        return_lift_checks.append(str(lift))
        gt = bt-(angle/2).tan().asinh()/pi+I*n*angle/(2*pi)-I
        assert gt.contains(0) and abs(gt) < arb(2)**(-80)
        angular_gradients.append(str(gt))
    assert gx.contains(0) and abs(gx) < arb(2)**(-80)
    # The constant and the regular-strip logarithm are those of the
    # already established phase, not reset independently at the root.
    assert J(arb(1)/2).contains(0)

    inputs = [
        Path(__file__).resolve(),
        root/"notes/research_real_pair_geometry_and_tail_gap.md",
        root/"notes/research_positive_edge_global_monotonicity.md",
        root/"notes/research_radical_path_sector_gap.md",
        root/"notes/research_mixed_wire_phase_concavity.md",
    ]
    record = {
        "status": "certified", "precision_bits": ctx.prec,
        "powers": [n, n], "box_radius": str(radius),
        "center": list(map(str, centers)), "root_box": list(map(str, box)),
        "fixed_point_image": list(map(str, images)),
        "contraction_upper": str(contraction),
        "center_period_residual": list(map(str, residual)),
        "return_branches": branch_checks,
        "positive_original_edges": positive_edges,
        "wire": str(x), "wire_tangent": str(W),
        "primitive_arguments_in_regular_strip": primitive_arguments,
        "wire_gradient": str(gx), "angular_gradients": angular_gradients,
        "return_logarithmic_lifts": return_lift_checks,
        "selected_action": str(action), "real_action": str(action.real),
        "strict_lower_bound": "163/50",
        "scope": (
            "Interval existence for the original unexponentiated (7,7) "
            "period equations, positivity on all three original edges, "
            "and calibrated action M77>163/50. No new quantum coefficient "
            "or volume-limit assertion is inferred from this certificate."),
        "sha256": {
            str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in inputs},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({key: record[key] for key in (
        "status", "powers", "contraction_upper", "wire", "real_action",
        "strict_lower_bound")}, indent=2))


if __name__ == "__main__":
    main()
