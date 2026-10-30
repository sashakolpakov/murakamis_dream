#!/usr/bin/env python3
"""Numerical convention audit for the proved local complex logarithmic limit.

The theorem uses the independent negative-root proof and holomorphic
compactness. These finite computations check the actual Fourier polynomial,
unwrapped logarithm and chosen critical branch; they are not the proof.
"""
import json
from pathlib import Path
import mpmath as mp


def J(z):
    if z == 0 or z == 1:
        return mp.mpf('0')
    return -(mp.polylog(2,mp.exp(2*mp.pi*1j*z))-mp.pi**2/6)/(2*mp.pi*1j)-mp.pi*1j*(z*z-z)/2


def energy(t,x,u,a):
    def B(v,w):return J(v)-J(w)-J(v-w)
    return B(x,a)+B(u,a)+B(t-u,x-a)-B(t,x)


def stationary(t,x,u,a,w):
    s=lambda z:mp.sin(mp.pi*z)
    return w*s(x-a)**2*s(u-a)-s(a)**2*s(t-u-x+a)


def chosen_action(t,x,u):
    lo=max(mp.mpf(0),u-t+x);hi=min(x,u)
    l,r=lo,hi
    for _ in range(280):
        a=(l+r)/2
        if stationary(t,x,u,a,mp.mpf(1))>0:l=a
        else:r=a
    a=(l+r)/2
    phi=mp.pi*(t+x-1)
    for k in range(1,121):
        w=mp.exp(1j*phi*k/120)
        a=mp.findroot(lambda b:stationary(t,x,u,b,w),(a,a+mp.mpf('0.00001')),tol=mp.mpf('1e-80'))
    assert lo < mp.re(a) < hi and mp.im(a)>0
    assert abs(stationary(t,x,u,a,mp.exp(1j*phi)))<mp.mpf('1e-75')
    return energy(t,x,u,a)+a*1j*phi,a


def actual_log(N,t,x,u):
    tn=int(mp.floor(t*N));jn=(N-1)//2 if x==mp.mpf('0.5') else int(mp.floor(x*N));un=int(mp.floor(u*N))
    assert 0<=jn<=tn<N and N-1-jn<=tn
    ls=[mp.mpf(0)]
    for n in range(1,N):ls.append(ls[-1]+mp.log(2*mp.sin(mp.pi*n/N)))
    def lb(n,a):return ls[n]-ls[a]-ls[n-a]
    a0=max(0,un-tn+jn);a1=min(jn,un)
    logs=[lb(jn,a)+lb(un,a)+lb(tn-un,jn-a)-lb(tn,jn) for a in range(a0,a1+1)]
    mx=max(logs);co=[mp.exp(v-mx) for v in logs];total=sum(co)
    co=[v/total for v in co]
    log_at_one=mx+mp.log(total)
    def value(w):
        p=mp.mpc(0)
        for c in reversed(co):p=p*w+c
        return w**a0*p
    phi=mp.pi*(tn+jn-(N-1))/N
    # Negative roots imply 0 <= d Arg P(e^{i phi})/d phi <= a1
    # on this quadrant. This mesh makes every exact increment < pi/4.
    steps=max(1,int(mp.ceil(4*max(a1,1)*abs(phi)/mp.pi))+1)
    phase=mp.mpf(0);prev=mp.mpc(1)
    for k in range(1,steps+1):
        current=value(mp.exp(1j*phi*k/steps))
        increment=mp.arg(current/prev)
        assert abs(increment)<mp.pi/4+mp.mpf('1e-60')
        phase+=increment;prev=current
    result=(log_at_one+mp.log(abs(prev))+1j*phase)/N
    # Exact finite cosine bound, evaluated with retained cancellation.
    lower=mp.cos(phi/2)**(a1-a0)
    assert abs(prev)>=lower*(1-mp.mpf('1e-60'))
    assert abs(prev)<=1+mp.mpf('1e-60')
    return result,{'N':N,'t':tn,'j':jn,'u':un,'polynomial_degree':a1,'nonzero_root_count':a1-a0,
                  'log_modulus_per_level':float(mp.re(result)),'unwrapped_phase_per_level':float(mp.im(result))}


def run():
    mp.mp.dps=100
    cases=[(mp.mpf(4)/5,mp.mpf(2)/5,mp.mpf(7)/20),
           (mp.mpf(4)/5,mp.mpf(1)/2,mp.mpf(7)/20),
           (mp.mpf(9)/10,mp.mpf(1)/3,mp.mpf(2)/5)]
    out=[]
    for t,x,u in cases:
        target,a=chosen_action(t,x,u);rows=[]
        for N in (50,101,202,405):
            val,row=actual_log(N,t,x,u);row['complex_error']=float(abs(val-target));rows.append(row)
        assert rows[-1]['complex_error']<rows[0]['complex_error']
        assert rows[-1]['complex_error']<0.04
        out.append({'parameters':[str(t),str(x),str(u)],
                    'selected_alpha':[float(mp.re(a)),float(mp.im(a))],
                    'limiting_action':[float(mp.re(target)),float(mp.im(target))],
                    'actual_polynomials':rows})
    return {'status':'PASS','precision_digits':mp.mp.dps,'cases':out,
            'scope':'Finite numerical checks of actual local Fourier cancellation and logarithmic sheets. The uniform limit is proved analytically; no global plat asymptotic or amplitude expansion is inferred.'}


if __name__=='__main__':
    result=run()
    Path(__file__).with_name('actual_q_hahn_selected_complex_action_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
