# The even complete low row on the spectral slit plane

Let \(N=2m\), \(\theta=\pi/N\), \(J=m-1\), and retain the original
Newton polynomials
\[
 c_a=2\cos((2a+1)\theta),\qquad
 S_k=\prod_{\nu=1}^k2\sin(\nu\theta),\qquad
 e_k(w)=S_k^{-2}\prod_{a<k}(c_a-w).
 \tag{1}
\]
The actual physical rows and the even complete low row are
\[
 K_N(z,w)=\sum_{k=0}^{N-1}e_k(z)e_k(w),\qquad
 F_{j,N}(w)=K_N(c_j,w),\qquad
 L_N(w)=\sum_{k=0}^{m-1}e_k(-2)e_k(w).
 \tag{2}
\]
Write \(\Omega=\mathbb C\setminus[2,\infty)\). The full kernel at
the even complete endpoint includes additional radical terms;
they are not part of \(L_N\).

**Theorem.** On every fixed compact \(\mathcal K\Subset\Omega\),
for all sufficiently large even \(N\),
\[
 \boxed{\qquad
 \frac{L_N(w)}{F_{J,N}(w)}=1+O_{\mathcal K}(N^{-1/2}).
 \qquad}
 \tag{3}
\]
Every fixed number of ordinary \(w\)-derivatives of the error
obeys the same bound on compact subsets. In particular \(L_N\)
has no zeros on \(\mathcal K\) for all sufficiently large even
levels. With the logarithm normalized by positivity at \(-2\),
locally on fixed slit neighborhoods,
\[
 \frac1N\log L_N(w)\longrightarrow
 \Psi_{1/2}(w),\qquad
 \Psi_x(w)=\int_0^x
 2\operatorname{arsinh}
 \left(\frac{\sqrt{2-w}}2\cot(\pi s)\right)\,ds .
 \tag{4}
\]
The convergence includes every fixed spectral derivative.
Only an \(o(N)\) logarithmic remainder is asserted on general
slit compacts.

## 1. Actual initialization and the tail coefficients

All estimates are taken first on a slightly larger fixed slit
compact, and then restricted if derivatives are needed. The
physical Jacobi realization makes the actual rows nonzero
there for large \(N\). Set
\[
 \rho_r=\frac{F_{r,N}}{F_{r-1,N}},\qquad
 r_0=\lfloor N/4\rfloor,\qquad
 h_r=N/2-r,\qquad Q_r=\frac{\cos(r\theta)}{\sin^3(r\theta)}.
 \tag{5}
\]
The full-slit bulk theorem in [B, Section 2] proves for the
original normalized solution
\[
 \rho_{r_0}=\lambda(r_0/N,w)+O(N^{-1}),\qquad
 \lambda(x,w)=
 \exp\!\left[
 2\operatorname{arsinh}
 \left(\frac{\sqrt{2-w}}2\cot(\pi x)\right)\right].
 \tag{6}
\]
Thus (6) is an actual row initialization, not a choice of a
formal growing mode.

For \(r_0\le r<J\), its exact recurrence is
\[
 \rho_{r+1}=1+d_r+q_r(1-\rho_r^{-1}),\qquad
 d_r=\frac{c_0-w}{A_r},\qquad
 A_r=\frac{[2\sin((r+1)\theta)]^4}
 {[2\sin((2r+1)\theta)][2\sin((2r+2)\theta)]}.
 \tag{7}
\]
Direct cancellation of these sine factors gives
\[
 q_r=\frac{Q_{r+1}}{Q_r},\qquad
 \frac{1/A_r}{Q_rQ_{r+1}}=B_r
 =\frac{\sin^3(r\theta)\sin((2r+1)\theta)}
 {2\cos(r\theta)}.
 \tag{8}
\]
On this tail \(Q_r\) is decreasing,
\[
 Q_r\asymp h_r/N,\qquad
 |Q_{r+1}-Q_r|\le C/N,\qquad 0<q_r\le1.
 \tag{9}
\]
These \(Q_r\) estimates also include \(r=J\).

Put \(\lambda_r=\lambda(r/N,w)\). The principal square root
has positive real part on the slit, and so does the principal
inverse hyperbolic sine of its positive real multiple. Hence
\(|\lambda(x,w)|>1\) for \(0<x<1/2\). At the last endpoint,
\[
 \lambda(x,w)-1
 =\sqrt{2-w}\,
 \frac{\cos(\pi x)}{\sin^3(\pi x)}
 +O\!\left(
 \frac{\cos^2(\pi x)}{\sin^6(\pi x)}\right).
 \tag{10}
\]
Compactness on \(1/5\le x\le1/2\) therefore gives constants
\(c,C>0\) such that
\[
 |\lambda_r|\ge1+cQ_r,\qquad
 |\lambda_r-1|\le CQ_r,\qquad
 |\lambda_{r+1}-\lambda_r|\le C/N .
 \tag{11}
\]
No assertion that \(\Re\lambda_r>1\) on the whole slit is used.

The defect in substituting \(\lambda_r\) into (7) is
\[
 \left|1+d_r+q_r(1-\lambda_r^{-1})
                  -\lambda_{r+1}\right|\le C/N .
 \tag{12}
\]
Indeed
\[
 A_r^{-1}=
 \frac{\sin((2r+1)\theta)\cos((r+1)\theta)}
 {2\sin^3((r+1)\theta)}
 \]
differs from \(\cot^2(r\theta)\) by \(O(N^{-1})\)
uniformly to the endpoint, and \(c_0-2=O(N^{-2})\).
Also \(|q_r-1|\,|1-\lambda_r^{-1}|\le C/N\) by
(9),(11). Now use the exact frozen equation
\(\lambda_r=1+(2-w)\cot^2(r\theta)+(1-\lambda_r^{-1})\).

## 2. Transport to a large square-root layer

Let \(e_r=|\rho_r-\lambda_r|\). Choose a fixed \(K_0\)
large enough to dominate the initialization (6) and the
forcing in (12). Next choose a fixed \(A>0\), sufficiently
large relative to \(K_0\) and the compact-set constants.
We claim
\[
 e_r\le K_0/h_r
 \quad\text{while }h_r\ge A\sqrt N,
 \tag{13}
\]
including the first following row.

Suppose (13) holds at a row in this range. By (9), taking
\(A\) large makes \(e_r\le(c/2)Q_r\). Thus
\(|\rho_r|\ge1+(c/2)Q_r\), and subtracting the two
recurrences gives
\[
 e_{r+1}\le
 \frac{q_r}{|\rho_r\lambda_r|}e_r+C/N
 \le(1-c_1h_r/N)e_r+C/N .
 \tag{14}
\]
Here \(c_1>0\) is fixed and can be decreased so the factor
is nonnegative. If \(K_0\ge C/c_1\), the right side at
the proposed barrier is at most \(K_0/h_r\), hence at
most \(K_0/(h_r-1)\). This proves the induction from (6).
On this part of the tail we have consequently
\[
 |\rho_r|\ge1+c_2Q_r,\qquad |\rho_r-1|\le C_2Q_r.
 \tag{15}
\]

## 3. The final layer as a fixed disk

Let \(k_N\) be the first row with \(h_{k_N}\le A\sqrt N\);
then \(h_{k_N}=A\sqrt N+O(1)\). For large \(N\), the
principal root
\(\sigma_N(w)=\sqrt{c_0-w}\) is defined on the chosen
compact neighborhood and satisfies
\[
 \Re\sigma_N\ge s_0>0,\qquad |\sigma_N|\le s_1.
 \]
Set \(\zeta_r=(\rho_r-1)/(\sigma_NQ_r)\).
Equations (7),(8) give exactly
\[
 \zeta_{r+1}=f_r(\zeta_r),\qquad
 f_r(\zeta)=\sigma_NB_rQ_r+
                     \frac{\zeta}{1+\sigma_NQ_r\zeta}.
 \tag{16}
\]
By (10),(13) and
\(\sigma_N-\sqrt{2-w}=O(N^{-2})\), its entry value obeys
\[
 \zeta_{k_N}=1+O(K_0/A^2)+O_A(N^{-1/2}).
 \tag{17}
\]

Fix \(\epsilon>0\) small enough that
\(\Re(\sigma_N\zeta)\ge s_0/2\) whenever
\(|\zeta-1|\le\epsilon\). On this convex disk
\[
 |f_r'(\zeta)|=|1+\sigma_NQ_r\zeta|^{-2}\le1.
 \tag{18}
\]
The displacement of its center has a summable bound.
Writing \(h=h_r\), the exact trigonometric identity
\[
 B_r=\cos^4(h\theta)\cos\theta
 -\frac{\cos^3(h\theta)\cos(2h\theta)\sin\theta}
 {2\sin(h\theta)}
 \]
implies
\(|B_r-1|\le C(h^{-1}+h^2/N^2)\) in this layer.
Therefore
\[
 \begin{split}
 f_r(1)-1
 &=\sigma_NQ_r(B_r-1)
       +\frac{\sigma_N^2Q_r^2}{1+\sigma_NQ_r},\\
 |f_r(1)-1|&\le C(N^{-1}+h_r^2/N^2),\\
 \sum_{r=k_N}^{J-1}|f_r(1)-1|&\le C_A N^{-1/2}.
 \end{split}
 \tag{19}
\]
Choose \(A\) so the first error in (17) is below
\(\epsilon/4\), and then choose \(N\) so the remaining
entry error and the sum in (19) are together below
\(\epsilon/4\). The line segment from \(\zeta_r\) to
one stays in the disk. Equations (18),(19) inductively
keep every \(\zeta_r\), through \(r=J\), within that disk.
In particular (15), with possibly different constants,
holds on the entire tail \(r_0\le r\le J\).

## 4. Relative alternating interpolation

Put \(b_\ell=F_{J-\ell,N}/F_{J,N}\), \(b_0=1\).
Products of the actual ratios in (15) give, for
\(0\le\ell\le J-r_0\),
\[
 \begin{split}
 |b_\ell|&\le C e^{-c\ell^2/N},\\
 |b_\ell-1|&\le C\min\{\ell(\ell+1)/N,1\},\\
 |b_{\ell+1}-b_\ell|
 &\le C(\ell+1)N^{-1}e^{-c\ell^2/N}.
 \end{split}
 \tag{20}
\]
The last line is first used when both indices are in
that range. It follows directly from
\(b_{\ell+1}=b_\ell/\rho_{J-\ell}\).

Earlier rows are exponentially suppressed. The all-row
slit logarithmic theorem [S, Theorem 1] gives uniformly
in the row index
\[
 N^{-1}\log F_{j,N}(w)=\Psi_{j/N}(w)+o(1).
 \tag{21}
\]
The integrand defining \(\Psi_x\) has strictly positive
real part for real \(0<x<1/2\). On a fixed slit compact,
\(\Re(\Psi_{J/N}-\Psi_{j/N})\) is consequently bounded
below by a fixed positive constant when \(j<r_0\).
Thus \(|b_\ell|\le Ce^{-cN}\) there. The transition
from (20) and all earlier adjacent differences obey
the same exponential bound.

The exact original interpolation [E, equations (6)--(9)] is
\[
 \frac{L_N}{F_{J,N}}
 =\sum_{\ell=0}^{J}(-1)^\ell a_{\ell,N}b_\ell,\qquad
 a_{\ell,N}=\frac1m\cot((\ell+1/2)\theta),\qquad
 \sum_{\ell=0}^{J}(-1)^\ell a_{\ell,N}=1.
 \tag{22}
\]
Its positive decreasing weights satisfy
\[
 a_{\ell,N}\le C/(\ell+1),\quad
 a_{\ell,N}-a_{\ell+1,N}\le C/(\ell+1)^2,\quad
 a_{J,N}=O(N^{-2}).
 \]
Abel summation bounds the difference from one in (22) by
\[
 \begin{split}
 &a_{J,N}|b_J-1|
 +\sum_{\ell<J}(a_{\ell,N}-a_{\ell+1,N})|b_\ell-1|\\
 &\hspace{35mm}
 +\sum_{\ell<J}a_{\ell+1,N}|b_{\ell+1}-b_\ell|.
 \end{split}
 \tag{23}
\]
Split the first sum at \(\sqrt N\); (20) bounds it by
\(O(N^{-1/2})\). The second is bounded by
\(CN^{-1}\sum_{\ell\ge0}e^{-c\ell^2/N}+Ce^{-cN}\),
also \(O(N^{-1/2})\). The endpoint term is \(O(N^{-2})\).
This proves (3).

## 5. Logarithms, derivatives and scope

Apply (3) on a buffered larger compact. Cauchy's formula
gives every fixed derivative bound. The quotient lies in
a fixed disk about one, so its logarithm near zero is
\(O(N^{-1/2})\), with the same derivative bounds.
On a fixed simply connected slit neighborhood containing
the anchor \(-2\), add that logarithm to the original
real-normalized logarithm of \(F_{J,N}\).
Equation (21), continuity of \(\Psi_x\) at \(x=1/2\),
and Cauchy's formula prove (4).

This establishes eventual nonvanishing on each fixed
slit compact, including points with real part two and
nonzero imaginary part. It neither locates every zero
at every finite level nor controls neighborhoods whose
distance to the removed ray shrinks with \(N\).
The existing odd complete row already has its physical
Jacobi logarithm; no shorter odd cutoff is substituted.
There is no estimate here for the additional even
radical sector, an original closing functional, or a
selected contribution after tangle composition.

## Direct sources

- E: [The even complete low kernel](research_even_complete_low_kernel.md),
  SHA256 ea3a8b7becbed501a28969f9cd6715c2b5e0b660aba7c5eb57229b1977220ed1.
  The literal low row, exact alternating interpolation and weights.
- B: [The slit normal connection](research_physical_row_slit_normal_connection.md),
  SHA256 a5084adb4ff25cb08020e5f9485bd1aaea5b49468c6ab0af311ebc1c0c504d99.
  The actual row recurrence and the full-slit bulk ratio initialization.
- S: [The first shortened edge on the slit plane](research_mixed_next_first_short_edge_slit_plane_bound.md),
  SHA256 efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b.
  The original normalized logarithms and their uniform all-row limit.
