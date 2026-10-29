# A source-preserving quadrature with an exponentially smaller error

28 October 2026. This proves a discrete-to-continuous comparison, including
the selected finite endpoints. It is a theorem for the displayed finite
factorial sum. The [finite whole-source transform](five_two_cyclotomic_transform_proof.md)
now proves that this is the ORIGINAL 5_2 invariant, including the whole
fixed-root meridian family. That identification is an exact finite
calculation, rather than an inference from finite checks.

The comparison removes the inner summation without choosing a saddle or
discarding a Fourier mode. Its TOTAL error is bounded by a logarithmic
factor times the already proved original figure-eight invariant. This
is useful because that error has a strictly smaller exponential rate
than the proposed 5_2 geometric contribution. The outer sum and the
nonzero geometric contribution of the remaining integral are not proved
by this result.

## 1. Reflection gives an entire interpolant

Write Q=exp(2 pi i/N), F_n=(Q;Q)_n, 0<=n<N, and m=N-1-n. Consider

    a_(n,j)=Q^[-n(n+2)-j(n+1)] F_n^3/(F_j F_(n-j)), 0<=j<=n.

Let Fhat be the exactly normalized interpolation in
[the factorial theorem](exact_factorial_interpolation_and_complex_contours.md).
The entire interpolation selected here is

    f_(N,n)(z)=Q^[-n(n+2)-z(n+1)]
                 F_n^3/[Fhat(z) Fhat(n-z)] * exp(2 pi i z).       (1)

Initially this is defined on the overlapping factorial strips. Reflection
and the integer shift m give the exact entire continuation

    f_(N,n)(z)=f_(N,n)(0) H_(N,n)(z)/F_m,
    H_(N,n)(z)=exp[-i pi z(z-N+1)/N] (Q^(z+1);Q)_m.             (2)

Here Q^z always denotes exp(2 pi i z/N). In fact

    1/[Fhat(z) Fhat(n-z)]
      =exp[-i pi(n-z)(n-z-N+1)/N] (Q^(z+1);Q)_m/N.

Substitution proves (2), including its constant by evaluation at z=0.
There is no branch choice or asymptotic step in this calculation.
In particular f(j)=a_(n,j) at EVERY allowed integer, and

    |f(0)|=|f(n)|=|F_n|^2.                                    (3)

The factor exp(2 pi i z) is essential to the bounds below. Its value is
one on the actual summation lattice. Its use is legitimate here because
the comparison is proved for the entire interpolant with the original
finite sum and its explicit endpoint terms retained.

## 2. Uniform endpoint bounds in a late-index region

Fix 0<delta<1/2 and assume

    (1/2+delta)N <= n <= N-1.                                  (4)

For a=0,n and real t, direct absolute values in (2) give

    |f(a+i t)|/|f(a)|=exp(pi lambda_a t) P_m(|t|),
    lambda_a=(2a+n-2N+2)/N,
    P_m(t)=product_(r=1)^m
          [1+sinh^2(pi t/N)/sin^2(pi r/N)]^(1/2).              (5)

At a=n the indices n+1,...,N-1 have the same sine magnitudes as
1,...,m. Thus (5) uses the same product at both original endpoints.

Since m<(N-1)/2, the factors for r and N-r are disjoint equal
pairs. The complete sine product gives

    P_m(t)^2 <= product_(r=1)^(N-1)
          [1+sinh^2(pi t/N)/sin^2(pi r/N)]^(1/2)
        =sinh(pi t)/[N sinh(pi t/N)] <= exp(pi t).              (6)

The identity follows by factoring w^N-1 at w=exp(-2 pi t/N),
and extends continuously to t=0. The last bound also follows from

    sinh(Ns)/(N sinh s)
       =(1/N) sum_(r=0)^(N-1) exp((N-1-2r)s) <= exp((N-1)s).

For the two endpoint lambdas, (4) implies

    |lambda_0| <= 3/2-delta-2/N,    |lambda_n| <= 1.

Consequently, uniformly in (4),

    |f(a+i t)| <= |F_n|^2 exp[(2 pi-pi delta)|t|].              (7)

For |t|<=1 one also has

    |f'(a+i t)| <= C(1+log N)|F_n|^2.                         (8)

To check (8), differentiate the Gaussian and the finite product in
(2). Each logarithmic derivative in the latter is bounded by
C/[N sin(pi r/N)] <= C/r, because r<=m<N/2 and |t|<=1.
Their sum is O(1+log N); (7) bounds the undifferentiated factor.
All constants in (8) can be absolute. No asymptotic estimate near
a zero endpoint factorial is being used.

## 3. Exact finite summation formula and its error

Contour integration gives the finite Abel--Plana identity

    sum_(j=0)^n f(j)
       =integral_0^n f(s) ds +(f(0)+f(n))/2
        +i integral_0^infinity
          [f(i t)-f(-i t)-f(n+i t)+f(n-i t)]
                    /(exp(2 pi t)-1) dt.                     (9)

For clarity, its hypotheses are verified directly here. The function
in (2) is entire. On every vertical line 0<=Re z<=n its upper growth
rate as Im z tends to infinity is at most pi(2n-N+1)/N < pi.
Its lower growth rate is at most pi(3N-3-2n)/N < 2 pi, by (4).
The bound is uniform in this closed horizontal interval for each
fixed N,n. Thus the horizontal edges disappear when the residue
contour with kernels (exp(-2 pi i z)-1)^(-1) above the real axis
and (exp(2 pi i z)-1)^(-1) below it is sent to infinity.
The real edges combine into the integral in (9), the two vertical
edges give its displayed differences, and half-circles at 0,n
give the two half endpoint values. This proves (9) for this
interpolant, rather than assuming a formal quadrature expansion.

For 0<t<=1, (8) bounds the numerator by
C t(1+log N)|F_n|^2. For t>=1, (7) and the denominator in (9)
give an integrable bound C exp(-pi delta t)|F_n|^2. Including
the two half endpoint terms proves

    |sum_(j=0)^n a_(n,j)-integral_0^n f_(N,n)(s) ds|
          <= C_delta (1+log N)|F_n|^2.                       (10)

In particular the finite endpoint source has been bounded, not
declared zero, and every Poisson contribution implicit in the
original finite lattice sum is accounted for by the exact error.

## 4. The total error is controlled by the original figure-eight period

Let I_(N,delta) be the sum of the integrals in (10) for all n
satisfying (4), and let S_(N,delta) be the same range of the
original double sum. The triangle inequality in (10) gives

    |S_(N,delta)-I_(N,delta)|
       <= C_delta(1+log N) sum_(n=0)^(N-1)|(Q;Q)_n|^2
        = C_delta(1+log N) K_(4_1),N.                         (11)

The final equality is the independently proved original-state
[figure-eight source identity](figure_eight_whole_source_identity.md).
Therefore

    limsup N^(-1) log|S_(N,delta)-I_(N,delta)|
              <= Vol(4_1)/(2 pi).                           (12)

This is an actual global exponential comparison for the specified
late-index sum. It does NOT assert that I_(N,delta) has a nonzero
geometric contribution, or remove the outer discrete summation.
The low-index part also requires its separate absolute bound.

## 5. A reusable criterion for other finite bridge convolutions

The same proof applies to

    h(z)=C exp[-i pi z^2/N+i pi beta z/N]
                      (Q^(z+1);Q)_m,
    n=N-1-m, m<=(N-1)/2, beta real.

If, for some epsilon>0,

    max(|-beta-m|,|2n-beta-m|)/N + 1/2 <= 2-epsilon,          (13)

then its finite quadrature error is at most

    C_epsilon(1+log N)(|h(0)|+|h(n)|),                       (14)

provided |beta|/N is bounded; this last bound in fact follows from
(13) and 0<=m<N. Multiplication by exp(2 pi i k z), k integer,
retains the exact lattice values and replaces beta by beta+2kN.
Condition (13) decides when that choice gives the required bound.

This criterion is checkable from the actual finite transfer rather
than a conjectured geometric cycle. If a bridge convolution has
this form and its endpoint sums have a smaller proven rate, it
can be removed with a controlled error. No assertion is made that
all knot diagrams admit such an ordering or such endpoint bounds.

[Finite-sum, entire-interpolant and exact contour diagnostics](../experiments/audit_source_preserving_inner_quadrature.py).

