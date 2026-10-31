# Polynomial-cost sublevel cycles for arbitrarily wide blockwise source cores

28 October 2026. There is a constructive higher-anchor case of the missing
mass theorem. Articulation points split the original coefficient, master,
and torus by an explicit unimodular monomial change of variables. If every
remaining biconnected block is either a two-anchor block or a balanced
unit-factor block, the resulting product cycle has polynomial logarithmic
mass. No semialgebraic triangulation or bound on an integer boundary-matrix
inverse is assumed.

The anchor count is arbitrary but fixed. This does not cover an unbalanced
biconnected block with three or more anchors, does not sum the original
clocks, and proves no new knot volume theorem.

## 1. Same original source and the exact articulation split

Use the strict-Hall master and source of
[the radial transport theorem](actual_anchor_sublevel_radial_transport.md):

    f=P/product_v X_v^(q_v),
    P=gamma product_e(alpha_e X_(u_e)-beta_e X_(v_e)),
    |alpha_e|=|beta_e|=1, sum_v q_v=M.

Original extracted scalars remain in gamma. Parallel factors are retained
with their multiplicities; their underlying simple graph determines the
articulation points. Zero loops and forced cuts have already been treated
by the exact source identities, not removed by an absolute estimate.

Suppose v is an articulation point, and C_1,...,C_s are the components
after deleting v. Put V_a=C_a union {v}, let P_a contain exactly the
factors on V_a, and let M_a=degree P_a. Assign the component charges

    q_u^(a)=q_u, u in C_a,
    q_v^(a)=M_a-sum_(u in C_a)q_u.               (1)

Their sums are M_a, and sum_a q_v^(a)=q_v. These are FORCED charges:
homogeneity makes every coefficient in the exterior C_a require exactly
the displayed remaining power of X_v. Thus

    [product_v X_v^(q_v)]P
        =gamma product_a [product_(u in V_a)X_u^(q_u^(a))]P_a, (2)

where gamma is allocated once, or equivalently kept outside every
scalar-free factor on the right. There is no summation over articulation
charges and no unknown source normalization.

The same factorization holds before integration. Choose X_v=1 as the
common gauge, and use Y_(a,u)=X_u/X_v for u in C_a. Then

    T=(C*)^V/C*  ~= product_a ((C*)^(V_a)/C*),
    f=gamma product_a f_a.                       (3)

This is a unimodular monomial isomorphism, so the logarithmic top form
and the original torus generator are the product forms and generators,
with the common orientation fixed accordingly. Iterating at further
articulations gives the biconnected-block factorization. Each factor
belongs to exactly one block.

Strict Hall is preserved by (1). For a set I not containing v, its
internal factors, crossing count and deficit are exactly the original
ones. For a local set containing v use its nonempty complement J in
C_a and the identity e_I=C_J-e_J. Hence every proper local cut remains
strict. In particular q_v^(a)=C_(C_a)-e_(C_a) is a positive integer.

## 2. The regular critical values also split exactly

In the independent coordinates (3),

    dlog f=direct_sum_a dlog f_a.

A nonzero point is therefore critical exactly when EACH component is
critical. Its value is gamma times the product of their values. Whenever
the component regular critical sets are nonempty,

    Mcrit(f)=|gamma| product_a Mcrit(f_a).        (4)

All blocks used below have a nonempty regular critical set. This is
immediate for balanced blocks by their positive unit-torus maximum.
For a two-anchor strict-Hall block, its Laurent map has poles at both
ends; its derivative numerator has degree m, and removing a root of
multiplicity h from that numerator removes only h-1 copies. Thus at
least one derivative zero remains off its zero divisor.

The identity (4) does not declare these FIXED-clock critical points to
be full knot/Hurwitz critical points. It only gives the exact critical
modulus appearing in the present coefficient estimate.

## 3. Balanced blocks require no deformation or integer-chain estimate

For a block B with incidence counts S_u and charges q_u, suppose

    S_u=2q_u for every vertex u of B.             (5)

On its unit torus every radial derivative of log|f_B| vanishes: this is
the exact off-critical identity with equal endpoint radii and delta=0.
The nonzero maximum on that compact torus also has all angular
derivatives zero. It is consequently a regular complex critical point.

Conversely the cut maximum principle forces every regular critical
point of a connected balanced block to have equal radii. Therefore

    Mcrit(f_B)=max_(unit torus)|f_B|.             (6)

The original unit torus itself lies in the Mcrit sublevel and has
normalized logarithmic top-form mass one. There is no positivity or
noncancellation inference about its integral: it can vanish.

## 4. Two-anchor blocks have the already proved explicit cycle

A two-anchor block with m factors and strict charge 1<=q<=m-1 becomes

    f_B(z)=gamma_B z^(-q) product_(j=1)^m(z-u_j), |u_j|=1.

For every R_B>Mcrit(f_B), the boundary of the component of
{|f_B|>R_B} containing the zero pole is a smooth oriented circle.
It represents the original generator, lies on |f_B|=R_B, and its
normalized logarithmic length tends, as R_B decreases to Mcrit, to
at most

    A_B=4m^2 log(m+1).                           (7)

This is the proved [two-anchor minimax estimate](actual_coefficient_minimax_upper.md).
The circle is a selected component of a degree-2m real algebraic
lemniscate. Its original pole component, not a favorable saddle, selects
it. Repeated or arbitrarily clustered unit roots are permitted.

## 5. Actual polynomial-mass product cycle and its coefficient bound

Assume EVERY biconnected block is either two-anchor or satisfies (5).
For each balanced block retain its unit torus; for each two-anchor block
use the circle above. Their product, followed by the inverse monomial
isomorphism (3), is homologous to the original source torus. Its absolute
logarithmic top-form mass is exactly the product of the block masses,
because the monomial logarithmic determinant is +/-1.

For any R>Mcrit(f), choose the finitely many R_B sufficiently close to
their Mcrit values that the product supremum is less than R. The
constructed product cycle then lies in {|f|<=R}. Its limiting normalized
mass is at most the product of the A_B over two-anchor blocks. Hence

    |I| <=Mcrit(f) product_(two-anchor blocks B)
                                   4m_B^2 log(m_B+1).       (8)

For fixed original diagram width and block count, m_B=O(N), so the cost
is polynomial in N. This bound includes |gamma| through (4). It is not
rescaled by the coefficient I or by a guessed regulator period.

The cycles also have bounded-complexity algebraic supports. They are
products of real algebraic lemniscates and unit tori; the monomial change
has degree bounded by the fixed anchor count. Their support degree is
polynomial in N. Their logarithmic radius range is O(log N), by the
explicit modulus-nonincreasing radial clipping if necessary. On the
product cycle the real logarithmic mass is the product of the block
lengths/torus masses; the fixed monomial change and clipping multiply it
by at most a constant depending on the anchor count. Thus the construction
itself supplies the chain complexity
which cannot be inferred from a triangulation of a general sublevel set.

## 6. Exact remaining scope

This is an arbitrary-width source transport theorem, with a structural
condition on its blocks. Exact articulation factorization reduces the
general mass problem to UNBALANCED BICONNECTED unit-factor cores with at
least three anchors. The statement does not prove that the full original
clock source decomposes into the permitted block family. Actual
macro-defect sectors can contain the excluded cores.

In particular, taking absolute values over clocks after (8) is not a
sharp knot upper bound. The critical actions in (4) are conditional,
and all factorial weights, feedback phases and original normalization
still enter the full source. The missing full-clock support/critical
comparison remains in addition to the unbalanced-core mass problem.

[Audit](../experiments/audit_actual_blockwise_sublevel_source_transport.py):
exact articulation charge and coefficient factorization, strict-Hall
preservation, actual source residual cores and wider mixed balanced/tree
examples, plus critical splitting and the quantitative coefficient bound.
