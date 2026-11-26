"""Complete conditional source on an enlarged positive type-four transition cap."""
import argparse,itertools,json,math,time,hashlib
from pathlib import Path
import sympy as sp
from fractions import Fraction as Fr
import numpy as np
from scipy.optimize import brentq
from flint import arb,acb,ctx
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_early_selected_source_cap.md'
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
pa=argparse.ArgumentParser(description=__doc__);pa.add_argument('--precision',type=int,default=256);pa.add_argument('--max-visits',type=int,default=250000);pa.add_argument('--input',type=Path);pa.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-early-selected-source-cap.json');args=pa.parse_args();assert args.precision>=128;ctx.prec=args.precision
proof_hash=sha(PROOF);script_hash=sha(__file__);dependencies={}
for stem in ('mixed_global_cotangent_roots','mixed_minimum_neighbor_contour','mixed_complex_horizontal_obstruction','lower_half_factorial_continuation','mixed_all_real_conditional_packet','mixed_transition_whole_period_source'):
 pp='notes/research_'+stem+'.md';ss='experiments/'+('certify_' if stem=='mixed_transition_whole_period_source' else 'check_')+stem+'.py';rr='repro/results/research-'+stem.replace('_','-')+'.json'
 for path in (pp,ss,rr):dependencies[path]=sha(ROOT/path)
 rec=json.loads((ROOT/rr).read_text());assert rec['status']=='passed'
 assert rec['proof_sha256']==dependencies[pp]and rec['script_sha256']==dependencies[ss]
 for field in ('dependencies','dependencies_sha256'):
  assert all(sha(ROOT/path)==dig for path,dig in rec.get(field,{}).items())
pp='notes/research_mixed_unselected_right_taper_products.md';ss='experiments/certify_mixed_right_square_conditional_packets.py';rr='repro/results/research-mixed-right-square-conditional-packets.json'
for path in (pp,ss,rr):dependencies[path]=sha(ROOT/path)
rec=json.loads((ROOT/rr).read_text());assert rec['status']=='passed'
assert rec['proof_sha256']==dependencies[pp]and rec['script_sha256']==dependencies[ss]
for field in ('dependencies','dependencies_sha256'):
 assert all(sha(ROOT/path)==dig for path,dig in rec.get(field,{}).items())
exact=[]
def zero(name,expression):
 assert sp.simplify(sp.expand(expression))==0,name
 exact.append(name)
w,R,ur,ui=sp.symbols('w R ur ui',real=True);Z=ur+sp.I*ui
nn=(1+R*Z)*(1+R*sp.conjugate(Z))+4*R*ui*w+(1-R*Z)*(1-R*sp.conjugate(Z))*w*w
uu=R*(w+sp.I)/(w-sp.I)
zero('full high-half numerator modulus',(1+w*w)*(1-Z*uu)*(1-sp.conjugate(Z*uu))-nn)
zero('unshifted denominator modulus',(1+w*w)*(1-uu)*(1-sp.conjugate(uu))-((1+R)**2+(1-R)**2*w*w))
zr,zi,dr,di=sp.symbols('zr zi dr di',real=True)
mod=(1+zr)**2+zi**2+4*zi*w+((1-zr)**2+zi**2)*w*w
mod_der=2*((1+zr)*dr+zi*di)+4*di*w+2*((zr-1)*dr+zi*di)*w*w
zero('exact numerator coefficient directional derivative',sp.diff(mod,zr)*dr+sp.diff(mod,zi)*di-mod_der)
t=sp.symbols('t')
for n in (4,6):
 cc=sp.symbols('c:'+str(n+1));ff=sum(cc[k]*w**k for k in range(n+1));gg=w*sp.diff(ff,w)-2*ff
 zero('coefficient derivative degree'+str(n),gg-sum((k-2)*cc[k]*w**k for k in range(n+1)))
 zero('monotone quotient degree'+str(n),w**3*sp.diff(ff/w**2,w)-gg)
 zero('Bernstein compactification degree'+str(n),(1-t)**n*gg.subs(w,t/(1-t))-sum((k-2)*cc[k]*t**k*(1-t)**(n-k)for k in range(n+1)))
x,y,aa,bb,ha,hb,eps=sp.symbols('x y aa bb ha hb eps',real=True)
upper=sp.pi*((y+ha)*(2*(x+aa)-1)+(y+hb)*(2*(x+bb)-1)-(2+eps)*y*(2*x-1))-2*sp.pi*(aa*y+ha*x)-2*sp.pi*y
collected=sp.pi*y*(eps*(1-2*x)+2*bb-2)+sp.pi*(ha*(2*aa-1)+hb*(2*x+2*bb-1))
zero('actual upper horizontal alias rate',upper-collected)
zero('original source normalization',1-eps/2-sp.Rational(1,2)-(1-eps)/2)
input_hash=sha(args.input)if args.input else None
saved=json.loads(args.input.read_text())if args.input else None
if saved:
 assert saved['status']=='passed'and saved['products']==161
 assert saved['script_sha256']==script_hash and saved['proof_sha256']==proof_hash
 assert saved['dependencies_sha256']==dependencies
 saved_cases={(c['mode'],tuple(c['types']),c['side'],tuple(c['parts'])):c for c in saved['cases']}
 assert len(saved_cases)==161

P=arb.pi();I=acb(0,1)
def ar(v):v=Fr(v);return arb(v.numerator)/v.denominator
def pt(v):return acb(ar(str(v.real)),ar(str(v.imag)))
def cot(z):return(P*z).cot()
def gp(z):return(1-(-2*P*I*z).exp()).log()
def g(z):return((-2*P*I*z).exp().polylog(2)-P*P/6)/(2*P*I)
def Q(s,a,b,d):return g(s+a)+g(s+b)-d*g(s)+2*P*I*a*s
def fp(s,a,b,d):return gp(s+a)+gp(s+b)-d*gp(s)+2*P*I*a
def hs(s,a,b,d):return P*(cot(s+a)+cot(s+b)-d*cot(s))+(d-2)*P*I
H={0:('-3/100','1/50'),1:('-57/1000','7/500')}
def corners(ty,low):
 lo,hi=map(ar,H[ty]);r=ar('11/50')
 if low:
  pts=[acb(ar('1/10')),acb(r,lo),acb(r,hi)]
  if ty==1:pts.append(acb(ar('3/25'),hi))
  return pts
 return [acb(r,lo),acb(ar('9/20'),lo),acb(ar('9/20'),hi),acb(r,hi)]
def decode(ad):
 b=[Fr(0),Fr(1),Fr(0),Fr(1)]
 for j,c in enumerate(ad):k=2*(j%2);m=(b[k]+b[k+1])/2;b[k+1-int(c)]=m
 return b

def mul(a,b):
 out=[arb(0)]*(len(a)+len(b)-1)
 for i,u in enumerate(a):
  for j,v in enumerate(b):out[i+j]+=u*v
 return out
def ppower(a,n):
 b=[arb(1)]
 for _ in range(n):b=mul(a,b)
 return b

def bernstein_positive(b,depth=0):
 if all(v>0 for v in b):return depth
 if depth>=12:return None
 levels=[b]
 while len(levels[-1])>1:levels.append([(u+v)/2 for u,v in zip(levels[-1],levels[-1][1:])])
 a=[v[0]for v in levels];c=[v[-1]for v in reversed(levels)]
 x=bernstein_positive(a,depth+1)
 if x is None:return None
 y=bernstein_positive(c,depth+1)
 return None if y is None else max(x,y)
def gpoly(a,b,y,e,da=None,db=None,dy=None):
 R=(2*P*y).exp();A=(-2*P*I*a).exp();B=(-2*P*I*b).exp();d=2+e
 norm2=lambda z:z.real**2+z.imag**2
 def nn(v):v*=R;return[norm2(1+v),4*v.imag,norm2(1-v)]
 base=[arb(1),arb(0),arb(1)]if e else[arb(1)]
 na,nb=nn(A),nn(B);dd=[(1+R)**2,arb(0),(1-R)**2];nd=ppower(dd,d)
 left=mul(mul(na,nb),base);right=[norm2(A)*v for v in nd]
 ff=[v-w for v,w in zip(left,right)]
 if da is None:return [(j-2)*v for j,v in enumerate(ff)]
 rd=2*P*R*dy;ad=-2*P*I*A*da;bd=-2*P*I*B*db
 def dn(v,vd):
  z=v*R;zd=vd*R+v*rd
  return[2*((1+z.conjugate())*zd).real,4*zd.imag,2*((z.conjugate()-1)*zd).real]
 dna,dnb=dn(A,ad),dn(B,bd)
 dl=[v+w for v,w in zip(mul(dna,nb),mul(na,dnb))];dl=mul(dl,base)
 ddd=[2*(1+R)*rd,arb(0),-2*(1-R)*rd]
 dnd=mul(ppower(dd,d-1),ddd);an=norm2(A);dan=2*(A.conjugate()*ad).real
 df=[dl[j]-dan*nd[j]-an*d*dnd[j]for j in range(len(dl))]
 return [(j-2)*v for j,v in enumerate(df)]
def ppart(v):
 lo=v.lower();hi=v.upper();return (lo if lo>0 else arb(0)).union(hi if hi>0 else arb(0))
def indicator(v):return arb(1)if v>0 else arb(0)if v<0 else arb(0).union(1)
def endpoint(s,a,b,d):
 y=s.imag;iy=acb(0,y)
 v=(g(a+iy)+g(b+iy)).real+d*P*ppart(y)-2*P*a.real*y
 return v,v+2*P*(ppart(y+a.imag)+ppart(y+b.imag)-d*ppart(y)-a.imag)

def check(ad,eta,e,side,parts,witness=None):
 bb=decode(ad);pp=[];p0=[];vel=[];dt=[]
 for j,ty in enumerate((eta,e)):
  cc=corners(ty,MODE=='TT' or j==side);v=cc[(parts[j]+1)%len(cc)]-cc[parts[j]];l,h=bb[2*j:2*j+2]
  pp.append(cc[parts[j]]+v*ar(l).union(ar(h)));p0.append(cc[parts[j]]+v*ar((l+h)/2));vel.append(v);dt.append(ar((h-l)/2))
 a,b=pp;a0,b0=p0;d=2+e
 af,bf=[complex(float(v.real),float(v.imag))for v in p0];pc,qc=1/np.tan(np.pi*af),1/np.tan(np.pi*bf)
 if witness is None:
  co=[1,pc+qc,-1+1j*(qc-pc)]if not e else[1,pc+qc+1j,pc*qc+1j*(pc+qc),1j*pc*qc-2j*(pc-1j)*(qc+1j)]
  rr=[v for v in np.roots(co)if v.real>0 and abs(v.imag)<1]
  if len(rr)!=1:return None,'rootproposal'
  zz=np.log((rr[0]+1j)/(rr[0]-1j))/(2j*np.pi);center=[str(zz.real),str(zz.imag)]
 else:center=witness['center']
 z0=acb(ar(center[0]),ar(center[1]));HH=hs(z0,a0,b0,d);Y=1/HH;f0=fp(z0,a0,b0,d)
 E0=[P*cot(z0+a0)+P*I,P*cot(z0+b0)-P*I]
 if witness is None:der=[pt(complex(float((-Y*v).real.mid()),float((-Y*v).imag.mid())))for v in E0]
 else:der=[acb(ar(v[0]),ar(v[1]))for v in witness['deriv']]
 dp=[pp[j]-p0[j]for j in(0,1)];dz=sum((der[j]*dp[j]for j in(0,1)),acb(0))
 lin=f0+sum(((HH*der[j]+E0[j])*dp[j]for j in(0,1)),acb(0))
 def rem(base,delta):
  v=base+acb(arb(0,abs(delta.real).upper()),arb(0,abs(delta.imag).upper()))
  if not(0<v.real<1):return arb.pos_inf()
  return P*P*abs(1/(P*v).sin()**2)*abs(delta)**2/2
 er=abs(Y)*(abs(lin)+rem(z0+a0,dz+dp[0])+rem(z0+b0,dz+dp[1])+d*rem(z0,dz))
 if not er.is_finite():return None,'wide root'
 rad=Fr(witness['radius'])if witness is not None else Fr(max(1,math.ceil(float(er.upper())*1.5*2**40)),2**40)
 if rad>Fr(1,25):return None,'large root'
 delta=dz+acb(arb(0,ar(rad)),arb(0,ar(rad)));z=z0+delta
 if not(0<z.real<ar('1/2')and 0<(z+a).real<1 and 0<(z+b).real<1):return None,'strip'
 def dc(base,delta):return -P*(P*delta).sin()/((P*base).sin()*(P*(base+delta)).sin())
 ee=1-Y*HH-Y*(dc(z0+a0,delta+dp[0])+dc(z0+b0,delta+dp[1])-d*dc(z0,delta))
 if not er+abs(ee)*ar(rad)<ar(rad):return None,'selfmap'
 rr=ar('1e-11');zp=z0+acb(arb(0,rr),arb(0,rr));ep=1-Y*hs(zp,a0,b0,d)
 if not abs(Y*f0)+abs(ep)*rr<rr:return None,'point'
 # The critical lift is original, not merely polynomial.
 if not abs(fp(z,a,b,d).imag)<P:return None,'lift'
 sc=cot(z)
 if not(sc.real>0 and abs(sc.imag)<1 and abs(z.imag)<1):return None,'cot strip'
 hess=hs(z,a,b,d);sd=[-(P*cot(z+a)+P*I)/hess,-(P*cot(z+b)-P*I)/hess]
 GG=gpoly(a0,b0,zp.imag,e);deg=len(GG)-1;errors=[arb(0)]*len(GG)
 for j in(0,1):
  da=vel[j]if j==0 else acb(0);db=vel[j]if j==1 else acb(0);dy=(sd[j]*vel[j]).imag
  gradient=gpoly(a,b,z.imag,e,da,db,dy)
  errors=[old+abs(v)*dt[j]for old,v in zip(errors,gradient)]
 GG=[v+arb(0,err.upper())for v,err in zip(GG,errors)]
 depth=bernstein_positive([GG[j]/math.comb(deg,j)for j in range(deg+1)])
 if depth is None:return None,'G positivity'
 # Compare both true full-period endpoints to the selected action, preserving y-dependence.
 selected=Q(zp,a0,b0,d).real;ep0=endpoint(zp,a0,b0,d)
 qa=gp(z+a)+2*P*I*z;qb=gp(z+b);hess=hs(z,a,b,d);sd=[-(P*cot(z+a)+P*I)/hess,-(P*cot(z+b)-P*I)/hess]
 y=z.imag;iy=acb(0,y);lga=gp(a+iy);lgb=gp(b+iy);U_y=-(lga+lgb).imag+d*P*indicator(y)-2*P*a.real
 mags=[arb(0),arb(0)]
 for j in(0,1):
  da=vel[j]if j==0 else acb(0);db=vel[j]if j==1 else acb(0);dy=(sd[j]*vel[j]).imag
  dM=(qa*da+qb*db).real;dL=(lga*da+lgb*db+2*P*I*iy*da).real+U_y*dy
  dR=dL+2*P*((indicator(y+a.imag)+indicator(y+b.imag)-d*indicator(y))*dy+(indicator(y+a.imag)-1)*da.imag+indicator(y+b.imag)*db.imag)
  mags[0]+=abs(dM-dL)*dt[j];mags[1]+=abs(dM-dR)*dt[j]
 gaps=[selected-ep0[j]-mags[j]for j in(0,1)]
 if not all(v>ar('1/10000')for v in gaps):return None,('endpoint gaps',[str(v)for v in gaps])
 mlow=selected-sum((abs((v*vel[j]).real)*dt[j]for j,v in enumerate((qa,qb))),arb(0))
 if not mlow>0:return None,'action positive'
 revived=[]
 for u,v in itertools.product((0,1),repeat=2):
  val=selected-(g(a0)+g(b0)).real-2*P*((u-1)*a0.imag+v*b0.imag)
  for j in(0,1):
   da=vel[j]if j==0 else acb(0);db=vel[j]if j==1 else acb(0)
   deriv=((qa-gp(a))*da+(qb-gp(b))*db).real-2*P*((u-1)*da.imag+v*db.imag)
   val-=abs(deriv)*dt[j]
  revived.append(val)
 if not all(v>ar('1/10000')for v in revived):return None,'real right endpoint'
 vertical=None
 if e:
  def vd(y):
   f=lambda zz:np.log(1-np.exp(-2j*np.pi*zz))
   return np.pi-(f(af+1j*y)+f(bf+1j*y)).imag-2*np.pi*af.real
  yp=float(witness['positive_vertical']['height'])if witness is not None else 0.0 if vd(0)<=0 else brentq(vd,0,2)
  yy=ar(str(yp));ii=acb(0,yy)
  vv=(g(a0+ii)+g(b0+ii)).real+P*yy-2*P*a0.real*yy
  vm=selected-vv
  for j in(0,1):
   da=vel[j]if j==0 else acb(0);db=vel[j]if j==1 else acb(0)
   deriv=(qa*da+qb*db-gp(a+ii)*da-gp(b+ii)*db).real+2*P*yy*da.real
   vm-=abs(deriv)*dt[j]
  slope=P-(gp(a+ii)+gp(b+ii)).imag-2*P*a.real
  tangent=max((-yy*slope).upper(),((2-yy)*slope).upper())
  vm-=tangent+2*P*ppart(b.imag)
  if not vm>ar('1/10000'):return None,'positive vertical'
  vertical={'height':str(yp),'gap':str(vm)}
 return{'center':center,'deriv':[[str(float(v.real)),str(float(v.imag))]for v in der],'radius':str(rad),'gaps':[str(v)for v in gaps],'G_bernstein_depth':depth,'root':str(z),'action_lower':str(mlow),'revived':[str(v)for v in revived],'positive_vertical':vertical},None

scalar_checks=[]
def positive(name,v):
 assert v>0,(name,v)
 scalar_checks.append({'name':name,'margin':str(v)})
radial=(-2*P*(2-ar('57/1000'))).exp();disk=5*radial/(2*P*(1-radial))
positive('upper horizontal alias gap three tenths',-ar('3/10')-(disk-P/5+ar('57/625')*P))
positive('lower horizontal alias gap three tenths',-ar('3/10')-(disk-ar('1043/500')*P))
positive('enlarged positive cap stays in cotangent half-strip',ar('1/2')-(2*P*ar('7/500')).sinh()/(2*(P*ar('1/10')).sin()**2))
start=time.time();visited=0;accepted=0;out=[]
for MODE,eta,e in itertools.product(('TT','TB','BT'),(0,1),(0,1)):
 side=1 if MODE=='BT' else 0
 for parts in itertools.product(range(len(corners(eta,MODE[0]=='T'))),range(len(corners(e,MODE[1]=='T')))):
  previous=saved_cases[(MODE,(eta,e),side,parts)]if saved else None
  saved_witness={v['address']:v for v in previous['witnesses']}if previous else {}
  todo=list(saved_witness)if previous else[''.join(z)for z in itertools.product('01',repeat=6)]
  output_witness=[];fails={}
  while todo:
   ad=todo.pop();ret,why=check(ad,eta,e,side,parts,saved_witness.get(ad));visited+=1
   if ret:output_witness.append({'address':ad,**ret});accepted+=1
   else:
    if previous:raise RuntimeError(('saved witness failed',eta,e,side,parts,ad,why))
    key=str(why[0])if isinstance(why,tuple)else why;fails[key]=fails.get(key,0)+1
    if len(ad)>=28:raise RuntimeError((eta,e,side,parts,ad,why))
    todo.extend((ad+'0',ad+'1'))
   if visited>args.max_visits:raise RuntimeError(('budget',visited,eta,e,side,parts,fails))
   if visited%2000==0:print('progress',visited,accepted,eta,e,side,parts,round(time.time()-start,1),fails,flush=True)
  codes={v['address']for v in output_witness}
  assert len(codes)==len(output_witness)
  assert sum((Fr(1,2**len(v))for v in codes),Fr(0))==1
  prefixes={v[:j]for v in codes for j in range(len(v))};assert not(codes&prefixes)
  if previous:assert codes==set(saved_witness)
  row={'mode':MODE,'types':[eta,e],'side':side,'parts':parts,'witnesses':output_witness,'failures':fails};out.append(row)
  print('case',len(out),eta,e,side,parts,len(output_witness),'visited',visited,'time',round(time.time()-start,1),flush=True)
assert len(out)==161
assert sha(PROOF)==proof_hash and sha(__file__)==script_hash
assert all(sha(ROOT/p)==dig for p,dig in dependencies.items())
if args.input:assert sha(args.input)==input_hash
record={'status':'passed','precision_bits':args.precision,'exact_identity_count':len(exact),'exact_identities':exact,'scalar_checks':scalar_checks,'products':len(out),'accepted':accepted,'visited':visited,'elapsed':time.time()-start,'cases':out,'proof_sha256':proof_hash,'script_sha256':script_hash,'dependencies_sha256':dependencies,'input_sha256':input_hash,'scope':'Complete canonical conditional packet on the enlarged transition cap products TT, TB, BT; type-four positive height rises linearly from zero at .10 to .014 at .12 and remains .014 above .12. All original currents and aliases retained. No selected outer-phase estimate.'}
args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(record,indent=2)+'\n')
print('PASS',len(exact),'exact identities,',len(scalar_checks),'scalar bounds,',len(out),'products,',accepted,'accepted cells,',visited,'visits')
