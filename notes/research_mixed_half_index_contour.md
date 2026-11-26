# Extending the fixed original index contour to one half

Research deduction, 5 November 2026. The fixed-reference horizontal
supporting plane and the asymmetric complete-contour bound remain valid
with right cut \(1/2\). This absorbs all rows between the old cut
\(49/100\) and \(1/2\) into the controlled central integral. The real
rows above \(1/2\) remain explicit; no sign for their excess is asserted.
There is no new root calculation, parameter cover, or change to a
frozen source certificate.

## 1. The additional pair strip

Use the original primitive, allocation and actual reference of the
[fixed zero-mode theorem](research_mixed_horizontal_zero_mode_support.md).
Set
\[
 \begin{split}
 \mathcal S_*&=[3/20,1/2]+i[-27/250,17/250],\\
 \mathcal P&=[11/50,9/20]+i[-3/25,3/25],\\
 V(s,a)&=g(s+a)-g(s)-g(a).
 \end{split}                                                    \tag{1}
\]
The old theorem already controls \(\Re s\le49/100\). On the
remaining strip write
\[
 S=\cot\pi s=u+iv,\qquad P=\cot\pi a=p+i\beta.
\]
The following bounds hold, including the real endpoint \(s=1/2\):
\[
 0\le u<\frac4{125},\qquad |v|<\frac{17}{50},\qquad
 \frac9{70}<p<\frac32,\qquad |\beta|<\frac45.          \tag{2}
\]
The last two are unchanged from the old theorem. For the first,
\(u\le\cot(.49\pi)=\tan(.01\pi)<4/125\), using
\(\sin t\le t\), \(\cos t\ge1-t^2/2\), and \(\pi<22/7\).
For the second, the exact cotangent formula shows that the absolute
imaginary part increases with absolute height on this strip: its
height derivative has the sign of
\(1-\cos(2\pi\Re s)\cosh(2\pi\Im s)>0\).
It is largest at real part \(49/100\) and absolute height
\(27/250\). The elementary bounds
\[
 \sinh(.216\pi)<\frac34,\qquad
 \cosh(.216\pi)>\frac{123}{100},\qquad
 \cos(.02\pi)>\frac{499}{500}                         \tag{3}
\]
give
\[
 |v|<\frac{3/4}{123/100+499/500}
      =\frac{375}{1114}<\frac{17}{50}.
\]
For explicit rational proofs of (3), use \(157/50<\pi<22/7\).
The lower hyperbolic bound follows from \(\cosh t>1+t^2/2\)
at \(t=4239/6250\); the cosine bound follows from
\(\cos t\ge1-t^2/2\) at \(t=11/175\). Finally
\(.216\pi<17/25\), and the positive sinh series gives
\[
 \sinh t\le t+\frac{t^3}{6}
          +\frac{t^5}{120(1-t^2/42)}<\frac34,
                      \qquad 0\le t\le17/25.          \tag{4}
\]
The denominator bounds the ratio of successive terms starting with
\(t^5/5!\). These are scalar inequalities, not interval sampling.

The exact pair determinant from the old theorem is
\[
 \det(-\Re V''/\pi)
 =\frac{(u+p)^2-(pv-u\beta)^2}
        {(u+p)^2+(v+\beta)^2}.                         \tag{5}
\]
Equation (2) implies
\(|pv-u\beta|<(4/5)(u+p)\). The numerator of (5) is
therefore greater than \(9p^2/25\), and its denominator is less
than
\[
 (4/125+3/2)^2+(17/50+4/5)^2<4.
\]
Writing \(C=\Re\cot\pi(s+a)\), the determinant also equals
\(up-(u+p)C\). Hence both pair diagonal entries are positive,
even when \(u=0\). Since
\(71/100\le\Re(s+a)\le19/20\),
\(C\ge\cot(19\pi/20)>-7\), so the pair trace is less
than \(u+p-2C<16\). Determinant divided by trace now yields
\[
 -\Re V''\succ\frac{729\pi}{7840000}I_2
                 \succ\frac1{4000}I_2               \tag{6}
\]
on the additional strip. Together with the old portion, the original
common constant \(\mu=1/1250000\) remains valid everywhere in
\(\mathcal S_*\times\mathcal P\).

## 2. The original supporting plane is unchanged

Retain the original allocated phase
\[
 F_{\eta\epsilon}(s,a,b)=V(s,a)+V(s,b)-\epsilon g(s)
       -\frac\eta2g(a)-\frac\epsilon2g(b)+2\pi ias,
                      \qquad \eta,\epsilon\in\{0,1\}. \tag{7}
\]
Its chirp Hessian has zero real part. All three additional own
negative real Hessians are nonnegative; the index one is allowed
to vanish at real part \(1/2\). The two pair estimates therefore
give \(-\Re F''\succ\mu I_3\) on
\(\mathcal S_*\times\mathcal P^2\).

Let \((s_0,a_0,b_0)\) be the same actual conditional reference as in
the old theorem, let \(M=\Re F(s_0,a_0,b_0)\), and retain the
original allocated marginals \(p_a,p_b\). All three heights stay
fixed at their reference values. With
\(d_a=\Re(a-a_0)\), \(d_b=\Re(b-b_0)\), set
\[
 B(a,b)=M+p_ad_a+p_bd_b
                   -\frac{d_a^2+d_b^2}{2500000}.       \tag{8}
\]
The index equation \(F_s(s_0,a_0,b_0)=0\) and horizontal
integration of (6)--(7) prove
\[
              \Re F(v+i\Im s_0;a,b)\le B(a,b),
                         \qquad 3/20\le v\le1/2.      \tag{9}
\]
This is the same plane and quadratic loss as before. No moving
index root or new elimination is used.

## 3. All currents on the longer asymmetric contour

Use the exact original contour of the
[asymmetric-contour theorem](research_mixed_horizontal_asymmetric_contour.md),
now with central interval \([3/20,1/2]\), lower height \(-1/5\)
and upper height \(1\). Every factorial argument still has real
part strictly between zero and one: the largest shifted real part
is \(1/2+9/20=19/20\).

The argument bounds (3)--(7) of that theorem hold unchanged at
\(v=1/2\). In its four-case table, all lower bounds increase with
\(v\); the upper estimates use decreasing positive parts of
\(1-2(v+x)\) and \(1-2(v+z)\). The own argument is nonnegative
for \(v\le1/2\), including its zero value at \(v=1/2\).
Thus the lower and upper horizontal aliases remain below (8) by
\(557\pi/6250\) and \(13/100\), respectively. The same
all-height marginal bounds make every vertical alias at the new
real cut decrease away from that cut after its Fourier penalty.

The zero-mode joins run only from height zero to \(\Im s_0\).
Their vertical convexity follows from the newly extended negative
real Hessian. Each is bounded by the maximum of its real cut rate
and (8). The full exact residue decomposition, its \(+N\) central
coefficient, every alias and join, and both level parities are
unchanged. Moving a half-grid cut by \(O(N^{-1})\) is harmless on
the common compact regular strip and uses only the single prescribed
rate tolerance.

Define \(\mathcal R_\epsilon\) by equation (13) of the cited
asymmetric-contour theorem, retaining both actual unselected Fourier
halfweights and every revived row. Put
\[
 T_*(a,b)=\max_{u\in[0,3/20]\cup[1/2,1]}
                                  \mathcal R_\epsilon(u;a,b).
                                                               \tag{10}
\]
For every fixed \(\tau>0\), the same literal finite kernel satisfies
\[
 \begin{split}
 &|C_{\epsilon,N}(e^{-2\pi ia},e^{-2\pi ib})|
 |d_N(e^{-2\pi ia})|^{\eta/2}
 |d_N(e^{-2\pi ib})|^{\epsilon/2}\\
 &\hspace{12mm}\le C_\tau N^A
                 \exp N\{\max(B(a,b),T_*(a,b))+\tau\}.
 \end{split}                                                    \tag{11}
\]
The original actual-height/Fourier-branch hypotheses remain necessary.
This is not an assertion on arbitrary independently selected heights.

The left tail still has its maximum at \(3/20\). The right tail
has its maximum among the real cut \(1/2\), the endpoint \(1\),
and **all** real roots \(w>0\) of polynomial (18) in the cited
theorem, where \(w=-\cot\pi u\). Zero walls are decreasing
and introduce no extra maximum. This narrows the exact remaining
comparison to \(T_*\le B\), or to a specified payable excess.
Neither that sign nor whole open-source dominance is concluded here.
The transverse-derivative and ordinary-color restrictions of the
asymmetric-contour theorem also remain unchanged.
