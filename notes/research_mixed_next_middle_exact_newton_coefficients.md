# Exact high Newton coefficients and the eligible outgoing-row tail

Private written source deduction, 8 November 2026. No mathematical
numerical evaluation, saved-value calculation, or frozen-source
edit is used.

Multiplying the exact weighted amplitude by its radical Newton
factor recovers the original physical outgoing coefficients.
All sine-factorial normalization factors cancel. The retained
outgoing rows nevertheless have a uniform contraction as the
physical index increases. This gives a positive coefficient-tail
bound whose initial norm is an absolute outgoing-row sum, not the
already bounded coherent outgoing observation.

## 1. Original polynomials and physical rows

Use
\[
\begin{gathered}
 D=N-1,\quad q=e^{\pi i/N},\quad r=q^{-2},\quad
 \kappa=q^{D^2/2},\\
 M=\lceil N/2\rceil,\quad U=D-M=\lfloor N/2\rfloor-1,\quad
 L=\lfloor N/6\rfloor,\quad d=U-L,\\
 K=\lfloor N/4096\rfloor,\quad
 s_a=2\sin(\pi a/N),\quad S_a=\prod_{\nu=1}^a s_\nu,\\
 P_a=(r;r)_a,\quad p_k(Z)=(rZ;r)_k,\quad
 c_j=2\cos((2j+1)\pi/N),\\
 e_b(\xi)=S_b^{-2}\prod_{h=0}^{b-1}(c_h-\xi).
\end{gathered}
 \tag{1}
\]
Here \(S_0=1\), \(s_0=0\), and every level below is
sufficiently large that \(K<U\). Both parities are included.
The symbol \(d\) is a degree, not the forced interpolation
polynomial of the original transfer.

For \(M\le b\le D\), put \(n=D-b\) and retain the literal
outgoing row
\[
 R_{b,k}(Z)=\frac{r^{-bk}p_k(r^b)p_k(Z)}{P_k^2},
 \qquad
 C_{0,N}^{>K}(r^b,Z)=\sum_{k=K+1}^{n}R_{b,k}(Z).
 \tag{2}
\]
All rows \(k>n\) vanish exactly. An empty sum is zero.
There is no additional \(+N\) in this physical conditional
kernel.

Let \(\mathscr A_N(\xi,T)\) be the exact polynomial in
[the all-Casimir amplitude theorem, equation (2)](research_mixed_next_middle_casimir_polynomial_amplitude.md).
The outgoing polynomial in
[the outer observation, equation (5)](research_mixed_next_three_outer_casimir_observation.md)
is
\[
 H_N(\xi,Z)=\sum_{k=K+1}^{U}
                     R_{M,k}(Z)\mathscr A_N(\xi,q^{2k}).
 \tag{3}
\]
This is the original high-outgoing-index sum with its exact
finite amplitude. It has degree at most \(d\) in \(\xi\).

**Exact coefficient identity.**
\[
 \boxed{\quad
 e_M(\xi)H_N(\xi,Z)
   =\sum_{\ell=0}^{d}(-q)^\ell
            C_{0,N}^{>K}(r^{M+\ell},Z)e_{M+\ell}(\xi).
 \quad}
 \tag{4}
\]
This is an equality of ordinary polynomials, before reduction
modulo the spectral relation. Their degree is at most
\(M+d=D-L<N\).
Replacing each high-\(k\) sum by its complete range starting
at zero gives the same identity for \(H_N^{\rm all}\) and the
complete original \(C_{0,N}\).

## 2. Product contraction with its exact phases

For \(0\le\ell\le d\), put \(n=U-\ell\), and set
\[
 Q_{\ell,N}(\xi)=\prod_{a=n+1}^{U}(\xi-c_a).
 \tag{5}
\]
The factors of the amplitude are
\[
 \widehat{\mathcal R}_{a,N}(\xi,T)
 =q\,\frac{(\xi-c_a)(q^a-Tq^{-a})}{i s_a^3}.
 \tag{6}
\]
At \(T=q^{2k}\), the original sine-factor identity gives
\[
 q^a-q^{2k-a}=i q^k s_{a-k}.
 \tag{7}
\]
Thus for \(k\le n\),
\[
 \widehat P_{\ell,N}(\xi,q^{2k})
  =q^{\ell(k+1)}Q_{\ell,N}(\xi)
       \frac{S_n^3}{S_U^3}
       \frac{S_{U-k}}{S_{n-k}}.
 \tag{8}
\]
If \(n<k\le U\), this product instead vanishes: its factor
with \(a=k\) contains \(s_0=0\). No negative factorial
index is introduced in that case.

The original physical reflection, as in
[coupled phases, equation (5)](research_mixed_next_middle_insertion_coupled_phases.md),
is
\[
 R_{D-n,k}(Z)
   =i^k q^{-nk+k(k-1)/2}
      \frac{S_n}{S_{n-k}S_k^2}p_k(Z),
       \qquad 0\le k\le n.
 \tag{9}
\]
Multiplying (8) by (9) at \(n=U\) proves the exact
row identity
\[
 R_{M,k}(Z)\widehat P_{\ell,N}(\xi,q^{2k})
   =q^\ell\frac{S_n^2}{S_U^2}
              Q_{\ell,N}(\xi)R_{D-n,k}(Z).
 \tag{10}
\]
Its zero continuation covers \(n<k\le U\).
Summing first over the retained \(k\) gives
\[
 H_N(\xi,Z)
  =\sum_{\ell=0}^{d}
       q^\ell\frac{S_{U-\ell}^2}{S_U^2}
          Q_{\ell,N}(\xi)
                  C_{0,N}^{>K}(r^{M+\ell},Z).
 \tag{11}
\]

The node identity
\[
                         c_{M+h}=c_{U-h}
 \tag{12}
\]
holds at both parities: their cosine arguments sum to
\(2\pi\), since \(M+U=D\). Consequently, as an ordinary
polynomial identity,
\[
 e_M(\xi)Q_{\ell,N}(\xi)
   =(-1)^\ell\frac{S_{M+\ell}^2}{S_M^2}
                                  e_{M+\ell}(\xi).
 \tag{13}
\]
No division by \(e_M\) is needed at its zeros.
Finally the exact full sine product gives
\[
 S_aS_{D-a}=N,\qquad
 S_{M+\ell}S_{U-\ell}=S_MS_U=N.
 \tag{14}
\]
The two sine ratios in (11),(13) therefore cancel exactly.
This proves (4), including its sign and the remaining power
\(q^\ell\). There is no parity-dependent residual scalar.

## 3. Original radical observation and normalization

Keep the full original Hermite trace and kernel
\[
 \mathcal K_{3,N}(-2,\xi)
  =\phi_N^{(t)}
       [\mathcal R_N(t)^3
          K_N^{\rm ord}(-2,t)K_N^{\rm ord}(\xi,t)],
\]
and the functional of the outer-observation note
\[
 \mathcal L_N(P)
  =\phi_N^{(\xi)}
       [\mathcal R_N(\xi)^3e_M(\xi)
                     \mathcal K_{3,N}(-2,\xi)P(\xi)].
 \tag{15}
\]
Applying (4) inside this literal trace gives exactly
\[
\begin{split}
 \frac{(-q)^M}{\kappa^2N}\mathcal L_N(H_N)
  =\frac1{\kappa^2N}\sum_{b=M}^{D-L}(-q)^b
       C_{0,N}^{>K}(r^b,Z)\,
       \phi_N^{(\xi)}
         [\mathcal R_N(\xi)^3e_b(\xi)
                           \mathcal K_{3,N}(-2,\xi)] .
\end{split}
 \tag{16}
\]
Here \(D-L=\lceil5N/6\rceil-1\), exactly. The final trace
in (16) is the original high Newton coefficient
\(\ell_b(-2)\), by the
[radical contraction and original source](research_mixed_next_high_coefficients_terminal_insertion.md).
Thus (16) is precisely the restored physical middle sum,
with its original \(\kappa^{-2}/N\), full inner signed trace,
and both parities. It does not introduce another projection,
Fourier sector, normal derivative, or filter correction.

The coefficient of \(e_{M+\ell}\) in (4) is therefore
\[
 h_{\ell,N}(Z)=(-q)^\ell
                         C_{0,N}^{>K}(r^{M+\ell},Z).
 \tag{17}
\]
In particular the conversion of the exact normalized amplitude
has no additional damping multiplier beyond these original
outgoing coefficients.

## 4. A valid positive tail for the retained outgoing rows

There is nevertheless a quantitative contraction for each
retained row. For \(M\le b<D\), put \(n=D-b\ge1\).
From (9), for \(0\le k<n\),
\[
 R_{b+1,k}(Z)=q^k\frac{s_{n-k}}{s_n}R_{b,k}(Z).
 \tag{18}
\]
The same equality holds at \(k=n\): its right side is zero,
and the next physical row has terminated. Zeros of \(p_k(Z)\)
do not cause a problem; (18) is an equality of polynomials
in \(Z\), not division by a possibly zero value.

For \(0<k<n<N/2\),
\[
 \frac{s_{n-k}}{s_n}
   =\cos(\pi k/N)-\cot(\pi n/N)\sin(\pi k/N)
   \le\cos(\pi k/N).
 \tag{19}
\]
Both sides are nonnegative. Set
\[
 \varepsilon=1/4096,\qquad
 r_\varepsilon=\cos(\pi\varepsilon)<1,\qquad
 \mathcal B_N^{>K}(Z)=\sum_{k=K+1}^{U}|R_{M,k}(Z)|.
 \tag{20}
\]
Every retained index has \(k/N>\varepsilon\). Iterating
(18)--(19), including literal terminating zeros, proves
\[
 |R_{M+\ell,k}(Z)|
       \le r_\varepsilon^\ell |R_{M,k}(Z)|
                   \qquad(0\le\ell\le d,\quad K<k\le U).
 \tag{21}
\]
For a row beyond its termination the left side is zero.
The stronger row-dependent factor
\(\cos(\pi k/N)^\ell\) is valid as well.

For every integer \(0\le a\le d\), the actual Newton
coefficients consequently satisfy
\[
 \boxed{\quad
 \sum_{\ell=a}^{d}|h_{\ell,N}(Z)|
  \le
  \sum_{\ell=a}^{d}\sum_{k=K+1}^{U-\ell}
                         |R_{M+\ell,k}(Z)|
  \le\frac{r_\varepsilon^a}{1-r_\varepsilon}
                                  \mathcal B_N^{>K}(Z).
 \quad}
 \tag{22}
\]
This is valid for any \(Z\), and for arbitrary subsets of the
displayed positive row sum. It retains the entire coherent
conditional kernel in (17) before that upper estimate.
The factor \(r_\varepsilon<1\) is fixed independently of \(N\),
so a tail beginning at \(a\ge\alpha N\), for fixed
\(\alpha>0\), gains the rate
\(\alpha\log r_\varepsilon<0\) relative to its stated
positive initial envelope.

For the actual \(|Z_*|<8/7\), one may insert the already
proved elementary bound
\[
 \mathcal B_N^{>K}(Z_*)\le N e^{29N/28},
 \tag{23}
\]
from
[small internal indices, equations (6)--(9)](research_mixed_next_three_small_internal_indices.md).
It applies at \(n=U<N/2\) and retains every outgoing row.
For completeness that proof uses
\[
 |R_{M,k}(Z_*)|
  \le \left(\frac{15e^2N^2}{56k^2}\right)^k
       \quad(k\ge1),
\]
whose logarithmic rate increases up to \(k/N=1/2\) and is
less than \(29/28\) there. Equation (23) is an absolute
envelope; it is not the sharper coherent estimate from the
weighted outgoing theorem.

## 5. What this changes and what remains unpaid

Equations (4),(16) identify the original correlation behind the
polynomially weighted radical trace. A maximum over independent
Chebyshev mode responses would control many insertions other than
this specific combination of physical outgoing coefficients.
The exact identity itself gives no bound for that maximum.

The initial norm in (22) is
\(\mathcal B_N^{>K}(Z)\), a sum of row moduli. It cannot be
replaced by
\(|C_{0,N}^{>K}(r^M,Z)|\), or by the supremum of the
weighted coherent polynomial \(H_N\), using the estimates
proved here. Their cancellations have not been preserved by
the positive inequality (22).
In the complete-\(k\) version of (4), the literal \(k=0\)
row has modulus one at every physical node, so there is
no strict rowwise contraction covering every row. The fixed
constant \(r_\varepsilon<1\) in (22) uses the removal of the
positive-fraction small-\(k\) block.

Nor does (22) control the action of
\(\phi_N[\mathcal R_N^3e_b\mathcal K_{3,N}(-2,\cdot)]\)
on those coefficients. The full inner Hermite observation,
its chirps and all original normals remain in (16).
The paid outer contour and filter errors are exactly those
of the adopted transfer reduction and are not split again.
No rate comparison for the remaining physical middle sum,
no noncancellation, and no full transfer asymptotic is
asserted by this coefficient-tail theorem.
