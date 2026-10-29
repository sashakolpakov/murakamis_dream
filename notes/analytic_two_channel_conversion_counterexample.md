# Analytic two-channel conversion can exceed every marked branch action

28 October 2026. A transverse crossing of eigenvalue MODULI, with
distinct nonzero eigenvalues and uniformly conditioned analytic
eigenvectors, does not justify replacing the integral of the largest
root modulus by the largest continuously marked branch action.
The following exact two-channel model quantifies the missing conversion
cost. It is a general recurrence example, not an operator or source
counterexample for a knot.

## 1. A uniformly separated analytic family

Fix

    0<theta<min(a,pi), b_N=N^(-p), p>=0 fixed,
    alpha(x)=exp(a(x-1/2)),
    beta(x)=exp(-a(x-1/2)+i theta),
    T_N(x)=[[alpha(x),b_N],[0,beta(x)]].          (1)

The entries are entire functions of x. All their fixed derivatives
are uniformly bounded on a fixed complex neighborhood of [0,1].
The eigenvalues are alpha,beta, independently of b_N, and

    |alpha(x)-beta(x)|^2
       =exp(2a(x-1/2))+exp(-2a(x-1/2))-2cos(theta)
       >=4sin(theta/2)^2                         (2)

on the real interval. They have a transverse modulus crossing at
x=1/2 but are distinct there. A diagonalizing matrix is

    S_N(x)=[[1,b_N/(beta(x)-alpha(x))],[0,1]].

Both S_N and its inverse have norm at most
1+1/(2sin(theta/2)) on [0,1]. They extend holomorphically with
uniform bounds to a smaller fixed neighborhood: the closest eigenvalue
collision is at x=1/2+i theta/(2a), off the real interval.

Each continuously marked full-interval logarithmic action is zero:

    integral_0^1 log|alpha(x)|dx
      =integral_0^1 log|beta(x)|dx=0.             (3)

In contrast, the scalar spectral-radius envelope is

    integral_0^1 log rho(T_N(x))dx=a/4.          (4)

The following calculation treats the complete ordered product,
including the actual conversion between the two channels.

## 2. Exact product and its Gaussian conversion entry

Let later times act on the left:

    P_N=T_N((N-1)/N)...T_N(0).

The diagonal entries are exactly exp(-a/2) and exp(a/2+iN theta).
The single possible channel conversion gives

    (P_N)_12=b_N sum_(k=0)^(N-1)
                     exp[a k(N-k)/N+i theta k].                 (5)

Indeed the term converting at time k contains alpha_j for j>k
and beta_j for j<k. The sum of their real logarithms is
a k(N-k)/N, and their phase is theta k. This is an exact finite
product calculation, without an eigenvector or adiabatic approximation.

Put

    Gamma=a/4-theta^2/(4a)>0,
    kappa=pi(pi-theta)/a>0.

For ALL integer N tending to infinity,

    (P_N)_12=b_N sqrt(pi N/a)
            exp(N Gamma+iN theta/2)
            [1+O(exp(-kappa N))+O(N^(-1/2)exp(-Gamma N))].       (6)

In particular there is no parity restriction or subsequence lower
bound hidden in (6). Its leading phase is a single nonzero phase,
not a cosine that might vanish.

Here is an elementary Fourier proof with the tails retained. Extend
the sum in (5) to every integer k. Periodize the integrable function

    g(t)=exp[-a(t-N/2)^2/N+i theta t].

Its m-th Fourier coefficient is the ordinary Gaussian integral

    integral_R g(t)exp(-2pi i m t)dt
      =sqrt(pi N/a) exp[-N(theta-2pi m)^2/(4a)]
                         exp[i(theta-2pi m)N/2].

The Gaussian Fourier integral itself follows by differentiation in
its frequency and integration by parts, with its value at frequency
zero fixed by the real Gaussian integral. The periodized function and
its Fourier series converge absolutely, so evaluation at zero gives

    sum_(k in Z) exp[a k(N-k)/N+i theta k]
      =sqrt(pi N/a) exp(aN/4+iN theta/2)
         sum_(m in Z)(-1)^(mN)
                         exp[-N(theta-2pi m)^2/(4a)].           (7)

Because 0<theta<pi, m=0 is the UNIQUE largest Fourier term.
All other terms together are smaller relatively by O(exp(-kappa N)).
The factor (-1)^(mN) therefore does not create leading cancellation.
At theta=pi this argument would fail and parity would matter; that
case is explicitly excluded.

The omitted terms k<0 or k>=N have absolute sum at most

    1+2sum_(r>=1)exp(-ar)=coth(a/2),             (8)

since their real exponents are at most -ar. Thus their contribution
is bounded independently of N, BEFORE multiplication by b_N. Combining
(7)--(8) proves (6) and its all-level nonvanishing assertion.

It follows directly from the bounded diagonal entries that

    lim_(N->infinity) N^(-1)log||P_N||_2=Gamma>0.                (9)

The same limit holds for the unit boundary source e_2 and the scalar
output e_1^t P_N e_2. These are fixed polynomially bounded boundary
data. The alternative source e_1 remains bounded and has rate zero.
Consequently source selection cannot be inferred from the eigenvalue
curves alone.

For example, a=2 and theta=1 give marked branch actions 0,
the scalar envelope 1/2, and the exact coherent-product rate 3/8.
There is genuinely exponentially small conversion compared with the
envelope: its penalty is theta^2/(4a), but that penalty is insufficient
to reduce the answer to the largest marked branch action.

The same calculation also gives a precise sufficient condition in
this model. Allow arbitrary a>0 and 0<theta<pi, without assuming
theta<a. Formula (7) and the bounded tails give the exact norm rate
max(0,a/4-theta^2/(4a)). At theta=a the conversion is only polynomial;
at theta>a it is bounded, as are the diagonal products. Thus here
the marked-branch bound is valid exactly when the conversion penalty
is at least its action gain. Real-axis eigenvalue separation alone
does not express that inequality.

## 3. Subprincipal coupling and reciprocal variants

The case p=0 is one fixed analytic matrix family with uniformly
separated eigenvalues. The case p=1 is stronger for a proposed
semiclassical robustness argument: T_N differs from the exactly
diagonal principal family by O(1/N), with all fixed analytic derivatives
obeying the same estimate. The diagonal principal product has rate
zero, whereas the true product still has rate Gamma. A polynomially
small channel coupling changes the leading exponential rate.

The same solution also satisfies a scalar second-order recurrence.
Writing h=1/N and u_j for its first component, eliminate the second
component to obtain

    u_(j+2)=[alpha(x+h)+beta(x)]u_(j+1)
                        -alpha(x)beta(x)u_j, x=j/N,
    u_0=0, u_1=b_N.                              (10)

Its literal companion is [[0,1],[-exp(i theta),alpha(x+h)+beta(x)]].
This analytic companion differs by O(h) from a principal companion
with the uniformly distinct roots alpha,beta. Its initial source is
polynomially bounded, and u_N is exactly (5). Thus the counterexample
also applies to a scalar finite-order recurrence with an analytic
subprincipal correction; it is not confined to a noncompanion matrix
presentation. No claim that its coefficients are those of a knot
quantum-A operator is being made.

A determinant-one condition does not prevent this example. Multiplying
every T_N by exp(-i theta/2) makes its determinant exactly one and
changes no norm, eigenvalue modulus or rate in (3)--(9).

One can also realize the modulus crossing between two distinct
EXPANDING roots of a reciprocal-conjugate four-channel family.
Let Ttilde=exp(-i theta/2)T_N, choose c>a/2, put B=exp(c)Ttilde,
and on the real interval set

    A_N(x)=diag(B(x),(B(x)^*)^(-1)),
    J=[[0,I_2],[I_2,0]].

Use coefficient conjugation to extend the second block holomorphically
off the real interval. Then A_N^* J A_N=J, det A_N=1, and its roots
are lambda_1,lambda_2,1/conj(lambda_1),1/conj(lambda_2), with
lambda_(1,2)=exp(c) times the two eigenvalues of Ttilde. All four
are distinct throughout [0,1]. At x=1/2 the two expanding roots
exp(c +/- i theta/2) have equal modulus and remain distinct.

The largest marked branch action is c and the scalar envelope is
c+a/4. Its coherent-product norm has rate c+Gamma. Indeed its two
product blocks are exp(cN)Ptilde_N and exp(-cN)(Ptilde_N^*)^(-1),
and a determinant-one 2 by 2 matrix has the same operator norm as its
inverse. Thus even this reciprocal-conjugate structure does not imply
the proposed branch-action shortcut.

## 4. What this does and does not decide

Analyticity, a uniform real eigenvalue gap, analytic conditioned
eigenvectors and polynomial boundary data are NOT sufficient to
bound a coherent product by the maximum of complete marked branch
actions. The exact Gaussian model identifies a real missing estimate:
one must control the action gained by changing channels together with
its exponentially small conversion cost and the actual source that
can excite it. A simultaneous constant diagonalization, or a preserved
boundary source channel, would prevent the conversion in this example;
plain slow variation does not.

This does not refute the lower classical 6_1 product rates already
computed, nor a stronger theorem using the special knot operator and
its original source. It rules out inferring that stronger theorem
from generic analytic slow variation alone. No quantum-A operator,
regulator identity or original knot source is asserted for (1).

[Audit](../experiments/audit_analytic_two_channel_conversion.py) compares
literal matrix products, the finite Gaussian sum and the Fourier
formula at odd and even levels, including the O(1/N) coupling and
the preserved-source alternative.
