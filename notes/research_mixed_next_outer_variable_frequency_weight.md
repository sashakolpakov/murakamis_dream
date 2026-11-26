# Variable frequency weights for the actual outer residual

Private finite-source theorem, 9 November 2026. A varying Fourier
weight can be used in the exact low-frequency adjoint compression.
Its admissibility is checked against the complete leading symbol at
each frequency. The original finite operator remains a small
perturbation after this conjugation, including its long downward
Fourier entries. This yields an outgoing-action convolution bound
for the eleven boundary output modes and retains the literal
higher-degree input tail.

An explicit admissible weight is supplied. The resulting sufficient
attachment inequality is not proved. In particular no principal
action is substituted for a finite inverse estimate, and no
exponentially small residual is discarded. No mathematical numerical
evaluation or frozen-source edit is used.

## 1. Exact source, symbol, and admissible weights

Keep the notation of the
[full-shift compression theorem](research_mixed_next_outer_full_shift_low_frequency_inverse.md):
\[
\begin{gathered}
 z(u)=-2\cos u,\qquad
 \mathcal C_Ng=e_M^{-1}\mathcal B_N(e_MQ_{3,N}^{\rm rev}g),\\
 (\mathcal P_Ng)(u)=\sum_{j=-3}^3a_j^0(u)g(u+2\pi j/N),\\
 p(u,\nu)=\sum_j a_j^0(u)e^{2\pi ij\nu}
      =(2-2\cos u)^3d(u,-e^{3iu+2\pi i\nu})
      =\sum_{\ell=-11}^{11}p_\ell(\nu)e^{i\ell u}.
\end{gathered}                                                     \tag{1}
\]
The exact ordered \(\mathcal B_N\), both parities, and original
full Hermite transpose are unchanged. The cited theorem proves
\[
\begin{gathered}
 p(u,\nu)>0\quad(u\in\mathbb R,\ |\nu|<1/2),\\
 p(0,\nu)=4096\cos^6(\pi\nu),\qquad p(\pi,\nu)=256,\\
 p(-u,-\nu)=p(u,\nu),\qquad
 (\mathcal P_N)_{n,k}=p_{n-k}(k/N).
\end{gathered}                                                     \tag{2}
\]
Every leading coefficient has degree at most eleven. The actual
operator on an even polynomial of degree \(k\) has degree at most
\(k+11\), before taking its full Hermite class.

Fix \(0<\alpha<1/2\), put \(K_N=\lfloor\alpha N\rfloor\), and
define the positive continuous function
\[
 \mu(t)=\min_{u\in[-\pi,\pi]}p(u,t),\qquad
 \mu_\alpha=\min_{0\le t\le\alpha}\mu(t)>0.                       \tag{3}
\]
Let \(\lambda:[0,\alpha]\to(0,\infty)\) be continuous and satisfy
\[
 \mathcal D(t,\lambda(t))
 :=\sum_{\ell=-11}^{11}|p_\ell(t)|
                   (e^{|\ell|\lambda(t)}-1)
                         \le\frac{\mu(t)}4
                          \qquad(0\le t\le\alpha).               \tag{4}
\]
Set
\[
 W(t)=\int_0^t\lambda(v)\,dv,\qquad
 (E_{W,N}f)_k=e^{NW(|k|/N)}f_k.                                \tag{5}
\]
Extend \(\lambda\) constantly a fixed distance beyond \(\alpha\)
when output indices up to \(K_N+11\) occur. This extension is
only used to bound those finite output modes, not to assert
coercivity on a larger solved band.

There is an explicit admissible choice requiring no further
hypothesis:
\[
 \lambda_*(t)=
 \min\left\{1,\,
 \frac{\mu(t)}
 {16e^{11}\{1+\sum_{\ell=-11}^{11}|\ell|\,|p_\ell(t)|\}}\right\}.
                                                                    \tag{6}
\]
Indeed \(e^{|\ell|\lambda}-1\le
|\ell|\lambda e^{11}\) for \(0\le\lambda\le1\), so (6)
gives \(\mathcal D\le\mu/16\).
This weight is continuous with a strictly positive minimum on
the fixed band. Formula (6) specifies a mathematical function of
the original symbol, not a numerical test or an assumed large
strip. Other weights satisfying (4) may give stronger estimates.

## 2. Variable-weight coercivity of the leading compression

Let \(\Pi_N\) project onto \(-K_N,\ldots,K_N\). On this full
Fourier space define
\[
 P_{I,N}=\Pi_N\mathcal P_N\Pi_N,\qquad
 B_{I,N}=E_{W,N}P_{I,N}E_{W,N}^{-1}.
\]
Its entries are
\[
 (B_{I,N})_{n,k}
 =p_{n-k}(k/N)
   \exp\{N[W(|n|/N)-W(|k|/N)]\},
 \qquad |n-k|\le11.                                            \tag{7}
\]
All entries are uniformly bounded for fixed \(\alpha,\lambda\).

We prove accretivity by the exact finite window argument.
Take \(L=\lfloor\sqrt N\rfloor>11\) and
\[
 \chi_j(k)=L^{-1/2}{\bf1}_{\{j\le k<j+L\}}.
\]
Zero-extend every compressed vector. As in the cited theorem,
\[
 \sum_j\chi_j(k)^2=1,\qquad
 \sum_j\chi_j(n)\chi_j(k)=1-|n-k|/L
                                      \quad(|n-k|\le11).         \tag{8}
\]
Since (7) has fixed bandwidth and bounded entries, replacing its
quadratic form by the sum of windowed forms costs at most
\(C/L\) times the squared norm.

For a nonempty window choose \(k_j\) in its intersection with
the compressed band, and put \(\nu_j=k_j/N\). Freeze the
unweighted coefficients to the Toeplitz matrix
\[
 (P_j^0v)_n=\sum_{\ell=-11}^{11}p_\ell(\nu_j)v_{n-\ell}.
\]
Its real quadratic form is at least
\(\mu(|\nu_j|)\|v\|_2^2\), by (2).

Here the negative-frequency and zero-crossing cases require
no differentiability of \(|k|\). From the symmetry in (2),
\[
 p_\ell(-t)=p_{-\ell}(t),\qquad \mu(-t)=\mu(t),
\]
and hence the sum in (4) is the same at \(t\) and \(-t\).
If \(n,k\) lie in the window, then
\[
 \left|N[W(|n|/N)-W(|k|/N)]\right|
 \le |n-k|
       \sup_{\substack{|v-|\nu_j||\le(L+11)/N\\v\ge0}}\lambda(v).
                                                                    \tag{9}
\]
This follows from \(\big||n|-|k|\big|\le|n-k|\) and the
integral definition of \(W\). It remains valid when the
window crosses zero.

Uniform continuity of \(p_\ell\) and \(\lambda\), the fixed
bandwidth, and row and column sums now bound the difference
between the weighted window matrix and \(P_j^0\) by
\[
 \mathcal D(|\nu_j|,\lambda(|\nu_j|))+o(1)
                         \le\frac{\mu(|\nu_j|)}4+o(1),           \tag{10}
\]
where the \(o(1)\) is uniform over all windows and both signs.
For example, the additional factor in an entry is bounded by
\(e^{|\ell|\lambda}-1\), with the local supremum in (9);
freezing \(p_\ell(k/N)\) costs another uniform \(o(1)\).
The frozen matrix is Hermitian; no such claim is made for (7).

Summing the window inequalities and using (8) proves, for
all sufficiently large levels,
\[
 \Re\langle f,B_{I,N}f\rangle
       \ge\left(\frac{3\mu_\alpha}{4}-o(1)-\frac CL\right)
                                             \|f\|_2^2
       \ge\frac{\mu_\alpha}{2}\|f\|_2^2.                         \tag{11}
\]
Both \(\mathcal P_N\) and \(E_{W,N}\) preserve even Fourier
sequences. Thus (11) also holds on their even restriction.
Compression at the two band endpoints uses zero extension
throughout; it introduces no missing endpoint term.

## 3. The actual finite operator in the varying norm

Write
\(\mathcal R_N=\mathcal C_N-\mathcal P_N\).
The full-shift source proves, at every fixed \(\rho>0\),
\[
 \|\mathcal R_Nf\|_{\rho,2}\le C_\rho N^{-1}\|f\|_{\rho,2}
                                                                    \tag{12}
\]
for even trigonometric polynomials. This is its exact coefficient
comparison on the two nonreal Hardy lines. It does not assume
removability of the individual finite coefficients.

Use the orthonormal cosine basis \(1,\sqrt2\cos u,\sqrt2\cos2u,\ldots\).
The one-column consequence of (12) is
\[
 |(\mathcal R_N)_{n,k}|
       \le C_\rho N^{-1}e^{\rho(k-n)}
                         \qquad(n,k\ge0).                       \tag{13}
\]
The norm equivalence follows directly from
\(\cosh(2k\rho)\asymp e^{2k\rho}\).
Ordinary polynomial degree gives the further exact fact
\[
                  (\mathcal R_N)_{n,k}=0\qquad(n>k+11).          \tag{14}
\]
This uses the degree bound for both operators, not a decay
estimate for a raw rational coefficient.

Put \(\lambda_-=\min\lambda>0\), \(\lambda_+=\max\lambda\),
and fix \(0<\rho<\lambda_-\). For \(n\le k\),
conjugating (13) by (5) gives
\[
 |(E_{W,N}\mathcal R_NE_{W,N}^{-1})_{n,k}|
 \le C_\rho N^{-1}
                  e^{-(\lambda_--\rho)(k-n)}.                  \tag{15}
\]
For \(k<n\le k+11\), it instead gives a bound by
\(C_\rho N^{-1}e^{11\max(\lambda_+-\rho,0)}\).
There are only eleven such upward diagonals.
Geometric row and column sums in (15), together with (14),
therefore prove
\[
 \|E_{W,N}\mathcal R_NE_{W,N}^{-1}\|
                             \le C_{\alpha,\lambda}/N            \tag{16}
\]
from degrees at most \(K_N\) to all its possible output degrees.
This is a one-sided finite-degree argument. No unproved
variable-strip version of (12) is used.

Combining (11),(16), the actual even compression
\[
 A_{I,N}^{\rm ev}
   =\Pi_N\mathcal C_N\big|_{\{\text{even polynomials of degree}
                                                    \le K_N\}}
\]
is invertible and obeys
\[
 \boxed{\quad
 \Re\langle f,E_{W,N}A_{I,N}^{\rm ev}E_{W,N}^{-1}f\rangle
                 \ge\frac{\mu_\alpha}{4}\|f\|_2^2,\qquad
 \|E_{W,N}(A_{I,N}^{\rm ev})^{-1}E_{W,N}^{-1}\|
                 \le\frac4{\mu_\alpha}.
 \quad}                                                         \tag{17}
\]
The corresponding norm of \(\mathcal C_N\) from solved inputs
to all output modes is bounded by a fixed constant, by (7),
(14)--(16). This includes the eleven modes above the solved band.

## 4. Literal residual and the outgoing action profile

For an even polynomial \(F_N\), solve exactly
\[
 g_N=(A_{I,N}^{\rm ev})^{-1}\Pi_NF_N,\qquad
 \rho_N=F_N-\mathcal C_Ng_N.                                    \tag{18}
\]
Then \(\Pi_N\rho_N=0\). The contribution of the operator image
above this band is confined to
\(K_N+1,\ldots,K_N+11\) in the cosine basis.
All larger residual coefficients equal the original input
coefficients. In particular the eleven boundary outputs cannot
be replaced by the corresponding coefficients of \(F_N\).

Take the actual attached polynomial from
[action-weighted Green interpolation](research_mixed_next_outgoing_action_weighted_green_ellipse.md):
\[
 F_N^+(\zeta,Z)=
 \sum_{b=M}^{D}(-q)^b C_{b,N}(Z)P_b^{\rm rad}(\zeta),
 \qquad
 P_b^{\rm rad}(\zeta)=e_b(\zeta)/e_M(\zeta).
                                                                    \tag{19}
\]
It has degree at most \(U=D-M\). Its exact original scalar in
the transfer is still \((\kappa_N^2N)^{-1}\).
Write
\[
 E_Z(t)=\mathcal E(1/2+t,Z),\qquad 0\le t\le1/2,
\]
where \(\mathcal E\) is the original terminally normalized
outgoing action. The adopted finite-source coefficient bound is
\[
 |f_{k,N}(Z)|\le C N^A e^{NE_Z(k/N)},\qquad 0\le k\le U,
                                                                    \tag{20}
\]
in the cosine expansion of \(F_N^+(-2\cos u,Z)\).
Changing from Chebyshev to this normalized cosine basis changes
only fixed factors and signs. The complete terminal coefficient
is included.

The function \(E_Z\) is continuous on \([0,1/2]\), smooth on
every compact subinterval below \(1/2\), and decreasing.
Uniformly over the actual outgoing rectangle, the same source
gives
\[
 E_Z(0)-E_Z(t)\ge c_*t,\qquad
 c_*=\frac18+\frac{53}{37800}.                                 \tag{21}
\]
Define the exact profile bound
\[
 \mathcal G_W(\alpha,Z)
   =\max_{0\le t\le\alpha}\{E_Z(t)+W(t)\}-W(\alpha).             \tag{22}
\]
In particular
\(\mathcal G_W(\alpha,Z)\ge E_Z(\alpha)\).

The weighted norm of the solved input is bounded by
\[
 \|E_{W,N}\Pi_NF_N^+\|_2
 \le C N^{A+1}
       \exp N\max_{0\le t\le\alpha}\{E_Z(t)+W(t)\}.              \tag{23}
\]
Equations (17)--(18) bound the full weighted operator output
by the same expression. On each of the eleven boundary modes,
\(W(n/N)=W(\alpha)+O(N^{-1})\), uniformly since
\(K_N=\lfloor\alpha N\rfloor\). Their ordinary coefficients,
including the original \(F_N^+\) coefficients there, are
therefore bounded by \(CN^{A'}e^{N\mathcal G_W}\).
Above that band the coefficients equal \(f_{n,N}\); decreasing
\(E_Z\) gives their bound by \(CN^Ae^{NE_Z(\alpha)}\).
There are at most \(N\) such coefficients.

Consequently the exact residual satisfies
\[
 \boxed{\quad
 \|\rho_N\|_{\mathbb R}
      \le C N^{A'} e^{N\mathcal G_W(\alpha,Z)}.
 \quad}                                                         \tag{24}
\]
All rounding errors in the eleven modes are \(O(1)\) in the
exponent, because \(\alpha<1/2\) is fixed. No endpoint derivative
of \(E_Z\) at \(1/2\) is used for the literal higher tail.

Equivalently the proved gain from \(E_Z(0)\) is
\[
 \delta_W(\alpha,Z)=
 \min_{0\le t\le\alpha}
 \{E_Z(0)-E_Z(t)+W(\alpha)-W(t)\}.                              \tag{25}
\]
It is strictly positive: (21) and
\(W(\alpha)-W(t)\ge\lambda_-(\alpha-t)\) give
\[
                 \delta_W(\alpha,Z)
                      \ge\alpha\min(c_*,\lambda_-)>0.           \tag{26}
\]
The complete profile in (25), rather than this coarse minimum,
is available when checking an actual attachment budget.

## 5. Original forcing and the exact coherent criterion

The solution \(g_N\) in (18) is the unique solution of the same
finite compressed system regardless of the norm used to bound it.
Choose also a sufficiently small constant Hardy weight
\(0<\rho_b\le1/8\) satisfying the constant-weight condition in
the full-shift theorem. That theorem and the adopted closed
\(1/8\)-ellipse bound give
\[
            \|g_N\|_{\mathbb R}\le C N^A e^{NE_Z(0)}.            \tag{27}
\]
This bounds the very same solution as (17); it does not
introduce another test or replace the variable-weight boundary
estimate.

Put \(h_N=Q_{3,N}^{\rm rev}g_N\).
Ordinary divisibility, its three exact endpoint zeros, and the
original full Hermite transpose give
\[
 \mathcal L_N(F_N^+)
       =\mathfrak f_N\ell_N(h_N)+\mathcal L_N(\rho_N),\qquad
 \mathfrak f_N=
 \begin{cases}
 4\kappa_N^3/N^2,&N\ \mathrm{even},\\
 0,&N\ \mathrm{odd},
 \end{cases}                                                    \tag{28}
\]
with the original functionals of the full-shift source.
Every first normal and the odd simple node is retained.
The consumed-normal formula bounds the forcing using (27);
it is exactly zero at odd levels. Applying the adopted
complete physical inner bound to (24) proves, for every
fixed \(\tau>0\),
\[
 \boxed{\quad
 |\mathcal L_N(F_N^+(\cdot,Z))|
 \le C_\tau N^{A_\tau}
       \left\{e^{NE_Z(0)}
          +e^{N[\mathfrak M_3+\mathcal G_W(\alpha,Z)+\tau]}\right\}.
 \quad}                                                         \tag{29}
\]
This is an estimate on the exact finite source. No algebraic
relative packet error is dropped inside a cancelling sum.

A sufficient uniform strict budget is consequently
\[
 E_{Z_*}(0)<\Lambda,\qquad
 \mathfrak M_3+\mathcal G_W(\alpha,Z_*)<\Lambda.                  \tag{30}
\]
The first inequality bounds the even forcing term. The second
is equivalent to
\(\delta_W(\alpha,Z_*)>
\mathfrak M_3+E_{Z_*}(0)-\Lambda\).
Because \(t=0\) is one competitor in (22), a **necessary
condition for this particular sufficient criterion** is
\[
 \boxed{\qquad
 W(\alpha)>
           \mathfrak M_3+E_{Z_*}(0)-\Lambda .
 \qquad}                                                       \tag{31}
\]
This is not a necessary condition for cancellation in the
original signed observation. It records a limitation of the
proved boundary majorant, whose low input modes can generate
high boundary outputs through the compressed inverse.

The literal high input tail benefits from \(E_Z(1/2)=0\).
That fact alone does not bound the eleven generated modes.
Nor does real-symbol positivity authorize the action-shaped
choice \(W'(t)=-E_Z'(t)\): it would still have to satisfy a
proved finite conjugation condition such as (4), uniformly
on the chosen band. The explicit weight (6) and all estimates
(17)--(29) are proved; an admissible choice satisfying (30)
has not been established. There is no assertion at
\(\alpha=1/2\), where the principal central symbol degenerates,
and no finite-exception conclusion.

## Source versions

- Full leading shifts, exact finite compression and Hardy comparison:
  7b11e96c482d3c435e3fac0d9a488d0025aae31e2ec9d806949858031381b84c.
- Exact outgoing action profile and complete attachment:
  e39abb76185b6969901b6ee4c95a4f947bdda5f74d8ff57062ed4b6591a0c029.
- Global grouped operator, ordinary removability and full pairing:
  cb47c9d87949e276615443150b2da2260fec5bb09d3780039b90b322cd14eeb8.
- Ordinary divisibility and degree increase:
  c5cb10096ed4c6aafefdc957958ddaf392ad17c81cab5e7e99dbbe026fc1aed3.

No numerical evaluation, saved-value calculation, or replay was used.

