"""Literal source patch and exact marked-strip support checks."""
import argparse,json,sys
from pathlib import Path
from collections import Counter
import sympy as s
sys.path.insert(0,str(Path(__file__).resolve().parent))
from audit_actual_original_marked_face_coefficient import morse_faces

def core_word(k):
 O=list(range(1,2*k-2,2));E=list(range(2,2*k,2));return O+E+O

def mapping(k,m,f):return k+2*m if f==2 else f+2*m if f>k else f

def check_source():
 charts=quartets=tris=edges=parities=0
 for k in range(2,9):
  w=core_word(k);old=morse_faces(k,w,0)
  for m in range(1,9):
   new=morse_faces(k,[1,2]*m+w,0);h=lambda f:mapping(k,m,f)
   aa=[2]+[k+2*j for j in range(1,m+1)];ff=[0]+[k+2*j-1 for j in range(1,m+1)]
   expect=[]
   for j in range(1,m+1):expect.extend([(1,ff[j-1],ff[j],aa[j-1]),(ff[j],aa[j-1],aa[j],0)])
   v,u,e,a=old['circles'][0];assert(v,u,a)==(1,0,2)
   expect.append((1,ff[m],h(e),h(a)))
   expect.extend(tuple(h(f) for f in q) for q in old['circles'][1:])
   assert new['circles']==expect and new['v']==1 and new['faces']==old['faces']+2*m
   tt=[t for x,b,c,y in expect for t in [(x,b,y),(x,y,c)]]
   ed=Counter(tuple(sorted((t[j],t[(j+1)%3]))) for t in tt for j in range(3))
   assert all(len(set(t))==3 for t in tt) and len({tuple(sorted(t)) for t in tt})==len(tt)
   assert set(ed.values())=={2} and new['faces']-len(ed)+len(tt)==2
   # All prefix exponents even, all original odd permutations retained.
   perm=list(range(2*k))
   for j in w[:k-1]:perm[j],perm[j+1]=perm[j+1],perm[j]
   adj={j:set() for j in range(2*k)}
   for j in range(0,2*k,2):
    for a,b in [(j,j+1),(perm[j],perm[j+1])]:adj[a].add(b);adj[b].add(a)
   seen={0};stack=[0]
   while stack:
    for f in adj[stack.pop()]-seen:seen.add(f);stack.append(f)
   assert len(seen)==2*k
   charts+=1;quartets+=len(expect);tris+=len(tt);edges+=len(ed);parities+=1
 return dict(literal_extended_charts=charts,quartets=quartets,triangles=tris,edges=edges,knot_parities=parities)

def pos(v):
 v=s.expand(v);a=v.coeff(s.sqrt(2),0);b=v.coeff(s.sqrt(2),1);assert s.expand(v-a-b*s.sqrt(2))==0
 if b>=0:return (a>=0 and(a>0 or b>0)) or(a<0 and 2*b*b>a*a)
 return a>0 and a*a>2*b*b

def check_geometry():
 q=s.sqrt(2);r=3-2*q
 seeds={2:{2:(s.Integer(2),s.Integer(1),s.Integer(1)),3:(s.Integer(0),s.Integer(1),s.Integer(1)),4:(-s.Integer(2),s.Integer(1),s.Integer(1))},
 3:{2:(q,s.Integer(1),s.Integer(1)),3:(2-q,r,r),4:(0,s.Rational(3,2),s.Rational(1,2)),5:(0,s.Rational(1,2),s.Rational(1,2)),6:(-q,s.Integer(1),s.Integer(1)),7:(q-2,r,r)}}
 counts=ports=0
 for k,seed in seeds.items():
  for m in range(1,7):
   shift=seed[2][0];disks={mapping(k,m,f):(s.expand(x-shift),y,rad) for f,(x,y,rad) in seed.items()}
   for j in range(m):disks[2 if j==0 else k+2*j]=(s.Integer(4*(m-j)),s.Integer(1),s.Integer(1))
   for j in range(1,m+1):disks[k+2*j-1]=(s.Integer(4*(m-j)+2),s.Integer(1),s.Integer(1))
   c=morse_faces(k,[1,2]*m+core_word(k),0)
   tt=[t for x,b,cc,y in c['circles'] for t in [(x,b,y),(x,y,cc)]]
   ed={tuple(sorted((t[j],t[(j+1)%3]))) for t in tt for j in range(3)}
   for i in range(c['faces']):
    for j in range(i+1,c['faces']):
     if(i,j)==(0,1):continue
     if i<2:
      x,y,rad=disks[j];slack=s.expand((y if i==0 else 2-y)-rad)
     else:
      x,y,rad=disks[i];xx,yy,rr=disks[j];slack=s.expand((x-xx)**2+(y-yy)**2-(rad+rr)**2)
     assert(slack==0) if(i,j) in ed else pos(slack),(k,m,i,j,slack)
     counts+=1
   curv={0:0,1:0}|{f:s.simplify(1/rad) for f,(x,y,rad) in disks.items()}
   for j,(x,b,cc,y) in enumerate(c['circles'][:2*m]):
    values=(curv[x],curv[b],curv[cc],curv[y]);assert values in[(0,0,1,1),(0,1,1,1),(1,1,1,0)];ports+=1
   x,b,cc,y=c['circles'][2*m];assert(curv[x],curv[b],curv[y])==(0,1,1)
   assert curv[cc]>=1
 return dict(exact_seed_extensions=12,exact_circle_line_supports=counts,new_unit_port_checks=ports,changed_core_port_checks=12)

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=Path(__file__).with_name('general_marked_unit_chain_filling_volume_results.json'));a=p.parse_args()
 out={'status':'PASS','scope':'Exact original source prefix/mark/typed incidences and preserved parity at fixed finite widths/depths, plus exact circle-line supports in two proved seed packings. General closure and volume implications are analytical, not inferred from samples.','counts':check_source()|check_geometry()}
 a.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
