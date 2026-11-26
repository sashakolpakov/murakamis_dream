# A uniform-sign normal form for every fixed rational corridor

Every fixed rational corridor can be changed to a chain whose
internal crossing powers have one sign. Except for the integral
and unit cases, all their magnitudes can be taken at least two.
The change preserves both arbitrary outside attachments. It
introduces fixed integral twists at the ends and a specified
proper half-turn, rather than a condition on the surviving
filling parameters.

The associated tridiagonal chain matrix is definite. Neither
definiteness nor the tangle isotopy proves a quantum asymptotic.
The exact quantum transformation below retains its scalar,
boundary twists and all repeated-root normal data.

## 1. The original word and its boundary map

Use the original physical crossing \(R\), clockwise turn \(T\),
and the supported pillowcase representatives
\[
 \widetilde R^{\,n}(x,y)=(x+ny+n/2,y),\qquad
 \widetilde T(x,y)=(-y,x+1/2).
 \tag{1}
\]
Their linear parts are
\[
 A_n=\begin{pmatrix}1&n\\0&1\end{pmatrix},\qquad
 S=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
 \tag{2}
\]
The four marked points are the half-lattice points of the torus,
modulo the deck involution \(z\mapsto-z\).
The [corridor compression note](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_rational_corridor_compression.md)
explains how these representatives are obtained from the actual
supported crossings and how an equality of their affine maps
gives an isotopy carrying arbitrary attached tangles.

Let \(W\) be a fixed finite word, and write its full affine lift as
\[
 \widetilde W(z)=Gz+v,\qquad
 G=\begin{pmatrix}a&b\\c&d\end{pmatrix},\quad
 \det G=1,\quad v\in\tfrac12\mathbb Z^2.
 \tag{3}
\]
All powers inside this word are fixed before any remaining
outside filling parameter is varied.

## 2. The ceiling Euclidean algorithm and the full matrix identity

Suppose \(|c|=C\ge2\). Multiply \(G\) by its deck sign
\(\varepsilon=\operatorname{sgn}(c)\), so its lower-left entry is
\(C>0\). There are unique integers \(r,s\) such that
\[
 G_0=A_{-r}(\varepsilon G)A_{-s}
    =\begin{pmatrix}A&B\\C&D\end{pmatrix},
       \qquad 1\le A,D<C.
 \tag{4}
\]
Indeed \(A\) and \(D\) are the nonzero residues of
\(\varepsilon a,\varepsilon d\) modulo \(C\), and
\[
 r=\frac{\varepsilon a-A}{C},\qquad
 s=\frac{\varepsilon d-D}{C}.
 \tag{5}
\]
The residues are nonzero because the determinant is one.
It also gives \(AD\equiv1\pmod C\) and
\(B=(AD-1)/C\ge0\).

Starting with \(q_1=C,p_1=A\), repeat
\[
 b_j=\left\lceil\frac{q_j}{p_j}\right\rceil,\qquad
 r_j=b_jp_j-q_j.
 \tag{6}
\]
If \(r_j=0\), stop. Otherwise set
\((q_{j+1},p_{j+1})=(p_j,r_j)\).
At every step \(q_j>p_j>0\), so \(b_j\ge2\).
Also \(0\le r_j<p_j\). The algorithm terminates,
preserves coprimality, and gives
\[
 \frac CA=[b_1,\ldots,b_k]_-
       :=b_1-\frac1{b_2-\dfrac1{\cdots-\dfrac1{b_k}}}.
 \tag{7}
\]
In particular \(k\le A\le C-1\). The output is unique:
at any nonintegral step the first coefficient of an
expansion with all later complete quotients greater than
one must be the ceiling.

**Proposition 1.** With (4)--(7),
\[
 G_0=(-1)^k S A_{-b_1}S A_{-b_2}\cdots S A_{-b_k}S.
 \tag{8}
\]

**Proof.** Let \(H\) denote the matrix on the right.
For \(k=1\), it is
\(\left(\begin{smallmatrix}1&0\\b_1&1\end{smallmatrix}\right)\).
Adding a new first coefficient sends a tail matrix
\(\left(\begin{smallmatrix}a'&b'\\c'&d'\end{smallmatrix}\right)\)
to
\[
 \begin{pmatrix}c'&d'\\b_1c'-a'&b_1d'-b'\end{pmatrix}.
 \tag{9}
\]
Thus the ratio of its lower-left to upper-left entries
is the negative continued fraction (7).

The continuant recurrence
\[
 K_j=b_jK_{j-1}-K_{j-2},\qquad K_0=1,\quad K_{-1}=0
 \tag{10}
\]
shows \(K_j>K_{j-1}>0\) for \(j\ge1\).
Applied to prefixes and reversed suffixes, it shows that
the two diagonal entries of \(H\) lie strictly between
zero and its lower-left entry. All matrices have
determinant one, so that entry and the upper-left entry
are coprime. Their ratio in (7) therefore identifies them
as \(C,A\), with no common factor.
The lower-right entry is the unique integer in
\(\{1,\ldots,C-1\}\) whose product with \(A\) is one
modulo \(C\); hence it is \(D\).
The determinant then identifies the remaining entry as
\(B\). This proves (8). \(\square\)

Combining the equations gives an equality in
\(\mathrm{PSL}_2(\mathbb Z)\):
\[
 G=A_r S A_{-b_1}S\cdots S A_{-b_k}S A_s .
 \tag{11}
\]
This is a full matrix statement, not just equality of
one rational-tangle slope.

## 3. The actual two-boundary tangle identity

Form the physical word
\[
 B=R^r T R^{-b_1}T\cdots T R^{-b_k}T R^s.
 \tag{12}
\]
Its affine lift is obtained from (1). Its linear part
agrees with \(G\) up to the one deck sign.
Consequently
\[
                \widetilde B^{-1}\widetilde W(z)
                          =\lambda z+w,\qquad
       \lambda\in\{1,-1\},\quad w\in\tfrac12\mathbb Z^2.
 \tag{13}
\]
After the deck involution this is translation by
\(\delta=\lambda w\bmod\mathbb Z^2\). Use the actual
proper rotation
\[
\begin{array}{c|cccc}
 \delta&(0,0)&(1/2,0)&(0,1/2)&(1/2,1/2)\\ \hline
 H_\delta&1&\rho&K&\tau .
\end{array}
\tag{14}
\]
The supported collar isotopy gives, for every attached
tangle \(F\),
\[
 \boxed{\;
 W(F)\simeq
 R^rT\!\left(R^{-b_1}T\!\left(\cdots
        T\!\left(R^{-b_k}T(R^sH_\delta(F))\right)
                     \cdots\right)\right).
 \;}
 \tag{15}
\]
It carries all marked arcs, closed components, and
any supplied ribbon. In particular the rotation in
(14) cannot be erased on an arbitrary outside branch.

This proves that every corridor with \(|c|\ge2\) has
a uniform-negative form with all internal magnitudes
at least two. Applying the same construction to the
mirrored word and then mirroring the whole equality
gives a uniform-positive form as well. Both sides
of that resulting equality are in the original
oriented ambient manifold; the argument does not
replace just one tangle by its mirror.

If \(|c|=1\), the one-vertex criterion gives a single
unit power with integral twists at both ends.
If \(c=0\), the word reduces to an integral twist
and a proper half-turn with no intervening turn.
The last case can merge two variable outside
parameters and must retain its fiber information.

For example, the mixed two-boundary corridor has
\[
 S A_{-2}S A_2S
    =\begin{pmatrix}-2&1\\-5&2\end{pmatrix}.
\]
After the deck sign, \(C=5,A=2,D=3\), and
\(5/2=[3,2]_-\). Here \(r=0,s=-1\).
Thus its common-sign replacement has internal
powers \(-3,-2\), with a twist \(-1\) on its
inner retained end and the rotation computed from
(13). It is not a reduction to a single internal
vertex.

## 4. The exact quantum scalar and the boundary chirps

Let \(M_N\) be original multiplication by \(R\)
and \(J_N\) the original Newton reversal. Put
\[
 D=N-1,\qquad
 \kappa_N=\exp\frac{\pi iD^2}{2N}.
 \tag{16}
\]
The full algebra includes the first normals at
the double roots. Its established identities are
\[
 J_N^2=I,\qquad
 J_NM_NJ_N=\kappa_N M_N^{-1}J_NM_N^{-1}.
 \tag{17}
\]
Use the displayed logarithm of \(\kappa_N\) and set
\(\widehat M_N=\kappa_N^{-1/3}M_N\). Direct multiplication
in (17) gives
\[
                J_N^2=I,\qquad
                (J_N\widehat M_N)^3=I.
 \tag{18}
\]
These are the defining relations of
\(\mathrm{PSL}_2(\mathbb Z)\) for \(S,A_1\).
One elementary verification of that presentation uses
the Farey ideal triangulation: its dual, subdivided
at edge midpoints, is a tree, the modular group acts
transitively on its edges, an edge has trivial
stabilizer, and the endpoint stabilizers have orders
two and three. A reduced alternating product of
nonidentity elements in these stabilizers moves
the base edge along a nonbacktracking path, so
cannot be the identity. The two generators also
generate every integral determinant-one matrix
by the Euclidean algorithm. This proves the
presentation used in (18).

For a word \(W\), let \(e(W)\) be the sum of its
signed crossing exponents; turns contribute zero.
Equations (11), (18) give the exact operator equality
\[
 \boxed{\;
 \mathcal Q_N(W)
   =\kappa_N^\ell
       M_N^r
       \bigl[J_NM_N^{-b_1}J_N\cdots
                  J_NM_N^{-b_k}J_N\bigr]M_N^s,
 \qquad
 \ell=\frac{e(W)-r-s+\sum_jb_j}{3}.
 \;}
 \tag{19}
\]
The exponent \(\ell\) is an integer. Indeed the
same modular presentation has a homomorphism to
\(\mathbb Z/3\mathbb Z\) sending \(A_1\) to one
and \(S\) to zero, so equal matrices have equal
crossing-exponent sums modulo three.

The actual physical rotation in (15) is still
carried in the topological statement. Equation
(19) is proved separately on the full original
quantum algebra; it is not an inference that
the rotation fixes every arbitrary tangle.

Here is the corresponding boundary interpretation.
An operator \(Q\) has Frobenius kernel coefficient
matrix \(QJ_N\). The identity
\[
             M_N^sJ_N=J_N(M_N^s)^T
 \tag{20}
\]
therefore makes the end factors in (19) multiplication
by \(R^r\) and \(R^s\) in its two boundary variables,
followed by canonical reduction. Thus, if the
uniform-negative kernel has an already proved
whole-boundary phase \(\Phi(u,v)\), the
[canonical boundary-multiplication theorem](research_boundary_crossing_packet_preservation.md)
and its [two-boundary version](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_internal_two_crossing_chain.md)
give the transformed phase
\[
           \Phi(u,v)+\frac{i}{4\pi}(ru^2+sv^2).
 \tag{21}
\]
The exact additional scalar is
\[
       \kappa_N^\ell C_{N,r}C_{N,s},\qquad
       C_{N,j}=\exp\frac{\pi i jD^2}{4N}.
 \tag{22}
\]
The amplitudes and the polynomial power of \(N\)
are unchanged by those multiplication operations.
Equations (21)--(22) are conditional on the stated
whole-boundary estimate for the new kernel.
The exact finite identity (19) needs no asymptotic
assumption and retains all normal data.

## 5. Pendant words and their cap scalar

For a pendant word the rational slope is the
second-column ratio \(p/q\), \(q\ge0\).
If \(q\ge2\), write
\[
                  p/q=r+x,\qquad
                  r=\lfloor p/q\rfloor,\quad 0<x<1.
 \tag{23}
\]
The ceiling algorithm for \(1/x\) gives
\[
        x=\frac1{b_1-\dfrac1{b_2-\cdots-1/b_k}},
                  \qquad b_j\ge2.
 \tag{24}
\]
The pendant word
\[
                   B=R^rTR^{-b_1}T\cdots TR^{-b_k}
 \tag{25}
\]
has precisely that slope. The actual cap-stabilizer
argument in the corridor note identifies \(W(I)\)
with \(B(I)\), where \(I\) is the through tangle.
No constraint is imposed on any remaining outside
power.

There is an exact scalar even though the two
full matrices need not agree. Normalize the
relative linear matrix to
\[
                  B^{-1}W=\begin{pmatrix}1&0\\h&1\end{pmatrix}
                      \quad\hbox{in }\mathrm{PSL}_2(\mathbb Z).
 \tag{26}
\]
It is the matrix of \(TR^{-h}T\).
The last Newton vector is an eigenvector of
the actual crossing with eigenvalue \(\kappa_N\):
the diagonal entry is
\(\kappa_N(-1)^D e^{\pi iD(D+1)/N}=\kappa_N\).
Therefore
\[
              J_NM_N^{-h}J_Ne_0=\kappa_N^{-h}e_0.
\]
Combining this with (18) yields
\[
 \boxed{\;
 \mathcal Q_N(W)e_0
      =\kappa_N^{\ell_{\rm cap}}\mathcal Q_N(B)e_0,
 \qquad
 \ell_{\rm cap}=\frac{e(W)-e(B)-2h}{3}\in\mathbb Z .
 \;}
 \tag{27}
\]
This equality is between the full original canonical
boundary elements. Any outer \(R^r\) in (25) is
handled by canonical multiplication, with its
chirp and scalar retained as above.

In the mixed example,
\[
             TR^{-2}TR^2(I)\simeq TR^{-3}TR^{-2}(I),
 \tag{28}
\]
and \(h=1\), \(\ell_{\rm cap}=1\).
Thus its exact boundary polynomial is \(\kappa_N\)
times that of the uniform-negative word in (28).
The known mixed-word theorem consequently also
estimates this particular uniform-negative word.
It does not estimate arbitrary such words.

If \(q=1\), the pendant word is an integral braid.
If \(q=0\), it is the cup-cap tangle. The latter
case uses the literal cap-sum decomposition and
can retain an unresolved closed core. It is not
silently put into the positive boundary class.

## 6. The definite chain matrix

The expansion (7) has the real symmetric matrix
\[
 Q_{\mathbf b}=
 \begin{pmatrix}
 b_1&-1\\
 -1&b_2&-1\\
 &\ddots&\ddots&\ddots\\
 &&-1&b_k
 \end{pmatrix}.
 \tag{29}
\]
For any real vector \(z\),
\[
 z^TQ_{\mathbf b}z
   =\sum_{j=1}^{k-1}(z_j-z_{j+1})^2
      +z_1^2+z_k^2+\sum_{j=1}^k(b_j-2)z_j^2.
 \tag{30}
\]
This is strictly positive for \(z\ne0\), also when
every \(b_j=2\). Its determinant is \(C\), and the
principal minor deleting the first row and column
is \(A\), by (7), (10). Its Schur effective first
weight is the same fraction \(C/A\).

This is the definite tridiagonal form associated
with the negative continued fraction. In the
usual continued-fraction surgery presentation,
the corresponding chain has the opposite form
\(-Q_{\mathbf b}\). No identification of this
intersection form with a quantum phase Hessian
is made here.

## 7. Surviving original parameters and branching

Normalize finitely many disjoint fixed degree-two
corridors in an ordered circle tree. They may
share retained branch vertices. The end factors
in (15) are collected with the original branch
powers by the supported twist-sliding isotopy;
each passed factor receives its prescribed
proper rotation. The total change at a retained
vertex is a fixed integer \(\Delta_v\):
\[
                        n'_v=n_v+\Delta_v.
 \tag{31}
\]
After choosing the transported carrier parity,
\[
 p'_v=p_v+
       \frac{\eta'_v-\eta_v-\Delta_v}{2},
                  \qquad n_v=\eta_v-2p_v.
 \tag{32}
\]
These are injective translations of the surviving
integer assignments. Independent eventual longness
is preserved. Internal old powers were already
fixed; the added coefficients in (7) are fixed
integers, not new freely variable surgery parameters.

Rotations do not change the signed crossing
power of an integral braid. Propagating a
rotation through an already normalized chain
can reverse its order, but does not change
its uniform sign or the condition \(b_j\ge2\).
Thus normalizing disjoint corridors does not
undo a neighboring corridor's normalization.
The actual branch weights do receive the
constant shifts (31), which must be retained.

This does not make an arbitrary branching tree
definite. For a weighted tree the symmetric
matrix with diagonal weights \(b_v\) and
off-diagonal edge entries \(-1\) is positive
definite exactly when successive leaf
elimination produces positive effective
weights
\[
                 q_v=b_v-\sum_{w\ {\rm child\ of}\ v}q_w^{-1}.
 \tag{33}
\]
The assertion follows by completing squares
at each leaf; the resulting diagonal factors
are the \(q_v\). It is independent of which
vertex is chosen as root.
For example a star with central weight two
and five leaves of weight two has central
effective weight \(2-5/2=-1/2\).
Every edge or chain in that star has positive
weights at least two, but the whole tree
matrix is indefinite.

Nor does (30) turn the full root-of-unity
source into a positive sum. The original
crossings still have their complex entries,
and the full trace still retains its normal
terms. Equation (19) preserves those facts
exactly. A general theorem for uniform-sign
chains would be a substantive new analytic
input; definite integral surgery data alone
does not supply it.

## 8. Scope of the reduction

The normal form gives a concrete common target
for every fixed rational corridor. Its quantum
and topological transformations are both exact.
In particular a future whole-boundary theorem
for all uniform-negative chains of magnitudes
at least two would immediately transfer to all
fixed rational corridors with \(c\ne0\), with
the original two boundary variables and their
normal data retained.

The zero case \(c=0\), the pendant cap case,
and connected regions with branching remain
separate. A zero merger has infinite parameter
fibers when its two ends are still variable.
The existing
[fiber criterion](research_affine_reduction_fibers_and_core_obligation.md)
must accompany those reductions; it is not
replaced by the continued-fraction algorithm.
For a general arborescent component, normalizing
its maximal degree-two paths leaves its actual
branching pieces in place.

The rational-tangle normal-form background is
classical; see
[Kauffman–Lambropoulou](https://arxiv.org/abs/math/0311499).
The independent ceiling algorithm, full affine
marking, scalar (19), and original parameter
map specify what is used here. No claim of
a new rational-tangle classification or of
cofinite volume coverage follows from them.

There is now a geometric theorem for the subfamily whose normalized
magnitudes are all at least four:
[the negative-corridor variation](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_negative_corridor_variational_bounds.md)
has an interior minimum, and
[the marked-completion theorem](research_positive_point_marked_completion.md)
identifies its actual filling when the retained outside cusps are
complete. The boundary shifts and rotations above still have to
be transported. This geometric result does not estimate the
original quantum source, and coefficients two and three remain
in the general normal form.

## 9. Reproducing the finite checks

Run the separate checker from the repository root:

    .venv/bin/python experiments/check_definite_rational_corridor_normal_form.py \
      --output repro/results/research-definite-rational-corridor-normal-form.json

The [checker](../experiments/check_definite_rational_corridor_normal_form.py)
uses exact integers and rational translations for all words of lengths
one through four with powers between minus three and three. Of the
2,800 words, 2,220 have the two-boundary normal form with
\(|c|\ge2\), and 2,220 have a nonintegral finite pendant slope.
It verifies the full affine identity, retained half-turn, integral
scalar exponent, determinant and tail minor. The two sets of 2,220
words need not be the same.

Separately, it compares the original quantum matrices and pendant
vectors for five displayed words at levels two through seven,
using 100 decimal digits. These 30 matrix and 30 pendant comparisons
check the scalar and ordering conventions numerically. The written
operator argument proves the identities for all levels.

The [saved output](../repro/results/research-definite-rational-corridor-normal-form.json)
contains the script and dependency hashes. Its script SHA256 is
6352af92a2124a407b2a2893560e4987c7679f80837cc2d3f39ee72d430bd354.
The output path can be changed for an independent replay.

A [140-digit replay](../repro/results/research-definite-rational-corridor-normal-form-root.json)
checks the same exact word set and extends the quantum comparisons
through level nine, giving 40 matrix and 40 pendant comparisons.
