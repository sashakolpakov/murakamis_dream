#!/usr/bin/env python3
"""One exact joint-domain corner; both original orientations and all targets.

Author mode proposes one original-log coupled root witness. Saved mode
reuses it. There is no external-input optimization or parameter cover.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys

from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT/"experiments"))
import pilot_mixed_attached_last_row_face as pilot
old = pilot.old
ar = old.ar
LO, HI = F(11, 50), F(9, 20)
KAPPA, CURVATURE = F(1, 2500000), F(1, 5)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def maximum(values):
    """Interval extension of the exact real identity max(x,y)."""
    answer = values[0]
    for value in values[1:]:
        answer = (answer+value+abs(answer-value))/2
    return answer


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--precision", type=int, default=256)
    ap.add_argument("--input", type=Path)
    ap.add_argument("--output", type=Path,
                    default=Path(__file__).with_name("result.json"))
    args = ap.parse_args()
    assert args.precision >= 256
    ctx.prec = args.precision
    pi, ii = arb.pi(), acb(0, 1)
    pilot.PI = old.PI = old.base.PI = pi
    pilot.II = old.II = old.base.I = ii
    sh = sha(__file__)
    ih = sha(args.input) if args.input else None
    previous = json.loads(args.input.read_text()) if args.input else None
    dependencies = {}
    checks = []

    def bind(name, expected=None):
        digest = sha(ROOT/name)
        if expected is not None:
            assert digest == expected, name
        if name in dependencies:
            assert dependencies[name] == digest, name
        dependencies[name] = digest
        return digest

    def read(name):
        bind(name)
        data = json.loads((ROOT/name).read_text())
        assert data["status"] == "passed", name
        for path, digest in data.get("dependencies_sha256", {}).items():
            bind(path, digest)
        return data

    def check(label, condition):
        assert condition, label
        checks.append(label)

    an = "repro/results/research-mixed-reduced-disk-conditional-packets.json"
    rn = "repro/results/research-mixed-reduced-disk-conditional-packets-replay.json"
    author, replay = read(an), read(rn)
    check("the inherited source replay binds the current author",
          replay["input_sha256"] == dependencies[an])
    for record in (author, replay):
        bind("notes/research_mixed_reduced_disk_conditional_packets.md", record["proof_sha256"])
        bind("experiments/certify_mixed_reduced_disk_conditional_packets.py", record["script_sha256"])
    for name in (
        "experiments/pilot_mixed_attached_last_row_face.py",
        "notes/research_mixed_attached_last_row_face_pilot.md",
        "notes/research_mixed_actual_last_row_reference_domains.md",
        "notes/research_mixed_horizontal_revived_endpoint.md",
        "notes/research_mixed_last_row_own_root_normal_form.md",
        "notes/research_mixed_open_word_endpoint_rectangles.md",
    ):
        bind(name)

    # Membership is algebraic. Interval comparisons are not used to decide
    # the exact equalities on either clipping boundary or the circle.
    q = F(29, 62500)
    check("the type-four input lies exactly on its reduced circle",
          q+F(7, 125)**2 == F(3, 50)**2)
    check("the type-four radical real part is inside the attached real interval",
          F(123, 500) < F(3, 10) and 0 < q < (F(7, 20)-F(3, 10))**2)
    check("the type-four height equals the attached lower boundary",
          -F(27, 250) == -F(13, 250)-F(7, 125)
          and -F(27, 250) < -F(1, 50))
    check("the type-three input lies strictly inside its reduced circle",
          F(41, 1000)**2+F(31, 500)**2 < F(83, 1000)**2)
    check("the type-three point is exactly the attached lower-right corner",
          F(139, 500) < F(391, 1000) and -F(9, 125) < F(21, 1000))
    check("the strict all-target halfweight curvature exceeds one fifth",
          F(9, 140)*F(157, 50)-2*KAPPA > CURVATURE)

    c = acb(ar("391/1000"), -ar("9/125"))
    a = acb(ar("3/10")+ar(q).sqrt(), -ar("27/250"))
    params = [c, a]
    if previous is None:
        proposed = pilot.propose(params, params)
        check("one original-log point proposal validates", proposed is not None)
        witness, certificate = proposed
    else:
        assert previous["status"] == "certified_fixed_point"
        assert previous["script_sha256"] == sh
        assert previous["dependencies_sha256"] == dependencies
        witness = previous["original_root_witness"]
        certificate = old.root_box(witness, params, params, 0)
        check("one original-log point proposal validates", certificate is not None)
    Z = certificate["root"]
    Y = [[old.cp(value) for value in row] for row in witness["inverse"]]
    for _ in range(14):
        assert all(0 < z.real < 1 for z in Z+params
                   +[Z[0]+Z[1], Z[0]+params[0], Z[1]+params[1]])
        center = [acb(z.real.mid(), z.imag.mid()) for z in Z]
        ff, _ = old.base.evalf(center, *params, 2)
        _, J = old.base.evalf(Z, *params, 2)
        YJ = old.mm(Y, J)
        E = [[acb(int(i == j))-YJ[i][j] for j in range(2)] for i in range(2)]
        residual = old.mv(Y, ff)
        remainder = old.mv(E, [Z[j]-center[j] for j in range(2)])
        Z = [center[i]-residual[i]+remainder[i] for i in range(2)]
    check("the identified original root remains in its regular chamber",
          all(ar("23/100") < z.real < ar("9/20") and abs(z.imag) < ar("3/25") for z in Z))
    check("fourteen fixed tightening steps give narrow enclosures",
          all(z.real.rad() < ar("1e-30") and z.imag.rad() < ar("1e-30") for z in Z))
    residual, _ = old.base.evalf(Z, *params, 2)
    check("both original unexponentiated residuals contain zero",
          all(value.contains(0) for value in residual))

    orientations = []
    for side in (0, 1):
        eta = side
        A, s, B = params[side], Z[side], Z[1-side]
        value = pilot.phase(s, A, B, eta).real
        p = [v.real for v in pilot.marginals(s, A, B, eta)]
        row_records = []
        slope_left = slope_right = None
        if eta == 0:
            xvalues = [LO, HI]
            xmode = "exact convex endpoint maxima"
        else:
            slope = lambda x: -old.gp(acb(ar(x), A.imag)).real/2-p[0]+2*ar(KAPPA)*(ar(x)-A.real)
            slope_left, slope_right = slope(LO), slope(HI)
            if slope_left < 0:
                xvalues = [LO]
                xmode = "unique clipped maximum at left endpoint"
            elif slope_right > 0:
                xvalues = [HI]
                xmode = "unique clipped maximum at right endpoint"
            else:
                check("the un-clipped target maximizer has a strict derivative bracket",
                      slope_left > 0 and slope_right < 0)
                if previous is None:
                    xvalues = [pilot.trial_x(s, A, B)]
                else:
                    xvalues = list(map(F, previous["orientations"][side]["x_trials"]))
                xmode = "rational clipped-cosine trial with certified global concavity gain"
        for x in xvalues:
            assert LO <= x <= HI
            for z in (LO, HI):
                delta = [ar(x)-A.real, ar(z)-B.real]
                for v in (0, 1):
                    for w in (0, 1):
                        row = -2*pi*v*A.imag+2*pi*w*B.imag
                        row -= ar(eta)*old.g(acb(ar(x), A.imag)).real/2
                        deficit = row-value-sum((p[i]*delta[i] for i in range(2)), arb(0))
                        deficit += ar(KAPPA)*sum((d*d for d in delta), arb(0))
                        gain = arb(0)
                        if eta and "trial" in xmode:
                            gain = pilot.target_gain(slope(x), x)
                        enclosure = deficit.union(deficit+gain)
                        row_records.append(dict(carrier=[v, w], target=[str(x), str(z)],
                                                point_deficit=str(deficit), target_gain=str(gain),
                                                maximum_enclosure=str(enclosure)))
        maximum_bound = maximum([arb(row["maximum_enclosure"]) for row in row_records])
        sign = "negative" if maximum_bound < 0 else "positive" if maximum_bound > 0 else "undecided"
        check("the all-target maximum sign is decided in orientation "+str(side), sign != "undecided")
        orientations.append(dict(side=side, own_epsilon=0, eta=eta,
                                 index_root=str(s), first_argument=str(A), retained_argument=str(B),
                                 reference_rate=str(value), marginals=[str(q) for q in p],
                                 x_mode=xmode, x_trials=[str(x) for x in xvalues],
                                 left_target_slope=None if slope_left is None else str(slope_left),
                                 right_target_slope=None if slope_right is None else str(slope_right),
                                 rows=row_records, maximum_enclosure=str(maximum_bound), sign=sign))
    global_max = maximum([arb(o["maximum_enclosure"]) for o in orientations])
    sign = "negative" if global_max < 0 else "positive" if global_max > 0 else "undecided"
    check("the maximum over both orientations has a certified sign", sign != "undecided")
    metadata = dict(status="certified_fixed_point", script_sha256=sh,
                    dependencies_sha256=dependencies, checks=checks,
                    own_epsilon=0, input_order=["type3 c", "type4 a"],
                    exact_inputs=dict(c=["391/1000", "-9/125"],
                                      a=["3/10+sqrt(29/62500)", "-27/250"]),
                    original_root_witness=witness, fixed_tightening_steps=14,
                    target_interval=[str(LO), str(HI)], kappa=str(KAPPA),
                    target_curvature=str(CURVATURE), final_sign=sign,
                    external_input_searches=0, parameter_cover_cells=0,
                    actual_word_realization_proved=False,
                    scope="One exact point of the closed A3-right-chord times A4 domain. "
                          "Both orientations/all carriers/all targets are enclosed, with no neighborhood "
                          "or actual-word/finite-kernel conclusion.")
    if previous is not None:
        for key, val in metadata.items():
            assert previous[key] == val, key
        assert args.precision >= previous["precision_bits"]
    assert sha(__file__) == sh
    assert all(sha(ROOT/path) == digest for path, digest in dependencies.items())
    if args.input:
        assert sha(args.input) == ih
    result = dict(metadata, precision_bits=args.precision, input_sha256=ih,
                  external_enclosures=[str(z) for z in params],
                  original_roots=[str(z) for z in Z],
                  orientations=orientations, full_maximum_enclosure=str(global_max))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("CERTIFIED FIXED POINT", sign, "full max", global_max,
          "checks", len(checks), "bindings", len(dependencies))
    for row in orientations:
        print("orientation", row["side"], row["x_mode"], row["maximum_enclosure"])


if __name__ == "__main__":
    main()
