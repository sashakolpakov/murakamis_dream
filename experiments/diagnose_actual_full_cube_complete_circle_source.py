#!/usr/bin/env python3
"""Full original cube finite diagnostic, never an asymptotic/positivity test.

The complete L_N=V h V^dagger P resolution is source-exact; these complex128
contractions have no proved growing-level error bound and remain diagnostics.
"""
import sys,itertools,math,time,json
from pathlib import Path
import numpy as np
from audit_actual_trivalent_complete_circle_vertex_kernel import ordered_cube_graph

def app(A,v,axis):
 return np.moveaxis(np.tensordot(A,np.moveaxis(v,axis,0),axes=(1,0)),0,axis)

def contract(ts):
 ts=[(v,tuple(ids)) for v,ids in ts]
 while len(ts)>1:
  choices=[]
  for i,(a,li) in enumerate(ts):
   for j,(b,lj) in enumerate(ts[i+1:],i+1):
    c=set(li)&set(lj)
    if not c:continue
    size=math.prod(a.shape[x] for x,l in enumerate(li) if l not in c)*math.prod(b.shape[x] for x,l in enumerate(lj) if l not in c)
    choices.append((size,-len(c),i,j,c))
  _,_,i,j,c=min(choices,key=lambda z:z[:4]);a,li=ts[i];b,lj=ts[j];c=sorted(c)
  out=np.tensordot(a,b,axes=([li.index(x) for x in c],[lj.index(x) for x in c]))
  labs=tuple(x for x in li if x not in c)+tuple(x for x in lj if x not in c)
  ts=[v for k,v in enumerate(ts) if k not in (i,j)]+[(out,labs)]
 return ts[0][0].item()

def data(N):
 d=N-1;q=np.exp(1j*np.pi/N);Q=q*q;x=q**d
 E=np.diag([Q**(-a)-1 for a in range(1,N)],1);F=np.diag([1-Q**a for a in range(1,N)],-1);K=np.diag([x*Q**(-a) for a in range(N)]);I=np.eye(N)
 Et=np.kron(E,K)+np.kron(I,E);Ft=np.kron(F,I)+np.kron(np.linalg.inv(K),F);Kt=np.kron(K,K)
 O=Ft@Et+q*Kt+q**-1*np.linalg.inv(Kt)
 P=np.zeros((N*N,N*N))
 for a,b in itertools.product(range(N),repeat=2):P[b*N+a,a*N+b]=1
 sine=[1.]
 for r in range(1,N):sine.append(sine[-1]*2*np.sin(np.pi*r/N))
 cols=[];weights=[];labs=[]
 for T in range(2*d+1):
  low,off=min(T,2*d-T),max(0,T-d);ids=[(off+a)*N+T-off-a for a in range(low+1)]
  for j in range(low+1):
   if not j<=d-j<=low:continue
   node=2*np.cos((2*j+1)*np.pi/N);v=np.zeros(N*N,dtype=complex);v[ids[0]]=1;prev=0;cur=1
   for a in range(low):
    nex=((node-O[ids[a],ids[a]])*cur-(O[ids[a],ids[a-1]]*prev if a else 0))/O[ids[a],ids[a+1]]
    v[ids[a+1]]=nex;prev,cur=cur,nex
   assert np.max(abs(O@v-node*v))<1e-6
   h=sine[low]**2/sine[low-j]**2 if j==d-j else 2*sine[low]**2/(sine[low-j]*sine[low+j-d])
   cols.append(v);weights.append(h);labs.append((T,j))
 V=np.array(cols).T;h=np.array(weights);r=len(h)
 J=np.zeros((N*N,)*3,dtype=complex);ell=J.copy();mark=J.copy()
 for a,b,c in itertools.product(range(N),repeat=3):
  ids=(a*N+b,(d-b)*N+c,(d-c)*N+d-a)
  J[ids]=N**3*x**(a+b+c-3*d);ell[ids]=N**-3*x**(a+b+c)
 for a,b,c in itertools.product(range(N),repeat=3):
  # two ordinary caps fix colors 23,45; outer m restrictable after full closure, keep every outer color now
  for a6 in range(N):
   ids=(a*N+b,(d-b)*N+c,(d-c)*N+a6)
   mark[ids]=N**-4*x**(a6+b+c)
 B=J;W=ell;M=mark
 for ax in range(3):
  B=app(V.conj().T@P,B,ax);W=app(V.T,W,ax);M=app(V.T,M,ax)
  factors=[1,1,1];factors[ax]=r;scale=np.sqrt(h).reshape(factors)
  B*=scale;W*=scale;M*=scale
 return B,W,M,labs

def run(N):
 t=time.time();B,W,M,labs=data(N);ports,black,marked=ordered_cube_graph();val=contract([(B if v in black else M if v==marked else W,ids) for v,ids in ports.items()]);print(N,len(labs),'full',val,'rate',np.log(abs(val))/N,'sec',time.time()-t,flush=True)
 # compare reflected ordinary coefficient tensors after all permutations/individual phase gauges later
 return B,W,M,labs,val
if __name__=='__main__':
 rows=[]
 for N in map(int,sys.argv[1:] or [3,4,5,6,7,8,9]):
  B,W,M,labs,value=run(N)
  m=(N-1)//2;ids=[i for i,(_,j) in enumerate(labs) if j==m]
  ports,black,marked=ordered_cube_graph()
  central=contract([((B if v in black else M if v==marked else W)[np.ix_(ids,ids,ids)],edges) for v,edges in ports.items()])
  rows.append({'N':N,'full_CD_dimension':len(labs),'full_raw_source_real':float(value.real),'full_raw_source_imag':float(value.imag),'relative_imaginary_residual':float(abs(value.imag)/max(abs(value),1e-300)),'central_folded_joint_sector_real':float(central.real),'full_to_central_complex_ratio':[float((value/central).real),float((value/central).imag)]})
 result={'status':'DIAGNOSTIC','precision':'IEEE complex128; growing cancellation/conditioning is not controlled here.','rows':rows,'source_scope':'Literal entire untwisted original cube CD source with unrestricted exposed mark; all12 circle colors retained.','limits':'Finite floating-point values are guidance only. They do not prove reality, positivity, dominance, a uniform error bound, or a full cube volume limit.'}
 Path(__file__).with_name('actual_full_cube_complete_circle_diagnostic_results.json').write_text(json.dumps(result,indent=2)+'\n')
