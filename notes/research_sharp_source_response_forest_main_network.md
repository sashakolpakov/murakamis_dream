# Exact Green responses and an original MAIN-network instability certificate

31 October 2026. **analytical research continuation**
of the constrained-Hessian reduction. No universal instability, globally realized
stable counterexample, or absolute source/volume bound is claimed.

## 1. Scope and the exact Green response

Use the actual full protected-zero transport fiber and the classified
stationary data of the [constrained-Hessian reduction](research_sharp_source_constrained_hessian.md). Each
ordinary face has demand one. Local rows have supply one and positive
load on every ordinary incidence. Complete CROSS spectra are held at
zero; strict Green spectra vary; residual cap spectra are held at 1/2.
For a constrained non-CROSS maximum retain the inherited high-value
hypothesis. Its strict overload is automatic by the [closed CROSS comparison and seam-gap theorem](research_sharp_cross_degree_domination_and_seam_gap.md).
No enlarged angle fiber is used here.

Let v denote local row-simplex coordinates, K the positive fixed-spectrum
row stiffness, and B the row/spectral derivative. The preferred local
row displacement of a Green under a unit spectral change is K_e^{-1}B_e.
Let r_e be its vector of original face-load changes.

For LEFT, write A=x+y, P=xy, z=sin^2(pi delta),
D_0=A^2-4Pz and C_0=A+2bz. At a strict critical Green,

    (c-b)z=A,  Delta=sqrt(C_0^2-D_0)>0.

The [original normalized row-optimized derivative](actual_global_left_weighted_spectral_envelope.md) is

    partial_delta F=log(T_c/E_b),
    E_b=C_0+sqrt(C_0^2-D_0),
    T_c=2cz-A+sqrt((2cz-A)^2-D_0).

Differentiate this identity in the logarithm of each actual face weight,
with delta fixed. At T_c=E_b, the common-discriminant derivatives cancel.
The gradient of F in log weights is the original row allocation, so
mixed derivatives give exactly

    r_e=(2/Delta)[zc e_c-zb e_b-x e_x-y e_y],          (1)
    W_e=(2/Delta)(c-b) pi sin(2pi delta)>0.           (2)

Here e_f denotes the coordinate of an ordinary face, and a protected
zero-weight term is absent. The derivative commutation is on the strict
smooth stationary branch; it is not a coefficient-limit argument. For
RIGHT reverse the original middle orientation and use its overloaded
face as c in (1).

The coefficients in (1) sum to zero by (c-b)z=A. Exactly one is positive,
at the overloaded child c; every supported input coefficient is negative.
Moreover L_c>L_b+L_x+L_y, so every such input has STRICTLY smaller weight
than the child. The actual response is thus a directed redistribution
from the three (or two) supported inputs toward its original overloaded
middle. No sign/phase compatibility has been assumed.

## 2. Independence survives actual cap elimination

Distinct Green ports have distinct overloaded children: two loads
strictly greater than 1/2 cannot occupy the same demand-one face. With
no caps, the response columns (1) are therefore linearly independent.
Indeed choose a nonzero coefficient in a putative relation whose child
has maximal common weight. At that child coordinate, no other selected
column can have a negative entry: such an entry would require an even
larger child. No other column has that positive child. Its coefficient
must vanish, a contradiction.

The same proof survives residual caps. Form the finite multigraph on
ordinary faces whose edges are the actual residual cap rows. A cap has
two distinct ordinary faces, equal common weights, and a load greater
than 1/2 at its child. Orient its edge toward that child. Demand one
implies indegree at most one. A Green child has cap indegree zero.

A connected cap component on n vertices has at least n-1 edges.
Since every edge contributes one to total indegree and no indegree
exceeds one, the component has at most one indegree-zero vertex.
It therefore contains at most one Green child. This argument allows
parallel edges and does not assume the component is a tree. A cyclic
component has no Green child.

Let U sum the original face loads in each cap component (isolated faces
are components). The span of actual cap row displacements is exactly
ker U. Hence U is an exact set of quotient face constraints after the
zero-action cap degrees are eliminated. All weights in a component
are equal. The column U r_e has one positive child component, distinct
for different Green ports, and negative entries only at strictly lower
weight components. The same maximal-child argument proves

    the columns of R_bar=(U r_e)_e are independent.    (3)

This agrees with the orthogonal projection P onto ker(T_cap^T) used in
the earlier note: U and P encode the same quotient, and their response
columns have the same kernel. Consequently no nonzero spectral
combination can cancel its entire preferred-load defect for free, even
after actual cap displacements. This is an injectivity obstruction to
one proposed whole-circuit shortcut, NOT a sign theorem for
S=W-R^T C^dagger R. A positive repair cost may still be smaller than W.

## 3. Build the repair network from actual supported MAIN edges

For a noncap spectator port p and a MAIN edge fg in one of its two
original triangles, suppose f,g are ordinary. Let v_{p,fg} be the unique
local row-coordinate vector whose original incidence displacement is
+1 at f, -1 at g and zero at its other incidences. Define

    kappa_{p,fg}=v_{p,fg}^T K_p v_{p,fg}>0.          (4)

This is an actual admissible infinitesimal row displacement; positive
ordinary loads permit both signs for sufficiently small magnitude.
It is evaluated with that spectator's spectrum fixed. There is no
independent face torus and no change in the protected targets.

Choose nonnegative numbers tau_{p,fg} with

    sum_(selected MAIN edges fg at p) tau_{p,fg}<=1. (5)

If the same port is encountered on several boundary edges, it is still
counted only once in (5). Put d_{fg}=U(e_f-e_g), and form the ordinary
quotient-graph Laplacian

    L_net=sum_(p,fg) [tau_{p,fg}/kappa_{p,fg}]
                                      d_{fg} d_{fg}^T. (6)

Edges collapsed by actual caps have d_{fg}=0 and need not be included.
In terms of the original face map A_p on port p, the elementary
rank-one Cauchy inequality is

    U A_p K_p^{-1} A_p^T U^T
           >= d_{fg}d_{fg}^T/kappa_{p,fg}.

Taking the convex combination (5), then summing ports, gives

    C>=L_net,                                      (7)

where C is the exact face compliance in these quotient coordinates.
This is why one cannot simply add every edge's full conductance when
several of them use the same coupon.

The support of each Green r_e is connected by a network of this kind
using only OTHER ports. The four original MAIN boundary edges of its
quartet form a cycle. A strict Green has at most one protected incident
face: an overloaded protected face vanishes, two protected outers are
forbidden by the actual mark, and the remaining double-protected input
case is excluded by the [stationary classification](research_full_fiber_sharp_stationary_classification.md). Deleting its possible
protected vertex leaves a connected three-vertex MAIN path; with no
protected vertex the original cycle remains. Each of these MAIN edges
has its other incident triangle at a port different from e. The
spectator ports need NOT be pairwise distinct across those edges.
If the other port is a cap, that edge is already collapsed at zero cost.
Otherwise (4) provides a finite positive conductance. Assign, for
example, equal total weight one among the finitely many selected edges
at each spectator. The resulting path/cycle connects the supported
quotient faces of r_e.

It follows that U r_e belongs to range(L_net). The same holds for any
linear combination of columns if the chosen network contains such a
path/cycle for every selected Green. Thus the network energies below
are finite and concern the original target defect, not a guessed
unconstrained electrical matrix.

## 4. A concrete general instability certificate

For r in range(L_net), the variational formula for resistance and (7)
give

    r^T C^dagger r <= r^T L_net^dagger r.            (8)

Indeed each side is the supremum over quotient face potentials p of
2p^T r-p^T C p, or respectively 2p^T r-p^T L_net p. Redundant total-load
constraints cause no problem because r is in the indicated range.

Consequently, if there is a spectral vector s such that

    (R_bar s)^T L_net^dagger (R_bar s)
                                      < sum_e W_e s_e^2, (9)

then the ACTUAL constrained Hessian has a positive direction and the
stationary datum is not a maximum. Equivalently it suffices that

    W-R_bar^T L_net^dagger R_bar

have a positive eigenvalue. All coefficients of this sufficient test
are explicit local derivatives, shared weights and original MAIN
incidences; its proof is independent of the diagram's width.

There is a useful one-port version: build the network from spectators
of one chosen Green and test its r_e against W_e. Holding that Green
at its preferred row response and repairing only through these
spectators is an actual feasible variation. If its repair energy is
less than W_e, the variation has positive second derivative. The full
network version may be stronger because it permits distributed repair
and a simultaneous choice of several spectral directions.

What remains OPEN is whether common-weight dominance and the exact
unit face demands ALWAYS force (9), or the corresponding sharper test
with C, at a high-value non-CROSS stationary configuration. The response
independence (3) specifically prevents proving this by setting the
preferred defect equal to zero. The earlier forced MAIN-cycle example
specifically prevents proving it by assigning a positive curvature to
each elementary odd cycle. No globally feasible stable stationary
counterexample has been obtained here.

## 5. The maximal child component

Use the classified common-weight stationary data and exact cap quotient
of sections 1--2 above. Let a
Green port e have maximal overloaded-child weight among ALL Green ports.
Let S be the connected cap component containing its child c; an isolated
ordinary face is permitted. All weights on S agree.

Every other noncap port incident to S is CROSS. Indeed another Green
cannot have its child in S, by the already proved at-most-one-child
count. If one of its inputs were in S, its child would have strictly
larger common weight, contradicting the choice of e. The chosen Green
itself has no input in S, because each input weight is strictly smaller
than its child weight.

The component S is automatically a tree; no assertion about other cap
components is needed. Orient each cap edge toward its greater-than-one-
half load. Every vertex has indegree at most one, while c has indegree
zero because its Green load already exceeds one half. If S has n
vertices and m cap edges, then m<=n-1. Connectedness gives m>=n-1.
Thus m=n-1, including the isolated-vertex case. Parallel edges have not
been discarded; a component containing such a cycle cannot contain c.

Its ordinary demands total n. Its n-1 internal cap rows each supply
one unit entirely to S. The remaining noncap supply into S is therefore
exactly one. Consequently

    sum of all CROSS incidence loads in S = 1-q_(e,c) < 1/2.       (10)

This is an exact original-target identity, not a collapsed-source
interpretation.

## 6. Exact triangle compliance

A complete triangle has loads alpha_i>=0, sum alpha_i=1/2, and entropy
C_tri=sum_i f(alpha_i), where -f''(a)=2pi/sin(2pi a). For positive
weights w_i its unique weighted stationary loads are

    alpha_i = (1/pi) atan(w_i/T),
    T=sqrt(w_1 w_2+w_1 w_3+w_2 w_3).                            (11)

Let s_i=sin(2pi alpha_i). Differentiating its constrained Legendre
problem, or inverting the diagonal stiffness on sum d alpha_i=0,
gives the exact Hessian in logarithmic weights:

    C_tri = (1/(2pi)) [diag(s)-s s^T/(sum_i s_i)].               (12)

Thus it is the three-vertex graph Laplacian with conductances

    g_ij = s_i s_j/[2pi sum_r s_r]
         = w_i w_j/[2pi(w_i+w_j)T].                           (13)

For the second equality use

    s_i=2w_i T/[(w_i+w_j)(w_i+w_k)],
    sum_i s_i=4T^3/[(w_1+w_2)(w_1+w_3)(w_2+w_3)].

One protected-zero weight is the literal limit of (12)--(13). A half
with only one positive weight has fixed load 1/2 and zero compliance;
the indeterminate all-zero expression in (12) is not used for that half.
A complete CROSS port contributes the sum of its two actual triangle
matrices, pushed to its four original incidence coordinates. Shared
outer coordinates are added, not treated as independent faces.

For any subset I of a triangle's faces, its component-charge diagonal
is

    1_I^T C_tri 1_I
      = (1/(2pi)) [s_I-s_I^2/(sum_i s_i)]
      <= sum_(i in I) s_i/(2pi)
      <= sum_(i in I) alpha_i.                                (14)

This includes I empty or the whole triangle and all permitted protected
limits. The last inequality is sin(2pi a)<=2pi a on [0,1/2].

Let C_sp be the exact face compliance from all noncap spectator ports,
written in the component-sum coordinates U of section 2. At S
all such incidences are CROSS. Equations (10) and (14) give

    (C_sp)_(S,S) <= 1-q_(e,c) < 1/2.                          (15)

Other spectators may be Green away from S; they contribute zero to
this diagonal because they have no incidence in S.

## 7. The resulting lower bound on spectator repair cost

Hold e at its preferred row response r_e under a unit spectral change,
and repair the original face targets only through spectators and the
zero-cost cap rows. Write r_bar=U r_e. If repair is possible, the exact
minimum cost is r_bar^T C_sp^dagger r_bar. Its dual variational formula,
restricted to potentials supported at S, gives

    r_bar^T C_sp^dagger r_bar
        >= r_bar_S^2/(C_sp)_(S,S)
        >= r_(e,c)^2/[1-q_(e,c)].                              (16)

If the relevant diagonal vanishes while r_bar_S is nonzero, repair is
impossible; this strengthens, rather than reverses, the obstruction.
The exact response has

    r_(e,c)=2 z c/Delta,
    W_e=2(c-b)pi sin(2pi delta)/Delta,
    z=sin^2(pi delta),
    Delta=sqrt((x+y+2bz)^2-[(x+y)^2-4xyz]).

At the protected-outer local datum

    (mu,nu,delta)=(1/6,1/3,1/4), (x,b,c,y)=(1,1,3,0),

these are q_(e,c)=2/3, r_(e,c)=sqrt(3), W_e=4pi/sqrt(3).
If this datum occurs with the maximal-child hypotheses above, every
spectator-only repair therefore costs at least

    3/(1/3)=9 > 4pi/sqrt(3)=W_e.                              (17)

The strict inequality is elementary, for example from pi<22/7.
Thus the one-port preferred-response/spectator-network criterion cannot
prove instability for ANY embedding satisfying those local and
maximal-child assumptions. No such global embedding is asserted here.
The full Schur complement also allows e's own row response to change,
and may combine several spectral directions. Equations (15)--(17) give
no sign theorem for that full matrix.

## 8. What comparison with the geometric weights does establish

Let L^G be the complete marked geometric weights and let ordinary
rho_f=L_f/L_f^G. At a face f maximizing rho, every incident COMPLETE
triangle contributes at least its geometric load at f. This follows
directly from (11): every neighbor ratio w_j/w_f is no larger than its
geometric counterpart, so T/w_f is no larger. Equality is possible
only when all supported neighboring ratios agree (apart from a fixed
one-positive-weight monomial half).

This is a valid triangle maximum principle. It is not yet a maximum
principle for the full Green/CROSS source. A Green input can have a
strict load deficit compared with its complete triangle allocation;
for instance the datum in section 7 has input-middle load 1/6 while
the complete same-weight load is 1/4. Its strictly larger child weight
does not imply a larger ratio rho_c: the geometric denominator L_c^G
is different. The present argument therefore does not propagate a
ratio maximum from a deficient Green input to a still larger ratio.
Any such propagation or full-Hessian inequality needs an additional
global identity, not just the absolute child-weight ordering.

No numerical search or source asymptotic claim enters this addendum.

## Internal validation and remaining scope

The network gives a conditional spectator-repair test. No universal inequality for the full constrained Hessian follows from it.

The original MAIN/MATCHING incidence used here is that of the
[certified augmented plat dictionary](general_augmented_plat_matching_geometry.md).
The [odd MAIN-cycle theorem](research_stationary_noncross_main_cycle_obstruction.md)
remains a qualitative phase obstruction; it is not substituted for (9).
The universal resistance comparison and any global stable counterexample
remain open.
