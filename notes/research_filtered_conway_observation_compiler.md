# Exact Conway packets with a finite observation budget

21 November 2026. Research note. Earlier final proofs and public papers
remain unchanged.

A full boundary representation can be irreducible at every fixed quantum
level while admitting smaller exact packets for observations of bounded
diagram complexity. The packets below preserve the original marked
closures and compose through both products and turns. Their sizes and
their allowed observations have different, explicitly recorded budgets.

The construction is algebraic compression, not a geometric lower
certificate. Computing its reachable packets or observation matrix can
already require the target open packet or its closed invariant.

## 1. Actual packets and a finite grammar

Fix \(N\ge2\). Let \(H_N\) be the full \(N\)-dimensional Newton
boundary algebra
\[
 H_N=\mathbb C[z]/(2T_N(z/2)+2).
\]
Here \(T_N\) is the Chebyshev polynomial of the first kind.
It has its Newton coefficient Hermitian inner product, actual product
\(M(f,g)=fg\), actual turn \(J\), and original signed crossing
packets \(R^+,R^-\). The two original rows are
\(\lambda_0=e_0^{\mathsf T}\) and
\(\lambda_d=e_d^{\mathsf T}\), where \(d=N-1\).
All physical first-normal directions are present in this initial
algebra. The complete source conventions are those of the
[full Conway compiler](research_conway_full_boundary_quotient_gram.md).

Use the finite syntax
\[
 t=1,\ R^+,\ R^-,\ Jt,\ \text{or }M(t_1,t_2).
                                                        \tag{1}
\]
Each leaf and each operation costs one. Write \(|t|\) for this
integer cost, and \([t]_N\in H_N\) for its exact packet.
The Cartan scalars in \(R^\pm\), and any recorded external framing
or closing factors, are not removed. A fixed integral power is a
finite term in (1), rather than a new letter from an infinite alphabet.
For example, \(n\) signed single crossings have cost \(2|n|-1\)
when \(n\ne0\); the zero power is the unit leaf.

A context \(C[\ ]\) is such a term with exactly one leaf replaced
by a hole. Its cost counts all vertices except the hole. Follow it
by either original row \(\lambda_0\) or \(\lambda_d\).
The resulting row on the hole is denoted \(\rho_C:H_N\to\mathbb C\).
Thus the two bare closing rows are contexts of cost zero. Because
the hole occurs once and \(M\) is bilinear, every \(\rho_C\) is
linear. Constants elsewhere in the context are their full actual
packets. All such well-defined cap completions are included, also
when their diagrams close to links. Restricting this set to knot
closures could invalidate closure under sibling substitution.

For integers \(l,m\ge0\), define
\[
 \begin{split}
 \mathcal R_l&=\operatorname{span}\{[t]_N:|t|\le l\},\\
 \mathcal C_m&=\{C:\ |C|\le m\},\\
 \mathcal Z_{l,m}&=\{x\in\mathcal R_l:
                   \rho_Cx=0\text{ for all }C\in\mathcal C_m\}.
 \end{split}                                             \tag{2}
\]
In particular \(\mathcal R_0=\{0\}\).
These are spaces of reachable packets and of reachable packets
invisible to the specified observations. They are not quotients by
all physical exterior operations.

## 2. A positive Gram and representatives inside the reachable space

Choose any orthonormal column matrix \(U_l\) with range
\(\mathcal R_l\). Let \(O_m\) stack the original rows \(\rho_C\)
for \(C\in\mathcal C_m\), and put
\[
 A_{l,m}=O_mU_l,\qquad
 Q_{l,m}=U_l A_{l,m}^*(A_{l,m}A_{l,m}^*)^\dagger
                              A_{l,m}U_l^*.             \tag{3}
\]
The dagger denotes the Moore--Penrose inverse; it is zero on the
zero eigenspace of the displayed positive semidefinite Gram.
This formula needs no invertibility or fixed-rank assumption.

The matrix \(A^*(AA^*)^\dagger A\) is the orthogonal projection
onto \(\operatorname{ran}A^*\): this follows by diagonalizing
\(AA^*\), or directly by applying the formula on
\(\ker A\) and its orthogonal complement. Consequently \(Q_{l,m}\)
is the orthogonal projection onto
\[
 \mathcal S_{l,m}=\mathcal R_l\ominus\mathcal Z_{l,m}.
                                                        \tag{4}
\]
For every \(x\in\mathcal R_l\),
\[
 Q_{l,m}x\in\mathcal R_l,\qquad
 x-Q_{l,m}x\in\mathcal Z_{l,m},\qquad
 O_mQ_{l,m}x=O_mx.                                      \tag{5}
\]
In particular its operator norm is at most one. Different
orthonormal choices of \(U_l\) give the same projection.

The condition that the representative stays inside \(\mathcal R_l\)
is essential. Projecting onto the Riesz rows of \(O_m\) in the whole
of \(H_N\) need not have this property.

## 3. Product descent and the total-budget rule

**Product lemma.** Suppose \(x\in\mathcal R_l\),
\(y\in\mathcal R_k\), and \(m\ge0\). Then
\[
 \begin{split}
 xy-
 \bigl(Q_{l,m+k+1}x\bigr)
 \bigl(Q_{k,m+l+1}y\bigr)
       \in\mathcal Z_{l+k+1,m}.                         \tag{6}
 \end{split}
\]

**Proof.** All products in (6) belong to \(\mathcal R_{l+k+1}\).
For a context of cost at most \(m\), inserting a fixed term of
cost at most \(k\) into the other product input produces a context
of cost at most \(m+k+1\). Linearity gives the same assertion for
any \(y\in\mathcal R_k\). Therefore replacing \(x\) by
\(Q_{l,m+k+1}x\) changes none of the required observations.
This representative is still in \(\mathcal R_l\), by (5).
It can therefore be used as the fixed first input when replacing
\(y\), at context cost at most \(m+l+1\).
Both replacements are safe, proving (6). \(\square\)

Similarly,
\[
 J\mathcal Z_{l,m+1}\subseteq\mathcal Z_{l+1,m}.          \tag{7}
\]
Indeed a turn at the hole adds one context vertex. Multiplication
by a fixed signed crossing packet has the same statement with a
cost increase of two, according to (1).

Fix a total syntax budget \(B\). At reachable size \(l\le B\)
use the quotient and its orthogonal representative space
\[
 V_l^B=\mathcal R_l/\mathcal Z_{l,B-l}
                   \simeq\mathcal S_{l,B-l}.            \tag{8}
\]
The product lemma and (7) give well-defined maps
\[
 V_l^B\otimes V_k^B\longrightarrow V_{l+k+1}^B,\qquad
 V_l^B\longrightarrow V_{l+1}^B,                         \tag{9}
\]
whenever the displayed sizes do not exceed \(B\).
For the first map, the required child observation budget is
\((B-l-k-1)+(k+1)=B-l\), exactly the budget in (8).
The corresponding equality holds for the other child.

Choose isometric inclusions
\(I_l:\mathbb C^{r_l^B}\to H_N\) with range
\(\mathcal S_{l,B-l}\). The actual compressed gates are
\[
 \widehat M_{l,k}=I_{l+k+1}^*M(I_l\otimes I_k),\qquad
 \widehat J_l=I_{l+1}^*JI_l.                            \tag{10}
\]
A leaf packet is replaced by its orthogonal representative.
More generally, a precomputed fixed subtree of cost \(l\) is
inserted as \(I_l^*[t]_N\); its earlier local normalization need
not be changed merely to assign its syntax cost. This is virtual
syntax bookkeeping: an atomic filled leaf \(R^n\) can retain
its original tensor and original budget while being assigned the
cost of its finite realization in (1). It is not physically
expanded and then assigned a falsely unchanged budget.

**Exact source theorem.** For every actual term \(t\) with
\(|t|=l\le B\), the recursion (10) computes the coordinates of
\(Q_{l,B-l}[t]_N\). Both original closing rows give exactly
their values on \([t]_N\).

**Proof.** Induct on the term. Equations (6)--(9) show that
replacing either child by its representative changes the parent
only by its prescribed invisible subspace. Taking the parent
representative therefore gives the stated recursion.
At the root, either original closing row is a context of cost
zero, which is allowed since \(B-l\ge0\). Equation (5) proves
the source equality. Recorded external scalar factors multiply
this equality unchanged. \(\square\)

The open packet is preserved only modulo the allowed observation
kernel. It need not agree in an exterior whose complexity exceeds
the remaining budget. In particular, no fixed invariant quotient
of the full physical algebra is asserted.
The graded turn in (10) need not be unitary or invertible: its
domain and codomain have different budgets. The original cap
rows are restricted literally, never replaced by a Hermitian norm.

## 4. Size bounds and the order of quantifiers

Preorder syntax encodes a term as a word on five letters.
A context has one additional hole letter and two possible closing
rows. A generous common bound is
\[
 \#\{t:|t|\le n\},\ \#\mathcal C_n\le16^{n+2}.
\]
It follows from (2)--(4) that
\[
 r_l^B\le
 \min\bigl(N,\ 16^{l+2},\ 16^{B-l+2}\bigr).             \tag{11}
\]
There is no assumption that the restricted invisible subspace
\(\mathcal Z_{l,m}\) is nonzero.
For fixed \(l\), the finite reachable space already has an
\(N\)-independent dimension bound before taking this quotient.
The size count by itself is therefore not a new analytic gain.

For instance, take
\[
 B_N=\left\lfloor\frac{\log N}{3\log16}\right\rfloor.
\]
Then \(B_N\to\infty\), and even the sum of the generous dimension
bounds over all \(B_N+1\) size layers is \(o(N)\).
Every fixed completed Conway term is represented exactly for all
sufficiently large \(N\), because its finite syntax size eventually
lies below \(B_N\).

A fixed filling coefficient is fixed before \(N\to\infty\);
its number of single crossings may be arbitrarily large but is
finite. No uniform statement over coefficients growing with \(N\)
follows. At a fixed \(N\), increasing the observation budget can
eventually recover the full physical representation. These facts
are consistent with fixed-level irreducibility and source tomography.

## 5. Only quotient residuals are charged, with the original budgets

Apply the construction to a fixed literal compiler of total syntax
size at most \(B\). A precomputed fixed leaf receives the cost of
its finite realization in (1). Keep every positive local budget
from the [normalized source construction](research_convex_normalized_conway_source.md):
\[
 b_v=16\max(1,\|T_v\|_{\rm HS}),\qquad
 B_{\rm tot}=\prod_vb_v,\qquad \sigma=1/16.
\]
The normalization tree and these numbers are not recomputed after
projection. All compressed proper maps and constants still have
Hilbert--Schmidt norm at most \(\sigma\), as does the normalized
closing row: isometric inclusion and orthogonal output projection
cannot increase Hilbert--Schmidt norm.

The proper spaces may have different dimensions, including zero.
Let \(\widehat\Phi_v\) be the compressed normalized gates and
\(\widehat L\) the normalized original closing row. The true
compressed forward field \(a\) satisfies
\[
 a_v=\widehat\Phi_v((a_c)_c),\quad \|a_v\|\le\sigma,
 \qquad k=K_N/B_{\rm tot}=\widehat L a_{\rm top}.
                                                        \tag{12}
\]
The exact source theorem proves the last equality.
For arbitrary trial packets \(\|x_v\|\le1\), define
\[
 G_v(x)=\widehat\Phi_v((x_c)_c)-x_v,\quad
 z(x)=\widehat Lx_{\rm top},\quad
 E(x)=|z(x)|^2+\sum_v\|G_v(x)\|^2.                       \tag{13}
\]
These are quotient residuals. No full physical norm of an
invisible discarded component is added to (13).

Here is a dimension-free source comparison, included to make the
effect of the changed spaces explicit. At the midpoint of \(x\)
and \(a\), let \(A\) be the block derivative of the proper forward
maps. Exact midpoint differentiation of linear and bilinear maps
gives
\[
 G(x)=(-I+A)(x-a),\qquad \|A\|\le\sqrt2\,\sigma\le1/8.
\]
The norm bound holds because a parent has at most two children
and each child occurs in one parent. Thus
\[
 |k-z(x)|\le\frac1{14}\|G(x)\|,\qquad
 |k|^2\le\frac{197}{196}\,E(x).                         \tag{14}
\]
The true forward field is feasible and has \(E(a)=|k|^2\).
The trial domain is a finite product of compact unit balls.
Consequently
\[
 B_{\rm tot}^2\min E\le |K_N|^2
       \le\frac{197}{196}B_{\rm tot}^2\min E.           \tag{15}
\]
This includes zeros and all level parities. The objective remains
quartic. In particular the original source comparison can be
applied on the graded observable packets without paying for the
norm of their invisible reachable complements. No geometric trial
field or lower rate is furnished by this fact.

## 6. What the compression does not supply

The raw pairing matrix
\[
 \mathsf H_{m,l}(C,t)=\rho_C[t]_N,\qquad
                  |C|\le m,\quad |t|\le l              \tag{16}
\]
is a finite tree-context version of a Hankel matrix. When
\(m+l\le B\), its entries are original closed periods of that
total complexity. One of them can already be the target \(K_N\).
Likewise the reachable synthesis used to form \(U_l\) can contain
the target open packet. No value of \(K_N\) is assumed or used
as a divisor, but constructing these matrices can require
contractions just as hard as the original problem.
At a root of size exactly \(B\), only the two bare cap tests remain,
so its representative has dimension at most two; its selected
coordinate still contains the original closed period.

Small rank therefore does not supply cheap computation,
subexponential Gram conditioning, independently known geometric
coefficients, a bounded algebraic degree, or a nonzero closing
coefficient. The packets are not identified with geometric sectors.
They can discard actual Jordan directions only when those
directions are invisible to all observations within the budget.

The [two-sided source-quotient theorem](actual_source_two_sided_quotients.md)
concerns a quotient compatible with an unrestricted relative
operator algebra. The present family instead changes with both
reachable and remaining-context size. It neither contradicts that
theorem nor infers a volume lower bound from finite-level kernels.
Its gain is the exact bilinear composition rule (6), which a
whole-space observation projection alone does not provide.

## Complete proof sources and coverage

All three complete matching texts were read. The first supplies the
contextual meaning and scope of a source quotient; the second fixes
the full physical operations and original closures; the third fixes
the retained local normalization. The filtered construction and its
source comparison are proved above.

| Complete proof source | SHA-256 |
|---|---|
| [Two-sided source quotients](actual_source_two_sided_quotients.md), Sections 1--5 | 7ec8b1482c6c312c3f103d148322219b31d318a79f6bf87dd5609071d0d184c0 |
| [Full Conway boundary compiler](research_conway_full_boundary_quotient_gram.md) | debe56dbad8151b90d44d0fccbf0dcf33dafb780370e01c8acdadbd2939dc077 |
| [Normalized complete source](research_convex_normalized_conway_source.md) | 6b89b4c6a67ef7a32cc41a5966c650f32de65d284ae7b70d94a71bddba21df3c |

For coverage, the complete
[twist tomography note](research_original_twist_observation_tomography.md)
(6885ad1b82b8f67ddda497f969337a9230b17925fd88b4326b0152dfdc738a1c),
[observation-composition criterion](research_source_adapted_observation_composition.md)
(e4a1781624d76edad35f6cc6ff3639e22b315f8314b049edaea25bc8623c0d27),
and [commutant/window repair](research_source_preserving_commutant_projection_and_window_repair.md)
(ff75410cfbba220c17bfd8153f27f901f21f1d98077b186945ebe502f24032e2)
were read. They do not state the graded reachable-context compiler
with the bilinear budget rule (6)--(9). No generic novelty claim is
made for finite-dimensional reachable/observable compression.

The general tree/context Hankel viewpoint is established in
Kiefer, Marušić and Worrell,
[Minimisation of Multiplicity Tree Automata](https://arxiv.org/html/1410.5352v4),
Sections 2.4--3.1. The finite-tree and one-hole-context definitions,
Hankel pairing, and forward/backward spaces were checked there
for coverage. No theorem or estimate from that paper is required
by the direct proofs above.

Only written mathematics and text/hash operations were used.
No mathematical program, numerical experiment, test, build, git
operation, or earlier-final edit was performed.
