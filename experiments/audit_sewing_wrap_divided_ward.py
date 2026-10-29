#!/usr/bin/env python3
"""Literal sewing wrap coupons under the full actual divided Hopf adjoint."""

import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_divided_ward_closure import actual_module, adjoint
from audit_finite_sum_annihilator import field


def case(N, generic):
    p, generator, root = field(N)
    q = generator if generic else root
    m, E, F, K = actual_module(N, 0, q, p)
    rho = (q-pow(q, -1, p)) % p
    diagonal = np.array([pow(-rho, j, p)*pow(q, j*(j+1)//2, p) % p for j in range(N)], dtype=np.int64)
    frame = diagonal[:, None]*np.array([pow(int(c), -1, p) for c in diagonal])[None, :] % p
    def gauge(pair):
        return pair[0]*frame % p, np.zeros((N, N), dtype=np.int64)
    Eb, Fb, Kb = list(map(gauge, E)), list(map(gauge, F)), gauge(K)
    Bp = np.zeros((N, N), dtype=np.int64); Bp[N-1, 0] = 1
    Bm = Bp.T
    const = lambda X: (X, np.zeros_like(X))
    imageE = adjoint(Eb, Kb, N, const(Bp), q, p, 'E')[0]
    imageF = adjoint(Fb, Kb, N, const(Bm), q, p, 'F')[0]
    Jp = np.zeros((N, N), dtype=np.int64)
    for j in range(N-1):
        Jp[j+1, j] = 1
    Jm = Jp.T
    S = Jp+Bm
    J = np.diag(np.arange(N, dtype=np.int64))
    z = 3
    if z % p == 0:
        z = 2
    Z = np.diag([pow(z, j, p) for j in range(N)])
    Zi = np.diag([pow(z, -j, p) for j in range(N)])
    assert np.array_equal(Z@S@Zi % p, (z*S+(pow(z, 1-N, p)-z)*Bm) % p)
    assert np.array_equal(Z@S.T@Zi % p, (pow(z, -1, p)*S.T+(pow(z, N-1, p)-pow(z, -1, p))*Bp) % p)
    polynomial = lambda j: j*j*j+2*j+1
    PJ = np.diag([polynomial(j) for j in range(N)])
    PJplus = np.diag([polynomial(j+1) for j in range(N)])
    PJminus = np.diag([polynomial(j-1) for j in range(N)])
    assert np.array_equal((PJ@S-S@PJplus) % p, (polynomial(0)-polynomial(N))*Bm % p)
    assert np.array_equal((PJ@S.T-S.T@PJminus) % p, (polynomial(N-1)-polynomial(-1))*Bp % p)
    L = N*(N-1)//2
    Mcol = -pow(q, N, p) % p
    G = [pow(Mcol, j, p)*int(E[j][0][0, j]) % p for j in range(N)]
    CE = pow(-rho, -N, p)*pow(q, -N*m-L, p) % p
    CF = pow(-1, m, p)*pow(-rho, N, p)*pow(q, L+1-m*m, p) % p
    assert np.array_equal(imageE, CE*Jm@np.diag(G) % p)
    assert np.array_equal(imageF, CF*Jp@np.diag(G) % p)
    if not generic:
        assert G == [1]*N
        assert CE == -pow(rho, -N, p)*pow(q, -L, p) % p
        assert CF == pow(-1, m, p)*pow(rho, N, p)*pow(q, L, p) % p
        assert np.array_equal(pow(-1, N, p)*np.kron(imageF, imageE) % p, np.kron(Jp, Jm))
    return dict(N=N, generic_q=generic, prime=p, q=q,
                whole_profile_G=G, CE=CE, CF=CF, actual_unit_transfer_identity=not generic,
                whole_clock_and_polynomial_endpoint_carries=True)


def mixed_source_witness():
    I = sp.I
    E, F, K = sp.Matrix([[0, sp.Rational(1, 2)], [0, 0]]), sp.Matrix([[0, 0], [2, 0]]), sp.diag(I, -I)
    ET = sp.kronecker_product(E, K)+sp.kronecker_product(sp.eye(2), E)
    FT = sp.kronecker_product(F, sp.eye(2))+sp.kronecker_product(K.inv(), F)
    KT = sp.kronecker_product(K, K)
    DE = I*sp.kronecker_product(E, E*K)
    DF = -I*sp.kronecker_product(K.inv()*F, F)
    Bm = sp.Matrix([[0, 1], [0, 0]]); Bp = Bm.T
    C = sp.kronecker_product(Bm, Bp)
    def AE(X):
        return sp.simplify(DE*X+I*ET*X*ET-X*DE)
    def AF(X):
        return sp.simplify(DF*X-I*FT*KT.inv()*X*KT*FT-X*DF)
    full = AF(AE(C))
    expected = sp.Matrix([[-I, 0, 0, 0], [0, -I, 1, 0], [0, 1, I, 0], [0, 0, 0, I]])
    assert full == expected
    independent = sp.kronecker_product(Bp, Bm)
    defect = full-independent
    R0 = sp.Matrix([[1, 0, 0, 0], [0, 0, -I, 0], [0, -I, 2, 0], [0, 0, 0, 1]])
    def phi(W):
        return sp.simplify(sum((-I, I)[k]*W[2*c+k, 2*a+k]
                               for a in range(2) for c in range(2) for k in range(2))/2)
    before, after = phi(defect*R0), phi(R0*defect)
    assert before == sp.Rational(1, 2) and after == -sp.Rational(1, 2)
    return dict(full_mixed_adjoint=str(full), independent_image=str(independent),
                original_cap_before_crossing=str(before), original_cap_after_crossing=str(after),
                full_Cartan_scalar='original kappa retained externally')


def source_endpoint():
    alpha, C, D, m, b = sp.symbols('alpha C D m b', nonzero=True)
    s = C*alpha**2
    r = (1+m)/2+D*alpha**2
    assert sp.simplify(r.subs(m, m+2*b*s)-r-b*s) == 0
    generator = sp.Matrix([[-1, 1], [-1, 1]])
    assert generator**2 == sp.zeros(2)
    return dict(exact_complete_meridian_endpoint='r -> r+s at b=1', generator='s(e-h-f)')


def main():
    cases = [case(N, generic) for N in range(2, 13) for generic in (False, True)]
    result = dict(status='PASS', current_cases=cases, actual_mixed_source_witness=mixed_source_witness(),
                  actual_paired_source_endpoint=source_endpoint(),
                  scope='Exact wrap/divided-adjoint and whole normal profile; mixed coproduct-to-geometric current fusion remains open.')
    Path(__file__).with_name('sewing_wrap_divided_ward_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(status='PASS', root_cases=11, whole_q_cases=11, characteristic_zero_source_witness=True)))


if __name__ == '__main__':
    main()
