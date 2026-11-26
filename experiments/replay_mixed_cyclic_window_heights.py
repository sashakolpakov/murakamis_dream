#!/usr/bin/env python3
"""Independent sine/cotangent replay of universal open-window heights.

Two external boundary circles suffice only because the completed block
localization theorem already gives a holomorphic root on each full bidisk.
No global cyclic word is sampled.
"""
import argparse,hashlib,itertools,json,time
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
from flint import arb,acb,acb_mat,ctx
ROOT=Path(__file__).resolve().parents[1]
I=acb(0,1);PI=arb.pi();CENT=[(Q(7,20),-Q(1,100)),(Q(3,10),-Q(13,250))];RAD=[Q(9,100),Q(8,125)]
def ar(q):
 q=Q(q);return arb(q.numerator)/q.denominator
def pt(z):return acb(ar(Q(str(z.real))),ar(Q(str(z.imag))))
def interval(a,b):return ar(a).union(ar(b))
def params(box,ta,tb):
 return [acb(ar(CENT[t][0]),ar(CENT[t][1]))+ar(RAD[t])*(2*PI*I*interval(box[k],box[k+1])).exp()for k,t in[(0,ta),(2,tb)]]
def propose(word,a,b):
 n=len(word);z=np.array([complex(*map(float,CENT[e]))for e in word for _ in(0,1)],complex)
 def cot(x):return 1/np.tan(np.pi*x)
 for it in range(70):
  f=np.zeros(2*n,complex);J=np.zeros((2*n,2*n),complex)
  for j in range(2*n):
   v=j//2;e=word[v];partner=j+1 if j%2==0 else j-1;ext=a if j==0 else(b if j==2*n-1 else z[j-1 if j%2==0 else j+1]);d=2+e
   f[j]=np.log(2*np.sin(np.pi*(z[j]+z[partner])))+np.log(2*np.sin(np.pi*(z[j]+ext)))-d*np.log(2*np.sin(np.pi*z[j]))+1j*np.pi*(ext-z[partner]+e*(z[j]-.5))
   J[j,j]=np.pi*(cot(z[j]+z[partner])+cot(z[j]+ext)-d*cot(z[j]))+1j*np.pi*e
  for j in range(2*n-1):J[j,j+1]=J[j+1,j]=np.pi*cot(z[j]+z[j+1])+(1j*np.pi if j%2 else -1j*np.pi)
  step=np.linalg.solve(J,f)
  if max(abs(step))>.075:step*=.075/max(abs(step))
  z-=step
  if max(abs(step))<1e-13:break
 if max(abs(f))>1e-9:return None
 Y=np.linalg.inv(J);E=np.zeros((2*n,2),complex);E[0,0]=np.pi*cot(z[0]+a)+1j*np.pi;E[-1,1]=np.pi*cot(z[-1]+b)+1j*np.pi
 return z,Y,-Y@E

def values(z,p,word):
 n=len(z);f=[];jj=[[acb(0)for j in range(n)]for i in range(n)]
 def L(x):return (2*(PI*x).sin()).log()
 def cot(x):return (PI*x).cos()/(PI*x).sin()
 for j in range(n):
  v=j//2;e=word[v];partner=j+1 if j%2==0 else j-1;ext=p[0]if j==0 else(p[1]if j==n-1 else z[j-1 if j%2==0 else j+1]);d=2+e
  f.append(L(z[j]+z[partner])+L(z[j]+ext)-d*L(z[j])+I*PI*(ext-z[partner]+e*(z[j]-ar(Q(1,2)))))
  jj[j][j]=PI*(cot(z[j]+z[partner])+cot(z[j]+ext)-d*cot(z[j]))+I*PI*e
 for j in range(n-1):jj[j][j+1]=jj[j+1][j]=PI*cot(z[j]+z[j+1])+(I*PI if j%2 else -I*PI)
 E=[[acb(0),acb(0)]for j in range(n)];E[0][0]=PI*cot(z[0]+p[0])+I*PI;E[-1][1]=PI*cot(z[-1]+p[1])+I*PI
 return acb_mat([[v]for v in f]),acb_mat(jj),acb_mat(E)

def certify(word,ta,tb,box,height_floor):
 n=2*len(word);mid=[(box[0]+box[1])/2,(box[2]+box[3])/2];p0=params([mid[0],mid[0],mid[1],mid[1]],ta,tb);pp=params(box,ta,tb);pf=[complex(float(v.real.mid()),float(v.imag.mid()))for v in p0]
 prop=propose(word,*pf)
 if prop is None:return False
 z,Yf,Df=prop;zz=[pt(v)for v in z];Y=acb_mat([[pt(v)for v in row]for row in Yf]);D=acb_mat([[pt(v)for v in row]for row in Df]);F0,J0,E0=values(zz,p0,word)
 ident=acb_mat([[int(i==j)for j in range(n)]for i in range(n)])
 # Y is nonsingular since I-YJ0 has row norm strictly below one.
 Epoint=ident-Y*J0
 if not all(sum((abs(Epoint[i,j])for j in range(n)),arb(0))<ar(Q(1,4))for i in range(n)):return False
 dp=[pp[i]-p0[i]for i in(0,1)];DP=acb_mat([[v]for v in dp]);DZ=D*DP;dz=[DZ[i,0]for i in range(n)];lin=Y*(F0+(J0*D+E0)*DP)
 def rem(base,delta):
  boxz=base+acb(arb(0,abs(delta.real).upper()),arb(0,abs(delta.imag).upper()))
  if not(boxz.real>0 and boxz.real<1):return arb.pos_inf()
  return PI**2*abs(1/(PI*boxz).sin()**2)*abs(delta)**2/2
 remlegs=[rem(zz[j],dz[j])for j in range(n)]
 remedges=[rem(zz[j]+zz[j+1],dz[j]+dz[j+1])for j in range(n-1)]
 boundary=[rem(zz[0]+p0[0],dz[0]+dp[0]),rem(zz[-1]+p0[1],dz[-1]+dp[1])]
 rema=[(remedges[j-1]if j else boundary[0])+(remedges[j]if j<n-1 else boundary[1])+(2+word[j//2])*remlegs[j]for j in range(n)]
 bb=[abs(lin[i,0])+sum((abs(Y[i,j])*rema[j]for j in range(n)),arb(0))for i in range(n)]
 if any(not b.is_finite()for b in bb):return False
 for fac in[1.25,1.5,2,1.375,1.75]:
  rad=[Q(max(1,int(np.ceil(float(b.upper())*fac*2**40))),2**40)for b in bb]
  hz=[dz[j]+acb(arb(0,ar(rad[j])),arb(0,ar(rad[j])))for j in range(n)];boxes=[zz[j]+hz[j]for j in range(n)]
  if not all(v.real>ar(Q(23,100))and v.real<ar(Q(9,20))and abs(v.imag)<ar(Q(3,25))for v in boxes+pp):continue
  center=2*(len(word)//2)
  if not all(boxes[j].imag>ar(height_floor)for j in[center,center+1]):continue
  def diff(base,delta):
   return -PI*(PI*delta).sin()/((PI*(base+delta)).sin()*(PI*base).sin())
  dl=[diff(zz[j],hz[j])for j in range(n)];de=[diff(zz[j]+zz[j+1],hz[j]+hz[j+1])for j in range(n-1)];db=[diff(zz[0]+p0[0],hz[0]+dp[0]),diff(zz[-1]+p0[1],hz[-1]+dp[1])]
  dj=[[acb(0)for j in range(n)]for i in range(n)]
  for j in range(n):dj[j][j]=(de[j-1]if j else db[0])+(de[j]if j<n-1 else db[1])-(2+word[j//2])*dl[j]
  for j in range(n-1):dj[j][j+1]=dj[j+1][j]=de[j]
  ee=Epoint-Y*acb_mat(dj)
  if all(bb[i]+sum((abs(ee[i,j])*ar(rad[j])for j in range(n)),arb(0))<ar(rad[i])for i in range(n)):
   return [boxes[center],boxes[center+1]]
 return False

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def decode(adr):
 box=[Q(0),Q(1),Q(0),Q(1)]
 for j,v in enumerate(adr):
  k=2*(j%2);mid=(box[k]+box[k+1])/2;box[k+1-int(v)]=mid
 return box

def main():
 global PI
 ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=256);ap.add_argument('--input',type=Path,default=ROOT/'repro/results/research-mixed-cyclic-window-heights.json');ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-cyclic-window-heights-replay.json');ap.add_argument('--allow-single-case',action='store_true');args=ap.parse_args();ctx.prec=args.precision;PI=arb.pi()
 d=json.loads(args.input.read_text());assert d['status']=='passed';assert d['proof_sha256']==sha(ROOT/'notes/research_mixed_cyclic_critical_height_bounds.md');assert d['script_sha256']==sha(ROOT/'experiments/certify_mixed_cyclic_window_heights.py')
 for p,h in d['dependencies_sha256'].items():assert sha(ROOT/p)==h
 n=d['window_size'];expected=set()
 for bits in itertools.product((0,1),repeat=n-1):
  k=n//2;word=tuple(bits[:k])+(1,)+tuple(bits[k:])
  for a,b in itertools.product((0,1),repeat=2):
   whole=(a,)+word+(b,)
   if whole<=whole[::-1]:expected.add((word,a,b))
 actual={(tuple(c['word']),*c['external_types'])for c in d['cases']}
 if not args.allow_single_case:assert actual==expected
 assert len(actual)==len(d['cases'])
 results=[];start=time.time()
 for c in d['cases']:
  word=tuple(c['word']);ta,tb=c['external_types'];addresses=sorted(c['addresses']);assert len(addresses)==len(set(addresses))
  for x,y in zip(addresses,addresses[1:]):assert not y.startswith(x)
  assert sum((Q(1,2**len(a))for a in addresses),Q(0))==1
  count=refined=0;hulls=None
  for a in addresses:
   stack=[a]
   while stack:
    adr=stack.pop();result=certify(word,ta,tb,decode(adr),Q(d['height_floor']))
    if result and not all(z.real>ar(Q(27,100)) and z.real<ar(Q(33,100)) for z in result):result=False
    if result:
     count+=1;hulls=result if hulls is None else [acb(hulls[i].real.union(result[i].real),hulls[i].imag.union(result[i].imag))for i in(0,1)]
     continue
    assert len(adr)<len(a)+12,(word,ta,tb,adr);stack.extend([adr+'0',adr+'1']);refined+=1
  row={'word':list(word),'external_types':[ta,tb],'author_cells':len(addresses),'replay_cells':count,'refinements':refined,'center_leg_hulls':[[str(z.real),str(z.imag)]for z in hulls]};results.append(row);print(json.dumps(row),flush=True)
 out={'status':'passed','precision':args.precision,'window_size':n,'height_floor':d['height_floor'],'center_real_bounds':['27/100','33/100'],'cases':results,'replay_cells':sum(c['replay_cells']for c in results),'refinements':sum(c['refinements']for c in results),'elapsed_seconds':time.time()-start,'input_sha256':sha(args.input),'script_sha256':sha(__file__),'proof_sha256':sha(ROOT/'notes/research_mixed_cyclic_critical_height_bounds.md'),'dependencies_sha256':d['dependencies_sha256']}
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n');print('PASS independent windows',len(results),flush=True)
if __name__=='__main__':main()
