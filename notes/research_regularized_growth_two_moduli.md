# Two separated modulus classes give a finite harmonic maximum

Research deduction, 6 November 2026.

The [vertical regularity theorem](research_regularized_growth_vertical_regularity.md)
can be upgraded to a two-dimensional conclusion when the regular
characteristic has at most two strictly separated modulus classes.
No \(C^1\) assumption on the envelope is needed. The proof first
constructs open single-class strips; it does not assume that a
finite decomposition on individual slices already gives open pieces.

## 1. Exact scope and notation

Let \(U\) be the joint envelope of the actual regularized meridian
period, in logarithmic coordinate \(z=x+iy\). Fix a finite positive
point in the regular-root region of the
[whole-period contact theorem](research_regularized_period_growth_characteristics.md).
The positive-part continuity theorem makes \(U\) continuous and
positive on a smaller rectangle \(R\).

Suppose all the simple nonzero characteristic roots on \(R\) lie in
two classes
\[
 L_{jr}(z)=e^{2\pi i a_{jr}}L_j(z),\qquad
 a_{jr}\in\mathbb R,\qquad j=1,2,
 \tag{1}
\]
with finitely many roots in each class. Assume, after ordering them,
\[
 b_2(z)-b_1(z)\ge\gamma>0,\qquad
                    b_j(z)=\frac{\log|L_j(z)|}{2\pi}.
 \tag{2}
\]
Roots in the same modulus class have the constant unit-phase ratios
in (1), by holomorphy. Thus this assumption includes two simple
roots of distinct moduli at the chosen point, after shrinking \(R\).
It does not include a point where two distinct modulus functions
cross. The one-class case is already covered by
[the single-modulus theorem](research_regularized_growth_single_modulus.md).

Choose holomorphic logarithms and primitives on \(R\), and put
\[
 H_j(z)=\Re\int^z\frac{\Log L_j(\zeta)}{2\pi i}\,d\zeta,\qquad
 p_j=\frac{\Log L_j}{2\pi i},\qquad
 \Lambda_j=\bigcup_r(a_{jr}+\mathbb Z).
 \tag{3}
\]
Every upper-contact slope of \(U\) lies in
\((p_1+\Lambda_1)\cup(p_2+\Lambda_2)\).
In particular its vertical derivative is \(b_1\) or \(b_2\).

By the vertical slice theorem, each fixed-\(x\) slice has at most
one switch: class 1 below, class 2 above. Either class may be absent.
The separation (2) rules out crossings of the vertical slope functions
and every downward switch.

## 2. A switch produces actual open strips

Suppose the slice at \(x_0\) switches at \(y_0\). Choose
\[
                      a<b<y_0<c<d
 \tag{4}
\]
inside \(R\), and choose \(b'\in(a,b)\), \(c'\in(c,d)\).
At \(x_0\), the increments of \(U-H_1\) across \([a,b]\)
and of \(U-H_2\) across \([c,d]\) are zero.
Continuity of \(U,H_1,H_2\) at these four endpoints gives,
for \(x\) near \(x_0\),
\[
 \begin{split}
 |(U-H_1)(x,b)-(U-H_1)(x,a)|&<\gamma(b-b'),\\
 |(U-H_2)(x,d)-(U-H_2)(x,c)|&<\gamma(c'-c).
 \end{split}
 \tag{5}
\]
If the neighboring slice switched at or below \(b'\), it would
have class 2 throughout \([b',b]\), and the first increment in
(5) would be at least \(\gamma(b-b')\). If it switched at or
above \(c'\), the second increment would be at most
\(-\gamma(c'-c)\). An entirely class-2 or entirely class-1
slice violates the respective inequality as well.

Consequently every nearby slice has its switch strictly between
\(b'\) and \(c'\). There are genuine open lower and upper strips
on which, respectively,
\[
                   U=H_1+c_1(x),\qquad U=H_2+c_2(x).
 \tag{6}
\]
The functions \(c_j\) are continuous, since they can be evaluated
at any fixed height in their strips. This is the needed open-set
conclusion; the buffer lengths in (5) prevent a switch from
approaching either strip.

## 3. The horizontal residuals are convex with discrete slopes

On each strip in (6), \(U-H_j=c_j(x)\) is subharmonic, hence
\[
                              c_j''\ge0
 \tag{7}
\]
in distributions. Thus \(c_j\) is a finite convex function.
At a differentiability point of \(c_j\), the first-order expansion
of \(H_j+c_j(x)\) is an upper contact of \(U\) at any interior
point of the strip. Its vertical derivative is \(b_j\).
By (2), the other root class is impossible. Therefore
\[
                              c_j'(x)\in\Lambda_j
                      \quad\hbox{almost everywhere}.
 \tag{8}
\]
Interior convex chord bounds control these slopes on smaller
horizontal intervals. Since \(\Lambda_j\) is locally finite,
only finitely many values occur. Monotonicity of the convex
derivative and absolute continuity give
\[
                       c_j(x)=\max_r\{\lambda_{jr}x+C_{jr}\},
                      \qquad\lambda_{jr}\in\Lambda_j ,
 \tag{9}
\]
with finitely many terms on a smaller interval.

For each such \(x\), continuity at its unique vertical switch
equates the two expressions in (6). Moreover
\[
       \partial_y\{H_2+c_2-H_1-c_1\}=b_2-b_1\ge\gamma.
 \tag{10}
\]
Their difference is negative below that switch and positive
above it. Throughout the rectangle between the strips,
\[
                     U=\max\{H_1+c_1,H_2+c_2\}.
 \tag{11}
\]
Combining (9) and (11) gives a finite maximum of harmonic functions.
The logarithmic integers are bounded by the convex chord estimates;
their boundedness was not assumed before constructing the strips.

## 4. A pure slice cannot acquire an interior switch nearby

Suppose instead that the slice through the point has only class 1
on a vertical interval \([a,d]\). Choose
\(a<a'<d'<d\). Its increment of \(U-H_1\) over \([a,d]\)
is zero. For nearby \(x\), continuity makes that increment
smaller in modulus than \(\gamma(d-d')\).
Any appearance of class 2 at or below \(d'\) would persist
upwards through \([d',d]\), contradicting this bound.
Thus the smaller rectangle with heights \([a',d']\)
has only class 1. The case of a pure class-2 slice uses the
increment of \(U-H_2\) and the lower buffer \([a,a']\).

On that smaller rectangle, the single residual \(c_j(x)\)
is convex and satisfies (8). Equations (9) and the finite
harmonic maximum conclusion follow exactly as before.
Every point of a slice is either in such a pure interval
or at its single switch, so the two arguments cover the
chosen positive point.

## 5. Conclusion and limitations

**Theorem.** At every finite positive growth point satisfying
(1)--(2), the actual envelope is locally of the form
\[
            U(z)=\max_{(j,r)\in\mathcal I}
                         \{H_j(z)+\lambda_{jr}\Re z+C_{jr}\},
       \qquad \mathcal I\ \hbox{finite},\quad
                         \lambda_{jr}\in\Lambda_j .
 \tag{12}
\]
In a pure neighborhood only one class is needed. The envelope
is therefore locally Lipschitz in both coordinates and harmonic
on its strict active-branch regions.

This theorem supplies the two-dimensional conclusion for one
modulus class or two strictly separated classes, without a
\(C^1\) premise and without discarding integer logarithmic lifts.
With three or more ordered modulus classes, a class absent from
one slice may occupy a thin intervening band on nearby slices;
the two-anchor construction above does not furnish an open
strip for that missing class. Nor does the theorem handle a
modulus-crossing point by continuity alone.

The constants, active characteristic roots and their geometric
interpretation are not determined. A finite harmonic maximum
does not establish an asymptotic coefficient or the complete
meridian value. All statements concern the already defined
whole-source envelope; there is no new source evaluation or
replacement interpolation.
