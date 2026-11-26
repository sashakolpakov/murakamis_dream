# Two prescribed canonical-prefix central budgets

Research evaluation specification, 6 November 2026. The
[saved canonical reference record](../repro/results/research-mixed-second-selected-canonical-reference.json)
already localizes the two original canonical prefixes with
\(\alpha=1\), \(\beta=0,1\), and fixed external coordinate
\(c=1/3\). This specification authorizes no execution by itself.
It specifies only the [separate budget driver](../experiments/evaluate_mixed_second_selected_canonical_budgets.py).

## 1. Certified references and outward reconstruction

Verify the exact canonical-record hash and all its 29 frozen inputs.
Its [residual-localization proof](research_mixed_prefix_residual_localization.md)
combines original canonical existence with the original strongly
accretive Hessian. Thus the saved coordinate rectangles contain
the actual canonical solutions with their original logarithmic lifts.
This existence conclusion is an input here; neither the residual nor
the proposed numerical centers are reevaluated.

Read only the saved coordinate enclosures for
\((e,\xi,a,u,z,v,b,c)\), preserving their exact rational endpoints.
At 256-bit precision construct outward real and imaginary intervals
and explicitly verify that each contains its saved rational interval.
For the seven negative-sign leg coordinates form
\[
 X_w=\exp(-2\pi i w),\qquad w\in\{e,a,u,z,v,b,c\},
 \tag{1}
\]
using the outward coordinate rectangles and outward \(\pi\).
The auxiliary \(\xi\) is retained as a coordinate only; no auxiliary
rational map or positive-sign parameter shape is needed. The exact
external input stays \(1/3\), even though its arithmetic enclosure
has outward rounding.

These separate rectangles and their exponential images contain one
common original canonical reference in each beta case. Losing
correlation enlarges the enclosures and does not replace that common
reference by independently selected points. No midpoint proposal,
root solve, rational transport, logarithmic decoding or source
evaluation is performed.

## 2. Exactly one reviewed wrapper call per prescribed case

Bind the frozen original evaluator, call its metadata-only
`verified_inputs` routine before importing its primitive provider,
and verify every returned dependency. Also bind the
[curvature wrapper and its specification](research_mixed_second_selected_curvature_evaluation.md)
and its four pinned proof/helper inputs before importing it.

For each beta, initialize the reviewed original centered primitive
without its unrelated private-cut construction. Pass the existing
outward coordinates and negative-sign shapes directly to
`improved.evaluate_reference`, exactly once. It calls the frozen
directional helper once and then applies its reviewed exact-rational
upper-bound improvements. Its original and improved results are both
preserved in full, including any incomplete branch calculation.

The phase height is \(H=1/100\). The original branch domains remain
the factorial plateau \([.22,.45]\) and forced interval \([.4,.45]\).
The original boundary tangents, chirp, true centers and signed forced
gain remain those of the [directional theorem](research_mixed_second_selected_directional_budget.md).
The optional local curvature candidates are selected only by the
wrapper's existing rational guards. No additional trial, target
optimization or replacement bound is introduced.

Per case, permit at most two branch attempts, three frozen node
conjugates and twelve centered primitive calls; the wrapper adds no
primitive, conjugate or reference call. The direct reconstruction
uses exactly sixteen real intervals and seven negative-shape
exponentials per completed case. Old source/reference/`inspect`/`main`
entry points, transfer maps, root solvers and finite quantum sums
remain forbidden.

## 3. Fixed stopping, output and scope

Evaluate the prescribed beta-zero case and then the prescribed
beta-one case. Stop after both, independently of the signs or success
of either result. Arithmetic failure is recorded and does not trigger
refinement, a repeated call, a higher precision or another external
input. An unexpected per-case failure preserves its partial input and
count records and proceeds only to the other prescribed case.

The fresh output stores the source case hashes, exact saved inputs,
outward reconstructed coordinates and all seven shape enclosures,
both complete result objects, directed endpoints and call counts.
All dependencies are verified again before writing. Preserve the
original canonical record and every earlier diagnostic unchanged.

Each successful scalar bound concerns the central main/main phase
at its prescribed genuine canonical prefix. The existence theorem
does not establish that \(c=1/3\) is realized by any finite suffix.
This diagnostic gives no parameter-cover, half-row, finite-source,
uniform second-selection or global filling-volume theorem.
