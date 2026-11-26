#!/usr/bin/env python3
"""Exact global exclusion and Hessian checks for the two-wire .03 cap."""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import argparse
import json

from flint import arb, acb, ctx
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]


def a(value):
    value=Q(value)
    return arb(value.numerator)/value.denominator


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision',type=int,default=192)
    ap.add_argument('--output',default='repro/results/research-three-vertex-two-wire-large-cap-bound.json')
    args=ap.parse_args()
    ctx.prec=args.precision
    pi=arb.pi()
    c=-(acb(0,5*pi/3).exp().polylog(2)).imag/pi
    checks=[]
    def positive(name,value):
        assert value>0,(name,value)
        checks.append({'name':name,'margin':str(value)})

    tangent=((pi/20).log()-1)/40
    weight=Q(27,10000)
    low=arb(2).log()+tangent+a(weight)
    positive('original central value exceeds .646',2*c-a(Q(323,500)))
    positive('J one-third endpoint below first-endpoint tangent',tangent+c/3)
    positive('reported weighted low-sum bound below .624573',a(Q(624573,10**6))-low)
    positive('weighted low-sum bound below original central value',2*c-low)
    positive('smaller-index monotonicity through middle sum band',a(Q(3,4))-(a(Q(5,4))-(pi/4).cos()))
    positive('index and wire coefficient monotonicity',a(Q(4,5))-(13*pi/50).cos())
    d=(pi/2)*(2*pi/5).sin()/(a(Q(5,4))-(2*pi/5).cos())
    positive('index endpoint coercivity exceeds 3/2',d-a(Q(3,2)))
    positive('wire endpoint coefficient exceeds3',2*d-3)
    positive('left index-face distance exceeds1/15',a(Q(1,3)-Q(13,50)-Q(1,15)))
    positive('global index-exit loss exceeds both capped weights',a(Q(1,300)-weight))
    positive('positive common Hessian coefficient',a(2*Q(13,50)-Q(1,2)))
    positive('top sine endpoint remains below1',a(1-2*Q(2,5)))
    positive('left wire boundary outside clipped interval',a(Q(1,6)-Q(3,100)-Q(13,100)))
    positive('right wire boundary outside clipped interval',a(Q(1,5)-Q(1,6)-Q(3,100)))
    positive('lower difference angle is positive',a(Q(13,50)-Q(1,5)))
    positive('upper difference angle is below half-period',a(Q(1,2)-Q(2,5)+Q(13,100)))

    # Exact endpoint coincidences and total budget.
    exact=[Q(2,5)-Q(1,3)==Q(1,15),
           Q(13,50)/2==Q(13,100), Q(2,5)/2==Q(1,5),
           2*Q(3,2)*Q(3,100)**2==weight,
           Q(3,4)*Q(1,15)**2-weight==Q(19,30000)]
    assert all(exact)

    # Direct four-variable negative Hessian versus the incidence form.
    k,dx,dy,cx,cy,ox,oy=sp.symbols('k Dx Dy Cx Cy omega_x omega_y',real=True)
    ds,dt,dxi,deta=sp.symbols('ds dt dxi deta',real=True)
    matrix=sp.Matrix([[k+dx,k,-dx,0],[k,k+dy,0,-dy],
                      [-dx,0,dx+cx-ox,0],[0,-dy,0,dy+cy-oy]])
    vector=sp.Matrix([ds,dt,dxi,deta])
    form=k*(ds+dt)**2+dx*(ds-dxi)**2+dy*(dt-deta)**2+(cx-ox)*dxi**2+(cy-oy)*deta**2
    assert sp.expand((vector.T*matrix*vector)[0]-form)==0

    paths=['notes/research_three_vertex_two_wire_large_cap_bound.md',
           'notes/research_three_vertex_global_wire_bound.md',
           'notes/research_three_vertex_symmetric_height_bound.md']
    result={'status':'passed','precision_bits':args.precision,
            'strict_scalar_comparisons':len(checks),'exact_endpoint_identities':len(exact),
            'exact_joint_Hessian_identities':1,'checks':checks,
            'cap_radius':'3/100','both_distance_coefficients':'3/2',
            'weighted_low_sum_upper':str(low),'index_exit_reserve':'19/30000',
            'wire_endpoint_coefficient':str(2*d),
            'scope':'Global real two-wire original retained-summand upper bound, including finite endpoints. No source lower bound or independent height extension.',
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependencies_sha256':{name:sha256((ROOT/name).read_bytes()).hexdigest() for name in paths}}
    (ROOT/args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:result[key] for key in ('status','strict_scalar_comparisons','exact_endpoint_identities','exact_joint_Hessian_identities','weighted_low_sum_upper','wire_endpoint_coefficient')},indent=2))


if __name__=='__main__':
    main()
