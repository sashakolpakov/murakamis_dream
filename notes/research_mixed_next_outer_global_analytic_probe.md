# A global analytic probe for the original outer observation

Private exact-source deduction, 9 November 2026. The constrained
outer adjoint admits an exponentially accurate analytic probe on
the entire real angular period. The proof groups its finite poles
using ordinary polynomial divisibility, then works on even
periodic holomorphic strips. Its exact full Hermite pairing has
no artificial matching boundaries.

For the actual Green insertion this gives a fixed positive
exponential gain below the complete inner action. The gain is
not compared with the outgoing attachment budget. No full
transfer asymptotic or finite-exception theorem is asserted.
No mathematical numerical evaluation or frozen-source edit is used.

## 1. The original grouped operator on a full period

Keep the full algebra and ordered operator of
[the central regularized source](research_mixed_next_outer_central_regularized_operator.md):
\[
\begin{gathered}
N\ge6,\quad \theta=\pi/N,\quad q=e^{i\theta},\quad
D=N-1,\quad M=\lceil N/2\rceil,\quad U=\lfloor N/2\rfloor-1,
\quad \kappa_N=q^{D^2/2},\\
z(u)=-2\cos u,\qquad c_j=2\cos((2j+1)\theta),\qquad
u_{j,N}=\pi-(2j+1)\theta,\\
Q_{3,N}^{\rm rev}(z)=\prod_{\nu=0}^2(z-c_{U-\nu}),\\
\mathcal B_N
 =q^{-2}\mathcal L_2(\mathcal L_3^2-I)
   +q^{-3}Z\mathcal L_3-8q^{-2}\mathcal L_3+(8q^{-1}+2)I .
\end{gathered}                                                     \tag{1}
\]
Here \(Z\) in (1) denotes multiplication by the spectral variable.
The separate outgoing parameter below will always appear as
an argument of an insertion or Green matrix.
In the original full Hermite algebra,
\[
\mathcal B_N=R_N^{-3}\mathcal D_{3,N}^{\mathrm t}R_N^3 .
                                                                    \tag{2}
\]
The transpose is bilinear and retains the original first normals.

Put \(E_N(u)=e_M(z(u))\). For an even \(2\pi\)-periodic analytic
function \(g\), define the grouped expression
\[
(\mathcal C_Ng)(u)
 =\frac{\mathcal B_N\bigl(e_M(z(u))Q_{3,N}^{\rm rev}(z(u))g(u)\bigr)}
              {e_M(z(u))}.
                                                                    \tag{3}
\]
Away from its displayed denominators, the definition uses the
original angular shift operators. Their formulas and exact
radical ratios are
\[
\begin{split}
(\mathcal L_nf)(u)
={}&(c_0+A_N(u)+C_N(u))f(u)\\
 &-q^nA_N(u)e^{-inu}f(u-2\theta)
  -q^nC_N(u)e^{inu}f(u+2\theta),\\
A_N(u)&=\frac{4\cos^4((u-\theta)/2)}
               {\sin u\sin(u-\theta)},\qquad C_N(u)=A_N(-u),
\qquad c_0=2\cos\theta,\\
\frac{E_N(u+2r\theta)}{E_N(u)}
&=(-1)^r
\begin{cases}
1,&N\text{ even},\\
\sin((u+2r\theta)/2)/\sin(u/2),&N\text{ odd}.
\end{cases}
\end{split}                                                       \tag{4}
\]
In particular the high angular frequency in \(E_N\) cancels
exactly before any bound. Expansion of (1),(3),(4) gives
\[
(\mathcal C_Ng)(u)
   =\sum_{r=-3}^3a_{r,p}(u,N^{-1})g(u+2\pi r/N),
                                                                    \tag{5}
\]
where \(p\) records parity. The coefficient order in (1)
is unchanged.
The only index-dependent factor besides (4) is
\[
Q_{3,N}^{\rm rev}(z(u))
 =\prod_{\nu=1}^3 2\{\cos(\lambda_{\nu,p}\theta)-\cos u\},
\qquad
\lambda_{\nu,p}=
\begin{cases}
2\nu-1,&N\text{ even},\\
2\nu,&N\text{ odd}.
\end{cases}
\]
Thus after fixing parity its dependence on \(N^{-1}\) is
analytic, with no varying floor left in the coefficient chart.

All possible poles of these raw coefficients are real modulo
\(2\pi\): they come from the shifted sine denominators in (4),
and from \(\sin(u/2)\) at odd levels. The number of shifts is
fixed. The following argument removes all these poles in the
grouped expression, including those near both \(0\) and \(\pi\).

Write
\[
\mathscr S_s=\{u\in\mathbb C:|\Im u|<s\},\qquad
\|g\|_s=\sup_{\mathscr S_s}|g|,
                                                                    \tag{6}
\]
with real parts taken modulo \(2\pi\). Let
\(\mathscr H_s^{\rm ev}\) be the bounded, even, \(2\pi\)-periodic
holomorphic functions on this strip.

Every \(g\in\mathscr H_t^{\rm ev}\) is uniformly approximated on
each smaller closed strip by its finite cosine sums. These are
ordinary polynomials in \(z(u)\), since
\(T_k(-z(u)/2)=\cos(ku)\).
This follows directly from the exponential Fourier coefficient
bound obtained by moving the coefficient integral to the two
horizontal lines inside \(\mathscr S_t\).

For an ordinary polynomial \(P\), the
[finite Newton theorem, equation (5)](research_mixed_next_outer_finite_newton_remainder.md)
proves
\[
\frac{\mathcal B_N(e_MQ_{3,N}^{\rm rev}P)}{e_M}
                              \in\mathbb C[z].
                                                                    \tag{7}
\]
The divisibility is ordinary, before reduction by the spectral
polynomial. Its endpoint proof includes all double-node first
normals and the odd simple node.

Fix \(0<s<t\) and a physical level \(N\).
Approximate \(g\) uniformly on a closed intermediate strip by
the cosine polynomials just described. All shifts in (5) are
real, so their evaluations on \(|\Im u|=s\) remain on that
same line. The coefficients there have no pole. Thus the
polynomial outputs in (7) converge uniformly on both horizontal
boundary lines. The maximum principle on the annulus obtained
from \(e^{iu}\) makes the outputs converge uniformly on the
entire closed strip \(|\Im u|\le s\). Away from the raw poles,
the limit agrees with (5), so it gives the unique holomorphic
continuation of (3) across every such pole. It is even and
\(2\pi\)-periodic.

This proves global grouped removability at every sufficiently
large physical level and both parities. It does not assert
that any separated coefficient \(a_{r,p}\) is removable,
nor continue the level to an independent complex variable
at those poles.

## 2. A nonvanishing principal multiplier on the real period

On fixed nonreal horizontal lines let \(N^{-1}\to0\) in (5).
The exact computation in the central regularized source gives
the multiplication symbol
\[
\begin{split}
m_0(u)&=(2-2\cos u)^3d(u,-e^{3iu}),\\
d(u,\zeta)&=(\ell^2-1)m-(8+2x)\ell+10,\qquad x=\cos u,\\
\ell(u,\zeta)&=2+2a-a(\zeta+\zeta^{-1}),\\
m(u,\zeta)&=2+2a-a(e^{-iu}\zeta+e^{iu}\zeta^{-1}),
\qquad a=\cot^2(u/2).
\end{split}                                                       \tag{8}
\]
The apparent central singularity is removed by its exact
entire expression. With
\[
\sigma=\sin^2(u/2),\quad
A=\cos^2(u/2)\cos^2(3u/2),\quad
B=\cos^2(u/2)\cos^2u,
\]
that expression is
\[
m_0(u)=64\left[
64A^2B+(32A^2+64AB)\sigma
 +(12B-8\cos u\,A)\sigma^2-4\cos u\,\sigma^3
\right].
                                                                    \tag{9}
\]
It is even, entire, and \(2\pi\)-periodic.

For \(0<u<\pi\), the
[all-character symbol theorem](research_mixed_next_outer_all_character_symbol.md)
gives \(d(u,-e^{3iu})\ge4\). Hence \(m_0(u)>0\) there.
Equation (9) supplies the exact endpoint values
\[
                         m_0(0)=4096,\qquad m_0(\pi)=256.
                                                                    \tag{10}
\]
Evenness and periodicity prove strict positivity on the entire
real period. Compactness therefore gives
\[
                     \mu=\min_{u\in[-\pi,\pi]}m_0(u)>0.
                                                                    \tag{11}
\]
There is a fixed \(R_*>0\) such that
\[
                 |m_0(u)|\ge\mu/2\qquad(|\Im u|\le R_*).
                                                                    \tag{12}
\]
This is a zero-free neighborhood of the complete real circle,
not merely a disk near the complete-color point. No quantitative
claim about a macroscopic strip is made.

## 3. Global small-shift control and a finite analytic inverse

Fix \(0<r<R<R_*\), with \(R-r<1\).
There is a finite constant \(C_{r,R}\), common to both parities,
such that for
\[
r\le s<s+\delta\le R,\qquad 0<\delta\le1,
\]
and all sufficiently large physical \(N\),
\[
\boxed{\quad
\|(\mathcal C_N-m_0)g\|_s
 \le\frac{C_{r,R}}{N\delta}\|g\|_{s+\delta},
                      \qquad g\in\mathscr H_{s+\delta}^{\rm ev}.
\quad}                                                            \tag{13}
\]
To prove this, work first on \(|\Im u|=s\).
The explicit finite coefficient expressions in (4),(5)
are jointly analytic in \(u,\epsilon\) near the compact
set
\[
-\pi\le\Re u\le\pi,\qquad
r\le|\Im u|\le R,\qquad \epsilon=0.
\]
Their denominators do not vanish there. Consequently
\[
|a_{r',p}(u,N^{-1})|\le C,\qquad
|a_{r',p}(u,N^{-1})-a_{r',p}(u,0)|\le C/N
                                                                    \tag{14}
\]
uniformly. The symbol in (8) is their sum at \(\epsilon=0\).
Cauchy's derivative bound on the larger strip, followed along
a real segment of length at most \(6\pi/N\), gives
\[
|g(u+2\pi r'/N)-g(u)|
 \le\frac{12\pi}{N\delta}\|g\|_{s+\delta}
                         \qquad(|r'|\le3).
                                                                    \tag{15}
\]
Real shifts require no loss of strip height merely to be
defined. The width \(\delta\) in (15) pays the derivative.
Summing (14),(15) proves (13) on both boundary lines.
Grouped removability from Section 1 and the annular maximum
principle prove it throughout the strip.

Let \(\Delta=R-r\), and choose a fixed
\[
M_{r,R}\ge\max\{1,2C_{r,R}/\mu\},\qquad
k_N=\left\lfloor\frac{\Delta N}{4M_{r,R}}\right\rfloor,\qquad
t_N=\Delta/k_N.
                                                                    \tag{16}
\]
For sufficiently large \(N\), \(k_N\ge1\) and \(t_N<1\).
Set, in this order,
\[
\mathcal T_N=(\mathcal C_N-m_0)m_0^{-1}.
                                                                    \tag{17}
\]
Multiplication by \(m_0^{-1}\) is applied before the shifts.
On each pair of nested strips with width loss \(t_N\),
(12),(13),(16) give operator norm at most \(1/4\).

For an arbitrary input \(F_N\in\mathscr H_R^{\rm ev}\), define
the finite expressions
\[
g_N=m_0^{-1}\sum_{\ell=0}^{k_N-1}(-\mathcal T_N)^\ell F_N,
\qquad
\rho_N=(-\mathcal T_N)^{k_N}F_N.
                                                                    \tag{18}
\]
Then \(g_N\) is analytic on \(\mathscr S_{r+t_N}\), and exact
finite telescoping gives
\[
\boxed{\quad
\mathcal C_Ng_N=F_N-\rho_N,\qquad
\|g_N\|_r\le\frac8{3\mu}\|F_N\|_R,\qquad
\|\rho_N\|_r\le e^{-cN}\|F_N\|_R,
\quad}                                                            \tag{19}
\]
where one admissible positive constant is
\[
                       c=\frac{\Delta\log4}{8M_{r,R}}.
                                                                    \tag{20}
\]
Indeed \(\mathcal C_Nm_0^{-1}=I+\mathcal T_N\);
the finite geometric identity proves the first formula.
The input norm of successive terms is at most \(4^{-\ell}\),
and the inverse-multiplier bound is \(2/\mu\).
For large \(N\), \(k_N\ge\Delta N/(8M_{r,R})\), which proves
the residual estimate.

The test
\[
                    h_N(u)=Q_{3,N}^{\rm rev}(z(u))g_N(u)
                                                                    \tag{21}
\]
vanishes at all three required central double nodes exactly.
It is a global even periodic analytic function, and therefore
descends to a holomorphic spectral function on an ellipse
containing the entire physical interval. The same holds for
\(F_N\) and \(\rho_N\), with the corresponding smaller strip.
There is no local cutoff or separately chosen matching test.

## 4. The full original transpose identity for analytic tests

For a spectral function holomorphic near \([-2,2]\), define
its class in the original full algebra by Hermite interpolation:
match its value and first derivative at every double node and
its value at the odd simple node. Use the original trace
\(\phi_N\) on that class.

The ordinary full transpose identity extends to the analytic
functions just constructed. To justify this without changing
a finite normal, approximate the even periodic \(g_N\) by
cosine polynomials on a strip strictly larger than
\(\mathscr S_r\) but smaller than \(\mathscr S_{r+t_N}\).
Their spectral polynomials converge, together with every
fixed derivative, on a smaller neighborhood of \([-2,2]\).
For each fixed physical \(N\), the original full pairing is a
finite continuous functional of those Hermite jets.
Their grouped operator outputs also converge by Section 1,
with derivatives on smaller neighborhoods.
The exact polynomial transpose identity can therefore be
passed to the limit. The argument is at each fixed \(N\);
no uniform approximation cost is inserted in any estimate.

The original complete source satisfies
\[
\mathcal D_{3,N}Q_N^{\rm full}=\mathfrak f_N\,1
\quad\hbox{in the full algebra},\qquad
\mathfrak f_N=
\begin{cases}
4\kappa_N^3/N^2,&N\text{ even},\\
0,&N\text{ odd}.
\end{cases}
                                                                    \tag{22}
\]
This is the exact parity forcing in the
[physical seven-term source theorem](research_mixed_next_physical_inner_seven_term_recurrence.md),
including its complete-end defect.

Define
\[
\mathcal L_N(F)
 =\phi_N[R_N^3e_MQ_N^{\rm full}F],\qquad
\ell_N(h)=\phi_N[R_N^3e_Mh].
                                                                    \tag{23}
\]
Restore (2),(3) in (19) and use the analytic transpose identity.
Explicitly, the chain is
\[
\begin{split}
\phi_N[R_N^3Q_N^{\rm full}e_M(F_N-\rho_N)]
 &=\phi_N[R_N^3Q_N^{\rm full}\mathcal B_N(e_Mh_N)]\\
 &=\phi_N[Q_N^{\rm full}
                    \mathcal D_{3,N}^{\rm t}(R_N^3e_Mh_N)]\\
 &=\phi_N[(\mathcal D_{3,N}Q_N^{\rm full})R_N^3e_Mh_N].
\end{split}
\]
It yields exactly
\[
\boxed{\qquad
\mathcal L_N(F_N)
 =\mathfrak f_N\,\ell_N(h_N)+\mathcal L_N(\rho_N).
\qquad}                                                           \tag{24}
\]
All normal coefficients are those of the original full algebra.
In particular the three zeros in (21) are conditions on the
test, as required by the endpoint theorem. They are not
assumed for \(F_N\). At odd levels the simple-node conditions
are included in the same polynomial approximation argument.

Because both terms in (24) contain the outer radical, the
original consumed-normal formula gives
\[
\begin{split}
\ell_N(h_N)&=\sum_{j=0}^{U}\mu_{j,N}h_N(u_{j,N}),\\
\mathcal L_N(\rho_N)&=\sum_{j=0}^{U}
       \mu_{j,N}Q_N^{\rm full}(c_j)\rho_N(u_{j,N}),
\qquad |\mu_{j,N}|\le2 .
\end{split}                                                       \tag{25}
\]
The unit crossing phases in \(\mu_{j,N}\) have not been replaced
by positive weights in the identity. At this stage they may
be bounded in estimating the residual.
On the real interval, \(|Q_{3,N}^{\rm rev}|\le4^3\).
Equations (19),(21),(22),(25) consequently imply
\[
|\mathfrak f_N\ell_N(h_N)|
 \le C N^{-1}\|F_N\|_R
                    \quad(N\text{ even}),
\qquad
\mathfrak f_N\ell_N(h_N)=0
                    \quad(N\text{ odd}).
                                                                    \tag{26}
\]
There is no artificial boundary current in (24). The entire
physical period and its original endpoint conditions were
used before the estimate.

The adopted complete physical-source upper bound is
\[
\max_{0\le j\le U}|Q_N^{\rm full}(c_j)|
 \le C_\tau N^{A_\tau}e^{N(\mathfrak M_3+\tau)}
                         \qquad(\tau>0).
                                                                    \tag{27}
\]
It combines the original nonzero physical packet and the
complementary physical upper bound, as recorded in the
[full-tail theorem, equation (28a)](research_mixed_next_outgoing_full_tail_weighted_energy.md).
It does not substitute a relative approximation inside (24).
Combining (19),(24)--(27) proves, for every \(\tau>0\),
\[
\boxed{\quad
|\mathcal L_N(F_N)|
 \le C_\tau N^{A_\tau}\|F_N\|_R
                \left\{N^{-1}+e^{N(\mathfrak M_3+\tau-c)}\right\}.
\quad}                                                            \tag{28}
\]
The estimate uses the exact recurrence, its forcing and full
transpose, not termwise integration of an algebraic packet error.

## 5. Application to the original lower-boundary Green observation

Let \(\nu_N(\xi,Z)\) be the exact insertion of the
[Green localization theorem](research_mixed_next_outgoing_finite_green_localization.md).
Keep its original region
\(\mathfrak Z=\{\rho e^{-i\alpha}:4/5\le\rho\le8/7,\
3\pi/5\le\alpha\le39\pi/50\}\).
For \(Z\in\mathfrak Z\), that theorem proves
\[
\sup_{\xi\in\mathcal E_{\gamma_0}}|\nu_N(\xi,Z)|\le CN^6,
\qquad
\gamma_0=\log(126/125),\qquad
\mathcal E_{\gamma_0}:
 \xi=2\cos(\vartheta+i\gamma_0).
                                                                    \tag{29}
\]
Choose once
\[
                       0<r<R<\min\{R_*,\gamma_0\}.
\]
Then \(F_N(u)=\nu_N(-2\cos u,Z)\) is an eligible even periodic
input with \(\|F_N\|_R\le CN^6\). The exact original observation
is \(v_M(Z)=\mathcal L_N(F_N)\). Choose, for example,
\(\tau=c/4\) in (28) and absorb polynomial factors using a
strict part of the remaining reserve. There is a fixed
\(\delta>0\), independent of \(Z\) and parity, such that
\[
\boxed{\qquad
|v_M(Z)|\le C e^{N(\mathfrak M_3-\delta)}
                           \qquad(Z\in\mathfrak Z)
\qquad}                                                           \tag{30}
\]
for all sufficiently large \(N\).
One may take \(\delta=\min\{c/4,1/4\}\) after increasing
the common level threshold; the polynomial forcing in (28)
then also lies below this rate since \(\mathfrak M_3>9/5\).

This is a genuine fixed positive gain for the signed original
Green observation. It is consistent with the positive-metric
obstruction: that obstruction bounds the cost of taking absolute
values before exploiting the recurrence, whereas (24) retains
the exact bilinear transpose and parity forcing.

The remaining transfer correction is still
\[
\frac{qA_Ma_{M-1}(Z_*)}{\kappa_N^2N}\,v_M(Z_*).
                                                                    \tag{31}
\]
No adequate rate for its product is inferred from (30).
In particular neither the strip width \(R\) nor the constant
\(c\) in (20) has been compared with
\(\mathfrak M_3+\operatorname{rate}(a_{M-1})-\Lambda\).
The original cutoff forcing and the full-tail reduction errors
retain their already proved separate bounds.
The nonzero geometric term and the larger short-filling
stability problem remain unchanged.

## Source versions

- Grouped central operator, exact radical ratios and multiplier:
  244a089f0046f1a8b81f55941c17c32304eb3fd679aa933361ebacbfa416f9a8.
- Ordinary divisibility and conjugated full transpose:
  c5cb10096ed4c6aafefdc957958ddaf392ad17c81cab5e7e99dbbe026fc1aed3.
- Original endpoint classification:
  9cde443d65bfdc41104ffe9e78ce4e4540ec998b53681923f99fd42a5d436d71.
- All-character positivity:
  c88ba98093fc147f5acfcf1790aa5b6f0f26edda6d741d2efc7c55315942e55e.
- Exact complete-source recurrence:
  49cd08c5759bd6669d3cbf1a7e661d60188639c9added0c973659c4723d0a21a.
- Full-tail finite source and physical upper bound:
  0037a31d5f2a8cedea53d70bf1f0434f906668fe0934e5ee303890a8b3eceee7.
- Actual Green insertion and its fixed spectral ellipse:
  b0cc349962797f5ef5afb3d4aec87fd2caf5a3740bb0041a0c6a8ae4d48e4492.

