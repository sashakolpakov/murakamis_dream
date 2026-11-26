# Source supports at the ends of right-coordinate runs

Research proof, 4 November 2026. The complete correlated cover passes all 8,192 boundary products on 76,030 cells. It proves the local source comparisons used by the separate plateau/right incidence theorem.

Let \(P=[.22,.45]\) and \(R=[.5,1]\). All targets discussed in the raw blocks have height zero, and all original rows and real Fourier selections remain present. Use the original allocated phases and five-window branches of [the isolated-right theorem](research_mixed_right_pair_correlated_support.md), and the raw plateau-neighbor supports \(S_{e\alpha,P}\) of [the full-row reduction](research_mixed_right_pair_raw_reduction.md).

## 1. Right neighbors use a different source theorem

The plateau-neighbor reduction requires \(p<1/2\) and is not extrapolated to a right neighbor. Instead use the complete slope-aware corner reduction in [the two-right source theorem](research_mixed_two_right_source_bound.md), with slopes \((0,k)\), \(-1/5\le k\le1/4\). It includes the low-row extra-candidate comparison, the full upper-row range, zeros and both true Fourier forcing terms. Its four endpoint rates are \(c_{e,2}-k/2\), \(c_{e,1}-k\), \(c_{e,1}-k/2\), and \(c_{e,0}-k\). The third and fourth are dominated. The certified constants satisfy \(c_{e,2}-c_{e,1}>1/10\), so the first also dominates the second throughout the indicated slope interval. Thus the full right-neighbor support is exactly
\[
 T_e(k)=c_{e,2}-k/2.
\tag{1}
\]
The real right coordinates have Fourier upper rate zero, with the same arbitrarily small finite-source tolerance as in the two-right theorem. Equation (1) does not posit a continued saddle for them.

## 2. Correlated targets to be certified

For a right coordinate with one plateau and one right neighbor, sum its two original incident phases. The center gradient cancels exactly, leaving a plane \(C+P_Lp+P_Rq\). Use \(S\) for the plateau neighbor and \(T\) for the right neighbor. Reserve the oriented reset debit \((151/20)(\Im a)^2\) for a left plateau neighbor and \((11/2)(\Im c)^2\) for a right plateau neighbor. Additionally reserve
\[
 f_L=1683/100000\quad\text{if the left plateau neighbor is type three},
 \qquad
 f_R=1202/100000\quad\text{if the right plateau neighbor is type three}.
\tag{2}
\]
These explicit allowances are intended for a later doubly reset plateau-block allocation; no such allocation is inferred merely from this local comparison.

For a run of exactly two right coordinates, use its three incident blocks between two plateau neighbors. The two internal critical gradients cancel, so again only the two external slopes remain. The source support is
\[
 S_{\beta\alpha,P}(\Re P_L)+c_{\gamma,2}
       +S_{\delta\delta,P}(\Re P_R),
\tag{3}
\]
where \((\alpha,\beta,\gamma,\delta)\) are the four outer types. Reserve both oriented debits and both applicable allowances (2). The common maximizing right target in these raw-envelope formulas is one half; all upper-row contributions are dominated by the proved endpoint reductions.

**Theorem 1.** The original supporting-plane sum minus the complete raw support, stated reset debits and applicable allowances has strict reserve \(>1/5000\) in each case. Its checker uses five-vertex windows for the endpoint pairs and six-vertex windows for the three-block run. The actual outer reference coordinates are \(t_1,t_2,t_3\), or \(t_1,t_2,t_3,t_4\), respectively. Original logarithmic stationarity cancels every internal reference derivative, including for repeated cyclic periods.

After the source supports are replaced by their upper chords, the derivative of the plane-minus-debit is exactly the two-boundary derivative (2) in the isolated-right proof. The original ten- or twelve-variable affine Newton self-map, weighted Neumann response remainder, midpoint root and full-cell derivative bound are all rechecked. Each negative support defect is separately subharmonic in the two external parameters, including the positive reset squares, so the complete boundary covers suffice after the already proved global window holomorphy. No target grid or numerical stationary value is accepted as proof.

There are \(2048+2048+4096=8192\) boundary products. Exact source constants, complete case sets, dyadic coverage and unchanged dependencies are checked explicitly. The existing isolated-right certificate remains frozen and retains its own scope.

```sh
python3 experiments/certify_mixed_right_run_supports.py --precision 256
```
