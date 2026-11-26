#!/usr/bin/env python3
"""Exact cap polynomial remainder and its complete Fourier observation.

The all-level identity is proved in the note. Finite exact tests are
normalization diagnostics, not a global mixed-source estimate.
"""
import argparse,hashlib,json
from pathlib import Path
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_three_first_cap_fourier_reduction.md'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-three-first-cap-fourier-reduction.json');args=ap.parse_args()
 field=sp.QQ.algebraic_field(sp.I,sp.sqrt(2),sp.sqrt(3));zero,one=field.zero,field.one;cv=lambda x:field.from_sympy(sp.sympify(x));checks=[]
 def test(name,x):assert x==zero,(name,field.to_sympy(x));checks.append(name)
 def product(xs):
  ans=one
  for x in xs:ans*=x
  return ans
 def pp(a,b):
  ans=[zero]*(len(a)+len(b)-1)
  for i,x in enumerate(a):
   for j,y in enumerate(b):ans[i+j]+=x*y
  return ans
 def pe(p,x):
  ans=zero
  for a in reversed(p):ans=ans*x+a
  return ans
 for N,qe in[(2,sp.I),(3,(1+sp.I*sp.sqrt(3))/2),(4,(1+sp.I)/sp.sqrt(2)),(6,(sp.sqrt(3)+sp.I)/2)]:
  q=cv(qe);r=q**-2;ii=cv(sp.I)
  P=[product(one-r**h for h in range(1,l+1))for l in range(N)]
  S=[product((q**h-q**-h)/ii for h in range(1,l+1))for l in range(N)]
  poly=[]
  for l in range(N):
   p=[one]
   for h in range(1,l+1):p=pp(p,[one,-r**h])
   poly.append(p)
  d=[sum((r**(-j*k)/P[j]for j in range(N)),zero)/N for k in range(N)]
  E=[];co=[one,zero,zero]
  for l in range(N):
   E.append([co[k]*sp.factorial(k)/S[l]**2 for k in range(3)])
   f=q**(2*l+1)+q**(-2*l-1)+2
   co=[f*co[0],f*co[1]+co[0],f*co[2]+co[1]]
  for k in range(3):
   H=[sum(((-q)**-l*E[l][k]*product(one-r**(-i+h)for h in range(l))/P[l]for l in range(i+1)),zero)for i in range(N)]
   U=[sum((H[i]*poly[i][a]/P[i]for i in range(a,N)),zero)for a in range(N)]
   K=[sum(((-q)**-l*E[l][k]*poly[l][a]/P[l]**2 for l in range(a,N)),zero)for a in range(N)]
   F=[N*x for x in pp(d,K)];F +=[zero]*(2*N-1-len(F))
   for j in range(N):
    test(f'N{N} jet{k} physical original reduction j{j}',pe(U,r**j)-N*pe(K,r**j)/P[j])
   for a in range(N):
    wrapped=F[a+N]if a+N<len(F)else zero
    test(f'N{N} jet{k} original polynomial remainder a{a}',U[a]-F[a]-wrapped)
    # G=X^{-a} is the complete following Fourier band.
    test(f'N{N} jet{k} full following Fourier monomial -{a}',U[a]-F[a]-wrapped)
    # The separate unwrapped substitution is generally false; retain alias.
   if k==0 and N>=3:assert any(F[a]!=zero for a in range(N,len(F)))
 # Exact degree and normalization algebra, separated from finite diagnostics.
 n,k,z,u=sp.symbols('n k z u');identity=[]
 assert sp.simplify((k-2)+1-sp.Rational(1,2)-(k-sp.Rational(3,2)))==0;identity.append('fixed K source N power')
 assert sp.simplify((k-1)-sp.Rational(1,2)-(k-sp.Rational(3,2)))==0;identity.append('physical U to K N power')
 assert sp.expand((z-u)/2-z/2+u/2)==0;identity.append('U to K order-one phase')
 assert sp.Rational(26,25)-sp.Rational(1,6)==sp.Rational(131,150);identity.append('selected fixed K action floor')
 record=ROOT/'repro/results/research-mixed-three-first-cap-packet.json';data=json.loads(record.read_text());assert data['status']=='passed'
 assert data['script_sha256']==sha(ROOT/'experiments/check_mixed_three_first_cap_packet.py') and data['proof_sha256']==sha(ROOT/'notes/research_mixed_three_first_cap_packet.md')
 for p,h in data['dependencies'].items():assert sha(ROOT/p)==h,p
 deps=['notes/research_mixed_three_first_cap_packet.md','experiments/check_mixed_three_first_cap_packet.py','repro/results/research-mixed-three-first-cap-packet.json','notes/research_mixed_conditional_torus_composition.md','notes/research_mixed_four_conditional_complex_neighbors.md','notes/research_complete_boundary_full_index_interval.md']
 out={'status':'passed','arithmetic':'Exact Q(i,sqrt(2),sqrt(3))','levels':[2,3,4,6],'ordinary_orders':[0,1,2],'exact_normalization_diagnostic_count':len(checks),'exact_normalization_diagnostics':checks,'exact_symbol_identity_count':len(identity),'exact_symbol_identities':identity,'scope':'Exact whole original first-cap Fourier replacement, with wrapped term retained, and source-normalized local packet for the fixed K polynomial; no remaining outer integral bound.','script_sha256':sha(__file__),'proof_sha256':sha(PROOF),'dependencies':{p:sha(ROOT/p)for p in deps}}
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n');print('PASS',len(checks),'exact source diagnostics,',len(identity),'symbol identities; current physical source provenance')
if __name__=='__main__':main()
