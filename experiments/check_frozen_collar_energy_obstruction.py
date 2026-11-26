#!/usr/bin/env python3
"""Certify the convex supporting-plane obstruction for a fixed collar.

This checks one exact algebraic configuration and one supporting plane.
It does not sample the feasible set or bound the unrestricted energy
minimum. The reduction to this plane is proved in the linked note.
"""

import argparse
import hashlib
import json
from pathlib import Path

from flint import acb, acb_poly, arb, ctx


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default=
                        "repro/results/research-frozen-collar-energy.json")
    args = parser.parse_args()
    ctx.prec = 192
    pi = arb.pi()
    imaginary = acb(0, 1)
    catalan = arb.const_catalan()
    complete_action = 4*catalan/pi

    # The roots routine encloses the roots of this exact integer polynomial.
    polynomial = [2, -2, 1, -4, 4]
    roots = acb_poly(polynomial).roots(tol=1e-40, maxprec=1024)
    selected = [z for z in roots
                if z.real > arb(".84") and z.real < arb(".85")
                and z.imag > arb(".29") and z.imag < arb(".30")]
    assert len(roots) == 4 and len(selected) == 1
    k = selected[0]
    for other in roots:
        if other is not k:
            assert other.real < 0 or other.imag < 0
    half_angle = k.acos()
    angle = 2*half_angle
    return_value = imaginary*(3*half_angle-pi)/2

    # The polynomial identity gives cos(3a/2)^2+tan(a)^2=0.
    # Excluding the opposite factor selects cos(3a/2)=i tan(a).
    opposite_factor = (3*half_angle/2).cos()+imaginary*half_angle.tan()
    assert abs(opposite_factor) > 1
    assert return_value.real > 0
    assert return_value.imag > -pi/2 and return_value.imag < pi/2
    assert angle.real > 0 and angle.real < pi
    assert angle.imag < 0

    old_s = angle.real
    old_g = (3*old_s/2-pi)/2
    assert old_g < 0 and old_g > -pi/2
    x = -old_g/2
    y = old_s/4

    def j_function(z):
        return (imaginary*pi*(z-z*z)/2
                + imaginary*((2*pi*imaginary*z).exp().polylog(2)
                             - pi*pi/6)/(2*pi))

    def square_energy(a, b):
        assert abs(a) < pi/4 and abs(b) < pi/4
        first, second = 4*a, 4*b
        c, d = first.cos(), second.cos()
        wire = ((1-c*d)/(2+c+d)).acos()/(2*pi)

        def newton_phase(t):
            left = arb(1)/2-wire+t/(2*pi)
            right = arb(1)/2-wire-t/(2*pi)
            assert left > 0 and left < 1
            assert right > 0 and right < 1
            assert wire > 0 and wire < 1
            return (-j_function(acb(left))-j_function(acb(right))
                    - 2*j_function(acb(wire)))

        phase = (newton_phase(first)+newton_phase(second)).real
        return pi*(complete_action-phase)/8

    def square_gradient(a, b):
        return (((2*a).tan()*(2*b).cos()).asinh()/2,
                ((2*b).tan()*(2*a).cos()).asinh()/2)

    # These rational coordinates are arbitrary test inputs, not asserted roots.
    s = arb("1.59335955")
    g = arb("-.39124668")
    center = ((pi+g-s)/2, s-(pi+g)/2)
    first = (x+s/4, y+g/2)
    second = (x-s/4, y-g/2)
    for a, b in [center, first, second, (x, y)]:
        assert abs(a) < pi/4 and abs(b) < pi/4

    value = (8*square_energy(*center)
             + 8*(square_energy(*first)+square_energy(*second)
                  - 2*square_energy(x, y)))
    dc = square_gradient(*center)
    dp = square_gradient(*first)
    dq = square_gradient(*second)
    ds = -4*dc[0]+8*dc[1]+2*(dp[0]-dq[0])
    dg = 4*dc[0]-4*dc[1]+4*(dp[1]-dq[1])
    assert abs(s) < pi and abs(g) < pi/2
    supporting_lower = value-2*pi*abs(ds)-pi*abs(dg)

    assert supporting_lower > arb(37)/10
    assert 4*catalan < arb(458)/125
    assert supporting_lower-4*catalan > arb(9)/250

    script = Path(__file__).resolve()
    root = script.parent.parent
    note = root/"notes/research_edge_cut_energy_comparison.md"
    record = {
        "status": "passed",
        "arithmetic": "python-flint complex and real balls",
        "precision_bits": ctx.prec,
        "scope": ("Four selected power-three vertices; old one-vertex halves "
                  "fixed; arbitrary feasible changes at the two middle "
                  "vertices. Not the unrestricted minimum."),
        "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
        "note_sha256": hashlib.sha256(note.read_bytes()).hexdigest(),
        "old_root_polynomial_coefficients_ascending": polynomial,
        "selected_root": str(k),
        "old_angle": str(angle),
        "old_return_imaginary_part": str(old_g),
        "test_point": {"s": "1.59335955", "g": "-.39124668"},
        "test_value": str(value),
        "gradient_s": str(ds),
        "gradient_g": str(dg),
        "supporting_plane_lower_bound": str(supporting_lower),
        "four_catalan": str(4*catalan),
        "certified_uniform_gap_lower": "9/250",
    }
    output = root/args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, indent=2)+"\n")
    print("Passed: every feasible fixed-collar cost exceeds 4G by 9/250.")


if __name__ == "__main__":
    main()
