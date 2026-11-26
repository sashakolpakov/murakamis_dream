#!/usr/bin/env python3
"""Reproduce exact edge identities and finite checks of the strip bound.

The symbolic identities are exact. The numerical cases check the printed
estimate; they are not a proof of its uniform validity or of a volume limit.
"""
import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp
import sympy as sp


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    p, q = sp.symbols('p q', real=True)
    c = (p*p+q*q)/(2+p*p+q*q)
    ct = (1-p*p)/(1+p*p)
    cu = (1-q*q)/(1+q*q)
    ident = [sp.factor((c+ct)*(c+cu)-(1-c)**2)]
    gradient = -sp.asinh(p/sp.sqrt(1+q*q))/sp.pi
    h11 = -(1+p*p)/(2*sp.pi*sp.sqrt(1+p*p+q*q))
    h12 = p*q/(2*sp.pi*sp.sqrt(1+p*p+q*q))
    h22 = -(1+q*q)/(2*sp.pi*sp.sqrt(1+p*p+q*q))
    ident += [sp.simplify(sp.diff(gradient,p)*(1+p*p)/2-h11),
              sp.simplify(sp.diff(gradient,q)*(1+q*q)/2-h12),
              sp.factor(h11*h22-h12*h12-1/(4*sp.pi**2))]
    assert ident == [0]*4, ident

    mp.mp.dps = 70
    case_count = 0
    worst = (-mp.inf, None)
    for n in (160, 161, 199, 200, 255, 256):
        indices = sorted({(n+4)//5, n//4, 3*n//10})
        for k in indices:
            r = [mp.cos((2*j+1)*mp.pi/n) for j in range(k)]
            reserved = n//32
            negative = [j for j in range(k) if r[j] < 0]
            partners = list(range(reserved, reserved+len(negative)))
            assert not set(partners) & set(negative)
            assert all(r[j] >= mp.mpf('0.9') for j in range(reserved))
            assert all(r[j] > mp.mpf('0.7') for j in partners)
            assert all(r[j] > mp.mpf('-0.4') for j in negative)
            for numerator in (-8,-7,-5,-3,-1,0,1,3,5,7,8):
                t = mp.pi*numerator/8
                for y in map(mp.mpf, ('-0.25','-0.125','0','0.125','0.25')):
                    cosine = mp.cos(t+1j*y)
                    value = mp.fsum(mp.log(abs((a+cosine)/(1+a))) for a in r)
                    bound = n*(-mp.sin(t/2)**2/160+4*y*y)
                    excess = value-bound
                    if excess > worst[0]:
                        worst = (excess, [n,k,numerator,mp.nstr(y,8)])
                    assert excess < mp.mpf('1e-60'), (n,k,t,y,excess)
                    case_count += 1

    delta=mp.mpf(1)/50
    eps=mp.mpf(1)/25
    gamma=(1+delta)/(1-delta)**2
    beta=mp.pi*gamma/2**25
    eta=1/(819200*mp.pi)
    connector=gamma*max((1+eps)/2,2/(3-4*eps))
    assert beta<eta/2 and connector<mp.mpf(3)/4
    assert 1/(80*mp.pi)>mp.mpf(1)/400 and 8*mp.pi<70

    result={
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'exact_symbolic_identities':len(ident),
        'finite_complex_gaussian_cases':case_count,
        'level_range':[160,256],
        'decimal_precision':mp.mp.dps,
        'largest_log_bound_excess':mp.nstr(worst[0],25),
        'largest_excess_case':worst[1],
        'critical_drop_upper_bound':mp.nstr(beta,25),
        'half_discarded_error_loss':mp.nstr(eta/2,25),
        'connector_coefficient':mp.nstr(connector,25),
        'scope':'Exact edge identities and finite checks only; not a uniform proof or a filled-volume certificate.',
    }
    if args.output:
        args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
