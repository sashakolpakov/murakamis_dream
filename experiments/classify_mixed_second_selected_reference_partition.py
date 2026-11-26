#!/usr/bin/env python3
"""One bounded alpha1 reference pass over 678 inherited candidate cells.

Both beta cases, staged necessary filters, Cartesian nonzero guards and
optional direct-only fallback. No subdivision, roots or scalar budgets.
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


ROOT = Path(__file__).resolve().parents[1]
SHIFTED = "experiments/diagnose_mixed_second_selected_shifted_reference.py"
COVER = "repro/results/research-mixed-next-four-adaptive-budget-attempt02.json"
SAVED = "repro/results/research-mixed-second-selected-shifted-reference-diagnostic.json"
PINNED = {
    SHIFTED: "bc407efcaf8c549a38e7c2e8d9c4493b5730481844b9262ac2a4c7ea0e3fb75e",
    COVER: "6e3520360bf93d779c359f39f33e479cf422ef2fa7eadbfe23ce0b5383af7d27",
    SAVED: "4030c1155214b98b9a7129204d99fbefae13fce6bf0313a3f45833f68f99d4d5",
    "notes/research_mixed_second_selected_reference_cover_reuse.md": "c742dbff21129df250f718c3155f079a095092fe298df8a030081d281d3ae2a8",
    "notes/research_mixed_second_selected_reference_partition_pass.md": "72e6ee4ea508daebd4ea31bf7fe8580241140fe98a2436cf21c17cf6dd6e21da",
    "notes/research_mixed_second_selected_saved_reference_exclusion.md": "6cdbff9cfc3459811c462e76c02d381f87eb07da8eb56f51709f0d7629c89292",
    "repro/results/research-mixed-second-selected-saved-reference-exclusion.json": "eebfecc37125d94d239388f346b612ba6e000b5067b0069a67091b65b383e36d",
}
CELL_LIMITS = {"reference_calls": 2, "shared_parameter_enclosures": 1,
               "rational_maps_attempted": 9, "unique_shifted_polynomials": 27,
               "gaussian_integer_shift_multiplications": 20962,
               "interval_polynomial_horner_multiplications": 714, "factored_products": 36}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def validate_partition(addresses):
    addresses = sorted(addresses)
    if len(addresses) != len(set(addresses)):
        raise ValueError("duplicate partition address")
    if any(not set(a) <= {"0", "1"} for a in addresses):
        raise ValueError("invalid binary partition address")
    if any(b.startswith(a) for a, b in zip(addresses, addresses[1:])):
        raise ValueError("partition is not prefix-free")
    if sum((F(1, 2**len(a)) for a in addresses), F(0)) != 1:
        raise ValueError("partition does not have unit mass")


def inputs():
    bindings = dict(PINNED)
    for name, expected in bindings.items():
        if sha(ROOT/name) != expected:
            raise ValueError("frozen pass input mismatch: "+name)
    # The pinned shifted module imports no repository provider at import time.
    shifted = importlib.import_module("diagnose_mixed_second_selected_shifted_reference")
    old, exact, previous, inherited = shifted.verified_inputs()
    for source in (inherited, json.loads((ROOT/SAVED).read_text())["input_sha256"]):
        for name, expected in source.items():
            p = Path(name)
            name = str((p if p.is_absolute() else ROOT/p).relative_to(ROOT))
            if name in bindings and bindings[name] != expected:
                raise ValueError("conflicting pass input: "+name)
            bindings[name] = expected
    bindings[str(Path(__file__).resolve().relative_to(ROOT))] = sha(Path(__file__))
    for name, expected in bindings.items():
        if sha(ROOT/name) != expected:
            raise ValueError("pre-import pass dependency mismatch: "+name)
    if previous["status"] != "proved" or previous["unresolved"]:
        raise ValueError("inherited cover is incomplete")
    validate_partition([leaf["address"] for leaf in previous["leaves"]])
    excluded = [leaf for leaf in previous["leaves"] if leaf["status"] == "excluded"]
    candidates = sorted((leaf for leaf in previous["leaves"] if leaf["status"] == "accepted"), key=lambda leaf: leaf["address"])
    if (len(previous["leaves"]), len(excluded), len(candidates)) != (3291, 2613, 678):
        raise ValueError("inherited leaf inventory mismatch")
    if sum((F(1, 2**len(leaf["address"])) for leaf in candidates), F(0)) != F(2587, 65536):
        raise ValueError("candidate mass mismatch")
    return shifted, old, exact, previous, excluded, candidates, bindings


def make_evaluator(shifted, old):
    Base = shifted.make_evaluator(old)

    class StagedReference(Base):
        def nonzero(self, value, label):
            item = {"label": label, "value": self.f.complex_record(value)}
            self.details["regularity_checks"].append(item)
            self.finite(value, label)
            distance = max(F(0), self.f.lower(value.real), -self.f.upper(value.real),
                           self.f.lower(value.imag), -self.f.upper(value.imag))
            radial = abs(value)
            radial_pass = radial.is_finite() and bool(radial > 0)
            passed = distance > 0 or radial_pass
            item.update({"cartesian_modulus_lower_rational": str(distance),
                         "modulus": self.f.real_record(radial), "strictly_separated": passed,
                         "criterion": "Cartesian" if distance > 0 else ("radial" if radial_pass else "none")})
            if not passed:
                raise self.f.Inconclusive("zero not excluded: "+label)
            return value

        def prepare(self, box):
            if getattr(self, "preparation_failure", None):
                raise self.f.Inconclusive(self.preparation_failure)
            if self.prepared_box is not None:
                if box != self.prepared_box:
                    raise ValueError("per-cell provider cannot change boxes")
                return
            if ctx.prec != 160:
                raise ValueError("fixed precision mismatch")
            try:
                self.counts["shared_parameter_enclosures"] += 1
                self.auxiliary = acb(self.base.ball(box[0], box[1]), self.base.ball(box[2], box[3]))
                self.W = self.nonzero((2*self.p.pi*self.p.ii*self.auxiliary).exp(), "W")
                self.W0 = acb(self.W.real.mid(), self.W.imag.mid())
                self.deltaW = self.W-self.W0
                real, imag = F(str(self.W0.real.fmpq())), F(str(self.W0.imag.fmpq()))
                if any(q.denominator & (q.denominator-1) for q in (real, imag)):
                    raise self.f.Inconclusive("midpoint is not dyadic")
                denominator = max(real.denominator, imag.denominator)
                self.shift = denominator.bit_length()-1
                self.M = real.numerator*(denominator//real.denominator)
                self.N = imag.numerator*(denominator//imag.denominator)
                self.shared.update({"auxiliary": self.f.complex_record(self.auxiliary),
                    "W": self.f.complex_record(self.W), "W0": self.f.complex_record(self.W0),
                    "W_minus_W0": self.f.complex_record(self.deltaW),
                    "midpoint_gaussian_numerators_hex": [hex(self.M), hex(self.N)],
                    "midpoint_denominator_power_of_two": self.shift})
                self.prepared_box = box
            except self.f.Inconclusive as error:
                self.preparation_failure = str(error)
                raise

        def shifted_polynomial(self, coefficients):
            result = super().shifted_polynomial(coefficients)
            record = self.shared["polynomials"][result[2]]
            key = "shifted_integer_coefficients_ascending_hex"
            if key in record:
                record["exact_shift_coefficients_sha256"] = canonical_hash(record.pop(key))
                record.pop("coefficient_denominator_powers_of_two")
            return result

        def rational_map(self, name):
            if name in self.map_failures:
                raise self.f.Inconclusive(self.map_failures[name])
            if name in self.map_cache:
                self.counts["rational_map_cache_hits"] += 1
                return self.map_cache[name]
            self.counts["rational_maps_attempted"] += 1
            saved = self.shared["maps"][name] = {}
            try:
                record = self.exact["maps"][name]
                n, n0, nf = self.factored_product(record["numerator"], name+" numerator")
                d, d0, df = self.factored_product(record["denominator"], name+" denominator", True)
                direct = self.finite(n/d, name+" direct quotient")
                midpoint = self.finite(n0/d0, name+" midpoint quotient")
                saved.update({"numerator": self.f.complex_record(n), "denominator": self.f.complex_record(d),
                    "numerator_factors": nf, "denominator_factors": df,
                    "direct_quotient": self.f.complex_record(direct), "midpoint_value": self.f.complex_record(midpoint)})
            except self.f.Inconclusive as error:
                saved.update({"status": "inconclusive", "reason": str(error)})
                self.map_failures[name] = str(error)
                raise
            value = direct
            try:
                record_d = record["derivative"]
                dn, _, dnf = self.factored_product(record_d["numerator"], name+" derivative numerator")
                saved["derivative_numerator"] = self.f.complex_record(dn)
                saved["derivative_numerator_factors"] = dnf
                dd, _, ddf = self.factored_product(record_d["denominator"], name+" derivative denominator", True)
                derivative = self.finite(dn/dd, name+" canceled derivative")
                centered = self.finite(midpoint+derivative*self.deltaW, name+" mean-value enclosure")
                saved.update({"derivative_denominator": self.f.complex_record(dd),
                    "derivative_denominator_factors": ddf, "full_derivative_dW": self.f.complex_record(derivative),
                    "mean_value_enclosure": self.f.complex_record(centered)})
                def intersect(x, y):
                    return self.f.interval(max(self.f.lower(x), self.f.lower(y)),
                                           min(self.f.upper(x), self.f.upper(y)))
                value = acb(intersect(direct.real, centered.real), intersect(direct.imag, centered.imag))
                saved["refinement_status"] = "direct and mean-value intersection"
            except self.f.Inconclusive as error:
                saved.update({"refinement_status": "direct-only fallback", "refinement_reason": str(error)})
                self.counts["direct_only_fallbacks"] += 1
            saved.update({"status": "enclosed", "full_value": self.f.complex_record(value),
                "full_value_widths_rational": {axis: str(self.f.upper(getattr(value, axis))-self.f.lower(getattr(value, axis)))
                                               for axis in ("real", "imag")}})
            self.map_cache[name] = value
            return value

        def original_regularity(self, shapes):
            E, A, U, Z, V, B, C = (shapes[name] for name in ("e", "a", "u", "z", "v", "b", "c"))
            self.nonzero(self.W, "original W")
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
            for label, value in (("endpoint final=(1-EA)/U", (1-E*A)/U),
                                 ("first retained=U(1-AU)", U*(1-A*U)),
                                 ("first external=(1-UZ)/V", (1-U*Z)/V),
                                 ("second retained=V(1-ZV)", V*(1-Z*V)),
                                 ("second external=(1-VB)/C", (1-V*B)/C)):
                self.nonzero(value, "original denominator identity "+label)

        def reference(self, box, beta, details):
            if beta not in (0, 1):
                raise ValueError("invalid beta")
            self.counts["reference_calls"] += 1
            self.details = details
            details.update({"regularity_checks": [], "reference_shapes": {},
                "reference_coordinates_before_intersection": {},
                "reference_coordinates_after_necessary_intersection": {}, "passed_stages": []})
            self.prepare(box)
            pi, ii = self.p.pi, self.p.ii
            ordinary = (".267", ".433", "-.065", ".068") if beta == 0 else (".24", ".36", "-.102", "-.001")
            ranges = {"e": (".333", ".363", "-.051", "-.019"),
                      "a": (".246", ".350", "-.078", "-.020"),
                      "u": (".24", ".36", "-.102", "-.001"),
                      "z": (".24", ".36", "-.102", "-.001"), "v": ordinary, "b": ordinary}
            shapes, coordinates = {}, {}
            for key, map_name in (("e", "E"), ("a", "A"), ("u", "U"), ("z", "Z"), ("v", "V"),
                                  ("b", "B"+str(beta)), ("c", "C"+str(beta))):
                shape = self.rational_map(map_name)
                shapes[key] = shape
                details["reference_shapes"][key] = self.f.complex_record(shape)
                if self.f.lower(shape.imag) > 0:
                    return "excluded", key+" shape strictly in upper half-plane", None
                if not self.f.upper(shape.imag) < 0:
                    raise self.f.Inconclusive("original lower-half-plane log branch uncertain: "+key)
                w = self.finite(ii*shape.log()/(2*pi), key+" decoded coordinate")
                details["reference_coordinates_before_intersection"][key] = self.f.complex_record(w)
                if key in ranges:
                    limits = ranges[key]
                    if self.outside_range(w, limits):
                        return "excluded", key+" necessary rectangle", None
                    if key != "e":
                        kind = 3+beta if key in ("v", "b") else 4
                        center = (".35", "-.01", ".083") if kind == 3 else (".30", "-.052", ".060")
                        if self.base.outside_disk(w, *center):
                            return "excluded", key+" reduced disk", None
                    w = acb(self.f.intersect_interval(w.real, *limits[:2]),
                            self.f.intersect_interval(w.imag, *limits[2:]))
                coordinates[key] = w
                details["reference_coordinates_after_necessary_intersection"][key] = self.f.complex_record(w)
                tests = {"u": (("a", "u"), ".545"),
                         "z": (("u", "z"), ".525" if beta == 0 else ".55"),
                         "v": (("z", "v"), ".545"),
                         "b": (("v", "b"), ".6" if beta == 0 else ".525"),
                         "c": (("b", "c"), ".545")}
                if key in tests:
                    names, floor = tests[key]
                    if self.outside_sum(coordinates, names, floor):
                        return "excluded", "+".join(names)+" necessary sum", None
                if key == "c":
                    suffix, reasons = [], {}
                    for sigma in (0, 1):
                        errors = []
                        if self.base.outside_typed_domain(w, 3+sigma):
                            errors.append("next external typed envelope")
                        floor = ".6" if beta == 0 else (".525" if sigma == 0 else ".55")
                        if self.outside_sum(coordinates, ("v", "b"), floor):
                            errors.append("typed v+b internal sum")
                        reasons[str(sigma)] = errors
                        if not errors:
                            suffix.append(3+sigma)
                    details["next_external_type_alternatives"] = suffix
                    details["next_type_exclusion_reasons"] = reasons
                    if not suffix:
                        return "excluded", "both next external types excluded", None
                details["passed_stages"].append(key)
            self.original_regularity(shapes)
            details["all_original_regularity_checks_passed"] = True
            return "retained", "necessary reference tests and original regularity retained", (shapes, coordinates)

    return StagedReference


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    shifted, old, exact, previous, excluded, candidates, bindings = inputs()
    four = importlib.import_module("diagnose_mixed_four_four_half_row_budget")
    root_box = tuple(map(F, previous["initial_auxiliary_rectangle"]))
    if root_box != four.BASE.ROOT:
        raise ValueError("root rectangle mismatch")
    def decode(address):
        box = root_box
        for depth, branch in enumerate(address):
            box = four.BASE.split(box, depth)[int(branch)]
        return box
    excluded_hash = canonical_hash(excluded)
    def forbidden(*args, **kwargs):
        raise RuntimeError("old source/reference/scalar callback forbidden")
    for provider in (shifted, old, four, four.frozen, four.maps_four, four.BASE):
        provider.inspect = provider.main = forbidden
    old.Evaluator.inspect = old.Evaluator.reference = old.Evaluator.conjugate = forbidden
    four.reference_four = four.frozen.reference = forbidden
    four.CenteredPrimitives.g = four.frozen.OriginalPrimitives.g = forbidden
    ctx.prec = 160
    primitive = SimpleNamespace(pi=arb.pi(), ii=acb(0, 1))
    Provider = make_evaluator(shifted, old)
    cells = [{"address": leaf["address"], "box": list(map(str, decode(leaf["address"]))),
              "original_leaf_sha256": canonical_hash(leaf), "cases": {
                  beta: {"status": "unvisited", "reason": "pending initial reference case", "details": {}}
                  for beta in ("0", "1")}} for leaf in candidates]
    aggregate = Counter()
    stop_reason = "completed all initial cases"
    started = time.monotonic()
    for index, cell in enumerate(cells):
        evaluator = Provider(four, primitive, exact)
        box = tuple(map(F, cell["box"]))
        fatal = False
        for beta in (0, 1):
            details = {}
            try:
                state, reason, _ = evaluator.reference(box, beta, details)
                cell["cases"][str(beta)] = {"status": state, "reason": reason, "details": details}
            except four.frozen.Inconclusive as error:
                cell["cases"][str(beta)] = {"status": "inconclusive", "reason": str(error), "details": details}
            except Exception as error:
                cell["cases"][str(beta)] = {"status": "inconclusive", "reason": "unexpected error: "+repr(error), "details": details}
                stop_reason, fatal = "unexpected error", True
                break
        cell["shared_transport"] = evaluator.shared
        cell["call_counts"] = dict(evaluator.counts)
        aggregate.update(evaluator.counts)
        for name, limit in CELL_LIMITS.items():
            if evaluator.counts[name] > limit:
                stop_reason, fatal = "arithmetic operation cap exceeded: "+name, True
        if (index+1) % 20 == 0 or index+1 == len(cells) or fatal:
            print(json.dumps({"processed_cells": index+1, "initial_cells": len(cells),
                "counts_by_beta": {beta: dict(Counter(c["cases"][beta]["status"] for c in cells)) for beta in ("0", "1")},
                "elapsed_seconds": time.monotonic()-started, "stop_reason": stop_reason if fatal else None}), flush=True)
        if fatal:
            break
    if canonical_hash(excluded) != excluded_hash:
        raise RuntimeError("inherited exclusions mutated")
    if [cell["address"] for cell in cells] != [leaf["address"] for leaf in candidates]:
        raise RuntimeError("candidate address inventory changed")
    validate_partition([leaf["address"] for leaf in excluded]+[cell["address"] for cell in cells])
    for cell in cells:
        if tuple(map(F, cell["box"])) != decode(cell["address"]):
            raise RuntimeError("candidate rectangle changed")
    coverage = {}
    for beta in ("0", "1"):
        counts = Counter({"inherited excluded": len(excluded)})
        masses = {"inherited excluded": sum((F(1, 2**len(leaf["address"])) for leaf in excluded), F(0))}
        for cell in cells:
            status = cell["cases"][beta]["status"]
            counts[status] += 1
            masses[status] = masses.get(status, F(0))+F(1, 2**len(cell["address"]))
        if sum(counts.values()) != 3291 or sum(masses.values(), F(0)) != 1:
            raise RuntimeError("beta partition accounting failed")
        coverage[beta] = {"counts": dict(counts), "dyadic_masses": {key: str(value) for key, value in masses.items()}}
    for name, limit in CELL_LIMITS.items():
        if aggregate[name] > 678*limit:
            stop_reason = "global arithmetic operation cap exceeded: "+name
    for name, expected in bindings.items():
        if sha(ROOT/name) != expected:
            raise RuntimeError("input changed during reference pass: "+name)
    complete = stop_reason == "completed all initial cases" and all(
        cell["cases"][beta]["status"] != "unvisited" for cell in cells for beta in ("0", "1"))
    result = {"status": "reference partition pass complete" if complete else "reference partition pass incomplete",
        "scope": "whole-alpha1 necessary-reference classification only; no scalar signs",
        "alpha": 1, "beta_candidates": [0, 1], "precision_bits": 160,
        "initial_auxiliary_rectangle": list(map(str, root_box)), "source_record": COVER,
        "source_record_sha256": PINNED[COVER], "source_leaves_canonical_sha256": canonical_hash(previous["leaves"]),
        "inherited_excluded_leaves": excluded, "inherited_excluded_canonical_sha256": excluded_hash,
        "candidate_cells": cells, "coverage_by_beta": coverage, "terminal_partition_verified": True,
        "stop_reason": stop_reason, "call_counts": dict(aggregate), "per_cell_operation_limits": CELL_LIMITS,
        "initial_cells": 678, "maximum_reference_cases": 1356, "subdivisions": 0,
        "automatic_retries": 0, "alternate_boxes": 0, "old_inspect_calls": 0,
        "primitive_evaluations": 0, "scalar_budget_evaluations": 0, "root_proposals": 0,
        "finite_source_evaluations": 0, "word_realization_claimed": False,
        "elapsed_seconds": time.monotonic()-started, "input_sha256": bindings}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as stream:
        stream.write(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": result["status"], "result_sha256": sha(args.output),
        "coverage_by_beta": coverage, "call_counts": dict(aggregate),
        "elapsed_seconds": result["elapsed_seconds"]}), flush=True)


if __name__ == "__main__":
    main()
