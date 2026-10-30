#!/usr/bin/env python3
"""Exact algebra only; the geometric obstruction uses reviewed inputs."""
import json
from pathlib import Path
import sympy as s


def main():
    N,a,k,t,B,b,e,x=s.symbols('N a k t B b e x')
    phase=(N-1-2*a+2*k)*(e*x+B-b)-t*k
    residual=s.expand(phase-(N-1-2*a+2*k)*e*x)
    assert s.expand(residual.subs(k,k+1)-residual-(2*(B-b)-t))==0
    xi,lam,tau,y=s.symbols('xi lam tau y',real=True)
    nu=tau/2-s.I*y/(2*s.pi)
    assert s.simplify(s.re(2*nu-tau))==0
    assert s.simplify(s.re(1+nu-tau)-(1-tau/2))==0
    assert s.simplify(s.re(1-nu)-(1-tau/2))==0
    assert s.simplify((tau-nu)-(tau/2+s.I*y/(2*s.pi)))==0
    # Exact additive exponent of each vertex character q^(d-2a+2k).
    assert s.expand((N-1-2*a+2*k)/(2*N)
                    -(k/N+s.Rational(1,2)-a/N)+1/(2*N))==0
    # A cup contributes d/(2N)=1/2-1/(2N).
    assert s.simplify((N-1)/(2*N)-s.Rational(1,2)+1/(2*N))==0
    Xr,Xi,delta=s.symbols('Xr Xi delta',real=True)
    equation=-y+2*s.pi*s.I*delta+e*2*s.pi*s.I*(Xr+s.I*Xi)
    # Treat the actual slope as real, then check both possible signs.
    for sign in (-1,1):
        q=s.expand(equation.subs(e,sign))
        assert s.simplify(s.re(q)+y+2*s.pi*sign*Xi)==0
        assert s.simplify(s.im(q)-2*s.pi*(delta+sign*Xr))==0
    result=dict(status='PASS',residual_phase_identities=1,
                central_adapter_and_reversal_identities=4,
                exact_character_shift_identities=2,
                real_imaginary_multiplier_identities=4,
                scope='Exact original affine phase and low/high algebra; no new numerical source or global rate test.')
    Path(__file__).with_name('actual_positive_fourier_radial_geometric_obstruction_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
