#!/usr/bin/env python3
"""Original Green phase, anti-diagonal sign and selected spectral action."""
import json
from pathlib import Path

import mpmath as mp

from audit_high_color_first_normal_r_degree import root_field
from audit_actual_q_hahn_physical_generic_jet_bound import Jet, matrix
from audit_actual_casimir_off_spectrum_prefix_action import action, log_continuant, root_matrix


def exact_phases():
    count=dict(actual_reversed_prefixes=0,original_Green_phase_entries=0,
               exact_antidiagonal_phase_entries=0)
    Jet.order=1
    for N in range(3,14):
        p,eta=root_field(N);q=eta*eta%p;imag=pow(eta,N,p);Jet.p=p
        sine=lambda r:(pow(q,r,p)-pow(q,-r,p))*pow(2*imag,-1,p)%p
        for t in range(N):
            dj,uj,lj=matrix(N,Jet(q),t)
            di,up,lo=[x.c[0] for x in dj],[x.c[0] for x in uj],[x.c[0] for x in lj]
            db,ub,lb=matrix(N,Jet(pow(q,-1,p)),t)
            assert di==list(reversed([x.c[0] for x in db]))
            assert up==lo==list(reversed([x.c[0] for x in ub]))
            lams=[(pow(q,2*m+1,p)+pow(q,-2*m-1,p))%p for m in range(t+1)]
            z=next(z for z in range(2,p) if z not in lams)
            pre=[1];bar=[1];tail=[0]*(t+2);tail[-1]=1
            for r in range(t+1):
                pre.append(((di[r]-z)*pre[-1]-(up[r-1]*lo[r-1]*pre[-2] if r else 0))%p)
                bar.append(((db[r].c[0]-z)*bar[-1]-(ub[r-1].c[0]*lb[r-1].c[0]*bar[-2] if r else 0))%p)
            for r in range(t,-1,-1):tail[r]=((di[r]-z)*tail[r+1]-(up[r]*lo[r]*tail[r+2] if r<t else 0))%p
            assert all(tail[r]==bar[t-r+1] for r in range(t+2))
            count['actual_reversed_prefixes']+=t+2
            denominator=1
            for lam in lams:denominator=denominator*(lam-z)%p
            assert denominator==pre[-1]
            for u in range(t+1):
                for v in range(u,t+1):
                    original_product=positive_product=1
                    for r in range(u,v):
                        original_product=original_product*up[r]%p
                        positive_product=positive_product*4*sine(t-r)*sine(r+1)%p
                    # Actual zI-J cofactors, with all three signs retained.
                    sign=1 if (u+t-v-(t+1))%2==0 else -1
                    original=original_product*sign*pre[u]*tail[v+1]*pow(denominator,-1,p)%p
                    revised=-pow(q,(v-u)*(u+v-t),p)*positive_product*pre[u]*bar[t-v]*pow(denominator,-1,p)%p
                    assert original==revised
                    count['original_Green_phase_entries']+=1
                    if u+v==t:
                        assert revised==-positive_product*pre[u]*bar[u]*pow(denominator,-1,p)%p
                        count['exact_antidiagonal_phase_entries']+=1
    return count


def selected_green_log(N,t,u,v,z):
    theta=mp.pi/N
    phase=1j*theta*(v-u)*(u+v-t)
    middle=mp.fsum(mp.log(4*mp.sin((t-r)*theta)*mp.sin((r+1)*theta)) for r in range(u,v))
    denominator=mp.fsum(mp.log(2*mp.cos((2*m+1)*theta)-z) for m in range(t+1))
    return phase+middle+log_continuant(N,t,u,z)+mp.conj(log_continuant(N,t,t-v,z))-denominator


def prefix_derivative(N,t,m,z):
    _,diag,up,_=root_matrix(N,t,m);pivot=der=None;out=0
    for r in range(m):
        nxt=diag[r]-z-(up[r-1]**2/pivot if r else 0)
        nxt_der=-1+(up[r-1]**2*der/pivot**2 if r else 0)
        out+=nxt_der/nxt;pivot,der=nxt,nxt_der
    return out


def limiting_green(tau,nu,omega,z):
    phase=1j*mp.pi*(omega-nu)*(nu+omega-tau)
    middle=mp.quad(lambda s:mp.log(4*mp.sin(mp.pi*(tau-s))*mp.sin(mp.pi*s)),[nu,omega])
    denominator=mp.quad(lambda s:mp.log(2*mp.cos(2*mp.pi*s)-z),[0,tau])
    return phase+middle+action(tau,nu,z)+mp.conj(action(tau,tau-omega,z))-denominator


def limiting_derivative(tau,nu,omega,z):
    w=2-z
    def part(b):
        def f(s):
            A=-4*mp.exp(mp.pi*1j*(2*s-tau))*mp.sin(mp.pi*(tau-s))*mp.sin(mp.pi*s)
            return -1/(mp.sqrt(w)*mp.sqrt(w+4*A))
        return mp.quad(f,[0,b])
    return part(nu)+mp.conj(part(tau-omega))+mp.quad(lambda s:1/(2*mp.cos(2*mp.pi*s)-z),[0,tau])


def generic_green(N,t,u,v,z,h):
    """Actual generic forward/backward entries: no conjugation off the root."""
    q=mp.exp(mp.pi*1j/N+h);di,up,lo=matrix(N,q,t)
    before=mp.mpc(1);older=mp.mpc(0)
    for r in range(u):
        before,older=(z-di[r])*before-(up[r-1]*lo[r-1]*older if r else 0),before
    after=mp.mpc(1);older=mp.mpc(0)
    for r in range(t,v,-1):
        after,older=(z-di[r])*after-(up[r]*lo[r]*older if r<t else 0),after
    denominator=mp.fprod(z-q**(2*N-2*m-1)-q**(-2*N+2*m+1) for m in range(t+1))
    return mp.fprod(up[r] for r in range(u,v))*before*after/denominator


def normal_diagnostics():
    circles=jets=0;largest=largest_jet=mp.mpf(0)
    for N in (24,41,80):
        t=4*N//5;u=N//5
        for v in sorted(set((t-u,3*N//5+1))):
            for z in (mp.mpf(-3),mp.mpf(-14)):
                root=generic_green(N,t,u,v,z,mp.mpf(0))
                assert abs(root+mp.exp(selected_green_log(N,t,u,v,z)))<mp.mpf('1e-60')*max(1,abs(root))
                radius=mp.mpf('.01')/N**2
                for k in range(8):
                    h=radius*mp.exp(2*mp.pi*1j*k/8)
                    ratio=generic_green(N,t,u,v,z,h)/root
                    bound=max(abs(ratio),1/abs(ratio))
                    assert bound<2
                    largest=max(largest,bound);circles+=1
                for order in (1,2):
                    derivative=mp.diff(lambda h:generic_green(N,t,u,v,z,h),mp.mpf(0),order)
                    normalized=abs(derivative/root)/N**(2*order)
                    assert normalized<100
                    largest_jet=max(largest_jet,normalized);jets+=1
    return dict(actual_generic_circle_ratios_and_inverses=circles,genuine_generic_q_derivatives=jets,
                largest_relative_circle_bound=float(largest),largest_N2r_scaled_relative_jet=float(largest_jet))


def diagnostics():
    mp.mp.dps=80;negative=0;direct_entries=0
    for N in (3,4,5,8,11):
        for t in sorted(set((N//2,N-1))):
            _,_,_,J=root_matrix(N,t,t+1)
            for z in (-3,-14):
                R=(z*mp.eye(t+1)-J)**-1
                for u in range(t//2+1):
                    v=t-u;entry=R[u,v]
                    assert mp.re(entry)<0 and abs(mp.im(entry))<mp.mpf('1e-60')
                    negative+=1
                    predicted=-mp.exp(selected_green_log(N,t,u,v,mp.mpf(z)))
                    assert abs(predicted-entry)<mp.mpf('1e-60')*max(1,abs(entry))
                    direct_entries+=1
    rows=[];largest=der_largest=mp.mpf(0)
    for N in (40,81,160):
        for rt,ru,rv in ((mp.mpf('.7'),mp.mpf('.18'),None),(mp.mpf('.9'),mp.mpf('.2'),mp.mpf('.62'))):
            t=int(rt*N);u=int(ru*N);v=t-u if rv is None else int(rv*N)
            tau,nu,omega=mp.mpf(t)/N,mp.mpf(u)/N,mp.mpf(v)/N
            for z in map(mp.mpf,('-14','-3')):
                actual=selected_green_log(N,t,u,v,z)
                predicted=N*limiting_green(tau,nu,omega,z)
                error=abs(actual-predicted);assert error<15
                actual_der=prefix_derivative(N,t,u,z)+mp.conj(prefix_derivative(N,t,t-v,z))
                actual_der+=mp.fsum(1/(2*mp.cos((2*m+1)*mp.pi/N)-z) for m in range(t+1))
                der_error=abs(actual_der-N*limiting_derivative(tau,nu,omega,z));assert der_error<5
                largest=max(largest,error);der_largest=max(der_largest,der_error)
                if u+v==t:
                    assert abs(mp.im(actual))<mp.mpf('1e-60')
                    assert abs(mp.im(predicted))<mp.mpf('1e-60')
                rows.append(dict(N=N,t=t,u=u,v=v,z=float(z),absolute_log_error=float(error),absolute_derivative_error=float(der_error)))
    return dict(strict_negative_original_antidiagonal_entries=negative,independent_actual_inverse_comparisons=direct_entries,
                selected_cross_central_rates=len(rows),selected_spectral_derivative_rates=len(rows),
                largest_absolute_log_error=float(largest),largest_absolute_derivative_error=float(der_largest),rates=rows)


def main():
    result=dict(status='PASS',exact=exact_phases(),diagnostics=diagnostics(),generic_normals=normal_diagnostics(),
                scope='Original Green phases, exact anti-diagonal sign, strict cross-central leading action and genuine fixed generic-q normal bounds. No relative amplitude, complex rows, closing-segment bound or selected contour contribution.')
    Path(__file__).with_name('actual_matching_edge_cross_central_green_action_results.json').write_text(json.dumps(result,indent=2)+'\n')
    short=dict(result);short['diagnostics']={k:v for k,v in result['diagnostics'].items() if k!='rates'}
    print(json.dumps(short,indent=2))


if __name__=='__main__':main()
