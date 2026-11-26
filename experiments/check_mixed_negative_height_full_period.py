#!/usr/bin/env python3
"""Exact negative-height conditional reflection and full-period phase identities."""
import argparse
import hashlib
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT/'notes/research_mixed_negative_height_full_period.md'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision', type=int, default=320)
    parser.add_argument('--output', type=Path, default=ROOT/'repro/results/research-mixed-negative-height-full-period.json')
    args = parser.parse_args()
    assert args.precision >= 128
    proof_hash, script_hash = sha(PROOF), sha(__file__)
    dependencies = {}
    sine_proof = 'notes/exact_factorial_interpolation_and_complex_contours.md'
    dependencies[sine_proof] = sha(ROOT/sine_proof)
    for stem in ['mixed_global_cotangent_roots', 'mixed_real_conditional_contour_geometry']:
        proof = 'notes/research_'+stem+'.md'
        script = 'experiments/check_'+stem+'.py'
        result = 'repro/results/research-'+stem.replace('_', '-')+'.json'
        for path in (proof, script, result):
            dependencies[path] = sha(ROOT/path)
        record = json.loads((ROOT/result).read_text())
        assert record['status'] == 'passed'
        assert record['proof_sha256'] == dependencies[proof]
        assert record['script_sha256'] == dependencies[script]
        for path, digest in record.get('dependencies', record.get('dependencies_sha256', {})).items():
            assert sha(ROOT/path) == digest
            dependencies[path] = digest

    exact = []

    def zero(name, expr, trigonometric=False):
        expr = sp.expand_trig(expr) if trigonometric else expr
        assert sp.trigsimp(sp.cancel(sp.expand(expr))) == 0, name
        exact.append(name)

    R, x, c = sp.symbols('R x c', real=True)
    A = 1+R**2-2*R*sp.cos(x+c)
    B = 1+R**2-2*R*sp.cos(x-c)
    zero('squared modulus difference', A-B-4*R*sp.sin(x)*sp.sin(c), True)
    zero('uniform squared modulus upper bound', (1+R)**2-A-2*R*(1+sp.cos(x+c)), True)
    z = R*(sp.cos(x)-sp.I*sp.sin(x))
    hessian = 2*sp.pi*sp.I*z/(1-z)
    zero('real primitive Hessian', sp.re(sp.expand_complex(hessian))-2*sp.pi*R*sp.sin(x)/(1+R**2-2*R*sp.cos(x)), True)
    aa, bb, xx = sp.symbols('a b xx', real=True)
    bound = R*sp.sin(2*sp.pi*xx)*(1-sp.cos(2*sp.pi*aa))/(sp.pi*(1+R)**2)
    zero('integrated second-difference lower bound', sp.diff(bound, aa)-2*R*sp.sin(2*sp.pi*xx)*sp.sin(2*sp.pi*aa)/(1+R)**2)
    t = sp.symbols('t', positive=True)
    logarithmic_gap = sp.log(t)-1+1/t
    zero('elementary logarithmic inequality derivative', sp.diff(logarithmic_gap, t)-(t-1)/t**2)
    assert logarithmic_gap.subs(t, 1) == 0
    exact.append('elementary logarithmic inequality initial value')
    Ja, Jma, Jb, Jmb, Jx, eps, constant = sp.symbols('Ja Jma Jb Jmb Jx eps constant', real=True)
    left = Ja+Jb-(2+eps)*Jx+constant
    right = -Jma-Jmb+(2+eps)*Jx+constant
    Da, Db = Ja+Jma-2*Jx, Jb+Jmb-2*Jx
    zero('same-type reflection including chirp constant', left-right-Da-Db+2*eps*Jx)
    low_four = Ja+Jb-3*Jx+constant
    high_three = -Jma-Jmb+2*Jx+constant
    zero('forcing-branch mixed reflection', low_four-high_three-Da-Db+Jx)
    y, a, s = sp.symbols('y a s', real=True)
    zero('real chirp independent of horizontal position', sp.re(2*sp.pi*sp.I*a*(x+sp.I*y))+2*sp.pi*a*y)
    zero('full-period original chirp increment', 2*sp.pi*sp.I*a*(s+1)-2*sp.pi*sp.I*a*s-2*sp.pi*sp.I*a)
    zero('full-period real chirp increment', sp.re(2*sp.pi*sp.I*a))
    zero('single Fourier harmonic oddness', sp.sin(-x)+sp.sin(x), True)
    N = sp.symbols('N', positive=True, real=True)
    phase = lambda w: -sp.I*sp.pi*w*(w+1)/(2*N)+sp.I*sp.pi*w/2
    zero('negative-root factorial phase increment', phase(s+1)-phase(s)+sp.I*sp.pi*(s+1)/N-sp.I*sp.pi/2)
    zero('finite factorial modulus exponent', sp.re(phase(N*(x+sp.I*y)))-sp.pi*N*y*(x-sp.Rational(1,2))-sp.pi*y/2)
    P_ratio = lambda z: sp.pi*N*y*(2*z-1)+sp.pi*y
    row_ratio = 4*sp.pi*N*a*y-P_ratio(x+a)-P_ratio(x+bb)+(2+eps)*P_ratio(x)
    expected_ratio = 2*sp.pi*N*y*(a-bb+eps*(x-sp.Rational(1,2)))+eps*sp.pi*y
    zero('finite original-row modulus reflection', row_ratio-expected_ratio)
    zero('upper alias finite relative exponent', -row_ratio-2*sp.pi*N*y+2*sp.pi*N*y*(1+a-bb+eps*(x-sp.Rational(1,2)))+eps*sp.pi*y)

    assert sha(PROOF) == proof_hash and sha(__file__) == script_hash
    assert all(sha(ROOT/path) == digest for path, digest in dependencies.items())
    result = {'status': 'passed', 'precision_bits': args.precision,
              'computational_scope': 'Exact symbolic identities only; precision flag is retained for reproduction consistency, not used as a numerical proof premise.',
              'exact_identity_count': len(exact), 'exact_identities': exact,
              'proof_sha256': proof_hash, 'script_sha256': script_hash, 'dependencies': dependencies,
              'scope': 'Full-period negative-height phase reflection, both endpoint phase joins, and the extra Fourier forcing rate. No complete finite interpolation, wrapped-term estimate, or source lower bound.'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS', len(exact), 'exact identities; no sampled extrema')


if __name__ == '__main__':
    main()
