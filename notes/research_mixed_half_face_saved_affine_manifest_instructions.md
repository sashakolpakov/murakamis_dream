# Manifest instructions for the unrun saved-affine checker

Preparation instructions, 7 November 2026. These instructions do not
authorize a numerical run. The root creates the new manifest only after
the protocol and exact final checker bytes have received root and
independent static review. No checker import, compilation, execution,
preliminary margin calculation, or mathematical replay is needed to
prepare that manifest.

The fixed files are:

* Protocol: [research_mixed_half_face_saved_affine_protocol.md](research_mixed_half_face_saved_affine_protocol.md),
  SHA256 4e69ba62e3e1346d25aca7a00e19bd4b5bdc5fcb88972851182a33a97031938d.
* Standalone checker: [check_mixed_half_face_saved_affine.py](../experiments/check_mixed_half_face_saved_affine.py).
* New manifest: repro/protocols/research-mixed-half-face-saved-affine.json.
* Exclusive sole output: repro/results/research-mixed-half-face-saved-affine-attempt01.json.

The manifest must bind this instructions file too. Do not bind the
mutable progress record or the not-yet-created output. Do not place the
new manifest in its own file-hash map.

## 1. Build the binding closure by reads and hashes only

Read the final checker as text; do not import it or evaluate its Python
definitions to obtain metadata. Copy the literal REQUIRED, PINNED,
PRIMARY, CIRCLES and TESTS inventories from its reviewed source.

Start the file-hash map with every REQUIRED entry and every path in
PRIMARY, including the new checker and these instructions. Add every
binding in the old boundary and saved-response manifests. Verify every
PINNED entry against both the current file bytes and the literal digest.
The pinned mathematical sources include the complete cap, complete
conditional and joint packets, the cap-action ceiling, scalar-envelope
proof, and the existing seam scalar replay used by the cap-action proof.
The required list also includes the selected-plateau, allocated-action,
Fourier-weight, exact following-sheet and original Hessian sources.

For every bound JSON file under repro/results or repro/protocols,
recursively inspect the dictionary-valued fields

* dependencies and dependencies_sha256;
* primary_records and primary_records_sha256;
* saved_replays and saved_replays_sha256;
* files_sha256.

Add and verify every child binding. Do not replace a conflicting
inherited digest by the current one. A missing file, conflicting digest,
or changed frozen file stops preparation and must be reported. Continue
until the finite closure is complete. Record the visited record paths
and every parent/field/child edge for static provenance review.

All this work uses only local file reads, JSON parsing, string
comparisons and SHA256 hashing. It must not decode ball displays,
calculate response radii, inspect extrema by new arithmetic, or
evaluate any margin. Both old results and manifests stay unchanged.

## 2. Required manifest fields

The checker validates the following exact fields:

* schema: fixed-saved-half-face-affine-v1.
* protocol, checker, manifest_instructions and output: the four
  corresponding paths above, with manifest_instructions pointing to
  this file.
* root_reviewed and peer_reviewed: true only after the respective
  complete reviews of the final protocol/checker bytes.
* precision_bits: 256.
* circle_inventory: the literal two CIRCLES records from the checker,
  including the center, radius and containing typed radius strings.
* cells_per_circle: 512; total_cells: 1024.
* comparison_inventory: the literal ordered TESTS list from the checker.
* total_comparisons: 4096.
* comparison_method: two_response_affine_disk_barrier.
* nu_method: original_elementary_log_lower_bound.
* catalan_upper: the string 73/500.
* cap_upper: a dictionary with base equal to the string 203/200 and
  subtract equal to the string 1303/7680000.
* point_radius: the string 1/1073741824.
* parameter_radius: the string 1/256.
* pinned_inputs_sha256: the complete literal PINNED dictionary.
* files_sha256: the verified finite binding closure from Section 1.
* review_records: at least one root and one independent exact-hash
  full static review, as detailed below.

Each required review record contains reviewer, verdict equal to PASS,
protocol_sha256 equal to the fixed protocol digest, checker_sha256
equal to the final bound checker digest, and execution_performed equal
to false. The root reviewer is exactly /root. The independent reviewer
is named separately. Also record the review's scope in words.

Recommended audit metadata includes preparation date, complete
dependency-edge inventory, counts of files and inherited records,
the fixed test order, and the following execution policy:

Only the root may execute the sole fixed attempt after inspecting
the final manifest and its digest. No mathematical evaluation,
checker import, compilation, preliminary test, retry, subdivision,
new root/action/dilogarithm, or source replay was performed during
preparation or review. No failure or insufficient comparison can be
removed from the prescribed inventory.

Write the manifest exclusively, then compute its SHA256 from its
completed bytes and send that digest to the root and reviewers.
Recheck the file-hash map without executing the checker. A later
source edit requires renewed review and a newly considered manifest;
it does not authorize silently updating a frozen binding.

## 3. What the future checker records

The new computation has two fixed arithmetic stages in one run.
First it attempts all 1,024 cells and saves their two response bounds,
holomorphic-product bound, two signed angular derivative enclosures,
and four midpoint proxies. Then it takes one exact-rational upper
maximum for each complete circle and applies that circle's fixed
disk debit to all 2,048 comparisons on it.

Any missing or failed cell blocks the entire circle's maximum and
all its final comparisons. The other full circle is still processed.
Nonpositive final lower certificates are retained as insufficient;
they do not become exceptions or claims that the source inequality
is false. A completed inconclusive run still records the full
inventory. Prefix checks, exceptions, blocked and unprocessed
identifiers, input provenance and final input rehashes are preserved.

The successful verdict requires all 4,096 lower certificates positive.
Even then the conclusion is the correlated half-face affine comparison
specified in the protocol. It does not assert control of the remaining
incoming arc, the prescribed vertical join, an entire later Fourier
sector, or a new knot family.

These instructions supply no manifest and no authorization to run.
