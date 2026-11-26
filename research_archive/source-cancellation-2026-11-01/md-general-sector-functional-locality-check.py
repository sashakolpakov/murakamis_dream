#!/usr/bin/env python3
"""Bounded checks of the one-sided full-Hermite locality obstruction.

Exact algebra at selected levels checks polynomial and functional identities.
The separate high-precision values are diagnostics for an analytically proved
limit. Neither part verifies a closed-diagram source or an asymptotic theorem.
"""
from pathlib import Path
import hashlib
import json
import sympy as s
import mpmath as mp

if not __debug__:
    raise SystemExit("Run without -O: exact checks use assertions.")

z = s.Symbol("z")
exact = []
for N in [2, 3, 4, 5, 6, 8]:
    m, d = N // 2, N - 1
    q_expr = s.exp(s.pi * s.I / N)
    field = s.QQ.algebraic_field(q_expr)
    q = field.from_sympy(q_expr)
    chi = s.Poly(2*s.chebyshevt(N,z/2)+2,z,domain=field)
    B = s.Poly(2*s.chebyshevt(m,z/2) if N%2==0 else
               s.chebyshevu(m,z/2)-s.chebyshevu(m-1,z/2),
               z,domain=field)
    Z = B if N%2==0 else B*s.Poly(z+2,z,domain=field)
    H = Z*s.Poly((z+2)**(m-1)/4**(m-1),z,domain=field)
    assert Z*B == chi
    assert H.degree() == d
    HP, BP = H.diff(), B.diff()
    def evaluate(poly, point):
        acc = field.zero
        for coeff in poly.rep.to_list():
            acc = acc*point+coeff
        return acc
    reconstruction = s.Poly(0,z,domain=field)
    alphas, nodes = [], []
    for a in range(m):
        c = q**(2*a+1)+q**(-(2*a+1))
        assert evaluate(B,c) == field.zero
        assert evaluate(H,c) == field.zero
        alpha = ((c+2)/4)**(m-1)/evaluate(BP,c)
        basis, rem = chi.div(s.Poly(z-field.to_sympy(c),z,domain=field))
        assert rem.is_zero
        reconstruction += basis.mul_ground(field.to_sympy(alpha))
        # Independent repeated-node recovery, with no partial fractions.
        assert (4-c*c)*evaluate(HP,c)/(N*N) == alpha
        alphas.append(alpha)
        nodes.append(c)
    assert reconstruction == H
    assert H.eval(-2)==0 or N in [2]
    if N%2:
        assert H.eval(-2)==0  # odd simple-root contribution
    for n in [-3, 1, 5]:
        derivative_sum = field.zero
        diagonal_sum = field.zero
        for a,(alpha,c) in enumerate(zip(alphas,nodes)):
            # Remove only the common unit lift q^(n*d*d/2).
            phase = (-1)**(a*n)*q**(n*a*(a+1))
            derivative_sum += (4-c*c)*evaluate(HP,c)*phase/(N*N)
            diagonal_sum += alpha*phase
        assert derivative_sum == diagonal_sum
        exact.append({"N":N,"n":n,"identity":"normal recovery equals literal diagonal mixture"})
    # Vanishing order, including the parity-dependent extra endpoint root.
    order = m-1+(N%2)
    for k in range(order):
        assert H.diff((z,k)).eval(-2)==0
    assert H.diff((z,order)).eval(-2)!=0

mp.mp.dps = 70
diagnostics = []
for N in [32, 33, 64, 65, 128, 129]:
    m, d = N//2, N-1
    for n in [1, -3]:
        phis = [(2*a+1)*mp.pi/N for a in range(m)]
        # The first expression uses the original Gaussian and direct Z' weights.
        original = mp.mpc(0)
        lifted_phase = mp.exp(mp.pi*1j*n*d*d/(4*N))
        for a,phi in enumerate(phis):
            alpha=(2 if N%2==0 else 4)/mp.mpf(N)*(-1)**a*mp.sin(phi)*mp.cos(phi/2)**(N-2)
            original += alpha*lifted_phase*mp.exp(1j*n*N*(phi-mp.pi)**2/(4*mp.pi))
        xi=lifted_phase*mp.exp(1j*n*N*mp.pi/4-1j*n*mp.pi/2)
        folded=mp.fsum(mp.sin(phi)*mp.cos(phi/2)**(N-2)
                      *mp.exp(1j*n*N*phi**2/(4*mp.pi)) for phi in phis)
        kappa=2 if N%2==0 else 4
        assert abs(original-xi*kappa*folded/N)<mp.mpf("1e-60")
        target=2/(mp.pi-2j*n)
        diagnostics.append({
            "N":N,"n":n,
            "sum_real":mp.nstr(folded.real,24),
            "sum_imag":mp.nstr(folded.imag,24),
            "distance_from_proved_limit":mp.nstr(abs(folded-target),12),
        })

out = {
    "scope":__doc__.strip(),
    "exact_levels":[2,3,4,5,6,8],
    "exact_functional_cases":exact,
    "exact_polynomial_checks":["Chebyshev factorization","degree N-1",
        "node values","partial fraction identity","repeated-node normal",
        "odd simple-root value","endpoint vanishing order"],
    "numerical_diagnostics_only":diagnostics,
    "excluded_claims":["closed-source realization","uniform asymptotics from samples",
        "hyperbolic volume equality","global source gap"],
    "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "sympy_version":s.__version__,
    "mpmath_version":mp.__version__,
}
path=Path("/private/tmp/md-general-sector-functional-locality-check-results.json")
path.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"exact_cases":len(exact),"diagnostics":len(diagnostics),"output":str(path)},indent=2))
