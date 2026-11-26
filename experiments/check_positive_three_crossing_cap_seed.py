#!/usr/bin/env python3
"""Check the exact third cap moment against the literal original source."""

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

import mpmath as mp

import check_one_crossing_gaussian_window as original


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=110)
    parser.add_argument(
        "--output", type=Path,
        default=Path("repro/results/research-positive-three-crossing-cap-seed.json"))
    args = parser.parse_args()
    if args.precision < 80:
        parser.error("Use at least 80 decimal digits.")
    mp.mp.dps = args.precision
    tolerance = mp.mpf(10)**(-(args.precision-30))
    records = []

    def check(label, level, sign, actual, expected):
        error = abs(actual-expected)/max(1, abs(actual), abs(expected))
        if error >= tolerance:
            raise AssertionError((label, level, sign, str(error)))
        records.append({
            "identity": label, "N": level, "sign": sign,
            "relative_error": mp.nstr(error, 16)})

    for level in range(2, 13):
        positive_crossing, q0, kappa0, _ = original.original_matrix(level)
        unit = mp.eye(level)[:, 0]
        reversal = mp.matrix([
            [int(j+k == level-1) for k in range(level)] for j in range(level)])
        for sign in (1, -1):
            matrix = (positive_crossing if sign == 1
                      else positive_crossing**-1)
            kappa = kappa0 if sign == 1 else mp.conj(kappa0)
            q = q0 if sign == 1 else mp.conj(q0)
            gram = matrix.transpose_conj()*matrix
            cap = gram*unit
            inverse_cap = reversal*matrix**-2*unit
            gamma = matrix*(reversal*(matrix*(matrix*(matrix*unit))))
            transported = matrix*cap
            expected = kappa*reversal*gamma.conjugate()
            factorial = mp.mpc(1)
            for j in range(level):
                if j:
                    factorial *= 1-q**(2*j)
                check("cap from inverse original word", level, sign,
                      cap[j], inverse_cap[j])
                check("exact q-exponential cap", level, sign,
                      cap[j], level*(-q)**j/factorial)
                check("third-moment source vector", level, sign,
                      transported[j], expected[j])
            moment = (unit.transpose_conj()*gram*gram*gram*unit)[0]
            norm = mp.fsum(abs(gamma[j])**2 for j in range(level))
            check("third positive moment", level, sign, moment, norm)
            # Construct the three selected crossing blocks separately,
            # retaining both literal J turns and the original closing row.
            closed = matrix*(matrix*unit)
            for _ in range(2):
                closed = reversal*closed
                for _ in range(3):
                    closed = matrix*closed
            check("literal 3,3,2 closure", level, sign,
                  closed[level-1], kappa**2*norm)

    root = Path(__file__).resolve().parents[1]
    certificate = root / "repro/results/research-three-crossing-real-tail-rates.json"
    data = json.loads(certificate.read_text())
    assert data["status"] == "passed"
    a_lo, a_hi = map(
        Fraction, data["certificates"]["A_global_peak"]["interval"])
    assert Fraction(9, 20) < a_lo <= a_hi < Fraction(23, 50)
    first_three = sum(
        (Fraction(1, (3*r+1)**2)-Fraction(1, (3*r+2)**2)
         for r in range(3)), Fraction(0))
    c_lower = Fraction(399, 968)*first_three
    assert first_three == Fraction(60939, 78400)
    assert c_lower == Fraction(3473523, 10841600)
    assert c_lower > Fraction(8, 25)
    delta_lower = 3*c_lower-2*a_hi
    assert delta_lower > Fraction(1, 25)
    paths = [
        Path(__file__).resolve(),
        root / "experiments/check_one_crossing_gaussian_window.py",
        root / "experiments/check_complete_boundary_coefficient_transport.py",
        certificate,
        root / "experiments/verify_three_crossing_real_tail_rates.py",
        root / "experiments/verify_next_crossing_complex_phase.py",
    ]
    result = {
        "status": "passed",
        "scope": "exact original third cap source; reused accepted rate enclosure",
        "precision_decimal_digits": args.precision,
        "levels": list(range(2, 13)),
        "checks": len(records),
        "max_relative_error": max(
            (r["relative_error"] for r in records), key=mp.mpf),
        "rational_bounds": {
            "c_lower": str(c_lower),
            "A_peak_lower": str(a_lo),
            "A_peak_upper": str(a_hi),
            "delta_lower": str(delta_lower),
            "comparison": "delta_lower > 1/25",
        },
        "sha256": {
            str(path.relative_to(root)):
                hashlib.sha256(path.read_bytes()).hexdigest()
            for path in paths},
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: result[key] for key in (
        "status", "checks", "max_relative_error")}))
    print(args.output)


if __name__ == "__main__":
    main()
