#!/usr/bin/env python3
"""Exact intermediate-stage audit of the own finite source/Racah proof."""
import itertools
import json
from pathlib import Path

import sympy as sp

from audit_actual_two_cut_ports import balanced_data
from audit_actual_trivalent_root_fourier_source_certificate import mul, coeff
from audit_finite_balanced_sears_operator_proof import poch, hyper


def case(N):
    p,eta,q,*_ = balanced_data(N)
    Q,d = q*q % p,N-1
    fac,sine = [1],[1]
    for k in range(1,N):
        fac.append(fac[-1]*(1-pow(Q,k,p)) % p)
        sine.append(pow(pow(eta,N,p),k,p)*pow(q,-k*(k+1)//2,p)*fac[k] % p)
    def pol(start,length):
        out = [1]
        for i in range(length):out = mul(out,[1,-pow(Q,start+i,p) % p],p)
        return out
    count = 0
    for a,b,c in itertools.product(range(d//2+1),repeat=3):
        J,r = a+b+c,b+c-a
        if J<d or not 0<=r<=2*min(b,c):continue
        delta,r1,r2 = J-d,a+b-c,a+c-b
        f2 = mul(pol(1-c,c),pol(1-c,c),p)
        D = [f2[h]*fac[h]*pow(fac[h-r],-1,p) % p for h in range(r,2*c+1)]
        P = coeff(mul(mul(pol(1,b),pol(1,b),p),D,p),d)
        Cdelta = pow(Q,-b*(b+1)+c*(c-1),p)*P % p
        inner = [0]*(c+1)
        for s in range(max(0,r-c),min(r,c)+1):
            weight = pow(Q,s*s-s*(r+c),p)*pow(fac[s]*fac[r-s]*fac[c-s]*fac[c-r+s],-1,p) % p
            term = pol(s-r,c)
            for i,v in enumerate(term):inner[i] = (inner[i]+weight*v) % p
        expected = [0]*(c+1)
        for k in range(min(c,2*c-r)+1):
            weight = pow(Q,-c*r,p)*(-1)**k*pow(Q,k*(k-1)//2,p)*fac[2*c-k]*pow(fac[r]*fac[2*c-k-r]*fac[k]*fac[c-k]**2,-1,p) % p
            term = pol(c-r,c-k)
            for i,v in enumerate(term):expected[i+k] = (expected[i+k]+weight*v) % p
        assert inner == expected
        for k in range(delta+1):
            moment = 0
            for s in range(max(0,r-c),min(r,c)+1):
                weight = pow(Q,s*s-s*(r+c),p)*pow(fac[s]*fac[r-s]*fac[c-s]*fac[c-r+s],-1,p) % p
                moment += weight*poch(pow(Q,s-c,p),k,Q,p)
            moment_expected = (-1)**k*pow(Q,-c*k+k*(k-1)//2-(c-k)*r,p)*fac[2*c-k]*pow(fac[r]*fac[2*c-k-r]*fac[c-k]*fac[c],-1,p) % p
            assert moment % p == moment_expected
        Hc = hyper(delta,[pow(Q,-delta,p),pow(Q,-r2,p),pow(Q,-c,p),pow(Q,-c,p)],
                   [pow(Q,-a-c,p),pow(Q,-a-c,p),pow(Q,-2*c,p)],Q,p)
        Hsym = hyper(delta,[pow(Q,-delta,p),pow(Q,-a,p),pow(Q,-b,p),pow(Q,-c,p)],
                     [pow(Q,-a-b,p),pow(Q,-a-c,p),pow(Q,-b-c,p)],Q,p)
        Hb = hyper(delta,[pow(Q,-delta,p),pow(Q,-r,p),pow(Q,-b,p),pow(Q,-b,p)],
                   [pow(Q,-b-c,p),pow(Q,-b-c,p),pow(Q,-2*b,p)],Q,p)
        K1 = poch(pow(Q,-a,p),delta,Q,p)*poch(pow(Q,-a-b,p),delta,Q,p)*pow(poch(pow(Q,-a-c,p),delta,Q,p)*poch(pow(Q,-r1,p),delta,Q,p),-1,p) % p
        K2 = poch(pow(Q,-c,p),delta,Q,p)*poch(pow(Q,-a-c,p),delta,Q,p)*pow(poch(pow(Q,-b-c,p),delta,Q,p)*poch(pow(Q,-r2,p),delta,Q,p),-1,p) % p
        assert Hc == K1*Hsym % p and Hb == K2*Hsym % p
        target = pow(Q,b*(a+c-b)+c*(2*c+1),p)*fac[2*b]*fac[a]**2*pow(fac[r1]*fac[delta]*fac[a-delta]**2,-1,p)*Hb % p
        assert Cdelta == target
        E = 3*a*a+b*b+c*c-2*a*b-2*a*c+2*b*c-2*c-2
        actual_from_source = N*pow(q,E,p)*P*pow(fac[a]*fac[b]*fac[c]*fac[r],-1,p) % p
        Dsym = N*N*pow(sine[r]*sine[r1]*sine[r2]*sine[delta]*sine[a-delta]*sine[b-delta]*sine[c-delta],-1,p) % p
        Esource = 2*a*a-a*b-a*c+b*c-J-3
        phase = (-1)**(N+J)*pow(q,Esource,p) % p
        assert actual_from_source == phase*Dsym*Hsym % p
        # Exact positive sine representation of every Hsym summand, including all endpoints.
        Hpositive = 0
        for k in range(delta+1):
            val = sine[delta]*sine[a]*sine[b]*sine[c]
            val *= sine[a+b-k]*sine[a+c-k]*sine[b+c-k]
            val *= pow(sine[delta-k]*sine[a-k]*sine[b-k]*sine[c-k]*sine[k]*sine[a+b]*sine[a+c]*sine[b+c],-1,p)
            Hpositive += val
        assert Hsym == Hpositive % p
        R = 0
        for t in range(max(a,b,c),J-max(a,b,c)+1):
            den = 1
            for j in (a,b,c):den = den*sine[t-j]*sine[J-j-t] % p
            R += sine[t]*sine[J-t]*pow(den,-1,p)
        Rpref = N**3*pow(sine[a]*sine[b]*sine[c]*sine[r]*sine[r1]*sine[r2]*sine[a-delta]*sine[b-delta]*sine[c-delta],-1,p) % p
        assert R % p == Rpref*Hsym % p
        count += 1
    return {'N':N,'supported_all_order_triples':count,'finite_Newton_Vandermonde_moments':True,
            'both_Sears_and_symmetric_positive_series':True,'full_original_source_phase_and_R_prefactors':True}


def symbolic_phase():
    a,b,c,N = sp.symbols('a b c N',integer=True)
    delta = a+b+c-N+1
    r = b+c-a
    Z0 = r*(1-c)+r*(r-1)/2+b*(b+1)/2+a*b-a*(a-1)/2+c*(b-a)+c*(c+1)/2
    Z = Z0-c*r+delta*(delta-1-2*b)-b*(b+1)+c*(c-1)
    K = -a*a+a*b-2*a*c-a+b*c+b+c*c
    assert sp.expand(Z+K-b*(a+c-b)-c*(2*c+1)+N*(-N+2*a+2*c+1)) == 0
    return {'exact_prefactor_exponent_multiple_N':True}


def main():
    rows = [case(N) for N in range(2,17)]
    out = {'status':'PASS','symbolic_phase':symbolic_phase(),'exact_all_stages':rows,
           'scope':'Own finite coefficient-to-Racah and original scalar phase/positivity proof. No full magnetic tensor norm, white/marked sewing or graph volume theorem.'}
    Path(__file__).with_name('finite_trivalent_euler_racah_transform_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(f'PASS {len(rows)} all-supported all-order exact Newton/Vandermonde/Sears/source families; symbolic phase and positive symmetric series')


if __name__=='__main__':
    main()
