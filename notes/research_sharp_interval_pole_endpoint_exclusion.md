# A spectral-pole endpoint cannot maximize the sharp shared functional

Unpublished workspace analytical theorem, 31 October 2026. Root and coherent
completed full internal analytical reviews; this is not external peer review. This is a calculus theorem for
the ORIGINAL full-interval sharp coefficient majorant. It uses the actual
unused prefix/suffix logarithms and makes no lower asymptotic or nonzero
claim for finite coefficients at sampled spectral zeros.

## 1. Statement with the exact gain

Fix 0<=mu<nu<=1, w=nu-mu>0, and any closed outer degree 0<=xi<=w.
Use the original sharp full-row functional

    H_delta=B_delta+inf_(l in R)[Phi_delta(l)-xi l],
    B_delta=int_0^mu log|alpha_delta(t)|dt
                       +int_nu^1 log|alpha_delta(t)|dt,
    Phi_delta(l)=int_mu^nu log Lambda_delta(t;exp(l),1)dt,
    alpha_delta(t)=4[cos^2(pi delta)-sin^2(pi t)].       (1)

The two simple spectral poles at 0<delta_0<1/2 are

    p_-=1/2-delta_0, p_+=1/2+delta_0.

Assume at least one endpoint mu or nu equals one of these poles.
Let m be the number of such endpoint contacts, so m=1 or2. There
is a sign s in {+1,-1} such that delta_epsilon=delta_0+s epsilon
moves every contacted pole INTO the fixed active interval [mu,nu].
For all sufficiently small epsilon>0,

    H_(delta_epsilon)-H_(delta_0)
                       =m epsilon log(1/epsilon)+O(epsilon). (2)

The constant is independent of xi, including xi=0,w, and independent
of the outer Cauchy tilt. It is locally uniform on a compact fixed-
contact stratum: delta stays inside(0,1/2), w stays positive, and
every noncontact endpoint-to-pole distance has a positive lower bound.
No uniformity as w->0 or delta approaches0,1/2 is asserted.

Thus no such positive-length datum can maximize H with a free real
spectral coordinate. The same conclusion holds in the original
shared-flow problem: varying only this delta changes none of its
face degrees, protected targets or row supplies.

## 2. There is always a compatible inward direction

The four single-contact choices are

    mu=p_- : s=-1,     nu=p_- : s=+1,
    mu=p_+ : s=+1,     nu=p_+ : s=-1.                (3)

Both endpoints cannot equal the same pole because mu<nu. The only
possible two-contact case is mu=p_-, nu=p_+, where s=-1 moves the
lower pole right and the upper pole left. Thus no two endpoint
contacts demand conflicting directions. Choose epsilon smaller
than the fixed interval length and the other indicated separations.
Protected mu=0 or nu=1 cannot itself be a pole at interior delta,
but it is permitted as the other endpoint throughout this proof.

## 3. The original unused products supply one logarithmic gain per contact

The exact factorization is

    log|alpha_delta(t)|=log4
       +log|sin(pi(t-p_-(delta)))|
       +log|sin(pi(t-p_+(delta)))|.                (4)

For delta in a compact subset of(0,1/2), write each sine logarithm
as log|t-p| plus log(|sin(pi(t-p))|/|t-p|). The latter extends
smoothly through t=p and has uniformly bounded first derivatives
on t in[0,1]. Its variation in either outside integral is O(epsilon).

Suppose first that p=mu and p moves to mu+epsilon. Its lower unused
prefix changes by EXACTLY

    int_0^mu [log(mu+epsilon-t)-log(mu-t)]dt
      =(mu+epsilon)log(mu+epsilon)-mu log mu
                                      -epsilon log epsilon
      =epsilon log(1/epsilon)+O(epsilon).          (5)

Here mu is bounded away from0 because it is an interior spectral
pole. The same pole's upper unused suffix is separated by w>0
and changes by O(epsilon). If p=nu and moves to nu-epsilon, the
upper unused suffix has the same expression with mu replaced by
1-nu, while the prefix changes by O(epsilon).

Any other pole not at an outside endpoint contributes O(epsilon),
even if it lies INSIDE an unused interval. To see this without
differentiating an absolute singular integrand, use the exact primitive

    F(r)=r log|r|-r, F(0)=0,
    int_a^b log|t-p|dt=F(b-p)-F(a-p).

Its p derivative is finite whenever neither fixed endpoint equals p.
The stated noncontact separations give the uniform bound. In the
two-contact case apply (5) once to each endpoint. Therefore

    B_(delta_epsilon)-B_(delta_0)
                       =m epsilon log(1/epsilon)+O(epsilon). (6)

This retains BOTH actual unused intervals. For a lower-half LEFT
presentation, the omitted upper-half integral is exactly zero, so
(6) agrees with the retained A_rest normalization. It is not a
claim that a sampled zero finite product has a nonzero logarithm.

## 4. Uniform control of the active tail, before taking any infimum

Write a=sin(pi t), k=cos(pi delta), s=sin(pi delta), A=x+y,
P=xy and R=sqrt((x-y)^2 a^2+4Pk^2). The ORIGINAL tail root is

    Lambda=2a(Aa+R).

For x,y>0 and 0<t<1,

    partial_delta log Lambda
      =-4pi Pks/[R(Aa+R)],
    |partial_delta log Lambda|<=pi tan(pi delta),  (7)

because R(Aa+R)>=R^2>=4Pk^2. This bound is independent of x/y,
hence holds on ALL outer tilts, including unbounded sequences of
tilts used to approach a closed coefficient degree. If P=0 the
literal monomer root has zero delta derivative and satisfies the
same bound. At t=0,1 use the integrable sine endpoint limit; a
single endpoint of integration has measure zero.

On a small fixed spectral interval around delta_0, integration of
(7) gives

    |Phi_(delta_epsilon)(l)-Phi_(delta_0)(l)|
                              <=C w epsilon                (8)

for EVERY real l, with the same C. Subtract xi l and take infima
in both directions. Since the Legendre values are finite for
0<=xi<=w, their difference is bounded by Cw epsilon. This requires
neither a finite minimizing tilt nor differentiability in xi.
Combining (6) and (8) proves (2), with its exact integer m.

## 5. Actual source and shared-maximum scope

The original finite coefficient is its unused-row scalar product
times one coefficient of the actual full-interval K_(i,j). No tail
recurrence is replaced by its absolute matrix, and no omitted-half
mode is differentiated away. The separately proved uniform upper
coefficient estimate uses positivity of the actual eta-word and
upper logarithmic Riemann sums, so sampled zeros only improve that
upper bound. Its tail estimate remains regular when a row endpoint
meets alpha=0; the unused-product estimate already allows such
zeros. Thus on otherwise regular coefficient charts, this pole
calculus does not require a new finite LOWER coefficient theorem.

For CROSS one may use the single full interval directly. There is
no need to choose a possibly singular latent half allocation; the
uniform estimate (8) survives its equivalent outer Legendre split.
For LEFT or RIGHT the same argument uses the corresponding half
interval. Closed outer degrees and an exact protected start0 or
stop1 are permitted in the calculus statement.

Consequently a genuine maximum of the sharp shared upper functional
cannot have a positive-length interval with an endpoint at a free
interior spectral pole. This does not remove diagonal intervals,
terminal row seams unrelated to a pole, spectral0 or1/2 corners,
ordinary-radius escape, phase-cocycle obstructions, or the need for
an absolute bound on inconsistent-phase contributions. It also does
not assert that arbitrary remaining KKT data are limits of coherent
regular solutions. No numerical audit is required for the elementary
integral identity and the tilt-uniform bound proved here.


## Dependencies and review scope

The [original full-interval source](research_original_one_sided_four_state_transfer.md)
and [positive eta-word](research_positive_eta_word_transfer.md) supply the
finite source normalization. The [regular coefficient upper bound](research_sharp_regular_coefficient_limsup_majorant.md)
and [shared stationary reduction](research_regular_shared_spectral_stationary_reduction.md)
state the upper-functional setting used here.

Both internal reviews checked all four inward directions, the compatible
two-contact direction, the exact logarithmic gain from the original unused
rows, the all-tilt active-root derivative estimate, and the closed-degree
shared-target scope. This analytical theorem has no numerical audit, lower
coefficient asymptotic, phase-compatibility assertion or density assertion
for boundary maximizers.
