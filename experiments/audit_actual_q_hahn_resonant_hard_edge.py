#!/usr/bin/env python3
"""Focused independent finite-source and geometric hard-edge checks."""
import argparse
import json
from pathlib import Path
import mpmath as mp
import sympy as sp


def geometric_checks():
    r, s, a, b, c, d = sp.symbols('r s a b c d', nonzero=True)
    F = sp.Matrix([[r, 1-r], [s, -s]])
    Pi = F * sp.diag(1, 0) * F.inv()
    Q = sp.Matrix([[a, b], [c, d]])
    L = -c*r*r/s + (a-d+c/s)*r + d+b*s
    assert sp.simplify(sp.trace(Q*Pi)-L) == 0
    bp, rho, mu = sp.symbols('bp rho mu', nonzero=True)
    A = sp.Matrix([[-1, 0], [4, -1]])
    B = sp.Matrix([[-1, -1], [0, -1]])
    Q1 = sp.Matrix([[1, bp], [0, 1]])
    Q0, Q2 = A.inv()*Q1, B*Q1
    assert sp.trace(B*A) == -2
    ls = [sp.expand(sp.trace(x*Pi)) for x in [Q0, Q1, Q2]]
    kap = Q0[1, 0]*rho**2/(s*ls[1])
    vv = -ls[1]/ls[2]
    kk = sp.sin(sp.pi*mu)**2*(vv-1)/(sp.pi**2*kap*vv)
    assert sp.simplify(kk-sp.sin(sp.pi*mu)**2*s*s/(4*sp.pi**2*rho*rho)) == 0
    # The distinct literal 002 endpoint, with first puncture -J.
    Q0s = Q1
    Q1s = B*Q0s
    Q2s = A*Q1s
    lss = [sp.expand(sp.trace(x*Pi)) for x in [Q0s,Q1s,Q2s]]
    U0s = -lss[0]/lss[1]
    kaps = s*lss[1]/(Q2s[1,0]*rho**2)
    kks = kaps*sp.sin(sp.pi*mu)**2*(1-U0s)/sp.pi**2
    assert sp.simplify(kks-sp.sin(sp.pi*mu)**2*s*s/(4*sp.pi**2*rho*rho)) == 0
    # Literal right-angled 202 disk: a marked point on the middle
    # white circle gives a strictly positive finite total.
    eta=sp.symbols('eta',nonzero=True)
    Ap=-sp.Matrix([[1,0],[2,1]])
    Bp=-sp.Matrix([[3,-2],[2,-1]])
    gg=sp.Matrix([[0,-1],[1,-eta]])
    ca=(gg*Ap*gg.inv())[1,0]
    cb=(gg*Bp*gg.inv())[1,0]
    assert sp.simplify(-ca/cb+eta**2/(eta-1)**2)==0
    hh=sp.symbols('hh',real=True,nonzero=True)
    circle=(hh**2+sp.I*hh)/(1+hh**2)
    assert sp.simplify((-ca/cb).subs(eta,circle)-hh**2)==0
    # Actual inverse-turn exponentials, with half-index q^-1 retained.
    l0, l1, lo, l2, q = sp.symbols('l0 l1 lo l2 q', nonzero=True)
    tt, vi, uo = lo/l1, -lo/l0, -lo/l2
    sig = q**(-2)*uo/vi
    ell = q**(-1)*tt/vi
    assert sp.simplify(sig/(q**(-1)*uo)-q**(-1)*(-l0/lo)) == 0
    assert sp.simplify(ell-q**(-1)*(-l0/l1)) == 0
    assert sp.simplify(sig/ell-q**(-1)*(-l1/l2)) == 0
    # Degree conservation of every one of the eight prefix patterns.
    patterns = []
    for e0 in [0, 1]:
        for e1 in [0, 1]:
            for e2 in [0, 1]:
                ku, kv, kt = 2*(e0-e1), 2*(e1-e2), 2*(e0-e2)
                assert ku+kv == kt
                patterns.append([2*e0, 2*e1, 2*e2, ku, kv, kt])
    return {'exact_geometric_identities': 9, 'incidence_patterns': patterns}


def normalized_series(N, m, U, V):
    Q = mp.exp(2j*mp.pi/N)
    term = mp.mpc(1)
    terms = [term]
    for l in range(1, m+1):
        ratio = (-Q**(-m+l-1) * ((1-Q**(m-l+1))/(1-Q**l))**2
                 * (V-Q**(l-1))/(U*V) / (1-Q**(m-l)/U))
        term *= ratio
        terms.append(term)
    return mp.fsum(terms)


def literal_source(N, m, U, V, raw=False):
    Q = mp.exp(2j*mp.pi/N)
    fs = [mp.mpc(1)]
    for j in range(1, m+1):
        fs.append(fs[-1]*(1-Q**j))
    values = []
    for k in range(m+1):
        gauss = fs[m]/(fs[k]*fs[m-k])
        ck = (-1)**k*Q**(k*(k+1)/2)*gauss**2
        values.append(ck*V**k*mp.fprod(U-Q**j for j in range(k))
                      *mp.fprod(V-Q**j for j in range(m-k)))
    cm = (-1)**m*Q**(m*(m+1)/2)
    endpoint = cm*(U*V)**m*mp.fprod(1-Q**j/U for j in range(m))
    return mp.fsum(values) if raw else mp.fsum(values)/endpoint


def small_second_series(N,m,U,V):
    Q=mp.exp(2j*mp.pi/N)
    term=mp.mpc(1)
    terms=[term]
    for k in range(1,m+1):
        term *= (-Q**k*((1-Q**(m-k+1))/(1-Q**k))**2
                 *V*(U-Q**(k-1))/(V-Q**(m-k)))
        terms.append(term)
    return mp.fsum(terms)


def boundary_polynomial(N,m,T):
    Q=mp.exp(2j*mp.pi/N)
    weight=mp.mpc(1)
    terms=[weight]
    for k in range(1,m+1):
        weight *= (mp.sin(mp.pi*(m-k+1)/N)/mp.sin(mp.pi*k/N))**2*(Q*T)
        terms.append(weight)
    return (-1)**m*Q**(m*(m-1)/2)*mp.fsum(terms)


def mixed_relative(N,a,U,T):
    Q=mp.exp(2j*mp.pi/N)
    ff=[mp.mpc(1)]
    gg=[mp.mpc(1)]
    for k in range(a):
        ff.append(ff[-1]*(1-Q**k/U))
        gg.append(gg[-1]*(1-(T/U)*Q**(-k)))
    weight=mp.mpc(1)
    base=[weight]
    modified=[weight*ff[0]*gg[a]]
    for k in range(1,a+1):
        weight *= (mp.sin(mp.pi*(a-k+1)/N)/mp.sin(mp.pi*k/N))**2*(Q*T)
        base.append(weight)
        modified.append(weight*ff[k]*gg[a-k])
    return mp.fsum(modified)/mp.fsum(base)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', default='experiments/actual_q_hahn_resonant_hard_edge_results.json')
    args = ap.parse_args()
    mp.mp.dps = 100
    result = geometric_checks()
    parameters = [(mp.mpc('0.7','0.3'), mp.mpc('0.6','0.2')),
                  (mp.mpc('-0.4','0.8'), mp.mpc('1.3','-0.1')),
                  (mp.mpc('1.2','-0.6'), mp.mpc(1))]
    comparisons = []
    for N in [7, 10, 15, 22]:
        for m in sorted(set([N//3, N//2, 2*N//3])):
            for kap, V in parameters:
                U = N*N*kap
                exact = literal_source(N,m,U,V)
                rearranged = normalized_series(N,m,U,V)
                err = abs(exact-rearranged)/max(1,abs(exact))
                assert err < mp.mpf('1e-85')
                comparisons.append(float(err))
                Us,Vsm=V,kap/(N*N)
                # Independent original polynomial, using its already checked
                # last-endpoint normalization and then exact endpoint ratio.
                q=mp.exp(2j*mp.pi/N)
                first=mp.fprod(Vsm-q**j for j in range(m))
                direct=literal_source(N,m,Us,Vsm,raw=True)/first
                err=abs(direct-small_second_series(N,m,Us,Vsm))/max(1,abs(direct))
                assert err<mp.mpf('1e-85')
                comparisons.append(float(err))
    rates = []
    for fraction in [mp.mpf('.32'), mp.mpf('.5'), mp.mpf('.68')]:
        for kap, V0 in parameters:
            for N in [64, 128, 256, 512]:
                m = int(mp.floor(fraction*N))
                # Include the allowed actual O(1/N) clock offsets.
                U = N*N*kap*mp.exp(-mp.pi*1j/N)
                V = V0*mp.exp(-mp.pi*1j/N)
                KN = mp.sin(mp.pi*m/N)**2*(V-1)/(mp.pi**2*(U/(N*N))*V)
                limit = mp.besselj(0,2*mp.sqrt(KN))
                value = normalized_series(N,m,U,V)
                scaled = N*abs(value-limit)
                assert scaled < 3
                rates.append({'N':N,'m':m,'N_absolute_error':float(scaled)})
                Us=V0*mp.exp(-mp.pi*1j/N)
                Vsm=kap*mp.exp(-mp.pi*1j/N)/(N*N)
                Ksm=N*N*Vsm*mp.sin(mp.pi*m/N)**2*(1-Us)/mp.pi**2
                small_value=small_second_series(N,m,Us,Vsm)
                scaled=N*abs(small_value-mp.besselj(0,2*mp.sqrt(Ksm)))
                assert scaled<3
                rates.append({'N':N,'m':m,'endpoint':'small_second','N_absolute_error':float(scaled)})
    result.update(status='PASS', literal_source_comparisons=len(comparisons),
                  max_source_relative_error=max(comparisons), boundary_packet_checks=len(rates),
                  maximum_N_absolute_error=max(x['N_absolute_error'] for x in rates), rates=rates,
                  scope='Root normalized numerator only; no generic normals or global period.')
    collision_errors=[]
    mixed_errors=[]
    for N in [7,10,15,22]:
        a=(N-1)//2-1
        m=N-1-a
        Q=mp.exp(2j*mp.pi/N)
        for T in [mp.mpc('1.2','.4'),mp.mpc('.6','-.2'),mp.mpc('2','.8')]:
            U=N*N*mp.mpc('.8','.3')
            aa=boundary_polynomial(N,a,T)
            am=boundary_polynomial(N,m,T)
            forced=mp.fprod(T-Q**j for j in range(a,m))
            err=abs(am-aa*forced)/max(1,abs(am))
            assert err<mp.mpf('1e-85')
            collision_errors.append(float(err))
            expected=am*mixed_relative(N,a,U,T)
            actual=literal_source(N,m,U,T/U,raw=True)
            err=abs(actual-expected)/max(1,abs(actual))
            assert err<mp.mpf('1e-85')
            collision_errors.append(float(err))
    for N in [32,64,128,256]:
        for a in [(N-1)//2,N//3]:
            for T in [mp.mpc('1.2','.4'),mp.mpc('.6','-.2'),mp.mpc('2','.8')]:
                scaled=N*abs(mixed_relative(N,a,N*N*mp.mpc('.8','.3'),T)-1)
                assert scaled<10
                mixed_errors.append(float(scaled))
    result.update(mixed_boundary_identities=len(collision_errors),
                  maximum_mixed_identity_error=max(collision_errors),
                  mixed_relative_packet_checks=len(mixed_errors),
                  maximum_mixed_N_relative_error=max(mixed_errors))
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['rates','incidence_patterns']},indent=2))


if __name__ == '__main__':
    main()
