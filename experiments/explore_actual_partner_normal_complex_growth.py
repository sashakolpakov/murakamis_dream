"""Exploration, not a theorem: actual large-partner first normals.

The original generic highest-vector ratio is differentiated before root
specialization. The examples stay in strict complete support and in the
joint central wedge. Positive apparent exponential rates are diagnostics;
no asymptotic lower bound follows from these finite computations.
"""
import json
from pathlib import Path
import mpmath as mp


def original_column_and_normal(N, t, j, u):
    q = mp.exp(mp.pi*1j/N)
    Q, d, v = q*q, N-1, t-u
    F, DF = [mp.mpc(1)], [mp.mpc(0)]
    for k in range(1, N):
        w = Q**k
        F.append(F[-1]*(1-w))
        DF.append(DF[-1]-2*k*w/(1-w))

    def binomial_jets(top):
        values, derivatives = [mp.mpc(1)], [mp.mpc(0)]
        for k in range(j):
            z, w = q**(2*(top-k)), Q**(k+1)
            numerator, denominator = 1-z, 1-w
            dn, dd = -2*(top-k)*z, -2*(k+1)*w
            ratio = numerator/denominator
            dr = (dn*denominator-numerator*dd)/denominator**2
            derivatives.append(derivatives[-1]*ratio+values[-1]*dr)
            values.append(values[-1]*ratio)
        return values, derivatives

    bu, du = binomial_jets(u)
    bv, dv = binomial_jets(v)
    bt, dt = binomial_jets(t)
    values, derivatives = [], []
    for a in range(j+1):
        m = j-a
        # Value may use root complementation; derivative uses the original
        # four factorials, exactly as the physical generic compiler does.
        R = Q**(a*(a-j))*F[j]/F[a]/F[j-a]
        dlogR = DF[N-j+a-1]+DF[N-a-1]-DF[N-j-1]-DF[N-1]
        exponent = d*(u-2*a)+2*a*v+a*(a-1)
        outer = (-1)**a*q**exponent*R
        product = bu[a]*bv[m]/bt[j]
        dproduct = ((du[a]*bv[m]+bu[a]*dv[m])/bt[j]
                    -product*dt[j]/bt[j])
        values.append(outer*product)
        derivatives.append(outer*((exponent+dlogR)*product+dproduct))
    return mp.fsum(values), mp.fsum(derivatives)


def main():
    mp.mp.dps = 420
    cases = [('.2','.87','.3'), ('.2','.87','.6'),
             ('.45','.8','.3'), ('.45','.8','1.0'),
             ('.48','.8','1.0')]
    rows = []
    for xi, tau, imag_nu in cases:
        for N in (40, 80, 160):
            j = int(mp.floor(mp.mpf(xi)*N))
            l = N-1-j
            t = mp.mpf(tau)*N
            u = t/2+1j*mp.mpf(imag_nu)*N
            assert t > l
            cj, dj = original_column_and_normal(N,t,j,u)
            cl, dl = original_column_and_normal(N,t,l,u)
            cancellation_error = abs(cl/cj-1)
            assert cancellation_error < mp.mpf('1e-180')
            rows.append(dict(level=N, small_channel=j, large_channel=l,
                             tau=tau, nu_real=str(mp.mpf(tau)/2),
                             nu_imaginary=imag_nu,
                             log_generic_difference_ratio_over_N=mp.nstr(
                                 mp.log(abs((dj-dl)/cj))/N, 50),
                             root_collapse_relative_error=mp.nstr(cancellation_error, 30)))
    result = dict(status='EXPLORATION_COMPLETED', precision_digits=mp.mp.dps,
                  scope=('Original generic derivatives and exact-value collapse '
                         'are checked numerically. Apparent exponential growth '
                         'is not a proved lower bound or a failure of every '
                         'smaller near-fold corridor.'), rows=rows)
    target = Path(__file__).with_name('actual_partner_normal_complex_growth_exploration.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status=result['status'], cases=len(rows),
                          precision_digits=mp.mp.dps,
                          result_path=str(target)),indent=2))


if __name__ == '__main__':
    main()
