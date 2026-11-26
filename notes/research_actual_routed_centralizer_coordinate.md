# An actual routed coordinate conjugate to the framing Ward field

Private written proof, 18 November 2026.

An explicit insertion in the original finite tensor source has
principal symbol \(t=r/s\) on a fixed irreducible complete framing
family. Its commutator with the actual weighted Ward current has
principal value one on that family. The insertion uses the ordered
meridian prefixes and only inverses of the original \(K\) matrices.
It is not an observable of the single cut alone.

All finite commutator corrections, cut and pivotal currents, and
marked-word defects are retained below. The result supplies a source
coordinate and an exact product-current identity. It does not give
an exact Heisenberg relation, a bound for the correction, or a
pushforward of the original relative cycle.

The complete proof directs are M, the actual marked braid holonomy,
and W, its weighted finite Ward lift, pinned below.

## 1. A coordinate on the actual framing family

Fix an irreducible complete representation of the knot group in
M's braid presentation, with its first physical meridian normalized
to
\[
 J_1=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
 \tag{1}
\]
Retain the central lift and the selected eigenflag. The other
physical meridians at the initial braid level generate the same
knot group with this first meridian. At least one of them has
the form
\[
 H^0=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad c\ne0.
 \tag{2}
\]
Indeed, if all their lower-left entries vanished, they would all
preserve the line spanned by \((1,0)^t\), contradicting
irreducibility. Fix one such meridian, at head \(j\), and its four
reference constants. They may lie in the chosen representation's
coefficient field; no rationality assumption on that field is used.

The selected-flag framing of M/W is
\[
 F(r,s)=\begin{pmatrix}r&1-r\\s&-s\end{pmatrix},\qquad s\ne0,
 \qquad
 \mu_1=F^{-1}J_1F,\qquad \mu_j=F^{-1}H^0F .
 \tag{3}
\]
It has
\[
 F^{-1}=
 \begin{pmatrix}1&(1-r)/s\\1&-r/s\end{pmatrix}.
\]
Subtracting its second row from its first gives \((0,1/s)\).
Multiplication by \(H^0\) and by the first column \((r,s)^t\)
of \(F\) therefore proves
\[
 (\mu_j)_{11}-(\mu_j)_{21}=\frac{cr+ds}{s}.
 \tag{4}
\]
Consequently the rational meridian expression
\[
 \tau=\frac{(\mu_j)_{11}-(\mu_j)_{21}-d}{c}
 \tag{5}
\]
restricts exactly to \(t=r/s\) on this whole framing family.
No choice of a fixed cut value \(s=s_\theta\) is needed for (5).

W proves that the actual weighted centralizer field restricts to
\[
                         \mathscr V=s\partial_r .
 \tag{6}
\]
Thus \(\mathscr V\tau=1\) on (3). This is a statement on the
framing family of the fixed reference representation. The same
expression (5) is defined on a larger regular phase chart, but
its derivative is not asserted to be one at every neighboring
representation.

There is a useful explicit check on this qualification. On the
slice with
\[
 \mu_1=\begin{pmatrix}1+s&-s\\s&1-s\end{pmatrix},
\]
put \(J=\left(\begin{smallmatrix}1&-1\\1&-1\end{smallmatrix}\right)\).
For any matrix \(Z\), the first-column difference of
\([-sJ,Z]\) is
\(s(Z_{11}+Z_{12}-Z_{21}-Z_{22})\). Hence the derivative of
(5), with \(\mu_j\) replaced by \(Z\), is
\[
                 \frac{\operatorname{tr}((\mu_1-I)Z)}{c}.
 \tag{7}
\]
On (3) the numerator is
\(\operatorname{tr}((J_1-I)H^0)=c\). Away from that fixed
conjugacy family it need not equal this reference constant.

## 2. The literal finite insertion and its ordering

Use W's factorial basis on each of the \(b\) physical heads,
with \(N\ge2\), \(q=e^{\pi i/N}\), \(Q=q^2\), \(h=2\pi i/N\),
and \(x=-M/q\). Keep its matrices
\[
\begin{split}
 K e_a&=xQ^{-a}e_a,\\
 \mathcal E e_a&=(MQ^{-a}-M^{-1})e_{a-1}\quad(a>0),
                  &\mathcal E e_0&=0,\\
 F e_a&=(1-Q^{a+1})e_{a+1}\quad(a<N-1),
                  &F e_{N-1}&=0 .
\end{split}
 \tag{8}
\]
The two missing arrows are zero matrices, not continued interior
entries. Every \(K\) is invertible for \(q,M\ne0\).

Auxiliary two-by-two matrices below have entries in the actual
endomorphism algebra of the tensor heads. Their products are
noncommutative products in the displayed order. Define
\[
 \widehat b_{-,i}=
   \begin{pmatrix}I&0\\-K_iF_i&K_i\end{pmatrix},\qquad
 \widehat b_{-,i}^{-1}=
   \begin{pmatrix}I&0\\F_i&K_i^{-1}\end{pmatrix},
 \tag{9}
\]
\[
 \widehat G_i=
   \begin{pmatrix}K_i&\mathcal E_i\\
             K_iF_i&K_i^{-1}+\mathcal E_iF_i\end{pmatrix}.
 \tag{10}
\]
Both products of the two matrices in (9) are the identity:
their lower-left entries cancel as
\(-K_iF_i+K_iF_i\) and \(F_i-K_i^{-1}K_iF_i\).
Thus (9) is an exact inverse, without assuming commutativity
of \(K_i,F_i\).

Set
\[
 \widehat B_{j-1}=\widehat b_{-,j-1}\cdots\widehat b_{-,1},
 \qquad
 \widehat B_{j-1}^{-1}
   =\widehat b_{-,1}^{-1}\cdots\widehat b_{-,j-1}^{-1},
 \tag{11}
\]
\[
 \widehat\mu_j
       =-\widehat B_{j-1}^{-1}\widehat G_j\widehat B_{j-1},
 \qquad
 \boxed{\quad
 \widehat T=
  \frac{(\widehat\mu_j)_{11}-(\widehat\mu_j)_{21}-dI}{c}.
 \quad}
 \tag{12}
\]
The minus sign is essential: M's prefixed matrix is \(H_j\),
whereas its physical meridian is \(\mu_j=-H_j\).
Formula (12) is a specified finite tensor insertion. It divides
only by the nonzero reference scalar \(c\) and the diagonal
Gauss units \(K_i\); no occupation, raising arrow, meridian gap,
or quantum dimension is inverted.

The commuting principal symbols of (9)--(12) are exactly M's
ordered prefix formulas. W's regular interior symbol calculus
therefore identifies the symbol of \(\widehat T\) with (5).
In particular it is \(r/s\) on (3). No noncommutative determinant
or exact quantum Hurwitz identity for \(\widehat\mu_j\) is needed
or asserted.

The insertion can be placed at that specified initial braid level
in the original source. Moving it to another level requires the
actual braid conjugation, with its order retained; it is not
replaced by an unprefixed one-head matrix. Its expansion is a
finite sum of original generator insertions on the prefix heads.
All their intermediate head indices and zero endpoints remain
the original finite ones.

## 3. Exact commutator with the sourced Ward current

Let \(X_E=\mathsf E,X_F=\mathsf F,X_K=\mathsf K\) be W's original
ordered coproduct matrices. Keep W's ordered coefficient matrices
\(A_E,A_F,A_K\), chosen there from the first physical meridian.
Its actual divergence-form current is
\[
 \mathcal D_N(B)=\frac1h\sum_{\iota=E,F,K}
                                  [X_\iota,A_\iota B].
 \tag{13}
\]
For left multiplication \(M_{\widehat T}(B)=\widehat T B\),
ordinary multiplication in the finite matrix algebra gives
\[
 \boxed{\quad
 [\mathcal D_N,M_{\widehat T}](B)
  =\frac1h\sum_\iota
       \left([X_\iota,\widehat T]A_\iota B
               +[X_\iota,[A_\iota,\widehat T]B]\right).
 \quad}
 \tag{14}
\]
Indeed, write
\(A_\iota\widehat T=\widehat T A_\iota+
[A_\iota,\widehat T]\) inside
\([X_\iota,A_\iota\widehat T B]\), and then subtract
\(\widehat T[X_\iota,A_\iota B]\). This proves (14)
with no interchange of the coefficients or omission of a
commutator.

For a fixed regular interior symbol \(b\), the first term of
(14) has principal symbol
\[
 \sum_\iota\{x_\iota,\tau\}\alpha_\iota b
                         =(\mathscr V\tau)b .
 \tag{15}
\]
The second term has zero principal symbol: the inner coefficient
commutator is of order \(h\), and the outer commutator has one
further factor \(h\), before the displayed division by \(h\).
Equivalently, W's principal operator is
\(\mathscr V+\operatorname{div}\mathscr V\); its commutator
with multiplication by \(\tau\) is multiplication by
\(\mathscr V\tau\). Restricting (15) to (3) gives the identity
operator.

Define the exact finite correction
\[
                    \mathcal A_N
       =[\mathcal D_N,M_{\widehat T}]-\operatorname{Id}.
 \tag{16}
\]
Its principal symbol vanishes after restriction to (3).
This does not assert that its ambient principal symbol vanishes:
there it is \((\mathscr V\tau-1)b\), as (7) illustrates.
Nor is the regular symbolic order statement for the second term
of (14) a norm estimate on whole heads, endpoint rows, growing
marks, or transported contours.

For every fixed polynomial \(p(t)=\sum_kp_kt^k\), the elementary
commutator rule gives an exact formula retaining all corrections:
\[
 [\mathcal D_N,M_{p(\widehat T)}]
       =M_{p'(\widehat T)}+\mathcal A_{N,p},
 \tag{17}
\]
\[
 \mathcal A_{N,p}
   =\sum_{k\ge1}p_k\sum_{\ell=0}^{k-1}
       M_{\widehat T}^{\,\ell}\mathcal A_N
                         M_{\widehat T}^{\,k-1-\ell}.
 \tag{18}
\]
Its restricted principal symbol is zero for a fixed polynomial.
No degree-uniform estimate is included.

## 4. Original boundary, marked defects, and genuine normals

Let \(P\) be the prescribed finite cut tensor with all original
pivots, and let \(O\) be the whole marked word. For the highest
presentation W has \(P=T_0\otimes g^{\otimes(b-1)}\).
An explicitly chosen trace-one diagonal cut is a different
presentation with that same \(P\) replaced throughout; none of
the following algebra discards its marked defect. Keep the
whole scalar framing/peripheral line \(\varkappa_\beta\), and put
\[
 \Phi_O(B)=\varkappa_\beta\operatorname{Tr}(PBO),
\]
\[
 \mathcal C_P(B,O)=\frac{\varkappa_\beta}{h}\sum_\iota
 \left\{\operatorname{Tr}([P,X_\iota]A_\iota BO)
       +\operatorname{Tr}(PA_\iota B[O,X_\iota])\right\}.
 \tag{19}
\]
W's literal cyclic-trace calculation is
\(\Phi_O(\mathcal D_N(B))=\mathcal C_P(B,O)\).
Combining it with (17) gives
\[
 \boxed{\quad
 \Phi_O(p'(\widehat T)B)
   =\mathcal C_P(p(\widehat T)B,O)
       -\Phi_O(p(\widehat T)\mathcal D_N(B))
       -\Phi_O(\mathcal A_{N,p}(B)).
 \quad}
 \tag{20}
\]
This is an exact source identity for the routed coordinate.
For \(p=t\), it expresses the unit insertion in terms of the
specified boundary current, the retained divergence current,
and the explicit correction (16). It does not set any of these
three terms to its principal value.

In particular
\(\mathcal D_N(I)=h^{-1}\sum_\iota[X_\iota,A_\iota]\)
is not generally zero. Replacing the divergence-form current
by only its vector-field part would lose this term.
For a marked product \(O=O_k\cdots O_1\), its other defect is
exactly
\[
 [O,X_\iota]=\sum_{\nu=1}^k
 O_k\cdots O_{\nu+1}[O_\nu,X_\iota]O_{\nu-1}\cdots O_1 .
 \tag{21}
\]
Every order and every internal clock or coupon remains.
The cut and tail-pivot commutators in (19) retain W's actual
zero arrows and all finite endpoint coefficients.

Equations (9)--(14) and (17)--(21) are finite matrix identities
wherever their entries and \(h\ne0\) are defined. They can
therefore be differentiated in any specified genuine parameter
germ, including the entries of \(\widehat T\), \(P\), \(O\),
and \(\varkappa_\beta\). For ordinary finite-color quantum
normals one must use the original path \(M=-q^N\), with
the head size \(N\) fixed. A fixed-\(M\) auxiliary continuation
is not relabeled as that path. If an intertwining simplification
is used, it must hold on that entire path; a defect vanishing
only at the root is differentiated in full. The trace identities
themselves require no such simplification.

## 5. What this adapter pays

The actual finite source now contains an explicit routed
observable whose restricted principal value is the centralizer
coordinate, together with its exact product currents. This
is stronger than assigning a Weyl coordinate to an abstract
additive fiber or to a single-cut occupation.

The correction (16), the source boundary (19), and the
divergence term in (20) have not been estimated or transported
to the original relative \(r\)-chain. In particular this is not
an exact finite Heisenberg pair with a computed rank-one
endpoint. Neither a unit framing period, an \(N\)-fold framing
path, nor a nonzero geometric coefficient follows from (20).
Those require the actual current/cycle comparison and its
normalization, including possible same-action endpoint layers.

## Complete proof-source pins

* M: notes/marked_braid_holonomy.md, SHA256
  eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f.
* W: notes/research_actual_weighted_ward_centralizer_lift.md,
  SHA256 e689364ab8e756ef51f8da43a7ea86d84086afd6bf57ffbe0af1a4f508c2648a.

Both complete texts were freshly read nontruncated in the active
author sequence. Their actual meridian signs, prefix order,
finite matrices, principal-field convention, and sourced
commutator identities were checked. Only written mathematics
and text/hash operations were used. Frozen and public files
are unchanged.
