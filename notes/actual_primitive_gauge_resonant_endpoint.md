# The actual primitive gauge has a Gaussian resonant endpoint

27 October 2026. The canonical finite Hilbert-90 gauge from the
original source has an exactly computable resonant endpoint. Its
polynomial Ward identity contains two retained highest-degree terms.
The endpoint is a quadratic Gauss period, of size N^(-1/2), despite
the gauge's exponential operator norm on the flat relative module.

This settles the endpoint of THIS specified source gauge. It does not
evaluate the knot-dependent endpoint sum or identify the marked
geometric A-period. In particular it supplies no additional knot-volume
conjecture proof.

## 1. Canonical polynomial and exact unreduced Ward equation

Use Q=exp(2pi*i/N), N>=2, F_r=(Q;Q)_r, and

    v_N(z)=sum_(r=0)^(N-1) (-1)^r Q^(r(r-1)/2)z^r/F_r.

Let g_N(z)=sum_(r=0)^(N-1)c_r z^r be the CANONICAL degree-<N
representative of v_N(z)v_N(Qz) modulo z^N. It is the actual
primitive source gauge in
[the Fourier transport theorem](actual_source_fourier_twisted_traces.md),
whose regular-disk action was proved in
[the gauge-action note](actual_hilbert90_gauge_dilogarithm_action.md).

As an ordinary polynomial, before setting z^N=0, it obeys

    (1-z)(1-Qz)g_N(Qz)-g_N(z)
                 =-(2/N)z^N+c_(N-1)z^(N+1).       (1)

To prove this, first keep the full ordinary product
w_N(z)=v_N(z)v_N(Qz), including its degrees N,...,2N-2.
The exact Euler Ward equation is

    (1-z)v_N(Qz)=v_N(z)-z^N/N.

Multiplying its versions at z and Qz gives

    (1-z)(1-Qz)w_N(Qz)-w_N(z)
      =-z^N[v_N(z)+v_N(Qz)]/N+z^(2N)/N^2.          (2)

Hence the coefficient of z^N is -2/N, and coefficients below N
vanish. Removing the high tail of w_N does not alter that z^N
coefficient: its own degree-N contribution to the left side is
(Q^N-1)[z^N]w_N=0. The left side for g_N has degree at most N+1;
its top coefficient is Q^N c_(N-1)=c_(N-1). This proves (1).
Equivalently it gives the exact coefficient relation

    c_(N-2)=(1+Q)c_(N-1)-2Q/N.

Setting the polynomial argument z=1 in (1) now yields

    g_N(1)=2/N-c_(N-1).                            (3)

Both source terms in (1) are required. If (1) were replaced by
its homogeneous identity in z^N=0 before evaluation, the selected
endpoint would be changed.

## 2. The retained coefficient is an exact Gauss period

The root factorial identity F_(N-1)=N gives, coefficient by
coefficient,

    [z^(N-1-r)]v_N(z)=Q^(r+1)F_r/N, 0<=r<N.

For example this follows from
F_(N-1-r)=N(-1)^r Q^(r(r+1)/2)/F_r. Substituting it into
the convolution for c_(N-1) cancels every factorial and gives

    c_(N-1)=(1/N)sum_(r=0)^(N-1)
                            (-1)^r Q^(r(r-1)/2).   (4)

Thus (3)-(4) are an exact algebraic period evaluation of the
canonical endpoint at every level, including composite N. They
are not an identification of the nilpotent algebra with scalar
points. The representative and the degree-N source were fixed
before evaluation.

## 3. Direct Gaussian asymptotic, with the finite boundary retained

Put

    T_N=sum_(r=0)^(N-1)(-1)^r Q^(r(r-1)/2),
    omega_N=exp[-pi*i*(N+1)/4-pi*i/(4N)].

Then

    T_N=sqrt(N) omega_N+O(1),                     (5)
    c_(N-1)=omega_N/sqrt(N)+O(1/N),
    g_N(1)=-omega_N/sqrt(N)+O(1/N).               (6)

Here is a proof of (5) without importing an incomplete-Gauss-sum
estimate. On integer r the summand equals exp(2pi*i*f(r)), where

    f(x)=[x^2-(N+1)x]/(2N).

Periodize exp(2pi*i*f(x)) times the indicator of
[-1/2,N-1/2]. This is a piecewise smooth periodic function, and
zero is away from its discontinuities. Its symmetrically summed
Fourier series therefore gives the finite Poisson identity

    T_N=sum_(m in Z)^sym I_m,
    I_m=integral_(-1/2)^(N-1/2)
                       exp(2pi*i*(f(x)-m*x)) dx.  (7)

For N>=4, f' lies in [-3/4,1/2]. For every nonzero m, integration
by parts expresses I_m as

    [exp(2pi*i*(f(x)-m*x))/(2pi*i*(f'(x)-m))]_a^b
       +(1/(2pi*i)) integral_a^b
          f''(x) exp(2pi*i*(f(x)-m*x))/(f'(x)-m)^2 dx,

with a=-1/2, b=N-1/2. The second term is O(m^-2), uniformly
in N: f''=1/N, the interval has length N, and
|f'(x)-m|>=|m|/4. The boundary terms also have an absolutely
summable PAIRED bound. Both endpoints have
exp(-2pi*i*m*x)=(-1)^m, and

    1/(t-m)+1/(t+m)=2t/(t^2-m^2)=O(m^-2)

uniformly for -3/4<=t<=1/2. Hence the sum of all m!=0
terms in (7) is O(1). No separate divergent boundary sums
have been discarded.

For m=0, complete the square around a_0=(N+1)/2. This gives

    I_0=exp[-pi*i*(N+1)^2/(4N)] sqrt(N)
          *integral_(-(N+2)/(2sqrt(N)))^((N-2)/(2sqrt(N)))
                                     exp(pi*i*y^2) dy.

The complete Fresnel integral is exp(pi*i/4). It follows by
Gaussian regularization, and its two tails are O(1/R) by one
integration by parts beyond |y|=R. The displayed endpoints
have size comparable to sqrt(N), so replacing them by infinity
changes I_0 by O(1). Its complete value is sqrt(N) omega_N.
Together with the nonzero Fourier modes this proves (5).
The finitely many smaller levels do not affect the asymptotic.
Equations (3)-(4) finish (6).

In particular the exact resonant source gauge satisfies

    |g_N(1)|=N^(-1/2)[1+O(N^(-1/2))],
    log|g_N(1)|=-(1/2)log N+O(N^(-1/2)),
    (1/N)log|g_N(1)| -> 0.                       (8)

It is nonzero for all sufficiently large N. No all-level
nonvanishing claim beyond this is needed for (8).

## 4. Consequence for the actual source comparison

The operator gauge has a positive exponential norm on a regular
flat-metric chart, as already proved, while its canonical resonant
endpoint (8) has no positive exponential rate. Neither its
operator size nor a regular-chart dilogarithm value determines
this selected endpoint. The high coefficient in (1) becomes the
leading term of the endpoint; the source carry must be retained.

This endpoint is not the original figure-eight invariant. Already
at N=2, g_2(1)=1 whereas the original source identity for 4_1
gives Kashaev_2(4_1)=1+4=5. The whole-source proof for that knot
uses a separate positive product sum, not this universal gauge.
No equality with that invariant or a general knot period is
introduced here.

Thus this is a usable fully evaluated local source period, but it
does not close the selected geometric-period or volume-norm gate
for a general actual word. It specifies what has to be composed
with that word and its other source sectors before any volume
conclusion can follow.

The [audit](../experiments/audit_actual_primitive_gauge_endpoint.py)
and [saved results](../experiments/actual_primitive_gauge_endpoint_results.json)
check the canonical polynomial coefficients, the FULL unreduced
Ward equation and Gauss-period identity exactly at finite-field
roots. High-precision samples separately diagnose (5)-(8); the
uniform proof above establishes their asymptotic scope.
