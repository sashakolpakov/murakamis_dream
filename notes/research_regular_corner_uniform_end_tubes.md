# Uniform original end tubes at regular one-square corners

Private written geometry, 16 November 2026.

The original end completion has a uniform form along a positive
approach to regular one-square corners. The essential additional
calculation is at the similarity links: the second peripheral fixed
point stays away from every collapsed link triangle. The logarithmic
link therefore has a continuous, marked limit. A direct height bound
then places a fixed-radius cone tube inside each original end.

This concerns the actual ends and their original primitive periods.
It does not extend a metric across the compact middle at the corner,
construct an ideal-cell replacement there, or transport a quantum
source to a new subdivision.

## 1. The family and the conclusion

Fix a finite original ordered circle-tree exterior with at least one
edge. Retain its projection copies, page orders, physical seam maps,
half-twist carriers, and primitive peripheral curves. Let
\(\mathbf t^{(j)}\) be positive original configurations converging to
\(\mathbf t^*\). At every selected auxiliary vertex \(v\), suppose
\[
 t_v^{(j)}=s_v^{(j)}-iH_v^{(j)},\qquad
 0<H_0\le H_v^{(j)}\le H_1,\qquad
 \chi_v^{(j)}\longrightarrow\chi_v^*>0,
 \tag{1}
\]
and impose the actual full-period equation
\[
 U_v^{(j)}+p_vV_v^{(j)}=-2\pi i\chi_v^{(j)},\qquad
 V_v^{(j)}=2it_v^{(j)},\qquad 0<\chi_v^{(j)}\le1.
 \tag{2}
\]
The integers \(p_v\), carriers, and hence powers
\(n_v=\eta_v-2p_v\), are fixed. All unselected auxiliary angles
are zero. The main cusps remain unfilled.

Assume the limiting original face charts are regular: every ideal
face triple remains distinct, all face-map denominators remain
nonzero, and the limit of each edge block is either positive or a
finite sharp one-square corner with the other square interior.
There are no two-square corners or collapsed ideal vertices.
Finitely many edges may have one-square corners. Their incident
page maps remain the original regular maps; a positive neighboring
page is not required.

The hypotheses concern a supplied positive family. No existence or
connectedness of a radial charge path is inferred. The adopted
radial compactness theorem supplies (1) along positive radial
approaches away from charge zero when their limits satisfy the
regularity just stipulated.

**Theorem 1.** There is \(R_0>0\), independent of sufficiently large
\(j\), such that the actual selected end at every \(v\) contains an
embedded punctured cone tube \(0<R<R_0\). Its metric and original
marked periods are
\[
 \begin{split}
 ds^2&=dR^2+\cosh^2R\,dX^2+\sinh^2R\,d\theta^2,\\
 \mu_v+p_v\lambda_v&:(X,\theta)\mapsto
                  (X,\theta-2\pi\chi_v^{(j)}),\\
 \lambda_v&:(X,\theta)\mapsto
             (X+2H_v^{(j)},\theta+2s_v^{(j)}).
 \end{split}
 \tag{3}
\]
These tubes can be chosen pairwise disjoint and disjoint from
uniform horoball neighborhoods of the main and unselected auxiliary
cusps. Adding the axis gives the same marked cone solid torus as
the original positive completion.

After identifying period lattices by convergent real-linear maps,
the logarithmic link diffeomorphisms have a uniform continuous limit
of degree one. Every fiber of this limit is cellular. Its quotient
is the flat torus with periods (3), retaining the marking. This
constructs the limiting end model as a quotient of the limiting
link; it does not assert that the quotient extends over the compact
middle.

## 2. The other fixed points in the actual corner chart

Use the angular source coordinates with plus apices \(Z,W_+\),
minus apices \(Z/E,W_-\), and equator \((0,\infty,1,R)\).
The ordered shape lists are
\[
 (A,B,-1/A,-1/B),\qquad(C,D,-1/C,-1/D).
 \tag{4}
\]
First take a \(P\)-corner. Its exact relations give
\[
 b=B\in\mathbb R\setminus\{0,1,-1\},\qquad D\in\mathbb H,
 \qquad C=\frac{1+b}{1-b},\qquad A=\frac{D-1}{D+1}.
 \tag{5}
\]
These are precisely the finite regular-corner exclusions. There is
no assumption \(b>0\).

Normalize by the original incoming base:
\[
 h(z)=\frac{z-1}{Z-1},\qquad L=bD,\qquad p=1-L,
 \tag{6}
\]
and put
\[
 u=\frac{(1-b)D+b+1}{2},\qquad
 v=\frac{2bD}{(b+1)D+b-1}.
 \tag{7}
\]
The plus apices are \(1,b\), and its equator is
\((u,\infty,0,v)\). These are the same rational identities used
for the ordered edge stars, now without \(b>0\). In particular
\[
 u=-\frac1{Z-1},\qquad E=\frac{u-p}{u},\qquad
 R=\frac{u-v}{u}.
 \tag{8}
\]

The longitude \(W_2^{-1}W_0\) at \(Z\) fixes exactly the roots of
\[
                        z^2-(1+E)z+ER=0.
 \tag{9}
\]
Indeed \(W_0z=W_2z\), with the literal white maps, reduces to
(9). Its roots are \(Z\) and \(Z_*=1+E-Z\); in the normalized
chart they are
\[
                              1,\quad -L.
 \tag{10}
\]
The second endpoint uses the actual turn-and-closing map
\(w=Rz/(z-R_1)\), \(R_1=1-R\), not the turn alone.
Substituting the roots of \(z^2-(1+E)z+ER_1=0\) shows that its
plus fixed points solve
\[
                         w^2-(1-E)w-ER=0.
 \tag{11}
\]
One is \(W_+\), whose normalized value is \(b\). The normalized
sum is \(u(1+E)=2u-p=b+D\), so its fixed points are
\[
                              b,\quad D.
 \tag{12}
\]

Transport the whole minus octahedron by the actual white inverse
\(W_0^{-1}(z)=Ez\), before applying \(h\). Its apices and
corresponding second fixed points are
\[
                       (1,-L),\qquad(p+b,p+D).
 \tag{13}
\]
For the second pair the untransported minus roots solve
\[
                          Ew^2-(E-1)w-R=0.
 \tag{14}
\]
Their transported normalized sum is \(u(3-E)=2u+p\); the first
apex is \(p+b\), giving \(p+D\). The transported equator is
\[
                            (u,\infty,p,p+Ev).
 \tag{15}
\]
These calculations use only the original white and turn-and-closing
maps. Pure or odd page attachments transport both members of a
fixed-point pair by the same original Möbius map.

## 3. Separation from every collapsed link triangle

The link of an ideal tetrahedron at an apex is a Euclidean triangle
after that apex is sent to infinity. At a flat limit the second
fixed point belongs to its containing line exactly when, before
normalization, it belongs to the tetrahedron's circumcircle.
Excluding the circle is stronger than excluding the collapsed
segment.

**Lemma 2.** At every corner in (5), both auxiliary second fixed
points are outside the circumcircle of every flat tetrahedron
incident to their selected apex.

**Proof.** There are two flat tetrahedra in each projection copy.
The following are real Möbius tests in \(D\in\mathbb H\). Such
a function with nonzero determinant cannot be real at \(D\).

In the plus copy the flat \(B\)-tetrahedron has vertices
\(\{1,b,0,\infty\}\). Its circle is the extended real line,
and both \(-bD,D\) are nonreal.

The other flat plus tetrahedron has vertices \(\{1,b,u,v\}\).
The map \(k(z)=(z-b)/(z-1)\) sends its circle to the line
through zero in the direction
\[
 k(u)=\frac{D+1}{D-1},\qquad k(v)=-b\,k(u).
 \tag{16}
\]
The two tests are
\[
 \frac{k(-bD)}{k(u)}=\frac{b(D-1)}{bD+1},\qquad
 \frac{k(D)}{k(u)}=\frac{D-b}{D+1}.
 \tag{17}
\]
Their determinants are \(b(b+1)\) and \(b+1\), both nonzero.

In the transported minus copy the flat \(C\)-tetrahedron has
vertices \(\{1,p+b,u,\infty\}\). Its circle is
\[
                              1+(D-1)\mathbb R,
 \tag{18}
\]
since \(p+b-1=-b(D-1)\) and \(u-1=(1-b)(D-1)/2\).
The two second-point ratios are
\[
 \frac{-bD-1}{D-1}=-b-\frac{b+1}{D-1},\qquad
 \frac{p+D-1}{D-1}=\frac{(1-b)D}{D-1}.
 \tag{19}
\]
They are nonreal since \(b\ne-1,1\).

The other flat minus circle has vertices
\(\{1,p+b,p,p+Ev\}\). Translate by \(-p\); it is the
circle through \(L,b,0\), and the second points become \(-1,D\).
The cross-ratio tests are
\[
 [0,b,L,-1]=\frac{(b+1)D}{D-1},\qquad
 [0,b,L,D]=\frac{D-b}{D-1}.
 \tag{20}
\]
They are nonreal since \(b\ne-1,1\). All denominators in these
tests are nonzero under (5).

A \(Q\)-corner is the same calculation with the original endpoints
interchanged. Directly from the rational shape formulas, the
new ordered shapes are
\[
                   (A',B',C',D')=(-1/B,-1/A,-1/D,-1/C).
 \tag{21}
\]
For example, with endpoint tangents \(a_0,b_0\) and
\(q^2=1+a_0^2+b_0^2\), the original formulas give
\(A'=(q+b_0)/(a_0-i)=(a_0+i)/(q-b_0)=-1/B\).
The other three identities follow from the same two factorizations
\((q\pm a_0)(q\mp a_0)=1+b_0^2\) and
\((q\pm b_0)(q\mp b_0)=1+a_0^2\).
They satisfy (5) for the new \(P\)-corner. This exchanges the
actual endpoint frames; it changes no primitive curve.
Circumcircle incidence is Möbius invariant, and both endpoints
have been checked. \(\square\)

## 4. Uniform logarithmic links

For each positive member the original completion proof gives a
nonsingular similarity link at a selected cusp. Send its selected
flag to infinity. Its peripheral group fixes a second point
\(q_v^{(j)}\). The longitude has modulus \(e^{2H_v^{(j)}}>1\),
so this point varies continuously and remains finite in regular
frames. The similarity development misses it. The original map
\[
       f_v^{(j)}=\log(\operatorname{dev}_v^{(j)}-q_v^{(j)})
 \tag{22}
\]
is a diffeomorphism from the simply connected link cover to
\(\mathbb C\), with periods
\[
 \Lambda_v^{(j)}
   =\mathbb Z(-2\pi i\chi_v^{(j)})
                    +\mathbb Z(2H_v^{(j)}+2is_v^{(j)}).
 \tag{23}
\]
These assertions use positivity before the limit. The pointwise
completion proof fixes its full periods by a positive tangent
contraction, without requiring filling equations along the
contraction. Replacing its final unit charge by \(\chi_v^{(j)}>0\)
gives (23).

Fix a finite triangulated fundamental link polygon and its original
transition words. The Euclidean vertex coordinates of its developed
triangles converge by regularity of the face charts. On fixed
abstract triangles use affine barycentric coordinates. The maps
converge uniformly, including triangles which flatten.

The limiting development misses the limiting second fixed point.
Flat triangles are covered by Lemma 2. If the point were in the
interior of a positive triangle, or on an edge or vertex whose
incident triangles remain positive, the limiting local development
would still cover a neighborhood of that point. Nearby positive
members would then also contain their second fixed point, a
contradiction. Edges and vertices incident to a flat triangle have
already been excluded by Lemma 2. At positive-only vertices the
original angle \(2\pi\) and identity return persist; the usual
positive finite fan gives the local neighborhood.
Equivalently, a small boundary polygon there has winding number one
around the limiting point; this winding persists for the nearby
point and maps. Thus the neighborhood assertion remains valid for
the piecewise affine triangle parameterizations.

There are consequently uniform constants on each of the finitely
many developed triangles,
\[
                0<m\le |z-q_v^{(j)}|\le M<\infty .
 \tag{24}
\]
The finitely many changes between these regular triangle frames
have bounded, uniformly nonzero similarity factors. This is the
meaning of (24), rather than a boundedness assertion on an entire
universal-cover development.

Fix a logarithm at one basepoint continuously. Avoidance (24),
the finite face words, and (23) give uniform convergence of
logarithmic maps on the fundamental polygon. The limiting period
lattice has covolume
\[
                             4\pi\chi_v^*H_v^*>0.
 \tag{25}
\]
Identify the ordered period bases with their limits by real-linear
maps tending to the identity. This gives homeomorphisms from the
fixed marked torus to a fixed flat torus, converging uniformly to
a continuous map \(f_v^*\).

Here is the needed elementary topological fact. A uniform limit
\(f\) of homeomorphisms between these compact tori is onto: take
a convergent subsequence of the preimages of a target point \(y\).
Put \(K=f^{-1}(y)\), and let \(U\) be any neighborhood of \(K\).
A sufficiently small closed target disk of radius \(2\delta\) has
limiting preimage contained in \(U\). For a sufficiently late
homeomorphism, the preimage of the closed disk of radius \(\delta\)
is a closed disk, contains \(K\) in its interior, and lies in \(U\).
Choosing these disks successively proves that every fiber is
cellular. Uniform closeness gives a homotopy to each sufficiently
late map, so degree one and the marking persist. The
compact-to-Hausdorff quotient by these fibers is precisely the
limiting flat torus. This proves the link assertions of Theorem 1.

## 5. A uniform original epigraph, not a circumradius estimate

Take an original positive tetrahedron in an upper-half-space frame
whose relevant ideal vertex is infinity. Let its other vertices be
\(z_1,z_2,z_3\in\mathbb C\). Over its Euclidean link triangle write
\[
            z=\sum_i\alpha_i z_i,\qquad
            \alpha_i\ge0,\quad\sum_i\alpha_i=1.
 \tag{26}
\]
If the opposite face is the hemisphere of center \(c\) and radius
\(r_c\), then
\[
 \begin{split}
 r_c^2-|z-c|^2
   &=\sum_i\alpha_i|z_i|^2-|z|^2\\
   &=\frac12\sum_{i,k}\alpha_i\alpha_k|z_i-z_k|^2
        \le\operatorname{diam}\{z_1,z_2,z_3\}^2.
 \end{split}
 \tag{27}
\]
The first equality uses \(|z_i-c|^2=r_c^2\); the right side
does not contain the circumradius. The tetrahedron is the region
over this triangle above the opposite face, between its three
vertical side planes. Thus every ray
\[
             z\in\operatorname{conv}\{z_1,z_2,z_3\},\qquad y>Y
 \tag{28}
\]
lies in that tetrahedron if \(Y\) exceeds its link diameter.
The finitely many regular triangle charts have uniformly bounded
diameters. One \(Y\) therefore works along the positive approach,
even when a triangle becomes thin and its circumradius diverges.

Increase \(Y\) so that tails for different ideal vertices are
disjoint inside every original tetrahedron. This is uniform as
well. Between two distinct ideal-vertex frames the boundary map is
\[
                  z\longmapsto\frac{\alpha}{z-z_0}+\beta,
                              \qquad\alpha\ne0,
 \tag{29}
\]
and its hyperbolic extension sends the height to
\[
               y'=\frac{|\alpha|y}{|z-z_0|^2+y^2}
                              \le\frac{|\alpha|}{y}.
 \tag{30}
\]
The coefficients \(|\alpha|\) are bounded for the finite regular
family of frame changes. Taking \(Y^2\) above this bound makes
\(y>Y\) and \(y'>Y\) incompatible. This uses only finitely
many original tetrahedral vertex occurrences. Individual
horospheres need not be peripheral-invariant; the compatible end
subsets below are defined by invariant coordinates.

Translate a selected second fixed point to zero. By (24),
\(|z|\ge m\) on each of its link triangles. Consequently
\[
                         r=\frac{y}{|z|}>\frac{Y}{m}
 \tag{31}
\]
implies (28). The coordinate \(r\), and the subset (31), are
invariant under the actual peripheral similarities. Original
side-face maps identify the vertical rays with their exact
similarity factors. These subsets therefore join over the whole
link, not merely within individual tetrahedra.

For each positive member, (22) is a link diffeomorphism. Its full
ray bundle is the actual original end; (31) is a genuine embedded
sub-end. The combinatorial end neighborhoods for different vertices
are disjoint by (30). Global injectivity of the exterior's
developing map is unnecessary.

Put
\[
 R=\operatorname{arsinh}(1/r),\qquad
 \theta=\Im f_v^{(j)},\qquad
 X=\Re f_v^{(j)}+\tfrac12\log(1+r^2).
 \tag{32}
\]
The exact metric substitution in the completion source gives (3).
After taking the finite minimum of the constants, any
\[
                           0<R_0<\operatorname{arsinh}(m/Y)
 \tag{33}
\]
works for every selected vertex and every sufficiently large \(j\).
The basis change
\((\mu_v,\lambda_v)\mapsto(\mu_v+p_v\lambda_v,\lambda_v)\)
has determinant one. Adding the axis therefore has exactly cone
angle \(2\pi\chi_v^{(j)}\) and core length \(2H_v^{(j)}\), with
the original primitive meridian and no reset of its period.
The limiting model uses the limiting parameters in (3), which are
nondegenerate by (1) and (25).

## 6. The complete cusps

Main meridians remain nontrivial parabolics in the regular face
charts. For example a literal consecutive-white word is
\[
             W_0^{-1}W_1:z\longmapsto z+(E-1),\qquad E-1\ne0.
 \tag{34}
\]
The other corner words remain nonidentity by the original regular
matrix entries. Normalize one such primitive main translation to
one. The finite developed triangle coordinates and the other
original translation period then converge.

Every main ideal vertex is incident to at least one tetrahedron
which stays positive. At a one-square corner, the two flat
tetrahedra in each octahedral fan alternate with the two positive
ones; each equatorial vertex is incident to one of each. The
assertion is immediate in a positive edge block. Thus some triangle
in every main link has positive limiting Euclidean area.

For the positive members, the area of the flat translation torus
equals the sum of the Euclidean areas of its fixed link triangles.
The limiting sum is strictly positive. Equivalently, its limiting
translation lattice has positive covolume and does not collapse.

At an unselected auxiliary vertex \(t_v=0\). Its incident edges
stay strictly positive at every regular finite angle of the other
endpoint in the canonical strip. In tangent coordinates the
criterion is \(C=0<X\), or, for a purely imaginary remaining
tangent, modulus less than one. All its limiting link triangles
are therefore positive. The same area argument proves that its
translation lattice stays nondegenerate, without selecting a
possibly vanishing generator.

The epigraph bound (27)--(28) gives original horoball cusp
neighborhoods with uniform cutoff in these translation frames.
Equations (29)--(30) make them disjoint from one another and from
the selected tubes. Their limiting translation tori are
nondegenerate. This completes Theorem 1.

## 7. Scope

The theorem supplies uniform embedded ends before the corner and
a canonical same-marked end model at the corner. The fixed-point
calculation uses the literal flat triangles; a loxodromic longitude
alone would not supply this conclusion. The quotient-link result
identifies the part that can be repaired with the same periods.

No claim is made that this quotient extends through the compact
middle, that a positive ideal triangulation of that middle is
constructed, or that any quantum change of cells is source
preserving. Infinite unfolded longitude saturation and the failure
of particular fixed-boundary star replacements are compatible with
the uniform end theorem.

## Direct sources and readback

- [Original angular cells](actual_all_circle_angular_octahedra.md):
  ordered apices, white maps, turn-and-closing placement, and
  endpoint shape conventions. SHA256
  1e4129977e047da2048e338cd1a40bb07edb022b8f6a97d6be7f1813efc7835a.
- [Original corner stars](research_regular_corner_original_edge_stars.md):
  rational normalization and original seam interpretation. SHA256
  cdbfedd7d7817ee962edb0154d6e2e9d159e11b8c4563ee6352c7efc0a92bc7c.
- [Finite square corners](research_square_corner_flat_geometry.md):
  one-square classification and regularity exclusions. SHA256
  511c2c93d61482664cf62ed3b146c0af19ffbb149fa8772a4d1eb5ca7026eed0.
- [Positive edge coordinates](research_positive_edge_global_monotonicity.md):
  the literal rational shape formulas used in the endpoint exchange
  (21). SHA256
  da5129c7110190035eedb8249d4004dd06b5a7555e78d948234d8de50fa17500.
- [Pointwise marked completion](research_positive_point_marked_completion.md):
  similarity links, logarithmic diffeomorphisms, actual period
  marking, and nontrivial main meridians. SHA256
  28de22f081e24629ea6d26ad05213301a9bcf5d17d3ae7d00cc9c675a8218887.
- [Original cone completion](actual_all_circle_geometric_completion.md):
  original epigraph ends, exact tube metric, and marked cone
  interpretation before unit charge. SHA256
  cc58cc7c7a133eb69295d9a447aa39568a3656a2a18a2bd8335eecda314efae9.
- [Radial compactness](research_radial_charge_compactness_and_corners.md):
  available uniform height input and scope of sharp corners. SHA256
  744d36368876f255df6e2b1f2ca15dd23e805d5d5a39b009f6983fec2c6243ec.

The entire final proof was reread by the author. The two completion
sources, square-corner source, and positive-edge source were read in
full in this sequence; prior complete reads of the unchanged angular,
original-star, and radial sources were retained, their used implications
reread, and all seven pinned hashes rechecked. Independent peer and root review are
required before adoption. Only written mathematics, source-text
inspection, and file hashes were used; no mathematical execution,
numerical computation, test, or compilation was run.
