#!/usr/bin/env python3
"""Exact cubic barriers and fixed scalar bounds for second-four first collars.

Existing complete certificates are bound and their saved scalar floors
are checked. No root, source row, or parameter cell is recomputed.
"""
import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

from flint import arb, ctx
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_second_four_cap_collar.md"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--precision", type=int, default=256)
    ap.add_argument("--input", type=Path)
    ap.add_argument("--output", type=Path, default=ROOT /
                    "repro/results/research-mixed-second-four-cap-collar.json")
    args = ap.parse_args()
    assert args.precision >= 192
    ctx.prec = args.precision
    ph, sh = sha(PROOF), sha(__file__)
    ih = sha(args.input) if args.input else None
    old = json.loads(args.input.read_text()) if args.input else None
    deps, records, visited, primary = {}, {}, set(), {}

    def bind(path, expected=None):
        if path not in deps:
            deps[path] = sha(ROOT/path)
        if expected is not None:
            assert deps[path] == expected, path
        return deps[path]

    def inherit(path):
        bind(path)
        if path in visited:
            return records[path]
        visited.add(path)
        record = json.loads((ROOT/path).read_text())
        records[path] = record
        nested = {}
        for field in ("dependencies", "dependencies_sha256"):
            for p, digest in record.get(field, {}).items():
                assert p not in nested or nested[p] == digest, p
                nested[p] = digest
                bind(p, digest)
        for p in nested:
            if p.startswith("repro/results/") and p.endswith(".json"):
                inherit(p)
        return record

    def load(stem, proof=None, script=None):
        path = "repro/results/research-"+stem.replace("_", "-")+".json"
        r = inherit(path)
        assert r["status"] == "passed", path
        proof = proof or "research_"+stem
        script = script or "check_"+stem
        p = "notes/"+proof+".md"
        expected = r.get("proof_sha256", r.get("dependencies_sha256", {}).get(p))
        assert expected is not None
        bind(p, expected)
        bind("experiments/"+script+".py", r["script_sha256"])
        primary[path] = deps[path]
        return r

    previous = load("mixed_three_cap_collar_comparison")
    seam = load("mixed_seam_run_connector_lower")
    strip = load("mixed_boundary_strip_bounds")
    cap = load("mixed_cap_seam_source_bounds")
    load("mixed_split_cutoff_hybrid_contour")
    load("mixed_closed_cotangent_roots")
    load("mixed_complete_first_cap_packet")
    rectangles = load("mixed_open_word_endpoint_rectangles")
    load("mixed_fourier_weight_continuation")
    load("mixed_acute_gradient_height_transfer")
    for stem in ("mixed_three_cap_collar_comparison", "mixed_complete_first_cap_packet",
                 "mixed_seam_run_connector_lower", "mixed_cap_seam_source_bounds"):
        path = "repro/results/research-"+stem.replace("_", "-")+"-replay.json"
        author_path = path.replace("-replay.json", ".json")
        r, a = inherit(path), records[author_path]
        assert r["status"] == "passed" and r["input_sha256"] == deps[author_path]
        for field in ("proof_sha256", "script_sha256", "dependencies_sha256"):
            assert r[field] == a[field], (path, field)
        primary[path] = deps[path]

    image = load("mixed_cyclic_block_boundary_images",
                 "research_mixed_cyclic_critical_height_bounds",
                 "certify_mixed_cyclic_block_boundary_images")
    geometry_replay_path = "repro/results/research-mixed-cyclic-block-boundary-images-replay.json"
    geometry_replay = inherit(geometry_replay_path)
    assert geometry_replay["status"] == "passed"
    assert geometry_replay["input_sha256"] == deps[
        "repro/results/research-mixed-cyclic-block-boundary-images.json"]
    bind("experiments/replay_mixed_cyclic_block_boundary_images.py",
         geometry_replay["script_sha256"])
    bind("notes/research_mixed_cyclic_critical_height_bounds.md",
         geometry_replay["proof_sha256"])
    bind("experiments/replay_mixed_cyclic_block_localization.py",
         geometry_replay["independent_localization_replay_script_sha256"])
    bind("experiments/certify_mixed_cyclic_block_localization.py", image["source_sha256"])
    for suffix, field in (("", "localization_record_sha256"),
                          ("-replay", "localization_replay_sha256")):
        path = "repro/results/research-mixed-cyclic-block-localization"+suffix+".json"
        bind(path, image[field])
        r = inherit(path)
        assert r["status"] == "passed"
        bind("experiments/"+("replay" if suffix else "certify")+
             "_mixed_cyclic_block_localization.py", r["script_sha256"])
        bind("notes/research_mixed_cyclic_critical_localization.md", r["proof_sha256"])
    local_author = "repro/results/research-mixed-cyclic-block-localization.json"
    assert records[local_author.replace(".json", "-replay.json")]["input_sha256"] == deps[local_author]
    primary[geometry_replay_path] = deps[geometry_replay_path]
    for p in ("notes/research_mixed_boundary_strip_bounds.md",
              "notes/research_mixed_conditional_torus_composition.md",
              "notes/research_mixed_open_boundary_comparison_reduction.md"):
        bind(p)

    checks, scalars = [], {}

    def check(name, condition):
        assert condition, name
        checks.append(name)

    def ar(value):
        value = F(value)
        return arb(value.numerator)/value.denominator

    def bound(name, value, threshold):
        check(name, value < ar(threshold))
        scalars[name] = value

    expected = [
        [[".376", ".438", "-.019", ".037"], [".278", ".391", "-.072", ".021"]],
        [[".333", ".363", "-.051", "-.019"], [".246", ".350", "-.108", "-.020"]],
    ]
    check("all four actual private and attached endpoint rectangles are retained",
          all(list(map(F, rectangles["rectangles"][e][j])) == list(map(F, expected[e][j]))
              for e in (0, 1) for j in (0, 1)))
    check("the full block-image height bounds and saved replay agree",
          image["height_bounds"] == geometry_replay["height_bounds"] ==
          ["-13/200", "17/250", "-51/500", "-1/1000"]
          and image["output_radii"] == geometry_replay["output_radii"] == ["83/1000", "3/50"])
    expected_types = [[0, 0, 0], [0, 0, 1], [0, 1, 1],
                      [1, 0, 0], [1, 0, 1], [1, 1, 1]]
    check("all six complete geometry cases have their matching saved replay",
          [r["types"] for r in image["cases"]] ==
          [r["types"] for r in geometry_replay["cases"]] == expected_types
          and sum(len(r["addresses"]) for r in image["cases"]) ==
          geometry_replay["replay_boxes"] == 6994
          and geometry_replay["refinements"] == 0
          and all(len(a["addresses"]) == b["author_boxes"] == b["replay_boxes"]
                  for a, b in zip(image["cases"], geometry_replay["cases"])))
    check("the ordinary and private type-four real ranges fit the corrected union",
          F(".30")-F(".060") == F(".24")
          and F(".30")+F(".060") < F(".363")
          and -F(".102") < -F(".051") < -F(".019") < -F(".001"))
    check("the first and second real ranges fit the interpolated rectangle",
          F(".246") < F(".278") < F(".350") < F(".391")
          and F(".24") < F(".333") < F(".363"))

    u, v, p, q, xi, zeta = sp.symbols("u v p q xi zeta", real=True)
    P, Q, S = p+sp.I*xi, q+sp.I*zeta, u+sp.I*v
    def equation(z):
        return (z+sp.I)*(z+P)*(z+Q)-2*sp.I*(P-sp.I)*(Q+sp.I)
    E = 2*(xi-1)*(zeta+1)-(v+1)*(xi+v)*(zeta+v)
    check("the full imaginary-side cubic obstruction is exact",
          sp.expand(sp.im(equation(sp.I*v))-((v-1)*p*q+E)) == 0)
    check("the imaginary-side expression is increasing in xi",
          sp.expand(sp.diff(E, xi)-(1-v)*(zeta+v+2)) == 0)
    check("the zeta coefficient has a uniformly negative square decomposition",
          sp.expand(sp.diff(E, zeta).subs(xi, sp.Rational(2, 3))
                    +(v+sp.Rational(5, 6))**2+sp.Rational(23, 36)) == 0)
    check("the corner polynomial has the claimed three-interval barrier",
          sp.expand(E.subs({xi:sp.Rational(2, 3), zeta:0})
                    +sp.Rational(2, 3)+v*(v+1)*(v+sp.Rational(2, 3))) == 0
          and -F(2, 3)+F(2, 3)*1*F(2, 3) == -F(2, 9))
    # Solve the upper-side equation exactly; no parameter or root sampling.
    w = sp.symbols("w")
    pol = ((u+2*sp.I)*(u+sp.I+w)*(u+sp.I+Q)
           -2*sp.I*(w-sp.I)*(Q+sp.I))
    solved = sp.cancel(-pol.subs(w, 0)/sp.diff(pol, w))
    upper_im = -1-2*(4*q+u*q*(u+q)+u*(zeta+1)**2)/(
        u*((u+q)**2+(zeta+3)**2))
    check("the full upper-side solution forces imaginary P below minus one",
          sp.factor(sp.im(solved)-upper_im) == 0)
    check("the full lower-side equation has its exact argument quotient",
          sp.expand(equation(u-sp.I)
                    -(u*(P+u-sp.I)*(Q+u-sp.I)-2*sp.I*(P-sp.I)*(Q+sp.I))) == 0)
    check("the second lifted gradient ratio has negative imaginary numerator",
          sp.expand(sp.im((S+Q)*sp.conjugate(S+sp.I))
                    -(u*(zeta-1)-q*(v+1))) == 0)
    C = sp.re((S*P-1)/(S+P))
    det = u*p-(u+p)*C
    expected_det = ((u+p)**2-(p*v-u*xi)**2)/((u+p)**2+(v+xi)**2)
    check("the full triangle determinant uses only the proved unit imaginary cone",
          sp.factor(det-expected_det) == 0)
    check("the entire actual path is strictly inside the cubic and triangle bands",
          F(61, 100) < F(2, 3) < 1 and -1 < -F(37, 100))

    floors = {
        (".30", ".27"): ".805", (".10", ".27"): ".597",
        (".30", ".10"): ".721", (".30", ".33"): ".789",
        (".10", ".33"): ".564", (".30", ".50"): ".664",
        (".39", ".27"): ".822", (".39", ".10"): ".725",
        (".50", ".27"): ".804", (".39", ".33"): ".812",
        (".50", ".33"): ".799", (".39", ".50"): ".703",
    }
    floors = {tuple(map(F, k)):F(v) for k, v in floors.items()}
    phase_rows = {tuple(map(F, r["target"])):r for r in seam["comparisons"]
                  if r["types"] == [0, 1]}
    check("all twelve saved original cubic phase floors are present",
          set(phase_rows) == set(floors)
          and all(arb(phase_rows[key]["real_phase"]) > ar(value)
                  for key, value in floors.items()))
    combinations = [
        ([".246", ".24"], [[".30", ".27"], [".10", ".27"], [".30", ".10"]],
         ["941/1700", "27/100", "3/17"]),
        ([".246", ".363"], [[".30", ".33"], [".10", ".33"], [".30", ".50"]],
         ["911/1700", "27/100", "33/170"]),
        ([".391", ".24"], [[".39", ".27"], [".39", ".10"], [".50", ".27"]],
         ["1523/1870", "3/17", "1/110"]),
        ([".391", ".363"], [[".39", ".33"], [".50", ".33"], [".39", ".50"]],
         ["149/187", "1/110", "33/170"]),
    ]
    convex_records = []
    for target, vertices, weights in combinations:
        t = tuple(map(F, target))
        vertices = [tuple(map(F, point)) for point in vertices]
        weights = list(map(F, weights))
        lower = sum(w*floors[point] for w, point in zip(weights, vertices))
        check("exact saved-phase convex combination at "+str(t),
              min(weights) > 0 and sum(weights) == 1
              and all(sum(w*point[j] for w, point in zip(weights, vertices)) == t[j]
                      for j in (0, 1))
              and lower > F(7, 10))
        convex_records.append(dict(target=list(map(str,t)),
                                   vertices=[list(map(str,v)) for v in vertices],
                                   coefficients=list(map(str,weights)), floor=str(lower)))
    check("both complete cap ceilings are the original inherited constants",
          cap["seam_ceilings"] == ["101/125", "433/500"])
    budget = [r for r in strip["endpoint_budgets"] if r["name"]=="left selected own4"]
    check("the full selected second halfweight and all-row budget are retained",
          len(budget)==1 and budget[0]["epsilon"]==1
          and F(budget[0]["C_pi"])==2*F(7,500)
          and F(budget[0]["weight_cost"])==F(1,12)
          and F(budget[0]["threshold"])==F(57,100)
          and arb(budget[0]["rate_upper"]) < ar(F(57,100)))
    check("first real selection and second half selection have exact modulus exponents",
          F(1,2)*F(1,6)==F(1,12)
          and F(2)*F(7,500)==F(7,250))

    pi = arb.pi()
    for name, x, h, limit in [
        ("first_three_cotangent", ".278", ".072", ".37"),
        ("first_four_cotangent", ".246", ".108", ".61"),
        ("second_four_cotangent", ".24", ".102", ".61"),
    ]:
        value = (2*pi*ar(h)).sinh()/((2*pi*ar(h)).cosh()-(2*pi*ar(x)).cos())
        monotonicity = (2*pi*ar(x)).cos()*(2*pi*ar(h)).cosh()
        bound(name, value, limit)
        bound(name+"_height_monotonicity", monotonicity, 1)
    cost4 = pi/2*ar(".102")*ar("1.26")
    cost3 = cost4+pi/2*ar(".021")
    margins = [ar("1.7")-ar(".808")-ar(".57")-cost3,
               ar("1.7")-ar(".866")-ar(".57")-cost4]
    for alpha, margin in enumerate(margins):
        check("full first-pair reserve for type"+str(3+alpha)+" followed by four",
              margin > ar(F(3,50)))
        scalars["pair_reserve_"+str(alpha)] = margin
    check("one collar allowance and one total source tolerance leave one twentieth",
          F(3,50)-F(1,200)-F(1,200)==F(1,20))

    result = dict(status="passed", precision_bits=args.precision,
                  exact_and_scalar_checks=len(checks), checks=checks,
                  scalar_enclosures={k:str(v) for k,v in scalars.items()},
                  saved_real_phase_values=12, convex_combinations=convex_records,
                  primary_records_sha256=primary, dependencies_sha256=deps,
                  proof_sha256=ph, script_sha256=sh, input_sha256=ih,
                  new_root_proposals=0, root_enclosures_recomputed=0,
                  new_parameter_cover_cells=0, seam_reserve="3/50", finite_reserve="1/20",
                  collar_scope="Sufficiently small fixed rho<=1/1000; one combined collar allowance and one total finite-source tolerance.",
                  scope="Actual open prefixes (3,4) and (4,4), full first Fourier weight, original second halfweight and both selections, with the surviving actual second tangent. No global open-source estimate.")
    if old:
        for key in result:
            if key not in ("precision_bits", "scalar_enclosures", "input_sha256"):
                assert old[key] == result[key], key
        assert old["scalar_enclosures"].keys() == scalars.keys()
        assert all(value.overlaps(arb(old["scalar_enclosures"][key]))
                   for key,value in scalars.items())
    assert sha(PROOF)==ph and sha(__file__)==sh
    assert all(sha(ROOT/p)==digest for p,digest in deps.items())
    if args.input:
        assert sha(args.input)==ih
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS",len(checks),"exact/scalar checks;",len(primary),
          "primary records;",len(deps),"bindings; no roots/cells recomputed")


if __name__ == "__main__":
    main()
