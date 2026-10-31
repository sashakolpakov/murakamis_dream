#!/usr/bin/env python3
"""Exact original-flow leakage witness; no entropy-rate experiment."""
import argparse
import json
from fractions import Fraction as F
from pathlib import Path
import sys
import sympy as sp
sys.path.insert(0,str(Path(__file__).resolve().parent))
from audit_actual_original_marked_face_coefficient import morse_faces


def verify(data):
    word=[1,3,0,2,4,1,3,0,2,4,1,3,0,2,4,1,3]
    assert data['word']==word and data['protected']==[0,16]
    chart=morse_faces(3,word,0)
    assert chart['v']==16 and chart['circles']==[tuple(p) for p in data['ports']]
    ports=chart['circles'];zero={0,16};loads={f:F(0) for f in range(chart['faces'])}
    rows={int(e):[F(v,40) for v in q] for e,q in data['loads_over_40'].items()}
    assert set(rows)==set(range(len(ports)))
    for e,port in enumerate(ports):
        assert len(rows[e])==4 and min(rows[e])>=0 and sum(rows[e])==1
        for f,v in zip(port,rows[e]):loads[f]+=v
    assert all(v==(0 if f in zero else 1) for f,v in loads.items())
    assert rows[5]==[F(1,8),F(1,10),F(13,20),F(1,8)]
    assert rows[10]==[F(1,8),F(3,20),F(3,5),F(1,8)]
    assert ports[5]==(6,4,9,7) and ports[10]==(11,9,14,12)
    assert ports[5][2]==ports[10][1]==9
    mu1,nu1=rows[5][1],1-rows[5][2]
    mu2,nu2=rows[10][1],1-rows[10][2]
    ell=1-rows[5][2]-rows[10][1]
    assert ell==F(1,5)==nu1-mu2
    assert 0<mu1<mu2<nu1<nu2<F(1,2)
    # Equal outers have the literal symmetric coefficient tilt. Both
    # selected interval endpoint triangles are rational and nonnegative.
    for e in (5,10):
        mu,nu=rows[e][1],1-rows[e][2]
        alpha=[(F(1,2)-mu)/2,mu,(F(1,2)-mu)/2]
        beta=[(F(1,2)-nu)/2,nu,(F(1,2)-nu)/2]
        assert alpha[0]-beta[0]==rows[e][0]
        assert alpha[2]-beta[2]==rows[e][3]
    a,p,l,q=sp.symbols('a p l q');f=sp.Function('f')
    D=lambda u,v:f(u)+f(v)-f(u+v)
    difference=D(a,p+l)+D(a+p,l+q)-D(a,p+l+q)-D(a+p,l)
    expected=f(p+l)+f(l+q)-f(l)-f(p+l+q)
    assert sp.expand(difference-expected)==0
    return {'status':'PASS','counts':{'literal_ports':len(ports),'ordinary_targets':len(loads)-2,
        'protected_zero_targets':2,'exact_quartet_coordinates':4*len(ports),
        'selected_one_sided_intervals':2,'symbolic_uncrossing_identities':1},
        'exact_overlap':'1/5','scope':'Exact original shared-flow witness and symbolic middle-only uncrossing identity. Other rows retain full source support; no score maximum, volume bound, or quantum counterexample is inferred.'}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--certificate',type=Path,default=Path(__file__).with_name('research_joint_middle_interval_leakage_certificate.json'))
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('research_joint_middle_interval_leakage_results.json'))
    args=parser.parse_args()
    result=verify(json.loads(args.certificate.read_text()))
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
