#!/usr/bin/env python3
"""Whole-support actual marked moments from the proved generic Racah trace.

Multiprecision diagnostics supplement the uniform analytical theorem.
The generic trace, all folded partners and original circle normal are
unchanged; only the already-proved one-sum source evaluation accelerates
the earlier physical-double-sum measurement.
"""
import argparse
import itertools
import json
from pathlib import Path

import mpmath as mp

from diagnose_actual_marked_boundary_conditioning import GenericPacket,positive_tau,ring_mul


class RacahPacket(GenericPacket):
    def __init__(self,N,t):
        super().__init__(N,t)
        self.qfac=[self.power(-k*(k-1)//2)*self.F[k]/self.f[1]**k for k in range(len(self.F))]

    def closed_branch(self,js):
        a,b,c=js;J=a+b+c;d=self.d;f=self.qfac
        if min(J-2*j for j in js)<0:return mp.mpc(0)
        S=mp.fsum((-1)**(d+t)*f[self.N+t]/
            (f[d+t-J]*mp.fprod(f[t-j]*f[J-j-t] for j in js))
            for t in range(max(*js,J-d),J-max(js)+1))
        pref=(-1)**d*mp.fprod((self.power(2*j+1)-self.power(-2*j-1))/
            (self.zeta-1/self.zeta) for j in js)
        pref*=mp.fprod(f[J-2*j] for j in js)/f[J+1]
        pref*=mp.fprod(f[j]**2*f[d-j]/f[self.N+j] for j in js)
        return pref*S*S


def sample(N,labels,dps,shrink=1,packet=RacahPacket):
    with mp.workdps(dps):
        step=mp.mpf(N)**-8/shrink
        plus=packet(N,step).moments_closed(labels)
        minus=packet(N,-step).moments_closed(labels)
        rho=2j*mp.sin(mp.pi/N);nu=2*N*(-1)**N/rho
        moments=[(a-b)/(2*step*nu) for a,b in zip(plus,minus)]
        tau=positive_tau(N,labels)
        normalized=[v/tau for v in moments]
        qpoly=list(reversed(normalized));qpoly[0]=mp.mpc(1)
        n=qpoly[:];n[0]=mp.mpc(0)
        power=[mp.mpc(1)]+[mp.mpc(0)]*(len(n)-1)
        root=[mp.mpc(0)]*len(n);r=(len(n)-1).bit_length()
        for k in range(r+1):
            root=[a+mp.binomial(mp.mpf('.5'),k)*b for a,b in zip(root,power)]
            power=ring_mul(power,n)
        K=mp.fsum(abs(v)**2 for v in root)
        return {'N':N,'labels':list(labels),'dps':dps,'normal_step':mp.nstr(step,20),
            'top_moment_relative_error':mp.nstr(abs(normalized[-1]-1),20),
            'K':mp.nstr(K,40),'log_K_over_N':mp.nstr(mp.log(K)/N,25),
            'largest_normalized_moment':mp.nstr(max(map(abs,normalized)),30),
            'normalized_moments':[[mp.nstr(mp.re(v),35),mp.nstr(mp.im(v),35)] for v in normalized]}


def paired(N,labels,dps):
    first=sample(N,labels,dps,1)
    second=sample(N,labels,dps+50,2)
    with mp.workdps(70):
        delta=max(abs(mp.mpc(*a)-mp.mpc(*b)) for a,b in zip(first['normalized_moments'],second['normalized_moments']))
        assert delta<mp.mpf(N)**-7
        assert mp.mpf(second['top_moment_relative_error'])<mp.mpf(N)**-7
    return {'paired_precision':True,'normal_step_ratio':2,
        'maximum_normalized_moment_difference':mp.nstr(delta,25),'refined':second}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--quick',action='store_true')
    args=parser.parse_args()
    cases=[(16,(1,7,7)),(64,(1,31,31)),(64,(16,16,31)),
        (128,(1,63,63)),(128,(16,55,63)),(129,(0,64,64)),
        (129,(1,63,64)),(129,(32,32,64)),(256,(1,127,127)),(256,(64,64,127))]
    if args.quick:cases=cases[:3]
    rows=[]
    for N,labels in cases:
        row=paired(N,labels,max(150,N+100));rows.append(row)
        print(json.dumps(row),flush=True)
    Path(__file__).with_name('actual_whole_support_boundary_conditioning_diagnostic_results.json').write_text(
        json.dumps({'status':'PASS_DIAGNOSTIC','paired_precision_actual_moments':rows,
        'scope':'Original all-partner Racah trace with physical marked normal. These finite measurements are not the uniform conditioning proof.'},indent=2)+'\n')
