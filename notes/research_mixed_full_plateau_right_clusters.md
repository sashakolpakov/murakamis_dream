# Allocating every plateau/right cluster without overlapping source bounds

Research proof, 4 November 2026. The full right-run source cover is complete. This note proves the original finite-source bound on every plateau/right configuration, with all selected subsets and the cyclic short cases included.

Let \(P=[.22,.45]\), \(R=[.5,1]\), and fix an original cyclic word of types three and four. Its actual zero-lift critical reference is denoted \(z_*\), and \(M\) is the real part of its original critical action. Use the exact coupled graph with cutoff one on \(P\) and zero on \(R\). On each \(P/R\) box, every right coordinate and its adjacent plateau coordinates have height zero. An untouched plateau coordinate has its geometric height when unselected, and height \(.014\) when selected. This is the same literal graph for either the product or minimum-neighbor formula on these boxes; its Jacobian is one almost everywhere.

All source bounds below are for original finite kernels and the actual polynomial Fourier factors. A selected factor at a real coordinate has modulus one. Each selected subset is treated separately before the finitely many contributions are summed. No source comparison is imported from the old independent-height taper.

## 1. Boundary debits and their extra allowances

For a right run with a left plateau neighbor \(a\) and a right plateau neighbor \(c\), reserve the oriented charges
\[
 L(a)=\frac{151}{20}(\Im a)^2,\qquad
 R(c)=\frac{11}{2}(\Im c)^2.
\tag{1}
\]
The order matters: the left plateau boundary block resets its second coordinate, while the right block resets its first. Both real coordinates may readjust.

Reserve in addition a left allowance \(f_L=1683/100000\) whenever \(a\) is type three, and a right allowance \(f_R=1202/100000\) whenever \(c\) is type three. These are charges in the supporting-plane comparison, not new phase constants.

The frozen isolated-right cover has the following lower reserves after (1), rounded downward from its outward cells. Rows list the neighboring/center types as binary indicators.
\[
\begin{array}{c|rrrrrrrr}
 (\alpha,\beta,\gamma)&000&001&010&011&100&101&110&111\\\hline
 \text{reserve}&.0695&.024&.138&.077&.0487&.0002&.098&.035
\end{array}
\tag{2}
\]
Subtracting the applicable left/right allowances still leaves at least \(1/5000\) in every case. The [right-run source theorem](research_mixed_right_run_supports.md) proves that same reserve after its applicable charges and allowances. Its two endpoint modes treat a single right coordinate with one right neighbor; its third mode treats a run of exactly two right coordinates.

## 2. Partition the original edges, not the inequalities

Assume first that both \(P\) and \(R\) occur, and decompose the right coordinates into maximal cyclic runs. A run of length \(r\) is assigned as follows.

- If \(r=1\), its two incident edges form the isolated-right pair.
- If \(r=2\), its three incident edges form the new three-block source piece.
- If \(r\ge3\), assign the first two edges to the left endpoint pair and the last two to the right endpoint pair. The remaining \(r-3\) internal right/right edges are individual blocks.

These edge sets are disjoint. For \(r=3\), the endpoint pairs meet only at their common middle vertex. Different runs have disjoint right-incident edges, even when they share one plateau boundary vertex. All untouched edges are plateau/plateau edges. In particular no shared right/right edge is counted twice.

Every source piece reserves exactly one charge and one possible type-three allowance at each plateau boundary it meets. There are no charges at its internal right neighbors. The all-right case is handled directly by the already proved full right/right block theorem and requires no run partition.

## 3. Spend each boundary charge at most once

Consider a plateau edge with its original ordering \((p,q)\).
If only its first height resets, use its right-boundary charge \((11/2)(\Im p)^2\). If only its second resets, use its left-boundary charge \((151/20)(\Im q)^2\). The oriented theorem includes arbitrary real readjustment of both coordinates.

An edge whose two heights reset can occur only in a plateau run of length two. If both types are four, the [same-sign reset cone](research_mixed_same_sign_height_reset.md) supplies exactly the sum of these two charges: both original heights are negative and both targets are real. No matrix domination on unrestricted height directions is inferred.

If at least one type is three, use instead the safe full-matrix bound \(10[(\Im p)^2+(\Im q)^2]\). Its excess over the already reserved charges is
\[
 \Delta(p,q)=\frac92(\Im p)^2+\frac{49}{20}(\Im q)^2.
\tag{3}
\]
The actual reference bounds give \(|\Im z_3|\le.03\), \(|\Im z_4|\le.057\). If the first type is three, irrespective of the second type,
\[
 \Delta\le\tfrac92(.03)^2+\tfrac{49}{20}(.057)^2
       =.01201005<f_R.
\tag{4}
\]
Charge this to the right allowance of the preceding right run. Otherwise the second type is three, and
\[
 \Delta\le\tfrac92(.057)^2+\tfrac{49}{20}(.03)^2
       =.0168255<f_L.
\tag{5}
\]
Charge it to the left allowance of the following right run. If both types are three, the first rule is used. Each plateau boundary incidence is adjacent to at most one plateau edge, so no allowance is spent twice. A plateau run of length one has no plateau edge, and its two reserved charges and allowances may simply remain unused. This includes parallel incidences in a two-cycle.

For a singly reset edge whose untouched endpoint is selected, the selected/reset theorem gives a full finite loss \(1/200\), which is stronger than the nonnegative charge above. For a doubly reset edge every selection has modulus one. An edge with no reset uses either unselected fixed-height plateau concavity or the selected-plateau finite loss. Thus all selected subsets fit the same accounting.

## 4. The remaining finite-source reserve

For each two- or three-edge source piece, spend less than \(1/10000\) in total on its uniform true-Fourier upper tolerances. Its phase reserve \(1/5000\) then leaves a full finite-source loss \(1/10000\), after all charges and allowances. Plateau targets lie in the compact interval \(P\subset(0,1/2)\), so the unselected weights on all reset/untouched plateau edges are relative; they require no extra positive exponential tolerance. Selected plateau bounds already include their own tolerance reserves.

Each unused right/right edge has its proved finite loss \(1/100\). A run of length one or two therefore loses respectively \(1/10000\) or \(1/10000\). A longer run loses at least
\[
 \frac2{10000}+\frac{r-3}{100}\ge\frac{r}{20000},
 \qquad r\ge3.
\tag{6}
\]
The same lower bound \(r/20000\) holds for \(r=1,2\). In the all-right case it follows directly from the right/right loss per edge, including the single loop at length one.

After every edge has been used once, all half-weights recombine to the original integer Fourier weights. The sum of the full complex tangent terms cancels by the original cyclic zero-lift equations, leaving \(M\). Carrier moduli are one and all remaining level powers are polynomial. **Theorem 1.** Consequently, every box with \(n_R\ge1\) right coordinates obeys
\[
 |\text{original contribution}|\le C_m N^{A_m}
                \exp N\{M-n_R/20000\}
\tag{7}
\]
for every selected subset, both parities, and its actual coupled-graph integral. The total number of boxes and subsets is fixed for a fixed word. This deduction has no uniform-in-word-length assertion for prefactors or the starting level.

The unaliased pure plateau box retains its previously proved nonzero original central coefficient. A nonempty selection on the pure plateau box has the existing selected-plateau loss. Thus (7) gives the same original central coefficient for the complete restricted \((P\cup R)^m\) integral. Transition angles and low coordinates remain outside this domain; no whole outer-period or volume-limit claim is made here.
