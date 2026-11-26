#!/usr/bin/env python3
"""Independent integer N=3 source check; no general cancellation theorem."""
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path


def source(spectra):
    m=len(spectra);zero=(0,)*m;one={zero:1}
    def add(a,b):
        out=dict(a)
        for k,v in b.items():out[k]=out.get(k,0)+v
        return {k:v for k,v in out.items() if v}
    def scale(a,c):return {k:v*c for k,v in a.items() if v*c}
    def mul(a,b):
        out=defaultdict(int)
        for ka,va in a.items():
            for kb,vb in b.items():
                k=tuple(x+y for x,y in zip(ka,kb))
                if max(k)<=2:out[k]+=va*vb
        return {k:v for k,v in out.items() if v}
    def var(k):
        a=[0]*m;a[k]=1;return {tuple(a):1}
    def rim(k):return var(k%m) if k%m else {}
    result=one
    for j,sigma in enumerate(spectra):
        x={} if j%2 else var(0);y=rim(j)
        b,c=(rim(j-1),rim(j+1)) if j%2 else (rim(j+1),rim(j-1))
        if sigma is None:
            H=add(add(mul(b,b),mul(b,c)),mul(c,c))
        else:
            # chi_3(z)=z^3-3z+2. Direct C^2+sigma*C+(sigma^2-3)I,
            # C diagonal (1,-2,1), first band -3(x+y), second -3xy.
            outer=add(x,y)
            H=scale(add(mul(b,b),mul(c,c)),(sigma-1)*(sigma+2))
            H=add(H,scale(mul(b,c),(sigma-1)**2))
            H=add(H,scale(mul(outer,add(b,c)),-3*(sigma-1)))
            H=add(H,scale(mul(outer,outer),9))
            H=add(H,scale(mul(x,y),-3*(sigma+2)))
        result=mul(result,H)
    return result.get((2,)*m,0)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,default=Path(__file__).with_suffix('.json'))
    args=ap.parse_args()
    spectra=[2,0,2,2,2,2]
    full=source(spectra)
    identities=[];second_differences=[]
    for j in (1,2):
        vals=spectra.copy();vals[j]=None;identities.append(source(vals))
        samples=[]
        for sigma in (-1,0,1):
            vals=spectra.copy();vals[j]=sigma;samples.append(source(vals))
        second=(samples[0]-2*samples[1]+samples[2])//2
        assert second==identities[-1]
        second_differences.append(dict(position=j,samples=samples,identity_coupon=second))
    all_plus=source([2]*6)
    current=-2*full-2*identities[0]+4*identities[1]
    assert (full,*identities,all_plus,current)==(910845,115587,243,2049705,-2051892)
    data=dict(status='exact_integer_checks_passed',N=3,equator_size=6,
              spectra=spectra,full_source=full,identity_at_1=identities[0],identity_at_2=identities[1],
              all_plus_source=all_plus,sewn_current=current,identity_second_differences=second_differences,
              script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              source='Original homogeneous 3x3 Casimir polynomial and shared S^2 z1^2 ... z5^2 coefficient; protected north=z0=0.',
              scope='Finite nonzero sewn-current identity only; no conclusion about the full-minus-CROSS spectral gap.')
    args.output.write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data,indent=2))


if __name__=='__main__':main()
