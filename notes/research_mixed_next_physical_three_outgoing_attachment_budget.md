# The outgoing budget after the physical-node three-kernel bound

Private exact source deduction, 8 November 2026. No mathematical
numerical evaluation or frozen-source edit is used.

The new complete signed-kernel estimate improves the inner trace.
Its uniform reserve does not by itself pay a positive estimate of
the remaining outgoing kernel. This note writes the exact required
index-dependent budget and proves that limitation at an original
retained index. It asserts no lower bound for the coherent outgoing
kernel or the actual transfer.

## 1. Exact physical row and its positive envelope

Keep \(D=N-1\), \(r=e^{-2\pi i/N}\), \(q=e^{\pi i/N}\),
\(\kappa=q^{D^2/2}\), and
\[
 P_j=(r;r)_j,\quad p_j(Z)=(rZ;r)_j,\quad
 S_j=|P_j|=\prod_{a=1}^j2\sin(\pi a/N).
\]
The original next-three kernel is
\[
 C_{0,N}(Y,Z)=\sum_{k=0}^D
                    \frac{Y^{-k}p_k(Y)p_k(Z)}{P_k^2}.
                                                                  \tag{1}
\]
For a retained physical node \(Y=r^b\), put \(n=D-b\).
Every row above \(k=n\) vanishes exactly. For \(0\le k\le n\),
the original row modulus is
\[
 \left|\frac{r^{-bk}p_k(r^b)p_k(Z)}{P_k^2}\right|
   =\frac{S_n}{S_{n-k}S_k^2}|p_k(Z)| .                          \tag{2}
\]
Indeed \(p_k(r^b)=P_{b+k}/P_b\), and the exact reflection
\(S_jS_{D-j}=N\) cancels the two factors \(N\).
There is no change of parity or terminal-row normalization.
Define the complete positive envelope
\[
 \mathcal A_{n,N}(Z)
   =\sum_{k=0}^n\frac{S_n}{S_{n-k}S_k^2}|p_k(Z)|,
 \qquad |C_{0,N}(r^b,Z)|\le\mathcal A_{n,N}(Z).
                                                                  \tag{3}
\]
The inequality in (3) does not assert equality for the signed sum.

Use the actual ordinary third-output range
\[
 Z=\rho e^{-2\pi iu},\qquad
 3/10\le u\le39/100,\qquad 4/5<\rho<8/7,
                                                                  \tag{4}
\]
from [the original correlated-height theorem, Section 3](research_mixed_cap_343_correlated_height_bounds.md)
and its \(j=3\) window source; the explicit two-sided radius
range is also recorded in
[selected-left upper rows, Section 1](research_mixed_next_three_selected_left_upper_rows.md).
These contain the original
complete words beginning \(343\) of length at least five.
Let
\[
\begin{split}
 J(t)&=\int_0^t\log(2\sin\pi s)\,ds,\\
 I_Z(t)&=\int_0^t\log|1-Ze^{-2\pi is}|\,ds,\\
 \mathcal E_C(\delta,Z)
 &=\max_{0\le t\le\delta}
       \{J(\delta)-J(\delta-t)-2J(t)+I_Z(t)\}.
\end{split}                                                       \tag{5}
\]
Uniformly for every integer \(0\le n\le\lfloor N/2\rfloor\)
and (4),
\[
 \log\mathcal A_{n,N}(Z)
             =N\mathcal E_C(n/N,Z)+O(\log N).
                                                                  \tag{6}
\]
For this statement the endpoints of the containing radius interval
may also be included. This includes every rounded middle-band index,
and at \(n=0\) both sides of (6) are zero. The outgoing factors
are uniformly nonzero:
their angles \(u+s\), \(0\le s\le1/2\), lie in
\([.30,.89]\), away from every integer. Their Riemann sums
therefore have uniform bounded errors. The exact uniform
sine-factorial estimates give \(O(\log N)\) in (2), including
\(k=0\) and \(k=n\). Taking the largest of the at most \(N\)
positive rows costs another \(O(\log N)\). Finally the integrated
logarithm's modulus of continuity on a mesh of size \(N^{-1}\)
is \(O((\log N)/N)\), so the grid maximum and the continuous
maximum in (5) have the same stated error. This proves (6)
without selecting a critical point or discarding a zero row.

## 2. A strict positive cost at the first retained right node

Take exactly
\[
 b_N=\lceil N/2\rceil,\qquad
 n_N=D-b_N=\lfloor N/2\rfloor-1,\qquad
 k_N=\lfloor N/16\rfloor .
                                                                  \tag{7}
\]
This physical node belongs to the unresolved middle right band
at both parities, for all sufficiently large levels.
For each factor in \(p_{k_N}(Z)\), its angle lies strictly
between \(1/4\) and \(1/2\), by (4). Consequently
\[
                    |1-Zr^a|>1\qquad(1\le a\le k_N).
\]
The uniform factorial estimate in the single row (2) gives
\[
 \liminf_{N\to\infty}\frac1N\log\mathcal A_{n_N,N}(Z)
 \ge -J(7/16)-2J(1/16)>\frac1{16},
                                                                  \tag{8}
\]
uniformly in the actual output range. To verify its strict last
inequality, \(J(7/16)<0\). Also
\(2\sin(\pi s)\le2\pi s<2/5\) for \(0<s\le1/16\),
using \(\pi<16/5\), so
\[
 -2J(1/16)>\frac18\log(5/2)>\frac1{16}.
                                                                  \tag{9}
\]
The final logarithmic comparison follows from
\(\log(5/2)>\log2=\int_1^2dt/t>1/2\).
Equations (8)--(9) are exact written inequalities, not sampled
or evaluated envelope values.

## 3. What the actual remaining attachment requires

With the original \(v(w)=(e_0(w),\ldots,e_D(w))^T\) and
\(A_3=JM^3\), the actual coefficient is
\(\ell_b(w)=(v(w)^TA_3^2)_b\). Its
[high-Newton reduction, equations (2)--(5)](research_mixed_next_high_coefficients_terminal_insertion.md)
is
\[
 \ell_b(w)=\sum_{j=0}^{D-b}b_{D-b,j}\mathcal R_N(c_j)^3
                                       \mathcal K_{3,N}(w,c_j).
                                                                  \tag{10}
\]
Here the original coefficient, including its alternating phase, is
\[
 b_{nj}=(-1)^{n+j}
 \frac{2\sin((2j+1)\pi/N)S_n^2}{S_{n-j}S_{n+j+1}},
 \qquad |b_{nj}|\le2 .
\]
The reviewed [complete Fourier estimate](research_mixed_next_physical_three_kernel_fourier_bound.md)
proves, uniformly on the original real ordinary-color interval,
\[
          |\ell_b(w)|\le CN^A e^{NE_0},\qquad
          E_0=419/200-1/125 .
                                                                  \tag{11}
\]
The still-required right observation retains
\[
 \frac1{\kappa^2N}
       \sum_b(-q)^b\ell_b(w)C_{0,N}(r^b,Z)
                                                                  \tag{12}
\]
on its original middle physical band, together with the explicit
currents in the exact paired-right identity. In (12) no additional
\(+N\) is inserted and no source vector is replaced.

Combining (11) only with (3) produces the comparison quantity
\(e^{NE_0}\mathcal A_{n,N}(Z)\). At (7), its exponential rate
is strictly greater than
\[
 E_0+1/16
       =419/200+\left(\frac1{16}-\frac1{125}\right)
       >419/200 .                                                \tag{13}
\]
Thus that particular attachment of the new uniform inner estimate
cannot supply a strict comparison with the available action floor.
This does not say that the actual action is its floor, nor that
\(|\ell_b C_0|\) has the rate in (13).

A sufficient index-dependent absolute estimate would have to
retain a debit of at least \(\mathcal E_C((D-b)/N,Z)\) from
the actual allocated action, uniformly over the middle band.
Alternatively the \(j\)- and \(b\)-sums in (10)--(12) can be
kept coupled before absolute values. Their original phases,
including \(b_{nj}\), \(\mathcal R_N(c_j)^3\), \((-q)^b\),
and all rows of (1), are not estimated by (8).

No coherent-kernel lower bound, failure of cancellation, outgoing
derivative theorem, or full-transfer noncancellation conclusion
follows from this positive-envelope calculation. Its purpose is to
identify the exact remaining budget after the genuinely improved
signed inner trace.
