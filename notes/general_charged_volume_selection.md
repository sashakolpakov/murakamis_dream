# What capacity can and cannot select in the actual charged source

28 October 2026. The exact original charged coefficient is a useful
place to ask for a general lower bound. Three commonly proposed
shortcuts do not supply one: ordinary half-plane stability, Lorentzian
positivity after taking magnitudes, and a subexponential comparison
with positive capacity. The last failure occurs in an actual nonzero
source sector, uniformly in the level, after its already proved
parallel-edge fusion. This is an obstruction to these particular
methods, not to a further phase-aware fusion or to the volume conjecture.

The source throughout is the specified functional in
[the global charged-flow theorem](actual_global_charged_bridge_flow.md),
with its [Fermat/nilpotent residue](actual_charged_socle_and_fermat_source.md).
No scalar multiple of the invariant or replacement boundary functional
is introduced.

## 1. The raw root blocks are not half-plane stable

Let q=exp(pi*i/N), Q=q^2, d=N-1. A genuine two-anchor block is

    B_L(X,Y)=product_(j=0)^(L-1)(alpha X-Q^j beta Y),
    alpha beta !=0, 2<=L<=d.                         (1)

A homogeneous linear polynomial aX+bY, with ab nonzero, has no zero
with Im X>0 and Im Y>0 if and only if b/a is positive real. Indeed a
zero requires X=-(b/a)Y; two open half-planes through zero intersect
unless the multiplier maps the upper half-plane exactly to the lower
one. A product is stable only when every nonconstant factor is stable.

After ANY nonzero diagonal changes X=cX', Y=eY', successive factor
ratios in (1) still differ by Q. Since N>=3 here, Q is not positive
real. Thus no such change makes (1), or a polynomial containing it,
upper-half-plane stable. This also covers arbitrary complex diagonal
changes, not just vertex phase gauges. Self-loop factors which have
already become scalars or monomials are excluded from this statement.

This does not rule out a different stable object obtained by an exact
fusion. It prevents applying stable-polynomial coefficient inequalities
directly to the original charged product.

## 2. Even the positive sine block is not Lorentzian

The exact grouped expansion has positive magnitudes

    C_(L,k)=|[L choose k]_Q|
           =product_(j=1)^k sin(pi*(L-k+j)/N)/sin(pi*j/N).

Put a_k=C_(L,k)/binom(L,k). Its successive ratios are

    a_k/a_(k-1)
      =sinc((L-k+1)*pi/N)/sinc(k*pi/N),              (2)
    sinc(t)=sin(t)/t.

On (0,pi), sinc is strictly decreasing: its derivative has numerator
t cos t-sin t, whose derivative is -t sin t<0. As k increases in
(2), the numerator increases and the denominator decreases. Hence
a_k is strictly log-CONVEX at every interior index when L>=2.

For a binary homogeneous polynomial with positive coefficients,
the Lorentzian coefficient condition is log-concavity after division
by binom(L,k). Thus the positive-sine block fails this condition.
Already L=2 gives X^2+2 cos(pi/N)XY+Y^2: a nonpositive Hessian
determinant would require the middle coefficient to be at least 2;
here the determinant is positive. Ordinary positive coefficients have
not restored the needed real-rooted or Lorentzian structure.

## 3. Logarithmic torus capacity forgets these root phases entirely

For an actual product P_h of unit-modulus binary linear factors
on DISTINCT anchor pairs, its Ronkin average is

    R_h(rho)=average_theta log|P_h(exp(rho+i theta))|
             =sum_factors max(rho_tail,rho_head).    (3)

To prove (3), integrate the relative angle of one linear factor.
The mean of log|A-Be^(it)| is log max(|A|,|B|); for unequal moduli
this follows by expanding log(1-z), and the equal-modulus value
follows by an integrable limit. Linearity of the average then gives
(3), irrespective of dependencies between the factor angles.

If the charge d at every anchor is feasible, choose an endpoint for
each factor giving that total charge. Each maximum in (3) dominates
the chosen endpoint, so

    R_h(rho)-d sum_a rho_a >=0.

At rho=0 equality holds. Consequently the logarithmic capacity

    exp inf_rho [R_h(rho)-d sum_a rho_a]

is EXACTLY ONE in every feasible sector of this type. If self-loop
factors occur, first evaluate them as an explicit scalar times a
monomial. The same assertion holds after division by that scalar
and subtraction of the monomial's charges; the scalar itself may
carry an exponential action and is not omitted from the period.
Nonzero selected coefficients in particular have feasible charge.
This average is therefore not
the exponential volume scale of the original source. It should not
be confused with the supremum-over-angles Cauchy bound, or with a
capacity which retains further phase information.

## 4. Positive capacity can exceed a surviving actual period exponentially

Use the already proved uniform original-source family in
[the anchor-phase and exact-fusion theorem](anchor_phase_cycles_and_exact_fusion.md):

    word=[1,-2,1,1,-2,-2], N=2r+1,
    h=(0,r,r,r,0,r).

Its selected coefficient, INCLUDING every original closure block, is

    c_N=[X_0^d ... X_8^d]P_h=N q^(2-r^2).           (4)

The same theorem fuses its two parallel r-blocks into the complete
d-block with every coefficient equal to one. Work AFTER this exact
fusion. In the remaining flow description choose

    a=c=f=0, b=floor(r/2).

These are feasible original source charges. The only nontrivial
magnitude in this term is

    M_N=|[r choose floor(r/2)]_Q|.                   (5)

Let P_h^+ mean the polynomial obtained from these fused grouped
blocks by replacing their coefficient phases by one. It has positive
coefficients. Its positive capacity is

    Cap_d(P_h^+)=inf_(x_a>0) P_h^+(x)/product_a x_a^d.

The feasible term (5) contributes M_N product x_a^d. All other
terms are nonnegative. Therefore, on EVERY radius,

    Cap_d(P_h^+) >= M_N.                            (6)

Put J(t)=integral_0^t log(2 sin(pi*s))ds. Elementary endpoint
splitting, followed by Riemann summation, gives uniformly for
0<=j<N

    log |(Q;Q)_j|=N J(j/N)+O(log N).

Here r/N tends to 1/2 and b/N,(r-b)/N tend to 1/4. Since
J(1/2)=0 and J(1/4)=-G/(2*pi), where G is Catalan's constant,

    log M_N=(G/pi)N+O(log N).                       (7)

Combining (4)--(7) proves the genuine actual-source gap

    limsup_(odd N) (1/N)log[|c_N|/Cap_d(P_h^+)]
                                      <=-G/pi<0.   (8)

This family is a nonzero sector of a reduced alternating hyperbolic
knot. Its phase curvature and feasibility were proved uniformly,
not inferred from an isolated numerical level. For this length-one
bridge diagram, all the original W_h factors have unit modulus, so
an omitted clock normalizer is not causing (8).

Equation (8) rules out a universal subexponential lower comparison
between a surviving charged source coefficient and its positive
capacity. It does NOT say this particular sector is a leading volume
sector: its coefficient is polynomial in N, and its exponential loss
is already explained by exact root correlations. It also does not
exclude phase-aware capacities after further exact fusions. In
particular the new source-exact full-length reproducing contractions
and balanced star--triangle moves can change the positive majorant
drastically. Equation (8) is not asserted to survive arbitrary such
reorganizations.

## 5. The remaining possibility is genuinely phase-aware

The finite-flat perfect pairing fixes the source functional; it does
not force that functional to be large on a specified state. The
calculation above gives a quantitative instance using the actual
state and the actual source. A useful general theorem would have to
retain the root-phase correlations, for example through exact local
fusions followed by a source-compatible geometric contour. Taking
magnitudes and invoking stability cannot replace that step.

The new [defect-jet theorem](charged_star_triangle_defect_jets.md)
makes this connection precise: on the unit-radius original anchor
torus the source phase frequency is exactly (S_a-2d)/2, where S_a
is incident factor degree. Balanced fusion removes a zero-frequency
direction, while its bounded-defect extension retains a finite Fourier
correction with polynomial cost. Macroscopic defects and the final
global coefficient are still present. The audit here independently
checks this phase identity on the actual unfused source graphs.

Ordinary dominant-saddle Stokes persistence is consistent with this:
in a proper deformation with a strictly highest-action saddle, its
top action-graded coefficient is preserved against jumps involving
only lower saddles. To use this observation here one still needs a
NONZERO original-source coefficient in one chamber and control of
singular/boundary competitors throughout the deformation. The
positive constrained-lens reference chain supplies neither original
cycle comparison by itself. Representation-volume rigidity at complete
boundary-parabolic critical points also does not control an entire
parameter path or its nonstationary boundaries.

No general geometric lower bound or new knot class follows from this
audit. Its constructive consequence is a restriction on methods:
the exact phase-aware graph fusions address information which each
of the three phase-blind shortcuts above loses.

[Audit](../experiments/audit_general_charged_volume_selection.py):
actual family metadata/source charges, exact small-level coefficients,
the feasible positive term on arbitrary radii, the sine normalization
inequalities, and the asymptotic rate in (7).
