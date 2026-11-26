# Bounded finite-source and canonical-product audit

This record concerns the current publication checkout at `/private/tmp/murakamis_dream-publication`. It reads Chapter 2's finite pair-algebra reduction, Appendix N's canonical remainder and full-Hermite functional, and Appendix M's use of canonical representatives. The accompanying snapshot records the source hashes and exact label locations. It does not claim a new audit of every matrix identity, analytic saddle estimate, or geometric theorem in those dependencies.

## 1. Result and the concrete formal addition

No new manuscript defect was found in the inspected finite-algebra chain. The new proposition `prop:canonical-remainder-products` in Appendix N is mathematically correct and agrees with the newly compiled Lean module `VolumeLogic/MonicProduct.lean`. Its conclusions concern the actual constructed multiplication and remainder, not an assumed quotient-compatibility axiom.

The module adds 43 theorems over an arbitrary commutative coefficient ring. Polynomials are ascending coefficient lists; trailing zero padding is permitted. The multiplication is recursively constructed by

\[
 (a+Xf)g=ag+X(fg).
\]

The proofs establish coefficientwise commutativity, associativity, addition and scalar distributivity, compatibility with coefficient-equivalent lists, and the explicit identity

\[
 (p q)g=p(qg),\qquad p=\prod_{r\in\text{roots}}(X-r),
\]

for `monicMultiple`, including repeated roots. The existing synthetic-division identity is then multiplied by the actual constructed product. This gives

\[
 \operatorname{rem}_p(fg)=
 \operatorname{rem}_p\bigl((\operatorname{rem}_p f)(\operatorname{rem}_p g)\bigr),
\]

as literal equality of the fixed-length canonical lists. The corresponding equality for `newtonFunctional` follows by taking the top coefficient. There is no input-degree restriction.

`quotientProduct` is defined by multiplication followed by that remainder. Its output length, coefficient congruence, commutativity, associativity and reduced unit are proved. `canonicalProduct` reduces at every multiplication in a finite list of factors; `monicRemainder_product` and `newtonFunctional_product` prove that this gives the same result as forming the unreduced product first. A separate abstract quotient-ring type or ring instance is not declared.

## 2. Normal data really retained

The product derivative is derived from the actual coefficient recursion:

\[
 (fg)'(r)=f'(r)g(r)+f(r)g'(r).
\]

`double_root_product_remainder` proves the full linear remainder

\[
 [f(r)g(r)-r(f'(r)g(r)+f(r)g'(r)),\quad
   f'(r)g(r)+f(r)g'(r)].
\]

The last pair of theorems goes beyond a modulus consisting only of the double root. With a root list `r :: r :: roots`, the canonical product retains both its value at `r` and its first derivative there. The existing root-permutation theorem allows any two occurrences of a node to be brought to the front. No distinctness, invertible root differences, nonzero polynomial values, characteristic-zero assumption, or sampled-data inference enters these proofs. In particular the derivative formula remains valid when one or both values vanish.

This matches Appendix N's first-normal requirement. At a double Chebyshev root, its equation `uf:eq-10` includes both the derivative of the inserted crossing function and the derivative of the numerator. At the odd simple node it includes the evaluation term only. The new formal theorem does not identify the whole quantum functional with an ordinary matrix trace, nor assert that the coefficient functional is multiplicative. The manuscript explicitly warns against the latter inference immediately after `prop:canonical-remainder-products`.

## 3. What was checked in the manuscript

### Chapter 2: source-to-polynomial interface

The definitions `eq:pair-casimir` and `eq:hermite-algebra` and the argument at `lem:commutant` supply the actual operator and the monic relation. The cyclic tridiagonal argument identifies the degree below which polynomial representatives are unique; the stated quantum-shift/continuant identity supplies the specific Chebyshev modulus. The later multiplication theorem `thm:positive-product` treats divisibility by that modulus with multiplicity, rather than only vanishing at its distinct eigenvalues. This use is consistent with the new abstract polynomial-product proof.

These are source inputs, not consequences of `MonicProduct`. This bounded read did not reconstruct all entries of the original pair matrices, reprove the quantum-shift annihilating identity, or replay the ordinary cups/caps and crossing-matrix comparison. The source's fixed scalar and cut normalization also remain outside the Lean functional.

### Appendix N: canonical degree and the finite functional

`prop:canonical-polynomial-remainder` remains valid over rings with zero divisors: multiplying a nonzero polynomial by a monic polynomial preserves its nonzero leading coefficient and increases degree by the modulus degree. Its characterization of the coefficient functional is a sufficient identification theorem. The hypotheses still have to be established for the actual crossing functional.

The new `prop:canonical-remainder-products` supplies the needed representative-algebra step without assuming it. Its written proof constructs the modulus multiple of the product difference and then applies uniqueness. The Lean proof independently performs the same task with coefficient lists, multiplication, and the explicit synthetic quotient. Both versions retain repeated-root jets.

Equations `uf:eq-8`–`uf:eq-15` keep the double-node and odd simple-node multiplicities and the original signed crossing phase. The midpoint derivative formula contains the evaluation term, the phase derivative, and the numerator derivative. The one-sided factor `uf:eq-21` removes the first two terms at spectral nodes but leaves the numerator normal. Equations `uf:eq-24`–`uf:eq-25` use joint product-grid vanishing for the unsplit complement; they do not assume vanishing on every node hyperplane. These are the correct finite distinctions for the stated supremum estimates.

The proof of the Riesz interpolation inequality and the resulting norm bound is written mathematics, not formalized by the new module. Likewise the exact identification of `uf:eq-10` with the original crossing operator uses the actual Chebyshev root constants and its full-Hermite interpolation. The finite algebra alone does not supply those constants or the diagram-to-operator correspondence.

### Appendix M: scope of the newly closed algebraic step

In `dao:sec-3.2`, the paragraph beginning “The full complete Hermite norm” restricts norm equivalence to representatives of degree strictly below `N`; products of higher degree are reduced first. The new multiplication theorem verifies that this reduction preserves the algebraic functional and all repeated-root product normals. It does not prove the polynomial norm equivalence, the bound on exact Chebyshev folding in fixed diagram degree, the translated-chart estimates, the local Gaussian expansion, or the source-selected nonzero first charge. Those remain the explicitly cited analytic inputs.

The formal product theorem also does not replace one common face coefficient extraction by independent local extractions. It is a theorem in the coefficient ring chosen by the application; shared face variables or a further coefficient map must retain their original identities.

## 4. Logical assumptions and compilation

The module and the aggregate library compiled without warnings under the pinned `leanprover/lean4:v4.32.2` toolchain. After that successful build, the parent resumed ownership of the shared aggregate and axiom-audit files to add its separate regrading module. No concurrent full build was run during that edit.

A separate temporary driver importing only `VolumeLogic.MonicProduct` printed the assumptions of all 43 new theorems. Its log is `/private/tmp/md-monic-product-axioms.log`. Every theorem has either no axioms or only the permitted standard logical axioms `propext`, `Classical.choice`, and `Quot.sound`. There is no `sorry`, `sorryAx`, or custom axiom in the module. All ring assumptions and theorem parameters are explicit.

The public changes owned in this pass are the new `MonicProduct.lean`, its aggregate import, 43 axiom-audit entries, and a narrowly scoped row and explanation in `formal/README.md`. No manuscript, guide, reproduction runner, recorded global result, or commit was changed by this agent. The parent owns integration and the final combined replay.

## 5. Remaining obligations and scope

The next substantial finite formalization step is the exact actual Chebyshev-root/crossing identity, including the nilpotent coefficient at every repeated node, rather than another assumed-functional characterization. An elementary Chebyshev polynomial recurrence and its actual Casimir evaluation would have to be constructed, together with the relevant matrix action and source scalar. No such result is claimed here.

The open full-source comparison for an arbitrary unchanged matched sphere is also unchanged. A finite functional bound, a canonical product operation, and complete Hermite data do not bound the signed shared source at the geometric rate. None of the new declarations promotes a fixed-spectrum odd cap estimate, a nodal stable expansion, or a geometric-sector asymptotic to a full knot-volume theorem.

The private nodal research was frozen separately in `md-physical-fold-nodal-stable-jets-and-mass.md` and its dependency record. It includes the actual stable maximal physical fold at both parities and polynomial stable atomic mass for central values and first normals; it explicitly leaves rank-tail concentration and filling cancellation open. It is not a premise of the public formal or manuscript conclusions audited here.
