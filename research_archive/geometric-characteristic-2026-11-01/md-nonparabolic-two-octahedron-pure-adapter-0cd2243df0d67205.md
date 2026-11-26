# A marked nonparabolic chart for the pure two-octahedron piece

1 November 2026. Private mathematical derivation.

This note constructs the face maps of the actual pure two-circle cut.
It identifies the two auxiliary peripheral pairs and the four-segment
main longitude as rational functions. In particular it identifies the
wire variable in the effective action; that variable is not the most
convenient white-face coordinate when the main meridian is nonparabolic.
The local disk-side sewing calculation is also exact. Arbitrary odd
seams and arbitrary oriented tree markings require the further
identifications specified in the last section.

The topological inputs are the labeled two-leaf cut in
[the angular edge chart](md-two-octahedron-angular-edge-block.md),
the pure white/shaded words in
[the marked peripheral calculation](/Users/sasha/volume-conjecture/notes/actual_conway_marked_peripheral_deformation.md),
and the literal ordered page attachment in
[the ordered decomposition](md-all-circle-ordered-octahedron-page-decomposition.md).
The target rational equations are those in
[the effective-action calculation](md-all-circle-rational-effective-ideal.md).
No volume asymptotic is used to identify a peripheral word.

## 1. The parameters and the actual faces

Write \(M\) for the main meridian eigenvalue parameter and set
\(m=M^2\). The symbols \(Q\) and \(P\) are the chosen square roots
of the two auxiliary longitude similarities. All parameters are near
\((m,Q,P)=(1,1,1)\). We use \(E\) temporarily for a white-face
coordinate, near \(i\). The effective-action wire coordinate will be
denoted \(X\).

The two projection copies have six ideal vertices
\[
 \begin{array}{c|c|c}
 &\text{equator}&\text{circle apices}\\ \hline
 +&(0,\infty,1,R)&(A,B)\\
 -&(0,\infty,1,S)&(a,b).
 \end{array}                                                     \tag{1}
\]
The four white identifications are the unique maps of the ordered
triangles
\[
\begin{aligned}
 W_0:(A,0,\infty)&\longmapsto(a,0,\infty),&
 W_1:(B,\infty,1)&\longmapsto(b,\infty,1),\\
 W_2:(A,1,R)&\longmapsto(a,1,S),&
 W_3:(B,R,0)&\longmapsto(b,S,0).
\end{aligned}                                                    \tag{2}
\]
These are the face labels of the original two-leaf cut. Changing the
minus equator from \(R\) to \(S\) is necessary: retaining the old
four white matrices would keep all four main meridians parabolic.

Put \(L=E^{-1}\), and define
\[
\begin{gathered}
 S=\frac{m^2R}{1+(m^2-1)R},\qquad
 \ell_1=L/m,\quad \ell_2=L/m^2,\quad \ell_3=Lm,\\
 c_2=\frac{\ell_2(R-1)/(S-1)-1}{R-1},\qquad
 c_3=\frac{\ell_3R/S-1}{R},\\
 W_0=\begin{pmatrix}L&0\\0&1\end{pmatrix},\quad
 W_1=\begin{pmatrix}\ell_1&1-\ell_1\\0&1\end{pmatrix},\\
 W_2=\begin{pmatrix}c_2+\ell_2&1-c_2-\ell_2\\c_2&1-c_2\end{pmatrix},
 \qquad
 W_3=\begin{pmatrix}\ell_3&0\\c_3&1\end{pmatrix}.
\end{gathered}                                                    \tag{3}
\]
Thus \(W_2(z)=1+\ell_2(z-1)/(1+c_2(z-1))\).
Every map sends its two equatorial vertices in (2) correctly.

If \(q=(0,\infty,1,R)\), the native main corner word
\(W_{j-1}^{-1}W_j\) fixes \(q_j\) and has local derivative
\[
                         (m^{-1},m,m^{-1},m)_j.                  \tag{4}
\]
At infinity the local coordinate is \(1/z\). To derive (3),
start with \(W_0(z)=Lz\). The derivatives at infinity, 1 and 0
give respectively \(\ell_1=L/m,\ell_2=L/m^2,\ell_3=Lm\).
The remaining derivative at \(R\), on its branch through the
complete chart, gives the displayed formula for \(S\).
This supplies the actual peripheral condition, not just equal traces.

## 2. The auxiliary longitude equations and the local gluing locus

Take
\[
 A=\frac{mE+Q}{m+Q},\qquad B=\frac{P(1-mE)}{P+m},\qquad
 a=A/E,\qquad b=1+\frac{B-1}{Em}=-\frac{B}{EP}.                  \tag{5}
\]
There are two expressions for the equatorial coordinate:
\[
\begin{aligned}
 R_v&=\frac{(mE+Q)(mEQ+1)}
 {Em(Q^2+1)+2EQm^2+Q(1-m^2)},\\
 R_w&=-\frac{P(mE-1)^2}
 {Em^2(P^2+1)+2EPm+P(m^2-1)}.
\end{aligned}                                                    \tag{6}
\]
The first is exactly \(W_2(A)=a\); the second is exactly
\(W_3(B)=b\). Their common value is \(R\).

For completeness, the longitude choices made here can be obtained
before solving for the apices. The first longitude is
\(W_2^{-1}W_0\). Its similarity in the coordinate with \(A\)
at infinity is \(W_2'(A)/L\), and is prescribed as \(Q^2\).
The chosen square-root branch is
\(1+c_2(A-1)=-1/(mQ)\). At the other circle the longitude is
\(W_1^{-1}W_3\), with similarity
\(\ell_1/W_3'(B)=P^2\), and the chosen branch is
\(1+c_3B=-mP\). Substitution gives (5)--(6).
Both signs equal \(-1\) at completeness.

Clearing the nonzero denominators of \(R_v-R_w\), and removing
the factor \(Em^2\), gives
\[
\begin{aligned}
G={}&E^2P^2Qm^2+E^2PQ^2m+2E^2PQm^2+2E^2PQm
       +E^2Pm+E^2Qm^2\\
 &+EP^2Q^2m+EP^2m-4EPQm+EQ^2m+Em\\
 &+P^2Q+PQ^2m+2PQm+2PQ+Pm+Q.
\end{aligned}                                                    \tag{7}
\]
The local gluing equation is \(G=0\). At \(m=Q=P=1\),
\(G=8(E^2+1)\), so \(G_E(i,1,1,1)=16i\).
It follows that there is a unique holomorphic branch \(E\) near
\(i\). Every denominator displayed above is nonzero on a sufficiently
small neighborhood of this branch.

The pure shaded maps in the two plus-copy circle frames are
\[
 S_v(A,R)=
 \begin{pmatrix}0&RA(1-A)\\A-R&R-A^2\end{pmatrix},\qquad
 S_w(B,R)=
 \begin{pmatrix}B(B-1)&-RB(B-1)\\B-R&R-B\end{pmatrix}.             \tag{8}
\]
The first fixes \(A\) and sends \(\infty\) to \(0\) and \(1\)
to \(R\). The second fixes \(B\) and sends \(R\) to \(0\)
and \(1\) to infinity. The minus maps are the same formulas with
\((A,B,R)\) replaced by \((a,b,S)\); denote them by
\(S_v^-\) and \(S_w^-\).

All the actual white/shaded edge returns hold projectively:
\[
\begin{array}{lll}
 W_0S_v=S_v^-W_0,&W_2S_v=S_v^-W_2,&W_3S_v=S_v^-W_1,\\
 W_1S_w=S_w^-W_1,&W_3S_w=S_w^-W_3,&W_0S_w=S_w^-W_2.
\end{array}                                                       \tag{9}
\]
The first row follows already on \(R=R_v\), and the second on
\(R=R_w\). One can verify each equality by multiplying one side
by the adjugate of the other: both off-diagonal entries and the
diagonal difference vanish. Consequently these are the face maps
of the marked local representation of the original cut, rather than
maps chosen solely to reproduce a character polynomial.

At completeness their apices are
\[
 (A,B)=((1+i)/2,(1-i)/2),\quad
 (a,b)=((1-i)/2,(1+i)/2),\quad R=S=1/2.                         \tag{10}
\]
The eight ordered tetrahedral shapes of the original apical
subdivision are then \(i\). Holomorphic continuity preserves their
positive imaginary parts on a sufficiently small parameter
neighborhood. This is a local incomplete hyperbolic structure with
decorated main eigenflags; it does not assert completeness at a
nonparabolic main cusp.

## 3. The wire coordinate is determined by the actual meridian

The positively chosen auxiliary meridians are \(S_v^{-1}\) and
\(S_w^{-1}\). Sending the corresponding apex to infinity changes
their similarities into the ordinary derivatives of \(S_v,S_w\)
at those apices. Direct differentiation of (8) gives
\[
\begin{aligned}
 U_v^{\exp}
 &=-\frac{A(A-R)}{R(1-A)}
   =\frac{(Em+Q)(Qm+1)}{(Q+m)(EQm+1)},\\
 U_w^{\exp}
 &=\frac{B(R-1)}{(B-R)(B-1)}
   =\frac{(E+P)(P+m)}{(EP+1)(Pm+1)}.
\end{aligned}                                                     \tag{11}
\]
These are similarities of the primitive words, not the squares of
unrecorded primitive words. The actual longitude similarities are
exactly \(Q^2,P^2\), as established in section 2.

Solve \(U_v^{\exp}=(Q+X)/(1+QX)\) for \(X\).
Cancel the removable \(Q=1\) factor before taking that limit:
\[
 X=
 \frac{EQ^2m+EQm^2+EQm+Em-Qm+Q}
 {EQm^2-EQm+Q^2m+Qm+Q+m}.                                    \tag{12}
\]
The denominator is \(4\) at completeness. The second meridian
similarly gives
\[
 X_w=-\frac{EP^2m+EPm+EP+Em+Pm-P}
 {EPm-EP-P^2-Pm-P-1}.                                        \tag{13}
\]
Their difference is \((m-1)G\) divided by the product of the
two displayed denominators. Hence \(X=X_w\) on the actual
gluing locus. In particular
\[
 U_v^{\exp}=\frac{Q+X}{1+QX},\qquad
 U_w^{\exp}=\frac{P+X}{1+PX},\qquad X|_{m=1}=E.                \tag{14}
\]
Thus the same source wire variable is selected from both actual
auxiliary meridians.

Substitution of (12) and (7) now gives
\[
 (X+Q)(X+Q^{-1})(X+P)(X+P^{-1})
       =(X-1)^2(1-Xm)(1-X/m).                                \tag{15}
\]
For a direct polynomial check, after reducing the rational
expression its numerator is \(G\) times
\[
 (Q+1)^2(Q+m)(Qm+1)
       (EQ^2m+EQm^2+EQm+Em-Qm+Q).
\]
Nonzero unit factors can differ if the common denominator is not
reduced. Alternatively put
\(\mathcal A=X+X^{-1}\), \(\mathcal B=Q+Q^{-1}\),
\(\mathcal C=P+P^{-1}\), \(\mathcal D=m+m^{-1}\).
Equation (15) is
\[
 (\mathcal A+\mathcal B)(\mathcal A+\mathcal C)
  =(\mathcal A-2)(\mathcal A-\mathcal D),\qquad
 \mathcal A=\frac{2\mathcal D-\mathcal B\mathcal C}
                  {\mathcal B+\mathcal C+\mathcal D+2}.       \tag{16}
\]
The denominator in the last expression is \(8\) at completeness.
This is the effective edge equation with \(m=M^2\).

## 4. The full disk-side seam, including its main punctures

Use the ordered cross ratio
\([a,b,c,d]=(a-c)(b-d)/((a-d)(b-c))\).
The incoming plus-copy triangle at the first circle is
\((A,\infty,1)\); the outgoing triangle is \((A,R,0)\).
Develop the adjacent minus triangle back through its actual white
map. The six neighboring third vertices are respectively
\[
 E,\quad W_1^{-1}(a),\quad W_2^{-1}(\infty),\qquad
 W_2^{-1}(0),\quad W_3^{-1}(a),\quad W_0^{-1}(S).              \tag{17}
\]
Substituting (3)--(6), with \(R=R_v\), gives
\[
\begin{array}{c|ccc}
 \text{incoming edge}&(A,\infty)&(\infty,1)&(1,A)\\ \hline
 \text{ratio}&-m/Q&-Q&-1/(mQ)\\
 \text{outgoing edge}&(A,R)&(R,0)&(0,A)\\ \hline
 \text{ratio}&-mQ&-1/Q&-Q/m .
\end{array}                                                       \tag{18}
\]
For example, the first ratio is \((A-1)/(A-E)=-m/Q\).
The other five reduce by the same single substitution. In particular
the table is independent of the other circle parameter \(P\) and
of the preliminary wire coordinate \(E\).

The original pure disk-side matching reverses the two main
punctures: outgoing \((A,R,0)\) is identified with incoming
\((A',1,\infty)\). Thus the outgoing entries are paired with
the incoming entries in reverse order. Each resulting product is
one, including its complex shear. A map of the three ordered
vertices identifies the first triangles; the three ratios then
identify the adjacent second triangles. This proves equality of
the full marked two-triangle disk-side structures. It does not
replace that matching by an arbitrary pants permutation.

The main puncture multipliers visible in the incoming table are
\(m,m^{-1}\), and the circle multiplier is \(Q^{-2}\);
the outgoing table reverses the boundary orientation. These
multipliers explain why recording the puncture order is essential.
Replacing \(M\) by \(M^{-1}\) exchanges eigenflags and is not
an innocuous reset of the marked representation.

Consequently any chain of these *compatibly framed pure seams*
can be sewn in its original cyclic order. The geometric seam at
each step uses the same \(m,Q\); it requires no parameter from
the opposite end of an edge. Products of the auxiliary meridian
increments are therefore products of the factors in (14).
The actual main component and its globally positive meridian
must still be traced through the endpoint frames, as explained
in section 6.

## 5. The actual four-segment main word

In the plus copy the word
\[
                    \Lambda=S_wS_v^{-1}S_w^{-1}S_v.          \tag{19}
\]
follows the equatorial path
\(\infty\to0\to R\to1\to\infty\). This is the actual
four-segment pure main traversal. The commutator of the
matrices (8) has determinant one without any choice of square
root. Its lower-left entry vanishes identically, and its affine
slope is
\[
 \frac{B^2(A-R)^2(B-1)^2}
 {A^2(A-1)^2(B-R)^2}.                                        \tag{20}
\]
Put \(f=(m-X)/(1-mX)\). Substituting the gluing locus in the
diagonal entries of this same determinant-one matrix gives
\[
                   \Lambda=
                    \begin{pmatrix}-f^{-1}&*\\0&-f\end{pmatrix}.
                                                                    \tag{21}
\]
In particular the slope is \(f^{-2}\). At completeness the full
matrix is
\[
                   \begin{pmatrix}-1&2+2i\\0&-1\end{pmatrix},  \tag{22}
\]
which fixes the central sign in (21).

At the selected source flag a positively oriented main meridian
has eigenvalue \(M^{-1}\) and local projective derivative \(M^2\).
If that flag is the infinity flag of this canonical traversal,
its affine meridian slope is \(M^{-2}\), and (21) has selected
longitude eigenvalue \(-f^{-1}\). The inverse-eigenvalue longitude
convention of the effective source therefore gives exactly
\(-f\). This statement specifies both the word and the flag.
Changing the traversal or exchanging its eigenflag must transport
those choices before comparing with a global preferred longitude.

The local two-circle commutator is not, by itself, a proof of the
global product of all the factors \(f\). That product requires
the boundary-path concatenation through the actual ordered tree,
including the closing frame and preferred-framing correction.

## 6. What is established and what remains to assemble

The actual pure two-octahedron block now realizes the effective
edge equation and both primitive auxiliary peripheral pairs.
It realizes the local main longitude factor with a specified
word, central sign and eigenflag. Formula (18) establishes full
pure disk-side seam compatibility, and therefore permits
compatible cyclic gluing without an unspecified shear.

For an arbitrary all-circle tree the next step is to trace the
two oriented main punctures through each original page attachment.
A transported frame can invert a native meridian; it must then
transport the selected eigenflag as well. One must show that the
local factors (21) concatenate to the preferred global word,
with exactly its existing framing monomial. This has not been
replaced here by reciprocity of the rational curve.

An odd distinguished seam also requires the actual puncture
exchange. A useful regular algebraic candidate is the
Hurwitz intertwiner \(AB-I\) for equal-trace puncture
matrices, but the positive crossing in the original collar
may use its inverse after changing the order of the punctures.
Its exact three-point/word correspondence remains separate
from the pure sewing calculation above.

The accompanying script
[checks the local rational identities](md-audit-nonparabolic-two-octahedron-pure-adapter.py)
directly from the matrices, including all six projective returns,
the four native main derivatives, both auxiliary peripheral
pairs, the source-coordinate equation, all six seam ratios,
and the main commutator. These finite identities support the
displayed derivation; they do not replace the topological cut or
the remaining global oriented-word argument.
