# Complex estimates and exact operations in the volume proof

Start with [ConwayAssembly.lean](ConwayAssembly.lean). It takes the
original finite coherent color contraction, bounds its entire remainder
using the actual crossing coefficients, and applies the complex packet
theorem. The coefficient bound is proved in
[FourierHermite.lean](FourierHermite.lean); it is not an assumed norm
bound for the filled expression.

The code follows the retained statements of the
[reference](../manuscript/README.md) and the
[17-page Conway paper](../papers/conway-asymptotics/README.md).
The [coverage map](../formal/coverage.json) records each module's exact
manuscript anchors, public roots and role.

## The Conway and conceptual statements

| Module | Statement proved |
| --- | --- |
| CoefficientGram | Finite synthesis in the complex l² coefficient space, adjoint Gram pairing, kernel equality, coordinate changes, the closing upper bound and exact corridor composition. Dependent spanning vectors are allowed. |
| FourierHermite | The actual shifted discrete Fourier transform, exact reconstruction, Parseval, centered normal energy, the exceptional zeroth coefficient and truncated two-place shift. Its physical specialization proves the full crossing coefficient mass bound at every level $N\ge2$. |
| StationaryElimination | Solve the linearized stationary matrix equation and derive its complex bilinear Schur complement. The transpose is ordinary transpose, as required for a holomorphic Hessian. |
| RealTransfer | Ordinary complex norms, real logarithms, zero-safe exponential envelopes and polynomial costs. A nonzero limiting amplitude, finite actions and a strict gap for the whole remainder give eventual nonvanishing and the volume-normalized limit. |
| ConwayAssembly | Retain the exact finite color sum, derive the product-of-coefficient-masses estimate, prove the resulting cost has zero upper rate, and transfer the whole remainder before applying RealTransfer. |

The Fourier estimate retains both spectral values and normal data. It
does not replace a double root by its value. The Gram estimates retain
the physical closing functional as additional data; they supply no
unjustified lower bound for a matrix coefficient.

The analytic implicit-function and chain-rule step is written in the
reference; StationaryElimination checks the resulting block algebra.
The source-specific contour estimates, nonzero whole filling packet and
marked geometric volume equality are the written inputs of the Conway
assembly. Their actual formulae and quantifiers are visible in the
theorem's hypotheses.

## The independent fixed-boundary variational argument

The remaining modules support the reference's ordinary triangular
insertion and weak-balance proofs:

- WeightedGraph and GroundedLaplacian construct the actual graph energy,
  its constant kernel and its grounded inverse.
- TriangleLoads and TrianglePotential differentiate the supported
  triangle action, retaining singleton rows and fixed zero corners.
- TransportCoercivity, GroundedConvexity and TriangleMinimizer prove
  attainment and uniqueness for the fixed-boundary potential.
- TriangleBalance, HallRecession and TriangleHall derive balance from
  strict finite cuts and compatible total demand.
- Flattening proves the one-variable cost and gain comparisons used
  with those actions.

These are the dual fixed-boundary arguments in the ordinary-insertion
appendix. They are not substituted for the different strict Newton
optimizer in the Conway proof.

## Pinned setup and replay

The projects use Lean 4.32.2 and Mathlib
905b95818eb32af7874a58b427f50c1711a5e96c. All nine Git dependency pins
are recorded in [dependency-pins.json](../formal/dependency-pins.json);
the Std package remains the relative dependency at ../formal.

For a fresh checkout, install the toolchain, materialize the pinned
dependencies and request only the imports used by the active sources:

~~~sh
elan toolchain install leanprover/lean4:v4.32.2
cd formal-real
MATHLIB_NO_CACHE_ON_UPDATE=1 lake update volumeLogic mathlib
rg --no-filename '^import Mathlib\.' --glob '*.lean' --glob '!**/.lake/**' . \
  | cut -d' ' -f2 | sort -u | xargs lake exe cache get
cd ..
python3 repro/check_lean.py --output repro/results/volume-lean
~~~

Routine replay makes no dependency downloads or pin updates. It cleans
only local generated build directories, builds the finite dependency,
compiles the selected Mathlib modules in dependency order, and audits
every public declaration. Admitted proofs and additional axioms are
rejected. The runner also detects retired-module imports, unexpected
source files and source changes during the run.

The [cleanup record](../repro/PROOF_PATH_CLEANUP_2026-11-25.md) gives the
actual replay result and the retained proof chain.
