#!/usr/bin/env python3
"""Certify that a proposed translated terminal contour is not concave.

Requires python-flint. The inputs are exact rational/algebraic numbers;
all elementary functions are evaluated with Arb/Acb enclosures.
"""

from flint import acb, arb, ctx


def main():
    ctx.prec = 180
    pi = arb.pi()
    b = ((arb(2).sqrt() - 1) / 4).sqrt()
    h_t = 2 * (b + (1 + b * b).sqrt()).log()
    h_x = arb(2).log() / (4 * pi)
    x = acb(arb(1) / 200, h_x)
    t = acb(arb(2), -h_t)
    denominator = (2 * pi * x).cos() + t.cos()
    h_xx = (
        -2 * pi * (2 * pi * x).sin() / denominator
        - 4 * pi / (pi * x).tan()
        - 2 * pi * (2 * pi * x).sin()
        / ((2 * pi * x).cos() + 1)
    )
    h_xt = -t.sin() / denominator
    h_tt = -(
        (pi * x + t / 2).tan() + (pi * x - t / 2).tan()
    ) / (4 * pi)
    determinant = h_xx.real * h_tt.real - h_xt.real**2
    assert arb(2) < 2 * pi / 3
    assert arb(1) / 200 + 1 / pi < arb(1) / 2
    assert h_t / (2 * pi) - h_x > 0
    assert determinant < -arb(4) / 5
    print("Real Hessian entries at the exact translated point:")
    print("H_xx =", h_xx.real)
    print("H_xt =", h_xt.real)
    print("H_tt =", h_tt.real)
    print("determinant =", determinant)
    print("Certified: determinant < -4/5 inside the central triangle.")


if __name__ == "__main__":
    main()
