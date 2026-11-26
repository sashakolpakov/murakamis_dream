# The first-action multiplier can increase on the new real domain

Private written observation, 11 November 2026. Author-frozen after full
proof and direct-source readback. Independent review is required before
adoption.

The original zero-lift critical action is well defined on the real
rectangle needed by the complete conditional-source theorem. Its
derivative in the first coordinate need not be nonpositive there.
The calculation below gives an exact algebraic crossing of modulus
one, followed by a strictly positive derivative.
It concerns a proposed action comparison, not the finite-source bound.

## 1. Original action and polynomial

Keep
\[
 Q(s;a,q)=g(a+s)+g(q+s)-3g(s)-g(a)-g(q)+2\pi ias,
 \qquad g'(u)=\operatorname{Log}(1-e^{-2\pi iu}),
\]
and put
\[
 X=e^{-2\pi ia},\qquad Y=e^{-2\pi iq},\qquad v=e^{2\pi is}.
\]
The original critical polynomial is
\[
                   v(v-X)(v-Y)-X(v-1)^3=0.                  \tag{1}
\]
The [zero-lift branch theorem](research_mixed_real_unit_pair_zero_lift_branch.md)
selects its unique solution of \(Q_s=0\) in
\(0<\Re s<\min(1-a,1-q)\), when
\[
             1/2\le a<1,\qquad1/2\le q<(1+a)/2.
 \tag{2}
\]
Write \(\Theta(a,q)=Q(s(a,q);a,q)\).
Differentiation at the critical point, with the original incoming
carrier retained, gives
\[
 \Theta_a=g'(a+s)-g'(a)+2\pi is,\qquad
                   e^{\Theta_a}=\frac{v-X}{1-X}.
 \tag{3}
\]
Thus \(\partial_a\Re\Theta=\log|(v-X)/(1-X)|\).
Equation (3) also appears in the
[unit-incoming branch source](research_mixed_four_conditional_unit_incoming_branch.md).

Fix \(a=1/2\), so \(X=-1\), and set
\[
                         \omega=(v+1)/2.
 \tag{4}
\]
We first find a zero-lift solution with \(|\omega|=1\).

## 2. An exact unit-modulus crossing

Write \(\omega=e^{i\phi}\), with \(0<\phi<\pi\), and introduce
\[
 d=2(1-\cos\phi),\qquad
 s_\phi=\sin\phi=\sqrt{d-d^2/4}.
\]
Then
\[
 v=1-d+2is_\phi,\qquad |v|^2=1+2d.
 \tag{5}
\]
Solving (1) for \(Y\), and using
\((v-1)^2/(v+1)=-2d\) on this circle, gives exactly
\[
 Y(v)=v+\frac{(v-1)^3}{v(v+1)}
                 =v-2d+\frac{2d}{v}.
 \tag{6}
\]
Consequently
\[
 \Re Y=\frac{1+d-8d^2}{1+2d},\qquad
 \Im Y=\frac{2s_\phi}{1+2d},
\]
and
\[
 |Y|^2-1
   =\frac{2d}{(1+2d)^2}P(d),\qquad
 P(d)=32d^3-8d^2-10d+1.                                    \tag{7}
\]

The two rational evaluations are
\[
 P(5/8)=-9/16,\qquad P(2/3)=7/27.
 \tag{8}
\]
Moreover \(P'(d)=96d^2-16d-10>0\) on \([5/8,2/3]\):
its value at \(5/8\) is \(35/2\), and its derivative is
positive on that interval.
There is therefore a unique \(d_0\in(5/8,2/3)\) for which
\(|Y|=1\).

At this point \(\Im Y>0\).
The function \((1+d-8d^2)/(1+2d)\) has derivative
\[
                  -\frac{1+16d+16d^2}{(1+2d)^2}<0,
\]
and its value at \(5/8\) is \(-2/3\).
Thus \(\Re Y<-2/3\). Writing \(Y=e^{-2\pi iq_0}\) on the
upper unit semicircle gives
\[
                         1/2<q_0<2/3.                       \tag{9}
\]
The corresponding \(v\) has positive real and imaginary parts
and modulus greater than one. Its original logarithmic coordinate
\[
                     s_0=\operatorname{Log}v/(2\pi i)
\]
therefore has
\[
             0<\Re s_0<1/4,\qquad \Im s_0<0.
 \tag{10}
\]
In particular \(s_0,a+s_0,q_0+s_0\) all remain in the original
regular strips; the last real part is smaller than \(11/12\).

This point has lift zero. To check it directly, at a negative height
the two shifted logarithms have arguments in \((-\pi/2,0)\),
while the own logarithm has argument in \((0,\pi/2)\).
The chirp in \(Q_s\) is \(+\pi i\), so
\[
                         -3\pi/2<\Im Q_s<\pi.
 \tag{11}
\]
Equation (1) makes \(Q_s\) an integral multiple of \(2\pi i\).
The only such value allowed by (11) is zero.
The uniqueness in (2) identifies this point with the distinguished
branch, without choosing a root by its imaginary part.

## 3. Which side of modulus one follows the outgoing arc

Differentiate \(Y(v)\) in (6) as a rational function of \(v\);
the original rational form, before restricting to the circle,
is used for this derivative. At the crossing set
\[
                            B=(v+1)Y'(v)/Y.
 \tag{12}
\]
Along \(\omega=e^{i\phi}\), one has
\(dv/d\phi=i(v+1)\) and \(d'(\phi)=2\sin\phi>0\).
Equation (7), together with \(P(d_0)=0\) and \(P'(d_0)>0\),
shows that
\[
              \frac d{d\phi}|Y(v(\phi))|^2>0.
 \tag{13}
\]
Since \(|Y|=1\) at the crossing, the same derivative equals
\(2\Re(iB)=-2\Im B\).
Thus \(\Im B<0\); in particular \(Y'(v)\ne0\).

Now move \(Y\) on its original unit circle by increasing \(q\).
Because \(dY/dq=-2\pi iY\), the corresponding local root satisfies
\[
 \frac d{dq}\log|\omega|
   =\Re\frac{-2\pi iY}{(v+1)Y'(v)}
   =2\pi\Im(1/B)>0.                                         \tag{14}
\]
The last sign follows from \(\Im B<0\).
The original strip and lift persist locally.
For all sufficiently small positive \(q-q_0\), (14) therefore gives
\[
           |\omega|>1,\qquad
       \partial_a\Re\Theta(1/2,q)=\log|\omega|>0.
 \tag{15}
\]
These outgoing parameters remain below \(18/25\), by (9).
The branch is holomorphic in a neighborhood of this point, so
the strict derivative sign also persists for \(a>1/2\)
sufficiently close to \(1/2\).

It follows in particular that for these fixed \(q\),
\[
                  \Re\Theta(a,q)>\Re\Theta(1/2,q)
\]
for all sufficiently small positive \(a-1/2\).
The old first-coordinate contraction cannot be extended to the
whole new real rectangle.

This does not contradict the complete finite-source estimate,
which retains the two rates \(\Re\Theta(a,q)\) and \(L(q)\).
Nor does it obstruct a comparison obtained by moving the second
coordinate while retaining the adjacent third-factor action.
It isolates exactly the failed monotonicity claim.

## Direct source versions

| Direct source | SHA-256 | Implication used |
|---|---|---|
| research_mixed_real_unit_pair_zero_lift_branch.md | 4e22a14247e7b11340d9b9ade4774760cd93722f82feb16c12ff2faa1c2b4d1a | Unique original zero-lift branch and its local holomorphic continuation |
| research_mixed_four_conditional_unit_incoming_branch.md | b6c8fdaffd436ec82670ec864629d93d36e7c7a8ae7e81033b684e3f86e92e43 | Original critical polynomial and stationary multiplier identity |

The entire proof and both directly used sources were read in full;
both source hashes match. Independent proof and direct-source review
are required before adoption.
No mathematical numerical evaluation, saved-value arithmetic, test,
import, compilation, or frozen-source edit is used.
