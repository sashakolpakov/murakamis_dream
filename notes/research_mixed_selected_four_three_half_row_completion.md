# Complete half-row bounds and one remaining joint comparison

Research theorem, 6 November 2026.

The two independent ordinary half-row profiles for the selected
first-four/next-three product are now strictly below their original
calibrated action. The proof uses a complete scalar cover with the
same actual reference correlations and original primitive branches.
It implies a bound for the whole cap multiplied by every literal
ordinary row from the half index onward. The full finite product
still has one independent comparison: the left cap cut paired with
the ordinary main contour.

## 1. Completed scalar comparisons

Keep the actual first-four/next-three reference of word length
\(m\ge3\), \(H=7/625\), \(z=y+iH\), \(b=v+ih_b\),
and \(y,v\in P=[.22,.45]\). All other heights remain their
original reference values. Use the phases and rates
\(\Psi,Q,A_i,B_j,M,\ell_b,W_\nu\) of
[the exact finite reduction](research_mixed_selected_four_three_finite_reduction.md).
In particular
\[
 W_1(y)=-\Re g(y+iH)-2\pi H,\qquad W_0(y)=0,
 \qquad \ell_b(v)=\Re p\,(v-\Re b_*).
 \tag{1}
\]
The two rates in (1) bound the same complete selected Fourier
factor, and \(p\) is the unchanged original outgoing marginal.

**Theorem 1.** Uniformly over these actual references and \(P^2\),
\[
 \begin{split}
 A_0(y)+B_R(y,v)+W_\nu(y)&<M+\ell_b(v)-1/2000,\\
 A_L(y)+B_R(y,v)+W_\nu(y)&<M+\ell_b(v)-1/2000,
 \end{split}
 \qquad \nu=0,1.
 \tag{2}
\]
The same gap therefore holds with any of the five cap profiles
\(A_0,A_L,A_R,A_-,A_+\) in place of \(A_0\).

The [half-row upper-bound theorem](research_mixed_selected_four_three_half_row_majorant.md)
maximizes the outgoing coordinate exactly with its original tangent
and bounds the remaining targets by clipped quadratic gains.
The [evaluation specification](research_mixed_selected_half_row_evaluation_design.md)
strengthens the main private curvature to \(28/5\). Consequently
it suffices to bound the four reference-only quantities
\[
 \mathcal H^+_{0,1},\quad\mathcal H^+_{0,0},\quad
 \mathcal H_{.27,1},\quad\mathcal H_{.27,0}
                         \quad\hbox{strictly below }-1/2000.
 \tag{3}
\]
The complete scalar certificate described below proves (3).
The [right-cut comparison](research_mixed_selected_cap_right_rows.md)
and [alias comparison](research_mixed_selected_cap_alias_transport.md)
give \(A_R<A_0-1/1250\), \(A_-<A_0-1/4\), and
\(A_+<A_0-1/50\). These prove the last assertion of Theorem 1.
They do not require the redundant right-cut scalar majorants to
have a negative sign.

## 2. Exact coverage and the two primitive providers

The scalar domain and all necessary filters are those of the
[proved first-four/next-three central comparison](research_mixed_first_four_next_three_central_gap.md):
\[
 u\in[.217,.234]+i[.027,.045],\qquad U=e^{2\pi iu},
 \tag{4}
\]
with the original rational \(E(U),Z(U),S(U),B(U)\) maps,
typed coordinate rectangles, reduced disks, coupled pair sums,
and next-external \(K_3\cup K_4\) condition. Every actual open
reference is covered, including the attached next external leg at
length three. No claim that every retained auxiliary point is an
actual word reference is used.

The [new scalar certificate proof](research_mixed_selected_half_row_scalar_certificate.md)
and [driver](../experiments/certify_mixed_selected_half_row_budget.py)
evaluate the original branch
\[
 g(w)=\frac{\operatorname{Li}_2(e^{-2\pi iw})-\pi^2/6}{2\pi i},
 \qquad 0<\Re w<1.
 \tag{5}
\]
The actual private action uses the same auxiliary \(u\) directly.
Only the fixed real cut uses its canonical explicit square-root
and arctangent expression. No root solve, moving target root,
quantum source sum or old source-certificate replay is involved.
Every free real target is already covered by the proved upper
bounds; there is no target grid.

Two valid outward arithmetic forms of (5) occur in the final
record. The first is direct ball evaluation. The second is the
[centered primitive enclosure](research_mixed_centered_primitive_enclosure.md)
\[
 g(W)\subseteq g(w_0)+g'(W)(W-w_0),\qquad
            g'(w)=\Log(1-e^{-2\pi iw}),
 \tag{6}
\]
on a convex regular rectangle \(W\) with exact dyadic center
\(w_0\). The integral identity proves (6) on every such rectangle;
the one-box diagnostic is not substituted for that analytic proof.
Only this primitive enclosure changes. The reference maps, strict
necessary filters, four scalar formulas, clipped gains, gap, and
160-bit precision are identical.

The finite cover was assembled in three preserved stages.

| Stage | New visits | New accepted | New excluded | Pending afterward |
|---|---:|---:|---:|---:|
| [Original attempt](../repro/results/research-mixed-selected-half-row-budget-attempt01.json) | 4,000 | 343 | 1,653 | 9 |
| [Direct continuation](../repro/results/research-mixed-selected-half-row-budget-attempt02.json) | 8,000 | 3,547 | 453 | 9 |
| [Centered continuation](../repro/results/research-mixed-selected-half-row-budget-attempt03.json) | 4,321 | 1,032 | 1,133 | 0 |

The [direct resume wrapper](../experiments/resume_mixed_selected_half_row_budget.py)
and [centered resume wrapper](../experiments/resume_mixed_selected_half_row_centered_budget.py)
validate their immutable parent records, dependencies, prefix-free
partitions and exact address-to-box correspondence. They evaluate
only pending boxes and descendants. The final record preserves the
first 5,996 terminal leaves unchanged. Its explicit provider ranges
are \([0,5996)\) for direct evaluation and \([5996,8161)\)
for centered evaluation.

The completed partition has exactly 8,161 terminal leaves:
4,922 accepted and 3,239 excluded. Their binary addresses are
prefix-free with exact dyadic mass one; the total node count is
\(16321=2\cdot8161-1\). There are no unresolved cells.
The maximal depth is 20; newly accepted centered leaves have
depth 15 or 16. Every accepted leaf has all four scalar upper
bounds strictly below \(-1/2000\).

All 19,688 serialized acceptance inequalities have also been
checked using their exact rational directed endpoints, without
reevaluating a primitive or reference map. The largest upper
endpoints are approximately
\[
 \begin{array}{c|r}
 \text{main factorial}&-0.0005239462468974678\\
 \text{main forced}&-0.09064375078091134\\
 \text{left factorial}&-0.0339424093745029\\
 \text{left forced}&-0.11382462508874931 .
 \end{array}
 \tag{7}
\]
The exact rational values, rather than these displays, determine
acceptance. The independent data audit also verifies all 26 current
input bindings, the unchanged original leaf prefix, the full
partition and both provider ranges.

The final record is
[attempt03](../repro/results/research-mixed-selected-half-row-budget-attempt03.json),
SHA256
139ecaa3b79c911b8993ef291076a9bbd2b96d12b8aa0efc77a58eab0d8a0975.
Its preserved parents have SHA256
face0d1cfe67cd2134f3ff8c661c9589089c0aaec95ec7fb96f5ad0012db55c4
and
8728c18541d17fd0a6533deb60bacfe8bbb8c728c50b90123ee3bc8fc6f5ba22.
All proof and driver bindings are retained in the record. These
facts prove (3), and hence Theorem 1.

## 3. A literal finite high-row sector

Define the complete ordinary right-row subsum
\[
 C_{0,N}^{\ge1/2}(X,Y)=
 \sum_{j=\lceil N/2\rceil}^{N-1}
     \frac{X^{-j}p_j(X)p_j(Y)}{P_j^2}.
 \tag{8}
\]
No cap index is restricted, and no inner endpoint coefficient is
split. The [real-row endpoint theorem](research_mixed_right_tail_endpoint_bound.md)
applies at \(|H|,|h_b|<.108\). It bounds every real
ordinary rate on \([1/2,1]\) by \(\max(B_R,B_1)\),
with the original chirp, wrapped factors and zero-safe endpoint
limits. Theorem 1 controls every cap profile paired with \(B_R\).
The [last-row theorem](research_mixed_selected_four_three_last_rows.md)
already controls every cap profile paired with \(B_1\) by the
larger raw gap \(3/100\).

**Corollary 2.** For every \(\tau>0\), every fixed ordinary-color
derivative order \(k\), and all sufficiently large integer levels,
\[
 \begin{split}
 &\left|\partial_w^k\left\{
 U_{1,N}(w,X)C_{0,N}^{\ge1/2}(X,Y)d_N(X)X^{-N}
 \right\}\right|\\
 &\qquad\le C_{\tau,k}N^{D_{\tau,k}}
       \exp N\{M+\ell_b(v)-1/2000+\tau\}.
 \end{split}
 \tag{9}
\]
This holds uniformly on \(P^2\) and a sufficiently small fixed
ordinary-color disk about \(-2\), for both level parities.
At even levels (8) includes the exact half row; at odd levels its
first row lies just above one half. The same complete real-row
estimate covers both cases.

Indeed the full cap is bounded by its five original profiles,
while the absolute sum in (8) has only a polynomial number of rows.
Apply the just-proved joint comparisons to each possible cap/rate/
Fourier alternative. The complete cap packet, factorial estimates,
color disk and half-grid tolerances are those of the finite
reduction and use one total arbitrarily small \(\tau\).
Cauchy's formula gives the fixed ordinary-color derivatives.
For example \(\tau<1/4000\) gives the finite gap \(1/4000\).

## 4. One remaining independent comparison

Put
\[
 D_L(y,v)=\max_{\nu=0,1}
 \{A_L(y)+B_0(y,v)+W_\nu(y)-M-\ell_b(v)\}.
 \tag{10}
\]
The three-comparison bound in the right-cap-cut theorem, together
with (2), now gives for the entire literal finite product
\[
 \begin{split}
 &|\partial_w^k\{U_{1,N}(w,X)C_{0,N}(X,Y)d_N(X)X^{-N}\}|\\
 &\qquad\le C_{\tau,k}N^{D_{\tau,k}}
 \exp N\{M+\ell_b(v)+\max(-1/2000,D_L(y,v))+\tau\}.
 \end{split}
 \tag{11}
\]
The original outgoing tangent is present throughout. The complete
Fourier polynomial is neither divided out nor replaced by its value
at the reference.

The two explicit reference-only upper bounds for (10) are supplied
by [the left-cap/main-contour deduction](research_mixed_selected_cap_left_main_majorant.md).
Their uniform signs remain unproved. Thus (11) is a reduction to
one remaining joint profile, with two Fourier alternatives; it is
not a full selected-source gap. No conclusion about all open-word
regions, arbitrary short fillings or the volume conjecture follows
from this sector theorem alone.
