import json,argparse
from pathlib import Path
import mpmath as mp
parser=argparse.ArgumentParser(description='Finite diagnostic of the protected cofactor packet; uniform proof is separate.')
parser.add_argument('--output',type=Path,default=Path(__file__).with_name('actual_cross_cofactor_protected_packet_results.json'))
args=parser.parse_args()
mp.mp.dps=70
records=[]
params=[(mp.mpf(1),mp.mpf(1),mp.mpf(0)),(mp.mpf(2),mp.mpf(3),mp.mpf('-.02')),(mp.mpc(1,'.01'),mp.mpc(2,'-.02'),mp.mpc('.02','.01')),(mp.mpf('.7'),mp.mpf(4),mp.mpf('.03'))]
for pi,(x,y,u) in enumerate(params):
 for N in (32,33,64,65,128,129,256,257,512,513):
  A=x+y;P=x*y;t=mp.pi/N;n=N//2-1
  def eig(j):
   tr=2*mp.sin(j*t)*A;pr=P*(4*mp.cos((j-mp.mpf('.5'))*t)**2+u)
   gap=mp.sqrt(tr*tr+4*pr)
   return (tr+gap)/2,(tr-gap)/2,gap
  plus,minus,gap0=eig(0);pred=mp.mpf(1);cs=mp.mpf(1);prev=plus;old=mp.mpf(1);older=mp.mpf(0)
  for j in range(1,n+1):
   s=2*mp.sin(j*t);alpha=4*mp.cos((j-mp.mpf('.5'))*t)**2+u
   now=s*s*A*old+s*(2*mp.sin((j-1)*t))*alpha*P*older
   older,old=old,now
   plus,minus,gap=eig(j)
   pred*=s*plus;cs*=(prev-minus)/gap;prev=plus
  pred*=plus/gap0*cs
  error=abs(old/pred-1)
  records.append(dict(parameter=pi,N=N,error=str(error),scaled_error=str(N*error)))
  assert error<mp.mpf(3)/N,(pi,N,error)
out={'status':'PASS','scope':'Finite asymptotic diagnostic of actual protected-middle recurrence and explicit adiabatic product, including complex parameters and negative u; the uniform theorem is proved analytically.','precision':70,'checks':len(records),'max_scaled_error':max(float(r['scaled_error']) for r in records),'records':records}
args.output.write_text(json.dumps(out,indent=2)+'\n')
print(out['status'],out['checks'],out['max_scaled_error'])
