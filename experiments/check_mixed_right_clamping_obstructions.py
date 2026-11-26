#!/usr/bin/env python3
"""Outward point counterexamples to two stronger right-clamp estimates."""
import argparse,hashlib,importlib.util,json
from fractions import Fraction as F
from pathlib import Path
from flint import arb,acb

ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_right_clamping_obstructions.md'
HELPERS=['experiments/certify_mixed_minimum_level_half_stencils.py',
         'experiments/certify_mixed_isolated_transition_phase.py',
         'experiments/certify_mixed_real_small_support.py']
spec=importlib.util.spec_from_file_location('clamp_obstruction_roots',ROOT/HELPERS[0])
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision',type=int,default=320)
    ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-right-clamping-obstructions.json')
    args=ap.parse_args();assert args.precision>=192
    ph,sh=sha(PROOF),sha(__file__);deps={p:sha(ROOT/p)for p in HELPERS}
    m.configure(args.precision)
    ar=m.ar;pi=m.pi;ii=m.ii;g=m.m.core.g;gp=m.m.core.gp
    witnesses=[]
    def phase(a,b,eta,eps):
        packet=m.root_box(a,b,a,b,eps);assert packet is not None
        _,s,w=packet;assert F(0)<F(w['radius'])<=F(1,20)
        value=g(s+a)+g(s+b)-(2+eps)*g(s)+2*pi*ii*a*s
        value-=(1+ar(F(eta,2)))*g(a)+(1+ar(F(eps,2)))*g(b)
        gradient,_=m.gradH(s,a,b,eta,eps)
        witnesses.append(w)
        return value,gradient
    z=acb(ar('1/2'));t=ar('481/1000');h=ar('2527/1250000')
    assert F('7/500')*400*(F('1/2')-F('481/1000'))**2==F('2527/1250000')
    b=acb(t,h);q=1+ii*ar('7/500')*(-800*(ar('1/2')-t))
    l,r=phase(z,b,1,1),phase(b,z,1,1)
    fb=l[1][1]+r[1][0]
    gap=-2*pi*h-g(b).real
    active=((fb+2*pi*ii)*q).real
    inactive=((fb+gp(b))*q).real
    assert gap>ar('1/2000') and active>ar('1/5') and inactive<0
    x=acb(ar('1/10'));b0=acb(ar('9/20'));u=ar('6/25');v=ar('11/40')
    J=lambda y:g(acb(y)).real
    left=J(ar('1/10')+u)-J(ar('1/10'))+J(ar('1/2')+u)-3*J(u)
    right=J(ar('1/2')+v)+J(ar('1/10')+v)-J(ar('1/10'))-2*J(v)
    raw=left+right-J(ar('1/10'))/2
    baseline=(phase(x,b0,1,1)[0]+phase(b0,x,1,0)[0]).real
    defect=raw-baseline
    assert defect>ar('1/5')
    assert all(v.is_finite()for v in(gap,active,inactive,raw,baseline,defect))
    assert ph==sha(PROOF) and sh==sha(__file__)
    assert all(sha(ROOT/p)==h for p,h in deps.items())
    out=dict(status='passed',precision_bits=args.precision,exact_checks=1,
             outward_comparisons=4,original_root_enclosures=4,
             linear_branch_gap=str(gap),active_linear_derivative=str(active),
             inactive_g_derivative=str(inactive),raw_rate=str(raw),
             baseline_rate=str(baseline),raw_excess=str(defect),root_witnesses=witnesses,
             proof_sha256=ph,script_sha256=sh,dependencies_sha256=deps,
             scope='Counterexamples to selected-path monotonicity and an absolute-row clamping bound; neither contradicts the selected-height or unselected-phase comparison.')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print('PASS 1 exact check, 4 strict outward comparisons, 4 original-log roots')

if __name__=='__main__':main()
