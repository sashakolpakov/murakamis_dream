#!/usr/bin/env python3
"""Exact algebra and outward endpoint checks for joint V3/V4 coercivity."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as Q
import argparse,json
import sympy as sp
from flint import arb,acb,ctx
ROOT=Path(__file__).resolve().parents[1]

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--precision',type=int,default=256)
 ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-three-four-joint-coercivity.json')
 args=ap.parse_args();ctx.prec=args.precision;identities=[]
 def exact(name,expr):
  assert sp.cancel(expr)==0,name;identities.append(name)
 a,s,t=sp.symbols('a s t');p=4*a**4-6*a**3+4*a**2-2*a+1
 B=a*a*(2*a-1)**2/(2*(a-1));k=a*a*B/(a*a+B);K=1/(1+2*a-4*a*a)
 U3=1-2*a;U4=(1-K)/(2*K)
 exact('geometric wire exponential',K+1/K-2+4*k)
 exact('power three stationary exponent',U3*(1-U3)-1/K+1)
 exact('power four stationary exponent',K*(1-U4*U4)-(1-U4)*(1-K*U4))
 numer,den=sp.fraction(sp.factor((1-K*U3)*(1-K*U4)-U3*U4*(1-K)**2))
 exact('opposite wire gradient exponent',sp.rem(numer,p,a))
 exact('phase polynomial difference',((s+t)-(s+t)**2-s+s*s-t+t*t)/2+s*t)
 aa,dx,dy,cx,cy=sp.symbols('aa dx dy cx cy',real=True)
 vs,vt,vx,vy=sp.symbols('vs vt vx vy',real=True)
 H=sp.Matrix([[aa+dx,aa,-dx,0],[aa,aa+dy,0,-dy],[-dx,0,dx+cx,0],[0,-dy,0,dy+cy]])
 v=sp.Matrix([vs,vt,vx,vy])
 exact('full unsummed real Hessian form',(v.T*H*v)[0]-aa*(vs+vt)**2-dx*(vs-vx)**2-dy*(vt-vy)**2-cx*vx**2-cy*vy**2)
 P=sp.Matrix([[sp.Rational(9,5),-sp.Rational(9,5)],[-sp.Rational(9,5),sp.Rational(9,5)+sp.Rational(10,3)]])-sp.eye(2)
 exact('unit coercivity determinant',P.det()-sp.Rational(1,15));exact('unit coercivity first minor',P[0,0]-sp.Rational(4,5))
 q,A=sp.symbols('q A',real=True)
 exact('coefficient angular derivative',sp.trigsimp(sp.diff(sp.sin(q)/(sp.cosh(A)-sp.cos(q)),q)-(sp.cosh(A)*sp.cos(q)-1)/(sp.cosh(A)-sp.cos(q))**2))
 recpath=ROOT/'repro/results/research-three-four-source-interface.json';rec=json.loads(recpath.read_text());assert rec['status']=='passed'
 dig=lambda path:sha256(path.read_bytes()).hexdigest()
 assert rec['script_sha256']==dig(ROOT/'experiments/check_three_four_source_interface.py')
 for path,h in rec['dependencies_sha256'].items():assert dig(ROOT/path)==h,path
 def r(x):
  if isinstance(x,Q):return arb(x.numerator)/x.denominator
  return arb(x)
 cr,ci=map(Q,rec['root_certificate']['center']);radius=r(Q(rec['root_certificate']['complex_disk_radius']))
 ar=acb(r(cr)+arb(0,radius),r(ci)+arb(0,radius));ii=acb(0,1);pi=arb.pi()
 kr=1/(1+2*ar-4*ar*ar);xr=kr.log()/(2*pi*ii);us=[1-2*ar,(1-kr)/(2*kr)];ss=[-u.log()/(2*pi*ii)for u in us]
 margins={}
 def pos(name,val):assert val>0,(name,str(val));margins[name]=str(val)
 def coeff(A,theta):return pi*theta.sin()/(A.cosh()-theta.cos())
 for name,height,angles,lower in [('wire',9*pi/50,[17*pi/50,2*pi/5],r(Q(10,3))),('index-wire',29*pi/100,[pi/10,14*pi/25],r(Q(9,5))),('extra index',11*pi/100,[pi/2,9*pi/10],r(Q(2,5)))]:
  for j,angle in enumerate(angles):pos(f'{name} endpoint {j}',coeff(height,angle)-lower)
 pos('disk product bound',r(Q(3,4))-(-11*pi/100).exp())
 pos('K upper half plane',kr.imag);pos('K inside disk',1-abs(kr))
 coords={'wire':xr,'index3':ss[0],'index4':ss[1]}
 bounds={'wire':(Q(17,100),Q(1,5),Q(7,100),Q(9,100)),
         'index3':(Q(1,4),Q(9,20),Q(-11,200),Q(3,200)),
         'index4':(Q(1,4),Q(9,20),Q(-11,200),Q(3,200))}
 for name,z in coords.items():
  lo,hi,lhi,uhi=bounds[name]
  for label,val in [('real lower',z.real-r(lo)),('real upper',r(hi)-z.real),('imaginary lower',z.imag-r(lhi)),('imaginary upper',r(uhi)-z.imag)]:pos(name+' '+label,val)
 gradients=[];wiregrad=[]
 for n,u,z in zip((3,4),us,ss):
  pos(f'U{n} logarithm lower',u.arg()+pi);pos(f'U{n} logarithm upper',-pi/2-u.arg())
  grad=(2*(2*pi*z).sin()).log()+ii*pi/2-2*pi*ii*z+kr.log()-(1-kr*u).log()
  if n==4:grad-=(2*(pi*z).sin()).log()+ii*pi/2-pi*ii*z
  assert grad.contains(0),(n,str(grad));pos(f'power {n} zero gradient lift',pi-abs(grad.imag));gradients.append(str(grad))
  wiregrad.append(2*pi*ii*z+(1-kr*u).log()-(1-kr).log()-pi*ii)
 total=sum(wiregrad);assert total.contains(0),str(total);pos('wire sum zero lift',pi-abs(total.imag))
 # More informative strict coordinate enclosures in the written reference table.
 table={'wire':(Q('.18299'),Q('.18301'),Q('.07871'),Q('.07873')),
        'index3':(Q('.3535'),Q('.3537'),Q('-.0169'),Q('-.0167')),
        'index4':(Q('.2845'),Q('.2846'),Q('-.0425'),Q('-.0423'))}
 for name,z in coords.items():
  a0,b0,c0,d0=table[name]
  for label,val in [('real min',z.real-r(a0)),('real max',r(b0)-z.real),('height min',z.imag-r(c0)),('height max',r(d0)-z.imag)]:pos('table '+name+' '+label,val)
 deps=['notes/research_mixed_three_four_joint_coercivity.md','notes/research_three_vertex_joint_concavity.md','notes/research_traced_three_vertex_endpoint.md','notes/research_power_four_finite_source.md','notes/research_root_pochhammer_interpolation.md','notes/research_three_four_source_interface.md']
 result={'status':'passed','precision_bits':args.precision,'exact_identity_count':len(identities),'exact_identities':identities,'strict_comparison_count':len(margins),'margins':margins,
         'reference_coordinates':{k:str(v)for k,v in coords.items()},'original_index_gradients':gradients,'wire_gradients':[str(g)for g in wiregrad],'wire_gradient_sum':str(total),
         'scope':'Exact local unsummed Hessian and scalar endpoint/reference checks. No mixed-word critical location, global contour coefficient, or knot inference.',
         'script_sha256':dig(Path(__file__)),'dependencies_sha256':{p:dig(ROOT/p)for p in deps},'inherited_reference':{'path':str(recpath.relative_to(ROOT)),'sha256':dig(recpath),'all_dependency_hashes_verified':True}}
 args.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k]for k in ('status','exact_identity_count','strict_comparison_count','reference_coordinates')},indent=2))
if __name__=='__main__':main()
