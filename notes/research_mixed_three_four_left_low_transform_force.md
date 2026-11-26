# Increasing the transform coordinate on the added left contour

Research deduction, 7 November 2026. The original terminal phase
increases with the real transform coordinate throughout the
rectangle added by a proposed left contour extension. This remains
true at both alias heights and at every original private height.
The proof keeps the incoming radius correlated with its height.
It supplies horizontal transport to the old cut \(t_R=.15\);
it does not by itself pay that old profile at a new incoming point.

## 1. Domain and the exact derivative

Let
\[
 a=x+ih,\qquad h=c(x-.1)/.12,\qquad
 -.072<c<.021,\quad .1\le x\le.22,
 \qquad \lambda=-c/.12 .
 \tag{1}
\]
Keep
\[
 t=u+iy,\quad .03\le u\le.15,\quad |y|\le.12,\qquad
 e\in[.27,.49]+i[-.055,.04].
 \tag{2}
\]
The complete terminal phase, with its original endpoint coefficient,
is
\[
 \Phi(a;t,e)=S(e)+g(a+t)+g(e+t)-3g(t)-g(e)-g(a)
       -\frac{\pi i}{2}(e-e^2)+2\pi iat.
 \tag{3}
\]
The primitive has \(g'(z)=\log(1-e^{-2\pi iz})\) on its
original regular strip.
All arguments in (1)--(3) are regular; in particular their positive
real parts stay uniformly away from zero and one.

**Theorem 1.** On (1)--(2),
\[
                         \partial_u\Re\Phi>1/2000.
 \tag{4}
\]
Consequently any horizontal main, private-face or penalized alias
profile in this added rectangle is bounded by its value at
\(u=.15\), with the same incoming coordinate and the same heights.

Put
\[
 R=e^{-2\pi h}=e^{2\pi\lambda(x-.1)},\quad
 r=e^{2\pi y},\quad k=e^{2\pi\Im e}.
\]
The chirp in (3) gives exactly
\[
 e^{2\partial_u\Re\Phi}
 =\frac{|R-r e^{-2\pi i(x+u)}|^2
         |1-kr e^{-2\pi i(\Re e+u)}|^2}
         {|1-r e^{-2\pi iu}|^6}.
 \tag{5}
\]
Throughout the proof,
\[
 R>4/5,\qquad k>7/10,\qquad
 7/15<r<32/15<15/7.
 \tag{6}
\]
The first two guards are the elementary exponential bounds in
[the right moving-cut proof](research_mixed_three_four_moving_transform_cut.md).
For the improved upper bound on \(r\), use \(.24\pi<132/175\)
and
\[
 e^z\le1+z+\frac{z^2}{2}+\frac{z^3}{6(1-z/4)}.
\]
At \(z=132/175\) this rational expression is less than \(32/15\).
Reciprocation gives \(r>15/32>7/15\).

## 2. The two smaller real intervals

First take \(.03\le u\le.08\). The angle \(x+u\) lies
strictly between \(1/8\) and \(3/8\). Completing a square in
either radius gives
\[
 |R-r e^{-2\pi i(x+u)}|^2>\tfrac12 r^2,
 \qquad
 |R-r e^{-2\pi i(x+u)}|^2>\tfrac12 R^2.
 \tag{7}
\]
Also \(\Re e+u\in[.30,.57]\), so its cosine is less than
\(-3/10\), and \(\cos(2\pi u)>7/8\).
Thus the other numerator and the squared denominator in (5)
are bounded by
\[
 B=1+\frac{49}{100}r^2+\frac{21}{50}r,\qquad
 D=1+r^2-\frac74r,
 \tag{8}
\]
from below and above, respectively.

If \(r\le1\), convexity of \(D\) on \([7/15,1]\) gives
\(D\le361/900<1/2\). Equations (6)--(8) give a ratio
in (5) greater than \(64/25\).
If \(1\le r\le15/7\), both
\(\tfrac12r^2-D\) and \(B-2D\) are concave quadratics.
Their respective endpoint values are
\[
 (1/4,\ 89/196),\qquad(141/100,\ 457/980).
\]
They are positive. Since \(D\le361/196\), the ratio in (5)
is greater than \(392/361\).

Next take \(.08\le u\le.1\).
Now \(1/6<x+u<1/3\), so the two lower bounds in (7)
hold with \(3/4\) in place of \(1/2\).
The other angle lies in \([.35,.59]\), with cosine
less than \(-7/12\), and \(\cos(2\pi u)>4/5\).
Use
\[
 B=1+\frac{49}{100}r^2+\frac{49}{60}r,\qquad
 D=1+r^2-\frac85r.
 \tag{9}
\]
For \(r\le1\), \(D\le106/225<1/2\), and the ratio in
(5) is greater than \(96/25\).
For \(1\le r\le15/7\), the concave quadratics
\(\tfrac34r^2-D\) and \(B-\tfrac94D\) have endpoint values
\[
 (7/20,\ 251/196),\qquad(211/150,\ 13/98).
\]
Since \(D\le106/49\), the ratio is greater than \(441/424\).

These guards follow from the exact values of sine and cosine at
\(\pi/5\) and the elementary Taylor bounds already used in the
right moving-cut proof. For example
\(\cos(.16\pi)>7/8\) follows from
\(\cos z\ge1-z^2/2+z^4/24-z^6/720\), evaluated at the
rational upper argument \(88/175>.16\pi\).
No phase or critical point is evaluated here.

## 3. Reduction of the remaining interval to its upper endpoint

For \(.1\le u\le.15\), put \(C(z)=\Re\cot(\pi z)\).
The original derivative gives
\[
 -\pi^{-1}\Re\Phi_{tt}=3C(t)-C(a+t)-C(e+t).
 \tag{10}
\]
Here \(C(t)>1\), as proved from the sine-plus-cosine inequality
in the right moving-cut proof.
Also
\[
 C(a+t)\le\cot(.2\pi)<3/2,\qquad
 C(e+t)\le\cot(.37\pi)<1/2.
\]
Thus the real transform derivative strictly decreases with \(u\)
on this interval. It suffices to bound it at \(u=.15\).

At that endpoint the first squared modulus in (5) increases with
\(x\) along the actual incoming taper. To see this, put
\(\theta=2\pi(x+.15)\). Differentiation gives
\[
 \frac d{dx}|R-r e^{-i\theta}|^2
 =4\pi R\{\lambda(R-r\cos\theta)+r\sin\theta\}.
 \tag{11}
\]
On this interval, \(\cos\theta\le0\),
\(\sin\theta>7/10\), and \(|\cos\theta|<7/10\).
If \(\lambda\ge0\), the braces are positive term by term.
If \(\lambda<0\), then \(R\le1\) and \(|\lambda|<7/40\);
their lower bound is
\[
 -\frac7{40}
   +r\left(\frac7{10}-\frac7{40}\frac7{10}\right)>0,
\]
using \(r>7/15\). This uses the actual radius--slope correlation.
The first modulus is therefore smallest at \(x=.1\), where
\(R=1\) and \(x+u=1/4\). Its square is \(A=1+r^2\).

At \(u=.15\), the cosine of the private angle is at most
\(-\cos(.28\pi)<-63/100\), while
\(\cos(.3\pi)>47/80\).
The numerator and denominator comparison in (5) becomes
\[
 \frac{AB}{D^3},\qquad
 A=1+r^2,\quad
 B=1+\frac{49}{100}r^2+\frac{441}{500}r,\quad
 D=1+r^2-\frac{47}{40}r.
 \tag{12}
\]
For \(r\le1\), \(A>D\), \(B>D\), and \(D\le33/40\);
the ratio is greater than \(40/33\).
For \(1\le r\le32/15\), the concave quadratics
\(A-\tfrac{91}{50}D\) and \(B-\tfrac{67}{40}D\)
have endpoint values
\[
 (997/2000,\ 23/2250),\qquad
 (7921/8000,\ 61/5000).
\]
Thus both are positive. Since \(D\le137/45\),
\[
 \frac{AB}{D^3}>
 \frac{6097}{2000D}\ge\frac{54873}{54800}.
 \tag{13}
\]

The last two trigonometric guards also have short exact witnesses.
Since \(.22\pi>.69\),
\(\sin(.22\pi)>\sin(.69)>.69-.69^3/6>63/100\).
Also \(\sqrt5<179/80\) and
\(\sin^2(\pi/5)=(5-\sqrt5)/8>2209/6400\), so
\(\sin(\pi/5)>47/80\).

Every lower ratio obtained above exceeds \(54873/54800\).
Taking logarithms in (5), with
\(\log(1+z)>z/(1+z)\), proves
\[
 \partial_u\Re\Phi>
 \frac12\log(54873/54800)>
 \frac{73}{109746}>\frac1{2000}.
\]
This completes the proof of Theorem 1.

## 4. Source interpretation and the remaining comparison

Integrating (4) at fixed \(a,e,\Im t\) gives
\[
 \Re\Phi(a;u+iy,e)
 \le\Re\Phi(a;.15+iy,e)-\frac{.15-u}{2000}.
 \tag{14}
\]
The same inequality holds after any original sampling penalty:
that penalty depends on the height, which has not changed.
It also survives multiplication by the whole first factor, since
that factor does not depend on \(t\).

Use the original exact row
\[
 e^{2\pi iNat}\Pi_N(a+t)\Pi_N(e+t)
 E_N(a)E_N(t)^3E_N(e)\Delta_N(e)^{-1}\mathcal C_N(e,w).
\]
On the added rectangle all its factorial arguments are regular,
and \(\mathcal C_N\) remains the complete ordinary endpoint
coefficient. Thus the original finite-symbol estimates and
half-grid rounding convert (14) into the same upper-rate
transport for every indicated current, with an arbitrary
prescribed rate tolerance and a polynomial prefactor.
Both parities and fixed ordinary-color derivatives remain included.

This statement compares profiles at the same incoming \(a\).
It does not identify the old profile at \(\Re t=.15\) with a
calibrated geometric rate when \(x<.22\). Nor does it give
separate height convexity on the entire added rectangle, or
transport up to the newer conditional cut \(.22\).
Those are distinct requirements for assembling a complete left
contour. The
[moving real-boundary theorem](research_mixed_three_four_left_moving_boundary.md)
supplies a calibrated boundary along \(t=x-.07\);
Theorem 1 supplies an additional horizontal estimate, not an
unproved inference from that boundary to the whole sum.
