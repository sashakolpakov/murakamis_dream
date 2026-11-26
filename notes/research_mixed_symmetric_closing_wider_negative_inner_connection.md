# The complete negative inner connection on the right hyperbola

Private finite-source deduction, 9 November 2026. At fixed first
depth \(7/10\), the negative central phase decreases away from
the imaginary axis. The entire negative horizontal and its far
vertical connection consequently lie below the actual closing
budget. All kernels, cutoffs and trace multipliers are the
original ones.

No mathematical numerical evaluation, saved-value arithmetic,
import, compilation or frozen-source edit is used.

## 1. Source and assertion

Retain \(U=\lfloor N/2\rfloor-1\), the original Newton polynomials
and the notation
\[
 \begin{gathered}
 \mathcal K_N^<(w,x)=\sum_{j=0}^{U}e_j(w)e_j(x),\qquad
 K_N^<(t,u)=\mathcal K_N^<(-2\cos t,-2\cos u),\\
 W_N(t)=\frac{e^{-iNt}}{(1-(-1)^{N-1}e^{-iNt})^2},
 \qquad C_{N,3}=e^{3\pi i(N-1)^2/(4N)}.
 \end{gathered}
 \tag{1}
\]
Let \(u_g=\beta_g-iK_g\) be the original closing point and set
\[
 \begin{gathered}
 M_g=\Re\{2S_3(0,u_g)+iu_g^2/\pi-iu_g\}>321/100,\\
 u=\beta-iK,\quad \pi/2\le\beta\le2\pi/3,\quad
 K=\frac{\pi K_g}{2\beta},\qquad h_0=7/10,\\
 \mathcal B(u)=\frac{M_g-(2\beta/\pi-1)K}{2}.
 \end{gathered}
 \tag{2}
\]
The original localization gives \(17/30<K_g<7/10\), so that
\(17/40<K\le K_g<7/10\).

Use the exact midpoint cut and fixed endpoint height of the
[fixed-low remainder theorem](research_mixed_symmetric_closing_fixed_low_remainder.md):
\[
 \Theta_N=\pi-\frac{2\pi\lfloor N/4000\rfloor}{N},\qquad
 e^{iN\Theta_N}=-(-1)^{N-1},\qquad
 \pi-\pi/2000\le\Theta_N\le\pi-\pi/4000 .
 \tag{3}
\]
Let \(h_c>0\) be its fixed sufficiently small height. The
oriented path considered here is
\[
 \gamma_-:\quad
 -\Theta_N-ih_c\longrightarrow-\Theta_N-ih_0
                           \longrightarrow-ih_0 .
 \tag{4}
\]
Its final horizontal includes the whole negative central
interval \([-\pi/2,0]-ih_0\).

**Theorem.** Uniformly on (2), at both parities and all
sufficiently large levels,
\[
 \sup_{w\in[-2,2]}\frac{N^2}{\pi}\int_{\gamma_-}
 \left|\sin t\,\mathcal K_N^<(w,-2\cos t)K_N^<(t,u)
                e^{3iNt^2/(4\pi)}W_N(t)\right|\,|dt|
       \le C e^{N(\mathcal B(u)-1/50)}.
 \tag{5}
\]
This bounds the original signed current with scalar
\(-N^2C_{N,3}/(\pi i)\) as well. On a sufficiently small
fixed complex neighborhood of \([-2,2]\), the same assertion
holds with gap \(1/100\); all fixed ordinary incoming
derivatives have that bound on smaller neighborhoods.

This is a bound on the specified two-short current.
It does not substitute that current for the full trace or
delete any of the separate finite trace corrections.

## 2. A monotone negative central phase

On \(t=-a-ih_0\), \(0\le a\le\pi/2\), the
[signed wider-source theorem](research_mixed_symmetric_closing_wider_signed_central_source.md)
gives the complete second-edge envelope
\[
 |K_N^<(t,u)|\le C_\tau
  e^{N(\max\{\Re\psi(t,u),(h_0+K)/2\}+\tau)}.
 \tag{6}
\]
Its proof uses the exact swap with the opposite-height source.
No complex conjugation of the cubic crossing occurs.
All physical endpoint rows, the two complete aliases, and
all original caps are retained.

The calibrated principal returns satisfy
\[
 r_0(t)=\operatorname{arsinh}\tan(t/2),\qquad
 r_1(t,u)=\operatorname{arsinh}\{\cos(u/2)\tan(t/2)\},
\]
\[
 \Phi_t(t,u)=-\frac{r_0(t)+r_1(t,u)}{\pi}
                                      +\frac{3it}{2\pi}-i .
 \tag{7}
\]
Their original branches on this entire signed box are those
verified in the signed source. In particular
\[
 |\tan((-a-ih_0)/2)|^2
   =\frac{\cosh h_0-\cos a}{\cosh h_0+\cos a}\le1,\qquad
 |\cos(u/2)|^2=\frac{\cosh K+\cos\beta}{2}<13/20 .
 \tag{8}
\]
Write \(r_1=X+iY\). The elementary identity
\[
 |\sinh(X+iY)|^2=\sinh^2X+\sin^2Y
 \tag{9}
\]
implies \(|X|\le\operatorname{arsinh}|\sinh r_1|
<\operatorname{arsinh}1<1\); the last inequality follows
from \(\sinh1>1\). Also \(\Re r_0\le0\), since its argument
has nonpositive real part and the original principal branch
preserves that sign. Consequently
\[
 \frac d{da}\Re\Phi(-a-ih_0,u)
       =\frac{\Re r_0+\Re r_1-3h_0/2}{\pi}
                          <-\frac1{20\pi}.
 \tag{10}
\]
Thus the entire geometric rate on this negative interval is
at most its axis value \(\Re\Phi(-ih_0,u)\).

Its endpoint rate also decreases with \(a\). Indeed evenness
and real coefficients give
\[
 E_-(a,u)=\Re\psi(a-ih_0,0)+(h_0+K)/2
                              -3ah_0/(2\pi)-h_0 .
 \tag{11}
\]
The first term has nonpositive \(a\)-derivative, because
\(\Re\operatorname{arsinh}\tan((a-ih_0)/2)\ge0\).
Hence \(E_-(a,u)\le E_-(0,u)\).

The
[center height-join theorem](research_mixed_symmetric_closing_center_height_join.md),
equations (23)--(25), proves the following pointwise
two-sector comparison, in particular at \(h=h_0\):
\[
 \max\{\Re\Phi(-ih_0,u),\ E_-(0,u)\}
                    <\mathcal B(u)-179/8000 .
 \tag{12}
\]
That theorem proves it on the entire independent outgoing
rectangle containing (2). Its proof keeps the original
primitive constant and exact outer half-weight.
Equations (10)--(12) transfer this margin to the whole
negative central interval.

For every real incoming \(w\), the first-short slit theorem
on this compact first-angle set gives
\[
 |\mathcal K_N^<(w,-2\cos t)|
       \le C_\tau e^{N(\Re\psi(t,0)+\tau)}.
 \tag{13}
\]
Together with (6) and
\[
 |W_N(-a-ih_0)|\le
 e^{-Nh_0}(1-e^{-Nh_0})^{-2},\qquad
 |e^{3iN(-a-ih_0)^2/(4\pi)}|
                      =e^{-3Nah_0/(2\pi)},
 \tag{14}
\]
this proves (5) on the negative central interval. For
example take \(\tau=1/2000\) in both edge bounds and absorb
all fixed lengths and polynomial costs into \(1/1000\).
The remaining reserve after gap \(1/50\) is \(3/8000>0\).

## 3. The far negative horizontal and vertical

The same slit theorem, its whole-real-period conclusion and
degree-\(U\) continuation give the literal finite bound
\[
 \left|\mathcal K_N^<(w,-2\cos(-a-ih))
                          K_N^<(-a-ih,u)\right|
 \le C_\tau N^A
 e^{N(2\Re\psi(a-ih,0)+K/2+2\tau)}
 \tag{15}
\]
for \(w\in[-2,2]\), \(\pi/2\le a\le\pi-\pi/4000\) and
\(0\le h\le h_0\). The first spectral image is a fixed
compact subset of the original slit plane. The \(K/2\)
cost follows from the exact degree \(U<N/2\) in the
outgoing ordinary variable, for every real outgoing angle.
This is the sign-independent source argument in Section 3
of the fixed-low theorem, not its former relative comparison
with a smaller-domain action.

At \(h=h_0\), the source rate after crossing and sampling is
\[
 L(a,u)=2\Re\psi(a-ih_0,0)+K/2-h_0-3ah_0/(2\pi).
 \tag{16}
\]
It decreases with \(a\). The original first-edge height bound
and real-angle monotonicity give
\[
 \Re\psi(a-ih_0,0)\le\psi(-ih_0,0)
                      \le2b_2+h_0^2/(4\pi),\qquad b_2<7/12 .
 \tag{17}
\]
Add the outer half-weight and use \(\beta K/\pi=K_g/2\).
At \(a=\pi/2\), equations (16)--(17) yield
\[
 \begin{split}
 L(a,u)+(\beta/\pi-1/2)K
 &<\frac73+\frac{49}{200\pi}
                +\frac7{20}-\frac7{10}-\frac{21}{40}\\
 &=\frac73+\frac{49}{200\pi}-\frac78
 <\frac{77}{50}.
 \end{split}
 \tag{18}
\]
The final bound uses \(\pi>3\).
Since \(M_g/2>321/200\), its reserve is \(13/200\).
Thus the whole horizontal
\([-\Theta_N,-\pi/2]-ih_0\) has more than the gap in (5),
after the same tolerances and polynomial absorption.

On the far vertical, the exact midpoint identity (3) gives
\[
 |W_N(-\Theta_N-ih)|
       =\frac{e^{-Nh}}{(1+e^{-Nh})^2}\le e^{-Nh}.
 \tag{19}
\]
The rate
\[
 2\Re\psi(\Theta_N-ih,0)+K/2-h-3\Theta_Nh/(2\pi)
 \tag{20}
\]
strictly decreases in \(h\), because the original return has
\(\partial_h\Re\psi(a-ih,0)<1/2\).
Its value at zero, after adding the half-weight, is
\[
 2\psi(\Theta_N,0)+K_g/2<1/100+7/20=9/25 .
 \tag{21}
\]
Here \(\psi(\Theta_N,0)<1/200\) is the original exact
real-endpoint estimate in the left-connection proof,
reproduced in equation (27) of the fixed-low theorem.
This estimate retains the original complete constant.
The same tolerances and bounded lengths therefore pay the
whole vertical in (4). This finishes the all-real assertion (5).

The incoming degree of the exact integrand is at most \(U\).
Its pointwise all-real bound, established before integrating,
continues to a fixed sufficiently small filled Bernstein
ellipse with an arbitrarily small fixed exponential cost.
Choose this cost, including polynomial absorption, below
\(1/100\). This proves the ordinary-neighborhood version
and, by Cauchy's formula on smaller neighborhoods, all fixed
incoming derivatives.

The path ends at \(-ih_0\). If the positive selected path
starts deeper, the separately proved center height join
supplies that vertical. The positive saddle path, its right
vertical, low/far currents and full traced edge restorations
remain separately identified source pieces. No estimate
for one is inferred merely from the bound (5).

## Frozen source bindings

- Original signed wider edge and calibrated returns:
  dea764c87b923f51be906688369da2fed794d376cb11469522f98983559d63c8.
- Actual axis pointwise budget and incoming normalization:
  943a40bd6addadc889b6a4b2629619d4ea6bb780fc5f9e6b25e67431a7ffa65a.
- Complete all-real first-short bound and degree continuation:
  efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b.
- Exact midpoint contour, original far source and calibrated endpoint:
  03accd56435b7c00be36b89a5e2ffcee70ae84027ad918a6b3b1dca204825ab0.
- Original negative connection and full midpoint vertical:
  0981672faffc8d4cb94848a59ce01eeeb9627110e05fed16a2664ba8c27f930f.
