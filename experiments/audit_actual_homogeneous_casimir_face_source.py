#!/usr/bin/env python3
"""Original homogeneous coupon face source, including cyclic replacements.

No source is built by a Casimir interpolation of the original R matrix.
The physical matrix, finite face grid and homogeneous coefficient are
compared independently, retaining all endpoints and level cosets.
"""
import argparse
import itertools
import json
from pathlib import Path
import numpy as np
from audit_actual_small_circle_polynomial_face_insertion import Local,insertions,local_polynomials,mul,add
from audit_actual_signed_small_circle_face_kernel import kernel_poly

def homogeneous(loc,h,eps):
 out={};p=loc.p
 for j in range(loc.N):
  poly=insertions({(0,j,0):1},0,1,2,loc)[h]
  if eps:poly=kernel_poly(poly,0,1,2,loc,eps)
  for (a,i,b),v in poly.items():out[(a,i,loc.d-j,b)]=v
 return out

def local_normalizations():
 complete=signed_complete=phase=identity=0
 for N in range(3,13):
  loc=Local(N);p,q,d=loc.p,loc.q,loc.d;im=pow(loc.eta,N,p)
  S=[pow(im,j,p)*pow(q,-j*(j+1)//2,p)*loc.fac[j]%p for j in range(N)]
  expected={eps:{} for eps in (0,1,-1)}
  for a in range(d//2+1):
   D,P=local_polynomials(loc,a)
   left={(x,b,0,y):v for (x,b,y),v in D.items()}
   right={(x,0,c,y):v for (x,c,y),v in D.items()}
   forced={(x,0,0,y):v for (x,y),v in P.items()}
   v=mul(mul(left,right,p),forced,p)
   ka=1 if 2*a==d else 2;beta=S[2*a]*pow(S[a]**2,-1,p)%p
   for eps in expected:
    expected[eps]=add(expected[eps],v,p,N*ka*beta*beta*pow(loc.omega[a],eps,p)%p)
  for eps in expected:
   got={k:v*pow(loc.eta,eps*d*d,p)%p for k,v in homogeneous(loc,N,eps).items()}
   assert got==expected[eps],(N,'complete',eps)
   if eps: signed_complete+=len(got)
   else: complete+=len(got)
  H1=homogeneous(loc,1,0)
  assert H1=={(0,j,d-j,0):1 for j in range(N)};identity+=N
  for eps in (1,-1):
   HR=homogeneous(loc,1,eps)
   for (k,i,t,l),v in HR.items():
    mag=N*pow(S[i]*S[k]*S[l]*S[t],-1,p)%p
    phase0=pow(-1,k+l+1,p)*pow(q,eps*(k*l-(i+1)*(t+1)),p)%p
    assert v==mag*phase0%p,(N,eps,(i,k,l,t),v,mag*phase0%p)
    phase+=1
 return dict(status='PASS',complete_circle_polynomial_coefficients=complete,
             signed_complete_circle_coefficients=signed_complete,
             actual_four_face_crossing_phase_coefficients=phase,identity_kernel_coefficients=identity)

from audit_actual_braided_two_cut_source_adapter import original_crossings
from audit_actual_small_circle_polynomial_face_insertion import physical_colors
def physical_grid():
 counts=dict(entries=0,wrong_unwrapped_totals=0,arbitrary_entries=0,signed_entries=0,levels=0)
 for N in range(3,8):
  loc=Local(N);p,q,Q,d=loc.p,loc.q,loc.Q,loc.d;colors=physical_colors(loc);_,_,_,Rs=original_crossings(N)
  coupons=[]
  for h in sorted(set([1,2,N//2,N])):
   for eps in (0,1,-1):
    poly=homogeneous(loc,h,eps)
    op=colors[h]
    if eps:
     op=op@Rs[0 if eps>0 else 1][0]%p
     scalar=pow(loc.eta,eps*d*d,p)
     poly={k:v*scalar%p for k,v in poly.items()}
    coupons.append((poly,op,False,eps))
  poly={}
  for h,w in ((1,3),(2,7),(3,11)):
   for ex,v in homogeneous(loc,h,0).items():poly[ex]=(poly.get(ex,0)+w*v)%p
  op=(3*colors[1]+7*colors[2]+11*colors[3])%p
  coupons.append((poly,op,True,0))
  for poly,op,arbitrary,eps in coupons:
   for u in range(N):
    for v in range(N):
     x=-q*pow(Q,u,p)%p;y=-pow(q,-1,p)*pow(Q,-v,p)%p
     for r in range(N):
      s=(u+v-r)%N;delta=r-u;c=pow(Q,-delta,p)
      value=sum(co*pow(x,a,p)*pow(c,t,p)*pow(y,b,p) for (a,i,t,b),co in poly.items())%p
      predicted=value*pow(N,-1,p)*pow(q,-d*delta,p)*pow(c,-d,p)%p
      actual=int(op[r*N+s,u*N+v])
      assert actual==predicted,(N,u,v,r,s,arbitrary,eps,actual,predicted)
      if r+s!=u+v:assert actual==0;counts['wrong_unwrapped_totals']+=1
      counts['entries']+=1;counts['arbitrary_entries']+=arbitrary;counts['signed_entries']+=eps!=0
  counts['levels']+=1
 return dict(status='PASS',counts=counts)

def whole_case(N,boxes,ports,hs,epss,marked=1,width=2,pattern=False,grid=False):
 from audit_actual_original_marked_face_coefficient import morse_faces,substitute,evaluate
 from audit_general_odd_endpoint_matching_network import apply_pair
 loc=Local(N);p,q,Q,d=loc.p,loc.q,loc.Q,loc.d
 chart=morse_faces(width,boxes,marked);nf=chart['faces'];M=d//2
 colors=physical_colors(loc);_,_,_,Rs=original_crossings(N)
 imag=pow(loc.eta,N,p)
 S=[pow(imag,j,p)*pow(q,-j*(j+1)//2,p)*loc.fac[j]%p for j in range(N)]
 target=tuple(0 if f in (0,chart['v']) else d for f in range(nf))
 product={(0,)*nf:1};local_faces=[];coupons=[]
 for e,ids in enumerate(chart['circles']):
  if e in ports:
   pos=ports.index(e);h=hs[pos];eps=epss[pos]
   if h==-1:
    H={}
    for hh,w in ((1,3),(2,7),(3,11)):H=add(H,homogeneous(loc,hh,0),p,w)
    op=(3*colors[1]+7*colors[2]+11*colors[3])%p
   else:
    H=homogeneous(loc,h,eps);op=colors[h]
   if eps:
    H={n:v*pow(loc.eta,eps*d*d,p)%p for n,v in H.items()}
    op=op@Rs[0 if eps>0 else 1][0]%p
  else:
   a=e%(M+1) if pattern else M;eps=(-1,0,1)[e%3]
   D,P=local_polynomials(loc,a)
   H=mul(mul({(x,b,0,y):v for (x,b,y),v in D.items()},
             {(x,0,c,y):v for (x,c,y),v in D.items()},p),
             {(x,0,0,y):v for (x,y),v in P.items()},p)
   beta=S[2*a]*pow(S[a]**2,-1,p)%p;ka=1 if 2*a==d else 2
   scale=N*ka*beta**2*pow(loc.omega[a],eps,p)%p
   H={n:v*scale%p for n,v in H.items()}
   op=loc.h0[a]*pow(loc.omega[a],eps,p)*(loc.W[a][0]@loc.pi[a][0]%p)%p
  assert all(sum(n)==d and min(n)>=0 for n in H)
  local_faces.append(H);coupons.append(op)
  fac=substitute(H,ids,list(range(nf)),p)
  # All factors are polynomial, so target-exceeding terms can never return.
  fac={n:v for n,v in fac.items() if all(n[j]<=target[j] for j in range(nf))}
  product=mul(product,fac,p,cap=d)
  product={n:v for n,v in product.items() if all(n[j]<=target[j] for j in range(nf))}
 predicted=product.get(target,0)
 state=np.array([1],dtype=np.int64);mark=np.array([1],dtype=np.int64)
 marker=np.array([[pow(loc.x,j,p)*pow(N*N,-1,p)%p for j in range(N)] for i in range(N)],dtype=np.int64)
 for j in range(width):
  state=np.kron(state,loc.cup[0].reshape(-1))%p
  mark=np.kron(mark,(marker if j==marked else loc.cap[0]).reshape(-1))%p
 state=state.reshape((N,)*(2*width))
 for slot,op in zip(boxes,coupons):state=apply_pair(op,state,slot,N,p)
 actual=int(mark@state.reshape(-1)%p)
 assert actual==predicted,(N,boxes,ports,hs,epss,marked,actual,predicted)
 points=wrong=0
 if grid:
  average=0;logs={pow(Q,j,p):j for j in range(N)}
  for pp in itertools.product(range(N),repeat=nf-1):
   potentials=(0,)+pp
   L=[pow(q,chart['parity'][f] if N%2==0 else 0,p)*pow(Q,potentials[f],p)%p for f in range(nf)]
   value=1
   for ids,H in zip(chart['circles'],local_faces):
    xx,b,c,yy=[L[j] for j in ids]
    local_value=evaluate(H,[xx,b,c,yy],p)
    u=logs[pow(q,d,p)*xx*pow(b,-1,p)%p]
    v=logs[pow(q,d,p)*b*pow(yy,-1,p)%p]
    r=logs[pow(q,d,p)*xx*pow(c,-1,p)%p]
    s=logs[pow(q,d,p)*c*pow(yy,-1,p)%p]
    if u+v!=r+s:assert local_value==0;wrong+=1
    value=value*local_value%p
   for f in range(nf):value=value*pow(L[f],-target[f],p)%p
   average=(average+value)%p;points+=1
  average=average*pow(N,-(nf-1),p)%p
  assert average==actual,(N,ports,'original grid',average,actual)
 return dict(N=N,width=width,ports=ports,colors=hs,signs=epss,marked=marked,
             actual_source=actual,grid_points=points,wrong_unwrapped_grid_boxes=wrong,
             original_boxes=len(boxes),remaining_label_pattern=pattern)

def whole_sources():
 rows=[]
 for N in (3,4,5,6):
  for marked in (0,1):
   for ports,hs in (([0,2],[2,2]),([0,3],[1,1]),([0,1,3],[1,2,1]),([0,1,2,3],[1,1,1,1])):
    for epss in ([1]*len(ports),[-1 if j%2 else 1 for j in range(len(ports))],[0]*len(ports)):
     rows.append(whole_case(N,[1,0,2,1],ports,hs,epss,marked,
                 pattern=bool(marked),grid=N in (3,4) and marked==1 and len(ports)==4))
  rows.append(whole_case(N,[1,0,2,1],[0,2],[-1,2],[0,-1],0))
 for N in (3,4):
  for eps in (-1,1):rows.append(whole_case(N,[1,3,0,2,4,1,3],[3],[2],[eps],2,3))
  rows.append(whole_case(N,[1,3,0,2,4,1,3],[1,4],[N,2],[1,-1],2,3,pattern=True))
 return dict(original_fixed_sector_sources=len(rows),nonzero_sources=sum(r['actual_source']!=0 for r in rows),
             original_face_grid_points=sum(r['grid_points'] for r in rows),
             wrong_unwrapped_grid_boxes=sum(r['wrong_unwrapped_grid_boxes'] for r in rows),cases=rows)

def certified_local_gap():
 from audit_actual_original_marked_face_coefficient import morse_faces
 from audit_actual_smoothed_source_capacity_blocks import F
 from itertools import combinations
 import sympy as s
 import mpmath as m
 R=s.Rational
 D=morse_faces(3,[1,3,0,2,4,1,3])
 tri=[t for x,b,c,y in D['circles'] for t in [(x,b,y),(x,c,y)]]
 E={tuple(sorted((t[j],t[(j+1)%3]))) for t in tri for j in range(3)}
 C={1:(R(4,5),R(1,25),R(1,25)),2:(R(2,3),R(1,9),R(1,9)),3:(R(1,2),R(1,16),R(1,16)),4:(R(1),R(1,4),R(1,4)),5:(R(0),R(1),R(1)),6:(R(4,3),R(1,9),R(1,9)),7:(R(2),R(1),R(1))}
 assert D['v']==8 and D['circles'][3]==(4,2,7,5)
 assert morse_faces(3,[1,3,0,4,1,3])['faces']==8
 pairs=0
 for a,b in combinations(range(9),2):
  if(a,b)==(0,8):continue
  if a==0:
   X,Y,r=C[b]; slack=Y-r
  elif b==8:
   X,Y,r=C[a];slack=2-Y-r
  else:
   X,Y,r=C[a];U,V,t=C[b];slack=(X-U)**2+(Y-V)**2-(r+t)**2
  assert (slack==0) if (a,b)in E else (slack>0)
  pairs+=1
 P={}
 for a,b in E:
  if (a,b)==(0,8):P[a,b]=None
  elif a==0:P[a,b]=s.Matrix([C[b][0],0])
  elif b==8:P[a,b]=s.Matrix([C[a][0],2])
  else:
   X,Y,r=C[a];U,V,t=C[b];P[a,b]=s.Matrix([(t*X+r*U)/(r+t),(t*Y+r*V)/(r+t)])
 supports=0
 for row in tri:
  inc={tuple(sorted((row[j],row[(j+1)%3]))) for j in range(3)}
  pp=[P[e] for e in inc]
  if any(p is None for p in pp):
   pp=[p for p in pp if p is not None];X=pp[0][0];assert pp[1][0]==X and X in (0,2)
   for e,p in P.items():
    if p is not None and e not in inc:assert p[0]>0 if X==0 else p[0]<2;supports+=1
  else:
   A=s.Matrix.vstack(*[2*(p-pp[0]).T for p in pp[1:]])
   rhs=s.Matrix([p.dot(p)-pp[0].dot(pp[0]) for p in pp[1:]])
   z=A.inv()*rhs;r2=(z-pp[0]).dot(z-pp[0]);assert r2>0
   for e,p in P.items():
    if p is not None:
     val=s.factor((p-z).dot(p-z)-r2)
     assert val==0 if e in inc else val>0
     supports+=1
 m.mp.dps=60
 gap=F(4,9,1)+F(4,1,1)-m.log(9)
 # Outward-rounded finite sums; each Lobachevsky tail is <=1/(2M).
 from flint import arb,ctx
 ctx.prec=256
 M=100;pi=arb.pi()
 Lam=lambda t:sum(((2*k*t).sin()/(2*k*k) for k in range(1,M+1)),arb(0))
 def partialF(x,b,y):
  vals=list(map(arb,(x,b,y)));dd=arb(x*b+x*y+b*y).sqrt()
  th=[2*(v/dd).atan() for v in vals]
  return (sum((t*v.log() for t,v in zip(th,vals)),arb(0))+2*sum((Lam(t/2)+Lam((pi-t)/2) for t in th),arb(0)))/(2*pi)
 partial=partialF(4,9,1)+partialF(4,1,1)-arb(9).log()
 tail=6/(pi*M)
 assert partial-tail>arb('.45')
 return {'status':'PASS','actual_word':D['boxes'],'marked_faces':(0,8),'selected_port':3,'quartet':(4,9,1,1),'white_pairs':pairs,'shaded_supports':supports,'gap_diagnostic':str(gap),'interval_engine':'python-flint arb','precision_bits':ctx.prec,'100_term_ball':str(partial),'analytic_tail_bound':str(tail),'certified_gap_lower':str((partial-tail).lower()),'certified_gap_upper':str((partial+tail).upper())}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',default='experiments/actual_homogeneous_casimir_face_source_results.json');args=ap.parse_args()
 data=dict(status='PASS',local_normalizations=local_normalizations(),physical_grid=physical_grid(),
           whole_sources=whole_sources(),certified_local_gap=certified_local_gap(),
           scope='Exact original homogeneous root source for arbitrary polynomial coupons, all original endpoint totals, marks, both parity cosets, cyclic and disconnected replacements. No universal local-G positivity or far-color claim.')
 Path(args.output).write_text(json.dumps(data,indent=2)+'\n')
 summary={**data,'whole_sources':{k:v for k,v in data['whole_sources'].items() if k!='cases'}}
 print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
