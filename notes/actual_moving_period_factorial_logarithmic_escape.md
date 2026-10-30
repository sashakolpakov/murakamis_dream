# Moving-period factorial normals along logarithmically escaping heads

30 October 2026. Independently reviewed source estimate. The marked Gamma
factorial remains controlled when a head has imaginary part of order
N log N. This is a bound for the actual factorial factors and fixed
quantum jets. It does not provide a packet for a polynomial whose
critical points merge, or cross an original zero or pole divisor.

## 1. The precise source factors and growing charts

Use EXACTLY the interpolant Fhat_P and its logarithmic mark in
[the moving-period factorial theorem](actual_moving_period_factorial_normals.md),
with P=pi i/(pi i/N+epsilon), d=N-1 fixed. Put L_N=1+log N.
Fix positive constants delta,C. The new interior arguments satisfy

    delta <= Re(z/N) <= 1-delta,
    |Im(z/N)| <= C L_N.                                  (1)

An exterior argument may instead have |Re(z/N)|<=C and
delta<=|Im(z/N)|<=C L_N. Choose a fixed integer shift k_N=O(N)
which puts its real part in a smaller interior strip, and use the
original unit recurrence for that SAME function. The shift stays
fixed when epsilon moves. Fixed physical integer arguments 0,...,d
are also allowed, by their exact finite factorials.

For a fixed finite number of these arguments, there are constants
c,C_1, independent of N and the arguments, such that on

    |epsilon| <= rho_N=c/[N^2 L_N^2]                      (2)

every factor is holomorphic and nonzero, and its relative value and
inverse are bounded by C_1. In particular, for every fixed j,

    |partial_epsilon^j Fhat_(P(epsilon))(z)|_(epsilon=0)
      <= j! C_1 (C_1 N^2 L_N^2)^j |Fhat_N(z)|.            (3)

The same assertion holds for products and inverses of a fixed number
of those factors, their normalized local square-root gauges, and
retained powers zeta^E with |E|<=C N^2 L_N^2. All exponential
root values and integer-linear characters remain part of the source.

## 2. A direct differentiated Gamma-product bound

The convergent product defining G_P gives, at FIXED z,

    partial_P Log G_P(z)=-z/P
      +sum_(k>=1) { k psi(Pk+z+1)-k psi(Pk-z)
                                         -(2z+1)/P }.    (4)

It suffices first to work on |P-N|<=c/L_N. All Gamma arguments
have positive real part there. Their real parts are at least c_delta N
for k=1 and comparable to Nk for k>=2. Take

    K=ceiling(C_2(1+|z|/N)), C_2 sufficiently large.

For k<=K, the uniform right-half-plane digamma expansion
psi(w)=Log w+O(1/|w|) applies. Both arguments have size at least
c_delta N. Their modulus ratio and the difference of their marked
arguments are bounded uniformly: the large imaginary parts enter with
opposite signs, and the real-part distance to the strip endpoints
is fixed. Hence

    |psi(Pk+z+1)-psi(Pk-z)|<=C_delta,

and the first K terms of (4) have total size O(K^2+K L_N)=O(L_N^2).
This includes the case that z stays bounded in scaled coordinates.

For k>K, |z+1|/|Pk|<1/4. Expanding the two digammas about Pk
shows that their 1/(Pk) term is (2z+1)/(Pk), while their
1/(Pk)^2 terms are EQUAL and cancel. More explicitly the latter
coefficient of psi(w+a) is -a^2/2+a/2-1/12, which has the same
value at a=z+1 and a=-z. The uniform next remainder gives

    |k[psi(Pk+z+1)-psi(Pk-z)]-(2z+1)/P|
                      <=C(1+|z|)^3/(N^3 k^2).            (5)

One may obtain (5) directly by differentiating the convergent
Gamma-ratio expansion on a fixed larger relative P disk; the same
1/k cancellation and uniform |z/(Pk)|<1/4 give its bound. Summing
(5) costs O((1+|z|/N)^3/K)=O(L_N^2). The initial -z/P term is
smaller. Therefore

    |partial_P Log G_P(z)|<=C L_N^2.                      (6)

The marked elementary exponential converting G_P to Fhat_P has
P derivative -pi i z(z+1)/(2P^2), also O(L_N^2).
Since |P'(epsilon)|=O(N^2),

    |partial_epsilon Log Fhat_P(z)|<=C N^2 L_N^2.         (7)

Disk (2) lies inside the P neighborhood just used. Integrating the
actual logarithmic derivative along that disk proves the two-sided
relative bound, and Cauchy's formula gives (3). No principal
logarithm is reset, and no root-only reflection is differentiated.

For completeness, the digamma estimates used here follow from the
same uniform complex-sector Stirling expansion used to construct
the original product. The Gamma arguments lie in the right half-plane,
so its fixed sector can include angles up to pi/2. The finite sum
and tail bounds above make explicit their dependence on the growing
imaginary argument; a compact-set estimate is not silently reused.

## 3. Exterior rows, fixed endpoints and original gauges

For an exterior row the O(N) fixed unit shifts introduce factors
1-exp[2(z+j)Log zeta]. Their scaled imaginary parts remain at least
delta/2 on (2). Thus

    |exp[2(z+j)Log zeta]/(1-exp[2(z+j)Log zeta])|<=C_delta.

Each logarithmic epsilon derivative has size O(N L_N), so the
whole shift product costs O(N^2 L_N), within (7). Large or small
absolute magnitudes of individual factors are NOT bounded away:
only their relative variation is being estimated. These magnitudes
and all phases remain in the root value.

For a fixed physical integer n<=d, the original finite product
has logarithmic derivative O(N^2 L_N), including n=d. Its known
relative disk contains (2). This keeps the endpoint N-1 fixed
rather than replacing it by P-1. Combining the bounds proves the
statement for any fixed product, ratio and locally normalized square
root. A marked monomial zeta^E has logarithmic derivative E, so it
has precisely the additional cost claimed after (3).

Consequently the actual moving-factorial cup and cap factors at
heads of size O(N log N) have polynomial fixed-jet cost whenever
their arguments obey these hypotheses. The same is true of their
specified boundary gauges. This does not give a relative estimate
for a SUM of white-polynomial terms, and does not replace the actual
large generic white by its root-colliding small partner.

## 4. What this resolves at the resonant framing boundary

For an actual clock X(r) asymptotic to c r^(2e), e=+1 or -1,
on a marked ray r=N R with R in a compact set avoiding zero,
its head z=Log X/(2Log q0) has |Im(z/N)|=O(log N).
On a fixed logarithmic sheet with bounded real part it falls into
the nonreal exterior class above for all sufficiently large N.
Thus its large imaginary lift by itself is tame for the actual
factorial normals. No bounded-lift hypothesis is falsely invoked.

In contrast, a clock tending to one can give a factorial argument
approaching an integer zero or pole. Nor does this theorem control
a white numerator's endpoint saddle or its resonant coefficient
sum. Those need their own exact small-argument products or turning
analysis. The original finite support, generic normal, cotangent
measure and selected global period remain unchanged and unproved
by this estimate.

The [focused audit](../experiments/audit_actual_moving_period_factorial_logarithmic_escape.py)
and [results](../experiments/actual_moving_period_factorial_logarithmic_escape_results.json)
retain 12 independent Gamma-tail comparisons, 48 two-sided relative
disk checks, 12 genuine fixed-index normals, 12 exact marked unit
recurrences and 12 actual opposite-head cup gauges, at 85 digits.
The maximum identity error was 2.18e-75. These are diagnostics of the
specified function; the uniform estimate is proved above.

Independent parent and geometry reviews passed the full proof,
including the growing Gamma domain, near/tail cancellation, nonreal
shift nonvanishing, fixed endpoint and marked quadratic gauges.
Both freshly replayed the focused audit successfully. Their scope
is the relative factorial/cup estimate and its genuine fixed jets,
not an absolute magnitude, turning packet or global period.
