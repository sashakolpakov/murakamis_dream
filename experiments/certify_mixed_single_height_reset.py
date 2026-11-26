#!/usr/bin/env python3
"""Outward directional Hessian bounds for one outer height reset."""
import argparse
import hashlib
import importlib.util
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_single_height_reset.md'
HELPER = ROOT / 'experiments/certify_mixed_real_small_support.py'
spec = importlib.util.spec_from_file_location('reset_root_arithmetic', HELPER)
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)
R = {0: ['.30','.39','-.03','.02'], 1: ['.27','.33','-.057','-.02']}
U = {0: ['.22','.50','-.03','.02'], 1: ['.22','.50','-.057','0']}
DEPS = [
    'experiments/certify_mixed_real_small_support.py',
    'notes/research_mixed_unselected_right_taper_products.md',
    'experiments/certify_mixed_right_square_conditional_packets.py',
    'repro/results/research-mixed-right-square-conditional-packets.json',
    'notes/research_mixed_fourier_weight_continuation.md',
]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def edge(rect, face, lo, hi):
    xl,xh,yl,yh = map(F,rect)
    t = core.ar(lo).union(core.ar(hi))
    if face in (0,2):
        return acb(core.ar(xl)+core.ar(xh-xl)*t,core.ar(yl if face==0 else yh))
    return acb(core.ar(xh if face==1 else xl),core.ar(yl)+core.ar(yh-yl)*t)


def test(case,address,witness=None):
    eta,eps,j,fa,fb=case
    al,ah,bl,bh=core.box(address)
    ra=U[eta] if j==0 else R[eta]
    rb=U[eps] if j==1 else R[eps]
    a,b=edge(ra,fa,al,ah),edge(rb,fb,bl,bh)
    a0=edge(ra,fa,(al+ah)/2,(al+ah)/2)
    b0=edge(rb,fb,(bl+bh)/2,(bl+bh)/2)
    packet=core.root_box(a,b,a0,b0,eps,witness)
    if packet is None:
        return None
    s,_,wit=packet
    _,_,H=core.phase(s,a,b,eta,eps)
    h=H[j][j]
    A,B=-h.real,h.imag
    if not A>0:
        return None
    margin=14*A-A*A-B*B
    if not margin>0:
        return None
    return wit,A.lower(),margin.lower(),((A*A+B*B)/A).upper()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision',type=int,default=256)
    parser.add_argument('--input',type=Path)
    parser.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-single-height-reset.json')
    args=parser.parse_args()
    assert args.precision>=128
    ctx.prec=args.precision
    core.pi,core.ii=arb.pi(),acb(0,1)
    initial={p:sha(ROOT/p) for p in DEPS}
    ph,sh=sha(PROOF),sha(__file__)
    source_record=json.loads((ROOT/DEPS[3]).read_text())
    assert source_record['status']=='passed'
    assert source_record['script_sha256']==initial[DEPS[2]]
    source_deps=source_record.get('dependencies_sha256',source_record.get('dependencies',{}))
    assert source_record.get('proof_sha256',source_deps.get(DEPS[1]))==initial[DEPS[1]]
    assert all(sha(ROOT/p)==h for p,h in source_deps.items())
    input_hash=sha(args.input) if args.input else None
    saved=json.loads(args.input.read_text()) if args.input else None
    if saved:
        assert saved['status']=='passed'
        assert saved['proof_sha256']==ph and saved['script_sha256']==sh
        assert saved['dependencies']==initial
    expected=list(itertools.product((0,1),(0,1),(0,1),range(4),range(4)))
    if saved:
        assert [tuple(row['case']) for row in saved['cases']]==expected
    rows=[];total=0;leastA=None;leastMargin=None;largestK=None
    for idx,case in enumerate(expected):
        pending=[('',None)] if saved is None else [(x['address'],x['witness']) for x in saved['cases'][idx]['leaves']]
        if saved:
            core.cover([a for a,w in pending])
        leaves=[];visited=0
        while pending:
            address,witness=pending.pop();visited+=1
            value=test(case,address,witness)
            if value is None:
                assert saved is None and len(address)<24,(case,address)
                pending.extend(((address+'0',None),(address+'1',None)))
                continue
            wit,aa,mm,kk=value
            leastA=aa if leastA is None else min(leastA,aa)
            leastMargin=mm if leastMargin is None else min(leastMargin,mm)
            largestK=kk if largestK is None else max(largestK,kk)
            leaves.append({'address':address,'witness':wit})
        leaves.sort(key=lambda x:x['address']);core.cover([x['address'] for x in leaves])
        rows.append({'case':list(case),'leaves':leaves,'visited':visited});total+=len(leaves)
    assert ph==sha(PROOF) and sh==sha(__file__)
    assert all(sha(ROOT/p)==h for p,h in initial.items())
    result={'status':'passed','precision_bits':args.precision,'domains':len(rows),'cells':total,
            'min_negative_real_hessian':str(leastA),'min_quadratic_margin':str(leastMargin),
            'max_directional_cost':str(largestK),'reference_rectangles':R,'moving_rectangles':U,
            'cases':rows,'proof_sha256':ph,'script_sha256':sh,'dependencies':initial,
            'scope':'One coordinate stays at its independent geometric reference; the other resets to real [.22,.50]. No complete cyclic or arbitrary selected-exterior estimate.'}
    if saved:
        assert sha(args.input)==input_hash
        result['input_sha256']=input_hash
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',len(rows),'domains',total,'cells; cost bound',largestK,flush=True)


if __name__=='__main__':
    main()
