# Pending-frontier continuation with exact disk exclusions

Research specification for the [new driver](../experiments/continue_mixed_second_selected_geometry_frontier_probe.py),
6 November 2026. This starts only from the 349
unvisited beta-specific leaves of the
[frozen first scalar probe](../repro/results/research-mixed-second-selected-pending-scalar-probe-attempt01.json).
It preserves every earlier exclusion and adds the independently
proved [saved-cell exclusion](research_mixed_second_selected_saved_cell_geometric_exclusion.md)
of the probe's last visited cell. The earlier files and statuses are
not modified. No run is authorized merely by this specification.

## 1. Exact initial partition and bounded traversal

The earlier first-pass exclusions number 3203 for beta zero and 3170
for beta one. The frozen probe then excluded 131 and 47 further leaves.
Its remaining visited terminal leaf, node 288 with beta zero, is
geometrically excluded by the saved-cell proof. Consequently the fixed
exclusions now number 3335 and 3217, respectively. The unvisited
frontier has 143 beta-zero and 206 beta-one leaves, of respective masses
\(6605/2097152\) and \(285/65536\).

Verify the prior records and all transitive input hashes, the saved
exclusion's source-node hash, the fixed-exclusion inventory, and the
prefix-free unit-mass partition for each beta before evaluation.
Reconstruct every box from its exact dyadic address. None of these
349 leaves has previously been evaluated for its beta.

Use the saved stack order, whose last item is next. This resumes the
same deterministic depth-first forest traversal. Evaluate each initial
pending leaf itself; do not split it in advance. A new arithmetic-
inconclusive node may be split by the original alternating-coordinate
rule, left child before right child. The cap is 2000 new beta-specific
reference visits, with maximum address depth 28 and precision 160 bits.
No previously visited node, alternate starting point, additional box,
or precision retry is permitted.

## 2. Full-box rational arithmetic and exact geometric filters

Keep the frozen shifted rational arithmetic, Cartesian denominator
guards, optional direct-only fallback, original logarithmic lifts,
regularity checks, and necessary source rectangles. Also retain the
reviewed pre-log [negative-shape half-plane test](research_mixed_reference_shape_half_plane.md).
It excludes only a negative-sign leg shape whose full-map imaginary
lower endpoint is strictly greater than \(-3/20\).

Add an exact rectangle-to-disk test after each finite coordinate is
decoded and before any coordinate intersection. For a full rectangle
\([x_-,x_+]+i[y_-,y_+]\) and disk center \(a+ib\), radius \(r\),
use the proved inequality
\[
 \max(0,x_--a,a-x_+)^2+\max(0,y_--b,b-y_+)^2>r^2.
 \tag{1}
\]
All endpoints and comparisons in (1) use exact fractions. A strict
inequality is a necessary exclusion; equality is retained. Save the
full decoded rectangle, center, radius, component distances and exact
squared excess. These calculations neither alter the rational maps
nor feed clipped values into their derivative enclosures.

The source allocations from the
[reference theorem](research_mixed_second_selected_reference_curve.md)
are:

| Coordinate | Necessary disk |
| --- | --- |
| Attached \(a\), ordinary \(u,z\) | \(P_4\), center \(.30-.052i\), radius \(.060\) |
| Ordinary \(v,b\) | \(P_{3+\beta}\) |
| External \(c\) | \(K_3\cup K_4\), with the corresponding \(P_3,P_4\) disks |

Here \(P_3\) has center \(.35-.01i\), radius \(.083\).
No disk test is imposed on the private endpoint \(e\) or the
positive-sign auxiliary \(W\).
There are at most seven exact disk tests and seven pre-log sector
tests per beta-specific node; the frozen rational-arithmetic caps
are unchanged.

For external \(c\), test each typed alternative separately: its disk,
its original height interval, and for \(K_3\) the original oblique
restriction \(\Re c-3\Im c\le.608\). Exclude the cell only if both
alternatives fail. Intersect the surviving types with the inherited
provider's alternatives, which also retain the typed internal
\(v+b\) sum. If that intersection is empty, exclude before calling
the original regularity check. Otherwise retain exactly the surviving
types and perform every original regularity check as before.

These are necessary-reference exclusions, raised distinctly from
arithmetic inconclusiveness. A retained box remains a necessary
superset; it is not a proof of word realization or nonempty geometry.

## 3. Unchanged scalar formulas and mandatory stopping

Only a reference retained after the strengthened geometry may call
the frozen [directional scalar evaluator](../experiments/evaluate_mixed_second_selected_directional_budget.py).
Reuse its existing shapes and coordinate enclosures without a second
reference evaluation. The generic scalar formulas remain unchanged;
the optional local-curvature estimates are not used in this run.

As in the earlier probe, permit at most one helper call, two branch
attempts, three node conjugates and twelve centered primitive calls
per retained node. Original source roots, finite quantum sums, old
`inspect`, old reference entry points and old `main` routines remain
forbidden. No edge conjugate or flow optimization is added.

Stop the whole continuation at the first helper result containing
finite rational endpoints for **both** Fourier branch budgets,
regardless of their signs or reported helper status. A fully evaluated
positive upper budget never triggers subdivision. If arithmetic fails
before both branch budgets are finite, preserve the partial result and
allow subdivision only within the same visit and depth caps.

## 4. Preserved coverage and compact output

At every stopping reason, each beta's fixed exclusions, new terminal
leaves, unvisited frontier and unresolved depth-limit leaves are
prefix-free and have total mass one. The scalar-evaluated leaf stays
in this partition independently of its budget signs. An unexpected
exception records the affected leaf or its already-created children
as unresolved and preserves the remaining stack.

Store only the new nodes, their shared transport and exact geometric
witnesses, the initial and final frontier, the unchanged-exclusion
hashes, and the prior-record provenance. Identical transport records
may be merged by address; differing records are retained under distinct
digest-qualified identifiers. The 103 MB first-pass record and the
40 MB earlier probe are not copied into the new output. All frozen
bindings are checked again before writing, and progress is printed
every 20 new visits.

No execution, automatic follow-up, half-row conclusion, uniform
second-selection gap, or global filling-volume theorem follows from
this specification alone.
