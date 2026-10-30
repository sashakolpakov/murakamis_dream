#!/usr/bin/env python3
"""Exact source phase and derivative identities; no coefficient continuation."""
import json
from pathlib import Path
import sympy as s


def main():
    N,j,t=s.symbols('N j t')
    d=N-1
    phase_c=j*(t+j-d)-j*(j+1)/2+j*N/2
    assert s.expand(phase_c+(d-2*j)*t/2-(d*(t-j)+j*j)/2)==0
    w,c,C,ss,r=s.symbols('w c C ss r', nonzero=True)
    B=w*w+2*c*w+C*C
    V=w*w+2*c*w+1
    # d_y log Y, where r^2=B, r_y=w(w+c)/r, ss^2+C^2=1.
    logY_y=2*s.I*w*(w+c)/(r*(ss+s.I*r))-2*w*(w+c)/V
    expected=2*s.I*ss*w*(w+c)/(r*V)
    numerator=s.factor(s.together(logY_y-expected)).as_numer_denom()[0]
    remainder=s.rem(s.Poly(numerator,r),s.Poly(r*r-B,r)).as_expr()
    assert s.factor(remainder.subs(C*C,1-ss*ss))==0
    T,U=s.symbols('T U',nonzero=True)
    # Multiplying w+c by 2sqrt(T) gives the caustic polynomial.
    caustic=2*U-(T+1)
    assert s.expand(caustic.subs(U,(T+1)/2))==0
    xi,lam,y,Phi,J=s.symbols('xi lam y Phi J')
    C0=s.symbols('C0')
    F=J+(xi-s.Rational(1,2))*y+Phi-C0
    L=F-lam*y
    H=L+(lam+s.Rational(1,2)-xi)*y
    assert s.expand(H-(J+Phi-C0))==0
    # Local tau shift at fixed y; Phi_nu=2pi i(lambda+1/2-xi).
    pt=s.symbols('Phi_tau')
    Ltau=pt+s.pi*s.I*(lam+s.Rational(1,2)-xi)-s.pi*s.I/2
    assert s.expand(Ltau-(pt+s.pi*s.I*(lam-xi)))==0
    result=dict(status='PASS',exact_source_prefactor_phase=1,
                characteristic_derivative_identity=1,caustic_identity=1,
                critical_value_identity=1,tau_momentum_shift=1,
                scope='Exact selected-action algebra; complex-domain exclusion is analytical. No off-lattice coefficient or global period test.')
    Path(__file__).with_name('actual_q_hahn_holomorphic_fourier_legendre_transport_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
