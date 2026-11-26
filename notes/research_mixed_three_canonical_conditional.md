# One canonical complex-neighbor source for the three-vertex conditional

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The [fixed-circle continuation](research_mixed_three_conditional_complex_neighbors.md)
retains a specified contour on each complex parameter patch. Here a
single fixed finite sum replaces those patchwise definitions. We prove
its asymptotic from its original index contour, including the rows
that vanish on the physical grid and revive off it. Agreement of
interpolants on the grid is not used to transfer a complex asymptotic.

## 1. The fixed source and the theorem

Put \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\), and use the original
marked sine factorial
\[
 \widehat P_N(v)=
 e^{\pi iv/2-\pi iv(v+1)/(2N)}G_N(v).
 \tag{1}
\]
It satisfies
\(\widehat P_N(v+j)=\widehat P_N(v)(r^{v+1};r)_j\)
for every nonnegative integer \(j\), and
\(\widehat P_N(j)=P_j\) for \(0\le j<N\). Define
\[
 \mathcal L_{0,N}(\alpha,\beta)=
 \widehat P_N(N\alpha)\widehat P_N(N\beta)
 \sum_{j=0}^{N-1}
 \frac{e^{2\pi i\alpha j}
       (r^{N\alpha+1};r)_j(r^{N\beta+1};r)_j}{P_j^2}.
 \tag{2}
\]
This is one holomorphic function on a fixed neighborhood of
\(K=[1/5,9/20]^2\). All prefactors are nonzero there. At physical
neighbors \(\alpha=a/N,\beta=b/N\), its terms with
\(j+\max(a,b)\ge N\) vanish exactly. The other terms give
\[
 \mathcal L_{0,N}(a/N,b/N)=
 \sum_{j=0}^{N-1-\max(a,b)}
       \frac{r^{-aj}P_{j+a}P_{j+b}}{P_j^2}=L_0(a,b).
 \tag{3}
\]
Thus the full original support and both level parities are retained.

Let \(J'(z)=\Log(2\sin\pi z)\) on \(0<\Re z<1\), with
\(J\) real on the real interval, and write
\[
 \begin{split}
 \varphi(z)&=\pi(z-z^2)/2,\\
 F_0(s;\alpha,\beta)&=J(s+\alpha)+J(s+\beta)-2J(s)
                              +i\pi s(\alpha-\beta),\\
 Q_0(s;\alpha,\beta)&=F_0(s;\alpha,\beta)
                              +i\varphi(\alpha)+i\varphi(\beta),\\
 A_0(s;\alpha,\beta)&=e^{-\pi i(\alpha+\beta)/2}
   \frac{\sqrt{2\sin\pi(s+\alpha)}\sqrt{2\sin\pi(s+\beta)}}
        {2\sin\pi s}.
 \end{split}
 \tag{4}
\]
The roots continue from the positive sine roots on the real strip.

**Theorem 1.** There is a fixed complex neighborhood of \(K\) on
which the selected root \(s_*\) of \(F_{0,s}=0\), the action and
the coefficient below are holomorphic, and
\[
 \mathcal L_{0,N}(\alpha,\beta)=
 \sqrt N\,
 \frac{\sqrt{2\pi}\,A_0(s_*;\alpha,\beta)}
      {\sqrt{-F_{0,ss}(s_*;\alpha,\beta)}}
 e^{NQ_0(s_*;\alpha,\beta)}\{1+O(N^{-1})\}.
 \tag{5}
\]
The coefficient is nonzero. The normalized error is holomorphic
and uniform, with every fixed parameter derivative on smaller
neighborhoods. The square root is the continued accretive Gaussian
root. This theorem concerns the single finite function (2); it does
not identify arbitrary off-grid continuations or estimate the
remaining coherent neighbor sum.

## 2. The common critical point and a whole middle rectangle

For real parameters in \(K\), the
[full-circle theorem](research_mixed_three_conditional_circle.md)
gives a unique critical point \(w_*\), with
\(|\Re w_*|<\log3\), imaginary part between \(\pi\alpha\)
and \(\pi\beta\), and \(\Re h_{ww}>1/10800\). Its exact
phase identity gives
\[
 s_* =\frac12+\frac{iw_*}{2\pi},\qquad
 F_{0,s}(s_*)=0,\qquad
 \frac{11}{40}\le\Re s_*\le\frac25,
 \quad |\Im s_*|<\frac{\log3}{2\pi}<\frac7{40}.
 \tag{6}
\]
This is equality of the actual logarithmic derivatives and their
lifts. In exponential variables it reads
\[
 (1-AU)(1-BU)=A(1-U)^2,\qquad
 A=e^{-2\pi i\alpha},\ B=e^{-2\pi i\beta},\ U=e^{-2\pi is_*}.
 \tag{7}
\]
No new algebraic root is selected independently of the circle source.

Set \(l=3/20\), \(u=49/100\), and
\(\mathcal R=[l,u]+i[-1/5,1/5]\). On this entire rectangle,
uniformly in the real neighbor square,
\[
                  -\Re F_{0,ss}>\frac15,
                       \qquad |F_{0,ss}|<46.
 \tag{8}
\]
To prove it, put
\(C=\cosh(2\pi h)\) and
\(R(x,h)=\Re\cot\pi(x+ih)
=\sin(2\pi x)/(C-\cos(2\pi x))\). The exact difference is
\[
 R(x,h)-R(x+\alpha,h)=
 \frac{2\sin\pi\alpha\,[\cos\pi\alpha-C\cos\pi(2x+\alpha)]}
 {(C-\cos2\pi x)(C-\cos2\pi(x+\alpha))}.
 \tag{9}
\]
Here \(1/2\le2x+\alpha\le143/100<3/2\), so the second
cosine is nonpositive. Thus (9) is at least
\(\sin(2\pi\alpha)/(1+C)^2\), and
\(\sin(2\pi\alpha)\ge\sin(\pi/10)\). The same applies to
\(\beta\), proving
\[
 -\Re F_{0,ss}\ge
 \frac{2\pi\sin(\pi/10)}{(1+\cosh(2\pi/5))^2}>\frac15.
 \tag{10}
\]
The shifted sine arguments have real parts in \([7/20,47/50]\),
and \(s\) has real part in \([3/20,49/100]\). Therefore
\[
 |F_{0,ss}|\le
 2\pi\{\cot(3\pi/50)+\cot(3\pi/20)\}<46.
 \tag{11}
\]
These inequalities also show strict complex-gradient injectivity
on the convex rectangle: integrate \(F_{0,ss}\) along a segment
and pair with the conjugate displacement. Hence (6) is its only
critical point. At its height,
\[
 \Re F_0(x+i\Im s_*)\le M-\frac1{10}(x-\Re s_*)^2,
                      \qquad M=\Re F_0(s_*).
 \tag{12}
\]
At fixed real part the real phase is strictly convex in height.

## 3. A full-parameter endpoint certificate

The focused outward certificate proves, on the entire real square,
\[
 M>\frac14,\qquad
 M-\Re F_0(l)>\frac1{100},\qquad
 M-\Re F_0(u)>\frac1{100}.
 \tag{13}
\]
Each exact rational parameter rectangle has a point root and a
uniform complex Newton square for the actual logarithmic derivative.
The inverse derivative is fixed at its rational proposal center.
The two-dimensional real row-norm contraction is less than \(1/2\),
and the residual plus radius times that contraction is less than
the radius. The square lies in \(\mathcal R\); uniqueness from
(8) identifies this root with (6). Numerical proposals are not
acceptance tests.

For \(M\), the parameter derivatives are
\[
 \partial_\alpha M=\Re\{J'(s_*+\alpha)+i\pi s_*\},\qquad
 \partial_\beta M=\Re\{J'(s_*+\beta)-i\pi s_*\}.
 \tag{14}
\]
For an endpoint difference, subtract the corresponding expression
at \(c=l,u\). Interval enclosures of these derivatives times the
parameter half-widths bound the change from the certified center
value. The stationary equation eliminates all root derivatives.
The recorded binary partition covers the entire parameter square
exactly. This certifies (13), not just sampled saddle values.

## 4. The original real tails and every middle contour current

On the original real support,
\[
 \partial_s\Re F_0=
 \log\frac{\sin\pi(s+\alpha)\sin\pi(s+\beta)}{\sin^2\pi s}.
 \tag{15}
\]
For \(0<s\le l\), the numerator sines are at least
\(\sin(\pi/5)\), whereas \(\sin\pi s\le\sin(3\pi/20)\),
so the entropy increases. For \(s\ge u\) in its physical support,
each numerator sine is strictly less than \(\sin\pi s\): below
\(1/2\), use \(s+\alpha>1-s\), and above \(1/2\) use monotonicity
of sine on that half interval. Thus the entropy decreases.
Uniform endpoint factorial bounds and (13) control both full real
tails, including their first and last rows, by
\(\operatorname{poly}(N)e^{N(M-1/100)}\).

At central physical rows the exact summand is
\(e^{2\pi iN\alpha s}\widehat P_N(N(s+\alpha))
\widehat P_N(N(s+\beta))/\widehat P_N(Ns)^2\).
The original regular-strip expansion gives
\[
                \mathcal T_N(s)=A_0(s)e^{NQ_0(s)}(1+O(N^{-1})),
 \tag{16}
\]
holomorphically with fixed derivatives on the whole middle contour.
There is no power of \(N\) in this symbol.

Choose half-grid cuts tending to \(l,u\), put
\(\varepsilon=10^{-5}\), \(Y=|\Im s_*|+\varepsilon<1/5\),
and \(\sigma=\operatorname{sign}\Im s_*\), taking \(\sigma=1\)
at zero. The exact counterclockwise cotangent formula is
\[
 \sum_{l_N<j/N<u_N}\mathcal T_N(j/N)
       =\frac{N}{2i}\oint\mathcal T_N(s)\cot(\pi Ns)\,ds.
 \tag{17}
\]
Its upper and lower constant modes combine to
\(+N\int_{l_N}^{u_N}\mathcal T_N(x)\,dx\). Deforming this
zero mode to the critical height keeps both endpoint integrals.
The remainders have weights \(Ce^{-2\pi NY}\) horizontally and
\(2e^{-2\pi N|h|}\) on the half-grid vertical sides.

The selected horizontal side at height \(\sigma Y\) obeys, by
(8) and (12),
\[
 \Re F_0(x+i\sigma Y)
 \le M-d^2/10+46\varepsilon|d|+23\varepsilon^2
 \le M+5313\varepsilon^2,
 \qquad d=x-\Re s_*.
 \tag{18}
\]
Reflection has the exact form
\[
 \Re F_0(x-ih)-\Re F_0(x+ih)=2\pi h(\alpha-\beta).
 \tag{19}
\]
Since \(|\alpha-\beta|\le1/4\), both horizontal aliases have
rate at most
\(M+5313\varepsilon^2-3\pi Y/2<M-1/25000\).
At either unrounded cut, (6) gives \(|d|\ge9/100\). The
right side of (18) is decreasing as a function of \(|d|\) there,
and is less than \(M-1/1500\). Height convexity and (13)
therefore control the whole same-side vertical segment. Reflection
(19) with the alias weight controls the opposite segment. Both
unweighted zero-mode endpoint currents are on the selected side
and have that gap directly. These bounds include \(\Im s_*=0\),
all corners and all endpoint currents. Half-grid rounding preserves
strict gaps; the final contour gap may be weakened to \(1/50000\).

Gaussian evaluation of the zero mode now gives (5) at physical
neighbors, since its exact power is \(N\cdot N^{-1/2}=\sqrt N\).
The first cubic correction is odd. The normalization agrees exactly
with the full-circle source: the actual zero lift implies
\[
 A_0(s_*)=e^{-\pi i\alpha},\qquad
 -F_{0,ss}(s_*)=4\pi^2h_{ww}(w_*),\qquad
 Q_0(s_*)=h(w_*)+\pi i\alpha.
 \tag{20}
\]
The first identity follows by exponentiating half of \(F_{0,s}=0\)
with its continued sine roots. The last is the exact primitive
identity, so no undetermined action constant is introduced.

## 5. Revived rows and the canonical complex neighborhood

Let \(J_{\rm per}(t)=J(t-\lfloor t\rfloor)\) for real \(t\),
with \(J(0)=J(1)=0\). The finite-product regularization proved
in Lemma 2 of the
[type-four continuation](research_mixed_four_conditional_complex_neighbors.md)
applies verbatim to (2), with two denominator factorials. For real
\((\alpha_0,\beta_0)\in K\), \(s=j/N\), and complex displacement
at most \(\delta\), each full summand is bounded by
\[
 C_\delta N^C\exp N\{H_{\rm per,0}(s;\alpha_0,\beta_0)
                        +C_0\delta(1+|\log\delta|)\},
 \quad
 H_{\rm per,0}=J_{\rm per}(s+\alpha_0)+J_{\rm per}(s+\beta_0)-2J(s).
 \tag{21}
\]
For clarity, the input is the literal inequality
\(|1-e^{-2\pi i(\alpha+h/N)}|
\le |1-e^{-2\pi i(\alpha_0+h/N)}|+C\delta\).
The regularized logarithm has a uniform Riemann-sum error
\(O_\delta(1)\), and its integral exceeds the unregularized one
by \(O(\delta|\log\delta|)\). Thus (21) does not differentiate
through any physical zero.

For \(s\ge1-\max(\alpha_0,\beta_0)\ge11/20\), one numerator
has crossed an integer and has fractional part in \([0,9/20]\),
where \(J\le0\). The other contributes at most
\(\max J<1/6\), while \(J(s)\ge0\). Consequently
\[
             H_{\rm per,0}<1/6<M-1/12
 \tag{22}
\]
by (13). Below this cutoff, the original tails have the gap already
proved in Section 4. Choose a fixed small complex neighborhood so
that the continuity of the critical action and the regularization
cost preserve positive parts of these gaps. Summing the at most
\(N\) rows costs only a polynomial.

On the retained fixed interval, the factorial recurrence identifies
(2) with exactly the central interpolant (16), also for complex
neighbors. Keep the real-reference cotangent rectangle fixed.
All its endpoint and alias gaps are strict on a compact regular
set, so they persist under small complex parameter changes. Move
the zero-mode segment to the continued critical point, retaining
its two short joins. The same Gaussian proves (5) there. No
complex-parameter reflection identity is assumed; reflection was
used only to establish the real-reference gap.

Strict complex-gradient injectivity on the common middle rectangle
persists on a small neighborhood, so the critical branches agree
on overlapping patches. The finite source (2) is already the same
function on all of them. Compactness gives a fixed neighborhood of
the whole real square. Cauchy's formula proves the normalized
derivative bounds on smaller neighborhoods. This proves Theorem 1.

The exact transfer \(T_0\) is obtained by division by
\(\widehat P_N(N\alpha)^2\), which is nonzero on this neighborhood.
Its power is \(N^{-1/2}\), with the original crossing scalar
\(\kappa\) still external. No remaining outer-index cycle, its
aliases, or a mixed-word volume limit is asserted.

## 6. Reproduction

Run `python3 experiments/certify_mixed_three_canonical_conditional.py --precision 256`.
The record checks exact finite support and normalization, the global
middle-rectangle constants, and an exact-cover interval certificate
of the selected action and endpoint gaps. The original-source and
complex-tail conclusions use the written contour and regularization
arguments; they are not inferred from numerical saddle samples.

An independent replay uses the opposite-frequency dilogarithm primitive,
a rational-exponential Hessian and an exact horizontal sweep of the
parameter cover:

    python3 experiments/replay_mixed_three_canonical_conditional.py --precision 320

The [author record](../repro/results/research-mixed-three-canonical-conditional.json)
contains 1,580 parameter cells. The
[independent record](../repro/results/research-mixed-three-canonical-conditional-replay.json)
checks all of them, including the absolute action floor and both endpoint
gaps; its 97-slab sweep verifies the full parameter square exactly.
