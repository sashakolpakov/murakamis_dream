#!/usr/bin/env python3
"""Exact contracted phase/symbol algebra and outward original branch checks.

This checks no complementary finite sum and no mixed-word lower bound.
"""
import argparse,json
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import sympy as sp
from flint import arb,acb,ctx

ROOT=Path(__file__).resolve().parents[1]
I=acb(0,1)
def r(v):
    q=Q(v);return arb(q.numerator)/q.denominator
def interval(lo,hi):return r(lo).union(r(hi))
def digest(p):return sha256(p.read_bytes()).hexdigest()

def algebra():
    checks=[]
    def zero(name,v):
        assert sp.cancel(sp.expand(v))==0,(name,v);checks.append(name)
    z,w,X=sp.symbols('z w X');xc=(1-z*w)/(z+w-2*z*w)
    zero('wire stationary rational equation',(1-xc*z)*(1-xc*w)-z*w*(1-xc)**2)
    zero('left Gram derivative ratio',xc/(1-xc*z)-(1-z*w)/(w*(1-z)**2))
    zero('right Gram derivative ratio',xc/(1-xc*w)-(1-z*w)/(z*(1-w)**2))
    v=sp.symbols('v')
    zero('three single-leg quadratic',(1-z*v)*(1-z*w)-w*(1-z)**2-(1-w+z*(w-v)+z*z*w*(v-1)))
    zero('four single-leg cubic',(1-z*v)*(1-z*w)-w*(1-z)**3-(1-w+z*(2*w-v)+z*z*w*(v-3)+w*z**3))
    u4=(-1-sp.I*sp.sqrt(7))/4
    zero('homogeneous four exponent',(1-u4*u4)**2-u4*(1-u4)**3)
    a=sp.symbols('a');p=4*a**4-6*a**3+4*a*a-2*a+1
    K=1/(1+2*a-4*a*a);U=1-2*a;V=(1-K)/(2*K)
    for name,v in {
        'original alternating contracted wire':K*(U+V-2*U*V)-(1-U*V),
        'contracted three-gradient exponent':(1-U*U)*(1-U*V)-V*(1-U)**2,
        'contracted four-gradient exponent':(1-V*V)*(1-U*V)-U*(1-V)**3}.items():
        numerator,_=sp.fraction(sp.factor(v));zero(name,sp.rem(numerator,p,a))
    N=sp.symbols('N',positive=True);J=sp.Function('J')
    phi=lambda x:sp.pi*(x-x*x)/2
    theta=lambda j:sp.pi*j/2-sp.pi*j*(j+1)/(2*N)
    for word in [(3,),(4,),(3,4),(3,3,4),(3,4,3,4)]:
        m=len(word);ss=sp.symbols(f's0:{m}',real=True);tt=sp.symbols(f't0:{m}',real=True)
        eps=[int(n==4)for n in word];k=sum(eps)
        leading=sp.pi*sum(tt[v]*(ss[(v+1)%m]-ss[v])for v in range(m))-sum(eps[v]*(phi(ss[v])+phi(tt[v]))for v in range(m))
        original=sum(theta(N*(ss[v]+tt[v]))if word[v]==3 else -sp.pi*N*ss[v]*tt[v]for v in range(m))-sum(theta(N*(tt[v]+ss[(v+1)%m]))for v in range(m))
        correction=sp.pi*sum(eps[v]*(ss[v]+tt[v])for v in range(m))/2
        zero(f'exact finite phase and coefficient {word}',original-N*leading-correction)
        H=sum(J(ss[v]+tt[v])+J(tt[v]+ss[(v+1)%m])-(2+eps[v])*(J(ss[v])+J(tt[v]))for v in range(m))
        g=lambda v:J(v)+sp.I*phi(v)
        direct=sum(g(ss[v]+tt[v])-eps[v]*(g(ss[v])+g(tt[v]))for v in range(m))
        direct+=sum(J(tt[v]+ss[(v+1)%m])-2*J(tt[v])-2*J(ss[(v+1)%m])-sp.I*phi(tt[v]+ss[(v+1)%m])for v in range(m))
        zero(f'absolute contracted phase decomposition {word}',direct-H-sp.I*leading)
        zero(f'original density N exponent {word}',k+sp.Rational(2*m,2)-sp.Rational(4*m+2*k,2)+m)
        zero(f'local Gaussian N exponent {word}',2*m-m-m)
        for entry in sp.hessian(leading,ss+tt):assert sp.im(entry)==0
        checks.append(f'quadratic phase Hessian real constant {word}')
    c=sp.pi/sp.sqrt(3)
    homogeneous=sp.Matrix([[4*c,2*c],[2*c,4*c]])
    zero('single-three cyclic Hessian determinant',homogeneous.det()-4*sp.pi**2)
    zero('single-three cyclic Gaussian coefficient',2*sp.pi/(sp.sqrt(3)*2*sp.pi)-1/sp.sqrt(3))
    return checks

def reference():
    path=ROOT/'repro/results/research-three-four-source-interface.json';data=json.loads(path.read_text());assert data['status']=='passed'
    assert data['script_sha256']==digest(ROOT/'experiments/check_three_four_source_interface.py')
    for dep,h in data['dependencies_sha256'].items():assert digest(ROOT/dep)==h,dep
    rr=data['root_certificate'];re,im=map(Q,rr['center']);radius=r(rr['complex_disk_radius'])
    a=acb(r(re)+arb(0,radius),r(im)+arb(0,radius));K=1/(1+2*a-4*a*a)
    U=1-2*a;V=(1-K)/(2*K);pi=arb.pi();s=-U.log()/(2*pi*I);t=-V.log()/(2*pi*I)
    return K,U,V,s,t,{'path':str(path.relative_to(ROOT)),'sha256':digest(path),'all_dependency_hashes_verified':True}

def branches(K,U,V,s,t):
    pi=arb.pi();margins={}
    def pos(name,v):assert v>0,(name,str(v));margins[name]=str(v)
    for name,z in [('three',s),('four',t)]:
        pos(name+' real lower',z.real-arb(1)/4);pos(name+' real upper',arb(9)/20-z.real)
        pos(name+' imaginary chamber',arb(11)/200-abs(z.imag))
    jp=lambda z:(2*(pi*z).sin()).log()
    d3=jp(2*s)+jp(s+t)-2*jp(s)+pi*I*(t-s)
    d4=jp(2*t)+jp(s+t)-3*jp(t)+pi*I*s-pi*I/2
    assert d3.contains(0)and d4.contains(0),(d3,d4)
    pos('three original zero lift',pi-abs(d3.imag));pos('four original zero lift',pi-abs(d4.imag))
    cb=pi*(9*pi/10).sin()/((11*pi/100).cosh()-(9*pi/10).cos())
    pos('length-independent coercivity exceeds .8',2*cb-arb(4)/5)
    # Explicit starting lifts at the calibrated diagonal.
    u0=acb(-arb(1)/2,-arb(3).sqrt()/2);x0=(1+u0)/(2*u0)
    wire=-2*u0.log()+2*(1-x0*u0).log()-2*(1-x0).log()-2*pi*I
    difference=(1-u0*u0).log()-2*(1-u0).log()-u0.log()-x0.log()+(1-x0*u0).log()
    assert wire.contains(0)and difference.contains(0),(wire,difference)
    pos('homogeneous wire zero lift',pi-abs(wire.imag));pos('homogeneous Gram derivative lift',pi-abs(difference.imag))
    # A rational interval cover of the connected original Legendre chart.
    stack=[('',Q(0),Q(1))];leaves=[];visits=0;inclusions=0
    while stack:
        address,lo,hi=stack.pop();lam=interval(lo,hi);u=u0+lam*(U-u0);v=u0+lam*(V-u0)
        x=(1-u*v)/(u+v-2*u*v);ss=-u.log()/(2*pi*I);tt=-v.log()/(2*pi*I)
        vals=[-u.real,-u.imag,-v.real,-v.imag,x.real,x.imag,1-abs(x),
              1-abs(x*u),1-abs(x*v),ss.real,tt.real,arb(1)/2-ss.real,arb(1)/2-tt.real,
              (ss+tt).real,1-(ss+tt).real,abs(u+v-2*u*v),abs(1-u*v)]
        visits+=1;inclusions+=len(vals)
        if all(q>0 for q in vals):leaves.append(address);continue
        assert hi-lo>Q(1,2**20),('path gap',lo,hi,[str(q)for q in vals])
        mid=(lo+hi)/2;stack.extend([(address+'0',lo,mid),(address+'1',mid,hi)])
    return margins,{'leaves':leaves,'leaf_count':len(leaves),'visited':visits,'strict_inclusions':inclusions},[str(d3),str(d4)]

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--precision',type=int,default=256)
    ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-contracted-phase.json')
    args=ap.parse_args();ctx.prec=args.precision
    exact=algebra();K,U,V,s,t,source=reference();margins,path,gradients=branches(K,U,V,s,t)
    deps=['notes/research_mixed_contracted_phase.md','notes/research_mixed_wire_exact_contraction.md',
          'notes/research_three_vertex_mixed_reference_packet.md','notes/research_power_four_source_packet.md',
          'notes/research_three_four_source_interface.md','notes/research_three_chain_action_volume_calibration.md',
          'notes/exact_factorial_interpolation_and_complex_contours.md']
    result={'status':'passed','precision_bits':args.precision,'exact_identity_count':len(exact),'exact_identities':exact,
            'strict_comparison_count':len(margins),'margins':margins,'gram_calibration_path':path,
            'original_alternating_gradients':gradients,'inherited_reference':source,
            'scope':'Exact phase, symbol powers, rational critical identities and original connected branch checks. The written proof supplies the all-level source and constant; no complementary-index or global-sum estimate is checked.',
            'script_sha256':digest(Path(__file__)),'dependencies_sha256':{p:digest(ROOT/p)for p in deps}}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k]for k in ['status','exact_identity_count','strict_comparison_count','gram_calibration_path']},indent=2))

if __name__=='__main__':main()
