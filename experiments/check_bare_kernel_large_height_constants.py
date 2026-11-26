#!/usr/bin/env python3
"""Outward scalar checks for the large-height edge-kernel proof.

The analytic contour, branches, and finite-source reconstruction are
written in the proof note. No parameter samples stand in for those
uniform arguments: this script checks their explicit endpoint constants.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json

from flint import arb, ctx


def main():
    root = Path(__file__).resolve().parents[1]
    ctx.prec = 192
    pi = arb.pi()

    def ball(q):
        q = Q(q)
        return arb(q.numerator) / q.denominator

    a, b, h = ball(Q(1, 10)), ball(Q(3, 10)), ball(Q(3, 100))
    cb0 = (pi*b).tan()/(4*pi)
    cb1 = (2*pi*b).sin()/(4*pi*(ball(Q(1, 2))+(2*pi*b).cos()))
    margins = {
        "cosine_real_lower": arb(1).cos()-ball(Q(27, 50)),
        "cosine_real_upper": ball(Q(523, 500))-b.cosh(),
        "cosine_imaginary_upper": ball(Q(129, 500))-arb(1).sin()*b.sinh(),
        "critical_real_lower": (2*pi*ball(Q(21, 100))).cos()-ball(Q(23, 100)),
        "critical_real_upper": -ball(Q(9, 200))-(2*pi*ball(Q(13, 50))).cos(),
        "critical_imaginary_height": ball(Q(23, 1000))-ball(Q(14, 97))/(2*pi),
        "real_critical_above_one_fifth": (2*pi/5).cos()-ball(Q(23, 100)),
        "height_cost_constant": ball(Q(11, 100))-cb0,
        "height_cost_chord_endpoint": ball(Q(2, 5))-cb1,
        "right_endpoint_tangent_lower": (pi*b).tan()-ball(Q(11, 8)),
        "atanh_argument_below_one": 1-(pi*b).tan()*ball(Q(1, 2)).tan(),
        "right_endpoint_constant_gap": pi/100-ball(Q(198, 10000))-ball(Q(1, 100)),
        "right_endpoint_quadratic_reserve": ((pi*b).tan()-1)/(4*pi)-ball(Q(261, 10000)),
        "left_endpoint_gap": 4*pi/100-ball(Q(9, 125))-ball(Q(1, 25)),
        "negative_tangent_bound": ball(Q(1, 5))+(pi*a-ball(Q(1, 2))).tan(),
        "cotangent_real_lower": (2*pi*b).sin()/((2*pi*h).cosh()-(2*pi*b).cos())-ball(Q(7, 10)),
        "cotangent_monotonicity": 1-(2*pi*a).cos()*(2*pi*h).cosh(),
        "numerator_real_lower": (2*pi*b).cos()*(2*pi*h).cosh()+arb(1).cos()-ball(Q(11, 50)),
        "numerator_imaginary_upper": ball(Q(9, 20))-(2*pi*h).sinh()-arb(1).sin()*b.sinh(),
        "numerator_argument_bound": ball(Q(9, 8)).tan()-ball(Q(45, 22)),
        "sine_argument_bound": ball(Q(3, 10)).tan()-(pi*a).cot()*(pi*h).tanh(),
        "horizontal_lattice_gap": (2*pi-ball(Q(7, 2)))*h-ball(Q(9, 125))-ball(Q(1, 100)),
        "upper_tail_cosine_square": ball(Q(7, 20))-(pi*b).cos()**2,
        "upper_tail_sine_square": (pi*b).sin()**2-ball(Q(13, 20)),
        "upper_tail_parameter_square": ball(Q(13, 50))-(ball(Q(1, 2))).sin()**2-(b/2).sinh()**2,
        "lower_tail_multiplier": ((2*pi*a).cos()+ball(Q(27, 50)))/(2*(pi*a).sin()**2)-1,
        "high_half_gap": ball(Q(10, 11))-ball(Q(3, 5)),
        "factorial_strip_lower": ball(Q(1, 2))-b-1/(2*pi),
        "factorial_strip_upper": 1-(ball(Q(1, 2))-a+1/(2*pi)),
    }
    # C bounds use rational identities, so their numerical margins
    # are checked without any floating-point enclosure.
    beta, smin = Q(129, 500), Q(77, 25)
    imag_c = beta/2*(1+(Q(253, 500)**2+Q(129, 250)**2)/smin**2)
    rational = {
        "critical_C_real_lower": Q(9, 200)-Q(23, 1000)-beta**2/smin,
        "critical_C_imaginary_upper": Q(7, 50)-imag_c,
        "critical_sine_lower": 1-Q(23, 100)**2-Q(97, 100)**2,
        "critical_height_inside_contour": Q(3, 100)-Q(23, 1000),
        "Ax_imaginary_bound": Q(7, 2)-2*Q(9, 8)-4*Q(3, 10),
        "upper_tail_ratio_below_one": 1-Q(61, 65),
        "right_connector_distance": Q(3, 10)-Q(13, 50),
        "left_connector_distance": Q(21, 100)-Q(1, 10),
    }
    # The bracket lower bound is strict because every analytic
    # ingredient is strict; verify its exact boundary value too.
    assert 4*Q(7, 10)-4*Q(1, 5) == 2
    for name, value in margins.items():
        assert value > 0, (name, value)
    for name, value in rational.items():
        assert value > 0, (name, value)
    dependencies = [
        "notes/research_bare_kernel_thin_rectangle.md",
        "notes/research_edge_hessian_and_phase_response.md",
        "notes/research_exact_cyclotomic_factorial.md",
        "papers/circle-tree-volume/finite-bounds.tex",
        "experiments/check_bare_kernel_large_height_constants.py",
    ]
    record = {
        "status": "passed",
        "scope": "Scalar endpoint inequalities only; the uniform analytic argument remains a written proof.",
        "precision_bits": ctx.prec,
        "interval_comparison_count": len(margins),
        "rational_comparison_count": len(rational),
        "exact_identity_count": 1,
        "interval_margins": {name: str(value) for name, value in margins.items()},
        "rational_margins": {name: str(value) for name, value in rational.items()},
        "dependencies": {name: sha256((root/name).read_bytes()).hexdigest()
                         for name in dependencies},
    }
    output = root/"repro/results/research-bare-kernel-large-height.json"
    output.write_text(json.dumps(record, indent=2)+"\n")
    print(f"Passed {len(margins)} outward interval comparisons, "
          f"{len(rational)} rational comparisons and 1 identity; "
          f"{output.relative_to(root)}")


if __name__ == "__main__":
    main()
