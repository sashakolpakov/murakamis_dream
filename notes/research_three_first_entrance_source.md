# The next original source after the prepared cap

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

This proves the first of the additional attachments needed to reach
the small-gradient source class. The incoming function is the original
prepared source. Its wider real-output expansion controls the real
annulus, and its packet on a complex disk controls a contour consisting
of two straight segments through the critical point. No source
asymptotic is inferred solely from continuation of its phase.

## 1. Original finite functions and statement

Use the original matrices and boundary vectors, and put
\[
 A_N=JM^3,\quad \widetilde A_N=A_N-E_{\lfloor N/40\rfloor},
 \quad x_h=\frac16+\frac{i\log2}{2\pi},\quad R=\frac1{200},
 \quad k_0=\frac{4\pi}{21}(2\sqrt3-3i).
 \tag{1}
\]
The incoming source and the retained kernel are
\[
 F_{1,N}(x,w)=v(w)^TA_N^2h(x),\qquad
 K_N(x,y)=h(x)^T\widetilde A_Nh(y).
\]
The complete ordinary color is \(w=-2\). Define the next exact
source by the full horizontal period
\[
 F_{2,N}(y,w)=N\int_{x_h-1/2}^{x_h+1/2}
                     F_{1,N}(x,w)K_N(x,y)\,dx
             =v(w)^TA_N^2\widetilde A_Nh(y).
 \tag{2}
\]
The equality is the original bilinear cardinal identity, at both
parities. Write \(S_1\) for the proved incoming phase and define
\[
 z_c(y,w)=\operatorname{crit}_x\{S_1(x,w)+\Phi(x,y)\},
 \qquad S_2(y,w)=S_1(z_c,w)+\Phi(z_c,y).
 \tag{3}
\]
Here \(\Phi\) is the original retained kernel phase, with all
its constants and logarithmic lifts kept.

**Theorem 1.** On a neighborhood of
\(\{|y-x_h|\le R\}\times\{-2\}\),
\[
 F_{2,N}(y,w)=C_{N,3}\kappa^2N^{-1}\mathcal A_2(y,w)
             e^{NS_2(y,w)}(1+O(N^{-1})),\qquad
                     \mathcal A_2(y,w)\ne0.
 \tag{4}
\]
The normalized remainder is holomorphic and uniform, including
every fixed ordinary outside-color derivative on a smaller
neighborhood. Both level parities are included. The same asymptotic
holds for the undeleted original source \(v(w)^TA_N^3h(y)\).

The phase satisfies
\[
 S_2'(x_h+z)/k_0=-\sqrt{21}z+h_2(z),\qquad
 |h_2(0)|<.0065,\quad \sup_{|z|\le R}|h_2'(z)|<.18.
 \tag{5}
\]
These bounds are not yet the entrance condition \(H\le.0004\)
in the earlier source-induction theorem.

## 2. Quantitative incoming information

The [wider real-output theorem](research_three_prepared_cap_real_extension.md)
gives, for real \(|t|\le.02\),
\[
 |F_{1,N}(x_h+t,-2)|\le CN^b
 \left[e^{N(M_1+P|t|-A_1t^2)}+e^{N\delta}\right],
 \quad M_1=\Re S_1(x_h)>1.9113,
 \quad P=.0113,\ A_1=4.65,\ \delta=1.9107.
 \tag{6}
\]
More precisely its first term is the actual analytic principal term
with phase \(S_1(x_h+t)\). On the complementary real arc,
\[
 |F_{1,N}(x_h+t,-2)|\le CN^b e^{1.91115N},
             \operatorname{dist}(t,\mathbb Z)\ge.02.
 \tag{7}
\]
The [critical-branch theorem](research_three_entrance_critical_branches.md)
proves
\[
 H_1:=\frac{69}{2500}=.0276>|S_1'(x_h)/k_0|,
 \qquad -\Re S_1''(x_h+t)>9.3\quad(|t|\le.02).
 \tag{8}
\]
The actual incoming packet on the closed complex disk is supplied
by the quantified source theorem.

Retain the constants from the analytic phase and source-induction
proofs:
\[
 D=5+\sqrt{21},\quad
 \rho=(5-\sqrt{21})/2,\quad
 Z=\frac{(21/20)\rho}{1-(3/10)\rho},\quad
 C_0=\frac{|k_0|(D+3/5)}{2(D-3/5)^2}.
 \tag{9}
\]
For \(M_2=\Re S_2(x_h,-2)\), they give
\[
 |M_2-M_1-2c|\le C_0H_1^2,\qquad
 |h_2(0)|\le ZH_1<.0065,\qquad |h_2'|<.18.
 \tag{10}
\]
In particular, for \(|u|\le R\),
\[
 \Re S_2(x_h+u)\ge M_1+2c-C_0H_1^2-|k_0|ZH_1R
 -\frac12\Re(k_0\sqrt{21}\,u^2)-\frac9{100}|k_0|R^2.
 \tag{11}
\]
Let
\[
 \Lambda_{13}=\frac{13+
 \sqrt{(\Re(k_0\sqrt{21})-13)^2+\Im(k_0\sqrt{21})^2}}2,
 \qquad
 B_*=C_0H_1^2+|k_0|ZH_1R+\frac9{100}|k_0|R^2
                              +\Lambda_{13}R^2.
 \tag{12}
\]
The last term is the exact quadratic maximum when the retained
height cost \(13(\Im u)^2\) is compared with (11). The checker
proves all of the following strict budgets:
\[
 \begin{split}
 (A_1+3/2)(.01)^2-P(.01)-B_*&>10^{-6},\\
 1.9113-\delta-B_*&>9\cdot10^{-5},\\
 1.9113-1.91115+(3/2)(.02)^2-B_*&>2\cdot10^{-4}.
 \end{split}
 \tag{13}
\]
The real slope \(P\) and complex gradient bound \(H_1\) have
different roles here. Replacing the former by \(|k_0|H_1\)
would lose the first inequality.

## 3. The real annulus and the rest of the period

First consider \(R\le|t|\le.01\). The actual retained kernel
packet is valid throughout this real input interval and the whole
complex output disk. Put
\[
 T(t,u)=S_1(x_h+t)+\Phi(x_h+t,x_h+u).
\]
At the two real cuts \(t=\pm R\), the correlated critical-point
certificate in Section 2 of the critical-branch theorem gives
\[
                  \Re T(\pm R,u)<\Re S_2(x_h+u)-\frac1{2\cdot10^6}.
 \tag{14}
\]
This conclusion keeps the correlation between the critical point
and the output; a disk bound on its displacement alone was insufficient.

The phase decreases as either real cut moves outward. To see this,
use \(\Phi_x/k_0=-5t+2u+R_x\) at \(|t|=R\), with
\(|R_x|\le(1/10)(|t|+|u|)\), and use (8). The lower bound
\[
 9.3R-P+5(\Re k_0)R-2|k_0|R-\frac15|k_0|R>0
 \tag{15}
\]
proves \(\Re T_t(-R,u)>0\) and \(\Re T_t(R,u)<0\).
On the entire larger real interval the exact cubic phase estimate
gives
\[
 -\Re T_{tt}>9.3+5\Re k_0-18|k_0|(.01+R)>18.
 \tag{16}
\]
Thus (14) holds throughout both annuli. Their principal terms have
a strict gap. For the absolute error in (6), apply the global joint
kernel bound and the second inequality in (13); that error has a
strict gap as well.

For \(.01\le|t|\le.02\), use (6) directly with
[the larger-cap joint bound](research_three_vertex_large_cap_height_bound.md).
The principal upper exponent is
\[
 M_1+2c+P|t|-(A_1+3/2)t^2+13(\Im u)^2.
\]
The quadratic loss increases with \(|t|\) on this interval.
The first inequality in (13) therefore bounds its difference from
the actual output phase by a strictly negative constant. The absolute
error in (6) is again covered by the second inequality in (13).

Finally, if the circular input distance is at least \(.02\),
use (7). The larger-cap kernel loss is at least
\((3/2)(.02)^2\), even past its clipping point at \(.04\).
The last inequality in (13) proves the required gap on this entire
complementary arc. These cases exhaust the original real period.

## 4. The central contour and the nonzero coefficient

Only the central segment \([-R,R]\) remains. The actual incoming
and retained packets are both uniform on its closed complex disk.
For each output, replace this segment by the two straight segments
from \(x_h-R\) to \(z_c\), and from \(z_c\) to \(x_h+R\).
They lie in that same disk by convexity. The finite sources are
holomorphic, so the replacement is exact and has the same endpoints.

Write \(d_\pm=\pm R-(z_c-x_h)\). The certified endpoint sectors
and the uniform Hessian defect give, throughout each segment,
\[
 \Re\{-[S_1''+\Phi_{xx}]d_\pm^2\}>10^{-6}.
 \tag{17}
\]
Integration twice from the critical point gives strict decrease
along each ray. The two rays occupy opposite Gaussian convergence
sectors: their real displacements have opposite signs, and the
positive quadratic sectors cannot cross the imaginary axis.
A small rounding near the critical point therefore gives the full
oriented Gaussian coefficient, not a pair of unrelated half-contributions.

If \(a_K\) is the original retained amplitude, that coefficient is
\[
 \mathcal A_2(y,w)=
 \frac{\sqrt{2\pi}\,\mathcal A(z_c,w)a_K(z_c,y)}
      {\sqrt{-[S_1''(z_c,w)+\Phi_{xx}(z_c,y)]}}.
 \tag{18}
\]
The square root has positive real part because the denominator
inside it has real part greater than 18. Every numerator factor
is nonzero. The exact measure \(N\,dx\), incoming \(N^{-1}\),
kernel \(N^{-1/2}\), and wire Gaussian \(N^{-1/2}\) give
\(N^{-1}\), with the carriers shown in (4). Uniform holomorphic
stationary phase gives the normalized \(O(N^{-1})\) error.
All omitted real regions have the strict gaps just proved, so they
cannot cancel this coefficient.

All inequalities are strict on compact parameter sets. They persist
on an open neighborhood of the output disk and for sufficiently
small ordinary outside-color deformations. Cauchy estimates retain
every fixed ordinary derivative. The angular dependence descends
to ordinary color at \(-2\) by its original evenness.

For the undeleted source, the Fourier corner-transfer theorem with
three vertices bounds the difference by the rate
\[
 1.715+2c+\pi R<2.38,
\]
while (11) gives \(\Re S_2>2.55\) throughout the output disk.
Restoring the original word consequently preserves (4). This proves
Theorem 1. \(\square\)

## 5. A global real bound for the new source

The preceding theorem also leaves an explicit upper bound useful
for later attachments. Set
\[
 v_{03}(t)=\min\{\operatorname{dist}(t,\mathbb Z),.03\},
 \qquad B_2=C_0H_1^2+\frac{P^2}{4(29/20+3/2)}<.000143.
\]
The stronger real envelope for \(F_1\) has linear coefficient
\(P\) and quadratic coefficient \(29/20\), with radius \(.01\).
Combining it with
[the two-wire real kernel bound](research_three_vertex_two_wire_large_cap_bound.md),
and completing the input square, gives on the full real period
\[
 |F_{2,N}(x_h+t,-2)|\le CN^b
       e^{N[M_2+B_2-(3/2)v_{03}(t)^2]}.
 \tag{19}
\]
In this comparison the kernel's input cap is larger than the source's,
so replacing it by the smaller distance only weakens the upper bound.
Equation (10) accounts for the actual center-action change. The same
bound holds for the undeleted source after the negligible corner
error is restored. The positive constant \(B_2\) is retained; it
has not been discarded to claim an invariant Gaussian envelope.

## 6. Reproduction

`experiments/check_three_first_entrance_source.py` verifies the
strict budgets (13), (15)--(16), the action and corner comparisons,
and the constants in (5), (19). The incoming contour and the true-circle
critical-point certificates have separate proofs and replays cited above.
The checks in this note do not assert the remaining entrance steps.
