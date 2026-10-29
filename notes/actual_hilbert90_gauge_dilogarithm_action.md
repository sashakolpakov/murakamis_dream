# The actual primitive Hilbert-90 gauge has a dilogarithm action and exponential norm

27 October 2026. The explicit cyclic source gauge in
[the actual Fourier twisted-trace theorem](actual_source_fourier_twisted_traces.md)
has a rigorously computable exponential scale, even in the flat
right-regular metric. This is an ACTUAL gauge from the original
source construction, not an arbitrary central rescaling of a state.
It proves why solving its norm-one transport equation does not by
itself give a subexponential comparison to a geometric period.

The result also identifies a concrete dilogarithm action of this
source gauge on a regular chart. It does not identify that chart
with the marked geometric A-component or its Bloch regulator.

## 1. The specified actual gauge

Let q=exp(pi*i/N), Q=q^2, h=2pi*i/N and z^N=0. The primitive
k=1 source sector has the unique scalar-polynomial gauge with
constant term one

    g_N(z)=v_N(z)v_N(Qz)
          =[u_N(z)u_N(Qz)]^-1,                   (1)
    u_N(z)=sum_(a=0)^(N-1) z^a/(Q;Q)_a,
    v_N=u_N^-1 in the nilpotent algebra.

It solves g_N(Qz)/g_N(z)=1/[(1-z)(1-Qz)], eliminating the
corresponding inner twist of the source automorphism. The
constant-term and transport equation make it unique: a quotient
of two gauges would be Q-invariant, hence constant in degree<N.
The full matrix comparison can have other choices; no uniqueness
claim for all matrix gauges is made.

The CANONICAL polynomial representative of (1), of degree<N, is
exactly the Taylor polynomial through degree N-1 of exp(L_N(z)),
where

    L_N(z)=sum_(a=1)^(N-1)
                    (1+Q^a) z^a/[a(Q^a-1)]
          =-i sum_(a=1)^(N-1) cot(pi*a/N) z^a/a.   (2)

Indeed the logarithm of v_N in the nilpotent algebra is
sum z^a/[a(Q^a-1)]. Adding its shifted logarithm gives (2).
This establishes the relation to the ACTUAL finite gauge before
using analytic estimates. It is not an unproved resummation of
quantum jets.

## 2. Uniform asymptotics of the actual polynomial on a fixed disk

For |z|<=1/4 one has, uniformly as N grows,

    g_N(z)=exp[(2/h) Li_2(z)+O(1/N)].            (3)

The same statement with the opposite sign holds for the
canonical degree-<N representative of g_N^-1. In particular
these finite polynomials have no zero on that disk for all
sufficiently large N.

Here is a proof that retains the truncation error. First, on every
fixed disk |z|<=rho<1,

    L_N(z)=(2/h)Li_2(z)+O(1/N).                 (4)

For a<=N/2 use the uniform elementary estimate
cot(t)=1/t+O(t) on 0<t<=pi/2. Dividing its error by a gives
O(1/N) per coefficient, whose sum against rho^a remains O(1/N).
For a>N/2, the inequality

    |cot(pi*a/N)| <= N/[2 min(a,N-a)]

gives a tail O(rho^(N/2) log N), and the omitted tail of Li_2
is smaller. This proves (4) with both root endpoints accounted for.

Put G_N=exp(L_N) as an ordinary analytic function. On |z|=1/2,
the coarser |cot(pi*a/N)|<=N/2 gives

    |L_N(z)| <= (N/2)log 2,
    |G_N(z)| <= exp[(N/2)log 2].

Cauchy's coefficient bound and the degree-N Taylor tail therefore
give, throughout |z|<=1/4,

    |G_N(z)-g_N(z)| <= 2 exp[-(N/2)log 2].       (5)

Meanwhile (4) gives

    |G_N(z)| >= exp[-N Li_2(1/4)/pi-O(1/N)].

For example Li_2(1/4)<=13/48, so Li_2(1/4)/pi is strictly
smaller than log(2)/2. Thus (5) is exponentially small RELATIVE
to G_N on the entire disk. Combining it with (4) proves (3)
for the actual canonical polynomial. Replacing L_N by -L_N
proves the inverse statement by the identical estimate.

The Taylor-tail estimate is essential. Nilpotent equality alone
would not justify evaluating its analytic exponential away from
zero, as the nonzero endpoint carry in
[the meridian half-step theorem](actual_euler_meridian_half_step.md)
explicitly demonstrates.

## 3. A positive exponential lower bound for this comparison gauge

Take w=i/4 and set

    c=Im Li_2(i/4)/pi > 0.

The alternating power series proves

    Im Li_2(i/4) >= 1/4-(1/4)^3/9=143/576.

Equation (3) gives the precise scalar-gauge rate

    log|g_N(i/4)|=c N+O(1/N).                    (6)

To pass from this polynomial value to an ACTUAL finite operator,
use the flat right-regular basis f^a e_j. The operator R_f is
a truncated shift with unit coefficients. For |x|=1, its
argument xR_f has norm one, and the powers applied to a degree-zero
basis vector are orthogonal. If g_N(z)=sum c_a z^a, this gives

    ||g_N(xR_f)|| >= (sum |c_a|^2)^(1/2)
                    >= sqrt(15/16)|g_N(i/4)|.    (7)

The second inequality is just Cauchy--Schwarz for evaluation at
|w|=1/4. Multiplication by x^a changes no coefficient norm.
Thus this specified comparison gauge has exponential operator
growth, with liminf N^-1 log||g_N(xR_f)||>=c. Applying the
inverse version of (3) at -i/4 proves the same lower bound
for its inverse. Its condition number therefore has liminf
logarithmic rate at least 2c.

All these operators are unipotent: their diagonal entries and
determinants are one. The source transport is cyclic and obeys
its exact norm-one equation. Those algebraic facts coexist with
the exponential norm in (7). This result concerns the flat
coefficient metric. A nonunitary physical fusion change requires
its own metric comparison.

## 4. Implication for the intended torsor proof

The primitive source transport is explicitly SOLVED at each level,
and its gauge action is the specified dilogarithm in (3). Its
comparison is not tempered. A proof may carry this action into
the marked regulator rather than try to discard the gauge as a
normalization. Which combination of actions and source sectors
is selected by the original knot word remains to be proved.

This establishes neither a counterexample to the volume conjecture
nor an exponential estimate for the knot invariant. The number c
above is a gauge-chart value, not a knot's hyperbolic volume.
It does not rule out a different whole comparison with controlled
norm. It does rule out inferring such control for this actual
primitive gauge solely from Hilbert 90, finite cyclicity,
unipotence or determinant one.

The rigorous uniform normal-form estimate (3) is the new local
period/action comparison here. The nonzero selected geometric
image and global sector/cancellation estimates remain open.

Subsequent direct source calculations now distinguish that
operator norm from selected local periods. The
[canonical resonant endpoint](actual_primitive_gauge_resonant_endpoint.md)
is an explicit Gauss period of size N^-1/2. The
[normalized top-coefficient period](actual_gauge_period_selects_algebraic_point.md)
selects the algebraic point 2 on fixed polynomial observables
and intertwines fixed ordered gauge meridian steps. Thus this
specified source has an evaluated local leading period, not
just an exponential operator estimate. Its full knot-word
coupling and selected hyperbolic action remain unproved.

[The high-precision diagnostic](../experiments/audit_actual_hilbert90_gauge_action.py)
and [saved output](../experiments/actual_hilbert90_gauge_action_results.json)
compare the literal finite v_N(z)v_N(Qz) polynomial with exp(L_N)
and its dilogarithm action. The theorem rests on the uniform proof
above; numerical rate samples are not used as a proof. Another
agent independently checked its source-gauge orientation, the
Cauchy remainder, both coefficient tails and the operator lower bound.
