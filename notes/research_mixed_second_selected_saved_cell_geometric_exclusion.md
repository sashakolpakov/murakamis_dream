# Exact saved-coordinate exclusion of the first finite scalar cell

Research deduction, 6 November 2026. This checks only serialized
rational endpoints from node 288 of the
[bounded pending-frontier probe](../repro/results/research-mixed-second-selected-pending-scalar-probe-attempt01.json).
No reference map, logarithm, primitive, scalar gain, or source is
reevaluated. The probe and its original statuses remain unchanged.

The prescribed cell has first flag \(\alpha=1\), next flag
\(\beta=0\), and auxiliary address
`0011111110111111100101`. The probe stopped there at the first
fully evaluated pair of scalar bounds. Those original interval upper
bounds were positive. Subsequent proposed elementary replacements
are unnecessary for this cell: it contains no required original
reference.

## 1. The necessary geometric condition

The [original reference theorem](research_mixed_second_selected_reference_curve.md),
Section 2, requires the final external coordinate to lie in
\[
 \begin{split}
 K_3&\subseteq\{w:|w-(7/20-i/100)|\le83/1000\},\\
 K_4&\subseteq\{w:\Im w\le-1/1000\},\qquad c\in K_3\cup K_4.
 \end{split}
 \tag{1}
\]
These domains include the terminal attachment case at length four.
They are necessary for every actual prefix in the cell, without
asserting that any point of the enclosing rectangle realizes a word.

For a rectangle \([x_-,x_+]+i[y_-,y_+]\) and a disk centered at
\(a+ib\), set
\[
 d_x=\max(0,x_--a,a-x_+),\qquad
 d_y=\max(0,y_--b,b-y_+).
 \tag{2}
\]
Every point of the rectangle has squared distance at least
\(d_x^2+d_y^2\) from the center. Thus a strict rational inequality
\(d_x^2+d_y^2>r^2\) excludes the closed disk of radius \(r\).
No complex-ball modulus or square root is needed.

## 2. The saved rectangle and exact separation

The probe's full decoded enclosure for \(c\), before any necessary
coordinate intersection, is
\[
 [x_-,x_+]=\left[\frac{1050214639}{4294967296},
                      \frac{1331525037}{4294967296}\right],\qquad
 [y_-,y_+]=\left[\frac{555453115}{8589934592},
                      \frac{1092931997}{8589934592}\right].
 \tag{3}
\]
At the type-three disk center in (1), formula (2) gives
\[
 d_x=\frac{858567583}{21474836480},\qquad
 d_y=\frac{16033811523}{214748364800},
 \qquad
 d_x^2+d_y^2-(83/1000)^2
 =\frac{327447290086775393061}{1152921504606846976000000}>0.
 \tag{4}
\]
This excludes \(K_3\). Also \(y_->-1/1000\), excluding \(K_4\).
Equation (1) therefore excludes every required original reference
throughout this auxiliary cell.

The earlier modulus-ball disk test did not detect this separation.
That was an inconclusive necessary filter, not an invalid enclosure
or an existence certificate. In particular its `retained` status
does not contradict (4). The finite scalar evaluation on this cell
provides no evidence about a realized prefix; any rate assertion
restricted to actual references in this empty cell is vacuous.

## 3. Saved-data verification and remaining scope

The [standalone checker](../experiments/check_mixed_second_selected_saved_cell_geometric_exclusion.py)
uses only standard-library JSON, hashes and exact fractions. It pins
this proof, the original reference theorem, the complete probe record,
and all inherited probe inputs. It checks the prescribed node, its
full saved coordinate, (2)--(4), both typed exclusions, and the strict
signs before and after immutable-input checks.

Its separate result preserves the original reference status and both
scalar budgets exactly. It marks only this one beta-zero leaf as a
new necessary exclusion. The other 349 unvisited leaves of the
probe are unchanged. It neither evaluates a replacement cell nor
certifies any central gap, half-row bound, finite-source theorem or
actual-word realization.
