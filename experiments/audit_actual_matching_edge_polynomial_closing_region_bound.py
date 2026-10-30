#!/usr/bin/env python3
"""Canceled actual Sears polynomial, spectral removable poles and q normals."""
import json
import math
from pathlib import Path
import mpmath as mp
from audit_actual_q_hahn_physical_generic_jet_bound import Jet
from audit_high_color_first_normal_r_degree import root_field
from audit_actual_matching_edge_polynomial_endpoint_control import original,transformed


def poch(x,Q,n):
    value=Q**0
    for r in range(n):value*=1-x*Q**r
    return value


def canceled_terms(d,a,q,Z):
    Q=q*q;A=q**-1*Z**-1*Q**(-d);B=q**-1*Z*Q**(-d-a)
    common=poch(Q**(-d),Q,a)*poch(Q**(-d-a-1),Q,a)
    return [((-1)**k*A**k*Q**(k*(2*a-k+1)//2)
             *poch(Q**(-a),Q,k)**2*poch(q*Z,Q,k)**2
             *poch(A,Q,a-k)*poch(B*Q**k,Q,a-k)
             /(poch(Q,Q,k)**2*common)) for k in range(a+1)]


def exact():
    generic=removable=germs=0;Jet.p=1000003;Jet.order=1
    for q0 in [2,3]:
        q=Jet(q0);Q=q*q
        for d in range(2,14):
            for a in range(1,d//2+1):
                for Z0 in [7,11]:
                    Z=Jet(Z0)
                    value=sum(canceled_terms(d,a,q,Z),Jet(0))
                    assert value==original(d,a,q,Z+Z**-1)==transformed(d,a,q,Z)
                    generic+=1
                for j in range(a):
                    # The UNcanceled Sears denominator C Q^j is exactly one.
                    Z=(q*Q**(d+1-a+j))**-1
                    assert q*Z*Q**(d+1-a+j)==1
                    value=sum(canceled_terms(d,a,q,Z),Jet(0))
                    assert value==original(d,a,q,Z+Z**-1)
                    removable+=1
    for N in range(3,15):
        p,eta=root_field(N);q0=eta*eta%p;Jet.p=p;Jet.order=4
        q=Jet([q0*pow(math.factorial(k),-1,p)%p for k in range(4)])
        for Z in [Jet([1,1]),Jet(7)]:
            for a in range((N-1)//2+1):
                assert sum(canceled_terms(N-1,a,q,Z),Jet(0))==original(N-1,a,q,Z+Z**-1)
                germs+=1
    return dict(exact_generic_canceled_Sears_values=generic,
                exact_removable_spectral_denominator_cases=removable,
                exact_genuine_joint_four_jets=germs)


def numerical():
    mp.mp.dps=100;count=positive=0;worst=mp.mpf(0)
    for N in [16,17,32,33,64,65,129]:
        q=mp.exp(mp.pi*1j/N);a=(N-1)//2;d=N-1
        rootterms=canceled_terms(d,a,q,mp.mpf(1));p2=sum(rootterms)
        bs=[mp.mpf(1)]
        for r in range(1,a+1):bs.append(bs[-1]*mp.sin((r-mp.mpf('.5'))*mp.pi/N)/mp.sin(r*mp.pi/N))
        for k,T in enumerate(rootterms):
            assert abs(T-bs[k]**2*bs[a-k]**2)<mp.mpf('1e-90')
            positive+=1
        for rad in [mp.mpf('0.0001'),mp.mpf('.01'),mp.mpf('.05')]:
            scale=N*mp.sqrt(rad)*mp.log(2+1/rad)+mp.log(N)
            for phase in [1,-1,1j,-1j]:
                z=2+rad*phase;Z=(z+mp.sqrt(z*z-4))/2
                eps=mp.mpf('.01')*phase/N**3
                terms=canceled_terms(d,a,q*mp.exp(eps),Z)
                actual=sum(terms)
                assert abs(actual-original(d,a,q*mp.exp(eps),z))<mp.mpf('1e-60')*max(1,abs(actual))
                # The theorem bounds EACH term relative to its positive
                # endpoint value before summation, including genuine q motion.
                normalized=max(mp.log(max(1,abs(T/T0)))/scale for T,T0 in zip(terms,rootterms))
                assert normalized<5
                worst=max(worst,normalized);count+=1
    return dict(precision_digits=100,positive_original_endpoint_terms=positive,
                genuine_fixed_region_samples=count,max_normalized_term_growth=str(worst))


def main():
    result=dict(status='PASS',exact=exact(),diagnostics=numerical(),
                scope='Original canceled finite polynomial, actual removable spectral denominators and genuine q normals; absolute small-region upper bounds only. No zero-free fixed disk or contour contribution.')
    Path(__file__).with_name('actual_matching_edge_polynomial_closing_region_bound_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
