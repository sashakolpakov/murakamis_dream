#!/usr/bin/env python3
"""Original complete-core source, shared coefficient, and contour checks.

The graph-wide asymptotic and exponential alias bounds are analytical
theorems. Finite complex-value samples below do not prove zero-freeness.
Cotangent checks retain both horizontal errors and vertical end currents.
"""
import argparse
import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_original_marked_face_coefficient import (
    Local, add, local_polynomials, morse_faces, mul, substitute,
)
from audit_general_odd_endpoint_matching_network import apply_pair
from audit_general_signed_augmented_source_volume import normalized_one_zero_polynomials
from audit_actual_q_hahn_complementary_hard_edge import matrices


def literal_sources():
    rows=[]
    fixtures=[(N,2,[1,0,2,1]) for N in (3,4,5,6)]
    fixtures.append((3,3,[1,3,0,2,4,1,3]))
    for N,k,boxes in fixtures:
        loc=Local(N);p=loc.p;d=N-1;M=d//2;chart=morse_faces(k,boxes)
        variables=[f for f in range(chart['faces']) if f not in (0,chart['v'])]
        polys={a:local_polynomials(loc,a) for a in range(M+1)}
        imag=pow(loc.eta,N,p)
        sine=[pow(imag,j,p)*pow(loc.q,-j*(j+1)//2,p)*loc.fac[j]%p for j in range(N)]
        beta=[sine[2*a]*pow(sine[a]**2,-1,p)%p for a in range(M+1)]
        signs=tuple((-1,0,1)[j%3] for j in range(len(boxes)))
        for seed in (2,11):
            clocks=[seed+2*j for j in range(len(boxes))]
            assert all(w%p for w in clocks)
            assert any(pow(w,2*N,p)!=1 for w in clocks)
            state=np.array([1],dtype=np.int64);mark=np.array([1],dtype=np.int64)
            marker=np.array([[pow(loc.x,j,p)*pow(N*N,-1,p)%p for j in range(N)] for i in range(N)],dtype=np.int64)
            for j in range(k):
                state=np.kron(state,loc.cup[0].reshape(-1))%p
                mark=np.kron(mark,(marker if j==chart['marked'] else loc.cap[0]).reshape(-1))%p
            state=state.reshape((N,)*(2*k));product={(0,)*len(variables):1}
            for slot,faces,eps,w in zip(boxes,chart['circles'],signs,clocks):
                coupon=np.zeros((N*N,N*N),dtype=np.int64);polynomial={}
                x,b,c,y=faces
                for a in range(M+1):
                    cosine=(pow(w,d-2*a,p)+pow(w,-d+2*a,p))*pow(2,-1,p)%p
                    unit=pow(loc.omega[a],eps,p)*cosine%p
                    coupon=(coupon+loc.h0[a]*unit%p*(loc.W[a][0]@loc.pi[a][0]%p))%p
                    D,P=polys[a];local={(0,)*len(variables):1}
                    for poly,ids in [(D,(x,b,y)),(D,(x,c,y)),(P,(x,y))]:
                        local=mul(local,substitute(poly,ids,variables,p),p,d)
                    ka=1 if 2*a==d else 2
                    polynomial=add(polynomial,local,p,ka*beta[a]**2*unit%p)
                product=mul(product,polynomial,p,d)
                state=apply_pair(coupon,state,slot,N,p)
            original=int(mark@state.reshape(-1)%p)
            expected=pow(N,len(boxes),p)*product.get((d,)*len(variables),0)%p
            assert original==expected,(N,k,clocks,original,expected)
            rows.append({'N':N,'width':k,'circles':len(boxes),'signs':signs,
                         'external_exponential_clocks':clocks,'field':p,
                         'literal_source':original,'coefficient_source':expected})
    return {'original_off_grid_complete_sources':len(rows),'cases':rows,
            'scope':'Actual W/pi, original cups and unrestricted marked cap; off-grid external cosine clocks are inserted in every complete-circle coupon. All labels, pivots, multiplicities and original omega phases remain.'}


def omega(N,a):
    d=N-1
    return mp.exp(mp.pi*1j/N*(mp.mpf(d*d)/2+a*(a+1)))*(-1)**a


def weighted_vector(N,rows,eps,chi,unfold=False):
    d=N-1;M=d//2;out=[mp.mpc(0)]*(M+1)
    for j in range(N if unfold else M+1):
        a=min(j,d-j)
        weight=omega(N,j)**eps
        if unfold:
            weight*=mp.exp(mp.pi*1j*(d-2*j)*chi)
        else:
            weight*=(1 if 2*j==d else 2)*mp.cos(mp.pi*(d-2*j)*chi)
        for r in range(a+1):out[r]+=weight*rows[a][a-r]
    return out


def core_profiles():
    profiles=[];worst_fourier=worst_cauchy=mp.mpf(0);entries=0
    choices=[((0,0),(mp.mpc('.012','.007'),mp.mpc('-.009','.004'))),
             ((1,-1),(mp.mpc('.009','-.006'),mp.mpc('.005','.008'))),
             ((1,1),(mp.mpc('-.011','.003'),mp.mpc('.007','-.005')))]
    for N in (9,10,17,18,33,34,65,66):
        rows=normalized_one_zero_polynomials(N);M=(N-1)//2
        for signs,chis in choices:
            vectors=[]
            for eps,chi in zip(signs,chis):
                folded=weighted_vector(N,rows,eps,chi)
                unfolded=weighted_vector(N,rows,eps,chi,True)
                scale=max(abs(v) for v in folded)
                for x,y in zip(folded,unfolded):
                    err=abs(x-y)/scale;worst_fourier=max(worst_fourier,err)
                    assert err<mp.mpf('1e-55');entries+=1
                vectors.append(folded)
            v,w=vectors
            exact=mp.fsum(x*y for x,y in zip(v,w))
            # Actual K4 marked coefficient: A(z)=sum v_r z^(d-r),
            # B(z)=sum w_r z^r. Its prescribed z^d coefficient is below.
            nodes=2*M+3
            quadrature=mp.fsum(
                mp.fsum(v[r]*mp.exp(-2j*mp.pi*j*r/nodes) for r in range(M+1))
                *mp.fsum(w[r]*mp.exp(2j*mp.pi*j*r/nodes) for r in range(M+1))
                for j in range(nodes))/nodes
            err=abs(quadrature-exact)/max(abs(exact),1);worst_cauchy=max(worst_cauchy,err)
            assert err<mp.mpf('1e-55')
            atzero=mp.fsum(x*y for x,y in zip(
                weighted_vector(N,rows,signs[0],0),weighted_vector(N,rows,signs[1],0)))
            assert abs(atzero)>0 and abs(exact)>0
            profiles.append({'N':N,'signs':signs,'chi':[str(z) for z in chis],
                             'original_core_ratio':str(exact/atzero),
                             'N_inverse_log_modulus_ratio':str(mp.log(abs(exact/atzero))/N)})
    return {'actual_shared_K4_complex_cores':len(profiles),
            'retained_phase_reflection_entries':entries,
            'exact_face_Cauchy_checks':len(profiles),
            'maximum_reflection_relative_error':str(worst_fourier),
            'maximum_Cauchy_relative_error':str(worst_cauchy),'profiles':profiles,
            'scope':'All original labels and shared coefficient are retained. Complex-value/nonzero samples are diagnostics, not a proof of a fixed zero-free neighborhood or of the asymptotic action.'}


def cotangent_functionals(N,a,shift):
    """Exact contour and all boundary terms for one literal cosine basis."""
    d=N-1;offset=mp.mpf(0) if N%2 else mp.mpf('.5')
    grid=[(mp.mpf(j)+offset)/N for j in range(-N,N+1)
          if abs((mp.mpf(j)+offset)/N)<mp.mpf('.23')]
    left=grid[0]-mp.mpf('.5')/N;right=grid[-1]+mp.mpf('.5')/N
    eta=mp.mpf('.055');freq=mp.pi*(d-2*a)
    f=lambda z:mp.cos(freq*(z+shift))
    cot=lambda z:mp.cot(mp.pi*(N*z-offset))
    integral=lambda g,lo,hi:mp.quad(g,[lo,(lo+hi)/2,hi])
    bottom=integral(lambda x:cot(x-1j*eta)*f(x-1j*eta),left,right)
    top=-integral(lambda x:cot(x+1j*eta)*f(x+1j*eta),left,right)
    vertical=1j*integral(lambda y:cot(right+1j*y)*f(right+1j*y)
                                   -cot(left+1j*y)*f(left+1j*y),-eta,eta)
    contour=N/(2j)*(bottom+top+vertical)
    horizontal_alias=N/(2j)*(
        integral(lambda x:(cot(x-1j*eta)-1j)*f(x-1j*eta),left,right)
        -integral(lambda x:(cot(x+1j*eta)+1j)*f(x+1j*eta),left,right))
    plain_closing=N/2*1j*(
        integral(lambda y:f(left+1j*y)-f(right+1j*y),-eta,0)
        +integral(lambda y:f(right+1j*y)-f(left+1j*y),0,eta))
    real=N*integral(f,left,right)
    reconstructed=real+horizontal_alias+N/(2j)*vertical+plain_closing
    exact=mp.fsum(f(z) for z in grid)
    scale=max(1,abs(exact));err=max(abs(contour-exact),abs(reconstructed-exact))/scale
    assert err<mp.mpf('1e-45'),(N,a,err)
    return exact,contour,reconstructed,err,len(grid)


def original_cotangent_checks():
    count=0;worst=mp.mpf(0);records=[]
    for N in (9,10):
        rows=normalized_one_zero_polynomials(N);M=(N-1)//2
        signs=(1,-1);shifts=(mp.mpc('.013','.007'),mp.mpc('-.011','.004'))
        vectors=[]
        for eps,shift in zip(signs,shifts):
            triples=[[mp.mpc(0)]*(M+1) for _ in range(3)]
            for a in range(M+1):
                values=cotangent_functionals(N,a,shift)
                worst=max(worst,values[3]);count+=1
                scalar=(1 if 2*a==N-1 else 2)*omega(N,a)**eps
                for r in range(a+1):
                    for k in range(3):triples[k][r]+=scalar*rows[a][a-r]*values[k]
            vectors.append(triples)
        values=[mp.fsum(x*y for x,y in zip(vectors[0][j],vectors[1][j])) for j in range(3)]
        scale=max(abs(values[0]),1)
        err=max(abs(z-values[0])/scale for z in values[1:])
        assert err<mp.mpf('1e-43');worst=max(worst,err)
        records.append({'N':N,'original_two_register_grid_period':str(values[0]),
                        'relative_contour_error':str(err)})
    return {'literal_cosine_contour_checks':count,
            'actual_two_register_core_contour_checks':len(records),
            'maximum_relative_error':str(worst),'cases':records,
            'scope':'Exact cotangent/constant-kernel calculus tested on the original finite entire K4 core in its external registers. Vertical cotangent and plain contour-closing terms are retained. This tests the multi-register contour normalization; it does not replace the analytical bound for the channel interpolant.'}


def fixed_window_angular_gap():
    checks=0;ratios=[]
    for N in (33,34,65,66,129,130):
        M=(N-1)//2
        for a in sorted({int(mp.floor(mp.mpf('.4')*N)),M}):
            Hp,Hm=matrices(N,a)
            for x,b,y in ((1.3,.8,2.1),(1.3,.8,0.),(1.3,0.,2.1)):
                X=[z for z in (x*Hm/2,b*np.eye(a),y*Hp/2) if np.linalg.norm(z)>0]
                mat=sum(X);ev,vec=np.linalg.eigh(mat)
                inv=(vec/np.sqrt(ev))@vec.conj().T;A=[inv@z@inv for z in X]
                pairs=[float(np.trace(A[j]@A[k]).real)/N for j in range(len(A)) for k in range(j+1,len(A))]
                # In 222 the two identity edges suffice; all three are
                # nevertheless positive in these actual finite samples.
                assert min(pairs)>0
                phases=[.31*(j+1)**2 for j in range(len(A))]
                B=sum(np.exp(1j*t)*z for t,z in zip(phases,A))
                gap=sum(abs(np.exp(1j*phases[j])-np.exp(1j*phases[k]))**2
                        *float(np.trace(A[j]@A[k]).real) for j in range(len(A)) for k in range(j+1,len(A)))
                sv=np.linalg.svd(B,compute_uv=False)
                assert float(np.log(sv).sum())+gap/2<1e-7*N
                ratios.extend(pairs);checks+=1
    return {'actual_fixed_window_matrix_checks':checks,
            'minimum_sampled_pair_trace_over_N':min(ratios),
            'scope':'Original matrices at a/N near0.4 and at both folds. Uniform lower bounds are proved by the fixed bulk-square/variance argument, not inferred from these samples.'}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',default='experiments/actual_complete_core_complex_packet_results.json');args=ap.parse_args()
    mp.mp.dps=75
    data={'status':'PASS','precision_digits':75,'literal_sources':literal_sources(),
          'shared_core':core_profiles(),'cotangent':original_cotangent_checks(),
          'angular':fixed_window_angular_gap(),
          'scope':'Original finite complete-image source and shared coefficient, retained reflected phases, both cotangent lattice offsets and original end currents. No ordinary-color subset, geometric reconstruction, or filled-source conclusion is tested or inferred.'}
    Path(args.output).write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))


if __name__=='__main__':main()
