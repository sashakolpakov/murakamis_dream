#!/usr/bin/env python3
"""Exact marked five-strand weave source: expanding nonreal reflection channels."""
import itertools,time,json
from pathlib import Path
from flint import fmpz_mat,fmpz_poly,fmpq
import sympy as sp

def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[0],-x[1])
def mul(x,y):
 a,b=x;c,d=y;return(a*c-b*d,a*d+b*c-b*d)
def conj(x):return(x[0]-x[1],-x[1])
def root(k):return [(1,0),(0,1),(-1,-1)][k%3]
def local():
 plus={};minus={}
 for a,b in itertools.product(range(3),repeat=2):
  for j in range(a+1):
   c=a+b-j
   if c>=3:continue
   v=root(-b-j+j*b)
   if a==2 and j==1:v=mul(v,(1,1))
   for k in range(b+1,c+1):v=mul(v,add((1,0),neg(root(k))))
   plus[c,j,a,b]=v
 for (c,d,a,b),v in plus.items():minus[d,c,b,a]=conj(v)
 return plus,minus

def blocks(b=5):
 states=list(itertools.product(range(3),repeat=b));P,M=local(); matrices=[]
 for T in range(2*(b-1)+1):
  sts=[s for s in states if sum(s)==T];lookup={s:j for j,s in enumerate(sts)};n=len(sts);entries=[[0]*(2*n) for _ in range(2*n)]
  for col,s in enumerate(sts):
   vec={s:(1,0)}
   for pos,mat in [(i,P) for i in range(0,b-1,2)]+[(i,M) for i in range(1,b-1,2)]:
    nxt={}
    for state,v in vec.items():
     a,b0=state[pos:pos+2]
     for (c,d,aa,bb),coef in mat.items():
      if (aa,bb)!=(a,b0):continue
      out=state[:pos]+(c,d)+state[pos+2:];nxt[out]=add(nxt.get(out,(0,0)),mul(v,coef))
    vec={s:v for s,v in nxt.items() if v!=(0,0)}
   for state,(a,bb) in vec.items():
    row=lookup[state];entries[2*row][2*col]=a;entries[2*row][2*col+1]=-bb;entries[2*row+1][2*col]=bb;entries[2*row+1][2*col+1]=a-bb
  B=fmpz_mat(entries);mask=[i for i,s in enumerate(sts) if s[0]==0];W=fmpz_mat(2*n,2*n)
  for i in range(2*n):W[i,i]=1
  matrices.append((T,B,mask,W))
 return matrices

def bm(s):
 C=[fmpq(1)];B=[fmpq(1)];L=0;m=1;b=fmpq(1)
 for n in range(len(s)):
  d=fmpq(s[n])+sum((C[i]*s[n-i] for i in range(1,L+1)),fmpq(0))
  if not d:m+=1;continue
  T=C[:];coef=d/b
  if len(C)<len(B)+m:C +=[fmpq(0)]*(len(B)+m-len(C))
  for j,c in enumerate(B):C[j+m]-=coef*c
  if 2*L<=n:L=n+1-L;B=T;b=d;m=1
  else:m+=1
 return C

if __name__=='__main__':
 from audit_actual_hardy_cauchy_network import HardyNetwork
 H=HardyNetwork(3,1);plus,minus=local()
 for table,actual,scale in ((plus,H.plus,pow(H.kappa,-1,H.p)),
                            (minus,H.minus,H.kappa)):
  for a,b,c,d in itertools.product(range(3),repeat=4):
   aa,bb=table.get((c,d,a,b),(0,0))
   assert (aa+bb*H.Q)%H.p == int(actual[c*3+d,a*3+b])*scale%H.p
 assert all(int(H.pivot[a])==pow(H.Q,1-a,H.p) for a in range(3))
 start=time.time();bs=blocks();seq=[]
 for k in range(100):
  val=(0,0)
  for T,B,mask,W in bs:
   a=sum(int(W[2*i,2*i]) for i in mask);b=sum(int(W[2*i+1,2*i]) for i in mask)
   val=add(val,mul(root(4-T),(a,b)))
  assert val[1]==0,(k,val)
  seq.append(val[0]);bs=[(T,B,mask,B*W) for T,B,mask,W in bs]
 C=bm(seq)
 assert len(C)-1==43 and all(x.denominator==1 for x in C)
 cc=[int(x) for x in C];z,w=sp.symbols('z w');pol=sum(c*z**i for i,c in enumerate(cc))
 numerator=[sum(cc[j]*seq[n-j] for j in range(min(n,len(cc)-1)+1)) for n in range(len(cc)-1)]
 num=sum(c*z**i for i,c in enumerate(numerator))
 assert sp.gcd(sp.Poly(pol,z),sp.Poly(num,z)).degree()==0
 for T,B,mask,W in bs:
  n=B.nrows();E=fmpz_mat(n,n)
  for i in range(n):E[i,i]=1
  P=E
  for c in cc[1:]:P=P*B+c*E
  assert P.is_zero(),T
 p8=z**8-19*z**7+126*z**6-380*z**5+557*z**4-380*z**3+126*z**2-19*z+1
 assert sp.rem(pol,p8**2,z)==0 and sp.gcd(sp.Poly(p8,z),sp.Poly(num,z)).degree()==0
 R8=sp.resultant(p8,w-z**5,z)
 other=sp.div(pol,p8**2,z)[0]
 assert sp.gcd(sp.Poly(R8,w),sp.Poly(sp.diff(R8,w),w)).degree()==0
 assert sp.gcd(sp.Poly(R8,w),sp.Poly(sp.resultant(other,w-z**5,z),w)).degree()==0
 boxes=sp.Poly(p8,z).intervals(all=True,eps=sp.Rational(1,10000))[1]
 chosen=[]
 for (lo,hi),multiplicity in boxes:
  if sp.Rational(41,100)<sp.re(lo)<sp.re(hi)<sp.Rational(42,100) and sp.Rational(11,100)<sp.im(lo)<sp.im(hi)<sp.Rational(13,100):
   chosen.append((lo,hi))
 assert len(chosen)==1
 # The whole box is inside |z|<1 and has Im(z^5)>0.
 assert sp.Rational(42,100)**2+sp.Rational(13,100)**2<1
 assert 5*sp.Rational(41,100)**4-10*sp.Rational(42,100)**2*sp.Rational(13,100)**2>0
 output={'status':'PASS','root_level':3,'actual_braid_width':5,
         'actual_bipartite_word':[1,3,-2,-4],
         'source':'original reduced first cut and all four original pivots; full external line retained separately',
         'actual_local_crossings_and_pivot_match':True,
         'all_source_supported_integer_degree_blocks':len(bs),
         'exact_recurrence_verified_as_matrix_identity':True,
         'denominator_coefficients_ascending':cc,
         'numerator_coefficients_ascending':numerator,
         'first_moments':seq[:12],
         'denominator_factorization':str(sp.factor(pol)),
         'selected_expanding_complex_factor':str(p8),
         'isolating_box':[[str(sp.re(lo)),str(sp.im(lo)),str(sp.re(hi)),str(sp.im(hi))] for lo,hi in chosen],
         'fifth_power_resultant':str(R8),
         'all_knot_subsequence_poles_survive':True,
         'scope':'Fixed-N word-growth obstruction to a reflection-positive Hankel part plus ordinary-color/unitary finite-jet correction. Not a disproof of a polynomial-in-N correction for each fixed knot or of a word-dependent scalar norm.'}
 Path(__file__).with_name('weaving_source_expanding_reflection_channels_results.json').write_text(json.dumps(output,indent=2)+'\n')
 print('PASS exact original weave source recurrence, selected complex expanding poles, and all-knot subsequence')
