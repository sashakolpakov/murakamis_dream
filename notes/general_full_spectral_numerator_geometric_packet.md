# The original full spectral numerator has the marked geometric packet

31 October 2026. Internally reviewed. This assembles the exact
local cofactors, their independently proved relative packets and their
angular estimates with the ORIGINAL shared coefficient period. The
full Gaussian filling cycle is not selected here.

## 1. Original source and exact local reference

Fix a connected original flat plat $D$ with $R$ ports, the original two
protected faces $u,v$ joined by a MAIN edge, and its labeled convex ideal
right-angled certificate. The ordinary white graph is the original
simple triangulated sphere with $u,v$ removed. All coefficients, cups,
caps and the marked target are the original ones. Put $d=N-1$ and

$$
\begin{aligned}S_N(\boldsymbol\sigma)&=\left[\prod_{f\ \mathrm{ordinary}}L_f^d\right]\left.\prod_e H_{V_N(\sigma_e)}\right|_{L_u=L_v=0},\\ \sigma_e&=-2\cos(2\pi\delta_e),\qquad w_e=-\sigma_e-2.\end{aligned}
$$

Write $P_{\mathrm{cross}}$ for $(-1)^d$ times the literal local CROSS numerator, and
$C_N(\boldsymbol\delta)$ for the same marked coefficient with $P_{\mathrm{cross}}$ at every port.
The full source is $(-1)^{dR}C_N$ plus its actual one-sided remainder.

Let $\mathcal B_{e,N}(\delta_e;L)$ be the exactly anchored even interpolation
from [the actual complete-fold interpolation](actual_positive_face_exponential_fold_interpolation.md). The [local nodal-rigidity theorem](actual_cross_cofactor_interpolant_rigidity.md) proves, uniformly in one FIXED complex
neighborhood of the complete positive ordinary radii and fixed small
complex $\boldsymbol\delta$ disk, with the protected zeros unchanged,

$$
P_{\mathrm{cross}}=N^2\mathcal B_{e,N}\left[1+O(e^{-\kappa N})\right].\qquad (1)
$$

This uses independent relative estimates of the ACTUAL finite cofactors;
it is not inferred from complete-node values alone. Both parities,
including the odd simple node and every repeated-node spectral datum,
are included.

## 2. The actual global angular complement

The [global local-angular theorem](actual_cross_cofactor_global_angular_gap.md) supplies the following property for every actual
triangle cofactor $R_n$, $n=N/2+O(1)$. Fix its positive nonzero face radii.
When the arguments of two of its nonzero faces differ by at least
$\varepsilon\pmod{2\pi}$, there are $c,\tau>0$ and a polynomial $B(N)$ such that

$$
\left|R_n(xe^{i\theta_x},be^{i\theta_b},ye^{i\theta_y};w(\delta))\right|\leq B(N)e^{-cN}R_n(x,b,y;0).\qquad (2)
$$

for every real $\operatorname{Re}\delta$ and $|\operatorname{Im}\delta|\leq\tau$. The constants can be uniform on a
fixed compact of these radii. A triangle with only one nonzero face is
an exact monomial and has no relative angular constraint. Zero faces
stay exactly zero. The estimate covers the literal terminal indices
$m-2,m-1,m$ as required by the even and odd central formulas.

The proof of (2) is source-specific. Every required lower cofactor is
a polynomial of degree at most its row index in $w$. Its actual physical
node values are nonnegative coefficientwise and bounded by its endpoint
value. Nearfold node values contain the original positive $D_a$ factor,
whose established angular contraction applies to the nonzero faces.
Far-node values are strictly smaller: when $xy>0$, a positive fraction
of disjoint tail dimer choices enlarges the endpoint tail exponentially
relative to its nodal monomer upper bound. When $xy=0,\ b>0$, small starts
have the strict starting-row gap and the remaining starts have an
exponentially contracting prefix product. The $b=0,\ xy=0$ case is the
literal monomial exception. Exact cosine-grid interpolation loses only
a polynomial, also when finitely many terminal nodes must be omitted;
Bernstein growth costs $e^{2\pi n|\operatorname{Im}\delta|}$, absorbed by a fixed thin
strip. The separate protected-middle three-step proof supplies an
independent direct check on a fixed $w$ disk.

The exact central formula for $P_{\mathrm{cross}}$ is a sum of two or three products
of these cofactors and factors of bounded face degree. Each summand
contains a cofactor for BOTH of its original triangles. Thus if either
triangle has the separation in (2), every summand contracts. The
remaining cofactor has its global polynomial endpoint majorant times
$e^{2\pi n|\operatorname{Im}\delta|}$. Shrink the common strip height so the sum of
these growth costs from ALL other cofactors and ports is smaller than
half the detected angular loss. The graph is fixed, so only finitely
many costs occur. Finite central coefficients cause no exponential cost.
At the positive endpoint their normalized central factor is a nonzero
unit, so the resulting local estimate is against $P_{\mathrm{cross}}(0;L)$, with
an exponential loss. This does not assert positivity off the real node
set or divide by an angularly vanishing cofactor.

For clarity, the relevant ordinary-face adjacency graph is connected.
A simple sphere triangulation stays connected after deleting two
vertices: reroute a path avoiding the first deleted vertex along its
cycle of neighbors, then reroute occurrences of the second along its
neighbor cycle with the first removed, a connected path. Thus the
ordinary phases can all agree only up to ONE simultaneous rotation.
Fix one ordinary face $f_0$ as the scale reference. Outside any fixed
neighborhood of the common-phase point on the remaining $(R-1)\text{-torus}$,
a bounded-length ordinary-face path contains a separated edge. One
actual triangle contains its two finite endpoints, hence has (2).

It follows, uniformly for small fixed complex $\boldsymbol\delta$, that the ORIGINAL
Cauchy integrand of $C_N$ has an exponential angular gap off that
neighborhood. Its positive endpoint logarithmic scale at the complete
radii is $\Phi=\operatorname{Vol}(Y_D)/(2\pi)$. The product of finitely many polynomial
losses is $e^{o(N)}$. No different face radii are optimized at separate
ports, and no independent local norms replace the shared target.

## 3. Exact finite-N phase and the original coefficient saddle

Fix the positive complete ordinary radii $\boldsymbol\rho$, with $\rho_{f_0}$ held fixed.
For $f\ne f_0$ write $L_f=\rho_f e^{z_f}$, and retain $L_{f_0}=\rho_{f_0}$.
All protected variables remain zero. On the fixed local complex chart,
choose the logarithm real at $\boldsymbol\delta=0$ and positive real radii, and define

$$
\Psi_N(\mathbf z,\boldsymbol\delta)=\frac1N\sum_e\operatorname{Log}\mathcal B_{e,N}(\delta_e;L(\mathbf z))-\frac dN\sum_{f\ \mathrm{ordinary}}\operatorname{Log}L_f(\mathbf z).\qquad (3)
$$

Every original scalar in $\mathcal B$, including $B_{N,M}$, beta, finite forced
factors, parity shifts and the actual half-index, stays in (3). The
explicit $N^{2R}$ in (1) is kept outside (3). No amplitude is fitted to
an unknown source value.

The local cofactor and complete-fold theorems give uniform convergence
of $\Psi_N$ and its fixed derivatives on smaller charts to

$$
\Psi(\mathbf z,\boldsymbol\delta)=\sum_e\bigl[Q_{b_e}(\delta_e)+Q_{c_e}(\delta_e)\bigr]-\sum_{f\ \mathrm{ordinary}}\operatorname{Log}L_f(\mathbf z).\qquad (4)
$$

Any parameter-independent $O(\log N)/N$ terms in (3) are retained; their
vanishing in the limit does not license dropping them from the finite
formula. At $\boldsymbol\delta=0$, the actual complete radii are stationary for (4).
Its ordinary-face Hessian $H_0$ is positive definite after fixing $f_0$, by
the proved complete coefficient Hessian/connectedness theorem.

The uniform holomorphic IFT therefore gives, for all large $N$, a unique
nearby $\mathbf z_N(\boldsymbol\delta)$, with $\partial_{\mathbf z}\Psi_N=0$, on one fixed small complex
$\boldsymbol\delta$ polydisk. It converges with fixed derivatives to $\mathbf z(\boldsymbol\delta)$. Put

$$
A_N(\boldsymbol\delta)=\Psi_N(\mathbf z_N(\boldsymbol\delta),\boldsymbol\delta),\qquad H_N(\boldsymbol\delta)=\partial_{\mathbf z}^2\Psi_N(\mathbf z_N(\boldsymbol\delta),\boldsymbol\delta).
$$

$H_N$ is a holomorphic unit matrix there. Its square-root determinant is
continued from its positive real value at $\boldsymbol\delta=0$. $A_N$ converges with
fixed derivatives to the marked ordinary-face critical action $A_0$.

The original Cauchy measure is exactly $(2\pi)^{-(R-1)}d\boldsymbol\theta$ after the
common phase is removed. Indeed the integrand's total homogeneous
numerator degree is $dR$, equal to the total target degree. The simultaneous
angular variable cancels, and its integral is exactly $1$. There is no
extra $N$, mark or quotient volume inserted in this step.

Use (1) on a fixed neighborhood of the saddle and (2) on its complement.
Within the neighborhood the integrand is $N^{2R}e^{N\Psi_N}$, with an
exponentially small relative error. Its absolute-sum cost under a small
fixed complex $\boldsymbol\delta$ perturbation is at most $e^{CN|\boldsymbol\delta|}$; shrink the
polydisk so this cost is less than the exponential accuracy in (1).
The angular complement is likewise smaller than the local critical
value after this shrink, by its fixed endpoint gap and continuity.

The local complex saddle follows from the ACTUAL Cauchy torus. One can
deform its logarithmic coordinates to the horizontal real-angle plane
through $\mathbf z_N(\boldsymbol\delta)$. Keep the finite side faces of the local deformation;
they lie in the angular gap. Equivalently translate the full Cauchy torus
by the small complex vector $\mathbf z_N$, then localize it; the polynomial
numerator and the fixed Laurent target have no poles in the swept
annular region. Uniform positivity of $\operatorname{Re}H_N$ and bounded holomorphic
higher derivatives give the ordinary multidimensional Gaussian estimate

$$
C_N(\boldsymbol\delta)=\frac{N^{2R}e^{N A_N(\boldsymbol\delta)}}{(2\pi N)^{(R-1)/2}\sqrt{\det H_N(\boldsymbol\delta)}}\left[1+O(N^{-1})\right].\qquad (5)
$$

All finite phase scalars are in (3) and the explicit sign convention;
the original geometric-period amplitude in (5) is nonzero. No arbitrary
thimble coefficient has been assigned: this is the original face torus.
The estimate is uniform on a fixed complex $\boldsymbol\delta$ polydisk, including
all fixed derivatives on smaller polydisks. At $R=1$ the quotient has
dimension zero and the determinant/measure factor is $1$.

## 4. Restore the full numerator, including its semisimple data

The already proved spectral-polydisk-complement theorem gives

$$
\left|(-1)^{dR}S_N(\boldsymbol\sigma(\boldsymbol\delta))-C_N(\boldsymbol\delta)\right|\leq e^{N(\Phi-\gamma)}.\qquad (6)
$$

on some fixed sufficiently small polydisk, with $\gamma>0$. Both parities
are included by the independently checked odd regularization majorant.
This is an absolute estimate for the actual one-sided remainder.
It does not approximate that remainder by arbitrary off-node data.

At zero, $A_0(0)=\Phi$. Shrink the common polydisk so $\operatorname{Re}A_0(\boldsymbol\delta)>\Phi-\gamma/4$; uniform convergence gives the same comparison for $A_N$ with
an additional $o(1)$. Formula (5), its nonzero Hessian and the explicitly
retained polynomial factor then make (6) exponentially small RELATIVE
to the displayed main term. Consequently the original full source has

$$
S_N(\boldsymbol\sigma(\boldsymbol\delta))=(-1)^{dR}\frac{N^{2R}e^{N A_N(\boldsymbol\delta)}}{(2\pi N)^{(R-1)/2}\sqrt{\det H_N(\boldsymbol\delta)}}\left[1+O(N^{-1})\right].\qquad (7)
$$

In particular it is nonzero on that fixed complex neighborhood for
all sufficiently large $N$. Fixed spectral derivatives, including the
independent repeated-node semisimple terms, are controlled by Cauchy.
The expressions are even in each $\delta_e$; the same statement descends
to a fixed smaller spectral polydisk around $\sigma_e=-2$. This is a
fixed-root spectral theorem, not a claim about a generic-q deformation.

## 5. What this proves about the desired volume and what remains

The [absolute cofactor-action theorem](actual_cross_cofactor_marked_action.md) identifies $A_0$, including all face
momenta and marked zeros, with the UNTWISTED longitude-polarized geometric
branch. To restore the actual fixed half-twist pattern, define explicitly

$$
A_{\boldsymbol\epsilon}=A_0+\pi i\sum_e\epsilon_e\delta_e^2,\qquad U_{\boldsymbol\epsilon,e}=\partial_{\delta_e}A_{\boldsymbol\epsilon},\qquad V_e=-4\pi i\delta_e.
$$

The EXACT Gaussian of the original powers $n_e=\epsilon_e-2p_e$ therefore
gives

$$
A_0+\pi i\sum_e n_e\delta_e^2+2\pi i\sum_e\ell_e\delta_e
=A_{\boldsymbol\epsilon}-2\pi i\sum_e p_e\delta_e^2+2\pi i\sum_e\ell_e\delta_e.
$$
Half twists are included ONCE. Its stationary condition is the actual
primitive equation

$$
U_{\boldsymbol\epsilon,e}+p_eV_e=-2\pi i\ell_e.
$$

At a unit-charge sufficiently long smooth filling, the peripheral
boundary correction cancels the Gaussian terms exactly. Thus the
critical exponential rate supplied by (7) is that filled hyperbolic
volume, with the original normalization.

The source face-torus coefficient in (7) is now selected and nonzero.
The ORIGINAL spectral Gaussian period is still a separate integral and
charge sum. Its global deformation, nonzero contribution of the unit
charge, and suppression/cancellation of all other spectral regions and
charges are not proved here. A local packet and the correct filled
critical value do not by themselves establish the general Kashaev limit.

The [fixed-root scope audit](fixed_root_direct_power_scope.md) confirms that the original invariant route requires its spectral Hermite data, not a separate generic-q normal estimate.

Root and two independent internal reviewers checked the complete assembly, including all spectator strip costs, the original common-scale quotient and measure, the finite-N phase and Hessian, full-numerator restoration, and half twists counted exactly once. This is internal analytical review, not external peer review. No finite numerical check is used to infer the saddle theorem or spectral-cycle survival.

The subsequent [localized spectral-period theorem](general_localized_unit_charge_filling_period.md)
now proves that the original unit-charge integral on a fixed real spectral
cube contributes with a nonzero coefficient. Its finite local charge
sector has the actual filled volume as its growth rate, for independently
long fixed signed twists. The exact remaining global sum retains every
unselected charge on its full original domain; the sharp local cube
must not be used to split an infinite charge sum into separately
convergent pieces without justification.
