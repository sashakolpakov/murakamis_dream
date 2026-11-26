# The outgoing scalar branch on the entire own-four image

Research addendum, 7 November 2026. The two sector barriers for an
actual last-four reference also control the entire holomorphic scalar
endpoint branch on the original convex own-four image. Its derivative
has a strict uniform bound below one. This is a critical-coordinate
statement; no finite-source or real physical-face sign is inferred.

## 1. The branch and its sector

Keep \(Y=e^{2\pi ix_0}\), \(c=Y^{-1}-1\), and
\[
 O_4=\{\,|s-(.30-.052i)|\le.060,\quad
                       -.102\le\Im s\le-.001\,\}.
 \tag{1}
\]
For every \(s\in O_4\), put \(S=e^{-2\pi is}\).
The original typed inequalities give
\[
 |S|<1,\qquad \Im S<-2/5,\qquad
                   \Re S+\Im S/15<0.
 \tag{2}
\]
These are proved analytically in the
[correlated endpoint](research_mixed_fourier_right_cap_correlated_endpoint.md)
and [annulus protocol](research_mixed_fourier_right_cap_annulus_protocol.md).

By the [half-plane branch theorem](research_mixed_fourier_endpoint_halfplane_branch.md),
the equation
\[
          Q^2-(1+Y^{-1}-S)Q+c=0
 \tag{3}
\]
has a unique nonzero root in \(|Q|<1\), holomorphic on a
neighborhood of the whole compact image of (1). Denote that branch
by \(Q(S)\). There is no independently selected square root.

**Proposition 1.** Throughout \(s\in O_4\),
\[
       Q(S)\in\{R e^{-i\theta}:0<R<1,\ \pi/2<\theta<2\pi/3\}.
 \tag{4}
\]
Consequently the single holomorphic logarithm
\[
                    q(s)=-\frac{\Log Q(e^{-2\pi is})}{2\pi i}
 \tag{5}
\]
has
\[
                  1/4<\Re q(s)<1/3,\qquad \Im q(s)<0.
 \tag{6}
\]
Its branch agrees with the original outgoing coordinate at every
actual reference.

*Proof.* Write \(\alpha=1-\cos\phi/\rho\),
\(d=\sin\phi/\rho\), where \(Y=\rho e^{i\phi}\).
The exact identity (3) gives
\[
 \Im S=-d+R\sin\theta+
                    \frac{\alpha\sin\theta+d\cos\theta}{R}.
 \tag{7}
\]
On the ray \(\theta=\pi/2\), the lower-barrier calculation of the
[real-strip theorem](research_mixed_fourier_endpoint_real_strip.md),
equations (7), (11)--(12), gives \(\Im S>-2/5\).
It uses only \(0<R<1\) and the original bounds for \(\alpha,d\),
not a preexisting type constraint on \(q\).
On the ray \(\theta=2\pi/3\), that theorem's equations
(13)--(14) similarly give \(\Im S<-1\).
Both contradict (2). Thus neither boundary ray can be crossed.

The domain \(O_4\) is convex, hence connected. It contains the
own leg of an already existing actual last-four reference, for
example one with incoming parameter in \(K_3\). At that anchor
the real-strip theorem places \(Q\) strictly in (4).
The continuous nonzero branch of (3) cannot leave the sector
without crossing one of its rays. Its modulus remains below one
by the half-plane theorem. This proves (4).

The sector avoids the cut of the principal logarithm, which proves
(5)--(6) and holomorphy on a neighborhood of the compact domain.
At actual points its argument lies in the original range, so this
decoding is the same original outgoing branch. \(\square\)

## 2. A uniform derivative and its precise scope

**Proposition 2.** The endpoint map in (5) satisfies
\[
 \left|\frac{dq}{ds}\right|<\frac{41}{60}
       \quad(s\in O_4),\qquad
 |q(s_1)-q(s_2)|\le\frac{41}{60}|s_1-s_2|
       \quad(s_1,s_2\in O_4).
 \tag{8}
\]

*Proof.* Differentiate the original rational identity
\(S=1+Y^{-1}-Q-c/Q\). The nonzero denominators already
proved in the half-plane theorem give exactly
\[
                    \frac{dq}{ds}=\frac{SQ}{c-Q^2}.
 \tag{9}
\]
By (4), \(Q^2\) is strictly in the upper half-plane.
But \(\Im c=-d\), and the real-strip parameter bounds give
\(d>60/41\). Therefore
\[
 |c-Q^2|\ge|\Im(c-Q^2)|=d+\Im Q^2>60/41,
 \qquad |SQ|<1.
 \tag{10}
\]
Equations (9)--(10) prove the derivative bound. The straight
segment between \(s_1,s_2\) stays in the convex domain (1);
integrating the derivative on that segment proves (8).
\(\square\)

No assertion \(q(O_4)\subset O_4\) is made: (6) bounds the
real part and the sign of the height, but supplies no new lower
height bound. Hence (8) is a Lipschitz contraction from this domain
into the complex plane, not a justified self-map iteration.
The auxiliary matching coordinate and the finite right-cap
halfweights remain those of the original source.

In particular (8) does not bound a change from \(\Im q<0\)
to the real physical row. It neither pays the outgoing real faces
nor replaces the exact finite Wall solution by its critical branch.
