"""All-color Weyl-chart source comparison, including alias/zero tests.

The actual q-binomial is evaluated by its polynomial recurrence, not by
the product used to derive the comparison. No knot-period norm is tested.
"""
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

mp.mp.dps = 85
c = 2j*mp.pi


def J(x):
    return 2*mp.sinh(x/2)/x if x else mp.mpf(1)


def qbinomial_row(n, H):
    Q = mp.exp(H)
    row = [mp.mpf(1)]
    for m in range(1,n+1):
        nxt = [mp.mpf(1)]
        for j in range(1,m):
            nxt.append(row[j]+Q**(m-j)*row[j-1])
        nxt.append(mp.mpf(1))
        row = nxt
    return [mp.exp(-H*j*(n-j)/2)*v for j,v in enumerate(row)]


def data(N, a=None, b_exact=None):
    H0 = c/N
    if b_exact is None:
        b = a/(1+a/N)
        H = H0+c*a/N**2
    else:
        b = mp.mpc(b_exact)
        a = b/(1-b/N)
        H = H0/(1-b/N)
    Mcol = mp.exp(H*b/2)
    Mp = mp.exp(H0*b/2)
    Mm = 1/Mp
    return H0,H,a,b,Mcol,Mp,Mm


def root_prefixes(N,M):
    Q0 = mp.exp(c/N)
    beta = [mp.mpf(1)]
    for r in range(1,N):
        beta.append(beta[-1]*(1-M*M*Q0**r)/(1-Q0**r))
    return beta


def units(N,H0,H,b):
    n = N-1
    L = n//2
    prefix = [mp.mpf(1)]
    for r in range(1,L+1):
        factor = mp.exp(-(H-H0)*b/2)*J(H*(r-b))*J(H0*r)/(J(H*r)*J(H0*(r-b)))
        prefix.append(prefix[-1]*factor)
    return [prefix[j] if j<=L else mp.exp((H-H0)*b*(n-2*j)/2)*prefix[n-j]
            for j in range(N)]


def targets(N,Mp,Mm):
    n = N-1
    L = n//2
    beta = root_prefixes(N,Mm)
    return [beta[j] if j<=L else Mp**(n-2*j)*beta[n-j] for j in range(N)]


def finite_checks():
    samples = [mp.mpc('.4','.3'),mp.mpc('-.6','.2'),mp.mpf(0),mp.mpf(-1)]
    records = []
    zero_checks = 0
    for N in (6,7,12,13,24,25):
        n = N-1
        for label,aa,bb in [(str(a),a,None) for a in samples]+[('b=1',None,1),('b=2',None,2)]:
            H0,H,a,b,Mcol,Mp,Mm = data(N,aa,bb)
            actual = [v/Mcol**j for j,v in enumerate(qbinomial_row(n,H))]
            B = targets(N,Mp,Mm)
            C = units(N,H0,H,b)
            beta_p,beta_m = root_prefixes(N,Mp),root_prefixes(N,Mm)
            HN = mp.fsum(Mp**(2*r-n) for r in range(N))/N
            maxerr = mp.mpf(0)
            for j in range(N):
                error = abs(actual[j]-C[j]*B[j])/(1+abs(actual[j]))
                assert error < mp.mpf('1e-65')
                maxerr = max(maxerr,error)
                # The actual whole root Weyl complement, checked for
                # every color, also at both source endpoint colors.
                assert abs(beta_p[j]*beta_m[n-j]-Mp**(2*j-n)*HN)<mp.mpf('1e-65')*(1+abs(HN))
                if j>n//2:
                    assert abs(beta_p[j]*B[j]-HN)<mp.mpf('1e-65')*(1+abs(HN))
                assert abs(C[j])>mp.mpf('0.001')
            if bb is not None:
                for j in range(N):
                    expected_zero = bb<=j<=n-bb
                    if expected_zero:
                        assert abs(actual[j]) < mp.mpf('1e-60')
                        assert abs(B[j]) < mp.mpf('1e-60')
                    else:
                        assert abs(actual[j]) > mp.mpf('0.001')
                        assert abs(B[j]) > mp.mpf('0.001')
                    zero_checks += 1
            else:
                # Literal 1/N source/dual transport in the two
                # meromorphic frames, including off-diagonal coupons.
                Uq=[mp.exp(H*(N*j-j*(j+1)//2)/2) for j in range(N)]
                U0=[mp.exp(H0*(N*j-j*(j+1)//2)/2) for j in range(N)]
                psi_col=[Uq[j]*actual[j] for j in range(N)]
                psi_root=[U0[j]*B[j] for j in range(N)]
                phi_col=[1/(N*x) for x in psi_col]
                phi_root=[1/(N*x) for x in psi_root]
                transport=[Uq[j]/U0[j]*C[j] for j in range(N)]
                for j in range(N):
                    assert abs(psi_col[j]-transport[j]*psi_root[j])<mp.mpf('1e-60')*(1+abs(psi_col[j]))
                    assert abs(phi_col[j]-phi_root[j]/transport[j])<mp.mpf('1e-60')*(1+abs(phi_col[j]))
                for r in (0,1,2):
                    pc=mp.fsum(phi_col[j]*(mp.mpf(j)/N)**r*psi_col[j] for j in range(N))
                    pr=mp.fsum(phi_root[j]*(mp.mpf(j)/N)**r*psi_root[j] for j in range(N))
                    assert abs(pc-pr)<mp.mpf('1e-65')
                assert abs(mp.fsum(phi_col[j]*psi_col[j] for j in range(N))-1)<mp.mpf('1e-65')
                for i,j in ((0,n),(n,0),(N//2,0)):
                    lhs=psi_col[i]*phi_col[j]
                    rhs=transport[i]*psi_root[i]*phi_root[j]/transport[j]
                    assert abs(lhs-rhs)<mp.mpf('1e-60')*(1+abs(lhs))
            records.append({'N':N,'normal_parameter':label,'all_colors':N,
                            'max_scaled_error':float(maxerr)})
        # A single upper prefix would have the wrong root-periodic
        # alias zero; the actual complementary source has no such zero.
        H0,H,a,b,Mcol,Mp,Mm = data(N,b_exact=-1)
        naive = root_prefixes(N,Mm)[n]
        folded = targets(N,Mp,Mm)[n]
        assert abs(naive) < mp.mpf('1e-65')
        assert abs(folded)>mp.mpf('0.5')
        assert abs(Mcol**(-n)-units(N,H0,H,b)[n]*folded)<mp.mpf('1e-65')
    return {'finite_cases':records,'all_head_zero_pattern_checks':zero_checks,
            'periodic_alias_counterexamples':6,'pointed_source_dual_and_moment_cases':24,
            'qbinomial_method':'independent polynomial recurrence'}


def uniform_norm_checks():
    samples = [mp.mpc('.4','.3'),mp.mpc('-.6','.2'),mp.mpf(0),mp.mpf(1),mp.mpf(2),mp.mpf(-2)]
    result = []
    for N in (16,32,64,128):
        worst_error = mp.mpf(0)
        smallest_unit = mp.inf
        worst_chirp = mp.mpf(0)
        for a in samples:
            H0,H,a,b,*_ = data(N,a=a)
            C = units(N,H0,H,b)
            for j,value in enumerate(C):
                worst_error = max(worst_error,N*abs(value-1))
                smallest_unit = min(smallest_unit,abs(value))
                exponent = c*a*(mp.mpf(j)/(2*N)-mp.mpf(j*(j+1))/(4*N*N))
                chirp = mp.exp(exponent)
                assert max(abs(chirp),abs(1/chirp))<=mp.exp(abs(c*a)/4)*(1+mp.mpf('1e-70'))
                worst_chirp = max(worst_chirp,abs(chirp*value),abs(1/(chirp*value)))
        assert worst_error<500
        result.append({'N':N,'max_all_head_unit_error_times_N':float(worst_error),
                       'minimum_unit_modulus':float(smallest_unit),
                       'maximum_full_source_comparison_norm_or_inverse':float(worst_chirp)})
    return result


def main():
    result = {'finite_exact_comparison':finite_checks(),
              'whole_head_operator_norm_diagnostics':uniform_norm_checks(),
              'scope':'actual source-factor/dual lattices; no crossing similarity or selected volume bound'}
    target = Path(__file__).with_name('full_head_gamma_source_transport_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'pass','finite_cases':len(result['finite_exact_comparison']['finite_cases']),
                      'zero_pattern_checks':result['finite_exact_comparison']['all_head_zero_pattern_checks'],
                      'results':str(target)},indent=2))


if __name__ == '__main__':
    main()
