# Fixed saved-data test for the remaining three-four right-strip faces

Protocol, 7 November 2026. This test reads existing certified
bounds and adds only the rational transport costs proved in
[the right-strip face extension](research_mixed_three_four_private_left_right_extension.md).
It evaluates no phase, root, primitive, derivative or optimizer.
All outcomes, including insufficient upper bounds, must be saved.

Execution is permitted only after full root and independent peer
review of this protocol, the final analytic cost proof, and the
standalone checker. The final files and inherited inputs must be
hash-bound before the single run.

## 1. Immutable source records and coverage

Use the completed author record
repro/results/research-mixed-terminal-four-source-stage4-attempt01.json,
SHA256
e3651c4ec370625b6be4b8a93ab000730926c33d4062162c7188d0712d56f5d3,
and its completed replay
repro/results/research-mixed-terminal-four-source-replay.json,
SHA256
3b38c1f62ee63f537db1ec2209bb9e278cc273b477dec03b7e0f15fb7f57cf79.

The original cover contains 21 comparison families on each of
1,911 reference cells. This test retains every original reference
cell, including both incoming types. No subset is selected by a
new numerical or geometric filter. This is conservative coverage
for extracting the saved reserves. The analytic transport theorem
itself remains restricted to the actual ordinary \((3,4)\) pair;
the extra cells do not extend that theorem's geometric hypotheses.

The standalone checker is
experiments/check_mixed_three_four_right_strip_saved_faces.py.
It must verify the passed, complete status of both records,
the replay's author hash and precision, full equality of their
saved trees, the complete 21-family inventory and job ordering,
and all inherited current dependency hashes. It must check the
source and exclusion leaf counts against each saved replay
summary. Every original exclusion keeps its original meaning,
as established by the completed replay. A job with no source
leaf has no numerical maximum; it cannot be assigned a negative
source value. Both records' existing completeness and coverage
statements remain hypotheses verified by their original replay,
not conclusions of a new root computation.

## 2. One prescribed rational comparison

For a finite printed ball \([m\mathbin{+/-}r]\), parse both
decimal strings as exact fractions and use the outward upper
bound \(u=m+r\). An exact displayed decimal may also be read
as its exact rational value. Reject unrecognized or nonfinite
data and negative radii.

Use exactly these eight families and costs, numbered as in the
original inventory:

| Index | Original face | Added cost |
|---|---|---|
| 0 | Real transform cut \(t=.15\), private main height | \(7/400\) |
| 1 | Real transform cut \(t=.5\), private main height | \(0\) |
| 2 | Real private cut \(e=.27\), transform main height | \(0\) |
| 3 | Real private cut \(e=.49\), transform main height | \(103/2000\) |
| 4 | Real corner \((t,e)=(.15,.27)\) | \(7/400\) |
| 5 | Real corner \((t,e)=(.15,.49)\) | \(7/400\) |
| 6 | Real corner \((t,e)=(.5,.27)\) | \(0\) |
| 7 | Real corner \((t,e)=(.5,.49)\) | \(0\) |

For every source-bearing job in those eight families, save the
original upper-bound string, the decoded rational upper, its
cost, their exact sum, and whether the sum is strictly negative.
Retain exact maxima and a witnessing job separately for every
family. The original bound is relative to the bare terminal
plane; the analytic cost proof combines it with the whole
first-cap plane and the exact cancellation of the two marginals.
No additional allocation or omitted quadratic debit is allowed.

A family succeeds only if it has at least one source-bearing
job, every such job has a strictly negative sum, and its full
original coverage is verified. An entirely excluded family
is reported separately and supplies no source estimate.
A zero or positive upper sum is inconclusive about
the sign of the actual source. It establishes only that this
fixed saved-bound comparison did not prove that family.

There is no fallback evaluation, changed cost, narrower target
domain, cell refinement, new exclusion, second output attempt,
or source replay in this protocol.

## 3. Output and scope

Use one fresh output:
repro/results/research-mixed-three-four-right-strip-saved-faces.json.

The output must retain all 15,288 selected jobs, family counts,
source and exclusion counts, all eight maxima, every insufficient
comparison, and all dependency hashes. It must explicitly record
zero phase evaluations, root evaluations, optimizer calls,
new cells, exclusions, refinements and source replays. On an
unexpected exception it must save the completed prefix and the
error, with the unprocessed inventory identified; such a result
cannot establish a family theorem. Existing output files must
not be overwritten.

If all families succeed, the remaining real-face anchors are
bounded below the geometric rate on \([.45,.5]\) at the actual
incoming height of the ordinary pair. Together with the separate
main and alias estimates, these bounds can control the regular
terminal contour after every piece and normalization is checked.

The test does not itself establish the full terminal polynomial
on the added interval. The original physical complements, their
transport to those anchors, the true index endpoints, and any
height-changing connectors must retain their separate proofs.
It does not give a whole-circle or outside-color theorem and
does not establish finitely many exceptional fillings.

