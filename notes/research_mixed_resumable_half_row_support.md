# Resumable certification of the ordinary half-row comparison

Research implementation design, 5 November 2026. The new driver
[certify_mixed_resumable_half_row_support.py](../experiments/certify_mixed_resumable_half_row_support.py)
continues the universal twelve-face comparison. It preserves
accepted work across bounded attempts and uses the
[validated adaptive splitting rule](research_mixed_half_row_adaptive_continuation.md).
No author run or completed universal inequality is asserted here.

## 1. The same twelve-face theorem and acceptance rules

The mathematical assertion is exactly that of the
[original half-row design](research_mixed_half_row_support.md):
for both own flags, all three unordered external type pairs,
both ordinary boundary slots, both conditional orientations,
and every real target \(X\in[.22,.45]^2\),
\[
 \begin{split}
 D(Z,X)={}&\Re F(1/2;X+i\Im Z)-\Re\phi(Z)\\
          &-\Re\phi'(Z)\cdot(X-\Re Z)
                  +\frac{\|X-\Re Z\|^2}{2500000}
                       <-\frac1{2000}.
 \end{split}
 \tag{1}
\]
The original primitive, log lifts, chirp, own denominator power
and two halfweights are unchanged. The full auxiliary matched-gap
and ordinary-boundary arguments are those of that design; the
smaller actual-height theorem is not substituted on a larger
auxiliary domain.

The two acceptance labels remain explicit:

- “fixed_trial_v1” invokes the unchanged original checker.
- “optimized_envelope_v1” invokes the
  [optimized method](research_mixed_half_row_optimized_envelope.md):
  curvature \(c=14/5-2/2500000\), midpoint-only target gains,
  whole-cell optimizer boxes, and the correlated envelope gradient.

The [mixed-rule design](research_mixed_optimized_half_row_support.md)
already proves why each label implies (1). Neither resuming nor
changing the split axis changes a leaf's inequality.

## 2. Two immutable seeds

The fixed-rule seed is the sole complete face
\((\epsilon,\alpha,\beta,\mathrm{face})=(0,0,0,0)\) in
[the original partial record](../repro/results/research-mixed-half-row-support-partial.json):
96,199 leaves, with record SHA256
f326bde32741e73dee5b9f8475d31b897d16569cdc002d970f4cfa49219f0686.
Its complete tree is referenced by that immutable file rather than
copied into every checkpoint. The unfinished opposite face in the
old partial record is not imported.

The optimized seed is case \((0,1,1,0)\) in
[the adaptive continuation record](../repro/diagnostics/2026-11-05-adaptive-half-row-continuation/result-partial.json),
SHA256
4061218279b8792578c8f89959ba75a16c088f77ab1b67531e7d0835faf9014a.
Its exact 1,022-node prefix contains 505 accepted leaves and thirteen
pending boxes; resolved volume is \(37/8192\). All those nodes and
the frontier are imported unchanged. Its first 511 nodes retain
their old cyclic axes; subsequent axes are read from the record.

The seeds and their complete dependency chains are hash-bound.
Author mode reconstructs their coverage but does not repeat old
root proposals or numerical leaf checks. Their accepted work was
checked in the original runs. The final complete saved replay
independently revalidates every seed leaf as well as every new leaf.

## 3. Independent domains and exact exchanged faces

The record always has twelve domains in the original order
\[
 \epsilon\in\{0,1\},\quad
 (\alpha,\beta)\in\{(0,0),(0,1),(1,1)\},\quad
 \mathrm{face}\in\{0,1\}.
 \tag{2}
\]
Each domain is one of:

- The pinned complete fixed-rule domain.
- An independent optimized domain with an exact tree prefix and
  its pending frontier.
- An exact exchanged face referring to its earlier equal-type
  independent or pinned face-zero domain.

The exact exchange
\[
 (s,t,A,C)\mapsto(t,s,C,A),\qquad
 \mathrm{center}\mapsto S\mathrm{center},\quad
 Y\mapsto SYS,\quad D_{\rm affine}\mapsto SD_{\rm affine}S
 \tag{3}
\]
uses the same \(2\times2\) permutation \(S\) as the mixed-rule
proof. Remainder-radius slots and target-orientation slots also
exchange; target coordinates within a pair do not.
The parameter labels are unchanged, so all recorded split axes
transport literally.

An exchanged face is marked complete only after its earlier
source face is complete. There is no numerical transport search,
no partial author transport cursor, and no chain of exchanged
references. Both unequal-type boundary slots are independent.
The fixed seed and its opposite retain the fixed-trial rule;
other domains use the optimized rule.

Author mode processes the first unfinished independent domain in
(2). Thus this is a universal continuation, not another isolated
weak-face pilot. The weak seed remains available when its turn
is reached.

## 4. Exact coverage under adaptive continuation

At a finite source-bound failure, both conditional orientations
are evaluated before choosing the split. The adaptive score is
\[
 E_j=\max_{\text{failed orientations }s}
                  h_j\sup|\mathcal G_{s,j}|,
 \tag{4}
\]
using the already validated optimized-envelope derivative and
the actual parameter halfwidth. Choose the largest outward score
with a fixed tie convention. Root-enclosure or nonfinite-source
failures use the old cyclic-axis fallback. The chosen axis is
stored; its heuristic is never an acceptance premise.

For any recorded axis \(j\), exact rational midpoint children
partition their parent and each have half its volume. Therefore
arbitrary stored axes preserve
\[
 \sum_{\text{accepted leaves}}2^{-\mathrm{depth}}
       +\sum_{\text{pending boxes}}2^{-\mathrm{depth}}=1
 \tag{5}
\]
on every independent face. The driver reconstructs the complete
tree prefix and requires exact equality with the stored frontier,
not merely agreement of counts or volumes.

On resume, each prior tree is an immutable prefix. Previously
complete independent trees cannot change at all. Final verification
rereads the previous input file and compares prefixes against that
fresh data, rather than comparing aliased mutable Python lists.
The weak seed is likewise reread and compared. New proposals occur
only on a currently pending box.

## 5. Bounded attempts and atomic checkpoints

One author invocation permits at most 600,000 additional attempted
nodes, 600 seconds including setup, and depth 45. Smaller limits
may be specified; the driver cannot increase these maxima.
Imported structural checks and exact logical exchanges make no
new root proposals. A node above the requested gap or a depth
limit stops with its unresolved box retained and a distinct status.
It does not automatically resume or broaden the claim.

During numerical work the active box remains on the frontier.
An acceptance or split is committed as one signal-protected
transaction: remove that box, append its leaf or split, insert
children if needed, and update counts. Thus an interruption before
commit leaves the entire box pending; an interruption after commit
sees the completed update. Attempted nodes and committed nodes are
reported separately and can differ by at most one.

The driver publishes an initial checkpoint, periodic checkpoints
and a final checkpoint. Publication writes a temporary file in the
same directory, flushes it, atomically replaces only the current
attempt's output, and flushes the directory. A reader sees either
the previous complete checkpoint or the new complete checkpoint.
Publication and structural commits mask the handled signals.
Every published tree/frontier state satisfies the same invariant.

A resume input is kept unchanged. The next attempt must use a
distinct, initially nonexistent output path. Its dependencies
include the previous checkpoint and all previous dependencies,
so the provenance hash remains meaningful. Periodic publication
updates only the newly created output of the current attempt.
Full reconstruction and all bindings are checked at startup and
before final publication; the final record marks that verification.

The time limit stops new mathematical work. Final validation and
serialization preserve the result without beginning another
attempt. There is no automatic retry. A partial checkpoint remains
incomplete regardless of how many leaves it contains.

## 6. Complete saved replay

A complete author record can be supplied with the replay option
at precision at least 320. All twelve domains must already be
complete. The replay:

1. Reconstructs every exact tree and verifies every acceptance-rule
   label, source pointer and immutable seed.
2. Follows each stored axis and each saved rational target trial.
3. Revalidates every original root enclosure, midpoint log lift,
   correlated response and source inequality under that leaf's
   fixed or optimized rule.
4. Numerically revalidates every exchanged leaf after the exact
   transformation (3), including the opposite of the fixed seed.

Root proposals, floating target proposals and the floating
two-leg solver are replaced by guards that fail if called.
No subdivision or new heuristic choice is made during replay.
Decimal display bounds may change; the domains, trees, rational
witnesses, targets and acceptance rules do not.

An interrupted replay is labeled incomplete and records its current
case/cursor. It cannot become a complete author record or a passed
replay. Replay is not an author continuation and does not spend a
new search budget. The 600-second and additional-node caps apply
only to author attempts; the saved replay has no time alarm and
may take longer without proposing or refining any cell.
Only a fully completed saved replay validates
the whole imported and newly built certificate at the higher
precision.

Completing this certificate would establish (1) on its ordinary
reference family. It would not prove the separate last-row,
terminal-graph or full ordinary-source comparisons, nor the
arbitrary short-filling and branching conclusions.
