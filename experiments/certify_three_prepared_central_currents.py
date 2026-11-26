#!/usr/bin/env python3
"""Concavity certificates for actual prepared-cap index and homotopy faces.

Floating optimization proposes rational supporting points only. Acceptance
uses exact rational domains and outward values/gradients; global concavity
of the original joint phase supplies the whole-domain inequality.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from itertools import product
import argparse,json,time
import numpy as np
from scipy.special import spence
from scipy.optimize import minimize
from flint import arb,acb,ctx
ROOT=Path(__file__).resolve().parents[1];I=acb(0,1)
BOUNDS=[(Q(7,50),Q(1,5)),(Q(0),Q(9,5)),(Q(1,4),Q(9,20)),
        (Q(1,4),Q(9,20)),(Q(97,600),Q(103,600))]
BASE=[Q(10135869,10**8),-Q(97895510,10**8),Q(300831,10**8),-Q(629803,10**8)]
def r(q):return arb(q.numerator)/q.denominator if isinstance(q,Q)else arb(q)
def primitive(z):
 p=arb.pi();return -I*p*(z*z-z)/2+I*(2*p*I*z).exp().polylog(2)/(2*p)-I*p/12
def function(point,heights):
 p=arb.pi();yh=arb(2).log()/(2*p)
 x,tau,s,t=[acb(r(point[j]),r(heights[j]))for j in range(4)]
 y=acb(r(point[4]),yh+r(heights[4]));X=(2*p*I*x).exp();Y=(2*p*I*y).exp()
 U=(-2*p*I*s).exp();V=(-2*p*I*t).exp()
 den=lambda z,Z:((Z*(-2*p*I*z).exp()).polylog(2)-Z.polylog(2))/(2*p*I)
 retained=primitive(s+t)+I*p*((s+t)-(s+t)**2)/2+s*X.log()+t*Y.log()-den(s,X)-den(t,Y)-p*I*(x+y)
 cap=-primitive(arb(1)/2-x+tau/(2*p))-primitive(arb(1)/2-x-tau/(2*p))-2*primitive(x)
 cap-=4*primitive(arb(1)/4+tau/(4*p))+4*primitive(arb(1)/4-tau/(4*p))
 cap+=3*I*tau*tau/(4*p)-I*tau
 cp=(p*x+tau/2).cos().log();cm=(p*x-tau/2).cos().log()
 bx=cp+cm-2*(p*x).sin().log()
 bt=(cp-cm)/(2*p)-((tau/2).tan()+1/(tau/2).cos()).log()/p+3*I*tau/(2*p)-I
 px=2*p*I*s+(1-X*U).log()-(1-X).log()-p*I
 py=2*p*I*t+(1-Y*V).log()-(1-Y).log()-p*I
 fs=X.log()+(1-U*V).log()-(1-X*U).log()
 ft=Y.log()+(1-U*V).log()-(1-Y*V).log()
 return(cap+retained).real,[z.real for z in (bx+px,bt,fs,ft,py)]
def numeric(point,heights):
 p=np.pi;x,tau,s,t=[float(point[j])+1j*float(heights[j])for j in range(4)]
 y=float(point[4])+1j*(np.log(2)/(2*p)+float(heights[4]));X=np.exp(2j*p*x);Y=np.exp(2j*p*y)
 li=lambda z:spence(1-z)
 J=lambda z:-1j*p*(z*z-z)/2+1j*li(np.exp(2j*p*z))/(2*p)-1j*p/12
 den=lambda z,Z:(li(Z*np.exp(-2j*p*z))-li(Z))/(2j*p)
 f=J(s+t)+1j*p*((s+t)-(s+t)**2)/2+s*np.log(X)+t*np.log(Y)-den(s,X)-den(t,Y)-1j*p*(x+y)
 f+=-J(.5-x+tau/(2*p))-J(.5-x-tau/(2*p))-2*J(x)-4*J(.25+tau/(4*p))-4*J(.25-tau/(4*p))+3j*tau*tau/(4*p)-1j*tau
 return f.real
def domains():
 for axis,end,hs,ht,hy in product((2,3),(0,1),(-Q(1,125),Q(1,125)),(-Q(17,1000),Q(3,250)),(-Q(1,200),Q(1,200))):
  h=BASE[:];h[2]=hs;h[3]=ht
  yield ('index_side',axis,end,str(hs),str(ht),str(hy)),axis,end,h+[hy],Q(19107,10000)
 for hs,ht,hy in product((-Q(1,125),Q(1,125)),(-Q(17,1000),Q(3,250)),(-Q(1,200),Q(1,200))):
  h=BASE[:];h[2]=hs;h[3]=ht
  yield ('alias',str(hs),str(ht),str(hy)),None,None,h+[hy],Q(39,20)
 for axis,end,hy in product(range(4),(0,1),(-Q(1,200),Q(1,200))):
  yield ('translation_face',axis,end,str(hy)),axis,end,BASE+[hy],Q(19107,10000)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=160)
 ap.add_argument('--output',default='repro/results/research-three-prepared-central-currents.json')
 args=ap.parse_args();ctx.prec=args.precision;start=time.monotonic();saved=[]
 for key,axis,end,heights,target in domains():
  bounds=list(BOUNDS)
  if axis is not None:bounds[axis]=(bounds[axis][end],bounds[axis][end])
  free=[j for j in range(5)if bounds[j][0]!=bounds[j][1]]
  center=[Q(1773,10000),Q(1534,1000),Q(351,1000),Q(325,1000),Q(1,6)]
  if axis is not None:center[axis]=bounds[axis][0]
  def extend(z):
   pt=list(map(float,center))
   for j,v in zip(free,z):pt[j]=v
   return pt
  sol=minimize(lambda z:-numeric(extend(z),heights),[float(center[j])for j in free],
               method='Nelder-Mead',bounds=[tuple(map(float,bounds[j]))for j in free],
               options={'maxiter':6000,'xatol':1e-12,'fatol':1e-13})
  proposal=list(center)
  for j,v in zip(free,sol.x):proposal[j]=min(bounds[j][1],max(bounds[j][0],Q(str(float(v)))))
  value,grad=function(proposal,heights)
  upper=value+sum(max((g*r(a-z)).upper(),(g*r(b-z)).upper())for g,(a,b),z in zip(grad,bounds,proposal))
  assert upper<r(target),(key,upper,proposal,grad)
  saved.append({'domain':list(key),'bounds':[[str(a),str(b)]for a,b in bounds],
                'heights':[str(h)for h in heights],'support_point':[str(z)for z in proposal],
                'threshold':str(target),'support_upper':str(upper)})
  print(key,str(upper),flush=True)
 checks={
  'new s contour contains certified root heights':Q(-1,125)<Q(-6301,10**6)and Q(6995,10**6)<Q(1,125),
  'new t contour contains certified root heights':Q(-17,1000)<Q(-15251,10**6)and Q(10401,10**6)<Q(3,250),
  'alias reserve':r(Q(39,20))-2*arb.pi()/125<r(Q(19107,10000)),
  'critical wire boundary gap':r(Q(27,40))*r(Q(21,1000))**2>r(Q(1,4000)),
  'critical index boundary gap':r(Q(3,8))*r(Q(3,50))**2>r(Q(1,4000)),
  'critical trace boundary gap':r(Q(7,880))*r(Q(1,4))**2>r(Q(1,4000)),
 }
 assert all(checks.values()),checks
 deps=['notes/research_three_vertex_joint_concavity.md','notes/research_three_cap_central_source.md',
       'notes/research_three_prepared_cap_quantified_source.md',
       'notes/research_three_phase_graph_transform.md','repro/results/research-three-phase-graph-transform.json']
 result={'status':'passed','precision_bits':args.precision,'domain_count':len(saved),'domains':saved,
         'scalar_checks':list(checks),'elapsed_seconds':time.monotonic()-start,
         'scope':'Concave supporting-plane bounds for actual joint source sides, aliases and base-height translation faces on outgoing coordinate square±.005.',
         'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
         'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest()for p in deps}}
 (ROOT/args.output).write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:result[k]for k in ('status','domain_count','elapsed_seconds')}))
if __name__=='__main__':main()
