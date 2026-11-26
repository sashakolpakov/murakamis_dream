# The crossing-tunnel construction of the marked shadow cellulation

Private written proof, 17 November 2026. This supplies an explicit
topological justification of the classical crossing-block claim in [F].
The individual face identifications are realized inside the original
oriented three-sphere. In particular, the proof does not identify an
over-port's two-triangle disk with an under-port's two-triangle disk:
their shared diagonals can have different vertex types.

No quantum Pachner identity, integral flattening transfer, positive
geometric triangulation, isolated critical point, or volume limit follows
from this construction.

## 1. Statement and the actual diagram

Let \(D\) be a regular oriented diagram on an oriented projection sphere
of a knot \(K\subset S^3\), with \(c>0\) crossings. Retain its crossing
signs, its specified cut on a regular arc, and its blackboard framing.
Use the four ordered tetrahedra of [F, Section 4] at a positive crossing:

\[
\begin{array}{c|c|c}
i&\text{ordered vertices}&\text{orientation}\\\hline
0&(p,a,c,s_0)&-1\\
1&(p,a,c,s_P)&+1\\
2&(p,a,b,s_M)&+1\\
3&(p,a,b,s_R)&-1.
\end{array}                                                   \tag{1}
\]

Here \(a\) is the over-arc, \(b,c\) the incoming and outgoing under-arcs.
The two occurrences of \(p\), and the region vertices, are local
occurrences before face identifications. Faces are numbered by the
omitted ordered vertex. The internal pairings are

\[
(0,0)\leftrightarrow(2,0),\quad
(1,0)\leftrightarrow(3,0),\quad
(0,3)\leftrightarrow(1,3),\quad
(2,3)\leftrightarrow(3,3).                              \tag{2}
\]

The exterior triangles continue along the actual diagram arcs as
specified in the table in Section 4 below. Read the negative block
backwards, reversing its orientation and retaining the actual over and
under arcs. The claim is about the resulting *individual* face maps.

**Theorem.** These identifications give a generalized tetrahedral
cellulation of \(S^3\setminus K\), with two additional spherical ends.
Filling those ends by balls gives the original knot exterior. Its
torus end is the boundary of the original tubular neighborhood of \(K\).
The chosen cut, oriented meridian, blackboard parallel, and hence the
preferred longitude are retained. The two spherical vertices are free
vertices; they are not additional cusps of a positive hyperbolic metric.

## 2. Add tunnels, but retain their co-cores

Realize the diagram in a thin product neighborhood of the projection
sphere. In each disjoint crossing ball add the short vertical interval
joining the over- and under-strands. These \(c\) intervals have mutually
disjoint interiors and meet \(K\) only at their endpoints. Put

\[
\Gamma=K\cup\bigcup_{j=1}^{c}\text{tunnel}_j,
\qquad H=N(\Gamma).                                     \tag{3}
\]

Equivalently, \(H\) is obtained from the actual \(N(K)\) by attaching
these \(c\) one-handles. Let \(\Delta_j\) be their co-core disks. Thus
cutting \(H\) along all \(\Delta_j\) restores \(N(K)\), up to harmless
boundary collars. This assertion retains the embedded core \(K\); it
does not identify a solid torus merely from its fundamental group.

In a crossing ball the two strand intervals and their joining interval
form an unknotted four-legged tree. Its regular neighborhood is a ball
with four specified exit disks. Contracting the joining interval changes
that tree to a planar four-valent star without changing its embedded
regular neighborhood. This is a local ball operation, performed with
the four exit collars fixed. Outside the crossing balls the connecting
arc neighborhoods are already the planar strips. Consequently \(H\)
is the unknotted regular neighborhood of the underlying planar shadow
graph. Carry the disks \(\Delta_j\) and the original core through this
identification; do not replace the disks by unspecified slopes.

Here is an explicit local disk which fixes that last point. Take a round
crossing ball, with north/south exits on the \(y\)-axis and east/west
exits on the \(x\)-axis. For small positive \(\delta,\epsilon\), use

\[
\begin{split}
K_{\rm over}&=(0,y,\delta(1-y^2)),\\
K_{\rm under}&=(x,0,-\delta(1-x^2)),\\
\Delta&=\{z=\epsilon(x^2-y^2)\}\cap\text{ball}.
\end{split}                                                   \tag{4}
\]

The first arc is strictly above the disk, the second strictly below it,
including at their exit centers. The disk meets the vertical joining
interval once, transversely at its center. It is the co-core for the
one-handle joining these two strand neighborhoods. Its boundary avoids
small exit disks and meets the equator at precisely \(x^2=y^2\), once in
each quadrant. The intersections are transverse. Rounding the exit
collars changes none of these incidences. Mirroring this construction
gives the other crossing sign. In particular no boundary Dehn twist is
introduced by choosing an arbitrary disk with the same partition of
the four exits.

## 3. An embedded simple foam and its complementary regions

The planar shadow is connected. Its regular neighborhood on the sphere
has \(c+2\) complementary disks, one for each diagram region; repeated
corners and nugatory crossings cause no difficulty. In the complement
of the planar \(H\), take the corresponding properly embedded region
disks \(D_f\). Cutting along all of them separates that complement into
the upper and lower balls, denoted \(B_P,B_S\).

Consider the embedded two-dimensional complex

\[
\Sigma=\partial H\ \cup\ \bigcup_j\Delta_j\ \cup\ \bigcup_fD_f.
                                                               \tag{5}
\]

The disk interiors are disjoint. Their boundary curves lie on opposite
sides of \(\partial H\) and meet there as in (4). Locally at one such
intersection the complex is a plane, one half-plane on its upper side,
and a transverse half-plane on its lower side. Its link is the
tetrahedral graph \(K_4\). Away from these points its singular lines
have the ordinary three-sheet \(Y\times I\) model. Thus there are
exactly four true vertices of \(\Sigma\) per crossing.

The faces on \(\partial H\) need an explicit check. Its upper and lower
portions are each a sphere with \(c+2\) holes, of Euler characteristic
\(-c\). A co-core boundary has two arcs on each portion. In the upper
portion, these arcs isolate the two under ends of a crossing and leave
the over passage continuous. Along the diagram strips the resulting
pieces are precisely regular neighborhoods of the arcs obtained by
cutting the diagram at every undercrossing: the \(c\) Wirtinger
intervals. Each piece is a disk. The lower pieces similarly thicken
the \(c\) intervals obtained by cutting at every overcrossing, and are
disks as well. This is an identification of the pieces, not a deduction
from Euler characteristic. The check
\(-c+2c=c\) agrees with their number.

It follows that all faces of \(\Sigma\) are disks, in these four
families:

\[
\begin{array}{c|c|c}
\text{face}&\text{adjacent region types}&\text{number}\\\hline
D_f&P,S&c+2\\
\text{upper arc disk}&P,K&c\\
\text{lower arc disk}&S,K&c\\
\Delta_j&K,K&c.
\end{array}                                                   \tag{6}
\]

The two \(K\)'s in the last row are occurrences of the same region.
Indeed the complementary regions of (5), before reattaching their
boundary faces, are exactly

\[
B_P,\quad B_S,\quad H\text{ cut along all }\Delta_j\cong N(K).
                                                               \tag{7}
\]

The first two are balls; the last is the original solid-torus region
with its original oriented core. All operations can avoid the chosen
cut and its small product neighborhood.

## 4. Dual tetrahedra and every local face map

Dualize the foam: one tetrahedron for each true vertex, one face pairing
for each singular-line segment, and one edge for each foam face. Near
a face the thickening is \(D^2\times I\); near a singular line it is
\(Y\times I\); near a true vertex it is the dual tetrahedral model.
Truncating the dual tetrahedra and gluing these models gives a regular
neighborhood of \(\Sigma\). One can verify this relative to all
boundary pieces by subdividing these product models into flags of
incident cells. Both the foam thickening and the truncated dual have
that same subdivision. No choice of a global saddle or developing map
is involved.

At a positive crossing label the four intersections in (4) by

\[
0=NE,\quad1=SE,\quad2=NW,\quad3=SW.                  \tag{8}
\]

The over passage is north-to-south, the under passage west-to-east.
The tetrahedra are ordered \((P,\text{over},\text{under},S)\).
With the ambient orientation their signs are \(-,+,+,-\), giving (1).
Here is a local orientation check in the foam itself. Near an
intersection use positive coordinates \((u,v,w)\), with \(u\) azimuth,
\(v\) height, and \(w\) the outward normal to \(\partial H\). The
outside regions are \(P=(0,1,1)\), \(S=(0,-1,1)\). If the co-core
boundary has negative slope \(v=ku\), the inside over/under chambers
can be represented by \((1,0,-1)\), \((-1,0,-1)\). The determinant
in order \((P,\text{over},\text{under},S)\) is \(-8\). Positive slope
interchanges these inside chambers and gives \(+8\). For (4), the
four slopes in order (8) have signs \(-,+,+,-\), as asserted. These
are orientations of dual topological cells, not signs of developed
hyperbolic volumes.

The upper co-core arcs join \((0,1)\) and \((2,3)\). Their three adjacent
regions are \(P,K,K\), so their dual face is the face omitting \(S\),
namely face 3. The lower co-core arcs join \((0,2)\) and \((1,3)\);
they omit \(P\), hence give face 0. This proves all four internal
pairings in (2), with their actual vertex maps.

The remaining singular lines lie on region-disk boundaries and
continue along the actual arc strips. Their individual exterior faces
are exactly

\[
\begin{array}{c|c|c}
\text{strand end}&\text{first triangle}&\text{second triangle}\\\hline
\text{over input }N&(0,2)&(2,2)\\
\text{over output }S&(1,2)&(3,2)\\
\text{under input }W&(2,1)&(3,1)\\
\text{under output }E&(0,1)&(1,1).
\end{array}                                                   \tag{9}
\]

Each triangle continues to the next triangle on the same side of the
same original diagram arc, preserving its \(P,K,S\) occurrences.
This is a continuation of a singular line in the embedded foam.
It does not require the union of the two triangles at one end to be
simplicially isomorphic to the union at the other end. This distinction
resolves the apparent over/under-port diagonal mismatch.

For the developed marking of [F], choose the meridian charts along
these same strips. The face-0 change crosses the over-meridian once:

\[
(a,c,s_0)\mapsto(a,b,a s_0),\qquad
(a,c,s_P)\mapsto(a,b,a s_P),\qquad b=a c a^{-1}.        \tag{10}
\]

Thus \(s_M=a s_0,s_R=a s_P\), and these are exactly the two transports
printed in [F]. The face-3 continuations stay in one chart and have
transport one. Reversing the crossing gives the inverse maps and
reversed orientations. This verifies the literal signed face table,
not just cancellation of its image in a configuration group.

## 5. The manifold and its peripheral marking

The truncated dual in Section 4 is the complement of smaller copies
of the three regions (7). For the solid-torus region, take a smaller
tubular neighborhood of its retained core; the portion between it and
the region boundary is a torus collar. For the ball regions take smaller
balls, leaving spherical collars. These choices make the dual regular
neighborhood identification relative to the original cut.

Consequently the truncated quotient is

\[
S^3\setminus\bigl(\operatorname{int}N(K)
 \cup\operatorname{int}B_P^3\cup\operatorname{int}B_S^3\bigr).
                                                               \tag{11}
\]

Its two free vertex links are spheres and its knot vertex link is the
original peripheral torus. Filling the two spheres gives precisely
\(S^3\setminus\operatorname{int}N(K)\), with its original orientation.
This follows from the embedded construction, not a comparison of
Euler characteristics, fundamental groups, or volumes.

The meridian is the positively oriented boundary of a transverse disk
to the retained core. Follow the blackboard parallel through the same
arc strips to obtain the longitudinal normal path on the dual torus.
It traverses \(K\) once. At a crossing its underpass transition is the
original Wirtinger transport (10); a local meridional circuit crosses
one meridian face, not a multiple cover. Thus this is the marked
blackboard longitude used in [F] and [L]. If the diagram has writhe
\(w\), subtracting \(w\) copies of that meridian gives the preferred
longitude. In the word convention of [L, (3.2)--(3.5)], it is exactly
\(\lambda=W^{-1}\mu^{-w}\). The opposite eigenflags of a peripheral
representation are not identified by this topological statement.

## 6. The five-cell replacement is relative to the same boundary

One may now replace each four-tetrahedron ball by the following five
tetrahedra without changing any external face map. In a coherently
developed crossing ball use abstract vertices

\[
(0,1,2,3,4,5)=(s_0,s_P,p,a^{-1}p,c,a).
\]

The transported four-cell chain and the five-cell chain are

\[
\begin{split}
\Gamma_4&=-[2540]+[2541]+[3540]-[3541],\\
\Gamma_5&=[0123]+[0134]+[0142]+[2315]+[2350].
\end{split}                                                   \tag{12}
\]

Their boundaries are literally the same simplicial chain:

\[
[134]-[034]+[142]-[042]
 +[315]-[215]+[350]-[250].                         \tag{13}
\]

This is verified by expanding the alternating boundary of each term
in (12), not by an oriented-shape identity. Both complexes are balls.
For \(\Gamma_4\), the four tetrahedra surround its over-to-under
diagonal. For \(\Gamma_5\), the displayed order attaches along
\(0,1,2,1,2\) previous faces. The two-face attaching disks are
\((012,014)\), meeting along \(01\), and \((023,235)\), meeting along
\(23\). Its boundary is the eight-triangle octahedral sphere (13).
A common subdivision of that boundary extends over the two balls by
coning, giving a homeomorphism relative to the boundary. Thus the
replacement preserves (9)--(11), including the cut and peripheral
curves. This is a statement about PL balls; it needs no positivity
or convexity of the developed hyperbolic shapes. Apply the reflected
order at a negative crossing.

The classical shapes can also be checked without the rational
three-five-term cancellation. On the complete regular parabolic chart,
normalize \(a:z\mapsto z+1\), \(p=0\), \(s_0=S\), \(s_P=T\), and
write \(c(S,1)^t=D(T,1)^t\). The fixed point of \(c\) is
\((DT-S)/(D-1)\). The actual coordinates of [F, (2.2)] are

\[
A=\frac{S}{S+1},\qquad
B=\frac{S+1}{D(T+1)},\qquad
C=\frac{S(T+1)}{(S+1)T}.                         \tag{14}
\]

Substitution in the specified cross-ratio convention gives the five
ordered cell shapes

\[
\left(C,B,\frac1{BC},\frac AC,\frac1A\right).       \tag{15}
\]

For example, the third is \(DT/S=1/(BC)\), the fourth is
\(T/(T+1)=A/C\), and the fifth is \((S+1)/S=1/A\).
Their two interior-edge products are one. This computation is on the
open set where the six points are distinct and all denominators are
nonzero; the topological replacement did not require that open set.
The negative case uses the same marked reversed block, not a replacement
of the diagram by a positive one.

The source interpretation of this corollary remains limited. Equations
(12)--(15) do not transfer the original finite scalar, integral
logarithmic marks, or factorial endpoint sources to new quantum tensors.
In particular, the classical interior-edge products must not be
substituted for the shifted finite charges. No finite factorial
reflection or quantum five-term identity is claimed here.

## 7. Scope and complete direct sources

The construction supplies the missing explicit geometric justification
of the existing classical cellulation claim. It does not remove the two
framing directions of the actual critical correspondence. Nor does it
make every developed tetrahedron positive, transfer the integral
logarithmic marks to an arbitrary positive triangulation, or prove that
the original finite cycle has a nonzero geometric coefficient.

Both complete direct texts were read at these unchanged versions. The
proof above uses no programs, numerical tests, or public/frozen edits.

| Label | Source | SHA-256 |
|---|---|---|
| F | [Crossing fundamental cycle](crossing_fundamental_cycle.md) | 0d7d7da0f5cf4fe0d16907e7e999d5ce7980f7ff39d437df167c99ca30205b0f |
| L | [Exact longitude and regulator action](quantum_longitude_and_regulator_action.md) | e8ac5dc6bab05be0dad3810311dc3a8b169ad810b898aa3db75582087dbe8aa7 |
