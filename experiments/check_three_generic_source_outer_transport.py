#!/usr/bin/env python3
"""Exact scalar budgets for generic original-source outer transport.

Only analytic scalar implications are checked here. The actual source,
kernel packet, full-period envelopes and curvature covers are cited
proved inputs, whose current file hashes are recorded.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
from flint import arb, ctx

ROOT=Path(__file__).resolve().parents[1]


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision',type=int,default=192)
    ap.add_argument('--output',type=Path,
                    default=ROOT/'repro/results/research-three-generic-source-outer-transport.json')
    args=ap.parse_args();ctx.prec=args.precision

    def a(v):
        v=Q(v);return arb(v.numerator)/v.denominator

    pi=arb.pi();sq=arb(21).sqrt();rho=(5-sq)/2;D=5+sq
    kmag=4*pi/sq;alpha=8*pi*arb(3).sqrt()/21
    R,W,L,H,b,A,aa=map(a,['.005','.009','.02','.0057','.18','1.45','1.5'])
    rD,rR,rDelta=map(a,['.00175','.0027','.0008'])
    Z=rho*a('1.05')/(1-a('.3')*rho)
    C0=kmag*(D+a('.6'))/(2*(D-a('.6'))**2)
    checks=[]

    def positive(name,value):
        assert value>0,(name,str(value))
        checks.append({'name':name,'strict_positive_margin':str(value)})

    positive('disk critical radius self-map',rD-rho*R-rho*(H+b*rD+a('.1')*(rD+R))/2)
    positive('real critical radius self-map',rR-rho*W-rho*(H+b*rR+9*(rR+W)**2)/2)
    positive('real correlated residual radius',rDelta-rho*(H+b*rR+9*(rR+W)**2)/2)
    positive('disk critical contraction below .05',a('.05')-rho*(b+a('.1'))/2)
    positive('real critical contraction below .05',a('.05')-rho*(b+a('.26'))/2)
    positive('real critical radius inside source disk',R-rR)
    positive('real kernel normalized Hessian below .26',a('.26')-18*(R+W))

    sectors={}
    for family,d0,r,eps in [('disk',R,rD,a('.28')),('real',R-rho*W,rDelta,a('.44'))]:
        q=r/d0
        gamma=2/arb(7).sqrt()*(1-2*q*q)-2*(arb(3)/7).sqrt()*q*(1-q*q).sqrt()
        positive(f'{family} sector ratio below .36',a('.36')-q)
        positive(f'{family} sector angular cosine positive',gamma)
        sector=kmag*(d0-r)**2*(D*gamma-eps)
        positive(f'{family} endpoint sector exceeds one forty-thousandth',sector-a(Q(1,40000)))
        sectors[family]=str(sector)
    positive('k0 argument smaller than pi/4',2*arb(3).sqrt()-3)
    positive('cos(3pi/8) exceeds one third',(3*pi/8).cos()-arb(1)/3)
    positive('outward endpoint derivative survives defect',D/3-a('.44'))
    positive('original incoming real curvature exceeds9',alpha*sq-kmag*b-9)
    positive('complex-output near-annulus curvature exceeds18',alpha*D-kmag*(b+18*(W+R))-18)
    positive('real-output near-annulus curvature exceeds18',alpha*sq-kmag*b+a('9.4')-18)

    loss=(A+aa)*L*L-kmag*H*L
    positive('far input loss increases beyond .02',2*(A+aa)*L-kmag*H)
    Lambda=(13+((alpha*sq-13)**2+(12*pi/sq)**2).sqrt())/2
    diskcost=C0*H*H+kmag*Z*H*R+b*kmag*R*R/2+Lambda*R*R
    realcost=C0*H*H+kmag*Z*H*W+(alpha*sq+b*kmag)*W*W/2
    positive('far complex-output gap exceeds .000563',loss-diskcost-a('.000563'))
    positive('far real-output gap exceeds .000424',loss-realcost-a('.000424'))
    positive('both far gaps exceed one twenty-five-hundredth',a('.000424')-a(Q(1,2500)))
    C=C0+kmag*kmag/(4*(A+aa))
    reset=kmag*Z*H*W+(aa-A)*W*W-C*H*H
    positive('reset at Hmax has reserve .00001061',reset-a('.00001061'))
    positive('reset at zero gradient', (aa-A)*W*W)
    positive('reset polynomial convex in H',C)
    # The two endpoint checks prove the full interval, since
    # C H^2-kmag Z W H-(a-A)W^2 is convex.
    paths=[
        'notes/research_three_generic_source_outer_transport.md',
        'notes/research_three_larger_phase_class.md',
        'notes/research_three_source_tail_propagation.md',
        'notes/research_three_vertex_real_input_union.md',
        'notes/research_three_vertex_input_rectangle.md',
        'notes/research_three_vertex_two_wire_large_cap_bound.md',
        'notes/research_three_vertex_large_cap_height_bound.md',
        'notes/research_three_first_entrance_real_extension.md',
        'repro/results/research-three-first-entrance-real-budgets.json',
    ]
    result={'status':'passed','precision_bits':ctx.prec,
            'strict_scalar_comparisons':len(checks),'comparisons':checks,
            'endpoint_sector_lower_bounds':sectors,
            'far_complex_gap':str(loss-diskcost),'far_real_gap':str(loss-realcost),
            'real_reset_reserve_at_Hmax':str(reset),
            'scope':'Generic original-source central V contour, near annulus .005..009, far input >=.02, and real reset beyond .009. Intermediate .009..02 is explicitly separate; no complete source induction is asserted.',
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest()for p in paths}}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(f'Passed {len(checks)} strict scalar comparisons.')
    print('Endpoint sectors:',sectors)
    print('Far gaps:',loss-diskcost,loss-realcost)
    print('Reset reserve:',reset)


if __name__=='__main__':main()
