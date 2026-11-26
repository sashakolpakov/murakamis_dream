#!/usr/bin/env python3
"""Two next-four cap-left/main scalar bounds on one prescribed box.

Reuses the frozen own-four reference and centered primitive only. There is
one new scalar call, no old inspection, root solve, source sum, subdivision,
alternate box, continuation, or automatic retry.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time

from flint import acb, ctx


REPO = Path(__file__).resolve().parents[1]
HELPER = "experiments/diagnose_mixed_four_four_half_row_budget.py"
PREVIOUS = "repro/results/research-mixed-next-four-adaptive-budget-attempt02.json"
ADDRESS = "001111101111010111"
BOX = tuple(map(F, ("115337/512000", "57677/256000", "8919/256000", "279/8000")))
H = F(1, 100)
GAP = F(1, 2000)
KEYS = ("factorial", "forced")
PINNED = {
    HELPER: "cc1d86c233ef74f343796b6ad64967ca8a86c8dd315546b1de7c440cd9f9f82f",
    PREVIOUS: "6e3520360bf93d779c359f39f33e479cf422ef2fa7eadbfe23ce0b5383af7d27",
    "notes/research_mixed_selected_four_four_left_main_majorant.md": "fffa8b11516d5ca95364e7c8823dd9323e8b09ca259bc7caaa93a8371f1006ed",
    "notes/research_mixed_selected_four_four_left_main_diagnostic.md": "8eeaad4fd2eb1f152899fd503a7c8be14b40b2375d89fbbf0dcdf4ec2690355b",
    "notes/research_mixed_selected_four_four_half_row_evaluation.md": "cb9dc4c264df6ad0fa7b590e4430ccaa21109dc697072d458d63eeebe0b242dc",
    "notes/research_mixed_centered_primitive_enclosure.md": "ce2bebcca5ff53ca466948517f4324123b09bb7c92c6736409ff47ece9aac956",
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inspect(box, primitive, helper):
    """Enclose precisely Eq(21) of the next-four left-main majorant."""
    frozen = helper.frozen
    details = {}
    try:
        state, reason, ref = helper.reference_four(box, primitive)
        if state != "retained":
            return state, reason, details
        auxiliary, shapes, coordinates = ref
        details["auxiliary"] = frozen.complex_record(auxiliary)
        details["reference_shapes"] = {
            name: frozen.complex_record(w) for name, w in shapes.items()}
        details["reference_coordinates_after_necessary_intersection"] = {
            name: frozen.complex_record(w) for name, w in coordinates.items()}
        pi, ii = primitive.pi, primitive.ii
        e, z, s = (coordinates[name] for name in ("e", "z", "s"))
        Z, S, B = (shapes[name] for name in ("z", "s", "b"))
        zH = acb(z.real, primitive.height)
        lam = (2*pi*primitive.height).exp()/abs(Z)
        if not lam.is_finite() or not lam > 0:
            raise frozen.Inconclusive("nonfinite or nonpositive radial multiplier")
        ell = lam.log()
        d_raw = ell-primitive.log_abs(1-lam*S*Z)+primitive.log_abs(1-S*Z)
        if not d_raw.is_finite() or frozen.upper(d_raw) < 0:
            raise frozen.Inconclusive("proved nonnegative d not enclosed")
        d = frozen.interval(max(F(0), frozen.lower(d_raw)), frozen.upper(d_raw))

        # At fixed actual h_s, the two pair terms reserve 39*pi/80,
        # and the additional own-four -g(s) reserves pi*a_star.
        a_star = (ii*(1+S)/(1-S)).real
        if not a_star.is_finite():
            raise frozen.Inconclusive("nonfinite actual index cotangent")
        a_lower = max(F(2, 5), frozen.lower(a_star))
        pi_lower = frozen.lower(pi)
        mu_s_lower = pi_lower*(F(39, 80)+a_lower)
        index_length = frozen.upper(s.real)-F(11, 50)
        if index_length < 0 or mu_s_lower <= 0:
            raise frozen.Inconclusive("invalid negative index displacement interval")
        d_upper = frozen.upper(d)
        index_displacement = min(index_length, d_upper/mu_s_lower)
        index_gain = (d_upper*index_displacement
                      -mu_s_lower*index_displacement*index_displacement/2)

        # Original Eq(21): the outgoing halfweight and extra -g(s)
        # cancel at unchanged reference coordinates, but their marginal
        # and curvature have already entered the proved upper bound.
        actual_action = primitive.endpoint_action(e, auxiliary)
        cap_increment = (primitive.psi(primitive.cut, zH, primitive.cut_action)
                         -primitive.psi(e, z, actual_action)).real
        gz, gzH = primitive.g(z), primitive.g(zH)
        ordinary_primitive_increment = (
            primitive.g(s+zH)-primitive.g(s+z)-gzH+gz).real
        delta_z = acb(0, primitive.height-z.imag)
        chirp_increment = (2*pi*ii*s*delta_z).real
        ordinary_increment = ordinary_primitive_increment+chirp_increment
        trial_common = cap_increment+ordinary_increment+gz.real
        if not trial_common.is_finite():
            raise frozen.Inconclusive("nonfinite common trial action")
        p_real = (primitive.log_abs(1-S*B)
                  -frozen.rat("3/2")*primitive.log_abs(1-B))

        details.update({
            "reference_private_action": frozen.complex_record(actual_action),
            "fixed_cut_private_action": frozen.complex_record(primitive.cut_action),
            "fixed_cut_private_root": frozen.complex_record(primitive.cut_u),
            "cap_increment": frozen.real_record(cap_increment),
            "ordinary_primitive_increment": frozen.real_record(ordinary_primitive_increment),
            "chirp_increment": frozen.real_record(chirp_increment),
            "ordinary_increment": frozen.real_record(ordinary_increment),
            "g_reference_incoming": frozen.complex_record(gz),
            "g_selected_incoming": frozen.complex_record(gzH),
            "trial_common": frozen.real_record(trial_common),
            "radial_multiplier": frozen.real_record(lam),
            "ell": frozen.real_record(ell),
            "d_unclipped": frozen.real_record(d_raw),
            "d_nonnegative": frozen.real_record(d),
            "index_cotangent": frozen.real_record(a_star),
            "index_cotangent_lower_rational": str(a_lower),
            "pi_lower_rational": str(pi_lower),
            "index_curvature_lower_rational": str(mu_s_lower),
            "negative_index_length_upper_rational": str(index_length),
            "negative_index_displacement_rational": str(index_displacement),
            "index_gain_rational": str(index_gain),
            "outgoing_p_real": frozen.real_record(p_real),
            "outgoing_marginal": "p=g'(s+b)-3*g'(b)/2",
            "outgoing_gradient_exact": "0",
            "outgoing_gain_exact": "0",
        })
        E0 = (-2*pi*ii*primitive.cut).exp()
        majorants = {}
        for nu, label in ((1, "factorial"), (0, "forced")):
            beta = (primitive.log_abs(1-lam*E0*Z)
                    +primitive.log_abs(1-lam*S*Z)
                    -primitive.log_abs(S)
                    -(2+nu)*primitive.log_abs(1-lam*Z))
            mu_z_lower = F(23+18*nu, 120)*pi_lower
            incoming_gain = frozen.quadratic_gain(
                beta, z.real, ".22", ".45", mu_z_lower)
            fourier = -nu*gzH.real-2*nu*pi*primitive.height
            trial = trial_common+fourier
            total = trial+frozen.rat(index_gain)+frozen.rat(incoming_gain)
            if not total.is_finite():
                raise frozen.Inconclusive("nonfinite "+label+" majorant")
            majorants[label] = {
                "nu": nu,
                "trial_action": frozen.real_record(trial),
                "fourier_adjustment": frozen.real_record(fourier),
                "incoming_gradient": frozen.real_record(beta),
                "incoming_curvature_lower_rational": str(mu_z_lower),
                "incoming_gain_rational": str(incoming_gain),
                "index_gain_rational": str(index_gain),
                "value": frozen.real_record(total),
                "strictly_below_zero": frozen.upper(total) < 0,
                "strictly_below_candidate_gap": frozen.upper(total) < -GAP,
            }
        details["majorants"] = majorants
        if all(majorants[key]["strictly_below_candidate_gap"] for key in KEYS):
            return "accepted", "two strict tests on this single box", details
        return "inconclusive", "two majorants not certified on this box", details
    except frozen.Inconclusive as error:
        return "inconclusive", str(error), details


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    for name, expected in PINNED.items():
        if digest(REPO/name) != expected:
            raise ValueError("pinned input hash mismatch: "+name)
    previous = json.loads((REPO/PREVIOUS).read_text())
    if previous["status"] != "proved" or previous["unresolved"]:
        raise ValueError("prescribed central record is not complete")
    bindings = dict(PINNED)

    def merge_binding(name, expected):
        path = Path(name)
        relative = str((path if path.is_absolute() else REPO/path).relative_to(REPO))
        if relative in bindings and bindings[relative] != expected:
            raise ValueError("conflicting inherited binding: "+relative)
        bindings[relative] = expected

    for name, expected in previous["input_sha256"].items():
        merge_binding(name, expected)
    for name, expected in bindings.items():
        if digest(REPO/name) != expected:
            raise ValueError("inherited dependency mismatch: "+name)

    import diagnose_mixed_four_four_half_row_budget as helper
    if Path(helper.__file__).resolve() != REPO/HELPER:
        raise ValueError("unexpected helper module path")
    if helper.H != H or helper.ADDRESS != ADDRESS or helper.BOX != BOX:
        raise ValueError("helper height or prescribed box mismatch")
    for name, expected in helper.PINNED.items():
        merge_binding(name, expected)
    bindings[str(Path(__file__).resolve().relative_to(REPO))] = digest(Path(__file__))
    for name, expected in bindings.items():
        if digest(REPO/name) != expected:
            raise ValueError("frozen dependency mismatch: "+name)

    # Only saved metadata and exact rational splits select the one box.
    accepted = [leaf for leaf in previous["leaves"] if leaf["status"] == "accepted"]
    depth = max(len(leaf["address"]) for leaf in accepted)
    chosen = min((leaf for leaf in accepted if len(leaf["address"]) == depth),
                 key=lambda leaf: leaf["address"])
    if chosen["address"] != ADDRESS or depth != 18:
        raise ValueError("deterministic inherited leaf differs from specification")
    box = helper.BASE.ROOT
    if list(map(str, box)) != previous["initial_auxiliary_rectangle"]:
        raise ValueError("original auxiliary root rectangle mismatch")
    for split_depth, branch in enumerate(ADDRESS):
        box = helper.BASE.split(box, split_depth)[int(branch)]
    if box != BOX:
        raise ValueError("exact inherited box reconstruction failed")

    def forbidden(*args, **kwargs):
        raise RuntimeError("all previous scalar inspect routines are forbidden")

    helper.inspect = helper.frozen.inspect = helper.maps_four.inspect = forbidden
    helper.BASE.inspect = forbidden
    ctx.prec = 160
    started = time.monotonic()
    result = inspect(box, helper.CenteredPrimitives(), helper)
    for name, expected in bindings.items():
        if digest(REPO/name) != expected:
            raise RuntimeError("input changed during diagnostic: "+name)
    record = {
        "status": "diagnostic complete",
        "scope": "Two next-four cap-left/main scalar bounds on one inherited box only",
        "actual_word_realization_claimed": False,
        "precision_bits": 160, "height": str(H), "candidate_gap": str(GAP),
        "tested_address": ADDRESS, "tested_box": list(map(str, box)),
        "inherited_leaf": chosen,
        "selection": "lexicographically first accepted leaf of maximum accepted depth",
        "formula": "next-four left-main Eq(21), exact halfweight cancellation at trial",
        "primitive": "frozen helper CenteredPrimitives; unchanged reference_four",
        "index_curvature": "pi*(39/80+Re cot(pi*s*)) with exact lower bound",
        "incoming_curvature": "(23+18*nu)*pi/120 with exact lower bound",
        "result": {"status": result[0], "reason": result[1], "details": result[2]},
        "inspect_calls": 1, "old_scalar_inspect_calls": 0,
        "tested_boxes": 1, "subdivisions": 0, "automatic_retries": 0,
        "root_proposals": 0, "finite_source_evaluations": 0,
        "elapsed_seconds": time.monotonic()-started,
        "input_sha256": bindings,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as output:
        output.write(json.dumps(record, indent=2)+"\n")
    print(json.dumps({
        "status": record["status"], "tested_address": ADDRESS,
        "result_status": result[0], "reason": result[1],
        "elapsed_seconds": record["elapsed_seconds"],
        "upper_bounds": {key: value["value"]["upper_rational"]
                         for key, value in result[2].get("majorants", {}).items()},
    }), flush=True)


if __name__ == "__main__":
    main()
