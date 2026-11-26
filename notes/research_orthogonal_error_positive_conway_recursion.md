# A positive matrix recursion for the original Conway source

22 November 2026. Research note. Frozen manuscripts and earlier final
notes remain unchanged.

The full Conway source has a positive representation which requires no
minimization. At each proper vertex of its expression tree, add a small
orthogonal error space. Contract the original maps and their adjoints,
keeping their complete Gram matrices. The resulting scalar differs
from the squared original invariant by a prescribed, uniformly bounded
additive error.

This construction uses the actual closing functional and the full
repeated-root boundary algebra. It gives local positive-matrix lower
and upper certificates. Their hyperbolic-volume rate is not evaluated
here.

## 1. The normalized original tree

Use the complete normalized compiler in the
[convex source theorem](research_convex_normalized_conway_source.md).
There is a fixed finite rooted expression tree. Its proper vertices
are leaves, unary linear maps, or binary complex-bilinear maps. The
root is the prescribed original complex-linear closing row.

At level \(N\ge2\), each proper boundary space is the entire
\[
 H_N=\mathbb C[\zeta]/(2T_N(\zeta/2)+2)\cong\mathbb C^N,
 \tag{1}
\]
with its declared Newton coefficient Hermitian metric. Here \(T_N\)
is the Chebyshev polynomial of the first kind. Value and derivative
directions at repeated roots both remain in this space. All adjoints
below are in this fixed metric.

Let \(b_v=16\max(1,\|T_v\|_{\rm HS})\) be the known local budgets,
including the root budget, and put
\[
 B_N=\prod_v b_v,\qquad \sigma=\frac1{16}.
 \tag{2}
\]
The coefficients of every local tensor \(T_v\) are prescribed by
the original construction. In particular \(B_N\ge1\) is known
without evaluating the closed invariant. After dividing each tensor
by its own budget, write its leaf vector as \(a_v\), its unary map as
\(A_v\), its bilinear map as \(M_v\), and its original closing row
as \(L\). Each has norm at most \(\sigma\); for a bilinear map this
means
\[
             \|M_v(u,w)\|\le\sigma\|u\|\,\|w\|.
 \tag{3}
\]
The normalized true packets, also denoted \(a_v\), obey
\[
 a_v=A_va_c\quad\hbox{or}\quad a_v=M_v(a_l,a_r),\qquad
 \|a_v\|\le\sigma,\qquad
 La_{\rm top}=K_N/B_N.
 \tag{4}
\]
At a leaf \(a_v\) is prescribed; at other vertices (4) defines it.
The invariant \(K_N\) is the original reduced Kashaev invariant
with the recorded marking, phases and framing normalization. It is
not an input to the construction below.

An expression is a literal tree: distinct child occurrences have
disjoint sets of descendants. Repeated equal-looking subexpressions
are kept as separate occurrences.

For a bilinear map, the same letter \(M_v\) denotes its linearization
from \(H_N\otimes H_N\) to \(H_N\). For Hermitian matrices,
\(U\preceq V\) means that \(V-U\) is positive semidefinite.

## 2. The deterministic matrix recursion

For any real \(\varepsilon>0\), define matrices from the leaves upward:
\[
 \begin{array}{ll}
 S_v=a_va_v^*+\varepsilon I,
       &v\ \hbox{a leaf},\\[2mm]
 S_v=A_vS_cA_v^*+\varepsilon I,
       &v\ \hbox{unary},\\[2mm]
 S_v=M_v(S_l\otimes S_r)M_v^*+\varepsilon I,
       &v\ \hbox{binary}.
 \end{array}
 \tag{5}
\]
All matrices in (5) are \(N\)-by-\(N\) and strictly positive definite.
The binary operation is positive and order preserving in either
matrix argument with the other held positive. Equivalently, one
applies the positive linear map \(U\mapsto M_vUM_v^*\) to the
tensor-product input. Joint linearity in the two matrices is not
asserted.

Retain the actual root row and set
\[
       F_N(\varepsilon)=B_N^2 L S_{\rm top}(\varepsilon)L^*.
 \tag{6}
\]
Equations (2), (5), and (6) prescribe this number entirely by local
source data. No true internal packet from (4), except the prescribed
leaf vectors, is needed to evaluate (5).

**Theorem.** Fix \(0<\theta\le1\), and choose
\[
            \varepsilon_N=\frac{\theta}{N B_N^2},
       \qquad P_N=1+F_N(\varepsilon_N).
 \tag{7}
\]
For every level and every such normalized tree,
\[
 \boxed{\qquad
 0\le F_N(\varepsilon_N)-|K_N|^2\le\frac{\theta}{128},
 \qquad
 1+|K_N|^2\le P_N\le1+|K_N|^2+\frac{\theta}{128}.
 \qquad}
 \tag{8}
\]
The bounds include exact zeros. They hold for both level parities
and composite levels because they use the full compiler, not a
distinct-root quotient.

## 3. Orthogonality and the error bound

Here is a finite Fourier interpretation and proof. At each proper
vertex take an independent variable \(\omega_v\), uniform on
\(\mathbb Z/(N+1)\). Let
\(\chi_j(\omega)=\exp(2\pi i j\omega/(N+1))\), and choose an
orthonormal basis \(e_1,\ldots,e_N\) of \(H_N\). Define
\[
          \xi_v=\sqrt{\varepsilon}
                         \sum_{j=1}^N\chi_j(\omega_v)e_j.
 \tag{9}
\]
Character orthogonality gives
\[
       \mathbb E\xi_v=0,\qquad
       \mathbb E(\xi_v\xi_v^*)=\varepsilon I,\qquad
       \mathbb E\|\xi_v\|^2=N\varepsilon.
 \tag{10}
\]
Define random packets by the original maps:
\[
 X_v=a_v+\xi_v\quad\hbox{at a leaf},\qquad
 X_v=A_vX_c+\xi_v,\qquad
 X_v=M_v(X_l,X_r)+\xi_v.
 \tag{11}
\]
Child subtrees are independent, and the fresh error at their parent
is independent of both. Induction therefore gives
\[
           \mathbb E X_v=a_v,\qquad
           \mathbb E(X_vX_v^*)=S_v.
 \tag{12}
\]
For the second identity at a binary vertex, use the exact equality
\(\mathbb E[(X_lX_l^*)\otimes(X_rX_r^*)]=S_l\otimes S_r\).
The adjoint in (5) conjugates the entire original map, including
its phases. Its entries are not squared separately.

Put
\[
 V_v=\mathbb E[(X_v-a_v)(X_v-a_v)^*]\succeq0,\qquad
 t_v=\operatorname{tr}V_v,\qquad h=N\varepsilon.
 \tag{13}
\]
Thus \(S_v=a_va_v^*+V_v\). At a binary vertex, writing
\(\delta_c=X_c-a_c\), the three propagated fluctuations are
\[
       M_v(a_l,\delta_r),\quad M_v(\delta_l,a_r),
                       \quad M_v(\delta_l,\delta_r).
 \tag{14}
\]
Their pairwise \(L^2\) inner products vanish: in each cross term
one independent centered child fluctuation occurs only once.
The fresh error is orthogonal to all three. In matrix form,
\[
 \begin{split}
 V_v={}&M_v\bigl(a_la_l^*\otimes V_r+
                  V_l\otimes a_ra_r^*+V_l\otimes V_r\bigr)M_v^*
                  +\varepsilon I .
 \end{split}
 \tag{15}
\]
Using (3), (4), independence and (10) consequently gives
\[
 \begin{array}{ll}
 t_v=h,&v\ \hbox{a leaf},\\
 t_v\le\sigma^2t_c+h,&v\ \hbox{unary},\\
 t_v\le\sigma^4(t_l+t_r)+\sigma^2t_lt_r+h,
                                      &v\ \hbox{binary}.
 \end{array}
 \tag{16}
\]
If \(h\le1\), induction shows \(t_v\le2h\) at every vertex.
For a unary vertex use \(1+2\sigma^2<2\). For a binary vertex,
\[
 \sigma^4(2h+2h)+\sigma^2(2h)^2+h
             =h(1+4\sigma^4+4\sigma^2h)<2h.
 \tag{17}
\]
These estimates do not accumulate a factor for the number of
vertices.

At the unchanged original closing,
\[
 F_N(\varepsilon)=|K_N|^2+B_N^2 L V_{\rm top}L^*,\qquad
 0\le B_N^2 L V_{\rm top}L^*
                   \le2\sigma^2B_N^2N\varepsilon.
 \tag{18}
\]
The choice (7) has \(h=\theta/B_N^2\le1\), and
\(2\sigma^2=1/128\). This proves (8).

The probability space in (9) is a proof device for a finite
orthogonal expansion. Evaluation of (5) requires no random
sampling, Gaussian integration or limiting operation.

## 4. A scalar polynomial of degree bounded by the number of leaves

There is a second fixed-degree simplification. If the original
tree has \(l\) leaf occurrences, then
\[
 F_N(\varepsilon)=|K_N|^2+
                 \sum_{j=1}^{l}c_{N,j}\varepsilon^j,
                  \qquad c_{N,j}\ge0.
 \tag{19}
\]
Indeed each \(S_v(\varepsilon)\) is a matrix polynomial with
positive semidefinite coefficient matrices. This holds at a leaf,
is preserved by \(A_v S A_v^*\), and is preserved by tensoring
the two polynomial matrices and applying \(M_v(\,\cdot\,)M_v^*\).
Adding \(\varepsilon I\) preserves the assertion. The degree is
at most one at a leaf, unchanged along a unary corridor, and at
most the sum of the child degrees at a binary vertex. The constant
coefficient is \(a_va_v^*\) by (4). Applying \(L\) proves (19).

More explicitly, an antichain is a set of proper vertices no one of
which is an ancestor of another. Let \(C_A\) be the original
normalized scalar expression with the subtrees at the vertices of
an antichain \(A\) replaced by free \(H_N\) inputs. All other
subtrees and the original closing remain as prescribed. Then
\[
 F_N(\varepsilon)=|K_N|^2+
 B_N^2\sum_{\substack{A\ne\varnothing\\A\ {\rm antichain}}}
                      \varepsilon^{|A|}\|C_A\|_{\rm HS}^2.
 \tag{20}
\]
To see this, expand (11) using bilinearity. Choosing a fresh
\(\xi_v\) replaces its entire subtree, so a surviving term uses
an antichain of error vertices. Different antichains are orthogonal:
an error variable present in just one term has mean zero.
For the same antichain, (10) contracts the full coefficient tensor
with its adjoint, giving its Hilbert--Schmidt norm. An antichain
has at most \(l\) vertices, since their descendant leaf sets are
disjoint. This also proves the degree bound.

The nonnegative coefficients in (19) are squared norms of complete
exterior contexts. Signed terms within a context are still assembled
before taking its norm. Formula (19) does not make the original
scalar state-sum coefficients nonnegative.

### Errors only at the original leaves

The internal additions in (5) can also be omitted. Define
\(\widetilde S_v=a_va_v^*+\varepsilon I\) at each original leaf,
and propagate by
\[
 \widetilde S_v=A_v\widetilde S_cA_v^*,\qquad
 \widetilde S_v=M_v(\widetilde S_l\otimes\widetilde S_r)M_v^*
 \tag{20a}
\]
at internal vertices. These matrices are positive semidefinite;
strict definiteness for an arbitrary unary map is not required.
The same independent-error proof applies, with no fresh internal
error. Now the covariance trace is at most \(h=N\varepsilon\le1\):
it equals \(h\) at leaves, is at most \(\sigma^2h\) after a unary
map, and at a binary map is at most
\(\sigma^2(2\sigma^2h+h^2)\le h\).
Consequently, at the same choice (7),
\[
 0\le B_N^2 L\widetilde S_{\rm top}L^*-|K_N|^2
                                      \le\frac{\theta}{256}.
 \tag{20b}
\]

Writing \(\mathcal B_E:H_N^{\otimes l}\to H_N\) for the
normalized synthesis map of the original expression, the exact
formula is simply
\[
 \widetilde S_{\rm top}
   =\mathcal B_E\!
       \left[\bigotimes_{\ell\ {\rm leaf}}
                  (a_\ell a_\ell^*+\varepsilon I)\right]
                      \mathcal B_E^* .
 \tag{20c}
\]
The nonconstant coefficients now correspond to subsets of leaves.
Equation (20c) is the usual weighted synthesis covariance; the
additional assertion here is its calibrated additive comparison
with the same filled source. This version needs orthogonal error
labels only at the original leaves. The all-vertex version gives a
strict positive floor at every intermediate packet independently of
the ranks of the maps.

## 5. Local matrix certificates

One need not evaluate the exact messages to obtain rigorous bounds.
Suppose positive semidefinite matrices \(Q_v^-\) satisfy the
following local inequalities, with the same \(\varepsilon_N\):
\[
 \begin{array}{ll}
 Q_v^-\preceq a_va_v^*+\varepsilon_N I,&v\ \hbox{a leaf},\\
 Q_v^-\preceq A_vQ_c^-A_v^*+\varepsilon_N I,&v\ \hbox{unary},\\
 Q_v^-\preceq M_v(Q_l^-\otimes Q_r^-)M_v^*+\varepsilon_N I,
                                             &v\ \hbox{binary}.
 \end{array}
 \tag{21}
\]
Likewise let positive semidefinite \(Q_v^+\) satisfy the reversed
inequalities. Then
\[
 Q_v^-\preceq S_v\preceq Q_v^+
 \tag{22}
\]
by induction. The tensor-product step follows from
\[
 S_l\otimes S_r-Q_l^-\otimes Q_r^-
  =(S_l-Q_l^-)\otimes S_r+
                         Q_l^-\otimes(S_r-Q_r^-)\succeq0,
 \tag{23}
\]
and the analogous identity for the upper comparison.
Combining (8), (18), and (22) gives
\[
 \boxed{\quad
 \max\!\left(0,B_N^2LQ_{\rm top}^-L^*-\frac{\theta}{128}\right)
       \le |K_N|^2\le B_N^2LQ_{\rm top}^+L^*.
 \quad}
 \tag{24}
\]
The matrices can have off-diagonal entries. Replacing them by their
diagonals is not justified by these inequalities.

For a hyperbolic knot complement of volume \(V>0\), one sufficient
geometric target is a family of such messages for which, eventually,
the two root observations are positive and
\[
 \liminf_{N\to\infty}\frac{\pi}{N}
                   \log(B_N^2LQ_{\rm top}^-L^*)\ge V,\qquad
 \limsup_{N\to\infty}\frac{\pi}{N}
                   \log(B_N^2LQ_{\rm top}^+L^*)\le V.
 \tag{25}
\]
The lower observation then grows exponentially; subtracting the
fixed constant in (24) does not change its rate. The original
volume identity follows by squeezing. No such geometric message
family is constructed in this note.

## 6. Scope and sources

At \(\varepsilon=0\), (5) is simply the exact rank-one contraction
of the original source with its conjugate. The additional result is
the explicit strictly positive regularization and its uniform
unnormalized error bound. It avoids a variational solve but retains
the full matrix size, precision requirements and coherent phases.
The chosen \(\varepsilon_N\) can be exponentially small because the
known budget \(B_N\) can grow exponentially.

The two sides of (8) imply, for every \(V>0\),
\[
 \frac{\pi}{N}\log P_N\longrightarrow V
 \quad\Longleftrightarrow\quad
 \frac{2\pi}{N}\log|K_N|\longrightarrow V.
 \tag{26}
\]
Indeed \(P_N\) differs from \(1+|K_N|^2\) by a bounded additive
quantity. A positive limiting rate implies eventual nonvanishing
of \(K_N\). This is a finite-level comparison, not a proof of either
limit.

Every fixed short partial filling can be inserted into its actual
leaf data, or contracted as a full open subtree before recompiling.
The theorem therefore has no restriction on short words. The
finite-exception program still needs (25), or the equivalent
geometric rate of (5), for every required fixed short partial
filling and sufficiently long remaining hyperbolic completions.
Local saddle existence and strict angle-volume concavity alone
do not supply the full-matrix inequalities (21).

The sole direct proof source is the complete normalized compiler
and its norm bounds:

| Source | SHA-256 |
|---|---|
| [Normalized complete Conway source](research_convex_normalized_conway_source.md) | 6b89b4c6a67ef7a32cc41a5966c650f32de65d284ae7b70d94a71bddba21df3c |

Second-moment contraction of a tensor with its conjugate and
transfer operators are standard. For literature coverage, see
[Schollwöck, sections 4.2.1–4.2.2](https://arxiv.org/abs/1008.3477).
No estimate from that reference is used in this proof, and no
novelty is claimed for those general operations. The statement here
is the calibrated additive comparison with the original Conway
source, together with its local matrix certificates.

Only written mathematics, source reads and text operations were used.
No mathematical program, numerical experiment, test, build, git
operation or public-document edit was performed.
