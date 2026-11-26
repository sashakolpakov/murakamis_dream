#!/usr/bin/env python3
"""Two rigorous concave support planes for the original prepared-cap period.

The support points are fixed rational numbers. No optimizer or sampled
maximum is used. Global concavity and the finite-source decomposition
are proved in the accompanying note.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import argparse
import json

from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[1]
I = acb(0, 1)


def r(v):
    v = Q(v)
    return arb(v.numerator)/v.denominator


def interval(a, b):
    return r(a).union(r(b))


def j_real(z):
    """Real part of the original J on its positive strip, by Schwarz."""
    z = acb(z.real, abs(z.imag))
    p = arb.pi()
    return (-I*p*(z*z-z)/2 + I*(2*p*I*z).exp().polylog(2)/(2*p)
            -I*p/12).real


def supporting_upper(value, gradient, point, box):
    return value+sum(max((g*r(a-z)).upper(), (g*r(b-z)).upper())
                     for g,z,(a,b) in zip(gradient, point, box))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=192)
    ap.add_argument('--output', type=Path)
    args = ap.parse_args()
    ctx.prec = args.precision
    p = arb.pi()
    yh = arb(2).log()/(2*p)
    hc = interval('.10135867', '.10135871')
    Hc = interval('.97895508', '.97895512')
    planes, checks = [], []

    def positive(name, value):
        assert value > 0, (name, value)
        checks.append({'name': name, 'positive_margin': str(value)})

    # Actual positive bottom of the full complete cap. All other cap
    # currents already have the strictly smaller rate1.26.
    z = [Q('.180461985434'), Q('1.522032732790')]
    box = [(Q(7,50),Q(1,5)), (Q(0),Q(9,5))]
    x, t = acb(r(z[0]), hc), acb(r(z[1]), -Hc)
    b = -j_real(acb(arb(1)/2)-x+t/(2*p)) \
        -j_real(acb(arb(1)/2)-x-t/(2*p))-2*j_real(x)
    psi = -4*j_real(acb(arb(1)/4)+t/(4*p)) \
          -4*j_real(acb(arb(1)/4)-t/(4*p))
    value = b+psi+3*t.real*(-t.imag)/(2*p)+t.imag
    cp, cm = (p*x+t/2).cos(), (p*x-t/2).cos()
    g = [abs(cp).log()+abs(cm).log()-2*abs((p*x).sin()).log(),
         (abs(cp).log()-abs(cm).log())/(2*p)
         -(t/2).tan().asinh().real/p-3*t.imag/(2*p)]
    upper = supporting_upper(value,g,z,box)
    positive('actual full central cap below1.26465', r('1.26465')-upper)
    planes.append({'name':'actual cap bottom', 'point':list(map(str,z)),
                   'box':[[str(a),str(b)]for a,b in box],
                   'value':str(value),'gradient':list(map(str,g)),
                   'support_upper':str(upper),'threshold':'1.26465'})

    # Global optimized denominator envelope. The established global
    # maximum is in[.30,.37]^2 throughout radius[.5,.53].
    z = [Q('.35320055'), Q('.32326893')]
    box = [(Q(3,10),Q(37,100))]*2
    s, t = map(r,z)
    radius = (-2*p*hc).exp()
    second = arb(1)/2
    J = -(2*p*I*(s+t)).exp().polylog(2).imag/(2*p)

    def ell(index, rad):
        return -(rad*(p*I*index).exp()).polylog(2).imag/p

    value = -(radius*second).log()/2+J+s*radius.log()+t*second.log() \
            -ell(s,radius)-ell(t,second)
    g = [(2*radius*(p*(s+t)).sin()).log()
         -abs(1-radius*(p*I*s).exp()).log(),
         (2*second*(p*(s+t)).sin()).log()
         -abs(1-second*(p*I*t).exp()).log()]
    upper = supporting_upper(value,g,z,box)
    positive('global retained envelope below.64699',r('.64699')-upper)
    planes.append({'name':'global retained envelope', 'point':list(map(str,z)),
                   'box':[[str(a),str(b)]for a,b in box],
                   'value':str(value),'gradient':list(map(str,g)),
                   'support_upper':str(upper),'threshold':'.64699'})

    positive('base height is below homogeneous height',yh-hc)
    positive('base height above homogeneous minus.009',hc-yh+r('.009'))
    positive('base radius below.53',r('.53')-radius)
    positive('base radius above.5',radius-r('.5'))
    positive('central height interval in joint chamber',hc-r('.09'))
    positive('central height interval below.12',r('.12')-hc)
    positive('cap depth above.97',Hc-r('.97'))
    positive('cap depth below1',1-Hc)

    positive('central product below1.91165',r('1.91165')-r('1.26465')-r('.64699'))
    positive('exterior product below1.91164',
             r('1.91164')-r('1.264')-2*r(Q(161533,500000)))
    positive('both wire joins below1.91164',r('1.91164')-r('1.2638')-r('.64699'))
    positive('original Fourier corner error below1.91164',r('1.91164')-r('1.715'))
    positive('homogeneous envelope below.64699',r('.64699')-2*r(Q(161533,500000)))

    positive('sqrt21 below23/5',r(Q(23,5))**2-21)
    positive('pi above25/8',p-r(Q(25,8)))
    k_lower = Q(125,46)
    floor = Q('1.9113')+k_lower*Q('.03')*Q('.005')-Q(29,20)*Q('.005')**2
    positive('initial class floor outside.005 exceeds1.91165',r(floor)-r('1.91165'))
    positive('initial class floor increases until.01',
             r(k_lower*Q('.03')-Q(29,10)*Q('.01')))

    paths = [Path(__file__).resolve(),
             ROOT/'notes/research_three_prepared_cap_period_bound.md',
             ROOT/'notes/research_three_cap_central_source.md',
             ROOT/'notes/research_three_vertex_joint_concavity.md',
             ROOT/'notes/research_three_vertex_global_wire_bound.md',
             ROOT/'notes/research_three_prepared_cap_quantified_source.md',
             ROOT/'notes/research_three_cap_wire_complement.md',
             ROOT/'notes/research_three_chain_fourier_corner_transfer.md',
             ROOT/'notes/research_three_phase_graph_transform.md']
    result={'status':'passed','precision_bits':args.precision,
            'scope':'Original prepared cap on the whole real outgoing period at homogeneous height, with original outside ordinary normals; no later attachment asserted.',
            'support_plane_count':len(planes),'support_planes':planes,
            'outward_comparison_count':len(checks),'outward_comparisons':checks,
            'constants':{'central_cap':'1.26465','retained_vertex':'.64699',
                         'complete_outside_period_rate':'1.91164',
                         'small_complex_outside_rate':'1.91165'},
            'sha256':{str(path.relative_to(ROOT)):sha256(path.read_bytes()).hexdigest()
                      for path in paths}}
    output=args.output or ROOT/'repro/results/research-three-prepared-cap-period-bound.json'
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(f'Passed {len(planes)} concave supporting planes and {len(checks)} outward comparisons.\n{output}')


if __name__=='__main__':main()
