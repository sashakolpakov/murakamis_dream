# A whole-source spectral upper bound from macroscopic ordinary-color pointing

28 October 2026. The actual source can be restarted at a positive fraction
of the color orbit, rather than only at fixed small colors. This gives a
quantitative upper bound for the FULL original Kashaev value in terms of
the classical roots of a specified actual all-level operator. All root
singularities and nearly singular steps are retained. There is no
unproved lower bound on a nonzero cyclotomic denominator in this argument.

The bound is proved below under an explicit classical-order condition.
It is sharp geometrically when its displayed classical spectral integral
is at most the hyperbolic-volume rate. That classical inequality, and
verification of the relevant operator for a broad knot class, remain
separate tasks. No broad volume-conjecture theorem is asserted here.

## 1. Actual inputs and the theorem

Fix a k-bridge presentation with k>=2, and use the ACTUAL reduced colors
C_j(q), q_N=exp(pi i/N), C_N(q_N)=K_N. The
[positive macroscopic color window](ordinary_color_macroscopic_normal_jet_window.md)
uses the original colored plat and its normalization. It bounds the
colors up to

    J_N=1+floor((N-1)/k).                            (1)

In addition to its polynomial fixed-jet bounds, the elementary complex
arc argument in Section 2 below gives, for any fixed A>4,

    sup_(|s|<=2N^(-A)) |C_j(q_N exp(s/N))|<=N^C
                  for 1<=j<=J_N.                  (2)

Constants depend on the fixed diagram and A, not j,N. A fixed scalar
multiple of N^C is harmless in every displayed polynomial bound.

Choose a specified ACTUAL all-level annihilator, retaining its original
peripheral factors and conventions:

    sum_(i=0)^d a_i(q,-q^j) C_(j+i)(q)=0,
    a_i in C[q^(+/-1),M^(+/-1)], d>=1.             (3)

Its fixed coefficients may lie in a number field; fix the intended
complex embedding. The identity is the original polynomial color
identity, not a conjectured quantization of a classical curve.
Remove a common q-1 power if needed. The additional classical-order
condition used here is

    a_d(1,M) is not identically zero.               (4)

Assume also that at least one a_i(1,M), i<d, is not identically zero.
This excludes an identically nilpotent classical companion; no
semisimplicity or generic eigenvalue separation is required.

Let T(x) be the d by d classical companion, with shift rows and last
row -a_i(1,M(x))/a_d(1,M(x)), where

    M(x)=-exp(pi i x),
    rho(x)=max{|L|: sum_i a_i(1,M(x))L^i=0}.        (5)

The finitely many leading-coefficient zeros are interpreted by improper
integration. Then

    limsup_(N->infinity) (1/N) log |K_N|
                  <= integral_(1/k)^1 log rho(x) dx.             (6)

More generally any actual family with polynomial complex source
packets at colors j/N->a satisfies the same result with lower endpoint
a. The bridge theorem supplies a=1/k without knowing K_N or any high
normal jet. An identically zero K_N is assigned logarithm minus infinity.

The exact Fourier energy E_N=|K_N|^2+O(N^C) consequently satisfies

    limsup (pi/N)log E_N
           <=2pi max(0, integral_(1/k)^1 log rho(x) dx).         (7)

The ordinary-color remainder used here is the independently proved
original positive trace estimate. Formula (6) is already a scalar
whole-source bound; (7) introduces no replacement model.

## 2. A tiny complex source disk from the real positive arc

For j in (1), the actual 2k-plat gives the real-arc bound

    |C_j(exp(i theta))|<=j^(k-1),
                 pi/(2N)<=theta<=pi/N.             (8)

At equality k(j-1)+1=N the upper endpoint follows by scalar Laurent
polynomial continuity from below. One does not differentiate a singular
path basis at the endpoint. The actual integral crossing formula bounds
the Laurent degree of C_j in q^(1/2) by D<=C_K j^2. For zero-framed
ordinary colors it is also harmless to use any fixed common angular
denominator; the following estimates change by fixed constants.

Here are details of the needed complex estimate. Put z=exp(i theta/h)
for that fixed integer denominator h, so the function is Laurent in z
with exponents between -D and D. Center the real arc at theta_c and
write

    t=tan((theta-theta_c)/(2h)),
    z=exp(i theta_c/h)(1+i t)/(1-i t).

Then p(t)=(1+t^2)^D C_j(z^h) is a polynomial of degree at most 2D.
The symmetric real t interval is [-tau,tau], tau comparable to 1/N.
Its supremum is at most

    (1+tau^2)^D j^(k-1)<=C_K j^(k-1).               (9)

Expand p(tau v) in Chebyshev polynomials. Each coefficient has modulus
at most twice the supremum, by its elementary cosine integral. For a
complex v with dist(v,[-1,1])<=delta<=1,

    |T_l(v)|<=exp(C l sqrt(delta)).                 (10)

Indeed solve w+w^(-1)=2v, choose |w|>=1, and use
T_l(v)=(w^l+w^(-l))/2. The elementary quadratic formula, compared
with a point of [-1,1], gives |w|<=1+C sqrt(delta).

For q=q_N exp(s/N), |s|<=2N^(-A), the complex angle differs from
the upper arc endpoint by -i s/N. Thus the normalized v is within
O(N^(-A)) of that endpoint. Equations (9)--(10) give

    |p(t)|<=C_K(2D+1)j^(k-1)
                            exp(C_K D N^(-A/2)).    (11)

Since D=O(N^2) and A>4, this is polynomial. Also |t|=O(1/N), so
|(1+t^2)^D| and its inverse are bounded by fixed constants. This
proves (2). This argument bounds the ACTUAL entire initial color
functions on the complex disk; it does not replace them by truncated
Taylor series.

That distinction will matter below. A Taylor approximation at s=0
need not cancel poles at OTHER nearby zeros of a leading coefficient.
Using the original analytic source retains those exact cancellations.

## 3. One small circle avoids every tail denominator with polynomial cost

Collect the s_0 distinct monomials of a_d(q,M). For a color j with
j larger than a fixed constant, its restriction to the complex orbit is

    g_(N,j)(s)=a_d(q_N exp(s/N),-(q_N exp(s/N))^j)
       =sum_(l=1)^s_0 c_l (-1)^(b_l)q_N^(a_l+b_l j)
                            exp[(a_l+b_l j)s/N].    (12)

The frequencies lambda_l=(a_l+b_l j)/N are real and uniformly bounded
for j<=N. They are distinct once j exceeds the q-exponent span: a
collision of different M powers would force j to be bounded. Their
pairwise differences have modulus at least 1/N.

The first s_0 derivatives at zero form a Vandermonde matrix applied
to coefficients whose moduli are the fixed nonzero |c_l|. The determinant
is at least N^(-s_0(s_0-1)/2) in modulus and its adjugate is bounded.
Consequently, for a fixed C_0,

    N^(-C_0)<=max_(0<=r<s_0)|g_(N,j)^(r)(0)|<=C_0. (13)

Normalize g by this maximum. All normalized functions solve a constant
coefficient ODE product_l(partial_s-lambda_l)g=0 with bounded
coefficients and initial jet norm one. The first-order system form and
its exponential series show that this is a compact family of entire
functions, uniformly on compact disks. Every limit has initial jet norm
one and is nonzero.

We record the elementary local consequence carefully. There exist
rho_0,c>0, depending only on s_0 and the frequency bound, such that
each normalized function has at most s_0-1 zeros in |s|<4rho_0 and,
after factoring all zeros zeta_l in |s|<3rho_0 with multiplicities,

    |g_normalized(s)|>=c product_l |s-zeta_l|
                                      for |s|<=rho_0.           (14)

For the zero count, otherwise take radii tending to zero and a compactly
convergent sequence with at least s_0 zeros in each disk. The nonzero
limit would have zero of order at least s_0 at the origin, contradicting
its initial jet norm one. Shrink a resulting uniform radius to obtain
4rho_0. For the quotient bound, pass to a subsequence of the bounded
number of zeros. On a circle between rho_0 and 2rho_0 avoiding their
limits, the quotients converge uniformly, and hence inside by Cauchy's
formula. A zero of the limit quotient inside rho_0 would, by the argument
principle on a small surrounding circle, force an additional zero of
the original functions there. All such zeros were factored. This
contradicts a quotient minimum tending to zero. The possible zeros
crossing |s|=3rho_0 stay away from the disk being estimated. Compactness
therefore gives the positive uniform c in (14).

There are at most (s_0-1)N zeros to avoid over ALL tail colors.
For each remove a radial interval of radius N^(-A-2) around |zeta_l|.
Their total length is O(N^(-A-1)), smaller than the length N^(-A)
of [N^(-A),2N^(-A)]. Choose a radius r_N outside this union.
Equations (13)--(14) prove, simultaneously for every tail color and
every point on this ONE circle,

    |g_(N,j)(s)|>=N^(-C_A), |s|=r_N.              (15)

No Diophantine estimate on g_(N,j)(0) is used. A nonzero zero may lie
arbitrarily close to zero inside the circle; the original source will
cancel its apparent pole. Exact zeros at s=0 are retained as well.

## 4. Transfer through the entire tail and its singular regions

Start at j_0=J_N-d+1. The initial companion vector consists only of
colors j_0,...,j_0+d-1 covered by (2), and j_0/N->1/k.
At every point on the circle in Section 3, propagate the exact
companion for (3). Denote the individual matrices by T_(N,j)(s).
Their entries have a polynomial bound from (15).

Away from the finite zeros of a_d(1,M(x)), they converge uniformly,
also uniformly in s on the circle, to T(x). On a fixed closed regular
interval, a direct positive metric gives

    limsup (1/N)log ||product T_(N,j)(s)||
                      <=integral log rho(x) dx,                 (16)

uniformly in s. To verify this without diagonalization, fix epsilon>0
and use H_epsilon(x)=sum_(n>=0)(T(x)^*)^n T(x)^n/
(rho(x)+epsilon)^(2n). On a compact matrix family this series converges
uniformly (bound the powers by a resolvent on an intermediate circle),
is continuous, and lies between I and C_epsilon I. In its norm a step
costs at most rho(x)+epsilon+o(1); neighboring metric changes are
1+o(1), uniformly. Summing logarithms proves (16) after epsilon tends
to zero. Include any isolated zero of rho in the exceptional set first.
This argument is valid for repeated roots and nonnormal companions.

We must also bound the steps near exceptional points, rather than
delete them. Let m be a bound on the orders of the classical leading
zeros. Outside distance N^(-epsilon_0) from them, with epsilon_0>0
sufficiently small, the coefficient error O(1/N) is less than half
the classical denominator, and

    ||T_(N,j)(s)||<=C dist(j/N,Z)^(-m).             (17)

Here A>4 makes the extra s perturbation smaller than O(1/N).
Inside those shrinking neighborhoods there are O(N^(1-epsilon_0))
steps; their polynomial bound from (15) costs exp(o(N)) in total.
Between that neighborhood and a fixed radius delta, summing the
logarithm of (17) costs at most

    C N delta(1+|log delta|)+o(N).                 (18)

This follows by comparing the monotone logarithm with its integral
on the color mesh; the shrinking core removes any near-grid anomaly.
Isolated zeros of rho with nonzero leading coefficient have bounded
matrix norm and cost O(N delta). Thus all exceptional neighborhoods
have a rate tending to zero as delta decreases.

Finally log rho is integrable. Upper root bounds use the rational
companion coefficients. For a fixed nonzero lower coefficient a_i,
the elementary-symmetric root formula gives

    rho^(d-i)>=|a_i/a_d|/binom(d,d-i).

Orders of zeros of the fixed analytic functions on the compact arc
are finite, so both upper and lower logarithmic bounds are integrable.
Combining (16)--(18) and sending delta to zero gives the full-tail
product bound with integral from 1/k to 1.

## 5. Recover the exact complete value, with every cancellation retained

On the chosen circle the generic recurrence identity gives

    C_N(q_N exp(s/N))
       =e_d^t [product_(j=j_0)^(N-d) T_(N,j)(s)]
                  (C_(j_0)(q(s)),...,C_(j_0+d-1)(q(s)))^t.      (19)

The right side uses the original source. Although its factors may
have poles INSIDE the circle, their full product in (19) is the
actual Laurent polynomial on the left and is holomorphic there.
Therefore ordinary Cauchy evaluation gives

    K_N=(2pi i)^(-1) integral_(|s|=r_N)
                                  C_N(q_N exp(s/N)) ds/s.      (20)

Its absolute value is at most the supremum on the circle. The initial
packet is polynomial by (2), and the transfer product has the rate
proved in Section 4. This proves (6). No source overlap, root-fiber
inverse bound, or assumption that normal data at color N are small
has entered the proof.

## 6. What is now a classical geometric question

A sufficient, independently checkable condition for the sharp upper
bound for a given actual operator is

    2pi integral_(1/k)^1 log rho(x) dx<=Vol(S^3 minus K).         (21)

Together with (3)--(4), this implies the desired original-source
limsup, not merely an auxiliary positive-state bound. Condition (21)
is NOT asserted for an arbitrary annihilator: multiplying by extra
operator factors can enlarge rho, and an actual operator's classical
support has to be determined rather than assumed to be the geometric
A-polynomial.

For k=2, a possible geometric proof of (21) is a continuously selected
dominant peripheral branch whose regulator starts at zero at x=1/2
and ends with absolute value at most Vol. One must verify its dominance
throughout the interval, including any changes at the unit circle;
switching freely between different regulator primitives is invalid.
The estimate (6) itself requires none of those geometric assertions.

This replaces an unspecified quantum boundary amplification by an
explicit classical spectral integral, under the stated order condition.
It does not yet verify (21) for a broad knot class or prove geometric
survival.

### A verified limitation of the scalar envelope

The independently derived [6_1 longitude quartic](six_one_classical_spectral_envelope_obstruction.md)
has a certified transverse modulus crossing at x=5/6 between DISTINCT
expanding eigenvalues. Hence rho is locally obtained by switching
analytic branches; it cannot be identified throughout that interval
with one fixed geometric branch. Its numerical half-integral has
2pi-scaled value about 3.44499, while the continued expanding branch
integrals are about 3.16396 and 1.41511. These integral values are
diagnostics, not certified volume comparisons or an actual quantum
operator calculation.

A separate [coherent classical-matrix diagnostic](classical_six_one_coherent_transfer_diagnostic.md)
has rates well below the scalar envelope at increasing levels.
This directs the next estimate toward phase-aware products and
continuously marked branch actions. It does not license replacing
the safe envelope in (6) by an unproved smaller number. In particular,
proving (21) for ALL two-bridge curves by asserting one dominant branch
would be an invalid next step.

A further [exact analytic conversion example](analytic_two_channel_conversion_counterexample.md)
shows that even replacing the scalar envelope by the maximum of complete
marked-branch actions is NOT a general adiabatic theorem. With distinct
nonzero roots, uniformly bounded analytic eigenframes and an O(1/N)
coupling, both individual actions can be zero while the actual selected
product has a positive exponential rate. The proof is a finite Gaussian
sum with an exact Fourier expansion. A separate
[polynomial-clock example](algebraic_clock_conversion_counterexample.md)
has an exact binomial proof. Neither example is a knot operator. They
show why a sharper bound must establish the actual source's conversion
cost, rather than infer it from the classical roots and slow variation.

## 7. Checks and coverage

[The actual-source audit](../experiments/audit_actual_macroscopic_a_spectral_upper_bound.py)
propagates the original figure-eight colors from the midpoint around
five tiny complex-q circles, through the full homogeneous recurrence,
and compares every output with the independent finite color product.
It also checks Cauchy recovery, the exact classical factor, and the
nearby-pole example explaining why the entire initial source is needed.
The general sparse-ODE zero argument is the proof in Section 3, not a
conclusion from those finite examples.


Its separate 5_2 diagnostic computes a classical cubic from the actual
Newton coefficient curve by the previously proved canonical map.
The half-interval integral numerically equals its known volume rate,
but that diagnostic does NOT certify an actual quantum operator or
the classical geometric comparison. It is labeled accordingly.

Coverage only: recurrence asymptotics and their connection with the
volume problem are established research topics; see
[Aptekarev--Dudnikova--Tulyakov (2021)](https://link.springer.com/article/10.1134/S1995080221110056).
Their introduction records earlier regularity hypotheses excluding
colliding and zero roots; their paper also discusses the nonregular
knot examples. This note makes no novelty claim and assumes none of
their proofs. Its source-window, small-circle, singular-region and
whole-value estimates are given above independently.
