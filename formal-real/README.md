# Complex estimates and variational arguments in Lean

This package proves specified internal implications from the
[reference manuscript](../manuscript/README.md) and the
[19-page Conway paper](../papers/conway-asymptotics/README.md). It contains
16 mathematical modules: five for complex and asymptotic arguments, and
eleven for fixed-boundary optimization. Together with the
[finite algebra package](../formal/README.md), the formalization has 28
modules and 76 selected theorem roots: 37 finite, 20 analysis and 19
variational roots.

Start with [ConwayAssembly.lean](ConwayAssembly.lean) to see how the
Conway implication is assembled. Its inputs include an exact finite
color contraction, estimates for its source terms, and the geometric
identification of the limiting action. It derives the coefficient cost
and controls the whole remainder before applying the scalar asymptotic
theorem. Constructing those inputs for a knot remains part of the written
proof; the code does not define a knot invariant independently.

## Complex norms, Fourier coefficients and asymptotic transfer

| Module | What is proved |
| --- | --- |
| [CoefficientGram](CoefficientGram.lean) | Finite synthesis in complex l², its adjoint Gram form, equality of their kernels, coordinate changes, an upper bound for a closing functional, and composition of linear corridors. The spanning vectors may be dependent. |
| [FourierHermite](FourierHermite.lean) | The shifted discrete Fourier transform, inversion and Parseval with their stated normalization; centered normal energy; reconstruction retaining both values and derivatives; and the crossing coefficient mass estimate for every level N ≥ 2. |
| [StationaryElimination](StationaryElimination.lean) | The solution of the linearized stationary equation and its complex bilinear Schur complement. The mixed Hessian blocks use ordinary transpose. |
| [RealTransfer](RealTransfer.lean) | Exponential upper envelopes, polynomial costs, and scalar asymptotic transfer. A convergent nonzero amplitude, convergent finite-level action and strictly smaller exponential rate for the whole remainder imply eventual nonvanishing and the logarithmic growth limit. |
| [ConwayAssembly](ConwayAssembly.lean) | The coherent finite color contraction, its product coefficient cost, the vanishing exponential rate of that cost, and the resulting conditional volume-limit implication. The physical coefficient identity is required only from level three. |

The distinctions matter. Parseval includes a factor 1/N. Repeated roots
retain derivative data, and the two-place shift is truncated rather than
cyclic. A Gram estimate supplies an upper bound; it does not prove that a
closing functional has a nonzero value. The stationary elimination module
checks block algebra after the required differentiations and local
existence argument have been supplied. It does not prove a holomorphic
implicit-function theorem.

The scalar transfer theorem keeps the finite-level action inside the
exponential. It allows an arbitrary unit scalar phase and proves
eventual nonvanishing before taking an ordinary real logarithm. The
equality between the limiting action and hyperbolic volume is an explicit
additional hypothesis in its geometric application.

## Fixed-boundary optimization

The other eleven modules formalize the variational argument used for
ordinary triangular insertion. WeightedGraph and GroundedLaplacian
construct the graph energy and remove its constant kernel by fixing one
vertex. TriangleLoads and TrianglePotential differentiate the supported
triangle action, including singleton rows and fixed zero corners.
TransportCoercivity, GroundedConvexity and TriangleMinimizer prove
attainment and uniqueness. TriangleBalance, HallRecession and TriangleHall
derive balance from strict cut inequalities and compatible total demand.
Flattening supplies the accompanying one-variable comparisons.

These are generic finite-dimensional theorems. Applying them to a
particular planar diagram requires the written construction of its
supports, coefficients and cuts. They do not replace the distinct Newton
optimizer in the Conway argument.

## Statement correspondence and checks

The [analysis](../formal/correspondence/analysis.json) and
[variational](../formal/correspondence/variational.json) records give
author-reviewed symbol dictionaries and spell out the hypotheses and
conclusion of each selected root. They distinguish exact statements,
specializations, components and conditional implications.
[AnalysisContracts.lean](AnalysisContracts.lean) and
[VariationalContracts.lean](VariationalContracts.lean) separately state
the expected propositions and prove them using the library. Lean checks
those types; the interpretation of manuscript notation remains a
mathematical reading task.

Three [compiler controls](../formal/correspondence/controls.json) check
that essential changes are rejected: omitting the Parseval factor 1/N,
substituting conjugate transpose for the holomorphic mixed-block
identification, and replacing the strict remainder gap by a nonstrict
one. Each control pairs a compiling application with a well-formed
application that must fail with a type mismatch. These tests check the
stated distinctions, not the correctness of a written contour argument.

The [coverage guide](../repro/PAPER_FORMAL_COVERAGE.md) and
[manuscript and logic audit](../repro/MANUSCRIPT_AND_LOGIC_AUDIT_2026-11-25.md)
describe the scope and corrections. Geometric constructions, contour
deformations, local analytic existence and the knot-specific application
of the abstract statements retain written proofs.

## Pinned setup and replay

The projects use Lean 4.32.2 and Mathlib
905b95818eb32af7874a58b427f50c1711a5e96c. The nine Git dependency pins
are in [dependency-pins.json](../formal/dependency-pins.json); the finite
package is a relative dependency at `../formal`.

For a fresh checkout:

~~~sh
elan toolchain install leanprover/lean4:v4.32.2
cd formal-real
MATHLIB_NO_CACHE_ON_UPDATE=1 lake update volumeLogic mathlib
rg --no-filename '^import Mathlib\.' --glob '*.lean' --glob '!**/.lake/**' . \
  | cut -d' ' -f2 | sort -u | xargs lake exe cache get
cd ..
python3 repro/check_lean.py --output repro/results/manuscript-and-lean/lean
~~~

Routine replay downloads nothing and changes no dependency pins. It
rebuilds local artifacts, checks all registered contracts and compiler
controls, and separately audits the axiom dependencies of every public
definition and theorem. The permitted axioms are `propext`,
`Classical.choice` and `Quot.sound`; admitted proofs and additional axioms
are rejected. The [completed replay](../repro/results/manuscript-and-lean/lean/summary.json)
records 28 compiled modules, 534 public declarations audited, all 76
statement contracts checked and all three intended type errors rejected.
