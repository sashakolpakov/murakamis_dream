#!/usr/bin/env python3
"""Exact H-insertion carries, original supported periods, and Gamma marks.

The comparisons use actual root channels and the moving-P factorial.
Numerical bounds are diagnostics of the written uniform proof, not a
test of global contour deformation or of a relative-period coefficient.
"""
import argparse
import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

from audit_actual_explicit_root_channel_normal_adapter import source_channel
from audit_actual_braided_residual_framing_current import fixture, rectangular_fixture
from audit_actual_nc_morse_graph_first_normal_source_reduction import const
from audit_high_color_first_normal_r_degree import root_field
from audit_actual_moving_period_factorial_normals import log_factorial


def exact_clock_algebra():
    nodes = transports = descents = carries = 0
    for N in range(2, 25):
        p, eta = root_field(N)
        q = eta*eta % p
        Q = q*q % p
        inv = lambda x: pow(int(x) % p, -1, p)
        den = [0]+[inv(1-pow(Q, -r, p)) for r in range(1, N)]
        mean = 2*sum(r*den[r] for r in range(1, N)) % p
        H = [0]
        for r in range(1, N):
            H.append((H[-1]+2*N*inv(1-pow(Q,r,p))) % p)
        tau = 7
        assert tau % p
        Pprime = -2*N*N*inv(tau) % p
        def S(U):
            return sum(pow(U,r,p)*den[r] for r in range(1,N)) % p
        def poly(U):
            return (mean-2*sum(r*pow(U,r,p)*den[r] for r in range(1,N))) % p
        def alg(x,U):
            return (2*N*(x-(N-1)*inv(2)+S(U))*inv(1-pow(U,N,p))
                    +mean+2*N*inv(tau)) % p
        for r in range(N):
            U = pow(Q,r,p)
            assert S(U) == ((N-1)*inv(2)-r) % p
            # The actual removable limit uses d/dx, not d/dU alone.
            Bprime = (1+tau*inv(N)*sum(j*pow(U,j,p)*den[j]
                                     for j in range(1,N))) % p
            removable = (-2*N*inv(tau)*Bprime+mean+2*N*inv(tau)) % p
            assert removable == poly(U) == H[r]
            nodes += 1
            for m in range(-2,3):
                ell = m*N+r
                B0 = (ell-(N-1)*inv(2)+S(U)) % p
                residue = -2*N*inv(tau)*B0 % p
                finite = (N*B0-2*N*inv(tau)*Bprime+mean+2*N*inv(tau)) % p
                literal_finite = (finite+tau*residue) % p
                assert residue == m*Pprime % p
                assert finite == (H[r]+m*N*N) % p
                assert literal_finite == (H[r]-m*N*N) % p
                carries += 1
        for U in range(2,12):
            Y = pow(U,N,p)
            if Y == 1:
                continue
            x = 13
            z = Q*U % p
            assert (alg(x+1,z)-alg(x,U)) % p == 2*N*inv(1-z) % p
            assert (alg(x+N,U)-alg(x,U)) % p == 2*N*N*inv(1-Y) % p
            assert (poly(z)-poly(U)) % p == (
                2*N*Y*inv(1-z)-2*z*(1-Y)*inv(1-z)**2) % p
            assert (Y*(alg(x+1,z)-alg(x,U))) % p == 2*N*Y*inv(1-z) % p
            transports += 4
            # Explicit cyclic descent, including its nonzero mean.
            b = lambda V: 2*N*inv(1-Q*V) % p
            avg = sum(b(pow(Q,j,p)*U % p) for j in range(N))*inv(N) % p
            R = sum(j*b(pow(Q,j,p)*U % p) for j in range(N))*inv(N) % p
            shiftedR = sum(j*b(pow(Q,j+1,p)*U % p) for j in range(N))*inv(N) % p
            assert avg == 2*N*inv(1-Y) % p
            assert R == 2*N*((N-1)*inv(2)+S(U))*inv(1-Y) % p
            assert (shiftedR-R) % p == (b(U)-avg) % p
            descents += 1
    return dict(exact_removable_physical_nodes=nodes,
                exact_unit_and_level_transports=transports,
                exact_cyclic_descents=descents,
                exact_general_carry_Laurent_coefficients=carries)


def symbolic_residues():
    y, A, tau, N, R, B, s0, s1, w0 = sp.symbols(
        'y A tau N R B s0 s1 w0', nonzero=True)
    complement = s0+s1*y
    # Primitive coordinate retained: head=a+A*y.
    rep = R/(A*y)+B
    res = sp.residue((1/y-sp.pi**2*y/3)*rep*complement,y,0)
    assert sp.cancel(res-B*s0-R*s1/A)==0
    regular = sp.residue(w0*rep*complement,y,0)
    assert sp.cancel(regular-w0*R*s0/A)==0
    Pprime = -2*N*N/tau
    inverse = -1/(tau*y)+sp.Rational(1,2)-tau*y/12
    gauge = inverse-1
    for density, sign in ((inverse,1),(gauge,-1)):
        got = sp.residue(2*N*N*(1/y-sp.pi**2*y/3)*density*complement,y,0)
        assert sp.cancel(got-(Pprime*s1+sign*N*N*s0))==0
    # Every carry, and both null differences from the finite polynomial.
    H = sp.symbols('H')
    count=0
    for m in range(-2,3):
        for lit in (False,True):
            rho=m*Pprime
            finite=H+(-1 if lit else 1)*m*N*N
            insertion=rho/y+finite
            got=sp.residue((1/y-sp.pi**2*y/3)*insertion*complement,y,0)
            assert sp.cancel(got-(finite*s0+rho*s1))==0
            difference=sp.residue((1/y-sp.pi**2*y/3)*(H-insertion)*complement,y,0)
            expected=(-m*Pprime*s1+(1 if lit else -1)*m*N*N*s0)
            assert sp.cancel(difference-expected)==0
            count+=2
    return dict(primitive_and_nonlattice_weight_residues=2,
                original_cotangent_transport_anomalies=2,
                general_carry_and_null_difference_residues=count)


def actual_periods():
    cases=insertions=weighted_currents=0
    for N in (2,3,4):
        for kind in ('braid','complete','rectangular'):
            data=rectangular_fixture(N) if kind=='rectangular' else fixture(N,2,kind)
            p,q,g,A,B,U,Ui,ow,iw=data
            Q=q*q % p
            inv=lambda x:pow(int(x)%p,-1,p)
            hs=[0]
            for r in range(1,N):hs.append((hs[-1]+2*N*inv(1-pow(Q,r,p)))%p)
            mean=2*sum(r*inv(1-pow(Q,-r,p)) for r in range(1,N))%p
            poly=[(mean-2*sum(r*pow(Q,r*l,p)*inv(1-pow(Q,-r,p))
                              for r in range(1,N)))%p for l in range(N)]
            assert poly==hs
            C=source_channel(data)
            I=np.eye(N,dtype=np.int64)
            H=np.diag(hs).astype(np.int64)
            HP=np.diag(poly).astype(np.int64)
            z=int(C(const(I))[0][0,0])
            t=2*inv(3)%p
            beta=np.array([int(sp.binomial(N-1,a))*pow(t,a,p)*pow(1-t,N-1-a,p)%p
                           for a in range(N)],dtype=np.int64)
            e=np.outer(beta,np.ones(N,dtype=np.int64))
            for momentum in (1,2,3):
                X=np.array([[pow(momentum,r-s,p)*inv(N)%p for s in range(N)]
                            for r in range(N)],dtype=np.int64)
                for left,right in ((H,HP),(X@H%p,X@HP%p)):
                    actual=C(const(left))[0]
                    replaced=C(const(right))[0]
                    assert np.array_equal(actual,replaced)
                    assert int(np.trace(e@actual)%p)==int(np.trace(e@replaced)%p)
                    insertions+=1
            lhs=0
            for l in range(N-1):
                forward=np.zeros((N,N),dtype=np.int64);forward[l+1,l]=1
                backward=forward.T
                raw=C(const((forward-q*backward)%p))[0]
                lhs=(lhs+int(np.trace(e@raw)))%p
            rhs=z*(1-q-int(beta[-1])+q*int(beta[0]))%p
            assert lhs==rhs
            cases+=1;weighted_currents+=1
    return dict(actual_root_sources=cases,
                actual_supported_root_insertion_periods=insertions,
                actual_H_weighted_Ward_identities=weighted_currents)


def gamma_comparisons():
    mp.mp.dps=75
    worst=mp.mpf(0);largest_bound=mp.mpf(0);largest_top=mp.mpf(0)
    cases=top_count=characters=0
    for N in (12,25,50):
        d=N-1;Q=mp.exp(2*mp.pi*1j/N);Pprime=-N*N/(mp.pi*1j)
        lf=lambda P,z:log_factorial(P,z,N,count=80,order=30)
        g_d=mp.diff(lambda P:lf(P,d),N)*Pprime
        fprime_d=mp.diff(lambda z:lf(N,z),mp.mpf(d))
        mean=2*mp.fsum(k/(1-Q**(-k)) for k in range(1,N))
        for kappa in (mp.mpc('1.1','.4'),mp.mpc('-.7','.9')):
            for direction in (1,-1):
                U=kappa*N**(2*direction)
                arg=mp.arg(U)
                if arg<0:arg+=2*mp.pi
                x=N*(mp.log(abs(U))+1j*arg)/(2*mp.pi*1j)
                g_x=mp.diff(lambda P:lf(P,x),N)*Pprime
                g_dx=mp.diff(lambda P:lf(P,d-x),N)*Pprime
                Hlog=x*(x+1)+g_d-g_x-g_dx
                Href=Pprime*(mp.diff(lambda z:lf(N,z),d-x)-fprime_d)
                Y=mp.exp(2*mp.pi*1j*x)
                Halg=(2*N*(x-d/2+mp.fsum(U**r/(1-Q**(-r)) for r in range(1,N)))/(1-Y)
                      +mean+N/(mp.pi*1j))
                for predicted in (Href,Halg):
                    error=abs(Hlog-predicted)/(1+abs(Hlog))
                    assert error<mp.mpf('1e-48'),(N,direction,error)
                    worst=max(worst,error)
                hroot=mp.exp(mp.pi*1j*x+mp.pi*1j*x*(x+1)/N+lf(N,d)-lf(N,x)-lf(N,d-x))
                error=abs(hroot/Y-1)
                assert error<mp.mpf('1e-48')
                worst=max(worst,error)
                assert abs(Y/U**N-1)<mp.mpf('1e-65')
                characters+=1
                scaled=abs(Hlog)/(N*N*(1+mp.log(N)))
                assert scaled<20
                largest_bound=max(largest_bound,scaled)
                if direction==1:
                    poly=mean-2*mp.fsum(r*U**r/(1-Q**(-r)) for r in range(1,N))
                    top=-2*d*U**d/(1-Q**(-d))
                    err=N*N*abs(poly/top-1)
                    assert err<5
                    largest_top=max(largest_top,err);top_count+=1
                cases+=1
    return dict(precision_digits=mp.mp.dps,
                original_moving_factorial_heads=cases,
                independent_reflection_and_algebraic_comparisons=2*cases,
                original_root_descendant_characters=characters,
                large_clock_leading_terms=top_count,
                maximum_relative_identity_error=str(worst),
                maximum_H_over_N2logN=str(largest_bound),
                maximum_N2_times_clock_top_error=str(largest_top))


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);args=ap.parse_args()
    result=dict(status='PASS',algebra=exact_clock_algebra(),residues=symbolic_residues(),
                source=actual_periods(),gamma=gamma_comparisons(),
                scope='Exact original supported H-inserted root periods, source-specific continuation and retained boundary currents. No unproved contour transport or global relative coefficient.')
    target=args.output or Path(__file__).with_name('actual_root_channel_H_period_transport_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
