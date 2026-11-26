#!/usr/bin/env python3
"""Exact endpoint-source extraction and zero-collar budgets; no support cover."""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
from flint import arb, acb, ctx
import sympy as sy

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_hybrid_zero_pair_reduction.md'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ar(value):
    v=F(value)
    return arb(v.numerator)/v.denominator


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision',type=int,default=256)
    parser.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-hybrid-zero-pair-reduction.json')
    args=parser.parse_args();assert args.precision>=160;ctx.prec=args.precision
    ph,sh=sha(PROOF),sha(__file__)
    specs=[('mixed_all_endpoint_support','certify'),('mixed_endpoint_support_grid','check'),('mixed_real_zero_collar','certify')]
    deps={};records={}
    for stem,prefix in specs:
        pp=f'notes/research_{stem}.md';ss=f'experiments/{prefix}_{stem}.py';rr=f'repro/results/research-{stem.replace("_","-")}.json'
        for p in(pp,ss,rr):deps[p]=sha(ROOT/p)
        rec=json.loads((ROOT/rr).read_text());assert rec['status']=='passed'
        assert rec['proof_sha256']==deps[pp] and rec['script_sha256']==deps[ss]
        for key in('dependencies','dependencies_sha256'):
            for p,h in rec.get(key,{}).items():
                assert sha(ROOT/p)==h,p
                if p in deps:assert deps[p]==h
                deps[p]=h
        records[stem]=rec
    source={}
    for row in records['mixed_all_endpoint_support']['source_grid']:
        if F(row['kappa'])==0:
            key=(*row['source'],F(row['height']));assert key not in source
            source[key]=F(row['upper'])
    for row in records['mixed_endpoint_support_grid']['source_grid']:
        if F(row['kappa'])==0:
            key=(0,1,1,F(row['height']));assert key not in source
            source[key]=F(row['upper'])
    heights={0:[F('-.03'),F(0),F('.02')],1:[F('-.057'),F(0),F('.014')]}
    A={(e,d):max(source[e,d,1,h]for h in heights[d])for e in(0,1)for d in(0,1)}
    B={e:max(source[e,e,0,h]for h in heights[e])for e in(0,1)}
    assert A=={(0,0):F('.360050'),(0,1):F('.447948'),(1,0):F('.485081'),(1,1):F('.551147')}
    assert B=={0:F('.347548'),1:F('.515591')}
    exact=6
    P,p,X=sy.symbols('P p X',nonzero=True);j,N=sy.symbols('j N',integer=True)
    for e in(0,1):
        for c in(0,1):
            assert sy.simplify(X**(-c*j)*p*P/P**(2+e)-X**(-c*j)*p/P**(1+e))==0
            exact+=1
    for d in(0,1):
        for selected in range(d+1):
            assert 2*F(d,2)==d and 2*F(d*selected,2)==d*selected
            exact+=1
        assert F(d,2)+F(d,2)==d;exact+=1
    L=F(1,1000);pi=arb.pi();ii=acb(0,1)
    g=(((-2*pi*ii*ar(L)).exp()).polylog(2)-pi*pi/6)/(2*pi*ii)
    nu=-g.real;delta=ar(L)*arb(2).log()+nu
    assert nu>0 and delta>0 and 2*delta+nu<ar('1/50')
    assert 2*(2*pi*ar(L)).sin()<ar('1/2')
    scalar=4
    assert ph==sha(PROOF) and sh==sha(__file__)
    assert all(sha(ROOT/p)==h for p,h in deps.items())
    result=dict(status='passed',precision_bits=args.precision,exact_checks=exact,scalar_comparisons=scalar,
                source_records=len(specs),left_endpoint_constants={f'{e}{d}':str(v)for(e,d),v in A.items()},
                right_endpoint_constants={str(e):str(v)for e,v in B.items()},low_cutoff=str(L),
                low_fourier_rate=str(nu),row_increment=str(delta),maximum_pair_collar_cost=str(2*delta+nu),
                proof_sha256=ph,script_sha256=sh,dependencies_sha256=deps,
                scope='Complete original endpoint-row height-band extension and zero-collar transfer budgets only; no geometric pair support cover or whole-region source theorem.')
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',exact,'exact checks +',scalar,'scalar comparisons +',len(specs),'source records',flush=True)


if __name__=='__main__':main()
