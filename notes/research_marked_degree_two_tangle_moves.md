# Marked tangle moves at a short vertex of degree two

Research note, 2 November 2026. The degree-two source identities have
topological counterparts, but a physical half-turn must be retained.
This note proves the local moves for arbitrary attached tangles. It
then explains their effect on the ordered circle-tree diagrams,
the remaining crossing-circle slopes, and the zero framing of a
closed knot. No rational-tangle flip invariance is assumed.

## 1. The boundary convention

Use the conventions of
[the ordered tangle-reduction paper](../papers/conway-reductions/main.tex).
The four boundary points, in diagram coordinates, are

\[
0=\text{lower left},\quad1=\text{lower right},\quad
2=\text{upper right},\quad3=\text{upper left}.
\]

The product \(FG\) puts \(F\) below \(G\). Let

\[
T(x,y,z)=(z,y,-x),\qquad
K(x,y,z)=(x,-y,-z),\qquad
\tau(x,y,z)=(-x,y,-z)=T^2(x,y,z).
\tag{1}
\]

These are actual proper rotations of a tangle ball. In particular,
\(K\) has endpoint permutation \((03)(12)\), while
\(\tau\) has permutation \((02)(13)\). A rotation carries all
closed components, marked arcs, crossing disks and ribbons in the
ball. It must not be replaced by the identity on an arbitrary
attached tangle.

Write \(R\) for the original physical crossing, with its original
sign convention. All assertions below hold with that convention:
no crossing is redefined by a quantum matrix identity.

**Proposition 1.** For every two-strand tangle \(F\), including
any closed components and any marks carried by its ball, and for
\(\sigma=1\) or \(-1\), there are isotopies relative to the
four outside endpoints

\[
T\bigl(R^\sigma T(F)\bigr)
\simeq R^{-\sigma}T\bigl(R^{-\sigma}K(F)\bigr),
\tag{2}
\]

\[
T\bigl(T(F)R^\sigma\bigr)
\simeq R^{-\sigma}T\bigl(R^{-\sigma}F\bigr).
\tag{3}
\]

At power zero the corresponding identity is simply

\[
T\bigl(R^0T(F)\bigr)=T\bigl(T(F)R^0\bigr)=\tau(F).
\tag{4}
\]

The statement is an unframed tangle isotopy, together with the
instruction to transport any supplied ribbon. A later drawing
with standard blackboard ribbons may differ from those transported
ribbons by integral framing twists. Section 5 keeps that issue
separate from the tangle and peripheral markings.

## 2. A boundary-collar proof for arbitrary tangles

Identify the four-point boundary sphere with the pillowcase

\[
\mathcal P=(\mathbb R^2/\mathbb Z^2)/(x,y)\sim(-x,-y).
\]

Its four branch points are labelled

\[
p_0=(0,0),\quad p_1=(1/2,0),\quad
p_2=(1/2,1/2),\quad p_3=(0,1/2).
\tag{5}
\]

The square bounded by the four short segments between successive
points is one projection face of the pillowcase. Its opposite
face has the reversed depth. Thus its proper symmetries identify
with the spatial rotations in (1). Their lifts may be chosen as

\[
\widetilde T(x,y)=(-y,x+1/2),\qquad
\widetilde K(x,y)=(x,y+1/2),
\]

\[
\widetilde\tau(x,y)=(x+1/2,y+1/2).
\tag{6}
\]

For example, \(\widetilde T\) sends the old labels
\(0,1,2,3\) to \(3,0,1,2\), exactly as the specified
clockwise physical turn. Its square agrees with
\(\widetilde\tau\) after the deck involution. The maps in
(6) specify more than endpoint permutations: they also specify
the boundary mapping classes.

A single bottom half-twist has an affine representative

\[
A_\sigma(x,y)=(x+\sigma y+1/2,y),\qquad\sigma=\pm1.
\tag{7}
\]

Here is a direct comparison with a supported half-twist, rather
than an inference from the permutation of branch points. For
\(\sigma=1\), replace the displacement \(y+1/2\) by a
continuous, increasing function \(h(y)\) satisfying

\[
h(y+1)=h(y)+1,\quad h(-y)=1-h(y),\quad h(0)=1/2,
\]

which is zero near \(-1/2\) and one near \(1/2\). It can
be chosen constant outside any small band about \(y=0\).
Linear interpolation between \(y+1/2\) and \(h(y)\)
gives homeomorphisms \((x,y)\mapsto(x+h_s(y),y)\).
They commute with the deck involution modulo an integer
translation, and have constant values at all four branch points
throughout the interpolation. They therefore descend to an
isotopy relative to the four points.

At its end the map is supported in the disk surrounding the
bottom pair \(p_0,p_1\). On its double-covering annulus it
twists one boundary once relative to the other, and moves the
middle two branch points through a half-turn. This is precisely
one supported bottom half-twist. Taking its inverse gives
\(A_{-1}\); the two affine inverses differ from the displayed
representatives only by an integer translation.

Extending such a boundary half-twist into an empty collar adds
one crossing below the inner tangle ball. The two possible
senses give \(R\) and its actual inverse \(R^{-1}\).
Which torus shear is named positive depends on the oriented
covering coordinates. That choice introduces no sign ambiguity
in (2): the following identity is proved for both senses, and
always reverses the same original crossing on the right.

Direct substitution gives, as maps of the pillowcase,

\[
\widetilde T A_\sigma\widetilde T
=A_{-\sigma}\widetilde T A_{-\sigma}\widetilde K.
\tag{8}
\]

For \(\sigma=1\), the two affine lifts differ by an integer
translation. For \(\sigma=-1\), one first applies the deck
involution to one lift and then an integer translation. These
are exactly the identifications in the definition of
\(\mathcal P\). In particular \(K\) in (8) is a genuine
part of the equality. Omitting it gives the wrong endpoint
permutation even before considering boundary winding.

The supported twist comparison above converts (8) into an
isotopy between the boundary maps of the two sides of (2),
relative to the marked points. Extend that isotopy across a
boundary collar. After this adjustment the two maps of the
tangle ball agree on its whole boundary. Their difference is
a homeomorphism of the ball fixing the boundary pointwise;
the Alexander isotopy contracts that difference to the identity
relative to the boundary. Applying these isotopies to the entire
inner tangle proves (2) for arbitrary \(F\), with all its
marks and components carried. No property particular to rational
tangles enters the proof.

For completeness, a top half-twist has affine representative
\(B_\sigma(x,y)=(x+\sigma y,y)\). The same direct computation
gives

\[
\widetilde T B_\sigma\widetilde T
=A_{-\sigma}\widetilde T A_{-\sigma}
\tag{9}
\]

on the pillowcase, proving (3). Equivalently, (3) follows from
(2) and the explicit twist-sliding isotopy in the companion
paper. Formula (4) is the physical double turn, so its
half-turn is retained as well.

The familiar rational-tangle flip and flype calculus provides
background for these moves; see
[Kauffman–Lambropoulou](https://arxiv.org/abs/math/0311499).
The proof above keeps the flip on an arbitrary attached tangle
instead of using flip invariance, which is a special property
of rational tangles.

## 3. Applying the moves to an ordered circle tree

Let \(v\) be a degree-two original vertex with neighbors
\(a,b\). Choose a root away from \(v\), so that \(a\)
is its parent and \(b\) its sole child. Such a root exists
because the tree has at least three vertices. Re-rooting a
closed diagram uses the actual closed turn-transfer moves in
the tangle-reduction paper, with their orders and rotations
retained.

The local word at \(v\) is one of

\[
W_v=R^{n_v}T(W_b),\qquad
W_v=T(W_b)R^{n_v}.
\tag{10}
\]

Its parent contains \(T(W_v)\) as one specified factor.
If \(n_v=\sigma=\pm1\), replace this factor by (2) or
(3), according to its literal order in (10). There are then
two new integral factors \(R^{-\sigma}\): one in the
parent stack, and one inside the turned child stack.

Collect the first with the distinguished factor \(R^{n_a}\),
and the second with \(R^{n_b}\). Each collection uses the
explicit collar isotopy

\[
R^rF\simeq\rho^r(F)R^r,
\qquad \rho(x,y,z)=(-x,-y,z),
\tag{11}
\]

or its inverse, for each intervening factor. Every factor
passed is rotated; it is not commuted unchanged. Proper
half-turns preserve the signed exponent of an integral braid.
They propagate through products and turns by

\[
\begin{aligned}
K(FG)&=K(G)K(F),& K(TF)&=T\rho(F),\\
\rho(FG)&=\rho(F)\rho(G),&\rho(TF)&=TK(F),\\
\tau(FG)&=\tau(G)\tau(F),&\tau(TF)&=T\tau(F).
\end{aligned}
\tag{12}
\]

Thus the procedure is finite and completely specifies the new
ordered expression. It deletes \(v\), joins \(a\) to
\(b\) by one tree edge, and changes the powers to

\[
n_a'=n_a-\sigma,\qquad n_b'=n_b-\sigma.
\tag{13}
\]

All other powers remain the same. The orders and physical
rotations of the attached branches are those obtained from
(2), (3), (11), and (12). Merely assigning (13) on the
unmodified abstract tree would omit part of the rule.

**Corollary 2.** Fix any ordered circle-tree knot template
and an original vertex \(v\) of degree two. Fix
\(n_v=1\) or \(-1\), with its permitted original parity.
There is a finite threshold such that every independently
sufficiently long fixed signed power at the other vertices
satisfies the original all-integer-level Kashaev volume
identity.

Indeed the displayed isotopies produce one fixed ordered
circle-tree template with one fewer vertex. Its main link
is the same knot, and its crossing powers differ from the
old remaining powers by at most one. Apply the existing
long-filling theorem to this reduced template. Increasing
its threshold by one suffices for the original powers.
The rotations in (12) are among those already retained in
the circle-tree construction. There is no restriction on
the relative sizes or signs of the remaining powers.

This corollary uses a knot isotopy, not an inference of
geometric equivalence from equality of quantum invariants.

## 4. A zero power merges two twist regions

If \(n_v=0\), formula (4) replaces \(T(W_v)\) by
\(\tau(W_b)\). This is now an ordinary factor in the
parent stack, without an intervening turn. Move the
distinguished integral factor of this rotated stack to
\(R^{n_a}\), using (11). The two powers combine to

\[
n_{ab}=n_a+n_b.
\tag{14}
\]

The physical rotation \(\tau\) reverses the child stack
order, and every branch passed by the moved integral braid
gets the rotation \(\rho^{n_b}\). Equations (12) express
the resulting diagram again as an ordered circle-tree
expression. The path \(a-v-b\) has been replaced by one
vertex carrying (14), with all its other branches in their
recorded order. If only that vertex remains, use the
original elementary closure, rather than manufacture an
empty tree.

This also is an isotopy for every assignment, including
zero sums. It preserves the knot complement after all
relevant main twists have been restored. It is not a
homeomorphism from an exterior with two unfilled neighboring
crossing-circle tori to one with only one such torus.

That distinction matters for finite exceptions. Independently
large values of \(n_a,n_b\) can have a bounded sum.
Consequently the zero move does not imply a long-filling
theorem for the original partially filled exterior solely
from longness of the remaining written powers. For every
fixed integer \(s\), the assignments
\((n_a,n_b)=(m,s-m)\) have the same merged power \(s\)
and form an infinite family. The physical ordering may
depend on the parity of \(m\), but only through the
explicit rotations in (11). Finite exceptions for reduced
assignments cannot be pulled back through this many-to-one
parameter map without further work.

## 5. Peripheral curves and framing

The isotopies above take place in the indicated tangle balls
and their empty collars. They extend by the identity through
all external attachments and the specified cylindrical
closure. When the closed main link is a knot, they give an
orientation-preserving ambient isotopy in \(S^3\), carrying
the chosen knot orientation and any marked point. Therefore
they identify its meridian and preferred longitude: the
meridian has oriented linking number one and the preferred
longitude is the null-homologous peripheral curve. They
also preserve the knot's zero framing.

For a degree-two power \(\pm1\), the other crossing circles
and their disks can be retained throughout the move. A rotated
branch carries these circles, disks and their orientations
with it. There is no deletion of an auxiliary circle in an
attached branch. The remaining power shift (13) is first
recorded in that transported disk frame.

If a neighboring original power is
\(n_w=\eta_w-2p_w\), the immediate new carrier is
\(\eta_w-\sigma\), with the same integer coefficient
\(p_w\). If one wishes to return the carrier to
\(\eta_w'\in\{-1,0,1\}\), choose it with the required
parity and put

\[
k_w=\frac{\eta_w'-\eta_w+\sigma}{2}\in\mathbb Z,
\qquad p_w'=p_w+k_w.
\tag{15}
\]

This is the ordinary transfer of full twists between a
retained carrier and its disk filling. With oriented
longitudes transported, the resulting peripheral basis
change is

\[
\lambda_w\longmapsto\lambda_w',\qquad
\mu_w\longmapsto\mu_w'+k_w\lambda_w'.
\tag{16}
\]

One can see (16) by cutting along the original twice-punctured
disk and transferring the indicated integer number of full
turns. Equivalently, it sends every original primitive
filling curve to

\[
\mu_w+p_w\lambda_w
\longmapsto
\mu_w'+(p_w+k_w)\lambda_w',
\]

which restores exactly the crossing power
\(n_w-\sigma=\eta_w'-2p_w'\). No half-longitude is
introduced. If a diagram is redrawn with reversed disk
orientation, both peripheral orientations must be
transported before applying (15); a rotation alone does
not negate a crossing exponent.

Finally distinguish the physical rotation \(K\) in (1)
from the quantum scalar
\(\kappa_N=q^{(N-1)^2/2}\). The
[exact degree-two source calculation](research_degree_two_short_reductions.md)
gives the factor \(\kappa_N^\sigma\), of modulus one,
when its algebraic representative deletes a degree-two
power \(\sigma\). That calculation retains the complete
normal data. It does not show that a physical half-turn
can be erased from an arbitrary tangle.

For the volume limit, the ambient isotopy identifies the
zero-framed invariant itself and the hyperbolic volume.
For unnormalized diagram evaluations, one must retain the
explicit unit scalar and the actual transported framing.
No formula for a writhe change is inferred from the sum of
the unoriented twist powers; the strand orientations must
also be known.

## 6. Exact reproduction of the boundary calculation

Run

```sh
python3 experiments/audit_marked_degree_two_moves.py
```

It multiplies the rational affine lifts in (6)--(9), checks
their equality modulo the torus lattice and deck involution,
and records every branch-point permutation. It also checks
that omitting \(K\), or replacing \(T^2\) by the identity,
fails the corresponding marked boundary test. These finite
calculations accompany the supported-collar and ball-isotopy
arguments above; they do not substitute an endpoint
permutation for a boundary isotopy.
