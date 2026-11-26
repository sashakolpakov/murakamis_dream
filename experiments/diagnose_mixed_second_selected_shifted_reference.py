#!/usr/bin/env python3
"""Exact-shift reference arithmetic on the one prescribed alpha1 box.

No primitive, scalar budget, source root, adaptive box or retry is run.
The reusable evaluator exposes reference(box, beta, details), returning
the original state/reason/(shapes, coordinates) protocol.
"""
import argparse
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
EXACT = "repro/results/research-mixed-second-selected-rational-transport-exact.json"
PRIOR = "repro/results/research-mixed-second-selected-centered-reference-diagnostic.json"
PINNED = {
    OLD: "fa99e0b8de2a9b2bb4bf999f6057024dcf4500c35b5173638961ad226251e9ce",
    EXACT: "7db105fdc67e0331bebc69d29d33c11cfaff6432f0366344932c96966887bc43",
    PRIOR: "368bc80f65b30971f2b742d5f52a71b8bdc2da4cc6b2fc6ba74a0d8a05411719",
    "experiments/diagnose_mixed_second_selected_centered_reference.py": "d8572fff700d88b88b891a83d73bcbd9bd9dcf02f9c7c88f500214e35889e228",
    "experiments/derive_mixed_second_selected_rational_transport.py": "71d5fd6d67229b69aaea53cc9e1c540ceb01a68e7fb0d126d2f8d63e8651470a",
    "notes/research_mixed_second_selected_canceled_rational_transport.md": "daf68906eeefa6d0fdda94456b942ff49545f5d4be07f274fa1701701366506d",
    "notes/research_mixed_second_selected_shifted_reference_evaluation.md": "93084573a8f4e2ad1f8d2292352164afe296c8793d6c068903137b20e0e3cee2",
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verified_inputs():
    bindings = dict(PINNED)
    for name, expected in bindings.items():
        if digest(REPO/name) != expected:
            raise ValueError("new frozen input mismatch: "+name)
    exact = json.loads((REPO/EXACT).read_text())
    prior = json.loads((REPO/PRIOR).read_text())
    if exact["status"] != "exact rational identities proved" or exact["alpha"] != 1:
        raise ValueError("exact rational record scope mismatch")
    for record in (exact, prior):
        for name, expected in record["input_sha256"].items():
            p = Path(name)
            relative = str((p if p.is_absolute() else REPO/p).relative_to(REPO))
            if relative in bindings and bindings[relative] != expected:
                raise ValueError("conflicting inherited binding: "+relative)
            bindings[relative] = expected
    for name, expected in bindings.items():
        if digest(REPO/name) != expected:
            raise ValueError("transitive frozen input mismatch: "+name)
    # This verified module imports only the standard library and flint.
    old = importlib.import_module("diagnose_mixed_second_selected_central_budget")
    old_bindings, previous = old.verified_inputs()
    for name, expected in old_bindings.items():
        if name in bindings and bindings[name] != expected:
            raise ValueError("conflicting original binding: "+name)
        bindings[name] = expected
    bindings[str(Path(__file__).resolve().relative_to(REPO))] = digest(Path(__file__))
    for name, expected in bindings.items():
        if digest(REPO/name) != expected:
            raise ValueError("pre-import input mismatch: "+name)
    return old, exact, previous, bindings


def make_evaluator(old):
    class ShiftedReference(old.Evaluator):
        def __init__(self, four, primitive, exact):
            super().__init__(four, primitive)
            self.exact = exact
            self.prepared_box = None
            self.polynomial_cache, self.map_cache, self.map_failures = {}, {}, {}
            self.shared = {"polynomials": {}, "maps": {}}
            factors = {tuple(factor["coefficients_descending"])
                       for shape in exact["maps"].values()
                       for source in (shape, shape["derivative"])
                       for part in ("numerator", "denominator")
                       for factor in source[part]["factors"]}
            degrees = [len(coefficients)-1 for coefficients in factors]
            if (len(degrees), max(degrees), sum(degrees), sum(d*(d+1)//2 for d in degrees)) != (27, 111, 714, 20962):
                raise ValueError("fixed polynomial operation bounds mismatch")

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

        def prepare(self, box):
            if self.prepared_box is not None:
                if box != self.prepared_box:
                    raise ValueError("this bounded provider cannot change its parameter box")
                return
            if box != old.BOX or ctx.prec != 160:
                raise ValueError("prescribed box or precision mismatch")
            self.counts["shared_parameter_enclosures"] += 1
            self.auxiliary = acb(self.base.ball(box[0], box[1]), self.base.ball(box[2], box[3]))
            self.W = self.nonzero((2*self.p.pi*self.p.ii*self.auxiliary).exp(), "W")
            self.W0 = acb(self.W.real.mid(), self.W.imag.mid())
            self.deltaW = self.W-self.W0
            real = F(str(self.W0.real.fmpq()))
            imag = F(str(self.W0.imag.fmpq()))
            for q in (real, imag):
                if q.denominator & (q.denominator-1):
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

        def shifted_polynomial(self, coefficients):
            key = tuple(coefficients)
            if key in self.polynomial_cache:
                return self.polynomial_cache[key]
            degree = len(key)-1
            if not 1 <= degree <= 111:
                raise ValueError("unexpected polynomial degree")
            self.counts["unique_shifted_polynomials"] += 1
            # Integer Horner shift of D^d P((M+iN+X)/D).
            shifted = [(key[0], 0)]
            for e, coefficient in enumerate(key[1:], 1):
                new = []
                for j, (x, y) in enumerate(shifted):
                    re, im = self.M*x-self.N*y, self.M*y+self.N*x
                    if j:
                        re += shifted[j-1][0]
                        im += shifted[j-1][1]
                    new.append((re, im))
                new[0] = (new[0][0]+(coefficient << (self.shift*e)), new[0][1])
                new.append(shifted[-1])
                self.counts["gaussian_integer_shift_multiplications"] += len(shifted)
                shifted = new
            balls = [acb(self.f.rat(F(re, 1 << (self.shift*(degree-j)))),
                         self.f.rat(F(im, 1 << (self.shift*(degree-j)))))
                     for j, (re, im) in enumerate(shifted)]
            value = balls[-1]
            for coefficient in reversed(balls[:-1]):
                value = value*self.deltaW+coefficient
                self.counts["interval_polynomial_horner_multiplications"] += 1
            name = hashlib.sha256(json.dumps(key, separators=(",", ":")).encode()).hexdigest()
            self.shared["polynomials"][name] = {
                "coefficients_descending": list(key), "degree": degree,
                "shifted_integer_coefficients_ascending_hex": [[hex(re), hex(im)] for re, im in shifted],
                "coefficient_denominator_powers_of_two": [self.shift*(degree-j) for j in range(degree+1)],
                "midpoint_value": self.f.complex_record(balls[0]),
                "full_value": self.f.complex_record(value)}
            self.finite(value, "shifted polynomial "+name)
            self.polynomial_cache[key] = (value, balls[0], name)
            return self.polynomial_cache[key]

        def factored_product(self, record, label, denominator=False):
            value, midpoint = acb(record["content"]), acb(record["content"])
            polynomial_ids = []
            self.counts["factored_products"] += 1
            for factor in record["factors"]:
                full, point, name = self.shifted_polynomial(factor["coefficients_descending"])
                if denominator:
                    self.nonzero(full, label+" factor "+name)
                value *= full**factor["power"]
                midpoint *= point**factor["power"]
                polynomial_ids.append({"polynomial_id": name, "power": factor["power"]})
            self.finite(value, label)
            self.finite(midpoint, label+" midpoint")
            if denominator:
                self.nonzero(value, label+" product")
                self.nonzero(midpoint, label+" midpoint product")
            return value, midpoint, polynomial_ids

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
                saved.update({"numerator": self.f.complex_record(n), "denominator": self.f.complex_record(d),
                    "numerator_factors": nf, "denominator_factors": df})
                direct = self.finite(n/d, name+" direct quotient")
                midpoint = self.finite(n0/d0, name+" midpoint quotient")
                record_d = record["derivative"]
                dn, _, dnf = self.factored_product(record_d["numerator"], name+" derivative numerator")
                dd, _, ddf = self.factored_product(record_d["denominator"], name+" derivative denominator", True)
                derivative = self.finite(dn/dd, name+" canceled derivative")
                centered = self.finite(midpoint+derivative*self.deltaW, name+" mean-value enclosure")
                saved.update({"direct_quotient": self.f.complex_record(direct),
                    "midpoint_value": self.f.complex_record(midpoint),
                    "derivative_numerator": self.f.complex_record(dn),
                    "derivative_denominator": self.f.complex_record(dd),
                    "derivative_numerator_factors": dnf, "derivative_denominator_factors": ddf,
                    "full_derivative_dW": self.f.complex_record(derivative),
                    "mean_value_enclosure": self.f.complex_record(centered)})
                def intersect(x, y):
                    return self.f.interval(max(self.f.lower(x), self.f.lower(y)),
                                           min(self.f.upper(x), self.f.upper(y)))
                value = acb(intersect(direct.real, centered.real), intersect(direct.imag, centered.imag))
                saved["full_value"] = self.f.complex_record(value)
                saved["full_value_widths_rational"] = {
                    axis: str(self.f.upper(getattr(value, axis))-self.f.lower(getattr(value, axis)))
                    for axis in ("real", "imag")}
                saved["status"] = "enclosed"
                self.map_cache[name] = value
                return value
            except self.f.Inconclusive as error:
                saved.update({"status": "inconclusive", "reason": str(error)})
                self.map_failures[name] = str(error)
                raise

        def reference(self, box, beta, details):
            if beta not in (0, 1):
                raise ValueError("only the two prescribed beta cases are allowed")
            self.counts["reference_calls"] += 1
            self.details = details
            details["regularity_checks"] = []
            self.prepare(box)
            pi, ii = self.p.pi, self.p.ii
            shapes = {key: self.rational_map(name) for key, name in
                      (("e", "E"), ("a", "A"), ("u", "U"), ("z", "Z"), ("v", "V"),
                       ("b", "B"+str(beta)), ("c", "C"+str(beta)))}
            details["auxiliary"] = self.f.complex_record(self.auxiliary)
            details["reference_shapes"] = {name: self.f.complex_record(value) for name, value in shapes.items()}
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
            details["original_denominator_identities"] = "All canceled original denominators checked by the exact identities in specification Eq(7), after numerator/shape separation."
            # FILTER_BLOCK is copied unchanged below from the frozen direct driver.
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

    return ShiftedReference


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    old, exact, previous, bindings = verified_inputs()
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
    evaluator = make_evaluator(old)(four, primitive, exact)
    started = time.monotonic()
    results = {}
    for beta in (0, 1):
        details = {}
        try:
            state, reason, _ = evaluator.reference(box, beta, details)
            results[str(beta)] = {"status": state, "reason": reason, "details": details}
        except four.frozen.Inconclusive as error:
            results[str(beta)] = {"status": "inconclusive", "reason": str(error), "details": details}
    limits = {"reference_calls": 2, "shared_parameter_enclosures": 1,
              "rational_maps_attempted": 9, "unique_shifted_polynomials": 27,
              "gaussian_integer_shift_multiplications": 20962,
              "interval_polynomial_horner_multiplications": 714, "factored_products": 36}
    if evaluator.counts["reference_calls"] != 2:
        raise RuntimeError("reference call count differs from the prescribed two cases")
    for name, limit in limits.items():
        if evaluator.counts[name] > limit:
            raise RuntimeError("bounded arithmetic operation count exceeded: "+name)
    for name, expected in bindings.items():
        if digest(REPO/name) != expected:
            raise RuntimeError("input changed during shifted reference diagnostic: "+name)
    record = {
        "status": "reference diagnostic complete", "scope": "exact-shift canceled rational reference transport only",
        "actual_word_realization_claimed": False, "uniform_sign_claimed": False,
        "alpha": 1, "beta_candidates": [0, 1], "precision_bits": 160,
        "tested_address": old.ADDRESS, "tested_box": list(map(str, box)), "inherited_leaf": chosen,
        "shared_transport": evaluator.shared, "results_by_beta": results,
        "call_counts": dict(evaluator.counts), "operation_limits": limits,
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
        "results": {beta: {"status": value["status"], "reason": value["reason"]}
                    for beta, value in results.items()}}), flush=True)


if __name__ == "__main__":
    main()
