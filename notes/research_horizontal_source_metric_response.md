# Horizontal transport of the regularized source metrics

22 November 2026. Research note; public manuscripts and earlier finals
remain unchanged.

The canonical source metrics vary with the prescribed quantum tensors.
Their coordinate derivatives can be large. Nevertheless, after fixing
the unitary freedom by a horizontal lift, their contribution to the
projective motion of the local tensors is controlled by the physical
parameter variation at those same optimized metrics. There is an exact
identity, with no inverse metric-Hessian constant.

This removes a separate moving-frame hypothesis. It does not estimate
the physical variances in the optimized metrics, identify geometric
principal vectors, or preserve an initialized geometric coefficient
without further source information.

## 1. The prescribed tree and its canonical metrics

Fix a finite rooted tensor tree with complex bilinear edge contractions.
Its local coefficient tensors \(T_v(t)\) are smooth in a real parameter
\(t\) in an open interval \(I\). All spaces are finite-dimensional and
fixed while differentiating. They may depend on a quantum level \(N\).
The original output is \(Y(t)\) in a fixed Hilbert space. Assume
\(\|Y(t)\|\ge1\). The complete anchored Conway compiler has exactly this
property, with \(Y_N(t)=(1,K_N(t))\), whenever a parameter family of its
actual tensors has been prescribed.

An edge gauge \(g_e\) acts at its child end and \(g_e^{-\mathsf T}\)
at its parent end. These preserve the original bilinear contraction.
Put \(H_e=g_e^*g_e>0\), and define
\[
 L(H,t)=\sum_v\log\|T_v(g,t)\|_{\rm HS},\qquad
 Z(H)=1+\sum_e\operatorname{tr}(H_e+H_e^{-1}),\qquad
 J_\varepsilon(H,t)=L(H,t)+\varepsilon\log Z(H).
 \tag{1}
\]
The local norms depend only on \(H\): changing \(g_e\) by a left
unitary applies unitary factors at both adjacent tensors.
When gauges are passed as arguments below,
\(J_\varepsilon(g,t)\) abbreviates \(J_\varepsilon((g_e^*g_e)_e,t)\).
Throughout this note \(\varepsilon>0\) is fixed with respect to \(t\).
It may depend on \(N\).

The complete capacity and regularization proofs give a unique minimizer
\(H(t)\) of (1). They also give geodesic convexity of \(L\) and strictly
positive geodesic second derivatives of \(\log Z\) on every nonconstant
positive-matrix geodesic.

The minimizing metrics are smooth in \(t\). Indeed the local tensor
norms are nonzero, since a zero tensor would give \(Y=0\).
At a minimum the ordinary coordinate Hessian of \(J_\varepsilon\)
equals its geodesic Hessian as a quadratic form: the first derivative
vanishes. The latter is positive definite by the regularizer. The
implicit function theorem therefore gives a smooth local critical
point. Geodesic convexity makes it a global minimum, and uniqueness
identifies these local solutions on overlaps.

## 2. A genuine horizontal lift

There is a smooth choice of gauges above \(H(t)\) satisfying
\[
             g_e^*g_e=H_e,\qquad
             g_e'=X_eg_e,\qquad X_e=X_e^*.
 \tag{2}
\]
To construct it from any initial \(g_e(t_0)^*g_e(t_0)=H_e(t_0)\), solve
\[
                  g_e'=\tfrac12g_e^{-*}H_e'.
 \tag{3}
\]
Here \(g^{-*}=(g^*)^{-1}\). Direct differentiation gives
\((g_e^*g_e)'=H_e'\), so the required equality is preserved.
Moreover
\[
                  X_e=\tfrac12g_e^{-*}H_e'g_e^{-1}
 \tag{4}
\]
is Hermitian. Local existence for (3) holds on the invertible matrices.
On a compact subinterval, positivity and continuity of \(H_e\) bound
both \(g_e\) and its inverse. The smooth equation then continues the
lift throughout that subinterval, and hence throughout \(I\).
Different initial lifts differ by a constant left unitary.

This choice matters. Arbitrary parameter-dependent unitary rotations
could create arbitrarily large coordinate velocities without changing
the metrics. Equation (2) removes that freedom. No assertion is made
that the positive square roots \(H_e^{1/2}\) themselves satisfy (2).

Write
\[
 U_v(t)=T_v(g(t),t),\qquad n_v=\|U_v\|_{\rm HS},\qquad
 \tau_v=U_v/n_v,\qquad P_v=\tau_v\tau_v^*.
 \tag{5}
\]
Let \(U_v^{[1]}=(\partial_tT_v)(g(t),t)\) denote the physical derivative
with every edge gauge frozen at that parameter value. Define
\[
 b_v=U_v^{[1]}/n_v,\qquad
 q_v=(I-P_v)b_v,\qquad
                     P_{\rm phys}^2=\sum_v\|q_v\|^2.
 \tag{6}
\]
These are the actual tangents in the optimized metrics, not tangents
in the original identity metric.

For the velocity \(X=(X_e)_e\) in (2), let \(A_v(X)\) be the sum of
its incident leg generators. An outgoing vector leg contributes \(X_e\);
an incoming dual leg contributes \(-X_e^{\mathsf T}\). Each generator
is Hermitian. Operators on different legs commute. Set
\[
 \mu_v=\langle\tau_v,A_v(X)\tau_v\rangle\in\mathbb R,\qquad
 a_v=(A_v(X)-\mu_vI)\tau_v,\qquad
                     P_{\rm gauge}^2=\sum_v\|a_v\|^2.
 \tag{7}
\]
Inner products are conjugate-linear in their first argument.
Differentiating the actual gauged tensor gives
\[
 U_v'=U_v^{[1]}+A_v(X)U_v,\qquad
 (I-P_v)\tau_v'=q_v+a_v,\qquad
                     P_{\rm tot}^2=\sum_v\|q_v+a_v\|^2.
 \tag{8}
\]
Thus \(P_{\rm tot}\) is the product-state Fubini--Study speed of the
moving normalized tensors in this horizontal lift.

## 3. An exact response identity

For a fixed parameter and a Hermitian tuple \(X\), use the gauge curve
\(g_e(s)=e^{sX_e}g_e\). Its metrics are
\(H_e(s)=g_e^*e^{2sX_e}g_e\), a simultaneous positive-matrix geodesic.
Define the nonnegative quadratic form
\[
 {\cal H}_R(X)=
 \left.\frac{d^2}{ds^2}\log Z((g_e^*e^{2sX_e}g_e)_e)\right|_{s=0}
 \ \ge0.
 \tag{9}
\]
The inequality is the regularizer's geodesic convexity, not convexity
in arbitrary noncommuting logarithmic coordinates.

**Theorem.** Along the canonical metrics and their horizontal lift,
\[
 \boxed{\qquad
 P_{\rm phys}^2
      =P_{\rm tot}^2+P_{\rm gauge}^2+\varepsilon{\cal H}_R(X).
 \qquad}
 \tag{10}
\]
In particular \(P_{\rm tot}\le P_{\rm phys}\) and
\(P_{\rm gauge}\le P_{\rm phys}\). The constants do not depend on any
edge dimension, the quantum level, or a metric condition number.

**Proof.** On the gauge curve, the local tensor is
\(e^{sA_v(X)}U_v\). Scalar integration in a spectral basis gives
\[
 \left.\frac{dL}{ds}\right|_0=\sum_v\mu_v,\qquad
 \left.\frac{d^2L}{ds^2}\right|_0=2\sum_v\|a_v\|^2.
 \tag{11}
\]
For the second identity, the squared norm is a sum of positive
exponentials; the second derivative of its half logarithm is twice
the variance of \(A_v(X)\).

Hold \(g,X\) fixed and differentiate the first expression in (11)
only through the physical tensors. Normalization and
\(q_v\perp\tau_v\) give
\[
 \partial_t^{\rm phys}\sum_v\mu_v
                         =2\operatorname{Re}\sum_v\langle q_v,a_v\rangle.
 \tag{12}
\]
The scalar phase and amplitude parts of \(b_v\) cancel from this
mixed derivative. They remain in the original local and source means.

Fix \(t_0\) and keep the tuple \(X=X(t_0)\) constant in this argument.
At every nearby \(t\), stationarity says
\[
 \left.\partial_s
 J_\varepsilon((e^{sX_e}g_e(t))_e,t)\right|_{s=0}=0.
 \tag{13}
\]
Differentiate (13) at \(t_0\). Its physical part is (12).
Since \(g_e'(t_0)=X_eg_e(t_0)\), its gauge part is the second
derivative on the same gauge curve used in (11) and (9).
This can also be checked in ordinary matrix coordinates: both are
the second differential in the direction \(Xg\), plus the first
differential applied to \(X^2g\). Thus no commuting-matrix assumption
or omitted frame-connection term is involved. We obtain
\[
 2P_{\rm gauge}^2+\varepsilon{\cal H}_R(X)
                  =-2\operatorname{Re}\sum_v\langle q_v,a_v\rangle.
 \tag{14}
\]
Expanding (8) and substituting (14) proves (10).
\(\square\)

If \(\varepsilon\) varied with the physical parameter, differentiating
(13) would produce an additional term. The fixed-\(\varepsilon\)
hypothesis is therefore essential to the stated identity.

## 4. What the identity controls about principal lines

Let \(\rho_v(t)\) be an output marginal of \(\tau_v(t)\), and suppose
its largest eigenvalue has gap at least \(\gamma>0\) from the rest.
Its principal unit vector can be chosen smoothly with
\(\langle\psi_v,\psi_v'\rangle=0\). Differentiating the marginal,
removing the scalar phase of \(\tau_v'\), and taking a partial trace gives
\[
 \|\rho_v'\|_{\rm op}\le\|\rho_v'\|_1
                                  \le2\|q_v+a_v\|.
 \tag{15}
\]
Differentiating \(\rho_v\psi_v=\lambda_v\psi_v\) and projecting onto
\(\psi_v^\perp\) then gives
\[
 \|\psi_v'\|\le\frac2\gamma\|q_v+a_v\|,\qquad
                 \sum_v\|\psi_v'\|^2\le\frac4{\gamma^2}P_{\rm phys}^2.
 \tag{16}
\]
Use the actual gap for each vector if no common \(\gamma\) is available.
The phase choice is a comparison convention; it does not reset any
original source phase.

For the anchored compiler the full marginal estimate gives
\(S\le2\varepsilon\). The capacity purity proof gives
\(1-\lambda_{\max}(\rho_v)\le2S\) on every proper output.
The original closing has one input and output \(\mathbb C^2\);
its input and output marginals have the same nonzero eigenvalues.
Consequently, for \(0<\varepsilon<1/8\), all these output gaps obey
\[
                  \lambda_1-\lambda_2\ge1-4S
                                             \ge1-8\varepsilon>0.
 \tag{17}
\]
The gap is supplied by purity, rather than assumed to control an
otherwise unknown eigenvector velocity. Equations (10) and (16)
provide the needed derivative estimate. Internal vectors are expressed
in the horizontal metric frames; this is not a velocity bound in the
original Newton coordinates.

## 5. The actual remaining source requirement

The projective parameter-response theorem uses the same frozen-gauge
physical \(q_v\) as (6). For a one-leg insertion
\(U_v^{[1]}=(B_v\otimes I)U_v\), it is exactly
\[
 \|q_v\|^2=\operatorname{tr}(\rho_{v,e}B_v^*B_v)
                           -|\operatorname{tr}(\rho_{v,e}B_v)|^2.
 \tag{18}
\]
Here \(\rho_{v,e}\) is the true optimized tensor marginal.
The dual-leg transpose, strict endpoints, nilpotents and known carrier
derivatives all remain in \(B_v\). A whole-tensor scalar derivative
is parallel and contributes zero to (6); an operation only on the
physical block of an anchored tensor need not be parallel.

Thus an independently proved bound on (18) also controls the moving
canonical principal lines, without a separate bound on \(H'(t)\).
The existence and smoothness hypotheses above hold for any prescribed
smooth anchored source family at each finite level. They do not give
a bound uniform in \(N\) for (18), or identify its limiting means.
The bound must be proved in the same optimized metrics, not imported
from an unrelated raw or geometric reference frame.

No parameter interpolation, positive geometric path, Gaussian variance
bound, marked Schlaefli identity, or initialized coefficient transport
is constructed here. Smooth transport of a line alone does not retain
its overlap or leading amplitude in the original closing.
The new deduction controls the extra optimizing-frame motion. The
remaining physical variance and geometric source comparisons are still
required for the finite-exception theorem. No new knot class is proved.

## Complete proof sources and coverage

The following three entire matching texts were read. They provide the
tree norm and purity estimates, canonical regularization and the earlier
frozen-gauge response. The horizontal lift and identity (10) are proved
above. No spectral-compactness or penalty asymptotic is imported.

| Source | SHA-256 |
|---|---|
| [Projective source response](research_projective_conway_parameter_response.md) | 9b1f374d5352a2f361d54096ae6cab9fe494c8dccfc309a35433fce656045335 |
| [Regularized actual-source capacity](research_regularized_actual_source_capacity.md) | 0cea0d52182eb24b4610538f354dbe5158fa54aa6f9cf7f9fc280c72ab090ff8 |
| [Full tree capacity](research_scalar_tree_full_gauge_capacity.md) | 2997b732aa73e063c66e81d6487a1d9927509609d61842c1dbb43d9345df1d6d |

The existing capacity and response notes were checked for coverage.
Geodesic variance formulas, horizontal frame choices and implicit
differentiation are standard methods; no novelty is claimed for them.
Only written mathematics and text/hash operations were used. No
mathematical program, test, build, git operation or earlier-final edit
was performed.
