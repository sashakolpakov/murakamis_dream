#!/usr/bin/env python3
"""Replay a fixed floating current testbed; no source certificate or search.

All rate branches are explicit below. Polynomial roots are numerical and
the original logarithmic residual is checked only in floating arithmetic.
The output is a diagnostic, never an outward enclosure or a proof.
"""
import argparse
import json
from pathlib import Path

import numpy as np
from scipy.special import spence

P = np.pi
A_VALUES = [.1, .22, .22-.057j, .22+.02j, .35, .35-.057j,
            .35+.02j, .45-.057j, .48-.00912j, .5]


def g(z):
    """Marked lower/upper primitive, retaining the upper period polynomial."""
    z = np.asarray(z, dtype=complex)
    lo = np.where(z.imag > 0, np.conj(z), z)
    gl = (spence(1-np.exp(-2j*P*lo))-P*P/6)/(2j*P)
    return np.where(z.imag > 0, np.conj(gl)+1j*P*(z-z*z), gl)


def qr(s, a, b, e):
    return np.real(g(s+a)+g(s+b)-(2+e)*g(s)+2j*P*a*s)


def root(a, b, e):
    p, q = 1/np.tan(P*a), 1/np.tan(P*b)
    co = ([1, p+q, -1+1j*(q-p)] if not e else
          [1, p+q+1j, p*q+1j*(p+q), 2*(p-q)-1j*(p*q+2)])
    rr = [z for z in np.roots(co) if z.real > 0 and abs(z.imag) < 1]
    assert len(rr) == 1, (a,b,e,rr)
    z = np.log((rr[0]+1j)/(rr[0]-1j))/(2j*P)
    residual = (np.log(1-np.exp(-2j*P*(z+a)))
                +np.log(1-np.exp(-2j*P*(z+b)))
                -(2+e)*np.log(1-np.exp(-2j*P*z))+2j*P*a)
    assert abs(residual) < 1e-10, (a,b,e,z,residual)
    assert 0 < z.real < .5 and 0 < (z+a).real < 1 and 0 < (z+b).real < 1
    return z


def arguments(c):
    ac = complex(*c['A'])
    return (ac,c['right']) if c['orientation'] == 0 else (c['right'],ac)


def original_diagnostic():
    ys, xs = np.linspace(-.5,.5,101), np.linspace(0,1,101)
    out = []
    for ac in A_VALUES:
        for r in [.5,.55]:
            for orientation in [0,1]:
                a,b = ((complex(ac),complex(r)) if orientation == 0 else
                       (complex(r),complex(ac)))
                for e in [0,1]:
                    s = root(a,b,e)
                    M, h, d = float(qr(s,a,b,e)), s.imag, 2+e
                    U = np.real(g(a+1j*ys)+g(b+1j*ys))+d*P*np.maximum(ys,0)-2*P*a.real*ys
                    W = U+2*P*(np.maximum(ys+a.imag,0)+np.maximum(ys+b.imag,0)
                                -d*np.maximum(ys,0)-a.imag)
                    vert = M-max(np.max(U-2*P*np.abs(ys)),np.max(W-2*P*np.abs(ys)))
                    joinys = np.linspace(min(h,0),max(h,0),31)
                    uj = np.real(g(a+1j*joinys)+g(b+1j*joinys))+d*P*np.maximum(joinys,0)-2*P*a.real*joinys
                    wj = uj+2*P*(np.maximum(joinys+a.imag,0)+np.maximum(joinys+b.imag,0)
                                 -d*np.maximum(joinys,0)-a.imag)
                    exterior = xs[np.abs(xs-s.real) > .04]
                    hess = P*(1/np.tan(P*(s+a))+1/np.tan(P*(s+b))-d/np.tan(P*s))+(d-2)*P*1j
                    out.append(dict(A=[complex(ac).real,complex(ac).imag],right=r,
                        orientation=orientation,epsilon=e,root=[s.real,s.imag],action=M,
                        strip_margin=min(s.real,.5-s.real,(s+a).real,1-(s+a).real,(s+b).real,1-(s+b).real),
                        curvature=-hess.real,
                        alias_gaps=[M-float(np.max(qr(xs+1j*hh,a,b,e)-2*P*abs(hh))) for hh in [-.5,.5]],
                        weighted_vertical_gap=float(vert),
                        zero_join_gap=float(M-max(np.max(uj),np.max(wj))),
                        horizontal_outside04_gap=M-float(np.max(qr(exterior+1j*h,a,b,e)))))
    return dict(status='diagnostic_only',cases=len(out),right_points=[.5,.55],
                fixed_horizontal_heights=[-.5,.5],cases_data=out)


def cut_diagnostic(cases, cut):
    out = []
    for c in cases:
        a,b = arguments(c)
        e,s,M = c['epsilon'],complex(*c['root']),c['action']
        fine = cut == .5
        ys = np.linspace(min(s.imag,0),max(s.imag,0),101 if fine else 51)
        vals = dict(
            real_right_tail=M-float(np.max(qr(np.linspace(cut,1,501 if fine else 301),a,b,e))),
            real_left_tail=M-float(np.max(qr(np.linspace(0,.05,51 if fine else 31),a,b,e))),
            right_cut_join=M-float(np.max(qr(cut+1j*ys,a,b,e))),
            left_cut_join=M-float(np.max(qr(.05+1j*ys,a,b,e))))
        xs = np.linspace(.05,cut,451 if fine else 101)
        if fine:
            exterior = xs[np.abs(xs-s.real) > .04]
            vals['horizontal_outside04'] = M-float(np.max(qr(exterior+1j*s.imag,a,b,e)))
        for y in [-.35,.35]:
            vals['alias_'+str(y)] = M-float(np.max(qr(xs+1j*y,a,b,e)-2*P*abs(y)))
        out.append(dict(case=c,values=vals))
    result = dict(status='diagnostic_only',cases=out)
    if cut == .5:
        result['contour'] = dict(left_cut=.05,right_cut=.5,aliases=[-.35,.35])
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir',type=Path,required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True,exist_ok=True)
    base = original_diagnostic()
    results = {'selected_height_currents.json':base,
               'cut_04_currents.json':cut_diagnostic(base['cases_data'],.4),
               'cut_half_currents.json':cut_diagnostic(base['cases_data'],.5)}
    remote = []
    # Revisit existing real cases only, without introducing parameter points.
    for c in base['cases_data']:
        if c['right'] == .55 and c['A'][1] == 0:
            a,b = arguments(c)
            remote.append(dict(case=c,upper_alias_at_x0=[
                dict(height=Y,gap=c['action']-float(qr(1j*Y,a,b,c['epsilon'])-2*P*Y))
                for Y in [2,.5,.25]]))
    results['old_remote_upper.json'] = dict(status='diagnostic_only',cases=remote)
    for name,result in results.items():
        (args.output_dir/name).write_text(json.dumps(result,indent=2)+'\n')
    print('Replayed80 fixed floating cases; no cover or finite-source claim.')


if __name__ == '__main__':
    main()
