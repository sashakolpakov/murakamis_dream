#!/usr/bin/env python3
"""Actual coherently summed transfer endpoints, whole source and support zeros."""
import itertools,json,math
from pathlib import Path
import numpy as np
import mpmath as mp

from audit_finite_sum_annihilator import field
from audit_figure_eight_whole_source import MixedEntries
from audit_actual_rogers_bridge_transport import crossing
from audit_actual_two_cut_ports import word_matrix,partial
from audit_exact_factorial_interpolation import factorial
from audit_actual_beta_current_connection_and_monodromy import log_full_psi


def endpoint_cases():
    rows=[]
    for N in range(2,11):
        p,gen,q=field(N);E=MixedEntries(N,p,q);Q=E.Q;d=N-1;x=-pow(q,-1,p)%p
        plus=crossing(E,x,x,1);minus=crossing(E,x,x,-1)
        g=np.array([pow(x,1-N,p)*pow(Q,-a,p)%p for a in range(N)],dtype=np.int64)
        theta=pow(x,1-N,p)
        for collar in range(d//2+1):
            grouped=np.zeros_like(plus);direct=np.zeros_like(plus)
            for a,b in itertools.product(range(N),repeat=2):
                for k in range(min(a,d-b)+1):
                    if d-k<=collar:
                        direct[(b+k)*N+a-k,a*N+b]=E.direct(x,x,a,b,k,1)
            for s in range(collar+1):
                a=d-s
                for j in range(collar-s+1):
                    for b in range(N):
                        for u in range(N):
                            grouped[u*N+j,a*N+b]=plus[u*N+j,a*N+b]
            assert np.array_equal(grouped,direct)
        for sign,R in ((1,plus),(-1,minus)):
            zero=np.zeros_like(R);top=np.zeros_like(R)
            for a,b in itertools.product(range(N),repeat=2):
                maximum=min(a,d-b) if sign>0 else min(b,d-a)
                for k in range(maximum+1):
                    u,v=(b+k,a-k) if sign>0 else (b-k,a+k)
                    value=E.direct(x,x,a,b,k,sign)
                    if not k:zero[u*N+v,a*N+b]=value
                    if k==d:top[u*N+v,a*N+b]=value
            target=np.zeros_like(top);a,b=(d,0) if sign>0 else (0,d)
            target[a*N+b,a*N+b]=N%p
            assert np.array_equal(top,target)
            fullcut=partial(R,g,2,N,p)
            expected=pow(theta,sign,p)*np.eye(N,dtype=np.int64)%p
            assert np.array_equal(fullcut,expected)
            topcut=partial(top,g,2,N,p)
            assert int(np.trace(topcut))%p==N*pow(theta,sign,p)%p
            assert int(np.trace(fullcut-topcut))%p==0
            # Keep the actual chosen cut BEFORE attaching the normalization.
            if N<=6:
                W=word_matrix([1,-2,1,-2],plus,minus,3,N,p)
                C=partial(W,g,3,N,p);K=int(C[0,0])
                assert np.array_equal(C,K*np.eye(N,dtype=np.int64)%p)
                full=int(np.trace(C@fullcut%p))*pow(N,-1,p)%p
                end=int(np.trace(C@topcut%p))*pow(N,-1,p)%p
                assert full==end==K*pow(theta,sign,p)%p
                assert int(np.trace(C@(fullcut-topcut)%p))%p==0
            if sign>0:
                zcut=partial(zero,g,2,N,p)
                gauss=sum(pow(Q,a*a,p) for a in range(N))%p
                assert int(np.trace(zcut))%p==theta*gauss%p
            rows.append({'N':N,'sign':sign,'original_top_corner_rank':1,
                         'original_Markov_source_top_equals_full':True,
                         'other_transfers_cancel_with_same_scalar_exterior':True})
    return rows


def low_normalization_packets():
    rows=[]
    for N in (3,5,7,9,11,13,15,17):
        p,gen,q=field(N);E=MixedEntries(N,p,q);Q=E.Q;d=N-1;x=-pow(q,-1,p)%p
        theta=pow(x,1-N,p);i4=pow(4,-1,N)
        gauss=sum(pow(Q,b*b,p) for b in range(N))%p
        assert gauss
        full=0
        for k in range(min(3,d)+1):
            poly=[1]
            for t in range(1,k+1):
                a=pow(Q,t,p);nxt=[0]*(len(poly)+1)
                for j,c in enumerate(poly):nxt[j]=(nxt[j]+c)%p;nxt[j+1]=(nxt[j+1]-a*c)%p
                poly=nxt
            squared=[0]*(2*k+1)
            for i,a in enumerate(poly):
                for j,b in enumerate(poly):squared[i+j]=(squared[i+j]+a*b)%p
            shift=sum(c*pow(Q,-s*s*i4,p) for s,c in enumerate(squared))%p
            inner=sum(pow(Q,b*b,p)*E.pochhammer(pow(Q,b+1,p),k)**2 for b in range(N))%p
            assert inner==gauss*shift%p
            literal=0
            for b in range(N-k):
                a=b+k;gb=theta*pow(Q,-b,p)%p
                literal=(literal+gb*E.direct(x,x,a,b,k,1))%p
            assert literal==theta*inner*pow(E.F[k],-1,p)%p
            full=(full+literal)%p
            expected=sum(sum(pow(Q,b*b,p)*E.pochhammer(pow(Q,b+1,p),j)**2
                             for b in range(N))*pow(E.F[j],-1,p) for j in range(k+1))%p
            assert full==theta*expected%p
        rows.append({'N':N,'summed_low_width':min(3,d),
                     'all_original_slice_traces_and_square_completions_exact':True})
    return rows


def sourced_normal_ward():
    rows=[]
    for N in range(2,12):
        p,gen,q=field(N);E=MixedEntries(N,p,q);Q=E.Q;d=N-1;x=-pow(q,-1,p)%p
        checks=0
        for a,b in itertools.product(range(N),repeat=2):
            r=[E.direct(x,x,a,b,k,1) if k<=min(a,d-b) else 0 for k in range(N)]
            c=x*pow(Q,-b,p)%p
            for R in range(N):
                f=r[:R+1]+[0]*(d-R+1)
                for ell in range(d+2):
                    current=(1-pow(Q,ell,p))*f[ell] if ell<len(f) else 0
                    if ell:
                        previous=f[ell-1] if ell-1<len(f) else 0
                        current-=c*(1-pow(Q,b+ell,p))*(1-pow(Q,a-ell+1,p))*previous
                    expected=0
                    if ell==R+1:
                        expected=-c*(1-pow(Q,b+R+1,p))*(1-pow(Q,a-R,p))*r[R]
                    assert (current-expected)%p==0,(N,a,b,R,ell)
                    checks+=1
        rows.append({'N':N,'literal_coefficient_level_Ward_interfaces_checked':checks,
                     'full_transfer_interface_zero':True})
    return rows


def collar_bounds():
    rows=[]
    for N in range(3,21):
        d=N-1;F=[mp.mpf(1)]
        for k in range(1,N):F.append(F[-1]*2*mp.sin(mp.pi*k/N))
        checked=0
        for k,b,j in itertools.product(range(N),repeat=3):
            if k+b>d or k+j>d:continue
            A=F[k+b]*F[k+j]/(F[k]*F[b]*F[j])
            if k<=N//2:
                assert A<=mp.mpf(N)**k/mp.factorial(k)*(1+mp.mpf('1e-65'))
                checked+=1
            r=d-k
            if r<=N//2:
                assert b<=r and j<=r
                reflected=N/F[r]*(F[r]/(F[b]*F[r-b]))*(F[r]/(F[j]*F[r-j]))
                assert abs(A/reflected-1)<mp.mpf('1e-65')
                assert A<=mp.mpf(N)**(r+1)/mp.factorial(r)*(1+mp.mpf('1e-65'))
                checked+=1
        rows.append({'N':N,'endpoint_magnitude_inequalities':checked,
                     'all_support_and_reflection_indices_valid':True})
    return rows


def extended_factorial(N,z):
    # Holomorphic extension to Re z>-1, by the proved exact shift.
    if mp.re(z)<N:return factorial(N,z)
    count=int(mp.floor(mp.re(z)-N))+1;base=z-count
    return factorial(N,base)*mp.fprod(1-mp.exp(2j*mp.pi*(base+r)/N)
                                    for r in range(1,count+1))


def inverse_factorial(N,z):
    # Holomorphic extension to Re z<N, including negative-integer zeros.
    if mp.re(z)>-1:return 1/factorial(N,z)
    count=int(mp.floor(-1-mp.re(z)))+1;base=z+count
    return mp.fprod(1-mp.exp(2j*mp.pi*(z+r)/N) for r in range(1,count+1))/factorial(N,base)


def support_zeros():
    rows=[]
    for N in (3,5,7):
        Q=mp.exp(2j*mp.pi/N);F=[mp.mpc(1)]
        for k in range(1,N):F.append(F[-1]*(1-Q**k))
        worst=mp.mpf(0);checks=0
        for a,b in ((0,N-1),(N-1,0),(N//2,N//2)):
            for k in range(N):
                value=extended_factorial(N,b+k)*F[a]*inverse_factorial(N,k)*inverse_factorial(N,a-k)/F[b]
                allowed=k<=a and b+k<N
                expected=F[b+k]*F[a]/(F[k]*F[b]*F[a-k]) if allowed else 0
                error=abs(value-expected)/max(1,abs(expected));worst=max(worst,error)
                assert error<mp.mpf('1e-60');checks+=1
            # Actual points on the half-integer contour, not an artificial
            # replacement of support zeros at forbidden integer states.
            for z in (mp.mpc('-.5','.3'),mp.mpc(N-mp.mpf('.5'),'.3')):
                v=extended_factorial(N,b+z)*inverse_factorial(N,z)*inverse_factorial(N,a-z)
                assert mp.isfinite(v)
        rows.append({'N':N,'literal_allowed_and_forbidden_integer_checks':checks,
                     'max_relative_error':float(worst),'half_integer_vertical_edges_regular':True})
    return rows


def factorial_full_psi_comparison():
    rows=[]
    for N in (3,5,8):
        h=2j*mp.pi/N
        phi=mp.sqrt(N)*mp.exp(mp.pi*1j*(mp.mpf(1)/4-(N+mp.mpf(1)/N)/12))
        worst=mp.mpf(0)
        for z in (mp.mpc('.3','.4'),mp.mpc('1.2','-.7'),mp.mpc(N/2,'.3')):
            expected=phi*mp.exp(-log_full_psi(N,h*(z+1)))
            err=abs(factorial(N,z)/expected-1);worst=max(worst,err)
            assert err<mp.mpf('1e-60')
        a=b=N//3;z=mp.mpc('.3','.4')
        ratio=factorial(N,b+z)*factorial(N,a)/(factorial(N,z)*factorial(N,b)*factorial(N,a-z))
        logpsi=(log_full_psi(N,h*(b+1))+log_full_psi(N,h*(z+1))
                +log_full_psi(N,h*(a-z+1))-log_full_psi(N,h*(a+1))
                -log_full_psi(N,h*(b+z+1)))
        assert abs(ratio/(mp.exp(logpsi)/phi)-1)<mp.mpf('1e-60')
        rows.append({'N':N,'independent_Barnes_full_Psi_relative_error':float(worst),
                     'literal_five_function_crossing_factor_checked':True})
    return rows


def simple_negative_seam():
    rows=[];delta=mp.mpf('1e-18')
    for N,a,b,m in ((9,3,3,2),(13,5,5,3)):
        h=2j*mp.pi/N;x=-mp.exp(-mp.pi*1j/N);t=mp.mpc('.8','.2')
        logct=mp.log(x)-h*b+mp.log(t)
        Fa,Fb=factorial(N,a),factorial(N,b)
        def kernel(z):
            return (mp.exp(z*logct)*extended_factorial(N,b+z)/Fb
                    *Fa*inverse_factorial(N,a-z)*inverse_factorial(N,z))
        for j in range(1,m+1):
            assert kernel(-j)==0
            left=mp.pi*mp.cot(mp.pi*(-j-delta))*kernel(-j-delta)
            right=mp.pi*mp.cot(mp.pi*(-j+delta))*kernel(-j+delta)
            assert abs(left-right)/max(1,abs(left),abs(right))<mp.mpf('1e-14')
        samples=[]
        for v in (-1,0,1):
            z=-mp.mpf(m)-mp.mpf('.5')+1j*v
            value=mp.pi*mp.cot(mp.pi*z)*kernel(z)
            assert mp.isfinite(value)
            samples.append(float(abs(value)))
        rows.append({'N':N,'physical_inputs':[a,b],'new_negative_cot_poles_canceled':m,
                     'regular_density_limits_agree':True,'finite_height_far_edge_samples':samples,
                     'contour_equality_uses_written_residue_proof':True})
    return rows


def main():
    mp.mp.dps=85
    data={'status':'PASS','actual_signed_Markov_endpoint_sources':endpoint_cases(),
          'summed_low_normalization_packets':low_normalization_packets(),
          'sourced_normal_Ward_interfaces':sourced_normal_ward(),
          'normal_collar_bounds':collar_bounds(),'closed_contour_support':support_zeros(),
          'exact_factorial_full_Psi_normalization':factorial_full_psi_comparison(),
          'simple_negative_side_cot_filling':simple_negative_seam(),
          'scope':'Original total physical transfer only. Whole all-corner subexponential bound; mixed corners and bridge overclock endpoints are not assigned zero rate.'}
    Path(__file__).with_name('actual_total_transfer_endpoint_packets_results.json').write_text(json.dumps(data,indent=2)+'\n')
    print('PASS original total-transfer collar bounds, exact Markov endpoint normalization and full-box support zeros')


if __name__=='__main__':main()
