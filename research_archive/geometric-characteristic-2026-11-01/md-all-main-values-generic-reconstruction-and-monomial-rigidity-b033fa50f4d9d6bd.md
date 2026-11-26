# Generic reconstruction at every nonzero main eigenvalue

1 November 2026. Private algebraic derivation.

The purpose of this note is narrower than a global positive-shape
theorem. It shows that the actual marked representation constructed
from the edge characters and the original page/collar gluing has a
regular generic point over every fixed \(M_0\ne0\). In particular
the trace-zero values \(M_0=\pm i\) do not force a pole of a main
peripheral eigenvalue ratio. The native octahedral ideal subdivision
does degenerate there, but the rational representation does not.

The local matrix input is
[the character adapter](md-all-circle-edge-four-punctured-character-adapter.md),
sections 2--4 and 7. The actual ordered gluing input is
[the page and collar construction](md-nonparabolic-pure-pages-and-hurwitz-collar.md),
including its full boundary tuples and the distinction between
unframed gluing and subsequent eigenflag decoration.

## 1. A uniform algebraic open set in every fiber

For one edge write
\[
 m=M^2,\quad D=m+m^{-1},\quad
 \beta=Q+Q^{-1},\quad\gamma=P+P^{-1},\quad
 S=\beta+\gamma+D+2.
                                                               \tag{1}
\]
Use \(X\) for the source wire coordinate. Its equation is the
quadratic
\[
 F(X)=S(X^2+1)+(\beta\gamma-2D)X=0.                            \tag{2}
\]
This is equivalent, on \(X\ne0\), to the original degree-four
effective edge equation after its cancellation. Define
\[
 J=\beta\gamma-2\beta-2\gamma-4D-4.
                                                               \tag{3}
\]
The discriminant of (2) is
\[
                 \Delta=(\beta+2)(\gamma+2)J.                 \tag{4}
\]
Consider the open conditions
\[
\begin{gathered}
 QP\ne0,\qquad
 (\beta+2)(\gamma+2)(\beta+D)(\gamma+D)\ne0,\\
 S\ne0,\qquad \Delta\ne0.
\end{gathered}                                                 \tag{5}
\]
For every fixed \(M_0\in\mathbb C^*\), these conditions define
a nonempty Zariski open subset of the \(Q,P\) torus. Indeed each
excluded expression is a nonzero polynomial in the independent
variables \(\beta,\gamma\). For a fixed finite tree the same
conditions can be imposed simultaneously at every edge, since
their product is again a nonzero Laurent polynomial in the
vertex parameters \(Q_v\).

On (5), both roots of (2) are finite, nonzero and distinct.
Several useful evaluations are
\[
\begin{aligned}
 F(1)&=(\beta+2)(\gamma+2),&
 F(-1)&=-J,\\
 F(m)&=m(\beta+D)(\gamma+D),&
 F(m^{-1})&=m^{-1}(\beta+D)(\gamma+D).
\end{aligned}                                                  \tag{6}
\]
Hence neither root is \(1,-1,m,m^{-1}\). In particular
\[
                         f=\frac{m-X}{1-mX}                  \tag{7}
\]
is a finite nonzero function at every point under consideration.
The auxiliary factors \((Q+X)/(1+QX)\) and
\((P+X)/(1+PX)\) are also finite and nonzero. To see this,
substitute \(X=-Q\) or \(X=-Q^{-1}\) in the original edge
equation. A zero can occur only when \(Q=-1\) or
\(Q=-m^{\pm1}\), excluded by (5); the other endpoint is
identical.

## 2. The actual character matrices remain regular

Put \(t=M+M^{-1}\), \(p=-\beta\), \(q=-\gamma\), and
\(\mathcal X=2+SX\). The character adapter uses
\[
 A=\begin{pmatrix}M&1\\0&M^{-1}\end{pmatrix},\qquad
 B=\begin{pmatrix}M^{-1}&0\\p-2&M\end{pmatrix}.                 \tag{8}
\]
Its matrix \(C\) is given by
\[
\begin{gathered}
 h=M-M^{-1},\qquad
 c=\frac{M\mathcal X+M^{-1}q-2t}{D-p},\\
 d=\frac{q-M^2-1+hc}{p-2},\qquad
 e=\mathcal X-1-M^{-2}-hc,\qquad
 C=\begin{pmatrix}c&d\\e&t-c\end{pmatrix},\\
                         D_0=(ABC)^{-1}.
\end{gathered}                                                 \tag{9}
\]
The only denominators in (8)--(9), besides powers of \(M\),
are \(p-2=-(\beta+2)\) and \(D-p=D+\beta\).
They are units on (5). The four matrices have determinant one
and trace \(t\), with
\(\operatorname{tr}(AB)=-\beta\) and
\(\operatorname{tr}(BC)=-\gamma\), by (2).
The formulas contain no division by \(M-M^{-1}\) or by \(t\).

The pure auxiliary transports are
\[
 V=AB-\frac{1+X(\beta+1)}{1-X}I,\qquad
 T=BC+\frac{X+\gamma+1}{1-X}I.                                \tag{10}
\]
They satisfy the full puncture conjugacies, not just the trace
equations. Their determinants simplify on (2) to
\[
 \det V=\frac{X(\beta+2)^2(\beta+D)}{S(X-1)^2},\qquad
 \det T=\frac{X(\gamma+2)^2(\gamma+D)}{S(X-1)^2}.              \tag{11}
\]
For example the first determinant before reduction is
\[
 \frac{(\beta+2)(X^2+\beta X+1)}{(X-1)^2}.
\]
Equation (2) implies
\(X+X^{-1}+\beta=(\beta+2)(\beta+D)/S\), giving (11).
The second computation is the same with \(\gamma\).
Thus both full transport matrices and their inverses are regular
on (5), on either root of the source equation.

Every disk boundary pair is irreducible there. For the first
pair the standard direct trace calculation gives
\[
       \operatorname{tr}[A,B]-2=(\beta+2)(\beta+D)\ne0.        \tag{12}
\]
The second has the corresponding \(\gamma\) formula.
One can also derive (12) directly from the two matrices (8).
For determinant-one two-generator representations this
nonzero expression excludes a common invariant line. In
particular neither generator is central.

The positive odd collar uses \(H=P_{\mathrm{disk}}^{-1}-I\)
with the original ordered disk product. Since
\(\operatorname{tr}P_{\mathrm{disk}}=-\beta\),
\[
                         \det H=2+\beta\ne0.                \tag{13}
\]
The same holds at the other endpoint. The actual positive and
negative Hurwitz generators and all fixed powers remain
invertible. Thus odd seams introduce no exceptional fixed
value of \(M\).

## 3. Sewing finitely many blocks uses a rational finite atlas

The ordered page construction glues two boundary pairs whose
matrices are explicit rational functions of the edge variables.
Their identification is the actual one in the native table;
where a loop is inverted or its order reversed, that operation
is included before asking for an intertwiner.

After those marked identifications, the two ordered boundary
pairs have the same three traces and are irreducible by (12).
Their intertwiner is the solution line of
\[
                   G a=a'G,\qquad G b=b'G.                   \tag{14}
\]
The solution line is one-dimensional, and every nonzero solution
is invertible. Indeed a nontrivial kernel or image would be an
invariant line for one of the two irreducible pairs. Existence
can be proved without using ideal vertices. For an irreducible
pair the four matrices \(I,a,b,ab\) span
\(\operatorname{Mat}_2\). Their multiplication table is
determined by the common trace \(t\) and product trace \(p\):
\[
 a^2=ta-I,\quad b^2=tb-I,\quad
 ab+ba=t(a+b)+(p-t^2)I.                                    \tag{14a}
\]
The same table for the primed pair gives an isomorphism of
the two full matrix algebras, hence conjugation by an
invertible matrix. Equivalently put both pairs in the
explicit form (8); irreducibility ensures that the two
selected generator flags are distinct and that the
off-diagonal entry used to normalize the frame is nonzero.
Either proof retains the ordered generators, not just the
individual conjugacy classes.

Equation (14) is a finite linear system with rational entries.
Choose a nonzero maximal minor and normalize one coordinate
on its one-dimensional kernel. This gives a rational
intertwiner regular in a neighborhood of that point.
No single choice of minor has to work at all parameters.
The finitely many choices form a rational atlas; the resulting
representation and peripheral eigenvalue ratios are independent
of the scalar normalization of an intertwiner.

Start with one edge block. The actual page insertion joins each
new block to the preceding union along one marked disk side.
Its attaching graph is a tree of blocks, so this inductively
constructs a representation of the entire page-cut object with
all matrices regular. The distinguished pure or odd seam at
each circle is then installed using (10), (13), and the two
full generator conjugacies of its actual mapping cylinder.
Those formulas preserve its outer disk product. Van Kampen
therefore gives the representation of the original augmented
exterior. No arbitrary pants permutation or commutativity of
tangles is used.

For any fixed finite tree, intersecting the finitely many
necessary open charts gives a nonempty open set over the
fixed \(M_0\). Equivalently, at any good point one may choose
each nonzero intertwiner minor in succession, obtaining a
regular neighborhood of that point. This proves existence of
the required actual rational \(\mathrm{PGL}_2\) reconstruction
at every nonzero main parameter.

This step requires the actual marked boundary conjugacies,
not just a formal family of characters. They were identified
with the original cut in the page/collar proof and remain
rational identities on the present open sets.

## 4. The exceptional-looking main parameters

At \(M=\pm1\), one has \(D=2\). Conditions (5) simply
exclude \(\beta=-2,\gamma=-2\), together with the stated
nonzero discriminant and denominator. The main matrix in
(8) is a noncentral parabolic. Nothing in (8)--(14) divides
by its eigenvalue difference, so the reconstruction is regular.

At \(M=\pm i\), one has \(D=-2\). The source discriminant
becomes
\[
                     \Delta=(\beta^2-4)(\gamma^2-4).         \tag{15}
\]
With \(\beta=Q+Q^{-1}\) and \(\gamma=P+P^{-1}\),
this is a square in \(\mathbb C(Q,P)\). The fiber therefore
splits; generic-fiber irreducibility must not be asserted
at these two values. Nevertheless (5) gives two distinct
simple roots at generic \(Q,P\), and all matrices (8)--(14)
are regular. The main punctures are semisimple, with
eigenvalues \(i,-i\) or \(-i,i\), and remain noncentral.
The two roots can be written explicitly as
\[
             X=-\frac{Q+P}{1+QP},\qquad
             X=-\frac{1+QP}{Q+P}.                            \tag{15a}
\]
For generic \(Q,P\) they differ and avoid \(1,-1\).
Fixing these auxiliary values, the implicit-function theorem
for (2) therefore continues either root holomorphically in
\(M\) through \(M_0=i\) or \(-i\).

The native ideal cell chart explains a possible false alarm.
At \(m=-1\), its preliminary white coordinate \(E_0\)
satisfies
\[
 (E_0P-E_0Q-PQ+1)(E_0PQ-E_0-P+Q)=0.
                                                               \tag{16}
\]
On one branch the two minus-copy circle apices coincide; on
the other the plus-copy apices coincide. Thus that particular
eight-tetrahedron ideal subdivision degenerates. This does
not make the actual group matrices singular: (8)--(14) are
an explicit regular reconstruction at precisely those points.
The rigidity argument needs the latter, not a positive
triangulation at every complex value of \(M\).

## 5. A regular nonzero main eigenvalue ratio

Every main peripheral word is a fixed finite product of the
regular invertible group matrices just constructed. Hence its
matrix and inverse are regular at the chosen point.
The main meridian is noncentral.

There is one important trace-zero detail. Commutation in
\(\mathrm{PGL}_2\) alone would allow a longitude to
exchange the two eigenlines of a trace-zero meridian.
Use the matrices on the local section through nearby \(M\).
Normalize the meridian \(\mu\) to determinant one.
Its projective commutation with a regular invertible
longitude representative \(L\) gives
\(L\mu L^{-1}=\kappa\mu\), where
\(\kappa^2=1\) by determinants. At the nearby parameters
with \(M+M^{-1}\ne0\), taking traces gives \(\kappa=1\).
Consequently the exact matrix identity
\[
                              L\mu=\mu L.                   \tag{16a}
\]
extends to the trace-zero point. The undesired
anticommuting component is not part of this continued
representation. This also follows as a rational identity
on the integral generic source family.

At \(M_0\ne\pm1\), choose
its specified eigenline locally; its eigenvalue on a commuting
peripheral word is finite and nonzero. The ratio of the two
peripheral eigenvalues is therefore a regular unit.

The same conclusion holds at \(M_0=\pm1\), without
diagonalizing the meridian. In a frame in which its
upper-right entry is a unit, a commuting matrix \(L\) has
the form
\[
                            L=aI+b\mu.                      \tag{17}
\]
Here \(b=L_{12}/\mu_{12}\) and
\(a=L_{11}-b\mu_{11}\) are regular. Its two selected
eigenvalues are \(a+bM\) and \(a+bM^{-1}\). Both are
nonzero at the point because \(\det L\ne0\).
Their ratio is therefore regular and nonzero through the
parabolic value. Scalar changes of the representative \(L\)
cancel from the ratio.

The selected meridian eigenline itself is regular as well:
in this frame it is spanned by
\((\mu_{12},M-\mu_{11})\), or by
\((\mu_{12},M^{-1}-\mu_{11})\) for the other selection.
The first coordinate is a unit, including at \(M=\pm1\).
Thus coalescence of the two flags does not create a pole in
the marked eigenvalue ratio.

This directly applies to the square of a determinant-one
preferred-longitude eigenvalue, with the chosen inverse
convention if necessary. It does not require choosing a
global square root of a projective matrix determinant.
Every factor (7), and every framing monomial in \(M\),
is likewise a unit at the point.

## 6. Consequence for a residual one-variable factor

Suppose the boundary isotropy calculation has established, in
the selected source function field, that
\[
          R(M)=\frac{L_{\mathrm{geom}}^{\,2}}
                         {\bigl(\prod_e f_e\bigr)^2}
                         \quad\text{belongs to }\mathbb C(M).
                                                               \tag{18}
\]
Here \(L_{\mathrm{geom}}\) uses the fixed marked longitude
convention. The function-field step is separate: geometric
integrality over \(\mathbb C(M)\) is required to exclude a
larger algebraic constant field.

Fix any \(M_0\ne0\). Choose a good point as above on the
selected total source family. Equations (2), (4) make the
source cover étale over its \((M,Q_v)\) base there: every
wire root is simple. Thus \(M-M_0\) is a genuine local
base parameter. Sections 1--5 show that the pullback of (18)
is a regular unit at that point. If the rational function
\(R(M)\) had a zero or pole at \(M_0\), its pullback would
have the same nonzero order in that parameter, a
contradiction.

More concretely, fix generic numerical auxiliary values
\(Q_v=q_v\) satisfying all the open conditions at \(M_0\),
and choose a simple root of every edge equation. The implicit
function theorem gives simultaneous holomorphic roots
\(X_e(M)\) near \(M_0\). At the chosen point select a
nonzero minor in each linear gluing system (14). Those same
minors remain nonzero nearby. All actual group matrices,
their inverses and the main eigenvalue ratio are then
holomorphic along this local section. This is stronger than
the existence of an isolated good point in a special fiber.

The split trace-zero fibers do not invalidate this argument.
Let \(B\) be the Laurent coordinate ring in \(M,Q_v\),
localized at all \(S_e\). Dividing (2) by \(S_e\) makes
every edge polynomial monic with constant term one. The
simultaneous source algebra is therefore free over \(B\),
with basis the products \(\prod_e X_e^{\epsilon_e}\),
\(\epsilon_e\in\{0,1\}\). The independent generic edge
squareclasses imply that its generic localization is a
single field of degree \(2^{|E|}\). Freeness embeds the
source algebra into that field; in particular the total
source variety is integral and has no additional vertical
component. Its simple points at \(M=\pm i\) belong to
the closure of the same generic family. A rational identity
proved there therefore holds on the regular local section
just constructed.

Consequently the divisor of \(R\) is supported at zero and
infinity, and
\[
                              R(M)=cM^k.                    \tag{19}
\]
for a nonzero constant \(c\) and an integer \(k\).
At \(M=1\), the preferred complete lift and \(f_e(1)=1\)
give \(c=1\). If the already marked geometric cusp formula
gives
\[
 \left.\frac{d}{d\log M}\log L_{\mathrm{geom}}\right|_{M=1}
       =a_{\mathrm{aug}}
          +\left.\frac{d}{d\log M}\log\prod_e f_e\right|_{M=1},
                                                               \tag{20}
\]
for the unfilled augmented diagram with its retained crossing
signs, then \(k=2a_{\mathrm{aug}}\). The preferred-longitude
correction after filling is a separate homology calculation.
The remaining square-root
sign is fixed by the actual complete longitude lift.

Thus there is no unavoidable exceptional nonzero main value
in the required representation-level regularity test. The
isotropy and constant-field premise in (18), and the exact
marked convention in (20), remain explicit separate inputs.
