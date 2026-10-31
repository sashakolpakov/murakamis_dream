# Source-normalized triangle entropy and an algebraic complete-radius balance test

exact lemma, 31 October 2026. This uses the original complete triangle potential and its proved closed coefficient entropy. It supplies a sufficient local test for the [complete-radius balance theorem](general_complete_radius_balance_filling_volume.md). Realization at arbitrary width remains separate. The full Fejér entropy $h$ is [not everywhere nonnegative](actual_fejer_entropy_signs_and_tail_insertion.md); no such assertion is used here.

## 1. The exact source normalization

For nonnegative weights $w=(x,b,y)$, not all zero, let $Q(w)=Q_b(0)$ be the original determinant-plus-beta-plus-half-forced-product triangle action. The [marked cofactor action theorem](actual_cross_cofactor_marked_action.md), equations (5)–(6), gives $Q_b(0)=F(x,b,y)$ with its absolute source normalization. No additive constant or magnetic monomial is changed here.

The [closed endpoint coefficient theorem](actual_fejer_half_block_entropy.md), Section 5, equations (15)–(16), gives on the triangle simplex

$$
\begin{aligned}
C_{\mathrm{tri}}(\boldsymbol\alpha)&=\sum_j f(\alpha_j),
&f(t)&=\frac{\Lambda(\pi t)+\Lambda(\pi/2-\pi t)}{\pi},\\
\alpha_j&\geq0,\qquad\sum_j\alpha_j=\frac12,
&\Lambda(s)&=-\int_0^s\log|2\sin v|\,dv.
\end{aligned}
$$

Its original positive triangle polynomial has degree $N/2+O(1)$, full triangle support, and uniform closed coefficient entropy $C_{\mathrm{tri}}$. Its weighted exponential rate is the same $F$. Finite positive Laplace summation therefore gives the exact identity

$$
Q(w)=\max_{\substack{\alpha_j\geq0\\\sum_j\alpha_j=1/2}}
\left[C_{\mathrm{tri}}(\boldsymbol\alpha)+\sum_j\alpha_j\log w_j\right].\tag{1}
$$

For a zero weight, the maximum is restricted to $\alpha_j=0$ at that coordinate; use $0\log0=0$ on the restricted face. This is literal coefficient specialization. It neither regularizes a protected target nor permits positive allocation to a zero weight.

More explicitly, the number of triangle coefficients is polynomial in $N$, uniform closed entropy gives the upper bound in (1), and lattice approximations to a maximizing point on the supported simplex face give the lower bound. The finite degree offset $O(1)$ vanishes after division by $N$. The polynomial comparison scalar between the original determinant and endpoint coefficient kernel has zero rate, as recorded in the closed theorem. Equation (1) is the source's own Legendre identity, not a free normalization choice.

## 2. A sharp elementary entropy lower bound

Define $g(t)=f(t)+t\log(2t)$, continuously at zero. Direct differentiation on $0<t<1/2$ gives

$$
f'(t)=\log\cot(\pi t),\qquad
g''(t)=\frac1t-\frac{2\pi}{\sin(2\pi t)}<0.\tag{2}
$$

The strict inequality follows from $0<\sin(2\pi t)<2\pi t$. Also $g(0)=g(1/2)=0$. Strict concavity gives $g(t)>0$ in the open interval. Summing at a triangle load yields

$$
C_{\mathrm{tri}}(\boldsymbol\alpha)
\geq-\sum_j\alpha_j\log(2\alpha_j),\tag{3}
$$

with equality exactly at the three vertices of its simplex. Indeed, equality requires every $\alpha_j$ to be either $0$ or $1/2$, and their sum is $1/2$. The inequality applies to boundary edges as well as the strict interior.

Let $S=x+b+y>0$ and choose $\alpha_j=w_j/(2S)$ in (1), retaining zero coordinates exactly. The Shannon expression in (3) then satisfies

$$
-\sum_j\alpha_j\log(2\alpha_j)+\sum_j\alpha_j\log w_j
=\sum_j\alpha_j\log S=\frac12\log S.
$$

Consequently

$$
Q(x,b,y)\geq\frac12\log(x+b+y).\tag{4}
$$

This is strict whenever at least two weights are positive, because the chosen load is not a simplex vertex. If exactly one weight is positive, the supported simplex consists of one vertex and (1) gives equality. This checks the absolute constant: $Q(x,0,0)=\tfrac12\log x$. If all weights vanish, the original positive-degree triangle polynomial vanishes and its logarithmic rate is minus infinity; that case is not used at an actual matching port.

## 3. Algebraic sufficient balance, including protected zeros

Let a port have nonnegative ordered weights $(x,b,c,y)$, and assume $A=x+y>0$. Write $X=Q(x,b,y)+Q(x,c,y)$. Then

$$
X\geq\frac12\log[(A+b)(A+c)].\tag{5}
$$

If $M=\max(b,c)>0$, at least the triangle with middle $M$ has two positive weights, so (5) is strict. Therefore the nonstrict algebraic condition

$$
(A+b)(A+c)\geq\max(b^2,c^2)\tag{6}
$$

implies

$$
X>\log b\quad\text{whenever }b>0,\qquad
X>\log c\quad\text{whenever }c>0.\tag{7}
$$

This includes equality in (6); strictness still comes from the actual triangle entropy. If $b=c=0$, condition (7) has no positive middle to test, and both one-sided finite sectors vanish exactly. No logarithm of a protected zero or assumption of four positive weights is hidden in this argument.

The simpler test

$$
\lvert b-c\rvert\leq x+y.\tag{8}
$$

implies (6) with strict inequality. For example, if $b\geq c$ and $b>0$, then $A+c\geq b$, hence $(A+b)(A+c)\geq b(A+b)>b^2$. If $b=c=0$, the product is $A^2>0$. The opposite order is symmetric. Both conditions are invariant under common positive rescaling of the original face weights.

The threshold in (6) can also be checked without squares: for $b\geq c$,

$$
A\geq\frac{\sqrt{(b-c)^2+4b^2}-(b+c)}2.\tag{9}
$$

This is the nonnegative root of the quadratic in $A$. In the boundary case $c=0$, it permits $b/A$ up to the golden ratio $(1+\sqrt5)/2$, with equality still sufficient for (7). Condition (8) is a convenient stronger test, not an equivalence.

## 4. Consequence and scope for the original diagram

At an actual certified simple-white port, $A>0$ because its outer pair is MATCHING and the two protected vertices are joined by the marked MAIN edge. Evaluate (6) or (8) on the one actual complete marked packing, with its protected zeros unchanged. If it holds at every port, (7) supplies exactly the strict hypothesis of the [complete-radius balance theorem](general_complete_radius_balance_filling_volume.md). Since the diagram has finitely many ports, the minimum of its finitely many required positive gaps is positive. That theorem controls the full one-sided remainder and original fixed-root filling period for independently sufficiently long fixed signed twists.

This lemma does not establish that every diagram satisfies (6), or that some diagram satisfying it exists at every bridge width. It does not prove the full Fejér entropy $h$ nonnegative, identify an independently optimized shared capacity, or interchange a minimax. The only entropy used in (2)–(4) is the triangle entropy.

## Validation
