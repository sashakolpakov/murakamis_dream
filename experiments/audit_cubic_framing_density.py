#!/usr/bin/env python3
"""Full 5_2 determinant-line calibration in Q[t](s,r), t^3+t^2+2t+1=0.

No sampling/interpolation: retain both framing coordinates in FLINT
polynomial arithmetic, independently compute the holonomy torsion,
and compare with the unchanged actual Gaussian coefficient model.
"""

from itertools import combinations
import json
from pathlib import Path

import sympy as sp
from flint import fmpq_mpoly_ctx

from audit_actual_normal_stationary_period import (
    exact_field_determinant, inverse, matmul, symbolic_framing_density)


CTX=fmpq_mpoly_ctx.get(('s','r'))
PZERO,PONE=CTX.constant(0),CTX.constant(1)


class CubicFraction:
    """(a+b t+c t^2)/d in Q(s,r)[t]/(t^3+t^2+2t+1)."""

    def __init__(self,a=PZERO,b=PZERO,c=PZERO,d=PONE):
        if not d:raise ZeroDivisionError
        if not a and not b and not c:
            self.a,self.b,self.c,self.d=PZERO,PZERO,PZERO,PONE
            return
        common=a.gcd(b).gcd(c).gcd(d)
        if not common.is_one():a,b,c,d=(v/common for v in (a,b,c,d))
        leading=d.leading_coefficient()
        self.a,self.b,self.c,self.d=(v/leading for v in (a,b,c,d))

    @staticmethod
    def coerce(x):
        return x if isinstance(x,CubicFraction) else CubicFraction(CTX.constant(x))

    def __bool__(self):return bool(self.a) or bool(self.b) or bool(self.c)
    def __neg__(self):return CubicFraction(-self.a,-self.b,-self.c,self.d)
    def __add__(self,x):
        x=self.coerce(x)
        return CubicFraction(self.a*x.d+x.a*self.d,self.b*x.d+x.b*self.d,
                             self.c*x.d+x.c*self.d,self.d*x.d)
    __radd__=__add__
    def __sub__(self,x):return self+-self.coerce(x)
    def __rsub__(self,x):return self.coerce(x)+-self
    def __mul__(self,x):
        x=self.coerce(x)
        z0=self.a*x.a;z1=self.a*x.b+self.b*x.a
        z2=self.a*x.c+self.b*x.b+self.c*x.a
        z3=self.b*x.c+self.c*x.b;z4=self.c*x.c
        return CubicFraction(z0-z3+z4,z1-2*z3+z4,z2-z3-z4,self.d*x.d)
    __rmul__=__mul__
    def inverse(self):
        a,b,c=self.a,self.b,self.c
        M=[[a,-c,-b+c],[b,a-2*c,-2*b+c],[c,b-c,a-b-c]]
        cof=[M[1][1]*M[2][2]-M[1][2]*M[2][1],
             M[1][2]*M[2][0]-M[1][0]*M[2][2],
             M[1][0]*M[2][1]-M[1][1]*M[2][0]]
        det=sum(M[0][j]*cof[j] for j in range(3))
        return CubicFraction(*(self.d*v for v in cof),det)
    def __truediv__(self,x):return self*self.coerce(x).inverse()
    def __rtruediv__(self,x):return self.coerce(x)/self
    def __pow__(self,n):
        n=int(n)
        if n<0:return self.inverse()**(-n)
        value,base=self.coerce(1),self
        while n:
            if n&1:value*=base
            n>>=1
            if n:base*=base
        return value


class CubicField:
    def __init__(self):
        self.zero=CubicFraction();self.one=CubicFraction(PONE)
        self.theta=CubicFraction(PZERO,PONE)
        self.gens=tuple(CubicFraction(g) for g in CTX.gens())
    def convert(self,value):return CubicFraction.coerce(value)
    def to_sympy(self,value):
        value=self.convert(value);s,r,t=sp.symbols('s r t');symbols={'s':s,'r':r}
        poly=lambda v:sp.sympify(str(v).replace('^','**'),locals=symbols)
        return (poly(value.a)+t*poly(value.b)+t*t*poly(value.c))/poly(value.d)


def mm(a,b):return matmul(a,b)
def madd(a,b):return tuple(x+y for x,y in zip(a,b))
def msub(a,b):return tuple(x-y for x,y in zip(a,b))
def mneg(a):return tuple(-x for x in a)


def holonomy_torsion(field,raw,word):
    z,o=field.zero,field.one;det=lambda M:exact_field_determinant(M,o,z)
    F=tuple(field.convert(v) for v in (2,-1,3,-3))
    initial=[mneg(mm(mm(inverse(F),mu),F)) for mu in raw]
    n=2*len(initial);eye=[[o if i==j else z for j in range(n)] for i in range(n)]
    variations=[]
    for j,H in enumerate(initial):
        K,e=H[0],H[1];trace=H[0]+H[3]
        basis=[(o,z,(trace-2*K)/e,-o),(z,o,-H[2]/e,z)]
        variations.append([basis[k-2*j] if k in (2*j,2*j+1) else (z,z,z,z) for k in range(n)])
    original=[list(v) for v in variations];moved=list(initial)
    for j,sign in word:
        a,b=moved[j:j+2];da,db=variations[j:j+2]
        if sign>0:
            ai=inverse(a);c=mm(mm(ai,b),a)
            dc=[madd(madd(mneg(mm(mm(ai,v),c)),mm(mm(ai,w),a)),mm(mm(ai,b),v)) for v,w in zip(da,db)]
            moved[j:j+2],variations[j:j+2]=[c,a],[dc,da]
        else:
            bi=inverse(b);c=mm(mm(b,a),bi)
            dc=[msub(madd(mm(mm(w,a),bi),mm(mm(b,v),bi)),mm(mm(c,w),bi)) for v,w in zip(da,db)]
            moved[j:j+2],variations[j:j+2]=[b,c],[db,dc]
    assert all(not(x-y) for a,b in zip(initial,moved) for x,y in zip(a,b))
    D=[[variations[j][k][i]-eye[2*j+i][k] for k in range(n)] for j in range(len(initial)) for i in (0,1)]
    lie=[(o,z,z,-o),(z,o,z,z),(z,z,o,z)]
    a=[[msub(mm(xi,H),mm(H,xi))[i] for xi in lie] for H in initial for i in (0,1)]
    P=(o,z,z,o);dP=[(z,z,z,z) for _ in range(n)]
    for H,var in zip(initial,original):
        dP=[madd(mm(v,P),mm(H,w)) for v,w in zip(var,dP)];P=mm(H,P)
    trivial=[mm(v,inverse(P)) for v in dP]
    m=[[v[i] for v in trivial] for i in (0,1,2)]
    assert all(not sum(D[i][j]*a[j][k] for j in range(n)) for i in range(n) for k in range(3))
    assert all(not sum(m[i][j]*D[j][k] for j in range(n)) for i in range(3) for k in range(n))
    complement=next(cols for cols in combinations(range(n),n-3)
                    if det([a[i]+[eye[i][j] for j in cols] for i in range(n)]))
    V=[[eye[i][j] for j in complement] for i in range(n)]
    pivots=next(cols for cols in combinations(range(n),3) if det([[m[i][j] for j in cols] for i in range(3)]))
    block=[[m[i][j] for j in pivots] for i in range(3)];db=det(block)
    bi=[[(-o if (i+j)%2 else o)*det([[block[k][l] for l in range(3) if l!=i] for k in range(3) if k!=j])/db
         for j in range(3)] for i in range(3)]
    W=[[z for _ in range(3)] for _ in range(n)]
    for i,j in enumerate(pivots):W[j]=bi[i]
    assert all(not(sum(m[i][k]*W[k][j] for k in range(n))-(o if i==j else z)) for i in range(3) for j in range(3))
    source=[a[i]+V[i] for i in range(n)]
    target=[[sum(D[i][k]*V[k][j] for k in range(n)) for j in range(n-3)]+W[i] for i in range(n)]
    return det(source)/det(target)


def main():
    field=CubicField();o,z,t=field.one,field.zero,field.theta;s=field.gens[0]
    assert not t**3+t*t+2*t+1
    test=(field.gens[1]+t*s)/(s-t*t)
    assert not test*test.inverse()-1
    A=(o,o,z,o);B=(o,z,t,o)
    D=mm(mm(inverse(A),B),A);E=mm(mm(inverse(D),A),D)
    C=mm(mm(E,A),inverse(E));raw=[A,B,C]
    word=[(0,1),(0,1),(0,1),(1,1),(0,-1),(1,1)]
    torsion=holonomy_torsion(field,raw,word)
    assert not (-torsion/2)*(t*t+2)*(3*t*t+2*t+2)-1
    expected=-torsion/(2*s*s*(s+o)**2)
    data={'meridians':raw,'word':word,'expected_density':expected,
          'field_label':'Q[t]/(t^3+t^2+2t+1)(s,r)'}
    result=symbolic_framing_density(None,exact_field=field,holonomy_data=data)
    result['intrinsic_holonomy_torsion']=str(sp.factor(field.to_sympy(torsion)))
    result['density_to_torsion_and_cut_form_ratio']='-1/2'
    result['Riley_residue_weight']='1/((t^2+2)*(3*t^2+2*t+2))'
    result['arithmetic']='FLINT exact cubic fraction field; both framing variables retained; no interpolation'
    result['scope']='5_2 principal determinant-line identity; selected global Kashaev volume theorem not asserted'
    from audit_full_framing_density import ExactQuadraticField
    quadratic=ExactQuadraticField();oq,zq=quadratic.one,quadratic.zero
    tq=(oq-quadratic.radical)/2;sq=quadratic.gens[0]
    Aq=(oq,oq,zq,oq);Bq=(oq,zq,tq,oq)
    Cq=mm(mm(mm(mm(inverse(Aq),Bq),Aq),inverse(Bq)),Aq)
    rawq=[Aq,Bq,Cq];wordq=[(0,1),(1,-1),(0,1),(1,-1)]
    torsionq=holonomy_torsion(quadratic,rawq,wordq)
    assert not (-torsionq/2)*(-oq)*(2*tq-oq)-1
    dataq={'meridians':rawq,'word':wordq,'expected_density':-torsionq/(2*sq*sq*(sq+oq)**2),
           'field_label':'Q(sqrt(-3))(s,r)'}
    result['figure_eight_exact_comparison']=symbolic_framing_density(None,exact_field=quadratic,holonomy_data=dataq)
    result['figure_eight_exact_comparison']['intrinsic_holonomy_torsion']=str(sp.simplify(quadratic.to_sympy(torsionq)))
    result['figure_eight_exact_comparison']['Riley_residue_weight']='-1/(2*t-1), t^2-t+1=0'
    path=Path(__file__).with_name('cubic_framing_density_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)


if __name__=='__main__':main()
