# Necessary adjacent-block exclusions for the terminal-four source

Research continuation design, 5 November 2026. This stage preserves
all three earlier terminal-source prefixes. It adds a necessary
actual-reference test to new parameter boxes only. The twenty-one
source families, original root branch, target domains and requested
gap are unchanged. No author attempt or saved replay of this stage
has been executed.

The new driver is
[continue_mixed_terminal_four_source_coupled.py](../experiments/continue_mixed_terminal_four_source_coupled.py).
The [oriented continuation](research_mixed_terminal_four_oriented_source_continuation.md)
and all earlier source proofs, scripts and records remain immutable.

## 1. The additional necessary condition

The original reference parameter is the incoming attached leg of a
type-four terminal block. Type-three inputs retain their full original
disk and are never tested by this filter. For a type-four incoming
leg, use the same compact domain
\[
 K_4^{\mathrm{adj}}=
 \{|b-(.30-.052i)|\le.060\}
 \cap\{-.108\le\Im b\le-.001,\ \Re b\ge.259\}.
 \tag{1}
\]
Its coverage of every actual input at every length \(m\ge2\) was
proved in the preceding continuation, using the ordinary oriented
image bounds and the separate 909-witness endpoint extraction.

Let \(a=E_4(b)\) be the attached output, coordinate 1 in the original
three-coordinate endpoint map. For \(m\ge3\), reflect the labels
in [the necessary inverse lemma](research_mixed_endpoint_inverse_filter.md):
\(b=t_{m-1}\), \(a=s_m\), \(t=s_{m-1}\), and \(c=t_{m-2}\).
The penultimate vertex is ordinary. With
\[
 U=e^{-2\pi ib},\quad A=e^{-2\pi ia},\qquad
 V=\frac{1-A(1-U)^3/(1-UA)}{U},\quad
 W=V+\frac{(1-V)^3}{A(1-U)^3/(1-UA)},
 \tag{2}
\]
the original critical equations imply
\[
 V=e^{-2\pi it},\qquad W=e^{2\pi ic},\qquad
 t\in P_4,\quad c\in P_3\cup P_4.
 \tag{3}
\]
Here \(P_3,P_4\) have centers \(.35-.01i,.30-.052i\)
and radii \(.083,.060\), respectively. For \(m=3\), \(c\)
is an attached endpoint leg, not a private one. The actual
local-factor extraction includes it in these smaller disks.

Consequently any one of the following whole-box interval conclusions
excludes every actual reference of length at least three:

* \(\Im V\ge0\) or \(\Im W\le0\);
* if \(\Im V<0\), the principal lift
  \(t=-\operatorname{Log}V/(2\pi i)\) is strictly separated
  from \(P_4\);
* if \(\Im W>0\), the principal lift
  \(c=\operatorname{Log}W/(2\pi i)\) is strictly separated
  from both \(P_3\) and \(P_4\).

The strict half-plane hypotheses identify the only possible lifts
with real part in \((0,1/2)\). No inverse-logarithm branch is chosen
for a crossing enclosure. Disk separation means an outward positive
lower bound for squared distance minus squared radius. Unresolved
denominators, half-planes or distances supply no exclusion.

The case \(m=2\) is treated independently. The word is \(44\);
original critical uniqueness and reflection give
\[
                         b=E_4(b),\qquad \Re b>.276.
 \tag{4}
\]
Thus either \(\sup\Re b<.276\) or a strict interval separation
of \(b-E_4(b)\) from zero excludes this case. A new filter node
is accepted **only if both** a length-two reason from (4) and a
length-at-least-three reason from (3) are certified. It is not
enough to fail the ordinary inverse equations alone.

The pure helper
[mixed_endpoint_inverse_filter.py](../experiments/mixed_endpoint_inverse_filter.py)
implements these implications. It does not solve a root or evaluate
a source inequality. It returns separate lists of valid reasons for
the two length cases; an inconclusive test retains the box. The
two-box [original diagnostic](../repro/results/research-mixed-endpoint-inverse-filter-attempt01.json)
is bound as provenance, but its success does not substitute for
testing each newly excluded box.

## 2. Original root enclosures and the new node

The geometric masks and interval clipping are unchanged from the
oriented continuation. In normalized type-four input coordinates
they retain
\[
 [-41/64,15/16]\times[-7/8,51/64]
 \quad\hbox{intersected with the disk of radius }15/16.
 \tag{5}
\]
Empty intersections and strict squared-radius exclusions remain
ordinary X nodes. Equality and boundary contact are retained.

For a nonexcluded type-four box, the driver first revalidates its
inherited original whole-cell root witness. It applies twelve
Taylor-image intersections using that witness's same inverse
matrix, the same original equations and the entire clipped
parameter box. Every intersection contains the already proved
original root. This produces the attached-output enclosure used
in (2) and (4), without a new root proposal or branch choice.

If both length cases are excluded, the new node is
\[
       [\texttt{F},\{\texttt{m2}:\text{reason},
                         \texttt{m3}:\text{reason}\}].
 \tag{6}
\]
Only sufficient reason codes are saved; precision-dependent decimal
interval displays are not replay witnesses. Saved replay recomputes
the enclosures and verifies that both saved reasons still hold.
Additional valid reasons at higher precision are harmless.

If the filter is inconclusive, the exact original source test is
applied on the same clipped rectangle, with unchanged
\[
 \mu=3/100,\qquad \kappa=1/2500000,\qquad
                         D<-1/20000.
 \tag{7}
\]
The fixed rational target proposal and its full concavity correction
remain those of the original certificate. A failed test is subdivided
within the recorded limits or retained on the unresolved frontier.
There is no conversion of filter feasibility into source acceptance.

## 3. Preserve three immutable prefixes

The bootstrap record is
[terminal stage three](../repro/results/research-mixed-terminal-four-source-stage3-attempt01.json),
SHA256
151200a014e548445543a2aba66210c38714d0904305cdb3a73d665f60429738.
It is incomplete, with 39,335 completed jobs, a 2,137-node active
prefix for job 39,335, four pending boxes, and 128,974 committed
nodes in total. Its additional count is 7,674. It stopped at the
depth cap without an arithmetic error. The uncommitted failed-trial
description is diagnostic and may be removed; no accepted node,
saved target or frontier box is removed.

The earlier two records remain separately pinned:

| Stage | Record hash | Complete jobs | Active nodes / pending boxes |
|---|---|---:|---:|
| Original | 8bd75d7cfc1a5dad99579cb48e69aef5ced000ce505687aae805ec24183b041e | 36,752 | 2,566 / 5 |
| Reduced disk | ac3053b04d24b46dda525f4746ba1e7c1b3fc937b51eef763adeb8e878d15a03 | 38,789 | 2,453 / 6 |

Every preceding complete tree is literally preserved, and each
preceding active tree is an exact prefix of its successor. Fixed
node positions in these three snapshots choose the replay rule:

1. Original nodes use the original lower-mask source arithmetic.
2. Remaining stage-two nodes use the reduced-disk arithmetic.
3. Remaining stage-three nodes use the oriented-domain arithmetic.
4. Only appended nodes may use the new filter.

All inherited source leaves are rechecked with their original rule,
even if they lie outside the newer necessary domain. A new F node
is forbidden in any inherited prefix and on every type-three input.
The ordered inventory remains all 1,911 original own-four root cells
times the same twenty-one target families, or 40,131 jobs.

## 4. Coverage, immutable continuation and complete replay

Every tree is reconstructed from its original root parameter
rectangle using the recorded split axes. Both exact children are
retained at every split. Exclusions and source leaves are terminal
nodes; the active tree's right-first stack must agree exactly with
its recorded frontier. In author mode this structural reconstruction
does not repeat inherited numerical source tests.

For actual references, geometric X exclusions and the two-case
F implication remove no required input. The remaining source leaves
therefore cover every actual terminal reference if all jobs complete.
This is a sufficient comparison on an implicitly restricted reference
set, not a comparison on the entire auxiliary domain (1), and not a
converse characterization of realizable references.

All original root/source records, proofs and scripts, the three
incomplete snapshots, the two exact oriented geometry extractions,
the necessary inverse proof, the two-box diagnostic and the pure
filter helper are hash-bound. A continuation uses a new output path
and extends an immutable input. An author attempt is capped at
600,000 additional committed nodes and 600 seconds; the default
depth cap is 30 and the allowed maximum is 45. The active box stays
pending through all fallible arithmetic. Signal-masked commits and
atomic checkpoints preserve the complete frontier on every stop.

Complete saved replay has no author alarm. It forbids both root and
target proposals, performs no subdivision, revalidates every original
witness used, and checks every source leaf and every new F reason.
All prefix, partition, inventory and dependency checks are repeated.
Only a complete author and this saved replay establish all twenty-one
comparisons at every actual input for fixed words of length \(m\ge2\).

The implication to
[whole-terminal completion](research_mixed_terminal_four_full_completion.md)
uses Condition C on this necessary reference set. Its proof needs
the twenty-one comparisons at the actual reference, so all phase
normalizations, halfweights, ordinary-color germs and discarded-current
budgets remain unchanged. Finite closed excluded boxes contain no
actual reference; for any fixed actual point, a sufficiently small
neighborhood avoids them. Thus this restriction does not remove the
local incoming germ used by the assembly. No global open-word source
theorem or larger auxiliary-domain comparison is inferred.

Commands only after the proof and driver have been reviewed:

~~~sh
.venv/bin/python experiments/continue_mixed_terminal_four_source_coupled.py --precision 256 --output repro/results/research-mixed-terminal-four-source-stage4-attempt01.json
.venv/bin/python experiments/continue_mixed_terminal_four_source_coupled.py --precision 320 --input repro/results/research-mixed-terminal-four-source-stage4-attempt01.json --output repro/results/research-mixed-terminal-four-source-replay.json
~~~

An incomplete attempt is an immutable --resume input, never a
complete-replay input.
