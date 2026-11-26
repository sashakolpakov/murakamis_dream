# A complete contour envelope beside the first cap on the actual taper

Research deduction, 7 November 2026. The adjoining ordinary conditional
factor has a complete finite-source upper bound on the enlarged actual
first-attached taper. Its central contour keeps the original reference
index height; it does not require a moving-root packet. Both horizontal
aliases have strict pointwise reserves, every vertical alias is paid by
a real cut, and the zero-mode joins are controlled by height convexity.
The remaining rates are one strictly concave fixed-height maximum and
a finite, exhaustive list of physical-tail values.

Multiplication by the completed first-cap envelope gives a bound for the
literal joint source at the same actual retained targets. No comparison
of that bound with the calibrated boundary plane is asserted.

## 1. Actual targets, allocation and the fixed reference line

Write the first and second types as \(3+\alpha,3+\epsilon\), where
\(\alpha,\epsilon\in\{0,1\}\). Consider unselected targets
\[
 a=x+ih_a,\quad b=z+ih_b,\qquad
 .1\le x\le .22,\quad .1\le z\le .5,
 \tag{1}
\]
with their actual minimum-cutoff heights from
[first-attached eligibility](research_mixed_first_attached_taper_root_eligibility.md).
In particular,
\[
 -.108\le h_a\le .021,\qquad -.102\le h_b\le .068,
 \tag{2}
\]
and an outer coordinate of type four has nonpositive height. The same
theorem proves
\[
 \Re\cot\pi a,\Re\cot\pi b\ge0,\qquad
 |\Im\cot\pi a|,|\Im\cot\pi b|<1.
 \tag{3}
\]
Equality in the real part can occur only at the real half endpoint.
The exact coupled height restrictions of that theorem remain in force;
the independent box (2) alone is not substituted for (3).

Let \(h_0\) be the original reference height of the ordinary index.
Its full typed image bounds imply
\[
                    -.108\le h_0\le .068.
 \tag{4}
\]
The comparisons below hold for any fixed \(h_0\) in (4). Use the original
primitive, chirp and unselected allocation:
\[
 \begin{split}
 Q_\epsilon(s;a,b)&=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias,\\
 F_{\alpha\epsilon}(s;a,b)
 &=Q_\epsilon(s;a,b)-(1+\alpha/2)g(a)-(1+\epsilon/2)g(b).
 \end{split}
 \tag{5}
\]
Put
\[
 I=[1/5,49/100],\qquad
 B_{\alpha\epsilon}^{\,0}(a,b;h_0)
       =\max_{v\in I}\Re F_{\alpha\epsilon}(v+ih_0;a,b).
 \tag{6}
\]
The superscript \(0\) denotes this fixed-line bound, not a zero-height
reset. It is not silently identified with the moving critical action.
The finite factor below is exactly the source of the
[low-row theorem](research_mixed_first_attached_low_row_transport.md):
with \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\) and
\(p_j(X)=(rX;r)_j\),
\[
 C_{\epsilon,N}(X,Y)
       =\sum_{j=0}^{N-1}X^{-j}
                     \frac{p_j(X)p_j(Y)}{P_j^{2+\epsilon}}.
 \tag{6a}
\]
No marked-factorial prefactor belongs to this definition.

## 2. Both aliases are paid on the entire enlarged target domain

For \(0<t<1\) and finite real \(y\), let
\[
 A(t,y)=\arg(1-e^{2\pi y-2\pi it})
\]
on the original logarithmic lift. The exact radial argument inequalities
from [the original alias proof](research_mixed_horizontal_alias_transport.md)
give
\[
 \pi\min(1-2t,0)\le A(t,y)\le\pi\max(1-2t,0).
 \tag{7}
\]
They are strict away from \(t=1/2\) at every finite radius.
For \(v\in I\), every unshifted and shifted real argument is strictly
between zero and one, even when \(z=1/2\). Consequently
\[
 \Im Q_{\epsilon,s}
 =A(v+x,y+h_a)+A(v+z,y+h_b)
                  -(2+\epsilon)A(v,y)+2\pi x.
 \tag{8}
\]

**Lemma 1.** On (1)--(2), for every \(v\in I\) and every finite \(y\),
\[
                         -2\pi<\Im Q_{\epsilon,s}<\pi .
 \tag{9}
\]

For the upper bound, drop the negative own term and bound (8), divided
by \(\pi\), by
\[
 \max(1-2v,2x)+(1-2v-2z)_+\le\frac35+\frac25=1.
\]
The negative own term is strictly negative. For the lower bound it
suffices to take \(\epsilon=1\). According to the positions of the
two shifted real arguments relative to \(1/2\), the four lower
expressions and their bounds are
\[
 \begin{array}{c|c|c}
 v+x&v+z&\text{lower expression}\\ \hline
 \ge1/2&\ge1/2&-1+2v-2z\ge-8/5\\
 <1/2&\ge1/2&-2+4v+2x-2z\ge-2\\
 \ge1/2&<1/2&-2+4v\ge-6/5\\
 <1/2&<1/2&-3+6v+2x\ge-8/5 .
 \end{array}
 \tag{10}
\]
The own argument in (8) makes the lower inequality strict also at
the limiting case of the second row. This proves (9).

Take the fixed lower and upper alias heights to be \(-1/5\) and \(2\).
Since \(\partial_y\Re F=-\Im Q_{\epsilon,s}\), (9) first gives
\[
 \Re F(v-i/5;a,b)-2\pi/5
 <\Re F(v+ih_0;a,b)-\frac{33\pi}{250}
 <\Re F(v+ih_0;a,b)-\frac13 .
 \tag{11}
\]
Here \(h_0+1/5\le67/250\).

For the taller upper alias retain the sharper limiting argument.
If \(y\ge1/2\), the two shifted inverse radii are less than
\(2e^{-2\pi y}<1/8\), because \(e^{.216\pi}<2\) and
\(e^\pi>20\). These elementary exponential bounds are already
proved in the first-cap and original alias notes. Using
\(|\Log(1-w)|\le(8/7)|w|\) on \(|w|\le1/8\) in the original
large-radius argument identity gives
\[
 \left|\Im Q_{\epsilon,s}
        -\pi\{-\epsilon+2\epsilon v-2z\}\right|
                         <8e^{-2\pi y}.
 \tag{12}
\]
There are two shifted terms of inverse radius at most
\(2e^{-2\pi y}\) and at most three own terms of radius
\(e^{-2\pi y}\); hence the coefficient \(8\) in (12).
The limiting expression is at least \(-8\pi/5\).
Integrate (9) from \(h_0\) to \(1/2\), and (12) from \(1/2\) to \(2\).
The entire exponential remainder is less than
\[
              \int_{1/2}^{\infty}8e^{-2\pi y}\,dy
                   =\frac4\pi e^{-\pi}<\frac1{15}.
\]
Subtracting the upper penalty \(4\pi\) yields
\[
 \begin{split}
 \Re F(v+2i;a,b)-4\pi-\Re F(v+ih_0;a,b)
 &<-\frac{48\pi}{125}+\frac1{15}\\
 &<-\frac{407}{375}<-1.
 \end{split}
 \tag{13}
\]
All outer allocations are constant during these comparisons, so
(11)--(13) hold for precisely (5).

On each half of a vertical side, (9) also gives
\[
 \begin{split}
 \partial_y\{\Re F(c+iy)-2\pi y\}&<0,\qquad &&y\ge0,\\
 \partial_y\{\Re F(c+iy)+2\pi y\}&>0,\qquad &&y\le0.
 \end{split}
 \tag{14}
\]
Thus every vertical alias is bounded by its own real-cut rate.
This does not need a high-strip curvature estimate.

## 3. Concavity of the fixed line and payment of its two joins

On \(v\in I\), \(|y|\le.108\), the inner cotangent has positive real
part and imaginary part of modulus less than one. Indeed
\[
 \cos(2\pi v)\le\cos(2\pi/5)<\frac13
                    <\frac12<e^{-.216\pi}
\]
is the exact cotangent criterion when its cosine is positive;
negative cosine gives the conclusion immediately. Together with (3),
the original
[triangle determinant](research_mixed_plateau_accretivity.md)
therefore makes both pair forms strictly accretive. The closed
outer half endpoint is permitted, as in the closed-boundary
argument of first-attached eligibility. In particular
\[
                 -\Re Q_{\epsilon,ss}(v+iy;a,b)>0.
 \tag{15}
\]
One can also read this directly from
\(Q_\epsilon=V(s,a)+V(s,b)-\epsilon g(s)+g(a)+g(b)+2\pi ias\);
the extra own term has nonnegative negative-real curvature.
On any compact actual parameter family the floor in (15) is uniform.

It follows that (6) is a strictly concave one-dimensional maximum.
It is attained at an endpoint or at the unique interior zero of
\(\Re Q_{\epsilon,s}(v+ih_0;a,b)\). No such zero is selected or
evaluated in this theorem.

For either real cut \(c\in\{1/5,49/100\}\), holomorphy and (15)
make \(y\mapsto\Re F(c+iy;a,b)\) convex between zero and \(h_0\).
Every zero-mode join is consequently bounded by
\[
        \max\{\Re F(c;a,b),B_{\alpha\epsilon}^{\,0}(a,b;h_0)\}.
 \tag{16}
\]
This is convexity of the original phase, not of a finite sum's
logarithmic modulus.

## 4. The exhaustive real-tail profiles

Let
\[
 \begin{split}
 \mathcal R_{\alpha\epsilon}(u;a,b)
 ={}&\int_0^u\log|1-e^{-2\pi i(a+t)}|\,dt
       +\int_0^u\log|1-e^{-2\pi i(b+t)}|\,dt\\
 &-(2+\epsilon)J(u)-2\pi h_a u
                  -\frac\alpha2\Re g(a)-\frac\epsilon2\Re g(b).
 \end{split}
 \tag{17}
\]
All wrapped, endpoint and revived physical rows are retained.
The [exact low-tail theorem](research_mixed_first_attached_low_row_transport.md)
pays their entire interval \(0\le u\le1/5\) by its cut value.
At each regular cut, (17) equals \(\Re F(c;a,b)\).
The true last-row value is exactly
\[
 \mathcal R_{\alpha\epsilon}(1;a,b)
 =2\pi(-h_a)_++2\pi(h_b)_+
                     -\frac\alpha2\Re g(a)-\frac\epsilon2\Re g(b).
 \tag{18}
\]

The old high-tail stationary equation remains exact on this new target
domain, since its derivation is the literal sine identity. Set
\[
 \begin{split}
 P_{a,b,\epsilon}(w)
 ={}&4^{-\epsilon}e^{2\pi(h_b-h_a)}
       |\cos\pi a-w\sin\pi a|^2
       |\cos\pi b-w\sin\pi b|^2(1+w^2)^\epsilon-1 .
 \end{split}
 \tag{19}
\]
For real \(w\), this is a real polynomial of degree \(4+2\epsilon\),
with positive leading coefficient. At \(w=-\cot\pi u\) it equals
\(e^{2\mathcal R'_{\alpha\epsilon}(u)}-1\), away from numerator
zeros. The argument in Section 3 of
[the original contour-allowance lemma](research_mixed_conditional_contour_allowance.md)
therefore proves that the high-tail maximum is attained at \(49/100\),
at \(1\), or at one of **all** real roots of (19) corresponding to
\(49/100<u<1\). A numerator-zero wall is not a missing maximum:
the derivative tends to \(-\infty\) on both sides and the rate decreases
through it. Coincident zeros have the same property.

Let \(T_{\alpha\epsilon}(a,b)\) be the maximum of the \(1/5\) cut,
these two high-tail endpoints, and every admissible critical value
just specified. There are at most \(7+2\epsilon\) values. This is
an exact finite list; no polynomial root or profile is evaluated or
discarded here.

## 5. The complete finite conditional and joint-cap conclusions

**Theorem.** For every prescribed \(\tau>0\), uniformly on the
compact actual first-attached target families (1)--(4), at sufficiently
large levels of either parity,
\[
 \begin{split}
 &|C_{\epsilon,N}(e^{-2\pi ia},e^{-2\pi ib})|\,
    |d_N(e^{-2\pi ia})|^{\alpha/2}
    |d_N(e^{-2\pi ib})|^{\epsilon/2}\\
 &\qquad\le C_\tau N^{A_\tau}
   \exp N\left\{
       \max\big(B_{\alpha\epsilon}^{\,0}(a,b;h_0),
                          T_{\alpha\epsilon}(a,b)\big)+\tau\right\}.
 \end{split}
 \tag{20}
\]

*Proof.* Split the original finite sum at half-grid cuts tending to
\(1/5\) and \(49/100\). The new exact low-tail theorem bounds all
rows before the first cut at constant cost. The original uniform
zero-safe finite-product estimate bounds all high physical rows by
(17). Its proof applies to the present compact outer domain:
numerator logarithmic zeros are integrable, their positive
regularizations converge uniformly, and the denominator has its
unchanged \(O(\log N)\) endpoint error.

For the central rows use the original marked factorial interpolation
and its exact cotangent trace on heights \(-1/5,2\). Every factorial
real argument stays in a compact subset of \((0,1)\), since
\[
 .2\le\Re s\le.49,\quad .3\le\Re(s+a)\le.71,\quad
                         .3\le\Re(s+b)\le.99 .
\]
The original factorial theorem has no restriction on a fixed finite
imaginary height. Thus the tall contour is legal, without new
interpolation poles or an off-grid replacement.

The cotangent constants give exactly the original \(+N\) zero mode.
Move it to the fixed reference height \(h_0\), retaining both joins.
Equations (6), (11), (13), (14) and (16) control every resulting
current by the maximum in (20). Both horizontal aliases and every
half-grid vertical side remain included. Strict bounds and continuity
absorb the \(O(1/N)\) cut shifts; all lengths and original symbols cost
only polynomial factors.

For each type-four outer argument its unselected height is nonpositive
and its real part is at most \(1/2\). The original absolute Fourier
bound has rate \(-\Re g\), including height zero and the half endpoint.
Multiply by its allocated halfweight; no finite Fourier value is
divided out. One aggregate source tolerance completes (20).
\(\square\)

Let \(\mathcal C_\alpha(a,\vartheta)\) be the **ungauged** allocated
cap envelope from
[complete early-cap transport](research_mixed_cap_early_taper_envelope_transport.md):
\[
 \begin{split}
 \mathcal C_1&=A^{\rm real}_1(a)-\tfrac12\Re g(a)
                       -c_1(1-\cos\vartheta),\\
 \mathcal C_0&=\max\{A^{\rm real}_0(a)-c_0(1-\cos\vartheta),
                                      E_{\rm end}(h_a)\}.
 \end{split}
 \tag{21}
\]
Here the literal bare cap is denoted \(U_{\alpha,N}\), with its
original ordinary-color parameter \(\vartheta\). Multiplying its
complete source bound by (20) proves
\[
 \begin{split}
 &|U_{\alpha,N}\,
       C_{\epsilon,N}(e^{-2\pi ia},e^{-2\pi ib})|\,
       |d_N(e^{-2\pi ia})|^\alpha
       |d_N(e^{-2\pi ib})|^{\epsilon/2}\\
 &\qquad\le C_\tau N^{A_\tau}\exp N\left\{
    \mathcal C_\alpha(a,\vartheta)
       +\max(B_{\alpha\epsilon}^{\,0}(a,b;h_0),
                           T_{\alpha\epsilon}(a,b))+\tau\right\}.
 \end{split}
 \tag{22}
\]
Each first-coordinate halfweight is used exactly once. The cap's true
endpoint branch remains in (21) when required; its own-four dominance
uses the actual reference theorem, not a discarded finite term.
All ordinary real colors and inherited fixed color jets have the
scope of that cap theorem. No transverse parameter-derivative claim
is deduced merely from an upper bound on the taper.

This is a whole finite-source bound for the joint block on the
enlarged actual targets. It leaves explicit phase comparisons, rather
than an unproved conditional-packet assumption. In using (22) for the
compensated left boundary, one must still compare its same-target
profiles with the original calibrated action and marginals, retaining
the moving neighboring height, middle energy and relative pinning fee.
Neither \(B^0\) nor the physical cuts are asserted to equal or lie below
that calibrated plane. No whole-boundary sign follows here.
