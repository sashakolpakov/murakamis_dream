# Coefficient reduction at repeated spectral roots

This record concerns the finite algebra added after the first manuscript
review. The implemented statements are in
[MonicRemainder.lean](../../formal/VolumeLogic/MonicRemainder.lean).
The [formal check report](../results/proof-logic/summary.json) records the
exact source hashes and the logical dependencies reported by Lean.

The mathematical issue is that a repeated spectral root must retain its
nilpotent, or first-derivative, contribution. Treating all spectral roots
as distinct evaluation points would change the functional. The earlier
formal file checked a cleared double-root identity after the value and
derivative relations had been supplied as hypotheses. The new module
constructs polynomial reduction itself.

## The construction and its statements

A polynomial is a list of coefficients in ascending powers. Lists with
different numbers of trailing zeros may represent the same polynomial;
`CoeffEq` means equality of every coefficient. Thus the division theorem
is a formal polynomial identity, not an inference from equality of values
at a finite set of points.

For a scalar \(r\), synthetic division constructs the coefficient list of
\((f(X)-f(r))/(X-r)\) without using division in the coefficient ring.
The reconstruction identity is proved directly from the list recursion.
For an ordered list \(r_1,\ldots,r_n\), the algorithm repeats this step
and reconstructs a remainder in ordinary monomial coordinates. It proves

\[
 f(X)=\prod_{i=1}^n(X-r_i)\,q(X)+\operatorname{rem}f(X),
 \qquad [X^k]\operatorname{rem}f=0\quad(k\ge n).
\]

The modulus is constructed by multiplying the linear factors, and its
coefficient at degree \(n\) is proved to be one. No factorization is
assumed in place of that construction. The separate application to the
actual spectral polynomial must prove its factorization into those
specified factors.

The top coefficient of the remainder equals the iterated synthetic
divided difference. The module also proves that reducing a multiple of
the modulus gives zero. Its reduced-input normalization theorem uses the
representation hypothesis `f.length ≤ roots.length`; trailing zeros count
toward this length. This is a sufficient way to present a polynomial of
degree below \(n\), not a formal theorem for every padded presentation of
such a polynomial.

For two coincident nodes the full remainder is proved to be

\[
 \operatorname{rem}_{(X-r)^2}f(X)=f(r)+f'(r)(X-r).
\]

Here the prime denotes formal differentiation, defined by its Horner
recursion. The derivative term is a conclusion of the reduction theorem.
No distinctness hypothesis or inverse root difference occurs.
The top-coefficient functional is not the ordinary trace of polynomial
multiplication. It contains no quantum-source scalar or sign normalization.

## Boundaries of the formal result

All statements use a commutative coefficient ring. This includes the
zero ring; a literal coefficient equal to one does not assert a nonzero
polynomial in that ring. The intended spectral application is over
\(\mathbb C\). For the empty root list the remainder and the Newton
functional are defined to be zero; the intended modulus has positive
degree.

The module does not prove the actual Chebyshev root list, its trigonometric
values or multiplicities, the crossing matrix's annihilating polynomial,
the prescribed normalization of its Hermite trace, or the passage from
that matrix calculation to the marked knot invariant. It also proves no
analytic norm, stationary-phase statement, or volume identity.
The later [linearity module](../../formal/VolumeLogic/MonicLinearity.lean)
closes two of the original gaps: coefficient-equivalent padding and
linearity of the constructed operations. Its proof first identifies
each synthetic-quotient coefficient as the Horner value of the
corresponding tail of the input list. Coefficient equality therefore
passes through synthetic division. Induction over the root list gives
literal equality of the reconstructed remainder lists. Addition and
scalar multiplication then pass through the same recursion.

Together with the existing theorem that a monic multiple reduces to
zero, these results prove

\[
 f=g+pq\quad\Longrightarrow\quad
 \operatorname{rem}_p f=\operatorname{rem}_p g,\qquad
 \mathcal L_p(f)=\mathcal L_p(g),
\]

where \(\mathcal L_p\) is the top-coefficient functional already
constructed. The equality in the hypothesis is coefficientwise, and
\(pq\) is obtained by multiplying by the actual split monic factors.
It is not a presumed quotient relation replacing the reduction proof.
The module adds 24 declarations, including the supporting coefficient
lemmas. They allow repeated and empty root lists and arbitrary
commutative rings. It does not yet introduce an abstract quotient-ring
type or give the general confluent root-sum formula. Root reordering
and uniqueness are now handled by the subsequent
[uniqueness module and its reading record](monic-uniqueness.md).

The reproduction runner inspects all theorem declarations, including
ones with a `simp` attribute on the same line. A clean build alone is
insufficient: the separate axiom report must contain every declaration,
with no additional axiom beyond the permitted foundations. The runner's
source and the exact compiled files are included in the saved report.
