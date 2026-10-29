#!/usr/bin/env python3
"""Original sink convolution, its endpoint current and balanced source residue."""

import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

from audit_finite_sum_annihilator import field
from audit_figure_eight_whole_source import MixedEntries
from audit_actual_modular_dilog_circle import psi, log_psi_inside, log_derivative


def polynomial(N,p,Q,u,v):
    total,term=1,1
    for a in range(1,N):
        term=term*(u-pow(Q,a-1,p)*v)%p
        total=(total+term)%p
    return total


def finite_checks():
    rows=[]
    for N in range(2,14):
        p,gen,q=field(N);E=MixedEntries(N,p,q);Q=E.Q;d=N-1
        pp=[(-1)**j*pow(Q,j*(j-1)//2,p)*pow(E.F[j],-1,p)%p for j in range(N)]
        pm=[pow(Q,j,p)*pow(E.F[j],-1,p)%p for j in range(N)]
        for u,v in [(2,3),(gen,pow(gen,2,p)),(1,1)]:
            direct=0
            for i in range(N):
                for j in range(N-i):
                    a=i+j
                    direct+=(E.F[a]*pow(E.F[i],-1,p)*pp[j]
                             *pow(u,i,p)*pow(v,j,p))
            expected=polynomial(N,p,Q,u,v)
            assert direct%p==expected
            U=u*pow(Q,-2,p)%p;V=v*pow(Q,-1,p)%p
            field_coefficient=sum(pm[i]*pp[j]*pp[d-i-j]*pow(U,i,p)*pow(V,j,p)
                                  for i in range(N) for j in range(N-i))%p
            assert N*pow(Q,d,p)*field_coefficient%p==expected
            shifted=polynomial(N,p,Q,u,Q*v%p)
            assert ((u-v)*shifted-expected+1-pow(u,N,p)+pow(v,N,p))%p==0
            rows.append({'N':N,'prime':p,'u':u,'v':v,'original_sink':expected,
                         'full_field_tags':True,'exact_inhomogeneous_q_step':True})
        # Algebraic nonvanishing on the norm-one divisor, including arbitrary roots.
        powers={}
        for v in range(1,p):powers.setdefault(pow(v,N,p),v)
        balanced=[]
        for u in range(1,p):
            vn=(pow(u,N,p)-1)%p
            if vn in powers:
                v=powers[vn]
                assert polynomial(N,p,Q,u,v)!=0
                balanced.append((u,v))
                if len(balanced)==4:break
        rows[-1]['balanced_nonzero_cases']=balanced
    return rows


def symbolic_norm():
    u0,v0,t=sp.symbols('u0 v0 t',nonzero=True)
    D=1-u0+v0;tstar=(u0-1)/v0
    assert sp.factor(1-u0+v0*tstar)==0
    assert sp.factor(1/(1-tstar)-v0/(1+v0-u0))==0
    # Residues of the normalized kernel; g(a) is held as a regular scalar.
    a,g=sp.symbols('a g')
    at_integer=sp.simplify(D/((1-u0+v0)))
    at_norm=sp.simplify(D/((tstar-1)*v0))
    assert at_integer==1 and sp.factor(at_norm+1)==0
    return {'integer_residue':1,'monodromy_one_residue':'-g(a)',
            'same_Frobenius_fiber_gluing':True}


def analytic_checks():
    mp.mp.dps=45
    rows=[]
    for N in (2,3,5):
        h=2j*mp.pi/N
        u=mp.exp(mp.mpc('1.2','-.3')/N)
        v=mp.exp(mp.mpc('.4','.5')/N)
        c=mp.log(v/u)
        D=1-u**N+v**N
        ts=(u**N-1)/v**N
        alpha=mp.log(ts)/(2j*mp.pi)
        while mp.re(alpha)<-.05:alpha+=1
        while mp.re(alpha)>=.95:alpha-=1
        def g(a):return mp.exp(a*mp.log(u))*psi(N,1,c)/psi(N,1,c+h*a)
        vs=v*mp.exp(h*alpha)
        bbal=mp.mpc(0);term=mp.mpc(1)
        Q=mp.exp(h)
        for k in range(N):
            if k:term*=u-Q**(k-1)*vs
            bbal+=term
        orbit=mp.fsum(g(alpha+k) for k in range(N))
        assert abs(orbit-g(alpha)*bbal)<mp.mpf('1e-36')
        assert abs(u**N-vs**N-1)<mp.mpf('1e-40')
        assert abs(bbal)>mp.mpf('1e-15')
        a=mp.mpc('.37','.04')
        variable=u**N-v**N*mp.exp(2j*mp.pi*a)
        assert abs(g(a+N)/g(a)-variable)<mp.mpf('1e-36')
        assert abs(variable-(u**N-v**N))>mp.mpf('1e-5')
        def omega(a):
            t=mp.exp(2j*mp.pi*a)
            return 2j*mp.pi*D*t*g(a)/((t-1)*(1-u**N+v**N*t))
        # A finite rectangle, no assumption about infinite vertical tails.
        left=mp.mpf('-.05');right=N+left;bot=-mp.mpf('.1');top=mp.mpf('.1')
        assert bot<mp.im(alpha)<top
        bottom=mp.quad(lambda x:omega(x+1j*bot),[left]+[mp.mpf(k) for k in range(N)]+[right])
        rhs=mp.quad(lambda y:1j*omega(right+1j*y),[bot,0,top])
        upper=-mp.quad(lambda x:omega(x+1j*top),[left]+[mp.mpf(k) for k in range(N)]+[right])
        lhs=-mp.quad(lambda y:1j*omega(left+1j*y),[bot,0,top])
        contour=(bottom+rhs+upper+lhs)/(2j*mp.pi)
        original=mp.mpc(0);term=mp.mpc(1)
        for k in range(N):
            if k:term*=u-Q**(k-1)*v
            original+=term
        error=abs(contour+orbit-original)
        assert error<mp.mpf('1e-28'),(N,error)
        rows.append({'N':N,'variable_norm_error':float(abs(g(a+N)/g(a)-variable)),
                     'balanced_orbit_absolute_value':float(abs(bbal)),
                     'finite_rectangle_source_error':float(error),
                     'all_four_contour_edges_retained':True})
    return rows


def norm_and_growth_checks():
    mp.mp.dps=55
    rows=[]
    def stable_derivative(N,z):
        # The exactly removable finite-sum form (7b) of the full-Psi
        # derivative avoids numerical 0/0 at the physical root angles.
        value=mp.mpc(0)
        for ell in range(N):
            a=z+2j*mp.pi*(mp.mpf(ell)/N-1)
            value+=1j/(2*mp.pi) if not a else -1j/(2*mp.pi)*a/mp.expm1(-a)
        return value
    def logpsi(N,z):
        h=2j*mp.pi/N
        j=int(mp.nint(mp.im(z)/mp.im(h)))
        if 1<=j<=N and abs(z-j*h)<100*N*mp.eps:
            phiN=mp.sqrt(N)*mp.exp(mp.pi*1j*(mp.mpf('1/4')-(N+mp.mpf(1)/N)/12))
            factorial=mp.fprod(1-mp.exp(h*k) for k in range(1,j))
            return mp.log(phiN/factorial)
        if mp.re(z)<=0:return log_psi_inside(N,1,z)
        # Exact full-Phi reflection, independently proved in the modular
        # source theorem, evaluates only anchored |exp(-z)|<1 products.
        # It avoids apparent-pole cancellation in horizontal quadrature.
        cb=1j*(mp.sqrt(N)+1/mp.sqrt(N))/2
        return (-mp.pi*1j*(1+2*cb*cb)/6
                +mp.pi*1j*(-mp.sqrt(N)*z/(2*mp.pi)+cb)**2
                +log_psi_inside(N,-1,-z))
    for uv in [('.7','-.4','.9','.2'),('.5','-.5','.5','.5'),('1.2','-.4','.9','.7')]:
        u=mp.mpc(uv[0],uv[1]);v=mp.mpc(uv[2],uv[3])
        phi=mp.arg(u);gamma=mp.arg(v/u)
        lam=(mp.im(mp.polylog(2,v/u))-mp.im(mp.polylog(2,u))
             +mp.log(abs(u))*(mp.pi-gamma)-phi*mp.log(abs(v)))/(2*mp.pi)
        assert lam>max(0,mp.log(abs(u)),mp.log(abs(v)))
        for N in (8,16,32):
            h=2j*mp.pi/N;Q=mp.exp(h)
            ts=(u**N-1)/v**N;alpha=mp.log(ts)/(2j*mp.pi)
            w=v*mp.exp(h*alpha)
            pp=[mp.mpc(1)];rr=[mp.mpc(1)]
            for k in range(1,N):
                pp.append(pp[-1]*(u-Q**(k-1)*w))
                rr.append(rr[-1]*(u-Q**(-(k-1)))/w)
            bbal=mp.fsum(pp)
            ratio=N*mp.fsum(abs(z)**2 for z in pp)/mp.fsum(abs(z)**2 for z in rr)
            assert abs(abs(bbal)**2/ratio-1)<mp.mpf('1e-42')
            c=mp.log(v/u)
            logg=alpha*mp.log(u)+logpsi(N,c)-logpsi(N,c+h*alpha)
            residue=mp.exp(logg)*bbal
            phiN=mp.sqrt(N)*mp.exp(mp.pi*1j*(mp.mpf('1/4')-(N+mp.mpf(1)/N)/12))
            exact_normalizer=(N/phiN*u**N*mp.exp(logpsi(N,h-mp.log(u))
                               +logpsi(N,c)-c*mp.log(u)/h))
            normalizer_error=abs(residue/exact_normalizer-1)
            assert normalizer_error<mp.mpf('1e-40'),(N,normalizer_error)
            U=u/Q**2;V=v/Q;z=mp.log(u)-2*h;c0=c+h
            typed=(Q**(2-(N-1))/phiN*U**(N+1)*(U-Q**(-1))*(U-Q**(-1)*V)/V**2
                   *mp.exp(logpsi(N,-z)+logpsi(N,c0)-c0*z/h))
            typed_error=abs(typed/(Q**(-(N-1))/N*exact_normalizer)-1)
            assert typed_error<mp.mpf('1e-40'),(N,typed_error)
            original=mp.mpc(0);term=mp.mpc(1)
            for k in range(N):
                if k:term*=u-Q**(k-1)*v
                original+=term
            D=1-u**N+v**N
            inferred_barnes=(original-residue)/D
            assert abs(inferred_barnes)<10
            rate_error=abs(mp.log(abs(residue))-N*lam)
            assert rate_error<10*mp.log(N)
            rows.append({'N':N,'u':str(u),'v':str(v),'predicted_rate':float(lam),
                         'positive_norm_ratio_relative_error':float(abs(abs(bbal)**2/ratio-1)),
                         'exact_full_Psi_normalizer_relative_error':float(normalizer_error),
                         'exact_physical_boundary_tag_relative_error':float(typed_error),
                         'log_residue_rate_error':float(rate_error),
                         'actual_source_over_residue_error':float(abs(original/residue-1)),
                         'retained_Barnes_current_absolute_value':float(abs(inferred_barnes))})
    return rows


def main():
    result={'finite_source':finite_checks(),'residue_and_norm':symbolic_norm(),
            'full_Psi_relative_contours':analytic_checks(),
            'positive_norm_ratio_and_source_growth':norm_and_growth_checks(),
            'scope':'exact actual sink polynomial/current and balanced residue completion; '
                    'no automatic selected growing-cycle coefficient'}
    Path(__file__).with_name('audit_actual_sink_source_convolution_results.json').write_text(
        json.dumps(result,indent=2)+'\n')
    print('PASS 36 original sink/tag/current cases, three full-Psi variable norms/finite '
          'contours, nine positive norm ratios/exact normalizers and source-growth cases')


if __name__=='__main__':main()
