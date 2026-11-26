#!/usr/bin/env python3
"""Exact barriers and fixed scalar bounds for the (4,3) first collar.

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
PROOF = ROOT / "notes/research_mixed_four_three_cap_collar.md"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--precision", type=int, default=256)
    ap.add_argument("--input", type=Path)
    ap.add_argument("--output", type=Path, default=ROOT /
                    "repro/results/research-mixed-four-three-cap-collar.json")
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
    load("mixed_complete_first_cap_packet")
    rectangles = load("mixed_open_word_endpoint_rectangles")
    load("mixed_fourier_weight_continuation")
    load("mixed_acute_gradient_height_transfer")
    for stem in ("mixed_three_cap_collar_comparison", "mixed_complete_first_cap_packet"):
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
              "notes/research_mixed_conditional_torus_composition.md"):
        bind(p)

    checks, scalars = [], {}

    def check(name, condition):
        assert condition, name
        checks.append(name)

    check("the actual attached four and private three boxes are retained",
          list(map(F, rectangles["rectangles"][1][1])) ==
          list(map(F, [".246", ".350", "-.108", "-.020"]))
          and list(map(F, rectangles["rectangles"][0][0])) ==
          list(map(F, [".376", ".438", "-.019", ".037"])))
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
    check("the ordinary and private type-three ranges fit the stated union",
          F(".35")-F(".083") == F(".267")
          and F(".35")+F(".083") < F(".438")
          and -F(".065") < -F(".019") < F(".037") < F(".068"))

    u, v, p, q, alpha, beta = sp.symbols("u v p q alpha beta", real=True)
    P, Q = p+sp.I*alpha, q+sp.I*beta
    def equation(S):
        return S*S+(P+Q)*S-1+sp.I*(Q-P)
    check("the imaginary-axis equation fixes v",
          sp.expand(sp.im(equation(sp.I*v))-((p+q)*v+q-p)) == 0)
    check("the imaginary-axis real obstruction has its exact sign form",
          sp.expand(sp.re(equation(sp.I*v))-
                    (-1-v*v+(1-v)*alpha-(1+v)*beta)) == 0)
    check("the entire upper strip side is excluded",
          sp.expand(sp.im(equation(u+sp.I))-(u*(2+alpha+beta)+2*q)) == 0)
    check("the entire lower strip side is excluded",
          sp.expand(sp.im(equation(u-sp.I))-(u*(-2+alpha+beta)-2*p)) == 0)
    check("the first ratio has positive imaginary numerator",
          sp.expand(sp.im((u+sp.I*v+P)*sp.conjugate(u+sp.I*v-sp.I))-
                    (u*(1+alpha)+p*(1-v))) == 0)
    check("the second ratio has negative imaginary numerator",
          sp.expand(sp.im((u+sp.I*v+Q)*sp.conjugate(u+sp.I*v+sp.I))-
                    (u*(beta-1)-q*(v+1))) == 0)
    A, B = F(61, 100), F(37, 100)
    check("the asymmetric cotangent bands exclude every axis crossing",
          A+B+(A-B)**2/4 == F(1243, 1250) < 1 and A+B < 1)
    vertices = [(F(a), F(b)) for a, b in
                [(".1", ".3"), (".1", ".39"), (".39", ".5"),
                 (".5", ".39"), (".39", ".1"), (".3", ".1")]]
    def cross(a, b, c):
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    check("the enlarged actual real rectangle lies inside the saved hexagon",
          all(cross(vertices[j], vertices[(j+1) % 6], c) < 0
              for j in range(6) for c in itertools.product(
                  map(F, [".246", ".350"]), map(F, [".267", ".438"]))))
    check("all six inherited original phase floors and both M0 ceilings are retained",
          previous["saved_root_disks"] == 6
          and [(F(r["a"]), F(r["b"])) for r in previous["roots"]] == vertices
          and all(arb(previous["scalar_enclosures"]["f_"+str(a)+"_"+str(b)]) > arb(".44")
                  for a, b in vertices)
          and arb(previous["scalar_enclosures"]["row_maximum_zero"]) < arb(".326")
          and arb(previous["scalar_enclosures"]["row_maximum_positive"]) < arb(".526"))

    pi = arb.pi()
    cot4 = (arb(".216")*pi).sinh()/(
        (arb(".216")*pi).cosh()-(arb(".492")*pi).cos())
    cot3 = (arb(".136")*pi).sinh()/(
        (arb(".136")*pi).cosh()-(arb(".534")*pi).cos())
    monotone = (arb(".492")*pi).cos()*(arb(".216")*pi).cosh()
    check("the entire first four-height segment has cotangent imaginary part below .61",
          cot4 < arb(".61") and monotone < 1)
    check("the entire type-three range has cotangent imaginary modulus below .37",
          cot3 < arb(".37"))
    check("both attenuation endpoints have the common source budget",
          F(".0325") < F(".068")
          and arb(".526") < arb(".326")+arb(".068")*pi)
    reserve = arb("1.44")-arb(".866")-arb(".326")-arb(".068")*pi
    check("the seam reserve exceeds seventeen five-hundredths", reserve > arb(".034"))
    check("one first-weight and two product collars plus one tolerance leave one fiftieth",
          F(17, 500)-F(1, 100)-F(1, 250) == F(1, 50))
    scalars.update(cotangent_four_maximum=cot4, cotangent_three_maximum=cot3,
                   height_monotonicity_product=monotone, seam_reserve=reserve)
    result = dict(status="passed", precision_bits=args.precision,
                  exact_and_scalar_checks=len(checks), checks=checks,
                  scalar_enclosures={k: str(v) for k, v in scalars.items()},
                  primary_records_sha256=primary, dependencies_sha256=deps,
                  proof_sha256=ph, script_sha256=sh, input_sha256=ih,
                  new_root_proposals=0, root_enclosures_recomputed=0,
                  new_parameter_cover_cells=0,
                  seam_reserve="17/500", finite_reserve="1/50",
                  collar_scope="A sufficiently small fixed rho <= 1/1000; existential first-weight allowance from the original forced polynomial bound.",
                  scope="Actual open words beginning (4,3), full first d_N and both first selections, complete neighboring height attenuation, and surviving second tangent. No global open-source comparison.")
    if old:
        for key in result:
            if key not in ("precision_bits", "scalar_enclosures", "input_sha256"):
                assert old[key] == result[key], key
        assert old["scalar_enclosures"].keys() == scalars.keys()
        assert all(value.overlaps(arb(old["scalar_enclosures"][key]))
                   for key, value in scalars.items())
    assert sha(PROOF) == ph and sha(__file__) == sh
    assert all(sha(ROOT/p) == h for p, h in deps.items())
    if args.input:
        assert sha(args.input) == ih
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(checks), "exact/scalar checks;", len(primary),
          "primary records;", len(deps), "bindings; no roots/cells recomputed")


if __name__ == "__main__":
    main()
