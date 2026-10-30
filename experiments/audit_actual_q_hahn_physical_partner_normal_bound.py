"""Original paired normal, half-prefix identity and first-order reflection.

Exact checks use the original generic R-factor derivative, independently
of the root continuant. Positivity and the uniform bound are proved in
the note; numerical eigenvalue checks are regressions only.
"""
import json
from pathlib import Path
import mpmath as mp
import numpy as np
import sympy as sp
from audit_actual_q_hahn_partner_normal_collision import original_column
from audit_high_color_first_normal_r_degree import root_field


def symbolic_row_identity():
    a, ca, b, cb, s, c = sp.symbols('a ca b cb s c')
    hs, hc = b*ca-cb*a, cb*ca+b*a
    numerator = sp.expand((hs*(2*a*b*c+(a*cb+ca*b)*s)
                            -(hs*c+hc*s)*a*b)*(b*c-cb*s)
                           -(hs*c-hc*s)*b*b*(a*c+ca*s))
    assert sp.expand(numerator-a*s*s*(b*b+cb*cb)*(a*cb+b*ca)) == 0
    return 1


def matrix_mod(N,t,q,p):
    Q, x, T = q*q % p, pow(q,N-1,p), pow(q,2*t,p)
    A, D = [], []
    for r in range(t+1):
        U = pow(Q,r,p)
        direct = ((pow(U,-1,p)-1)*x*pow(Q,-(t-r),p)*(1-U)
                  +(pow(Q,-(t-r),p)-1)*pow(x,-1,p)*U*(1-pow(Q,t-r,p))
                  +q*x*x*pow(T,-1,p)+pow(q,-1,p)*pow(x,-2,p)*T) % p
        simplified = U*pow(T,-1,p)*(2*(pow(q,-1,p)+q*T)
                                   -(q+pow(q,-1,p))*U) % p
        assert direct == simplified
        D.append(direct)
        if r<t:
            direct_A = pow(Q,-(t-r),p)*(1-pow(Q,t-r,p))*(1-pow(Q,r+1,p))%p
            assert direct_A == (U-T)*(1-Q*U)*pow(T,-1,p)%p
            A.append(direct_A)
    return A,D


def forward_mod(A,D,z,p):
    f,g = [1],[0]
    for r in range(len(A)):
        prev = A[r-1]*f[r-1] if r else 0
        dprev = A[r-1]*g[r-1] if r else 0
        f.append(((z-D[r])*f[r]-prev)*pow(A[r],-1,p)%p)
        g.append((f[r]+(z-D[r])*g[r]-dprev)*pow(A[r],-1,p)%p)
    return f,g


def exact_checks():
    counts = dict(original_Casimir_blocks=0, weighted_row_identities=0,
                  original_generic_paired_normals=0,
                  reflected_value_and_first_normal=0,
                  original_endpoint_normals=0)
    for N in range(3,24):
        p,eta = root_field(N)
        q, ii = eta*eta%p, pow(eta,N,p)
        inv2i = pow(2*ii,-1,p)
        sine = lambda r:(pow(q,r,p)-pow(q,-r,p))*inv2i%p
        cosine = lambda r:(pow(q,r,p)+pow(q,-r,p))*pow(2,-1,p)%p
        for t in range((N+1)//2,N):
            A,D = matrix_mod(N,t,q,p)
            Ac,Dc = matrix_mod(N,t,pow(q,-1,p),p)
            assert D[::-1] == Dc and A[::-1] == Ac
            counts['original_Casimir_blocks'] += 1
            m = t//2
            weights = [pow(sine(t-r),-1,p) for r in range(m+1)]
            os = [(A[r]-Ac[r])*inv2i%p for r in range(m)]
            for r in range(m):
                di = (D[r]-Dc[r])*inv2i%p
                residual = di-os[r]*weights[r+1]*pow(weights[r],-1,p)
                if r:
                    residual -= os[r-1]*weights[r-1]*pow(weights[r],-1,p)
                exact = 4*sine(r)*sine(1)**2*sine(t)*pow(sine(t-r-1),-1,p)%p
                assert residual%p == exact
                assert os[r]*weights[r]*weights[r+1]%p == (
                    4*sine(t-2*r-1)*sine(r+1)*pow(sine(t-r-1),-1,p)%p)
                counts['weighted_row_identities'] += 1
            for j in range(N-1-t,(N-2)//2+1):
                l = N-1-j
                z = (pow(q,2*j+1,p)+pow(q,-2*j-1,p))%p
                delta = (pow(q,2*j+1,p)-pow(q,-2*j-1,p))%p
                f,g = forward_mod(A,D,z,p)
                fc,gc = forward_mod(Ac,Dc,z,p)
                assert ((z-D[-1])*f[-1]-A[-1]*f[-2])%p == 0
                assert (f[-1]+(z-D[-1])*g[-1]-A[-1]*g[-2])%p == 0
                endpoint = -(l-j)*pow(2*delta,-1,p)%p
                assert g[-1] == endpoint*f[-1]%p
                counts['original_endpoint_normals'] += 1
                for u in range(t+1):
                    cj,dj = original_column(N,t,j,u,p,q)
                    cl,dl = original_column(N,t,l,u,p,q)
                    assert cj == cl == f[u]
                    assert (dj-dl)*pow(-2*N*delta,-1,p)%p == g[u]
                    counts['original_generic_paired_normals'] += 1
                    assert f[t-u] == f[-1]*fc[u]%p
                    assert g[t-u] == (g[-1]*fc[u]+f[-1]*gc[u])%p
                    counts['reflected_value_and_first_normal'] += 1
    return counts


def numerical_checks():
    mp.mp.dps = 90
    counts = dict(positive_prefix_matrices=0, conductance_bounds=0,
                  actual_normal_relative_bounds=0)
    min_eigenvalue_ratio = float('inf')
    max_normal_bound_ratio = mp.mpf(0)
    for N in range(3,35):
        th, q = mp.pi/N, mp.exp(mp.pi*1j/N)
        Q = q*q
        for t in range((N+1)//2,N):
            T = Q**t
            D = [Q**r/T*(2*(q**-1+q*T)-(q+q**-1)*Q**r) for r in range(t+1)]
            A = [(Q**r-T)*(1-Q**(r+1))/T for r in range(t)]
            m = t//2
            weights = [1/mp.sin((t-r)*th) for r in range(m+1)]
            for r in range(m):
                conductance = mp.im(A[r])*weights[r]*weights[r+1]
                assert conductance >= 4*mp.sin(th)-mp.mpf('1e-80')
                counts['conductance_bounds'] += 1
            B = np.diag([float(mp.im(D[r])) for r in range(m)])
            if m>1:
                off = [float(mp.im(A[r])) for r in range(m-1)]
                B += np.diag(off,1)+np.diag(off,-1)
            ev = float(np.linalg.eigvalsh(B)[0])
            lower = float(4*mp.sin(th)**3/m**2)
            assert ev >= lower*(1-1e-9), (N,t,ev,lower)
            min_eigenvalue_ratio = min(min_eigenvalue_ratio,ev/lower)
            counts['positive_prefix_matrices'] += 1
            if N>24:
                continue
            for j in range(N-1-t,(N-2)//2+1):
                z = q**(2*j+1)+q**(-2*j-1)
                f,g = [mp.mpc(1)],[mp.mpc(0)]
                for r in range(t):
                    f.append(((z-D[r])*f[r]-(A[r-1]*f[r-1] if r else 0))/A[r])
                    g.append((f[r]+(z-D[r])*g[r]-(A[r-1]*g[r-1] if r else 0))/A[r])
                bound = mp.mpf(N)**6/256+mp.mpf(N)**2/8
                for value,normal in zip(f,g):
                    assert abs(value)>mp.mpf('1e-70')
                    ratio = abs(normal/value)/bound
                    assert ratio <= 1+mp.mpf('1e-75')
                    max_normal_bound_ratio = max(max_normal_bound_ratio,ratio)
                    counts['actual_normal_relative_bounds'] += 1
    return dict(**counts,precision_digits=mp.mp.dps,
                minimum_eigenvalue_over_proved_lower_bound=min_eigenvalue_ratio,
                maximum_normal_over_proved_bound=mp.nstr(max_normal_bound_ratio,40))


if __name__ == '__main__':
    result = dict(status='PASS', symbolic_weighted_row_identity=symbolic_row_identity(),
                  exact=exact_checks(),numerical=numerical_checks(),
                  scope=('Original physical-grid paired normals, both parities and all '
                         'complete double channels. No complex magnetic corridor, '
                         'whole-source norm, or volume-limit claim.'))
    target = Path(__file__).with_name('actual_q_hahn_physical_partner_normal_bound_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
