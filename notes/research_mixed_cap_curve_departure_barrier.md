# A required departure before private real part \(6/25\)

Research deduction, 8 November 2026. At the exact later incoming
parameter, the outer-cap action already exceeds its critical value
on an explicit point of the auxiliary-real curve whose real part is
strictly between \(23/100\) and \(6/25\). The entire vertical segment
from this point to the real axis also exceeds that value. Thus the
closed source region above the curve, supplemented by a below-curve
corridor beginning only at \(6/25\), does not itself contain a
pointwise descending connection from its left part to the saddle.

The proof uses exact logarithmic series bounds, not a numerical
evaluation of an action. It does not rule out cancellation in the
original source, a different contour, or a sufficiently wide
neighborhood of the proved source domains. No width for such a
neighborhood is assumed.

## 1. Original branch and an exact multiplier

Use the original phase \(\Psi(e,a)\), the curve \(e(t)\), and the
actual critical point \((e_0,a_0)\) of
[the local curve obstruction](research_mixed_cap_auxiliary_real_curve_obstruction.md),
equations (1)--(4). Put
\[
 \sigma=\sqrt2,\qquad q=\sqrt2\,t,\qquad d=1-q,\qquad
 0\le d\le1/20,\qquad
 \phi(d)=\Re\Psi(e((1-d)/\sqrt2),a_0).
 \tag{1}
\]
Thus \(\phi(0)=M_{\rm cap}(a_0)\). On this part of the curve,
\[
 p=1-q^2+i\sigma q,\qquad
 X_0=(-1+2\sigma i)/3.
 \tag{2}
\]
The exact original multiplier
\(L=\exp\Psi_e=\omega(p-X_0)/(p-\omega)\) simplifies to
\[
 L=1+\frac{2(1-q)}{3q^3}
       \left\{(3q^2+3q-2)-i\sigma(3q+2)\right\}.
 \tag{3}
\]
For \(19/20\le q<1\), its real part exceeds one and its imaginary
part is negative. The original lift, zero at \(q=1\), is therefore
the continuous principal logarithm of (3).

An equivalent factorization, useful for uniform remainders, is
\[
 L(d)=
 \frac{(1-cd)\{1-3\sigma i\,d+(-1+\sigma i)d^2\}}{(1-d)^3},
 \qquad c=(1+\sigma i)/3.
 \tag{4}
\]
No phase constant is changed in passing from (3) to (4).

## 2. A uniform integrated action comparison

The first three terms of the logarithm in (4) are
\[
 \Log L(d)=
 \left(\frac83-\frac{10\sigma i}{3}\right)d
 +\left(\frac{86}{9}+\frac{8\sigma i}{9}\right)d^2
 +\left(-\frac{400}{81}+\frac{1214\sigma i}{81}\right)d^3
 +\mathcal R(d),
 \qquad |\mathcal R(d)|\le200d^4.
 \tag{5}
\]
Here is a direct remainder proof. Factor the quadratic in (4) as
\((1-\alpha d)(1-\beta d)\). Then
\[
 \alpha+\beta=3\sigma i,\quad
 \alpha\beta=-1+\sigma i,\quad
 |\alpha|,|\beta|
 \le\frac{3\sigma+\sqrt{\,2\sqrt{57}\,}}2<\frac{33}{8}.
 \tag{6}
\]
The last inequality follows from \(3\sqrt2<17/4\) and
\(\sqrt{2\sqrt{57}}<4\). Also \(|c|<1\).
For each logarithm use the absolute tail after degree three.
Since \(d\le1/20\), their total is at most
\[
 \frac{4+2(33/8)^4}{4(1-33/160)}d^4<200d^4.
 \tag{7}
\]
For the final strict inequality one may use
\((33/8)^4<290\) and \(4(1-33/160)>3\).
The coefficients in (5) follow either by multiplication or from
the power sums of \(\alpha,\beta,c\). All factors stay in their
logarithmic disks, so these expansions have the lift in (3).

Differentiating the actual curve gives
\[
 \frac{de}{dq}
    =\frac{1+q^2-i\sigma q^3}
                 {\sigma\pi(1+q^4)}.
 \tag{8}
\]
Consequently
\[
 \phi'(d)=
 \frac{q^3(-\Im\Log L)-(1+q^2)\Re\Log L/\sigma}
                         {\pi(1+q^4)}.
 \tag{9}
\]
Inserting the polynomial part of (5), the numerator in (9) is
\(\sigma P(d)\), where
\[
 P(d)=\frac23d-\frac{160}{9}d^2+\frac{878}{81}d^3
       +\frac{2369}{81}d^4-\frac{3370}{81}d^5
       +\frac{1214}{81}d^6.
 \tag{10}
\]
The error in that numerator has absolute value less than
\(200(1+\sqrt2)d^4<500d^4\).

For completeness, an elementary bound for the remaining rational
factor gives
\[
 \left|\phi'(d)-\frac{\sigma}{\pi}
       \left(\frac d3-\frac{74d^2}{9}-\frac{974d^3}{81}\right)
 \right|\le\frac{600}{\pi}d^4.
 \tag{11}
\]
Indeed, write \(W=(1+(1-d)^4)^{-1}\) and
\(W_2=1/2+d+d^2/2\). Direct multiplication gives
\[
 |W-W_2|
 =\frac{2d^3-d^4/2-d^5+d^6/2}{1+(1-d)^4}
 \le2d^3,\qquad W\le1.
 \tag{12}
\]
For \(0<d\le1/20\), (10) has
\(|\sigma P(d)|<3d\): bound its six coefficient moduli by
\(1,18,11,30,42,15\), respectively, and use \(\sqrt2<3/2\).
Thus the error caused by replacing \(W\) by \(W_2\) is
less than \(6d^4\). The terms of \(W_2\sigma P\) after degree
three have total modulus less than \(81d^4\). One explicit
bound is \(50d^4\) for the terms of \(P\) of degree at least
four, \(14d^4\) for the degree-two term multiplied by \(d^2/2\),
and \(17d^4\) for the degree-three term multiplied by
\(d+d^2/2\). Combining these with the \(500d^4\) error proves
(11).
At \(d=0\), the error bounds hold by equality and continuity.

Integrating (11), for \(0<D\le1/20\) we obtain
\[
 \begin{split}
 \phi(D)-\phi(0)
 &\ge\frac1\pi\left\{
  \sigma\left(\frac{D^2}{6}-\frac{74D^3}{27}
                         -\frac{487D^4}{162}\right)-120D^5
                    \right\}\\
 &\ge\frac{D^2}{\pi}
       \left\{\frac{1433\sqrt2}{64800}-\frac3{200}\right\}
 >\frac{5171}{324000\pi}D^2>0.
 \end{split}                                                     \tag{13}
\]
The second line uses \(D\le1/20\); the last uses
\(\sqrt2>7/5\). This is a lower bound on an exact phase
difference derived from its original derivative, not an inversion
of an upper envelope.

## 3. An explicit barrier to the currently described source route

Set
\[
 q_b=19/20,\qquad t_b=19/(20\sqrt2),\qquad
 e_b=e(t_b)=E_b-i\eta_b.
 \tag{14}
\]
The point belongs to the proved auxiliary-real source curve.
It lies to the left of the proposed below-curve threshold:
\[
                      \frac{23}{100}<E_b<\frac6{25}.
 \tag{15}
\]
To check the upper inequality, the exact curve gives
\[
 \cot(2\pi E_b)=\frac{39}{380\sqrt2}>
 \frac{13}{190}>\frac{11}{164}>
                     \tan(\pi/50).
 \tag{16}
\]
For the last inequality use
\(\tan x<x/(1-x)\) for \(0<x<1\), and
\(\pi/50<11/175\).
For the lower inequality in (15),
\[
 \cot(2\pi E_b)<\frac{39}{532}<\frac1{12}
                  <\frac{\pi}{25}<\tan(\pi/25).
 \tag{17}
\]
Both conclusions use the strict decrease of cotangent on
\((0,\pi/2)\).

By (13), \(\Re\Psi(e_b,a_0)>M_{\rm cap}(a_0)\).
In fact the entire vertical segment above \(e_b\) satisfies
\[
 \Re\Psi(E_b+ih,a_0)>M_{\rm cap}(a_0),
                         \qquad -\eta_b\le h\le0.
 \tag{18}
\]
Here the phase and critical auxiliary branch are the ones in
[the above-curve source region](research_mixed_endpoint_region_above_real_curve.md),
Section 2. They obey
\(0<\Re u_c<E_b<1/2\) and the original zero logarithmic lift
on this whole segment. The negative real part of the full
endpoint Hessian is positive definite in that chamber, so its
Schur derivative gives \(-\Re S''>0\).
Since \(1/2<a_0+E_b<1\), also
\[
 -\Re\Psi_{ee}=-\Re S''-\pi\Re\cot\pi(a_0+E_b+ih)>0.
 \tag{19}
\]
Thus the real phase is strictly convex in \(h\). At the bottom,
(3) has \(\Im\Psi_e<0\), so
\(\partial_h\Re\Psi=-\Im\Psi_e>0\). It increases from an
already excessive value, proving (18).

Any continuous path from private real part \(1/8\) to \(e_0\)
must cross the line \(\Re e=E_b\). In the closed union consisting
of the above-curve region and a below-curve corridor whose real
parts start at \(6/25\), this cross-section is exactly the segment
in (18). Therefore that closed union contains no such path with
pointwise action everywhere at most \(M_{\rm cap}(a_0)\).
The same conclusion holds if further source rectangles with real
parts at least \(6/25\) are added: they have no point with real
part \(E_b\).

This specifies a necessary leftward extent for a contour staying
in these described domains: it needs an additional eligible
crossing below the curve at real part \(E_b<6/25\), or another
source-controlled route outside the union. The source theorems
also give unspecified open neighborhoods; (18) does not determine
their widths or exclude that a sufficiently wide one might help.
Nor does this phase barrier obstruct cancellation in a complete
signed contour integral. It identifies the missing geometric
comparison for this particular pointwise contour construction.
