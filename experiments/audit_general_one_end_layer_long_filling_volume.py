"""Exact checks specific to the new right-end source and physical boundary.
The old interior recurrence audit remains separate. No sample proves the
uniform comparison or asymptotic invariant theorem.
"""
import argparse,json,sys
from pathlib import Path
from collections import Counter
import sympy as s
sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit_actual_original_marked_face_coefficient import morse_faces

def boundary():
 p,q,H=s.symbols('p q H',positive=True)
 assert s.expand(1-2*q*(1+p)+q*q*(1-p*p)*(1-1)-(1-2*q*(1+p)))==0
 assert s.factor((1-2*q*(1+p)).subs(q,1/(2*(1+p))))==0
 z=s.sqrt(2)/2
 assert s.simplify((1-z*z)*(1+1)-1)==0
 Xp=H/p;rp=H/(2*p*p);X=H/(1+p);r=X*X/(2*H)
 assert s.factor((Xp-X)**2-4*rp*r)==0
 assert s.factor(1/r-2*(1+p)**2/H)==0
 assert s.factor((1/r)/(2/H)-(1+p)**2)==0
 return {'new_linear_boundary_and_small_width_identities':3,'exact_positive_final_center_identities':3}

def source():
 rows=ports=triangles=edges=reflection=components=0
 for k in range(2,41):
  O=list(range(1,2*k-2,2));E=list(range(2,2*k,2));word=O+E+O
  c=morse_faces(k,word,0)
  u=0;a=list(range(1,k+1));e=[None]+list(range(k+1,2*k))+[0];b=[a[0]]+list(range(2*k,3*k-1))
  expect=[(a[j-1],u,e[j],a[j]) for j in range(1,k)]
  expect +=[(e[j],a[j],b[j],e[j+1]) for j in range(1,k)]
  expect +=[(b[j-1],e[j],u,b[j]) for j in range(1,k)]
  assert c['circles']==expect and c['v']==a[0]
  tt=[t for x,bb,cc,y in expect for t in [(x,bb,y),(x,y,cc)]]
  assert all(len(set(t))==3 for t in tt) and len({tuple(sorted(t)) for t in tt})==len(tt)
  ed=Counter(tuple(sorted((t[i],t[(i+1)%3]))) for t in tt for i in range(3))
  assert set(ed.values())=={2}
  assert c['faces']==3*k-1 and len(ed)==9*k-9 and len(tt)==6*k-6
  refl=dict(zip(a,b));refl.update(zip(b,a));refl.update({f:f for f in [u]+e[1:-1]})
  assert {tuple(sorted(refl[f] for f in t)) for t in tt}=={tuple(sorted(t)) for t in tt}
  parent=list(range(2*k));perm=list(range(2*k))
  for j in O:perm[j],perm[j+1]=perm[j+1],perm[j]
  def find(x):
   while parent[x]!=x:x=parent[x]
   return x
  for j in range(k):
   parent[find(2*j)]=find(2*j+1);parent[find(perm[2*j])]=find(perm[2*j+1])
  assert len({find(j) for j in range(2*k)})==1
  rows+=1;ports+=len(expect);triangles+=len(tt);edges+=len(ed);reflection+=len(refl);components+=1
 return {'literal_all_width_source_charts':rows,'actual_quartets':ports,'actual_triangles':triangles,'edge_incidence_counts':edges,'reflection_vertex_checks':reflection,'one_component_parity_checks':components}

def seeds():
 rt=s.sqrt(2);small=3-2*rt
 all_disks={2:{2:(s.Integer(2),s.Integer(1),s.Integer(1)),3:(s.Integer(0),s.Integer(1),s.Integer(1)),4:(-s.Integer(2),s.Integer(1),s.Integer(1))},
 3:{2:(rt,s.Integer(1),s.Integer(1)),3:(2-rt,small,small),4:(s.Integer(0),s.Rational(3,2),s.Rational(1,2)),5:(s.Integer(0),s.Rational(1,2),s.Rational(1,2)),6:(-rt,s.Integer(1),s.Integer(1)),7:(rt-2,small,small)}}
 pairs=tests=0
 for k,disks in all_disks.items():
  O=list(range(1,2*k-2,2));E=list(range(2,2*k,2));c=morse_faces(k,O+E+O,0)
  tt=[t for x,b,cc,y in c['circles'] for t in [(x,b,y),(x,y,cc)]]
  ed={tuple(sorted((t[i],t[(i+1)%3]))) for t in tt for i in range(3)}
  for i in range(c['faces']):
   for j in range(i+1,c['faces']):
    if (i,j)==(0,1):continue
    if i in (0,1):
     x,y,r=disks[j];slack=s.Abs(y-(0 if i==0 else 2))-r
    else:
     x,y,r=disks[i];xx,yy,rr=disks[j];slack=(x-xx)**2+(y-yy)**2-(r+rr)**2
    slack=s.simplify(slack)
    assert slack==0 if (i,j) in ed else slack.is_positive is True,(k,i,j,slack)
    pairs+=1
  curv={0:s.Integer(0),1:s.Integer(0)}|{f:s.simplify(1/r) for f,(x,y,r) in disks.items()}
  for x,b,cc,y in c['circles']:
   if b==0 or cc==0:
    E=curv[cc] if b==0 else curv[b];ratio=s.simplify(E/(curv[x]+curv[y]));assert s.simplify(s.Rational(9,4)-ratio).is_positive
   else:assert s.simplify(curv[b]-curv[cc])==0
   tests+=1
 return {'exact_k2_k3_circle_support_pairs':pairs,'exact_k2_k3_port_balance_tests':tests}

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=Path(__file__).with_name('general_one_end_layer_long_filling_volume_results.json'));a=p.parse_args()
 out={'status':'PASS','scope':'Exact original right-end source incidences, first mark, reflection and parity at k2..40; changed linear/right boundary identities; exact k2/k3 packing contacts and noncontacts. The prior interior audit is not repeated, and no numerical samples are used to prove the uniform theorem.','counts':boundary()|source()|seeds()}
 a.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
