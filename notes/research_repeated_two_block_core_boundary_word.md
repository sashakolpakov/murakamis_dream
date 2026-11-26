# The core handlebody and its full boundary word

Research deduction, 8 November 2026. No numerical evaluation,
combinatorial execution or saved-certificate replay is used.

The [five-core face theorem](research_repeated_two_block_five_core_faces.md)
constructs a complete positive ten-cell double. This note records
its core's exact handle cancellation and based boundary words.
The full boundary homomorphism, not merely its traces, is the
reflected original half-word. A separating compression disk and the
two primitive annular sides identify the core as that rational-tangle
exterior. The closing map differs from the original physical turn by
a specified half-lattice translation; an actual extending tangle
automorphism removes that discrepancy. The resulting identification
is of unmarked knot exteriors, allowing orientation reversal. No
longitude or transported ribbon identification is claimed.

## 1. Dual handles and their literal relators

Retain exactly the five tetrahedra and face pairings from that
theorem. Choose the four tree faces
\[
                         A-C,\quad A-B,\quad B-E,\quad B-D.
 \tag{1}
\]
The remaining oriented face generators are
\[
 X:C0\to D3,\qquad Y:C1\to E1,\qquad
 Z:D1\to E2,\qquad W:D2\to E0 .
 \tag{2}
\]
Words act as transformations, so the rightmost map is applied
first. All tree face maps have been identified with the identity.
The two internal edge cycles in equation (4) of the face theorem
give precisely
\[
                    Y=1,\qquad
            W^{-1}ZXY^{-1}WZ^{-1}=1 .
 \tag{3}
\]
For the second cycle its successive non-tree traversals are
\(Z^{-1},W,Y^{-1},X,Z,W^{-1}\), in path order.
Consequently
\[
                 X=Z^{-1}WZW^{-1},\qquad
                    \pi_1(\mathcal C)=\langle Z,W\rangle .
 \tag{4}
\]

There is a topological handle conclusion here. Truncating the
two annular ideal ends gives the compact core. Its dual handle
decomposition has five zero-handles, eight one-handles and
the two two-handles for the internal edges; there is no
interior vertex and no three-handle. The tree (1) combines
the zero-handles to one. The first attaching curve in (3)
passes through the \(Y\)-handle once and no other handle.
Cancel that one/two-handle pair, using it to remove the
single \(Y^{-1}\) in the second attaching curve. The remaining
attaching curve passes through \(X\) once. Cancel that pair
as well. These are geometric once-crossing handle cancellations,
not a deduction from freeness of the group alone. What remains
is one zero-handle and two one-handles. Thus the compact core
is a genus-two handlebody, with free basis \(Z,W\).

The cancellations establish its unmarked topology. They do not
erase the four-punctured boundary or its two annular sutures.

## 2. Four actual outward boundary paths

Use the old puncture names \(a_0,b_0,c_0,d_0\) from the face
theorem. On tetrahedron \(A\) these are
\[
                     (A0,A1,A3,A2)=(a_0,b_0,c_0,d_0).
 \tag{5}
\]
Choose the source-ordered boundary labels
\[
                        (a,b,c,d)=(d_0,b_0,c_0,a_0).
 \tag{6}
\]
The two boundary faces \(A2,A3\) give a common boundary base
tree for all four small outward loops. Reading the edge fans
with this base tree gives
\[
 \boxed{\quad
 a=Z,\qquad b=X^{-1}W^{-1}X,\qquad
 c=WX,\qquad d=(XZ)^{-1}.
 \quad}
 \tag{7}
\]
Here the same letters denote their based group words.
The original inverse product is retained:
\[
                 dcba=(XZ)^{-1}(WX)(X^{-1}W^{-1}X)Z=1.
 \tag{8}
\]

For a direct path audit, write \((A,i)\) for a vertex of a
tetrahedron, and \(A i\to B j\) for a face traversal only
when explicitly indicated. The loop \(a\), based at the
\((A,2)\) link triangle, is
\[
 (A,2)\to(B,3)\to(D,3)\to(E,0)\to(C,0)\to(A,2).
 \tag{9}
\]
Its faces are \(A1\to B1,\ B2\to D0,\ D1\to E2,\
E1\to C1,\ C2\to A0\). This is the literal \(d_0\)-annulus
loop already used to prove completeness. Its only nontrivial
map is \(Z\).

For \(b\), the path is
\[
 (A,1)\to(C,1)\to(D,1)\to(B,1)\to(E,1)
                        \to(D,1)\to(C,1)\to(A,1).
 \tag{10}
\]
Its non-tree maps in path order are \(X,W^{-1},X^{-1}\).
For \(c\), use
\[
 (A,3)\to(C,3)\to(D,0)\to(E,2)\to(B,2)\to(A,3),
 \tag{11}
\]
whose non-tree maps are \(X,W\).
Finally the reverse of the path
\[
 (A,0)\to(B,0)\to(D,2)\to(E,3)\to(C,2)
                         \to(D,2)\to(B,0)\to(A,0)
 \tag{12}
\]
is \(d\); the forward maps are \(Z,X\).
All unspecified maps in (9)--(12) are tree maps or \(Y=1\).
These paths are the fans at the six boundary edges from
equation (3) of the face theorem. In particular (10)--(12)
are small puncture loops with their base paths retained,
not arbitrarily chosen conjugates of parabolics.

The induced boundary orientation gives the order (8).
The annular pairings are \((a,d)\) and \((b,c)\), in
agreement with the link inventory. Their core words are
conjugate to \(Z\) and \(W\), respectively.

## 3. The exact inverse Hurwitz reduction to the original cap

Use the actual positive crossing on an ordered quadruple,
\[
 R(a,b,c,d)=(a^{-1}ba,a,c,d),\qquad
 R^{-1}(a,b,c,d)=(b,bab^{-1},c,d),
 \tag{13}
\]
as proved by the based side paths in
[the original two-flip attachment, equation (17)](research_newton_crossing_two_flip_attachment.md).
Let the physical turn transport the four boundary labels cyclically:
\[
             T(a,b,c,d)=(b,c,d,a),\qquad
             T^{-1}(a,b,c,d)=(d,a,b,c).
 \tag{14}
\]
Unlike its reduced Newton character, the labelled turn in
(14) has its literal fourth-order puncture permutation.
No physical half-turn has been set equal to the identity.

Apply the inverse reflected half-word
\[
                          R^2T^{-1}R^{-2}T^{-1}
 \tag{15}
\]
to (7). The first turn and the two inverse crossings give
\[
 \left(X^{-1}Z^{-1},\ X^{-1}ZX,\
                         X^{-1}W^{-1}X,\ WX\right).
 \tag{16}
\]
The second inverse turn gives
\[
 \left(WX,\ X^{-1}Z^{-1},\
                         X^{-1}ZX,\ X^{-1}W^{-1}X\right).
 \tag{17}
\]
After \(R^2\), its second and third entries are inverse.
Indeed the second entry is
\[
 X^{-1}W^{-1}X^{-1}Z^{-1}WX=X^{-1}Z^{-1}X,
 \tag{18}
\]
using \(Z^{-1}WZ=XW\). Since all operations preserve the
ordered product, the first and fourth entries are inverse
as well. The full final quadruple is exactly
\[
          X^{-1}\,(W,\ Z^{-1},\ Z,\ W^{-1})\,X.
 \tag{19}
\]
The two cap generators \(W,Z^{-1}\) form a free basis.
Thus the full based boundary homomorphism (7) is that of
the reflected original rational half-word
\[
                            \overline F=T R^2T R^{-2},
 \tag{20}
\]
with its actual free inverse-pair cap. This is an identity
in the free group (4), before any parabolic matrix
specialization. It is stronger than equality of a character
polynomial or of the single cap trace.

The reflected word (20) is consistent with the documented global
orientation reversal in the raw subdivision theorem. It follows
here from the full free boundary words, without a parabolic
specialization or an inference from traces.

## 4. What the explicit closing map does to slopes

The doubled map \(\tau\) from equation (13) of the face
theorem is orientation preserving as a self-map of the
oriented core boundary. For example \(A2\) has orientation
\((a_0,b_0,c_0)\), while \(B3\) has its negative, and
\(\tau\) swaps \(a_0,b_0\). It is an orientation-reversing
gluing only when the second core is given the opposite
orientation. In the labels (6), it interchanges \(b,d\)
and fixes \(a,c\).

There is an exact slope calculation which retains this
distinction. Let \(\mathcal A\) be the frontier of a small
neighborhood of boundary edge \(r\), joining \(a,b\), and
\(\mathcal B\) the corresponding frontier for edge \(s\),
joining \(b,c\). Choose the usual adjacent-arc representatives;
their sphere intersection is two, so their lifts to the
branched torus cover give a homology basis with intersection
one. The actual edge map is
\[
                       r\leftrightarrow u_0,\qquad
                       s\leftrightarrow v .
 \tag{22}
\]
The arcs \(u_0,s\) are disjoint and join complementary
puncture pairs. Their neighborhood frontiers are isotopic
through the remaining annulus. The same is true for \(v,r\).
Thus \(\tau\) exchanges the actual two basis slopes
\(\mathcal A,\mathcal B\), not just their endpoint partitions.
As it preserves orientation, its torus linear part is
\[
                 \pm S,\qquad
                 S=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
 \tag{23}
\]
The deck sign does not affect a pillowcase slope.

In the physical convention of
[the rational-corridor normal form, equations (1)--(2)](research_definite_rational_corridor_normal_form.md),
the reflected half-word has disk-slope vector
\[
 v=\begin{pmatrix}-2\\5\end{pmatrix},\qquad
 Sv=\begin{pmatrix}-5\\-2\end{pmatrix}.
 \tag{24}
\]
For example \(T R^2T R^{-2}\) has linear matrix
\(\left(\begin{smallmatrix}1&-2\\-2&5\end{smallmatrix}\right)\)
up to deck sign, and acts on the through-cap vector
\((0,1)^T\). The unimodular normalization
\[
 \begin{pmatrix}5&2\\2&1\end{pmatrix}v
   =\begin{pmatrix}0\\1\end{pmatrix},\qquad
 \begin{pmatrix}5&2\\2&1\end{pmatrix}Sv
   =\begin{pmatrix}-29\\-12\end{pmatrix}
 \tag{25}
\]
gives the candidate two-bridge slope \(29/12\), reflected
from \(29/17\).

Equation (25) is not, by itself, a knot-exterior identification.
The original physical turn has affine lift
\[
                          (x,y)\longmapsto(-y,x+1/2),
 \tag{26}
\]
not merely the linear part \(S\). Its puncture permutation
is a four-cycle, whereas \(\tau\) fixes two punctures.
Consequently their difference includes a nontrivial
half-lattice translation. The exact rational-corridor theorem
explicitly retains such proper half-turns on arbitrary attached
tangles. Sections 5--6 identify the present particular tangle and
construct the required extension.

## 5. The relative rational-tangle extension

Pull the boundary marking back by the actual inverse word (15).
The compact boundary is the four-holed sphere \(P\) together with
two annuli pairing \((a,d)\) and \((b,c)\); the permutation of
(15) preserves these two pairs as a set. Let \(\gamma\subset P\)
be the standard simple curve separating \(b,c\) from \(a,d\).
Its based word is \(cb\), up to a common conjugation and possible
inversion. Equation (19) proves that it is nullhomotopic in the
core. It is essential on the compact genus-two boundary and
separates that boundary into two once-punctured tori.

We use the standard boundary consequence of Dehn's lemma: a simple
nullhomotopic curve on the boundary of a three-manifold bounds a
properly embedded disk. The precise external topological input is
C. D. Papakyriakopoulos,
[“On Dehn's Lemma and the Asphericity of Knots,”
PNAS 43 (1957), 169--172, Dehn's lemma on page 169](https://doi.org/10.1073/pnas.43.1.169).
Its hypothesis is a nullhomotopy with no singularities on a boundary
annulus. In the present boundary application, collar \(\gamma\)
into the interior first and take the remaining nullhomotopy beyond
that collar. The lemma supplies an embedded disk with the same
boundary; the boundary collar puts its interior in the interior
of the manifold. This standard theorem is an input here, not a
new consequence of the word reduction.

Thus \(\gamma\) bounds a proper disk \(\mathcal D\). Its boundary
separates the genus-two boundary surface, so the disk separates the
handlebody. Cutting a handlebody along a proper disk gives
handlebodies: cut also along a complete meridian system, remove
circular intersections by innermost-disk surgery, and successively
cut along outermost intersection arcs; the resulting pieces are
balls. Here each new boundary is a torus, so the two pieces are
solid tori. This uses the geometric handlebody established in
Section 1, not freeness of an unspecified three-manifold group.

Each original annulus lies on its corresponding solid torus.
Its core represents, up to conjugation and inversion, one of the
free generators \(W,Z^{-1}\) in (19). It is therefore a generator
of that solid torus's fundamental group, rather than a proper
power: the inclusions of the two solid tori are the two free
factors, and a proper power cannot be a member of a free basis.
Consequently each annulus has primitive longitudinal slope.

A solid torus with such an annulus is the exterior of a trivial
proper arc in a ball. Explicitly, attaching a two-handle on that
annulus cancels its single one-handle; the co-core is the trivial
arc. Joining the two resulting balls along the disk \(\mathcal D\)
gives the standard trivial two-arc ball. This also proves the
required relative statement on \(P\). After aligning \(\gamma\)
and its disk, the prescribed maps on the two pairs of pants extend
over their capping disks. The unspecified maps on the retained
annuli may be twisted by an integer so that the two torus meridians
match; this is possible because each annular core is primitive.
The resulting torus maps extend over the solid tori. No adjustment
to the prescribed four-holed-sphere map is required.

We have thus proved, with the labels (6), an identification of
unframed tangle pairs
\[
            (\mathcal C,P)\cong
            \operatorname{Exterior}\bigl(\overline F(I)\bigr),
       \qquad \overline F=T R^2T R^{-2}.
 \tag{27}
\]
The annular twists used in this argument are not a claim about a
preferred ribbon framing or a chosen longitude.

## 6. The finite translation extends over this actual core

Use the precise original pillowcase labels from
[the marked collar proof, equations (5)--(7)](research_marked_degree_two_tangle_moves.md):
\[
 a=(0,0),\quad b=(1/2,0),\quad
 c=(1/2,1/2),\quad d=(0,1/2).
 \tag{28}
\]
They agree with (13)--(14): the bottom crossing exchanges \(a,b\),
and the physical turn sends old \(a,b,c,d\) to \(d,a,b,c\).
The slopes of \(r,s\) are the horizontal and vertical basis used
in (23). In these coordinates the simplicial closing map has
representative
\[
 \widetilde\tau(z)=Sz,\qquad
 \widetilde T(z)=Sz+(0,1/2),\qquad
                  \tau T^{-1}=H_{(0,1/2)}=K .
 \tag{29}
\]
Here \(\tau\) is the closing map of the face theorem, not the
rotation denoted \(T^2\) in the general corridor notation.

For completeness, (29) uses the full mapping class. The map
\(\tau\) exchanges the two actual basis curves by (22), and
fixes \(a,c\) while exchanging \(b,d\). After the linear part
\(S\) is removed, a four-punctured-sphere map preserving those
two intersecting slope curves is one of the four pillowcase
half-translations. This elementary kernel description follows
by cutting along the curves: after its action on the four
punctured regions is removed, the map is isotopic to the identity
on their boundary arcs and then on each disk. A nonzero
half-translation has a double-transposition puncture permutation,
so none fixes \(a\). The remaining translation is therefore zero,
which proves the first identity in (29), not only its linear part.

Here is the extension needed to use the last identity in (29).
In a round ball take the trivial tangle to be two parallel chords
at \(x=\pm c,\ y=0\), for a fixed \(0<c<1\). The three rotations
through \(\pi\) about the coordinate axes preserve that pair of
arcs and induce the three nonzero pillowcase half-translations.
They are the proper rotations retained in the original marked
collar proof and in the rational-corridor theorem, Section 3.
In particular every
\[
             H_\delta,\qquad
        \delta\in(\tfrac12\mathbb Z^2)/\mathbb Z^2,
 \tag{30}
\]
extends over the trivial tangle as an unframed tangle-pair
automorphism, with its actual endpoint permutation.

More generally let a rational tangle be \(F(I)\), with physical
boundary word \(\widetilde F(z)=G_Fz+v_F\). Choose
\(\epsilon=G_F^{-1}\delta\) modulo \(\mathbb Z^2\). Conjugating the
preceding ball automorphism by the actual ball map \(F\) gives
an automorphism of \(F(I)\), and its boundary mapping class is
exactly
\[
 \widetilde F H_\epsilon\widetilde F^{-1}(z)
                  =z+G_F\epsilon=z+\delta.
 \tag{31}
\]
Thus all four half-translations extend over every rational
tangle. The affine translation \(v_F\) cancels in (31); no
endpoint permutation has been discarded. If a representative
differs from the specified boundary map by an isotopy, extend
that isotopy over a collar to obtain the specified map itself.

For the particular \(\overline F\) in (27), its linear part is
\(\left(\begin{smallmatrix}-1&2\\2&-5\end{smallmatrix}\right)\),
which acts as the identity on the half-lattice quotient. Hence
the extension of \(K\) in (29) can be chosen as
\(\overline F K\overline F^{-1}\). Applying its inverse to the
target core changes the gluing map \(KT=\tau\) to \(T\).
We obtain an actual homeomorphism of the two unmarked doubles,
\[
      \mathcal C\cup_\tau\overline{\mathcal C}
                   \cong \mathcal C\cup_T\overline{\mathcal C}.
 \tag{32}
\]
This absorption is specific to the now proved rational cores.
It does not remove a rotation on an arbitrary outside branch.

## 7. The resulting unmarked exterior

After (27) and (32), both pieces are literal rational-tangle
exteriors with their separating disk slopes. Apply the same
normalizing boundary map in (25) to the two pieces. One tangle
becomes \(I\), and the other has vector \((-29,-12)\), or
\((29,12)\) after the harmless deck sign. The actual rational
tangle classification in
[the corridor-compression theorem, Section 3](research_rational_corridor_compression.md)
includes the stabilizing curls and all half-translations.
It therefore identifies this gluing with the two-bridge closure
of fraction \(29/12\), not merely with a character of that closure.

The original capped list \((2,4,2,3)\) has fraction \(29/17\) by
equations (22)--(23) of the
[original repeated-block source](research_repeated_reflected_block_positive_moments.md).
The relation to the preceding fraction can be checked with the
same cap convention. Mirroring sends the vector \((29,17)\) to
\((-29,17)\), equivalent to \((29,-17)\). The lower shear
\(\left(\begin{smallmatrix}1&0\\1&1\end{smallmatrix}\right)\),
which extends over the trivial cap by its removable cap curl,
sends this to \((29,12)\). Thus \(29/12\) is the mirror closure
of the specified original \(29/17\) diagram.

**Theorem.** The complete positive ten-cell double of the face
theorem is homeomorphic, allowing orientation reversal, to the
exterior of the original capped knot with list \((2,4,2,3)\).

The proof supplies the unmarked exterior identification needed to
compare its hyperbolic volume with the already calibrated source
regulator. It asserts neither a preferred-longitude identification
nor equality of transported ribbons. It concerns this one actual
capped knot, not arbitrary mixed blocks or arbitrary short clusters.
