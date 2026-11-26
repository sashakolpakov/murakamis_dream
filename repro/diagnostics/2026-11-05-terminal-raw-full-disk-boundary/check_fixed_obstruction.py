#!/usr/bin/env python3
"""One original-map raw-row obstruction; no actual-word/kernel counterexample."""
from fractions import Fraction as F
import hashlib,json
from pathlib import Path
import sys
from flint import arb,acb,ctx

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
sys.path.insert(0,str(ROOT/'experiments'))
import check_mixed_terminal_raw_half_gap as raw
core,base,end=raw.core,raw.base,raw.end
ar=raw.ar

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    ctx.prec=320
    pi,ii=arb.pi(),acb(0,1)
    core.PI,core.II,core.HALF=pi,ii,acb(ar('1/2'))
    end.PI,end.II=pi,ii
    raw.PI,raw.II,raw.HALF=pi,ii,core.HALF
    deps={}
    def bind(p,expected=None):
        h=sha(ROOT/p)
        if expected is not None:assert h==expected,p
        assert p not in deps or deps[p]==h
        deps[p]=h
    ap='repro/results/research-mixed-open-word-critical-localization.json'
    rp='repro/results/research-mixed-open-word-critical-localization-replay.json'
    bind(ap);bind(rp)
    author=json.loads((ROOT/ap).read_text());replay=json.loads((ROOT/rp).read_text())
    assert author['status']==replay['status']=='passed'
    assert replay['input_sha256']==deps[ap]
    assert author['domains']==replay['domains']
    for record in(author,replay):
        bind('notes/research_mixed_open_word_critical_localization.md',record['proof_sha256'])
        bind('experiments/certify_mixed_open_word_critical_localization.py',record['script_sha256'])
        for p,h in record['dependencies_sha256'].items():bind(p,h)
    for p in ['experiments/check_mixed_terminal_raw_half_gap.py',
              'experiments/check_mixed_terminal_half_endpoint_gap.py',
              'experiments/certify_mixed_endpoint_packet_extension.py',
              'notes/research_mixed_terminal_half_endpoint_gap.md',
              'notes/research_mixed_terminal_conditional_packet.md',
              'notes/research_mixed_terminal_half_row_envelope.md']:
        bind(p)
    domain=author['domains'][0]
    assert(domain['epsilon'],domain['neighbor_epsilon'])==(0,0)
    pending=[([(F(-1),F(1)),(F(-1),F(1))],0)]
    witness=None
    for ni,node in enumerate(domain['tree']):
        assert pending
        box,depth=pending.pop()
        if node[0]=='S':
            assert node[1]==depth%2
            left,right=base.split(box,node[1]);pending.extend([(left,depth+1),(right,depth+1)])
        elif node[0]=='X':
            assert base.excluded(box)
        else:
            assert node[0]=='L'
            if ni==1685:
                assert box==[(F(-9,16),F(-1,2)),(F(11,16),F(3,4))]
                assert base.test(node[1],base.parameter(box,0),0)is not None
                witness=node[1]
    assert not pending and witness is not None
    ax,ay=F(967,3200),F(7,128)
    a=acb(ar(ax),ar(ay))
    assert (ax-F(7,20))**2+(ay+F(1,100))**2==F(33129,5120000)
    assert F(33129,5120000)<F(83,1000)**2
    point=dict(witness,radius='1/10000000000')
    assert base.test(point,a,0)is not None
    rr=ar(point['radius'])
    e,t,u=[base.cp(c)+acb(arb(0,rr),arb(0,rr))for c in point['centers']]
    reference=core.action(a,e,t,u,0).real
    uh=acb(ar('1/4'),arb(3).log()/(4*pi))
    hhalf=(end.J(raw.HALF)+end.phase(raw.HALF,uh)).real
    trial=F(67,250)
    fixed_row=raw.row(ar(trial),a,0)
    excess=hhalf+fixed_row-reference
    assert excess>ar(F(7,10000)),excess
    assert all(sha(ROOT/p)==h for p,h in deps.items())
    out=dict(status='passed_fixed_original_map_obstruction',precision_bits=ctx.prec,
        scope='A single allowed endpoint-map input inside the smaller type-three disk; the raw lower-row envelope exceeds the optimized terminal phase. This is not an actual-word realization or a counterexample to the coherent kernel, invariant, or conjecture.',
        epsilon=0,neighbor_epsilon=0,external=[str(ax),str(ay)],
        original_domain=0,original_node=1685,row=str(trial),
        point_witness=point,reference_action=str(reference),
        h_half=str(hhalf),fixed_raw_row=str(fixed_row),
        excess=str(excess),excess_lower=str(excess.lower()),floor='7/10000',
        dependencies_sha256=deps,script_sha256=sha(__file__),
        new_endpoint_roots=0,new_parameter_subdivisions=0)
    (HERE/'fixed-obstruction.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS fixed row excess',excess,flush=True)

if __name__=='__main__':main()

