# Semantic addendum: canonical products and the manuscript dependency map

Read-only review, 1 November 2026. I read the complete `MonicProduct.lean`, the relevant imported remainder/uniqueness definitions, the new Appendix N proposition `prop:canonical-remainder-products` (lines 200–256), and the complete dependency manifest and Python checker. I did not rerun Lean or the Python checker and did not edit public files.

## Product formalization

No mathematical correction is needed in the inspected formal statements or the new proposition.

`polyMul` is actual multiplication of ascending coefficient lists: the recursion is `a g + X (f g)`. It is not a supplied quotient operation or an oracle whose compatibility is assumed. The module proves its coefficientwise congruence, commutativity, distributivity, scalar behavior, shift identity and associativity. Trailing zeros are handled through `CoeffEq`; canonical remainders have fixed length equal to the number of roots, so coefficient equality can legitimately be upgraded to equality of their lists.

The key bridge is `polyMul_monicMultiple_left`. Multiplication of a polynomial by the explicitly constructed product of linear factors remains that same monic multiple after multiplication by a second polynomial. The proof uses `polyMul_timesLinear_left` inductively. Then `monicRemainder_mul_reduce_left` constructs the exact polynomial decomposition from the existing synthetic-division identity and applies remainder uniqueness. Thus no hypothesis of the form “multiplication respects the quotient” has been assumed to prove the quotient law. The right and two-factor reduction laws follow from the proved product properties.

`quotientProduct` is literally ordinary multiplication followed by the canonical remainder. Its associative law reduces both sides to the same actual three-factor product. `canonicalProduct` starts from the remainder of the unit polynomial and reduces after each multiplication. `monicRemainder_product` proves equality with reducing the unreduced finite product once, and `newtonFunctional_product` takes the actual coefficient in degree `roots.length-1`. This is the base coefficient functional, not a declaration that the functional is multiplicative. The manuscript expressly states that it generally is not multiplicative.

There is no bound on the unreduced factor or product degrees, no distinct-root condition, and no field or division assumption. The coefficient ring is a commutative ring. The Lean definitions also handle an empty root list with zero remainder; the manuscript proposition inherits its earlier nonempty modulus hypothesis, so its top-coefficient notation has its usual meaning. Extra hypotheses are not being hidden in padding or list length.

The repeated-node statements preserve actual formal derivatives. `formalDerivativeValue_polyMul` establishes the Leibniz rule for the constructed product. `double_root_product_remainder` then gives the full degree-one remainder modulo `(X-r)^2`. More importantly, `monicRemainder_double_head_derivative` proves derivative preservation for a root list `r :: r :: roots` with an arbitrary additional list. It uses the synthetic divided difference at the repeated node, rather than replacing the modulus by only two roots. The previously proved root-permutation invariance allows any two occurrences of r to be placed first. Repetitions among the additional roots cause no problem; no reciprocal root differences are used. The manuscript's assertion for a node occurring at least twice is therefore supported, including with extra roots.

The physical limitations remain explicit. These lemmas do not identify the Chebyshev modulus, prove the original Casimir relation, or identify an arbitrary crossing multiplier with the base coefficient functional. Appendix N lines 248–256 retains those requirements. For a weighted functional one must still form the actual multiplier times the source and retain its Hermite values and derivatives. The newly proved product law does not supply that physical identification by itself.

## Structural dependency checker

The checker accurately describes itself as a consistency check of a **manually supplied** proof map. It checks file/anchor existence, stated role compatibility, the six declared roles for a full-volume conclusion, acyclicity, propagation of assumptions and unresolved inputs, and the exclusion of odd-only premises from all-level conclusions. Memoization does not bypass the cycle check: stack membership is tested first. Open obligations and odd-level scope propagate through intermediate nodes. The seven negative controls alter these actual structures and require rejection.

It neither parses the mathematical meaning of an anchor nor derives whether a written proof is correct or complete. In particular, a manually mislabeled `written` node or an omitted internal hypothesis could pass; the result's `meaning` field and module docstring state this limitation. The manifest also says that it does not enumerate every internal lemma or external source. Its declaration that the general remainder and general full-volume theorem remain open is preserved and propagated into the corresponding conclusion. It does not mistake the central contribution or a one-cap estimate for a full-remainder proof.

Two concrete precision issues were found and reported to the parent; both are corrected in the snapshot hashed below:

- `filling_norm` originally pointed to `uf:eq-2`, which is the stronger vanishing-node estimate. It now points to `uf:eq-3`, whose empty specified set gives the stated full tensor norm.
- `long_twists` originally said that each signed filling integer exceeded a threshold. It now says that each **absolute value** exceeds it and that signs are independent.

These were declaration/reference repairs, not missing proofs of the norm or long-filling theorem. The fact that the wrong but existing anchor passed the structural checks illustrates why their output must not be described as mathematical certification.

No remaining defect was found in the inspected product logic or in the checker's stated structural scope. This addendum does not certify all manuscript nodes and makes no claim that finite or machine checks establish the analytical source estimates or geometric completion.

## Exact source snapshot

- `formal/VolumeLogic/MonicProduct.lean`: `35bb1ca26172547f9bae61d2dd3161aeba8a84810768f87f29477568dd457b85`
- `formal/VolumeLogic/MonicRemainder.lean`: `f6781dba17c7677adcfe2aec41d31f8742004fc38a45be9732c24ce98b65dbfd`
- `formal/VolumeLogic/MonicUniqueness.lean`: `5b1923608c3117ba4875879310b51d56995b8548f1bc93e9491eda2238d4ab1c`
- `manuscript/sections/N-uniform-filling-bound.tex`: `a354da3d946202ae06dd656411961342f2dca8f95ec7d9257f94fb7a3eba27d8`
- `repro/manuscript_logic.json`: `c0866a203643295dbd6557766ebe8e991bd8c79fe8ec4ab212d2c20144097759`
- `repro/check_manuscript_logic.py`: `2f2450f16cbaa237c2c68636c28e8ad88c76124d5295d086ac0ab0f926f204b6`
