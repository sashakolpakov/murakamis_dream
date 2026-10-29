#!/usr/bin/env python3
"""Candidate positive Racah partition only; no original-source identity assumed."""
import itertools
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from audit_actual_two_cut_ports import balanced_data
from audit_exact_factorial_interpolation import sine_factorial
from audit_actual_trivalent_one_channel_source_packet import Jfun


def finite_candidate(N):
    p, eta, q, *_ = balanced_data(N)
    d, Q, im = N-1, q*q % p, pow(eta, N, p)
    f, sine = [1], [1]
    for a in range(1, N):
        f.append(f[-1]*(1-pow(Q, a, p)) % p)
        sine.append(pow(im,a,p)*pow(q,-a*(a+1)//2,p)*f[a] % p)
    count = 0
    for js in itertools.product(range(d//2+1), repeat=3):
        J, lo = sum(js), max(js)
        hi = J-lo
        first = second = 0
        for t in range(lo, hi+1):
            den = sine[d+t-J]
            den2 = 1
            for j in js:
                den = den*sine[t-j]*sine[J-j-t] % p
                den2 = den2*sine[t-j]*sine[J-j-t] % p
            first += N*sine[t]*pow(den,-1,p)
            second += sine[t]*sine[J-t]*pow(den2,-1,p)
        assert first % p == second % p
        if N % 2 and js[0] == d//2 and js[2] == d//2:
            m, j = d//2, js[1]
            positive = sum(sine[j+k]*pow(sine[j-k]*sine[k]**2,-1,p)*N*pow(sine[k]**2*sine[m-k]**2,-1,p) for k in range(j+1)) % p
            assert first % p == positive
        count += 1
    return {'N':N,'exact_candidate_reflection_triples':count,
            'odd_oneleg_partition_comparison': bool(N % 2),
            'source_identity_not_assumed':True}


def symbolic():
    x,y,z = sp.symbols('x y z')
    rows = [(x-y-z)/2,(-x+y-z)/2,(-x-y+z)/2,(x+y+z)/2]
    assert sp.expand(sum(r*r for r in rows)-x*x-y*y-z*z) == 0
    assert sp.expand(sum(r**3 for r in rows)-3*x*y*z) == 0
    gamma_cubic = sp.pi**2*(x**3+y**3+z**3-(x+y+z)**3)/6
    assert sp.expand(gamma_cubic+sp.pi**2*((x+y+z)**3-x**3-y**3-z**3)/6) == 0
    # Exact cotangent identity after sin/cos addition in three variables.
    a,b,c = sp.symbols('a b c', real=True)
    expr = sp.sin(a+b+c)*(sp.cos(a)*sp.sin(b)*sp.sin(c)
           +sp.sin(a)*sp.cos(b)*sp.sin(c)+sp.sin(a)*sp.sin(b)*sp.cos(c))
    expr -= sp.cos(a+b+c)*sp.sin(a)*sp.sin(b)*sp.sin(c)
    expr -= sp.sin(a+b)*sp.sin(a+c)*sp.sin(b+c)
    assert sp.trigsimp(sp.expand_trig(expr)) == 0
    return {'joint_action_Hessian_and_cubic':True,'exact_amplitude_trigonometric_identity':True}


def phi(sigmas):
    aa = [mp.mpf('.5')-s for s in sigmas]
    R = sum(aa)/2
    rr = [R-a for a in aa]
    return 2*(Jfun(R)-sum(Jfun(r) for r in rr))


def gamma(sigmas):
    return sum(Jfun(mp.mpf('.5')-s) for s in sigmas)-Jfun(mp.mpf('.5')-sum(sigmas))


def positive_partition(N, js):
    sine = [mp.mpf(1)]
    for r in range(1,N):
        sine.append(sine[-1]*2*mp.sin(mp.pi*r/N))
    J = sum(js)
    terms = []
    for t in range(max(js),J-max(js)+1):
        terms.append(sine[t]*sine[J-t]/mp.fprod(sine[t-j]*sine[J-j-t] for j in js))
    return sum(terms), terms


def laplace_profile(N):
    m = mp.mpf(N-1)/2
    triples = [(int(mp.floor(m)),)*3,
               tuple(int(mp.floor(m))-round(c*N) for c in (.03,.07,.10)),
               (int(mp.floor(m)),int(mp.floor(m))-round(.12*N),int(mp.floor(m)))]
    out = []
    for js in triples:
        actual, terms = positive_partition(N,js)
        sigmas = [(m-j)/N for j in js]
        predicted = N**mp.mpf('-1.5')*mp.exp(N*phi(sigmas))/(4*mp.sqrt(mp.fprod(mp.cos(mp.pi*s) for s in sigmas)))
        ratio = actual/predicted
        assert N*abs(ratio-1) < 4
        # Exact finite positivity/reflection; uniqueness may be a two-point coset maximum.
        assert all(t>0 for t in terms)
        assert max(abs(a/b-1) for a,b in zip(terms,terms[::-1])) < mp.mpf('1e-38')
        sine = [mp.mpf(1)]
        for r in range(1,N):
            sine.append(sine[-1]*2*mp.sin(mp.pi*r/N))
        normalizer = mp.fprod(sine[j] for j in js)/(N*sine[sum(js)-(N-1)])
        ceiling = 1 if N % 2 else mp.cos(mp.pi/N)
        assert normalizer <= ceiling*(1+mp.mpf('1e-40'))
        normal_error = N*abs(normalizer/mp.exp(N*gamma(sigmas))-1)
        assert normal_error < 4
        out.append({'labels':js,'normalized_prefactor':float(mp.re(ratio)),
                    'scaled_N_error':float(N*abs(ratio-1)),
                    'candidate_source_normalizer':float(normalizer),
                    'normalizer_scaled_N_error':float(normal_error)})
    return {'N':N,'all_parity_joint_profiles':out}


def complex_window(N):
    m = mp.mpf(N-1)/2
    sigma = [mp.mpc('.015','.006'),mp.mpc('.02','-.005'),mp.mpc('.01','.003')]
    js = [m-N*s for s in sigma]
    J = sum(js)
    total = 0
    for t in range(N):
        if abs(mp.mpf(t)/N-mp.mpf('.75')) > mp.mpf('.12'):
            continue
        total += sine_factorial(N,t)*sine_factorial(N,J-t)/mp.fprod(sine_factorial(N,t-j)*sine_factorial(N,J-j-t) for j in js)
    predicted = N**mp.mpf('-1.5')*mp.exp(N*phi(sigma))/(4*mp.sqrt(mp.fprod(mp.cos(mp.pi*s) for s in sigma)))
    error = N*abs(total/predicted-1)
    assert error < 4
    normalizer = mp.fprod(sine_factorial(N,j) for j in js)/(N*sine_factorial(N,sum(js)-(N-1)))
    normal_error = N*abs(normalizer/mp.exp(N*gamma(sigma))-1)
    assert normal_error < 4
    return {'N':N,'joint_canonical_Barnes_packet_scaled_N_error':float(error),
            'candidate_normalizer_complex_scaled_N_error':float(normal_error)}


def main():
    exact = [finite_candidate(N) for N in range(2,13)]
    algebra = symbolic()
    with mp.workdps(50):
        profiles = [laplace_profile(N) for N in (64,65,128,129)]
        complex_rows = [complex_window(N) for N in (17,33)]
    out = {'status':'PASS','exact_candidate_reflection':exact,'symbolic':algebra,
           'joint_Laplace_profiles':profiles,'complex_exact_windows':complex_rows,
           'scope':'Candidate positive partition geometry and asymptotic only. Actual-source scalar identity, magnetic/normal factors and sewn graph survival are separate.'}
    Path(__file__).with_name('actual_trivalent_candidate_racah_partition_geometry_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(f'PASS {len(exact)} exact candidate all-triple families, symbolic Hessian/cubic/amplitude, 4 all-parity joint profiles, 2 exact complex windows')


if __name__ == '__main__':
    main()
