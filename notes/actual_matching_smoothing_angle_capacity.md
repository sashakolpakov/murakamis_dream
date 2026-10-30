# A finite angle-flow certificate for matching-edge smoothing

30 October 2026. Independently reviewed. This note gives a
sufficient, source-compatible strict capacity comparison after replacing
ONE untwisted crossing-circle operator by L_1=I. It is not a theorem
that every proper small-color subset has an exponential gap. In
particular the finite test below has not been proved to follow from
the labeled right-angled certificate for every matching edge.

## 1. Literal smoothing and the capacity being compared

Start with the connected original marked source and labeled geometric
certificate of the [complete-source theorem](general_signed_augmented_source_volume.md).
Let one matching edge have its two actual ordered triangles

    (x,b,y), (x,c,y).

Replacing its untwisted operator by L_1=I deletes these two triangles
and identifies the two middle faces b,c. This is the literal identity
on the two physical strands, with their original order. It is not an
evaluation of the old source at unrelated b,c. Require for this lemma:

* the resulting projection is connected;
* the original two marked faces remain distinct;
* b,c,x are distinct unmarked faces, and y is distinct from them
  (y may be a marked face);
* all remaining incidences are the actual ones after this smoothing.

No positive polyhedron for the smoothed graph is assumed. The
[exact marked face coefficient](actual_original_marked_face_coefficient.md)
still defines its complete source, including repeated incidences or
bigons. A disconnected source, a merged pair of marked faces, and a
retained half twist at the deleted port require separate treatment.
They are not discarded or renormalized here.

Write F(l_0,l_1,l_2) for the exact maximal-fold determinant rate from
[the absolute source normalization](actual_original_boundary_stationary_character.md),
section 6. It has logarithmic homogeneity one half. Set the two marked
face variables to zero, and use one positive variable for every other
face, with one common scale fixed. The smoothed capacity is

    Phi_sm = inf_l [sum_(remaining triangles t) F(l_t)
                                      -sum_(smoothed finite faces f) log l_f]. (1)

Assume this infimum is attained at finite positive shared radii l.
In particular the split labels b,c both have the SAME radius z>0.
This is an explicit regularity hypothesis on the smoothed capacity;
it is not supplied by the old circle packing. Let Phi_old denote the
original packing evaluation, already proved to equal
Vol(Y_original)/(2pi).

## 2. Angle duality with its absolute normalization

For theta_j>=0 and sum_j theta_j=pi, put

    V(theta)=2 sum_j [Lambda(theta_j/2)
                              +Lambda((pi-theta_j)/2)],
    Lambda(t)=-integral_0^t log|2sin u| du.

The source-normalized local identity is

    2pi F(l)=max_theta [sum_j theta_j log l_j+V(theta)].          (2)

A zero l_j forces theta_j=0; its product theta_j log l_j is then
interpreted by continuity. To prove (2), differentiate V on the open
angle simplex:

    partial_j V=-log tan(theta_j/2),
    Hess V=diag(-1/sin theta_j).

Thus the objective is strictly concave, and its critical point is
exactly the source angle formula

    theta_j=2atan(l_j/sqrt(l_0 l_1+l_1 l_2+l_2 l_0)).

The absolute constant is zero by F(l,0,0)=(1/2)log l and
V(pi,0,0)=0. Continuity gives the one- and two-positive-face cases.

Apply (2) at the positive minimizer in (1). The radius stationarity
conditions say that the corners at every smoothed finite face have
sum 2pi. Hence its actual local angles theta maximize total V subject
to these face sums and the triangle sums pi, and

    sum_t V(theta_t)=2pi Phi_sm.                              (3)

This also proves the required dual equality without an external
duality theorem: (2) bounds any feasible total entropy above by the
right side of (3), and the displayed local angles attain it.

Split the merged face's corners into their OLD b-side and c-side sets.
Write their sums as pi+Delta and pi-Delta, respectively. This split is
part of the original incidence, not an arbitrary partition. The single
merged-face constraint gives their sum, not their individual values.

## 3. A finite source-incidence feasibility test

A corner transfer moves angle between two allowed corners of ONE
remaining triangle. It preserves its triangle sum. Fixed zero corners
and fixed pi corners are excluded. The graph of allowed face transfers
joins two face labels when their allowed corners occur in one such
triangle, retaining the original incidences.

The possible face-divergence vectors are exactly those having zero sum
on each connected component of this graph. One direction follows by
summing the triangle transfers. For the other, route the required
balances along a spanning forest. The path construction uses only
actual remaining triangles; it is not a new quantum routing of a cut.

There is also an exact finite test with prescribed corner slack.
Give each allowed corner a lower bound e_tf>=0. For proposed face
demands d_f, put

    r_t=pi-(fixed row sum)-sum_f e_tf,
    q_f=d_f-(fixed column sum)-sum_t e_tf.

Nonnegative angles with these lower bounds, triangle sums and face
demands exist if and only if r_t,q_f>=0, their total sums agree, and
for EVERY subset S of the split face labels,

    sum_(f in S) q_f <= sum_(t incident to S) r_t.               (4)

Here fixed corner values are first subtracted from both their row and
column demands. A triangle with repeated labels is still one row.
To prove (4), use a finite network with capacities r_t from the source
to triangle nodes, unlimited edges to their allowed face nodes, and
capacities q_f from the face nodes to the sink. A finite cut is precisely
one of (4), after minimizing over its triangle nodes. Augmenting along
residual paths until none remains proves the converse and constructs
the angles. Real capacities follow by the usual limiting argument from
rational capacities on this finite network.

In particular d_b=d_c=pi and d_f=2pi elsewhere tests a balanced
DEGENERATE insertion. It is stronger than the merged 2pi condition.
Feasibility alone gives no volume inequality: redistribution can lose
entropy. The following test includes that loss.

## 4. Quantitative strict comparison

Suppose every allowed movable corner of theta lies in
[sigma,pi-sigma], sigma>0. Choose two actual corner directions D_bc,D_x
with zero sum in each remaining triangle and face divergences

    div D_bc = e_c-e_b,
    div D_x  = e_b+e_c-2e_x.                                (5)

They are zero at the excluded corners. Such directions exist, for
example, whenever b,c,x belong to the same allowed transfer component;
they can be constructed by the preceding spanning-forest rule.
Their finite norms, not just their existence, enter the test.

Choose 0<eta<pi and set v=Delta D_bc+eta D_x. Require

    ||v||_infinity <= sigma/2,
    G := 2V(eta,pi-eta,0)+2eta log(l_x/z)
                          -||v||_2^2/[2sin(sigma/2)] > 0.     (6)

Then the exact capacity comparison is

    Phi_sm <= Phi_old-G/(2pi) < Phi_old.                      (7)

Proof. The adjusted old angles theta+v have sums pi+eta at b,c,
2pi-2eta at x, and the required unchanged sums elsewhere. Insert
the deleted triangles with angles (eta,pi-eta,0) in their literal
orders (x,b,y),(x,c,y). This is a feasible angle assignment for the
ORIGINAL source. The new triangles are permitted boundary points;
no positive geometric realization of this assignment is presumed.

At the smoothed maximizer the entropy gradient at a movable corner is
-log l_f plus a constant depending only on its triangle. The two old
middle-face multipliers agree. The first variation on v is therefore
EXACTLY 2eta log(l_x/z): the Delta term cancels. Taylor's integral
remainder and the first inequality in (6) give

    sum_t[V(theta_t+v_t)-V(theta_t)]
          >=2eta log(l_x/z)-||v||_2^2/[2sin(sigma/2)].          (8)

Add the two new entropies. Formula (2), evaluated at the ORIGINAL
packing radii, bounds the entropy of every feasible original angle
assignment by 2pi Phi_old. Equations (3), (6), (8) imply (7).
This comparison retains the shared variables and the actual target
face sums throughout.

The test is not confined to zero imbalance. Indeed

    2V(eta,pi-eta,0)=4eta log(1/eta)+O(eta).

At Delta=0 the left positive term dominates the linear and quadratic
costs for sufficiently small eta. Once a strict test succeeds, it
continues to succeed under small changes of its regular input data.
This is an openness statement about the explicit finite data subject
to the hypotheses; it does not assert an open family of knot diagrams,
or that every certified diagram satisfies the test.

## 5. Consequence and remaining source requirement

The zero patterns created by smoothing need an explicit extension of the
old local upper bound. At fixed nonnegative shared radii set A=x+y
and retain the exact circle B_(N,a)=beta_a^2 D_a(x,b,y)D_a(x,c,y)P_s(x,y).
There are precisely the following cases.

* If A>0, the determinant-rate proof remains valid for every b,c>=0.
  A single positive matrix summand uses the exact LDL product, already
  treated separately in that proof. Its circle derivative is
  log(E_b E_c/D_xy)>=0, since E_b,E_c>=A and D_xy<=A^2.
  Thus the fold is still an upper bound, though strictness may be lost.
  The newly possible case b=c=0, xy=0 has EXACTLY B_(N,a)=A^d
  for every label: beta_a D_a=A^a and P_s=A^s.
* If A=0 and b,c>0, P_s(0,0)=0 unless s=0. Even N therefore gives
  zero for every channel. At odd N only a=d/2 survives, beta_a=1,
  and B_(N,a)=(bc)^(d/2). Its rate is (1/2)log(bc), exactly the
  sum of the two fold rates F(0,b,0)+F(0,c,0).
* If A=0 and b=0 or c=0, every channel contribution is zero.

These statements include empty determinants at a=0; when A=0 the
positive-degree forced factor still kills that channel. They do not
apply the old strict geometric zero-pattern theorem to a new bigon.

For a literal untwisted L_1 deletion satisfying the certificate,
evaluate the EXACT smoothed positive face coefficients at the shared
minimizer l in (1). The preceding cases bound every remaining local
circle, including its beta factor, by its fold rate. There are only
polynomially many channel choices, and the multiplicities, measure and
mark have polynomial cost. Hence the whole smoothed complete source
has upper rate at most Phi_sm and the strict gap (7). An identically
zero local case is already stronger. Half-twist phases on retained
ports may be bounded in modulus for this upper bound; they are not
removed from the finite identity.

This does not yet prove the proper-small-subset estimate needed for
external colors N-h. A genuine L_h insertion has actual tridiagonal
paths of displacement at most h-1. With the original outgoing/incoming
first-head convention, displacement p imposes c=Q^p b, and its clock
monomials shift face targets. At marked zero faces they can be Laurent;
one must extract the shifted coefficient before setting those faces to
zero. Their unwrapped intervals and possible Fourier aliases must still
be controlled. A signed removed port also retains its actual braid.
Neither those finite-source requirements nor arbitrary degenerate or
JSJ smoothing limits follow from (7).

Focused audit: [finite flow and source checks](../experiments/audit_actual_matching_smoothing_angle_capacity.py),
with [saved results](../experiments/actual_matching_smoothing_angle_capacity_results.json).
It checks 79 literal Morse box-deletion/face-identification maps;
74 exact rational Hall systems against an independent linear program
(175,680 cut inequalities, including 26 infeasible systems); seven
finite entropy-flow comparisons, four with nonzero imbalance; and
270 original degenerate channel factors through both parities.
The entropy examples use stated combinatorial bipyramid/split incidences,
not newly asserted labeled right-angled knot certificates. They audit
the sufficient inequality, not its universal applicability.


Independent full analytical review and fresh redirected audit: PASS.
The reviewer checked the literal smoothing target, finite Hall criterion,
split-side divergences, entropy normalization and Taylor bound, and every
new A=0/A>0 local zero-pattern case. All reported audit counts were
reproduced at 75-digit source precision. The attained shared-capacity and
explicit finite-flow inequality hypotheses remain essential; no universal
contraction or h>1 source estimate was inferred.

Primary full analytical proof/code review and fresh redirected audit:
PASS. The review independently checked the exact face balance, sign of
the stationary linear term, Hessian bound, small-eta entropy gain and
all degenerate source factors, with the same scoped conclusions.
