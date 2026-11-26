#!/usr/bin/env python3
"""Exact scalar audit from typed crossings, coherent carriers and turns.

Standard library only.  The local inputs are the two mixed positive
braidings, their monodromy, and the six physical turn phases.  Signed words
are composed before a carrier is removed.  Typed expression trees are
evaluated from local operations; the global scalar formula is checked
only at the end.

This audit checks the algebra of the scalar reduction.  It does not
rederive the physical turn tensors, prove a knot isotopy, or establish
an asymptotic estimate.  Those statements have separate proofs.

run_scalar_checks() returns a JSON-serializable report and can be called
from another audit without writing files.
"""
from __future__ import annotations

import argparse
from collections import Counter, deque
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
import json
from pathlib import Path


# A monomial is t^a r^b g^c, with t=q^(s^2/2).
# r is transported naturally between A and B; g is the chosen A->B carrier.
@dataclass(frozen=True)
class Monomial:
    t: int = 0
    r: int = 0
    g: int = 0

    def __mul__(self, other: "Monomial") -> "Monomial":
        return Monomial(self.t + other.t, self.r + other.r, self.g + other.g)

    def inverse(self) -> "Monomial":
        return Monomial(-self.t, -self.r, -self.g)


IDENTITY = Monomial()
POSITIVE = {
    "A": Monomial(r=1, g=1),       # R_AB=G r
    "B": Monomial(t=-2, r=1, g=-1),  # R_BA G=t^-2 r
}
OTHER = {"A": "B", "B": "A"}


def physical_generator(start: str, sign: int) -> Monomial:
    if sign == 1:
        return POSITIVE[start]
    if sign == -1:
        # The inverse crossing starting at A is the inverse of R_BA.
        return POSITIVE[OTHER[start]].inverse()
    raise ValueError("a crossing sign must be +1 or -1")


def word_value(start: str, signs: tuple[int, ...]) -> tuple[str, Monomial]:
    current = start
    value = IDENTITY
    for sign in signs:
        value = physical_generator(current, sign) * value
        current = OTHER[current]
    height = {"A": 0, "B": 1}
    carrier = Monomial(g=height[current] - height[start])
    return current, carrier.inverse() * value


# Each type records its actual input and output ordered object.
BOUNDARIES = {
    "PP": ("++", "++"),
    "MM": ("--", "--"),
    "AA": ("A", "A"),
    "BB": ("B", "B"),
    "AB": ("A", "B"),
    "BA": ("B", "A"),
}
TYPE_FROM_BOUNDARIES = {v: k for k, v in BOUNDARIES.items()}

# These integer exponents are copied from the physical six-type theorem,
# not generated from the potential which the audit is about to recover.
TURN = {
    "PP": ("BA", -1),
    "BA": ("MM", +1),
    "MM": ("AB", +1),
    "AB": ("PP", -1),
    "AA": ("BB", 0),
    "BB": ("AA", 0),
}


def derive_turn_potential() -> dict[str, int]:
    potential: dict[str, int] = {}
    for base in ("PP", "AA"):
        potential[base] = 0
        queue = deque([base])
        while queue:
            source = queue.popleft()
            target, exponent = TURN[source]
            candidate = potential[source] + exponent
            if target in potential:
                if potential[target] != candidate:
                    raise AssertionError(("nonzero turn-cycle phase", source, target))
            else:
                potential[target] = candidate
                queue.append(target)
    if set(potential) != set(BOUNDARIES):
        raise AssertionError("turn graph did not cover all six types")
    return potential


def compose_type(left: str, right: str) -> str | None:
    """Type of right after left, when the original maps are composable."""
    source, middle = BOUNDARIES[left]
    required, target = BOUNDARIES[right]
    if middle != required:
        return None
    return TYPE_FROM_BOUNDARIES.get((source, target))


@dataclass(frozen=True)
class State:
    kind: str
    phase: int
    crossing_sum: int


def crossing_block(start: str, n: int) -> State:
    if start in ("++", "--"):
        # The equal-color scalar comes from the separately verified full
        # chirp exponent identity below, not the mixed carrier formula.
        kind = "PP" if start == "++" else "MM"
        return State(kind, -n, n)
    signs = ((1,) * n) if n >= 0 else ((-1,) * (-n))
    finish, value = word_value(start, signs)
    if value.g != 0 or value.r != n:
        raise AssertionError("carrier extraction lost the crossing polynomial")
    return State(TYPE_FROM_BOUNDARIES[(start, finish)], value.t, n)


# Exact multivariate polynomial arithmetic over Q, for exponent checks.
# The variables are N, j, s, w; a key is the corresponding exponent tuple.
ZERO_KEY = (0, 0, 0, 0)


def const(value: int | Fraction) -> dict[tuple[int, ...], Fraction]:
    value = Fraction(value)
    return {} if not value else {ZERO_KEY: value}


def var(index: int) -> dict[tuple[int, ...], Fraction]:
    key = [0] * 4
    key[index] = 1
    return {tuple(key): Fraction(1)}


def add(*polynomials):
    result: dict[tuple[int, ...], Fraction] = {}
    for polynomial in polynomials:
        for key, value in polynomial.items():
            result[key] = result.get(key, Fraction(0)) + value
    return {key: value for key, value in result.items() if value}


def scale(polynomial, factor):
    return {key: value * Fraction(factor) for key, value in polynomial.items()
            if value * Fraction(factor)}


def mul(left, right):
    result: dict[tuple[int, ...], Fraction] = {}
    for ka, va in left.items():
        for kb, vb in right.items():
            key = tuple(a + b for a, b in zip(ka, kb))
            result[key] = result.get(key, Fraction(0)) + va * vb
    return {key: value for key, value in result.items() if value}


def square(polynomial):
    return mul(polynomial, polynomial)


def exponent_checks() -> list[str]:
    N, j, s, w = (var(i) for i in range(4))
    d = add(N, const(-1))
    alpha = add(d, s)
    # (-1)^j=q^(Nj); the chirp is q^((d/2+s-j)^2).
    physical = add(scale(square(alpha), Fraction(1, 2)), mul(N, j),
                   square(j), j, scale(mul(s, j), -2))
    chirp = add(scale(square(d), Fraction(1, 4)),
                scale(square(s), Fraction(-1, 2)),
                square(add(scale(d, Fraction(1, 2)), s, scale(j, -1))))
    if add(physical, scale(chirp, -1), scale(mul(N, j), -2)):
        raise AssertionError("full crossing and chirp exponents disagree")
    # The discrepancy 2Nj has exponential one at the prescribed root.
    twist = scale(add(square(alpha), scale(mul(d, alpha), -2)),
                  Fraction(1, 2))
    if add(twist, scale(square(s), Fraction(-1, 2)),
           scale(square(d), Fraction(1, 2))):
        raise AssertionError("ribbon twist did not complete its square")
    stripped = add(mul(w, add(mul(d, s),
                             scale(square(s), Fraction(1, 2)))),
                   scale(mul(w, square(s)), Fraction(-1, 2)))
    if add(stripped, scale(mul(mul(w, d), s), -1)):
        raise AssertionError("stripped-Cartan convention mismatch")
    return ["physical_chirp_mod_2Nj", "ribbon_twist_square",
            "stripped_Cartan_linear_gauge"]


def run_scalar_checks(max_word_length: int = 8, max_tree_size: int = 7) -> dict:
    if max_word_length < 1 or max_tree_size < 2:
        raise ValueError("use word length >=1 and tree size >=2")
    counts = Counter()
    potential = derive_turn_potential()
    polynomial_checks = exponent_checks()
    counts["exact_polynomial_exponent_identities"] = len(polynomial_checks)

    # The monodromy follows from the two positive morphisms before
    # extracting a carrier.  Both starting orders are checked.
    for start in ("A", "B"):
        monodromy = POSITIVE[OTHER[start]] * POSITIVE[start]
        if monodromy != Monomial(t=-2, r=2):
            raise AssertionError(("monodromy", start, monodromy))
        for sign in (-1, 1):
            if physical_generator(OTHER[start], -sign) * physical_generator(start, sign) != IDENTITY:
                raise AssertionError(("inverse crossing", start, sign))
            counts["generator_inverse_identities"] += 1
        counts["monodromy_identities"] += 1

    # Compose every signed word first, with its actual order changes.
    negative_examples = []
    for length in range(max_word_length + 1):
        for signs in product((-1, 1), repeat=length):
            n = sum(signs)
            for start in ("A", "B"):
                finish, value = word_value(start, signs)
                expected = -2 * (n // 2 if start == "A" else -((-n) // 2))
                if (value.t, value.r, value.g) != (expected, n, 0):
                    raise AssertionError(("signed word", start, signs, value))
                counts["signed_words"] += 1
                if n < 0:
                    counts["negative_net_words"] += 1
                if n < 0 and n % 2:
                    counts["negative_odd_net_words"] += 1
                if length > 1 and len(set(signs)) == 2:
                    counts["mixed_sign_words"] += 1
                if length <= 3 and n < 0 and n % 2:
                    negative_examples.append({"start": start, "signs": list(signs),
                                              "finish": finish, "t_exponent": value.t,
                                              "r_exponent": value.r})

    # Recover the potential from the actual turn graph, then check every
    # compatible product independently from its source/target objects.
    for source, (target, exponent) in TURN.items():
        if exponent != potential[target] - potential[source]:
            raise AssertionError(("turn potential", source))
        counts["turn_types"] += 1
    for left, right in product(BOUNDARIES, repeat=2):
        target = compose_type(left, right)
        if target is not None:
            if potential[target] != potential[left] + potential[right]:
                raise AssertionError(("product potential", left, right))
            counts["compatible_type_products"] += 1

    # Exhaustively build reachable scalar/type states of finite expression
    # trees. Unary turns and binary compatible products have cost one.
    # States with identical scalar data are merged; operation checks are
    # still performed on each generated transition.
    states: dict[int, dict[State, str]] = {1: {}}
    for start, n in product(("++", "--", "A", "B"), range(-3, 4)):
        state = crossing_block(start, n)
        states[1].setdefault(state, f"R[{start},{n}]")
    closed_examples = []
    for size in range(1, max_tree_size + 1):
        if size > 1:
            current: dict[State, str] = {}
            for state, expression in states[size - 1].items():
                target, exponent = TURN[state.kind]
                result = State(target, state.phase + exponent, state.crossing_sum)
                current.setdefault(result, f"T({expression})")
                counts["typed_turn_transitions"] += 1
            for left_size in range(1, size - 1):
                right_size = size - left_size - 1
                for left, lexpr in states[left_size].items():
                    for right, rexpr in states[right_size].items():
                        target = compose_type(left.kind, right.kind)
                        if target is None:
                            continue
                        result = State(target, left.phase + right.phase,
                                       left.crossing_sum + right.crossing_sum)
                        current.setdefault(result, f"({lexpr};{rexpr})")
                        counts["typed_product_transitions"] += 1
            states[size] = current
        for state, expression in states[size].items():
            if state.phase - potential[state.kind] != -state.crossing_sum:
                raise AssertionError(("open typed expression", expression, state))
            counts["reachable_typed_states"] += 1
            source, target = BOUNDARIES[state.kind]
            if source == target:
                if state.phase != -state.crossing_sum:
                    raise AssertionError(("End closing", expression, state))
                counts["closed_End_states"] += 1
                # Independently attach any integer zero-framing correction.
                for writhe in range(-3, 4):
                    phase = state.phase - writhe
                    if phase != -writhe - state.crossing_sum:
                        raise AssertionError("closing framing phase")
                    counts["framed_End_states"] += 1
                if size == max_tree_size and len(closed_examples) < 8:
                    closed_examples.append({"expression": expression,
                                            "phase": state.phase,
                                            "crossing_sum": state.crossing_sum})

    return {
        "method": "exact integer Laurent exponents and rational polynomial coefficients",
        "parameters": {"max_word_length": max_word_length,
                       "max_expression_tree_size": max_tree_size,
                       "primitive_block_exponents": [-3, -2, -1, 0, 1, 2, 3]},
        "local_inputs": {
            "positive_AB": "G r",
            "positive_BA": "t^-2 r G^-1",
            "t": "q^(s^2/2)",
            "six_turn_table": {key: [target, exponent]
                               for key, (target, exponent) in TURN.items()},
        },
        "derived_turn_potential": potential,
        "counts": dict(sorted(counts.items())),
        "polynomial_checks": polynomial_checks,
        "negative_odd_examples": negative_examples,
        "closed_expression_examples": closed_examples,
        "scope": (
            "Finite exact scalar algebra. The local physical tensors, topology, "
            "uniform asymptotics and cusp interpretation are separate inputs; "
            "expression states are compatible algebraic morphisms, not a knot census."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-word-length", type=int, default=8)
    parser.add_argument("--max-tree-size", type=int, default=7)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run_scalar_checks(args.max_word_length, args.max_tree_size)
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
        print(json.dumps({"output": str(args.output), "counts": result["counts"]},
                         sort_keys=True))
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
