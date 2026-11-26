#!/usr/bin/env python3
"""Verify signed peripheral homology through recorded local moves.

Uses only combinatorial t3mlite moves and exact cubic arithmetic. The
recorded peripheral updates are checked by a local disk-homology test;
no native peripheral-curve update or hyperbolic solver is called.
"""
from __future__ import annotations
import argparse
import collections
from fractions import Fraction as Q
import hashlib
import itertools
import json
from pathlib import Path
import sympy as s
from snappy.exterior_to_link.mcomplex_with_memory import McomplexWithMemory
from snappy.snap.t3mlite.arrow import Arrow
ROOT=Path(__file__).resolve().parents[1]
FIXTURE=ROOT/'repro/fixtures/research-mixed-peripheral-transport.json'
BASE=ROOT/'repro/fixtures/research-mixed-two-crossing-subdivision.json'
D=json.loads(FIXTURE.read_text()); BASE_DATA=json.loads(BASE.read_text())
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-peripheral-transport.json')
ARGS=parser.parse_args()
CHECKS=collections.Counter()
faces=[14,13,11,7]
X=s.Symbol('X'); POLY=X**3+2*X**2+1

def reduced(expr):
 num,den=s.fraction(s.cancel(expr))
 return s.rem(s.rem(num,POLY,X)*s.invert(s.rem(den,POLY,X),POLY,X),POLY,X)

def equal(a,b=0,category='cubic_identities'):
 assert reduced(a-b)==0,(a,b)
 CHECKS[category]+=1

def diagram_faces(pd):
    """Four tetrahedra per crossing, as in the diagram crossing-ball proof."""
    ends = collections.defaultdict(list)
    for c, row in enumerate(pd):
        for j, arc in enumerate(row):
            ends[arc].append((c, j))
    assert all(len(es) == 2 for es in ends.values())
    neighbors = [[None]*4 for _ in range(4*len(pd))]
    for c in range(len(pd)):
        for j in range(4):
            neighbors[4*c+j][0] = 4*c+3-j
            neighbors[4*c+j][1] = 4*c+(j ^ 1)
    for es in ends.values():
        for (c, j), (d, k) in [es, es[::-1]]:
            neighbors[4*c+(j+1)%4][2] = 4*d+(k+2)%4
            neighbors[4*c+(j+2)%4][3] = 4*d+(k+1)%4
    return [[ns, [[0, 1, 3, 2] for _ in range(4)]] for ns in neighbors]


def face_data(T):
    T.rebuild()
    faces = [14, 13, 11, 7]
    return [[[tet.Neighbor[f].Index for f in faces],
             [list(tet.Gluing[f].tuple()) for f in faces]] for tet in T]


data=face_data

def local_boundary_map(old,new,removed,created,survivor,move,index,edge,face):
 # Label vertices of the abstract bipyramid before applying any identifications
 # on its boundary. Thus repeated global cusp labels do not merge these labels.
 parent={(t,v):(t,v) for t in removed for v in range(4)}
 def find(x):
  if parent[x]!=x:parent[x]=find(parent[x])
  return parent[x]
 def join(a,b):parent[find(a)]=find(b)
 internal=set()
 if move=='two_to_three':
  f=faces.index(face);n,p=old[index][0][f],old[index][1][f]
  internal.update([(index,f),(n,p[f])])
  for v in range(4):
   if v!=f:join((index,v),(n,p[v]))
  pole_nodes=[(index,f),(n,p[f])]
 else:
  # Propagate the distinguished edge around the old star.
  start_vertices=[v for v in range(4) if edge&(1<<v)]
  edge_vertices={index:set(start_vertices)};todo=[index]
  while todo:
   t=todo.pop()
   for f in range(4):
    if f in edge_vertices[t]:continue
    n,p=old[t][0][f],old[t][1][f]
    assert n in removed
    internal.add((t,f))
    for v in range(4):
     if v!=f:join((t,v),(n,p[v]))
    target={p[v] for v in edge_vertices[t]}
    if n not in edge_vertices:edge_vertices[n]=target;todo.append(n)
    else:assert target==edge_vertices[n]
  pole_nodes=[(index,v) for v in start_vertices]
 roots=sorted({find(x) for x in parent});assert len(roots)==5
 labels={x:roots.index(find(x)) for x in parent}
 poles={labels[x] for x in pole_nodes};assert len(poles)==2
 ring=set(range(5))-poles
 old_boundary={}
 for t in removed:
  for f in range(4):
   if (t,f) not in internal:
    key=frozenset(labels[t,v] for v in range(4) if v!=f)
    assert key not in old_boundary
    old_boundary[key]=(t,f)
 assert len(old_boundary)==6
 subsets=([poles|set(e) for e in itertools.combinations(ring,2)]
          if move=='two_to_three' else [ring|{p} for p in poles])
 inverse_survivor={n:o for o,n in survivor.items()}
 candidates={}
 for t in created:
  constraints={}
  for f in range(4):
   n,p=new[t][0][f],new[t][1][f]
   if n in inverse_survivor:
    oo=inverse_survivor[n];ff=p[f]
    ot,op=old[oo][0][ff],old[oo][1][ff];assert ot in removed
    for v in range(4):
     if v!=f:
      lab=labels[ot,op[p[v]]]
      assert v not in constraints or constraints[v]==lab
      constraints[v]=lab
  candidates[t]=[q for subset in subsets for q in itertools.permutations(sorted(subset))
                 if all(q[v]==lab for v,lab in constraints.items())]
  assert candidates[t]
 solutions=[]
 created=sorted(created)
 for choice in itertools.product(*(candidates[t] for t in created)):
  assignment=dict(zip(created,choice));valid=True;bd={}
  for t in created:
   q=assignment[t]
   for f in range(4):
    key=frozenset(q[v] for v in range(4) if v!=f)
    n,p=new[t][0][f],new[t][1][f]
    if key in old_boundary:
     ot,of=old_boundary[key];bd[ot,of]=(t,f)
     on,op=old[ot][0][of],old[ot][1][of]
     if on in survivor:
      if n!=survivor[on] or p[f]!=op[of]:valid=False;break
      for v in range(4):
       if v==f:continue
       ov=next(j for j in range(4) if j!=of and labels[ot,j]==q[v])
       if p[v]!=op[ov]:valid=False;break
     else:
      if n not in assignment:valid=False;break
      target_key=frozenset(assignment[n][v] for v in range(4) if v!=p[f])
      if old_boundary.get(target_key)!=(on,op[of]):valid=False;break
      for v in range(4):
       if v==f:continue
       ov=next(j for j in range(4) if j!=of and labels[ot,j]==q[v])
       if assignment[n][p[v]]!=labels[on,op[ov]]:valid=False;break
    else:
     if n not in assignment:valid=False;break
     if any(q[v]!=assignment[n][p[v]] for v in range(4) if v!=f):valid=False;break
   if not valid:break
  if valid:solutions.append((assignment,bd,labels))
 assert len(solutions)==1,(move,removed,created,len(solutions))
 return solutions[0]
# Original oriented curves in the crossing-circle cusp. Entries are fluxes
# out of the three sides f != v of the triangle (tetrahedron, vertex).
# The four-entry convention includes a zero in the omitted position f=v.
MU=[(20,3,[0,-1,1,0]),(21,2,[0,1,0,-1]),
    (33,3,[-1,0,1,0]),(34,2,[1,0,0,-1])]
LONGITUDE=[(20,3,[1,0,-1,0]),(23,2,[-1,0,0,1]),
 (24,3,[1,0,-1,0]),(27,2,[-1,0,0,1]),
 (30,2,[0,-1,0,1]),(31,3,[0,1,-1,0]),
 (34,2,[0,-1,0,1]),(35,3,[0,1,-1,0])]
raw=diagram_faces(BASE_DATA['pd']); assert raw==BASE_DATA['raw_gluing']
def diagram_arc_walk(chain):
 entries={(t,v):flux for t,v,flux in chain}
 start=next(iter(entries));at=start;seen=set();arcs=[]
 while at not in seen:
  seen.add(at);t,v=at;flux=entries[at]
  assert sorted(flux)==[-1,0,0,1]
  f=flux.index(1);n,p=raw[t][0][f],raw[t][1][f]
  if f>=2:
   slot=(t%4-(1 if f==2 else 2))%4
   arcs.append(BASE_DATA['pd'][t//4][slot])
  at=(n,p[v]);assert entries[at][p[f]]==-1
 assert at==start and seen==set(entries)
 return arcs
assert diagram_arc_walk(MU)==[17,17]
assert diagram_arc_walk(LONGITUDE)==[16,15,14,17]
CHECKS['original_diagram_curve_walks']=2
raw_curves=[[0]*16 for _ in range(4*len(raw))]
for row,curve in [(0,MU),(2,LONGITUDE)]:
 for t,v,flux in curve: raw_curves[4*t+row][4*v:4*v+4]=flux
T=McomplexWithMemory(raw); original=list(T)
aux_vertex=T[20].Class[1<<3]
assert aux_vertex.link_genus()==1
raw_aux={(t.Index,v) for t in T for v in range(4)
         if t.Class[1<<v] is aux_vertex}
for number,(move,edge,face,index) in enumerate(D['collapses']):
 T._relabel_tetrahedra(); before=list(T)
 a=Arrow(edge,face,T[index]); e=a.Tetrahedron.Class[edge]
 assert e.distinct() and e.Vertices[0]!=e.Vertices[1]
 assert sorted(v.link_genus() for v in e.Vertices)==([0,0] if number==0 else [0,1])
 # The whole star, not only the collapsed endpoints, misses this cusp.
 for corner in e.Corners:
  for v in range(4):
   assert (original.index(corner.Tetrahedron),v) not in raw_aux
 assert T.smash_star(e)
 CHECKS['collapses_disjoint_from_auxiliary_cusp']+=1
assert data(T)==D['initial']['gluing']
indices=[original.index(t) for t in T]
assert indices==D['raw_to_ideal_original_indices']
cs=[[int((old,v) in raw_aux) for v in range(4)] for old in indices]
pc=[raw_curves[4*old+row] for old in indices for row in range(4)]
assert cs==D['initial']['cusps'];assert pc==D['initial']['curves']

def closed(gluing,cusps,curves):
 for t in range(len(gluing)):
  for v in range(4):
   for row in range(4):
    coeff=curves[4*t+row][4*v:4*v+4]
    if cusps[t][v]!=1:
     assert coeff==[0]*4;continue
    assert coeff[v]==0 and sum(coeff)==0
    for f in range(4):
     if f==v:continue
     n,p=gluing[t][0][f],gluing[t][1][f]
     assert cusps[n][p[v]]==1
     assert coeff[f]+curves[4*n+row][4*p[v]+p[f]]==0
    CHECKS['closed_triangle_fluxes']+=1
closed(data(T),cs,pc)
for rec in D['records']:
 move,edge,face,index=rec['move']
 T._relabel_tetrahedra(); before=list(T); old=data(T)
 a=Arrow(edge,face,T[index])
 if move=='two_to_three':
  assert a.Tetrahedron.Neighbor[face] is not a.Tetrahedron
 elif move=='three_to_two':
  e=a.Tetrahedron.Class[edge]
  assert e.IntOrBdry=='int' and e.distinct() and e.valence()==3
 else:raise AssertionError(move)
 assert getattr(T,move)(a,must_succeed=True)
 after=list(T);new=data(T);assert new==rec['gluing']
 survivor={i:after.index(t) for i,t in enumerate(before) if t in after}
 removed=set(range(len(before)))-set(survivor)
 created=set(range(len(after)))-set(survivor.values())
 labels,boundary,oldlabels=local_boundary_map(old,new,removed,created,survivor,move,index,edge,face)
 assert sorted([[t,list(q)] for t,q in labels.items()])==sorted(rec['local_vertex_labels'])
 assert sorted([[ot,of,nt,nf] for (ot,of),(nt,nf) in boundary.items()])==sorted(rec['boundary_faces'])
 nc,np=rec['cusps'],rec['curves']
 for ot,nt in survivor.items():
  assert cs[ot]==nc[nt]
  assert pc[4*ot:4*ot+4]==np[4*nt:4*nt+4]
  CHECKS['unchanged_outside_tetrahedra']+=1
 for (ot,of),(nt,nf) in boundary.items():
  for ov in range(4):
   if ov==of:continue
   nv=labels[nt].index(oldlabels[ot,ov])
   assert cs[ot][ov]==nc[nt][nv]
   for row in range(4):
    assert pc[4*ot+row][4*ov+of]==np[4*nt+row][4*nv+nf]
    CHECKS['individual_boundary_fluxes']+=1
 closed(new,nc,np);cs,pc=nc,np
 CHECKS['peripheral_pachner_moves']+=1
assert len(T)==8
assert sorted(v.link_genus() for v in T.Vertices)==[1,1]

# A complete positive structure on the last eight tetrahedra. All
# coefficients and products below are rational functions in the cubic root.
Y=1+2*X+2*X**2
aa=1-1/X;bb=X*(1-X);ll=-2/(Y-1)
shapes=[reduced(z) for z in [aa/2,X,aa/2,aa,(bb-1)/bb,ll,ll,bb]]
params=[reduced(p) for z in shapes for p in [z,1/(1-z),(z-1)/z]]
edge_parent={}
def edge_find(x):
 edge_parent.setdefault(x,x)
 if edge_parent[x]!=x:edge_parent[x]=edge_find(edge_parent[x])
 return edge_parent[x]
def edge_join(x,y):edge_parent[edge_find(x)]=edge_find(y)
for t,(ns,ps) in enumerate(new):
 for f in range(4):
  for a,b in itertools.combinations([v for v in range(4) if v!=f],2):
   edge_join((t,a,b),(ns[f],*sorted((ps[f][a],ps[f][b]))))
parameter={(0,1):0,(2,3):0,(0,2):1,(1,3):1,(0,3):2,(1,2):2}
edge_rows={}
for t in range(8):
 for e in itertools.combinations(range(4),2):
  row=edge_rows.setdefault(edge_find((t,*e)),[0]*24)
  row[3*t+parameter[e]]+=1
assert len(edge_rows)==8
for row in edge_rows.values():
 product=s.Integer(1)
 for z,n in zip(params,row):product=reduced(product*z**n)
 equal(product,1,'exact_edge_products')

def cusp_coordinates(z,v):
 return [{1:s.Integer(0),2:s.Integer(1),3:z},
         {0:s.Integer(0),2:s.Integer(1),3:1/z},
         {0:s.Integer(0),1:s.Integer(-1),3:1/(z-1)},
         {0:s.Integer(0),1:-1/z,2:1/(1-z)}][v]
pot={};translations={}
for t in range(8):
 for v in range(4):
  if (t,v) in pot:continue
  pot[t,v]=s.Integer(1);queue=collections.deque([(t,v)])
  while queue:
   i,w=queue.popleft()
   for f in range(4):
    if f==w:continue
    n,p=new[i][0][f],new[i][1][f]
    a,b=[j for j in range(4) if j not in (f,w)]
    c,d=cusp_coordinates(shapes[i],w),cusp_coordinates(shapes[n],p[w])
    L=reduced((d[p[b]]-d[p[a]])/(c[b]-c[a]))
    V=reduced(d[p[a]]-L*c[a]);target=(n,p[w])
    wanted=reduced(pot[i,w]*L)
    if target not in pot:pot[target]=wanted;queue.append(target)
    else:equal(pot[target],wanted,'all_cusp_linear_cycles')
    translations[i,w,f]=reduced(V/wanted)
periods=[]
for row in [0,2]:
 value=s.Integer(0)
 for (t,v,f),delta in translations.items():
  if cs[t][v]==1:value=reduced(value+pc[4*t+row][4*v+f]*delta/2)
 periods.append(value)
mu,longitude=periods
equal(mu,-(X**2+7*X+7)/2,'original_peripheral_translations')
equal(longitude,X**2-X-5,'original_peripheral_translations')
ratio=reduced(longitude/mu)
equal(ratio,1+1/Y,'original_peripheral_ratio')
tau=-ratio
equal(17*tau**3+58*tau**2+72*tau+32,0,'cusp_ratio_cubic')
assert all((17*j**3+58*j**2+72*j+32)%3!=0 for j in range(3))
CHECKS['cusp_ratio_irreducibility_modulo_three']=1
class I:
    def __init__(self,a,b=None): self.a,self.b=Q(a),Q(a if b is None else b)
    def __add__(self,o):
        if not isinstance(o,I): o=I(o)
        return I(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return I(-self.b,-self.a)
    def __sub__(self,o): return self+-asI(o)
    def __rsub__(self,o): return asI(o)+-self
    def __mul__(self,o):
        o=asI(o); vals=[x*y for x in (self.a,self.b) for y in (o.a,o.b)]
        return I(min(vals),max(vals))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=asI(o); assert o.a*o.b>0
        return self*I(1/o.b,1/o.a)
    def __pow__(self,n):
        assert n>=0
        v=I(1)
        for _ in range(n): v=v*self
        return v

def asI(o): return o if isinstance(o,I) else I(o)
def atan_small(q):
    if q<0: return -atan_small(-q)
    assert q<=Q(1,2)
    total=sum((-1)**j*q**(2*j+1)/Q(2*j+1) for j in range(40))
    return I(total,total+q**81/Q(81))

# Machin's identity follows by twice applying the tangent double-angle
# formula to atan(1/5), then subtracting atan(1/239); the result is pi/4
# in (0,pi/2). Its alternating rational bounds certify this enclosure.
PI = 16*atan_small(Q(1,5))-4*atan_small(Q(1,239))

def atan(q):
    if q<0: return -atan(-q)
    if q>1: return PI/2-atan(1/q)
    return atan_small(Q(1,2))+atan_small((2*q-1)/(q+2))

alpha=I(Q(102784715200295,10**15),Q(102784715200296,10**15))
f=lambda q:8*q*(1+q)**2-1
assert f(alpha.a)<0<f(alpha.b)
beta=I(Q(665456951152810,10**15),Q(665456951152820,10**15))
assert beta.a**2<(4*alpha+3*alpha**2).a
assert beta.b**2>(4*alpha+3*alpha**2).b

def interval_complex(poly):
    co=[Q(str(s.expand(poly).coeff(X,i))) for i in range(3)]
    return co[0]+co[1]*alpha+co[2]*(alpha**2-beta**2), co[1]*beta+2*co[2]*alpha*beta

arguments=[]
for zz in params:
 real,imag=interval_complex(zz);assert imag.a>0
 ratio_i=real/imag
 arguments.append(PI/2-I(atan(ratio_i.a).a,atan(ratio_i.b).b))
 CHECKS['positive_shape_parameters']+=1
for row in edge_rows.values():
 angle=sum(e*a for e,a in zip(row,arguments))
 assert Q(6)<angle.a<angle.b<Q(7)
 CHECKS['exact_edge_winding']+=1
report={'status':'passed','checks':dict(CHECKS),
 'meridian_translation':str(mu),'longitude_translation':str(longitude),
 'longitude_over_meridian':str(ratio),
 'verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'fixture_sha256':hashlib.sha256(FIXTURE.read_bytes()).hexdigest(),
 'original_diagram_fixture_sha256':hashlib.sha256(BASE.read_bytes()).hexdigest(),
 'scope':'Transport of the explicit original auxiliary-cusp normal curves; complete exact cusp ratio. It does not identify a deformed source period or change a peripheral orientation convention.'}
ARGS.output.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
