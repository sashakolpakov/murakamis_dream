#!/usr/bin/env python3
"""Bounded exact checks of actual adjacent source boundary currents.

Build the original bidiagonal Casimir and its full Chebyshev resolvent
numerator by matrix powers. Compare the actual central a^m t^(d-m)
coefficient, protected coefficients, and inverse-current formula.
These tests do not bound the closed R54 source or its filled period.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import sympy as sp


def check_level(N):
    z, r = sp.symbols('z r')
    F = sp.QQ.algebraic_field(sp.CRootOf(sp.cyclotomic_poly(2*N, r), 0))
    q, zero, one = F.unit, F.zero, F.one
    d, m = N-1, N//2
    nodes = [q**(2*j+1)+q**(-2*j-1) for j in range(N)]
    sq = [2-q**(2*j)-q**(-2*j) for j in range(N+1)]
    C = [[zero for _ in range(N)] for _ in range(N)]
    for j in range(N):
        C[j][j] = nodes[j]
        if j: C[j-1][j] = -sq[j]
    I = [[one if i == j else zero for j in range(N)] for i in range(N)]
    powers = [I]
    for _ in range(N-1):
        A = powers[-1]
        powers.append([[sum((A[i][k]*C[k][j] for k in range(N)), zero)
                        for j in range(N)] for i in range(N)])
    chi = sp.Poly(2*sp.chebyshevt(N,z/2)+2,z)
    h = [F.convert(chi.nth(k)) for k in range(N+1)]
    def V0j(j, sigma):
        return sum((h[k]*sum((sigma**ell*powers[k-ell-1][0][j]
                             for ell in range(k)), zero)
                    for k in range(1,N+1)), zero)
    K = V0j(m, F.convert(-2))
    expected = F.convert(N*N) if N%2 else -F.convert(4*N)/(2-nodes[0])
    assert K == expected and K
    counts = Counter(actual_central_boundary_coefficients=1)
    v = [V0j(j, F.convert(2)) for j in range(m)]
    for j0 in range(1,m):
        B = [zero]*N
        B[d-j0] = K
        assert B[d] == B[d-m] == zero
        direct_pair = sum((v[j]*B[d-j] for j in range(m)), zero)
        assert direct_pair == K*v[j0] and direct_pair
        A = []
        for k in range(N):
            A.append((B[k]-(sq[k]*A[k-1] if k else zero))/(2-nodes[k]))
        current = 4*A[d]+F.convert(4*N*(-1)**(m-1))*A[d-m]
        assert current == direct_pair
        counts['nonzero_actual_pairs_with_zero_raw_endpoints'] += 1
        counts['inverse_current_equalities'] += 1
    return dict(counts)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('md-protected-left-adjacent-transport-results.json'))
    args = parser.parse_args()
    if not __debug__: raise SystemExit('Do not run with -O')
    cases = {str(N): check_level(N) for N in (4,5,6,7,8)}
    result = {'status':'passed','levels':[4,5,6,7,8], 'checks':cases,
              'arithmetic':'exact cyclotomic fields',
              'construction':'Original bidiagonal Casimir powers and full Chebyshev polynomial quotient, before selecting the central coefficient.',
              'scope':'Finite adjacent-source identities and nonzero local boundary-sector obstruction, both parities.',
              'limits':'No closed R54 realization of the prescribed exterior monomial is asserted. No exponential source or filled-period bound is tested.',
              'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'levels':result['levels'],'output':str(args.output)}))


if __name__ == '__main__': main()
