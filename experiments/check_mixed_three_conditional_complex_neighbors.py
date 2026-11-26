#!/usr/bin/env python3
"""Check exact interpolation data for the complex-neighbor conditional packet.

The Gamma comparisons are finite diagnostics of the actual off-real
interpolant. They do not certify the uniform contour proof or a remaining
mixed-word sum. Exact identities and upstream provenance are checked
separately.
"""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def sine_factorial(N: int, z):
    """Finite Barnes formula for the original G_N, with its scalar fixed."""
    result = mp.exp(z*mp.log(2*mp.pi/N))*mp.gamma(z+1)
    for rr in range(N):
        result *= (mp.barnesg(1+(rr-z)/N)
                   /mp.barnesg(1+(rr+z+1)/N))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dps', type=int, default=80)
    parser.add_argument('--output', type=Path, default=ROOT/
        'repro/results/research-mixed-three-conditional-complex-neighbors.json')
    args = parser.parse_args()
    mp.mp.dps = args.dps
    exact = []

    def identity(name, expression):
        value = sp.simplify(sp.expand(expression))
        assert value == 0, (name, value)
        exact.append(name)

    N, alpha, beta, w, h = sp.symbols('N alpha beta w h', nonzero=True)
    s = sp.Rational(1, 2)+sp.I*w/(2*sp.pi)
    phase = N*alpha*w/2-sp.I*sp.pi*N*alpha**2/2-sp.I*sp.pi*alpha/2
    identity('exact one-step interpolation prefactor',
             phase.subs(alpha, alpha+1/N)-phase
             -(w/2-sp.I*sp.pi*(alpha+1/N)))
    identity('sine recurrence prefactor has no additional sign',
             sp.I*sp.pi/2-sp.I*sp.pi*(s+alpha+1/N)
             -(w/2-sp.I*sp.pi*(alpha+1/N)))
    a = sp.symbols('a', integer=True, nonnegative=True)
    identity('original integer prefactor', phase.subs(alpha, a/N)
             -(a*w/2-sp.I*sp.pi*a*(a+1)/(2*N)))
    phi = lambda x: sp.pi*(x-x*x)/2
    identity('regular-strip leading primitive',
             sp.I*(phi(s+alpha)-phi(s))
             -(alpha*w/2-sp.I*sp.pi*alpha**2/2))
    identity('conditional absolute action carrier',
             -alpha*w+sp.I*sp.pi*alpha-2*sp.pi*sp.I*alpha*s)
    identity('local square-root mark',
             -sp.I*sp.pi*(s+alpha)+sp.I*sp.pi*s+sp.I*sp.pi*alpha)
    q0 = sp.symbols('q0')
    identity('critical lift fixes endpoint symbol',
             (-q0/(sp.pi*sp.I)-alpha)*(-sp.pi*sp.I)
             -(q0+sp.pi*sp.I*alpha))
    identity('Gaussian N power', 1-sp.Rational(1, 2)-sp.Rational(1, 2))
    identity('vertical contour orientation',
             sp.I/(2*sp.pi*sp.I)-1/(2*sp.pi))
    k = sp.symbols('k', positive=True)
    identity('summable digamma first correction',
             (1/(k+s)-1/(k-s))/2+s/(k*k-s*s))
    identity('central factorial real-part minimum at reference box',
             sp.Rational(1, 2)-sp.Rational(9, 40)-sp.Rational(11, 40))
    identity('central shifted factorial real-part maximum',
             sp.Rational(1, 2)-sp.Rational(1, 10)+sp.Rational(9, 20)
             -sp.Rational(17, 20))

    diagnostics = []
    tolerance = mp.mpf(10)**(-args.dps+15)
    for level in (2, 3, 4, 6):
        rr = mp.exp(-2j*mp.pi/level)
        for height in (mp.mpf('-.2'), mp.mpf('.2')):
            for angle in (mp.mpf('-.5'), mp.mpf('1'),
                          mp.mpf('3'), mp.mpf('5.5')):
                ww = height+1j*angle
                ss = mp.mpf('.5')+1j*ww/(2*mp.pi)
                base = sine_factorial(level, level*ss)
                actual = mp.mpc(1)
                for degree in range(level):
                    if degree:
                        actual *= 1+mp.exp(ww)*rr**degree
                    interpolation = (
                        mp.exp(degree*ww/2
                               -1j*mp.pi*degree*(degree+1)/(2*level))
                        *sine_factorial(level, level*ss+degree)/base)
                    error = abs(interpolation/actual-1)
                    assert error < tolerance, (level, degree, ww, error)
                    diagnostics.append({
                        'N': level, 'degree': degree,
                        'circle_height': str(height), 'lifted_angle': str(angle),
                        'scaled_factorial_real_part': str(ss.real),
                        'relative_error': str(error)})

    upstream_records = [
        'repro/results/research-mixed-conditional-leg-sum.json',
        'repro/results/research-mixed-three-conditional-circle.json',
    ]
    provenance = []
    for name in upstream_records:
        record = json.loads((ROOT/name).read_text())
        assert record['status'] == 'passed', name
        script = ('experiments/check_mixed_conditional_leg_sum.py'
                  if 'leg-sum' in name else
                  'experiments/check_mixed_three_conditional_circle.py')
        assert record['script_sha256'] == sha256((ROOT/script).read_bytes()).hexdigest(), script
        for path, digest in record['dependencies_sha256'].items():
            assert digest == sha256((ROOT/path).read_bytes()).hexdigest(), path
        provenance.append({'record': name, 'script': script,
                           'status': 'all recorded source hashes current'})

    dependencies = [
        'notes/research_mixed_three_conditional_complex_neighbors.md',
        'notes/research_mixed_three_conditional_circle.md',
        'notes/research_mixed_conditional_leg_sum.md',
        'notes/exact_factorial_interpolation_and_complex_contours.md',
        'experiments/check_mixed_three_conditional_circle.py',
        'experiments/check_mixed_conditional_leg_sum.py',
        *upstream_records,
    ]
    result = {
        'status': 'passed', 'precision_decimal_digits': args.dps,
        'exact_identity_count': len(exact), 'exact_identities': exact,
        'finite_interpolation_diagnostic_count': len(diagnostics),
        'finite_interpolation_diagnostics': diagnostics,
        'maximum_relative_error': str(max(mp.mpf(row['relative_error'])
                                          for row in diagnostics)),
        'upstream_provenance_count': len(provenance),
        'upstream_provenance': provenance,
        'scope': ('Exact phase/normalization algebra and finite diagnostics of '
                  'the actual shifted sine-factorial ratio over both off-real '
                  'half-planes, including scaled real parts outside (0,1). '
                  'The uniform full-contour continuation is proved in the note; '
                  'no remaining neighbor sum or mixed-word lower theorem is checked.'),
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependencies_sha256': {path: sha256((ROOT/path).read_bytes()).hexdigest()
                                for path in dependencies},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in (
        'status', 'exact_identity_count', 'finite_interpolation_diagnostic_count',
        'maximum_relative_error', 'upstream_provenance_count')}))


if __name__ == '__main__':
    main()
