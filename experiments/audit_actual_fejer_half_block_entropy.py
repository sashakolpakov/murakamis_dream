"""Actual half-block coefficients and normalization; limit samples are diagnostic.

The original-numerator/path/anchor block consolidates the independently
reviewed weighted-rate audit. It is supplemented by Jacobi identities,
closed-entropy reconstruction and actual finite coefficient profiles.
"""
import sys,json,argparse
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import mpmath as mp
import sympy as sp
from audit_actual_small_circle_polynomial_face_insertion import Local
from audit_actual_gaussian_resolvent_numerator_and_cap import finite_H
from audit_actual_smoothing_fixed_radius_gap import F

def add(out,key,value,p):out[key]=(out.get(key,0)+value)%p

def exact_coefficients():
 count=right=0
 for N in range(4,17,2):
  loc=Local(N);p=loc.p;M=N//2-1;d=N-1;q,Q=loc.q,loc.Q
  cs=[(q*pow(Q,j,p)+pow(q,-1,p)*pow(Q,-j,p))%p for j in range(N)]
  aa=[(2+c)%p for c in cs]
  ss2=[(2-pow(Q,j,p)-pow(Q,-j,p))%p for j in range(N)]
  ee=[(q+pow(q,-1,p)-q*pow(Q,-j,p)-pow(q,-1,p)*pow(Q,j,p))%p for j in range(N)]
  r2={};r1={};H={}
  for j in range(M+1):
   out={(0,j,0):pow(aa[j],-1,p)}
   al=ss2[j]*pow(aa[j],-1,p)%p;be=ee[j]*pow(aa[j],-1,p)%p
   for (a,b,y),v in r1.items():
    add(out,(a+1,b,y),al*v,p);add(out,(a,b,y+1),al*v,p)
   for (a,b,y),v in r2.items():add(out,(a+1,b,y+1),be*v,p)
   out={k:v for k,v in out.items() if v}
   for (a,b,y),v in out.items():add(H,(a,b,d-j,y),4*v,p)
   r2,r1=r1,out
  H={k:v for k,v in H.items() if v}
  actual={ex:(-v)%p for ex,v in finite_H(loc,-2).items() if ex[2]>=N//2}
  assert H==actual,(N,'left')
  count+=len(H)
  reverse={(a,c,b,y):v for (a,b,c,y),v in H.items()}
  actual={ex:(-v)%p for ex,v in finite_H(loc,-2).items() if ex[1]>=N//2}
  assert reverse==actual,(N,'right');right+=len(reverse)
 return count,right

def weights(N,x,b,c,y):
 M=N//2-1;th=mp.pi/N;A=x+y;P=x*y
 r2=r1=mp.mpf(0);val=mp.mpf(0)
 for j in range(M+1):
  aa=4*mp.cos((j+mp.mpf('.5'))*th)**2
  sj=2*mp.sin(j*th);sm=2*mp.sin((j-1)*th)
  rr=b**j/aa+sj*sj*A/aa*r1+sj*sm*P/aa*r2
  val+=4*c**(N-1-j)*rr;r2,r1=r1,rr
 return val

def coefficients(N,i,j):
 """Original Q recurrence, with all physical endpoint denominators."""
 qprev=[mp.mpf(1)];qprevprev=[]
 for v in range(i+1,j+1):
  aa=4*mp.cos(mp.pi*(mp.mpf(v)+mp.mpf('.5'))/N)**2
  sj=2*mp.sin(mp.pi*v/N);sm=2*mp.sin(mp.pi*(v-1)/N)
  al=sj*sj/aa;be=sj*sm/aa
  out=[mp.mpf(0)]*(len(qprev)+1)
  for k,value in enumerate(qprev):
   out[k]+=al*value;out[k+1]+=al*value
  for k,value in enumerate(qprevprev):out[k+1]+=be*value
  qprevprev,qprev=qprev,out
 return qprev

def triangle(alpha):
 lam=lambda v:mp.mpf(0) if abs(mp.sin(v))<mp.mpf('1e-65') else mp.im(mp.polylog(2,mp.exp(2j*v)))/2
 return sum(lam(mp.pi*a)+lam(mp.pi/2-mp.pi*a) for a in alpha)/mp.pi

def entropy(mu,nu,xi):
 if mu==nu:return mp.mpf(0)
 width=nu-mu;ang=2*mp.pi*(xi-width/2)
 a=mp.cos(mp.pi*mu);b=mp.cos(mp.pi*nu)
 if xi==0:k=-mp.mpf(1)
 elif xi==width:k=mp.mpf(1)
 else:k=mp.sin(ang)/mp.sqrt(a*a+b*b-2*a*b*mp.cos(ang))
 def loads(t):
  arg=max(-mp.mpf(1),min(mp.mpf(1),k*mp.cos(mp.pi*t)))
  ax=mp.mpf('.25')-t/2+mp.asin(arg)/(2*mp.pi)
  return ax,t,mp.mpf('.5')-t-ax
 return triangle(loads(mu))-triangle(loads(nu))

def coefficient_checks():
 symbolic=0
 x,z,T=sp.symbols('x z T')
 p0,p1=sp.Integer(1),x+1
 q0,q1=sp.Integer(1),T
 for r in range(2,11):
  gamma=sp.Rational(r+1,r+3)
  pp=sp.expand((x+1)*p1+gamma*x*p0)
  qq=sp.expand(T*q1-gamma*q0)
  assert sp.cancel(pp.subs(x,-z*z)-z**r*qq.subs(T,1/z-z))==0
  symbolic+=1;p0,p1=p1,pp;q0,q1=q1,qq
 # Independently differentiate the actual logarithmic root at zero tilt.
 tau,l=sp.symbols('tau l',positive=True,real=True)
 g=l/2+sp.log(tau)+sp.asinh(tau*sp.cosh(l/2))
 assert sp.simplify(sp.diff(g,l).subs(l,0)-sp.Rational(1,2))==0
 assert sp.simplify(sp.diff(g,l,2).subs(l,0)-tau/(4*sp.sqrt(1+tau*tau)))==0
 symbolic+=2
 # Finite Jacobi spectra, using actual level-N coefficients.
 roots=0;root_error=mp.mpf(0)
 for N,i,j in ((24,3,9),(32,4,12),(40,5,15),(48,6,18),(64,8,24)):
  rr=j-i;J=mp.matrix(rr)
  for v in range(1,rr):
   s1=2*mp.sin(mp.pi*(i+v+1)/N);s0=2*mp.sin(mp.pi*(i+v)/N)
   aa=4*mp.cos(mp.pi*(i+v+mp.mpf('.5'))/N)**2
   J[v-1,v]=J[v,v-1]=mp.sqrt(aa/(s1*s0))
  vals=mp.eigsy(J,eigvals_only=True)
  co=coefficients(N,i,j)
  for val in vals:
   zz=2/(mp.sqrt(val*val+4)+val)
   xx=-zz*zz;assert xx<0
   num=sum(v*xx**k for k,v in enumerate(co));den=sum(abs(v*xx**k) for k,v in enumerate(co))
   err=abs(num)/den;root_error=max(root_error,err);roots+=1
   assert err<mp.mpf('1e-60')
 # Compare finite closed E with an independent one-dimensional integral
 # at selected tilts, including one-sided row endpoints.
 recon=0;recon_error=mp.mpf(0)
 for mu,nu in ((mp.mpf(0),mp.mpf('.5')),(mp.mpf(0),mp.mpf('.3')),(mp.mpf('.1'),mp.mpf('.5')),(mp.mpf('.125'),mp.mpf('.25'))):
  for ell in map(mp.mpf,('-2','0','1.4')):
   kap=mp.tanh(ell/2)
   ax=lambda t:mp.mpf('.25')-t/2+mp.asin(kap*mp.cos(mp.pi*t))/(2*mp.pi)
   xi=ax(mu)-ax(nu)
   gg=lambda t:ell/2+mp.log(mp.tan(mp.pi*t))+mp.asinh(mp.tan(mp.pi*t)*mp.cosh(ell/2))
   value=mp.quad(gg,[mu,(mu+nu)/2,nu])-xi*ell
   err=abs(value-entropy(mu,nu,xi));recon_error=max(recon_error,err);recon+=1
   assert err<mp.mpf('1e-60')
 profiles=[];extremes=0
 for N in (32,64,128,256):
  M=N//2-1
  intervals=((0,0),(M,M),(0,1),(M-1,M),(0,M),(N//8,N//4),(0,N//4),(N//4,M))
  for i,j in intervals:
   co=coefficients(N,i,j);rr=j-i
   assert all(v>0 for v in co)
   prod=mp.fprod(mp.sin(mp.pi*v/N)**2/mp.cos(mp.pi*(v+mp.mpf('.5'))/N)**2 for v in range(i+1,j+1))
   assert abs(co[0]/prod-1)<mp.mpf('1e-65')
   assert abs(co[-1]/prod-1)<mp.mpf('1e-65');extremes+=2
   for kk in sorted(set((0,rr//2,rr,max(0,rr-1)))):
    aa=4*mp.cos(mp.pi*(i+mp.mpf('.5'))/N)**2
    rate=mp.log(4*co[kk]/aa)/N
    target=entropy(mp.mpf(i)/N,mp.mpf(j)/N,mp.mpf(kk)/N)
    profiles.append(dict(N=N,i=i,j=j,k=kk,source_rate=str(rate),entropy=str(target),difference=str(rate-target)))
 curvature=mp.pi/(1-1/mp.sqrt(2))-mp.pi/(mp.cos(mp.pi/8)-1/mp.sqrt(2))
 assert curvature<0
 convexity=[]
 for N in (128,256,512,1024):
  i=N//8;k=N//16;j=N//4;step=N//64
  values=[]
  for jj in (j-step,j,j+step):values.append(mp.log(coefficients(N,i,jj)[k]))
  defect=values[1]-(values[0]+values[2])/2
  convexity.append(dict(N=N,step=step,log_convexity_defect=str(defect),normalized_defect=str(defect/N)))
  # This is a finite original-coefficient check, not the uniform proof.
  assert defect>0
 return dict(jacobi_and_log_root_symbolic_identities=symbolic,
             actual_negative_roots=roots,maximum_root_relative_error=str(root_error),
             closed_entropy_integral_reconstructions=recon,maximum_entropy_reconstruction_error=str(recon_error),
             exact_extreme_coefficients=extremes,closed_coefficient_rate_diagnostics=profiles,
             exact_negative_curvature_value=str(curvature),finite_log_convexity_failures=convexity)

def run():
 mp.mp.dps=75
 A,P,b,z=sp.symbols('A P b z',positive=True)
 assert sp.factor((b*b-A*z*b-P*z).subs(z,b*b/(A*b+P)))==0
 symbolic=1
 a,beta,Lp,Lm=sp.symbols('a beta Lp Lm')
 for l in range(2,12):
  ql=lambda n:sum(Lp**(n-j)*Lm**j for j in range(n+1))
  assert sp.expand(ql(l)-(Lp+Lm)*ql(l-1)+Lp*Lm*ql(l-2))==0
  symbolic+=1
 left,right=exact_coefficients()
 params=[tuple(map(mp.mpf,p)) for p in [('1','1','1','1'),('1','4096','1','1'),('1','1','4096','1'),('.4','2.3','1.7','3.2'),('5','.03','2','.7')]]
 anchors=[];rates=[];worst=mp.mpf(0)
 for x,b,c,y in params:
  A=x+y;P=x*y;mu=mp.atan(b/mp.sqrt(A*b+P))/mp.pi
  def LL(t):
   ss=mp.sin(mp.pi*t);cc=mp.cos(mp.pi*t)
   return (A*ss*ss+ss*mp.sqrt(A*A*ss*ss+4*P*cc*cc))/(2*cc*cc)
  H=mu*mp.log(b)+mp.quad(lambda t:mp.log(LL(t)),[mu,(mu+mp.mpf('.5'))/2,mp.mpf('.5')])
  exactF=F(x,b,y);err=abs(H-exactF);worst=max(worst,err)
  assert err<mp.mpf('1e-60'),(x,b,y,err)
  anchors.append(str(err));target=max(mp.log(c),exactF+mp.log(c)/2)
  for N in (32,64,128,256,512):
   rate=mp.log(weights(N,x,b,c,y))/N
   rates.append(dict(N=N,faces=list(map(str,(x,b,c,y))),rate=str(rate),target=str(target),difference=str(rate-target)))
 # Independent direct path sum for small real levels, rather than the R recurrence.
 path_checks=0
 for N in (4,6,8,10,12):
  x,b,c,y=map(mp.mpf,('.7','1.4','2.1','.9'));M=N//2-1;th=mp.pi/N
  aa=[4*mp.cos((j+mp.mpf('.5'))*th)**2 for j in range(N)]
  ss=[2*mp.sin(j*th) for j in range(N)]
  total=mp.mpf(0)
  def rec(i,j,weight,vis):
   nonlocal total,path_checks
   total+=weight*b**i*c**(N-1-j)*mp.fprod(aa[r] for r in range(N) if r not in vis)
   path_checks+=1
   if i:rec(i-1,j,weight*ss[i]**2*(x+y),vis+[i-1])
   if i>=2:rec(i-2,j,weight*ss[i]*ss[i-1]*x*y,vis+[i-2])
  for j in range(M+1):rec(j,j,mp.mpf(1),[j])
  assert abs(total/weights(N,x,b,c,y)-1)<mp.mpf('1e-65')
 out=dict(status='PASS',precision=mp.mp.dps,symbolic_identities=symbolic,
             original_positive_numerator_left_coefficients=left,
             original_positive_numerator_right_coefficients=right,
             direct_positive_paths=path_checks,absolute_triangle_anchors=len(anchors),
             maximum_anchor_error=str(worst),rate_diagnostics=rates,
             scope='Original half-block/source coefficient and path comparisons, exact Jacobi/log-root identities and independent F normalization. Closed-boundary rates and finite curvature profiles are diagnostics, not proofs of uniform limits, shared capacity, or a filling asymptotic.')
 out.update(coefficient_checks());return out

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',default=str(Path(__file__).with_name('actual_fejer_half_block_entropy_results.json')));args=ap.parse_args()
 out=run();Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ('rate_diagnostics','closed_coefficient_rate_diagnostics')},indent=2))
