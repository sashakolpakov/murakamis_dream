# Exponential forgetting along an unselected plateau chain

Research deduction, 5 November 2026. This is a real variational
consequence of the proved original phase
Hessian bounds. It uses no new numerical cover and asserts no new
finite-source asymptotic.

## 1. The original open-chain objective

Fix a periodic type word and its actual geometric reference
\(r_j=a_j+i c_j\), extended to integer indices. All target heights
in this note are the fixed, unselected heights \(c_j\). Put
\[
 P=[.22,.45],\qquad .27<a_j<.39.
\]
Take vertices \(0,\ldots,n+1\), with \(n\ge1\), and fix
real endpoints \(x_0=u\in P\), \(x_{n+1}=v\in P\).
The \(n\) interior real coordinates vary independently in \(P^n\).
Let \(\phi_j\) be the original allocated conditional phase on edge
\((j-1,j)\), with the normalized primitive, original logarithmic
root and tangent \(\Gamma_j\) from the
[open-chain boundary note](research_mixed_nonlow_open_chain_boundary.md).
Define
\[
\begin{split}
 e_j(s,t)&=-\Re\{\phi_j(s+i c_{j-1},t+i c_j)
                    -\Gamma_j(s+i c_{j-1},t+i c_j)\},\\
 E_n(x;u,v)&=\sum_{j=1}^{n+1}e_j(x_{j-1},x_j),\\
 V_n(u,v)&=\min_{x\in P^n}E_n(x;u,v).
                                                               \tag{1}
\end{split}
\]
There is one term for each original edge. The periodicity of the
coefficient data does not identify different interior variables.

Original reference stationarity cancels the interior linear terms in
\(\sum_j\Gamma_j\). Consequently, for fixed \(u,v\), minimizing
\(E_n\) is exactly equivalent to maximizing
\[
 f_n(x;u,v)=\Re\sum_{j=1}^{n+1}
                         \phi_j(x_{j-1}+i c_{j-1},x_j+i c_j).
                                                               \tag{2}
\]
Their sum is the reference bulk action plus the two original endpoint
tangent terms, independent of \(x\). No new affine normalization
of a finite source is made.

The reference interior vector is \(a=(a_1,\ldots,a_n)\).
Each \(e_j\) and its gradient vanish at its reference pair.
In particular, with reference endpoints \(a_0,a_{n+1}\), the
unique minimizing interior will be \(a\).

## 2. Uniform Hessian constants, including fixed endpoints

Write \(K_j=-\Re\phi_j''\), the two-by-two real Hessian of
\(e_j\). The existing inputs give throughout all the required
unselected plateau products
\[
               \lambda I_2\preceq K_j\preceq L I_2,
               \qquad \lambda=\frac15,\quad L=20.
                                                               \tag{3}
\]
The lower bound is the
[extraction from the completed full-reset certificate](research_mixed_extracted_plateau_curvature.md),
Theorem 1. Both its original 256-bit cover and completed 320-bit saved
replay recorded a whole-cell lower bound for the least eigenvalue
greater than .202125. Fixed-vector harmonic minimum principles extend
that bound through the full products. This uses the already established
holomorphic original branch and is not a point-sampling assertion.

For the upper bound, use equation (9) of the
[full height-reset theorem](research_mixed_full_height_reset.md).
Its fixed-direction harmonic argument already proves, throughout the
whole unselected source product,
\[
 \Re\{(p+iq)^T\phi_j''(p+iq)\}\le20|q|^2
                         \qquad(p,q\in\mathbb R^2).
\]
Setting \(p=0\) gives \(q^TK_jq\le20|q|^2\).
This deduction uses the extended quadratic inequality, not a claim
that the nonlinear matrix completed in that theorem is harmonic.

For an interior variation \(h\), set \(h_0=h_{n+1}=0\).
Every interior coordinate occurs in two edge forms, even at the first
or last free vertex. Summing (3) therefore gives
\[
 \mu I_n\preceq D_x^2E_n\preceq\Lambda I_n,
 \qquad \mu=2\lambda=\frac25,\quad\Lambda=2L=40.
                                                               \tag{4}
\]
The constants do not depend on the chain length, type period, or
actual reference. The Hessian is tridiagonal: a coordinate gradient
depends only on that coordinate and its immediate neighbors.

Repeated primitive type periods one and two cause no change to (4).
The two incident edge terms at an interior vertex remain distinct
terms of this open chain. Reference stationarity still holds with
its original repeated incidences. A cyclic optimization obtained by
identifying free variables is not being substituted for (1).

## 3. Projected contraction and finite propagation

Set
\[
 \alpha=\frac2{\Lambda+\mu}=\frac5{101},\qquad
 q=\frac{\Lambda-\mu}{\Lambda+\mu}=\frac{99}{101}<1,
 \qquad
 T_{u,v}(x)=\Pi_{P^n}\bigl(x-\alpha\nabla_xE_n(x;u,v)\bigr).
                                                               \tag{5}
\]
Projection is coordinatewise clipping to \(P\). The averaged
Hessian between any two points has spectrum in \([\mu,\Lambda]\).
Thus the derivative-free mean-value comparison for the unprojected
map has Euclidean norm at most \(q\). Projection is nonexpansive,
so
\[
                \|T_{u,v}(x)-T_{u,v}(y)\|_2
                              \le q\|x-y\|_2.               \tag{6}
\]
The unique fixed point is the constrained minimizer \(x^*(u,v)\).
Indeed the projection identity is equivalent to the variational
inequality
\[
 \nabla E_n(x^*;u,v)\cdot(y-x^*)\ge0\qquad(y\in P^n).
                                                               \tag{7}
\]
The contraction argument does not assume that constraints are inactive.

Put
\[
 \Delta=|u-a_0|+|v-a_{n+1}|,\qquad
 G=20\Delta,\qquad C_1=\frac G\mu=50\Delta.
                                                               \tag{8}
\]
At \(a\), changing the endpoints affects only the first and last
gradient coordinates. Each cross-edge derivative has absolute value
at most \(L=20\), by (3). Therefore
\[
                         \|\nabla E_n(a;u,v)\|_2\le G.      \tag{9}
\]
This includes \(n=1\), where both changes enter the same gradient
coordinate and their absolute values are added.

Strong monotonicity, together with (7) at \(y=a\), gives
\[
 \mu\|x^*-a\|_2^2
 \le(\nabla E_n(x^*)-\nabla E_n(a))\cdot(x^*-a)
 \le-\nabla E_n(a)\cdot(x^*-a).
\]
Hence
\[
                             \|x^*(u,v)-a\|_2\le C_1.       \tag{10}
\]

A sharper bound is available because this comparison starts at the
reference. Each residual edge has zero reference value and gradient.
Taylor's formula using (3) gives
\[
 E_n(x;u,v)\ge\frac\mu2\|x-a\|_2^2
       +\frac\lambda2[(u-a_0)^2+(v-a_{n+1})^2],\qquad
 E_n(a;u,v)\le\frac L2[(u-a_0)^2+(v-a_{n+1})^2].
                                                               \tag{10a}
\]
Only the two endpoint edges contribute to the upper bound. Comparing
the minimizer with this competitor and discarding the nonnegative
boundary term proves
\[
 \|x^*(u,v)-a\|_2\le C,
 \qquad
 C=\min\left\{\frac G\mu,
   \sqrt{\frac L\mu}\sqrt{(u-a_0)^2+(v-a_{n+1})^2}\right\}.
                                                               \tag{10b}
\]
Uniformly over both endpoints in \(P\), each endpoint displacement
has absolute value at most .18. Thus
\(C\le.18\sqrt{2L/\mu}=9/5\), independently of the chain length.
This improved reference-start estimate is not used for comparing two
arbitrary nonreference boundary pairs.

Start the iteration at \(x^{(0)}=a\). The map in (5) has locality
radius one, including its projection. Since \(a\) is a fixed point
for reference endpoints, induction gives
\[
 x_j^{(k)}=a_j\quad\text{whenever}
                \operatorname{dist}(j,\{0,n+1\})>k.
                                                               \tag{11}
\]
Only the two boundary-adjacent coordinates can change in the first
step; each later step enlarges the possible changed set by one.
Combining (6), (10b), and (11) proves the following result.

**Theorem 1.** If
\(d_j=\min\{j,n+1-j\}\), then
\[
             |x_j^*(u,v)-a_j|\le Cq^{d_j-1}.                \tag{12}
\]
More strongly, for every integer \(d\ge0\), the whole deep tail
\(J_d=\{j:d_j>d\}\) satisfies
\[
                   \|(x^*-a)|_{J_d}\|_2\le Cq^d.           \tag{13}
\]
For (13), the corresponding coordinates of \(x^{(d)}\) equal
\(a\), while the norm of the full error \(x^{(d)}-x^*\)
is at most \(q^d\|a-x^*\|_2\). There is no sum of coordinatewise
estimates and no factor depending on the number of deep coordinates.

## 4. Freezing the middle and controlling the optimal action

Let \(\widetilde x^{(d)}\) agree with \(x^*\) outside \(J_d\)
and with \(a\) on \(J_d\). It is feasible, and (13) gives
\[
                         \|\widetilde x^{(d)}-x^*\|_2
                                           \le Cq^d.        \tag{14}
\]
By (4), (9), and (10b),
\(\|\nabla E_n(x^*)\|_2\le G+\Lambda C\).
Smoothness and constrained minimality therefore imply
\[
\begin{split}
 0&\le E_n(\widetilde x^{(d)};u,v)-V_n(u,v)\\
  &\le (G+\Lambda C)Cq^d+\frac\Lambda2C^2q^{2d}
                         =:\varepsilon_d.                 \tag{15}
\end{split}
\]
The linear term is retained: (7) does not in general make the gradient
zero at an active constraint.

There is a stronger bound once the frozen part is sufficiently deep.
Every reference coordinate has distance greater than \(.05\) from
the boundary of \(P\). If
\[
                              Cq^d<\frac1{20},              \tag{16}
\]
then each \(x_j^*\) with \(j\in J_d\) is strictly inside \(P\).
Its individual gradient coordinate is zero. The displacement in (14)
is supported precisely on these coordinates, so the linear Taylor
term vanishes and
\[
 0\le E_n(\widetilde x^{(d)};u,v)-V_n(u,v)
                         \le20C^2q^{2d}.                    \tag{17}
\]
The other coordinates may remain constrained; no global interiority
of the minimizer is required.

Let \(V_{n,d}(u,v)\) denote the minimum with every coordinate in
\(J_d\) pinned to its reference value. Since
\(\widetilde x^{(d)}\) is feasible for this problem,
\[
                0\le V_{n,d}(u,v)-V_n(u,v)\le\varepsilon_d,
                                                               \tag{18}
\]
with the stronger right side from (17) under (16). This is also the
loss of the maximal original phase when that middle is pinned, because
the affine difference between (1) and minus (2) is independent of the
interior variables.

If \(n\ge2d+1\), at least one reference vertex is pinned. The
nearest-neighbor energy then separates exactly:
\[
 V_{n,d}(u,v)=L_d(u)+R_{n,d}(v),                              \tag{19}
\]
where \(L_d\) minimizes the original edges \(1,\ldots,d+1\)
over vertices \(1,\ldots,d\), with boundary values \(u,a_{d+1}\),
and \(R_{n,d}\) minimizes edges \(n-d+1,\ldots,n+1\) over
vertices \(n-d+1,\ldots,n\), with boundary values
\(a_{n-d},v\). All intervening reference/reference edge energies
are exactly zero. When there is just one pinned vertex, the two
windows share that fixed vertex and no edge. If \(n\le2d\), the
original problem already has at most \(2d\) free coordinates.

Thus, for any prescribed positive action tolerance, the same finite
window depth works for every chain length, every periodic type word,
and every allowed endpoint pair. One may use \(C=9/5\) in
(15)--(17) to make this assertion uniform in the endpoints as well.
The constants are expressed in terms of the proved local curvature
reserve; any stronger established value of \(\lambda\) can be
substituted in the same proof.

There is a second action estimate requiring no inactivity threshold.
Use the projected step \(1/\Lambda\) and put
\(q_0=1-\mu/\Lambda=99/100\). Its quadratic model is minimized over
\(P^n\) by the projected step. Compare that model with the feasible
point \(x+(\mu/\Lambda)(x^*-x)\). Strong convexity and smoothness
give, exactly,
\[
 E_n(T_0x)-V_n\le q_0(E_n(x)-V_n),\qquad
 E_n(a)-V_n\le\frac{G^2}{2\mu}.                            \tag{19a}
\]
For the first inequality the squared-distance coefficient is
\(\tfrac12[\Lambda(\mu/\Lambda)^2-
\mu(\mu/\Lambda)]=0\). For the second, minimize the strong-convexity
lower quadratic at \(a\) over the full real space; enlarging the
feasible set only decreases that lower bound. Starting this local
iteration at \(a\), its \(d\)-th iterate is feasible for the
pinned-middle problem. Hence
\[
              0\le V_{n,d}-V_n\le\frac{G^2}{2\mu}q_0^d.
                                                               \tag{19b}
\]
This controls the optimized windows, rather than the literal candidate
\(\widetilde x^{(d)}\). It is valid with every active set.

**Explicit universal depths.** Exact rational arithmetic gives
\[
 \frac95\left(\frac{99}{101}\right)^{295}<\frac1{20},\qquad
 \frac{324}{5}\left(\frac{99}{101}\right)^{590}<\frac1{2000},
 \qquad
 \frac{324}{5}\left(\frac{99}{101}\right)^{630}<\frac1{4000}.
                                                               \tag{19c}
\]
Thus depth 295 gives action error less than \(1/2000\), and depth
315 gives error less than \(1/4000\), uniformly in length and all
endpoint choices. These require at most 590 or 630 free boundary-window
coordinates in total. A shorter chain is simply retained in full.
Equation (19c) is checked exactly by the focused script below; it is
not a sampled statement about finitely many chain lengths.

## 5. A direct bound on interaction between the two ends

The same method also compares different boundary values. If only the
left endpoint changes from \(\bar u\) to \(u\), with the right
endpoint fixed, the difference of the two gradients at the old
minimizer is supported only at coordinate 1 and has norm at most
\(20|u-\bar u|\). Apply the two variational inequalities and
strong monotonicity to obtain total minimizer distance at most
\((20/\mu)|u-\bar u|\). Iterating the new projected map from the old
minimizer propagates this change only from the left. Consequently
\[
\begin{split}
 |x_j^*(u,v)-x_j^*(\bar u,v)|
                       &\le\frac{20}{\mu}|u-\bar u|q^{j-1},\\
 |x_j^*(u,v)-x_j^*(u,\bar v)|
                       &\le\frac{20}{\mu}|v-\bar v|q^{n-j}. \tag{20}
\end{split}
\]
This includes active constraints. For example, comparison first with
\(x^*(a_0,v)\) and then with \(a\) gives the two-tail
version of (12), with right side
\((20/\mu)[|u-a_0|q^{j-1}+|v-a_{n+1}|q^{n-j}]\).

Uniqueness and continuous dependence of the minimizer give the usual
envelope derivative without differentiating that minimizer:
\[
 \partial_v V_n(u,v)=\partial_2e_{n+1}(x_n^*(u,v),v).         \tag{21}
\]
This follows directly by using each minimizing vector as a competitor
at a nearby endpoint and taking the two resulting difference quotients.
The derivatives extend continuously to one-sided derivatives at the
ends of \(P\). The cross derivative of the last edge is bounded by
20. Combining (20)--(21), then integrating from \(a_{n+1}\) to
\(v\), proves
\[
\begin{split}
 \big|V_n(u,v)-V_n(u,a_{n+1})-V_n(a_0,v)
                              +V_n(a_0,a_{n+1})\big|\\
 \hspace{15mm}\le1000\,
       |u-a_0|\,|v-a_{n+1}|\,q^{n-1}.                      \tag{22}
\end{split}
\]
The last reference value is zero. The analogous mixed finite difference
of the maximal original phase obeys the same absolute bound, because
its extra bulk and endpoint-affine terms cancel from that difference.
Equation (22) remains valid at changes of the active set; it needs no
derivative of \(x^*\).

## 6. Scope

All assertions concern optimization of the original real part of the
phase at fixed actual unselected plateau heights. They do not compare
original finite kernels pointwise, change a contour, or prove an
open-chain asymptotic or a nonzero coefficient. Selected heights,
partially reset heights, and real coordinates outside \(P\) are
outside this deduction. A chain with no interior coordinate is just
its one original block and requires no forgetting argument.

Only the two already proved Hessian inputs supply numerical constants.
Projection, convexity, finite propagation and the action comparisons
are exact analytic arguments. In particular, no test of finitely many
chain lengths substitutes for the uniform statements above.

```sh
python3 experiments/check_mixed_plateau_boundary_forgetting.py
```

This focused check binds the completed curvature and reference-domain
inputs, checks their current provenance, and verifies the displayed
rational constants. It performs no new Hessian cover and does not
claim to verify the arbitrary-length proof by finite enumeration.
