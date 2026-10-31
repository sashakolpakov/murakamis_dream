# Independent audit of the whole cyclic Rees crossing

Audit, 27 October 2026. The proof in
[rees_whole_crossing_source_factorization.md](rees_whole_crossing_source_factorization.md)
passes this independent normalization, order and source check.
No test rerun was needed.

The common head root and Hopf scales cancel in the crossing argument:
\(\mathcal E_{\mathrm{hat,1}}F_{\mathrm{hat,2}}\) is precisely the conjugate of
\(\mathcal E_1F_2\). Separate roots instead retain their stated ratio.
Consequently the universal series can be conjugated coefficientwise
with a central bookkeeping variable; local nilpotence after this
irregular change is not assumed.

Splitting \(\log P_Q(z)\) at indices divisible by \(N\) gives exactly
\[
 P_Q(z)=C_Q(z)\,P_{Q^N}(z^N)^{1/N}.
\]
Both factors are functions of the same operator and commute. The two
functional ratios have logarithms
\[
 -\log(1-z)+\frac1N\log(1-z^N),\qquad
 -\frac1N\log(1-z^N).
\]
Their sum has the required original Pochhammer transport.

At a root, for \(N\nmid m\),
\(\sum_{j=1}^{N-1}jQ_N^{jm}=-N/(1-Q_N^m)\).
Thus the inverse weighted product has exactly the nonresonant
coefficients of \(C_{Q_N}\). At \(m=Nr\), its weighted coefficient
is canceled by \(\nu^{-(N-1)/2}\), with
\(\nu=(1-z^N)^{1/N}\). This verifies
\(C_{Q_N}=g_D^{-1}\), including even and composite levels.
Deck summation annihilates every remaining logarithmic coefficient,
so the cyclic norm and the marked generic matrix determinant are one.

For \(d=N(Q^N-1)\), direct expansion gives
\[
 \log P_{Q^N}(w)^{1/N}
 =\frac{\operatorname{Li}_2(w)}d+
   \frac{\operatorname{Li}_2(w)+\log(1-w)}{2N}+O(d).
\]
The finite \(\operatorname{Li}_2/(2N)\) term is required for this
linear normal. The note correctly does not apply the displayed
finite scalar part to a moving noncommutative operator lift.

The rational universal conjugation identities, rather than the
inner root matrix \(g_D\), supply the center transport. The ordered
power \(v^N=-e_1f_2k_2/k_1\) gives
\(D_c=1+e_1f_2k_2/k_1\); the printed center formulas preserve each
individual fixed-Casimir equation
\(ef-k-k^{-1}=\text{constant}\). The coproduct \(N\)-th powers also
give the stated obstruction
\[
 e_1k_2+e_2=k_1e_2+e_1
\]
to any generic regular same-fiber matrix replacement. This is
consistent with a canonical operator transporting the center.

Finally \(i_{\mathrm{new}}=Ci\), \(p_{\mathrm{new}}=pC^{-1}\) prove the exact
finite-head pairing. Their normalized product does not remove the
source exponential \(e^{-\sum p_i u_i/d}\), the head ratios, or
the exponential at each internal projector. The literal pivot,
peripheral functions and two-wall correction remain selected.

The proof's scope is appropriate: a coefficientwise formal whole
factorization and its rational canonical transport, with an explicitly
irregular source. It does not assert convergence of the transformed
series at bookkeeping parameter one, a regular full-cyclic matrix
limit, survival of its polar phase in a finite-head pairing, or the
physical large-level volume norm.
