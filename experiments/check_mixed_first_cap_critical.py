#!/usr/bin/env python3
"""Outward first-cap critical branches; no full finite-source assertion."""
import argparse, hashlib, json
from pathlib import Path
from fractions import Fraction
import mpmath as mp
import sympy as sp
from flint import acb, arb, acb_mat, ctx
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_first_cap_critical.md'
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--precision',type=int,default=256)
 ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-first-cap-critical.json')
 args=ap.parse_args();ctx.prec=args.precision;mp.mp.dps=85
 pi=arb.pi();ii=acb(0,1)
 def ar(q):
  q=Fraction(q);return arb(q.numerator)/q.denominator
 def point(q): return acb(ar(mp.nstr(mp.re(q),80)),ar(mp.nstr(mp.im(q),80)))
 def cot(q): return (pi*q).cos()/(pi*q).sin()
 def equations(s,u,z,e):
  fs=-(2*(pi*(s-u)).sin()).log()+(2*(pi*(s+z)).sin()).log()-e*(2*(pi*s).sin()).log()+ii*pi*(u-z)-ii*e*pi*(ar('1/2')-s)
  fu=2*(pi*u).cos().log()+(pi*(s-u)).sin().log()-3*(pi*u).sin().log()+ii*pi*s
  return acb_mat([[fs],[fu]])
 def hessian(s,u,z,e):
  a=pi*(2*(pi*u).tan()+3*cot(u));b=pi*cot(s-u);c=-pi*cot(s+z)+e*pi*cot(s)
  return acb_mat([[-b-c+ii*e*pi,b+ii*pi],[b+ii*pi,-a-b]]),a,b,c
 def propose(z,e):
  def eq(s,u):
   return (-mp.log(2*mp.sin(mp.pi*(s-u)))+mp.log(2*mp.sin(mp.pi*(s+z)))-e*mp.log(2*mp.sin(mp.pi*s))+1j*mp.pi*(u-z)-1j*e*mp.pi*(mp.mpf('.5')-s),2*mp.log(mp.cos(mp.pi*u))+mp.log(mp.sin(mp.pi*(s-u)))-3*mp.log(mp.sin(mp.pi*u))+1j*mp.pi*s)
  return mp.findroot(eq,(mp.mpc('.42','.02') if not e else mp.mpc('.36','-.04'),mp.mpc('.23','.06')),tol=mp.mpf('1e-75'))
 def certify(lo,hi,e):
  z=acb(ar(lo).union(ar(hi)));mid=(lo+hi)/2;rr=propose(mp.mpf(mid.numerator)/mid.denominator,e);s0,u0=map(point,rr)
  J0=hessian(s0,u0,acb(ar(mid)),e)[0];Y=J0.inv();Id=acb_mat([[1,0],[0,1]])
  for radq in ['1/1000','1/500','1/250','1/125','1/64']:
   rad=ar(radq);s=s0+acb(arb(0,rad),arb(0,rad));u=u0+acb(arb(0,rad),arb(0,rad))
   J,a,b,c=hessian(s,u,z,e);E=Id-Y*J;f=Y*equations(s0,u0,z,e)
   ok=all(abs(f[i,0])+sum(abs(E[i,j])*rad for j in range(2))<rad for i in range(2))
   ok=ok and all(0<v.real<ar('1/2') for v in [u,s-u]) and ar('1/2')<(s+z).real<1
   if e:ok=ok and 0<s.real<ar('1/2')
   ok=ok and a.real>1 and b.real>0 and c.real>1
   ok=ok and ar('33/100')<s.real<ar('47/100') and ar('-9/100')<s.imag<ar('8/100') and ar('21/100')<u.real<ar('1/4') and ar('1/100')<u.imag<ar('1/10')
   if ok:
    uc=((ii+(1-2*(2*pi*ii*s).exp()).sqrt())/2).atan()/pi
    assert 0<uc.real<ar('1/2') and 0<(s-uc).real<ar('1/2')
    assert abs(equations(s,uc,z,e)[1,0])<pi
    assert all(sum(abs((Id-Y*J0)[i,j])for j in range(2))<ar('1/4')for i in range(2))
    return {'interval':[str(lo),str(hi)],'centers':[[mp.nstr(v.real,80),mp.nstr(v.imag,80)]for v in rr],'radius':radq,'s':[str(s.real),str(s.imag)],'u':[str(u.real),str(u.imag)],'hessian_a_lower':str(a.real.lower()),'hessian_c_lower':str(c.real.lower())}
  return None
 cases=[]
 for e in (0,1):
  todo=[(Fraction(1,5),Fraction(9,20),0)];cells=[]
  while todo:
   lo,hi,depth=todo.pop();r=certify(lo,hi,e)
   if r:cells.append(r);continue
   assert depth<14;mid=(lo+hi)/2
   todo.extend([(lo,mid,depth+1),(mid,hi,depth+1)])
  cells.sort(key=lambda x:Fraction(x['interval'][0]));assert Fraction(cells[0]['interval'][0])==Fraction(1,5) and Fraction(cells[-1]['interval'][1])==Fraction(9,20)
  assert all(x['interval'][1]==y['interval'][0]for x,y in zip(cells,cells[1:]))
  cases.append({'epsilon':e,'cells':cells});print('PASS branch',e,len(cells),'closed intervals',flush=True)
 # Exact elimination; the logarithmic root is certified independently above.
 U,Z=sp.symbols('U Z');V=(1+U)**2/(1-2*U+5*U**2)
 cubic=(Z-6)*U**3+(2*Z+5)*U**2+(Z-4)*U+1
 quartic=(5*Z-29)*U**4+(8*Z+36)*U**3+(2*Z-38)*U**2+20*U+Z-5
 exact=[]
 for e,p in [(0,cubic),(1,quartic)]:
  q=sp.factor(U*(1-V*Z)-(1-V*U)*(1-V)**e)
  ratio=sp.factor(q/p);expected=-1/(5*U**2-2*U+1) if not e else -U/(5*U**2-2*U+1)**2
  assert sp.cancel(ratio-expected)==0 and sp.cancel(q-expected*p)==0
  exact.append(str(ratio))
 # A separate, rigorous obstruction to cutting the type-three outer index at1/2.
 z=acb(ar('1/5'));rr=propose(mp.mpf(1)/5,0);s0,u0=map(point,rr);rad=ar('1e-65');s=s0+acb(arb(0,rad),arb(0,rad));u=u0+acb(arb(0,rad),arb(0,rad));Y=hessian(s0,u0,z,0)[0].inv();E=acb_mat([[1,0],[0,1]])-Y*hessian(s,u,z,0)[0];f=Y*equations(s0,u0,z,0)
 assert all(abs(f[i,0])+sum(abs(E[i,j])*rad for j in range(2))<rad for i in range(2))
 def J(v):return ((-2*pi*ii*v).exp().polylog(2)-pi*pi/6)/(2*pi*ii)-ii*pi*(v-v*v)/2
 def F(s,u,z,e):return -2*J(ar('1/2')-u)-3*J(u)-J(s-u)+J(s+z)-J(z)-e*J(s)+ii*pi*s*(u-z)-ii*e*pi*(s-s*s)/2
 uh=((ii+(1-2*(2*pi*ii*ar('1/2')).exp()).sqrt())/2).atan()/pi
 # At s=1/2, sqrt(3) is positive and fixes the original endpoint branch.
 assert abs(equations(acb(ar('1/2')),uh,z,0)[1,0])<ar('1e-60')
 excess=(F(acb(ar('1/2')),uh,z,0)-F(s,u,z,0)).real
 assert excess>ar('11/1000')
 deps=['notes/research_mixed_complete_boundary_sum.md','notes/research_complete_boundary_coefficient_asymptotic.md','notes/research_mixed_conditional_torus_composition.md']
 out={'status':'passed','precision_bits':args.precision,'scope':'Original two-variable zero-lift branches and a resummed outer-index cutoff obstruction only; no full cap source theorem.','cases':cases,'exact_elimination_factors':exact,'half_index_action_excess':str(excess),'proof_sha256':sha(PROOF),'script_sha256':sha(__file__),'dependencies':{p:sha(ROOT/p)for p in deps}}
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n');print('PASS two exact eliminations; half-index excess',excess)
if __name__=='__main__':main()
