# Recognizing rational terminal pieces from their marked slopes

Research deduction, 3 November 2026.

The available boundary theorems apply to more rational presentations
than their displayed crossing words suggest. This note gives an
arithmetic sufficient condition for replacing a fixed rational
terminal piece by a piece already covered by those theorems. The
replacement retains the outside boundary, its primitive curves,
and the original free filling parameter. It also gives a new
family of binary negative chains whose last two complementary
powers are both short.

The criterion is sufficient, not a classification of all rational
pieces satisfying the volume conjecture. In particular, a theorem
for a terminal piece supplies one free boundary variable. It does
not supply a kernel with two free boundaries.

## 1. A marked rational presentation and its exact quantum scalar

Let \(I\) be the through tangle, \(R\) the original crossing,
and \(T\) the original quarter-turn. Let \(W\) be any fixed word
in \(R,T\), with all its integer powers fixed. Its matrix on the
pillowcase is obtained from
\[
 A_n=\begin{pmatrix}1&n\\0&1\end{pmatrix},\qquad
 S=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
 \tag{1}
\]
The slope of \(W(I)\) is the ratio \(p/q\) of the entries in the
second column, reduced with \(q\ge0\). The actual affine lifts,
including their half-lattice translations, are those in
[the marked corridor theorem](research_rational_corridor_compression.md).
That theorem proves the cap-stabilizer statement needed below:
equal slopes give an isotopy of these rational tangles relative
to their marked attaching boundary. The proper rotations in the
affine comparison fix \(I\); they are not discarded on an
arbitrary second attachment.

Suppose \(q\ge2\). Set
\[
 r=\left\lceil\frac pq\right\rceil,\qquad d=rq-p,
 \qquad 1\le d<q.
 \tag{2}
\]
Apply the ceiling Euclidean algorithm to \(q/d\). It gives a
unique finite list \(\mathbf c=(c_1,\ldots,c_\ell)\), with every
\(c_j\ge2\), such that
\[
 \frac qd=[c_1,\ldots,c_\ell]_-
 :=c_1-\frac1{c_2-\dfrac1{\cdots-1/c_\ell}}.
 \tag{3}
\]
At each nonterminal step, replace a coprime pair \((q_j,d_j)\)
by \((d_j,c_jd_j-q_j)\), with
\(c_j=\lceil q_j/d_j\rceil\). The second entry strictly decreases,
which proves termination. The ceiling at each step is forced,
which proves uniqueness.

Write
\[
 F_{\mathbf c}=T\bigl(R^{c_1}T(R^{c_2}\cdots
                   T(R^{c_\ell})\cdots)\bigr),\qquad
 B=R^rF_{\mathbf c}.
 \tag{4}
\]
Its slope is \(r-1/[\mathbf c]_-=p/q\). Thus \(W(I)\) and
\(B(I)\) are the same marked rational tangle.

There is an exact identity of the canonical quantum boundary
elements, including their first normal derivatives. Let
\(\mathcal Q_N\) denote evaluation in the original quantum
operators, let \(e(W)\) be the sum of the signed crossing powers
in \(W\), and put
\[
 \kappa_N=\exp\frac{\pi i(N-1)^2}{2N}.
\]
Normalize the relative matrix by its deck sign so that
\[
 B^{-1}W=\begin{pmatrix}1&0\\h&1\end{pmatrix}
 \quad\text{in }\mathrm{PSL}_2(\mathbb Z).
\]
Then Section 5 of
[the definite rational normal form](research_definite_rational_corridor_normal_form.md)
gives
\[
 \mathcal Q_N(W)e_0
   =\kappa_N^{\ell_{\rm cap}}\mathcal Q_N(B)e_0,
 \qquad
 \ell_{\rm cap}=\frac{e(W)-e(B)-2h}{3}\in\mathbb Z.
 \tag{5}
\]
Here is the scalar calculation, including its sign. The original
relations \(J^2=1\) and
\(JMJ=\kappa_NM^{-1}JM^{-1}\) imply that
\(J,\widehat M=\kappa_N^{-1/3}M\) represent the generators
\(S,A_1\) of \(\mathrm{PSL}_2(\mathbb Z)\), with the
displayed logarithm of \(\kappa_N\). The relative cap matrix
is represented by \(TR^{-h}T\), so
\[
 \mathcal Q_N(W)
 =\kappa_N^{(e(W)-e(B)+h)/3}
       \mathcal Q_N(B)JM^{-h}J.
 \tag{5a}
\]
The last Newton vector has eigenvalue \(\kappa_N\) under
\(M\): its diagonal entry is
\(\kappa_N(-1)^{N-1}e^{\pi i(N-1)}=\kappa_N\).
Since \(Je_0=e_{N-1}\), applying the last factor in (5a)
to \(e_0\) contributes \(\kappa_N^{-h}\). This gives the
exponent \((e(W)-e(B)-2h)/3\) in (5). It is an integer:
the homomorphism from the modular group to
\(\mathbb Z/3\mathbb Z\) sending \(A_1\) to one and
\(S\) to zero gives \(e(W)-e(B)+h\equiv0\pmod3\).
Thus (5) is an identity before any asymptotic estimate,
including the full first normal data.

The cases \(q=1\) and \(q=0\) are separate. The first is an
integral braid, whose power can be collected at the adjacent
vertex. The second is a cup-cap tangle and can separate off a
closed component. Neither case is placed in the boundary class
below without its corresponding exact reduction.

## 2. Which positive lists have a proved boundary theorem

There are three kinds of initial positive list:
\[
 (a)\quad(a\ge2),\qquad (3,2),\qquad (3,3).
 \tag{6}
\]
The first consists of the original terminal pieces. The last is
the adjacent-three piece with its
[whole-period theorem](research_three_crossing_whole_period_source.md)
and [marked volume normalization](research_three_crossing_action_volume_calibration.md).
The middle list is already supplied by the mixed pair theorem.
Indeed the exact relation in the definite-normal-form note and
its conjugate give
\[
 \mathcal Q_N(TR^3TR^2)e_0
       =\kappa_N\mathcal Q_N(TR^2TR^{-2})e_0.
 \tag{7}
\]
The mixed pair and its mirror have their original geometric
attachment identified. The cap isotopy in (7) carries that
attachment to the positive list \((3,2)\).

Choose one common boundary disk and strip for these initial
pieces and their mirrors. On that disk their canonical sources
have expansions
\[
 F_N(u)=\epsilon_N A(u)e^{NW(u)}(1+O_F(N^{-1})),
 \qquad |\epsilon_N|=1,\quad A(u)\ne0,
 \tag{8}
\]
where \(A,W\) are even holomorphic functions. They have common
bounds on \(W-W(0)\), a common positive lower bound for
\(-\Re W''\), and a common estimate
\[
 |F_N(x+iy)|\le C_FN^{d_F}
  \exp N\{\Re W(0)-c(1-\cos x)+Cy^2\},
 \quad |x|\le\pi,\ |y|\le h,
 \tag{9}
\]
with \(c,h>0\). The constants \(C_F,d_F\), error constant and
starting level may depend on the entire fixed piece.

**Theorem 1.** There is an integer \(B_0\ge3\) with the
following property. A positive list \(\mathbf c\) has all the
boundary conclusions (8)--(9) if it ends in one of the lists
(6) and every preceding coefficient is at least \(B_0\).
The common disk, strip and phase bounds do not depend on the
number of preceding coefficients. The phase is the original
marked geometric phase, with its absolute real volume constant.
The same statement holds after mirroring the entire word.

**Proof.** The initial family has the common constants just
specified. The proof of the fixed-domain long-power theorem
depends only on those constants and on the original bare edge.
Choose its thresholds after enlarging the initial family by the
two finite pieces in (6). Starting at the last piece, prepend
the earlier powers one at a time by
\(F\mapsto T(R^nF)\), \(|n|\ge B_0\). Each operation restores
the same boundary class, has a nonzero leading coefficient,
and retains the full quotient and normal data. Its marked
geometric composition retains the original primitive curves
and integrates from the complete child volume. This is also
the one-child case of Corollary 2 in
[the enlarged hybrid-tree theorem](research_three_crossing_long_closing_fiber.md).
The number of operations is arbitrary but fixed before
\(N\to\infty\). \(\square\)

In particular, (2)--(3), followed by the finite suffix test in
(6), gives an arithmetic sufficient criterion for an arbitrary
fixed rational presentation. An outer power \(R^r\) in (4)
is retained; it is not silently removed from the boundary
function.

## 3. Original filling parameters after replacement

Suppose this fixed terminal piece is attached at a vertex whose
original crossing power is
\[
                       n=\eta-2p,
 \tag{10}
\]
where \(\eta\) is its fixed carrier and \(p\in\mathbb Z\) is
the free original filling coefficient. Equation (5) is first
inserted in the original full contraction. The outer \(R^r\)
then combines with \(R^n\), giving the exact effective power
\[
                       n+r=\eta+r-2p.
 \tag{11}
\]
For several fixed child replacements, use the sum of their
outer powers in place of \(r\). The original variable \(p\)
is never identified with another assignment.

If the carrier is put back in \(\{0,1\}\), choose
\(\eta'\equiv\eta+r\pmod2\), set
\(s=(\eta+r-\eta')/2\), and write
\[
                  p'=p-s,\qquad n+r=\eta'-2p'.
 \tag{12}
\]
The primitive basis change is
\(\lambda\mapsto\lambda'\),
\(\mu\mapsto\mu'-s\lambda'\), so that the original slope
\(\mu+p\lambda\) becomes precisely
\(\mu'+p'\lambda'\). This translation is a bijection of the
free integer parameter, not a quotient of its fibers.

This is the disk-cut convention in Section 5 of
[the marked degree-two moves](research_marked_degree_two_tangle_moves.md):
its integer basis coefficient is
\(k=(\eta'-\eta-r)/2=-s\). The immediate change of carrier
from \(\eta\) to \(\eta+r\) leaves \(p\) unchanged;
only its subsequent normalization transfers these full twists
to the disk filling. For \(r=1\) and \(\eta\in\{0,1\}\),
one has \(s=\eta\), exactly as in equation (14) of
[the binary complementary-word theorem](research_binary_negative_corridor_positive_reexpression.md).
All disk and longitude orientations are transported by the
marked isotopy. If a redraw reverses the disk orientation,
both peripheral orientations must first be transported; an
unrecorded orientation reversal is not part of (12).

**Corollary 2.** If the list in (3) meets Theorem 1, a
sufficiently long fixed final closing power \(n+r\) gives the
original Kashaev volume identity, under the original component
and framing conditions. For each fixed original word \(W\) and
carrier \(\eta\), all but finitely many original integers
\(p\) satisfy this sufficient condition. The same replacement
can be used at a pendant leaf of the proved hybrid tree class,
with every effective attaching power and every original
component condition retained.

**Proof.** Apply the scalar closing theorem, or the hybrid tree
theorem, to the transformed contraction. Equation (5) contributes
only the displayed unit \(\kappa_N^{\ell_{\rm cap}}\).
The boundary isotopy identifies the actual knot and its marked
filling slopes, so the geometric action is the volume of that
knot complement. For a closing threshold \(B\), the untreated
integers satisfy \(|\eta+r-2p|<B\), a bounded interval.
No assertion about those finitely many values is made. \(\square\)

The fixed-word qualification matters. If powers inside \(W\)
also vary, its normal form and its outer shift can change.
The criterion may be applied to each fixed stratum, but finite
exceptions on each such stratum do not imply finite exceptions
in their union. Zero reductions that merge two free powers
still have their original infinite fibers.

## 4. A family with two consecutive short complementary powers

Here is a concrete consequence that allows arbitrary word
length. Let
\[
 \mathbf b=(2^{r_0},3,2^{r_1},3,\ldots,3,2^{r_k}),
 \quad k\ge1,\quad r_0\ge1,\quad r_j\ge0\ (j>0),
 \tag{13}
\]
where \(2^r\) means a string of \(r\) entries, all equal to
two. There are \(k\) threes and
\(m=k+\sum_{j=0}^k r_j\) entries in all. Unlike the earlier
binary-chain statement, the final string is allowed to be
empty. Define
\[
 \mathbf c=(r_0+2,r_1+3,\ldots,r_{k-1}+3,r_k+2).
 \tag{14}
\]
Then
\[
 \frac{[\mathbf b]_-}{[\mathbf b]_--1}=[\mathbf c]_-.
 \tag{15}
\]
One proof starts with the terminal coefficient and uses the
elementary rule that prepending two increments the first
complementary entry, while prepending three inserts a two
and increments the former first entry. A final three starts
with the complementary list \((2,2)\). This proves (14)
also when \(r_k=0\); it is not a limiting argument.

The marked identity and exact scalar are
\[
 \begin{split}
 TR^{-b_1}T\cdots TR^{-b_m}(I)
       &\simeq R\,TR^{c_1}T\cdots TR^{c_{k+1}}(I),\\
 F_{\mathbf b,-,N}
       &=\kappa_N^{-(m+k)}R F_{\mathbf c,+,N}.
 \end{split}
 \tag{16}
\]
For the scalar, multiplication of (1), using the same recursion
that proves (14), gives the full linear identity
\[
 SA_{-b_1}\cdots SA_{-b_m}
   =A_1SA_{c_1}\cdots SA_{c_{k+1}}SA_1S^{-1}
       \quad\text{in }\mathrm{PSL}_2(\mathbb Z).
 \tag{16a}
\]
The base lists \((2)\) and \((3)\) have complements \((2)\)
and \((2,2)\). The two induction identities are
\(SA_{-1}S=-A_1SA_1\) and
\(SA_{-2}S=-A_1SA_2SA_1\); these follow by multiplication
of the displayed two-by-two matrices. After the leading
\(A_1\) in (16a), they are exactly the operations of prepending
two or three. Thus the calculation also retains the empty
final run. The relative cap matrix is
\(SA_1S^{-1}=\left(\begin{smallmatrix}1&0\\-1&1\end{smallmatrix}\right)\).
The crossing sums are \(-(2m+k)\) and \(m+2k+2\), including
the outer positive crossing. Substitution in (5), with
\(h=-1\), gives exactly \(-(m+k)\). The full affine
cap comparison is the same as in
[the complementary-word theorem](research_binary_negative_corridor_positive_reexpression.md).

**Corollary 3.** In (13), choose \(r_k\in\{0,1\}\).
If \(k=1\), require \(r_0=1\). If \(k\ge2\), require
\[
 \begin{split}
 r_{k-1}&=0,\\
 r_0&\ge\max(1,B_0-2),\\
 r_j&\ge\max(0,B_0-3)\qquad(1\le j\le k-2).
 \end{split}
 \tag{17}
\]
Then the original negative word has a nonzero complete boundary
asymptotic and a whole-period strip estimate. A sufficiently
long signed final closing power, translated by \(+1\) as in
(16), gives the original volume identity whenever the original
closure is a knot. The mirrored statement holds as well.

**Proof.** The final two entries in (14) are \((3,2)\) if
\(r_k=0\), and \((3,3)\) if \(r_k=1\). All preceding
entries meet Theorem 1. Equation (16) and the fixed-power
boundary-multiplication theorem transfer its whole-boundary
estimate to the original negative presentation. Equivalently,
for the final scalar contraction combine the outer crossing
with the original closing power before applying Corollary 2.
The parameter translation is exactly (11), with \(r=1\).
\(\square\)

Thus the original negative chain may end with the short powers
\((-3,-3)\), or with \((-3,-3,-2)\), after arbitrarily many
earlier threes separated by the specified long strings of twos.
The case \(k=1\) gives the initial words \((-2,-3)\) and
\((-2,-3,-2)\). These are consequences of the mixed and
adjacent-three theorems, respectively. The conclusion is a
family statement with no upper bound on \(k\); the sufficient
threshold was chosen before the word length.

## 5. A further allowed sequence and the remaining obstruction

The reset lemma in
[the alternating-turn theorem](research_alternating_long_and_nonzero_turns.md)
applies to any controlled class with (8)--(9). A single
sufficiently long turn therefore sends any of the initial
pieces (6) into that theorem's fixed bare-edge class. After
this first turn one may repeatedly apply
\[
             F\longmapsto T\bigl(R^bT(R^nF)\bigr),
             \qquad b\ne0,\quad |n|\ge B_1,
 \tag{18}
\]
with one finite \(B_1\) independent of all the nonzero
integers \(b\) and the number of stages. This gives another
explicit class of rational presentations recognizable from
their words. The threshold for the first reset is fixed for
the finite enlargement (6), and is chosen separately from
\(B_1\). It may be included in their maximum. Geometric
periods and original component conditions are those retained
by the cited reset and composition theorems.

None of these reductions removes arbitrary adjacent short
nonzero powers. The positive expansion (3) is unique with its
fixed outside frame and outer integral twist. If it has a
short coefficient immediately outside a proved suffix, a
long-turn theorem cannot be used there. The operation (18)
also needs its specified long partner. Nor may the seed
\((3,3)\) be cut out of the middle of a longer word: that
would require an estimate with two independent free boundary
variables. The next general extension must therefore prove
a new stable composition operation or a theorem for these
connected short pieces. Exact rational classification alone
does not establish their nonzero quantum contribution.
