#!/usr/bin/env python3
"""All colors and original mark in a literal 21-circle reflected cube double.

Conjugate-root evaluations are independent exact cyclotomic specializations.
The finite-field audit tests identities, not positivity from field elements.
"""
import itertools,json,math
from pathlib import Path
import numpy as np
import audit_actual_nc_morse_graph_first_normal_source_reduction as normal
from audit_actual_nc_three_port_source_sewing import graft
from audit_actual_trivalent_complete_circle_vertex_kernel import ordered_cube_graph,theta_graph,axis_apply,contract
from audit_actual_two_cut_ports import balanced_data
EP={0:0,1:10,2:11,3:3,4:7,5:8,6:6,7:4,8:5,9:9,10:1,11:2}
class Full:
 def __init__(self,N,bar=False):
  base=balanced_data(N)
  if bar:
   saved=normal.balanced_data
   normal.balanced_data=lambda n:(base[0],pow(base[1],-1,base[0]),pow(base[2],-1,base[0]),*base[3:])
   try:self.L=normal.Local(N)
   finally:normal.balanced_data=saved
  else:self.L=normal.Local(N)
  l=self.L;self.N=N;self.p=l.p;self.M=(N-1)//2
  self.W=np.concatenate([l.W[j][0] for j in range(self.M+1)],axis=1)
  self.pi=np.concatenate([l.h0[j]*l.pi[j][0]%l.p for j in range(self.M+1)],axis=0)
  # Independently reconstruct the ORIGINAL full complete circle by its
  # Casimir polynomial, including every double-node first normal.
  K=l.Kpair[0];Ki=np.diag([pow(int(z),-1,l.p) for z in np.diag(K)])
  Omega=(l.Fpair[0]@l.Epair[0]+l.q*K+pow(l.q,-1,l.p)*Ki)%l.p
  old=np.eye(N*N,dtype=np.int64);now=Omega.copy()
  for _ in range(2,N):old,now=now,(Omega@now-old)%l.p
  circle=(-1)**(N-1)*now%l.p
  assert np.array_equal(self.W@self.pi%l.p,circle)
  self.ids={};off=0
  for j in range(self.M+1):self.ids[j]=list(range(off,off+2*j+1));off+=2*j+1
  self.colors=sum(([j]*(2*j+1) for j in range(self.M+1)),[])
  self.T=[]
  for initial,A in ((l.J[0],self.pi),(l.ellS[0],self.W.T),(l.marker,self.W.T)):
   val=initial
   for k in range(3):val=axis_apply(A,val,k,l.p)
   self.T.append(val)
 def value(self,graph,powers=None,fixed=None):
  p=self.p;ports,black,mark=graph;ts=[];fixed=fixed or {};powers=powers or [0]*(3*len(ports)//2)
  for v,es in ports.items():
   val=self.T[0 if v in black else 2 if v==mark else 1]
   for k,e in enumerate(es):
    if v in black and powers[e]:
     shape=[1,1,1];shape[k]=len(self.colors)
     val=val*np.array([pow(self.L.omega[j],powers[e],p) for j in self.colors]).reshape(shape)%p
    if e in fixed:val=np.take(val,self.ids[fixed[e]],axis=k)
   ts.append((val,es))
  return contract(ts,p)

def level(N):
 a=Full(N);bar=Full(N,True);p=a.p;m=a.M;g=ordered_cube_graph()
 P=a.L.P[0]
 assert np.array_equal(bar.L.cup[0].T%p,N*N*a.L.cap[0]%p)
 assert np.array_equal(N*N*bar.L.cap[0].T%p,a.L.cup[0])
 for j in range(m+1):
  left=a.L.h0[j]*a.L.W[j][0]%p@a.L.pi[j][0]%p
  conjugate=bar.L.h0[j]*bar.L.W[j][0]%p@bar.L.pi[j][0]%p
  assert np.array_equal(P@conjugate.T%p@P%p,left)
  assert a.L.omega[j]*bar.L.omega[j]%p==1
 rows=[]
 for name,es in [('untwisted',[0]*12),('signed',[1,-2,0,1,-1,3,0,-1,2,0,0,1])]:
  bs=[0]*12
  for e,f in EP.items():bs[f]=-es[e]
  double,labels,powers=graft(g,g,0,4,[m]*12,[m]*12,es,bs)
  rhs=0;count=0;nonzero=0
  for js in itertools.product(range(m+1),repeat=3):
   z=a.value(g,es,dict(zip((0,1,2),js)))
   w=a.value(g,bs,dict(zip((0,10,11),js)))
   if sum(js)<N-1:
    assert z==w==0
    continue
   zb=bar.value(g,es,dict(zip((0,1,2),js)))
   assert w==zb,(N,js,z,w,zb)
   theta=a.value(theta_graph(),fixed=dict(enumerate(js)))
   rhs=(rhs+z*w*pow(theta,-1,p))%p;count+=1;nonzero+=bool(z)
  actual=a.value(double,powers)
  assert actual==rhs,(N,name,actual,rhs)
  rows.append(dict(twists=name,supported_boundary_triples=count,
                   nonzero_field_boundary_packets=nonzero,
                   complete_twenty_one_circle_source=actual))
 return dict(N=N,prime=p,full_root_reflection_sectors=m+1,
             direct_full_color_doubles=rows)


def main():
 graph=ordered_cube_graph();ports,black,_=graph
 vertex_map={4:0,0:4,2:5,1:6,6:1,3:7,5:2,7:3}
 assert {vertex_map[v] for v in black}==set(ports)-black
 for v,edges in ports.items():
  target=ports[vertex_map[v]]
  assert tuple(EP[e] for e in edges) in [target[k:]+target[:k] for k in range(3)]
 assert tuple(EP[e] for e in ports[0])==ports[4]
 rows=[level(N) for N in range(2,8)]
 result=dict(status='PASS',levels=rows,
             scope='All colors, actual original mark, both parities; no central cycle projections. Positivity is proved analytically, not inferred from finite-field residues.')
 Path(__file__).with_name('actual_planar_three_port_reflection_double_results.json').write_text(json.dumps(result,indent=2)+'\n')
 print('PASS 6 levels / 12 full 21-circle sources / complete Hermite reflection and conjugate boundary packets')


if __name__=='__main__':main()
