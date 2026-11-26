#!/usr/bin/env python3
"""Certify failure of one proposed flat contour, not of a volume limit."""
from flint import acb, arb, ctx
import certify_terminal_three_central_phase as e


def main():
    ctx.prec = 160
    pi, I, half = arb.pi(), acb(0, 1), arb(1) / 2
    hx = arb(3).log() / (4 * pi)
    ht = (2 + arb(3).sqrt()).log()

    def phase(x, t):
        p, m, J = half + t / (2 * pi), half - t / (2 * pi), e.Js
        A = (J(p, -1) + J(m, 1) - J(p-x, -1) - J(m-x, 1)
             + 2*J(half, 1) - 2*J(half-x, -1) - 4*J(x, 1))
        return 2*A + I*t*t/(2*pi) - I*t

    selected_x, selected_t = acb(arb(1)/4, hx), acb(pi/2, -ht)
    trial_x, trial_t = acb(arb(21)/80, hx), acb(2*pi/3, -ht)
    excess = (phase(trial_x, trial_t)-phase(selected_x, selected_t)).real
    assert ht/(2*pi) > hx > 0
    assert excess > arb(1)/100
    print("Degree 2, power 2; excess on the proposed flat contour:")
    print(excess)
    print("The excess is rigorously greater than 1/100.")


if __name__ == "__main__":
    main()
