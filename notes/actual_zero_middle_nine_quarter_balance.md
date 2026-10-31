# An elementary balance certificate for one zero middle

source-normalized lemma, 31 October 2026. This is a local analytic test on actual complete curvatures. It does not by itself construct a family of diagrams or assert that the test holds for one.

Let a port have middle curvatures $0$ and $e>0$, outer curvatures $x,y\geq0$, and $A=x+y>0$. Retain the original complete triangle potential $Q$ from the [calibrated source](actual_cross_cofactor_marked_action.md). If

$$
\frac eA\leq\frac94,\tag{1}
$$

then its strict complete-radius balance gap satisfies

$$
Q_e(0)+Q_0(0)-\log e>\frac1{2500}.\tag{2}
$$

Here $Q_e(0)=Q(x,e,y)$ and $Q_0(0)=Q(x,0,y)$. Either outer curvature may vanish. If $e=0$ as well, both one-sided sectors vanish exactly and no positive-middle balance inequality is required.

## 1. The worst outer split has one zero outer curvature

For fixed $A$ and $P=xy$, the zero-spectral lower-tail Perron factor is

$$
\Lambda_P(t)=2\sin(\pi t)
\left[A\sin(\pi t)+\sqrt{A^2\sin^2(\pi t)+4P\cos^2(\pi t)}\right].
$$

It increases with $P$ for every $t\in(0,1/2)$. The original weighted start action is

$$
F_b(\mu;P)=\mu\log b+\int_0^\mu\log[4\cos^2(\pi t)]\,dt
+\int_\mu^{1/2}\log\Lambda_P(t)\,dt.
$$

Its maximum over $\mu$ is exactly $Q(x,b,y)$; for $b=0$ the sole start is $\mu=0$. Each $Q$ is therefore nondecreasing in $P$ at fixed $A,b$, by taking the maximum after the pointwise comparison of these actual actions. This is a local comparison, not a shared minimax exchange. Consequently

$$
Q(x,e,y)+Q(x,0,y)\geq Q(A,e,0)+Q(A,0,0).
$$

The exact half-degree homogeneity and monomial normalization give

$$
\begin{aligned}
Q(A,e,0)+Q(A,0,0)-\log e&=F(r)-\log r,\\
r&=e/A,\qquad F(r)=Q(1,r,0),\qquad Q(A,0,0)=\tfrac12\log A.
\end{aligned}\tag{3}
$$

No additive source constant has been removed.

## 2. Exact one-variable formula and monotonicity

At outer weights $1,0$, the actual saddle is

$$
\mu(r)=\frac1\pi\arctan\sqrt r,\qquad
\frac{dF}{d\log r}=\mu(r),\qquad F(0)=Q(1,0,0)=0.
$$

Define $T(z)=\int_0^z\arctan(t)\,dt/t$. Then

$$
F(r)=\frac2\pi T(\sqrt r).\tag{4}
$$

The derivative of $F(r)-\log r$ with respect to $\log r$ is $\mu(r)-1<0$, so it suffices to bound its value at $r=9/4$. Direct differentiation using $\arctan z+\arctan(1/z)=\pi/2$ for $z>0$ proves

$$
T(z)-T(1/z)=\frac\pi2\log z.
$$

At $z=3/2$, (4) therefore yields

$$
F(9/4)-\log(9/4)=\frac2\pi T(2/3)-\log(3/2).\tag{5}
$$

## 3. A rational lower bound without numerical quadrature

Integrating the alternating power series of $\arctan$ gives

$$
T(t)=\sum_{j\geq0}\frac{(-1)^jt^{2j+1}}{(2j+1)^2},\qquad0<t<1.
$$

Four terms, ending with the negative term $j=3$, give a strict lower bound at $t=2/3$. The inequality $\pi<22/7$ follows, for example, from the positive integral

$$
\frac{22}7-\pi=\int_0^1\frac{x^4(1-x)^4}{1+x^2}\,dx>0.
$$

Hence

$$
\frac2\pi T(2/3)>
\frac7{11}\sum_{j=0}^3\frac{(-1)^j(2/3)^{2j+1}}{(2j+1)^2}
=\frac{155342}{382725}.\tag{6}
$$

For the logarithm, use $\log(3/2)=2\operatorname{artanh}(1/5)$. Its positive series and a geometric tail bound give

$$
\log(3/2)<2\sum_{j=0}^2\frac{(1/5)^{2j+1}}{2j+1}
+\frac{2(1/5)^7}{7(1-1/25)}
=\frac{177391}{437500}.\tag{7}
$$

Subtracting (7) from (6),

$$
F(9/4)-\log(9/4)>
\frac{57269}{136687500}>\frac1{2500}.\tag{8}
$$

Equations (1), (3), (5), and (8) prove (2), including the exact one-zero-outer limit. The estimate does not depend on normalization scale, because the balance gap is scale invariant.

## 4. Interface with an actual symmetric plat construction

Suppose an actual certified source has only the following port types in its one complete marked packing:

- Equal middle curvatures $b=c$, with $A>0$.
- One zero middle and the other $e$ satisfying $e/(x+y)\leq9/4$.

Every such port is balanced. For equal positive middles, this follows from $Q_b(0)>\tfrac12\log b$; if both are zero, the one-sided sectors vanish. For the second type, it follows from (2). The [conditional full-invariant balance theorem](general_complete_radius_balance_filling_volume.md) therefore applies to any literal source for which these actual geometric statements have been proved.

The [reduced-layer family theorem](general_reduced_layer_long_filling_volume.md) establishes the required packing, reflection, original mark and uniform ratio bound for its literal words at every $k\geq4$. Those are separate geometric conclusions, not consequences of the local inequality alone.

## Validation and scope

The bound follows from scalar comparison, monotonicity, exact rational inequalities and protected-zero limits. Numerical quadrature or a sample of diagrams cannot establish its uniformity.