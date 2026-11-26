#!/usr/bin/env python3
"""Exact boundary checks for the marked degree-two tangle moves.

The geometric proof is in notes/research_marked_degree_two_tangle_moves.md.
All arithmetic here is rational; endpoint permutations are recorded in
addition to, not in place of, the complete affine mapping-class check.
"""

import argparse
import json
from pathlib import Path

import sympy as sp


HALF = sp.Rational(1, 2)
IDENTITY = sp.eye(3)
DECK = sp.diag(-1, -1, 1)
TURN = sp.Matrix([[0, -1, 0], [1, 0, HALF], [0, 0, 1]])
FLIP = sp.Matrix([[1, 0, 0], [0, 1, HALF], [0, 0, 1]])
HALF_TURN = sp.Matrix([[1, 0, HALF], [0, 1, HALF], [0, 0, 1]])
POINTS = [sp.Matrix([x, y, 1])
          for x, y in [(0, 0), (HALF, 0), (HALF, HALF), (0, HALF)]]


def bottom(sign):
    return sp.Matrix([[1, sign, HALF], [0, 1, 0], [0, 0, 1]])


def top(sign):
    return sp.Matrix([[1, sign, 0], [0, 1, 0], [0, 0, 1]])


def same_pillowcase_map(left, right):
    for use_deck in [False, True]:
        candidate = DECK * right if use_deck else right
        difference = left - candidate
        if difference[:2, :2] != sp.zeros(2):
            continue
        if difference[2, :] != sp.zeros(1, 3):
            continue
        translation = [difference[i, 2] for i in range(2)]
        if all(value.is_Integer for value in translation):
            return {
                "deck_involution_on_right": use_deck,
                "integer_translation": [int(value) for value in translation],
            }
    return None


def permutation(matrix):
    answer = []
    for point in POINTS:
        image = matrix * point
        normalized = tuple(image[i] % 1 for i in range(2))
        answer.append(next(j for j, candidate in enumerate(POINTS)
                           if tuple(candidate[:2, 0]) == normalized))
    return answer


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    records = []
    assert same_pillowcase_map(TURN * TURN, HALF_TURN)
    assert not same_pillowcase_map(TURN * TURN, IDENTITY)
    for sign in [1, -1]:
        left = TURN * bottom(sign) * TURN
        right = bottom(-sign) * TURN * bottom(-sign) * FLIP
        witness = same_pillowcase_map(left, right)
        assert witness is not None
        assert permutation(left) == permutation(right)
        missing_flip = bottom(-sign) * TURN * bottom(-sign)
        assert same_pillowcase_map(left, missing_flip) is None
        assert permutation(left) != permutation(missing_flip)
        top_left = TURN * top(sign) * TURN
        top_witness = same_pillowcase_map(top_left, missing_flip)
        assert top_witness is not None
        assert permutation(top_left) == permutation(missing_flip)
        assert same_pillowcase_map(bottom(sign) * bottom(-sign), IDENTITY)
        records.append({
            "sign": sign,
            "bottom_identity_witness": witness,
            "bottom_permutation": permutation(left),
            "wrong_permutation_without_flip": permutation(missing_flip),
            "top_identity_witness": top_witness,
            "top_permutation": permutation(top_left),
        })
    result = {
        "arithmetic": "exact rational affine maps modulo lattice and deck",
        "turn_permutation": permutation(TURN),
        "flip_permutation": permutation(FLIP),
        "physical_half_turn_permutation": permutation(HALF_TURN),
        "half_turn_is_not_identity": True,
        "records": records,
        "passed": True,
    }
    encoded = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
