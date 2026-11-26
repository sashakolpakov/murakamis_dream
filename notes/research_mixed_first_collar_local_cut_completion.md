# A full first collar with small cut triples and an unrestricted middle

Private research deduction, 10 November 2026. A fixed loss already proved
for the complete first-collar prefix pays the actual completed boundary
comparison when its cut triple and the opposite boundary are close to
their original references. The middle retains its full alphabet. No
long unselected corridor, pinning construction, or local minimizing
branch is required.

This is an additional nonlocal region of the boundary comparison:
the first coordinate occupies its whole proved seam collar, its first
two permitted selections remain present, and the later left-prefix
targets vary independently over the plateau. It is not a bound for
arbitrary physical boundary targets. In particular an occupation-small
cut does not by itself make the intervening prefix eligible.

## 1. The original source and the specified region

Fix an actual complete-color reference of a finite open word
\(n_j=3+\epsilon_j\), \(1\le j\le m\), with its original
retained coordinates \(r_j=a_j+ic_j\). Use safe ordinary cuts
\(p,\ldots,q\) from
[the open boundary reduction](research_mixed_open_boundary_comparison_reduction.md).
Put
\[
 I=[p-2,q+1],\qquad h=p-1,\qquad
 v_L=(q_{p-2},q_{p-1},q_p),\quad
 v_R=(q_{q-1},q_q,q_{q+1}).
 \tag{1}
\]
Assume the two triples are disjoint and \(h\ge3\). All required
ordinary windows and their safety halos are those of that reduction.
These are restrictions on the actual finite word; short words for
which such cuts do not exist are not included.

Write \(P=[.22,.45]\), \(D_j=d_N(X_j)^{\epsilon_j}
X_j^{-N\sigma_j}\), and \(X_j=e^{-2\pi iz_j}\), on the
original periodic hybrid graph. Keep the literal moduli
\[
\begin{split}
 L_N&=|U_{\epsilon_1,N}|
       \prod_{j=2}^{p-1}|C_{\epsilon_j,N}|
       \prod_{j=1}^{p-2}|D_j|\ |D_{p-1}|^{1/2},\\
 R_N&=|H_N|\prod_{j=q+1}^{m}|C_{\epsilon_j,N}|
       |D_q|^{1/2}\prod_{j=q+1}^{m}|D_j|.
\end{split}
\tag{2}
\]
In particular the right terminal coordinate has not been contracted
into a reversed-cap transform. The original ordinary colors are
\((-2,-2)\).

Impose the following source conditions.

* The first two types are any \((3+\alpha,3+\beta)\).
  The first real coordinate lies in the entire previously chosen
  collar \(0\le x_1\le\rho\). Its allowed first selection is
  retained. The second real coordinate is in
  \(I_3=[.267,.433]\) if \(\beta=0\), or
  \(I_4=[.24,.363]\) if \(\beta=1\).
  Its actual height follows the original first-collar path:
  between \(c_2\) and zero if unselected; if \(\beta=1\),
  the permitted selected path lies between zero and \(7/500\).
  No independent height reset is made.
* The coordinates \(3,\ldots,p-1\) are unselected and range
  independently in \(P\), at their original heights. The triple
  \(v_L\), including coordinate \(p\), is unselected and close
  to its baseline triple.
* The physical right-buffer coordinates \(q,\ldots,m\) are
  unselected and lie in one sufficiently small coherent real
  neighborhood of their actual reference, at their original heights.
  The triple \(v_R\), including coordinate \(q-1\), is also
  unselected and close to its baseline.
* Every other symbol of \(I\) is unrestricted: it may occupy
  the full original real period and carry either type-compatible
  selection. Its original hybrid height, seam label and complete
  source alternatives remain present.

The three protected symbols on each side ensure that the unrestricted
middle does not change the heights used in (2). The original height
stencil has exactly the interaction range retained in the six-edge
closure; in particular the left cut height depends only on its
protected neighbors, and likewise on the right.

For a triple of unselected symbols let \(d_L,d_R\) denote its three
real displacements. Below use
\[
 \delta_0=\frac3{125},\qquad
                   \|d_L\|^2+\|d_R\|^2
                                      \le\frac{\delta_0}{80}.
 \tag{3}
\]
The coherent-neighborhood requirements may further shrink this set.
They do not restrict \(x_1\) or the independent earlier
left-prefix targets to a local neighborhood.

## 2. Exact prefix calibration

The completed
[three-row source assembly](research_mixed_three_row_source_assembly.md),
Section 3, equation (11), supplies for the literal prefix (2)
\[
\begin{split}
 N^{-1}\log L_N
 \le{}&M_L+\Re P_{p-1,b}\,d_{p-1}
       -\delta_{\alpha\beta}+\tau\\
 &-\kappa_*\left(
 d_2^2+2\sum_{j=3}^{p-2}d_j^2+d_{p-1}^2\right)
       +O_m(\log N/N),\\
 &\kappa_*=\frac1{2500000},\\
 &\delta_{00}=\frac3{100},\quad
   \delta_{10}=\frac3{125},\quad
   \delta_{01}=\delta_{11}=\frac4{125}.
\end{split}
\tag{4}
\]
The tolerance \(\tau>0\) is arbitrarily prescribed once for the
whole prefix. Its ordinary-color disk and polynomial factor are fixed
before \(N\). Equation (4) bounds every finite row, physical
endpoint, revived product and alias. For a second type four the
complete second selected weight is included, with the transported
half on edge three counted once.

The exact identification with (2) is equations (15), (19) of
[fixed-reference first-collar completion](research_mixed_first_collar_fixed_reference_completion.md)
for second type three, and equation (25) of
[the type-four enlarged-contour transport](research_mixed_four_enlarged_contour_transport.md)
for second type four. All ordinary row excesses in those earlier
formulas are zero by the completed three-row theorem. Thus (4) is
not an estimate of a restricted cap or of an uncontracted error
subsequently multiplied by an uncontrolled factor.

Define the calibrated prefix rate \(G_L\) before its synthetic
closing term by subtracting \(M_L\) and adding
\(\Re[P_{p,a}(z_{p-1}-r_{p-1})]\). The cut is at its
original height. Original stationarity gives
\(P_{p-1,b}+P_{p,a}=0\), so (4) proves, at the rate level,
\[
                         G_L\le-\delta_{\alpha\beta}
                                      \le-\delta_0.
 \tag{5}
\]
The omitted quadratic terms are favorable. This cancellation uses the
original complex marginals before taking real parts. No marginal
at a moving target or altered reference is used.

At the right buffer use the real phases of its literal coherent local
packets. Section 2, equation (4), of
[the buffered endpoint theorem](research_mixed_buffered_endpoint_sectors.md)
gives, on a sufficiently small fixed neighborhood,
\[
 G_R:=b_R-M_R+\Re[P_{q,b}(z_q-r_q)]\le0.
 \tag{6}
\]
This is the one-ended horizontal negative-Hessian argument for the
complete terminal conditional factor, \(H_N\), its full final
weight and the remaining ordinary factors. It is not an assertion
that the separately closed rate \(\mathcal B_R\) is nonpositive.

## 3. The two closing fees and the full-alphabet completion

Let \(A_p,E_q,D\) be the unchanged six-edge closure in the
open boundary reduction. Set
\[
 \mathcal B_L=G_L-A_p,\qquad
 \mathcal B_R=G_R-E_q .
 \tag{7}
\]
The synthetic closing configurations have all nonbaseline symbols
inside \(I\). On the protected unselected plateau triples,
their closing terms simplify exactly to
\[
\begin{split}
 A_p&=-e_{p-2}(a_{p-3},x_{p-2})
                 -e_{p-1}(x_{p-2},x_{p-1}),\\
 E_q&=-e_{q+1}(x_q,x_{q+1})
                 -e_{q+2}(x_{q+1},a_{q+2}),
\end{split}
\tag{8}
\]
where \(e_j=-\Re(\phi_j-\Gamma_j)\) is the original
ordinary pair energy at the fixed reference heights. The third
nominal closing edge on each side is identically at baseline.
All relevant cutoffs equal one, so no height term remains hidden
in this simplification.

The safe open windows inherit the bound
\(0\preceq e_j''\preceq20I_2\) from
[plateau boundary forgetting](research_mixed_plateau_boundary_forgetting.md),
equation (3), as already used in the actual-open completion.
Since each \(e_j\) and its gradient vanish at its reference pair,
Taylor's integral formula proves
\[
 0\le -A_p\le20\|d_L\|^2,\qquad
 0\le -E_q\le20\|d_R\|^2.
 \tag{9}
\]
The intermediate coordinate of either pair is counted twice; the
constant \(20\) includes precisely these two incidences.

For \(0\le\theta<1\), retain the original reserved cost and its
full-alphabet infimum:
\[
\begin{split}
 D_\theta&=D-\theta\kappa\sum_{i\in I}p_i,\qquad
 \kappa=\frac1{20000},\\
 D_\theta&\ge(1-\theta)\kappa\sum_{i\in I}p_i\ge0,\qquad
 V_\theta(v_L,v_R)=\inf D_\theta .
\end{split}
\tag{10}
\]
This is [actual-open full-alphabet completion](research_mixed_actual_open_full_alphabet_completion.md).
Every allowed middle symbol is included in the infimum.

**Theorem 1.** On the region in Section 1, for every
\(0\le\theta<1\),
\[
 \boxed{\quad
 \mathcal B_L+\mathcal B_R-V_\theta(v_L,v_R)
                                  \le-\frac{3\delta_0}{4}.
 \quad}
 \tag{11}
\]
The same bound holds for every pinned completion
\(V_\theta^{[d]}\), without any approximation error.

*Proof.* Equations (5)--(9) and (3) give
\[
 \mathcal B_L+\mathcal B_R
 \le-\delta_0+20(\|d_L\|^2+\|d_R\|^2)
 \le-\frac{3\delta_0}{4}.
\]
Subtract \(V_\theta\ge0\). A pinned completion restricts the
infimum and is also nonnegative. No assertion about where a minimizing
configuration lies is needed. \(\square\)

More directly, every original middle configuration satisfies
\[
 \mathcal B_L+\mathcal B_R-D
 \le-\frac{3\delta_0}{4}
                    -\theta\kappa\sum_{i\in I}p_i.
 \tag{12}
\]
Choose one aggregate source and color tolerance below
\(\delta_0/8\), and then \(N\) large enough to absorb all
polynomial factors into another \(\delta_0/8\). The exact
whole source on this region consequently has a finite exponential
gap at least
\[
                         \frac{\delta_0}{2}=\frac3{250}
 \tag{13}
\]
below its original \(M_{\rm open}\), retaining the nonnegative
occupation term in (12). This is uniform through both parities.
Small fixed ordinary-color disks and fixed ordinary derivatives
follow from the complete prefix estimates and the literal right
local packet; their total cost is included in the same tolerance.
The middle has no ordinary-color dependence.

The original polynomial scalar, the bounded hybrid Jacobian, finite
selection sum and integration over this fixed-word sector do not
change the exponential conclusion. No finite Fourier factor has
been divided out. This is suppression of a region of the full
uncontracted source, not a nonzero assertion about that region.

## 4. Why occupation does not automatically produce this whole region

The small protected cut in (3) can be *located* from an occupation
bound, but its eligible prefix cannot.

Indeed, suppose \(M\) disjoint six-symbol blocks have total
occupation at most \(B\). One of them has occupation at most
\(B/M\). If \(B/M<1\), every symbol of that block is
unselected plateau and
\[
       \sum_{\text{block}}|x_i-a_i|^2
                                  \le\frac{B}{400M}.
 \tag{14}
\]
Thus choosing \(M\) large enough makes any protected triple in
that block as close to baseline as required, while the six symbols
retain the complete four-symbol interaction stencil. This is the
same averaging step used in full-alphabet finite-depth completion.

However, (4) requires **every** target between positions three and
the cut to be unselected plateau. A bound on total occupation may
still permit one earlier selected, early, seam or raw-right symbol;
its occupation is only one. Such a symbol remains in the literal
prefix when the cut is moved to a later good block. Formula (14)
neither deletes it nor supplies the missing prefix source estimate.
Moreover the occupation used for a synthetic middle says nothing
about physical symbols lying outside that middle.

The preceding
[buffered endpoint theorem](research_mixed_buffered_endpoint_sectors.md)
and its fixed-reference enlargement pay arbitrary cores behind two
long unselected corridors. The present deduction removes those
corridor-length and corridor-state requirements after the protected
triples: a bad symbol may occur immediately beyond either triple.
It replaces them by the explicit small-triple condition (3).
Neither assertion contains the other without its additional
hypotheses.

The first-collar displacement is genuinely nonlocal: \(x_1\)
ranges down to zero, at the actual first seam height, rather than in
the local chart of
[completed boundary local sign](research_mixed_completed_boundary_local_sign.md).
But a remote defect already in the intervening physical prefix,
or an arbitrary noncoherent opposite boundary, is still unpaid.
The general endpoint comparison and the finite-exception objective
are not inferred.

## Source bindings

All direct proof inputs and the two scope comparisons were read at
the following unchanged hashes.

| File | SHA-256 |
|---|---|
| research_mixed_actual_open_full_alphabet_completion.md | d41f2c57b0ee397a24f299f5ffbfb132a1fb78ed1c47423543c56c975da0b782 |
| research_mixed_open_boundary_comparison_reduction.md | 5d3f875a6c1a7e0c2c9840c16674dc8ad5921bf0f2312202cb26f278c86c72ce |
| research_mixed_three_row_source_assembly.md | 947fe40bd6125a0bca0f984dc4dde6d55e478ecf0719911829bdb840ef34396c |
| research_mixed_first_collar_fixed_reference_completion.md | cd44c55c73a305ac6a2aac9c3e05a82b60a512bd3758cea2db79e7d9570ff317 |
| research_mixed_four_enlarged_contour_transport.md | 84b1213895edbb5b10590161cc940118ebb343269cbf6a9af61b9e3cc972db2a |
| research_mixed_buffered_endpoint_sectors.md | 57bd3869f66c188d837da2de109bba6bfd01dc73c16a199e6f8eb26e11b7bb71 |
| research_mixed_plateau_boundary_forgetting.md | 6f3294e9beaaa20c1048dff534cca91d0036150ead2f6609df56a31a22f495c9 |
| research_mixed_full_period_occupation.md | 70cd6262e5737c70ed178cbf88ca69cb6f7d7eb659a493a21673bdd5b2830fec |
| research_mixed_completed_boundary_local_sign.md | b9f99c7a78b7bcf82f749c3045cd71fd9ceae876e9dc45ceddb5476d0446747d |

No mathematical numerical evaluation, source replay, test, import,
compilation, or edit to a frozen manuscript was used.
