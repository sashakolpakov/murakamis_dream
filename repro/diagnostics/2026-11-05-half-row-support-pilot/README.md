# Bounded half-row support pilot

This is a partial diagnostic of the new ordinary-reference half-row
acceptance scheme. It is not a complete certificate or a uniform
support theorem.

The design is
[research_mixed_half_row_support.md](../../../notes/research_mixed_half_row_support.md),
implemented by
[certify_mixed_half_row_support.py](../../../experiments/certify_mixed_half_row_support.py).
The complete design has twelve ordinary circle-times-disk faces,
both own types and both conditional orientations. Strict target
concavity covers the whole real plateau square on each accepted cell.

The sole pilot used case `(0,1,1,0)`: own type three, two external
type-four inputs, first input on its circle and the other in its
whole disk. Its command was:

```sh
python3 experiments/certify_mixed_half_row_support.py --precision 256 --pilot --max-nodes 511 --max-seconds 60 --output repro/diagnostics/2026-11-05-half-row-support-pilot/result.json
```

The run stopped at the authorized node cap with process exit code 2
and record status `incomplete`. It visited 511 nodes, accepted 249
leaves, retained 14 pending cells, and completed zero faces. Its
recorded certificate-loop time was about 0.768 seconds. Each accepted
leaf passed the outward `deficit < -1/2000` test in both orientations,
including the quadratic bound for every target. The 68 root-enclosure
and 194 source-bound subdivision events are not counterexamples.
There was no point-gap stop. Nothing is claimed for the pending cells.

The immutable pilot inputs are:

| Item | SHA-256 |
|---|---|
| Proof | `9ef16f20755e45cf88b13e11f8f13c96a1b8caa70540487ce1c97618412e5b95` |
| Script | `1126603ccf44d8240d4ef82f086e034d7209031b1e56a7ab9a5a8a79c5dae490` |
| [Partial record](result-partial.json) | `f53dc6380862fb1c824755732202f002388c49ba5ad6e52c84c10306e77c2591` |

The record binds 25 current dependencies, including the complete
original reduced-disk author and independent replay. The matched gap
at row one half comes from that original theorem's entire right-tail
entropy comparison and its fixed-row subharmonic extension. It does
not use a newer actual-height theorem on the larger auxiliary domain.

The proof and code remain awaiting the separate authorization for any
full author run. This pilot provides no lower bound for a signed
finite sum, no terminal-endpoint graph theorem, and no ordinary-knot
or finite-exception conclusion.
