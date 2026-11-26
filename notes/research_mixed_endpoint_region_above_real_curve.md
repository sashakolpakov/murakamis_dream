# The complete endpoint sum between the real axis and the auxiliary-real curve

Research deduction, 8 November 2026. The endpoint asymptotic holds
throughout the closed region between the real private-index interval
\([1/8,1/4]\) and the explicit curve on which its auxiliary critical
point is real. This is a two-dimensional source domain, rather than
an unspecified neighborhood of a path. The proof compares the two
real auxiliary endpoints with the critical action and retains every
term of the finite sum.

The result does not cover the deeper side of the curve. In particular,
it does not supply a descending outer-cap contour or a complete
outer-cap asymptotic. No numerical evaluation is used.

## 1. Source, region, and statement

Use precisely the original source and phase of
[the auxiliary-real curve theorem](research_mixed_endpoint_auxiliary_real_curve.md):
\[
\begin{split}
C_N(e,w)&=\sum_{l=0}^{N-1}
 \frac{e^{i\pi e l}e_l(w)}{S_lG_N(Ne-l)},\\
F(e,u)&=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu,\qquad
J'(q)=\Log(2\sin\pi q).
\end{split}                                                     \tag{1}
\]
The Newton polynomials, sine factorial, logarithms and additive
constants are unchanged. Write
\[
p(t)=1-2t^2+2it,\quad
e(t)=E(t)-i\eta_0(t)=\frac{\Log p(t)}{2\pi i},\quad
\frac{\sqrt3-1}{2}\le t\le\frac1{\sqrt2}.
                                                               \tag{2}
\]
The cited theorem proves that \(E(t)\) increases strictly from
\(1/8\) to \(1/4\), and that
\[
u_0(t)=\frac{\arctan t}{\pi},\qquad
0<u_0(t)<E(t),\qquad
F_u(e(t),u_0(t))=0.
                                                               \tag{3}
\]
Regard the depth in (2) as a continuous function \(\eta_0(E)>0\).
Our new region is
\[
\mathcal W=\{E-i\eta:1/8\le E\le1/4,\quad0\le\eta\le\eta_0(E)\}.
                                                               \tag{4}
\]

**Theorem.** On a fixed complex neighborhood of
\(\mathcal W\times\{-2\}\), the complete original sum has
\[
C_N(e,w)=N^{-3/2}A(e,w)e^{NS(e,w)}
                 (1+O_{\rm hol}(N^{-1})),\qquad A(e,w)\ne0.
                                                               \tag{5}
\]
The action, symbol, and Gaussian square root are the original
endpoint ones. Both integer parities and every fixed mixed
ordinary-color/private-index derivative of the normalized error
are included on smaller fixed neighborhoods.

## 2. The critical branch remains in the original chamber

For every upper-half-plane \(p\), the equation
\[
(p-5)\omega^2+2(p+1)\omega+p-1=0
                                                               \tag{6}
\]
has exactly one upper-half-plane root. This is the root-count
argument in Section 1 of
[the bridge phase theorem](research_mixed_endpoint_bridge_phase_floor.md);
that argument applies to the entire upper half-plane, independently
of the smaller strip subsequently used there. A real root would
make \(p=(5\omega^2-2\omega+1)/(\omega+1)^2\) real. The leading
coefficient and discriminant do not vanish in the upper half-plane.
The selected root is therefore simple and holomorphic. Set
\(u_c=\Log\omega/(2\pi i)\), with \(0<\arg\omega<\pi\).

We claim that throughout (4),
\[
0<\Re u_c<E,\qquad \Im u_c\ge0,\qquad F_u(e,u_c)=0,
                                                               \tag{7}
\]
with equality in the height assertion exactly on the lower
boundary (2).

Start at that boundary and decrease \(\eta\) while holding \(E\)
fixed. At its real auxiliary saddle put
\[
A_0=2\tan\pi u_0+3\cot\pi u_0>0,\qquad
C_0=\cot\pi(e-u_0)=B+iD .
\]
Here \(B,D>0\), since \(0<E-u_0<1/2\) and
\(\Im(e-u_0)<0\). Implicit differentiation of the original
equation gives
\[
\frac{du_c}{de}=\frac{C_0+i}{A_0+C_0},\qquad
\Re\frac{du_c}{de}
=\frac{B(A_0+B)+D(D+1)}{|A_0+C_0|^2}>0.
                                                               \tag{8}
\]
Thus \(d(\Im u_c)/d\eta=-\Re(du_c/de)<0\) at the boundary:
moving toward the real private axis makes the auxiliary height
strictly positive.

It cannot return to height zero in the interior. If \(u_c\) is
real, write \(t=\tan\pi u_c>0\). Equation (6) then forces exactly
\(p=1-2t^2+2it\). The argument of this expression increases
strictly with \(t>0\), since its derivative is
\(2(1+2t^2)/(1+4t^4)>0\). For fixed \(E\) there is therefore
only the one depth \(\eta_0(E)\) with a real auxiliary root.

Nor can \(\Re u_c\) reach \(E\) while \(\Im u_c\ge0\).
Until a first such crossing the original chamber is regular,
so the zero logarithmic lift is preserved. At a putative
crossing, \(e-u_c\) has real part zero and strictly negative
height. The limiting imaginary derivative is
\[
\Im F_u
 =2\Arg\sin\pi(1/2-u_c)-3\Arg\sin\pi u_c
                    -\pi/2+\pi E<0.
                                                               \tag{9}
\]
The first two terms are nonpositive because \(\Im u_c\ge0\);
also \(E\le1/4\). This contradicts the zero lift.
The global upper-root selection prevents \(\Re u_c=0\).
The root cannot vanish or diverge on the compact parameter
region, since \(p\ne1,5\) there. These facts complete the
continuation to \(\eta=0\) and prove (7).

Consequently \(u_c,1/2-u_c,e-u_c\) have real parts uniformly
inside their original strips on (4). Also
\[
-\Re F_{uu}(e,u)
=\pi\Re\{2\tan\pi u+3\cot\pi u+\cot\pi(e-u)\}>0
                    \quad(0<\Re u<E).
                                                               \tag{10}
\]
This holds at every finite auxiliary height. The critical
point is simple, and its original action is \(S(e)=F(e,u_c(e))\).

## 3. Both real auxiliary endpoints lie below the action

Consider first the right endpoint \(u=E\), using the continuous
lower boundary value of \(J(-i\eta)\). Its real value is
\(-\pi\eta/2\). Hence
\[
\Re F(E-i\eta,E)
 =-2J(1/2-E)-3J(E)+\pi\eta(1/2+E).
                                                               \tag{11}
\]
Let \(G_R(E,\eta)=\Re S(E-i\eta)-\Re F(E-i\eta,E)\).
The original envelope derivative is
\[
S'(e)=-J'(e-u_c)+i\pi u_c.
                                                               \tag{12}
\]
Since \(e-u_c\) has negative height and real part in \((0,1/2)\),
\[
0<\Im S'(e)<\pi/2+\pi\Re u_c.
\]
For \(\eta>0\), (11) therefore gives
\[
\partial_\eta G_R
 =\Im S'(e)-\pi(1/2+E)
 <-\pi(E-\Re u_c)<0.
                                                               \tag{13}
\]
At \(\eta=\eta_0(E)\), the curve theorem's strictly decreasing
real profile after \(u_0\) proves \(G_R>0\). Integrating (13)
toward smaller depths preserves this strict gap, including
the continuous endpoint at \(\eta=0\).

For the left endpoint use \(F(e,0)=-J(e)\), and put
\(G_L(E,\eta)=\Re\{S(e)+J(e)\}\).
If \(q=r-ih\), \(0<r<1/2\), \(h\ge0\), then
\[
\Arg\sin\pi q=-\arctan\{\cot(\pi r)\tanh(\pi h)\}.
\]
Compared with \(e\), the argument \(e-u_c\) has a smaller
positive real part and at least as large a depth. By (7),
\[
\Arg\sin\pi(e-u_c)\le\Arg\sin\pi e .
\]
Together with (12), this proves
\[
\partial_\eta G_L
 =-\Arg\sin\pi(e-u_c)+\pi\Re u_c+\Arg\sin\pi e>0.
                                                               \tag{14}
\]
On the real axis \(G_L(E,0)=h(E)=\Re S(E)+J(E)>0\).
Here the original real endpoint profile has \(h(0)=0\),
\(h'(1/2)=0\), and \(h''<0\) on \((0,1/2)\); these are the
profile identities of
[the endpoint polynomial collar](research_mixed_endpoint_polynomial_collar.md)
and [wrapped-row transport](research_mixed_cap_wrapped_row_transport.md).
Thus (14) proves the left gap on all of (4).

Both gaps are continuous and strictly positive on the compact
region. They have positive common lower bounds. In particular,
\[
\Re S(E-i\eta)>-2J(1/2-E)-3J(E)
                                                               \tag{15}
\]
throughout the new region, with the original additive constant.

## 4. All physical and revived rows

Use the complete zero-safe row rate \(R(e,x)\) from equations
(11)--(12) of the curve theorem. For \(0<x<1/2\), its exact force
can also be written
\[
e^{R_x(e,x)}
=\frac12\left|e^{2\pi\eta}-e^{-2\pi i(E-x)}\right|
                        \frac{\cos^2\pi x}{\sin^3\pi x}.
                                                               \tag{16}
\]
For fixed \(E,x\), this increases with \(\eta\ge0\):
the square of the modulus is \(T^2-2T\cos(2\pi(E-x))+1\),
whose derivative in \(T\ge1\) is nonnegative.
Thus every shallower force is bounded above by the curve force.
The latter is strictly less than one for \(x>u_0(E)\),
by the exact factorization in the curve theorem.

Choose one sufficiently small fixed \(\varepsilon>0\).
The gaps of Section 3 and continuity ensure that
\[
\Re S(e)-\Re F(e,\varepsilon)>c,\qquad
\Re S(e)-\Re F(e,E-\varepsilon)>c
                                                               \tag{17}
\]
for some \(c>0\), uniformly on (4). Shrink \(\varepsilon\) so
that both cuts surround \(\Re u_c\) and
\(E-\varepsilon>u_0(E)\), using compactness and (7).
The force near zero tends uniformly to infinity: the private
sine numerator stays separated from zero and the denominator
in (16) vanishes cubically. Hence the real profile increases
up to the lower cut, after another reduction of \(\varepsilon\).
For \(x\ge E-\varepsilon\), (16) and the curve comparison make
it strictly decreasing until \(1/2\), including all revived rows
beyond \(x=E\). At a real reciprocal zero this assertion means
the corresponding integrated continuous rate inequality.
Thus (17) pays every omitted lower-half row.

For \(x\ge1/2\), the exact reflected bound of the curve theorem
still gives
\[
R(e,x)<1/6+5\pi\eta/2.
                                                               \tag{18}
\]
For \(E\le1/6\), one has
\(\eta\le\eta_0(E)<\log(10/9)/(2\pi)\), so (18) is less than
\(11/36\); (15) is greater than \(1/2\).
For \(E\ge1/6\), (18) is less than \(29/48\), whereas (15)
is greater than \(103/165\). These are exactly the elementary
\(J\)-bounds proved in Section 3 of the curve theorem, now applied
using (15). The upper-half gap is therefore at least \(53/2640\).
The original uniform row bounds include both true ends, all
reciprocal zeros, and both level parities.

## 5. The retained contour and nonzero coefficient

At each fixed base \(e=E-i\eta\), retain the integer rows between
the cuts \(\varepsilon,E-\varepsilon\), with their half-grid
contour boundaries. Use the original exact interpolation
\[
f_N(e,u,w)=
 \frac{e^{i\pi Neu}\mathcal E_N(u,w)}
                      {G_N(Nu)G_N(N(e-u))}
                                                               \tag{19}
\]
from the curve theorem. It is holomorphic on the retained
strip and has the original symbol \(N^{-2}b(e,u)e^{NF(e,u)}\).
No physical row or Newton term is deleted.

Let \(H=\Im u_c\ge0\). The horizontal main path at height \(H\)
has a unique nondegenerate maximum at \(u_c\), by (10).
Its two endpoints are strictly below the action. If \(H>0\),
the exact reflection identity used in
[the deeper endpoint theorem](research_mixed_endpoint_cap_rectangle_deeper_extension.md),
equations (13)--(15), gives
\[
\Re F(e,x-iH)-2\pi H
 \le\Re S(e)-\pi(1-2E)H
 \le\Re S(e)-\pi H/2.
                                                               \tag{20}
\]
The other horizontal alias loses \(2\pi H\). Slightly enlarge
the outer heights to put the main path inside the rectangle,
retaining strict gaps. On both vertical sides, (10) gives
convexity in height. After subtracting the linear cotangent
penalty on each sign half, their maxima occur at endpoints
already paid by (17) and (20). The two unweighted joins are
also paid by convexity between their real and main-height
endpoints.

At \(H=0\), use the fixed small symmetric rectangle of the
curve theorem instead. Its original bound
\(|\Im F_u|<\pi\) near the retained real path pays both
horizontal aliases, and the strict cut gaps pay the whole
vertical sides and joins. A rectangle of zero height is
never used.

The exact residue density remains \(+N\). Stationary phase
on the main path gives the original nonzero symbol
\[
A(e,-2)=
\frac{\sqrt{2\pi}}
 {\sqrt{-F_{uu}(e,u_c)}
  (2\sin\pi u_c)^{3/2}(2\sin\pi(e-u_c))^{1/2}}.
                                                               \tag{21}
\]
The powers are \(N\cdot N^{-2}\cdot N^{-1/2}=N^{-3/2}\).
Every other source contribution has a fixed exponential gap.
This proves (5) at each base point.

Hold cuts, integer row sets and contour paths fixed before
varying parameters. The original uniform factorial/Newton
bounds preserve all strict gaps on small fixed neighborhoods,
including at numerator and reciprocal zeros in omitted rows.
The saddle and its symbol continue in the regular chart.
A finite cover of (4), followed by Cauchy's formula on smaller
neighborhoods, gives the uniform holomorphic error and all
fixed mixed derivatives claimed in (5).

This completes the endpoint sum on the whole region (4).
It supplies no width on the deeper side of its lower boundary.
The outer action can increase along that boundary near its
own critical point, so a valid outer contour must still be
proved separately.
