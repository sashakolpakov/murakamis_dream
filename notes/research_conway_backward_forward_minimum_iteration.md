# Backward source transport and one forward pass solve the Conway minimum

23 November 2026. Written research proof.

The original normalized quartic admits a contracting iteration consisting
of one backward source pass and one forced forward pass. Its contraction
factor is at most \(15/2744\), independently of the quantum level and the
size of the literal tree. After exact elimination of the closing turn
corridor, the factor is at most \(5\zeta^2/C\), with the original,
explicit endpoint coefficient \(\zeta\) and corridor factor \(C\).
Thus that second factor decreases exponentially with the level.

This is an iteration for the same minimum, not an evaluation of its
geometric rate. Starting at zero makes its first forward pass the actual
open-source evaluation. Full boundary packets, all their Hermite
directions, the original closing, and every normalization budget remain.

## 1. The exact normalized source

Fix \(N\ge2\). Use the literal normalized Conway tree of [C], with
one packet in the complete Newton space \(H_N\cong\mathbb C^N\)
at each proper vertex. Put
\[
 \sigma=1/16,\qquad
 \mathcal X=\bigoplus_v H_N,\qquad
 \mathcal D=\prod_v\{x_v:\|x_v\|\le1\}.
 \tag{1}
\]
Each normalized leaf, turn, and bilinear product \(\Phi_v\) has
norm at most \(\sigma\). The original closing row is \(c\),
supported at the top packet, with \(\|c\|\le\sigma\). Let
\[
 G(x)=\Phi(x)-x,\quad A_x=D\Phi(x),\quad S_x=I-A_x,
 \qquad E(x)=\|G(x)\|^2+|cx|^2.
 \tag{2}
\]
The positive budget \(B_{\rm tot}\), all original phases, and the
marking are exactly those in [C]. If \(e_* =\min_{\mathcal D}E\),
then
\[
 B_{\rm tot}^2e_*\le |K_N|^2
 \le\frac{197}{196}B_{\rm tot}^2e_*.
 \tag{3}
\]
The unique minimizer is interior, and \(I\le D^2E\le3I\).
All gradients are real gradients for \(\operatorname{Re}(u^*v)\);
the local maps themselves are complex multilinear.

We also use the following direct consequences of the literal tree:
\[
 \|A_x\|\le1/8,\quad \|S_x^{-1}\|\le\rho:=8/7,
 \qquad \|A_x-A_y\|\le\sigma\|x-y\|.
 \tag{4}
\]
The norm is the Hilbert direct-sum norm. For the last assertion, only
products have a second derivative. At one product it is
\(\Phi_v(h_L,k_R)+\Phi_v(k_L,h_R)\). The two child slots of distinct
products are disjoint. Cauchy--Schwarz first on a sibling pair and then
over those pairs gives
\(\|D^2\Phi(x)[h,k]\|\le\sigma\|h\|\|k\|\).
Integration along the feasible segment proves (4). Its first two bounds
are also proved in [C].

## 2. Exact inversion of the residual by a forward pass

Given a forcing \(r=(r_v)_v\), define \(Y(r)\) from leaves to root by
\[
                  Y(r)_v=\Phi_v((Y(r)_j)_{j\text{ child of }v})-r_v.
 \tag{5}
\]
This finite recursion is the unique solution of \(G(Y(r))=r\).
It contains no solve for a simultaneous nonlinear system. If
\(\|r\|\le\varepsilon\) and \(\sigma+\varepsilon\le1\),
induction from the leaves gives
\[
                     \|Y(r)_v\|\le\sigma+\varepsilon.
 \tag{6}
\]
In particular these fields are feasible. For any two forcings whose
fields are feasible, (4), integrated between the fields, gives
\[
                     \|Y(r)-Y(s)\|\le\rho\|r-s\|.
 \tag{7}
\]
Indeed \(G(u)-G(v)=-(u-v)+\int_0^1A_{v+t(u-v)}(u-v)\,dt\),
whose norm is at least \(7\|u-v\|/8\). Feasibility in this argument
comes from (6), before the Lipschitz estimate is used.

For a known complex-linear row \(b_x\), the row
\(d_x=b_xS_x^{-1}\) is computed in one backward pass. Its blocks obey
\[
 (d_x)_v=(b_x)_v+
 (d_x)_{\operatorname{parent}(v)}
                  D_v\Phi_{\operatorname{parent}(v)}(x),
 \tag{8}
\]
with the second term absent at a top vertex. This is the finite
triangular identity \(d_x=b_x+d_xA_x\), not a dense inverse.

## 3. The original quartic: contraction by \(15/2744\)

Set
\[
 d_x=cS_x^{-1},\qquad r_x=d_x^*(cx),\qquad
                         \mathcal T(x)=Y(r_x).
 \tag{9}
\]
Everything on the right is known from the trial packets and original
source tensors. Neither \(K_N\) nor the true field is an input.
From (4) and the resolvent identity,
\[
 \|d_x\|\le1/14,\qquad
 \|d_x-d_y\|\le\sigma^2\rho^2\|x-y\|
                         =\frac1{196}\|x-y\|.
 \tag{10}
\]
Since \(|cx|\le\sigma\) on \(\mathcal D\),
\[
 \|r_x\|\le1/224,\qquad
 \|r_x-r_y\|\le
 \left(\frac1{14}\frac1{16}+\frac1{196}\frac1{16}\right)
 \|x-y\|=\frac{15}{3136}\|x-y\|.
 \tag{11}
\]
Equations (6)--(7) now prove
\[
 \boxed{\quad
 \mathcal T(\mathcal D)\subset(15/224)\mathcal D,
 \qquad \operatorname{Lip}(\mathcal T)\le15/2744<1/180.
 \quad}
 \tag{12}
\]
The fixed point is exactly the original quartic minimizer. In fact
\[
 \tfrac12\nabla E(x)=-S_x^*G(x)+c^*cx=0
 \quad\Longleftrightarrow\quad G(x)=d_x^*cx
 \quad\Longleftrightarrow\quad x=\mathcal T(x).
 \tag{13}
\]
The last equivalence uses uniqueness of the causal recursion (5).
Contraction produces a unique feasible fixed point; its image bound
makes it interior. Stationarity and [C]'s convexity identify it with
the same minimum appearing in (3).

For the scalar dual problem of [S], fix \(|\lambda|\le\sigma\) and put
\[
 \mathcal T_\lambda(x)=Y(d_x^*\lambda),\qquad
 J_\lambda(x)=\|G(x)\|^2+2\operatorname{Re}(\bar\lambda cx).
 \tag{14}
\]
The same forcing bound applies, while the variation of \(cx\) is now
absent. Therefore
\[
 \mathcal T_\lambda(\mathcal D)\subset(15/224)\mathcal D,
 \qquad \operatorname{Lip}(\mathcal T_\lambda)\le1/2744.
 \tag{15}
\]
Its fixed point solves \(-S_x^*G(x)+c^*\lambda=0\), and hence is
the unique inner minimizer in [S]. This supplies a faster certified
field iteration for that already established scalar response.

## 4. The exactly eliminated closing corridor

Suppose the literal tree has a highest binary product. Eliminate only
its output and the turns above it exactly as in [F]. The remaining
variables are all packets strictly below that product, including its
two input packets. Their residual still has the form \(G=\Phi-x\),
on a forest, with the same bounds (4). The reduced objective is exactly
\[
 F(x)=\|G(x)\|^2+|g(x)|^2,
 \qquad g(x)=x_L^{\mathsf t}B x_R/\sqrt C,
 \qquad \|B\|=\zeta,\quad t:=\zeta/\sqrt C.
 \tag{16}
\]
Here \(C=1+\nu_{\rm corr}\) is the explicit inclusive corridor
factor of [F]. In the original notation,
\(B=(\eta/b_*)J\) or \((\eta/b_*)e_0e_0^{\mathsf t}\),
according to the original closing, and
\(\eta=\chi/(b_{\rm root}\prod_i\beta_i)\).
All corridor budgets, the physical scalar \(\chi\), and the product
budget \(b_*\) remain in \(\zeta=|\eta|/b_*\).
In particular \(C\ge1\), \(\zeta\le1/256\), and [F] proves
that the minimum in (16) is the original full minimum \(e_*\).

On the feasible balls,
\[
 |g|\le t,\qquad \|Dg\|\le\sqrt2t,
                       \|D^2g\|\le t.
 \tag{17}
\]
Define now
\[
 d_x=Dg(x)S_x^{-1},\qquad r_x=d_x^*g(x),\qquad
                         \mathcal T_F(x)=Y(r_x).
 \tag{18}
\]
The backward pass (8) starts with the known row \(Dg(x)\), supported
at the two input packets. The scalar \(g(x)\) is also a known trial
contraction. The resolvent identity and (17) give
\[
 \|d_x\|\le\rho\sqrt2t,\qquad
 \operatorname{Lip}(d)\le t(\rho+\rho^2\sqrt2\sigma).
 \tag{19}
\]
Consequently
\[
 \|r_x\|\le\rho\sqrt2t^2\le2t^2,\qquad
 \operatorname{Lip}(r)\le t^2(3\rho+\rho^2\sqrt2\sigma).
 \tag{20}
\]
First (6) proves feasibility; then (7) proves
\[
 \boxed{\quad
 \mathcal T_F(\mathcal D)\subset(\sigma+2t^2)\mathcal D,
 \qquad \operatorname{Lip}(\mathcal T_F)
 \le\left(\frac{192}{49}+\frac{32\sqrt2}{343}\right)t^2
 \le5\zeta^2/C\le5/65536<1/13000.
 \quad}
 \tag{21}
\]
As in (13), its fixed points are exactly stationary points of (16).
The eliminated objective is strongly convex by [F], so the fixed point
is its unique minimum. The exact corridor formulas then recover all
eliminated packets, with their ball constraints inactive.

For a fixed literal tree with a product, [F] also gives
\[
 \zeta\le\exp\{-2G_{\rm Cat}N/\pi+O(\log N)\}.
 \tag{22}
\]
Thus the contraction bound in (21) is at most
\(\exp\{-4G_{\rm Cat}N/\pi+O(\log N)\}\).
This is a convergence bound, not a lower bound for the source.
If there is no product, [F]'s corridor elimination is already exact
with no remaining optimization. A zero closing is likewise harmless.

## 5. What the passes do and do not remove

Each iteration uses the actual local derivatives in one backward pass
and the actual local gates in one forward pass. Their number is linear
in the number of literal vertices. The packet dimension remains \(N\);
no bound independent of \(N\) is asserted for tensor arithmetic, storage,
bit complexity, or the precision needed to resolve a small scalar.
The causal compositions can have higher degree than four. The objective
being minimized, rather than this iteration map, is the original quartic.

For any of these contractions with factor \(q<1\),
\[
 \|x_j-x_*\|\le q^j\|x_0-x_*\|,
 \qquad
 \|x_j-x_*\|\le\frac{\|x_{j+1}-x_j\|}{1-q}.
 \tag{23}
\]
These are absolute field bounds. In particular they do not supply
relative precision for an exponentially small minimum or a nonzero
geometric coefficient. At \(x=0\), the frozen scalar forcing is zero
for both full objectives. Thus \(\mathcal T(0)=a\), and
\(\mathcal T_F(0)=a_{\rm below}\): the first forward pass is precisely
the true open recursion. No difficulty in the coherent closing is
removed by naming it a field iteration.

There are nevertheless direct value certificates. The eliminated
objective has \(D^2F\le3I\): in the Schur formula of [F], test the
eliminated variation by zero and use [C]'s upper Hessian bound.
Consequently, for \(q=5t^2\),
\[
 F(u)-\frac{3\|\mathcal T_F(u)-u\|^2}{2(1-q)^2}
                  \le e_*\le F(u).
 \tag{24}
\]
This follows from (23) and Taylor's theorem at the minimizer. Restoring
the original source uses (3), with its unchanged \(B_{\rm tot}^2\).

For a sharper comparison of minimum values, begin at the known forward
field \(u_0=a_{\rm below}=\mathcal T_F(0)\), and let
\(u_j=\mathcal T_F^j(u_0)\). The lower Hessian bound
\(m=41/32\), the upper bound \(3\), and [F]'s estimate
\(F(u_0)-e_*\le t^2F(u_0)/82\) give
\[
 0\le F(u_j)-e_*
 \le\frac{3}{m}q^{2j}(F(u_0)-e_*)
 \le\frac{48}{1681}t^2q^{2j}\frac{|k|^2}{C}.
 \tag{25}
\]
Indeed strong convexity bounds \(\|u_0-u_*\|^2\) by
\(2(F(u_0)-e_*)/m\), then (23) and the upper Hessian bound apply.
This includes zeros. Each extra pass pair therefore improves the
minimum approximation by two powers of \(q\). It does not improve the
previous comparison of \(CB_{\rm tot}^2e_*\) with \(|K_N|^2\):
\(F(u_0)=|k|^2/C\) already evaluates the same coherent source exactly.

## Complete sources and coverage

The complete proof inputs are [C] and [F], at the matching pins below.
[C] supplies the original normalized tensors, source comparison and
convexity; [F] supplies the exact original corridor elimination,
endpoint form, constants and exponential estimate (22). The two-pass
iteration and its contraction bounds are proved here.

| Label | Complete source | SHA256 |
|---|---|---|
| C | [Normalized quartic](research_convex_normalized_conway_source.md) | 6b89b4c6a67ef7a32cc41a5966c650f32de65d284ae7b70d94a71bddba21df3c |
| F | [Explicit corridor factor](research_conway_explicit_corridor_minimum_factor.md) | 85d482ef7121621447ea5ec2b158c9445d413add7495700964792d205a224938 |

The following complete comparison texts were also read at matching pins:

| Complete comparison | SHA256 |
|---|---|
| [S: scalar cap response](research_conway_scalar_cap_response.md) | 6b9b73ae429713bdff63120a9841c06d2311d249f058f3da6b1f4e89dbfaecfb |
| [Source normal and Gauss--Newton](research_conway_source_normal_gauss_newton_certificate.md) | 36cea2a5e40cc515e0034e91f41eeb23cb75f57d0f4750d5d341f2dcbd9081f3 |
| [Residual transport and finite repair](research_conway_source_visible_residual_transport.md) | 0d344301b0df65246551cf81498eff84582f796a03271b201f8fbba6c7742007 |
| [Compressed convex source](research_conway_compressed_convex_source.md) | 065989bd50a891d1e3a67ce7b556921a8050ac83f019b8ba27360a6386a2189c |
| [Internal-edge scalar response](research_conway_internal_edge_scalar_response.md) | a9f55feb64ed941faced7ecd1eb0baa4f1a4eb7f6b85aeeb7827113c945aa7a2 |

Those notes already provide scalar duality, the stationary identity,
finite residual repairs, and other contracting optimizations. The
Gauss--Newton occurrence of \(1/2744\) bounds one displacement; it is
not the contraction (15). The compressed objective is a different
reduction. No general novelty is asserted for alternating forward and
adjoint passes or for contraction methods. Only written mathematics
and text operations were used; no mathematical programs or tests ran.
