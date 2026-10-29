# Independent audit of the irregular Rees cyclic bridge

Audit, 27 October 2026. The proof in
[irregular_rees_full_cyclic_module.md](irregular_rees_full_cyclic_module.md)
is sound. I checked its operator order, wrap sign, centers,
Casimir, dense-chart coverage, transformed source and pivot.
No test rerun was needed. The Green moment/source formulas
audited in section 5 below are consistent with it.

## 1. The genuine block operators and the regularized wraps

On \(u^r/r!\), the wrap
\[
 B(MD_{Z^{-1}}-M^{-1})
\]
has coefficient \(MZ^{-r}-M^{-1}\) into block \(r-1\).
Reversing the displayed order would change that coefficient.
Similarly
\[
 T\frac{1-Z^{L+1}}{L+1}
\]
has the required coefficient \(1-Z^{r+1}\) into block \(r+1\).
The integral expression in the proof is exactly the same
operator, not a convergence approximation.

For \(d=N(Z-1)\), the scalar conjugation gives
\[
 G^{-1}D_ZG=e^{u/N}D_Z,\quad
 G^{-1}D_{Z^{-1}}G=e^{-u/(NZ)}D_{Z^{-1}},\quad
 G^{-1}BG=B+1/d.
\]
The head factors \(\eta^j\), followed by the Hopf scaling,
cancel on the nonwrap entries. They give \(d\) on the
\(E\)-wrap and \(d^{-1}\) on the \(F\)-wrap. Consequently
the \(E\)-wrap is exactly
\[
 (1+d\partial_u)
       [Me^{-u/(NZ)}D_{Z^{-1}}-M^{-1}],
\]
with that order. In the \(F\)-wrap, \(x=1+(Z-1)t\) reverses
the original integral endpoints and gives the negative sign
\[
 -\frac uN\int_0^1 e^{tu/N}f((1+(Z-1)t)u)\,dt.
\]
Both are regular coefficientwise. Its root value is \(1-y\),
\(y=e^{u/N}\), including the regular value at \(u=0\).

The completion convention is appropriate: \(G\) belongs to
the \(u\)-adic completion with Laurent \(\eta\)-coefficients,
not to a ring requiring one pole bound for its entire series.
The regular operator lattice and the irregular selected source
are therefore genuinely different objects.

## 2. Exact root centers, Casimir, and coverage

Multiplying the \(N\) cyclic arrows gives
\[
 K^N=\gamma M^N/U,\quad
 \mathcal E^N=\gamma(M^N/U-M^{-N}),\quad
 F^N=1-U,\qquad \gamma=(-1)^{N+1}.
\]
Their product is precisely
\[
 ef=k+k^{-1}-\gamma(M^N+M^{-N}).
\]
Adjacent products, or the unchanged generic Casimir, give
\(F\mathcal E+qK+q^{-1}K^{-1}=-M-M^{-1}\).
All signs agree with these formulas.

For \(U\ne1\), the cyclic \(F\)-arrows are units; distinct
clock projectors and those arrows generate every matrix unit.
Given \(k_t,e_t,f_t\ne0\) satisfying the central equation,
the displayed \(U=\gamma M^N/k_t\) fixes \(k\).
The unscaled \(e_0,f_0\) satisfy \(e_0f_0=e_tf_t\), so both
are nonzero. The root \(\lambda^N=e_t/e_0\) fixes \(e\),
and its inverse scaling fixes \(f\) automatically.
This proves dense full fixed-Casimir module coverage on
the stated cover, not coverage of a selected knot source.

At \(U=1\) and generic \(M\), the wrap is \(\kappa\):
this is the E-semicyclic fiber \(s=1\), rather than the
nilpotent head \(s=0\). They coincide at \(M=1\).
This distinction is essential and is retained.

## 3. The original source and its ramified flags

Since \(\pi_0G=\pi_0\), transforming the actual source pair gives
\[
 \psi_{\rm new}=D_{\rm head}e^{-u/d}\psi,\qquad
 \phi_{\rm new}=\phi D_{\rm head}^{-1}\pi_0.
\]
Their pairing is one. The corresponding coupon has
entries \(\eta^{i-j}e^{-u/d}/N\) followed by evaluation at zero.
Its \(u^h\) term has worst pole \(\eta^{-Nh-(N-1)}\),
exactly the stated bound. It remains idempotent, but is
not a regular source on the limiting lattice.

The coefficientwise head projector commutes with the scalar
exponential; the finite vacuum coupon does not. The proof
correctly preserves that distinction instead of inferring
source regularity from unchanged vacuum normalization.

## 4. The literal pivot and the actual scope

Conjugation preserves the literal identity \(g=K^{1-N}\).
The regular root clock therefore selects
\[
 g_{\rm lit}=U g_{\rm red},\qquad
 g_{\rm red}=x^{1-N}A^{-1}.
\]
The paired inverse defect has the opposite \(U^{-1}\)
factor. This agrees with the revised Mellin source adapters
and does not identify their separate normal derivatives.

The proof supplies a genuine full-cyclic module limit and
an explicitly irregular marked source. It does not claim
regularity of a conjugated \(R\)-network, survival of that
source in the limit, or a geometric regulator norm.
Those scope statements are mathematically necessary.

## 5. Additional check of the bounded Green moment/source formulas

[green_moment_carry_filtration.md](green_moment_carry_filtration.md)
also passes a direct formula check:

- The Newton carry is \((I+L)\otimes C-I\); retaining \(C-I\)
  gives the stated triangular complex and power expansion.
- The actual index operator is \(j+NTB\).
  Newton interpolation and
  \(\binom{TB}{m}e^{st}=(st)^me^{st}/m!\)
  give the exact bounded conversion, including the extra
  \(Nx\) in the image of the squared index.
- Differentiating the relative source at \(u=0\) gives
  \(\partial_\sigma f_n-nf_{n-1}\), and its transgression
  has every stated binomial endpoint term.
- The Leibniz formula gives the coefficient-normal rows
  (12) and (12a), with their factorials and powers of \(N\).
  A trivial coefficient monodromy does not kill these rows.
- The whole-clock gauge and its powers have the displayed
  regular root values. Its finite row satisfies
  \(\Gamma G=\Gamma\), while its coupon is
  \(e^{-s_Qu}\Gamma\), whose normal commutator is exactly
  the two-term formula (17).

Thus polynomial moment degree bounds the explicit triangular
source construction, but does not remove coefficient carries,
the irregular vacuum, or the two-wall excursion adapter.
Neither note asserts the missing full Green boundary
cancellation.
