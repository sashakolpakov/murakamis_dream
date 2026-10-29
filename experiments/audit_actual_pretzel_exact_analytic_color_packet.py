#!/usr/bin/env python3
"""Exact high-window polynomial, original marked source and complex colors."""

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_two_cut_ports import balanced_data,coproduct
from audit_actual_pretzel_complete_base_casimir_polynomial import (
    rotate_box,polyadd,polymul,matrix_value,remainder)
from audit_actual_pretzel_cusp_color_two_band_bound import continuants
from audit_actual_odd_pretzel_augmented_transfer_source import transfer_source
from audit_actual_pair_casimir_commutant_and_rotated_trace import phi
from audit_exact_factorial_interpolation import factorial


def field_case(N,s=5):
    p,eta,q,E,F,K,pivot,Rp,Rm=balanced_data(N)
    d=N-1;Q=q*q%p;x=int(K[0,0]);kappa=int(Rp[0,0]);M=d//2
    lo=(26*N+99)//100;hi=min(M,48*N//100)
    rho=(q-pow(q,-1,p))%p
    Et,Ft,Kt=coproduct(rho*rho*E%p,F,K,2,N,p)
    Ki=np.diag([pow(int(z),-1,p)for z in np.diag(Kt)])
    O=(Ft@Et+q*Kt+pow(q,-1,p)*Ki)%p;eye=np.eye(N*N,dtype=np.int64)
    ids=[a*N+d-a for a in range(N)];f=continuants(O[np.ix_(ids,ids)],p)
    fac=[1]
    for a in range(1,N):fac.append(fac[-1]*(1-pow(Q,a,p))%p)
    nodes=[(pow(q,2*a+1,p)+pow(q,-2*a-1,p))%p for a in range(M)]
    B=[[1]]
    for a in range(M):B.append(polymul(B[-1],[nodes[a],-1],p))
    Us=[eye,O.copy()]
    for a in range(2,N):Us.append((O@Us[-1]-Us[-2])%p)
    # Monic P_N = trace-Chebyshev_N + 2.
    t0,t1=[2],[0,1]
    for a in range(2,N+1):t0,t1=t1,polyadd([0]+t1,[-z for z in t0],p)
    PN=polyadd(t1,[2],p)
    originals={};fulls={};cores={};windows={};polys={}
    for h in range(min(2,lo-1)+1):
        j=N-h;Lj=pow(-1,j-1,p)*Us[j-1]%p
        originals[h]=Rm@Lj%p;fulls[h]=rotate_box(originals[h],N,x,p)
        row=fulls[h][ids[0],ids]
        core=[0]
        for v in range(M+1):core=polyadd(core,[int(row[v])*z for z in f[v]],p)
        cores[h]=matrix_value(core,O,p)
        reconstructed=[0];window=[0]
        for r in range(M+1):
            A=sum(pow(Q,-v*r,p)*fac[2*v]*pow(fac[v]*fac[v-h]*fac[v+h]*fac[v-r]%p,-1,p)
                  for v in range(max(h,r),M+1))%p
            coefficient=N*N*pow(kappa,-1,p)*pow(q,h*h,p)*pow(-1,r,p)*pow(q,2*r*r+r,p)*A*pow(fac[r]**3%p,-1,p)%p
            term=[coefficient*z%p for z in B[r]]
            reconstructed=polyadd(reconstructed,term,p)
            if lo<=r<=hi:window=polyadd(window,term,p)
        assert matrix_value(reconstructed,O,p).tolist()==cores[h].tolist()
        windows[h]=matrix_value(window,O,p);polys[h]=window
    hs=[0,1,min(2,lo-1),1,0][:s]
    prod_full=eye.copy();prod_core=eye.copy();prod_win=eye.copy();poly=[1]
    for h in hs:
        prod_full=prod_full@fulls[h]%p;prod_core=prod_core@cores[h]%p;prod_win=prod_win@windows[h]%p
        poly=polymul(poly,polys[h],p)
    packet=phi(prod_win,N,pivot,p)
    residue=pow(-1,d,p)*N*N*remainder(poly,PN,p)[d]%p
    assert packet==residue
    assert packet==transfer_source(N,x,p,[rotate_box(windows[h],N,x,p)for h in hs])
    actual=transfer_source(N,x,p,[originals[h]for h in hs])
    assert actual==phi(prod_full,N,pivot,p)
    alias=phi((prod_full-prod_core)%p,N,pivot,p)
    truncation=phi((prod_core-prod_win)%p,N,pivot,p)
    assert (actual-packet-alias-truncation)%p==0
    return {'N':N,'boxes':s,'physical_deficits':hs,'window':[lo,hi],
            'actual_original_turn_and_mark_packet':True,
            'all_Hermite_normals_equal_coefficient_source':True,
            'retained_alias_and_window_residuals_exact':True}


def mp_poly_add(a,b):
    c=[mp.mpc(0)]*max(len(a),len(b))
    for j,x in enumerate(a):c[j]+=x
    for j,x in enumerate(b):c[j]+=x
    return c


def mp_poly_mul(a,b):
    c=[mp.mpc(0)]*(len(a)+len(b)-1)
    for j,x in enumerate(a):
        for k,y in enumerate(b):c[j+k]+=x*y
    return c


def evaluate(poly,z):
    f,df=mp.mpc(0),mp.mpc(0)
    for a in reversed(poly):df=df*z+f;f=f*z+a
    return f,df


def complex_window(N,chi):
    q=mp.exp(mp.j*mp.pi/N);Q=q*q;d=N-1;M=d//2;h=N*chi/mp.pi
    lo=int(mp.ceil(mp.mpf('.26')*N));hi=min(M,int(mp.floor(mp.mpf('.48')*N)))
    fac=[mp.mpc(1)]
    for a in range(1,N):fac.append(fac[-1]*(1-Q**a))
    gm={lo:factorial(N,lo-h)};gp={lo:factorial(N,lo+h)}
    for v in range(lo,M):gm[v+1]=gm[v]*(1-Q**(v+1-h));gp[v+1]=gp[v]*(1-Q**(v+1+h))
    B=[mp.mpc(1)];out=[mp.mpc(0)];kappa=q**(mp.mpf(d*d)/2)
    for r in range(M+1):
        if lo<=r<=hi:
            A=mp.fsum(Q**(-v*r)*fac[2*v]/(fac[v]*fac[v-r]*gm[v]*gp[v])for v in range(r,M+1))
            coefficient=N*N/kappa*q**(h*h)*(-1)**r*q**(2*r*r+r)*A/fac[r]**3
            out=mp_poly_add(out,[coefficient*a for a in B])
        B=mp_poly_mul(B,[2*mp.cos((2*r+1)*mp.pi/N),-1])
    return out


def complex_case(N):
    mp.mp.dps=80;s=5;d=N-1
    chis=[mp.mpc('.012','.007'),mp.mpc('-.009','.003'),mp.mpc(0),mp.mpc('.01','-.004'),mp.mpc('.005','.008')]
    polys=[complex_window(N,z)for z in chis]
    for chi,poly in zip(chis,polys):
        reflected=complex_window(N,-chi)
        assert max(abs(a-b)for a,b in zip(poly,reflected))<mp.mpf('1e-55')*max(1,*(abs(a)for a in poly))
    poly=[mp.mpc(1)]
    for f in polys:poly=mp_poly_mul(poly,f)
    source=mp.mpc(0)
    for j in range((d+1)//2):
        c=2*mp.cos((2*j+1)*mp.pi/N);value,normal=evaluate(poly,c)
        source+=(-1)**d*((4-c*c)*normal-c*value)
    if N%2:source+=evaluate(poly,-2)[0]
    alpha=mp.pi/s;lob=lambda a:mp.im(mp.polylog(2,mp.exp(2*mp.j*a)))/2
    F0=4*s/mp.pi*(lob(mp.pi/4+alpha/2)+lob(mp.pi/4-alpha/2))
    u=mp.atan(mp.sec(alpha));aa=mp.sin(2*u)/(2*mp.pi);bb=(1+mp.cos(2*u))/(2*mp.pi)
    growth=F0-aa/4*sum(mp.re(z)**2 for z in chis)+(5*aa/4+2*bb*bb/aa)*sum(mp.im(z)**2 for z in chis)
    normalized=abs(source)/(N**mp.mpf('1.5')*mp.exp(N*growth))
    # Finite diagnostic only; the theorem's N-independent constant is
    # established from the uniform complex contour proof, not these values.
    assert normalized<1000
    return {'N':N,'exact_separate_color_evenness':True,
            'full_original_normal_source_at_complex_color':True,
            'finite_complex_growth_normalized':float(normalized)}


if __name__=='__main__':
    finite=[field_case(N)for N in range(5,11)]
    complex_rows=[complex_case(N)for N in (8,9,12,13)]
    result={'status':'PASS','literal_physical_packet_and_retained_source':finite,
            'exact_holomorphic_color_packets':complex_rows,
            'scope':'Packet is defined by finite original coefficients and full Phi2; rate/residual estimates proved analytically, not inferred from diagnostics.'}
    Path(__file__).with_name('actual_pretzel_exact_analytic_color_packet_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(f'PASS {len(finite)} full original marked packet/source decompositions; {len(complex_rows)} exact even holomorphic normal-source packets')
