# An asymmetric contour for horizontal boundary transport

Research deduction, 5 November 2026. Keep the original conditional
index contour, but put its lower side at height \(-1/5\) and its
upper side at height \(1\). On the whole real plateau, both
horizontal aliases are below the fixed-reference zero-mode supporting
plane. Every vertical alias is bounded by its corresponding real cut,
and the zero-mode joins are bounded by their endpoints. Thus the
remaining complete-source comparison is precisely a bound on the full
real-row tails. No moving root, numerical cover, or new finite
interpolation is used.

## 1. The fixed-reference setting

Use the actual reference and allocation of the
[zero-mode theorem](research_mixed_horizontal_zero_mode_support.md)
and the [shorter alias lemma](research_mixed_horizontal_alias_transport.md):
\[
 \begin{split}
 a=x+ih_a,\quad b=z+ih_b,\quad
 x,z\in[11/50,9/20],\quad |h_a|,|h_b|\le3/25,\\
 F(s;a,b)=g(s+a)+g(s+b)-(2+\epsilon)g(s)
 -(1+\eta/2)g(a)-(1+\epsilon/2)g(b)+2\pi ias,\\
 \eta,\epsilon\in\{0,1\},\qquad
 \ell=3/20,\quad r=49/100,\quad
 -27/250\le y_0=\Im s_0\le17/250.
 \end{split}
 \tag{1}
\]
The outer imaginary parts remain their actual unselected reference
heights. In particular every type-four outer coordinate has negative
height and retains its factorial Fourier upper branch. The phase
derivations allow the displayed larger height box, but the finite
conclusion keeps this stated Fourier allocation.

Write \(M=\Re F(s_0;a_0,b_0)\), let \(p_a,p_b\) be its
original allocated real marginals, and put
\[
 \begin{split}
 d_a=x-\Re a_0,\quad d_b=z-\Re b_0,\qquad
 B(a,b)=M+p_ad_a+p_bd_b-\frac{d_a^2+d_b^2}{2500000}.
 \end{split}
 \tag{2}
\]
The fixed-reference zero-mode theorem proves
\(\Re F(v+iy_0;a,b)\le B(a,b)\) for every
\(v\in[\ell,r]\). The actual reference, its original index
equation, and its two marginals are unchanged throughout this note.

## 2. Argument bounds at every index height

Let \(Q_\epsilon=F+(1+\eta/2)g(a)+(1+\epsilon/2)g(b)\).
The original regular-strip argument inequalities in the shorter lemma
hold at every finite imaginary height. They give
\[
            -\frac{93\pi}{50}
             <\Im Q_{\epsilon,s}(v+iy;a,b)
             <\frac{29\pi}{25}
       \qquad(\ell\le v\le r,\ y\in\mathbb R).
 \tag{3}
\]
The upper bound is equation (5) there. For the lower bound it is enough
to take \(\epsilon=1\), because the original own argument is
positive. According to whether \(v+x\) and \(v+z\) are
above or below \(1/2\), the same elementary argument bounds give,
after division by \(\pi\), respectively
\[
 \begin{array}{c|c}
 (v+x,v+z)&\text{lower bound}\\ \hline
 (\ge1/2,\ge1/2)&-1+2v-2z\ge-8/5\\
 (<1/2,\ge1/2)&-2+4v+2x-2z\ge-93/50\\
 (\ge1/2,<1/2)&-2+4v\ge-7/5\\
 (<1/2,<1/2)&-3+6v+2x\ge-83/50.
 \end{array}
 \tag{4}
\]
The strictness follows from the finite-radius own-argument estimate.

For \(y\ge1/2\), there is a sharper estimate. If
\(0<t<1\), then on the original lift
\[
 \arg(1-e^{2\pi(y+h)-2\pi it})
 =\pi(1-2t)+\arg(1-e^{-2\pi(y+h)+2\pi it}).
 \tag{5}
\]
All inverse radii here are less than \(1/8\), because
\(y+h\ge.38\). For \(|w|\le1/8\),
\(|\operatorname{Log}(1-w)|\le(8/7)|w|\). Also
\(e^{.24\pi}<9/4\). Applying these estimates to the two
shifted arguments and the at most three own arguments yields
\[
 \left|\Im Q_{\epsilon,s}
       -\pi\{-\epsilon+2\epsilon v-2z\}\right|
 <\frac{60}{7}e^{-2\pi y}.
 \tag{6}
\]
The limiting expression is at least \(-8\pi/5\) for either
own type. Thus
\[
          -\Im Q_{\epsilon,s}
            <\frac{8\pi}{5}+\frac{60}{7}e^{-2\pi y},
                  \qquad y\ge1/2.
 \tag{7}
\]
All auxiliary comparisons are elementary. For example
\(.24\pi<19/25\) and
\(e^t\le1+t+t^2/[2(1-t/3)]\) prove \(e^{.24\pi}<9/4\).
The positive exponential series gives \(e^{.76\pi}>8\) and
\(e^\pi>20\), using \(\pi>3\). These justify the inverse-radius
bound and the integral estimate below without a numerical test.

## 3. Both horizontal aliases are below the fixed line

The lower side is unchanged. Equation (8) of the shorter alias lemma
gives
\[
 \Re F(v-i/5;a,b)-2\pi/5
 \le\Re F(v+iy_0;a,b)-\frac{557\pi}{6250}
 \le B(a,b)-\frac{557\pi}{6250}.
 \tag{8}
\]
For the upper side, integrate
\(\partial_y\Re F=-\Im Q_{\epsilon,s}\) from \(y_0\)
to \(1/2\) using (3), and from \(1/2\) to \(1\)
using (7). The first cost is at most
\((93/50)(1/2+27/250)\pi=(3534/3125)\pi\).
The second constant cost is \(4\pi/5\), and its entire
exponentially decaying error is less than
\[
 \int_{1/2}^{\infty}\frac{60}{7}e^{-2\pi y}\,dy
 =\frac{30}{7\pi}e^{-\pi}<\frac1{14}.
 \tag{9}
\]
Subtracting the upper-alias penalty \(2\pi\) gives
\[
 \begin{split}
 \Re F(v+i;a,b)-2\pi-\Re F(v+iy_0;a,b)
 &<-\frac{216\pi}{3125}+\frac1{14}<-\frac{13}{100},\\
 \Re F(v+i;a,b)-2\pi&<B(a,b)-\frac{13}{100}.
 \end{split}
 \tag{10}
\]
The last rational comparison follows already from \(\pi>3\).
Both bounds preserve the original two supporting marginals and the
outer quadratic loss in (2).

## 4. The vertical pieces and the exact interpolation

For any real cut \(c\in\{\ell,r\}\), (3) implies
\[
 \begin{split}
 \frac d{dy}\{\Re F(c+iy)-2\pi y\}&<-7\pi/50,
                                      &&y\ge0,\\
 \frac d{dy}\{\Re F(c+iy)+2\pi y\}&>21\pi/25,
                                      &&y\le0.
 \end{split}
 \tag{11}
\]
Consequently every upper and lower half-grid vertical alias is bounded
by the allocated rate at its corresponding real cut. This argument
works up to the new upper height one; no unproved high-strip curvature
estimate is used.

The zero-mode joins run only between height zero and \(y_0\).
They lie in the index rectangle of the zero-mode theorem, where
\(-\Re F_{ss}>0\). Holomorphy therefore makes
\(y\mapsto\Re F(c+iy)\) convex. Each join is bounded by
\[
                \max\{\Re F(c;a,b),B(a,b)\}.
 \tag{12}
\]

The taller contour is legal for the *original* finite sum.
Section 4 of the
[exact factorial interpolation theorem](exact_factorial_interpolation_and_complex_contours.md)
gives its uniform expansion on every fixed compact subset of
\(0<\Re w<1\), without an imaginary-height restriction. On
\([\ell,r]+i[-1/5,1]\), the real parts of all factorial
arguments \(s,s+a,s+b,a,b\) stay strictly inside that strip.
The marked factorials remain holomorphic and nonzero, so no new
interpolation poles are crossed. The same exact cotangent residue
formula encloses precisely the original central rows between the two
half-grid cuts. Its constant modes still combine to \(+N\) times
the real central integral. Its horizontal nonconstant modes have
penalties \(2\pi/5\) and \(2\pi\), and its vertical modes
have penalty \(2\pi|y|\). All currents, both orientations of
the boundary, and both level parities remain present.

Deform only the zero-mode real integral to the fixed height \(y_0\).
The preceding bounds control that line, both joins, both horizontal
aliases, and all vertical aliases. Uniform factorial symbols and
half-grid rounding contribute only a polynomial and one arbitrarily
small rate tolerance on this fixed compact family.

## 5. The remaining full real-row inequality

For clarity the exact allocated real-row rate is
\[
 \begin{split}
 \mathcal R_\epsilon(u;a,b)
 ={}&\int_0^u\log|1-e^{-2\pi i(a+t)}|\,dt
     +\int_0^u\log|1-e^{-2\pi i(b+t)}|\,dt\\
 &-(2+\epsilon)J(u)-2\pi u\Im a
       -\tfrac\eta2\Re g(a)-\tfrac\epsilon2\Re g(b),\\
 T(a,b)&=\max_{u\in[0,\ell]\cup[r,1]}
                              \mathcal R_\epsilon(u;a,b).
 \end{split}
 \tag{13}
\]
The full row interval includes all revived and endpoint rows, with
integrable zeros interpreted by continuity. At either cut it equals
\(\Re F(c;a,b)\), since all shifted cut arguments remain in
the original strip. Thus the cut rates in (11)--(12) are included
in \(T\).

**Complete-contour upper bound.** For every prescribed \(\tau>0\),
uniformly over the fixed actual-reference family and its horizontal
plateau changes, the literal conditional kernel with its two allocated
unselected Fourier halfweights obeys
\[
 |C_{\epsilon,N}(e^{-2\pi ia},e^{-2\pi ib})|
 |d_N(e^{-2\pi ia})|^{\eta/2}|d_N(e^{-2\pi ib})|^{\epsilon/2}
 \le C_\tau N^A
       \exp N\{\max(B(a,b),T(a,b))+\tau\}.
 \tag{14}
\]
The uniform zero-safe product bound controls the at most \(N\)
real tail rows in (13); Sections 3--4 control every central current.
Taking their maximum and assigning the one total tolerance proves
(14). There is no division by a finite Fourier value or assumption
that an off-grid row vanishes.

Equivalently, with \(D(a,b)=[T(a,b)-B(a,b)]_+\), the exponent
is \(B+D+\tau\). This is an upper bound on the stated real
horizontal family with fixed actual heights. It does not by itself
give derivatives transverse to that family. Such derivatives require
the same source bound on an ambient complex neighborhood before
applying Cauchy's estimate. Conditional factors have no ordinary-color
argument of their own; ordinary-color derivatives in a larger product
retain the independently proved cap or endpoint neighborhood and its
allocated tolerance.

In particular the missing horizontal supporting-plane theorem is now
reduced to \(T(a,b)\le B(a,b)\), or to an explicit allowed
excess that is paid by a specified boundary reserve. No such uniform
tail inequality is asserted here. A constant excess per edge cannot
be silently accumulated over an arbitrary long chain. This note
does not prove global open-source dominance or a new knot-family
statement.

## 6. A finite explicit candidate set for the real tails

The left tail reduces to its real cut on the full plateau, not only
on the narrower old rectangle. Direct differentiation of (13) gives
\[
 \begin{split}
 \mathcal R_\epsilon'(u)
 ={}&\log\left|\frac{\sin\pi(u+a)}{\sin\pi u}\right|
    +\log\left|\frac{\sin\pi(u+b)}{\sin\pi u}\right|\\
 &-\epsilon\log(2\sin\pi u)+\pi(h_b-h_a).
 \end{split}
 \tag{15}
\]
For \(0<u\le3/20\), each sine ratio has modulus greater than
two. An imaginary shift only increases the numerator modulus. For
real \(x\in[.22,.45]\), the ratio decreases with \(u\),
since it is \(\cos\pi x+\cot\pi u\sin\pi x\). Its
minimum in \(x\) is at an endpoint, by concavity of the positive
sine on this interval. The remaining endpoint comparisons are
\[
 \sin(37\pi/100)>91/100>2\sin(3\pi/20),\qquad
 \sin(3\pi/5)>91/100.
 \tag{16}
\]
For an elementary rational verification, use \(157/50<\pi<22/7\).
The alternating lower sine polynomial through degree seven at
\(5809/5000\), the upper polynomial through degree five at
\(33/70\), and the lower polynomial through degree three at
\(157/125\) give the three comparisons in (16), respectively;
the last uses \(\sin(3\pi/5)=\sin(2\pi/5)\).
Also \(2\sin\pi u<1\) here. Thus
\[
       \mathcal R_\epsilon'(u)>
              \log4-.24\pi>\frac12,
                 \qquad 0<u\le3/20.
 \tag{17}
\]
The final inequality uses \(\log4>4/3\) and \(\pi<22/7\).
Consequently the left-tail maximum is its value at \(\ell\).

For the right tail use the exact polynomial from Section 3 of the
[allowed-rate contour lemma](research_mixed_conditional_contour_allowance.md):
\[
 \begin{split}
 p_{a,b,\epsilon}(w)={}&4^{-\epsilon}
 e^{2\pi(h_b-h_a)}
 |\cos\pi a-w\sin\pi a|^2
 |\cos\pi b-w\sin\pi b|^2(1+w^2)^\epsilon-1.
 \end{split}
 \tag{18}
\]
Its derivation is the literal sine identity in (15), so it remains
valid on the full plateau. For real \(w\) it is a real polynomial
of degree \(4+2\epsilon\), with strictly positive leading
coefficient. At \(w=-\cot\pi u\), it equals
\(e^{2\mathcal R_\epsilon'(u)}-1\) away from numerator-zero
walls. The allocated outer halfweights are constant in \(u\)
and do not change this identity.

Every interior maximum on \((r,1)\) is therefore a real root of
(18) with \(w>-\cot\pi r\). At a numerator-zero wall,
the affected logarithm tends to \(-\infty\) from both sides,
while the other terms in (15) are bounded above locally. The rate
strictly decreases across that wall; it is not a missing maximum.
The continuous endpoint value at \(u=1\) is explicitly
\[
 \mathcal R_\epsilon(1;a,b)
 =2\pi(-h_a)_++2\pi(h_b)_+
       -\tfrac\eta2\Re g(a)-\tfrac\epsilon2\Re g(b).
 \tag{19}
\]

Hence \(T(a,b)\) is exactly the maximum of the two real-cut
values, (19), and the values at **all** admissible real roots of
(18). There are at most four such roots for type three and six
for type four, so at most seven or nine candidate values in total.
This does not select a convenient stationary branch or drop a revived
row. The coefficients still retain the actual fixed heights and
horizontal targets; no independent reference relaxation or sign of
\(T-B\) is asserted. Equations (13), (18), and (19) turn the
remaining source obligation into a finite explicit variational test.
