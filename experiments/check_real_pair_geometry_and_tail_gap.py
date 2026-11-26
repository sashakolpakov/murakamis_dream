#!/usr/bin/env python3
"""Exact scalar checks for real pair geometry and the after-trace tail gap.

This checks rational inequalities and a previously saved Arb enclosure.
It does not replace the continuation, source, or contour arguments.
"""
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import re

from flint import arb, ctx


def cosh_upper(x):
    return 1 + x*x/(2*(1-x*x/12))


def sinh_upper(x):
    return x/(1-x*x/6)


def positive_taylor(x, parity, terms):
    return sum(x**(2*j+parity)/factorial(2*j+parity)
               for j in range(terms))


def bernstein_on_interval(coefficients, left, right):
    """Exact power-to-Bernstein conversion after x=left+(right-left)y."""
    degree = len(coefficients)-1
    power = [
        sum(coefficients[k]*comb(k,j)*left**(k-j)*(right-left)**j
            for k in range(j,degree+1))
        for j in range(degree+1)
    ]
    return [
        sum(power[j]*Q(comb(i,j),comb(degree,j)) for j in range(i+1))
        for i in range(degree+1)
    ]


def poly_add(left, right, right_scale=Q(1)):
    return [(left[k] if k<len(left) else Q(0))
            +right_scale*(right[k] if k<len(right) else Q(0))
            for k in range(max(len(left),len(right)))]


def poly_mul(left, right):
    product=[Q(0)]*(len(left)+len(right)-1)
    for i,a in enumerate(left):
        for j,b in enumerate(right):
            product[i+j]+=a*b
    return product


def aligned_angle_polynomial(C, S):
    A=[Q(1),Q(2),Q(1)]
    B=[2*C*C,Q(0),2*C*C]
    D=[1+S*S,Q(0),S*S]
    plus,minus=poly_add(B,A),poly_add(B,A,Q(-1))
    first=[Q(0),Q(0)]+[
        4624*c for c in poly_mul(D,poly_mul(plus,plus))]
    last=poly_add(D,[Q(0),Q(0),Q(1156)])
    second=poly_mul(poly_mul(minus,minus),poly_mul(last,last))
    return poly_add(first,second,Q(-1))


def main():
    root = Path(__file__).resolve().parents[1]
    ctx.prec = 160
    h = Q(107,100)
    hmax = Q(23,20)
    pi_lower = Q(333,106)
    atan_lower = sum(Q((-1)**k,2*k+1)*Q(1,5)**(2*k+1)
                     for k in range(4))
    catalan_upper = sum(Q((-1)**k,(2*k+1)**2) for k in range(21))
    angle_blocks = sum(
        Q(1,(8*j+1)**2)+Q(1,(8*j+3)**2)
        -Q(1,(8*j+5)**2)-Q(1,(8*j+7)**2)
        for j in range(3))
    angle_series_upper = angle_blocks+Q(41,15625)
    angle_rate_upper = 2*Q(99,70)*Q(106,333)*Q(533,500)
    complete_rate_lower = 4*(1-Q(1,9)+Q(1,25)-Q(1,49))/Q(22,7)
    angle_rate_lower = 2*Q(707,500)*Q(7,22)*angle_blocks
    logarithm_argument_lower = Q(41,99)
    asinh_one_lower = 2*(logarithm_argument_lower
                        +logarithm_argument_lower**3/3)
    three_quarter_angle_upper = (
        Q(24,25)-Q(7,32)-Q(7,5)*Q(25,8)/64
        -Q(7,5)*Q(25,8)**2/1536)
    left_mixed_upper = Q(15,16)*Q(7,6)+Q(3,4)*Q(24,25)+Q(2,3)
    asymmetric_corner_upper = Q(1801,600)-Q(3,5)+Q(36,625)
    two_thirds_angle_block=(Q(1,2)+Q(1,9)+Q(1,50)
                           -Q(1,98)-Q(1,81)-Q(1,242))
    two_thirds_angle_lower=4*Q(7,22)*two_thirds_angle_block
    short_angle=Q(19,20)
    short_angle_cosine_lower=(1-short_angle**2/2
                             +short_angle**4/24-short_angle**6/720)
    high_power_shape_radius=Q(19,40)**2+sinh_upper(Q(3,20))**2
    refined_angle=Q(15,16)
    refined_cosine=(1-refined_angle**2/2
                    +refined_angle**4/24-refined_angle**6/720)
    refined_sine=refined_angle-refined_angle**3/6+refined_angle**5/120
    shape_real_lower=Q(159,200)
    shape_imaginary_upper=Q(243,1970)
    refined_wire_height_upper=(
        2*shape_imaginary_upper/Q(19,20)
        *(Q(1,2)+((1-shape_real_lower)**2+shape_imaginary_upper**2)
          /(8*shape_real_lower**2)))
    third_angle_series=sum(Q(1,(3*j+1)**2)-Q(1,(3*j+2)**2)
                           for j in range(3))+Q(2,1000)+Q(1,300)
    global_mixed_real_upper=Q(7,6)+18*Q(26,15)/(4*pi_lower)*Q(157,200)
    third_angle_constant_upper=3*Q(26,15)/(4*pi_lower)*Q(157,200)
    half_angle_newton_max_upper=Q(5,4)*third_angle_constant_upper
    fixed_square_complement_upper=(
        half_angle_newton_max_upper+Q(24,25)+Q(7,4)+Q(2,15))
    margins = {
        "Machin_pi_lower":16*atan_lower-Q(4,239)-pi_lower,
        "pi_above_25_over_8":pi_lower-Q(25,8),
        "cosh_height_cap_upper":Q(7,4)-cosh_upper(hmax),
        "height_cap_below_pi_over_2":Q(25,8)/2-hmax,
        "barrier_constant_coefficient":pi_lower*(pi_lower-3),
        "barrier_quadratic_coefficient":pi_lower**2/6+pi_lower-4,
        "barrier_quartic_coefficient":(pi_lower-2)/3,
        "critical_height_below_four_fifths":
            (Q(6,5)+Q(6,5)**3/6)**2-2,
        "cosh_four_fifths_upper":Q(7,5)-cosh_upper(Q(4,5)),
        "entry_k0_above_three_quarters":1-Q(7,5)*Q(24,29)**2,
        "sqrt2_upper_three_halves":Q(3,2)**2-2,
        "beta_derivative_upper_squared":Q(3,4)**2-Q(1,2),
        "entry_angle_sum_below_pi_over_2":
            1-Q(60,67)*Q(3,2)*Q(30,73),
        "entry_height_derivative":
            1-Q(64,125)*(Q(3,4)+Q(7,5)*Q(17,20)),
        "height_107_cosh_sinh_squared":
            positive_taylor(h,0,4)*positive_taylor(Q(18,25),1,4)**2-1,
        "asinh_one_below_441_over_500":
            positive_taylor(Q(441,500),1,4)-1,
        "height_107_period_contradiction":
            3*h/2-Q(18,25)-Q(441,500),
        "half_charge_cosh_one_fifth":
            Q(50,49)-cosh_upper(Q(1,5)),
        "half_charge_sec_upper_squared":Q(7,6)**2-Q(4,3),
        "complete_rate_below_7_over_6":
            Q(7,6)-4*catalan_upper/pi_lower,
        "half_charge_rate_below_219_over_200":
            Q(219,200)-(Q(7,6)-Q(441,6086)),
        "exponential_taylor_for_tail":
            sum(Q(23,8)**k/factorial(k) for k in range(7))-Q(50,3),
        "radical_below_final_tail_threshold":
            Q(63,25)-Q(1,50)-Q(7,3),
        "three_angle_blocks_and_tail":Q(533,500)-angle_series_upper,
        "complete_angle_rate_upper":Q(24,25)-angle_rate_upper,
        "double_reflected_real_rate_gap":
            Q(63,25)-2*(Q(24,25)+Q(7,24)),
        "sqrt2_above_140_over_99":2-Q(140,99)**2,
        "sqrt2_above_seven_fifths":2-Q(7,5)**2,
        "asinh_one_above_seven_eighths":asinh_one_lower-Q(7,8),
        "three_quarter_angle_below_two_thirds":
            Q(2,3)-three_quarter_angle_upper,
        "left_mixed_real_rate_gap":Q(63,25)-left_mixed_upper,
        "complete_rate_above_23_over_20":complete_rate_lower-Q(23,20),
        "sqrt2_above_707_over_500":2-Q(707,500)**2,
        "complete_angle_rate_above_239_over_250":
            angle_rate_lower-Q(239,250),
        "mixed_corner_above_29_over_10":
            Q(7,4)*Q(23,20)+Q(239,250)-Q(29,10),
        "asymmetric_height_below_pi":pi_lower-Q(107,100),
        "asymmetric_corner_gap":Q(63,25)-asymmetric_corner_upper,
        "aligned_cosh_quarter_upper":Q(1033,1000)-cosh_upper(Q(1,4)),
        "aligned_cosh_three_eighths_upper":Q(134,125)-cosh_upper(Q(3,8)),
        "aligned_small_coordinate_root":
            1-2*Q(134,125)**2*Q(13,20)**2,
        "aligned_small_coordinate_ratio":Q(33,7)-Q(17,4),
        "aligned_logarithmic_margin":Q(17,12)**2-2,
        "two_thirds_kernel_domain":2-cosh_upper(Q(3,4)),
        "two_thirds_kernel_radical_gap":two_thirds_angle_lower-Q(3,4),
        "small_trace_height_cosh":2-cosh_upper(Q(1,7)),
        "small_trace_asinh_comparison":Q(7,10)-sinh_upper(Q(3,5)),
        "small_trace_sqrt_comparison":Q(1,2)-Q(7,10)**2,
        "large_power_asinh_one_upper":
            positive_taylor(Q(9,10),1,3)-1,
        "large_power_initial_cosh":Q(8,7)-cosh_upper(Q(18,35)),
        "large_power_neighbor_imaginary_cosine":
            Q(1,5)-Q(5,7)*sinh_upper(Q(9,35)),
        "large_power_neighbor_sqrt_bound":Q(5,7)**2-Q(1,2),
        "large_power_angle_upper":Q(19,20)-Q(660,707),
        "large_power_angle_cosine_lower":
            short_angle_cosine_lower-Q(29,50),
        "large_power_first_height_bootstrap":
            (Q(14,25)+Q(14,25)**3/6)**2-Q(197,603),
        "large_power_second_cosh":Q(53,50)-cosh_upper(Q(8,25)),
        "large_power_second_height_bootstrap":
            (Q(21,40)+Q(21,40)**3/6)**2-Q(12,41),
        "large_power_shape_disk_radius":Q(1,4)-high_power_shape_radius,
        "refined_large_power_angle":refined_angle-Q(660,707),
        "refined_large_power_cosine":refined_cosine-Q(59,100),
        "refined_large_power_sine":Q(81,100)-refined_sine,
        "sqrt5_above_111_over_50":5-Q(111,50)**2,
        "refined_wire_height":Q(2,15)-refined_wire_height_upper,
        "third_angle_series_tail":Q(2,1000)+Q(1,300)-Q(21,12100)-Q(1,330),
        "third_angle_series_upper":Q(157,200)-third_angle_series,
        "sqrt3_below_26_over_15":Q(26,15)**2-3,
        "global_mixed_real_rate":Q(25,8)-global_mixed_real_upper,
        "global_mixed_wire_gap":Q(163,50)-Q(25,8)-Q(2,15),
        "left_full_wire_log_comparison":
            sum(Q(7,4)**k/factorial(k) for k in range(5))-Q(50,9),
        "left_full_wire_gap":Q(163,50)-Q(33,50)-Q(7,3)-Q(1,4),
        "right_traced_log_comparison":
            sum(Q(5,4)**k/factorial(k) for k in range(5))-Q(10,3),
        "right_traced_gap":Q(163,50)-Q(7,3)-Q(9,10),
        "fixed_square_complement_gap":
            Q(163,50)-fixed_square_complement_upper-Q(1,100),
        "fixed_square_height_sinh":Q(1,20)-sinh_upper(Q(3,20))**2,
        "fixed_square_height_cosine":Q(1,2)-Q(7,10)**2,
    }
    assert all(v>0 for v in margins.values())
    identities = {
        "sinh_three_quarters_majorant":
            sinh_upper(Q(3,4))==Q(24,29),
        "sinh_four_fifths_majorant":
            sinh_upper(Q(4,5))==Q(60,67),
        "sinh_two_fifths_majorant":
            sinh_upper(Q(2,5))==Q(30,73),
        "entry_height_derivative":
            margins["entry_height_derivative"]==Q(21,3125),
        "entry_k_upper":2*Q(4,5)-Q(3,4)==Q(17,20),
        "cosh_one_fifth_majorant":
            cosh_upper(Q(1,5))==Q(305,299),
        "power_three_half_charge_upper":
            Q(7,6)-Q(441,6086)==Q(9989,9129),
        "half_charge_height_slope":
            2/(Q(450,49)+Q(7,6))==Q(588,3043),
        "integrated_height_slope":
            Q(588,3043)/8==Q(147,6086),
        "tail_log_bound":Q(1,25)*(1+Q(23,8))==Q(31,200),
        "action_difference_bound":
            Q(63,25)-2*Q(219,200)==Q(33,100),
        "final_tail_gap":
            Q(33,100)-2*Q(31,200)==Q(1,50),
        "angle_block_tail":Q(16,25**3)+Q(1,25**2)==Q(41,15625),
        "angle_rate_upper":angle_rate_upper==Q(310739,323750),
        "double_reflected_real_gap":
            margins["double_reflected_real_rate_gap"]==Q(1,60),
        "asinh_one_logarithm_argument":Q(140,99)-1==Q(41,99),
        "three_quarter_angle_upper":
            three_quarter_angle_upper==Q(1631821,2457600),
        "left_mixed_real_rate_upper":left_mixed_upper==Q(5953,2400),
        "left_mixed_real_gap":
            margins["left_mixed_real_rate_gap"]==Q(19,480),
        "mixed_corner_rate_lower":
            Q(7,4)*Q(23,20)+Q(239,250)==Q(5937,2000),
        "mixed_corner_rate_upper":
            Q(7,4)*Q(7,6)+Q(24,25)==Q(1801,600),
        "asymmetric_corner_rate_upper":
            asymmetric_corner_upper==Q(36889,15000),
        "asymmetric_corner_quadratic_correction":
            Q(9,25)/(2*Q(25,8))==Q(36,625),
        "asymmetric_corner_gap":
            margins["asymmetric_corner_gap"]==Q(911,15000),
        "two_thirds_angle_first_block":
            two_thirds_angle_block==Q(7256912,12006225),
        "two_thirds_angle_lower":
            two_thirds_angle_lower==Q(14513824,18866925),
        "two_thirds_kernel_radical_gap":
            margins["two_thirds_kernel_radical_gap"]==Q(1454521,75467700),
        "small_trace_sinh_majorant":sinh_upper(Q(3,5))==Q(30,47),
        "small_trace_angular_descent":Q(3,5)-Q(1,2)==Q(1,10),
        "large_power_initial_height":4*Q(9,10)/7==Q(18,35),
        "large_power_first_tangent_ratio":
            (Q(8,7)-Q(29,50))/(Q(8,7)+Q(29,50))==Q(197,603),
        "large_power_first_height":4*Q(14,25)/7==Q(8,25),
        "large_power_second_tangent_ratio":
            (Q(53,50)-Q(29,50))/(Q(53,50)+Q(29,50))==Q(12,41),
        "large_power_second_height":4*Q(21,40)/7==Q(3,10),
        "large_power_shape_disk_radius":
            high_power_shape_radius==Q(252350449,1016334400),
        "refined_shape_sinh_bound":sinh_upper(Q(3,10))==Q(60,197),
        "refined_shape_imaginary_bound":Q(81,200)*Q(60,197)==shape_imaginary_upper,
        "refined_wire_height_bound":
            refined_wire_height_upper==Q(108361228815,816082404766),
        "third_angle_series_bound":third_angle_series==Q(920357,1176000),
        "global_mixed_real_rate_bound":global_mixed_real_upper==Q(57641,18500),
        "global_mixed_wire_rate_bound":Q(25,8)+Q(2,15)==Q(391,120),
        "global_mixed_wire_gap":margins["global_mixed_wire_gap"]==Q(1,600),
        "left_full_wire_exponential_taylor":
            sum(Q(7,4)**k/factorial(k) for k in range(5))==Q(34193,6144),
        "left_full_wire_rate":Q(33,50)+Q(7,3)+Q(1,4)==Q(973,300),
        "left_full_wire_gap":margins["left_full_wire_gap"]==Q(1,60),
        "right_traced_exponential_taylor":
            sum(Q(5,4)**k/factorial(k) for k in range(5))==Q(7083,2048),
        "right_traced_rate":Q(7,3)+Q(9,10)==Q(97,30),
        "right_traced_gap":margins["right_traced_gap"]==Q(2,75),
        "third_angle_constant_upper":
            third_angle_constant_upper==Q(108173,333000),
        "half_angle_newton_max_upper":
            half_angle_newton_max_upper==Q(108173,266400),
        "fixed_square_complement_upper":
            fixed_square_complement_upper==Q(865637,266400),
        "fixed_square_complement_gap":
            Q(163,50)-fixed_square_complement_upper==Q(2827,266400),
        "fixed_square_height_secant":Q(7,10)/Q(21,20)==Q(2,3),
    }
    assert all(identities.values())
    polynomial = list(map(Q,(1,1,-8,8,-4,4)))
    tables = [
        bernstein_on_interval(polynomial,Q(0),Q(1,2)),
        bernstein_on_interval(polynomial,Q(1,2),Q(1)),
    ]
    expected = [
        [Q(1),Q(11,10),Q(1),Q(4,5),Q(11,20),Q(3,8)],
        [Q(3,8),Q(1,5),Q(1,10),Q(1,5),Q(7,10),Q(2)],
    ]
    assert tables==expected
    assert all(v>0 for table in tables for v in table)
    aligned_tables=[]
    for C,S,left,right,lower in (
        (Q(1033,1000),Q(0),Q(1,8),Q(1),Q(555)),
        (Q(134,125),Q(1,2),Q(1,8),Q(9,16),Q(747)),
        (Q(134,125),Q(1,2),Q(9,16),Q(1),Q(12130)),
    ):
        coefficients=aligned_angle_polynomial(C,S)
        assert len(coefficients)==9
        values=bernstein_on_interval(coefficients,left,right)
        assert all(v>lower for v in values)
        aligned_tables.append({
            "C":str(C),"S":str(S),"interval":[str(left),str(right)],
            "strict_coefficient_lower":str(lower),
            "polynomial_coefficients":list(map(str,coefficients)),
            "Bernstein_coefficients":list(map(str,values)),
        })

    saved_path=root/"repro/results/research-internal-pair-three-mixed-packet.json"
    saved=json.loads(saved_path.read_text())
    assert saved["status"]=="certified"
    match=re.match(r"(\[[^\]]+\])",saved["root"]["selected_action"])
    assert match is not None
    half_action=arb(match.group(1))
    assert half_action>arb(63)/50
    assert half_action<arb(13)/10
    angle_parts=re.findall(r"\[[^\]]+\]",saved["root"]["angle"])
    assert len(angle_parts)==2
    power_three_height=-arb(angle_parts[1])
    assert arb(3)/5<power_three_height<arb(107)/100
    seven_path=root/"repro/results/research-pair-seven-action.json"
    seven_saved=json.loads(seven_path.read_text())
    assert seven_saved["status"]=="certified"
    seven_action=arb(seven_saved["real_action"])
    assert seven_action>arb(163)/50

    dependencies=[
        Path(__file__).resolve(),
        root/"notes/research_real_pair_geometry_and_tail_gap.md",
        root/"notes/research_radical_path_sector_gap.md",
        root/"notes/research_internal_pair_angle_bound.md",
        root/"notes/research_internal_pair_complete_edge_gap.md",
        root/"notes/research_pair_half_charge_action_gap.md",
        root/"notes/research_physical_normal_defect_packet.md",
        root/"notes/research_complete_source_pick_observation.md",
        root/"notes/research_odd_half_charge_observation.md",
        root/"notes/research_internal_pair_reflected_current_identity.md",
        root/"notes/research_internal_pair_combined_contour_reduction.md",
        root/"notes/research_internal_pair_grouped_angular_connectors.md",
        root/"notes/research_internal_pair_local_gaussian.md",
        root/"notes/research_free_boundary_half_charge_observation.md",
        seven_path,
        saved_path,
    ]
    record={
        "status":"passed",
        "arithmetic":"exact rational; saved action and height enclosures read at 160-bit Arb precision",
        "strict_rational_comparisons":len(margins),
        "exact_scalar_identities":len(identities),
        "positive_Bernstein_coefficients":sum(map(len,tables))+27,
        "saved_geometric_half_action":str(half_action),
        "saved_power_three_geometric_height":str(power_three_height),
        "saved_seven_pair_action":str(seven_action),
        "geometric_pair_rate_lower":"63/25",
        "power_three_half_charge_rate_upper":"219/200",
        "action_difference_lower":"33/100",
        "outer_index_rate_profile_upper":"31/200",
        "tail_rate_gap":"1/50",
        "retained_index_range":"1/50 < j/N < 12/25",
        "double_reflected_real_rate_upper":"751/300",
        "double_reflected_real_gap":"1/60",
        "left_mixed_real_index_range":"0 < xi <= 1/8",
        "left_mixed_real_rate_upper":"5953/2400",
        "left_mixed_real_gap":"19/480",
        "left_mixed_near_real_gap":"19/960",
        "mixed_corner_real_rate_lower":"5937/2000",
        "power_three_pair_rate_upper":"13/5",
        "asymmetric_corner_height_range":"3/5 <= H <= 107/100",
        "asymmetric_corner_rate_upper":"36889/15000",
        "asymmetric_corner_real_gap":"911/15000",
        "asymmetric_corner_tube_gap":"911/30000",
        "aligned_angle_height_range":"0 < h <= 3/4",
        "aligned_angle_lower":"K_h(tau) > log(34)/2 > 2*asinh(1)",
        "aligned_angle_Bernstein_certificates":aligned_tables,
        "two_thirds_complete_kernel_rate_lower":str(two_thirds_angle_lower),
        "two_thirds_complete_kernel_radical_gap":
            str(margins["two_thirds_kernel_radical_gap"]),
        "large_power_geometry": {
            "power_range":"n,p >= 7",
            "angle_upper":"19/20",
            "trace_height_upper":"3/10",
            "wire_height_2piY_upper":"2/15",
            "shape_disk_radius":str(high_power_shape_radius),
        },
        "large_power_global_comparisons": {
            "power_range":"n,p >= 7",
            "real_mixed_rate_upper":str(global_mixed_real_upper),
            "mixed_rate_at_geometric_wire_height_upper":"391/120",
            "mixed_rate_at_geometric_wire_height_gap":"1/600",
            "left_wire_cut":"3/50",
            "left_wire_real_trace_rate_upper":"973/300",
            "left_wire_real_trace_gap":"1/60",
            "right_traced_index_cut":"2/5",
            "right_traced_rate_upper":"97/30",
            "right_traced_rate_gap":"2/75",
            "fixed_square_complement_rate_upper":str(fixed_square_complement_upper),
            "fixed_square_complement_rate_gap":"2827/266400 > 1/100",
        },
        "margins":{k:str(v) for k,v in margins.items()},
        "identities":identities,
        "Bernstein_tables":[list(map(str,t)) for t in tables],
        "sha256":{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in dependencies},
        "scope":"Exact scalar comparisons, degree-eight Bernstein certificates for aligned-height angular descent, and saved action/height enclosures. Analytic continuation, geometric period implications, contour assembly and source implications require the written proofs; no middle-cycle coefficient is asserted.",
    }
    output=root/"repro/results/research-real-pair-geometry-and-tail-gap.json"
    output.write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({k:record[k] for k in (
        "status","strict_rational_comparisons","exact_scalar_identities",
        "positive_Bernstein_coefficients","tail_rate_gap")}))


if __name__=="__main__":
    main()
