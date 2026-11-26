# A bounded pending-frontier continuation to one scalar pair

Research specification, 6 November 2026. This continues the complete
[first reference partition](../repro/results/research-mixed-second-selected-reference-partition-attempt01.json)
without replaying its reference evaluations. Its purpose is to obtain
one fully finite pair of directional central upper bounds from that
systematic partition. No uniform scalar sign or word realization is
presumed.

## 1. Preserved exclusions and the beta-specific frontier

The first pass preserved 2613 inherited exclusions for each beta and
proved 590 additional exclusions for beta zero and 557 for beta one.
Its 88 and 121 inconclusive cases form 209 beta-specific frontier
leaves. Their exact remaining masses are respectively
\(223/65536\) and \(607/131072\) of the original root rectangle.
All earlier exclusions and their provenance remain unchanged.

Before evaluation, verify the prior record, its input bindings, its
complete prefix-free partitions, all candidate box reconstructions,
and these status counts. Each saved inconclusive seed is split once
by the original alternating-coordinate dyadic rule, using its already
proved inconclusive status. No reference evaluator is called on a
seed. The resulting 418 children are the initial computational
frontier; their closed boxes cover exactly the old seed boxes.

Order seeds by binary address, then beta zero before beta one.
Within this ordered forest use deterministic depth-first traversal,
left child before right child. Every new beta/address pair is visited
at most once. The global cap is 2000 new reference nodes, with address
depth at most 28. There are no alternative starting points, precision
changes, source roots or replays of earlier inspections.

## 2. The reference provider and one necessary strengthening

Use the reviewed [staged classifier](research_mixed_second_selected_reference_partition_pass.md)
on each new descendant, at 160 bits. It retains the exact shifted
rational maps, Cartesian nonzero checks, optional direct-only fallback,
staged necessary filters, both suffix alternatives and all original
regularity checks before reference retention. Per-node caches and
arithmetic caps are unchanged, except that a node has one beta case.

The continuation adds exactly one necessary test before logarithmic
decoding. The [shape-sector lemma](research_mixed_reference_shape_half_plane.md)
proves that every required negative-sign shape
\(E,A,U,Z,V,B_\beta,C_\beta\) has imaginary part strictly below
\(-3/20\). After a full-box rational map is enclosed, an imaginary
lower endpoint strictly greater than \(-3/20\) therefore excludes
the whole cell. Save the full shape enclosure, its exact lower endpoint,
and the threshold, and raise a distinct necessary-exclusion exception.
This is not an arithmetic failure. Equality is retained, and the test
never applies to the positive-sign auxiliary shape \(W\). It changes
neither the frozen classifier nor its first-pass records.

A necessary-reference exclusion is terminal and preserved. A
reference-inconclusive node may be split if its depth is below 28.
At depth 28 it remains an unresolved leaf; no larger depth is tried.
Reference retention is a statement about arithmetic and necessary
filters. It does not certify a finite-word realization.

## 3. One reviewed scalar calculation per retained node

For a reference-retained node, pass its existing shapes and pointwise
coordinate enclosures directly to the frozen
[directional scalar helper](../experiments/evaluate_mixed_second_selected_directional_budget.py).
There is no second reference evaluation. Its
[specification](research_mixed_second_selected_directional_evaluation.md)
and [directional theorem](research_mixed_second_selected_directional_budget.md)
retain the exact vertical cost, original chirp and marginals, a common
left gain, the proved right quadratic gain, and the signed selected
gain on the factorial interval \([.22,.45]\) or the forced interval
\([.4,.45]\).

The helper may call the original centered primitive and the frozen
node-conjugate routine. The original scalar `inspect`, source `main`,
old reference implementations, root solvers and finite quantum sums
remain forbidden. The primitive constructor omits the unrelated
private-cut construction. Each retained node gets exactly one helper
call, with at most two branch attempts and three node conjugates.
There is no flow trial or numerical optimizer.

**Stopping rule.** Stop the entire continuation as soon as one helper
call records both factorial and forced budgets with finite rational
directed endpoints. Stop whether their upper bounds are negative,
zero or positive. In particular a fully evaluated positive upper bound
never triggers subdivision or a new test point.

If the helper is arithmetically inconclusive before both branch
budgets are finite, preserve its partial output. Such a node may be
split under the same 2000-visit/depth-28 limits. This is refinement of
an arithmetic enclosure, not optimization driven by a budget sign.
The helper is unchanged; its early failure may leave zero or one
branch record. A successful sign on one branch does not alter the
stopping criterion.

The candidate margin \(1/2000\) is reported by the helper separately
from strict negativity. The present continuation requires neither
that candidate margin nor a negative sign in order to stop.

## 4. Coverage, storage and exceptional stopping

Every split replaces a leaf by its two original dyadic children.
At any stop, each beta's fixed prior exclusions, new terminal leaves,
unvisited frontier and unresolved depth-limit leaves are prefix-free
and have total mass one. A leaf with the fully evaluated scalar pair
remains in that partition regardless of its signs; it is not excluded
from the parameter domain. Save all unvisited and unresolved leaves,
including the beta whose traversal may not yet have begun.

Check these invariants exactly before writing. A visit cap, exhausted
frontier, depth limits, or an unexpected error is recorded explicitly.
An unexpected error preserves the current cell as unresolved and stops
without losing the rest of the frontier. No such stop can be reported
as a uniform scalar proof.

The compact result stores the prior record hash and unchanged exclusion
provenance, the 209 seed hashes and exact initial splits, all new node
outcomes, the final frontier, every partial scalar calculation, and the
first fully evaluated pair if one exists. Identical shared transport
data are stored once per new auxiliary address and referenced by
beta-specific nodes. If two rigorously computed records differ, preserve
both under distinct transport identifiers rather than overwriting either
or aborting the frontier serialization. Large shifted integer arrays
remain omitted as in the first
pass; rigorous polynomial/map endpoints and all required reference
data remain. The record uses compact JSON and does not copy the
103 MB first-pass record.

All frozen inputs are checked before repository imports and again
after completion. Progress is printed every 20 new visits. No
automatic continuation, refinement after a finite scalar pair, or
global filling-volume conclusion is authorized by this specification.
