# A global spectral bound for an actual diagonal source sector

Independently reviewed analytical theorem, 31 October 2026. This concerns the original homogeneous face polynomial and its original shared marked coefficient. The triangular-basis diagonal sector is not identified with the identity operator. A coefficientwise inequality reduces its absolute bound to an actual identity-inserted positive source.

## 1. The exact diagonal polynomial and a uniform real bound

Let $N\geq3$, $d=N-1$, and

$$
\chi_N(\sigma)=2T_N(\sigma/2)+2,
\qquad c_j=2\cos\frac{(2j+1)\pi}{N},\quad 0\leq j<N.
$$

In the original triangular face representation, $\Omega$ has diagonal $c_j$ and lowers the face degree by one or two. The zero-step part of its actual resolvent numerator is

$$
\begin{aligned}
V_N(\sigma)&=\chi_N(\sigma)(\sigma-\Omega)^{-1},\\
D_N(\sigma;b,c)&=\sum_{j=0}^{d}d_j(\sigma)b^jc^{d-j},
&d_j(\sigma)&=\frac{\chi_N(\sigma)}{\sigma-c_j}.
\end{aligned}\tag{1}
$$

Every quotient is a polynomial, including all repeated and simple spectral nodes. This is exactly the part of $H_{V_N}$ with zero outer exponents. The middle names $b,c$ and their original orientation are unchanged. It is a restriction of the homogeneous coefficient polynomial, not an assertion that the physical kernel has been diagonalized or made into an identity.

For every real $\sigma\in[-2,2]$,

$$
|d_j(\sigma)|\leq N^2.\tag{2}
$$

Indeed, $\chi_N(c_j)=0$ and the real mean-value integral gives

$$
d_j(\sigma)=\int_0^1\chi_N'\bigl(c_j+t(\sigma-c_j)\bigr)\,dt.
$$

For $z=2\cos\theta$,

$$
\chi_N'(z)=N U_{N-1}(\cos\theta),\qquad
U_{N-1}(\cos\theta)=\sum_{r=0}^{N-1}e^{i(N-1-2r)\theta}.
$$

Its modulus is at most $N$, including the endpoint limits. Thus the removable values are handled automatically, and

$$
|D_N(\sigma)|_{\mathrm{coef}}\leq N^2 H_1(b,c),
\qquad H_1(b,c)=\sum_{j=0}^{d}b^jc^{d-j}.\tag{3}
$$

This is an upper bound, not an equality or a phase-preserving replacement of $d_j$ by $1$. The weight in (1) depends on both $j$ and $\sigma$.

Since $d_j$ has degree $d$, there is also a uniform complex-cover bound:

$$
\bigl|d_j(-2\cos(2\pi\delta))\bigr|
\leq N^2 e^{2\pi d|\operatorname{Im}\delta|}.\tag{4}
$$

For completeness, if a polynomial $p$ of degree $d$ is bounded by $M$ on $[-1,1]$, then $w^{-d}p((w+w^{-1})/2)$ is holomorphic outside the unit disk and at infinity, with boundary modulus at most $M$. The exterior maximum principle gives $|p((w+w^{-1})/2)|\leq M|w|^d$. Apply this with $p(z)=d_j(-2z)$ and $|w|=e^{2\pi|\operatorname{Im}\delta|}$. No division by distance to a spectral node occurs.

## 2. The positive identity-inserted reference at both parities

For the original fixed certified diagram $D$, let $F_N$ denote its actual positive Fejér reference coupon:

$$
F_N=
\begin{cases}
(-1)^dV_N(-2),&N\text{ even},\\
V_N(-2)-N^{-2}V_N'(-2),&N\text{ odd}.
\end{cases}
$$

Fix a nonempty set $I$ of ports carrying the literal identity coupon. Let $Z_{I,N}$ be the original shared marked coefficient with $H_1$ at $I$ and $H_{F_N}$ elsewhere. Every original ordinary target is $d$; the two original protected targets are zero.

The [strict identity-insertion theorem](general_fejer_endpoint_source_volume.md), Section 6, gives at even levels a compact full-flow maximum $W_I<\Phi_D$, where $\Phi_D=\operatorname{Vol}(Y_D)/(2\pi)$, or a zero source when the flow is infeasible. Its proof uses an actual representation of the original drilled group killing an essential deleted auxiliary meridian, together with the canonical general-peripheral volume bound. It does not bound independent pieces with unrelated marks.

The same rate applies at odd levels. This does not differentiate an even identity: the odd regularized coefficient theorem gives the same uniform local full-simplex entropy $h$ for $H_{F_N}$, while $H_1$ has exact coefficient $1$ on its middle edge and zero elsewhere. Removing the two outer arcs at identity ports leaves the same integral bipartite-flow rounding with literal degree $d$. Compact Laplace therefore gives, at both parities,

$$
\lim_{N\to\infty}\frac1N\log Z_{I,N}=W_I<\Phi_D.\tag{5}
$$

If the flow is infeasible, every finite coefficient is zero. This includes an identity edge joining the two protected roots: it cannot supply positive degree $d$ to either zero target. No protected radius is replaced by a positive surrogate.

## 3. Two strict-gap consequences for the actual spectral sectors

First take one port $i$ in the pure-middle diagonal sector (1), with arbitrary $\sigma_i\in[-2,2]$. Allow every other port to retain its full numerator, provided $|\sigma_j+2|\leq r$. The [original unused-row majorant](actual_fejer_spectral_polydisk_complement.md), Section 3, gives

$$
|H_{V_N(\sigma_j)}|_{\mathrm{coef}}\leq M_N(r)H_{F_N},
\qquad M_N(r)\leq\operatorname{poly}(N)e^{N\theta(r)},
\qquad\theta(r)=\operatorname{arcosh}(1+r/2).\tag{6}
$$

At odd levels the factor $\max(1,N^2r)$ in $M_N$ is essential. Bare $H_{V_N(-2)}$ is not an odd majorant. Taking absolute coefficients before multiplying and extracting the one original marked target proves the finite inequality

$$
|Z_{\mathrm{diag}\ i;\,\mathrm{full\ elsewhere}}(\boldsymbol\sigma)|
\leq N^2M_N(r)^{R-1}Z_{\{i\},N}.\tag{7}
$$

Choose fixed $r>0$ so $(R-1)\theta(r)$ is smaller than half the positive gap $\Phi_D-W_{\{i\}}$. Equation (5) gives $\gamma>0$ and $N_0$ such that, uniformly in this region and at both parities,

$$
|Z_{\mathrm{diag}\ i;\,\mathrm{full\ elsewhere}}(\boldsymbol\sigma)|
\leq e^{N(\Phi_D-\gamma)},\qquad N\geq N_0.\tag{8}
$$

If the identity reference is zero, the sector is identically zero. Constants depend on the original fixed diagram. No independently framed norm or unproved physical smoothing has been used.

Second, if all other ports are restricted to their actual CROSS sectors, those ports may range over the entire real spectral interval. The [exact cofactor interpolation theorem](actual_cross_cofactor_factorization.md), Section 8, gives

$$
|P_{N,\mathrm{cross}}(\sigma)|_{\mathrm{coef}}
\leq C\log^2(N+1)P_{N,\mathrm{cross}}(-2)
\leq C\log^2(N+1)H_{F_N},\qquad \sigma\in[-2,2].\tag{9}
$$

Combining (3) and (9) with the same marked extraction gives (8) uniformly over the full real spectral cube. The proof applies to any fixed nonempty collection $I$ of diagonal ports, using $Z_{I,N}$, with CROSS elsewhere. This is an inequality for every original coefficient; it neither identifies the restricted quantum sector with a smoothed representation nor asserts absence of cancellation.

Both conclusions persist on a sufficiently small fixed complex strip in each globally varying $\delta$ coordinate. Equation (4) and the strip version of (9) add at most $2\pi N\sum_j|\operatorname{Im}\delta_j|$ to the exponent. Shrink the strip so this and the cost in (6) fit within the strict gap in (5). Polynomial factors contribute $o(N)$.

## 4. The entire original Fourier period of the diagonal/CROSS sector

Use the global case of Section 3: a fixed nonempty set $I$ is pure diagonal and every other port is CROSS. For a disjoint path partition, remove the odd central zero-step monomial from CROSS and assign it to the diagonal class. This is only a coefficient projection onto positive outer degree, so (9) remains an upper bound. The exact sectors are then disjoint at both parities.

Let $Z_N(\boldsymbol\sigma)$ be this shared sector polynomial. It has degree at most $d$ in each spectral variable. The preceding proof supplies fixed $\tau,\gamma>0$ such that

$$
\left|Z_N\bigl(-2\cos(2\pi\delta_1),\ldots,-2\cos(2\pi\delta_R)\bigr)\right|
\leq e^{N(\Phi_D-\gamma)}\tag{10}
$$

for all large $N$, uniformly when $|\operatorname{Im}\delta_i|\leq\tau$ and for all real parts. Real periodicity follows from the polynomial cosines. Shrink $\tau$ once for Cauchy estimates; it is independent of the crossing powers.

Insert this sector into the exact original Fourier formula, retaining its scalar, charge factors, sine factors and parity. Write

$$
\begin{aligned}
B_N(\boldsymbol\delta)
&=\left(\prod_i\sin(2\pi\delta_i)\right)
 Z_N(-2\cos(2\pi\boldsymbol\delta))
 e^{\pi iN\sum_i n_i\delta_i^2},\\
J_{N,\boldsymbol\ell}
&=\int_{[-1/2,1/2]^R}B_N(\boldsymbol\delta)
 e^{2\pi iN\sum_i\ell_i\delta_i}\,d\boldsymbol\delta.
\end{aligned}
$$

Every $n_i$ is a fixed integer, with independent signs allowed. At either endpoint of coordinate $i$,

$$
B_N|_{\delta_i=\pm1/2}=0,
\qquad
\partial_iB_N|_{\delta_i=1/2}
=\partial_iB_N|_{\delta_i=-1/2}.\tag{11}
$$

The sine vanishes, its derivative is $-2\pi$ at both endpoints, the source sees $\sigma_i=2$ at both, and the Gaussian is $e^{\pi iNn_i/4}$ at both. Only the sine-derivative term survives. These identities persist after derivatives in other coordinates. The Fourier endpoint factor is the same $(-1)^{N\ell_i}$ at both ends.

Three integrations by parts therefore give

$$
\begin{aligned}
J_i=(2\pi iN\ell_i)^{-3}\bigg\{&
\left[\partial_i^2 B_N e^{2\pi iN\ell_i\delta_i}\right]_{-1/2}^{1/2}\\
&-\int_{-1/2}^{1/2}\partial_i^3 B_N
 e^{2\pi iN\ell_i\delta_i}\,d\delta_i\bigg\}.
\end{aligned}\tag{12}
$$

The first two endpoint terms vanish by (11); the second-derivative endpoint difference in (12) is retained. Repeat in every coordinate. The boundary operations commute with the other derivatives and preserve their endpoint identities. There are at most $3^R$ terms, each with at most three derivatives per coordinate and evaluations or integrals over intervals of length one.

Cauchy applied to the source alone in (10) bounds all such fixed-order derivatives by $C_\tau e^{N(\Phi_D-\gamma)}$. On the real cube the Gaussian has modulus one, and its $k$th derivative in coordinate $i$ is bounded by $C_k(1+N|n_i|)^k$. Thus

$$
|J_{N,\boldsymbol\ell}|
\leq C_{D,\tau,R}\left(\prod_i(1+|n_i|)^3\right)
e^{N(\Phi_D-\gamma)}\prod_i|\ell_i|^{-3}.\tag{13}
$$

The derivative cost $N^{3R}$ has canceled the integration-by-parts denominator. No Gaussian growth on the complex strip is used. The entire sector stays on the original whole real cube.

The original charge weights have modulus $\prod_i|\ell_i|$; the parity and original framing scalar have modulus one. Since $\sum_{\ell\ne0}|\ell|^{-2}=\pi^2/3$, the complete charge sum is absolutely bounded by

$$
|I_{N,\mathbf n;\,\mathrm{diag}\ I,\,\mathrm{CROSS\ elsewhere}}|
\leq C_D\left(\prod_i(1+|n_i|)^3\right)e^{N(\Phi_D-\gamma)}.\tag{14}
$$

This includes all charges and the actual second-derivative currents. It is not a sharp-cube localization or separately divergent inside/outside charge sum. Multilinearity of the finite source and fixed-level absolute Fourier convergence justify taking this polynomial sector; (13) additionally proves its uniform summability.

There are finitely many diagonal/CROSS sectors for fixed $D$, so the same conclusion with a smaller gap holds for their union. For sufficiently long fixed independent signed twists, the proved local unit-charge filling rate exceeds $\Phi_D-\gamma/2$. Equation (14) is exponentially smaller than that nonzero local contribution. Constants may grow polynomially with the fixed powers; no joint growing-power/level asymptotic is claimed.

The first case of Section 3, where other full ports are controlled only near $-2$, does not automatically have this whole-period conclusion. Equation (14) explicitly uses the global CROSS bound at every other port.

## 5. Remaining scope and verification

The result is compatible with failure of a global coefficientwise endpoint bound for the full numerator. That failure already occurs at $\sigma=\sqrt3$ for a genuinely one-sided path with positive outer exponent, not for (1). Such a remote moving port is not covered by (9) or a small spectral neighborhood in (6). The [short-moving extension](actual_global_short_moving_spectral_sector_gap.md) treats a separate small outer-degree corridor; it does not exhaust macroscopic one-sided paths.

Root and both independent peers read the complete analytical proof and reported PASS, including the global CROSS comparison, both-parity identity reference, odd central-path projection, source-only strip derivatives and entire charge estimate. The [focused audit](../experiments/audit_actual_global_diagonal_spectral_sector_gap.py) and [recorded results](../experiments/actual_global_diagonal_spectral_sector_gap_results.json) retain the exact finite source.

Author and independent fresh 65-digit replays passed 807 zero-step/divided-Chebyshev checks, 431 removable node values, 94 disjoint parity sectors, and 18 original marked sector polynomials. The four nonzero fixtures supplied 16 one-coordinate, whole-interval three-integration-by-parts identities, all with nonzero second-derivative endpoint currents; maximum relative error was $8.26\times10^{-66}$. Root also reviewed the audit code. These checks supplement the analytical entropy and infinite-charge proofs rather than numerically establish them.
