#!/usr/bin/env python3
"""Certify two action bounds used in the terminal real-angle tail proof.

This is a rigorous ball-arithmetic check of explicit constants. It does
not certify a global contour or a volume asymptotic.
"""

from flint import acb, arb, ctx


def main():
    ctx.prec = 180
    pi = arb.pi()
    imaginary = acb(0, 1)
    half = arb(1) / 2

    def primitive(z):
        z = acb(z)
        assert z.real > 0 and z.real < 1, "Outside the chosen bulk branch"
        return (
            -imaginary * pi * (z * z - z) / 2
            + imaginary * (2 * imaginary * pi * z).exp().polylog(2) / (2 * pi)
            - imaginary * pi / 12
        )

    def boundary_phase(x, t):
        return (
            primitive(half + t / (2 * pi))
            + primitive(half - t / (2 * pi))
            - primitive(half - x + t / (2 * pi))
            - primitive(half - x - t / (2 * pi))
            - 2 * primitive(x)
        )

    k = (arb(7).sqrt() + imaginary) / 4
    terminal_angle = 2 * k.acos()
    wire = k.atan() / pi
    action = (
        boundary_phase(wire, terminal_angle)
        + boundary_phase(wire, acb(0))
        + 3 * imaginary * terminal_angle * terminal_angle / (4 * pi)
        - imaginary * terminal_angle
    )
    cutoff = 2 * pi / 3
    cutoff_wire = acb(half).atan() / pi
    tail = boundary_phase(cutoff_wire, cutoff) + boundary_phase(cutoff_wire, acb(0))
    assert tail.imag.contains(0), "The real tail action must be real"
    assert tail.real < arb(4) / 5
    assert action.real > arb(5) / 6
    assert action.real - tail.real > arb(1) / 30
    print("Outer-angle action:", tail.real)
    print("Selected three-crossing action:", action.real)
    print("Certified gap:", action.real - tail.real)
    print("Certified: tail < 4/5 < 5/6 < selected action.")


if __name__ == "__main__":
    main()
