#!/usr/bin/env python3
"""Exact affine checks for the marked rational-corridor normal form."""

from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
from itertools import product
import json
from pathlib import Path


IDENTITY = ((1, 0), (0, 1))


def multiply(a, b):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


def compose(left, right):
    a, v = left
    b, w = right
    return multiply(a, b), tuple(
        v[i] + sum(a[i][k] * w[k] for k in range(2)) for i in range(2)
    )


def inverse(affine):
    matrix, translation = affine
    (a, b), (c, d) = matrix
    assert a * d - b * c == 1
    inv = ((d, -b), (-c, a))
    return inv, tuple(
        -sum(inv[i][k] * translation[k] for k in range(2))
        for i in range(2)
    )


def crossing(power):
    return ((1, power), (0, 1)), (Q(power, 2), Q(0))


TURN = (((0, -1), (1, 0)), (Q(0), Q(1, 2)))
AFFINE_IDENTITY = (IDENTITY, (Q(0), Q(0)))
ROTATIONS = {
    (Q(0), Q(0)): "identity",
    (Q(1, 2), Q(0)): "rho",
    (Q(0), Q(1, 2)): "K",
    (Q(1, 2), Q(1, 2)): "tau",
}


def word(powers, internal):
    """Powers are read from the innermost box toward the outside."""
    affine = AFFINE_IDENTITY
    for n in powers:
        affine = compose(TURN, compose(crossing(n), affine))
    return compose(affine, TURN) if internal else affine


def normal_form(r, m, s):
    return compose(
        crossing(r),
        compose(TURN, compose(crossing(m), compose(TURN, crossing(s)))),
    )


def relative_rotation(target, original):
    matrix, shift = compose(inverse(target), original)
    lam = matrix[0][0]
    assert lam in (-1, 1) and matrix == ((lam, 0), (0, lam))
    delta = tuple((lam * entry) % 1 for entry in shift)
    assert delta in ROTATIONS
    reconstructed = compose(target, (IDENTITY, delta))
    a, v = reconstructed
    b, w = original
    assert a == tuple(tuple(lam * x for x in row) for row in b)
    assert all((v[i] - lam * w[i]).denominator == 1 for i in range(2))
    return ROTATIONS[delta]


def internal_forms(affine):
    (a, b), (c, d) = affine[0]
    if c == 0:
        assert a == d and a in (-1, 1)
        k = a * b
        return [{
            "kind": "no intervening turn",
            "end_power": k,
            "rotation": relative_rotation(crossing(k), affine),
            "fiber_warning": "Two free neighboring powers may merge.",
        }]
    forms = []
    for eps in (-1, 1):
        if (a - eps) % abs(c) or (d - eps) % abs(c):
            continue
        cp = eps * c
        r = (eps * a - 1) // cp
        s = (eps * d - 1) // cp
        m = -cp
        forms.append({
            "kind": "one internal vertex",
            "r": r, "m": m, "s": s,
            "rotation": relative_rotation(normal_form(r, m, s), affine),
        })
    return forms


def pendant_forms(affine):
    (a, b), (c, d) = affine[0]
    if d == 0:
        assert abs(b) == 1
        return {"slope": "infinity", "kind": "cap"}
    slope = Q(b, d)
    p, q = slope.numerator, slope.denominator
    if q == 1:
        return {"slope": str(slope), "kind": "integral", "power": p}
    choices = []
    for m in (-q, q):
        numerator = p * m + q
        if numerator % (q * m):
            continue
        r = numerator // (q * m)
        target = compose(crossing(r), compose(TURN, crossing(m)))
        relative, shift = compose(inverse(target), affine)
        (aa, bb), (cc, dd) = relative
        assert bb == 0 and aa == dd and aa in (-1, 1)
        assert all((2 * value).denominator == 1 for value in shift)
        assert Q(r * m - 1, m) == slope
        choices.append({"r": r, "m": m})
    return {"slope": str(slope), "kind": "terminal compression", "forms": choices}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-length", type=int, default=4)
    parser.add_argument("--max-power", type=int, default=3)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    assert args.max_length >= 1 and args.max_power >= 2
    words = signs = zero_forms = pendant_choices = 0
    for length in range(1, args.max_length + 1):
        for powers in product(range(-args.max_power, args.max_power + 1), repeat=length):
            forms = internal_forms(word(powers, True))
            words += 1
            signs += sum(f["kind"] == "one internal vertex" for f in forms)
            zero_forms += sum(f["kind"] == "no intervening turn" for f in forms)
            pendant = pendant_forms(word(powers, False))
            pendant_choices += len(pendant.get("forms", []))
    examples = []
    for powers in ([2, 2], [-2, -2], [2, -2], [3, 2], [2] * 5):
        affine = word(powers, True)
        examples.append({
            "powers_from_inside": powers,
            "internal_matrix": affine[0],
            "internal_forms": internal_forms(affine),
            "pendant": pendant_forms(word(powers, False)),
        })
    result = {
        "description": "Exact rational affine checks; no asymptotic or hyperbolicity test.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "max_length": args.max_length,
        "max_absolute_power": args.max_power,
        "words_checked": words,
        "one_vertex_sign_choices_checked": signs,
        "zero_lower_left_forms_checked": zero_forms,
        "pendant_compressions_checked": pendant_choices,
        "examples": examples,
        "status": "all asserted affine identities verified",
    }
    encoded = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    print(encoded)


if __name__ == "__main__":
    main()
