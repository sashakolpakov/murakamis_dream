# Volume equality for the original untwisted augmented source

30 October 2026. Independently reviewed. This theorem
concerns the original complete-circle source of every fixed connected
augmented plat carrying the stated labeled right-angled geometric
certificate, with NO retained half twists. Its bridge width and matching
graph are arbitrary. Both quantum parities and composite levels occur.
The source is exactly the original marked root invariant with its recorded
normalization; its value is not chosen using the geometric answer.

This is a theorem about complete augmented LINK exteriors. It does not
assert the volume conjecture for general long-filled k-bridge knots.
In a standard adjacent-cap2k-plat the zero-half-twist skeleton has k main
components. A full twist cannot change that component count. Thus the
untwisted result must not be advertised as that knot theorem.

## 1. Precise statement

Fix the literal connected2k-plat box diagram D, k>=2, with R designated
crossing circles and its original physical mark. Require a labeled convex
ideal right-angled polyhedron Q_D whose face identifications are the
actual projection/crossing-disk cut of this diagram. The actual quotient
is its complete hyperbolic augmented exterior Y_D and

    Vol(Y_D)=2Vol(Q_D).

This is the [marked geometric certificate](general_augmented_plat_matching_geometry.md),
not merely the existence of an unlabeled polyhedron or a positive
triangulation of unspecified topology. There is no restriction on R,
bridge width, a Conway grammar, or an octahedral decomposition.

Let A_(D,N) be the ORIGINAL marked complete-circle root source of
[the full matching-graph identity](general_matching_graph_full_normal_source.md),
with epsilon_i=0 at every box. Write chi_(D,N) for its separately
specified exterior framing factor (one when absent); it has modulus1
in the recorded normalization and is retained below.
Then

    lim_(N->infinity) (2pi/N) log|A_(D,N)|
                                =Vol(Y_D).             (1)

In particular A_(D,N) is nonzero for all sufficiently large N. The limit
runs over all positive integer levels, including even and composite
levels. It is not an iterated limit in which the diagram grows with N.

## 2. The exact positive finite source

Set d=N-1 and M=floor(d/2). The
[marked face-coefficient theorem](actual_original_marked_face_coefficient.md)
gives EXACTLY

    A_(D,N)=chi_(D,N) N^R sum_(a in {0,...,M}^R)
                 product_i[k_ai beta_ai^2] C_(N,a),    (2)
    C_(N,a)=[product_(f!=u,v)L_f^d]
                 product_i[D_ai,in D_ai,out P_si] at L_u=L_v=0.

All C_(N,a) are nonnegative, so positivity concerns the scalar after
the displayed common unit phase is removed. The original mark removes exactly the two
face exponents u,v, and total polynomial degree dR excludes every
additional Fourier alias. The primitive face grid supplies precisely
N^R after its original single1/N marked factor. The complete-circle
normal is already in k_ai beta_ai^2. No root-only replacement for an
uncomputed generic normal is made here.

The finite identity also holds for several main components. It requires
connected projection and the literal single marked cap. It does not
replace that mark by independent reduced normalizations on each link
component.

## 3. Lower bound from an actual positive coefficient

Choose the single original label vector a_i=M at every circle. The
[global coefficient saddle theorem](actual_positive_face_coefficient_saddle.md)
applies through both folds. It proves a positive coefficient with an
exact compact-torus integral, a unique positive critical radius near the
actual circle packing, and a nonzero relative Gaussian asymptotic.
Its absolute action is computed from the source determinant and the
actual facet coning:

    lim (1/N)log C_(N,(M,...,M))=Vol(Y_D)/(2pi).         (3)

At the fold beta_M has zero normalized logarithmic rate, k_M is1 or2,
and the factor N^R is polynomial. After removing the same unit phase,
every other term of (2) is nonnegative.
Keeping this ONE actual term therefore proves the required lower bound.
No local-contour contribution or cancellation coefficient is left to
assume in this step.

## 4. Upper bound for the whole original sum

Evaluate all face polynomials at the SAME finite positive circle-packing
radii l_f, with L_u=L_v=0. Positivity gives for each exact coefficient

    C_(N,a)<= product_i[D_ai,in(l)D_ai,out(l)P_si(l)]
                                      /product_f l_f^d. (4)

The [uniform channel-rate theorem](actual_positive_face_channel_rate.md)
keeps the original beta factors and proves a uniform logarithmic rate
for every integer a_i, including0 and both folds. At these shared radii
the local circle rate is strictly increasing in mu_i=a_i/N up to1/2.
Its derivative is the explicit positive quantity

    log[E_b(mu_i)E_c(mu_i)/D_xy(mu_i)].

Thus (4), WITH the beta factors in (2), has normalized rate at most
the all-fold value plus o(1), uniformly over all label vectors. The
actual coning identity fixes that value absolutely as Vol(Y_D)/(2pi).
There are only (M+1)^R channel vectors, the multiplicities are at most
2^R, and the outside N^R is polynomial. Summing the upper bounds does
not change their exponential rate. This proves the matching upper bound
and hence (1).

The same argument gives a strict macroscopic channel gap: for each
fixed eta>0, terms having some a_i/N<=1/2-eta have a smaller common-radius
upper rate by a positive diagram-dependent amount. It does not by itself
give a relative asymptotic in the sqrt(N) folded window.

## 5. What remains for the requested knot theorem

Retained half twists preserve the exact positive coefficients but attach
the original phases product_i omega_ai^epsilon_i to different channels.
The upper bound above survives. Positivity no longer supplies the lower
bound for that signed sum. A uniform relative folded-window estimate
and a nonzero signed Gaussian coefficient are still required generally.

Long fillings require a further source theorem in the EXTERNAL
crossing-circle colors. These are different from the internal a_i in
(2). The existing exact long-filling transform and marked geometric
filling threshold do not supply that mixed-color packet or its alias
gap. The target remains: every fixed essential hyperbolic2k-plat skeleton,
with independently sufficiently long FIXED signed full twists, has the
original knot volume limit. This note establishes the complete untwisted
augmented-source theorem and a general signed-source upper bound; it does
not mark that larger target as solved.

## 6. Dependencies and verification scope

The proof combines exact source normalization/support/measure, a global
positive coefficient saddle, a uniform all-channel upper rate, and an
absolute geometric coning identity. Each dependency has a separate
written proof and focused original-source audit. No finite set of knot
examples, estimated limiting graph values, or unverified literature
proof replaces any of these steps. No novelty or literature-coverage
claim is made by this note.

Independent source and geometry reviews of the complete theorem and its dependency chain: PASS. The primary reader checked every dependency and freshly replayed its focused audit. The reviewers confirmed the N^R measure, retained common exterior phase, all-label upper bound, positive central-sector lower bound, both folded parities and absolute 2Vol(Q) normalization. This is the stated complete untwisted augmented-link theorem; the general signed long-filled knot conjecture remains open.

The [primary-statement coverage comparison](general_untwisted_augmented_source_literature_coverage.md) records prior overlapping families and root conventions. In particular, the parallel-belt examples with even-level zeros fail the required nondegenerate cut certificate; the exact coefficient formula reproduces their zeros. No external proof or priority claim is used.
