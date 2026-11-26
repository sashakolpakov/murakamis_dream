#!/usr/bin/env python3
"""Certify a positive regular edge with an indefinite horizontal wire Hessian.

The endpoint angles below are exact rational complex numbers. This is
an obstruction to inferring fixed-horizontal concavity from positive
edge geometry alone, not a counterexample to a volume conjecture or
to a unit-charge filling theorem.
"""

import argparse
import hashlib
import json
from pathlib import Path

import flint
from flint import acb, arb, ctx


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=192)
    parser.add_argument("--output", type=Path, default=Path(
        "repro/results/research-positive-edge-horizontal-hessian-obstruction.json"))
    args = parser.parse_args()
    if args.precision < 128:
        parser.error("Use at least 128 bits.")
    ctx.prec = args.precision
    pi, imaginary = arb.pi(), acb(0, 1)
    t = arb(21)/10-imaginary*arb(3)/4
    r = arb(3)/4-imaginary*arb(3)/20
    a, b = (t/2).tan(), (r/2).tan()
    q = (1+a*a+b*b).sqrt()
    x = (1/q).atan()/pi
    assert q.real > 0 and x.real > 0 and x.imag > 0
    positive_margin = q.real-(a.real*a.real+b.real*b.real).sqrt()
    assert positive_margin > arb(23)/100
    shapes = [(q+a)/(b-imaginary), (q-a)/(b-imaginary),
              -(q-b)/(a+imaginary), -(q+b)/(a+imaginary)]
    assert all(z.imag > arb(3)/10 for z in shapes)
    incidence = []
    gradient = acb(0)
    for endpoint in (t, r):
        s = arb(1)/2-endpoint/(2*pi)
        for argument in (x, s-x, 1-s-x):
            assert argument.real > 0 and argument.real < 1
        u = 1/(pi*(s+x)).tan()
        v = 1/(pi*(s-x)).tan()
        w = 1/(pi*x).tan()
        incidence.append((s, u, v, w))
        gradient += ((2*(pi*(s+x)).sin()).log()
                     +(2*(pi*(s-x)).sin()).log()
                     -2*(2*(pi*x).sin()).log())
    # The exact cotangent relation makes the exponentiated gradient one.
    # This enclosure selects the zero logarithmic lift.
    assert abs(gradient) < arb(1)/100
    s, u, v, w = incidence[0]
    margin = (s-x).real
    negative_diagonal = (pi*(v-u)).real
    assert margin > arb(9)/10000
    assert negative_diagonal < -arb(59)/100

    # The reduced original edge phase still has positive real Hessian.
    reduced = [(1+a*a)/(2*pi*q), -a*b/(2*pi*q),
               (1+b*b)/(2*pi*q)]
    reduced_determinant = reduced[0].real*reduced[2].real-reduced[1].real**2
    assert reduced[0].real > 0 and reduced_determinant > 0

    script = Path(__file__).resolve()
    record = {
        "status": "certified",
        "scope": ("Positive original edge, stationary wire in the regular "
                  "factorial chart; the fixed-horizontal mixed Hessian "
                  "has a negative diagonal. No filling equation is asserted."),
        "precision_bits": ctx.prec,
        "python_flint_version": flint.__version__,
        "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
        "exact_t": "21/10 - (3/4)i",
        "exact_r": "3/4 - (3/20)i",
        "q": str(q), "wire": str(x),
        "positive_edge_margin": str(positive_margin),
        "four_original_shapes": [str(z) for z in shapes],
        "stationary_wire_log_lift": str(gradient),
        "smallest_regular_factorial_margin": str(margin),
        "negative_real_hessian_s_t_diagonal": str(negative_diagonal),
        "negative_diagonal_upper_bound": "-59/100",
        "reduced_real_hessian_entries": [str(z.real) for z in reduced],
        "reduced_real_hessian_determinant": str(reduced_determinant),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2)+"\n")
    print("Certified: positive regular edge; horizontal diagonal < -59/100.")
    print(args.output)


if __name__ == "__main__":
    main()
