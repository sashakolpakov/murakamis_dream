# The geometric branch of the adjacent negative three-crossing source

The pendant \(T(R^{-3}T(R^{-3}))\) has original positive edge
geometry. Its selected vertices have degrees one and two, and
the degree-two vertex retains its outgoing edge. The complete
positive solution is already supplied by Theorem 15 of
[the negative-corridor analysis](research_negative_corridor_variational_bounds.md).
This note identifies that solution on the rational curve of
[the exact three-crossing boundary current](research_three_crossing_boundary_current.md),
Section 5, and identifies its original boundary periods.

The selected point lies on one specified quartic, with a
specified simple root. The full logarithmic filling equations
fix the sign. The negative source also reverses the clock
orientation, which changes the boundary multiplier to its
reciprocal. These distinctions are retained below. No
asymptotic estimate for the boundary source is inferred.

## 1. The original marked positive solution

Write the original path as \(v-w-b\), with \(b\) unfilled.
Let \(\alpha,\beta,u\) be its auxiliary angles, respectively.
The selected powers are both \(-3\). Retain their original
carriers and coefficients:
\[
        -3=\eta_v-2p_v=\eta_w-2p_w .
 \tag{1}
\]
In the standard positive-carrier choice this is
\(\eta_v=\eta_w=1\), \(p_v=p_w=2\).
The final outside carrier is not included in the piece.

For the canonical positive edge returns put
\[
 r(x,y)=\operatorname{arsinh}\bigl(\tan(x/2)\cos(y/2)\bigr).
\]
The full original unit-charge equations are
\[
 \begin{split}
 r(\alpha,\beta)&=-\frac{3i}{2}\alpha-\pi i,\\
 r(\beta,\alpha)+r(\beta,u)&=-\frac{3i}{2}\beta-\pi i.
 \end{split}                                                   \tag{2}
\]
At \(u=0\), the cited negative-path theorem gives a unique
solution with both original edge blocks positive and
\[
 -\pi<\Re\alpha,\Re\beta<0,\qquad
                      \Im\alpha,\Im\beta<0.                    \tag{3}
\]
Its actual filled core lengths are
\(-2\Im\alpha\) and \(-2\Im\beta\).
The positive-point marked completion theorem identifies
this metric with the original filling of the two selected
circles. The main cusps and the outside auxiliary cusp are
complete.

The positive-edge filling Jacobian is nonsingular. Hence
\(\alpha(u),\beta(u)\) extend holomorphically to a disk about
zero, with both old primitive periods fixed, the original
outgoing interface retained, and the original cells still
positive. Positivity and the full equations also imply the
strict core signs throughout that disk, by Lemma 3 of
[the attached-pair geometry](research_attached_even_reflected_pair_geometry.md).

Use the original edge phase \(\psi_x=-r/\pi\) and define
\[
 S_-(u)=\operatorname{stat}_{\alpha,\beta}
 \left[
 \psi(\alpha,\beta)+\psi(\beta,u)
 -\frac{3i}{4\pi}(\alpha^2+\beta^2)-i(\alpha+\beta)
 \right].
 \tag{4}
\]
The original pure outside periods and complete volume are
\[
 U_0=-2\pi S_-'(u)=2r(u,\beta(u)),\qquad V=2iu,
 \qquad
 \operatorname{Vol}(B_{-3,-3})=2\pi\Re S_-(0).
 \tag{5}
\]
The volume is that of the pendant's augmented exterior with
the remaining circle complete. It is not a closed two-circle
volume.

## 2. Deriving the quartic from the full primitive equations

To distinguish the rational parameter from the geometric
angles, denote it by \(\tau\). Put
\[
 c=\cos(\alpha/2),\qquad d=\cos(\beta/2),\qquad
 \tau=-2\cos\alpha=2-4c^2.
 \tag{6}
\]
The canonical half-angle cosines have positive real parts.
They and the selected half-angle sines are nonzero at the
complete positive point and in a sufficiently small disk.

Let \(\mathfrak q\) be the canonical edge square root
\[
 \mathfrak q^2=1+\tan^2(\alpha/2)+\tan^2(\beta/2).
 \tag{7}
\]
Its branch is continued from \(\mathfrak q=1\) at the
complete edge. On the positive original-cell domain it
is characterized by
\(\Re\mathfrak q>
\sqrt{(\Re\tan(\alpha/2))^2+(\Re\tan(\beta/2))^2}\).
For the original edge,
\(\cosh r(\alpha,\beta)=\mathfrak qd\) and
\(\cosh r(\beta,\alpha)=\mathfrak qc\).
Taking the sinh and cosh of the first *full* equation in
(2), including its \(-\pi i\), gives
\[
 d=i(1-\tau)c,\qquad
 \mathfrak q=\frac{i(\tau+1)}{\tau-1}.
 \tag{8}
\]
Indeed
\(\sinh(-3i\alpha/2-\pi i)=i\sin(3\alpha/2)\),
and
\(-\cos(3\alpha/2)=c(1+\tau)\).
Using \(4c^2=2-\tau\) in (8) yields
\[
 -2\cos\beta
   =2-4d^2
   =z(\tau),\qquad
 z(\tau)=4-5\tau+4\tau^2-\tau^3 .
 \tag{9}
\]
Thus the source's initial parameter is exactly the
original inner pair trace, and its function \(L=z(\tau)\)
is the original outer selected pair trace.

Subtract \(r(\beta,\alpha)\) from the second equation of
(2). Its sinh gives
\[
 \begin{split}
 \tan(\beta/2)\cos(u/2)
 &=ic\mathfrak q\sin(3\beta/2)+c\tan(\beta/2)\cos(3\beta/2).
 \end{split}
\]
Divide by the nonzero \(\tan(\beta/2)\), and use
\(\sin(3\beta/2)/\tan(\beta/2)=d(1-z)\) and
\(\cos(3\beta/2)=-d(1+z)\). Equations (8)--(9) then give
\[
 \begin{split}
 \cos(u/2)
 &=cd\{i\mathfrak q(1-z)-(1+z)\}\\
 &=2ic^2(\tau-z)
 =-\frac{i}{2}(\tau-2)^2(\tau^2-2\tau+2).
 \end{split}
 \tag{10}
\]
Consequently the actual negative geometric branch satisfies
\[
 \boxed{\quad v(\tau)=2i\cos(u/2),\qquad
         v(\tau)=(\tau-2)^2(\tau^2-2\tau+2).\quad}               \tag{11}
\]
This fixes the sign in the two quartics of the source
curve. Reflection changes the powers to \(+3,+3\);
the reflected geometric branch has
\(v(\tau)=-2i\cos(u/2)\).

Equations (8)--(11) were derived from the calibrated
logarithmic periods. An arbitrary root of the squared
boundary equation is not thereby a positive geometric
solution.

## 3. Exact selection of the complete root

At \(u=0\), put
\[
 f(\tau)=v(\tau)-2i
       =\tau^4-6\tau^3+14\tau^2-16\tau+8-2i .
 \tag{12}
\]
There is exactly one root in each disk of radius \(1/1000\)
with the following rational centers:
\[
 \frac{2610+416i}{1000},\quad
 \frac{624-683i}{1000},\quad
 \frac{1822-1037i}{1000},\quad
 \frac{944+1303i}{1000}.
 \tag{13}
\]
Here is a finite exact proof. For a center \(a\), expand
\(f(a+\zeta)=\sum_{j=0}^4b_j\zeta^j\), and put
\(\rho=1/1000\). Bound a complex number from above by
the sum of the absolute values of its real and imaginary
parts, denoted \(\|\cdot\|_1\), and from below by the
larger of those absolute values, denoted
\(\|\cdot\|_\infty\). For the four centers, respectively,
\[
 \rho\|b_1\|_\infty-\|b_0\|_1
                   -\sum_{j=2}^4\rho^j\|b_j\|_1
 =\frac1{10^{12}}
 \begin{cases}
 3702643231,\\
 1874713022,\\
 932436308,\\
 2635665116 .
 \end{cases}                                                   \tag{14}
\]
All four numbers are positive. Rouché's theorem therefore
gives one root, counted with multiplicity, in each disk.
The disks are disjoint and the polynomial has degree
four, so this is the complete root list and every root
is simple.

The actual geometric root must be in the upper half-plane:
writing \(\alpha=-\theta-ih\), with \(0<\theta<\pi\),
\(h>0\), gives
\[
                  \Im\tau=2\sin\theta\,\sinh h>0 .
 \tag{15}
\]
This excludes the middle two disks.

The first disk is also incompatible with (8). To see
this without a numerical square root, write
\(\tau=a+ib\), \(b>0\), and take
\(c=\sqrt{2-\tau}/2=p-iq\), \(p,q>0\).
The sign of
\(\Re\{i(1-\tau)c\}\) is the sign of
\[
                         |2-\tau|+3-2a .
 \tag{16}
\]
Indeed \(q/p=b/(|2-\tau|+2-a)\), and direct multiplication
gives this expression after multiplication by a positive
factor. In the first disk,
\[
 a>2.609,\qquad |2-\tau|<0.75,\qquad 2a-3>2.218.
 \]
Expression (16) is therefore negative, contradicting
\(\Re d>0\). In the last disk \(a<0.945<3/2\), so (16)
is positive.

We conclude that the complete geometric parameter is
precisely the root
\[
 \boxed{\quad
 |\tau_0-(944+1303i)/1000|<1/1000 .
 \quad}                                                        \tag{17}
\]
Its decimal value, only for orientation, is
\(\tau_0\simeq0.9435821114+1.3032352906i\).
Existence of the positive solution came from the
negative-corridor theorem; (12)--(17) identify it
uniquely among the source-curve intersections.

Since \(f'(\tau_0)\ne0\), equation (11) has a unique
holomorphic root \(\tau(u)\) through \(\tau_0\). The
actual geometric \(-2\cos\alpha(u)\) satisfies that
equation and has the same initial value. They therefore
agree as holomorphic germs. This also retains the full
logarithmic charges in (2); it does not choose them
afresh by exponentiation.

## 4. The rational source chart and the primitive outside period

Use the exact functions of the boundary-current note,
with the negative source's conjugated clock orientation:
\[
 \begin{split}
 r_0(\tau)&=\tau^2-3\tau+3,\\
 X(\tau)&=\frac{r_0(\tau)}{z(\tau)r_0(\tau)-1},\\
 E(\tau)&=-\frac{(\tau-2)^3(\tau^2-2\tau+2)^2}{(\tau-1)^2}.
 \end{split}                                                   \tag{18}
\]
The symbol \(r_0\) here is a polynomial; it is unrelated
to the edge return \(r(x,y)\).
The source's frozen trace coordinates are
\[
 \begin{split}
 C&=X+X^{-1}-(2-X-X^{-1})E,\\
 L&=X+X^{-1}-(2-X-X^{-1})E^{-1}.
 \end{split}
\]
Its exact rational identities are
\[
                   L=z(\tau),\qquad C=2+v(\tau)^2 .
 \tag{19}
\]
On (11), with \(w=e^{iu}\), these become
\[
               C=-(w+w^{-1}),\qquad
               L=-2\cos\beta .
 \tag{20}
\]
All chart denominators are nonzero at (17). For example
direct rational interval evaluation on its containing
rectangle gives
\[
 \frac1{50}<\Re X<\frac14,\qquad
                    -\frac45<\Im X<-\frac12 .
 \tag{21}
\]
The factors \(\tau-1,\tau-2,\tau^2-2\tau+2\) are also
nonzero there. The chart is consequently regular on
the selected germ.
For clarity, writing \(D=z(\tau)r_0(\tau)-1\), the same
rectangle evaluation gives
\[
 \frac{187}{100}<\Re D<\frac{206}{100},\qquad
 -\frac{144}{100}<\Im D<-\frac54,\qquad |D|^2>5.
\]
Thus the interval division used in (21) does not cross
a zero denominator.

The actual primitive pure boundary multiplier is
\[
 \boxed{\quad
       e^{U_0}=\frac{1+wX}{X+w},\qquad
       e^V=w^2 .
 \quad}                                                        \tag{22}
\]
In particular, the first ratio is the reciprocal of
the positive-clock expression. Here is a direct proof
with the sign fixed.

Eliminate \(E\) between (20) and the trace formulas.
Using \(d^2=(2-L)/4\) gives the rational identity
\[
 d^2=-\frac{(1-X)^2(1+w)^2}
               {4(X+w)(1+wX)} .
 \tag{23}
\]
Put \(R=(1+wX)/(X+w)\). Then \(R(0)=1\), and
\[
               \frac{(R-1)^2}{4R}
                        =d(u)^2\tan^2(u/2).
 \tag{24}
\]
At \(u=0\), (23) says
\(d_0^2=-((1-X_0)/(1+X_0))^2\).
Both \(d_0\) and
\(-i(1-X_0)/(1+X_0)\) have positive real part;
for the latter this follows from \(\Im X_0<0\) in (21).
Therefore
\[
       d_0=-i\frac{1-X_0}{1+X_0},\qquad
                         (\log R)'(0)=d_0 .
 \tag{25}
\]
The logarithm in (25) is normalized to zero at zero.
By (24), its half has the same squared sinh as
\(r(u,\beta(u))\), and by (25) the same nonzero initial
derivative. The analytic factors in the difference of
these squared equations select the same sign near
zero. Thus
\[
                 \tfrac12\log R=r(u,\beta(u)),
 \]
which proves (22) with the full logarithm in (5).
The complete boundary curvature is consequently
\[
 S_-''(0)=-\frac{d_0}{2\pi}
       =\frac{i(1-X_0)}{2\pi(1+X_0)},\qquad
                         \Re S_-''(0)<0 .
\]
The phase is even: (11), its selected simple root and
the original filling solution are unchanged by
\(u\mapsto-u\).

Equivalently, the physical positive-clock leaf
coordinate is \(Y=X^{-1}\). Its usual ordered-leaf
formula \((Y+w)/(1+wY)\) is exactly (22).
For the negative source the quantum root
\(q_N=e^{\pi i/N}\) is conjugated, so the clock is
\(X=e^{-2\pi i x}\), not the physical
positive-clock coordinate \(e^{2\pi i x}\).
The direct calculation above proves the peripheral
identity without relying on that terminology.

If the outside original circle has carrier \(\eta_b\),
insert it once after assembling all pieces. For this
single piece the periods are
\[
 U=U_0-i\eta_bu,\qquad V=2iu.
 \tag{26}
\]
The outside framing and the primitive filling
\(\mu_b+p_b\lambda_b\) are therefore retained. Neither
curve has been replaced by a multiple or by an
unrecorded shear.

## 5. What the identification proves

The rational source curve has a simple holomorphic
branch with the actual original geometric boundary
periods (22). Its complete point is fixed by (17).
The calibrated generating function is the original
stationary action (4), with absolute real value fixed
by (5). The original ordered triangle interface is
the one supplied by the positive original edge cells;
no new topological collar is inferred from trace
matching alone.

The four roots of the other quartic, and the remaining
three roots of (12), are not discarded from the exact
quantum boundary problem. The source determinant may
have other contributions and cancellations. This note
does not estimate those contributions, assert a
nonzero coefficient for (17), or prove the
\((-3,-3)\) boundary asymptotic.

## 6. Exact arithmetic record

[The geometric-branch checker](../experiments/check_three_crossing_geometric_branch.py)
reproduces all four rational Rouché margins, the
rectangle bounds and nonvanishing denominator above,
and seven rational identities used in the trace and
peripheral comparison. It also checks coprimality of
the complete quartic with the displayed chart
denominators.
[The saved result](../repro/results/research-three-crossing-geometric-branch.json)
contains exact intervals, library versions and the
script and note hashes. An independent record can be
written without replacing it:

~~~sh
python3 experiments/check_three_crossing_geometric_branch.py --output /tmp/three-crossing-geometry.json
~~~

The arithmetic record checks the finite calculations.
The existence theorem, the original peripheral
marking and the logarithmic selection are the
written arguments above.
