# Maximal volume fixes the actual marked endpoint configuration

31 October 2026. Internally reviewed general concentration theorem. This strengthens
the already proved positive endpoint rate. It does not identify a
phase-sensitive filling cycle, a genuine-q normal, or a Gaussian contour.
All group conjugacies below are in PSL2(C); central SL2 lift signs are not
inferred from volume.

## 1. Equality in the natural-map bound gives actual conjugacy

Let Gamma be the marked complete finite-volume hyperbolic exterior group,
with its original inclusion iota into PSL2(C). Let rho be ONE fixed
representation with Vol(rho)=Vol(Gamma\H3)>0, in the normalization of
[the representation-volume proof](general_representation_volume_kernel_strictness.md). Its proved section3
constructs orientation-preserving target isometries g_j and natural maps
F_j such that

    G_j=g_j F_j -> J locally in C1 on H3,                  (1)

where J is a global orientation-preserving hyperbolic isometry. This
convergence is obtained on every compact subset with the SAME g_j.
The equivariance is exact:

    rho_j(gamma)G_j(x)=G_j(iota(gamma)x),
    rho_j(gamma)=g_j rho(gamma)g_j^(-1).                  (2)

For each fixed gamma the right and left input points converge. In
particular rho_j(gamma) sends one point converging to J(x) into a bounded
set, so these isometries are precompact: the stabilizer of a point of
H3 is compact. A limiting isometry sends J(x) to J(iota(gamma)x) for
every x, by (1)--(2). Hence it is uniquely J iota(gamma) J^(-1), and

    rho_j(gamma) -> J iota(gamma) J^(-1)                 (3)

for every gamma. Equivalently one may first use four noncoplanar points
and a finite generating set. This is exactly the equivariance upgrade
in the proved peripheral-gap note; it uses no compactness of g_j yet.

We now prove that for this FIXED rho the g_j themselves have a bounded
subsequence. Suppose instead that a subsequence escapes every compact
subset of PSL2(C). Choose its elementary singular-value decomposition

    g_j=k_j diag(exp(t_j/2),exp(-t_j/2)) l_j,
    k_j,l_j in PSU(2), t_j -> infinity.

Pass to convergent k_j,l_j, with limits k,l. For each fixed gamma the
matrix entries of rho_j(gamma) stay bounded by (3), in either SL2 lift.
The upper-right entry of the middle conjugated matrix is

    exp(t_j) [l_j rho(gamma) l_j^(-1)]_12.

It follows that [l rho(gamma) l^(-1)]_12=0 for every generator and hence
for every gamma. Thus rho has a common fixed point p on CP1. Each rho_j
then has the common fixed point p_j=g_j p. Compactness of CP1 gives a
further subsequence p_j->p_infinity. Passing to the action in (3) shows
that the complete holonomy J iota J^(-1) fixes p_infinity, a contradiction.

Here non-elementarity of the complete exterior is elementary in this
setting, not an imported volume-rigidity theorem. For the actual
certified exterior, the noncentral based cusp words at distinct vertices
of one convex white face already have distinct fixed points. More
generally, if a complete cusped finite-volume lattice fixed one point,
normalize it to infinity and take a precisely invariant embedded cusp
horoball. All its translates are concentric and intersect, so every
group element stabilizes the horoball and its horospheres. The positive
finite-area Euclidean cusp quotient then extends through all heights;
its hyperbolic volume below the horoball is infinite. This contradicts
finite volume.

Therefore g_j has a convergent subsequence g. Equation (3) yields

    g rho(gamma) g^(-1)=J iota(gamma) J^(-1) for all gamma.
                                                               (4)

In particular rho ITSELF, not just a limit of its characters, is conjugate
to the actual marked complete holonomy. This proof does not deduce
conjugacy merely from faithfulness and does not assume a closed orbit
from outside results.

## 2. Every endpoint maximizer has the original labeled white circles

Use the original fixed certified flat plat D and the full compact
incidence-flow entropy

    H_D(q)=sum_e h(q_e), q in Q_D,
    W_D=max H_D=Phi_D=Vol(Y_D)/(2pi).                   (5)

The last equality and all boundary reductions are the reviewed
[full endpoint theorem](general_fejer_endpoint_source_volume.md). Let q be ANY maximizer, choosing maximizing triangle
allocations at CROSS ports.

No port of q is pure-middle. Otherwise the exact identity reduction and
hybrid-piece representation construct a representation of the ORIGINAL
pi_1(Y_D) with volume 2pi H_D(q)=Vol(Y_D), killing an essential original
crossing-circle meridian. The strict-kernel theorem forbids this. Thus
there is no identity contraction at a maximum.

Consequently the source white triangulation is still the ORIGINAL
simplicial sphere. Its induced graphs have no parallel-edge digons, so
the hybrid tight-set classification gives no proper tight set. The
positive hybrid witness and the proved corner expansions then give
finite positive ordinary multipliers and only the two original marked
zero curvatures. Terminal seams may be tagged CROSS, without changing
q or entropy. The resulting signed circle development and original
cut-ball representation rho are the regular marked ones, with volume
Vol(Y_D). There are no independent pieces or arbitrary closing cusps in
this equality case.

Apply (4). It remains to show that conjugacy of the ORIGINAL marked
representation actually determines its labeled face geometry. At every
original MAIN contact, the based meridian supplied by the literal
prefix/turn dictionary is noncentral parabolic and fixes exactly that
contact. At every original MATCHING contact, the recorded full ordered
product P=BA is the noncentral parabolic preferred longitude, and its
unique fixed point is that contact. These are the actual based words of
the original cut balls, not just unbased cusp conjugacy classes. There
are no deleted ports with free peripheral flags here.

A conjugacy to the actual complete holonomy therefore takes every
labeled developed contact to the corresponding original complete
contact. Each original white face of the nondegenerate convex
certificate has at least THREE DISTINCT such contacts. Three distinct
points of CP1 determine a unique generalized circle. Thus every
labeled developed white circle/line is carried to its original complete
white circle/line. This uses the source dictionary as well as the
representation; an unlabeled character alone would not suffice.

Normalize both configurations at their ORIGINAL marked MAIN contact
p=infinity. The conjugacy sends p to p because it carries that based
noncentral meridian. It is therefore affine, z->a z+b, a!=0. Affine
maps preserve bounded disks and oriented center triangles. The two
ordered marked lines also determine the strip sides; the ordinary
bounded circles lie on the prescribed inward sides. Thus the possible
choice of a complementary disk is not an additional freedom.

The complete circle packing has the positive center-triangle signs in
the original cyclic order. The reconstructed signed development must
have those same signs. A GREEN port would have a negative triangle
with an ordinary overloaded middle. Such a triangle cannot be a
sign-invisible two-line triangle: on the original marked MAIN edge
one of its middles is protected, and an outer matching pair cannot be
the two protected vertices. It has either three finite circles or one
line and two finite circles. In the latter case the cooriented line
and horizontal contact order still distinguish its sign. Both cases
contradict the recovered complete configuration. Hence EVERY port of
a maximum is CROSS, and every local triangle angle is its actual
complete geometric angle.

The common affine scale cancels from all angle formulas. Let
q_geom,e=(alpha_x,in+alpha_x,out, alpha_b, alpha_c,
          alpha_y,in+alpha_y,out),
where each alpha is the corresponding complete angle divided by2pi.
Then the preceding argument proves

    q=q_geom, and the maximizing CROSS allocations are geometric.
                                                               (6)

Thus q_geom is the UNIQUE full incidence-flow maximizer. No unspecified
choice of square root, resetting of Gauss flags, or local open-word
regulator invariance was used.

## 3. Compact gaps and the entire one-sided remainder

For every epsilon>0 with a nonempty set in the maximum below, compactness
of Q_D and continuity of the full h give

    gamma_D(epsilon)
       =Phi_D-max_{q in Q_D, ||q-q_geom||>=epsilon} H_D(q)>0.
                                                               (7)

This is a fixed-D gap; no effective uniformity in diagrams or increasing
bridge width is asserted.

There is also a single gap for all one-sided branches. At every original
port its two outer vertices form a MATCHING edge. They cannot both be
the original protected pair, whose edge is MAIN in the simple labeled
certificate. Hence each complete triangle has middle angle strictly
less than pi, even when one outer face is marked. Therefore

    eta_D=min_e {1/2-q_geom,e,b, 1/2-q_geom,e,c}>0.

The closed set

    B_D={q in Q_D: some q_e,b>=1/2 or q_e,c>=1/2}

is separated from q_geom by eta_D in the sup norm. If nonempty, its
maximum entropy is Phi_D-gamma_D^one with gamma_D^one>0.

At even N=2m,d=2m-1 every literal LEFT coefficient has c exponent at
least m, and every RIGHT coefficient has b exponent at least m. After
normalizing by d, any summand with at least one such port lies in B_D.
The actual finite one-sided coefficient is bounded by the full positive
coefficient at the same exponent. The uniform full coefficient theorem,
polynomially many source summands and positivity consequently imply

    limsup_(even N) N^(-1)log Z_(D,N;at least one one-sided port)
                 <=Phi_D-gamma_D^one.                 (8)

When no such feasible source terms exist the left side is -infinity.
The same argument bounds every fixed neighborhood complement by (7).
In particular the whole positive source outside its CROSS contribution
is exponentially smaller, uniformly over all its finitely many
one-sided forest patterns. No subtraction or cancellation estimate is
needed for this positive-source statement.

The odd regularized source has the same uniform h and a positive path
split with LEFT c>=m+1 or RIGHT b>=m+1, d=2m. Thus the same fixed-D gap
applies to its one-sided remainder as well, by the separate exact
[odd comparison theorem](actual_fejer_odd_regularized_full_numerator.md). Its extra visited-central spectral
derivative paths stay in the cross support and are not called a
one-sided remainder.

These gaps do not themselves give a relative Gaussian asymptotic,
a bound on an oscillatory filling transform away from the controlled
spectral region, or a nonzero contribution of the original filling
cycle. Those remain separate quantum statements.

## 4. Review and scope

Root and three independent internal reviewers checked the complete written
argument, including the fixed-representation Cartan compactness step,
the original based contact dictionary, affine recovery of signs and
the compact gaps. This is internal analytical review, not external peer
review. The result is a structural consequence of the linked analytic
and geometric proofs; finite numerical tests are not used to infer
maximal-volume rigidity or uniqueness. The fixed long-filled Kashaev
volume conjecture remains open.
