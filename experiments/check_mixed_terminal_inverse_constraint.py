#!/usr/bin/env python3
"""Exact terminal coupling and one incompatible original endpoint-map input."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

from flint import acb,arb,ctx
import sympy as sp
import certify_mixed_open_word_critical_localization as base

ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_terminal_inverse_constraint.md'
ar,cp=base.ar,base.cp

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision',type=int,default=256)
    parser.add_argument('--input',type=Path)
    parser.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-terminal-inverse-constraint.json')
    args=parser.parse_args();assert args.precision>=192;ctx.prec=args.precision
    ph,sh=sha(PROOF),sha(__file__)
    ih=sha(args.input)if args.input else None
    saved=json.loads(args.input.read_text())if args.input else None
    deps={}
    def bind(path,expected=None):
        hh=sha(ROOT/path)
        if expected is not None:assert hh==expected,path
        assert path not in deps or deps[path]==hh
        deps[path]=hh;return hh
    ap='repro/results/research-mixed-open-word-critical-localization.json'
    rp='repro/results/research-mixed-open-word-critical-localization-replay.json'
    bind(ap);bind(rp)
    author=json.loads((ROOT/ap).read_text());replay=json.loads((ROOT/rp).read_text())
    assert author['status']==replay['status']=='passed'
    assert replay['input_sha256']==deps[ap]and author['domains']==replay['domains']
    for r in(author,replay):
        bind('notes/research_mixed_open_word_critical_localization.md',r['proof_sha256'])
        bind('experiments/certify_mixed_open_word_critical_localization.py',r['script_sha256'])
        for p,h in r['dependencies_sha256'].items():bind(p,h)
    fixedpath='repro/diagnostics/2026-11-05-terminal-raw-full-disk-boundary/fixed-obstruction.json'
    bind(fixedpath);fixed=json.loads((ROOT/fixedpath).read_text())
    assert fixed['status']=='passed_fixed_original_map_obstruction'
    bind('repro/diagnostics/2026-11-05-terminal-raw-full-disk-boundary/check_fixed_obstruction.py',fixed['script_sha256'])
    for p,h in fixed['dependencies_sha256'].items():bind(p,h)
    for p in ['notes/research_mixed_cyclic_critical_height_bounds.md',
              'notes/research_mixed_open_word_endpoint_rectangles.md',
              'notes/research_mixed_open_local_factor_coverage.md',
              'repro/results/research-mixed-open-word-endpoint-rectangles.json',
              'repro/results/research-mixed-cyclic-block-boundary-images.json',
              'repro/results/research-mixed-cyclic-block-boundary-images-replay.json']:
        bind(p)
    extracted=json.loads((ROOT/'repro/results/research-mixed-open-word-endpoint-rectangles.json').read_text())
    assert extracted['status']=='passed'
    bind('notes/research_mixed_open_word_endpoint_rectangles.md',extracted['proof_sha256'])
    bind('experiments/check_mixed_open_word_endpoint_rectangles.py',extracted['script_sha256'])
    for p,h in extracted['dependencies_sha256'].items():bind(p,h)
    if saved:
        assert saved['status']=='passed'
        assert saved['proof_sha256']==ph and saved['script_sha256']==sh
        assert saved['dependencies_sha256']==deps
    V,B=sp.symbols('V B');exact=[]
    for d in(2,3):
        U=(1-B*(1-V)**d/(1-V*B))/V
        A=(1-U*V)/((1-U)**d+U*(1-U*V))
        for expression in ((1-U*V)*(1-V*B)-B*(1-V)**d,
                           (1-U*V)*(1-U*A)-A*(1-U)**d):
            assert sp.cancel(expression)==0;exact.append(True)
    domain=author['domains'][0]
    assert(domain['epsilon'],domain['neighbor_epsilon'])==(0,0)
    pending=[([(F(-1),F(1)),(F(-1),F(1))],0)];witness=None
    for ni,node in enumerate(domain['tree']):
        assert pending
        box,depth=pending.pop()
        if node[0]=='S':
            assert node[1]==depth%2
            left,right=base.split(box,node[1]);pending.extend([(left,depth+1),(right,depth+1)])
        elif node[0]=='X':assert base.excluded(box)
        else:
            assert node[0]=='L'
            if ni==1685:
                assert box==[(F(-9,16),F(-1,2)),(F(11,16),F(3,4))]
                assert base.test(node[1],base.parameter(box,0),0)is not None
                witness=node[1]
    assert not pending and witness is not None
    ax,ay=F(967,3200),F(7,128)
    assert fixed['external']==[str(ax),str(ay)]and fixed['original_node']==1685
    assert fixed['epsilon']==fixed['neighbor_epsilon']==0
    assert (ax-F(7,20))**2+(ay+F(1,100))**2==F(33129,5120000)<F(83,1000)**2
    pi,ii=arb.pi(),acb(0,1);a=acb(ar(ax),ar(ay))
    point=dict(witness,radius='1/10000000000')
    assert point==fixed['point_witness']
    if saved:assert saved['point_witness']==point
    assert base.test(point,a,0)is not None
    rr=ar(point['radius']);b=cp(point['centers'][1])+acb(arb(0,rr),arb(0,rr))
    V=(-2*pi*ii*a).exp();B=(-2*pi*ii*b).exp();den=1-V*B
    assert abs(den)>0
    U=(1-B*(1-V)**2/den)/V
    q_floor=(-ar('.24')*pi).exp()
    assert abs(U)<q_floor
    assert ay>F(21,1000)
    assert abs(U)<(-ar('.13')*pi).exp()
    out=dict(status='passed',precision_bits=ctx.prec,exact_identities=len(exact),
        original_domain=0,original_node=1685,external=[str(ax),str(ay)],point_witness=point,
        endpoint_attached=str(b),inverse_U=str(U),inverse_U_modulus=str(abs(U)),
        Q_modulus_floor=str(q_floor),Q_exclusion_margin=str(q_floor-abs(U)),
        stronger_ordinary_type3_exclusion_margin=str((-ar('.13')*pi).exp()-abs(U)),
        length_two_excluded=True,length_ge_three_excluded=True,
        scope='Necessary compatibility only: the fixed independent-disk raw obstruction is not an actual open-word terminal neighbor. No feasible-domain raw-gap or kernel noncancellation conclusion.',
        new_endpoint_roots=0,new_parameter_subdivisions=0,
        proof_sha256=ph,script_sha256=sh,dependencies_sha256=deps)
    if ih:out['input_sha256']=ih
    assert sha(PROOF)==ph and sha(__file__)==sh
    assert all(sha(ROOT/p)==h for p,h in deps.items())
    if ih:assert sha(args.input)==ih
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print('PASS',len(exact),'identities; fixed original-map exclusion margin',q_floor-abs(U),';',len(deps),'bindings')

if __name__=='__main__':main()
