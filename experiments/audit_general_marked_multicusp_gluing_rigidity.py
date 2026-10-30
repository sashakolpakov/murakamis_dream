#!/usr/bin/env python3
"""Actual three-cusp marked gluing Jacobians and exact peripheral reduction."""
import sympy as s
import json
from pathlib import Path
from itertools import product
from collections import defaultdict
from audit_general_marked_positive_gluing_certificate import DSU
TET={}
for half in range(2):
 for j in range(4):
  eq=[j,(j+1)%4]
  if half:eq.reverse()
  TET[(half,j)]=['A','B']+eq
PAIR={}
def glue(a,b,m):
 PAIR[a]=(b,m);PAIR[b]=(a,{v:k for k,v in m.items()})
for h in range(2):
 for j in range(4):
  a=(h,(j-1)%4);b=(h,j)
  ia=next(i for i,v in enumerate(TET[a]) if v not in ['A','B',j])
  ib=next(i for i,v in enumerate(TET[b]) if v not in ['A','B',j])
  glue((a,ia),(b,ib),{v:v for v in ['A','B',j]})
for j in range(4):
 omitted=1 if j%2 else 0
 names=[v for i,v in enumerate(TET[(0,j)]) if i!=omitted]
 glue(((0,j),omitted),((1,j),omitted),{v:v for v in names})
for h in range(2):
 glue(((h,0),1),((h,2),1),{'A':'A',0:3,1:2})
 glue(((h,1),0),((h,3),0),{'B':'B',1:0,2:3})
ED,VE=DSU(),DSU()
PED=[]
for (t,missing),((u,missing2),m) in PAIR.items():
 p={i:TET[u].index(m[v]) for i,v in enumerate(TET[t]) if i!=missing}
 for i in p:
  VE.join((t,i),(u,p[i]))
  if (t,missing)<(u,missing2):PED.append(((t,i,missing),(u,p[i],missing2)))
  for j in p:
   if i<j:ED.join((t,i,j),(u,min(p[i],p[j]),max(p[i],p[j])))
TS=sorted(TET);TI={t:i for i,t in enumerate(TS)}
typeedge=lambda a,b:0 if tuple(sorted((a,b))) in [(0,1),(2,3)] else (1 if tuple(sorted((a,b))) in [(0,2),(1,3)] else 2)
evec=[s.Matrix([[1,0]]),s.Matrix([[0,1]]),s.Matrix([[-1,-1]])]
rows={}
for t in TS:
 for i in range(4):
  for j in range(i+1,4):
   e=ED.find((t,i,j));rows.setdefault(e,s.zeros(1,16))
   rows[e][0,2*TI[t]:2*TI[t]+2]+=evec[typeedge(i,j)]
EM=s.Matrix.vstack(*rows.values());Omega=s.diag(*([s.Matrix([[0,1],[-1,0]])]*8))
assert EM.rank()==5 and EM*Omega*EM.T==s.zeros(8)
EB=EM[list(EM.T.rref()[1]),:]
CUSPS=defaultdict(list)
for t in TS:
 for i in range(4):CUSPS[VE.find((t,i))].append((t,i))
curves=[]
for cusp,nodes in CUSPS.items():
 edges=[e for e in PED if VE.find(e[0][:2])==cusp]
 B=s.zeros(len(nodes),len(edges));ni={v:i for i,v in enumerate(nodes)}
 for k,(h0,h1) in enumerate(edges):B[ni[h0[:2]],k]+=1;B[ni[h1[:2]],k]-=1
 cycles=B.nullspace();delta=[]
 for cy in cycles:
  flows=defaultdict(lambda:s.Integer(0))
  for coeff,(h0,h1) in zip(cy,edges):flows[h0]+=coeff;flows[h1]-=coeff
  dv=s.zeros(1,16)
  for t,v in nodes:
   f0,f1,f2=[j for j in range(4) if j!=v]
   vv=(-1)**v*(flows[(t,v,f1)]*evec[typeedge(v,f2)]-flows[(t,v,f2)]*evec[typeedge(v,f1)])
   dv[0,2*TI[t]:2*TI[t]+2]+=vv
  assert dv*Omega*EM.T==s.zeros(1,8)
  delta.append(dv)
 found=False
 for mu in delta:
  for lam in delta:
   p=(mu*Omega*lam.T)[0]
   if abs(p)==2:
    curves.append((mu,lam if p==2 else -lam));found=True;break
  if found:break
 assert found
MM=s.Matrix.vstack(EB,*[m for m,l in curves]);assert MM.rank()==8 and MM*Omega*MM.T==s.zeros(8)
AA=MM[:,::2];BB=MM[:,1::2];tt=(-1+s.I)/2
JJ=AA+tt*BB
assert s.factor(JJ.det())==16*s.I
D=JJ.inv()[:,5:]
LC=s.Matrix.vstack(*[l for m,l in curves]);slope=s.simplify((LC[:,::2]+tt*LC[:,1::2])*D)
assert slope==s.diag(s.I/2,s.I/2,2*s.I)
assert all((m*Omega*l.T)[0]==2 for m,l in curves)
for i,(mu,lam) in enumerate(curves):
 for j,(mu2,lam2) in enumerate(curves):
  if i!=j:
   assert all((x*Omega*y.T)[0]==0 for x in (mu,lam) for y in (mu2,lam2))
marked=[]
for choices in product((0,1),repeat=3):
 rows=s.Matrix.vstack(EB,*[curves[i][choice] for i,choice in enumerate(choices)])
 assert rows.rank()==8 and rows*Omega*rows.T==s.zeros(8)
 jac=rows[:,::2]+tt*rows[:,1::2]
 determinant=s.factor(jac.det())
 assert determinant!=0
 marked.append({'fixed_paths':['longitude' if c else 'meridian' for c in choices],
                'exact_Jacobian_determinant':str(determinant)})
# Commuting affine maps: (exp U-1)*l=(exp V-1)*m.
# Over dual numbers this forces l0*dU=m0*dV with the exact multiplier logs.
u,v,m,l=s.symbols('u v m l',nonzero=True)
affine_mu=s.Matrix([[1+u,m],[0,1]])
affine_la=s.Matrix([[1+v,l],[0,1]])
assert s.expand((affine_mu*affine_la-affine_la*affine_mu)[0,1])==l*u-m*v
# An invariant Artin flag alone does not fix its eigenvalue.
e=s.symbols('e'); unipotent=s.Matrix([[1,1],[0,1]]); flag=s.Matrix([1,e])
assert (unipotent*flag-(1+e)*flag).applyfunc(s.expand)==s.Matrix([0,-e**2])
# Prescribing eigenvalue one forces e=0 through the first coordinate.
assert unipotent*flag-flag==s.Matrix([e,0])
result={'status':'PASS','actual_ideal_fixture':{'tetrahedra':8,'global_edges':8,'torus_cusps':3},
 'edge_rank':5,'marked_rank':8,'edge_and_marked_isotropy':True,
 'primitive_normal_curve_pairings':[2,2,2],
 'meridian_Jacobian_determinant':str(JJ.det()),
 'marked_cusp_derivative':[[str(slope[i,j]) for j in range(3)] for i in range(3)],
 'mixed_meridian_longitude_choices':marked,
 'primitive_peripheral_rows':[{'meridian':[int(x) for x in m],'longitude':[int(x) for x in l]} for m,l in curves],
 'commuting_similarity_first_order_identity':str(l*u-m*v),
 'exact_eigenvalue_eliminates_nilpotent_flag_motion':True,
 'scope':'Own multi-cusp positive marked gluing rigidity and decorated representation germ. No source critical-scheme or quantum period comparison.'}
Path(__file__).with_name('general_marked_multicusp_gluing_rigidity_results.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS actual 8-tetrahedron/3-cusp edge and peripheral rows, 8 marked Jacobians, exact diagonal cusp derivative, Artin flag distinction')
