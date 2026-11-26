#!/usr/bin/env python3
"""Check positive three-crossing cycles against the original quotient matrix."""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

import check_one_crossing_gaussian_window as original


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument(
        "--output", type=Path,
        default=Path("repro/results/research-positive-three-crossing-cycle.json"))
    args = parser.parse_args()
    if args.precision < 80:
        parser.error("Use at least 80 decimal digits.")
    mp.mp.dps = args.precision
    tolerance = mp.mpf(10)**(-(args.precision-35))
    checks = []

    def check(label, level, sign, power, actual, expected):
        error = abs(actual-expected)/max(1, abs(actual), abs(expected))
        if error >= tolerance:
            raise AssertionError((label, level, sign, power, str(error)))
        checks.append({
            "identity": label, "N": level, "sign": sign, "power": power,
            "relative_error": mp.nstr(error, 16)})

    for level in range(2, 11):
        base, q0, kappa0, factorial = original.original_matrix(level)
        last = level-1
        reversal = mp.matrix([
            [int(j+k == last) for k in range(level)] for j in range(level)])
        unit = mp.eye(level)[:, 0]
        roots = [2*mp.cos(mp.pi*(2*j+1)/level) for j in range(level)]

        def evaluation(z):
            value, derivative = [], []
            product, deriv = mp.mpc(1), mp.mpc(0)
            for j in range(level):
                value.append(product/factorial[j]**2)
                derivative.append(deriv/factorial[j]**2)
                deriv, product = (
                    deriv*(roots[j]-z)-product, product*(roots[j]-z))
            return mp.matrix(value), mp.matrix(derivative)

        z = mp.mpc("-1.9", ".07")
        w = mp.mpc("-.3", "-.11")
        vz, dz = evaluation(z)
        vw, dw = evaluation(w)

        # A shifted complete N-point quadrature is exact for every product
        # of two cardinal functions: its integer bandwidth is < N.
        sample = mp.matrix(level)
        for r in range(level):
            x = (mp.mpf(r)+mp.mpf("0.27"))/level + mp.mpc(0, ".04")
            for j in range(level):
                shift = x-mp.mpf(j)/level
                sample[r, j] = (mp.sin(mp.pi*level*shift)
                                /(level*mp.sin(mp.pi*shift)))
        gram = sample.T*sample
        for j in range(level):
            for k in range(level):
                check("shifted cardinal contraction", level, 0, 0,
                      gram[j, k], int(j == k))

        for sign in (1, -1):
            # Negative multiplication uses an independent matrix inverse.
            matrix = base if sign == 1 else base**-1
            q = q0 if sign == 1 else mp.conj(q0)
            kappa = kappa0 if sign == 1 else mp.conj(kappa0)
            inverse = matrix**-1
            positive = matrix.transpose_conj()*matrix
            vertex = reversal*matrix**3
            transformed = matrix*vertex*inverse
            reciprocal = reversal*positive*reversal
            expected_reciprocal = positive**-1
            for j in range(level):
                for k in range(level):
                    check("positive similarity", level, sign, 1,
                          transformed[j, k], kappa*positive[j, k])
                    check("reciprocal positive operator", level, sign, 0,
                          reciprocal[j, k], expected_reciprocal[j, k])
            first = positive*unit
            for j in range(level):
                expected = (level*(-sign*1j)**j
                            *q**(-mp.mpf(j*(j-1))/2)/factorial[j])
                check("exact reciprocal-factorial cap", level, sign, 1,
                      first[j], expected)

            hp = mp.eye(level)
            ap = mp.eye(level)
            capped = matrix**2*unit
            two_crossing_input = matrix**2*unit
            two_crossing_norm = (two_crossing_input.transpose_conj()*two_crossing_input)[0]
            next_column = matrix*two_crossing_input
            next_norm = (next_column.transpose_conj()*next_column)[0]
            moments = [mp.mpf(1)]
            for power in range(1, 7):
                hp = hp*positive
                ap = ap*vertex
                moment = hp[0, 0]
                moments.append(moment)
                check("literal capped chain", level, sign, power,
                      capped[last], kappa**(power-1)*moment)
                check("full cyclic trace", level, sign, power,
                      mp.fsum(ap[j, j] for j in range(level)),
                      kappa**power*mp.fsum(hp[j, j] for j in range(level)))
                negative_moment = (positive**(-power))[0, 0]
                check("reciprocal cap measure", level, sign, power,
                      negative_moment, moments[power-1])
                transported = (two_crossing_input.transpose_conj()
                               *hp*two_crossing_input)[0]
                if power == 1:
                    literal = matrix**-3*reversal*matrix**3*unit
                else:
                    literal = (matrix**-3*reversal*matrix**2
                               *(reversal*matrix**3)**(power-2)
                               *reversal*matrix**4*unit)
                check("two-crossing cap transport word", level, sign, power,
                      literal[last], kappa**(power-1)*transported)
                transport_lower = next_norm**power/two_crossing_norm**(power-1)
                if mp.re(transported-transport_lower) < -tolerance*abs(transported):
                    raise AssertionError(("positive-block transport lower bound",
                                          level, sign, power))
                for left_name, left in (("value", vz), ("normal", dz)):
                    for right_name, right in (("value", vw), ("normal", dw)):
                        actual = (left.T*ap*right)[0]
                        expected = (kappa**power
                                    *(left.T*inverse*hp*matrix*right)[0])
                        check("free boundary "+left_name+"/"+right_name,
                              level, sign, power, actual, expected)
                if abs(mp.im(moment)) >= tolerance*max(1, abs(moment)):
                    raise AssertionError(("nonreal positive moment", level))
                if mp.re(moment) <= 0:
                    raise AssertionError(("nonpositive moment", level))
                capped = matrix**3*reversal*capped
            check("first cap moment", level, sign, 1, moments[1], level)
            check("second cap moment", level, sign, 2, moments[2],
                  level**2*mp.fsum(s**-2 for s in factorial))
            for power in range(1, 6):
                slack = mp.re(moments[power-1]*moments[power+1]
                              -moments[power]**2)
                if slack < -tolerance*abs(moments[power]**2):
                    raise AssertionError(("moment log convexity", level, power))

    here = Path(__file__).resolve()
    dependencies = [
        here,
        here.with_name("check_one_crossing_gaussian_window.py"),
        here.with_name("check_complete_boundary_coefficient_transport.py")]
    result = {
        "status": "passed",
        "scope": "finite original-source identities; no asymptotic fit",
        "precision_decimal_digits": args.precision,
        "levels": list(range(2, 11)),
        "signed_powers": list(range(1, 7)),
        "checks": len(checks),
        "max_relative_error": max(
            (item["relative_error"] for item in checks), key=mp.mpf),
        "sha256": {
            str(path.relative_to(here.parent.parent)):
                hashlib.sha256(path.read_bytes()).hexdigest()
            for path in dependencies},
        "records": checks,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k: result[k] for k in (
        "status", "checks", "max_relative_error")}))
    print(args.output)


if __name__ == "__main__":
    main()
