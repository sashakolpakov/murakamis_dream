# Recovering the original punctured-disk seam from its marked pants group

This note supplies a relative topological argument for the pure mixed
block. It does not require the two shaded triangles in one particular
triangulation to be carried through the recorded Pachner moves. Instead,
it straightens the original embedded twice-punctured disk and keeps its
ordered boundary curves throughout.

The relevant general geometric fact is usually attributed to Adams:
an incompressible embedded thrice-punctured sphere in a finite-volume
hyperbolic three-manifold is isotopic to a totally geodesic one. We give
the geometric argument needed here, and use a precise relative isotopy
theorem for its last topological step. Thus no unproved assertion that
an arbitrary isotopy of lifts descends is used.

## 1. The relative topology input

We use Corollary 5.5 of Waldhausen,
[On irreducible 3-manifolds which are sufficiently large](https://homepages.math.uic.edu/~kauffman/Waldhausen.pdf),
Annals of Mathematics 87 (1968), 56–88, at pp. 76–77:

> In a compact orientable irreducible three-manifold, incompressible
> surfaces homotopic relative to their boundary are ambient isotopic
> relative to the manifold boundary.

The wording here includes the conventions at the start of that paper.
The surfaces are properly embedded and two-sided. For our application
they are compact pairs of pants in a cusp truncation. This is the
surface theorem, not the later theorem about homotopic homeomorphisms;
the latter's line-bundle exceptions are not hypotheses of this result.

The argument in Sections 5.3–5.5 first finds a product between small
surface pieces, after cutting along one surface and simplifying the
homotopy's inverse images. Minimizing the number of intersection curves
forces this product to extend across both surfaces. The isotopy then
slides through that product, fixing the ambient boundary. We use this
standard topology theorem as an explicit input; the verification below
checks its boundary and incompressibility hypotheses.

## 2. Straightening the original disk

**Lemma 1.** Let \(M\) be an orientable complete finite-volume hyperbolic
three-manifold. Let \(D\) be a properly embedded thrice-punctured sphere
whose three ends lie in distinct ambient cusps and whose three
peripheral curves have nonidentity parabolic holonomy.
Assume that outside a compact cusp truncation its ends are
products of three boundary curves with the cusp height coordinate.
Suppose its based peripheral generators \(\alpha,\beta\) have different
fixed points and \(\alpha\beta\) is parabolic. Then \(D\) is
\(\pi_1\)-injective. It is properly isotopic to an embedded totally
geodesic pair of pants. The isotopy preserves the three labelled,
oriented peripheral classes and the induced primitive classes on the
ambient cusp tori.

**Proof.** Choose trace-\(2\) lifts and normalize
\[
 A=\begin{pmatrix}1&2\\0&1\end{pmatrix},\qquad
 B=\begin{pmatrix}1&0\\z&1\end{pmatrix}.
\]
Since \(AB\) is parabolic, \(2+2z=\pm2\). Distinct fixed points
exclude \(z=0\), so \(z=-2\). The two matrices preserve the vertical
plane \(P\) with ideal boundary \(\mathbb R\cup\{\infty\}\).
Their usual ideal quadrilateral, with vertices
\(-1,0,1,\infty\), is a fundamental polygon: the vertical sides
are paired by \(A\), and the circular sides by \(B\). Its
vertex cycles are parabolic. Thus
\[
                  H=\langle A,B\rangle
\]
is the faithful complete pants group, with quotient area \(2\pi\).
The map from the free group \(\pi_1(D)\) to \(H\) is an
isomorphism. In particular the inclusion of \(D\) in \(M\)
is \(\pi_1\)-injective.

The assumed product ends lie in disjoint standard cusp neighborhoods.
Its cross-section curves can be straightened on the flat cusp
tori while retaining their slopes and orientations. A lift
\(\widetilde D\) and the standard \(H\)-equivariant copy of \(P\)
then have an equivariant correspondence at uniformly bounded
hyperbolic distance. On a compact pants core this follows by
compactness of a fundamental region. On a cusp end the horizontal
difference is bounded in Euclidean coordinates and decreases in
the hyperbolic metric as the height increases.

Consequently \(\widetilde D\) extends to the same ideal circle
as \(P\). More explicitly, identify its abstract universal
cover with the complete hyperbolic pants cover. The equivariant
map differs a bounded distance from the standard embedding of
that cover into \(P\); it therefore extends continuously by the
identity on the ideal circle. Its interior is embedded and
proper, so its compactification is an embedded closed disk.

Distinct lifts of \(D\) are disjoint. Their ideal circles cannot
cross. Indeed an embedded disk with its boundary on the sphere
at infinity separates the hyperbolic ball into sides corresponding
to the two complementary ideal disks. A disjoint connected lift
lies entirely on one side; its ideal boundary cannot meet the
interiors of both complementary disks. Hence the round planes
\(gP\), for \(g\) in the ambient group \(\Gamma\), have disjoint
interiors unless they coincide.

Coincident planes do not create a multiple covering. Let \(H'\)
be the full stabilizer of \(P\) in \(\Gamma\). It is discrete and
acts freely on \(P\): any fixed point there would be an elliptic
element of the torsion-free ambient group. Since it contains the
finite-area lattice \(H\), the index \([H':H]\) is finite and
\[
            2\pi=[H':H]\operatorname{Area}(P/H').
\]
The quotient \(P/H'\) is a complete finite-area hyperbolic
surface, possibly nonorientable. Its negative Euler
characteristic is an integer, so its area is at least \(2\pi\).
It follows that \([H':H]=1\). In particular no orientation-reversing
plane stabilizer or twisted surface quotient remains.

It follows that \(P/H\) embeds in \(M\). Its three ends lie
properly in the three prescribed cusp neighborhoods, so it is
a properly embedded geodesic pants surface \(D_{\mathrm{geo}}\).

Choose the marked proper homeomorphism from the abstract pants
\(D\) to \(P/H\), preserving its three peripheral generators.
It can be constructed by cutting both pants into two labelled
ideal triangles. Its lift is the equivariant correspondence used
above. On a horosphere at one selected peripheral fixed point,
the original and target boundary lifts are parallel straight lines
with the same primitive translation. Use that translation as
their common parametrization. A Euclidean translation of the
horosphere then makes the two lifted maps agree pointwise.
This translation descends to an isotopy of the ambient flat cusp
torus. Choose the full translation vector, not just its residue
modulo the cusp lattice; this retains the based arc track and
any integral winding. The three cusps are distinct, so all three
adjustments can be performed independently and extended through
disjoint cusp collars, fixing a core basepoint.

After those ambient collar isotopies, the equivariant maps from
\(\widetilde D\) to itself and to \(P\) agree pointwise on every
lifted truncation boundary. Join corresponding points by
hyperbolic geodesics. This is an equivariant homotopy constant
on those boundaries. It descends to a homotopy of the compact
pants relative to their actual boundary curves; no embedding
assertion is made about its intermediate maps. Radial
retraction of the cusps puts its image in the compact
truncation without moving those curves.

Now truncate the cusps. The compact truncation \(\overline M\)
is orientable and irreducible, and both truncated surfaces
are incompressible and properly embedded. The homotopy just
constructed is relative to their common boundary. Waldhausen's
relative surface theorem therefore supplies an ambient isotopy
fixed on \(\partial\overline M\). Extending it by the product
on the removed cusps gives the required proper isotopy. The
initial cusp straightening was itself isotopic to the identity
on each torus, so none of the original primitive classes,
orientations, or disk framings is changed. \(\square\)

For comparison, the geometric normalization and limit-circle
argument are also presented in Jessica Purcell,
[Hyperbolic Knot Theory](https://users.monash.edu/~jpurcell/book/HypKnotTheory.pdf),
Theorem 12.1, pp. 243–244. The full-stabilizer argument and the
explicit relative isotopy input above make the two topological
steps used here separate.

## 3. The pure mixed block

Let \(M_0\) and its original oval disk \(D_0\) be those of
[the pure-carrier geometry note](research_mixed_pure_carrier_geometry.md).
The circle's spanning disk meets the main tangle in exactly two
points. After deleting the link it is an embedded thrice-punctured
sphere. Its three ordered peripheral curves are the original
puncture meridians \(l,r\), and the disk longitude \(L=rl\)
with the appropriate boundary orientation. Their complete
holonomies are nonidentity parabolics. The two puncture
meridians have different flags: otherwise (3) of that note
would make the whole complete holonomy elementary.
The compact spanning disk meets small link tubes in ordinary
collars, so attaching product cusp ends gives exactly the end
condition in Lemma 1. Its punctures lie on the two distinct
main components, while its outside boundary lies on the
auxiliary component.

Thus Lemma 1 applies directly to the original disk, not to a
surface guessed from the final tetrahedron drawing. The resulting
geodesic pants has the same based pants representation and the
same labelled, oriented boundary curves. Cut it into its two
ideal triangles using the three original pairs of punctures.
The induced maps are the original pure reference maps.
At completeness every labelled ideal triangle is determined
by its three flags. Under the marked deformation, the two
parabolic puncture holonomies and the selected auxiliary
eigenflag determine their continued ordered maps. These are
precisely the original leaf's two-triangle tables
\[
                (-Q^{-1},-Q,-Q^{-1}),\qquad
                (-Q,-Q^{-1},-Q),\qquad Q=e^{iu}.
\]
The dependence on \(Q\) is the already proved leaf calculation;
no change of outside angle or shear is made in straightening
the complete disk. Specifically, use the subsection
“The full disk-side boundary maps” and equation
\(\texttt{ctg:pants}\) in
[the circle-tree geometry paper](../papers/circle-tree-geometry/main.tex).
That table is computed from its four full white transition
matrices \(\texttt{ctg:white}\), with the incoming edge order
\((Z,\infty),(\infty,1),(1,Z)\) and outgoing edge order
\((Z,R),(R,0),(0,Z)\). Section 5, equations (13)–(14), of
[the zero-subtree geometry note](research_zero_subtree_conway_geometry.md)
spells out the same pure Legendre normalization \(Q=e^{iu}\).

This constructs the annular interface on the original topological
piece. It need not be the particular pair of triangles singled
out in one saved triangulation. Positivity of that triangulation
gives the complete metric. The isotopy above supplies the correct
cut, and the original marked geometric germ supplies the
continued face maps on a small parameter disk.

**Corollary 2.** The pure mixed boundary block is eligible for the
finite-library annular composition theorem, on one fixed
sufficiently small geometric disk. In any such composition its
outside circle retains the original primitive meridian and disk
longitude, and its carrier is inserted only once. The source
asymptotic and curvature assumptions are exactly those of the
proved mixed boundary theorem.

The corollary does not extend the quantum asymptotic theorem
to an arbitrary rational word. It permits this already proved
block to be used in the compositions whose remaining analytic
hypotheses have been established.

