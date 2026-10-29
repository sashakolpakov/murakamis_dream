"""Actual Frobenius relative endpoints and literal normal-generator defect."""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

import sympy as sp


def generators(N):
    e, f = sp.zeros(N+1), sp.zeros(N+1)
    h = sp.diag(*[N-2*k for k in range(N+1)])
    for k in range(1, N+1):
        e[k-1, k] = N-k+1
        f[k, k-1] = k
    return e, f, h


def zero(matrix):
    return all(sp.expand(x) == 0 for x in matrix)


def root_endpoint_case(N):
    L, t, z, m = sp.symbols('L t z m')
    e, f, h = generators(N)
    n = h+f-e
    psi = sp.ones(N+1, 1)
    row = sp.Matrix([[sp.binomial(N,k)*(L*t)**(N-k)*(1-L*t)**k
                      for k in range(N+1)]])
    assert zero(n*psi)
    assert zero(n**(N+1))
    assert zero(row.diff(t)-L*row*n)
    assert sp.expand((row*psi)[0]-1) == 0
    row0, row1 = row.subs(t,0), row.subs(t,1)
    interval = row.applyfunc(lambda x:sp.integrate(sp.expand(x),(t,0,1)))
    assert zero(interval*(L*n)-row1+row0)
    assert all(sp.expand(x-sp.Rational(1,N+1)) == 0 for x in interval.subs(L,1))
    C = sp.Matrix(N+1,N+1,lambda i,j:(i+2)*(j+1)+int(i==j))
    assert sp.expand((interval*(L*n*C-C*L*n)*psi-(row1-row0)*C*psi)[0]) == 0
    cochain = sum(row[k]/sp.binomial(N,k)*z**(-k-1) for k in range(N+1))
    inserted = C*psi
    section = sum(sp.binomial(N,k)*inserted[k]*z**k for k in range(N+1))
    assert sp.expand(sp.expand(cochain*section).coeff(z,-1)-(row*C*psi)[0]) == 0
    dual = [sp.binomial(N,k)*((1+m)/2)**(N-k)*((1-m)/2)**k
            for k in range(N+1)]
    norm_squared = sum(x*x/sp.binomial(N,k) for k,x in enumerate(dual))*2**N
    assert sp.expand(norm_squared-(1+m*m)**N) == 0
    return {'N':N,'finite_interval_and_actual_endpoint_Ward':True,
            'Serre_pairing_exact':True,'coherent_metric_exact':True}


def actual_normal_defect():
    q, Q = sp.symbols('q Q')
    phi = q*q-q+1

    @lru_cache(None)
    def gaussian(a,k):
        if k < 0 or k > a:return sp.Integer(0)
        if k == 0 or k == a:return sp.Integer(1)
        return sp.expand(gaussian(a-1,k)+Q**(a-k)*gaussian(a-1,k-1))

    def reduce_q(x):
        numerator, denominator = sp.cancel(x).as_numer_denom()
        numerator = sp.rem(numerator,phi,q)
        denominator = sp.rem(denominator,phi,q)
        return sp.rem(numerator*sp.invert(denominator,phi,q),phi,q)

    N=r=3
    s=1
    highest=N*(r+1)-1
    beta=[(-1)**(N*k*(k-1)//2+k*s) for k in range(r+1)]
    e0,e1,f0,f1=[sp.zeros(r+1) for _ in range(4)]
    tau=(-1)**(N*r-1)
    for k in range(r+1):
        index=k*N+s
        if k:
            upper=highest-index+N
            value=tau*beta[k]*beta[k-1]*q**(-N*(upper-N))*gaussian(upper,N).subs(Q,q*q)
            e0[k-1,k]=reduce_q(value)
            e1[k-1,k]=reduce_q(q*sp.diff(value,q))
        if k<r:
            upper=index+N
            value=beta[k]*beta[k+1]*q**(-N*(upper-N))*gaussian(upper,N).subs(Q,q*q)
            f0[k+1,k]=reduce_q(value)
            f1[k+1,k]=reduce_q(q*sp.diff(value,q))
    e,f,h=generators(r)
    gamma=1-2*q
    assert e0==e and f0==f
    assert zero(e1-gamma*e) and zero(f1-gamma*f)
    psi0=sp.ones(r+1,1)
    psi1=gamma*f*psi0
    n0=e*f-f*e+f-e
    n1=e1*f+e*f1-f1*e-f*e1+f1-e1
    defect=n1*psi0+n0*psi1
    assert zero(defect+2*gamma*f*psi0)
    assert not zero(defect)
    return {'N':N,'r':r,'head_string':s,
            'cyclotomic_polynomial':str(phi),
            'actual_q_log_derivative_gamma':str(gamma),
            'naive_normal_endpoint_generator_defect':[str(sp.expand(x)) for x in defect]}


def source_connection_case():
    # A generic actual-pair first jet: this also checks the exact
    # gauge formula algebraically, without replacing its source unit.
    t, L, eps = sp.symbols('t L eps')
    N=2
    e,f,h=generators(N)
    n=h+f-e
    psi0=sp.ones(N+1,1)
    row0=sp.Matrix([[sp.binomial(N,k)*(L*t)**(N-k)*(1-L*t)**k
                     for k in range(N+1)]])
    psi1=sp.Matrix([1,3,5])
    raw1=sp.Matrix([[t+1,t*t-2,3*t]])
    unit1=(raw1*psi0+row0*psi1)[0]
    row1=raw1-unit1*row0
    P0=psi0*row0
    P1=psi1*row0+psi0*row1
    G1=psi1*row0-P1*(sp.eye(N+1)-P0)
    assert zero(G1*psi0-psi1)
    assert zero(row0*G1+row1)
    K0=L*n
    K1=G1*K0-K0*G1-G1.diff(t)
    assert zero(K0*psi1+K1*psi0)
    assert zero(row1.diff(t)-row1*K0-row0*K1)
    return {'generic_paired_source_connection_first_jet':True,
            'pairing_unit_derivative_retained':True}


def main():
    result={'status':'pass','root_cases':[root_endpoint_case(N) for N in range(2,9)],
            'actual_normal_defect':actual_normal_defect(),
            'source_connection':source_connection_case(),
            'scope':'Actual root endpoints and whole-source connection; no full Hopf/Gaussian current identification.'}
    path=Path(__file__).with_name('actual_frobenius_relative_endpoint_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'pass','root_levels':len(result['root_cases']),
                      'actual_normal_counterexample':'N3,r3,s1','results':str(path)},indent=2))


if __name__=='__main__':main()
