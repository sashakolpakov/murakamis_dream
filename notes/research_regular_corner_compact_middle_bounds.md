# Compact middle bounds before regular one-square corners

Private written geometry, 16 November 2026.

The uniform original end tubes give elementary control of the
remaining positive metrics. After fixed end truncations, every
retained tetrahedral piece lies in a uniformly compact developed
region, including tetrahedra which flatten. Paths through the finite
original dual graph then bound the diameter in the completed metric.
At least one tetrahedron stays positive and supplies a uniform
embedded hyperbolic ball.

These are bounds on the supplied positive sequence. No metric
convergence theorem, extension across the limiting middle, or
continuation of a geometric structure is inferred.

## 1. Hypotheses and actual truncations

Use exactly the family of the
[uniform original end theorem](research_regular_corner_uniform_end_tubes.md).
In particular, the original ordered circle-tree exterior is connected
and has at least one edge. Its finite tetrahedral gluing, page maps,
carriers and primitive curves are fixed. The positive configurations
converge in regular original face charts. Every limiting edge is
positive or has one finite sharp square corner and its other square
interior; no face triple or tetrahedral vertex pair collides. At the
selected auxiliary ends,
\[
 t_v^{(j)}=s_v^{(j)}-iH_v^{(j)},\qquad
 0<H_0\le H_v^{(j)}\le H_1,\qquad
 \chi_v^{(j)}\longrightarrow\chi_v^*>0,
 \tag{1}
\]
\[
 U_v^{(j)}+p_vV_v^{(j)}=-2\pi i\chi_v^{(j)},\qquad
 V_v^{(j)}=2it_v^{(j)},\qquad 0<\chi_v^{(j)}\le1.
 \tag{2}
\]
The integers and marking are unchanged. Unselected auxiliary angles
are zero and main cusps stay complete. This is a supplied sequence;
existence or connectedness of a charge path is not an assumption
deduced here.

Let \(M_j\) be its actual positive metric with the selected axes
added by the original cone completion. The original tetrahedral
interiors embed in \(M_j\); only their prescribed faces are glued.
The tube theorem gives disjoint selected tubes of a common radius.
Choose a smaller fixed radius \(\bar R>0\), and choose disjoint
complete cusp neighborhoods with fixed height cutoffs in the
convergent translation frames of that theorem. These neighborhoods
may be made smaller once more below.

Write
\[
 K_j=M_j\setminus
 \left(\bigcup_{v\ {\rm selected}}\{R_v<\bar R\}
             \ \cup\ \bigcup_{b\ {\rm complete}}\mathcal H_{b,j}\right),
 \qquad
 C_j=M_j\setminus\bigcup_{b\ {\rm complete}}\mathcal H_{b,j},
 \tag{3}
\]
where the removed neighborhoods are open. Thus \(C_j\) adds the
closed cone tubes, including their axes, to the retained middle
\(K_j\). All distances below are measured in \(M_j\), allowing paths
to enter the removed end neighborhoods. An intrinsic path metric
on \(K_j\) is not asserted to have the same bound.

**Theorem 1.** The truncations can be chosen so that for all
sufficiently large \(j\):

1. In a continuously normalized frame for each original tetrahedron,
   its part mapping to \(K_j\) lies in a fixed compact subset of
   \(\mathbb H^3\).
2. There is \(D<\infty\), independent of \(j\), such that
   \(\operatorname{diam}_{M_j}K_j\le D\) and
   \(\operatorname{diam}_{M_j}C_j\le D+2\bar R\).
   Both \(K_j\) and \(C_j\) are compact for each \(j\).
3. There is \(r>0\), independent of \(j\), and an isometrically
   embedded hyperbolic ball of radius \(r\) contained in \(K_j\).
   In particular,
   \[
   \operatorname{Vol}(M_j)\ge
             4\pi\int_0^r\sinh^2 u\,du
             =\pi(\sinh(2r)-2r)>0.
   \tag{4}
   \]

The constants depend on the fixed original gluing and the supplied
regular limiting configuration. They are not uniform over arbitrary
graphs or over approaches to excluded two-square or collision limits.

## 2. Height bounds in every original vertex frame

Fix a tetrahedral vertex occurrence and send it to infinity by a
continuously chosen Möbius frame. The other three ideal vertices
stay in a bounded subset of \(\mathbb C\), converge, and remain
distinct. For example, send two of them to zero and one; the fourth
coordinate is finite and avoids zero and one by regularity.
The projection of the positive tetrahedron to the boundary plane
lies in the Euclidean triangle of these three vertices.

For a selected occurrence, the end theorem gives, in this frame,
a second fixed point \(q_j\) and constants
\[
 0<m\le |z-q_j|\le M<\infty
 \tag{5}
\]
on its whole link triangle. The invariant end coordinate and the
distance from the completed axis are
\[
 r_{\rm end}=\frac{y}{|z-q_j|},\qquad
 R=\operatorname{arsinh}(1/r_{\rm end}).
 \tag{6}
\]
The same theorem identifies all points with sufficiently large
\(r_{\rm end}\) with the actual punctured tube, with the original
side-face identifications. Put
\(\bar r=1/\sinh\bar R\), choosing \(\bar R\) small enough that
this identification holds whenever \(r_{\rm end}>\bar r\).
Every point of this tetrahedron lying over \(K_j\) therefore obeys
\[
              r_{\rm end}\le\bar r,\qquad y\le\bar r M .
 \tag{7}
\]
This uses the upper as well as the lower bound in (5). The fact
that the tube is contained in a high horoball by itself would not
give the height bound on its complement.

For a complete cusp occurrence, the actual neighborhood is a
horoball in a translation frame. Its complement has bounded height
there. The finitely many changes to the continuously normalized
vertex frames have bounded nonzero similarity factors. Thus it has
a uniform height bound in these frames also.

There are finitely many vertex occurrences. Consequently there
are constants \(Y_{\Delta,a}<\infty\), one for each vertex \(a\)
of each original tetrahedron \(\Delta\), such that
\[
 y_{\Delta,a}^{(j)}(x)\le Y_{\Delta,a}
 \quad\hbox{whenever }x\in\Delta_j
                     \hbox{ maps to }K_j.
 \tag{8}
\]
All these frames, ideal vertices and finite transition maps
converge. No bound is being imposed on an entire universal-cover
development.

## 3. A compactness lemma for a flattening ideal tetrahedron

**Lemma 2.** Let \(\Delta_j\) be positive ideal tetrahedra whose
four ideal vertices converge, in a fixed continuous normalization,
to four distinct ideal points. The limiting four points may be
coplanar. Suppose a subset \(A_j\subset\Delta_j\) has a uniform
upper height bound in a continuously normalized upper-half-space
frame at each of the four ideal vertices. Then all the \(A_j\),
for sufficiently large \(j\), lie in one compact subset of
\(\mathbb H^3\).

**Proof.** Work first in the Klein ball. Its closed ideal
tetrahedron is the Euclidean convex hull of its four ideal vertices.
If a sequence \(x_j\in A_j\) escapes every compact subset of
\(\mathbb H^3\), a subsequence converges to a point \(x\) on the
unit sphere. Write
\[
 x_j=\sum_{a=0}^3\lambda_{a,j}v_{a,j},\qquad
 \lambda_{a,j}\ge0,\qquad\sum_a\lambda_{a,j}=1.
 \tag{9}
\]
Taking a subsequence also makes the coefficients converge. The
strict convexity of the Euclidean ball implies that a convex
combination of distinct unit vectors lies on its boundary only
when a single coefficient is one. Hence \(x\) is one of the four
limiting vertices, say \(v_0\).

Pass to the continuously normalized frame sending \(v_{0,j}\)
to infinity. The images of \(x_j\) tend to the ideal point
infinity. Their horizontal coordinates stay in the bounded link
triangles of the other three vertices. Their heights are bounded
above by hypothesis. This is impossible: in upper half-space a
sequence with bounded horizontal coordinates and bounded heights
cannot approach ideal infinity. If its height tends to zero, its
ideal limit instead has a finite horizontal coordinate.
The contradiction proves the lemma. \(\square\)

Apply Lemma 2 to (8). This proves assertion 1 of Theorem 1.
It also proves that each retained tetrahedral piece is compact:
it is a closed subset of the ideal tetrahedron away from its
ideal vertices, and it lies in a compact developed region.
The quotient of their finite union is \(K_j\), so \(K_j\) is
compact. A closed cone tube of radius \(\bar R\) is compact
because its period lattice has rank two and its axis is a circle.
Thus \(C_j\) is compact as well.

The argument does not estimate the circumradius of a flattening
face. Such a radius can diverge. Only distinct ideal vertices,
bounded link projections, and the actual end cutoffs are used.

## 4. Paths through the fixed dual graph

For each original face choose its intrinsic ideal-triangle incenter.
Every face triple remains distinct. Therefore these points vary
continuously and stay in compact developed subsets in the frames
of each incident tetrahedron. The original face isometry identifies
the two choices, since the incenter is intrinsic.

The finite dual graph of the original tetrahedral gluing is
connected. This follows also directly from connectedness of the
original exterior: a path between two tetrahedral interiors can
be perturbed away from its codimension-two skeleton and crosses
only a finite sequence of faces. Fix simple dual paths once and
for all.

For each tetrahedron enlarge the compact region from Lemma 2 to
contain its finitely many face incenters. There is a common
\(D_0<\infty\) bounding the hyperbolic distance between any two
points in each of these enlarged regions, for all sufficiently
large \(j\). A positive ideal tetrahedron is geodesically convex.
Thus two such points can be joined inside that tetrahedron by
the ambient hyperbolic geodesic, of length at most \(D_0\).
That geodesic may enter a truncated end; this is allowed in the
metric convention of (3).

Let \(T\) be the number of original tetrahedra. Given two points
of \(K_j\), join them to the successive shared face incenters
along a simple dual path. The path uses at most \(T\)
tetrahedra. The resulting piecewise geodesic is a path in the
actual glued metric of length at most
\[
                                D=T D_0 .
 \tag{10}
\]
No global injectivity of the developing map is used: the path is
built in individual cells and joined by their actual face maps.
This proves the asserted bound for \(K_j\).

Every point of an added selected tube can be joined to its boundary
by a radial segment of length at most \(\bar R\), including points
on the axis. This follows from the exact metric
\[
 dR^2+\cosh^2R\,dX^2+\sinh^2R\,d\theta^2 .
 \tag{11}
\]
Joining two such radial segments to a path from (10) proves the
bound \(D+2\bar R\) for \(C_j\).

## 5. A surviving actual hyperbolic ball

At least one limiting tetrahedron is strictly positive. Indeed
there is an original edge, and a one-square corner leaves four
of its eight tetrahedra positive; a positive edge leaves all
eight positive. Fix such a tetrahedron \(\Delta_j\), and normalize
its limiting positive tetrahedron \(\Delta_*\) continuously.
Choose a point \(o\) in the interior of \(\Delta_*\).
There is \(r>0\) such that the closed ball
\[
                       \overline B_{\mathbb H^3}(o,4r)
                                      \subset\operatorname{int}\Delta_j
 \tag{12}
\]
for all sufficiently large \(j\). This follows from convergence
of the four geodesic face planes and the positive distance of
\(o\) from them.

Shrink the selected tubes and the complete cusp neighborhoods,
once and uniformly, so that these balls avoid all end neighborhoods.
This is legitimate in the frames already used: on the fixed compact
ball all complete-cusp heights are bounded; at selected occurrences
(5) bounds \(r_{\rm end}\). Increasing their cutoff heights and
\(\bar r\), respectively, excludes the ball. The already proved
compactness and diameter arguments apply to these new fixed
cutoffs, with possibly larger constants.

The image of \(B(o,r)\) is an isometrically embedded ball in
the actual metric. The interior of an original tetrahedron is
not identified to itself by the gluing. A path starting in this
ball and leaving \(\Delta_j\) must first travel to one of its
faces. By (12) that costs at least \(3r\). In particular a path
between two points of \(B(o,r)\) that leaves the tetrahedron
has length at least \(6r\), whereas their ambient geodesic has
length at most \(2r\) and stays in \(\Delta_j\).
No outside shortcut can shorten their distance. Likewise every
point within metric distance \(r\) of \(o\) is reached before any
face is crossed. Thus the ordinary radius-\(r\) ball is precisely
the metric ball there, and it is contained in \(K_j\).
The hyperbolic polar-coordinate volume formula gives (4).
This completes Theorem 1.

## 6. What has and has not been established

The proof supplies finite, explicit types of controls: height
cutoffs in every original vertex frame, compact developed retained
pieces, a dual-path diameter estimate, and a positive-volume ball.
It works when several edges have regular one-square limits.
It does not require an embedded development of an entire
projection block or of the whole exterior.

No limit of the compact-middle metric is constructed here. In
particular the uniform bounds do not themselves identify a marked
geometric limit, exclude new identifications or collapses of
two-dimensional strata, supply a positive replacement of flat
cells, or continue the filled metric through the corner. Such
claims need a separate proof. The result also makes no assertion
about an original quantum cycle or its asymptotic coefficient.

## Direct sources and author readback

- [Uniform original end tubes](research_regular_corner_uniform_end_tubes.md):
  all hypotheses, uniform second-point separation, actual invariant
  tube cutoffs and complete cusp frames. SHA256
  904cc289bb829e4a737064e412fc18adb5e95818cc6590219643a7e373460e81.
- [Pointwise marked completion](research_positive_point_marked_completion.md):
  Sections 3--6, the original gluing metric, embedded tetrahedral
  interiors, full primitive periods and completed selected ends.
  SHA256
  28de22f081e24629ea6d26ad05213301a9bcf5d17d3ae7d00cc9c675a8218887.
- [Original cone completion](actual_all_circle_geometric_completion.md):
  Sections 3--5, the original nonsingular finite metric and exact
  cone-tube line element. SHA256
  cc58cc7c7a133eb69295d9a447aa39568a3656a2a18a2bd8335eecda314efae9.
- [Finite square corners](research_square_corner_flat_geometry.md):
  Sections 1--3, distinct ideal vertices and four surviving positive
  tetrahedra at a regular one-square corner. SHA256
  511c2c93d61482664cf62ed3b146c0af19ffbb149fa8772a4d1eb5ca7026eed0.

Only written mathematics and source-text/hash inspection are used.
No mathematical program, numerical computation, test or compilation
was run. The entire final proof was reread by the author. The end-tube
and both completion sources were reread in full in this sequence;
the earlier complete square-corner read was retained at its unchanged
hash and the used classification reread. All four source hashes were
rechecked. Independent peer/root review is required before adoption.
