# Finitely many exceptional assignments for a two-circle template

Research consequence, 2 November 2026. This note applies the proved
terminal-filling theorem to a tree consisting of one edge. It does not
prove the finite-exception statement for arbitrary trees or Conway
templates. The frozen manuscripts are unchanged.

## 1. The knot family and the claim

Use the physical tangle conventions of the
[circle-tree geometry paper](../papers/circle-tree-geometry/main.tex).
Let \(R\) be the elementary crossing, \(T\) the prescribed quarter-turn,
and \(C\) cylindrical closure. The one-edge tree has the closure

\[
K(a,b)=C\bigl(R^aT(R^b)\bigr).
\]

Fix the original endpoint marking, disk frames, and carrier parities.
Thus \(a=\eta_1-2p_1\) and \(b=\eta_2-2p_2\), with fixed
\(\eta_1,\eta_2\in\{-1,0,1\}\) and \(p_1,p_2\in\mathbb Z\).
Restrict attention to assignments whose closure is a hyperbolic knot.
The parameters count assignments; no identification of distinct
assignments representing the same knot is made.

**Corollary.** There is a finite number \(B_*\), depending on this
fixed marked template, such that every hyperbolic knot \(K(a,b)\) with

\[
\max\{|a|,|b|\}\ge B_*
\]

satisfies the original Kashaev volume identity

\[
\lim_{N\to\infty}\frac{2\pi}{N}\log|\langle K(a,b)\rangle_N|
=\operatorname{Vol}(S^3\setminus K(a,b)).
\]

The twists are fixed before \(N\) tends to infinity, and the limit is
through all integer levels. Consequently only finitely many original
filling assignments in this two-parameter family remain untreated.
The corollary does not claim that the remaining assignments violate
the volume identity.

## 2. The three elementary powers have no hyperbolic descendants

For the zero power, \(T(R^0)\) is the cup-cap tangle, rather than the
through identity. It changes the cylindrical closure into the cap
closure:

\[
K(a,0)\simeq D(R^a).
\]

Here \(D\) denotes the cap closure. Each crossing can be pulled to an
end cap and removed as a curl. The resulting unframed knot is the
unknot. The precise cap identities and the retained components are
proved in [the tangle reduction paper](../papers/conway-reductions/closures.tex).

A quarter-turn of a single crossing gives the inverse crossing in
the original vertical frame:

\[
T(R)=R^{-1},\qquad T(R^{-1})=R.
\]

This is a local equality of the two one-crossing diagrams with their
ordered endpoints. It is also reflected by the exact turned crossing
identities \(\mathcal H_1=R^{-1}\) and \(\mathcal H_{-1}=R\) in
[the finite transform calculation](research_terminal_powers_qbinomial.md).
Therefore

\[
K(a,1)\simeq C(R^{a-1}),\qquad
K(a,-1)\simeq C(R^{a+1}).
\]

The latter closures are two-strand torus links. When they have one
component, they are unknots or torus knots and are not hyperbolic.
The elementary group argument excluding these knots is included in
the tangle reduction paper. Its closed-turn and cyclicity isotopies,
proved in [the collar calculation](../papers/conway-reductions/moves.tex),
also give

\[
C(R^aT(R^b))\simeq C(T(R^a)R^b)
                 \simeq C(R^bT(R^a)).
\]

They retain the physical rotations and crossing signs. Thus the same
conclusion holds when \(a\in\{0,1,-1\}\).

It follows that every hyperbolic knot in this family has

\[
|a|\ge2,\qquad |b|\ge2.
\]

This is a statement about the actual knot diagrams. A vanishing or
small exponential rate of a polynomial would not by itself establish
the required topological exclusion.

## 3. Closing the finitely many short-coordinate families

Let \(B_0\ge3\) be an integer threshold for the all-long theorem on
this fixed one-edge template. It proves the identity whenever both
\(|a|\ge B_0\) and \(|b|\ge B_0\), with the allowed fixed parities.

For each allowed fixed integer \(c\) with \(2\le|c|<B_0\), the
[terminal-filling theorem](research_verified_terminal_fillings_and_long_remainder.md)
applies with the first vertex fixed at \(a=c\). It supplies a finite
threshold \(B_{1,c}\) for the other power. The same theorem with the
second vertex fixed supplies \(B_{2,c}\). Both vertices are original
terminal vertices, so this use does not require a theorem about a
vertex that becomes terminal after a previous short filling.

Choose an integer

\[
B_*\ge\max\left(B_0,
 \{B_{1,c}:2\le|c|<B_0\},
 \{B_{2,c}:2\le|c|<B_0\}\right),
\]

where only the allowed parity values are included. These are finite
sets. No uniform bound for all fixed terminal powers is needed.

Suppose \(K(a,b)\) is hyperbolic and
\(\max\{|a|,|b|\}\ge B_*\). Section 2 excludes the powers \(0,\pm1\).
If both powers have magnitude at least \(B_0\), the original all-long
theorem applies. Otherwise exactly one power is in the finite range
\(2\le|c|<B_0\), while the other has magnitude at least \(B_*\).
The corresponding terminal-filling theorem applies. This proves the
corollary.

All unresolved assignments lie in the finite square
\(|a|<B_*, |b|<B_*\). The affine maps from \(p_1,p_2\) to \(a,b\) are
injective, so the corresponding set of original surgery assignments
is finite as well.

## 4. Why this does not yet extend to arbitrary trees

The later [isolated-vertex theorem](research_isolated_vertex_coverage_and_assembly.md)
now estimates every original vertex with degree \(d_v\) and fixed
power \(n_v\) satisfying \(d_v+|n_v|>2\), with all its boundary
variables retained. Its assembly theorem permits any independent
set of such fixed vertices before independently long remaining
fillings. Thus isolated internal short powers are no longer the
missing case.

Arbitrary connected sets of adjacent short fillings still need a
joint boundary estimate. Several specific connected families have
been proved, but the finite-branching argument for arbitrary templates
requires a theorem at every partial assignment it reaches. It must
also retain the original parameter fibers in zero-power and cap
reductions: a finite untreated set of reduced knots can have infinitely
many original assignments. The one-edge corollary is therefore a
completed special case of the finite-exception target, rather than
its general proof.
