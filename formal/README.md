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
| [MonicRemainder.lean](VolumeLogic/MonicRemainder.lean) | Synthetic division and an explicit remainder modulo a split monic polynomial; coefficientwise reconstruction, the degree bound, and its top coefficient as an iterated divided difference. Repeated nodes are allowed. | Constructs the finite coefficient operation underlying Appendix N's Hermite functional. The actual Chebyshev polynomial and crossing-operator interpretation remain separate inputs. |
| [MonicLinearity.lean](VolumeLogic/MonicLinearity.lean) | Linearity of that constructed remainder and its top-coefficient functional; invariance under coefficient-equivalent lists, arbitrary trailing zeros, and addition of a multiple of the modulus. | Establishes that polynomial representatives give the same functional. It does not identify that functional with the marked crossing matrix. |
| [MonicUniqueness.lean](VolumeLogic/MonicUniqueness.lean) | Uniqueness of the remainder under a coefficientwise degree bound, including padded lists; idempotence; invariance under permutations of repeated or distinct roots; characterization of the functional by its values below the modulus degree and its vanishing on multiples. | Formalizes the canonical-remainder proposition in Appendix N. The characterization gives sufficient hypotheses for identifying a candidate functional; it does not prove those hypotheses for a crossing matrix. |
| [ProtectedSum.lean](VolumeLogic/ProtectedSum.lean) | The three local sector comparisons for a protected triangular sum, cancellation of the duplicated face target, and preservation of a positive gap. The local maxima and the sector map are constructed explicitly. | Scalar part of Appendix Q. The triangle lower bounds, existence of shared witnesses, diagram construction, and analytic and geometric inputs remain written proofs. |
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

For the uniqueness result, suppose a polynomial has a coefficientwise
decomposition \(f=pq+r\), where
\(p(X)=\prod_{i=1}^m(X-r_i)\) and every coefficient of \(r\) in
degree at least \(m\) is zero. The constructed remainder equals
\(r\), coefficient by coefficient. This formulation allows any number
of trailing zero entries. Permuting the roots gives the same modulus
and hence the same remainder, even when some roots coincide. The proof
does not divide by a root difference.

The characterization theorem considers a candidate functional \(F\)
on coefficient lists. If it respects coefficient equality, is additive,
vanishes on every multiple of the modulus, and takes a polynomial of
degree below \(m\) to its coefficient in degree \(m-1\), then it
equals the constructed functional on every input. The four hypotheses
are explicit Lean parameters. Proving them for the literal spectral
functional remains part of the application.

The monic-remainder module represents polynomials by their actual
coefficient lists, allowing trailing zeros. Its main division theorem
proves equality of every coefficient, rather than only equality of
polynomial values at selected arguments. If
\(p(X)=\prod_{i=1}^n(X-r_i)\), it constructs \(q\) and a remainder
of degree less than \(n\), with \(f=pq+\operatorname{rem}_p f\).
Successive synthetic divisions give the iterated divided difference;
the theorem identifies it with the coefficient of \(X^{n-1}\) in
the remainder. No distinctness hypothesis on the nodes is used.
The module also proves that a multiple of the modulus has zero remainder
and that an input represented by at most \(n\) coefficients is unchanged.
This representation bound is the hypothesis of the normalization theorem;
trailing zero entries count toward the list length. For two
coincident nodes it proves the full formula

\[
 \operatorname{rem}_{(X-r)^2}f(X)=f(r)+f'(r)(X-r).
\]

Here \(f'\) is formal polynomial differentiation, defined by a coefficient
recurrence. No claim about analytic differentiability is needed. Thus
the derivative term is derived from polynomial reduction itself.
This top-coefficient functional is not the ordinary trace of the
multiplication matrix. The quantum source's scalar and sign normalization
are not included in its definition.

The empty root list has remainder zero and a zero Newton functional. In
the intended application the root list has positive length and the
coefficient ring is \(\mathbb C\).
The companion `MonicLinearity` module proves that the constructed
remainder and functional are linear over the coefficient ring. If two
lists have equal coefficients at every degree, they give literally the
same remainder list and the same functional value. Thus arbitrary
trailing zeros make no difference. It also proves that
\(f=g+pq\), interpreted coefficientwise with the constructed monic
multiple \(pq\), implies equal remainders and equal functional values.
These conclusions establish invariance under changing the polynomial
representative modulo \(p\). An abstract quotient-ring type and the general confluent root-sum
formula are not yet exported by the project. Invariance under reordering
the roots is proved in `MonicUniqueness`.

The next algebraic step is to supply the actual Chebyshev factorization
and prove that this finite functional evaluates the original crossing
operator, including its nilpotent part. The general coefficient
calculation does not establish that diagram-to-operator correspondence
or the analytic norm of the resulting functional.

## The protected triangular sum

`ProtectedSum` doubles every rate, target and gap to avoid division.
Its variable `b` is \(\log B\), while `qa` and `qc` are
\(2Q(0,a,B)\) and \(2Q(0,c,B)\). The two inequalities
`b ≤ qa` and `b ≤ qc` come from testing a vertex of the triangle
allocation simplex. The module assumes these inequalities; it does not
formalize that variational problem.

The new crossing has three possibilities. Central maps to two central
input pieces, left to left/central, and right to central/right. The
module defines the corresponding maxima, proves their comparison, and
subtracts the actual duplicated target \(2\log B\). Its main theorem,
`protected_sum_certified_rate`, then selects an input certificate from
the noncentral-sector map and proves that the output gap is at least
the smaller input gap. The complete actions and gaps in that statement
are doubled as well.

The finite-list corollary assumes that the accumulated output cost is
bounded by the sum of the selected input costs. It proves the remaining
scalar implication; it does not construct a sequence of triangulated
spheres or shared weight vectors. Those constructions, including the
normalization at each joining face, are proved in Appendix Q.
