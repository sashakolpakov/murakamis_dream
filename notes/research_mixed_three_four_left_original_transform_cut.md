# Keeping the original transform cut on the ordinary left taper

Research deduction, 7 November 2026. Retaining the correlated incoming
radius improves the coupled derivative at the original transform cut
\(t=.15\). The cut need not move into the small-transform region.
The original left vertical sides and joins are consequently paid by
their actual endpoint profiles and strict height convexity at this
fixed cut. No numerical evaluation or new saved comparison is used.

## 1. The same original source and the fixed-cut derivative

Use the exact ordinary \((3,4)\) source and complete cap profiles in
[the private-height transport](research_mixed_three_four_private_height_left_transport.md).
Put
\[
 a=x+ih,\quad h=c(x-.1)/.12=-\lambda(x-.1),\quad
 .1\le x\le.22,\quad -.072<c<.021,\quad
 -7/40<\lambda<3/5.                                      \tag{1}
\]
The first private profiles have \(e=u+ik\),
\(.27\le u\le.49\), \(-.019\le k\le.037\).
Retain the complete right endpoint coefficient at
\(b\in E_c=[.27,.49]+i[-.055,.04]\).
At a fixed real transform \(t=v\), the exact full coupled
incoming derivative is
\[
 \mathcal H=\Re D+\lambda\Im D,\qquad
 D=g'(e+a)+g'(a+v)-2g'(a)+2\pi iv.                       \tag{2}
\]
The right endpoint action, its allocations and every original
private sampling penalty are independent of \(x\).
Equation (2) retains both shared allocations and the ordinary chirp.

**Theorem 1.** At the original cut \(v=3/20\), uniformly on (1),
\[
                         \mathcal H>1/100.               \tag{3}
\]
The exact first-cap true-end alternative has a nonnegative coupled
incoming derivative at this same real cut.

The previous private-height proof reduces the regular minimum to
\(k=-.019\), \(u=.27,.49\). Write \(r=e^{2\pi h}\) and
\(\rho=e^{2\pi k}\); then
\[
 3/5<r<23/20,\quad \rho>22/25,\quad
 \lambda\ge0\Rightarrow r\le1,\quad
 \lambda\le0\Rightarrow r\ge1.                         \tag{4}
\]
For \(\lambda\le0\), the original argument bound, including
the private-height correction, gives
\(\Im D<\pi(.15-.27+.019)<0\).
The first squared modulus ratio exceeds \(13/10\), the second
exceeds one, so \(\mathcal H>\frac12\log(13/10)>3/23\).
It remains to treat \(\lambda\ge0\), keeping its actual radius.

## 2. The earlier incoming interval has a large modulus reserve

For \(.1\le x\le.18\), the fixed-radius real part decreases
with \(x\), by the own-cotangent and shifted-cotangent comparison
in Section 3 of the private-height proof. Its lower bound may
therefore be taken at \(x=.18\). At both private endpoints,
\[
 \cos(2\pi x)>21/50,\qquad
 \cos2\pi(x+u)<-12/25,\qquad
 \cos2\pi(x+.15)<-12/25.                                \tag{5}
\]
These follow from the original elementary cosine guards; for example
the tight first shifted angle is \(1.34\pi\), with
\(\cos(.34\pi)>12/25\), and the own angle is \(.36\pi\).
Taylor upper and lower bounds through degree six at the rational
arguments from \(\pi<22/7\), \(\pi>157/50\) give these strict
rational inequalities.

Let
\[
 D_r=1+r^2-21r/25,\quad
 N_1=1+484r^2/625+528r/625,\quad
 N_2=1+r^2+24r/25.                                     \tag{6}
\]
The first and second squared modulus ratios are bounded below by
\(N_1/D_r\), \(N_2/D_r\), respectively. The concave
quadratics \(N_1-2D_r\) and \(N_2-(9/4)D_r\) have values
\[
 (1151/15625,\ 187/625),\qquad(1/100,\ 7/20)             \tag{7}
\]
at \(r=3/5,1\). Thus
\[
 \Re D>\tfrac12\log(9/2)
   =\operatorname{atanh}(7/11)>2884/3993>7/10.            \tag{8}
\]
The last inequality uses the first two positive terms of the
atanh series. The largest possible imaginary debit is
\((3/5)(.49-.15)\pi<561/875\): the negative private height
improves the argument when \(u=.49\), and at \(u=.27\)
its loss is less than \(.019\pi\).
Consequently \(\mathcal H>103/1750>1/20\) on this interval.

## 3. The later interval keeps the radial argument credit

For \(.18\le x\le.22\), the private endpoint \(u=.27\)
has first squared ratio \(>9/5\) and second ratio
\(\ge270/143\), as in
[the positive-alias comparison](research_mixed_three_four_left_positive_alias.md).
Thus \(\Re D>\frac12\log3>1/2\); its imaginary debit is
less than \((3/5)(139/1000)\pi<3/10\).
This endpoint is paid with room to spare.

Only \(u=.49\), \(\lambda\ge0\) remains. The same exact
modulus witnesses give
\[
 \Re D>\tfrac12\log(360/143)
   >156/343.                                            \tag{9}
\]
For its imaginary part first set \(k=0\), keeping the same
\(r=e^{-2\pi\lambda(x-.1)}\), and put
\(z=\tanh(\pi\lambda(x-.1))\). The original logarithmic lift
gives the identity
\[
\begin{split}
 \Im D_0={}&-17\pi/50+2\arctan(z\cot\pi x)\\
 &-\arctan(z\cot\pi(x+.49))
  -\arctan(z\cot\pi(x+.15)).
\end{split}                                             \tag{10}
\]
Indeed, for \(0<q<1\),
\(\arg(1-r e^{-2\pi iq})=\pi(1/2-q)-\arctan(z\cot\pi q)\).
This follows by factoring the positive multiple of
\(e^{-\pi iq}[\sinh(\pi\lambda(x-.1))\cos\pi q+
i\cosh(\pi\lambda(x-.1))\sin\pi q]\).
All sines are positive, so there is no logarithmic-lift change.
Restoring \(k=-.019\) only increases the imaginary part at
\(u=.49\), as proved in the original private-height comparison.

The relevant elementary bounds are
\[
 \cot\pi x>6/5,\quad
 \cot\pi(x+.49)<-1/2,\quad
 \cot\pi(x+.15)<3/5.                                   \tag{11}
\]
The first is the established \(\cot(.22\pi)>6/5\) guard.
The second follows from \(x+.49\ge.67>2/3\).
For the last, \(\cot(.33\pi)=\tan(.17\pi)<3/5\):
the four alternating arctangent terms give
\[
 \arctan(3/5)>
 3/5-(3/5)^3/3+(3/5)^5/5-(3/5)^7/7
 >539/1000>187/350>.17\pi.                              \tag{12}
\]
Also \(0\le z<6/25\), since
\(\pi\lambda(x-.1)\le.072\pi<6/25\).
Using \(\arctan w\ge w-w^3/3\) for positive \(w\),
and \(\arctan w\le w\), (10)--(11) give
\[
 \Im D>-17\pi/50+23z/10-(6/5)z^3
                 >-17\pi/50+(111/50)z.                 \tag{13}
\]
At \(\lambda=0\) the non-strict limiting argument statement
is sufficient, because the imaginary contribution vanishes.

For positive \(\lambda\), \(x-.1\ge.08\) and
\(\pi>25/8\) imply
\[
 z>\tanh(\lambda/4)
   >\lambda/4-\lambda^3/192
   \ge397\lambda/1600>31\lambda/125.                    \tag{14}
\]
The elementary inequality \(\tanh w\ge w-w^3/3\)
follows by differentiating and using \(\tanh w\le w\).
Combining (9), (13), and (14), with \(\pi<22/7\), gives
\[
 \mathcal H>
 156/343-187\lambda/175+(3441/6250)\lambda^2.             \tag{15}
\]
This quadratic decreases on \([0,3/5]\). Its endpoint value is
\[
 156/343-561/875+30969/156250
             =636117/53593750>1/100.                    \tag{16}
\]
This proves (3). The true-end assertion follows from the original
same-radius argument comparison for the real conditional target:
when \(\lambda\ge0\), both its real derivative and the argument
contribution are nonnegative; when \(\lambda\le0\), the term
\(E_{\rm end}'=-2\pi\lambda\) pays that argument contribution.
It is precisely the true-end calculation in Section 3 of
[the moving-boundary proof](research_mixed_three_four_left_moving_boundary.md).

## 4. Negative heights and the original complete left sides

For \(.15\le v\le.22\) at transform height zero, the exact
downward-crossing argument in the positive-alias proof reduces
each minimum to \(v=.15,.22\). Theorem 1 and the original
private-height theorem therefore imply \(\mathcal H>1/100\)
throughout this interval. For \(\eta\le0\), exact differentiation
at \(t=v+i\eta\) gives
\[
 \partial_\eta\mathcal H
 =-2\pi\frac{1-qC-\lambda qS}{1+q^2-2qC},\quad
 q=e^{2\pi(h+\eta)},\ C=\cos2\pi(x+v),\ S=\sin2\pi(x+v).
                                                               \tag{17}
\]
Here \(C\le0,S\ge0\). If \(\lambda\ge0\), then
\(q\le r\le1\), so the numerator is at least \(1-3q/5>0\).
If \(\lambda\le0\), each term in the numerator is nonnegative
and its constant term is positive. Hence the negative-height
derivative is no smaller than at height zero.
The same reasoning applies to the true-end alternative.
For \(.22\le v\le.49\), the already proved negative-height
transport applies. On \([.49,.5]\), one has
\(C<-9/50\) and \(S<0\) in (17). If \(\lambda\ge0\),
its numerator is positive term by term. If \(\lambda\le0\),
then \(C+\lambda S<-9/50+7/40=-1/200\), so it is again
positive. Equation (5) of the positive-alias theorem gives the
height-zero bound \(\mathcal H(0)>1/100\) on this last interval;
the true-end height-zero calculation above applies there too.
Thus all original main and lower-alias profiles on
\(.15\le v\le.5\), with the same fixed right private states,
retain their calibrated endpoint comparisons at \(x=.22\).
The upper aliases are paid separately by the positive-alias theorem.

At the original left side \(t=.15+i\eta\), \(|\eta|\le.12\),
the entire original terminal phase satisfies
\[
 -\pi^{-1}\Re\Phi_{tt}
      =3C(t)-C(a+t)-C(b+t)>3-1-1/2>0.                  \tag{18}
\]
The guard \(C(t)>1\) is proved in
[the all-height low-transform force](research_mixed_three_four_left_low_transform_force.md),
Section 3. The other bounds follow from
\(\Re(a+t)\ge.25\), \(\Re(b+t)\ge.42\), with a
nonpositive shifted cotangent whenever its real part is at least
\(.5\). Thus vertical convexity holds on this fixed original
side. The private-variable convexity also remains the original
one, including at intermediate transform heights.
On each sign of height the sampling penalties are linear, so
they preserve this convexity.

The zero-height left face is calibrated by its original raw gap
\(1/20000\) at \(x=.22\), as in Section 4 of the moving-boundary
proof. Theorem 1 preserves that gap when \(x\) decreases;
the true-end alternative is nondecreasing and has the same
endpoint payment. Lower aliases retain the original raw alias
reserve, and upper aliases have the proved raw gap \(1/125\).
Convexity (18) therefore pays every original left transform
side and zero-mode join by its actual endpoint profiles, with
the original right-private sides and penalties retained.

Use exactly the original finite retained row, whole endpoint
coefficient, residue coefficient \(+N\), and half-grid cut
adjacent to \(.15\). Its factorial arguments are regular on
these compact contours. The stated strict gaps absorb rounding,
symbol errors and polynomial contour costs, giving the original
left-face groups a finite gap \(1/40000\), uniformly on a small
ordinary-color bidisk and for all fixed ordinary derivatives,
at both level parities. No small-transform vertical convexity is
used, and the frozen moving-cut theorem remains valid independently.

This resolves these original contour groups and the negative-height
transport on the old central interval. The physical complement,
all real-color angular comparisons, the remaining incoming-circle
pieces and final ordinary observation must still be assembled from
their complete sources. No whole \((3,4)\) theorem is asserted here.
