#!/usr/bin/env python3
"""Own row identities and original prefix action checks; no cycle theorem."""
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from audit_actual_q_hahn_physical_generic_jet_bound import matrix


def symbolic():
    q,U,T=sp.symbols('q U T',nonzero=True)
    D=U/T*(2*(1/q+q*T)-(q+1/q)*U)
    A=(U-T)*(1-q*q*U)/T
    Am=(U/q**2-T)*(1-U)/T
    R=-U*(q-1)**2*(T*q*q-U*q*q-U*q-U+1)/(T*q*q)
    assert sp.factor(D-q-1/q-A/q-q*Am)==0
    assert sp.factor(D-2-A-Am-R)==0
    return 2


def root_matrix(N,t,m):
    q=mp.exp(mp.pi*1j/N)
    di,up,low=matrix(N,q,t)
    J=mp.diag(di[:m])
    for r in range(m-1):
        J[r,r+1]=up[r];J[r+1,r]=low[r]
        assert abs(up[r]-low[r])<mp.mpf('1e-65')
    return q,di,up,J


def log_continuant(N,t,m,z):
    q,di,up,J=root_matrix(N,t,m)
    # All pivots are selected continuously from negative infinity.
    # In these real-z fixtures their imaginary parts are nonnegative.
    logs=[];pivot=None
    for r in range(m):
        pivot=di[r]-z-(up[r-1]**2/pivot if r else 0)
        assert mp.im(pivot)>-mp.mpf('1e-60')
        logs.append(mp.log(pivot))
    return mp.fsum(logs)


def action(tau,nu,z):
    w=2-z
    def value(x):
        A=-4*mp.exp(mp.pi*1j*(2*x-tau))*mp.sin(mp.pi*(tau-x))*mp.sin(mp.pi*x)
        # w>0 and Im A>=0 in these real-z fixtures; the product root
        # below is the continuation from negative real infinity.
        root=mp.sqrt(w)*mp.sqrt(w+4*A)
        return mp.log((w+2*A+root)/2)
    return mp.quad(value,[0,nu])


def main():
    mp.mp.dps=80
    count=dict(original_prefix_entries=0,dirichlet_forms=0,rotated_inverse_checks=0,
               selected_log_rates=0,trace_moment_checks=0)
    rows=[];largest=mp.mpf(0);moment_errors=[]
    for N in (13,24,41):
        for t in sorted(set((N//2+1,3*N//4,N-2))):
            for m in sorted(set((max(1,t//5),max(1,t//3)))):
                q,di,up,J=root_matrix(N,t,m);theta=mp.pi/N;T=q**(2*t)
                sign=mp.diag([(-1)**r for r in range(m)]);H=sign*J*sign
                A=[(q**(2*r)-T)*(1-q**(2*r+2))/T for r in range(m)]
                R=[];L=mp.zeros(m)
                for r in range(m):
                    U=q**(2*r)
                    residual=-U*(q-1)**2*(T*q*q-U*q*q-U*q-U+1)/(T*q*q)
                    R.append(residual)
                    L[r,r]=A[r]+(A[r-1] if r else 0)
                    if r<m-1:L[r,r+1]=L[r+1,r]=-A[r]
                    polar=-4*mp.exp(1j*(2*r+1-t)*theta)*mp.sin((t-r)*theta)*mp.sin((r+1)*theta)
                    assert abs(A[r]-polar)<mp.mpf('1e-65')
                assert mp.norm(H-2*mp.eye(m)-L-mp.diag(R))<mp.mpf('1e-65')
                count['original_prefix_entries']+=m*m
                v=mp.matrix([mp.mpc(r+1,1-r) for r in range(m)])
                energy=(v.H*L*v)[0]
                expected=mp.fsum(A[r]*abs(v[r]-(v[r+1] if r+1<m else 0))**2 for r in range(m))
                assert abs(energy-expected)<mp.mpf('1e-60')
                count['dirichlet_forms']+=1
                beta=mp.pi+(2*m-1-t)*theta
                for z in (-14,-3,0):
                    K=mp.exp(-1j*beta/2)*(H-z*mp.eye(m))
                    herm=(K+K.H)/2
                    lower=(2-z)*mp.cos(beta/2)-max(map(abs,R))
                    assert min(mp.eighe(herm,eigvals_only=True))>=lower-mp.mpf('1e-60')
                    if lower>0:assert mp.norm((J-z*mp.eye(m))**-1,2)<=mp.sqrt(m)/lower+mp.mpf('1e-50')
                    count['rotated_inverse_checks']+=1
    for N in (40,81,160):
        for rt,rm in ((.7,.18),(.9,.28)):
            t=int(rt*N);m=int(rm*N);tau=mp.mpf(t)/N;nu=mp.mpf(m)/N
            for z in (-14,-2,1):
                actual=log_continuant(N,t,m,z)
                predicted=N*action(tau,nu,mp.mpf(z))
                error=abs(actual-predicted)
                assert error<5
                largest=max(largest,error);count['selected_log_rates']+=1
                rows.append(dict(N=N,t=t,m=m,z=z,absolute_log_error=float(error)))
            _,_,_,J=root_matrix(N,t,m)
            for k in (1,2,3):
                power=J**k
                actual=mp.fsum(power[r,r] for r in range(m))/N
                def moment(x):
                    A=-4*mp.exp(mp.pi*1j*(2*x-tau))*mp.sin(mp.pi*(tau-x))*mp.sin(mp.pi*x)
                    D=2+2*A
                    if k==1:return D
                    if k==2:return D*D+2*A*A
                    return D**3+6*D*A*A
                expected=mp.quad(moment,[0,nu])
                # A diagnostic tolerance for these fixed fixtures, not the
                # constant in the general closed-path proof.
                assert abs(actual-expected)<1000/N
                moment_errors.append(dict(N=N,t=t,m=m,k=k,
                    normalized_error=float(abs(actual-expected)),
                    error_times_N=float(N*abs(actual-expected))))
                count['trace_moment_checks']+=1
    result=dict(status='PASS',symbolic_identities=symbolic(),counts=count,
                largest_absolute_log_error=float(largest),rates=rows,
                trace_moment_diagnostics=moment_errors,
                scope='Exact original row decomposition and selected strict-half-prefix leading action. Numerical rates supplement the analytic proof; no relative amplitude, magnetic continuation or contributing contour assertion.')
    Path(__file__).with_name('actual_casimir_off_spectrum_prefix_action_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('rates','trace_moment_diagnostics')},indent=2))


if __name__=='__main__':main()
