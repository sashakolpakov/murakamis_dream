#!/usr/bin/env python3
"""Exact full-Psi chart transition and isolated-collision downhill diagnostics.

The analytic theorem is independent of these checks. Re u<0 is used for
the finite-product check so every logarithm is on its original anchored
power-series branch; no numerical branch unwrapping is inferred.
"""

import json
from pathlib import Path
import mpmath as mp


def psi_plus(n,z):
    h=2*mp.pi*mp.j/n;Q=mp.exp(h);t=mp.exp(z)
    central=mp.log(1-t**n)
    logV=(n-1)*central/(2*n)-sum(mp.mpf(j)/n*mp.log(1-Q**j*t) for j in range(1,n))
    return mp.exp(logV+(mp.mpf(n+1)/(2*n)+mp.j*z/(2*mp.pi))*central
                  +mp.j*mp.polylog(2,t**n)/(2*mp.pi*n))


def psi(n,eps,z):
    return psi_plus(n,z) if eps==1 else mp.conj(psi_plus(n,mp.conj(z)))


def run():
    mp.mp.dps=90
    transition=[];descent=[]
    for n in (32,33,64,65,128,256):
        delta=mp.mpf(n)**(-mp.mpf('0.4'))
        for eps in (1,-1):
            h=eps*2*mp.pi*mp.j/n
            for imagfrac in ('-.9','.2','.8'):
                u=-delta/3+eps*mp.j*delta*mp.mpf(imagfrac)
                shifted=u-eps*2*mp.j*delta
                # Exact selected-strip reset with its WHOLE central norm.
                left=psi(n,eps,shifted)
                right=(1-mp.exp(n*shifted))*psi(n,eps,shifted+eps*2*mp.pi*mp.j)
                assert abs(left-right)<mp.mpf('1e-65')*max(1,abs(left),abs(right))
                k=int(mp.ceil(2*n*delta/mp.pi))
                upstairs=u+k*h
                product=mp.fprod(1-mp.exp(u+j*h) for j in range(k))
                continued=product*psi(n,eps,upstairs)
                exact=psi(n,eps,u)
                assert abs(continued-exact)<mp.mpf('1e-65')*max(1,abs(exact),abs(continued))
                transition.append({'N':n,'epsilon':eps,'imag_fraction':imagfrac,
                                   'retained_full_norm_transition':True,
                                   'finite_h_shift_continuation':True})
            for realfrac in ('-.8','-.2','.2','.8'):
                u=delta*mp.mpf(realfrac)+eps*mp.j*delta/2
                out=u-eps*2*mp.j*delta
                # A polynomially regular background, adverse normal gradient.
                g=-eps*mp.mpf('.1')*mp.log(n)
                incoming=eps*mp.polylog(2,mp.exp(u))+g*u
                base=eps*mp.polylog(2,mp.exp(out))+g*out
                outgoing=max(mp.im(base),mp.im(base+2*mp.pi*mp.j*out))
                drop=mp.im(incoming)-outgoing
                assert drop>mp.mpf('.1')*delta*mp.log(n)
                descent.append({'N':n,'epsilon':eps,'real_fraction':realfrac,
                                'both_outgoing_sector_action_drop':mp.nstr(drop,18)})
    return {'transition':transition,'descent':descent}


def main():
    result={'status':'PASS',**run(),
            'scope':'Exact anchored chart factors and local downhill checks; no global patch-count or simultaneous-circuit theorem.'}
    Path(__file__).with_name('actual_isolated_shape_one_patch_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS 36 exact full-Psi normal-chart transitions and 48 signed two-sector downhill checks')


if __name__=='__main__':main()
