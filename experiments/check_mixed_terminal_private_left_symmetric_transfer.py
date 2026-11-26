#!/usr/bin/env python3
"""Fixed rational witnesses for the terminal-four private-left barriers.

Stdlib only. This checks elementary rational witnesses and inherited
record bindings; it evaluates no primitive, root, phase or optimizer.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PROOF = "notes/research_mixed_terminal_private_left_symmetric_transfer.md"
FORCE = "repro/results/research-mixed-terminal-four-input-private-left-force.json"
VERTEX = "repro/results/research-mixed-terminal-shared-force-vertices.json"
PINNED = {
    PROOF: "1c007e90e1fd8057d8b3773fd712fbb331b0d71c4b253664535805b37e9e7199",
    "notes/research_mixed_terminal_uniform_main_comparison.md":
        "8658da027d6b5c5692a2da7032c657007b163617d2904b3f06b3e3c21d3b92bb",
    "notes/research_mixed_terminal_symmetric_pair_costs.md":
        "b4ee1a7bdde317edab0210b20cb8616913984c4f992d1cbed240f6092a8e593f",
    "notes/research_mixed_terminal_private_left_joint_transfer.md":
        "41de4b6ab3197e2180bab6174fe01406d525a551ae470f964d0478e8171075ff",
    "notes/research_mixed_terminal_four_input_private_left_force.md":
        "28fd9890765e9b4f666d7fe11bc0364c4e1b6c9de4ae45506251c0ec27679f3b",
    "notes/research_mixed_terminal_private_left_uniform_force.md":
        "20361d2a52affe5273ab4aa056f66b250fa498bb9f87742609f1d9450b9b2ee2",
    "notes/research_mixed_terminal_four_reduced_currents.md":
        "cc4dfa641fdbeab421edf9e450e8ed7ac9c55daff46e0a8153d9e5a65656666c",
    "notes/research_mixed_terminal_full_input_index_barrier.md":
        "45ae03bf28a78df930fc8e7c97054ca40689630423a4d36c0009b6b0bb900ee2",
    FORCE: "a0f03c1a0ca1396a69b685a384dfc2939fbc5ee45eeadf5c3b66cd84472bcf44",
    VERTEX: "feaf49d8666aea740a44d167bc898f5770c059c6331a6b6ff695aba65cf9603f",
}


def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1048576), b""):
            h.update(chunk)
    return h.hexdigest()


def merge_bindings(target, other):
    for path, digest in other.items():
        assert isinstance(digest, str) and len(digest) == 64
        if path in target:
            assert target[path] == digest, (path, target[path], digest)
        target[path] = digest


def verify_bindings(bindings):
    for path, digest in bindings.items():
        assert sha(ROOT / path) == digest, path


def polyval(coefficients, x):
    result = F(0)
    for coefficient in reversed(coefficients):
        result = result*x + coefficient
    return result


def polymul(a, b):
    out = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    bindings = dict(PINNED)
    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    bindings[own] = sha(ROOT / own)
    verify_bindings(bindings)
    force = json.loads((ROOT / FORCE).read_text())
    vertex = json.loads((ROOT / VERTEX).read_text())
    for saved in (force, vertex):
        assert saved["changed_inputs"] == []
        merge_bindings(bindings, saved["input_sha256"])
    assert force["status"] == "passed"
    assert vertex["status"] == "completed fixed saved-only protocol"
    assert vertex["common_all_four_gap_rational"] == "1/400"
    assert F(vertex["worst_budget_upper_rational"]) < -F(1, 400)
    verify_bindings(bindings)

    result = dict(
        status="initializing", proof_path=PROOF, proof_sha256=PINNED[PROOF],
        checker_path=own, checker_sha256=bindings[own], input_sha256=bindings,
        inherited_force_sha256=PINNED[FORCE], inherited_main_vertex_sha256=PINNED[VERTEX],
        domain=dict(beta=1, epsilon=1, private_coordinate_rational="27/100",
            selected_height_interval_rational=["0", "7/500"],
            transfer_selected_height_rational="1/100",
            terminal_height_interval_rational=["-27/250", "-1/50"],
            incoming_real_interval_rational=["11/50", "9/20"],
            original_terminal_interval_rational=["3/20", "1/2"],
            restricted_terminal_interval_rational=["11/50", "2/5"]),
        witnesses=[], curvature_allocations=[], changed_inputs=[],
        counts=dict(analytic_callbacks=0, primitives=0, roots=0,
            reference_evaluations=0, optimizer_evaluations=0,
            source_replays=0, parameter_subdivisions=0),
        rational_barrier_witnesses_verified=False,
        source_scope="original actual oriented and inverse-feasible K4 source references",
        complete_terminal_kernel_proved=False,
    )

    def witness(name, value, expected=None, sign="positive"):
        value = F(value)
        if expected is not None:
            assert value == F(expected), (name, value, expected)
        if sign == "positive":
            assert value > 0, (name, value)
        elif sign == "nonnegative":
            assert value >= 0, (name, value)
        elif sign == "zero":
            assert value == 0, (name, value)
        else:
            raise AssertionError(sign)
        result["witnesses"].append(dict(
            name=name, rational_value=str(value), required_sign=sign))
        return value

    try:
        pi_lo, pi_hi = F(157, 50), F(22, 7)
        witness("pi interval nonempty", pi_hi-pi_lo)
        witness("max negative height exponent below .68",
            F(17, 25)-F(216, 1000)*pi_hi)
        z = F(17, 25)
        exp_majorant = 1+z+z*z/(2*(1-z/3))
        witness("exponential majorant identity",
            exp_majorant-F(5739, 2900), 0, "zero")
        witness("exponential majorant below 2",
            2-exp_majorant, F(61, 2900))
        witness("selected height linear lower",
            1-F(28, 1000)*pi_hi-F(114, 125), 0, "zero")
        witness("selected radius above .9",
            F(114, 125)-F(9, 10))

        witness("left summed-angle cosine lower",
            1-F(187, 175)**2/2-F(2, 5), F(1781, 61250))
        witness("left private cosine lower",
            1-F(11, 175)**2/2-F(99, 100), F(983, 122500))
        witness("left denominator cosine positive angle",
            F(1, 2)-F(44, 100))
        poly = [-F(163, 500), F(18, 25), -F(17, 125)]
        literal = [F(81, 100)-F(142, 125),
                   F(18, 25), 1-F(142, 125)]
        assert literal == poly
        witness("left quadratic concavity", -2*poly[2], F(34, 125))
        witness("left quadratic value at .5", polyval(poly, F(1, 2)), 0, "zero")
        witness("left quadratic value at 1", polyval(poly, F(1)), F(129, 500))
        assert polymul([-F(1), F(2)], [F(2), -F(1)]) == [-F(2), F(5), -F(2)]
        witness("left second factor coefficient",
            1+F(99, 50)*F(2, 5)-F(224, 125), 0, "zero")
        left_ratio = F(142, 125)*F(224, 125)/2
        witness("left ratio identity", left_ratio-F(15904, 15625), 0, "zero")
        witness("left ratio above 1", left_ratio-1, F(279, 15625))
        left_derivative = (left_ratio-1)/(2*left_ratio)
        witness("left derivative lower", left_derivative, F(279, 31808))

        witness("right summed angle above .75 radians", F(24, 100)*pi_lo-F(3, 4))
        z = F(3, 4)
        witness("right cosine upper Taylor reserve",
            F(3, 4)-(1-z*z/2+z**4/24), F(37, 2048))
        witness("right private angle above pi/3", F(34, 100)-F(1, 3))
        witness("right denominator cosine lower",
            1-F(22, 35)**2/2-F(4, 5), F(3, 1225))
        witness("right first numerator smaller than D", F(8, 5)-F(3, 2), F(1, 10))
        witness("right second numerator smaller than D", F(8, 5)-1, F(3, 5))
        d_min = 1+F(1, 2)**2+F(8, 5)*F(1, 2)
        witness("right denominator minimum identity", d_min-F(41, 20), 0, "zero")
        right_ratio = 1/d_min
        witness("right ratio identity", right_ratio-F(20, 41), 0, "zero")
        right_derivative = (right_ratio-1)/2
        witness("right negative derivative reserve", -right_derivative, F(21, 82))

        # Each row is an actual contribution of a pair, intrinsic term,
        # or diagonal weight, ordered (b,s,a,t); no private S'' is used.
        pair_rows = [
            [F(1, 2), F(1, 2), F(0), F(0)],    # V(s,b)
            [F(0), F(1, 2), F(1, 2), F(0)],    # V(s,a)
            [F(0), F(0), F(1, 2), F(1, 2)],    # V(t,a)
            [F(0), F(0), F(0), F(1, 2)],       # V(t,e0), principal t block
            [F(0), F(1), F(0), F(1)],          # -g(s)-g(t)
        ]
        witness("fixed private pair sum below 1", 1-F(2, 5)-F(27, 100), F(33, 100))
        for nu in (0, 1):
            rows = pair_rows + [[F(1, 2), F(0), F(nu), F(0)]]
            total = [sum(row[i] for row in rows) for i in range(4)]
            assert total == [F(1), F(2), F(nu+1), F(2)]
            result["curvature_allocations"].append(dict(nu=nu,
                contributions=[[str(x) for x in row] for row in rows],
                coefficients=[str(x) for x in total],
                scalar_domains=[["11/50", "1/2"], ["11/50", "9/20"], ["11/50", "2/5"]]))
        raw_gap = F(1, 400)+F(1, 20000)
        witness("raw gap arithmetic", raw_gap-F(51, 20000), 0, "zero")
        witness("finite tolerance and polynomial reserve",
            raw_gap-F(1, 1600)-F(1, 800))
        result.update(
            derivative_lower_at_left_rational=str(left_derivative),
            derivative_upper_at_right_rational=str(right_derivative),
            main_budget_gap_rational="1/400",
            inherited_private_face_gap_rational="1/20000",
            scoped_raw_face_gap_rational=str(raw_gap),
            scoped_finite_face_gap_rational="1/800",
            rational_barrier_witnesses_verified=True,
            status="passed",
        )
    except Exception as exc:
        result["status"] = "error"
        result["error"] = repr(exc)
    finally:
        result["changed_inputs"] = [
            path for path, digest in bindings.items() if sha(ROOT/path) != digest]
        if result["changed_inputs"]:
            result["status"] = "error"
            result["error"] = "input hashes changed"
        result["counts"]["rational_witnesses"] = len(result["witnesses"])
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x", encoding="utf-8") as stream:
            json.dump(result, stream, indent=2)
            stream.write("\n")
    print(json.dumps(dict(status=result["status"],
        rational_witnesses=len(result["witnesses"]),
        input_bindings=len(bindings), output=str(args.output))))
    if result["status"] != "passed":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
