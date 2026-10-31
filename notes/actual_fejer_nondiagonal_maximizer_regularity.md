# Non-diagonal maximizers have no free zero degrees

Independently reviewed, 31 October 2026. This uses the actual shared
entropy theorem and the labeled complete geometric all-cross flow. It
does not assume a global entropy redistribution or exchange inf and max.
It supplies ordinary finite positive Lagrange multipliers on a precise
stratum. The remaining diagonal strata are expressly excluded.

## 1. Source setting and the admissible perturbation

Use the [shared entropy theorem](actual_fejer_shared_entropy_variational.md), with the actual
two protected faces and fixed incidence map. A maximizer includes the
two triangular allocations at each cross port. First perform the
proved [batch terminal reduction](actual_fejer_batch_terminal_reduction.md): every one-sided port with nu=1/2 is
retagged cross at the SAME degree vector and entropy. Eventual
feasibility of the new pattern follows by mixing with the geometric
all-cross flow, scaling by d and rounding with strict middle slack.

Assume now that no remaining one-sided port is diagonal. Thus at each
one-sided port

    0<=mu<nu<1/2, xi>=0, eta=nu-mu-xi>=0.              (1)

The positive interval length and upper endpoint margin are fixed at
this particular finite-dimensional maximizer. No uniform margin over
all possible maximizers is being asserted.

Let qG be the actual geometric all-cross flow, with its literal
triangular allocations. Every ordinary triangular corner of qG is
positive; protected corners are zero. Every ordinary middle is strictly
less than1/2, because its two outer faces form a matching edge and cannot
both be the marked MAIN pair. Protected middle loads are zero.

For a fixed sufficiently small epsilon>0 put

    q(epsilon)=(1-epsilon)q+epsilon qG.                (2)

At cross ports mix the triangular allocations themselves. At a one-sided
port interpret its four mixed incidences by the SAME affine (mu,nu,xi)
parameterization, or its actual reflection. It is immaterial that qG
alone lies outside this one-sided domain: the strict margins in (1)
keep (2) inside it for all small epsilon. Shared ordinary targets remain
one and BOTH protected targets remain zero. The original label pattern
is unchanged. Its eventual feasibility was already proved, so (2) is a
legitimate limiting source flow in that same pattern.

This perturbation activates every zero ordinary local incidence and
every zero ordinary cross-triangle corner, while it leaves all protected
zeros exactly zero.

## 2. All corner expansions for the actual E

Write

    C(alpha)=sum_j f(alpha_j),
    f(t)=[Lambda(pi t)+Lambda(pi/2-pi t)]/pi,
    f(t)=-t log t+O(t) as t->0,
    f(1/2-t)=f(t).                                    (3)

For a cross triangle along an affine admissible path, the coefficient
of epsilon log(1/epsilon) in its entropy change is

    sum_(alpha_j=0) dot_alpha_j
                   -sum_(alpha_j=1/2) dot_alpha_j.    (4)

All these terms are nonnegative. At a vertex it is twice the sum of
the activated zero corners; on an open edge it is the activation of
its single zero corner. The remainder is O(epsilon), uniformly when
the fixed direction ranges over a compact admissible set. This follows
from t log t and boundedness of a log a for bounded nonnegative slopes.

For a one-sided port set eta=nu-mu-xi. Along an affine path satisfying
(1) for small epsilon, the coefficient h in

    E(epsilon)-E(0)=h epsilon log(1/epsilon)+O(epsilon) (5)

is as follows. Slopes of coordinates that vanish at epsilon=0 are
nonnegative.

* If mu,xi,eta are all positive, h=0.
* If mu=0 and xi,eta>0, h=dot_mu.
* If mu>0 and xi=0, h=dot_xi; if eta=0, h=dot_eta.
* If mu=xi=0, h=2(dot_mu+dot_xi).
* If mu=eta=0, h=2(dot_mu+dot_eta).

These cases exhaust (1). Here is a proof from the ACTUAL closed
coefficient entropy, including the simultaneous corner. Use its exact
formula from the [closed coefficient theorem](actual_fejer_half_block_entropy.md),

    E=C(alpha)-C(beta),
    alpha_b=mu, beta_c=nu,
    alpha_x-beta_x=xi, alpha_y-beta_y=eta,             (6)

where the input/output triangles have the common outer tilt. Their
explicit arcsine reconstruction is the one in the half-block theorem;
no independent optimization of alpha and beta is made.

In the first case all corners are strict, so E is smooth. In the second,
the tilt stays finite and the only vanishing corner is alpha_b=mu;
the arcsine formulas are smooth for the other corners. Equation (3)
therefore gives h=dot_mu.

If mu>0 and xi=0, both alpha_x and beta_x vanish, but all their other
corners stay strict. The arcsine formulas are smooth at kappa=-1
because mu,nu are strictly between0 and1/2. Both small corners are
O(epsilon), and their difference is EXACTLY xi. Their singular
coefficients subtract to dot_xi. The y-reflected case is identical.

For mu=xi=0, the input triangle is the vertex (0,0,1/2), while the
output triangle has its x corner zero and its other two corners strict.
The common outer tilt gives

    tan(pi alpha_x)/tan(pi alpha_y)
                      =tan(pi beta_x)/tan(pi beta_y).

Since alpha_y=1/2-mu-alpha_x and beta_c remains near the fixed
nu in (0,1/2), this equality and alpha_x=xi+beta_x imply

    beta_x=O(xi(mu+xi)), alpha_x=xi+O(xi(mu+xi)).       (7)

Indeed the left ratio is comparable to alpha_x(mu+alpha_x), while
the right is comparable to beta_x. After continuity makes all these
quantities small, absorb the beta_x terms. The constants are uniform
over compact direction sets at the fixed positive nu.
Thus beta_x=O(epsilon^2), alpha_x=epsilon dot_xi+O(epsilon^2),
and alpha_y=1/2-epsilon(dot_mu+dot_xi)+O(epsilon^2).
Equation (3) gives the coefficient 2(dot_mu+dot_xi) for C(alpha).
The change in C(beta) is only O(epsilon), including its
O(epsilon^2 log epsilon) zero-corner term. This proves the joint
case, even if either or both activation slopes vanish. Reflection
proves the remaining case. Every displayed O(epsilon) is for a fixed
source point, uniformly over a compact set of admissible directions.

## 3. General exclusion of free zeros at a non-diagonal maximum

Apply (4)--(5) to (2). Every entropy singular coefficient is nonnegative.
If any ordinary local degree or ordinary cross-triangle corner is zero,
the geometric witness activates it and at least one coefficient is
strictly positive. All other changes are O(epsilon). The sum therefore
increases by

    h_total epsilon log(1/epsilon)+O(epsilon)>0,
    h_total>0,

contradicting maximality. Consequently a maximizer with all terminals
removed and with no diagonal one-sided port has ONLY the zeros forced
by the two original protected faces. Every ordinary cross-triangle
corner and every ordinary incidence in a one-sided port is positive.

For cross ports it is enough to retain the particular mixed triangular
split: the optimized cross entropy at the mixed total degrees is at
least that value. Thus the proof does not assume the new split is an
optimizer, nor differentiate a maximum at a nonsmooth split.

## 4. Finite positive shared multipliers and the actual local equations

Remove the protected variables, which are fixed to zero. On the stratum
just obtained, all remaining local inequalities are strict except those
that are identities of a zero-dimensional triangle. The objective is
smooth in the resulting affine local coordinates. At a constrained
maximum its differential annihilates the kernel of the actual face-
balance matrix. Elementary finite-dimensional linear algebra gives
FINITE REAL face multipliers lambda_f satisfying

    d(sum local entropy)+sum_(ordinary f) lambda_f dq_f=0. (8)

Redundant balances cause no issue: a linear functional annihilating
the kernel belongs to the row space. No constraint independence or
unproved multiplier compactness across different maximizers is assumed.
Put l_f=exp(lambda_f)>0 for ordinary f, and retain l_u=l_v=0.
The common-scale freedom is harmless because every port has total
degree one and every protected incidence is zero.

At a cross triangle with at least two ordinary corners,
f'(alpha)=log cot(pi alpha), so (8) implies

    tan(pi alpha_f)=l_f/T,
    T^2=sum_(pairs f,g in that triangle) l_f l_g.

This is the actual center-angle formula; its one-ordinary-corner
case is the forced angle vector (0,0,1/2).

At a one-sided port with both outer variables ordinary, its outer
stationarity gives the actual tilt log(l_x/l_y). If the parent middle
is ordinary, row stationarity gives L(mu;l_x,l_y)=l_b; if it is
protected, mu=0 and the same equation holds by the endpoint limit.
The overloaded middle is ordinary, and its strict terminal equation is
L(nu;l_x,l_y)=l_c. When one outer face is protected, the corresponding
outer degree is fixed zero and the actual entropy is its extreme value
B; the same equations hold with L(t;0,y)=y tan^2(pi t), or its reflection.
Both outer faces cannot be protected, since their matching edge is not
the protected MAIN edge. These formulas also include the forced joint
corner x=b=0: the input is the two-line angle vector and the remaining
terminal equation is unchanged.

Thus these maxima supply the FINITE positive ordinary multipliers and
strict remaining equations required by the [marked signed-circle
development](actual_fejer_marked_signed_development.md). The [global
signed cut-ball regulator](actual_fejer_signed_cut_ball_regulator.md)
uses the original labeled degree-one fundamental chain, actual face
pairings, one reflection of the second ball, and the retained peripheral
horospheres. It proves that this stationary entropy is Vol(rho)/(2pi),
and therefore at most Phi_D=Vol(Y_D)/(2pi). This invokes that GLOBAL
chain proof, not the disproved invariance of a re-framed open crossing
word.

Consequently every global maximizer satisfying the no-diagonal
hypothesis after batch terminal reduction has value at most Phi_D.
If such a maximizer exists, the all-cross lower bound gives W_D=Phi_D.
Equivalently, any strict inequality W_D>Phi_D would force a diagonal
one-sided port in every maximizer with the minimal number of one-sided
labels. This is a general reduction at arbitrary fixed width under the
original labeled certificate, not an assertion that diagonals are absent.

## 5. The diagonal exception is essential

This proof excludes every mu=nu port. In particular a diagonal at
mu=nu=0 can LOSE entropy of order epsilon log(1/epsilon) under the
same mixing, and can cancel the gains above. If the mixing has parent
activation B and outer activations X,Y, then

    E(epsilon B,epsilon(B+X+Y),epsilon X)
                =2 max(X,Y) epsilon log epsilon+O(epsilon). (9)

For X>Y, the exact arcsine reconstruction has kappa=1-O(epsilon^2).
Both endpoint triangles approach the x vertex; their other-outer and
middle loads are O(epsilon). The middle loads differ by
-epsilon(X+Y), while their y loads differ by epsilon Y. The vertex
singular terms in (3) therefore subtract to
2X epsilon log epsilon. For X<Y use the reflected calculation.
For X=Y the tilt is exactly zero; the two outer corners stay near1/4
and only the middle corners are small. Their middle difference is
-2epsilon X, giving the same formula. The parent B changes only the
O(epsilon) term. The zero-width case X=Y=0 gives E=0 exactly.

No such term was concealed in (5). Diagonal ports require an actual
identity-deletion/block argument or another global entropy exchange.
The lemma does not settle those strata or the phase-sensitive filling
asymptotic.

Root and both independent analytical reviews checked every corner
coefficient, joint-corner absorption, actual geometric mixing, finite
row-space multipliers, and the forced one-/two-line equations. The
underlying exact entropy and finite coefficient checks are in the linked
half-block theorem. This finite-dimensional proof does not require a
new numerical asymptotic audit. The global signed-chain invocation was
also independently reviewed with its original pairings and marked apex.
