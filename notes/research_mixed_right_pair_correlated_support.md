# A correlated comparison for two blocks incident to a right coordinate

Research proof, 4 November 2026. The full outward cover passes all 2,048 boundary products on 19,001 cells. This gives an original finite-source bound for isolated right coordinates, with the separation condition below; it does not settle the whole right region.

Use the source supports and exact critical tangent cancellation in [the full-row reduction](research_mixed_right_pair_raw_reduction.md). For a consecutive actual triple \(a,b,c\) with types \(\alpha,\beta,\gamma\), let \(C,P_L,P_R\) be its equation (11). **Theorem 1.** Every actual cyclic critical triple satisfies
\[
 \Re C-S_{\beta\alpha,P}(\Re P_L)-S_{\gamma\gamma,P}(\Re P_R)
 -\frac{151}{20}(\Im a)^2-\frac{11}{2}(\Im c)^2>1/5000,
 \qquad P=[.22,.45].
\tag{1}
\]

The cover uses all five-vertex windows with two external typed reference parameters. The global holomorphic branch on their full product is established by Lemma 2 in [the height theorem](research_mixed_cyclic_critical_height_bounds.md). Number the window vertices from zero to four, with legs \((s_j,t_j)\), and use \(a=t_1,b=t_2,c=t_3\). Both incoming and outgoing conditional roots are the original \(s_2,s_3\). Their central derivative sum vanishes by the literal window equation. Every actual cyclic word, including short words after repeating the period, appears in such a window.

The external rectangles are \(R_3=[.30,.39]+i[-.03,.02]\) and \(R_4=[.27,.33]+i[-.057,-.02]\). Full bidisk/window holomorphy is an earlier input, so the distinguished-boundary reduction is not being used to prove existence. For fixed raw source coordinates the negative of the left side of (1), before optimizing those coordinates, is the real part of a holomorphic expression plus positive multiples of squared imaginary parts of holomorphic legs. It is separately subharmonic in both external parameters. Taking the supremum over the fixed compact source rectangle preserves separate subharmonicity and local boundedness. Consequently a uniform strict comparison on the external boundary products extends throughout the full product.

The checker encloses each exact ten-variable logarithmic root using the earlier affine Newton method. It recomputes the root derivative with a finite Neumann expansion and a weighted-norm tail. The two condensed block Hessians then give derivatives of \(P_L,P_R\). Their source supports are bounded by the certified convex chords. If those chords are \(A_L k+B_L\) and \(A_R k+B_R\), the comparison reduces to the original plane at the fixed targets \(p=-A_L,q=-A_R\), minus the two height squares. Along each boundary parameter its exact derivative is
\[
 \Re\{(p-a)\,dP_L+(q-c)\,dP_R\}
 -\frac{151}{10}\Im a\,\Im da-11\Im c\,\Im dc.
\tag{2}
\]
The center is evaluated on a fresh point Newton box. An outward first-derivative enclosure bounds its variation on the entire cell. Exact prefix-free binary covers are required for all \(32\cdot4\cdot16=2048\) boundary products. No floating root or optimized target is an acceptance premise.

## Finite source and separated right coordinates

**Corollary 2 (four distinct blocks).** Take four consecutive original blocks with five reference outer coordinates \((d,a,b,c,e)\). The five references may come from any actual cyclic word; when the cycle has length four the first and last coordinate coincide. Let the middle target \(x\) be any real number in \([1/2,1]\), and let its two neighbors be any real \(p,q\in P\). The two outer targets have real parts in \(P\). An unselected outer target retains its original reference height; a selected type-four outer target has height \(7/500\). Then the product of these four literal allocated finite blocks is at most
\[
 C N^A\exp N\left\{\Re\sum_{v=1}^4\Gamma_v-\frac1{10000}\right\}.
\tag{3}
\]
Every row and true Fourier forcing term is retained. Fourier selections at the three real target coordinates have modulus one. Every selected subset is allowed.

Indeed, the middle two raw blocks obey the complete-row upper bound (12) of the reduction note, uniformly at every product zero and real seam. The left boundary block changes only its second height, with both real coordinates free; the right boundary block changes only its first height. Their respective costs are precisely the two terms subtracted in (1). The right-square packets give actual finite upper bounds on both boundary blocks. All type-four targets in those blocks either have their original negative height or are real in \(P\), where the Fourier comparison is relative. The only positive exponential tolerance needed is the uniform absolute Fourier upper bound at the right target. Spend a total tolerance smaller than \(1/10000\) against the strict reserve \(1/5000\). If one or both outer targets are selected, use instead [the selected/reset plateau theorem](research_mixed_selected_reset_plateau_support.md) on the corresponding boundary block. It supplies a full-source loss \(1/200\) relative to the same original plane, which is stronger than the nonnegative oriented debit already reserved in (1). Its other argument is the real reset coordinate, exactly as required, and both true Fourier alternatives remain included. The same proof therefore covers every selected subset. This proves (3) for both parities, with a fixed polynomial prefactor. The statement is an upper bound for original moduli, not a choice of holomorphic square root of a half-weight.

**Corollary 3 (separated right boxes).** Fix a cyclic word of length \(m\ge4\). Put each real outer coordinate either in \(P=[.22,.45]\) or in \(R=[.5,1]\), and suppose consecutive \(R\) coordinates around the cycle are separated by at least three \(P\) coordinates. Use the coupled graph whose cutoff equals one on \(P\) and zero on \(R\). The product and minimum-neighbor choices agree on these boxes: each right coordinate and its two neighbors have height zero, and all other heights are their geometric values when unselected and \(7/500\) when selected. Let \(r\ge1\) be the number of right coordinates, and let \(M\) be the real part of the original cyclic critical action. For every selected subset, its literal finite density and its integral over this box satisfy
\[
 |\text{contribution}|\le C_m N^{A_m}
                  \exp N\{M-r/10000\}.
\tag{4}
\]
Summing over all selected subsets preserves (4), since the number of subsets is fixed with the word length.

For the proof, assign to each right coordinate the four blocks in its distance-two star. The separation hypothesis makes these four-block sets disjoint, including cyclic distance exactly four. All untouched blocks have two plateau arguments. If neither is selected, fixed-height concavity from [the plateau theorem](research_mixed_plateau_accretivity.md) bounds the phase by its original tangent plane; its full packet and relative Fourier weights add only polynomial factors. If either is selected, [the selected plateau theorem](research_mixed_selected_plateau_support.md) supplies the stronger full-source loss \(1/200\) relative to that plane, with every forcing branch retained. Apply Corollary 2 to every star. All half-weights recombine to the original integer powers, and the sum of the full complex tangent terms cancels by original zero-lift stationarity. The coupled graph is piecewise constant in height on each such box, so its Jacobian is one almost everywhere; exact contour bookkeeping is supplied by [the coupled-graph theorem](research_mixed_coupled_outer_graph.md). The phase carrier has modulus one. These facts give (4) for the original finite source.

The separation condition excludes short cyclic gaps one, two and three. In particular an isolated right coordinate in a three-cycle has one adjacent plateau block whose two heights reset; this is not replaced by two one-height estimates. Boxes with closer right coordinates, transition angles, or low coordinates remain separate. No full mixed-cycle asymptotic is claimed.

```sh
python3 experiments/certify_mixed_right_pair_correlated_support.py --precision 256
```
