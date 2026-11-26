# The retained-index rate after the actual outgoing contraction

Research deduction, 7 November 2026. The completed half-degree Wall
theorem sums the outgoing physical index before any modulus is taken.
The remaining incoming polynomial is kept through its entire period,
including its zeros and the crossing of \(\Re a+s=1\). The resulting
real rate decreases on \(1/2\le s\le3/4\). On the remaining compact
interval its maximum reduces to endpoints and a finite algebraic
candidate set. No rate value or candidate is evaluated here.

This is an upper-envelope reduction for the original finite source.
The middle-rate comparison with the actual supporting plane remains
unproved; no whole-cap or knot-invariant lower bound is inferred.

## 1. A zero-safe upper rate for the exact remaining rows

Use the original parameters and allocation
\[
 r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad
 X=e^{-2\pi ia},\quad a=x+ih,\quad
 x\in P=[11/50,9/20],\quad -.108\le h\le.068.
 \tag{1}
\]
The output is the original \(y=x_0\), \(Y=e^{2\pi iy}\). The
[completed half-degree theorem](research_mixed_fourier_right_cap_wall_half_degree_completion.md)
proves, for every fixed \(\delta>0\), uniformly at physical indices
\(1/2\le s=j/N\le1-\delta\),
\[
 H_{j,N}(y)=N^{-1/2}\mathcal B(s,y)e^{N\Phi(s;y)}
                                      (1+O(N^{-1})),
 \qquad \mathcal B\ne0.
 \tag{2}
\]
Here \(H_{j,N}\) is the entire outgoing sum, with its original
cardinal scalar and degree \(N-j-1\). Its action is
\[
 \Phi(s;y)=g(s)-\pi iy+I_{\rm W}(1-s,Y),\qquad
 \partial_t I_{\rm W}(t,Y)=\log R(t,0,Y),
 \tag{3}
\]
with the original logarithmic lift and the exterior degree root
\(|R(t,0,Y)|>1\), \(0\le t\le1/2\).

Define the continuous real integral
\[
 I_a(s)=\int_0^s\log|1-Xe^{-2\pi iu}|\,du,\qquad J(s)=\Re g(s),
 \tag{4}
\]
and, for \(\eta\in\{0,1\}\), set
\[
 \mathcal E_\eta(s;a)
 =I_a(s)-3J(s)-2\pi hs+\Re\Phi(s;y)
                                      -\frac{\eta}{2}\Re g(a).
 \tag{5}
\]
The logarithmic zeros in (4) are integrable. In particular (4) is
not replaced by an unmarked difference of two dilogarithms across
the period seam.

The exact remaining source is
\[
 V_N^{\rm F}(y,X)=\sum_{j=0}^{N-1}
                  X^{-j}\frac{(rX;r)_j}{P_j^3}H_{j,N}(y).
 \tag{6}
\]
The uniform product theorem in
[the right-half source reduction, equations (6)--(7)](research_mixed_right_half_source_reduction.md)
gives
\[
 |(rX;r)_j|\le N^A e^{NI_a(j/N)},\qquad
 |P_j|=e^{NJ(j/N)+O(\log N)}.
 \tag{7}
\]
Its truncated-log proof works uniformly as \(|X|\) crosses one:
the truncation has variation \(O(\log N)\) and adds \(O(1/N)\)
to the integral. Thus (7) includes every incoming polynomial zero;
it asserts an upper bound, not relative asymptotic equality.

For the actual admissible incoming height \(h=\Im a_*\), allocate
the original factor \(|d_N(X)|^{\eta/2}\). Its established rate is
\(-\eta\Re g(a)/2\), with the prescribed arbitrarily small tolerance,
as in the
[endpoint-payment theorem](research_mixed_fourier_right_cap_endpoint_payment.md).
Equations (2), (6), (7) then imply, for any index set
\(\mathcal J_N\subset\{j:1/2\le j/N\le1-\delta\}\) and \(\tau>0\),
\[
 |d_N(X)|^{\eta/2}
 \left|\sum_{j\in\mathcal J_N}
            X^{-j}\frac{(rX;r)_j}{P_j^3}H_{j,N}(y)\right|
 \le C_{\delta,\tau}N^{A_{\delta,\tau}}
       \exp N\left\{
        \sup_{s\in\overline{\mathcal J_N/N}}\mathcal E_\eta(s;a)
                                                       +\tau\right\}.
 \tag{8}
\]
One may replace that finite supremum by any containing real interval.
The additional row count is polynomial. Both original parities,
the exact outgoing normalization, and zeros of the incoming
polynomial or Fourier factor remain included.

## 2. An exact derivative and a decreasing quarter-period

Put \(S=e^{-2\pi is}\), \(t=1-s\), and \(V=X^{-1}\). The calibrated
identity (3) gives
\[
 \Re\Phi_s(s;y)=\log|1-S|-\log|R(t,0,Y)|.
 \]
Since \(|X|=e^{2\pi h}\), differentiating (5) yields
\[
 \boxed{\quad
 \mathcal E'_\eta(s;a)=
       \log\frac{|V-S|}{|1-S|^2|R(1-s,0,Y)|}.
 \quad}
 \tag{9}
\]
This holds away from a numerator zero and almost everywhere on the
whole interval. It is independent of \(\eta\).

**Proposition 1.** For every parameter in (1),
\[
 \mathcal E_\eta(s;a)\le\mathcal E_\eta(1/2;a),
                      \qquad 1/2\le s\le3/4,
 \tag{10}
\]
with strict inequality when \(s>1/2\).

*Proof.* Write \(V=R_a e^{i\alpha}\), where
\(\alpha=2\pi x\in[.44\pi,.9\pi]\). The elementary logarithmic
series gives
\[
 \log2>2(1/3+1/81)=56/81>594/875=.216(22/7).
 \]
Consequently \(R_a=e^{-2\pi h}<2\) on (1).

For \(1/2\le s\le2/3\), or \(1/3\le t\le1/2\),
\[
 |V-S|<3,\qquad |1-S|^2=4\sin^2(\pi t)\ge3.
 \]
Together with \(|R|>1\), this makes (9) strictly negative.

For \(2/3\le s\le3/4\), put \(\theta=2\pi t\in[\pi/2,2\pi/3]\).
Then \(S=e^{i\theta}\) and \(|\alpha-\theta|\le2\pi/5\).
The squared distance is convex as a function of \(R_a\in[0,2]\).
Its maximum is therefore at a radial endpoint, giving
\[
 |V-S|^2
 \le\max\{1,5-4\cos(\alpha-\theta)\}
 \le6-\sqrt5<4,\qquad |1-S|^2\ge2.
 \tag{11}
\]
Equation (9) is again negative. If \(V=S\), necessarily \(h=0\);
the derivative instead has an integrable logarithmic divergence
to \(-\infty\). Formula (5) is absolutely continuous, so integrating
the almost-everywhere strict inequality proves (10), including
through that incoming zero. No convexity of the retained rate is
asserted. \(\square\)

All strict inequalities persist on a sufficiently small common
output-parameter neighborhood, by the uniform degree separation
and compactness. The real input-height interval in (1) is unchanged.

## 3. A finite algebraic list for the remaining middle interval

For a fixed \(0<\delta<1/4\), consider \(3/4\le s\le1-\delta\).
The limiting degree equation is
\[
 AR^2-DR+C=0,\qquad
 z=e^{-2\pi i(1-s)}=\overline S,\quad
 A=z(1-Yz),\quad C=Yz(1-z),\quad D=A+C-Y.
 \tag{12}
\]
At a smooth stationary point of (5), equation (9) implies
\[
 |R|^2=M,\qquad M=\frac{|V-S|^2}{|1-S|^4}>1.
 \tag{13}
\]
Conjugating (12) and using \(\overline R=M/R\) gives a second
quadratic,
\[
 \overline C R^2-\overline D M R+\overline A M^2=0.
 \]
Its resultant with (12) is
\[
 \boxed{\quad
 (|A|^2M^2-|C|^2)^2
       -M|A\overline D M-D\overline C|^2=0.
 \quad}
 \tag{14}
\]
For example, the quadratic resultant formula
\((af-cd)^2-(ae-bd)(bf-ce)\) gives (14) directly; the
last two factors are \(L\) and \(M\overline L\), with
\(L=-A\overline D M+D\overline C\).
Only necessity is used: extraneous resultant roots will not be
discarded.

Here is an explicit degree bound, without root evaluation. Put
\[
 u=\tan(\pi(1-s)),\quad d=1+u^2,\quad
 Z=1-u^2-2iu,\quad z=Z/d,\quad S=\overline Z/d.
 \]
If \(V=v_1+iv_2\), define the real polynomials
\[
 n=(|V|^2+1)d-2\{v_1(1-u^2)+2v_2u\},\qquad
 m=nd,\qquad v=16u^4.
 \tag{15}
\]
Then \(M=m/v\). Define degree-at-most-four complex polynomials
\[
 \widetilde A=Z(d-YZ),\quad
 \widetilde C=YZ(d-Z),\quad
 \widetilde D=\widetilde A+\widetilde C-Yd^2.
 \]
Clearing the positive denominator \(d^8v^4\) in (14) yields the
real polynomial
\[
 \begin{split}
 \mathscr P(u)={}&
 \big(|\widetilde A|^2m^2-|\widetilde C|^2v^2\big)^2\\
 &-mv\,
    |\widetilde A\overline{\widetilde D}\,m
                      -\widetilde D\overline{\widetilde C}\,v|^2,
 \qquad \deg\mathscr P\le32.
 \end{split}
 \tag{16}
\]
Conjugation in this formula conjugates coefficients and leaves the
real variable \(u\) unchanged. The polynomial is not identically
zero: at \(u=0\), \(m=|V-1|^2>0\),
\(\widetilde A=1-Y\ne0\), \(\widetilde C=v=0\), so its value is
\(|1-Y|^4|V-1|^8>0\).

Thus the maximum of (5) on \([3/4,1-\delta]\) is attained at an
endpoint or at one of at most 32 real roots of (16) in
\([\tan(\pi\delta),1]\), after conversion back to \(s\).
One may retain every such root. An incoming numerator-zero point
is not a missing local maximum: (9) tends to \(-\infty\) on both
sides and the rate decreases through it. Such a point may also
be added harmlessly to the list.

## 4. What remains to pay the high retained-index source

The [proved endpoint payment](research_mixed_fourier_right_cap_endpoint_payment.md)
already controls the complete source with
\(j\ge N-1-\lfloor\delta_0N\rfloor\), for some fixed
\(\delta_0>0\), with finite exponential gap \(1/200\).
Choose \(0<\delta<\min(\delta_0,1/4)\). For all sufficiently large
\(N\), this endpoint strip and the range \(j/N\le1-\delta\)
overlap. Equations (8), (10), (16) reduce all remaining indices
\(j/N\ge1/2\) to
\[
 \mathcal E_\eta(1/2;a),\qquad
 \mathcal E_\eta(1-\delta;a),\qquad
 \mathcal E_\eta(s;a)
 \ \text{at the retained real roots of (16)}.
 \tag{17}
\]
The \(3/4\) endpoint is already bounded by the first entry.

For an actual incoming reference, keep exactly the supporting plane
\(B_\eta(x)\) of the endpoint-payment theorem, including its original
linear marginal, quadratic cost and incoming allocation.
A uniform positive deficit of every value in (17) below that plane
would, by (8) and the paid endpoint strip, give a strict bound for
the entire high retained-index portion of (6). This last comparison
has not been proved or tested. In particular no rate equality is
inferred at an incoming polynomial zero, no sign is inferred from
the finite candidate reduction, and no omitted contour current is
declared paid.
