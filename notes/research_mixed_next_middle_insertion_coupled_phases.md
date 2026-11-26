# The coupled phases of the actual middle right insertion

Private exact source calculation, 8 November 2026. No mathematical
numerical evaluation or change to a frozen input is used.

The alternating radical coefficients do not independently create
cancellation in the physical-node sum: their signs cancel the
original crossing and attachment signs. The remaining finite sum
can nevertheless be written with all three indices coupled. Its
physical-index phase is explicit, and its zeroth outgoing row has
a precise obstruction to cancellation in that index alone.
No estimate of the whole coupled sum at the geometric rate is
asserted here.

## 1. The original middle block

Use \(D=N-1\), \(q=e^{\pi i/N}\), \(r=q^{-2}\),
\(\kappa=q^{D^2/2}\),
\[
 s_a=2\sin(\pi a/N),\qquad S_a=\prod_{\nu=1}^a s_\nu,
 \qquad P_a=(r;r)_a,
 \qquad p_k(Z)=(rZ;r)_k .
\]
Let \(v(w)=(e_0(w),\ldots,e_D(w))^T\), \(A_3=JM^3\), and
\(\ell_b(w)=(v(w)^TA_3^2)_b\), exactly as in
[high coefficients, Section 1](research_mixed_next_high_coefficients_terminal_insertion.md).
The middle physical block after the already paid high-right band is
\[
 \mathscr S_N^{\rm mid}(w,Z)
 =\frac1{\kappa^2N}
   \sum_{b=\lceil N/2\rceil}^{\lceil5N/6\rceil-1}
          (-q)^b\ell_b(w)C_{0,N}(r^b,Z).
                                                                  \tag{1}
\]
This is the unfiltered full-prefix block in the
[right paired identity, equations (17)--(19)](research_mixed_next_right_paired_terminal_insertion.md).
The existing first-coordinate deletion, the already paid high band,
and the explicit contour currents of that identity remain separate.
There is no extra factor \(+N\) in (1).

Set
\[
 L=\lfloor N/6\rfloor,\qquad U=\lfloor N/2\rfloor-1.
                                                                  \tag{2}
\]
The substitution \(n=D-b\) converts the physical range in (1)
exactly into \(L\le n\le U\), at both parities. In particular,
the last rounded middle node is not replaced by \(n\ge N/6\).
The original radical identity is
\[
\begin{split}
 \ell_{D-n}(w)
 &=\sum_{j=0}^n b_{nj}\mathcal R_N(c_j)^3
                               \mathcal K_{3,N}(w,c_j),\\
 b_{nj}&=(-1)^{n+j}
           \frac{s_{2j+1}S_n^2}{S_{n-j}S_{n+j+1}},\\
 \mathcal R_N(c_j)&=\kappa(-1)^j q^{j(j+1)} .
\end{split}                                                       \tag{3}
\]
These are the original physical values after the radical insertion
has consumed the required normal; the inner kernel retains its
whole Hermite trace.

## 2. Exact cancellation of the alternating signs

Combining all three displayed phases in (1),(3), rather than
choosing a new gauge, gives
\[
 (-q)^{D-n}b_{nj}\mathcal R_N(c_j)^3
 =(-q)^D\kappa^3 q^{-n+3j(j+1)}
                 \frac{s_{2j+1}S_n^2}{S_{n-j}S_{n+j+1}}.
                                                                  \tag{4}
\]
The amplitude on the right is positive. In particular the
\((-1)^{n+j}\) in the radical coefficients is not a spare
alternating phase that can be used after the other source factors
have been bounded in modulus.

The exact outgoing polynomial at this physical node is
\[
 C_{0,N}(r^{D-n},Z)
 =\sum_{k=0}^n
 i^k q^{-nk+k(k-1)/2}
        \frac{S_n}{S_{n-k}S_k^2}\,p_k(Z).
                                                                  \tag{5}
\]
To check its phase, use
\[
 P_a=i^a q^{-a(a+1)/2}S_a,
 \qquad p_k(r^{D-n})=\frac{\overline{P_n}}{\overline{P_{n-k}}},
 \qquad (r^{D-n})^{-k}=r^{(n+1)k}.
\]
Substitution into the literal row
\(Y^{-k}p_k(Y)p_k(Z)/P_k^2\) gives (5). All rows above \(n\)
vanish exactly; no approximation or endpoint extension is used.

For comparison, (5) also has the terminating Gaussian-binomial
form
\[
 C_{0,N}(r^{D-n},Z)
 =\sum_{k=0}^n (-1)^k r^{k(k+1)/2}
            {n\brack k}_r\,\frac{p_k(Z)}{P_k},
 \qquad {n\brack k}_r=\frac{P_n}{P_kP_{n-k}}.
                                                                  \tag{6}
\]
It keeps the outgoing Newton polynomial \(p_k(Z)\); replacing
that polynomial by its modulus would discard another source phase.

## 3. One exact finite sum with all cutoff endpoints

For \(0\le j,k\le U\), define
\[
\begin{split}
 m_{jk}&=\max\{L,j,k\},\\
 W_{jk,N}
 &=\sum_{n=m_{jk}}^U q^{-(k+1)n}
             \frac{S_n^3}{S_{n-j}S_{n+j+1}S_{n-k}} .
\end{split}                                                       \tag{7}
\]
Then the complete block (1) is exactly
\[
\boxed{\begin{split}
 \mathscr S_N^{\rm mid}(w,Z)
 =\frac{\kappa(-q)^D}{N}
  \sum_{j,k=0}^U
   &\frac{s_{2j+1}\,i^k
       q^{3j(j+1)+k(k-1)/2}}{S_k^2}\,p_k(Z)\\
   &\hspace{8mm}\cdot W_{jk,N}\,\mathcal K_{3,N}(w,c_j).
\end{split}}                                                     \tag{8}
\]
This is a finite interchange of (1),(3),(5). All denominator
indices are nonnegative and less than \(N\): in particular
\(n+j+1\le2U+1<N\). It includes the cutoff endpoints, the
zero outgoing row, and both parities.

For successive terms within (7), the exact ratio is
\[
 q^{-(k+1)}
 \frac{s_{n+1}^3}{s_{n-j+1}s_{n+j+2}s_{n-k+1}},
                 \qquad m_{jk}\le n<U .
                                                                  \tag{9}
\]
Thus its consecutive phase is constant; its positive amplitude
is a specific sine-factorial ratio, not an arbitrary test vector.
Writing that amplitude as \(a_n\), the exact summation-by-parts
identity is
\[
\begin{split}
 (1-z)W_{jk,N}
  =a_{m_{jk}}z^{m_{jk}}-a_Uz^{U+1}
     +\sum_{n=m_{jk}+1}^U(a_n-a_{n-1})z^n,
 \quad z=q^{-(k+1)} .
\end{split}                                                       \tag{10}
\]
Neither endpoint term in (10) is absent under the original
physical projection. This identity alone gives no exponential
gain for the actual amplitudes.

## 4. A precise limitation of cancellation in the physical index

At the actual outgoing Newton row \(k=0\), all the phases
\(q^{-n}\), \(m_{j0}\le n\le U\), lie in an arc of width
\(\pi(U-m_{j0})/N<\pi/2\). Rotating by the midpoint of that
arc and taking the real part gives the two-sided comparison
\[
 \frac12\sum_{n=m_{j0}}^U
          \frac{S_n^2}{S_{n-j}S_{n+j+1}}
 \le |W_{j0,N}|
 \le\sum_{n=m_{j0}}^U
          \frac{S_n^2}{S_{n-j}S_{n+j+1}} .                     \tag{11}
\]
The constant \(1/2\) is conservative: every rotated phase has
real part greater than \(\cos(\pi/4)\). These inequalities
hold at every retained \(j\), without a large-level limit.

Consequently an exponential cancellation estimate in the
\(n\)-sum alone, uniform in every outgoing row \(k\), is
unavailable. Equation (11) does not lower-bound the \(j\)-sum
in (8), nor the sum of its different outgoing Newton rows.
The factors \(q^{3j(j+1)}\), the signed inner kernel, and the
polynomials \(p_k(Z)\) still permit cancellation. In particular
\(p_0=1\) does not imply a lower bound for the complete value
at an actual output.

## 5. The retained Fourier source

The remaining coupled polynomial may be put inside the original
complete trace, before any of the moduli in the preceding
[attachment budget](research_mixed_next_physical_three_outgoing_attachment_budget.md)
are used. Define
\[
 \mathcal B_N(t,Z)=\sum_{j,k=0}^U
  \frac{s_{2j+1}i^k q^{3j(j+1)+k(k-1)/2}}{S_k^2}
       p_k(Z)W_{jk,N}K_N(c_j,t).
\]
Then
\[
 \mathscr S_N^{\rm mid}(w,Z)
 =\frac{\kappa(-q)^D}{N}\,
      \phi_N^{(t)}[\mathcal R_N(t)^3K_N(w,t)\mathcal B_N(t,Z)].
                                                                  \tag{12}
\]
Here \(\deg_t\mathcal B_N,\deg_Z\mathcal B_N\le U<N/2\).
The exact derivative-sampling and double-pole contour apply to
(12), with every endpoint current and charge retained. The new
[signed inner-kernel bound](research_mixed_next_physical_three_kernel_fourier_bound.md)
does not estimate this coupled polynomial with its outgoing
observation attached.

Equations (8)--(12) fix the actual phase problem that remains.
They do not assert a positive quadrature for the original Hermite
trace, remove a physical cutoff, or prove suppression of the
complete middle block. The old filter correction and all open
contour currents retain their previous separate estimates and
obligations.
