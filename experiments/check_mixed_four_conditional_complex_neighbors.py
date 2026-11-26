#!/usr/bin/env python3
"""Exact full-sum continuation and outward revived-row rate margins."""
import argparse,json
from hashlib import sha256
from pathlib import Path
from flint import arb,acb,ctx
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]

def digest(p):return sha256(p.read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision',type=int,default=256)
    ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-four-conditional-complex-neighbors.json')
    args=ap.parse_args();ctx.prec=args.precision
    records=[]
    for name in ['research-mixed-four-conditional-packet.json',
                 'research-mixed-four-conditional-packet-replay.json']:
        p=ROOT/'repro/results'/name;data=json.loads(p.read_text())
        assert data['status']=='passed'
        for f,h in data['dependencies_sha256'].items():assert digest(ROOT/f)==h,f
        script='experiments/'+('replay_' if 'replay' in name else 'certify_')+'mixed_four_conditional_packet.py'
        assert digest(ROOT/script)==data['script_sha256'],script
        records.append({'path':str(p.relative_to(ROOT)),'sha256':digest(p)})
    pi,ii=arb.pi(),acb(0,1)
    def J(x):
        z=acb(x)
        return (((-2*pi*ii*z).exp().polylog(2)-pi*pi/6)/(2*pi*ii)-ii*pi*z*(1-z)/2).real
    comparisons=[]
    def positive(name,v):
        assert v>0,(name,str(v));comparisons.append({'name':name,'margin':str(v)})
    positive('maximum periodic numerator entropy below1/6',arb(1)/6-J(arb(5)/6))
    positive('whole real critical action above1/5',
             2*J(arb(3)/10)-3*J(arb(1)/10)+arb(1)/50-arb(1)/5)
    positive('common revived-row reserve',arb(1)/5-arb(1)/6-arb(1)/31)
    field=sp.QQ.algebraic_field(sp.I,sp.sqrt(2),sp.sqrt(3))
    one,zero=field.one,field.zero
    cv=lambda z:field.from_sympy(sp.sympify(z))
    def prod(xs):
        out=one
        for x in xs:out*=x
        return out
    exact=[]
    def check(name,z):
        assert z==zero,(name,field.to_sympy(z));exact.append(name)
    for N,qq in [(2,sp.I),(3,(1+sp.I*sp.sqrt(3))/2),
                 (4,(1+sp.I)/sp.sqrt(2)),(6,(sp.sqrt(3)+sp.I)/2)]:
        r=cv(qq)**-2
        P=[prod(1-r**h for h in range(1,j+1))for j in range(N)]
        for a in range(N):
            for b in range(N):
                total=zero;original=zero
                for i in range(N):
                    continued=r**(-a*i)*P[a]*P[b]*prod(1-r**(a+h)for h in range(1,i+1))*prod(1-r**(b+h)for h in range(1,i+1))/P[i]**3
                    target=r**(-a*i)*P[i+a]*P[i+b]/P[i]**3 if i+max(a,b)<N else zero
                    check(f'N{N} full term and support a{a} b{b} i{i}',continued-target)
                    total+=continued;original+=target
                check(f'N{N} entire conditional a{a} b{b}',total-original)
    deps=['notes/research_mixed_four_conditional_complex_neighbors.md',
          'notes/research_mixed_four_conditional_packet.md',
          'notes/research_mixed_conditional_leg_sum.md',
          'notes/exact_factorial_interpolation_and_complex_contours.md',
          'experiments/certify_mixed_four_conditional_packet.py',
          'experiments/replay_mixed_four_conditional_packet.py',
          'repro/results/research-mixed-four-conditional-packet.json',
          'repro/results/research-mixed-four-conditional-packet-replay.json']
    result={'status':'passed','precision_bits':args.precision,
            'strict_comparison_count':len(comparisons),'comparisons':comparisons,
            'exact_identity_count':len(exact),'exact_identities':exact,
            'levels':[2,3,4,6],'inherited_physical_packet':records,
            'scope':'Canonical full N-term continuation, exact physical support zeros, and scalar entropy margins. The proof supplies uniform complex tail control and the full conditional packet, not a remaining mixed-word coefficient.',
            'script_sha256':digest(Path(__file__)),
            'dependencies_sha256':{p:digest(ROOT/p)for p in deps}}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k]for k in ['status','strict_comparison_count','exact_identity_count']}))

if __name__=='__main__':main()
