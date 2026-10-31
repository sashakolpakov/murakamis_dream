# The entire original all-CROSS Fourier period from its local packet and global spectral gap

Independently reviewed analytical theorem, 31 October 2026. This concerns the actual all-CROSS shared numerator and its **whole original Fourier/Hermite period**. The two source estimates used below have separate proofs. All twists are independently signed, sufficiently long, and fixed before the level tends to infinity. The remaining moving one-sided sectors of the full numerator are not estimated here.

## 1. Exact source, hypotheses, and conclusion

Fix the original certified marked flat plat $D$ with $R$ ports, $d=N-1$ and $q=e^{\pi i/N}$. In this note write $C_N(\boldsymbol\delta)$ for the raw shared all-CROSS coefficient

$$
C_N=C_N^{\mathrm{raw}}=
\left[\prod_{f\ \mathrm{ordinary}}L_f^d\right]
\left.\prod_i H_{V_N,\mathrm{cross}}\right|_{L_u=L_v=0},\qquad
C_N^{\mathrm{raw}}=(-1)^{dR}C_N^{\mathrm{positive}}.
$$

where $C_N^{\mathrm{positive}}$ is the sign-adjusted coefficient formed from
$P_{\mathrm{cross}}=(-1)^dH_{V_N,\mathrm{cross}}$ in the preceding cofactor/global-gap notes.
The spectral arguments are $\sigma_i=-2\cos(2\pi\delta_i)$, with both parity
definitions of CROSS retained. The absolute global gap is unchanged by
this exact sign. The raw source is an entire, separately even,
one-periodic function of each $\delta_i$, obtained from a polynomial of
degree at most $d$ in each $\sigma_i$. It is not an independently optimized
product of local norms. In particular the sign $(-1)^{dR}$ in (2) belongs
to this raw convention, not to the preceding positive $C_N$.

The original all-CROSS sector of the raw marked period is

$$
\begin{aligned}
I_{\mathrm{cross}}={}&q^{\frac{d^2}{4}\sum_i n_i}(-i)^R
\sum_{\boldsymbol\ell\in(\mathbb Z\setminus\{0\})^R}
\left(\prod_i\ell_i\right)(-1)^{(N+1)\sum_i\ell_i}\\
&\quad\times\int_{[-1/2,1/2]^R}
\left(\prod_i\sin(2\pi\delta_i)\right)C_N(\boldsymbol\delta)
\exp\!\left\{N\sum_i[\pi i n_i\delta_i^2+2\pi i\ell_i\delta_i]\right\}
\,d\boldsymbol\delta.
\end{aligned}\tag{1}
$$

Every $n_i=\epsilon_i-2p_i$ is its actual nonzero fixed integer crossing power. A separately recorded final-diagram framing/component character multiplies (1) when converting the raw contraction to the final invariant convention. No additional mark or power of N is inserted. Formula (1) follows by linear projection of the [exact full numerator identity](actual_cross_cofactor_factorization.md) onto these path sectors; a separate covariance claim for an individual path sector is unnecessary.

For every fixed $N$ and $\mathbf n$ the whole-domain charge series is absolutely convergent. Indeed $B_N=(\prod_i\sin(2\pi\delta_i))C_Ne^{\pi iN\sum_i n_i\delta_i^2}$ has zero endpoint values and matching first derivatives in each variable, including after differentiating other variables. Three integrations by parts in each coordinate give $O_{N,\mathbf n}(\prod_i|\ell_i|^{-3})$; after the charge factors this is summable. This observation alone is not a bound uniform in $N$.

The two source inputs are:

(H1) On a fixed complex cube around $\boldsymbol\delta=0$, the actual all-CROSS numerator has the relative packet

$$
C_N(\boldsymbol\delta)
=\frac{(-1)^{dR}N^{2R}e^{N A_N(\boldsymbol\delta)}}
{(2\pi N)^{(R-1)/2}\sqrt{\det H_N(\boldsymbol\delta)}}
\left[1+O(N^{-1})\right].\tag{2}
$$

with its exact finite anchors and determinant branch. $A_N$ is real on the real chart, even in each coordinate, and tends with fixed derivatives to $A_0$, with $A_0(0)=\Phi_D$ and $A_0''(0)=-2\operatorname{diag}(C_i)$, $C_i>0$. On a smaller chart $\operatorname{Re}A_N''$ is uniformly negative definite. This is the CROSS packet proved before the full-numerator restoration in the [whole-source packet theorem](general_full_spectral_numerator_geometric_packet.md), so it uses the same $A_N$ and $H_N$. Equivalently the full packet plus its independently controlled noncross error gives the same local asymptotic.

(H2) For every fixed $\eta>0$, there are $\tau_\eta,\gamma_\eta>0$ such that

$$
|C_N(\boldsymbol\delta)|\leq e^{N(\Phi_D-\gamma_\eta)}.\tag{3}
$$

for all sufficiently large N, $\max_i|\operatorname{Re}\delta_i|\geq\eta$ on the centered real cube, and $|\operatorname{Im}\delta_i|\leq\tau_\eta$. Periodicity extends this to equivalent real representatives. Every fixed derivative has the same strict exponential bound on smaller strips. The [global CROSS spectral-gap theorem](actual_global_cross_spectral_gap.md) retains the protected zero faces and all original start rows.

**Theorem.** There is a diagram-dependent threshold $n_0$ such that for every fixed independently signed integer vector with $|n_i|\geq n_0$, the entire period (1) equals

$$
\begin{aligned}
I_{\mathrm{cross}}={}&q^{\frac{d^2}{4}\sum_i n_i}(-2i)^R\sqrt{2\pi}\,N^{R+1/2}\\
&\quad\times\frac{\prod_i\sin(2\pi\delta_{N,\mathbf1,i})}
{\sqrt{\det H_N(\boldsymbol\delta_{N,\mathbf1})}\sqrt{\det Q_{N,\mathbf1}}}
 e^{N S_{N,\mathbf1}}\\
&\quad\times\left[1+O_{\mathbf n}(N^{-1})+O_{\mathbf n}(e^{-\eta_{\mathbf n}N})\right].
\end{aligned}\tag{4}
$$

for some $\eta_{\mathbf n}>0$. Here $\boldsymbol\delta_{N,\boldsymbol\ell}$ is the actual finite saddle of

$$
\begin{aligned}
\Phi_{N,\boldsymbol\ell}(\boldsymbol\delta)
&=A_N(\boldsymbol\delta)+\pi i\sum_i n_i\delta_i^2+2\pi i\sum_i\ell_i\delta_i,\\
S_{N,\boldsymbol\ell}&=\Phi_{N,\boldsymbol\ell}(\boldsymbol\delta_{N,\boldsymbol\ell}),\\
Q_{N,\boldsymbol\ell}&=-\Phi_{N,\boldsymbol\ell}''(\boldsymbol\delta_{N,\boldsymbol\ell}).
\end{aligned}
$$

and the $Q$ determinant root is the Gaussian branch $\operatorname{Re}Q>0$. The coefficient in (4) is nonzero for each fixed $\mathbf n$, at both level parities. Its normalized logarithmic modulus limit is the actual smooth filled hyperbolic volume, by the [marked action and boundary correction](actual_cross_cofactor_marked_action.md). The same exact half twist $\mathbf n=\boldsymbol\epsilon-2\mathbf p$ occurs only once.

The proof uses no separately summed infinite sharp-cube series. Only a finite charge set is localized. The infinite tail is estimated on whole original intervals before any charge summation.

## 2. Basic bounds, endpoint identities, and parameter choices

The local packet and real concavity bound near zero, together with (H2) outside a smaller fixed cube, imply

$$
\sup_{\boldsymbol\delta\ \mathrm{real}}|C_N(\boldsymbol\delta)|
\leq e^{N(\Phi_D+e_N)},\qquad e_N\longrightarrow0.\tag{5}
$$

Polynomial Bernstein on each cosine variable yields, for any fixed $T$,

$$
|C_N(\boldsymbol\delta)|
\leq\exp\!\left[N(\Phi_D+e_N)+2\pi d\sum_i|\operatorname{Im}\delta_i|\right],
\qquad |\operatorname{Im}\delta_i|\leq T.\tag{6}
$$

This is a bound for the whole shared polynomial; no factorwise positive-radius majorant is used. For source derivatives, apply Cauchy to (6) in the required variables. Gaussian derivatives are evaluated separately on REAL spectator coordinates, avoiding any unwanted large-twist exponential cost.

If a source factor $Z$ is an arbitrary entire polynomial in the $\sigma_i$, its product with $\prod_i\sin(2\pi\delta_i)$ and the fixed Gaussian satisfies

$$
\left.B\right|_{\delta_j=\pm1/2}=0,\qquad
\left.\partial_j B\right|_{\delta_j=1/2}
=\left.\partial_j B\right|_{\delta_j=-1/2}.\tag{7}
$$

The first derivative is solely the derivative of the sine: the two cosines are both $-1$, the spectral argument is $2$ at both ends, and the Gaussian endpoint value is $e^{\pi iNn_j/4}$. These facts remain true after arbitrary derivatives in other variables, including when one different coordinate is held complex. Thus three integrations by parts give exactly

$$
\begin{aligned}
\int_{-1/2}^{1/2}B e^{2\pi iN\ell_j\delta_j}\,d\delta_j
=(2\pi iN\ell_j)^{-3}\biggl\{
&\left[\partial_j^2B e^{2\pi iN\ell_j\delta_j}\right]_{-1/2}^{1/2}\\
&-\int_{-1/2}^{1/2}\partial_j^3B e^{2\pi iN\ell_j\delta_j}\,d\delta_j
\biggr\}.
\end{aligned}\tag{8}
$$

The second-derivative endpoint difference is retained. Repeating (8) over any spectator subset gives at most $3^{R-1}$ boundary/integral terms. Fixed source Cauchy bounds and real Gaussian derivatives cost at most $C_{\mathbf n}N^3$ per differentiated variable; these powers cancel the $N^3$ denominators. After the actual charge factors, every spectator coordinate supplies $|\ell_j|^{-2}$.

Choose a small fixed outer cube $K_B=[-B,B]^R$ inside (H1). Choose $a>0$ much smaller than $B$ so the localized contribution theorem applies uniformly for all positive charges $\ell_i/|n_i|\leq a$. Next choose $0<b<a/4$, with $K_b$ inside the same chart. All these constants depend only on $D$. Below $n_0$ will be enlarged finitely many times, independently of ratios among the $|n_i|$.

## 3. The infinite far-charge union is exponentially small

Use (H2) at $\eta=1/4$. Choose $\tau>0$ sufficiently small that the source and all required spectator derivatives have a strict bound $e^{N(\Phi_D-\gamma_e)}$ at

$$
\delta_i=\pm\frac12+iv,\qquad 0\leq v\leq\tau.
$$

with every other coordinate real or in a fixed Cauchy neighborhood of radius $\tau$. This uses the separated endpoint coordinate, regardless of the other real coordinates. Shrink $\tau$ and $\gamma_e$ once if needed.

For a positive far charge $\ell_i$, shift its whole interval upwards by $i\tau$, keeping all other integrations on their whole real intervals. Write

$$
B_i(z;\boldsymbol\delta_{\mathrm{other}})
=\sin(2\pi z)e^{\pi i n_iNz^2}C_N(z,\boldsymbol\delta_{\mathrm{other}}).
$$

The exact pair of endpoint currents is

$$
\begin{aligned}
B_i(1/2+iv)-B_i(-1/2+iv)
={}&2i\sinh(2\pi v)\sinh(\pi n_iNv)\\
&\quad\times e^{\pi i n_iN(1/4-v^2)}
 C_N(1/2+iv,\boldsymbol\delta_{\mathrm{other}}).
\end{aligned}\tag{9}
$$

The other sine/Gaussian factors remain outside this equality. Multiplying the actual Fourier character leaves the endpoint parity $(-1)^{\ell_i}$. Its modulus is one. Both vertical sides were retained; the paired factor vanishes quadratically at $v=0$.

For the paired vertical contribution, apply (8) in every spectator coordinate. The strict endpoint strip bound and source Cauchy estimates then give, after all original charge weights, an upper bound

$$
C_{\mathbf n}|n_i|N\ell_i\,e^{N(\Phi_D-\gamma_e)}
\left(\prod_{j\ne i}|\ell_j|^{-2}\right)
\int_0^\tau v^2 e^{-2\pi N(\ell_i-|n_i|/2)v}\,dv.\tag{10}
$$

Here $|\sinh(2\pi v)\sinh(\pi n_iNv)|\leq C|n_i|Nv^2e^{\pi|n_i|Nv}$. No oscillatory-sine substitution is made. For $\ell_i>|n_i|/2+D$, with $D\geq1$, the integral is at most $C/[N^3(\ell_i-|n_i|/2)^3]$. Consequently summing (10) over this far coordinate and all nonzero spectator charges is bounded by a polynomial factor times $e^{N(\Phi_D-\gamma_e)}$. The exact estimate

$$
\sum_{\ell>M}\frac{\ell}{(\ell-|n|/2)^3}
\leq C\left[D^{-1}+(|n|+1)D^{-2}\right].\tag{11}
$$

makes the summability explicit. Constants may depend on the fixed $\mathbf n$.

For the upper horizontal contribution, apply the same spectator integrations by parts. Source Cauchy from (6), in a fixed radius-$\tau$ neighborhood of the spectators, has exponential cost at most $2\pi R\tau N$. The shifted sine is bounded, while the bad-coordinate Gaussian and Fourier factors cost exactly at most

$$
e^{\pi|n_i|N\tau-2\pi\ell_iN\tau}.
$$

Thus the weighted horizontal contribution is bounded by

$$
C_{\mathbf n}\ell_i\left(\prod_{j\ne i}|\ell_j|^{-2}\right)
\exp\!\left\{N\left[\Phi_D+e_N+2\pi R\tau
-2\pi\tau(\ell_i-|n_i|/2)\right]\right\}.\tag{12}
$$

Choose a fixed $D$ large enough that $2\pi\tau D>2\pi R\tau+2\gamma_e$, and set

$$
M_i=\left\lceil\frac{|n_i|}{2}+D\right\rceil.\tag{13}
$$

The geometric tail of $\ell_i$ times (12) is exponentially bounded by $\Phi_D-\gamma_e$ after a harmless decrease of $\gamma_e$ and all large N. Both signs of the far charge obey the same estimate, either by downward shifts or the exact separate-evenness/reflection identity.

Therefore, for some fixed $\gamma_\infty>0$,

$$
\sum_{\substack{\boldsymbol\ell\in(\mathbb Z\setminus\{0\})^R\\
\exists i:\ |\ell_i|>M_i}}
\left|\mathcal I_{N,\boldsymbol\ell}^{\mathrm{cross}}\right|
\leq C_{\mathbf n}\operatorname{poly}(N)e^{N(\Phi_D-\gamma_\infty)}.\tag{14}
$$

Here $\mathcal I_{N,\boldsymbol\ell}^{\mathrm{cross}}$ denotes the full weighted charge term in (1). Use the union bound over $i$; multiple far coordinates cause no issue. Every other coordinate was summed on its whole original domain after (8). Finite-N absolute convergence and the displayed dominating series justify all summations. No partial-far exterior with uncontrolled $R$ powers appears: the hypothesis used is the shared all-CROSS endpoint gap, valid for arbitrary real spectator spectra. This is the stronger input missing from the local operator-tail argument.

## 4. The finite charges outside the local scaled box

The remaining set $0<|\ell_i|\leq M_i$ is finite after $\mathbf n$ is fixed. Suppose at least one coordinate $i$ has $|\ell_i|/|n_i|>a$. Reflect charge signs if necessary; the source is separately even, so absolute estimates are unchanged and assume $\ell_i>0$.

On the original real domain outside $K_b$, (H2) gives rate $\Phi_D-\gamma_b$. The Gaussian and Fourier factors there have modulus one. No contour estimate is needed for this finite-charge portion.

Inside $K_b$, shift only coordinate $i$ upward by

$$
t_i=\frac{b}{|n_i|}.\tag{15}
$$

All actual side currents of this small rectangle are retained. The packet and its real-action Taylor bound give, uniformly for $x$ in $K_b$ and $0\leq v\leq t_i$,

$$
\operatorname{Re}A_N(x+iv e_i)
\leq A_N(0)-c|x|^2+Cv^2.\tag{16}
$$

Reality makes the first Taylor term purely imaginary. The Gaussian-plus-Fourier contribution in this coordinate is

$$
-2\pi n_ix_iv-2\pi\ell_iv
\leq-2\pi|n_i|(a-b)v\leq0.\tag{17}
$$

On the horizontal translate, $v=t_i$, this costs at least $2\pi b(a-b)$, while the source error is at most $Cb^2/n_0^2$. On either vertical side $|x_i|=b$, (16) gives at least $cb^2$ loss, and (17) is nonpositive. Enlarge $n_0$ so $C/n_0^2$ is small. Then the horizontal and both sides have a fixed strict gap $\gamma_{\mathrm{bad}}>0$ below $\Phi_D$, independently of slope ratios. The packet's amplitudes contribute only polynomial factors.

Together with the exterior $K_b$ bound, every such bounded bad charge is exponentially small. There are finitely many of them, so their whole sum obeys the same strict rate with a fixed-n prefactor. No infinite sharp-cube series has been split.

## 5. Finite local charges and the actual unit contribution

It remains to consider the finite set with all $|\ell_i|/|n_i|\leq a$. On the real domain outside the larger $K_B$, (H2) gives a fixed loss $\gamma_B$. Inside $K_B$ apply the [localized original contour theorem](general_localized_unit_charge_filling_period.md) to the packet (2). It retains the exact side currents, the finite action, the Gaussian determinant branch and all sine/charge/parity factors.

For positive charges the finite critical values satisfy

$$
\operatorname{Re}S_{N,\mathbf1}-\operatorname{Re}S_{N,\boldsymbol\ell}
\geq\sum_i\frac{C_i}{2n_i^2}(\ell_i^2-1).\tag{18}
$$

All sign-unit choices contribute exactly equally. Every other charge in this finite local box has a positive fixed-n gap. The all-unit local contribution is precisely (4), with its $O_{\mathbf n}(N^{-1})$ relative error and nonzero limiting amplitude. The half twists are included once through $n_i=\epsilon_i-2p_i$.

The limiting unit loss from $\Phi_D$ is $O_D(\sum_i|n_i|^{-2})$. Enlarge the diagram-dependent $n_0$ until this loss is less than one quarter of the minimum of $\gamma_\infty$, $\gamma_{\mathrm{bad}}$, $\gamma_b$ and $\gamma_B$. Also require $a n_0\geq1$ so the unit charge lies in the local box. Since $S_{N,\mathbf1}$ tends to its limiting value, all complementary bounds above are then exponentially smaller than $e^{N\operatorname{Re}S_{N,\mathbf1}}$ for large N. The smallest nonunit gap in (18) may depend on the fixed vector $\mathbf n$, but remains positive. Combining the finite local sector, bounded bad charges and the absolutely bounded infinite union proves (4).

The exact critical volume identity identifies

$$
\lim_{N\to\infty}\frac{2\pi}{N}\log|I_{\mathrm{cross}}|
=\operatorname{Vol}(\text{the actual smooth filled exterior}).\tag{19}
$$

There is no uniform joint growing-twist/level error assertion: the twists are fixed first, while the threshold applies to arbitrary independent signs and magnitudes.

## 6. Scope of the transfer

The argument proves a contribution theorem and all-charge control for the entire original all-CROSS spectral sector from the proved inputs (H1)-(H2). The original full numerator also contains moving one-sided sectors. The already established diagonal/CROSS and short-moving sector gaps can be retained separately, but they do not exhaust that remainder. Formula (19) is therefore not yet the general filled-knot invariant theorem.

The crucial new analytic point is (14): a uniform shared endpoint gap makes partial far-charge tails summable without changing the actual source or creating infinite sharp-cut subseries. The old polynomial $+2$ operator bound alone would not control the spectator environment. No generic-$q$ normal theorem or unproved choice of a Lefschetz coefficient is used.

## Validation and scope

The full analytical transfer proof received independent root and geometry reviews. The review checked the raw versus sign-adjusted source convention, the paired hyperbolic-sine endpoint current, all spectator second-derivative endpoint terms, absolute summability of the partial-far union, the two distinct finite-charge cubes, and the original nonzero prefactor. No numerical audit is substituted for this analytic consequence. The theorem evaluates the entire all-CROSS sector; the moving one-sided remainder of the original full numerator remains outside its conclusion.
