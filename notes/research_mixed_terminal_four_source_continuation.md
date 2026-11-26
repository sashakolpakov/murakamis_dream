# Continuing the type-four comparisons on the actual input domain

Research certificate design, 5 November 2026. This note changes only
the auxiliary type-four reference domain and preserves every accepted
node of the first attempt. No continuation has been executed. All
twenty-one uniform signs remain conditional until a complete author
record and independent saved replay pass.

The new driver is
[continue_mixed_terminal_four_source.py](../experiments/continue_mixed_terminal_four_source.py).
The original [proof](research_mixed_terminal_four_source_certificate.md),
[driver](../experiments/certify_mixed_terminal_four_source.py), and
[partial record](../repro/results/research-mixed-terminal-four-source-attempt01.json)
remain unchanged. In particular this note does not replace an
unproved sign by a new root or a sampled exclusion.

## 1. The compact domain used by actual open words

Keep the full original type-three disk. For a type-four incoming
reference use
\[
 K_4=\{|a-(.30-.052i)|\le.060\}
                 \cap\{-.108\le\Im a\le-.001\}.
 \tag{1}
\]
Every nonprivate original open leg lies in its reduced disk by
[local factor coverage, Section 1](research_mixed_open_local_factor_coverage.md).
For ordinary type-four legs the full-map height bounds are
\(-.102<\Im a<-.001\), from
[the ordinary height theorem](research_mixed_cyclic_critical_height_bounds.md).
For attached type-four endpoint legs the exact
[endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md)
give \(-.108<\Im a<-.020\).
Thus (1) contains every actual type-four terminal input at length
\(m\ge2\), including the opposite attached endpoint when \(m=2\).
No statement about a private endpoint input or the one-vertex source
is made.

The original disk coordinates are
\(a=.30-.052i+.064(x+iy)\). In these coordinates (1) is
\[
       x^2+y^2\le(15/16)^2,
       \qquad -7/8\le y\le51/64.
 \tag{2}
\]
For any rational parameter rectangle, first intersect its real
coordinate with \([-15/16,15/16]\) and its imaginary coordinate
with \([-7/8,51/64]\). An empty intersection is excluded.
Otherwise exclude it only when the exact minimum of \(x^2+y^2\)
over the clipped rectangle is **strictly** greater than
\((15/16)^2\). Every boundary contact is retained. An accepted
source bound is proved on the entire clipped rectangle; it need not
describe the circular intersection exactly. The normalized reference
parameter and physical derivative radii are evaluated on this same
clipped rectangle.

For type three, the old original-disk test and all arithmetic are
unchanged. These rules are sufficient for coverage of the actual
reference set and make no assertion that every retained auxiliary
point is geometrically realized.

## 2. What the first attempt established and what is imported

The pinned partial author record has SHA256
`8bd75d7cfc1a5dad99579cb48e69aef5ced000ce505687aae805ec24183b041e`.
It ended at its prescribed depth limit with no arithmetic error:

* 36,752 complete job trees;
* a 2,566-node prefix of job 36,752 and its five pending boxes;
* 93,994 committed nodes in total, with a separate count for the
  final attempted but uncommitted trial.

The unresolved box belongs to the flattened private face \(e=.27\)
at inherited root cell 1,750. In normalized coordinates it is
\[
 [-479/1024,-15327/32768]\times
 [-7099/8192,-14197/16384].
 \tag{3}
\]
Its minimum squared distance from the disk center exceeds
\((15/16)^2\) by exactly
\(97417765/1073741824>0\). This excludes that entire box
from (1), rather than just its midpoint. Its failed enclosure in the
larger original disk was a failure to meet the chosen margin, not a
proved positive deficit or a counterexample to the actual source.

Every existing node, split axis, target trial and completed tree is
copied unchanged. The active tree prefix and five-box frontier are
also copied exactly. Only the diagnostic failed-trial entry may be
removed: that trial was never committed to the tree. The original
40,131 jobs remain, with their original order and 1,911 inherited
own-four root witnesses. There is no new root proposal.

An imported leaf keeps the **original** lower-height-mask acceptance
rule, even if the leaf lies outside (1). This is a stronger valid
bound wherever it overlaps (1), and final replay must check its
original arithmetic. No newly narrowed interval is substituted into
an old accepted calculation.

## 3. Unchanged source acceptance on the appended nodes

The entire target inventory, original logarithmic phase, canonical
inner branch, reference response, and target optimization rule are
those of the first-stage certificate. In particular
\[
       \kappa=1/2500000,\qquad \mu=3/100,
       \qquad \text{accepted deficit}<-1/20000.
 \tag{4}
\]
The eight reduced faces, twelve reduced alias families and raw
half-transform face retain their original fixed penalties and
retained-height flags. All free target variables are controlled by
the same strict-concavity gain; no target grid is used.

For a new nonexcluded rectangle, the driver calls the original
`check_face` helper with the clipped rectangle from Section 1.
That rectangle already satisfies the original weaker lower-height
mask, so the helper leaves it unchanged. Its midpoint, whole-cell
implicit responses, halfwidths, original value and target gain all
refer to that same rectangle. There is no arithmetic change inside
the acceptance helper. The original whole-cell root witness remains
the source of existence and branch identification.

An unsuccessful source test may select a split axis by the original
two reference-derivative contributions. This decision affects only
efficiency. Both exact children are retained in the stored tree and
their union is the unsplit rectangle. An inherited-root or arithmetic
failure stops with the uncommitted box still pending.

## 4. Immutable prefixes, exact coverage and complete saved replay

The pinned first-stage record determines the acceptance rule at every
job/node position. Nodes inside its exact tree prefixes use
`original_mask_fixed_trial_v1`; appended nodes use
`actual_k4_fixed_trial_v1`. The output declares both rules. A rule
is never chosen from the outcome of a new interval calculation.

For each job, reconstruct a right-first stack from its original
inherited rectangle. Each stored split consumes one box and adds
both exact children in their recorded order. A stored exclusion
must pass its declared exact exclusion rule. A stored leaf must
have a valid saved target trial and pass its declared source rule
during replay. A complete tree exhausts its stack; an active prefix
must reconstruct exactly the saved pending stack, including depths.
This verifies full coverage for arbitrary recorded split axes.

A resume uses a distinct immutable input record and a new output
path. Every previously completed tree must remain identical, and
the previous active tree must remain an exact prefix of its resumed
tree. The input hash, the pinned first-stage hash, all original
source/root bindings and the new compact-domain extraction are
checked at publication. Accepted work is never searched again on
resume. In particular the continuation does not replace the already
completed 36,752 jobs by fresh proposals.

Each author attempt has at most 600,000 **additional committed**
nodes and 600 seconds of numerical continuation, with the depth cap
recorded separately. The attempted-node count may exceed committed
nodes by the unfinished trial. A box remains on the frontier until
its terminal node or exact split is committed. The alarm is blocked
during commits and atomic file replacement. Deadline, depth or
arithmetic stops therefore retain a complete frontier.

Saved replay has no author time alarm. It prohibits both complex-root
and target proposals, rechecks **every** imported and appended leaf
with its stored rational trial, and performs no subdivision. Legacy
leaves are replayed on their original mask even when outside (1).
Every original witness is revalidated before its source checks.
Only a complete 40,131-job author followed by this saved replay
establishes all twenty-one signs on \(D_3\times P\) and
\(K_4\times P\), with each family's additional free target
coordinates understood. A complete conclusion would discharge
Condition C of [the whole-terminal assembly](research_mixed_terminal_four_full_completion.md),
not the global open-word source theorem.

Example bounded author and complete saved replay commands, to be used
only after the proof and driver reviews:

```sh
.venv/bin/python experiments/continue_mixed_terminal_four_source.py --precision 256 --output repro/results/research-mixed-terminal-four-source-stage2-attempt01.json
.venv/bin/python experiments/continue_mixed_terminal_four_source.py --precision 320 --input repro/results/research-mixed-terminal-four-source-stage2-attempt01.json --output repro/results/research-mixed-terminal-four-source-replay.json
```

If an attempt is incomplete, a later reviewed continuation uses
`--resume` with that immutable input and a fresh output filename.
An incomplete record cannot be passed to complete saved replay.
