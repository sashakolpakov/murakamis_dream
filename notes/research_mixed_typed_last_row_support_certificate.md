# Resumable typed last-row support certificate

Research certificate specification, 5 November 2026. The
[height-chart design](research_mixed_typed_last_row_height_charts.md)
gives 72 exact three-parameter charts for the ordinary boundary of the
six typed reference products. This note specifies their common acceptance,
checkpoint, and independent replay rules. It asserts no uncomputed sign.

## 1. Certificate implication and imported chart

Let \(D_{vw}\), the original conditional phase, both allocation flags,
and \(\kappa_0=1/2500000\) be exactly those of the height-chart design,
equations (8)--(13). A **complete accepted record** in the format below
proves
\[
 D_{vw}(Z,X)<0
 \quad\text{for every typed reference in the six products, both
 conditional orientations, all four carriers, and every }
 X\in[11/50,9/20]^2 .
 \tag{1}
\]
Indeed each chart's closed unit cube is covered by its accepted boxes.
Their boundary inequalities give (1) on the full ordinary boundary.
The [interior-reference exclusion lemma](research_mixed_horizontal_tail_reference_boundary.md)
excludes a nonnegative interior maximum: its only possible interior
reference critical point has target equal to reference, where the old
complete matched last-row entropy gap is strictly positive. Compactness
then proves (1). This argument uses all four revived carriers and the
formal original halfweights; it is not a cancellation-only packet argument.

One chart is already complete: own type three, external types \((3,4)\),
boundary \(S_3\) in slot zero, and other-input chart \(D_4^-\).
The [402-cell completion and saved replay](../repro/diagnostics/2026-11-05-typed-last-row-low-cap/completion.md)
have exactly the same parameters and deficit. They prove the stronger
bound \(D_{vw}<-10^{-6}\) on that chart.
The new record imports that immutable tree by its author/replay file
hashes, without any new author proposal or reevaluation there.
A final full saved replay nevertheless revalidates all its original
witnesses and saved rational targets.
For this imported chart, the certifier calls the pinned original
parameter routine itself, including its exact interval expressions and
derivatives. Algebraic equality of alternative chart formulas alone
would not ensure unchanged whole-box enclosures.

## 2. Whole-box acceptance

The external input chart and all its derivatives are the exact
height/width formulas of the design. Every parameter point is admitted;
there are no masks or rejected outside regions. A coarse interval
enclosure may fail a root or deficit test, in which case its entire
parameter box remains pending or is split.
Full-width charts use the correlated centered expression
\(m_n+(2v-1)r_n(h)+ih\) and derivative
\((b-a)\{(2v-1)r_n'(h)+i\}\), rather than separately enclosing their
left endpoint and width.

Each cell uses a rational original-log affine two-leg witness, including
the original midpoint lift, a whole-box self-map, and its validated
coupled response. Own flag \(\epsilon\) is used in both original equations.
Both conditional orientations use the first external flag \(\eta\)
and the own flag for their two allocated halfweights.

Unweighted target coordinates need only their two endpoints. Weighted
coordinates have the strict curvature bound \(1/5\), hence unique clipped
maximizers. A rational trial is saved for every weighted coordinate of
each orientation. The whole-box slope gives the optimizer enclosure
\[
 I\cap[q+5\min(0,\beta^-),\ q+5\max(0,\beta^+)] .
 \tag{2}
\]
The reference derivative of the optimized envelope is evaluated throughout
these enclosures with the original complex Schur Hessian and coupled
response. No optimizer derivative is inserted. At the parameter midpoint
only, add the one-sided \(1/5\)-concavity gain for each weighted coordinate.
The midpoint value, these gains, and the parameter mean-value error give
the full box upper bound.

Acceptance requires strict negativity for every carrier and every
unweighted endpoint choice, in both orientations. The compulsory
envelope counts are \(32,24,16\) for own type three and \(16,12,8\)
for own type four on external types \((3,3),(3,4),(4,4)\).
Only the maximum of these bounds and the count need be stored:
saved replay recomputes the complete deterministic branch inventory.

Floating calculations can propose affine witnesses and rational target
trials only. All accepted inequalities use outward arithmetic.
A certified positive fixed trial stops an author attempt with its
original witness and exact parameter box retained. Such a point would
concern the sufficient typed product; actual-word realization would
remain a separate question.

## 3. Exact pending work and atomic checkpoints

Each nonimported chart starts with its closed unit cube. A stored node is
either a binary split, with its axis, or an accepted leaf carrying its
witness and rational target trials. Following the saved traversal
reconstructs every exact dyadic box and the entire pending frontier.
Closed children include their common boundary; their rational parameter
volumes partition the parent up to that boundary.

A pending box remains on the frontier during a root/source computation.
Only a signal-protected commit removes it and appends either its accepted
leaf or both children. Thus an interrupted computation loses no region.
Every checkpoint reconstructs the complete tree, verifies its frontier,
and verifies
\[
 \operatorname{vol}(\text{accepted boxes})
 +\operatorname{vol}(\text{pending boxes})=1
 \quad\text{on each chart}.
 \tag{3}
\]
The imported chart contributes volume one through its pinned complete tree.

Each author attempt has at most 200000 additional visits and a
300-second working deadline, including setup and checkpoint work.
A depth guard of 60 stops with the exact unresolved box retained.
These are stopping conditions, not acceptance conditions.
At a checkpoint the complete record is written to a temporary file in the
output directory, flushed and synchronized, and atomically renamed.
Signals are blocked only while committing a tree update or publishing
that checkpoint. A pending signal is handled immediately afterward;
the final bounded file publication may finish after the working deadline.

Resume input is immutable and distinct from the new output. The new
attempt validates its complete tree/frontier and preserves every stored
node and accepted witness. It processes only its pending boxes.
Completed charts are skipped; there is no automatic extra sweep.
The attempt history records the input hash, prior node count, and newly
visited nodes. Neither a timed-out checkpoint nor a positive-point record
can be labeled complete.

## 4. Full saved replay

A final saved replay requires a complete author record and precision at
least 320 bits. It follows the exact saved trees, roots, target trials,
chart definitions, and source bindings. Root-proposal and target-proposal
entry points are disabled. It neither subdivides a cell nor changes a
saved rational target. All 72 chart cubes are checked, including the
402 imported witnesses.

A replay is accepted only if all original root/lift tests and all branch
upper bounds pass, and each chart has no pending frontier. Precision
dependent interval strings may change; trees, witnesses, and targets
remain identical. The replay records its input hash and rechecks all
frozen dependencies at the end.

Conclusion (1), if certified, is a last-row supporting-plane comparison
on sufficient typed reference domains. It is not by itself a complete
horizontal source theorem, an actual-word realization statement, or an
open-knot noncancellation theorem.

