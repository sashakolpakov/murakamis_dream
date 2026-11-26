#!/usr/bin/env python3
"""Complete frozen-center distance-two-R half family with immutable replay."""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import time

from flint import arb, acb

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT/"notes/research_mixed_frozen_center_distance_two_right_halves.md"
HELPER = ROOT/"experiments/certify_mixed_minimum_level_half_stencils.py"
spec = importlib.util.spec_from_file_location("original_half_arithmetic", HELPER)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def coefficient_interval(word, index, table):
    own = word[index]
    lo, hi = (F("-.03"), F(".02")) if not own else (F("-.057"), F("-.02"))
    triple = word[index-1:index+2]
    middle = table["".join(map(str, triple))][1]
    lo, hi = max(lo, F(middle[0], 1000)), min(hi, F(middle[1], 1000))
    following = [word[index+2]] if index+2 < 4 else [0, 1]
    first = [table["".join(map(str, (own, word[index+1], last)))][2]
             for last in following]
    lo = max(lo, F(min(p[0] for p in first), 1000))
    hi = min(hi, F(max(p[1] for p in first), 1000))
    if own == word[index+1] == 1:
        lo, hi = max(lo, F("-.056")), min(hi, F("-.048"))
        if word[index-1] == 1:
            hi = min(hi, F("-.053"))
    assert lo < hi
    return lo, hi


def cases(table):
    result = []
    for region in ("lower", "upper"):
        for word in itertools.product((0, 1), repeat=4):
            for side in ("left", "right"):
                ci, ni = (1, 2) if side == "right" else (2, 1)
                nb = coefficient_interval(word, ni, table)
                for sc, sn in itertools.product(range(word[ci]+1), range(word[ni]+1)):
                    hb = ((F("-.005"), F(1, 300)) if not word[ci] else
                          (F(0), F(".014")) if sc else (F("-.0095"), F(0)))
                    for xi in range(1 if sn else 2):
                        result.append(dict(region=region, word=list(word), side=side,
                            selected=[sc, sn], neighbor_switch=xi,
                            frozen_height_interval=list(map(str, hb)),
                            neighbor_coefficient_interval=list(map(str, nb))))
    assert len(result) == 240
    assert len({json.dumps(c, sort_keys=True) for c in result}) == 240
    return result


def parameters(v, case):
    ar, ii = m.ar, m.ii
    sc, sn = case["selected"]
    hlo, hhi = map(F, case["frozen_height_interval"])
    nlo, nhi = map(F, case["neighbor_coefficient_interval"])
    dh, dn = hhi-hlo, (F(0) if sn else nhi-nlo)
    hc = ar(hlo)+ar(dh)*v[2]
    cn = arb(0) if sn else ar(nlo)+ar(dn)*v[3]
    t = ar(".12")+ar(".1")*v[0]
    rho = (t-ar(".1"))/ar(".12")
    if case["region"] == "lower":
        y = t+(ar(".45")-t)*v[1]
        yp = [ar(".1")*(1-v[1]), ar(".45")-t, arb(0), arb(0)]
        taper, rp = arb(1), [arb(0)]*4
    else:
        y = ar(".45")+ar(".05")*v[1]
        yp = [arb(0), ar(".05"), arb(0), arb(0)]
        taper = 400*(ar(".5")-y)**2
        rp = [800*(y-ar(".5"))*z for z in yp]
    dt, dr = [ar(".1"), arb(0), arb(0), arb(0)], [ar(F(5, 6)), arb(0), arb(0), arb(0)]
    hp, np_ = [arb(0), arb(0), ar(dh), arb(0)], [arb(0), arb(0), arb(0), ar(dn)]
    hn = ar(".014")*taper if sn else cn*taper*rho
    zc, zn = acb(t, hc), acb(y, hn)
    zcp = [d+ii*h for d, h in zip(dt, hp)]
    znp = [d+ii*ar(".014")*rr if sn else
           d+ii*(c*taper*rho+cn*rr*rho+cn*taper*r)
           for d, c, rr, r in zip(yp, np_, rp, dr)]
    bn = cn*taper/ar(".12")
    bnp = [(c*taper+cn*rr)/ar(".12") for c, rr in zip(np_, rp)]
    # Actual center height varies across the enclosure, but its physical
    # minimum-flow velocity is identically zero.
    return zc, zn, zcp, znp, arb(0), bn, [arb(0)]*4, bnp


def compensation(zc, zcp, case):
    ci = 1 if case["side"] == "right" else 2
    if not case["word"][ci]:
        return arb(0), [arb(0)]*4
    if case["side"] == "right":
        return m.ar(F(-1, 5)), [arb(0)]*4
    # The bands meet at h=0; each affine expression equals 4|h|-.053.
    sign = 1 if case["selected"][0] else -1
    return 4*sign*zc.imag-m.ar(F(53, 1000)), [4*sign*z.imag for z in zcp]


def raw_T(u, z, epsilon, d):
    gp, pi, ii, ar = m.m.core.gp, m.pi, m.ii, m.ar
    return (gp(acb(u+ar(".5")))+gp(z+u)-(2+epsilon)*gp(acb(u))
            +2*pi*ii*(d*z+ar(F(1-d, 2)))).real


def row_trial(z, epsilon, d):
    lo, hi = F(1, 5), F(2, 5)
    for _ in range(24):
        trial = (lo+hi)/2
        value = raw_T(m.ar(trial), z, epsilon, d)
        if value > 0:
            lo = trial
        elif value < 0:
            hi = trial
        else:
            break
    return (lo+hi)/2


def row_box(z, trial, epsilon, d):
    assert F(1, 5) <= trial <= F(2, 5)
    u0 = m.ar(trial)
    radius = (abs(raw_T(u0, z, epsilon, d))/(2*m.pi)).upper()
    return (u0+arb(0, radius)).intersection(m.ar(F(1, 5)).union(m.ar(F(2, 5))))


def test(box, case, witness=None):
    ar, ii, pi, gp, gpp = m.ar, m.ii, m.pi, m.m.core.gp, m.gpp
    if witness is not None:
        if not F(0) < F(witness["coherent"]["radius"]) <= F(1, 20):
            return None, None, None
    v = [ar(a).union(ar(b)) for a, b in box]
    vm = [ar((a+b)/2) for a, b in box]
    zc, zn, zcp, znp, bc, bn, bcp, bnp = parameters(v, case)
    zc0, zn0, zcp0, _, bc0, bn0, _, _ = parameters(vm, case)
    word, right = case["word"], case["side"] == "right"
    ci, ni = (1, 2) if right else (2, 1)
    ac, an = word[ci], word[ni]
    a, b, a0, b0, eta, eps = (zc, zn, zc0, zn0, ac, an) if right else (zn, zc, zn0, zc0, an, ac)
    packet = m.root_box(a, b, a0, b0, eps, None if witness is None else witness["coherent"])
    if packet is None:
        return None, None, None
    s, s0, root_witness = packet
    assert F(0) < F(root_witness["radius"]) <= F(1, 20)
    G, HH = m.gradH(s, a, b, eta, eps)
    G0, HH0 = m.gradH(s0, a0, b0, eta, eps)
    if not all(z.is_finite() for z in G+G0+[z for row in HH+HH0 for z in row]):
        return None, None, None
    cidx, nidx = (0, 1) if right else (1, 0)
    d, raw_eps = (1, word[3]) if right else (0, an)
    trial = row_trial(zn0, raw_eps, d) if witness is None else F(witness["row_trial"])
    if not F(1, 5) <= trial <= F(2, 5):
        return None, None, None
    u, u0 = row_box(zn, trial, raw_eps, d), row_box(zn0, trial, raw_eps, d)
    K = gp(zn+u)-(1+ar(F(an, 2)))*gp(zn)+2*pi*ii*d*u
    K0 = gp(zn0+u0)-(1+ar(F(an, 2)))*gp(zn0)+2*pi*ii*d*u0
    Kz = gpp(zn+u)-(1+ar(F(an, 2)))*gpp(zn)
    Ku = gpp(zn+u)+2*pi*ii*d
    Tu = (gpp(acb(u+ar(".5")))+gpp(zn+u)-(2+raw_eps)*gpp(acb(u))).real
    if not Tu.is_finite():
        return None, None, None
    Tu = Tu.intersection(Tu.lower().union((-2*pi).upper()))
    assert Tu < 0
    up = [-(Ku*zz).real/Tu for zz in znp]
    xi = case["neighbor_switch"]
    v_n, v0 = ii*xi*bn, ii*xi*bn0
    vp = [ii*xi*x for x in bnp]
    gamma, gammap = compensation(zc, zcp, case)
    gamma0, _ = compensation(zc0, zcp0, case)
    direct = (G[cidx]+v_n*(G[nidx]+K)).real+gamma
    center = (G0[cidx]+v0*(G0[nidx]+K0)).real+gamma0
    grads = [
        (HH[cidx][cidx]*dc+HH[cidx][nidx]*dn
         +dv*(G[nidx]+K)+v_n*(HH[nidx][cidx]*dc+HH[nidx][nidx]*dn+Kz*dn+Ku*du)).real+dg
        for dc, dn, dv, du, dg in zip(zcp, znp, vp, up, gammap)]
    if not all(z.is_finite() for z in [direct, center, *grads]):
        return None, None, None
    mean = center-sum((abs(z)*ar((b-a)/2) for z, (a, b) in zip(grads, box)), arb(0))
    return max(direct.lower(), mean.lower()), grads, dict(coherent=root_witness, row_trial=str(trial))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--precision", type=int, default=256)
    ap.add_argument("--input", type=Path)
    ap.add_argument("--output", type=Path, default=ROOT/"repro/results/research-mixed-frozen-center-distance-two-right-halves.json")
    ap.add_argument("--max-visits", type=int, default=200000)
    ap.add_argument("--seconds", type=float, default=120)
    args = ap.parse_args()
    m.configure(args.precision)
    ph, sh, deps, primary = sha(PROOF), sha(__file__), {}, {}

    def bind(path, expected=None):
        digest = sha(ROOT/path)
        if expected is not None:
            assert digest == expected, path
        assert path not in deps or deps[path] == digest, path
        deps[path] = digest

    for stem, prefix in [
        ("mixed_neighbor_conditioned_critical_boxes", "certify"),
        ("mixed_four_before_four_height_lower", "certify"),
        ("mixed_three_consecutive_four_height", "check"),
        ("mixed_algebraic_right_row", "check"),
        ("mixed_raw_row_stationarity", "check"),
        ("mixed_one_early_neighbor_transport", "certify"),
        ("mixed_distance_two_right_halves", "certify")]:
        path = "repro/results/research-"+stem.replace("_", "-")+".json"
        bind(path)
        data = json.loads((ROOT/path).read_text())
        assert data["status"] == "passed"
        bind("notes/research_"+stem+".md", data["proof_sha256"])
        bind("experiments/"+prefix+"_"+stem+".py", data["script_sha256"])
        for field in ("dependencies", "dependencies_sha256"):
            for name, digest in data.get(field, {}).items():
                bind(name, digest)
        primary[stem] = data
    assert primary["mixed_four_before_four_height_lower"]["lower_height"] == "-7/125"
    assert primary["mixed_four_before_four_height_lower"]["upper_height"] == "-6/125"
    assert primary["mixed_raw_row_stationarity"]["physical_branch_count"] == 12
    for path in [
        "experiments/certify_mixed_minimum_level_half_stencils.py",
        "experiments/certify_mixed_isolated_transition_phase.py",
        "experiments/certify_mixed_real_small_support.py",
        "notes/research_mixed_minimum_level_half_stencils.md",
        "notes/research_mixed_constant_selected_height_transport.md",
        "notes/research_mixed_one_right_star_reduction.md",
        "notes/research_mixed_early_selected_transport.md",
        "notes/research_mixed_early_selected_source_cap.md",
        "notes/research_mixed_left_right_interface_source.md",
        "notes/research_mixed_unselected_right_taper_products.md"]:
        bind(path)
    replay_path = "repro/results/research-mixed-distance-two-right-halves-replay.json"
    bind(replay_path)
    replay = json.loads((ROOT/replay_path).read_text())
    original_path = "repro/results/research-mixed-distance-two-right-halves.json"
    original = primary["mixed_distance_two_right_halves"]
    assert replay["status"] == "passed" and replay["input_sha256"] == deps[original_path]
    for key in ("proof_sha256", "script_sha256", "dependencies_sha256", "required_cases",
                "completed_cases", "accepted_cells", "visited_cells", "monotonic_reductions"):
        assert replay[key] == original[key], key
    assert replay["completed_cases"] == 400
    specifications = cases(primary["mixed_neighbor_conditioned_critical_boxes"]["limits_in_thousandths"])
    old, ih = None, None
    if args.input:
        raw = args.input.read_bytes()
        ih, old = hashlib.sha256(raw).hexdigest(), json.loads(raw)
        assert old["status"] == "passed" and old["proof_sha256"] == ph and old["script_sha256"] == sh
        assert old["dependencies_sha256"] == deps and len(old["cases"]) == len(specifications)
    started, total_visits, records, status = time.monotonic(), 0, [], "passed"
    for index, case in enumerate(specifications):
        saved = None if old is None else old["cases"][index]
        if saved is not None:
            assert saved["case"] == case
        stack = [[(F(0), F(1))]*4]
        cursor = leaves = visits = monotonic = 0
        nodes, minimum = [], None
        while stack:
            if old is None and (total_visits >= args.max_visits or time.monotonic()-started >= args.seconds):
                status = "incomplete"
                break
            box = stack.pop()
            visits += 1
            total_visits += 1
            node = None if saved is None else saved["nodes"][cursor]
            cursor += saved is not None
            if node is not None and node[0] == "S":
                axis = node[1]
                assert axis in range(4)
            else:
                assert node is None or node[0] in ("L", "M")
                witness = None if node is None else node[-1]
                lower, gradient, witness = test(box, case, witness)
                if node is not None and node[0] == "M":
                    axis, bit = node[1:3]
                    assert axis in range(4) and bit in (0, 1) and gradient is not None
                    assert gradient[axis] > 0 if bit == 0 else gradient[axis] < 0
                    value = box[axis][bit]
                    assert box[axis][0] < box[axis][1]
                    child = list(box); child[axis] = (value, value)
                    stack.append(child); nodes.append(node); monotonic += 1
                    continue
                if lower is not None and lower > 0:
                    leaves += 1
                    minimum = lower if minimum is None else min(minimum, lower)
                    nodes.append(["L", witness])
                    continue
                assert saved is None, ("saved leaf failed", index, cursor, str(lower))
                choices = [] if gradient is None else [
                    (j, 0 if gradient[j] > 0 else 1)
                    for j, (a, b) in enumerate(box) if a < b and
                    (gradient[j] > 0 or gradient[j] < 0)]
                if choices:
                    axis, bit = choices[0]
                    value = box[axis][bit]
                    child = list(box); child[axis] = (value, value)
                    stack.append(child); nodes.append(["M", axis, bit, witness]); monotonic += 1
                    continue
                if gradient is None:
                    _, _, dc, dn, *_ = parameters([m.ar((a+b)/2) for a, b in box], case)
                    axis = max((((abs(dc[j])+abs(dn[j]))*m.ar(b-a)).upper(), j)
                               for j, (a, b) in enumerate(box) if a < b)[1]
                else:
                    axis = max(((abs(gradient[j])*m.ar(b-a)).upper(), j)
                               for j, (a, b) in enumerate(box) if a < b)[1]
            a, b = box[axis]
            assert b-a > F(1, 2**30)
            mid = (a+b)/2
            nodes.append(["S", axis])
            for pair in ((a, mid), (mid, b)):
                child = list(box); child[axis] = pair; stack.append(child)
        if saved is not None:
            assert not stack and cursor == len(saved["nodes"])
            assert (leaves, visits, monotonic) == (
                saved["accepted_cells"], saved["visited_cells"], saved["monotonic_reductions"])
        records.append(dict(case=case, accepted_cells=leaves, visited_cells=visits,
            monotonic_reductions=monotonic, remaining_boxes=len(stack),
            minimum_lower_bound=str(minimum), nodes=nodes))
        print(index, case["region"], case["word"], case["side"], case["selected"],
              case["neighbor_switch"], leaves, visits, str(minimum), flush=True)
        if status != "passed":
            break
    assert sha(PROOF) == ph and sha(__file__) == sh
    assert all(sha(ROOT/path) == digest for path, digest in deps.items())
    if args.input:
        assert sha(args.input) == ih
    result = dict(status=status, precision_bits=args.precision, cases=records,
        required_cases=len(specifications), completed_cases=sum(r["remaining_boxes"] == 0 for r in records),
        accepted_cells=sum(r["accepted_cells"] for r in records), visited_cells=total_visits,
        monotonic_reductions=sum(r["monotonic_reductions"] for r in records),
        maximum_visits=args.max_visits, time_limit_seconds=args.seconds,
        elapsed_seconds=time.monotonic()-started, primary_records=len(primary),
        current_bindings=len(deps), proof_sha256=ph, script_sha256=sh,
        dependencies_sha256=deps,
        scope="Frozen-center distance-two-right halves with the exact one-early "
              "compensations, all states/orientations and both literal neighbor-real "
              "pieces. The complete theorem requires all 240 cases; an incomplete "
              "record proves no full-family sign.")
    if ih:
        result["input_sha256"] = ih
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(status.upper(), result["completed_cases"], "/", len(specifications),
          result["accepted_cells"], total_visits, flush=True)


if __name__ == "__main__":
    main()
