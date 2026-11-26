#!/usr/bin/env python3
"""Original full-kernel/current and adjacent-three boundary diagnostics.

Every source vector is computed from the original crossing coefficients.
The banded operator is constructed separately from its recorded entries.
No numerical asymptotic claim is tested.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp


ROOT = Path(__file__).resolve().parents[1]


def pad(a, n):
    return list(a) + [mp.mpc(0)] * max(0, n - len(a))


def sub(a, b):
    n = max(len(a), len(b))
    aa, bb = pad(a, n), pad(b, n)
    return [aa[j] - bb[j] for j in range(n)]


def scale(a, c):
    return [c * z for z in a]


def peval(a, x):
    return mp.polyval(list(reversed(a)), x)


def shift(a, Q):
    return [z * Q**(-j) for j, z in enumerate(a)]


def dop(a, q, which):
    Q = q*q
    out = [mp.mpc(0)] * (len(a) + 1)
    for j, value in enumerate(a):
        if which == 3:
            out[j+1] += q * value
        else:
            out[j+1] += (q - q**-1 * Q**-j) * value
            out[j] += 2 * q**-1 * Q**-j * value
        if j:
            out[j-1] += q**-1 * (1 - Q**-j) * value
    return out


def maxnorm(a):
    if isinstance(a, mp.matrix):
        return max([abs(z) for z in a] + [mp.mpf(0)])
    return max([abs(z) for z in a] + [mp.mpf(0)])


def rel(a, b):
    if isinstance(a, mp.matrix):
        return maxnorm(a-b) / max(1, maxnorm(a), maxnorm(b))
    if isinstance(a, (list, tuple)):
        return maxnorm(sub(a, b)) / max(1, maxnorm(a), maxnorm(b))
    return abs(a-b) / max(1, abs(a), abs(b))


def original(N, sign):
    q = mp.exp(sign * mp.pi * 1j / N)
    Q = q*q
    kappa = mp.exp(sign * mp.pi * 1j * (N-1)**2 / (2*N))
    sine = [mp.mpf(1)]
    for j in range(1, N):
        sine.append(sine[-1] * 2 * mp.sin(mp.pi*j/N))
    M, C, J, B, L1 = [mp.matrix(N) for _ in range(5)]
    c, d = [], []
    for j in range(N):
        c.append(2*mp.cos((2*j+1)*mp.pi/N))
        d.append(4*mp.sin(j*mp.pi/N)**2)
        C[j, j] = c[-1]
        J[j, N-1-j] = 1
        B[j, j] = -q*Q**j
        L1[j, j] = 4*q*Q**j - q*(1+Q)*Q**(2*j)
        if j:
            C[j, j-1] = -d[-1]
            B[j-1, j] = 1-Q**j
            L1[j-1, j] = L1[j, j-1] = -(1-Q**j)**2
        for l in range(j+1):
            M[j, l] = (kappa * (-1)**j * q**(j*(l+1))
                       * sine[j] / (sine[l]*sine[j-l]))
    return q, Q, kappa, c, d, M, C, J, B, L1


def newton_jet(w, c, d):
    values, normals = [mp.mpc(1)], [mp.mpc(0)]
    for j in range(len(c)-1):
        values.append((c[j]-w)*values[-1]/d[j+1])
        normals.append(((c[j]-w)*normals[-1]-values[-2])/d[j+1])
    return values, normals


def spectral_relation(w, N):
    a, b = mp.mpc(2), w
    if N == 1:
        return b + 2
    for _ in range(2, N+1):
        a, b = b, w*b-a
    return b+2


def determinant(T):
    """Row-pivot determinant, including exactly singular cofactor matrices.

    mpmath's LU determinant can send a None pivot to swap_row for a
    singular derivative-cofactor matrix. No tolerance is used here.
    """
    if T.rows != T.cols:
        raise ValueError("Determinant requires a square matrix")
    work = T.copy()
    value = mp.mpc(1)
    for j in range(T.rows):
        pivot = max(range(j,T.rows),key=lambda i:abs(work[i,j]))
        if work[pivot,j] == 0:
            return mp.mpc(0)
        if pivot != j:
            for col in range(T.cols):
                work[j,col],work[pivot,col] = work[pivot,col],work[j,col]
            value = -value
        p = work[j,j]
        value *= p
        for i in range(j+1,T.rows):
            multiplier = work[i,j]/p
            work[i,j] = 0
            for col in range(j+1,T.cols):
                work[i,col] -= multiplier*work[j,col]
    return value


def determinant_jet(T, derivative):
    value = determinant(T)
    normal = mp.mpc(0)
    for j in range(T.cols):
        one = T.copy()
        for i in range(T.rows):
            one[i, j] = derivative[i, j]
        normal += determinant(one)
    return value, normal


def run(precision):
    mp.mp.dps = precision
    categories = {}
    count = {}
    rows = []

    def check(name, actual, expected):
        error = rel(actual, expected)
        categories[name] = max(categories.get(name, mp.mpf(0)), error)
        count[name] = count.get(name, 0) + 1
        if error > mp.mpf(10)**(-(precision//2)):
            raise ArithmeticError(f"{name}: relative error {mp.nstr(error, 12)}")

    for N in range(2, 11):
        for sign in (1, -1):
            q,Q,kappa,c,d,M,C,J,B,L1 = original(N, sign)
            D, eta = N-1, (-1)**(N-1)
            I, e0, ed = mp.eye(N), mp.eye(N)[:,0], mp.eye(N)[:,D]
            X = mp.diag([Q**j for j in range(N)])
            L = C.T
            alpha, alpha1 = M**3*e0, M*e0
            current = kappa**2/q
            check("source_current", (C-q*X)*alpha, current*alpha1)
            h, r, emat = [[mp.mpc(1)]], [[mp.mpc(0)]], [I]
            for l in range(D):
                h.append(scale(sub(scale(h[-1],c[l]),dop(h[-1],q,3)),
                               1/d[l+1]))
                rr = sub(sub(scale(r[-1],c[l]),dop(r[-1],q,1)),
                         shift(h[-2],Q))
                r.append(scale(rr,1/d[l+1]))
                emat.append((c[l]*I-C)*emat[-1]/d[l+1])
            for l in range(N):
                expected = mp.matrix([
                    peval(h[l],Q**j)*alpha[j]
                    +current*peval(r[l],Q**j)*alpha1[j]
                    for j in range(N)
                ])
                check("all_degree_two_state", emat[l]*alpha, expected)

            # Chebyshev applied to the polynomial oscillator, off the clock.
            t0, t1 = [mp.mpc(2)], dop([mp.mpc(1)],q,3)
            for _ in range(2,N+1):
                t0,t1 = t1,sub(dop(t1,q,3),t0)
            t1[0] += 2
            wanted = [mp.mpc(2)] + [mp.mpc(0)]*(N-1) + [-1]
            check("full_central_forcing",t1,wanted)

            S = J*M**3*J
            source = S*alpha
            A3 = q**-2*(L*L-I)*L1 + q**-3*L*C - 8*q**-2*L + 8*q**-1*I
            A = B*(A3-L)-I
            zeta = eta*kappa**2/q
            check("original_L1",L1,M**-1*L*M)
            check("conjugated_C",A3,S*C*S**-1)
            check("conjugated_clock",S*X*S**-1,q**-1*(L+B**-1))
            check("terminal_current",B*(J*M**2*e0),eta*ed)
            check("endpoint_forced_source",A*source,zeta*ed)
            check("operator_determinant",determinant(A),-eta)
            for i in range(N):
                for j in range(N):
                    if i-j > 1 or j-i > 4:
                        check("zero_band",A[i,j],0)
            for j in range(1,N):
                check("lower_diagonal",A[j,j-1],-q*d[j]*Q**(4*j))
            for j in range(N-4):
                expected = -q**-2*(1-Q**(j+1))*d[j+2]*d[j+3]*(1-Q**(j+4))**2
                check("upper_diagonal",A[j,j+4],expected)
            deltas = [mp.mpc(1)]
            for n in range(1,N+1):
                value = A[n-1,n-1]*deltas[n-1]
                for rr in range(1,min(4,n-1)+1):
                    product = mp.fprod(A[j,j-1] for j in range(n-rr,n))
                    value += (-1)**rr*A[n-1-rr,n-1]*product*deltas[n-rr-1]
                deltas.append(value)
                check("hessenberg_continuant",value,determinant(A[:n,:n]))
            check("closing_coefficient",-kappa**2/q*deltas[D],source[D])

            points = [mp.mpc(-2),mp.mpc(".37",".12")]
            # Every repeated physical root, plus the odd simple root via -2.
            points += [mp.mpc(c[j]) for j in range(N//2)]
            for w in points:
                ev,dv = newton_jet(w,c,d)
                kernel = sum((ev[l]*emat[l] for l in range(N)),mp.zeros(N))
                kernel_d = sum((dv[l]*emat[l] for l in range(N)),mp.zeros(N))
                for jet, Kmat in ((ev,kernel),(dv,kernel_d)):
                    H = [sum(jet[l]*peval(h[l],Q**j) for l in range(N))
                         for j in range(N)]
                    R = [sum(jet[l]*peval(r[l],Q**j) for l in range(N))
                         for j in range(N)]
                    expect = mp.matrix([H[j]*alpha[j]+current*R[j]*alpha1[j]
                                        for j in range(N)])
                    check("full_boundary_kernel_jet",Kmat*alpha,expect)
                    direct = sum(jet[j]*source[j] for j in range(N))
                    check("same_sign_pair_jet",direct,(alpha.T*Kmat*alpha)[0])

                pencil = (A*(w*I-C))[:D,:D]
                determinant_value, normal = determinant_jet(pencil,A[:D,:D])
                unit = -eta*kappa**2/(q*N*N)
                check("ordinary_boundary_determinant",unit*determinant_value,
                      sum(ev[j]*source[j] for j in range(N)))
                check("ordinary_boundary_normal",unit*normal,
                      sum(dv[j]*source[j] for j in range(N)))

                # Test X-polynomial coefficients of both forced kernel equations.
                HI = [mp.mpc(0)]
                HT = [mp.mpc(0)]
                LT = [mp.mpc(0)]
                for l in range(N):
                    HI = sub(HI,scale(h[D-l],-ev[l]))
                    HT = sub(HT,scale(h[l],-ev[l]))
                    lv = c[l]*ev[l] - (d[l]*ev[l-1] if l else 0)
                    LT = sub(LT,scale(h[l],-lv))
                rhs = [eta*(spectral_relation(w,N)-2)/(N*N)]
                rhs += [mp.mpc(0)]*(N-1)+[eta/mp.mpf(N*N)]
                check("identity_kernel_forcing",sub(scale(HI,w),dop(HI,q,3)),rhs)
                rhs2 = [-2*eta*ev[D]/(N*N)]
                rhs2 += [mp.mpc(0)]*(N-1)+[eta*ev[D]/(N*N)]
                check("turn_kernel_forcing",sub(LT,dop(HT,q,3)),rhs2)
            rows.append({"N":N,"sign":sign,"boundary_points":len(points)})

    # Exact commutative chart calculations are separate from finite-level
    # diagnostics; they assert no limiting root or source-cycle selection.
    import sympy as sp
    xx, ee, tt = sp.symbols("X E t")
    dd = 2-xx-1/xx
    cc, ll = xx+1/xx-dd*ee, xx+1/xx-dd/ee
    bb = -xx+(1-xx)/ee
    ll1 = 4*xx-2*xx**2-(1-xx)**2*(ee+1/ee)
    aa = bb*((ll**2-1)*ll1+ll*cc-9*ll+8)-1
    zz, rr = 4-5*tt+4*tt**2-tt**3, tt**2-3*tt+3
    xmap = rr/(zz*rr-1)
    emap = -(tt-2)**3*(tt**2-2*tt+2)**2/(tt-1)**2
    substitutions = {xx:xmap,ee:emap}
    symbolic = {
        "transported_cap":sp.factor(aa.subs(substitutions)),
        "boundary_casimir":sp.factor(cc.subs(substitutions)
                                    -2-((tt-2)**2*(tt**2-2*tt+2))**2),
        "turned_casimir":sp.factor(ll.subs(substitutions)-zz),
        "primitive_factor":sp.factor(bb.subs(substitutions)
                                    -1/((tt-2)*(tt**2-2*tt+2))),
        "lower_diagonal":sp.factor(sp.expand(aa).coeff(ee,1)-xx**3*(xx-1)**2),
        "upper_diagonal":sp.factor(sp.expand(aa).coeff(ee,-4)-(xx-1)**7/xx**2),
    }
    if any(value != 0 for value in symbolic.values()):
        raise ArithmeticError(f"Frozen chart identity failed: {symbolic}")
    return {
        "precision":precision,
        "mpmath_version":mp.__version__,
        "sympy_version":sp.__version__,
        "cases":rows,
        "checks":count,
        "maximum_relative_errors":{k:mp.nstr(v,35) for k,v in categories.items()},
        "maximum_relative_error":mp.nstr(max(categories.values()),35),
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "exact_symbolic_checks":{key:True for key in symbolic},
        "status":"passed",
        "scope":"Finite original-source identities and boundary normals; no asymptotic test."
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--precision",type=int,default=120)
    parser.add_argument("--output",type=Path,
                        default=ROOT/"repro/results/research-three-crossing-boundary-current.json")
    args = parser.parse_args()
    result = run(args.precision)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"status":result["status"],"cases":len(result["cases"]),
                      "checks":sum(result["checks"].values()),
                      "maximum_relative_error":result["maximum_relative_error"],
                      "output":str(args.output)},indent=2))
