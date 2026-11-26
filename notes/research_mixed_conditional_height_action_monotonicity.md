# The conditional action increases as the incoming contour moves down

Research deduction, 7 November 2026. On the displaced incoming
rectangle, the original conditional action increases strictly
when its incoming height decreases. Its known real-arc action
floor therefore holds at the full required negative depth.
The proof is an elementary consequence of the critical equation
and the original logarithmic lift.

This is a statement about the critical action. It gives no
estimate of the complete finite sum away from its already
proved source domains. No numerical evaluation is used.

## 1. Original branch and derivative

Use the phase \(Q\), parameters \(a,y\), and selected root
\(v=e^{2\pi it}\) of
[the negative-height branch theorem](research_mixed_conditional_negative_height_branch.md).
Thus
\[
 \frac12\le x=\Re a\le\frac7{10},\quad
 -\frac9{125}\le h=\Im a\le0,\qquad
 y\in[11/50,9/20]+i[0,1/100],
\tag{1}
\]
and
\[
 X=e^{-2\pi ia},\quad Y=e^{-2\pi iy},\quad
 \Im v>0,\quad \arg v<\arg X,\quad Q_t=0.
\tag{2}
\]
At \(x=1/2\), \(\arg X=\pi\). The same theorem supplies
all original strip margins, simplicity, and holomorphic dependence.

Let
\[
       \Theta(a,y)=Q(t(a,y);a,y),\qquad
       w=\frac{v-X}{1-X}.
\tag{3}
\]
Stationarity and the unchanged incoming carrier give
\[
 \Theta_a=g'(a+t)-g'(a)+2\pi it,\qquad
                             e^{\Theta_a}=w.
\tag{4}
\]
No additive constant in \(\Theta\) is changed in (3).

## 2. An upper-half-plane property of the derivative

**Lemma.** On (1), \(\Im w>0\).

*Proof.* At a negative real \(X\), this is immediate from
\(\Im v>0\) and \(1-X>0\). It suffices to exclude a real
value of \(w\) as \(X\) moves into the upper left quadrant.
The cases \(w=0,1\) would give \(v=X,1\), already excluded
by the critical equation.

Suppose \(w\) is real and \(\Im X>0\).
The identity
\[
                          v=w+(1-w)X
\tag{5}
\]
and \(\Im v>0\) imply \(w<1\). If \(w<0\), then
\(\Im(v/X)=w\Im(X^{-1})>0\), contradicting
\(0<\arg v<\arg X<\pi\). Hence
\[
                              0<w<1.
\tag{6}
\]

Write \(A=\Re v\), \(r=|v|^2>0\), and \(d=1-A\).
Since \(\Re X<0\) and \(|X|\le1\), (5) gives
\[
                    A<w,\qquad r\le1-2wd.
\tag{7}
\]
For the second inequality, use the exact identity
\[
 |v|^2=1-2w(1-w)(1-\Re X)
                           -(1-w)^2(1-|X|^2)
\]
and \(d=(1-w)(1-\Re X)>0\).

The original critical equation (3) of the branch theorem
can be rearranged, at (5), as
\[
                        Y=2-\frac1v+\frac{(v-1)^2}{w}.
\tag{8}
\]
Taking imaginary parts gives
\[
             \frac{\Im Y}{\Im v}=\frac1r-\frac{2d}{w}.
\tag{9}
\]
Since \(\Im Y<0\), it follows that \(w<2rd\).
Combining this with (7),
\[
           w<2d(1-2wd),\qquad
           w<\frac{2d}{1+4d^2}\le\frac12.
\tag{10}
\]
The last inequality is \((2d-1)^2\ge0\).
In particular \(A<1/2\).

We show that (8) must then have \(\Re Y>1\), a contradiction.
Multiplication by the positive number \(wr\) gives
\[
 wr(\Re Y-1)
       =w(r-A)+r(2A^2-2A+1-r)=:M.
\tag{11}
\]
If \(A\le0\), the first term is strictly positive and the
second is nonnegative, since \(r\le1\).
If \(A>0\), (7) and \(w>A\) give
\[
                    r<1-2A(1-A)=2A^2-2A+1.
\tag{12}
\]
Thus \(M>0\) when \(r\ge A\).
In the remaining case \(r<A\), the inequality \(w<2rd\)
multiplies a negative number \(r-A\), so
\[
\begin{split}
 M&>2rd(r-A)+r(2A^2-2A+1-r)\\
  &=r(1-2A)(r+1-2A)>0,
\end{split}
\tag{13}
\]
where the last sign uses \(A<1/2\).
All possibilities contradict \(\Re Y<1\).

Therefore \(w\) never crosses the real axis. Continuation
from negative real \(X\) proves the lemma. \(\square\)

## 3. The original logarithm and the action floor

At \(x=1/2\), write \(X=-\rho\), \(\rho>0\).
Using the actual principal logarithms in (4) gives
\[
       \Im\Theta_a=\arg(v+\rho)=\Arg w\in(0,\pi).
\tag{14}
\]
Indeed the argument of \(1-X/v=(v+\rho)/v\), plus
the carrier argument \(2\pi\Re t=\arg v\), is
\(\arg(v+\rho)\); \(1-X=1+\rho\) is positive real.
The lemma and continuity now preserve this exact lift throughout
(1):
\[
                              \Im\Theta_a=\Arg w\in(0,\pi).
\tag{15}
\]

Holomorphy consequently gives
\[
       \frac{\partial}{\partial h}\Re\Theta(x+ih,y)
                       =-\Im\Theta_a(x+ih,y)<0.
\tag{16}
\]
For \(-9/125\le h_1<h_2\le0\),
\[
 \Re\Theta(x+ih_1,y)-\Re\Theta(x+ih_2,y)
      =\int_{h_1}^{h_2}\Arg w(x+is,y)\,ds>0.
\tag{17}
\]
The [complete real-arc conditional theorem](research_mixed_real_arc_complete_conditional_packet.md)
proved, with the original normalization,
\(\Re\Theta(x,y)>13/24\). Thus
\[
             \boxed{\ \Re\Theta(x+ih,y)>\frac{13}{24}\ }
                     \qquad\text{throughout (1)}.
\tag{18}
\]
Since the parameter set is compact and the original derivative
stays strictly in the upper half-plane, its argument also has
a positive uniform minimum. No numerical value of that minimum
is needed or asserted.

## 4. What this supplies for the finite-source problem

The branch theorem already puts the selected critical point
strictly between the original lower index cut and the incoming
numerator wall, and gives strict horizontal curvature at every
height of that regular index interval. Equations (16)--(18)
add an absolute lower bound for its original critical action at
the full negative incoming height.

They do not compare this action with all physical end rows
or the two finite contour remainders after the incoming
parameter moves. Those source terms also change with the
incoming height, including the carrier \(X^{-j}\). Nor do
these equations control the cap factor or the next geometric
affine comparison. A complete source asymptotic must retain
and bound those contributions before the critical action
can be used as the growth rate of the finite sum.
