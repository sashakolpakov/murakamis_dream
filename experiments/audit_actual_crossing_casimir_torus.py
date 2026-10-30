"""Source phase/conic identities and actual finite R powers; no growth claim."""
import argparse,json
from fractions import Fraction as Qr
from pathlib import Path
import sympy as s
import numpy as np
from audit_actual_homogeneous_casimir_face_source import homogeneous
from audit_actual_small_circle_polynomial_face_insertion import Local
from audit_actual_braided_two_cut_source_adapter import original_crossings

def symbolic():
 x,y,b,z,c,r,lam=s.symbols('x y b z c r lam',nonzero=True)
 A=x+y;P=x*y;f=lambda v:(v+x)*(v+y)
 sig=2+(b+z+A)**2/(P-b*z)
 checks=[]
 rb=(P-b*z)/f(b)
 checks.append(2+(rb-1)**2/rb*f(b)/b**2-sig)
 cn=-sig*z-b-2*A
 checks.append((P-b*z)*(P-z*cn)-f(z)**2)
 checks.append(2+(z+cn+A)**2/(P-z*cn)-sig)
 # Exact inverse in the SAME phase chart.
 cc=(P-r*f(b))/b;rr=f(cc)/(P-b*cc)
 bb=(P-f(cc)/rr)/cc;rback=(P-cc*bb)/f(bb)
 checks.extend((bb-b,rback-r))
 # Norm, Darboux Jacobian, and source reference point.
 sigma=-lam-1/lam;h=2*A/(sigma+2)
 u=b+h;v=z+h;eta=u-lam*v
 F=b*b+z*z+sigma*b*z+2*A*(b+z)+A*A-(sigma-2)*P
 C0=(sigma-2)*(P-A*A/(sigma+2))
 checks.append((u-lam*v)*(u-v/lam)-C0-F)
 w=(lam+1)/(lam-1)*(x+lam*y)
 wb=w.subs(lam,1/lam)
 checks.append(w*wb-C0)
 checks.append(eta.subs({b:-x,z:-y})-w)
 checks.append(lam*s.diff(F,b)+s.diff(F,z)-(lam-1/lam)*eta)
 un=z+h;vn=-sigma*z-b-2*A+h
 checks.append(un-lam*vn-lam*eta)
 # Nonreduced endpoint: retain e rather than setting it to zero.
 e=s.symbols('e');zz=-b-A+e
 c2=-2*zz-b-2*A;z2=-2*c2-zz-2*A
 checks.extend((c2-(b-2*e),z2-(zz+2*e)))
 for item in checks:assert s.cancel(item)==0,item
 M=lambda sig:s.Matrix([[0,1,0],[-1,-sig,-2*A],[0,0,1]])
 U=M(-2)-s.eye(3)
 assert U**3==s.zeros(3) and U**2!=s.zeros(3)
 assert (M(2)+s.eye(3))**2*(M(2)-s.eye(3))==s.zeros(3)
 return len(checks)+2

def exact_orbits():
 count=punctures=endpoints=signs=0
 for x,y in ((Qr(1),Qr(2)),(Qr(2),Qr(3)),(Qr(1),Qr(1))):
  A=x+y;P=x*y;f=lambda b:(b+x)*(b+y)
  for lam in (Qr(2),Qr(3),Qr(-2),Qr(-3,2)):
   sig=-lam-1/lam;h=2*A/(sig+2)
   C0=(sig-2)*(P-A*A/(sig+2))
   if not C0:continue
   w=(lam+1)/(lam-1)*(x+lam*y);wb=(1/lam+1)/(1/lam-1)*(x+y/lam)
   def point(a):
    u=(lam*wb/a-w*a/lam)/(lam-1/lam)
    v=(wb/a-w*a)/(lam-1/lam)
    return u-h,v-h
   assert point(Qr(1))==(-x,-y);punctures+=1
   other=(y+lam*x)/(x+lam*y)
   assert point(other)==(-y,-x);punctures+=1
   for aa in (Qr(2),Qr(5,3),Qr(-2)):
    for n in range(-7,8):
     b,z=point(aa*lam**n);c=-sig*z-b-2*A
     assert (z,c)==point(aa*lam**(n+1))
     assert b*b+z*z+sig*b*z+2*A*(b+z)+A*A-(sig-2)*P==0
     count+=1
     if b*z*f(b)*f(z)*(P-b*z)*(A+b+z):
      r=(P-b*z)/f(b);rr=f(z)/(P-b*z)
      assert (P-r*f(b))/b==z
      assert (P-f(z)/rr)/z==b
      assert (P-b*z)/f(b)==r;signs+=2
  for t0 in map(Qr,(1,2,5)):
   def parpoint(t):return (-(t-A)**2/(4*A)-P/A,-(t+A)**2/(4*A)-P/A)
   for n in range(-8,9):
    b,z=parpoint(t0+2*A*n);c=2*z-b-2*A
    assert (z,c)==parpoint(t0+2*A*(n+1));endpoints+=1
   for b in map(Qr,(0,1,3)):
    z=-b-A;c=-2*z-b-2*A
    assert c==b;endpoints+=1
 return dict(torus_integer_steps=count,inverse_phase_checks=signs,excluded_basepoints=punctures,parabolic_and_reduced_endpoint_steps=endpoints)

def compose(F,G,d,p):
 out={}
 for (a,i,t,b),v in F.items():
  for (aa,ii,tt,bb),w in G.items():
   if t+ii!=d:continue
   ex=(a+aa,i,tt,b+bb);out[ex]=(out.get(ex,0)+v*w)%p
 return {e:v for e,v in out.items() if v}

def original_source():
 counts=dict(powers=0,original_entries=0,wrong_unwrapped_zeros=0,mixed_inverse_compositions=0,unwrapped_gaussian_node_values=0,spectral_adjacent_ratios=0)
 for N in range(3,7):
  loc=Local(N);p,q,Q,d=loc.p,loc.q,loc.Q,loc.d
  _,_,_,Rs=original_crossings(N)
  hs={0:homogeneous(loc,1,0)};ops={0:np.eye(N*N,dtype=np.int64)}
  for eps in (-1,1):
   base={e:v*pow(loc.eta,eps*d*d,p)%p for e,v in homogeneous(loc,1,eps).items()}
   step=Rs[0 if eps>0 else 1][0]
   for k in range(1,6):
    n=eps*k;hs[n]=compose(base,hs[n-eps],d,p);ops[n]=step@ops[n-eps]%p
  for a,b in ((2,-2),(3,-2),(-5,3)):
   assert compose(hs[a],hs[b],d,p)==hs[a+b];counts['mixed_inverse_compositions']+=1
  for n in (-5,-3,-2,0,2,3,5):
   H=hs[n];op=ops[n]
   for u in range(N):
    for v in range(N):
     x=-q*pow(Q,u,p)%p;y=-pow(q,-1,p)*pow(Q,-v,p)%p
     for r in range(N):
      ss=(u+v-r)%N;delta=r-u;c=pow(Q,-delta,p)
      val=sum(co*pow(x,a,p)*pow(c,t,p)*pow(y,b,p) for (a,i,t,b),co in H.items())%p
      pred=val*pow(N,-1,p)*pow(q,-d*delta,p)*pow(c,-d,p)%p
      assert pred==int(op[r*N+ss,u*N+v]),(N,n,u,v,r)
      counts['original_entries']+=1
      if r+ss!=u+v:assert pred==0;counts['wrong_unwrapped_zeros']+=1
   counts['powers']+=1
   for a in range(d//2+1):
    full=pow(loc.omega[a],n,p)
    gaussian=pow(loc.eta,n*(2*a*a-2*a*d+d*d),p)
    assert full==gaussian;counts['unwrapped_gaussian_node_values']+=1
  # Adjacent unwrapped spectral values, including formal upper partners.
  for a in range(d):
   nu=lambda j:pow(-1,j,p)*pow(q,j*(j+1),p)%p
   assert nu(a+1)*pow(nu(a),-1,p)%p==-pow(q,2*a+2,p)%p
   counts['spectral_adjacent_ratios']+=1
 return counts

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=Path(__file__).with_name('actual_crossing_casimir_torus_results.json'));args=parser.parse_args()
 out=dict(status='PASS',symbolic_identities=symbolic(),exact_classical_transport=exact_orbits(),original_source=original_source(),scope='Original crossing composition and localized classical Casimir transport, including degenerations. No quantum norm or finite-cycle selection estimate.')
 args.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
