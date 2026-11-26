#!/usr/bin/env python3
"""Floating-point exploration of the scaled isolated-vertex surfaces.

No optimizer output in this script is a certified maximum or a proof.
The surfaces are those of the trace-first decomposition: there is no
interior angular homotopy. A lower-wire penalty is multiplied by d in
the scaled phase, so averaging over d wires restores its actual cost.
"""

import argparse
import json
from pathlib import Path

import numpy as np
from scipy.optimize import differential_evolution, root
from scipy.special import spence


PI = np.pi


def upper_primitive(z):
    z = complex(z)
    return (-0.5j * PI * (z * z - z)
            + 0.5j * spence(1 - np.exp(2j * PI * z)) / PI
            - 1j * PI / 12)


def primitive(z, side):
    return (upper_primitive(z) if side == 1
            else -upper_primitive(-z) - 1j * PI * z)


def phase(x, t, degree, power, side):
    p, m = 0.5 + t / (2 * PI), 0.5 - t / (2 * PI)
    block = (primitive(p, -1) + primitive(m, 1)
             - primitive(p - x, -1) - primitive(m - x, 1)
             + 2 * primitive(0.5, 1)
             - 2 * primitive(0.5 - x, -side)
             - 4 * primitive(x, side))
    return degree * block + 1j * power * t * t / (4 * PI) - 1j * t


def saddle(degree, power):
    def equations(values):
        a, b = values
        return [
            np.sin(a) - np.cosh(b) * np.tanh(power * b / degree),
            power * a + degree * np.arctan(np.sinh(b) / np.cos(a)) - PI,
        ]

    scale = degree**2 + power**2
    result = root(equations, [PI * power / scale, PI * degree / scale],
                  tol=1e-12)
    if np.max(np.abs(equations(result.x))) > 1e-10:
        raise ArithmeticError(result.message)
    a, b = result.x
    t = 2 * a - 2j * b
    x = np.arctan(np.cos(t / 2)) / PI
    if not (x.imag > 0 and -t.imag / (2 * PI) > x.imag):
        raise ArithmeticError("The prescribed denominator half-planes failed")
    return x, t


def explore(degree, power, alpha, seed):
    beta, cutoff = 0.5 - alpha, 2 * PI / 3
    xs, ts = saddle(degree, power)
    hx, ht = xs.imag, -ts.imag
    selected = phase(xs, ts, degree, power, 1).real
    penalty = degree * 2 * PI * hx
    rows = []

    def maximize(name, function, bounds):
        result = differential_evolution(
            lambda values: -function(*values), bounds, seed=seed,
            popsize=16, maxiter=400, tol=1e-10, polish=True,
        )
        maximum = float(-result.fun)
        rows.append({
            "surface": name, "sampled_maximum": maximum,
            "selected_minus_sampled_maximum": float(selected - maximum),
            "parameters": result.x.tolist(), "optimizer_success": bool(result.success),
        })
        print(f"d={degree}, n={power}: {name}: "
              f"gap {selected - maximum:.12g}", flush=True)

    def value(x, t, side):
        return float(phase(x, t, degree, power, side).real)

    maximize("central_positive",
             lambda x, t: value(x + 1j * hx, t - 1j * ht, 1),
             [(alpha, beta), (0, cutoff)])
    maximize("central_negative",
             lambda x, t: value(x + 1j * hx, t - 1j * ht, 1),
             [(alpha, beta), (-cutoff, 0)])
    maximize("bottom_lower",
             lambda x, t: value(x - 1j * hx, t - 1j * ht, -1) - penalty,
             [(alpha, beta), (-cutoff, cutoff)])

    for angular_sign in (-1, 1):
        for wire_sign in (-1, 1):
            maximize(
                f"angular_cutoff_{angular_sign}_{wire_sign}",
                lambda x, s, a=angular_sign, w=wire_sign:
                    value(x + w * 1j * hx * s,
                          a * cutoff - 1j * ht * s, w)
                    - (penalty * s if w < 0 else 0),
                [(alpha, beta), (0, 1)],
            )

    for endpoint in (alpha, beta):
        for wire_sign in (-1, 1):
            maximize(
                f"bottom_endpoint_{endpoint}_{wire_sign}",
                lambda t, v, e=endpoint, w=wire_sign:
                    value(e + w * 1j * hx * v, t - 1j * ht, w)
                    - (penalty * v if w < 0 else 0),
                [(-cutoff, cutoff), (0, 1)],
            )
            for angular_sign in (-1, 1):
                maximize(
                    f"nested_endpoint_{endpoint}_{wire_sign}_{angular_sign}",
                    lambda v, s, e=endpoint, w=wire_sign, a=angular_sign:
                        value(e + w * 1j * hx * v * s,
                              a * cutoff - 1j * ht * s, w)
                        - (penalty * v * s if w < 0 else 0),
                    [(0, 1), (0, 1)],
                )

    g_alpha = (primitive(2 * alpha, 1) - 4 * primitive(alpha, 1)).real
    m_infinity = 4 * 0.91596559417721901505 / PI
    return {
        "degree": degree, "power": power, "alpha": alpha, "beta": beta,
        "cutoff": cutoff, "selected_wire": [xs.real, xs.imag],
        "selected_angle": [ts.real, ts.imag], "selected_rate": selected,
        "wire_tail_gap": selected - (degree - 1) * m_infinity - 2 * g_alpha,
        "surfaces": rows,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--degree", type=int, default=2)
    parser.add_argument("--degrees", type=int, nargs="+")
    parser.add_argument("--powers", type=int, nargs="+", default=[3])
    parser.add_argument("--alpha", type=float, default=1 / 32)
    parser.add_argument("--seed", type=int, default=47)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = {
        "status": "Floating-point exploration only; no certified inequalities.",
        "penalty_rule": "Each individual lower-wire cost p becomes d*p in the scaled phase.",
        "powers": [explore(d, n, args.alpha, args.seed)
                   for d in (args.degrees or [args.degree])
                   for n in args.powers],
    }
    rendered = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered)
        print(f"Saved {args.output}")
    else:
        print(rendered)


if __name__ == "__main__":
    main()
