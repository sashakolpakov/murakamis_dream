# Complete endpoint continuation to a deeper private rectangle

Research deduction, 7 November 2026. The complete original endpoint
packet extends from private depth \(11/200\) to depth \(3/50\),
with the same real interval \([27/100,49/100]\). The proof transports
the already proved real-cut gaps, uses the new full real-row bounds,
and retains both finite aliases when the auxiliary critical height
changes sign.

This is a complete endpoint-coefficient theorem. It does not cover
private real parts below \(27/100\), enclose the continued outer-cap
path in the new rectangle, or estimate the entire outer cap.
No numerical evaluation, source replay, or frozen-note edit is used.

## 1. Exact function and the enlarged statement

Keep the specified finite continuation
\[
 C_N(e,w)=\sum_{l=0}^{N-1}
       \frac{e^{i\pi e l}e_l(w)}
                         {S_lG_N(Ne-l)},\qquad
 S_l=\prod_{j=1}^{l}2\sin(\pi j/N).                            \tag{1}
\]
Every Newton polynomial and canonical factorial is the original
one. In particular all terms \(l>\Re(Ne)\) remain at complex
indices; physical reciprocal-factorial zeros do not delete them
from (1).

At \(w=-2\), use
\[
 \begin{split}
 F(e,u)&=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu,\\
 S(e)&=F(e,u_c(e)).
 \end{split}                                                   \tag{2}
\]
The original critical branch, logarithmic lift, and additive
constant are those proved in
[the bridge phase theorem](research_mixed_endpoint_bridge_phase_floor.md).
For the new part of the domain write
\[
 e=E-i\eta,\qquad
 \mathcal E_-=[27/100,49/100]+i[-3/50,0],
 \qquad a=1/20,\quad b(E)=E-1/100.                             \tag{3}
\]

**Theorem.** On a fixed complex neighborhood of
\[
       \bigl([27/100,49/100]+i[-3/50,1/25]\bigr)\times\{-2\},
                                                                  \tag{4}
\]
the whole function (1) has the original packet
\[
        C_N(e,w)=N^{-3/2}A(e,w)e^{NS(e,w)}
                             (1+O_{\rm hol}(N^{-1})),
                 \qquad A(e,w)\ne0 .                          \tag{5}
\]
Both level parities and all fixed joint ordinary-color/index
derivatives are included on smaller neighborhoods. The phase,
symbol and accretive Gaussian square root agree with the original
endpoint theorem on the overlap. No new normalizing scalar is
introduced.

The positive-height part of (4) is already proved by
[the original cap rectangle theorem](research_mixed_endpoint_cap_rectangle.md).
It remains to prove (5) on \(\mathcal E_-\).

## 2. Transport of the exact old real-cut comparisons

Equation (10) of the original cap rectangle theorem proves on
the entire old rectangle, for exactly the cuts in (3),
\[
 \Re S(e)-\Re F(e,a)>1/5,\qquad
                    \Re S(e)-\Re F(e,b(E))>1/50.              \tag{6}
\]
Those are whole-rectangle certified inequalities, not isolated
sample values. Their stated range includes every
\(E\in[.27,.49]\) at \(\eta=11/200\). No certificate is
replayed here.

The bridge phase theorem proves throughout the larger strip
\[
 0<\Re u_c<E<1/2,\quad F_u(e,u_c)=0,\quad
                         \partial_\eta\Re S(E-i\eta)>0.       \tag{7}
\]
For fixed \(E\), either real cut \(r=a\) or \(r=b(E)\) is
held fixed during the height transport. Directly from (2),
\[
 \partial_\eta\Re F(E-i\eta,r)
                  =-\Arg\sin\pi(E-r-i\eta)+\pi r<\pi,        \tag{8}
\]
because \(0<E-r<1/2\) and \(0<r<1/2\).
Thus each cut gap in (6) can decrease by less than
\(\pi/200\) when \(\eta\) moves from \(11/200\) to \(3/50\).
Throughout \(\mathcal E_-\),
\[
 \boxed{\quad
  \Re S(e)-\Re F(e,a)>3/700,\qquad
  \Re S(e)-\Re F(e,b(E))>3/700.
 \quad}                                                       \tag{9}
\]
Indeed \(1/50-\pi/200>1/50-11/700=3/700\).
The left gap starts larger, and the already proved old part
has the larger margins (6).

These comparisons also keep the actual critical point between
the real cuts. On \(0<\Re u<E<1/2\), at every finite height,
\[
 -\Re F_{uu}(e,u)=
 \pi\Re\{2\tan\pi u+3\cot\pi u+\cot\pi(e-u)\}>0.              \tag{10}
\]
For fixed \(E\), the original critical point lies between the
cuts at \(\eta=11/200\). Suppose its real part first reaches
one of the cuts in the new height interval. Along that
vertical line, (10) gives strict convexity of \(\Re F\) as
a function of the auxiliary height. Since \(F_u=0\) at
the critical point, that height is its minimum. The value
at height zero would therefore be at least \(\Re S(e)\),
contradicting (9). Hence
\[
                         a<\Re u_c(e)<b(E)                   \tag{11}
\]
on the whole new rectangle. Compactness supplies uniform
positive separations from both cuts. No positive sign of
\(\Im u_c(e)\) is required or asserted.

## 3. Every omitted physical and revived row is paid

The [bridge real-tail theorem](research_mixed_endpoint_bridge_real_tails.md)
applies throughout \(\mathcal E_-\). Its exact zero-safe
rate reduces all rows \(0\le l/N\le a\) and
\(b(E)\le l/N\le1/2\) to the two cut values in (9).
It bounds every row \(l/N\ge1/2\) by the rate \(67/105\).
The bridge phase theorem proves
\[
                 \Re S(e)>1511/2000,\qquad
                 1511/2000-67/105>1/10.                    \tag{12}
\]
Thus every original row outside the retained real interval
has a fixed positive own-action gap, uniformly on
\(\mathcal E_-\). This includes all revived rows beyond
the noninteger private endpoint, both parities, the odd
Newton zero and every reflected reciprocal zero. The carrier
\(e^{i\pi e l}\) and the full normalization (1) have already
been included in those tail rates.

The finite row sums cost only polynomial factors. The same
source bounds hold for each fixed ordinary derivative at
complete color. Their original uniform Newton upper
bounds preserve the strict gaps on sufficiently small fixed
ordinary-color neighborhoods, after one prescribed allowance.

## 4. Both signs of critical height in the finite contour

For a fixed base \(e\in\mathcal E_-\), put
\[
             h_c=\Im u_c(e),\qquad
             f_e(x,h)=\Re F(e,x+ih).
 \]
By (10)--(11), the horizontal line through \(u_c\) has its
unique nondegenerate maximum at that point, with value
\(\Re S(e)\). Its two cut endpoints have strict gaps.

The exact reflection calculation behind equation (11) of
the old rectangle theorem gives, for \(H\ge0\),
\[
 f_e(x,-H)-f_e(x,H)
    =2\pi E H+
       \int_{-H}^{H}\Im J'(e-x+it)\,dt .                      \tag{13}
\]
Throughout the retained real interval,
\(0<E-x<1/2\). The sine logarithm in (13) has argument
between \(-\pi/2\) and \(\pi/2\), regardless of height.
Consequently
\[
 \left|f_e(x,-H)-f_e(x,H)-2\pi EH\right|\le\pi H.             \tag{14}
\]
This estimate retains the original logarithmic lift and
does not require real \(e\).

If \(h_c=H>0\), take symmetric outer heights \(\pm H\).
The upper line is the main line. Its weighted alias loses
\(2\pi H\), and (14) gives on the lower weighted alias
\[
            f_e(x,-H)-2\pi H
                  \le\Re S(e)-\pi(1-2E)H.                  \tag{15}
\]
The loss is positive since \(E\le49/100<1/2\).

If \(h_c=-H<0\), the lower line is instead the main line.
Its weighted alias again loses \(2\pi H\). The other
direction of (14), essential in this case, gives
\[
            f_e(x,H)-2\pi H
                  \le\Re S(e)-\pi(1+2E)H.                  \tag{16}
\]
Thus both horizontal aliases are strictly paid for either
nonzero sign. This is not an application of the old
positive-height criterion to a negative-height saddle.

The whole vertical alias sides are retained. On each of
their sign halves the rate is a convex function of the
height minus its exact linear alias penalty. Its maximum
is therefore at its real or horizontal endpoint. The real
cut bounds are (9); the horizontal weighted endpoints are
paid by (15) or (16). Every such side is paid.
The unweighted connectors from the real path to the chosen
main line are also retained. Vertical convexity bounds
them by the real cut and the cut point on that main line;
both have strict own-action gaps.

For \(h_c=0\), a separate finite rectangle is needed.
On the retained real segment,
\[
 \Im F_u(e,x)=\Arg\sin\pi(e-x)+\pi E
                              \in(-\pi/2,\pi/2).              \tag{17}
\]
The real path passes through the critical point and is
strictly concave. Choose a fixed sufficiently small
\(\epsilon>0\) so that on
\([a,b(E)]+i[-\epsilon,\epsilon]\) one has
\(|\Im F_u|<\pi\), and both cut sides keep their gaps
from (9). The two horizontal aliases then satisfy
\[
              f_e(x,\pm\epsilon)-2\pi\epsilon
                        \le\Re S(e)-\pi\epsilon.             \tag{18}
\]
All whole vertical currents are on the paid cut sides.
This is the finite small-height construction used at the
later incoming point, not a limiting rectangle of zero height.

All inequalities just used are strict on fixed compact
contours at each base point. When \(h_c\ne0\), one may
enlarge the two outer alias heights slightly beyond
\(\pm|h_c|\), spending only part of their strict gaps;
the main point then lies inside the finite rectangle.
When \(h_c=0\), use the rectangle in (18).
Each construction persists on a fixed neighborhood of
its base parameter and color. A finite cover of the compact
set \(\mathcal E_-\) gives uniform positive current gaps,
bounded contour lengths and the necessary parameter
neighborhoods, including where \(h_c\) changes sign.

## 5. Exact residue inventory and the original packet

At a fixed base parameter use the half-grid cuts
\[
 L_N=\lceil Na\rceil,\qquad M_N=\lceil Nb(E)\rceil,\qquad
 a_N=(L_N-1/2)/N,\quad b_N=(M_N-1/2)/N.                       \tag{19}
\]
The retained sum consists exactly of \(L_N\le l<M_N\).
Apply the same original finite cotangent-residue identity
and the exact holomorphic factorial summand from the
complex-index theorem. Its reciprocal arguments are
regular throughout these rectangles because
\[
                 0<\Re u<1/2,\qquad 0<\Re(e-u)<1/2.
 \]
The constant-mode coefficient is \(+N\). There remain
the two horizontal aliases, the four sign-half vertical
aliases and the two unweighted joining currents, with
their original orientations. The constant mode may be
moved to either sign of the main height inside the
rectangle; the two joining currents record that exact
deformation. No infinite-height contour is used.

The exact regular summand has its original nonzero
\(N^{-2}\) symbol. Equations (10)--(11) give the
nondegenerate Gaussian on the main line. Its normalization
is therefore precisely
\[
                     N\cdot N^{-2}\cdot N^{-1/2}=N^{-3/2}.
 \tag{20}
\]
The accretive branch of \(\sqrt{-F_{uu}}\) agrees with
the old branch, since its real part is strictly positive.
The first odd Gaussian correction integrates to zero.
Equations (9), (12), and Section 4 pay every other
finite source group with a common fixed gap.
The \(O(N^{-1})\) half-grid shifts preserve those gaps
by the original uniform zero-safe bounds.

Keep each base contour and its integer row sets fixed
while the parameters vary on its neighborhood. The
actual saddle moves inside the regular chart; its short
deformation joins remain paid. The original joint
factorial symbol and Gaussian argument prove (5) on
these neighborhoods. The functions in (1) are the
same exact finite functions on all overlaps, and the
critical branch and symbol have the original continuation
there. Thus the local packets agree.
The finite cover gives the uniform packet on
\(\mathcal E_-\), and adjoining the unchanged original
positive-height rectangle proves (4)--(5).
The nonzero normalized denominator and Cauchy's formula
give all fixed mixed derivatives.

There is no differentiation of the moving cuts \(b(E)\)
or the ceiling in (19). The source estimate includes
every omitted row before any contour is differentiated.
No new all-real-color relative packet is claimed.
In particular the remaining interval of private real
parts below \(27/100\), its required contour bridge, and
the actual outer-cap path enclosure are still separate
obligations.
