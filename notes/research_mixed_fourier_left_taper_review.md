# Review record for the fixed left-contour certificate

7 November 2026. The preceding user-facing turn was a progress report;
it did not advance the proof. Work resumed by proving the endpoint
estimate in Lemma 2 and preparing the compact-rectangle certificate.
The finite-exception goal remains open.

## Frozen candidate

| Item | SHA-256 |
|---|---|
| Derivative reduction and endpoint lemma | eb64296ffe3ad8849a3350f1155ca34d30bbc34003ff7a397a513e6b143d5801 |
| Fixed protocol | af9426ee67af62acc8cec618f8dd27c647e0b9fff958b87dc87c4573d9c936c3 |
| Checker | 2f58b3f2a157e84e4a4f9082fd2407ac472c8de70ed0c6a63e44a6b5652c8f7e |

The root review covers the original derivative and its logarithm
branches, endpoint minimization in the retained real coordinate,
exact radial minimization, the direct bound for \(0<x\le1/100\),
and all prescribed interval operations in the checker. In particular,
the clipping function is monotone in both arguments; its rational
endpoint enclosure is valid even when a minimizing radius changes
between an endpoint and an interior value. The checker uses the whole
saved geometric parameter rectangle.

The complete source review also checked the fixed grid coverage,
analytic-call inventory, branch guards, outward dyadic output,
exclusive output creation, pre- and post-execution hashes, and the
failure paths. A static-only inspection matched all 28 prescribed and
inherited file hashes. The checker has not been imported or executed;
its syntax was parsed, and the installed Flint package was located
without importing it. The first static AST inspection did not resolve
named dictionary keys and stopped; a corrected static inspection
completed. Neither inspection called an analytic evaluator.

The endpoint lemma and the earlier reduction have received a separate
full proof review. The endpoint reviewer then read the complete frozen
checker, protocol and inherited source-association chain and found no
correction necessary. This included the whole-box parameter, monotone
clamp enclosure, logarithm branches, complete grid, analytic inventory,
outward recording, exclusive output and failure semantics. The reviewer
performed no execution or analytic evaluation. Both required reviews
are now complete on the exact hashes above. The sole root execution
of this frozen checker is authorized. There have been no preliminary
evaluations or grid probes.

Success will establish the phase comparison only. The finite-source
consequences must retain the half-grid endpoint, contour corrections,
and all original scalar factors in their own written proofs.

## Sole execution and read-only result review

The authorized root execution used session `76020`, which finished
with exit code zero. It must not be run again. All 131072 prescribed
rectangles passed. The complete fixed analytic inventory was recorded,
all 524289 logarithm guards passed, and all 29 source and writer
bindings were unchanged. There were no inconclusive cells or errors.

The result file is
`repro/results/research-mixed-fourier-left-taper.json`, with SHA-256
`55a7c56f33f576c9e6b13b015fd69a448c269ccda82166682675e06d76bcc4c9`.
Its least saved lower endpoint is
\[
                    \frac{5917819973}{274877906944}>\frac1{50}.
\]
The root then inspected every saved cell index and integer interval,
the recorded minimum, analytic counts, and current hashes of all
bound inputs. This read-only check performed no analytic evaluation
and did not import or replay the checker. A separate read-only result
review also checked all 512 ordered rows, all 262144 positive derivative
intervals, the exact minimum, branch and operation counts, zero replay
and adaptation counters, the 29 current bindings, and the original
full parameter enclosure. It found no discrepancy and performed no
analytic recomputation. The finite-source seam proof has already received
both full analytical reviews, with its scalar premise left explicit;
this certificate supplies precisely that premise.
