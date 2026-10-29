# The geometric volume of the literal augmented pretzel source

29 October 2026. The link underlying the original \(s\)-box source
\(B_i=R^{-1}L_N\), for odd \(s\geq3\), is a half-twist partner of
the untwisted fully augmented pretzel link. It has \(s+1\) components,
not one. Both complements have the volume

\[
 \boxed{\displaystyle V_s=8s\left[
 \Lambda\left(\frac\pi4+\frac\pi{2s}\right)
 +\Lambda\left(\frac\pi4-\frac\pi{2s}\right)\right].} \tag{1}
\]

Here is an explicit face-labeled geometric construction and a direct
volume calculation. No quantum invariant is changed. In particular,
volume invariance of the half-twist partners does NOT permit deleting
the retained half twists from their original quantum source.

## 1. A right-angled ideal antiprism constructed explicitly

Put \(\alpha=\pi/s\), \(h=\tan(\alpha/2)\), and
\(r=\sqrt{1-h^2}\). In the ideal boundary of the Klein ball take

\[
 A_k=(r\cos(2k\alpha),r\sin(2k\alpha),h),
 \quad B_k=(r\cos((2k+1)\alpha),r\sin((2k+1)\alpha),-h).
\]

Their convex hull is the \(s\)-antiprism \(\mathcal A_s\): two
\(s\)-gonal faces and the \(2s\) staggered side triangles.
For example the side face \((A_0,A_1,B_0)\), in coordinates rotated
by \(\alpha\), has supporting plane

\[
 X+bZ=c,\qquad
 b=\frac{r(1-\cos\alpha)}{2h},\quad
 c=\frac{r(1+\cos\alpha)}2.
\]

Its spacelike Lorentz normal is \((c,\cos\alpha,\sin\alpha,b)\).
The top face normal is \((h,0,0,1)\). Their Lorentz product is
\(b-hc=0\), exactly because
\(h^2=(1-\cos\alpha)/(1+\cos\alpha)\). The adjacent lower side
face has normal \((c,1,0,-b)\); its product with the upper normal is
\(\cos\alpha-b^2-c^2=0\). Rotations and the top/bottom symmetry
give every other edge. Thus ALL dihedral angles are \(\pi/2\).
All vertices are distinct and ideal, all the face planes are supporting,
and their normals are spacelike. This constructs the metric directly.

## 2. The actual projection polyhedra are DOUBLES of antiprisms

Double \(\mathcal A_s\) across one of its \(s\)-gonal faces. The
adjacent triangle pairs become coplanar and merge to quadrilaterals.
The resulting ideal right-angled polyhedron \(\mathcal P_s\) has
vertices

\[
 Z_k,\ U_k^+,\ U_k^-,\qquad k\in\mathbb Z/s,
\]

and the following face cycles:

\[
 W_+=(U_{s-1}^+,\ldots,U_0^+),\quad
 W_-=(U_0^-,\ldots,U_{s-1}^-),
\]
\[
 Q_k=(Z_k,U_k^+,Z_{k+1},U_k^-),
\quad T_k^+=(Z_k,U_{k-1}^+,U_k^+),\quad
 T_k^-=(Z_k,U_k^-,U_{k-1}^-).                         \tag{2}
\]

The white faces are \(W_\pm,Q_k\), the shaded faces are \(T_k^\pm\).
There are \(3s\) ideal vertices, \(6s\) edges, \(s\) white quads,
two white \(s\)-gons and \(2s\) shaded triangles. Every edge separates
a white and a shaded face.

This is exactly the topological projection-plane cut of the untwisted
pretzel port graph in
[the original source theorem](actual_odd_pretzel_augmented_transfer_source.md).
The \(k\)-th crossing disk meets the adjacent planar arcs labeled
\(U_{k-1},U_k\); flattening its two sides gives the bowtie
\(T_k^+,T_k^-\) with common ideal crossing-circle vertex \(Z_k\).
Between consecutive disks, the planar arc gives the quad \(Q_k\).
The two remaining planar regions follow the cycles \(W_+,W_-\).
Thus cutting the two complementary balls along the crossing disks
gives TWO copies \(\mathcal P_s^{(0)},\mathcal P_s^{(1)}\), with
the displayed face identifications. This is a labeled cellulation of
the literal link complement, not just a match of its cusp count.

In the untwisted graph, white faces glue across the two copies by
their labels, while each \(T_k^+\) glues to \(T_k^-\) WITHIN its own
copy, fixing \(Z_k\) and matching each outer index to itself.
Restoring a half twist changes that shaded gluing to

\[
 T_k^+\subset\mathcal P_s^{(\epsilon)}
   \longleftrightarrow T_k^-\subset\mathcal P_s^{(1-\epsilon)},
 \quad Z_k\mapsto Z_k,\quad
 U_{k-1}^+\mapsto U_k^-,\quad U_k^+\mapsto U_{k-1}^- . \tag{3}
\]

The CROSS-COPY change in (3) is necessary: swapping the two outer
labels inside the same oriented copy would give the wrong boundary
orientation. Equation (3) is the actual exchange of the two punctures
of the crossing disk. It realizes the retained odd half twist of
\(R^{-1}L_N\); its sign affects the peripheral marking, not this metric
volume. The ordinary circle is not filled or removed.

Every edge cycle has FOUR right angles under either choice, including
mixed choices at different disks. Symmetric small horospheres can be
chosen at the two vertex orbits \(Z\) and \(U\). The white isometries
preserve them. The two outer vertices of each shaded triangle have
equal decorations by its reflection symmetry, so BOTH the untwisted
and half-twisted shaded identifications preserve them. Thus the cusp
rectangles glue without dilation to compact flat tori. This verifies
completeness as well as the \(2\pi\) edge equations.

The untwisted link has \(s\) planar main components and \(s\) crossing
circles. With every half twist restored, following the main strands
advances their labels by two modulo \(s\); for odd \(s\) these form
one main component. The literal quantum base therefore has \(s+1\)
cusps. It is an AUGMENTED LINK base, not the filled pretzel knot.

We have constructed the same complete finite-volume metric from two
copies of \(\mathcal P_s\), hence FOUR copies of \(\mathcal A_s\),
for all these half-twist partners. No hyperbolic Dehn filling is
used in this equality.

## 3. Direct volume of one antiprism

Send the north ideal point to \(\infty\) in upper half-space by
stereographic coordinates. For
\(t=\tan(\pi/4-\alpha/2)\) and \(\rho=t^{-1/2}\), the vertices are

\[
 a_k=\rho e^{2ik\alpha},\qquad
 b_k=\rho^{-1}e^{(2k+1)i\alpha}.
\]

Cone the oriented boundary faces to \(\infty\), triangulating the two
base polygons in matching fans. This is the ordinary signed pyramid
volume identity, obtainable first with a finite cone point and then
by taking its ideal limit. The two base-cone volumes cancel: the
similarity \(z\mapsto\rho^{-2}e^{i\alpha}z\) takes one fan to the
other, fixes \(\infty\), and their boundary orientations are opposite.
No assertion that all these outside cones form a disjoint triangulation
is needed.

Each side pair gives the two oriented ideal tetrahedron shapes

\[
 z_+=\tfrac12+\tfrac i2 t,\qquad
 z_-=\tfrac12-\frac i{2t},
\]

with net volume \(D(z_+)-D(z_-)\). Put
\(\beta_\pm=\pi/4\pm\alpha/2\). Their Euclidean triangle angles
give

\[
 D(z_+)=2\Lambda(\beta_-)-\Lambda(2\beta_-)
                                            =2\Lambda(\beta_+),
\]
\[
 -D(z_-)=2\Lambda(\beta_+)-\Lambda(2\beta_+)
                                            =2\Lambda(\beta_-).
\]

The last equalities follow by differentiating the elementary
Lobachevsky duplication identity and fixing its value at zero.
Summing over the \(s\) side pairs proves

\[
 \operatorname{Vol}(\mathcal A_s)
 =2s[\Lambda(\beta_+)+\Lambda(\beta_-)],
\]

and multiplying by four proves (1). At \(s=3\), the explicitly
constructed antiprism is a regular ideal octahedron, so
\(V_3=4v_8\), not \(2v_8\).

## 4. Coverage and exact quantum scope

For coverage only, Kellerhals's
[abstract, introduction and Theorem C](https://homeweb.unifr.ch/kellerha/pub/Kellerhals-FAL.pdf)
identify the untwisted pretzel FAL with the \(2s\)-chain-link family,
state the four-antiprism decomposition, and state the same volume
formula. The derivation above is independent of that paper's proof.
The [Meyer--Millichap--Trapp abstract](https://nyjm.albany.edu/j/2020/26-8.html)
also records the study of fully augmented pretzel link complements.
No literature volume-conjecture proof is being used.

Equation (1) is the genuine geometric right side for the unfilled
source \(B_i=R^{-1}L_N\). It does not prove its quantum asymptotics,
nonzero geometric coefficient, or the analogous assertion for its
fixed-slope fillings. All retained half-twist phases, the original
marked cut and the full peripheral line remain in the source theorem;
they have not been replaced by the untwisted invariant.

[Audit](../experiments/audit_actual_augmented_pretzel_geometric_volume.py)
checks the normals/supporting planes, all labeled face pairings and
edge cycles, cusp links and original half-twist component counts,
and the independent ideal-tetrahedron volume calculation.
