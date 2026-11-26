"""Three fixed interval inequalities; no uniform geometric theorem is tested."""
from pathlib import Path
import json, hashlib
from flint import arb, ctx

ctx.prec=192
terms=2048
pi=arb.pi()
def lam(x):
    value=sum(((2*k*x).sin()/(2*k*k) for k in range(1,terms+1)),arb(0))
    return value+arb(0,arb(1)/(2*terms))
def f(num,den):
    a=arb(num)/den
    return (lam(pi*a)+lam(pi*(arb(1)/2-a)))/pi
g=f(1,4)
b1=5+4*arb(2).sqrt()
b2=14+8*arb(2).sqrt()
values={
 "unchanged_protected_caps":2*g-arb(3)/4*arb(2).log(),
 "root_region":2*f(1,12)+f(1,3)+2*f(1,5)+f(1,10)
                 +arb(17)/30*arb(2).log()-arb(2)/3*b1.log(),
 "all_internal_regions":4*g-(b2**3/(2*b1*b1)).log()/4,
}
bounds={"unchanged_protected_caps":"0.06","root_region":"0.25","all_internal_regions":"0.09"}
for k,v in values.items():
    assert v>arb(bounds[k]),(k,v)
out={
 "precision_bits":ctx.prec,"fourier_terms":terms,
 "lobachevsky_tail_radius":"1/(2*terms)",
 "inequalities":{k:{"lower":str(v.lower()),"upper":str(v.upper()),
                    "strict_rational_lower_bound":bounds[k]} for k,v in values.items()},
 "scope":"Only the three fixed constants in the private thin-face derivation. All-chain matching, topology, source estimates and volume identification require the written proof.",
}
p=Path("/private/tmp/md-thin-face-zigzag-constant-results.json")
p.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
