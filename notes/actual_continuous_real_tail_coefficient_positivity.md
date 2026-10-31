# Continuous real-spectral positivity of each exact tail continuant

exact lemma, 31 October 2026. This strengthens the local tail estimate used in the [global CROSS theorem](actual_global_cross_spectral_gap.md). It gives no positivity statement for the full spectral numerator or for the signed prefix factors.

Write $\theta=\pi/N$, $s_j=2\sin(j\theta)$, and

$$
\alpha_{j-1}(\delta)=4\cos^2\!\left((j-\tfrac12)\theta\right)-4\sin^2(\pi\delta).
$$

For a fixed original start $i$ in the lower range $0\leq i\leq j\leq\lfloor N/2\rfloor$, normalize the [exact tail continuant](actual_cross_cofactor_factorization.md) by

$$
Q_j=\frac{K_{i,j}}{\prod_{r=i+1}^{j}s_r^2}.
$$

Then $Q_i=1$, $Q_{i+1}=x+y$, and the exact recurrence for $j\geq i+2$ is

$$
Q_j=(x+y)Q_{j-1}+\beta_jxyQ_{j-2},
\qquad \beta_j=\frac{\alpha_{j-1}}{s_js_{j-1}}.\tag{1}
$$

In the actual lower range the denominator is positive. The recurrence starts at its second step, so it never divides by $s_0$. Direct product-to-sum gives the row-independent identity

$$
s_js_{j-1}+\alpha_{j-1}
=4\cos^2(\pi\delta)-4\sin^2(\theta/2).\tag{2}
$$

Consequently $1+\beta_j\geq0$ for every row whenever

$$
|\delta|\leq\frac12-\frac1{2N}.
$$

Set $D_j=Q_j-xQ_{j-1}$. The exact induction is

$$
D_j=y\left[D_{j-1}+(1+\beta_j)xQ_{j-2}\right].\tag{3}
$$

Its initial value is $D_{i+1}=y$. Thus $Q_j$ and $D_j$ have nonnegative coefficients in $x,y$ on the entire indicated real-spectral interval, including its endpoint. The proof also allows $x=0$ or $y=0$. It uses no sign condition on $\beta_j$ itself.

For arbitrary complex outer faces, this proves

$$
|K_{i,j}(x,y;\delta)|\leq K_{i,j}(|x|,|y|;\delta).\tag{4}
$$

The original start sum is therefore bounded at arbitrary face phases by the same absolute-prefix sum used in the global CROSS upper-action proof. No cancellation is discarded inside the tail recurrence.

For a polynomial in $\sigma=-2\cos(2\pi\delta)$ of degree at most $CN$, this interval corresponds to $[-2,2\cos(\pi/N)]$. The affine Chebyshev variable of $\sigma=2$ relative to this interval is $1+O(N^{-2})$. The real Bernstein inequality therefore extends a uniform supremum bound to $[-2,2]$ with factor $\exp[O(C)]$, since

$$
\operatorname{arcosh}(1+O(N^{-2}))=O(N^{-1}).\tag{5}
$$

This is an absolute polynomial-norm extension, not a coefficientwise extension of positivity beyond the last physical spectral node. The [global LEFT weighted envelope](actual_global_left_weighted_spectral_envelope.md) applies this distinction to the actual one-sided source.

## Validation and scope

The row identity uses the original starting rows and avoids the zero sine denominator. It proves neither a shared one-sided capacity bound nor positivity of the full numerator.