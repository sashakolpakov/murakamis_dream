#!/usr/bin/env python3
"""Check the ordered two-strand transport as exact rational matrices.

This verifies a local algebraic statement. It does not verify the
identification of the corresponding paths in a global knot diagram.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sympy as s


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    lam, alpha, beta, scale = s.symbols('lambda alpha beta scale', nonzero=True)
    A = s.Matrix([[lam, alpha], [0, 1/lam]])
    B = s.Matrix([[1/lam, 0], [beta, lam]])
    P = B*A
    K = P.inv()-s.eye(2)
    delta = s.factor(K.det())
    swap = s.Matrix([[1,0,0,0], [0,0,1,0], [0,1,0,0], [0,0,0,1]])
    records = []

    def check(name, expression):
        entries = list(expression) if isinstance(expression, s.MatrixBase) else [expression]
        residuals = [s.cancel(x) for x in entries]
        if any(x != 0 for x in residuals):
            raise AssertionError((name, residuals))
        records.append({'name': name, 'entries': len(entries)})

    def pair(g):
        return (g.det()*s.kronecker_product(g.inv()*A.inv(), g.inv())*swap).applyfunc(s.cancel)

    R = pair(K)
    check('equal puncture traces', s.trace(A)-s.trace(B))
    check('regular determinant', delta-(2-s.trace(P)))
    check('ordered K B = A K', K*B-A*K)
    check('ordered first Hurwitz image', K*A*K.inv()-A.inv()*B*A)
    check('K preserves disk longitude', K*P-P*K)
    check('projective half-longitude', K*K+delta*P.inv())
    check('full twist on both tensor factors', R*R-s.kronecker_product(A,B))
    check('projective scale independence', pair(scale*K)-R)
    check('transport determinant', R.det()+1)

    h = lam-1/lam
    ap, am = s.Matrix([1,0]), s.Matrix([-alpha,h])
    bp, bm = s.Matrix([0,1]), s.Matrix([h,-beta])
    for name, C, v, value in [('A plus',A,ap,lam),('A minus',A,am,1/lam),
                             ('B plus',B,bp,lam),('B minus',B,bm,1/lam)]:
        check(name+' eigenvector', C*v-value*v)
    states = [s.kronecker_product(x,y) for x,y in [(ap,bp),(ap,bm),(am,bp),(am,bm)]]
    targets = [-lam*states[0], -lam*beta/alpha*states[2],
               -alpha/(lam*beta)*states[1], -states[3]/lam]
    for name, state, target in zip(['++','+-','-+','--'], states, targets):
        check('half twist on '+name, R*state-target)
    check('equal-line raw tensor comparison',
          s.kronecker_product(K*ap,K*bp)/delta+s.kronecker_product(A.inv()*bp,ap)/lam)

    # The operator itself is regular at the parabolic value; its chosen
    # eigenvector basis is deliberately not used for this evaluation.
    R0 = R.subs(lam,1)
    for entry in R0:
        if entry.has(s.zoo,s.nan,s.oo,-s.oo):
            raise AssertionError('singular parabolic operator')
    check('parabolic full twist', R0*R0-s.kronecker_product(A.subs(lam,1),B.subs(lam,1)))
    check('inverse twist', R.inv()*R-s.eye(4))
    result = {
        'scope':'Local rational transport only; no global peripheral identification.',
        'count':len(records),
        'scalar_entries':sum(r['entries'] for r in records),
        'checks':records,
        'all_exact':True,
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['count','scalar_entries','all_exact']}))


if __name__ == '__main__':
    main()
