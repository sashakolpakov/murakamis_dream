#!/usr/bin/env python3
"""Exact scalar and inherited-branch checks for the radius .04 cap.

No new optimizer or root solve is used. The existing uniform Newton
certificate and independent replay are retained with their exact hashes.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import argparse
import json
import time

from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[1]


def a(value):
    value = Q(value)
    return arb(value.numerator)/value.denominator


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=192)
    ap.add_argument('--output', default='repro/results/research-three-vertex-large-cap-height-bound.json')
    args=ap.parse_args()
    ctx.prec=args.precision
    start=time.monotonic()
    pi=arb.pi()
    checks=[]
    def positive(name, value):
        assert value>0, (name, value)
        checks.append({'name':name, 'margin':str(value)})

    # The known bound 2c>.646 is an input from the symmetric-height theorem.
    tangent=((pi/20).log()-1)/40
    correction=-(a(Q(24,25))).log()/2
    positive('J one-third endpoint lies below tangent', tangent+a(Q(323,3000)))
    upper=Q(13,25)
    derivative_bound=(3*upper-1)/(6*upper*(1-upper))
    positive('positive-radius derivative bound', a(Q(2,5)-derivative_bound))
    positive('positive-radius correction below negative-radius correction', correction-a(Q(1,125)))
    low=arb(2).log()+tangent+correction+a(Q(3,1250))
    positive('weighted low-sum bound below .645', a(Q(129,200))-low)
    positive('low-sum bound below known central value', a(Q(323,500)-Q(129,200)))
    positive('actual radius lower endpoint', (-pi/100).exp()/2-a(Q(12,25)))
    positive('actual radius upper endpoint', a(Q(13,25))-(pi/100).exp()/2)

    positive('refined unweighted index lower bound', a(Q(1,3)-Q(221,14400)-Q(317,1000)))
    positive('refined unweighted index upper bound', a(Q(35,100)-Q(1,3)-Q(221,14400)))
    positive('index-radius derivative sign', a(1-Q(13,25)**2))
    positive('index-angle derivative sign', a(2*Q(12,25)/(1+Q(12,25)**2))-(pi/4).cos())
    r,s=a(Q(12,25)),a(Q(21,50))
    d=pi*r*(pi*s).sin()/(1+r*r-2*r*(pi*s).cos())
    positive('larger-square coercivity exceeds 7/5', d-a(Q(7,5)))
    positive('reported endpoint value exceeds1.4728', d-a(Q(1841,1250)))
    assert Q(317,1000)-Q(1,4)==Q(67,1000)
    positive('upper index-face distance exceeds .067', a(Q(21,50)-Q(35,100)-Q(67,1000)))
    budget=15*Q(1,200)**2+Q(3,1250)
    loss=Q(7,10)*Q(67,1000)**2
    positive('global index-exit reserve', a(loss-budget))

    positive('left sliding center inside W', a(Q(1,8)-Q(3,25)))
    assert Q(21,50)/2==Q(21,100)
    positive('left W endpoint outside cap', a(Q(1,6)-Q(3,25)-Q(1,25)))
    positive('right W endpoint outside cap', a(Q(21,100)-Q(1,6)-Q(1,25)))
    positive('D lower angle positive', a(Q(1,4)-Q(21,100)))
    positive('D upper angle below half-period', a(Q(1,2)-Q(21,50)+Q(3,25)))
    def fp(u):
        return pi*(2*pi*a(u)).sin()/(a(Q(5,4))-(2*pi*a(u)).cos())
    positive('C left endpoint exceeds3', fp(Q(3,25))-3)
    positive('C right endpoint exceeds3', fp(Q(21,100))-3)
    assert 2*Q(1,4)==Q(1,2)
    positive('sine-strip upper endpoint below1', a(1-2*Q(21,50)))
    positive('old critical branch inside new quadratic region', a(Q(1,25)-Q(1,100)))

    author_path=ROOT/'repro/results/research-three-vertex-weighted-height-bound.json'
    review_path=ROOT/'repro/results/research-three-vertex-weighted-height-bound-replay.json'
    original=json.loads(author_path.read_text())
    review=json.loads(review_path.read_text())
    assert original['status']=='passed' and original['height_cell_count']==2048
    assert review['status']=='passed' and review['height_cell_count']==2048
    assert review['artifact_sha256']==sha256(author_path.read_bytes()).hexdigest()
    assert review['author_script_sha256']==original['script_sha256']
    assert sha256((ROOT/'experiments/certify_three_vertex_weighted_height_bound.py').read_bytes()).hexdigest()==original['script_sha256']
    assert sha256((ROOT/'experiments/replay_three_vertex_weighted_height_bound.py').read_bytes()).hexdigest()==review['script_sha256']
    for path,digest in original['dependencies_sha256'].items():
        assert sha256((ROOT/path).read_bytes()).hexdigest()==digest,path
    seen=set()
    mesh=2048
    for cell in original['height_cells']:
        j=cell['index']
        assert isinstance(j,int) and 0<=j<mesh and j not in seen
        seen.add(j)
        lo=Q(-1,200)+Q(j,100*mesh)
        hi=lo+Q(1,100*mesh)
        assert list(map(Q,cell['height_interval']))==[lo,hi]
        s,t,xi=map(arb,cell['critical_boxes'])
        assert all(z>a(Q(1,4)) and z<a(Q(21,50)) for z in(s,t))
        assert xi>a(Q(1,6)-Q(1,100)) and xi<a(Q(1,6)+Q(1,100))
    assert seen==set(range(mesh))

    dependencies=['notes/research_three_vertex_large_cap_height_bound.md',
                  'notes/research_three_vertex_weighted_height_bound.md',
                  'notes/research_three_vertex_symmetric_height_bound.md',
                  'notes/research_three_vertex_global_wire_bound.md',
                  str(author_path.relative_to(ROOT)), str(review_path.relative_to(ROOT))]
    result={'status':'passed','precision_bits':args.precision,
            'strict_scalar_comparisons':len(checks),'exact_endpoint_identities':3,
            'inherited_critical_cells_checked':mesh,'exact_height_cover':True,
            'new_input_cap_radius':'1/25','unchanged_height_coefficient':13,
            'unchanged_distance_coefficient':'3/2',
            'low_sum_weighted_bound':str(low),'index_exit_reserve':str(a(loss-budget)),
            'scalar_checks':checks,
            'scope':'Analytic global exclusion for the larger capped weight, using the unchanged proved critical-height branch. No source lower bound or entrance packet.',
            'elapsed_seconds':time.monotonic()-start,
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependencies_sha256':{name:sha256((ROOT/name).read_bytes()).hexdigest() for name in dependencies}}
    (ROOT/args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:result[key] for key in ('status','strict_scalar_comparisons','exact_endpoint_identities','inherited_critical_cells_checked','low_sum_weighted_bound','index_exit_reserve','elapsed_seconds')},indent=2))


if __name__=='__main__':
    main()
