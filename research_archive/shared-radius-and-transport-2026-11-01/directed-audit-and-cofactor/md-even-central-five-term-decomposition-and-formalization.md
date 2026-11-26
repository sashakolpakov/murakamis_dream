# An exact five-term decomposition of the even central cofactor

This note preserves an exact algebraic reduction suggested by the
parent investigation. It does not prove the real stability or a
positive-semidefinite representation of either of the two cofactors
that appear in the reduction. Those are explicit missing hypotheses
for the proposed parity bridge.

## 1. Exact original-level identity

Let \(N=2m\ge4\), \(M=m-1\), \(\theta=\pi/N\), and retain

\[
a_j=2+2\cos((2j+1)\theta),\quad s_j=2\sin(j\theta),
\quad A=x+y,\quad P=xy.
\tag{1}
\]

The actual lower cofactors satisfy

\[
R_j(z)=z^j\prod_{r<j}a_r+s_j^2 A R_{j-1}(z)
                 +s_js_{j-1}a_{j-1}P R_{j-2}(z),
\qquad R_0=1.
\tag{2}
\]

Set \(D_z=R_M(z)\), \(E_z=a_M R_{M-1}(z)\), and continue this
same finite recurrence by **one row** to define \(T_z=R_m(z)\).
This is still the original level \(N\). The letter \(T\) here denotes
only this polynomial, not a physical quarter-turn operator.
The sine product gives
\(\prod_{r<m}a_r=2\), and \(s_m=2\). Thus

\[
T_z=2z^m+4A D_z+2s_{m-1}P E_z.
\tag{3}
\]

The actual even central polynomial, after removal of its fixed common
raw sign, is

\[
P_C=4A D_bD_c+2s_{m-1}P(D_bE_c+E_bD_c).
\tag{4}
\]

Substitution of (3), without division by any face variable, gives

\[
\boxed{
P_C=D_bT_c+T_bD_c-4A D_bD_c
                  -2b^mD_c-2c^mD_b.}
\tag{5}
\]

This identity holds on every boundary face, including \(xy=0\),
and at every zero of a cofactor. It therefore avoids solving (3) for
\(E_z\), which would introduce a spurious division by \(xy\).
Every term in (5) has degree \(2m-1=d\), exactly the original local
face degree. No endpoint term or central-skipping path is discarded.

The factor \(2\) in (3) and (5) is exact. For example, pairing the
roots of \(z^N+1\) gives
\(\prod_{r<m}4\cos^2((r+\tfrac12)\pi/N)=2\).
Equivalently evaluate the even Chebyshev product at \(-2\) and take
the positive square root of its paired factors.

## 2. Original shared targets remain in the identity

Let \(W\) be the product of all other original source factors and
let \([\boldsymbol z^{\boldsymbol t}]\) be the original shared face
coefficient extraction. Multiplying (5) by \(W\) and applying this
one linear functional is exact. The last two terms are literal
shifted targets:

\[
[\boldsymbol z^{\boldsymbol t}](b^m D_c W)
=[\boldsymbol z^{\boldsymbol t-m e_b}](D_c W),
\tag{6}
\]

and likewise for \(c\). Here \(e_b\) is the unit exponent vector
of the actual face \(b\). A coefficient with a negative demanded
exponent is zero. If \(b\) is a retained boundary variable rather
than an extracted face, its factor \(b^m\) simply remains in the
resulting boundary polynomial. If \(b\) is a protected zero face,
that term vanishes. These are the ordinary rules of the original
coefficient extraction, not alternative comparison targets.

For a fixed exterior containing \(r\) even central coupons, expansion
of (5) at all of them gives at most \(5^r\) signed terms before the
same extraction. This number is independent of \(N\), while \(r\)
is fixed by the original diagram. Keeping the signed sum is exact.
Taking absolute values of the extracted terms is a proposed upper
bound and requires a rate estimate for each of those actual terms.

## 3. What a stable decomposition would require

Suppose one could prove, at every relevant level, that both
\(D_z=R_{m-1}(z;x,y)\) and \(T_z=R_m(z;x,y)\) are real stable
in their three face variables, with their original positive
coefficients. Then each of the five unsigned summands in (5) would
be a product of stable polynomials, linear factors, and monomials.
Products, nonnegative real boundary specialization, and the original
face coefficient extraction would make every resulting boundary
polynomial stable or zero. Formula (6) would retain the collapsed-row
demand shifts explicitly.

This would reduce the even problem to finitely many stable boundary
polynomials. It would **not yet** give the required absolute source
rate. One must still identify the positive boundary pressures and
responses of those terms, and control the two monomial terms by their
actual collapsed-row source geometry or another valid estimate.
In particular, a bound measured relative to the complete central
pressure cannot simply be assigned to a term with shifted targets.

At present the all-level stability hypothesis in the preceding
paragraph is unproved. The existing exact counterexample for
\(D+tE\) does not decide it, and neither does the obstruction in
`md-even-cofactor-unbounded-nonreal-root-obstruction.md`: that result
concerns the shorter \(E\). Low-level root checks also do not prove
the hypothesis. No PSD representation or even negative-axis theorem
is asserted here.

## 4. A useful finite formalization target

The publication checkout currently uses
`formal/VolumeLogic/FiniteAlgebra.lean` and
`formal/VolumeLogic/FiniteSupport.lean`, rather than files named
`VolumeProofLogic*.lean`. These use Lean's standard library with no
Mathlib dependency. They already prove a division-free divided
difference, the cleared double-root identity, product subtraction,
and the parity-specific support cutoffs. They do not yet connect
the actual path weights to the central cofactor factorization.

Proving only that substitution of (3) turns (4) into (5) would be a
short ring calculation with the important source content supplied as
hypotheses. A more useful next finite theorem is the **three-path
central-cut identity**, from which (4) and then (5) follow:

1. Define a decreasing path whose steps have length one or two.
   A length-one step ending at row \(r-1\) has weight \(p_r\).
   A length-two step from \(r\) to \(r-2\) has weight \(t_r\)
   and retains the unused diagonal \(a_{r-1}\).
2. Define its cleared weight by multiplying all unused diagonal rows,
   including the prefix below its end and the suffix above its start.
   The middle monomial is the actual \(b^i c^{d-j}\).
3. For an even central path \(i<m\le j\), prove that the unique step
   crossing the cut is exactly one of
   \(m\to m-1\), \(m+1\to m-1\), or \(m\to m-2\).
   Splitting there is a bijection with two lower-block paths, after
   the original row reflection on the upper side.
4. Under the literal reflected weights, summing this bijection proves

\[
\sum_{i<m\le j}b^ic^{d-j}
 \left(\prod_{r<i}a_r\right)
 \left(\prod_{r>j}a_r\right)K_{i,j}
=p_mD_bD_c+t_m(D_bE_c+E_bD_c).
\tag{7}
\]

Here \(K_{i,j}\) is the internal path sum, with the skipped-row
diagonal included, and the reflection hypotheses identify the
two length-two central weights. In the actual source
\(p_m=4(x+y)\) and \(t_m=2s_{m-1}xy\).

This is a finite identity over an arbitrary commutative ring and
uses no inverse of any \(a_r\). It therefore remains valid on the
singular spectral rows that matter to the original source. It can
be implemented with list-indexed finite sums and recursive path
weights in the existing standard-library setup; a polynomial library
is not needed to prove the identity after evaluation at arbitrary
\(b,c\). A later coefficient-convolution lemma would connect it to
(6). This is a proposed next formalization target, not a claimed
Lean proof or a source stability assertion.

## 5. Status and dependencies

Equations (3)–(6) are proved exact identities. Equation (7) is the
existing written unique-crossing-path argument recast as a precise
formalization target. The analytic parity bridge is open because
the stability and rate inputs in Section 3 are not established.

The source dependencies and hashes are the same as those recorded in
the companion hard-edge obstruction note. The formal files were read
only; no repository file, formal declaration, or public theorem was
changed during this investigation.
