# Formal checks of finite proof steps

This directory contains Lean proofs of several finite steps used by the
manuscript. It is the beginning of a formalization, not a formal proof of
the volume conjecture or of a complete theorem in the paper.

From the repository root, with Lean 4.32.2 installed, run:

```sh
python3 repro/check_proof_logic.py --output repro/results/proof-logic
```

The project uses Lean's standard library and has no Mathlib dependency.
The script first builds the library, then runs a separate inspection of
every theorem's logical assumptions. It rejects compiler warnings,
missing theorem reports, and axioms other than `propext`,
`Classical.choice`, and `Quot.sound`. In particular, a proof containing
an admitted step cannot pass this inspection. Hypotheses written as
theorem parameters are not axioms: they must still be proved when the
theorem is applied.

## What the declarations say

| File | Mathematical content | Relation to the manuscript |
| --- | --- | --- |
| [FiniteSupport.lean](VolumeLogic/FiniteSupport.lean) | The central and two one-sided degree regions exhaust the stated support; the one-sided regions do not overlap. The exact endpoint cutoffs are checked separately at even and odd levels. | The decomposition in Appendix O, §3; the degree constraints retained in Appendix P. The extra moment-degree lemma records the cutoff for the separate protected moment calculation. |
| [FiniteAlgebra.lean](VolumeLogic/FiniteAlgebra.lean) | A polynomial divided difference is defined without division. Its resolvent identity holds even at a repeated root. The double-root formula retains the first derivative. A finite product expansion removes precisely the all-evaluation term. | Algebra used in Appendix N. The Hermite identity is proved after clearing denominators; the nonzero denominator and the Chebyshev root data are separate inputs. |
| [RateComparison.lean](VolumeLogic/RateComparison.lean) | A linear entropy gain exceeds a quadratic cost under the stated inequality; nonnegative additional losses cannot undo a strict sector gap; a sufficiently small filling-action drop preserves the gap. | Scalar implications in Appendix P, following the entropy, Hessian, and filling estimates. |

The algebraic declarations quantify over arbitrary commutative rings, or
ordered commutative rings where an inequality is needed. The list
`[a₀, …, aₘ]` in `horner` represents
`a₀ + z(a₁ + z(… + zaₘ))`: its entries are in **ascending** powers.
`dividedDifference` is defined by a recurrence, so no inverse of `z-w`
is assumed. In the tensor identity, the first entry of each pair is the
cost of evaluation and the second is the cost of differentiation.
`nonemptySecondChoices` sums precisely the choices with at least one
derivative. The polynomial product identities concern scalar source
coefficients; they do not assume that neighboring crossing matrices
commute.

For the rate comparisons, `t` is the change of logarithmic face weights,
`h` is a positive lower bound for the relevant triangle entropy,
`energy` bounds the quadratic action cost, and `defect` measures failure
of the unperturbed balance inequality. Formulas are multiplied by two
to avoid introducing division. The Lean proofs do not establish that
these constants have the required properties for a given diagram.
The algebraic comparison lemmas permit a general real margin. The two
`strictly_below` theorems explicitly add its positivity to obtain a
strict rate loss. The geometric application also supplies
\(0<t<1\); the scalar flattening identity itself only needs \(t\ge0\).

## What remains outside these checks

The construction of the exact source from the marked knot diagram,
Chebyshev root multiplicities, analytic coefficient bounds, entropy and
Hessian formulas, nonzero stationary contribution, primitive filling
curves, and equality with hyperbolic volume remain written arguments.
Neither the Lean build nor the finite experimental checks certify those
arguments. The [manuscript audit](../repro/MANUSCRIPT_AUDIT.md) records
which parts have been read and where further formalization is needed.

The next substantial algebraic step is the full quotient-ring Hermite
functional: define the top-coefficient trace modulo the Chebyshev
polynomial and prove that it evaluates the original crossing operator,
including its nilpotent part. That would connect the finite identities
here to the actual functional, rather than adding more scalar bounds.
