# A triangle upper bound for every one-sided relative-energy coefficient

31 October 2026. Root derivation for independent review. The proof below is
local and retains the actual full spectral numerator and positive endpoint
reference at both parities. It does not yet prove a shared global energy bound.

## 1. Positive dependence on a single spectral parameter

Write $\theta=\pi/N$, $s_j=2\sin(j\theta)$, and normalize the original tail by

$$
q_{i,j}=K_{i,j}/\prod_{r=i+1}^j s_r^2.
$$

It satisfies $q_{i,i}=1$, $q_{i,i+1}=x+y$, and

$$
q_{i,j}=(x+y)q_{i,j-1}+(\eta_j-1)xyq_{i,j-2},
\quad
\eta_j=\frac{\lambda}{d_j},
\quad d_j=\cos\theta-\cos((2j-1)\theta)>0,
\quad \lambda=\cos\theta+\cos(2\pi\delta).
\tag{1}
$$

The actual start has $j\geq i+2$ in the last term, so no zero sine denominator
occurs. On $0\leq\delta\leq1/2-1/(2N)$, $\lambda\geq0$.

For an interval of length $r=j-i$, expand the continuant in the parameters
$\eta$. A chosen set of disjoint edges contributes $(xy)^{|S|}\prod_{e\in S}\eta_e$.
The remaining vertex intervals contribute their baseline continuants

$$
h_\ell(x,y)=\sum_{k=0}^{\ell}x^ky^{\ell-k},
$$

which solve (1) with $\eta=0$. Thus every outer coefficient
$q_{i,j,k}(\lambda)=[x^ky^{r-k}]q_{i,j}$ is a polynomial in $\lambda$ with
nonnegative coefficients. This expansion follows by grouping the selected
$\eta$ terms in the usual matching expansion of a tridiagonal determinant;
the deleted-edge complements are disjoint intervals.

Let $\lambda_0=1+\cos\theta$. Cauchy applied to these nonnegative polynomial
coefficients gives the exact finite inequality

$$
\frac{q_{i,j,k}(\lambda)^2}{q_{i,j,k}(\lambda_0)}
\leq q_{i,j,k}\left(\frac{\lambda^2}{\lambda_0}\right).
\tag{2}
$$

It is a coefficient inequality for the actual tail. It does not assume real
negative roots or a coefficient central-limit theorem.

## 2. The original prefix and suffix normalization

For the actual LEFT exponent $v=(k,i,d-j,r-k)$, write
$a_N(v;\sigma)=B_N(\delta)q_{i,j,k}(\lambda)$ with $\sigma=-2\cos(2\pi\delta)$.
Here $B_N$ contains the exact omitted-half scalar, all unused lower prefix
and suffix diagonals, and $\prod_{r=i+1}^j s_r^2$. The original endpoint
reference is $p_N(v)=B_N^{\rm ref}q_{i,j,k}(\lambda_0)$, $B_N^{\rm ref}>0$.
At even levels the reference is $-V_N(-2)$; at odd levels it is
$V_N(-2)-N^{-2}\partial_\sigma V_N(-2)$. For a one-sided odd path the
central zero is unused, so the derivative removes precisely that zero;
its remaining normalization has only polynomial size. Bare odd $V_N(-2)$
is not the reference.

Consequently (2) implies

$$
\sum_{k=0}^{r}\frac{|a_N(v;\sigma)|^2}{p_N(v)}x^ky^{r-k}
\leq\frac{|B_N(\delta)|^2}{B_N^{\rm ref}}
 q_{i,j}\left(x,y;\lambda^2/\lambda_0\right).
\tag{3}
$$

All exterior and marked factors remain in $B_N$. We will estimate (3) by
the uniform tail upper bound and logarithmic prefix/suffix estimates in
[the global CROSS proof](actual_global_cross_spectral_gap.md), also used
for arbitrary tail intervals in [the LEFT theorem](actual_global_left_weighted_spectral_envelope.md).

## 3. The effective weighted kernel

Put $\mu=i/N$, $\nu=j/N$, $w=\nu-\mu$, and, for $0<t<1/2$,

$$
s=\sin(\pi t),\quad c=\cos(\pi t),\quad
z=\sin^2(\pi\delta),\quad k_\delta^2=1-z,
\quad A=x+y,\quad \rho=4xy/A^2.
$$

The effective parameter in (2) satisfies
$\cos^2(\pi\delta_{\rm eff})\to k_\delta^4$ uniformly in $\delta$.
The exact finite parameter stays in the original positive-tail range.
Define

$$
\Lambda_{\rm eff}(t)=2s\left[As+
 \sqrt{(x-y)^2s^2+4xy k_\delta^4}\right],
\qquad \alpha_\delta(t)=4(c^2-z).
$$

The uniform transfer upper bound, the upper Riemann bounds for both unused
products, and the uniform positive reference estimate yield the weighted
upper action

$$
\int_\mu^\nu\log\mathcal L_\delta(t;x,y)\,dt,
\qquad
\mathcal L_\delta=
 \frac{\Lambda_{\rm eff}\alpha_0}{|\alpha_\delta|^2}.
\tag{4}
$$

This rewriting uses $\int_0^{1/2}\log|\alpha_\delta|=0$ only AFTER estimating
the actual unused products. No finite division at a spectral zero is made.
The tail estimate is uniform in both endpoints and the real spectral
parameter, including the repeated-root case. The logarithmic errors are
$o(N)$ uniformly, at fixed positive $x,y$ in a compact set.

Let

$$
R_\delta(t)=\frac{sc}{c^2-z}
 =\frac{\sin(2\pi t)}{\cos(2\pi t)+\cos(2\pi\delta)},
\qquad B_\rho(v)=\frac{1+\sqrt{1-\rho+\rho v^2}}2.
$$

A direct simplification of (4) gives

$$
\mathcal L_\delta=A R_\delta^2 B_\rho(k_\delta^2/s).
\tag{5}
$$

The complete positive half-block root is

$$
L_0(t;x,y)=A\tan^2(\pi t)B_\rho(1/\sin(\pi t)).
\tag{6}
$$

It is strictly increasing in $t$ and its logarithm is integrable.

## 4. An elementary rearrangement

Define $t'=\pi^{-1}\arctan|R_\delta(t)|\in[0,1/2]$. The algebraic identity

$$
(c^2-z)^2+s^2c^2-k_\delta^4c^2=z^2s^2\geq0
\tag{7}
$$

implies $k_\delta^2/s\leq1/\sin(\pi t')$. Since $B_\rho$ is nondecreasing,

$$
\mathcal L_\delta(t;x,y)\leq L_0(t';x,y).
\tag{8}
$$

The map $t\mapsto t'$ preserves the uniform distribution on $[0,1/2]$.
To prove this, set $\vartheta=2\pi t$, $a=\cos(2\pi\delta)$ and
$\varphi=\arg(e^{i\vartheta}+a)$. For $|a|<1$ this angle increases from
$0$ to $\pi$, and

$$
\vartheta=\varphi+\arcsin(a\sin\varphi).
$$

The set $|R_\delta|>r$ has endpoint angles $\varphi_1=\arctan r$ and
$\varphi_2=\pi-\arctan r$. Their arcsine corrections agree. Its length in
$t$ is therefore $1/2-\pi^{-1}\arctan r$, exactly the distribution of
$\tan(\pi t)$. The endpoint cases are $t'=t$ and $t'=1/2-t$.

For any measurable set of length $w$, the integral of an increasing
function of a uniformly distributed $t'$ is at most its upper-tail integral
of length $w$. Apply this elementary rearrangement to the interval
$[\mu,\nu]$ and to $\log L_0$, using truncation for its integrable endpoint
singularities. Equations (8) and the distribution identity prove

$$
\boxed{\displaystyle
\int_\mu^\nu\log\mathcal L_\delta(t;x,y)\,dt
\leq\int_{1/2-w}^{1/2}\log L_0(t;x,y)\,dt.}
\tag{9}
$$

## 5. The coefficient consequence and its current scope

Write $\xi=k/N$. Weighted coefficient extraction in (3), (9), and the
original complete-triangle Legendre formula give

$$
\limsup\frac1N\log\frac{\sup_{\sigma\in[-2,2]}|a_N(v;\sigma)|^2}{p_N(v)}
\leq C(\xi,w-\xi,1/2-w).
\tag{10}
$$

The statement is uniform on the entire closed one-sided simplex. For this,
first choose a finite outer tilt within any prescribed error at each
limiting degree, use continuity of the triangle entropy to obtain a finite
cover, and apply the uniform weighted estimates to these finitely many
positive tilts. This includes outer degree zero and collapsing intervals.
The omitted final spectral cap has width $O(N^{-2})$ in $\sigma$; the
polynomial Bernstein bound for each actual coefficient adds only $O(1)$
to its logarithmic supremum. Both parity reference normalizations are kept.
RIGHT follows by the original row reflection. If a protected outer is zero,
only its exponent-zero coefficients survive, and the already derived sharp
boundary formula attains (10).

The middle degrees remain $\mu$ and $1-\nu$ in the ORIGINAL shared flow.
Although the entropy bound depends only on the two outer degrees, it is
not permission to reassign middle loads independently. The global energy
comparison still requires a proof using the original shared targets.
