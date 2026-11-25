# Formal statements in the retained volume proofs

The active formalization follows the cleaned reference and its shared
strict Conway proof. Start with
[ConwayAssembly.lean](../formal-real/ConwayAssembly.lean): the theorem
retains the exact coherent color sum, derives the whole filled-remainder
bound from the actual crossing coefficient estimate, and applies the
direct complex packet theorem.

The [coverage map](../formal/coverage.json) gives every active module's
manuscript anchors, selected public roots and mathematical role. It
includes the finite polynomial/support arguments in the filling
appendix and the independent fixed-boundary variational argument.
It contains no standalone recurrence or microscopic-profile branch.

The principal new statements are:

| Retained manuscript argument | Lean source |
| --- | --- |
| Transported Gram, its kernel and coordinate changes | [CoefficientGram](../formal-real/CoefficientGram.lean) |
| Shifted Parseval and the actual Hermite coefficient mass | [FourierHermite](../formal-real/FourierHermite.lean) |
| Linearized stationary equation and Schur block | [StationaryElimination](../formal-real/StationaryElimination.lean) |
| Zero-safe costs and the complex packet-to-volume implication | [RealTransfer](../formal-real/RealTransfer.lean) |
| Exact coherent color contraction and its derived whole remainder | [ConwayAssembly](../formal-real/ConwayAssembly.lean) |

The analytic implicit-function/contour arguments and primitive geometric
calibration remain the written inputs at their stated places. The Lean
statements give the exact finite and analytic implications listed here;
they are not an independently defined knot invariant.

Run the complete current check from the repository root:

~~~sh
python3 repro/check_lean.py --output repro/results/volume-lean
~~~

The runner compiles from empty local build directories, validates the
active import graph and pinned dependencies, and audits every public
definition and theorem. It also verifies the literal manuscript
anchors. The source-location checks and the kernel checks have different
roles; their results are recorded separately.

The [cleanup record](PROOF_PATH_CLEANUP_2026-11-25.md) explains the
manuscript-first revision and the subsequent deletion of obsolete sources.
