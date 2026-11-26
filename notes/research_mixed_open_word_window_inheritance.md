# Interior reference domains and the remaining open-word boundary contour

Research deduction, 5 November 2026. The completed open-word critical
localization implies the old refined cyclic reference domains a fixed
distance from either ordinary endpoint. This is an exact identification
with the already certified finite-window roots, not an approximation by
a long periodic word. No new numerical cover or finite-source dominance
is asserted.

## 1. Which vertices satisfy the ordinary window equations

Fix a word \(3+\epsilon_1,\ldots,3+\epsilon_m\). Use its original
open critical point from the
[all-word localization theorem](research_mixed_open_word_critical_localization.md),
with legs \(s_j,t_j\). For \(m\ge2\), \(s_1,t_m\) are private
endpoint legs. The attached legs \(t_1,s_m\), and both legs of every
vertex \(2,\ldots,m-1\), lie in the original typed disks
\[
 D_3=\{|z-(.35-.01i)|\le.09\},\qquad
 D_4=\{|z-(.30-.052i)|\le.064\}.                         \tag{1}
\]
Only vertices \(2,\ldots,m-1\) have both ordinary cyclic gradient
equations. A private endpoint is never silently included among them.

Let \(2\le p\le q\le m-1\). The restriction to vertices
\([p,q]\) solves exactly the ordinary open-window equations with
external legs
\[
                         a=t_{p-1},\qquad b=s_{q+1}.       \tag{2}
\]
Both external legs belong to (1), even if \(p=2\) or \(q=m-1\).
The [universal open-window lemma](research_mixed_cyclic_critical_height_bounds.md),
Lemma 2, gives a unique original zero-lift root in the common convex
chamber for those external values. Hence this root is the restriction
of the open critical point. Its whole holomorphic dependence and every
certified image inequality apply without changing the reference.

This argument does not repeat the open word. Repetition would change
its boundary equations. If an index interval below is empty, its
assertion is simply vacuous. In particular no interior-window
conclusion is asserted for one- or two-vertex open words.

## 2. Exact inheritance ranges

Write
\[
\begin{split}
 R_3&=(.30,.39)+i(-.03,.02),\\
 R_4^0&=(.27,.33)+i(-.057,-.001),\\
 R_4&=(.27,.33)+i(-.057,-.02).
\end{split}                                               \tag{3}
\]
Here and below a statement about both legs uses the type of their
own vertex.

**Theorem 1.** The following ranges hold at every original open
critical point.

| Inherited statement | Vertex range | Window and external input |
|---|---|---|
| Both type-three legs lie in \(R_3\) | \(3\le j\le m-2\) | Three ordinary vertices, external typed disks |
| Both type-four legs lie in \(R_4^0\) | \(4\le j\le m-3\) | Five ordinary vertices, external typed disks |
| Both legs lie in their final \(R_3,R_4\) | \(5\le j\le m-4\) | One ordinary type-four block, external coarse rectangles |
| The conditioned three-type table bounds for \(t_{j-1},t_j\) | \(7\le j\le m-6\) | Three ordinary vertices, external final rectangles |
| \(-1/5<\Re P_{j,a},\Re P_{j,b}<1/4\) for the conditional block at vertex \(j\) | \(7\le j\le m-6\) | The same three-vertex reference window |
| If \(\epsilon_j=\epsilon_{j+1}=1\), then \(-.056<\Im t_j<-.048\) | \(8\le j\le m-7\) | Five ordinary vertices, external final rectangles |
| If \(\epsilon_{j-1}=\epsilon_j=\epsilon_{j+1}=1\), then \(\Im t_j<-.053\) | \(8\le j\le m-7\) | The three-four subset of that five-window cover |

The final two rows concern the **right leg of vertex \(j\)**. The
first of them bounds the first right leg in the ordered pair \(44\);
it does not bound the following leg by reflection. In the last row,
combining the two results gives \(-.056<\Im t_j<-.053\).

*Proof.* A three-vertex window centered at \(j\) is ordinary when
\(j-1\ge2\) and \(j+1\le m-1\). Its external legs are
\(t_{j-2},s_{j+2}\), which lie in their typed disks. Apply the
[type-three window theorem](research_mixed_type_three_window_strip.md).
Similarly a five-vertex window centered at \(j\) is ordinary for
\(4\le j\le m-3\), and the
[five-window theorem](research_mixed_cyclic_critical_height_bounds.md),
Theorem 3, gives the second row. Therefore both types have their
coarse rectangles throughout \(4\le j\le m-3\).

For \(5\le j\le m-4\), the two external legs of the one-vertex
block are \(t_{j-1},s_{j+1}\) in those coarse rectangles. The
[type-four refinement](research_mixed_type_four_height_refinement.md),
Proposition 1, gives the stronger upper height \(-.02\).
Type-three bounds already hold on this range. This proves the third
row without assuming the final rectangles at the endpoints of the
open word.

The [conditioned table](research_mixed_neighbor_conditioned_critical_boxes.md)
and [supporting-slope bounds](research_mixed_geometric_support_slopes.md)
use three-vertex windows with external legs in the final rectangles.
Those external vertices are \(j-2,j+2\). They both lie in
\([5,m-4]\) precisely on the stated common range
\([7,m-6]\). The table bounds \(t_{j-1},t_j\) in the original
orientation, and its stated intersections with the actual final
rectangles are legitimate here too.

For the last two rows use the five-vertex word
\((\epsilon_{j-2},\epsilon_{j-1},1,1,\epsilon_{j+2})\).
Its external legs are at vertices \(j-3,j+3\), so both belong
to the final rectangles when \(8\le j\le m-7\). The
[four-before-four upper bound](research_mixed_four_before_four_height.md),
its [lower-bound extraction](research_mixed_four_before_four_height_lower.md),
and the [three-consecutive-four extraction](research_mixed_three_consecutive_four_height.md)
all use this same original root branch. The checked output is
coordinate 5, namely \(t_2\), in the zero-based ordering
\((s_0,t_0,\ldots,s_4,t_4)\). Thus it is \(t_j\), with exactly
the claimed orientation. Uniqueness in Section 1 identifies every
restricted open root with the certified branch. \(\square\)

**Corollary 2 (all fixed window certificates).** Any ordinary window
\([p,q]\) with
\[
                         6\le p\le q\le m-5               \tag{4}
\]
has its two external legs in the final rectangles. Consequently every
previously proved estimate for its original window root on those
independent external rectangles applies, retaining all correlations.
This includes a five- or six-vertex support certificate whenever that
whole window satisfies (4). It is unnecessary, and generally invalid,
to replace the open reference by a periodic reference of the same
type word.

The assertion concerns the hypotheses of each imported certificate.
Its target-domain, source, selection, and debit hypotheses remain
unchanged. In particular a geometric image inequality alone does not
prove a conditional finite packet on a new target domain.

## 3. The two boundary tangents do not disappear

Put \(r_j=t_j\). For an ordinary conditional block at vertex \(j\),
write
\[
\begin{split}
 \phi_j(a,b)&=\phi_{\epsilon_{j-1},\epsilon_j}(a,b),\\
 P_{j,a}&=\partial_a\phi_j(r_{j-1},r_j),\qquad
 P_{j,b}=\partial_b\phi_j(r_{j-1},r_j),\\
 \Gamma_j(a,b)&=\phi_j(r_{j-1},r_j)
                 +P_{j,a}(a-r_{j-1})+P_{j,b}(b-r_j).
\end{split}                                               \tag{5}
\]
The phase, conditional root, chirp, and factorial half-weights are
exactly those of the
[geometric-slope theorem](research_mixed_geometric_support_slopes.md),
equations (3)--(4). On an internal adjacent pair the original open
critical equation gives
\[
                         P_{j,b}+P_{j+1,a}=0.             \tag{6}
\]
Indeed the left side is the original equation at \(t_j\), after
the two neighboring conditional \(s\)-equations have been imposed.
There is no endpoint action in that internal derivative.

For any consecutive ordinary conditional blocks \(p,\ldots,q\)
for which these phases are defined, (6) yields the exact complex
identity
\[
\begin{split}
 \sum_{j=p}^q\Gamma_j(z_{j-1},z_j)
 ={}&\sum_{j=p}^q\phi_j(r_{j-1},r_j)\\
 &+P_{p,a}(z_{p-1}-r_{p-1})
   +P_{q,b}(z_q-r_q).
\end{split}                                               \tag{7}
\]
Unlike a cyclic sum, (7) retains two boundary terms. Define the
allocated defect on a target branch by
\[
 w_j=\Re(\phi_j-\Gamma_j)
       +\frac{\sigma_{j-1}}2\chi(z_{j-1})
       +\frac{\sigma_j}2\chi(z_j),\qquad
 \chi(z)=\max\{\Re g(z),-2\pi\Im z\}.                       \tag{8}
\]
Then summing (8) and (7) is the exact interior rate accounting,
including the endpoint half-corrections. All complex tangents in (7)
must be retained when comparing an endpoint source to this interior.
Neither a complete-color endpoint value nor an unspecified constant
boundary penalty supplies that comparison.

The old cyclic subaction construction starts from the pointwise
inequality for a *periodic critical reference*. Theorem 1 does not
make the present reference periodic, so it does not by itself
authorize that construction with \(r_j=t_j\) of an open word.
Local source inequalities and local transport inequalities whose
entire reference windows satisfy (4) do transfer. A global
edge-deleted-chain estimate still needs its own boundary accounting.

## 4. The exact source left at the cuts

The [open torus identity](research_mixed_conditional_torus_composition.md),
Theorem 2 and Corollary 3, is the starting finite source. In each
selection term its integrand, apart from its unchanged scalar, is
\[
 \mathcal U_{\epsilon_1,N}(w_L,X_1)
 \prod_{j=2}^m C_{\epsilon_j,N}(X_{j-1},X_j)
 \mathcal H_N(w_R,X_m^{-1})\prod_{j=1}^m D_j,
 \quad
 D_j=d_N(X_j)^{\epsilon_j}X_j^{-N\sigma_j}.
                                                               \tag{9}
\]
Here \(0\le\sigma_j\le\epsilon_j\), with integral selections.
Every allowed term is retained. The original scalar is
\(\kappa_N^{m+\sum\epsilon_j}N^{m+\sum\epsilon_j}\);
ordinary derivatives use the exact signed endpoint-jet factors in
that theorem.

For \(2\le p\le q\le m\), the following is an exact identity of
nonnegative moduli, not a choice of analytic square roots:
\[
 |(9)|=\mathcal L_N
       \prod_{j=p}^q
       \left(|C_{\epsilon_j,N}(X_{j-1},X_j)|
                       |D_{j-1}|^{1/2}|D_j|^{1/2}\right)
       \mathcal R_N,                                      \tag{10}
\]
where
\[
\begin{split}
 \mathcal L_N={}&|\mathcal U_{\epsilon_1,N}|
       \prod_{j=2}^{p-1}|C_{\epsilon_j,N}|
       \prod_{j=1}^{p-2}|D_j|\;|D_{p-1}|^{1/2},\\
 \mathcal R_N={}&|\mathcal H_N|
       \prod_{j=q+1}^{m}|C_{\epsilon_j,N}|
       |D_q|^{1/2}\prod_{j=q+1}^{m}|D_j|.
\end{split}                                               \tag{11}
\]
Empty products have value one. Every original factorial weight and
selected frequency appears exactly once, including at the cuts.
No division by a vanishing endpoint or kernel is made.

For example, when \(m\ge17\), taking \(p=9,q=m-8\) leaves
eight original vertices in each boundary factor and a middle chain.
The two reference cut legs are in the final rectangles, as are the
external legs of all ordinary reference windows contained in
\([6,m-5]\). For \(m\le16\), this particular middle chain is
empty; one retains the complete finite boundary block instead.
This is a finite-width algebraic separation, not a proof of the
absolute norm or gap for either boundary factor.

There are two concrete source obligations:

1. Obtain the original left cap packet and full complementary-current
   estimate on the actual attached image, with both true Fourier
   alternatives. The completed
   [type-three first-cap packet](research_mixed_three_first_cap_packet.md)
   and [exact Fourier replacement](research_mixed_three_first_cap_fourier_reduction.md)
   already give important inputs, but their stated complex neighborhood
   is not a proved enclosure of the whole attached disk (1). The type-four
   first-cap polynomial is the literal \(\mathcal U_{1,N}\) in (9).
2. At the other endpoint, the proved
   [full-\(E\) ordinary coefficient packet](research_mixed_endpoint_packet_extension_criterion.md)
   controls the canonical complete-end coefficient on the private-leg
   image. The exact finite identity from
   [the complex-index coefficient proof](research_complete_boundary_complex_index.md),
   equation (18), is
   \(\mathcal H_N(w,e^{2\pi i e})=G_N(Ne)\mathcal C_N(e,w)\).
   It supplies the factorial normalization of the polynomial in (9),
   rather than a mere identification of its physical samples.
   It does not extend the adjacent conditional kernel to that
   private image automatically. In (9) the final kernel has arguments
   \(t_{m-1},t_m\), and \(t_m\) is private. A right-oriented cap,
   or a complete source theorem for that terminal kernel and its
   endpoint coefficient together, is still required.

These are order-\(N\) endpoint phases. They cannot be treated as fixed
holomorphic insertions in the cyclic Gaussian theorem. A boundary
contour proof must bound (11) against the two terms of (7), and bound
all discarded original boundary rows and currents absolutely. For the
whole ordinary boundary polynomial, the sufficient strip criterion in
Section 5 of the full-\(E\) packet note additionally requires the
weighted absolute retained-contour norm and the discarded gap for
both entire real ordinary boundary angles. The complete-color scalar
alone does not imply either bound.

Thus the reference-domain obstacle has a fixed finite boundary width;
the endpoint contour and its quantitative boundary comparison remain
separate. No open-word nonzero coefficient, arbitrary short-filling
stability, or enlarged knot family follows from this deduction alone.
