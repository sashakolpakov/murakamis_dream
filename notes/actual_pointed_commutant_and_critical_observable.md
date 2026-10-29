# The actual pointed commutant is scalar on its selected Mellin state

Research obstruction and constructive formal adapter, 27 October 2026.
The canonical actual Mellin companion cannot directly provide a
nontrivial irreducible critical-field observable through an endomorphism
which commutes with whole quantum transport and preserves its source
lattice. Such endomorphisms have a scalar character on the selected
state. A concrete critical observable instead exists on the actual
partial Gaussian insertion module; it has a covariant, rather than
horizontal, transport rule.

No geometric candidate for the final selected cyclotomic residue is
constructed here. The distinction identifies a necessary change of
object before applying the critical trace nonvanishing theorem.

## 1. The entire admissible horizontal lattice is one-dimensional

Use the original [actual Mellin source](fourier_mellin_actual_source.md),
with F=k(Q,X), R=k(Q)[[X]], sigma(X)=QX, and Q an indeterminate:

\[
 AZ=B\ne0,\qquad Z\in X^{n_0}R,\qquad
 \widehat A=(S-\sigma(B)/B)A.
\]

All fixed left-shift conventions, source coefficients and finite color
pointing are those of that construction. Its exact affine equation
has exactly one solution in this lattice. Let d be the order of
\(\widehat A\), C its forward companion, \(T=C^{-1}\sigma\),
\(v=J_dZ\), and \(\ell J_df=Af/B\).

If \(w\in k(Q)((X))^d\) satisfies \(Tw=w\), the companion's first
rows force \(w=J_dW\) for its first component W. If also
\(W\in X^{n_0}R\), then

\[
 h=\ell w=AW/B,\qquad \sigma h=h.
\]

The sigma invariants of k(Q)((X)) are exactly k(Q): its coefficient
of X^j satisfies \((Q^j-1)h_j=0\), which forces h_j=0 for j!=0.
Thus h=c(Q). The source-lattice uniqueness gives

\[
                         W=c(Q)Z,\qquad w=c(Q)v.      \tag{1.1}
\]

No minimal-annihilator, semisimplicity or rationality of Z is assumed.
This statement concerns the supplied homogeneous SOURCE object and
its lattice, not arbitrary solutions in a larger formal lattice.

## 2. A whole admissible endomorphism has a scalar character

Let Theta be an F-linear companion endomorphism with

\[
                         \Theta T=T\Theta.             \tag{2.1}
\]

Require that Theta preserves the specified formal source lattice,
or just that the first component of Theta v lies in X^(n_0)R.
For instance a matrix regular at X=0 preserves X^(n_0)R^d and
has this property. Rational poles at X=0 do NOT automatically
preserve it; the actual lattice condition must be checked.

The vector Theta v is horizontal. Equation (1.1) therefore gives

\[
                       \Theta v=\chi(\Theta)v,
                 \qquad \chi(\Theta)\in k(Q).         \tag{2.2}
\]

On the algebra of lattice-preserving endomorphisms, chi is a unital
algebra character. It is exactly computable by

\[
              \chi(\Theta)=[X^0]\,\ell\Theta J_dZ.      \tag{2.3}
\]

Only finitely many fixed color coefficients enter this constant
coefficient for a fixed rational Theta. Thus this is a consequence
of the ACTUAL finite pointing, not an unmarked eigenvalue choice.

In particular Theta cannot satisfy an irreducible polynomial
\(p(z)\in F[z]\) of degree greater than one: applying p(Theta) to
v gives p(chi(Theta))=0, a rational root of that polynomial.
Hence the full actual pointed companion does not carry the
irreducible critical observable proposed in
[the critical trace theorem](irreducible_critical_source_and_whole_norm.md)
through such an admissible horizontal endomorphism.

The same obstruction is visible in exact moments:

\[
             \ell\Theta^jv=\chi(\Theta)^j,\qquad
             \operatorname{rank}(m_{i+j})_{i,j}=1.     \tag{2.4}
\]

At any admissible root, monodromy H_0 itself satisfies H_0v_0=v_0,
so \(\ell_0H_0^jv_0=1\). Functional calculus of that monodromy sees
only this source-one direction, regardless of the other spectrum.
It cannot manufacture higher critical moments or identify its
characteristic polynomial with the classical A-polynomial.

Neither (2.2) nor (2.4) proves that the knot has no geometric period
quotient. They exclude this particular construction on the raw
pointed object. Endomorphisms which do not preserve the lattice,
root-only operators without a whole lift, relative correspondences,
and observables with a nonzero covariant derivative are different
objects.

## 3. Actual inserted partial moments provide a different observable

There is a concrete associated-graded adapter before final framing
contraction. Use the ACTUAL two-index partial family and nondegenerate
transverse formal contraction of
[the partial support theorem](partial_geometric_support_theorem.md).
Keep both framing indices external and the full base, cut, pivot,
half-density and peripheral normalization lines. Put H=Log Q.

Let F_0 be the rational function field of the external meridian and
framing variables on the marked chart, and K/F_0 its finite separable
geometric critical field, of degree d. Keep any Gaussian line separate
from K; a square-root sign is not an extra critical point. The field
K is generated by the critical values of the actual internal flow
monomials z_i=Q^(j_i). A fixed rational linear combination
\(\theta=\sum c_i z_i\) can be chosen primitive: each pair of distinct
embeddings excludes one proper linear hyperplane of choices c, and
there are finitely many pairs.

The insertions theta^j, 0<=j<d, are literal finite sums of monomial
weights on the SAME finite array. They change no underlying invariant
or selected source. Their unweighted member j=0 is the original
partial array. Let G_sigma be its transverse formal contraction at
the conjugate critical place sigma and form

\[
 M_{\sigma,j}(H)=
       \frac{G_\sigma(\theta^j I)}{G_\sigma(I)},
       \quad 0\le j<d.                               \tag{3.1}
\]

The denominator is nonzero by the actual transverse support theorem.
The common exponential and base line cancel in this ratio. Termwise
formal Gaussian contraction gives algebraic coefficients and

\[
 M_{\sigma,j}=\sigma(\theta)^j+O(H).                 \tag{3.2}
\]

Thus M is a unit matrix over the normal closure's formal H-ring:
its leading determinant is the nonzero Vandermonde. Define

\[
 D_\theta=\operatorname{diag}(\sigma\theta),\qquad
        \Theta_H=M^{-1}D_\theta M.                    \tag{3.3}
\]

This is an explicit formula from d actual inserted partial moments,
at every formal order. Galois conjugation permutes both the rows of
M and the entries of D_theta, so Theta_H descends to F_0[[H]].
It satisfies the exact irreducible critical relation

\[
                         p(\Theta_H)=0,               \tag{3.4}
\]

where p is the minimal polynomial of theta. Its leading operator is
multiplication by theta in the power basis. The distinguished source
e_0 has M e_0=(1,...,1)^t; it has not been replaced by a favored
critical point. The matrix in (3.3) is a completed formal insertion
operator, not an actual finite-N companion endomorphism or a claim
that the raw multiplication theta commutes with quantum integration.
Generally Theta_H e_0 is NOT e_1: the raw first insertion column is
sigma(theta)+O(H), while M Theta_H e_0 is exactly sigma(theta).
Powers of Theta_H therefore correspond to explicitly renormalized
combinations of insertion columns, including their formal
counterterms, rather than to the uncorrected higher raw moments.

## 4. Its covariant rule explains the escape from the obstruction

Let delta be the external meridian derivation, extended uniquely to
the separable critical field. In the normalized branch frame the
insertion connection is ordinary differentiation. In the actual
moment frame it is

\[
               \nabla=M^{-1}\delta M
                      =\delta+M^{-1}(\delta M).
\]

Its commutator with the critical observable is exactly

\[
 [\nabla,\Theta_H]
          =M^{-1}\operatorname{diag}(\delta\sigma\theta)M.
                                                               \tag{4.1}
\]

The analogous formal meridian difference rule uses the actual
transverse block ratios b_sigma=T G_sigma(I)/G_sigma(I), already
constructed in the partial support theorem. In branch coordinates
transport is diag(b_sigma) sigma_H. Pulling this back by M gives
the exact conjugation rule

\[
 \mathcal T_H\Theta_H\mathcal T_H^{-1}
           =M^{-1}\operatorname{diag}(\sigma_H(\sigma\theta))M.
                                                               \tag{4.2}
\]

Equations (4.1)--(4.2) are Leibniz/covariant laws, not the zero
commutator (2.1). If theta varies on the geometric branch, the
commutator (4.1) and the conjugation DIFFERENCE
T_H Theta_H T_H^(-1)-Theta_H in (4.2) are nonzero. In addition the coefficient field and
lattice are those of the completed critical insertion module, not
the original formal X-lattice. Both changes are essential.

This constructs the correct formal shape observable from actual
insertions rather than guessing an extra monodromy eigenvalue.
It still leaves an explicit gap: the final finite two-index
co-source, its endpoint carries and logarithmic moments have not
been mapped to the trace pairing on this insertion module. Hence
(3.3) gives no selected critical trace weight or global volume norm.
The exact boundary currents in the full certificate must still be
transported through that map. No q^N, M^N, parity, or peripheral
factor has been discarded in making the partial formal adapter.

## 5. The raw actual compact co-source has infinite moment rank

There is a second concrete obstruction to extracting a finite critical
field directly from the unmodified cut. The exact
[actual centralizer Toeplitz row](centralizer_normal_residue_and_actual_cut_moments.md)
has on the identity insertion the moments

\[
 \mu(b^h)=\frac1N\sum_{j=0}^{N-1}
          (-1)^h\frac{(j+1)^{\overline h}}{(N+1)^{\overline h}}
              =\frac{(-1)^h}{h+1}.                  \tag{5.1}
\]

The equality follows by summing
(j+1)^(rising h)=h! binom(j+h,h). These moments are the same at
EVERY N and equal the integral of (-T)^h on 0<=T<=1. Every finite
Hankel matrix (mu(b^(i+j))) is nonsingular: after removing the
alternating signs its quadratic form is

\[
                \int_0^1|\sum_i c_iT^i|^2dT>0
\]

for a nonzero coefficient vector. Thus this raw co-source cannot
factor through any finite algebra k[b]/p with nonzero p. Such a
factorization would force mu(p q)=0 for every polynomial q; taking
q to have the conjugate coefficients gives a strictly positive
integral. The same argument can be made after any generic complex
specialization of the remaining rational parameters.

This is compatible with the finite matrix size: the actual Toeplitz
maps T_N(b^h) are NOT powers of T_N(b). Their multiplication is a
star product. Consequently a finite initial trace-Gram calculation
does not certify a polynomial relation for the raw b insertion.
The full relation moments must be proved after the proposed
action-normalized or relative reduction. The renormalized observable
in Section 3 and the raw compact coordinate are different objects.
