# The actual outgoing contraction through half the Wall degree range

Research result, 7 November 2026. The single fixed degree-separation
certificate has passed. Together with the exact initialized recurrence
and the analytic branch continuation, it proves a uniform asymptotic
with a nonzero coefficient for the actual outgoing contraction at every
high physical retained index. The normalization comes from the original
finite sum, not from a chosen formal solution.

The final retained-index summation and its calibrated reference-plane
comparison remain separate. In particular this is a boundary-function
result, not a knot-invariant lower bound.

## 1. The completed fixed premise

The [fixed protocol](research_mixed_fourier_wall_degree_separation_protocol.md)
tests
\[
 |A\overline D-D\overline C|^2-(|A|^2-|C|^2)^2>0,\qquad
 A=z(1-Yz),\quad C=Yz(1-z),\quad D=A+C-Y,
 \tag{1}
\]
on \(z=e^{-2\pi it}\), \(0\le t\le1/2\), and the full original
saved rectangular enclosure of \(Y=e^{2\pi ix_0}\).
The two rational charts cover the closed lower semicircle.
All 128 fixed cells and all 1,152 degree-eight Bernstein coefficient
lower endpoints passed strictly. The recorded lower endpoint for
(1) is positive; all 25 input bindings remained unchanged.

| Artifact | SHA-256 |
|---|---|
| Fixed protocol | e962441bf71b0d0d92cb24862280ee80823af8a1e87ed2d3ba3c4ce91ce99ac4 |
| Reviewed checker | 142d1f2911ba727d1a1ea230a2a9cdeb189ec827a2b6398c337cf648474627db |
| Sole completed result | 4b2f7b4da3bc30a485041e9530092bd0206fe4eaaf889f1d3981d0fdd1288846 |
| Original saved parameter source | 5d4cb057cb82ca4fff826ad768012480fd6f51afe66d3f5c632e48983cf17514 |

The [result](../repro/results/research-mixed-fourier-wall-degree-separation.json)
retains both chart polynomials, every substituted polynomial and every
Bernstein interval. It has no inconclusive cells or errors. Its
analytic, quantum-source, root, gain, source-replay, proposal,
refinement and retry counters are all zero. The separate read-only
review checked its saved inventory, coefficient signs and provenance;
it did not reconstruct a polynomial or repeat the test.

The protocol's elementary guards prove \(|Y|<1\) and
\(3|Y|^2-2\Re Y>0\) on the same input box. Thus at \(z=1\) the
degree roots are zero and \((1-2Y)/(1-Y)\), the latter strictly
outside the unit circle. Equation (1) excludes a unit root throughout
the semicircle. Since \(A\ne0\), continuity gives one interior and one
exterior root throughout. Compactness supplies their uniform modulus
separation. This is the simple root-count argument of the protocol;
no positivity assertion for the original quantum sum is involved.

## 2. The actual normalized finite solution

Retain \(r=e^{-2\pi i/N}\) and the finite polynomial
\[
 W_{n,N}(u;a)=
 \sum_{l=0}^n
       \frac{(r^{-n};r)_l}{(r;r)_l(ar;r)_l}u^l,
                      \qquad 0\le n<N.
 \tag{2}
\]
Its original diagonal value is \(W_{n,N}(Y;Y)\), and
\(W_{0,N}=1\). The exact degree recurrence, initial ratio and
adiabatic amplitude are those proved in
[the initialized endpoint-strip theorem](research_mixed_fourier_right_cap_wall_endpoint_strip.md),
whose frozen SHA-256 is
f1883a55225ebaa85d1f11f149de1ab89a5a94d1bf86f991f9cea53e00385e18.

For clarity, define its analytic coefficients on a neighborhood of
\(0\le t\le1/2\):
\[
 \begin{split}
 z&=e^{-2\pi it},\qquad r_\varepsilon=e^{-2\pi i\varepsilon},\\
 A(t,\varepsilon,Y)&=z(1-Yr_\varepsilon z),\\
 C(t,\varepsilon,Y)&=Yz(1-z),\\
 B(t,\varepsilon,Y)&=A+C-Y/r_\varepsilon.
 \end{split}
 \tag{3}
\]
Let \(R(t,\varepsilon,Y)\) be the continuation of the exterior root
of \(AR^2-BR+C=0\), fixed by
\[
                  R(0,\varepsilon,Y)
                    =1-\frac{Y}{r_\varepsilon(1-Yr_\varepsilon)}.
 \tag{4}
\]
Write
\[
 d=\frac{C}{AR^2},\qquad L=\log R,\qquad
 I(t,Y)=\int_0^t L(s,0,Y)\,ds,
 \tag{5}
\]
where \(L\) continues the original logarithm at zero. Define
\[
 \mathcal A(t,Y)=
 \exp\left\{
  \frac{L(t,0,Y)-L(0,0,Y)}2
  +\int_0^t\left(
       \frac{R_\varepsilon}{R}
       -\frac{R_t}{R(1-d)}\right)(s,0,Y)\,ds
       \right\}.
 \tag{6}
\]
This is an explicit analytic, nonzero coefficient with
\(\mathcal A(0,Y)=1\).

**Theorem 1.** There are a fixed complex neighborhood of the original
\(Y\) and \(N_0\) such that, for all integers \(N\ge N_0\),
both parities and every \(0\le n\le\lfloor N/2\rfloor\),
\[
 \boxed{\quad
 W_{n,N}(Y;Y)=\mathcal A(n/N,Y)
                  e^{NI(n/N,Y)}(1+O(N^{-1})).
 \quad}
 \tag{7}
\]
The actual polynomial is nonzero throughout this range.
The error is uniform; its normalized derivatives of any fixed order
in \(Y\) satisfy the same bound on smaller common neighborhoods.

*Proof.* The completed premise (1) discharges precisely the sole
additional hypothesis of Proposition 2 in
[the high-index branch addendum](research_mixed_fourier_right_cap_wall_high_index_branch.md),
frozen SHA-256
1292c6491d0106455b93a677b5a3a7239c24dbb94947f8acaa374dedd5dae5a8.
Here are the finite-solution points needed for the implication.
The derivative of the ratio map \(w\mapsto B/A-C/(Aw)\) at \(R\)
has modulus \(|R_{\rm in}/R_{\rm out}|<1\), uniformly on the whole
compact interval at \(\varepsilon=0\). Uniform small complex
neighborhoods and sufficiently small \(\varepsilon=1/N\) preserve
this contraction and the nonzero exterior root.

The exact first ratio is (4), because the recurrence has \(C_0=0\).
The initialized induction therefore controls the actual ratios
\(W_n/W_{n-1}\) on the full interval; it does not insert an
unverified asymptotic seed. Their first correction is
\(-R_t/(1-d)\), with a uniform \(O(N^{-2})\) ratio error.
Summing their logarithms with the endpoint correction gives (6)--(7).
These are the same detailed estimates already proved in the
endpoint-strip theorem, now on a compact interval with the
separation premise certified. They also prove actual nonvanishing.
Cauchy's formula on the common parameter neighborhood gives the
fixed normalized derivative bounds. \(\square\)

## 3. The original outgoing action and finite scalar

The analytic addendum proves, independently of the degree certificate,
that
\[
 Q(t,Y)=z-\frac{z-1}{R(t,0,Y)},\qquad
 q(t,Y)=-\frac{\log Q(t,Y)}{2\pi i}
 \tag{8}
\]
uses the original branch and satisfies
\[
 0<\Re q(t,Y)<t,\qquad \Im q(t,Y)<0,
                                      \qquad 0<t\le1/2.
 \tag{9}
\]
The addendum first proves these inequalities at the original \(Y\).
They hold on a common smaller \(Y\)-neighborhood as follows. Near
\(t=0\), the analytic quotient \(q(t,Y)/t\) has the strict signs
\(0<\Re q_t(0,Y)<1\), \(\Im q_t(0,Y)<0\) from the endpoint-strip
proof, uniformly after shrinking that neighborhood. Away from zero,
compactness of the \(t\)-interval and the strict original chamber
margins preserve (9) under a further common shrinking. The original
logarithmic lifts persist by continuity throughout this neighborhood.
Thus the original factorial and cardinal arguments stay regular.
The outgoing critical point is nondegenerate. The original logarithmic
equation, not only its exponential, holds throughout.

For \(s=1-t\), its calibrated critical action is
\[
 \Phi(s;y)=g(s+q)-g(q)+\ell_q(y)
          =g(s)-\pi iy+I(1-s,Y),\qquad Y=e^{2\pi iy}.
 \tag{10}
\]
The limit at \(s=1\) fixes the constant \(-\pi iy\).
No new logarithmic mark or favorable action constant is chosen.

The actual outgoing contraction at the physical retained index \(j\) is
\[
 H_{j,N}(y)
   =\sum_{l=0}^{N-j-1}\frac{P_{j+l}}{P_l}\,f_l(y)
   =\frac{e^{-\pi i(N-1)y}(1-Y^N)}{N(1-Y)}
                      P_jW_{N-j-1,N}(Y;Y).
 \tag{11}
\]
Equation (7) applies directly to (11) whenever
\(0\le N-j-1\le\lfloor N/2\rfloor\), with \(P_j\) kept exact.
This form is uniform even when the degree stays bounded near zero.
It contains every outgoing physical row, with its cancellation.

For a fixed \(t_->0\), the ordinary interior-scale version is uniform
at the physical indices
\[
                  \frac12\le s=\frac jN\le1-t_-.
 \tag{12}
\]
Writing \(A_g(s)=\sqrt{2\sin\pi s}\,e^{-\pi is/2}\) with the
original mark, it is
\[
 \boxed{\quad
 H_{j,N}(y)=N^{-1/2}\mathcal B(s,y)
                         e^{N\Phi(s;y)}(1+O(N^{-1})),\qquad
 \mathcal B(s,y)=
 \frac{e^{\pi iy}A_g(s)\mathcal A(1-s,Y)}
                     {(1-Y)R(1-s,0,Y)}\ne0.
 \quad}
 \tag{13}
\]
The factor \(R^{-1}\) is required by the exact degree
\(N-j-1\), rather than \(N-j\). The factor \(N^{-1/2}\)
combines the original \(N^{-1}\) Fourier scalar and the marked
factorial \(P_j\). Formula (11), rather than a nonuniform factorial
approximation, is used next to the endpoint itself.
All original parities and fixed normalized output jets are retained.

This settles the actual finite outgoing contraction throughout the
high retained-index region. It does not bound the final sum
\[
 V_N^{\rm F}(y,X)
       =\sum_{j=0}^{N-1}
          \frac{X^{-j}(rX;r)_j}{P_j^3}\,H_{j,N}(y)
\]
by its full geometric reference plane, and it proves no lower bound
for that sum or for an attached knot invariant. The incoming
polynomial, its possible zeros and its branch across
\(j/N+\Re a=1\) remain part of that next exact-source problem.
