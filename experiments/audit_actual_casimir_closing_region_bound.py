#!/usr/bin/env python3
"""Structural audits for the actual all-degree spectral closing region.

The uniform counting/determinant estimates are proved in the note. Numerical
rates and conservative inequalities below are diagnostics, not substitutes.
"""
import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_q_hahn_physical_generic_jet_bound import matrix


def blocks(t):
    out=[];middle=t//2;start=0;step=1
    while start<middle:
        end=min(middle,start+step);out.append((start,end))
        start=end;step*=2
    end=t;step=1
    while end>middle:
        start=max(middle,end-step);out.append((start,end))
        end=start;step*=2
    return sorted(out)


def exact_dyadic_comparison():
    count=dict(exact_dyadic_partitions=0,exact_deleted_spring_matrices=0,
               block_conductance_scale_checks=0)
    for t in range(1,129):
        pieces=blocks(t)
        assert [r for lo,hi in pieces for r in range(lo,hi)]==list(range(t))
        assert len(pieces)<=2*(t.bit_length()+1)
        a=[16*min(r+1,t-r)**2 for r in range(t)]
        L=[[0]*t for _ in range(t)];B=[[0]*t for _ in range(t)]
        removed=[[0]*t for _ in range(t)]
        for r in range(t):
            L[r][r]+=a[r]
            if r+1<t:
                L[r+1][r+1]+=a[r]
                L[r][r+1]-=a[r];L[r+1][r]-=a[r]
        kept=set()
        for lo,hi in pieces:
            ell=hi-lo
            for r in range(lo,hi-1):
                assert min(r+1,t-r)>=ell
                assert a[r]>=16*ell**2
                kept.add(r)
                B[r][r]+=a[r];B[r+1][r+1]+=a[r]
                B[r][r+1]-=a[r];B[r+1][r]-=a[r]
                count['block_conductance_scale_checks']+=1
        for r in range(t):
            if r in kept:continue
            removed[r][r]+=a[r]
            if r+1<t:
                removed[r+1][r+1]+=a[r]
                removed[r][r+1]-=a[r];removed[r+1][r]-=a[r]
        assert all(L[i][j]-B[i][j]==removed[i][j]
                   for i in range(t) for j in range(t))
        count['exact_dyadic_partitions']+=1
        count['exact_deleted_spring_matrices']+=1
    return count


def continuant(diagonal,off,m):
    prev=mp.mpc(1);older=mp.mpc(0)
    for r in range(m):
        prev,older=diagonal[r]*prev-(off[r-1]**2*older if r else 0),prev
    return prev


def physical_determinants():
    counts=dict(universal_conductance_bounds=0,all_prefix_congruences=0,
                positive_prefix_determinant_comparisons=0,
                original_all_entry_Green_comparisons=0,
                exact_telescoped_products=0,characteristic_halfplane_bounds=0)
    for N in range(3,14):
        theta=mp.pi/N;q=mp.exp(1j*theta);lam0=2*mp.cos(theta)
        for t in range(N):
            di,up,lo=matrix(N,q,t)
            J=mp.diag(di)
            for r in range(t):J[r,r+1]=up[r];J[r+1,r]=lo[r]
            a=[4*mp.sin((t-r)*theta)*mp.sin((r+1)*theta) for r in range(t)]
            for r in range(t):
                assert a[r]>=16*mp.mpf(min(r+1,t-r))**2/N**2-mp.mpf('1e-60')
                counts['universal_conductance_bounds']+=1
            Ldiag=[a[r]+(a[r-1] if r else 0) for r in range(t)]
            for z in (mp.mpc(2),mp.mpc('2.02','.03'),mp.mpc(2,'.04')):
                R=(z*mp.eye(t+1)-J)**-1
                chi=mp.fprod(z-2*mp.cos((2*r+1)*theta) for r in range(t+1))
                chi2=mp.fprod(2-2*mp.cos((2*r+1)*theta) for r in range(t+1))
                assert abs(chi)>=chi2-mp.mpf('1e-60')
                counts['characteristic_halfplane_bounds']+=1
                prefix=[mp.mpc(1)];positive=[mp.mpf(1)];products=[mp.mpf(1)]
                s=abs(z-lam0)
                for m in range(1,t+1):
                    delta=continuant([di[r]-z for r in range(t)],up,m)
                    v=[q**(t-2*r) for r in range(m)]
                    rhs=continuant([Ldiag[r]+(z-lam0)*v[r] for r in range(m)],
                                   [-x for x in a],m)
                    Fdet=mp.fprod((-1/q)**r for r in range(m))
                    assert abs(Fdet**2*delta-(-q**(-t))**m*rhs)<mp.mpf('1e-55')*max(1,abs(rhs))
                    pos=mp.re(continuant([Ldiag[r]+s for r in range(m)],a,m))
                    product=mp.fprod(a[:m])
                    assert abs(delta)<=pos+mp.mpf('1e-55')*max(1,pos)
                    prefix.append(delta);positive.append(pos/product);products.append(product)
                    counts['all_prefix_congruences']+=1
                    counts['positive_prefix_determinant_comparisons']+=1
                sf2=mp.fprod(a)
                assert chi2>=4*sf2/N**2-mp.mpf('1e-55')*max(1,sf2)
                for u in range(t+1):
                    for v in range(u,t+1):
                        middle=mp.fprod(a[u:v])
                        assert abs(products[u]*products[t-v]*middle-sf2)<mp.mpf('1e-55')*max(1,sf2)
                        bound=mp.mpf(N)**2/4*positive[u]*positive[t-v]
                        assert abs(R[u,v])<=bound+mp.mpf('1e-50')*max(1,bound)
                        counts['exact_telescoped_products']+=1
                        counts['original_all_entry_Green_comparisons']+=1
    return counts


def counting_diagnostics():
    counts=dict(dyadic_spectral_comparisons=0,uniform_counting_diagnostics=0,
                all_prefix_positive_determinant_diagnostics=0)
    largest_count=largest_det=0.0
    for N in (8,17,32,65):
        for t in sorted(set((1,N//3,N//2,N-2,N-1))):
            a=np.array([4*np.sin((t-r)*np.pi/N)*np.sin((r+1)*np.pi/N) for r in range(t)])
            L=np.diag(a+np.r_[0,a[:-1]])
            if t>1:L+=np.diag(-a[:-1],1)+np.diag(-a[:-1],-1)
            B=np.zeros_like(L)
            for lo,hi in blocks(t):
                for r in range(lo,hi-1):
                    B[r,r]+=a[r];B[r+1,r+1]+=a[r]
                    B[r,r+1]-=a[r];B[r+1,r]-=a[r]
            assert np.linalg.eigvalsh(L-B).min()>-1e-12
            eig=np.linalg.eigvalsh(L)
            assert eig[0]>0
            assert np.sum(1/eig)<N**3
            counts['dyadic_spectral_comparisons']+=1
            for value in np.geomspace(N**-4,16,25):
                number=np.sum(eig<=value)
                majorant=np.log(N)+N*np.sqrt(value)*np.log(2+1/value)
                largest_count=max(largest_count,float(number/majorant))
                assert number<100*majorant
                counts['uniform_counting_diagnostics']+=1
            for m in sorted(set((1,(t+1)//2,t))):
                em=np.linalg.eigvalsh(L[:m,:m])
                for s in (N**-3,N**-2,.001,.01,.1,1.):
                    value=np.sum(np.log1p(s/em))
                    majorant=N*np.sqrt(s)*np.log(2+1/s)+np.log(N)**2
                    largest_det=max(largest_det,float(value/majorant))
                    assert value<100*majorant
                    counts['all_prefix_positive_determinant_diagnostics']+=1
    return counts,dict(largest_count_over_reference=largest_count,
                       largest_logdet_over_reference=largest_det)


def generic_resolvent_jets():
    count=dict(actual_generic_first_resolvent_identities=0,
               actual_generic_second_resolvent_identities=0,
               actual_spectral_resolvent_identities=0)
    for N in (3,4,7,10):
        for t in sorted(set((0,N//2,N-1))):
            def J(h):
                di,up,lo=matrix(N,mp.exp(mp.pi*1j/N+h),t)
                out=mp.diag(di)
                for r in range(t):out[r,r+1]=up[r];out[r+1,r]=lo[r]
                return out
            z=mp.mpc('2.01','.015');J0=J(0);R=(z*mp.eye(t+1)-J0)**-1
            J1=mp.matrix(t+1);J2=mp.matrix(t+1)
            R1=mp.matrix(t+1);R2=mp.matrix(t+1)
            for u in range(t+1):
                for v in range(t+1):
                    J1[u,v]=mp.diff(lambda h:J(h)[u,v],0)
                    J2[u,v]=mp.diff(lambda h:J(h)[u,v],0,2)
                    R1[u,v]=mp.diff(lambda h:((z*mp.eye(t+1)-J(h))**-1)[u,v],0)
                    R2[u,v]=mp.diff(lambda h:((z*mp.eye(t+1)-J(h))**-1)[u,v],0,2)
            assert mp.norm(R1-R*J1*R)<mp.mpf('1e-50')*max(1,mp.norm(R1))
            assert mp.norm(R2-R*J2*R-2*R*J1*R*J1*R)<mp.mpf('1e-50')*max(1,mp.norm(R2))
            count['actual_generic_first_resolvent_identities']+=1
            count['actual_generic_second_resolvent_identities']+=1
            for u,v in ((0,t),(t//2,t//2)):
                derivative=mp.diff(lambda zz:((zz*mp.eye(t+1)-J0)**-1)[u,v],z)
                assert abs(derivative+(R*R)[u,v])<mp.mpf('1e-50')*max(1,abs(derivative))
                count['actual_spectral_resolvent_identities']+=1
    return count


def angular_characteristic_checks():
    counts=dict(angular_node_distance_bounds=0,angular_characteristic_product_bounds=0,
                angular_small_node_and_tail_diagnostics=0)
    largest_small=largest_tail=mp.mpf(0)
    for N in (3,4,7,16,31,64,129):
        xs=[4*mp.sin((h+mp.mpf('.5'))*mp.pi/N)**2 for h in range(N)]
        for h,x in enumerate(xs):
            v=min(h+mp.mpf('.5'),N-h-mp.mpf('.5'))
            assert 16*v*v/N**2<=x+mp.mpf('1e-65')
            assert x<=4*mp.pi**2*v*v/N**2+mp.mpf('1e-65')
            counts['angular_node_distance_bounds']+=1
        for rho in (mp.mpf(N)**-3,mp.mpf(N)**-2,mp.mpf('.001'),mp.mpf('.03'),mp.mpf('.2')):
            scale=N*mp.sqrt(rho)+1
            small=sum(x<=2*rho for x in xs)
            tail=mp.fsum(rho/x for x in xs if x>2*rho)
            largest_small=max(largest_small,small/scale)
            largest_tail=max(largest_tail,tail/scale)
            assert small<=10*scale and tail<=10*scale
            counts['angular_small_node_and_tail_diagnostics']+=1
            for gamma in (mp.mpf('.1'),mp.mpf('.35'),mp.pi/4):
                for phi in (0,mp.pi/2,-mp.pi/2,mp.pi-gamma,-mp.pi+gamma):
                    for t in sorted(set((0,N//3,N//2,N-1))):
                        actual=mp.fsum(mp.log(abs(1+rho*mp.exp(1j*phi)/x)) for x in xs[:t+1])
                        lower=mp.fsum(mp.log(mp.sin(gamma)) if x<=2*rho else -2*rho/x for x in xs[:t+1])
                        assert actual>=lower-mp.mpf('1e-60')
                        counts['angular_characteristic_product_bounds']+=1
    return counts,dict(largest_small_node_count_over_scale=float(largest_small),
                       largest_angular_tail_over_scale=float(largest_tail))


def main():
    mp.mp.dps=80
    counts=exact_dyadic_comparison()
    counts.update(physical_determinants())
    diagnostics,values=counting_diagnostics();counts.update(diagnostics)
    counts.update(generic_resolvent_jets())
    angular,angular_values=angular_characteristic_checks();counts.update(angular);values.update(angular_values)
    result=dict(status='PASS',counts=counts,diagnostics=values,
                scope='Exact deleted-spring structure; actual all-prefix congruences, conductance cancellation and Green bounds; genuine first/second q-resolvent identities. Spectral-count and rate samples are diagnostics; uniform proof is in the note. No contour contribution or scalar-q-normal assertion.')
    Path(__file__).with_name('actual_casimir_closing_region_bound_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
