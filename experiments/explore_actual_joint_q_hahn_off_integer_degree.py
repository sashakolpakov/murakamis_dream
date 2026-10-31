#!/usr/bin/env python3
"""Scoped exploration of revived finite-source terms off integer pair degree.

This tests the literal terminating source at t+eta against continued
phase/amplitude formulas. It is not a proof of a joint corridor. The
subsequent accretive determinant gives the separate exact zero theorem.
The printed error values are normalization diagnostics only.
"""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import mpmath as mp
from audit_actual_q_hahn_uniform_complex_amplitude import chosen_packet,sine_data
from audit_actual_q_hahn_selected_complex_action import energy
mp.mp.dps=150

def actual(N,t,j,u):
 q=mp.exp(mp.pi*1j/N);sf=[mp.mpf(1)]
 for k in range(1,j+1):sf.append(sf[-1]*2*mp.sin(mp.pi*k/N))
 def bs(z):
  a=[mp.mpc(1)]
  for k in range(j):a.append(a[-1]*mp.sin(mp.pi*(z-k)/N)/mp.sin(mp.pi*(k+1)/N))
  return a
 bu,bv,bt=bs(u),bs(t-u),bs(t)
 bj=[sf[j]/sf[a]/sf[j-a] for a in range(j+1)]
 w=q**(t+j-N+1)
 val=mp.fsum(w**a*bj[a]*bu[a]*bv[j-a] for a in range(j+1))/bt[j]
 return mp.exp(mp.pi*1j*u)*q**(-(j+1)*u)*val

def packet(N,t,j,u,eta):
 tau,xi,nu=mp.mpf(t)/N,mp.mpf(j)/N,mp.mpf(u)/N
 w=mp.exp(mp.pi*1j*(tau+xi-1))
 _,Acal,a,_=chosen_packet(tau,xi,nu,w)
 _,B,Fs,_=sine_data(tau,xi,nu,a,w)
 def C(t):return mp.sin(mp.pi*xi)*mp.sqrt(mp.sin(mp.pi*nu)*mp.sin(mp.pi*(t-nu))*mp.sin(mp.pi*(t-xi))/mp.sin(mp.pi*t))/2
 prevBF=B*Fs;prevC=C(tau)
 for k in range(1,21):
  tt=tau+eta*k/(20*N);ww=mp.exp(mp.pi*1j*(tt+xi-1))
  a=mp.findroot(lambda aa:sine_data(tt,xi,nu,aa,ww)[0]-ww*sine_data(tt,xi,nu,aa,ww)[1],(a,a+mp.mpf('1e-6')),tol=mp.mpf('1e-120'))
  _,B,Fs,_=sine_data(tt,xi,nu,a,ww);cc=C(tt)
  Acal*=cc/prevC*mp.sqrt(prevBF/(B*Fs));prevBF=B*Fs;prevC=cc
 phi=energy(tt,xi,nu,a)+a*mp.log(ww)+mp.pi*1j*nu*(1-xi)
 return Acal*mp.exp(mp.pi*1j*(a-nu))*mp.exp(N*phi)/mp.sqrt(N)

for N in (32,65,128,257):
 for ts,js,us in (('.8','.4','.35'),('.8','.49','.35'),('.7','.3','.25')):
  j=int(mp.floor(mp.mpf(js)*N));t=N-1-j if ts=='.7' else int(mp.floor(mp.mpf(ts)*N));u=int(mp.floor(mp.mpf(us)*N))
  for eta in (mp.mpf('.2'),mp.mpc(0,'.2'),mp.mpc(0,'-.2')):
   exact=actual(N,t+eta,j,u);pred=packet(N,t,j,u,eta)
   print(N,t,j,u,str(eta),'rel',float(abs(exact/pred-1)),'Nrel',float(N*abs(exact/pred-1)),flush=True)
