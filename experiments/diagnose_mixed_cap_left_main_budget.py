#!/usr/bin/env python3
"""Two cap-left/ordinary-main scalar bounds on one prescribed reference box.

Imports the frozen reference/phase helpers, with only the proved centered g
enclosure substituted. No cover, root solve, finite quantum sum or old
inspect() evaluation is performed.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time

from flint import acb, ctx

import certify_mixed_selected_half_row_budget as frozen


REPO = Path(__file__).resolve().parents[1]
PREVIOUS = REPO/"repro/results/research-mixed-half-row-centered-primitive-diagnostic.json"
PREVIOUS_SHA = "d27dd0d7a4d42147c92084a3c77b37b1b0091809e78ba3b096826109e110709d"
PROOF = REPO/"notes/research_mixed_selected_cap_left_main_majorant.md"
PROOF_SHA = "0b8a4fce5f53e4279171d6c3ba09e7e36eb75e5005f6214e655e58219a3d02d1"
CENTERED_PROOF = REPO/"notes/research_mixed_centered_primitive_enclosure.md"
CENTERED_SHA = "ce2bebcca5ff53ca466948517f4324123b09bb7c92c6736409ff47ece9aac956"
DRIVER_SHA = "c3fcced82e6677c65f7f76242e9ca7b00712e236d50a3608bca589e5456f0f34"
KEYS = ("factorial", "forced")
GAP = F(1, 2000)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class CenteredPrimitives(frozen.OriginalPrimitives):
    """The exact enclosure reviewed in the frozen centered-primitive note."""
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


def inspect(box, primitive):
    """Evaluate only the corrected pair of Eq(20)/(23) majorants."""
    details = {}
    try:
        state, reason, ref = frozen.reference(box, primitive)
        if state != "retained":
            return state, reason, details
        auxiliary, shapes, coordinates = ref
        details["reference_coordinates"] = {
            name: frozen.complex_record(w) for name, w in coordinates.items()}
        pi, ii = primitive.pi, primitive.ii
        e, z, s = (coordinates[name] for name in ("e", "z", "s"))
        Z, S = shapes["z"], shapes["s"]
        zH = acb(z.real, primitive.height)
        lam = (2*pi*primitive.height).exp()/abs(Z)
        if not lam.is_finite() or not lam > 0:
            raise frozen.Inconclusive("nonfinite or nonpositive radial multiplier")
        ell = lam.log()
        d_raw = ell-(primitive.log_abs(1-lam*S*Z)-primitive.log_abs(1-S*Z))
        if not d_raw.is_finite() or frozen.upper(d_raw) < 0:
            raise frozen.Inconclusive("proved nonnegative d not enclosed")
        d = frozen.interval(max(F(0), frozen.lower(d_raw)), frozen.upper(d_raw))

        # Only negative s displacement can increase the linear term -d*ds.
        # The exact gain increases with d and allowed length, and decreases
        # with positive curvature. All quantities below are exact rationals.
        cot_s = (ii*(1+S)/(1-S)).real
        if not cot_s.is_finite():
            raise frozen.Inconclusive("nonfinite actual index curvature")
        delta_lower = max(F(1, 5), min(frozen.lower(cot_s), F(15, 53)))
        pi_lower = frozen.lower(pi)
        mu_s_lower = 2*pi_lower*delta_lower
        index_length = frozen.upper(s.real)-F(1, 5)
        if index_length < 0 or mu_s_lower <= 0:
            raise frozen.Inconclusive("invalid negative index displacement interval")
        d_upper = max(F(0), frozen.upper(d))
        index_displacement = min(index_length, d_upper/mu_s_lower)
        index_gain = (d_upper*index_displacement
                      -mu_s_lower*index_displacement*index_displacement/2)

        # Eq(23): preserve S(.27)-S(e*) at the original complex e*, as well
        # as both original cap chirps inside psi(). No outgoing phase or
        # slope is independently maximized: its trial gradient is exactly 0.
        actual_action = primitive.endpoint_action(e, auxiliary)
        cap_increment = (primitive.psi(primitive.cut, zH, primitive.cut_action)
                         -primitive.psi(e, z, actual_action)).real
        gz, gzH = primitive.g(z), primitive.g(zH)
        ordinary_primitive_increment = (
            primitive.g(s+zH)-primitive.g(s+z)-gzH+gz).real
        # zH and z share the same real coordinate, so this exact form
        # retains the chirp without a spurious real subtraction interval.
        delta_z = acb(0, primitive.height-z.imag)
        chirp_increment = (2*pi*ii*s*delta_z).real
        ordinary_increment = ordinary_primitive_increment+chirp_increment
        trial_common = cap_increment+ordinary_increment+gz.real
        if not trial_common.is_finite():
            raise frozen.Inconclusive("nonfinite common trial action")

        details["reference_private_action"] = frozen.complex_record(actual_action)
        details["fixed_cut_private_action"] = frozen.complex_record(primitive.cut_action)
        details["cap_increment"] = frozen.real_record(cap_increment)
        details["ordinary_primitive_increment"] = frozen.real_record(ordinary_primitive_increment)
        details["chirp_increment"] = frozen.real_record(chirp_increment)
        details["ordinary_increment"] = frozen.real_record(ordinary_increment)
        details["g_reference_incoming"] = frozen.complex_record(gz)
        details["g_selected_incoming"] = frozen.complex_record(gzH)
        details["trial_common"] = frozen.real_record(trial_common)
        details["ell"] = frozen.real_record(ell)
        details["d_unclipped"] = frozen.real_record(d_raw)
        details["d_nonnegative"] = frozen.real_record(d)
        details["index_cotangent"] = frozen.real_record(cot_s)
        details["index_delta_lower_rational"] = str(delta_lower)
        details["pi_lower_rational"] = str(pi_lower)
        details["index_curvature_lower_rational"] = str(mu_s_lower)
        details["negative_index_length_upper_rational"] = str(index_length)
        details["negative_index_displacement_rational"] = str(index_displacement)
        details["index_gain_rational"] = str(index_gain)
        details["outgoing_gradient_exact"] = "0"
        details["outgoing_gain_exact"] = "0"

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
                "strictly_below_zero": bool(total < 0),
                "strictly_below_candidate_gap": bool(total < -frozen.rat(GAP)),
            }
        details["majorants"] = majorants
        if all(majorants[key]["strictly_below_candidate_gap"] for key in KEYS):
            return "accepted", "two strict tests on this single box", details
        return "split", "two majorants not certified on this box", details
    except frozen.Inconclusive as error:
        return "split", str(error), details


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    for path, expected in ((PREVIOUS, PREVIOUS_SHA), (PROOF, PROOF_SHA),
                           (CENTERED_PROOF, CENTERED_SHA),
                           (Path(frozen.__file__), DRIVER_SHA)):
        if digest(path) != expected:
            raise ValueError("frozen input hash mismatch: "+str(path))
    previous = json.loads(PREVIOUS.read_text())
    if previous["precision_bits"] != 160 or previous["tested_address"] != "01101001101111000":
        raise ValueError("unexpected prescribed diagnostic box")
    bindings = dict(previous["input_sha256"])
    for path in (PREVIOUS, PROOF, CENTERED_PROOF, Path(__file__).resolve()):
        bindings[str(path.relative_to(REPO))] = digest(path)
    for name, expected in bindings.items():
        if digest(REPO/name) != expected:
            raise ValueError("frozen dependency mismatch: "+name)

    ctx.prec = 160
    address = previous["tested_address"]
    box = frozen.base.ROOT
    for depth, branch in enumerate(address):
        box = frozen.base.split(box, depth)[int(branch)]
    if list(map(str, box)) != previous["tested_box"] or len(address) != 17:
        raise ValueError("exact depth17 box reconstruction failed")
    started = time.monotonic()
    result = inspect(box, CenteredPrimitives())
    for name, expected in bindings.items():
        if digest(REPO/name) != expected:
            raise RuntimeError("input changed during diagnostic: "+name)
    record = {
        "status": "diagnostic complete",
        "scope": "Two cap-left/ordinary-main scalar majorants on one prescribed box only",
        "precision_bits": 160, "height": str(frozen.H),
        "candidate_gap": str(GAP), "tested_address": address,
        "tested_box": list(map(str, box)),
        "formula": "Corrected cap-left/main Eq(23), with the strong one-sided index gain",
        "primitive": "Reviewed centered original g enclosure; original canonical cap actions",
        "result": {"status": result[0], "reason": result[1], "details": result[2]},
        "inspect_calls": 1, "frozen_half_row_inspect_calls": 0,
        "tested_boxes": 1, "subdivisions": 0,
        "root_proposals": 0, "finite_source_evaluations": 0,
        "elapsed_seconds": time.monotonic()-started,
        "input_sha256": bindings,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({
        "status": record["status"], "tested_address": address,
        "result_status": result[0], "reason": result[1],
        "elapsed_seconds": record["elapsed_seconds"],
        "upper_bounds": {
            key: value["value"]["upper_rational"]
            for key, value in result[2].get("majorants", {}).items()},
    }), flush=True)


if __name__ == "__main__":
    main()
