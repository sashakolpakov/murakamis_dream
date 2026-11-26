# The derivative beside one immediate right-half neighbor

This note treats one half of the minimum-coordinate derivative when the
neighbor on that side is a right-half coordinate. The original raw bound
on that edge is retained. Its row is maximized over real rows, rather
than replaced by the complex stationary point of a coherent edge.
The geometry of consecutive types gives a positive estimate with the
same imaginary constant used in the earlier half decomposition.

## 1. Parameters and the geometric restriction

Let the moving coordinate have type indicator \(\alpha\in\{0,1\}\),
where zero means type three and one means type four. Its adjacent right
coordinate has indicator \(\beta\). Set \(d=1\) if the moving
coordinate is the first argument of this edge and \(d=0\) otherwise.
The row's factorial indicator is
\[
 \epsilon=\begin{cases}\beta,&d=1,\\\alpha,&d=0.\end{cases}
 \tag{1}
\]
After the established complete-row reduction, the right argument is
\(1/2\), with zero height. Write
\[
 .12\le t\le .22,\qquad \rho(t)=(t-.1)/.12,
 \qquad z=t+ic\rho(t)
 \tag{2}
\]
for an unselected moving coordinate. The reference coefficient \(c\)
is constant during the motion. It lies in the following closed interval:

| \(d\) | \(\alpha\) | \(\beta\) | interval for \(c\) |
|---|---|---|---|
| 1 | 0 | 0 | \([-.017,.010]\) |
| 1 | 0 | 1 | \([-.025,-.002]\) |
| 1 | 1 | 0 | \([-.054,-.030]\) |
| 1 | 1 | 1 | \([-.056,-.048]\) |
| 0 | 0 | 0 | \([-.017,.010]\) |
| 0 | 0 | 1 | \([-.025,.002]\) |
| 0 | 1 | 0 | \([-.056,-.030]\) |
| 0 | 1 | 1 | \([-.056,-.036]\) |

These are restrictions on actual cyclic references. To obtain them,
take the union of the appropriate middle-coordinate intervals in the
[three-type window table](research_mixed_neighbor_conditioned_critical_boxes.md).
For \(d=1\) the middle and last types are fixed; for \(d=0\)
the first and middle types are fixed. Intersect each window interval
with the actual type rectangle. Whenever the middle and last types
are both four, also use
[the sharper consecutive-four bound](research_mixed_four_before_four_height_lower.md),
\(-.056<c<-.048\), before taking the union. This gives exactly
the displayed intervals. A right *integration coordinate* has the
same original type and reference coefficient as before the row reduction.
Its replacement by the real target \(1/2\) does not change this
geometric information.

A selected center has \(\alpha=1\) and instead has target
\(z=t+iH\), \(H=.014\), with zero height velocity. No reference
height parameter occurs in that case.

## 2. The half derivative

Put \(g'(z)=\log(1-e^{-2\pi iz})\) on the original regular strip.
For every permitted Fourier alternative \(q\), set
\[
 K_q(z,u)=g'(z+u)-(1+\alpha/2-q/2)g'(z)
                  +2\pi i d u+\pi i(\sigma-q),
 \tag{3}
\]
where \(\sigma=0\), \(q=0\) in the unselected case, and
\(\sigma=1\), \(q\in\{0,1\}\) in the selected case.
These are the allocated source marginals: the half Fourier weight
and selected monomial have not been removed. Let
\[
 v=1+i\chi c/.12,\quad \chi\in\{0,1\}
 \tag{4}
\]
in the unselected case, and \(v=1\) in the selected case.
Use the earlier constants \(\kappa=3/2\) and
\(\gamma=\sigma/10\). The proposed half is
\[
 B_q(t,c)=\Re\bigl[v\{K_q(z,u_*)+i\kappa(1-2d)\}\bigr]
                           +\gamma(1-2d).
 \tag{5}
\]
Here \(u_*\) is the unique maximizing real row of this original
raw edge. The [row theorem](research_mixed_right_boundary_row_bracket.md)
gives \(1/5<u_*<2/5\); the
[algebraic description](research_mixed_algebraic_right_row.md) gives
its unique positive quartic or sextic root after the tangent substitution.

**Theorem 1.** For all eight unselected intervals above, both switches,
and every selected type/orientation/Fourier choice,
\[
                         B_q>1/2000.\tag{6}
\]
The following proof reduces (6) to elementary interval inequalities on
twelve compact parameter domains. The complete saved partition has
32 accepted rectangles, and its smallest lower bound exceeds .000826.
Numerical values at individual parameters are not used to assert (6).

## 3. Enclosing the maximizing row and its derivatives

The stationarity equation, written directly with the original logarithm,
is
\[
 T(u,z)=\Re\{g'(u+1/2)+g'(u+z)-(2+\epsilon)g'(u)
                  +2\pi i[d z+(1-d)/2]\}=0.
 \tag{7}
\]
All its arguments are regular on the above domains. The completed row
theorem gives \(T_u\le-2\pi\). Therefore, for any trial row
\(u_0\in[1/5,2/5]\),
\[
 |u_*(z)-u_0|\le |T(u_0,z)|/(2\pi).
 \tag{8}
\]
This is the real mean-value theorem between the trial row and the
unique zero. A bound on the whole parameter box in (8), intersected
with \([1/5,2/5]\), encloses every corresponding maximizing row.
The checker chooses its trial by sign-validated bisection at the exact
parameter midpoint. The trial does not certify itself: (7)--(8) are
reevaluated on the full parameter box. In particular, an uncertain
bisection sign never discards either possible root.

The implicit function theorem applies since \(T_u<0\). For each
real parameter \(p=t,c\), write \(z_p=\partial_pz\). Then
\[
 \begin{split}
 T_u&=\Re\{g''(u+1/2)+g''(u+z)-(2+\epsilon)g''(u)\},\\
 (u_*)_p&=-\Re\{[g''(u+z)+2\pi i d]z_p\}/T_u,\\
 (K_q)_z&=g''(u+z)-(1+\alpha/2-q/2)g''(z),\\
 (K_q)_u&=g''(u+z)+2\pi i d,\qquad
 g''(w)=\pi\cot(\pi w)-\pi i.
 \end{split}\tag{9}
\]
Consequently the parameter derivatives of (5) are exactly
\[
 \partial_pB_q=
 \Re\left[v_p\{K_q+i\kappa(1-2d)\}
       +v\{(K_q)_z z_p+(K_q)_u(u_*)_p\}\right].
 \tag{10}
\]
For an unselected center,
\(z_t=1+ic/.12\), \(z_c=i\rho(t)\), \(v_t=0\),
and \(v_c=i\chi/.12\). For a selected center only \(t\)
varies, \(z_t=1\), and \(v_t=0\).
This includes the variation of the maximizing row; it does not treat
that row as a fixed complex critical point.

On each rational parameter rectangle the checker bounds (5) directly,
and also bounds its midpoint value minus the full-box derivative
bounds from (10) times the parameter radii. The larger of these two
valid lower bounds is used. A rectangle is accepted only if all its
switch or Fourier alternatives exceed \(1/2000\).
Otherwise it is divided into its two exact closed midpoint children.
A saved replay reconstructs the complete trees, reevaluates (7)--(10),
and consumes every leaf. The finite tree partitions all twelve initial
domains: eight unselected rectangles and four selected intervals.
No complex critical-root solver or floating optimizer enters this proof.

## 4. Centers whose heights are fixed by an early neighbor

An early neighbor can keep the center's height fixed while its real
coordinate moves through \([.12,.22]\). The corresponding height
bands are
\[
 [-.005,1/300]\quad(3),\qquad [-.0095,0]\quad(4\text{ unselected}),
 \qquad [0,.014]\quad(4\text{ selected}).\tag{11}
\]
In this case \(v=1\), irrespective of the actual height. The
imaginary constant in (5) contributes zero, but the selected real
constant remains.

**Corollary 2.** On (11), the immediate-right half with fixed height
satisfies \(B_q>13/100\), for all local types, orientations and
permitted Fourier alternatives.

Here is a scalar proof requiring no new parameter partition. Write
\(z=t+ih\) and \(A=1+\alpha/2-q/2\), so \(A\) is either
one or \(3/2\). The nonconstant part of the horizontal derivative is
\[
                  \Re g'(z+u)-A\Re g'(z).\tag{12}
\]
For \(.12\le t\le.22\), \(.2\le u\le.4\), and
\(|h|\le.014\),
\[
       \Re\cot\pi(z+u)<1<\Re\cot\pi z.\tag{13}
\]
For the first inequality, if \(t+u\ge.5\) the real part is
nonpositive; otherwise it is at most \(\cot(.32\pi)<1\).
For the second, use
\[
 \Re\cot\pi(t+ih)=\frac{\sin(2\pi t)}{\cosh(2\pi h)-\cos(2\pi t)}.
\]
The numerator plus \(\cos(2\pi t)\) exceeds \(23/20\)
throughout the interval. Indeed \(\sin\theta+\cos\theta\)
is concave there, and both endpoint values exceed \(23/20\).
Also \(\cosh(.028\pi)<101/100\). These strict scalar
inequalities prove (13).
Thus (12) decreases with \(t\), at fixed \(h,u\); its minimum
is at \(t=.22\). On the remaining row interval, the maximum of
\(\cos(2\pi(.22+u))\) is at \(u=.4\), rather than at
\(u=.2\): the respective distances from \(.5\) are .12
and .08. The numerator modulus is consequently smallest at .4.
It suffices to bound
\[
 F_A(h)=\frac12\log(1+r^2-2rC_1)
          -\frac A2\log(1+r^2-2rC_0),
 \quad r=e^{2\pi h},\quad C_0=\cos(.44\pi),\ C_1=\cos(1.24\pi).
 \tag{14}
\]
For \(A=1\), this is even in \(h\); its derivative with respect
to \(r\) has the sign of \((C_0-C_1)(1-r^2)\). Its minimum
on the type-three band is therefore \(F_1(-.005)\).

For \(A=3/2\), the numerator of that derivative, after multiplication
by the two positive quadratic denominators, is
\[
 (C_0-C_1)(1-r^2)-\tfrac12(r-C_0)(1+r^2-2rC_1).\tag{15}
\]
Throughout (11),
\(47/50<r<11/10\), \(.18<C_0<.19\), and
\(-.74<C_1<-.72\). Hence (15) is at most
\[
 .93(1-.94^2)-\tfrac12(.94-.19)(1+.94^2+2(.94)(.72))<0.
\]
Thus \(F_{3/2}\) decreases with \(h\). For a selected center
and \(h\ge0\), the quadratic containing \(C_0\) exceeds one;
therefore \(F_1(h)\ge F_{3/2}(h)\), so the other Fourier
alternative requires no smaller bound. Finally, direct outward scalar
evaluations give
\[
 F_1(-.005)>.37,\qquad F_{3/2}(0)>.25,\qquad
                   F_{3/2}(.014)-.1>.13.\tag{16}
\]
The last expression includes the unfavorable selected real constant.
These inequalities prove the corollary. The checker records each
scalar comparison in (13)--(16) and the exact rational upper bound
in (15). No optimized row or uncertain numerical sign is used here.

## 5. What this adds to the minimum-coordinate argument

The constants agree with the
[unselected half decomposition](research_mixed_minimum_level_half_stencils.md)
and the [constant-selected decomposition](research_mixed_constant_selected_height_transport.md).
The imaginary and real constants in (5) are exactly opposite on the
left and right halves of the same center. Thus they cancel when two
compatible halves are added. Corollary 2 also permits a center whose
height is fixed by an early neighbor on its other side. The actual
unselected height velocity
uses \(\chi=1\); allowing both switches also controls the more
conservative negative-height-cost criterion. Selected right endpoints
are stationary and real, so their source factors have no derivative
along this motion. All original row and Fourier choices remain present.

The assertion treats an immediate right neighbor only. It can be
combined with an already proved opposite half when that opposite half's
full domain assumptions hold. It does not extend those assumptions to
an upper-taper neighbor, prove the distance-two right case, or supply
noncancellation for the full finite sum. It is also compatible with a
two-cycle: the two incidences remain separate and their constants cancel.

    python3 experiments/check_mixed_immediate_right_half.py

