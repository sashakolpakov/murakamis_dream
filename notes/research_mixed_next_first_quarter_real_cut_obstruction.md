# The real right cut cannot be paid inside the first quarter

Private exact source obstruction, 8 November 2026. No mathematical
numerical evaluation, saved-value calculation, or frozen-source
change is used.

The proposed separate right-cut estimate fails at the original
complete outside value \(u=0\). This does not obstruct the full
edge packet, which is already proved there on a different contour.

## 1. Original branch and statement

Use the actual cubic family and original wire phase of
[the first-quarter reduction](research_mixed_next_two_angle_bare_first_quarter_contour.md),
equations (1)--(5),(13)--(14). At \(u=0\), put
\[
 t_3=t(0),\qquad
 v=2\cos(t_3/2)=x+ib,\qquad
 y_*=\pi^{-1}\arctan\!\bigl(\cos(t_3/2)\bigr)
                  =x_*+ih_* .
 \tag{1}
\]
These are the original selected branches. In particular
\[
 0<x_*<1/4,\qquad h_*>0,\qquad
 F_y(y_*;t_3,0)=0,\qquad
 \psi(t_3,0)=F(y_*;t_3,0).
 \tag{2}
\]
No root is chosen by a new numerical approximation.

**Theorem.** For every real \(\beta\) satisfying
\(x_*\le\beta\le1/4\), one has
\[
 \boxed{\qquad
       \Re F(\beta;t_3,0)>\Re\psi(t_3,0).
 \qquad} \tag{3}
\]
Consequently there is no fixed
\[
 \sup_{u\in\mathcal U_+}\Re y_*(u)<\beta<1/4
\]
for which the real right-cut rate is uniformly strictly below the
selected action on the actual family \(\mathcal U_+\).
Indeed that estimate would already fail at its member \(u=0\).

## 2. An exact modulus inequality at the actual cubic root

The [adopted cubic theorem](research_mixed_next_inner_three_cubic_continuation.md)
gives
\[
 v^3-2iv^2-3v+2i-2=0,\qquad
 x>0,\qquad \frac13<b<\frac23 .
 \tag{4}
\]
Write \(p=x^2\). The imaginary and real parts of (4) are
\[
 p=p(b):=\frac{b^3-2b^2+3b-2}{3b-2},\qquad
                    2=\sqrt{p(b)}\,Q(b),
 \tag{5}
\]
\[
                  Q(b)=p(b)-3b^2+4b-3.
\]
On \(1/3<b<2/3\), the numerator and denominator defining
\(p\) are negative, so \(p>0\), and direct differentiation gives
\[
 p'(b)=
 \frac{2b\{3(b-1)^2+1\}}{(3b-2)^2}>0,\qquad
                   Q'(b)=p'(b)+4-6b>0 .
 \tag{6}
\]

At the rational point \(b_0=29/50\),
\[
 p_0=\frac{92211}{32500},\qquad
 Q_0=\frac{9328}{8125},
\]
\[
 \frac{17}{6}<p_0<\frac{20}{7},\qquad
 0<Q_0<\frac76,\qquad b_0^2>\frac13.
 \tag{7}
\]
The respective integer comparisons are
\[
 553266>552500,\qquad 645477<650000,\qquad
 55968<56875,\qquad 2523>2500.
\]
If the actual \(b\) were at most \(b_0\), equation (5) would
give \(Q(b)>0\), while (6)--(7) would imply
\[
 1=\frac{p(b)Q(b)^2}{4}
   \le\frac{p_0Q_0^2}{4}
   <\frac14\frac{20}{7}\left(\frac76\right)^2
   =\frac{35}{36}<1 .
 \tag{8}
\]
This contradiction proves
\[
                     b>b_0,\qquad
                     p>\frac{17}{6},\qquad b^2>\frac13 .
 \tag{9}
\]

For \(p\ge17/6\) and \(q\ge1/3\), the function
\[
                         (p+q)^2-4(p-q)
\]
increases strictly in both variables: its two derivatives are
\(2(p+q)-4>0\) and \(2(p+q)+4>0\).
Since \(\cos t_3=(v^2-2)/2\), (9) yields
\[
\begin{split}
 |\cos t_3|^2-1
 &=\frac{(p+b^2)^2-4(p-b^2)}4\\
 &>\frac14\left\{\left(\frac{19}{6}\right)^2-10\right\}
   =\frac1{144}.
\end{split} \tag{10}
\]
Thus the exact original root satisfies \(|\cos t_3|>1\).

## 3. The real cut lies above the selected action

The original derivative identity in
[the complete-end ray proof](research_pair_free_boundary_kernel.md),
equation (4), is
\[
 e^{F_y(y;t_3,0)}
   =\frac{A-(1-A)z^2}{z^4},
 \qquad A=\cos^2(t_3/2),\quad z=\tan(\pi y).
 \tag{11}
\]
At \(y=1/4\), \(z=1\), so (10)--(11) give
\[
             \Re F_y(1/4;t_3,0)=\log|\cos t_3|>0 .
 \tag{12}
\]
Only the real part of the original logarithmic derivative is used;
there is no change of its charge. This endpoint remains in the
regular factorial domain, since \(0<\Re t_3<\pi/2\).

The first-quarter source proof, equation (26), gives
\[
 \Re F_{yy}(r+i\sigma;t_3,0)<0,
               \qquad 0<r<1/4,\quad \sigma\ge0 .
 \tag{13}
\]
At real height, (12)--(13) imply
\[
                      \Re F_y(r;t_3,0)>0
                            \quad(0<r\le1/4).
 \tag{14}
\]
Hence the real-cut rate is strictly increasing throughout that
interval.

For the vertical line through \(x_*\), let
\[
                       f(\sigma)=\Re F(x_*+i\sigma;t_3,0).
\]
Equations (2),(13) imply
\[
 f''(\sigma)=-\Re F_{yy}(x_*+i\sigma;t_3,0)>0,\qquad
                              f'(h_*)=0 .
 \tag{15}
\]
Since \(h_*>0\), strict convexity gives
\[
             \Re F(x_*;t_3,0)=f(0)>f(h_*)=\Re\psi(t_3,0).
 \tag{16}
\]
Combining (14),(16) proves (3).

This obstruction concerns the actual real upper rate assigned to
the original right cut. It does not show that the signed cut current
itself has a corresponding lower bound, or that cancellation with
the remaining source is impossible. In particular the complete
free-boundary edge packet at \(u=0\) remains valid: its ray contour
continues beyond the first quarter and has separately paid endpoint
sectors. A successful continuation of the first-quarter reduction
must therefore change that cut treatment or retain the necessary
signed contour combination. No full two-angle, inner-kernel, or
outer-transfer conclusion is asserted here.
