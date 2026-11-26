# Selected plateau coordinates at intermediate heights

Research proof, 4 November 2026. A transition coordinate lowers the
heights of its neighboring plateau coordinates. If such a neighbor is
selected, its height lies between zero and \(H=7/500\). The endpoint
estimates already proved in the research notes give bounds throughout
that interval by convexity. The resulting loss need not be positive
near height zero; the formulas below retain the cost that adjoining
blocks must pay.

## 1. The finite block and its two Fourier branches

Let both real target coordinates belong to \(P=[11/50,9/20]\), and
let \(r=(r_0,r_1)\) be an original geometric reference pair of the
corresponding types. Write \(c_j=\Im r_j\), let
\(\phi=\phi_{\eta\epsilon}\) be the allocated critical phase, and set
\[
 \Gamma_r(z)=\phi(r)+\phi'(r)\cdot(z-r),\qquad
 q_0=\frac{11}{2},\quad q_1=\frac{151}{20},\quad
 \delta=\frac1{100}.                                         \tag{1}
\]
The coordinates are numbered zero and one in their original order.

Let \(\sigma_j\) indicate that coordinate \(j\) is selected; selection
is allowed only at type-four positions. For each choice
\(f_j\in\{0,\ldots,\sigma_j\}\), use the holomorphic phase
\[
 \psi_f(z)=\phi(z)+\sum_{j=0}^1
       \left\{\frac{f_j}{2}g(z_j)
                         +\pi i(\sigma_j-f_j)z_j\right\}.
                                                               \tag{2}
\]
At a selected height \(h\ge0\), the true allocated Fourier rate is
\[
 \frac12\max\{-\Re g(x+ih),2\pi h\}-\pi h.
\]
Taking the maximum over the choices in (2) retains this rate exactly.
At height zero, the branch with \(f_j=1\) adds
\(\Re g(x)/2<0\), and the branch with \(f_j=0\) adds zero.

The [selected right-taper curvature theorem](research_mixed_selected_right_taper_support.md),
Lemma 2, applies on the entire plateau square with the independent
height intervals used here. It gives
\[
 -\Re\psi_f''\succ\frac54 I.
\]
Consequently, with the other coordinate fixed,
\(\Re(\psi_f-\Gamma_r)\) is convex in either target height.
The maximum of these branches need not be concave in the real
coordinates; no such assertion is needed.

At the corners of the height intervals we use three existing results:
the [selected plateau bound](research_mixed_selected_plateau_support.md),
the [selected/reset bound](research_mixed_selected_reset_plateau_support.md),
and the [orientation-dependent reset bound](research_mixed_oriented_height_reset.md).
The first two give phase defect at most \(-\delta\) whenever a
selected coordinate has height \(H\) and the other coordinate has
its stated endpoint height. Resetting only coordinate \(j\) to zero,
with the other at its reference height, costs at most \(q_jc_j^2\).

## 2. One selected coordinate

Suppose coordinate \(j\) is selected and has target height \(tH\),
where \(0\le t\le1\). If the other coordinate is unselected and
has its original reference height, every branch satisfies
\[
 \Re\{\psi_f(z)-\Gamma_r(z)\}
       \le (1-t)q_jc_j^2-t\delta.                             \tag{3}
\]
Indeed, the value at \(t=0\) is at most the oriented reset cost:
the extra forcing branch at a real coordinate only decreases it.
The value at \(t=1\) is at most \(-\delta\). Convexity bounds
the intermediate value by the chord joining these endpoint bounds.

If the other coordinate is selected and remains at height \(H\),
the stronger estimate
\[
 \Re\{\psi_f(z)-\Gamma_r(z)\}\le-\delta                     \tag{4}
\]
holds for the whole interval. At \(t=0\) use the selected/reset
theorem. Any forcing term belonging to the coordinate at height zero
is again nonpositive. At \(t=1\) use the selected plateau theorem,
then interpolate each branch.

## 3. Two selected coordinates

Now both positions are type four and both are selected. Their heights
are \(t_0H,t_1H\), with \(0\le t_0,t_1\le1\). Both reference
heights are negative. The
[same-sign reset theorem](research_mixed_same_sign_height_reset.md)
therefore bounds the corner with both target heights zero by
\[
 C=q_0c_0^2+q_1c_1^2.
\]
Every other corner has a selected height \(H\), so its phase defect
is at most \(-\delta\). Applying height convexity successively to
the two coordinates gives
\[
 \Re\{\psi_f(z)-\Gamma_r(z)\}
 \le (1-t_0)(1-t_1)C
       -\{1-(1-t_0)(1-t_1)\}\delta.                           \tag{5}
\]
This includes all four forcing choices. It also covers unequal height
reductions at the two endpoints of a plateau edge.

## 4. A selected height and a partially reset unselected height

Let position \(j\) be selected at height \(tH\), and let the other
position \(k\) be unselected at height \(u c_k\), with
\(0\le t,u\le1\). Define a bound for the corner with both heights
zero by
\[
 C=\begin{cases}
 q_0c_0^2+q_1c_1^2,&\text{if both positions have type four},\\
 10(c_0^2+c_1^2),&\text{otherwise}.
 \end{cases}                                                   \tag{6}
\]
The first line uses the same-sign theorem; the second uses the
[full height-reset estimate](research_mixed_full_height_reset.md).
The four corners \((t,u)=(0,0),(0,1),(1,0),(1,1)\) have respective
upper bounds \(C,q_jc_j^2,-\delta,-\delta\). Thus
\[
 \Re\{\psi_f(z)-\Gamma_r(z)\}
 \le (1-t)\{(1-u)C+u q_jc_j^2\}-t\delta.                    \tag{7}
\]
Convexity applies even when \(c_k<0\): composition with the affine
parameter \(u\mapsto u c_k\) preserves convexity.

## 5. A uniform loss above four fifths of the original contour height

Suppose at least one coordinate is selected, and each target height is
at least four fifths of its prescribed height in the following sense:
write a selected height as \(t_jH\), and an unselected height as
\(t_jc_j\), with \(4/5\le t_j\le1\). Then every branch obeys
\[
                 \Re(\psi_f-\Gamma_r)<-\frac1{500}.           \tag{8}
\]
This follows directly from the preceding bounds and the original
reference height intervals. In both lines of (6),
\[
 C\le C_*=(q_0+q_1)(.057)^2=\frac{847989}{20000000},\qquad
 q_jc_j^2\le Q_*=q_1(.057)^2=\frac{490599}{20000000}.
\]
For the type-three alternative, use
\(10[(.057)^2+(.03)^2]\le C_*\).
Since \(C\ge q_jc_j^2\), the right side of (7) is decreasing in
both \(t\) and \(u\). At their smallest allowed values it is at most
\[
 \frac15\left(\frac15 C_*+\frac45 Q_*\right)
                    -\frac45\delta
       =-\frac{237923}{100000000}<-\frac1{500}.
\]
For two selected coordinates, (5) instead gives
\(C_*/25-24\delta/25=-3952011/500000000\), a stronger bound.
These comparisons are exact rational inequalities.

## 6. Bounds for the original finite functions

The full conditional source theorem on the plateau rectangle includes
all the height intervals above. For every fixed \(\varepsilon>0\),
its uniform asymptotic and the actual Fourier-polynomial upper bound
therefore convert each right side \(B\) of (3)--(7) into
\[
 |C_{\epsilon,N}(X,Y)|
 |d_N(X)X^{-N\sigma_0}|^{\eta/2}
 |d_N(Y)Y^{-N\sigma_1}|^{\epsilon/2}
 \le C_\varepsilon N^A
                 e^{N(\Re\Gamma_r(z)+B+\varepsilon)}.         \tag{9}
\]
Here \(X=e^{-2\pi iz_0}\), \(Y=e^{-2\pi iz_1}\); the square
roots in this modulus notation are nonnegative real roots. All original
rows and both parities are retained. The tolerance in (9) must be
budgeted when several blocks are multiplied. In particular, (8) gives
a complete finite-source loss of \(1/1000\) when every height fraction
is at least \(4/5\), by choosing \(\varepsilon<1/1000\).

These are bounds for plateau edges whose heights have been lowered by
neighboring transition coordinates. They do not estimate an edge whose
real coordinate itself lies below \(.22\), and do not prove a global
selected-term gap. Their purpose is to supply explicit costs for that
remaining comparison.
