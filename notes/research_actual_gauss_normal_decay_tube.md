# The actual Gauss matrix normal on an asymmetric decay tube

Private written proof, 19 November 2026.

This note estimates the actual inhomogeneous matrix normal, including
its axis injection. On a small negative-activity annulus in the first
variable it is a bounded multiple of the root first column in the
second variable, with an absolute \(O(N^{-1})\) remainder. The second
disk is chosen after the annulus, the analytic parametrix, and the
finite-cap constants. In particular the physical matrix normal is
\(O(N^{-1})\) on compact negative-activity subsets of that tube.
This is leading-order cancellation; it is not an exponentially small
normal estimate or an estimate of the binomial-input closing circle.

The two complete directs are R and N, pinned below. R supplies the
actual symmetric normal, its exact finite Green current and root
matrix kernel. N supplies the whole-meridian first column and its
two normal sectors. All estimates below are at fixed \(q=q_N\).

## 1. Actual normalization and the domain of the estimate

Use
\[
 c_0=2\pi i,\quad Q=e^{c_0/N},\quad q=e^{c_0/(2N)},\quad
 d=N-1,\quad \mathsf x=-q^{-1},\quad C=Q^{-T-1},
 \qquad (T+1)/N\in I\Subset(1/2,1).
 \tag{1}
\]
The degree-\(T\) physical basis is \(e_a=|a,T-a\rangle\).
Retain the exact root vacuum and monomial kernels
\[
 a_{00}=(-1)^d C^d f_T^2,\qquad \bar A=A_N(1)/a_{00},
 \quad
 \mathcal K_0(\rho,\zeta)
 =\sum_{a,j=0}^T\mathsf x^{-a-j}\bar A_{aj}\rho^a\zeta^j,
 \quad G_N(\rho)=\mathcal K_0(\rho,0).
 \tag{2}
\]
Here \(f_a=(Q;Q)_a\). R's actual diagonal symmetrizer is
\[
 S_a(M)^2=
 \frac{g_T(M)f_{T-a}}{g_{T-a}(M)f_T}\frac{f_a}{g_a(M)},
 \quad g_a(M)=(M^{-2}Q;Q)_a,\quad S_a(1)=1.
 \tag{3}
\]
Primes mean the true derivative \(\partial_\mu|_0\), \(M=e^\mu\).
Set
\[
 B=a_{00}^{-1}(S^{-1}A_N(M)S)'|_0,\qquad
 \mathcal K_B=\sum_{a,j=0}^T\mathsf x^{-a-j}B_{aj}\rho^a\zeta^j.
 \tag{4}
\]
The normalization \(a_{00}\) is fixed in (4).

On a uniform root disk the adopted kernels have representations
\[
 G_N=e^{N\phi}a_N^{\rm bd},\qquad
 \mathcal K_0=e^{N S_0}a_N^0,\qquad
 \phi'(0)=c_*:=2/c_0,
 \quad S_0=c_*(\rho+\zeta)+O((|\rho|+|\zeta|)^2),
 \tag{5}
\]
with bounded analytic unit amplitudes and their inverses.
The amplitudes have analytic \(O(N^{-1})\) expansions.
The root parameter \(C\) in these statements is the exact one in (1).

Fix a closed angular cone strictly inside
\(\Re(c_*\rho)<0\). Choose all activities sufficiently small.
Let \(\Omega_*\) be any compact annular patch in that cone,
with a bounded complex neighborhood \(\Omega\) whose closure
avoids zero and remains inside a slightly larger negative cone.
The upper radius is required to be smaller than the common
root and cap radii specified in the proof. The lower radius can
be any positive fixed number below it.

There are \(r_\zeta>0\), a uniformly analytic bounded function
\(a_N(\rho,\zeta)\), and constants independent of \(N,T\), such that
on \(\Omega_*\times\{|\zeta|\le r_\zeta\}\)
\[
 \boxed{\quad
 \mathcal K_B(\rho,\zeta)=G_N(\zeta)a_N(\rho,\zeta)+O(N^{-1}),
 \qquad
 a_N=\frac{C-1}{\rho(\lambda_G(\zeta)-2)}+O(N^{-1}).
 \quad}                                                     \tag{6}
\]
Here
\[
 \lambda_G(z)=\Lambda(z,\phi'(z)),\qquad
 \Lambda(z,p)=2+
    \frac{(1-z)^2(1-e^{c_0zp})(1-Ce^{c_0zp})}{z},
 \quad \lambda_G(0)=2C.
 \tag{7}
\]
All displayed singularities at \(z=0\) are removable.
The disk \(r_\zeta\) is chosen after the annular buffers and
parametrix residual rate. It can be much smaller than \(|\rho|\).
No estimate on every product decay cone is asserted.

In particular, on any compact patch
\(\Xi_*\Subset\{0<|\zeta|<r_\zeta\}\) in the same fixed
closed negative-activity cone,
\[
 \mathcal K_B=O(N^{-1}),\qquad
 \mathcal K_{A'}=O(N^{-1})
                  \quad\hbox{on }\Omega_*\times\Xi_*,
 \tag{8}
\]
where \(\mathcal K_{A'}\) is the physical normal divided by
\(a_{00}\), with the fixed monomial normalization of (2).
All fixed activity derivatives have these orders on smaller
compact subsets. Formula (6), not (8), includes \(\zeta=0\).

## 2. The exact forced clock equation and its terminal terms

Write \(\mathsf T_z f(z)=f(Qz)\) and
\[
 \mathscr D_z=
 C(1-Qz)(1-Q^2z)\mathsf T_z^2
 -(1+C)(1-Qz)^2\mathsf T_z+1+Qz^2.
 \tag{9}
\]
The root Jacobi action on a monomial kernel is
\(q^{-1}\mathscr D_z/z\); its apparent pole is removable.
R proves
\[
 [J,B]=[\bar A,J_1],\qquad
 (J_1)_{a+1,a}=(J_1)_{a,a+1}=(C-1)Q^{a+1},
 \quad (J_1)_{aa}=2q(C-1)Q^a.
 \tag{10}
\]
Put \(R_T(\zeta)=[\rho^T]\mathcal K_0(\rho,\zeta)\).
The literal finite left \(J_1\) action is
\[
 -\frac{q^{-1}(C-1)}{\rho}
 \left\{(1-Q\rho)^2\mathcal K_0(Q\rho,\zeta)
       -G_N(\zeta)-Q^{T+2}\rho^{T+2}R_T(\zeta)\right\}.
 \tag{11}
\]
For example, the lower arrow contributes
\(-qQ(C-1)\rho\,\mathcal K_0(Q\rho,\zeta)\); removing its
forbidden last state adds \(qQ^{T+1}(C-1)\rho^{T+1}R_T\),
which is precisely the final term of (11).
The upper arrow removes its first state and supplies \(G_N(\zeta)\).
Thus, with \(\mathcal L_N=\mathscr D_\rho/\rho-\mathscr D_\zeta/\zeta\),
\[
 \begin{split}
 \mathcal L_N\mathcal K_B=(C-1)\{&
 (1-Q\rho)^2\mathcal K_0(Q\rho,\zeta)/\rho-G_N(\zeta)/\rho\\
 &-(1-Q\zeta)^2\mathcal K_0(\rho,Q\zeta)/\zeta+G_N(\rho)/\zeta\\
 &-Q^{T+2}\rho^{T+1}R_T(\zeta)
   +Q^{T+2}\zeta^{T+1}R_T(\rho)\}.
 \end{split}                                                \tag{12}
\]
Symmetry of \(\bar A\) was used for the last term.
The two terms divided by \(\zeta\) stay as one analytic
divided difference. No infinite Jacobi row replaces (12).

All actual coefficients in \(\mathcal K_0,\mathcal K_B\) are bounded
by \(e^{cN}\), uniformly in (1). For \(\mathcal K_0\) this follows
from the finite formula in R. For \(\mathcal K_B\), use R's
finite continuant formula and N's actual first-column coefficients.
The latter retain their aliases and satisfy the same bound after
the true derivative insertion \(O(N\log(N+1))\).
Products of interior Jacobi arrows have upper and lower bounds
\(e^{\pm cN}\); the continuant determinants have \(c^N\) bounds.
These observations give the stated whole-matrix coefficient bound
without a spectral condition number.

Consequently the terminal terms in (12) are \(e^{-cN}\) on a
sufficiently small fixed \(\rho\) disk and then a sufficiently
small \(\zeta\) disk. On a buffered negative \(\rho\) annulus,
(5) makes the other root terms exponentially small when the
comparison \(\zeta\) disk is sufficiently small. For the divided
difference at \(\zeta=0\), use Cauchy on a slightly larger such
disk. We obtain the actual equation
\[
 \mathcal L_N\mathcal K_B
     =-\frac{C-1}{\rho}G_N(\zeta)+\mathcal R_N,\qquad
                  \|\mathcal R_N\|\le e^{-cN}.
 \tag{13}
\]
Equation (13) is a bound on the full complex comparison tube,
including growing directions of \(G_N(\zeta)\). Its proof only
uses root decay in the first variable for the terms in
\(\mathcal R_N\). The isolated axis source is not discarded.

## 3. The actual half-axis boundary

Let \(\Sigma_n=\sum_{j=1}^nQ^j/(1-Q^j)\) and
\(s_n=\Sigma_T-\Sigma_{T-n}-\Sigma_n\).
R and N give the exact boundary
\[
 \mathcal K_B(\rho,0)
 =\mathcal H_N(\rho)+(2d+D-s(D))G_N(\rho),
 \quad D=\rho\partial_\rho,\qquad
 \mathcal H_N(\rho)=\rho^{-1}+O(N^{-1})
 \tag{14}
\]
on the negative annulus. We need the gauge term at the same
accuracy; its norm estimate alone would not suffice.

The following actual multiplier estimates hold there:
\[
 \Sigma(D)G_N=-\frac1{2\rho}+O(N^{-1}),\qquad
 [\Sigma_T-\Sigma_{T-D}]G_N=O(N^c e^{-c'N}).
 \tag{15}
\]
Here and below a finite multiplier acts on the physical
coefficients \(0,\ldots,T\).
We give details of its endpoint and analytic remainder.

For \(n\le\delta N\), put
\[
 r(y)=\frac{e^{c_0y}}{1-e^{c_0y}}+\frac1{c_0y},
 \quad r(0)=-\tfrac12.
 \]
Then, exactly,
\[
 \Sigma_n=-\frac N{c_0}H_n+\sum_{j=1}^n r(j/N),
 \qquad H_n=\sum_{j=1}^n j^{-1}.
 \tag{16}
\]
The smooth sum has a uniformly analytic interpolation of size
\(O(N)\), with an exponentially small nodal error. Indeed truncate
Euler--Maclaurin at \(L=\lfloor\delta_1N\rfloor\):
\[
 \begin{split}
 A_N(y)={}&N\int_0^y r(v)\,dv+\frac{r(y)-r(0)}2\\
 &+\sum_{k=1}^{L-1}\frac{B_{2k}}{(2k)!}N^{1-2k}
       \{r^{(2k-1)}(y)-r^{(2k-1)}(0)\}.
 \end{split}                                                \tag{17}
\]
Choose \(\delta,\delta_1\) inside a fixed analytic disk of \(r\).
Cauchy's derivative bound and
\(|B_{2k}|/(2k)!\le C(2\pi)^{-2k}\) bound the \(k\)-th term
by \(CN(Ck/N)^{2k}\), and the remainder by
\(CN(CL/N)^{2L}\). Taking \(\delta_1\) small gives a bounded
analytic \(A_N/N\) and a remainder \(e^{-cN}\).
The same construction for the sum from \(T-n+1\) to \(T\)
is uniform, since \(T/N\) stays away from both endpoints.

Apply N's cancellation-preserving analytic multiplier lemma to
\(A_N/N\). It keeps the root phase and gives an \(O(N)G_N\)
bound. For the low-index nodal remainder, use the finer
root-unit bound \(\sup_{|\rho|=R}|G_N|\le C e^{CNR}\).
Choose this comparison radius after the Euler--Maclaurin
remainder exponent, so its coefficient sum on \(|\rho|<R/2\)
costs less than half that exponent. The nodal error is then
exponentially small after summation. For coefficients above
\(\delta N\), the coarse \(e^{cN}\) physical bound and a further
fixed reduction of the evaluation radius give the exponential
tail. This does not apply an absolute coefficient estimate to
the low analytic multiplier. The same reasoning proves the
second estimate in (15).

The harmonic part is exact:
\[
 H(D)G_N=\int_0^1
           \frac{G_N(\rho)-G_N(x\rho)}{1-x}\,dx .
 \tag{18}
\]
Keep the numerator together near \(x=1\); it and its derivatives
are exponentially small there. On the remaining segment the
radial phase is strictly decreasing. The \(x=0\) layer uses
\(G_N(0)=1,\ \phi'(0)=c_*\) and gives
\[
 H(D)G_N=\frac1{Nc_*\rho}+O(N^{-2}).
 \tag{19}
\]
For example compare \(G_N(x\rho)\) with
\(\exp(Nc_*\rho x)\). The amplitude error is \(O(x)\), and the
phase error is \(O(Nx^2)\); their integrals are \(O(N^{-2})\).
Replacing \((1-x)^{-1}\) by one has the same error in this
layer. Away from it the bound is exponential. Combining
(16)--(19) proves (15), since \(c_0c_*=2\).
These estimates are holomorphic on a larger negative annulus,
so their fixed derivatives follow by Cauchy.

It follows that the true initial row is
\[
                 \mathcal K_B(\rho,0)
                     =\frac1{2\rho}+O(N^{-1}).
 \tag{20}
\]
This is the actual axis selection used below. It includes
the normal source of N and the moving symmetrizing gauge.

## 4. An exponentially accurate local axis particular

First use a fixed preliminary \(\zeta\) disk on which \(G_N\)
is a root unit. It need not be a decay disk. Conjugating the
operator in (13) by that exact polynomial gives
\[
 G_N(\zeta)^{-1}\mathcal L_N(G_N(\zeta)a)
                       =(g_N+\mathcal V_N)a,
 \tag{21}
\]
\[
 g_N=\beta_N(\rho)-\lambda_N(\zeta),\qquad
 \beta_N=\mathscr D_\rho1/\rho=2+O(N^{-1}),\quad
 \lambda_N=\mathscr D_\zeta G_N/(\zeta G_N)
                       =\lambda_G+O(N^{-1}).
 \tag{22}
\]
All errors are uniformly analytic on smaller domains. The
last expression is removable at zero; (5),(9) and Cauchy
give its stated estimate also there. Shrink the preliminary
disk so that \(|g_N|\ge c>0\), using \(\lambda_G(0)=2C\).

Every term of \(\mathcal V_N\) is a bounded analytic coefficient
times an exact short clock difference of \(a\). In the second
variable its possible division by \(\zeta\) is removable:
\[
 \frac{a(Q^k\zeta)-a(\zeta)}{\zeta}
 =(Q^k-1)\int_0^1
          \partial_\zeta a((1+t(Q^k-1))\zeta)\,dt,\quad k=1,2.
 \tag{23}
\]
The first variable stays away from zero. Hence on nested
analytic domains with buffer \(\Delta\), larger than \(c/N\),
\[
       \|\mathcal V_N a\|_{\rm inner}
                      \le \frac{C}{N\Delta}\|a\|_{\rm outer}.
 \tag{24}
\]
The exact ratios \(G_N(Q^k\zeta)/G_N(\zeta)\) in these
coefficients are bounded by (5); no exponential factor is
lost in (24).

Put \(f=-(C-1)/\rho\), \(V_N=g_N^{-1}\mathcal V_N\).
For \(L_N=\lfloor\delta_PN\rfloor\), define
\[
 a_N=\sum_{\ell=0}^{L_N-1}(-V_N)^\ell(g_N^{-1}f).
 \tag{25}
\]
Choose \(\delta_P>0\) small after fixed preliminary buffers.
Allocate a fixed total buffer among the \(\ell\) applications
in an individual term. Equation (24) gives
\[
 \|V_N^\ell(g_N^{-1}f)\|
                \le C(C_1\ell/N)^\ell,\qquad \ell\le L_N.
 \tag{26}
\]
The same bound applies to the last residual, with \(\ell=L_N\).
Make \(C_1\delta_P<1/4\). The terms with \(\ell\ge1\) sum to
\(O(N^{-1})\), and the residual is \(e^{-\eta N}\), for a
fixed \(\eta>0\). Each clock path fits its allocated buffer
because its displacement is \(O(N^{-1})\) and
\(\delta_P\) was chosen after that buffer. The estimates
also hold with fixed derivatives on smaller domains.
Thus
\[
 (g_N+\mathcal V_N)a_N=f+O(e^{-\eta N}),\qquad
 a_N=\frac{C-1}{\rho(\lambda_G(\zeta)-2)}+O(N^{-1}).
 \tag{27}
\]
In particular \(a_N(\rho,0)=1/(2\rho)+O(N^{-1})\).

Only now choose a smaller comparison \(\zeta\) disk.
Since \(|G_N(\zeta)|\le C\exp(C_2N|\zeta|)\), make its
radius less than \(\eta/(2C_2)\), and also small enough for
(13) on the buffered annulus. The parametrix residual after
multiplication by \(G_N(\zeta)\) is then exponentially small
on the whole comparison tube. Consequently
\[
 E_N:=\mathcal K_B-G_N(\zeta)a_N,\qquad
 \mathcal L_NE_N=\widetilde{\mathcal R}_N,\quad
 \|\widetilde{\mathcal R}_N\|\le e^{-\eta' N},\quad
 E_N(\rho,0)=O(N^{-1}).
 \tag{28}
\]
The last assertion is (20), not an inference from a small
residual. A homogeneous solution has not been suppressed.

## 5. Stable finite propagation from the selected axis

Here the exact linear coefficient recurrence, rather than a
global matrix inverse, controls the possible homogeneous part.
Write
\[
 \mathscr D_z=P_0(\mathsf T_z)+zP_1(\mathsf T_z)
                                      +z^2P_2(\mathsf T_z),
 \]
\[
 P_0(t)=(t-1)(Ct-1),\quad
 P_1(t)=-CQ(1+Q)t^2+2(1+C)Qt,\quad
 P_2(t)=Q(Qt-1)(CQt-1).
 \tag{29}
\]
For \(E_N=\sum_{j\ge0}e_j(\rho)\zeta^j\) and
\(\widetilde{\mathcal R}_N=\sum R_j(\rho)\zeta^j\), (28) gives
\[
 \begin{split}
 Nm_{j+1}e_{j+1}
  ={}&N\{\mathscr D_\rho/\rho-P_1(Q^j)\}e_j\\
     &-NQm_je_{j-1}-NR_j,\qquad
 m_j=(Q^j-1)(CQ^j-1),\quad e_{-1}=0.
 \end{split}                                                \tag{30}
\]
For \(j\le k_N=\lfloor\delta_SN\rfloor\), with fixed sufficiently
small \(\delta_S\),
\[
 |Nm_{j+1}|\asymp j+1,\quad
 |N(2-P_1(Q^j))|\le C(j+1),\quad |NQm_j|\le Cj.
 \tag{31}
\]
On the annulus the other operator in (30) is uniformly first order
in the following exact sense:
\[
 N(\mathscr D_\rho/\rho-2)
     =\sum_{\ell=1}^2 b_{\ell,N}(\rho)
        \int_0^1\partial_\rho
           (\cdot)((1+t(Q^\ell-1))\rho)\,dt+b_{0,N}(\rho),
 \tag{32}
\]
where all \(b_{\ell,N}\) are bounded analytic. To obtain (32),
subtract the value of each shifted function at \(\rho\),
use (23), and use \(N(\beta_N-2)=O(1)\).
It is not an \(N\partial_\rho^2\) estimate.

For completeness a padded Cauchy estimate proves uniform
stability of (30). Cover the desired annular patch by finitely
many smaller disks inside buffered disks
\(\Omega_0=\{|\rho-\rho_c|<R\}\) that avoid zero and remain
in the negative sector. It suffices to work in one of them.
Put \(\Omega_j=\{|\rho-\rho_c|<R-\kappa j/N\}\), with
\(\kappa\) larger than every clock displacement in (32).
Choose \(\delta_S\) so these domains contain a fixed inner
neighborhood of \(\Omega_*\). Put
\[
 \|v\|_{p,j}=\sup_{\rho\in\Omega_j}
       |v(\rho)|\,\operatorname{dist}(\rho,\partial\Omega_j)^p.
 \tag{33}
\]
Cauchy on a circle of radius
\(\operatorname{dist}(\rho,\partial\Omega_j)/(p+1)\) gives
\(\|\partial_\rho v\|_{p+1,j}\le e(p+1)\|v\|_{p,j}\).
For \(p=0\) use half that distance, changing only the constant.
The padding ensures that every point in a clock path from
\(\Omega_{j+1}\) belongs to \(\Omega_j\), with distance to
its boundary at least the original distance to
\(\partial\Omega_{j+1}\). The same weighted derivative bound
therefore applies inside (32).

Taking \(p=j\) in (30), the factor \(j+1\) from Cauchy
cancels the denominator in (31). The zero-order and
previous-row terms have the same bounded recurrence cost.
Cauchy for \(R_j\) on the comparison \(\zeta\) disk gives
\[
 \|e_j\|_{j,j}\le
       C_3^j\{N^{-1}+N e^{-\eta'N}\},
                   \qquad 0\le j\le k_N.
 \tag{34}
\]
This follows by induction; the diameter factors from
changing weights \(j\) to \(j+1\), or \(j-1\) to \(j+1\),
are bounded constants. The forcing coefficients add a
geometric sequence, absorbed by increasing \(C_3\).
On the fixed inner neighborhood the boundary distances in
(33) are at least a fixed \(\Delta_*>0\). Thus
\(|e_j|\le(C_3/\Delta_*)^j\{N^{-1}+Ne^{-\eta'N}\}\);
the low \(\zeta\) series is \(O(N^{-1})\) on a fixed smaller disk.

Finally recover its whole cap. The actual coefficients of
\(\mathcal K_B\) have the \(e^{cN}\) bound after (12).
The analytic particular \(G_N(\zeta)a_N\) has the same
type of Cauchy bound on a fixed comparison disk, by (26).
Hence the terms of \(E_N\) above \(k_N\) are bounded by
\[
             Ce^{c_4N}(r_\zeta/R_\zeta)^{k_N+1}.
 \tag{35}
\]
Choose the final \(r_\zeta\) after \(c_4,\delta_S,R_\zeta\)
so (35) is exponentially small. This retains the physical
matrix cap and also the infinite analytic tail of the
particular. It applies no ill-conditioned inverse to an
error controlled only at a small radius. Equations
(28),(34),(35) prove (6).

## 6. Physical gauge and source scope

On compact negative \(\zeta\) patches the factor \(G_N(\zeta)\)
in (6) is exponentially small, proving the first part of (8).
R's exact restoration is
\[
 \mathcal K_{A'}=\mathcal K_B+
                [s(D_\rho)-s(D_\zeta)]\mathcal K_0.
 \tag{36}
\]
Both terms on the right of this gauge correction are exponentially
small up to powers of \(N\) on \(\Omega_*\times\Xi_*\).
For the harmonic multiplier use the exact integral (18)
in the relevant variable. Along either radial segment the
other variable remains in its fixed negative patch; (5) gives
a uniform exponential gap even at the zero endpoint.
Near the other endpoint keep the divided difference.
For the analytic smooth multipliers use (17) and N's multiplier
lemma with the other variable as a compact analytic parameter.
The high coefficients have the same finite-cap bound as before.
This proves the physical estimate in (8).

At the microscopic second axis, (6) also records the actual
injection, uniformly for bounded \(w\):
\[
        \mathcal K_B(\rho,w/N)
            =\frac{e^{c_*w}}{2\rho}+O(N^{-1}).
 \tag{37}
\]
The origin in the first variable is excluded. No assertion of
an exponentially small remainder beyond (8) is made.

For \(M=e^{u/N}\), the true \(u\)-normal is \(N^{-1}\)
times the \(\mu\)-normal throughout this note. No whole
meridian-disk estimate or quantum-parameter derivative follows.
The original binomial input still requires exactly R's finite
constant-term pairing
\[
 v(w)A_N'(1)c(z)=a_{00}(w_2z_2)^T\binom dT
       \operatorname{CT}_{\zeta}
            \mathcal K_{A'}(\rho,\zeta)\mathcal B_T(\eta/\zeta).
 \tag{38}
\]
Its entire circle need not lie in the asymmetric tube.
The exterior braid, turnover, inverse Cartan coupon, cut,
pivotal insertions and closing finite part retain their
own normals. The present absolute \(O(N^{-1})\) estimate
does not identify a geometric branch, prove source incidence,
or imply a closed invariant bound or noncancellation.

## Complete proof directs

* R: notes/research_actual_gauss_matrix_normal_green_current.md,
  524 lines, SHA256
  05bd72cc4ea051287363e0a410a99b48fad5aea8b1588674fd6c502443df0439.
* N: notes/research_actual_gauss_first_column_meridian_normal.md,
  695 lines, SHA256
  6315ba61735d2f37363f59037fa4c0cb59f1cb729a20c6159a9e1b54d40f46d4.

Only written mathematics and text/hash operations are used.
Both complete directs were freshly read nontruncated in this
author sequence. The entire matching final was then freshly
reread nontruncated, every used implication checked, and all
three hashes renewed. Independent matching review and adoption
remain separate.
