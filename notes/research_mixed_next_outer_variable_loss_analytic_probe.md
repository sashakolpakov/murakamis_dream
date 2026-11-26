# A variable strip-loss estimate for the original analytic probe

Private exact-source deduction, 9 November 2026. Each loss of analytic
strip height can be chosen from the actual leading shift coefficients
of the grouped adjoint. Separating the shift cost from the zeroth-order
defect gives an explicit improved exponent for a finite probe. The
full Hermite transpose, parity forcing and central test conditions
are unchanged.

All parameters below are fixed before the level varies. No numerical
evaluation, saved-value calculation or frozen-source edit is used.
The resulting exponent has not been shown to pay the volume budget.

## 1. The original operator and its exact leading moment

Keep the operator and function spaces of the adopted
[global analytic probe](research_mixed_next_outer_global_analytic_probe.md):
\[
\begin{gathered}
z(u)=-2\cos u,\quad D=N-1,\quad M=\lceil N/2\rceil,\quad U=D-M,\\
q=e^{i\pi/N},\quad\kappa_N=q^{D^2/2},\quad
Q_{3,N}^{\rm rev}(z)=\prod_{\nu=0}^2(z-c_{U-\nu}),\\
\mathcal C_Ng=e_M^{-1}\mathcal B_N(e_MQ_{3,N}^{\rm rev}g),\\
\mathcal B_N=q^{-2}\mathcal L_2(\mathcal L_3^2-I)
 +q^{-3}Z_{\rm mult}\mathcal L_3
 -8q^{-2}\mathcal L_3+(8q^{-1}+2)I.
\end{gathered}                                                     \tag{1}
\]
Here \(Z_{\rm mult}\) is spectral multiplication, not the outgoing
parameter. All factors retain their original order.

After the exact radical ratios, the finite expression on nonreal
horizontal lines is
\[
(\mathcal C_Ng)(u)=
 \sum_{j=-3}^3a_{j,p}(u,N^{-1})g(u+2\pi j/N),                       \tag{2}
\]
where \(p\) records parity. For even periodic analytic \(g\), the
whole expression has the source's global grouped removal of every
real pole. No individual coefficient is asserted removable.

The common leading coefficients \(a_j^0(u)=a_{j,p}(u,0)\) are fixed
by the original principal symbol:
\[
\sum_{j=-3}^3a_j^0(u)v^j
 =(2-2\cos u)^3d(u,-e^{3iu}v),                                    \tag{3}
\]
\[
\begin{split}
d(u,\zeta)&=(\ell^2-1)m-(8+2\cos u)\ell+10,\\
\ell&=2+2a-a(\zeta+\zeta^{-1}),\\
m&=2+2a-a(e^{-iu}\zeta+e^{iu}\zeta^{-1}),\qquad a=\cot^2(u/2).
\end{split}                                                       \tag{4}
\]
Indeed division by the radical reverses each single shift sign.
The leading symbol of \(\mathcal L_n\) in (1) is
\(2+2a+a e^{-inu}v^{-1}+a e^{inu}v\).
Using \(n=3,2\) in the ordered product gives (3).
Its outside factor removes the apparent central poles of these
leading Laurent coefficients.

Let
\[
m_0(u)=\sum_j a_j^0(u)=(2-2\cos u)^3d(u,-e^{3iu}).
\]
The source proves that this is even, entire, periodic, positive
on the real circle and zero-free on a fixed closed strip of
height \(R_*>0\). Fix
\[
0<r<R<R_*,\qquad
\mu_R=\min_{|\Im u|\le R}|m_0(u)|>0,                               \tag{5}
\]
taking real parts modulo \(2\pi\). Define the exact leading moment
\[
K(s)=2\pi\sup_{\substack{-\pi\le\Re u\le\pi\\|\Im u|=s}}
 \sum_{j=-3}^3 |j|
       \left|\frac{a_j^0(u)}{m_0(u)}\right|,
                       \qquad r\le s\le R.                       \tag{6}
\]
It is finite, nonnegative and Lipschitz on this interval:
the quotients have uniformly bounded derivatives near the compact
line families, and modulus, finite sum and supremum preserve the
resulting common Lipschitz bound. No lower bound for \(K\) is assumed.

Write \(\mathscr H_s^{\rm ev}\) for bounded even \(2\pi\)-periodic
holomorphic functions on \(|\Im u|<s\), with norm \(\|\cdot\|_s\).
Retain the preconditioning order
\[
               \mathcal T_N=(\mathcal C_N-m_0)m_0^{-1}.           \tag{7}
\]

## 2. Separate shift and zeroth-order costs

There is a fixed \(C\), uniform in parity and all
\(r\le s<s+\delta\le R\), \(0<\delta\le1\), such that
\[
\boxed{\quad
\|\mathcal T_Nf\|_s
 \le\left\{\frac{K(s)}{N\delta}
          +\frac{C}{N^2\delta}+\frac CN\right\}
                     \|f\|_{s+\delta}.
\quad}                                                            \tag{8}
\]
To prove this on the two boundary lines, put
\[
 b_{j,N}(u)=
 \frac{a_{j,p}(u,N^{-1})}{m_0(u+2\pi j/N)}.
\]
Uniform coefficient analyticity on those nonreal compact sets gives
\[
b_{j,N}=\frac{a_j^0}{m_0}+O(N^{-1}),\qquad
\sum_jb_{j,N}=1+O(N^{-1}),\qquad
2\pi\sup_{|\Im u|=s}\sum_j|j|\,|b_{j,N}|\le K(s)+C/N.
                                                                    \tag{9}
\]
The exact identity is
\[
\mathcal T_Nf(u)
 =\sum_j b_{j,N}(u)\{f(u+2\pi j/N)-f(u)\}
       +\left(\sum_jb_{j,N}(u)-1\right)f(u).                       \tag{10}
\]
Cauchy's derivative estimate on the larger strip, integrated
along the real shift, gives
\[
 |f(u+2\pi j/N)-f(u)|
 \le\frac{2\pi|j|}{N\delta}\|f\|_{s+\delta}.                       \tag{11}
\]
The shifts are real; their definition imposes no requirement
\(\delta\ge6\pi/N\). Equations (9)--(11) prove (8) on the
boundary. Global grouped removability and the annular maximum
principle prove it throughout the strip. This is an estimate for
the exact finite operator, not a substituted differential operator.

## 3. Variable strip losses with a fixed reserve

Choose a fixed \(\eta>0\), independent of \(N\), and set
\[
\Psi_\eta(s)=\frac1e\int_r^s\frac{dt}{K(t)+\eta},
\qquad c_\eta(r,R)=\Psi_\eta(R)>0,\qquad
k_N=\lfloor Nc_\eta(r,R)\rfloor.                                 \tag{12}
\]
The added \(\eta\) absorbs the finite-level errors in (8).
No \(N\)-dependent limit of that reserve is used.

For large \(N\), \(k_N\ge1\). Take the unique partition
\[
r=s_0<s_1<\cdots<s_{k_N}=R,\qquad
\Psi_\eta(s_j)=j\,c_\eta(r,R)/k_N,                                \tag{13}
\]
and write \(\delta_j=s_{j+1}-s_j\).
Since \(K\) is Lipschitz and \(K+\eta\ge\eta\), the inverse of
\(\Psi_\eta\) has Lipschitz continuous derivative. Also
\(c_\eta/k_N=N^{-1}+O(N^{-2})\). The mean-value estimate for
that inverse gives uniformly
\[
 \delta_j=\frac{e(K(s_j)+\eta)}N+O(N^{-2}).                        \tag{14}
\]
Thus every width is between positive fixed multiples of \(N^{-1}\)
and is eventually less than one.

Let \(K_{\max}=\max_{[r,R]}K\). Equations (8),(14) give
\[
\begin{split}
\|\mathcal T_N:
 \mathscr H_{s_{j+1}}^{\rm ev}\longrightarrow
 \mathscr H_{s_j}^{\rm ev}\|
&\le\frac{K(s_j)}{e(K(s_j)+\eta)}+O(N^{-1})\\
&\le\frac1e-\frac{\eta}{e(K_{\max}+\eta)}+O(N^{-1}).
\end{split}                                                       \tag{15}
\]
One common level threshold makes every step at most \(1/e\).
The reserve is uniform over all steps and both parities.

For \(F_N\in\mathscr H_R^{\rm ev}\), define finite expressions
\[
g_N=m_0^{-1}\sum_{\ell=0}^{k_N-1}(-\mathcal T_N)^\ell F_N,
\qquad \rho_N=(-\mathcal T_N)^{k_N}F_N.                            \tag{16}
\]
The same exact operator occurs in every factor, so finite
telescoping gives
\[
\boxed{\quad
\mathcal C_Ng_N=F_N-\rho_N,\qquad
\|g_N\|_r\le\frac{\|F_N\|_R}{\mu_R(1-e^{-1})},\qquad
\|\rho_N\|_r\le e^{\,1-Nc_\eta(r,R)}\|F_N\|_R.
\quad}                                                            \tag{17}
\]
Each successive iterate uses the next inward interval of (13);
its norm is at most \(e^{-\ell}\|F_N\|_R\).
The last residual is at most \(e^{-k_N}\|F_N\|_R\), giving the
displayed factor by the exact floor. The function \(g_N\) is
holomorphic on \(\mathscr S_{s_1}\), strictly larger than
\(\mathscr S_r\).

For comparison, a constant bound
\(\|\mathcal T_Nf\|_s\le\mathcal M(N\delta)^{-1}\|f\|_{s+\delta}\)
with any fixed \(\mathcal M>0\) permits
\(k_N=\lfloor(R-r)N/(e\mathcal M)\rfloor\), and therefore residual
\(\exp\{1-(R-r)N/(e\mathcal M)\}\|F_N\|_R\).
There is no need to replace \(\mathcal M\) by \(\max\{\mathcal M,1\}\).
Equation (12) additionally retains the height dependence of the
moment and separates the zeroth-order defect.

## 4. Unchanged full Hermite pairing

Define
\[
h_N=Q_{3,N}^{\rm rev}(z(u))g_N,\qquad
\mathcal L_N(F)=\phi_N[R_N^3e_MQ_N^{\rm full}F],\qquad
\ell_N(h)=\phi_N[R_N^3e_Mh].                                     \tag{18}
\]
The test \(h_N\) has the same three required central zeros.
It is even and periodic and descends to a holomorphic spectral
function around the whole physical interval.

For each fixed \(N\), approximate \(g_N\) by cosine polynomials
on a strip strictly between \(r\) and \(s_1\). Their spectral
polynomials converge with fixed derivatives on smaller
neighborhoods. The original transpose identity passes to the
full Hermite classes, as in Section 4 of the global probe.
The grouped outputs converge as well. Hence (17) gives exactly
\[
\boxed{\quad
\mathcal L_N(F_N)
 =\mathfrak f_N\ell_N(h_N)+\mathcal L_N(\rho_N),\qquad
\mathfrak f_N=
\begin{cases}
4\kappa_N^3/N^2,&N\ {\rm even},\\
0,&N\ {\rm odd}.
\end{cases}
\quad}                                                            \tag{19}
\]
Every original first normal, the odd simple node and the order
of the bilinear transpose remain present. There are no artificial
matching boundaries. Approximation is used only at fixed \(N\);
no approximation-rate assertion is inserted into (17).

The consumed-normal weights satisfy \(|\mu_{j,N}|\le2\), and
\(|Q_{3,N}^{\rm rev}|\le64\) on the real physical interval.
Together with the complete physical-source bound
\[
\max_j|Q_N^{\rm full}(c_j)|
 \le C_\tau N^{A_\tau}e^{N(\mathfrak M_3+\tau)}
                                      \qquad(\tau>0),
\]
equations (17)--(19) prove
\[
\boxed{\quad
|\mathcal L_N(F_N)|
 \le C_\tau N^{A_\tau}\|F_N\|_R
 \{N^{-1}+e^{N(\mathfrak M_3+\tau-c_\eta(r,R))}\}.
\quad}                                                            \tag{20}
\]
The first term is the original even forcing and vanishes
identically at odd levels. The residual is paired with the
exact complete source; no relative packet error is discarded.

## 5. Attach the actual outgoing factor before optimizing

Use the natural-last-row insertion of the adopted
[action-weighted Green ellipse theorem](research_mixed_next_outgoing_action_weighted_green_ellipse.md):
\[
\nu_N^+(\zeta,Z)=
 \sum_{b=M}^{D}(G_N^+)_{b,M}\frac{e_b(\zeta)}{e_M(\zeta)},\qquad
F_N^+(\zeta,Z)=qA_M\alpha_{M-1,N}(Z)\nu_N^+(\zeta,Z).
                                                                    \tag{21}
\]
Here \(G_N^+=(\mathcal J_{[M,D],N}-ZI)^{-1}\); it is not the
earlier inverse with endpoint \(D-1\). The degree is at most
\(U\), including its original last coefficient.

On the actual closed output rectangle that source proves
\[
\|F_N^+(-2\cos u,Z)\|_R\le CN^A e^{N\mathcal P_Z(R)},\qquad
\mathcal P_Z(R)=\max_{1/2\le a\le1}
 \{\Re\widetilde{\mathcal S}(a,z_*)+R(a-1/2)\}.                    \tag{22}
\]
For \(R\le1/8\), this maximum equals the original
\(\Re\mathcal S(1/2,z_*)\).
The separate restriction \(R<R_*\) in (5) remains: no larger
zero-free strip for the adjoint multiplier is presumed.

Applying (20) to this complete attached source yields
\[
\boxed{\quad
|\mathcal L_N(F_N^+(\cdot,Z))|
 \le C_\tau N^{A_\tau}e^{N\mathcal P_Z(R)}
 \{N^{-1}+e^{N(\mathfrak M_3+\tau-c_\eta(r,R))}\}.
\quad}                                                            \tag{23}
\]
The exact full transfer keeps this observation with scalar
\((\kappa_N^2N)^{-1}\), its nonzero geometric term, and the already
paid cutoff, forcing and contour errors. A uniform strict
sufficient budget on the specified actual family is therefore
\[
\boxed{\qquad
\mathcal P_{Z_*}(R)+\max\{0,\mathfrak M_3-c_\eta(r,R)\}<\Lambda .
\qquad}                                                           \tag{24}
\]
The parameters \(r,R,\eta\) must be selected once with (5).
The admissible exponent is now the explicit integral (12) of
the original shift moment. Increasing \(R\) still pays the
actual input norm (22); repeated cycles give no free gain.

Neither (24) nor an adequate quantitative lower bound for
\(c_\eta(r,R)\) is established here. The proof improves the
admissible probe exponent and supplies its full-source attachment;
it does not close the remaining signed boundary product or
prove stability under arbitrary fixed short fillings.

## Source versions

- Original grouped global probe and full Hermite pairing:
  cb47c9d87949e276615443150b2da2260fec5bb09d3780039b90b322cd14eeb8.
- Exact all-character principal symbol:
  c88ba98093fc147f5acfcf1790aa5b6f0f26edda6d741d2efc7c55315942e55e.
- Central grouped operator and original radical shift conventions:
  244a089f0046f1a8b81f55941c17c32304eb3fd679aa933361ebacbfa416f9a8.
- Full source recurrence and parity forcing:
  49cd08c5759bd6669d3cbf1a7e661d60188639c9added0c973659c4723d0a21a.
- Action-weighted natural Green insertion and attachment:
  e39abb76185b6969901b6ee4c95a4f947bdda5f74d8ff57062ed4b6591a0c029.

