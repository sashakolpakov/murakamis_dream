"""Positive root numerator paths and the original shared degree constraints.

No bound for the remaining forest weights is claimed.
"""
import argparse,json,itertools,collections
from pathlib import Path
import mpmath as mp
from audit_actual_original_marked_face_coefficient import morse_faces
parser=argparse.ArgumentParser()
parser.add_argument('--output',type=Path,default=Path(__file__).with_name('actual_fejer_cross_half_source_reduction_results.json'))
args=parser.parse_args()
mp.mp.dps=70

def paths(j):
 def rec(i,steps,visited):
  yield i,steps,visited
  if i:yield from rec(i-1,steps+[(i,1)],visited+[i-1])
  if i>=2:yield from rec(i-2,steps+[(i,2)],visited+[i-2])
 yield from rec(j,[],[j])
counts={'positive_paths':0,'cross_coefficients':0,'repaired_paths':0,'half_block_coefficients':0,'original_gap_forests':0,'noncross_target_states':0}
ratios=[]
for N in(4,6,8,10,12,14):
 m=N//2;d=N-1;cs=[2*mp.cos((2*j+1)*mp.pi/N) for j in range(N)];ss=[2*mp.sin(j*mp.pi/N) for j in range(N)];star=cs[m-1];delta=2+star
 C=4*(4-delta)/(delta*N*N);R=delta/(8*mp.cos(mp.pi/N));assert C*(1+2*R)<3
 B=collections.defaultdict(mp.mpf);cross=collections.defaultdict(mp.mpf);left=collections.defaultdict(mp.mpf)
 for j in range(N):
  for i,steps,visited in paths(j):
   weight=mp.mpf(1);ones=twos=0
   for v,step in steps:
    if step==1:weight*=ss[v]**2;ones+=1
    else:weight*=ss[v]*ss[v-1];twos+=1
   full=weight*mp.fprod(2+cs[v] for v in range(N) if v not in visited)
   paired=weight*mp.fprod(cs[v]-star for v in range(N) if v not in visited) if m-1 in visited and m in visited else mp.mpf(0)
   if i<m<=j and paired==0:
    defect=[v for v,step in steps if step==2 and v in(m,m+1)]
    assert len(defect)==1;v=defect[0]
    repaired=[]
    for vv,step in steps:
     repaired.extend(((vv,1),(vv-1,1))) if vv==v and step==2 else repaired.append((vv,step))
    assert sum(t for vv,t in repaired)==sum(t for vv,t in steps)
    counts['repaired_paths']+=1
   for a in range(ones+1):
    e=(a+twos,i,d-j,ones-a+twos);binom=mp.binomial(ones,a)
    if i<m<=j:cross[e]+=full*binom;B[e]+=paired*binom
    if j<m:left[e]+=full*binom
   counts['positive_paths']+=1
 for e,v in cross.items():
  assert B[e]<=v*(1+mp.mpf('1e-55'))
  assert v<=C*(1+2*R)*B[e]*(1+mp.mpf('1e-55'))
  counts['cross_coefficients']+=1
 ratios.append(str(max(cross[e]/B[e] for e in cross)))
 # Independent lower block path assembly, with c^m and upper product2.
 lower=collections.defaultdict(mp.mpf)
 for j in range(m):
  for i,steps,vis in paths(j):
   weight=2*mp.fprod(2+cs[v] for v in range(m) if v not in vis);o=t=0
   for v,s in steps:
    weight*=ss[v]**2 if s==1 else ss[v]*ss[v-1];o+=s==1;t+=s==2
   for a in range(o+1):lower[(a+t,i,d-j,o-a+t)]+=weight*mp.binomial(o,a)
 for e,v in left.items():
  assert abs(v-lower[e])<=mp.mpf('1e-55')*max(1,abs(v));counts['half_block_coefficients']+=1
# Actual gap charts: enumerate ALL noncross edge orientations admitting degree overloads.
for k,word,mark in [(2,[1,0,1],1),(2,[1,0,2,1],1),(3,[1,3,0,2,4,1,3],2)]:
 D=morse_faces(k,word,mark);protected={0,D['v']};edges=[(b,c) for x,b,c,y in D['circles']]
 for states in itertools.product((0,1,2),repeat=len(edges)):
  incoming=collections.Counter();sel=[]
  for st,(b,c) in zip(states,edges):
   if st:incoming[(b,c)[st-1]]+=1;sel.append((b,c))
  if any(v>1 or x in protected for x,v in incoming.items()):continue
  parent={v:v for edge in sel for v in edge}
  def find(v):
   while parent[v]!=v:v=parent[v]
   return v
  for b,c in sel:
   bb,cc=find(b),find(c);assert bb!=cc;parent[bb]=cc
  groups=collections.defaultdict(list)
  for v in parent:groups[find(v)].append(v)
  for vs in groups.values():assert sum(incoming[v]==0 for v in vs)==1
  counts['original_gap_forests']+=1
 # Coefficient support test: genuine marked target allows noncross forests.
 N=4;d=3;m=2;nf=D['faces'];target=tuple(0 if f in protected else d for f in range(nf));poly={(tuple([0]*nf),0):1}
 for ids in D['circles']:
  fac=[]
  for a,i,t in itertools.product(range(d+1),repeat=3):
   y=d-a-i-t
   if y<0:continue
   ex=[0]*nf
   for f,v in zip(ids,(a,i,t,y)):ex[f]+=v
   if any(ex[f]>target[f] for f in range(nf)):continue
   fac.append((tuple(ex),int(i>=m or t>=m)))
  nxt=collections.defaultdict(int)
  for (old,n),v in poly.items():
   for ex,tag in fac:
    ee=tuple(a+b for a,b in zip(old,ex))
    if all(ee[f]<=target[f] for f in range(nf)):nxt[(ee,n+tag)]+=v
  poly=nxt
 counts['noncross_target_states']+=sum(v for (e,n),v in poly.items() if e==target and n)
out={'status':'PASS','precision':mp.mp.dps,'counts':counts,'maximum_cross_ratios':ratios,'scope':'Exact positive central-path comparison and actual original-gap degree forests. No forest weight or global rate bound.'}
args.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
