# Flat edge-star propagation along the original longitude

Private written geometry, 16 November 2026.

At a regular sharp corner the original tetrahedral incidences give
an explicit obstruction to finite star saturation. Requiring the
full star of every \(\pi\)-angle edge of each acquired flat
tetrahedron forces an infinite orbit of the original primitive
longitude whenever its core height is nonzero.

The argument uses the original white maps and four ordered
tetrahedra in each projection copy. It does not replace a tangle,
change a slope, or infer nonexistence of the filled geometry.
It also does not prohibit a finite repair using a different
boundary triangulation or a different choice of cluster.

## 1. Original tetrahedra and white maps

Use the same regular ordered wall as in the pinned edge-star note.
The plus apices are \(Z,W_+\), the minus apices are \(Z/E,W_-\),
and both equators have ordered coordinates
\[
                      q_0=0,\quad q_1=\infty,\quad q_2=1,\quad q_3=R.
 \tag{1}
\]
Write \(\Delta_j^\pm\) for the tetrahedron with the corresponding
two apices and \(q_j,q_{j+1}\), with indices modulo four.
The minus orientation reverses the last two entries. Their shapes are
\[
 \begin{array}{c|cccc}
 j&0&1&2&3\\ \hline
 +&A&B&-1/A&-1/B\\
 -&C&D&-1/C&-1/D .
 \end{array}
 \tag{2}
\]
At the wall under consideration,
\[
 B=b>0,\quad b\ne1,\qquad
 C=\frac{1+b}{1-b},\qquad A,D\in\mathbb H.
 \tag{3}
\]
Thus \(\Delta_1^+,\Delta_3^+,\Delta_0^-,\Delta_2^-\) are flat,
with all four vertices of each tetrahedron distinct.

The two original white maps adjacent to the selected apex are
\[
 W_0(z)=z/E,\qquad
 W_2(z)=
 \frac{(E-R)z+R(1-E)}{(E-1)z+1-ER}.
 \tag{4}
\]
They carry \(Z\) to \(Z/E\). The first fixes \(0,\infty\);
the second fixes \(1,R\). Consequently these are actual
face-pairing occurrences, not arbitrary maps with the same
peripheral multipliers.

The primitive longitude in the original marked basis is
\[
                  \lambda=W_2^{-1}W_0,\qquad
                  \text{multiplier at its selected flag }Q^2,
                  \quad Q=e^{it}.
 \tag{5}
\]
The original full logarithm is \(2it\). If
\(t=s-iH\), \(H>0\), then \(|Q^2|=e^{2H}>1\).
The radial compactness theorem provides a positive lower bound
for \(H\) along positive-charge limiting families away from
charge zero. For the propagation theorem only \(H\ne0\) is needed.

## 2. The local side-edge star has eight sectors

Here we record the complete side-star calculation in the ordered
frame of the edge-star note. This supplies the finite local
incidences; it is separate from termination of repeated saturation.

Normalize the corner tetrahedron to
\[
                       F=\{0,\infty,1,b\}.
 \tag{6}
\]
The old apex edge is \((1,b)\). The equatorial edge is
\((0,\infty)\). Put
\[
 D=\frac{A+1}{1-A},\quad L=bD=-Q,\quad p=1-L,
 \qquad
 u=\frac{p+b+L/b}{2}.
 \tag{7}
\]
For the next actual page let \(B',D'\) be its original shapes,
with \(B'D'=L\). Its original face chart is assumed regular
for this local formula; positivity is not needed for the rational
identities. In the pure and odd ordered seam respectively set
\[
 d=-B'\quad\hbox{or}\quad d=-D',\qquad
                    q=\frac{p+d+L/d}{2}.
 \tag{8}
\]
These symbols are ideal-point coordinates; \(q\) is not the
square root used in the angular chart.

**Lemma 1.** In the unfolded occurrence the original side edge
\((\infty,1)\) has cyclic link
\[
                 (u,\ b,\ 0,\ d,\ q,\ p+d,\ p,\ p+b).
 \tag{9}
\]
Each consecutive pair in (9), together with
\((\infty,1)\), is one original tetrahedral sector.
In particular the side star has eight sectors, not four.
Repeated global labels are retained as separate occurrences.

**Proof.** In the incoming leaf frame use
\[
 h(z)=\frac{z-1}{Z-1},\qquad c=Z-1.
 \tag{10}
\]
The plus fan contributes the link path \(u,b,0\).
The original seam gives the next far apex \(d\), as in the
pinned pure/odd calculation. Thus three consecutive sectors
have link path \(u,b,0,d\).

Across the original white face with map \(W_0\), develop the
minus cell by \(W_0^{-1}\). Its other main vertex is
\[
             h(E)=\frac{E-1}{c}=1-L=p.
 \tag{11}
\]
Its far apex is \(p+b\). Indeed the other original white map
\(W_1(z)=(z+E-1)/E\) carries \(W_+\) to \(W_-\), so
\[
 h(EW_-)=\frac{W_++E-2}{c}=b+p.
 \tag{12}
\]
This supplies the two consecutive sectors with link path
\(p,p+b,u\).

For the neighboring page use primes and put
\(k'(w)=w/(w-R')\), \(c'=Z'-1\).
At a pure seam its developed coordinate is
\[
 g(w)=k'(Z')/k'(w),\qquad k'(Z')=E'/c'.
 \tag{13}
\]
The other main vertex is \(g(\infty)=E'/c'\).
The original quadratic relation and \(B'D'=L\) give
\[
 \frac{E'}{c'}=\frac{1-L-B'-D'}2
              =\frac{p+d+L/d}{2}=q .
 \tag{14}
\]
After the adjacent \(W'_0\) pairing, the remaining main
vertex and far apex are respectively \(p,p+d\).
For example
\[
 g(E'R')=q(1-1/E')=p,
 \quad
 g(E'W'_-)=p-B'=p+d,
 \tag{15}
\]
using \(E'W'_-=W'_++E'-1\) and
\(W'_+=1+B'c'\).

For the odd ordered seam the developed coordinate is instead
\[
                       g(w)=c'L\,\frac{w}{w-R'} .
 \tag{16}
\]
The other main vertex is \(g(1)=E'/c'=q\), since
\(E'(1-R')=c'^2L\). The next white pairing is \(W'_2\).
Direct substitution gives
\[
 g(W'_2z)-p=\frac{1-R'}{c'}\,\frac{z}{z-R'}.
 \tag{17}
\]
It follows that \(g(W'_2(0))=p\). The outgoing plus
fan identity
\[
 \frac{k'(W'_+)}{k'(Z')}=-1/B'
 \tag{18}
\]
then gives
\[
              g(W'_2W'_+)=p-L/B'=p-D'=p+d.
 \tag{19}
\]
Thus both seam choices supply the link path \(d,q,p+d,p\).
The original pure or odd side-edge return closes this path
with the incoming one.

Each octahedral occurrence contributes two tetrahedra at
an apex-to-equator side edge. The four original face
occurrences therefore give exactly the eight sectors
listed in (9). No additional tetrahedron is inferred from
a four-occurrence face word alone. \(\square\)

This formula alone does not assert that the side star or
any union of such stars has an embedded developed boundary.
For example, the seven-tetrahedron cluster already contains
the three sectors \(u,b,0,d\); five further sectors, with
four further link occurrences, are required to close this
one side edge.

## 3. Three forced \(\pi\)-edge steps give a longitude

Work in the universal cover of the original face-paired
triangulation, with its same developing representation.
For a set \(\mathcal C\) of tetrahedral occurrences impose
the following saturation rule:

If a flat tetrahedron belongs to \(\mathcal C\), then the
full original star of every one of its \(\pi\)-angle edges
also belongs to \(\mathcal C\).

The rule refers to the inherited angle limits from the
positive side. It is stronger than choosing a new
triangulation with the same representation.

**Proposition 2.** If \(b>1\), saturation starting from
\(F=\Delta_1^+\) forces
\[
 \Delta_1^+
 \ \longrightarrow\ W_0^{-1}\Delta_0^-
 \ \longrightarrow\ W_0^{-1}\Delta_2^-
 \ \longrightarrow\ (W_0^{-1}W_2)\Delta_1^+.
 \tag{20}
\]
If \(0<b<1\), it forces
\[
 \Delta_1^+
 \ \longrightarrow\ W_2^{-1}\Delta_2^-
 \ \longrightarrow\ W_2^{-1}\Delta_0^-
 \ \longrightarrow\ (W_2^{-1}W_0)\Delta_1^+.
 \tag{21}
\]
Every arrow uses the full star of a \(\pi\)-angle edge
of its preceding flat tetrahedron.

**Proof.** For a flat tetrahedron with cross ratio \(z>1\),
the two \(\pi\)-angle edges are the diagonals of its
cyclic ideal quadrilateral. For \(0<z<1\) the other pair
of side edges are the \(\pi\)-edges; for \(z<0\) the
displayed apex edge and its opposite equatorial edge
have angle \(\pi\). Applying this to the literal
ordered tuples (1)--(2) gives the following checks.

If \(b>1\), the edge \((Z,\infty)\) is a \(\pi\)-edge
of \(\Delta_1^+\). The developed tetrahedron
\(W_0^{-1}\Delta_0^-\) contains that same edge.
Its shape \(C=(1+b)/(1-b)\) is negative, so its apex
diagonal is a \(\pi\)-edge. The opposite tetrahedron
\(W_0^{-1}\Delta_2^-\) lies in that diagonal's star.
Its shape \(-1/C\) belongs to \((0,1)\), and its
selected-apex side edge
\[
                   W_0^{-1}(Z/E,1)=(Z,E)
 \tag{22}
\]
has angle \(\pi\). Since \(W_2\) fixes \(1\) and sends
\(Z\) to \(Z/E\), the last tetrahedron in (20)
contains (22). This proves all three steps.

If \(0<b<1\), begin with the \(\pi\)-edge \((Z,1)\).
It belongs to \(W_2^{-1}\Delta_2^-\), whose negative
shape \(-1/C\) makes its apex diagonal a \(\pi\)-edge.
That diagonal brings \(W_2^{-1}\Delta_0^-\), whose
shape \(C>1\) makes its selected-apex side edge
\[
                         W_2^{-1}(Z/E,\infty)
 \tag{23}
\]
a \(\pi\)-edge. The last tetrahedron in (21)
contains (23), because \(W_0\) fixes \(\infty\) and
sends \(Z\) to \(Z/E\). This proves (21).

All intermediate tetrahedra are flat by (2)--(3).
The maps used are the original face occurrences, so the
two final transformations are exactly \(\lambda^{-1}\)
and \(\lambda\) from (5), respectively. \(\square\)

## 4. No finite saturation at nonzero core height

**Theorem 3.** Suppose the regular wall (3) has
\(\Im t\ne0\). No finite set of unfolded tetrahedral
occurrences containing \(\Delta_1^+\) satisfies the
\(\pi\)-edge saturation rule.

**Proof.** Proposition 2 forces an occurrence
\(\lambda^{\varepsilon}\Delta_1^+\), where
\(\varepsilon=-1\) for \(b>1\) and \(+1\) for \(b<1\).
The original incidence rule is deck-equivariant.
Repeating the same three steps therefore forces
\[
                    \lambda^{j\varepsilon}\Delta_1^+,
                    \qquad j=0,1,2,\ldots .
 \tag{24}
\]
The original longitude is loxodromic, since its
multiplier \(Q^2\) has modulus different from one.
Its powers cannot give a finite orbit of the four
distinct developed vertices of \(\Delta_1^+\).
Indeed repetition would make a nonzero power permute
this finite set. A further power would fix at least
three distinct ideal points, hence would be the identity,
contradicting its nonunit multiplier.
Thus (24) contains infinitely many distinct occurrences.
The saturation set cannot be finite. \(\square\)

In particular complete stars of all edges of every
acquired flat tetrahedron cannot terminate either.
The projected graph support of (20)--(21) stays in
the same original two-octahedron edge block. Finiteness
of the original circle graph therefore does not imply
finiteness of the unfolded saturation. The obstruction
is peripheral winding, not graph-distance growth.

The theorem is stated in the ordered \(B>0\) wall
frame. Other occurrences require their original
transported labels; no arbitrary pants permutation is
being silently added. No neighboring-positive-page
hypothesis is needed for Theorem 3.

## 5. What the cyclic quotient supplies

The three-arrow walk (20) or (21) closes after
quotienting by the original longitude. It represents
that primitive peripheral class, rather than a new
surgery curve. This is a finite quotient walk in the
incidence complex. It is not yet a finite positive
collar or a solid-torus cellulation: saturation at
the other edges of its flat tetrahedra can introduce
further orbits, and its outer developed boundary
has not been identified.

There is an exact contracting coordinate for the
cyclic action. Let \(Z_*\) be the other fixed point
of \(\lambda\), and set
\[
                   \zeta=\frac{z-Z_*}{z-Z}.
 \tag{25}
\]
After the original flag convention, \(\lambda\)
acts as \(\zeta\mapsto Q^2\zeta\). For \(H>0\) its
inverse contracts finite \(\zeta\) by \(e^{-2H}\).
The adopted lower height bound makes this contraction
uniform along the stated positive-charge limiting
families.

This contraction is not a positive-cell construction.
A Möbius transformation preserves each tetrahedral
cross ratio, so the translated tetrahedra in (24)
remain flat. Likewise the adjoint action on the
three-dimensional projective Lie algebra has weights
\[
                           Q^2,\quad1,\quad Q^{-2}.
 \tag{26}
\]
For example a representative
\(\operatorname{diag}(Q,Q^{-1})\) acts by these weights
on the two off-diagonal matrices and the traceless
diagonal matrix. The centralizer direction has
eigenvalue one. Consequently a formal inverse of
\(1-\operatorname{Ad}\lambda\) on the whole space
is unavailable, and an inverse on its other two
weight spaces does not supply embedded positive
cells or the original contour coefficient.

The actual remaining geometric question is to
construct a compatible periodic replacement with
the original boundary and peripheral words, or
to find a finite replacement which does not impose
the saturation rule. Neither is obtained from
local star closure or the coordinate contraction alone.

## Direct sources and author readback

- [Original angular octahedra](actual_all_circle_angular_octahedra.md),
  Sections 1--4, read in full: the two original fans,
  the white maps, and the actual pants ratios.
  SHA256
  `1e4129977e047da2048e338cd1a40bb07edb022b8f6a97d6be7f1813efc7835a`.
- [Original marked face words](actual_conway_general_mask_marked_filling.md),
  Sections 4--6, complete readback retained at unchanged hash:
  actual white maps, pure/odd side returns, and
  \(\lambda=W_2^{-1}W_0\) with its primitive multiplier.
  SHA256
  `881a265fd9356e6c531ca5db49f337aff3928fac0fe6113a1a03acde39b16ec3`.
- [Regular corner edge stars](research_regular_corner_original_edge_stars.md),
  full readback retained, especially Sections 1 and 3--4:
  the ordered wall and the exact pure/odd normalizations.
  SHA256
  `cdbfedd7d7817ee962edb0154d6e2e9d159e11b8c4563ee6352c7efc0a92bc7c`.
- [Radial compactness and sharp corners](research_radial_charge_compactness_and_corners.md),
  full readback retained, especially Theorem 2 and
  Corollary 3: sharp limiting corners and positive heights.
  SHA256
  `744d36368876f255df6e2b1f2ca15dd23e805d5d5a39b009f6983fec2c6243ec`.
