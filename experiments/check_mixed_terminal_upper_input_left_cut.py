#!/usr/bin/env python3
"""One prescribed 128-check upper-input left-cut comparison.

Original regular-strip primitives only, no root or optimizer and no
adaptive parameter subdivision. Nonpositive lower bounds are retained.
"""
import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

import flint
from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = "notes/research_mixed_terminal_upper_input_left_cut_protocol.md"
PINNED = {
    PROOF: "1f2fd095cfcf9a0a3a847d6db9d811f6236bb5f6cec940206b20420dbe445fc8",
    "notes/research_mixed_terminal_ordinary_label_height_extension.md":
        "1b3b37f6166aed8b5b4e21170d2e6ad9056a73235ce63005c4ba021da341ab7d",
    "notes/research_mixed_terminal_full_input_index_barrier.md":
        "45ae03bf28a78df930fc8e7c97054ca40689630423a4d36c0009b6b0bb900ee2",
    "notes/research_mixed_second_selected_plateau_reduction.md":
        "015c85c322ff3563ec6752b5c499080c3e906360920aaeed2063508ef2db868f",
    "notes/research_mixed_second_selected_left_cut_domination.md":
        "d7a9236af4a5aac3f4acbd2de38354746693f0902eed5d537040d9ad1e82cac5",
    "notes/research_mixed_typed_last_row_envelopes.md":
        "5732f40ffc086acddb21632a5d6af3e4905ebad38f97e62e89953802b1bdd10d",
}
PARTS = 32
PRECISION = 160
HEIGHTS = (F(-51, 500), F(-1, 1000))
INCOMING_HEIGHT = F(17, 250)
SELECTED_HEIGHT = F(1, 100)
TRIAL = F(1, 4)
LEFT_CUT = F(1, 8)
TARGET_CORNERS = tuple(itertools.product((F(11, 50), F(9, 20)), repeat=2))


def sha(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1048576), b""):
            digest.update(chunk)
    return digest.hexdigest()


def endpoint(value, side):
    assert value.is_finite()
    return F(str(getattr(value, side)().fmpq()))


def record(value):
    return {"finite": bool(value.is_finite()),
            "lower_rational": str(endpoint(value, "lower")),
            "upper_rational": str(endpoint(value, "upper"))}


def rat(value):
    value = F(value)
    result = arb(value.numerator)/value.denominator
    if not (endpoint(result, "lower") <= value <= endpoint(result, "upper")):
        raise ArithmeticError("Rational input was not contained outward.")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise SystemExit("Refusing to overwrite a result.")
    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    bindings = dict(PINNED)
    bindings[own] = sha(ROOT/own)
    for path, digest in bindings.items():
        if sha(ROOT/path) != digest:
            raise SystemExit("Input binding failed before evaluation: "+path)

    ctx.prec = PRECISION
    pi, ii = arb.pi(), acb(0, 1)
    calls, rows, error = 0, [], None
    step = (HEIGHTS[1]-HEIGHTS[0])/PARTS
    planned = [{"index": j, "height_interval": [
                    str(HEIGHTS[0]+j*step), str(HEIGHTS[0]+(j+1)*step)],
                "real_targets": list(map(str, corner))}
               for j in range(PARTS) for corner in TARGET_CORNERS]

    def primitive(w):
        nonlocal calls
        if not (w.is_finite() and w.real > 0 and w.real < 1):
            raise ArithmeticError("Primitive argument left its original strip.")
        z = (-2*pi*ii*w).exp()
        if not (z.imag > 0 or z.imag < 0 or z.real < 1):
            raise ArithmeticError("Dilogarithm cut not separated.")
        calls += 1
        value = (z.polylog(2)-pi*pi/6)/(2*pi*ii)
        if not value.is_finite():
            raise ArithmeticError("Nonfinite original primitive enclosure.")
        return value

    try:
        left = acb(rat(LEFT_CUT))
        for spec in planned:
            lo, hi = map(F, spec["height_interval"])
            mid = (lo+hi)/2
            x, y = map(F, spec["real_targets"])
            s = acb(rat(TRIAL), rat(mid))
            b = acb(rat(x), rat(INCOMING_HEIGHT))
            a = acb(rat(y), rat(SELECTED_HEIGHT))
            difference = (
                primitive(s+b)-primitive(left+b)
                +primitive(s+a)-primitive(left+a)
                -3*primitive(s)+3*primitive(left)
                +2*pi*ii*b*(s-left))
            midpoint = record(difference.real)
            loss = record(rat(F(3, 4))*pi*rat((hi-lo)/2))
            # Exact recombination of outward endpoints; no second Arb round-trip.
            loss_hi = F(loss["upper_rational"])
            lower = F(midpoint["lower_rational"])-loss_hi
            upper = F(midpoint["upper_rational"])+loss_hi
            rows.append({
                **spec, "height_midpoint": str(mid),
                "midpoint_difference": midpoint, "height_loss": loss,
                "whole_interval_lower_rational": str(lower),
                "whole_interval_upper_rational": str(upper),
                "strictly_positive": lower > 0,
            })
    except Exception as exc:
        error = {"type": type(exc).__name__, "message": str(exc),
                 "completed_checks": len(rows), "primitive_calls": calls}

    changed = [path for path, digest in bindings.items()
               if sha(ROOT/path) != digest]
    arithmetic_complete = error is None and len(rows) == 128 and calls == 768
    passed = arithmetic_complete and not changed and all(r["strictly_positive"] for r in rows)
    worst = min((F(r["whole_interval_lower_rational"]) for r in rows), default=None)
    status = ("passed" if passed else "input failure" if changed else
              "arithmetic error" if error is not None else "inconclusive signs")
    result = {
        "status": status, "precision_bits": PRECISION,
        "python_flint": flint.__version__, "proof_path": PROOF,
        "proof_sha256": PINNED[PROOF], "checker_sha256": bindings[own],
        "input_sha256": bindings, "changed_inputs": changed,
        "height_interval": list(map(str, HEIGHTS)), "partition_count": PARTS,
        "incoming_height": str(INCOMING_HEIGHT),
        "selected_height": str(SELECTED_HEIGHT),
        "trial_real_part": str(TRIAL), "left_cut": str(LEFT_CUT),
        "incoming_strip_covered_if_passed": ["3/100", "17/250"],
        "target_real_interval": ["11/50", "9/20"],
        "lipschitz_coefficient_times_pi": "3/4",
        "planned_checks": 128, "completed_checks": len(rows),
        "arithmetic_complete": arithmetic_complete, "checks": rows,
        "pending_planned_checks": planned[len(rows):], "error": error,
        "strictly_positive_checks": sum(r["strictly_positive"] for r in rows),
        "minimum_whole_interval_lower_rational": None if worst is None else str(worst),
        "uniform_left_cut_comparison_proved": passed,
        "primitive_evaluations": calls, "root_evaluations": 0,
        "finite_source_evaluations": 0, "adaptive_subdivisions": 0,
        "target_optimizations": 0, "automatic_retries": 0,
        "new_terminal_profile_sign_claimed": False,
        "whole_word_or_global_knot_theorem_claimed": False,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps({"status": status, "checks": len(rows),
                      "positive": result["strictly_positive_checks"],
                      "worst_lower": None if worst is None else float(worst),
                      "output_sha256": sha(args.output)}))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
