# Reoptimizing the inner saddles after an outer alias shift

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The conditional critical action remains below the original geometric
rate after any nonempty subset of four-type outer variables is moved
to height \(7/500\), including the true Fourier-weight correction.
This estimate allows every affected inner saddle to move. It does not
estimate the full conditional sum at the shifted parameters, its tails,
or the rest of an outer integration cycle.

## 1. Conditional roots on the required parameter rectangles

Use the original logarithmic primitive and conditional phase
\[
 g'(z)=\Log(1-e^{-2\pi iz}),\qquad
 Q_\epsilon(s;a,b)=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias,
 \quad \epsilon\in\{0,1\}.
 \tag{1}
\]
All arguments below have real part in \((0,1)\), so the logarithm
has its original lift. Define
\[
 \begin{split}
 R_3&=[.267,.433]+i[-.065,.068],\\
 R_4&=[.27,.33]+i[-.057,.0141],\\
 D&=[.15,.49]+i[-.12,.12].
 \end{split}
 \tag{2}
\]
The upper edge of \(R_4\) leaves room around the final height
\(.014\). The actual critical legs lie in the respective rectangles,
before any shift, by the
[universal height theorem](research_mixed_cyclic_critical_height_bounds.md).

**Lemma 1.** For each of
\[
 (\epsilon,a,b)\in
 (0,R_4,R_3),\quad (1,R_3,R_4),\quad (1,R_4,R_4),
 \tag{3}
\]
the original equation \(Q_{\epsilon,s}=0\) has a unique root in
the interior of \(D\). This root is holomorphic on a neighborhood of
the whole parameter rectangle and has its original logarithmic lift.

*Proof.* The analytic curvature lemma in
[the conditional contour reductions](research_mixed_conditional_image_contours.md)
gives \(-\Re Q_{\epsilon,ss}>1/8\) throughout \(D\), for every
parameter pair in (3). The outward checker verifies the following
strict pointing inequalities, uniformly in those parameters:
\[
 \begin{array}{ll}
 \Re Q_s(.15+iy)>1/50,&\Re Q_s(.49+iy)<-1/50,\\
 \Im Q_s(x-.12i)>1/50,&\Im Q_s(x+.12i)<-1/50.
 \end{array}
 \tag{4}
\]
Every side is divided into 128 exact equal slabs. For a fixed slab,
each parameter dependence in
\(Q_s=g'(s+a)+2\pi ia+g'(s+b)-(2+\epsilon)g'(s)\)
is separately harmonic. Its real or imaginary extrema on a parameter
rectangle lie on its four sides. The checker covers each of these
sides by 32 exact intervals, bounds the two parameter contributions
separately, and adds their rigorous bounds and the remaining term.
Thus (4) is a complete rectangle calculation, not a test of corners
or numerical roots.

The two-dimensional Poincaré--Miranda theorem gives a zero of the
original real and imaginary equations. The negative real derivative
of \(Q_s\) proves uniqueness on the convex rectangle: the averaged
derivative along a segment has strictly negative real part and cannot
vanish. The same curvature makes the zero simple. The implicit
function theorem, uniqueness, and the strict boundary margins give
the asserted holomorphic branch. At the original cyclic configuration
it is the original inner root. \(\square\)

## 2. Horizontal optimization with the original inner heights

**Lemma 2.** Fix an original inner height \(y_*\), so
\(|y_*|<.068\). For every pair of parameters in (3),
\[
 -\Re Q_{\epsilon,ss}(x+iy_*;a,b)>4
                         \qquad(.15\le x\le.49).
 \tag{5}
\]
If an incident outer variable of type four moves vertically from its
original height to \(.014\), while the inner variable remains at its
original critical value \(s_*\), then
\[
             |\Im\cot\pi(s_*+t)|<3/4
 \tag{6}
\]
throughout this height change.

*Proof.* The own-index cotangent in (5) has the lower bound
\[
 c(x)=\frac{\sin(2\pi x)}
             {\cosh(.136\pi)-\cos(2\pi x)}.
\]
Every pair argument has real part in
\([x+.267,x+.433]\) and imaginary part of magnitude at most
\(.136\). If \(x+.267<.5\), its real cotangent is at most
\(\cot\pi(x+.267)\). If \(x+.267\ge.5\), its real cotangent is
at most
\[
 p(x)=\frac{\sin(2\pi(x+.267))}
             {\cosh(.272\pi)-\cos(2\pi(x+.267))}.
\]
To justify the latter maximum over the whole pair interval, the
derivative of \(\sin\theta/(C-\cos\theta)\), with
\(C=\cosh(.272\pi)\), changes sign at most once on
\(\pi<\theta<2\pi\), from negative to positive. Only the two
endpoints can maximize it. The upper endpoint is smaller because
\(C\cos(.32\pi)<\cos(.166\pi)\); the sine subtraction formula
applies with the fixed interval width \(.166\).

The checker verifies
\(2\pi(c(x)-p(x))>4\), with the stated positive-cotangent
replacement below \(x=.233\), on 512 exact intervals in each of
\([.15,.233]\) and \([.233,.49]\). The own-index cotangent is
positive, so the additional type-four coefficient only strengthens
the bound. This proves (5).

For (6), the real pair argument belongs to \([.537,.763]\);
its imaginary part has magnitude at most \(.125\). In
\[
 |\Im\cot\pi(r+iy)|
   =\frac{|\sinh(2\pi y)|}{\cosh(2\pi y)-\cos(2\pi r)},
\]
the maximum on that rectangle is at \(|y|=.125,r=.763\).
The derivative signs and the strict bound \(3/4\) are checked
outward. \(\square\)

Let \(s_*\) be an original conditional critical point. Increase
the heights of its left and right parameters by
\(\delta_a,\delta_b\ge0\); each nonzero change belongs to a
type-four variable. Write \(s_+\) for the new root from Lemma 1.
Put
\[
 G=\partial_x\Re Q_\epsilon(s_*;a+i\delta_a,b+i\delta_b),
                         \qquad K=7\pi/4.
\]
Since \(g''=\pi\cot-\pi i\), integration of the mixed derivatives
gives
\[
 G=-A\delta_a+B\delta_b,\qquad
             0<A,B<K
 \quad\hbox{for each nonzero corresponding change}.
 \tag{7}
\]
In particular the cross term has a favorable sign:
\(G^2\le K^2(\delta_a^2+\delta_b^2)\).

Convexity in the imaginary inner direction and concavity in its real
direction now compare the two actions without estimating the inverse
complex Hessian in norm. At the new critical real coordinate,
the imaginary coordinate of \(s_+\) minimizes the real phase;
both that coordinate and \(y_*=\Im s_*\) lie in \(D\).
On the original-height line, (5) bounds its maximum by completing
the real quadratic. Therefore
\[
 \Re Q_\epsilon(s_+;a+i\delta_a,b+i\delta_b)
 \le \Re Q_\epsilon(s_*;a+i\delta_a,b+i\delta_b)
                         +\frac{K^2}{8}
                                  (\delta_a^2+\delta_b^2).
 \tag{8}
\]
Here imaginary convexity uses the already proved
\(-\Re Q_{ss}>1/8\) on the full vertical segment; the stronger
constant \(4\) is needed only on the original-height line.

## 3. Every alias subset has a strict optimized action reserve

Use the full contracted phase \(\mathcal F\) of the
[local reflection budget](research_mixed_alias_reflection_budget.md).
Let \((\mathbf s^*,\mathbf t^*)\) be an actual cyclic mixed
critical configuration and put
\(M=\Re\mathcal F(\mathbf s^*,\mathbf t^*)\).
For a nonempty subset \(S\) of its four-type outer variables, write
\(t_v^*=x_v-iH_v\), with \(.001<H_v<.057\), and put
\[
 h=7/500,\qquad t_v^+=x_v+ih,\qquad
 \delta_v=H_v+h<.071\quad(v\in S).
 \tag{9}
\]
Leave all other outer variables fixed. Reoptimize every affected
inner variable by Lemma 1; leave unaffected variables unchanged.
Call the resulting critical inner configuration \(\mathbf s^+\).
All affected cases are precisely (3). Repeated incidences in a
one- or two-vertex cycle are counted separately.

The original full first variation vanishes. The fixed-inner
diagonal height estimate from the reflection budget gives cost
at most \(8\sum_{v\in S}\delta_v^2\).
There are no outer--outer Hessian entries. Summing (8) charges
each changed outer variable to its two incident inner factors.
Thus the fully reoptimized action satisfies
\[
 \Re\mathcal F(\mathbf s^+,\mathbf t^+)
 \le M+C\sum_{v\in S}\delta_v^2,\qquad
                       C=8+\frac{49\pi^2}{64}<15.557.
 \tag{10}
\]
The bound is uniform in the word length and in the alias subset.

This estimate also pays for the actual Fourier weights. Set
\(\nu(z)=-\Re g(z)\). The original weight proof gives
\[
 \nu(x+ih)\ge c_0+c_1h>2\pi h,\quad
 c_0=\frac{\sin(.66\pi)\log2}{2\pi},\quad
 c_1=.34\pi-\frac{\sin(.66\pi)}2
                    \qquad(.27\le x\le.33).
 \tag{11}
\]
Consequently the true upper bound for the wrapped factor
\(\widehat P_N(Nt)d_N(e^{-2\pi it})e^{2\pi iNt}\)
has rate at most \(-2\pi h+\eta\), for any fixed \(\eta>0\).
This follows from the whole-strip maximum bound for \(d_N\);
it does not assume a reciprocal-factorial relative expansion
outside its proved domain.

The outward scalar reserve is
\[
 2\pi h-C(.071)^2>.009,\qquad
 2\pi h-C(.071)^2-\frac1{1000}>\frac1{125}.
 \tag{12}
\]
Hence the exact local factorial density with its actual wrapped
weights, evaluated at the reoptimized inner critical configuration,
is at most
\(\operatorname{poly}(N)e^{N(M-|S|/125)}\).
Unreflected four-type weights remain in their already proved
relative-comparison domain. For each fixed word, continuity retains
a smaller strict gap on a neighborhood of these configurations.

The conclusion is an action and local-density estimate. Turning it
into a bound for a complete alias term still requires the full
conditional-source packet and its real tails and cotangent aliases
on the shifted parameter sets, followed by control of the remaining
outer contours. Lemma 1 alone is not that source theorem.

## 4. Reproduction

Run:

    python3 experiments/check_mixed_reoptimized_alias_action.py

The checker verifies all twelve pointing faces using 1,536 exact
uniform slabs and harmonic parameter-boundary reductions, all 1,024
horizontal curvature intervals, and eight explicit scalar reserves.
It uses the original logarithmic equations throughout. No numerical
root proposal or finite-word sampling enters acceptance.
