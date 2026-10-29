#!/usr/bin/env python3
"""Explicit prism geometry and the actual stationary two-prism cube.

The uniform proof is in the note. Exact rational-circle checks and
symbolic identities supplement numerical face-incidence diagnostics.
"""
from fractions import Fraction as F
import itertools
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

mp.mp.dps = 70


def add(a,b): return (a[0]+b[0],a[1]+b[1])
def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def scale(a,s): return (a[0]*s,a[1]*s)
def det(a,b): return a[0]*b[1]-a[1]*b[0]
def norm(a): return a[0]*a[0]+a[1]*a[1]
def multiply(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def divide(a,b): return scale(multiply(a,(b[0],-b[1])),1/norm(b))
def point(t): return ((1-t*t)/(1+t*t),2*t/(1+t*t))
def mpc(v): return mp.mpc(mp.mpf(v[0].numerator)/v[0].denominator,mp.mpf(v[1].numerator)/v[1].denominator)


def exact_prisms():
    ts=[F(1,4),F(1,3),F(1,2),F(1),F(2),F(3),F(4),
        F(-4),F(-3),F(-2),F(-1),F(-1,2),F(-1,3),F(-1,4)]
    cases=0
    for t1,t2,t3 in itertools.combinations(ts,3):
        v0=(F(1),F(0));v1=point(t1);v2=point(t2);v3=point(t3)
        u=sub(v1,v0);v=sub(v2,v3);w=sub(v3,v0)
        determinant=det(u,v)
        if not determinant: continue
        T=det(w,v)/determinant;S=det(w,u)/determinant
        if T<=1 or S<=1: continue
        P=add(v0,scale(u,T));assert P==add(v3,scale(v,S))
        rho=norm(P)-1;assert rho>0
        def reflection(z):return add(P,scale(sub(z,P),rho/norm(sub(z,P))))
        assert reflection(v0)==v1 and reflection(v1)==v0
        assert reflection(v2)==v3 and reflection(v3)==v2
        kz=divide(multiply(sub(v0,v1),sub(v2,v3)),multiply(sub(v0,v3),sub(v1,v2)))
        assert kz[1]==0 and kz[0]>0
        angles=[mp.arg(mpc(x))%(2*mp.pi)/(2*mp.pi) for x in(v1,v2,v3)]
        p=angles[0];r=angles[1]-angles[0];q=angles[2]-angles[1];ww=1-p-q-2*r
        assert min(p,q,r,ww)>0
        x=q+r;y=p+r;z=p+q+r
        sin=lambda a:mp.sin(mp.pi*a)
        kx=sin(x)*sin(r)/(sin(ww)*sin(p))
        ky=sin(y)*sin(r)/(sin(ww)*sin(q))
        assert abs(kx-mp.mpf((T-1).numerator)/(T-1).denominator)<mp.mpf('1e-55')
        assert abs(ky-mp.mpf((S-1).numerator)/(S-1).denominator)<mp.mpf('1e-55')
        assert abs(sin(p)*sin(q)/(sin(z)*sin(r))-mp.mpf(kz[0].numerator)/kz[0].denominator)<mp.mpf('1e-55')
        cases+=1
    assert cases>50
    return cases


def symbolic_certificates():
    p,q,r=sp.symbols('p q r');w=1-p-q-2*r
    source=[(p+r,q+r,w),(p,q,1-p-q),(p+q,r,r+w)]
    actual=[(p+r,q+r,w),(p,r,1-p-r),(p+r,q,r+w)]
    def phase_key(expr):
        poly=sp.Poly(sp.expand(expr),p,q,r)
        v=(poly.coeff_monomial(p),poly.coeff_monomial(q),poly.coeff_monomial(r),poly.coeff_monomial(1)%1)
        neg=(-v[0],-v[1],-v[2],(-v[3])%1)
        return (v,1) if v<=neg else (neg,-1)
    def certificate(atoms):
        out={}
        for atom in atoms:
            assert sp.expand(sum(atom)-1)==0
            for angle in atom:
                key,sgn=phase_key(angle);out[key]=out.get(key,0)+sgn
        return {k:v for k,v in out.items() if v}
    assert certificate(source)==certificate(actual)
    X,Y,Z,W,T=sp.symbols('X Y Z W T')
    equation=sp.expand((Z*T-1)*(X*Y-T)*(W-T)-(T-X)*(T-Y)*(Z*T-W))
    numerator=X*Y*Z*W-X*Y*Z+X*Y-X*W-Y*W+W
    denominator=X*Y*Z-X*Z-Y*Z+Z*W-W+1
    assert sp.expand(equation-T*(numerator-denominator*T))==0
    z,zb=sp.symbols('z zb')
    ua=z/zb;ub=(1-zb)/(1-z);uc=1/(ua*ub)
    assert sp.cancel((1-1/z)/(1-1/zb)-uc)==0
    assert sp.cancel((1-z)/(1-zb)-1/ub)==0
    return dict(source_atom_and_actual_prism_phase_classes_equal=True,
                five_term_phase_arguments_checked=True,
                stationary_cubic_reduces_to_nonzero_linear_root=True)


def prism(x,y,z):
    p=z-x;q=z-y;r=x+y-z;w=1-x-y
    assert min(p,q,r,w)>0
    vs=[mp.mpc(1),mp.exp(2j*mp.pi*p),mp.exp(2j*mp.pi*(p+r)),mp.exp(2j*mp.pi*(p+r+q))]
    kx=mp.sin(mp.pi*x)*mp.sin(mp.pi*r)/(mp.sin(mp.pi*w)*mp.sin(mp.pi*p))
    P=vs[1]+kx*(vs[1]-vs[0])
    return vs,P


def root(a,b,c,d):
    lo=max(a,b,d-c);hi=min(a+b,d,1-c)
    assert lo<hi
    def derivative(t):
        ss=lambda x:mp.sin(mp.pi*x)
        return mp.log(ss(t+c)*ss(a+b-t)*ss(d-t)/(ss(t-a)*ss(t-b)*ss(t+c-d)))
    for _ in range(220):
        mid=(lo+hi)/2
        if derivative(mid)>0:lo=mid
        else:hi=mid
    t=(lo+hi)/2
    X,Y,Z,W=[mp.exp(2j*mp.pi*v)for v in(a,b,c,d)]
    formula=(X*Y*Z*W-X*Y*Z+X*Y-X*W-Y*W+W)/(X*Y*Z-X*Z-Y*Z+Z*W-W+1)
    assert abs(mp.exp(2j*mp.pi*t)-formula)<mp.mpf('1e-58')
    return t


def sphere(z):
    if z is None:return (mp.mpf(0),mp.mpf(0),mp.mpf(1))
    n=abs(z)**2
    return (2*z.real/(1+n),2*z.imag/(1+n),(n-1)/(1+n))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def subtract(a,b):return tuple(x-y for x,y in zip(a,b))


def cube(a,b,c,d):
    t=root(a,b,c,d);s,P=prism(a,b,t);v,Q=prism(t,c,d)
    alpha=(v[0]*(s[0]-s[3])-v[1]*(s[1]-s[3]))/(s[0]-s[1])
    beta=v[0]*(s[0]-s[3])-alpha*s[0]
    def mobius(z):return alpha if z is None else (alpha*z+beta)/(z-s[3])
    assert abs(mobius(s[2])-Q)<mp.mpf('1e-57')
    side=lambda z:mp.im((z-v[0])*mp.conj(v[1]-v[0]))
    target=side(v[2])
    alternatives=[(mobius(None),mobius(P)),(mobius(0),mobius(1/mp.conj(P)))]
    A,B=next((A,B)for A,B in alternatives if side(A)*target<0 and side(B)*target<0)
    points=[None,Q,*v,A,B]
    # Index order: infinity,Q,v0,v1,v2,v3,A,B.
    faces=[(6,2,3,7),(6,0,1,7),(0,1,4,5),(2,3,4,5),
           (7,3,4,1),(6,2,5,0)]
    coords=[sphere(z) for z in points]
    for face in faces:
        normal=cross(subtract(coords[face[1]],coords[face[0]]),subtract(coords[face[2]],coords[face[0]]))
        signed=[dot(normal,subtract(z,coords[face[0]])) for z in coords]
        assert max(abs(signed[i])for i in face)<mp.mpf('1e-53')
        rest=[signed[i]for i in range(8)if i not in face]
        assert all(x>0 for x in rest) or all(x<0 for x in rest)
    reflected=Q+(abs(Q)**2-1)/(mp.conj(A)-mp.conj(Q))
    assert abs(reflected-B)<mp.mpf('1e-54')
    # Four endpoints of the OTHER reflection-section diagonal lie on
    # one actual ideal circle, giving the alternative prism cut.
    other=(A-v[2])*(B-v[3])/((A-v[3])*(B-v[2]))
    assert abs(mp.im(other))<mp.mpf('1e-54')
    u=root(b,c,a,d)
    return dict(boundary=[float(v)for v in(a,b,c,d)],
                left_internal=float(t),right_internal=float(u),
                six_convex_ideal_cube_faces=True,common_reflection=True,
                actual_alternative_ideal_quadrilateral_cut=True)


def main():
    exact=exact_prisms();symbolic=symbolic_certificates()
    cases=[]
    for abc in ((2,3,4),(3,3,4),(2,5,3),(4,3,5),(3,5,4),(2,2,3),
                (1,4,5),(4,4,4),(2,3,6),(5,4,3)):
        a,b,c=[mp.mpf(v)/20 for v in abc]
        lower=max(a,b,c);upper=min(mp.mpf(1),a+b+c)
        for ratio in (mp.mpf(1)/3,mp.mpf(2)/3):
            cases.append(cube(a,b,c,lower+(upper-lower)*ratio))
    result=dict(status='PASS',exact_rational_circle_prisms=exact,
                symbolic_certificates=symbolic,stationary_actual_ideal_cubes=cases,
                scope='Uniform proof in note; exact rational reflection/face checks and symbolic Bloch-phase/critical equations; high-precision actual cube incidence and alternative cuts. No arbitrary closed-link geometry inferred.')
    Path(__file__).with_name('actual_newton_ideal_prism_and_associativity_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',exact,'exact rational-circle prisms; symbolic phase/critical identities;',len(cases),'stationary actual ideal cubes')


if __name__=='__main__':main()
