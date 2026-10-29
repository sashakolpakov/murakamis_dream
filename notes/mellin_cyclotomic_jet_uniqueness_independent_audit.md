# Independent audit of bounded-jet cyclotomic Mellin uniqueness

27 October 2026. The proof of
[the whole-function uniqueness theorem](mellin_cyclotomic_jet_uniqueness.md)
passes independently. Its finite X-window, uniform quantum-jet budget,
and cyclotomic numerator condition are sufficient as written. No
semisimplicity, minimal operator, or scalar-ratio hypothesis is needed.

## 1. The finite window really is closed

In the exact Fourier ordering, a monomial \(X^{-j}S^\ell\)
takes the coefficient \(w_{m+j}\) to power \(X^m\), with
factor \(Q^{\ell m}\) after the retained \(Q^{-\ell j}\).
Since \(0\le j\le d\) and \(m\le N-d\), only coefficients
through \(w_N\) enter. Hence a truncation at \(X^N\) is enough
for the entire indicated window. Negative S-powers cause no
change to this statement: they rescale the same X exponent.

Subtracting the actual truncation therefore gives precisely
\[
 \sum_{j=0}^d a_j(Q,Q^m)e_{m+j}=0
                  \quad\bmod\epsilon^{B+1}.
\]
The starting lattice sets every \(e_r\) below \(n_0\) to zero.
There is no unmentioned assumption on the X-degree of higher
quantum-normal coefficients.

## 2. The singular-step budget and truncated valuation argument

After one fixed coherent denominator clearing, \(a_d\) is
Laurent polynomial in \(Q,Y\). Its Q-span \(A\) implies
\(a_d(Q,Q^m)\ne0\) for \(m>A\): equality of two collected
exponents \(u+mv\) with different \(v\)'s would force \(m\le A\).
Its at most \(s\) remaining monomials have nonzero-root
multiplicity at most \(s-1\), by the logarithmic-derivative
Vandermonde determinant.

For all sufficiently large levels, \(a_d(Q_N,Y)\ne0\) as a
Laurent polynomial in \(Y\). The visited Y-values are distinct;
there are at most \(D\) roots on them. Thus the sum of all
leading vanishing orders through coefficient \(N\) is at most
\(B=D(s-1)\). The excluded levels include any zeros or poles
of fixed Q-scalar clearing factors and any specialization where
all Y-coefficients of \(a_d\) vanish. There are only finitely
many such root values. No uniform lower bound on their nonzero
numerical magnitudes is needed.

The truncated-ring step is valid despite zero divisors.
If \(k=B+1\), \(h=\epsilon^\mu u\) with \(u\) a unit, and
\(he\in\epsilon^tR_k\), \(t\le k\), then
\[
 e\in\epsilon^{t-\mu}R_k\qquad(t\ge\mu).
\]
The additional annihilator \(\epsilon^{k-\mu}R_k\) is
already contained in that asserted ideal. Applying this at
each step gives \(e_r\in\epsilon^{k-M_r}R_k\), so every root
coefficient through \(X^N\) agrees. In particular no singular
step was divided at its root value.

For the finitely many fixed initial colors the leading
trajectory polynomials are units at all sufficiently large
roots, as suggested in the outline. The written proof is
stronger: the total budget would handle their vanishing as
well, whenever its other hypotheses hold.

## 3. The whole pole lattice is the necessary last step

Subtracting the two cyclotomic conditions gives
\[
 H(X)=(1-X^N)(W_N-Z_N)\in\mathbb C[X],\qquad \deg H\le N .
\]
Both expansions have the same starting lattice and agree
through power \(N\). Thus every coefficient of \(H\) through
its maximal degree vanishes, proving \(W_N=Z_N\).

Simple cyclotomic poles alone would not suffice: an arbitrary
polynomial part of higher degree could remain invisible to
the finite window. The stated degree bound and prescribed
low prefix are therefore substantive source-lattice data.
The residue at infinity is then fixed, including the case
that the actual Kashaev value vanishes.

## 4. The exact actual-unknot sharpness example checks

Direct Ore multiplication gives the displayed actual operator
\[
 (T-Q)[(1-QY)T-(1-Y)].
\]
The inner bracket applied to the actual color \(1\) is
\((1-Q)Y\), which the outer factor kills. Its exact Fourier
transform is
\(X^{-2}(1-X)(1-QX)(1-S)\).
Applying this to \(X^{n_0}/(1-X)\) gives exactly the stated
finite source. The leading trajectory is \(1-Q^r\);
only \(r=N\) vanishes in the reconstruction range, and it
has multiplicity one.

The alternative root section
\(\lambda X^N/(1-X^N)\) is shift-invariant and preserves the
affine root source and all the stated root pole/prefix data.
Its residue contribution is \(+\lambda\). Its first normal
would require
\[
 (1-S_0)g_1=NUf'(U),\qquad
 f(U)=\lambda U/(1-U).
\]
The cyclic average kills the left side and gives
\(N^2Uf'(U)\ne0\) on the right for \(\lambda\ne0\).
This works in the formal Laurent field as well as the rational
field. The two required jet levels in this actual example
are therefore sharp.

The proof and the saved exact diagnostics support the stated
uniqueness theorem. They do not construct a regulator candidate
in the same pole and source lattice, establish its bounded
quantum lift, or estimate the selected residue. Those remain
the geometric comparison and volume questions.

