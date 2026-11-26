#!/usr/bin/env python3
"""Outward full-index currents for the undeleted V3 kernel at K34.

The finite certificate covers complete rational rectangles, not samples.
Real-index complement control is a separate written/source input.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import time
import sympy as sp
from flint import arb,acb,ctx

ROOT=Path(__file__).resolve().parents[1]
A,B,LOW,HIGH=Q(1,4),Q(9,20),Q(-3,100),Q(3,200)
I=acb(0,1)

def ball(x):
    return arb(x.numerator)/x.denominator if isinstance(x,Q) else arb(x)
def interval(a,b):return ball(a).union(ball(b))
def abs_upper(x):return max(abs(x.lower()),abs(x.upper()))
def digest(p):return sha256(p.read_bytes()).hexdigest()
def phase(s,t,K):
    pi=arb.pi();u=(-2*pi*I*s).exp();v=(-2*pi*I*t).exp()
    return ((u*v).polylog(2)-pi*pi/6-(K*u).polylog(2)
            -(K*v).polylog(2)+2*K.polylog(2))/(2*pi*I)+(s+t)*K.log()
def derivative(s,t,K):
    u=(-2*arb.pi()*I*s).exp();v=(-2*arb.pi()*I*t).exp()
    common=K.log()+(1-u*v).log()
    return common-(1-K*u).log(),common-(1-K*v).log()
def side(k,v):
    if k<2:return acb(ball(A if k==0 else B),ball(LOW)+ball(HIGH-LOW)*v),I*ball(HIGH-LOW)
    return acb(ball(A)+ball(B-A)*v,ball(LOW if k==2 else HIGH)),acb(ball(B-A))

def reference():
    path=ROOT/'repro/results/research-three-four-source-interface.json'
    rec=json.loads(path.read_text());assert rec['status']=='passed'
    assert rec['script_sha256']==digest(ROOT/'experiments/check_three_four_source_interface.py')
    for p,h in rec['dependencies_sha256'].items():assert digest(ROOT/p)==h,p
    re,im=map(Q,rec['root_certificate']['center']);rad=ball(Q(rec['root_certificate']['complex_disk_radius']))
    a=acb(ball(re)+arb(0,rad),ball(im)+arb(0,rad))
    K=1/(1+2*a-4*a*a);u=1-2*a;x=K.log()/(2*arb.pi()*I);z=-u.log()/(2*arb.pi()*I)
    return K,z,x,{'record':str(path.relative_to(ROOT)),'sha256':digest(path),'all_dependency_hashes_verified':True}

def exact_checks():
    a=sp.symbols('a');k=1/(1+2*a-4*a*a);u=1-2*a
    b=a*a*(2*a-1)**2/(2*(a-1));wire=a*a*b/(a*a+b)
    checks={'geometric wire exponential':k+1/k-2+4*wire,
            'original stationary exponent':k*(1-u*u)-(1-k*u)}
    for name,v in checks.items():assert sp.cancel(v)==0,name
    return list(checks)

def scalar_checks(K,z,x):
    pi=arb.pi();out=[]
    def positive(name,v):
        assert v>0,(name,str(v));out.append({'name':name,'margin':str(v)})
    positive('reference first quadrant real',K.real);positive('reference first quadrant imaginary',K.imag)
    positive('reference disk',1-abs(K))
    positive('parameter argument lower',K.arg()-pi/5)
    positive('parameter argument upper',2*pi/5-K.arg())
    positive('denominator product radius',arb(7)/10-abs(K)*(2*pi*ball(HIGH)).exp())
    positive('critical real lower',z.real-ball(A));positive('critical real upper',ball(B)-z.real)
    positive('critical height lower',z.imag-ball(LOW));positive('critical height upper',ball(HIGH)-z.imag)
    grad=derivative(z,z,K)[0]
    assert grad.contains(0)
    positive('critical zero logarithmic lift',pi-abs(grad.imag))
    positive('critical total action exceeds .6562',(phase(z,z,K)-2*pi*I*x).real-arb(3281)/5000)
    d0=2*pi*ball(A)-K.arg();d1=2*pi*ball(B)-K.arg()
    positive('rotated angle lower',d0);positive('rotated angle upper',pi-d1)
    positive('minimum rotated sine at left',d1.sin()-d0.sin())
    rmin=abs(K)*(2*pi*ball(LOW)).exp();rmax=abs(K)*(2*pi*ball(HIGH)).exp()
    positive('whole-rectangle Hessian reserve',2*pi*rmin*d0.sin()/(1+rmax)**2-arb(2)/5)
    positive('upper alias gap exceeds .07',2*pi*ball(HIGH)-arb(1)/50-arb(7)/100)
    return out

def calibration_path(K,z):
    """A connected diagonal path to the already calibrated homogeneous chart."""
    pi=arb.pi();u0=acb(-arb(1)/2,-arb(3).sqrt()/2);u1=(-2*pi*I*z).exp()
    leaves=[];stack=[('',Q(0),Q(1))];count=0
    while stack:
        address,lo,hi=stack.pop();v=interval(lo,hi);u=u0+(u1-u0)*v
        X=1/(1+u-u*u);x=X.log()/(2*pi*I);s=-u.log()/(2*pi*I)
        W=(u*u-2*u-1)/2;tau=-I*(W+(W-1).sqrt()*(W+1).sqrt()).log()
        ap=acb(arb(1)/2)-x+tau/(2*pi);am=acb(arb(1)/2)-x-tau/(2*pi)
        vals=[-u.real,-u.imag,X.real,X.imag,1-abs(X),1-abs(X*u),
              x.real,arb(1)/4-x.real,x.imag,W.imag,s.real,arb(1)/2-s.real,
              ap.real,1-ap.real,am.real,1-am.real,abs(1-2*u)]
        count+=len(vals)
        if all(q>0 for q in vals):leaves.append(address);continue
        assert hi-lo>Q(1,2**16),('path failed',lo,hi,[str(q)for q in vals])
        mid=(lo+hi)/2;stack.extend([(address+'0',lo,mid),(address+'1',mid,hi)])
    return {'leaves':leaves,'leaf_count':len(leaves),'strict_inclusions_checked':count,
            'scope':'Connected original index/angular branch chart to homogeneity; real action constant is inherited, not numerically estimated.'}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision',type=int,default=256)
    parser.add_argument('--output',type=Path,default=ROOT/'repro/results/research-three-vertex-mixed-reference.json')
    parser.add_argument('--max-visited',type=int,default=100000)
    args=parser.parse_args();ctx.prec=args.precision;start=time.monotonic()
    exact=exact_checks();K,z,x,source=reference();scalars=scalar_checks(K,z,x)
    calibration=calibration_path(K,z);fc=phase(z,z,K).real
    real_path=ROOT/'repro/results/research-three-vertex-alternating-complement.json'
    real_record=json.loads(real_path.read_text());assert real_record['status']=='passed'
    assert real_record['script_sha256']==digest(ROOT/'experiments/certify_three_vertex_alternating_complement.py')
    for p,h in real_record['dependencies_sha256'].items():assert digest(ROOT/p)==h,p
    real_input={'record':str(real_path.relative_to(ROOT)),'sha256':digest(real_path),'all_dependency_hashes_verified':True}
    visited=0;results=[]
    for j in range(4):
        for k in range(4):
            leaves=[];stack=[('',((Q(0),Q(1)),(Q(0),Q(1))))]
            threshold=ball(Q(1,1000) if min(j,k)<2 else Q(-1,50))
            while stack:
                path,box=stack.pop();visited+=1;assert visited<=args.max_visited,'budget exhausted: no certificate'
                points=[interval(a,b)for a,b in box];centers=[ball((a+b)/2)for a,b in box]
                radii=[ball((b-a)/2)for a,b in box]
                try:
                    s,ds=side(j,points[0]);t,dt=side(k,points[1]);fs,ft=derivative(s,t,K)
                    sm,_=side(j,centers[0]);tm,_=side(k,centers[1])
                    costs=[radii[0]*abs_upper((fs*ds).real),radii[1]*abs_upper((ft*dt).real)]
                    margin=fc-phase(sm,tm,K).real-sum(costs)-threshold;passed=margin>0
                except (ValueError,ZeroDivisionError):passed=False;costs=None
                if passed:leaves.append(path);continue
                axis=max(range(2),key=lambda a:float(costs[a].upper())) if costs is not None and all(c.is_finite()for c in costs) else max(range(2),key=lambda a:float(box[a][1]-box[a][0]))
                lo,hi=box[axis];assert hi-lo>Q(1,2**24),('unproved',j,k,box)
                mid=(lo+hi)/2
                for bit,(a,b)in enumerate(((lo,mid),(mid,hi))):
                    child=list(box);child[axis]=(a,b);stack.append((path+str(2*axis+bit),tuple(child)))
            results.append({'s_side':j,'t_side':k,'leaves':leaves})
            print('completed',j,k,'leaves',len(leaves),flush=True)
    deps=['notes/research_three_vertex_mixed_reference_packet.md','notes/research_traced_three_vertex_endpoint.md',
          'notes/research_three_vertex_alternating_reference_complement.md',
          'notes/research_three_four_source_interface.md','notes/research_three_chain_action_volume_calibration.md',
          'notes/research_root_pochhammer_interpolation.md','notes/exact_factorial_interpolation_and_complex_contours.md']
    result={'status':'passed','precision_bits':args.precision,'domains':results,'domain_count':len(results),
            'leaf_count':sum(len(d['leaves'])for d in results),'visited':visited,
            'index_rectangle':{'real':[str(A),str(B)],'imaginary':[str(LOW),str(HIGH)]},
            'vertical_product_gap':'1/1000','horizontal_product_excess':'1/50',
            'exact_identities':exact,'exact_identity_count':len(exact),'scalar_checks':scalars,'scalar_count':len(scalars),
            'reference':source,'real_complement_input':real_input,'calibration_path':calibration,
            'critical_index':str(z),'critical_action':str(phase(z,z,K)-2*arb.pi()*I*x),
            'elapsed_seconds':time.monotonic()-start,
            'scope':'Outward complete index-side products, aliases, whole-rectangle Hessian constants and connected calibration chart. The real triangle complement and all-level source assembly are written proof inputs.',
            'script_sha256':digest(Path(__file__)),'dependencies_sha256':{p:digest(ROOT/p)for p in deps}}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k]for k in ['status','domain_count','leaf_count','visited','scalar_count','elapsed_seconds']}))

if __name__=='__main__':main()
