# The even Fejér source: complete crossing paths and a forest remainder

Status update, 31 October 2026: the [full endpoint theorem](general_fejer_endpoint_source_volume.md) now controls the entire positive source, and the [unique-maximizer theorem](actual_fejer_unique_geometric_maximizer.md) gives a strict exponential gap for the one-sided remainder under the same labeled certificate. The exact decomposition and the warnings about inferring bounds from forest topology alone remain valid.

, 31 October 2026. This is an exact coefficient reduction at every
even level N>=4 for the original connected fixed flat plat. No estimate
of the remaining forest contribution is asserted. The shared original
marked targets are unchanged. The geometric rate corollary assumes the
same labeled right-angled certificate as the complete-source theorem.

Let N=2m>=4,d=N-1, c_j=2cos((2j+1)pi/N), s_j=2sin(jpi/N).
In the actual face monomial basis,

    Omega z^j=c_j z^j-s_j^2(x+y)z^(j-1)-s_js_(j-1)xy z^(j-2).

Use the [original homogeneous compiler](actual_homogeneous_casimir_face_source.md).
Let chi_N(z)=2T_N(z/2)+2 and V_N(z)=chi_N(z)(z-Omega)^(-1), its
polynomial resolvent numerator. Let P=-H_(V_N(-2)) be the positive Fejer
homogeneous polynomial. The exact fixed-root resolvent convention is
that of the [spectral derivative theorem](actual_spectral_total_derivative_source.md).
Every path goes from its input j to its output i using steps1 or2;
its middle exponents are b^i c^(d-j). A k-step path contributes its
positive edge product times product_(unvisited r)(2+c_r), with the
usual binomial expansion of its one-step factors (x+y).

Split P=P_cross+P_left+P_right by

    cross: i<=m-1 and j>=m;
    left: j<=m-1;
    right: i>=m.

These three classes partition the actual path set. Equivalently the
cross part consists of monomials whose b and c exponents are both<=m-1.
The two other classes have respectively c exponent>=m or b exponent>=m.
Thus the decomposition is also by disjoint monomial supports, without
any cancellation or selection of a new physical state.
The three polynomials are parts of the original homogeneous coupon;
they are not asserted separately to be covariant Casimir coupons or
physical-head projections. The identity between the original source
and the coefficient of their SUM is the frozen compiler identity.

## 1. Exact coefficientwise comparison for the entire cross part

Put c_*=-2cos(pi/N), delta=2+c_*=4sin^2(pi/(2N)). The two minimum
diagonal entries are c_(m-1)=c_m=c_*. At spectral value c_* the
polynomial numerator has a nonzero path exactly when it visits BOTH
indices m-1,m: otherwise its unused-factor product contains a zero.
Call the resulting positive polynomial B=|H_(V_N(c_*))|_coef.

For a path visiting both central indices, its coefficient at -2 divided
by its coefficient in B is a subproduct of

    (2+c_r)/(c_r-c_*), r notin{m-1,m}.

Every ratio is>=1, and the product of ALL such ratios is exactly

    C_N=[4/delta^2]/[chi''(c_*)/2]
       =4(4-delta)/(delta N^2)<2.                       (1)

Here chi(-2)=4 and chi''(c_*)/2=N^2/[delta(4-delta)]. The bound
delta N^2>=8 follows from the chord bound for sin on[0,pi/4].
Consequently B<=P_both<=C_N B coefficientwise.

Every cross path that misses one of the central indices has exactly
one crossing two-step: either m->m-2 or m+1->m-1. Split that step into
two consecutive one-steps. This produces a path visiting both central
indices, with the SAME input/output and total face degree. Its other
edges and unused factors are unchanged; only the missed central factor
delta is removed. If the original two-step starts at j0, its edge is
s_(j0)s_(j0-1)xy and the repaired pair is
s_(j0)^2s_(j0-1)^2(x+y)^2. Since xy<= (x+y)^2/2 coefficientwise,

    original path <= delta/[2s_(j0)s_(j0-1)] * repaired path
                  =delta/[8cos(pi/N)] * repaired path.   (2)

A repaired path has at most TWO original preimages (merging either
of those two pairs). Hence

    B <= P_cross
      <= C_N[1+delta/(4cos(pi/N))] B <3B.               (3)

The last bound uses N>=4, delta<=2-sqrt2 and cos(pi/N)>=sqrt2/2.
All statements are coefficientwise, so they remain true at zero
protected faces and after every original shared coefficient extraction.

Let H_M be the actual maximal complete-channel contribution to H_(L_N),
including N k_M beta_M^2 D_M(x,b,y)D_M(x,c,y)Ptilde_1(x,y),
M=m-1. The exact paired derivative formula gives H_M=2B/N. Thus

                 (N/2)H_M <= P_cross <= (3N/2)H_M.      (4)

Here beta and D are the literal factors of the
[complete-circle polynomial theorem](actual_complete_circle_positive_face_polynomial.md).
This includes the forced factor x+y and the actual multiplicity k_M=2.
It is a comparison within the original source coefficient, not after
choosing independent local radii. For a diagram with the stated geometric
certificate, the all-cross term of the entire marked Fejer source has
exactly the [known complete-volume exponential rate](general_signed_augmented_source_volume.md),
with only fixed-diagram polynomial factors between its two bounds.
At odd N the full positive endpoint numerator is already N times the
simple maximal complete coupon, so its whole coefficient has that rate
directly. The forest remainder treated here is specific to even levels.

## 2. Exact shared degree restriction on the remainder

Expand the whole positive product by choosing cross,left,right at each
original port. A noncross port puts at least m units into exactly one
of its two middle faces: c for left, b for right. Draw its middle-graph
edge pointing to that overloaded face. Each ordinary face has target
d=2m-1, so it cannot receive TWO such arrows. Each protected face has
target0, so it receives none.

The original flat-plat middle graph has the
[frozen gap description](actual_simultaneous_small_circle_face_correspondence.md):
each odd gap is a path of distinct bounded faces; each internal even
gap is a cycle based at the SAME exterior face u, with its other faces
unique to that gap. Therefore every selected-edge cycle contains u.
An orientation with indegree<=1 at each vertex and indegree(u)=0 cannot
exist on such a cycle: its equal numbers of edges and vertices would
force indegree1 everywhere. This includes the length-two multicycles.

Thus every nonzero remainder term is a ROOTED FOREST of noncross
middle edges. Each component has exactly one indegree-zero root;
any protected face in that component must be that root. Geometry
independently checked this use of the frozen gap lemma. No free
re-marking, smoothing order, or graph-to-plat adapter is used.

This is the precise remaining positive source problem: bound the
shared marked coefficient for these one-sided forest components,
with the cross coupons on their complement. The cross comparison(4)
does not estimate their weights. Local positive-radius estimates can
be too large and are not substituted for this shared problem.

## 3. Exact half-size factorization, without an asymptotic conclusion

For a left path all visited rows are in0,...,m-1, so every upper-half
diagonal factor is unused. Their product is exactly2, since the two
halves have equal products and chi(-2)=4. Moreover c^(d-j)=c^m c^(m-1-j).
Consequently P_left=2c^m times the degree-(m-1) positive polynomial
resolvent numerator of the literal lower m-row triangular block,
at spectral value -2. The analogous upper block gives P_right with
the factor b^m. All original sine coefficients are still evaluated
at level N, not at level m. Replacing them by a level-m source would
be a new, unproved step.

The factorization explains the overloaded-face condition but does not
yet identify an entropy or an actual smoothed representation for the
forest. In particular the already proved L_1 smoothing gap cannot
be applied merely because the selected middle graph is a forest.

## Validation and remaining scope

The [focused audit](../experiments/audit_actual_fejer_cross_half_source_reduction.py)
checks the complete positive path sum, the central coefficient comparison,
the repair and half-block identities, and actual original gap charts.
[Results](../experiments/actual_fejer_cross_half_source_reduction_results.json)
include nonzero marked-target support terms with noncross ports: the
forest contribution does not vanish merely by this graph argument.
The source interface of the path representation is separately audited
against the original coproduct matrices; these new checks do not relabel
that earlier test as a new independent physical-matrix construction.

The positive path partition is not a covariant complete-colored image or a half-colored tensor. The scalar identity does not justify an $L^1$ smoothing argument for the half-block forest.