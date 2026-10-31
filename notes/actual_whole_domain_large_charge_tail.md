# Whole-domain large Fourier charges: exact paired currents and a vanishing-rate operator tail

, 31 October 2026. This concerns the actual fixed-root
operator coupons and their original marked contraction. It does not split
an infinite charge series at an artificial real cutoff. Twists are fixed
before $N$. The resulting all-far-sector bound is proved; a partial-far
mixed-source estimate is isolated explicitly in Section 5.

## 1. Original one-port Fourier coupons

Put $d=N-1$, $q=e^{\pi i/N}$, $\Omega$ equal to the original pair Casimir,
$\chi_N(z)=2T_N(z/2)+2$ and $V_N(z)=\chi_N(z)(z-\Omega)^{-1}$, interpreted as
its degree-$d$ polynomial. Work in the original balanced physical basis
used by the [full endpoint-resolvent theorem](actual_casimir_endpoint_resolvent_bound.md), including its high-total
adapter. All physical degrees form its orthogonal direct sum.
For a fixed integer $n$ define

$$
\begin{aligned}
B_{N,n}(\delta)&=\sin(2\pi\delta)e^{\pi i nN\delta^2}V_N(-2\cos(2\pi\delta)),\\
J_{N,n,\ell}&=\int_{-1/2}^{1/2}B_{N,n}(\delta)e^{2\pi i\ell N\delta}\,d\delta,\\
F_{N,n,\ell}&=q^{nd^2/4}(-i)\ell(-1)^{(N+1)\ell}J_{N,n,\ell}.
\end{aligned}
$$

The [exact full-Hermite formula](actual_spectral_total_derivative_source.md) gives

$$
R^n=\sum_{\ell\in\mathbb Z\setminus\{0\}}F_{N,n,\ell}.\tag{1}
$$

The series is absolutely convergent for each fixed $N,n$. Its endpoint
regularity is that of the WHOLE interval. Since $B$ is odd, $J_{-\ell}=-J_\ell$;
therefore $F_{-\ell}=F_\ell$, including the original parity character.
There is no $\ell=0$ term. For integer $M\geq1$ put

$$
T_{N,n;M}=\sum_{|\ell|>M}F_{N,n,\ell}.\tag{2}
$$

This is a literal operator in the actual Casimir quotient, not an
auxiliary scalar source or a truncated physical head sum.

## 2. Exact contour shift and the paired endpoint current

For positive $\ell$ shift the WHOLE interval vertically UP to height $\tau>0$.
The integrand is entire. If $H_{N,n,\ell;\tau}$ denotes the upper horizontal
integral, the two actual side currents give

$$
\begin{aligned}
J_{N,n,\ell}={}&H_{N,n,\ell;\tau}\\
&-i(-1)^{N\ell}\int_0^\tau e^{-2\pi\ell Nv}
\left[B_{N,n}\!\left(\tfrac12+iv\right)-B_{N,n}\!\left(-\tfrac12+iv\right)\right]dv.
\end{aligned}\tag{3}
$$

Both endpoints have the SAME spectral value $z(v)=2\cosh(2\pi v)$.
Their sine values are $-i\sinh(2\pi v)$, whereas the two Gaussian values
are $e^{\pi i nN(1/4-v^2)}e^{\mp\pi nNv}$. Consequently EXACTLY

$$
B\!\left(\tfrac12+iv\right)-B\!\left(-\tfrac12+iv\right)
=2i\sinh(2\pi v)\sinh(\pi nNv)e^{\pi i nN(1/4-v^2)}V_N(2\cosh(2\pi v)).\tag{4}
$$

In particular the paired current vanishes to order TWO at $v=0$.
The second factor is a hyperbolic sine, not a bounded oscillatory sine.
Its growth $e^{\pi|n|Nv}$ is kept in every estimate. Substitution in (3)
gives the plus-sign version

$$
J=H+2(-1)^{N\ell}\int_0^\tau e^{-2\pi\ell Nv}
\sinh(2\pi v)\sinh(\pi nNv)e^{\pi i nN(1/4-v^2)}V_N(2\cosh(2\pi v))\,dv.\tag{5}
$$

Thus multiplication by the original Fourier character in $F$ leaves the
vertical character $(-1)^\ell$, not a level-dependent endpoint sign. No
individual vertical side is set to zero. Formula (3) is an equality
before any summation or norm bound.

## 3. Uniform original operator bound for the tail

There are absolute $\tau_0>0$ and constants $c,C,C_0$ such that the following
holds for every fixed $n$, $0<\tau\leq\tau_0$ and integer $M$ with

$$
D=M-\frac{|n|}{2}-1\geq1.
$$

After increasing the constants when needed,

$$
\begin{aligned}
\|T_{N,n;M}\|\leq{}&C_{n,\tau}N^Ce^{C(\log N)^2}
\Bigl\{(M+1)e^{-N(2\pi\tau D-C_0)}\\
&\qquad+\left[D^{-1}+(|n|+1)D^{-2}\right]e^{N\varepsilon(D)}\Bigr\},\\
\varepsilon(D)&=Ce^{-cD}\longrightarrow0\quad(D\longrightarrow\infty).
\end{aligned}\tag{6}
$$

Only fixed-$n$ uniformity in $N$ is asserted. In particular, for every
$\eta>0$ there is $L_\eta$, independent of $n$, such that choosing

$$
M\geq\frac{|n|}{2}+1+L_\eta,
$$

(with an integer ceiling) makes

$$
\limsup_{N\to\infty}\frac1N\log\|T_{N,n;M}\|\leq\eta.\tag{7}
$$

The constants multiplying (6) may depend on the fixed $n$. The cutoff
in (7) has the natural Gaussian threshold $|n|/2$ and an additional
fixed allowance. This is a bound for the original FULL-V Fourier
coupon, including semisimple data.

Proof of the horizontal part. In the original balanced root basis $\|F\|,\|\mathcal E\|\leq2$ and $K$ is
unitary. The literal coproduct gives $\|F_{\mathrm{tot}}\|,\|\mathcal E_{\mathrm{tot}}\|\leq4$,
hence $\|\Omega\|\leq18$ on the ENTIRE physical tensor product. This
includes high totals without changing the norm by a basis adapter.
Equivalently the actual blocks have fixed bandwidth and uniformly
bounded entries.
The exact divided-Chebyshev identity is

$$
V_N(z)=U_{N-1}(\Omega/2)+2\sum_{h=1}^{N-1}T_{N-h}(z/2)U_{h-1}(\Omega/2).
$$

The scalar recurrences imply $\|U_j(\Omega/2)\|\leq C_*^{j+1}$ for an
absolute $C_*>1$. On $\delta=x+i\tau$, $|x|\leq1/2$,

$$
|T_k(-\cos(2\pi\delta))|\leq e^{2\pi k\tau}.
$$

Thus $\|V_N(-2\cos(2\pi\delta))\|\leq CN e^{N(C_0+2\pi\tau)}$
for a fixed $C_0$. The sine is bounded, the Gaussian modulus is at most
$e^{\pi|n|N\tau}$, and the Fourier modulus is $e^{-2\pi\ell N\tau}$.
The resulting geometric sum of $\ell$ times horizontal integrals is
bounded by the first term of (6), after a harmless adjustment from
$M+1$ to $M$. It introduces no false coefficientwise real-spectral bound.

Proof of the vertical part. Use the already proved [original closing-region estimate](actual_casimir_closing_region_bound.md) on the right real ray, with $r=2\cosh(2\pi v)-2$:

$$
\|(2\cosh(2\pi v)-\Omega)^{-1}\|
\leq CN^3e^{CNf(r)+C(\log N)^2},\qquad
f(r)=\sqrt r\log(2+1/r).
$$

It applies at $v=0$ by the polynomial endpoint bound as well. Since
$\chi_N(2\cosh(2\pi v))=2\cosh(2\pi Nv)+2$, and $r$ is comparable to $v^2$,

$$
\|V_N(2\cosh(2\pi v))\|
\leq CN^3\exp\!\left\{N\left[2\pi v+Cv\log(C/v)\right]+C(\log N)^2\right\}.\tag{8}
$$

All constants are uniform for $0\leq v\leq\tau_0$, and $v\log(C/v)=0$ at $v=0$.
Also

$$
|\sinh(2\pi v)\sinh(\pi nNv)|\leq C|n|Nv^2e^{\pi|n|Nv}.
$$

For $D_\ell=\ell-|n|/2-1$, (5) therefore gives, up to polynomial factors,

$$
|n|N^4\ell e^{C(\log N)^2}\int_0^\tau v^2
\exp\!\left\{N\left[-2\pi D_\ell v+Cv\log(C/v)\right]\right\}dv.\tag{9}
$$

Reserve half the damping for the integral. Elementary one-variable
optimization yields

$$
\sup_{v\geq0}\left[Cv\log(C/v)-\pi Dv\right]
\leq C'e^{-cD}=\varepsilon(D).
$$

Since $D_\ell\geq D$, the remaining integral is at most

$$
e^{N\varepsilon(D)}\int_0^\infty v^2e^{-\pi ND_\ell v}\,dv
=\frac{2e^{N\varepsilon(D)}}{(\pi ND_\ell)^3}.
$$

Finally

$$
\sum_{\ell>M}\frac{\ell}{D_\ell^3}
\leq C\left[D^{-1}+(|n|+1)D^{-2}\right].\tag{10}
$$

This proves (6), with both charge signs included using their exact
symmetry. The bound is an ABSOLUTE summation of paired whole-domain
currents. It never uses convergence of an infinite sharp-cube series.
Choose $D$ so $2\pi\tau D-C_0>0$ and $\varepsilon(D)<\eta$ to obtain (7).
The $n=0$ case has zero vertical current; its finite-band Fourier formula
in fact has no charges $|\ell|>1$, consistent with this proof.

## 4. A genuine source consequence when ALL ports are far

Keep the original diagram order, the original physical cups/caps and
its single mark. Replacing every $R_i^{n_i}$ by $T_{N,n_i;M_i}$ gives
EXACTLY the subseries of the original whole-domain Fourier period
with $|\ell_i|>M_i$ for EVERY port. Finite-$N$ absolute convergence and
multilinearity justify this identity; physical coupons are never
commuted. Call this marked contraction $Z_{\mathrm{allfar}}$.

In the same balanced physical basis, the finitely many actual turns,
closures and single marked cap have polynomial operator/Euclidean norms
in $N$. Their entries are the original $N$ times unit-phase cup, $N^{-1}$
ordinary cap and $N^{-2}$ marked cap.
More explicitly, cups and ordinary caps have $a+b=d$; the marked cap
$m_{ab}=x^b/N^2$ is UNRESTRICTED. Their Euclidean norms are respectively
$N^{3/2}$, $N^{-1/2}$ and $N^{-1}$, and the retained right-turn pivots are
unit phases. The number of wires and contractions is fixed by the diagram. Hence

$$
|Z_{\mathrm{allfar}}|\leq\operatorname{poly}_D(N)\prod_i\|T_{N,n_i;M_i}\|,
\qquad\limsup_{N\to\infty}\frac1N\log|Z_{\mathrm{allfar}}|\leq\sum_i\varepsilon(D_i).\tag{11}
$$

once each horizontal term has been made exponentially decreasing.
This is an actual shared-source estimate, not a replacement of its
coefficient by arbitrary face radii. All $n_i$ are fixed before $N$.

The [geometric local unit theorem](general_localized_unit_charge_filling_period.md) gives $\Phi_{\mathrm{fill}}\geq\Phi_D/2$ for ALL
independently sufficiently long fixed twists, after increasing a
threshold depending only on the original diagram. Choose fixed $D_i$
so $\sum_i\varepsilon(D_i)<\Phi_D/4$ and all horizontal exponents in (6)
are negative. These $D_i$ depend on the fixed diagram, not on ratios or
magnitudes of the long slopes. The actual cutoffs can therefore be
chosen as $M_i=\lceil|n_i|/2+1+D_i\rceil$. Then (11) gives a uniform strict
RATE gap from the proved local contribution throughout that general
long-filling class. Prefactor and relative-error constants may still
depend on the fixed twists; no joint growing-twist/level limit follows.
This does not cover the much larger UNION
of sectors in which only one or some charges are far.

## 5. Partial far subsets: the exact missing mixed-source estimate

Let $\mathcal E_{D,S,N}$ be the literal original marked exterior functional with
$R_j^{n_j}$ retained, in their original order, on every $j$ outside a
nonempty set $S$. Define its norm on the remaining tensor product of
operator spaces by

$$
\|\mathcal E_{D,S,N}\|=
\sup_{\substack{\|A_i\|\leq1\\ i\in S}}
\left|\mathcal E_{D,S,N}\!\left(\bigotimes_{i\in S}A_i\right)\right|.
$$

Then the immediate correct bound for that subset is

$$
\left|\mathcal E_{D,S,N}\!\left(\bigotimes_{i\in S}T_i\right)\right|
\leq\|\mathcal E_{D,S,N}\|\prod_{i\in S}\|T_i\|.\tag{12}
$$

There is no established reason for the first factor to have rate less
than $\Phi_{\mathrm{fill}}$. The remaining signed $R$ powers are NOT uniformly unitary
in this basis. Their individual exponential norm bounds only supply a
crude upper rate depending on the retained twists. Equation (7) alone
therefore cannot remove a partial-far sector.

The exact finite inclusion-exclusion identity for the union is

$$
Z_{\mathrm{full}}-Z_{\mathrm{all\,low}}
=\sum_{\varnothing\ne S\subseteq\mathrm{ports}}(-1)^{|S|+1}
\mathcal E_{D,S,N}\!\left(\bigotimes_{i\in S}T_i\right).\tag{13}
$$

It retains the original full $R$ powers on the complement of $S$, rather
than replacing them by an uncontrolled collection of infinitely many
spectator charge pieces. A direct sufficient new input would be a
strict bound on these actual mixed exteriors, or a narrower estimate
on the paired-current families

$$
\mathcal E_{D,S,N}\!\left(\bigotimes_{i\in S}V_i(2\cosh(2\pi v_i))\right),
\qquad0\leq v_i\leq\tau.\tag{14}
$$

with a rate strictly below $\Phi_{\mathrm{fill}}$ as $v$ tends to zero, uniformly on
a small fixed closing box, including simultaneous endpoint subsets.
Every sine, Gaussian and charge character in (4)-(5) would then remain
explicit and summably controlled. Horizontal pieces can be made as
small as needed by increasing the fixed charge cutoffs, using a crude
finite exponential norm for the fixed remaining coupons. The difficult
input is thus the SHARED endpoint environment in (14), not a missing
local +2 resolvent estimate.

Neither the positive Fejer endpoint theorem at $\sigma=-2$ nor the
noncross local gap proves (14) at $\sigma=+2$ with arbitrary remaining
$R$ powers. Nor does a local norm estimate prove the needed shared rate.
This distinction is preserved in (11)-(14). No full invariant or
partial-far complement theorem is claimed here.

## Validation and scope

The [focused audit](../experiments/audit_actual_whole_domain_large_charge_tail.py) and its [results](../experiments/actual_whole_domain_large_charge_tail_results.json) check paired endpoint entries, whole-interval contour identities and charge-sign identities from the physical blocks. These are finite normalization checks, not proofs of an asymptotic rate or a mixed-source gap.