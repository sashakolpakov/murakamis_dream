# Odd raw source: the same low-demand recurrence and contour bound

31 October 2026. The even theorem is recorded separately. The regularized odd coupon is used only in the positive endpoint comparator; the signed numerator remains the raw pair \(V_N(-2),V_N(2)\).

## 1. Original odd supports and an all-parity Newton identity

Let \(N=2m+1\ge3\), \(d=2m\), \(M=m-1\), and \(\theta=\pi/N\).
Retain the actual quartets \(E=(A,0,C,Z)\), \(F=(0,A,0,C)\), with
the same original \(A^d\) demand as in
[the odd high-demand source](research_cap_cross_high_demand_signed_contraction.md).
Put \(c_j=2\cos((2j+1)\theta)\), \(a_j=2+c_j\),
\(\gamma_j=2-c_j\), \(s_j=2\sin(j\theta)\), and
\[
 B_j=\prod_{r=1}^j s_r^2,\qquad
 v_j=B_j\prod_{h=j+1}^d a_h .
\]
The sole zero \(a_m=0\) is never replaced or divided out.

There is an exact all-parity Newton coefficient formula
\[
 (\alpha_{V_N(\sigma)})_j
     =(-1)^j B_j\prod_{h=j+1}^d(\sigma-c_h).             \tag{1}
\]
Indeed, first take \(\sigma\) off all nodes. The divided difference
of \(V_N(\sigma;z)=(\chi_N(z)-\chi_N(\sigma))/(z-\sigma)\) at
\(c_0,\ldots,c_j\) is
\(\chi_N(\sigma)/\prod_{r=0}^j(\sigma-c_r)\), the displayed tail
product. This is polynomial in \(\sigma\), so it extends to every
node, retaining all confluent derivatives. Consequently
\[
              \alpha_{V_N(-2),j}=(-1)^d v_j.           \tag{2}
\]
At odd level this is \(+v_j\); it vanishes for \(j<m\) and is
strictly positive for \(j\ge m\).

For every \(0\le n\le d\) define the auxiliary full slice
\[
 S_n^{\mathrm{full}}=\sum_{j=0}^n(-1)^jU_j C_{j,n-j},
 \qquad U_j=4B_j/\prod_{r=0}^j\gamma_r.                 \tag{3}
\]
The unused-product convention gives \(C_{j,h}=0\) if \(h>m\).
The original odd projected sum uses
\[
 J_n=\{\max(0,n-m),\ldots,\min(M,n)\}.                  \tag{4}
\]
For \(0\le n\le M\), both sums have exactly \(0\le j\le n\).
Thus the auxiliary equals the original raw sum in the needed low
range. No above-\(M\) identification is asserted.

The physical three-port completion and its swap/complement turn
identity in
[the Newton source proof](research_cap_cross_low_demand_newton_contraction.md)
hold at every level. With \(g_n=\prod_{r<n}(\Omega-c_r)\), its raw
marked scalar is \((-1)^{d+n}B_nS_n^{\mathrm{full}}\).
The genuine Newton turn, (2), and
\(\alpha_{g_n}=(-1)^nB_ne_n\) give the same sign times
\(B_n v^T V_N(2;Z_N)e_{d-n}\). Since \(\chi_N(2)=4\) at every
level and every \(\gamma_j>0\), this proves
\[
 S_n^{\mathrm{full}}=v^T[4(2I-Z_N)^{-1}]e_{d-n}.             \tag{5}
\]
No division by the odd value \(\chi_N(-2)=0\) occurs.
The bidiagonal resolvent equation and literal row reflection yield
\[
 \gamma_n S_n^{\mathrm{full}}+s_n^2S_{n-1}^{\mathrm{full}}
       =4v_{d-n}=4C_{0,n},\qquad S_{-1}^{\mathrm{full}}=0,
 \qquad C_{0,n}=\frac{N^2}{B_n}\prod_{h=0}^{n-1}a_h .
                                                               \tag{6}
\]
Here \(B_nB_{d-n}=N^2\), and the reflected unused product is exactly
the last product. This forcing is nonzero for \(n\le M\).
Therefore the original raw odd coefficient obeys
\[
 R_n=\frac{\gamma_n S_{N,n}}{4C_{0,n}},\qquad
 R_0=1,\quad R_n=1-t_nR_{n-1},\quad
 t_n=\frac{4\sin^4(n\theta)}{\sin^2((2n-1)\theta)}.      \tag{7}
\]
No extra regularization factor appears in this raw recurrence.

## 2. The contour proof permits half-integral \(N/2\)

Apply
[the even full-low contour proof](research_cap_cross_full_low_demand_subexponential_contraction.md)
to \(P_j=\prod_{r=1}^jt_r\), \(A_j=P_j^{-1}\).
In its Gamma factorization replace the parameter \(m\) by \(N/2\),
now half-integral. Every exact factorization and shifted
Euler--Maclaurin formula remains valid. The largest row here is
\(M=N/2-3/2\), so all Gamma real-part bounds on the contour
\([-1/4,n+1/4]\times[-NY,NY]\) are at least as strong.
The relative nodal error remains at most \(e^{-6N/5}\), and the
leading analytic action remains \(2f(z/N)\).

Replace the parity-specific sine-product bound on \(P_j\) by the
already proved uniform real-node estimate
\[
                   \log P_j=-2Nf(j/N)+O(\log N).        \tag{8}
\]
Its proof uses the explicit Gamma factors, smooth interpolation and
uniform Stirling estimate, independently of any prior bound on \(P_j\).
Since \(f\ge0\) on \([0,1/2]\), this gives \(P_j\le N^C\) uniformly.
That polynomial bound suffices on the left/top/bottom contour and
for the nodal replacement error. The right edge still has the exact
rate cancellation supplied by (8).
Thus the same fixed-\(Y\), then \(N\to\infty\), then \(Y\to\infty\)
argument proves
\[
 \limsup_{\substack{N\to\infty\\N\ {\mathrm{odd}}}}
     \frac1N\log\max_{0\le n\le (N-3)/2}|R_n|\le0.       \tag{9}
\]
No row-interior coefficient lower theorem is used.

## 3. The actual regularized endpoint comparator

Use exactly the original odd reference
\[
 F_N=V_N(-2)-N^{-2}\partial_\sigma V_N(-2).
\]
Let \(\overline C_{j,h}\) be its CROSS coefficient at \(E\), and
\(V_j^o\) its RIGHT coefficient at \(F\). The positive path expansion
gives \(\overline C_{j,h}\ge C_{j,h}\ge0\). At \(j=0\), the unused-row
derivative removes the sole central zero and yields
\[
 V_0^o=N^{-2}\prod_{\substack{0\le r\le d-1\\r\ne m}}a_r
       =\frac1{a_d}=\frac1{a_0},                       \tag{10}
\]
since \(\prod_{r\ne m}a_r=N^2\).
The actual positive comparator
\[
 D_{N,n}^o=\sum_{j\in J_n}V_j^o\overline C_{j,n-j}
\]
contains its \(j=0\) term for \(n\le M\). Hence
\[
 \frac{|S_{N,n}|}{D_{N,n}^o}
       \le\frac{4a_0}{\gamma_n}|R_n|
       \le4N^2|R_n| .                                 \tag{11}
\]
Combining (9) and (11) proves
\[
 \limsup_{\substack{N\to\infty\\N\ {\mathrm{odd}}}}
   \frac1N\log\max_{0\le n\le (N-3)/2}
             \frac{|S_{N,n}|}{D_{N,n}^o}\le0.           \tag{12}
\]
Regularization occurs only in the comparator. The numerator, its
support, spectral pair, and all original face demands stay raw.

## Validation and open scope

A private exact-field specialization of the physical
three-port audit checked \(N=3,5,7,9\): 24 original physical scalars,
24 full auxiliary recurrences, 10 explicit low-cutoff identifications,
and 24 Newton resolvent entries. It uses the literal tail product
(1)--(2), never a division by \(a_m\).
The [portable audit](../experiments/audit_research_cap_cross_odd_low_demand_subexponential_extension.py) has [recorded results](../experiments/research_cap_cross_odd_low_demand_subexponential_extension_results.json).
These checks support only the parity/source dictionary, not the
analytic estimate (9).

No polynomial full-low estimate, nearby-spectral bound, or projected
middle-demand conclusion is inferred.