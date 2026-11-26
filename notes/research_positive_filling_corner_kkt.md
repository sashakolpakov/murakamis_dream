# Corner conditions and an interior criterion for the filling minimum

Research note, 2 November 2026.

The convex filling functional can have a corner minimum even when all
selected powers are nonzero integers. This note gives its complete
corner optimality conditions, an explicit example with powers \(2,-2\),
and a general sufficient condition for an interior minimum. These are
statements about the original positive geometric chart. They do not
assert a quantum source asymptotic or nonhyperbolicity when that chart
degenerates.

We use the coordinates and normalization of
[the convex filling variation](research_positive_filling_convex_variation.md).
For clarity, its one-square energy has gradient
\[
 E_A=x=\tfrac12\operatorname{arsinh}(\tan(2A)\cos(2y)),\qquad
 E_y=B=\tfrac12\operatorname{arsinh}(\tan(2y)\cos(2A)),
 \quad |A|,|y|<\pi/4.                                    \tag{1}
\]
The energy is strictly convex, is zero at the origin, and extends
continuously to the closed square. In this note it is assigned the
value \(+\infty\) outside that square.

## 1. The exact corner subdifferential

A vector \(p\) is a subgradient at \(c\) when
\(E(z)\ge E(c)+p\cdot(z-c)\) for every \(z\). At an interior point
there is only the gradient (1). At an open side there is no finite
subgradient: the inward directional derivative is \(-\infty\).

**Proposition 1.** At
\(c=(\epsilon_A\pi/4,\epsilon_y\pi/4)\), put
\(U=\epsilon_Ap_A\), \(V=\epsilon_yp_y\). Then
\[
 p\in\partial E(c)
 \quad\Longleftrightarrow\quad
 U>0,\quad V>0,\quad \sinh(2U)\sinh(2V)\ge1.               \tag{2}
\]
In the positive variables \(X=e^{2U}\), \(Y=e^{2V}\), the same
condition is algebraic:
\[
          X>1,\quad Y>1,\quad
             (X^2-1)(Y^2-1)\ge4XY.                       \tag{3}
\]

**Proof.** An inward direction has the form
\((-\epsilon_Aa,-\epsilon_yb)\), \(a,b\ge0\). Directly from (1),
its directional derivative is \(-H(a,b)\), where
\[
 H(a,b)=\tfrac12\{a\operatorname{arsinh}(b/a)
                   +b\operatorname{arsinh}(a/b)\}.        \tag{4}
\]
The continuous value on either coordinate axis is zero. Convexity
shows that the subgradient condition is equivalent to
\[
                         Ua+Vb\ge H(a,b)\quad(a,b\ge0).
                                                               \tag{5}
\]
Indeed a subgradient bounds each directional derivative from below;
conversely a convex secant slope is at least its initial directional
derivative.

Define
\[
 v(U)=\tfrac12\operatorname{arsinh}(\operatorname{csch}(2U)),
                         \qquad U>0.
\]
It has \(v'(U)=-\operatorname{csch}(2U)\) and \(v''(U)>0\).
For \(a,b>0\), the minimum of \(Ua+bv(U)\) occurs at
\(\sinh(2U)=b/a\), and its value is exactly (4). Thus every
point above this convex curve satisfies (5). Conversely a point
strictly below the curve fails (5) for the supporting ratio at its
first coordinate. The axis tests first give \(U,V\ge0\).
Neither can be zero: for example \(H(1,b)/b\) tends to infinity
as \(b\downarrow0\), so \(U=0\) cannot satisfy (5) with finite \(V\).
This proves (2). Substituting the exponentials proves (3).
\(\square\)

Equality in (2) is the limit of actual gradients along a line
entering the corner with a fixed positive slope ratio. A strict
inequality is an additional supporting covector at the corner.
It must not be substituted into the smooth shape equations as if
it were such a gradient limit.

## 2. The complete finite graph conditions

Let \(S\) be the selected vertices, let \(B\) be their incident outside
vertices, and include every incident edge once. All degrees count
incidences, including both ends of a loop if one is present. Each
selected vertex has positive degree. At \(b\in B\), prescribe
\(t_b=s_b+ih_b\). At \(v\in S\), fix its real power \(n_v\) and cone
charge \(c_v\).

The real unknowns are \(s_v\), \(v\in S\), and the incidence values
\(g_{v,e}\). Their affine equations are
\[
            \sum_{e\ni v}g_{v,e}-\frac{n_v}{2}s_v
                                  =-\pi c_v.             \tag{6}
\]
For an oriented edge \(e=(v,w)\), its square coordinates are
\[
 A_P=s_v/4-g_{w,e}/2,\quad A_Q=s_v/4+g_{w,e}/2,\qquad
 y_P=g_{v,e}/2+s_w/4,\quad y_Q=g_{v,e}/2-s_w/4.             \tag{7}
\]
The closed feasible region requires all these coordinates to lie
in the closed square. Assume there is a strictly feasible point.
The energy is
\[
 \mathcal E=4\sum_e(E(A_P,y_P)+E(A_Q,y_Q))
                   -\sum_{b\in B}h_b\sum_{e\ni b}g_{b,e}. \tag{8}
\]

At a feasible point, assign to each square a covector
\((x_P,B_P)\) or \((x_Q,B_Q)\). For an interior square it must be
(1); at a corner it must satisfy (2). Define formal endpoint lengths
from these covectors by
\[
 h_{v,e}=2(B_P+B_Q),\quad h_{w,e}=-2(x_P-x_Q),\qquad
 k_{v,e}=x_P+x_Q,\quad k_{w,e}=B_P-B_Q.                    \tag{9}
\]
At an interior point these are the actual geometric coordinates.
At a corner they are only dual variables until a separate shape
interpretation is proved.

**Theorem 2.** A feasible point minimizes (8) if and only if it has
no open-side square and there are the above square covectors and
real numbers \(h_v\), \(v\in S\), such that
\[
 \begin{split}
 h_{v,e}&=h_v &&(v\in S,\ e\ni v),\\
 h_{b,e}&=h_b &&(b\in B,\ e\ni b),\\
 \sum_{e\ni v}k_{v,e}+\frac{n_v}{2}h_v&=0 &&(v\in S).
 \end{split}                                             \tag{10}
\]

**Proof.** Necessity of excluding open sides follows by moving
towards a strictly feasible point: an open-side square has derivative
\(-\infty\), whereas corner and interior factors have finite
derivatives in this direction.

Here is the multiplier justification at corners. Work temporarily
with all square coordinates as independent variables and impose
their linear matching, boundary and filling conditions as \(Cz=b\).
The product-square energy is convex and continuous on its compact
domain. Strict feasibility implies that its minimum-value function,
as a function of \(Cz-b\), is finite in a neighborhood of zero in
the range of \(C\): a small linear right inverse perturbation of
the strictly feasible point stays inside the squares. The supporting
hyperplane theorem applied to this finite convex value function
gives a multiplier at zero. Its pullback is a subgradient of the
unconstrained product energy at the minimizing point. Since this
energy is a sum of functions of separate square variables, its
subgradient consists exactly of their separate subgradients.
This establishes the multiplier statement without assuming
differentiability at the corners.

Returning to the independent variables \(s_v,g_{v,e}\), use the
Lagrangian
\[
 \mathcal E-\sum_{v\in S}h_v
       \left(\sum_{e\ni v}g_{v,e}-\frac{n_v}{2}s_v+\pi c_v\right).
\]
The linear differentiation identity following from (7) is
\[
 4\,dE_e=k_{v,e}\,ds_v+k_{w,e}\,ds_w
                   +h_{v,e}\,dg_{v,e}+h_{w,e}\,dg_{w,e}.
\]
With subgradients in place of gradients, its coefficients give
exactly (10). Conversely, sum the supporting inequalities for all
squares. Equations (10) cancel their linear terms on every feasible
variation, proving global minimality. \(\square\)

This is a finite certificate for every specified corner pattern:
each square is interior or one of four corners. Corner coordinates
and the graph matching/filling relations are linear; corner
covectors satisfy the explicit algebraic condition (3). Interior
covectors retain (1). The complete system is not being called
linear or semialgebraic in the angle variables. Exponentiating
integer-power period equations requires their original logarithmic
branches to be retained.

Thus excluding all nonempty corner patterns in (6)--(10) is an
exact characterization of interiority. A simpler sufficient test,
which needs no such enumeration, follows next.

## 3. The fixed energy cost of a corner

Let \(G=\sum_{j\ge0}(-1)^j/(2j+1)^2\) be Catalan's constant.
The energy is nonnegative throughout its square: it is even in
each variable, and (1) points in the direction of increasing
absolute value of the corresponding coordinate.

Every boundary side has the same constant energy \(G/2\).
For example \(E_A(A,y)\to0\) as \(y\to\pi/4\), uniformly on compact
subintervals of the open \(A\)-interval. Continuity therefore makes
that side constant. Its value is
\[
 E(\pi/4,0)=\frac14\int_0^{\pi/2}\operatorname{arsinh}(\tan u)\,du
          =\frac12G.                                     \tag{11}
\]
For the last equality,
\(\operatorname{arsinh}(\tan u)=\log\tan(\pi/4+u/2)\).
The integral of \(\log\tan\) from \(0\) to \(\pi/4\) is \(-G\):
substitute \(x=\tan u\), expand \(1/(1+x^2)\) by its finite
geometric sum, and use
\(\int_0^1x^{2j}\log x\,dx=-(2j+1)^{-2}\).
The integrated remainder tends to zero.

With complete outside angles, a feasible point containing a corner
therefore has
\[
                          \mathcal E\ge2G.                \tag{12}
\]
Consequently any strictly feasible test assignment with energy
less than \(2G\) proves that the minimum is interior. More generally,
with prescribed \(h_b\), the lower bound is
\[
 \mathcal E\ge2G-\frac{\pi}{2}\sum_{b\in B}d_b|h_b|,        \tag{13}
\]
because \(|g_{b,e}|\le\pi/2\). Comparing a feasible test value with
this bound gives a criterion with nonzero boundary data as well.

For an elementary upper estimate, whenever
\(|A|,|y|\le\pi/6\),
\[
                        E(A,y)\le A^2+y^2.                \tag{14}
\]
Indeed \(E(A,y)\le E(A,0)+E(0,y)\), since the first derivative
in \(|A|\) decreases when \(|y|\) increases. On the axis,
\(E_{AA}(A,0)=\sec(2A)\le2\), proving (14) by two integrations.

## 4. An explicit general condition for an interior minimum

Assume complete outside angles \(t_b=0\). Set
\(D_v=d_v^2+n_v^2\) for \(v\in S\). At outside vertices assign the
expressions \(|c_vn_v|/D_v\) and \(|c_v|d_v/D_v\) the value zero;
no outside power or charge needs to be chosen.

**Theorem 3.** The minimum is interior if
\[
 \begin{split}
 \frac{|c_vn_v|}{D_v}+\frac{|c_w|d_w}{D_w}
       &\le\frac13
       &&\text{at both orientations of every included edge},\\
 \sum_{v\in S}\frac{c_v^2d_v}{D_v}
       &<\frac{G}{\pi^2}.&
 \end{split}                                             \tag{15}
\]
Thus under (15) the original positive primitive filling equations
have their unique solution in this chart.

**Proof.** Use the explicit test assignment
\[
 s_v=\frac{2\pi c_v n_v}{D_v},\qquad
 g_{v,e}=-\frac{\pi c_v d_v}{D_v}
                \quad(v\in S),\qquad s_b=g_{b,e}=0.       \tag{16}
\]
It satisfies (6) exactly. The first condition in (15) gives
\(|s_v|+2|g_{w,e}|\le2\pi/3\), so every square coordinate has
absolute value at most \(\pi/6\). In particular the assignment
is strictly feasible.

Using (7) and (14),
\[
 \begin{split}
 \mathcal E
 &\le\frac12\sum_{v\in S}d_v s_v^2
                  +2\sum_{v\in S}\sum_{e\ni v}g_{v,e}^2\\
 &=2\pi^2\sum_{v\in S}\frac{c_v^2d_v}{D_v}<2G.
 \end{split}                                             \tag{17}
\]
The minimum exists on the compact closed polytope. It has no
open-side factors, and (12) excludes corners. The variational
theorem then gives the stated original positive solution.
\(\square\)

There is a particularly simple consequence at unit charges.
For \(k=|S|\ge1\), the condition
\[
                    d_v^2+n_v^2\ge16k\,d_v
                       \qquad(v\in S)                    \tag{18}
\]
implies (15). The sum in (15) is at most \(1/16\).
Also
\[
 \frac{|n_v|}{D_v}\le\frac1{\sqrt{D_v}}
                  \le\frac1{4\sqrt{k}},\qquad
 \frac{d_w}{D_w}\le\frac1{16k},
\]
whose sum is at most \(5/16<1/3\).
Finally \(1/16<G/\pi^2\), for example from
\(G>1-1/9=8/9\) and \(\pi^2<10\).
This condition allows arbitrary signs and arbitrary incidence
patterns. It is a geometric existence criterion, not an extension
of the previously proved quantum source bounds.

The quadratic upper bound in (17) is already minimized by (16)
subject to the affine filling equations alone. To verify this,
first minimize over a vertex's incidences with fixed sum; they must
all be equal. The remaining quadratic in \(s_v\) has its unique
minimum at (16), with value \(2\pi^2c_v^2d_v/D_v\).
Adding the square-coordinate bounds to that quadratic minimization
can only increase its minimum. Thus this particular energy test
cannot handle an arbitrary short vertex merely because its neighbors
have long powers: a single unit-charge zero-power degree-three
vertex already contributes \(2\pi^2/3>2G\).
More refined boundary comparisons would have to use additional
structure, rather than optimize the same quadratic upper bound.

## 5. An exact corner minimum with two nonzero powers

Consider the path \(b-v-w-b'\), with \(v,w\) selected, outside
angles zero, and original degrees \(d_v=d_w=2\). Choose
\[
                   n_v=2,\quad n_w=-2,\quad c_v=c_w=1.
                                                               \tag{19}
\]
The linear constraints are strictly feasible. For example set
\(s_v=\pi/2,s_w=-\pi/2\). At each selected vertex take its internal
incidence to be \(-\pi/8\), its outside incidence to be
\(-3\pi/8\), and every outside-endpoint incidence zero.
Their sums are \(-\pi/2\), so (6) holds, and every edge inequality
\(|s_v|+2|g_{w,e}|<\pi\) is strict.

Now define
\[
 u=\tfrac12\operatorname{arsinh}\sqrt3,\qquad
 t_v=\pi/2-2iu,\quad t_w=-\pi/2-2iu.                      \tag{20}
\]
At the candidate minimum keep \(s_v,s_w\) as above, but put
every selected incidence \(g_{v,e},g_{w,e}\) equal to
\(-\pi/4\). The outside edges are the actual positive one-edge
configurations with angles (20) and zero. Their selected increments
are exactly
\[
                    r_v=u-i\pi/4,\qquad r_w=-u-i\pi/4.    \tag{21}
\]
Indeed \(\tanh u=1/\sqrt3\), so
\(\tan(\pi/4-iu)=e^{-i\pi/3}\), while
\(\sinh(u-i\pi/4)=e^{-i\pi/3}\).
These values are on the continued one-edge branches.
The outside endpoints have their actual increments and hence
their prescribed imaginary angles zero.

On the internal edge oriented \(v\to w\), (7) gives
\[
                (A_P,y_P)=(\pi/4,-\pi/4),\qquad
                (A_Q,y_Q)=(0,0).                         \tag{22}
\]
Choose their subgradients to be \((u,-u)\) and \((0,0)\).
This is permitted by (2), since
\[
                       \sinh(2u)^2=3>1.                 \tag{23}
\]
Equations (9) now give internal endpoint values
\[
        h_{v,e}=h_{w,e}=-2u,\qquad
        k_{v,e}=u,\quad k_{w,e}=-u.
\]
They match the imaginary angles of the outside edges. The total
real increments at the two selected vertices are \(2u,-2u\);
thus the last equations in (10) read
\[
                2u+2(-2u)/2=0,\qquad
               -2u-2(-2u)/2=0.
\]
All conditions of Theorem 2 hold, proving a global minimum.
It is the unique minimum by the strict-feasibility uniqueness
argument of the convex variation note. Since (22) is a corner,
there is no interior solution in this original positive chart.

The strict inequality (23) also matters: these dual variables are
not the gradient of a limiting original strip with that corner.
The example proves a genuine limitation of the smooth positive
edge decomposition and of any assertion that nonzero signed powers
automatically avoid its corners. It does not rule out a different
cell decomposition, a reduced diagram, or a source identity that
treats the same original filling.

The distinction can also be checked directly in the actual shapes.
The angles (20) have tangents
\[
 a=(1-i\sqrt3)/2,\qquad b=(-1-i\sqrt3)/2,\qquad
                         1+a^2+b^2=0.
\]
In the original rational shape formulas with \(q=0\), this gives
\[
 A=\frac{\sqrt3-1}{2}(1+i),\quad C=-A,\qquad
 B=-\frac{\sqrt3+1}{2}(1+i),\quad D=-B.
\]
They have opposite orientations. They are not the flat shapes of
the corner square (22). Hence interpreting the strict supporting
covector in (23) as an actual original meridian increment would
produce a false geometric identification.
