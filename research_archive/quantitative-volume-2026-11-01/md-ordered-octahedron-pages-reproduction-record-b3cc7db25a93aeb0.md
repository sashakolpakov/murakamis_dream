# Finite reproduction of ordered octahedral pages

1 November 2026. The portable runner is `audit_ordered_octahedron_pages.py`; its output is `ordered_octahedron_pages_results.json`. Run it from the repository root:

```sh
python3 /path/to/audit_ordered_octahedron_pages.py --output /path/to/results.json
```

If the working directory is elsewhere, supply `--repo /path/to/volume-conjecture`. The runner uses Python's standard library, SymPy, and the existing public `experiments/audit_actual_conway_bowtie_projection_cut.py` on one side of the comparison. It has no private imports or embedded private paths.

The independent side constructs the initial combinatorial octahedron from endpoint pairs, attaches a new colored octahedron at each terminal insertion, removes its attaching face, and merges adjacent white faces. It compares every oriented colored face cycle and every endpoint pair with the literal compiler after each insertion. The original circle sector order and the signed distinguished disk maps are retained separately. Both projection orientations are compared. Inverse turns are three actual rotations; half-turns are two actual rotations. The root adapter retains the physical half-turn.

The run includes chains, stars and branched ordered trees, arbitrary left/right child placement, physical half-turn decorations, inverse-quarter-turn frames and all three retained disk signs. The 128 cases are a finite sample, not an exhaustive enumeration of all tree shapes.

Exact counts:

- 128 cases with 2–9 circle vertices.
- 448 terminal attachments: 215 left insertions and 233 right insertions.
- 576 intermediate boundary spheres and cyclic page-list checks.
- 8,640 oriented colored face cycles in the primary projection, with the oppositely oriented projection also compared.
- 128 literal physical root-adapter comparisons.
- 704 retained distinguished circle seams, giving 1,408 signed disk-face identifications in the final cases.
- 28 exact SymPy rational identities: the three full odd edge returns entry by entry, apex images, the four marked peripheral multipliers and fixed flags, the charge equation, regulator cancellation, and normalized slope/threshold algebra.

All checks passed. Arithmetic is exact: finite permutations, combinatorial face operations and rational symbolic algebra. There are no numerical tolerances. These checks do not establish arbitrary-tree topology, a complex Gaussian estimate, analytic charge dominance, geometric completeness, or an invariant volume limit. Those remain the mathematical proofs being supplemented.

The signed seam check distinguishes the pure within-copy identifications from the odd cross-copy identifications. Positive and negative odd crossings have the same endpoint permutation; their distinct primitive words are checked separately as multipliers rho/Q and rho Q. The runner does not infer their difference from permutation data alone.

SHA256 records:

- Runner: `0a0c36e5d7e18856118ecd26353dc63c85b8b2ba7f0ae69231568552af3ca40c`.
- Results: `13cdd23bbbe02a31cf0bde53dffd9739baa68c760387461a50af921feefd2fae`.

Only private files were written. Earlier implementation snapshots are preserved alongside the final runner. The first snapshot's root test omitted the turn on its child module and therefore constructed a cap-degenerate test input; the final runner uses the actual strict root adapter. That correction was to the test construction, not to the theorem or endpoint conventions.
