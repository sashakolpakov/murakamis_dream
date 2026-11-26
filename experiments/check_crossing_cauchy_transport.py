#!/usr/bin/env python3
"""Finite transport/Green algebra, residue normalization and corner budgets.

No complementary contour or dominant-source estimate is certified here.
The mixed reference is inherited from a checked Newton disk, with its
script/dependency hashes verified before reuse.
"""
import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

from flint import acb, arb, ctx
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=192)
    ap.add_argument('--output', type=Path,
                    default=ROOT/'repro/results/research-crossing-cauchy-transport.json')
    args = ap.parse_args()
    ctx.prec = args.precision
    exact = []

    # Pure rational identities need no approximate logarithmic equality.
    X,Y,Z,U,V,P = sp.symbols('X Y Z U V P')

    def rational_identity(name,expr):
        assert sp.cancel(expr) == 0,name
        exact.append(name)

    rational_identity('Cauchy numerator split',
                      (1-Y*Z)/(1-X*Z)-(1-Y/X)/(1-X*Z)-Y/X)
    rational_identity('one step inhomogeneous recurrence',
                      (X-Y)*P+Y*(1-X)*((Y-X)*P/(Y*(1-X))+X/(Y*(1-X)**2))-X/(1-X))
    a,b = sp.symbols('a b')
    rational_identity('cyclic denominator',1-(b-a)/(b*(1-a))-a*(1-b)/(b*(1-a)))
    rational_identity('residue cancels original X endpoint factor',
                      -(1-a)*(1-b)/(a-1)-(1-b))
    rational_identity('crossing first phase derivative',
                      -Y*(1-1/X)/(1-Y/X)-Y*(1-X)/(X-Y))
    rational_identity('crossing second phase derivative',
                      -X*(1-Y/X)/(1-Y)-(Y-X)/(1-Y))
    VV=Y/(Z*(Y-1)+Y)
    UU=1-(1/Z-1)/VV
    rational_identity('mixed formal stationarity elimination',
                      UU*(1-VV)-(1/Y-1)
                      -Z*(Y-1)*(Y*Z+2*Y-Z)/(Y*(Y*Z+Y-Z)))
    av=sp.symbols('a0:3')
    bv=sp.symbols('b0:3')
    green_numerator=sum(bv[j]*sp.prod(av[k] for k in range(j+1,3)) for j in range(3))
    sigma={av[j]:av[(j+1)%3] for j in range(3)}
    sigma.update({bv[j]:bv[(j+1)%3] for j in range(3)})
    rational_identity('abstract cyclic numerator identity',
                      green_numerator.xreplace(sigma)-av[0]*green_numerator
                      -(1-sp.prod(av))*bv[0])
    ar,ai,ct,st=sp.symbols('ar ai ct st',real=True)
    rho2=ar**2+ai**2
    dpoly=rho2*((1-ct)**2+st**2)-((1-ar*ct-ai*st)**2+(ar*st-ai*ct)**2)
    sinusoid=-(1-rho2)+2*(ar-rho2)*ct+2*ai*st
    assert sp.rem(sp.expand(dpoly-sinusoid),st**2+ct**2-1,st)==0
    exact.append('endpoint profile derivative sinusoid on unit circle')
    rational_identity('endpoint profile derivative at zero',
                      sinusoid.subs({ct:1,st:0})+(1-ar)**2+ai**2)

    # Exact root-of-unity finite checks, with independent rational input
    # values. The all-N result is the recurrence proof in the note.
    field=sp.QQ.algebraic_field(sp.I,sp.sqrt(3))
    xx=field.from_sympy(sp.Rational(1,3)+sp.I/5)
    yy=field.from_sympy(sp.Rational(1,4)+sp.I/7)
    def product(values):
        out=field.one
        for value in values:
            out*=value
        return out
    def field_identity(name,expr):
        assert expr==field.zero,name
        exact.append(name)
    finite=[]
    for N,r in [(2,-sp.Integer(1)),(3,(-1-sp.I*sp.sqrt(3))/2),
                (4,-sp.I),(6,(1-sp.I*sp.sqrt(3))/2)]:
        r=field.from_sympy(sp.sympify(r))
        bb=[]
        for i in range(N):
            bb.append(yy**i*product(1-r**j for j in range(1,i+1))
                      /product(1-yy*r**j for j in range(i+1)))
        for i in range(N):
            field_identity(f'N{N} original coefficient recurrence {i}',
                     (1-yy*r**i)*bb[i]-yy*(1-r**i)*bb[(i-1)%N]-(1 if i==0 else 0))

        def G(x):
            return sum(bb[i]/(1-x*r**i) for i in range(N))

        g0,g1=G(xx),G(xx*r)
        field_identity(f'N{N} Cauchy finite transport',(xx-yy)*g0+yy*(1-xx)*g1-xx/(1-xx))
        aa=[(yy-xx*r**j)/(yy*(1-xx*r**j)) for j in range(N)]
        ff=[xx*r**j/(yy*(1-xx*r**j)**2) for j in range(N)]
        mon=(yy**N-xx**N)/(yy**N*(1-xx**N))
        field_identity(f'N{N} cyclic monodromy',product(aa)-mon)
        green=sum(ff[j]*product(aa[k] for k in range(j+1,N)) for j in range(N))/(1-mon)
        field_identity(f'N{N} exact forced Green solution',g0-green)
        # X=Y remains regular in the recurrence and fixes the adjacent layer.
        field_identity(f'N{N} diagonal layer',G(yy*r)-field.one/(1-yy)**2)
        finite.append(N)

    for size in (3,7):
        pascal=sp.Matrix(size,size,lambda j,k:sp.binomial(j,k) if j>=k else 0)
        for power in range(5):
            claimed=sp.Matrix(size,size,lambda j,k:
                              sp.Integer(power)**(j-k)*sp.binomial(j,k) if j>=k else 0)
            assert pascal**power==claimed
            exact.append(f'Pascal power size{size} exponent{power}')

    source_path=ROOT/'repro/results/research-three-four-source-interface.json'
    source=json.loads(source_path.read_text())
    assert source['status']=='passed'
    assert source['script_sha256']==sha256((ROOT/'experiments/check_three_four_source_interface.py').read_bytes()).hexdigest()
    for p,h in source['dependencies_sha256'].items():
        assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p

    def rat(v):
        v=Fraction(v)
        return arb(v.numerator)/v.denominator

    cr,ci=source['root_certificate']['center']
    rad=rat(source['root_certificate']['complex_disk_radius'])
    aa=acb(rat(cr)+arb(0,rad),rat(ci)+arb(0,rad))
    BB=aa**2*(2*aa-1)**2/(2*(aa-1))
    pi,ii=arb.pi(),acb(0,1)
    wire=(aa**2*BB/(aa**2+BB)).sqrt().asin()/pi
    KK=(2*pi*ii*wire).exp()
    ZZ=2*KK/(1-KK)
    intermediate=ZZ.log()/(2*pi*ii)
    checks=[]

    def positive(name,value):
        assert value>0,(name,str(value))
        checks.append({'name':name,'strict_positive_margin':str(value)})

    for label,val,lo,hi in [('intermediate Z real',ZZ.real,'-.281','-.280'),
                          ('intermediate Z imaginary',ZZ.imag,'1.274','1.275'),
                          ('intermediate wire real',intermediate.real,'.284','.285'),
                          ('intermediate wire height',intermediate.imag,'-.043','-.042')]:
        positive(label+' lower',val-rat(lo))
        positive(label+' upper',rat(hi)-val)
    positive('outside old root-product domain',abs(ZZ)-rat('1.30'))
    positive('inside moving-residue domain',rat('.468')-abs(KK/ZZ))
    rho=abs(KK)
    vv=acb(KK.real-rho**2,KK.imag)
    alpha=((1-rho**2)/(2*abs(vv))).acos()
    theta=vv.arg()
    splus=(theta+alpha)/(2*pi)
    jplus=-(2*pi*ii*splus).exp().polylog(2).imag/(2*pi)
    iplus=((KK*(-2*pi*ii*splus).exp()).polylog(2)-KK.polylog(2))/(2*pi*ii)
    fplus=jplus+splus*rho.log()-iplus.real
    positive('profile has two interior turning points',2*abs(vv)-(1-rho**2))
    positive('first profile turning point is positive',theta-alpha)
    positive('last profile turning point precedes one',2*pi-theta-alpha)
    positive('profile maximum location lower',splus-rat('.441'))
    positive('profile maximum location upper',rat('.442')-splus)
    positive('strict endpoint profile gap exceeds .069',-rat('69/1000')-fplus)
    scut=rat('1/40')
    jcut=-(2*pi*ii*scut).exp().polylog(2).imag/(2*pi)
    icut=((KK*(-2*pi*ii*scut).exp()).polylog(2)-KK.polylog(2))/(2*pi*ii)
    fcut=jcut+scut*rho.log()-icut.real
    positive('L40 profile boundary below -.08',-rat('2/25')-fcut)
    fexterior=((1/ZZ).polylog(2)-pi**2/6-(KK/ZZ).polylog(2)+KK.polylog(2))/(2*pi*ii)+intermediate*KK.log()
    residue_relative_rate=fexterior.real-abs(ZZ).log()
    positive('residue below actual endpoint rate by .31',-rat('31/100')-residue_relative_rate)
    positive('L40 original corner budget',rat('27/200')-(arb(80).log()+1)/40)
    positive('inserted r<=3 logarithmic budget',rat('7/5')-arb(4).log())
    positive('one-factor old gap reserve exceeds1/60',rat('31/600')-arb(4).log()/40-rat('1/60'))
    for r in (1,2,3):
        positive(f'inserted r{r} total budget below .17',rat('17/100')-(arb(80).log()+1+arb(1+r).log())/40)

    deps=[
        'notes/research_crossing_cauchy_transport.md',
        'notes/research_three_four_source_interface.md',
        'notes/research_root_pochhammer_interpolation.md',
        'notes/exact_factorial_interpolation_and_complex_contours.md',
        'notes/research_three_chain_fourier_corner_transfer.md',
        'notes/research_traced_three_vertex_endpoint.md',
    ]
    result={
        'status':'passed','precision_bits':args.precision,
        'scope':'Exact rational finite transport, full-period Green and residue normalization, Pascal powers, inherited validated mixed-reference enclosure, one-factor inserted-corner budgets, and the outward critical-value test for the written endpoint-dominance criterion. Does not bound the remaining moved contour or prove a mixed-vertex source asymptotic.',
        'exact_identity_count':len(exact),'exact_identities':exact,'finite_levels':finite,
        'strict_comparison_count':len(checks),'comparisons':checks,
        'intermediate_enclosures':{'parameter':str(ZZ),'wire':str(intermediate),'output_over_input':str(KK/ZZ)},
        'endpoint_profile_enclosures':{'s_plus':str(splus),'F_at_s_plus':str(fplus),'F_at_L40':str(fcut),'residue_relative_rate':str(residue_relative_rate)},
        'inherited_reference':{'record':str(source_path.relative_to(ROOT)),
                               'sha256':sha256(source_path.read_bytes()).hexdigest(),
                               'script_and_all_dependency_hashes_verified':True},
        'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},
    }
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','exact_identity_count','strict_comparison_count']},indent=2))
    print('Necessary intermediate wire:',intermediate)


if __name__=='__main__':
    main()
