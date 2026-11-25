# Manuscript and Lean audit

25 November 2026. Updated after the second audit.

The Conway paper and the reference use the same pure-source proof.
The audit checked the exact wire lattice, the factorial continuation,
the local and global Fourier estimates, the full Hermite coefficients,
the whole filling sum and the primitive geometric comparison.
The knot, framing, integer powers, derivative data and finite critical
action remain the same throughout that chain.

## Corrections and deletions

- The reference's abbreviated leaf definition now explicitly includes
  the quarter-turn of the crossing-circle box and its disk.
- The pointed quantum A-period section was removed from the volume
  account. It reconstructed a recurrence and substituted a previously
  proved limit; it supplied no step of the volume proof.
- An unused TikZ style and historical proof-route commentary were removed.
- The quarter-index paper now contains the signed local argument it
  needs. Its proof no longer depends on a deleted edition of the
  Conway paper. The full completed-root packet was not restored.
- FourierHermite now proves exact reconstruction on the shifted grid,
  in addition to Parseval and the full normal-data coefficient bound.
  This closes the finite reconstruction part of the manuscript's
  stated proposition directly in Lean.

The re-audit found no further gap in the retained Conway chain or in
its Gram, stationary-matrix and complex-rate interfaces. This records
the conclusions of the source audit, rather than a claim that source
locations or compiler success prove an analytic contour argument.

Obsolete sources and modules were deleted. The three recent snapshot
trees, older Lean and TeX copies, superseded manuscript PDFs, old
formal controls and their outdated reports are gone. No replacement
archive was created. Ongoing research notes, counterexamples, exact
certificate data and cited external papers remain available.
The [deletion record](results/manuscript-and-lean/deletions.json)
contains paths and sizes only.

Earlier tracked versions are available in
[Git history](https://github.com/sashakolpakov/murakamis_dream/commits/main/).
At the start of the audit, this workspace had no Git metadata. The
[history check](results/manuscript-and-lean/history-check.json)
distinguishes committed files from later uncommitted intermediates;
we did not presume that every intermediate copy was committed.
The obsolete intermediate copies were deleted as requested.

## What the current formalization proves

The [coverage map](../formal/coverage.json) names the retained manuscript
statements and their selected Lean roots. Its principal modules are:

| Source | Mathematical content |
| --- | --- |
| [CoefficientGram](../formal-real/CoefficientGram.lean) | Actual complex coefficient synthesis, adjoint Gram pairing, null directions, coordinate changes, closing upper bound and exact corridor composition. |
| [FourierHermite](../formal-real/FourierHermite.lean) | Shifted Fourier reconstruction and Parseval, centered normal energy, exceptional zeroth coefficient, truncated shift and the physical crossing coefficient bound. |
| [StationaryElimination](../formal-real/StationaryElimination.lean) | The linearized stationary equation and complex bilinear Schur complement. |
| [RealTransfer](../formal-real/RealTransfer.lean) | Zero-safe exponential envelopes, polynomial costs, finite-action complex packets, eventual nonvanishing and ordinary logarithmic limits. |
| [ConwayAssembly](../formal-real/ConwayAssembly.lean) | The coherent whole-color contraction and a derived whole-remainder estimate using the proved Fourier coefficient bound. |

The finite polynomial/support modules still serve the filling-functional
and source appendices. The fixed-boundary variational modules still serve
the weak-balance and ordinary-insertion proofs. They have no dependency
on the removed local quantum induction.

The analytic implicit-function, contour, stationary asymptotic and
geometric calibration arguments have written proofs. Their actual
hypotheses remain explicit in the formal assembly. A Gram norm does
not replace the prescribed closing or supply a lower bound for it.

## Replay

From the repository root:

~~~sh
python3 repro/check_lean.py --output repro/results/manuscript-and-lean/lean
python3 repro/check_manuscript_logic.py --output repro/results/manuscript-and-lean/manuscript-logic
python3 -I papers/conway-asymptotics/check.py --output repro/results/manuscript-and-lean/conway-finite
python3 tools/build_dependency_graph.py
~~~

The Lean replay clears generated local project builds, checks the
pinned dependencies and exact active source inventory, compiles every
selected module and audits every public declaration's axioms. It checks
that its inputs remain unchanged during compilation. The dependency
checker separately verifies the declared assumptions, level scopes
and criterion implications, including rejection of circular assumption
discharges.

The finite examples exercise the actual crossing powers, inverse
powers, repeated-root normals and midpoint formula. They do not replace
the all-level written estimates. The document checks build the PDFs,
resolve the paper graph and check the rewritten guide's MathML and
local links.

The [current verification record](results/manuscript-and-lean/verification-summary.json)
collects those results. The frozen sufficient hypotheses and their
natural-density-one conclusion are unchanged; the general
finite-exception problem remains outside the proved statements.
