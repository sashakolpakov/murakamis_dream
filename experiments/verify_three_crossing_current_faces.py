#!/usr/bin/env python3
"""Outward certificates for the 144 cellwise boundary-height cases.

Every case is bounded on its whole face by a concave tangent plane.
The input fixture supplies only arbitrary rational tangent points;
all rate comparisons are reevaluated with rational outward arithmetic.
"""

import argparse
from concurrent.futures import ProcessPoolExecutor
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

from verify_next_crossing_complex_phase import C,R,PI,IM,exponential
from verify_three_crossing_formal_horizontals import logarithm as raw_logarithm,dilogarithm


ROOT=Path(__file__).resolve().parents[1]
LOG_TWO=raw_logarithm(C(2))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def logarithm(z):
    """Principal right-half log, with exact radial/angular normalization."""
    assert z.re.lo>0
    correction=C(0)
    if z.im.lo>=0:
        z=(1-IM)*z
        correction=-LOG_TWO/2+IM*C(PI/4)
    elif z.im.hi<=0:
        z=(1+IM)*z
        correction=-LOG_TWO/2-IM*C(PI/4)
    radius=z.radius_upper()
    scale=F(1);power=0
    while radius>2:
        radius/=2;scale*=2;power+=1
    while radius<1:
        radius*=2;scale/=2;power-=1
    normalized=z/scale
    assert normalized.re.lo>0
    assert ((normalized-1)/(normalized+1)).radius_upper()<F(3,4)
    return raw_logarithm(normalized)+power*LOG_TWO+correction


def principal_log(z):
    if z.re.lo>0:
        return logarithm(z)
    if z.im.lo>0:
        return logarithm(-IM*z)+IM*C(PI/2)
    assert z.im.hi<0
    return logarithm(IM*z)-IM*C(PI/2)


def li2(z,depth=0):
    assert depth<4
    if z.radius_upper()<F(9,10):
        return dilogarithm(z,terms=150)
    inverse=z.inverse()
    if inverse.radius_upper()<F(9,10):
        assert z.re.hi<0 or z.im.lo>0 or z.im.hi<0
        return -dilogarithm(inverse,terms=150)-C(PI.square()/6)-principal_log(-z)**2/2
    reflected=1-z
    if reflected.radius_upper()<F(9,10):
        return C(PI.square()/6)-principal_log(z)*principal_log(reflected)-dilogarithm(reflected,terms=150)
    transformed=z/(z-1)
    if transformed.radius_upper()<F(9,10):
        return -dilogarithm(transformed,terms=150)-principal_log(1-z)**2/2
    # In this remaining lens the ray and its square avoid all cuts.
    assert z.re.lo>0 and (z.im.lo>0 or z.im.hi<0)
    return li2(z*z,depth+1)/2-li2(-z,depth+1)


def J(t):
    assert 0<t.re.lo<=t.re.hi<1
    z=exponential(2*IM*C(PI)*t)
    return IM*C(PI)*(t-t*t)/2+IM*(li2(z)-C(PI.square()/6))/(2*C(PI))


def log_sine(t):
    z=exponential(IM*C(PI)*t)
    return logarithm((z-z.inverse())/IM)


def phase_gradient(x,y,z):
    value=(J(x+y)-J(x)-J(x-z)-3*J(z)-6*J(y)+J(2*y)
           +IM*C(PI)*((x-y)**2-x+y+2*x*z+2*z*z)/2)
    lx,ly,lz=log_sine(x),log_sine(y),log_sine(z)
    lp,ls,l2y=log_sine(x-z),log_sine(x+y),log_sine(2*y)
    gradient=[ls-lx-lp+IM*C(PI)*(x-y-F(1,2)+z),
              ls-6*ly+2*l2y+IM*C(PI)*(y-x+F(1,2)),
              lp-3*lz+IM*C(PI)*(x+2*z)]
    return value,gradient


def vertices(face,value):
    if face=='x':
        return [(value,y,z) for y in [F(1,10),F(2,5)]
                for z in [F(1,100),value-F(1,400)]]
    if face=='y':
        return [(x,value,z) for x in [F(1,10),F(1,2)]
                for z in [F(1,100),x-F(1,400)]]
    if face=='z':
        return [(x,y,value) for x in [F(1,10),F(1,2)]
                for y in [F(1,10),F(2,5)]]
    assert face=='p'
    return [(x,y,x-value) for x in [F(1,10),F(1,2)]
            for y in [F(1,10),F(2,5)]]


def check_case(task):
    item,height_pairs=task
    face,value=item['face'],F(item['value'])
    signs=tuple(item['signs']);point=tuple(map(F,item['point']))
    heights=[R(F(a),F(b)) for a,b in height_pairs]
    assert F(1,10)<=point[0]<=F(1,2)
    assert F(1,10)<=point[1]<=F(2,5)
    assert F(1,100)<=point[2]<=point[0]-F(1,400)
    assert (point[{'x':0,'y':1,'z':2}[face]]==value if face!='p'
            else point[0]-point[2]==value)
    xyz=[C(point[j],signs[j]*heights[j]) for j in range(3)]
    phase,gradient=phase_gradient(*xyz)
    tangent=max((phase.re+sum((gradient[j].re*(vertex[j]-point[j])
                for j in range(3)),R(0))).hi for vertex in vertices(face,value))
    magnitudes=[-heights[0],heights[1],heights[2]]
    penalty=2*PI*sum((magnitudes[j] for j in range(3) if signs[j]<0),R(0))
    upper=tangent-penalty.lo
    assert upper<F(151,100),(face,value,signs,upper)
    return dict(item,phase=phase.record(),gradient=[g.re.record() for g in gradient],
                tangent_upper=str(tangent),penalty=penalty.record(),
                penalized_face_upper=str(upper))


def run(workers):
    fixture=ROOT/'repro/fixtures/research-three-crossing-current-face-points.json'
    cases=json.loads(fixture.read_text())['cases']
    signs=list(itertools.product([0,1,-1],repeat=3))
    expected={(f,str(v),s) for f,v in [('x',F(1,10)),('y',F(1,10)),
                 ('y',F(2,5)),('z',F(1,100))] for s in signs}
    expected|={('x','1/2',s) for s in signs if s[2]!=0}
    expected|={('p','1/400',s) for s in signs if s[1]!=0}
    actual=[(r['face'],r['value'],tuple(r['signs'])) for r in cases]
    assert len(cases)==len(set(actual))==len(expected)==144 and set(actual)==expected
    certificate=ROOT/'repro/results/research-three-crossing-closing-action.json'
    root=json.loads(certificate.read_text())
    source=ROOT/'experiments/verify_three_crossing_closing_action.py'
    assert root['status']=='passed' and root['script_sha256']==sha(source)
    deps={str(source.relative_to(ROOT)):sha(source)}
    for name,digest in root['dependency_sha256'].items():
        assert sha(ROOT/name)==digest
        deps[name]=digest
    for name in ['verify_three_crossing_formal_horizontals.py',
                 'verify_next_crossing_complex_phase.py']:
        path=ROOT/'experiments'/name;deps[str(path.relative_to(ROOT))]=sha(path)
    inner=root['root_certificate']
    assert inner['script_sha256']==deps['experiments/verify_next_crossing_complex_phase.py']
    heights=[root['remaining_color_x']['imaginary'],root['remaining_color_y']['imaginary'],
             inner['certificates']['selected_saddle']['imaginary']]
    assert -F(3,40)<F(heights[0][0])<F(heights[0][1])<0
    assert 0<F(heights[1][0])<F(heights[1][1])<F(13,200)
    assert 0<F(heights[2][0])<F(heights[2][1])<F(19,250)
    tasks=[(case,heights) for case in cases]
    if workers==1:
        reports=list(map(check_case,tasks))
    else:
        with ProcessPoolExecutor(max_workers=workers) as pool:
            reports=list(pool.map(check_case,tasks))
    return {
        'status':'passed','case_count':len(reports),
        'method':'Exact rational outward arithmetic and global concave tangent planes.',
        'common_penalized_upper_bound':'151/100',
        'maximum_certified_upper_bound':str(max(F(r['penalized_face_upper']) for r in reports)),
        'cases':reports,'script_sha256':sha(Path(__file__).resolve()),
        'dependency_sha256':deps,'fixture':str(fixture.relative_to(ROOT)),
        'fixture_sha256':sha(fixture),'height_certificate':str(certificate.relative_to(ROOT)),
        'height_certificate_sha256':sha(certificate),
        'scope':'Complete six-family boundary-height list; support identification and convexity are proved separately.',
    }


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workers',type=int,choices=[1,2,3],default=2)
    parser.add_argument('--output',type=Path,
                        default=ROOT/'repro/results/research-three-crossing-current-faces.json')
    args=parser.parse_args();result=run(args.workers)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('All144 cellwise boundary-height certificates passed.')
    print(f'Saved {args.output}')
