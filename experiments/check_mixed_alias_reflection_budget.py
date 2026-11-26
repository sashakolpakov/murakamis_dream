#!/usr/bin/env python3
"""Exact phase algebra and outward local alias-height reserves.

No full outer-contour or conditional-tail estimate is checked here.
"""
import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp
from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[1]


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=256)
    ap.add_argument('--output', type=Path, default=ROOT /
                    'repro/results/research-mixed-alias-reflection-budget.json')
    args = ap.parse_args()
    ctx.prec = args.precision
    pi = arb.pi()
    strict = []

    def positive(name, margin):
        assert margin > 0, (name, str(margin))
        strict.append({'name': name, 'strict_margin': str(margin)})

    K = pi*(3*(27*pi/100).cot()+2*(11*pi/50).cot())
    c0 = (33*pi/50).sin()*arb(2).log()/(2*pi)
    c1 = 17*pi/50-(33*pi/50).sin()/2
    hmax = arb(57)/1000
    positive('moving four-leg height curvature is below sixteen', 16-K)
    positive('wrapped linear branch exceeds half-height loss',
             2*pi-arb(1)/2-32*hmax)
    positive('factorial branch quadratic at zero', c0)
    positive('factorial branch quadratic at maximum height',
             c0+(c1-arb(1)/2)*hmax-32*hmax*hmax)
    positive('stated maximum-height scalar reserve',
             c0+(c1-arb(1)/2)*hmax-32*hmax*hmax-arb(1135)/10000000)
    positive('weight epsilon leaves more than quarter-height loss',
             arb(1)/4000-arb(1)/8000)
    positive('strict reflected neighborhood still retains positive loss',
             arb(1)/4000-arb(1)/8000)

    identities = []
    phi = lambda z: sp.pi*(z-z*z)/2
    for m in (1, 2, 3):
        ss = sp.symbols(f's0:{m}')
        tt = sp.symbols(f't0:{m}')
        ee = sp.symbols(f'e0:{m}')
        carrier = sum(phi(ss[v]+tt[v])+phi(tt[v]+ss[(v+1) % m])
                      -(2+ee[v])*(phi(ss[v])+phi(tt[v]))
                      +2*sp.pi*tt[v]*ss[(v+1) % m] for v in range(m))
        theta = sum(sp.pi*tt[v]*(ss[(v+1) % m]-ss[v])
                    -ee[v]*(phi(ss[v])+phi(tt[v])) for v in range(m))
        assert sp.expand(carrier-theta) == 0
        identities.append(f'm{m}: exact original contracted phase conversion')
        F = sp.Function('g')
        full = sum(F(ss[v]+tt[v])+F(tt[v]+ss[(v+1) % m])
                   -(2+ee[v])*(F(ss[v])+F(tt[v]))
                   +2*sp.pi*sp.I*tt[v]*ss[(v+1) % m] for v in range(m))
        for a in range(m):
            for b in range(a+1, m):
                assert sp.diff(full, tt[a], tt[b]) == 0
                identities.append(f'm{m}: no outer Hessian cross entry {a},{b}')
    h, cc0, cc1 = sp.symbols('h cc0 cc1')
    assert sp.diff(cc0+(cc1-sp.Rational(1, 2))*h-32*h*h, h, 2) == -64
    identities.append('factorial-branch residual is concave on the full height interval')
    x = sp.symbols('x', positive=True)
    assert sp.simplify(sp.diff(sp.log(1+sp.exp(-x)), x, 2)
                       -sp.exp(x)/(1+sp.exp(x))**2) == 0
    identities.append('logarithmic height majorant has the stated convex tangent')
    eta = sp.Rational(1, 8000)
    assert sp.Rational(1, 2)*sp.Rational(1, 1000)-eta > sp.Rational(1, 4000)
    identities.append('true Fourier-weight cost absorbed at the smallest allowed height')

    paths = [
        'notes/research_mixed_alias_reflection_budget.md',
        'notes/research_mixed_contracted_phase.md',
        'notes/research_mixed_conditional_torus_composition.md',
        'notes/research_mixed_cyclic_critical_height_bounds.md',
        'notes/research_mixed_fourier_weight_continuation.md',
    ]
    out = {
        'status': 'passed', 'precision_bits': args.precision,
        'scope': 'Local exact-factorial density and actual Fourier-weight upper bound only; no full conditional or outer-complement estimate.',
        'exact_identity_count': len(identities), 'exact_identities': identities,
        'strict_comparison_count': len(strict), 'strict_comparisons': strict,
        'height_curvature_upper': str(K), 'weight_lower_constant': str(c0),
        'weight_lower_slope': str(c1), 'maximum_height': '57/1000',
        'weight_epsilon': '1/8000', 'point_gap_per_alias': '1/4000',
        'script_sha256': sha(__file__),
        'proof_sha256': sha(ROOT/paths[0]),
        'dependencies': {p: sha(ROOT/p) for p in paths[1:]},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2)+'\n')
    print(f'PASS {len(identities)} exact identities, {len(strict)} outward comparisons')


if __name__ == '__main__':
    main()
