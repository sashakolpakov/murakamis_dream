#!/usr/bin/env python3
"""Whole-support marked Gram: universal identity and actual-source checks.

The uniform proof is in the companion note. Finite grid checks validate
the half-step/range implementation; finite precision does not prove a
uniform bound. The exact universal even-product identity supplies the
analytical second-band inequality.
"""
import itertools
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp
from scipy.special import spence

from diagnose_actual_marked_boundary_conditioning import GenericPacket
from diagnose_actual_whole_support_boundary_conditioning import RacahPacket,sample


def universal_even_product():
    c,s=sp.symbols('c s')
    a=sp.symbols('a0:4');b=sp.symbols('b0:4')
    plus=sp.prod(a[i]*c+b[i]*s for i in range(4))
    minus=sp.prod(a[i]*c-b[i]*s for i in range(4))
    even=0
    for mask in range(16):
        count=mask.bit_count()
        if count%2:continue
        even+=2*c**(4-count)*s**count*sp.prod(b[i] if mask>>i&1 else a[i] for i in range(4))
    assert sp.expand(plus+minus-even)==0
    return {'universal_even_product_cleared_polynomial':True,'positive_even_terms':8}


def integer_and_action_ranges(N):
    d=N-1;M=d//2;branches=terms=tails=centers=0
    # L at a quarter-grid: comparisons are only diagnostics. Range and
    # midpoint assertions below are exact integers.
    grid=np.arange(4*N)/(4*N)
    L=-np.imag(spence(1-np.exp(2j*np.pi*grid)))/(2*np.pi)
    worst=0.0
    for low in itertools.product(range(M+1),repeat=3):
        if sum(low)<d:continue
        choices=[(j,) if 2*j==d else (j,d-j) for j in low]
        for js in itertools.product(*choices):
            J=sum(js);rs=[J-2*j for j in js]
            assert d<=J<=2*d and min(rs)>=0 and max(rs)<=d
            xn=[2*J+1-4*j for j in js]+[4*N-2*J-3]
            assert sum(xn)==4*N and all(0<x<2*N for x in xn)
            # A single actual high fold is an exact complementary
            # permutation of the four half-step coordinates.
            for axis in range(3):
                flipped=list(js);flipped[axis]=d-flipped[axis]
                Jf=sum(flipped)
                xf=[2*Jf+1-4*j for j in flipped]+[4*N-2*Jf-3]
                assert sorted(xf)==sorted(2*N-x for x in xn)
            lo=max(*js,J-d);hi=J-max(js)
            mid=J//2
            assert lo<=mid<=hi and mid<N
            assert lo<=(J+1)//2<=hi and (J+1)//2<N
            phi=-2*sum(L[x] for x in xn)
            centers+=1;branches+=1
            for t in range(lo,hi+1):
                indices=[d+t-J]+[t-j for j in js]+[J-j-t for j in js]
                assert all(0<=k<N for k in indices)
                vn=4*t-2*J
                assert abs(vn)<min(xn[:3])
                assert all(0<xn[i]+vn<4*N and 0<xn[i]-vn<4*N for i in range(3))
                assert 0<xn[3]+vn<4*N
                assert (xn[3]-vn<0)==(t>=N)
                assert 1<=(N+t)//N<=2
                h=-sum(L[(x+vn)%(4*N)]+L[(x-vn)%(4*N)] for x in xn)
                worst=max(worst,float(h-phi))
                assert h<=phi+2e-12
                terms+=1;tails+=int(t>=N)
    return {'N':N,'unfolded_supported_branches':branches,'true_terms':terms,
        'second_zero_terms':tails,'exact_midpoints':centers,
        'largest_float_action_excess_diagnostic':worst}


def actual_source_comparison(N):
    with mp.workdps(110):
        # A fixed genuinely generic complex parameter, not a root-only
        # interpolation. Both implementations retain every normal factor.
        t=mp.mpc('0.003','0.002')
        physical=GenericPacket(N,t);racah=RacahPacket(N,t)
        M=(N-1)//2;count=0;maximum=mp.mpf(0)
        for low in itertools.product(range(M+1),repeat=3):
            if sum(low)<N-1:continue
            choices=[(j,) if 2*j==N-1 else (j,N-1-j) for j in low]
            for js in itertools.product(*choices):
                a=physical.closed_branch(js);b=racah.closed_branch(js)
                err=abs(a-b)/max(1,abs(a),abs(b))
                assert err<mp.mpf('1e-85')
                maximum=max(maximum,err);count+=1
        return {'N':N,'actual_generic_all_partner_traces':count,
            'maximum_relative_error':mp.nstr(maximum,15)}


def marked_source_crosscheck(N,labels):
    a=sample(N,labels,130,packet=GenericPacket)
    b=sample(N,labels,130,packet=RacahPacket)
    with mp.workdps(70):
        err=max(abs(mp.mpc(*u)-mp.mpc(*v)) for u,v in zip(a['normalized_moments'],b['normalized_moments']))
        assert err<mp.mpf('1e-30')
    return {'N':N,'labels':labels,'all_actual_marked_normal_moments_match':True,
            'maximum_normalized_moment_error':mp.nstr(err,15)}


if __name__=='__main__':
    identity=universal_even_product()
    ranges=[integer_and_action_ranges(N) for N in range(2,33)]
    traces=[actual_source_comparison(N) for N in range(3,9)]
    marked=[marked_source_crosscheck(N,labels) for N,labels in
        [(4,(1,1,1)),(5,(0,2,2)),(6,(1,2,2)),(7,(1,2,3)),(8,(1,3,3))]]
    out={'status':'PASS','universal_identity':identity,'integer_band_and_midpoint':ranges,
        'independent_generic_physical_trace':traces,'original_marked_normal_checks':marked,
        'scope':'Universal algebraic even-product certificate; exact finite integer range checks; independent actual generic traces and marked normals. Whole-support polynomial theorem is analytical, not inferred from finite action or conditioning samples.'}
    Path(__file__).with_name('actual_whole_support_boundary_gram_envelope_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS universal even-product identity;31 full support range levels;6 physical generic families;5 all-moment marked crosschecks')
