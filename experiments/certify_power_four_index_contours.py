#!/usr/bin/env python3
"""Outward index-current and alias certificate for the exact power-four sum.

Every accepted leaf covers its full exact rational rectangle. The
reference comes from the validated alternating three/four geometry.
The real triangle complement is a separate proof input.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import time
from flint import arb,acb,ctx

ROOT=Path(__file__).resolve().parents[1]
A,B,LOW,HIGH=Q(1,5),Q(21,50),Q(-11,200),Q(3,200)
I=acb(0,1)

def ball(x):
    if isinstance(x,Q):return arb(x.numerator)/x.denominator
    return arb(x)
def interval(a,b):return ball(a).union(ball(b))
def abs_upper(x):return max(abs(x.lower()),abs(x.upper()))
def phase(s,t,K):
    pi=arb.pi();u=(-2*pi*I*s).exp();v=(-2*pi*I*t).exp()
    return ((u*v).polylog(2)-u.polylog(2)-v.polylog(2)+pi*pi/6
            -(K*u).polylog(2)-(K*v).polylog(2)+2*K.polylog(2))/(2*pi*I)+(s+t)*K.log()
def derivative(s,t,K):
    u=(-2*arb.pi()*I*s).exp();v=(-2*arb.pi()*I*t).exp()
    common=(1-u*v).log()
    return (K.log()+common-(1-u).log()-(1-K*u).log(),
            K.log()+common-(1-v).log()-(1-K*v).log())
def side(k,v):
    if k<2:return acb(ball(A if k==0 else B),ball(LOW)+ball(HIGH-LOW)*v),I*ball(HIGH-LOW)
    return acb(ball(A)+ball(B-A)*v,ball(LOW if k==2 else HIGH)),acb(ball(B-A))

def reference():
    path=ROOT/'repro/results/research-three-four-source-interface.json'
    rec=json.loads(path.read_text());assert rec['status']=='passed'
    assert rec['script_sha256']==sha256((ROOT/'experiments/check_three_four_source_interface.py').read_bytes()).hexdigest()
    for p,h in rec['dependencies_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    re,im=map(Q,rec['root_certificate']['center']);rad=ball(Q(rec['root_certificate']['complex_disk_radius']))
    a=acb(ball(re)+arb(0,rad),ball(im)+arb(0,rad));b=a*a*(2*a-1)**2/(2*(a-1))
    x=(a*a*b/(a*a+b)).sqrt().asin()/arb.pi();K=(2*arb.pi()*I*x).exp();Z=2*K/(1-K)
    z=Z.log()/(2*arb.pi()*I)
    return K,z,x,{'record':str(path.relative_to(ROOT)),'sha256':sha256(path.read_bytes()).hexdigest(),'all_dependency_hashes_verified':True}

def scalar_checks(K,z,x):
    pi=arb.pi();out=[]
    def positive(name,v):
        assert v>0,(name,str(v));out.append({'name':name,'margin':str(v)})
    positive('parameter argument lower',K.arg()-pi/5)
    positive('parameter argument upper',2*pi/5-K.arg())
    positive('denominator product radius',arb(7)/10-abs(K)*(2*pi*ball(HIGH)).exp())
    positive('critical real lower',z.real-ball(A));positive('critical real upper',ball(B)-z.real)
    positive('critical height lower',z.imag-ball(LOW));positive('critical height upper',ball(HIGH)-z.imag)
    grad=derivative(z,z,K)[0]
    positive('critical zero logarithmic lift',pi-abs(grad.imag))
    positive('critical total action exceeds .8562',(phase(z,z,K)-2*pi*I*x).real-arb(4281)/5000)
    positive('cotangent sine lower',(2*pi/5).sin()-arb(19)/20)
    positive('cotangent hyperbolic numerator',arb(9)/25-(11*pi/100).sinh())
    positive('small-square cotangent upper',arb(7)/5-1/(pi/5).tan())
    positive('small-square cotangent lower',(2*pi/5).sin()/((11*pi/100).cosh()+(2*pi/5).cos())-arb(2)/3)
    positive('whole-square cotangent lower',(21*pi/25).sin()/((11*pi/100).cosh()-(21*pi/25).cos())-arb(6)/25)
    gamma,zeta=arb(36)/95,arb(252)/475
    delta=(1-zeta*zeta)/((arb(14)/5)*(1+gamma*gamma))
    positive('positive cotangent-sum Hessian reserve',pi*delta-arb(1)/4)
    positive('nonpositive cotangent-sum Hessian reserve',pi*arb(6)/25-arb(1)/4)
    positive('upper alias gap exceeds .05',2*pi*ball(HIGH)-arb(1)/25-arb(1)/20)
    return out

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision',type=int,default=192)
    parser.add_argument('--output',type=Path,default=ROOT/'repro/results/research-power-four-index-contours.json')
    parser.add_argument('--max-visited',type=int,default=100000)
    args=parser.parse_args();ctx.prec=args.precision
    K,z,x,source=reference();scalars=scalar_checks(K,z,x);fc=phase(z,z,K).real
    real_path=ROOT/'repro/results/research-power-four-real-complement.json'
    real_record=json.loads(real_path.read_text());assert real_record['status']=='passed'
    assert real_record['script_sha256']==sha256((ROOT/'experiments/check_power_four_real_complement.py').read_bytes()).hexdigest()
    for p,h in real_record['dependencies_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    real_input={'record':str(real_path.relative_to(ROOT)),'sha256':sha256(real_path.read_bytes()).hexdigest(),'all_dependency_hashes_verified':True}
    visited=0;results=[];start=time.monotonic()
    for j in range(4):
        for k in range(4):
            leaves=[];stack=[('',((Q(0),Q(1)),(Q(0),Q(1))))]
            threshold=ball(Q(1,200) if min(j,k)<2 else Q(-1,25))
            while stack:
                path,box=stack.pop();visited+=1;assert visited<=args.max_visited,'budget exhausted: no certificate'
                points=[interval(a,b) for a,b in box]
                centers=[ball((a+b)/2) for a,b in box]
                radii=[ball((b-a)/2) for a,b in box]
                try:
                    s,ds=side(j,points[0]);t,dt=side(k,points[1]);fs,ft=derivative(s,t,K)
                    sm,_=side(j,centers[0]);tm,_=side(k,centers[1])
                    costs=[radii[0]*abs_upper((fs*ds).real),radii[1]*abs_upper((ft*dt).real)]
                    margin=fc-phase(sm,tm,K).real-sum(costs)-threshold
                    passed=margin>0
                except (ValueError,ZeroDivisionError):passed=False;costs=None
                if passed:leaves.append(path);continue
                if costs is not None and all(c.is_finite() for c in costs):axis=max(range(2),key=lambda a:float(costs[a].upper()))
                else:axis=max(range(2),key=lambda a:float(box[a][1]-box[a][0]))
                lo,hi=box[axis];assert hi-lo>Q(1,2**24),('unproved',j,k,box)
                mid=(lo+hi)/2
                for bit,(a,b) in enumerate(((lo,mid),(mid,hi))):
                    child=list(box);child[axis]=(a,b);stack.append((path+str(2*axis+bit),tuple(child)))
            results.append({'s_side':j,'t_side':k,'leaves':leaves})
            print('completed',j,k,'leaves',len(leaves),flush=True)
    deps=['notes/research_power_four_source_packet.md','notes/research_power_four_real_complement.md',
          'notes/research_power_four_finite_source.md','notes/research_three_four_source_interface.md',
          'notes/research_exterior_crossing_phase.md',
          'notes/research_root_pochhammer_interpolation.md','notes/exact_factorial_interpolation_and_complex_contours.md']
    result={'status':'passed','precision_bits':args.precision,'domains':results,'domain_count':len(results),
            'leaf_count':sum(len(d['leaves']) for d in results),'visited':visited,
            'index_rectangle':{'real':[str(A),str(B)],'imaginary':[str(LOW),str(HIGH)]},
            'vertical_product_gap':'1/200','horizontal_product_excess':'1/25',
            'scalar_checks':scalars,'scalar_count':len(scalars),'reference':source,'real_complement_input':real_input,
            'elapsed_seconds':time.monotonic()-start,
            'scope':'Outward full index-side products, alias reserves, analytic-Hessian scalar constants and reference branch. The real triangle complement and final source assembly are separate written inputs.',
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','domain_count','leaf_count','visited','scalar_count','elapsed_seconds']}))

if __name__=='__main__':main()
