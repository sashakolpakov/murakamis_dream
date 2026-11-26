#!/usr/bin/env python3
"""Conditional outside-deficit transport: exact algebra and scalar reserves.

The initial real outside-color bound is not proved by this checker.
All norm-to-action comparisons retain the actual complete critical drift.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import sympy as sp
from flint import arb, ctx

ROOT=Path(__file__).resolve().parents[1]


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision',type=int,default=192)
    ap.add_argument('--output',type=Path,
                    default=ROOT/'repro/results/research-three-outside-deficit-transport.json')
    args=ap.parse_args();ctx.prec=args.precision

    def a(value):
        value=Q(value);return arb(value.numerator)/value.denominator

    sq=arb(21).sqrt();K=4*arb.pi()/sq;rho=(5-sq)/2;D=5+sq
    Z=a('1.05')*rho/(1-a('.3')*rho)
    H,A,aa=map(a,['.0057','1.45','1.5'])
    C0=K*(D+a('.6'))/(2*(D-a('.6'))**2)
    Ccl=K*(2*sq+a('.36'))/(2*(2*sq-a('.36'))**2)
    cost=lambda h:K*K*h*h/(4*(A+aa))
    drift=C0*H*H/(1-Z*Z);Einfty=cost(H)+drift
    H1,H2=Z*H,Z*Z*H
    one2=Einfty+cost(H2)+4*Ccl*H2*H2
    both2=2*Einfty+4*Ccl*H2*H2
    zero=K*K*(2*H)**2/(8*A)+Ccl*(2*H)**2
    mixed_one0=K*K*(H+H1)**2/(8*A)+Ccl*(H+H1)**2
    mixed_one1=Einfty+cost(H)+Ccl*(H+H1)**2
    positive_both=2*Einfty+4*Ccl*H1*H1
    positive_one=Einfty+cost(H1)+4*Ccl*H1*H1
    checks=[]

    def positive(name,value):
        assert value>0,(name,str(value))
        checks.append({'name':name,'strict_positive_margin':str(value)})

    positive('Z is positive',Z)
    positive('Z is below one',1-Z)
    positive('closing analytic critical disk radius below .0013',a('.0013')-2*H/(2*sq-a('.36')))
    positive('closing derivative is a contraction',1-a('.36')/(2*sq))
    positive('two attachments enter the small closing class',a('.0004')-H2)
    positive('one smoothing plus all drift below .000026652',a('.000026652')-Einfty)
    positive('one outside end after two attachments costs below .000027',a('.000027')-one2)
    positive('two outside ends after two attachments cost below .000054',a('.000054')-both2)
    positive('two unsmoothed ends cost below .000107',a('.000107')-zero)
    for name,value in [('unsmoothed outside and smoothed complete',mixed_one0),
                       ('smoothed outside and unsmoothed complete or outside',mixed_one1),
                       ('two smoothed outside ends',positive_both),
                       ('smoothed outside and smoothed complete',positive_one)]:
        positive(name+' costs below .000056',a('.000056')-value)
    positive('ordinary corner reserve remains above .05',a(Q(31,600))-a('.05'))

    z,h,k,c,A0,a0=sp.symbols('z h k c A a',positive=True)
    j=sp.symbols('j',integer=True,nonnegative=True)
    q=k*k*h*h/(4*(A0+a0))
    ej=q+c*h*h*(1-z**(2*j))/(1-z*z)
    einf=q+c*h*h/(1-z*z)
    assert sp.simplify(einf-ej-c*h*h*z**(2*j)/(1-z*z))==0
    identities=['exact remaining geometric-series drift after j attachments']
    v=sp.symbols('v',real=True)
    assert sp.simplify(k*h*v-(A0+a0)*v*v-q+(A0+a0)*(v-k*h/(2*(A0+a0)))**2)==0
    identities.append('single first-attachment square completion')
    ell1,ell2,B1,B2=sp.symbols('ell1 ell2 B1 B2',positive=True)
    assert sp.simplify((ell1+ell2)*v-(B1+B2)*v*v-(ell1+ell2)**2/(4*(B1+B2))
                     +(B1+B2)*(v-(ell1+ell2)/(2*(B1+B2)))**2)==0
    identities.append('general bilinear closing square completion')
    n=sp.symbols('n',integer=True,positive=True)
    jj,kk=sp.symbols('j k',integer=True,nonnegative=True)
    MM,TT=sp.MatrixSymbol('A',n,n),sp.MatrixSymbol('T',n,n)
    word=(MM**3*TT**jj*(MM**3*TT**kk).T).doit().xreplace({MM.T:MM,TT.T:TT}).doit()
    assert word==MM**3*TT**(jj+kk)*MM**3
    identities.append('original bilinear right-word reversal')
    assert Q(3,25)+Q(1,15)-Q(27,200)==Q(31,600)
    identities.append('ordinary full-word corner reserve31/600')
    deps=[
        'notes/research_three_outside_deficit_transport.md',
        'notes/research_three_larger_source_propagation.md',
        'notes/research_three_first_entrance_real_extension.md',
        'notes/research_three_vertex_two_wire_large_cap_bound.md',
        'notes/research_three_small_source_closure.md',
        'notes/research_three_larger_source_closure.md',
        'notes/research_three_chain_fourier_corner_transfer.md',
    ]
    result={'status':'passed','precision_bits':args.precision,
            'strict_scalar_comparisons':len(checks),'comparisons':checks,
            'exact_identities':identities,
            'first_smoothing_cost':str(cost(H)),'total_complete_action_drift':str(drift),
            'uniform_per_end_reserve':str(Einfty),
            'one_end_reserve_after_two_attachments':str(one2),
            'two_end_reserve_after_two_attachments':str(both2),
            'unsmoothed_closing_reserve':str(zero),
            'mixed_closing_reserve':str(mixed_one1),
            'scope':'Conditional real outside-color upper transport only. The initial outside bound and its normal estimates are hypotheses. No far-color local packet, complex strip, knot identification or initial deficit is certified.',
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest()for p in deps}}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(f'Passed {len(checks)} strict comparisons and {len(identities)} exact identities.')
    print('Uniform per-end reserve:',Einfty)
    print('One/two outside ends after two attachments:',one2,both2)


if __name__=='__main__':main()
