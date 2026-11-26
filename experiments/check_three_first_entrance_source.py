#!/usr/bin/env python3
"""Outward budgets for the actual first entrance source attachment."""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import argparse
import json
from flint import arb, ctx

ROOT=Path(__file__).resolve().parents[1]

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision',type=int,default=192)
    ap.add_argument('--output',type=Path)
    args=ap.parse_args();ctx.prec=args.precision
    def a(v):
        v=Q(v);return arb(v.numerator)/v.denominator
    checks=[]
    def positive(name,v):
        assert v>0,(name,str(v))
        checks.append({'name':name,'positive_margin':str(v)})
    pi=arb.pi();r21=arb(21).sqrt();kmag=4*pi/r21
    alpha=8*pi*arb(3).sqrt()/21;beta=-4*pi/7
    D=5+r21;rho=(5-r21)/2;R=a(Q(1,200))
    H=a(Q(69,2500));P=a(Q(113,10000));A1=a(Q(93,20))
    Z=rho*a(Q(21,20))/(1-a(Q(3,10))*rho)
    C0=kmag*(D+a(Q(3,5)))/(2*(D-a(Q(3,5)))**2)
    Lambda=(13+((alpha*r21-13)**2+(beta*r21)**2).sqrt())/2
    B=C0*H*H+kmag*Z*H*R+a(Q(9,100))*kmag*R*R+Lambda*R*R
    positive('middle main input gap above one millionth',
             (A1+a(Q(3,2)))*a('.01')**2-P*a('.01')-B-a(Q(1,10**6)))
    positive('absolute input error gap above nine hundred-thousandths',
             a('1.9113')-a('1.9107')-B-a(Q(9,10**5)))
    positive('far input gap above two ten-thousandths',
             a('1.9113')-a('1.91115')+a(Q(3,2))*a('.02')**2-B-a(Q(2,10**4)))
    positive('middle input loss increases',2*(A1+a(Q(3,2)))*a('.01')-P)
    positive('real endpoint derivatives point outward',
             a('9.3')*R-P+5*alpha*R-2*kmag*R-a(Q(1,5))*kmag*R)
    positive('real annulus combined curvature above18',
             a('9.3')+5*alpha-18*kmag*(a('.01')+R)-18)
    positive('outgoing complex gradient below .0065',a('.0065')-Z*H)
    lower=a('1.9113')+a('.646')-C0*H*H-kmag*Z*H*R-kmag*r21*R*R/2-a(Q(9,100))*kmag*R*R
    positive('output phase real part above2.55',lower-a('2.55'))
    positive('three-vertex corner rate below2.38',a('2.38')-a('1.715')-2*a(Q(161533,500000))-pi*R)
    B2=C0*H*H+P*P/(4*(a(Q(29,20))+a(Q(3,2))))
    positive('global real envelope slack below .000143',a('.000143')-B2)
    positive('restored real-corner error below global real-envelope floor',
             a('1.9113')+a('.646')-C0*H*H-a(Q(3,2))*a('.03')**2-a('2.38'))
    dependencies=[
        'notes/research_three_first_entrance_source.md',
        'notes/research_three_prepared_cap_real_extension.md',
        'notes/research_three_entrance_critical_branches.md',
        'notes/research_three_prepared_cap_quantified_source.md',
        'notes/research_three_phase_graph_transform.md',
        'notes/research_three_vertex_input_rectangle.md',
        'notes/research_three_vertex_large_cap_height_bound.md',
        'notes/research_three_vertex_two_wire_large_cap_bound.md',
        'notes/research_three_chain_fourier_corner_transfer.md',
    ]
    result={'status':'passed','precision_bits':ctx.prec,'scalar_comparison_count':len(checks),
            'scalar_comparisons':checks,'constants':{'complex_output_cost':str(B),'next_gradient_bound':str(Z*H),'real_envelope_slack':str(B2)},
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependencies_sha256':{s:sha256((ROOT/s).read_bytes()).hexdigest()for s in dependencies},
            'scope':'Strict budgets for the written first additional original-source attachment. Incoming absolute expansion and correlated critical sectors are separately proved inputs; later entrance attachments are not asserted.'}
    out=args.output or ROOT/'repro/results/research-three-first-entrance-source.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(f'Passed {len(checks)} strict scalar comparisons. {out}')
    print('Complex output cost:',B)
    print('Next gradient bound:',Z*H)
    print('Real envelope slack:',B2)

if __name__=='__main__':main()
