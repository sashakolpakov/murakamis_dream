#!/usr/bin/env python3
"""Exact rational checks supporting the written preferred-longitude proof.

These checks do not prove topology, constant-field descent, an all-fiber
existence assertion, spin holonomy, or the stationary analytic theorem.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
COUNT = 0


def zero(x):
    global COUNT
    assert s.cancel(x) == 0, s.factor(x)
    COUNT += 1


def same(a, b):
    assert a.shape == b.shape
    for x, y in zip(a, b):
        zero(x-y)


def projective(a, b):
    k = next(i for i, x in enumerate(b) if x != 0)
    for x, y in zip(a, b):
        zero(x*b[k]-y*a[k])


def affine(a, slope, shift):
    zero(a[1, 0]); zero(a[0, 0]-slope*a[1, 1])
    zero(a[0, 1]-shift*a[1, 1])
    assert s.cancel(a.det()) != 0


def edge_checks():
    M, Q, P, X, beta, gamma = s.symbols('M Q P X beta gamma', nonzero=True)
    D=M**2+M**-2; S=beta+gamma+D+2
    F=S*(X**2+1)+(beta*gamma-2*D)*X
    zero((X**2+beta*X+1)*(X**2+gamma*X+1)-(X-1)**2*(X**2-D*X+1)-X*F)
    J=beta*gamma-2*beta-2*gamma-4*D-4
    zero(s.discriminant(F,X)-(beta+2)*(gamma+2)*J)
    for x, target in [(1,(beta+2)*(gamma+2)),(-1,-J),
                       (M**2,M**2*(beta+D)*(gamma+D)),
                       (M**-2,M**-2*(beta+D)*(gamma+D))]:
        zero(F.subs(X,x)-target)
    H=(Q-1)**2*(P-1)**2-4*(M+M**-1)**2*Q*P
    zero(((beta+2)*(gamma+2)*J).subs({beta:Q+1/Q,gamma:P+1/P})
         -(Q+1)**2*(P+1)**2*H/(Q**2*P**2))
    t,x,y=s.symbols('t x y')
    zero(s.discriminant((x-1)**2*(y-1)**2-4*t*x*y,y)
         -16*t*x*(x*x+(t-2)*x+1))
    R=(X+Q)*(X+1/Q)*(X+P)*(X+1/P)/((X-1)**2*(1-X*M*M)*(1-X/M**2))
    f=(M*M-X)/(1-M*M*X); rho=(Q+X)/(1+Q*X)
    zero(M*s.diff(R,M)/R-2*X*s.diff(f,X)/f)
    zero(Q*s.diff(R,Q)/R+X*s.diff(rho,X)/rho)
    zero(P*s.diff(R,P)/R+X*s.diff((P+X)/(1+P*X),X)/((P+X)/(1+P*X)))
    zero((M*s.diff(f,M)/f).subs(M,1)-2*(1+X)/(1-X))
    for root in [-(Q+P)/(1+Q*P),-(1+Q*P)/(Q+P)]:
        zero(F.subs({M:s.I,beta:Q+1/Q,gamma:P+1/P,X:root}, simultaneous=True))
    # The wrong differential factor and the wrong surgery sign must fail.
    assert s.cancel(M*s.diff(R,M)/R-X*s.diff(f,X)/f) != 0
    return M,beta,gamma,X,D,S,F


def character_checks(data):
    M,beta,gamma,X,D,S,F=data
    # Rational parametrization of the same quadratic, not a numerical sample.
    gam=s.cancel((2*D-(X+1/X)*(beta+D+2))/(X+1/X+beta))
    sub=lambda a: a.applyfunc(lambda x:s.cancel(x.subs(gamma,gam))) if isinstance(a,s.MatrixBase) else s.cancel(a.subs(gamma,gam))
    t=M+1/M; p=-beta; q=-gamma; calX=2+S*X; h=M-1/M
    c=(M*calX+q/M-2*t)/(D-p)
    d=(q-M*M-1+h*c)/(p-2); e=calX-1-1/M**2-h*c
    A=s.Matrix([[M,1],[0,1/M]]); B=s.Matrix([[1/M,0],[p-2,M]])
    C=sub(s.Matrix([[c,d],[e,t-c]])); Do=(A*B*C).inv().applyfunc(s.cancel)
    for mat in (A,B,C,Do): zero(mat.det()-1); zero(s.trace(mat)-t)
    same(A*B*C*Do,s.eye(2))
    zero(s.trace(A*B)+beta); zero(s.trace(B*C)+gam)
    V=A*B-(1+X*(beta+1))/(1-X)*s.eye(2)
    T=(B*C+(X+gam+1)/(1-X)*s.eye(2)).applyfunc(s.cancel)
    same(V*A,Do.inv()*V); same(V*B,C.inv()*V)
    same(T*B,A.inv()*T); same(T*C,Do.inv()*T)
    zero(V.det()-sub(X*(beta+2)**2*(beta+D)/(S*(X-1)**2)))
    zero(T.det()-sub(X*(gamma+2)**2*(gamma+D)/(S*(X-1)**2)))
    zero(s.trace(A*B*A.inv()*B.inv())-2-(beta+2)*(beta+D))
    zero(((A*B).inv()-s.eye(2)).det()-(beta+2))
    Q,P=s.symbols('Q P',nonzero=True)
    zv=-(1+X*(Q+1/Q+1))/(1-X)
    zw=(X+P+1/P+1)/(1-X)
    zero((zv-Q)/(zv-1/Q)-(Q+X)/(1+Q*X))
    zero((zw-1/P)/(zw-P)-(P+X)/(1+P*X))
    assert any(s.cancel(x)!=0 for x in T*B-A*T), 'wrong puncture inverse unexpectedly accepted'


def white(E,R):
    return [s.Matrix([[1,0],[0,E]]),s.Matrix([[1,E-1],[0,E]]),
            s.Matrix([[E-R,R*(1-E)],[E-1,1-E*R]]),
            s.Matrix([[R,0],[1-E,E*R]])]


def coords(E,R):
    return [s.Matrix([[0,E*R],[E-1,0]]),s.Matrix([[-1,0],[0,E-1]]),
            s.Matrix([[0,-E*(R-1)],[E-1,-(E-1)]]),
            s.Matrix([[0,-R*(R-1)],[E-1,-R*(E-1)]])]


def cusp_checks():
    E,R=s.symbols('E R',nonzero=True)
    W=white(E,R); xi=coords(E,R)
    for j in range(4):
        mu=W[(j-1)%4].inv()*W[j]
        if j%2: mu=mu.inv()
        affine(xi[j]*mu*xi[j].inv(),1,1)
    turn=s.Matrix([[0,R-1],[1,-1]])
    xt=coords(1/E,1-R)
    for j,shift in enumerate([E*R/(E-1),-1/(E-1),0,R/(E-1)]):
        affine(xt[(j-1)%4]*turn*xi[j].inv(),-1,shift)
    close=s.Matrix([[1,-R],[1,-1]])
    xc=coords(1/E,R)
    for j,shift in enumerate([R/(E-1),-E/(E-1),-1/(E-1),E*R/(E-1)]):
        affine(xi[3-j]*close*xc[j].inv(),1,shift)
    pure=s.Matrix([[0,-E*R],[1,-1-E]])
    oddA=s.Matrix([[R,-R],[1,E*R-1-E]])
    oddB=s.Matrix([[R/E-1-1/E,R],[-1,R]])
    affine(xi[0]*pure*xi[1].inv(),1,(E+1)/(E-1))
    affine(xi[3]*pure*xi[2].inv(),1,(R-1)/(E-1))
    plus=[W[1].inv()*oddB,W[2].inv()*oddA]
    minus=[W[2].inv()*oddB,W[3].inv()*oddA]
    for paths,shifts in [(plus,[E/(E-1),(R-E-1)/(E-1)]),
                          (minus,[1/(E-1),(R-2)/(E-1)])]:
        for (a,b),path,shift in zip([(0,2),(1,3)],paths,shifts):
            affine(xi[b]*path*xi[a].inv(),-1,shift)
    mp=W[0].inv()*oddB; mm=oddA.inv()*W[0]
    mu0=W[3].inv()*W[0]; mu1=(W[0].inv()*W[1]).inv()
    projective(plus[0],mu1*mp);projective(plus[1],mp.inv())
    projective(minus[0],mm);projective(minus[1],mu0*mm.inv())
    P=lambda e,r:(e+r)/(e-1)
    zero((E*R-R+1)/(E-1)-P(1/E,1-R)+P(E,R)-2*(E+1)/(E-1))
    zero(P(E,R)+P(1/E,R)-(1-R))
    bare=W[1].inv()*W[3]/R
    zero(bare.det()-1)
    zero(s.trace(bare)-(2+(E+1/E-2)/R))
    # A missing endpoint orientation would give a different odd displacement.
    assert s.cancel(E/(E-1)+(R-E-1)/(E-1)-((R-E-2)/(E-1)-1)) != 0
    return E,R


def prism_checks():
    a,b,c=s.symbols('a b c',nonzero=True)
    Pstar=1+a-a*(a*b*(1+c)-1-a)/(a*a*b*b*c-a)
    RF=a*(b-1)*(b*c-1)/((a*b-1)*(a*b*c-1))
    RG=c*(b-1)*(a*b-1)/((b*c-1)*(a*b*c-1))
    RO=(b-1)*(a*b*c-1)/((a*b-1)*(b*c-1))
    norm=lambda q0,q1,q2:s.Matrix([[q2-q1,-q0*(q2-q1)],[q2-q0,-q1*(q2-q0)]])
    NF=norm(1,a,Pstar);NG=s.Matrix([[0,a*b-Pstar],[1,-Pstar]])
    NO=norm(1,a,a*b)
    XF=[(m*NF).applyfunc(s.cancel) for m in coords(b*c,RF)]
    XG=[(m*NG).applyfunc(s.cancel) for m in coords(a*b,RG)]
    XO=[(m*NO).applyfunc(s.cancel) for m in coords(a*b*c,RO)]
    shifts=[b*c/(b*c-1),-a*(b-1)/((a*b-1)*(a*b*c-1)),0,0,
            a*b*(c-1)/((a*b-1)*(a*b*c-1)),
            (b-1)*(c-1)/((a*b-1)*(b*c-1)*(a*b*c-1))]
    for end,start,shift in zip([XG[1],XG[0],XO[0],XO[1],XO[2],XO[3]],
                               [XF[2],XF[3],XF[0],XF[1],XG[2],XG[3]],shifts):
        affine(end*start.inv(),1,shift)
    P=lambda e,r:(e+r)/(e-1)
    zero(-shifts[0]+shifts[1]-shifts[4]+shifts[5]-(P(a*b*c,RO)-P(b*c,RF)-P(a*b,RG)))


def framing_checks():
    p,eps,o=s.symbols('p eps o')
    n=eps-2*p
    zero(-o*eps-eps+2*p*(1+o)-(-o*n-n))
    cases=[]
    for p0 in range(-3,4):
        for o0 in (-1,1):
            ell2=2*(1+o0)
            assert ell2 in (0,4)
            for eps0 in (-1,0,1):
                assert (-o0*eps0-eps0+p0*ell2)==-(1+o0)*(eps0-2*p0)
                assert (p0*ell2)%2==0
                cases.append((p0,o0,eps0))
    wrong=-o*eps-eps-2*p*(1+o)-(-o*n-n)
    assert wrong.subs({p:1,o:1,eps:1}) != 0, 'wrong surgery sign control failed'
    return len(cases)


def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=HERE/'build'/'check.json')
    args=parser.parse_args();args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.unlink(missing_ok=True)
    if not __debug__: raise SystemExit('Assertions must be enabled; do not use -O or -OO.')
    global s
    import sympy as s
    sources=sorted(HERE.glob('*.tex'))+sorted((HERE/'figures').glob('*.tex'))+[Path(__file__).resolve(),HERE/'README.md']
    before={str(p.relative_to(ROOT)):digest(p) for p in sources}
    data=edge_checks();character_checks(data);cusp_checks();prism_checks();finite=framing_checks()
    assert before=={str(p.relative_to(ROOT)):digest(p) for p in sources},'Source changed during check'
    result={'success':True,'exact_rational_equalities':COUNT,'integer_framing_cases':finite,
            'negative_controls':4,'source_sha256':before,'sympy_version':s.__version__,
            'scope':'Exact rational identities and bounded integer framing compatibility; no finite evidence substituted for the written topology, constant-field, all-fiber, spin, or stationary proofs.'}
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:result[k] for k in ('success','exact_rational_equalities','integer_framing_cases','negative_controls')}))


if __name__=='__main__': main()
