# First-cap continuation with necessary adjacent-block exclusions

Research certificate design, 5 November 2026. This stage preserves every
completed tree and the entire active frontier of the first four cap
attempts. It adds a necessary geometric exclusion only for an own-four
cap with a type-four external input. No new source inequality, root
proposal or numerical execution is asserted here. A complete author
record and independent saved replay are still required.

The new driver is
[continue_mixed_first_cap_coupled_plateau.py](../experiments/continue_mixed_first_cap_coupled_plateau.py).
It calls the separately reviewed pure
[inverse filter](../experiments/mixed_endpoint_inverse_filter.py).
All predecessor proofs, scripts, partial records and the two-box
diagnostic remain immutable.

## 1. The actual-reference subset, including length two

Keep the geometric reference domains of
[the oriented first-cap design](research_mixed_first_cap_oriented_plateau_certificate.md):
full original \(D_3\), and the reduced type-four disk with the
height cuts \(-.108\le\Im b\le-.001\). In the own-four/input-four
family also retain the already proved \(\Re b\ge.259\) restriction.
All outgoing real targets remain the full plateau \([.22,.45]\).

Only in this last type family, let \(a=E_4(b)\) be the original
endpoint map's **attached** coordinate. The
[necessary inverse theorem](research_mixed_endpoint_inverse_filter.md)
proves, for every actual word of length at least three,
\[
 \begin{split}
 U&=e^{-2\pi ib},\qquad A=e^{-2\pi ia},\\
 V&=\frac{1-A(1-U)^3/(1-UA)}{U}=e^{-2\pi it},\\
 W&=V+\frac{(1-V)^3}{1-UV}=e^{2\pi ic},
 \end{split}
 \tag{1}
\]
where \(t\) is the opposite leg of the adjacent ordinary
own-four block and \(c\) is its next external nonprivate leg.
The complete original two-leg equations, including their logarithmic
lifts, imply (1). The inverse equations are used only in this
necessary direction.

Every actual such point satisfies
\[
 t\in P_4,\qquad c\in P_3\cup P_4,
 \quad P_3=\{|z-(.35-.01i)|\le.083\},\quad
 P_4=\{|z-(.30-.052i)|\le.060\}.
 \tag{2}
\]
At length three, \(c\) can be the other endpoint's attached leg;
therefore the union in (2) cannot be replaced by an ordinary-only
height domain. At length two the word is \(44\), and the ordinary
equations (1) do not apply. Instead reflection and uniqueness of the
original endpoint system give
\[
                     b=E_4(b),\qquad \Re b>.276.
 \tag{3}
\]
The real lower bound follows from the exact 909-witness extraction,
not from an ordinary-block assertion.

The admissible own-four/input-four reference subset can consequently
be restricted to the union of the set in (3) and the inverse feasible
set in (1)--(2), intersected with the previous geometric domain. This
union contains every actual reference of every length \(m\ge2\).
Its points need not themselves be realizable by words. No critical
constraint is imposed on the independently varying outgoing integration
target: the filter acts only on the original reference parameter \(b\).

## 2. What one new exclusion node proves

The wrapper first revalidates the original inherited endpoint root on
its original whole parameter cell. For a candidate descendant box it
uses twelve same-inverse Taylor intersections, all containing that
same root, to enclose \(E_4(b)\) throughout the box. The entire
unclipped parameter rectangle is used, as in every previous cap source
calculation. No midpoint is substituted for this enclosure.

The helper receives only these two enclosures and has no root or
source routine. It requires a certified reason for each disjoint
length case:

* For \(m=2\), either the entire box has \(\Re b<.276\),
  or the enclosure of \(b-E_4(b)\) is separated from zero.
* For \(m\ge3\), either the inverse exponential has the wrong
  half-plane, the valid opposite-leg lift is outside \(P_4\), or
  the valid next-leg lift is outside **both** \(P_3\) and \(P_4\).

The exponential-image tests use \(\Im V<0\) and \(\Im W>0\)
as necessary conditions. A logarithm is used only after the whole
interval is in its required strict half-plane, so it gives the unique
lift with real part in \((0,1/2)\). Disk rejection requires a
strict positive lower bound for the squared distance minus the radius
squared. Boundary contacts and unresolved intervals remain.

The denominator identity
\[
                  1-UV=\frac{A(1-U)^3}{1-UA}
 \tag{4}
\]
is evaluated without a cancellation-prone subtraction. If an interval
denominator is not separated from zero, the helper returns unresolved.
It does not treat an interval failure as geometric infeasibility.
Both \(V\) and \(W\) may have zeros away from actual references.
The half-plane test can reject such points, without an invalid inverse
logarithm.

A new tree node has the form `['F', {'m2': reason, 'm3': reason}]`.
It is permitted only for own type and input type both four, after
all older geometric exclusions have failed. The two saved reason codes
are sufficient witnesses; interval display strings are not acceptance
identities. Replay recomputes the full-box enclosure and checks that
both saved reasons remain certified. Higher precision may discover
additional reasons, but cannot replace a missing saved reason.

## 3. Immutable source tiers and exact inherited coverage

The pinned stage-four input is
[research-mixed-first-cap-oriented-plateau-attempt01.json](../repro/results/research-mixed-first-cap-oriented-plateau-attempt01.json),
SHA256 `fb21ee2dc6ec496b1b890fd8d26cc471da9d845075565b05179d1abf7086e507`.
It contains 19,996 complete job trees and the 306-node prefix of the
next job, with nine pending boxes: 24,564 committed nodes in total.
The stage-five driver copies all of them literally. The final failed
uncommitted trial is diagnostic only and can be removed without
changing a tree or its frontier.

The pinned stage-four record also binds the original three predecessor
records. Each successor must retain every predecessor's completed
trees and active prefix exactly. Thus five arithmetic tiers are fixed
by job and node position, not selected by a new interval outcome:

| Tier | Source rule and exclusions available when created |
|---|---|
| Original stage one | Original source helper with gap \(1/20000\); original disk exclusions |
| Stage two | Its unchanged source helper with gap \(1/20000\); additional lower-height exclusions |
| Stage three | Its source helper with gap \(1/200000\); reduced disk and upper-height exclusions |
| Stage four | Its source helper with gap \(1/200000\); the adjacent-four real restriction |
| New stage five | The same stage-four source helper and gap, plus the necessary `F` exclusions |

Every saved source leaf is replayed by the module that originally
accepted it, with its original target trial and margin. The newly
coupled domain does not retroactively narrow an old arithmetic box,
weaken an old margin, or exempt an old leaf from replay. Legacy source
helpers have the same formulas; keeping the literal modules also
retains their original constants.

The complete job inventory is unchanged: all 5,258 original endpoint
witnesses, both own types, both input types, and four cut/alias families
per witness, for 21,032 jobs. On every leaf, the free outgoing target
is covered by the same strict-concavity gain with
\[
                 \mu=3/200,\qquad \kappa=1/2500000.
 \tag{5}
\]
Neither the target domain nor an alias penalty is changed.

Each job starts with its original inherited reference rectangle. A
stored split consumes one box and retains both exact children in the
recorded right-first order. Each geometric exclusion must pass its
original strict test. A source leaf must pass its declared source
rule. A coupled exclusion must pass both length tests above. Complete
trees exhaust their stacks; an active prefix reconstructs exactly its
saved pending stack, including depths. Therefore all admissible actual
references are either inside a validated source leaf or still pending.
The test covers full parameter rectangles, so removing infeasible
boxes does not invoke a minimum principle on an uncontrolled new
boundary.

## 4. Resumable author and complete saved replay

Each author attempt uses a fresh output path and at most 600,000
additional committed nodes and 600 seconds of numerical continuation.
The separately recorded depth limit defaults to 30 and may not exceed
45. An attempted box remains pending during every fallible root,
filter and source calculation. Signal-masked commits and atomic file
replacement preserve coverage at a deadline or failure. Attempted and
committed counts are distinct. An uncertain filter simply continues
to the ordinary source check; it is not an accepted exclusion.

Every resume verifies the immutable input hash, retains all completed
trees, and extends the prior active tree as a prefix. All four pinned
ancestors and their proof, script and input bindings remain current.
The two exact geometry extractions are rechecked independently of
source acceptance. The successful two-box diagnostic motivated the
new rule but is not an acceptance input: every adopted `F` box is
proved afresh by its whole inherited root enclosure.

Complete saved replay has no author time alarm. It prohibits complex
root and target proposals, does not split or refine boxes, and checks
every source leaf under its original tier. Every `F` node is recomputed
from the original witness using the saved two reason codes. Structural
checkpoint validation checks its shape and allowed position; only
complete replay supplies its independent higher-precision verification.

Only a complete author and its independent saved replay establish the
four cap comparisons on the necessary actual-reference domain. The
first-cap source reduction and the whole-plateau assembly can then use
those comparisons at every actual word reference of length at least
two. This is not the stronger false comparison on discarded independent
inputs, and it is not a theorem for selected/nonplateau open-source
sectors or arbitrary short fillings.

Example commands after proof and code reviews:

```sh
.venv/bin/python experiments/continue_mixed_first_cap_coupled_plateau.py --precision 256 --output repro/results/research-mixed-first-cap-coupled-plateau-attempt01.json
.venv/bin/python experiments/continue_mixed_first_cap_coupled_plateau.py --precision 320 --input repro/results/research-mixed-first-cap-coupled-plateau-attempt01.json --output repro/results/research-mixed-first-cap-coupled-plateau-replay.json
```

An incomplete author remains a fresh-path `--resume` input; it cannot
be passed as a complete-replay record.
