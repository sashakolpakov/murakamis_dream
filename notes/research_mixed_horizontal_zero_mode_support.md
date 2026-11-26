# Horizontal support for the fixed original conditional zero mode

Research lemma, 5 November 2026. The original saddle-height contour
has a joint horizontal supporting-plane bound on the whole real plateau,
even when a moving conditional root would leave its old index strip.
This controls the central zero-mode integral. The real tails, the
zero-mode joins, and both aliases still require their own estimates;
no complete horizontal finite-kernel extension is asserted here.

## 1. A joint domain larger than the individual cotangent cone

Use the original primitive \(g''(z)=\pi\cot\pi z-\pi i\)
and let
\[
 \begin{split}
 \mathcal S&=[.15,.49]+i[-.108,.068],\\
 \mathcal P&=[.22,.45]+i[-.12,.12],\\
 V(s,a)&=g(s+a)-g(s)-g(a).
 \end{split}
 \tag{1}
\]
Every individual argument and every pair sum lies strictly in its
original regular strip. Write
\(S=\cot\pi s=u+iv\), \(P=\cot\pi a=p+i\beta\).
For \(s\in\mathcal S\), \(a\in\mathcal P\), the following
elementary bounds hold:
\[
 \frac1{40}<u<2,\qquad
 \frac{(|v|-1)_+}{u}<\frac18,\qquad
 \frac9{70}<p<\frac32,\qquad |\beta|<\frac45.
 \tag{2}
\]

Here are direct scalar reductions, without a parameter cover.
For the real cotangent use
\[
 \Re\cot\pi(x+iy)
 =\frac{\sin(2\pi x)}{\cosh(2\pi y)-\cos(2\pi x)}.
 \tag{3}
\]
On the index rectangle, the sine is greater than \(3/50\)
and the denominator less than \(9/4\), since
\(\cosh(.216\pi)<5/4\). Thus \(u>2/75>1/40\).
Also \(u\le\cot(.15\pi)<2\). On the outer rectangle,
the sine is greater than \(3/10\) and the denominator less
than \(7/3\), giving \(p>9/70\), as in the
[open Hessian estimate](research_mixed_open_word_hessian.md).
The upper bound follows from
\(p\le\cot(.22\pi)<1/(.22\pi)<3/2\).

If \(|v|>1\), the real part of the index is below \(1/4\),
and the exact cotangent formula gives
\[
 \frac{|v|-1}{u}
 =\frac{\cos(2\pi\Re s)-e^{-2\pi|\Im s|}}
        {\sin(2\pi\Re s)}
 <\frac{3/5-1/2}{4/5}=\frac18.
 \tag{4}
\]
We used the exact pentagon inequalities
\(\cos(.3\pi)<3/5\), \(\sin(.3\pi)>4/5\), and
\(e^{-.216\pi}>1/2\), already established in the
[vertical contour proof](research_mixed_four_fixed_contour_transport.md).
The fraction decreases with the real coordinate and increases with
the absolute height, so (4) controls the whole rectangle.

The outer imaginary cotangent modulus is maximized at
\(\Re a=.22,|\Im a|=.12\). Monotonicity in height follows
from \(\cos(.44\pi)\cosh(.24\pi)<1\).
The sufficient scalar bounds
\[
 \sinh(.24\pi)<5/6,\qquad
 \cosh(.24\pi)>9/7,\qquad \cos(.44\pi)<1/5
 \tag{5}
\]
give \(|\beta|<175/228<4/5\). For completeness, (5) follows
from \(.75<.24\pi<.755\), the positive hyperbolic series
with a geometric bound on its remainder, and
\(\cos(.44\pi)=\sin(.06\pi)<.06(22/7)<1/5\).
The remaining scalar bounds in (2) follow from the same elementary
series: \(\cosh(.68)<5/4\),
\(\tan(.15\pi)>.47+.47^3/3>1/2\), and
\(\sin(.02\pi)>.06\).

## 2. The whole pair form is strictly positive

The general determinant identity is
\[
 \det(-\Re V''/\pi)
 =\frac{(u+p)^2-(pv-u\beta)^2}
        {(u+p)^2+(v+\beta)^2}.
 \tag{6}
\]
It is important here to use this exact criterion, rather than to
assume that each index separately lies in \(|\Im\cot|<1\).
Equation (2) gives
\[
 |pv-u\beta|<p+u(p/8+4/5)<p+79u/80<u+p.
 \tag{7}
\]
Thus the determinant is positive. If
\(C=\Re\cot\pi(s+a)\), then that determinant also equals
\(up-(u+p)C\). Hence \(C<up/(u+p)\), proving that
both diagonal entries of the pair matrix are positive.

An explicit common reserve is available. From (7), the numerator
of (6) is greater than \(up/40>9/112000\). Its denominator
is less than
\((7/2)^2+(5/4+4/5)^2<17\). The shifted real argument is
between \(.37\) and \(.94\), so
\(C\ge\cot(.94\pi)>-6\). Therefore the pair trace is
less than \(31/2\), and determinant divided by trace gives
\[
 -\Re V''\succ
 \frac{18\pi}{59024000}I_2
 \succ\frac1{1250000}I_2.
 \tag{8}
\]
All estimates are strict on the closed domains in (1).

For types \(\eta,\epsilon\in\{0,1\}\), retain the exact
allocated, uneliminated phase
\[
 \begin{split}
 F_{\eta\epsilon}(s,a,b)
 ={}&V(s,a)+V(s,b)-\epsilon g(s)
       -\tfrac\eta2g(a)-\tfrac\epsilon2g(b)+2\pi ias.
 \end{split}
 \tag{9}
\]
The bilinear chirp has purely imaginary Hessian. All additional
own terms have nonnegative negative real Hessian because their
real cotangents are positive. Adding the two pair forms in (8)
therefore proves
\[
 -\Re F_{\eta\epsilon}''\succ\mu I_3,
 \qquad \mu=1/1250000,
 \quad (s,a,b)\in\mathcal S\times\mathcal P^2.
 \tag{10}
\]
No critical root is needed to establish (10).

## 3. A fixed-reference horizontal zero-mode estimate

Let \((s_0,a_0,b_0)\) be an actual original conditional reference
of an open word, with both outer legs in \(\mathcal P\).
Ordinary index roots and attached endpoint index roots obey
\(s_0\in\mathcal S\), as recorded in the vertical contour proof.
Let \(\phi\) denote the original allocated critical phase near
that reference, and put
\[
 M=\Re F(s_0,a_0,b_0),\quad
 P_a=\partial_a\phi(a_0,b_0),\quad
 P_b=\partial_b\phi(a_0,b_0).
 \tag{11}
\]
The original index equation is \(F_s(s_0,a_0,b_0)=0\), so
\(P_a=F_a\) and \(P_b=F_b\) there.

Keep all three imaginary parts fixed at their reference values.
For any \(s=t+i\Im s_0\) with \(.15\le t\le.49\),
and any real outer changes \(d_a,d_b\) leaving the two real
targets in \([.22,.45]\), the straight segment from the reference
lies in the product (1). Integrating (10) along it gives
\[
 \begin{split}
 \Re F(s,a_0+d_a,b_0+d_b)
 \le{}&M+\Re(P_a)d_a+\Re(P_b)d_b\\
 &-\frac\mu2\{(t-\Re s_0)^2+d_a^2+d_b^2\}.
 \end{split}
 \tag{12}
\]
This is a joint uneliminated supporting-plane estimate; it does
not substitute a new root into the phase.

The original regular-strip factorial interpolation is valid uniformly
on this entire fixed contour and parameter product. For unselected
type-four outer coordinates, retain their actual negative reference
heights, so the actual Fourier upper rate is its factorial branch.
The unchanged zero-mode coefficient is \(+N\). Bounding its
integral absolutely by (12), including both allocated outer
halfweights, consequently gives the central zero-mode upper rate
\[
 M+\Re(P_a)d_a+\Re(P_b)d_b
       -\frac{d_a^2+d_b^2}{2500000}+\eta
 \tag{13}
\]
for every fixed \(\eta>0\), with a polynomial level factor,
at both parities. The original half-grid rounding changes the compact
contours by \(O(N^{-1})\) and is absorbed by the same tolerance.
No moving Gaussian calculation or new nonzero
packet is asserted. The general curvature statement (10) allows
the larger height box; the finite assertion (13) only uses the
unselected actual reference heights just specified.

The full kernel additionally contains the zero-mode joins, the real
tails, and both horizontal and vertical aliases. Equation (13) does
not bound those other pieces. In particular the
[released-height obstruction](research_mixed_horizontal_root_obstruction.md)
shows why moving-root containment cannot be supplied from the
independent height box alone. The original fixed-reference contour
avoids that containment requirement, but a complete horizontal
source theorem still needs its remaining currents bounded by the
same supporting plane. All frozen source theorems remain unchanged.
