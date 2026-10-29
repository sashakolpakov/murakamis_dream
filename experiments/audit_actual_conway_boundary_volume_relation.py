#!/usr/bin/env python3
"""Exact prescribed-output support and relative-boundary certificates."""
import json
from fractions import Fraction
from math import isqrt
from pathlib import Path
import sympy as sp
from audit_actual_positive_conway_variational_limit import EXPRS, compile_wires


def anchor(expr,d,r):
    assert d>=2 and 0<=r<=d
    if expr[0]=='A':
        m=d//2
        i=min(m,r);j=min(m,r-i);k=r-i-j
        assert 0<=k<=m
        return [i,j,k,i+j,r]
    if expr[0]=='turn':
        return anchor(expr[1],d,d-r)+[r]
    return anchor(expr[1],d,r)+anchor(expr[2],d,0)+[r]


def verify(nodes,root,d,labels,r):
    assert len(labels)==len(nodes) and labels[root]==r
    for (kind,children),v in zip(nodes,labels):
        assert isinstance(v,int) and 0<=v<=d
        if kind=='h':assert 2*v<=d
        elif kind=='turn':assert v+labels[children[0]]==d
        else:
            i,j=(labels[c] for c in children)
            assert max(i,j)<=v<=i+j<=d


def support():
    anchors=corrections=endpoints=0
    for expr in EXPRS:
        nodes,root=compile_wires(expr)
        for d in range(2,27):
            for r in range(d+1):
                verify(nodes,root,d,anchor(expr,d,r),r);anchors+=1
        D=12;eps=Fraction(1,4)
        for base_r in (3,6,9):
            base=anchor(expr,D,base_r)
            for d in range(200,601,7):
                k=((1-eps)*d)//D;l=d-k*D
                # Prescribed outputs oscillate around the interior base ratio.
                r=(d*base_r)//D+(isqrt(d)//4)*(1 if d%2 else -1)
                R=r-k*base_r
                assert 0<=R<=l
                a=anchor(expr,l,R)
                labels=[k*u+v for u,v in zip(base,a)]
                verify(nodes,root,d,labels,r)
                assert all(abs(D*v-d*u)<=D*l for u,v in zip(base,labels))
                corrections+=1
        for end in (0,1):
            base=anchor(expr,D,end*D)
            for d in range(30,600,7):
                deviation=isqrt(d)
                r=deviation if end==0 else d-deviation
                lower=deviation+2
                l=lower+(d-lower)%D;k=(d-l)//D
                R=r-k*end*D
                assert 0<=R<=l and l<deviation+2+D
                a=anchor(expr,l,R)
                labels=[k*u+v for u,v in zip(base,a)]
                verify(nodes,root,d,labels,r)
                assert all(abs(D*v-d*u)<=D*l for u,v in zip(base,labels))
                endpoints+=1
    return {'full_output_anchors':anchors,'interior_exact_output_corrections':corrections,
            'sublinear_endpoint_corrections':endpoints,'expressions':len(EXPRS)}


def algebraic_boundary():
    U,M=sp.symbols('U M',nonzero=True)
    sine=lambda t:(t-1/t)/sp.I
    t_c=-1/(U*M)
    internal=sp.factor(sp.together(sine(U)-sine(t_c)))
    assert sp.cancel(internal/(U*U*M+1)-sp.I*(M-1)/(M*U)) == 0
    P=sine(M)/sine(t_c)
    z=U*P;zd=P/U
    relation=sp.Poly(U*U*M+1,U)
    def rem(expr):
        numerator=sp.cancel(expr).as_numer_denom()[0]
        return sp.rem(numerator,relation.as_expr(),U)
    assert rem(P**2-(2-M-1/M))==0
    assert rem(z-(1-1/M))==0
    assert rem(zd-(1-M))==0
    # Additive basis m=ell(M), a=ell(1-M), with p=a-m/2.
    wedge=lambda v,w:v[0]*w[1]-v[1]*w[0]
    delta_z=wedge((-1,1),(-1,0))
    delta_zd=wedge((0,1),(1,0))
    assert Fraction(delta_z-delta_zd,2)==wedge((1,0),(Fraction(-1,2),1))==1
    return {'internal_relation':'U^2 M=-1','boundary_relation':'P^2=2-M-M^-1',
            'companion_shapes':'1-M^-1, 1-M','relative_boundary':'delta beta=M wedge P',
            'rational_symbolic_checks':'PASS'}


def strict_profiles():
    def state(expr,b):
        if expr[0]=='A':
            c=min(b/2,(1-b)/2,Fraction(1,4))/2
            t=b-c/2
            a=(t/2+min(t,Fraction(1,2)))/2
            return [a,a,c,t,b]
        if expr[0]=='turn':return state(expr[1],1-b)+[b]
        x=(b/2+min(b,Fraction(1,2)))/2
        return state(expr[1],x)+state(expr[2],x)+[b]
    count=0
    for expr in EXPRS:
        nodes,root=compile_wires(expr)
        for r in range(1,200):
            b=Fraction(r,200);labels=state(expr,b)
            assert labels[root]==b
            for (kind,children),v in zip(nodes,labels):
                if kind=='h':assert 0<v<Fraction(1,2)
                elif kind=='turn':assert v+labels[children[0]]==1
                else:
                    x,y=(labels[c] for c in children)
                    assert min(v-x,v-y,x+y-v,1-x-y)>0
            count+=1
    return {'exact_strict_interior_profiles':count,'expressions':len(EXPRS),
            'scope':'Constructive strict feasibility; global optimizer strictness is the written barrier proof.'}


if __name__=='__main__':
    result={'status':'PASS','support':support(),'strict_feasibility':strict_profiles(),'boundary':algebraic_boundary(),
            'scope':'Exact prescribed-output support and normalization checks supplement the uniform proof. No knot A-polynomial or manifold-volume identification is asserted.'}
    Path(__file__).with_name('actual_conway_boundary_volume_relation_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',result['support'],'/exact algebraic boundary and wedge normalization')
