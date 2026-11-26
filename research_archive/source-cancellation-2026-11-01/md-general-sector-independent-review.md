# Independent bounded review: absolute-source parity and functional locality

1 November 2026. Read-only mathematical review; no public file was changed.
The two results below have different scopes. Neither identifies a new filled
invariant or proves a general complementary-source bound.

## 1. Files and extent of the reading

The public absolute-source note was read in full, with the requested checks
concentrated in sections 3–5, 8, and 9. I reopened the exact odd factor and
closed coefficient argument in actual_fejer_odd_regularized_full_numerator,
sections 2–3, and the coefficient convention and applied theorem in
research_cap_uniform_spectral_gap, sections 1, 3–4.

The private locality note was read in full, including its final section 6
scope clarification and separate short-power example. I independently
rederived the finite constants and the Riemann limit below, using the
literal full-Hermite and homogeneous-source formulas. Its accompanying
script was read, but was not independently executed in this review.
No numerical diagnostic is used to establish an asymptotic statement here.

The hashes at the end identify the text actually checked. The public note
was subsequently reported committed by the parent at 8761cf74; that commit
status is not an input to any mathematical conclusion.

After the proof reading, the parent made a display-only integration change:
40 equation tags became visible parenthesized equation numbers. The reviewed
baseline remains ba75bae505892010300b5e1e45a2a9ac2d8e0cce7f2be79b558d7caa086c590c.
The integrated file is c3ef6983692802da89dcf7d7ec4ad067c07050fdb6c9e6cac70f60cf48955894.
Reversing exactly those 40 tag substitutions recovers the reviewed baseline
byte for byte. This formatting check does not represent a new proof reading.

## 2. Public absolute-source note: bounded acceptance

No concrete correction is required in the requested sections.

### Protected coefficient and odd normalization

For odd \(N=2m+1\), the left cutoff is \(M=m-1\). The original unused
spectral factors give
\[
 U_{N,j}=4S_j^2/T_j^2,\qquad
 S_j=\prod_{r=1}^j2\sin(r\pi/N),\quad
 T_j=\prod_{r=0}^j2\sin((r+\tfrac12)\pi/N).
\]
The full sine products imply \(S_{m-1}^2=N/(4\sin^2(m\pi/N))\) and
\(T_{m-1}^2=1\). Thus the minimum in this range is
\[
 U_{N,M}=N\sec^2(\pi/(2N))\ge N.
\]
At even levels the corresponding endpoint is exactly \(N\). The successive
ratios are at most one, and \(U_{N,0}=\csc^2(\pi/(2N))\le N^2\).
All factors in the stated lower bound are therefore retained.

At odd levels the raw central numerator at \(-2\) is
\(R_m(b)R_m(c)=N^2D_m(b)D_m(c)\). Its degree is \(2m=d\).
There is no forced outer linear factor. This is the raw visited-central
factorization, not an inference from the positive regularization. The
cited odd proof explicitly proves closed, uniform coefficient entropy for
\(D_m\) itself from its half-block recurrence, including supported boundary
loads. The scalar \(N^2\) changes no exponential rate.

### Exact original target rounding

Let \(j=\lfloor m\lambda\rfloor\) and \(e=m\lambda-j\).
For the two distinguished ordinary faces \(x,z\), the old rational table,
scaled by \(d=2m\), has column sums \(d-m\lambda,m\lambda\).
The required sums after taking the cap monomial are \(d-j,j\).
The correction is consequently exactly \(+e\) at \(x\), \(-e\) at \(z\),
with all other corrections zero. It has zero total mass.

Connectivity of the positive support graph permits bounded row-preserving
transfers; positivity makes them feasible for all sufficiently large
levels. The subsequent floor/ceiling cycle rounding preserves the now
integer row and column sums and changes each entry by less than one.
This produces actual arrays with the original targets. Since
\(0<\lambda<1\), \(j\le m-1\), as required for the genuine left support.

The selected odd array has cap magnitude at least \(N\) and \(R-1\)
central factors each contributing \(N^2\). Its scalar is therefore
\(N^{2R-1}\), precisely as in (26). The previously established even
construction retains one actual outer unit per spectator and has its
different scalar \(N4^{R-1}\). These parity-specific scalars are not
interchanged.

### Same-odd-level signed comparison

The positive spectator coefficient called \(B_{N,j}\) has remaining
face targets \(d-j\) at face 0 and \(j\) at face 16. The cited cap theorem
defines its binary variables by \(A=L_{16}, C=L_0\), so its coefficient
\(p_j\) of \(A^jC^{d-j}\) is exactly \(B_{N,j}\). Its cutoff is the same
\(M=m-1\). The raw \(N^2\) factors are included in both polynomials.

The cited theorem's odd-level signed upper rate \(\Phi-\eta\), with
\(\eta=\min(3/1000,\gamma_D)>0\), thus applies to the same selected tuple.
Combining it with the absolute lower rate \(E_{\rm tab}\) proves
\[
 \limsup_{\substack{N\to\infty\\N\ {\rm odd}}}
 \frac1N\log\frac{|S_N|}{\mathcal A_N}
 \le -(E_{\rm tab}-\Phi+\eta).
\]
The denominator is positive for all sufficiently large levels by the
constructed array. Zeros of the signed numerator are allowed. This
deduction makes no even-level signed claim and does not vary the other
spectra or perform filling.

### Same-flow score implication

At the protected left load \((u,0,1-u,0)\), the exact values
\(h=-2f(u)\), \(g=2f(u)\), and \(h_{\rm env}=0\) give
\(h_{\rm sharp}=0\). At each spectator the actual two table rows are a
feasible central split, so its central entropy is at least their sum.
Consequently the original shared table proves the stated lower bounds
for both \(\sum h_{\rm sharp}\) and \(\sum(h+g)\). This does not alter a
face target or manufacture a complete feasible flow. The distinction
from previously stated flat-plat results is necessary and is retained.

## 3. Private locality note: exact finite checks

No concrete correction is required in the frozen final text.

Write \(m=\lfloor N/2\rfloor\),
\(\chi_N=2T_N(z/2)+2=Z_NB_N\), where \(B_N\) is the product over its
distinct double nodes and \(Z_N=B_N\) at even levels,
\(Z_N=(z+2)B_N\) at odd levels. Then
\[
 H_N=Z_N((z+2)/4)^{m-1}
\]
has degree \(N-1\), vanishes at every spectral node, and belongs to the
span of the actual left diagonal coefficients
\(\chi_N/(z-c_a)\).

For a node-vanishing polynomial the original functional is
\[
 \mathcal L_N^nH=N^{-2}\sum_a(4-c_a^2)f_n(c_a)H'(c_a).
\]
Since \(\chi_N''(c_a)/2=N^2/(4-c_a^2)\), it sends
\(\chi_N/(z-c_a)\) exactly to \(f_n(c_a)\). The odd simple-root
contribution is zero. No normal, \(N\)-factor, or root phase was
discarded.

The Lagrange coefficients are
\[
 \alpha_{N,a}=\frac{\kappa_N}{N}(-1)^a\sin\phi_a
                 \cos^{N-2}(\phi_a/2),\quad
 \kappa_N=2\ {\rm(even)},\quad4\ {\rm(odd)}.
\]
Their absolute sum is at most two. Their level dependence is explicit;
they are not assumed to come from one fixed exterior diagram.

The displayed Chebyshev expressions give \(\|H_N\|_{[-2,2]}\le4\).
For \(z=w+w^{-1}\), \(|w|\ge1\), the exact ellipse identity gives
\[
 |z-2|+|z+2|=2(|w|+|w|^{-1}).
\]
This proves the stated disk bound with
\(\rho_r=(2+r+\sqrt{r(4+r)})/2\), including the odd factor \(Nr\).
At \(r=1\), its rate is
\(-\tfrac12\log(8/(3+\sqrt5))<0\).
The endpoint vanishing orders are \(m-1\) and \(m\), respectively.

## 4. Private locality note: phases and asymptotic

For each fixed signed odd integer \(n\), the original midpoint phase has
\[
 e^{-inN\phi_a/2}=(-1)^a e^{-in\pi/2}.
\]
It cancels the Lagrange sign exactly. This leaves precisely the sum in
(18), with the original common unit phase \(\xi_{N,n}\), not an
absolute-value surrogate.

With \(t_a=\sqrt N\phi_a\), mesh size \(h_N=2\pi/\sqrt N\), the summand is
\(N^{-1/2}g_N(t_a)\), where \(g_N\) converges uniformly on compact
intervals to
\(t\exp[-(1/8-in/(4\pi))t^2]\). For \(N\ge4\) its absolute value is
bounded by \(t e^{-t^2/16}\). Since \(h_N\le\pi\), the decreasing tail
can be bounded by an integral starting at \(T-\pi\), uniformly for
large \(T\). This justifies the midpoint limit, including its factor:
\[
 \frac1{2\pi}\int_0^\infty
 t e^{-(1/8-in/(4\pi))t^2}\,dt
 =\frac2{\pi-2in}.
\]
Thus at each parity
\[
 \mathcal L_N^nH_N
 =\frac{\xi_{N,n}}N
       \left(\frac{2\kappa_N}{\pi-2in}+o(1)\right).
\]
The constant is nonzero for negative as well as positive fixed odd \(n\).
There is no uniformity claim for powers growing with \(N\). The part
over any fixed closed spectral neighborhood separated from \(+2\) is
exponentially small, so the stated opposite-end localization is correct.

## 5. Scope of the final section 6 addition

The example disproves a generic subexponential-cost bound of the full
functional by only its negative-endpoint disk norm, even with the exact
one-sided divisor and finite endpoint derivatives. It does not disprove
a theorem with an additional small positive Fejér mass hypothesis.

The separate even-level monomial example in (24)–(26) is consistent with
the cited original crossing formula. For \(x^jc^{d-j}\), the positive
endpoint coefficient is
\[
 (4/a_0)\prod_{r=1}^j(s_r^2/a_r),
\]
whereas the original powers \(n=\pm1\) have coefficient magnitude
\(N/(S_jS_{d-j})=1\). Reflection of the sine factors gives
\(S_jS_{d-j}=S_d=N\). Its negative endpoint-reference rate for
\(j/N\to u\in(0,1/2)\) therefore supplies the stated short-power
coefficientwise obstruction. It is not an assertion about independently
long powers, and not a closed-source counterexample.

The remaining unresolved problem is a coherent estimate on the original
shared complementary source with all of its targets and global
restrictions. Neither the locality example nor the absolute-array
obstruction provides a lower bound for a general signed source or for
a filled invariant.

## 6. Exact input hashes

| File | SHA-256 |
|---|---|
| /private/tmp/md-general-sector-source-review.md | 2424c27ce99d8176eb575d3b30830914ed624df4b7f8d6799235da1f81859360 |
| /private/tmp/md-general-sector-functional-locality-check.py | 89af8e1e6a61d0c3a83d8e0d640493bd9ae8ea822496bb0fcfddb7aa6c7a3ad5 |
| /private/tmp/murakamis_dream-publication/notes/research_absolute_source_cancellation_obstruction.md (reviewed baseline) | ba75bae505892010300b5e1e45a2a9ac2d8e0cce7f2be79b558d7caa086c590c |
| /private/tmp/murakamis_dream-publication/notes/research_cap_uniform_spectral_gap.md | 155dedaa76857e0da51d085f69c340477c9280274b4dd657ce700e6d4e379440 |
| /private/tmp/murakamis_dream-publication/notes/actual_fejer_odd_regularized_full_numerator.md | b1e84fe49c3831496b01dbe14fee4aa165e42d0005d9a1cf888778936a8916b1 |
| /private/tmp/murakamis_dream-publication/notes/actual_uniform_filling_supremum_bound.md | 372915a7be462b9487b6d5ca9b1132fb25a5d1a0dbbef57406981659513139ca |
| /private/tmp/murakamis_dream-publication/notes/actual_homogeneous_casimir_face_source.md | a7d89f310f2cb4193ab73ef49f715198b224d1c3756d84c4cb940d7fa850c2f2 |
| /private/tmp/murakamis_dream-publication/notes/actual_fejer_entropy_signs_and_tail_insertion.md | 1d7c542bae2c65a89e9cae84af8f450810154e8f7972b9b8bc4da1d677fa3736 |
| /private/tmp/murakamis_dream-publication/notes/actual_fejer_half_block_entropy.md | 3f92c7fc9af003822aba97b5394dcbe4a81ce6a1db177049c29817d891699a7d |
