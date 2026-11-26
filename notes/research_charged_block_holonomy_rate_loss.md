# A quantitative phase loss for the original charged block source

Private written proof, 14 November 2026. No computation, import, test or
manuscript change is used.

The exact bridge reduction of the original signed braid gives root
intervals with positive sine-binomial magnitudes and a specified phase
on each block. Here their phase loss is bounded explicitly, at every
block length and every positive radius. The resulting coefficient
estimate retains the original shared charges, all clock factors and the
closing pivots. It improves the positive radial upper bound by a
weighted graph phase energy.

The positive radial bound has a precise constrained tetrahedral-volume
dual. Neither that dual nor the phase loss is identified here with the
hyperbolic volume of the original partially filled tangle. No lower
bound for its coherent clock sum is asserted.

## 1. The exact block and a uniform angular estimate

Put \(q=e^{\pi i/N}\), \(Q=q^2\), \(N\ge2\). For \(0\le L<N\), set
\[
 c_{L,j}=\left|{L\brack j}_Q\right|,\qquad
 B_{L,N}(t)=\sum_{j=0}^L c_{L,j}t^j
          =\prod_{r=0}^{L-1}(1+q^{2r-L+1}t).
 \tag{1}
\]
All the coefficients are positive, and \(c_{L,j}=c_{L,L-j}\).
The last equality is the finite Gaussian binomial identity: the
phase \(q^{j(L-j)}\) of \({L\brack j}_Q\) cancels the phase
\(q^{j(j-L)}\) from expanding the product. Empty products are one.

For \(0\le\lambda\le1\), \(\rho>0\), define
\[
 \begin{split}
 I_{\lambda,\rho}(\theta)
   &=\frac1{2\pi}\int_{-\pi\lambda}^{\pi\lambda}
                \log|1+\rho e^{i(\theta+x)}|\,dx,\\
 k(\lambda,\rho)&=\frac{\rho\sin(\pi\lambda)}
                         {\pi(1+\rho)^2}.
 \end{split}
 \tag{2}
\]
The logarithmic singularities in this ordinary integral are integrable.

**Theorem 1.** There is an absolute constant \(C\ge1\) such that,
for every \(N,L,\rho,\theta\) as above,
\[
 |B_{L,N}(\rho e^{i\theta})|
 \le C N^C B_{L,N}(\rho)
       \exp\{-N k(L/N,\rho)(1-\cos\theta)\}.
 \tag{3}
\]
The elementary bound \(|B_{L,N}(\rho e^{i\theta})|\le B_{L,N}(\rho)\)
also holds. No interval of lengths, positive-radius compactum, or
avoidance of the zeros on the left of (3) is required.

We first prove the exact integral inequality
\[
 I_{\lambda,\rho}(0)-I_{\lambda,\rho}(\theta)
                  \ge k(\lambda,\rho)(1-\cos\theta).
 \tag{4}
\]
By evenness and periodicity it suffices to take \(0\le\theta\le\pi\).
Put \(a=\pi\lambda\) and \(f_\rho(x)=\log|1+\rho e^{ix}|\).
The arc integral is absolutely continuous in its center. Almost
everywhere,
\[
 -I'_{\lambda,\rho}(\theta)
 =\frac1{4\pi}\log\frac{1+\rho^2+2\rho\cos(\theta-a)}
                             {1+\rho^2+2\rho\cos(\theta+a)}.
 \tag{5}
\]
The numerator \(A\) is at least the denominator \(B\), because
\(A-B=4\rho\sin a\sin\theta\). Using
\(\log(A/B)\ge(A-B)/A\) and \(A\le(1+\rho)^2\) proves
\(-I'(\theta)\ge k(\lambda,\rho)\sin\theta\).
Integration gives (4). Isolated zeros are handled by the integrable
limit. The endpoint lengths have \(k=0\) and obey the same assertion.

Here is a uniform sum-to-integral estimate which retains those zeros:
\[
 \begin{split}
 \log|B_{L,N}(\rho e^{i\theta})|
       &\le N I_{L/N,\rho}(\theta)+C_1\log(N+1),\\
 \left|\log B_{L,N}(\rho)-N I_{L/N,\rho}(0)\right|
       &\le C_1\log(N+1).
 \end{split}
 \tag{6}
\]
The first line is automatic if the polynomial vanishes. Palindromicity
reduces both assertions to \(0<\rho\le1\), since replacing \(\rho\)
by \(\rho^{-1}\) adds \(L\log\rho\) to both the discrete and integral
expressions.

For \(0<\rho\le1/2\), \(f_\rho\) is uniformly bounded and has uniformly
bounded variation. For \(1/2\le\rho\le1\), put
\(t=|x-\pi|_{\mathbb T}\in[0,\pi]\). Then
\[
 |1+\rho e^{ix}|^2
   =(1-\rho)^2+4\rho\sin^2(t/2)
   \ge 2t^2/\pi^2.
 \tag{7}
\]
Clip \(f_\rho\) below at \(-M\), where \(M=\log N+2\).
The clipped periodic function has total variation \(O(M+1)\),
uniformly in \(\rho\): on each half-period it is monotone before
clipping, and its maximum is at most \(\log2\). Equation (7) gives
\[
 \int_0^{2\pi}(\max(f_\rho,-M)-f_\rho)\,dx
                         \le C_2 e^{-M}.
 \tag{8}
\]
Indeed clipping occurs only where \(t\le C_3e^{-M}\), and there
its excess is bounded by \(\log(C_3e^{-M}/t)\), whose integral on
\([0,C_3e^{-M}]\) is \(C_3e^{-M}\).

The points \((2r-L+1)\pi/N\) in (1) are the midpoints of \(L\)
intervals of length \(2\pi/N\) filling
\([-\pi L/N,\pi L/N]\). For a function of bounded variation, the
error between this midpoint sum and \(N/(2\pi)\) times its integral
is bounded by its total variation on the arc. Apply this to the
clipped function, then use (8). This proves the first line of (6)
with \(O(\log N)+O(Ne^{-M})=O(\log(N+1))\).

For the centered arc in the second line, every point is at circular
distance at least \(\pi/N\) from \(\pi\), since \(L\le N-1\).
Equation (7) makes clipping inactive throughout that arc; the
case \(\rho\le1/2\) is already bounded. The same variation estimate
proves the second line of (6). The empty arc is immediate.
Combining (4) and (6) proves (3).

## 2. The actual shared coefficient and its graph phase energy

Consider a fixed finite directed multigraph, including parallel edges
and loops, and the ordinary polynomial
\[
 P_N(X)=\Gamma_N\prod_{e:u\to v}
                 X_u^{L_e}B_{L_e,N}(w_eX_v/X_u),
 \qquad |w_e|=1,\quad 0\le L_e<N.
 \tag{9}
\]
The Laurent notation represents an ordinary polynomial. Let \(a_i\)
be prescribed nonnegative integral coefficient charges, with
\(\sum_i a_i=\sum_e L_e\). Retain \(\Gamma_N\) exactly. Its vanishing
makes all subsequent bounds trivial.

Write \(w_e=e^{i\omega_e}\). With one positive radius \(r_i\) at
each original vertex, put
\[
 \begin{split}
 {\cal C}_N(r)
   &=|\Gamma_N|\frac{\prod_e r_u^{L_e}
                         B_{L_e,N}(r_v/r_u)}
                        {\prod_i r_i^{a_i}},\\
 {\cal E}_N(r,w)
   &=\min_{\vartheta\in\mathbb T^{V}}
       \sum_{e:u\to v}k(L_e/N,r_v/r_u)
          \{1-\cos(\omega_e+\vartheta_v-\vartheta_u)\}.
 \end{split}
 \tag{10}
\]
The minimum exists. There is one radius per shared vertex, not
separate radii for its different incidences. The full arc loss
gives the stronger energy
\[
 \begin{split}
 D_{\lambda,\rho}(\theta)
   &=I_{\lambda,\rho}(0)-I_{\lambda,\rho}(\theta),\\
 {\cal E}^{\rm arc}_N(r,w)
   &=\min_{\vartheta\in\mathbb T^V}
       \sum_{e:u\to v}
       D_{L_e/N,r_v/r_u}(\omega_e+\vartheta_v-\vartheta_u)
       \ \ge {\cal E}_N(r,w).
 \end{split}
 \tag{10a}
\]
The inequality is (4). The integral profiles are continuous in
their center, including across their integrable logarithmic zeros,
so this minimum also exists.

**Theorem 2.** If there are \(b\) blocks in (9), then
\[
 \boxed{\displaystyle
 |[X^a]P_N|
 \le C^bN^{Cb}\inf_{r_i>0}
       \{{\cal C}_N(r)e^{-N{\cal E}^{\rm arc}_N(r,w)}\}.}
 \tag{11}
\]
This bounds the specified coefficient itself.

Take its original Cauchy integral on \(X_i=r_ie^{i\vartheta_i}\).
Subtract the two estimates in (6) to bound each block by its
positive value times \(\exp(-ND_{\lambda,\rho}(\theta))\), at
polynomial cost, with the literal relative angle
\(\theta=\omega_e+\vartheta_v-\vartheta_u\). Multiplication and
the minimum in (10a) give the bound at that radius. Normalized
Haar integration adds no factor. The constant is independent of
every radius, so infimizing proves (11). No block value is divided
out. Replacing \({\cal E}^{\rm arc}_N\) by \({\cal E}_N\) gives
the explicit weaker bound using only (3).

For a simple cycle \(C\) with no repeated edges, orient its
traversal and let
\[
 \delta_C=\left|\arg\prod_{e\in C}w_e^{\epsilon_e}
                                      \right|_{\mathbb T}\in[0,\pi].
 \tag{12}
\]
If \(k_e=k(L_e/N,r_v/r_u)>0\) on this cycle, then
\[
 {\cal E}_N(r,w)\ge
          \frac{2\delta_C^2}{\pi^2\sum_{e\in C}k_e^{-1}}.
 \tag{13}
\]
Vertex angles telescope, so the sum of the circular distances of
its edge angles is at least \(\delta_C\). Now use
\(1-\cos t\ge2|t|_{\mathbb T}^2/\pi^2\) and weighted Cauchy.
A loop is included as a one-edge cycle. Collections of cycles may
be combined by the existing fractional cycle-packing argument.

The energy is zero exactly when the connection is flat on the
subgraph with positive \(k_e\), by spanning-tree propagation of
vertex phases and the nonnegative summands in (10). This
characterization is not needed for (11). If lengths approach zero
or one, or radius ratios escape, the bound still holds; its explicit
\(k_e\)'s may tend to zero, so a uniform exponential loss is not inferred.

## 3. Source normalization and the coherent clock sum

The original-source identity in
[the charged bridge-flow theorem](actual_global_charged_bridge_flow.md),
equations (12), (17)--(19), is
\[
 K_N=\frac{\chi_N}{N}
       \sum_{h\ {\rm over\text{-}monotone}}
       W_h[X_1^{N-1}\cdots X_s^{N-1}]P_h(X).
 \tag{14}
\]
It retains integer-weight conservation, all original closure
adapters and pivots, and the homogeneous alias cancellation. Each
fixed-clock block is exactly
\[
 \prod_{\ell=0}^{L-1}(\alpha X_u-Q^\ell\beta X_v)
  =\alpha^L X_u^L
       B_{L,N}\bigl(-(\beta/\alpha)q^{L-1}X_v/X_u\bigr).
 \tag{15}
\]
The actual propagated root phases have modulus one. Thus (9) is
literally the fixed-clock polynomial in (14), with the extracted
\(\alpha^L\)'s retained in \(\Gamma_h\). Its \(w_e\)'s are the
source theorem's equation (18), including the unpivoted cut and
every pivotal closing block. They are not selected by optimizing
(10). Every \(W_h\), including its sine-factorial magnitudes and
Gaussian phases, remains.

If \(b\) bounds the number of blocks of the fixed word, (11) yields
\[
 |K_N|\le\frac{|\chi_N|}{N}C^bN^{Cb}
   \sum_h |W_h|\inf_r
       \{{\cal C}_{h,N}(r)e^{-N{\cal E}^{\rm arc}_{h,N}(r,w_h)}\}.
 \tag{16}
\]
The number of clocks is polynomial in \(N\) for a fixed word.
No zero-feedback fiber, omitted closing character, or arbitrary
observation replaces (14). Formula (11) applies also to another
prescribed coefficient of an actual charged polynomial. Its use
for an open matrix element requires that element's actual boundary
coefficient adapter; (14) alone is not such an adapter.

## 4. The constrained tetrahedral entropy of the positive bound

This identifies the positive optimization, not the knot geometry.
Put
\[
 J(x)=\int_0^x\log(2\sin\pi t)\,dt,\qquad
 v_\lambda(x)=J(\lambda)-J(x)-J(\lambda-x).
 \tag{17}
\]
For \(0\le x\le\lambda\le1\), reflection gives
\[
 v_\lambda(x)=\frac1\pi
   \{\Lambda(\pi x)+\Lambda(\pi(\lambda-x))
                             +\Lambda(\pi(1-\lambda))\},
 \tag{18}
\]
where \(\Lambda(a)=-\int_0^a\log|2\sin t|\,dt\).
The three arguments are the angles of a possibly degenerate ideal
tetrahedron. The endpoint-aware sine-product estimate gives
\[
 \log c_{L,j}=N v_{L/N}(j/N)+O(\log(N+1))
                    \quad(0\le j\le L<N).
 \tag{19}
\]
For clarity, the uniform sine-product estimate used here follows
by subtracting the endpoint logarithms from \(\log(2\sin\pi t)\).
The remainder is smooth on the closed interval; ordinary integral
comparison for the increasing sequence \(\log j\), at either
endpoint, gives error \(O(\log(N+1))\). Applying it to the three
factorials in \(c_{L,j}\) proves (19).

For \(0<\lambda<1\),
\[
 v_\lambda''(x)=
 -\frac{\pi\sin(\pi\lambda)}
          {\sin(\pi x)\sin(\pi(\lambda-x))}<0,
                  \qquad 0<x<\lambda.
 \tag{20}
\]
Its endpoint derivatives are \(+\infty\) and \(-\infty\).
For real \(y\), the unique maximum of \(v_\lambda(x)+yx\)
is therefore interior and satisfies
\[
             e^y\sin(\pi(\lambda-x))=\sin(\pi x).
 \tag{21}
\]
The largest-term estimate in (1), its at most \(N\) positive terms,
and (19), together with (6) at phase zero, prove
\[
 I_{\lambda,e^y}(0)
       =\max_{0\le x\le\lambda}\{v_\lambda(x)+yx\}.
 \tag{22}
\]
The endpoint lengths follow by continuity.

Fix limiting lengths \(\lambda_e\) and limiting charges \(a_i^0\).
Their literal coefficient-flow equations are
\[
 \sum_{e:v\to i}x_e-\sum_{e:i\to v}x_e
       =a_i^0-\sum_{e:i\to v}\lambda_e,\qquad
                           0\le x_e\le\lambda_e.
 \tag{23}
\]
Suppose this polytope has a point strict in every coordinate and
all \(0<\lambda_e<1\). Then \(\sum_e v_{\lambda_e}(x_e)\) has a
unique interior maximizer. Strict concavity gives uniqueness.
Moving a boundary point toward the strict feasible point has
positive infinite derivative from every opened endpoint, so a
boundary point cannot maximize. Lagrange multipliers for the
affine equations supply vertex log-radii \(\rho_i\) with (21)
and \(y_e=\rho_v-\rho_u\). Substitution into (22) gives
\[
 \begin{split}
 \max_{\text{(23)}}\sum_e v_{\lambda_e}(x_e)
 =\inf_{\rho\in\mathbb R^V}
 \left\{\sum_{e:u\to v}
   [\lambda_e\rho_u+I_{\lambda_e,e^{\rho_v-\rho_u}}(0)]
                                -\sum_i a_i^0\rho_i\right\}.
 \end{split}
 \tag{24}
\]
Conversely, (22) bounds any feasible flow by the expression in
braces, since (23) cancels its radius terms. This proves both
directions without assuming an interchange of extrema.

At finite \(N\), write \(P_N^+\) for (9) with \(\Gamma_N\) replaced
by its modulus and all \(w_e\) replaced by one. The existing
[flat-block coefficient theorem](actual_flat_block_sublevel_transport.md)
gives, under its strict-Hall hypotheses,
\[
 \frac{\operatorname{Cap}(P_N^+)}{\prod_e(L_e+1)}
       \le [X^a]P_N^+\le\operatorname{Cap}(P_N^+).
 \tag{25}
\]
The scalar magnitude is included on both sides. At a minimizing
radius \(r_*\), (11) and (25) imply
\[
 |[X^a]P_N|\le
 C^bN^{Cb}\prod_e(L_e+1)\,[X^a]P_N^+
                         e^{-N{\cal E}^{\rm arc}_N(r_*,w)}.
 \tag{26}
\]
This is an upper comparison, not a positive lower bound for the
original coefficient.

## 5. Contribution and remaining geometric comparison

The earlier
[cycle-packing theorem](research_regular_window_cycle_packing.md)
already turns supplied local losses into a shared coefficient bound.
The additions here are the explicit loss for the actual
sine-binomial blocks, uniformity through all allowed lengths and
all positive radii with polynomial cost, and (11) for the original
charged bridge source. No asymptotic replacement of a crossing or
deletion of an endpoint is used to obtain the phase loss.

Equations (18), (23), (24) connect the bound to a concave
tetrahedral entropy problem. In (14), however, the lengths and
block phases depend on the remaining clocks. Their Gaussian
feedback and \(W_h\) remain part of the source. The coefficient
flow equations have not been proved to give all marked geometric
gluing and peripheral equations for arbitrary short Conway pieces.
The maximum in (24) must not be called their hyperbolic volume.

At specified geometric radii, (11) supplies the positive radial
envelope minus the full arc-loss energy, bounded below by the
explicit graph cosine energy. Proving a strict
gap below the geometric action on a whole complementary family
still requires that numerical-free analytic comparison. Nontrivial
holonomy alone, or positive energy alone, does not supply it.
Compatible sectors and cancellation among original clock phases
remain. No general partial-filling volume theorem is claimed.

## Direct source versions

The written proof was checked against these source versions:

| Source | SHA-256 |
| --- | --- |
| actual_global_charged_bridge_flow.md | b444e487eab3ec0a56c40b22584837cefcbe374a137b0beeaa185116c2a81d8c |
| anchor_phase_cycles_and_exact_fusion.md | 37cdfb5125a27671069581e631b73f98c67e7ca944f38e37fe151a37f729a571 |
| actual_flat_block_sublevel_transport.md | 182d1f125cb927b709556095c8cc888f0b459713b2943013c08eb99033c70a5b |
| research_regular_window_cycle_packing.md | b0e36ecff57053bb660d542387ad903d36a6c39a52c142555d2e5dfc1b05d3ea |
