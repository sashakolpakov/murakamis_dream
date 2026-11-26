# Comparing selected and unselected heights beside a raw edge

The geometric phase on one incident edge can be combined with the real
row maximum on the other. Although this maximum is not holomorphic in
the moving coordinate, it is convex in its imaginary part. This suffices
for the vertical comparison used to remove a selected height. It also
reduces the required derivative estimates to two real parameters.

The reduction below is proved analytically. The numerical derivative
bounds specified in Section 3 are additional hypotheses; this note does
not assert that they have been established.

## 1. The real envelope and its derivative

Use
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},
 \qquad g'(z)=\log(1-e^{-2\pi iz}),
 \qquad g''(z)=\pi\cot(\pi z)-\pi i,
\]
with the original logarithmic branches. The moving coordinate has type
four and belongs to
\[
 W=\operatorname{conv}\{.45-.057i,\ .5,\ .45+.014i\}.
\]
Its right-half neighbor has already been replaced by the real target
\(1/2\) in the complete raw upper bound. Put \(d=1\) if the
moving coordinate is the first argument of that edge, and \(d=0\)
otherwise. The row factorial indicator \(\epsilon\) equals the
right neighbor's type indicator when \(d=1\), and equals one when
\(d=0\). Here zero and one denote types three and four.

For \(z=t+ih\), define
\[
\begin{split}
 E_d(u,z)=\Re\{&g(u+1/2)+g(u+z)-(2+\epsilon)g(u)\\
             &+2\pi i[d z+(1-d)/2]u-\tfrac32g(z)\},\\
 A_d(z)&=\max_{1/5\le u\le2/5}E_d(u,z).
\end{split}\tag{1}
\]
Terms independent of \(z\) have no effect on this comparison.
The completed [raw-row theorem](research_mixed_right_boundary_row_bracket.md)
puts the full maximizing row strictly inside this interval and gives
\(\partial_u^2E_d\le-2\pi\). Its unique maximizer \(u_d(z)\)
is consequently smooth in the two real coordinates of \(z\).

Let \(a\) be the other, nonright neighbor, with type indicator
\(\beta\). Write \(\phi_{\eta\epsilon}\) for the original
allocated conditional phase defined in
[the clamping theorem](research_mixed_unselected_right_clamping.md),
equation (2). Define the real combined rate
\[
 V_d(a,z)=\begin{cases}
 \Re\phi_{\beta1}(a,z)+A_1(z),&d=1,\\
 \Re\phi_{1\beta}(z,a)+A_0(z),&d=0.
 \end{cases}\tag{2}
\]
The allowed neighbor polygons are
\[
\begin{split}
 \Omega_3&=\operatorname{conv}\{.1,.22-.03i,.45-.03i,.5,
                                      .45+.02i,.22+.02i\},\\
 \Omega_4&=\operatorname{conv}\{.1,.22-.057i,.45-.057i,.5,
                                      .45+.014i,.12+.014i\}.
\end{split}\tag{3}
\]
They include permitted selected neighbor heights. Those neighbors are
held fixed in the vertical motion of the center.

The center marginal of the raw edge is
\[
 K_d(z)=g'(z+u_d(z))-\tfrac32g'(z)+2\pi i d u_d(z).
\]
Let \(G_d(a,z)\) be this expression plus the center marginal of
the conditional phase in (2). Real stationarity of \(u_d\), or
the elementary envelope theorem, gives
\[
                 \partial_h V_d(a,t+ih)=-\Im G_d(a,t+ih).
 \tag{4}
\]
No complex stationary equation is imposed on the raw row.

## 2. Convexity removes one continuous parameter

**Lemma 1.** For every fixed permitted \(a,t\), the function
\(h\mapsto V_d(a,t+ih)\) is convex on the vertical segment of
\(W\). In particular \(\Im G_d(a,t+ih)\) is nonincreasing in
\(h\). A lower bound for this imaginary marginal on \(W\)
therefore follows from its lower bound on the top edge
\[
                z=t+i(.014)20(.5-t),\qquad .45\le t\le.5.
 \tag{5}
\]

For the raw edge, at each fixed \(u\in[.2,.4]\),
\[
 \partial_h^2 E_d(u,t+ih)
       =-\Re\{g''(u+z)-\tfrac32g''(z)\}>0.\tag{6}
\]
Indeed \(.65\le u+t\le.9\), so
\(\Re\cot\pi(u+z)<0\), whereas
\(\Re\cot\pi z\ge0\) for \(.45\le t\le.5\).
These signs follow directly from
\(\Re\cot\pi(x+ih)=\sin(2\pi x)/(\cosh(2\pi h)-\cos(2\pi x))\).
The linear chirp contributes no second derivative. A supremum of convex
functions is convex, which proves the assertion for \(A_d\).

For the conditional phase, the
[closed-cotangent theorem](research_mixed_closed_cotangent_roots.md)
supplies its original holomorphic root on a neighborhood of the whole
product \(\Omega_{3+\beta}\times W\), in either order. The
negative real part of its full Hessian before elimination is positive:
it is the sum of the two positive triangle forms, the nonnegative
own-factorial forms, and a chirp with zero real Hessian. Complex Schur
elimination preserves this positivity. This is the same argument used
in [the selected curvature deduction](research_mixed_selected_height_reference_extension.md),
Corollary 2; here its input is the closed cotangent inclusion of the
polygons (3) and \(W\). Thus the real conditional phase is convex
in the center height. Adding the two convex functions proves the lemma,
and (4) proves the monotonicity assertion.

For fixed \(z\), the row \(u_d(z)\) is independent of \(a\).
Consequently \(\Im G_d(a,z)\) is harmonic in \(a\): its raw
part is a constant and its remaining part is the imaginary part of a
holomorphic marginal. A minimum principle reduces the neighbor to
\(\partial\Omega_{3+\beta}\). The same holds for the clipped
polygon \(\Omega_{3+\beta}\cap\{\Re a\ge.16\}\).
Together with (5), this leaves only the top-edge parameter \(t\)
and one neighbor-edge parameter. It does not apply a harmonic minimum
principle to the raw envelope in \(z\).

If both neighbors are right coordinates, replace (2) by
\(A_0(z)+A_1(z)\). The same proof applies with two independently
maximized rows and no neighbor-edge parameter.

## 3. Sufficient derivative bounds for removing a selected height

Suppose the reduced comparisons establish
\[
\begin{array}{ll}
 \Im G_d(a,z)>-3/5,&a\in\Omega_{3+\beta},\ z\in W,\\
 \Im G_d(a,z)>-9/20,&a\in\Omega_{3+\beta},\ \Re a\ge.16,\ z\in W.
\end{array}\tag{7}
\]
These are sufficient numerical hypotheses, not conclusions of Lemma 1.
With two right neighbors, only the second bound is needed.

Let \(s\in[0,1]\) be the center's slow neighboring cutoff,
\(f=\min\{6s,1\}\), \(R=400(.5-t)^2\), and
\(c_*\in[-.057,0]\) its original unselected coefficient. Its
unselected and selected targets are
\[
 z_u=t+ic_*sR,\qquad z_s=t+i(.014)fR.
\]
All intervening heights belong to \(W\). If \(s\ge1/2\),
the nonright neighbor has real part at least .16; the right neighbor
has real part .5. Hence the corresponding line of (7) applies.

Integrating (4) between these heights gives exactly the vertical bound
used in [the selected-height comparison](research_mixed_right_selected_height_removal.md),
equation (5). That proof uses only this real derivative bound, not
holomorphy of the combined rate. Its scalar inequalities therefore give
\[
\begin{split}
 V_d(a,z_s)+\max\{\Re g(z_s),-2\pi\Im z_s\}
 \le V_d(a,z_u)-\min\{\kappa_F fR,\kappa_G(.5-t)\},\\
 \kappa_F=.028\pi-.0426>0,\qquad
 \kappa_G=\log(2\sin(.45\pi))-.639>0.
\end{split}\tag{8}
\]
Both Fourier alternatives remain in (8). Neighbor corrections are
constant in this comparison and cancel. As in the earlier argument,
the conclusion allows equality at a zero cutoff or the half endpoint.

This is a conditional comparison of upper rates. To use it for the
original finite source one must retain the established source bounds
and their tolerances. To remove upper-transition coordinates entirely
one also needs the separate unselected mixed clamping inequality.
Neither that inequality nor (7) is inferred from the convexity lemma.
