#!/usr/bin/env python3
"""Independent exact supporting-plane replay; no numerical optimizer."""
from fractions import Fraction as R
from pathlib import Path
from hashlib import sha256
from itertools import product
import argparse,json,time
from flint import arb,acb,ctx
from replay_three_cap_wire_complement import positive_primitive
from replay_three_vertex_directed_packet import action
ROOT=Path(__file__).resolve().parents[1];ii=acb(0,1)
B=[(R(7,50),R(1,5)),(R(0),R(9,5)),(R(1,4),R(9,20)),(R(1,4),R(9,20)),(R(97,600),R(103,600))]
H=[R(10135869,10**8),-R(97895510,10**8),R(300831,10**8),-R(629803,10**8)]
def r(q):return arb(q.numerator)/q.denominator
def value_gradient(point,heights):
 p=arb.pi();x,tau,s,t=[acb(r(point[j]),r(heights[j]))for j in range(4)]
 y=acb(r(point[4]),arb(2).log()/(2*p)+r(heights[4]))
 X=(2*p*ii*x).exp();Y=(2*p*ii*y).exp();U=(-2*p*ii*s).exp();V=(-2*p*ii*t).exp()
 jr=lambda z:positive_primitive(z.real,abs(z.imag))
 cap=-jr(arb(1)/2-x+tau/(2*p))-jr(arb(1)/2-x-tau/(2*p))-2*jr(x)
 cap-=4*jr(arb(1)/4+tau/(4*p))+4*jr(arb(1)/4-tau/(4*p))
 cap+=3*tau.real*(-tau.imag)/(2*p)+tau.imag
 v=cap+(action(s,t,X,Y)-p*ii*(x+y)).real
 lp=abs((p*x+tau/2).cos()).log();lm=abs((p*x-tau/2).cos()).log()
 bx=lp+lm-2*abs((p*x).sin()).log()
 bt=(lp-lm)/(2*p)-((tau/2).tan().asinh()).real/p-3*tau.imag/(2*p)
 px=-2*p*s.imag+abs(1-X*U).log()-abs(1-X).log()
 py=-2*p*t.imag+abs(1-Y*V).log()-abs(1-Y).log()
 fs=abs(X).log()+abs(1-U*V).log()-abs(1-X*U).log()
 ft=abs(Y).log()+abs(1-U*V).log()-abs(1-Y*V).log()
 return v,[bx+px,bt,fs,ft,py]
def expected():
 for axis,end,hs,ht,hy in product((2,3),(0,1),(-R(1,125),R(1,125)),(-R(17,1000),R(3,250)),(-R(1,200),R(1,200))):
  h=H[:];h[2]=hs;h[3]=ht;b=B[:];b[axis]=(b[axis][end],b[axis][end])
  yield ('index_side',axis,end,str(hs),str(ht),str(hy)),b,h+[hy],R(19107,10000)
 for hs,ht,hy in product((-R(1,125),R(1,125)),(-R(17,1000),R(3,250)),(-R(1,200),R(1,200))):
  h=H[:];h[2]=hs;h[3]=ht
  yield ('alias',str(hs),str(ht),str(hy)),B,h+[hy],R(39,20)
 for axis,end,hy in product(range(4),(0,1),(-R(1,200),R(1,200))):
  b=B[:];b[axis]=(b[axis][end],b[axis][end])
  yield ('translation_face',axis,end,str(hy)),b,H+[hy],R(19107,10000)
def coordinates():
 path=ROOT/'repro/results/research-three-phase-graph-transform.json';d=json.loads(path.read_text())
 assert d['status']=='passed'and d['seed_cell_count']==4096 and d['exact_square_cover']
 seen=set()
 for cell in d['seed_cells']:
  ix,iy=cell['cell'];assert(ix,iy)not in seen and 0<=ix<64 and 0<=iy<64;seen.add((ix,iy))
  wanted=[[R(-1,200)+R(j,6400),R(-1,200)+R(j+1,6400)]for j in (ix,iy)]
  assert [[R(v)for v in row]for row in cell['output_box']]==wanted
  z=[]
  for text in cell['coordinate_enclosures']:
   re,im=text[:-1].rsplit(' + ',1);z.append(acb(arb(re),arb(im)))
  x,tau,s,t=z
  assert x.real>r(R(176,1000))and x.real<r(R(179,1000))
  assert x.imag>r(R(9,100))and x.imag<r(R(3,25))
  assert tau.real>r(R(3,2))and tau.real<r(R(31,20))
  assert tau.imag>-1 and tau.imag<-r(R(97,100))
  assert all(w.real>r(R(31,100))and w.real<r(R(39,100))for w in(s,t))
  assert s.imag>-r(R(1,125))and s.imag<r(R(1,125))
  assert t.imag>-r(R(17,1000))and t.imag<r(R(3,250))
 assert len(seen)==4096
 return sha256(path.read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=192)
 ap.add_argument('--output',default='repro/results/research-three-prepared-central-currents-replay.json')
 args=ap.parse_args();ctx.prec=args.precision;start=time.monotonic()
 path=ROOT/'repro/results/research-three-prepared-central-currents.json';data=json.loads(path.read_text());assert data['status']=='passed'
 wanted={key:(b,h,target)for key,b,h,target in expected()};seen=set()
 for item in data['domains']:
  key=tuple(item['domain']);assert key in wanted and key not in seen;seen.add(key)
  b,h,target=wanted[key]
  assert[[R(v)for v in row]for row in item['bounds']]==[list(z)for z in b]
  assert list(map(R,item['heights']))==h and R(item['threshold'])==target
  z=list(map(R,item['support_point']));assert all(a<=v<=c for v,(a,c)in zip(z,b))
  value,g=value_gradient(z,h)
  support=value+sum(max((gj*r(a-zj)).upper(),(gj*r(c-zj)).upper())for gj,zj,(a,c)in zip(g,z,b))
  assert support<r(target),(key,support,target)
 assert seen==set(wanted)and len(seen)==56
 checks=[r(R(19107,10000))-r(R(39,20))+2*arb.pi()/125,
         r(R(27,40))*r(R(21,1000))**2-r(R(1,4000)),
         r(R(3,8))*r(R(3,50))**2-r(R(1,4000)),
         r(R(7,880))*r(R(1,4))**2-r(R(1,4000))]
 assert all(v>0 for v in checks)
 coordinate_hash=coordinates()
 for f,hsh in data['dependencies_sha256'].items():assert sha256((ROOT/f).read_bytes()).hexdigest()==hsh,f
 assert sha256((ROOT/'experiments/certify_three_prepared_central_currents.py').read_bytes()).hexdigest()==data['script_sha256']
 result={'status':'passed','precision_bits':args.precision,'support_planes':len(seen),
         'exact_domain_list':True,'scalar_checks':len(checks),'critical_coordinate_cells_checked':4096,
         'elapsed_seconds':time.monotonic()-start,'artifact_sha256':sha256(path.read_bytes()).hexdigest(),
         'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'critical_artifact_sha256':coordinate_hash,
         'method':'Independent negative-frequency vertex action, reflected cap primitive and real logarithmic gradients; no optimizer.'}
 (ROOT/args.output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
