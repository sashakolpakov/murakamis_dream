#!/usr/bin/env python3
"""Exact scalar comparisons in the small-height pair activation lemma."""

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1]
                        / "repro/results/research-pair-activation-small-height.json")
    args = parser.parse_args()
    margins = {}

    def positive(name, value):
        assert value > 0, name
        margins[name] = str(value)

    positive("imaginary-period angle bound", Q(21, 10)-Q(44, 21)*Q(1001, 1000))
    z = Q(21, 10) ** 2
    positive("sine lower polynomial", 1-z/6+z*z/120-z**3/5040-Q(2, 5))
    positive("sine polynomial decreases", Q(1, 6)-z/60)
    positive("small-height cosine bound", Q(101, 100)-1/(1-Q(1, 2000000)))
    positive("linear angle bound", Q(17*359, 4020)-Q(3, 2)/(1-Q(3, 8000000)))
    positive("complex angle bound", Q(18)**2-Q(17)**2-1)
    positive("sine over radius below 101/100", Q(101, 100)-1/(1-Q(1, 60000)))
    positive("cosh below 101/100", Q(101, 100)-1/(1-Q(1, 20000)))
    positive("tangent linear estimate", Q(6, 5)-Q(101, 99))
    positive("tangent cubic estimate", Q(1, 16)-Q(3, 50))
    positive("tangent absolute estimate", Q(51, 100)-Q(1, 2)-Q(18, 1000)**2/16)
    positive("cosine quadratic estimate", 8*(1-Q(18, 1000)**2/48)-7)
    positive("inverse-sine cubic estimate", Q(1, 5)-1/(6*(1-Q(1, 50)**2)))
    positive("old return within analytic disk", Q(1, 50)-Q(51, 100)*Q(18, 1000)*Q(6, 5))
    positive("new return within analytic disk", Q(1, 50)-Q(51, 100)*Q(18, 1000)*Q(101, 100))
    coefficient = 324*(Q(11, 40)+Q(51, 350)+Q(2, 5)*Q(51, 100)**3
                        *(Q(6, 5)**3+Q(101, 100)**3))
    assert coefficient == Q(803822915834217, 4375000000000)
    positive("relative return error below 184H^2", Q(184)-coefficient)
    assert Q(200)*Q(1, 1000)**2 == Q(1, 5000)
    kappa = Q(2200, 413)
    lower = 8-kappa-Q(11, 108)*(kappa-2)**2-Q(27, 19)
    assert lower == Q(1213006, 9722433)
    positive("unperturbed support separation", lower)
    positive("denominator bound", Q(16)-9-Q(11, 5)**2)
    positive("kappa below 16/3", Q(16, 3)-kappa)
    positive("perturbed support separation", lower-Q(40, 3)*Q(1, 5000))

    # Theorem 2: the exact period equation improves the angle bounds twice.
    maximum_height = Q(3, 100)
    positive("extended imaginary-period angle bound",
             Q(43, 20)-Q(44, 21)*(1+Q(3, 118)))
    z = Q(43, 20)**2
    positive("extended sine lower polynomial",
             1-z/6+z*z/120-z**3/5040-Q(3, 8))
    positive("extended sine polynomial decreases", Q(1, 6)-z/60)
    positive("extended cosh bound",
             Q(101, 100)-1/(1-maximum_height**2/2))
    assert 1-Q(43, 40)**2/2 == Q(1351, 3200)
    assert Q(3, 8)/Q(201, 100)*Q(1351, 3200) == Q(1351, 17152)
    positive("extended real angle bound",
             Q(20)-Q(17152, 1351)*Q(3, 2)/(1-Q(3, 8)*maximum_height**2))
    positive("extended complex angle bound", Q(21)**2-Q(20)**2-1)
    radius = Q(63, 200)
    positive("extended tangent on disk",
             Q(6, 5)-1/((1-radius**2/6)*(1-radius**2/2)))
    positive("extended tangent linear bound",
             Q(11, 20)-Q(1, 2)-Q(63, 100)**2/16)
    positive("extended cosine quadratic bound", 8*(1-Q(63, 100)**2/48)-7)
    positive("extended cosine absolute bound", Q(17, 16)-1-Q(63, 100)**2/7)
    positive("extended old return disk", Q(9, 20)-Q(11, 20)*Q(63, 100)*Q(6, 5))
    positive("extended new return disk", Q(9, 20)-Q(11, 20)*Q(63, 100)*Q(17, 16))
    positive("extended asinh error",
             Q(11, 50)-1/(6*(1-Q(9, 20)**2)))
    coarse = 441*(Q(11, 40)+Q(11, 70)+Q(11, 25)*Q(11, 20)**3
                  *(Q(6, 5)**3+Q(17, 16)**3))
    positive("first relative error below 286H^2", Q(286)-coarse)
    first_error = 286*maximum_height**2
    assert first_error == Q(1287, 5000)
    positive("first exact period improvement",
             Q(23, 5)**2-1-((3+first_error)/(1-first_error))**2)
    radius = Q(69, 1000)
    positive("sharper tangent on disk",
             Q(6, 5)-1/((1-radius**2/6)*(1-radius**2/2)))
    positive("sharper tangent linear bound",
             Q(51, 100)-Q(1, 2)-Q(69, 500)**2/16)
    positive("sharper cosine quadratic bound", 8*(1-Q(69, 500)**2/48)-7)
    positive("sharper cosine absolute bound", Q(101, 100)-1-Q(69, 500)**2/7)
    positive("sharper old return disk",
             Q(1, 10)-Q(51, 100)*Q(69, 500)*Q(6, 5))
    positive("sharper new return disk",
             Q(1, 10)-Q(51, 100)*Q(69, 500)*Q(101, 100))
    positive("sharper asinh error", Q(1, 5)-1/(6*(1-Q(1, 10)**2)))
    sharp = coefficient/324
    positive("second relative error below 13H^2", Q(13)-sharp*Q(23, 5)**2)
    second_error = 13*maximum_height**2
    assert second_error == Q(117, 10000)
    positive("second exact period improvement",
             Q(13, 4)**2-1-((3+second_error)/(1-second_error))**2)
    positive("final relative error below 6H^2", Q(6)-sharp*Q(13, 4)**2)
    assert 6*maximum_height**2 == Q(27, 5000)
    extended_separation = lower-Q(40, 3)*Q(27, 5000)
    assert extended_separation == Q(64123853, 1215304125)
    positive("extended final separation", extended_separation)
    result = {"status": "passed", "arithmetic": "exact fractions",
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "checks": len(margins), "positive_margins": margins}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: value for key, value in result.items() if key != "positive_margins"},
                     indent=2))


if __name__ == "__main__":
    main()
