#!/usr/bin/env python3
"""Local zero-pattern and rigorous constant checks for the contrast corollary.

No original-source experiment is claimed: that interface is the frozen
homogeneous theorem. Finite Fourier arithmetic uses outward-rounded Arb.
"""
import argparse
from fractions import Fraction
from itertools import combinations
import json
from pathlib import Path
from flint import arb,ctx
import sympy as sp


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=Path(__file__).with_name('general_local_curvature_source_corridor_results.json'));args=p.parse_args()
    ctx.prec=256;pi=arb.pi();M=1024
    x=sp.Symbol('x')
    assert sp.integrate(x**4*(1-x)**4/(1+x*x),(x,0,1))==sp.Rational(22,7)-sp.pi
    assert Fraction(56,99)-Fraction(1,2)==Fraction(13,198)>Fraction(1,16)
    def lam(t):return sum(((2*k*t).sin()/(2*k*k) for k in range(1,M+1)),arb(0))
    fs={1:arb(0)}
    for n in (2,3):fs[n]=n*(lam(pi/(2*n))+lam((pi-pi/n)/2))/pi
    gs={2:arb(0),3:3*lam(pi/3)/pi,4:4*lam(pi/4)/pi}
    rows=[]
    # Positions are the actual cyclic port dictionary (x,b,c,y). Both outers
    # cannot be the marked MAIN pair: their edge is MATCHING.
    for nz in range(3):
        for zz in combinations(range(4),nz):
            if set(zz)=={0,3}:continue
            nonzero=set(range(4))-set(zz)
            n1=len(nonzero&{0,1,3});n2=len(nonzero&{0,2,3});m=len(nonzero)
            assert min(n1,n2)>=1 and max(n1,n2)>=2
            if m>=3:assert min(n1,n2)>=2
            gap=fs[n1]+fs[n2]-gs[m]-arb(3).log()+arb(2).log()
            f_tail=sum(n/(pi*M) for n in (n1,n2) if n>1)
            g_tail=arb(0) if m==2 else m/(2*pi*M)
            lower=gap-f_tail-g_tail;upper=gap+f_tail+g_tail
            assert lower>arb(1)/16
            rows.append({'zero_positions':[['x','b','c','y'][i] for i in zz],'positive_triangle_sizes':[n1,n2],'positive_quartet_size':m,'gap_minus_log_3over2_lower':str(lower.lower()),'gap_minus_log_3over2_upper':str(upper.upper())})
    assert len(rows)==10
    result={'status':'PASS','scope':'Elementary local inequality only; no new source experiment, diagram realization, all-width existence, or far-color estimate.','interval_engine':'python-flint arb','precision_bits':ctx.prec,'fourier_terms':M,'allowed_zero_patterns':len(rows),'exact_elementary_constant_checks':2,'common_proved_margin':'1/16','patterns':rows}
    args.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='patterns'},indent=2))

if __name__=='__main__':main()
