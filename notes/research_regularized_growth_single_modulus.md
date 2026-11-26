# Piecewise harmonic growth when the characteristic roots have one modulus

Research deduction, 6 November 2026.

The [whole-period contact theorem](research_regularized_period_growth_characteristics.md),
Section 3, has a regularity consequence which does not assume a
\(C^1\) envelope. It applies on a positive disk where the simple
nonzero characteristic roots have a common modulus. A single
simple root is the first case. Subharmonicity then controls the
otherwise unbounded integer logarithmic lifts.

The conclusion below is local and conditional on this characteristic
root configuration. No claim is made that every knot operator, or
its geometric component, has this configuration.

## 1. The envelope and the branch assumption

Let \(z\) denote the local logarithmic meridian coordinate. Let
\(U\) be the joint upper-regularized envelope of the actual
regularized periods, as in equation (14) of the cited note.
Work on an open disk \(D\) on which
\[
                         0<U(z)<\infty .
 \tag{1}
\]
The whole-source upper bound makes \(U\) locally bounded above.
Assume the stable characteristic has constant degree and simple
nonzero roots \(L_1,\ldots,L_k\) on \(D\), and
\[
                         |L_j(z)|=|L_1(z)|
                    \qquad(z\in D,\ 1\le j\le k).
 \tag{2}
\]
Shrink the disk if necessary to choose holomorphic logarithms.
Since \(L_j/L_1\) is holomorphic with constant modulus one, it
is constant. Thus real constants \(a_j\), taken modulo integers,
can be chosen so that
\[
 L_j=e^{2\pi i a_j}L_1,\qquad
 p_1=\frac{\Log L_1}{2\pi i},\qquad
 H=\Re\int^z p_1(\zeta)\,d\zeta,\qquad
 \Lambda=\bigcup_{j=1}^k(a_j+\mathbb Z).
 \tag{3}
\]
The set \(\Lambda\subset\mathbb R\) is locally finite.

The upper-contact theorem says that at every first-order upper
contact of \(U\), its complex slope is \(p_1(z)+\lambda\) for
some \(\lambda\in\Lambda\). Hence \(v=U-H\) has only **real**
upper-contact slopes. The integer in (3) has not been assumed
bounded or constant.

The envelope \(U\) is subharmonic on \(D\). Here that standard
envelope fact can be checked directly. The upper regularizations
of the tail suprema
\[
 \left(\sup_{N\ge m}N^{-1}\log|R_N(e^z)|\right)^*
 \tag{4}
\]
are subharmonic, by the submean inequality and their common local
upper bound. They decrease to the joint envelope: both
regularization and the tail limit are infima over their respective
neighborhood and tail parameters. On a compact subdisk the tail
envelopes are bounded above and bounded below by \(U>0\).
Bounded convergence passes the submean inequality to \(U\);
the decreasing limit is upper semicontinuous. Therefore
\(v=U-H\) is subharmonic as well. Positivity of the envelope on
a disk is an explicit hypothesis, not inferred from its value
at one point.

## 2. A directional upper-contact lemma

Let \(v\) be a finite, locally bounded, upper-semicontinuous
function on a rectangle in \(\mathbb R^2\). Suppose every
smooth test function touching it from above at an interior point
has zero derivative in the second coordinate. Then
\[
                            v(x,y)=f(x).
 \tag{5}
\]
Here local boundedness means bounds on both sides; it holds for
\(U-H\) on compact subsets of (1).

To prove (5), suppose first that
\(v(x_0,y_2)>v(x_0,y_1)\) with \(y_2>y_1\).
Choose \(y_3>y_2\) still inside the rectangle, a small
\(\lambda>0\), and then a small \(\epsilon>0\), so that
\[
 v(x_0,y_2)-\lambda y_2-\frac{\epsilon}{y_3-y_2}
 >
 v(x_0,y_1)-\lambda y_1-\frac{\epsilon}{y_3-y_1}.
 \tag{6}
\]
Upper semicontinuity at \((x_0,y_1)\) bounds the bottom edge near
\(x_0\). On a fixed small horizontal interval about \(x_0\), choose
\(A\) large enough that
\[
        v(x,y)-\lambda y-\frac{\epsilon}{y_3-y}
                                      -A(x-x_0)^2
 \tag{7}
\]
has no maximum on either vertical side or on the bottom edge.
For the bottom edge outside a smaller neighborhood of \(x_0\),
the fixed positive quadratic penalty and local upper boundedness
give this choice of \(A\). The barrier tends uniformly to
\(-\infty\) as \(y\uparrow y_3\), so a maximum is attained in
the interior. Its smooth upper test has second-coordinate
derivative
\(\lambda+\epsilon/(y_3-y)^2>0\), a contradiction.
Thus \(v(x_0,y)\) is nonincreasing in \(y\). Reversing \(y\)
gives the opposite inequality, proving (5).

Apply this lemma to \(U-H\). A smooth upper test gives a
first-order upper contact. Its complex slope is real by (3),
so its second-coordinate derivative is zero. Consequently
\[
                        U(z)=H(z)+f(\Re z)
 \tag{8}
\]
on every sufficiently small rectangle in \(D\).

## 3. Convexity bounds the integer lifts

Since \(v\) is subharmonic and independent of \(y\),
its distributional Laplacian is \(f''(x)\). It is nonnegative,
so \(f\) is convex. One may see the pointwise statement by
mollifying in \(x\): the mollifications are convex, and the
subharmonic representative agrees with their convex limit.

At every differentiability point of this finite convex function,
\(f'\) is an upper-contact slope in (8). Hence
\[
                          f'(x)\in\Lambda
                  \quad\hbox{for almost every }x .
 \tag{9}
\]
On compact intervals \(I\Subset J\) in its domain, convexity
bounds every interior one-sided slope by
\[
             |f'_\pm(x)|\le
             \frac{\operatorname{osc}_J f}
                  {\operatorname{dist}(I,\partial J)}
                         \qquad(x\in I).
 \tag{10}
\]
Thus only finitely many elements of \(\Lambda\) can occur in
(9) on \(I\). The a.e. derivative is monotone, so it is a
finite step function there. Absolute continuity of a finite
convex function on interior compact intervals now gives
\[
                f(x)=\max_{1\le r\le m}
                               \{\lambda_r x+C_r\},
             \qquad \lambda_r\in\Lambda ,
 \tag{11}
\]
after restricting to a slightly smaller interval if needed.
The affine pieces are supporting lines of the convex function.

**Theorem.** Under (1)--(2), the actual envelope is locally a
finite maximum of harmonic actions:
\[
              U(z)=\max_{1\le r\le m}
                       \{H(z)+\lambda_r\Re z+C_r\}.
 \tag{12}
\]
It is locally Lipschitz and harmonic away from finitely many
vertical interfaces in each such rectangle. All integer
logarithmic translates are controlled by (10). The constants,
active slopes and their geometric interpretation remain
undetermined.

In the one-root case, \(\Lambda=\mathbb Z\) after choosing the
initial logarithm. Thus the \(C^1\) hypothesis can be removed
completely on a positive disk in that case. It cannot be replaced
by a conclusion of one harmonic branch. For example the exact
holomorphic family
\[
 f_N(Y)=2^N(1+Y^N),\qquad
 f_N(Q_NY)=f_N(Y)
 \tag{13}
\]
has simple characteristic \(L-1\), and joint envelope
\[
                   \log2+\max(0,\Re z).
 \tag{14}
\]
It is positive and subharmonic but not \(C^1\) across
\(\Re z=0\). This is an exact difference-equation example,
not an identification with a knot period.

## 4. What is still missing with several distinct moduli

If the roots do not satisfy (2), the imaginary parts of the
allowed slopes need not coincide. The directional argument
then no longer makes \(U-H\) independent of one coordinate.
Local boundedness alone does not give the convex slope estimate
(10) by the proof above. The subsequent
[vertical regularity](research_regularized_growth_vertical_regularity.md)
and [null-support theorem](research_regularized_growth_null_riesz_support.md)
now prove continuity and area-zero Riesz support for the positive
envelope on the whole regular-root region. A locally bounded choice
among all logarithmic translates, and a finite holomorphic derivative
family near accumulating components, remain unproved in general.

There is relevant existing coverage:
[Björk, Borcea and Bøgvad, *Subharmonic Configurations and
Algebraic Cauchy Transforms of Probability Measures*, Theorem 1](https://arxiv.org/pdf/0912.4650).
Their class \(SH_0\) requires the support of the Riesz measure
to have area zero. Their finite piecewise holomorphic derivative
hypothesis then yields local piecewise harmonicity. We checked
these hypotheses in the introduction and theorem statement;
the later null-support proof supplies the first hypothesis, but
not the finite derivative-family hypothesis. That theorem is
therefore not being applied to the general meridian envelope.

Neither this limitation nor example (13) disproves local
piecewise harmonicity for a general regular characteristic.
The common-modulus theorem (12) is the proved extension here;
[two separated modulus classes](research_regularized_growth_two_moduli.md)
are handled in a separate proof.
No source computation, new asymptotic coefficient, or geometric
rate calibration is used.
