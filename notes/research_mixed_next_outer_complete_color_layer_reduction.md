# The actual outer observation reduces to a fixed complete-color layer

Private finite-source theorem, 8 November 2026. The bounded interior
adjoint inverse eliminates every physical node outside an arbitrarily
small fixed neighborhood of the complete color. The far-side terms
are paid by the original full inner-kernel estimate. The resulting
complete-color layer retains the actual insertion, with explicit
corrections at its first three nodes.

A banded inverse estimate shows that these corrections have uniformly
bounded coefficient norm and exponentially decreasing dependence on
distant interior data. It does not make the remaining layer small.
No numerical evaluation or frozen-source edit is used.

## 1. Original source and exact cutoffs

Keep the actual complete reference for a word in powers three and
four beginning \(343\), of length at least five, with \(w=-2\)
and \(Z=Z_*\). The adopted
[outer Casimir observation](research_mixed_next_three_outer_casimir_observation.md)
gives
\[
\begin{gathered}
 D=N-1,\quad q=e^{\pi i/N},\quad \kappa_N=q^{D^2/2},\quad
 m=\lfloor N/2\rfloor,\quad U=m-1,\quad M=\lceil N/2\rceil,\\
 c_j=2\cos((2j+1)\pi/N),\qquad
 u_{j,N}=\pi-(2j+1)\pi/N,\qquad
 q_{j,N}=Q_N^{\rm full}(c_j),\\
 \mathcal L_N(H_N)
       =\sum_{j=0}^{U}\mu_{j,N}H_N(c_j,Z_*)q_{j,N},\\
 \mu_{j,N}=(-1)^U\kappa_N^3\omega_N(u_{j,N})q^{3j(j+1)},\\
 \omega_N(u)=
 \begin{cases}
 \sin u,&N\ \text{even},\\
 \sin u\sin(u/2)/\cos^2(\pi/(2N)),&N\ \text{odd}.
 \end{cases}
\end{gathered}                                                     \tag{1}
\]
The values \(q_{j,N}\) are those of the original full Hermite
inner trace. Its shortened second edge has exactly the same
physical values; no statement about their off-grid derivatives
is used. At odd levels the simple complete node has already been
treated in the original full trace and radical contraction.
It is not added as another term to (1).

The insertion is the literal outgoing polynomial \(H_N\), not an
approximation to it. Put
\[
 \Lambda=\Re\mathcal P_*>\frac{419}{200},\qquad
 B_0=\frac{2383}{1500},\qquad
 E_*=\Lambda-B_0-\frac1{50},\qquad
 G_N=\max_{0\le j\le U}|H_N(c_j,Z_*)|.
                                                                  \tag{2}
\]
The complete real-polynomial source bound is
\[
 G_N\le C_\tau N^{A_\tau}e^{N(E_*+\tau)}
                       \qquad(\tau>0).
                                                                  \tag{3}
\]
It retains the full outgoing sum and the separately paid
small-index subtraction.

Fix any
\[
                         0<\delta<\pi/2.
                                                                  \tag{4}
\]
Define integer cutoffs
\[
 a_N=\lfloor N/24\rfloor,\qquad
 b_N=\left\lfloor\frac{N(\pi-\delta)}{2\pi}-\frac12\right\rfloor,
 \qquad I_N=[a_N,b_N]\cap\mathbb Z.
                                                                  \tag{5}
\]
All following statements are for sufficiently large \(N\),
depending on this fixed \(\delta\). Then \(I_N\) is nonempty,
its six-index neighborhood is regular, and
\[
 \delta\le u_{b_N,N}<\delta+\frac{2\pi}{N},\qquad
 0<u_{k,N}<\delta\quad(b_N<k\le U).
                                                                  \tag{6}
\]
In particular \(b_N+3\le U\). The endpoints near the far color
satisfy
\[
 u_{j,N}\ge\frac{11\pi}{12}+\frac{\pi}{N}
       \quad(0\le j<a_N),\qquad
 u_{a_N,N}\le\frac{11\pi}{12}+\frac{\pi}{N}.
                                                                  \tag{7}
\]
Thus \(I_N\), with all needed neighbors, lies in one fixed
interior chart, for example inside a slightly enlarged
neighborhood of \([\delta/2,23\pi/24]\).

## 2. The actual inverse and its localized coefficient response

Let \(A_{I_N,N}\) be the exact zero-extended weighted adjoint
from the adopted
[interior Dirichlet theorem](research_mixed_next_outer_interior_dirichlet_inverse.md).
The matrix is banded with width three and satisfies
\[
 \Re\langle f,A_{I_N,N}f\rangle\ge3\|f\|_2^2,\qquad
                    \|A_{I_N,N}^{-1}\|_{2\to2}\le1/3 .
                                                                  \tag{8}
\]
Its entries are the original coefficients
\[
 (A_{I_N,N})_{i,i-r}
       =\frac{\mu_{i-r,N}}{\mu_{i,N}}d_{i-r,r,N},
                      \qquad |r|\le3.
                                                                  \tag{9}
\]
They are bounded by a constant \(C_\delta\ge1\), uniformly in
the level and parity on this fixed chart. The statement refers
to the actual ratios in (9), with their crossing phases.

We record a useful bound for this specific inverse. Enlarge
\(C_\delta\), if necessary, to bound each entry in (9), and set
\[
       \gamma_\delta=\frac13
                   \log\left(1+\frac1{7C_\delta}\right)>0.
                                                                  \tag{10}
\]
For real \(\gamma\), conjugate the finite matrix by
\(\mathsf E_\gamma=\operatorname{diag}(e^{\gamma i})_{i\in I_N}\).
Each entry at displacement \(r\) acquires \(e^{\gamma r}\).
The row and column sums of the difference are therefore at most
\[
                  7C_\delta(e^{3|\gamma|}-1).
                                                                  \tag{11}
\]
The elementary row/column estimate for the Euclidean operator
norm gives the same bound for that difference. At
\(\gamma=\pm\gamma_\delta\) it is at most one. Equation (8)
then gives
\[
 \Re\langle f,\mathsf E_\gamma A_{I_N,N}
                  \mathsf E_\gamma^{-1}f\rangle\ge2\|f\|_2^2,
 \qquad
 \|(\mathsf E_\gamma A_{I_N,N}
                  \mathsf E_\gamma^{-1})^{-1}\|_{2\to2}\le1/2 .
                                                                  \tag{12}
\]
These are estimates of the conjugated actual band matrix,
not an assumption that its diagonal conjugation is well
conditioned uniformly in the interval length.

Choose the sign of \(\gamma\) according to \(i-\ell\).
Since the inverse in (12) equals
\(\mathsf E_\gamma A_{I_N,N}^{-1}\mathsf E_\gamma^{-1}\),
its single-entry bound proves
\[
 \boxed{\quad
 |(A_{I_N,N}^{-1})_{i\ell}|
       \le\frac12 e^{-\gamma_\delta|i-\ell|}
                       \qquad(i,\ell\in I_N).
 \quad}                                                          \tag{13}
\]
In particular, with
\[
 C_{\infty,\delta}
       =\frac12\left(1+\frac{2}{e^{\gamma_\delta}-1}\right),
                                                                  \tag{14}
\]
the inverse also satisfies
\[
                \|A_{I_N,N}^{-1}g\|_\infty
                           \le C_{\infty,\delta}\|g\|_\infty .
                                                                  \tag{15}
\]
This is independent of the degree, oscillation, and interval
length of the nodal right-hand side.

Apply this to the actual data and retain the exact solution
\[
 g_j=H_N(c_j,Z_*),\qquad
 h=A_{I_N,N}^{-1}g,\qquad
                         \|h\|_\infty\le C_{\infty,\delta}G_N.
                                                                  \tag{16}
\]
As before, zero extension is imposed only on this test
sequence \(h\), never on the original values \(q_{j,N}\).

## 3. Exact modified coefficients at the boundary of the layer

For \(b_N<k\le b_N+3\), define
\[
 \Gamma_{k,N}
    =\sum_{\substack{j\in I_N\\1\le k-j\le3}}
               \mu_{j,N}h_jd_{j,k-j,N}.
                                                                  \tag{17}
\]
Set
\[
 \widehat H_{k,N}=
 \begin{cases}
 H_N(c_k,Z_*)-\Gamma_{k,N}/\mu_{k,N},
                           &b_N<k\le b_N+3,\\
 H_N(c_k,Z_*),             &b_N+3<k\le U .
 \end{cases}
                                                                  \tag{18}
\]
All \(\mu_{k,N}\) in the first line are nonzero. Their angles
approach the fixed positive number \(\delta\), so the ratios
\(\mu_{j,N}/\mu_{k,N}\) in (17)--(18), at distance at most
three, are uniformly bounded. This statement does not divide
by the small weights at the complete-color nodes near zero.

There is a constant \(C'_\delta\), independent of \(N\) and
the parity, such that
\[
                  \max_{b_N<k\le U}|\widehat H_{k,N}|
                                  \le C'_\delta G_N.
                                                                  \tag{19}
\]
Indeed only the first three coefficients change, there are
at most three terms for each, and (16) and the regular
coefficient bounds apply. Thus the modified nodal data keep
the original ceiling \(E_*+\tau\) in (3), without an
additional exponential cost.

The inverse estimate records more than this norm bound.
For each of the three changed nodes there are exact coefficients
\(K_{k\ell,N}\) such that
\[
 \widehat H_{k,N}
   =H_N(c_k,Z_*)-\sum_{\ell=a_N}^{b_N}
                           K_{k\ell,N}H_N(c_\ell,Z_*),
 \qquad
 |K_{k\ell,N}|
                \le C''_\delta
                     e^{-\gamma_\delta(b_N-\ell)} .
                                                                  \tag{20}
\]
The equality substitutes \(h_j=\sum_\ell
(A_{I_N,N}^{-1})_{j\ell}g_\ell\) into (17).
Every such \(j\) lies in \(\{b_N-2,b_N-1,b_N\}\), so
(13) proves the displayed bound after a fixed enlargement
of its constant. For example, interior data with
\(\ell\le b_N-R\) contribute at most
\(C'''_\delta e^{-\gamma_\delta R}G_N\) to each changed
coefficient. This is a controlled response of the actual
insertion; no boundary coefficient has been discarded.

## 4. Paying the far side and the original forcing

The exact finite-source identity of the Dirichlet theorem is
\[
 \sum_{j\in I_N}\mu_{j,N}H_N(c_j,Z_*)q_{j,N}
   =\mathfrak f_N\sum_{j\in I_N}\mu_{j,N}h_j
                        -\mathcal B_{I_N}^{\rm out}(h,q),
                                                                  \tag{21}
\]
where the original forcing is
\(\mathfrak f_N=4\kappa_N^3/N^2\) at even levels and zero
at odd levels. Split its outgoing boundary expression into
left and right:
\[
\begin{split}
 \mathcal B_L&=
    \sum_{\substack{j\in I_N,\ -3\le r\le-1\\j+r<a_N}}
                 \mu_{j,N}h_jd_{j,r,N}q_{j+r,N},\\
 \mathcal B_R&=
    \sum_{k=b_N+1}^{b_N+3}\Gamma_{k,N}q_{k,N}.
\end{split}                                                       \tag{22}
\]
Both signs are those of the original weighted summation by
parts. The right term is precisely the correction in (18).

The full inner kernel, including its complete first edge
and all original normals, satisfies
\[
 |Q_N^{\rm full}(-2\cos u)|
      \le C N^A e^{8N/5}
               \qquad(11\pi/12\le u\le\pi),
                                                                  \tag{23}
\]
by
[far-angle removal, Section 3, equation (25)](research_mixed_next_outer_far_angles_and_verticals.md).
Here the notation on the left means the same outgoing spectral
polynomial whose values are \(q_{j,N}\) in (1).
This is its pointwise whole-source bound, not an inference
from a signed contour estimate.

All nodes \(j<a_N\), and all outside source values occurring
in \(\mathcal B_L\), satisfy (23), by (7).
Use \(|\mu_{j,N}|\le2\), (16), and the regular coefficients
at the far cut. Together with the even forcing bound and
its odd vanishing, this gives
\[
\begin{split}
 \mathcal R_{N,\delta}
  &:=
   \sum_{j<a_N}\mu_{j,N}H_N(c_j,Z_*)q_{j,N}
       +\mathfrak f_N\sum_{j\in I_N}\mu_{j,N}h_j
       -\mathcal B_L,\\
 |\mathcal R_{N,\delta}|
  &\le C_\delta N^{A_\delta}G_N e^{8N/5}.
\end{split}                                                       \tag{24}
\]
This estimate keeps the complete far-node sum; it does not
borrow a normal or derivative bound for a shortened polynomial.
The consumed outer normal has already produced the exact
weights in (1).

Combining the three disjoint node ranges with (21)--(22)
therefore gives the exact identity
\[
 \boxed{\quad
 \mathcal L_N(H_N)
    =\sum_{k=b_N+1}^{U}
             \mu_{k,N}\widehat H_{k,N}q_{k,N}
                       +\mathcal R_{N,\delta}.
 \quad}                                                          \tag{25}
\]
There is no recurrence residual or packet approximation in
this identity.

For the actual insertion choose \(\tau=1/3000\) in (3).
Its far-side ceiling is
\[
 E_*+\frac85+\frac1{3000}
       =\Lambda-\frac1{120}.
                                                                  \tag{26}
\]
Indeed \(B_0+1/50-8/5=13/1500\).
After absorbing the fixed polynomial factors, (24) implies
\[
                  |\mathcal R_{N,\delta}|
                          =O_\delta(e^{N(\Lambda-1/200)}).
                                                                  \tag{27}
\]
The thresholds and constants may depend on \(\delta\), but
the displayed exponential gap is available for every fixed
choice in (4).

## 5. Consequence for the original transfer and remaining scope

The adopted exact transfer reduction is
\[
 \mathcal T_0[F_N](-2,Z_*)
     =I_{{\rm geom},N}
        +\frac{(-q)^M}{\kappa_N^2N}\mathcal L_N(H_N)
        +O(e^{N(\Lambda-\epsilon_*)}),
 \qquad \epsilon_*>0 .
                                                                  \tag{28}
\]
Its original geometric term is
\[
 I_{{\rm geom},N}
      =N^{-2}\mathcal A_0e^{N\mathcal P_*}
                              (1+O(N^{-1})),\qquad
 \mathcal A_0\ne0.
                                                                  \tag{29}
\]
No modification of its two Fourier sectors or original
filter is made here. Since the outside scalar in (28) has
modulus \(1/N\), equations (25),(27) prove
\[
\boxed{\quad
 \mathcal T_0[F_N](-2,Z_*)
    =I_{{\rm geom},N}
       +\frac{(-q)^M}{\kappa_N^2N}
           \sum_{k=b_N+1}^{U}
                    \mu_{k,N}\widehat H_{k,N}q_{k,N}
       +O_\delta(e^{N(\Lambda-\epsilon_\delta)}),
 \quad}                                                          \tag{30}
\]
where one may take
\(\epsilon_\delta=\min\{\epsilon_*,1/200\}>0\).
This is a base-reference statement, with no new derivative
or jet assertion.

Every remaining node in (30) lies in the actual
physical-outgoing packet range \(0<u<\delta<\pi/2\).
The restriction has not turned its relative \(O(N^{-1})\)
error into a negligible error in a canceled sum. The full
values \(q_{k,N}\) remain in (30).

The layer can be chosen arbitrarily small but is fixed
before taking the large-level limit. Its size is still
proportional to \(N\). Neither the inverse constants nor
(19)--(20) are asserted uniform if \(\delta\) tends to zero
with \(N\).

Only three nodal coefficients change. They depend coherently
on the actual interior data through the exact inverse.
No holomorphic continuation or low-degree polynomial bound
for these modified coefficients is asserted. Any use of the
central holomorphic inner packet or of exact reflection must
retain these three corrections and their original signs.

The complete-color action exceeds the desired outer budget.
Accordingly the remaining sum in (30) cannot be discarded
using (19) and absolute values alone. The theorem removes
the other physical colors, with controlled coefficient
response and a proved far-side error, but does not prove
suppression or noncancellation of this final coherent layer.

### Source hashes

- Interior Dirichlet inverse:
  e1b713461bacdf263c07c3baa21de67960fae5e5e2735e5c400c009c987afddf.
- Complete far-angle source:
  5e64e4909b55107431d13fcbff92f41776ff101757c5a9f7eb70ae2d8ea1408d.
- Actual outer insertion and exact transfer:
  cbbc62951666d06e0ae77b29f49f563d91c2024dc8da900ae996144d7db39dab.
- Original seven-term recurrence:
  49cd08c5759bd6669d3cbf1a7e661d60188639c9added0c973659c4723d0a21a.
