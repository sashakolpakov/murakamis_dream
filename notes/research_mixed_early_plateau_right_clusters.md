# Early, plateau and right coordinates on the periodic hybrid

Research theorem, 5 November 2026. On one fixed periodic hybrid, the
original contribution from \(([0,.12]\cup P\cup R)^m\) retains the
central coefficient with error gap \(1/160000\); its low-present
part has absolute gap \(1/4000\). The completed early block and
raw right-source estimates first give the intermediate region
\[
 E=[1/10,3/25],\qquad P=[11/50,9/20],\qquad R=[1/2,1].
 \tag{1}
\]
Early heights are retained; they need not be zero. Sections 5--7
add every low coordinate and arbitrary seam contacts.
No new source or reference cover is used. The remaining transition
intervals, the complete outer period and a new knot family are not
claimed.

## 1. The graph and the original rates

Fix an original cyclic word of length \(m\ge1\), its actual complex
reference \(r\), and every permitted selection \(\sigma\). Write
\(c_j=\Im r_j\) and let \(M\) be the real critical action. Use
the exact [periodic hybrid](research_mixed_split_cutoff_hybrid_contour.md)
with any fixed \(0<\rho\le.001\). On the region (1), a prescribed
height is \(c_j\) when unselected and \(H=7/500\) when selected.
Its actual value is
\[
 h_j=h_j^{\,0}R_\rho(x_j)
       \min_{k\in\{j-1,j,j+1\}}L_{b_j}(x_k),
 \qquad b_j=\begin{cases}.22,&\sigma_j=0,\\ .12,&\sigma_j=1.
 \end{cases}
 \tag{2}
\]
Every R coordinate is real, and its left cutoff equals one. It
therefore does not reset a neighboring plateau height. A P endpoint
is affected exactly when it has an E neighbor; calling it affected
even when its height happens to be prescribed only overestimates
costs. The actual height of an unselected affected P endpoint lies
between zero and \(c_j/6\); a selected one lies between zero and
\(H\). An E target has the same small height bounds.

Use coherent conditional rates on EE, EP and PP edges, with their
true selected corrections, and complete raw row envelopes on every
R-incident edge. Each is the rate of the original allocated
nonnegative modulus
\[
 |C_{\epsilon_j,N}(X_{j-1},X_j)|
 |d_N(X_{j-1})X_{j-1}^{-N\sigma_{j-1}}|^{\epsilon_{j-1}/2}
 |d_N(X_j)X_j^{-N\sigma_j}|^{\epsilon_j/2}.
 \tag{3}
\]
No modulus-one assertion is made for \(d_N\). Its forcing alternative
and every selected monomial remain in these rates. The two halves
at every original cyclic vertex recombine once.

First move all R real angles to \(1/2\), keeping the raw labels.
The [complete complex-neighbor row comparison](research_mixed_complex_right_row_reduction.md)
does not decrease the total mixed upper rate. Both old and new R
coordinates have height zero and left cutoff one, so every other
target, selection and height is unchanged. This operation compares
upper rates; it is not a change of variables or a monotonicity
claim for the finite kernels. Relative to the original complex
tangents, the same comparison holds after summing all incident
edges, by original critical stationarity. Henceforth all estimates
are at these half-angle R targets.

## 2. Local source allowances before one common tolerance

Put
\[
             \delta_E=\frac1{100},\qquad
             q_0=\frac{11}{2},\qquad q_1=\frac{151}{20},
             \qquad b_R=\frac1{200}.
 \tag{4}
\]
The [early-transition theorem](research_mixed_early_transition_support.md)
gives an EE edge loss \(\delta_E\), discarding its extra allowance.
On EP or PE it gives loss \(\delta_E\) together with the
oriented credit \(q_jc_p^2\) for its plateau endpoint. Its height
hypotheses hold independently: the unselected type-three targets
lie in \([-1/200,1/300]\), the unselected type-four targets in
\([-19/2000,0]\), and selected type-four targets in \([0,H]\).
Both actual Fourier branches are covered. The complete early-cap
source is the same one used in the
[early/plateau assembly](research_mixed_early_plateau_clusters.md).

For ER or RE, write \(s(y)=(y-.1)/.12\), where \(y\in E\).
Equation (2) implies the target bands
\[
 \begin{array}{c|c}
 3&-.03s(y)\le h\le .02s(y)\\
 4\text{ unselected}&-.057s(y)\le h\le0\\
 4\text{ selected}&0\le h\le .014\min\{6s(y),1\}.
 \end{array}
 \tag{5}
\]
These are precisely the bands of the completed
[transition/right source theorem](research_mixed_transition_right_support.md).
At right angle \(1/2\), its full raw comparison, before the final
finite-source tolerance, gives defect at most \(-1/1000\).
It includes all rows, both orientations, both level parities and
every selection at either endpoint.

For a PR or RP edge whose plateau endpoint is affected, use the
underlying raw ceiling
\[
                    \text{raw rate}-\Re\Gamma < b_R=\frac1{200}.
 \tag{6}
\]
This is the actual certified ceiling in equation (10) and Section 4
of the [partial-reset right theorem](research_mixed_partially_reset_right_support.md),
not its separately rounded finite ceiling \(1/100\). The zero-height
core supports have ceiling \(1/200\); the prescribed-height supports
have negative margin \(1/500\). Convexity in height bounds every
fraction between these endpoints by \(1/200\), separately retaining
the true forcing alternatives. The complete upper-row reduction at
the same angle and height gives (6) for every original row at
right angle \(1/2\). This uses all the partial heights in (2);
no target/reference height dependence is treated as holomorphic.

If the plateau endpoint is unaffected, its height is prescribed and
the original right-core support has negative defect. A PP edge with
no affected endpoint has nonpositive defect, by unselected plateau
concavity or the selected plateau bound. An RR edge has the
strict raw margin \(1/50\) of the
[two-right source theorem](research_mixed_two_right_source_bound.md);
only its nonpositive defect is needed here.

The PP reset costs are exactly those of the early/plateau assembly.
A single affected endpoint costs its assigned oriented credit.
For two affected endpoints of types \(u,v\), with reference heights
\(a,b\), the cost is at most \(q_0a^2+q_1b^2\) if both types
are four, and at most \(10(a^2+b^2)\) otherwise. This holds for
all mixtures of partial selections by height convexity and the
selected/reset endpoint bounds. Its excess over the two credits is
bounded by
\[
 \begin{array}{c|cccc}
 (u,v)&(3,3)&(3,4)&(4,3)&(4,4)\\ \hline
 \text{excess}&.006255&.01201005&.0168255&0.
 \end{array}
 \quad
 D_*=\frac{33651}{2000000}.
 \tag{7}
\]

## 3. Assign each early/plateau incidence once

Let \(n_{EE},n_{EP},n_{ER}\) count the original edges of these
types, with both orientations included. Put
\(n_E=n_{EE}+n_{EP}+n_{ER}\), the number of edges incident to E.
A plateau vertex having one E incidence has exactly one other
incidence. If that other edge is PP, assign its EP credit to the
affected PP endpoint as before. If it is PR, assign that EP edge
to pay (6) instead; its unused nonnegative credit can be discarded.
A plateau vertex between two E vertices has no PP or PR edge to
pay. This assigns no EP edge twice.

Let \(a_R\) count the EP edges assigned to PR, and let \(d_P\)
count doubly affected PP edges. Each such double PP edge has two
distinct EP payers, neither assigned to PR. Distinct double PP
edges also have disjoint payers. Therefore
\[
                         2d_P\le n_{EP}-a_R.
 \tag{8}
\]
After the single PP costs have been paid, the total defect is at most
\[
 -\frac{n_{EE}+n_{EP}}{100}
       +\frac{a_R}{200}+D_*d_P-\frac{n_{ER}}{1000}.
 \tag{9}
\]
Inserting (8), its negative is at least
\[
 \frac{n_{EE}}{100}
   +\frac{a_R}{200}
   +\frac{6349}{4000000}(n_{EP}-a_R)
   +\frac{n_{ER}}{1000}
                     \ \ge\ \frac{n_E}{1000}.
 \tag{10}
\]
Thus the early allowance pays affected PR edges as well as PP
edges. Its reserve is used only once. The imaginary tangent terms
cancel with all real tangent terms in the full cyclic sum, leaving
\(M\).

This is an arbitrary-length degree-two argument. A one-cycle in E
has one early loop and no plateau charge. In a mixed two-cycle,
an E/P pair has two distinct EP edges and no PP edge; an E/R pair
has two ER edges. A plateau vertex shared by two early vertices has
no outside incidence, regardless of whether those early vertices
are identified in a short period. No four-distinct-vertex assumption
or division by a source factor is used.

## 4. Complete finite integral and scope

**Theorem 1.** For every fixed word and every original selection,
the mixed phase/raw rate on \((E\cup P\cup R)^m\) is at most
\[
                            M-\frac{n_E}{1000}.
 \tag{11}
\]
Every target in the coherent part lies in the completed early-cap
or plateau source products. The raw part includes all original rows
and the true Fourier-polynomial upper bounds. Choose one positive
total finite-source tolerance less than \(1/2000\) over all physical
edges. Equations (6) and (11) are unrounded rate bounds, so no
already-rounded finite gap is charged a second tolerance. Since
\(n_E\ge1\) whenever an early coordinate is present, this gives
\[
 \sum_\sigma\int_{(E\cup P\cup R)^m\setminus(P\cup R)^m}
   |\mathcal D_{N,\sigma}(x)\det(I+iD\mathcal H_\sigma(x))|\,dx
       \le C_mN^{A_m}e^{N(M-1/2000)}.
 \tag{12}
\]
The fixed hybrid Jacobian, scalar powers of \(N\), and finite
number of selections change only the prefactor. Both integer-level
parities are included.

On the no-E region \((P\cup R)^m\), the hybrid is exactly the
independent right graph. Its already proved pointwise selected
source estimates retain the unselected plateau coefficient, as
recorded in Section 5 of the
[hybrid low/plateau/right theorem](research_mixed_hybrid_low_plateau_right_clusters.md).
Combining that separate result with (12) gives
\[
 \mathcal Z_N^{\rm hyb}((E\cup P\cup R)^m)
   =\mathcal I_{N,\varnothing}(P^m)
        +O\!\left(N^A e^{N(M-1/160000)}\right).
 \tag{13}
\]
The central coefficient is counted once.

## 5. Adding the whole low interval without clamping right angles

For the remainder of the note choose the collar \(\rho\) once,
independently of the level, below \(1/1000\) and the inherited
uniform endpoint-thickening radius of the
[hybrid low/plateau theorem](research_mixed_hybrid_low_plateau_clusters.md),
Section 1. Thus the direct endpoint bound used for unused half-edges
has its stated positive finite gap. Partition the new low interval as
\[
 S=[0,\rho],\qquad D=(\rho,.1],\qquad E_+=(.1,.12],
 \qquad T=D\cup E_+=(\rho,.12].
 \tag{14}
\]
These sets are disjoint, including their boundary convention. Denote
also by \(S\) the set of positions with their real coordinate in
this interval. Unlike Section 1, the proof below leaves every
physical right angle unchanged.

First use the complete seam-pair inequality at power \(1/2\) for
each seam vertex. An edge with \(k\in\{1,2\}\) seam endpoint
incidences receives exponent \(k/2\); supply its unused exponent
\(1-k/2\) from the direct endpoint bound. The original
[fractional seam allocation](research_mixed_hybrid_low_plateau_clusters.md),
Section 3, therefore gives finite loss at least
\[
                              |S|/10
 \tag{15}
\]
on all edges incident to \(S\). It allows arbitrary neighboring
real angles and full physical height bands, so E and R neighbors
are included. Discard the nonnegative reserved \(Q\) and the
unused direct endpoint losses. These edges have now been used
once and will not be used again.

A plateau endpoint is S-affected if it has a seam incidence.
For a PP block with at least one S-affected endpoint, pay for its
entire possible defect, including its other endpoint, using
\[
 C_*=\max\left\{
  (q_0+q_1)(.057)^2,\ 10\bigl((.057)^2+(.03)^2\bigr),\
                      20(.03)^2\right\}
       =.04239945<\frac9{200}.
 \tag{16}
\]
The first term is the same-sign type-four reset cost; the other
two terms are the full matrix cost. Successive height convexity
and the selected/reset corners give these bounds for all partial
selections, just as in Section 2. Charging an unchanged endpoint
as if it could change only enlarges this nonnegative bound.

For a PR block with an S-affected plateau endpoint, the completed
partial-reset theorem gives the whole-angle finite ceiling
\[
                         \Re\Gamma+\frac3{500}.
 \tag{17}
\]
Indeed its proof has raw core ceiling \(1/200\), then the original
whole-angle and full-row reductions and the already negative endpoint
\(1\) bound. Choose its one total finite-source tolerance less than
\(1/1000\). This yields \(1/200+1/1000=3/500\), throughout
\([.5,1]\), for both orientations and all physical height fractions.
No numerical threshold or source cover is changed. Equation (17)
already includes this block's Fourier/product tolerance and will
not receive the later AA tolerance.

Assign each PP or PR block just described to one of the SP incidences
which makes its plateau endpoint S-affected. A given SP incidence
has one plateau endpoint and at most one other incidence, so it can
be assigned at most one outside block. If both PP endpoints are
S-affected, choose one payer and charge the whole block only once.
Every such block costs less than \(9/200\), by (16)--(17), and
there are at most \(2|S|\) assigned blocks. The seam loss (15)
therefore leaves at least
\[
                  |S|/10-(9/200)\,2|S|=|S|/100.
 \tag{18}
\]
The AA tolerances for the PP blocks in (16) are reserved for the
single final tolerance below. Every other source used in (15) and
(17) is already a finite bound.

## 6. The remaining T incidences

All counts in this section exclude the already consumed S-incident
edges. A TT block of two E vertices has early phase loss \(1/100\).
If at least one endpoint lies in D, both its targets are real:
DD has the closed finite loss \(1/100\), and DE has the uniform
real one-low finite loss \(1/20\). These are the completed inputs
of the [uniform real low theorem](research_mixed_uniform_real_low_support.md)
and the [closed both-low source](research_mixed_both_low_raw_support.md).
Thus every TT block supplies \(1/100\), before an AA tolerance
only where its estimate was a coherent early rate.

For TP, an E endpoint supplies the phase allowance
\(1/100+q_jc_p^2\) as before. A D endpoint forces both heights
to zero and supplies the finite loss \(1/20\). This also supplies
the same allowance, because
\[
             \frac1{100}+\frac{151}{20}(.057)^2
                       =.03452995<\frac1{20}.
 \tag{19}
\]
Any additional attenuation from a seam neighbor preserves the E
source bounds. For TR or RT, a D target has the real low/right
finite loss \(1/2000\) proved in the
[hybrid low/plateau/right theorem](research_mixed_hybrid_low_plateau_right_clusters.md),
Lemma 1. An E target has that same finite loss from the complete
transition/right theorem. Both bounds hold at the physical right
angle, without clamping.

Remove the outside PP/PR blocks already paid wholly by an SP
incidence. On the remaining PP edges, only T-induced changes remain
and the old oriented credit allocation applies. On a remaining
affected PR edge, use the finite ceiling (17), assigning it to its
unique TP incidence. TP credits next to an already S-paid PP block
remain unused. Let \(a_R\) now count the TP payers assigned to
these remaining PR blocks, and let \(d_P\) count the remaining
doubly affected PP blocks. Their two TP payers are distinct and
not assigned to PR, so again
\[
                         2d_P\le n_{TP}-a_R.
 \tag{20}
\]
Here \(n_{TT},n_{TP},n_{TR}\) count edges not incident to S,
and \(n_T=n_{TT}+n_{TP}+n_{TR}\).

After the seam charges, all remaining positive debits are therefore
paid with total retained loss at least
\[
 \begin{split}
 \frac{|S|}{100}
 &+\frac{n_{TT}}{100}+\frac{a_R}{250}
 +\frac{6349}{4000000}(n_{TP}-a_R)
 +\frac{n_{TR}}{2000}\\
 &\hspace{25mm}\ge \frac{|S|}{100}+\frac{n_T}{2000}.
 \end{split}
 \tag{21}
\]
The coefficient \(1/250\) is exactly \(1/100-3/500\).
No TP edge pays two outside blocks. In particular, a PP block
having one S-affected and one T-affected endpoint was paid wholly
from S; its T allowance is not spent again. Untouched PP, PR and
RR blocks have their existing nonpositive finite or phase bounds.

## 7. The larger restricted original integral

**Theorem 2.** On the fixed hybrid just specified, let
\[
                           W_m=([0,.12]\cup P\cup R)^m.
 \tag{22}
\]
For every fixed original word, all original selections on its
low-present part satisfy
\[
 \sum_\sigma\int_{W_m\setminus(P\cup R)^m}
 |\mathcal D_{N,\sigma}(x)\det(I+iD\mathcal H_\sigma(x))|\,dx
        \le C_mN^{A_m}e^{N(M-1/4000)}.
 \tag{23}
\]
Choose one common total tolerance less than \(1/4000\) for the
remaining coherent AA estimates, including the PP bounds in (16).
The PR ceiling (17), every TR loss, and the seam/real-low bounds
are already finite inequalities and are not charged again.
If \(S\ne\varnothing\), (21) leaves at least \(1/100\) before
this tolerance. Otherwise a low coordinate belongs to T, and
\(n_T\ge1\), leaving at least \(1/2000\). This proves (23).
All tangent terms cancel on the original cycle, and each original
source halfweight occurs exactly once.

The incidence statements include loops and parallel edges. A seam
loop is squared by its pair inequality and restored by its
half-power. A T loop uses its TT bound. A plateau vertex in a
mixed two-cycle has two S or T incidences and no outside block.
The remaining cases keep their two distinct boundary edges.
No source is divided out, and no zero-coordinate coherent packet
is assumed. All levels of either parity and all approaches to
zero are covered, for this fixed positive collar.

The no-low part is the same established \((P\cup R)^m\) region as
in Section 4. Consequently
\[
 \mathcal Z_N^{\rm hyb}(W_m)
   =\mathcal I_{N,\varnothing}(P^m)
       +O\!\left(N^A e^{N(M-1/160000)}\right).
 \tag{24}
\]
The original central coefficient and normalization are retained
once. The two intervals \((.12,.22)\) and \((.45,.5)\) remain
outside this conclusion. No complete outer-period, insertion into
an arbitrary partial filling, or new knot-family theorem follows.

Reproduction:

    python3 experiments/check_mixed_early_plateau_right_clusters.py

The checker verifies the exact source-domain inclusions, reset
arithmetic, both incidence allocations, and complete current input
bindings. Its short-cycle checks are diagnostics of the written
arbitrary-length argument, not a substitute for that proof. No new
source or reference cover is computed.
