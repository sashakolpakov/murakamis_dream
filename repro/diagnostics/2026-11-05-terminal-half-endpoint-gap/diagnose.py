#!/usr/bin/env python3
"""Reuse archived endpoint proposals; floating terminal half-point gaps only."""
import hashlib
import json
from pathlib import Path
import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
INPUT = ROOT / 'repro/diagnostics/2026-11-05-open-word-endpoint-maps/result.json'


def g(z):
    z = mp.mpc(z)
    return (mp.polylog(2, mp.exp(-2j*mp.pi*z))-mp.pi**2/6)/(2j*mp.pi)


def J(z):
    return g(z)-1j*mp.pi*(z-z*z)/2


def Q(s, a, e, eps):
    return g(s+a)+g(s+e)-(2+eps)*g(s)+2j*mp.pi*a*s


def endpoint(e, u):
    return -2*J(.5-u)-3*J(u)-J(e-u)+1j*mp.pi*e*u


def action(a, e, t, u, eps):
    return Q(t,a,e,eps)-g(a)-(1+eps)*g(e)+J(e)+endpoint(e,u)


def half_root(a, eps):
    p = 1/np.tan(np.pi*a)
    coefficients = ([1,p,-1-1j*p] if eps == 0 else
                    [1,p+1j,1j*p,2*(p-1j)])
    good = []
    for r in np.roots(coefficients):
        s = np.log((r+1j)/(r-1j))/(2j*np.pi)
        if s.real < 0:
            s += 1
        residual = (np.log(1-np.exp(-2j*np.pi*(s+a)))
                    +np.log(1-np.exp(-2j*np.pi*(s+.5)))
                    -(2+eps)*np.log(1-np.exp(-2j*np.pi*s))+2j*np.pi*a)
        if abs(residual) < 1e-7 and .1 < s.real < .49 and abs(s.imag) < .17:
            good.append((s,float(abs(residual))))
    assert len(good) == 1
    return good[0]


def main():
    mp.mp.dps = 35
    old = json.loads(INPUT.read_text())
    cases = []
    raw_centers = []
    uh = .25+1j*np.log(3)/(4*np.pi)
    for case in old['cases']:
        eps, other = case['epsilon'], case['neighbor_epsilon']
        lo,hi = (-.03,.02) if other == 0 else (-.057,0)
        rows = []
        for i,row in enumerate(case['rows']):
            a = complex(*row['external'])
            if not (.22 <= a.real <= .5 and lo <= a.imag <= hi):
                continue
            e,t,u = map(lambda v:complex(*v),row['root'])
            sh,residual = half_root(a,eps)
            rows.append(dict(original_row=i, external=row['external'],
                half_root=[float(sh.real),float(sh.imag)], half_residual=residual,
                gap=float(mp.re(action(a,e,t,u,eps)-action(a,.5,sh,uh,eps)))))
        cases.append(dict(epsilon=eps,neighbor_epsilon=other,rows=rows,
                          minimum=min(rows,key=lambda row:row['gap'])))
        # Only the already archived disk center, never an additional scan.
        original=case['rows'][0]
        a=mp.mpc(*original['external'])
        e,t,u=map(lambda v:mp.mpc(*v),original['root'])
        def derivative(v):
            return (mp.log(abs(1-mp.exp(-2j*mp.pi*(a+v))))
                    +mp.log(2*mp.cos(mp.pi*v))
                    -(2+eps)*mp.log(2*mp.sin(mp.pi*v))-2*mp.pi*mp.im(a))
        lo,hi=mp.mpf('.2'),mp.mpf('.4')
        assert derivative(lo)>0 and derivative(hi)<0
        for _ in range(100):
            mid=(lo+hi)/2
            if derivative(mid)>0:lo=mid
            else:hi=mid
        v=(lo+hi)/2
        raw=mp.re(g(a+v)-g(a)+J(mp.mpf('.5')+v)-J(mp.mpf('.5'))
                  -(2+eps)*J(v))-2*mp.pi*mp.im(a)*v
        sh,_=half_root(complex(a),eps)
        coherent=mp.re(Q(sh,a,.5,eps)-g(a)-g(.5))
        reference=mp.re(action(a,e,t,u,eps))
        hhalf=mp.re(J(.5)+endpoint(.5,uh))
        raw_centers.append(dict(epsilon=eps,neighbor_epsilon=other,
            external=original['external'],row=float(v),
            raw_minus_coherent=float(raw-coherent),
            coherent_gap=float(reference-hhalf-coherent),
            raw_gap=float(reference-hhalf-raw)))
    out = dict(status='diagnostic_only',
        scope='50 archived admitted-height proposals, no new endpoint solves, no uniform bound, no interval proof, no whole boundary comparison.',
        input_sha256=hashlib.sha256(INPUT.read_bytes()).hexdigest(),
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        cases=cases,raw_center_comparisons=raw_centers)
    assert [len(c['rows']) for c in cases] == [9,16,9,16]
    (HERE/'result.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps([dict(epsilon=c['epsilon'],neighbor_epsilon=c['neighbor_epsilon'],minimum=c['minimum']) for c in cases],indent=2))


if __name__ == '__main__':
    main()
