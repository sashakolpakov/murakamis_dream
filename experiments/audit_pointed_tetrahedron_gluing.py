#!/usr/bin/env python3
"""Pointed shape-ordering coherence and integral edge reduction.

Exact symbolic quantum-torus maps, finite root intertwiners, projector
ranks including even levels, and optional Regina incidence/Smith tests.
These do not compare the selected gluing vector with the actual ADO
source period or prove a volume asymptotic.
"""

import argparse
from itertools import combinations, product
import json
from math import gcd
from pathlib import Path
from random import Random

import numpy as np
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form

from audit_actual_peripheral_fusion import inverse_mod, matrix_power
from audit_cyclic_steinberg_lattice import determinant, rank
from audit_finite_sum_annihilator import field
from audit_regular_holonomy_braiding import mm

R=sp.Symbol('R',nonzero=True)
EDGES=list(combinations(range(4),2))


def multiply(a,b):
    c,i,j=a;d,k,l=b
    return sp.cancel(c*d*R**(-j*k)),i+k,j+l


def power(a,n):
    c,i,j=a
    return sp.cancel(c**n*R**(-i*j*n*(n-1)//2)),i*n,j*n


def rho(a):
    c,i,j=a
    return multiply((c,0,0),multiply(power((1,0,-1),i),power((-R,1,-1),j)))


def sigma(a):
    c,i,j=a
    return sp.cancel(c.subs(R,1/R) if hasattr(c,'subs') else c)*R**(-i*j),j,i


def same(a,b):
    return a[1:]==b[1:] and sp.cancel(a[0]-b[0])==0


def abstract_symmetry():
    for i,j in product(range(-3,4),repeat=2):
        a=(R**(i-j),i,j)
        assert same(rho(rho(rho(a))),a)
        assert same(sigma(sigma(a)),a)
        assert same(sigma(rho(sigma(a))),rho(rho(a)))
    def add(terms):
        out={}
        for c,i,j in terms:out[i,j]=sp.cancel(out.get((i,j),0)+c)
        return {key:value for key,value in out.items() if value!=0}
    L=[(1,1,0),(1,0,1),(-1,0,0)]
    assert add([rho(a) for a in L])==add([multiply((-1,0,-1),a) for a in L])
    assert add([sigma(a) for a in L])==add(L)
    return {'Laurent_monomials':49,'rho_cubed_sigma_squared_and_S3_exact':True,
            'pointed_left_ideal_preserved_with_full_unit':True}


def shape_field(level):
    for k in range(10,1000):
        prime=4*level*k+1
        if not sp.isprime(prime):continue
        roots={pow(a,level,prime):a for a in range(1,prime)}
        choices=[(s,roots[(1-pow(s,level,prime))%prime]) for s in range(1,prime)
                 if (1-pow(s,level,prime))%prime in roots]
        if choices:
            generator=int(sp.primitive_root(prime));q=pow(generator,(prime-1)//(2*level),prime)
            return prime,q,choices[0]
    raise AssertionError('no diagnostic nondegenerate shape field')


def shape_module(level,prime,s,t,r):
    omega=r*r%prime
    X=np.diag([s*pow(omega,a,prime)%prime for a in range(level)]).astype(np.int64)
    Y=np.zeros((level,level),dtype=np.int64)
    for a in range(level):Y[(a+1)%level,a]=t
    assert pow(s,level,prime)+pow(t,level,prime)==1 or (pow(s,level,prime)+pow(t,level,prime))%prime==1
    p=np.ones(level,dtype=np.int64)
    for a in range(1,level):p[a]=p[a-1]*t*pow(1-s*pow(omega,a,prime),-1,prime)%prime
    L=(X+Y-np.eye(level,dtype=np.int64))%prime
    assert not np.any(L@p%prime) and rank(L,prime)==level-1
    return X,Y,p


def adapter(level,prime,params,kind):
    s,t,r=params
    X,Y,p=shape_module(level,prime,*params)
    if kind=='rho':
        A=inverse_mod(Y,prime);B=-mm(prime,A,X)%prime
        target=(pow(t,-1,prime),r*s*pow(t,-1,prime)%prime,r)
    else:
        A,B=Y,X
        target=(t,s,pow(r,-1,prime))
    Xt,Yt,pt=shape_module(level,prime,*target)
    I=np.eye(level,dtype=np.int64);projection=np.zeros_like(I);term=I.copy()
    for _ in range(level):
        projection=(projection+term)%prime
        term=mm(prime,term,A*pow(target[0],-1,prime)%prime)
    projection=projection*pow(level,-1,prime)%prime
    v=projection[:,0]
    columns=[]
    for _ in range(level):
        columns.append(v);v=mm(prime,B*pow(target[1],-1,prime)%prime,v.reshape(-1,1))[:,0]
    J=np.column_stack(columns)
    assert determinant(J,prime)
    assert np.array_equal(mm(prime,A,J),mm(prime,J,Xt))
    assert np.array_equal(mm(prime,B,J),mm(prime,J,Yt))
    anchor=int((J@pt%prime)[0]);assert anchor
    J=J*pow(anchor,-1,prime)%prime
    assert np.array_equal(J@pt%prime,p)
    return J,target


def move_word(level,prime,params,word):
    value=np.eye(level,dtype=np.int64);current=params
    for kind in word:
        J,current=adapter(level,prime,current,kind)
        value=mm(prime,value,J)
    return value,current


def root_symmetry(level,sign):
    prime,q,(s,t)=shape_field(level)
    r=q if sign>0 else pow(q,-1,prime)
    params=(s,t,r);I=np.eye(level,dtype=np.int64)
    for word in [('rho',)*3,('sigma',)*2]:
        value,current=move_word(level,prime,params,word)
        assert current==params and np.array_equal(value,I)
    left,lp=move_word(level,prime,params,('sigma','rho','sigma'))
    right,rp=move_word(level,prime,params,('rho','rho'))
    assert lp==rp and np.array_equal(left,right)
    return {'level':level,'orientation_parameter':sign,'prime':prime,
            'clock_shift_and_pointed_kernel_exact':True,'canonical_adapters_constructed':True,
            'all_S3_relations_scalar_one_exact':True,'full_rotation_root_q_retained':True}


def local_stokes():
    left=sp.symbols('l01 l02 l03 l12 l13 l23')
    right=sp.symbols('m01 m02 m03 m12 m13 m23')
    l=dict(zip(EDGES,left));m=dict(zip(EDGES,right))
    def abc(x):return x[0,1]+x[2,3],x[0,2]+x[1,3],x[0,3]+x[1,2]
    a,b,c=abc(l);u,v,w=abc(m)
    full=(a-c)*(v-w)-(b-c)*(u-w)
    def omega(x,y):return sum(x[i]*y[(i+1)%3]-x[(i+1)%3]*y[i] for i in range(3))
    faces=0
    for f in range(4):
        vertices=[v for v in range(4) if v!=f]
        edges=list(combinations(vertices,2))
        faces-=(-1)**f*omega([l[e] for e in edges],[m[e] for e in edges])
    assert sp.expand(full-faces)==0
    return {'six_edge_oriented_face_pairing_identity_exact':True}


def incidence(tri):
    count=tri.size();m=tri.countEdges();v=tri.countVertices()
    signs=[tet.orientation() for tet in tri.tetrahedra()]
    rows=np.zeros((m,2*count),dtype=np.int64)
    d0=np.zeros((m,v),dtype=np.int64);seen=set()
    faces=[]
    for j,tet in enumerate(tri.tetrahedra()):
        for local,(a,b) in enumerate(EDGES):
            edge=tet.edge(local).index()
            vec=((1,0),(0,1),(-1,-1))[min(local,5-local)]
            rows[edge,2*j:2*j+2]+=signs[j]*np.array(vec,dtype=np.int64)
            if edge not in seen:
                d0[edge,tet.vertex(a).index()]+=1;d0[edge,tet.vertex(b).index()]+=1
                seen.add(edge)
        for f in range(4):
            other=tet.adjacentTetrahedron(f).index();perm=tet.adjacentGluing(f)
            if (j,f)>(other,perm[f]):continue
            row=np.zeros(m,dtype=np.int64)
            for a,b in combinations([a for a in range(4) if a!=f],2):
                row[tet.edge(EDGES.index((a,b))).index()]+=1
            faces.append(row)
    d1=np.array(faces,dtype=np.int64)
    h1=m-rank(d1,2)-rank(d0,2)
    Omega=np.zeros((2*count,2*count),dtype=np.int64)
    for j,e in enumerate(signs):Omega[2*j:2*j+2,2*j:2*j+2]=np.array([[0,e],[-e,0]])
    assert not np.any(rows@Omega@rows.T)
    S=smith_normal_form(sp.Matrix(rows),domain=sp.ZZ)
    invariants=[abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]]
    assert len(invariants)==m-v
    assert all(d in (1,2) for d in invariants) and invariants.count(2)==h1
    assert m-rank(rows,2)==v+h1
    return rows,signs,{'tetrahedra':count,'edges':m,'vertices':v,
                       'compactification_H1_mod_two':h1,'edge_Smith_invariants':invariants,
                       'isotropy_and_mod_two_kernel_formula_exact':True}


def relabel(tri,regina,seed):
    rng=Random(seed);perms=[]
    for _ in range(tri.size()):
        p=list(range(4));rng.shuffle(p);perms.append(p)
    new=regina.Triangulation3();tets=[new.newTetrahedron() for _ in range(tri.size())]
    for j,tet in enumerate(tri.tetrahedra()):
        for f in range(4):
            k=tet.adjacentTetrahedron(f).index();old=tet.adjacentGluing(f)
            if (j,f)>(k,old[f]):continue
            inverse=[perms[j].index(a) for a in range(4)]
            p=[perms[k][old[inverse[a]]] for a in range(4)]
            tets[j].join(perms[j][f],tets[k],regina.Perm4(*p))
    assert new.isValid() and new.isOrientable() and new.isIsomorphicTo(tri) is not None
    return new


def regina_cases():
    import regina
    from audit_crossing_fundamental_cycle import shadow_pairing
    examples=[('figure_eight',regina.Example3.figureEight(),True),
              ('trefoil',regina.Example3.trefoil(),True),
              ('Whitehead_link',regina.Example3.whitehead(),True)]
    for p in (2,3,4,8):examples.append((f'lens_{p}',regina.Example3.lens(p,1),False))
    words=[('unknot_positive',2,[(0,1)]),('unknot_negative',2,[(0,-1)]),
           ('Hopf',2,[(0,1)]*2),('trefoil_shadow',2,[(0,1)]*3),
           ('figure_eight_shadow',3,[(0,1),(1,-1)]*2),
           ('weaving_3_4',3,[(0,1),(1,-1)]*4),
           ('torus_3_4',3,[(0,1),(1,1)]*4),
           ('weaving_4_3',4,[(0,1),(1,-1),(2,1)]*3)]
    for name,b,word in words:
        pairs,_=shadow_pairing(b,word);tri=regina.Triangulation3()
        tets=[tri.newTetrahedron() for _ in range(4*len(word))]
        for t,f,u,g,p in pairs:tets[t].join(f,tets[u],regina.Perm4(*p))
        assert tri.isValid() and tri.isOrientable()
        examples.append((name,tri,True))
    records=[]
    for index,(name,tri,is_link) in enumerate(examples):
        for change in range(3):
            current=tri if not change else relabel(tri,regina,9100+17*index+change)
            _,_,record=incidence(current)
            if is_link:
                assert record['compactification_H1_mod_two']==0
                assert set(record['edge_Smith_invariants'])<=set([1])
            records.append({'name':name,'relabeling':change,'S3_link_exterior':is_link,**record})
    return records,examples[:3]


def weyl(v,signs,level,prime,q):
    Q0=q*q%prime;lam=-q%prime
    answer=np.array([[1]],dtype=np.int64)
    for j,e in enumerate(signs):
        a,b=int(v[2*j]),int(v[2*j+1])
        X=np.diag([pow(Q0,e*k,prime) for k in range(level)]).astype(np.int64)
        Y=np.zeros_like(X)
        for k in range(level):Y[(k+1)%level,k]=1
        local=mm(prime,matrix_power(X,a%level,prime),matrix_power(Y,b%level,prime))
        local=local*pow(lam,-e*a*b,prime)%prime
        answer=np.kron(answer,local)%prime
    return answer


def projector_case(level,tri,name):
    rows,signs,_=incidence(tri);count=len(signs)
    basis=hermite_normal_form(sp.Matrix(rows).T).T
    r=basis.rows;prime,_,q=field(level);size=level**count
    I=np.eye(size,dtype=np.int64);P=I.copy()
    for i in range(r):
        U=weyl(list(basis.row(i)),signs,level,prime,q)
        assert np.array_equal(matrix_power(U,level,prime),I)
        term=I.copy();Pi=np.zeros_like(I)
        for _ in range(level):Pi=(Pi+term)%prime;term=mm(prime,term,U)
        P=mm(prime,P,Pi*pow(level,-1,prime)%prime)
    expected=level**(count-r)
    assert rank(P,prime)==expected and np.array_equal(mm(prime,P,P),P)
    boundary=False
    if count==2 and count-r==1:
        O=np.zeros((4,4),dtype=np.int64)
        for j,e in enumerate(signs):O[2*j:2*j+2,2*j:2*j+2]=np.array([[0,e],[-e,0]])
        B=np.array(basis.tolist(),dtype=np.int64)
        candidates=[np.array(v,dtype=np.int64) for v in product(range(-2,3),repeat=4)
                    if any(v) and not np.any(B@O@np.array(v,dtype=np.int64))]
        pair=next((a,b) for a in candidates for b in candidates if int(a@O@b)==1)
        for a,b in product(range(level),repeat=2):
            W=weyl(a*pair[0]+b*pair[1],signs,level,prime,q)
            value=int(np.einsum('ij,ji->',P,W))%prime
            assert value==(expected if not a and not b else 0)
        boundary=True
    return {'name':name,'level':level,'tetrahedra':count,'edge_rank':r,
            'projector_rank':expected,'idempotent_exact':True,
            'saturated_boundary_trace_basis_exact':boundary}


def parity_cases(level):
    prime,_,q=field(level);Q0=q*q%prime;I=np.eye(level,dtype=np.int64)
    X=np.diag([pow(Q0,a,prime) for a in range(level)]).astype(np.int64)
    Y=np.zeros_like(X)
    for a in range(level):Y[(a+1)%level,a]=1
    U=mm(prime,X,X)
    ranks=[]
    for character in (1,Q0):
        term=I.copy();P=np.zeros_like(I)
        for j in range(level):P=(P+term*pow(character,-j,prime))%prime;term=mm(prime,term,U)
        P=P*pow(level,-1,prime)%prime
        expected=gcd(2,level) if level%2 or character==1 else 0
        assert rank(P,prime)==expected;ranks.append(expected)
    if level%2:
        assert np.array_equal(matrix_power(U,(level+1)//2,prime),X)
    else:
        Z=matrix_power(Y,level//2,prime)
        P=(I+Z)*pow(2,-1,prime)%prime;Pm=(I-Z)*pow(2,-1,prime)%prime
        assert rank(P,prime)==rank(Pm,prime)==level//2
        assert not np.any((mm(prime,U,P)-mm(prime,P,U))%prime)
        assert np.array_equal(mm(prime,X,P,inverse_mod(X,prime)),Pm)
    return {'level':level,'nonprimitive_edge_character_ranks':ranks,
            'marked_index_two_boundary_keeps_even_sectors':True}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--regina',action='store_true');args=parser.parse_args()
    symbolic=abstract_symmetry();stokes=local_stokes()
    roots=[root_symmetry(n,e) for n in (2,3,4,5,6,8,9,10,12) for e in (1,-1)]
    parity=[parity_cases(n) for n in (2,3,4,5,6,8,9,10,12)]
    print(f'pointed root S3 adapters: {len(roots)} passed',flush=True)
    incidence_checks=[];projectors=[]
    if args.regina:
        incidence_checks,small=regina_cases()
        print(f'exact incidence/Smith checks: {len(incidence_checks)} passed',flush=True)
        projectors=[projector_case(n,small[0][1],small[0][0]) for n in (2,3,4,5,6,8,9,10,12)]
        projectors += [projector_case(n,small[2][1],small[2][0]) for n in (2,3)]
        print(f'all-level edge projectors: {len(projectors)} passed',flush=True)
    result={'scope':'Pointed tetrahedron order changes and integral/all-level edge reduction; selected ADO gluing period and regulator norm are not identified.',
            'abstract_order_symmetry':symbolic,'local_edge_Stokes':stokes,
            'root_pointed_adapters':roots,'parity_and_nonprimitive_scope':parity,
            'Regina_requested':args.regina,'integral_edge_lattices':incidence_checks,'edge_projectors':projectors}
    Path(__file__).with_name('pointed_tetrahedron_gluing_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',flush=True)


if __name__=='__main__':main()
