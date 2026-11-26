#!/usr/bin/env python3
"""Outward root and endpoint gaps for the original type-four conditional.

Floating point roots propose rational centers only. Every accepted parameter
rectangle has its own complex Newton self-map, point root, zero logarithmic
lift, and mean-value action gap. The stored dyadic tree covers the full box.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import mpmath as mp
from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[1]

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision',type=int,default=256)
    ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-four-conditional-packet.json')
    args=ap.parse_args();ctx.prec=args.precision;mp.mp.dps=95
    pi,ii=arb.pi(),acb(0,1)
    def a(q):
        q=Q(q);return arb(q.numerator)/q.denominator
    def iv(l,r):return arb(a((l+r)/2),a((r-l)/2))
    def square(z,r):return acb(arb(z.real,a(r)),arb(z.imag,a(r)))
    def ln_sin(z):return (2*(pi*z).sin()).log()
    def fp(s,u,v):return ln_sin(s+u)+ln_sin(s+v)-3*ln_sin(s)+ii*pi*(u-v+s-a('1/2'))
    def fpp(s,u,v):return pi*((pi*(s+u)).cot()+(pi*(s+v)).cot()-3*(pi*s).cot())+ii*pi
    def J(z):return (pi*pi/6-(2*pi*ii*z).exp().polylog(2))/(2*pi*ii)+ii*pi*z*(1-z)/2
    def F(s,u,v):return J(s+u)+J(s+v)-3*J(s)+ii*pi*(s*(u-v)+(s*s-s)/2)
    def sup(z):return max(abs(z.real).upper(),abs(z.imag).upper())
    def rows(z):return abs(z.real)+abs(z.imag)
    def positive(name,x):
        assert x>0,(name,str(x));scalars.append({'name':name,'margin':str(x)})
    scalars=[]
    positive('cotangent comparison on the full middle rectangle',
             (pi/5).cos()-(2*pi/5).cos()*(2*pi/5).cosh())
    positive('middle negative Hessian exceeds one third',
             pi*(pi/10).sin()/((2*pi/5).cosh()+(pi/10).cos())-a('1/3'))
    positive('whole Hessian modulus below56',56-pi*(5*(pi/10).cot()+1))
    positive('left real-tail monotonicity',(pi/5).sin()**2-2*(pi/10).sin()**3)
    positive('right real-tail monotonicity before half',2*(9*pi/20).sin()**3-1)
    positive('right real-tail monotonicity after half',2*(pi/5).sin()-1)
    eps=a('1/100000')
    positive('horizontal alias reserve exceeds1e-5',pi*eps/2-4732*eps**2-a('1/100000'))
    positive('side excess retains1/600',
             a('11/100')**2/6-56*eps*a('11/100')-28*eps**2-a('1/600'))
    positive('height reserve',a('1/5')-a('17/100')-eps)
    # The exact cubic is obtained by the displayed sine exponential identity.
    import sympy as sp
    A,B,U=sp.symbols('A B U')
    assert sp.expand((1-A*U)*(1-B*U)-A*(1-U)**3-
                     (1-A+(2*A-B)*U+A*(B-3)*U**2+A*U**3))==0
    # Uniform Newton cells. The root proposal is never an acceptance test.
    def proposal(u,v):
        u=mp.mpf(u.numerator)/u.denominator;v=mp.mpf(v.numerator)/v.denominator
        def ff(s):
            return mp.log(2*mp.sin(mp.pi*(s+u)))+mp.log(2*mp.sin(mp.pi*(s+v)))-3*mp.log(2*mp.sin(mp.pi*s))+1j*mp.pi*(u-v+s-mp.mpf('.5'))
        z=mp.findroot(ff,(mp.mpc('.3','-.06'),mp.mpc('.3','-.1')),tol=mp.mpf('1e-85'))
        return [mp.nstr(z.real,85),mp.nstr(z.imag,85)]
    def certify(box,address):
        ul,ur,vl,vr=box;um=(ul+ur)/2;vm=(vl+vr)/2
        center=proposal(um,vm);z=acb(*map(arb,center));u0,v0=acb(a(um)),acb(a(vm))
        inv=1/fpp(z,u0,v0);point_radius=Q(1,10**40)
        zp=square(z,point_radius)
        kp=rows(1-inv*fpp(zp,u0,v0));ep=sup(inv*fp(z,u0,v0))
        assert kp<a('1/2') and ep+kp*a(point_radius)<a(point_radius)
        u,v=acb(iv(ul,ur)),acb(iv(vl,vr))
        residual=sup(inv*fp(z,u,v))
        # Rounded-up dyadic radius, independently checked below.
        rv=Q(1,2**16)
        while a(rv)<3*residual:rv*=2
        if rv>Q(1,16):return None
        zs=square(z,rv);k=rows(1-inv*fpp(zs,u,v))
        if not (k<a('1/2') and residual+k*a(rv)<a(rv)):return None
        if not (zs.real>a('6/25') and zs.real<a('17/50') and
                zs.imag>-a('17/100') and zs.imag<a('1/100')):return None
        gaps=[]
        for cut in [Q(1,10),Q(9,20)]:
            c=acb(a(cut))
            center_gap=(F(zp,u0,v0)-F(c,u0,v0)).real
            da=(ln_sin(zs+u)-ln_sin(c+u)+ii*pi*(zs-c)).real
            db=(ln_sin(zs+v)-ln_sin(c+v)-ii*pi*(zs-c)).real
            gap=center_gap-abs(da)*a((ur-ul)/2)-abs(db)*a((vr-vl)/2)
            if not gap>a('1/50'):return None
            gaps.append(str(gap))
        return {'address':address,'bounds':[str(x)for x in box],
                'center':center,'radius':str(rv),'point_radius':str(point_radius),
                'newton_contraction':str(k),'newton_residual':str(residual),
                'endpoint_gaps':gaps}
    queue=[((Q(1,5),Q(9,20),Q(1,5),Q(9,20)),'')]
    leaves=[];visited=0
    while queue:
        box,address=queue.pop();visited+=1
        if len(address)>22:raise RuntimeError(('unresolved',box,address))
        got=certify(box,address)
        if got is not None:
            leaves.append(got)
        else:
            l,r,b,t=box
            if len(address)%2==0:
                c=(l+r)/2;children=[(l,c,b,t),(c,r,b,t)]
            else:
                c=(b+t)/2;children=[(l,r,b,c),(l,r,c,t)]
            queue.extend((z,address+str(j))for j,z in enumerate(children))
    # Exact binary partition audit, independent of the acceptance predicates.
    codes={x['address']for x in leaves};assert len(codes)==len(leaves)
    def cover(code):
        if code in codes:return
        assert any(x.startswith(code+'0')for x in codes),code
        assert any(x.startswith(code+'1')for x in codes),code
        cover(code+'0');cover(code+'1')
    cover('')
    deps=['notes/research_mixed_four_conditional_packet.md',
          'notes/research_mixed_conditional_leg_sum.md',
          'notes/exact_factorial_interpolation_and_complex_contours.md']
    result={'status':'passed','precision_bits':args.precision,
            'strict_scalar_count':len(scalars),'scalars':scalars,
            'exact_identity_count':1,'visited_cells':visited,'accepted_cells':len(leaves),
            'parameter_domain':['1/5','9/20','1/5','9/20'],
            'root_box':['6/25','17/50','-17/100','1/100'],
            'endpoint_gap':'1/50','leaves':leaves,
            'scope':'Uniform zero-lift physical conditional saddle and endpoint gaps. The written contour proof supplies the full original finite-sum packet, not a mixed-word theorem.',
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest()for p in deps}}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k]for k in ['status','strict_scalar_count','exact_identity_count','visited_cells','accepted_cells']}))

if __name__=='__main__':main()
