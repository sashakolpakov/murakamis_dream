#!/usr/bin/env python3
"""Exact Laplacian and barrier bookkeeping; no numerical source comparison."""
from pathlib import Path
import argparse,hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_height_coupled_reference_extension.md'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-height-coupled-reference-extension.json')
 args=ap.parse_args();ph,sh=sha(PROOF),sha(__file__);checks=0
 p,pb,t=s.symbols('p pb tau',real=True)
 # p and pb are independent Wirtinger variables. Their assigned real
 # flag is irrelevant: conjugation is implemented by the explicit swap.
 n=3;x=s.symbols('x0:3',real=True);d=s.symbols('d0:3',real=True)
 z=s.Matrix([p+s.I*p**2,p**2+(2-s.I)*p,p**3-s.I*p])
 zb=z.xreplace({p:pb,s.I:-s.I})
 q=z.diff(p);qb=zb.diff(pb)
 w=s.Matrix([x[j]+t*(z[j]-zb[j])/2 for j in range(n)])
 v=s.symbols('v0:3');V=s.Matrix(v)
 # This exact cubic check tests chain terms from nonlinear references
 # and a nonconstant symmetric Hessian. The general identity is proved
 # by the Wirtinger calculation in the note, not by polynomial sampling.
 f=(1+s.I)*v[0]**3+(2-s.I)*v[1]**2*v[2]+v[0]*v[1]*v[2]+s.I*v[2]**2
 grad=s.Matrix([s.diff(f,a)for a in v]);H=s.hessian(f,v)
 sub=lambda a:dict(zip(v,a))
 Fz=f.subs(sub(z),simultaneous=True);Fw=f.subs(sub(w),simultaneous=True)
 E=Fw-Fz-(grad.subs(sub(z),simultaneous=True).T*(w-z))[0]
 conjugate=lambda a:s.conjugate(a).xreplace({p:pb,pb:p})
 # x,d,t,p,pb are real symbols solely to make the explicit formal
 # conjugation above act only on coefficients, followed by p<->pb.
 D=(E+conjugate(E))/2+(1-t)**2*sum(d[j]*(-(z[j]-zb[j])**2/4)for j in range(n))
 lap=4*s.diff(D,p,pb)
 T= -t*t*(q.T*H.subs(sub(w),simultaneous=True)*qb)[0]+2*t*(q.T*H.subs(sub(z),simultaneous=True)*qb)[0]
 rhs=(T+conjugate(T))/2+2*(1-t)**2*sum(d[j]*q[j]*qb[j]for j in range(n))
 assert s.expand(lap-rhs)==0;checks+=1
 u=s.symbols('u0:3',real=True);vv=s.symbols('r0:3',real=True)
 aa=s.symbols('a0:6',real=True);bb=s.symbols('b0:6',real=True)
 A=s.Matrix([[aa[0],aa[1],aa[2]],[aa[1],aa[3],aa[4]],[aa[2],aa[4],aa[5]]])
 B=s.Matrix([[bb[0],bb[1],bb[2]],[bb[1],bb[3],bb[4]],[bb[2],bb[4],bb[5]]])
 Q=s.Matrix(u)+s.I*s.Matrix(vv)
 identity=s.re((Q.T*(-A+s.I*B)*s.conjugate(Q))[0])+(s.Matrix(u).T*A*s.Matrix(u))[0]+(s.Matrix(vv).T*A*s.Matrix(vv))[0]
 assert s.expand(identity)==0;checks+=1
 y,lo,hi,C=s.symbols('y lo hi C',real=True)
 barrier=t*C*(y-lo)*(hi-y)
 assert s.diff(barrier,y,2)==-2*t*C;checks+=1
 assert s.expand(barrier.subs(y,(lo+hi)/2)-t*C*(hi-lo)**2/4)==0;checks+=1
 assert barrier.subs(y,lo)==barrier.subs(y,hi)==0;checks+=1
 assert s.Rational(151,20)==s.Rational('7.55')and s.Rational(11,2)==s.Rational('5.5');checks+=1
 assert ph==sha(PROOF)and sh==sha(__file__)
 out=dict(status='passed',exact_checks=checks,proof_sha256=ph,script_sha256=sh,
          scope='Exact height-coupled-reference Laplacian and barrier formulas only; no numerical support gap, target curvature, or source assertion.')
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n')
 print('PASS',checks,'exact identities',flush=True)
if __name__=='__main__':main()
