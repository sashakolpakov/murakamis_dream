# Transport of a fixed negative-height profile on the real pair

Private written proof, 11 November 2026. This note gives elementary
inequalities for the phase of the own-four conditional sum. It does
not bound that complete sum: its physical rows and contour connections
remain separate obligations.

## 1. Definitions

For real \(a,q\), use the phase
\[
 Q(s;a,q)=g(a+s)+g(q+s)-3g(s)-g(a)-g(q)+2\pi ias.
 \tag{1}
\]
In the lower half-plane take the analytic logarithm
\[
 g'(w)=\log(1-e^{-2\pi iw})
      =-\sum_{n\ge1}\frac{e^{-2\pi inw}}n .
 \tag{2}
\]
The primitive is normalized to have continuous value \(g(0)=0\).
Explicitly,
\[
 g(w)=\frac1{2\pi i}\sum_{n\ge1}
                       \frac{e^{-2\pi inw}-1}{n^2}.
\]
This series converges uniformly on the closed lower half-plane,
since its summands have modulus at most \(2/n^2\).
It is periodic there; its real boundary values are the integrals
of \(\log(2|\sin\pi x|)\). Formula (1) at real arguments uses those
continuous limits. The estimates below depend only on derivatives
or differences with identical normalizations.

Write \(s=t+i\eta\), \(\rho=e^{2\pi\eta}\), and
\[
 D_t(\rho)=|1-\rho e^{-2\pi it}|,\qquad
 N_x(t,\rho)=|1-\rho e^{-2\pi i(x+t)}|.
 \tag{3}
\]
For \(\eta<0\), direct differentiation gives
\[
 \partial_t\Re Q
   =\log\frac{N_aN_q}{D_t^3},\qquad
 \partial_q\Re Q
   =\log\frac{N_q}{|1-e^{-2\pi iq}|}.
 \tag{4}
\]
The real \(a\) in the chirp is important: the chirp contributes
zero to the first real derivative in (4).

## 2. The horizontal part beyond one quarter decreases

**Lemma 1.** If \(a,q\in[1/2,1)\), \(1/4\le t\le1/2\), and
\(\eta<0\), then
\[
 \partial_t\Re Q(t+i\eta;a,q)\le-\log D_t(\rho)<0.
 \tag{5}
\]

For either \(x=a\) or \(x=q\),
\[
             -t\le x+t-1\le t .
\]
Indeed the lower inequality is \(x+2t\ge1\), and the upper
one is \(x\le1\). The cosine decreases with distance from zero
on \([-1/2,1/2]\). Thus
\[
 \cos 2\pi(x+t)\ge\cos2\pi t,\qquad N_x(t,\rho)\le D_t(\rho).
\]
Also \(\cos2\pi t\le0\), so \(D_t^2\ge1+\rho^2>1\).
Substitution into (4) proves (5).

In particular, a maximum on \([\ell,r]\), where
\(0<\ell\le1/4\le r\le1/2\), is already attained on
\([\ell,1/4]\). No contour is moved in making this comparison.

## 3. The short horizontal part decreases as the second input moves

Put \(h_0=\log2/(2\pi)\).

**Lemma 2.** For
\[
 0\le t\le1/4,\qquad -h_0\le\eta<0,\qquad
                      1/2\le q\le7/8,
 \tag{6}
\]
one has \(N_q(t,\rho)\le|1-e^{-2\pi iq}|\). Consequently
\(\partial_q\Re Q\le0\), independently of the real first input.

Here \(1/2\le\rho\le1\). The squared numerator is a convex
quadratic in \(\rho\), so it suffices to check \(\rho=1/2,1\).
Set \(\theta=2\pi q\), \(\tau=2\pi t\).
For \(\rho=1\), the bounds
\[
                 q\le q+t\le2-q
\]
give \(\cos(\theta+\tau)\ge\cos\theta\), which proves the claim.

For \(\rho=1/2\), the required inequality is
\[
             \cos(\theta+\tau)\ge2\cos\theta-\frac34.
 \tag{7}
\]
On \(\theta\in[\pi,7\pi/4]\), the interval
\([\theta,\theta+\pi/2]\) contains no interior minimum of cosine.
Its minimum is therefore at one of its endpoints:
\(\cos\theta\) or \(-\sin\theta\).
The first endpoint satisfies (7), since
\(\cos\theta\le1/\sqrt2<3/4\).
For the second it is enough to show
\[
                        2\cos\theta+\sin\theta<3/4.
\]
On \([\pi,3\pi/2]\) the left side is nonpositive. On
\([3\pi/2,7\pi/4]\) it increases, since its derivative
\(-2\sin\theta+\cos\theta\) is positive. Its final value is
\(1/\sqrt2<3/4\). This proves (7) and the lemma.

**Corollary 3.** Fix \(a\in[1/2,1)\),
\(-h_0\le\eta<0\), and \(0<\ell<r\le1/2\) with
\(\ell\le1/4\). Then
\[
 B(q)=\max_{\ell\le t\le r}\Re Q(t+i\eta;a,q)
 \tag{8}
\]
is nonincreasing on \(q\in[1/2,7/8]\).

Lemma 1 reduces the maximum to
\([\ell,\min(r,1/4)]\). On this fixed interval every profile
is nonincreasing by Lemma 2; taking its maximum preserves
that order. This does not follow a critical point.

The same conclusion holds at \(\eta=0\), with continuous
integrated rates. To prove it, let \(\eta\uparrow0\) in the
inequality between two values of \(q\). The real parts of the
primitives converge uniformly on the compact real parameter
sets, including their logarithmic zeros, and so do their
maxima on the compact interval. No derivative or local
Lipschitz property at a real zero is asserted.

## 4. A bound for the deeper lower weighted segments

**Lemma 4.** Suppose
\[
 \frac12\le a\le\frac78,\quad \frac12\le q\le\frac78,\quad
 0<t<\min(1/2,1-a),\quad \eta\le-h_0 .
 \tag{9}
\]
Then, on the logarithms (2),
\[
 \partial_\eta\{\Re Q(t+i\eta;a,q)+2\pi\eta\}
                                  \ge\frac{\pi}{12}.
 \tag{10}
\]

The incoming argument \(a+t\) lies in \((1/2,1)\), so
\(\arg(1-\rho e^{-2\pi i(a+t)})\le0\). The own argument
lies in \((0,1/2)\), so
\(\arg(1-\rho e^{-2\pi it})\ge0\).
For \(0<\rho\le1/2\), every point of the disk with center
one and radius \(\rho\) has argument at most
\(\arcsin\rho\le\pi/6\).
Writing \(I=\Im Q_s\), we therefore obtain
\[
 I\le2\pi a+\frac{\pi}{6}
      \le\frac{7\pi}{4}+\frac{\pi}{6}
      =\frac{23\pi}{12}.
\]
The Cauchy--Riemann equations give
\(\partial_\eta\Re Q=-I\); this proves (10).

In particular, for \(T\ge h_0\), integration yields
\[
 \Re Q(t-iT;a,q)-2\pi T
 \le \Re Q(t-ih_0;a,q)-2\pi h_0
                       -\frac{\pi}{12}(T-h_0).
 \tag{11}
\]
This estimates a weighted profile, with its sampling penalty
retained. It does not remove that contour term from a finite identity.

## 5. What these statements do and do not supply

Corollary 3 compares a fixed horizontal profile with its value at
\(q=1/2\) all the way to \(q=7/8\). Lemma 4 bounds deeper
weighted profiles without transporting them in \(q\).
These are possible inputs to extending the first conditional
estimate past \(18/25\).

They do not yet bound every connecting segment, positive-height
sampling term, physical row, cap, or following conditional factor.
In particular, shortening the interval on which a maximum is
computed is not a license to shorten the exact contour and omit
its additional connections. No complete finite-source estimate,
nonzero coefficient, or knot-volume identity is claimed here.

The proof is self-contained from (1)--(2), and imports no
mathematical assertion from another project note. Its phase is
the same expression as equation (3) in
research_mixed_443_real_first_fixed_half_contour.md,
version e65a5c9d69db49c633b06b02c070e9fa005566ad07ec02dd91d7bb182618f950.
That reference specifies the intended application, not an
additional premise of the inequalities proved here.

No numerical evaluation, test, import, or compilation is used.
The author has read the complete proof and checked the displayed
phase against its stated application. Independent complete review
is required before adoption.
