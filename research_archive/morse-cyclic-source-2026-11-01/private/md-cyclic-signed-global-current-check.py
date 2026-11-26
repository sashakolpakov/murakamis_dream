"""Exact integer shared-current obstruction at N=3 on the literal m=6 source.

This tests a proposed vanishing identity, not a norm or asymptotic estimate.
All coefficients follow from the original three-arrow face operator.
"""
import argparse
import hashlib
import json
from pathlib import Path
from collections import defaultdict

def H(t=None):
 c=[1,-2,1]; a=[0,3,3]; b=[0,0,3]
 casimir=isinstance(t,tuple)
 if casimir:t=t[1]
 f=[1,0,0] if t is None else [t*t-3,t,1]
 if casimir:f=[0]+f
 out=defaultdict(int)
 for j in range(3):
  st={(0,j,0):1}
  for r in range(len(f)):
   for (x,i,y),v in st.items():out[x,i,2-j,y]+=f[r]*v
   ne=defaultdict(int)
   for (x,i,y),v in st.items():
    ne[x,i,y]+=c[i]*v
    if i:
     ne[x+1,i-1,y]-=a[i]*v
     ne[x,i-1,y+1]-=a[i]*v
    if i>=2:ne[x+1,i-2,y+1]-=b[i]*v
   st=ne
 return {k:v for k,v in out.items() if v}

def source(spec):
 m=len(spec); p={(0,)*m:1}
 for j,t in enumerate(spec):
  labels=[None,(j-1)%m,(j+1)%m,j] if j%2 else [0,(j+1)%m,(j-1)%m,j]
  # Index zero is S, while the original equatorial z_0 is protected.
  if j%2:
   labels=[None,None if (j-1)%m==0 else (j-1)%m,None if (j+1)%m==0 else (j+1)%m,None if j==0 else j]
  else:
   labels=[0,None if (j+1)%m==0 else (j+1)%m,None if (j-1)%m==0 else (j-1)%m,None if j==0 else j]
  loc=defaultdict(int)
  for exps,v in H(t).items():
   ee=[0]*m
   ok=True
   for e,l in zip(exps,labels):
    if l is None:
     if e:ok=False;break
    else:ee[l]+=e
   if ok and max(ee)<=2:loc[tuple(ee)]+=v
  ne=defaultdict(int)
  for a,v in p.items():
   for b,w in loc.items():
    e=tuple(x+y for x,y in zip(a,b))
    if max(e)<=2:ne[e]+=v*w
  p={e:v for e,v in ne.items() if v}
 return p.get((2,)*m,0)

def chi(t):return t**3-3*t+2

def main():
 parser=argparse.ArgumentParser()
 parser.add_argument('--output',type=Path,default=Path(
  '/private/tmp/md-cyclic-signed-global-current-results.json'))
 args=parser.parse_args()
 records=[]
 for s,t in [(0,2),(-2,2),(2,0),(0,0)]:
  sp=[2,s,t,2,2,2]
  v=source(sp)
  a=sp.copy();a[1]=None
  b=sp.copy();b[2]=None
  iv=source(a);jv=source(b)
  current=(s-t)*v-chi(s)*iv+chi(t)*jv
  ac=sp.copy();ac[1]=('C',s)
  bc=sp.copy();bc[2]=('C',t)
  direct=source(ac)-source(bc)
  assert direct==current
  records.append(dict(spectra=sp,full=v,north_identity=iv,
   south_identity=jv,cleared_current=current,
   direct_CV_insertion_difference=direct))
 assert records[0]['full']==910845
 assert records[0]['cleared_current']==-2051892
 result=dict(status='passed',N=3,m=6,arithmetic='exact integers',
  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
  all_plus_two_source=source([2]*6),records=records,
  scope=('The actual shared four-band current need not vanish. '
   'This is not a counterexample to a strict full-minus-CROSS supremum gap, '
   'and no filled invariant or volume is evaluated.'))
 args.output.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(dict(status='passed',nonzero_current=records[0]['cleared_current'],
  output=str(args.output))))

if __name__=='__main__':main()
