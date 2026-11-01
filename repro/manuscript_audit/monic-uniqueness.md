# Canonical remainders and the order of spectral roots

This reading concerns the algebra underlying Appendix N's finite
functional. It extends the [earlier reduction record](monic-remainder.md).
The new implementation is
[MonicUniqueness.lean](../../formal/VolumeLogic/MonicUniqueness.lean),
and the manuscript now includes a proposition with the same mathematical
content before specializing to the Chebyshev roots. The reproduction
[report](../results/proof-logic/summary.json) records the compiled sources
and each theorem's logical dependencies.

## The issue being checked

Synthetic division uses an ordered list of roots. The spectral
functional, however, should depend on the polynomial, rather than the
order chosen to list its roots. This needs a proof when roots repeat:
arguments that divide by every pairwise root difference would exclude
the actual spectral polynomial. There is a separate representation
issue because the implementation allows trailing zero coefficients.

The new proofs handle both issues over any commutative coefficient
ring. They introduce no assumption that the roots are distinct.

## The formal implication

Let \(p(X)=\prod_{i=1}^m(X-r_i)\). The preceding modules already
constructed \(\mathcal R_p f\), proved a coefficientwise identity
\(f=pq+\mathcal R_p f\), and showed that reduction is linear and
annihilates multiples of \(p\).

Suppose another decomposition is supplied:

\[
 f=pq_1+r,\qquad [X^k]r=0\quad(k\ge m).
\]

Applying the constructed reduction gives
\(\mathcal R_p f=\mathcal R_p r=r\). The first equality uses
annihilation of the actual constructed multiple. The second uses the
coefficientwise degree bound. To accommodate padding, the formal proof
first truncates the list at degree \(m\), proves coefficient equality
with that truncation, and applies the earlier reduced-input theorem.
Thus list length is no longer an additional restriction on the input
representation.

The proof of permutation invariance has two steps. First, multiplication
by \((X-r)(X-s)\) is proved coefficientwise to commute, using ring
arithmetic. Induction on a list permutation then proves equality of the
two modulus-multiplication operations. Second, the remainder constructed
in the new order satisfies the old order's reconstruction identity and
degree bound. Uniqueness identifies the remainders. Since their output
lists have the same fixed length, this is literal list equality as well
as coefficient equality. Their coefficients in degree \(m-1\), and
hence their confluent divided-difference functionals, agree.

The module also proves idempotence and gives the following
characterization. A candidate functional on coefficient lists agrees
with the constructed one if it:

1. respects coefficient equality;
2. is additive;
3. vanishes on every polynomial obtained by multiplying by \(p\);
4. equals \([X^{m-1}]\) on every polynomial represented in degree below
   \(m\).

These are hypotheses, quantified over all relevant polynomials. Applying
the candidate to the proved division identity establishes the
conclusion. The characterization does not establish those hypotheses
for a candidate coming from a knot operator.

## Scope

The module adds 15 theorems, including the coefficient and truncation
lemmas used above. The library and separate axiom inspection compile
them without admitted steps. No numerical samples enter these proofs.

The manuscript's proof uses the familiar leading-coefficient argument
for uniqueness of division by a monic polynomial. The Lean proof instead
uses the previously constructed reduction operator. Both prove the
stated uniqueness; the formal proof does not assume it as a parameter.

The actual Chebyshev factorization, its repeated-root multiplicities,
the original Casimir relation, the full Hermite residue formula, and
the crossing and framing conventions still need their own proofs in
the application. This extension does not formalize a matrix spectral
decomposition, a uniform analytic estimate, or a volume theorem. It
also does not yet construct an abstract quotient-ring type. It proves
the needed representative invariance directly on coefficient lists.
