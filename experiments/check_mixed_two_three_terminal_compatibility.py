#!/usr/bin/env python3
"""Exact fixed-point clipping for the original two-vertex(3,3) input."""
import argparse
from fractions import Fraction as F
import hashlib,json
from pathlib import Path
from flint import acb,arb,ctx
import sympy as sp
import certify_mixed_open_word_critical_localization as base

ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_two_three_terminal_compatibility.md'
ar,cp=base.ar,base.cp
SURVIVORS=[2030,2031,2033,2034,2123,2126]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision',type=int,default=256)
    parser.add_argument('--input',type=Path)
    parser.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-two-three-terminal-compatibility.json')
    args=parser.parse_args();assert args.precision>=192;ctx.prec=args.precision
    ph,sh=sha(PROOF),sha(__file__);ih=sha(args.input)if args.input else None
    saved=json.loads(args.input.read_text())if args.input else None
    deps={};primary={}
    def bind(p,h=None):
        hh=sha(ROOT/p)
        if h is not None:assert hh==h,p
        assert p not in deps or deps[p]==hh
        deps[p]=hh;return hh
    def read(p):
        primary[p]=bind(p);r=json.loads((ROOT/p).read_text());assert r['status']=='passed'
        for key in('dependencies_sha256','dependencies'):
            for pp,hh in r.get(key,{}).items():bind(pp,hh)
        return r
    p='repro/results/research-mixed-terminal-coupled-disk-gap.json'
    r='repro/results/research-mixed-terminal-coupled-disk-gap-replay.json'
    ca,cr=read(p),read(r)
    assert cr['input_sha256']==deps[p]
    for rec in(ca,cr):
        assert rec['circle_cells']==165 and rec['raw_majorant_branches']==4
        assert rec['multiplier']=='1/200'and rec['floor']=='1/4000'
        bind('notes/research_mixed_terminal_coupled_disk_gap.md',rec['proof_sha256'])
        bind('experiments/check_mixed_terminal_coupled_disk_gap.py',rec['script_sha256'])
    p='repro/results/research-mixed-open-word-critical-localization.json'
    r='repro/results/research-mixed-open-word-critical-localization-replay.json'
    original,replay=read(p),read(r)
    assert replay['input_sha256']==deps[p]and original['domains']==replay['domains']
    for rec in(original,replay):
        bind('notes/research_mixed_open_word_critical_localization.md',rec['proof_sha256'])
        bind('experiments/certify_mixed_open_word_critical_localization.py',rec['script_sha256'])
    if saved:
        assert saved['status']=='passed'
        assert saved['proof_sha256']==ph and saved['script_sha256']==sh
        assert saved['dependencies_sha256']==deps
    s,t,x,e,u,v=sp.symbols('s t x e u v')
    Q=t*x-s*t-x*e+s*u+e*v
    assert sp.expand(Q.xreplace({s:e,t:x,x:t,e:s,u:v,v:u})-Q)==0
    V=sp.symbols('V')
    assert sp.cancel((1-V*(1-V)**2/(1-V**2))/V-(1+V**2)/(V*(1+V)))==0
    domain=original['domains'][0]
    assert(domain['epsilon'],domain['neighbor_epsilon'])==(0,0)
    stack=[([(F(-1),F(1)),(F(-1),F(1))],0)]
    nodes=leaves=excluded=discarded=0;rows=[];minimum=None
    for ni,node in enumerate(domain['tree']):
        assert stack
        box,depth=stack.pop();nodes+=1
        if node[0]=='S':
            assert node[1]==depth%2
            left,right=base.split(box,node[1]);stack.extend([(left,depth+1),(right,depth+1)])
            continue
        if node[0]=='X':
            assert base.excluded(box);excluded+=1;continue
        assert node[0]=='L';leaves+=1
        w=node[1];radius=F(w['radius']);center=list(map(F,w['centers'][1]))
        cr,ci,scale=base.DISKS[0]
        inputs=[(c+scale*lo,c+scale*hi)for c,(lo,hi)in zip((cr,ci),box)]
        outputs=[(c-radius,c+radius)for c in center]
        clipped=[(max(a,c),min(b,d))for(a,b),(c,d)in zip(inputs,outputs)]
        if any(lo>hi for lo,hi in clipped):
            discarded+=1;continue
        assert base.test(w,base.parameter(box,0),0)is not None
        a=acb(ar(clipped[0][0]).union(ar(clipped[0][1])),
              ar(clipped[1][0]).union(ar(clipped[1][1])))
        assert abs(a-acb(ar('.35'),ar('-.01')))<ar('.083')
        pi,ii=arb.pi(),acb(0,1)
        V=(-2*pi*ii*a).exp();den=V*(1+V)
        assert abs(den)>0
        U=(1+V*V)/den
        assert abs(U)>0
        psi=abs(U).log()+ar('.13')*pi
        assert psi>0
        low=psi.lower()
        if minimum is None or low<minimum:minimum=low
        rows.append(dict(node=ni,clipped_rectangle=[[str(x)for x in side]for side in clipped],
                         fixed_point_surrogate_U=str(U),psi_fp_lower=str(low)))
    assert not stack
    assert(nodes,leaves,excluded,discarded)==(3439,1645,75,1639)
    assert[r['node']for r in rows]==SURVIVORS
    if saved:
        assert[(r['node'],r['clipped_rectangle'])for r in rows]==[(r['node'],r['clipped_rectangle'])for r in saved['survivors']]
    out=dict(status='passed',precision_bits=ctx.prec,exact_identities=2,
        original_nodes=nodes,original_leaves=leaves,original_exclusions=excluded,
        disjoint_fixed_point_cells=discarded,survivors=rows,minimum_psi_fp_lower=str(minimum),
        new_endpoint_roots=0,new_parameter_subdivisions=0,
        scope='Actual complete-color(3,3) length-two reference: the fixed-point surrogate psi_fp is positive throughout each retained rectangle; equality to the original coupling function is used only at the actual fixed point. No ordinary-vertex substitution or original-psi sign for nonfixed targets.',
        proof_sha256=ph,script_sha256=sh,primary_records_sha256=primary,dependencies_sha256=deps)
    if ih:out['input_sha256']=ih
    assert sha(PROOF)==ph and sha(__file__)==sh
    assert all(sha(ROOT/p)==h for p,h in deps.items())
    if ih:assert sha(args.input)==ih
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print('PASS2 identities/1645 leaves/6 fixed-point survivors; psi_fp>',minimum,'bindings',len(deps))

if __name__=='__main__':main()
