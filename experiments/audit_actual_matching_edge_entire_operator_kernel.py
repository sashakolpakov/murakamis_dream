#!/usr/bin/env python3
"""Phase-canceled entire source, including every actual support-zero entry."""
import json
from pathlib import Path
import mpmath as mp
from audit_high_color_first_normal_r_degree import root_field
from audit_actual_q_hahn_physical_generic_jet_bound import Jet,matrix
from audit_actual_matching_edge_polynomial_finite_propagation import source_polynomial
from audit_actual_q_hahn_joint_complex_amplitude import Source


def exact():
    entries=inside=residual=zeros=factors=parity=0
    for N in range(3,15):
        p,eta=root_field(N);q=eta*eta%p;d=N-1;ii=pow(eta,N,p)
        inv2=pow(2,-1,p);invi=pow(ii,-1,p)
        sine=lambda r:(pow(q,r,p)-pow(q,-r,p))*invi%p
        cosine=lambda r:(pow(q,r,p)+pow(q,-r,p))*inv2%p
        sf=[1]
        for r in range(1,N):sf.append(sf[-1]*sine(r)%p)
        def R(a,z,c):
            if not a:return 1
            old,new=1,(z+c*pow(cosine(1),-1,p))%p
            for n in range(1,a):
                # The factors2 in our sine cancel in the quotient.
                bn=sine(n)**2*pow(cosine(n)**2*sine(2*n-1)*sine(2*n+1)%p,-1,p)%p
                old,new=new,((z+c*pow(cosine(n)*cosine(n+1)%p,-1,p))*new
                             +bn*(cosine(n)**2-c*c)*old)%p
            return new
        for a in range(d//2+1):
            for sig in range(a):
                c=-cosine(sig+1)%p
                for r in range(sig+1):
                    assert R(a,pow(q,sig-2*r,p),c)==0;factors+=1
                if a==sig+1:
                    for z in [2,3,7]:
                        value=1
                        for r in range(sig+1):value=value*(z-pow(q,sig-2*r,p))%p
                        assert R(a,z,c)==value;factors+=1
            for z,c in [(2,3),(7,11)]:
                assert R(a,z,-c%p)==(-1)**a*R(a,-z%p,c)%p;parity+=1
        Jet.p=p;Jet.order=1;jq=Jet(q)
        for t in range(N):
            D,U,L=matrix(N,jq,t)
            for v in range(t+1):
                e=[Jet(int(r==v)) for r in range(t+1)]
                for a in range(d//2+1):
                    out,_,_=source_polynomial(N,jq,a,D,U,L,e,Jet(3))
                    for u in range(v+1):
                        h=v-u;l=t-v;sig=d-h;c=cosine(h)
                        b=sf[2*a]*pow(sf[a]**2,-1,p)%p
                        product=1
                        for r in range(a+1,d-a+1):product=product*sine(h+r)%p
                        R1=R(a,pow(q,-sig+2*u,p),c);R2=R(a,pow(q,sig-2*l,p),c)
                        value=b*b*pow(N,-1,p)*product*R1*R2%p
                        assert out[u].c[0]==value,(N,a,t,u,v)
                        entries+=1
                        if h<=a:inside+=1
                        elif h<=d-a:assert product==0;residual+=1
                        else:assert R1==R2==0;zeros+=1
    return dict(full_original_physical_entries=entries,within_band_entries=inside,
                forbidden_residual_product_zeros=residual,
                forbidden_two_determinant_zeros=zeros,
                forced_factor_and_monic_base_checks=factors,exact_chart_parities=parity)


def numerical():
    mp.mp.dps=140;values=physicalzeros=offgrid=0;error=mp.mpf(0)
    for N in (9,10,17,18,33,34):
        d=N-1;a=d//2;src=Source(N,a);th=mp.pi/N
        def poly(z,c):
            old,new=mp.mpf(1),z+c/src.cos[1]
            for n in range(1,a):
                old,new=new,(z+c/(src.cos[n]*src.cos[n+1]))*new+src.B[n]*(src.cos[n]**2-c*c)*old
            return new
        def entire(h,u,l):
            sig=d-h;c=mp.cos(th*h)
            return (src.central_beta**2/N*mp.fprod(2*mp.sin(th*(h+r)) for r in range(a+1,d-a+1))
                    *poly(mp.exp(th*1j*(-sig+2*u)),c)*poly(mp.exp(th*1j*(sig-2*l)),c))
        for delta,nu,lam in [(mp.mpc('.2','.03'),mp.mpc('.13','.02'),mp.mpc('.19','-.01')),
                             (mp.mpc('.72','.025'),mp.mpc('.07','.01'),mp.mpc('.11','-.015'))]:
            h,u,l=N*delta,N*nu,N*lam;tp=1-delta-mp.mpf(1)/N
            P=mp.fprod(2*mp.sin(mp.pi*(delta+mp.mpf(r)/N)) for r in range(1,N-a))
            P*=mp.fprod(2*mp.sin(mp.pi*(delta+mp.mpf(r)/N)) for r in range(1,a+1));P/=N
            old=(mp.exp(-mp.pi*1j*(N-1)*(lam-nu))*P
                 *mp.conj(src.direct(mp.conj(tp),mp.conj(nu)))*src.direct(tp,lam))
            new=entire(h,u,l)
            err=abs(old/new-1);assert err<mp.mpf('1e-105');error=max(error,err);values+=1
        # At a forbidden integer degree sigma<a, determinant zeros live
        # on the PHYSICAL magnetic nodes, not at arbitrary complex rows.
        sig=max(1,a//2);h=d-sig
        for u in range(sig+1):
            for l in range(sig+1):
                assert abs(entire(h,u,l))<mp.mpf('1e-110');physicalzeros+=1
        val=entire(h,mp.mpc('.25','.03'),mp.mpc('.4','-.02'))
        assert abs(val)>mp.mpf('1e-50');offgrid+=1
    return dict(precision_digits=mp.mp.dps,independent_original_finite_source_comparisons=values,
                forbidden_physical_grid_zeros=physicalzeros,nonzero_offgrid_values_at_forbidden_degree=offgrid,
                max_phase_canceled_source_relative_error=str(error))


def main():
    result=dict(status='PASS',exact=exact(),nonphysical=numerical(),
                scope='Entire finite ROOT source with all physical support zeros retained. No second-chart asymptotic, zero-free region or generic-q-normal continuation.')
    Path(__file__).with_name('actual_matching_edge_entire_operator_kernel_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
