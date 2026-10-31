# Exact homogeneous insertion for a far-charge coupon, and why it is not an identity insertion

, 31 October 2026. This accompanies the [whole-domain large-charge theorem](actual_whole_domain_large_charge_tail.md). It supplies an exact
source coefficient bound, not a shared volume or capacity theorem.

## 1. The full face-grid transform gives a coefficient bound

For ANY actual fixed-root Casimir coupon $F=f(\Omega)$, with the complete
Hermite data retained, its homogeneous kernel has degree $d=N-1$:

$$
H_F(x,b,c,y)=\sum_{a+i+t+s=d}h_{a,i,t,s}\,x^ab^ic^ty^s.
$$

Set $c=1$ and sample the THREE independent original clock cosets

$$
b=Q^p,\qquad x=-qQ^r,\qquad y=-q^{-1}Q^s,\qquad0\leq p,r,s<N.
$$

The actual input clocks $U=-q^{-1}x/b$ and $V=-q^{-1}b/y$ are respectively
$Q^{r-p},Q^{p-s}$, and the output relation $c=Q^{-p}b$ is literal.
Write canonical physical heads $u=[r-p]_N$, $v=[p-s]_N$,
$R=r$, $S=[-s]_N$, and retain the TRUE integer displacement $\Delta=R-u$.
The [original local matrix/grid identity](actual_homogeneous_casimir_face_source.md) therefore says

$$
H_F(-qQ^r,Q^p,1,-q^{-1}Q^s)=Nq^{d\Delta}F_{R,S;u,v}.\tag{1}
$$

Although $\Delta$ is congruent to $p$ modulo $N$, their phase ratio is
$(-1)^{d(\Delta-p)/N}$, which cannot be dropped at even levels.
For example $N=4$, $p=3$, $r=0$, $s=1$ has $u=1$, $v=2$, $R=0$, $S=3$ and
$\Delta=-1$, a valid nonzero transition with the opposite carry sign.

If canonical representatives violate unwrapped total conservation,
the right side is zero, exactly as is the left side by the original
physical endpoint factors. No nonphysical wrap is inserted.
All coset and $q$ factors in (1) have modulus one, at both parities.

Every exponent of $H_F(x,b,1,y)$ is between $0$ and $d<N$. Its coefficients
are thus recovered WITHOUT aliases by the three-dimensional inverse
DFT on this grid, with the fixed coset phases removed. Consequently

$$
|h_{a,i,t,s}|\leq N\max_{\mathrm{physical\ entries}}|F_{\mathrm{entry}}|
\leq N\|F\|_{\mathrm{op}}.\tag{2}
$$

The remaining exponent $t=d-a-i-s$ is fixed by homogeneity. In particular
this is not an estimate that loses an exponential basis conversion.
It uses the SAME original balanced physical tensor basis as the
endpoint and Fourier-tail theorems.

Let $h_d(x,b,c,y)=\sum_{a+i+t+s=d}x^ab^ic^ty^s$ denote the complete
homogeneous polynomial with all coefficients $1$. Then

$$
|H_F|_{\mathrm{coef}}\preceq N\|F\|h_d.\tag{3}
$$

An entire spectral function of $\Omega$ still reduces to its unique
finite Hermite polynomial, so (1)-(3) apply to the absolutely summed
far-charge coupon $T_{N,n;M}$ as well. Combined with the tail theorem,
for $M=\lceil|n|/2+1+D\rceil$,

$$
|H_T|_{\mathrm{coef}}\preceq e^{N\varepsilon(D)+o(N)}h_d.\tag{4}
$$

with the horizontal tail already made decreasing. The $o(N)$ is uniform
in $N$ for each fixed $n,D$. No arbitrary face radius has replaced an
original marked coefficient.

## 2. The precise partial-source coefficient family

Insert $T_i$ on a nonempty subset $S$ and keep the exact original $R_j^{n_j}$
on its complement. Multilinearity gives the finite identity

$$
Z=\sum_{\substack{\kappa_i\in\mathbb Z_{\geq0}^4,\ |\kappa_i|=d\\i\in S}}
\left[\prod_{i\in S}h_{T_i}(\kappa_i)\right]
\left[L^{\,\mathbf d-\sum_{i\in S}\kappa_i}\right]
\prod_{j\notin S}H_{R_j^{n_j}}.\tag{5}
$$

Here $\mathbf d$ is the original target vector, and each $\kappa_i$ is extended by zero to the other original faces. Terms
with any negative target, including a positive allocation to either
protected zero face, are zero. There are at most $O(N^{3|S|})$ terms.
Thus (4) bounds this source by a polynomial number of the ACTUAL
shifted-target coefficients in (5), with an arbitrarily small extra
rate $\sum_i\varepsilon(D_i)$. Those shifted coefficients, with their original
signed phases, are the remaining source-specific problem.

The fixed-radius growth of $h_d$ is $\log\max(x,b,c,y)$, because its number
of monomials is polynomial in $N$. It is not $\log\max(b,c)$, the rate of
$H_1$. In particular (4) is NOT an identity-insertion or smoothing theorem.

## 3. Full Fejer entropy is not everywhere nonnegative

A proposed shortcut would replace a port by $h_d$, note its entropy $0$,
and appeal to nonnegativity of the removed full Fejer entropy $h$.
That nonnegativity is false for an ACTUAL coefficient.

At even $N=2m$ let $a_r=4\cos^2((r+1/2)\pi/N)$, $s_j=2\sin(j\pi/N)$, and
$P=(-1)^d H_{V_N(-2)}$. The monomial $x^jc^{d-j}$, with $b=y=0$ and
$0\leq j<m$, comes from the unique all-one-step path from $j$ to $0$. Since
$\prod_{r=0}^d a_r=4$, its exact coefficient is

$$
[x^jc^{d-j}]P=\frac{4\prod_{r=1}^j s_r^2}{\prod_{r=0}^j a_r}.\tag{6}
$$

Take $j/N\to\nu\in(0,1/2)$. The integrable endpoint Riemann sums give

$$
\lim_{N\to\infty}\frac1N\log\bigl([x^jc^{d-j}]P\bigr)
=2\int_0^\nu\log\tan(\pi t)\,dt=E(0,\nu,\nu)<0.\tag{7}
$$

The integral decreases until $\nu=1/4$ and returns to $0$ only at $1/2$.
At $\nu=1/4$ its value is $-2G/\pi$, where $G$ is Catalan's constant. This is the established CLOSED
half-block coefficient entropy and the actual one-sided branch of $h$;
there is no omitted source scalar. Replacing (6) by coefficient $1$ of
$h_d$ increases this local entropy. The endpoint maximum's uniqueness
therefore does not by itself imply a strict gap after an $h_d$ insertion.
This is a local obstruction to THAT comparison, not a global source
counterexample.

## 4. The far-charge endpoint functional is not scalar identity

There is also a direct phase-preserving fixed-$N$ check. Keep $N,n$ fixed,
$n\ne0$, and let $\ell$ tend to positive infinity. For the exact whole-
interval $B_{N,n}$ in the tail note,

$$
\begin{aligned}
B(1/2)&=B(-1/2)=0,\qquad B'(1/2)=B'(-1/2),\\
B''(1/2)-B''(-1/2)&=-8\pi^2inN e^{\pi inN/4}V_N(2).
\end{aligned}\tag{8}
$$

The source is odd in $\delta$, so its third derivatives also agree at the
two endpoints. Five integrations by parts, keeping all endpoint terms,
yield

$$
\begin{aligned}
J_{N,n,\ell}&=(-1)^{N\ell}e^{\pi inN/4}\frac{nV_N(2)}{\pi N^2\ell^3}
+O_{N,n}(\ell^{-5}),\\
F_{N,n,\ell}&=q^{nd^2/4}e^{\pi inN/4}
\left[-\frac{in(-1)^\ell V_N(2)}{\pi N^2\ell^2}\right]+O_{N,n}(\ell^{-4}).
\end{aligned}\tag{9}
$$

Using the exact sign-charge equality and the elementary alternating
tail sum, this also gives

$$
T_{N,n;M}=q^{nd^2/4}e^{\pi inN/4}
\left[-\frac{in(-1)^{M+1}V_N(2)}{\pi N^2M^2}\right]+O_{N,n}(M^{-3}).\tag{10}
$$

These limits are ONLY $\ell$ or $M\to\infty$ at fixed $N$; they are not
interchanges with the level limit in (4). They identify the actual
endpoint coupon:
$V_N(2)=4(2-\Omega)^{-1}$, rather than $I$. For example the one-step $xc^{d-1}$ coefficient is a nonzero
negative step weight times a product of positive factors $2-c_r$. Thus
$H_{V_N(2)}$ has nonzero outer powers, and (10) gives the same nonzero
outer coefficient for every sufficiently large $M$ at fixed $N,n$. Therefore literal coefficientwise domination by a
multiple of $H_1$, whose outer powers vanish, cannot hold for every far
coupon. The correct possible next step is a source-specific bound for
these near-+2 coupons and shifted targets, not replacement by identity.

## Validation and scope

The finite carry check uses the actual original Casimir entry; it is not a new large-level estimate. The fixed-level large-charge limits in (9)–(10) are never interchanged with the level limit. For the complete entropy range and the remaining insertion problem, see the [entropy-sign theorem](actual_fejer_entropy_signs_and_tail_insertion.md).