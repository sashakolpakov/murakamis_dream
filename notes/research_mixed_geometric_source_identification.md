# The geometric solution is the selected source critical point

Research proof, 5 November 2026. For every fixed open word in three-
and four-crossing blocks, the positive geometric inverse equals the
critical point localized from the original finite source. Its critical
action therefore has the original marked volume normalization. This
identification does not show that the local contribution survives in the
whole open-chain quantum sum.

## 1. The two points and the remaining distinction

Fix a nonempty word \((n_1,\ldots,n_m)\), \(n_j\in\{3,4\}\).
Let \(z_*\) be the original source critical point, with coordinates
\((s_j,t_j,u_L,u_R)\), given by the
[open-word localization theorem](research_mixed_open_word_critical_localization.md).
Its nonprivate legs lie in
\(Q=[.23,.45]+i[-.12,.12]\), its private legs in
\(E=[.33,.47]+i[-.09,.08]\), and its two endpoint variables satisfy
\(0<\Re u_L<\Re s_1\), \(0<\Re u_R<\Re t_m\).
In particular every leg has real part at least \(23/100\) and
imaginary part of absolute value at most \(3/25\).

Let \(z_{\rm geom}\) be the inverse leg coordinates and outside
wire coordinates of the positive unit solution on the same marked
path. The [absolute action calibration](research_mixed_geometric_action_calibration.md)
already proves, with the same original logarithms,
\[
 \nabla\mathcal F_m(z_*)=\nabla\mathcal F_m(z_{\rm geom})=0,
 \qquad 2\pi\Re\mathcal F_m(z_{\rm geom})=V_{\rm cells}.
 \tag{1}
\]
The two zero-gradient assertions have different constructions. Their
equality is not part of (1).

The [unit cotangent bounds](research_mixed_unit_cotangent_bounds.md) give
at every geometric leg
\[
 \frac18<\Re s<\frac12,\qquad
 |\Im\cot\pi s|<1,\qquad
 |\Im s|<H:=\frac{\log(1+4\sqrt3)}{2\pi}.
 \tag{2}
\]
The [endpoint sum lemma](research_mixed_three_endpoint_pair_sum.md)
also gives \(\Re(s_1+t_1)>1/2\) when the left endpoint is
type three, and the corresponding assertion at the right endpoint.
It includes the one-vertex case. These inequalities hold at \(z_*\)
as well, directly from \(E,Q\). The real wire-before-leg order
holds at both points.

## 2. Every leg segment stays in the cotangent domain

We need a statement about the segment, because the cotangent domain
itself is not convex. Write
\[
 f(x)=-\frac{\log\cos(2\pi x)}{2\pi},\qquad 0<x<1/4.
 \tag{3}
\]
For \(z=x+iy\), \(0<x<1/2\), the exact condition is
\[
 |\Im\cot\pi z|<1
 \quad\Longleftrightarrow\quad
 \begin{cases}
 |y|<f(x),&0<x<1/4,\\
 \text{no height restriction},&1/4\le x<1/2.
 \end{cases}
 \tag{4}
\]
Here \(f'(x)=\tan(2\pi x)>0\) and
\(f''(x)=2\pi\sec^2(2\pi x)>0\).

**Lemma 1.** Let \(z=x+iy\) satisfy (2), and let
\(z_0=a+ib\) satisfy \(23/100\le a<1/2\), \(|b|\le3/25\).
Then the straight segment from \(z\) to \(z_0\) satisfies (4).

*Proof.* First,
\[
 H<f(23/100),\qquad 3/25<f(23/100).
 \tag{5}
\]
The first inequality is (15) of the unit cotangent note. For the
second, \(\cos(23\pi/50)<22/175<1/3\), while
\(e^{6\pi/25}<e<3\). If \(x\ge23/100\), every point of the
segment has real part at least \(23/100\) and height bounded by
\(\max(H,3/25)<f(23/100)\). Monotonicity of \(f\), followed
by the unrestricted second case of (4), proves the claim.

Suppose instead \(1/8<x<23/100\). The tangent line to \(f\) at
\(x\) is \(L_x(t)=f(x)+f'(x)(t-x)\). Since \(a\ge23/100\),
\[
\begin{split}
 L_x(a)&\ge f(x)+f'(x)(23/100-x)\\
 &\ge f(1/8)+f'(1/8)(23/100-1/8)\\
 &=\frac{\log2}{4\pi}+\frac{21}{200}>\frac3{25}.
\end{split}                                                    \tag{6}
\]
The middle expression is increasing in \(x\) on this interval:
its derivative is \(f''(x)(23/100-x)\ge0\). For the last strict
inequality it suffices that \(\log2>1/2\) and \(\pi<4\),
giving a lower bound \(1/32+21/200>3/25\).

At the geometric endpoint, \(|y|<f(x)=L_x(x)\); at the source
endpoint, \(|b|\le3/25<L_x(a)\). The triangle inequality
therefore places every intermediate height strictly between the two
affine lines \(\pm L_x\). Convexity gives \(L_x(t)\le f(t)\)
whenever the intermediate real part is below \(1/4\). Above that
value (4) imposes no restriction. This proves the lemma. \(\square\)

## 3. Identification by the actual Hessian

Apply Lemma 1 separately to every leg on the segment
\[
                         z(\lambda)=(1-\lambda)z_*+
                                      \lambda z_{\rm geom},
                         \qquad 0\le\lambda\le1.
 \tag{7}
\]
The real endpoint ordering and the type-three endpoint-sum inequalities
are linear, so they also persist along (7). These are exactly the
hypotheses of the [cotangent Hessian criterion](research_mixed_cotangent_cone_injectivity.md#2-what-this-gives-for-the-full-open-word).
It proves
\[
                  -\Re\mathcal F_m''(z(\lambda))\succ0
                    \qquad(0\le\lambda\le1).
 \tag{8}
\]
Every primitive stays on its original strip along this segment.
No extrapolation of the small source localization box is used in (8).

Put \(d=z_{\rm geom}-z_*\). The complex symmetric Hessian has
Hermitian real part equal to its entrywise real part. If \(d\ne0\),
integration along (7) gives
\[
\begin{split}
 &\Re\left[d^*\{-\nabla\mathcal F_m(z_{\rm geom})
                         +\nabla\mathcal F_m(z_*)\}\right]\\
 &\hspace{12mm}=
       \int_0^1 d^*[-\Re\mathcal F_m''(z(\lambda))]d\,d\lambda>0.
\end{split}                                                    \tag{9}
\]
Both gradients on the left are zero by (1), a contradiction.

**Theorem 2.** For every fixed nonempty open word in three and four,
\[
 \boxed{\quad z_*=z_{\rm geom},\qquad
                  2\pi\Re\mathcal F_m(z_*)=V_{\rm cells}.\quad}
 \tag{10}
\]
The original marked completion identifies these cells with their part
of the corresponding partial filling, retaining its original primitive
slopes and all complete outside-edge volumes. This does not change the
topological scope of that completion theorem.

## 4. Consequence and the next analytic requirement

The [local Gaussian theorem](research_mixed_open_local_gaussian.md)
already supplies a nonzero coefficient at \(z_*\), with all local
factor hypotheses discharged. Its specified unselected local integral
therefore satisfies
\[
 I_{{\rm loc},N}=\kappa_N^{m+k}N^{-3/2}A_m
             e^{N\mathcal F_m(z_*)}(1+O(N^{-1})),
 \qquad A_m\ne0,\quad |\kappa_N|=1,
 \tag{11}
\]
where \(k\) is the number of type-four vertices. In particular
\[
             \lim_{N\to\infty}\frac{2\pi}{N}
                       \log|I_{{\rm loc},N}|=V_{\rm cells}.
 \tag{12}
\]
Both level parities are included. The integral in (11) is still only
the previously specified local term of the exact finite source.
The complement of its contour, the other Fourier terms, and the
ordinary-boundary estimates needed for attachment remain unproved.
Equation (12) is consequently not a new knot volume-conjecture theorem
or a finite-exception result.
