#!/usr/bin/env python3
"""Centered rational reference transport on one prescribed alpha1 box only.

Two beta cases, 160 bits, no scalar budget, primitive, source root, cover,
replacement box, retry or subdivision. Failed direct inputs stay frozen.
"""
import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import importlib
import json
from pathlib import Path
import time
from types import SimpleNamespace

from flint import acb, arb, ctx


REPO = Path(__file__).resolve().parents[1]
OLD = "experiments/diagnose_mixed_second_selected_central_budget.py"
PINNED = {
    OLD: "fa99e0b8de2a9b2bb4bf999f6057024dcf4500c35b5173638961ad226251e9ce",
    "repro/results/research-mixed-second-selected-central-budget-diagnostic.json": "805c2e5ebf71f0c043c0d5bacfdf6a3bd25a64f250a45e6df755224a79df9f9f",
    "notes/research_mixed_second_selected_centered_reference_evaluation.md": "e62b6e2ad427b10fe16944ab9551918e85b8f35d2116bab313216605163dfaea",
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def make_evaluator(old):
    class CenteredReference(old.Evaluator):
        def nonzero(self, value, label):
            item = {"label": label, "value": self.f.complex_record(value)}
            self.details["regularity_checks"].append(item)
            self.finite(value, label)
            modulus = abs(value)
            item["modulus"] = self.f.real_record(modulus)
            item["strictly_separated"] = bool(modulus > 0)
            if not modulus > 0:
                raise self.f.Inconclusive("zero not excluded: "+label)
            return value

        def save_jet(self, name, midpoint, value, derivative, extra):
            item = {"midpoint_value": self.f.complex_record(midpoint),
                    "full_value": self.f.complex_record(value),
                    "full_derivative_dW": self.f.complex_record(derivative), **extra}
            self.details["stages"][name] = item
            for label, q in (("midpoint", midpoint), ("full image", value), ("derivative", derivative)):
                self.finite(q, name+" "+label)
            return {"midpoint": midpoint, "value": value, "derivative": derivative}

        def factored(self, name, factors):
            self.counts["factored_map_stages"] += 1
            numerator, denominator = factors
            n, dn = self.base.product_jet(numerator, self.W)
            d, dd = self.base.product_jet(denominator, self.W)
            self.nonzero(d, name+" full factored denominator")
            n0, _ = self.base.product_jet(numerator, self.W0)
            d0, _ = self.base.product_jet(denominator, self.W0)
            self.nonzero(d0, name+" midpoint factored denominator")
            midpoint = n0/d0
            derivative = (dn*d-n*dd)/(d*d)
            # This frozen helper evaluates precisely midpoint+derivative*(W-W0).
            value = self.base.rational_enclosure(factors, self.W)
            return self.save_jet(name, midpoint, value, derivative, {
                "formula": "frozen factored rational mean-value map",
                "full_numerator": self.f.complex_record(n),
                "full_denominator": self.f.complex_record(d),
                "full_numerator_derivative": self.f.complex_record(dn),
                "full_denominator_derivative": self.f.complex_record(dd)})

        def retained_stage(self, name, Pjet, Qjet, power):
            self.counts["retained_transfer_stages"] += 1
            P, Q = Pjet["value"], Qjet["value"]
            dP, dQ = Pjet["derivative"], Qjet["derivative"]
            n = self.nonzero(1-P*Q, name+" full 1-PQ")
            self.nonzero(Q, name+" full Q")
            dn = -dP*Q-P*dQ
            h = (1-Q)**power
            dh = -power*(1-Q)**(power-1)*dQ
            f = n-P*h
            df = dn-dP*h-P*dh
            d = self.nonzero(Q*n, name+" full quotient denominator")
            dd = dQ*n+Q*dn
            derivative = self.finite((df*d-f*dd)/(d*d), name+" quotient derivative")
            P0, Q0 = Pjet["midpoint"], Qjet["midpoint"]
            n0 = 1-P0*Q0
            d0 = self.nonzero(Q0*n0, name+" midpoint quotient denominator")
            midpoint = (n0-P0*(1-Q0)**power)/d0
            value = midpoint+derivative*self.deltaW
            return self.save_jet(name, midpoint, value, derivative, {
                "formula": "Eq(3)-(4), quotient-rule retained stage", "power": power,
                "full_numerator": self.f.complex_record(f),
                "full_denominator": self.f.complex_record(d),
                "full_numerator_derivative": self.f.complex_record(df),
                "full_denominator_derivative": self.f.complex_record(dd)})

        def external_stage(self, name, Qjet, Rjet, power):
            self.counts["external_transfer_stages"] += 1
            Q, R = Qjet["value"], Rjet["value"]
            dQ, dR = Qjet["derivative"], Rjet["derivative"]
            k = self.nonzero(1-Q*R, name+" full 1-QR")
            dk = -dQ*R-Q*dR
            d = self.nonzero(R*k+(1-R)**power, name+" full quotient denominator")
            dd = dR*k+R*dk-power*(1-R)**(power-1)*dR
            derivative = self.finite((dk*d-k*dd)/(d*d), name+" quotient derivative")
            Q0, R0 = Qjet["midpoint"], Rjet["midpoint"]
            k0 = 1-Q0*R0
            d0 = self.nonzero(R0*k0+(1-R0)**power, name+" midpoint quotient denominator")
            midpoint = k0/d0
            value = midpoint+derivative*self.deltaW
            return self.save_jet(name, midpoint, value, derivative, {
                "formula": "Eq(5)-(6), quotient-rule external stage", "power": power,
                "full_numerator": self.f.complex_record(k),
                "full_denominator": self.f.complex_record(d),
                "full_numerator_derivative": self.f.complex_record(dk),
                "full_denominator_derivative": self.f.complex_record(dd)})

        def reference(self, box, beta, details):
            self.counts["reference_calls"] += 1
            self.details = details
            details.update({"stages": {}, "regularity_checks": []})
            pi, ii = self.p.pi, self.p.ii
            auxiliary = acb(self.base.ball(box[0], box[1]), self.base.ball(box[2], box[3]))
            self.W = self.nonzero((2*pi*ii*auxiliary).exp(), "W")
            self.W0 = acb(self.W.real.mid(), self.W.imag.mid())
            self.deltaW = self.W-self.W0
            details["auxiliary"] = self.f.complex_record(auxiliary)
            details["positive_sign_W"] = self.f.complex_record(self.W)
            details["common_midpoint_W0"] = self.f.complex_record(self.W0)
            details["full_W_minus_W0"] = self.f.complex_record(self.deltaW)
            jets = {name: self.factored(name, self.four.maps_four.MAPS[key])
                    for name, key in (("e", "e"), ("a", "z"), ("u", "s"), ("z", "b"))}
            jets["v"] = self.external_stage("v", jets["u"], jets["z"], 3)
            jets["b"] = self.retained_stage("b", jets["z"], jets["v"], 2+beta)
            jets["c"] = self.external_stage("c", jets["v"], jets["b"], 2+beta)
            shapes = {name: jet["value"] for name, jet in jets.items()}
            details["reference_shapes"] = {name: self.f.complex_record(value) for name, value in shapes.items()}
            E, A, U, Z, V, B, C = (shapes[name] for name in ("e", "a", "u", "z", "v", "b", "c"))
            self.nonzero(5*self.W*self.W-2*self.W+1, "original endpoint D")
            for name, value in shapes.items():
                self.nonzero(value, "original shape "+name)
            for label, value in (("1-EW", 1-E*self.W), ("1-E", 1-E), ("1-EA", 1-E*A),
                                 ("1-UA", 1-U*A), ("1-A", 1-A)):
                self.nonzero(value, "original endpoint "+label)
            for label, P, Q, R, T in (("first", A, U, Z, V), ("second", Z, V, B, C)):
                for expression, value in (("1-PQ", 1-P*Q), ("1-QR", 1-Q*R), ("1-RT", 1-R*T),
                                          ("1-Q", 1-Q), ("1-R", 1-R)):
                    self.nonzero(value, "original "+label+" "+expression)
            details["original_denominator_identities"] = {
                "endpoint_final": "(1-EA)/U; numerator and denominator separated",
                "first_retained": "U(1-AU); both factors separated",
                "remaining_transfer_denominators": "checked before the respective centered stage"}
            # FILTER_BLOCK: copied verbatim from the frozen direct reference.
            coordinates = {}
            for name, shape in shapes.items():
                # Every admissible leg shape is strictly in the lower half-plane.
                if self.f.lower(shape.imag) > 0:
                    return "excluded", name+" shape strictly in upper half-plane", None
                if not self.f.upper(shape.imag) < 0:
                    raise self.f.Inconclusive("original lower-half-plane log branch uncertain: "+name)
                coordinates[name] = self.finite(ii*shape.log()/(2*pi), name+" decoded coordinate")
            details["reference_coordinates_before_intersection"] = {
                name: self.f.complex_record(value) for name, value in coordinates.items()}
            ordinary = (".267", ".433", "-.065", ".068") if beta == 0 else (
                ".24", ".36", "-.102", "-.001")
            ranges = {
                "e": (".333", ".363", "-.051", "-.019"),
                "a": (".246", ".350", "-.078", "-.020"),
                "u": (".24", ".36", "-.102", "-.001"),
                "z": (".24", ".36", "-.102", "-.001"),
                "v": ordinary, "b": ordinary,
            }
            for name, limits in ranges.items():
                if self.outside_range(coordinates[name], limits):
                    return "excluded", name+" necessary rectangle", None
            for name in ("a", "u", "z", "v", "b"):
                kind = 3+beta if name in ("v", "b") else 4
                center = (".35", "-.01", ".083") if kind == 3 else (".30", "-.052", ".060")
                if self.base.outside_disk(coordinates[name], *center):
                    return "excluded", name+" reduced disk", None
            for names, lo in ((("a", "u"), ".545"), (("z", "v"), ".545"),
                              (("b", "c"), ".545"), (("u", "z"), ".525" if beta == 0 else ".55")):
                if self.outside_sum(coordinates, names, lo):
                    return "excluded", "+".join(names)+" necessary sum", None
            if self.outside_sum(coordinates, ("v", "b"), ".6" if beta == 0 else ".525"):
                return "excluded", "v+b necessary sum", None
            suffix = []
            suffix_reasons = {}
            for sigma in (0, 1):
                reasons = []
                if self.base.outside_typed_domain(coordinates["c"], 3+sigma):
                    reasons.append("next external typed envelope")
                floor = ".6" if beta == 0 else (".525" if sigma == 0 else ".55")
                if self.outside_sum(coordinates, ("v", "b"), floor):
                    reasons.append("typed v+b internal sum")
                suffix_reasons[str(sigma)] = reasons
                if not reasons:
                    suffix.append(sigma)
            details["next_external_type_alternatives"] = [3+sigma for sigma in suffix]
            details["next_type_exclusion_reasons"] = suffix_reasons
            if not suffix:
                return "excluded", "both next external types excluded", None
            for name, limits in ranges.items():
                w = coordinates[name]
                coordinates[name] = acb(self.f.intersect_interval(w.real, *limits[:2]),
                                        self.f.intersect_interval(w.imag, *limits[2:]))
            details["reference_coordinates_after_necessary_intersection"] = {
                name: self.f.complex_record(value) for name, value in coordinates.items()}
            details["filters"] = "reference-curve (7)-(9), endpoint alpha1 and proved attached-height bound; no proposed z-height strengthening"
            return "retained", "", (shapes, coordinates)

    return CenteredReference


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    for name, expected in PINNED.items():
        if digest(REPO/name) != expected:
            raise ValueError("new frozen input mismatch: "+name)
    # The verified direct driver imports no other repository module at import.
    old = importlib.import_module("diagnose_mixed_second_selected_central_budget")
    bindings, previous = old.verified_inputs()
    for name, expected in PINNED.items():
        if name in bindings and bindings[name] != expected:
            raise ValueError("conflicting frozen binding: "+name)
        bindings[name] = expected
    bindings[str(Path(__file__).resolve().relative_to(REPO))] = digest(Path(__file__))
    four = importlib.import_module("diagnose_mixed_four_four_half_row_budget")
    accepted = [leaf for leaf in previous["leaves"] if leaf["status"] == "accepted"]
    depth = max(len(leaf["address"]) for leaf in accepted)
    chosen = min((leaf for leaf in accepted if len(leaf["address"]) == depth), key=lambda leaf: leaf["address"])
    if chosen["address"] != old.ADDRESS or depth != 18:
        raise ValueError("prescribed inherited address mismatch")
    box = four.BASE.ROOT
    if list(map(str, box)) != previous["initial_auxiliary_rectangle"]:
        raise ValueError("original root rectangle mismatch")
    for split_depth, branch in enumerate(old.ADDRESS):
        box = four.BASE.split(box, split_depth)[int(branch)]
    if box != old.BOX:
        raise ValueError("exact prescribed box reconstruction failed")

    def forbidden(*args, **kwargs):
        raise RuntimeError("source/primitive/scalar/old reference evaluation forbidden")

    for provider in (old, four, four.frozen, four.maps_four, four.BASE):
        provider.inspect = provider.main = forbidden
    old.Evaluator.inspect = old.Evaluator.reference = old.Evaluator.conjugate = forbidden
    four.reference_four = four.frozen.reference = forbidden
    four.CenteredPrimitives.g = four.frozen.OriginalPrimitives.g = forbidden
    ctx.prec = 160
    primitive = SimpleNamespace(pi=arb.pi(), ii=acb(0, 1))
    evaluator = make_evaluator(old)(four, primitive)
    started = time.monotonic()
    results = {}
    for beta in (0, 1):
        details = {}
        try:
            state, reason, _ = evaluator.reference(box, beta, details)
            results[str(beta)] = {"status": state, "reason": reason, "details": details}
        except four.frozen.Inconclusive as error:
            results[str(beta)] = {"status": "inconclusive", "reason": str(error), "details": details}
    if evaluator.counts["reference_calls"] != 2:
        raise RuntimeError("reference call limit violated")
    for name, expected in bindings.items():
        if digest(REPO/name) != expected:
            raise RuntimeError("input changed during reference diagnostic: "+name)
    record = {
        "status": "reference diagnostic complete", "scope": "centered rational reference transport only",
        "actual_word_realization_claimed": False, "uniform_sign_claimed": False,
        "alpha": 1, "beta_candidates": [0, 1], "precision_bits": 160,
        "tested_address": old.ADDRESS, "tested_box": list(map(str, box)), "inherited_leaf": chosen,
        "results_by_beta": results, "call_counts": dict(evaluator.counts),
        "tested_boxes": 1, "subdivisions": 0, "automatic_retries": 0, "alternate_boxes": 0,
        "scalar_budget_evaluations": 0, "primitive_evaluations": 0, "old_reference_calls": 0,
        "old_inspect_calls": 0, "root_proposals": 0, "finite_source_evaluations": 0,
        "elapsed_seconds": time.monotonic()-started, "input_sha256": bindings,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as output:
        output.write(json.dumps(record, indent=2)+"\n")
    print(json.dumps({"status": record["status"], "result_sha256": digest(args.output),
        "elapsed_seconds": record["elapsed_seconds"], "call_counts": record["call_counts"],
        "results": {beta: {"status": value["status"], "reason": value["reason"],
                           "completed_stages": list(value["details"].get("stages", {}))}
                    for beta, value in results.items()}}), flush=True)


if __name__ == "__main__":
    main()
