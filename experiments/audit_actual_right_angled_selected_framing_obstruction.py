#!/usr/bin/env python3
"""Exact Lorentz/lift identities and a right-angled octahedral convex audit.

The diagram-wide Morse dictionary is a written topological proof, not
established by the finite octahedral fixture.
"""
import itertools
import json
from pathlib import Path
import random
import sympy as s

E=s.Matrix([[0,-1],[1,0]])

def M(n):
    a,b,c,d=n
    return s.Matrix([[a+d,b-s.I*c],[b+s.I*c,a-d]])

def H(n):return M(n).adjugate()
def J(n):return E*s.conjugate(H(n))
def lor(a,b):return -a[0]*b[0]+sum(a[k]*b[k] for k in range(1,4))
def trace(a):return s.simplify(s.trace(a))
def flag(w):return s.Matrix([w,1])
def lift(w):
    a,b=s.re(w),s.im(w);den=1+a*a+b*b
    return s.Matrix([1,2*a/den,-2*b/den,(a*a+b*b-1)/den])
def polar(n,w,v):return s.simplify((s.conjugate(flag(w)).T*H(n)*flag(v))[0])


def symbolic():
    n=s.symbols('n0:4',real=True);m=s.symbols('m0:4',real=True)
    assert s.simplify(J(n)*s.conjugate(J(n))-lor(n,n)*s.eye(2))==s.zeros(2)
    assert s.simplify(trace(J(m)*s.conjugate(J(n)))-2*lor(m,n))==0
    wr,wi,vr,vi,yr,yi=s.symbols('wr wi vr vi yr yi',real=True)
    w=wr+s.I*wi;v=vr+s.I*vi;y=yr+s.I*yi
    n_y=lift(y)*(1+yr*yr+yi*yi)/2
    expected=s.conjugate(s.det(s.Matrix.hstack(flag(y),flag(w))))*s.det(s.Matrix.hstack(flag(y),flag(v)))
    assert s.simplify(polar(n_y,w,v)-expected)==0
    assert s.simplify(s.det(s.Matrix.hstack(flag(w),J(n)*s.conjugate(flag(v))))-s.conjugate(polar(n,w,v)))==0
    j0=s.Matrix([[-1,0],[0,1]])
    jm=s.Matrix([[1,0],[2,-1]])
    j1=s.Matrix([[1,-2],[0,-1]])
    A=jm*j0;B=j1*jm;P=j1*j0
    assert A==s.Matrix([[-1,0],[-2,-1]])
    assert B==s.Matrix([[-3,2],[-2,1]])
    assert P==s.Matrix([[-1,-2],[0,-1]]) and B*A==P
    assert all(trace(g)==-2 for g in (A,B,P))


def octahedron():
    white=[s.Matrix([1,*v]) for v in itertools.product((-1,1),repeat=3) if v[0]*v[1]*v[2]==1]
    black=[s.Matrix([1,*v]) for v in itertools.product((-1,1),repeat=3) if v[0]*v[1]*v[2]==-1]
    facets=[]
    for b in black:
        face=[k for k,n in enumerate(white) if lor(b,n)==0]
        assert len(face)==3
        assert all(lor(b,n)<0 for k,n in enumerate(white) if k not in face)
        facets.append(face)
    assert sorted(sum(([tuple(sorted((face[i],face[(i+1)%3]))) for i in range(3)] for face in facets),[])) == sorted([p for p in itertools.combinations(range(4),2) for _ in range(2)])
    js=[J(n)/s.sqrt(2) for n in white]
    prefix_checks=0
    for order in itertools.permutations(range(4)):
        product=s.eye(2)
        for a,b in zip(order,order[1:]):
            head=js[b]*s.conjugate(js[a]);assert trace(head)==-2
            product=head*product
            assert s.simplify(product-js[b]*s.conjugate(js[order[0]]))==s.zeros(2)
            prefix_checks+=1
    prescribed=0
    base=s.Matrix([s.Rational(2,3),s.Rational(2,3),-s.Rational(1,3)])
    points=[]
    for b in black:
        center=s.Matrix(list(b)[1:])/3
        circle=s.Matrix([b[k+1]*base[k] for k in range(3)])
        point=center+s.Rational(101,100)*(circle-center)
        lift_point=s.Matrix([1,*point])
        assert sum(v*v for v in circle)==1
        assert lor(b,lift_point)==0 and sum(v*v for v in point)>1
        assert all(lor(other,lift_point)<0 for other in black if other!=b)
        points.append(point)
    for a,b in itertools.combinations(points,2):
        midpoint=(a+b)/2
        assert sum(v*v for v in midpoint)<1
        assert all(lor(n,s.Matrix([1,*midpoint]))<0 for n in black)
        prescribed+=1
    candidates=[]
    for a,b in itertools.product(range(-8,9),repeat=2):
        w=s.Rational(a,3)+s.I*s.Rational(b,3)
        p=lift(w)
        if all(lor(n,p)<0 for n in black):candidates.append(w)
    assert len(candidates)>20
    rng=random.Random(301026);checked=0;selected=0;two_facets=0
    for _ in range(80):
        w,w0=rng.sample(candidates,2);p=lift(w);q=lift(w0)
        direction=q-p
        hit_facets=[]; transverse=True
        for bi,normal in enumerate(black):
            slope=lor(normal,direction)
            if slope==0:continue
            hit=p-lor(normal,p)*direction/slope
            columns=s.Matrix.hstack(*[white[k] for k in facets[bi]])
            coeff=list(s.linsolve((columns,hit)))[0]
            if all(t>=0 for t in coeff):
                hit_facets.append(bi)
                transverse=transverse and all(t>0 for t in coeff)
        if transverse:
            assert len(hit_facets)==2
            two_facets+=1
        exits=[]
        for i,b in enumerate(black):
            slope=lor(b,direction)
            if slope>0:exits.append((-lor(b,p)/slope,i))
        assert exits
        time,index=min(exits,key=lambda z:z[0]);assert time>1
        point=p+time*direction
        assert lor(black[index],point)==0
        assert all(lor(b,point)<=0 for b in black)
        face=facets[index]
        columns=s.Matrix.hstack(*[white[k] for k in face])
        weights=list(s.linsolve((columns,point)))[0]
        assert all(t>=0 for t in weights) and sum(weights)==1
        vals=[polar(n,w,w0) for n in white]
        assert s.simplify(sum(weights[i]*vals[k] for i,k in enumerate(face)))==0
        # Literal rank-one prefix coefficients, including the global exterior
        # reflection and a single shared covector.
        v=js[0]*s.conjugate(flag(w0))
        denominator=s.simplify(v[0]-w*v[1])
        if denominator==0:continue
        ell=s.Matrix([[1,-w]])/denominator;Pi=v*ell
        assert s.simplify(Pi*Pi-Pi)==s.zeros(2) and trace(Pi)==1
        actual=[trace(js[k]*s.conjugate(js[0])*Pi) for k in range(4)]
        assert s.simplify(sum(weights[i]*actual[k] for i,k in enumerate(face)))==0
        # For every shaded pair and either common white face, the right flag
        # remains in both selected halfspaces, as required by the strip test.
        for i,j in itertools.combinations(range(4),2):
            common=set(facets[i])&set(facets[j]);assert len(common)==2
            for f in common:
                n=white[f]/s.sqrt(2)
                reflected=q-2*lor(q,n)*n
                assert reflected[0]>0
                assert lor(black[i],reflected)<0 and lor(black[j],reflected)<0
                selected+=1
        checked+=1
    return dict(exact_outward_prefix_products=prefix_checks,
                selected_boundary_flags_available=len(candidates),
                exact_polar_kernel_facet_relations=checked,
                exact_generic_two_facet_cases=two_facets,
                exact_prescribed_distinct_facet_pairs=prescribed,
                exact_selected_pair_reflections=selected,
                convex_facets=facets)


def main():
    symbolic()
    result=dict(status='PASS',exact_symbolic=['reflection involution and Lorentz trace',
        'null polarization factorization and determinant convention',
        'canonical source A,B,P with trace minus two'],octahedral_fixture=octahedron(),
        scope='Exact lift/polarization conventions and finite convex checks. The general facet-sphere and actual Morse-prefix identification require the written proof; no volume-conjecture counterexample is asserted.')
    Path(__file__).with_name('actual_right_angled_selected_framing_obstruction_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
