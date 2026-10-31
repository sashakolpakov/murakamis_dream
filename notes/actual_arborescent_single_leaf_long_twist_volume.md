# Knot complement volume under repeated single-tangle attachments

31 October 2026. This research theorem enlarges the previously proved
two-or-more-leaf composition class by permitting a single original leaf
to be attached to either side of any completed child. The source estimate,
ordered geometry and marked peripheral deformation are retained together.
The conclusion is the hyperbolic volume of the resulting **knot complement**.
Only the auxiliary crossing-circle cusps are filled; the knot cusp stays
unfilled.

## 1. The class and quantifiers

Let \(h=T(L_N)\) be the original turned complete crossing-circle coupon,
\(T\) the literal ordered quarter-turn, and multiplication the original
stack of four-port boxes. Distinct occurrences have independent leaves
and auxiliary colors, with their original local disk framings and the
original global one-cut mark retained. Define completed expressions by

\[
 E::=hh\mid T(E)\mid E_1E_2\mid hE\mid Eh.                 \tag{1}
\]

The closed class consists of the original cylindrical closures \(C(FG)\)
with **both** \(F,G\) completed expressions in (1). Equivalently, any
\(h^s\), \(s\ge2\), may be included among the initial blocks.
Choose a fixed half-twist pattern \(\epsilon_\ell\in\{0,1,-1\}\)
whose literal endpoint pairings give a knot without closed components
inside the tangle tree. Such a pattern exists for every expression in
this class by the constructive endpoint-pairing induction.

At every auxiliary crossing circle insert an independently chosen,
fixed disk-framed full twist \(R^{-2p_\ell}\). The resulting rational
leaf is the actual tangle \(T(R^{\epsilon_\ell-2p_\ell})\).
Write \(K_{E,\epsilon}(\mathbf p)\) for the resulting knot.

**Theorem.** For each fixed finite expression and knot half-twist pattern
there is a finite threshold \(P(E,\epsilon)\) such that, for all fixed
signed integers \(p_\ell\) with \(|p_\ell|>P(E,\epsilon)\), the knot
complement is hyperbolic and

\[
 \lim_{N\to\infty}\frac{2\pi}{N}
       \log\left|K_N\bigl(K_{E,\epsilon}(\mathbf p)\bigr)\right|
  =\operatorname{Vol}\!\left(S^3\setminus
                         K_{E,\epsilon}(\mathbf p)\right).       \tag{2}
\]

The number of tangles, nesting depth, and number of single-leaf
attachments are arbitrary finite numbers. The signs and magnitudes
of the \(p_\ell\) need not agree or be comparable. The expression and
all twists are fixed before \(N\) tends to infinity, through both
parities and composite levels. No threshold uniform over all trees is
claimed.

Here \(K_N\) is the original marked invariant with the retained
enhancement. The [normalization comparison](actual_complete_augmented_source_normalization.md)
and [original crossing calculation](kashaev_crossing_and_period_lattice.md)
retain an outer unit-modulus factor in the reduced enhanced Kashaev
normalization, or the recorded single factor of modulus \(1/N\) in
the full modified one-cut normalization. Both give (2).

The previously proved isolated closures \(C(h^s)\), \(s\ge3\), are
also available from the [two-or-more-leaf theorem](actual_arborescent_two_leaf_long_twist_volume.md).
They are inherited cases, not an assertion that every root-leaf
closure \(C(hE)\) belongs to (1). The isolated \(C(hh)\) remains
excluded.

## 2. Strict geometry and the selected finite source

The [source composition proof](actual_conway_single_leaf_source_composition.md)
establishes a strict reduced state at every interior output of every
completed expression. At closure only the final forced gate is removed;
its exact coefficient is one. Its inputs satisfy \(i+j=N-1\).
The original entropy barrier and injective angle maps then give a unique
strict complete optimizer with negative definite reduced Hessian.

The [geometric composition proof](actual_conway_single_leaf_geometric_composition.md)
retains the stationary port variables

\[
 B=\cot(\pi b),\qquad X^2+Y^2-B^2=1,\qquad -Y<B<X.
\]

Both completed root children have \(0<X,Y<1\), and these bounds
propagate to all completed descendants. At a new leaf attachment,

\[
 B_p=X-\frac1{X+B},\qquad
 Y_p=\frac{Y}{X+B},\qquad X+B>0.                         \tag{3}
\]

The proper parent and child bounds imply
\(1<2X(X+B)<4X^2\). The \(hh\) base gives the same lower bound
from \(Y_p=1/(2X)<1\). Every physical leaf consequently satisfies

\[
 \frac12<X_\ell=\cot(\pi a_\ell)<1,
 \qquad \frac14<a_\ell<\frac{\arctan2}{\pi}.              \tag{4}
\]

This is automatic for (1), not an extra test of individual knots.
It supplies the strict high-index window required by the original
[signed complex packet](actual_odd_conway_complex_color_packet.md).

With \(H\) original leaves, the primitive wire lattice has dimension
\(2H-3\). Turns impose \(r\mapsto N-1-r\), and one root variable
is eliminated integrally; no constraint \(2r=N-1\) is introduced.
Strict-state rounding works at every sufficiently large level. The
\(H\) leaf factors and \(H-2\) retained gates have total prefactor
\(N^{3-H}\); the lattice Gaussian gives \(N^{(2H-3)/2}\), leaving
\(N^{3/2}\). Original integer offsets, Hermite directions and phases
remain in the nonzero leading amplitude. The changed color Hessian has
diagonal entries

\[
 -\frac{2\pi X_\ell}{1-\epsilon_\ell iX_\ell},             \tag{5}
\]

with negative real part. These facts concern the original finite source.
The global alias bounds needed to pass to the full invariant are supplied
next.

## 3. The estimate that makes a single attachment composable

At an actual attachment, let \(\mu=f_E'(b)\) be the child slope and
\(\lambda=f_{hE}'(c)\) the parent slope. Use the original leaf actions
\(g,k\), gate action \(m\), and true support tetrahedron

\[
 D=\{(x,y,z):x,y\ge0,\ \max(x,y)\le z\le x+y\le1\}.
\]

The [single-leaf alias theorem](actual_conway_single_leaf_alias_composition.md)
proves the two dual bounds

\[
 \begin{aligned}
 P(\mu,\lambda)&=\max_{D,\ x\le1/2}
           [g(x)+m(x,y,z)+\mu y-\lambda z],\\
 Q(\mu,\lambda)&=\max_D
           [k(x)+m(x,y,z)+\mu y-\lambda z],\\
 P(\mu,\lambda)-Q(\mu,\lambda)&\ge\frac1{2500}
 \quad\text{at every proper attachment.}
 \end{aligned}                                                   \tag{6}
\]

The child enters through its output tangent \(\mu y\); it is not
replaced by a bare leaf. For \(1/2<X\le2/3\), the actual slopes
lie in \([-2\log2,0]^2\). A finite rational certificate proves the
stronger gap \(1/1000\) on that entire square: 55 dyadic rectangles,
four slope corners, and the four exact vertices of \(D\) give 880
outward-rounded rational inequalities. A feasible pure state bounds
\(P\) below; a global concave tangent bounds \(Q\) above. The
[portable verifier](../experiments/verify_conway_single_leaf_attachment_certificate.py)
uses no numerical optimizer. For \(X\ge2/3\), the retained individual
leaf certificate supplies the margin \(1/2500\). A separate monotone
response argument and four-vertex endpoint certificate strengthen the
bound on the actual small-\(X\) port set; they are not needed for (6).

For every completed subtree the inductive estimate is its selected
output tangent, with zero loss for its core and positive loss for any
nonempty alias sector. The \(hh\) block supplies the base.
Turns reverse the slope. Completed/completed products add the child
tangents and the gate tangent; stationary equations cancel the internal
linear terms.

At \(hE\) the exact alias split is

\[
 A_h\star C_E+C_h\star A_E+A_h\star A_E.                  \tag{7}
\]

The three terms lose, respectively, the new margin (6), the inherited
child margin, and their sum. The kernel \(\star\) retains all original
colors, normal directions, and the constraint \(i+j\le N-1\).
The same argument applies to \(Eh\). A turn is never replaced by a
multiplicative rule.

At the completed/completed root the two output tangents cancel on the
original closing relation. The \(N-1\) shifts cost \(O(1)\) in the
exponent. A fixed tree has only polynomially many wire states and
finitely many alias sectors, so a strict whole-source alias gap follows.
The all-core concave majorant has the same unique strict optimizer;
compactness away from it and the original local far-color estimate give
the physical-color complement gap. This supplies both global hypotheses
of the [original-source filling transfer](general_original_source_long_filling_transfer.md).

## 4. Why the right-hand side is the knot complement volume

The geometry companion constructs the actual augmented-link complement
\(Y_E^\epsilon\) from the original ideal pyramids, ordered multiplication
prisms, bowtie cuts and signed shaded face pairings. A single leaf uses
its original \(\pi/2\) CAP case; a completed input uses its completed
CAP case. The completed/completed root retains the original closing
maps. The cusp decorations and pointwise edge words give the complete
metric, with absolute anchor

\[
 \operatorname{Vol}(Y_E^\epsilon)=2\pi F_0.                 \tag{8}
\]

The original marked deformation retains the primitive auxiliary logs
and absolute regulator

\[
 U_\ell=-2\pi i\chi_\ell,\qquad
 V_\ell=-2\partial_\ell\Phi_\epsilon,\qquad
 G=2\pi i\Phi_\epsilon.                                  \tag{9}
\]

The changed half-twist correction is included. The full-source transfer
gives a nonzero asymptotic with selected action

\[
 S_{\epsilon,\mathbf p}(\chi)
   =\Phi_\epsilon(\chi)+\frac{\pi i}{2}
          \sum_\ell\frac{(\chi_\ell-1)^2}{p_\ell}.         \tag{10}
\]

Its critical equations are exactly the primitive filling equations
\(U_\ell+p_\ell V_\ell=-2\pi i\). The marked geometric completion
and absolute regulator identity on this same branch give

\[
 2\pi\operatorname{Re}S_{\epsilon,\mathbf p}(\chi_*)
   =\operatorname{Vol}\!\left(S^3\setminus
                           K_{E,\epsilon}(\mathbf p)\right).
                                                               \tag{11}
\]

All auxiliary crossing circles have been filled to insert the chosen
twists. The main component becomes the knot, and its cusp is unfilled.
Thus (11) concerns its knot complement, whereas (8) concerns the
starting augmented-link complement. The nonzero full-source asymptotic
and (11) prove (2).

## 5. Scope and remaining work

The new grammar permits repeated chains \(E_{n+1}=hT(E_n)\), starting
from \(E_0=hh\), as well as arbitrary completed products and turns.
This is a wider class of literal presentations than the previous seed
grammar. Algebraic equalities between closed source scalars do not by
themselves prove tangle isotopy or novelty of a knot class.

No coverage theorem for every arborescent knot is asserted. Independently
turned bare leaves and arbitrary root-leaf closures require further work.
For example, \(C(hT(h^s))\) has a strict complete state but inner leaf
coordinates exactly \(1/4\). The two transport eigenvalues there are
distinct with equal modulus. The subsequent
[quarter-index packet theorem](actual_conway_quarter_index_color_packet.md)
extends the local selected packet through that boundary. It does not
supply the whole-source alias and physical-color estimates for those
closures. The completed-root restriction in (1) remains in force.

The generic main-meridian quantum A-operator and coverage of all desired arborescent presentations remain open. The present theorem uses the original quantum source and its marked algebraic deformation, with the specified analytic and geometric dependencies.