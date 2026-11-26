# The exact stability radius of a prescribed closing coefficient

Research deduction, 7 November 2026. The prescribed bilinear closing
has an exact distance to its zero set, even after the original last
coordinate is pinned. For an already solved family of original
sources, that relative distance is exponentially small. Thus a
coefficient-norm approximation to every algebraic order, with the
correct last-coordinate normalization, does not by itself preserve
the closing coefficient. A general transport theorem needs control
at the calibrated observation scale.

The comparison vectors constructed below are full finite coefficient
vectors. They are not asserted to be literal tangle sources or exact
solutions of the original forced equation. This is an obstruction to
a robust norm-only inference, not a counterexample to any knot theorem.
There is no numerical evaluation.

## 1. Distance with prescribed linear normal data

Use the standard Hermitian inner product, conjugate-linear in its first
entry, on the full original Newton coefficient space \(\mathbb C^N\).
Let the prescribed scalar be
\[
                         Z=u^Tv=\langle\overline u,v\rangle .
 \tag{1}
\]
Let \(C\) be any fixed linear normal map, and require a replacement
of \(v\) to have exactly the same normal data \(Cv\). Write
\(P\) for the orthogonal projection onto \(\ker C\).

**Lemma 1.** If \(P\overline u\ne0\), the smallest perturbation
preserving these data and annihilating the closing is exactly
\[
 \min_{\substack{C\delta=0\\u^T(v+\delta)=0}}\|\delta\|
             =\frac{|Z|}{\|P\overline u\|}.
 \tag{2}
\]
It is attained by
\[
                   \delta_*=-\frac{Z}{\|P\overline u\|^2}
                                      P\overline u .
 \tag{3}
\]
If \(P\overline u=0\), every permitted perturbation leaves the
scalar unchanged.

*Proof.* For \(C\delta=0\),
\(\langle\overline u,\delta\rangle
=\langle P\overline u,\delta\rangle\).
An annihilating perturbation therefore satisfies
\[
                  |Z|\le\|P\overline u\|\,\|\delta\|.
\]
Formula (3) attains equality and has precisely the required
normal data. The final assertion follows from the same identity.
\(\square\)

The last-coordinate normal in the original complete-boundary source
corresponds to \(C=\mathbf e_D^T\), \(D=N-1\). In this case
\[
 \|P\overline u\|^2=\|u\|^2-|u_D|^2,\qquad
 \frac{\|\delta_*\|}{\|v\|}
 =\frac{|u^Tv|}{\|u\|\|v\|}
           \left(1-\frac{|u_D|^2}{\|u\|^2}\right)^{-1/2}.
 \tag{4}
\]
In particular, if a norm-error ball with fixed normal contains (3),
it contains a source vector with zero observed scalar. This is an
exact finite-dimensional statement; it does not compare the scalar
with a larger positive norm action.

## 2. An exponentially small radius for actual solved sources

Keep the original conventions
\[
 A_n=JM^n=A_n^T,\qquad v_0=v(-2),\qquad
 w_n=A_nv_0,\qquad (w_n)_D=\kappa_N^n,\qquad |\kappa_N|=1.
 \tag{5}
\]
The [complete coefficient theorem](research_complete_boundary_coefficient_transport.md),
Sections 1--4, supplies these exact identities, including both
level parities and all Hermite coordinates. Its Section 7 proves
that, for every sufficiently large fixed positive integer \(n\),
\[
 \mathfrak c_{n,N}
 :=\frac{|w_n^Tw_n|}{\|w_n\|^2}
 =C_n e^{-N\Delta_n}(1+O(N^{-1})),\qquad C_n>0,
 \tag{6}
\]
where
\[
                  \Delta_n=\frac{16\pi^3}{n^6}
                                      +O(n^{-7})>0.
 \tag{7}
\]
The limit in (6) fixes \(n\) and lets \(N\) tend to infinity.
Equation (7) is the separate large-\(n\) expansion.

The same original signed long-path theorem gives
\(\|w_n\|^2=\mathcal P_{-n,n,N}(-2,-2)\) a nonzero packet
with positive exponential rate. Positivity of that rate holds
for all sufficiently large fixed \(n\): its limiting action as
\(n\) tends to infinity is the sum of three positive bare-edge
complete actions, as in equations (34)--(40) of the cited proof.
Consequently \(\|w_n\|\) grows exponentially for the \(n\)'s
used below.

**Theorem 2.** For every such fixed \(n\), there are full coefficient
vectors \(\widetilde w_n\), at every sufficiently large level of
either parity, with
\[
 \begin{split}
 (\widetilde w_n)_D&=\kappa_N^n,\\
 w_n^T\widetilde w_n&=0,\\
 \frac{\|\widetilde w_n-w_n\|}{\|w_n\|}
       &=C_n e^{-N\Delta_n}(1+O(N^{-1})).
 \end{split}
 \tag{8}
\]
This perturbation has the least possible norm among perturbations
with the first two properties.

*Proof.* Apply Lemma 1 with \(u=v=w_n\) and
\(C=\mathbf e_D^T\). Since \(|(w_n)_D|=1\), the denominator
in (4) is positive for all sufficiently large \(N\).
The exact minimizing perturbation is
\[
 \widetilde w_n-w_n
 =-\frac{w_n^Tw_n}{\|w_n\|^2-1}
           (I-\mathbf e_D\mathbf e_D^*)\overline{w_n}.
 \tag{9}
\]
It preserves the original last coordinate exactly, so the modified
vector itself is nonzero. Its relative norm is
\[
       \mathfrak c_{n,N}(1-\|w_n\|^{-2})^{-1/2}.
 \tag{10}
\]
Exponential growth of \(\|w_n\|\) and (6) prove (8).
Minimality is (2). \(\square\)

The unchanged last-coordinate normal is material: rescaling a
source by an unknown scalar cannot explain (8). The actual left
source \(w_n\) is also held fixed. Only its right boundary vector
is varied within the complete coefficient space.

## 3. Full Fourier norm accuracy does not remove the obstruction

Let \(W_{n,N}\) and \(\widetilde W_{n,N}\) be the original
half-band Fourier interpolants of \(w_n\) and \(\widetilde w_n\).
Their frequency set is
\[
          \Lambda_N=\{-D/2,-D/2+1,\ldots,D/2\}.
 \tag{11}
\]
At even levels these functions are antiperiodic; their products
and squared moduli are still periodic. The exact bilinear and
Plancherel formulas give
\[
 \begin{split}
 N\int_0^1W_{n,N}(t)\widetilde W_{n,N}(t)\,dt&=0,\\
 N\int_0^1W_{n,N}(t)^2\,dt&=w_n^Tw_n,\\
 N\|W_{n,N}\|_{L^2(0,1)}^2&=\|w_n\|^2 .
 \end{split}
 \tag{12}
\]
No conjugation is inserted into the first two integrals.
For every fixed nonnegative integer \(k\), the finite frequency
band also gives
\[
 \frac{\|\partial_t^k(\widetilde W_{n,N}-W_{n,N})\|_{L^2(0,1)}}
      {\|W_{n,N}\|_{L^2(0,1)}}
 \le(\pi D)^k
       \frac{\|\widetilde w_n-w_n\|}{\|w_n\|}
 =O_n(N^k e^{-N\Delta_n}).
 \tag{13}
\]
Indeed each Fourier multiplier has modulus at most \((\pi D)^k\).
Thus these two full finite functions agree, relative to the original
positive norm, beyond every algebraic order in every fixed Fourier
Sobolev norm. Their prescribed bilinear observations in (12) are
different: one is the proved nonzero geometric source, the other
is exactly zero.

This is not a claim that the functions have the same pointwise
holomorphic Gaussian packet on a particular complex chart.
The positive norm and the selected geometric action have distinct
exponential rates in this example. Nor does (13) identify the
modified source with a fixed knot or tangle.

## 4. Consequence for a general short-block transport criterion

The [calibrated three/four overlap criterion](research_mixed_three_four_observed_coercivity.md)
keeps the prescribed vectors \(w_3,w_4\), the full forcing and
the last-coordinate normal. Lemma 1 makes its precision requirement
sharp for errors measured in the original norm. In particular the
exact normal-preserving zero-observation radius for this pair is
\[
 \frac{|w_3^Tw_4|}
       {\|w_4\|\sqrt{\|w_3\|^2-1}},
 \tag{14}
\]
whenever \(\|w_3\|>1\). No value or asymptotic for (14) is
asserted. The \((3,4)\) source is not identified with the
long-power family of Theorem 2.

For an approximation to a source with fixed normal, the exact
error inequality is
\[
 |u^T(v+\delta)-u^Tv|
                \le\|P\overline u\|\,\|\delta\|.
 \tag{15}
\]
It is sharp by (3). Therefore a norm-based proof calibrated to a
proposed geometric term \(T_N\) must control the observed error
at the scale \(|T_N|\), for example by
\[
           \|P\overline u\|\,\|\delta\|
                         \le\varepsilon_N|T_N|.
 \tag{16}
\]
Smallness relative only to \(\|u\|\|v\|\) does not give this
when the calibrated overlap is exponentially small.
Theorem 2 proves that such exponentially small radii occur for
actual solved sources, including their exact original normal.
Thus no universal closing-preservation theorem based solely on
an algebraic-order relative norm-error ball can cover all fixed
short-block assignments.

There is no freedom to perturb an exact forced source arbitrarily.
If \(Bv=f\) is its original forced equation, (9) changes its
residual by exactly \(B\delta_*\). Preserving both that equation
and the pin may determine the vector uniquely. The present result
does not construct a second solution or bound that unnormalized
residual. It says why the independently constructed adjoint test,
or an exact source-compatible relative-cycle estimate, must
control its error at the prescribed observation scale.

The existing
[dominant-cycle transport theorem](research_dominant_saddle_transport.md)
offers a different sufficient structure: a nonzero top relative
cycle, with lower-chain bounds and no omitted pole, boundary or
infinity contribution. It retains the signed period directly and
does not infer its coefficient from a positive norm. Those hypotheses
remain source-specific. Neither this obstruction nor the abstract
transport criterion establishes the ordinary \((3,4)\) closing,
an arbitrary short-cluster closure theorem, or the per-template
finite-exception conclusion.
