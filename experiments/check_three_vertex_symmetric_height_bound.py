#!/usr/bin/env python3
"""Scalar premises for the full-torus symmetric Fourier-height bound."""

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
from flint import arb, acb, ctx


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision',type=int,default=192)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args();ctx.prec=args.precision
    pi=arb.pi();checks=[]
    def a(q):
        q=Q(q);return arb(q.numerator)/q.denominator
    def positive(name,value):
        assert value>0,(name,value)
        checks.append({'name':name,'positive_margin':str(value)})
    positive('minimum radius above 12/25',(-pi/100).exp()/2-a(Q(12,25)))
    positive('maximum radius below 13/25',a(Q(13,25))-(pi/100).exp()/2)
    positive('lower p endpoint J bound',-a(Q(7,100))-((pi/20).log()-1)/40)
    c=acb(0,pi/3).exp().polylog(2).imag/pi
    positive('upper p endpoint J bound',c/3-a(Q(7,100)))
    positive('central value exceeds .646',2*c-a(Q(323,500)))
    positive('log 2 below .694',a(Q(347,500))-arb(2).log())
    positive('negative radius g bound',a(Q(21,1000))+a(Q(24,25)).log()/2)
    positive('positive radius g derivative bound',Q(2,5)-(-Q(1,6)/Q(13,25)+Q(1,3)/(1-Q(13,25))))
    positive('small p envelope below central',Q(323,500)-(Q(347,500)-Q(7,100)+Q(21,1000)))
    r=a(Q(12,25))
    positive('middle p increase of smaller index',3*r*r-(1+r*r-2*r*(pi/4).cos()))
    positive('lower square face inward',a(Q(24,25))**2*(67*pi/100).sin()**2-(1+r*r-2*r*(3*pi/10).cos()))
    r=a(Q(13,25))
    positive('upper square face inward',1+r*r-2*r*(37*pi/100).cos()-a(Q(26,25))**2*(67*pi/100).sin()**2)
    positive('cosine monotonicity premise',a(Q(3,5))-(3*pi/10).cos())
    positive('radius monotonicity premise',2*Q(12,25)/(1+Q(12,25)**2)-Q(3,5))
    def dq(s,r):
        theta=pi*a(s);r=a(r);den=1+r*r-2*r*theta.cos()
        return pi*r*theta.sin()/den,2*pi*(1-r*theta.cos())/den
    positive('d lower',dq(Q(37,100),Q(12,25))[0]-a(Q(8,5)))
    positive('d upper',a(Q(21,10))-dq(Q(3,10),Q(13,25))[0])
    positive('q upper',a(Q(34,5))-dq(Q(3,10),Q(12,25))[1])
    positive('k lower',-pi/(3*pi/5).tan()-1)
    assert 1/(Q(8,5)+Q(8,5)/(Q(8,5)+1))==Q(65,144)
    positive('height Hessian below 30',30-Q(42,5)-Q(34,5)**2*Q(65,144))
    positive('calibrated c upper',a(Q(161533,500000))-c)
    assert 2*Q(161533,500000)+15*Q(1,200)**2==Q(646507,10**6)
    positive('uniform exponent below .6466',Q(6466,10000)-Q(646507,10**6))
    positive('input lower height keeps radius below .53',a(Q(53,100))-(9*pi/500).exp()/2)
    pcard=-a(Q(6,25)).log()/2
    logratio=a(Q(53,47)).log()
    positive('two-height small-p lower endpoint',2*c-pcard-((pi/20).log()-1+logratio)/40)
    positive('two-height small-p upper endpoint',2*c-pcard+c/3-logratio/3)
    r=a(Q(53,100))
    positive('two-height upper square face inward',1+r*r-2*r*(37*pi/100).cos()-4*r*r*(67*pi/100).sin()**2)
    positive('two-height d upper',a(Q(21,10))-dq(Q(3,10),Q(53,100))[0])
    assert Q(42,5)+Q(34,5)**2*Q(5,8)==Q(373,10)
    positive('two-height Hessian below 38',38-Q(373,10))
    assert 2*Q(161533,500000)+19*(Q(9,1000)**2+Q(1,200)**2)==Q(648146,10**6)
    positive('two-height exponent below .6485',Q(1297,2000)-Q(648146,10**6))
    root=Path(__file__).resolve().parents[1]
    files=[Path(__file__).resolve(),root/'notes/research_three_vertex_symmetric_height_bound.md',
           root/'notes/research_three_vertex_global_wire_bound.md',
           root/'notes/research_three_chain_fourier_corner_transfer.md']
    data={'status':'passed','precision_bits':ctx.prec,'scalar_comparison_count':len(checks),
          'scalar_comparisons':checks,'exact_budget_identity_count':4,
          'scope':'Endpoint premises for the written unique global envelope, symmetric one-height bound and two-height Schur bound for the L40 retained vertex. No source asymptotic or maximum is inferred from sampling.',
          'sha256':{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest()for p in files}}
    output=args.output or root/'repro/results/research-three-vertex-symmetric-height-bound.json'
    output.write_text(json.dumps(data,indent=2)+'\n')
    print(f'Passed {len(checks)} scalar comparisons and four exact budget identities. {output}')


if __name__=='__main__':main()
