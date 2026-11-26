#!/usr/bin/env python3
"""Original-matrix checks of the canonical polynomial and its full forcing."""

import argparse
import hashlib
import json
from pathlib import Path
import mpmath as mp

from check_even_reflected_casimir_insertions import apply_power, original_crossing


ROOT=Path(__file__).resolve().parents[1]


def multiply_linear(poly,constant,linear):
    out=[mp.mpc(0)]*(len(poly)+1)
    for j,a in enumerate(poly):
        out[j]+=constant*a
        out[j+1]+=linear*a
    return out


def evaluate(poly,z):
    return mp.polyval(poly[::-1],z)


def derivative(poly,z):
    return evaluate([j*poly[j] for j in range(1,len(poly))],z) if len(poly)>1 else mp.mpc(0)


def run(precision):
    mp.mp.dps=precision
    worst=mp.mpf(0)
    counts={}

    def check(name,a,b):
        nonlocal worst
        error=abs(a-b)/max(1,abs(a),abs(b))
        worst=max(worst,error)
        counts[name]=counts.get(name,0)+1
        if error>mp.mpf(10)**(-precision//2):
            raise ArithmeticError(f"{name}: {mp.nstr(error,12)}")

    for N in range(2,16):
        D=N-1
        M=original_crossing(N)
        e0=[mp.mpc(1)]+[mp.mpc(0)]*D
        for sign in (1,-1):
            q=mp.exp(sign*mp.pi*1j/N)
            Q=q*q
            kappa=mp.exp(sign*mp.pi*1j*D*D/(2*N))
            F=[mp.mpc(1)]
            S=[mp.mpf(1)]
            for k in range(1,N):
                F.append(F[-1]*(1-Q**k))
                S.append(S[-1]*2*mp.sin(mp.pi*k/N))
            alpha=apply_power(M,e0,3*sign)
            gamma=apply_power(M,alpha[::-1],sign)

            # The canonical H polynomial, constructed without M.
            H=[mp.mpc(0)]*N
            product=[mp.mpc(1)]
            for k in range(N):
                scalar=(-1)**k*Q**(k*(k+1)//2)/F[k]**2
                for j,a in enumerate(product):
                    H[j]+=scalar*a
                product=multiply_linear(product,1,-Q**k)
            G=[H[D-j]*Q**(D-j) for j in range(N)]
            check("constant_G",G[0],mp.mpf(1)/N**2)

            def transform(u):
                poly=[mp.mpc(0)]*N
                product=[mp.mpc(1)]
                for k in range(N):
                    scalar=q**(k*k)*u[D-k]/(N*kappa*F[k])
                    for j,a in enumerate(product):
                        poly[D-k+j]+=scalar*a
                    product=multiply_linear(product,-Q**(-k),1)
                return poly

            original_G=transform(alpha)
            for j in range(N):
                check("original_polynomial_coefficient",G[j],original_G[j])
            generic=[mp.mpc(j+1,mp.mpf(1)/(j+1)) for j in range(N)]
            generic_G=transform(generic)
            generic_gamma=apply_power(M,generic[::-1],sign)
            for j in range(N):
                prefactor=N*kappa*kappa*(-q**-1)**j
                check("original_physical_column",gamma[j],prefactor*evaluate(G,Q**-j))
                check("generic_physical_column",generic_gamma[j],
                      prefactor*evaluate(generic_G,Q**-j))

            # Exact leading scalar and full polynomial remainder.
            peak=max(range(N),key=lambda j:S[j]**2)
            h=[q**(j*(j+2))*S[j]**2 for j in range(N)]
            A=alpha[peak]/(kappa**3*h[peak])
            delta=[alpha[j]-kappa**3*A*h[j] for j in range(N)]
            error_G=transform(delta)
            main_G=[mp.mpc(0)]*N
            product=[mp.mpc(1)]
            for k in range(N):
                scalar=A*N*Q**(k*(k+1))/F[k]**3
                for j,a in enumerate(product):
                    main_G[D-k+j]+=scalar*a
                product=multiply_linear(product,1,-Q**k)
            for j in range(N):
                check("full_main_and_current",G[j],main_G[j]+error_G[j])
            for X in [mp.mpc(0),mp.mpc(1),mp.mpc(".2","-.3"),
                      mp.mpc("-.254366","-.577476"),Q]:
                Z=X
                forcing=mp.fsum(Z**(N-1-k)*Q**k for k in range(N))
                hleft=((Z-Q)*evaluate(H,Z/Q)-(3*Z-1-Q)*evaluate(H,Z)
                       -(Z-1)**2*evaluate(H,Q*Z))
                check("H_full_forcing",hleft,-Z*Z*forcing/N**2)
                gleft=((1-X/Q)**2*evaluate(G,X/Q)
                       +X*(3-(1+Q**-1)*X)*evaluate(G,X)
                       -Q*X*(1-X)*evaluate(G,Q*X))
                check("G_full_forcing",gleft,mp.fsum(X**k for k in range(N))/N**2)
                check("full_normal_decomposition",derivative(G,X),
                      derivative(main_G,X)+derivative(error_G,X))
            # Same integer values, different noninteger chirp lifts.
            x=mp.mpc(".316034718201632","-.073278930517287")
            if sign<0:
                x=mp.conj(x)
            X=mp.exp(-sign*2j*mp.pi*x)
            numerator=mp.exp(sign*(-1j*mp.pi+1j*mp.pi/N)*N*x)
            denominator=mp.exp(sign*(1j*mp.pi-1j*mp.pi/N)*N*x)
            check("retained_noninteger_chirp",numerator/denominator,X**(N-1))
        print(f"Checked canonical complex polynomial, both signs, N={N}.",flush=True)
    path=Path(__file__).resolve()
    dependency=path.with_name("check_even_reflected_casimir_insertions.py")
    return {
        "status":"passed","precision_decimal_digits":precision,
        "mpmath_version":mp.__version__,
        "exact_check_counts":counts,
        "maximum_relative_residual":mp.nstr(worst,30),
        "script_sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
        "dependency_sha256":{str(dependency.relative_to(ROOT)):
                            hashlib.sha256(dependency.read_bytes()).hexdigest()},
        "scope":"Finite original-source identities, full forcing and derivatives; no asymptotic claim tested.",
    }


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision",type=int,default=120)
    parser.add_argument("--output",type=Path,
                        default=ROOT/"repro/results/research-three-crossing-complex-polynomial.json")
    args=parser.parse_args()
    result=run(args.precision)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print(f"Saved {args.output}")
