"""Focused exact checks for the analytic reduced-layer family proof.
The all-width comparison and full invariant conclusion are proved in the note,
not inferred from these finitely many source and algebra checks.
"""
import argparse, json, sys
from pathlib import Path
from collections import Counter
from fractions import Fraction as F
import sympy as sp
sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit_actual_original_marked_face_coefficient import morse_faces

def algebra():
 p,z,w,q=sp.symbols('p z w q',positive=True)
 Q=1-z*z
 X=z/p;Y=Q*w/z
 r=(p*p+(1-p*p)*z*z)/(2*p*p)
 rr=Q*(z*z+Q*w*w)/(2*z*z)
 poly=1-2*Q*(1+p*w)+Q*Q*(1-p*p)*(1-w*w)
 assert sp.factor((X-Y)**2-4*r*rr-poly/p**2)==0
 polynomial=1-2*q*(1+p*w)+q*q*(1-p*p)*(1-w*w)
 for root in [1/((1+p)*(1+w)),1/((1-p)*(1-w))]:assert sp.factor(polynomial.subs(q,root))==0
 W=1/((1+p)*(1-z*z))-1
 D=p*p+z*z-p*p*z*z
 prev=p*p*z*z/D
 nxt=z**4/((1-z*z)*(z*z+(1-z*z)*W*W))
 assert sp.factor(nxt-z**4*(1+p)**2/D)==0
 assert sp.factor(prev+nxt-z*z*(1+2*p*(1+p)*z*z/D))==0
 seed=[F(0),F(2,3),F(4,5),F(2,3),F(0)]
 for j in range(1,4):assert (1+seed[j-1])*(1-seed[j]**2)*(1+seed[j+1])==1
 low=F(7,11)*sum((-1)**j*F(2,3)**(2*j+1)/((2*j+1)**2) for j in range(4))
 up=2*sum(F(1,5)**(2*j+1)/(2*j+1) for j in range(3))+2*F(1,5)**7/(7*(1-F(1,25)))
 assert low-up==F(57269,136687500)>F(1,2500)
 return {'symbolic_tangency_root_curvature_identities':5,'exact_seed_equations':3,'exact_rational_balance_bounds':1}

def source():
 charts=ports=triangles=edges=reflections=components=0
 for k in range(3,41):
  O=list(range(1,2*k-2,2));E=list(range(2,2*k-2,2));word=O+E+O
  c=morse_faces(k,word,0)
  u=0;a=list(range(1,k+1));e=[None]+list(range(k+1,2*k));b=[a[0]]+list(range(2*k,3*k-2))+[a[-1]]
  expect=[(a[j-1],u,e[j],a[j]) for j in range(1,k)]
  expect +=[(e[j],a[j],b[j],e[j+1]) for j in range(1,k-1)]
  expect +=[(b[j-1],e[j],u,b[j]) for j in range(1,k)]
  assert c['circles']==expect and c['v']==a[0]
  tt=[t for x,bb,cc,y in expect for t in [(x,bb,y),(x,y,cc)]]
  assert all(len(set(t))==3 for t in tt)
  assert len({tuple(sorted(t)) for t in tt})==len(tt)
  ed=Counter(tuple(sorted((t[i],t[(i+1)%3]))) for t in tt for i in range(3))
  assert set(ed.values())=={2}
  assert c['faces']==3*k-2 and len(ed)==9*k-12 and len(tt)==6*k-8
  refl=dict(zip(a,b));refl.update(zip(b,a));refl.update({f:f for f in [u]+e[1:]})
  assert {tuple(sorted(refl[f] for f in t)) for t in tt}=={tuple(sorted(t)) for t in tt}
  parent=list(range(2*k));perm=list(range(2*k))
  for j in O:perm[j],perm[j+1]=perm[j+1],perm[j]
  def find(x):
   while parent[x]!=x:x=parent[x]
   return x
  for j in range(k):
   parent[find(2*j)]=find(2*j+1)
   parent[find(perm[2*j])]=find(perm[2*j+1])
  assert len({find(j) for j in range(2*k)})==1
  charts+=1;ports+=len(expect);triangles+=len(tt);edges+=len(ed);reflections+=len(refl);components+=1
 return {'literal_source_widths':charts,'actual_quartets':ports,'actual_triangles':triangles,'edge_incidence_counts':edges,'reflection_vertex_checks':reflections,'one_component_parity_checks':components}

def exact_seed_geometry():
 k=4;O=[1,3,5];E=[2,4];c=morse_faces(k,O+E+O,0)
 # Source labels: a0..a3=1..4, e1..e3=5..7, b1,b2=8,9.
 disks={2:(F(4,3),F(1),F(1)),3:(F(1,3),F(1,4),F(1,4)),4:(F(0),F(1,9),F(1,9)),
        5:(F(0),F(14,9),F(4,9)),6:(F(0),F(34,45),F(16,45)),7:(F(0),F(14,45),F(4,45)),
        8:(-F(4,3),F(1),F(1)),9:(-F(1,3),F(1,4),F(1,4))}
 tt=[t for x,b,cc,y in c['circles'] for t in [(x,b,y),(x,y,cc)]]
 ed={tuple(sorted((t[i],t[(i+1)%3]))) for t in tt for i in range(3)}
 pairs=0
 for i in range(c['faces']):
  for j in range(i+1,c['faces']):
   if (i,j)==(0,1):continue
   if i in (0,1):
    x,y,r=disks[j];slack=abs(y-(0 if i==0 else 2))-r
   else:
    x,y,r=disks[i];xx,yy,rr=disks[j];slack=(x-xx)**2+(y-yy)**2-(r+rr)**2
   assert slack==0 if (i,j) in ed else slack>0,(i,j,slack)
   pairs+=1
 curv={0:F(0),1:F(0)}|{f:1/r for f,(x,y,r) in disks.items()}
 for x,b,cc,y in c['circles']:
  if b==0 or cc==0:assert max(curv[b],curv[cc])/(curv[x]+curv[y])<=F(9,4)
  else:assert curv[b]==curv[cc]
 return {'exact_seed_circle_support_pairs':pairs,'exact_seed_port_balance_tests':len(c['circles'])}

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=Path(__file__).with_name('general_reduced_layer_long_filling_volume_results.json'));args=parser.parse_args()
 out={'status':'PASS','scope':'Exact literal source incidence and reflection at 38 widths; symbolic tangency/branch/curvature identities and rational seed/balance checks. Uniform comparison and full quantum limit are analytical, not sampled.','counts':algebra()|source()|exact_seed_geometry()}
 args.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
