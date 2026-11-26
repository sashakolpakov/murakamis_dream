# What the Lean proofs cover

The formalization proves finite algebraic, scalar analytic and
variational implications used in the manuscripts. The completed semantic
audit compares **76 selected theorem roots in 28 modules** with their
written statements. It combines an author-reviewed interpretation of
each statement with a separate, kernel-checked expected-type contract.
It does not formally define the knot invariant, build the hyperbolic
metric or verify every step of the written volume proof.

The [manuscript and logic audit](MANUSCRIPT_AND_LOGIC_AUDIT_2026-11-25.md)
records the mathematical corrections and the division of work among the
papers. The [reference manuscript](../manuscript/README.md) is a unified
account of overlapping arguments; it is not another prerequisite for
every paper. The 19-page [Conway paper](../papers/conway-asymptotics/README.md)
uses its stated companion results. Its final application in Lean is
conditional on the written source and geometric inputs.

## Selected statements and their contracts

| Group | Modules / selected roots | Correspondence and expected types |
| --- | --- | --- |
| Finite algebra, support and sector comparisons | 12 / 37 | [Finite record](../formal/correspondence/finite.json); [StatementContracts.lean](../formal/StatementContracts.lean) |
| Complex norms, Fourier estimates and asymptotic transfer | 5 / 20 | [Analysis record](../formal/correspondence/analysis.json); [AnalysisContracts.lean](../formal-real/AnalysisContracts.lean) |
| Fixed-boundary optimization | 11 / 19 | [Variational record](../formal/correspondence/variational.json); [VariationalContracts.lean](../formal-real/VariationalContracts.lean) |

The [coverage map](../formal/coverage.json) registers the modules, selected
roots and manuscript anchors. Each correspondence record adds a symbol
dictionary, hypotheses, conclusion and explanation of what remains
written. The audit checked meanings as well as names: for example, the
ordinary transpose in a holomorphic Hessian, the shifted Fourier
normalization, the derivative data at repeated roots, and the total-mass
condition needed to recover the grounded variational equation at the
fixed vertex.

Each contract is an anonymous Lean example. It explicitly states the
expected proposition, then applies the selected theorem to prove it.
This checks that the theorem supplies that proposition with those
hypotheses. A declaration-name check or matching source hash would not
do so. Conversely, the contract does not make Lean interpret mathematical
prose: identifying its variables with manuscript notation remains an
author-reviewed part of the correspondence.

The records use four relations:

| Relation | Selected roots | Meaning |
| --- | --- | --- |
| Exact | 15 | The Lean proposition matches the cited abstract mathematical statement under the recorded dictionary. No part of that cited statement is left unformalized. |
| Specialization | 10 | A more general Lean theorem is instantiated with the manuscript's hypotheses and parameters. |
| Component | 41 | Lean proves the identified finite or algebraic part of a larger written argument. The other steps are listed explicitly. |
| Conditional | 10 | Lean proves the conclusion after the listed application hypotheses have been supplied. Their proofs remain written. |

An exact abstract lemma can still have a written application. For
example, proving a scalar exponential-transfer theorem exactly does not
identify its arbitrary complex sequence with a knot invariant.

## The Conway implication

The five analysis modules cover the following chain:

| Written argument | Lean contribution and boundary |
| --- | --- |
| Synthesis and gluing | [CoefficientGram](../formal-real/CoefficientGram.lean) proves the adjoint Gram identity, kernel equality, coordinate changes and a closing upper bound. It allows dependent spanning vectors, but gives no lower bound for a matrix coefficient. |
| Finite filling coefficients | [FourierHermite](../formal-real/FourierHermite.lean) proves shifted inversion and Parseval, retains values and derivatives at repeated roots, and bounds the full crossing coefficient mass. |
| Elimination of stationary variables | [StationaryElimination](../formal-real/StationaryElimination.lean) proves the linearized block algebra and bilinear Schur complement. Differentiation and local analytic existence remain written. |
| Logarithmic growth | [RealTransfer](../formal-real/RealTransfer.lean) proves eventual nonvanishing and the scalar growth limit from a nonzero amplitude, convergent finite-level actions and a strict exponential bound for the whole remainder. |
| Final assembly | [ConwayAssembly](../formal-real/ConwayAssembly.lean) derives the product coefficient cost from a coherent finite contraction and applies the scalar theorem. Its physical coefficient identity is required from level three; the coefficient estimate itself holds from level two. |

The actual knot construction, its exact source formula, contour and
stationary-phase estimates, survival of the combined leading
coefficient, and absolute identification of the action with hyperbolic
volume must be established in the manuscripts. The code keeps these
inputs visible rather than treating an arbitrary source as a knot.

The variational group proves generic graph-energy, coercivity,
minimization and balance statements. A particular planar diagram still
requires its written support and cut calculations. These fixed-boundary
results are distinct from the Newton optimization used in the Conway
proof.

## Tests that reject incorrect propositions

The three [compiler controls](../formal/correspondence/controls.json)
pair a valid theorem application with a deliberately altered expected
type. The positive source must compile; the well-formed negative source
must fail with a type mismatch.

1. **Parseval normalization.** The valid statement divides the input
   energy by N. Removing 1/N is false already for the constant function
   at N = 2: its shifted transform has energy one, while its input has
   energy two.
2. **Holomorphic mixed blocks.** The Schur calculation needs the
   identification D = Bᵀ. Replacing that premise by D = B* does not supply
   it over the complex numbers. Taking B = i and D = −i separates the two
   identities.
3. **Strict remainder gap.** The scalar transfer uses b < Re S. Replacing
   it by b ≤ Re S allows a remainder with the same exponential rate to
   cancel the entire leading term. Eventual nonvanishing then fails.

These are controls on substantive type distinctions. They supplement
the proofs and the semantic reading; they are not a numerical test of
the volume conjecture.

## Replay and the separate axiom inventory

Run from the repository root:

~~~sh
python3 repro/check_lean.py --output repro/results/manuscript-and-lean/lean
~~~

The runner rebuilds both packages from empty local build directories,
checks the pinned dependencies and active import graph, compiles the
expected-type contracts and exercises the three controls. It also
inventories **all public definitions and theorems**, not just the 76
selected roots, and checks their axiom dependencies. The allowed axioms
are `propext`, `Classical.choice` and `Quot.sound`. Admitted proofs and
additional axioms are rejected.

Source inventories, anchors and hashes check which statements were
compiled and whether the inputs stayed fixed. Kernel checks prove the
Lean propositions. The author-reviewed dictionaries explain their
relationship to the manuscripts. These are separate checks with
different purposes.

The [completed Lean replay](results/manuscript-and-lean/lean/summary.json)
records 28 compiled modules and 534 public declarations audited, including
all 76 expected-type contracts and the rejection of all three intended
type errors. The [combined verification record](results/manuscript-and-lean/verification-summary.json)
links the document, proof-logic and formal checks. The
[collection record](results/paper-collection/summary.json) covers 21 papers
totalling 420 pages; the unified reference is 210 pages. These build and
replay results have the mathematical scope explained above.
