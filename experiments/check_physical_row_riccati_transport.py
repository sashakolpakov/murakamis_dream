#!/usr/bin/env python3
"""Check actual Newton rows and their quantitative Riccati transport.

The finite identities and contraction inequalities are checked directly.
Reported scaled asymptotic errors are diagnostics, not a numerical proof
of the uniform theorem.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp


def relative(a, b):
    return abs(a-b)/max(1, abs(a), abs(b))


def limiting_root(x, w):
    p = 2+(2-w)*mp.cot(mp.pi*x)**2
    return (p+mp.sqrt(p*p-4))/2


def direct_rows(level, w, last):
    theta = mp.pi/level
    factorials = [mp.mpf(1)]
    for r in range(1, 2*last+1):
        factorials.append(factorials[-1]*2*mp.sin(r*theta))
    basis = [mp.mpf(1)]
    for r in range(last):
        basis.append(basis[-1]*(2*mp.cos((2*r+1)*theta)-w)
                     /(2*mp.sin((r+1)*theta))**2)
    return [
        mp.fsum(factorials[j+i]/(
            factorials[j-i]*factorials[i]**2)*basis[i]
                for i in range(j+1))
        for j in range(last+1)]


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//3)
    records = []
    maximum_identity_error = mp.mpf(0)
    recurrence_checks = 0
    contraction_checks = 0
    endpoint_contraction_checks = 0
    for level in (32, 64, 128, 256):
        theta = mp.pi/level
        c0 = 2*mp.cos(theta)
        last, start, left = 3*level//8, level//16, level//8
        s = lambda r: 2*mp.sin(r*theta)
        aa = [s(r+1)**4/(s(2*r+1)*s(2*r+2)) for r in range(last)]
        cc = [mp.mpf(0) if r == 0 else
              s(r)**4/(s(2*r)*s(2*r+1)) for r in range(last)]
        for w in (mp.mpc(-2), mp.mpc(-2, ".4"),
                  mp.mpc("-.7", ".9"), mp.mpc("1.7", ".3")):
            values = direct_rows(level, w, last)
            ratios = [None]+[values[j]/values[j-1] for j in range(1, last+1)]
            roots = [None]+[limiting_root(mp.mpf(j)/level, w)
                             for j in range(1, last+1)]
            error = mp.mpf(0)
            for r in range(last):
                q = cc[r]/aa[r]
                if r:
                    q_product = (mp.sin(r*theta)/mp.sin((r+1)*theta))**3
                    q_product *= mp.cos((r+1)*theta)/mp.cos(r*theta)
                    error = max(error, relative(q, q_product))
                    assert 0 < q < 1
                predicted = 1+(c0-w)/aa[r]
                if r:
                    predicted += q*(1-1/ratios[r])
                error = max(error, relative(predicted, ratios[r+1]))
                assert ratios[r+1].real >= 1+(c0-w.real)/aa[r]-tolerance
                recurrence_checks += 1
            kappa = min(
                (c0-w.real)/max(aa[start-1:last]),
                (2-w.real)*mp.cot(mp.pi*last/level)**2)
            assert kappa > 0
            contraction = (1+kappa)**-2
            accumulated_bound = abs(ratios[start]-roots[start])
            maximum_scaled_defect = mp.mpf(0)
            for r in range(start, last):
                mapped_root = 1+(c0-w)/aa[r]+cc[r]/aa[r]*(1-1/roots[r])
                defect = abs(mapped_root-roots[r+1])
                maximum_scaled_defect = max(maximum_scaled_defect, level*defect)
                accumulated_bound = contraction*accumulated_bound+defect
                actual = abs(ratios[r+1]-roots[r+1])
                assert actual <= accumulated_bound+tolerance
                contraction_checks += 1
            endpoint_kappa = min(
                (c0-w.real)/max(aa),
                (2-w.real)*mp.cot(mp.pi*last/level)**2)
            endpoint_contraction = (1+endpoint_kappa)**-2
            endpoint_bound = abs(ratios[1]-roots[1])/abs(roots[1])
            for r in range(1, last):
                mapped_root = 1+(c0-w)/aa[r]+cc[r]/aa[r]*(1-1/roots[r])
                relative_defect = abs(mapped_root-roots[r+1])/abs(roots[r+1])
                endpoint_bound = endpoint_contraction*endpoint_bound+relative_defect
                actual_relative_error = abs(ratios[r+1]-roots[r+1])/abs(roots[r+1])
                assert actual_relative_error <= endpoint_bound+tolerance
                endpoint_contraction_checks += 1
            continued_log = mp.fsum(mp.log(ratios[r]) for r in range(left+1, last+1))
            ordinary_action = level*mp.quad(
                lambda x: mp.log(limiting_root(x, w)),
                [mp.mpf(left)/level, mp.mpf(last)/level])
            xi_left = (mp.mpf(left)+mp.mpf(".5"))/level
            xi_right = (mp.mpf(last)+mp.mpf(".5"))/level
            physical_action = mp.quad(
                lambda x: mp.log(limiting_root(x, w)), [xi_left, xi_right])
            t_left, t_right = mp.pi*(1-2*xi_left), mp.pi*(1-2*xi_right)
            geometric_action = -mp.quad(
                lambda t: mp.asinh(mp.tan(t/2)*mp.sqrt(2-w)/2),
                [t_left, t_right])/mp.pi
            error = max(error, relative(physical_action, geometric_action),
                        relative(mp.exp(continued_log), values[last]/values[left]))
            absolute_log = mp.fsum(mp.log(ratios[r]) for r in range(1, last+1))
            x_end = mp.mpf(last)/level
            def regularized_integrand(x):
                if x == 0:
                    return mp.log(2-w)-2*mp.log(mp.pi)
                return mp.log(limiting_root(x, w))+2*mp.log(x)
            absolute_action = (
                mp.quad(regularized_integrand, [0, x_end])
                -2*x_end*(mp.log(x_end)-1))
            error = max(error, relative(mp.exp(absolute_log), values[last]))
            if error >= tolerance:
                raise ArithmeticError((level, w, error))
            maximum_identity_error = max(maximum_identity_error, error)
            records.append({
                "N": level,
                "w_real": mp.nstr(w.real, 18), "w_imaginary": mp.nstr(w.imag, 18),
                "first_bulk_row": left, "last_bulk_row": last,
                "maximum_identity_error": mp.nstr(error, 20),
                "riccati_contraction_factor": mp.nstr(contraction, 20),
                "maximum_N_times_local_defect": mp.nstr(maximum_scaled_defect, 20),
                "maximum_N_times_bulk_ratio_error_diagnostic": mp.nstr(
                    level*max(abs(ratios[r]-roots[r]) for r in range(left, last+1)), 20),
                "maximum_r_times_relative_ratio_error_diagnostic": mp.nstr(max(
                    r*abs(ratios[r]-roots[r])/abs(roots[r]) for r in range(1, last+1)), 20),
                "absolute_log_error_over_log_N_diagnostic": {
                    "real": mp.nstr((absolute_log-level*absolute_action).real/mp.log(level), 20),
                    "imaginary": mp.nstr((absolute_log-level*absolute_action).imag/mp.log(level), 20)},
                "continued_log_error_diagnostic": {
                    "real": mp.nstr((continued_log-ordinary_action).real, 20),
                    "imaginary": mp.nstr((continued_log-ordinary_action).imag, 20)},
                "physical_phase_log_error_diagnostic": {
                    "real": mp.nstr((continued_log-level*physical_action).real, 20),
                    "imaginary": mp.nstr((continued_log-level*physical_action).imag, 20)}})
    return {
        "status": "passed", "precision_digits": precision,
        "scope": "Finite source identities and Riccati inequalities; asymptotic errors are diagnostics.",
        "source_cases": len(records), "recurrence_checks": recurrence_checks,
        "contraction_checks": contraction_checks,
        "endpoint_contraction_checks": endpoint_contraction_checks,
        "maximum_identity_error": mp.nstr(maximum_identity_error, 20),
        "rows": records}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--precision", type=int, default=140)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run(args.precision)
    root = Path(__file__).resolve().parents[1]
    paths = [Path(__file__).resolve(),
             root/"notes/research_physical_row_riccati_transport.md"]
    result["sha256"] = {
        str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in paths}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: result[key] for key in (
        "status", "source_cases", "recurrence_checks",
        "contraction_checks", "endpoint_contraction_checks",
        "maximum_identity_error")}, indent=2))


if __name__ == "__main__":
    main()
