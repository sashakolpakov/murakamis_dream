# Continuity and vertical action pieces for the actual growth envelope

Research deduction, 6 November 2026.

On a regular logarithmic meridian disk, the
[whole-period contact theorem](research_regularized_period_growth_characteristics.md)
imposes a finite set of possible vertical slopes even though its
integer logarithmic lifts are unbounded in the horizontal direction.
This gives continuity of the positive growth envelope, and a finite
action decomposition on each compact vertical interval. It does not
yet give a two-dimensional finite action decomposition.

## 1. The positive part has finite vertical test slopes

Write the logarithmic meridian as \(z=x+iy\). Let \(U\) be the joint
upper envelope of the actual regularized periods. Work on a disk
where the stable characteristic has constant degree and simple
nonzero holomorphic roots \(L_1,\ldots,L_k\). Set
\[
 V=\max(U,0),\qquad
 b_0=0,\qquad b_j(z)=\frac{\log|L_j(z)|}{2\pi}
                                \quad(1\le j\le k).
 \tag{1}
\]
The whole-source bound makes \(V\) finite and locally bounded.
It is subharmonic. Indeed take the upper regularizations of the
tail suprema of \(N^{-1}\log|R_N(e^z)|\), take their maxima with
zero, and then decrease the tail index to infinity. These functions
are subharmonic by the submean inequality and local upper boundedness.
Their decreasing limit is \(V\); it is upper semicontinuous, and
bounded convergence passes the submean inequality because the
functions lie between zero and a common local upper bound.

At a smooth upper test for \(V\), its vertical derivative belongs to
\[
                         \{b_0(z),b_1(z),\ldots,b_k(z)\}.
 \tag{2}
\]
At a point with \(V>0\), the same test touches \(U\) from above.
Its complex slope has the form
\(\Log L_j/(2\pi i)+n\), so its vertical derivative is \(b_j\).
At a point with \(V=0\), the test has a local minimum because
it lies above \(V\ge0\); its entire gradient is zero.
Thus (2) does not require a positive neighborhood in advance.

## 2. Restricting upper tests to a vertical line

Fix \(x_0\) and let \(f(y)=V(x_0,y)\). Every \(C^1\) upper test
\(\phi\) of \(f\) at \(y_0\) satisfies
\[
                     \phi'(y_0)\in\{b_j(x_0,y_0):0\le j\le k\}.
 \tag{3}
\]
This restriction is not inferred by assigning an arbitrary horizontal
derivative. Add \(\epsilon(y-y_0)^2\) to the test to make the contact
strict on a small vertical interval. On a surrounding compact rectangle,
maximize
\[
 V(x,y)-\phi(y)-\epsilon(y-y_0)^2-A(x-x_0)^2 .
 \tag{4}
\]
For large \(A\), local boundedness forces its maximizing horizontal
coordinate to approach \(x_0\). Upper semicontinuity and the strict
vertical contact force its vertical coordinate to approach \(y_0\);
the rectangle's sides are excluded for all sufficiently large \(A\).
At each maximum, (2) applies to the resulting upper test. Its
vertical derivative tends to \(\phi'(y_0)\), while the finite
continuous set in (2) tends to the set in (3). Taking a subsequence
with a fixed index proves (3). The horizontal derivative in (4)
need not be bounded.

On a compact rectangle, put \(B=\max_j\sup|b_j|\).
The directional upper-test argument in
[the single-modulus proof, Section 2](research_regularized_growth_single_modulus.md)
now gives
\[
          |V(x,y_2)-V(x,y_1)|\le B|y_2-y_1|
 \tag{5}
\]
for each vertical segment in a slightly smaller rectangle.
For completeness, if the increasing secant slope exceeded \(B\),
subtract \(\lambda y+\epsilon/(y_3-y)\), with \(\lambda>B\)
smaller than that secant slope and \(y_3>y_2\). An interior
maximum gives an upper-test derivative greater than \(B\), contrary
to (3). Reflecting \(y\) proves the opposite inequality.

There is also the integrated version
\[
 \int_{y_1}^{y_2}\min_j b_j(x,s)\,ds
 \le V(x,y_2)-V(x,y_1)
 \le\int_{y_1}^{y_2}\max_j b_j(x,s)\,ds .
 \tag{6}
\]
Subtract the \(C^1\) primitive of the maximum, respectively minimum,
and use the same directional test argument.

## 3. Subharmonicity supplies full continuity

Choose a smooth nonnegative one-dimensional mollifier \(\rho\)
supported in \([-1,1]\), with integral one, and mollify only vertically:
\[
 V_\epsilon(x,y)=\int\rho_\epsilon(t)V(x,y-t)\,dt .
 \tag{7}
\]
On interior rectangles, (5) gives the pointwise uniform bound
\[
              |V_\epsilon-V|\le B\epsilon .
 \tag{8}
\]
The function \(V_\epsilon\) is upper semicontinuous by the reverse
Fatou inequality, locally bounded, smooth vertically and subharmonic.
Since \(\int\rho_\epsilon''=0\), subtracting \(V(x,y)\) inside
the second derivative integral gives
\[
 |(V_\epsilon)_{yy}|
 \le B\int|\rho_\epsilon''(t)|\,|t|\,dt
 \le \frac{C_\rho B}{\epsilon},\qquad
 (V_\epsilon)_{xx}\ge-\frac{C_\rho B}{\epsilon}
                          \quad\hbox{in distributions}.
 \tag{9}
\]
The second inequality uses \(\Delta V_\epsilon\ge0\).

Here the pointwise representative matters. Mollify \(V_\epsilon\)
in both real coordinates with a nonnegative smooth radial kernel of
radius \(\delta\). Inequality (9) passes to the smooth functions.
After adding \(C_\rho Bx^2/(2\epsilon)\), they are convex in \(x\).
Their local oscillation is uniformly bounded, and (5) is preserved.
Interior chord bounds for these convex functions therefore give
horizontal Lipschitz bounds independent of \(\delta\), with
\(\epsilon\) fixed. Radial mollifications of the subharmonic
representative converge to its pointwise value: the submean inequality
gives the lower bound, and upper semicontinuity gives the reverse
limsup. Thus \(V_\epsilon\) itself is continuous. Equation (8)
makes \(V\) a uniform limit of continuous functions, so
\[
                              V\ \hbox{is continuous}.
 \tag{10}
\]
In particular the positive-growth locus is open, and \(U=V\) is
continuous there.

One can retain a quantitative modulus. In the horizontal chord bound
take radius \(\sqrt\epsilon\), inside the fixed larger rectangle.
Uniform boundedness and (9) give
\(\operatorname{Lip}_x(V_\epsilon)\le C\epsilon^{-1/2}\).
Then (8), with \(\epsilon=|h|^{2/3}\), yields
\[
 |V(x+h,y)-V(x,y)|\le C'|h|^{2/3}
 \tag{11}
\]
for small \(h\) on every compact interior rectangle. This is an
upper regularity estimate, not a horizontal slope bound.
When \(B=0\), the single-direction argument instead gives vertical
independence and local horizontal convexity directly.

## 4. Each vertical slice has finitely many analytic action pieces

On a fixed vertical line, the functions \(b_j(x_0,y)\) are real
analytic. On a compact interval, identify those that coincide
identically, and split at the finitely many zeros of all remaining
pairwise differences. On every resulting open interval they have
a strict fixed order, written
\[
                             \beta_1(y)<\cdots<\beta_s(y).
 \tag{12}
\]
The Lipschitz function \(f(y)=V(x_0,y)\) is differentiable almost
everywhere. At each differentiability point,
\[
                          f'(y)\in\{\beta_1(y),\ldots,\beta_s(y)\}.
 \tag{13}
\]
Indeed a first-order expansion can be majorized by a \(C^1\)
upper test with the same derivative: dominate its \(o(|h|)\)
remainder by the integral of a continuous modulus tending to zero.
Then apply (3).

The branch index in (13) is nondecreasing on each ordered interval.
Suppose instead that at two differentiability points \(y_1<y_2\)
the first index exceeds the second. Choose an intervening gap and
let \(g'\) be the midpoint of its two bounding analytic branches.
Then \((f-g)'(y_1)>0\) and \((f-g)'(y_2)<0\). The continuous
function \(f-g\) attains a maximum in the interior of
\([y_1,y_2]\), since neither endpoint can maximize it. There
\(g+\mathrm{constant}\) is an upper test whose derivative lies
strictly in the gap, contradicting (3).

There are consequently at most \(s\) derivative branches in order
on this interval. Absolute continuity gives a finite analytic
primitive decomposition of \(f\). Across a crossing point of
the \(\beta_j\), a downward derivative jump is also impossible:
every slope strictly between the right and left derivatives would
be an upper-contact slope, whereas the allowed set is finite.
Only upward jumps can occur.

In particular, with a constant uniform on the surrounding compact
rectangle,
\[
             f''\ge-C\,dy,\qquad
             C=\max_j\sup|\partial_y b_j| .
 \tag{14}
\]
The ordinary second derivative on each analytic piece is at least
\(-C\), and all jump masses are nonnegative. Equivalently every
vertical slice is semiconvex with this uniform constant.
The number of pieces is asserted finite for each fixed compact
slice; no uniform count in the horizontal parameter is needed here.

For \(j\ge1\), \(b_j=\partial_y H_j\), where
\[
                  H_j(z)=\Re\int^z\frac{\Log L_j(\zeta)}
                                             {2\pi i}\,d\zeta .
 \tag{15}
\]
Thus the slice pieces are restrictions of \(H_j\) plus real constants;
the branch \(b_0=0\) gives constant pieces. Their constants and
switching locations may depend on the horizontal coordinate.
No regularity or constancy of that dependence is inferred.

## 5. What this settles and what it does not

The contact condition now proves that the actual positive envelope
is continuous, locally Lipschitz vertically, and has finite analytic
vertical pieces with a uniform semiconvexity bound. This uses the
finite analytic choices in (2), not merely a bounded vertical derivative.
In particular it makes every finite positive point an interior point
of the positive locus. The
[single/common-modulus theorem](research_regularized_growth_single_modulus.md)
therefore applies near every such point when its root hypothesis holds.

For roots of different moduli, (14) and the slice constants in
(15) do not yet bound horizontal derivatives or the integer
logarithmic lifts. The function \(-\Re(z\Log z)\), continued
continuously over its principal cut, illustrates why vertical
Lipschitz continuity and subharmonicity alone would not suffice:
its horizontal derivative has a logarithmic singularity.
Our finite analytic vertical-branch condition is stronger, but
a two-dimensional finite branch conclusion has not been proved here.
No geometric rate, nonzero source coefficient, or finite-exception
theorem is claimed.
