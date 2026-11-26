#!/usr/bin/env python3
"""Universal open-window height certificate after global root existence.

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
 for it in range(60):
  u=np.exp(-2j*np.pi*z);f=np.zeros(2*n,complex);J=np.zeros((2*n,2*n),complex)
  for v,e in enumerate(word):
   s,t=2*v,2*v+1;pa=a if v==0 else z[s-1];pb=b if v==n-1 else z[t+1];A=np.exp(-2j*np.pi*pa);B=np.exp(-2j*np.pi*pb);d=2+e;off=2j*np.pi*u[s]*u[t]/(1-u[s]*u[t])
   f[s]=np.log(1-u[s]*u[t])+np.log(1-u[s]*A)-d*np.log(1-u[s])+2j*np.pi*pa
   f[t]=np.log(1-u[s]*u[t])+np.log(1-u[t]*B)-d*np.log(1-u[t])+2j*np.pi*pb
   J[s,s]=off+2j*np.pi*(u[s]*A/(1-u[s]*A)-d*u[s]/(1-u[s]));J[t,t]=off+2j*np.pi*(u[t]*B/(1-u[t]*B)-d*u[t]/(1-u[t]));J[s,t]=J[t,s]=off
   if v>0:J[s,s-1]=2j*np.pi/(1-u[s]*A)
   if v<n-1:J[t,t+1]=2j*np.pi/(1-u[t]*B)
  step=np.linalg.solve(J,f)
  if max(abs(step))>.08:step*=.08/max(abs(step))
  z-=step
  if max(abs(step))<1e-13:break
 if max(abs(f))>1e-9:return None
 Y=np.linalg.inv(J);E=np.zeros((2*n,2),complex);E[0,0]=2j*np.pi/(1-np.exp(-2j*np.pi*(z[0]+a)));E[-1,1]=2j*np.pi/(1-np.exp(-2j*np.pi*(z[-1]+b)))
 return z,Y,-Y@E

def values(z,p,word):
 n=len(z);f=[];jj=[[acb(0)for j in range(n)]for i in range(n)]
 def L(x):return (1-(-2*PI*I*x).exp()).log()
 def G(x):
  q=(-2*PI*I*x).exp();return 2*PI*I*q/(1-q)
 for j in range(n):
  v=j//2;partner=j+1 if j%2==0 else j-1;ext=p[0]if j==0 else(p[1]if j==n-1 else z[j-1 if j%2==0 else j+1]);d=2+word[v]
  f.append(L(z[j]+z[partner])+L(z[j]+ext)-d*L(z[j])+2*PI*I*ext)
  jj[j][j]=G(z[j]+z[partner])+G(z[j]+ext)-d*G(z[j])
 for j in range(n-1):jj[j][j+1]=jj[j+1][j]=G(z[j]+z[j+1])+(2*PI*I if j%2 else 0)
 E=[[acb(0),acb(0)]for j in range(n)];E[0][0]=2*PI*I/(1-(-2*PI*I*(z[0]+p[0])).exp());E[-1][1]=2*PI*I/(1-(-2*PI*I*(z[-1]+p[1])).exp())
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
  q=(-2*PI*I*boxz).exp();return 2*PI**2*abs(q/(1-q)**2)*abs(delta)**2
 remlegs=[rem(zz[j],dz[j])for j in range(n)]
 remedges=[rem(zz[j]+zz[j+1],dz[j]+dz[j+1])for j in range(n-1)]
 boundary=[rem(zz[0]+p0[0],dz[0]+dp[0]),rem(zz[-1]+p0[1],dz[-1]+dp[1])]
 rema=[(remedges[j-1]if j else boundary[0])+(remedges[j]if j<n-1 else boundary[1])+(2+word[j//2])*remlegs[j]for j in range(n)]
 bb=[abs(lin[i,0])+sum((abs(Y[i,j])*rema[j]for j in range(n)),arb(0))for i in range(n)]
 if any(not b.is_finite()for b in bb):return False
 for fac in[1.25,1.5,2]:
  rad=[Q(max(1,int(np.ceil(float(b.upper())*fac*2**40))),2**40)for b in bb]
  hz=[dz[j]+acb(arb(0,ar(rad[j])),arb(0,ar(rad[j])))for j in range(n)];boxes=[zz[j]+hz[j]for j in range(n)]
  if not all(v.real>ar(Q(23,100))and v.real<ar(Q(9,20))and abs(v.imag)<ar(Q(3,25))for v in boxes+pp):continue
  center=2*(len(word)//2)
  if not all(boxes[j].imag>ar(height_floor)for j in[center,center+1]):continue
  def diff(base,delta):
   q=(-2*PI*I*base).exp();dq=q*((-2*PI*I*delta).exp()-1);return 2*PI*I*dq/((1-q-dq)*(1-q))
  dl=[diff(zz[j],hz[j])for j in range(n)];de=[diff(zz[j]+zz[j+1],hz[j]+hz[j+1])for j in range(n-1)];db=[diff(zz[0]+p0[0],hz[0]+dp[0]),diff(zz[-1]+p0[1],hz[-1]+dp[1])]
  dj=[[acb(0)for j in range(n)]for i in range(n)]
  for j in range(n):dj[j][j]=(de[j-1]if j else db[0])+(de[j]if j<n-1 else db[1])-(2+word[j//2])*dl[j]
  for j in range(n-1):dj[j][j+1]=dj[j+1][j]=de[j]
  ee=Epoint-Y*acb_mat(dj)
  if all(bb[i]+sum((abs(ee[i,j])*ar(rad[j])for j in range(n)),arb(0))<ar(rad[i])for i in range(n)):
   return [boxes[center],boxes[center+1]]
 return False

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 global PI
 ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=160);ap.add_argument('--size',type=int,default=5);ap.add_argument('--floor',default='-57/1000');ap.add_argument('--case',nargs=3);ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-cyclic-window-heights.json');args=ap.parse_args();ctx.prec=args.precision;PI=arb.pi();assert args.size%2==1
 if args.case:cases=[(tuple(map(int,args.case[0])),int(args.case[1]),int(args.case[2]))]
 else:
  cases=[]
  for bits in itertools.product((0,1),repeat=args.size-1):
   k=args.size//2;word=tuple(bits[:k])+(1,)+tuple(bits[k:])
   for a,b in itertools.product((0,1),repeat=2):
    whole=(a,)+word+(b,)
    if whole<=whole[::-1]:cases.append((word,a,b))
 allcases=[];start=time.time()
 for word,ta,tb in cases:
  stack=[('',[Q(0),Q(1),Q(0),Q(1)])];leaves=[];vis=0;t0=time.time();hulls=None
  while stack:
   adr,box=stack.pop();vis+=1;assert len(adr)<=26,(word,ta,tb,adr,box)
   result=certify(word,ta,tb,box,Q(args.floor))
   if result:
    leaves.append(adr)
    hulls=result if hulls is None else [acb(hulls[i].real.union(result[i].real),hulls[i].imag.union(result[i].imag))for i in(0,1)]
    continue
   k=2*(len(adr)%2);mid=(box[k]+box[k+1])/2
   for bit in(0,1):child=box.copy();child[k+1-bit]=mid;stack.append((adr+str(bit),child))
  assert sum((Q(1,2**len(a))for a in leaves),Q(0))==1
  row={'word':list(word),'external_types':[ta,tb],'addresses':leaves,'accepted':len(leaves),'visited':vis,'elapsed_seconds':time.time()-t0,'center_leg_hulls':[[str(z.real),str(z.imag)]for z in hulls]};allcases.append(row);print(json.dumps({k:v for k,v in row.items()if k!='addresses'}),flush=True)
  partial={'status':'running','cases':allcases};Path(str(args.output)+'.partial').write_text(json.dumps(partial,separators=(',',':'))+'\n')
 deps=['notes/research_mixed_cyclic_critical_localization.md','repro/results/research-mixed-cyclic-block-localization.json','repro/results/research-mixed-cyclic-block-localization-replay.json']
 out={'status':'passed','precision':args.precision,'window_size':args.size,'height_floor':args.floor,'cases':allcases,'elapsed_seconds':time.time()-start,'script_sha256':sha(__file__),'proof_sha256':sha(ROOT/'notes/research_mixed_cyclic_critical_height_bounds.md'),'dependencies_sha256':{p:sha(ROOT/p)for p in deps}}
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n');Path(str(args.output)+'.partial').unlink(missing_ok=True);print('PASS',len(cases),'universal windows',flush=True)
if __name__=='__main__':main()
