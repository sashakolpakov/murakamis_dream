"""Exact rational certificate for both A2 alias block envelopes.

Input candidate states are rational. No optimizer or floating-point function
is used in verification. Interval endpoints use outward integer rounding.
"""
from fractions import Fraction as F
from pathlib import Path
import json

S=10**40
def floorq(a,b): return a//b
def ceilq(a,b): return -((-a)//b)

class I:
    def __init__(self,lo,hi=None,raw=False):
        if raw:self.lo,self.hi=lo,hi
        else:
            a=F(lo); b=a if hi is None else F(hi)
            self.lo=floorq(a.numerator*S,a.denominator)
            self.hi=ceilq(b.numerator*S,b.denominator)
        assert self.lo<=self.hi
    def __add__(self,o):
        o=iv(o);return I(self.lo+o.lo,self.hi+o.hi,raw=True)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo,raw=True)
    def __sub__(self,o):return self+-iv(o)
    def __rsub__(self,o):return iv(o)+-self
    def __mul__(self,o):
        o=iv(o);v=[a*b for a in [self.lo,self.hi] for b in [o.lo,o.hi]]
        return I(min(v)//S,ceilq(max(v),S),raw=True)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=iv(o);assert o.lo*o.hi>0
        v=[F(a*S,b) for a in [self.lo,self.hi] for b in [o.lo,o.hi]]
        return I(min(v).__floor__(),max(v).__ceil__(),raw=True)
    def __pow__(self,n):
        assert n>=0;out=I(1)
        for _ in range(n):out=out*self
        return out
    def bounds(self):return [str(F(self.lo,S)),str(F(self.hi,S))]

def iv(x):return x if isinstance(x,I) else I(x)
def atan_recip(q,n=40):
    a=sum((F((-1)**j,(2*j+1)*q**(2*j+1)) for j in range(n)),F(0))
    b=F(1,(2*n+1)*q**(2*n+1))
    return I(a-b,a+b)
PI=16*atan_recip(5)-4*atan_recip(239)

def log_core(x):
    z=(x-1)/(x+1);assert z.lo>=0 and z.hi<S//2
    z2=z*z;term=z;out=I(0);n=80
    for j in range(n):
        out+=term/F(2*j+1);term*=z2
    rem=2*term/(F(2*n+1)*(1-z2))
    return 2*out+I(0,rem.hi,raw=True)
LOG2=log_core(I(2))
def logi(x):
    x=iv(x);assert x.lo>0;k=0
    while x.lo<S:x=x*2;k-=1
    while x.lo>=2*S:x=x/2;k+=1
    return log_core(x)+k*LOG2

def sinpi(t):
    t=F(t);assert 0<t<1
    if t>F(1,2):t=1-t
    x=PI*t;x2=x*x;term=x;out=x
    for j in range(1,21):
        term=term*x2/F((2*j)*(2*j+1))
        out+=((-1)**j)*term
    rem=term*x2/F(42*43)
    return out+I(-rem.hi,rem.hi,raw=True)

ZETA={1:PI*PI/6}
for n in range(2,21):
    base=sum((F(1,k**(2*n)) for k in range(1,65)),F(0))
    ZETA[n]=I(base,base+F(1,(2*n-1)*64**(2*n-1)))

JCACHE={}
def J(t):
    t=F(t);assert 0<=t<=1
    if t in JCACHE:return JCACHE[t]
    if t==0 or t==F(1,2) or t==1:out=I(0)
    elif t>F(1,2):out=-J(1-t)
    else:
        out=t*logi(2*PI*t)-t
        for n in range(1,21):out-=ZETA[n]*F(t**(2*n+1),n*(2*n+1))
        rem=F(2*t**43,21*43*(1-t*t))
        out+=I(-rem,0)
    JCACHE[t]=out;return out

def g(x):return J(2*x)-4*J(x)
def k(x):return -2*J(x/2)
def m(v):
    x,y,z=v
    return J(x+y)+J(z)-J(x)-J(y)-J(z-x)-J(z-y)-J(x+y-z)
def grad_m(v):
    x,y,z=v
    ls=lambda t:logi(sinpi(t))
    return [ls(x+y)-ls(x)+ls(z-x)-ls(x+y-z),
            ls(x+y)-ls(y)+ls(z-y)-ls(x+y-z),
            ls(z)-ls(z-x)-ls(z-y)+ls(x+y-z)]
def feasible(v,core=False):
    x,y,z=v
    return 0<x and 0<y and max(x,y)<z<x+y<1 and (not core or F(1,4)<y<F(1,2))
def alias_data(v,n):
    assert feasible(v,n==1)
    x,y,z=v;grad=grad_m(v)
    grad[0]+=-logi(2*sinpi(x/2))
    if n==1:
        val=k(x)+g(y)+m(v)
        grad[1]+=2*(logi(sinpi(F(1,2)-y))-logi(sinpi(y)))
    else:
        val=k(x)+k(y)+m(v)
        grad[1]+=-logi(2*sinpi(y/2))
    return val,grad

VERTICES={
 1:[[0,0,0],[1,0,1],[F(1,2),F(1,2),F(1,2)],[0,F(1,2),F(1,2)],[F(1,2),F(1,2),1]],
 2:[[0,0,0],[1,0,1],[0,1,1],[F(1,2),F(1,2),F(1,2)]]}

def verify(path, output=None):
    data=json.loads(Path(path).read_text());records=[];last=None
    for cell in data['cells']:
        left,right=map(F,cell['lambda_over_log2'])
        assert left<right and (last is None or left==last)
        last=right
        pure=[F(i,data['denominator']) for i in cell['pure']]
        assert feasible(pure) and pure[0]==pure[1] and pure[0]<F(1,2)
        P=g(pure[0])+g(pure[1])+m(pure)
        for n in [1,2]:
            v=[F(i,data['denominator']) for i in cell['alias'][str(n)]]
            B,grad=alias_data(v,n);lower=[]
            for l in [left,right]:
                lam=l*LOG2
                for vertex in VERTICES[n]:
                    U=B+sum((grad[j]*(vertex[j]-v[j]) for j in range(3)),I(0))
                    gap=P-lam*pure[2]-U+lam*vertex[2]
                    lower.append(gap.lo)
            minimum=min(lower)
            assert minimum>S//100,(left,right,n,F(minimum,S))
            records.append({'cell':cell['lambda_over_log2'],'aliases':n,
                            'gap_lower':str(F(minimum,S))})
    assert F(data['cells'][0]['lambda_over_log2'][0])==-2 and last==2
    result={'status':'PASS','exact_rational_arithmetic':True,
            'domain':'lambda in [-2log2,2log2], entire actual A2 product polytope',
            'certified_uniform_gap':'1/100','cells':len(data['cells']),
            'records':records,'minimum_lower':str(F(min(F(r['gap_lower']) for r in records)))}
    assert F(result['minimum_lower'])>F(1,25)
    if output is not None:
        Path(output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))
    return result

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data',type=Path,default=Path(__file__).with_name('conway_two_leaf_block_alias_certificate.json'))
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    verify(args.data,args.output)
