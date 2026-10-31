#!/usr/bin/env python3
"""Literal coproduct/DFT monomer coefficients and closed spectral identities.

No large-N sampling is used to certify an asymptotic theorem.
"""
import argparse
from fractions import Fraction
import json
from pathlib import Path
import sys

import mpmath as mp
import numpy as np
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit_actual_nc_morse_graph_first_normal_source_reduction import Local


def run():
    z = sp.symbols('z')
    counts = dict(levels=0, spectral_values=0, original_grid_entries=0,
                  wrong_total_entries=0, monomer_coefficients=0,
                  odd_reference_coefficients=0, even_reference_coefficients=0,
                  exact_chi_four_nodes=0, exact_node_avoidances=0,
                  symbolic_identities=0, integral_profiles=0,
                  stationary_identities=0, closed_energy_identities=0)
    for N in range(3,9):
        loc = Local(N)
        p,q,Q,d = loc.p,loc.q,loc.Q,loc.d
        # Build the actual physical coproduct Casimir, independently of the
        # triangular face path whose coefficient is being tested.
        K = loc.Kpair[0]
        Ki = np.diag([pow(int(v),-1,p) for v in np.diag(K)])
        omega = (loc.Fpair[0] @ loc.Epair[0]+q*K+pow(q,-1,p)*Ki) % p
        powers = [np.eye(N*N,dtype=np.int64)]
        for _ in range(d): powers.append(powers[-1] @ omega % p)
        chi = sp.Poly(2*sp.chebyshevt(N,z/2)+2,z)
        cc = [int(a)%p for a in chi.all_coeffs()]
        nodes = [(q*pow(Q,j,p)+pow(q,-1,p)*pow(Q,-j,p))%p for j in range(N)]
        bs = [(2-pow(Q,j,p)-pow(Q,-j,p))%p for j in range(N)]

        def operator(sigma, derivative=False):
            op = np.zeros_like(omega)
            for pos,a in enumerate(cc[:-1]):
                degree = N-pos
                for r in range(degree):
                    exponent = degree-1-r
                    if derivative:
                        if exponent == 0: continue
                        value = a*exponent*pow(sigma,exponent-1,p)%p
                    else: value = a*pow(sigma,exponent,p)%p
                    op = (op+value*powers[r]) % p
            return op

        def extract(op, i, j):
            k,t = j-i,d-j
            total = 0
            for u in range(N):
                x = -q*pow(Q,u,p)%p
                for v in range(N):
                    for r in range(N):
                        s = (u+v-r)%N
                        delta = r-u
                        c = pow(Q,-delta,p)
                        hgrid = N*pow(q,d*delta,p)*pow(c,d,p)*int(op[r*N+s,u*N+v])%p
                        total = (total+hgrid*pow(x,-k,p)*pow(c,-t,p))%p
            return total*pow(N,-3,p)%p

        values = list(dict.fromkeys([(-2)%p,2,0,nodes[0],nodes[N//2-1]]))
        for sigma in values:
            op = operator(sigma)
            for u in range(N):
                for v in range(N):
                    for r in range(N):
                        s = (u+v-r)%N
                        if r+s != u+v:
                            assert int(op[r*N+s,u*N+v]) == 0
                            counts['wrong_total_entries'] += 1
                        counts['original_grid_entries'] += 1
            for j in range(N//2):
                for i in range(j+1):
                    expected = pow(-1,j-i,p)
                    for r in range(i+1,j+1): expected = expected*bs[r]%p
                    for r in range(N):
                        if r<i or r>j: expected = expected*(sigma-nodes[r])%p
                    assert extract(op,i,j) == expected,(N,sigma,i,j)
                    counts['monomer_coefficients'] += 1
            counts['spectral_values'] += 1
        reference = (-operator(-2%p))%p if N%2==0 else (operator(-2%p)-pow(N,-2,p)*operator(-2%p,True))%p
        for j in range(N//2):
            for i in range(j+1):
                expected = 1
                for r in range(i+1,j+1): expected = expected*bs[r]%p
                for r in range(N):
                    if (r<i or r>j) and not (N%2 and r==N//2):
                        expected = expected*(2+nodes[r])%p
                if N%2: expected = expected*pow(N,-2,p)%p
                assert extract(reference,i,j) == expected
                counts['odd_reference_coefficients' if N%2 else 'even_reference_coefficients'] += 1
        for k in range(N//2+1):
            delta = Fraction(k,N) if N%2==0 else Fraction(2*k+1,2*N)
            if delta>Fraction(1,2): continue
            zz = (-pow(Q,k,p)-pow(Q,-k,p))%p if N%2==0 else (-nodes[k])%p
            assert int(chi.eval(zz))%p == 4
            assert all(zz != node for node in nodes)
            counts['exact_chi_four_nodes'] += 1
            counts['exact_node_avoidances'] += N
        counts['levels'] += 1

    a,b = sp.symbols('a b',real=True)
    kappa = -sp.cos(a+b)/sp.cos(b-a)
    expressions = [sp.cos(2*a)+kappa-sp.sin(2*a)*sp.tan(b-a),
                   sp.cos(2*b)+kappa+sp.sin(2*b)*sp.tan(b-a),
                   sp.cos(a+z)*sp.cos(b-z)+sp.cos(b+z)*sp.cos(a-z)
                   -sp.cos(a+b)-sp.cos(b-a)*sp.cos(2*z)]
    for expr in expressions:
        assert sp.trigsimp(expr, method='fu') == 0
        counts['symbolic_identities'] += 1

    mp.mp.dps = 75
    half = mp.mpf(1)/2
    lob = lambda t: mp.im(mp.polylog(2,mp.exp(2j*t)))/2
    f = lambda t: (lob(mp.pi*t)+lob(mp.pi*(half-t)))/mp.pi
    max_error = mp.mpf(0)
    pairs = [(mp.mpf(1)/8,mp.mpf(3)/8),(mp.mpf(1)/6,mp.mpf(1)/3),
             (mp.mpf(1)/10,mp.mpf(2)/5),(mp.mpf(1)/9,mp.mpf(2)/7),
             (mp.mpf(0),mp.mpf(1)/4),(mp.mpf(1)/4,half)]
    for mu,nu in pairs:
        w = nu-mu
        if mu==0: delta=half
        elif nu==half: delta=mp.mpf(0)
        else: delta=mp.acos(-mp.cos(mp.pi*(mu+nu))/mp.cos(mp.pi*w))/(2*mp.pi)
        tc=half-delta
        pts=[mu]+([tc] if mu<tc<nu else [])+[nu]
        if mu==0: integral=mp.mpf(0)
        elif nu==half:
            integral=2*mp.quad(lambda t:mp.log(mp.tan(mp.pi*t)),[mu,nu])
        else:
            integral=mp.quad(lambda t:mp.log(mp.sin(mp.pi*t)**2/abs(mp.cos(mp.pi*t)**2-mp.sin(mp.pi*delta)**2)),pts)
        closed=f(mu)+f(w)-f(nu)
        h0=2*(f(mu)-f(nu))
        max_error=max(max_error,abs(integral-closed),abs(2*closed-h0-2*f(w)))
        counts['integral_profiles'] += 1
        counts['closed_energy_identities'] += 1
        if 0<mu<nu<half:
            ratio=abs(mp.cos(mp.pi*(mu+delta))*mp.cos(mp.pi*(nu-delta)) /
                      (mp.cos(mp.pi*(nu+delta))*mp.cos(mp.pi*(mu-delta))))
            max_error=max(max_error,abs(ratio-1))
            counts['stationary_identities'] += 1
    assert max_error < mp.mpf('1e-65')
    return dict(status='PASS',counts=counts,max_identity_error=str(max_error),
                scope='Original physical coproduct polynomial and exact inverse DFT, both-parity reference, symbolic stationary identities and fixed integral identities. No rate sampling or shared energy estimate.')


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('actual_protected_outer_spectral_energy_results.json'))
    args=parser.parse_args()
    result=run()
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
