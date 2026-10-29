#!/usr/bin/env python3
"""Exact Fourier reduction of the existing charged face contraction.

The reduction allows a singular stacked face matrix. Independent analytic
justification and the general Stokes identity are in the companion note.
The script supplies finite rank, normalization, and matrix certificates.
"""

import argparse
import json
from collections import deque
from functools import reduce
from itertools import product
from math import gcd,lcm
from pathlib import Path

import sympy as sp

from audit_two_bridge import branchings, ordered_faces, parity
from layered_two_bridge import flip_sequence, layered_gluings, orientation_signs
from twist_family_certificates import combinatorial_data
from twist_topology_audit import (ANGLE_INDEX, cusp_next, curve_chain,
                                curve_holonomy, dual_complex, intersection)


def right_inverse(M):
    rows, cols = M.shape
    if rows == 0:
        return sp.zeros(cols, 0)
    pivots = M.rref()[1]
    assert len(pivots) == rows
    result = sp.zeros(cols, rows)
    block = M[:, list(pivots)].inv()
    for i, p in enumerate(pivots):
        result[p, :] = block[i, :]
    assert M * result == sp.eye(rows)
    return result


def kernel(M):
    columns = M.nullspace()
    return sp.Matrix.hstack(*columns) if columns else sp.zeros(M.cols, 0)


def local_cocycle_certificate():
    a,b,c=sp.symbols("a b c")
    for epsilon in [-1,1]:
        potentials=[0,c,b+c,b+c+epsilon*a]
        momentum=[b,b+c,c,c]
        position=[a,-a,a+epsilon*b,-epsilon*b]
        for i in range(4):
            u,v,w=[j for j in range(4) if j!=i]
            assert sp.expand(momentum[i]-(potentials[v]-potentials[u]))==0
            assert sp.expand(position[i]-epsilon*(-1)**i*(potentials[w]-potentials[v]))==0
    return True


def exact_reduction(faces, signs):
    n = len(faces)
    labels = sorted({label for row in faces for label in row})
    assert len(labels) == 2*n
    X = [sp.Matrix(n,2*n,lambda t,k:int(faces[t][i]==labels[k])) for i in range(4)]
    D, R = X[0]-X[1]+X[2], X[2]-X[3]
    E = sp.diag(*signs)
    G, F = right_inverse(D), kernel(D)
    assert F.cols == n
    T, U = E*R*F, X[0]*F
    pivots = T.rref()[1]
    Z = sp.eye(n)[:,list(pivots)]
    K = kernel(T)
    P = T*Z
    C = K.T*U.T*P
    J, V = right_inverse(C), kernel(C)
    S = P*V
    lift = F*Z*V
    assert S.rank() == S.cols == n-2*K.cols
    assert D*lift == sp.zeros(n,S.cols) and E*R*lift == S
    assert K.T*U.T*S == sp.zeros(K.cols,S.cols)
    unsym = -S.T*U*Z*V
    Qred = (unsym+unsym.T)/2
    Sinv = (S.T*S).inv()*S.T if S.cols else sp.zeros(0,n)
    Qambient = Sinv.T*Qred*Sinv
    constant = abs(G.row_join(F).det()*Z.row_join(K).det()*J.row_join(V).det())
    assert constant != 0

    cells = dual_complex(faces)
    edge_index={edge:j for j,group in enumerate(cells["edge_groups"]) for edge in group}
    cocycle=sp.zeros(2*n,len(cells["edge_groups"]))
    for row,label in enumerate(labels):
        t=next(t for t in range(n) if label in faces[t])
        i=faces[t].index(label)
        u,v,w=[j for j in range(4) if j!=i]
        cocycle[row,edge_index[t,u,v]]+=1
        cocycle[row,edge_index[t,u,w]]-=1
        cocycle[row,edge_index[t,v,w]]+=1
    incidence = sp.zeros(len(cells["edge_groups"]),3*n)
    for row, group in enumerate(cells["edge_groups"]):
        for t,a,b in group:
            incidence[row,3*t+ANGLE_INDEX[a,b]] += 1
    gp, gpp = sp.zeros(incidence.rows,n), sp.zeros(incidence.rows,n)
    for j, sign in enumerate(signs):
        gp[:,j] = incidence[:,3*j+(2 if sign==1 else 1)]
        gpp[:,j] = incidence[:,3*j+(1 if sign==1 else 2)]
    Aed, Bed = incidence[:,0::3]-gp, gpp-gp
    Gambient = -2*Qambient+sp.diag(*[int(e==1) for e in signs])
    assert S*Sinv*Bed.T == Bed.T
    assert S.T*(Aed.T-Gambient*Bed.T) == sp.zeros(S.cols,incidence.rows)
    if K.cols == 0:
        proper = combinatorial_data(faces,signs)
        assert Qambient == proper["Qf"]
        assert constant/abs(S.det()) == 1/abs(proper["face_A"].det())
    return {"D":D,"R":R,"E":E,"F":F,"T":T,"U":U,"Z":Z,"K":K,
            "C":C,"J":J,"V":V,"S":S,"Sinv":Sinv,"lift":lift,
            "Qred":Qred,"Qambient":Qambient,"Gambient":Gambient,
            "normalization":constant,"incidence":incidence,"Aed":Aed,"Bed":Bed,
            "cells":cells,"face_labels":labels,"edge_cocycle_matrix":cocycle}


def angle_certificate(data, signs):
    n, S, Q = len(signs),data["S"],data["Qambient"]
    constraints = sp.Matrix(n,3*n,lambda i,j:int(j//3==i)).col_join(data["incidence"])
    tangent = kernel(constraints)
    A = sp.Matrix(n,3*n,lambda i,j:int(j==3*i))
    C = sp.diag(*signs)*sp.Matrix(n,3*n,lambda i,j:int(j==3*i+2))
    # d=pi-a and W=2 Q d-epsilon*c, so these are their variations.
    dvar = -A*tangent
    Wvar = (-2*S.T*Q*A-S.T*C)*tangent
    d_perp = sp.eye(n)-S*data["Sinv"]
    return {"balanced_angle_dimension":tangent.cols,
            "balanced_d_support_variation_rank":(d_perp*dvar).rank(),
            "restricted_W_variation_rank":Wvar.rank(),
            "edge_B_rank":data["Bed"].rank()}


def gaussian_normalization_certificate(data):
    """A weighted Gaussian checks the retained Fourier/Jacobian normalization."""
    n=data["T"].rows
    weights=sp.diag(*range(1,n+1))
    T,U,S=data["T"],data["U"],data["S"]
    full=T.T*weights*T+sp.I*(T.T*U+U.T*T)
    reduced=S.T*weights*S-2*sp.I*data["Qred"]
    G=right_inverse(data["D"])
    cD=abs(G.row_join(data["F"]).det())
    # Fourier pullback, rather than an unspecified square-root branch,
    # fixes the Gaussian phase in the analytical proof.
    assert sp.expand(cD**2*reduced.det()-data["normalization"]**2*full.det())==0
    return True


def cusp_fundamental_cycles(adjacency,n):
    nodes=[(t,v) for t in range(n) for v in range(4)]
    pending=deque([nodes[0]])
    reached={nodes[0]}
    tree=set()
    while pending:
        node=pending.popleft()
        for face in range(4):
            if face==node[1]:
                continue
            target,entered=cusp_next(adjacency,node,face)
            edge=frozenset(((node,face),(target,entered)))
            if target not in reached:
                reached.add(target)
                pending.append(target)
                tree.add(edge)
    assert len(reached)==4*n
    seen=set()
    cycles=[]
    for node in nodes:
        for face in range(4):
            if face==node[1]:
                continue
            target,entered=cusp_next(adjacency,node,face)
            edge=frozenset(((node,face),(target,entered)))
            if edge in tree or edge in seen:
                continue
            seen.add(edge)
            pending=deque([target])
            previous={target:None}
            while node not in previous:
                a=pending.popleft()
                for h in range(4):
                    if h==a[1]:
                        continue
                    b,k=cusp_next(adjacency,a,h)
                    if frozenset(((a,h),(b,k))) in tree and b not in previous:
                        previous[b]=(a,h)
                        pending.append(b)
            trail=[]
            a=node
            while a!=target:
                b,h=previous[a]
                trail.append((b,h))
                a=b
            cycles.append([(node,face)]+trail[::-1])
    return cycles


def peripheral_cycles(faces,signs,data):
    n=len(faces)
    cells=data["cells"]
    assert cells["smith"]==[1]*n
    eq=cells["boundary2"].T.col_join(sp.Matrix(len(cells["tree"]),2*n,
                                  lambda i,j:int(j==cells["tree"][i])))
    basis=eq.nullspace()
    assert len(basis)==1
    h=basis[0]*lcm(*[q.q for q in basis[0]])
    h/=reduce(gcd,[int(q) for q in h])
    cycles=cusp_fundamental_cycles(cells["adjacency"],n)
    links=[int((h.T*curve_chain(cells,cycle))[0]) for cycle in cycles]
    for i,alpha in enumerate(cycles):
        if links[i]!=1:
            continue
        for j,beta in enumerate(cycles):
            pairing=intersection(signs,cells["adjacency"],alpha,beta)
            if abs(pairing)!=1:
                continue
            alpha_chain=curve_chain(cells,alpha)
            longitude_chain=curve_chain(cells,beta)-links[j]*alpha_chain
            boundary,parameters=cells["boundary2"].gauss_jordan_solve(longitude_chain)
            assert parameters.rows==0 and all(q.q==1 for q in boundary)
            ah=curve_holonomy(faces,signs,cells["adjacency"],alpha)
            lh=curve_holonomy(faces,signs,cells["adjacency"],beta)-links[j]*ah
            return {"alpha":alpha,"beta":beta,"beta_linking":links[j],
                    "intersection":pairing,"homology_generator":h,
                    "longitude_boundary":boundary,"alpha_holonomy":ah,"longitude_holonomy":lh}
    raise AssertionError("No primitive peripheral pair among fundamental cycles")


def json_matrix(M):
    return [[str(q) for q in row] for row in M.tolist()]


def audit(word):
    gluings = layered_gluings(word)
    orders = next(branchings(gluings,10000))
    signs = [e*parity(p) for e,p in zip(orientation_signs(gluings),orders)]
    faces = ordered_faces(gluings,orders)
    data = exact_reduction(faces,signs)
    return {"word":word,"tetrahedra":len(faces),"orders":orders,"faces":faces,"signs":signs,
            "face_rank":data["D"].col_join(data["R"]).rank(),
            "kernel_dimension":data["K"].cols,"fourier_constraint_rank":data["C"].rank(),
            "reduced_dimension":data["S"].cols,
            "normalization":str(data["normalization"]),"S":json_matrix(data["S"]),
            "Qred":json_matrix(data["Qred"]),"Qambient":json_matrix(data["Qambient"]),
            "projected_edge_stokes_identity_exact":True,
            "local_cocycle_formula_exact":local_cocycle_certificate(),
            "ideal_edge_cocycle_kernel_dimension":len(data["edge_cocycle_matrix"].nullspace()),
            "weighted_gaussian_normalization_exact":gaussian_normalization_certificate(data),
            "balanced_angles":angle_certificate(data,signs)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("words",nargs="*",default=["RL","RLRL","RRLR","RRLLL","RLRLRLRL"])
    parser.add_argument("--scan-length",type=int)
    args = parser.parse_args()
    records = []
    words=args.words
    if args.scan_length is not None:
        words=['R'+''.join(tail) for length in range(2,args.scan_length+1)
               for tail in product('RL',repeat=length-1)
               if 'L' in tail and flip_sequence('R'+''.join(tail))[-1]!=0]
    for word in words:
        result = audit(word)
        records.append(result)
        print(json.dumps({k:result[k] for k in ("word","tetrahedra","kernel_dimension",
              "fourier_constraint_rank","reduced_dimension","normalization","balanced_angles")}),flush=True)
    destination="singular_word_scan_results.json" if args.scan_length is not None else "singular_face_results.json"
    Path(__file__).with_name(destination).write_text(json.dumps({
        "scope":"Exact certificates for Fourier reduction and its edge identity; finite words do not prove a uniform family theorem.",
        "records":records},indent=2)+"\n")


if __name__ == "__main__":
    main()
