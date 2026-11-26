#!/usr/bin/env python3
"""Exact finite checks only; no large-level or invariant-volume inference."""
from collections import defaultdict
from pathlib import Path
import argparse, hashlib, json

names=('x','b','c','y','w','s','t'); n=len(names)
def clean(p): return {e:a for e,a in p.items() if a}
def const(a): return {(0,)*n:a} if a else {}
def variable(name):
 e=[0]*n;e[names.index(name)]=1;return {tuple(e):1}
def add(*ps):
 z=defaultdict(int)
 for p in ps:
  for e,a in p.items():z[e]+=a
 return clean(z)
def scale(p,k): return clean({e:a*k for e,a in p.items()})
def mul(p,q):
 z=defaultdict(int)
 for e,a in p.items():
  for f,b in q.items():z[tuple(i+j for i,j in zip(e,f))]+=a*b
 return clean(z)
def powp(p,k):
 z=const(1)
 for _ in range(k):z=mul(z,p)
 return z
def extract(p,name,k):
 i=names.index(name);z={}
 for e,a in p.items():
  if e[i]==k:
   f=list(e);f[i]=0;z[tuple(f)]=a
 return z
def subst(p,images):
 z={}
 for e,a in p.items():
  term=const(a)
  for name,k in zip(names,e):term=mul(term,powp(images.get(name,variable(name)),k))
  z=add(z,term)
 return z
x,b,c,y,w,s,t=map(variable,names)
I=[[const(int(i==j)) for j in range(3)] for i in range(3)]
def mm(A,B):return [[add(*(mul(A[i][k],B[k][j]) for k in range(3))) for j in range(3)] for i in range(3)]
A=add(x,y)
O=[[const(1),scale(A,-3),scale(mul(x,y),-3)], [{},const(-2),scale(A,-3)],[{},{},const(1)]]
O2=mm(O,O)
V=[[add(mul(powp(s,2),I[i][j]),mul(s,O[i][j]),O2[i][j],scale(I[i][j],-3)) for j in range(3)] for i in range(3)]
H={}
for j in range(3):
 for i in range(j+1):H=add(H,mul(V[i][j],mul(powp(b,i),powp(c,2-j))))
a=mul(add(s,const(-1)),add(s,const(2))); bb=powp(add(s,const(-1)),2)
formula=add(mul(a,add(powp(b,2),powp(c,2))),mul(bb,mul(b,c)),scale(mul(mul(add(const(1),scale(s,-1)),A),add(b,c)),3),scale(powp(A,2),9),scale(mul(add(s,const(2)),mul(x,y)),-3))
assert H==formula
parent=subst(H,{'b':w})
child=subst(H,{'x':b,'b':y,'c':x,'y':w,'s':t})
B=extract(mul(parent,child),'w',2)
def boundary_coefficient(p,degrees):
 z={}
 for e,a0 in p.items():
  if all(e[names.index(name)]==degrees.get(name,0) for name in ('x','b','c','y','w')):
   f=list(e)
   for name in ('x','b','c','y','w'):f[names.index(name)]=0
   z[tuple(f)]=a0
 return z
assert boundary_coefficient(B,{'b':2})==scale(a,9)
assert boundary_coefficient(B,{'c':2})==scale(a,9)
assert boundary_coefficient(B,{'b':1,'c':1})==scale(mul(add(const(4),scale(t,-1)),bb),3)
B00=subst(B,{'s':{},'t':{}});H00=subst(H,{'s':{}})
assert boundary_coefficient(B00,{'b':2})==const(-18)
assert boundary_coefficient(H00,{'b':2})==const(-2)
assert boundary_coefficient(B00,{'b':1,'c':1})==const(12)
assert boundary_coefficient(H00,{'b':1,'c':1})==const(1)
assert subst(B,{'s':const(-2)})==scale(mul(add(const(4),scale(t,-1)),subst(H,{'s':const(-2)})),3)
parser=argparse.ArgumentParser();parser.add_argument('--certificate',type=Path,default=Path('/private/tmp/murakamis_dream-publication/experiments/actual_singleton_sector_obstruction_certificate.json'));parser.add_argument('--output',type=Path,default=Path('/private/tmp/md-triangular-block-full-source-check-results.json'));args=parser.parse_args()
data=json.loads(args.certificate.read_text());src=data['source']
assert src['faces'][34]==[29,50,22]
assert src['faces'][97]==[29,22,45]
assert src['ports'][28]==[29,50,45,22]
assert src['matching_faces'][28]==[34,97]
assert src['ports'][32]==[0,50,16,29]
assert src['matching_faces'][32]==[39,62]
assert set(src['faces'][39])=={0,29,50}
assert set(src['protected'])=={29,50}
assert set(src['matching_faces'][28]).isdisjoint(src['matching_faces'][32])
result={'scope':'Exact N=3 local resolvent/stellar contraction and R54 removed-face incidence only. No asymptotic or signed-source lower bound.','level':3,'H3_matrix_resolvent_matches_formula':True,'full_scalar_contraction_counterexample':{'spectra':[0,0],'old_b2':-2,'new_b2':-18,'old_bc':1,'new_bc':12,'forced_scalar':9},'complete_node_identity_exact':True,'removed_R54_face':34,'removed_R54_crossing':28,'retained_R54_bad_crossing':32,'certificate_sha256':hashlib.sha256(args.certificate.read_bytes()).hexdigest()}
args.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
