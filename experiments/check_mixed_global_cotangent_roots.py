#!/usr/bin/env python3
"""Exact global cotangent-root boundaries, Rouche count, and original lift."""
import argparse,hashlib,json
from fractions import Fraction
from pathlib import Path
import sympy as sp
from flint import arb,acb,ctx
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_global_cotangent_roots.md'
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--precision',type=int,default=256)
 parser.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-global-cotangent-roots.json')
 args=parser.parse_args();assert args.precision>=128;ctx.prec=args.precision
 initial_script,initial_proof=sha(__file__),sha(PROOF)
 deps={'notes/research_mixed_plateau_accretivity.md':sha(ROOT/'notes/research_mixed_plateau_accretivity.md')}
 exact=[]
 def zero(name,value):
  assert sp.cancel(sp.expand(value))==0,name
  exact.append(name)
 P,Q,S=sp.symbols('P Q S');ii=sp.I
 A=(P-ii)/(P+ii);B=(Q-ii)/(Q+ii);U=(S-ii)/(S+ii)
 F0=S*S+(P+Q)*S-1+ii*(Q-P)
 F1=(S+ii)*(S+P)*(S+Q)-2*ii*(P-ii)*(Q+ii)
 zero('quadratic exponentiation',(1-A*U)*(1-B*U)-A*(1-U)**2+4*F0/((P+ii)*(Q+ii)*(S+ii)**2))
 zero('cubic exponentiation',(1-A*U)*(1-B*U)-A*(1-U)**3+4*F1/((P+ii)*(Q+ii)*(S+ii)**3))
 p,q,u,v,alpha,beta=sp.symbols('p q u v alpha beta',real=True)
 sub={P:p+ii*alpha,Q:q+ii*beta}
 zero('quadratic upper boundary',sp.im(F0.subs(sub).subs(S,u+ii))-u*(2+alpha+beta)-2*q)
 zero('quadratic lower boundary',sp.im(F0.subs(sub).subs(S,u-ii))-u*(-2+alpha+beta)+2*p)
 zero('quadratic left boundary',sp.re(F0.subs(sub).subs(S,ii*v))-(-1-v*v+alpha*(1-v)-beta*(1+v)))
 remainder=2*(alpha-1)*(beta+1)-(v+1)*(alpha+v)*(beta+v)
 zero('cubic left boundary',sp.im(F1.subs(sub).subs(S,ii*v))-((v-1)*p*q+remainder))
 corners=[
 (sp.Rational(1,2),sp.Rational(1,2),-sp.Rational(3,2)-(v+1)*(v+sp.Rational(1,2))**2),
 (-sp.Rational(1,2),-sp.Rational(1,2),-sp.Rational(3,2)-(v+1)*(v-sp.Rational(1,2))**2),
 (sp.Rational(1,2),-sp.Rational(1,2),-sp.Rational(1,2)+(v+1)*(sp.Rational(1,4)-v*v)),
 (-sp.Rational(1,2),sp.Rational(1,2),-sp.Rational(9,2)+(v+1)*(sp.Rational(1,4)-v*v))]
 for j,(aa,bb,expr)in enumerate(corners):zero('left bilinear corner '+str(j),remainder.subs({alpha:aa,beta:bb})-expr)
 assert sp.Rational(1,2)-sp.Rational(3,2)*sp.Rational(1,4)==sp.Rational(1,8)
 top=u+ii;QQ=q+ii*beta
 den=(top+ii)*(top+QQ)-2*ii*(QQ+ii)
 num=2*(QQ+ii)-top*(top+ii)*(top+QQ)
 zero('upper denominator',den-u*(u+QQ+3*ii))
 # Avoid assumptions on signs in the exact rational identity.
 imagP=sp.im(sp.expand_complex(num/den))
 expected=-1-2*(4*q+u*q*(u+q)+u*(beta+1)**2)/(u*((u+q)**2+(beta+3)**2))
 zero('upper forced imaginary part',imagP-expected)
 lower_ratio=(p+u+ii*(alpha-1))/(p+ii*(alpha-1))
 zero('lower first factor real',sp.re(lower_ratio)-1-u*p/(p*p+(alpha-1)**2))
 zero('lower first factor imaginary',sp.im(lower_ratio)-u*(1-alpha)/(p*p+(alpha-1)**2))
 zero('quadratic base',F0.subs({P:1,Q:1})-(S*S+2*S-1))
 f=sp.expand(F1.subs({P:1,Q:1}))
 zero('cubic base',f-(S**3+(2+ii)*S*S+(1+2*ii)*S-3*ii))
 r=sp.Rational(1,20)
 centers=[sp.Rational(3,5)+ii/3,-sp.Rational(21,10)+ii*sp.Rational(11,20),-sp.Rational(1,2)-ii*sp.Rational(19,10)]
 expected_margins=[sp.Rational(5621,43200),sp.Rational(1971,8000),sp.Rational(2359,8000)]
 rouche=[]
 for j,c in enumerate(centers):
  f0=sp.expand(f.subs(S,c));df=sp.expand(sp.diff(f,S).subs(S,c));quad=3*c+2+ii
  margin=r*max(abs(sp.re(df)),abs(sp.im(df)))-abs(sp.re(f0))-abs(sp.im(f0))-r*r*(abs(sp.re(quad))+abs(sp.im(quad)))-r**3
  assert margin==expected_margins[j]and margin>0
  if j==0:assert sp.re(c)>r and abs(sp.im(c))+r<1
  else:assert sp.re(c)+r<0
  rouche.append({'center':str(c),'radius':str(r),'margin':str(margin)})
 for j in range(3):
  for k in range(j):assert abs(sp.re(centers[j]-centers[k]))>2*r
 zero('wide-strip counterexample',F0.subs({P:1+99*ii/100,Q:1-99*ii/100})-(S*S+2*S+sp.Rational(49,50)))
 # Exact radical identity for the quadratic zero lift.
 zero('quadratic positive root',F0.subs({P:1,Q:1,S:sp.sqrt(2)-1}))
 pi=arb.pi();I=acb(0,1)
 ar=lambda x:arb(Fraction(x).numerator)/Fraction(x).denominator
 sbox=acb(ar('3/5')+arb(0,ar('1/20')),ar('1/3')+arb(0,ar('1/20')))
 z=(sbox-I)/(sbox+I)
 lifted=2*(1+I*z).log()-3*(1-z).log()+I*pi/2
 assert abs(lifted.imag)<pi
 scalar=[{'name':'cubic original zero logarithmic lift','margin':str(pi-abs(lifted.imag))}]
 cot_bound=(2*pi*ar('57/1000')).sinh()/(2*(pi*ar('11/50')).sin()**2)
 assert cot_bound<ar('1/2')
 scalar.append({'name':'whole quadratic-taper cotangent half-strip','bound':str(cot_bound),'margin':str(ar('1/2')-cot_bound)})
 assert initial_script==sha(__file__)and initial_proof==sha(PROOF)
 assert all(sha(ROOT/p)==h for p,h in deps.items())
 result={'status':'passed','precision_bits':args.precision,'exact_identity_count':len(exact),'exact_identities':exact,
         'rational_rouche_disks':rouche,'rational_rouche_count':3,'strict_scalar_comparisons':scalar,
         'proof_sha256':initial_proof,'script_sha256':initial_script,'dependencies':deps,
         'scope':'Unique simple original zero-lift conditional roots for both types on the global cotangent half-strip; local coercivity and taper applicability only. No finite-source dominance or whole-period lower bound.'}
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n')
 print('PASS',len(exact),'exact identities,3 rational Rouche disks,2 outward comparisons')
if __name__=='__main__':main()
