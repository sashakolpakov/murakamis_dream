# The original localized spectral period has a nonzero unit-charge filling contribution

analytical theorem, 31 October 2026. This proves a relative asymptotic on an **actual fixed real spectral cube**, with its original Fourier charges, sine factors, parity and marked coefficient. It does not estimate the integral outside that cube or the remote charge sum.

The inputs are the [full spectral numerator packet](general_full_spectral_numerator_geometric_packet.md), the [local charge comparison](general_local_charge_critical_monotonicity.md), and the exact period (13a) in the [cross-cofactor source interface](actual_cross_cofactor_factorization.md). The finite-root spectral identity is also recorded in the [spectral total-derivative theorem](actual_spectral_total_derivative_source.md).

## 1. Exact original normalization and the local quantity

Fix the original certified marked flat plat with $R$ ports. Put $d=N-1$,
$q=e^{\pi i/N}$, and let $n_i$ be its actual nonzero integer crossing
powers. In the long-twist convention $n_i=\epsilon_i-2p_i$. Define the
ENTIRE original shared spectral numerator

$$
S_N(\boldsymbol\sigma)=\left[\prod_{f\ \mathrm{ordinary}}L_f^d\right]
\left.\prod_i H_{V_N(\sigma_i)}\right|_{L_u=L_v=0}.
$$

The original fixed-root Fourier/Hermite period is exactly

$$
\begin{aligned}
I_{D,\mathbf n}
={}&q^{\frac{d^2}{4}\sum_i n_i}(-i)^R
\sum_{\boldsymbol\ell\in(\mathbb Z\setminus\{0\})^R}
\left(\prod_i\ell_i\right)(-1)^{(N+1)\sum_i\ell_i}\\
&\quad\times\int_{[-1/2,1/2]^R}
\left[\prod_i\sin(2\pi\delta_i)\right]
S_N\!\left(-2\cos(2\pi\boldsymbol\delta)\right)
\exp\!\left\{N\sum_i\left[\pi i n_i\delta_i^2+2\pi i\ell_i\delta_i\right]\right\}
\,d\boldsymbol\delta .
\end{aligned}\tag{1}
$$

Here $I_{D,\mathbf n}$ is the RAW original marked contraction. If the final
$K_N$ convention is $K_N=\chi_{D,N}I_{D,\mathbf n}$, its already recorded external
character multiplies every localized formula below as well. The
[complete-pointing normalization](actual_complete_augmented_source_normalization.md), especially
sections 1 and 3, retains the reduced framing character (modulus one)
and the enhanced component sign; a full one-cut modified ADO convention
has the additional $i^{N+3}/N$ factor. None is silently absorbed into
our raw amplitude. The actual final-diagram framing/component
character must be used, rather than the augmented diagram's component
count. Any such separately recorded scalar is still outside (1).
In particular (1) has no additional $N^R$, mark, spectral square-root
Jacobian or division by a quantum dimension. The displayed $q$ power is
the literal unwrapped scalar $\exp[\pi i d^2(\sum_i n_i)/(4N)]$. Charge zero
is absent by the exact total-derivative identity, not discarded by an
asymptotic argument. The full finite-$N$ charge series in (1) is
absolutely convergent; no uniform-in-$N$ summability is used below.

Choose $b>0$ within the fixed complex neighborhood of the full packet.
For a charge $\boldsymbol\ell$ let $J_{N,\boldsymbol\ell}$ be the integral in (1) restricted to the
CLOSED real cube $K_b=[-b,b]^R$. All local charge contributions below
include the factors preceding that integral in (1). This is a sharp
restriction of the original real contour, with its actual boundary.
There is no analytic compactly supported cutoff and no assigned
Lefschetz-cycle coefficient. Only FINITELY many restricted charge
terms are ever summed here. A sharp cube has boundary jumps and its
individual $J_{N,\boldsymbol\ell}$ do not inherit the absolute charge summability of
the original full-domain integral.

The proved full packet is

$$
S_N\!\left(-2\cos(2\pi\boldsymbol\delta)\right)
=\frac{(-1)^{dR}N^{2R}e^{N A_N(\boldsymbol\delta)}}
{(2\pi N)^{(R-1)/2}\sqrt{\det H_N(\boldsymbol\delta)}}
\left[1+O(N^{-1})\right].\tag{2}
$$

It is uniform and holomorphic on a fixed complex polydisc. Every
finite scalar and logarithmic normalization stays in $A_N$; the explicit
$N^{2R}$ alone is taken out. $H_N$ is the ordinary-face Hessian after
fixing ONE common face scale. Its determinant root is continued from
its positive value at $\boldsymbol\delta=0$. The dimension of that face quotient is
$R-1$. The packet restores the full $V$ numerator, including its
semisimple spectral data, by the proved noncross exponential gap.

The finite interpolant used to define $A_N$ is real on the real local
chart and even in each $\delta_i$. Uniqueness of the face IFT preserves
both properties. On smaller fixed polydiscs, with all fixed derivatives,

$$
A_N\longrightarrow A_0,\qquad A_0(0)=\Phi_D,\qquad
A_0''(0)=-2\operatorname{diag}(C_1,\ldots,C_R),\qquad C_i>0.\tag{3}
$$

These are finite-source properties, not a choice of a phase fitted to
the answer. In particular

$$
\partial_i A_N(\boldsymbol\delta)
=-2\delta_i B_{i,N}(\delta_1^2,\ldots,\delta_R^2),\qquad
B_{i,N}\longrightarrow B_i,\qquad B_i(0)=C_i.\tag{4}
$$

The quotients at $\delta_i=0$ are removable. After shrinking the chart,
$|B_{i,N}-C_i|\leq C_i/8$ for all large N. In particular
$\operatorname{Re}B_{i,N}>C_i/2$, and the real symmetric matrix $\operatorname{Re}A_N''(z)$ is negative
definite uniformly for ALL complex z in that chart and all large N.

## 2. Finite-N filling saddles for independent signed twists

There are fixed $b,a,n_0>0$, with a much smaller than b, such that the
following holds for every fixed integer vector $\mathbf n$ with $|n_i|\geq n_0$.
There is no condition on ratios $|n_i|/|n_j|$. For positive real charges
satisfying $\ell_i/|n_i|\leq a$ define

$$
\Phi_{N,\boldsymbol\ell}(\boldsymbol\delta)
=A_N(\boldsymbol\delta)+\pi i\sum_i n_i\delta_i^2
+2\pi i\sum_i\ell_i\delta_i.\tag{5}
$$

It has a unique critical point $\boldsymbol\delta_{N,\boldsymbol\ell}$ in the chosen small
polydisc. Indeed, writing $t_i=\ell_i/n_i$, its equations are precisely

$$
\delta_i=-\frac{t_i}{1+i B_{i,N}(\boldsymbol\delta^2)/(\pi n_i)}.\tag{6}
$$

Uniform contraction proves existence, uniqueness and holomorphic
parameter dependence, exactly as in the limiting charge lemma. Bounds
on $B_{i,N}$ and their derivatives are uniform in N. Consequently

$$
|\delta_i|\leq 2|t_i|,\qquad
\operatorname{Im}\delta_i
=\frac{\ell_i}{\pi n_i^2}
\frac{\operatorname{Re}B_{i,N}(\boldsymbol\delta^2)}
{\left|1+i B_{i,N}(\boldsymbol\delta^2)/(\pi n_i)\right|^2}>0.\tag{7}
$$

In particular $\operatorname{Im}\delta_i\leq C\ell_i/n_i^2$. This sign holds for BOTH
signs of $n_i$. All coordinates of the saddle are nonzero when all
$\ell_i>0$. Write $\boldsymbol\delta_*=x_*+iy_*$, with $y_*>0$ componentwise, and put

$$
S_{N,\boldsymbol\ell}=\Phi_{N,\boldsymbol\ell}(\boldsymbol\delta_*),\qquad
Q_{N,\boldsymbol\ell}=-\Phi_{N,\boldsymbol\ell}''(\boldsymbol\delta_*).
$$

Since the Gaussian contributes a purely imaginary diagonal Hessian,
$\operatorname{Re}Q_{N,\boldsymbol\ell}$ is positive definite. No real or complex eigenvalue of Q
vanishes. The spectral determinant root used below is the unique
Gaussian branch on the convex cone of complex symmetric matrices
with positive real part, positive at a positive real matrix. Thus

$$
\int_{\mathbb R^R}e^{-\frac12 t^TQt}\,dt
=\frac{(2\pi)^{R/2}}{\sqrt{\det Q}}.\tag{8}
$$

This fixes its phase even when the different $n_i$ have different signs.

For fixed $\mathbf n$ and $\boldsymbol\ell$, $\boldsymbol\delta_{N,\boldsymbol\ell}$ and $S_{N,\boldsymbol\ell}$ converge to the
corresponding limiting critical point and value. No convergence rate
is needed and $A_N$ is NOT replaced by $A_0$ in a relative formula.

## 3. Deformation of the actual restricted real contour

We prove the requisite contour coefficient, rather than postulate it.
Translate $K_b$ coordinate by coordinate to $K_b+i y_*$. Cauchy's theorem
on each rectangle gives equality with the translated integral plus
its oriented side integrals. The exact integrand is entire in $\boldsymbol\delta$;
the packet is only used to estimate it inside the common local chart.
The side integrals are retained in this equality.

Here is a uniform exponential bound for every side. Its points have
$z=x+iv$ with x in $K_b$, at least one $|x_j|=b$, and $0\leq v_i\leq y_{*,i}$.
Separate reality and the real Hessian bound give

$$
\operatorname{Re}A_N(x+iv)\leq A_N(0)-c|x|^2+C|v|^2.\tag{9}
$$

To see the quadratic, rather than linear, error in v, Taylor-expand
at the REAL point x: the first term $i\nabla A_N(x)\cdot v$ is imaginary.
The remaining derivatives are uniformly bounded. The real Gaussian
and charge contribution is

$$
-2\pi\sum_i n_i x_i v_i-2\pi\sum_i\ell_i v_i
\leq Cb\sum_i\frac{\ell_i}{|n_i|}.\tag{10}
$$

The second term is nonpositive. Equation (7) bounds the first term,
without using a common sign or a bound on slope ratios. Thus every
side has real phase at most

$$
A_N(0)-cb^2+C|y_*|^2+Cb\sum_i|t_i|.\tag{11}
$$

The critical value satisfies the complementary estimate

$$
\operatorname{Re}S_{N,\boldsymbol\ell}
\geq A_N(0)-C\sum_i|t_i|^2.\tag{12}
$$

For completeness, $A_N(\boldsymbol\delta_*)-A_N(0)=O(\sum_i|t_i|^2)$.
The critical equations imply $|n_i x_{*,i}+\ell_i|\leq C|\delta_{*,i}|$;
hence the real quadratic-plus-linear phase
$-2\pi\sum_i(n_i x_{*,i}+\ell_i)y_{*,i}$ has the same bound (and in fact a
smaller additional factor $n_{\min}^{-1}$). This proves (12) without
bounding the large purely imaginary quantity $n_i\delta_i^2$ by its
absolute value.

First fix b within the source chart, then choose a/b sufficiently
small and $n_0$ sufficiently large. Equations (11)-(12) give a fixed
$\kappa_b>0$ such that ALL sides satisfy

$$
\operatorname{Re}\Phi_{N,\boldsymbol\ell}(z)
\leq\operatorname{Re}S_{N,\boldsymbol\ell}-\kappa_b.\tag{13}
$$

All polynomial prefactors in (2), bounded sine factors and finite
side volumes preserve this exponential loss. Thus the actual local
real contour has coefficient +1 on its translated horizontal saddle
plane, with only exponentially small side currents.

On that plane $\Phi'$ vanishes at $x_*+iy_*$, and for every real x in $K_b$

$$
\operatorname{Re}\Phi_{N,\boldsymbol\ell}(x+iy_*)
\leq\operatorname{Re}S_{N,\boldsymbol\ell}-c|x-x_*|^2.\tag{14}
$$

Indeed the real part of its real-coordinate Hessian is $\operatorname{Re}A_N''$,
which is uniformly negative definite along the entire segment. The
critical point stays a fixed distance from the cube boundary because
$|x_*|\leq2a$ much less than b. This proves the requisite local and
nonlocal estimates on the translated restricted contour. It does
not say anything about the original contour outside $K_b$.

## 4. Relative asymptotic and its nonzero coefficient

Define

$$
a_N(\boldsymbol\delta)
=\frac{\prod_i\sin(2\pi\delta_i)}{\sqrt{\det H_N(\boldsymbol\delta)}}.
$$

The holomorphic Gaussian estimate on (14), using (8), yields

$$
J_{N,\boldsymbol\ell}
=(-1)^{dR}\sqrt{2\pi}\,N^{R+1/2}
\frac{a_N(\boldsymbol\delta_{N,\boldsymbol\ell})}{\sqrt{\det Q_{N,\boldsymbol\ell}}}
 e^{N S_{N,\boldsymbol\ell}}
\left[1+O_{\mathbf n,\boldsymbol\ell}(N^{-1})\right].\tag{15}
$$

The error in the full packet is holomorphic and uniformly $O(N^{-1})$;
Cauchy bounds, or direct Gaussian integration of that error, preserve
(15). The ordinary Taylor Gaussian error is $O(N^{-1})$, since its odd
first correction integrates to zero; replacing the cube by the full
real Gaussian changes the answer exponentially. The exact side
integrals in (13) are likewise exponentially small relative to (15).
Constants may depend on the FIXED slopes and charges. No joint
large-twist/large-level error estimate is asserted.

The power and constant follow directly from the TWO actual integrals:

$$
N^{2R}(2\pi N)^{-(R-1)/2}(2\pi/N)^{R/2}
=\sqrt{2\pi}\,N^{R+1/2}.\tag{16}
$$

There is no undetermined stationary multiplier. Every sine in (15)
is nonzero: $\delta_{*,i}$ is nonzero by (6) and lies in a small disk with
no other zero of $\sin(2\pi\delta_i)$. Both determinant roots are units.
For each fixed $\mathbf n$ and $\boldsymbol\ell$ the coefficient in (15) converges to a
nonzero number. Therefore the local integral is nonzero for all
sufficiently large N.

Let $U_{N,\mathbf n;b}$ denote the sum of the original contributions in (1)
with $\ell_i\in\{+1,-1\}$, each restricted to $K_b$. Reflection of one
coordinate $\delta_i\mapsto-\delta_i$ changes $J_{N,\boldsymbol\ell}$ by a minus sign
and also changes $\prod_i\ell_i$ by a minus sign. $S_N$ and the quadratic
phase are separately even, and the parity character is unchanged.
Thus all $2^R$ sign choices contribute EXACTLY equally. With
$S_{N,\mathbf1}$, $\boldsymbol\delta_{N,\mathbf1}$, $Q_{N,\mathbf1}$ defined above,

$$
\begin{aligned}
U_{N,\mathbf n;b}
={}&q^{\frac{d^2}{4}\sum_i n_i}(-2i)^R\sqrt{2\pi}\,N^{R+1/2}\\
&\quad\times\frac{\prod_i\sin(2\pi\delta_{N,\mathbf1,i})}
{\sqrt{\det H_N(\boldsymbol\delta_{N,\mathbf1})}\sqrt{\det Q_{N,\mathbf1}}}
 e^{N S_{N,\mathbf1}}\left[1+O_{\mathbf n}(N^{-1})\right].
\end{aligned}\tag{17}
$$

The parity cancellation is literal:

$$
(-1)^{(N+1)R}(-1)^{dR}=(-1)^{2NR}=1.
$$

Equation (17) holds through BOTH level parities and arbitrary
independent signs of the sufficiently long fixed $n_i$. The remaining
$q$ scalar has modulus one and is kept exactly. This proves a nonzero
contributing localized original unit-charge period, not merely the
existence of the corresponding critical point.

## 5. Optional enlargement to the finite LOCAL charge sector

For fixed $\mathbf n$ let $L_i=\lfloor a|n_i|\rfloor$, with $n_0$ enlarged so $L_i\geq1$.
Restrict (1) to $K_b$ and to $0<|\ell_i|\leq L_i$. This is a finite set after
the twists are fixed. The exact finite version of the monotonicity
calculation applies to $A_N$, because (4) and $\operatorname{Re}B_{i,N}>0$ hold:

$$
\partial_{\ell_i}\operatorname{Re}S_{N,\boldsymbol\ell}
=-\frac{2\ell_i}{n_i^2}
\frac{\operatorname{Re}B_{i,N}}
{\left|1+iB_{i,N}/(\pi n_i)\right|^2}.
$$

After the same fixed shrink, for every positive charge in this box,

$$
\operatorname{Re}S_{N,\mathbf1}-\operatorname{Re}S_{N,\boldsymbol\ell}
\geq\sum_i\frac{C_i}{2n_i^2}(\ell_i^2-1).\tag{18}
$$

The harmless constants can be decreased if needed to make this
inequality uniform in all large N. If any nonunit positive charge
exists, the right side has a strictly positive minimum $\eta_{\mathbf n}$ over
that FINITE set. Formula (15), the exact charge factors $\prod_i\ell_i$,
and the independent sign symmetry imply that the entire restricted
local charge sector equals (17) with an additional relative
$O_{\mathbf n}(e^{-\eta_{\mathbf n}N})$ error (or after a smaller $\eta_{\mathbf n}$). If all $L_i=1$,
there are no extra local charges. There is no comparison of an
infinite charge sum and no assertion about charges near an alias.

## 6. Geometric value and exact remaining limitation

The limiting action in (5) is

$$
\begin{aligned}
A_0+\pi i\sum_i(\epsilon_i-2p_i)\delta_i^2
+2\pi i\sum_i\ell_i\delta_i
&=A_{\boldsymbol\epsilon}-2\pi i\sum_i p_i\delta_i^2
+2\pi i\sum_i\ell_i\delta_i,\\
A_{\boldsymbol\epsilon}&=A_0+\pi i\sum_i\epsilon_i\delta_i^2.
\end{aligned}
$$

Thus the half twists occur ONCE. The [marked action and collar identity](actual_cross_cofactor_marked_action.md) gives the actual primitive saddle equation

$$
U_{\boldsymbol\epsilon,i}+p_iV_i=-2\pi i\ell_i.
$$

Here $S_{0,\mathbf1}$ denotes the limiting critical value. At the all-unit long-filling branch, its Gaussian peripheral correction
cancels exactly and $2\pi\operatorname{Re}S_{0,\mathbf1}$ is the actual smooth filling volume.
Consequently the localized quantity (17), and the finite local charge
sector in Section 5, have that volume as their normalized logarithmic
modulus limit. The original exterior unit framing phase does not
change this conclusion.

This is NOT yet the original invariant's volume limit. For the FINITE
selected charge set $\mathcal L$ (the sign-unit set or the finite box of section 5),
define the exact remainder as the original full period (1) MINUS that
finite localized sector. It is the sum of:

- the finitely many $\boldsymbol\ell\in\mathcal L$, each integrated over the original
  full cube minus $K_b$, with its original charge factor; and
- ALL $\boldsymbol\ell\notin\mathcal L$, each kept on its WHOLE original domain
  $[-1/2,1/2]^R$, with the original absolutely convergent summation.

Do not separately sum the remote inside-$K_b$ and outside-$K_b$ pieces.
The sharp boundaries would generally destroy their separate charge
summability; such a split would require a specified shared
regularization and its boundary cancellation. The endpoint currents
are already encoded in the exact identity (1), not additional terms
to append to that identity. No endpoint cancellation was discarded in
deriving the finite localized formula.

This exact remainder still requires a phase-preserving global estimate
excluding cancellation of the nonzero contribution (17). Generic-$q$
normal derivatives are not an additional requirement for this
fixed-root route; the exact marked source and all $\sigma$-Hermite data
are already retained in (1)-(2).

## Validation and scope

The result proves a localized contribution and its finite local charge sector; it does not prove a bound for the remaining original period or the general filled-knot volume conjecture.