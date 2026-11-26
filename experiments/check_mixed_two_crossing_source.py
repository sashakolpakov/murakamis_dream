#!/usr/bin/env python3
"""Check the exact mixed pendant source in the full original Newton algebra."""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_boundary_crossing_packet_preservation import original_crossings, evaluate
from check_twist_period_insertion import encode


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    records = []
    for level in range(2, 17):
        positive, negative = original_crossings(level)
        unit = mp.matrix([1]+[0]*(level-1))
        turn = mp.matrix([[int(i+j == level-1) for j in range(level)]
                          for i in range(level)])
        exact = turn*negative*negative*turn*positive*positive*unit
        gram = (positive*positive).transpose_conj()*positive*positive*unit
        q = mp.exp(mp.pi*1j/level)
        factorial = [mp.mpf(1)]
        for k in range(1, level):
            factorial.append(factorial[-1]*2*mp.sin(mp.pi*k/level))
        formula = mp.matrix([
            level**2 * (-1j)**j * q**(-mp.mpf(j*(j-1))/2)
            / factorial[j]**2
            * mp.fsum(q**(a*j)*factorial[a+j]/factorial[a]**3
                      for a in range(level-j))
            for j in range(level)])
        scale = max(1, mp.norm(exact), mp.norm(formula))
        coefficient_error = mp.norm(exact-formula)/scale
        gram_error = mp.norm(exact-gram)/scale
        endpoint = mp.fsum(s*s for s in factorial)
        endpoint_error = abs(formula[0]-endpoint)/max(1, abs(endpoint))
        jet_rows = []
        for angle in (mp.mpf(0), mp.mpc('.08', '.025'), mp.mpc('-.17', '.04')):
            actual = evaluate(level, exact, angle)
            expected = evaluate(level, formula, angle)
            error = max(abs(a-b)/max(1, abs(a), abs(b))
                        for a, b in zip(actual, expected))
            jet_rows.append({'angle': encode(angle), 'relative_error': mp.nstr(error, 35)})
        worst = max(coefficient_error, gram_error, endpoint_error,
                    *(mp.mpf(row['relative_error']) for row in jet_rows))
        if worst > tolerance:
            raise ArithmeticError((level, worst))
        records.append({'N': level,
                        'coefficient_relative_error': mp.nstr(coefficient_error, 35),
                        'gram_relative_error': mp.nstr(gram_error, 35),
                        'endpoint_positive_sum_relative_error': mp.nstr(endpoint_error, 35),
                        'boundary_value_and_derivative_checks': jet_rows})
        print(f'Original mixed source checked at N={level}.', flush=True)
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision', type=int, default=120)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = {'scope': 'Full original coefficient and boundary-jet normalization checks; '
                       'no asymptotic follows from these finite comparisons.',
              'decimal_precision': args.precision,
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'checks': run(args.precision)}
    content = json.dumps(result, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content)
        print(f'Saved {args.output}.')
    else:
        print(content)


if __name__ == '__main__':
    main()
