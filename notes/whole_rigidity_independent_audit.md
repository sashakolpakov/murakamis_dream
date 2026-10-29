# Independent check of the whole-comparison rigidity arguments

Audit, 27 October 2026. I checked the proofs in
[whole-period rigidity](whole_period_cyclotomic_rigidity.md) and
[cyclotomic divisor descent](cyclotomic_divisor_descent.md), including
their stated hypotheses, without importing a published q-curvature
theorem. No counterexample to the stated reconstruction, bounded
comparison, or divisor-descent theorems was found.

## 1. Finite reconstruction and algebraic norms

The rectangular jet identity is correct. After the power substitution,
the two exponent lists are a+Nb and c+Nd. The strict bounds on N
separate these lists. The two Vandermonde matrices and the diagonal
q_N-power matrix are invertible, and interpolation at D+1 distinct
values of 1/N kills every coefficient. No number-field degree bound
for q_N is needed.

The algebraic-norm extension is valid for the stated finite free
integral algebra and a regular element. At a selected etale place,
one may first extend the residue field to its separable closure;
the chosen formal branch then splits off as a rank-one factor.
The norm is its product with the regular complementary determinant,
so vanishing in a rectangular Artin jet quotient passes to the norm.
Nonzero field elements have nonzero norms. This does not extend the
argument to arbitrary independently chosen root-level covers.

## 2. Bounded-comparison existence

The rank-minor argument is valid for the explicitly supplied affine
linear system over F=k(q,t,v). A jet solution kills the augmented
minors to the required order. Fixed support and degree bounds then
make them zero identically. A nonzero generic-rank minor survives as
a whole q-germ at one of the tested levels. Its sparse multiplicity
bound makes its inverse's pole order strictly smaller than the jet
budget, so exact pivot repair preserves the invertible leading map.

This exact specialized solution lies in the specialization of the
generic affine solution family: the selected pivot remains nonzero
over the Laurent-series field, so the rank has not dropped there.
Consequently the generic determinant polynomial is nonzero, and the
infinite coefficient field supplies an invertible rational member.
For rank zero, the minors force b=0 and the invertible test member
shows that the proposed matrix space has a nonzero determinant
polynomial. This also proves the stated rank-zero conclusion.

The restrictions in the note are material. The finite system must
really be coefficientwise; a test at one algebraic place does not
by itself prove coefficientwise equality in an algebraic basis.
Candidate denominators must be regular units in the chosen test
charts. The q-connection equation involves derivatives of unknown
coefficients and is not included in the finite affine system.
The later cyclic-source lemma correctly supplies a sufficient
condition for that additional compatibility.

## 3. Moving algebraic divisors and rational descent

The exponential-sequence independence lemma is correct. At the
largest modulus and least Laurent order, Cesaro orthogonality of
distinct unit-circle phases kills every alleged nonzero leading
coefficient. This includes root-of-unity phase ratios because the
identity holds at every sufficiently large integer.

Under the finite nonresonance condition, the first d power sums
separate the limiting-root groups. Padding to d elements with zero
then makes Newton identities sufficient even before the group sizes
are known equal. All actual germs are units, so the padded zeroes
are distinguished and the group sizes agree. Equality of the paired
exponentials forces a constant integral logarithmic difference and
therefore the claimed q^(2k) ratio. The half-root convention and
the derivative formula for k are consistent.

The gauge constructed over the splitting field descends rationally.
There is also a short alternative justification for that final step.
Remove its Y^(k_0) part and normalize the product gauge f_0 at Y=0
to one. For any splitting-field Galois automorphism tau, both f_0
and tau(f_0) have the same sigma-coboundary. Their quotient is a
sigma-invariant rational function of Y and hence a coefficient-field
constant. Its value at Y=0 is one, so tau(f_0)=f_0. This proves the
descent without any additional choice of branch pairings.

The explicit half-root alias coefficient is a genuine obstruction
to dropping the divisor/parameter hypotheses. Its transport is
identity at every selected q_N, while its q=1 value prevents a
generic rational coboundary. Thus the printed scope qualifications
are necessary and do not merely reflect missing estimates.

## 4. Verification and limit of the audit

Both diagnostic scripts were rerun. They verify their claimed exact
finite checks; these are validation of formulas, not a replacement
for the uniform arguments above. No actual/geometric knot-period
comparison, integral-lattice extension at every polar chart, or
volume-conjecture proof is established by this audit.
