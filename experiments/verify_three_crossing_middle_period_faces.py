#!/usr/bin/env python3
"""Exact 39 new current bounds at boundary angle u=3/5.

The boundary correction is constant along each tested face/edge.
Only the unchanged x,z tangential derivatives are used. The completed
144-case verifier and result are read-only dependencies.
"""

import argparse
from concurrent.futures import ProcessPoolExecutor
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

from verify_next_crossing_complex_phase import C,R,PI
from verify_three_crossing_current_faces import J,phase_gradient


ROOT=Path(__file__).resolve().parents[1]
Y_CUT=F(13,40)
P_CUT=F(1,400)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def vertices(face):
    if face=='y':
        return [(x,Y_CUT,z) for x in [F(1,10),F(1,2)]
                for z in [F(1,100),x-P_CUT]]
    assert face=='yp'
    return [(x,Y_CUT,x-P_CUT) for x in [F(1,10),F(1,2)]]


def check_case(task):
    item,height_pairs,shift_pair=task
    face=item['face'];signs=tuple(item['signs'])
    point=tuple(map(F,item['point']))
    heights=[R(F(a),F(b)) for a,b in height_pairs]
    shift=R(F(shift_pair[0]),F(shift_pair[1]))
    assert F(1,10)<=point[0]<=F(1,2) and point[1]==Y_CUT
    assert F(1,100)<=point[2]<=point[0]-P_CUT
    if face=='yp':assert point[0]-point[2]==P_CUT
    xyz=[C(point[j],signs[j]*heights[j]) for j in range(3)]
    original,gradient=phase_gradient(*xyz)
    phase_real=original.re+shift
    face_vertices=vertices(face)
    assert all(v[1]==point[1] for v in face_vertices)
    # The correction depends on y only. No uncorrected y derivative
    # is used in this face/edge tangent comparison.
    upper=max((phase_real+sum((gradient[j].re*(v[j]-point[j])
                 for j in [0,2]),R(0))).hi for v in face_vertices)
    magnitudes=[-heights[0],heights[1],heights[2]]
    penalty=2*PI*sum((magnitudes[j] for j in range(3) if signs[j]<0),R(0))
    penalized=upper-penalty.lo
    assert penalized<F(3,2),(face,signs,penalized)
    return dict(item,original_phase=original.record(),
                real_boundary_shift=shift.record(),corrected_real_phase=phase_real.record(),
                unchanged_tangential_gradient={name:gradient[j].re.record()
                                              for name,j in [('x',0),('z',2)]},
                vertices=[[str(v) for v in vertex] for vertex in face_vertices],
                tangent_upper=str(upper),penalty=penalty.record(),
                penalized_face_upper=str(penalized))


def run(workers):
    fixture=ROOT/'repro/fixtures/research-three-crossing-middle-period-face-points.json'
    data=json.loads(fixture.read_text());cases=data['cases']
    assert F(data['boundary_angle'])==F(3,5) and F(data['new_y_upper'])==Y_CUT
    signs=list(itertools.product([-1,0,1],repeat=3))
    expected={('y',s) for s in signs if s[0]!=0 and s[2]!=0}
    expected|={('yp',s) for s in signs}
    actual=[(row['face'],tuple(row['signs'])) for row in cases]
    assert len(cases)==len(set(actual))==len(expected)==39 and set(actual)==expected

    original_certificate=ROOT/'repro/results/research-three-crossing-current-faces.json'
    original=json.loads(original_certificate.read_text())
    source=ROOT/'experiments/verify_three_crossing_current_faces.py'
    assert original['status']=='passed' and original['case_count']==144
    assert original['script_sha256']==sha(source)
    dependencies={str(source.relative_to(ROOT)):sha(source)}
    for name,digest in original['dependency_sha256'].items():
        assert sha(ROOT/name)==digest
        dependencies[name]=digest
    certificate=ROOT/original['height_certificate']
    assert sha(certificate)==original['height_certificate_sha256']
    root=json.loads(certificate.read_text())
    inner=root['root_certificate']
    heights=[root['remaining_color_x']['imaginary'],root['remaining_color_y']['imaginary'],
             inner['certificates']['selected_saddle']['imaginary']]
    assert -F(3,40)<F(heights[0][0])<F(heights[0][1])<0
    assert 0<F(heights[1][0])<F(heights[1][1])<F(13,200)
    assert 0<F(heights[2][0])<F(heights[2][1])<F(19,250)

    angle_shift=R(F(3,10))/PI
    shifts={}
    for sign in [0,1]:
        hy=sign*R(F(heights[1][0]),F(heights[1][1]))
        y=C(Y_CUT,hy);center=F(1,2)-y
        # J(1/2+a)+J(1/2-a)=0 and J(1/2)=0 on the
        # original strip; hence this is exactly b(y,3/5)-b(y,0).
        delta=2*J(center)-J(center+angle_shift)-J(center-angle_shift)
        assert delta.re.hi<0
        shifts[sign]=delta
    tasks=[]
    for case in cases:
        # Schwarz reflection gives equal real shifts at +/- H_y.
        shift=shifts[abs(case['signs'][1])].re.record()
        tasks.append((case,heights,shift))
    if workers==1:
        reports=list(map(check_case,tasks))
    else:
        with ProcessPoolExecutor(max_workers=workers) as pool:
            reports=list(pool.map(check_case,tasks))
    return {
        'status':'passed','case_count':len(reports),'boundary_angle':'3/5',
        'new_y_upper':str(Y_CUT),'diagonal_cut':str(P_CUT),
        'method':'Rational outward arithmetic; constant boundary shift plus globally concave tangential planes.',
        'boundary_shift_formula':'2J(1/2-y)-J(1/2-y+3/(10pi))-J(1/2-y-3/(10pi))',
        'boundary_shifts':{str(sign):value.record() for sign,value in shifts.items()},
        'common_penalized_upper_bound':'3/2',
        'maximum_certified_upper_bound':str(max(F(r['penalized_face_upper']) for r in reports)),
        'cases':reports,'script_sha256':sha(Path(__file__).resolve()),
        'dependency_sha256':dependencies,'fixture':str(fixture.relative_to(ROOT)),
        'fixture_sha256':sha(fixture),
        'previous_current_certificate':str(original_certificate.relative_to(ROOT)),
        'previous_current_certificate_sha256':sha(original_certificate),
        'height_certificate':str(certificate.relative_to(ROOT)),
        'height_certificate_sha256':sha(certificate),
        'scope':'12 new pure-y face states and27 y/diagonal edge states at u=3/5; monotonic continuation and current support are separate proved inputs.',
    }


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workers',type=int,choices=[1,2,3],default=2)
    parser.add_argument('--output',type=Path,
                        default=ROOT/'repro/results/research-three-crossing-middle-period-faces.json')
    args=parser.parse_args();result=run(args.workers)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('All39 new middle-period current certificates passed.')
    print(f'Saved {args.output}')
