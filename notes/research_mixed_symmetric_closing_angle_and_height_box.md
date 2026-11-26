# An algebraic angle and height box for the actual symmetric closing point

Private written geometric deduction, 9 November 2026. The original
positive symmetric \(343\) closing point has middle real angle
strictly below \(\pi/2\), and height strictly below \(5/6\).
Its end cosine is the distinguished original cubic root. These
bounds do not place it inside the finite-source height \(7/10\).

No mathematical numerical evaluation, saved-value arithmetic,
import, compilation, or frozen-source edit is used.

## 1. Original equations and conclusions

Keep the actual positive unit-charge solution and its original
logarithmic returns from the
[closing-height theorem](research_mixed_symmetric_343_closing_height.md):
\[
 t_g=a-iH,\quad u_g=\beta-iK,\quad
 c=\cos(t_g/2)=p+iq,\quad C=\cos(u_g/2),
\]
\[
 \begin{split}
 \operatorname{arsinh}\tan(t_g/2)
 +\operatorname{arsinh}\{C\tan(t_g/2)\}
                 &=i(3t_g/2-\pi),\\
 \operatorname{arsinh}\{c\tan(u_g/2)\}
                 &=i(u_g-\pi/2).
 \end{split}
 \tag{1}
\]
All real angles are in \((0,\pi)\), and both depths are positive.
The adopted positive-path cosine theorems give
\[
             |c|<1,\quad |C|<1,\quad 0<q/p<1/\sqrt2.
 \tag{2}
\]
Their proofs use the original return sums, so (2) applies to this
three-vertex geometric solution without an assumption about a
quantum packet.

**Proposition.** At the actual point (1),
\[
 \boxed{\quad
 0<\beta<\pi/2,\qquad17/30<K<5/6,\qquad
 3/4<p<6/7,\qquad1/4<q<7/20,\qquad|\cos u_g|<1 .
 \quad}
 \tag{3}
\]
The end cosine is the unique root with \(\Re(2c)>3/2\) of
\[
             v^3-2iv^2-3v+2i-2C=0,\qquad v=2c .
 \tag{4}
\]
It is therefore the same original cubic sheet wherever the
phase continuation is defined over \(\Re C>1/2\).
No converse from an arbitrary root of (4) is asserted.

## 2. Excluding a middle real angle at least \(\pi/2\)

The unsquared end equation already gives
\[
 4c^3-4ic^2-3c+i=C,\qquad
 p^2>3q^2-2q+3/4\ge5/12,\qquad q>1/4 .
 \tag{5}
\]
These are exactly the conclusions proved in the closing-height
theorem; in particular the constant in the cubic is \(i\).
Taking the hyperbolic sine of the specified middle return gives
\[
 c\tan(u_g/2)=-i\cos u_g.
 \tag{6}
\]
Set \(L=\cosh K,\ S_K=\sinh K,\ B=\cos\beta\). Its exact real
and imaginary consequences are
\[
 p=S_K\left(B+\frac1{L-B}\right),\qquad
 q=\sin\beta\left(L-\frac1{L-B}\right).
 \tag{7}
\]
All denominators are positive.

Suppose \(B\le0\), and write \(x=-B\), \(r=\sin\beta=\sqrt{1-x^2}>0\).
Since \(p>0\), the numerator \(1-Lx-x^2\) below is positive:
\[
 p=\frac{S_K(1-Lx-x^2)}{L+x},\qquad
 \frac qp=\frac{r(S_K^2+Lx)}{S_K(1-Lx-x^2)}.
 \tag{8}
\]
The difference needed to compare the last ratio with \(S_K\) is
\[
 r(S_K^2+Lx)-S_K^2(1-Lx-x^2)
       =S_K^2r(1-r)+Lx(r+S_K^2)\ge0 .
 \tag{9}
\]
Thus \(q/p\ge S_K\). Also the expression for \(p\) in (7)
increases strictly with \(B\), so \(p\le S_K/L=\tanh K\)
when \(B\le0\). Equation (2) now implies \(S_K^2<1/2\) and
\[
                  p^2\le\frac{S_K^2}{1+S_K^2}<1/3.
 \tag{10}
\]
This contradicts (5). Hence \(B>0\), proving \(\beta<\pi/2\).

Consequently \(\Re C\ge1/\sqrt2>1/2\). In the real part of
(4), the expression for \(0<x=\Re v\le3/2\) is at most
\(7/16\), by the original cubic proof. Since \(p>0\), the
actual root must have \(x>3/2\). That proof gives exactly
one such root over the half-plane \(\Re C>1/2\).
This identifies the original sheet and proves \(p>3/4\).

## 3. A stronger upper height from the same equations

The middle return in (1) has real part \(K\). Since \(B>0\),
\[
 |\tan(u_g/2)|^2=\frac{L-B}{L+B}<1 .
 \tag{11}
\]
Equations (2),(6) therefore give \(|\cos u_g|<1\), as claimed.
Moreover
\[
 \sinh^2 K\le
 \left|\sinh\{K+i(\beta-\pi/2)\}\right|^2
 =|c\tan(u_g/2)|^2<1 .
 \tag{12}
\]
Thus \(L<\sqrt2\). In particular
\[
 (\Im C)^2=\frac{(L-1)(1-B)}4
             <\frac{\sqrt2-1}{4}<\frac19,
 \tag{13}
\]
where the final comparison uses \(\sqrt2<13/9\).

By (2), \(q^2<p^2/2\) and \(p^2+q^2<1\), so
\(q<1/\sqrt3<3/5\). For fixed \(p>3/4\), the imaginary
part of the cubic,
\[
 F_p(q)=(12q-4)p^2-4q^3+4q^2-3q+1,
 \tag{14}
\]
strictly increases for \(0\le q\le3/5\). Its derivative exceeds
\(15/4+8q-12q^2\), a positive concave quadratic on this interval
(its endpoint values are \(15/4\) and \(423/100\)).
At \(q=7/20\),
\[
 F_p(7/20)>\frac9{80}+\frac{537}{2000}
                  =\frac{381}{1000}>\frac13 .
 \tag{15}
\]
Since \(F_p(q)=\Im C<1/3\), equations (14)--(15) prove \(q<7/20\).

On \(1/4<q<7/20\), the concave quadratic
\(-12q^2+8q-3\) is at least \(-7/4\). The real cubic equation
and \(\Re C<1\) consequently imply
\[
                 p(4p^2-7/4)<1.
 \tag{16}
\]
The left side increases for \(p>3/4\), and at \(p=6/7\)
it is \(699/686>1\). Hence \(p<6/7\). We have obtained
\[
                       |c|^2<\frac{36}{49}+\frac{49}{400}
                                      =\frac{16801}{19600}.
 \tag{17}
\]
Finally,
\[
 \sinh(5/6)>\frac56+\frac{(5/6)^3}{6}
                    =\frac{1205}{1296},
 \qquad
 \left(\frac{1205}{1296}\right)^2>\frac{16801}{19600}.
 \tag{18}
\]
The cleared comparison is
\(28459690000>28219228416\).
Together (11)--(12) and (17)--(18) give \(K<5/6\).
The already proved \(K>17/30\) completes (3).

## 4. Exact remaining localization question

The reduction (7) is still coupled to both components of
\[
 \begin{split}
 \Re C&=p(4p^2-12q^2+8q-3),\\
 \Im C&=(12q-4)p^2-4q^3+4q^2-3q+1,\\
 (\Re C)^2&=(L+1)(1+B)/4,\qquad
 (\Im C)^2=(L-1)(1-B)/4 .
 \end{split}
 \tag{19}
\]
The roots in the last line are positive. These identities retain
the actual positive solution; solving only a squared elimination
polynomial would not retain its logarithmic lift.

The interval \(17/30<K<5/6\) still crosses \(7/10\).
Neither (3) nor (19) proves the needed upper bound \(K\le7/10\).
Thus the actual saddle is not yet placed in the enlarged finite
inner-kernel domain. No packet, contributing closing contour,
or closed-knot asymptotic is inferred.

## Source versions

- Original positive unit-charge solution:
  d3806cebb427d94b795e85c5c089592c4646b49ffc01238673f4f9d04f7f3bac.
- Cosine phase ratio, Theorem 5:
  8d95b1cff9ad7cd1fad2d36c96f1c3463b3a4aeaeebd13b5c9fe3d9f3afe01b5.
- Original cosine modulus maximum principle:
  aaaf88d30be6be6737cd27e78669f2cb42bc9d0ad98315e1104616928038d0bb.
- Exact original closing system and geometric sheet:
  ef74516ae0cc9a4d965f6a528e8f582cfbca43a06e53d017201f3c30b982955a.
- Unsquared end/middle identities and lower height:
  c12acffe796dae3ad3e7990cd302020a7ff289e75f2e5c8b997836aa826764d3.
- Distinguished cubic root on \(\Re C>1/2\):
  8a8ef3f93a4ab44724d43f7bb9b15c5f8210d4649f79d1f0d4c0ec277801f41a.
