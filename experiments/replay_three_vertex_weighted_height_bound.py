#!/usr/bin/env python3
"""Independent uniform Newton replay for the global weighted envelope.

Uses complex logarithmic moduli and direct 3x3 cofactors, independently
of the author’s real trigonometric gradient and Schur implementation.
No optimizer or author module is imported.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import argparse
import json
import time

from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[1]
I = acb(0, 1)


def r(value):
    value = Q(value)
    return arb(value.numerator)/value.denominator


def interval(lo, hi):
    return r((lo+hi)/2)+arb(0, r((hi-lo)/2))


def original_gradient_hessian(z, height):
    s, t, xi = z
    pi = arb.pi()
    radius = (-2*pi*height).exp()/2
    first = (2*pi*I*(xi-s)).exp()/2
    second = (2*pi*I*xi).exp()/2
    output = radius*(pi*I*t).exp()
    l1, l2, lo = abs(1-first).log(), abs(1-second).log(), abs(1-output).log()
    f1 = (-2*pi*I*first/(1-first)).real
    f2 = (-2*pi*I*second/(1-second)).real
    dt = (-pi*I*output/(1-output)).real
    common = pi/(pi*(s+t)).tan()
    gradient = [((pi*(s+t)).sin()).log()-l1,
                (2*radius*(pi*(s+t)).sin()).log()-lo,
                l1-l2+3*(xi-arb(1)/6)]
    jacobian = [[common+f1, common, -f1],
                [common, common-dt, arb(0)],
                [-f1, arb(0), f1-f2+3]]
    H = [[-v for v in row] for row in jacobian]
    first_minor = H[0][0]*H[1][1]-H[0][1]**2
    determinant = H[0][0]*H[1][1]*H[2][2]-H[0][1]**2*H[2][2]-H[0][2]**2*H[1][1]
    cofactor = H[0][0]*H[2][2]-H[0][2]**2
    q = 2*pi*(1/(1-output)).real
    curvature = 4*dt+q*q*cofactor/determinant
    return gradient, jacobian, q, curvature, (H[0][0], first_minor, determinant)


def scalar_checks():
    pi = arb.pi()
    def fp(u):
        z=(2*pi*I*r(u)).exp()/2
        return (-2*pi*I*z/(1-z)).real
    budget = 15*Q(1,200)**2+Q(3,2)*Q(1,100)**2
    rr, ss = r(Q(12,25)), r(Q(39,100))
    denominator = abs(1-rr*(pi*I*ss).exp())**2
    ds = pi*rr*(pi*ss).sin()/denominator
    checks = [r(Q(1,3)-Q(221,14400)-Q(317,1000)),
              r(Q(35,100)-Q(1,3)-Q(221,14400)),
              r(2*Q(12,25)/(1+Q(12,25)**2))-(7*pi/25).cos(),
              ds-r(Q(3,2)),
              r(Q(3,4)*Q(37,1000)**2-budget),
              r(Q(323,500)-Q(129,200)-Q(3,20000)),
              fp(Q(7,100))-3, fp(Q(21,100))-3,
              fp(Q(12,100))-3, fp(Q(39,200))-3,
              fp(Q(14,100))-2, fp(Q(27,100))-2,
              r(3*Q(3,200)**2-budget),
              r(Q(5,2)*Q(1,50)**2-budget),
              r(13-Q(251,20)-75*Q(1,200))]
    assert all(c>0 for c in checks)
    return len(checks)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=256)
    ap.add_argument('--artifact', default='repro/results/research-three-vertex-weighted-height-bound.json')
    ap.add_argument('--output', default='repro/results/research-three-vertex-weighted-height-bound-replay.json')
    args=ap.parse_args()
    ctx.prec=args.precision
    start=time.monotonic()
    source=ROOT/args.artifact
    data=json.loads(source.read_text())
    assert data['status']=='passed' and data['height_cell_count']==2048
    count=scalar_checks()
    mesh=2048
    step=Q(1,100*mesh)
    seen=set()
    for cell in data['height_cells']:
        j=cell['index']
        assert isinstance(j,int) and 0<=j<mesh and j not in seen
        seen.add(j)
        lo=Q(-1,200)+j*step
        hi=lo+step
        assert list(map(Q,cell['height_interval']))==[lo,hi]
        centers=[r(v) for v in cell['center']]
        C=[[r(v) for v in row] for row in cell['preconditioner']]
        assert len(centers)==3 and len(C)==3 and all(len(row)==3 for row in C)
        dv=r(step/2)
        radii=[4*dv,4*dv,3*dv]
        z=[v+arb(0,rad) for v,rad in zip(centers,radii)]
        vb=interval(lo,hi)
        g0=original_gradient_hessian(centers,r((lo+hi)/2))[0]
        _, jac, _, second, minors=original_gradient_hessian(z,vb)
        qparam=original_gradient_hessian(centers,vb)[2]
        assert qparam>0 and all(m>0 for m in minors)
        for row in range(3):
            contraction=sum(abs(arb(int(row==col))-sum(C[row][k]*jac[k][col] for k in range(3)))*radii[col]
                            for col in range(3))/radii[row]
            displacement=abs(sum(C[row][k]*g0[k] for k in range(3)))+abs(C[row][1])*qparam*dv
            assert contraction<arb(1)/10 and radii[row]*(1-contraction)>displacement,(j,row)
        s,t,xi=z
        assert all(v>r('.28') and v<r('.39') for v in(s,t))
        assert xi>r(Q(1,6)-Q(1,100)) and xi<r(Q(1,6)+Q(1,100))
        ceiling=Q(251,10)+450*max(lo,Q(0))
        assert Q(cell['ceiling'])==ceiling
        assert second<r(ceiling),(j,second,ceiling)
    assert seen==set(range(mesh))
    author=ROOT/'experiments/certify_three_vertex_weighted_height_bound.py'
    assert sha256(author.read_bytes()).hexdigest()==data['script_sha256']
    for name,digest in data['dependencies_sha256'].items():
        assert sha256((ROOT/name).read_bytes()).hexdigest()==digest,name
    result={'status':'passed','precision_bits':args.precision,'height_cell_count':mesh,
            'exact_rational_cover':True,'scalar_comparison_count':count,
            'Newton_and_curvature_on_entire_boxes':True,
            'method':'Independent logarithmic-modulus gradient, direct Hessian and cofactors; rational stored centers, no optimizer or author import.',
            'elapsed_seconds':time.monotonic()-start,
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'author_script_sha256':data['script_sha256'],
            'artifact_sha256':sha256(source.read_bytes()).hexdigest(),
            'dependencies_sha256':data['dependencies_sha256']}
    (ROOT/args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
