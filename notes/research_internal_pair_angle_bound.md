# The two selected angles of a positive internal pair

Research proof, 3 November 2026. Frozen manuscripts are unchanged.

Consider two consecutive selected vertices, with one complete outside
endpoint attached to each of them. This note proves that both selected
angles have real part less than \(\pi/2\), throughout the charge cube,
when both crossing powers are integers at least three. The proof uses
the coupled period equations. Separate height bounds would not imply
this conclusion.

The result concerns geometry. It does not assert an asymptotic for a
complete-end kernel at a complex selected angle, or a nonzero
coefficient in the finite two-vertex source.

## 1. The family and the first possible boundary point

Let the powers be \(n,p\in\mathbb Z_{\ge3}\), and let the charges belong
to \([0,1]^2\). The
[fractional-charge theorem](research_positive_path_fractional_charge_cube.md)
gives the continuous positive geometric family. At an active vertex
write its angle as
\[
 t=a-iH,\qquad 0<a<\pi,\quad 0<H<23/20.
 \tag{1}
\]
At a zero-charge or complete endpoint the angle is zero. The bounds
we need from the
[maximum-phase theorem](research_geometric_phase_maximum_principle.md)
are
\[
 \cosh H<7/4,\qquad
       a<\frac{9\pi}{4n}\chi .
 \tag{2}
\]
The original return from this vertex to a neighbor of angle \(u\) is
\[
 r(t,u)=\operatorname{asinh}\bigl(\tan(t/2)\cos(u/2)\bigr)=k+ig.
 \tag{3}
\]
Its branch has \(k>0\) and \(-\pi/2<g<\pi/2\) when the first vertex is
active. There are two incidences, one to a complete endpoint. Their
returns satisfy
\[
 k_0+k_1=\frac{nH}{2},\qquad
 g_0+g_1=\frac{na}{2}-\pi\chi .
 \tag{4}
\]

**Theorem 1.** Throughout this charge cube, both selected angles satisfy
\[
                         0\le \Re t<\pi/2.
 \tag{5}
\]

It suffices to exclude a first point with \(a=\pi/2\). Indeed, join the
complete point to any prescribed charge by the straight charge
segment. Along this segment the geometric solution is continuous. At
a first such point the other selected angle still has real part at
most \(\pi/2\). A vertex of power at least five cannot be the first
one, by (2).

At the proposed first point put
\[
 z=\tan(t/2)=\operatorname{sech}H-i\tanh H=e^{-i\omega},
 \qquad \omega=\arctan(\sinh H).
 \tag{6}
\]
Let \(C=\cos(u/2)\) for the other selected endpoint. Its real angle
is at most \(\pi/2\), and its height is less than \(23/20\). Therefore
\[
       \Re C^2\ge\frac12,\qquad
 0\le\arg C<\arctan(23/40).
 \tag{7}
\]
The first inequality follows from
\(\Re C^2=(1+\cos(\Re u)\cosh(-\Im u))/2\). For the second, use
\(\tan\arg C=\tan(\Re u/2)\tanh(-\Im u/2)\).

The complete-end return \(r_0=\operatorname{asinh}z\) has the exact
components
\[
 k_0=\operatorname{asinh}\sqrt{\operatorname{sech}H},
 \qquad
 g_0=-\arctan\bigl(\sqrt2\sinh(H/2)\bigr).
 \tag{8}
\]
These formulas follow by squaring \(\sinh(k_0+ig_0)=z\), with the
positive real and negative imaginary branches. They agree at \(H=0\)
and retain those branches for \(H>0\).

For the other return, \(\sinh r_1=zC\) implies
\[
 \tan g_1=\tanh k_1\,\tan(\arg C-\omega).
 \tag{9}
\]
Consequently \(g_1\) lies strictly between \(0\) and
\(\arg C-\omega\), unless the latter is zero, in which case \(g_1=0\).

## 2. A vertex of power four cannot reach the boundary

Suppose \(n=4\). By (2) and (8),
\[
 k_0>\operatorname{asinh}(3/4)=\log2>2/3.
 \tag{10}
\]
The real period equation gives \(2H>k_0\), hence \(H>1/3\). Since
\(\sqrt2>7/5\),
\[
 \omega+|g_0|
 >\arctan(1/3)+\arctan(7/30)
 =\arctan(51/83)>\arctan(23/40)>\arg C.
 \tag{11}
\]
If \(\arg C\le\omega\), (9) gives \(g_1\le0\). Otherwise it gives
\(g_1<\arg C-\omega<|g_0|\). In either case \(g_0+g_1<0\).
But at \(a=\pi/2\), the imaginary period equation for power four is
\(g_0+g_1=\pi(1-\chi)\ge0\). This is a contradiction.

## 3. A vertex of power three cannot reach the boundary

Suppose \(n=3\). First,
\[
                              H>1/2.
 \tag{12}
\]
Otherwise
\[
 \cosh H\,\sinh^2(3/4)
 <\frac87\left(\frac78\right)^2<1,
 \]
so \(k_0>3/4\ge3H/2\), contradicting (4). The elementary bounds used
here follow directly from the positive Taylor series:
\(\cosh(1/2)\le53/47<8/7\) and
\(\sinh(3/4)\le24/29<7/8\).

Equations (8) and (12) now give
\[
 \omega+|g_0|>
 \arctan(1/2)+\arctan(7/20)
 =\arctan(34/33)>\pi/4.
 \tag{13}
\]
Put
\[
 k_*=\frac{3H}{2}-k_0=k_1,\qquad
                  g_*=-\frac{\pi}{4}-g_0.
 \tag{14}
\]
Since \(\chi\le1\), the imaginary equation in (4) gives \(g_1\ge g_*\).
By (13), \(g_*+\omega>0\). Equation (9) also gives
\(0<g_1+\omega<\pi/2\), since both \(\omega\) and \(\arg C\) belong
to \([0,\pi/2)\), with \(\omega>0\).

For fixed \(k>0\), the correct real-square identity is
\[
 \Re\!\left[\bigl(e^{i\omega}\sinh(k+ig)\bigr)^2\right]
 =\frac12\left\{
   \cos(2\omega)\bigl(\cosh(2k)\cos(2g)-1\bigr)
      -\sin(2\omega)\sinh(2k)\sin(2g)\right\}.
 \tag{15}
\]
Its monotonicity must be checked on the actual first-quadrant
arc, rather than inferred from \(g+\omega>0\).
Write \(e^{i\omega}\sinh(k+ig)=X(g)+iY(g)\).
For \(-\pi/2<g<\pi/2\), direct differentiation gives
\[
 X'=-\tanh k\,Y-\frac{\sin\omega\cos g}{\cosh k},
 \qquad
 Y'=\tanh k\,X+\frac{\cos\omega\cos g}{\cosh k}.
 \tag{16}
\]
Thus \(X'<0\) and \(Y'>0\) wherever \(X>0\) and \(Y\ge0\).
In particular \(X^2-Y^2\) strictly decreases along that arc.
The arc is an interval in \(g\): its inequalities are
\[
 -\tan\omega\,\tanh k\le\tan g
                         <\cot\omega\,\tanh k.
\]

Put \(C_*=e^{i\omega}\sinh(k_*+ig_*)\).
The complete-return identity \(\sinh r_0=e^{-i\omega}\), together
with (8), simplifies this expression to
\[
 C_*=2\sinh H-\frac{\cosh(3H/2)}{\sqrt2}
                 +i\left(\frac{\sinh(3H/2)}{\sqrt2}-1\right).
 \tag{17}
\]
For the calculation, put \(h=H/2\) and use
\[
 e^{i\omega}\sinh r_0=1,\qquad
 e^{i\omega}\cosh r_0
       =\frac{\sqrt2(\cosh h+i\sinh h)}{\cosh H}.
\]
In the expansion of
\(e^{i\omega}\sinh(3H/2-i\pi/4-r_0)\), the first product is
\[
 \frac{(\sinh(3h)-i\cosh(3h))(\cosh h+i\sinh h)}
          {\cosh(2h)}
       =2\sinh H-i.
\]
Subtracting
\((\cosh(3h)-i\sinh(3h))/\sqrt2\) gives (17). No exponentiated
period equation is substituted.

Let \(X=\sqrt2\sinh(H/2)\). Then \(0<X<1\), because
\(X^2=\cosh H-1<3/4\), and (17) gives the polynomial identity
\[
 \frac12-\Re C_*^2
   =S(X):=4X^5-4X^4+8X^3-8X^2+X+1.
 \tag{18}
\]
The polynomial is strictly positive on \([0,1]\). For an explicit
rational verification, its degree-five Bernstein coefficients on
the two indicated intervals are

| Interval for \(X\) | Bernstein coefficients |
|---|---|
| \([0,1/2]\) | \(1,\ 11/10,\ 1,\ 4/5,\ 11/20,\ 3/8\) |
| \([1/2,1]\) | \(3/8,\ 1/5,\ 1/10,\ 1/5,\ 7/10,\ 2\) |

Here the coefficients multiply
\(\binom5j y^j(1-y)^{5-j}\), after the affine change from the stated
interval to \(0\le y\le1\). Each basis function is nonnegative,
and their sum is one.

It remains to compare the actual first-quadrant point \(C\)
with \(C_*\). This requires two height ranges. Set
\[
 H_c=\frac23\operatorname{asinh}\sqrt2 .
\]
One has \(1/2<H_c<1\): use
\(\sinh(3/4)<7/8<\sqrt2<3/2<\sinh(3/2)\).
For every height under consideration, and also at \(H_c\),
the real part in (17) is positive. Indeed
\[
 \Re C_*=\frac{\sqrt{1+X^2/2}}{\sqrt2}
                           (4X-2X^2-1),
 \qquad 7/20<X<1,
\]
and the concave quadratic in parentheses is positive on
\([7/20,1]\). At \(H_c\), the upper bound \(X<1\) follows,
for example, from
\(\cosh H_c<\cosh1\le17/11<2\).

If \(H\ge H_c\), (17) also gives \(\Im C_*\ge0\).
Both \(C_*\) and the actual \(C\) therefore lie on the
first-quadrant arc for \(k=k_*\). Since \(g_1\ge g_*\),
(16) gives
\(\Re C^2\le\Re C_*^2<1/2\), by (18).

If \(H<H_c\), \(C_*\) lies below that arc, so the preceding
comparison cannot be used. The maximum of \(X(g)^2-Y(g)^2\)
on the first-quadrant arc occurs at \(Y=0\). Solving that
condition gives its value
\[
 R_0(H)=
 \frac{\sinh^2k_*(H)\cosh^2k_*(H)}
      {\sinh^2k_*(H)+\operatorname{sech}^2H}.
\]
Here \(k_*(H)=3H/2-k_0(H)>0\) at the proposed point.
It increases strictly with \(H\), since \(k_0(H)\) decreases.
The function
\[
 R(x,c)=\frac{x(1+x)}{x+c}
 \quad\text{satisfies}\quad
 \partial_xR=\frac{x^2+2cx+c}{(x+c)^2}>0,\qquad
 \partial_cR=-\frac{x(1+x)}{(x+c)^2}<0
\]
for \(x,c>0\). Thus \(R_0(H)\) increases with \(H\), on
the interval from the proposed height to \(H_c\).
At \(H_c\), \(k_*>0\) and (17) gives \(\Im C_*=0\), so
\[
 \Re C^2\le R_0(H)<R_0(H_c)
                         =\Re C_*(H_c)^2<1/2 .
\]
The final strict bound is again (18) and its positive
Bernstein coefficients. Both height ranges contradict (7).
The power-three first point is impossible as well. This
proves Theorem 1.

## 4. Scope and reproducibility

The argument uses the original two incidences at each selected
vertex, including its complete outside end. It does not apply to
an arbitrary interior vertex of a longer selected path. It also uses
the integer alternatives \(n=3\), \(n=4\), and \(n\ge5\); no assertion
for every noninteger power between three and five is made.

The bound places the two selected angles in a smaller regular
region for subsequent contour work. It does not by itself prove
\(\Re\psi(t,0)>-\Im t\), nor does it control the endpoint and alias
terms in a finite-source contour.

The exact polynomial identities, Bernstein coefficients and scalar
comparisons are checked by
[the accompanying script](../experiments/check_internal_pair_angle_bound.py):

~~~sh
python3 experiments/check_internal_pair_angle_bound.py
~~~
