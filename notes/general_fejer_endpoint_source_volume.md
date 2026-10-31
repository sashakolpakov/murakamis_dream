# The full even Fejér endpoint source has the actual complete volume

31 October 2026. Independently reviewed general endpoint-volume theorem. This is an endpoint
theorem for the ORIGINAL positive polynomial numerator. It does not
rename that numerator Kashaev's invariant, prove its Gaussian filling
transform, or assert the fixed long-filled knot conjecture.

## 1. Statement and normalization

Fix a connected original flat plat D, at any fixed bridge width, with R
ports and its literal ordered face incidences (x_e,b_e,c_e,y_e). Retain
the original two protected faces u,v and their MAIN edge. Assume the
existing labeled convex ideal right-angled certificate for its actual
untwisted augmented exterior Y_D. Thus Y_D is hyperbolic and its two
original cut balls, white/shaded face pairings, crossing-circle matching
and primitive markings are specified. No realization of an unrelated
triangulation is sufficient for this hypothesis.

For even N put d=N-1 and use the original pair Casimir Omega_N and its
full characteristic polynomial

    chi_N(sigma)=2T_N(sigma/2)+2,
    V_N(sigma)=chi_N(sigma)(sigma-Omega_N)^(-1),
    P_N=-V_N(-2)=4(2+Omega_N)^(-1).

The middle expression is the actual polynomial numerator, including its
repeated-node data. H is the original homogeneous coupon compiler. Set

    Z_(D,N)=[prod_(f ordinary)L_f^d]
                 prod_(e=1)^R H_(P_N)(x_e,b_e,c_e,y_e)
                 |_(L_u=L_v=0).                       (1)

All coefficients in (1) are nonnegative. All source scalars and the
marked coefficient targets are retained; no additional N^R is inserted.
Then

    lim_(even N->infinity) (2pi/N) log Z_(D,N)
                              =Vol(Y_D).              (2)

The limit runs through all even levels, including composite levels.
Its hypotheses impose no bound on the fixed bridge width or number of
ports. The geometric certificate and original flat-plat incidence are
essential stated assumptions. This theorem concerns the complete
augmented exterior, not a metric obtained by long filling.

## 2. One continuous entropy on the full local simplex

The [closed local coefficient theorem](actual_fejer_half_block_entropy.md) gives the one-sided entropy

    E(mu,nu,xi)=inf_l {integral_mu^nu g(t,l)dt-xi*l},
    g(t,l)=l/2+log tan(pi*t)
                        +asinh(tan(pi*t)cosh(l/2)),
    0<=mu<=nu<=1/2, 0<=xi<=nu-mu.

Its triangular endpoint is C(alpha)=E(alpha_b,1/2,alpha_x), for
nonnegative alpha of sum1/2, and its ABSOLUTE normalization is

    C(alpha)=V(2pi alpha)/(2pi),
    V(theta)=2sum_j[Lambda(theta_j/2)+Lambda((pi-theta_j)/2)].

On q=(X,B,Cm,Y)>=0 of sum1 define h by the two E branches when Cm>=1/2
or B>=1/2, and by max[C(alpha)+C(beta)] over the actual cross split when
B,Cm<=1/2. The branches agree at both terminal seams; h is continuous
on the ENTIRE closed simplex and h(0,B,1-B,0)=0.

Every degree-d monomial is present in the full positive H_P. Uniformly
over those monomials, its coefficient p_N(n) satisfies

    N^-1 log p_N(n)=h(n/d)+o(1).                      (3)

This is the [uniform full-kernel theorem](actual_fejer_full_kernel_entropy_identity_reduction.md), proved from the closed
half-block estimates, positive cross convolution, the coefficientwise
cross comparison and continuous seam values. It retains the finite
forced outer factor. It does not require assigning a fixed half label
to a limiting seam point.

Let Q_D be the compact nonnegative incidence-flow polytope: each port
supplies1, each ordinary face demands1, and protected demands are0.
Repeated local incidences remain distinct arcs. Scaling a flow by d
and fractional-cycle rounding preserves exact integer balances with
at most one unit of error per incidence. Every rounded local vector
is in the full support. The number of summands is polynomial in N.
Thus (3), positivity and compactness prove

    lim_(even N) N^-1 log Z_(D,N)
       =W_D:=max_(q in Q_D) sum_e h(q_e).              (4)

The [all-cross comparison](actual_fejer_cross_half_source_reduction.md) and the
[complete source volume theorem](general_signed_augmented_source_volume.md) give W_D>=Phi_D:=Vol(Y_D)/(2pi). It remains to prove the
opposite inequality for a maximizer of (4).

## 3. Remove pure-middle maximizing ports by exact source identities

Choose a maximizer q, including maximizing triangle allocations at its
cross ports. Let J consist of ALL ports with both outer loads zero.
This includes one-sided diagonals and the pure-middle cross seam.
The literal identity coupon is

    H_1(b,c)=sum_(j=0)^d b^j c^(d-j).

It has entropy zero on the whole pure-middle segment, and coefficientwise
H_1<=H_P. The mixed source with H_1 on J therefore has rate at most W_D.
The SAME maximizing q is feasible for its mixed flow problem and has the
same entropy. The full-kernel flow theorem with identity nodes gives
the reverse inequality, so these rates are EXACTLY equal. No finite
cross monomial with zero outer degree is invented.

The selected middle edges form a forest in the ORIGINAL gap graph.
Every possible original middle cycle contains the protected exterior;
its unit edge supplies would exceed its vertices' total demand. A tree
cannot contain both protected vertices either, by the same load count.
For each remaining monomial, its identity degrees along a tree are
uniquely determined by subtree balances and lie between0 and d.
Consequently exact coefficient extraction contracts each identity tree
to its ordinary/protected merged face, with coefficient one and no
multiplicity. This is the [actual connected identity smoothing](actual_fejer_diagonal_identity_forest_reduction.md).

The inherited maximizing local vectors at the remaining ports still
have positive total outer load. A loop in the smoothed white cellulation
would enclose v ordinary vertices but only v-1 whole ports and one
half port. Its demand forces that half port's middle load1, making it
pure-middle, a contradiction. A retained matching edge between the two
protected roots would also force a pure-middle port. Thus the remaining
white triangular cellulation is loopless, with distinct adjacent
protected roots. Multiple edges are retained. The empty source has
rate zero and is handled separately; it cannot attain W_D>=Phi_D>0.

## 4. Hybrid Hall theory resolves all remaining forced boundary degrees

At the inherited maximum tag each B,Cm<=1/2 port CROSS, retaining its
two triangle allocations. Every other port is GREEN, in a strict
one-sided chamber with 0<=mu<nu<1/2. A CROSS port supplies two triangle
nodes of mass1/2. A GREEN port supplies one node of mass1 incident to its
four original faces. Its entropy is E, not two independent triangle
entropies. A shared outer incidence is aggregated once for this node.

For an ordinary vertex set S, merging a triangle pair changes its Hall
capacity by +1/2 exactly when one triangle touches S and the other does
not. It never decreases capacity. The [hybrid Hall theorem](actual_fejer_hybrid_tight_cut_reduction.md) proves:

* Every proper tight set is a union of actual digon interiors, after
  adjoining neighboring holes joined by a GREEN matching edge.
* Their surviving cuts are MAIN/MAIN, or MATCHING/MATCHING with BOTH
  boundary ports CROSS. No GREEN pair is split.
* These tight sets explain exactly the structurally forced zero arcs.
  Every other ordinary arc is positive in one common feasible witness.

For completeness, the counting behind this classification is exact.
On the induced graph of U=V\S, let p count ORIGINAL triangle faces and
n=|U|. Euler and boundary-walk length at least2 give p<=2n-4; equality
forces a connected induced graph whose other faces are genuine digons.
Hybrid equality additionally forbids a GREEN edge from separating a
triangle touching S from one not touching S. Adjacent such holes merge
along the same parallel-edge pair. For proper S these mergers are paths,
not cycles. Thus the surviving cuts have precisely the types above.
The reserve-epsilon Hall test then proves the positive-witness assertion.

Split along these actual permitted cuts, iterating on the inherited
marked pieces. The child boundary loads are zero. At a matching cut,
the separated CROSS triangles are the original additive C rows; their
pure-middle closing caps have entropy zero. Formal re-pairing of two
boundary C rows is only bookkeeping and creates no physical coupon.
The resulting hybrid flow and entropy constraints are Cartesian across
pieces. Every piece perturbation reassembles an original cross split,
whose full h is at least the corresponding C+C value. Hence the inherited
point is maximizing on each piece.

Mix that point slightly with its strictly positive relative hybrid
witness. CROSS allocations stay within their triangle simplexes, so
no terminal seam is pushed into a losing one-sided chamber. The strict
GREEN row margins persist. The [proved corner expansions](actual_fejer_nondiagonal_maximizer_regularity.md) give only
nonnegative epsilon log(1/epsilon) terms and a strictly positive one
at every activated ordinary zero. All other changes are O(epsilon).
Maximality therefore excludes every ordinary zero except the two marked
faces and the zero-dimensional closing rows. Diagonal losses are absent:
all pure-middle ports were removed in section3.

Finite-dimensional row-space Lagrange multipliers now exist on each
piece, including when the balance equations are redundant. Exponentiating
them gives finite positive ordinary curvatures. The local equations are
the actual tangent-circle formula for each C row and the actual Green
equations L(mu;x,y)=b, L(nu;x,y)=c for each E port, with their proved
one-line/two-line limits. Every ordinary signed star sums to0 or2pi.

## 5. The entropy is the volume of a representation of the ORIGINAL group

The [hybrid-piece representation theorem](actual_fejer_hybrid_piece_representation.md) applies to exactly these data.
Its essentials are included here to specify the volume being bounded.
Each piece develops ONE signed circle family by finite-center star
holonomy. The marked edge may be MAIN or MATCHING. In the latter case
its two incident rows are the positive zero-entropy CROSS closing halves,
so the same two-line strip construction applies. All permitted parallel
marked chords have been split. No unproved translation holonomy remains.

Along the actual cut tree, map each child's ordered tangent boundary
planes to the parent's pair by ONE Mobius map. This gives one reflection
for each occurrence of an actual shared white face. A GREEN port remains
within one piece and retains its entire local source collar. At an
ORIGINAL CROSS port spanning pieces, the common outer product P is
noncentral parabolic. Its two raw first meridians have trace-2 and
Tr((P+I)A)=4. The parabolic centralizer acts simply transitively on them,
so there is a unique C mapping the WHOLE ordered input pair to the output
pair and all three recorded contact flags. This is the original shaded
pairing, even when its two triangles lie in different pieces.

Use the two ORIGINAL topological cut balls and the original face maps.
One global reflection develops the second ball. Their proper digon-cut
disks have both ends at the same tangent-pair contact. Compatible finite
incidence horospheres and the short-edge tetrahedron bound make the added
cut-disk volume tend to zero. Signed cyclic polygon coning, including
winding-zero faces and repeated contact images, then computes the actual
relative fundamental chain:

    Vol(rho_sm)=sum_pieces sum_triangles sigma V(theta)
              =2pi*(inherited maximizing entropy).     (5)

Each piece uses its own genuine marked contact in this chain calculation.
Mobius invariance is used for geometric tetrahedron volumes, not for
an open crossing expression with a reset Gauss flag. The failed local
re-framing argument is neither needed nor reinstated.

Finally restore the deleted ORIGINAL auxiliary meridians as identities.
The ordered physical pairs coincide across each identity smoothing.
Their outer product need not be parabolic; the established axial
(loxodromic or elliptic), parabolic, or central zero-volume filling cap
retains its actual peripheral flag. Thus rho_sm extends through the
actual quotient to a representation rho of pi_1(Y_D), with the SAME
relative volume. Equations (4)--(5) give

    2pi W_D=Vol(rho)<=Vol(Y_D).

The last inequality is the [independently proved representation-volume
bound](general_representation_volume_kernel_strictness.md) for the original hyperbolic exterior. Together with the all-cross
lower bound this proves (2), including the absolute volume constant.

## 6. A strict identity-insertion consequence

The same argument starts with any fixed nonempty set I of original
identity coupons and P coupons elsewhere. If its mixed incidence polytope is empty, its coefficient is zero at
every even level and its rate is -infinity. Otherwise its original identity graph is a
forest with at most one protected vertex per tree, and its coefficient
contracts exactly. The full-kernel theorem gives a compact maximum.
Any further pure-middle maximum ports can be added to I: lifting the
identity degrees gives a feasible pure-middle assignment in the ORIGINAL
graph, so the union is again a permitted forest. The hybrid argument
and actual representation assembly then apply unchanged.

The resulting representation kills each specified original auxiliary
meridian. Those are essential in Y_D. The [already proved strict-kernel
volume bound](general_representation_volume_kernel_strictness.md) therefore gives

    lim_(even N) N^-1 log Z_(D,N;H_1 on I)
                              <Vol(Y_D)/(2pi).         (6)

The empty remaining source has rate zero, also strictly below the
positive complete hyperbolic volume. This is a strict statement about
the actual positive identity-inserted source. It is not a phase-sensitive
estimate for all small colors or a replacement for their normal data.

## 7. What is still required for the requested knot conjecture

The theorem closes the COMPLETE even positive endpoint estimate, at
arbitrary fixed bridge width under the labeled geometric certificate.
It does not control the full Gaussian-resolvent contour away from this
endpoint, its nonzero Fourier charges, the selected geometric cycle or
its nonzero contribution. The [odd regularized numerator theorem](actual_fejer_odd_regularized_full_numerator.md)
now supplies the same rate for its actual value-plus-spectral-derivative
coupon, and fixed spectral jets have an explicit polynomial bound. These
are spectral derivatives at the fixed root, not genuine-q normals. Independently long fixed signed fillings still require
those quantum inputs, with the original peripheral normals and scalars,
before the filled hyperbolic volume can be concluded.

The general original Kashaev volume conjecture remains OPEN. Its target
has not been replaced by (2).


## 8. Independent review and focused verification

Root and all three independent reviewers checked the complete proof,
including the original normalization, full-support entropy, exact identity
contraction, hybrid cut regularity, actual group/relative chain, and the
strict identity-insertion corollary. This is internal analytical review,
not a claim of external peer review.

The [focused structural audit](../experiments/audit_general_fejer_endpoint_source_volume.py)
and [recorded results](../experiments/general_fejer_endpoint_source_volume_results.json)
check 41 literal loopless identity smoothings at widths two, three and
four; 918 hybrid patterns; 121004 exact Hall cuts; 716 tight-set covers
by independently constructed actual dual digon disks; and 816 independent
positive-arc max-flow tests. The original local coefficient, physical
source and signed-volume audits remain linked in the dependencies. These
finite tests supplement the general proof; they do not numerically prove
the asymptotic or the relative fundamental-class identification.
