# Original edge stars at a regular sharp corner

Private written geometry, 16 November 2026.

A regular sharp corner admits an explicit calculation in the original
face-paired cells. The white pairing and the next disk-page pairing
close the zero-angle equatorial edge in a four-tetrahedron star.
Combining that star with the old apex-diagonal star gives a natural
seven-tetrahedron ball, under the distinct-star hypothesis stated below.
Its eight developed vertices are explicit and distinct. Its developed
outer boundary nevertheless intersects itself at the corner.

This rules out two particular embedded-cell repairs: changing only the
internal subdivision of one original octahedron, and replacing the
seven-tetrahedron ball while keeping its developed outer boundary.
It does not rule out a larger cluster, an abstract positive gluing
whose developing map is not injective on that boundary, or the original
filled geometry. No filling power or primitive curve is changed here.

## 1. The original local data and the wall

Use the original ordered angular cells, with equator
\((0,\infty,1,R)\), plus apices \(Z,W_+\), and minus apices
\(Z/E,W_-\). Their cyclic shapes are
\[
 (A,B,-1/A,-1/B),\qquad(C,D,-1/C,-1/D).
 \tag{1}
\]
The opposite equatorial edge of each tetrahedron has the same dihedral
angle as the internal apex diagonal. The four tetrahedra around that
diagonal form the original octahedral fan.

The full corner calculation in the pinned square-corner source gives
\[
 A=i e^{2Q_0},\qquad C=i e^{-2P_0},\qquad
 B=\frac{C-1}{C+1},\qquad D=\frac{A+1}{1-A}.
 \tag{2}
\]
Here \(P_0,Q_0\) are the original strip coordinates; they are not
peripheral multipliers. A finite sharp \(P_0\)-corner has
\[
 \sinh(2U)\sinh(2V)=1,\qquad U,V>0,
 \tag{3}
\]
and makes \(B,C,-1/B,-1/C\) real, away from \(0,1,\infty\).
If the other square is interior, \(A,D\) remain in the upper
half-plane and all original face coordinates remain regular.
The adopted radial compactness theorem supplies precisely sharp
corners, with nonzero core heights, as possible positive-charge
limits. It does not assert that such a limit occurs.

For the explicit ordered-star calculation assume that the incoming
base tetrahedron has
\[
                    b=B>0,\qquad b\ne1,\qquad a=A\in\mathbb H.
 \tag{4}
\]
The other real shape in that octahedron is \(-1/b<0\). Write
\[
       D=\frac{a+1}{1-a}\in\mathbb H,\qquad
       L=bD=-Q,\qquad Q=e^{it}.
 \tag{5}
\]
The last equality is the original angular identity
\[
 B=i e^{it/2-r_w},\qquad D=i e^{it/2+r_w}.
 \tag{6}
\]
In particular \(L\in\mathbb H\).

Condition (4) specifies the ordered chart used in the theorem.
The calculation is independent of all integer powers. At other
ordered corner occurrences the original face labels must first be
transported, including any copy exchange and reversal of a disk frame.
The individual-octahedron conclusion in Section 2 does not need (4).
We do not identify a MAIN diagonal substitution with this relabeling.

## 2. Why an internal diagonal change in one octahedron cannot suffice

**Proposition 1.** At a finite sharp corner where the developed
triangular boundary of an original octahedron remains regular, no
embedded strictly positive ideal cell has exactly that developed
triangulated boundary.

**Proof.** Each affected reciprocal pair \(z,-1/z\) contains one
positive real shape. In the apex-diagonal fan its opposite
equatorial edge belongs to only that tetrahedron. Its inherited
interior dihedral angle therefore tends to zero.

Normalize the equatorial edge to \((0,\infty)\). The other two
vertices of this flat tetrahedron lie on the same positive real ray,
after a rotation and scaling. The two adjacent boundary triangles
then overlap in an open collar of that edge in their common
geodesic plane. Thus the prescribed developed boundary is not
embedded. Equivalently, any subdivision retaining that boundary
edge and its inherited zero angle would express zero as a sum of
strictly positive incident tetrahedral angles.

An artificial \(2\pi\) boundary wedge changes the inherited angle
lift and does not give the stipulated embedded boundary. This
argument is not applied at a two-corner singularity where the
equator or boundary faces cease to be defined. \(\square\)

## 3. The actual white and disk-page orbit

Let the next outgoing page at the same circle belong to an edge
\(e'\). Denote its corresponding shapes by \(B',D'\), and assume
that edge is positive:
\[
                 B',D'\in\mathbb H,\qquad B'D'=L.
 \tag{7}
\]
This is a hypothesis about that actual neighboring page, not a new
choice of a filling. The relevant pure or odd seam is the prescribed
original seam.

Normalize the incoming base edge \((\infty,1)\) and its plus apex
by
\[
                         h(z)=\frac{z-1}{Z-1}.
 \tag{8}
\]
The base endpoints become \((\infty,0)\), the plus apex is \(1\),
and the far apex is \(b\), since
\[
                    B=[Z,W_+,\infty,1]
                      =\frac{W_+-1}{Z-1}.
 \tag{9}
\]
The original white map is
\[
 W_1(z)=\frac{z+E-1}{E}.
 \tag{10}
\]
Consequently the transported opposite apex is
\[
 h\bigl(W_1^{-1}(Z/E)\bigr)
       =\frac{Z-E}{Z-1}=-Q=L.
 \tag{11}
\]
The first two tetrahedral sectors around this equatorial edge
therefore have shapes \(b,D\). This uses the actual white transition
of the completed two-leaf block; a virtual leaf map has not been
installed as an additional face.

For the outgoing page put
\[
                         k'(w)=\frac{w}{w-R'}.
 \tag{12}
\]
Its plus and minus apices are \(Z'\), \(Z'/E'\).
The ordered outgoing fan gives
\[
 \frac{k'(W'_+)}{k'(Z')}=-\frac1{B'},\qquad
 \frac{k'(W'_-)}{k'(Z'/E')}=-D'.
 \tag{13}
\]
The second formula retains the reversed equatorial order in the
minus projection copy.

The original pure disk map sends the ordered incoming triangle
to \((Z',0,R')\) in the same copy. Thus, for its transition \(M\),
the unique three-point normalization gives
\[
                    h(M^{-1}w)=\frac{k'(Z')}{k'(w)}.
 \tag{14}
\]
Its transported far apex is consequently \(-B'\).
For the original odd map from an incoming plus triangle to an
outgoing minus triangle, the ordered target is
\((Z'/E',R',0)\). Its normalization is instead
\[
                    h(M^{-1}w)=\frac{k'(w)}{k'(Z'/E')},
 \tag{15}
\]
and the transported far apex is \(-D'\).

These are literal seam orders. In a single leaf frame they can
also be checked from
\[
 S(z)=\frac{-ER}{z-1-E},\qquad
 A_{\rm odd}(z)=\frac{R(z-1)}{z+ER-1-E},
 \qquad Z^2-(1+E)Z+ER=0.
 \tag{16}
\]
In particular
\[
 \begin{split}
 S^{-1}(w)-1&=\frac{E}{k(w)},\\
 A_{\rm odd}^{-1}(w)-1&=E(1-R)k(w),\\
 \frac{E(Z-R)}{Z(Z-1)}&=1,\qquad
 \frac{E(1-R)Z}{(Z-1)(Z-ER)}=1.
 \end{split}
 \tag{17}
\]
Equations (13) and (17) give exactly (14)--(15).
For different incident blocks, uniqueness of their ordered
three-point face map proves the same formulas with primes.

The pure base return \(W_3S=\bar S W_1\), and the odd base return
\(W_1^{-1}B_{\rm odd}W_3^{-1}A_{\rm odd}=I\), close four
successive face occurrences. The primitive paths and both physical
odd signs remain those of these original words. Traversing a seam
in reverse means inverting that word, not retaining the same
displayed ordered tuple.

It follows that the developed link of this original equatorial
edge has cyclic vertices
\[
                   (1,b,L,d),\qquad
 d=\begin{cases}
       -B',&\text{pure ordered seam},\\
       -D',&\text{odd ordered seam}.
    \end{cases}
 \tag{18}
\]
Its four cyclic tetrahedral shapes are respectively
\[
 \begin{cases}
 (b,D,-1/D',-1/B'),&\text{pure},\\
 (b,D,-1/B',-1/D'),&\text{odd}.
 \end{cases}
 \tag{19}
\]
Their product is one. At the wall, the first has inherited
angle zero; the other three have angles in \((0,\pi)\) and
sum to \(2\pi\). Indeed, writing
\(\theta=\arg L\in(0,\pi)\), (7) gives
\(\arg B'+\arg D'=\theta\), while \(\arg D=\theta\).

The four edge occurrences, rather than distinct global vertex
names in the quotient, are what the face words specify. The
following ball statement makes the required local incidence
hypothesis explicit.

## 4. The seven-tetrahedron ball and its eight actual vertices

Assume that the local old apex-edge star and the equatorial-edge
star just traced each have four tetrahedra and, in the chosen
unfolded occurrence, intersect only in their common tetrahedron.
No additional identification of their simplices is imposed.
This condition must be checked before treating the cluster as an
embedded subcomplex of a particular quotient or cover.

In the normalization (8), the original equatorial vertices \(0,R\)
become
\[
 u=\frac{ab-1}{a-1}
      =\frac{(1-b)D+b+1}{2},\qquad
 v=\frac{b(a+1)}{a+b}
      =\frac{2bD}{(b+1)D+b-1}.
 \tag{20}
\]
For the first formula use
\(a=Z/W_+=(1+c)/(1+bc)\), where \(c=Z-1\).
For the second use the next original fan shape
\[
                  [1,b,0,v]=-\frac1a.
 \tag{21}
\]
Thus the union has precisely the developed vertex list
\[
                    0,\ \infty,\ 1,\ b,\ u,\ v,\ L,\ d.
 \tag{22}
\]

**Lemma 2.** All eight points in (22) are distinct under
(4) and (7).

**Proof.** The four first points are distinct. All denominators
in (20) are nonzero, because \(D\in\mathbb H\) and \(b>0\),
\(b\ne1\). Moreover
\[
 \operatorname{sign}\Im u=\operatorname{sign}(1-b),\qquad
 \operatorname{sign}\Im v=\operatorname{sign}(b-1).
 \tag{23}
\]
Neither \(u\) nor \(v\) is \(0,1,b,\infty\), and they differ
from each other. Also \(L\in\mathbb H\) and \(d\in-\mathbb H\).
If \(u=L\), (20) gives
\((1-3b)D=-(b+1)\), impossible for nonreal \(D\).
If \(v=L\), it gives
\((b+1)D+b-1=2\), also impossible.

Write \(d=-X\), with \(X=B'\) or \(D'\). Equation (7) gives
\[
                         0<\arg X<\arg D=\theta<\pi.
 \tag{24}
\]
Only the lower-half-plane member of \(u,v\) could equal \(d\).
If \(b>1\), that member is \(u\), and
\[
              -u=\frac{b-1}{2}D-\frac{b+1}{2}
 \tag{25}
\]
has argument strictly greater than \(\arg D\): subtracting a
positive real number from a positive multiple of \(D\) rotates
its upper-half-plane argument strictly counterclockwise.
If \(0<b<1\), the member is \(v\), and
\[
              \frac{-v}{D}
                 =\frac{-2b}{(b+1)D+b-1}\in\mathbb H.
 \tag{26}
\]
Since \(-v,D\in\mathbb H\), this again gives
\(\arg(-v)>\arg D\). Both possibilities contradict (24).
All remaining pairs are separated by half-planes. \(\square\)

Ignoring orientation only for the following incidence list, the
seven tetrahedra are
\[
 \begin{gathered}
 F=\{0,\infty,1,b\},\\
 O_1=\{1,b,0,v\},\quad
 O_2=\{1,b,v,u\},\quad
 O_3=\{1,b,u,\infty\},\\
 N_1=\{0,\infty,b,L\},\quad
 N_2=\{0,\infty,L,d\},\quad
 N_3=\{0,\infty,d,1\}.
 \end{gathered}
 \tag{27}
\]
The \(O\) fan is the original octahedron, and the \(N\) fan
is the actual paired equatorial-edge star. The central
tetrahedron and \(O_2\) are flat at the wall; the other five
tetrahedra are positive in their original orientations.

**Lemma 3.** Under the stated incidence hypothesis, (27) is a
triangulated topological ball. Its only interior edges are
\((1,b)\) and \((0,\infty)\). Its boundary has twelve triangles.

**Proof.** Attach the tetrahedra in the displayed order.
\(O_1,O_2\) each attach along one boundary face;
\(O_3\) attaches along its two boundary faces adjoining the
old apex edge. This closes the old four-tetrahedron fan and
gives its octahedral ball. Then \(N_1,N_2\) each attach along
one boundary face, and \(N_3\) attaches along two boundary
faces adjoining the other central edge. Each attaching
intersection is a disk and contains all incidental shared
edges and vertices. The distinct-star hypothesis excludes
additional attachments, so every step preserves a ball.

The four edges of \(F\) other than these two star centers are
still boundary edges. The remaining boundary triangles are
\[
 \begin{gathered}
 (1,0,v),(b,0,v),(1,v,u),(b,v,u),
 (1,u,\infty),(b,u,\infty),\\
 (0,b,L),(\infty,b,L),(0,L,d),(\infty,L,d),
 (0,d,1),(\infty,d,1).
 \end{gathered}
 \tag{28}
\]
This also checks the assertion directly. \(\square\)

## 5. The developed boundary obstruction

**Theorem 4.** The developed boundary (28) is not embedded at
the sharp corner. Consequently this seven-tetrahedron ball
has no embedded strictly positive ideal-cell replacement
with exactly that developed boundary.

**Proof.** All four ideal vertices of \(F\) lie on the real
circle. If \(b>1\), their cyclic order is
\[
                           0,\ 1,\ b,\ \infty.
 \tag{29}
\]
The geodesics \((0,b)\) and \((1,\infty)\) are its two
diagonals and intersect at a finite point of their common
geodesic plane. Both are distinct boundary edges in (28).
If \(0<b<1\), the cyclic order is
\[
                           0,\ b,\ 1,\ \infty,
 \tag{30}
\]
and the two intersecting boundary diagonals are \((0,1)\)
and \((b,\infty)\). In either case these are the two
\(\pi\)-angle edges of the flat tetrahedron.

Their intersection is not a common combinatorial vertex
or boundary edge. Therefore the prescribed boundary
development is not injective. An embedded cell cannot
have that boundary, independently of its proposed internal
triangulation or additional internal vertices. \(\square\)

This is a wall statement. It does not assert nonembedding
on either open side of the wall. It also does not forbid
a larger cluster which internalizes or removes these
crossing boundary edges. Any such further move must use
the original face words and verify its own developed
outer boundary.

## 6. Marking and coverage

The formulas above are obtained by unfolding the existing
white and disk faces. They do not replace \(R^n\) by a
quarter-turned power, exchange a rational tangle, alter
\(n=\eta-2p\), or reset a meridian logarithm. They identify
where a same-marked cell replacement would have to act;
they do not construct that replacement.

The regular one-corner hypothesis excludes the separate
two-corner loci where \(q=0\), \(q=\pm i\), or the original
equator/apex coordinates become singular. The neighboring
positive-page hypothesis is used in (7), the angle count,
and the noncollision proof. The distinct-star incidence
hypothesis is used only for the seven-tetrahedron ball
and its explicit outer boundary. No general absence of
global cell identifications is deduced from a local return
word.

The result gives no new radial existence theorem, positive
cone-metric continuation, quantum-cycle coefficient, or
filling class satisfying the volume identity.

## Direct sources and author readback

The complete texts of the first three sources below were
read for this proof; the full adopted readback of the
unchanged fourth source was retained and its implications
and hash were rechecked. Only their stated original
incidence, face-map, and corner formulas are used.

- [Original angular octahedra](actual_all_circle_angular_octahedra.md),
  Sections 1--4: apex-diagonal fans, the actual completed white
  maps, and the two-triangle pants ratios.
  SHA256
  `1e4129977e047da2048e338cd1a40bb07edb022b8f6a97d6be7f1813efc7835a`.
- [Original marked face words](actual_conway_general_mask_marked_filling.md),
  Sections 4--6: pure/odd ordered maps, four-occurrence edge
  words, actual versus virtual white transitions, and the
  retained primitive disk paths.
  SHA256
  `881a265fd9356e6c531ca5db49f337aff3928fac0fe6113a1a03acde39b16ec3`.
- [Finite square-corner geometry](research_square_corner_flat_geometry.md),
  Sections 1--3 and 7: the exact interleaved shape formulas,
  sharp finite corner equality, regular one-corner face chart,
  and the scope of previously supplied replacements.
  SHA256
  `511c2c93d61482664cf62ed3b146c0af19ffbb149fa8772a4d1eb5ca7026eed0`.
- [Radial compactness and sharp corners](research_radial_charge_compactness_and_corners.md),
  Theorem 2 and Corollary 3: the sharp finite corner alternative
  and nonzero limiting heights. They provide context rather
  than an existence assertion for the wall analyzed here.
  SHA256
  `744d36368876f255df6e2b1f2ca15dd23e805d5d5a39b009f6983fec2c6243ec`.
