#!/usr/bin/env python3
"""Scoped root-source and positive determinant checks; not a global proof."""
import argparse
import json
from pathlib import Path
import mpmath as mp


def literal_h(N, m, U, V):
    Q = mp.exp(2j * mp.pi / N)
    poch = [mp.mpc(1)]
    for r in range(1, m + 1):
        poch.append(poch[-1] * (1 - Q**r))
    pu, pv = [mp.mpc(1)], [mp.mpc(1)]
    for r in range(m):
        pu.append(pu[-1] * (U - Q**r))
        pv.append(pv[-1] * (V - Q**r))
    return mp.fsum(
        (-1)**k * Q**(k*(k+1)//2)
        * (poch[m] / (poch[k]*poch[m-k]))**2
        * V**k * pu[k] * pv[m-k] for k in range(m+1)
    )


def gaussian(N, a):
    Q = mp.exp(2j * mp.pi / N)
    return mp.fprod((1-Q**(a+r))/(1-Q**r) for r in range(1, a+1))


def coefficients(N, a, alpha, beta, da=0, db=0):
    theta = mp.pi / N
    diagonals, products, ddiag, dprod = [], [], [], []
    for n in range(a):
        scale = 1/(mp.cos(n*theta)*mp.cos((n+1)*theta))
        diagonals.append(1+(alpha+beta)*scale)
        ddiag.append((da+db)*scale)
        if n:
            sn, cn = mp.sin(n*theta), mp.cos(n*theta)
            B = sn**2/(cn**2*mp.sin((2*n-1)*theta)*mp.sin((2*n+1)*theta))
            products.append(B*((alpha+beta)**2*sn**2+(beta-alpha)**2*cn**2))
            dprod.append(2*B*((alpha+beta)*(da+db)*sn**2+(beta-alpha)*(db-da)*cn**2))
    return diagonals, products, ddiag, dprod


def logdet_trace(N, a, alpha, beta, da=0, db=0):
    diag, product, ddiag, dprod = coefficients(N, a, alpha, beta, da, db)
    if not a:
        return mp.mpc(0), mp.mpc(0)
    piv, dpiv = diag[0], ddiag[0]
    value, derivative = mp.log(piv), dpiv/piv
    for n in range(1, a):
        new = diag[n]-product[n-1]/piv
        dnew = ddiag[n]-dprod[n-1]/piv+product[n-1]*dpiv/piv**2
        piv, dpiv = new, dnew
        value += mp.log(piv)
        derivative += dpiv/piv
    return value, derivative


def matrix(N, a, alpha, beta):
    theta = mp.pi/N
    M = mp.eye(a)
    for n in range(a):
        M[n,n] += (alpha+beta)/(mp.cos(n*theta)*mp.cos((n+1)*theta))
        if n:
            sn, cn = mp.sin(n*theta), mp.cos(n*theta)
            B = sn**2/(cn**2*mp.sin((2*n-1)*theta)*mp.sin((2*n+1)*theta))
            M[n-1,n] = mp.sqrt(B)*((alpha+beta)*sn+1j*(beta-alpha)*cn)
            M[n,n-1] = mp.sqrt(B)*((alpha+beta)*sn-1j*(beta-alpha)*cn)
    return M


def rate(xi, alpha, beta):
    if not xi:
        return mp.mpf(0)
    def integrand(t):
        c = mp.cos(mp.pi*t)
        D = 1+(alpha+beta)/c**2
        gap = mp.sqrt(1+(2*(alpha+beta)+4*alpha*beta)/c**2)
        return mp.log((D+gap)/2)
    cuts = [mp.mpf(0)]
    cuts += [x for x in map(mp.mpf, ['.25','.4','.48']) if x < xi]
    cuts.append(xi)
    return mp.quad(integrand, cuts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', default='experiments/actual_q_hahn_negative_clock_boundary_results.json')
    args = ap.parse_args()
    mp.mp.dps = 90
    params = [(mp.mpf('.25'),mp.mpf('.25')),
              (mp.mpf('1.5'),mp.mpf('.7')),
              (mp.mpf('.4'),mp.mpf('2'))]
    source_errors, matrix_errors, partner_errors = [], [], []
    for N in [3,4,7,10,15,18]:
        q, Q = mp.exp(1j*mp.pi/N), mp.exp(2j*mp.pi/N)
        for a in sorted(set([0,1,(N-1)//2])):
            for alpha,beta in params:
                X,Y = -2*alpha,-1/(2*beta)
                U,V = X/q,Y/q
                ld,_ = logdet_trace(N,a,alpha,beta)
                expected = V**a*gaussian(N,a)*mp.exp(ld)
                literal = literal_h(N,a,U,V)
                err = abs(literal-expected)/max(1,abs(literal))
                assert err < mp.mpf('1e-72')
                source_errors.append(float(err))
                if a:
                    M = matrix(N,a,alpha,beta)
                    err = abs(mp.det(M)-mp.exp(ld))/max(1,abs(mp.det(M)))
                    assert err < mp.mpf('1e-75')
                    matrix_errors.append(float(err))
                m=N-1-a
                forced=mp.fprod(U*V-Q**r for r in range(a,m))
                large=literal_h(N,m,U,V)
                err=abs(large-literal*forced)/max(1,abs(large))
                assert err < mp.mpf('1e-70')
                partner_errors.append(float(err))

    perturbations=[]
    direct_trace_errors=[]
    for N in [16,33,64,129,256,513]:
        for a in [N//3,(N-1)//2]:
            for alpha,beta in params:
                em=mp.mpc('.4','.2')/N
                ep=mp.mpc('-.3','.15')/N
                eta=abs(em)+abs(ep)
                ld,tr=logdet_trace(N,a,alpha,beta,alpha*em,beta*ep)
                lp,_=logdet_trace(N,a,alpha*(1+em),beta*(1+ep))
                bound=a*eta**2/(2*(1-eta))
                remainder=abs(lp-ld-tr)
                assert remainder <= bound*(1+mp.mpf('1e-65'))
                assert abs(lp-ld) <= -a*mp.log(1-eta)*(1+mp.mpf('1e-65'))
                perturbations.append({'N':N,'a':a,'remainder_over_bound':float(remainder/bound),'N_remainder':float(N*remainder)})
                if N==16:
                    M=matrix(N,a,alpha,beta)
                    Delta=matrix(N,a,alpha*em,beta*ep)-mp.eye(a)
                    direct=mp.trace(M**-1*Delta) if hasattr(mp,'trace') else sum((M**-1*Delta)[i,i] for i in range(a))
                    err=abs(direct-tr)
                    assert err<mp.mpf('1e-72')
                    direct_trace_errors.append(float(err))

    rates=[]
    for alpha,beta in params:
        for fraction in map(mp.mpf,['.27','.42','.5']):
            for N in [48,96,192,384]:
                a=min(int(mp.floor(fraction*N)),(N-1)//2)
                ld,_=logdet_trace(N,a,alpha,beta)
                predicted=rate(mp.mpf(a)/N,alpha,beta)
                error=abs(ld/N-predicted)
                assert error<mp.mpf('.3')
                rates.append({'N':N,'a':a,'absolute_rate_error':float(error),'N_over_logN_error':float(N*error/mp.log(N))})

    tails=[]
    for N in [33,64,129,256,513]:
        a=(N-1)//2
        for alpha,beta in params:
            ld,_=logdet_trace(N,a,alpha,beta)
            diag,_,_,_=coefficients(N,a,alpha,beta)
            for h in sorted(set([1,max(1,N//20),max(1,N//8)])):
                bulk,_=logdet_trace(N,a-h,alpha,beta)
                upper=mp.fsum(mp.log(z) for z in diag[a-h:])
                assert mp.re(ld-bulk)>=-mp.mpf('1e-70')
                assert mp.re(ld-bulk)<=upper+mp.mpf('1e-70')
                tails.append(float(mp.re(ld-bulk)/upper))

    result={'status':'PASS','precision_digits':mp.mp.dps,
            'literal_source_determinant_comparisons':len(source_errors),
            'independent_dense_determinants':len(matrix_errors),
            'actual_large_partner_checks':len(partner_errors),
            'relative_trace_transport_checks':len(perturbations),
            'independent_dense_trace_checks':len(direct_trace_errors),
            'fold_rate_diagnostics':len(rates),'positive_Schur_tail_checks':len(tails),
            'max_source_relative_error':max(source_errors),
            'max_large_partner_error':max(partner_errors),
            'max_transport_remainder_over_bound':max(r['remainder_over_bound'] for r in perturbations),
            'max_rate_N_over_logN_error':max(r['N_over_logN_error'] for r in rates),
            'rates':rates,'relative_transport':perturbations,
            'scope':'Root numerator, exact scalar and partner checks, retained finite-clock trace correction and leading-rate diagnostics. Written proof supplies the theorem; no genuine quantum normals or global period tested.'}
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('rates','relative_transport')},indent=2))


if __name__=='__main__':
    main()
