import mpmath as mp
mp.mp.dps=90
s=mp.mpc('0.23','0.11')
for N in (20,21,40,41,80,81):
 r=int(mp.mpf('.31')*N);th=mp.pi/N;d=N-1
 S=mp.fprod([2*mp.sin(j*th) for j in range(1,r+1)])
 def e(t):
  return mp.fprod([2*mp.cos((2*j+1)*th)+2*mp.cos(t) for j in range(r)])/S**2
 def Q(a,eps):
  return mp.fsum([e(t)*mp.exp(1j*eps*N*t*t/(4*mp.pi)) for t in [2*mp.pi*(mp.mpf(d)/2+a-j)/N for j in range(N)]])
 for eps in (1,-1):
  err=abs(Q(s,eps)/Q(0,eps)-1)
  print(N,r,eps,mp.nstr(err,10),mp.nstr(mp.log(err)/N,8))
