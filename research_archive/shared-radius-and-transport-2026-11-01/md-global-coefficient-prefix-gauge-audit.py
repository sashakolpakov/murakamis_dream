#!/usr/bin/env python3
"""Bounded checks of the full-numerator prefix-gauge comparison.

Exact finite-field matrix powers are compared with a separate free-Green
expansion.  Real inequality checks are diagnostics at 80 decimal digits;
the all-level inequalities are proved in the companion note.
"""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import mpmath as mp


SOURCE = Path("/private/tmp/md-shifted-cyclic-excursion-audit.py")
spec = importlib.util.spec_from_file_location("literal_source_audit", SOURCE)
literal = importlib.util.module_from_spec(spec)
spec.loader.exec_module(literal)


def green(N, i, sigma, diagonal, double, modulus=None):
    """Homogeneous x-degree arrays from the positive free-Green formula."""
    out = [[1]]
    for k in range(1, N-i):
        row = [1] * (k+1)
        for r in range(2, k+1):
            denominator = double[i+r]
            a = ((diagonal[0]-sigma) * pow(denominator, -1, modulus)
                 if modulus else (diagonal[0]-sigma)/denominator)
            for p in range(k-r+1):
                for t, value in enumerate(out[r-2]):
                    row[p+t+1] += a*value
        if modulus:
            row = [v % modulus for v in row]
        out.append(row)
    return out


def exact_checks():
    cases, coefficients = [], 0
    for N in (2, 3, 4, 7, 8, 12):
        for lower in (1009, 5003):
            prime, q = literal.finite_field(N, lower)
            qp = lambda r: pow(q, r % (2*N), prime)
            c = [(qp(2*r+1)+qp(-2*r-1)) % prime for r in range(N)]
            ss = [(2-qp(2*r)-qp(-2*r)) % prime for r in range(N)]
            double = [(c[0]-c[r-1]) % prime if r else 0
                      for r in range(N)]
            beta = (-2-pow(N*N, -1, prime)) % prime
            for sigma in (-2, 0, 1, 2, beta):
                direct = literal.numerator_from_matrix(N, sigma, prime, q)
                U = [1]
                for value in c:
                    U.append(U[-1]*(sigma-value) % prime)
                count = 0
                for i in range(N):
                    H = green(N, i, sigma, c, double, prime)
                    steps = 1
                    for j in range(i, N):
                        if j > i:
                            steps = steps*ss[j] % prime
                        k = j-i
                        factor = U[i]*U[N-1-j]*(-1)**k*steps
                        for p, value in enumerate(H[k]):
                            predicted = factor*value % prime
                            actual = direct.get((i,j,p,k-p),0)
                            assert predicted == actual
                            count += 1
                coefficients += count
                cases.append({"N":N,"prime":prime,"q":q,
                              "sigma_residue":sigma % prime,
                              "coefficients":count})
    return {"cases":len(cases),"coefficients":coefficients,"details":cases}


def product_jet(values):
    value, derivative = mp.mpf(1), mp.mpf(0)
    for a in values:
        value, derivative = value*a, derivative*a+value
    return value, derivative


def endpoint_arrays(N, i, a, ss, double):
    """Positive raw interval continuant and its first u-normal at zero."""
    values, derivatives = [[mp.mpf(1)]], [[mp.mpf(0)]]
    for k in range(1,N-i):
        j = i+k
        row, jet = [mp.mpf(0)]*(k+1), [mp.mpf(0)]*(k+1)
        for p,v in enumerate(values[-1]):
            row[p] += ss[j]*v
            row[p+1] += ss[j]*v
            jet[p] += ss[j]*derivatives[-1][p]
            jet[p+1] += ss[j]*derivatives[-1][p]
        if k >= 2:
            for p,v in enumerate(values[-2]):
                row[p+1] += double[j]*a[j-1]*v
                jet[p+1] += double[j]*(v+a[j-1]*derivatives[-2][p])
        values.append(row)
        derivatives.append(jet)
    return values, derivatives


def real_checks():
    mp.mp.dps=80
    endpoint_count=tail_count=gauge_count=0
    max_endpoint=mp.mpf(0)
    max_tail=mp.mpf(0)
    max_complement=mp.mpf(0)
    for N in (2,3,4,7,8,12):
        nu=mp.mpf(1)/(N*N)
        beta=-2-nu
        c=[2*mp.cos((2*r+1)*mp.pi/N) for r in range(N)]
        if N % 2:
            c[(N-1)//2]=mp.mpf(-2)
        if N == 2:
            c=[mp.mpf(0)]*2
        a=[2+x for x in c]
        ss=[4*mp.sin(mp.pi*r/N)**2 for r in range(N)]
        double=[4*mp.sin(mp.pi*r/N)*mp.sin(mp.pi*(r-1)/N)
                for r in range(N)]
        spectra=[mp.mpf(-2),-mp.mpf(7)/4,mp.mpf(0),
                 mp.sqrt(3),c[0],mp.mpf(2)]
        for i in range(N):
            Hbeta=green(N,i,beta,c,double)
            endpoint, derivative=endpoint_arrays(N,i,a,ss,double)
            steps=mp.mpf(1)
            for j in range(i,N):
                if j > i:
                    steps *= ss[j]
                k=j-i
                unused=a[:i]+a[j+1:]
                uv,uj=product_jet(unused)
                base=mp.fprod(v+nu for v in unused)
                for p,hb in enumerate(Hbeta[k]):
                    at_beta=base*steps*hb
                    first=(uv*endpoint[k][p]
                           +nu*(uj*endpoint[k][p]+uv*derivative[k][p]))
                    assert first > 0
                    ratio=at_beta/first
                    assert ratio <= 2+mp.mpf("1e-60")
                    max_endpoint=max(max_endpoint,ratio)
                    endpoint_count+=1
            for sigma in spectra:
                H=green(N,i,sigma,c,double)
                for row,reference in zip(H,Hbeta):
                    for value,ref in zip(row,reference):
                        ratio=abs(value)/ref
                        assert ratio <= 1+mp.mpf("1e-60")
                        max_tail=max(max_tail,ratio)
                        tail_count+=1
        for sigma in spectra:
            G=[mp.mpf(1)]
            for r in range(N):
                G.append(G[-1]*abs(sigma-c[r])/(a[r]+nu))
            for i in range(N):
                ratio=G[i]*G[N-1-i]/(N*N)
                assert ratio <= 5+mp.mpf("1e-60")
                max_complement=max(max_complement,ratio)
                gauge_count+=1
    return {"decimal_digits":80,"endpoint_jet_coefficients":endpoint_count,
            "tail_coefficient_comparisons":tail_count,
            "complementary_gauge_comparisons":gauge_count,
            "largest_endpoint_jet_ratio":mp.nstr(max_endpoint,25),
            "largest_tail_ratio":mp.nstr(max_tail,25),
            "largest_complementary_ratio_divided_by_N_squared":mp.nstr(max_complement,25)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,
                        default=Path(__file__).with_name("md-global-coefficient-prefix-gauge-results.json"))
    args=parser.parse_args()
    result={"status":"passed","exact":exact_checks(),"real_diagnostics":real_checks(),
            "scope":"Exact finite-field checks compare literal polynomial matrix powers with the independent free-Green expression. Finite 80-digit inequalities are diagnostics, not all-level proofs. No sewn source gap or filling asymptotic is tested.",
            "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "literal_builder_sha256":hashlib.sha256(SOURCE.read_bytes()).hexdigest()}
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"status":result["status"],"exact_cases":result["exact"]["cases"],
                      "exact_coefficients":result["exact"]["coefficients"],
                      "real_diagnostics":result["real_diagnostics"],"output":str(args.output)}))


if __name__=="__main__":
    main()
