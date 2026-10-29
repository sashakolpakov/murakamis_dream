#!/usr/bin/env python3
"""Numerical diagnostics for the independently certified singular 6_2 state.

Exact root/branch/matrix certificates are in certify_six_two.py. This checks
the orientation convention, critical value, and finite-b Faddeev integral;
it is not used as proof of the volume limit.
"""

import json
from itertools import product
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.special import roots_hermite

from certify_six_two import H_EXPECTED, SIMPLE_SUPPORT
from check_literature_state_volume import Remainder, dilog_minus_exp


def saddle():
    mp.mp.dps=60
    c=mp.findroot(lambda c:c**5-3*c**4+5*c**3-5*c**2+4*c-1,
                  mp.mpc('1.1860784','.87464646'))
    a=c**3-2*c**2+2*c-1
    b=2*c**4-5*c**3+8*c**2-7*c+6
    # Uniform global inversion/conjugation fixes the source orientation.
    shapes=[1/mp.conj(q) for q in [a,a,b,b,1/(1-c),c]]
    y=np.array([complex(-mp.log(q)+mp.pi*1j) for q in shapes])
    r=y[[0,1,4,5]]
    D=lambda q:mp.im(mp.polylog(2,q))+mp.arg(1-q)*mp.log(abs(q))
    volume=float(2*sum(D(q) for q in [a,b,c]))
    S=np.array(SIMPLE_SUPPORT,dtype=float)
    H=np.array(H_EXPECTED,dtype=float)
    linear=np.array([-2,-2,-1,1])
    phase=1j*r@H@r+np.pi*linear@r-1j*np.sum(dilog_minus_exp(y))
    gradient=2j*H@r+np.pi*linear+1j*S.T@np.log(1+np.exp(y))
    assert np.max(np.abs(gradient))<1e-12
    assert abs(phase.real+volume)<1e-12
    assert abs(-r[0]-r[1]-r[2]+r[3])<1e-12
    fibre=np.vstack([np.eye(3),np.ones(3)])
    L=S@fibre
    Hf=fibre.T@H@fibre
    sigmoid=np.exp(y)/(1+np.exp(y))
    hessian=2j*Hf+1j*L.T@np.diag(sigmoid)@L
    cholesky=np.linalg.cholesky(-hessian.real)
    return r,y,H,linear,fibre,cholesky,phase,volume,float(np.max(np.abs(gradient)))


def integrate(b,order,data,importance=4):
    r0,y0,H,linear,fibre,cholesky,F0,volume,_=data
    h=b*b/(1+b*b)**2
    nodes,weights=roots_hermite(order)
    indices=np.array(list(product(range(order),repeat=3)))
    points=nodes[indices]
    log_weights=np.log(weights[indices]).sum(axis=1)
    # A narrower quadrature coordinate resolves the imaginary Hessian;
    # the compensating node^2 term and Jacobian retain the same integral.
    transform=np.linalg.inv(cholesky.T)*np.sqrt(4*np.pi*h/importance)
    S=np.array(SIMPLE_SUPPORT,dtype=float)
    remainder=Remainder(b,order=300)
    total=0j
    for start in range(0,len(points),256):
        p=points[start:start+256]
        real_displacement=p@transform.T
        r=r0+real_displacement@fibre.T
        y=y0+real_displacement@(S@fibre).T
        scaled=(1+b*b)*y
        log_phi=dilog_minus_exp(scaled)/(2j*np.pi*b*b)
        # The two equal middle Phi factors share the same exact evaluation.
        for j in [0,1,2,4,5]:
            correction=remainder(scaled[:,j])
            log_phi[:,j]+=correction
            if j==2:
                log_phi[:,3]+=correction
        exponent=(1j*np.einsum('bi,ij,bj->b',r,H,r)+np.pi*(r@linear)-F0)/(2*np.pi*h)
        exponent+=log_phi.sum(axis=1)+np.sum(p*p,axis=1)+log_weights[start:start+256]
        total+=np.exp(exponent).sum()
    # sqrt(h) exp(-F0/(2pi h))*J, with all three integration Jacobians.
    prefactor=(4*np.pi/importance)**1.5/((2*np.pi)**4*np.linalg.det(cholesky))
    return prefactor*total


def main():
    data=saddle()
    records=[]
    for b in [0.24,0.16]:
        values=[]
        for order in [36,56]:
            value=integrate(b,order,data)
            values.append(value)
            print(json.dumps({"b":b,"order":order,"normalized_modulus":abs(value)}),flush=True)
        records.append({"b":b,"orders":[36,56],
                        "normalized_complex":[[z.real,z.imag] for z in values],
                        "relative_refinement_difference":abs(values[1]-values[0])/abs(values[1])})
    Path(__file__).with_name('singular_state_volume_results.json').write_text(json.dumps({
        "scope":"Numerical diagnostics only; the proof uses exact certificates and analytic bounds.",
        "quadrature_importance":4,
        "classical_volume":data[-2],"classical_critical_gradient_max":data[-1],
        "classical_real_critical_value":data[-3].real,"records":records},indent=2)+'\n')


if __name__=='__main__':
    main()
