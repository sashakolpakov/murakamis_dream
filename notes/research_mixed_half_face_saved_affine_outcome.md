# Outcome of the fixed saved-data half-face comparison

Record, 7 November 2026. The sole prescribed saved-data calculation
completed its entire inventory. Its conservative certificates do not
prove the half-face affine comparison on both full following disks.
This is an inconclusive comparison, not a failure of the underlying
finite source or its actual critical-action inequality.

## 1. Frozen calculation and complete recorded outcome

The calculation is specified by
[the analytic protocol](research_mixed_half_face_saved_affine_protocol.md)
and implemented by
[the fixed checker](../experiments/check_mixed_half_face_saved_affine.py).
The sole output is
[saved-affine-attempt01](../repro/results/research-mixed-half-face-saved-affine-attempt01.json),
SHA256
533f8dd9663b920b541c2f7e3252d12153fb6d16dfe726c615da9d63148092c2.
Its [manifest](../repro/protocols/research-mixed-half-face-saved-affine.json)
has SHA256
a71b93551de6fb5a8137988cef3cad860cbf3894c5f369babd3ab978c6ba0b04.
The checker, protocol and manifest instructions remain respectively at
the frozen hashes

* 0e21dcd63a282a441e643b40af90934957c43d60dc2e2407e340805f2b08f3e6;
* 4e69ba62e3e1346d25aca7a00e19bd4b5bdc5fcb88972851182a33a97031938d;
* f61017f8456396056e18d9741840b8b3cd5955bef2412206ff10131906695037.

The output status is `completed`, with verdict
`complete_inventory_recorded_affine_test_inconclusive`. The fixed order
is all 512 type-three circle cells followed by all 512 type-four circle
cells. Each cell retains the factorial alternative at both
\(x=11/50,9/20\), followed by the forcing alternative at those same
two endpoints.

| Recorded item | Outcome |
| --- | ---: |
| Attempted and completed cells | 1,024 |
| Passed checks in every cell | 61 |
| Completed comparisons | 4,096 |
| Positive lower certificates | 1,498 |
| Insufficient lower certificates | 2,598 |
| Cells with all four lower certificates positive | 0 |
| Failed cells, blocked comparisons and unprocessed identifiers | 0 |

Both full-circle certificates are recorded as insufficient. The result
retains every midpoint proxy, signed derivative enclosure, cell
transport debit, product bound, circle maximum and its witness, disk
debit, and final lower certificate. No failed or insufficient portion
was excluded from the inventory.

## 2. Provenance and the scope of the audit

A read-only metadata and provenance audit checked all 379 file
bindings, 118 inherited records and 5,507 dependency edges against the
saved manifest and result. The exact cell and comparison inventories,
all recorded checks, response-row and inverse-column associations,
stored certificate signs and verdicts, and the saved circle-witness
references agree. Every bound file and the manifest retained its
recorded hash. The final output lists no changed input or manifest.

The earlier boundary-cover attempt remains `failed` and `inconclusive`,
with its original direct interval-inverse exception preserved. Its
successful inclusions and the separately completed saved-response
record are used exactly as in the protocol; the earlier inverse failure
has not been relabeled.

The new result records 1,024 two-coordinate response enclosures,
1,024 product bounds, 2,048 angular derivative enclosures, 4,096
midpoint proxies and 4,096 final comparisons. All counters for new
roots, inclusions, Hessians, matrix inverses, actions, dilogarithms,
source replays, retries and subdivisions are zero.

The audit used only saved strings, inventories, status fields, file
reads and hashes. It did not import or replay the checker, decode new
interval values, recompute a mathematical bound, or search for a new
extremum. This note reports that audit and the existing output; it
introduces no additional calculation.

## 3. Mathematical interpretation

The protocol's final expression is a conservative lower certificate
for the negative of the true deficit. It substitutes an elementary
lower bound for the unsaved halfweight, then spends the prescribed
cell-transport and full-disk barrier debits. A nonpositive certificate
therefore does not imply that the actual deficit is nonnegative.
Nor does an insufficient certificate identify a failed source estimate
or a counterexample on the canonical geometric image.

The proposed test requires every one of its 4,096 lower certificates
to be strictly positive. That sufficient condition was not obtained.
The previously proved complete half-face cap and conditional
asymptotic expansions, their joint local source, and the phase
transport results are unchanged. This output does not establish the
full half-face affine comparison, the remaining incoming arc, its
vertical join, a complete next Fourier sector, or any new knot family.

No retry, refinement or further evaluation is specified by this
outcome record.
