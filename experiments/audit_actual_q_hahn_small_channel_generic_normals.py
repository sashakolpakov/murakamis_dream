"""Focused audit of the ORIGINAL small-channel generic-q deformation.

Finite-field dual numbers compare values and genuine q derivatives before
root simplification. Complex checks retain the original highest-vector
ratio independently of the generic determinant. These are regressions;
the polynomial-radius bound is proved in the accompanying note.
"""
import json
from pathlib import Path
import mpmath as mp
from audit_actual_two_cut_ports import balanced_data


class Dual:
    p = 1000000007

    def __init__(self, a=0, b=0):
        if isinstance(a, Dual):
            self.a, self.b = a.a, a.b
        else:
            self.a, self.b = int(a) % self.p, int(b) % self.p

    def __add__(self, other):
        o = Dual(other)
        return Dual(self.a+o.a, self.b+o.b)
    __radd__ = __add__

    def __neg__(self):
        return Dual(-self.a, -self.b)

    def __sub__(self, other):
        return self + -Dual(other)

    def __rsub__(self, other):
        return Dual(other) + -self

    def __mul__(self, other):
        o = Dual(other)
        return Dual(self.a*o.a, self.a*o.b+self.b*o.a)
    __rmul__ = __mul__

    def __pow__(self, n):
        a = pow(self.a, int(n), self.p)
        return Dual(a, int(n)*pow(self.a, int(n)-1, self.p)*self.b)

    def __truediv__(self, other):
        return self * Dual(other)**-1

    def __rtruediv__(self, other):
        return Dual(other) * self**-1

    def __eq__(self, other):
        o = Dual(other)
        return (self.a, self.b) == (o.a, o.b)


def prod(seq):
    out = 1
    for a in seq:
        out *= a
    return out


def poch(a, Q, n):
    return prod(1-a*Q**r for r in range(n))


def gauss(Q, n, k):
    return poch(Q, Q, n)/poch(Q, Q, k)/poch(Q, Q, n-k)


def original_column(N, q, t, j, u):
    """The original generic highest-vector ratio; no root complementation."""
    Q, x, v = q*q, q**(N-1), t-u
    F = [poch(Q, Q, k) for k in range(N)]
    return sum((-1)**a*x**(u-2*a)*Q**(a*v+a*(a-1)//2)
               *F[N-j+a-1]*F[N-a-1]/F[N-j-1]/F[N-1]
               *gauss(Q, u, a)*gauss(Q, v, j-a)/gauss(Q, t, j)
               for a in range(max(0, j-v), min(j, u)+1))


def source_S(N, q, j, U, T):
    Q, B = q*q, q**(-2*N)
    return sum((-1)**a*B**a*Q**(a*(a+1)//2)*gauss(Q, j, a)
               *poch(B*Q**(j-a+1), Q, a)/poch(B*Q, Q, a)*T**a
               *prod(U-Q**r for r in range(a))
               *prod(T-U*Q**r for r in range(j-a))
               for a in range(j+1))


def scalar_K(N, q, j):
    Q, B = q*q, q**(-2*N)
    return poch(B*B*Q**(j+1), Q, j)/poch(B*Q, Q, j)


def jacobi(N, q, s, J):
    Q, B = q*q, q**(-2*N)
    A = 1/B
    lam = lambda n: A*Q**(-n)+B*Q**(n+1)
    b = lambda n: ((1+A)+Q*s*s*(1+B)-Q**(-n)*(Q*s*s+A)
                   -Q**n*(B*Q*s*s+1))/s
    d = lambda n: Q**(1-n)+Q**n-1-Q
    u = [0]+[b(n)/(lam(n)-lam(n-1)) for n in range(1, J+1)]
    v = [0]*(J+1)
    for n in range(2, J+1):
        v[n] = (b(n-1)*u[n]+d(n))/(lam(n)-lam(n-2))
    alpha = [u[n+1]-u[n] for n in range(J)]
    beta = [0]+[v[n+1]-v[n]-alpha[n]*u[n] for n in range(1, J)]
    return alpha, beta


def determinant(N, q, s, j, z):
    if j == 0:
        return 1
    alpha, beta = jacobi(N, q, s, j)
    prev, now = 1, z+alpha[0]
    for n in range(1, j):
        prev, now = now, (z+alpha[n])*now+beta[n]*prev
    return now


def det_column(N, q, t, j, u):
    s, U, T = q**t, q**(2*u), q**(2*t)
    return (q**((N-1)*u+j*t)*scalar_K(N, q, j)
            *determinant(N, q, s, j, s/U)
            /prod(T-q**(2*r) for r in range(j)))


def exact_checks():
    counts = dict(original_generic_value_and_normal=0,
                  generic_source_determinants=0, generic_Casimir_values=0,
                  Vandermonde_values_and_normals=0, root_original_normals=0)
    # Non-root q tests verify the deformation, not its specialized formula.
    for N in range(3, 15):
        for qval in (2, 5):
            Dual.p = 1000000007
            q = Dual(qval, qval)
            Q = q*q
            for j in range((N-1)//2+1):
                for sval in (17, 37):
                    s, U = Dual(sval), Dual(11)
                    T = s*s
                    K = scalar_K(N, q, j)
                    assert source_S(N, q, j, 0, T) == T**j*K
                    counts['Vandermonde_values_and_normals'] += 1
                    z = s/U
                    assert source_S(N, q, j, U, T)*z**j == (
                        s**(2*j)*K*determinant(N, q, s, j, z))
                    counts['generic_source_determinants'] += 1
                    B, A = q**(-2*N), q**(2*N)
                    residual = (Q**(-j)*(Q*U-A)*(U-T)*source_S(N,q,j,Q*U,T)
                                +Q**j*(B*Q*T-U)*(1-U)*source_S(N,q,j,U/Q,T)
                                +((1+A)*U+Q*T*(1+B)*U-(1+Q)*U*U
                                  -T*(A*Q**(-j)+B*Q**(j+1)))
                                *source_S(N,q,j,U,T))
                    assert residual == 0
                    counts['generic_Casimir_values'] += 1
                for t in range(N-1-j, N):
                    for u in sorted(set((0, t//3, t//2, t))):
                        assert original_column(N,q,t,j,u) == det_column(N,q,t,j,u)
                        counts['original_generic_value_and_normal'] += 1
    # Independent root prime fields compare ORIGINAL q jets, not a root
    # squared-binomial differentiation.
    for N in range(3, 16):
        p, _, qval, *_ = balanced_data(N)
        Dual.p = p
        q = Dual(qval, qval)
        for j in range((N-1)//2+1):
            for t in sorted(set((N-1-j, N-1))):
                for u in range(t+1):
                    assert original_column(N,q,t,j,u) == det_column(N,q,t,j,u)
                    counts['root_original_normals'] += 1
    return counts


def complex_original(N, q, t, j, u):
    """Literal finite generic source, independently normalized by binomials."""
    Q, x = q*q, q**(N-1)
    def binom(top, k):
        return prod((1-q**(2*(top-r)))/(1-Q**(r+1)) for r in range(k))
    return mp.fsum((-1)**a*x**(u-2*a)*Q**(a*(t-u)+a*(a-1)/2)
                   *poch(Q**(N-j),Q,a)/poch(Q**(N-a),Q,a)
                   *binom(u,a)*binom(t-u,j-a)/binom(t,j)
                   for a in range(j+1))


def complex_checks():
    mp.mp.dps = 100
    counts = dict(complex_generic_source_comparisons=0,
                  genuine_root_normal_comparisons=0,
                  polynomial_disk_samples=0)
    max_exact, max_normal = mp.mpf(0), mp.mpf(0)
    max_disk, max_scaled_normal = mp.mpf(0), mp.mpf(0)
    for N in (16, 17, 32, 33, 64, 65):
        for j in sorted(set((int(mp.mpf('.3')*N), (N-1)//2))):
            for tau, nu in ((mp.mpc('.79','.035'),mp.mpc('.37','-.021')),
                            (mp.mpc('.68','-.027'),mp.mpc('.45','.013'))):
                t, u = N*tau, N*nu
                q0 = mp.exp(mp.pi*1j/N)
                base = det_column(N,q0,t,j,u)
                for eps in (mp.mpc('.00001','.00002')/N,
                            mp.mpc('-.00002','.00001')/N):
                    q = q0*mp.exp(eps)
                    direct, value = complex_original(N,q,t,j,u), det_column(N,q,t,j,u)
                    err = abs(direct/value-1)
                    max_exact = max(max_exact, err)
                    assert err < mp.mpf('1e-75'), (N,j,'source',err)
                    counts['complex_generic_source_comparisons'] += 1
                d_direct = mp.diff(lambda e: complex_original(N,q0*mp.exp(e),t,j,u), 0)
                d_det = mp.diff(lambda e: det_column(N,q0*mp.exp(e),t,j,u), 0)
                err = abs(d_direct-d_det)/max(abs(base),abs(d_direct))
                max_normal = max(max_normal,err)
                assert err < mp.mpf('1e-75'), (N,j,'normal',err)
                max_scaled_normal = max(max_scaled_normal,abs(d_direct/base)/N**2)
                counts['genuine_root_normal_comparisons'] += 1
                for phase in (0, mp.pi/2, mp.pi, 3*mp.pi/2):
                    eps = mp.mpf('.1')*N**-8*mp.exp(1j*phase)
                    ratio = abs(det_column(N,q0*mp.exp(eps),t,j,u)/base)
                    max_disk = max(max_disk,ratio)
                    counts['polynomial_disk_samples'] += 1
    return dict(**counts, precision_digits=mp.mp.dps,
                max_source_relative_error=str(max_exact),
                max_normal_relative_error=str(max_normal),
                max_polynomial_disk_ratio=str(max_disk),
                max_root_normal_ratio_over_N_squared=str(max_scaled_normal))


if __name__ == '__main__':
    result = dict(status='PASS', exact=exact_checks(), complex=complex_checks(),
                  scope=('Actual generic small-channel values and normals only. '
                         'No paired-large-channel, whole-source, or global volume claim. '
                         'Complex samples illustrate the proved polynomial disk; '
                         'they do not establish its uniform bound.'))
    target = Path(__file__).with_name('actual_q_hahn_small_channel_generic_normals_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
