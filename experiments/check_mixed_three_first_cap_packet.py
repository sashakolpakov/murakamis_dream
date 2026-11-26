#!/usr/bin/env python3
"""Exact reduction and outward bounds for the whole physical type-three cap.

The statement is for physical outgoing j/N, not an off-grid substitution
for the original cap polynomial.
"""
import argparse, hashlib, json
from pathlib import Path
from fractions import Fraction as Q
import mpmath as mp
import sympy as sp
from flint import arb, acb, ctx
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_three_first_cap_packet.md'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--precision',type=int,default=256);ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-three-first-cap-packet.json');args=ap.parse_args();ctx.prec=args.precision;mp.mp.dps=80
 pi=arb.pi();ii=acb(0,1)
 def ar(q):q=Q(q);return arb(q.numerator)/q.denominator
 def pt(v):return acb(ar(v[0]),ar(v[1]))
 def J(v):return ((-2*pi*ii*v).exp().polylog(2)-pi*pi/6)/(2*pi*ii)-ii*pi*(v-v*v)/2
 def g(v):return J(v)+ii*pi*(v-v*v)/2
 def gp(v):return (1-(-2*pi*ii*v).exp()).log()
 def T(u,z):return -2*J(ar('1/2')-u)-2*J(u)+g(u+z)-2*g(u)-2*g(z)+ii*pi*u
 def dT(u,z):return 2*(2*(pi*u).cos()).log()-4*(2*(pi*u).sin()).log()+(2*(pi*(u+z)).sin()).log()+ii*pi*(u-z+ar('1/2'))
 def ddT(u,z):return -2*pi*(pi*u).tan()-4*pi*(pi*u).cot()+pi*(pi*(u+z)).cot()+ii*pi
 def C(x,h):return (2*pi*x).sin()/((2*pi*h).cosh()-(2*pi*x).cos())
 margins={}
 def positive(name,v):assert v>0,(name,str(v));margins[name]=str(v)
 positive('global J maximum below1/6',ar('1/6')-J(acb(ar('5/6'))).real)
 positive('small-index entropy increases', (pi/10).cos()**2*(pi/5).sin()-2*(pi/10).sin()**4)
 positive('upper regular entropy decreases',2*(2*pi/5).sin()**4-(2*pi/5).cos()**2)
 cc=min(C(ar('1/10'),ar('3/25')).lower(),C(ar('3/10'),ar('3/25')).lower())
 positive('lower horizontal interval curvature exceeds3',pi*(4*cc-(3*pi/10).cot())-3)
 cc=min(C(ar('3/10'),ar('3/25')).lower(),C(ar('2/5'),ar('3/25')).lower())
 positive('upper horizontal interval curvature exceeds3',4*pi*cc-3)
 # Recheck selected reduced roots and their absolute actions using the
 # already-certified original two-variable parameter boxes.
 source=ROOT/'repro/results/research-mixed-first-cap-critical.json';d=json.loads(source.read_text());assert d['status']=='passed'
 assert d['script_sha256']==sha(ROOT/'experiments/check_mixed_first_cap_critical.py') and d['proof_sha256']==sha(ROOT/'notes/research_mixed_first_cap_critical.md')
 branch=next(c for c in d['cases']if c['epsilon']==0);root_tests=[]
 assert Q(branch['cells'][0]['interval'][0])==Q(1,5) and Q(branch['cells'][-1]['interval'][1])==Q(9,20)
 assert all(Q(a['interval'][1])==Q(b['interval'][0])for a,b in zip(branch['cells'],branch['cells'][1:]))
 for c in branch['cells']:
  lo,hi=map(Q,c['interval']);z=acb(ar(lo).union(ar(hi)));z0=acb(ar((lo+hi)/2));u0=pt(c['centers'][1]);rr=ar('1e-60');up=u0+acb(arb(0,rr),arb(0,rr));Y=1/ddT(u0,z0)
  assert abs(Y*dT(u0,z0))+abs(1-Y*ddT(up,z0))*rr<rr
  r=ar(c['radius']);ub=u0+acb(arb(0,r),arb(0,r));assert abs(dT(ub,z))<pi
  derivative=gp(ub+z)-2*gp(z)
  lower=T(up,z0).real-abs(derivative.real)*ar((hi-lo)/2)
  assert lower>ar('26/25'),(c['interval'],str(lower))
  root_tests.append({'interval':c['interval'],'action_lower':str(lower)})
 # Every real cut point and both full horizontal alias intervals.
 endpoint_tests=alias_tests=0
 for k in range(64):
  z=acb(ar(Q(1,5)+Q(k,256)).union(ar(Q(1,5)+Q(k+1,256))))
  for cut in ['1/10','2/5']:
   v=T(acb(ar(cut)),z).real;assert v<1,(k,cut,str(v));endpoint_tests+=1
  for j in range(32):
   x=ar(Q(1,10)+Q(3*j,320)).union(ar(Q(1,10)+Q(3*(j+1),320)))
   for sign in(-1,1):
    v=T(acb(x,sign*ar('3/25')),z).real-6*pi/25
    assert v<ar('9/10'),(k,j,sign,str(v));alias_tests+=1
 # Exact terminating q-binomial algebra at several symbolic lengths;
 # the all-length identity is proved by the finite q-binomial theorem.
 r,x=sp.symbols('r x');exact=[]
 def poch(a,n):return sp.prod(1-a*r**h for h in range(n))
 for M in range(7):
  lhs=sum(poch(r**(-M),k)/poch(r,k)*x**k for k in range(M+1));rhs=poch(x*r**(-M),M)
  assert sp.cancel(lhs-rhs)==0;exact.append('terminating length '+str(M))
 for l in range(7):
  assert sp.cancel(poch(r**(-l),l)-(-1)**l*r**(-sp.Rational(l*(l+1),2))*poch(r,l))==0;exact.append('reflection length '+str(l))
 # Literal whole-source normalization diagnostics, including normal orders.
 errors=[]
 for N in range(2,13):
  q=mp.exp(mp.pi*1j/N);r0=q**-2;P=[mp.mpc(1)];S=[mp.mpf(1)]
  for j in range(1,N):P.append(P[-1]*(1-r0**j));S.append(S[-1]*2*mp.sin(mp.pi*j/N))
  # Signed Taylor jets E_l,k=(-1)^k e_l^(k)(-2), no division by zeros.
  E=[];coeff=[mp.mpf(1),mp.mpf(0),mp.mpf(0)]
  for l in range(N):
   E.append([coeff[k]*mp.factorial(k)/S[l]**2 for k in range(3)])
   factor=2*mp.cos((2*l+1)*mp.pi/N)+2
   coeff=[factor*coeff[0],factor*coeff[1]+coeff[0],factor*coeff[2]+coeff[1]]
  for k in range(3):
   H=[sum((-q)**(-l)*E[l][k]/P[l]*mp.fprod(1-r0**(-i+h)for h in range(l))for l in range(i+1))for i in range(N)]
   for j in range(N):
    a=sum(H[i]*P[i+j]/P[j]/P[i]for i in range(N-j))
    b=N/P[j]**2*sum((-q)**(-l)*E[l][k]*P[j+l]/P[l]**2 for l in range(N-j))
    err=abs(a-b)/max(1,abs(a),abs(b));assert err<mp.mpf('1e-65');errors.append(err)
 deps=['notes/research_mixed_first_cap_critical.md','experiments/check_mixed_first_cap_critical.py','repro/results/research-mixed-first-cap-critical.json','notes/research_mixed_conditional_torus_composition.md','notes/research_uniform_factorial_and_boundary_decay.md','notes/research_complete_boundary_full_index_interval.md','notes/research_complete_boundary_coefficient_asymptotic.md','notes/exact_factorial_interpolation_and_complex_contours.md']
 out={'status':'passed','precision_bits':args.precision,'scope':'Whole original type-three cap at physical outgoing indices; no off-grid identification of a reduced continuation.','root_intervals':root_tests,'strict_scalar_count':len(margins),'strict_scalars':margins,'real_cut_checks':endpoint_tests,'horizontal_alias_checks':alias_tests,'exact_finite_algebra_count':len(exact),'exact_finite_algebra':exact,'normalization_diagnostic_count':len(errors),'maximum_normalized_diagnostic_error':mp.nstr(max(errors),12),'script_sha256':sha(__file__),'proof_sha256':sha(PROOF),'dependencies':{p:sha(ROOT/p)for p in deps}}
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n');print('PASS',len(root_tests),'root intervals,',endpoint_tests,'cuts,',alias_tests,'aliases,',len(exact),'exact algebra checks,',len(errors),'normalization diagnostics')
if __name__=='__main__':main()
