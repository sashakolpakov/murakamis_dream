"""Exact source/packing and Arb capacity witnesses; no numerical optimizer is used."""
import argparse,json,sys
from pathlib import Path
from collections import Counter
import sympy as s
from flint import arb,ctx
ctx.prec=192
sys.path.insert(0,str(Path(__file__).resolve().parent))
from audit_actual_original_marked_face_coefficient import morse_faces
PORTS=[(1,0,4,2),(2,0,5,3),(4,2,6,5),(1,4,0,6),(6,5,0,3)]
M=1024

def source_packing():
 chart=morse_faces(3,[1,3,2,1,3],0)
 assert chart['circles']==PORTS and chart['v']==1 and chart['faces']==7
 tt=[t for x,b,c,y in PORTS for t in [(x,b,y),(x,c,y)]]
 ed=Counter(tuple(sorted((t[i],t[(i+1)%3]))) for t in tt for i in range(3))
 assert len(ed)==15 and set(ed.values())=={2}
 z=s.sqrt(5);r=(3-z)/2
 discs={2:(z-1,s.Integer(1),s.Integer(1)),3:(s.Integer(0),r,r),4:(s.Integer(0),(1+z)/2,r),5:(s.Integer(0),s.Integer(1),z-2),6:(1-z,s.Integer(1),s.Integer(1))}
 count=0
 for i in range(7):
  for j in range(i+1,7):
   if (i,j)==(0,1):continue
   if i in (0,1):
    x,y,rr=discs[j];v=s.Abs(y-(0 if i==0 else 2))-rr
   else:
    x,y,rr=discs[i];xx,yy,ss=discs[j];v=(x-xx)**2+(y-yy)**2-(rr+ss)**2
   v=s.simplify(v)
   assert (v==0) if (i,j) in ed else v.is_positive is True,(i,j,v)
   count+=1
 return {'actual_ports':5,'actual_triangles':10,'actual_edges':15,'exact_contact_and_noncontact_pairs':count}

CACHE={}
def lob(angle,zero=False):
 if zero:return arb(0)
 acc=arb(0)
 for n in range(1,M+1):acc+=(2*n*angle).sin()/(2*n*n)
 return acc+arb(0,arb(1)/(2*M))
def Q(weights):
 key=tuple(str(v) for v in weights)
 if key in CACHE:return CACHE[key]
 w=[arb(v) if isinstance(v,(int,str)) else v for v in weights]
 pos=[i for i,v in enumerate(w) if not v.is_zero()]
 assert pos
 if len(pos)==1:ret=w[pos[0]].log()/2;CACHE[key]=ret;return ret
 disc=(w[0]*w[1]+w[1]*w[2]+w[2]*w[0]).sqrt();ret=arb(0)
 for i in pos:
  a=(w[i]/disc).atan()
  ret+=(lob(a)+lob(arb.pi()/2-a))/arb.pi()+a/arb.pi()*w[i].log()
 CACHE[key]=ret;return ret

def maxball(vals):
 lo=max(v.lower() for v in vals);hi=max(v.upper() for v in vals)
 return (arb(lo)+arb(hi))/2+arb(0,(arb(hi)-arb(lo))/2)
def X(port,L):
 x,b,c,y=port;return Q([L[x],L[b],L[y]])+Q([L[x],L[c],L[y]])
def full(port,L):
 return maxball([X(port,L)]+[L[f].log() for f in port[1:3] if not L[f].is_zero()])
def anchor_value(e,side,L):
 values=[]
 for j,port in enumerate(PORTS):
  if j!=e:values.append(full(port,L));continue
  x,b,c,y=port
  if side=='R':b,c=c,b
  assert not L[c].is_zero()
  values.append(maxball([L[c].log(),Q([L[x],L[b],L[y]])+L[c].log()/2]))
 return sum(values,arb(0))-sum((L[f].log() for f in range(2,7)),arb(0))
def interval(a):return {'lower':str(a.lower()),'upper':str(a.upper())}
def certificates():
 r5=arb(5).sqrt();g=[arb(0),arb(0),arb(1),(3+r5)/2,(3+r5)/2,2+r5,arb(1)]
 phi=sum((X(p,g) for p in PORTS),arb(0))-sum((g[f].log() for f in range(2,7)),arb(0))
 assert phi>arb('5.17') and phi<arb('5.20')
 failure=[]
 for e in [0,3]:
  p=PORTS[e];bad=X(p,g)-g[4].log();assert bad<arb('-0.09');failure.append(interval(bad))
 seeds=[(0,'L',['3','4','1.5','5','1']),(1,'L',['1.5','5','2','2','1']),(2,'L',['2','6','2','18','1'])]
 data=[]
 for e,side,rr in seeds:
  for reflection in [False,True]:
   L=[arb(0),arb(0)]+[arb(v) for v in rr]
   if reflection:L[2],L[6]=L[6],L[2]
   ee=({0:3,1:4,2:2}[e] if reflection else e);ss='R' if reflection else side
   cap=anchor_value(ee,ss,L);gap=phi-cap
   assert gap>arb('0.45'),(ee,ss,gap)
   data.append({'anchor':ee,'side':ss,'rational_ordinary_radii':([rr[4],rr[1],rr[2],rr[3],rr[0]] if reflection else rr),'capacity':interval(cap),'gap':interval(gap)})
 return {'complete_rate':interval(phi),'geometric_balance_failures':failure,'six_anchored_certificates':data,'fourier_terms':M,'precision_bits':ctx.prec,'uniform_certified_gap':'0.45','lobachevsky_tail_bound':'1/(2M) per term'}
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=Path(__file__).with_name('general_anchored_shared_radius_filling_volume_results.json'));a=p.parse_args()
 out={'status':'PASS','scope':'Exact original reduced width-three source/mark and circle contacts; six fixed rational shared-radius witnesses rigorously enclosed with Arb finite Fourier sums and explicit tails. No numerical optimization, universal sector-capacity theorem, or asymptotic sampling claim.','counts':source_packing(),'certificate':certificates()}
 a.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
