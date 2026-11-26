# One bounded adaptive half-row continuation

The root agent reviewed and ran exactly one continuation. It stopped
at the fixed budget of 511 additional nodes, with status incomplete.
No full half-row run or further continuation followed.

The input was the
[optimized weak-face pilot](../2026-11-05-optimized-half-row-support-pilot/README.md).
All 511 original tree nodes and 249 accepted leaves were imported
unchanged. Only its fourteen pending boxes were processed; old
root/source evaluations and root proposals were not repeated.

Command:

    python3 experiments/continue_mixed_optimized_half_row_pilot.py --precision 256

The [result](result-partial.json) records:

| Quantity | Result |
|---|---:|
| Additional attempted nodes | 511 |
| Additional accepted leaves | 256 |
| Total tree nodes / accepted leaves | 1022 / 505 |
| Pending boxes | 13 |
| Maximum visited depth | 18 |
| Initial resolved volume | 535/262144 |
| Final resolved volume | 37/8192 |
| Added resolved volume | 649/262144 |
| Remaining volume | 8155/8192 |
| Elapsed time, including setup | 3.1074 seconds |

Every new accepted leaf passed the same optimized-envelope
inequality in both orientations, with all target coordinates
included. The worst saved new upper bound is below
\(-0.0006221912217644\), stricter than the requested \(-1/2000\).
No point obstruction was reported.

The split counts were 131 adaptive source-cost choices, 67 cyclic
root-enclosure fallbacks, and 57 cyclic nonfinite-source fallbacks.
Of the adaptive choices, 116 split the disk-angle parameter and
15 split the circle-angle parameter; none split the disk radius.
This reflects the directional cost scores used by the algorithm.
It is not by itself evidence of a computational speedup.

## What the result does and does not compare

This run adds certified coverage to the exact existing frontier.
Its initial region differs from the region visited by either
original 511-node pilot. No cyclic continuation of this same
frontier was run as a control. Therefore neither the number of new
leaves nor the added volume establishes a speedup over cyclic
splitting. Most of this weak face, every other unfinished face,
and the universal half-row assertion remain unresolved.

## Exact audit and provenance

The final structural audit checked:

- Byte-equivalent original tree prefix and its rational witnesses.
- Every stored arbitrary split axis and reconstructed rational box.
- Exact equality between the reconstructed and saved frontiers.
- Accepted plus pending volume exactly one.
- New split-policy counts and the exact volume increment.

The root agent checked all 32 current bindings. The subsequent
structural audit repeated no numerical root or source evaluation.

Result SHA256:
4061218279b8792578c8f89959ba75a16c088f77ab1b67531e7d0835faf9014a.

Proof:
[research_mixed_half_row_adaptive_continuation.md](../../../notes/research_mixed_half_row_adaptive_continuation.md),
SHA256 4b96b1ee38ee07ba13c2db238a53e3feaca40bef9786d174c18a37b2168e5625.

Driver:
[continue_mixed_optimized_half_row_pilot.py](../../../experiments/continue_mixed_optimized_half_row_pilot.py),
SHA256 f3bef62b9adbe1ba39e1204b185c1086737a0cea66d8cba2e50ef8b1e6e429fb.

The prior proofs, checkers and partial records remain unchanged.
