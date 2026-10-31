"""Independent literal-source review of simultaneous first-layer gap chains."""
import argparse,json,itertools,sys
import sympy as sp
from collections import Counter
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from audit_actual_original_marked_face_coefficient import morse_faces

def explicit(k,depth):
 L=k-1;labels=['u','a0']+[f'C{j},{2*depth[j-1]}' if depth[j-1] else f'a{j}' for j in range(1,L+1)]
 expected=[];word=[];old_positions=[]
 for j,m in enumerate(depth,1):
  A=f'a{j-1}';slot=2*j-1
  for r in range(1,m+1):
   h=2*(m-r)+1;f=f'C{j},{h}';prev='u' if r==1 else f'C{j},{h+2}';old=f'C{j},{h+1}';new=f'a{j}' if h==1 else f'C{j},{h-1}'
   expected.extend([(A,prev,f,old),(f,old,new,'u')]);labels.extend([f,new]);word.extend([slot,slot+1])
  expected.append((A,f'C{j},1' if m else 'u',f'e{j}',f'a{j}'));labels.append(f'e{j}');old_positions.append(len(word));word.append(slot)
 for j in range(1,L+1):
  expected.append((f'e{j}',f'a{j}',f'b{j}',f'e{j+1}' if j<L else 'u'));labels.append(f'b{j}');word.append(2*j)
 for j in range(1,L+1):
  expected.append((f'b{j-1}' if j>1 else 'a0',f'e{j}','u',f'b{j}'));word.append(2*j-1)
 ids={s:i for i,s in enumerate(labels)}
 assert len(ids)==len(labels)
 return word,[tuple(ids[f] for f in t) for t in expected],old_positions,ids

def check_source():
 counts=Counter();cases=[]
 for k in range(2,7):cases +=[(k,t) for t in itertools.product(range(3),repeat=k-1)]
 for k in range(7,17):
  for shift in range(5):cases.append((k,tuple((j+shift)%5 for j in range(k-1))))
 for k,depth in cases:
  w,expected,oddpos,ids=explicit(k,depth);ch=morse_faces(k,w,0)
  assert ch['circles']==expected and ch['v']==ids['a0']==1
  R=3*k-3+2*sum(depth)
  assert len(w)==R and ch['faces']==R+2
  tris=[t for x,b,c,y in expected for t in [(x,b,y),(x,c,y)]]
  assert all(len(set(t))==3 for t in tris) and len(set(tuple(sorted(t)) for t in tris))==2*R
  ed=Counter(tuple(sorted((t[i],t[(i+1)%3]))) for t in tris for i in range(3))
  assert len(ed)==3*R and set(ed.values())=={2}
  assert (0,1) in ed
  # The only odd exponents are the retained first-layer core boxes.
  perm=list(range(2*k))
  for i in oddpos:s=w[i];perm[s],perm[s+1]=perm[s+1],perm[s]
  core=list(range(2*k))
  for s in range(1,2*k-2,2):core[s],core[s+1]=core[s+1],core[s]
  assert perm==core
  parent=list(range(2*k))
  def find(i):
   while i!=parent[i]:i=parent[i]
   return i
  for j in range(k):
   parent[find(2*j)]=find(2*j+1);parent[find(perm[2*j])]=find(perm[2*j+1])
  assert len({find(j) for j in range(2*k)})==1
  counts['literal_nonuniform_depth_charts']+=1;counts['actual_ports']+=R;counts['actual_triangles']+=2*R;counts['actual_edges']+=3*R;counts['first_marks_retained']+=1;counts['exact_core_permutations']+=1
  counts['new_chain_ports']+=2*sum(depth);counts['retained_old_ports']+=3*k-3
 return dict(counts)


def symbolic():
 u,v,n,l,t,z,w=sp.symbols('u v n l t z w',positive=True)
 rn=1/(v+n*u)**2;rl=1/(v+l*u)**2;xn=2/(u*(v+n*u));xl=2/(u*(v+l*u));R=1/u**2
 assert sp.factor(xn*xn+(rn-R)**2-(rn+R)**2)==0
 assert sp.factor((xn-xl)**2+(rn-rl)**2-(rn+rl)**2-4*rn*rl*((n-l)**2-1))==0
 assert sp.factor(xn-xn.subs(n,n+1)-2/((v+n*u)*(v+(n+1)*u)))==0
 assert sp.expand(2*(1+t*t)-(t+1)**2-(t-1)**2)==0
 assert sp.factor(sp.Rational(9,4)-((t+1)/t)**2-(t-2)*(5*t+2)/(4*t*t))==0
 assert sp.expand(2*(u*u+v*v)-(u+v)**2-(u-v)**2)==0
 assert sp.expand(z*z+w*w-z*z*w*w-z*w-((z-w)**2+z*w*(1-z*w)))==0
 return {'exact_tangency_and_support_identities':3,'exact_ratio_and_order_identities':4}

def norm(x):return sp.expand(sp.radsimp(sp.cancel(x)))
def pos(x):
 x=norm(x);q=sp.sqrt(2);a=x.coeff(q,0);b=x.coeff(q,1);assert sp.expand(x-a-b*q)==0,x
 if b>=0:return(a>=0 and(a>0 or b>0)) or(a<0 and 2*b*b>a*a)
 return a>0 and a*a>2*b*b

def geometry():
 q=sp.sqrt(2);r=3-2*q
 seeds={2:{'a1':(sp.Integer(2),sp.Integer(1),sp.Integer(1)),'e1':(sp.Integer(0),sp.Integer(1),sp.Integer(1)),'b1':(-sp.Integer(2),sp.Integer(1),sp.Integer(1))},
 3:{'a1':(q,sp.Integer(1),sp.Integer(1)),'a2':(2-q,r,r),'e1':(0,sp.Rational(3,2),sp.Rational(1,2)),'e2':(0,sp.Rational(1,2),sp.Rational(1,2)),'b1':(-q,sp.Integer(1),sp.Integer(1)),'b2':(q-2,r,r)}}
 counts=Counter()
 for k,seed in seeds.items():
  depths=[(m,) for m in range(9)] if k==2 else list(itertools.product(range(4),repeat=2))
  for depth in depths:
   word,ports,oldpos,ids=explicit(k,depth)
   disks={ids[name]:data for name,data in seed.items()}
   for j,m in enumerate(depth,1):
    for n in range(1,2*m+1):
     if j==1:data=(norm(seed['a1'][0]+2*n),sp.Integer(1),sp.Integer(1))
     else:
      # Exact k3 finite-gap chain: A=a1=1, sqrt(B)=1+sqrt2, orientation negative.
      rad=norm(1/(1+q+n)**2);data=(norm(q-2/(1+q+n)),rad,rad)
     disks[ids[f'C{j},{n}']]=data
   tt=[t for x,b,c,y in ports for t in [(x,b,y),(x,y,c)]]
   ed={tuple(sorted((t[i],t[(i+1)%3]))) for t in tt for i in range(3)}
   for i in range(len(ids)):
    for j in range(i+1,len(ids)):
     if(i,j)==(0,1):continue
     if i<2:
      x,y,rad=disks[j];slack=norm((y if i==0 else 2-y)-rad)
     else:
      x,y,rad=disks[i];xx,yy,rr=disks[j];slack=norm((x-xx)**2+(y-yy)**2-(rad+rr)**2)
     assert(slack==0) if(i,j) in ed else pos(slack),(k,depth,i,j,slack)
     counts['exact_circle_line_supports']+=1
   curv={0:sp.Integer(0),1:sp.Integer(0)}|{f:norm(1/rr) for f,(x,y,rr) in disks.items()}
   first_end=oldpos[-1]+1
   for pidx,(x,b,c,y) in enumerate(ports[:first_end]):
    if pidx in oldpos:
     jj=oldpos.index(pidx)
     if depth[jj]:
      slack=norm(2*(curv[x]+curv[y])-curv[b]);assert slack==0 or pos(slack);counts['modified_core_target_bounds']+=1
    else:
     M=curv[b] if curv[b]==curv[c] or pos(curv[b]-curv[c]) else curv[c]
     slack=norm(sp.Rational(9,4)*(curv[x]+curv[y])-M);assert slack==0 or pos(slack);counts['new_port_nine_quarter_bounds']+=1
   counts['exact_simultaneous_seed_packings']+=1
 return dict(counts)

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=Path(__file__).with_name('general_simultaneous_bridge_gap_filling_volume_results.json'));a=p.parse_args()
 out={'status':'PASS','scope':'Exact original simultaneous source dictionary/nonuniform depths and knot parity; symbolic all-parameter chain/support/ratio identities; exact joint k2/k3 finite and parallel-line patch supports and balance bounds. The general empty-gap and full quantum conclusions are analytical, not inferred from finite sampling.','counts':check_source()|symbolic()|geometry()}
 a.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
