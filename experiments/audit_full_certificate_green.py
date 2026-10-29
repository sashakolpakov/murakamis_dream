#!/usr/bin/env python3
"""Universal polynomial checks of the full-certificate Green identity.

The array values f(k+v) are algebraically independent symbols, so these
are exact Ore-module checks, with no choice of a knot or finite level.
"""

import itertools
import json
import math
from pathlib import Path

import sympy as s


def clean(module):
    return {v:s.expand(c) for v,c in module.items() if s.expand(c)!=0}


def add(a,b,scale=1):
    out=dict(a)
    for v,c in b.items():out[v]=out.get(v,0)+scale*c
    return clean(out)


def multiply(module,p):return clean({v:c*p for v,c in module.items()})


def delta(module,i,k):
    shifted={}
    for v,c in module.items():
        w=list(v);w[i]+=1;w=tuple(w)
        coefficient=c.subs(k[i],k[i]+1) if hasattr(c,'subs') else c
        shifted[w]=shifted.get(w,0)+coefficient
    return add(shifted,module,-1)


def dword(word,k):
    out={tuple(0 for _ in k):s.Integer(1)}
    for i in reversed(word):out=delta(out,i,k)
    return out


def check(alpha,beta):
    d=len(alpha)
    k=s.symbols(f'k0:{d}')
    p=s.Integer(1)
    for i,a in enumerate(alpha):
        p*=s.prod(k[i]-r for r in range(a))/math.factorial(a)
    p=s.expand(p)
    word=tuple(i for i,b in enumerate(beta) for _ in range(b))
    current={}
    residual=p
    for j,i in enumerate(word):
        h=residual.subs(k[i],k[i]-1)
        term=multiply(dword(word[j+1:],k),h)
        current=add(current,delta(term,i,k))
        residual=s.expand(h-residual)
    rhs=add(current,{tuple(0 for _ in k):residual})
    lhs=multiply(dword(word,k),p)
    assert not add(lhs,rhs,-1),(alpha,beta)
    if sum(beta)>=sum(alpha):
        expected=(-1)**sum(alpha) if beta==alpha else 0
        assert s.expand(residual-expected)==0,(alpha,beta,residual)


def main():
    records=[]
    for alpha in ((1,),(2,),(1,1),(2,1),(1,1,1)):
        h=sum(alpha)
        count=0
        for beta in itertools.product(range(h+2),repeat=len(alpha)):
            if sum(beta)>h+1:continue
            check(alpha,beta)
            count+=1
        records.append({'moment_multiindex':alpha,'universal_shift_checks':count})
    result={'green_certificate':records,
            'scope':'Pointwise universal Green identities; no final framing-boundary cancellation inferred.'}
    out=Path(__file__).with_name('full_certificate_green_results.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'universal_checks':sum(r['universal_shift_checks'] for r in records),
                      'output':str(out)},indent=2))


if __name__=='__main__':main()
