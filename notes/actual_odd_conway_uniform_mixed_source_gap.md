# A whole mixed-color gap for arbitrary robust odd-coupon Conway factors

29 October 2026. For every retained C(FG), with F and G robust,
arbitrary fixed pure or signed odd-half-twist coupons have a uniform
gap for ALL actual alias sectors and for the entire physical color
complement. The estimate permits arbitrarily many aliases and arbitrary
fixed turns and branching. It uses supporting planes of the actual
concave source action, with the full Newton alias profile.

The minimal retained factor C(A), A=h^3, is EXCLUDED from this theorem.
Its complete odd-coupon asymptotic is already proved, but the stronger
leaf bound used here does not hold for it. No claim for its whole
mixed-color source follows by ignoring that exception.

## 1. Exact changed source and statement

Fix a literal C(FG) and a choice epsilon_l in {0,+1,-1} at each
individual leaf. The actual mixed leaf is

    h_j^epsilon=T(R^epsilon L_j), 1<=j<=N.

All turns, products, pivots and the original marked cylindrical
closure are unchanged. Write its exact full-algebra decomposition
as C_j^epsilon+A_j^epsilon, obtained by applying the half-twist
transport to the pure core and alias separately. At epsilon=0 this
is the pure split. Let Z_N(j) be the original closed source and
Z_N^core(j) the circuit using only the C_j^epsilon.

Let F0 be the complete PURE maximizing action. The
[complete odd-source theorem](actual_odd_conway_newton_transport.md)
already proves the nonzero complete asymptotic with this same F0.
There is gamma>0 such that, uniformly over the ENTIRE physical color
cube, for all sufficiently large N,

    |Z_N(j)-Z_N^core(j)| <= exp[N(F0-gamma)].            (1)

For every fixed sufficiently small delta>0 there is gamma_delta>0
such that

    max_(some N-j_l>=delta N) |Z_N(j)|
                       <=exp[N(F0-gamma_delta)].       (2)

Both parities and composite levels are included. The expression,
coupon signs and delta are fixed before N tends to infinity. These
are whole original-source bounds, including all normal coordinates;
no semisimple quotient or positive-matrix replacement is used.

## 2. A stricter leaf interval for every C(FG)

Use the port variables of the
[strict-quarter theorem](actual_conway_strict_leaf_quarter_bound.md).
At every proper robust macro-port of this CLOSED factor, they obey

    0<X<1, 0<Y<1.

At a proper seed A=h^3 its three leaf cotangents all equal X, and
its port invariant is Y=1/(4X^2-1). Therefore Y<1 gives

    1/sqrt(2)<X<1,
    1/4<a_l< a0:=atan(sqrt(2))/pi <1/3                 (3)

for EVERY complete maximizing leaf label a_l. This is why both root
children must be robust: C(A) instead has X=1/2 and its leaves lie
at atan(2)/pi, outside (3).

## 3. One supporting plane dominates an alias at every output

Put

    g(a)=J(2a)-4J(a),
    k(u)=-2J(u/2), 0<=u<=1,
    J(u)=integral_0^u log(2sin(pi t))dt.

The new full-Newton transport theorem gives the global alias rate k.
For every a in [1/4,a0] its tangent to g satisfies the UNIFORM strict
inequality

    k(u) <= g(a)+g'(a)(u-a)-c0   for all 0<=u<=1,       (4)
    c0=g(1/4)-(3/4)log2=2Catalan/pi-(3/4)log2>0.

Here is a direct proof, including both ends of the output interval.
Write s=g'(a)=2log cot(pi a), so -log2<=s<=0. The function k is
strictly concave in the interior, with

    k'(u)=-log(2sin(pi u/2)).

Its slope decreases from +infinity to -log2. The maximizer u(a) of
k(u)-su lies in [1/3,1], and is characterized by k'(u)=s, with
u=1 at s=-log2. The minimum tangent gap is

    I(a)=g(a)+s(u(a)-a)-k(u(a)).

On the interior, I'(a)=g''(a)(u(a)-a)<0, since u(a)>=1/3>a.
Continuity extends this monotonicity to the endpoints. Thus

    I(a)>=I(a0)=g(a0)-(1-a0)log2.

Since g' decreases from zero to -log2 on [1/4,a0], integration gives
g(a0)>=g(1/4)-(a0-1/4)log2. This proves (4).

For an explicit elementary positive certificate, the alternating
Catalan series gives Catalan>1-1/9=8/9. Using pi<22/7 and log2<7/10,

    c0>56/99-21/40=161/3960>0.                         (5)

No numerical optimizer or special-function decimal is needed to
establish the margin.

## 4. Sum the source supporting planes before estimating states

For an odd coupon its all-color core has the uniform upper rate

    g_tilde(u)=g(max(u,1/4)), 0<=u<=1/2,               (6)

by the [actual mixed-source recurrence](actual_pretzel_global_core_spectral_gap.md).
In that recurrence's normalization, the modulus of the actual Newton
core coefficient is exactly

    N^2 s_(2r)/s_r^4 * |V_(h,r)|.

Its complete factorial rate is g, so the recurrence bound adds E and
g+E is precisely g_tilde. No coefficientwise domination is inferred
by applying an oscillatory transform to the pure core inequality.
The error beyond this rate is uniformly o(N), including all colors
and both index endpoints. A pure core has rate at most g(u), hence
also at most g_tilde(u). At a complete maximizing leaf a_l in (3),
concavity gives

    g_tilde(u)<=g(a_l)+g'(a_l)(u-a_l).                 (7)

For every alias, the [full Newton transport bound](actual_odd_conway_newton_transport.md)
gives rate at most k(u) on its ENTIRE range 0<=u<=1, so (4) applies.
A pure alias has polynomial coefficients and rate zero; it obeys
the same upper bound because k(u)>=0 on [0,1].

Every actual positive Newton multiplication has action m on
max(x,y)<=z<=x+y<=1. This domain is convex, m is concave, and at
its complete strict state w_* its tangent gives

    m(w)<=m(w_*)+grad m(w_*) dot(w-w_*).                (8)

Expand the exact original source according to its alias subset S.
Its state support may allow alias leaf outputs above one half, but
every product still lies in the SAME domain in (8). The actual
turn equations and final closing input relation are the same affine
relations as before. Thus one may add (4),(7),(8) for any one of
these expanded states, even when it lies outside the pure-leaf
polytope. All linear terms cancel by stationarity of the original
pure action in its free wire coordinates. The resulting upper rate is

    F0-|S|c0.                                         (9)

This is the essential reason the argument handles multiple aliases.
No assertion that their products vanish is made; indeed those
products generally do not vanish after an odd half twist.

At finite N use the actual scaled wire labels r/N, which remain in
the domains of all the supporting inequalities. Their turn and closing
equations have right-hand side 1-1/N. Thus the cancellation of the
fixed tangent linear terms has only O(1/N) error; multiplying by N
costs O(1). The endpoint-uniform factorial errors cost O(log N).
The fixed tree has only polynomially
many Newton states and finitely many alias subsets. Their uniformly
subexponential coefficient factors can therefore be absorbed into
half the fixed margin in (9). Summing all nonempty S proves (1).

## 5. The complete physical color complement

Replace g by g_tilde at all leaves to get a convenient common
majorant for the all-core circuit. It is concave and agrees with
the pure action near its strict complete optimizer, by (3).
Consequently that optimizer is its unique global maximum with
value F0. Outside a small fixed neighborhood W of that state the
majorant has a strict compactness gap, uniformly over all colors.
The finite physical supports have the same inequalities and affine
relations with O(1/N) shifts. Every convergent sequence of finite
states therefore limits to the stated compact support. The same
outside-W gap, slightly reduced, holds for all sufficiently large N.

Choose beta<1/2 larger than every leaf coordinate throughout W.
For an odd coupon, the actual mixed-source theorem gives, uniformly
for delta N<=h<=floor((N-1)/2) and r<=beta N,

    log|core_coefficient_(N,h,r)|
             <=N[g_tilde(r/N)-gamma(delta,beta)+o(1)], (10)

where gamma(delta,beta)>0. It retains the actual terminal source,
both recurrence branches, and repeated-root endpoint colors. For
a pure coupon the exact factorial formula gives the analogous
strict loss from

    g_chi(u)=g(u)-[J(u-chi)+J(u+chi)-2J(u)],
    chi=h/N>=delta,

uniformly near its interior complete coordinate; if h>r its
coefficient is zero. A physical color j<=floor(N/2) has zero core
and needs no further core estimate.

If some deficit is at least delta N, every all-core state either
lies outside W and loses the majorant gap, or lies inside W and
loses the positive amount in (10) at that leaf. Uniformity and
the polynomial state count prove a strict whole-core complement
gap. Combine it with (1) to obtain (2).

## 6. Scope of the advance

This proves the full physical color-gap hypothesis needed for
long-filling transfer for arbitrary fixed coupon patterns on C(FG).
The complete signed source is already nonzero by its separately
proved local coherent amplitude and global plateau bound.

The [exact finite analytic packet](actual_odd_conway_complex_color_packet.md)
for these CHANGED mixed coupons and the
[marked odd deformation](actual_odd_conway_marked_peripheral_deformation.md)
are proved separately. Literal connectivity is supplied by the
[half-partner theorem](actual_conway_half_twist_partner_geometry.md).
Together they give the [long-filled knot and link equality](actual_odd_conway_long_filling_volume.md).
None of these interfaces is obtained by substituting the unchanged
pure colored packet for the actual odd source.

Audit: [exact port, tangent and transport certificates](../experiments/audit_actual_odd_conway_uniform_mixed_source_gap.py).
The all-expression proof is the supporting-plane argument above,
not an extrapolation from finitely sampled source values.

The mixed-source gap requires a separately established changed complex packet and marked geometric deformation.