# An exponentially accurate local probe for the actual outer constant mode

Private exact-source application, 8 November 2026. On each fixed
interior color interval the actual weighted seven-term adjoint has
a bounded analytic probe for the constant observation, with an
exponentially small residual. Finite summation by parts then reduces
the original local observation to its explicit parity forcing,
the unchanged finite endpoint terms, and that residual.

The analytic construction is the already proved
[whole-kernel Ward localization](research_whole_kernel_adjoint_ward_localization.md),
Sections 2--3, applied to the actual coefficients now verified in
[the constant-mode symbol theorem](research_mixed_next_outer_constant_mode_symbol.md).
The new conclusion is its finite-sum application to the original
inner source and its error sequence. No boundary term is estimated
below its original exponential rate. No numerical evaluation is used.

## 1. Exact source and a fixed interior chart

Keep the full Hermite source and weights of
[the seven-term recurrence](research_mixed_next_physical_inner_seven_term_recurrence.md):
\[
\begin{gathered}
 m=\lfloor N/2\rfloor,\qquad U=m-1,\qquad
 M=\lceil N/2\rceil,\qquad q=e^{\pi i/N},\\
 u_{j,N}=\pi-(2j+1)\pi/N,\\
 q_{j,N}=Q_N^{\rm full}(c_j),\qquad
 \mu_{j,N}=(-1)^U\kappa_N^3\omega_N(u_{j,N})
                            e^{3\pi i j(j+1)/N},\\
 \omega_N(u)=
 \begin{cases}
 \sin u,&N\ \text{even},\\
 \sin u\sin(u/2)/\cos^2(\pi/(2N)),&N\ \text{odd}.
 \end{cases}
\end{gathered}                                                     \tag{1}
\]
The values \(q_{j,N}\) are exactly the values of the original
full-first, shortened-second inner trace at these physical nodes.
No equality of their off-grid polynomials or first normals is
needed here. The full-quotient source theorem supplies those normals
before its interior evaluation.

The original equation and its bilinear weighted adjoint are
\[
\begin{split}
 (\mathbf D_{3,N}f)_j&=\sum_{\nu=-3}^{3}d_{j,\nu,N}f_{j+\nu},\\
 (\mathbf D_{3,N}^{\dagger}h)_i
 &=\sum_{\nu=-3}^{3}
   \frac{\mu_{i-\nu,N}}{\mu_{i,N}}d_{i-\nu,\nu,N}h_{i-\nu},\\
 (\mathbf D_{3,N}q)_j&=\mathfrak f_N,\qquad
 \mathfrak f_N=
 \begin{cases}
 4\kappa_N^3/N^2,&N\ \text{even},\\
 0,&N\ \text{odd}.
 \end{cases}
\end{split}                                                       \tag{2}
\]
The recurrence is used only in its proved regular interior range.
In particular its nonzero even forcing is not suppressed.

Fix a nonempty compact interval \(J\Subset(0,\pi)\). For \(s>0\)
write \(J_s=\{z:\operatorname{dist}(z,J)<s\}\). The constant-mode
symbol theorem gives a fixed \(R_0>0\), analytic realizations
\[
 (\mathcal A_{N,p}h)(u)=
       \sum_{\nu=-3}^{3}b_{\nu,p}(u,N^{-1})
                                  h(u+2\pi\nu/N),
                                                                  \tag{3}
\]
and an analytic function \(d_0\) such that
\[
 |d_0|\ge\frac18\quad\hbox{on }J_{R_0}.
                                                                  \tag{4}
\]
The index \(p\) specifies the original even or odd coefficient
formula. Evaluation of (3) at an interior physical node is exactly
the adjoint in (2), including its quadratic crossing phase.

Choose \(0<r<R<R_0\), with \(\Delta=R-r\le1\), so that the
closed tube \(\overline{J_R}\) is still in the regular chart.
The actual coefficient estimate in that theorem gives a fixed
constant \(C_J\), common to both parities, for which
\[
 \|(\mathcal A_{N,p}-d_0)v\|_{J_s}
 \le \frac{C_J}{N\delta}\|v\|_{J_{s+\delta}},
 \qquad
 12\pi/N\le\delta\le1,\quad
 0<s<s+\delta\le R .
                                                                  \tag{5}
\]
The constant can be increased to cover this smaller closed tube.
The \(12\pi/N\) reserve is twice the largest angular shift.

## 2. The actual bounded probe

Multiplication by \(d_0^{-1}\) is performed first in the operator
\[
 \mathcal T_{N,p}
       =(\mathcal A_{N,p}-d_0)\,d_0^{-1}.
                                                                  \tag{6}
\]
Equations (4)--(5) imply
\[
 \|\mathcal T_{N,p}v\|_{J_s}
       \le\frac{8C_J}{N\delta}\|v\|_{J_{s+\delta}}.
                                                                  \tag{7}
\]
Thus the inverse multiplier, including its analytic variation, is
part of the norm estimate; it is not commuted past the shifts.

Fix
\[
 M_J\ge\max\{1,8C_J,12\pi\},\qquad
 k_N=\left\lfloor\frac{\Delta N}{4M_J}\right\rfloor,\qquad
 t_N=\Delta/k_N .
                                                                  \tag{8}
\]
For sufficiently large \(N\), \(k_N\ge1\), and each of the
\(k_N\) successive tube losses \(t_N\) satisfies the shift
reserve in (5). Moreover
\[
          \frac{8C_J}{Nt_N}\le\frac14.
                                                                  \tag{9}
\]
Define the finite analytic functions
\[
\begin{split}
 h_{N,p}
   &=d_0^{-1}\sum_{\ell=0}^{k_N-1}(-\mathcal T_{N,p})^\ell1,\\
 \rho_{N,p}&=(-\mathcal T_{N,p})^{k_N}1 .
\end{split}                                                       \tag{10}
\]
Exact telescoping, rather than an asymptotic inverse, gives
\[
 \boxed{\quad
 \mathcal A_{N,p}h_{N,p}=1-\rho_{N,p},\qquad
 \|h_{N,p}\|_{J_r}\le\frac{32}{3},\qquad
 \|\rho_{N,p}\|_{J_r}\le4^{-k_N}.
 \quad}                                                          \tag{11}
\]
Indeed \(\mathcal A_{N,p}d_0^{-1}=I+\mathcal T_{N,p}\);
the finite geometric sum in (10) therefore has exactly the
remainder displayed in (11). Applying (7) on the nested tubes
bounds its successive terms by \(4^{-\ell}\). The same
construction defines \(h_{N,p}\) with one remaining tube layer
before the last application, so every shift used in the first
identity of (11) is legitimate.

A concrete, non-evaluated exponential rate is
\[
 c_J=\frac{\Delta\log4}{8M_J}>0,\qquad
                         4^{-k_N}\le e^{-c_JN}
                                                                  \tag{12}
\]
for all sufficiently large \(N\). Both the tube width and
\(M_J\) depend on the chosen interior interval. No lower bound
for \(c_J\) independent of that interval is asserted.

## 3. Exact finite-sum application

Let \(I_N=[a,b]\cap\mathbb Z\) be any nonempty integer interval
whose physical angles lie in \(J\). For large enough \(N\),
all indices from \(a-6\) through \(b+6\) are eligible interior
indices where required, and their angles lie in \(J_{r/2}\).
More precisely, the recurrence centers used below lie in
\([3,U-3]\); the slightly larger six-index neighborhood retains
all coefficient shifts. Since \(J\Subset(0,\pi)\), these claims
follow from a fixed positive distance to the two physical ends.
They are not assumptions on a shrinking endpoint interval.

Put \(h_j=h_{N,p}(u_{j,N})\) and
\(\rho_j=\rho_{N,p}(u_{j,N})\). For any sequence \(f\) on the
required neighborhood, keep the original boundary expression
\[
\begin{split}
 \mathcal B_{I_N}(h,f)
 ={}&\sum_{\nu=-3}^{3}
   \sum_{\substack{j\in I_N\\j+\nu\notin I_N}}
       \mu_{j,N}h_jd_{j,\nu,N}f_{j+\nu}\\
 &-\sum_{\nu=-3}^{3}
   \sum_{\substack{j\notin I_N\\j+\nu\in I_N}}
       \mu_{j,N}h_jd_{j,\nu,N}f_{j+\nu}.
\end{split}                                                       \tag{13}
\]
These are the two finite endpoint currents in the recurrence
theorem. Their signs and the outside values of the source are
unchanged.

**Theorem.** The actual constant-mode observation on \(I_N\)
satisfies
\[
\boxed{\quad
 \sum_{i\in I_N}\mu_{i,N}q_{i,N}
   =\mathfrak f_N\sum_{j\in I_N}\mu_{j,N}h_j
       -\mathcal B_{I_N}(h,q)+\mathcal E_N,
 \qquad
 |\mathcal E_N|
    \le e^{-c_JN}
          \sum_{i\in I_N}|\mu_{i,N}q_{i,N}|.
 \quad}                                                          \tag{14}
\]
This holds for the original source, both parities, and every
such interval simultaneously, with constants fixed by \(J\).

*Proof.* Exact finite summation by parts in equations (21)--(22)
of the recurrence theorem gives
\[
 \sum_{i\in I_N}\mu_{i,N}
          (\mathbf D_{3,N}^{\dagger}h)_iq_{i,N}
 =\mathfrak f_N\sum_{j\in I_N}\mu_{j,N}h_j
                         -\mathcal B_{I_N}(h,q).
                                                                  \tag{15}
\]
Substitute the exact first identity of (11), evaluated at
the physical nodes. The remainder is precisely
\[
                  \mathcal E_N
                     =\sum_{i\in I_N}\mu_{i,N}\rho_iq_{i,N}.
                                                                  \tag{16}
\]
Equations (11)--(12) prove its bound. No holomorphic continuation
or derivative estimate for \(q_{i,N}\) was used. \(\square\)

The forcing term has an actual polynomial bound. Since
\(|\kappa_N|=1\), \(|\mu_{j,N}|=\omega_N(u_{j,N})\le2\)
at every eligible node, and \(I_N\) has at most \(N\) indices,
\[
 \left|\mathfrak f_N\sum_{j\in I_N}\mu_{j,N}h_j\right|
   \le\frac{256}{3N}\quad(N\ \text{even}),
 \qquad
 \mathfrak f_N\sum_{j\in I_N}\mu_{j,N}h_j=0
                  \quad(N\ \text{odd}).
                                                                  \tag{17}
\]
The first bound is deliberately uniform rather than sharp.

The endpoint term has not acquired an exponential gain.
Let \(D_J\) bound the actual coefficients
\(|d_{j,\nu,N}|\) on the fixed regular neighborhood used above.
There are at most
\(2\sum_{\nu=-3}^{3}|\nu|=24\) summands in (13). Hence, for
example,
\[
 |\mathcal B_{I_N}(h,q)|
 \le512D_J
       \max_{\substack{a-3\le i\le a+2\\
                        \text{or }\,b-2\le i\le b+3}}
                              |q_{i,N}|.
                                                                  \tag{18}
\]
Equation (13), rather than this coarse inequality, preserves
the available endpoint cancellation.

## 4. A correlated error-sequence identity

The same probe controls the error of an approximate solution
without replacing that error by independent pointwise errors
inside a canceled sum. Let \(p_j\) be any comparison sequence
on the required neighborhood, and define
\[
 e_j=q_{j,N}-p_j,\qquad
 \varepsilon_j=(\mathbf D_{3,N}p)_j-\mathfrak f_N .
                                                                  \tag{19}
\]
The original equation gives \(\mathbf D_{3,N}e=-\varepsilon\).
The exact adjoint formula therefore yields
\[
\begin{split}
 \sum_{i\in I_N}\mu_{i,N}e_i
 ={}&-\sum_{j\in I_N}\mu_{j,N}h_j\varepsilon_j
       -\mathcal B_{I_N}(h,e)
       +\sum_{i\in I_N}\mu_{i,N}\rho_i e_i,\\
 \left|\sum_{i\in I_N}\mu_{i,N}\rho_i e_i\right|
 \le{}&e^{-c_JN}\sum_{i\in I_N}|\mu_{i,N}e_i|.
\end{split}                                                       \tag{20}
\]
In particular the residual contribution is at most
\((32/3)\sum_{j\in I_N}|\mu_{j,N}\varepsilon_j|\).
This is an exact constraint on the error sequence of the
original source. No all-orders approximation or residual bound
for a proposed packet is supplied by (20).

## 5. Scope and the remaining outer estimate

The original transfer has the outside factor
\((-q)^M/(\kappa_N^2N)\). It multiplies every term of
(14) or (20) equally and is not absorbed into a new trace
normalization.

For the constant observation, (14) is a genuine exponentially
accurate interior reduction with a bounded test function. It
does not assert that \(c_J\) exceeds the excess of the positive
nodal norm above the required budget
\(B_f=77/50+\pi/50\). The endpoint term (13) remains at its
original rate until its cancellation or a sharper bound is
proved. Covering the interval by different local probes does
not cancel their boundary terms: such cancellation requires
the same probe on the shared neighborhoods, or the exact
additional mismatch terms.

The construction also does not apply uniformly to physical
indices a bounded number of steps from zero or \(U\).
Those points lie outside the fixed interior charts. Finally,
the actual insertion \(H_N(c_j,Z_*)\) has degree proportional
to \(N\); replacing the right side \(1\) in (11) by that
insertion requires retaining its analytic norm or its changed
principal symbol. No bound for the complete signed observation
\(\mathcal L_N(H_N)\), and no global inverse, follows here.

### Source hashes

- Seven-term recurrence:
  49cd08c5759bd6669d3cbf1a7e661d60188639c9added0c973659c4723d0a21a.
- Actual constant-mode symbol and coefficient control:
  ef07c25bb23cf52763d8ef19d145be14b4abd69445df321b6cdb6d78697ee7cc.
- Whole-kernel adjoint Ward localization:
  43f0058f8eed882abe1ec548484786656b025274488ad12de80cda0fea42e540.
- Quantitative power Ward exclusion:
  0c29c993b88c7c40c73c8820ad001754fef2dd4a9b86873ab39ad83ef7a11e49.
