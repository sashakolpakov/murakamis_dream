#!/usr/bin/env python3
"""Exact minimum-cutoff contour bounds, with a strict cotangent enclosure."""
import argparse
import hashlib
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

import sympy as sp
from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_minimum_neighbor_contour.md'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision', type=int, default=256)
    parser.add_argument('--output', type=Path,
                        default=ROOT / 'repro/results/research-mixed-minimum-neighbor-contour.json')
    args = parser.parse_args()
    assert args.precision >= 128
    ctx.prec = args.precision
    ph, sh = sha(PROOF), sha(__file__)
    dependencies = {}
    for stem in ('mixed_coupled_outer_graph', 'mixed_selected_low_plateau_clusters',
                 'mixed_closed_cotangent_roots'):
        pp = f'notes/research_{stem}.md'
        ss = f'experiments/check_{stem}.py'
        rr = f'repro/results/research-{stem.replace("_", "-")}.json'
        for path in (pp, ss, rr):
            dependencies[path] = sha(ROOT / path)
        record = json.loads((ROOT / rr).read_text())
        assert record['status'] == 'passed'
        assert record['script_sha256'] == dependencies[ss]
        inherited = record.get('dependencies_sha256', record.get('dependencies', {}))
        assert record.get('proof_sha256', inherited.get(pp)) == dependencies[pp]
        for key in ('dependencies', 'dependencies_sha256'):
            assert all(sha(ROOT / p) == h for p, h in record.get(key, {}).items())

    x, a = sp.symbols('x a', real=True)
    rho = sp.Rational(25, 3) * (x-sp.Rational(1, 10))
    assert sp.expand(sp.Rational(125, 6)*x*x-rho
                     -sp.Rational(125, 6)*(x-sp.Rational(1, 5))**2) == 0
    ratio = (1-rho)/(a-x)
    assert sp.cancel(sp.diff(ratio, x)
                     -(sp.Rational(11, 50)-a)/(sp.Rational(3, 25)*(a-x)**2)) == 0
    assert sp.cancel(ratio.subs(x, sp.Rational(1, 10))-1/(a-sp.Rational(1, 10))) == 0
    assert ratio.subs({x: sp.Rational(1, 10), a: sp.Rational(3, 10)}) == 5
    assert ratio.subs({x: sp.Rational(1, 10), a: sp.Rational(27, 100)}) == sp.Rational(100, 17)
    assert F(57, 1000)*F(100, 17) == F(57, 170)
    assert 3*F(57, 170)**2 < F(9, 25)
    assert 1+F(57, 50)**2 < F(38, 25)**2
    assert F(121, 120)/F(11, 50)**2 == F(125, 6)
    pattern_count = 0
    for length in range(1, 11):
        for values in itertools.product((0, 1), repeat=length):
            for j in range(length):
                neighbors = [values[(j-1) % length], values[j], values[(j+1) % length]]
                assert min(neighbors) == neighbors[0]*neighbors[1]*neighbors[2]
            pattern_count += 1
        incidences = [sum(i in {(j-1) % length, j, (j+1) % length}
                          for j in range(length)) for i in range(length)]
        assert max(incidences) <= 3

    pi = arb.pi()
    cot_bound = arb(121)*(arb(57)*pi/500).sinh() / (240*(11*pi/50).sin()**2)
    assert cot_bound < arb(23)/50 < arb(1)/2
    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT / p) == h for p, h in dependencies.items())
    result = dict(
        status='passed', precision_bits=args.precision,
        exact_scalar_checks=9, cyclic_binary_patterns=pattern_count,
        sampled_length_range=[1, 10], cotangent_bound=str(cot_bound.upper()),
        secant_norm_upper_bound='3/5', jacobian_base_upper_bound='38/25',
        proof_sha256=ph, script_sha256=sh, dependencies_sha256=dependencies,
        scope='Exact periodic minimum-neighbor contour, unchanged low/plateau contribution, convex cotangent domains, and a length-independent height displacement bound. No transition source or global phase gap.'
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS 9 exact scalar checks,', pattern_count, 'binary patterns, strict cotangent bound')


if __name__ == '__main__':
    main()
