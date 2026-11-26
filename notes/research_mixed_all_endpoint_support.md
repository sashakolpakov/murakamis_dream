# Endpoint bounds for every type-three and type-four block

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

This note gives one source-support construction for the seven endpoint
orientations complementary to the proved
[(4,3) right-endpoint case](research_mixed_43_endpoint_support.md).
The 192-bit author certificate passes 165 source values on 38,579 exact
source cells and all 112 reference boundary products on 1,774 cells.
The independent 320-bit replay passes all 165 values on 38,621 source
cells and all 112 products on 1,829 reference cells, after 97 exact
refinements. Full written and acceptance-code reviews pass.
It does not assert the remaining global mixed-word estimate.

## 1. Original source and reference domains

Let \(\eta,\epsilon\in\{0,1\}\) denote the left-leg and own-block types,
with zero meaning type three. Use
\[
 R_3=[.30,.39]+i[-.03,.02],\qquad
 R_4=[.27,.33]+i[-.057,-.02].                         \tag{1}
\]
The actual cyclic critical legs lie in these rectangles, by the proved
window and type-four height theorems. Fix the original normalized primitive
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},
 \qquad 0<\Re z<1,
\]
with its original continuation. Its additive constant is retained in every
phase and supporting plane below. For references
\(a\in R_{3+\eta},b\in R_{3+\epsilon}\), the original zero-lift root
\(s=s(a,b)\) defines
\[
 \begin{split}
 \Phi(a,b)={}&g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias\\
 &-(1+\eta/2)g(a)-(1+\epsilon/2)g(b),\\
 0={}&g'(s+a)+g'(s+b)-(2+\epsilon)g'(s)+2\pi ia.
 \end{split}                                                     \tag{2}
\]
Here \(g'(z)=\log(1-e^{-2\pi iz})\) with the original lift and
\(J(u)=\Re g(u)\). The central conditional theorem proves holomorphy
on a neighborhood of the whole reference product before any boundary
maximum principle is applied.

Write \(c=0\) for the left endpoint and \(c=1\) for the right endpoint.
The target pair is
\[
 (a',b')=\begin{cases}(e,z),&c=0,\\(z,e),&c=1,\end{cases}
 \quad e\in\{0,1\},\quad z=x+ih,\quad0\le x\le1.                 \tag{3}
\]
The moving target type is \(\beta=\epsilon\) for \(c=0\), and
\(\beta=\eta\) for \(c=1\). Its full graph heights are
\[
 \begin{array}{c|c|c}
 \beta&\sigma&h\\\hline
 0&0&[-.03,.02]\\
 1&0&[-.057,0]\\
 1&1&[0,.014].
 \end{array}                                                     \tag{4}
\]
The reference type-four height restriction in (1) is not imposed on targets.
Both endpoint representatives in (3) are retained in the supporting plane.

**Theorem 1.** Uniformly in (1), (3), and (4), the literal finite kernel
and its actual Fourier weight obey, for sufficiently large \(N\),
\[
 |C_{\epsilon,N}(e^{-2\pi ia'},e^{-2\pi ib'})|
 |d_N(e^{-2\pi iz})e^{2\pi iN\sigma z}|^{\beta/2}
 \le C N^A\exp N\left\{
 \Re[\Phi+\Phi_a(a'-a)+\Phi_b(b'-b)]-\frac1{2000}\right\}.
                                                               \tag{5}
\]
Every row, the forced Fourier branch, and selected-alias normalization remain.
The estimate persists with a smaller strict gap in a fixed small complex
neighborhood of the tapered endpoint. Derivatives in that endpoint have
the same scope. Derivatives in the moving target concern the squared
integer-weight holomorphic expression, or complete original contractions;
no derivative of a half-modulus weight and no division by \(d_N\) is used.

The previously proved \((\eta,\epsilon,c)=(1,0,1)\) case supplies one
orientation. The new certificate covers the other seven, rather than
altering the completed theorem or its records.

## 2. Full row support, including both Fourier branches

Set
\[
 I_h(u,x)=\int_0^u\log|1-e^{2\pi h-2\pi i(x+t)}|\,dt,
 \quad \nu_h(x)=-\Re g(x+ih),\quad h_+=\max(h,0).
\]
The exact finite products and the whole-period Fourier-weight upper bound
give the raw row exponent
\[
 E(u,x;h)=I_h(u,x)-(1+\epsilon)J(u)-2\pi c h u
 +\frac\beta2\{\max(\nu_h(x),2\pi h_+)-2\pi\sigma h\}.
                                                               \tag{6}
\]
The finite product estimates are uniform through product zeros and the top
rows; their errors are \(O(\log N)\), with an arbitrarily small fixed
Fourier-envelope tolerance. No cancellation between rows is needed in (6).
For \(S_h(\kappa)=\sup_{0\le u,x\le1}(E-\kappa x)\), convexity in
\(\kappa\) gives certified upper chords between any two certified support
values. The chords are used only on their own slope intervals.

For a reproducible smooth-branch formula put
\(H=|h|\), \(G_H(v)=\Re g(v-iH)\). Then (6) minus \(\kappa x\)
is the maximum, over \(q\in\{0,\beta\}\), of
\[
 \begin{split}
 G_H(x+u)&-(1+q/2)G_H(x)-(1+\epsilon)J(u)
       +2\pi(h_+-ch)u\\
 &+\pi h_+(\beta-q/2)-\pi\beta\sigma h
       -(\kappa+q\pi h_+)x .
 \end{split}                                                     \tag{7}
\]
For \(\beta=0\) there is one branch. Formula (7) includes the forcing
alternative rather than replacing it by the factorial branch.

There are five new source families \((\epsilon,\beta,c)\):
\((0,0,0),(0,0,1),(1,1,0),(1,0,1),(1,1,1)\).
Each uses the three heights \((-.03,0,.02)\) or \((-.057,0,.014)\)
and eleven slopes \(-.5,-.4,\ldots,.5\), making 165 support values.
Floating optimization only proposes rational upper targets. Whole-square
exact dyadic interval covers of (7) decide every acceptance. Interior
cells use the midpoint and the complete real Hessian remainder. At a row
endpoint, the smooth part is expanded and the exact minimum of \(J\)
on the row interval is retained. For \(h=0\) cells meeting a product zero,
separate exact ranges of \(J\) are used; these require only the interval
endpoints and the translates of \(1/6,5/6\). Thus the closed row square,
including all corners and the line \(u+x=1\), is covered.

## 3. Reference-boundary comparison with the original complex tangent

Let \(j=1-c\) index the moving coordinate in the pair \((a,b)\), and
let \(r=(a,b)\). Define \(t_j=ih\), \(t_{1-j}=e\), and
\[
 \kappa=\Re\Phi_j,\qquad
 C_e=\Phi+\sum_{k=0}^1(t_k-r_k)\Phi_k .                        \tag{8}
\]
The source defect is \(S_h(\Re\Phi_j)-\Re C_e\). This is separately
subharmonic in both reference variables: it is the locally bounded
supremum over the fixed compact source square of harmonic defects.
This statement concerns the actual supremum, not a slope-restricted
subdomain or extrapolated chords. Hence the sixteen products of reference
rectangle edges suffice.

For a support chord \(\alpha\kappa+\gamma\), its holomorphic defect has
exact derivative
\[
 \partial_{r_l}(\alpha\Phi_j+\gamma-C_e)
 =\sum_{k=0}^1(r_k-t_k+\alpha\mathbf1_{k=j})H_{kl},\qquad
 H=\Phi'' .                                                     \tag{9}
\]
The complete complex tangent, including the height term, remains in (8).
The Schur complement used for (9) is
\[
 \begin{split}
 T&=g''(s+a)+g''(s+b)-(2+\epsilon)g''(s),\\
 A&=g''(s+a)+2\pi i,\qquad B=g''(s+b),\\
 H_{aa}&=g''(s+a)-(1+\eta/2)g''(a)-A^2/T,\\
 H_{ab}&=-AB/T,\\
 H_{bb}&=g''(s+b)-(1+\epsilon/2)g''(b)-B^2/T.
 \end{split}                                                     \tag{10}
\]
On every parameter cell, an affine original-logarithm Newton self-map
certifies the selected root and a separate point Newton disk certifies
its midpoint. Polynomial roots provide centers only. The inherited
strict conditional Hessian identifies these roots with (2).
The checker bounds every intersecting slope chord by its midpoint value
plus the enclosed edge-direction derivatives in (9). The certified
slope range lies strictly in \((-.5,.5)\). Every accepted defect is below
\(-1/1000\), for both geometric endpoint representatives and every
required horizontal target height. Exact prefix-free binary covers of
mass one verify all 112 boundary products.

## 4. Raw seam bounds throughout the target height intervals

At \(x=0\) or \(1\), put \(R=e^{2\pi(1-2c)h}\) and
\(D_k=|1-r^k|^2\). The literal raw row has modulus
\[
 \prod_{k=1}^j\sqrt{R+(1-R)^2/D_k}\;S_j^{-\epsilon}.             \tag{11}
\]
The moving target Fourier half-weight has zero upper seam rate in (4):
there is no weight for type three; for negative type-four heights its
forced upper branch is zero; for selected positive heights the alias
normalization cancels its radial rate. This does not cancel any rows.

For \(R\ge1\), the first factors are at least one. Their full product
is \((R^N-1)/(N(R-1))\), giving rate \(\log R\). The elementary
\(-J(u)<1/6\) then gives the coarse raw rate
\(\log R+\epsilon/6\). For \(R_0\le R\le1\), use the factorwise bound
\[
 R+(1-R)^2/D_k\le1+(1-R_0)^2/D_k.
\]
The full positive majorant is
\[
 \frac{\sinh(N\alpha)}{N\sinh\alpha},\qquad
 \alpha=\operatorname{arsinh}((1-R_0)/2),                       \tag{12}
\]
giving raw rate \(\alpha+\epsilon/6\). All these bounds are uniform
at \(h=0\). Split each target interval there. The coarse rate is affine
or constant in each piece; subtracting the original tangent gives an
affine height bound, checked at its two endpoints.

Only \((\eta,\epsilon,c)=(1,1,1)\), \(h\in[-.057,0]\), needs a
sharper coupled row estimate. The factors in (11) increase with \(R\ge1\),
so it is enough to set \(R=e^{.114\pi}\). The exact continuum row rate
has derivative
\[
 \frac12\log\frac{4Rv+(R-1)^2}{16v^2},
 \qquad v=\sin^2(\pi u).                                      \tag{13}
\]
There is one positive quadratic root
\[
 v_*={R+\sqrt{R^2+4(R-1)^2}\over8}\in(0,1),\qquad
 u_*={\arcsin\sqrt{v_*}\over\pi}.
\]
The first critical point is a maximum and the second is a minimum.
The outward scalar check gives the first rate below \(7/25\), while
the last-row rate is \(.114\pi<9/25\); the initial rate is zero.
Thus the entire raw seam has the uniform rate \(9/25\). This includes
all finite rows by the same uniform product-entropy estimate, and is
not the coherent endpoint identity. Both height endpoints again suffice
after subtracting the affine geometric tangent.

Every seam defect is certified below \(-1/1000\). For each fixed row,
(6) minus its plane is subharmonic in the moving target; the Fourier
maximum retains both harmonic branches. Its compact row supremum is
also subharmonic. Horizontal and raw seam bounds therefore cover the
whole target rectangles (4). The reference maximum principles then
cover (1). Absorb the small Fourier-envelope tolerance in the reserve
between \(1/1000\) and \(1/2000\) to obtain (5).

## 5. Endpoint thickening and scope

Near the tapered endpoint, exact product regularization gives
\(|p_j(Y)|\le S_j N^A e^{N\omega(\delta)}\), uniformly in all rows,
with \(\omega(\delta)\to0\). The denominator monomials and the original
plane cost only \(O(\delta)\); the endpoint Fourier half-weight likewise
has arbitrarily small rate by the proved forced seam estimate. Since
all estimates above are raw row bounds, these costs fit inside the strict
gap. This proves a fixed small endpoint neighborhood without replacing
any coherent sum by its cancelled endpoint value.

Cauchy estimates apply to the actual holomorphic integer-power products,
with the moving weight kept fixed when differentiating the other endpoint.
No half-weight branch is introduced. The theorem supplies all tapered
endpoint families; it supplies no claim for the intervening outer-angle
region or a full mixed cyclic-word asymptotic.

Reproduction:

    python3 experiments/certify_mixed_all_endpoint_support.py --precision 192

    python3 experiments/replay_mixed_all_endpoint_support.py --precision 320

The independent replay uses the opposite-frequency dilogarithm, original
sine logarithms and cotangents, exact complete-tree coverage, and every
saved rational Newton witness. Neither the bounded floating pilots nor
numerical root selection is part of the acceptance criteria.
