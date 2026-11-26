#!/usr/bin/env python3
"""Saved complete top-edge comparisons for a selected height beside raw R."""
import argparse,hashlib,importlib.util,itertools,json,time
from fractions import Fraction as F
from pathlib import Path
from flint import acb,arb
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_raw_coherent_height_bounds.md'
HELPER=ROOT/'experiments/certify_mixed_raw_coherent_right_clamping.py'
sp=importlib.util.spec_from_file_location('mixed_height_arithmetic',HELPER)
b=importlib.util.module_from_spec(sp);sp.loader.exec_module(b)
ar=b.ar;sha=b.sha

def configure(bits):
 global pi,ii
 b.configure(bits);pi,ii=b.pi,b.ii

def polygon(ty,clipped):
 p=[(F(x),F(y))for x,y in b.OMEGA[ty]]
 return b.m.m.clip(p,F('.16'),True)if clipped else p

def specifications():
 ans=[]
 for clipped in(0,1):
  for d,beta in((0,0),(1,0),(1,1)):
   for other in(0,1):
    for face in range(len(polygon(other,clipped))):ans.append([clipped,d,beta,other,face])
 assert len(ans)==75
 return ans+[[2,beta,0,0,0]for beta in(0,1)]

def params(box,case):
 t=ar('.45')+ar('.05')*ar(box[1][0]).union(ar(box[1][1]))
 z=acb(t,ar('.28')*(ar('.5')-t));dz=[acb(0),ar('.05')*(1-ii*ar('.28'))]
 if case[0]==2:return None,z,None,dz
 clipped,d,beta,other,face=case;p=polygon(other,clipped)
 aa,bb=p[face],p[(face+1)%len(p)];vel=acb(ar(bb[0]-aa[0]),ar(bb[1]-aa[1]))
 a=acb(ar(aa[0]),ar(aa[1]))+vel*ar(box[0][0]).union(ar(box[0][1]))
 return a,z,[vel,acb(0)],dz

def test(box,case,witness=None):
 a,z,da,dz=params(box,case);mid=[((lo+hi)/2,(lo+hi)/2)for lo,hi in box]
 a0,z0,_,_=params(mid,case)
 if case[0]==2:
  assert witness is None
  G=acb(0);G0=acb(0);dg=[acb(0),acb(0)]
  rawcases=((0,1),(1,case[1]));wit=None
 else:
  clipped,d,beta,other,face=case
  if d:left,right,l0,r0,eta,eps,ci,oi=a,z,a0,z0,other,1,1,0
  else:left,right,l0,r0,eta,eps,ci,oi=z,a,z0,a0,1,other,0,1
  if witness is not None:assert F(0)<F(witness['radius'])<=F(1,20)
  packet=b.m.root_box(left,right,l0,r0,eps,witness)
  if packet is None:return None,None,None
  s,s0,wit=packet;assert F(0)<F(wit['radius'])<=F(1,20)
  GG,H=b.m.gradH(s,left,right,eta,eps);GG0,_=b.m.gradH(s0,l0,r0,eta,eps)
  G=GG[ci];G0=GG0[ci];dg=[H[ci][oi]*da[j]+H[ci][ci]*dz[j]for j in range(2)]
  rawcases=((d,beta if d else 1),)
 for d,eps in rawcases:
  u=b.raw_row(z,z0,eps,d);u0=b.raw_row(z0,z0,eps,d)
  raw=b.raw_data(z,u,1,eps,d);raw0=b.raw_data(z0,u0,1,eps,d)
  if raw is None or raw0 is None:return None,None,None
  K,Kz,Ku,Tu=raw;G+=K;G0+=raw0[0]
  for j in range(2):
   up=-(Ku*dz[j]).real/Tu;dg[j]+=Kz*dz[j]+Ku*up
 fv=-G.imag;fc=-G0.imag;grads=[-v.imag for v in dg]
 if not all(v.is_finite()for v in[fc,fv]+grads):return None,None,None
 mv=fc+sum((abs(g)*ar((hi-lo)/2)for g,(lo,hi)in zip(grads,box)),arb(0))
 return min(fv.upper(),mv.upper()),grads,wit

def choose(box,case,grads):
 if grads is not None:return max(((abs(grads[j])*ar(hi-lo)).upper(),j)for j,(lo,hi)in enumerate(box)if hi>lo)[1]
 _,_,da,dz=params([((lo+hi)/2,(lo+hi)/2)for lo,hi in box],case)
 return max((((abs(dz[j])+(abs(da[j])if da else 0))*ar(hi-lo)).upper(),j)for j,(lo,hi)in enumerate(box)if hi>lo)[1]

def bindings():
 deps,records=b.bindings()
 for p in('experiments/certify_mixed_raw_coherent_right_clamping.py',
          'notes/research_mixed_raw_coherent_height_comparison.md',
          'notes/research_mixed_right_selected_height_removal.md'):
  deps[p]=sha(ROOT/p)
 return deps,records

def exact_checks():
 assert len(polygon(0,0))==len(polygon(1,0))==6
 assert len(polygon(0,1))==7 and len(polygon(1,1))==6
 assert F('.014')*20==F('.28')
 assert F('.028')*F(3)-F('.0426')>0
 # log(2sin(.45pi))>.639 and exact pi bounds pay the original two branches.
 assert (2*(pi*ar('.45')).sin()).log()>ar('.639')
 assert ar('.028')*pi-ar('.0426')>0
 return ['exact clipped edge counts','top-edge affine height','frequency reserve','factorial reserve']
def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--precision',type=int,default=256);ap.add_argument('--input',type=Path)
 ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-raw-coherent-height-bounds.json')
 ap.add_argument('--max-visits',type=int,default=100000);ap.add_argument('--seconds',type=float,default=120)
 ap.add_argument('--first',type=int,default=0);ap.add_argument('--last',type=int,default=77)
 args=ap.parse_args();assert args.precision>=160 and 0<=args.first<args.last<=77
 started=time.monotonic();configure(args.precision);ph,sh=sha(PROOF),sha(__file__)
 deps,primary=bindings();exact=exact_checks();specs=specifications();assert len(specs)==77
 ih=sha(args.input)if args.input else None;saved=json.loads(args.input.read_text())if args.input else None
 if saved:
  assert saved['status']=='passed'and saved['products']==77
  assert saved['proof_sha256']==ph and saved['script_sha256']==sh and saved['dependencies_sha256']==deps
  assert len(saved['cases'])==77
 records=[];totalvisits=0;status='passed'
 for index in range(args.first,args.last):
  case=specs[index];threshold=ar(F(3,5)if case[0]==0 else F(9,20));old=saved['cases'][index]if saved else None
  if old:assert old['index']==index and old['case']==case
  stack=[[(F(0),F(0)if case[0]==2 else F(1)),(F(0),F(1))]];nodes=[];cursor=leaves=visits=monotone=0;worst=None
  while stack:
   if saved is None and(totalvisits>=args.max_visits or time.monotonic()-started>=args.seconds):status='incomplete';break
   box=stack.pop();visits+=1;totalvisits+=1
   node=old['nodes'][cursor]if old else None;cursor+=bool(old)
   if node and node[0]=='S':
    _,axis=node;assert type(axis)is int and 0<=axis<2 and box[axis][0]<box[axis][1]
   else:
    assert node is None or node[0]in('L','M')
    upper,grads,wit=test(box,case,node[-1]if node else None)
    if node and node[0]=='M':
     _,axis,bit,_=node;assert type(axis)is int and 0<=axis<2 and bit in(0,1)
     assert box[axis][0]<box[axis][1]and grads is not None
     assert(grads[axis]>0 if bit else grads[axis]<0)
     point=box[axis][bit];reduced=list(box);reduced[axis]=(point,point)
     nodes.append(node);stack.append(reduced);monotone+=1;continue
    if upper is not None and upper<threshold:
     assert node is None or node[0]=='L';nodes.append(['L',wit]);leaves+=1
     worst=upper if worst is None else max(worst,upper);continue
    assert old is None,('saved leaf failure',index,box,str(upper))
    signed=[]
    if grads is not None:
     for j,(lo,hi)in enumerate(box):
      if hi>lo and(grads[j]>0 or grads[j]<0):signed.append(((abs(grads[j])*ar(hi-lo)).upper(),j,int(grads[j]>0)))
    if signed:
     _,axis,bit=max(signed);nodes.append(['M',axis,bit,wit]);reduced=list(box)
     point=box[axis][bit];reduced[axis]=(point,point);stack.append(reduced);monotone+=1;continue
    assert any(lo<hi for lo,hi in box),('point did not pass',index,box,str(upper))
    axis=choose(box,case,grads)
   lo,hi=box[axis];assert lo<hi and(max(lo.denominator,hi.denominator).bit_length()<65)
   middle=(lo+hi)/2;nodes.append(['S',axis]);left=list(box);right=list(box)
   left[axis]=(lo,middle);right[axis]=(middle,hi);stack.extend((left,right))
  if old:
   assert not stack and cursor==len(old['nodes'])
   assert(leaves,visits,monotone)==(old['leaves'],old['visits'],old['monotone'])
  records.append(dict(index=index,case=case,leaves=leaves,visits=visits,monotone=monotone,nodes=nodes,
                      remaining_boxes=len(stack),maximum_derivative_upper=str(worst)))
  print('product',index+1,'leaves',leaves,'visits',visits,'M',monotone,'elapsed',round(time.monotonic()-started,2),'upper',worst,flush=True)
  if status=='incomplete':break
 if status=='passed'and(args.first,args.last)!=(0,77):status='passed_subset'
 assert ph==sha(PROOF)and sh==sha(__file__)
 assert all(sha(ROOT/path)==digest for path,digest in deps.items())
 if saved:assert ih==sha(args.input)
 result=dict(status=status,precision_bits=args.precision,products=len(records),product_range=[args.first,args.last],cases=records,
             leaves=sum(x['leaves']for x in records),visits=totalvisits,monotone_reductions=sum(x['monotone']for x in records),
             imaginary_lower_bounds=['-3/5','-9/20'],
             exact_identities=exact,primary_records=primary,proof_sha256=ph,script_sha256=sh,
             dependencies_sha256=deps,input_sha256=ih,elapsed_seconds=time.monotonic()-started,
             scope='Top-edge imaginary marginal bounds for mixed coherent/raw and double-raw centers; height convexity extends to W. Full selected height removal through explicit source comparison, no selected horizontal clamping or full-period conclusion.')
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n')
 print(status.upper(),len(records),result['leaves'],result['visits'],flush=True)

if __name__=='__main__':main()
