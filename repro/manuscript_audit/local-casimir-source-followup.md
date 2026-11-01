# The local Casimir and the full crossing functional

This bounded follow-up records the finite algebra used by Appendix N.
The base commit is `2301771b66296cb7f2331938f1bfe0855719dd3d`;
the companion snapshot pins the subsequently added Fourier proof and checker.
It does not validate the manuscript's global analytic or volume arguments.

## 1. Which operators are compared

Let $N\ge2$, $d=N-1$, $q=e^{\pi i/N}$, $Q=q^2$, and
$\rho=q-q^{-1}$. The original color has
$Kv_j=q^{d-2j}v_j$, $Fv_j=v_{j+1}$, and
$Ev_j=[j]_q^2v_{j-1}$, where
$[j]_q=(q^j-q^{-j})/\rho$; missing endpoint vectors are zero.
The pair Casimir is
$$
\Omega=\rho^2(\Delta F)(\Delta E)+q\Delta K+q^{-1}(\Delta K)^{-1},
$$
with $\Delta E=E\otimes K+1\otimes E$,
$\Delta F=F\otimes1+K^{-1}\otimes F$, and $\Delta K=K\otimes K$.
Write $B=P\mathcal R$ for the checked crossing, where $P$ exchanges
factors and $\mathcal R$ is the specified finite universal matrix.
The direct-power source note denotes this checked crossing by $R$.

The [original crossing comparison](../../notes/kashaev_crossing_and_period_lattice.md)
keeps its transpose, Fourier gauges, enhancement, and actual inverse.
The [self-dual comparison](../../notes/kashaev_ado_pointing.md), §2,
uses $Jv_j=(-1)^jq^{j(j-N)}v_{d-j}$ and sends $K$ to $K^{-1}$.
Its entrywise Cartan identity is
$(H_jH_k-H_{j+a}H_{k-a})/2=2a(j-k+a)$, with $H_j=d-2j$.
Thus changing between these two conventions does not omit a pivot.

## 2. Two proofs of the physical annihilator

The older [Casimir proof](../../notes/casimir_braiding_and_recoupling_lattice.md),
§3, decomposes the generic $N$-dimensional tensor product into the
highest-weight summands of dimensions $2N-1-2k$, $0\le k<N$.
Their distinct Casimir eigenvalues are
$c_k(z)=z^{2N-1-2k}+z^{-2N+1+2k}$, and the dimensions sum to $N^2$.
Consequently $\prod_k(X-c_k(z))$ annihilates the generic pair matrix.
The matrix and polynomial coefficients are regular at $z=q$; specialization gives
$$
\chi_N(\Omega)=0,\qquad
\chi_N(X)=\prod_{j=0}^{N-1}(X-q^{2j+1}-q^{-2j-1})=2T_N(X/2)+2,
$$
where $T_N$ is the first-kind Chebyshev polynomial.
This argument does not specialize an inverse singular recoupling matrix.
Nor does it assert that the physical pair module is cyclic.

The new direct proof is in
[Appendix N](../../manuscript/sections/N-uniform-filling-bound.tex),
labels `uf:local-fourier` and `prop:local-face-fourier`.
In the balanced basis $e_i=v_i/(Q;Q)_i$, where
$(Q;Q)_i=\prod_{j=1}^i(1-Q^j)$, the scaled operator
$\mathcal E=\rho^2E$ has coefficient $Q^{-i}-1$;
$F$ has coefficient $1-Q^{i+1}$.
This follows from $\rho^2[i]_q^2/(1-Q^i)=Q^{-i}-1$.

For a residue $s$, order the physical block by
$e_u\otimes e_{[s-u]_N}$, $0\le u<N$.
Set $x=Q^{s+1}y$, $y\ne0$, $b_u=-q^{-1}xQ^{-u}$,
$\mathsf E_{uj}=b_u^j$, and $G_{uu}=q^{du}$.
For the displayed polynomial face operator $T$, direct substitution proves
$$
\mathsf E T\mathsf E^{-1}=-G^{-1}\Omega_s^{\mathsf T}G.
$$
The diagonal of $-T$ gives $\chi_N$ by Cayley–Hamilton.
The four physical endpoint zeros kill wraps before this conjugacy is used.
Moreover $(\mathsf E^{-1})_{jr}=N^{-1}b_r^{-j}$ gives the exact
homogeneous adapter in `uf:physical-local-adapter`, including its $N^{-1}$.
The displacement is the integer $r-u$: at even levels replacing it
by a residue can change the sign of $q^{-d(r-u)}$.

## 3. Repeated nodes determine the crossing's normal data

In the generic calculation the crossing eigenvalue is
$\lambda_k(z)=(-1)^kz^{d^2/2-k(2N-1-k)}$.
Put $h=2k+1<N$, $l=N-1-k$, and $A=q^h-q^{-h}\ne0$.
At $q$, the colliding values agree; their logarithmic derivatives satisfy
$$
(c_k-c_l)'=-2NA,\qquad
(\lambda_k-\lambda_l)'=\lambda_k(q)N(N-h).
$$
The resulting confluent Vandermonde system is invertible. Hence its
coefficients are regular, and the whole matrix identity specializes to
$$
B=\lambda_0r_N(\Omega),\quad \lambda_0=q^{d^2/2},\qquad
r_N(c_k)=\nu_k=(-1)^kq^{k(k+1)},\quad
r_N'(c_k)=-\nu_k\frac{N-h}{2A}.
$$
At odd $N$, $-2$ is simple and has only a value condition.
All $\nu_k$ are nonzero, so inverse crossings and every integer power
retain the derivative multiplier $n\,r_N'(c_k)/r_N(c_k)$.
Nodal values alone would not prove this matrix identity.

The [direct-power Gaussian](../../notes/actual_direct_long_power_source.md), §3,
matches both these values and derivatives, using the prescribed branch
of $K(z)=\operatorname{arccosh}(-z/2)^2$ on
$\mathbb C\setminus[2,\infty)$ and $\hbar=2\pi i/N$:
$B^n=q^{nd^2/4}\exp(nK(\Omega)/(2\hbar))$.
This is fixed-root functional calculus, including the nilpotent part.

## 4. Pivotal and filling functionals

Define $\Phi_N(f)I=\operatorname{tr}_2((1\otimes K)f(\Omega))$.
Coproduct intertwining and trace cyclicity make this a scalar on the
simple original color. The generic full pivotal trace gives
$[N]_z\Phi_z(f)=\sum_k[2N-1-2k]_z f(c_k(z))$.
Dividing the paired first-order zeros by $[N]_z$ gives
$$
\Phi_N(f)=-\sum_{2k+1<N}\{c_kf(c_k)+(c_k^2-4)f'(c_k)\}
 +\mathbf1_{N\text{ odd}}f(-2).
$$
The unpaired odd term is exactly $[N]_zf(z^N+z^{-N})$ before division.
The positive and negative crossing partial traces are
$\alpha_N^{\pm1}$, where $\alpha_N=q^{(N^2-1)/2}$.
Thus $\lambda_0/\alpha_N=-q$ is the retained writhe character.

For the degree-$d$ resolvent numerator
$V_N(z)=\chi_N(z)(z-\Omega)^{-1}$, the actual multiplier functional is
$\mathcal L_N^f(H)=\ell_{\chi_N}(\widetilde fH)=N^{-2}\Phi_N(\widetilde fH)$.
Here $\ell_{\chi_N}$ takes the top coefficient of the canonical remainder,
and $\widetilde f$ is the full Hermite multiplier.
It sends $V_N$ to $f(\Omega)$.
This correspondence retains the odd weight $1/N^2$ and every double-root derivative.
The untwisted functional alone, or a scalar normalization alone,
does not implement arbitrary crossing powers.

## 5. What was checked and what remains separate

The review independently derived the generic collision, pivotal quotient,
self-dual entry relation, Gaussian values and derivatives, and Fourier signs.
A private exact symbolic calculation also checked six rational identities,
including the auxiliary face-kernel commutator; it sampled no levels.
No mathematical correction to these finite inputs was identified.

The [local Fourier checker](../check_local_face_fourier.py) was read, not
rerun in this review. It constructs the physical matrix from its coproduct,
separately from the face matrix, and tests a multiplier of degree $N+1$,
wrong-total zeros, and an intentionally incorrect even-level residue phase.
The recorded run has 154 residue blocks and 12,166 entries over two finite
fields at each $N=2,\ldots,12$. These are bounded checks of the written proof,
not an all-level proof by extrapolation.

The local argument uses only primitivity, not primality or oddness.
It does not commute Casimirs at different boxes. The global marked
coefficient identity, complex interpolation bounds, signed remainder,
nonzero geometric contribution, and hyperbolic completion remain separate
written dependencies. No finite check here proves any of those analytic
or geometric statements.
