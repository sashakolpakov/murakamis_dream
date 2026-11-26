#!/usr/bin/env python3
"""Exact scalar checks for the positive-path power-seven geometry and currents.

The branch, maximum-principle and arbitrary-length arguments are written
in the proof note. This script checks only their rational comparisons.
"""
from fractions import Fraction as Q
from hashlib import sha256
from math import factorial
from pathlib import Path
import json


def sinh_upper(x):
    return x / (1-x*x/6)


def cosh_upper(x):
    return 1+x*x/(2*(1-x*x/12))


def main():
    root = Path(__file__).resolve().parents[1]
    pi_lower, pi_upper = Q(25, 8), Q(22, 7)
    angle = Q(19, 20)
    cosine_lower = 1-angle**2/2+angle**4/24-angle**6/720
    radius = Q(19,40)**2+sinh_upper(Q(3,20))**2
    margins = {
        "initial_angle_below_pi_over_two": Q(1,2)-Q(40,119),
        "asinh_one_below_nine_tenths":
            sum(Q(9,10)**(2*j+1)/factorial(2*j+1) for j in range(3))-1,
        "sqrt_half_below_five_sevenths": Q(5,7)**2-Q(1,2),
        "initial_neighbor_imaginary_part":
            Q(1,5)-Q(5,7)*sinh_upper(Q(9,35)),
        "first_arcsine_derivative": Q(25,24)**2*(1-Q(1,5)**2)-1,
        "first_period_coefficient": Q(8,15)-Q(5,3)/pi_lower,
        "first_angle_below_one": 1-Q(30,97)*pi_upper,
        "refined_neighbor_imaginary_part": Q(2,15)-sinh_upper(Q(9,35))/2,
        "refined_arcsine_derivative": Q(101,100)**2*(1-Q(8,105)**2)-1,
        "refined_period_coefficient": Q(7,20)-Q(404,375)/pi_lower,
        "final_angle_bound": Q(19,20)-Q(40,133)*pi_upper,
        "angle_cosine_lower": cosine_lower-Q(29,50),
        "first_cosh_upper": Q(8,7)-cosh_upper(Q(18,35)),
        "first_asinh_comparison":
            (Q(14,25)+Q(14,25)**3/6)**2-Q(197,603),
        "second_cosh_upper": Q(53,50)-cosh_upper(Q(8,25)),
        "second_asinh_comparison":
            (Q(21,40)+Q(21,40)**3/6)**2-Q(12,41),
        "shape_disk_radius": Q(1,4)-radius,
        "golden_ratio_cosine_comparison": 5-Q(2)**2,
        "central_angle_contains_saddle": Q(2,5)*pi_lower-Q(19,20),
        "central_wire_contains_quarter": Q(3,10)-Q(1,4),
        "current_neighbor_sinh": Q(4,25)-sinh_upper(Q(3,20)),
        "current_neighbor_cosine": Q(1,2)-Q(7,10)**2,
        "current_side_sine": Q(99,100)-Q(99,100)**3/6-Q(4,5),
        "current_height_cosh": Q(21,20)-cosh_upper(Q(3,10)),
        "current_return_positive_real_part":
            Q(16,41)*Q(7,10)-Q(3,10)*Q(4,35),
        "current_hessian_trace_bound": Q(7,4)**2-3,
        "current_hessian_eigenvalue": Q(41,350)-Q(1,10),
        "current_vertical_derivative": Q(353,13200)-Q(1,40),
        "current_face_gap": Q(1,25000)/pi_upper-Q(1,80000),
        "activation_cost_per_incidence": Q(1,10)-35*pi_upper/Q(1138),
        "centered_loss_reserve": Q(21,200)-Q(1,10)-Q(1,200),
        "signed_eight_angle_bound": Q(9,10)-5*pi_upper/18,
        "signed_eight_height_bound": Q(3,10)-35*pi_upper/373,
    }
    # Two earlier inequalities are exact non-strict bounds, made strict
    # in the proof by pi>25/8 and the open geometric domain.
    nonstrict = {"first_period_coefficient", "centered_loss_reserve"}
    for name, margin in margins.items():
        assert margin >= 0 if name in nonstrict else margin > 0, (name, margin)
    assert radius == Q(252350449,1016334400)
    assert (Q(8,7)-Q(29,50))/(Q(8,7)+Q(29,50)) == Q(197,603)
    assert (Q(53,50)-Q(29,50))/(Q(53,50)+Q(29,50)) == Q(12,41)
    assert (7-Q(2,5))**2+Q(7,5)**2 == Q(1138,25)
    assert (7-Q(4,5))**2+Q(14,5)**2 == Q(1157,25)
    dependencies = [
        "notes/research_unsummed_network_phase_coercivity.md",
        "notes/research_positive_path_fractional_charge_cube.md",
        "notes/research_geometric_phase_maximum_principle.md",
        "notes/research_positive_path_real_wire_order.md",
        "notes/research_positive_path_partial_charge_bounds.md",
        "notes/research_path_mixed_trace_currents.md",
        "notes/research_edge_hessian_and_phase_response.md",
        "notes/research_uniform_path_trace_assembly.md",
        "notes/research_bare_kernel_thin_rectangle.md",
        "experiments/check_positive_path_seven_geometry.py",
    ]
    record = {
        "status": "passed",
        "scope": "Exact scalar comparisons only; the original path and branch arguments remain written proofs.",
        "comparison_count": len(margins),
        "exact_identity_count": 5,
        "margins": {name: str(value) for name,value in margins.items()},
        "nonstrict_comparisons": sorted(nonstrict),
        "dependencies": {name: sha256((root/name).read_bytes()).hexdigest()
                         for name in dependencies},
    }
    output = root/"repro/results/research-positive-path-seven-geometry.json"
    output.write_text(json.dumps(record,indent=2)+"\n")
    print(f"Passed {len(margins)} exact comparisons and 5 exact identities; {output.relative_to(root)}")


if __name__ == "__main__":
    main()
