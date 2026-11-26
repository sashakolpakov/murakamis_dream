# Pure page sewing and the decorated half-twist collar

1 November 2026. Private derivation.

This note uses the actual two-octahedron face maps of
[the local nonparabolic chart](md-nonparabolic-two-octahedron-pure-adapter.md).
It keeps the original cyclic page order and the two puncture
eigenflags. The global preferred main-longitude concatenation is a
separate calculation: local seam compatibility alone does not prove
that longitude formula.

## 1. The two ends of one edge

Write \(m=M^2\). At the first circle, whose longitude parameter
is \(Q\), the full doubled incoming and outgoing triangles have
the following cyclic edge ratios:
\[
 I(m,Q)=(-m/Q,-Q,-1/(mQ)),\qquad
 O(m,Q)=(-mQ,-1/Q,-Q/m).                                    \tag{1}
\]
The original pure matching sends outgoing \((A,R,0)\) to
incoming \((A',1,\infty)\). Consequently
\[
                  O_j(m,Q)I_{2-j}(m,Q)=1
                  \qquad (j=0,1,2).                        \tag{2}
\]
These are complex ratios, so the statement includes the shear.
The three ordered vertices fix the first triangle map, and the
ratios fix the second triangle. This proves compatibility of the
entire marked two-triangle disk side.

The same edge chart at its other circle has incoming triangle
\((B,R,1)\) and outgoing triangle \((B,\infty,0)\).
With the notation of the local chart, the six neighboring third
vertices developed through the white faces are
\[
 W_3^{-1}(1),\ W_2^{-1}(b),\ W_1^{-1}(S),\qquad
 W_1^{-1}(0),\ W_0^{-1}(b),\ W_3^{-1}(\infty).
                                                                  \tag{3}
\]
Their ratios, on \(R=R_w\), are
\[
 I(m^{-1},P)=(-1/(Pm),-P,-m/P),\qquad
 O(m^{-1},P)=(-P/m,-1/P,-Pm).                                \tag{4}
\]
Thus an edge reverses the native orientation parameter at its
second end. This is the actual reversal of the equatorial cyclic
order in the turned second leaf. It is not a replacement of the
positive global main meridian by its inverse.

## 2. An arbitrary finite pure page tree

Let the original tree have no retained odd seam. Choose one
bipartition sign \(\sigma_v\in\{1,-1\}\), so adjacent
vertices have opposite signs. At an edge with first endpoint
\(v\), use the local chart with \(m_e=m^{\sigma_v}\).
Its other endpoint then has parameter \(m^{\sigma_w}\) by
(4). Every incident page at a fixed vertex therefore has the
same table \(I(m^{\sigma_v},Q_v),O(m^{\sigma_v},Q_v)\).

For each circle, sew these pages in the original cyclic order,
using the three ordered punctures in (2). Start with a terminal
edge and use the literal left and right insertion operations of
[the ordered page decomposition](md-all-circle-ordered-octahedron-page-decomposition.md),
equations (5) and (7a). Every insertion attaches the doubled
two-triangle disk side just described. Formula (2) verifies the
new seam, and no preceding seam is altered. The actual turns
and any half-turn frame decoration carry all the labels and maps.
No open-tangle commutativity is used.

This proves that the charts assemble on every finite pure ordered
page tree. The endpoint-inverted parameter causes no ambiguity in
the source wire: its equation depends on \(m+m^{-1}\), and its
branch through \(X=i\) is unique. The same \(X_e\) is therefore
used at the two ends. The auxiliary meridian increment of edge
\(e\) at circle \(v\) is
\[
                         \frac{Q_v+X_e}{1+Q_vX_e},           \tag{5}
\]
and its disk longitude has similarity \(Q_v^2\).
Multiplication of the successive increments is in the original
circle order. Since each is measured in that same eigenflag,
their similarities multiply without an additional scalar.

The maps give an actual nearby representation of the original
pure exterior. Indeed the face returns within every edge block
are the six identities in the local chart, and the newly created
page-edge returns are (2). These are precisely the relations
obtained by the reversible projection/disk cut. Positive
tetrahedral shapes persist for a sufficiently small neighborhood
depending on the fixed tree.

### Positive main meridians and their flags

The bipartition signs describe native page coordinates. They are
not extra choices of the knot orientation. At a main boundary
vertex, take the actual small oriented meridian word supplied by
the physical collar. Its local derivative at the displayed ideal
point is \(m\) or \(m^{-1}\), depending on whether that native
meridian is the positive one or its inverse. Transport the word
and its eigenflag together through each face map.

For a main component, choose its orientation at one segment.
The same oriented small meridian propagates by the actual
annular collar conjugacies. The geometric ideal flag propagates
by those same conjugacies, so its chosen eigenvalue stays fixed.
There is no freedom to exchange it after returning around the
component: for generic \(M\), the peripheral longitude commutes
with a nonparabolic meridian and hence preserves both eigenlines.
At \(M=1\) use the analytic limit of this transported flag.
Thus one can record which global component orientation makes
the displayed flag the \(M^{-1}\) source flag. For a knot this
is one global orientation choice, not a separate reset at each
edge. A comparison with an already specified positive
meridian must make this initial choice explicitly.

This argument identifies the local auxiliary products for the
pure tree. It does not yet compute the global preferred main
longitude from them; that still requires its actual boundary
path and framing.

## 3. Why the old odd three-point maps cannot be inserted unchanged

In the local chart keep the pure white maps \(W_j\) fixed.
Let \(A_{\mathrm o}\) and \(B_{\mathrm o}\) be the unique
three-point maps with the old odd permutations
\[
 (A,\infty,1)\mapsto(a,S,0),\qquad
 (A,R,0)\mapsto(a,\infty,1).
\]
They are
\[
 A_{\mathrm o}=
 \begin{pmatrix}S&-S\\1&S(A-1)/a-A\end{pmatrix},\qquad
 B_{\mathrm o}=
 \begin{pmatrix}(a(A-R)+R)/A&-R\\1&-R\end{pmatrix}.             \tag{6}
\]
The first original odd edge return is not trivial:
\[
 W_0^{-1}B_{\mathrm o}W_2^{-1}A_{\mathrm o}:
             z\longmapsto m^{-2}z+(1-m^{-2})A.              \tag{7}
\]
The second return is likewise nontrivial; the third,
\(W_1^{-1}B_{\mathrm o}W_3^{-1}A_{\mathrm o}\), is
projectively the identity. In particular the two defects vanish
at \(M=1\), which is why the old parabolic calculation did not
detect them.

Equation (7) is an obstruction to keeping both the pure white
charts and the old odd vertex assignment. It is not an
obstruction to the half-twist homeomorphism. That homeomorphism
must transport the puncture eigenflags and the adjacent charts.

## 4. A regular matrix implementing the actual positive braid collar

Let \(a,b\in\mathrm{SL}_2(\mathbb C)\) be the two ordered
puncture meridians in the physical braid frame. They have the
same trace \(M+M^{-1}\). The original positive crossing
convention is
\[
             (a,b)\longmapsto(a^{-1}ba,a),\qquad P=ba.
                                                                  \tag{8}
\]
This is the literal Wirtinger rule of
[the marked braid calculation](/Users/sasha/volume-conjecture/notes/marked_braid_holonomy.md),
section 5. In particular the preserved product is \(ba\),
not \(ab\).

Put
\[
                            H=P^{-1}-I.                     \tag{9}
\]
Near the auxiliary complete lift \(P\), whose trace is \(-2\),
\(\det H=2-\operatorname{tr}P\) is near \(4\).
There is no singular diagonalizing frame.
The Cayley--Hamilton identities for \(a,b\), with their equal
traces, give
\[
 (P-I)a=b(P-I),\qquad
 (P-I)^2=(\operatorname{tr}P-2)P.
                                                                  \tag{10}
\]
Consequently \(H\) is projectively \((P-I)^{-1}\), it
commutes with \(P\), and
\[
              HaH^{-1}=a^{-1}ba,\qquad HbH^{-1}=a.           \tag{11}
\]
This is the exact positive collar rule (8). Its inverse realizes
the negative crossing.

Suppose the selected auxiliary flag has \(P\)-eigenvalue
\(-Q\). The eigenvalue ratio of \(H\) at that flag is
\[
                    \frac{-Q^{-1}-1}{-Q-1}=Q^{-1}.          \tag{12}
\]
Thus composing a pure auxiliary meridian with \(H^\epsilon\)
changes its similarity by \(Q^{-\epsilon}\). It keeps the
disk longitude \(P\) and its chosen flag.

There is an independent matrix calibration against the original
geometric collar. In the local chart set
\[
                 P=m^{-1}W_2^{-1}W_0.                       \tag{13}
\]
This is the determinant-one disk word and has selected
eigenvalue \(-Q\). At \(m=1\), for all nearby \(E,Q\),
not just at the complete point,
\[
           S_v^{-1}(P^{-1}-I)=W_0^{-1}B_{\mathrm o}
                        \quad\text{projectively}.           \tag{14}
\]
The right side is the original physical positive-\(R\)
meridian, by section 6 of
[the marked mask filling proof](/Users/sasha/volume-conjecture/notes/actual_conway_general_mask_marked_filling.md).
Its inverse crossing is the other old odd path.
Equations (8) and (14) fix both the braid sign and the actual
copy/collar marking; the sign has not been chosen from a desired
source formula.

### The full ordered boundary groups in the actual edge chart

Let \(N_j=W_{j-1}^{-1}W_j\), with indices modulo four.
Their determinant-one lifts, in the order of the original
equatorial boundary, are
\[
 A_g=M^{-3}N_3,\qquad B_g=MN_0,\qquad
 C_g=MN_1,\qquad D_g=MN_2,\qquad
                    A_gB_gC_gD_g=I.                        \tag{14a}
\]
Each trace is \(M+M^{-1}\). These lifts follow from
\(\det W_0=L,\det W_1=L/m,\det W_2=L/m^2,\det W_3=Lm\).
They include the native loop directions, which need not all be
positive main meridians.

The pure edge returns give the following complete boundary
intertwinings:
\[
\begin{array}{c|c|c|c|c}
 \text{circle}&(a,b)\text{ on the input side}
 &(a',b')\text{ on the output side}&C_0&P=ba=b'a'\\ \hline
 v&(B_g,A_g)&(C_g^{-1},D_g^{-1})&S_v^{-1}&A_gB_g\\
 w&(B_g^{-1},C_g^{-1})&(A_g,D_g)&S_w^{-1}&(B_gC_g)^{-1}.
\end{array}                                                    \tag{14b}
\]
Here \(C_0aC_0^{-1}=a'\) and \(C_0bC_0^{-1}=b'\).
For example the first row is equivalent to
\[
 S_v C_g S_v^{-1}=B_g^{-1},\qquad
 S_v D_g S_v^{-1}=A_g^{-1}.
                                                                  \tag{14c}
\]
The second is equivalently
\(S_w A_gS_w^{-1}=B_g^{-1}\) and
\(S_w D_gS_w^{-1}=C_g^{-1}\).
These are consequences of the full white/shaded returns;
they may also be checked by direct multiplication of the local
matrices. The product columns agree because
\(D_g^{-1}C_g^{-1}=A_gB_g\) and
\(D_gA_g=(B_gC_g)^{-1}\).

The disk convention \(P=ba\) is therefore explicit at both
ends, including the inversions caused by the turned second
circle. The same table transports under the actual conjugating
frames in a tree; an orientation reversal transports the whole
tuple and its disk word. It does not silently replace \(P\)
by a different boundary product.

For the positive braid put \(H=P^{-1}-I\) in the input
frame. Then \(C_+=C_0H\) satisfies
\[
\begin{aligned}
 C_+aC_+^{-1}&=a'^{-1}b'a',\\
 C_+bC_+^{-1}&=a',\\
 C_+PC_+^{-1}&=P .
\end{aligned}                                                    \tag{14d}
\]
For the negative braid use \(H^{-1}\) and the inverse
automorphism. Thus the construction checks both generators of
the actual twice-punctured disk and its outer boundary word;
it is stronger than checking a peripheral similarity or three
traces. Formula (14) fixes the positive crossing in the
original physical convention.

## 5. The opposite-eigenflag qualification

Let \(F_a,F_b\) be the two displayed puncture flags, with
eigenvalues \(\lambda_a,\lambda_b\). The natural braid output
flags for (8) are
\[
                          (a^{-1}F_b,F_a).                  \tag{15}
\]
Their eigenvalues are \((\lambda_b,\lambda_a)\), since
the strands have exchanged positions. By contrast,
\((HF_a,HF_b)\) has eigenvalues
\((\lambda_a,\lambda_b)\) on that same output tuple.
If the selected eigenvalues agree, the two descriptions coincide
by uniqueness of the relevant eigenline. If they differ, use
\(H\) on the opposite input eigenlines to obtain (15).
At a native pure circle the geometric flags on its two main
punctures have opposite selections \(M^{-1},M\).
The qualification is therefore essential.

This identifies the error in an unqualified instruction to
transport both displayed flags by \(H\). The intertwiner is
correct; the displayed decorated triangle needs the accompanying
Weyl change. The two eigenlines coalesce at the parabolic point,
so the complete figure alone cannot distinguish the operations.

## 6. Representation gluing followed by global decoration

The following construction keeps that distinction explicit.
First perform the actual collar gluing at the level of
representations; then select the geometric eigenflags on the
resulting original link group.

The half-twist is the actual mapping cylinder of the two-punctured
disk, fixing its outer boundary. Its two boundary generator
tuples are related by (8). If \(C\) is the pure boundary
intertwiner, replacing it by \(CH^\epsilon\), with the side
and composition order fixed by (14), supplies the new
intertwiner. Equation (11) verifies the two puncture relations;
\([H,P]=0\) verifies the outer disk-boundary relation. These
are the generators and relation of the twice-punctured disk.
The van Kampen presentation of that actual cut therefore gives
the representation of the reglued exterior. It uses the one
distinguished disk seam at that circle, once.

Apply the operation in every original circle's transported
puncture frame. The other cyclic page seams remain those of
section 2. At this stage no assertion is made that the old
pure ideal vertices still provide the correct decoration.

For each resulting main component, choose its actual positive
meridian and its \(M^{-1}\) eigenflag. At a corner whose
native loop is the inverse, take the corresponding \(M\)
eigenflag. Transport these choices by the original paths in the
completed cut. Peripheral commutation makes the choice independent
of a peripheral path. Keep the already selected disk-longitude
flag on each auxiliary circle.

These choices are holomorphic near the complete structure.
For example, for a noncentral matrix
\(\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\)
with \(b\ne0\), an eigenline with prescribed holomorphic
eigenvalue \(\lambda\) is represented by
\((b,\lambda-a)\). The opposite eigenline is obtained by
replacing \(\lambda\) by \(\lambda^{-1}\).
Both approach the unique parabolic flag at the complete point.
A change of coordinate handles a chart with \(b=0\).
The same argument applies to the selected auxiliary eigenvalue
\(-Q\).

Develop the original topological ideal triangulation from these
global flags and the constructed representation. The map of
each triangle is the unique map of its transported ordered
triple. Adjacent white maps must be rebuilt in this way;
(7) shows why they cannot generally be retained unchanged.
Equivariance gives every edge return. At the complete parameter,
(14) and the original collar convention identify the actual odd
development. Its positively oriented tetrahedra therefore remain
positive in a sufficiently small neighborhood of the fixed
finite tree. This is a local decorated representation
construction, not a global completeness assertion for a
nonparabolic main cusp.

The tuple with \(P=ba\) is exactly (14b), transported in the
original physical collar. The positive main loops are chosen
in the completed cut. For the canonical four-segment traversal,
they are \(C_g,B_g^{-1},A_g,D_g^{-1}\) at
\(\infty,0,R,1\), respectively; all four select their geometric
corner with eigenvalue \(M^{-1}\). A reversed physical route
transports both its loop direction and its flag. Section 5
describes the required Weyl change for the native opposite pair.

At representation level the primitive auxiliary increment is
\[
 U_v^{\exp}
       =Q_v^{-\epsilon_v}
          \prod_{e\ni v}\frac{Q_v+X_e}{1+Q_vX_e},\qquad
 V_v^{\exp}=Q_v^2.                                           \tag{16}
\]
It is unchanged by the main-flag redecoration. The exponentiated filling
equation with \(n_v=\epsilon_v-2p_v\) is then
\[
                \prod_{e\ni v}\frac{Q_v+X_e}{1+Q_vX_e}
                                =Q_v^{n_v}.                 \tag{17}
\]

The remaining global marking task is to track these transported
flags through all ordered tree attachments and read the original
preferred main longitude. In particular (16) does not by itself
prove its proposed product formula. An explicit common boundary
path, including the main source flag and the preferred framing,
is still required. The collar construction above gives the
regular local operator for that calculation and rules out an
unmarked three-point swap.
