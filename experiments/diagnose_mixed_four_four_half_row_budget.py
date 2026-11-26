#!/usr/bin/env python3
"""Four next-four half-row scalar bounds on one prescribed reference box.

The own-four reference and centered primitive are reusable pure helpers.
The main program evaluates exactly one inherited box at 160 bits: no cover,
root solve, finite quantum sum, old scalar inspection, or automatic retry.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time

from flint import acb, arb, ctx

import certify_mixed_selected_half_row_budget as frozen
import certify_mixed_next_four_endpoint_budget as maps_four


REPO = Path(__file__).resolve().parents[1]
BASE = frozen.base
H = F(1, 100)
GAP = F(1, 2000)
KEYS = ("main_factorial", "main_forced", "left_factorial", "left_forced")
PREVIOUS = "repro/results/research-mixed-next-four-adaptive-budget-attempt02.json"
ADDRESS = "001111101111010111"
BOX = tuple(map(F, ("115337/512000", "57677/256000", "8919/256000", "279/8000")))
PINNED = {
    "notes/research_mixed_selected_four_four_half_row_evaluation.md": "cb9dc4c264df6ad0fa7b590e4430ccaa21109dc697072d458d63eeebe0b242dc",
    "notes/research_mixed_selected_four_four_half_row_majorant.md": "06d69406acf6e6666038e52ac5af3383d848b80c3802b621ca57dc0314e84680",
    "notes/research_mixed_centered_primitive_enclosure.md": "ce2bebcca5ff53ca466948517f4324123b09bb7c92c6736409ff47ece9aac956",
    "notes/research_mixed_first_four_next_four_central_gap.md": "0acb83fa492a0ce6b2c10f1ddeb21480d2c94dfeb10055e925e51f5ae34d4c99",
    "notes/research_mixed_private_cap_curvature_bound.md": "a689a6ba154ed596beead75d88aa12c797ebfae4dc4b47072b9884f62d184c98",
    "notes/research_mixed_rational_critical_transport.md": "0cba78ed20d7e98d65414b61a96412a8ee6f3e43b766d7d10f9900ea36a96635",
    "notes/research_mixed_open_word_endpoint_rectangles.md": "ac5603badc00d42e98d17a1c5948cae011a6abd991d5249fa61d4224a829ad07",
    "notes/research_mixed_first_four_attached_height_bound.md": "42329b71c8af492823bb5fd5a74b2a472eab8b4f0ecdf2b25cb83ae7f09d7bfe",
    "notes/research_mixed_reduced_disk_pair_sums.md": "6c93f96db406e73aca137c5e492d65cb1c8e2333d410c89d945d5ef3d071ed96",
    "notes/research_mixed_open_local_factor_coverage.md": "b0fdc0b9b968c29469b86f5d29f9bc86b1dd535f762ac1386f96bd3514e3659a",
    "notes/research_mixed_typed_last_row_envelopes.md": "5732f40ffc086acddb21632a5d6af3e4905ebad38f97e62e89953802b1bdd10d",
    "notes/research_mixed_endpoint_cap_rectangle.md": "9211d45bdd031c908690a723ebcd4b40a34fed90f44858301a809ee5901c15e8",
    "notes/research_mixed_selected_half_row_evaluation_design.md": "9c102c39633e39edb74163b29df89b5f048c969e3aea81bf426a03350f8cf18c",
    "experiments/certify_mixed_selected_half_row_budget.py": "c3fcced82e6677c65f7f76242e9ca7b00712e236d50a3608bca589e5456f0f34",
    "experiments/certify_mixed_next_four_endpoint_budget.py": "079d452389081a400235fd27aa0f0afbb68b91113943cb0eb9250be904b2e11f",
    "experiments/certify_mixed_reduced_disk_conditional_packets.py": "eb2fdf73da09bc7878cf2302688b44c86d4df95d76ead0e0dea106dad4998a33",
    "experiments/certify_mixed_endpoint_packet_extension.py": "cd90bd5d1dcaf37c909ff1b06a31e79cd9afc16225f0ce6b0e5bac3d8788928e",
    PREVIOUS: "6e3520360bf93d779c359f39f33e479cf422ef2fa7eadbfe23ce0b5383af7d27",
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class CenteredPrimitives(frozen.OriginalPrimitives):
    """Original branches, centered g, and the explicit own-four Q4 phase."""
    def __init__(self):
        # The inherited fixed cut and its private action are H-independent.
        super().__init__()
        self.height = frozen.rat(H)

    def g(self, w):
        self.regular(w)
        center = acb(w.real.mid(), w.imag.mid())
        center_value = super().g(center)
        derivative = (1-(-2*self.pi*self.ii*w).exp()).log()
        if not derivative.is_finite():
            raise frozen.Inconclusive("centered primitive derivative not finite")
        result = center_value+derivative*(w-center)
        if not result.is_finite():
            raise frozen.Inconclusive("centered primitive enclosure not finite")
        return result

    def Q4(self, s, z, b):
        # The additional own-factorial is -g(s), relative to Q3.
        return (self.g(s+z)+self.g(s+b)-3*self.g(s)
                -self.g(z)-self.g(b)+2*self.pi*self.ii*z*s)

    def Q(self, s, z, b):
        raise frozen.Inconclusive("use the explicit own-four Q4 phase")


def reference_four(box, primitive):
    """Return state, reason, (auxiliary, shapes, coordinates) for own four.

    Coordinates are intersected with necessary rectangles only after all
    whole-box exclusions. This is a pointwise containing enclosure, not a
    parameter-derivative enclosure. No coupled critical root is proposed.
    """
    pi, ii = primitive.pi, primitive.ii
    auxiliary = acb(BASE.ball(box[0], box[1]), BASE.ball(box[2], box[3]))
    U = (2*pi*ii*auxiliary).exp()
    shapes = {name: BASE.rational_enclosure(factors, U)
              for name, factors in maps_four.MAPS.items()}
    coordinates = {}
    for name, shape in shapes.items():
        if not shape.is_finite():
            return "split", "nonfinite "+name+" shape", None
        coordinate = ii*shape.log()/(2*pi)
        if not coordinate.is_finite():
            return "split", "nonfinite "+name+" coordinate", None
        lo, hi, hlo, hhi = map(F, maps_four.RANGES[name])
        if (frozen.upper(coordinate.real) < lo or frozen.lower(coordinate.real) > hi
                or frozen.upper(coordinate.imag) < hlo
                or frozen.lower(coordinate.imag) > hhi):
            return "excluded", name+" range", None
        coordinates[name] = coordinate
    for name in ("z", "s", "b"):
        if BASE.outside_disk(coordinates[name], ".30", "-.052", ".060"):
            return "excluded", name+" reduced disk", None
    for names, lo in ((("z", "s"), ".545"), (("s", "b"), ".527")):
        total = sum((coordinates[name].real for name in names), arb(0))
        if frozen.upper(total) < F(lo) or frozen.lower(total) > F(".77"):
            return "excluded", "+".join(names)+" coupled sum", None
    E, Z, S, B = (shapes[name] for name in ("e", "z", "s", "b"))
    # Own four: the next conditional denominator has (1-B)^3, not ^2.
    next_shape = (1-S*B)/(B*(1-S*B)+(1-B)**3)
    if not next_shape.is_finite():
        return "split", "nonfinite next external shape", None
    if frozen.lower(next_shape.imag) > 0:
        return "excluded", "next external upper half-plane", None
    next_coordinate = ii*next_shape.log()/(2*pi)
    if not next_coordinate.is_finite():
        return "split", "nonfinite next external coordinate", None
    if (BASE.outside_typed_domain(next_coordinate, 3)
            and BASE.outside_typed_domain(next_coordinate, 4)):
        return "excluded", "next external typed domains", None

    lam = (2*pi*primitive.height).exp()/abs(Z)
    if not lam.is_finite() or not lam > 0:
        return "split", "nonfinite or nonpositive radial multiplier", None
    try:
        A = primitive.log_abs(1-lam*E*Z)-primitive.log_abs(1-E*Z)
        B_log = primitive.log_abs(1-lam*S*Z)-primitive.log_abs(1-S*Z)
        C = primitive.log_abs(1-lam*Z)-primitive.log_abs(1-Z)
    except frozen.Inconclusive as error:
        return "split", str(error), None
    ell = lam.log()
    a_star = (ii*(1+S)/(1-S)).real
    if not all(value.is_finite() for value in (A, B_log, C, ell, a_star)):
        return "split", "nonfinite adaptive reference scalar", None
    necessary = (
        (ell-B_log, F(0), F(1)),
        (coordinates["s"].real+coordinates["z"].real-frozen.rat("1/2"),
         F(".045"), F(".21")),
        (coordinates["z"].imag, F("-.078"), F("-.020")),
        (coordinates["s"].imag, F("-.102"), F("-.001")),
    )
    if any(frozen.upper(value) < lo or frozen.lower(value) > hi
           for value, lo, hi in necessary):
        return "excluded", "actual scalar ranges", None
    if frozen.upper(a_star) < F(2, 5):
        return "excluded", "actual ordinary curvature", None
    for name, w in coordinates.items():
        lo, hi, hlo, hhi = maps_four.RANGES[name]
        coordinates[name] = acb(frozen.intersect_interval(w.real, lo, hi),
                                frozen.intersect_interval(w.imag, hlo, hhi))
    return "retained", "", (auxiliary, shapes, coordinates)


def inspect(box, primitive):
    """One evaluation of the four bounds in the specification, Eq(13)."""
    details = {}
    try:
        state, reason, ref = reference_four(box, primitive)
        if state != "retained":
            return state, reason, details
        auxiliary, shapes, coordinates = ref
        details["auxiliary"] = frozen.complex_record(auxiliary)
        details["reference_shapes"] = {
            name: frozen.complex_record(w) for name, w in shapes.items()}
        details["reference_coordinates_after_necessary_intersection"] = {
            name: frozen.complex_record(w) for name, w in coordinates.items()}
        pi, ii = primitive.pi, primitive.ii
        e, z, s, b = (coordinates[name] for name in ("e", "z", "s", "b"))
        E, Z, S, B = (shapes[name] for name in ("e", "z", "s", "b"))
        zH = acb(z.real, primitive.height)
        lam = (2*pi*primitive.height).exp()/abs(Z)
        if not lam.is_finite() or not lam > 0:
            raise frozen.Inconclusive("nonfinite or nonpositive radial multiplier")

        # j(v)=Re q(v+ih_b)-Re g(v+ih_b)/2. Its tangent uses
        # p=g'(s+b)-3g'(b)/2. These halfweights cancel at the trial,
        # but remain in both the gradient and its curvature 41/10.
        p_real = primitive.log_abs(1-S*B)-frozen.rat("3/2")*primitive.log_abs(1-B)
        outgoing_gradient = primitive.log_abs(1+B)-primitive.log_abs(1-S*B)
        outgoing_gain = frozen.quadratic_gain(
            outgoing_gradient, b.real, ".22", ".45", F(41, 10))
        details["outgoing"] = {
            "p_real": frozen.real_record(p_real),
            "gradient": frozen.real_record(outgoing_gradient),
            "curvature_rational": "41/10",
            "gain_rational": str(outgoing_gain),
            "halfweight": "j=Re q-Re g/2; p=g'(s+b)-3g'(b)/2",
        }
        gz, gzH = primitive.g(z), primitive.g(zH)
        qzH, qb = primitive.q(zH), primitive.q(b)
        ordinary = primitive.Q4(s, z, b)
        common = qzH.real+qb.real-pi*primitive.height-ordinary.real+gz.real
        main_increment = (primitive.g(e+zH)-primitive.g(e+z)-gzH+gz).real
        actual_action = primitive.endpoint_action(e, auxiliary)
        left_increment = (primitive.psi(primitive.cut, zH, primitive.cut_action)
                          -primitive.psi(e, z, actual_action)).real
        A = primitive.log_abs(1-lam*E*Z)-primitive.log_abs(1-E*Z)
        private_gain = frozen.quadratic_gain(A, e.real, ".3", ".4", F(28, 5))
        details.update({
            "radial_multiplier": frozen.real_record(lam),
            "reference_private_action": frozen.complex_record(actual_action),
            "fixed_cut_private_action": frozen.complex_record(primitive.cut_action),
            "fixed_cut_private_root": frozen.complex_record(primitive.cut_u),
            "ordinary_Q4": frozen.complex_record(ordinary),
            "q_selected_incoming": frozen.complex_record(qzH),
            "q_outgoing": frozen.complex_record(qb),
            "g_reference_incoming": frozen.complex_record(gz),
            "g_selected_incoming": frozen.complex_record(gzH),
            "common": frozen.real_record(common),
            "main_increment": frozen.real_record(main_increment),
            "left_increment": frozen.real_record(left_increment),
            "private_gradient": frozen.real_record(A),
            "private_curvature_rational": "28/5",
            "private_gain_rational": str(private_gain),
        })
        majorants = {}
        for where, ep, increment in (
                ("main", E, main_increment),
                ("left", (-2*pi*ii*primitive.cut).exp(), left_increment)):
            for nu, label in ((1, "factorial"), (0, "forced")):
                gradient = (primitive.log_abs(1-lam*ep*Z)
                            +primitive.log_abs(1+lam*Z)
                            -(2+nu)*primitive.log_abs(1-lam*Z))
                mu = (F(7) if nu else F(33, 5)) if where == "main" else (
                    F(69, 10) if nu else F(13, 2))
                incoming_gain = frozen.quadratic_gain(
                    gradient, z.real, ".22", ".45", mu)
                fourier = -nu*gzH.real-2*nu*pi*primitive.height
                private = private_gain if where == "main" else F(0)
                total = (increment+common+fourier+frozen.rat(outgoing_gain)
                         +frozen.rat(private)+frozen.rat(incoming_gain))
                if not total.is_finite():
                    raise frozen.Inconclusive("nonfinite "+where+"/"+label+" majorant")
                majorants[where+"_"+label] = {
                    "nu": nu, "cap_profile": where,
                    "fourier_adjustment": frozen.real_record(fourier),
                    "incoming_gradient": frozen.real_record(gradient),
                    "incoming_curvature_rational": str(mu),
                    "incoming_gain_rational": str(incoming_gain),
                    "private_gain_rational": str(private),
                    "outgoing_gain_rational": str(outgoing_gain),
                    "value": frozen.real_record(total),
                    "strictly_below_zero": frozen.upper(total) < 0,
                    "strictly_below_candidate_gap": frozen.upper(total) < -GAP,
                }
        details["majorants"] = majorants
        if all(majorants[key]["strictly_below_candidate_gap"] for key in KEYS):
            return "accepted", "four strict tests on this single box", details
        return "inconclusive", "four majorants not certified on this box", details
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
    for name, expected in previous["input_sha256"].items():
        path = Path(name)
        relative = str((path if path.is_absolute() else REPO/path).relative_to(REPO))
        if relative in bindings and bindings[relative] != expected:
            raise ValueError("conflicting inherited binding: "+relative)
        bindings[relative] = expected
    bindings[str(Path(__file__).resolve().relative_to(REPO))] = digest(Path(__file__))
    for name, expected in bindings.items():
        if digest(REPO/name) != expected:
            raise ValueError("frozen dependency mismatch: "+name)

    # Metadata and exact rational splits only; no old inspect is called.
    accepted = [leaf for leaf in previous["leaves"] if leaf["status"] == "accepted"]
    depth = max(len(leaf["address"]) for leaf in accepted)
    chosen = min((leaf for leaf in accepted if len(leaf["address"]) == depth),
                 key=lambda leaf: leaf["address"])
    if chosen["address"] != ADDRESS or depth != 18:
        raise ValueError("deterministic inherited leaf differs from the specification")
    box = BASE.ROOT
    if list(map(str, box)) != previous["initial_auxiliary_rectangle"]:
        raise ValueError("original root rectangle mismatch")
    for split_depth, branch in enumerate(ADDRESS):
        box = BASE.split(box, split_depth)[int(branch)]
    if box != BOX:
        raise ValueError("exact depth18 box reconstruction failed")

    def forbidden(*args, **kwargs):
        raise RuntimeError("old scalar inspection is forbidden in this diagnostic")

    frozen.inspect = maps_four.inspect = BASE.inspect = forbidden
    ctx.prec = 160
    started = time.monotonic()
    result = inspect(box, CenteredPrimitives())
    for name, expected in bindings.items():
        if digest(REPO/name) != expected:
            raise RuntimeError("input changed during diagnostic: "+name)
    record = {
        "status": "diagnostic complete",
        "scope": "Four next-four half-row bounds on one inherited auxiliary box only",
        "actual_word_realization_claimed": False,
        "precision_bits": 160, "height": str(H), "candidate_gap": str(GAP),
        "tested_address": ADDRESS, "tested_box": list(map(str, box)),
        "inherited_leaf": chosen,
        "selection": "lexicographically first accepted leaf of maximum accepted depth",
        "formula": "next-four evaluation Eq(13), explicit Q4 and outgoing Gamma_41/10",
        "primitive": "centered original g; original actual auxiliary and canonical fixed cut",
        "result": {"status": result[0], "reason": result[1], "details": result[2]},
        "inspect_calls": 1, "old_scalar_inspect_calls": 0,
        "tested_boxes": 1, "subdivisions": 0, "automatic_retries": 0,
        "root_proposals": 0, "finite_source_evaluations": 0,
        "elapsed_seconds": time.monotonic()-started, "input_sha256": bindings,
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
