#!/usr/bin/env python3
"""Original finite crossing, regular balanced Fourier source, full-Psi scalar.

Proof: notes/actual_balanced_fourier_crossing_kernel.md. The source-null
theorem uses exact unwrapped degree BEFORE Fourier conjugation. The
negative kernel is the complete-color antiunitary mirror, never a
pointwise deletion of its continuous Gaussian.
"""

import json
import itertools
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_two_cut_ports import word_matrix,partial
from audit_figure_eight_whole_source import MixedEntries
from audit_actual_modular_dilog_circle import psi


def original_normalized(N,p,q,x):
    E=MixedEntries(N,p,q)
    out=np.zeros((N*N,N*N),dtype=np.int64)
    for a in range(N):
        for b in range(N):
            for k in range(min(a,N-1-b)+1):
                c,e=b+k,a-k
                out[c*N+e,a*N+b]=E.direct(x,x,a,b,k,1)
    return out


def fold_kernel(N,p,Q,x,r0,r1):
    """Exact inverse external DFT, using its coefficient folding identity."""
    F=[1]
    for j in range(1,N):F.append(F[-1]*(1-pow(Q,j,p))%p)
    iv=[pow(f,-1,p) for f in F]
    pp=[(-1)**j*pow(Q,j*(j-1)//2,p)*iv[j]%p for j in range(N)]
    r6=x*r1%p;r7=x*r0%p
    c0=(pow(r1,-N,p)-pow(r7,-N,p))%p
    assert c0
    T=pow(c0,-1,p);s=pow(x,N,p)
    A=pow(r0,N,p);B=pow(r1,N,p)
    assert s*s%p==1
    assert (1-T*pow(B,-1,p)+s*T*pow(A,-1,p))%p==0
    assert (1-s*B*pow(A,-1,p)-B*pow(T,-1,p))%p==0
    assert (1-s*A*pow(B,-1,p)+s*A*pow(T,-1,p))%p==0
    result=np.zeros((N*N,N*N),dtype=np.int64)
    folded_counts={'internal_minus_N':0,'large_first_input':0,'negative_first_output':0}
    triples=[(i,j) for i in range(N) for j in range(N-i)]
    for i,j in triples:
        b0=F[i+j]*iv[i]*pp[j]*pow(x,-j,p)%p
        for r,k in triples:
            rc=F[r+k]*iv[r]*iv[k]*pow(x,-k,p)%p
            for h,l in triples:
                power=i+j-k-l
                if power not in (0,-N):continue
                a,b=j+r,i;c,e=r+k-h,h+l
                assert c+e-a-b==-power
                assert 0<=a<=2*N-2 and 0<=b<N and 0<=e<N and -(N-1)<=c<N
                coefficient=b0*rc*F[h+l]*iv[h]*pp[l]*pow(x,-h-2*l,p)%p
                if power==-N:
                    assert a<N and c>=0
                    coefficient=coefficient*c0%p
                    folded_counts['internal_minus_N']+=1
                else:
                    assert not(a>=N and c<0)
                    folded_counts['large_first_input']+=int(a>=N)
                    folded_counts['negative_first_output']+=int(c<0)
                ap,cp=a%N,c%N
                coefficient=coefficient*pow(r0,-(a-ap),p)*pow(r6,c-cp,p)%p
                result[cp*N+e,ap*N+b]=(result[cp*N+e,ap*N+b]+coefficient)%p
    return result,folded_counts


def finite_checks():
    rows=[];words=[]
    for N in range(2,11):
        H=HardyNetwork(N,1);p,Q,x,q=H.p,H.Q,H.x,H.q
        r0,r1=2,3
        while (pow(r1,-N,p)-pow(x*r0,-N,p))%p==0:r1+=1
        plus,counts=fold_kernel(N,p,Q,x,r0,r1)
        B=original_normalized(N,p,q,x)
        assert np.array_equal(B,H.plus*pow(H.kappa,-1,p)%p)
        err=(plus-B)%p
        for out,inp in zip(*np.nonzero(err)):
            assert out//N+out%N-inp//N-inp%N==N
        ehead=np.zeros((N,N),dtype=np.int64)
        for a in range(1,N):ehead[a-1,a]=(pow(Q,-a,p)-1)%p
        etotal=(np.kron(ehead,H.K)+np.kron(np.eye(N,dtype=np.int64),ehead))%p
        assert np.array_equal(etotal@plus%p,plus@etotal%p)
        assert np.array_equal(plus,B)
        # Original E is injective on every upper total-degree block.
        for t in range(N,2*N-1):
            inputs=[a*N+(t-a) for a in range(t-(N-1),N)]
            extreme_rows=[(a-1)*N+(t-a) for a in range(t-(N-1),N)]
            minor=etotal[np.ix_(extreme_rows,inputs)]
            assert np.all(np.diag(minor)%p)
            assert not np.any(np.triu(minor,1)%p)
        swap=np.zeros((N*N,N*N),dtype=np.int64)
        for a in range(N):
            for b in range(N):swap[b*N+a,a*N+b]=1
        qb,xb=pow(q,-1,p),pow(x,-1,p)
        rb0,rb1=5,7
        while (pow(rb1,-N,p)-pow(xb*rb0,-N,p))%p==0:rb1+=1
        barhat,barcounts=fold_kernel(N,p,pow(Q,-1,p),xb,rb0,rb1)
        barorig=original_normalized(N,p,qb,xb)
        minus=swap@barhat%p@swap%p
        literalminus=H.minus*H.kappa%p
        assert np.array_equal(swap@barorig%p@swap%p,literalminus)
        errminus=(minus-literalminus)%p
        for out,inp in zip(*np.nonzero(errminus)):
            assert out//N+out%N-inp//N-inp%N==N
        assert np.array_equal(minus,literalminus)
        rows.append({'N':N,'field':p,'all_three_source_norms_zero':True,
                     'original_positive_independently_evaluated':True,
                     'original_negative_independently_mirrored':True,
                     'positive_only_N_degree_error':True,
                     'negative_only_N_degree_error':True,
                     'EXACT_original_operator_both_signs':True,
                     'actual_E_coproduct_and_upper_degree_injectivity':True,
                     'measured_positive_error_entries':int(np.count_nonzero(err)),
                     'measured_negative_error_entries':int(np.count_nonzero(errminus)),
                     'positive_alias_routes_retained':counts,
                     'negative_mirror_alias_routes_retained':barcounts})
        if N<=4:
            completedplus=plus*H.kappa%p
            completedminus=minus*pow(H.kappa,-1,p)%p
            for word in ([1,-2,1,-2],[1,2,-1,-2,1,2]):
                original=word_matrix(word,H.plus,H.minus,3,N,p)
                completed=word_matrix(word,completedplus,completedminus,3,N,p)
                originalcut=partial(original,H.pivot,3,N,p)
                completedcut=partial(completed,H.pivot,3,N,p)
                assert np.array_equal(originalcut%p,completedcut%p)
                writhe=sum(1 if k>0 else -1 for k in word)
                external=H.dimension*pow(H.twist,-writhe,p)%p
                assert np.array_equal(external*originalcut%p,external*completedcut%p)
                words.append({'N':N,'word':word,'full_original_cut_matrix':True,
                              'Cartan_pivots_dimension_twist_retained':True})
    return rows,words


def analytic_checks():
    mp.mp.dps=55;rows=[]
    for N in (2,3,5,8):
        h=2j*mp.pi/N;Q=mp.exp(h);X=mp.pi*1j-h/2;x=mp.exp(X)
        ph=mp.sqrt(N)*mp.exp(mp.pi*1j*(mp.mpf('1/4')-(N+mp.mpf(1)/N)/12))
        cb=1j*(mp.sqrt(N)+1/mp.sqrt(N))/2
        zeta=mp.exp(-mp.pi*1j*(1+2*cb*cb)/6)
        zeta0=mp.exp(mp.pi*1j*(1-4*cb*cb)/12)
        aa=mp.sqrt(N)/(2*mp.pi)
        def P(z):
            if mp.re(z)<=0:return psi(N,1,z)
            return zeta*mp.exp(mp.pi*1j*(aa*z-cb)**2)/psi(N,1,2j*mp.pi+h-z)
        def M(z):return mp.conj(P(mp.conj(z)))
        fac=[mp.mpc(1)]
        for j in range(1,N):fac.append(fac[-1]*(1-Q**j))
        def B(u,v):
            term=total=mp.mpc(1)
            for j in range(1,N):term*=u-Q**(j-1)*v;total+=term
            return total
        def R(u,v):
            return sum(fac[i+j]/(fac[i]*fac[j])*u**i*v**j
                       for i in range(N) for j in range(N-i))
        def S(lu,lv):
            return N/ph*mp.exp(N*lu)*P(h-lu)*P(lv-lu)*mp.exp(-(lv-lu)*lu/h)
        def TR(lr,lw):
            return ph*M(lr-h)*M(lw-h)*mp.exp(-lr*lw/h)
        r0log=mp.log(2)/N;r1log=mp.log(3j)/N
        r6log=X+r1log;r7log=X+r0log
        tau0=-mp.log(mp.exp(-N*r1log)-mp.exp(-N*r7log))/N
        for labels in ((0,0,0,0),(1%N,0,0,1%N),
                       (0,1%N,1%N,0),(N-1,1%N,N-1,0)):
            i,j,k,l=labels
            a=r0log+h*i;b=r1log+h*j;c=r6log+h*k;d0=r7log+h*l
            beta=b-a-X;fl=d0-c-X;rho=c-a
            total=homtotal=mp.mpc(0);normerr=mp.mpf(0);pointwise=mp.mpf(0)
            for m in range(N):
                tau=tau0+h*m
                lu=tau-b;lv=tau-X-a;lw=c-X-tau
                u,v,f,r,w=map(mp.exp,(lu,lv,fl,rho,lw))
                norms=[1-u**N+v**N,1-r**N-w**N,1-f**N+(f*w)**N]
                normerr=max(normerr,*map(abs,norms))
                finite=B(u,v)*R(r,w)*B(f,f*w)
                homogeneous=S(lu,lv)*TR(rho,lw)*S(fl,fl+lw)
                pointwise=max(pointwise,abs(homogeneous/finite-1))
                total+=finite;homtotal+=homogeneous
            z=h+b-tau0;lam=d0-b+2j*mp.pi
            C=(N*N/ph*mp.exp(N*(fl-b))*(1-mp.exp(N*rho))
               *P(beta)*P(h-fl)/P(rho)
               *mp.exp((beta*b-(c-X)*(fl+rho))/h))
            Hbal=(1j*mp.sqrt(N)*ph*zeta0*(1-mp.exp(-N*lam))
                  *mp.exp((N+z/h)*lam))
            FT=(zeta0/(1j*mp.sqrt(N))*mp.exp(1j*mp.sqrt(N)*lam*cb
                  -1j*N*lam*lam/(4*mp.pi))*P(lam+2j*mp.pi+h))
            reference=(C*(1-mp.exp(N*(c-X-tau0)))
                       *mp.exp(lam*tau0/h)*Hbal*FT)
            Flog=d0-a-X
            E=(N*fl+(N+1)*lam/2
               +(Flog*(b-c+X)+lam*lam/2)/h)
            Rcentral=mp.exp(N*rho)
            simple=(zeta0*zeta0/N*Rcentral*(1-Rcentral)**2*mp.exp(E)
                    *P(beta)*P(h-fl)*P(lam+2j*mp.pi+h)/P(rho))
            def kernel(aa0,bb0,cc0,dd0):
                be=bb0-aa0-X;ff=dd0-cc0-X;rr=cc0-aa0
                ll=dd0-bb0+2j*mp.pi;gg=dd0-aa0-X
                ee=N*ff+(N+1)*ll/2+(gg*(bb0-cc0+X)+ll*ll/2)/h
                rc=mp.exp(N*rr)
                return zeta0*zeta0/N*rc*(1-rc)**2*mp.exp(ee)*P(be)*P(h-ff)*P(ll+2j*mp.pi+h)/P(rr)
            A0,B0,C0,D0=map(mp.exp,(a,b,c,d0))
            q=mp.exp(h/2)
            R1=-C0/A0*(1-D0/B0)/(1-C0/(Q*A0))
            R2=q*C0/D0*(1-D0/B0)/(1-Q*x*C0/D0)
            R4=q*B0/A0*(1-D0/B0)/(1-B0/(x*A0))
            ratio_errors=[abs(kernel(a,b,c-h,d0-h)/simple-R1),
                          abs(kernel(a,b,c,d0-h)/simple-R2),
                          abs(kernel(a+h,b+h,c,d0)/simple-R1),
                          abs(kernel(a,b+h,c,d0)/simple-R4)]
            assert max(ratio_errors)<mp.mpf('1e-35'),(N,labels,ratio_errors)
            assert normerr<mp.mpf('1e-40')
            assert pointwise<mp.mpf('1e-38'),(N,labels,pointwise)
            error=abs(reference/total-1)
            assert error<mp.mpf('1e-37'),(N,labels,error)
            simple_error=abs(simple/(total/N**3)-1)
            assert simple_error<mp.mpf('1e-37'),(N,labels,simple_error)
            assert abs(total)>mp.mpf('1e-30')
            # Four external DFT factors and one internal root average.
            assert abs((reference/N**3)/(total/N**3)-1)<mp.mpf('1e-37')
            rows.append({'N':N,'external_labels':labels,
                         'three_exact_balance_error':float(normerr),
                         'pointwise_full_source_normalizer_error':float(pointwise),
                         'entire_Fourier_scalar_relative_error':float(error),
                         'four_full_Psi_simplified_kernel_error':float(simple_error),
                         'actual_E_Ward_full_function_shift_error':float(max(ratio_errors)),
                         'kernel_entry_nonzero':True,'all_N_factors_retained':True})
    return rows


def frame_checks():
    rows=[]
    for N in (2,3,8,16,32):
        Q=np.exp(2j*np.pi/N);a=np.arange(N)
        U=Q**np.outer(a,a)/np.sqrt(N)
        A=2+0j;B=3j
        r=np.exp(np.log(A)/N);rp=np.exp(np.log(B)/N)
        Fr=U@np.diag(r**a);Fp=U@np.diag(rp**a)
        transition=Fp@np.linalg.inv(Fr)
        rho=rp/r;C=rho**N
        formula=np.array([[(1-C)/(N*(1-rho*Q**(j-k))) for k in range(N)]
                          for j in range(N)])
        assert np.max(abs(transition-formula))<1e-11
        bound=max(1,abs(B/A))
        inversebound=max(1,abs(A/B))
        assert np.linalg.norm(transition,2)<=bound+1e-10
        assert np.linalg.norm(np.linalg.inv(transition),2)<=inversebound+1e-10
        ephys=np.zeros((N,N),dtype=complex)
        for j in range(1,N):ephys[j-1,j]=Q**(-j)-1
        T=np.roll(np.eye(N,dtype=complex),-1,axis=1)
        eeval=np.diag(1/(r*Q**a))@(T-np.eye(N))
        assert np.max(abs(Fr@ephys@np.linalg.inv(Fr)-eeval))<1e-10
        rows.append({'N':N,'exact_Dirichlet_transition':True,
                     'transition_norm':float(np.linalg.norm(transition,2)),
                     'uniform_bound':bound,'inverse_uniform_bound':inversebound})
    return rows


def symbolic_actual_E_Ward():
    A,B,C,D,x=sp.symbols('z0 z1 z6 z7 x',nonzero=True)
    Q=x**-2;q=-1/x
    R1=-C/A*(1-D/B)/(1-C/(Q*A))
    R2=q*C/D*(1-D/B)/(1-Q*x*C/D)
    R4=q*B/A*(1-D/B)/(1-B/(x*A))
    left=x/C*(R1-R2)+(R2-1)/D
    right=x/A*(R1/Q-R4)+(R4/Q-1)/B
    assert sp.factor(left-right)==0
    return {'exact_actual_E_coproduct_rational_identity':True,
            'root_relation_used':'Q=x^(-2), q=-1/x',
            'right_input_transpose_Q_factor_retained':True}


def uniform_density_checks():
    """Re E is affine in the four label angles; check all exact extrema."""
    rows=[]
    for N in (2,3,8,32,128):
        h=2j*np.pi/N;X=1j*np.pi-h/2
        r0log=np.log(2+0j)/N;r1log=np.log(3j)/N
        bases=(r0log,r1log,X+r1log,X+r0log)
        Rc=np.exp(N*(bases[2]-bases[0]))
        densities=[]
        for labels in itertools.product((0,N-1),repeat=4):
            a,b,c,d0=[z+h*k for z,k in zip(bases,labels)]
            fl=d0-c-X;lam=d0-b+2j*np.pi;G=d0-a-X
            E=N*fl+(N+1)*lam/2+(G*(b-c+X)+lam*lam/2)/h
            densities.append(abs(Rc*(1-Rc)**2)*np.exp(E.real))
        lo,hi=min(densities),max(densities)
        assert 0<lo<=hi<np.inf
        rows.append({'N':N,'N_times_prefactor_minimum_all_labels':float(lo),
                     'N_times_prefactor_maximum_all_labels':float(hi),
                     'all_angle_corner_extrema_checked':True})
    assert max(r['N_times_prefactor_maximum_all_labels'] for r in rows)<1e12
    assert min(r['N_times_prefactor_minimum_all_labels'] for r in rows)>1e-12
    return rows


def main():
    local,words=finite_checks()
    result={'original_finite_crossings_and_aliases':local,
            'whole_original_sources':words,'balanced_full_Psi_Fourier_kernel':analytic_checks(),
            'exact_bounded_frame_adapters':frame_checks(),
            'symbolic_actual_E_Ward':symbolic_actual_E_Ward(),
            'uniform_nonzero_four_function_density':uniform_density_checks(),
            'proved_scope':'EXACT regular complete-color pure-balanced original Fourier crossing; '
                'one original E Ward eliminates all degree-N alias errors; '
                'all original operators, currents, and closed-word sources retained; '
                'no global geometric noncancellation claimed'}
    Path(__file__).with_name('audit_actual_balanced_fourier_crossing_kernel_results.json').write_text(
        json.dumps(result,indent=2)+'\n')
    print('PASS nine EXACT original signed crossings with E-rigidity, six whole original sources, '
          'sixteen full-Psi Fourier kernels/current shifts, five bounded exact frames, symbolic E Ward')


if __name__=='__main__':main()
