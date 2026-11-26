# First-cap plateau certification on the proved typed reference envelope

Research design, 5 November 2026. This final stage continues the
immutable [second-stage certificate](research_mixed_first_cap_actual_plateau_certificate.md)
on a smaller, already proved auxiliary domain, with a less demanding
positive gap. Both earlier proofs, drivers and incomplete records
remain unchanged. No author or replay of this stage has yet run;
the uniform current inequalities remain unproved until they do.

## 1. Domain and unchanged actual-word scope

Keep the entire original type-three disk. For a type-four external
parameter use
\[
 \widehat D_3=D_3,\qquad
 K_4=\{|b-(.30-.052i)|\le.060\}
                  \cap\{-.108\le\Im b\le-.001\}.
 \tag{1}
\]
Every actual first-cap reference of every word of length \(m\ge2\)
belongs to the interior of its corresponding set in (1), with either
own cap type. The first external input is \(s_2\). For \(m\ge3\)
the whole ordinary-block image bounds put this nonprivate leg in the
reduced disk and at height \((-.102,-.001)\). At \(m=2\), it is
the opposite endpoint's **attached** leg, whose reduced-disk inclusion
and height \((-.108,-.020)\) follow from exact extraction of the
original endpoint witnesses. These are the arguments of Lemma 1 in
the second-stage proof together with the radius extraction in
[local factor coverage](research_mixed_open_local_factor_coverage.md).
Equivalently, the
[typed-envelope deduction](research_mixed_typed_last_row_envelopes.md)
proves that the union of the ordinary and attached type-four
enclosures is exactly \(K_4\). No private endpoint leg is being used
as the external reference, including at length two.

All four target families remain unchanged: outgoing real part
\(y\in[.22,.45]\), private real cuts \(.27,.49\), and the
two private horizontal aliases at heights \(-.055,.04\).
Their original allocated phases, penalties, actual attached output
height, both own flags, ordinary colors and source support are
unchanged. The one-vertex case is excluded as before.

In the original normalized type-four input coordinates
\(b=.30-.052i+.064(\xi+i\eta)\), (1) is exactly
\[
                  \xi^2+\eta^2\le(15/16)^2,
                 \qquad -7/8\le\eta\le51/64.
 \tag{2}
\]
Thus restricting the auxiliary reference set preserves the whole
intended actual-word theorem. It does not prove a statement on
either larger domain used by the preceding attempts.

## 2. Requested gap and the preserved incomplete attempts

The original first-stage record is
[research-mixed-first-cap-plateau-attempt01.json](../repro/results/research-mixed-first-cap-plateau-attempt01.json),
SHA256
`a403b6999d00a41d0fdcdb0dd826767b61b3d430cf296a77ff25d3a546471321`.
The second-stage record is
[research-mixed-first-cap-actual-plateau-attempt01.json](../repro/results/research-mixed-first-cap-actual-plateau-attempt01.json),
SHA256
`5f01a37845618dd40301b1310816d71d3180eac17a0df9ece2af981fd88ca796`.
The second attempt stopped at added depth 20, with no arithmetic
error, after 19,732 completed jobs. Its active job 19,732 has a
399-node accepted/split prefix and six pending rectangles.

The last pending box straddles the circle in (2); it cannot be
discarded wholesale. Its saved outward source upper is approximately
\(-4.99874696\cdot10^{-5}\), still strictly negative, but does
not meet the former requested margin \(-1/20000\). Neither this
stop nor the first-stage stop is a counterexample to a current's
sign, or a proof that the larger-domain inequality fails.

We now request
\[
 \delta=1/200000,
 \qquad\kappa=1/2500000,
 \qquad\mu=3/200.
 \tag{3}
\]
The last two constants and every computed source enclosure remain
unchanged. The earlier accepted leaves have the stronger requested
gap \(1/20000\), which implies the new acceptance threshold.

Any fixed strictly positive common gap suffices for the
[first-cap source reduction](research_mixed_first_cap_plateau_phase.md).
It separates discarded cuts and aliases from the fixed-reference
plane and permits a fixed ordinary-color neighborhood and a single
finite-source tolerance. The resulting plane's quadratic coefficient
\(\kappa\) does not depend on this gap. No later conclusion here
spends the former numerical value \(1/20000\) as a budget.

## 3. Exact bootstrap and exclusions

The driver
[certify_mixed_first_cap_typed_plateau.py](../experiments/certify_mixed_first_cap_typed_plateau.py)
requires `--bootstrap-stage2` with the exact immutable second-stage
record above. It binds both ancestor records and their unchanged
proofs, scripts and complete dependency sets. The second-stage
dependency snapshot must agree literally with the currently verified
ancestor inputs. Its original stage-one prefix and provenance must
also match. The four families, both own flags, all 5,258 original
endpoint cells and all 21,032 jobs remain the same.

The 19,732 completed trees and the active 399-node prefix are copied
verbatim. The driver reconstructs their exact right-first partitions
and pending frontier. Author mode performs no arithmetic replay of
accepted leaves, and it does not replace previously accepted leaves
outside (1) by exclusions. The complete numerical helper source
block is still compared literally against the immutable first-stage
script. Only the global requested gap in (3) has changed.

For a normalized box \(B=I\times J\), the disjoint terminal
node rules, in their priority order, are:

* `X`: the original strict outside-unit-disk test;
* `H`: for type-four inputs only, \(\sup J<-7/8\);
* `R`: for type-four inputs only,
  \(\min_{\xi\in I}\xi^2+\min_{\eta\in J}\eta^2>(15/16)^2\);
* `U`: for type-four inputs only, \(\inf J>51/64\).

Each rule is applied only when all preceding rules fail. Thus the
new height and radial exclusions are distinguishable from the old
disk exclusion and from one another. Every comparison is strict:
boundary and crossing boxes are retained. Each square minimum is
zero if its interval contains zero, and otherwise is the smaller
endpoint square. These are exact rational predicates, not sampled
geometric tests. No excluded point belongs to (1).

All admitted boxes retain the original root witness and the unchanged
whole-target concavity test; target boxes are never subdivided.
Additional source failures may refine the reference box. The new
default depth cap is 30, within the unchanged hard limit 45.
The author limits remain 600,000 additional nodes and 600 seconds.
The active box stays pending during fallible arithmetic; commits are
signal-masked and checkpoints atomic. Resuming requires a distinct
immutable input/output pair and literal preservation of every
accepted prefix, trial, split axis and exact frontier.

## 4. Complete replay and conditional source consequence

The final saved replay recomputes every accepted source leaf under
(3), including all imported leaves from both earlier attempts.
Each uses its saved rational target and original-root witness;
target proposals, complex-root proposals and refinement are
forbidden. All four exclusion kinds are validated and counted
separately. No accepted arithmetic is inferred merely from a
historical record's status. The all-job coverage, all ancestor and
current hashes, exact source input and proof/script bindings are
checked before publication.

Only a complete author and an independent complete saved replay
can establish the four comparisons on (1). Combined with the
unchanged analytic source reduction, those comparisons supply the
full outgoing-plateau first-cap supporting plane at every actual
reference of every word of length at least two, for both own types.
The conclusion retains the original outgoing halfweight, every
private finite row, both parities and ordinary-color dependence.
It remains a first-cap result; additional assembly is required for
the full ordinary open-word sum.
