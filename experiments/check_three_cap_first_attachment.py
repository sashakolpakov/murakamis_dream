#!/usr/bin/env python3
"""Outward analytic Newton certificate for the first retained-vertex attachment.

This checks the original continued cap period and the exact retained
critical branch. It proves a local critical point and derivative bounds;
it does not estimate the complementary full wire contour.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

from flint import acb, arb, ctx


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=192)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    ctx.prec = args.precision
    pi, ii = arb.pi(), acb(0, 1)

    def rat(s):
        q = Q(s)
        return arb(q.numerator)/q.denominator

    def point(real, imag):
        return acb(rat(real), rat(imag))

    y = acb(arb(1)/6, arb(2).log()/(2*pi))
    centers = [point(".177337918569469382175948562048", ".101358689576302370861575311618"),
               point("1.533800710765884206016520588964", "-.978955098405739999074096803416")]
    radius = rat("1e-8")
    boxes = [acb(z.real+arb(0, radius), z.imag+arb(0, radius)) for z in centers]
    preconditioner = [
        [point("-.012459042950055255651267420891", ".009121085447815058535390706888"),
         point("-.030322991884195644218839259185", "-.022730223128523958826095306578")],
        [point(".222750256842225811720371833986", "-.117735701411284707218221686158"),
         point(".057309470071241114644219436946", ".078282475605306592775433429801")],
    ]

    def retained(x):
        X, Y = (2*pi*ii*x).exp(), (2*pi*ii*y).exp()
        alpha, beta = 1/X-1, 1/Y-1
        root = (1-2*(alpha+beta)+(alpha-beta)**2).sqrt()
        U, V = (1+alpha-beta-root)/2, (1-alpha+beta-root)/2
        alpha_x, beta_y = -2*pi*ii/X, -2*pi*ii/Y
        Ux = alpha_x*(1-(alpha-beta-1)/root)/2
        Uy = beta_y*(-1-(beta-alpha-1)/root)/2
        Vy = beta_y*(1-(beta-alpha-1)/root)/2
        px = -U.log()+(1-X*U).log()-(1-X).log()-pi*ii
        py = -V.log()+(1-Y*V).log()-(1-Y).log()-pi*ii
        pxx = -Ux/U-(2*pi*ii*X*U+X*Ux)/(1-X*U)+2*pi*ii*X/(1-X)
        pxy = -Uy/U-X*Uy/(1-X*U)
        pyy = -Vy/V-(2*pi*ii*Y*V+Y*Vy)/(1-Y*V)+2*pi*ii*Y/(1-Y)
        return dict(X=X, Y=Y, root=root, U=U, V=V, px=px, py=py,
                    pxx=pxx, pxy=pxy, pyy=pyy)

    def system(x, t):
        data = retained(x)
        q, z, sec = 1/(pi*x).tan(), (t/2).tan(), 1/(t/2).cos()
        period = 3*t+2*ii*(z+sec).log()+ii*((q+z).log()-(q-z).log())-2*pi
        ft = 3+ii*(sec+q*sec**2/(q-z)/(q+z))
        fx = 2*pi*ii*z*(1+q*q)/(q-z)/(q+z)
        tp, tm = (pi*x+t/2).tan(), (pi*x-t/2).tan()
        bx = (pi*x+t/2).cos().log()+(pi*x-t/2).cos().log()-2*(pi*x).sin().log()
        bxx, bxt = -pi*(tp+tm+2*q), (tm-tp)/2
        return [period, bx+data["px"]], [[fx, ft], [bxx+data["pxx"], bxt]], data, (bxx, bxt, ii*ft/(2*pi))

    residual, _, _, _ = system(*centers)
    _, jacobian, data, (bxx, bxt, ftt) = system(*boxes)
    defect = [[acb(int(i == j))-sum(preconditioner[i][k]*jacobian[k][j] for k in range(2))
               for j in range(2)] for i in range(2)]
    row_norms = [sum(abs(z) for z in row) for row in defect]
    displacements = [abs(sum(preconditioner[i][k]*residual[k] for k in range(2))) for i in range(2)]
    checks = []

    def positive(name, value):
        assert value > 0, (name, value)
        checks.append({"name": name, "positive_margin": str(value)})

    for i in range(2):
        positive(f"Newton row {i}: contraction below 1/1000", rat(".001")-row_norms[i])
        positive(f"Newton row {i}: maps polydisk strictly inside itself", radius-displacements[i]-row_norms[i]*radius)
    x, t = boxes
    q, z, sec = 1/(pi*x).tan(), (t/2).tan(), 1/(t/2).cos()
    for name, value in [("cap q+z log", q+z), ("cap q-z log", q-z),
                        ("cap sec+z log", sec+z), ("retained square root", data["root"]),
                        ("cap numerator plus", (pi*x+t/2).cos()),
                        ("cap numerator minus", (pi*x-t/2).cos()),
                        ("cap sine", (pi*x).sin())]:
        positive(name+": right half-plane", value.real)
    r = x.real-arb(1)/6
    s = x.imag-y.imag+arb(4)/5*r
    positive("wire corridor r lower", r)
    positive("wire corridor r upper", rat(".013")-r)
    positive("wire corridor s lower", s+rat(".0015"))
    positive("wire corridor s upper", rat(".001")-s)
    positive("cap angle lower", t.real-rat("1.52"))
    positive("cap angle upper", rat("1.575")-t.real)
    positive("cap height lower", -t.imag-rat(".97"))
    positive("cap height upper", 1+t.imag)
    for name in ("X", "Y"):
        positive(name+": first quadrant real", data[name].real-rat(".08"))
        positive(name+": first quadrant imaginary", data[name].imag-rat(".08"))
        positive(name+": modulus below 4/5", rat(".8")-abs(data[name]))
    for name, parameter in (("U", "X"), ("V", "Y")):
        value = data[name]
        positive(name+": negative real part", -value.real)
        positive(name+": negative imaginary part", -value.imag)
        positive(parameter+name+": modulus below one", 1-abs(data[parameter]*value))
        index = ii*value.log()/(2*pi)
        positive(name+": index real above 1/4", index.real-arb(1)/4)
        positive(name+": index real below 49/100", rat(".49")-index.real)
        positive(name+": index height lower", index.imag+rat(".03"))
        positive(name+": index height upper", rat(".03")-index.imag)
    cap_second = bxx-bxt*bxt/ftt
    total_second = cap_second+data["pxx"]
    outgoing_second = data["pyy"]-data["pxy"]**2/total_second
    derivative = -data["pxy"]/total_second
    positive("negative real composed wire Hessian above 21", -total_second.real-21)
    positive("outgoing negative real Hessian above 9", -outgoing_second.real-9)
    positive("outgoing phase gradient modulus below 2/25", rat(".08")-abs(data["py"]))
    positive("critical wire response modulus below 21/100", rat(".21")-abs(derivative))

    def sine_primitive(value):
        value = acb(value)
        return (-ii*pi*(value*value-value)/2
                +ii*(2*pi*ii*value).exp().polylog(2)/(2*pi)-ii*pi/12)

    def denominator_primitive(index, parameter):
        return ((parameter*(-2*pi*ii*index).exp()).polylog(2)
                -parameter.polylog(2))/(2*pi*ii)

    s_index = ii*data["U"].log()/(2*pi)
    t_index = ii*data["V"].log()/(2*pi)
    summed_index = s_index+t_index
    retained_action = (sine_primitive(summed_index)
                       +ii*pi*(summed_index-summed_index*summed_index)/2
                       +s_index*data["X"].log()+t_index*data["Y"].log()
                       -denominator_primitive(s_index, data["X"])
                       -denominator_primitive(t_index, data["Y"])-pi*ii*(x+y))
    cap_action = (-sine_primitive(arb(1)/2-x+t/(2*pi))
                  -sine_primitive(arb(1)/2-x-t/(2*pi))-2*sine_primitive(x)
                  -4*sine_primitive(arb(1)/4+t/(4*pi))
                  -4*sine_primitive(arb(1)/4-t/(4*pi))
                  +3*ii*t*t/(4*pi)-ii*t)
    total_action = cap_action+retained_action
    positive("actual composed action above 19113/10000", total_action.real-rat("1.9113"))

    root = Path(__file__).resolve().parents[1]
    dependencies = [Path(__file__).resolve(), root/"notes/research_homogeneous_wire_complete_cap.md",
                    root/"notes/research_three_vertex_central_index_chart.md",
                    root/"notes/research_three_vertex_local_composition.md",
                    root/"notes/research_three_vertex_directed_packet.md"]
    proof = root/"notes/research_three_cap_first_attachment.md"
    if proof.exists():
        dependencies.append(proof)
    record = {
        "status": "passed", "precision_bits": ctx.prec,
        "scope": "Two-complex-variable analytic Newton contraction, exact continued critical branches, directed-domain inclusion and local derivative bounds. The source packets and restricted Gaussian integration are written proofs. No complementary full wire-period bound is checked.",
        "center": [str(z) for z in centers], "polydisk_radius": str(radius),
        "preconditioner": [[str(z) for z in row] for row in preconditioner],
        "Newton_contraction_rows": [str(z) for z in row_norms],
        "Newton_center_displacements": [str(z) for z in displacements],
        "directed_wire_coordinates": [str(r), str(s)],
        "effective_wire_Hessian": str(total_second),
        "outgoing_phase_gradient": str(data["py"]),
        "outgoing_phase_Hessian": str(outgoing_second),
        "critical_wire_response": str(derivative),
        "actual_composed_action": str(total_action),
        "check_count": len(checks), "checks": checks,
        "sha256": {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in dependencies},
    }
    output = args.output or root/"repro/results/research-three-cap-first-attachment.json"
    output.write_text(json.dumps(record, indent=2)+"\n")
    print(f"Passed {len(checks)} outward comparisons at {ctx.prec} bits.\n{output}")


if __name__ == "__main__":
    main()
