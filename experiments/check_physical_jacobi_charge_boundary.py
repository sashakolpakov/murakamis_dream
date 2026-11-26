#!/usr/bin/env python3
"""Check the Jacobi/Fourier boundary identity against original matrices."""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_internal_two_crossing_chain import basis_jet
from check_twist_period_insertion import original_matrices
from check_all_color_path_normal_bound import coefficient_data
from check_odd_ward_logarithmic_factorial import ward_function


def relative(a, b):
    return abs(a-b)/max(1, abs(a), abs(b))


def vector_error(a, b):
    return max(relative(a[k], b[k]) for k in range(len(a)))


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    records = []
    maximum = mp.mpf(0)
    value_checks = 0
    green_checks = 0
    regularized_value_checks = 0
    regularized_mixed_normal_checks = 0
    for level in range(3, 13):
        theta = mp.pi/level
        c0 = 2*mp.cos(theta)
        count = (level-1)//2
        eta = (-1)**(level-1)
        crossing, _, _ = original_matrices(level)
        unit = mp.matrix([1]+[0]*(level-1))
        z = mp.matrix(level)
        for r in range(level):
            z[r, r] = 2*mp.cos((2*r+1)*theta)
            if r+1 < level:
                z[r+1, r] = -4*mp.sin((r+1)*theta)**2
        coupons = [mp.eye(level), -z/2]
        for _ in range(1, 2*level-1):
            coupons.append(-z*coupons[-1]-coupons[-2])
        angles = [mp.pi-(2*r+1)*theta for r in range(count+1)]
        jets = [basis_jet(level, -2*mp.cos(t))[0] for t in angles]
        s = lambda x: 2*mp.sin(x*theta)
        aa = [s(r+1)**4/(s(2*r+1)*s(2*r+2)) for r in range(count)]
        cc = [mp.mpf(0) if r == 0 else
              s(r)**4/(s(2*r)*s(2*r+1)) for r in range(count)]
        weights = [s(2*r+1)/s(1) for r in range(count)]
        jacobi = mp.matrix(count)
        jacobi_derivative = mp.matrix(count)
        shifted_coefficients = [coefficient_data(level, r) for r in range(count)]
        for r in range(count):
            jacobi[r, r] = c0+aa[r]+cc[r]
            a, c, ap, cp = shifted_coefficients[r]
            jacobi_derivative[r, r] = ap+cp
            if r+1 < count:
                jacobi[r, r+1] = jacobi[r+1, r] = -mp.sqrt(aa[r]*cc[r+1])
                an, cn, apn, cpn = shifted_coefficients[r+1]
                off = -mp.sqrt(a*cn)*(ap/a+cpn/cn)/2
                jacobi_derivative[r, r+1] = jacobi_derivative[r+1, r] = off
        fourier = mp.matrix(level, count)
        for k in range(level):
            for r in range(count):
                fourier[k, r] = (
                    mp.exp(-1j*k*angles[r])-mp.exp(1j*k*angles[r])
                )/mp.sqrt(2*level)
        sine_weight = mp.diag([
            mp.sin(angles[r])/mp.sqrt(weights[r]) for r in range(count)])
        gram = fourier.H*fourier
        for r in range(count):
            for t in range(count):
                maximum = max(maximum, abs(gram[r, t]-(r == t)))

        colors = [mp.mpc(-2, ".3"), mp.mpc(".5", ".7"),
                  mp.mpc(c0-mp.mpf(".1"), "-.2")]
        for color in colors:
            free, _ = basis_jet(level, color)
            values = [(jet.T*free)[0] for jet in jets]
            delta = c0-color.real
            for r in range(count):
                ratio = values[r+1]/values[r]
                lower = 1+delta/aa[r]
                if ratio.real < lower-tolerance:
                    raise ArithmeticError(("ratio", level, r, color))
                value_checks += 1
            for size in range(1, count+1):
                block = jacobi[:size, :size]-color*mp.eye(size)
                inverse = block**-1
                boundary_factor = mp.sqrt(weights[size-1])*aa[size-1]
                recovered = 1/(boundary_factor*inverse[0, size-1])
                maximum = max(maximum, relative(recovered, values[size]))
                green_checks += 1
            h = mp.matrix([mp.sqrt(weights[r])*values[r] for r in range(count)])
            boundary_factor = mp.sqrt(weights[-1])*aa[-1]
            for power in (-3, 0, 3):
                mult = crossing**power
                density = mult*free
                carriers = [(jet.T*mult*unit)[0] for jet in jets]
                phase = mp.diag(carriers[:count])
                y = phase*h
                operator = phase*(jacobi-color*mp.eye(count))*phase.H
                rhs = mp.matrix(count, 1)
                rhs[count-1] = boundary_factor*values[count]*carriers[count-1]
                error = vector_error(operator*y, rhs)
                observations = [(coupon*density)[level-1] for coupon in coupons]
                increment = mp.matrix([
                    observations[k+level]-eta*observations[k] for k in range(level)])
                coords = fourier.H*increment
                expected = -1j*level*mp.sqrt(2*level)*sine_weight*y
                error = max(error, vector_error(coords, expected))
                transformed = sine_weight*operator*(sine_weight**-1)
                forced = -1j*level*mp.sqrt(2*level)*sine_weight*rhs
                error = max(error, vector_error(transformed*coords, forced))
                maximum = max(maximum, error)
                if error >= tolerance:
                    raise ArithmeticError(("source", level, power, color, error))
                records.append({
                    "N": level, "power": power,
                    "w_real": mp.nstr(color.real, 20),
                    "w_imaginary": mp.nstr(color.imag, 20),
                    "ordinary_rows": count,
                    "maximum_relative_error": mp.nstr(error, 18)})

        # Compare the regularized full normal with the original kernel jets.
        double_count = level//2
        cp0 = -4*theta*mp.sin(theta)
        for k in range(count+1):
            t = angles[k]
            color = -2*mp.cos(t)
            is_double = not (level % 2 and k == count)
            free_value, free_normal = basis_jet(level, color)
            ward_value, ward_angle_normal = ward_function(level, t)
            q_regular = (eta*ward_value+c0)/s(1)**2
            q_regular_derivative = (eta*ward_angle_normal
                                    /(2*mp.sin(t)*s(1)**2)) if is_double else 0
            for j in range(double_count):
                node = 2*mp.cos((2*j+1)*theta)
                fixed_value, fixed_normal = basis_jet(level, node)
                f = (fixed_value.T*free_value)[0]
                fw = (fixed_value.T*free_normal)[0]
                if j == 0:
                    u = q_regular
                    uw = q_regular_derivative
                else:
                    resolvent = (jacobi[:j, :j]-color*mp.eye(j))**-1
                    derivative = jacobi_derivative[:j, :j]
                    cpj = -4*theta*mp.sin((2*j+1)*theta)
                    normalization = mp.fsum(
                        shifted_coefficients[r][2]/shifted_coefficients[r][0]
                        for r in range(j))
                    trace_term = mp.fsum((resolvent*derivative)[r, r] for r in range(j))
                    u = (cp0*q_regular+trace_term-normalization)/cpj
                    trace_derivative = mp.fsum(
                        (resolvent*resolvent*derivative)[r, r] for r in range(j))
                    uw = (cp0*q_regular_derivative+trace_derivative)/cpj
                error = relative(f*u, (fixed_normal.T*free_value)[0])
                regularized_value_checks += 1
                if is_double:
                    error = max(error, relative(
                        fw*u+f*uw, (fixed_normal.T*free_normal)[0]))
                    regularized_mixed_normal_checks += 1
                maximum = max(maximum, error)
                if error >= tolerance:
                    raise ArithmeticError(("regularized normal", level, j, k, error))
    if maximum >= tolerance:
        raise ArithmeticError(("maximum", maximum))
    return {
        "status": "passed", "precision_digits": precision,
        "source_cases": len(records), "ratio_checks": value_checks,
        "green_checks": green_checks,
        "regularized_value_checks": regularized_value_checks,
        "regularized_mixed_normal_checks": regularized_mixed_normal_checks,
        "maximum_relative_error": mp.nstr(maximum, 18), "rows": records}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run(args.precision)
    root = Path(__file__).resolve().parents[1]
    paths = [
        Path(__file__).resolve(),
        root/"notes/research_physical_jacobi_charge_boundary.md",
        root/"experiments/check_internal_two_crossing_chain.py",
        root/"experiments/check_twist_period_insertion.py",
        root/"experiments/check_all_color_path_normal_bound.py",
        root/"experiments/check_odd_ward_logarithmic_factorial.py"]
    result["sha256"] = {
        str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in paths}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k: result[k] for k in (
        "status", "source_cases", "ratio_checks", "green_checks",
        "regularized_value_checks", "regularized_mixed_normal_checks",
        "maximum_relative_error")}, indent=2))


if __name__ == "__main__":
    main()
