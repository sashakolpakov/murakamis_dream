#!/usr/bin/env python3
"""Integral preferred-longitude saturation, with arbitrary face permutations.

The meridian constructed in the cellular tests is a homological meridian;
its framing is not asserted to equal a diagram's marked meridian. The
uniform theorem applies to any supplied marked meridian. No source-state
comparison or volume asymptotic is tested here.
"""

import argparse
from collections import deque
from itertools import permutations, product
import json
from math import gcd, lcm
from pathlib import Path

import numpy as np
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form

from audit_actual_peripheral_fusion import inverse_mod, matrix_power
from audit_cyclic_steinberg_lattice import rank
from audit_finite_sum_annihilator import field
from audit_pointed_tetrahedron_gluing import EDGES, incidence, relabel, weyl
from audit_regular_holonomy_braiding import mm
from twist_topology_audit import (ANGLE_INDEX, curve_arcs, curve_chain,
                                 curve_holonomy, cusp_next)

VECTORS=[sp.Matrix([1,0]),sp.Matrix([0,1]),sp.Matrix([-1,-1])]
J=sp.Matrix([[0,1],[-1,0]])
J3=sp.Matrix([[0,1,-1],[-1,0,1],[1,-1,0]])


def local_delta(vertex, flow):
    sides=[f for f in range(4) if f!=vertex]
    return (-1)**vertex*(flow[sides[1]]*VECTORS[ANGLE_INDEX[tuple(sorted((vertex,sides[2])))]]
                        -flow[sides[2]]*VECTORS[ANGLE_INDEX[tuple(sorted((vertex,sides[1])))]] )


def local_certificate():
    left={};right={}
    for vertex in range(4):
        sides=[f for f in range(4) if f!=vertex]
        a,b=sp.symbols(f'a{vertex} b{vertex}');c,d=sp.symbols(f'c{vertex} d{vertex}')
        left[vertex]=dict(zip(sides,[-a-b,a,b]))
        right[vertex]=dict(zip(sides,[-c-d,c,d]))
    dl=sum((local_delta(v,left[v]) for v in range(4)),sp.zeros(2,1))
    dr=sum((local_delta(v,right[v]) for v in range(4)),sp.zeros(2,1))
    for epsilon in (-1,1):
        twice_intersection=0;faces=0
        for v in range(4):
            f,g,_=[f for f in range(4) if f!=v]
            twice_intersection-=epsilon*(-1)**v*(left[v][f]*right[v][g]-left[v][g]*right[v][f])
        for f in range(4):
            vertices=[v for v in range(4) if v!=f]
            rf=sp.Matrix([left[v][f] for v in vertices]);sf=sp.Matrix([right[v][f] for v in vertices])
            faces+=epsilon*(-1)**f*(rf.T*J3*sf)[0]
        assert sp.expand((dl.T*(epsilon*J)*dr)[0]+twice_intersection-faces)==0
    for p in permutations(range(3)):
        P=sp.zeros(3)
        for i,j in enumerate(p):P[j,i]=1
        assert P.T*J3*P==P.det()*J3
    checks=0
    for u,w in product(range(2),repeat=2):
        q=[-w,u,w-u];b=[0,*q];v=sp.Matrix([u,w])
        for a,c in EDGES:
            f,g=[f for f in range(4) if f not in (a,c)]
            assert (b[f]+b[g]-q[ANGLE_INDEX[a,c]])%2==0
        for vertex in range(4):
            sides=[f for f in range(4) if f!=vertex]
            for entered,exited in permutations(sides,2):
                flow={f:int(f==exited)-int(f==entered) for f in sides}
                delta=local_delta(vertex,flow)
                for epsilon in (-1,1):
                    assert int((v.T*(epsilon*J)*delta)[0]-b[entered]-b[exited])%2==0
                    checks+=1
    return {'symbolic_flow_face_identities':2,'arbitrary_face_permutations':6,
            'mod_two_arc_potential_checks':checks}


def binary_rref(matrix):
    A=[[int(x)%2 for x in row] for row in matrix.tolist()];pivots=[];r=0
    for c in range(matrix.cols):
        pivot=next((i for i in range(r,len(A)) if A[i][c]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        for i in range(len(A)):
            if i!=r and A[i][c]:A[i]=[a^b for a,b in zip(A[i],A[r])]
        pivots.append(c);r+=1
        if r==len(A):break
    return A,pivots


def binary_kernel(matrix):
    A,pivots=binary_rref(matrix);columns=[]
    for free in range(matrix.cols):
        if free in pivots:continue
        v=[0]*matrix.cols;v[free]=1
        for row,pivot in enumerate(pivots):v[pivot]=A[row][free]
        columns.append(sp.Matrix(v))
    return columns


def binary_solve(matrix,target):
    A,pivots=binary_rref(matrix.row_join(target))
    assert matrix.cols not in pivots and len(pivots)==matrix.cols
    answer=sp.zeros(matrix.cols,1)
    for row,pivot in enumerate(pivots):answer[pivot]=A[row][-1]
    assert all(int(x)%2==0 for x in matrix*answer-target)
    return answer


def dual_cells(tri):
    n=tri.size();adj={};labels=[];tree=[];components=list(range(n))
    def root(i):
        while components[i]!=i:i=components[i]
        return i
    for t,tet in enumerate(tri.tetrahedra()):
        for f in range(4):
            u=tet.adjacentTetrahedron(f).index();p=tet.adjacentGluing(f);g=p[f]
            if (t,f)>(u,g):continue
            k=len(labels);labels.append(k);perm={a:p[a] for a in range(4)}
            adj[t,f]=(u,g,perm,k,1);adj[u,g]=(t,f,{b:a for a,b in perm.items()},k,-1)
            if root(t)!=root(u):components[root(t)]=root(u);tree.append(k)
    d1=sp.zeros(n,len(labels))
    for (t,f),(u,g,p,k,s) in adj.items():
        if s==1:d1[t,k]-=1;d1[u,k]+=1
    groups=[[] for _ in range(tri.countEdges())]
    for t,tet in enumerate(tri.tetrahedra()):
        for local,(a,b) in enumerate(EDGES):groups[tet.edge(local).index()].append((t,a,b))
    d2=sp.zeros(len(labels),len(groups))
    for column,group in enumerate(groups):
        t,a,b=min(group);f=min(v for v in range(4) if v not in (a,b))
        initial=(t,a,b,f);state=initial;visited=set()
        while True:
            assert state not in visited;visited.add(state)
            t,a,b,f=state;u,g,p,k,s=adj[t,f];d2[k,column]+=s
            a,b=sorted((p[a],p[b]));f=next(v for v in range(4) if v not in (a,b,g))
            state=(u,a,b,f)
            if state==initial:break
        assert len(visited)==len(group)
    assert d1*d2==sp.zeros(d1.rows,d2.cols)
    return {'labels':labels,'index':{k:k for k in labels},'adjacency':adj,
            'boundary1':d1,'boundary2':d2,'tree':tree}


def torus_cycles(tri,cells):
    adj=cells['adjacency'];cusps=[v.index() for v in tri.vertices() if str(v.linkType())=='Link.Torus']
    assert len(cusps)==1
    nodes=[(t,v) for t,tet in enumerate(tri.tetrahedra()) for v in range(4)
           if tet.vertex(v).index()==cusps[0]]
    reached={nodes[0]};pending=deque([nodes[0]]);tree=set()
    while pending:
        node=pending.popleft()
        for f in range(4):
            if f==node[1]:continue
            target,g=cusp_next(adj,node,f);edge=frozenset(((node,f),(target,g)))
            if target not in reached:reached.add(target);pending.append(target);tree.add(edge)
    assert reached==set(nodes)
    seen=set();cycles=[]
    for node in nodes:
        for f in range(4):
            if f==node[1]:continue
            target,g=cusp_next(adj,node,f);edge=frozenset(((node,f),(target,g)))
            if edge in seen or edge in tree:continue
            seen.add(edge);previous={target:None};pending=deque([target])
            while node not in previous:
                a=pending.popleft()
                for h in range(4):
                    if h==a[1]:continue
                    b,k=cusp_next(adj,a,h)
                    if frozenset(((a,h),(b,k))) in tree and b not in previous:
                        previous[b]=(a,h);pending.append(b)
            trail=[];a=node
            while a!=target:
                b,h=previous[a];trail.append((b,h));a=b
            cycles.append([(node,f)]+trail[::-1])
    return cycles


def bezout(values):
    coefficients=sp.zeros(len(values),1);g=0
    for i,x in enumerate(values):
        a,b,h=sp.gcdex(g,int(x));coefficients*=a;coefficients[i]+=b;g=int(h)
    assert g==1 and sum(int(x)*int(y) for x,y in zip(values,coefficients))==1
    return coefficients


def smith_entries(matrix):
    S=smith_normal_form(matrix,domain=sp.ZZ)
    return [abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]]


def cellular_case(tri,name,change):
    edges,signs,record=incidence(tri);n=len(signs);E=sp.Matrix(edges)
    Omega=sp.diag(*[epsilon*J for epsilon in signs]);cells=dual_cells(tri)
    cycles=torus_cycles(tri,cells);k=len(cycles);flows={}
    D=sp.zeros(2*n,k);C=sp.zeros(len(cells['labels']),k)
    for j,cycle in enumerate(cycles):
        C[:,j]=curve_chain(cells,cycle)
        for t,v,entered,exited in curve_arcs(cells['adjacency'],cycle):
            for f,s in ((entered,-1),(exited,1)):
                flows.setdefault((t,v,f),sp.zeros(1,k))[j]+=s
        old=curve_holonomy([None]*n,signs,cells['adjacency'],cycle)
        for t in range(n):D[2*t:2*t+2,j]=signs[t]*sp.Matrix([old[3*t]-old[3*t+2],old[3*t+1]-old[3*t+2]])
    Itwice=sp.zeros(k)
    for t in range(n):
        local=sp.zeros(2,k)
        for v in range(4):
            f,g,h=[f for f in range(4) if f!=v]
            rf=flows.get((t,v,f),sp.zeros(1,k));rg=flows.get((t,v,g),sp.zeros(1,k))
            rh=flows.get((t,v,h),sp.zeros(1,k))
            assert rf+rg+rh==sp.zeros(1,k)
            Itwice-=signs[t]*(-1)**v*(rf.T*rg-rg.T*rf)
            local+=(-1)**v*(VECTORS[ANGLE_INDEX[tuple(sorted((v,h)))]]*rg
                                    -VECTORS[ANGLE_INDEX[tuple(sorted((v,g)))]]*rh)
        assert local==D[2*t:2*t+2,:]
    assert all(int(x)%2==0 for x in Itwice)
    I=Itwice/2
    assert E*Omega*D==sp.zeros(E.rows,k) and D.T*Omega*D==-2*I
    assert I.rank()==2
    balanced=binary_kernel(E*Omega)
    for v in balanced:
        potentials=[]
        for t in range(n):
            u,w=map(int,v[2*t:2*t+2,0]);potentials.append([0,-w,u,w-u])
        a=sp.zeros(len(cells['labels']),1)
        for (t,f),(u,g,p,label,s) in cells['adjacency'].items():
            if s==1:a[label]=(potentials[t][f]+potentials[u][g])%2
        assert all(int(x)%2==0 for x in cells['boundary2'].T*a)
        assert all(int(x)%2==0 for x in v.T*Omega*D-a.T*C)
    treeeq=sp.Matrix(len(cells['tree']),C.rows,lambda i,j:int(j==cells['tree'][i]))
    homology=cells['boundary2'].T.col_join(treeeq).nullspace();assert len(homology)==1
    h=homology[0]*lcm(*[int(x.q) for x in homology[0]])
    divisor=0
    for x in h:divisor=gcd(divisor,int(x))
    h/=divisor;p=C.T*h;alpha=bezout(list(p));beta=bezout(list(alpha.T*I))
    longitude=beta-int((p.T*beta)[0])*alpha
    assert (p.T*alpha)[0]==1 and (p.T*longitude)[0]==0 and (alpha.T*I*longitude)[0]==1
    bounds=hermite_normal_form(cells['boundary2'])
    coeff=bounds.gauss_jordan_solve(C*longitude)[0]
    assert all(x.q==1 for x in coeff)
    mu=D*alpha;lam=D*longitude;basis=hermite_normal_form(E.T).T
    correction_coeff=binary_solve(basis.T,lam);correction=basis.T*correction_coeff
    half=(lam-correction)/2
    assert all(x.q==1 for x in half)
    assert E*Omega*half==sp.zeros(E.rows,1) and (mu.T*Omega*half)[0]==-1
    fullsmith=smith_entries(basis.col_join(mu.T).col_join(half.T))
    oldsmith=smith_entries(basis.col_join(mu.T).col_join(lam.T))
    assert set(fullsmith)=={1} and oldsmith.count(2)==1 and set(oldsmith)<={1,2}
    result={'name':name,'relabeling':change,**record,'cusp_graph_cycles':k,
            'unbranched_flow_intersection_identity_exact':True,
            'mod_two_balanced_basis_cochains_checked':len(balanced),
            'preferred_longitude_bounds_integrally':True,'half_longitude_integral':True,
            'meridian_pairing_with_half_longitude':-1,
            'saturated_basis_Smith':fullsmith,'unhalved_basis_Smith':oldsmith,
            'audit_meridian_is_homological_and_framing_unspecified':True}
    return result,{'basis':basis,'signs':signs,'mu':mu,'lambda':lam,
                   'half':half,'correction_coeff':correction_coeff}


def quantum_case(level,data):
    prime,generator,q=field(level);Q=q*q%prime;basis=data['basis'];signs=data['signs']
    size=level**len(signs);Id=np.eye(size,dtype=np.int64);P=Id.copy();exponent=0
    for i in range(basis.rows):
        U=weyl(list(basis.row(i)),signs,level,prime,q);character=pow(Q,i+1,prime)
        exponent+=int(data['correction_coeff'][i])*(i+1)
        term=Id.copy();Pi=np.zeros_like(Id)
        for j in range(level):
            Pi=(Pi+term*pow(character,-j,prime))%prime;term=mm(prime,term,U)
        P=mm(prime,P,Pi*pow(level,-1,prime)%prime)
    assert rank(P,prime)==level
    eta=pow(q,exponent,prime)
    Y=weyl(list(data['mu']),signs,level,prime,q)
    T=weyl(list(data['half']),signs,level,prime,q)*eta%prime
    Lambda=weyl(list(data['lambda']),signs,level,prime,q)
    assert np.array_equal(mm(prime,T,T,P),mm(prime,Lambda,P))
    assert np.array_equal(mm(prime,T,Y),mm(prime,Y,T)*Q%prime)
    assert np.array_equal(mm(prime,matrix_power(T,level,prime),P),P*pow(eta,level,prime)%prime)
    if level%2==0:
        Z=matrix_power(Y,level//2,prime)
        plus=mm(prime,P,(Id+Z)*pow(2,-1,prime)%prime)
        minus=mm(prime,P,(Id-Z)*pow(2,-1,prime)%prime)
        assert rank(plus,prime)==rank(minus,prime)==level//2
        assert np.array_equal(mm(prime,T,plus),mm(prime,minus,T))
        assert np.array_equal(matrix_power(-T%prime,level,prime),matrix_power(T,level,prime))
    Ygeneric=Y*generator%prime
    gauge=mm(prime,(Q*Ygeneric-Id)%prime,inverse_mod((Ygeneric-Id)%prime,prime))
    gauge=gauge*(-pow(q,-1,prime))%prime
    full=mm(prime,gauge,T);delta=(-1)**(level-1)%prime
    assert np.array_equal(matrix_power(full,level,prime),matrix_power(T,level,prime)*delta%prime)
    return {'level':level,'prime':prime,'edge_character_lift_exponent':exponent,
            'half_longitude_square_and_Q_commutator_exact':True,
            'even_sectors_exchanged_by_half_longitude':level%2==0,
            'even_central_sign_unchanged_by_mu_two_choice':level%2==0,
            'generic_center_full_ADO_gauge_norm':int(delta),
            'geometric_lift_not_asserted_to_equal_actual_ADO_state':True}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--regina',action='store_true');args=parser.parse_args()
    local=local_certificate();records=[];quantum=[]
    print('symbolic local intersection and parity identities: passed',flush=True)
    if args.regina:
        import regina
        from audit_crossing_fundamental_cycle import shadow_pairing
        cases=[('figure_eight',regina.Example3.figureEight()),('trefoil',regina.Example3.trefoil())]
        for name,strands,word in [('unknot_shadow',2,[(0,1)]),('trefoil_shadow',2,[(0,1)]*3),
                                  ('figure_eight_shadow',3,[(0,1),(1,-1)]*2),
                                  ('weaving_3_4_shadow',3,[(0,1),(1,-1)]*4)]:
            pairs,_=shadow_pairing(strands,word);tri=regina.Triangulation3()
            tets=[tri.newTetrahedron() for _ in range(4*len(word))]
            for t,f,u,g,p in pairs:tets[t].join(f,tets[u],regina.Perm4(*p))
            cases.append((name,tri))
        for index,(name,tri) in enumerate(cases):
            for change in range(2):
                current=tri if not change else relabel(tri,regina,19000+index)
                record,data=cellular_case(current,name,change);records.append(record)
                if index==change==0:quantum=[quantum_case(n,data) for n in (2,3,4,5,6,8,9,10,12)]
            print(f'{name}: exact lattice and face-cochain checks passed',flush=True)
    result={'scope':'Integral half of the preferred longitude and marked boundary Weyl algebra; source-state/regulator comparison remains unproved.',
            'local_identities':local,'Regina_requested':args.regina,
            'cellular_lattice_checks':records,'all_level_quantum_checks':quantum}
    Path(__file__).with_name('integral_half_longitude_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(f'PASS: {len(records)} cellular cases, {len(quantum)} quantum levels',flush=True)


if __name__=='__main__':main()
