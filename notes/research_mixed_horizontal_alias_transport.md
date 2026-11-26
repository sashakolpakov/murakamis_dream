# Horizontal aliases on the full plateau

Research deduction, 5 November 2026. The lower horizontal alias of
the original conditional contour is uniformly below its fixed-reference
zero-mode line on the full real plateau. The upper alias has the same
property for a type-three conditional kernel. These comparisons require
no moving critical point. They do not bound the real tails, the joins,
or the type-four upper alias.

## 1. Fixed contours and the original allocation

Use the notation and the actual reference of the
[horizontal zero-mode theorem](research_mixed_horizontal_zero_mode_support.md):
\[
 \begin{split}
 a=x+ih_a,\quad b=z+ih_b,\quad
 x,z\in[11/50,9/20],\quad |h_a|,|h_b|\le3/25,\\
 Q_\epsilon(s;a,b)=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias,\\
 F(s;a,b)=Q_\epsilon(s;a,b)
             -(1+\eta/2)g(a)-(1+\epsilon/2)g(b),
 \qquad \eta,\epsilon\in\{0,1\}.
 \end{split}
 \tag{1}
\]
The original primitive satisfies
\(g'(w)=\operatorname{Log}(1-e^{-2\pi iw})\) on the regular
strip. The index real coordinate is
\(v\in[3/20,49/100]\). Its reference height \(y_0\) obeys
\[
             -27/250\le y_0\le17/250.
 \tag{2}
\]
These are the actual common bounds for ordinary and terminal attached
indices, including the terminal type-four lower bound \(-.108\).
The original horizontal aliases lie at heights \(\pm1/5\)
and have exponential penalty \(2\pi/5\).

All unshifted and shifted real parts in (1) lie strictly between zero
and one on this entire rectangle. Thus the logarithms below are on
their original lifts. The Fourier allocation in (1) is the same as in
the zero-mode theorem; in particular an unselected type-four outer
coordinate retains its actual negative reference height. Any separately
specified Fourier branch correction depends only on the outer targets
and is constant during the index-height comparisons below. It may be
retained on both sides, but is not silently discarded when comparing
with the actual reference plane.

## 2. A uniform bound on the original index argument

For real \(t\in(0,1)\) and arbitrary real \(h\), put
\[
 A(t,h)=\arg(1-e^{2\pi h-2\pi it}).
\]
The argument is positive for \(t<1/2\), negative for
\(t>1/2\), and zero at \(1/2\). Varying the positive radius
from zero to infinity, or just differentiating its argument, gives
\[
 \pi\min(1-2t,0)\le A(t,h)
                   \le\pi\max(1-2t,0).
 \tag{3}
\]
The bounds are strict away from \(t=1/2\) at finite nonzero
radius. In particular \(A(v,y)>0\). The exact original chirp
in (1) gives
\[
 \Im Q_{\epsilon,s}(v+iy;a,b)
 =A(v+x,y+h_a)+A(v+z,y+h_b)
             -(2+\epsilon)A(v,y)+2\pi x.
 \tag{4}
\]
Dropping the negative own term and applying (3) shows
\[
 \begin{split}
 \pi^{-1}\Im Q_{\epsilon,s}
 &<(1-2v-2x)_++(1-2v-2z)_++2x\\
 &=\max(1-2v,2x)+(1-2v-2z)_+\le29/25.
 \end{split}
 \tag{5}
\]
Indeed the two terms in the last line are at most \(9/10\)
and \(13/50\). This holds for both own types and every index
height in the original rectangle.

For \(\epsilon=0\) there is also the lower bound
\[
                         \Im Q_{0,s}>-29\pi/25.
 \tag{6}
\]
To check it, apply the lower estimates in (3) to the two shifted
arguments and the upper estimate to \(A(v,y)\). According to
whether \(v+x\) and \(v+z\) are below or above \(1/2\),
the resulting lower bounds after division by \(\pi\) are
\[
 \begin{array}{c|c}
 (v+x,v+z)&\text{lower bound}\\ \hline
 (\ge1/2,\ge1/2)&-2z\ge-9/10\\
 (<1/2,\ge1/2)&-1+2v+2x-2z\ge-29/25\\
 (\ge1/2,<1/2)&-1+2v\ge-7/10\\
 (<1/2,<1/2)&-2+4v+2x\ge-24/25.
 \end{array}
 \tag{7}
\]
The original index argument is strictly smaller than its upper bound,
so (6) remains strict also at the limiting real-coordinate cases.

## 3. Comparison with the same zero-mode line

The allocated outer terms in (1) are independent of the index height,
and
\(\partial_y\Re F(v+iy;a,b)=-\Im Q_{\epsilon,s}(v+iy;a,b)\).
Integrating (5) from \(-1/5\) to \(y_0\) yields
\[
 \boxed{\quad
 \Re F(v-i/5;a,b)-2\pi/5
 \le\Re F(v+iy_0;a,b)-\frac{557\pi}{6250}.
 \quad}
 \tag{8}
\]
Here
\(2/5-(29/25)(1/5+17/250)=557/6250\).
For a type-three conditional kernel, integration of (6) from
\(y_0\) to \(1/5\) similarly gives
\[
 \boxed{\quad
 \Re F(v+i/5;a,b)-2\pi/5
 \le\Re F(v+iy_0;a,b)-\frac{267\pi}{6250},
 \qquad\epsilon=0.
 \quad}
 \tag{9}
\]
The second constant uses
\(2/5-(29/25)(1/5+27/250)=267/6250\).
No derivative of a moving critical point enters either identity.

Let \(M\), \(p_a,p_b\), and \((x_0,z_0)\) be the actual
reference action, its allocated real marginals, and its outer real
coordinates. The zero-mode theorem bounds the fixed line pointwise by
\[
 \Re F(v+iy_0;a,b)
 \le M+p_a(x-x_0)+p_b(z-z_0)
       -\frac{(x-x_0)^2+(z-z_0)^2}{2500000}.
 \tag{10}
\]
It also retains a nonnegative index displacement loss, which is not
needed here. Equations (8)--(10) therefore transfer this same supporting
plane and outer quadratic loss to the entire lower horizontal alias,
with the displayed extra gap, and to both aliases when \(\epsilon=0\).

The original central factorial interpolation is valid on this fixed
compact regular-strip family. Its polynomial prefactors, half-grid
rounding, and one prescribed Fourier tolerance cost only an arbitrarily
small rate error. Consequently these pointwise bounds also bound the
corresponding original horizontal current integrals at every sufficiently
large level, for both parities. They concern the literal retained
currents, not a new interpolation or a sum with selected aliases deleted.

The type-four upper alias is not covered by (6). Nor do (8)--(10)
bound either real cut, the revived last rows, the right-tail interior,
or the zero-mode joins. In particular this deduction does not enlarge
the complete-source domain in the
[horizontal completion theorem](research_mixed_first_collar_horizontal_completion.md)
without the remaining current estimates.
