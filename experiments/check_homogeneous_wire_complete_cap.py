#!/usr/bin/env python3
"""Outward scalar certificate for the actual cap at the homogeneous wire.

The proof supplies the global contour inequalities. This script checks
the selected analytic period zero and the finite scalar premises of
that proof, with no finite-level quantum extrapolation or sampling.
"""

from __future__ import annotations

import argparse
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
    root3 = arb(3).sqrt()
    q = 2 / root3 - ii
    x = acb(arb(1) / 6, arb(2).log() / (2 * pi))
    center = acb(arb(1567043151) / 10**9, -arb(992123761) / 10**9)
    radius = arb(1) / 10**8
    disk_box = acb(center.real + arb(0, radius), center.imag + arb(0, radius))
    checks = []

    def positive(name, value):
        assert value > 0, (name, value)
        checks.append({"name": name, "positive_margin": str(value)})

    def period(t):
        z = (t / 2).tan()
        sec = 1 / (t / 2).cos()
        return 3 * t + 2 * ii * (z + sec).log() + ii * ((q + z).log() - (q - z).log()) - 2 * pi

    def first_period_derivative(t):
        z = (t / 2).tan()
        sec = 1 / (t / 2).cos()
        return 3 + ii * (sec + q * sec**2 / (q*q - z*z))

    z = (disk_box / 2).tan()
    sec = 1 / (disk_box / 2).cos()
    dz = (1 + z*z) / 2
    ddz = z * (1 + z*z) / 2
    second = 2 * ii * (sec*z/4 + q*(ddz/(q*q-z*z) + 2*z*dz*dz/(q*q-z*z)**2))
    positive("cos-half has positive real part", (disk_box / 2).cos().real)
    positive("asinh logarithm has positive real part", (z + sec).real)
    positive("first atanh logarithm has positive real part", (q + z).real)
    positive("second atanh logarithm has positive real part", (q - z).real)
    linear = abs(first_period_derivative(center)) * radius
    error = abs(period(center)) + abs(second) * radius**2 / 2
    positive("Rouche linear term exceeds exact residual and Taylor remainder", linear - error)

    def J(value):
        value = acb(value)
        return (-ii*pi*(value*value-value)/2
                + ii*(2*ii*pi*value).exp().polylog(2)/(2*pi) - ii*pi/12)

    def b(t):
        return -J(arb(1)/2-x+t/(2*pi)) - J(arb(1)/2-x-t/(2*pi)) - 2*J(x)

    def psi(t):
        return -4*J(arb(1)/4+t/(4*pi)) - 4*J(arb(1)/4-t/(4*pi))

    def phase(t):
        return b(t) + psi(t) + 3*ii*t*t/(4*pi) - ii*t

    T, H = arb(41)/20, -disk_box.imag
    M = phase(disk_box).real
    positive("selected real angle positive", disk_box.real)
    positive("selected real angle below pi/2", pi/2-disk_box.real)
    positive("height exceeds log2", H-arb(2).log())
    positive("height below 107/100", arb(107)/100-H)
    positive("selected cosine modulus below one", 1-abs((disk_box/2).cos()))
    positive("cut below 2pi/3", 2*pi/3-T)
    positive("whole spectral rectangle real color below 3/2", arb(3)/2+2*T.cos()*H.cosh())
    positive("endpoint angular alpha condition", 1+T.cos()*H.cosh())
    positive("wire alpha condition", 1-arb(1)/2*arb(2).log().cosh())
    positive("outer radical rate gap greater than 3/5", M-b(acb(0)).real-arb(3)/5)
    positive("real cut rate gap greater than 1/50", M-phase(acb(T)).real-arb(1)/50)
    positive("lower cut rate gap greater than 1/25", M-phase(acb(T,-H)).real-arb(1)/25)
    positive("regular factorial real-strip margin", arb(1)/2-x.real-T/(2*pi))

    tp, tm = (pi*x+disk_box/2).tan(), (pi*x-disk_box/2).tan()
    ftt = -(tp+tm+2/(disk_box/2).cos())/(4*pi) + 3*ii/(2*pi)
    positive("selected negative real Hessian exceeds 1/3", -ftt.real-arb(1)/3)
    sx = (pi*x+disk_box/2).cos().log() + (pi*x-disk_box/2).cos().log() - 2*(pi*x).sin().log()
    bxx = -pi*(tp+tm+2/(pi*x).tan())
    bxt = (tm-tp)/2
    sxx = bxx-bxt*bxt/ftt
    positive("actual wire phase gradient is nonzero", -sx.imag-arb(1)/3)
    positive("actual wire negative real Hessian exceeds 10", -sxx.real-10)

    task_root = Path(__file__).resolve().parents[1]
    dependencies = [
        Path(__file__).resolve(),
        task_root / "notes/research_homogeneous_wire_complete_cap.md",
        task_root / "notes/research_internal_pair_three_mixed_packet.md",
        task_root / "notes/research_mixed_wire_phase_concavity.md",
        task_root / "notes/research_free_boundary_half_charge_observation.md",
        task_root / "notes/research_pair_free_boundary_kernel.md",
        task_root / "notes/research_last_physical_row_riccati.md",
        task_root / "notes/research_even_complete_low_kernel.md",
        task_root / "notes/research_exact_complete_trace_contour.md",
        task_root / "notes/research_terminal_real_angle_tail.md",
    ]
    result = {
        "status": "passed",
        "precision_bits": ctx.prec,
        "scope": (
            "Outward analytic-period Rouche disk and finite scalar contour premises. "
            "The global real-part inequalities and the original-source passage are "
            "proved in the note, not inferred from sampling. No long-chain quantum "
            "or complete wire-period assertion is checked."
        ),
        "checks": checks,
        "check_count": len(checks),
        "root_center": str(center),
        "root_radius": str(radius),
        "root_enclosing_box": str(disk_box),
        "rouche_linear_lower": str(linear),
        "rouche_error_upper": str(error),
        "phase": str(phase(disk_box)),
        "phase_t_second_derivative": str(ftt),
        "actual_wire_phase_gradient": str(sx),
        "actual_wire_phase_second_derivative": str(sxx),
        "sha256": {str(p.relative_to(task_root)): hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in dependencies},
    }
    output = args.output or task_root / "repro/results/research-homogeneous-wire-complete-cap.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(f"Passed {len(checks)} outward scalar comparisons at {ctx.prec} bits.\n{output}")


if __name__ == "__main__":
    main()
