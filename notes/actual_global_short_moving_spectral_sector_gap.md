# A global spectral gap for short-moving source sectors

Independently reviewed analytical theorem, 31 October 2026. This retains the actual
full numerator, original two protected targets and entire Fourier
period. It extends the reviewed diagonal/CROSS sector lemma to a fixed
small outer-degree corridor. It does not bound remote one-sided paths
of arbitrary macroscopic displacement.
Here "moving" refers to the original triangular face path degree;
it is not an identification with physical input/output head displacement.

## 1. Exact path divided differences, including repeated nodes

Write $d=N-1$, $\chi_N(\sigma)=2T_N(\sigma/2)+2$ and
$c_j=2\cos((2j+1)\pi/N)$. In the original triangular face path expansion,
a path from $j$ to $i$ has $k$ one- or two-row steps, displacement

$$
D=j-i,\qquad k\leq D\leq2k,
$$

and $k+1$ distinct visited row indices $v_0,\ldots,v_k$. Its scalar factor is

$$
\prod_{r\ \mathrm{not\ visited}}(\sigma-c_r)
=\chi_N[c_{v_0},\ldots,c_{v_k},\sigma].\tag{1}
$$

The right side is the divided difference of order $k+1$. Repeated
spectral values among the $c_{v_l}$ mean the exact Hermite divided
difference. The identity remains polynomial at all removable nodes:
$\chi_N$ vanishes with at least the required multiplicity at the listed
nodes, so Newton's divided-remainder identity proves (1). It also
follows by polynomial division, with no inverse spectral gap.

For real $\sigma\in[-2,2]$, the iterated fundamental theorem of calculus
on the divided-difference simplex bounds (1) by

$$
\frac{\sup_{[-2,2]}|\chi_N^{(r)}|}{r!}
=\frac{2N}{N+r}\binom{N+r}{2r},\qquad r=k+1.\tag{2}
$$

Here is an elementary proof of the derivative value used in (2).
Each derivative of $T_N$ has nonnegative Chebyshev coefficients, since
$T_j'=jU_{j-1}$ and $U_{j-1}$ is a nonnegative sum of cosine characters.
Therefore its absolute maximum on $[-1,1]$ occurs at $1$. Differentiating
$(1-z^2)T_N''-zT_N'+N^2T_N=0$ at $z=1$ gives

$$
T_N^{(r)}(1)=\frac{N^2\prod_{a=1}^{r-1}(N^2-a^2)}{(2r-1)!!}.
$$

The scaling $\chi_N(\sigma)=2T_N(\sigma/2)+2$ and division by $r!$ give
(2). The divided-difference simplex has volume $1/r!$, including the
limit of coincident nodes, so the same bound applies there.

The remaining original step weights have absolute value at most $4$.
A one-step move contributes a multiple of $x+y$; a two-step move a
multiple of $xy$. There are at most $2^D$ compositions of $D$ into steps $1,2$,
and each path's chosen outer coefficient is at most $4^k2^k\leq8^D$.
The total coefficient of any monomial $x^ab^ic^{d-j}y^{D-a}$ is
therefore bounded by

$$
2\cdot16^D\left[\frac{e(N+D+1)}{2D+2}\right]^{2D+2}.\tag{3}
$$

Indeed $\binom{N+r}{2r}\leq[e(N+r)/(2r)]^{2r}$, and this last expression
is increasing for $1\leq r\leq N$: its logarithmic derivative is
$2\log((N+r)/(2r))+2r/(N+r)>0$. This applies with $r\leq D+1\leq N$.
No cancellation among different paths is required for the upper bound.

For $0<\eta<1$, let $L_{N,\eta}$ be the exact coefficient projection of
$H_{V_N}$ onto outer degree $a_x+a_y\leq\lfloor\eta d\rfloor$, and put

$$
T_{N,\eta}
=\sum_{\substack{|\mathbf a|=d\\a_x+a_y\leq\lfloor\eta d\rfloor}}
x^{a_x}b^{a_b}c^{a_c}y^{a_y}.
$$

All coefficients of $T$ are $1$. Equations (1)--(3) prove uniformly over
the whole real interval

$$
\begin{aligned}
|L_{N,\eta}(\sigma)|_{\mathrm{coef}}&\leq K_{N,\eta}T_{N,\eta},\\
\limsup_{N\to\infty}\frac1N\log K_{N,\eta}&\leq\omega(\eta),\\
\omega(\eta)&=\eta\log16+2\eta\log\frac{e(1+\eta)}{2\eta}
\longrightarrow0.
\end{aligned}\tag{4}
$$

One can take $K$ to be the right side of (3) at $D=\lfloor\eta d\rfloor$.
Every coefficient polynomial has spectral degree at most $d$. Thus
the exterior-circle maximum-principle argument of the diagonal lemma
extends (4) to $\sigma=-2\cos(2\pi\delta)$, multiplying its right side by
$e^{2\pi d|\operatorname{Im}\delta|}$. Both parities, the central odd row and all
repeated spectral nodes are included in these polynomial identities.

## 2. Shared target continuity, rather than an identity reset

Fix the actual certified diagram $D$ and a nonempty set $I$ of ports.
At $I$ take the projection $L_{N,\eta}$; elsewhere take the exact CROSS
projection. Keep the original ordinary targets $d$ and protected
targets $0$. The global CROSS coefficient bound from the reviewed
[cofactor interpolation lemma](actual_cross_cofactor_factorization.md) is

$$
|P_{\mathrm{cross}}(\sigma)|_{\mathrm{coef}}
\leq C\log^2(N+1)H_{F_N},
$$

on the real interval, where $F_N$ is the actual even positive endpoint
or odd regularized Fejer reference. Its strip version has the same
degree-$d$ exponential factor as (4). Hence the absolute original
sector is bounded by $K_{N,\eta}^{|I|}[C\log^2(N+1)]^{R-|I|}$ times

$$
[\text{original targets}]\,
\prod_{i\in I}T_{N,\eta;i}\prod_{j\notin I}H_{F_N;j}.\tag{5}
$$

The comparison does not change the positive outer degrees into zero.
They remain in (5) with the exact shared incidences and protected
targets. In particular, it does not apply the old identity theorem
to a finite shifted target or to a physically different coupon.

Let $\mathcal P_I(\eta)$ be the compact continuous flow polytope on the original
port-to-face incidence graph: each port supplies $1$, each ordinary
face demands $1$, each protected face demands $0$, and at a port in $I$
the total outer load is at most $\eta$. Let

$$
W_I(\eta)=\max_{\mathbf q\in\mathcal P_I(\eta)}
\sum_{j\notin I}h(\mathbf q_j).\tag{6}
$$

with value minus infinity for an empty polytope. Here $h$ is precisely
the [continuous full-simplex local entropy](actual_fejer_full_kernel_entropy_identity_reduction.md) of $H_{F_N}$, the same at
both parities. Selected ports have entropy zero because $T$ has
coefficient $1$. The uniform local coefficient theorem, and the
polynomial number of degree-$d$ monomial assignments for fixed $D$,
give the upper bound

$$
\limsup_{N\to\infty}\frac1N\log\bigl(\text{coefficient in (5)}\bigr)
\leq W_I(\eta).\tag{7}
$$

Only an upper bound is needed: no boundary rounding or eventual
fixed-label feasibility is asserted here. Normalize the integer
exponents by $d$, retaining the exact face balances; replacing $d/N$
by $1$ is uniform because $h$ is continuous on its compact simplex.

At $\eta=0$ this is exactly the identity-inserted compact flow problem,
so $W_I(0)<\Phi_D=\operatorname{Vol}(Y_D)/(2\pi)$ by the [proved strict identity theorem](general_fejer_endpoint_source_volume.md)
for the original drilled group. Moreover

$$
W_I(\eta)\longrightarrow W_I(0)\qquad\text{as }\eta\downarrow0.\tag{8}
$$

To see this, take a convergent subsequence of maximizers in the
nested compact polytopes. Its limit lies in $\mathcal P_I(0)$; continuity of
the entropy gives the upper inequality, and inclusion gives the
reverse inequality. If $\mathcal P_I(0)$ is empty, compactness instead implies
$\mathcal P_I(\eta)$ is empty for every sufficiently small $\eta$.

Combining (4),(7),(8), choose a fixed $\eta_D>0$ so

$$
W_I(\eta_D)+|I|\omega(\eta_D)<\Phi_D-2\gamma_D.\tag{9}
$$

There are finitely many nonempty $I$, so $\eta_D$ and $\gamma_D$ can be
chosen for all of them at once, ignoring identically zero cases.
Shrinking a fixed complex $\boldsymbol\delta$ strip absorbs $2\pi\sum_j|\operatorname{Im}\delta_j|$.
For all sufficiently large $N$, at both parities the sector satisfies

$$
\left|Z_{I,\eta_D;\mathrm{cross}}(-2\cos(2\pi\boldsymbol\delta))\right|
\leq e^{N(\Phi_D-\gamma_D)}.\tag{10}
$$

uniformly on that strip. Constants depend on the original fixed
diagram, independently of the eventual fixed signed crossing powers.

## 3. Whole original period and precise remaining scope

The sector in (10) is still a polynomial of spectral degree at most
$d$ in every coordinate. The three-integration-by-parts argument of
[the global diagonal/CROSS sector theorem](actual_global_diagonal_spectral_sector_gap.md), §4, therefore
applies verbatim to its entire original Fourier period. In particular,
sine factors give $B(\pm1/2)=0$ and matching first derivatives; the
second-derivative endpoint current is retained. Cauchy differentiates
the source on its fixed strip, while the Gaussian is differentiated
only on the real cube. Summing all nonzero integer charges with the
actual charge weights gives

$$
\left|I_{N,\mathbf n;\,\mathrm{short}\ I,\,\mathrm{cross\ elsewhere}}\right|
\leq C_D\prod_j(1+|n_j|)^3e^{N(\Phi_D-\gamma_D)}.\tag{11}
$$

Thus a fixed small outer-degree corridor, including genuinely moving
near-diagonal paths, is exponentially negligible relative to the
[proved local unit-charge contribution](general_localized_unit_charge_filling_period.md) for independently sufficiently
long fixed signed twists. No sharp local cube splits an infinite
charge sum. If disjoint sectors are required, project overlapping
classes further; coefficient projections preserve every upper bound.

This does not control a macroscopic one-sided path whose outer load
stays outside this small corridor. In particular the known $\sigma=\sqrt3$
counterexample with outer load tending to $1/4$ is compatible with (11).
Nor does the statement bound a partial-far-charge source with an
uncontrolled original $R^n$ coupon at another port. Those remain
separate global phase-sensitive questions.

## Scoped verification

Root and an independent peer read the complete analytical proof and
reported PASS: the repeated-node divided differences, scaled endpoint
derivative formula, actual path/coefficient counts, truncated original
support, compact upper-capacity continuity, both parities, fixed complex
strip and entire all-charge consequence were checked. The finite-source
endpoint/IBP audit of the preceding diagonal lemma remains its relevant
audit dependency; no numerical test is claimed to prove the compactness
or infinite-charge steps here. The promotion changes only mathematical typesetting and dependency links.
