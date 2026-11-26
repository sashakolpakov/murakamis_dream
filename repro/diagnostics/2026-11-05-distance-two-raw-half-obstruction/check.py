#!/usr/bin/env python3
"""One fixed outward obstruction in the old independent half-stencil box."""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
from flint import arb, acb, ctx

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision',type=int,default=320)
    parser.add_argument('--output',type=Path,default=HERE/'result.json')
    args=parser.parse_args();assert args.precision>=160
    ctx.prec=args.precision
    deps={}
    def bind(path,expected=None):
        value=sha(ROOT/path)
        if expected is not None:assert value==expected,path
        if path in deps:assert deps[path]==value,path
        deps[path]=value
    primary={}
    for stem,prefix in [('mixed_raw_row_stationarity','check'),
                        ('mixed_closed_cotangent_roots','check'),
                        ('mixed_neighbor_conditioned_critical_boxes','certify')]:
        path='repro/results/research-'+stem.replace('_','-')+'.json'
        raw=(ROOT/path).read_bytes();bind(path,hashlib.sha256(raw).hexdigest())
        record=json.loads(raw);assert record['status']=='passed'
        bind('notes/research_'+stem+'.md',record['proof_sha256'])
        bind('experiments/'+prefix+'_'+stem+'.py',record['script_sha256'])
        for field in ('dependencies','dependencies_sha256'):
            for name,digest in record.get(field,{}).items():bind(name,digest)
        primary[stem]=record
    bind('notes/research_mixed_minimum_level_half_stencils.md')
    bind(str((HERE/'README.md').relative_to(ROOT)))
    bind(str(Path(__file__).resolve().relative_to(ROOT)))
    assert primary['mixed_raw_row_stationarity']['row_endpoints']==['1/5','2/5']
    table=primary['mixed_neighbor_conditioned_critical_boxes']['limits_in_thousandths']['101']
    assert table[1]==[-25,-11] and table[2]==[-53,-34]
    assert -30<table[1][0] and -57<table[2][0]
    pi=arb.pi();ii=acb(0,1)
    def ar(v):
        v=F(v);return arb(v.numerator)/v.denominator
    def gp(z):return (1-(-2*pi*ii*z).exp()).log()
    t=ar(F(21999,100000));x=ar(F(11,50))
    cc=ar(F(-57,1000));cn=ar(F(-3,100));r=(t-ar(F(1,10)))/ar(F(3,25))
    a=acb(t,cc*r);b=acb(x,cn*r)
    P,Q=(pi*a).cot(),(pi*b).cot()
    assert P.real>0 and Q.real>0 and abs(P.imag)<ar(F(1,2)) and abs(Q.imag)<ar(F(1,2))
    S=(-(P+Q)+((P+Q)**2+4-4*ii*(Q-P)).sqrt())/2
    assert S.real>0 and abs(S.imag)<1
    s=((S+ii)/(S-ii)).log()/(2*pi*ii)
    assert 0<s.real<ar(F(1,2)) and all(0<z.real<1 for z in (s,s+a,s+b))
    assert (S*S+(P+Q)*S-1+ii*(Q-P)).contains(0)
    eq=gp(s+a)+gp(s+b)-2*gp(s)+2*pi*ii*a
    # Exact quadratic identity gives exp(eq)=1; this excludes all
    # nonzero logarithmic lifts on the regular original branch.
    assert abs(eq)<1
    ga=gp(s+a)+2*pi*ii*s-ar(F(3,2))*gp(a)
    gb=gp(s+b)-gp(b)
    lo,hi=ar(F(2577507243,10**10)),ar(F(2577507245,10**10))
    def rowder(u):
        return ((2*(pi*u).cos()).log()+gp(b+u).real
                -3*(2*(pi*u).sin()).log()-2*pi*b.imag)
    assert ar(F(1,5))<lo<hi<ar(F(2,5))
    assert rowder(lo)>0 and rowder(hi)<0
    u=lo.union(hi)
    K=gp(b+u)-gp(b)+2*pi*ii*u
    inner=((1+ii*cc/ar(F(3,25)))*(ga-ar(F(3,2))*ii)).real
    coherent_height=(ii*cn/ar(F(3,25))*gb).real
    raw_height=(ii*cn/ar(F(3,25))*K).real
    total=inner+coherent_height+raw_height
    assert raw_height>0 and total<ar(F(-7,5000))
    assert all(sha(ROOT/path)==digest for path,digest in deps.items())
    result=dict(status='passed',precision_bits=args.precision,
        scope='Single old independent-height-box right half, types(center,neighbor,R)=(4,3,4), chi=xi=1. BOTH coefficients are excluded by actual conditioned101 geometry. No actual-reference, whole-flow, or finite-source counterexample.',
        t='21999/100000',neighbor_real='11/50',center_height_coefficient='-57/1000',neighbor_height_coefficient='-3/100',
        coherent_root=str(s),original_log_residual=str(eq),raw_row=str(u),
        raw_row_rational_bracket=['2577507243/10000000000','2577507245/10000000000'],
        row_derivative_left=str(rowder(lo)),row_derivative_right=str(rowder(hi)),
        inner_center_term=str(inner),inner_neighbor_height_term=str(coherent_height),
        favorable_raw_height_term=str(raw_height),old_gauged_half=str(total),
        strict_half_upper='-7/5000',actual_conditioned_101_excludes_both_coefficients=True,
        new_parameter_cover=False,dependencies_sha256=deps)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS fixed half',total,';',len(deps),'current bindings; both coefficients excluded by actual geometry')

if __name__=='__main__':main()
