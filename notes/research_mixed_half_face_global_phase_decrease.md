# Uniform decrease of the original incoming critical action

Research deduction, 7 November 2026. The original cap--conditional
critical action has a strictly negative incoming derivative on the
entire real arc \(1/2\le a\le7/10\), uniformly over the selected
outgoing rectangle. The proof keeps the selected cap branch and the
original zero logarithmic lift of the conditional equation.

This settles the phase-sign question left open in
[the general incoming transport theorem](research_mixed_half_face_general_incoming_transport.md).
It does not continue the complete finite-source asymptotics over
that arc. The endpoint saddle leaves the previously proved source
rectangle, so its finite tails and contour currents remain a
separate obligation. No numerical evaluation is used.

## 1. Original branches and exact multipliers

Throughout, the ordinary color is \(-2\), and
\[
 \mathcal A=[1/2,7/10],\qquad
 \mathcal Y=\{11/50\le\Re y\le9/20,\quad0\le\Im y\le1/100\}.
                                                                    \tag{1}
\]
Retain the original phases, their additive constants and their
logarithmic lifts from the general transport theorem:
\[
 \begin{split}
 \Psi(e,a)&=S(e)+J(e+a)-J(a)-i\pi ea,\\
 Q(t;a,y)&=g(a+t)+g(y+t)-3g(t)-g(a)-g(y)+2\pi iat,\\
 \mathcal P(a,-2,y)&=\mathcal T(a,-2)+\Theta(a,y).
 \end{split}                                                       \tag{2}
\]
The last two actions evaluate \(\Psi,Q\) on the continued original
critical points. Put
\[
 X=e^{-2\pi ia},\quad Y=e^{-2\pi iy},\quad
 \omega=e^{2\pi iu_c(e)},\quad p=e^{2\pi ie},\quad
 v=e^{2\pi it},\qquad k=\frac{1-\omega}{1+\omega}.                 \tag{3}
\]
The cited theorem proves simple selected branches on (1), with
\[
 \Im\omega>0,\quad \Im p>0,\quad \Im v>0,\qquad
 0<\Re u_c<\Re e<1-a,\quad0<\Re t<1-a.                           \tag{4}
\]
All original primitive arguments remain regular. In particular,
the continued conditional equation is \(Q_t=0\), rather than
merely \(e^{Q_t}=1\).

The exact cap parametrization and incoming multipliers are
\[
 \begin{gathered}
 p=1-2k+2k^2,\qquad
 X=4k^2+3-\frac2{1-k}
       =1-\frac{2kp}{1-k},\\
 e^{\mathcal T_a}=(k/p)^2,\qquad
 e^{\Theta_a}=\frac{v-X}{1-X},\qquad
 \boxed{\ e^{\mathcal P_a}=(k/p)^2\frac{v-X}{1-X}\ }.
 \end{gathered}                                                     \tag{5}
\]
The original chirps in (2) are included in (5). The divisors
\(1+\omega,1-k,k,p,1-X\) are nonzero on (1), as follows from
the same theorem and its parametrization. No arbitrary root of
the multiplier polynomial is substituted for the selected branch.

## 2. A sharper radius bound for the conditional critical point

**Lemma 1.** The selected conditional root satisfies
\[
                         |v(a,y)|<2
             \qquad(a\in\mathcal A,\ y\in\mathcal Y).             \tag{6}
\]

*Proof.* On the original regular strips,
\[
 Q_t=\Log(1-X/v)+\Log(1-Y/v)
                         -3\Log(1-1/v)+2\pi ia.                 \tag{7}
\]
These are the continued original logarithms. If \(|v|\ge2\),
the arguments inside each \(1-z\) lie in the unit disk, so
these logarithms have their principal imaginary parts. More
explicitly, \(g'(z)=\Log(1-e^{-2\pi iz})\) is already principal
on \(0<\Re z<1\), and (4) places all three arguments there.

For \(0\le R<1\), the disk centered at \(1\) with radius \(R\)
gives the elementary bound
\[
                |\Arg(1-z)|\le\arcsin R\quad(|z|\le R).         \tag{8}
\]
The outgoing rectangle has \(|Y|<8/7\), by the complete
conditional theorem. Thus under \(|v|\ge2\), the three radii
in (7) are at most \(1/2,4/7,1/2\), respectively. It follows that
\[
 \Im Q_t
 \ge 2\pi a-4\arcsin(1/2)-\arcsin(4/7)
 >\pi-\frac{2\pi}{3}-\frac{\pi}{5}
 =\frac{2\pi}{15}>0.                                             \tag{9}
\]
Here \(\arcsin(4/7)<\pi/5\) has an elementary rational witness:
\[
 \sin(\pi/5)>\sin(5/8)
 \ge \frac58-\frac{(5/8)^3}{6}
 =\frac{1795}{3072}>\frac47,
\]
using \(\pi>25/8\). The last comparison is \(12565>12288\).
Equation (9) contradicts the original zero lift \(Q_t=0\).
This proves (6). \(\square\)

## 3. A barrier for the selected cap branch

Write
\[
 k=r-i\tau,\qquad \tau>0,\qquad u=|k|^2,\qquad
                         D=|1-k|^2=1-2r+u.                     \tag{10}
\]
The sign of \(\tau\) follows directly from \(\Im\omega>0\).
Here \(u\) is a nonnegative modulus variable, not the endpoint
coordinate \(u_c\).

**Lemma 2.** Along the selected cap branch on \(\mathcal A\),
\[
                              r<\frac15.                        \tag{11}
\]

*Proof.* At the half face, the exact enclosure in
[the complete cap theorem, Section 2](research_mixed_half_face_complete_cap_packet.md)
gives \(|\omega|^2>2/3\) and \(\Re\omega>3/28\). Therefore
\[
 r=\frac{1-|\omega|^2}{|1+\omega|^2}
 <\frac{1/3}{\,1+2/3+3/14\,}
 =\frac{14}{79}<\frac15.                                        \tag{12}
\]
If the numerator were nonpositive, the required upper bound
would be immediate; the displayed estimate covers the positive
case.

The unit-modulus condition for \(X\) in (5) gives exactly
\[
                   \Re\{kp(1-\bar k)\}=u|p|^2.                 \tag{13}
\]
Direct expansion yields
\[
 \begin{split}
 |p|^2&=1-4r+8r^2-8ru+4u^2,\\
 \Re\{kp(1-\bar k)\}
   &=r(1-4r+8r^2)+u(1-4r-4r^2)+2u^2 .
 \end{split}                                                       \tag{14}
\]
Equivalently,
\[
 4u^3-(8r+2)u^2+12r^2u-8r^3+4r^2-r=0.                          \tag{15}
\]

Suppose the continued branch first reaches \(r=1/5\).
Equation (15) then becomes
\[
                         500u^3-450u^2+60u-13=0.                \tag{16}
\]
For \(0\le u\le13/20\), its left side is bounded above by
\[
                         -125u^2+60u-13<0.                      \tag{17}
\]
The inequality follows from \(500u-450\le-125\); the last
quadratic is strictly negative because
\(60^2-4\cdot125\cdot13<0\). Thus (16) forces \(u>13/20\), and
\[
                         D=3/5+u>5/4.                          \tag{18}
\]
But the exact imaginary part of the rational expression for
\(X\) in (5) is
\[
                         \Im X=2\tau(1/D-4r).                  \tag{19}
\]
At \(r=1/5\), (18) makes this strictly negative. On the incoming
arc one has \(\Im X\ge0\), with equality only at its half-face
endpoint. This contradiction rules out a first crossing.
Continuity from (12) proves (11). \(\square\)

**Lemma 3.** The selected cap multiplier obeys
\[
                     |e^{\mathcal T_a}|=|k/p|^2<\frac12
                                  \qquad(a\in\mathcal A).        \tag{20}
\]

*Proof.* If \(r\le0\), the first line of (14) gives
\[
                 |p|^2\ge1+4u^2>2u.
\]
Indeed \(4u^2-2u+1>0\). If \(0<r<1/5\), use (13)--(14):
\[
 u|p|^2
 =r(1-4r+8r^2)+u(1-4r-4r^2)+2u^2>2u^2.                        \tag{21}
\]
The first term is positive, while
\(1-4r-4r^2>1/25>0\). Since \(u>0\), this again gives
\(|p|^2>2u\), proving (20).

The argument uses the selected initial value and its continuous
branch. It does not assert that every root of the eliminated
cap-multiplier polynomial lies in the same disk. \(\square\)

## 4. Uniform phase decrease and its precise scope

**Theorem.** For the original continued critical action at
complete ordinary color,
\[
 \boxed{\quad
 |e^{\mathcal P_a(a,-2,y)}|<\frac{15}{16},\qquad
 \Re\mathcal P_a(a,-2,y)<\log(15/16)<-\frac1{16}
 \quad}                                                         \tag{22}
\]
uniformly for \(a\in\mathcal A\), \(y\in\mathcal Y\).

*Proof.* On the incoming arc,
\[
 |1-X|=2\sin(\pi a)
 \ge2\sin(3\pi/10)=\frac{1+\sqrt5}{2}>\frac85.                    \tag{23}
\]
Lemma 1 gives \(|v-X|<3\). Combining (5), (20) and (23) proves
\[
                 |e^{\mathcal P_a}|<
                   \frac12\,\frac3{8/5}=\frac{15}{16}.
\]
Taking logarithms proves (22), including
\(\log(1-1/16)<-1/16\). \(\square\)

In particular, for fixed \(y\in\mathcal Y\) and
\(1/2\le a_1<a_2\le7/10\), the original absolute action satisfies
\[
 \Re\mathcal P(a_2,-2,y)-\Re\mathcal P(a_1,-2,y)
 \le(a_2-a_1)\log(15/16)
 <-\frac{a_2-a_1}{16}.                                          \tag{24}
\]
The analytic branch and no-wall theorem already gives a fixed
complex neighborhood in \((a,y)\) of the compact set (1).
By continuity and compactness, shrinking that neighborhood
preserves, for example, \(\Re\mathcal P_a<-1/32\), still at
ordinary color \(-2\).

These are statements about the original critical phase, with
its actual additive constant and logarithmic lift. Near the
half face, the complete finite product and its short incoming
integral are already controlled by
[the local incoming-source theorem](research_mixed_half_face_incoming_transport.md).
No new whole-product estimate along the entire arc is deduced
here. The explicit continued saddle outside the old endpoint
rectangle, recorded in Section 4 of the general transport
theorem, still requires its own complete finite-source contour
and bounds. The present result removes the intervening
phase-sign obstruction; it does not remove those source
obligations or establish a comparison with the next filled
action.

