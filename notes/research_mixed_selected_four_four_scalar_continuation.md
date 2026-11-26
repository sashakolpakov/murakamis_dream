# Pending-only continuation of the ten next-four scalar tests

Research certificate specification, 6 November 2026. This permits one
bounded continuation of an incomplete scalar cover. It does not claim
that the remaining partition has been evaluated or completed.

## 1. The immutable prefix and exact remaining domain

The [original ten-test specification](research_mixed_selected_four_four_scalar_cover.md)
and its [wrapper](../experiments/certify_mixed_selected_four_four_scalar_cover.py)
remain unchanged. The sole input to the new continuation is
[attempt01](../repro/results/research-mixed-selected-four-four-scalar-cover-attempt01.json),
SHA256
`07ed9c2f056f1e5ddc133212c5639a49fe63e1bd43a65773a4b9b28715ef5f4a`.
It stopped at its 8,000-visit budget, with no depth-limit failure
or arithmetic error. Its 3,997 terminal leaves consist of 1,454
accepted and 2,543 necessarily excluded leaves. Every accepted
leaf has all six upper endpoints below \(-1/2000\) and
all four corner lower endpoints above zero.

A saved-data check has verified all 14,540 exact rational acceptance
inequalities, all 36 current bindings, the full address-to-box
correspondence, and the prefix-free partition of dyadic mass one.
That check evaluated no reference map, primitive, root, or source.
The seven unresolved boxes are all uninspected. Their addresses,
in the saved stack order from bottom to top, are
\[
 \begin{gathered}
 11,\quad101,\quad10011,\quad1001011,\quad10010101111,\quad
 100101011101,\quad10010101110011.
 \end{gathered}
 \tag{1}
\]
Their exact total dyadic mass is \(6797/16384\).
Their boxes are reconstructed from the original auxiliary rectangle
and alternating real/imaginary binary split, with the lower child
first. The stored boxes and this reconstruction must agree exactly.

The new wrapper copies every terminal entry in attempt01, in its
original order, as the initial leaf prefix. It records the canonical
JSON hash of that prefix and checks exact equality again before
writing the new result. The immutable input record is separately
bound by its full file hash. No accepted or excluded leaf is sent
to any scalar callback. Only boxes descending from the seven roots
in (1) may be evaluated or newly subdivided.

## 2. Unchanged arithmetic and bounded control

The [continuation wrapper](../experiments/resume_mixed_selected_four_four_scalar_cover.py)
imports the original combined inspector and its three frozen scalar
providers only after checking their bytes and every inherited binding.
It calls the original `inspect_combined` without modifying it. Thus
the necessary reference filters, centered original primitive, own-four
phase, outgoing halfweight, clipped gains, and all ten strict
acceptance tests are identical to the first attempt.

This continuation uses 160-bit precision, at most 8,000 additional
visits, and the same absolute depth limit 20. It stops the entire
traversal at the first unresolved depth-20 box or unexpected error.
There is no new target trial, primitive rule, root proposal,
precision escalation, larger domain, or automatic further attempt.
The fixed canonical cut constant may be constructed for the new
provider; no previously accepted cell is reevaluated.

The saved frontier order is preserved. An active box stays on the
stack until an accepted or excluded leaf, or its two exact children,
is committed. Handled interruption signals request a stop after
that commit. At every stop, the new record retains all untouched
pending boxes and any failed active box with its enclosures.
Every new address is checked to have exactly one of (1) as a prefix.
Together with the immutable old leaves, the terminal and pending
addresses must remain prefix-free and have exact dyadic mass one.
Every recorded box is reconstructed from its address.

The output distinguishes cumulative counts from new visits, new
callback calls, new terminal leaves, and new refinements. The original
prefix count and hash, initial pending list, exact remaining mass,
and complete input bindings are retained. The fresh output is
installed atomically without overwriting another record. All bindings
are checked before inspection and afterward; the new proof and
wrapper are bound in addition to the unchanged original inputs.

## 3. Scope of a completed or partial result

The original soundness proof applies verbatim to each new accepted
leaf. If the pending stack becomes empty and all checks pass, the
old and new leaves together cover the complete required reference
domain. This would prove the ten scalar comparisons and hence the
weighted two-factor consequence (8) of the original specification,
with the original outgoing affine term, all ordinary-color jets,
both parities, and all finite rows and currents.

A budget, depth, interruption or error stop instead gives only a
partial result, with its exact residual domain. Such a result does
not establish a uniform finite-source gap. Neither kind of result
would by itself handle every selected or nonplateau open-word
sector, length two, arbitrary short fillings, or global
noncancellation. No completed continuation is asserted here.
