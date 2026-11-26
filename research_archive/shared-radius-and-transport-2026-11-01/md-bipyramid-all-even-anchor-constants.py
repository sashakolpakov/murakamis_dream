"""Fixed constants in the symbolic all-even-size shared-radius proof.

Only rigorous ball evaluations of finitely many specified expressions;
there is no diagram-size loop, nonlinear solve, or floating optimizer.
"""
import json
from pathlib import Path
from fractions import Fraction
from flint import arb,ctx
ctx.prec=192
TERMS=8192
def rat(a,b=1): return arb(a)/b
def lob(t):
    out=arb(0)
    for n in range(1,TERMS+1):out+=(2*n*t).sin()/(2*n*n)
    return out+arb(0,rat(1,2*TERMS))
_cache={}
def Q(*ww):
    key=tuple(sorted(str(x) for x in ww))
    if key in _cache:return _cache[key]
    w=list(ww);p=[x for x in w if not x.is_zero()]
    if len(p)==1:return p[0].log()/2
    D=(w[0]*w[1]+w[1]*w[2]+w[2]*w[0]).sqrt()
    ans=arb(0)
    for x in p:
        t=(x/D).atan()
        ans+=(lob(t)+lob(arb.pi()/2-t)+t*x.log())/arb.pi()
    _cache[key]=ans
    return ans
def F(r):return Q(arb(1),r,arb(0))
a=rat(9,4);C=rat(27,4)
D=rat(16,9)-1+rat(9,16).log()
cap=F(a)-a.log()
near1=F(a)+Q(arb(1),C,a)-C.log()
near2=Q(arb(1),C,a)-C.log()/2
interior1=F(rat(1,3))+F(arb(2))-arb(2).log()
interior2=F(arb(2))-arb(2).log()/2
changed_neighbor=F(rat(4,27))+F(arb(2))-arb(2).log()
change=2*(F(arb(1))-F(a)+Q(arb(1),arb(1),C)-Q(arb(1),a,C))+a.log()
penalty=C.log()-F(arb(1))-Q(arb(1),arb(1),C)
assert penalty>0
saving=F(arb(1))-change-penalty
assert D<rat(203,1000)
assert cap>0
assert near1>rat(28,100) and near2>rat(42,100)
assert interior1>rat(43,100) and interior2>rat(42,100)
assert changed_neighbor>rat(32,100)
assert saving>rat(37,100)
assert near1-D>rat(7,100)
assert near2-D>rat(7,100)
assert interior1-D>rat(7,100)
assert interior2-D>rat(7,100)
assert saving-D>rat(16,100)
out={k:{'ball':str(v),'lower':str(v.lower()),'upper':str(v.upper())} for k,v in locals().copy().items() if k in [
'D','cap','near1','near2','interior1','interior2','changed_neighbor',
'change','penalty','saving']}
out.update(precision_bits=ctx.prec,lobachevsky_terms=TERMS,
           proved_uniform_anchor_margin='7/100',
           scope='Fixed constants only; arbitrary even m is covered by the symbolic trigonometric and derivative proof.')
Path('/private/tmp/md-bipyramid-all-even-anchor-constants.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
