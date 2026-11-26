#!/usr/bin/env python3
"""Bounded outward check of one two-height all-four minimum-flow face.

This does not cover a neighborhood in the target real coordinates.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import time

from flint import arb, acb

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
HELPER = ROOT/'experiments/certify_mixed_minimum_level_half_stencils.py'
spec = importlib.util.spec_from_file_location('original_phase_face', HELPER)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
ar = m.ar


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def test(box, witness=None):
    if witness is not None and not F(0)<F(witness['radius'])<=F(1,20):
        return None,None,None
    mid = [(lo+hi)/2 for lo,hi in box]
    hs = [ar(lo).union(ar(hi)) for lo,hi in box]
    zs = [acb(ar('.22'), h) for h in hs]
    z0 = [acb(ar('.22'), ar(h)) for h in mid]
    packet = m.root_box(zs[0],zs[1],z0[0],z0[1],1,witness)
    if packet is None:
        return None,None,None
    s,sc,wit = packet
    assert F(0)<F(wit['radius'])<=F(1,20)
    gp, gpp, ii, pi = m.m.core.gp,m.gpp,m.ii,m.pi
    full = m.gradH(s,*zs,1,1)
    point = m.gradH(sc,*z0,1,1)
    if not all(v.is_finite() for data in (full,point)
               for v in data[0]+[v for row in data[1] for v in row]):
        return None,None,None
    lows, gradients = [], []
    # The unselected height-only left raw edge minimizes at u=2/5.
    uleft = ar(F(2,5))
    for uright in (F(1,5),F(2,5)):
        ur = ar(uright)
        gc = full[0][1]+gp(zs[1]+ur)-ar(F(3,2))*gp(zs[1])+2*pi*ii*ur
        gn = full[0][0]+gp(zs[0]+uleft)-ar(F(3,2))*gp(zs[0])
        gc0 = point[0][1]+gp(z0[1]+ur)-ar(F(3,2))*gp(z0[1])+2*pi*ii*ur
        gn0 = point[0][0]+gp(z0[0]+uleft)-ar(F(3,2))*gp(z0[0])
        rc = gpp(zs[1]+ur)-ar(F(3,2))*gpp(zs[1])
        rn = gpp(zs[0]+uleft)-ar(F(3,2))*gpp(zs[0])
        HH = full[1]
        for chin,chic in itertools.product((0,1),repeat=2):
            qc = 1+ii*chic*hs[1]/ar('.12')
            qn = ii*chin*hs[0]/ar('.12')
            qc0 = 1+ii*chic*ar(mid[1])/ar('.12')
            qn0 = ii*chin*ar(mid[0])/ar('.12')
            value = (qc*gc+qn*gn).real
            center = (qc0*gc0+qn0*gn0).real
            grad = [
                (qc*ii*HH[1][0]+qn*ii*(HH[0][0]+rn)
                 +ii*chin*gn/ar('.12')).real,
                (qc*ii*(HH[1][1]+rc)+qn*ii*HH[0][1]
                 +ii*chic*gc/ar('.12')).real,
            ]
            if not all(v.is_finite() for v in [value,center]+grad):
                return None,None,None
            taylor = center-sum((abs(g)*ar((hi-lo)/2)
                                for g,(lo,hi) in zip(grad,box)),arb(0))
            lows.append(max(value.lower(),taylor.lower()))
            gradients.append(grad)
    return min(lows),gradients,wit


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision',type=int,default=256)
    ap.add_argument('--input',type=Path)
    ap.add_argument('--output',type=Path,default=HERE/'author.json')
    ap.add_argument('--max-visits',type=int,default=4095)
    ap.add_argument('--seconds',type=float,default=30)
    args = ap.parse_args()
    m.configure(args.precision)
    paths = [Path(__file__).resolve(),HERE/'README.md',HELPER,
        ROOT/'experiments/certify_mixed_isolated_transition_phase.py',
        ROOT/'experiments/certify_mixed_real_small_support.py',
        ROOT/'notes/research_mixed_global_cotangent_roots.md',
        ROOT/'notes/research_mixed_raw_row_stationarity.md',
        ROOT/'experiments/check_mixed_raw_row_stationarity.py',
        ROOT/'repro/results/research-mixed-raw-row-stationarity.json']
    deps = {str(p.relative_to(ROOT)):sha(p) for p in paths}
    stationarity=json.loads(paths[-1].read_text())
    assert stationarity['status']=='passed'
    assert stationarity['proof_sha256']==deps['notes/research_mixed_raw_row_stationarity.md']
    assert stationarity['script_sha256']==deps['experiments/check_mixed_raw_row_stationarity.py']
    assert stationarity['row_endpoints']==['1/5','2/5']
    assert stationarity['physical_branch_count']==12
    for path,digest in stationarity['dependencies_sha256'].items():
        assert path not in deps or deps[path]==digest
        assert sha(ROOT/path)==digest
        deps[path]=digest
    old,ih = None,None
    if args.input:
        raw=args.input.read_bytes();ih=hashlib.sha256(raw).hexdigest();old=json.loads(raw)
        assert old['status']=='passed' and old['dependencies_sha256']==deps
    stack=[[(F('-.057'),F('-.02'))]*2]
    cursor=leaves=visits=0
    nodes=[];minimum=None;started=time.monotonic()
    status='passed'
    while stack:
        if not old and (visits >= args.max_visits or time.monotonic()-started > args.seconds):
            status='incomplete';break
        box=stack.pop();visits+=1
        if old:
            node=old['nodes'][cursor];cursor+=1
            if node[0]=='S':
                axis=node[1];lo,hi=box[axis];mid=(lo+hi)/2
                for interval in ((lo,mid),(mid,hi)):
                    child=list(box);child[axis]=interval;stack.append(child)
                nodes.append(node);continue
            assert node[0]=='L'
            lower,grads,wit=test(box,node[1])
        else:
            lower,grads,wit=test(box)
        if lower is not None and lower > ar(F(1,50)):
            leaves+=1
            minimum=lower if minimum is None else min(minimum,lower)
            nodes.append(['L',wit])
            continue
        assert old is None,('saved leaf fails',cursor,str(lower))
        if grads is None:
            axis=max((hi-lo,j)for j,(lo,hi)in enumerate(box))[1]
        else:
            axis=max((max((abs(g[j])*ar(hi-lo)).upper() for g in grads),j)
                     for j,(lo,hi)in enumerate(box))[1]
        lo,hi=box[axis];mid=(lo+hi)/2
        assert hi-lo > F(1,2**24)
        nodes.append(['S',axis])
        for interval in ((lo,mid),(mid,hi)):
            child=list(box);child[axis]=interval;stack.append(child)
    if old:
        assert not stack and cursor==len(old['nodes'])
        assert leaves==old['accepted_cells'] and visits==old['visited_cells']
        assert ih==sha(args.input)
    assert all(sha(ROOT/p)==h for p,h in deps.items())
    result=dict(status=status,precision_bits=args.precision,accepted_cells=leaves,
        visited_cells=visits,remaining_boxes=len(stack),smooth_functions=8,
        height_box=['-57/1000','-1/50'],fixed_reals=['11/50','11/50'],
        lower_target='1/50',minimum_lower_bound=str(minimum),nodes=nodes,
        elapsed_seconds=time.monotonic()-started,dependencies_sha256=deps,
        scope='Outward two-height face only: unselected type4 neighbor and moving center both at real .22, right raw edges on both outside ends, all negative-height-cost switches. No t/neighbor-real neighborhood, selected/mixed-type case, or whole-flow sign.')
    if ih:result['input_sha256']=ih
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(status.upper(),leaves,'leaves',visits,'visits; minimum',minimum,flush=True)


if __name__=='__main__':
    main()
