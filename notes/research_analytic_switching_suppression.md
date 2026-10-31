# Exponential suppression of an analytic discrete switch

31 October 2026.
This is a finite difference normal-form theorem with an explicit error.
It does not identify one eigenbranch as the growth rate of a general
slowly varying recurrence. Its application to the original middle-row
sums requires their literal transfer and boundary data.

## 1. Analytic triangular transfer and an exact finite construction

Let \(I=[a,b]\), \(U_R=\{z\in\mathbb C:\operatorname{dist}(z,I)<R\}\),
and let the bounded analytic block matrix
\[
 T(t)=\begin{pmatrix}A(t)&B(t)\\0&C(t)\end{pmatrix}
 \tag{1}
\]
be given on \(U_R\). Rectangular off-diagonal blocks are allowed. Assume
the Sylvester operator
\[
 \mathcal S_t(X)=XC(t)-A(t)X
\]
has a bounded analytic inverse on \(U_R\). Fix compatible matrix norms.
Put
\[
 H_0(t)=\mathcal S_t^{-1}B(t),\qquad
 \mathcal L_t(X)=\mathcal S_t^{-1}(A(t)X),
 \quad K=\sup_{U_R}\|\mathcal L_t\|,
 \quad M_0=\sup_{U_R}\|H_0(t)\|.
\]
For a positive mesh \(h\), define the EXACT difference operator
\[
 (\mathcal F_h H)(t)=\mathcal L_t\,[H(t-h)-H(t)]
\]
and its finite sum
\[
 H^{[m]}=\sum_{j=0}^{m-1}\mathcal F_h^j H_0,
 \qquad P_h(t)=\begin{pmatrix}I&H^{[m]}(t)\\0&I\end{pmatrix}.
 \tag{2}
\]
All shifts in this expression are literal. No convergent infinite formal
series, interpolated solution of a difference equation, or summability
theorem is assumed.

Direct multiplication gives
\[
 P_h(t)^{-1}T(t)P_h(t-h)
   =\begin{pmatrix}A(t)&R_h(t)\\0&C(t)\end{pmatrix},
 \qquad
 R_h(t)=\mathcal S_t\bigl(\mathcal F_h^mH_0(t)\bigr).
 \tag{3}
\]
Indeed the off-diagonal block is
\(B-\mathcal S_tH^{[m]}+A(H^{[m]}(t-h)-H^{[m]}(t))\),
and the finite geometric identity
\(H^{[m]}-\mathcal F_hH^{[m]}=H_0-\mathcal F_h^mH_0\)
proves (3).

## 2. An exponentially small residual with a bounded gauge

Choose
\[
 m=\left\lfloor\frac{R}{8(K+1)h}\right\rfloor\ge1,
 \qquad \sigma=\frac{R}{2m}.
 \tag{4}
\]
For a function analytic on \(U_r\), Cauchy's derivative bound on the
segment from \(t-h\) to \(t\) gives, when \(h\le\sigma/2\),
\[
 \|H(t-h)-H(t)\|_{U_{r-\sigma}}
       \le \frac{2h}{\sigma}\|H\|_{U_r}.
\]
There are \(m\) nested domains between \(U_R\) and \(U_{R/2}\).
Consequently each application of \(\mathcal F_h\) costs at most
\[
 q=\frac{4Khm}{R}\le\frac{K}{2(K+1)}<\frac12.
\]
The choice (4) also ensures \(h\le\sigma/2\). Thus on \(U_{R/2}\),
\[
 \|H^{[m]}\|\le2M_0,\qquad
 \|R_h\|\le M_0\sup_{U_R}\|\mathcal S_t\|\,2^{-m}
                 \le C_0e^{-c/h},
 \quad c=\frac{R\log2}{8(K+1)}.
 \tag{5}
\]
One may take \(C_0=2M_0\sup\|\mathcal S_t\|\). The matrices
\(P_h,P_h^{-1}\) are uniformly bounded. If the coefficients also depend
analytically on parameters on a compact complex neighborhood, the same
construction and constants work uniformly after shrinking that neighborhood.
Only the stated Sylvester separation is needed; eigenvalues within either
diagonal block may coincide or vanish.

## 3. The full product retains both endpoint contributions

Take \(t_j=t_0+jh\), \(j=1,\ldots,n\), all in \(I\), with
\(nh\le L\) fixed. Write \(A_j=A(t_j)\), \(C_j=C(t_j)\),
\(H_j=H^{[m]}(t_j)\), and use identity matrices for empty products.
Let \(S_n\) be the off-diagonal block of \(T_n\cdots T_1\). The block
triangular product has at most one off-diagonal transition, so (3) gives
the exact identity
\[
 \boxed{\displaystyle
 S_n=H_n(C_n\cdots C_1)-(A_n\cdots A_1)H_0
       +\sum_{j=1}^n A_n\cdots A_{j+1}\,R_h(t_j)\,
                             C_{j-1}\cdots C_1.}
 \tag{6}
\]
In (6), \(H_0\) denotes the gauge at \(t_0\), not the zeroth term
\(\mathcal S^{-1}B\) used in (2).

Define the possible switch amplification
\[
 \Omega_n=\max_{1\le j\le n}
          \|A_n\cdots A_{j+1}\|\,
          \|C_{j-1}\cdots C_1\|.
\]
Then
\[
 \|S_n\|\le2M_0\bigl(\|A_n\cdots A_1\|
                        +\|C_n\cdots C_1\|\bigr)
                   +nC_0e^{-c/h}\Omega_n.             \tag{7}
\]
In particular, if the two pure endpoint products satisfy
\[
 \|A_n\cdots A_1\|+\|C_n\cdots C_1\|
                  \le C_1e^{-\gamma/h}\Omega_n,
 \qquad\gamma>0,
\]
then \(\|S_n\|\le C_2(1+n)e^{-\min(c,\gamma)/h}\Omega_n\).
This is a strict exponential loss relative to the absolute interior-switch
envelope. The residual term in (7) can still dominate both pure products.
It would be false to infer from this theorem that the growth is always
one diagonal branch's action.

## 4. Scalar phase separation

For scalar blocks \(a,c\), the Sylvester hypothesis is just
\(c-a\ne0\) on a fixed complex neighborhood. If on the real interval
\[
 a(t)=e^{i\theta_a}a_+(t),\qquad
 c(t)=e^{i\theta_c}c_+(t),\qquad m_*\le a_+,c_+\le M_*,
\]
and \(|\sin((\theta_a-\theta_c)/2)|\ge\varepsilon>0\), then
\[
 |a(t)-c(t)|\ge2m_*\varepsilon.
\]
Analyticity and uniform bounds extend this separation to a sufficiently
small fixed complex neighborhood. Thus a nonzero relative phase gives
the required analytic gap even when \(|a|=|c|\) on the real interval.

With a scalar positive coupling \(b_+(t)\) bounded above and below,
the corresponding positive switch sum has size between constant multiples
of \(\Omega_n\) and \(n\Omega_n\). Hence (7) proves exponential
cancellation relative to that positive sum whenever its maximizing switch
has a fixed rate gap from both endpoints. Constant phases on the coupling
do not affect this comparison.

## 5. Interface with the original source

The [positive tail transfer](research_positive_eta_word_transfer.md) supplies
an exact two-state active block for the original spectral continuant.
Before and after that block, the source carries the actual middle powers,
unused row factors, and the retained omitted-half scalar modes. The
[literal four-state dictionary](research_original_one_sided_four_state_transfer.md)
now applies (3) directly to a mismatched middle phase. The
[regular-window theorem](research_regular_spectral_window_phase_exclusion.md)
checks full block separation and both endpoint gaps, without a guessed
analytic interpolation of discrete endpoints. In particular it excludes a
collision with the secondary eigenvalue as well as the Perron eigenvalue.

Those regular windows include exact sampled zeros in common retained
factors. Protected degeneracies, spectral caps and boundary maxima still
require separate estimates. An inconsistent shared phase system gives an
exponential improvement relative to its specified window envelope; no
general comparison of that envelope with hyperbolic volume is claimed.
