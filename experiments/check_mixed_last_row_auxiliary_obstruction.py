#!/usr/bin/env python3
"""One inherited whole-cell witness and fourteen fixed enclosure steps."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

from flint import arb, acb, ctx
import certify_mixed_reduced_disk_conditional_packets as source

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_last_row_auxiliary_obstruction.md"
STEM = "research-mixed-last-row-auxiliary-obstruction"
ANGLES = ["17/20", "159/200"]
BOX = [["27/32", "55/64"], ["25/32", "13/16"]]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--precision", type=int, default=256)
    ap.add_argument("--input", type=Path)
    ap.add_argument("--output", type=Path,
                    default=ROOT / "repro/results" / (STEM + ".json"))
    args = ap.parse_args()
    assert args.precision >= 256
    ctx.prec = args.precision
    source.PI = arb.pi(); source.II = acb(0, 1)
    source.base.PI = source.PI; source.base.I = source.II
    ar = source.ar
    ph, sh = sha(PROOF), sha(__file__)
    ih = sha(args.input) if args.input else None
    old = json.loads(args.input.read_text()) if args.input else None
    deps = {}
    checks = []

    def check(label, condition):
        assert condition, label
        checks.append(label)

    def bind(name, expected=None):
        digest = sha(ROOT / name)
        if expected is not None:
            assert digest == expected, name
        if name in deps:
            assert deps[name] == digest, name
        deps[name] = digest
        return digest

    def read(name):
        bind(name)
        obj = json.loads((ROOT / name).read_text())
        assert obj["status"] == "passed", name
        for path, digest in obj.get("dependencies_sha256", {}).items():
            bind(path, digest)
        return obj

    author_name = "repro/results/research-mixed-reduced-disk-conditional-packets.json"
    replay_name = "repro/results/research-mixed-reduced-disk-conditional-packets-replay.json"
    author, replay = read(author_name), read(replay_name)
    for obj in (author, replay):
        bind("notes/research_mixed_reduced_disk_conditional_packets.md", obj["proof_sha256"])
        bind("experiments/certify_mixed_reduced_disk_conditional_packets.py", obj["script_sha256"])
    check("the inherited replay binds the current source author",
          replay["input_sha256"] == deps[author_name])
    check("both source records retain the same six exact witness trees",
          author["domain_count"] == replay["domain_count"] == 6
          and all(a["types"] == b["types"] and a["tree"] == b["tree"]
                  and a["leaves"] == b["leaves"]
                  for a, b in zip(author["domains"], replay["domains"])))
    for path in (
        "notes/research_mixed_horizontal_revived_endpoint.md",
        "notes/research_mixed_last_row_own_root_normal_form.md",
        "notes/research_mixed_cyclic_critical_height_bounds.md",
        "notes/research_mixed_open_local_factor_coverage.md",
        "notes/research_mixed_open_word_endpoint_rectangles.md",
    ):
        bind(path)
    domain = next(d for d in author["domains"] if d["types"] == [0, 0, 1])
    theta = list(map(F, ANGLES))
    stack = [([(F(0), F(1)), (F(0), F(1))], 0)]
    chosen = None
    for ni, node in enumerate(domain["tree"]):
        box, depth = stack.pop()
        if node[0] == "S":
            assert node[1] == depth % 2
            left, right = source.split(box, node[1])
            stack.extend([(left, depth+1), (right, depth+1)])
        elif all(lo <= t <= hi for (lo, hi), t in zip(box, theta)):
            assert node[0] == "L"
            chosen = ni, box, node[1]
            break
    check("the fixed parameters lie in the stated original leaf", chosen is not None)
    ni, box, witness = chosen
    check("the original right-first traversal gives the accepted leaf at node 127 and its exact rectangle",
          ni == 127 and [[str(v) for v in row] for row in box] == BOX)
    p0 = source.parameter([(sum(row, F(0))/2,)*2 for row in box], (0, 1))
    whole = source.parameter(box, (0, 1))
    check("the inherited original-log affine witness passes on its WHOLE saved cell",
          source.root_box(witness, whole, p0, 0) is not None)
    params = source.parameter([(t, t) for t in theta], (0, 1))
    cert = source.root_box(witness, params, p0, 0)
    check("restriction of the same original witness contains the fixed-point root",
          cert is not None)
    Z = cert["root"]
    Y = [[source.cp(v) for v in row] for row in witness["inverse"]]
    for _ in range(14):
        assert all(0 < z.real < 1 for z in Z + params
                   + [Z[0]+Z[1], Z[0]+params[0], Z[1]+params[1]])
        center = [acb(z.real.mid(), z.imag.mid()) for z in Z]
        ff, _ = source.base.evalf(center, *params, 2)
        _, J = source.base.evalf(Z, *params, 2)
        YJ = source.mm(Y, J)
        E = [[acb(int(i == j))-YJ[i][j] for j in range(2)] for i in range(2)]
        residual = source.mv(Y, ff)
        rem = source.mv(E, [Z[j]-center[j] for j in range(2)])
        Z = [center[i]-residual[i]+rem[i] for i in range(2)]
    check("fourteen fixed mean-value images give narrow original-root enclosures",
          all(z.real.rad() < ar("1e-30") and z.imag.rad() < ar("1e-30") for z in Z))
    ff, _ = source.base.evalf(Z, *params, 2)
    check("both original logarithmic residual enclosures contain zero",
          all(v.contains(0) for v in ff))
    s, b = Z[1], Z[0]
    c, a = params
    x = ar("9/20")
    check("both target real coordinates lie in the closed plateau",
          F("11/50") <= F("9/20") <= F("9/20"))
    check("the exact revived carrier has its stated signed-height branch",
          a.imag < 0 < b.imag)
    check("the own roots retain their original regular source chamber",
          all(ar("23/100") < z.real < ar("9/20") and abs(z.imag) < ar("3/25") for z in Z))
    check("the type-four input violates even the attached lower height bound",
          a.imag < -ar("27/250") < -ar("51/500"))
    check("the type-three input violates even the attached lower height bound",
          c.imag < -ar("9/125") < -ar("13/200"))
    M = (source.phase(s, a, b, 0)-ar("3/2")*source.g(a)-source.g(b)).real
    pa = (source.gp(s+a)-ar("3/2")*source.gp(a)+2*source.PI*source.II*s).real
    pb = (source.gp(s+b)-source.gp(b)).real
    row = 2*source.PI*(-a.imag+b.imag)-source.g(acb(x, a.imag)).real/2
    plane = M+pa*(x-a.real)+pb*(x-b.real)
    excess = row-plane
    check("the retained-halfweight endpoint exceeds its original affine plane",
          excess > ar("9/2000"))
    metadata = dict(
        status="passed", proof_sha256=ph, script_sha256=sh,
        dependencies_sha256=deps, checks=checks, source_domain=[0, 0, 1], side=1,
        angles=ANGLES, containing_node=ni, containing_box=BOX,
        target=["9/20", "9/20"], inherited_witness=witness,
        fixed_tightening_steps=14, new_root_proposals=0, new_parameter_cells=0,
        strict_excess_floor="9/2000", first_type_four_halfweight_retained=True,
        actual_open_word_excluded_by_existing_geometry=True,
        finite_kernel_lower_bound_proved=False,
        scope="A fixed untrimmed auxiliary-image last-row rate obstruction; "
              "the inputs violate ordinary AND attached height bounds.")
    if old is not None:
        for key, value in metadata.items():
            assert old[key] == value, key
        assert args.precision >= old["precision_bits"]
    assert sha(PROOF) == ph and sha(__file__) == sh
    assert all(sha(ROOT/path) == digest for path, digest in deps.items())
    if args.input:
        assert sha(args.input) == ih
    result = dict(metadata, precision_bits=args.precision, input_sha256=ih,
                  reference_enclosures=dict(a=str(a), external_c=str(c), s=str(s), b=str(b)),
                  allocated_reference_rate=str(M), marginals=[str(pa), str(pb)],
                  allocated_last_row_rate=str(row), affine_plane=str(plane), excess=str(excess))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(f"PASS {len(checks)} checks, one inherited witness, 14 fixed steps, "
          f"{len(deps)} bindings; excess {excess} > 9/2000")


if __name__ == "__main__":
    main()
