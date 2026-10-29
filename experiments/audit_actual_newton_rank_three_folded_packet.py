#!/usr/bin/env python3
"""Original rank-three source and whole-cell Rouche profile certificates."""
import json
from pathlib import Path

from flint import arb,acb,ctx
import numpy as np
import sympy as sp

from audit_actual_two_cut_ports import balanced_data
from audit_actual_twist_endpoint_gaussian_certificate import original_case
ctx.prec=128
pi=arb.pi()

def coeff(t,kind):
 z=(2j*t).exp() if kind=='f' else (-2j*t).exp()
 if kind=='f':return [-3+7*z-3*z*z,(3-5*z)*(1-z)**3,-(1-z)**7]
 return [5*z-3,(3-7*z+3*z*z)*(1-z),-(1-z)**5]

def radius(tlo,thi,kind):
 u=(arb(tlo)+arb(thi))/2*pi +arb(0,(arb(thi)-arb(tlo))/2)*pi
 ab=coeff(acb(u),kind);mid=float(((arb(tlo)+arb(thi))/2*pi).mid())
 yy=np.exp((2j if kind=='f' else -2j)*mid)
 aa=[-3+7*yy-3*yy**2,(3-5*yy)*(1-yy)**3,-(1-yy)**7] if kind=='f' else [5*yy-3,(3-7*yy+3*yy**2)*(1-yy),-(1-yy)**5]
 cs=[acb(str(z.real),str(z.imag)) for z in np.roots([1]+aa)]
 discs=[]
 for c in cs:
  a,b,d=ab
  p=((c+a)*c+b)*c+d
  p1=(3*c+2*a)*c+b
  p2=6*c+2*a
  lo=p1.abs_lower()
  if not lo>0:return None
  rr=max(1e-24,4*float(p.abs_upper()/lo));r=arb(str(rr))
  if not lo*r > p.abs_upper()+p2.abs_upper()*r*r/2+r**3:return None
  discs.append(r)
 for i in range(3):
  for j in range(i):
   if not (cs[i]-cs[j]).abs_lower()>discs[i]+discs[j]:return None
 mags=[abs(c)+arb(0,r) for c,r in zip(cs,discs)]
 bound=mags[0].max(mags[1]).max(mags[2])
 if not bound.lower()>0:return None
 return bound

def integrate(a,b,n,which):
 out=arb(0);cells=0;stack=[(arb(a)+(arb(b)-arb(a))*i/n,arb(a)+(arb(b)-arb(a))*(i+1)/n,0) for i in range(n)]
 while stack:
  l,r,dep=stack.pop();rb=radius(l,r,'b');rf=radius(l,r,'f') if which==1 else None
  if rb is None or (which==1 and rf is None):
   if dep>=16:raise RuntimeError((l,r,which))
   m=(l+r)/2;stack.extend([(l,m,dep+1),(m,r,dep+1)]);continue
  if which==1:v=(rf/rb).log()
  else:
   u=(l+r)/2*pi+arb(0,(r-l)/2)*pi
   v=(rb/(2*u.sin())**2).log()
  out+=(r-l)*pi*v;cells+=1
 return out,cells

def exact_source(N):
 record=original_case(N)
 if N<3:return record
 prime,eta,q,E,F,K,pivot,Rp,Rm=balanced_data(N)
 d=N-1;Q=q*q%prime
 f=[1];fb=[1];Pb=[1]
 for i in range(1,N):
  f.append(f[-1]*(1-pow(Q,i,prime))%prime)
  fb.append(fb[-1]*(1-pow(Q,-i,prime))%prime)
  Pb.append(((1-pow(Q,-i,prime))**2*Pb[-1]+pow(Q,-i,prime))%prime)
 kval=[]
 for i in range(N):
  value=sum((-1)**j*pow(Q,j*(j+1)//2,prime)*f[i]
            *pow(f[j]*f[i-j]%prime,-1,prime)*Pb[d-j] for j in range(i+1))%prime
  kval.append(value)
 M=[f[i]**2*kval[i]%prime for i in range(N)]
 g=[pow(fb[k],4,prime)*M[d-k]%prime for k in range(N)]
 S0=sum(Pb)%prime
 assert sum(pow(Q,-j,prime)*Pb[j] for j in range(N))%prime==N*Q%prime
 assert g[0]==N*N*S0%prime
 assert g[1]==N*N*pow(Q,-1,prime)*((Q-3)*S0+2*N)%prime
 assert g[2]==N*N*pow(Q,-4,prime)*((Q**4-3*Q**3-3*Q**2+6*Q+3)*S0
                  +2*(Q**3+Q**2-3*Q-1)*N)%prime
 for k in range(3,N):
  Z=pow(Q,-k,prime)
  a=1+pow(Q,-1,prime)+pow(Q,-2,prime)-(4+pow(Q,-1,prime))*Z
  b=(-pow(Q,-3,prime)-pow(Q,-2,prime)-pow(Q,-1,prime)
     +(3+4*pow(Q,-1,prime))*Z-3*Q*Z*Z)*(1-Q*Z)
  c=pow(Q,-3,prime)*(1-Q*Z)*pow(1-Q*Q*Z,4,prime)
  assert g[k]==(a*g[k-1]+b*g[k-2]+c*g[k-3])%prime
 record['exact_backward_companion_and_ALL_source_currents']=True
 return record

def critical_polynomial():
 l,y,z=sp.symbols('l y z')
 p=l**3+(5*y-3)*l**2+(3-7*y+3*y*y)*(1-y)*l-(1-y)**5
 reflected=sp.together(l**3*p.subs({l:z*z/l,y:1/y})).as_numer_denom()[0]
 R=sp.resultant(p,reflected,l)
 elimination=sp.factor(sp.resultant(R,y*y-(2-z)*y+1,y))
 P6=z**6-9*z**5+29*z**4-38*z**3+10*z**2+2*z+1
 assert elimination==z**24*P6**2
 poly=sp.Poly(P6,z)
 assert poly.count_roots(0,1)==1 and poly.count_roots(1,4)==1
 assert poly.count_roots(sp.Rational(2,3),sp.Rational(7,10))==1
 assert poly.count_roots(sp.Rational(19,5),sp.Rational(77,20))==1
 return {'exact_modulus_resultant':str(P6),'two_positive_Sturm_intervals':['(2/3,7/10)','(19/5,77/20)']}

def interval_profiles():
 n=4096
 v,c1=integrate(arb('0.005'),arb('0.4'),n,1)
 uu=arb('0.0025')*pi+arb(0,arb('0.0025'))*pi
 aa=coeff(acb(uu),'f');R=1+abs(aa[0]).max(abs(aa[1])).max(abs(aa[2])).upper()
 near=arb('0.005')*pi*(R*arb(3)/2).log()
 first=v+near
 second,c2=integrate('0.4','0.5',n,2)
 assert first.upper()<arb('-0.0327')
 assert second.upper()<arb('-0.0114')
 return {'complete_Rouche_cells_first':c1,'complete_Rouche_cells_second':c2,
         'forward_backward_logratio_upper':str(first.upper()),
         'backward_tail_derivative_integral_upper':str(second.upper()),
         'method':'Every root disk validated for whole parameter intervals; not a sampling estimate.'}

if __name__=='__main__':
 records=[exact_source(N) for N in range(2,13)]
 algebra=critical_polynomial()
 profiles=interval_profiles()
 output={'status':'PASS','literal_original_source_families':records,
         'exact_critical_certificate':algebra,'certified_profile_overlap':profiles,
         'scope':'Actual folded rank-three source and whole-domain spectral envelopes; no topological/volume identification.'}
 Path(__file__).with_name('actual_newton_rank_three_folded_packet_results.json').write_text(json.dumps(output,indent=2)+'\n')
 print(f'PASS {len(records)} exact original source/backward-current levels; exact modulus resultant/Sturm; '
       f'{profiles["complete_Rouche_cells_first"]+profiles["complete_Rouche_cells_second"]} certified spectral cells')
