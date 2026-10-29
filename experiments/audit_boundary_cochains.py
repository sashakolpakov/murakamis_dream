#!/usr/bin/env python3
"""Independent local and global audits of the preferred-longitude cochain map.

Construction data: Kambampati, arXiv:2610.04103v1, Sections 4--6.
We derive the local auxiliary potentials and verify their identities.
The cusp-intersection formula has a separate 24-by-24 local audit.
Published analytic conclusions and ancillary verification code are not inputs.
"""

import argparse
import json
from itertools import permutations
from pathlib import Path

import sympy as sp

from audit_two_bridge import branchings,ordered_faces,parity
from certify_six_three import ab
from layered_two_bridge import layered_gluings,orientation_signs
from reduce_singular_faces import (cusp_fundamental_cycles,exact_reduction,
                                  kernel,peripheral_cycles)
from twist_topology_audit import (ANGLE_INDEX,arc_coordinates,cross,curve_chain,
                                  curve_holonomy,permutations_sign)


J0=sp.Matrix([[0,1,-1],[-1,0,1],[1,-1,0]])
ENDPOINT_FORM=sp.Matrix([[1,1,-1],[-1,-1,1],[1,-1,1]])
ARCS=[(0,v,i,j) for v in range(4)
      for i,j in permutations([u for u in range(4) if u!=v],2)]


def local_arc_holonomy(arc,epsilon):
    _,v,i,j=arc
    lone=next(k for k in range(4) if k not in [v,i,j])
    others=[k for k in range(4) if k!=v]
    sign=epsilon*(-1)**v*permutations_sign([others.index(k) for k in [i,j,lone]])
    row=sp.zeros(1,3)
    row[ANGLE_INDEX[tuple(sorted((v,lone)))]]=sign
    return row


def local_intersection(a,b,epsilon):
    if a[1]!=b[1]:
        return 0
    x,y=arc_coordinates(a,sp.Rational(1,3))
    u,v=arc_coordinates(b,sp.Rational(2,3))
    dx=[y[k]-x[k] for k in range(2)]
    du=[v[k]-u[k] for k in range(2)]
    determinant=cross(dx,du)
    if determinant==0:
        return 0
    offset=[u[k]-x[k] for k in range(2)]
    ta=cross(offset,du)/determinant
    tb=cross(offset,dx)/determinant
    if 0<ta<1 and 0<tb<1:
        return -epsilon*(-1)**a[1]*sp.sign(determinant)
    return 0


def local_intersection_certificate():
    count=0
    for epsilon in [-1,1]:
        for a in ARCS:
            for b in ARCS:
                boundary=0
                for face in range(4):
                    ra=int(face==a[3])-int(face==a[2])
                    rb=int(face==b[3])-int(face==b[2])
                    if not ra or not rb:
                        continue
                    vertices=[v for v in range(4) if v!=face]
                    i,j=vertices.index(a[1]),vertices.index(b[1])
                    boundary+=epsilon*(-1)**face*ra*rb*ENDPOINT_FORM[i,j]
                algebra=(local_arc_holonomy(a,epsilon)*(epsilon*J0)*local_arc_holonomy(b,epsilon).T)[0]
                assert algebra+2*local_intersection(a,b,epsilon)==boundary
                count+=1
    return {"ordered_arc_pair_identities":count,
            "endpoint_form":[list(map(int,row)) for row in ENDPOINT_FORM.tolist()],
            "global_pairing_convention":"h_gamma J_epsilon h_eta^T = -2 intersection(gamma,eta)"}


def local_cochain_certificate():
    a,b,p,w,t=sp.symbols("a b p w t")
    count=0
    for epsilon in [-1,1]:
        x=[a,a+b,b,b-epsilon*t]
        y=[p-epsilon*t,p,p+w,w]
        phi=[]
        for i in range(4):
            vertices=[j for j in range(4) if j!=i]
            phi.append(dict(zip(vertices,[0,x[i],x[i]-y[i]])))
        f=[sp.Integer(0)]
        for i in (1,2,3):
            j,m=[v for v in range(4) if v not in [0,i]]
            f.append(sp.expand(phi[0][j]+phi[0][m]-phi[i][j]-phi[i][m]))
        for i in range(4):
            for j in range(i+1,4):
                v,w0=[k for k in range(4) if k not in [i,j]]
                assert sp.expand(phi[i][v]+phi[i][w0]-phi[j][v]-phi[j][w0]-f[j]+f[i])==0
                count+=1
        s=x[0]+y[3]+sp.Rational(epsilon+1,2)*t
        theta=sp.Matrix([t,-s,s-t] if epsilon==1 else [t,s-t,-s])
        for arc in ARCS:
            _,v,i,j=arc
            hol=(local_arc_holonomy(arc,epsilon)*theta)[0]
            difference=f[j]+2*phi[j][v]-f[i]-2*phi[i][v]
            assert sp.expand(hol-difference)==0
            count+=1
    return {"potential_and_arc_identities":count,
            "auxiliary_face_potentials_derived_from_endpoint_sums":True}


def global_certificate(word):
    gluings=layered_gluings(word)
    orders=next(branchings(gluings,10000))
    faces=ordered_faces(gluings,orders)
    signs=[e*parity(p) for e,p in zip(orientation_signs(gluings),orders)]
    data=exact_reduction(faces,signs)
    n=len(faces)
    labels=data["face_labels"]
    X=[sp.Matrix(n,2*n,lambda t,k:int(faces[t][i]==labels[k])) for i in range(4)]
    D=X[0]-X[1]+X[2]
    Drev=X[3]-X[2]+X[1]
    R=X[2]-X[3]
    Rrev=X[1]-X[0]
    zero=sp.zeros(n,2*n)
    equations=D.row_join(zero).col_join(zero.row_join(Drev)).col_join(R.row_join(-Rrev))
    family=kernel(equations)
    assert family.cols==n
    xf,yf=family[:2*n,:],family[2*n:,:]
    t=sp.diag(*signs)*R*xf
    s=X[0]*xf+X[3]*yf+sp.diag(*[int(e==1) for e in signs])*t
    assert t.col_join(s).rank()==n
    assert data["S"]*data["Sinv"]*t==t
    assert data["S"].T*(s-data["Gambient"]*t)==sp.zeros(data["S"].cols,n)

    phi={}
    auxiliary={}
    for tetrahedron in range(n):
        for face in range(4):
            vertices=[v for v in range(4) if v!=face]
            row=labels.index(faces[tetrahedron][face])
            values=[sp.zeros(1,n),xf[row,:],xf[row,:]-yf[row,:]]
            for v,value in zip(vertices,values):
                phi[tetrahedron,face,v]=value
        auxiliary[tetrahedron,0]=sp.zeros(1,n)
        for face in (1,2,3):
            j,m=[v for v in range(4) if v not in [0,face]]
            auxiliary[tetrahedron,face]=(phi[tetrahedron,0,j]+phi[tetrahedron,0,m]
                                        -phi[tetrahedron,face,j]-phi[tetrahedron,face,m])
    cells=data["cells"]
    periods=sp.zeros(2*n,n)
    for row,label in enumerate(cells["labels"]):
        occurrences=[(j,i) for j in range(n) for i in range(4) if faces[j][i]==label]
        (j,i),(k,l)=occurrences
        periods[row,:]=auxiliary[j,i]-auxiliary[k,l]
    assert cells["boundary2"].T*periods==sp.zeros(n,n)
    physical=sp.zeros(3*n,n)
    for j,epsilon in enumerate(signs):
        physical[3*j,:]=t[j,:]
        physical[3*j+1,:]=-s[j,:] if epsilon==1 else s[j,:]-t[j,:]
        physical[3*j+2,:]=s[j,:]-t[j,:] if epsilon==1 else -s[j,:]
    cycles=cusp_fundamental_cycles(cells["adjacency"],n)
    for cycle in cycles:
        holonomy=curve_holonomy(faces,signs,cells["adjacency"],cycle)
        assert holonomy.T*physical==curve_chain(cells,cycle).T*periods
    peripheral=peripheral_cycles(faces,signs,data)
    ah,lh=peripheral["alpha_holonomy"],peripheral["longitude_holonomy"]
    assert lh.T*physical==sp.zeros(1,n)
    Am,Bm,_=ab(ah,signs)
    Al,Bl,_=ab(lh,signs)
    intersection=peripheral["intersection"]
    assert (Am*Bl.T-Bm*Al.T)[0]==-2*intersection
    edge_rows=data["Aed"].row_join(data["Bed"])
    pivots=list(edge_rows.T.rref()[1])
    assert len(pivots)==n-1
    A=data["Aed"][pivots,:].col_join(Al)
    B=data["Bed"][pivots,:].col_join(Bl)
    assert A.row_join(B).rank()==n and A*B.T==B*A.T
    assert A*t-B*s==sp.zeros(n,n)
    assert B.rank()==data["S"].cols
    assert data["S"]*data["Sinv"]*Bl.T==Bl.T
    assert data["S"].T*(Al.T-data["Gambient"]*Bl.T)==sp.zeros(data["S"].cols,1)
    return {"word":word,"tetrahedra":n,"pair_space_dimension":family.cols,
            "normal_cycles_checked":len(cycles),"dual_spine_cochain_closed":True,
            "every_cycle_period_matches_holonomy":True,"preferred_longitude_period_zero":True,
            "meridian_longitude_symplectic_pairing":int((Am*Bl.T-Bm*Al.T)[0]),
            "intersection":intersection,"completed_B_rank":B.rank(),
            "edge_B_rank":data["Bed"].rank(),"reduced_dimension":data["S"].cols,
            "nullity_doubling_exact":n-B.rank()==2*data["K"].cols,
            "preferred_longitude_constraint_and_form_exact":True}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("words",nargs="*",default=["RL","RLRL","RRLR","RRLLL","RLRLRLRL"])
    args=parser.parse_args()
    result={"source_construction":"Kambampati, arXiv:2610.04103v1, Sections 4--6",
            "scope":"Independent local identities and finite global diagnostics; uniform statements use the accompanying proof.",
            "local_cochains":local_cochain_certificate(),
            "local_intersection":local_intersection_certificate(),"records":[]}
    for word in args.words:
        record=global_certificate(word)
        result["records"].append(record)
        print(json.dumps(record),flush=True)
    Path(__file__).with_name("boundary_cochain_results.json").write_text(json.dumps(result,indent=2)+"\n")


if __name__=="__main__":
    main()
