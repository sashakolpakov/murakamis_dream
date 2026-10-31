# Composition of original matched-disk boundary data

31 October 2026. **exact-source and analytical research theorem.**
Unpublished.
This is an exact composition law for admissible disk modules built from
WHOLE original matched ports. It concerns the actual positive CROSS
source and its classical boundary response. It does not assert that
every Conway/arborescent tangle admits this geometry, that arbitrary
diagonal changes preserve a filled knot, or that signed quantum volume
gaps follow from composing classical curves.

## 1. The compositional object retains weights, loads and the primitive

A module is a finite union of original matched triangle pairs, with
all its boundary edges MAIN. Its coupons retain their ordered frames.
Protected face weights are set to zero before every extraction.
Let I be its ordinary vertices whose original targets are internal
to the module, and B its remaining ordinary boundary vertices. For
every ordinary graph component require a vertex in B. Suppose the
module has one finite positive weight assignment with all supported
ordinary incidences positive and every I load equal to one.

At the actual CROSS endpoint define, at either parity,

\[
P_{\mathcal M,N}(L_B)
 =\left[\prod_{i\in I}L_i^d\right]
   \prod_{e\in\mathcal M}P_{e,\mathrm{CROSS}}(-2;L),
 \qquad d=N-1.\tag{1}
\]

Every actual coupon scalar and fixed raw sign is retained, or a single
declared product of its fixed raw unit signs is removed consistently.
The degree in all boundary weights is

\[
\deg P_{\mathcal M,N}=d\kappa_{\mathcal M},\qquad
\kappa_{\mathcal M}=|\operatorname{ports}(\mathcal M)|-|I|.\tag{2}
\]

The object is this original coefficient module, not a separately
closed tangle invariant with a guessed pivotal trace. No new cup/cap
normalization is introduced along the cut.

Let z_b=log L_b and put

\[
F_{\mathcal M}(z_B)
 =\inf_{w_I}\left\{\sum_{t\in\mathcal M}Q_t(L)-\sum_{i\in I}w_i\right\}.
\tag{3}
\]

The recession proof of the [algebraic boundary-pressure theorem](research_cap_algebraic_boundary_curve_and_volume_period.md)
applies verbatim:
the known strict allocation makes every recession summand nonnegative;
equality forces a constant on every supported triangle and hence zero
after the boundary anchors. The grounded Hessian is positive definite
at every finite positive weight. Thus the minimizer is unique and
finite for every finite real z_B, and F_M is real analytic there.
Define the actual lifted boundary loads and phases

\[
q_{\mathcal M,b}=\partial_{z_b}F_{\mathcal M},\qquad
B_{\mathcal M,b}=\exp(2\pi i q_{\mathcal M,b}).\tag{4}
\]

They obey sum_B q_(M,b)=kappa_M by homogeneity. The phase tuple does
not determine these integer lifts or the absolute value of F_M.

As before, introduce positive square roots T_t^2=ab+ac+bc for every
nonmonomial triangle, retain pure-corner factors -1, and impose the
interior equations prod_t (T_t+iL_i)/(T_t-iL_i)=1 with their original
load-one lifts. The invertible interior Jacobian makes the selected
boundary phases algebraic functions of the boundary weights. Their
graph defines an algebraic boundary correspondence on the selected
regular component, with differential

\[
dF_{\mathcal M}=\sum_{b\in B}q_{\mathcal M,b}\,d\log L_b,
\qquad
\sum_b d\log B_{\mathcal M,b}\wedge d\log L_b=0.\tag{5}
\]

The latter follows from Hessian symmetry. The graph has dimension
|B| in the 2|B|-dimensional boundary weight/phase torus; locally it
is Lagrangian for that displayed logarithmic symplectic form. Common
scaling is retained, with its known linear primitive kappa_M log(scale).
This is source boundary data, not an asserted knot character variety.

At odd levels the actual stable positive determinants and the anchored
ordinary phase graph give the same finite positive saddle as in the
one-cap pressure theorem, now with several external z coordinates:
the interior torus has one angular maximum, a positive grounded
Hessian and an analytic critical point on a fixed small complex
boundary neighborhood. Its normalized logarithm tends to F_M there.
The determinant and original coefficient measures retain their
polynomial N factors. This statement uses the actual positive source;
it is not an assertion about a negative-axis or truncated signed sum.

## 2. Admissible disk gluing and exact finite coefficients

Take two such modules with disjoint port interiors. Identify a specified
MAIN boundary arc of the first with a specified MAIN boundary arc of
the second, reversing boundary orientation and respecting the recorded
vertex labels and bipartite colors. Alternatively glue their entire
boundary circles to form a sphere. Within each old module the map on
vertices is injective. All old matching edges and ordered port disks
remain internal and unchanged.

Identified vertices must agree in their protected/ordinary status.
If a proposed new mark changes that status, first specialize the
newly protected labels to zero in BOTH module definitions, then
recheck their stated positivity and anchoring hypotheses. One cannot
glue a positive ordinary boundary variable to a protected zero and
silently keep the old positive pressure branch.

This constructs the usual disk or sphere cellulation. For a geometric
simple-white application it must additionally have no loops, repeated
edges or repeated vertices in a port. The last condition follows from
the injectivity just stated; repeated edges from two old diagonals
are an actual possible obstruction and must be checked. These are
explicit combinatorial admissibility conditions, not automatic facts
about arbitrary Conway compositions.

For an OPEN glued module impose an additional anchoring condition:
EVERY resulting ordinary graph component must meet a retained ordinary
boundary vertex. This does not follow merely because both child
modules were anchored; gluing may consume their last anchors. If an
unanchored component is instead a balanced closed component, treat
its scalar coefficient factor separately and fix one common scale
in that component for the classical minimization. A strict load-one
solution requires its total triangle supply to equal its total
ordinary demand; an unbalanced closed component has no such branch.
For an eligible full sphere with connected ordinary graph, in particular
with the original protected adjacent MAIN pair, one global scale is enough.

Let S consist of the identified ORDINARY boundary vertices that become
internal and acquire their original demand one. Shared vertices that
remain on the external boundary keep a single common boundary weight.
Protected vertices retain zero weight and are never assigned a d
extraction. Under the literal source identification,

\[
P_{\mathcal M_1\cup\mathcal M_2,N}(L_B)
 =\left[\prod_{s\in S}L_s^d\right]
 P_{\mathcal M_1,N}(L_{B_1})P_{\mathcal M_2,N}(L_{B_2}).\tag{6}
\]

This is simply the coefficient of the product of the same original
coupons: the two sets of old internal variables are disjoint, and
they are absent from the other module. Coefficient extractions
therefore commute. Shared unextracted variables are identified before
the last extraction. There is no independent variable for a repeated
face occurrence, no shifted residual target, and no missing normalization.
The degree check is kappa_glued=kappa_1+kappa_2-|S|.

The right side of (6) is not claimed to preserve joint real stability
under an arbitrary total-degree projection. It uses the precise
individual original face extractions. If a different tangle operation
requires a total degree or a linear combination of cut states, (6)
does not silently replace that operation.

## 3. Classical pressures and algebraic boundary correspondences compose

The exact classical law corresponding to (6) is

\[
F_{\mathrm{glued}}(z_B)
 =\inf_{z_S}\left\{F_1(z_{B_1})+F_2(z_{B_2})-\sum_{s\in S}z_s\right\}.
\tag{7}
\]

Indeed expanding (3) on the right gives the joint infimum over ALL
old interior weights and the new shared interior weights of the sum
of the unchanged triangle potentials with each interior target log
subtracted exactly once. This is exactly the definition of the glued
pressure. Infimum associativity proves (7) even at a boundary dual
limit; no exchange with a shared entropy maximum is used.

For a finite strict positive glued branch satisfying the resulting
anchoring condition, the same coercivity and Hessian argument gives
unique finite minimizers. Each balanced closed component is instead
handled with its separate scalar factor and one scale fixed, as just
specified. In an eligible full sphere with connected ordinary graph,
in particular with the original protected adjacent MAIN pair, this is
the single common scale.
At
each shared interior face the actual gluing condition is

\[
q_{1,s}+q_{2,s}=1,\qquad B_{1,s}B_{2,s}=1.\tag{8}
\]

The SECOND equation alone loses the required integer. At a retained
boundary face b the loads add over its actual old occurrences and
the phases multiply:

\[
q_{\mathrm{glued},b}=\sum_{i:\,b\in B_i}q_{i,b},\qquad
B_{\mathrm{glued},b}=\prod_{i:\,b\in B_i}B_{i,b}.\tag{9}
\]

Thus the algebraic boundary correspondence composes by matching common
weights, imposing the phase equations in (8), and eliminating the
shared variables, while retaining the original load-one lift and the
selected positive branch. Elimination without those choices may keep
unrelated components or wrong integer loads.

The pressure primitive composes with the explicit target correction:

\[
F_{\mathrm{glued}}=F_1+F_2-\sum_{s\in S}\log L_s.\tag{10}
\]

evaluated at the shared critical weights. Differentiating (10), the
shared-weight terms vanish by the FIRST equation in (8), leaving
exactly the external differential in (5). Therefore the corresponding
relative logarithmic periods add, with their original absolute base
constants and the displayed target-log term. The eliminated curve
alone does not retain those constants.

Finite coefficient associativity, joint infimum associativity and the
lifted equations prove associativity of these laws for any finite
admissible assembly of modules. This is a closure theorem for actual
source boundary data, not just a relabeling of a list of knot families.

## 4. What this supplies for a tangle formulation

When a tangle decomposition is represented by such cuts of actual
ordered matched-port disks, the original source coefficient and its
positive boundary curve/period can be computed module by module using
(6)-(10). If the resulting simple matched sphere carries the eligible
original protected adjacent MAIN pair and the hypotheses of the
original complete-packing theorem, that theorem identifies the full
complete critical value with its original drilled hyperbolic volume.
The inherited zero set and mark are part of this hypothesis, not
consequences of simplicity alone. Nothing in the composition
requires calling the whole diagram a bridge presentation.

To apply this to a proposed Conway/algebraic tangle operation one must
still verify its literal MAIN-arc boundary identification, original
coupon frames and face targets, and the simplicity/packing hypotheses
of the resulting source. This note does not identify every algebraic
knot with such an assembly or transport integer long fillings through
a rotated diagonal. The signed non-CROSS/cap cancellation inequality,
even-parity negative-axis adapter, and filled-period estimates remain
their separate original-source questions.

## Inputs

The [original homogeneous source](actual_homogeneous_casimir_face_source.md)
and [matched-sphere Morse construction](research_matched_sphere_morse_source.md)
retain the literal ordered port disks, face variables and target
extractions used in (1) and (6). The
[triangle entropy theorem](actual_triangle_entropy_algebraic_balance.md)
fixes the local half-supply potentials in (3).
The [algebraic boundary-pressure theorem](research_cap_algebraic_boundary_curve_and_volume_period.md)
supplies the coercivity, regular algebraic branch and retained-load
arguments generalized to several boundary variables here. The
[actual CROSS determinant factorization](actual_cross_cofactor_factorization.md)
and [positive face-coefficient saddle](actual_positive_face_coefficient_saddle.md)
supply the odd-level positive pressure identification. The
[complete packing capacity](actual_smoothed_source_capacity_blocks.md)
supplies the drilled-volume identification only under the original
marked packing hypotheses stated in section 4.

Every resulting ordinary component must satisfy the stated anchoring condition. Gluing also preserves protected versus ordinary status and the inherited marked pair.

No numerical audit is used or claimed. This theorem composes actual
admissible source boundary data. It does not prove that every Conway
tangle operation preserves the required source geometry, identify a
knot A-polynomial, transport arbitrary fillings, or supply an unsigned
or signed non-CROSS volume bound.
