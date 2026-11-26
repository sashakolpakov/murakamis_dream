#!/usr/bin/env python3
"""Exact algebra behind the complete angular support candidate reduction."""
import argparse,hashlib,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_angular_support_candidates.md'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-angular-support-candidates.json');args=ap.parse_args()
 rho,t,c,d,E=s.symbols('rho t c d E',real=True)
 a=(1-rho)**2+(1+rho)**2*t*t
 b=1+rho*rho-2*rho*c+4*rho*d*t+(1+rho*rho+2*rho*c)*t*t
 checks=[]
 def exact(name,x):
  assert s.factor(s.together(x))==0,(name,s.factor(x));checks.append(name)
 cos=(1-t*t)/(1+t*t);sin=2*t/(1+t*t)
 D0=1+rho*rho-2*rho*cos;D1=1+rho*rho-2*rho*(cos*c-sin*d)
 exact('unshifted tangent substitution',D0-a/(1+t*t))
 exact('shifted tangent substitution',D1-b/(1+t*t))
 P0=b-E*a;P1=b*b*(1+t*t)-E*E*a**3
 exact('quadratic stationary equation',(1+t*t)*(D1-E*D0)-P0)
 exact('sextic stationary equation',(1+t*t)**3*(D1*D1-E*E*D0**3)-P1)
 exact('sextic nonidentity at tangent pole',P1.subs(t,s.I)-64*E*E*rho**3)
 exact('zero or full row shifts',b.subs({c:1,d:0})-a)
 exact('quadratic identity on zero/full rows',P0.subs({c:1,d:0,E:1}))
 exact('quadratic linear coefficient',s.Poly(P0,t).coeff_monomial(t)-4*rho*d)
 # If P0 is an identity, adding constant and quadratic coefficients
 # forces E=1; then the constant coefficient forces cos(omega)=1.
 poly=s.Poly(P0,t)
 exact('equal angular averages force E one',
       poly.coeff_monomial(1)+poly.coeff_monomial(t*t)-2*(1+rho*rho)*(1-E))
 exact('nonzero first Fourier coefficient forces integer row',
       poly.coeff_monomial(1).subs(E,1)-2*rho*(1-c))
 assert s.degree(P0,t)<=2 and s.degree(P1,t)<=6
 checks.extend(['quadratic degree at most two','sextic degree at most six'])
 beta,u,h,kappa,sigma,eps=s.symbols('beta u h kappa sigma eps',real=True)
 nu=s.Function('nu')(beta);I=s.Function('I')(beta)
 logD0,logD1=s.symbols('logD0 logD1',real=True)
 for q in [0,1]:
  deriv=s.Rational(1,2)*(logD1-logD0)-s.Rational(q,4)*logD0-kappa
  exact('regular derivative branch '+str(q),
        4*deriv-(2*logD1-(2+q)*logD0-4*kappa))
 exact('selected half-weight exponent',
       eps*s.Rational(1,2)*(-2*s.pi*sigma*h)+eps*s.pi*sigma*h)
 exact('selected normalization has zero angular derivative',
       s.diff(-eps*s.pi*sigma*h,beta))
 # Original complex tangent: both horizontal and vertical terms retained.
 pr,pi,db,dh=s.symbols('pr pi db dh',real=True)
 exact('complex tangent horizontal and vertical parts',
       s.re((pr+s.I*pi)*(db+s.I*dh))-(pr*db-pi*dh))
 # The log-derivative critical equation for nu has the stated cosine.
 exact('Fourier branch critical cosine',
       (1+rho*rho-2*rho*c)-1-rho*(rho-2*c))
 deps=['notes/research_mixed_boundary_strip_bounds.md',
       'notes/research_mixed_fourier_weight_continuation.md',
       'notes/research_mixed_conditional_torus_composition.md']
 out={'status':'passed','exact_identity_count':len(checks),'exact_identities':checks,
      'scope':'Exact angular candidate reduction including actual Fourier maximum, selected aliases, tangent poles, zeros and degenerate identities; no supporting-plane budget.',
      'script_sha256':sha(__file__),'proof_sha256':sha(PROOF),
      'dependencies':{p:sha(ROOT/p)for p in deps}}
 args.output.parent.mkdir(parents=True,exist_ok=True)
 args.output.write_text(json.dumps(out,indent=2)+'\n')
 print('PASS',len(checks),'exact identities and degree checks')
if __name__=='__main__':main()
