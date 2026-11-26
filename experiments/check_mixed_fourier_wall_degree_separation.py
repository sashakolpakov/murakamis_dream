#!/usr/bin/env python3
"""Fixed rational Wall degree certificate. No analytic evaluator is imported."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import comb
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "repro/results/research-mixed-fourier-boundary-update.json"
WRITER = "experiments/check_mixed_fourier_boundary_update.py"
ORIGINAL = "repro/results/research-three-four-source-interface.json"
ORIGINAL_WRITER = "experiments/check_three_four_source_interface.py"
PROTOCOL = "notes/research_mixed_fourier_wall_degree_separation_protocol.md"
THEORY = "notes/research_mixed_fourier_right_cap_wall_endpoint_strip.md"
OUTPUT = ROOT / "repro/results/research-mixed-fourier-wall-degree-separation.json"
PINS = {
    SOURCE: "5d4cb057cb82ca4fff826ad768012480fd6f51afe66d3f5c632e48983cf17514",
    WRITER: "5017a53b6417630f1cab1e9c4be3f71d3ad24256af1ca67a8edd8faf0be0b1cc",
    ORIGINAL: "9218011f3f5d41ff15835f74ccf83ccfeb266beea112c67607fa1eaef96ba9dd",
    ORIGINAL_WRITER: "e9d009fdf8712a7577bd9220c8bbf6c2f8fd1d3eefece969cad45357d8a45f91",
    PROTOCOL: "e962441bf71b0d0d92cb24862280ee80823af8a1e87ed2d3ba3c4ce91ce99ac4",
    THEORY: "f1883a55225ebaa85d1f11f149de1ab89a5a94d1bf86f991f9cea53e00385e18",
    "notes/research_mixed_fourier_right_cap_wall_operator.md":
        "f430ee21130e9f39a100bd7a8dd167e17f6b4cd4c32e8a1525425c5fa339eac8",
}
K_CANONICAL = "00f030c9a079403c2811e9b1c0dcca898ca8d912f4c11c0e338b3cc655a89591"
ROOT_CANONICAL = "f04e925c094ba2f2c6723d3321cb58ac4988255b52e3408c2895b662bcf1cf8f"
DEGREE, CELLS = 8, 64
EXPECTED = dict(charts=2, cells=128, bernstein_intervals=1152)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(1048576), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                      allow_nan=False).encode()).hexdigest()


def point(value):
    value = F(value)
    return value, value


ZERO, ONE = point(0), point(1)


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def neg(a):
    return -a[1], -a[0]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    products = (a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1])
    return min(products), max(products)


def scale(a, value):
    return mul(a, point(value))


def saved_interval(value):
    require(value["finite"] is True, "nonfinite saved interval")
    lo, hi = F(value["lower_rational"]), F(value["upper_rational"])
    require(lo <= hi, "reversed saved interval")
    return lo, hi


def encode(a):
    require(a[0] <= a[1], "reversed constructed interval")
    return [str(a[0]), str(a[1])]


# Increasing powers of the same exact chart variable; never box-evaluated.
def padd(a, b):
    return [add(a[i] if i < len(a) else ZERO,
                b[i] if i < len(b) else ZERO)
            for i in range(max(len(a), len(b)))]


def pscale(a, coefficient):
    return [mul(value, coefficient) for value in a]


def psub(a, b):
    return padd(a, [neg(value) for value in b])


def pmul(a, b):
    out = [ZERO for _ in range(len(a) + len(b) - 1)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i+j] = add(out[i+j], mul(ai, bj))
    return out


def pencode(poly):
    return [encode(value) for value in poly]


def construct(chart, p, v, k, u):
    require(chart in (0, 1), "chart index")
    denominator = [ONE, ZERO, ONE]
    if chart == 0:
        cnum, snum = [ONE, ZERO, point(-1)], [ZERO, point(2)]
    else:
        cnum, snum = [ZERO, point(-2)], [ONE, ZERO, point(-1)]
    d2 = pmul(denominator, denominator)
    cd, sd = pmul(cnum, denominator), pmul(snum, denominator)
    base = pscale(d2, sub(ONE, k))
    h = psub(padd(base, pscale(cd, scale(u, 2))), pscale(sd, scale(v, 2)))
    e = psub(padd(base, pscale(cd, scale(u, 3))), pscale(sd, v))
    f = psub(padd(pscale(cd, v), pscale(sd, add(p, k))),
             pscale(pmul(cnum, snum), scale(k, 4)))
    require(all(len(poly) <= 5 for poly in (h, e, f)), "degree-four inventory")
    qnum = psub(padd(pmul(e, e), pmul(f, f)), pmul(h, h))
    require(len(qnum) <= DEGREE + 1, "degree-eight inventory")
    qnum += [ZERO] * (DEGREE + 1 - len(qnum))
    return dict(d=denominator, cnum=cnum, snum=snum, H=h, E=e, F=f, Qnum=qnum)


def bernstein(poly, cell):
    require(len(poly) == DEGREE + 1 and 0 <= cell < CELLS, "Bernstein input")
    left, width = F(cell, CELLS), F(1, CELLS)
    shifted = [ZERO for _ in range(DEGREE + 1)]
    # x=left+width*t, with the exact 0**0=1 convention.
    for power in range(DEGREE + 1):
        for degree in range(power + 1):
            weight = comb(power, degree) * left**(power-degree) * width**degree
            shifted[degree] = add(shifted[degree], scale(poly[power], weight))
    coefficients = []
    for degree in range(DEGREE + 1):
        value = ZERO
        for power in range(degree + 1):
            weight = F(comb(degree, power), comb(DEGREE, power))
            value = add(value, scale(shifted[power], weight))
        coefficients.append(value)
    return shifted, coefficients


def clear_claims(result):
    result["degree_root_separation_certified"] = False
    result["uniform_ratio_contraction_certified"] = False
    result["certified_Q_lower_rational"] = None


def run(result, script_sha):
    inputs = result["input_sha256"]

    def bind(name, expected):
        require(isinstance(name, str) and not Path(name).is_absolute() and
                (ROOT/name).resolve().is_relative_to(ROOT) and
                (ROOT/name).resolve() != OUTPUT.resolve(), "invalid input path")
        require(isinstance(expected, str) and len(expected) == 64 and
                all(c in "0123456789abcdef" for c in expected), "invalid input pin")
        if name in inputs:
            require(inputs[name] == expected, "conflicting input pin: " + name)
        actual = sha(ROOT/name)
        result["binding_checks"].append(dict(path=name, expected=expected, actual=actual,
                                              passed=actual == expected))
        require(actual == expected, "input changed: " + name)
        inputs[name] = actual

    for name, expected in PINS.items():
        bind(name, expected)
    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    bind(own, script_sha)
    result.update(script_path=own, script_sha256=script_sha, protocol_path=PROTOCOL,
                  protocol_sha256=PINS[PROTOCOL], initialized_theory_path=THEORY)
    source = json.loads((ROOT/SOURCE).read_text())
    require(source["status"] == "passed" and source["inclusion_certified"] is True and
            source["all_inputs_unchanged"] is True and
            source["full_analytic_inventory_completed"] is True, "incomplete original source")
    require(source["script_path"] == WRITER and source["script_sha256"] == inputs[WRITER],
            "original writer association")
    before = source["input_sha256"]
    require(before == source["input_sha256_after"] and
            len(before) == source["input_binding_count"] == 20, "old before/after bindings")
    for name, expected in before.items():
        bind(name, expected)
    require(source["visited_arcs"] == source["passed_arcs"] == 512 and
            source["failed_arcs"] == source["inconclusive_arcs"] == 0, "old arc inventory")
    require(len(source["arcs"]) == 512 and
            [arc["index"] for arc in source["arcs"]] == list(range(512)) and
            all(arc["status"] == "passed" for arc in source["arcs"]), "old arc associations")
    radius_summary = source["maximum_squared_distance"]
    radius_upper = F(radius_summary["upper_rational"])
    worst_arc = radius_summary["arc"]
    require(type(worst_arc) is int and 0 <= worst_arc < 512 and
            radius_upper == F(source["arcs"][worst_arc][
                "conservative_squared_distance_upper_rational"]) and
            0 <= radius_upper < F(41, 500)**2, "old inclusion radius association")
    original = json.loads((ROOT/ORIGINAL).read_text())
    require(original["status"] == "passed" and
            original["script_sha256"] == inputs[ORIGINAL_WRITER], "original reference status")
    for name, expected in original["dependencies_sha256"].items():
        bind(name, expected)
    reference = source["reference"]
    require(reference["path"] == ORIGINAL and reference["sha256"] == inputs[ORIGINAL] and
            reference["writer_path"] == ORIGINAL_WRITER and
            reference["writer_sha256"] == inputs[ORIGINAL_WRITER] and
            reference["original_success_and_associations_verified"] is True,
            "boundary-to-reference association")
    certificate = original["root_certificate"]
    require(canonical(certificate) == ROOT_CANONICAL ==
            reference["root_certificate_canonical_sha256"], "full original root identity")
    center = list(map(F, certificate["center"]))
    radius = F(certificate["complex_disk_radius"])
    require(len(center) == 2 and radius > 0 and
            center == list(map(F, reference["center_rational"])) and
            radius == F(reference["radius_rational"]), "original center/radius")
    square = [[c-radius, c+radius] for c in center]
    require(square == [list(map(F, row)) for row in reference["full_square_rational"]],
            "original full square")
    constants = source["constants"]
    require(constants["K_formula"] == "1/(1+2*a-4*a*a)" and
            constants["K_denominator_nonzero"] is True, "original K formula")
    for axis, part in enumerate(("real", "imag")):
        outer = saved_interval(constants["full_original_root_square"][part])
        require(outer[0] <= square[axis][0] <= square[axis][1] <= outer[1],
                "full-square containment")
    require(canonical(constants["K"]) == K_CANONICAL, "full K box identity")
    p = saved_interval(constants["K"]["real"])
    v = saved_interval(constants["K"]["imag"])
    k = add(mul(p, p), mul(v, v))
    u = sub(k, p)
    result["source"] = dict(path=SOURCE, sha256=inputs[SOURCE], writer_sha256=inputs[WRITER],
                           K=constants["K"], K_canonical_sha256=K_CANONICAL,
                           K_formula=constants["K_formula"], reference=reference,
                           root_certificate_canonical_sha256=ROOT_CANONICAL,
                           analytic_enclosures_inherited=True,
                           full_original_root_square_rational=[
                               [str(value) for value in row] for row in square],
                           original_arc_count=512, original_binding_count=20)
    result["scalar_intervals"] = dict(p=encode(p), v=encode(v), k=encode(k), u=encode(u))
    tests = (
        ("nonzero_Y", k, "lower_positive", k[0] > 0),
        ("unit_disk_Y", k, "upper_below_one", k[1] < 1),
        ("upper_halfplane_Y", v, "lower_positive", v[0] > 0),
        ("initial_exterior_root", sub(scale(k, 3), scale(p, 2)),
         "lower_positive", sub(scale(k, 3), scale(p, 2))[0] > 0),
    )
    for name, interval, condition, passed in tests:
        result["elementary_checks"].append(dict(name=name, interval=encode(interval),
                                                 condition=condition, passed=passed))
    require(all(row["passed"] for row in result["elementary_checks"]), "elementary input bounds")
    minimum = None
    for chart_index in range(2):
        chart = dict(index=chart_index, parameter_rational=["0", "1"],
                     cells=[], status="initializing")
        result["charts"].append(chart)
        polynomials = construct(chart_index, p, v, k, u)
        chart["power_polynomials"] = {name: pencode(poly) for name, poly in polynomials.items()}
        result["counts"]["charts"] += 1
        for cell_index in range(CELLS):
            cell = dict(index=cell_index, parameter_rational=[
                str(F(cell_index, CELLS)), str(F(cell_index+1, CELLS))], status="initializing")
            chart["cells"].append(cell)
            result["active_cell"] = [chart_index, cell_index]
            shifted, coefficients = bernstein(polynomials["Qnum"], cell_index)
            cell["substituted_power_intervals"] = pencode(shifted)
            cell["bernstein_intervals"] = pencode(coefficients)
            cell["coefficient_lower_positive"] = [value[0] > 0 for value in coefficients]
            lower = min(value[0] for value in coefficients)
            cell["lower_rational"] = str(lower)
            cell["status"] = "passed" if all(cell["coefficient_lower_positive"]) else "inconclusive"
            if cell["status"] != "passed":
                result["inconclusive_cells"].append([chart_index, cell_index])
            minimum = lower if minimum is None else min(minimum, lower)
            result["minimum_recorded_lower_rational"] = str(minimum)
            result["counts"]["cells"] += 1
            result["counts"]["bernstein_intervals"] += len(coefficients)
        chart["status"] = ("passed" if all(c["status"] == "passed" for c in chart["cells"])
                           else "inconclusive")
    result["active_cell"] = None
    require(result["counts"] == EXPECTED, "fixed inventory incomplete")
    result["all_cells_passed"] = not result["inconclusive_cells"]
    result["candidate_Q_lower_rational"] = str(minimum / 16)
    result["status"] = "pending_final_bindings"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--script-sha", required=True)
    args = parser.parse_args()
    require(len(args.script_sha) == 64 and
            all(c in "0123456789abcdef" for c in args.script_sha), "invalid frozen script pin")
    require(sha(__file__) == args.script_sha, "frozen script mismatch")
    result = dict(schema="fourier-wall-degree-separation-v1", status="initializing",
                  input_sha256={}, input_sha256_after={}, binding_checks=[],
                  charts=[], counts={name: 0 for name in EXPECTED}, expected_counts=EXPECTED,
                  elementary_checks=[], inconclusive_cells=[], errors=[], active_cell=None,
                  degree=DEGREE, cells_per_chart=CELLS, all_cells_passed=False,
                  interval_encoding="[lower_rational,upper_rational]",
                  polynomial_order="increasing powers; Bernstein indices 0 through 8",
                  minimum_recorded_lower_rational=None, candidate_Q_lower_rational=None,
                  analytic_evaluations=0, quantum_source_evaluations=0, root_solves=0,
                  gain_optimizations=0, source_replays=0, proposals=0, refinements=0, retries=0,
                  scope="Only the two degree roots are separated across the unit circle, "
                        "on t in [0,1/2] and the full saved Y box. No quantum-source "
                        "asymptotic or geometric-rate comparison is certified here.")
    clear_claims(result)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("x", encoding="utf-8") as handle:
        try:
            run(result, args.script_sha)
        except BaseException as error:
            result["errors"].append(type(error).__name__ + ": " + str(error))
            result["status"] = "calculation_failure"
        finally:
            for name, before in result["input_sha256"].items():
                try:
                    after = sha(ROOT/name)
                    result["input_sha256_after"][name] = after
                    require(after == before, "changed input: " + name)
                except BaseException as error:
                    result["errors"].append(type(error).__name__ + ": " + str(error))
                    result["status"] = "calculation_failure"
            result["input_binding_count"] = len(result["input_sha256"])
            result["all_inputs_unchanged"] = (
                result["input_sha256"] == result["input_sha256_after"])
            if result["status"] == "pending_final_bindings" and not result["errors"]:
                result["status"] = "passed" if result["all_cells_passed"] else "inconclusive"
                if result["status"] == "passed":
                    result["degree_root_separation_certified"] = True
                    result["uniform_ratio_contraction_certified"] = True
                    result["certified_Q_lower_rational"] = result["candidate_Q_lower_rational"]
            if result["status"] != "passed":
                clear_claims(result)
            json.dump(result, handle, sort_keys=True, indent=2, allow_nan=False)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
    print(json.dumps(dict(status=result["status"], counts=result["counts"],
                          inconclusive_cells=len(result["inconclusive_cells"]),
                          input_binding_count=result["input_binding_count"],
                          output=str(OUTPUT), errors=result["errors"]), sort_keys=True))
    return 0 if result["status"] == "passed" else 1


if __name__ == "__main__":
    sys.exit(main())
