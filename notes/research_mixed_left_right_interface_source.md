# Complete conditional sources across a left/right interface

Research proof, 4 November 2026. This supplies the original conditional
packet when an early left parameter meets a right taper parameter. It
keeps every finite row, both midpoint currents and both cotangent
remainders. It does not compare the resulting action with a geometric
supporting plane or supply a packet on a prescribed right-half region.

## 1. Independent compact domains and the literal source

Put \(H=7/500\) and
\[
\begin{split}
T_3&=\operatorname{conv}\{.1,.22-.03i,.22+.02i\},\\
T_4^+&=\operatorname{conv}\{.1,.22-.057i,.22+Hi,.12+Hi\},\\
W_3&=\operatorname{conv}\{.45-.03i,.5,.45+.02i\},\\
W_4&=\operatorname{conv}\{.45-.057i,.5,.45+Hi\}.
\end{split}                                                    \tag{1}
\]
Write \(T_4=T_4^+\). For each ordered pair of types, allow
\(T_{3+\eta}\times W_{3+\epsilon}\) and
\(W_{3+\eta}\times T_{3+\epsilon}\), independently.
These domains contain the mixed taper targets of the
[split-cutoff hybrid](research_mixed_split_cutoff_hybrid_contour.md).
Indeed, for \(.45\le x\le.5\),
\[
0\le400(.5-x)^2\le20(.5-x)\le1.                              \tag{2}
\]
Every further neighboring suppression moves a height toward zero and
stays inside the indicated triangle. The early selected rise is already
contained in \(T_4^+\).

Retain the marked factorial and the literal canonical sum from the
[whole-period transition source](research_mixed_transition_whole_period_source.md):
\[
L_{\epsilon,N}(a,b)=\sum_{j=0}^{N-1}e^{2\pi iaj}
 \frac{P_N(Na+j)P_N(Nb+j)}{P_N(j)^{2+\epsilon}}.               \tag{3}
\]
Its phase is the original regular-strip function
\[
Q(s;a,b)=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias,
\qquad g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i}.
                                                                    \tag{4}
\]

**Theorem 1.** Uniformly on a fixed open neighborhood of every closed
product in (1), at every sufficiently large integer level,
\[
L_{\epsilon,N}(a,b)=N^{(1-\epsilon)/2}
 \frac{\sqrt{2\pi}\,a_0(s_*+a)a_0(s_*+b)}
 {a_0(s_*)^{2+\epsilon}\sqrt{-Q_{ss}(s_*;a,b)}}
 e^{NQ(s_*;a,b)}(1+O(N^{-1})),                               \tag{5}
\]
where \(a_0(z)=\sqrt{2\sin\pi z}\,e^{-\pi iz/2}\), with the
original branches. The selected root \(s_*\) and the symbol are
holomorphic and the symbol is nowhere zero. All fixed derivatives have
the corresponding expansion on smaller neighborhoods. Division by
\(P_N(Na)P_N(Nb)\) gives the original Laurent kernel
\(C_{\epsilon,N}\), with power \(N^{-(1+\epsilon)/2}\), action
\(Q(s_*)-g(a)-g(b)\), and the divided original symbol.

## 2. Root geometry and the half-period endpoint

The early-cap cotangent estimate has already been proved in
[the enlarged-cap theorem](research_mixed_early_selected_source_cap.md).
On the right triangles, \(\Re\cot\pi z\ge0\), and
\[
 |\Im\cot\pi z|\le
 \frac{\sinh(2\pi\cdot.057)}{2\sin^2(.45\pi)}<\frac12.
                                                                    \tag{6}
\]
The [closed-cotangent root theorem](research_mixed_closed_cotangent_roots.md)
therefore supplies the unique simple original zero-lift root on a
neighborhood of each product before a boundary maximum principle is
used. All critical factorial arguments lie in their original regular
strips, and the positive triangle forms give \(-\Re Q_{ss}>0\).
At the vertex \(.5\), its outer cotangent is exactly zero; the other
outer real coordinate remains in \([.1,.22]\), with positive real
cotangent. Thus no root count is inferred merely by taking a limit.

The left-half circle proof in the whole-period source theorem remains
valid here. An original factor with zero real cotangent has the same
form \(p^2+B^2+r^2+2r(p\sin\theta+B\cos\theta)\), now with
\(p=0\) and \(B>0\). Its logarithm is concave on the first quarter
and strictly decreasing on the second; the other original factor keeps
the total strict. At height zero the factors increase with positive
real inner cotangent. Consequently the selected root is the unique
interior horizontal maximum of the left half, and its right endpoint
is strictly below it. The high-half polynomial criterion is unchanged.

The midpoint argument inequalities at an outer real coordinate \(.5\)
become non-strict for that factor alone: its argument is zero. The other
factor, whose real part is at most \(.22\), keeps every required
monotonicity strict. The exceptional positive profile
\[
V(y)=\Re\{g(a+iy)+g(b+iy)\}+\pi y-2\pi\Re(a)y,
\quad0\le y\le2,                                             \tag{7}
\]
remains strictly concave. Its maximum may occur at either endpoint.
The proposed tangent point is therefore zero if \(V'(0)\le0\), two
if \(V'(2)\ge0\), and an interior critical proposal otherwise.
Acceptance always uses the full concave tangent bound on \([0,2]\);
no numerical optimizer value is accepted as a bound.

## 3. Remote aliases on the enlarged domain

The old negative upper-alias rate is not imported unchanged. Let
\[
D=5\frac{e^{-2\pi(2-.057)}}{2\pi(1-e^{-2\pi(2-.057)})}.
\]
The disk parts of the calibrated factorial phases on the remote
horizontals are bounded by \(D\). After the exact upper cotangent
penalty \(4\pi\), its polynomial rate divided by \(\pi\) is
\[
2\{\epsilon(1-2x)+2b_r-2\}
 +h_a(2a_r-1)+h_b(2x+2b_r-1),\qquad0\le x\le1.             \tag{8}
\]
For \(\epsilon=0\) this is at most \(-2+.0912\).
For \(\epsilon=1\) and \(b\in T\), it is at most
\(-1.12+.0912\). In the remaining case \(b\in W\), write
\(q=.5-b_r\ge0\). Expression (8) is exactly
\[
h_a(2a_r-1)+x(2h_b-4)-q(4+2h_b)\le .0456.                 \tag{9}
\]
Both omitted terms are nonpositive for the full typed height range.
The complete upper-alias rate is thus at most \(D+.0456\pi\).
The lower-alias rate is at most \(D-1.886\pi\). The certificate
uses the strictly stronger action floor and scalar reserve
\[
M=\Re Q(s_*)>\frac15,\qquad
\frac15-D-.0456\pi>\frac1{20}.                              \tag{10}
\]
This retains a uniform remote gap in both orientations, including the
vertex \(.5\). The half-grid displacement changes these rates only
by a bounded factor.

## 4. Complete boundary currents and original normalization

There are 42 edge products in each orientation, hence 84 in total.
On every complete dyadic cover the checker verifies the original-log
root self-map, the selected cotangent strip, the action floor (10),
the strict Bernstein positivity of \(wF'(w)-2F(w)\), both full
horizontal endpoint gaps, all four revived right-midpoint branches,
and the full profile (7). Every endpoint or profile gap is greater
than \(10^{-4}\). The interval derivatives include the implicit
critical-height response. The exact cover and every rational affine
root witness are retained; a saved replay uses no new root or maximum
proposal. Complete acceptance of all 84 products is required.

The proof of (5) now follows the original whole-period current argument,
with precisely the two changes in Sections 2 and 3. The marked row is
holomorphic throughout the complete midpoint residue rectangle; outer
real part \(.5\) creates no pole. The exact cotangent decomposition
retains coefficient \(+N\) in its zero mode and both vertical joins.
Every shifted factorial uses its own calibrated upper or lower primitive,
so revived rows and real-index walls are retained. Far horizontal pieces
are displaced slightly from shifted real factorial axes, while only the
regular central segment passes through the saddle. The strict current
gaps persist on these connecting pieces. This also handles a zero
critical height and the vertex \(.5\).

The nondegenerate Gaussian supplies exactly the symbol and power in (5).
The normalized error is holomorphic near each complete convex parameter
product. Successive maximum principles extend its boundary estimate
through that product; compactness gives a fixed neighborhood, and Cauchy
estimates give the derivative statement. This extends the proved finite
error, not merely a root or a phase inequality.

The open neighborhood in (5) is not quantified as a packet on any
prescribed region of \((.5,1]\). The full finite-product upper envelope remains available there,
including when its left neighbor has nonzero height. Nor does (5) alone
prove a mixed-interface supporting-plane gap or a new cyclic contribution.

```sh
python3 experiments/certify_mixed_left_right_interface_source.py --precision 256
python3 experiments/certify_mixed_left_right_interface_source.py --precision 320 --input repro/results/research-mixed-left-right-interface-source.json --output /tmp/research-mixed-left-right-interface-source-review.json
```
