#!/usr/bin/env python3
"""One inherited-box second-selection central diagnostic, alpha=1 only.

Both beta alternatives, two Fourier branches and fifteen predetermined
flows. No root solve, source evaluation, cover, refinement or replacement.
All repository providers are hash-checked before they are imported.
"""
import argparse
import ast
from collections import Counter
from fractions import Fraction as F
import hashlib
import importlib
import json
from pathlib import Path
import time

from flint import acb, arb, ctx


REPO = Path(__file__).resolve().parents[1]
HELPER = "experiments/diagnose_mixed_four_four_half_row_budget.py"
PREVIOUS = "repro/results/research-mixed-next-four-adaptive-budget-attempt02.json"
ADDRESS = "001111101111010111"
BOX = tuple(map(F, ("115337/512000", "57677/256000", "8919/256000", "279/8000")))
H, GAP = F(1, 100), F(1, 2000)
THETAS = tuple(map(F, ("0", "1/4", "1/2", "3/4", "1")))
RHOS = tuple(map(F, ("0", "1/4", "1/2")))
PINNED = {
    HELPER: "cc1d86c233ef74f343796b6ad64967ca8a86c8dd315546b1de7c440cd9f9f82f",
    PREVIOUS: "6e3520360bf93d779c359f39f33e479cf422ef2fa7eadbfe23ce0b5383af7d27",
    "experiments/certify_mixed_endpoint_log_budget.py": "b8306df590b8b4c90e4e230845245658bc5695d8355c6e63779aba50973c75b2",
    "notes/research_mixed_second_selected_central_budget.md": "c839f134024ccd2ad0a95ce81ed8cd16fb0bcefb9d508a347c9278c84bd3f21d",
    "notes/research_mixed_second_selected_central_evaluation.md": "f38b0ff6e5f7194e2f3740553a3acc26bb0c09894d5cd95bac94caa184443be8",
    "notes/research_mixed_second_selected_horizontal_concavity.md": "dac208b242a8dd24f1ce0c29e15775bd343554e0cb0141e2ad84c0fe64312ca8",
    "notes/research_mixed_second_selected_reference_curve.md": "4a591366418d251cbcfaad5705ff439747a8745cc8e75f64561e70aec3ef5bd5",
    "notes/research_mixed_second_selected_plateau_reduction.md": "015c85c322ff3563ec6752b5c499080c3e906360920aaeed2063508ef2db868f",
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verified_inputs():
    """Read pinned metadata and literal helper pins without importing code."""
    bindings = dict(PINNED)
    for name, expected in bindings.items():
        if digest(REPO/name) != expected:
            raise ValueError("initial frozen input mismatch: "+name)
    tree = ast.parse((REPO/HELPER).read_text())
    assignments = {target.id: node.value for node in tree.body
                   if isinstance(node, ast.Assign)
                   for target in node.targets if isinstance(target, ast.Name)}
    previous_name = ast.literal_eval(assignments["PREVIOUS"])
    if previous_name != PREVIOUS:
        raise ValueError("helper inherited-record mismatch")
    literal_pins = assignments["PINNED"]
    if not isinstance(literal_pins, ast.Dict):
        raise ValueError("helper pins are not a static dictionary")
    imported_pins = {}
    for key, value in zip(literal_pins.keys, literal_pins.values):
        name = previous_name if isinstance(key, ast.Name) and key.id == "PREVIOUS" else ast.literal_eval(key)
        imported_pins[name] = ast.literal_eval(value)
    previous = json.loads((REPO/PREVIOUS).read_text())
    if previous["status"] != "proved" or previous["unresolved"]:
        raise ValueError("inherited central cover is not complete")
    for source in (imported_pins, previous["input_sha256"]):
        for name, expected in source.items():
            path = Path(name)
            relative = str((path if path.is_absolute() else REPO/path).relative_to(REPO))
            if relative in bindings and bindings[relative] != expected:
                raise ValueError("conflicting frozen binding: "+relative)
            bindings[relative] = expected
    bindings[str(Path(__file__).resolve().relative_to(REPO))] = digest(Path(__file__))
    for name, expected in bindings.items():
        if digest(REPO/name) != expected:
            raise ValueError("transitive frozen input mismatch: "+name)
    return bindings, previous


def make_primitive_class(four):
    class CentralPrimitives(four.CenteredPrimitives):
        def __init__(self):
            # No unrelated private-cut construction is needed for this phase.
            self.pi, self.ii = arb.pi(), acb(0, 1)
            self.height = four.frozen.rat(H)
            self.counts = Counter()

        def g(self, w):
            self.counts["centered_primitive_calls"] += 1
            return super().g(w)
    return CentralPrimitives


class Evaluator:
    def __init__(self, four, primitive):
        self.four, self.f, self.base = four, four.frozen, four.BASE
        self.p = primitive
        self.counts = Counter()

    def finite(self, value, label):
        if not value.is_finite():
            raise self.f.Inconclusive("nonfinite "+label)
        return value

    def nonzero(self, value, label):
        self.finite(value, label)
        if not abs(value) > 0:
            raise self.f.Inconclusive("zero not excluded: "+label)
        return value

    def divide(self, numerator, denominator, label):
        return self.finite(numerator/self.nonzero(denominator, label), label+" quotient")

    def transfer(self, P, Q, power, label):
        n = self.nonzero(1-P*Q, label+" 1-PQ")
        self.nonzero(1-Q, label+" 1-Q")
        R = self.divide(1-self.divide(P*(1-Q)**power, n, label+" n"), Q, label+" Q")
        self.nonzero(R, label+" R")
        self.nonzero(1-R, label+" 1-R")
        k = self.nonzero(1-Q*R, label+" 1-QR")
        T = self.divide(k, R*k+(1-R)**power, label+" final denominator")
        self.nonzero(T, label+" T")
        self.nonzero(1-R*T, label+" 1-RT")
        return R, T

    def outside_range(self, w, ranges):
        lo, hi, hlo, hhi = map(F, ranges)
        return (self.f.upper(w.real) < lo or self.f.lower(w.real) > hi
                or self.f.upper(w.imag) < hlo or self.f.lower(w.imag) > hhi)

    def outside_sum(self, coordinates, names, lo, hi=".77"):
        total = sum((coordinates[name].real for name in names), arb(0))
        return self.f.upper(total) < F(lo) or self.f.lower(total) > F(hi)

    def reference(self, box, beta, details):
        """The same W in both transfers; necessary filters only, no old inspect."""
        self.counts["reference_calls"] += 1
        pi, ii = self.p.pi, self.p.ii
        auxiliary = acb(self.base.ball(box[0], box[1]), self.base.ball(box[2], box[3]))
        W = self.nonzero((2*pi*ii*auxiliary).exp(), "W")
        D = self.nonzero(5*W*W-2*W+1, "endpoint D")
        E = self.divide((1+W)**2, D, "endpoint D")
        self.nonzero(E, "E")
        self.nonzero(1-E*W, "1-EW")
        self.nonzero(1-E, "1-E")
        A = self.divide(1-self.divide((1-E*W)*(1-E), W, "W"), E, "E")
        self.nonzero(A, "A")
        self.nonzero(1-A, "1-A")
        n = self.nonzero(1-E*A, "1-EA")
        U = self.divide(n, A*n+(1-A)**3, "endpoint final denominator")
        self.nonzero(U, "U")
        self.nonzero(1-U*A, "1-UA")
        Z, V = self.transfer(A, U, 3, "first transfer")
        B, C = self.transfer(Z, V, 2+beta, "second transfer")
        shapes = dict(e=E, a=A, u=U, z=Z, v=V, b=B, c=C)
        details["auxiliary"] = self.f.complex_record(auxiliary)
        details["positive_sign_W"] = self.f.complex_record(W)
        details["reference_shapes"] = {name: self.f.complex_record(value) for name, value in shapes.items()}
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

    def angle_at(self, q):
        """T(q) with exact rational clipping before the half-angle formula."""
        q = min(F(1), max(F(-1), q))
        if q == -1:
            return self.f.rat(F(1, 2))
        if q == 1:
            return arb(0)
        ratio = (1-q)/(1+q)
        if ratio <= 0:
            raise self.f.Inconclusive("nonpositive exact half-angle ratio")
        value = self.f.rat(ratio)
        if not value > 0:
            raise self.f.Inconclusive("half-angle ratio not outward positive")
        return self.finite(value.sqrt().atan()/self.p.pi, "half-angle value")

    def angle_interval(self, cosine):
        self.finite(cosine, "formal cosine target")
        lower_angle = self.angle_at(self.f.upper(cosine))
        upper_angle = self.angle_at(self.f.lower(cosine))
        return self.f.interval(self.f.lower(lower_angle), self.f.upper(upper_angle))

    def objective(self, force, target, center, height, coefficient, center_g, derivative):
        displacement = target-center
        value = (force*displacement-self.f.rat(coefficient)*(
            self.p.g(acb(target, height)).real-center_g-derivative*displacement))
        return self.finite(value, "scalar conjugate candidate")

    def conjugate(self, force, center, height, coefficient, lo, hi, zero=False, zero_edge=False):
        """Outward maximizer enclosure and both required nonconvex-edge candidates."""
        self.counts["node_conjugates" if coefficient > 0 else "edge_conjugates"] += 1
        record = {"force": self.f.real_record(force), "center": self.f.real_record(center),
                  "height": self.f.real_record(height), "coefficient": str(coefficient),
                  "target_interval": [str(lo), str(hi)]}
        if coefficient > 0 and zero:
            self.counts["exact_zero_node_conjugates"] += 1
            record.update({"exact_zero_node_identity": True, "value": self.f.real_record(arb(0))})
            return arb(0), record
        wstar = acb(center, height)
        shape = (-2*self.p.pi*self.p.ii*wstar).exp()
        derivative = self.p.log_abs(1-shape)
        center_g = self.p.g(wstar).real
        if coefficient == -1 and zero and zero_edge:
            # The proved outer-sum geometry gives .5<center<.77 pointwise.
            left = self.objective(force, self.f.rat(lo), center, height, coefficient, center_g, derivative)
            value = self.f.interval(max(F(0), self.f.lower(left)), max(F(0), self.f.upper(left)))
            record.update({"exact_zero_outer_edge_identity": True,
                           "left_candidate": self.f.real_record(left),
                           "upper_candidate": self.f.real_record(arb(0)),
                           "value": self.f.real_record(value)})
            return value, record
        radius = (2*self.p.pi*height).exp()
        if not radius > 0:
            raise self.f.Inconclusive("nonpositive scalar radius")
        target_norm = abs(1-shape)**2*(2*force/self.f.rat(coefficient)).exp()
        cosine = self.finite((1+radius*radius-target_norm)/(2*radius), "formal cosine")
        angle = self.angle_interval(cosine)
        candidate = self.f.clip_interval(angle if coefficient > 0 else 1-angle,
                                         lo if coefficient > 0 else F(1, 2), hi)
        candidate_value = self.objective(force, candidate, center, height, coefficient, center_g, derivative)
        record.update({"formal_cosine_before_clipping": self.f.real_record(cosine),
                       "clipped_angle": self.f.real_record(angle),
                       "candidate_target": self.f.real_record(candidate),
                       "candidate_value": self.f.real_record(candidate_value)})
        value = candidate_value
        if coefficient == -1:
            left = self.objective(force, self.f.rat(lo), center, height, coefficient, center_g, derivative)
            value = self.f.interval(max(self.f.lower(left), self.f.lower(candidate_value)),
                                    max(self.f.upper(left), self.f.upper(candidate_value)))
            record["left_candidate"] = self.f.real_record(left)
            record["upper_candidate"] = self.f.real_record(candidate_value)
        record["value"] = self.f.real_record(value)
        return value, record

    def inspect(self, box, beta):
        details = {}
        try:
            state, reason, reference = self.reference(box, beta, details)
            if state != "retained":
                return {"status": state, "reason": reason, "details": details}
            shapes, coords = reference
            pi, height = self.p.pi, self.p.height
            a, u, z, v, b = (coords[name] for name in ("a", "u", "z", "v", "b"))
            U, Z, V = (shapes[name] for name in ("u", "z", "v"))
            zH = acb(z.real, height)
            lam = self.finite((2*pi*height).exp()/abs(Z), "radial multiplier")
            if not lam > 0:
                raise self.f.Inconclusive("nonpositive radial multiplier")
            ell = lam.log()
            A = self.p.log_abs(1-lam*U*Z)-self.p.log_abs(1-U*Z)
            B = self.p.log_abs(1-lam*V*Z)-self.p.log_abs(1-V*Z)
            C = self.p.log_abs(1-lam*Z)-self.p.log_abs(1-Z)
            GH = self.p.log_abs(1-lam*Z)
            gzH = self.p.g(zH).real
            vertical = ((self.p.g(u+zH)-self.p.g(u+z)
                         +self.p.g(v+zH)-self.p.g(v+z)).real
                        -3*gzH+3*self.p.g(z).real-2*pi*v.real*(height-z.imag))
            coarse = self.f.rat(F(21, 5) if beta == 0 else F(39, 10))*pi*(height-z.imag)**2/2
            scalar = dict(A=A, B=B, C=C, ell=ell, G_H=GH, radial_multiplier=lam,
                          exact_vertical_cost=vertical, coarse_vertical_bound=coarse, g_zH_real=gzH)
            details["scalars"] = {key: self.f.real_record(self.finite(value, key)) for key, value in scalar.items()}
            centers = [a.real, u.real, z.real, v.real, b.real]
            heights = [a.imag, u.imag, height, v.imag, b.imag]
            lows = list(map(F, (".22", ".22", ".22", ".2" if beta == 0 else ".22", ".22")))
            highs = list(map(F, (".45", ".5", ".45", ".5", ".45")))
            branches = {}
            for nu in (0, 1):
                D = A+B-3*C+(1-nu)*GH
                T = vertical+(1-nu)*gzH-2*nu*pi*height
                branch = {"nu": nu, "D_nu": self.f.real_record(D), "T_nu": self.f.real_record(T), "trials": []}
                for theta in THETAS:
                    for rho in RHOS:
                        self.counts["trial_attempts"] += 1
                        record = {"theta": str(theta), "rho": str(rho), "nodes": {}, "edges": {}}
                        try:
                            t, r = self.f.rat(theta), self.f.rat(rho)
                            R = 3*C-ell-(1-t)*A-(1-nu)*GH
                            flows = [r*(1-t)*A, t*A, D-t*A, r*R]
                            forces = [-r*(1-t)*A, (1-r)*(1-t)*A, arb(0), (1-r)*R, -r*R]
                            record["R_nu_theta"] = self.f.real_record(R)
                            record["flows"] = [self.f.real_record(q) for q in flows]
                            record["node_forces"] = [self.f.real_record(q) for q in forces]
                            record["selected_force_symbolically_zero"] = True
                            coefficients = [F(3, 2), F(3), F(2+nu), F(2+beta), F(1)+F(beta, 2)]
                            node_zero = [rho == 0 or theta == 1, theta == 1, True, False, rho == 0]
                            edge_zero = [rho == 0 or theta == 1, theta == 0, False, rho == 0]
                            total = arb(0)
                            for j, name in enumerate(("a", "u", "z", "v", "b")):
                                value, component = self.conjugate(forces[j], centers[j], heights[j],
                                    coefficients[j], lows[j], highs[j], zero=node_zero[j])
                                record["nodes"][name] = component
                                total += value
                            for j, name in enumerate(("au", "uz", "zv", "vb")):
                                value, component = self.conjugate(flows[j], centers[j]+centers[j+1],
                                    heights[j]+heights[j+1], F(-1), lows[j]+lows[j+1],
                                    highs[j]+highs[j+1], zero=edge_zero[j], zero_edge=j in (0, 3))
                                record["edges"][name] = component
                                total += value
                            budget = self.finite(T+total, "trial budget")
                            upper = self.f.upper(budget)
                            record.update({"status": "evaluated", "horizontal_gain_bound": self.f.real_record(total),
                                "budget": self.f.real_record(budget), "strictly_below_zero": upper < 0,
                                "strictly_below_candidate_gap": upper < -GAP})
                            self.counts["evaluated_trials"] += 1
                        except self.f.Inconclusive as error:
                            record.update({"status": "inconclusive", "reason": str(error)})
                        branch["trials"].append(record)
                successful = [trial for trial in branch["trials"] if trial["status"] == "evaluated"]
                if successful:
                    best = min(successful, key=lambda trial: F(trial["budget"]["upper_rational"]))
                    branch.update({"best_upper_rational": best["budget"]["upper_rational"],
                        "best_trial": {key: best[key] for key in ("theta", "rho")},
                        "strictly_below_zero": best["strictly_below_zero"],
                        "strictly_below_candidate_gap": best["strictly_below_candidate_gap"]})
                else:
                    branch.update({"best_upper_rational": None, "strictly_below_zero": False,
                                   "strictly_below_candidate_gap": False})
                branches["factorial" if nu else "forced"] = branch
            details["branches"] = branches
            passed = all(branch["strictly_below_candidate_gap"] for branch in branches.values())
            return {"status": "accepted diagnostic" if passed else "inconclusive",
                    "reason": "both branch upper bounds below candidate gap" if passed else "no common candidate-gap certificate on this box",
                    "details": details}
        except self.f.Inconclusive as error:
            return {"status": "inconclusive", "reason": str(error), "details": details}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    bindings, previous = verified_inputs()
    four = importlib.import_module("diagnose_mixed_four_four_half_row_budget")
    accepted = [leaf for leaf in previous["leaves"] if leaf["status"] == "accepted"]
    depth = max(len(leaf["address"]) for leaf in accepted)
    chosen = min((leaf for leaf in accepted if len(leaf["address"]) == depth), key=lambda leaf: leaf["address"])
    if chosen["address"] != ADDRESS or depth != 18:
        raise ValueError("prescribed inherited address mismatch")
    box = four.BASE.ROOT
    if list(map(str, box)) != previous["initial_auxiliary_rectangle"]:
        raise ValueError("original root rectangle mismatch")
    for split_depth, branch in enumerate(ADDRESS):
        box = four.BASE.split(box, split_depth)[int(branch)]
    if box != BOX:
        raise ValueError("exact depth18 box reconstruction failed")

    def forbidden(*args, **kwargs):
        raise RuntimeError("old scalar inspect/main forbidden in this diagnostic")

    for provider in (four, four.frozen, four.maps_four, four.BASE):
        provider.inspect = provider.main = forbidden
    four.reference_four = four.frozen.reference = forbidden
    ctx.prec = 160
    started = time.monotonic()
    primitive = make_primitive_class(four)()
    evaluator = Evaluator(four, primitive)
    results = {str(beta): evaluator.inspect(box, beta) for beta in (0, 1)}
    if evaluator.counts["reference_calls"] != 2 or evaluator.counts["trial_attempts"] > 60:
        raise RuntimeError("bounded diagnostic call count violated")
    for name, expected in bindings.items():
        if digest(REPO/name) != expected:
            raise RuntimeError("input changed during diagnostic: "+name)
    record = {
        "status": "diagnostic complete", "scope": "second-selection central scalar dual on one inherited alpha1 box only",
        "actual_word_realization_claimed": False, "uniform_sign_claimed": False,
        "alpha": 1, "beta_candidates": [0, 1], "precision_bits": 160, "height": str(H), "candidate_gap": str(GAP),
        "tested_address": ADDRESS, "tested_box": list(map(str, BOX)), "inherited_leaf": chosen,
        "selection": "lexicographically first accepted leaf of maximal accepted depth; saved metadata only",
        "flows": {"theta": list(map(str, THETAS)), "rho": list(map(str, RHOS))},
        "results_by_beta": results, "call_counts": dict(evaluator.counts+primitive.counts),
        "tested_boxes": 1, "subdivisions": 0, "automatic_retries": 0, "alternate_boxes": 0,
        "old_inspect_calls": 0, "root_proposals": 0, "finite_source_evaluations": 0,
        "elapsed_seconds": time.monotonic()-started, "input_sha256": bindings,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as output:
        output.write(json.dumps(record, indent=2)+"\n")
    print(json.dumps({"status": record["status"], "result_sha256": digest(args.output),
        "elapsed_seconds": record["elapsed_seconds"], "call_counts": record["call_counts"],
        "results": {beta: {"status": value["status"], "reason": value["reason"],
            "best_upper_rationals": {label: branch["best_upper_rational"]
                for label, branch in value["details"].get("branches", {}).items()}}
            for beta, value in results.items()}}), flush=True)


if __name__ == "__main__":
    main()
