# Projective parameter response of the original Conway source

22 November 2026. Research note; public manuscripts and earlier finals
remain unchanged.

Near saturation of the tree norm bound controls parameter derivatives
of the original source. The error depends only on the projective
tangent of each normalized local tensor. Parallel amplitude and phase
variations make no contribution to that error. For a one-leg insertion,
the projective tangent is an exact variance in the actual gauged
half-edge density, including all nonnormal and nilpotent terms.

The regularized metric construction supplies near saturation. Its
penalized minimum also gives a weak derivative statement without a
tangent bound. Neither statement identifies the local quantum means
with geometric filling derivatives.

## 1. A prescribed family and frozen gauges

Let a fixed finite tree have \(m\ge2\) vertices and complex bilinear
edge contractions. Its local coefficient tensors \(T_v(t)\) depend
smoothly on a real parameter \(t\). The root has a fixed Hilbert output
space, and the exact contracted output is \(Y(t)\ne0\). At a specified
parameter value choose invertible edge gauges, with inverse transpose
on the opposite endpoint. Write
\[
 U_v=T_v(g),\quad U_v^{[1]}=(\partial_tT_v)(g),\quad
 n_v=\|U_v\|_{\rm HS}>0,\quad \tau_v=U_v/n_v,\quad
 F=\prod_v n_v,\quad r=\|Y\|/F\in(0,1].
 \tag{1}
\]
The derivative in \(U_v^{[1]}\) freezes these gauges. It is not the
total derivative of a parameter-dependent gauged tensor.
All edge spaces are finite-dimensional; their dimensions may depend
on the quantum level.

Define the normalized insertion, its scalar part, and its projective
part by
\[
 b_v=U_v^{[1]}/n_v,\qquad z_v=\langle\tau_v,b_v\rangle,\qquad
 b_v^\perp=b_v-\tau_v z_v,\qquad
 P_{\rm pr}=\sum_v\|b_v^\perp\|.
 \tag{2}
\]
Inner products are conjugate-linear in the first argument. Let
\(Y_v^{[1]}\) be the original contraction with only \(T_v\) replaced
by \(\partial_tT_v\), and put
\[
 w_v=\frac{\langle Y,Y_v^{[1]}\rangle}{\|Y\|^2}.
 \tag{3}
\]
These insertions retain the original closing and all source phases.

## 2. The finite response inequality

**Theorem 1.** At every parameter value described above,
\[
 \boxed{\quad
 |w_v-z_v|\le\frac{\sqrt{1-r^2}}{r}\,\|b_v^\perp\|,
 \qquad
 \left|\partial_t\log\|Y\|-\partial_t L(g)\right|
 \le\frac{\sqrt{1-r^2}}{r}\,P_{\rm pr},
 \quad}
 \tag{4}
\]
where \(L(g)=\sum_v\log\|T_v(g)\|_{\rm HS}\), and its displayed
derivative holds the gauges fixed. The first inequality is complex;
the second uses real derivatives.

**Proof.** Remove vertex \(v\) and contract every other normalized
tensor. This defines a linear environment map
\(E_v\) from the full coefficient Hilbert space at \(v\) to the root
output. Tree Cauchy--Schwarz, applied with an arbitrary tensor in the
missing slot, gives
\[
 \|E_v\|_{\rm op}\le1,\qquad E_v\tau_v=Y/F,\qquad
 E_vb_v=Y_v^{[1]}/F .
 \tag{5}
\]
The tree and its original bilinear evaluation are essential here;
the environment is complex-linear in the missing tensor.
Put \(W_v=E_v^*E_v\). Then \(0\le W_v\le I\) and
\(\langle\tau_v,W_v\tau_v\rangle=r^2\). Consequently
\[
 w_v-z_v=\langle d_v,b_v\rangle,\qquad
 d_v=(W_v/r^2-I)\tau_v,\qquad \langle\tau_v,d_v\rangle=0,
 \tag{6}
\]
and \(W_v^2\le W_v\) gives
\[
 \|d_v\|^2
 =\frac{\langle\tau_v,W_v^2\tau_v\rangle}{r^4}-1
 \le r^{-2}-1.
 \tag{7}
\]
The exact orthogonality in (6) permits replacing \(b_v\) by
\(b_v^\perp\). Cauchy--Schwarz proves the first bound in (4).
Finally
\[
 \partial_t\log\|Y\|=\operatorname{Re}\sum_vw_v,\qquad
 \partial_tL(g)=\operatorname{Re}\sum_vz_v.
 \tag{8}
\]
The triangle inequality proves the second bound. \(\square\)

The projective quantity has the explicit formula
\[
 \|b_v^\perp\|^2=
 \frac{\|U_v^{[1]}\|^2}{\|U_v\|^2}
 -\frac{|\langle U_v,U_v^{[1]}\rangle|^2}{\|U_v\|^4}.
 \tag{9}
\]
It is unchanged by adding any scalar multiple of \(U_v\) to
\(U_v^{[1]}\). Thus a whole-tensor scalar amplitude or phase derivative
is removed exactly, rather than bounded separately.

This statement does not permit discarding a factor acting only on
the physical block of an anchored tensor \((1,f)\). Its derivative
need not be parallel to the whole anchored tensor. Every recorded
carrier remains unless its complete tensor action is genuinely scalar.

## 3. A local observable and its exact projective variance

Suppose at the frozen gauges the insertion acts on one tensor leg:
\[
 U_v^{[1]}=(B\otimes I)U_v .
 \tag{10}
\]
Let \(\rho_{v,e}\) be the actual reduced density of the unit vector
\(\tau_v\) on that coordinate leg. Partial trace gives
\[
 z_v=\operatorname{tr}(\rho_{v,e}B),\qquad
 \boxed{\quad
 \|b_v^\perp\|^2
 =\operatorname{tr}(\rho_{v,e}B^*B)
                   -|\operatorname{tr}(\rho_{v,e}B)|^2.
 \quad}
 \tag{11}
\]
No Hermiticity, normality, or diagonalizability of \(B\) is required.
If the leg is dual, (10) uses its literal dual-coordinate generator;
the prescribed transpose and signs are included in \(B\).
Endpoint arrows and nilpotent directions are retained.

These are the actual normalized tensor marginals at the chosen
gauges. They are not freely chosen calibration densities or diagonal
probabilities. A spectral eigenvalue substitution does not establish
(11) for a different density or a truncated insertion.
Equation (9) is also one quarter of the pure-state quantum Fisher
information: for \(\tau=U/\|U\|\), its real-parameter derivative is
\(\tau'=b-\tau\operatorname{Re}z\), and
\(\|\tau'\|^2-|\langle\tau,\tau'\rangle|^2=\|b^\perp\|^2\).

## 4. The actual anchored compiler and regularized metrics

Apply the theorem to an already prescribed parameter family of the
complete anchored Conway compiler. Its output is exactly
\(Y_N(t)=(1,K_N(t))\). Full Hermite boundary spaces, original turns,
crossing coupons, closing row, framing and peripheral factors remain.
This does not define a new interpolation between integer fillings.
Any parameter-dependent extension must specify its actual tensors
and source conventions.

Use the regularized metrics with fixed tree size \(m\) and
\[
 \varepsilon_N=\frac1{m^2N^2},\qquad
 J_{N,\varepsilon_N}(H,t)=L_N(H,t)+\varepsilon_N\log Z(H),\qquad
 Z(H)=1+\sum_e\operatorname{tr}(H_e+H_e^{-1}).
 \tag{12}
\]
The complete regularization proof gives a unique minimizer \(H_N(t)\).
Its unpenalized product \(F_N=e^{L_N(H_N(t),t)}\) satisfies
\[
 a_{N,m}F_N\le\|Y_N\|\le F_N,\qquad
 a_{N,m}=1-\frac{4\sqrt2}{N}-\frac{10}{mN^2},
 \tag{13}
\]
whenever \(a_{N,m}>0\), in particular for \(N\ge8\).
Evaluate all projective tangents at these metrics, freezing them
inside each tensor derivative. Theorem 1 yields
\[
 \left|\partial_t\log\|Y_N\|-\partial_tL_N(H_N(t),t)\right|
 \le\sqrt{a_{N,m}^{-2}-1}\,P_{{\rm pr},N}.
 \tag{14}
\]
The prefactor is \(O(N^{-1/2})\) for a fixed tree.
Thus \(P_{{\rm pr},N}=O(N)\) would give an \(O(N^{-1/2})\)
error after division by \(N\). A bound \(O(\sqrt N)\) would give
an \(O(N^{-1})\) scaled error. Such bounds for arbitrary required
short-filled geometric sources are not proved here.

For a smooth family, differentiation of the stationary metric problem
also gives the usual envelope identity
\[
 j_N(t)=\min_HJ_{N,\varepsilon_N}(H,t),\qquad
 j_N'(t)=\partial_tL_N(H_N(t),t)=\operatorname{Re}\sum_vz_{v,N}.
 \tag{15}
\]
For example real-analytic finite tensor families meet this smoothness
condition. The positive coordinate Hessian at the unique regularized
minimum gives the local implicit-function argument; uniqueness
identifies the local minimizers. Stationarity removes the metric
derivative of the **penalized** objective.
It does not identify \(j_N'\) with the total derivative of the
unpenalized value \(L_N(H_N(t),t)\). Their exact relation is
\[
 \frac d{dt}L_N(H_N(t),t)
 =j_N'(t)-\varepsilon_N\frac d{dt}\log Z(H_N(t)).
\]

## 5. A weak statement without a tangent bound

There is a second consequence using the explicit penalty estimate.
Suppose on each compact parameter interval the same compiler has
\[
 \log B_N(t)\le C N,\qquad
 B_N(t)=\prod_v\max(1,\|T_{v,N}(t)\|_{\rm HS}),
 \qquad \log D_N=O(\log N),
 \tag{16}
\]
uniformly, where \(D_N\) is the sum of the edge dimensions.
The ordinary anchored spaces give \(D_N=(m-1)(N+1)\).
The spectral-compactness proof supplies, for any anchored tree,
\[
 0\le j_N(t)-\log\|Y_N(t)\|
 \le\varepsilon_N\{1+A_m(B_N(t),D_N,\varepsilon_N)\}=O(N^{-1}),
 \tag{17}
\]
where
\(A_m(B,D,\eta)=\log(1+2D)+(2+2m(m-1))\log B
 +(m-1)\log(m/(2\eta))\).
This uses the additional explicit near-capacity construction, not
coercivity alone. The bound is uniform under (16).
For every real \(C^1\) test function \(\varphi\) supported in the
interior of such an interval, (15), (17), and integration by parts give
\[
 \boxed{\quad
 \left|\int\varphi(t)
 \left[\operatorname{Re}\sum_vz_{v,N}(t)
                -\partial_t\log\|Y_N(t)\|\right]dt\right|
 \le \frac C N\|\varphi'\|_{L^1}.
 \quad}
 \tag{18}
\]
After division by \(N\), this is an \(O(N^{-2})\) weak error.
No pointwise insertion-variance bound is used in (18).
It proves no pointwise derivative convergence by itself.

## 6. The remaining geometric step

The means in (11) and (15) are explicit finite quantum quantities.
To use a geometric parameter path one must still identify their
scaled limits with its marked Schlaefli derivatives. Here \(t_v\)
denotes the complex angular coordinate at vertex \(v\) of a supplied
marked geometric stationary configuration. The phase convention has
the explicit filling and charge terms
\(in_vt_v^2/(4\pi)-i\chi_vt_v\), with no other explicit dependence
on these parameters. Stationarity removes derivatives of the angular
coordinates, so the corresponding real-action derivatives are
\(\operatorname{Re}(it_v^2/(4\pi))\) for a filling-power parameter
and \(\operatorname{Im}t_v\) for its charge.
That identification is not a consequence of matrix balance alone.
Likewise, a local formal Gaussian does not establish the actual
projective variances in (11) in the full compiler metric.

The theorem constructs no universally positive geometric branch,
parameter path, initialized cycle, or new source asymptotic after
arbitrary short partial filling. It supplies an actual response
inequality and a weak local-mean identity for the unchanged source.
No geometric volume limit or new filling class follows here.

## Complete proof sources

All four complete matching texts were read. The environment and
projective-response proofs are given above; the directs supply the
actual compiler, norm comparison, regularization and penalty bound.

| Source | SHA-256 |
|---|---|
| [Full tree capacity](research_scalar_tree_full_gauge_capacity.md) | 2997b732aa73e063c66e81d6487a1d9927509609d61842c1dbb43d9345df1d6d |
| [Regularized capacity](research_regularized_actual_source_capacity.md) | 0cea0d52182eb24b4610538f354dbe5158fa54aa6f9cf7f9fc280c72ab090ff8 |
| [Spectral compactness and the penalty](research_regularized_source_metric_compactness.md) | fd8dae7561eff37089e8481b4eb8c8344acb56da86b502350292f6d2be9c8818 |
| [Anchored Conway compiler](research_anchored_conway_positive_variational_period.md) | e83c35d16c79faa13ac6556db78b9b57da2a2371d3fc04c4673ecd74e1d336f7 |

Envelope differentiation, matrix projection bounds and
integration by parts are standard methods; no novelty is claimed for
them. Only written mathematics and text/hash operations were used.
No mathematical program, numerical test, build, git operation, or
earlier-final edit was performed.
