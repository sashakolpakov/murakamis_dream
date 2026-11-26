# The intermediate input interval for the larger three-crossing source class

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

This bounds an actual complementary part of the Fourier attachment. It
keeps the original retained kernel phase and compares it with the actual
outgoing critical action. The central contour, the more distant input
periods, and the complete induction are separate statements.

## 1. Exact source and scope

Write
\[
 R=1/200,\quad W=9/1000,\quad H_* =57/10000,\quad
 b=9/50,\quad e=13/50,\quad A=29/20,
 \quad s=\sqrt{21},\quad D=5+s,\quad \rho=(5-s)/2,
 \tag{1}
\]
and retain \(x_h,k_0\) from
[the original local composition](research_three_vertex_local_composition.md).
Put \(K=|k_0|=4\pi/\sqrt{21}\) and \(\alpha=\Re k_0\).
Let \(F_N\) be an incoming finite source with a nonzero holomorphic
packet on a neighborhood of
\(x_h+(\{|z|\le R\}\cup[-W,W])\), with phase \(S\) satisfying
\[
 S'(x_h+z)/k_0=-s z+h(z),\qquad
 |h(0)|\le H\le H_*,\qquad |h'|\le b.
 \tag{2}
\]
Suppose its actual real-period upper bound is
\[
 |F_N(x_h+t)|\le CN^q
 \exp N\{M+KHv(t)-Av(t)^2\},\qquad
 M=\Re S(x_h),\quad v(t)=\min\{d_{\mathbb T}(t,0),.03\}.
 \tag{3}
\]
The kernel is exactly
\(K_N(x,y)=h(x)^T\widetilde A_N^{(40)}h(y)\).
The proved [union-domain source theorem](research_three_vertex_real_input_union.md)
gives its original packet, with phase \(\Phi\), for real input
\(|t|\le.02\) and output in the union in (2). Thus no increasing-order
interpolation or approximation of the incoming source is used below.
Define
\[
 S_+(x_h+w)=\operatorname{crit}_z
       \{S(x_h+z)+\Phi(x_h+z,x_h+w)\}.
 \tag{4}
\]
The [larger analytic phase theorem](research_three_larger_phase_class.md)
supplies this original critical branch.

**Theorem 1.** Uniformly for \(|w|\le R\) and for real
\(|w|\le W\), the literal intermediate part of the original integral
satisfies
\[
 \left|N\int_{W\le |t|\le .02}
 F_N(x_h+t)K_N(x_h+t,x_h+w)\,dt\right|
 \le C'N^{q'}\exp N\{\Re S_+(x_h+w)-10^{-5}\}.
 \tag{5}
\]
In fact the same bound holds for the integral of the absolute value.
All constants may depend on the fixed source. Strict margins permit
smaller fixed parameter neighborhoods whenever the input hypotheses
are supplied there uniformly; Cauchy estimates then give fixed parameter
derivatives. This does not assume a bound for an unproved complex input
annulus.

## 2. A full-box original curvature bound

The following estimate concerns the selected original analytic phase:
\[
 -\Re\Phi_{xx}(x_h+t,x_h+u+iv)>47/5
 \quad\bigl(|t|\le.02,\ |u|\le.009,\ |v|\le.005\bigr).
 \tag{6}
\]
The auxiliary output rectangle here is larger than the output source
domain. It is used only for a phase derivative. Its selected branch
was established in Section 2 of the union-domain theorem.

For completeness the exact expression checked in (6) is as follows.
With \(X=e^{2\pi ix},Y=e^{2\pi iy}\), set
\[
 a=X^{-1}-1,\quad b_1=Y^{-1}-1,\quad
 \Delta=1-2(a+b_1)+(a-b_1)^2,\quad
 U=\frac{1+a-b_1-\sqrt\Delta}{2},\quad
 U_x=-\frac{2\pi i(1-U)}{X\sqrt\Delta}.
 \tag{7}
\]
The root has its continued homogeneous branch, with
\(\Im\Delta>0\) throughout the rectangle. Differentiation of the
original envelope formula gives
\[
 \Phi_{xx}=-\frac{U_x}{U(1-XU)}
       +\frac{2\pi iX(1-U)}{(1-X)(1-XU)}.
 \tag{8}
\]
The outward checker covers the entire rational three-dimensional
rectangle in (6). On each box it encloses (8) at the center plus
its exact holomorphic first-derivative mean-value enclosure. The
real directions are \(\Phi_{xxx},\Phi_{xxy},i\Phi_{xxy}\).
The derivative expressions are obtained by exact forward algebra,
including the selected square root. A separate reconstruction of
the complete binary partition checks the cover, not merely its volume.
Every accepted enclosure proves (6) and separates the selected root
from its branch cut. No value sampling is an acceptance criterion.

## 3. Real output: comparison at a correlated reference point

For real \(|w|\le W\), use the reference input
\(z_0=\rho w\). In the incoming disk the original kernel gradient is
\[
 \Phi_x(x_h+z,x_h+w)/k_0=-5z+2w+R_x(z,w),\qquad
 |R_x(z,w)|\le9(|z|+|w|)^2.
 \tag{9}
\]
This is the proved analytic remainder of
[the input-rectangle theorem](research_three_vertex_input_rectangle.md),
Section 5, applied by symmetry; here one displacement is at most
\(R\) and the other at most \(W<.01\).
Since \(D\rho=2\), the derivative of the full phase at \(z_0\)
has modulus at most \(K r(w)\), where
\[
 r(w)=H+b\rho|w|+9(1+\rho)^2w^2,
 \qquad C_{\rm ref}=\frac{K(D+b+e)}{2(D-b-e)^2}.
 \tag{10}
\]
The disk bound \(|T''/k_0+D|\le b+e\), for
\(T(z)=S(x_h+z)+\Phi(x_h+z,x_h+w)\), implies
\(|z_c-z_0|\le r(w)/(D-b-e)\). Both this disk and the segment to
the actual critical point remain inside \(|z|<R\); the checker
verifies the strict worst-case inequality. The exact identity
\[
 T(z_c)-T(z_0)=-(z_c-z_0)^2
       \int_0^1 qT''(z_0+q(z_c-z_0))\,dq
 \tag{11}
\]
therefore bounds its modulus by \(C_{\rm ref}r(w)^2\). Integrating
the incoming derivative in (2) along the real reference segment gives
\[
 \begin{split}
 \Re S_+(x_h+w)\ge{}&M+\Re\Phi(x_h+\rho w,x_h+w)
       -\frac{\alpha s}2\rho^2w^2-KH\rho|w|\\
       &-\frac{Kb}2\rho^2w^2-C_{\rm ref}r(w)^2.
 \end{split}
 \tag{12}
\]
This retains the actual kernel phase at the correlated reference.

At the intermediate endpoint \(t=\sigma W\), put
\(v=\sigma w\), \(u=|v|\), and \(d=W-\rho v>0\).
The real curvature (6) and (9) give
\[
 \begin{split}
 &\Re\{\Phi(x_h+\sigma W,x_h+w)
                -\Phi(x_h+\rho w,x_h+w)\}\\
 &\hspace{5mm}\le
 \alpha(2-5\rho)vd+9K(1+\rho)^2u^2d-\frac{47}{10}d^2.
 \end{split}
 \tag{13}
\]
Combining (3), (12), and (13), the exponent relative to the outgoing
critical action is at most
\[
 \begin{split}
 E(v)={}&KHW-AW^2+\alpha(2-5\rho)vd
       +9K(1+\rho)^2u^2d-\frac{47}{10}d^2\\
       &+\frac{\alpha s+Kb}{2}\rho^2u^2+KH\rho u
       +C_{\rm ref}\{H+b\rho u+9(1+\rho)^2u^2\}^2.
 \end{split}
 \tag{14}
\]
This is increasing in the certified upper bound \(H\). At
\(H=H_*\), an outward exact interval partition of \([-W,W]\)
proves \(E(v)<-10^{-5}\). For orientation, the limiting upper
expression at \(v=W\) is less than \(-.00001198\); the proof
uses the entire interval cover, not that endpoint value.

For \(t=\sigma r\), \(r\ge W\), let
\(G_\sigma(r,w)=KHr-Ar^2+\Re\Phi(x_h+\sigma r,x_h+w)\).
Using (6) and the derivative at the reference point,
\[
 \partial_rG_\sigma(W,w)
 \le KH_*-2AW+\alpha(2-5\rho)W
 +9K(1+\rho)^2W^2-\frac{47}{5}(W-\rho W)<-1/20.
 \tag{15}
\]
Also \(\partial_r^2G_\sigma<-2A-47/5<0\) through \(r=.02\).
Thus the bound at \(W\) controls the entire intermediate interval
for every real output.

## 4. Complex output: endpoint completion and the same monotonicity

On \(|w|\le R\), the established phase transform gives
\(|h_+(0)|\le ZH\), \(|h_+'|<.16\), and
\[
 \Re S_+(x_h)\ge M+2c-C_0H^2,
 \quad Z=\frac{(21/20)\rho}{1-(3/10)\rho},\quad
 C_0=\frac{K(D+.6)}{2(D-.6)^2}.
 \tag{16}
\]
Use the exact original homogeneous quadratic and the holomorphic
cubic remainder at \(t=\sigma W\). The quadratic-completion
identity in [the earlier source-tail proof](research_three_source_tail_propagation.md)
then bounds the relative exponent by
\[
 \begin{split}
 E_{\mathbb C}={}&C_0H^2+KHW+KZHR+.08KR^2
 -(A+5\alpha/2)W^2+Q(W)+3K(W+R)^3,\\
 Q(W)={}&\lambda R^2+
 \frac{W^2K^2(\lambda-\rho\alpha)}{\lambda^2-\rho^2K^2},
 \qquad\lambda=3W/R.
 \end{split}
 \tag{17}
\]
The denominator is positive. At \(H=H_*\), the outward scalar
comparison gives \(E_{\mathbb C}<-10^{-4}\). The cubic bound
is used only at \(W<.01\), within its proved domain.

For the rest of the interval use (6), not an extrapolation of that
cubic estimate. At the left endpoint,
\[
 \partial_rG_\sigma(W,w)
 \le KH_*-2AW-5\alpha W+2KR+9K(W+R)^2<-1/20.
 \tag{18}
\]
Equation (6) again makes this derivative decreasing through \(.02\).
The original real-input kernel packet applies everywhere on these
intervals. Its polynomial prefactors, the incoming polynomial bound,
the original factor \(N\), and the fixed interval length are absorbed
into \(C'N^{q'}\). This proves (5) for both parts of the output union.
No incoming source is evaluated on a complex complementary interval.
\(\square\)

## 5. Reproduction

Run

```sh
python3 experiments/check_three_larger_source_intermediate_annulus.py --precision 192
```

The [checker](../experiments/check_three_larger_source_intermediate_annulus.py)
and [record](../repro/results/research-three-larger-source-intermediate-annulus.json)
retain the exact curvature cover, the scalar interval partition,
all strict margins, and the proof/script hashes. Their computational
scope is precisely the inequalities above; the previously proved
finite-source packets remain explicit dependencies.
