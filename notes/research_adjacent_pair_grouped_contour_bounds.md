# Bounds for the grouped contours of the adjacent pair

The full-period residue formula combines the two vertical \(x\)-sides before estimating them. With the exponent of that exact combined multiplier retained, every remaining nonprincipal contour has a strict loss below the selected stationary value. This note proves the required inequalities on their entire parameter domains.

The inputs from elsewhere are the [exact full-period identity](research_adjacent_pair_full_period_contour.md), its uniform midpoint factorial estimate, and the cancellation of all four complete lower circles. The present note supplies the phase bounds; it does not replace an endpoint of the original finite sum by a limiting endpoint.

## 1. The functions and the bounds

Use
\[
 W(x,y)=J(x+y)-3J(x)-6J(y)+J(2y)
       +i\pi(x^2-xy+y^2/2+x+y/2),                 \tag{1}
\]
where \(J'(z)=\Log(2\sin\pi z)\), real on \(0<z<1\), and \(J(0)=0\). Put
\[
 h_x=\frac{3\log2}{4\pi},\quad h_y=\frac{\log7}{4\pi},
 \quad h_a=\frac{\log2}{4\pi},\quad \delta=10^{-5}.
\]
The chosen upper \(y\)-height and the exponent of the combined side multiplier are
\[
 v(s)=
 \begin{cases}
 \delta+(h_a-\delta)(-s),&-1\le s\le0,\\
 \delta+(h_y-\delta)s/h_x,&0\le s\le h_x,
 \end{cases}
\qquad
 {\cal E}(s,t)=
 \begin{cases}
 4\pi s+2\pi\max(t,0),&s\le0,\\
 2\pi\max(t-2s,0),&s\ge0.
 \end{cases}                                                   \tag{2}
\]
The variable \(t\) is the imaginary part of \(y\). In particular \(v(-1)=h_a\), \(v(0)=\delta\), and \(v(h_x)=h_y\).

Let \(M=\Re W(x_*,y_*)\). The rational reference enclosure in [the horizontal proof](research_adjacent_two_crossing_horizontal_maximum.md) gives
\[
 M>0.84885122401210508399>8488/10000.              \tag{3}
\]
The terminating decimal is rounded down from that certified interval.

Define
\[
\begin{aligned}
 F_U(b,s)&=\Re W(is,b+i v(s))+{\cal E}(s,v(s)),\\
 F_L(b,s)&=\Re W(is,b-ih_y)+{\cal E}(s,-h_y)-2\pi h_y,\\
 F_E(b,s,t)&=\Re W(is,b+it)+{\cal E}(s,t)-2\pi(-t)_+.
\end{aligned}                                                   \tag{4}
\]
The bounds proved below are:

* \(F_U,F_L<169/200\) on \(0\le b\le1/2\), \(-1\le s\le h_x\).
* On \(-1\le s\le h_x\), \(-h_y\le t\le v(s)\),
  \[
  F_E(0,s,t)\le\pi h_y,\qquad F_E(1/2,s,t)\le\pi h_x.             \tag{5}
  \]
* For \(0\le a\le1\), \(-h_y\le t\le h_y\), and \(b=0,1/2\),
  \[
    \Re W(a+ih_x,b+it)-2\pi(-t)_+<3/4.             \tag{6}
  \]
* For \(0\le a\le1\), \(0\le b\le1/2\),
  \[
    \Re W(a+ih_x,b-ih_y)-2\pi h_y<3/4.             \tag{7}
  \]

The corner bounds (5) are piecewise linear. The other bounds use certified complex-ball arithmetic on compact rectangles. All omitted endpoint strips are handled analytically. Section 5 gives quantitative allowances for the actual cutoff \(\epsilon=10^{-6}\) and half-grid endpoints. After those allowances the common bound \(847/1000<M\) still holds.

## 2. Formulas evaluated on the boxes

For \(0\le a\le1\), write \(j(a,q)=\Re J(a+iq)\). The canonical upper branch and Schwarz reflection give
\[
 j(a,q)=
 -\frac{\Im\operatorname{Li}_2(e^{-2\pi|q|+2\pi ia})}{2\pi}
 -\frac{\pi|q|(1-2a)}2.                            \tag{8}
\]
This is continuous at \(q=0\), including both endpoints. For positive height the same upper-branch formula continues to arbitrary real \(a\). That continuation is used when \(a+b>1\).

In particular,
\[
 j(0,q)=-\pi|q|/2,\quad j(1/2,q)=0,\quad j(1,q)=\pi|q|/2.
\]
Hence
\[
\begin{split}
 \Re W(is,b+it)={}&j(b,s+t)+3\pi|s|/2-6j(b,t)+j(2b,2t)\\
 &-\pi\{s(1-b)+t(b+1/2)\}.                        \tag{9}
\end{split}
\]
For (6) the corresponding formula is
\[
\begin{split}
 \Re W(a+ih_x,b+it)={}&j(a+b,h_x+t)-3j(a,h_x)+c_b\pi|t|\\
 &-\pi\{(2a-b+1)h_x+(-a+b+1/2)t\},                \tag{10}
\end{split}
\]
where \(c_0=2\), \(c_{1/2}=1\). The first height is at least \(h_x-h_y>0\). Formula (7) is evaluated before specializing the three terms involving \(b\). These are the exact formulas in the verifier.

## 3. The grouped corners

At \(b=0\), (9) divided by \(\pi\) equals
\[
 -|s+t|/2+3|s|/2+2|t|-s-t/2.                     \tag{11}
\]
After adding \({\cal E}/\pi\) and subtracting \(2(-t)_+\), the result for \(t<0\) is \(2s\le0\) when \(s\le0\), and \(\min(s,-t)\le h_y\) when \(s\ge0\).

For \(t\ge0,s\le0\), the result is
\[
 -|s+t|/2+3s/2+7t/2.
\]
It increases with \(t\). Put \(k=h_a-\delta\). After substituting \(t=v(s)=\delta-ks\), the two linear pieces have slopes \(1-3k\) and \(2-4k\), both positive since \(h_a<1/6\). The maximum is \(3\delta<h_y\) at zero. For \(s\ge0,t\ge0\), the result is \(t+\max(2t-4s,0)\). It increases with \(t\); after substituting \(v(s)\), it is convex and piecewise linear in \(s\), with endpoint values \(3\delta\) and \(h_y\). This proves the first inequality in (5).

At \(b=1/2\), the phase divided by \(\pi\) is
\[
 3|s|/2+|t|-s/2-t.
\]
Subtracting \(2(-t)_+\) removes its \(t\)-dependent part. Adding \({\cal E}/\pi\), for \(s\le0\) the result is \(2s+2\max(t,0)\le2\delta\). For \(s\ge0\) it is \(s+\max(2t-4s,0)\). Substitution of \(t=v(s)\) gives a convex piecewise-linear function with endpoint values \(2\delta\) and \(h_x\). This proves the second inequality in (5).

## 4. Compact certificates and endpoint strips

The standalone [verifier](../experiments/verify_adjacent_pair_grouped_contour_bounds.py) uses Arb/Acb through python-flint 0.9.0. The saved run uses 100-bit midpoints with outward ball radii. Every domain endpoint and every subdivision endpoint is an exact rational number.

Ball arithmetic and subdivision are established numerical methods, used here to verify the specific contour inequalities. The arithmetic is described in F. Johansson, [“Arb: efficient arbitrary-precision midpoint-radius interval arithmetic”](https://doi.org/10.1109/TC.2017.2690633), *IEEE Transactions on Computers* **66** (2017), 1281–1292; the implementations used here are documented in the official [Arb](https://flintlib.org/doc/arb.html) and [Acb](https://flintlib.org/doc/acb.html) references.

For \(F_U,F_L\), first restrict \(b\) to
\[
 [\eta,1/2-\eta],\qquad \eta=10^{-5}.               \tag{12}
\]
The two \(s\)-intervals are parametrized separately by \(u\in[0,1]\):
\(s=-u\) and \(s=h_xu\), with the corresponding affine heights from (2). The sign in (2) is selected from this exact parametrization; it is never inferred from an outward ball straddling zero.

A box is accepted only when its full ball enclosure is below the required rational threshold. Otherwise it is bisected at a rational midpoint. A nonfinite enclosure is never accepted. Reaching the maximum allowed depth or count causes failure. The completed partitions are:

| Function | Accepted boxes | Strict upper bound |
| --- | ---: | ---: |
| \(F_U\), negative \(s\) | 676 | \(169/200\) |
| \(F_U\), positive \(s\) | 20073 | \(169/200\) |
| \(F_L\), negative \(s\) | 73 | \(169/200\) |
| \(F_L\), positive \(s\) | 918 | \(169/200\) |
| Upper-\(x\), bottom endpoint | 77 | \(3/4\) |
| Upper-\(x\), top endpoint | 184 | \(3/4\) |
| Upper-\(x\), lower-\(y\) horizontal term | 1733 | \(3/4\) |

Binary subdivision preserves coverage. The verifier also sums the accepted areas as exact fractions and checks equality with each original rectangle's area. Its output records those areas, counts, depths, and hashes of all accepted partitions. Rerunning it rechecks every box. No optimization or sampled maximum enters a decision.

For the two missing strips in (12), use the uniform horizontal modulus
\[
 |j(a+\alpha,q)-j(a,q)|
 \le m(\alpha):=\alpha(9-\log\alpha),
 \quad |q|\le7/6,\quad 0<\alpha\le1/4,              \tag{13}
\]
provided the intervening real segment lies in \([0,1]\). The same estimate holds in the opposite direction. To prove it, note that
\[
 \partial_a j(a,q)=\log|2\sin\pi(a+iq)|.
\]
Its positive part is less than \(8\), using \(2\cosh(7\pi/6)<e^8\). Its negative part is bounded by
\((-\log(4\min(a,1-a)))_+\), because \(\sin\pi a\ge2\min(a,1-a)\).
The integral of the latter over a segment of length \(\alpha\le1/4\) is at most \(\alpha(1-\log\alpha)\). This proves (13), including the endpoint limits.

Changing \(b\) by \(\alpha\) in (9) costs at most
\[
 7m(\alpha)+m(2\alpha)+4\alpha
 \le\alpha(85-9\log\alpha).                        \tag{14}
\]
Here \(\pi|s-t|<4\), and \(m(2\alpha)\le2m(\alpha)\). Neither \({\cal E}\) nor the lattice penalty depends on \(b\). For \(\alpha\le\eta\), \(\log\eta>-12\); (14) is less than \(193/100000\). Applying the endpoint bounds (5) therefore controls both missing strips for both \(F_U,F_L\) by
\[
 \pi h_x+193/100000<21/40+193/100000<169/200.        \tag{15}
\]
This proves their inequalities on the full closed \(b\)-interval.

## 5. The actual cutoff and half-grid endpoints

The exact formula has \(a_N=-1/(2N)\), \(a_N+1\), and
\[
 |c_N-\epsilon|,\ |d_N-(1/2-\epsilon)|\le1/N,
 \qquad \epsilon=10^{-6}.                         \tag{16}
\]
For \(N\ge2\cdot10^6\), these \(y\)-endpoints lie in \([\epsilon/2,1/2-\epsilon/2]\) and within \(2\epsilon\) of the corresponding limiting endpoint. Thus the whole-interval estimates for \(F_U,F_L\) already cover their actual domains.

For the grouped corners, put \(\alpha=2\epsilon\) in (14). Since \(\log(2\epsilon)>-14\), the cost is less than \(422\cdot10^{-6}\). Their actual rates are below
\[
 21/40+422\cdot10^{-6}<0.526.                       \tag{17}
\]
This is an explicit allowance for the chosen cutoff.

For (6)--(7), moving the small negative part of the real \(x\)-interval to zero costs less than \(14/(2N)\). Indeed \(x\) and \(x+y\) have positive height at least \(h_x-h_y\), and
\[
 \pi(h_x-h_y)=\tfrac14\log(8/7)>1/32.
\]
Their sine moduli lie between \(1/16\) and \(8\), so the real logarithmic derivatives have absolute value less than \(3\). The two corresponding factorial terms and the quadratic phase give \(|\partial_a\Re W|<14\).

At an upper-\(x\) \(y\)-endpoint, moving \(b=0\) or \(1/2\) by \(\alpha\le2\epsilon\) costs at most
\[
 8m(\alpha)+5\alpha=\alpha(77-8\log\alpha).          \tag{18}
\]
The \(x+y\) term has real logarithmic derivative less than \(3\); the \(y,2y\) terms use (13), and the quadratic phase costs less than \(2\alpha\). Formula (18) is below \(378\cdot10^{-6}\). Including the \(x\)-shift adds at most \(7\cdot10^{-6}\) for \(N\ge10^6\). All the actual rates in (6)--(7) are consequently below \(0.751\).

The combined side has \(Nx=-1/2+iNs\). Its uniform polynomial prefactor through \(s=0\) is supplied by the midpoint factorial estimate used in the [exact assembly](research_adjacent_pair_full_period_contour.md), applied also to \(N(x+y)\). Its exponent is precisely (4). No interior Stirling expansion at \(x=0\) is assumed here.

All these bounds leave a fixed margin below \(847/1000\). On the actual \(y\)-contours, the real parts are separated from zero and one half by a fixed positive multiple of \(\epsilon\) for all sufficiently large \(N\). The boundary-dependent factorial arguments remain regular for all sufficiently small complex boundary angles \(u\). Their leading phases vary uniformly continuously on these compact contours. Shrinking that fixed disk in \(u\) retains the common bound \(847/1000\). The midpoint \(x\)-factors are independent of \(u\). Thus the same strict loss holds with the uniform polynomial prefactors of the exact assembly.

## 6. The full upper rectangle

The horizontal proof was stated for \(a+b\le1\), but proves the same result on the full rectangle \([0,1]\times[0,1/2]\). Its rational certificate covers \([0,1/2]^2\). Its separate elementary estimate for \(a\ge1/2\) assumes only \(a\le1\), \(0\le b\le1/2\), and gives
\[
 \Re W(a+ih_x,b+ih_y)<32525/65940<1/2.
\]
It never uses \(a+b\le1\). The upper-half-plane formula for \(J(x+y)\) continues across \(\Re(x+y)=1\), because its imaginary part is \(h_x+h_y>0\).

The full rectangle therefore has the same unique stationary maximum, local Hessian bound, and exterior gap \(1/10000\). Its \(O(1/N)\) real \(x\)-displacement changes exterior values by \(O(1/N)\), since these fixed-height phases have bounded derivatives. It preserves a smaller exterior gap for sufficiently large \(N\); the stationary point stays in the interior.

Upper corrections to either lattice kernel have an additional positive exponential penalty. Bounds (4), (6), and (7) consequently control the associated upper-correction terms as well. The four lower-\(x\) terms are removed by the separate full-circle theorem. These are exactly the remaining classes in the sixteen-term identity; no diagonal corner current is discarded separately.

## 7. Reproduction

Run

~~~sh
python3 experiments/verify_adjacent_pair_grouped_contour_bounds.py --output repro/results/research-adjacent-pair-grouped-contour-bounds.json
~~~

The [saved record](../repro/results/research-adjacent-pair-grouped-contour-bounds.json) contains all seven successful compact-domain checks. The analytic strips and piecewise-linear corner bounds are proved above, not inferred from those computations. A separate 128-bit replay is saved in [the root replay record](../repro/results/research-adjacent-pair-grouped-contour-bounds-root.json).
