#!/usr/bin/env python3
"""Exact open-boundary spectral weights at original level three."""

from hashlib import sha256
import json
from pathlib import Path

import sympy as sp


def main():
    q = (1 + sp.I * sp.sqrt(3)) / 2
    kappa = sp.expand(q**2)
    # Defining original Newton formula, with S=(1,sqrt(3),3).
    factorial = (1, sp.sqrt(3), 3)
    M = sp.zeros(3)
    for j in range(3):
        for k in range(j+1):
            M[j,k] = sp.simplify(kappa*(-1)**j*q**(j*(k+1))
                                  *factorial[j]/(factorial[k]*factorial[j-k]))
    J = sp.Matrix([[0,0,1], [0,1,0], [1,0,0]])
    v = sp.Matrix([1,1,0])
    B = sp.simplify(J*M**3/kappa)
    lam = sp.symbols('lambda')
    checks = []

    def equal(name, expression):
        assert sp.simplify(sp.expand_complex(expression)) == 0, name
        checks.append(name)

    equal('original characteristic polynomial',
          B.charpoly(lam).as_expr()-(lam-1)*(lam**2-5*lam+1))
    a = sp.sqrt(3)/2+5*sp.sqrt(7)/14
    b = sp.sqrt(3)/2-5*sp.sqrt(7)/14
    lp, lm = (5+sp.sqrt(21))/2, (5-sp.sqrt(21))/2
    phase = (sp.sqrt(3)-sp.I)/2
    for m in range(3):
        equal(f'original boundary moment {m}',
              phase*(v.T*B**m*v)[0] - (a*lp**m+b*lm**m-sp.I))
    equal('opposite weight product', a*b+sp.Rational(1,7))
    equal('unit eigenvalue',
          sp.det(B-sp.eye(3)))
    recurrence = B**3-6*B**2+6*B-sp.eye(3)
    for j in range(3):
        for k in range(3):
            equal(f'full Cayley Hamilton recurrence {j}{k}', recurrence[j,k])

    rho = sp.simplify(M[1,1])
    equal('odd physical crossing square', rho**2-kappa)
    for j in range(3):
        equal(f'complete physical eigenfunctional {j}', (v.T*M-rho*v.T)[j])
    equal('complete identity-kernel normalization', (v.T*J*v)[0]-1)
    equal('negative moment normalization', rho*(v.T*B**-1*v)[0]-1)
    cplus, cminus = a/phase, b/phase
    equal('reciprocal spectral weight', cminus-rho**-2*lp**-2*sp.conjugate(cplus))

    z = sp.symbols('z', real=True)
    vz = sp.Matrix([1,(1-z)/3,(1-z)*(-2-z)/9])
    inverse = sp.simplify(M**-1)
    inverse_crossing = sp.simplify((vz.T*inverse[:,0])[0])
    residual = sp.simplify(vz.T*inverse-inverse_crossing*vz.T)
    for node, orders in ((1,(0,1)),(-2,(0,))):
        for order in orders:
            for j in range(3):
                equal(f'original inverse-crossing jet {node}/{order}/{j}',
                      sp.diff(residual[j],z,order).subs(z,node))
    root = Path(__file__).resolve().parents[1]
    proof = root/'notes/research_positive_three_crossing_cycle.md'
    result = {
        'status': 'passed', 'exact_identities': len(checks), 'checks': checks,
        'scope': 'Original N=3 open-boundary spectral weights; no large-level assertion.',
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'proof_sha256': sha256(proof.read_bytes()).hexdigest(),
        'dependencies_sha256': {
            name: sha256((root/name).read_bytes()).hexdigest()
            for name in (
                'notes/research_one_crossing_gaussian_window.md',
                'notes/research_terminal_powers_qbinomial.md',
                'notes/research_degree_three_zero_wire_tails.md',
            )
        },
    }
    output = root/'repro/results/research-positive-three-boundary-spectrum.json'
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(f'Passed {len(checks)} exact identities.\n{output}')


if __name__ == '__main__':
    main()
