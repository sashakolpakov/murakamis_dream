#!/usr/bin/env python3
"""Original R port bands, exact scalar, paired interpolation and adapter symbol."""
import json
from pathlib import Path
import numpy as np
import mpmath as mp
from audit_actual_hardy_cauchy_network import HardyNetwork


def finite_checks():
    rows=[]
    for N in range(2,11):
        H=HardyNetwork(N,1);p,Q,x=H.p,H.Q,H.x
        r0,r1=2,3
        while pow(r1,N,p)==pow(x*r0,N,p):r1+=1
        r6,r7=x*r1%p,x*r0%p
        def V(r):return np.array([[pow(r,a,p)*pow(Q,i*a,p)%p for a in range(N)]
                                 for i in range(N)],dtype=np.int64)
        def Vi(r):return np.array([[pow(r,-a,p)*pow(Q,-i*a,p)*pow(N,-1,p)%p
                                   for i in range(N)] for a in range(N)],dtype=np.int64)
        M=np.kron(V(r6),V(r7))@H.plus%p@np.kron(Vi(r0),Vi(r1))%p
        assert np.all(M%p)
        grids={t:[rr*pow(Q,j,p)%p for j in range(N)]
               for t,rr in [(0,r0),(1,r1),(6,r6),(7,r7)]}
        def poch(z,L):
            v=1
            for j in range(L):v=v*(1-pow(Q,j,p)*z)%p
            return v
        checked={0:0,1:0,6:0,7:0};paired=0
        def check(port,vals,polys,band):
            nonlocal checked
            assert all(polys)
            scalar=int(vals[0])*pow(int(polys[0]),-1,p)%p
            assert all(int(y)%p==scalar*int(z)%p for y,z in zip(vals,polys))
            sign=1 if port in (0,1) else -1
            coeff=[sum(int(vals[j])*pow(grids[port][j],sign*a,p) for j in range(N))
                   *pow(N,-1,p)%p for a in range(N)]
            for a,v in enumerate(coeff):assert bool(v)==(band[0]<=a<=band[1]),(N,port,band,a,v)
            checked[port]+=1
        for kk in range(1,N+1):
            i=0;l=kk%N;z0=grids[0][i]
            for c in range(N):
                vals=[M[c*N+l,i*N+j] for j in range(N)]
                polys=[poch(pow(Q,kk+1,p)*x*z0*pow(z,-1,p)%p,N-kk) for z in grids[1]]
                check(1,vals,polys,(0,N-kk))
            for j in range(N):
                vals=[M[c*N+l,i*N+j] for c in range(N)]
                polys=[pow(z,N-kk,p)*poch(pow(Q,1-kk,p)*z*pow(z0,-1,p)%p,kk-1)%p
                       for z in grids[6]]
                check(6,vals,polys,(N-kk,N-1))
            block=np.array([[M[c*N+l,i*N+j] for j in range(N)] for c in range(N)],dtype=np.int64)
            assert np.array_equal(block*int(block[0,0])%p,np.outer(block[:,0],block[0,:])%p)
            hh=N-kk
            pin0=poch(pow(Q,1-hh,p)*x*r0*pow(r1,-1,p)%p,hh)
            pout0=pow(r6,hh,p)*poch(pow(Q,hh+1,p)*r6*pow(r0,-1,p)%p,N-1-hh)%p
            explicit=(H.kappa*pow(N,-1,p)*(-1)**hh*pow(Q,hh*(hh+1)//2,p)*pow(r0,-hh,p))%p
            assert int(block[0,0])==explicit*pin0*pout0%p
            paired+=1
        for mm in range(1-N,1):
            c=0;j=(-mm)%N;z1,z6=grids[1][j],grids[6][c]
            for l in range(N):
                vals=[M[c*N+l,i*N+j] for i in range(N)]
                polys=[pow(z,mm,p)*poch(z1*pow(x*z,-1,p)%p,N+mm-1)%p for z in grids[0]]
                check(0,vals,polys,(-mm,N-1))
            for i in range(N):
                vals=[M[c*N+l,i*N+j] for l in range(N)]
                polys=[poch(pow(Q,mm,p)*z*pow(x*z6,-1,p)%p,-mm) for z in grids[7]]
                check(7,vals,polys,(0,-mm))
            block=np.array([[M[c*N+l,i*N+j] for i in range(N)] for l in range(N)],dtype=np.int64)
            assert np.array_equal(block*int(block[0,0])%p,np.outer(block[:,0],block[0,:])%p)
            hh=-mm
            pin0=pow(r0,-hh,p)*poch(z1*pow(x*r0,-1,p)%p,N-1-hh)%p
            pout0=poch(pow(Q,-hh,p)*r7*pow(x*z6,-1,p)%p,hh)
            explicit=(H.kappa*pow(N,-1,p)*(-1)**hh*pow(Q,hh*(hh+1)//2,p)*pow(z6,hh,p))%p
            assert int(block[0,0])==explicit*pin0*pout0%p
            paired+=1
        rows.append({'N':N,'field':p,'all_source_normalized_port_rows':checked,
                     'conditional_opposite_pair_rank1_blocks':paired,
                     'explicit_tame_pair_normalizers':True,
                     'cyclic_endpoint_cases_included':True,
                     'original_full_Cartan_crossing_used':True})
    return rows


def analytic_symbols():
    mp.mp.dps=55;rows=[]
    for N in (16,32,64,128):
        h=2j*mp.pi/N;Q=mp.exp(h);x=-mp.exp(-h/2)
        r0=mp.exp(mp.log(2)/N);r1=mp.exp(mp.log(3j)/N)
        z0=r0;z1=r1*Q**(3*N//4);z6=x*r1*Q**(N//4);z7=x*r0*Q**(N//2)
        k=N//2;m=-N//2;delta=mp.mpc('.3','.2')
        def poch(a,L):return mp.fprod(1-a*Q**j for j in range(L))
        ps={0:lambda Z:Z**m*poch(z1/(x*Z),N+m-1),
            1:lambda Z:poch(Q**(k+1)*x*z0/Z,N-k),
            6:lambda Z:Z**(N-k)*poch(Q**(1-k)*Z/z0,k-1),
            7:lambda Z:poch(Q**m*Z/(x*z6),-m)}
        args={0:(z1/(x*z0),N+m-1),1:(Q**(k+1)*x*z0/z1,N-k),
              6:(Q**(1-k)*z6/z0,k-1),7:(Q**m*z7/(x*z6),-m)}
        zz={0:z0,1:z1,6:z6,7:z7};momenta={};errors={}
        for port in (0,1,6,7):
            a,L=args[port];S=sum(a*Q**j/(1-a*Q**j) for j in range(L))
            der=({0:m+S,1:S,6:N-k-S,7:-S})[port]
            pk=der/N
            momenta[port]=(-pk if port in (0,1) else pk)
            ratio=ps[port](zz[port]*mp.exp(delta/N))/ps[port](zz[port])
            err=abs(ratio/mp.exp(delta*pk)-1)
            assert N*err<5,(N,port,err)
            errors[port]=float(N*err)
        targets={0:mp.mpf('.75'),1:mp.mpf('.25'),6:mp.mpf('.75'),7:mp.mpf('.25')}
        assert max(N*abs(momenta[t]-targets[t]) for t in targets)<5
        rows.append({'N':N,'N_scaled_adapter_symbol_errors':errors,
                     'physical_momenta_real_parts':{t:float(mp.re(v)) for t,v in momenta.items()},
                     'original_negative_input_powers_retained':True})
    return rows


def global_profiles():
    mp.mp.dps=35;rows=[]
    L=lambda t:mp.im(mp.polylog(2,mp.exp(1j*t)))
    for scale in (mp.mpf('.4'),mp.mpf('.9'),mp.mpf('1.5')):
        delta=scale*mp.pi;hs=mp.pi-delta/2;js=delta/2
        H=lambda t:L(t)-L(t+delta)
        J=lambda t:L(t)+L(delta-t)
        Hmax=2*L(hs);Jmax=2*L(js)
        assert abs(H(hs)-Hmax)<mp.mpf('1e-30')
        assert abs(J(js)-Jmax)<mp.mpf('1e-30')
        hg=mp.inf;jg=mp.inf
        for q in range(96):
            t=2*mp.pi*q/96
            assert H(t)<=Hmax+mp.mpf('1e-25')
            assert J(t)<=Jmax+mp.mpf('1e-25')
            if abs(mp.arg(mp.exp(1j*(t-hs))))>mp.mpf('.2'):hg=min(hg,Hmax-H(t))
            if abs(mp.arg(mp.exp(1j*(t-js))))>mp.mpf('.2'):jg=min(jg,Jmax-J(t))
        assert min(hg,jg)>0
        rows.append({'delta_over_pi':float(scale),'H_global_max':float(Hmax),
                     'J_global_max':float(Jmax),'sampled_complement_gaps':[float(hg),float(jg)],
                     'entire_circle_and_shape1_endpoints_included':True})
    return rows


def main():
    result={'original_exact_port_polynomials':finite_checks(),
            'analytic_nonzero_adapter_symbols':analytic_symbols(),
            'global_conditional_profile_checks':global_profiles(),
            'scope':'EXACT original one-port and opposite-pair physical interpolants; '
                    'nonzero compact-positive adapter symbol; no arbitrary four-port continuation '
                    'or global scalar noncancellation claim'}
    Path(__file__).with_name('audit_actual_fourier_port_polynomials_results.json').write_text(
        json.dumps(result,indent=2)+'\n')
    print('PASS nine original full-scalar port tables/all cyclic cases/paired ranks, '
          'four analytic adapter-symbol scales, three whole-circle profile tests')


if __name__=='__main__':main()
