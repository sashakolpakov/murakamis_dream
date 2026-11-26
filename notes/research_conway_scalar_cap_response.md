# Separating the closing functional in the convex Conway energy

21 November 2026. The final closing functional in the normalized Conway
energy has complex rank one. This note separates it by an exact scalar
dual problem. The scalar response is a contraction, and its first
nonlinear correction has a bound independent of the quantum level and
the size of the expression tree. Keeping this rank-one term in the
quadratic minorant also improves the explicit lower certificate.

The internal minimization still retains all physical boundary packets.
None of the formulas below evaluates their geometric asymptotic rate.

## 1. The original closing row and the residual energy

Use the complete boundary spaces, fixed local budgets, and normalized
maps of the [convex Conway source](research_convex_normalized_conway_source.md).
Write the product of unit balls as \(\mathcal D\), the true normalized
field as \(a\), and the full residual map as \(G\). Put
\[
 R(x)=\|G(x)\|^2,\qquad cx=Lx_{v_0},\qquad
 E(x)=R(x)+|cx|^2,\qquad k=ca=K_N/B_{\rm tot}.
 \tag{1}
\]
Here \(v_0\) is the proper vertex immediately below the closing root,
and \(L\) is the original marked closing row divided by its recorded
local budget. The full scalar \(B_{\rm tot}\) is unchanged. In
particular, a framing phase or recorded power of \(N\) in the physical
closing row stays in (1).

Set \(\sigma=1/16\) and \(\ell=\|L\|\le\sigma\). The coefficient
norms are the Euclidean norms in the complete Newton basis. Repeated-root
derivatives and both original closing directions remain present. All
gradients and Hessians below are real, for the inner product
\(\operatorname{Re}\sum_vx_v^*y_v\). Thus a scalar complex coordinate
has two real coordinates. The complex-linear row \(c\) satisfies
\(cc^*=\ell^2I_2\) in these real coordinates.

We use the following estimates, proved in the complete source theorem:
\[
 G(a)=0,\quad \|a_v\|\le\sigma,\quad |k|\le\sigma^2,
 \qquad I\le D^2R\le3I,\qquad I\le D^2E\le3I
 \quad\hbox{on }\mathcal D.
 \tag{2}
\]
The stated estimate for \(R\) follows from that theorem's residual
Hessian proof before adding the nonnegative closing Hessian. If
\(e_* =\min_{\mathcal D}E\), the original source comparison is
\[
 B_{\rm tot}^2e_*\le |K_N|^2
       \le\gamma B_{\rm tot}^2e_*,\qquad \gamma=197/196.
 \tag{3}
\]

## 2. An exact scalar dual problem

For \(\lambda\in\mathbb C\), define
\[
 h(\lambda)=\min_{x\in\mathcal D}
       \{R(x)+2\operatorname{Re}(\bar\lambda cx)\},\qquad
 q(\lambda)=h(\lambda)-|\lambda|^2.
 \tag{4}
\]
This definition uses only the known local maps and the prescribed closing
row. It does not take \(K_N\) or the true field \(a\) as an input.

**Theorem 1.** The exact minimum is
\[
 \boxed{\quad e_* =\max_{\lambda\in\mathbb C}q(\lambda).
 \quad} \tag{5}
\]
The maximum is unique. It lies in \(|\lambda|\le\sigma\), where
the inner minimum has a unique interior minimizer \(x(\lambda)\).
Writing \(s(\lambda)=cx(\lambda)\), the maximizer is characterized by
\[
 \lambda_*=s(\lambda_*),\qquad
 \|Ds(\lambda)\|\le2\ell^2\le1/128.
 \tag{6}
\]
Thus the iteration \(\lambda_{j+1}=s(\lambda_j)\) converges to
\(\lambda_*\) from any point in this disk.

**Proof.** For any \(x,\lambda\),
\[
 |cx|^2-2\operatorname{Re}(\bar\lambda cx)+|\lambda|^2
                                      =|cx-\lambda|^2\ge0.
\]
Consequently \(q(\lambda)\le e_*\). Let \(x_*\) be the unique
interior minimizer of \(E\), whose existence and stationarity were
proved in the source theorem. Put \(\lambda_*=cx_*\), so
\(|\lambda_*|\le\ell\le\sigma\). The stationary equations give
\[
           \nabla R(x_*)+2c^*\lambda_*=0.
\]
Since the objective in the inner problem is strongly convex, this
equation makes \(x_*\) its unique minimum at \(\lambda_*\).
The displayed square vanishes there, proving (5).

For \(|\lambda|\le\sigma\), the inner half-gradient map has, at
a nontop vertex \(v\), the same component as the residual energy:
\[
 \Phi_v-(D_v\Phi_{\operatorname{parent}(v)})^*
                    \mathcal R_{\operatorname{parent}(v)}.
\]
Its norm is at most \(\sigma+\sigma(1+\sigma)=33/256\).
The top component is \(\Phi_{v_0}-L^*\lambda\), with norm at most
\(\sigma+\sigma^2=17/256\). The Hessian is \(D^2R\), so this
map is a contraction with factor \(1/2\). It maps \(\mathcal D\)
strictly inside itself. Its unique fixed point is the unique interior
inner minimum. The implicit function theorem therefore gives a smooth
real response \(x(\lambda)\) on a neighborhood of the closed disk.

Differentiating its stationary equation gives
\[
 Dx(\lambda)=-2H(\lambda)^{-1}c^*,\qquad
 Ds(\lambda)=-2cH(\lambda)^{-1}c^*,\qquad
 H(\lambda)=D^2R(x(\lambda)).
 \tag{7}
\]
Equation (2) implies (6). Also
\(|s(\lambda)|\le\sigma(\sigma+\sigma^2)<\sigma\), because
the top fixed-point equation has that same component bound.
The disk is therefore preserved by the scalar contraction.

The function \(h\) is concave on the whole scalar plane, being an
infimum of affine functions of \(\lambda\). Hence subtracting
\(|\lambda|^2\) makes \(q\) strictly concave, so its global maximum
is unique. On the disk,
\[
 \nabla q=2(s-\lambda),\qquad
 -(2+4\ell^2)I_2\le D^2q\le-2I_2.
 \tag{8}
\]
This proves the remaining assertions. \(\square\)

The reduction is scalar at the outside. Each evaluation of \(s\) still
solves a problem involving the actual internal packets. It has not
converted their coherent value into a known local norm.

## 3. Positive response and its first nonlinear correction

Since \(x(0)=a\), integrating (7) along the scalar segment gives
\[
 s(\lambda)=k-\mathsf B(\lambda)\lambda,\qquad
 \mathsf B(\lambda)=2\int_0^1
       cH(t\lambda)^{-1}c^*\,dt.
 \tag{9}
\]
This is a real \(2\times2\) response matrix, with
\[
 \tfrac23\ell^2I_2\le\mathsf B(\lambda)\le2\ell^2I_2.
 \tag{10}
\]
In particular \(k=(I_2+\mathsf B(\lambda_*))\lambda_*\).
The response correction is positive and close to the identity. It is
not asserted to be a complex-holomorphic scalar function.

There is a uniform expansion at the exact residual field. Set
\[
 T=DG(a),\qquad \nu=\|cT^{-1}\|^2\le1/196.
 \tag{11}
\]
The inverse exists because \(T=-I+A(a)\), with \(\|A(a)\|\le1/8\).
At \(\lambda=0\), \(H(0)=2T^*T\), so
\(\mathsf B(0)=\nu I_2\). This scalar form uses the fact that
\(T\) and \(c\) are complex-linear at the zero residual.

**Theorem 2.** With the normalizations above,
\[
 \left|e_*-\frac{|k|^2}{1+\nu}\right|
       \le\frac{|k|^3}{4096},\qquad
 \left|\lambda_*-\frac{k}{1+\nu}\right|
       \le\frac{|k|^2}{4096}.
 \tag{12}
\]
The constants are independent of \(N\), the expression tree, and its
fixed filling coefficients after the recorded budgets are retained.

**Proof.** The full residual is quadratic. For a displacement \(e\),
\[
 G(a+e)=Te+Q(e),\qquad
 \|Q(e)\|\le\tfrac\sigma2\|e\|^2,\qquad
 \|DQ(e)\|\le\sigma\|e\|.
 \tag{13}
\]
Indeed \(Q_v(e)=\Phi_v(e_L,e_R)\) at a product and is zero at
other vertices. Sibling pairs are disjoint. For two variations, the
second derivative has components
\(\Phi_v(u_L,v_R)+\Phi_v(v_L,u_R)\). Cauchy--Schwarz on each
sibling pair and then on their disjoint sum bounds its norm by
\(\sigma\|u\|\|v\|\), which proves (13).

The quadratic model is
\[
 E_0(e)=\|Te\|^2+|k+ce|^2.
\]
Putting \(d=cT^{-1}\) and minimizing first in \(Te\) gives
\[
 e_0=-T^{-1}d^*k/(1+\nu),\quad
 \min E_0=|k|^2/(1+\nu),\quad
                       k+ce_0=k/(1+\nu).
 \tag{14}
\]
Moreover \(\|e_0\|\le4|k|/49<|k|/8\).
Write \(u_*=x_*-a\) for the actual minimizing displacement.
Strong monotonicity of \(\nabla E\) gives
\[
 \|u_*\|\le\|\nabla E(a)\|
                  =2\|c^*k\|\le |k|/8.
 \tag{15}
\]
Both comparison points are feasible, since \(\|a_v\|\le1/16\)
and \(|k|\le1/256\).

For \(\|e\|\le1\), let \(W(e)=E(a+e)-E_0(e)\). From
\(\|T\|\le9/8\) and (13),
\[
 |W(e)|\le\tfrac18\|e\|^3,\qquad
 \|\nabla W(e)\|\le\tfrac14\|e\|^2.
 \tag{16}
\]
For clarity, the first coefficient is bounded by
\(\sigma\|T\|+\sigma^2/4=73/1024<1/8\).
The second is bounded by
\(3\sigma\|T\|+\sigma^2=55/256<1/4\).
Evaluating the two objectives at their respective minima, using
(15) and the bound for \(e_0\), proves the value bound in (12).

Finally \(D^2E_0\ge I\), and the actual stationary equation is
\(\nabla E_0(u_*)=-\nabla W(u_*)\). Hence
\[
 \|u_*-e_0\|\le\tfrac14\|u_*\|^2
                         \le |k|^2/256.
\]
Applying \(c\), whose norm is at most \(1/16\), and using (14)
proves the second bound. \(\square\)

The field \(a\) and the row in (11) can be obtained by the exact open
recursions and their backward linear response. They are not supplied by
hyperbolic gluing data in this argument. Thus (12) isolates the effect
of the final scalar closing inside the variational problem, while
leaving the geometric estimate for the actual source outstanding.

## 4. A stronger explicit lower certificate

The closing Hessian can also be kept exactly in the quadratic minorant.
For \(g=\nabla E(x)\), define
\[
 \boxed{\quad
 D_{\rm cap}(x)=E(x)-\tfrac12\|g\|^2
                       +\frac{|cg|^2}{1+2\ell^2}.
 \quad} \tag{17}
\]
This is a real polynomial of degree at most six. Its coefficients use
only the prescribed source maps and closing row.

Since \(D^2E\ge I+2c^*c\), strong convexity with this constant matrix
gives the lower bound
\[
 D_{\rm cap}(x)\le e_*\le E(x).
 \tag{18}
\]
Indeed the unconstrained minimum of the corresponding quadratic
minorant is
\(E-\tfrac12\langle g,(I+2c^*c)^{-1}g\rangle\).
The identity
\[
 (I+2c^*c)^{-1}=I-\frac{2c^*c}{1+2\ell^2}
\]
gives (17). At the interior minimizing field \(g=0\), so
\[
               \max_{x\in\mathcal D}D_{\rm cap}(x)=e_*.
 \tag{19}
\]
No concavity of this polynomial is asserted. It improves the earlier
certificate by the nonnegative term \(|cg|^2/(1+2\ell^2)\).

Equivalently, apply the quadratic minorant to the inner problem in
(4) at a trial field \(x\), then maximize its explicit scalar lower
bound. With \(b=\nabla R(x)\) and \(s=cx\), that maximum is attained
at
\[
 \lambda_{\rm trial}=\frac{s-cb}{1+2\ell^2},
\]
and its value is
\[
 R(x)-\tfrac12\|b\|^2
                  +\frac{|s-cb|^2}{1+2\ell^2}=D_{\rm cap}(x).
 \tag{20}
\]
This calculation is a lower bound even when the displayed trial scalar
lies outside the disk used for the smooth response theorem.

Combining (3) and (18), every feasible trial field gives
\[
 B_{\rm tot}^2\max(0,D_{\rm cap}(x))
       \le |K_N|^2\le\gamma B_{\rm tot}^2 E(x).
 \tag{21}
\]
This is an explicit lower witness for the original marked source. A
positive witness at the hyperbolic volume rate is still required; the
scalar reduction does not establish it.

## Sources and relation to previous boundary elimination

The complete sole proof source was read at the matching pin:

| Source | SHA-256 |
|---|---|
| [Convex normalized Conway source](research_convex_normalized_conway_source.md) | 6b89b4c6a67ef7a32cc41a5966c650f32de65d284ae7b70d94a71bddba21df3c |

The [connected-block energy](research_connected_conway_block_boundary_energy.md)
was also read in full for comparison, at pin
`426b0eba0c7f4c502cf2b82052daf4d5a224ad8ec8419b3e2d8a624771f192ae`.
It eliminates arbitrary internal blocks with clamped input and output
packets. The present argument instead separates the original scalar
closing by its convex conjugate. Both arguments retain the original
budgets; neither substitutes an operator norm for the coherent boundary
map. The older
[effective boundary response](research_global_cap_effective_response_criterion.md),
read at pin `14bbf99f1422b4d11d969c65919132824680be1a33bba6875c0e757d3b206754`,
concerns the variance of a particular endpoint-sector coefficient and
does not assert the exact scalar source dual proved here.

Only written reasoning and text operations were used. No mathematical
program, test, numerical iteration, build, git operation, or edit to an
existing final note was performed.
