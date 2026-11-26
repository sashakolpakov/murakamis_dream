# Sector charges and the complete open planar array

Private written proof, 17 November 2026. We prove the charge-change
formula for the full two-ended planar source, including both end colors.
The input is Kashaev's explicit planar weight [K, (2.7),(2.8),(3.6)].
Neither its claimed invariance nor its asserted freedom in the sector
charges is a proof premise.

## 1. Corners, end colors, and the source

Let \(G\) be a connected finite plane graph with four half-edges at
each crossing and two vertices of degree one. Both degree-one vertices
meet the unbounded face. Loops, multiple edges and repeated occurrences
of a region at a crossing are allowed. Each crossing specifies its
overpassing pair of opposite half-edges. A *corner* is an occurrence of
the sector between consecutive half-edges at a crossing. Thus four
corners are retained even if the same face occupies two sectors.

Fix \(N\ge2\) and a primitive \(N\)-th root \(q\). Every color and charge
below belongs to \(\mathbb Z/N\mathbb Z\). In counterclockwise order at
a crossing, label the edge colors \(i,j,k,l\), with \(j,l\) on the
overpassing strand, and let \(a,b,c,d\) label the following corners:
\[
       (i,j),\quad(j,k),\quad(k,l),\quad(l,i).
\]
Use the specified finite weight
\[
 R(i,j,k,l\mid a,b,c,d)
   =q^{a-k-j}W(j-i-a,\ i-l-d,\ l-k-c,\ k-j-b),
                                                        \tag{1}
\]
where \(W\) is exactly [K, (2.7)], including its finite products,
integer-residue representatives and two theta factors.
It is enough here that its four arguments in (1) are retained exactly.

A sector assignment is *admissible* if the four charges at every
crossing sum to one, the charges on every bounded face sum to one,
and every corner of the unbounded face has charge zero. Face sums
count corner occurrences. For two fixed end-edge colors \(u,v\), put
\[
 F_a(u,v)=\sum_{\substack{\text{internal}\\\text{edge colors}}}
       \prod_{\text{crossings }t}R_t
       \prod_{\text{all edges }e}q^{j_e}.             \tag{2}
\]
The two end edges also occur in the last product. This is the original
fixed-end source when \(u=v=0\). When four distinct regions occur at
every crossing, its charge conventions agree literally with [K,
(3.1)--(3.6)]. With repeated regions, (1),(2) specify the
occurrence-level convention explicitly, rather than identifying
different corner charges by the name of their face.

## 2. A planar potential lemma

Suppose corner values \(\delta_c\) sum to zero at each crossing and
around each bounded face, and vanish at every unbounded-face corner.
There are edge values \(x_e\) such that at each corner from a half-edge
\(e\) to its next counterclockwise half-edge \(e'\),
\[
                         \delta_c=x_{e'}-x_e.        \tag{3}
\]
They can be chosen zero on both end edges.

To prove this integrally, replace each crossing by a small circle.
Its four incident half-edges meet that circle at four separate vertices;
connect consecutive vertices by the four circle arcs. Keep the
original graph edges between these circles and the two degree-one
vertices. Give an original edge increment zero and an oriented circle
arc increment \(\delta_c\), with sign reversed on the oppositely
oriented arc. This is a connected plane graph. Its bounded faces are
the small crossing disks and the original bounded regions, with the
same corner occurrences. The assumed sums say that the increment
around every bounded-face boundary is zero.

The oriented boundaries of the bounded faces generate the integral
cycle group of a connected plane graph. One direct proof takes any
simple cycle and sums the faces inside it: interior edge occurrences
cancel and its boundary remains. Split any closed edge walk at its
repeated vertices into simple cycles, canceling immediate backtracks.
Bridges contribute nothing. This proves the assertion for loops and
repeated face boundaries as well. It uses only integer sums, so it
remains valid after reduction modulo any \(N\).

The increment therefore integrates along paths to a vertex potential,
independent of the chosen path. Its value is the same at both ends of
each original edge, giving \(x_e\), and its circle steps give (3).
The outer boundary walk visits both degree-one vertices. Every
increment along that walk is zero: original edges have zero increment
and outer corners have \(\delta_c=0\). The two end values are equal.
Subtract their common value to make both zero. Connectivity also shows
that this normalized potential is unique.

## 3. Exact charge change, with its phase

Let \(a\) and \(a'\) be admissible assignments. Their corner difference
\(\delta=a'-a\) satisfies the potential lemma. Choose its normalized
edge values \(x_e\), and replace every edge color by
\(j'_e=j_e+x_e\). The end colors are unchanged.
At one crossing, equation (3) says
\[
 a'-a=x_j-x_i,\quad b'-b=x_k-x_j,\quad
 c'-c=x_l-x_k,\quad d'-d=x_i-x_l .
\]
All four arguments of \(W\) in (1) are unchanged, as elements of
\(\mathbb Z/N\mathbb Z\). Consequently their integer residues and theta
supports are unchanged as well. The explicit prefactor gives
\[
 R(i+x_i,j+x_j,k+x_k,l+x_l\mid a',b',c',d')
       =q^{-x_i-x_k}R(i,j,k,l\mid a,b,c,d).            \tag{4}
\]
In particular this comparison loses no zero entry or endpoint residue.

The color change is a bijection of the finite internal summation set.
Each edge factor in (2) supplies \(q^{x_e}\). Multiplying (4) proves
the identity of the entire open arrays
\[
 \boxed{F_{a'}(u,v)=q^{\Omega(x)}F_a(u,v),\qquad
 \Omega(x)=\sum_e x_e-
       \sum_{\text{crossings }t}
            (x_{\text{first under-half-edge}}+
             x_{\text{second under-half-edge}}).}    \tag{5}
\]
The second sum counts half-edge occurrences; a loop can contribute
twice. This is an explicit unit independent of \(u,v\) and of the
summation colors. No primality, oddness or division modulo \(N\) is
required.

Thus an admissible sector assignment may be changed with both end
colors fixed, while retaining the single root phase in (5). The
conclusion concerns the whole open array, so it also retains a
specified closing functional once that functional is applied to the
same end coordinates. It does not identify a different cap functional,
prove scalarity of the open array, establish a geometric contribution,
or supply a large-level lower bound.

## Complete direct source

- [K] R. M. Kashaev, *A Link Invariant from Quantum Dilogarithm*,
  [q-alg/9504020v1](https://arxiv.org/pdf/q-alg/9504020).
  Only the finite planar definitions are used. The complete ten-page
  primary text was read. Local PDF:
  research_archive/finite-source-identification-2026-11-01/md-kashaev-normalization-critical-audit/kashaev1995.pdf,
  SHA256
  0baef40fa9934c9119af2c67252f8032e288c884da72eeaecf405bf91569cda9.
  The complete text extraction has SHA256
  24932c5d5eab93684888a6149518d710ed7ad48fe3674522c8adaa38a0b62cb1.

No mathematical programs or numerical experiments were used.
