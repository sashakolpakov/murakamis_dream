# Manifest instructions for the unrun saved-quadratic checker

Preparation instructions, 7 November 2026. These instructions do not
authorize a calculation. The root creates the new manifest only after
the exact protocol, standalone checker, and this guide receive root
and independent full static review. Do not import, compile, execute,
or perform preliminary calculations with the checker.

The fixed paths are:

* Protocol: [research_mixed_half_face_saved_quadratic_protocol.md](research_mixed_half_face_saved_quadratic_protocol.md),
  SHA256 13b6d4cc3c9c76c0cd83fff00acbe430d32d89331af5879ffb175484e4f0f527.
* Checker: [check_mixed_half_face_saved_quadratic.py](../experiments/check_mixed_half_face_saved_quadratic.py).
* New manifest: repro/protocols/research-mixed-half-face-saved-quadratic.json.
* Exclusive output: repro/results/research-mixed-half-face-saved-quadratic-attempt01.json.
* Old result: repro/results/research-mixed-half-face-saved-affine-attempt01.json,
  SHA256 533f8dd9663b920b541c2f7e3252d12153fb6d16dfe726c615da9d63148092c2.
* Old manifest: repro/protocols/research-mixed-half-face-saved-affine.json,
  SHA256 a71b93551de6fb5a8137988cef3cad860cbf3894c5f369babd3ab978c6ba0b04.

Bind this guide. Do not bind notes/research_finite_exceptions_progress.md,
which the checker explicitly rejects, or any mutable progress record, the new
manifest to itself, or the new output. Every old file stays unchanged.

## 1. Prepare the complete binding closure using reads and hashes only

Read the checker as text. Copy its literal PINNED, REQUIRED, CIRCLES,
OLD_TESTS, TESTS and CONSTANTS metadata; do not import its definitions.
Start with every one of the 379 bindings from the old manifest.
Add every REQUIRED path, including the new checker and this guide.
Verify the exact PINNED digests against current bytes.

The added mathematical inputs are the conditional curvature theorem,
the complete real-arc conditional packet and absolute-decrease theorem,
the complete real-arc cap upper bound, and the old outcome record.
Their direct written source inputs are explicitly required too, all
under notes/:

* research_mixed_half_face_general_incoming_transport.md;
* research_mixed_half_face_global_phase_decrease.md;
* research_mixed_next_selected_first_wall_rows.md;
* research_mixed_next_far_half_conditional_aliases.md;
* research_mixed_three_four_next_local_source.md;
* research_mixed_next_coherent_cap_far_arc.md;
* research_mixed_next_wrapped_private_sector.md;
* research_mixed_cap_seam_source_bounds.md;
* research_mixed_three_four_continuous_far_half_cap.md;
* research_mixed_three_four_complementary_real_colors.md.

Bind the exact reviewed bytes of these direct mathematical sources.
This is an explicit proof-input list, not automatic closure of
navigation or historical Markdown links.
The old closure retains the cap ceiling and its saved scalar, the
full cap/conditional/joint source packets, the selected-plateau and
allocated-action sources, the Fourier weights, and all original
root, inclusion, response, and failed inverse records.

For each bound JSON file under repro/results or repro/protocols,
recursively inspect the dictionary-valued fields dependencies,
dependencies_sha256, primary_records, primary_records_sha256,
saved_replays, saved_replays_sha256, and files_sha256. Add and verify
every child binding until closure. Record visited paths and each
parent/field/child/hash edge. A missing file, conflicting inherited
digest, or changed file stops preparation; never repair the binding
by silently replacing its digest.

This preparation uses only file reads, JSON parsing, string equality,
integer inventory counts, and SHA256 hashes. Do not parse any stored
certificate as a number, compute a quadratic value, decode an interval,
recompute a product or disk debit, or reevaluate a mathematical source.
Metadata inspections may confirm the old completed-inconclusive
verdict, ordered inventories, stored labels, and failure records.

## 2. Required manifest fields

The checker validates these fields exactly:

* schema: fixed-saved-half-face-quadratic-v1.
* protocol, checker, manifest_instructions and output: their paths above;
  manifest_instructions is this guide.
* old_result and old_manifest: the two old paths above.
* root_reviewed and peer_reviewed: true only after both complete
  exact-hash static reviews.
* circle_inventory: the exact literal CIRCLES list from the checker.
* cells_per_circle: 512; total_cells: 1024.
* old_comparison_inventory: the exact OLD_TESTS list, in the order
  factorial_left, factorial_right, forcing_left, forcing_right.
* saved_endpoint_count: 4096.
* comparison_inventory: the exact TESTS list: factorial first with
  mu equal to 3575/3072, then forcing with mu equal to 25/24, preserving
  both left_label and right_label fields.
* total_comparisons: 2048.
* constants: delta_left equal to -3/100, delta_right equal to 1/5,
  and height_gain equal to 3/200, all as strings.
* comparison_method: exact_saved_endpoint_chord_clipped_quadratic.
* arithmetic: python_integer_and_fraction_only.
* pinned_inputs_sha256: the complete literal PINNED dictionary.
* files_sha256: the complete verified binding closure.
* review_records: exact-hash root and independent PASS records.

Each valid review record contains reviewer, verdict equal to PASS,
protocol_sha256, checker_sha256, guide_sha256, and
execution_performed equal to false. The root reviewer is /root;
the independent reviewer has a different nonempty name. Include a
short review scope. The checker and guide digests must match the
final entries in files_sha256.

Record preparation date, binding/record/edge inventory and this policy:

Only root may execute the one fixed attempt after inspecting the final
manifest and its hash. No preliminary certificate arithmetic, checker
import, compilation, execution, adaptive constant choice, retry,
subdivision, root/action/dilogarithm evaluation, or source replay was
performed during preparation or review. The old inconclusive result
and all inherited failures remain intact.

Write the manifest exclusively. Compute its final SHA256 and send
that hash to root and the reviewers. Recheck every binding by reading
and hashing, without executing the checker. A changed reviewed file
requires renewed review; it does not authorize a silent update.

## 3. Fixed execution and result semantics

The checker has no adjustable mathematical arguments and no interval
library. It opens the one fixed manifest and creates only attempt01
with exclusive file creation. Root alone runs it after the gate above.

Preflight verifies the old completed-inconclusive verdict, all 1,024
ordered cells, all four labels per cell, the full 61 passed checks per
cell, all 4,096 saved certificates, both old circle records, original
failed inverse status, and the complete frozen provenance. It parses
only exact_final_certificate_lower as a saved mathematical number.
Every string must be a canonical exact rational. It does not parse
the displayed balls or recompute any old numerical quantity.

If preflight succeeds, the checker evaluates exactly two minima per
cell, factorial then forcing. For each it records both old endpoint
strings and verdicts, the exact lower-chord slope, unconstrained and
clipped minimizers, exact minimum, minimizer location, and strict sign.
It applies the fixed gain once and never subtracts the old disk debit
again. No sampled parameter, action, or interval calculation is repeated.

Every insufficient minimum remains a completed comparison.
Success requires all 2,048 strict signs positive. Otherwise a complete
run is inconclusive. Runtime exceptions preserve the per-comparison
failure, attempted and unprocessed inventories, and any other completed
comparisons; no failed item is replaced or retried. Invalid preflight
inputs block all minima and retain the exact error and input bindings.

The output preserves the old status, summary, circle records, operation
counts, original inverse failure, and all 61-check lists. Its new
counters distinguish the 4,096 rational parses, 2,048 minima and 2,048
strict-sign tests from forbidden operations, which must all stay zero.
A final complete file/manifest rehash can only invalidate a result;
it cannot repair it.

Even a successful new result concerns the complete selected real
incoming arc covered by the protocol. It does not pay the remaining
incoming vertical connector or establish a new knot-family theorem.
The old affine calculation remains completed and inconclusive.

These instructions create no manifest and authorize no execution.

