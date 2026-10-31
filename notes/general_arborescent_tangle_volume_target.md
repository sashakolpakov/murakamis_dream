# Volume equality through Conway tangle composition

31 October 2026. Current research formulation, following the user's
explicit choice of Conway algebraic/arborescent knots. Bridge number
is no longer the organizing parameter. The active objective remains
a general equality for the original invariant with the ACTUAL
hyperbolic volume; the full arborescent target below is open.

## 1. The target is a composition theorem

An algebraic tangle is obtained from rational tangles by the literal
Conway sum/product operations and rotations. Close the resulting
four-port tangle by a specified numerator or denominator closure,
retaining its endpoint order. When the closure has one component it
is a Conway algebraic, or arborescent, knot. This is the sense used
here, consistent with [Wu's definition](https://homepage.divms.uiowa.edu/~wu/papers/p17.pdf).
It is not the plane-curve-singularity meaning of algebraic knot.

Fix a reduced, marked tangle expression tree tau, with a specified
continued-fraction presentation of each rational leaf, explicit twist
boxes, and a closure. Every twist box retains its disk framing and a
half-twist parity epsilon_e; its final exponent is epsilon_e-2p_e.
Require the resulting diagram to be a knot and its marked augmentation
to satisfy the actual hyperbolic/source hypotheses being used. Those
requirements must be verified, not inferred from the word arborescent.

The desired theorem is: for each such fixed admissible template tau,
there is T(tau)<infinity such that every independently chosen fixed
signed filling vector with |p_e|>T(tau) has

\[
 \lim_{N\to\infty}\frac{2\pi}{N}
     \log|K_N(K_\tau(p))|
       =\operatorname{Vol}(S^3\setminus K_\tau(p)). \tag{1}
\]

The template, parity pattern and twists are fixed BEFORE the quantum
level tends to infinity. Both level parities and composite levels
belong to (1). The right side is the knot complement volume after the auxiliary
fillings; the knot cusp itself remains unfilled. No threshold depending only on tree depth,
valence or bridge number is asserted.

The useful structural task is to prove that the required source,
boundary-period and signed-estimate properties survive the actual
tangle operations. Arbitrarily large coefficients in a fixed rational
tangle do not by themselves prove such closure.

## 2. The baseline grammar and its subsequent enlargements

The existing internally reviewed Conway results already give a
constructive subclass with unbounded branching and turn depth. After
ALL auxiliary circles are filled, write

\[
 h(n)=\mathcal R(R^n),\qquad n=\epsilon-2p,\qquad
 A_s=h(n_1)\cdots h(n_s),\quad s\ge3. \tag{2}
\]

Here R^n means the literal integral two-strand twist tangle, and
mathcal R is the actual quarter-turn with the recorded oriented cups
and caps. Each h(n) is rational. Generate expressions by

\[
 E ::= A_s\ (s\ge3)\quad|\quad\mathcal R(E)
                     \quad|\quad E_1E_2. \tag{3}
\]

The retained closure class is C(FG), with both F and G in (3), plus
the isolated C(A_s) for s>=4. The isolated C(A_3) is outside the
mixed-color long-filling theorem. Each expression and every s are
fixed but otherwise unbounded.

The [signed long-filling theorem](actual_odd_conway_long_filling_volume.md)
and its [arbitrary-width extension](actual_conway_arbitrary_width_seeds.md)
state (1) for this literal class, at independently sufficiently long
signed fillings, whenever its parity pattern gives a knot. Their
connectivity construction supplies such a pattern for EVERY allowed
expression. It is a choice of endpoint pairings, not an assertion
that every sign/parity pattern has one component.

Here is the exact membership argument. Filling an original auxiliary
circle replaces its box by R^(epsilon-2p), with its original disk
framing. All auxiliary components disappear when all are filled.
Its turned leaf is the rational tangle h(n). Actual stacking and
quarter-turns are Conway operations, so structural induction on (3)
gives an algebraic tangle. Its literal cylindrical closure is a
Conway closure; a loop-free one-component endpoint pattern makes it
an arborescent knot. No addition of numerical fractions is used to
claim that a sum of rational tangles is rational. With partial fillings,
auxiliary components remain and this all-filled membership statement
is not the asserted description of the whole link.

This membership audit does not reprove every analytic dependency of
the existing long-filling theorem. It locates its exact topological
scope. In particular there is NO coverage theorem identifying every
algebraic tangle with grammar (3). The seed grouping, closure choices,
parity test and long-filling conditions remain substantive. A continued-
fraction chain cannot be replaced by a three-leaf seed merely because
some numerical tangle fractions coincide.

The [new two-leaf theorem](actual_arborescent_algebraic_leaf_long_twist_volume.md)
extends the retained C(FG) class to seeds of every width s>=2, provided
the actual selected complete port solution satisfies

\[
              X_\ell=\cot(\pi a_\ell)>0,
                       \qquad 9X_\ell^2\ge4             \tag{3a}
\]

at every leaf. This is a finite algebraic sign test on an isolated
selected geometric solution. All old proper seeds with s>=3 satisfy
it automatically; only the new two-leaf seeds need checking. The
actual even-level missing top coefficient of h^2 is handled by strict
interior rounding on the original primitive lattice. The full complex
packet, whole-color bound and marked geometric completion then give
(1) with the original source normalization. C(A_2) itself remains
excluded. \(C(A_2\mathcal R(A_2))\) is an exact passing instance with
X=1/sqrt(2); no claim of topological novelty is attached to it.

This is a general finite-tree theorem with a geometric certificate,
not an all-arborescent theorem. The exact failing tangent example
\(C(A_2\mathcal R(A_4))\) has some leaves X=1/sqrt(3). It shows that
one cannot simply omit (3a); it does not refute the desired invariant
limit. A sharper version uses the exact positive tangent-deficit
condition, whose threshold is proved in the same new argument.

**The subsequent block theorem removes both restrictions.** The
[uniform two-leaf grammar theorem](actual_arborescent_two_leaf_long_twist_volume.md)
covers EVERY fixed tree of seeds s>=2 with retained closure C(FG),
without (3a). It contracts the two leaves with their original gate and
proves an alias margin1/100 on the entire proper geometric range. The
finite rational certificate covers all slopes and every point of the
actual convex domain; closed-source stationarity gives the global gap.
Thus \(C(A_2\mathcal R(A_4))\) is now included. Exact regrouping also
supplies the isolated C(A_3) gap, so all isolated C(A_s),s>=3, are
included. C(A_2) alone remains excluded.

The earlier algebraic leaf test remains sufficient but is no longer
required for this grammar.

**The single-leaf extension now allows repeated rational-leaf additions.**
The [current composition theorem](actual_arborescent_single_leaf_long_twist_volume.md)
uses completed expressions

\[
 E::=hh\mid T(E)\mid E_1E_2\mid hE\mid Eh,                 \tag{3b}
\]

with both root children completed in the closure \(C(FG)\). Every
physical leaf automatically has \(1/2<X_\ell<1\). An exact alias
comparison with the completed child's output tangent propagates through
each single attachment, retaining the actual gate and all original
physical colors. The whole-source gaps, original nonzero packet and
primitive marked filling action give (1) for this enlarged grammar.
Any finite number and depth of these operations is allowed, with the
same independently long fixed signed-twist quantifiers. The isolated
\(C(h^s)\), \(s\ge3\), cases remain available separately.

Arbitrary root-leaf closures and independently turned bare-leaf atoms
are not automatically included. In \(C(hT(h^s))\), inner leaves can
reach exactly the quarter-index equal-modulus boundary of the inherited
transport estimate, despite strict geometric cells. The subsequent
[quarter-index theorem](actual_conway_quarter_index_color_packet.md)
extends the local packet there, and the
[general mask construction](actual_conway_general_strict_mask_geometry.md)
proves the untwisted complete geometry for all strict syntax. Whole-source
signed bounds, the corresponding marked deformation and general
presentation coverage still require proof. No theorem yet
identifies every arborescent presentation with (3b), and no claim of new
knot isotopy classes follows just from the wider syntax.

## 3. What the algebraic boundary object must retain

For composition, a polynomial relation alone is incomplete boundary
data. Retain the original boundary quantum state, an algebraic boundary
correspondence, the selected logarithmic lifts, and an absolutely
normalized pressure/action primitive. For a geometric CROSS disk module
with boundary weights L_b, the currently proved version is

\[
 q_b=\frac{\partial F}{\partial\log L_b},\qquad
 B_b=e^{2\pi i q_b},\qquad
 dF=\sum_b q_b\,d\log L_b. \tag{4}
\]

The selected phases B_b are algebraic in the boundary weights.
The integer lifts q_b and the additive constant of F are extra data.
The [algebraic boundary-curve theorem](research_cap_algebraic_boundary_curve_and_volume_period.md)
constructs these explicitly for the original one-cap exterior and
reconstructs its quantum root density from the same branch. Restoring
the original complete cap gives a unique algebraic point and an
absolutely normalized period equal to the ORIGINAL drilled hyperbolic
volume divided by 2pi. This is an actual geometric calibration, not
a claim that an arbitrary eliminated curve carries that volume.

For admissible gluing of whole original port disks, internal shared
faces s impose the lifted condition

\[
 q_{1,s}+q_{2,s}=1,\qquad B_{1,s}B_{2,s}=1, \tag{5}
\]

and the positive primitive composes by

\[
 F_{12}=\inf_{\log L_S}
       \left(F_1+F_2-\sum_{s\in S}\log L_s\right). \tag{6}
\]

At finite level the same operation is coefficient extraction at the
original face demands:

\[
 P_{12,N}=\left[\prod_{s\in S}L_s^{N-1}\right]P_{1,N}P_{2,N}. \tag{7}
\]

Shared external variables are identified, and every old internal
extraction and original coupon factor is retained. The
[boundary composition theorem](research_tangle_source_boundary_composition.md)
proves these laws and their associativity under its explicit whole-port,
anchoring and simplicity conditions. It does not identify arbitrary
Conway operations with those cuts automatically. The actual signed
four-port tangle tensor carries additional information beyond this
positive CROSS coefficient module.

A four-punctured Conway seam has boundary shape data. Its geometric
volume is obtained after matching that data and solving the shared
critical equations. One cannot replace (6) by a sum of independently
maximized piece volumes. Neither this source-boundary correspondence
nor its one-variable eliminant is called the ordinary knot A-polynomial
without the missing meridian/longitude dictionary.

## 4. The remaining closure theorem

The general extension beyond these certified grammars must establish, for each allowed
rational-tangle building block and composition:

* The literal original quantum boundary contraction, including turns,
  full repeated-root information, framing and the final knot closure.
* The selected algebraic boundary branch and primitive with correct
  integer lifts and all shared shape variables.
* A signed estimate that survives that contraction, at both level
  parities, followed by the original full filling-period argument.

The current two-cap calculation demonstrates why the last requirement
is substantive: pair-total extraction can destroy joint stability,
and completing two cap sums creates mixed tails as well as a double
tail. The [joint response theorem](research_two_cap_joint_extraction_response_bound.md)
retains those terms and gives a finite sufficient comparison.
The [even-level obstruction](research_even_cross_stability_obstruction.md)
shows that the actual local CROSS polynomial already fails real
stability at N=6; a positive comparison does not transfer its signed
negative-axis rate automatically. These findings concern the general
source extension and do not revoke the existing robust Conway proof,
which uses a different exact full-Newton estimate.

Thus the immediate target is a tangle-gluing theorem on the original
boundary data, capable of enlarging the admissible seed and rational-
edge class. The older general prescribed-plat question remains an open
presentation of the broader problem; bridge number is not used to
organize the present argument. The research goal remains ACTIVE.
