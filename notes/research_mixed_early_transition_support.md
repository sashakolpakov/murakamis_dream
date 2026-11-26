# A block estimate for the beginning of the left transition

Research theorem, 4 November 2026. The finite boundary inequalities
below prove a uniform block estimate. No global transition assembly
is asserted in this note.

The selected contour reaches its positive height at real coordinate
\(.12\). Before that point, the monotonicity used farther along the
contour need not hold. We instead compare a block directly with its
geometric supporting plane, including the cost of changing the height
in its neighboring plateau block.

## 1. Parameters and the estimate

Let \(\eta,\epsilon\in\{0,1\}\) be the type indicators of an
ordered block. Retain the original critical phase
\[
 \phi_{\eta\epsilon}(a,b)
 =\operatorname{stat}_s\{g(s+a)+g(s+b)-(2+\epsilon)g(s)
                       +2\pi ias\}
 -(1+\eta/2)g(a)-(1+\epsilon/2)g(b),
 \qquad
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i}.
 \tag{1}
\]
All critical roots and logarithms use their original zero lift. The
reference pair \(r=(r_0,r_1)\) belongs to
\[
 R_3=[.30,.39]+i[-.03,.02],\qquad
 R_4=[.27,.33]+i[-.057,-.02].                                 \tag{2}
\]
Its supporting plane is
\(\Gamma_r(z)=\phi(r)+\phi'(r)\cdot(z-r)\).

Let \(\sigma_0\le\eta\) and \(\sigma_1\le\epsilon\)
indicate the selected Fourier factors. For each
\(f_k\in\{0,\ldots,\sigma_k\}\), put
\[
 \psi_f(z)=\phi(z)+\sum_{k=0}^1
     \{f_kg(z_k)/2+\pi i(\sigma_k-f_k)z_k\}.                 \tag{3}
\]
Taking the maximum of these real parts retains both actual Fourier
alternatives. It does not replace the selected term by a formal phase.

Choose the low position \(j\in\{0,1\}\), and put \(k=1-j\).
The real targets satisfy
\[
 \Re z_j\in[.10,.12],\qquad \Re z_k\in[.10,.45].             \tag{4}
\]
The target heights vary independently in these closed intervals:

| Type and selection | Allowed height |
|---|---|
| Type three | \([-1/200,1/300]\) |
| Unselected type four | \([-19/2000,0]\) |
| Selected type four | \([0,7/500]\) |

Write \(q_0=11/2\), \(q_1=151/20\).

**Theorem 1.** For every parameter and Fourier choice specified above,
\[
 \Re\{\psi_f(z)-\Gamma_r(z)\}
             +q_j(\Im r_k)^2<-\frac1{100}.                  \tag{5}
\]
The index on \(q_j\) records which argument of the *adjoining*
block has its height changed. It is the same orientation as in the
[isolated-transition estimate](research_mixed_isolated_transition_phase.md).
Using the full allowance \(q_j(\Im r_k)^2\) pays for every fraction
of a removed height when the adjoining block satisfies the hypotheses
of the existing reset theorem. Here the neighboring target need not
itself be on the plateau; (5) is asserted with that same allowance
throughout (4), without claiming that every adjoining reset has already
been estimated.

## 2. Why finite tangents suffice

Every target rectangle above lies in
\([.1,.45]+i[-.0095,.014]\). The elementary cotangent bound
\[
 |\Im\cot\pi(x+ih)|
 \le \frac{\sinh(7\pi/250)}{2\sin^2(\pi/10)}<\frac12       \tag{6}
\]
and \(\Re\cot\pi(x+ih)>0\) hold throughout this rectangle.
The [global cotangent theorem](research_mixed_global_cotangent_roots.md)
therefore supplies the unique holomorphic original root on its full
product, before a comparison of values is made.

For completeness, (3) retains the positive Hessian argument even on
branches with \(f_k=1\). Before eliminating \(s\), its phase is
\[
 V(s,a)+V(s,b)-\epsilon g(s)
  -\frac{\eta-f_0}{2}g(a)-\frac{\epsilon-f_1}{2}g(b)
  +2\pi ias+\pi i\sum_k(\sigma_k-f_k)z_k,
 \quad V(s,a)=g(s+a)-g(s)-g(a).                              \tag{7}
\]
The two triangle forms are positive on (6), and all three remaining
diagonal coefficients are nonnegative. The imaginary chirp and
linear terms do not change the real Hessian. The complex Schur
identity from the [real support theorem](research_mixed_real_outer_support.md)
therefore gives \(-\Re\psi_f''>0\). Hence, for fixed heights,
\(\Re\psi_f\) is concave in the two real coordinates. With
the other variables fixed it is convex in each height.

Apply height convexity twice. It suffices to prove (5) at the four
height endpoints. At such an endpoint, partition the other real
coordinate into sixteen equal intervals of length \(7/320\), from
\(.10\) to \(.45\). On each small rectangle, take the tangent
to \(\Re\psi_f\) at low coordinate \(.12\) and at the midpoint
of the other interval. Concavity bounds the phase by that tangent.
The difference between this tangent and \(\Re\Gamma_r\) is affine
in the real target coordinates. Its maximum on the small rectangle
is therefore attained at a corner.

It remains to check finitely many fixed complex targets. For each of
them the reference-dependent function
\[
 -\Re\Gamma_r(z)+q_j(\Im r_k)^2                            \tag{8}
\]
is separately subharmonic on the two reference rectangles. Indeed,
the first term is the real part of a holomorphic function of each
reference, while the additional quadratic has nonnegative Laplacian.
Two maximum principles reduce (8) to the sixteen products of rectangle
sides. The independence of the target heights is essential here: no
height depending on a reference is silently treated as holomorphic.

## 3. Outward verification and the finite sums

There are 64 reference boundary products across the four ordered type
pairs. On each one the checker tests every permitted selection and
forcing choice, both low positions, all height endpoints and all tangent
corners. It uses exact original-logarithm Newton self-maps for the
reference and tangent roots. The reference derivative identity is
\[
 d_r\Gamma_r(z)=\phi''(r)(z-r)\,dr.                         \tag{9}
\]
The derivative of the quadratic in (8) is included in each interval
mean-value estimate. Prefix-free dyadic covers of mass one exhaust
the full reference boundary products. Saved-cover replay rechecks
every rational witness and every inequality.

The 64 reference boundary products have a complete cover of 251
accepted dyadic cells. Every tangent comparison on these cells is
strictly below \(-1/100\), so Sections 1--2 prove (5) on the
whole stated domain. For an actual early contour with one common low
coordinate \(t\in[.1,.12]\), the unselected height fraction is
\((t-.1)/.12\le1/6\), and the selected fraction is
\(50(t-.1)\le1\). Its two heights lie in the intervals above.
The [early-cap source theorem](research_mixed_early_selected_source_cap.md)
then converts (5) into a bound for the entire finite block, with loss
\(1/200\) after allowing the uniform subexponential factors.
This finite-sum conclusion is asserted only on those actual contour
parameters; an asymptotic on the larger independent height rectangles
is not needed or claimed.

The comparison now includes an early coordinate next to another early
coordinate or a later transition. It retains a full algebraic allowance
for an adjoining reset. Assigning these allowances consistently to all
affected edges, and controlling the remaining edges in a cycle, still
requires a global argument.

```sh
python3 experiments/certify_mixed_early_transition_support.py --precision 256
```

To replay the same complete cover at higher precision, run:

```sh
python3 experiments/certify_mixed_early_transition_support.py \
  --precision 320 \
  --input repro/results/research-mixed-early-transition-support.json \
  --output /tmp/research-mixed-early-transition-support-replay.json
```
