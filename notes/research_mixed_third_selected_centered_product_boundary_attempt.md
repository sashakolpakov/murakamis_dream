# Centered product-boundary calculation: accepted cells and remaining domain

Research record, 6 November 2026. The single calculation prescribed by
the [centered protocol](research_mixed_third_selected_centered_product_boundary_protocol.md)
stopped at its fixed limit of 2,000 reference cells. It proves the requested
strict comparison on 977 boundary cells, but does **not** complete any of
the 162 product-chart cases. The whole-domain third-selection comparison
therefore remains open.

## 1. Fixed calculation and saved result

The [new driver](../experiments/certify_mixed_third_selected_centered_product_boundary.py)
used the original reference equations and all prescribed target profiles.
The [centered evaluator](research_mixed_third_selected_centered_tangent_evaluation.md)
bounds the original difference of actions on the full certified reference
box, retaining the nonstationary gradient terms away from the true
reference curve. It adds the concave target-support bound and subtracts
the lower endpoint of the required centered boundary correction.
Acceptance requires the resulting upper bound to be strictly less than
\(-1/2000\).

The fixed limits were 256-bit arithmetic, combined binary depth 16,
4,000 visited cells and 2,000 reference cells. The latter count includes
cached references. The run stopped at that reference-cell limit; no
limit was increased and no continuation was performed.

The [terminal record](../repro/results/research-mixed-third-selected-centered-product-boundary-attempt01.json.gz)
has SHA-256
`ef7c37a13f836d0e09a3ad45170e79946b16dd1436cb030816330f5270bed2ba`.
It records:

| Quantity | Count |
|---|---:|
| Visited cells | 2,042 |
| Subdivided parents | 1,023 |
| Accepted terminal cells | 977 |
| Strict geometric exclusions | 42 |
| Pending cells | 166 |
| Depth-limit unresolved cells or errors | 0 |
| Enclosed references | 2,000 |
| Completed profile bounds | 23,892 |
| Inconclusive profile attempts on subdivided parents | 108 |

The maximum reached depth was 13. All 24,000 prescribed profile attempts
were retained, including the inconclusive attempts; acceptance always
requires every profile of that cell to pass.

The exact cache matched eleven of the twenty eligible old references and
132 of their saved target trials. The remaining calls comprised 1,989 new
reference proposals/certificates and 23,868 new target proposals. Every
profile bound used the new centered evaluator. Cached proposal counters
were kept as provenance and were not counted as new calls.

## 2. Exact scope of the covered region

Only case zero was visited. Its flags are
\((\alpha,\beta,\sigma)=(0,0,0)\), and both external coordinates use
the chart `k3_circle_left`. The union of accepted and strictly excluded
terminal descendants compresses to these eight binary prefixes:

```text
00  010  01100  0110100  01101010  0110101100  01101011010  011010110110
```

The five pending prefixes in this case are:

```text
011010110111  011010111  011011  0111  1
```

Their exact normalized parameter masses are
\[
 \text{accepted}=\frac{837}{4096},\qquad
 \text{excluded}=\frac{441}{2048},\qquad
 \text{pending}=\frac{2377}{4096}.
\]
These are binary-chart parameter masses, not geometric boundary lengths,
physical areas or proportions of the family of knots. Each of the other
161 chart cases remains an untouched pending root.

Including the pending cells, all 162 chart domains have exact prefix-free
partitions of mass one. There are 1,185 terminal or pending leaves, and
\[
 2042+166=2\cdot1185-162.
\]
This complete bookkeeping does not assert a completed inequality on the
pending region.

The weakest accepted profile is main/main with factorial alternative
\(\nu=1\), at node 298, address `00100110011`. Its upper bound is
approximately
\[
 -0.0005225951685281931<-\frac1{2000}.
\]
The largest evaluated parent upper bound is approximately
\(2.18223883204734\), also main/main with \(\nu=1\), at node 470,
address `0011`. That cell was subdivided. A positive upper enclosure on
such a parent is neither a proved positive maximum nor a competing
contribution to the original source.

## 3. Saved-data verification and endpoint convention

The [saved-data checker](../experiments/check_mixed_third_selected_centered_product_boundary_record.py)
verifies the raw chart images, strict exclusions, all 162 partitions,
reference residual witnesses, exact cache associations and every finite
profile's derivative, target-support and boundary-correction arithmetic.
All 37 input bindings are unchanged. Its
[compact result](../repro/results/research-mixed-third-selected-centered-product-boundary-saved-audit.json)
has SHA-256
`20ab98fc265aaf08b3ef8c00c58fe2e37fcc0bbfbf6ddb4ceade096528e79ed8`.

An initial saved-data check stopped because separately serialized
interval endpoints can produce a slightly wider rational recombination
than an Arb operation performed before serialization. The
[initial checker](../experiments/check_mixed_third_selected_centered_product_boundary_record_initial.py)
and [failure witness](../repro/results/research-mixed-third-selected-centered-audit-assertion.json)
are preserved. The corrected check does not use a tolerance or replace
containment by overlap. It rebuilds boundary displacements, responses,
all ten mean-value derivatives and target-support slopes by exact rational
interval arithmetic, taking outward hulls with the saved intervals.
It checks the original recorded products separately and then rechecks
every accepted cell with the larger resulting upper bound.

This increases 4,156 profile upper bounds by at most
\(2\cdot10^{-78}\); the largest observed increase is approximately
\(1.45049526291709\cdot10^{-78}\). All 977 accepted cells still satisfy
the original strict threshold. No reference, primitive, optimizer or
source evaluation was repeated by either saved-data check.

## 4. Consequence

The centered formulation certifies substantially more boundary cells
than the previous direct-action attempt and avoids that attempt's first
depth-limit obstruction. The present terminal record nevertheless leaves
five prefixes of the first chart case and all other chart cases pending.
It supplies no whole-domain maximum-principle conclusion, no completed
third-selection finite-product theorem and no new full Kashaev asymptotic
or knot-family result. The earlier completed first-two-selection and
interior-selection theorems retain their stated scopes.
