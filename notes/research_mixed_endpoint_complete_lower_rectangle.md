# The complete endpoint asymptotic on the enlarged lower rectangle

Research assembly, 8 November 2026. The original endpoint finite sum
now has a nonzero leading term on the whole rectangle
\[
\mathcal R=\{e:6/25\le\Re e\le49/100,\quad-3/50\le\Im e\le0\}.
                                                               \tag{1}
\]
Earlier results covered a smaller rectangle and a neighborhood of
the particular cap critical path. The two new region proofs cover
all the intervening private-index values. This distinction matters
when constructing an outer contour: knowing the endpoint sum only
at the outer critical point does not justify using its asymptotic
along a connecting path.

This note assembles complete finite-sum theorems. It does not
construct that outer contour, compare the outer action along it,
or enlarge the established family of knots. No numerical evaluation
is used.

## 1. The function and its leading term

Let \(G_N\) be the original canonical sine-factorial interpolation,
\(e_l(w)\) the original Newton polynomials in the ordinary color,
and \(S_l=\prod_{j=1}^{l}2\sin(\pi j/N)\). The function is exactly
\[
C_N(e,w)=\sum_{l=0}^{N-1}
              \frac{e^{i\pi e l}e_l(w)}{S_lG_N(Ne-l)}.
                                                               \tag{2}
\]
Terms beyond the real private index remain in this sum; they
are not deleted using physical-grid termination.

At complete ordinary color \(w=-2\), its original phase is
\[
F(e,u)=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu,\qquad
J'(q)=\Log(2\sin\pi q).
                                                               \tag{3}
\]
Use the original primitive normalization and the root \(u_c(e)\)
for which \(F_u(e,u_c)=0\), with zero logarithmic lift. It has
\(0<\Re u_c<\Re e<1/2\). Define \(S(e)=F(e,u_c(e))\).

**Theorem.** On a fixed open complex neighborhood of
\(\mathcal R\times\{-2\}\),
\[
C_N(e,w)=N^{-3/2}A(e,w)e^{NS(e,w)}
                     (1+O_{\mathrm{hol}}(N^{-1})),
\qquad A(e,w)\ne0.
                                                               \tag{4}
\]
The limit includes all integer levels, both parities, and every
fixed mixed derivative of the normalized error on smaller
neighborhoods. At complete color the coefficient is
\[
A(e,-2)=
\frac{\sqrt{2\pi}}
{\sqrt{-F_{uu}(e,u_c)}
 (2\sin\pi u_c)^{3/2}(2\sin\pi(e-u_c))^{1/2}},
                                                               \tag{5}
\]
with the original branches. In particular, uniformly for
\(e\in\mathcal R\) and all sufficiently large \(N\),
\[
|C_N(e,-2)|\ge
\frac{|A(e,-2)|}{2N^{3/2}}\exp\{N\Re S(e)\}.
                                                               \tag{6}
\]

## 2. Coverage of the rectangle

For \(6/25\le E\le27/100\), let \(\eta_0(E)\) be the depth
of the explicit curve
\[
p(t)=1-2t^2+2it,\qquad
E-i\eta_0(E)=\frac{\Log p(t)}{2\pi i}.
                                                               \tag{7}
\]
Its real part increases strictly with \(t>0\), so the depth
is uniquely defined. The auxiliary critical point is real on
this curve. The two sides of the curve have separate complete
source proofs:

* For \(0\le\eta\le\min\{\eta_0(E),3/50\}\), use
  [the shallower-region extension](research_mixed_endpoint_above_curve_to_rectangle.md).
  Its real endpoint comparisons, force monotonicity, and
  upper-half bounds pay every omitted row. The retained
  contour contains the nonnegative-height auxiliary saddle.
* For \(\eta_0(E)\le\eta\le3/50\), use
  [the deeper-side corridor](research_mixed_endpoint_below_auxiliary_curve.md).
  Explicit bounds on the auxiliary critical point and Hessian
  compare both real cuts with its action. The signed-height
  contour estimate includes both Fourier remainders and all
  joining segments. When \(\eta_0(E)>3/50\), this second
  interval is empty and the first one covers the entire depth.

These two closed parameter sets cover
\([6/25,27/100]+i[-3/50,0]\). Their proofs retain the same
finite function (2), critical root, primitive constants,
coefficient (5), and density \(+N\). They agree at zero
auxiliary height; neither proof takes a contour of zero height.

For \(27/100\le E\le49/100\), use the already proved
[deeper endpoint rectangle](research_mixed_endpoint_cap_rectangle_deeper_extension.md).
This completes the coverage of (1). Each of the three input
theorems holds on a fixed open neighborhood of its compact
set. Their union contains a fixed neighborhood of the compact
rectangle. The original root and symbols agree on overlaps,
so their relative errors have common bounds after a finite
cover. This proves (4). Cauchy's formula gives the stated
derivatives, and a uniform relative error less than \(1/2\)
gives (6).

The same shallower-region theorem also supplies a western
extension with \(1/8\le E<6/25\) and
\(0\le\eta\le\min\{\eta_0(E),3/50\}\). It supplies no full
rectangle at these smaller real parts. A proposed outer
contour entering the deeper side there still needs a separate
source estimate, as well as a comparison with the outer
critical action.
