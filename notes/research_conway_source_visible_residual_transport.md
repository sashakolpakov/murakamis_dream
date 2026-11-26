# Source-visible residuals and exact correction on a Conway tree

21 November 2026. Research note; previous finals and public manuscripts
remain unchanged.

A trial boundary packet can have a large error which is nearly invisible
to the prescribed closing functional. Bounding the norm of that error
before applying the closing row loses this information. Here we
transport the actual closing row backwards through the linearization
of the complete Conway compiler. The resulting correction is a coherent
complex scalar. Its remaining error has an explicit quadratic bound.

This is a finite-level error estimate for the original source. It does
not establish that a geometric trial field has a nonzero corrected
closing or the required volume rate. Its advantage over a full-norm
criterion is precise: the first-order error is retained as a
source-visible scalar, and only the nonlinear remainder is bounded by
a norm.

## 1. The normalized physical tree

Use the complete physical boundary data of
[the normalized source theorem](research_convex_normalized_conway_source.md).
At level \(N\ge2\), every proper edge carries the full \(N\)-dimensional
Newton coefficient space \(H_N\), including its repeated-root normal
directions. The original product, turn, signed crossing packets and
marked closing row are unchanged.

There are \(s\ge1\) proper vertices. The closing root has a unique child
\(v_0\). At every physical vertex, including leaves and the closing root,
the known budget is
\[
 b_v=16\max(1,\|T_v\|_{\rm HS}),\qquad \sigma=\frac1{16}.
\]
Let \(B_v\) be the product of the budgets in the proper subtree at \(v\),
and \(B_{\rm tot}\) the product over the whole compiler. If \(f_v\) is
the actual open packet, put \(a_v=f_v/B_v\). Then
\[
 a_v=\Phi_v((a_c)_c),\qquad
 k_N=\frac{K_N}{B_{\rm tot}}=La_{v_0}.
 \tag{1}
\]
Here \(\Phi_v\) is a prescribed constant at a leaf, a linear map at a
turn, and a bilinear map at a product. Each normalized map, constant,
and the original normalized closing row \(L\) has norm at most
\(\sigma\). In particular \(\|a_v\|\le\sigma\).

Choose a feasible trial field
\[
 x=(x_v)_v\in\mathcal D_N
       =\prod_v\{x_v\in H_N:\|x_v\|\le1\}.
\]
Define the error, residual and trial closing by
\[
 e=a-x,\qquad r_v=\Phi_v((x_c)_c)-x_v,\qquad
 r=G(x),\qquad z=Lx_{v_0}.
 \tag{2}
\]
All norms on direct sums are Euclidean. Rows act by their ordinary
complex-linear composition. A star denotes a Hermitian adjoint and is
used only when identifying a row with a vector or estimating a norm.
In particular, complex residual contributions are added before their
absolute values are taken.

## 2. Backward transport of the actual closing row

Let \(A=A(x)\) be the derivative of the map
\(x\mapsto(\Phi_v((x_c)_c))_v\). Thus
\[
                       DG(x)=-I+A.
\]
Its block from a child \(c\) to its proper parent \(v\) is
\(D_c\Phi_v(x)\); all other blocks vanish. Ordering children before
parents makes \(A\) strictly triangular, so \(A^s=0\). Consequently
\[
 (I-A)^{-1}=\sum_{j=0}^{s-1}A^j.
 \tag{3}
\]
Each derivative block has norm at most \(\sigma\). Each row has at
most two child blocks and each child occurs in at most one parent row.
It follows that
\[
 \|A\|\le\sqrt2\sigma\le\frac18,\qquad
                    \|(I-A)^{-1}\|\le\frac87.
 \tag{4}
\]

Let \(c\) be the row on the full direct sum which is \(L\) at \(v_0\)
and zero elsewhere. Define
\[
 d=c(I-A)^{-1},\qquad
 \eta=d^*=(I-A^*)^{-1}c^*.
 \tag{5}
\]
No unknown closed invariant enters (5). The individual rows \(d_v\)
are obtained by the following actual backward recursion:
\[
 d_{v_0}=L,\qquad
            d_c=d_vD_c\Phi_v(x)
       \quad(c\text{ a child of the proper vertex }v).
 \tag{6}
\]
This follows either from \(d=c+dA\) or from the unique path from the
closing root to each vertex. If \(r_v^{\rm dep}\) is the depth of \(v\)
from that root, then
\[
 \|d_v\|\le\sigma^{r_v^{\rm dep}},\qquad
                         \|\eta\|=\|d\|\le\frac1{14}.
 \tag{7}
\]
The second estimate uses (4) and \(\|c\|=\|L\|\le1/16\).
The linearized source error is the computable complex scalar
\[
                         dr=\sum_vd_vr_v=\eta^*r.
 \tag{8}
\]
Equation (8) is not a sum of absolute values and is not a replacement
of the original marked closing row by an ordinary trace.

## 3. The exact nonlinear error identity

For a field \(h\), define \(Q(h)\) to be zero at leaves and turns, and
at a product vertex define
\[
                         Q_v(h)=\Phi_v(h_L,h_R).
 \tag{9}
\]
The exact bilinear expansion of (1) gives
\[
                 (I-A)e=r+Q(e).
 \tag{10}
\]
There is no Taylor remainder beyond (9). Applying the actual source
row to (10) proves
\[
 \boxed{\quad
 k_N=z+dr+\sum_{v\ {\rm product}}d_v\Phi_v(e_L,e_R).
 \quad}
 \tag{11}
\]
Define the corrected trial closing
\[
                         \widehat k(x)=z+dr.
 \tag{12}
\]
Thus the first-order residual has been evaluated in the actual
exterior determined by \(x\), rather than bounded in every exterior.
No direction of the physical boundary space has been quotiented out.

There is a uniform quadratic bound. Since sibling pairs belonging to
different parents are disjoint,
\[
 \begin{split}
 \|Q(h)\|^2
 &\le\sigma^2\sum_{v\ {\rm product}}\|h_L\|^2\|h_R\|^2\\
 &\le\frac{\sigma^2}{4}\|h\|^4.
 \end{split}
 \tag{13}
\]
Integrating \(DG=-I+A\) along the segment from \(x\) to the true field
\(a\), as in the normalized source theorem, gives
\[
                         \|e\|\le\frac87\|r\|.
 \tag{14}
\]
Equations (7), (11), (13) and (14) now imply
\[
 \boxed{\quad
 |k_N-\widehat k(x)|
       \le\frac1{14}\frac1{32}\left(\frac87\right)^2\|r\|^2
       =\frac{\|r\|^2}{343}.
 \quad}
 \tag{15}
\]
If \(dr=0\), the uncorrected closing \(z\) already has this quadratic
error bound. A first-order source-invisible residual is therefore
harmless only after its nonlinear contribution has also been controlled.
Equation (15) does not license discarding an arbitrary residual.

## 4. A sharper local radius

An alternative bound keeps the original incidence and the actual
transported rows. Define nonnegative numbers \(\Delta_v\) upwards
through the tree by
\[
 \Delta_v=\|r_v\|+\sigma\sum_{c\ {\rm child\ of}\ v}\Delta_c.
 \tag{16}
\]
The empty sum at a leaf is zero. Then
\[
                              \|e_v\|\le\Delta_v.
 \tag{17}
\]
For a turn this follows by linearity. For a product use the exact
ordered identity
\[
 \Phi_v(a_L,a_R)-\Phi_v(x_L,x_R)
       =\Phi_v(e_L,a_R)+\Phi_v(x_L,e_R),
 \tag{18}
\]
and the unit-ball bounds on \(a_R,x_L\). Induction proves (17).
The bound can be improved, without changing any conclusion below,
by using the local map norm and the minimum of
\[
 \sigma\Delta_L+\|x_L\|\Delta_R,\qquad
 \|x_R\|\Delta_L+\sigma\Delta_R
 \tag{19}
\]
in place of \(\Delta_L+\Delta_R\) at a product. The factor multiplying
this minimum is \(\|\Phi_v\|_{\rm op}\). Each choice in (19) follows
from one of the two ordered versions of (18), using
\(\|a_L\|,\|a_R\|\le\sigma\).

The explicit local radius is
\[
 \mathcal R_{\rm loc}(x)
   =\sum_{v\ {\rm product}}\|d_v\|\,\|\Phi_v\|_{\rm op}
                                      \Delta_L\Delta_R.
 \tag{20}
\]
Equations (11) and (17) prove
\[
 |k_N-\widehat k(x)|\le
 \mathcal R(x):=\min\left\{\mathcal R_{\rm loc}(x),
                                      \frac{\|r\|^2}{343}\right\}.
 \tag{21}
\]
Thus one backward row flow and one forward scalar majorant flow give
a rigorous source-specific error disk. All operations involve the
actual finite quantum packets and their original phases.

## 5. A phase-sensitive lower bound at one trial field

The error disk immediately gives
\[
 \boxed{\quad
 B_{\rm tot}\max(0,|\widehat k(x)|-\mathcal R(x))
 \le |K_N|
 \le B_{\rm tot}(|\widehat k(x)|+\mathcal R(x)).
 \quad}
 \tag{22}
\]
This does not require minimizing a new function. For a sequence of
feasible trial fields, suppose that eventually
\[
 \mathcal R(x_N)\le(1-\theta_N)|\widehat k(x_N)|,\qquad
 0<\theta_N\le1,\qquad \log\theta_N=o(N).
 \tag{23}
\]
If also
\[
 \frac{2\pi}{N}\log\bigl(B_{\rm tot}|\widehat k(x_N)|\bigr)
                              \longrightarrow V>0,
 \tag{24}
\]
then (22) proves
\[
                         \frac{2\pi}{N}\log|K_N|\longrightarrow V.
 \tag{25}
\]
Indeed the lower and upper factors relative to the center in (22)
are at least \(\theta_N\) and at most \(2\), respectively.

The uniform radius (15) can reduce the required exponential accuracy
of a residual estimate. If the corrected normalized closing has size
\(\exp\{-\alpha N+o(N)\}\), it suffices for its quadratic remainder
to have a strictly smaller rate; for example
\(\|r_N\|\le\exp\{-(\alpha/2+\varepsilon)N+o(N)\}\) with
\(\varepsilon>0\). A direct linear residual disk instead requires
an error on the scale of the closing itself. The correction
\(dr_N\), its complex phase, and the nonzero leading behavior in
(24) must still be established. A formal small residual alone does
not prove a volume lower bound.

## 6. Fixed short components and exact linear corridors

Any fixed proper short subtree may first be contracted to its complete
actual open packet and inserted as one prescribed leaf. Recompute the
known budgets in (1). This preserves the original knot source and all
Hermite directions, including a packet which vanishes on the distinct
Casimir roots but has a nonzero normal part.

Put the true normalized value at such a leaf. Its residual and error
are exactly zero. At a product with one exact child, the corresponding
term \(Q_v(e)=\Phi_v(e_L,e_R)\) in (11) is zero. Attachments through a
sequence of exact short sibling components therefore transport the
remaining error linearly, with their actual complex matrices. The
backward rows in (6) retain those matrices and their phases exactly.
Nonlinear remainder terms occur only where two uncertain branches meet.

This is a structural simplification for arbitrary fixed short
components; it is not a positivity or nonvanishing theorem for their
closing coefficients. The estimates are for the specified original
exterior. They do not declare a direction invisible to every other
possible exterior.

## 7. Exact Newton repair and finite pruning

The correction in (12) has a direct transport interpretation. Solve
the triangular linear system
\[
 (I-A(x))\delta=r,\qquad x^+=x+\delta.
 \tag{26}
\]
Equation (3) makes this an explicit finite operation. Its closing is
exactly
\[
                         Lx^+_{v_0}=z+dr=\widehat k(x).
 \tag{27}
\]
The next residual is exactly
\[
                         G(x^+)=Q(\delta).
 \tag{28}
\]
Expanding \(G\) at \(x\) proves this: the linear terms are
\(r+(-I+A)\delta=0\), and the only remaining terms are (9).
Consequently
\[
                  \|G(x^+)\|\le\frac{2}{49}\|G(x)\|^2.
 \tag{29}
\]
Here \(\|\delta\|\le8\|r\|/7\) and (13) give the stated constant.

All these repairs remain feasible. In fact
\[
              (I-A)x^+=\Phi(x)-Ax.
 \tag{30}
\]
The right side is the prescribed constant at a leaf, zero at a turn,
and \(-\Phi_v(x_L,x_R)\) at a product. Every block has norm at most
\(\sigma\). Solving (30) upwards and using the derivative block bound
\(\sigma\) gives
\[
                  \|x_v^+\|\le\frac{\sigma}{1-2\sigma}
                                      =\frac1{14}
                  \quad\text{for every }v.
 \tag{31}
\]
For example, if both children satisfy this bound, the parent is
bounded by \(\sigma+2\sigma/14=1/14\); leaves start the induction.
Thus (21) and (29) can be applied at every repair.

There is also an exact termination statement in exact arithmetic.
Give a leaf rank one and a turn the rank of its child. At a product set
\[
 \nu_v=\max\{\nu_L,\nu_R,\min(\nu_L,\nu_R)+1\}.
 \tag{32}
\]
This is the usual Strahler rank, with leaves numbered one.
Starting from any feasible trial field and applying (26) repeatedly,
\[
                         x_v^{(j)}=a_v\qquad(j\ge\nu_v).
 \tag{33}
\]
To prove this, put \(e^{(j)}=a-x^{(j)}\). Subtracting (26) from
(10) gives the exact recurrence
\[
 (I-A(x^{(j)}))e^{(j+1)}=Q(e^{(j)}).
 \tag{34}
\]
Leaves are exact after one repair. At a turn, exactness of the new
child implies exactness of the new parent. At a product, both new
children are exact once \(j+1\ge\max(\nu_L,\nu_R)\); its remaining
quadratic term is zero once \(j\ge\min(\nu_L,\nu_R)\).
These are precisely the conditions in (32). Induction through the
tree proves (33).

If the tree has \(n\) leaves, a vertex of rank \(\nu\) has at least
\(2^{\nu-1}\) descendant leaves: an increase of rank requires two
children of the same preceding rank. Therefore
\[
              \nu_{v_0}\le1+\lfloor\log_2n\rfloor.
 \tag{35}
\]
After this many repairs the whole actual normalized field, and hence
its original closing, is exact. The proof needs the bilinear tree
structure; a network with shared descendants or contraction loops
is outside this assertion.

This finite repair theorem does not solve the asymptotic problem.
It is an alternative exact evaluation and error-reduction mechanism.
An asymptotic use of (22) still requires control of its coherent
corrected closing, or of the successive corrected closings, at the
hyperbolic volume rate.

## 8. Relation to earlier residual estimates

The existing
[stationary-observable estimate](research_stationary_observable_residual_cancellation.md)
subtracts stationary equations from a scalar observable to cancel
its uncertain first derivatives, retaining a quadratic Taylor remainder.
The
[pointed transport estimate](actual_pointed_metric_transport_and_crossing_obstruction.md),
Section 4, gives an exact adjoint-defect identity for a linear cocycle.
Those are relevant precedents within these notes. No novelty is claimed
for adjoint-weighted residual estimation as a general technique.

Here the backward row is constructed from the actual complete Conway
tree, its nonlinear remainder is exactly the finite bilinear expression
(11), and both the local radius and the finite repair/pruning statements
are proved explicitly. No new knot volume identity or finite-exception
class is concluded without the quantitative conditions (23)--(24).

## Complete proof and coverage sources

The following complete matching texts were read. The normalized source
note supplies the actual physical compiler and its norm convention.
The other two are coverage sources; none of their analytic estimates is
an assumption in the identities proved above.

| Source | SHA-256 |
|---|---|
| [Normalized actual source](research_convex_normalized_conway_source.md) | 6b89b4c6a67ef7a32cc41a5966c650f32de65d284ae7b70d94a71bddba21df3c |
| [Stationary observable and residual cancellation](research_stationary_observable_residual_cancellation.md) | 85c3c5410cb1279ff8142f7678c65a6fdb4e6860323f8e810c27d68ae3ea2448 |
| [Pointed transport and adjoint defects](actual_pointed_metric_transport_and_crossing_obstruction.md) | 46a0109371f7e39438232e059a8de9708734a68439b5b610b78ce78fd1faf392 |

Only written mathematics and text/hash operations were used. No
mathematical program, test, numerical iteration, build, git operation,
previous-final edit, or public-document change was performed.
