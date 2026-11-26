# Reducing the boundary search in the pair-height estimate

Research note, 3 November 2026. This note does not assert completion of
the pair-height certificates.

The support tests in
[the pair-activation comparison](research_positive_path_pair_activation_gap.md)
bound two return maps of the form
\[
 r(c)=\operatorname{arsinh}(Ac),\qquad
 A=\tan\frac{a-iH}{2},\qquad 0<a<\pi,\quad H>0.
 \tag{1}
\]
Here \(\Re A>0\), \(\Im A<0\), and the inverse sine is continued from
the right half-plane. Write \(r=k+ig\). Every slope used by those
tests is nonpositive, and the support function is
\[
 F(c)=k(c)-s g(c)=\Re\bigl((1+is)r(c)\bigr),\qquad s\le0.
 \tag{2}
\]
There are two elementary reductions of the boundary search. Neither
requires a new estimate of the source or its leading coefficient.

## 1. The straight segments need no subdivision

**Lemma 1.** On a real segment \(0\le c\le C\), the maximum of
\(F\) occurs at an endpoint. On an imaginary segment \(c=iy\),
\(0\le y\le S\), the function \(F\) is increasing.

*Proof.* Put \(\alpha=\arg A\in(-\pi/2,0)\). Along the real
segment,
\[
 r'(x)=\frac{A}{\sqrt{1+A^2x^2}},\qquad
 \delta(x)=\arg r'(x)
       =\alpha-\frac12\arg(1+A^2x^2).
 \tag{3}
\]
The square root is the continuation from \(x=0\). Since
\(\Im A^2<0\), the argument in (3) decreases continuously from
zero towards \(2\alpha\). More explicitly,
\[
 \delta'(x)=
       -\frac{x\,\Im A^2}{|1+A^2x^2|^2}>0\quad(x>0).
 \tag{4}
\]
Thus \(\delta\) increases from \(\alpha\) towards zero. The sign of
the real derivative of \(F\) is the sign of
\(\cos(\delta+\arctan s)\). Its argument belongs to \((-\pi,0)\)
and increases with \(x\). The cosine increases on that interval.
The derivative can therefore change sign only from negative to
positive. There is no interior maximum.

On the imaginary segment replace \(A\) by \(iA\), whose argument
belongs to \((0,\pi/2)\). The argument of
\[
 \frac{iA}{\sqrt{1+(iA)^2y^2}}
 \tag{5}
\]
decreases towards zero while remaining in \((0,\pi/2)\).
After adding \(\arctan s\in(-\pi/2,0]\), its argument remains
strictly between \(-\pi/2\) and \(\pi/2\). The real derivative
of \(F(iy)\) is positive. \(\square\)

For the closed quarter ellipse
\[
 c=C\cos\theta+iS\sin\theta,\qquad
 0\le\theta\le\frac\pi2,\qquad
 C=\cosh(b/2),\quad S=\sinh(b/2),\quad b>0,
 \tag{6}
\]
the harmonic maximum principle and Lemma 1 imply that the maximum
over the whole domain occurs on the curved arc. Both real-axis
endpoints are accounted for: \(C\) belongs to the arc, and
\(F(iS)>F(0)=0\).

For the smaller domain imposed by
\(\sinh h\le\sqrt3\sin\beta\), the bottom segment is \(0\le c\le1\).
Its endpoints already belong to the two curved boundary pieces.
Thus this bottom segment also needs no subdivision.

These statements extend to \(a=0,\pi\) by continuity from
\(0<a<\pi\). At those endpoints the inverse sine must retain
its right-half-plane limit; a library's value on the cut need
not equal that limit.

## 2. There are at most four stationary candidates on an ellipse arc

**Lemma 2.** Under (1), with \(b>0\) and a fixed real slope \(s\),
every interior stationary point of (2) on (6) is obtained from
a positive real root of the nonzero polynomial
\[
 \begin{split}
 P(q)=\Im\Bigl[
 &(1+is)^2 A^2(-Cq+iS)^2\\
 &\qquad\cdot
   \overline{(1+q^2)+A^2(C+iSq)^2}
 \Bigr].
 \end{split}
 \tag{7}
\]
This polynomial has degree at most four. A positive root is an
actual stationary point precisely when
\[
 \Re\frac{(1+is)^2 A^2(-Cq+iS)^2}
              {(1+q^2)+A^2(C+iSq)^2}<0,
 \qquad \theta=\arctan q.
 \tag{8}
\]
Consequently the support maximum can be found from the two arc
endpoints and at most four interior candidates.

*Proof.* Differentiation in \(\theta\) gives
\[
 \left((1+is)\frac{d r}{d\theta}\right)^2
 =\frac{(1+is)^2 A^2(-Cq+iS)^2}
              {(1+q^2)+A^2(C+iSq)^2}.
 \tag{9}
\]
Neither numerator nor denominator vanishes on the interior arc.
The derivative of \(F\) vanishes exactly when the unsquared
quantity is purely imaginary. Equivalently (9) is negative real.
Multiplication by the squared modulus of the denominator gives
(7) and (8).

For completeness, let \(P_j\) denote the coefficient of \(q^j\).
The constant and leading coefficients satisfy
\[
 \frac{P_4}{C^2}+\frac{P_0}{S^2}
       =-2s\,|A|^4(C^2+S^2).
 \tag{10}
\]
Thus the polynomial cannot vanish identically if \(s\ne0\).
If \(s=0\), then \(P_4=C^2\Im A^2<0\), so it is again
nonzero. \(\square\)

Equation (7) is a reduction for each fixed parameter pair
\((a,H)\), not an interval certificate on a rectangle of such
pairs. A replacement checker would still need to isolate all
roots uniformly, or enclose their possible locations together
with the endpoints. Values sampled at the central parameters
would not suffice.

## 3. A stable return formula near the complete point

The distance formula used by the current certificate is valid
at every required branch limit. Near \(z=Ac=0\), however, it
first subtracts quantities near one before taking an inverse
hyperbolic cosine. A rationalized formula avoids that loss.

Write \(z=x+iy\), \(x\ge0\), and suppose \(|z|^2<1\). Set
\[
 B=1-x^2-y^2,\qquad
 T=\frac{2x^2}{\sqrt{B^2+4x^2}+B}.
 \tag{11}
\]
Then the required right-half-plane branch satisfies
\[
 k=\operatorname{arsinh}\sqrt T,\qquad
 g=\arcsin\frac{y}{\sqrt{1+T}}.
 \tag{12}
\]
Indeed \(T=\sinh^2k\) is the nonnegative solution of
\(T^2+BT-x^2=0\); (11) is its rationalized expression.
The identity \(y=\cosh k\sin g\), with
\(-\pi/2\le g\le\pi/2\), gives (12). This proof also covers
\(x=0\) under the stated strict bound \(|z|<1\).

For interval evaluation one can evaluate
\(\sqrt T=\sqrt2\,x/\sqrt{\sqrt{B^2+4x^2}+B}\) directly.
The denominator is bounded away from zero on every compact
subdisk of \(|z|<1\). This is an optional enclosure improvement,
not a change of branch or of the mathematical support test.

The separate
[small-height proof](research_pair_activation_small_height.md#4-extending-the-height-interval-by-the-exact-period-equation)
already covers \(H\le3/100\). A future author run could therefore
start its scaled support coverage at \(3/100\), use only the
curved boundaries from Section 1, and use (11) near small returns.
The existing running certificates have not been changed, and
their acceptance still requires full coverage and replay.

## 4. The maximizing vertex also obeys the sector bound

The [proved tangent-sector estimate](research_positive_path_fractional_charge_cube.md#8-a-uniform-relation-between-angle-and-height)
applies to the vertex at which the height is maximal, as well as
to its neighbors. Hence every actual candidate has
\[
 a_{\min}(H)<a<\pi-a_{\min}(H),\qquad
 a_{\min}(H)=\arcsin\frac{\sinh H}{\sqrt3}.
 \tag{13}
\]
The current certificates cover the larger angle interval
\([0,\pi]\). A future support test may instead parameterize its
angle by
\[
 a=a_{\min}(H)+
       \bigl(\pi-2a_{\min}(H)\bigr)\xi,\qquad 0\le\xi\le1.
 \tag{14}
\]
This restriction is valid for both the scaled and the affine
height comparisons. It is a necessary condition already proved
for the actual geometric solution.

There is also a useful branch margin on the ellipse arcs.
For \(H\ge3/100\), and either cap \(b\ge H\), equations (1),
(6), and (13) imply
\[
 \begin{split}
 \Re A&\ge\frac{\tanh(H/2)}{\sqrt3},&
 -\Im A&\ge\tanh(H/2),\\
 \Re(Ac)&\ge
 \min\!\left\{
 \frac{\tanh(H/2)}{\sqrt3},
 \tanh(H/2)\sinh(H/2)
 \right\}>\frac1{5000}.
 \end{split}
 \tag{15}
\]
For the second line use \(\cos\theta+\sin\theta\ge1\).
For its last bound it is enough to use \(\sqrt3<2\),
\(\sinh x\ge x\), and
\(\tanh x\ge x-x^3/3\) at \(x=3/200\).
The last inequality follows by differentiating:
\((\tanh x-x+x^3/3)'=x^2-\tanh^2x\ge0\).
Both expressions in the minimum increase with \(H\).

Thus, after (13) and the small-height reduction, the scaled
arc search stays a fixed distance inside the right half-plane.
Direct complex inverse-sine enclosures may then be used on
rectangles retaining this positive real-part margin. The
distance formulas remain available for the other boundary
pieces and their limiting endpoints.
