# Two stronger right-clamping estimates that fail

Research calculations, 5 November 2026. Neither example contradicts the
selected-height comparison or unselected clamping theorem. They explain
why those arguments retain the complex phase and compare the selected
and unselected heights separately.

Use the original allocated phases \(\phi_{\eta\epsilon}\), primitive
\(g\), and quadratic profile \(R(t)=400(.5-t)^2\) from
[the clamping proof](research_mixed_unselected_right_clamping.md).
Type indicator one denotes type four. All numbers below are enclosed
outward by the accompanying checker using the original logarithmic roots.

## A selected rate can increase along the right taper

Take three type-four positions with the two neighboring targets fixed
at \(a=c=1/2\). The selected center has
\[
 t=481/1000,\qquad h=.014R(t)=2527/1250000,\qquad b=t+ih.
\]
The center's slow and fast cutoff fractions are both one. Neighboring
heights vanish at the half-period endpoint, so these targets are
compatible with the hybrid contour. Write
\(F(b)=\phi_{11}(a,b)+\phi_{11}(b,c)\).

At this point
\[
 -2\pi h-\Re g(b)>1/2000.
\]
Thus the active correction in
\(\Re F(b)+\max\{\Re g(b),-2\pi h\}\) is \(-2\pi h\).
Its derivative along \(b(t)=t+i(.014)R(t)\) satisfies
\[
 \Re\{[F'(b)+2\pi i][1+i(.014)R'(t)]\}>1/5.
\]
Numerically the derivative is about .2322934. The other branch has
derivative about -.3942496 and is inactive. Hence the complete selected
rate is not decreasing throughout the right taper. Removing the selected
height at the same real coordinate avoids that false premise.

## Absolute row bounds cannot always be clamped to the same local phase

Take neighboring real targets \(a=c=1/10\), a center target
\(t=1/2\), and the type triple \((4,4,3)\). All heights are zero.
The proposed clamped center is \(b_0=9/20\), also at height zero,
because the neighboring slow cutoffs vanish.

Let \(J(x)=\Re g(x)\), with its continuous real periodic extension.
Choose two row fractions \(u=6/25\), \(v=11/40\). The complete
absolute-row expression, including the left type-four halfweight, is
\[
\begin{split}
 E={}&J(a+u)-J(a)+J(1/2+u)-3J(u)\\
    &+J(1/2+v)+J(c+v)-J(c)-2J(v)-\tfrac12J(a).
\end{split}
\]
The middle Fourier weight has rate zero at \(t=1/2\). Direct
outward evaluation gives
\[
 E-\Re\{\phi_{11}(a,b_0)+\phi_{10}(b_0,c)\}>1/5;
\]
the difference is about .2322257. In particular, the supremum of the
absolute-row expressions cannot be bounded by this clamped phase.
The row fractions are rational and occur exactly along levels divisible
by 200, so this obstruction is not an off-grid artifact.

This is a failure of that proposed envelope comparison. Cancellation
inside the original finite kernels is still present; taking their
absolute rows loses it. A supporting-plane comparison using neighboring
blocks, or the complete complex asymptotic where available, remains a
different possibility.

```sh
python3 experiments/check_mixed_right_clamping_obstructions.py
```
