# The low-index complete-end kernel at even levels

Research proof, 3 November 2026. Frozen manuscripts are unchanged.

The last physical color at an even level is close to the complete
color, but they are different. The full kernel cannot simply be
evaluated at the last physical row and called the complete-end kernel.
This note proves the needed comparison for its low-index part. The
comparison is relative, so it preserves the nonzero coefficient.

The proof uses an exact Chebyshev interpolation formula. Its alternating
weights have sum one. The actual row recurrence controls the variation
of the values against those weights; no positivity of the final quantum
trace is assumed.

## 1. The original low-index kernel

Let \(N=2m\), \(J=m-1\), and \(\theta=\pi/N\). Use the original
Newton polynomials and physical colors
\[
 e_k(z)=\frac{\prod_{a=0}^{k-1}(c_a-z)}{S_k^2},\qquad
 c_a=2\cos((2a+1)\theta),\qquad
 S_k=\prod_{a=1}^k2\sin(a\theta).
 \tag{1}
\]
Define
\[
 L_N(w)=\sum_{k=0}^{m-1}e_k(-2)e_k(w),\qquad
 F_{j,N}(w)=K_N(c_j,w).
 \tag{2}
\]
Thus \(L_N\) is the original complete-end kernel with its radical
Newton indices \(k\ge m\) removed. At every physical color those
removed polynomials vanish. In particular
\[
 F_{j,N}(w)=\sum_{k=0}^{m-1}e_k(c_j)e_k(w)
                  \quad(0\le j\le J).
 \tag{3}
\]
Fix a compact set of free colors
\[
 \mathcal W_{\gamma,R}
   =\{w:\Re w\le2-\gamma,\ |w|\le R\},
                  \qquad \gamma>0,
 \tag{4}
\]
and allow constants to depend on this set. All asymptotic statements
below are uniform on (4) as the even level tends to infinity.

**Theorem 1.** The original low-index kernel satisfies
\[
 \boxed{\qquad
        \frac{L_N(w)}{F_{J,N}(w)}=1+O(N^{-1/2}).
       \qquad}
 \tag{5}
\]
The same estimate holds after every fixed number of derivatives in
\(w\). In particular, \(L_N\) is nonzero on (4) for all sufficiently
large even levels.

## 2. Exact alternating interpolation

The \(m\) distinct physical colors are the zeros of \(T_m(z/2)\).
Lagrange interpolation of the polynomial of degree at most \(m-1\)
in the first variable in (3) therefore gives
\[
 L_N(w)=\sum_{h=0}^{m-1}(-1)^h a_{h,N} F_{J-h,N}(w),\qquad
 a_{h,N}=\frac1m\cot\bigl((h+\tfrac12)\theta\bigr)>0.
 \tag{6}
\]
For completeness, put \(\varphi_j=(2j+1)\theta\). The Lagrange
coefficient at \(z=-2\) is
\[
 \frac{T_m(-1)}{(-2-c_j)T_m'(c_j/2)/2}
 =\frac{(-1)^{m+j+1}}m\tan(\varphi_j/2).
 \tag{7}
\]
Here \(T_m'(\cos\varphi_j)=m(-1)^j/\sin\varphi_j\).
Substitution of \(j=J-h\) proves (6). Applying interpolation to
the constant polynomial also proves the exact identity
\[
                   \sum_{h=0}^{m-1}(-1)^h a_{h,N}=1.
 \tag{8}
\]
The weights decrease with \(h\), and elementary differentiation of
the cotangent gives constants independent of \(N\) such that
\[
 a_{h,N}\le\frac C{h+1},\qquad
 0<a_{h,N}-a_{h+1,N}\le\frac C{(h+1)^2}.
 \tag{9}
\]
The second estimate is needed only when \(h<m-1\). For example,
use \(\sin x\ge2x/\pi\) on \([0,\pi/2]\) in the derivative
\(m^{-1}\theta\csc^2((h+1/2)\theta)\). Also
\(a_{m-1,N}=O(N^{-2})\).

## 3. The actual rows vary slowly near the last row

The [endpoint Riccati theorem](research_last_physical_row_riccati.md)
applies to the original normalized solution, not to an independently
chosen approximate solution. Write
\[
 \rho_r=F_{r,N}/F_{r-1,N},\qquad u_r=\rho_r-1,\qquad
 Q_r=\frac{\cos(r\theta)}{\sin^3(r\theta)},\qquad
 r_0=\lfloor N/4\rfloor.
 \tag{10}
\]
For all sufficiently large \(N\), it gives, on the entire tail,
\[
 \Re u_r\ge c Q_r,\qquad |u_r|\le C Q_r,
       \qquad r_0\le r\le J,
       \qquad Q_r\asymp (N/2-r)/N.
 \tag{11}
\]
The upper bound throughout this tail follows explicitly from that
proof. At distance at least \(\sqrt N\) from the endpoint, its
ratio error is \(O((N/2-r)^{-1})\), which is
\(O((N/2-r)/N)\) there; its limiting root differs from one by
\(O(Q_r)\). In the final square-root layer the proof gives
\(|u_r|\le C Q_r\) directly. The lower bound is its propagated
positive-real barrier. At every earlier row one still has
\(\Re\rho_r>1\).

Set
\[
                   B_h=F_{J-h,N}/F_{J,N},\qquad B_0=1.
 \tag{12}
\]
All ratios are defined by the zero-free physical solution. Equations
(11) imply, for \(0\le h\le J-r_0\),
\[
 \begin{split}
 |B_h|&\le C\exp(-c h^2/N),\\
 |B_h-1|&\le C\min\{h(h+1)/N,1\},\\
 |B_{h+1}-B_h|&\le
      \frac{C(h+1)}N\exp(-c h^2/N).
 \end{split}
 \tag{13}
\]
The final line is used when \(J-h\ge r_0\). Indeed
\[
 B_{h+1}=B_h/\rho_{J-h},\qquad
 |\rho_r|\ge1+cQ_r.
 \tag{14}
\]
Taking the product in (14), and using
\(\log(1+cQ_r)\ge c'Q_r\) on this bounded tail, proves the
first estimate in (13). Summing the elementary difference bound
\(|B_{h+1}-B_h|\le |u_{J-h}|\), and using \(|B_h|\le1\),
proves the second. Retaining the first estimate in the difference
bound proves the third. After this tail, monotonicity of the moduli
\(|F_{j,N}|\) gives
\[
 |B_h|\le C e^{-cN},\qquad
 |B_{h+1}-B_h|\le C e^{-cN}
                     \quad(h>J-r_0).
 \tag{15}
\]

## 4. The alternating sum preserves its coefficient

Divide (6) by \(F_{J,N}\), and subtract (8). The error is exactly
\[
        \sum_{h=0}^{m-1}(-1)^h d_h,
                      \qquad d_h=a_{h,N}(B_h-1).
 \tag{16}
\]
Partial sums of \((-1)^h\) have modulus at most one. Summation by
parts therefore bounds (16) by
\[
 |d_{m-1}|+
 \sum_{h=0}^{m-2}(a_{h,N}-a_{h+1,N})|B_h-1|
       +\sum_{h=0}^{m-2}a_{h+1,N}|B_{h+1}-B_h|.
 \tag{17}
\]
The endpoint term is \(O(N^{-2})\). By (9), (13), and the bound
\(|B_h-1|\le2\), the first sum is at most a constant times
\[
 \sum_{h\le\sqrt N}\frac1{(h+1)^2}\frac{h(h+1)}N
        +\sum_{h>\sqrt N}\frac1{(h+1)^2}
                         =O(N^{-1/2}).
 \tag{18}
\]
The second sum, through the tail, is bounded by
\[
             \frac CN\sum_{h\ge0}e^{-c h^2/N}
                            =O(N^{-1/2}).
 \tag{19}
\]
Its remaining terms are exponentially small by (15). This proves
(5). Apply the argument on a slightly larger compact subset of
\(\Re w<2\); Cauchy's formula then proves the derivative estimates.

The cancellation in (16) has been estimated relative to the actual
last row. This is the point that an absolute bound for the interpolation
weights would miss.

## 5. Consequence for the geometric exponential rate

Put
\[
 \Psi(w)=\int_0^{1/2}\Log\lambda(x,w)\,dx,
 \qquad
 \lambda(x,w)=\exp\left(2\operatorname{asinh}
            \left(\frac{\sqrt{2-w}}2\cot\pi x\right)\right).
 \tag{20}
\]
The branches and normalization are those of the endpoint theorem.
In particular \(\Psi(-2\cos t)=\psi(t,0)\) on the original branch.
Since \(J/N=1/2-1/N\), the omitted part of the integral contributes
only \(O(N^{-1})\) to its exponent. Combining Theorem 1 with the
endpoint theorem gives
\[
 L_N(w)=\exp\{N\Psi(w)+\widetilde E_N(w)\},\qquad
 |\partial_w^\ell\widetilde E_N(w)|\le C_\ell\log N
 \tag{21}
\]
for every fixed \(\ell\). The logarithm of the quotient in (5) is
the branch near zero, so it adds only \(O(N^{-1/2})\), with the same
derivative bounds, to the logarithm of the physical row.

At odd levels the low-index part at a complete end equals the full
kernel, because every radical polynomial vanishes at the simple
physical node \(-2\). The odd-level conclusion of the endpoint
theorem and (21) thus give a nonzero complete-end **low-index**
factor at both parities. In a source calculation the removed radical
terms must still be retained and bounded after their original traces.
No estimate of the full even-level off-grid kernel is inferred.

This qualification is necessary. The
[exact radical asymptotic](research_even_complete_radical_asymptotic.md)
gives the full kernel different odd- and even-level exponential
rates at \(w=(1-3\sqrt3\,i)/2\). At that color the low sector
still has the rate proved here. The additional even-level sector
is larger before the original traces are taken.

## 6. Reproducing the finite identities

The accompanying checker constructs the original Newton polynomials,
their last physical rows and their low complete-end sums separately.
It checks the interpolation weights and the full finite identity (6).
The reported relative errors in (5) are diagnostics; the proof of the
uniform estimate is (10)--(19).

~~~sh
python3 experiments/check_even_complete_low_kernel.py
~~~

The [saved results](../repro/results/research-even-complete-low-kernel.json)
record the code and proof dependencies.
