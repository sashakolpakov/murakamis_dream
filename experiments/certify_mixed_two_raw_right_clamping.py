#!/usr/bin/env python3
"""Complete two-real-parameter clamp with two independent raw right rows."""
import argparse,hashlib,importlib.util,itertools,json,time
from fractions import Fraction as F
from pathlib import Path
from flint import acb,arb
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_two_raw_right_clamping.md'
HELPER=ROOT/'experiments/certify_mixed_raw_coherent_right_clamping.py'
sp=importlib.util.spec_from_file_location('two_raw_clamp_arithmetic',HELPER)
b=importlib.util.module_from_spec(sp);sp.loader.exec_module(b)
ar=b.ar;sha=b.sha

def configure(bits):
 global pi,ii
 b.configure(bits);pi,ii=b.pi,b.ii

def specifications():return[list(v)for v in itertools.product((0,1),repeat=2)]

def params(box,case):
 alpha,beta=case;t=ar('.45')+ar('.05')*ar(box[0][0]).union(ar(box[0][1]))
 kl,kh=b.K[alpha];dk=ar(kh-kl);k=ar(kl)+dk*ar(box[1][0]).union(ar(box[1][1]))
 R=400*(ar('.5')-t)**2;Rp=-800*(ar('.5')-t);q=1+ii*k*Rp;z=acb(t,k*R)
 dz=[ar('.05')*q,ii*dk*R];dq=[ii*40*k,ii*dk*Rp]
 return z,dz,q,dq

def test(box,case,witness=None):
 assert witness is None
 z,dz,q,dq=params(box,case);mid=[((lo+hi)/2,(lo+hi)/2)for lo,hi in box]
 z0,_,q0,_=params(mid,case);alpha,beta=case;G=acb(0);G0=acb(0);dg=[acb(0),acb(0)]
 for d,eps in((0,alpha),(1,beta)):
  u=b.raw_row(z,z0,eps,d);u0=b.raw_row(z0,z0,eps,d)
  raw=b.raw_data(z,u,alpha,eps,d);raw0=b.raw_data(z0,u0,alpha,eps,d)
  if raw is None or raw0 is None:return None,None,None
  K,Kz,Ku,Tu=raw;G+=K;G0+=raw0[0]
  for j in range(2):
   up=-(Ku*dz[j]).real/Tu;dg[j]+=Kz*dz[j]+Ku*up
 fv=(q*G).real;fc=(q0*G0).real;grads=[(q*dd+qq*G).real for dd,qq in zip(dg,dq)]
 if not all(v.is_finite()for v in[fc,fv]+grads):return None,None,None
 mv=fc+sum((abs(g)*ar((hi-lo)/2)for g,(lo,hi)in zip(grads,box)),arb(0))
 return min(fv.upper(),mv.upper()),grads,None

def choose(box,case,grads):
 if grads is not None:return max(((abs(grads[j])*ar(hi-lo)).upper(),j)for j,(lo,hi)in enumerate(box)if hi>lo)[1]
 _,dz,_,_=params([((lo+hi)/2,(lo+hi)/2)for lo,hi in box],case)
 return max(((abs(dz[j])*ar(hi-lo)).upper(),j)for j,(lo,hi)in enumerate(box)if hi>lo)[1]

def bindings():
 deps,records=b.bindings();deps[str(HELPER.relative_to(ROOT))]=sha(HELPER)
 return deps,records

def exact_checks():return b.exact_checks()
def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--precision',type=int,default=256);ap.add_argument('--input',type=Path)
 ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-two-raw-right-clamping.json')
 ap.add_argument('--max-visits',type=int,default=100000);ap.add_argument('--seconds',type=float,default=120)
 ap.add_argument('--first',type=int,default=0);ap.add_argument('--last',type=int,default=4)
 args=ap.parse_args();assert args.precision>=160 and 0<=args.first<args.last<=4
 started=time.monotonic();configure(args.precision);ph,sh=sha(PROOF),sha(__file__)
 deps,primary=bindings();exact=exact_checks();specs=specifications();assert len(specs)==4
 ih=sha(args.input)if args.input else None;saved=json.loads(args.input.read_text())if args.input else None
 if saved:
  assert saved['status']=='passed'and saved['products']==4
  assert saved['proof_sha256']==ph and saved['script_sha256']==sh and saved['dependencies_sha256']==deps
  assert len(saved['cases'])==4
 records=[];totalvisits=0;status='passed'
 for index in range(args.first,args.last):
  case=specs[index];old=saved['cases'][index]if saved else None
  if old:assert old['index']==index and old['case']==case
  stack=[[(F(0),F(1))for _ in range(2)]];nodes=[];cursor=leaves=visits=monotone=0;worst=None
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
    if upper is not None and upper<-ar(F(1,20)):
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
 if status=='passed'and(args.first,args.last)!=(0,4):status='passed_subset'
 assert ph==sha(PROOF)and sh==sha(__file__)
 assert all(sha(ROOT/path)==digest for path,digest in deps.items())
 if saved:assert ih==sha(args.input)
 result=dict(status=status,precision_bits=args.precision,products=len(records),product_range=[args.first,args.last],cases=records,
             leaves=sum(x['leaves']for x in records),visits=totalvisits,monotone_reductions=sum(x['monotone']for x in records),
             derivative_upper_bound='-1/20',complex_roots_per_cell=0,raw_scalar_roots_per_cell=2,
             exact_identities=exact,primary_records=primary,proof_sha256=ph,script_sha256=sh,
             dependencies_sha256=deps,input_sha256=ih,elapsed_seconds=time.monotonic()-started,
             scope='Unselected upper-taper center between two independent raw right edges fixed at .5. Upper-rate clamping only; no raw kernel lower bound or full-period conclusion.')
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n')
 print(status.upper(),len(records),result['leaves'],result['visits'],flush=True)

if __name__=='__main__':main()
