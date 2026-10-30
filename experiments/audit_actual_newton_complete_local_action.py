"""Marked local-action identities; not a finite contour/amplitude test."""
import argparse,json
from pathlib import Path
import sympy as sp
import mpmath as mp
from audit_actual_smoothed_source_capacity_blocks import F
mp.mp.dps=70

def symbolic():
 x,y,k,C,S,z=sp.symbols('x y k C S z',real=True)
 H=1-z;A=x+y
 R0=x*H*(y-x)+2*sp.I*x*S*k
 R1=H*A+2*x*(z-C*C)+2*sp.I*x*S*C
 bc=(k*k-x*y*H)/z;bs=(A*H-2*k*C)/z
 prod=R0**2+bs*R0*R1+bc*R1**2
 norm=(x*x+x*bs+bc)*(A*A*H+4*x*y*(z-C*C))*H
 expr=sp.cancel(z*(prod*(k-x*C-sp.I*x*S)-norm*(k-x*C+sp.I*x*S)))
 num=sp.fraction(expr)[0]
 rem=sp.rem(sp.Poly(sp.expand(num),S),sp.Poly(S*S-(1-C*C),S)).as_expr()
 assert sp.factor(rem)==0
 b,c,kap=sp.symbols('b c kap',real=True)
 L=A+b+c;D=x*y-b*c
 P=(L*L+kap*D)*z*z-(2*L*A+kap*x*y)*z+A*A
 assert sp.expand((A-L*z)**2-kap*z*(x*y-D*z)-P)==0
 return 2

def J0(t):
 return -mp.im(mp.polylog(2,mp.exp(2j*mp.pi*t)))/(2*mp.pi)
def J(t):
 if t<0:return -J0(-t)+1j*mp.pi*t
 if t>1:return J0(t-1)+1j*mp.pi*(t-1)
 return J0(t)
def jp(t):
 return mp.log(abs(2*mp.sin(mp.pi*t)))+(1j*mp.pi if t<0 or t>1 else 0)
def kernel(rho,mu,xi,eta):
 return J(mu)+J(mu+rho-xi-eta)-J(mu-rho)-J(mu-xi-eta)-J(xi)-J(rho-xi)-J(eta)-J(rho-eta)
def coeff(alpha,rho):
 return 2*J(rho)+J(alpha+rho)-J(2*rho)-J(alpha-rho)

def run(output):
 worst=mp.mpf(0);count=0;derivatives=0;faces=0;ratios=0
 def check(v,scale=1):
  nonlocal worst
  err=abs(v)/max(1,abs(scale));worst=max(worst,err)
  assert err<mp.mpf('1e-60'),(v,scale)
 for vals in ((1,1,1,1),(2,3,5,7),(4,9,1,1),('.2','3','7','.5'),(20,1,2,3),(1,40,3,5)):
  x,b,c,y=map(mp.mpf,vals);A=x+y;L=A+b+c;D=x*y-b*c
  for alpha in map(mp.mpf,('0','.01','.05','.12')):
   kap=4*mp.cos(mp.pi*alpha)**2
   aa=L*L+kap*D;bb=2*L*A+kap*x*y
   z=2*A*A/(bb+mp.sqrt(bb*bb-4*aa*A*A))
   theta=mp.acos(mp.cos(mp.pi*alpha)*mp.sqrt(z));rho=1-theta/mp.pi
   k=(A-L*z)/(2*mp.cos(theta));beta=mp.asinh(mp.sin(mp.pi*alpha)*mp.sqrt(z/(1-z)))/mp.pi
   xi=mp.arg(k-x*mp.exp(-1j*theta))/mp.pi
   eta=mp.arg(k-y*mp.exp(-1j*theta))/mp.pi
   pb=mp.arg(k+b*mp.exp(1j*theta))/mp.pi
   pc=mp.arg(k+c*mp.exp(1j*theta))/mp.pi;mu=1-pc
   assert 0<xi<rho and 0<eta<rho and rho<mu<1 and xi+eta<mu and mu+rho-xi-eta<1
   check(mu-xi-eta-pb);check(k*k-(x*y*(1-z)+b*c*z))
   # Independent raw critical derivatives on the explicitly chosen sine sheet.
   a=mu+rho-xi-eta;v=mu-xi-eta
   check(jp(mu)+jp(a)-jp(mu-rho)-jp(v)+mp.log(b/c))
   check(-jp(a)+jp(v)-jp(xi)+jp(rho-xi)+mp.log(x/b))
   check(-jp(a)+jp(v)-jp(eta)+jp(rho-eta)+mp.log(y/b))
   check(jp(a)+jp(mu-rho)-jp(rho-xi)-jp(rho-eta)+2*jp(rho)+jp(alpha+rho)-2*jp(2*rho)+jp(alpha-rho)+1j*mp.pi)
   check(jp(alpha+rho)-jp(alpha-rho)+1j*mp.pi+2*mp.pi*beta)
   derivatives+=5
   def data(mid,t):
    sh=mp.sinh(mp.pi*t);ch=mp.cosh(mp.pi*t)
    T=mp.sqrt(mid*A+x*y-mid*mid*sh*sh);dg=A*A+4*x*y*sh*sh
    E=A-2*mid*sh*sh+2j*sh*T
    angmid=2*mp.atan(mid*ch/T)
    def outer(u,vv):
     co=(u*(vv-u)+mid*(vv+u*(1+2*sh*sh)))/((u+mid)*mp.sqrt(dg))
     si=2*u*ch*T/((u+mid)*mp.sqrt(dg))
     return mp.atan2(si,co)
    return E,angmid,outer(x,y),outer(y,x),dg,T
   eb,mb,xb,yb,dg,tb=data(b,beta);ec,mc,xc,yc,_,tc=data(c,beta)
   check(eb*ec/dg-mp.exp(2j*mp.pi*alpha));ratios+=1
   check(mb/(2*mp.pi)-pb);check(mc/(2*mp.pi)-pc)
   check((xb+xc)/(2*mp.pi)-xi);check((yb+yc)/(2*mp.pi)-eta);faces+=4
   check(tb-(k+b*mp.cos(theta))/mp.sqrt(1-z));check(tc-(k+c*mp.cos(theta))/mp.sqrt(1-z))
   psi=kernel(rho,mu,xi,eta)+coeff(alpha,rho)+1j*mp.pi*(alpha+rho)+mp.log(c)+mu*mp.log(b/c)+xi*mp.log(x/b)+eta*mp.log(y/b)
   angle_integral=mp.quad(lambda t:mp.arg(data(b,t)[0])+mp.arg(data(c,t)[0]),[0,beta]) if beta else 0
   core=F(x,b,y)+F(x,c,y)+angle_integral-2*mp.pi*alpha*beta
   check(psi-core-1j*mp.pi,core);count+=1
 out=dict(status='PASS',symbolic_identities=symbolic(),critical_actions=count,raw_stationarity_and_external_derivatives=derivatives,marked_face_derivatives=faces,unsquared_collar_checks=ratios,max_error=mp.nstr(worst,20),scope='Specified local classical sine-sheet action equality only; no finite amplitude or cycle contribution.')
 output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

if __name__=='__main__':
 parser=argparse.ArgumentParser()
 parser.add_argument('--output',type=Path,default=Path(__file__).with_name('actual_newton_complete_local_action_results.json'))
 run(parser.parse_args().output)
