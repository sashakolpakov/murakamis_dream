# A directed phase bound for one isolated left transition

Research proof, 4 November 2026. This treats the original allocated
conditional action and pays the adjacent plateau height-reset cost.
It does not assert a finite-source estimate on the new transition
parameters.

Use the original zero-lift phase \(\phi_{\eta\epsilon}\),
\(\eta,\epsilon\in\{0,1\}\), and reference rectangles
\[
 R_3=[.30,.39]+i[-.03,.02],\qquad
 R_4=[.27,.33]+i[-.057,-.02].                         \tag{1}
\]
Put \(P=[.22,.45]\) and \(\rho(t)=(t-.10)/.12\) for
\(.10\le t\le.22\). Let \(r=(r_0,r_1)\) be any independent
typed reference pair. Choose a low coordinate \(j\in\{0,1\}\),
put \(k=1-j\), and define
\[
 z_j=t+i\rho(t)\Im r_j,\qquad
 z_k=x+i\rho(t)\Im r_k,\qquad x\in P,
 \quad \Gamma_r(z)=\phi(r)+\phi'(r)\cdot(z-r).       \tag{2}
\]
Only this common suppression factor is asserted. Independent extra
neighbor suppressions and selected complex heights are not included.

**Theorem 1.** With \(q_0=11/2\) and \(q_1=151/20\),
\[
 \Re\{\phi(z)-\Gamma_r(z)\}
 +q_j(1-\rho(t))^2(\Im r_k)^2
 \le-\frac{(\Re r_j-t)^2}{16}
 \le-\frac1{6400}.                                  \tag{3}
\]
The cost \(q_j\) is precisely the
[oriented plateau reset](research_mixed_oriented_height_reset.md)
for the other block incident to the plateau coordinate: when the low
coordinate is the first argument of this block, the adjoining block
resets its first argument; when it is the second, the adjoining block
resets its second argument. Both real coordinates of that adjoining
block remain free in its source domain.

## 1. A convex phase domain and the actual secants

Define the convex polygons by their counterclockwise vertices
\[
 \begin{split}
 D_3={}&\operatorname{conv}\{.10,\ .22-.03i,\ .39-.03i,
                                      \ .39+.02i,\ .22+.02i\},\\
 D_4={}&\operatorname{conv}\{.10,\ .22-.057i,\ .33-.057i,
                                                   \ .33-.02i\},\\
 B_3={}&P+i[-.03,.02],\qquad B_4=P+i[-.057,0].
 \end{split}                                                   \tag{4}
\]
Every straight reference-to-target segment from (2) lies in the
product with \(D_{3+\eta}\) or \(D_{3+\epsilon}\) at coordinate
\(j\) and the corresponding \(B\) at coordinate \(k\).
In particular the upper boundary of \(D_4\) joins \(.10\) to
\(.33-.02i\); it is not the narrower target-height triangle.

Throughout these products, \(0<\Re a,\Re b<1/2\) and
\(|\Im\cot\pi a|,|\Im\cot\pi b|<1/2\). One explicit bound is
\[
 |\Im\cot\pi w|
 \le\frac{121}{120}\frac{\sinh(.114\pi)}
                                  {2\sin^2(.22\pi)}<\frac12.
                                                               \tag{5}
\]
For the left ramp, use
\(\rho(x)/x^2\le(121/120)/(.22)^2\), whose maximum is attained
at \(x=.20\), convexity of \(\sinh\), and the decrease of
\(\sin(\pi x)/x\). For \(x\ge.22\), the same estimate follows
from \(|\Im w|\le.057\) and \(\sin(\pi x)\ge\sin(.22\pi)\).
The [cotangent root theorem](research_mixed_closed_cotangent_roots.md)
therefore supplies the unique original zero-lift inner root, a
holomorphic allocated phase on a neighborhood of each product, and
\(A=-\Re\phi''>0\). No finite-source continuation is used here.

Write \(d=\Re z_j-\Re r_j<0\) and
\[
 \lambda=\frac{1-\rho(t)}{\Re r_j-t},\qquad
 z-r=d\,w,\qquad
 w_j=1+i\lambda\Im r_j,\quad
 w_k=u+i\lambda\Im r_k,
 \quad u=\frac{x-\Re r_k}{d}\in\mathbb R.             \tag{6}
\]
If \(y\) is the real part of coordinate \(j\) anywhere on this
segment, and \(r_{\min}=.30\) for type three or \(.27\) for type
four, then
\[
 0\le\lambda\le\frac1{\Re r_j-.10}
                  \le\frac1{\max(r_{\min},y)-.10}.     \tag{7}
\]
The first inequality follows by multiplying positive denominators;
the remaining numerator is
\((t-.10)(.22-\Re r_j)\le0\).

## 2. Directed Schur certificate

Let \(H=\phi''\). On each product in (4), with the local upper
bound \(L\) for (7), the certificate proves
\[
 \Re(w^T H w)+2q_j\beta_k^2<-\frac18,
 \qquad
 w_j=1+i\beta_j,\quad w_k=u+i\beta_k,
 \quad u\in\mathbb R,                                \tag{8}
\]
for all \((\beta_0,\beta_1)\) in the convex hull of the origin and
\(L\) times the four corners of the reference-height rectangle.
Thus it includes the actual direction in (6).

Here is the exact scalar test, with
\(w^0_j=1+i\beta_j\), \(w^0_k=i\beta_k\),
\(a=-\Re H_{kk}>0\), and
\(b=\Re\sum_\ell H_{k\ell}w^0_\ell\):
\[
 -\Re((w^0)^THw^0)-\frac{b^2}{a}
                           -2q_j\beta_k^2>\frac18.    \tag{9}
\]
Completing the real square in \(u\) proves (8). For a fixed real
\(u\), its left side is convex in \(\beta\), since its quadratic
height matrix is \(A\) plus a nonnegative diagonal. It is therefore
enough to test the five slope vertices. For fixed \(u,\beta\),
\(\Re(w^THw)\) is harmonic in each original complex parameter.
Successive maximum principles reduce (8) to products of polygon
edges. This does not apply a maximum principle to the Schur ratio.

The checker uses the entire polygons and the bound
\(L=1/(r_{\min}-.10)\), except in the ordered type-four/type-four
case with low coordinate one. There it clips \(D_4\) at the exact
real cuts
\[
 .10,\ .27,\ .275,\ .280,\ldots,\ .325,\ .330        \tag{10}
\]
and uses \(L=1/(\max(.27,\ell)-.10)\) on each slab with left
endpoint \(\ell\). All clipped edges are retained, including the
new vertical edges. There are 336 edge products; the outward cover
has 75,094 accepted cells. Each edge product has a prefix-disjoint dyadic
cover of exact total area one. Rational affine Newton witnesses are
checked against the original logarithmic equation; their roots stay
in the selected cotangent strip. Floating proposals have no role in
acceptance, and a saved-cover replay needs no new proposals.

## 3. Integration and scope

The direction \(w\) in (6) is constant along the reference-to-target
segment. Applying (8) pointwise and integrating the exact Taylor
remainder gives
\[
 \Re\{\phi(z)-\Gamma_r(z)\}
 \le-\frac{d^2}{16}-q_j\lambda^2(\Im r_k)^2d^2.
                                                               \tag{11}
\]
This is (3), since \(\lambda^2d^2=(1-\rho(t))^2\) and
\(\Re r_j-t\ge.27-.22=.05\).

The conclusion pays a genuine neighboring plateau reset debit.
It does not yet estimate the whole finite conditional block at (2).
In particular real-index tails, the full cotangent aliases and both
midpoint joins must still be bounded on these prescribed complex
parameters. A complete transition-star source theorem also needs
that source input and its own incidence bookkeeping; no assertion
for overlapping stars or short cyclic words is made here.

```sh
python3 experiments/certify_mixed_isolated_transition_phase.py --precision 256
python3 experiments/certify_mixed_isolated_transition_phase.py --precision 320 --input repro/results/research-mixed-isolated-transition-phase.json --output /tmp/research-mixed-isolated-transition-phase-review.json
```
