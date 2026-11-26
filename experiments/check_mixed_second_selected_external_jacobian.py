#!/usr/bin/env python3
"""Differentiate the original logarithmic gradient and check its provider Jacobian."""
import argparse
import hashlib
import json
from pathlib import Path

import sympy as s
import mixed_second_selected_external_reference as reference
from certify_mixed_second_selected_canonical_reference import gradient


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    root = Path(__file__).resolve().parents[1]
    files = ['experiments/mixed_second_selected_external_reference.py',
             'experiments/certify_mixed_second_selected_canonical_reference.py',
             'notes/research_mixed_second_selected_external_reference_evaluation.md',
             'experiments/check_mixed_second_selected_external_jacobian.py']
    digest = lambda name: hashlib.sha256((root/name).read_bytes()).hexdigest()
    bindings = {name: digest(name) for name in files}
    q = s.symbols('e xi a u z v b')
    c = s.symbols('c')
    forms = {name: s.Rational(constant.numerator, constant.denominator)
             + sum(a*x for a, x in zip(row, (*q, c)))
             for name, (constant, row) in reference.FORMS.items()}
    k = {name: s.pi*s.cos(s.pi*w)/s.sin(s.pi*w) for name, w in forms.items()}
    cases = []
    for beta in (0, 1):
        original = gradient(q, c, beta, s.Integer, s.log, s.sin, s.cos, s.pi, s.I)
        H, fc = reference.jacobian_from_k(k, beta, s.pi, s.I)
        for i in range(7):
            for j in range(7):
                difference = s.trigsimp(s.diff(original[i], q[j])-H[i][j])
                if difference != 0:
                    raise ValueError((beta, i, j, str(difference)))
            difference = s.trigsimp(s.diff(original[i], c)-fc[i])
            if difference != 0:
                raise ValueError((beta, i, 'external derivative', str(difference)))
        cases.append({'beta': beta, 'jacobian_entries': 49, 'external_derivatives': 7})
    if any(digest(name) != value for name, value in bindings.items()):
        raise ValueError('symbolic-check input changed')
    record = {'status': 'all original-gradient derivative identities proved symbolically',
              'cases': cases, 'identity_count': 112, 'input_sha256': bindings,
              'root_evaluations': 0, 'parameter_evaluations': 0,
              'finite_source_evaluations': 0}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as stream:
        stream.write(json.dumps(record, indent=2)+'\n')
    print(json.dumps({'status': record['status'], 'identity_count': 112,
                      'output_sha256': hashlib.sha256(args.output.read_bytes()).hexdigest()}))


if __name__ == '__main__':
    main()
