"""Diagnostic only: literal even two-port convolution at (cap,CROSS)=(0,-2).
No asymptotic conclusion follows from these samples."""
import mpmath as mp,json
mp.mp.dps=100
out=[]
for N in [16,32,64,96,128]:
 d=N-1;m=N//2;M=m-1;theta=mp.pi/N
 c=[2*mp.cos((2*r+1)*theta) for r in range(N)]
 a=[2+x for x in c];s=[2*mp.sin(r*theta) for r in range(N)]
 K=[[mp.mpf(1)],[s[1]**2,s[1]**2]]
 for r in range(2,N):
  row=[mp.mpf(0)]*(r+1)
  for j,v in enumerate(K[-1]):
   row[j]+=s[r]**2*v;row[j+1]+=s[r]**2*v
  for j,v in enumerate(K[-2]):row[j+1]+=s[r]*s[r-1]*a[r-1]*v
  K.append(row)
 suffix=[mp.mpf(1)]*(N+1)
 for r in range(N-1,-1,-1):suffix[r]=suffix[r+1]*a[r]
 def C(j,h):return K[d-h][j]*suffix[d-h+1]
 B=mp.mpf(1);V=[];cap=[]
 for j in range(m):
  if j:B*=s[j]**2
  V.append(B*suffix[j+1])
  cap.append((-1)**j*B*mp.fprod(-c[r] for r in range(j+1,N)))
 for u in [mp.mpf(1)/8,mp.mpf(3)/16,mp.mpf(7)/32,mp.mpf(15)/64,mp.mpf(1)/4]:
  n=int(mp.floor(u*N))
  D=mp.fsum(V[j]*C(j,n-j) for j in range(n+1))
  T=mp.fsum(cap[j]*C(j,n-j) for j in range(n+1))
  out.append({'N':N,'n':n,'u':str(u),'rate_log_ratio':str(mp.log(abs(T)/D)/N),
              'dominating_reference_j':max(range(n+1),key=lambda j:V[j]*C(j,n-j))})
print(json.dumps(out,indent=2))
