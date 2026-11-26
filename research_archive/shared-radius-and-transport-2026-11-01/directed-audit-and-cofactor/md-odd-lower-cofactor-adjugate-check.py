"""Bounded high-precision checks of literal identities, not an all-level proof.
No least-squares residual is called an exact identity.
"""
import hashlib,json
from pathlib import Path
import mpmath as mp
mp.mp.dps=90
cases=[]
for N in (5,7,9,13):
 m=N//2; th=mp.pi/N
 s=lambda j:2*mp.sin(j*th)
 a=lambda j:4*mp.cos((j+mp.mpf('.5'))*th)**2
 for xi,bi,yi in ((2,3,5),(1,2,1),(3,0,2)):
  x,b,y=map(mp.mpf,(xi,bi,yi)); A=x+y;P=x*y
  rr=[mp.mpf(1)]
  for j in range(1,m+1):
   r=b**j*mp.fprod(a(k) for k in range(j))+s(j)**2*A*rr[j-1]
   if j>=2:r+=s(j)*s(j-1)*a(j-1)*P*rr[j-2]
   rr.append(r)
  # Literal triangular Casimir block, last-row replacement.
  errs=[]
  for j in (m-1,m):
   B=mp.zeros(j+1)
   for k in range(j+1):
    B[k,k]=a(k)
    if k>=1:B[k-1,k]=-s(k)**2*A
    if k>=2:B[k-2,k]=-s(k)*s(k-1)*P
   for k in range(j+1):B[j,k]=b**k
   errs.append(abs(mp.det(B)-rr[j])/max(1,abs(rr[j])))
  # Independent positive Hermitian central determinant.
  M=mp.zeros(m)
  for k in range(m):M[k,k]=b+A/(2*mp.cos(k*th)*mp.cos((k+1)*th))
  for k in range(1,m):
   beta=mp.sin(k*th)**2/(mp.cos(k*th)**2*mp.sin((2*k-1)*th)*mp.sin((2*k+1)*th))
   z=mp.sqrt(beta)/2*(A*mp.sin(k*th)+mp.j*(y-x)*mp.cos(k*th))
   M[k-1,k]=z;M[k,k-1]=mp.conj(z)
  errs.append(abs(mp.det(M)-rr[m]/N)/max(1,abs(rr[m]/N)))
  cases.append({'N':N,'x_b_y':[xi,bi,yi],'relative_errors':[mp.nstr(e,10) for e in errs]})
  assert max(errs)<mp.mpf('1e-80')
# These discriminants are a numerical check of the separate elementary proof.
discriminants=[]
for N in (7,9,13,21):
 sm=2*mp.cos(mp.pi/(2*N));sm1=2*mp.cos(3*mp.pi/(2*N))
 v=sm**4-N*sm*sm1
 assert v<0
 discriminants.append({'N':N,'quarter_discriminant':mp.nstr(v,30)})
result={'scope':'12 literal cofactor/central-determinant evaluations at 90 decimal digits; 4 high-Taylor discriminant checks. No all-level adjugate identity, bound, or source estimate is proved by this script.','cases':cases,'discriminants':discriminants,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
path=Path('/private/tmp/md-odd-lower-cofactor-adjugate-check-results.json')
path.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'evaluations':len(cases),'maximum_relative_error':max(float(e) for c in cases for e in c['relative_errors']),'output':str(path)}))
