#!/usr/bin/env python3
"""Exact rational identities used in the bounded Casimir/crossing audit.
No sampled levels, asymptotic bounds, or global source claims are checked.
"""
import hashlib
import json
from pathlib import Path
import sympy as s

q, I, K, L, U, V = s.symbols('q I K L U V', nonzero=True)
Q = q*q
J = I*K*L
c = lambda Z: q*Z + 1/(q*Z)
b = lambda Z: 2-Z-1/Z
e = lambda Z: q+1/q-q/Z-Z/q
lhs = c(I)-b(Q*I)*q*I*(2-K-L)/(1-Q*I)-e(Q**2*I)*Q**2*I**2*(1-K)*(1-L)/((1-Q*I)*(1-Q**2*I))
rhs = c(J)+b(J)/q*(2-K-L)/(1-J)-e(J)/Q*(1-K)*(1-L)/((1-J)*(1-J/Q))
checks = {'auxiliary_crossing_commutator_cleared_numerator': s.cancel(lhs-rhs)}
x, y = -q*U, -1/(q*V)
Ap = (1/V-1)*(1-Q*U)
Am = (1/(Q*V)-1)*(1-U)
D = 2*q*U+2/(q*V)-(q+1/q)*U/V
checks['physical_positive_shift'] = s.cancel(-(1+q*(x+y)+q*q*x*y)/q-Ap/q)
checks['physical_negative_shift'] = s.cancel(-q*(1+(x+y)/q+x*y/(q*q))-q*Am)
checks['physical_diagonal'] = s.cancel(2*(x+y)+(q+1/q)*x*y+D)
N, a, j, k = s.symbols('N a j k', integer=True)
d = N-1
checks['gaussian_value_exponent_difference'] = s.expand((d*d+(d-2*a)**2)/4-d*d/2-a*(a+1)+a*N)
H = lambda z: d-2*z
checks['self_dual_R_cartan_exponent'] = s.expand((H(j)*H(k)-H(j+a)*H(k-a))/2-2*a*(j-k+a))
assert all(v == 0 for v in checks.values()), checks
result = {
    'scope': __doc__.strip(),
    'identities': {name: 'identically zero after exact rational simplification' for name in checks},
    'number_of_identities': len(checks),
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'sympy_version': s.__version__,
    'not_checked': ['root-level matrix reconstruction', 'all manuscript results', 'global source bounds', 'asymptotic or geometric claims'],
}
out = Path('/private/tmp/md-casimir-crossing-symbolic-check-results.json')
out.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
