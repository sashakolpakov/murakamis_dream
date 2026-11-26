#!/usr/bin/env python3
"""Independent original-sine/positive-frequency replay of critical-image packets.

No author acceptance function is imported. Stored rational affine witnesses
are independently validated before any source/contour inequality is tested.
"""
import argparse, hashlib, itertools, json, time
from pathlib import Path
from fractions import Fraction as Q
from flint import arb, acb, acb_mat, ctx
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_conditional_critical_images.md'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--precision',type=int,default=320);ap.add_argument('--input',type=Path,default=ROOT/'repro/results/research-mixed-conditional-critical-images.json');ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-conditional-critical-images-replay.json');args=ap.parse_args();ctx.prec=args.precision
 input_bytes=args.input.read_bytes();input_hash=hashlib.sha256(input_bytes).hexdigest();script_hash=sha(__file__)
 data=json.loads(input_bytes);assert data['status']=='passed' and data['proof_sha256']==sha(PROOF) and data['script_sha256']==sha(ROOT/'experiments/certify_mixed_conditional_critical_images.py')
 for p,h in data['dependencies'].items():assert sha(ROOT/p)==h,p
 pi=arb.pi();ii=acb(0,1)
 def ar(q):q=Q(q);return arb(q.numerator)/q.denominator
 def pt(x):return acb(ar(x[0]),ar(x[1]))
 def cot(z):return (pi*z).cos()/(pi*z).sin()
 def J(z):return -((2*pi*ii*z).exp().polylog(2)-pi*pi/6)/(2*pi*ii)+ii*pi*(z-z*z)/2
 def g(z):return J(z)+ii*pi*(z-z*z)/2
 def gp(z):return (1-(-2*pi*ii*z).exp()).log()
 def ph(s,a,t,d):return g(s+a)+g(s+t)-d*g(s)+2*pi*ii*a*s
 def decode(code):
  box=[Q(0),Q(1),Q(0),Q(1)]
  for j,c in enumerate(code):k=2*(j%2);mid=(box[k]+box[k+1])/2;box[k+1-int(c)]=mid
  return box
 corners=[acb(ar(x),ar(y))for x,y in [('27/100','-57/1000'),('33/100','-57/1000'),('33/100','-1/1000'),('27/100','-1/1000')]]
 def boundary(kind,part,theta):
  if kind==0:return acb(ar('7/20'),-ar('1/100'))+ar('83/1000')*(2*pi*ii*theta).exp()
  return corners[part]+theta*(corners[(part+1)%4]-corners[part])
 def tangent(kind,part,p):return 2*pi*ii*(p-acb(ar('7/20'),-ar('1/100')))if kind==0 else corners[(part+1)%4]-corners[part]
 def evalf(z,p,e):
  s,t=z;a,b=p;d=2+e;L=lambda x:(2*(pi*x).sin()).log()
  f=acb_mat([[L(s+t)+L(s+a)-d*L(s)+ii*pi*(a-t+e*(s-ar('1/2')))], [L(s+t)+L(t+b)-d*L(t)+ii*pi*(b-s+e*(t-ar('1/2')))]])
  off=pi*cot(s+t)-ii*pi
  H=acb_mat([[pi*(cot(s+t)+cot(s+a)-d*cot(s))+ii*pi*e,off],[off,pi*(cot(s+t)+cot(t+b)-d*cot(t))+ii*pi*e]])
  E=acb_mat([[pi*cot(s+a)+ii*pi,0],[0,pi*cot(t+b)+ii*pi]])
  return f,H,E
 Id=acb_mat([[1,0],[0,1]])
 def valid_witness(w,types,parts):
  e,ta,tb=types;box=decode(w['address']);pp=[];p0=[]
  for j,kind in enumerate((ta,tb)):
   lo,hi=box[2*j:2*j+2];pp.append(boundary(kind,parts[j],ar(lo).union(ar(hi))));p0.append(boundary(kind,parts[j],ar((lo+hi)/2)))
  zz=list(map(pt,w['root_centers']));D=acb_mat([[pt(v)for v in row]for row in w['affine_matrix']]);r=list(map(ar,w['affine_radii']));dp=acb_mat([[pp[j]-p0[j]]for j in (0,1)]);dz=[sum((D[j,k]*dp[k,0]for k in(0,1)),acb(0))for j in(0,1)]
  f0,H0,E0=evalf(zz,p0,e);Y=H0.inv();point=Id-Y*H0
  assert all(sum(abs(point[i,j])for j in(0,1))<ar('1/4')for i in(0,1))
  lin=Y*(f0+(H0*D+E0)*dp)
  def rem(base,delta):
   v=base+acb(arb(0,abs(delta.real).upper()),arb(0,abs(delta.imag).upper()));assert 0<v.real<1
   return pi*pi*abs(1/(pi*v).sin()**2)*abs(delta)**2/2
  common=rem(zz[0]+zz[1],dz[0]+dz[1]);rema=[]
  for i in(0,1):rema.append(common+rem(zz[i]+p0[i],dz[i]+dp[i,0])+(2+e)*rem(zz[i],dz[i]))
  bnd=[abs(lin[i,0])+sum(abs(Y[i,j])*rema[j]for j in(0,1))for i in(0,1)]
  hz=[dz[j]+acb(arb(0,r[j]),arb(0,r[j]))for j in(0,1)];zb=[zz[j]+hz[j]for j in(0,1)]
  assert all(ar('23/100')<v.real<ar('9/20') and abs(v.imag)<ar('3/25')for v in pp+zb)
  def dc(base,delta):return -pi*(pi*delta).sin()/((pi*base).sin()*(pi*(base+delta)).sin())
  off=dc(sum(zz),sum(hz));diag=[off+dc(zz[i]+p0[i],hz[i]+dp[i,0])-(2+e)*dc(zz[i],hz[i])for i in(0,1)]
  EE=point-Y*acb_mat([[diag[0],off],[off,diag[1]]])
  assert all(bnd[i]+sum(abs(EE[i,j])*r[j]for j in(0,1))<r[i]for i in(0,1)),('affine',types,parts,w['address'])
  rr=ar('1e-11');zp=[v+acb(arb(0,rr),arb(0,rr))for v in zz];Ep=Id-Y*evalf(zp,p0,e)[1];fp=Y*f0
  assert all(abs(fp[i,0])+sum(abs(Ep[i,j])*rr for j in(0,1))<rr for i in(0,1)),('point',types,parts,w['address'])
  # Exact two-by-two inverse, with original sine/cotangent derivatives.
  # This avoids interval Gaussian elimination and its repeated dependency.
  common=pi*cot(sum(zb))-ii*pi
  diagonals=[common+pi*cot(zb[j]+pp[j])-(2+e)*pi*cot(zb[j])+(1+e)*ii*pi for j in(0,1)]
  ext=[pi*cot(zb[j]+pp[j])+ii*pi for j in(0,1)]
  det=diagonals[0]*diagonals[1]-common*common
  response=acb_mat([[-diagonals[1]*ext[0]/det,common*ext[1]/det],
                    [common*ext[0]/det,-diagonals[0]*ext[1]/det]])
  return box,pp,p0,zb,zp,response
 expected={(e,a,b,pa,pb)for e in(0,1)for a,b in((0,0),(0,1),(1,1))for pa in range(1 if a==0 else 4)for pb in range(1 if b==0 else 4)}
 got={(tuple(c['types'])+tuple(c['parts']))for c in data['cases']};assert got==expected and len(got)==len(data['cases'])==42
 results=[];start=time.time();total=0
 for case in data['cases']:
  types=case['types'];parts=case['parts'];e,ta,tb=types;codes=sorted(case['addresses']);assert len(codes)==len(set(codes));assert all(not y.startswith(x)for x,y in zip(codes,codes[1:]));assert sum((Q(1,2**len(x))for x in codes),Q(0))==1
  assert sorted(w['address']for w in case['witnesses'])==codes
  ng=na=0
  for w in case['witnesses']:
   box,pp,p0,zb,zp,D=valid_witness(w,types,parts);dt=[ar((box[2*j+1]-box[2*j])/2)for j in(0,1)];tan=[tangent(t,parts[j],pp[j])for j,t in enumerate((ta,tb))]
   for side in(0,1):
    a=pp[side];s=zb[side];t=zb[1-side];a0=p0[side];s0=zp[side];t0=zp[1-side];d=2+e;selected=ph(s0,a0,t0,d);ga=gp(s+a)+2*pi*ii*s;gt=gp(s+t)
    def lower(val,da,dtv):
     deriv=[((da if j==side else 0)+dtv*D[1-side,j])*tan[j]for j in(0,1)]
     return val.real-sum(abs(v.real)*dt[j]for j,v in enumerate(deriv))
    for cut in('3/20','49/100'):
     c=acb(ar(cut));gap=lower(selected-ph(c,a0,t0,d),ga-gp(c+a)-2*pi*ii*c,gt-gp(c+t));assert gap>ar('1/10000'),('endpoint',types,parts,w['address'],side,cut,str(gap));ng+=1
    for k,l in itertools.product((0,1),repeat=2):
     gap=lower(selected-g(a0)-g(t0)-2*pi*ii*k*a0+2*pi*ii*l*t0,ga-gp(a)-2*pi*ii*k,gt-gp(t)+2*pi*ii*l);assert gap>ar('1/10000'),('revived',types,parts,w['address'],side,k,l,str(gap));ng+=1
    qa=(2*pi*a.real).sin()/((2*pi*a.imag).cosh()-(2*pi*a.real).cos());qt=(2*pi*t.real).sin()/((2*pi*t.imag).cosh()-(2*pi*t.real).cos());right=max(qa.upper(),qt.upper());left=-cot(acb(ar('49/100'))).real
    ca,sa=(pi*a).cos(),(pi*a).sin();ct,st=(pi*t).cos(),(pi*t).sin();factor=(2*pi*(t.imag-a.imag)).exp()/4**e
    for j in range(12):
     v=(left+(right-left)*j/12).union(left+(right-left)*(j+1)/12);polynomial=factor*abs(ca-v*sa)**2*abs(ct-v*st)**2*(1+v*v)**e
     assert polynomial<1,('tail shape',types,parts,w['address'],side,j,str(polynomial))
    for sign in(-1,1):
     for j in range(8):
      x=ar(Q(3,20)+Q(34,100)*Q(j,8)).union(ar(Q(3,20)+Q(34,100)*Q(j+1,8)));c=acb(x,sign*ar('1/5'))
      gap=lower(selected-ph(c,a0,t0,d),ga-gp(c+a)-2*pi*ii*c,gt-gp(c+t))+2*pi/5
      assert gap>ar('1/1000'),('alias',types,parts,w['address'],side,sign,j,str(gap));na+=1
   total+=1
  row={'types':types,'parts':parts,'cells':len(codes),'endpoint_checks':ng,'alias_checks':na};results.append(row);print(json.dumps(row),flush=True)
 assert sha(args.input)==input_hash and sha(__file__)==script_hash and sha(PROOF)==data['proof_sha256']
 for p,h in data['dependencies'].items():assert sha(ROOT/p)==h,p
 out={'status':'passed','precision_bits':args.precision,'scope':data['scope'],'boundary_pieces':42,'replay_cells':total,'refinements':0,'cases':results,'elapsed_seconds':time.time()-start,'input_sha256':input_hash,'script_sha256':script_hash,'proof_sha256':sha(PROOF),'dependencies':data['dependencies'],'independent_method':'Original sine logarithms and cotangent differences validate each saved rational affine witness; positive-frequency dilogarithm phase and explicit two-by-two cotangent response verify all source gaps.'}
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n');print('PASS independent critical images',total,flush=True)
if __name__=='__main__':main()
