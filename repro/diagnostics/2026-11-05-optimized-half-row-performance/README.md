# Why the bounded optimized pilot did not gain coverage

This is a performance diagnosis of existing accepted trees, not a
new parameter search or a uniform sign certificate. Three fixed
saved witnesses were revalidated and their existing acceptance
expressions reevaluated at 256 bits. There were no root proposals,
new boxes or subdivisions.

The exact full-prefix comparison is in the
[optimized pilot archive](../2026-11-05-optimized-half-row-support-pilot/README.md):
both 511-node pilots resolved volume 535/262144 and left the same
14-box frontier. The optimized rule refined two local boxes that
the old rule accepted, while coarsening two other sibling pairs.
Their maximum depth remained 18.

## The three fixed boxes

Addresses use the original right-first exact binary trees.

| Saved box | Reason selected | Depth |
|---|---|---:|
| 11111111100001010 | Old rule accepted; optimized rule refined | 17 |
| 11111111101011101 | Optimized rule accepted; old rule refined | 17 |
| 111111111111111 | Accepted by both rules | 15 |

The evaluator is [diagnose.py](diagnose.py); the interval components
are [result.json](result.json). It imports the unchanged two
checkers, instruments only their returned diagnostic fields in
memory, and supplies the saved rational targets. The original
root certifier revalidates each saved witness without proposing or
solving for a new root.

For the limiting orientation, rounded outward component bounds are:

| Box | Rule | Mean-value upper | Target gain upper |
|---|---|---:|---:|
| Old-only parent | Fixed trial | .0195 | .01343 |
| Old-only parent | Optimized envelope | .0331 | \(2\cdot10^{-15}\) |
| New-only parent | Fixed trial | .0214 | .01514 |
| New-only parent | Optimized envelope | .0364 | \(2\cdot10^{-15}\) |
| Common box | Fixed trial | .0260 | .01790 |
| Common box | Optimized envelope | .0443 | \(2\cdot10^{-15}\) |

The midpoint gain has disappeared as intended, but widening the
gradient evaluation from a fixed trial to its interval optimizer
box has nearly replaced that cost. The optimized rule is therefore
not pointwise stronger than the old acceptance test.

The optimized mean-value contributions from the circle angle,
disk radius and disk angle, respectively, are approximately
\[
\begin{array}{c|ccc}
 &\theta&\rho&\psi\\ \hline
\text{old-only parent, side 1}&.00598&.00204&.02510\\
\text{new-only parent, side 1}&.00645&.00203&.02790\\
\text{common box, side 1}&.01480&.00377&.02580
\end{array}
\]
These are upper interval contributions, not derivative midpoint
values. Both orientations are retained in the saved result.

The nonlinear affine-root remainder radii are about .00046--.00060,
whereas full root coordinate halfwidths are about .0033--.0048.
Thus most root width in these examples comes from genuine input
variation through the affine map, rather than the nonlinear
remainder alone. The complete pilot's 68 root versus 194 source
subdivisions also locate the larger bottleneck at source acceptance.
These three examples do not characterize every remaining box.

## One proposed modification: recorded adaptive splitting

On a source-bound failure with finite envelope derivatives, compute
for each parameter axis
\[
 E_j=\max_{\text{failed orientations }s}
                  h_j\sup|\mathcal G_{s,j}|.
\]
Bisect an axis with largest \(E_j\), using a deterministic tie rule.
Evaluate both orientations before making this choice. If a root
enclosure or finite derivative bounds are unavailable, retain the
existing cyclic-axis fallback. Do not change the mathematical
acceptance inequality.

The evidence for this proposal is directional: the disk-radius
cost is small in all three examples, yet the current cyclic rule
spends one third of its splits on that axis. An adaptive choice can
instead refine the angular direction responsible for the larger
mean-value enclosure. This is a proposed efficiency change, not
a prediction that a full certificate will finish.

The coverage proof does not require cyclic axes. A midpoint split
along any recorded axis in {0,1,2} partitions its exact rational
parent box. Induction over the saved tree gives complete coverage;
each split halves volume regardless of axis. The optimized-envelope
bound already applies to arbitrary rectangular parameter boxes
with their actual halfwidths. Saved replay must reconstruct the
recorded axis, not recompute the heuristic at a new precision.

Keep all existing accepted nodes immutable. Graft adaptive subtrees
only onto the current exact pending frontier. Preserve the pinned
completed old face and its exact exchanged opposite. Old imported
trees retain their old cyclic validation and acceptance rule.
The equal-type exchange keeps the three parameter labels, so it
also transports recorded adaptive axes unchanged.

No adaptive code, new pilot or full run was executed for this
diagnosis.

## Provenance

Source records:

- Original pilot SHA256:
  f53dc6380862fb1c824755732202f002388c49ba5ad6e52c84c10306e77c2591.
- Optimized pilot SHA256:
  16e0ffe2e8b2ad6d33ecefbf34f1c6f01523d49102072d06ecf145ac20cec145.
- Original checker SHA256:
  1126603ccf44d8240d4ef82f086e034d7209031b1e56a7ab9a5a8a79c5dae490.
- Optimized checker SHA256:
  47c1b9e2cb546c0adf9e066dff112c54bdda68aa4c4473c6373986a2969cf9df.

The component result is diagnostic evidence only. The existing
author and partial records, proofs and checkers remain unchanged.
