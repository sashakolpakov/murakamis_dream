#!/usr/bin/env python3
"""Explore candidate contours; numerical optimization here is NOT a proof.

This records why a whole rectangular translation is insufficient for
small powers, and why a coupled deformation at a cutoff may help.
"""

import json
import math

import numpy as np
from scipy.optimize import differential_evolution, root
from scipy.special import spence


def primitive_bulk(z):
    return (
        -0.5j * np.pi * (z * z - z)
        + 0.5j * spence(1 - np.exp(2j * np.pi * z)) / np.pi
        - 1j * np.pi / 12
    )


def primitive(z):
    if z.real < 0:
        side = 1 if z.imag >= 0 else -1
        return -primitive_bulk(-z) + side * 1j * np.pi * z
    return primitive_bulk(z)


def boundary_phase(x, t):
    return (
        primitive(0.5 + t / (2 * np.pi))
        + primitive(0.5 - t / (2 * np.pi))
        - primitive(0.5 - x + t / (2 * np.pi))
        - primitive(0.5 - x - t / (2 * np.pi))
        - 2 * primitive(x)
    )


def selected_saddle(power):
    def equations(value):
        angle, depth = value
        return [
            math.sin(angle) - math.cosh(depth) * math.tanh(power * depth),
            power * angle
            + math.atan(math.sinh(depth) / math.cos(angle))
            - math.pi,
        ]

    solution = root(equations, [math.pi / (power + 1), 1 / power**2])
    if not solution.success:
        raise RuntimeError(solution.message)
    angle, depth = solution.x
    t = 2 * angle - 2j * depth
    x = np.arctan(np.cos(t / 2)) / np.pi
    return x, t


def explore(power):
    x_saddle, t_saddle = selected_saddle(power)

    def real_phase(x, t):
        return float(
            (
                boundary_phase(x, t)
                + boundary_phase(x, 0)
                + 1j * power * t * t / (4 * np.pi)
                - 1j * t
            ).real
        )

    def maximize(function, bounds):
        result = differential_evolution(
            lambda parameters: -function(*parameters),
            bounds,
            seed=17,
            tol=1e-10,
            polish=True,
        )
        return {"sampled_maximum": float(-result.fun), "parameters": result.x.tolist()}

    edge = 1e-6
    whole_rectangle = maximize(
        lambda x, t: real_phase(x + 1j * x_saddle.imag, t + 1j * t_saddle.imag),
        [(edge, 0.5 - edge), (edge, np.pi - edge)],
    )
    cutoff = 2 * np.pi / 3
    retained_rectangle = maximize(
        lambda x, t: real_phase(x + 1j * x_saddle.imag, t + 1j * t_saddle.imag),
        [(edge, 0.5 - edge), (edge, cutoff)],
    )
    coupled_face = maximize(
        lambda x, homotopy: real_phase(
            x + 1j * x_saddle.imag * homotopy,
            cutoff + 1j * t_saddle.imag * homotopy,
        ),
        [(edge, 0.5 - edge), (edge, 1)],
    )
    return {
        "power": power,
        "saddle_wire": [float(x_saddle.real), float(x_saddle.imag)],
        "saddle_angle": [float(t_saddle.real), float(t_saddle.imag)],
        "selected_real_action": real_phase(x_saddle, t_saddle),
        "whole_translated_rectangle": whole_rectangle,
        "retained_translated_rectangle": retained_rectangle,
        "coupled_cutoff_face": coupled_face,
    }


def main():
    print(json.dumps({
        "status": "Floating-point diagnostics; no certified global maxima or contour theorem.",
        "powers": [explore(power) for power in (3, 4, 5, 8)],
    }, indent=2))


if __name__ == "__main__":
    main()
