#!/usr/bin/env python3
"""Exact scalar margins for the original wide-rectangle kernel proof.

The separate endpoint certificate proves the right endpoint inequalities.
This script checks sufficient rational/Taylor bounds for the other regions.
It does not replace the written residue, branch, or Gaussian argument.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_bare_kernel_thin_rectangle.md"
DEPENDENCIES = [
    "notes/research_bare_kernel_wide_endpoint_gaps.md",
    "experiments/certify_bare_kernel_wide_endpoint_gaps.py",
    "repro/results/research-bare-kernel-wide-endpoint-gaps.json",
    "notes/research_path_mixed_trace_currents.md",
    "notes/research_edge_hessian_and_phase_response.md",
]


def cos_upper(x: F) -> F:
    return sum(((-1)**k * x**(2*k) / factorial(2*k) for k in range(5)), F(0))


def cos_lower(x: F) -> F:
    return sum(((-1)**k * x**(2*k) / factorial(2*k) for k in range(4)), F(0))


def sin_lower(x: F) -> F:
    return sum(((-1)**k * x**(2*k+1) / factorial(2*k+1) for k in range(4)), F(0))


def cosh_upper(x: F) -> F:
    assert x*x < 12
    return 1 + x*x / (2*(1-x*x/12))


def sinh_upper(x: F) -> F:
    assert x*x < 6
    return x/(1-x*x/6)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    lo, hi = F(157, 50), F(22, 7)
    C, S = cosh_upper(F(3, 10)), sinh_upper(F(3, 10))
    margins: dict[str, F] = {}

    def check(name: str, value: F) -> None:
        assert value > 0, (name, str(value), float(value))
        margins[name] = value

    check("cosh_height_less_523_over_500", F(523, 500)-C)
    check("sinh_height_less_31_over_100", F(31, 100)-S)
    check("cosh_squared_less_11_over_10", F(11, 10)-C*C)
    check("wire_cosh_less_26_over_25", F(26, 25)-cosh_upper(2*hi/25))
    check("critical_real_C_lower", 1-F(1023, 1000)-F(31, 100)**2/2+F(3, 40))
    imag_C = F(31, 100)*(F(1, 2)+(F(21, 20)**2+F(31, 50)**2)/8)
    check("critical_imag_C_less_3_over_14", F(3, 14)-imag_C)
    check("critical_sine_greater_6_over_7", F(3, 4)-F(6, 7)**2)
    check("critical_wire_height_less_1_over_25", F(1, 25)-1/(8*lo))
    check("critical_real_upper_53_over_200", sin_lower(3*lo/100)-F(3, 40))
    check("high_patch_cos_27_over_20_less_11_over_50", F(11, 50)-cos_upper(F(27, 20)))
    check("high_patch_U_less_5_over_4", F(1, 4)-F(11, 50)*C)
    check("high_patch_real_C_greater_1_over_6", 1-F(205, 264)-F(1, 20)-F(1, 6))
    check("critical_cosh_nu_less_11_over_10", F(11, 10)-cosh_upper(F(1, 4)))
    check("high_patch_critical_real_less_23_over_100", F(5, 33)-hi/25)
    check("patch0_regular_factorial_margin", F(1, 2)-F(3, 10)-F(23, 20)/(2*lo)-F(1, 200))
    check("patch1_regular_factorial_margin", F(1, 2)-F(27, 100)-F(7, 5)/(2*lo)-F(1, 200))
    catalan = sum((F((-1)**k, (2*k+1)**2) for k in range(6)), F(0))
    check("complete_edge_rate_greater_29_over_25", 4*catalan/hi-F(29, 25))
    check("one_over_sqrt2_greater_7_over_10", F(1, 2)-F(7, 10)**2)
    check("high_half_gap_greater_4_over_25", F(29, 25)-4*(1-F(7, 10))/lo-F(3, 5)-F(4, 25))
    check("left_relative_endpoint_gap", 4*lo/225-9/(200*lo)-F(23, 600))
    check("modulus_critical_q_lower", (1-C)/2+F(23, 1000))
    check("height_increment_linear_coefficient", F(1, 10)-2*(C-1))
    check("modulus_critical_X_squared_greater_1_over_16",
          F(3, 4)**4/(F(1, 4)+F(523, 500))**2-F(1, 8)-F(1, 16))
    check("patch0_log_numerator_right_halfplane", cos_lower(F(23, 20))-F(31, 100)*F(26, 25))
    check("patch1_log_numerator_right_halfplane", cos_lower(F(7, 5))-(hi/25)*F(26, 25))
    check("patch2_log_numerator_right_halfplane", sin_lower(lo/100)-F(3, 100))
    check("cot_pi_over_10_less_31_over_10", F(5, 16)+F(5, 16)**3/3-F(10, 31))
    check("argument_tangent_less_39_over_100", F(39, 100)-F(31, 10)*hi/25)
    check("tan_3_over_8_greater_39_over_100", F(3, 8)+F(3, 8)**3/3-F(39, 100))
    check("sin_3pi_over_5_greater_19_over_20", sin_lower(2*lo/5)-F(19, 20))
    check("minus_cos_3pi_over_5_less_31_over_100", F(31, 100)-cos_upper(2*lo/5))
    check("minus_cos_3pi_over_5_greater_3_over_10", cos_lower(2*hi/5)-F(3, 10))
    check("cotangent_monotone_real_coordinate", 1-F(26, 25)*cos_upper(lo/5))
    check("real_cotangent_greater_7_over_10", F(19, 27)-F(7, 10))
    x = 3*hi/20
    check("negative_tangent_greater_minus_3_over_5", F(3, 5)-x/(1-x*x/2))
    check("alias_gap_greater_1_over_200", (lo-F(3, 2))/25-F(3, 50)-F(1, 200))
    check("patch0_modulus_endpoint0", F(9, 16)-F(19, 90))
    check("patch0_product_ratio_less_3_over_5", F(3, 5)-F(225, 676))
    check("patch1_cosine_less_1_over_2", F(1, 2)-cos_upper(F(11, 10)))
    check("patch1_q_less_minus_1_over_10", sin_lower(lo/25)-F(1, 10))
    check("patch1_q_greater_minus_3_over_20", F(3, 20)-hi/25)
    check("patch1_first_modulus_endpoint0", F(11, 20)**2-F(3, 20)**2-F(1, 10))
    check("patch1_first_modulus_endpoint_half", F(11, 20)**2-F(3, 20)**2-F(1, 4))
    check("patch1_product_ratio_less_3_over_5", F(3, 5)-F(66, 121))
    check("patch2_q_less_1_over_25", F(1, 25)-hi/100)
    high_first = F(1, 25)**2+F(1, 4)**2+2*F(1, 25)*F(1, 4)*F(21, 20)+F(1, 10)
    check("patch2_first_modulus_less_9_over_20", F(9, 20)**2-high_first)
    check("patch2_product_ratio_less_3_over_5", F(3, 5)-F(9, 20)*F(109, 100)/F(24, 25)**2)
    check("whole_low_tail_ratio_less_99_over_100", F(99, 100)**2-(1-F(6561, 250000)))
    identities = {
        "last_patch_factorial_margin": F(1, 2)-F(49, 200)-F(1, 4) == F(1, 200),
        "tail_gap_constant": F(16, 25)*F(9, 10)**4/16 == F(6561, 250000),
        "left_coarse_gap": F(4, 75)-F(3, 200) == F(23, 600),
    }
    assert all(identities.values())
    result = {
        "status": "passed",
        "strict_comparisons": len(margins),
        "exact_identities": len(identities),
        "arithmetic": "exact fractions and rational Taylor remainders",
        "scope": "Scalar margins outside the separately certified right-endpoint phase bound.",
        "margins": {k: {"exact": str(v), "approximate": float(v)} for k,v in margins.items()},
        "identities": identities,
        "script_sha256": sha(Path(__file__).resolve()),
        "proof_sha256": sha(PROOF),
        "dependency_sha256": {name: sha(ROOT/name) for name in DEPENDENCIES},
    }
    out = ROOT / "repro/results/research-bare-kernel-wide-rectangle.json"
    out.write_text(json.dumps(result, indent=2)+"\n")
    print(f"Passed {len(margins)} strict comparisons and {len(identities)} identities: {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
