#!/usr/bin/env python3
"""Outward checks of four scalar derivative bounds; no source or root search."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_selected_boundary_optimizer_bounds.md'
PARTS = 128


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ar(value):
    q = F(value)
    return arb(q.numerator) / q.denominator


def pieces(lo, hi):
    lo, hi = F(lo), F(hi)
    for j in range(PARTS):
        a = lo + (hi-lo)*j/PARTS
        b = lo + (hi-lo)*(j+1)/PARTS
        yield a, b, ar(a).union(ar(b))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision', type=int, default=192)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    assert args.precision >= 192
    assert not args.output.exists(), 'use a fresh output path'
    ctx.prec = args.precision
    pi, ii = arb.pi(), acb(0, 1)
    proof_hash, script_hash = sha(PROOF), sha(__file__)
    dependencies = {
        name: sha(ROOT/name) for name in (
            'notes/research_mixed_first_cap_height_tangent.md',
            'notes/research_mixed_first_cap_plateau_phase.md',
            'notes/research_mixed_first_four_attached_height_bound.md',
            'repro/results/research-mixed-first-four-attached-height-bound.json',
        )
    }
    height_record = json.loads((ROOT /
        'repro/results/research-mixed-first-four-attached-height-bound.json').read_text())
    assert height_record['status'] == 'passed'
    assert height_record['uniform_height_lower'] == '-39/500'
    assert height_record['next_three_height_lower'] == '-7/100'
    assert height_record['proof_sha256'] == dependencies[
        'notes/research_mixed_first_four_attached_height_bound.md']

    def log_abs_sine(v):
        value = abs(2*(pi*v).sin())
        assert value > 0
        return value.log()

    def gp_real(v):
        value = abs(1-(-2*pi*ii*v).exp())
        assert value > 0
        return value.log()

    checks = []
    for lo, hi, height in pieces('-.051', '-.019'):
        e, z = acb(ar('.4'), height), acb(ar('.22'), ar('.014'))
        disc = 1-2*(2*pi*ii*e).exp()
        assert disc.real > 1
        u = ((ii+disc.sqrt())/2).atan()/pi
        assert u.is_finite()
        assert u.real > 0 and u.real < ar('.5')
        assert (e-u).real > 0 and (e-u).real < ar('.5')
        derivative = (-log_abs_sine(e-u)-pi*u.imag
                      +log_abs_sine(e+z)+pi*z.imag
                      -log_abs_sine(e)-pi*e.imag)
        assert derivative < -ar('1/20'), (lo, hi, derivative)
        checks.append(dict(kind='e_upper', height=[str(lo), str(hi)],
                           upper=str(derivative.upper()), threshold='-1/20'))

    cases = [
        ('s_four_upper', 1, '.44', '.22', '-1/25'),
        ('sum_three_upper', 0, '.40', '.45', '-1/100'),
        ('sum_four_upper', 1, '.37', '.45', '-1/25'),
    ]
    for kind, epsilon, sx, zx, threshold in cases:
        low, high = ('-.072', '.068') if epsilon == 0 else ('-.108', '-.001')
        k_low = '-.070' if epsilon == 0 else '-.078'
        for k in (k_low, '.014'):
            for hb in ('-.108', '.068'):
                z, b = acb(ar(zx), ar(k)), acb(ar('.22'), ar(hb))
                for lo, hi, height in pieces(low, high):
                    s = acb(ar(sx), height)
                    derivative = (gp_real(s+z)+gp_real(s+b)
                                  -(2+epsilon)*gp_real(s)-2*pi*z.imag)
                    assert derivative < ar(threshold), (kind, k, hb, lo, hi, derivative)
                    checks.append(dict(kind=kind, height=[str(lo), str(hi)],
                                       k=k, hb=hb, upper=str(derivative.upper()),
                                       threshold=threshold))
    assert len(checks) == 13*PARTS

    # Exact polynomial calculation used in Proposition 3.
    def multiply(p, q):
        out = [F(0)]*(len(p)+len(q)-1)
        for i, a in enumerate(p):
            for j, b in enumerate(q):
                out[i+j] += a*b
        return out

    base = [F(1), F(8, 5), F(1)]
    lhs = multiply(multiply(base, base), base)
    rhs = multiply([F(1), F(9, 10), F(81, 100)], [F(4), F(4), F(1)])
    poly = [a-(rhs[i] if i < len(rhs) else F(0)) for i, a in enumerate(lhs)]
    expected = [F(-3), F(-14, 5), F(71, 25), F(2389, 250),
                F(987, 100), F(24, 5), F(1)]
    assert poly == expected
    r = F(3, 5)
    value = sum(a*r**i for i, a in enumerate(poly))
    slope = sum(i*a*r**(i-1) for i, a in enumerate(poly) if i)
    assert value == F(6597, 62500) and slope > 0
    assert all(a > 0 for a in poly[2:])
    assert sha(PROOF) == proof_hash and sha(__file__) == script_hash
    assert all(sha(ROOT/name) == digest for name, digest in dependencies.items())
    result = dict(status='passed', precision=args.precision,
                  scope='central-phase optimizer exclusions for actual mixed words m>=3',
                  subdivisions_per_height_interval=PARTS, scalar_checks=len(checks),
                  new_coupled_roots=0, source_comparisons_repeated=0,
                  proof_sha256=proof_hash, script_sha256=script_hash,
                  dependencies_sha256=dependencies, tests=checks,
                  polynomial_coefficients=list(map(str, poly)),
                  polynomial_value=str(value), polynomial_slope=str(slope))
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('Completed:', len(checks), 'outward scalar checks and exact polynomial identity.')


if __name__ == '__main__':
    main()
