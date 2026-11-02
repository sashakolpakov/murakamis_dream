#!/usr/bin/env python3
"""Exact local matrices and gluing algebra; no topology or analytic proof."""
from argparse import ArgumentParser
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REPLAYS = [
    "experiments/audit_all_circle_nonparabolic_edge.py",
    "experiments/audit_all_circle_four_punctured_adapter.py",
    "experiments/audit_all_circle_hurwitz_line_transport.py",
]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sources():
    own = [HERE / "check.py", *HERE.glob("*.tex"), *HERE.glob("figures/*.tex")]
    imports = [
        "papers/circle-tree-geometry/main.tex",
        "papers/strict-conway-geometry/main.tex",
        "papers/strict-conway-geometry/complete.tex",
        "papers/strict-conway-geometry/deformation.tex",
        "papers/marked-fillings/main.tex",
        *REPLAYS,
    ]
    return sorted(set(own + [ROOT / p for p in imports]))


def supplementary_algebra():
    import sympy as s
    E, Q, P, m = s.symbols("E Q P m", nonzero=True)
    beta, gamma = Q + 1 / Q, P + 1 / P
    native_R = (E + Q) * (E * Q + 1) / (E * (Q + 1)**2)
    assert s.cancel(native_R - (E + 1 / E + beta) / (beta + 2)) == 0
    y, z, k = s.symbols("y z k", real=True)
    b = 2 * (1 - y*y) / (1 + y*y)
    g = 2 * (1 - z*z) / (1 + z*z)
    assert s.cancel((4-b*g)/(b+g+4)-2*(y*y+z*z)/(2+y*y+z*z)) == 0
    angular_E = (1+s.I*k)/(1-s.I*k)
    identity = s.cancel(angular_E + 1/angular_E
                        - 2*(1-k*k)/(1+k*k))
    assert identity == 0
    angular_Q = (1+s.I*y)/(1-s.I*y)
    angular_P = (1+s.I*z)/(1-s.I*z)
    H0, H1 = (1-k*y)/(1+k*y), (1-k*z)/(1+k*z)
    assert s.cancel((angular_E+angular_Q)/(1+angular_Q)
                    -(1+angular_E)/(1+H0)) == 0
    Rw = -angular_P*(angular_E-1)**2/(angular_E*(angular_P+1)**2)
    Z1 = (1+angular_E)/(1+H1)
    assert s.cancel(angular_P*(1-angular_E)/(angular_P+1)
                    -Rw*Z1/(Z1-(1-Rw))) == 0
    # Original incoming/outgoing order is essential, at the two-triangle seam.
    incoming = [-m/Q, -Q, -1/(m*Q)]
    outgoing = [-m*Q, -1/Q, -Q/m]
    assert all(s.cancel(outgoing[j]*incoming[2-j]-1) == 0 for j in range(3))
    assert s.cancel(outgoing[0]*incoming[0]-1) != 0

    # The local edge-dependence description is genuinely solved, not assumed.
    a, b0, c, d = s.symbols("a b c d", real=True)
    edges = {(0, 1): a+b0, (0, 2): a+c, (0, 3): a+d,
             (1, 2): b0+c, (1, 3): b0+d, (2, 3): c+d}
    opposite = [edges[0, 1]+edges[2, 3],
                edges[0, 2]+edges[1, 3], edges[0, 3]+edges[1, 2]]
    assert s.expand(opposite[0]-opposite[1]) == 0
    assert s.expand(opposite[0]-opposite[2]) == 0
    assert s.expand((edges[0, 1]+edges[0, 2]-edges[1, 2])/2-a) == 0
    # Positive-shape polarization and the coordinate change used in the proof.
    x0, x1, t0, t1 = s.symbols("x0 x1 t0 t1", real=True)
    x, t = x0+s.I*x1, t0+s.I*t1
    omega = x*s.conjugate(t*x)-t*x*s.conjugate(x)
    assert s.expand(s.I*omega/2-t1*(x0*x0+x1*x1)) == 0
    shape_change = s.Matrix([[1, 0], [-1, -1]])
    assert shape_change.det() == -1

    # Equal eigenvalue ratios at a parabolic auxiliary word do not imply filling.
    parabolic = s.Matrix([[1, 1], [0, 1]])
    longitude = s.Matrix([[1, 2], [0, 1]])
    assert parabolic.det() == 1 and parabolic.trace() == 2
    assert parabolic != s.eye(2)
    assert parabolic*longitude == longitude*parabolic
    # The wrong fixed-white half twist has a nonidentity generic dilation.
    assert s.cancel(m**-2-1) != 0
    return {
        "angular_chart_identities": 5,
        "correct_seam_products": 3,
        "edge_dependence_identities": 3,
        "polarization_and_coordinate_change": 2,
        "negative_controls": {
            "unreversed_seam_rejected": True,
            "parabolic_ratio_does_not_kill_word": True,
            "fixed_white_odd_return_is_not_identity": True,
        },
    }


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.unlink(missing_ok=True)
    if not __debug__:
        raise SystemExit("Assertions must be enabled; no success record written.")
    paths = sources()
    if any(not p.is_file() for p in paths):
        raise SystemExit("A pinned source is missing.")
    before = {str(p.relative_to(ROOT)): digest(p) for p in paths}
    records = []
    with tempfile.TemporaryDirectory(prefix="nonparabolic-tree-") as tmp:
        for index, script in enumerate(REPLAYS):
            output = Path(tmp) / f"{index}.json"
            completed = subprocess.run(
                [sys.executable, "-I", str(ROOT / script), "--output", str(output)],
                text=True, capture_output=True, check=True)
            if not output.is_file():
                raise AssertionError(f"No fresh output from {script}")
            record = json.loads(output.read_text())
            records.append({"script": script, "result": record})
            print(f"Completed exact identities: {script}", flush=True)
    extra = supplementary_algebra()
    assert before == {str(p.relative_to(ROOT)): digest(p) for p in paths}, "Inputs changed"
    result = {
        "scope": "Exact rational face/character/Hurwitz identities and finite row/polarization algebra. No proof by sampling; no verification of inverse-cut topology, global gluing rank, metric completion, analytic uniformity, or preferred-longitude/quantum conclusions.",
        "input_sha256": before,
        "inputs_unchanged": True,
        "replays": records,
        "supplementary": extra,
        "python": sys.version.split()[0],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"output": str(args.output), "supplementary": extra}))


if __name__ == "__main__":
    main()
