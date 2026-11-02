"""Targeted tests of the stated leading phase against the exact midpoint sum.
Finite samples do not prove the asymptotic or any uniform charge estimate.
"""
from pathlib import Path
import json
import mpmath as mp
mp.mp.dps=75
HERE=Path(__file__).resolve().parent

def serial(z):
    return {'real':float(mp.re(z)),'imag':float(mp.im(z))}

def grid(N, example):
    data=[]
    if example=='unique':
        power=N-1
        for j in range(N):
            phi=(2*j+1)*mp.pi/N
            s,c=mp.sin(phi),mp.cos(phi)
            b=2-c
            h=(b/3)**power
            dh=power*s/b
            data.append((phi,s,c,h,dh))
    else:
        power=(N-1)//2
        for j in range(N):
            phi=(2*j+1)*mp.pi/N
            s,c=mp.sin(phi),mp.cos(phi)
            b=2+mp.cos(2*phi)
            h=(b/3)**power
            dh=-2*power*mp.sin(2*phi)/b
            data.append((phi,s,c,h,dh))
    return data

def exact(N,n,data):
    # The explicit Gamma_N is divided out of both exact and predicted values.
    return -mp.fsum(h*mp.exp(1j*n*N*(phi-mp.pi)**2/(4*mp.pi))*
                    (c+1j*n*N/(2*mp.pi)*(phi-mp.pi)*s+s*dh)
                    for phi,s,c,h,dh in data)/(N*N)

def predicted(N,n):
    a=mp.mpf(N-1)/N
    def A(z):
        return a*mp.log(2+mp.cos(2*mp.pi*z))
    def dA(z):
        return -a*2*mp.pi*mp.sin(2*mp.pi*z)/(2+mp.cos(2*mp.pi*z))
    def ddA(z):
        c=mp.cos(2*mp.pi*z); s=mp.sin(2*mp.pi*z)
        return -a*4*mp.pi**2*(c*(2+c)+s*s)/(2+c)**2
    z=mp.findroot(lambda z:dA(z)+2j*mp.pi*n*z+2j*mp.pi,
                  -1/(n+1j*(2*mp.pi/3)))
    Q=-ddA(z)-2j*mp.pi*n
    S=A(z)+1j*mp.pi*n*z*z+2j*mp.pi*z
    val=(-1)**(N+1)*(-2j)*mp.sqrt(2*mp.pi/N)*mp.sin(2*mp.pi*z)/mp.sqrt(Q)*mp.exp(N*(S-A(0)))
    return val,z,Q

records=[]; products=[]; negative=[]
for N in [256,257,512,513,1024,1025]:
    data=grid(N,'unique'); values={}
    for n in [12,-12,41,-41]:
        actual=exact(N,n,data); lead,z,Q=predicted(N,n)
        values[n]=(actual,lead)
        records.append({'N':N,'twist':n,'ratio':serial(actual/lead),
                        'relative_error':float(abs(actual/lead-1)),
                        'saddle':serial(z),'real_Q':float(mp.re(Q))})
        assert mp.im(z)>0 and mp.re(Q)>0
    assert abs(values[-12][0]-mp.conj(values[12][0]))<mp.mpf('1e-65')
    assert abs(values[-41][0]-mp.conj(values[41][0]))<mp.mpf('1e-65')
    products.append({'N':N,'twists':[12,-41],
      'ratio':serial(values[12][0]*values[-41][0]/(values[12][1]*values[-41][1]))})
    bad=exact(N,12,grid(N,'two_maxima'))
    negative.append({'N':N,'twist':12,'N_times_abs_normalized_functional':float(N*abs(bad))})
out={
 'precision_decimal_digits':mp.mp.dps,
 'scope':'Finite phase/amplitude probes, not a proof of a limit or uniform charge sum. The explicit Gamma_N and complete value of the source have been divided out consistently.',
 'valid_example':'C_N(delta)=(2+cos(2*pi*delta))^(N-1), satisfying Hlocal and Hgap.',
 'scalar_probes':records,'separable_two_variable_probe':products,
 'negative_control':{'source':'C_N(delta)=(2+cos(4*pi*delta))^floor((N-1)/2). It satisfies Hlocal but violates Hgap exactly: C_N(1/2)=C_N(0). This is not a counterexample under both hypotheses.',
                     'observed_endpoint_diagnostic':negative}}
(HERE/'finite-phase-probe.json').write_text(json.dumps(out,indent=2)+'\n')
print('Saved 24 signed/parity scalar probes, 6 mixed-sign tensor probes, and 6 gap-omission diagnostics.')
