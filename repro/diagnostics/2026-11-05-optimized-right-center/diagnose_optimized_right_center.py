"""Bounded scalar diagnostic; no certificate or finite-sum conclusion."""
from pathlib import Path
import hashlib
import importlib.util
import itertools
import json
import time

from scipy.optimize import minimize_scalar

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
HELPER = ROOT / "repro/diagnostics/2026-11-05-seam-attenuation-vertices/phase_helpers.py"
spec = importlib.util.spec_from_file_location("phase_helpers", HELPER)
phase_helpers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(phase_helpers)
phase, g = phase_helpers.phase, phase_helpers.g


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def J(x):
    return float(g(x).real)


def raw_row(a, b, eta, eps, u):
    return (
        J(a + u) - J(a) + J(b + u) - J(b)
        - (2 + eps) * J(u)
        - eta * .5 * min(J(a), 0)
        - eps * .5 * min(J(b), 0)
    )


def raw_max(a, b, eta, eps):
    # The proved full-row reduction puts the real-right maximum on this
    # lower half-row interval; this call is nevertheless floating only.
    f = lambda u: raw_row(a, b, eta, eps, u)
    opt = minimize_scalar(
        lambda u: -f(u), bounds=(1e-10, .5 - 1e-10),
        method="bounded", options={"xatol": 1e-13},
    )
    trials = [(f(0), 0.), (f(.5), .5), (-float(opt.fun), float(opt.x))]
    return max(trials)


def main():
    output = HERE / "results.json"
    assert not output.exists(), "refuse to overwrite"
    before = sha(HELPER)
    start = time.monotonic()
    cases = []
    for eta, beta, gamma in itertools.product(range(2), repeat=3):
        for a, c in itertools.product((.1, .5), repeat=2):
            def coherent(t):
                return float((phase(a, t, eta, beta)[0]
                              + phase(t, c, beta, gamma)[0]).real)
            opt = minimize_scalar(
                lambda t: -coherent(t), bounds=(.1 + 1e-10, .5 - 1e-10),
                method="bounded", options={"xatol": 1e-13},
            )
            trials = [(coherent(.1), .1), (coherent(.5), .5),
                      (-float(opt.fun), float(opt.x))]
            coherent_max, center = max(trials)
            left, u = raw_max(a, .5, eta, beta)
            right, v = raw_max(.5, c, beta, gamma)
            cases.append(dict(
                types=[eta, beta, gamma], endpoints=[a, c],
                raw=left + right, rows=[u, v], center=center,
                coherent_max=coherent_max, excess=left + right - coherent_max,
            ))
    # Preserve rational rows from the already-certified physical example.
    t = .344
    values = [phase(.1, t, 1, 0), phase(t, .5, 0, 1)]
    f = float((values[0][0] + values[1][0]).real)
    derivative = float((values[0][1][1] + values[1][1][0]).real)
    tangent_upper = f + max(derivative * (.1 - t), derivative * (.5 - t))
    fixed_raw = raw_row(.1, .5, 1, 0, .28) + raw_row(.5, .5, 0, 1, .23)
    assert sha(HELPER) == before
    result = dict(
        scope=(
            "Floating diagnostic only. Real right center is one half; neighbors "
            "are real .1 or .5 and all selections are zero. Full raw row "
            "maximization reduces to the lower half by an existing theorem. "
            "Coherent one-variable maxima and the tangent comparison here are "
            "not outward certified. No original finite-kernel or whole-cycle "
            "failure is asserted."
        ),
        cases=cases,
        worst=max(cases, key=lambda row: row["excess"]),
        preserved_physical_case=dict(
            types=[1, 0, 1], endpoints=[.1, .5], rows=["7/25", "23/100"],
            tangent_center="43/125", fixed_raw=fixed_raw,
            coherent_value=f, coherent_derivative=derivative,
            concave_tangent_upper=tangent_upper,
            fixed_rows_minus_tangent=fixed_raw-tangent_upper,
        ),
        helper=str(HELPER.relative_to(ROOT)), helper_sha256=before,
        script_sha256=sha(Path(__file__)),
        elapsed_seconds=time.monotonic()-start,
    )
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result["preserved_physical_case"], indent=2))


if __name__ == "__main__":
    main()
