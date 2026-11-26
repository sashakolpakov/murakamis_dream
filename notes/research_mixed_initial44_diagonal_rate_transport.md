# Diagonal rate transport for the initial four/four source

Private written deduction, 10 November 2026. Several original cap
and conditional rates decrease on a right/up diagonal which resets
the actual negative first height to zero before real part \(7/10\).
The quantitative conditional estimate below is a shared hand
derivation with the root reviewer. The cap estimates and all-row
comparison retain the original finite sources.

The upper private cap alias is explicitly not paid here. These
lemmas therefore do not yet bound the complete outer connector.

## 1. Source, path and logarithmic conventions

Use the actual initial four/four reference and original source of
[the complete lower-right pair](research_mixed_initial44_lower_right_complete_pair.md):
\[
 -.078<c<-.020,\qquad b=z+id,\quad
 .22\le z\le .45,\quad -.102<d<-.001.
 \tag{1}
\]
Its unchanged factors are
\[
 U_{1,N}(w,X)=\sum_{i=0}^{N-1}
 H_N(w,q_N^{-i})\frac{(q_NX;q_N)_i}{P_i^2},
\quad
 C_{1,N}(X,Y)=\sum_{j=0}^{N-1}
 \frac{X^{-j}(q_NX;q_N)_j(q_NY;q_N)_j}{P_j^3},
 \tag{2}
\]
where \(q_N=e^{-2\pi i/N}\), \(P_i=(q_N;q_N)_i\).
The entire first weight is \(d_N(X)\), and the outside outgoing
factor is \(|d_N(Y)|^{1/2}\).

Consider the fixed path
\[
 a(\tau)=\frac{31}{50}+ic+(1+i)\tau,\qquad
                    0\le\tau\le-c.
 \tag{3}
\]
It ends at \(31/50-c<7/10\), at height zero. Write
\[
 a=x+ih,\quad X=e^{-2\pi ia}=r e^{i\phi}.
\]
Throughout the path,
\[
 \frac35<r\le1,\qquad
 \frac{31}{50}\le x<\frac7{10},\qquad
          \frac{3\pi}{5}<\phi\le\frac{19\pi}{25}<\frac{4\pi}{5}.
 \tag{4}
\]
The radius bound is the same written exponential bound used in
the lower-right action theorem. For a function of \(a\), denote its
derivative along (3) by \(\partial_{\nearrow}=\partial_x+\partial_h\).

For \(0<r\le1\), let
\[
 F(r,\theta)=\log|1-re^{i\theta}|-\Arg(1-re^{i\theta}).
 \tag{5}
\]
The argument is the original disk argument, with its continuous
integrated limits at a unit-circle zero. On \(0<\theta<\pi\),
\[
 F_\theta=\frac{r(\sin\theta+\cos\theta-r)}
                    {1+r^2-2r\cos\theta},\qquad
 F_r=\frac{r-\cos\theta+\sin\theta}
                    {1+r^2-2r\cos\theta}.
 \tag{6}
\]
For the original cap phase \(\Psi(e,a)\), all terms other than its
incoming factorial quotient are independent of \(a\). Thus, with
\(e=u+i\eta\), \(q=e^{2\pi\eta}\),
\[
 \partial_{\nearrow}\Re\Psi(e,a)
       =F(rq,\phi-2\pi u)-F(r,\phi)
 \tag{7}
\]
whenever \(\eta\le0\). Across the numerator period wall this remains
the derivative of the continuous zero-safe rate: \(h+\eta\le0\),
so the positive part of the period-multiplier rate is zero.

## 2. Every nonpositive-height retained cap point decreases

**Lemma 1.** If \(.27\le u\le.49\) and \(\eta\le0\), then the
right side of (7) is strictly negative throughout (3).

*Proof.* Put \(\theta=\phi-2\pi u\).
If \(\theta\le0\), then \(|\theta|<2\pi/5<\phi\).
For \(0\le R\le r\), convexity of
\(1+R^2-2R\cos\theta\) puts its maximum at \(R=0\) or \(r\).
Both values are less than \(|1-re^{i\phi}|^2\), since the latter
is greater than one and \(\cos\theta>\cos\phi\).
Also \(\Arg(1-Re^{i\theta})\ge0\), whereas
\(\Arg(1-re^{i\phi})<0\). These facts prove the claim.

If \(\theta>0\), then
\[
                   0<\theta\le\frac{11\pi}{50}<\frac\pi4.
 \tag{8}
\]
As a function of \(R\), \(F(R,\theta)\) has at most one
stationary point, a minimum, by the second formula in (6).
Its maximum on \([0,r]\) is therefore at zero or \(r\).
The first formula in (6) shows that \(F(r,\theta)\) increases
for \(0\le\theta\le\pi/4\). Moreover \(F(r,\pi/4)>0\), since
its radial derivative is positive. Hence
\[
                       F(rq,\theta)\le F(r,\pi/4).
 \tag{9}
\]
On \([3\pi/5,4\pi/5]\), the angular derivative in (6) changes
sign at most once, from positive to negative. Consequently it
is enough to prove
\[
 F(r,\pi/4)<F(r,3\pi/5),\qquad
 F(r,\pi/4)<F(r,4\pi/5).
 \tag{10}
\]

Here is a fully written radial comparison. If \(b>\pi/4\), the
numerator of \(F_r(r,\pi/4)-F_r(r,b)\), after multiplication
by its two positive denominators, is
\[
 (\cos b-\sin b)
 +(-\cos b+\sqrt2-\sin b)r^2
 +2r\sin(b-\pi/4).
 \tag{11}
\]
For \(b=3\pi/5\), this is greater than
\[
 -\frac{13}{10}+\frac7{10}r^2+\frac74r\ge\frac1{500}>0
                         \qquad(r\ge3/5).
 \tag{12}
\]
Indeed \(-5/16<\cos b<-3/10\), \(\sin b<24/25\),
\(\sqrt2>7/5\), and
\(\sin(7\pi/20)=\cos(3\pi/20)>7/8\).
For \(b=4\pi/5\), (11) is greater than
\[
 -\frac32+\frac32r^2+\frac{19}{10}r
                         \ge\frac9{50}>0.
 \tag{13}
\]
Use \(-5/6<\cos b<-4/5\), \(\sin b<3/5\), and
\(\sin(11\pi/20)=\cos(\pi/20)>19/20\).
All these witnesses follow from the elementary half-angle formulas
and \(1-t^2/2<\cos t\), with \(\pi<22/7\).

Thus each difference on the right of (10) minus its left decreases
with \(r\), and it suffices to check \(r=1\). There
\[
 F(1,b)-F(1,\pi/4)
 =\log\frac{\sin(b/2)}{\sin(\pi/8)}
                         -\frac{b-\pi/4}{2}.
 \tag{14}
\]
For \(b=3\pi/5\), the sine ratio exceeds two, so this is positive
by \(\log2>2/3>7\pi/40\).
For \(b=4\pi/5\), the ratio exceeds \(12/5\):
\(\sin(2\pi/5)>19/20\), \(\sin(\pi/8)<39/100\), and
\(95/39>12/5\).
The first sine bound follows by squaring from \(\sqrt5>111/50\);
the second follows from \(\sqrt2>7/5\). Finally
\[
 \log(12/5)=2\operatorname{artanh}(7/17)
 >\frac{14}{17}+\frac{686}{14739}
 =\frac{12824}{14739}>\frac{121}{140}>\frac{11\pi}{40}.
 \tag{15}
\]
The middle cross-product difference is \(11941>0\).
This proves (14), then (10) and the lemma. \(\square\)

In particular this transports the original main cap, lower alias,
and nonpositive-height parts of the retained private joins. Their
sampling penalties are independent of the outer parameter.

## 3. A uniform growth ceiling for every real cap row

For a real physical cap index \(e\), let \(\mathcal R_1(e,a)\)
be its original complete-coefficient rate from the lower-right
physical-row theorem. Its incoming derivative is exactly (7)
with \(q=1\). No modulus is substituted inside the full \(H_N\).

**Lemma 2.** For every real \(e\), with angles interpreted periodically,
\[
                 \partial_{\nearrow}\mathcal R_1(e,a)
                                      <\frac{31}{140}.
 \tag{16}
\]

*Proof.* Negative angles in (5) have no larger value than the
corresponding positive angle. The angular maximum of \(F(r,\cdot)\)
is at a point \(\theta_*\in[\pi/2,2\pi/3]\), determined by
\[
                        \sin\theta_*+\cos\theta_*=r.
 \tag{17}
\]
Again \(F(r,\phi)\) is no smaller than the lesser of its values at
\(3\pi/5,4\pi/5\).
Between \(\theta_*\) and \(3\pi/5\), formula (6) gives
\(|F_\theta|<1/3\): on \([\pi/2,2\pi/3]\),
\(|\sin\theta+\cos\theta-r|<2/3\) and
\(r/(1+r^2-2r\cos\theta)\le1/2\).
The length is at most \(\pi/10\), so this loss is less than
\(\pi/30<31/140\).

For the other endpoint, differentiation of the maximum in \(r\)
using (17) gives
\[
 \frac{d}{dr}F(r,\theta_*)=\frac1{\sin\theta_*}\ge1.
 \tag{18}
\]
At \(b=4\pi/5\), \(F_r(r,b)<1\). Indeed the denominator in
(6) minus its numerator is
\[
 r^2-r+1+(1-2r)\cos b-\sin b
                         >\frac34-\frac35>0.
 \tag{19}
\]
The maximum-to-endpoint loss therefore increases with \(r\).
At \(r=1\) it is
\[
 \log\frac{\sin(\pi/4)}{\sin(2\pi/5)}+\frac{3\pi}{20}
 <\log(3/4)+\frac{3\pi}{20}
 <-\frac14+\frac{33}{70}=\frac{31}{140}.
 \tag{20}
\]
The sine-ratio inequality follows by squaring from \(19<9\sqrt5\).
This proves (16), including its integrated limits at zeros.
\(\square\)

## 4. Quantitative decay of the original conditional action

Let \(t_*(a,b)\) and \(\Theta(a,b)=Q(t_*;a,b)\) be the original
conditional critical point and action of
[the algebraic transport theorem](research_mixed_four_conditional_algebraic_transport_domain.md).
Its phase remains
\[
 Q(t;a,b)=g(a+t)+g(b+t)-3g(t)-g(a)-g(b)+2\pi iat.
 \tag{21}
\]
Put \(v=e^{2\pi it_*}\) and
\(\omega=(v-X)/(1-X)\). The cited theorem, or its
[enlarged-domain version](research_mixed_four_conditional_positive_incoming_action.md),
gives \(\omega\) in the open upper unit disk and
\(\Theta_a=\Log\omega\) on the original lift.

**Lemma 3.** On (3),
\[
                    \partial_{\nearrow}\Re\Theta<-\frac14.
 \tag{22}
\]

*Proof.* Put \(A=-\log|\omega|+\Arg\omega\).
Suppose \(A\le1/4\). The elementary chord bound gives
\[
 |1-\omega|
 \le(1-|\omega|)+|\omega|\Arg\omega
 \le A\le\frac14,\qquad |\omega|\ge\frac34.
 \tag{23}
\]
The identity \(v=1-(1-X)(1-\omega)\), with \(|X|\le1\), gives
\(|v-1|\le1/2\) and \(|v|\ge1/2\).
The exact cubic, without a new logarithmic lift, also gives
\[
 Y=v-\frac{X(1-X)^2(\omega-1)^3}{v\omega}.
 \tag{24}
\]
Thus \(|Y-v|\le1/6\), and
\[
                         \Re Y\ge1-\frac12-\frac16=\frac13.
 \tag{25}
\]
But the actual outgoing coordinate in (1) satisfies
\[
 \Re Y\le\max\{0,\cos(11\pi/25)\}
 =\sin(3\pi/50)<\frac15.
 \tag{26}
\]
This contradiction proves \(A>1/4\), which is (22).
\(\square\)

Combining (16) and (22) gives the useful strict joint inequality
\[
 \partial_{\nearrow}\{\mathcal R_1(e,a)+\Re\Theta(a,b)\}
                                      <-\frac1{35}.
 \tag{27}
\]
It applies also to compact cap rows below the retained cap cut.
Their omission from the cap contour does not invalidate this
comparison.

## 5. All original ordinary physical rows decrease

Let \(\mathcal E(t;a,b)=\Re Q(t;a,b)\) at real physical index
\(t\in[0,1]\), with its continuous periodic factorial rate.
The outgoing factors are constant along (3). Set
\[
 D=|1-X|,\quad N_t=|1-Xe^{-2\pi it}|,\quad
 A(q)=\Arg(1-e^{-2\pi iq}).
\]
The exact derivative is
\[
 \partial_{\nearrow}\mathcal E
   =\log(N_t/D)+A(a)-A(a+t)-2\pi t.
 \tag{28}
\]
In particular the incoming carrier has not been dropped.

If \(0<t\le1-x\), use the exact finite product
\[
 X^{-j}(q_NX;q_N)_j
                   =\prod_{\ell=1}^j(X^{-1}-q_N^\ell).
 \tag{29}
\]
For \(T=|X|^{-1}\ge1\) and \(\theta=2\pi(x+s)\in[\pi,2\pi]\),
the derivative of the squared individual modulus along (3) is
\[
 4\pi T(\sin\theta+\cos\theta-T)\le0.
 \tag{30}
\]
It is strict away from the isolated unit-radius endpoint zero.
Moreover its logarithmic derivative is at most \(-\pi\), because
\[
 2T(T-\cos\theta-\sin\theta)
 -(T^2+1-2T\cos\theta)=T^2-1-2T\sin\theta\ge0.
 \tag{31}
\]
Integration gives
\[
                   \partial_{\nearrow}\mathcal E\le-\pi t.
 \tag{32}
\]
The isolated zero at the unit-radius endpoint is interpreted by
the original integrated upper rate.

If \(1-x\le t\le3/2-x\), the disk arguments satisfy
\(A(a)\le0\), \(A(a+t)\ge0\), while \(D>1,N_t\le2\).
Since \(t\ge3/10\), (28) is less than
\[
                              \log2-\frac{3\pi}{5}<0.
 \tag{33}
\]
If \(3/2-x\le t\le1\), both arguments lie in \([-\pi/2,0]\)
and \(t\ge4/5\), so (28) is at most
\[
                       \log2+\frac\pi2-\frac{8\pi}{5}<0.
 \tag{34}
\]
These are the same original periodic disk arguments on both sides
of a wall, with their continuous integrated limits.

Combining (16), (32)--(34) shows, for every \(t\ge2/25\),
\[
 \partial_{\nearrow}\{\mathcal R_1(e,a)+\mathcal E(t;a,b)\}
                                      <-\frac1{35}.
 \tag{35}
\]
For (32), use \(2\pi/25>1/4\); (33)--(34) give larger losses.
For the low ordinary block \(0\le t\le2/25\), the original real
row ratio exceeds one uniformly on the present path. Indeed
\(x+t\in[.62,.78]\), \(z+t\in[.22,.53]\);
the first squared numerator is greater than one after chirp
folding, the second is bounded below by the unrestricted radial
minimum at the angle \(11\pi/25\), and the own denominator is
\((2\sin\pi t)^6\).
More explicitly the second squared factor exceeds \(9/10\),
whereas \(2\sin(2\pi/25)<16/25<2/3\); the ratio is greater
than \((9/10)/(2/3)^6>1\).
Here the first numerator bound uses \(T\ge1\),
\(\cos(2\pi(x+t))<1/5\), so
\(|T-e^{-2\pi i(x+t)}|^2>8/5>1\).
Thus this block reduces to its current \(2/25\) cut, including
the harmless half-mesh rounding. No low-index factorial is
divided out at a zero.

## 6. What these comparisons do and do not propagate

All bounds above are for the original complete coefficient profiles,
their original critical action, or actual finite row products. They
can be integrated from \(31/50+ic\), where the adopted complete
lower-right proof supplies the applicable calibrated profile bounds.
Specifically, the paid nonpositive-height cap contour profiles
remain paid when multiplied by the conditional critical exponential
or by the ordinary low/high/cut blocks already calibrated in the
physical-row theorem. The paid compact cap-row blocks remain paid
against the critical exponential by (27), and against those same
ordinary physical blocks by (35) and the low-cut reduction.
The constant true-cap-end ceilings can be combined with either
conditional decrease.
Although the derivative lemma covers every ordinary physical row,
it does not supply an initial calibrated bound for the central real
rows that were handled coherently in the original conditional contour.

The full first weight has upper rate zero for \(|X|\le1\), including
the real endpoint, so this comparison does not remove it. The outside
outgoing halfweight is unchanged and is never divided out. These
pointwise rate inequalities are parity independent, and their strict
gaps absorb the existing finite half-grid roundings and polynomial
costs. The all-real-color coefficient upper bounds used by the bound
sources remain the same.

There is still an unpaid profile: the cap's upper horizontal private
alias at height \(+.04\), and any finite-current comparison needed
to replace it. A bound for its weighted vertical sides alone does
not bound that horizontal alias. In particular, a reduction to a
central real cap profile is not enough unless that profile has its
own calibrated bound. Nor does agreement of two candidate cap
interpolants on physical indices justify replacing the retained
main integral off-grid.

Accordingly this note does not assert a full bound on the diagonal
outer connector, the remaining real right arc, either whole Fourier
period, or a closed-knot asymptotic. Any ordinary-color neighborhood
or differentiated full-connector conclusion must wait for that
complete finite-source assembly.

## Frozen source bindings

All proofs are written; no mathematical numerical evaluation was
performed.

| Direct source | SHA-256 |
|---|---|
| research_mixed_first_four_cap_lower_right_horizontal.md | 4d41a967edabf0710fc7b04b723bb3e2fb7a407d44bb5a0fc1678e3f9ee5ee6e |
| research_mixed_four_conditional_algebraic_transport_domain.md | 4788b140b0ab435bb5951db75aadad03376ddaf3bfb6378b8f17242253b7ace0 |
| research_mixed_four_conditional_positive_incoming_action.md | e8608019efbd73b2c05e6ede084b4781182259dc0e32be12b4610c66f352d371 |
| research_mixed_initial44_lower_right_physical_rows.md | 6665075b979801c0d5b9296738508be527bddd8827e3aea004b9ff1e7a60f702 |
| research_mixed_initial44_lower_right_complete_pair.md | 631492d2c8c6bec47e95ae6c84641429ba64256201fc7dd459aa403872a93f7b |
