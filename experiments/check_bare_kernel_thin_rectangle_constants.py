#!/usr/bin/env python3
"""Exact scalar inequalities used by the thin-rectangle kernel proof.

This checks rational Taylor bounds, not a finite sample of the kernel.
The analytic contour and parameter-uniform arguments are in the note.
"""

import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path


def alternating(x, odd, last):
    return sum(((-1) ** k * x ** (2 * k + odd)
                / math.factorial(2 * k + odd)
                for k in range(last + 1)), F(0))


def cos_lower(x):
    return alternating(x, 0, 7)


def sin_lower(x):
    return alternating(x, 1, 7)


def sin_upper(x):
    return alternating(x, 1, 6)


def hyperbolic_upper(x, odd):
    last = 8
    total = sum((x ** (2 * k + odd) / math.factorial(2 * k + odd)
                 for k in range(last + 1)), F(0))
    power = 2 * (last + 1) + odd
    first_tail = x ** power / math.factorial(power)
    ratio = x * x / ((power + 1) * (power + 2))
    assert 0 <= ratio < 1
    return total + first_tail / (1 - ratio)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', default=
                        'repro/results/research-bare-kernel-thin-rectangle.json')
    args = parser.parse_args()
    margins = {}

    def greater(name, left_lower, right_upper):
        margin = left_lower - right_upper
        assert margin > 0, (name, margin)
        margins[name] = {'numerator': str(margin.numerator),
                         'denominator': str(margin.denominator)}

    a1, b1 = F(10001, 10000), F(1, 190)
    greater('cos_one', cos_lower(F(1)), F(27, 50))
    greater('cosh_height', a1, hyperbolic_upper(F(1, 200), 0))
    greater('sinh_height', b1, hyperbolic_upper(F(1, 200), 1))
    greater('tangent_cosine_floor', cos_lower(F(101, 70)), F(1, 8))
    greater('saddle_real_lower', cos_lower(F(33, 25)), F(6, 25))
    greater('saddle_real_upper', sin_lower(F(3, 500)), F(1, 1000))
    greater('saddle_real_correction', F(1, 30000),
            b1*b1*(F(1, 3) + 4*a1/9 + F(4, 27)))
    greater('saddle_real_C_lower', F(1, 1000), F(1, 20000)+F(1, 30000))
    greater('saddle_real_C_upper', F(231, 1000), F(23, 100)+F(1, 30000))
    greater('saddle_imaginary_C', F(1, 200),
            2*b1*((1+a1)**2+b1*b1)/9)
    greater('saddle_sine_floor_squared', 1-F(231, 1000)**2, F(9, 10)**2)
    greater('saddle_height', F(1, 1000), F(1, 200)/(6*F(9, 10)))
    greater('tangent_height', F(9, 1000), F(11, 1750)+F(1, 400))
    greater('tangent_sinh', F(1, 100), hyperbolic_upper(F(9, 1000), 1))
    greater('cotangent_sinh', F(1, 100), hyperbolic_upper(F(11, 1750), 1))
    greater('tangent_real_attenuation', F(100, 99), 1+F(64, 10000))
    greater('cotangent_real_attenuation', F(100, 99), 1+F(4, 10000))
    greater('tangent_imaginary', F(3, 320),
            hyperbolic_upper(F(18, 1000), 1)/2)
    greater('cotangent_imaginary', F(13, 2000),
            hyperbolic_upper(F(22, 1750), 1)/2)
    greater('negative_real_Hessian', F(99, 100)*24, F(20))
    greater('imaginary_Hessian', F(8), F(22, 7)*(4*F(3, 5)+4*F(13, 500)))
    greater('modulus_Hessian', F(128), 40*F(22, 7))
    vertical = -10*F(3, 100)**2 + 8*F(3, 100)*F(3, 1000) + 64*F(3, 1000)**2
    greater('vertical_contour_gap', -F(7, 1000), vertical)
    horizontal = (64+F(64, 40))*F(3, 1000)**2
    greater('horizontal_excess', F(1, 1000), horizontal)
    greater('nonconstant_cotangent_gap', F(6, 500)-horizontal, F(1, 100))
    greater('low_wire_cosine', cos_lower(F(198, 175)), F(2, 5))
    greater('low_wire_sine_squared', F(3, 10), sin_upper(F(99, 175))**2)
    greater('half_angle_sine', F(12, 25), sin_upper(F(1, 2)))
    greater('half_angle_sinh', F(1, 300), hyperbolic_upper(F(1, 400), 1))
    greater('complex_half_angle_squared', F(6, 25), F(12, 25)**2+F(1, 300)**2)
    greater('upper_low_wire_ratio', F(19, 20), F(59, 65))
    greater('factorial_strip_margin', F(1, 5)-F(1, 6), F(3, 100))
    greater('high_half_gap', F(10, 11)-F(1, 100), F(89, 100))

    script = Path(__file__).resolve()
    note = script.parent.parent / 'notes/research_bare_kernel_thin_rectangle.md'
    record = {
        'status': 'passed', 'arithmetic': 'exact fractions',
        'scope': 'scalar inequalities only; analytic proof is in the linked note',
        'script_sha256': hashlib.sha256(script.read_bytes()).hexdigest(),
        'note_sha256': hashlib.sha256(note.read_bytes()).hexdigest(),
        'inequality_count': len(margins), 'strict_positive_margins': margins,
        'parameter_domain': {'abs_real': '1', 'abs_imaginary': '1/200'},
        'wire_interval': ['9/50', '3/10'], 'wire_height': '1/500',
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, indent=2) + '\n')
    print(f'passed {len(margins)} exact scalar inequalities; {output}')


if __name__ == '__main__':
    main()
