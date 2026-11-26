# A direct half-row comparison with the original supporting plane

Research deduction, 5 November 2026. An explicit sign condition on the
unchanged outer heights and the two moving real targets makes the real
half row no larger than the corresponding point on the original saddle
height. The fixed-contour horizontal theorem then pays that row with
the original two supporting marginals. This proves a region of the
missing half-row comparison; it does not assert that every actual
reference and every pair of horizontal targets satisfies the condition.

## 1. The original phase and the sufficient condition

Retain the original normalized primitive
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},
 \qquad g'(z)=\operatorname{Log}(1-e^{-2\pi iz}),
 \tag{1}
\]
with its regular-strip continuation, and the complete allocated phase
\[
 F(s;a,b)=g(s+a)+g(s+b)-(2+\epsilon)g(s)
 -(1+\eta/2)g(a)-(1+\epsilon/2)g(b)+2\pi ias.
 \tag{2}
\]
Here \(\eta,\epsilon\in\{0,1\}\). Let
\((s_0,a_0,b_0)\) be an actual original conditional reference in the
scope of the [half-index fixed-contour theorem](research_mixed_half_index_contour.md),
so \(F_s(s_0;a_0,b_0)=0\) on its original logarithmic lift. Set
\[
 \begin{split}
 y_0=\Im s_0,\quad h_a=\Im a_0,\quad h_b=\Im b_0,\qquad
 a=x+ih_a,\quad b=z+ih_b,\quad x,z\in[11/50,9/20],\\
 d_a=x-\Re a_0,\quad d_b=z-\Re b_0,\qquad
 M=\Re F(s_0;a_0,b_0),\\
 p_a=\Re F_a(s_0;a_0,b_0),\qquad
 p_b=\Re F_b(s_0;a_0,b_0),\qquad \mu=1/1250000,\\
 B(a,b)=M+p_ad_a+p_bd_b-\frac\mu2(d_a^2+d_b^2).
 \end{split}
 \tag{3}
\]
All heights remain their actual reference heights; in particular the
physical halfweight interpretation is the unselected one used in the
fixed-contour theorem. No independent reference-height relaxation is
made here.

Put
\[
 \begin{split}
 A=2\pi x,\quad Z=2\pi z,\qquad
 r_a=e^{2\pi h_a},\quad r_b=e^{2\pi h_b},\\
 q(x,z;h_a,h_b)
 =\sin A+r_b\sin(A-Z)-r_ar_b\sin Z.
 \end{split}
 \tag{4}
\]

**Theorem 1.** If
\[
                         y_0q(x,z;h_a,h_b)\le0,
 \tag{5}
\]
then the original allocated half-row rate satisfies
\[
 \begin{split}
 \mathcal R_\epsilon(1/2;a,b)
 &=\Re F(1/2;a,b)\\
 &\le\Re F(1/2+iy_0;a,b)\\
 &\le B(a,b)-\frac\mu2(1/2-\Re s_0)^2.
 \end{split}
 \tag{6}
\]
The equality on the first line retains the original chirp and both
allocated outer halfweights. The half row has no wrapped numerator
wall because \(1/2+x,1/2+z<1\). The last reserve is strictly positive
for every original reference in question, since \(\Re s_0<1/2\).

## 2. The exact vertical sign

For real \(y\), put \(t=e^{2\pi y}>0\). Since
\(g'(1/2+iy)=\log(1+t)\) is real, the own-index factorial term in
(2) contributes nothing to the imaginary marginal on this line.
The exact original marginal is therefore
\[
 \Theta(y):=\Im F_s(1/2+iy;a,b)
 =A+\arg(1+r_at e^{-iA})+\arg(1+r_bt e^{-iZ}).
 \tag{7}
\]
For every \(R>0\) and \(0<\theta<\pi\), the argument of
\(1+Re^{-i\theta}\) lies strictly between \(-\theta\) and zero:
the positive sum of the rays of arguments zero and \(-\theta\)
lies in their open sector. These are the original logarithmic
arguments, because their imaginary parts are negative and no cut is
crossed. Hence
\[
                         -Z<\Theta(y)<A,
 \qquad -\pi<\Theta(y)<\pi.
 \tag{8}
\]
There is consequently no ambiguity in recovering the sign of
\(\Theta\) from the imaginary part of its exponential. Multiplying
the two factors in (7) gives that imaginary part, up to a positive
modulus, as
\[
 Q(t)=\sin A+r_bt\sin(A-Z)-r_ar_bt^2\sin Z.
 \tag{9}
\]
Its constant term is positive and its quadratic coefficient is
negative. The two real roots have negative product, so exactly one
is positive. Thus \(Q(t)>0\) before that positive root and
\(Q(t)<0\) after it. In particular \(Q(1)=q\).

If \(y_0<0\), condition (5) says \(Q(1)\ge0\). Therefore
\(Q(t)\ge0\) throughout \(e^{2\pi y_0}\le t\le1\).
Equations (7)--(9) and the Cauchy--Riemann identity give
\[
 \frac{d}{dy}\Re F(1/2+iy;a,b)=-\Theta(y)\le0
 \quad(y_0\le y\le0).
 \tag{10}
\]
Integrating in the increasing direction from \(y_0\) to zero proves
the first inequality in (6).

If \(y_0>0\), condition (5) says \(Q(1)\le0\). The positive
root is then at most one, so \(Q(t)\le0\) for
\(1\le t\le e^{2\pi y_0}\). The derivative in (10) is now
nonnegative; integrating from zero to \(y_0\) gives the same
inequality. If \(y_0=0\), the two rates are identical and no sign
condition on \(q\) is needed. This treats all equality cases in (5).

For the final line of (6), apply the unchanged joint horizontal
Hessian bound \(-\Re F''\succ\mu I_3\) on the fixed original
height slice, now including index real coordinate \(1/2\).
The original index derivative is zero; the two other real derivatives
are precisely \(p_a,p_b\). Taylor's formula therefore retains the
index displacement as well as the two outer displacements:
\[
 \Re F(1/2+iy_0;a,b)
 \le M+p_ad_a+p_bd_b
 -\frac\mu2\bigl((1/2-\Re s_0)^2+d_a^2+d_b^2\bigr).
 \tag{11}
\]
This proves the theorem. In particular no marginal at a new cut,
new conditional root, or independently optimized real phase replaces
the original supporting plane.

## 3. Explicit regions and the remaining comparison

**Corollary 2.** Condition (5), and hence (6), holds in either region
\[
 \begin{array}{ll}
 y_0\le0,\ h_a\le0,\ h_b\le0, & x\ge z,\\
 y_0\ge0,\ h_a\ge0,\ h_b\ge0, & x\le z.
 \end{array}
 \tag{12}
\]
For example the first region covers all horizontal targets with
\(x\ge z\) when the actual index and both outer coordinates have
negative heights. This includes the corresponding ordinary
type-four incidences; no assertion about a mixed-sign incidence is
inferred merely from its types.

To prove the first case, use \(r_a,r_b\le1\) to obtain
\[
 q\ge \sin A+r_b\{\sin(A-Z)-\sin Z\}
 \ge\min\{\sin A,\ \sin A+\sin(A-Z)-\sin Z\}\ge0.
 \tag{13}
\]
The last inequality uses the exact identity
\[
 \sin A+\sin(A-Z)-\sin Z
 =4\sin((A-Z)/2)\cos(A/2)\cos(Z/2),
 \tag{14}
\]
and \(A\ge Z\). For the second case \(r_a,r_b\ge1\) and
\(A\le Z\); the coefficient
\(\sin(A-Z)-\sin Z\) is strictly negative. Reversing the
two radius comparisons in (13) gives \(q\le0\).

Condition (5) is more general than (12) and is a direct elementary
test. For instance, when \(y_0<0\), it is equivalently
\[
 r_a\le
 \frac{\sin A+r_b\sin(A-Z)}{r_b\sin Z};
 \tag{15}
\]
a nonpositive numerator makes this region empty. For \(y_0>0\)
the inequality reverses; the undivided form (5) remains valid in
all cases.

This removes the half row from the
[three-row full-source upper bound](research_mixed_right_tail_endpoint_bound.md)
on the region (5). The two other calibrated comparisons at index
\(3/20\) and at the revived endpoint \(1\) remain required,
or their excess must be retained and paid in the full boundary
assembly. The complement of (5) has not been estimated here.
No new finite-source interpolation, transverse derivative estimate,
parameter cover, or knot-family conclusion is used or asserted.
