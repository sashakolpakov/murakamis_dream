"""Exact Hermitian cone and actual ordinary packets outside the central wedge.

The proof supplies the domains and uniform errors. These checks retain
literal source normalization, both parities, the folded endpoint, and a
vanishing offdiagonal in the generic perturbation adapter.
"""
import json
from pathlib import Path
import mpmath as mp
import numpy as np
import sympy as sp
from audit_actual_two_cut_ports import balanced_data
from audit_actual_q_hahn_partner_normal_collision import finite_h
from audit_actual_q_hahn_joint_complex_amplitude import Source, selected_packet, transport
from audit_actual_q_hahn_small_channel_generic_normals import jacobi, determinant


def symbolic_cones():
    E,G = sp.symbols('E G',nonzero=True)
    si = lambda w:(w-1/w)/(2*sp.I)
    co = lambda w:(w+1/w)/2
    assert sp.cancel(si(E*G)*si(E/G)-co(G)**2+co(E)**2)==0
    # The two offdiagonal phases in H_+ have modulus one formally.
    assert sp.cancel((si(E)+sp.I*co(E))*(si(E)-sp.I*co(E))-1)==0
    s,C,z = sp.symbols('s C z')
    u=sp.Matrix([1,0]);v=sp.Matrix([s,C])
    B=G*u*u.T+v*v.T/G
    residual=sp.expand((sp.eye(2)-z*B).det()-(1-(G+1/G)*z+C*C*z*z))
    assert sp.rem(residual,s*s+C*C-1,s)==0
    return dict(offdiagonal_product=True,unitary_H_phases=True,
                PSD_symbol_determinant=True)


def exact_source_checks():
    checks=0
    for N in range(3,24):
        p,eta,q,*_=balanced_data(N)
        Q,ii=q*q%p,pow(eta,N,p)
        inv2,inv2i=pow(2,-1,p),pow(2*ii,-1,p)
        si=lambda v:(v-pow(v,-1,p))*inv2i%p
        co=lambda v:(v+pow(v,-1,p))*inv2%p
        sine=lambda r:si(pow(q,r,p))
        cosine=lambda r:co(pow(q,r,p))
        sf=[1]
        for r in range(1,N):sf.append(sf[-1]*(1-pow(Q,r,p))%p)
        for G,U in ((17,11),(29,7)):
            sigma=G*pow(q,-1,p)%p
            T=sigma*sigma%p
            z=sigma*pow(U,-1,p)%p
            cg=co(G)
            old,new=1,(z-cg*pow(cosine(1),-1,p))%p
            for j in range(1,(N-1)//2+1):
                if j>1:
                    n=j-1
                    bn=sine(n)**2*pow(cosine(n)**2*sine(2*n-1)*sine(2*n+1)%p,-1,p)%p
                    upper=bn*si(pow(q,n,p)*G%p)%p
                    lower=si(pow(q,n,p)*pow(G,-1,p)%p)
                    old,new=new,((z-cg*pow(cosine(n)*cosine(n+1)%p,-1,p))*new-upper*lower*old)%p
                den=1
                for r in range(j):den=den*(T-pow(Q,r,p))%p
                if not den:continue
                F=finite_h(j,Q,1,pow(U,-1,p),T,p)
                choose=sf[2*j]*pow(sf[j]**2%p,-1,p)%p
                direct_R=F*den*pow(pow(sigma,j,p)*choose%p,-1,p)%p
                assert direct_R==new
                checks+=1
    return checks


def matrices(N,j):
    th=mp.pi/N
    A,K,D=mp.matrix(j),mp.matrix(j),mp.matrix(j)
    for n in range(j):
        A[n,n]=D[n,n]=1/(mp.cos(n*th)*mp.cos((n+1)*th))
    for n in range(1,j):
        root=mp.sin(n*th)/(mp.cos(n*th)*mp.sqrt(mp.sin((2*n-1)*th)*mp.sin((2*n+1)*th)))
        D[n-1,n]=D[n,n-1]=root
        A[n-1,n]=A[n,n-1]=root*mp.sin(n*th)
        K[n-1,n]=root*mp.cos(n*th);K[n,n-1]=-K[n-1,n]
    return A,K,D


def finite_boundary_and_adapters():
    mp.mp.dps=180
    boundary=adapters=zero_upper=0
    max_error=mp.mpf(0)
    for N in (3,4,7,12,25,41):
        tau=1-mp.mpf(1)/(4*N)+1j
        z=mp.cos(mp.pi*(tau+mp.mpf(1)/N))/mp.cos(mp.pi/N)
        nu=(tau-mp.log(z)/(mp.pi*1j))/2
        assert 0<mp.re(nu)<mp.re(tau)<1
        assert abs(mp.arg(z))<mp.pi*mp.re(tau)
        assert abs(Source(N,1).determinant(tau,nu))<mp.mpf('1e-160')
        boundary+=1
    for N in (16,17,32,33):
        j=(N-1)//2;t=(3*N)//4
        tau,nu=mp.mpf(t)/N,mp.mpc('.06','.015')
        assert abs(mp.re(tau-2*nu))>mp.mpf('.5')
        q0=mp.exp(mp.pi*1j/N);gamma=mp.pi*(tau+mp.mpf(1)/N)
        A,K,D=matrices(N,j)
        Hplus,Hminus=A+1j*K,A-1j*K
        for H in (Hplus,Hminus):
            arr=np.array(H.tolist(),dtype=complex)
            assert np.linalg.eigvalsh(arr)[0]>0
        rootM=mp.exp(mp.pi*1j*(tau-2*nu))*mp.eye(j)-mp.cos(gamma)*A-mp.sin(gamma)*K
        choices=[]
        for n in range(1,j):
            upper,lower=rootM[n-1,n],rootM[n,n-1]
            if abs(upper)<mp.mpf('1e-160'):
                zero_upper+=1
                assert abs(lower)>mp.mpf('.01')
            choices.append(('upper',upper) if abs(upper)>=abs(lower) else ('lower',lower))
        for phase in (0,mp.pi/2):
            eps=mp.mpf('.1')*mp.exp(1j*phase)/N**8
            q=q0*mp.exp(eps);sigma=q**t;z=q**(t-2*N*nu)
            alpha,beta=jacobi(N,q,sigma,j)
            M=mp.matrix(j)
            for n in range(j):M[n,n]=z+alpha[n]
            for n,(side,value) in enumerate(choices,1):
                if side=='upper':M[n-1,n],M[n,n-1]=value,-beta[n]/value
                else:M[n,n-1],M[n-1,n]=value,-beta[n]/value
            target=determinant(N,q,sigma,j,z)
            error=abs(mp.det(M)/target-1)
            assert error<mp.mpf('1e-160')
            max_error=max(max_error,error);adapters+=1
    return dict(exact_boundary_counterexamples_checked=boundary,
                genuine_zero_upper_entries_avoided=zero_upper,
                original_generic_tridiagonal_adapters=adapters,
                maximum_adapter_relative_error=mp.nstr(max_error,30))


def full_physical_amplitudes():
    mp.mp.dps=180
    cases=[(mp.mpc('.8','.02'),mp.mpc('.07','.01'),'fold'),
           (mp.mpc('.8','-.02'),mp.mpc('.73','-.01'),'fold'),
           (mp.mpc('.9','.025'),mp.mpc('.12','-.01'),'.4'),
           (mp.mpc('.9','-.025'),mp.mpc('.78','.01'),'.4')]
    rows=[];max_source=max_error=max_gradient=mp.mpf(0);gradients=0
    for N in (32,65,128,257):
        for tau,nu,kind in cases:
            assert abs(mp.re(tau-2*nu))>mp.mpf('.5')
            assert 0<mp.re(nu)<mp.re(tau)<1
            j=(N-1)//2 if kind=='fold' else int(mp.floor(mp.mpf(kind)*N))
            src=Source(N,j)
            exact,literal=src.determinant(tau,nu),src.direct(tau,nu)
            source_error=abs(literal/exact-1)
            assert source_error<mp.mpf('1e-115')
            max_source=max(max_source,source_error)
            phase,amplitude,alpha=selected_packet(tau,src.xi,nu)
            predicted=amplitude*mp.exp(N*phase)/mp.sqrt(N)
            error=N*abs(exact/predicted-1)
            assert error<30,(N,kind,tau,nu,error)
            max_error=max(max_error,error)
            row=dict(N=N,j=j,tau=str(tau),nu=str(nu),N_times_relative_error=float(error))
            if kind=='fold':
                a,b,r,ss=transport(tau,src.xi,nu,alpha)
                an=mp.diff(lambda v:src.determinant(tau,v),nu)/exact/N
                bn=mp.diff(lambda v:src.determinant(v,nu),tau)/exact/N
                errors=[N*N*abs(an-a-r/N),N*N*abs(bn-b-ss/N)]
                assert max(errors)<100
                max_gradient=max(max_gradient,*errors);gradients+=2
                row['N_squared_gradient_remainders']=[float(v) for v in errors]
            rows.append(row)
    return dict(precision_digits=mp.mp.dps,
                outside_central_actual_amplitude_cases=len(rows),
                independent_literal_source_comparisons=len(rows),
                actual_subprincipal_gradient_checks=gradients,
                maximum_source_relative_error=mp.nstr(max_source,35),
                maximum_N_times_relative_error=float(max_error),
                maximum_N_squared_gradient_remainder=float(max_gradient),cases=rows)


if __name__=='__main__':
    result=dict(status='PASS',symbolic=symbolic_cones(),
                exact_actual_source_cone_determinants=exact_source_checks(),
                finite=finite_boundary_and_adapters(),amplitude=full_physical_amplitudes(),
                scope=('Actual ordinary joint packet on fixed full strict-physical '
                       'compacts, with retained finite boundary correction and generic '
                       'offdiagonal choice. No global frame, contributing cycle or '
                       'whole-source asymptotic claim.'))
    target=Path(__file__).with_name('actual_q_hahn_full_physical_complex_packet_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    summary=dict(result);summary['amplitude']={k:v for k,v in result['amplitude'].items() if k!='cases'}
    print(json.dumps(summary,indent=2))
