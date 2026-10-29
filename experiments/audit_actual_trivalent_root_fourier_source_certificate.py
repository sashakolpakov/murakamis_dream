#!/usr/bin/env python3
"""Exact original trivalent scalar versus independent root-Fourier formula.

The candidate Racah comparison is a finite check, not the missing proof.
"""
import itertools
import json
from pathlib import Path

from audit_actual_two_cut_ports import balanced_data


def mul(a,b,p):
    out = [0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):
            out[i+j] = (out[i+j]+v*w) % p
    return out


def coeff(a,n):
    return int(a[n]) if 0<=n<len(a) else 0


def case(N):
    p,eta,q,*_ = balanced_data(N)
    d,Q,x = N-1,q*q % p,pow(q,N-1,p)
    qb,Qb,xb = pow(q,-1,p),pow(Q,-1,p),pow(x,-1,p)
    fac,bar,sine = [1],[1],[1]
    for a in range(1,N):
        fac.append(fac[-1]*(1-pow(Q,a,p)) % p)
        bar.append(bar[-1]*(1-pow(Qb,a,p)) % p)
        sine.append(pow(pow(eta,N,p),a,p)*pow(q,-a*(a+1)//2,p)*fac[a] % p)
    def poch(start,length):
        v = [1]
        for a in range(length):
            v = mul(v,[1,-pow(Q,start+a,p) % p],p)
        return v
    def h(j,k):
        return pow(qb,k*k,p)*bar[d-j]*pow(bar[k]*bar[d-j-k],-1,p) % p
    def W(j,r,a,b):
        high = d-j
        total = 0
        for z in range(max(0,a-r),min(high,a)+1):
            total += pow(qb,z*z,p)*pow(xb,-r+a-z,p)*pow(Qb,z*(r-a+z),p)*pow(bar[z]**2*bar[high-z]**2*bar[a-z]*bar[r-a+z],-1,p)
        return bar[a]*bar[b]*bar[high]*total % p
    count = vanished = positive_domain = 0
    for j1,j2,j3 in itertools.product(range(d//2+1),repeat=3):
        r,J = j2+j3-j1,j1+j2+j3
        if not 0<=r<=2*min(j2,j3):
            continue
        actual = pow(q,-j1*(d-2*j1),p)*sum(pow(x,k+j1+j3-2*d,p)*h(j1,k)*h(j3,k)*W(j2,r,j3+k,d-j1-k) for k in range(min(d-j1,d-j3)+1)) % p
        f2 = mul(poch(1-j3,j3),poch(1-j3,j3),p)
        H,D = [],[]
        for hh,c in enumerate(f2):
            factor = 1
            for a in range(r):
                factor = factor*(1-pow(Q,1-r+hh+a,p)) % p
            H.append(c*factor % p)
            if hh>=r:
                D.append(c*fac[hh]*pow(fac[hh-r],-1,p) % p)
        assert all(c==0 for c in H[:r])
        g2 = mul(poch(1,j2),poch(1,j2),p)
        poly = mul(g2,D,p)
        assert len(poly)-1 <= J
        E = 3*j1*j1+j2*j2+j3*j3-2*j1*j2-2*j1*j3+2*j2*j3-2*j3-2
        pref = N*pow(q,E,p)*pow(fac[j1]*fac[j2]*fac[j3]*fac[r],-1,p) % p
        source_coeff = pref*coeff(poly,d) % p
        assert actual == source_coeff
        # Full root Fourier selection and the retained/annihilated two marks.
        ph = mul(g2,H,p)
        fourier = sum(pow(Q,(1-r)*z,p)*sum(c*pow(Q,z*h,p) for h,c in enumerate(ph)) for z in range(N)) % p
        assert fourier == N*(coeff(ph,r-1)+coeff(ph,N+r-1)) % p
        assert coeff(ph,r-1)==0
        delta = J-d
        if delta<0:
            assert actual==0
            vanished += 1
        else:
            ce = mul(poch(0,j3),poch(0,j3),p)
            reverse_D = [ce[e]*fac[2*j3-e]*pow(fac[2*j3-e-r],-1,p) % p for e in range(2*j3-r+1)]
            reverse_g = mul(poch(-j2,j2),poch(-j2,j2),p)
            low = coeff(mul(reverse_g,reverse_D,p),delta)*pow(Q,j2*(j2+1)-j3*(j3-1),p) % p
            assert low == coeff(poly,d)
            lead = pow(Q,j2*(j2+1)-j3*(j3-1),p)*fac[2*j3]*pow(fac[2*j3-r],-1,p) % p
            assert coeff(poly,J) == lead
            if delta==0:
                assert actual and coeff(poly,d)==lead
            if delta==1:
                ratio = 2*pow(Q,-2*j2,p)*(1-pow(Q,j2,p))*(1-pow(Q,j2+j3,p))*pow((1-Q)*(1+pow(Q,j3,p)),-1,p) % p
                assert actual and ratio and coeff(poly,d)==lead*ratio % p
            # Candidate comparison remains a finite validation only.
            R = 0
            for t in range(max(j1,j2,j3),J-max(j1,j2,j3)+1):
                den = 1
                for j in (j1,j2,j3):den = den*sine[t-j]*sine[J-j-t] % p
                R += sine[t]*sine[J-t]*pow(den,-1,p)
            C = sine[j1]*sine[j2]*sine[j3]*pow(N*sine[delta],-1,p) % p
            phase = (-1)**(N+J)*pow(q,2*j1*j1-j1*j2-j1*j3+j2*j3-J-3,p) % p
            assert actual == phase*C*R % p
            positive_domain += 1
        count += 1
    return {'N':N,'prime':p,'admissible_actual_source_triples':count,
            'exact_saturation_zeros':vanished,'candidate_positive_domain_checks':positive_domain,
            'own_Euler_derivative_formula_and_low_degree_reversal':True,
            'full_clock_low_mode_annihilation':True,
            'manifest_source_nonzero_entire_delta_zero_and_one_layers':True,
            'candidate_Racah_identity_not_proved_by_tests':True}


def main():
    rows = [case(N) for N in range(2,15)]
    result = {'status':'PASS','exact_original_source_root_Fourier_families':rows,
              'scope':'Own proof of Euler-coefficient source formula and exact J<d cancellation. Candidate C R comparison is supplementary finite validation; its general finite transformation remains separate.'}
    Path(__file__).with_name('actual_trivalent_root_fourier_source_certificate_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(f'PASS {len(rows)} original all-triple source/root-Fourier families; Euler coefficient, saturation zeros, low-degree reversal; candidate C R checks supplementary')


if __name__=='__main__':
    main()
