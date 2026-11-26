# Semantic audit of the split-monic remainder formalization

Read-only audit of
`/private/tmp/md-hermite-quotient-formal/VolumeLogic/MonicRemainder.lean`
and the definitions of `horner` and `dividedDifference` in its imported
`FiniteAlgebra.lean`. The inspected file has 37 theorems, 12 definitions,
and SHA256
`f6781dba17c7677adcfe2aec41d31f8742004fc38a45be9732c24ce98b65dbfd`.
No Lean compiler, axiom audit, or numerical check was run, and no code was
edited.

No false algebraic statement or hidden distinct-root assumption was found.
The file supports the intended claim of explicit division by a split monic
polynomial, with repeated factors retained. The representation and scope
qualifications below should accompany that claim.

## What the statements express

- Lines 10--16 use ascending coefficient lists and compare every formal
  coefficient. `CoeffEq` is stronger than equality of evaluations, so the
  division theorem is not relying on an invalid inference from polynomial
  functions over a finite ring.
- Lines 24, 45--53 implement multiplication by \(X-r\): the constant
  coefficient is \(-ra_0\), and coefficient \(n+1\) is
  \(a_n-ra_{n+1}\). `synthetic` is the quotient of
  \(f(X)-f(r)\) by this factor. Reconstruction is coefficientwise even
  for the empty list representing zero.
- `monicMultiple`, `monicQuotient`, and `monicRemainder` at lines
  152--165 are explicit operations, not hypotheses asserting a quotient
  relation. `monic_division_identity` at line 169 proves
  \(f=\prod_i(X-r_i)q+R\) coefficient by coefficient.
- `monic_remainder_degree_bound` at line 231 proves that every coefficient
  at or above the number of factors vanishes. The modulus in line 274 has
  coefficient one at the number of roots by `monicPolynomial_monic`.
- `newtonFunctional` successively applies synthetic division, then
  evaluates at the last root. `top_coefficient_is_newton` at line 243
  proves that this equals coefficient \(n-1\) of the explicit remainder
  for a nonempty list of \(n\) roots. The annihilation theorems at
  lines 380 and 399 kill actual explicit multiples of the modulus.
- `formalDerivativeValue` is the algebraic derivative of the Horner
  polynomial. Lines 417--433 prove the full double-root formula
  \[
  R(X)=f(r)-r f'(r)+Xf'(r)=f(r)+(X-r)f'(r)
  \quad\bmod (X-r)^2.
  \]
  The derivative survives at coincident roots; there is no division by a
  root difference or a factorial. This remains correct in positive
  characteristic.

## Representation and normalization qualifications

1. **List length is not intrinsic degree.** Trailing zero entries are
   permitted. The exact length of `monicRemainder` is the number of roots
   because the result is padded; this is not an assertion that its leading
   coefficient is nonzero. Likewise `monicQuotient_length` is a statement
   about the chosen list representation. The hypotheses of
   `monicRemainder_of_degree_lt` and `newtonFunctional_of_degree_lt`
   (lines 332 and 349) are explicitly `f.length ≤ roots.length`.
   This is sufficient for degree below the modulus, but is stronger than
   that intrinsic condition for an unnecessarily zero-padded input.

2. **Empty roots have an explicit convention.** The modulus is one,
   quotient is the input, and remainder and Newton functional are zero.
   Natural subtraction makes `roots.length - 1` equal zero in this case;
   it does not represent a genuine degree-minus-one coefficient. The
   usual description as the top coefficient at degree \(n-1\) should
   be restricted to a nonempty root list.

3. **The ring need not be a field or nontrivial.** Only `CommRing R` is
   assumed. Zero divisors and repeated roots cause no problem because
   every divisor is monic and the construction is division-free. The
   zero ring is also permitted: the theorem's leading coefficient is
   literally one, but an assertion of exact nonzero polynomial degree
   additionally needs \(1\ne0\). The intended complex application has
   this property.

4. **This is the normalized top-coefficient functional.** There is no
   factor \(N^2\), sign, or other quantum normalization in its definition.
   It is not the ordinary linear-algebra trace of multiplication in the
   quotient; for example its double-root value is \(f'(r)\), not
   \(2f(r)\). The intended interpretation is the algebraic
   top-coefficient, or Frobenius, functional.

5. **The file does not construct an abstract quotient ring.** Its
   statements are about explicit coefficient lists and explicit monic
   multiples. It does not yet export general uniqueness of monic division,
   root-order invariance, linearity of the Newton functional, or congruence
   of every operation under arbitrary `CoeffEq` padding. These are
   mathematical consequences of the same algebra, but should not be
   advertised as separate formalized interfaces already present here.

The safe public description is: the kernel checks coefficientwise synthetic
division and its iteration for an explicit split monic modulus, the
remainder degree bound, the top-coefficient Newton functional, its
annihilation of explicit modulus multiples, and the full double-root
remainder formula. Identification of a particular Chebyshev modulus,
Casimir operator, physical source normalization, or full Hermite filling
functional remains a separate proof input.
