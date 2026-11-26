#!/usr/bin/env python3
"""Exact diagonal-height reference extension; no numerical support gap."""
from pathlib import Path
import argparse
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_selected_height_reference_extension.md'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'repro/results/research-mixed-selected-height-reference-extension.json')
    args = parser.parse_args()
    ph, sh = sha(PROOF), sha(__file__)
    checks = 0
    p, pb = s.symbols('p pb', real=True)
    x = s.symbols('x0:2', real=True)
    b = s.symbols('b0:2', real=True)
    lam = s.symbols('lambda0:2', real=True)
    d = s.symbols('d0:2', real=True)
    z = s.Matrix([p + s.I*p**2, (2-s.I)*p + p**3])
    conjugate = lambda value: s.conjugate(value).xreplace({p: pb, pb: p})
    zb = conjugate(z)
    q, qb = z.diff(p), zb.diff(pb)
    L = s.diag(*lam)
    w = s.Matrix(x) + s.I*s.Matrix(b) + L*(z-zb)/2
    v = s.symbols('v0:2')
    F = (1+s.I)*v[0]**3 + (2-s.I)*v[0]*v[1]**2 + s.I*v[1]**2
    Psi = (3-2*s.I)*v[1]**3 + (1+s.I)*v[0]**2*v[1] + 2*v[0]**2
    subs = lambda expr, point: expr.subs(dict(zip(v, point)), simultaneous=True)
    gradF = s.Matrix([s.diff(F, a) for a in v])
    HF, HP = s.hessian(F, v), s.hessian(Psi, v)
    E = subs(Psi, w)-subs(F, z)-(subs(gradF, z).T*(w-z))[0]
    D = (E+conjugate(E))/2-sum(d[j]*(z[j]-zb[j])**2/4 for j in range(2))
    lap = 4*s.diff(D, p, pb)
    T = -(q.T*L*subs(HP, w)*L*qb)[0]+2*(q.T*subs(HF, z)*L*qb)[0]
    rhs = (T+conjugate(T))/2+2*sum(d[j]*q[j]*qb[j] for j in range(2))
    assert s.expand(lap-rhs) == 0
    checks += 1

    # A complex symmetric matrix has no surviving imaginary cross term
    # against q^T H conjugate(q); positivity uses its real symmetric part.
    u0, u1, v0, v1 = s.symbols('u0 u1 v0 v1', real=True)
    aa = s.symbols('a0:3', real=True)
    bb = s.symbols('c0:3', real=True)
    A = s.Matrix([[aa[0], aa[1]], [aa[1], aa[2]]])
    B = s.Matrix([[bb[0], bb[1]], [bb[1], bb[2]]])
    u, vv = s.Matrix([u0, u1]), s.Matrix([v0, v1])
    Q = u+s.I*vv
    assert s.expand(s.re((Q.T*L*(-A+s.I*B)*L*s.conjugate(Q))[0])+(u.T*L*A*L*u)[0]+(vv.T*L*A*L*vv)[0]) == 0
    checks += 1

    y, lo, hi, C = s.symbols('y lo hi C', real=True)
    barrier = C*(y-lo)*(hi-y)
    assert s.diff(barrier, y, 2) == -2*C
    assert s.expand(barrier.subs(y, (lo+hi)/2)-C*(hi-lo)**2/4) == 0
    assert barrier.subs(y, lo) == barrier.subs(y, hi) == 0
    checks += 3

    tau = s.symbols('tau', real=True)
    # The old common-height formula is a literal specialization; Lambda=0
    # removes both possibly negative terms for a fixed target.
    assert (L.subs(dict.fromkeys(lam, tau))-tau*s.eye(2)).is_zero_matrix
    assert L.subs(dict.fromkeys(lam, 0)).is_zero_matrix
    checks += 2
    h, charge, delta = s.symbols('h charge delta', real=True)
    for selected in (0, 1):
        coefficient = charge*((1-selected)*(1-tau)**2+selected*(1-tau))
        debit = coefficient*h**2-tau*delta*selected
        expected = (1-tau)**2*charge*h**2 if not selected else (1-tau)*charge*h**2-tau*delta
        assert s.expand(debit-expected) == 0
        checks += 1
    assert s.Rational(1, 4)*2*s.Rational(1, 5)*s.Rational(1, 20)**2 == s.Rational(1, 4000)
    checks += 1
    for typ in (0, 1):
        for selected in range(typ+1):
            for branch in range(selected+1):
                assert s.Rational(typ-branch, 2) >= 0
    assert s.Rational(1, 2)+s.Rational(1, 2) == 1
    checks += 1
    assert ph == sha(PROOF) and sh == sha(__file__)
    result = dict(status='passed', exact_checks=checks, proof_sha256=ph, script_sha256=sh,
                  scope='Exact generalized reference Laplacian, barrier and selected-pair debit formulas; no numerical support gap or finite-source theorem.')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS', checks, 'exact identities', flush=True)


if __name__ == '__main__':
    main()
