# Two upper roots at the beginning of the real second arc

Private written observation, 11 November 2026. The original conditional
cubic acquires a second upper-half-plane root when its outgoing real
angle moves just past one half. This prevents extending the old
“unique upper root” selection rule to that side. It does not disprove
the desired finite-source estimate.

The new root has logarithmic lift \(-2\pi i\), rather than zero.
Thus the original zero-lift branch is still distinguished locally.
Controlling a complete finite contour over the whole new interval
requires a further argument.

Author-frozen after full proof and direct-source readback. Independent
review is required before adoption. No frozen source or public document
is changed.

## 1. The unchanged polynomial and phase

For \(r_N=e^{-2\pi i/N}\), retain
\[
 C_{1,N}(X,Y)=\sum_{j=0}^{N-1}
       \frac{X^{-j}(r_NX;r_N)_j(r_NY;r_N)_j}{(r_N;r_N)_j^3}.
\]
Its original phase, with its original strip logarithms, is
\[
 Q(s;a,q)=g(a+s)+g(q+s)-3g(s)-g(a)-g(q)+2\pi ias,
 \qquad g'(w)=\operatorname{Log}(1-e^{-2\pi iw}).
\]
Writing \(X=e^{-2\pi ia}\), \(Y=e^{-2\pi iq}\), and
\(v=e^{2\pi is}\), the exact exponential critical equation is
\[
 F(v;X,Y):=v(v-X)(v-Y)-X(v-1)^3=0.                         \tag{1}
\]
This is equation (7) of
[the unit-incoming branch theorem](research_mixed_four_conditional_unit_incoming_branch.md).
That theorem assumes \(\Im Y<0\), which for unit \(Y\) is
\(0<q<1/2\). It proves a unique upper root and fixes its logarithmic
lift to \(Q_s=0\).

We examine the boundary input \(a=1/2\), so \(X=-1\), and the
outgoing path
\[
 q=1/2+\varepsilon,\qquad
 Y(\varepsilon)=-e^{-2\pi i\varepsilon}.
                                                               \tag{2}
\]
All claims below hold for a sufficiently small fixed
\(\varepsilon>0\), in particular within the desired interval
\(q\in[1/2,18/25]\).

## 2. The real root moves into the upper half-plane

At \(\varepsilon=0\), equation (1) becomes
\[
                   F_0(v)=2v^3-v^2+4v-1=0.               \tag{3}
\]
For real \(v\),
\[
          F_0'(v)=6v^2-2v+4
                  =6(v-1/6)^2+23/6>0 .
\]
Since \(F_0(0)<0<F_0(1)\), there is exactly one real root
\(r\in(0,1)\). The remaining roots form a nonreal conjugate pair.
All three roots are simple: the real root has nonzero derivative,
and a multiple nonreal root would require its conjugate to have
the same multiplicity, exceeding degree three.

Let \(v_r(\varepsilon)\) be the local analytic continuation of the
real root. The implicit derivative of (1), with \(X=-1\), is
\[
 F_Y=-v(v+1),\qquad
 Y'(0)=2\pi i.
\]
Consequently
\[
 v_r'(0)=
       \frac{2\pi i\,r(r+1)}{6r^2-2r+4}.                  \tag{4}
\]
Its imaginary part is strictly positive. Taylor's formula therefore
gives \(\Im v_r(\varepsilon)>0\) for all sufficiently small positive
\(\varepsilon\).

The original nonreal roots also continue analytically. Their
imaginary parts retain their signs in a sufficiently small common
neighborhood. Hence:

**Proposition 1.** At \(X=-1\) and
\(Y=-e^{-2\pi i\varepsilon}\), with every sufficiently small positive
\(\varepsilon\), equation (1) has exactly two simple upper-half-plane
roots and one simple lower-half-plane root.

The assertion is open in the incoming parameter as well. For each
such fixed \(\varepsilon\), sufficiently small positive changes from
\(a=1/2\) preserve the three imaginary-part signs and simplicity.
Thus the failure of unique-upper-root selection is not confined to
the first-input endpoint.

## 3. The extra root is on a different logarithmic lift

The real root equation in (3) can be written
\[
                  r(r+1)^2=(1-r)^3.                     \tag{5}
\]
Put \(h=-\log r/(2\pi)>0\). The logarithmic coordinate of this root
is \(s=ih\). To evaluate the phase lift, approach this point with
\(\Re s>0\), keeping the original strip branches.

As \(\Re s\downarrow0\),
\[
\begin{split}
 g'(s)&\longrightarrow\log(e^{2\pi h}-1)+i\pi,\\
 g'(1/2+s)&\longrightarrow\log(1+e^{2\pi h}).
\end{split}
\]
The first sign follows because
\(1-e^{-2\pi i(u+ih)}\), for \(u>0\) small, approaches the negative
real axis from above. Substituting these limits and \(a=q=1/2\)
into \(Q_s\) gives
\[
 Q_s\longrightarrow
   \log\frac{(1+r^{-1})^2}{(r^{-1}-1)^3}-2\pi i
                         =-2\pi i,                      \tag{6}
\]
where the real logarithm vanishes by (5).

For sufficiently small \(\varepsilon>0\), equation (4) puts
\(v_r(\varepsilon)\) in the upper half-plane near the positive
real axis. Choose the logarithm continuous from \(r\), and let
\(s_r(\varepsilon)=\log v_r(\varepsilon)/(2\pi i)\).
Then
\[
 0<\Re s_r(\varepsilon)<1/2,\qquad
 0<\Re(a+s_r)<1,\qquad 0<\Re(q+s_r)<1.
\]
These are strict for sufficiently small positive \(\varepsilon\);
all phase logarithms are consequently on their original strips.
Equation (1) implies \(Q_s\in2\pi i\mathbb Z\).
Continuity and the boundary value (6) fix that integer:
\[
                  Q_s(s_r;a,q)=-2\pi i.                 \tag{7}
\]

Meanwhile, the original upper nonreal root at \(\varepsilon=0\)
is the limit of the unit-incoming theorem's upper root as
\(\varepsilon\uparrow0\) from below. Its logarithmic coordinate
has real part strictly between zero and one half, because its
argument is strictly between zero and \(\pi\). Its shifted
arguments therefore remain within the original strips at the
boundary and in a fixed small neighborhood. The original
zero lift continues without change:
\[
                        Q_s(s_{\mathrm{old}};a,q)=0.     \tag{8}
\]

**Proposition 2.** In this local neighborhood the two upper roots
are distinguished by their original logarithmic lifts: the continued
old root has lift zero, whereas the root coming from the positive
real axis has lift \(-2\pi i\).

No new period constant is inserted in (6)--(8). In particular, the
extra root cannot simply be substituted as the zero-mode critical
point. Conversely, its nonzero lift does not authorize discarding
it from every finite sampling correction.

## 4. The missing estimate on the middle first arc

The missing middle-arc source estimate concerns the complete
\(C_{1,N}(e^{-2\pi ia},e^{-2\pi iq})\), uniformly for
\[
                 1/2\le a\le7/8,\qquad
                 1/2\le q\le18/25,
\]
after multiplication by the original cap, Fourier factors and
third conditional kernel. One possible route is a conditional
bound in terms of the already calibrated first profiles. Its proof
must include every physical
index, the two unweighted joins, the horizontal sampling corrections,
and all four weighted vertical halves. Alternatively, a direct joint
cap/kernel/third estimate with the original affine normalization
would suffice.

The old branch theorem alone supplies neither alternative. Proposition
1 gives an exact reason why its upper-half-plane root count cannot be
continued unchanged. Proposition 2 gives a possible replacement local
selection rule, but proves neither its global continuation nor the
required finite-source inequalities. The far first arc is treated
separately by positive bounds; this observation concerns the missing
middle arc.

## Direct source versions

| Direct source | Used implication | SHA-256 |
|---|---|---|
| research_mixed_four_conditional_unit_incoming_branch.md | Exact polynomial (1), original strip phases, and the unique upper zero-lift branch on the lower outgoing semicircle | b6c8fdaffd436ec82670ec864629d93d36e7c7a8ae7e81033b684e3f86e92e43 |

The author read the entire proof and the complete directly used branch
source, including its zero-lift argument, and checked its binding.
No mathematical numerical evaluation, saved-value arithmetic, test,
import, compilation or frozen-source edit was used.

