#!/usr/bin/env python3
"""Check the terminal trace coordinate against the original period equations.

The proof is in research_terminal_intrinsic_trace_domain.md. These finite
checks use recurrence evaluation, continuation from the original complete
root, and a separate product of the real roots. They are not certificates
for a quantum contour or for all arguments in the half-plane.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp


def chebyshev_u(degree, z):
    if degree == 0:
        return mp.mpf(1)
    previous, current = mp.mpf(1), 2*z
    for _ in range(1, degree):
        previous, current = current, 2*z*current-previous
    return current


def chebyshev_t(degree, z):
    previous, current = mp.mpf(1), z
    if degree == 0:
        return previous
    for _ in range(1, degree):
        previous, current = current, 2*z*current-previous
    return current


def polynomial(power, z):
    return z*chebyshev_u(power-1, z)


def selected_complete_root(power):
    # The established complete root has t=2a-2ib, 0<a<pi/p.
    t_guess = 2*mp.pi*(power-1j)/(power*power+1)
    k_guess = mp.cos(t_guess/2)
    return mp.findroot(lambda k: polynomial(power, k)-1j,
                       k_guess, solver="mnewton")


def continue_root(power, complete, target, steps=96):
    roots = [mp.mpf(0)] + [mp.cos(j*mp.pi/power)
                          for j in range(1, power)]

    def advance(value, start, end, depth=0):
        candidate = mp.findroot(lambda k: polynomial(power, k)-end,
                                value, solver="mnewton")
        argument = mp.fsum(mp.arg(candidate-r) for r in roots)
        if candidate.imag > 0 and 0 < argument < mp.pi:
            return candidate
        # A numerical Newton iteration may cross sheets near a boundary
        # critical value. Reduce the step instead of accepting that root.
        if depth >= 60:
            raise ArithmeticError(("continuation did not retain its branch",
                                   power, start, end, candidate))
        middle = (start+end)/2
        midpoint_root = advance(value, start, middle, depth+1)
        return advance(midpoint_root, middle, end, depth+1)

    value = complete
    previous_target = mp.mpc(0, 1)
    for index in range(1, steps+1):
        w = 1j+(target-1j)*mp.mpf(index)/steps
        value = advance(value, previous_target, w)
        previous_target = w
    return value


def relative(left, right):
    return abs(left-right)/max(1, abs(left), abs(right))


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    targets = [mp.mpc(a, b) for a, b in
               [("0", ".1"), ("0", "1"), ("0", "3"),
                ("-4", ".2"), ("5", ".2"), ("-2", "5")]]
    inverse_rows = []
    period_rows = []
    for power in (2, 3, 4, 5, 8, 15, 30):
        complete = selected_complete_root(power)
        roots = [mp.mpf(0)] + [mp.cos(j*mp.pi/power)
                              for j in range(1, power)]
        for w in targets:
            k = continue_root(power, complete, w)
            argument = mp.fsum(mp.arg(k-r) for r in roots)
            product = mp.power(2, power-1)*mp.fprod(k-r for r in roots)
            residual = max(relative(polynomial(power, k), w),
                           relative(product, w))
            derivative = mp.diff(lambda z: polynomial(power, z), k)
            ratio = (2*abs(k)/abs(derivative))*w.imag/(k*k).imag
            assert k.real > 0 and k.imag > 0 and 0 < argument < mp.pi
            assert residual < tolerance and ratio <= 1+tolerance
            if power == 2:
                assert relative(k*k, w/2) < tolerance
            inverse_rows.append({
                "power": power, "target": str(w),
                "lifted_argument": mp.nstr(argument, 30),
                "relative_residual": mp.nstr(residual, 30),
                "hyperbolic_derivative_ratio": mp.nstr(ratio, 30),
            })
        for u in (mp.mpf(".3"), mp.mpc(".7", ".4"),
                  mp.mpc("2.4", "-.6")):
            y = mp.cos(u/2)
            k = continue_root(power, complete, 1j*y)
            t = 2*mp.acos(k)
            tp = chebyshev_t(power, k)
            period_exponential = k*(mp.sin(u/2)-tp)/y
            reverse_exponential = k*(-mp.sin(u/2)-tp)/y
            discriminant = -k*tp/y
            residual = max(
                relative(mp.sinh(1j*(power*t/2-mp.pi)),
                         mp.tan(t/2)*y),
                relative(discriminant**2, 1+k*k*mp.tan(u/2)**2),
                relative(period_exponential*reverse_exponential, 1),
            )
            assert residual < tolerance
            assert 0 < t.real < mp.pi and t.imag < 0
            period_rows.append({
                "power": power, "boundary_angle": str(u),
                "relative_residual": mp.nstr(residual, 30),
            })
    fold_rows = []
    power = 3
    complete = selected_complete_root(power)
    constant = 1/(3*mp.sqrt(3))
    height = mp.asinh(constant)
    critical_u = mp.pi-2j*height
    predicted = -mp.power(7, mp.mpf(3)/4)/mp.sqrt(6)*mp.exp(1j*mp.pi/4)
    for exponent in (2, 4, 6, 8, 10):
        epsilon = mp.power(10, -exponent)
        u = critical_u-epsilon
        y = mp.cos(u/2)
        k = continue_root(power, complete, 1j*y, steps=160)
        derivative = mp.diff(lambda z: polynomial(power, z), k)
        response_derivative = (
            k/y**2-1j*(1-y*y)/(y*derivative)
        )/(-k*chebyshev_t(power, k)/y)
        normalized = response_derivative*mp.sqrt(epsilon)/predicted
        assert response_derivative.real < 0
        fold_rows.append({
            "epsilon": str(epsilon),
            "normalized_fold_coefficient": mp.nstr(normalized, 40),
            "real_response_derivative": mp.nstr(response_derivative.real, 30),
        })
    assert abs(normalized-1) < mp.mpf(".0001")
    return {
        "scope": ("Finite checks of the geometric inverse branch and exact "
                  "period identities; no quantum contour conclusion."),
        "precision_decimal_digits": precision,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "inverse_checks": inverse_rows, "period_checks": period_rows,
        "boundary_fold_diagnostics": fold_rows,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    result = run(arguments.precision)
    rendered = json.dumps(result, indent=2)+"\n"
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(rendered)
        print(f"Checked {len(result['inverse_checks'])} inverse branches and "
              f"{len(result['period_checks'])} period identities; "
              f"saved {arguments.output}.")
    else:
        print(rendered)


if __name__ == "__main__":
    main()
