#!/usr/bin/env python3
"""Whole-witness cap-rate and real-cut bounds; no new roots or subdivisions."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time

from flint import acb, arb, ctx
import certify_mixed_endpoint_packet_extension as base

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_cap_real_cut_gaps.md"
ar = base.ar


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def phase(e, t, u, eps):
    return (base.phase(e, u)+base.J(e+t)-base.J(t)-II*PI*e*t
            -eps*(base.J(e)+II*PI*e*(1-e)/2))


def test(witness, eps, one=False):
    radius = ar(witness["radius"])
    assert radius > 0
    centers = [acb(ar(v[0]), ar(v[1])) for v in witness["centers"]]
    if one:
        assert len(centers) == 2
        centers = [centers[0], centers[0], centers[1]]
    assert len(centers) == 3
    em, tm, um = centers
    e, t, u = [v+acb(arb(0, radius), arb(0, radius)) for v in centers]
    assert all(0 < v.real < 1 for v in (e, t, u, e-u, e+t, acb(ar(F(1, 2)))-u))
    value = phase(em, tm, um, eps).real
    pe = (-base.gp(em-um)+II*PI*um+base.gp(em+tm)-II*PI*tm
          -eps*(base.gp(em)+II*PI*(ar(F(1, 2))-em)))
    pu = base.partials(em, um)[1]
    pt = base.gp(em+tm)-base.gp(tm)-II*PI*em
    b = PI*(PI*(e-u)).cot()
    c = PI*(PI*(e+t)).cot()
    h = PI*(2*(PI*u).tan()+3*(PI*u).cot())
    common = (abs(-b+c-eps*PI*(PI*e).cot()+II*PI*eps)
              +2*abs(c-II*PI)+2*abs(b+II*PI)+abs(-h-b))
    lower_m = (value-radius*(abs(pe)+abs(pt)+abs(pu))
               -radius**2*(common+abs(c-PI*(PI*t).cot()))/2)
    assert lower_m > 1, ("selected cap rate", eps, one, lower_m)
    lows = [lower_m.lower()]
    for cut in CUTS:
        uc, _ = base.critical(cut)
        cut_value = phase(cut, tm, uc, eps).real
        dt = base.gp(em+tm)-base.gp(cut+tm)-II*PI*(em-cut)
        hessian = common+abs(c-PI*(PI*(cut+t)).cot())
        loss = (value-cut_value-radius*(abs(pe)+abs(pu)+abs(dt))
                -radius**2*hessian/2)
        assert loss > ar(F(1, 2000)), ("real cut", eps, one, str(cut), loss)
        lows.append(loss.lower())
    return lows


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--precision", type=int, default=256)
    ap.add_argument("--input", type=Path)
    ap.add_argument("--output", type=Path, default=ROOT /
                    "repro/results/research-mixed-cap-real-cut-gaps.json")
    args = ap.parse_args()
    assert args.precision >= 192
    ctx.prec = args.precision
    global PI, II, CUTS
    PI, II = arb.pi(), acb(0, 1)
    base.PI, base.II = PI, II
    CUTS = [acb(ar(F(27, 100))), acb(ar(F(49, 100)))]
    ph, sh = sha(PROOF), sha(__file__)
    ih = sha(args.input) if args.input else None
    old = json.loads(args.input.read_text()) if args.input else None
    deps = {}

    def bind(path, expected=None):
        digest = sha(ROOT/path)
        if expected is not None:
            assert digest == expected, path
        assert path not in deps or deps[path] == digest, path
        deps[path] = digest
        return digest

    extraction_path = "repro/results/research-mixed-open-word-endpoint-rectangles.json"
    bind(extraction_path)
    extraction = json.loads((ROOT/extraction_path).read_text())
    assert extraction["status"] == "passed"
    bind("notes/research_mixed_open_word_endpoint_rectangles.md", extraction["proof_sha256"])
    bind("experiments/check_mixed_open_word_endpoint_rectangles.py", extraction["script_sha256"])
    for p, digest in extraction["dependencies_sha256"].items():
        bind(p, digest)
    roots_path = "repro/results/research-mixed-open-word-critical-localization.json"
    roots = json.loads((ROOT/roots_path).read_text())
    assert roots["status"] == "passed"
    assert [(d["epsilon"], d["neighbor_epsilon"]) for d in roots["domains"]] == [
        (0, 0), (0, 1), (1, 0), (1, 1)]
    # The source phase is fixed by this established original finite identity.
    bind("notes/research_mixed_conditional_torus_composition.md")
    bind("notes/research_mixed_complete_boundary_sum.md")
    if old is not None:
        assert old["status"] == "passed"
        assert old["proof_sha256"] == ph and old["script_sha256"] == sh
        assert old["dependencies_sha256"] == deps
    start = time.monotonic()
    minimum = [[None]*3 for _ in range(2)]
    counts = [0, 0]

    def collect(witness, eps, one=False):
        values = test(witness, eps, one)
        for j, value in enumerate(values):
            prior = minimum[eps][j]
            minimum[eps][j] = value if prior is None else min(prior, value)
        counts[eps] += 1

    for domain in roots["domains"]:
        leaves = 0
        for node in domain["tree"]:
            if node[0] == "L":
                collect(node[1], domain["epsilon"])
                leaves += 1
        assert leaves == domain["leaves"]
        print("PASS endpoint domain", domain["epsilon"], domain["neighbor_epsilon"], leaves, flush=True)
    assert sum(counts) == extraction["endpoint_witnesses"] == 5258
    assert [v["epsilon"] for v in roots["one_vertex"]] == [0, 1]
    for one in roots["one_vertex"]:
        collect(one["witness"], one["epsilon"], one=True)
    assert counts == [3348, 1912]
    if old:
        assert old["witness_counts"] == counts
    assert sha(PROOF) == ph and sha(__file__) == sh
    assert all(sha(ROOT/p) == digest for p, digest in deps.items())
    if args.input:
        assert sha(args.input) == ih
    result = dict(status="passed", precision_bits=args.precision,
        endpoint_maps=4, one_vertex_count=2, witness_counts=counts,
        selected_rate_floor="1", real_cut_gap_floor="1/2000",
        minimum_rate_left_right=[[str(x) for x in row] for row in minimum],
        proof_sha256=ph, script_sha256=sh, dependencies_sha256=deps,
        input_sha256=ih, elapsed_seconds=time.monotonic()-start,
        scope="Correlated original endpoint cap rates and two real cuts only; no horizontal alias or whole real-tail theorem.")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", sum(counts), "original witness disks; minima", result["minimum_rate_left_right"], flush=True)


if __name__ == "__main__":
    main()
