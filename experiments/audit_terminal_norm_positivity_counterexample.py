#!/usr/bin/env python3
"""Exact counterexample to Newton norm positivity under N >= 2|n|.

Computes in Q[q]/(q^16-q^8+1), q=exp(pi*i/24). The result is a
strictly negative sum of positive cosines, so no numerical sign test
is used. Requires SymPy.
"""
import json

import sympy as sp
from sympy.polys.domains import QQ


def main():
    level, power, output_index = 24, 9, 3
    x = sp.Symbol('x')
    field = QQ.alg_field_from_poly(
        sp.Poly(x**16-x**8+1, x), alias='q')
    q = field([1, 0])
    Q = q*q
    factorial = [field.one]
    for k in range(1, level):
        factorial.append(factorial[-1]*(1-Q**k))
    crossing = [
        [(-1)**k*q**(k+j*j)*factorial[k]
         / (factorial[j]*factorial[k-j]) for j in range(k+1)]
        for k in range(level)
    ]
    vector = [field.one]+[field.zero]*(level-1)
    for _ in range(power):
        vector = [sum((crossing[k][j]*vector[j] for j in range(k+1)),
                      field.zero) for k in range(level)]
    # These are H_n coefficients with the unit factor kappa**n omitted.
    terminal = vector[::-1]

    def conjugate(value):
        result, inverse = field.zero, q**-1
        for coefficient in value.to_list():
            result = result*inverse+field(coefficient)
        return result

    coefficient = field.zero
    r = output_index
    for i in range(r+1):
        for j in range(r+1):
            if i+j < r:
                continue
            multiplication = (
                q**(i*i-2*i*r+j*j-2*j*r+r*r)
                * factorial[i+j]*factorial[r]
                / (factorial[i]*factorial[j]*factorial[r-i]
                   * factorial[r-j]*factorial[i+j-r])
            )
            coefficient += terminal[i]*conjugate(terminal[j])*multiplication
    cosine_coefficients = {
        1: 930022046, 3: 998071796, 5: 998071796,
        7: 930022046, 9: 667276414, 11: 227489320,
    }
    negative_sum = -sum(
        (weight*(q**index+q**(-index))/2
         for index, weight in cosine_coefficients.items()), field.zero)
    assert coefficient == conjugate(coefficient)
    assert coefficient == negative_sum
    assert level >= 2*power
    assert all(weight > 0 and 0 < index < level/2
               for index, weight in cosine_coefficients.items())
    print(json.dumps({
        'level': level,
        'power': power,
        'Newton_index': output_index,
        'exact_field_relation': 'q^16-q^8+1=0; q=exp(pi*i/24)',
        'negative_cosine_sum': {
            str(index): weight for index, weight in cosine_coefficients.items()
        },
        'interpretation': '-sum(weight[index]*cos(index*pi/24))',
        'all_cosines_strictly_positive': True,
        'coefficient_strictly_negative': True,
        'N_at_least_2n': True,
        'passed': True,
    }, indent=2))


if __name__ == '__main__':
    main()
