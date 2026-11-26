# Exponential loss for auxiliary colors below the complete color

Consider a fixed ordered Conway construction with its original auxiliary crossing circles and half-twist choices. Its reduced multiplication tree is obtained by combining consecutive products with no intervening quarter-turn. A junction is flagged when it carries one original crossing-circle operator used without the outer quarter-turn; a junction with no such operator is bare. We assume the construction has a strict complete state and that no two bare junctions are adjacent. The [source-bound theorem](actual_main_meridian_source_bounds.md) defines this class and constructs its actual typed source.

Write \(Y^\epsilon\) for the complete augmented complement, with all auxiliary circles still unfilled. The exponential rate \(F_0\) from the original complete calculation is
\[
F_0=\frac{\operatorname{Vol}(Y^\epsilon)}{2\pi}.
\tag{G}
\]
This is the volume of that original augmented complement. The intrinsic pressures used to evaluate its source do not insert additional crossing circles.

At level \(N\), put \(q=e^{\pi i/N}\), move the main meridian to \(M=q^s\), and retain every ordinary auxiliary color \(1\le j_i\le N\). The complete auxiliary color is \(N\). The theorem below says that a fixed proportional deficit in any one of the original colors gives a strict exponential loss, uniformly in all the other colors.

**Theorem.** Fix the construction and its half-twist choices \(\epsilon_i\in\{0,\pm1\}\). For every \(0\le R<1/2\) and \(0<\delta<1\), there is \(\gamma>0\) such that its actual reduced cut scalar satisfies
\[
\sup_{\substack{|s|\le R,\ 1\le j_i\le N\\
                 \text{some }j_i\le(1-\delta)N}}
 \left|\mathcal F_{N,\mathbf j}^{\epsilon}(q^s)\right|
 \le \exp N(F_0-\gamma)
\tag{F}
\]
for all sufficiently large \(N\), through both parities. The original framing, independent colors, carrier phases and primitive cut normalization are retained. The strict two-leaf case keeps its original component conditions.

The [uniform source upper bound](actual_main_meridian_source_bounds.md) holds on the larger disks \(R<1\). The present strict color gap is proved only for \(R<1/2\): the contour below uses one unwrapped interval of the physical crossing roots. Neither estimate identifies the smaller volume of a filled knot. The result also does not supply a lower bound or convergence of a normalized main-meridian profile.

The proof has two parts. First, an exact root-grid formula expresses the actual half-twist as a quadratic phase. Pairing the two grids removes the apparent singularity at the complete meridian and gives a contour estimate against a localized raw source polynomial. Second, the typed pairing exposes any selected original circle, and the existing source induction provides exactly that localization at the original action \(F_0\). No complex-strip estimate for the canonical crossing interpolation polynomial is assumed.

The finite algebra comes from the [typed compiler](actual_main_meridian_newton_compiler.md) and [six physical quarter-turns](actual_main_meridian_turn_comparison.md). The needed coefficient bounds and fresh Gaussian estimates are proved in [the source-bound theorem](actual_main_meridian_source_bounds.md). The original geometric normalization is the [marked strict-tree geometry](actual_conway_general_mask_marked_filling.md), with its [rigid-profile](actual_conway_rigid_spine_and_flagged_tree_geometry.md) and [intrinsic-pressure](actual_conway_unflagged_probe_geometry.md) identities.

## 1. The physical root data

Let
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad
 \eta=(-1)^{N+1},\quad
 P_s(z)=\mathcal T_N(z)+2\cos(2\pi s),
 \tag{1}
\]
where \(\mathcal T_N(u+u^{-1})=u^N+u^{-N}\). The normalized polynomial trace is
\[
 \phi_s(F)=(-1)^dN^2[z^d]\operatorname{rem}_{P_s}F.
 \tag{2}
\]
The actual ordinary-circle operator, including its pivot sign, is
\[
 L_j(z)=(-1)^{j-1}U_{j-1}(z/2),\qquad
 L_j(-2\cos\tau)=\frac{\sin(j\tau)}{\sin\tau}.
 \tag{3}
\]
The quotient in (3) is its polynomial continuation at zeros of the denominator.

For the equal-color object with parameter \(s\), the actual checked crossing has scalar and stripped eigenvalues
\[
 \kappa_s=q^{(d+s)^2/2},\qquad
 \lambda_r=(-1)^r q^{r(r+1)}q^{-2sr},
 \qquad 0\le r<N.
 \tag{4}
\]
These are the physical crossing and its retained Cartan scalar. Define
\[
 a_s=\frac d2+s,\qquad
 \tau_r(s)=\frac{2\pi}{N}(a_s-r),\qquad
 z_r=-2\cos\tau_r(s).
 \tag{5}
\]
Then \(e^{iN\tau_r}=\eta e^{2\pi is}\), and the \(z_r\) are the roots of \(P_s\), with multiplicity at collisions.

For the prescribed logarithmic lift,
\[
 r^2+(N+1-2s)r=(r-a_s)^2-a_s^2+2Nr.
 \tag{6}
\]
The last summand contributes \(e^{2\pi ir}=1\). Therefore
\[
 \lambda_r=q^{-a_s^2}
       \exp\!\left(\frac{iN\tau_r(s)^2}{4\pi}\right).
 \tag{7}
\]
Multiplication by the physical scalar in (4) gives the exact formula
\[
 \boxed{\displaystyle
 (\kappa_s\lambda_r)^\epsilon
 =C_{N,\epsilon}(s)
       \exp\!\left(\frac{i\epsilon N\tau_r(s)^2}{4\pi}\right),
 \quad
 C_{N,\epsilon}(s)=q^{\epsilon(d^2/4-s^2/2)},}
 \tag{8}
\]
for \(\epsilon=0,\pm1\). In particular, no factor of modulus \(e^{cN}\) has been suppressed. The complete factor \(q^{\epsilon d^2/4}\) has modulus one, and \(C_{N,\epsilon}(s)\) and its inverse are uniformly bounded on every fixed \(s\)-disk.

The crossing operator is denoted by \(R_s\) below; the unsubscripted real number \(R\) is the radius of the parameter disk. The opposite equal-color orientation uses \(-s\); (8)'s scalar is even in \(s\). The two mixed reference orders use the full complete crossing polynomial \(r_0\), with the already specified bounded monodromy scalar on reversal. They are addressed by the constant-relation version at the end.

## 2. A paired-grid integral with no meridian denominator

Fix \(0\le R<1/2\) and \(y>0\). Let \(\mathcal R_y\) be the positively oriented rectangle with real sides at \(-\pi,\pi\) and imaginary sides at \(-y,y\). For all sufficiently large \(N\), both grids \(\tau_r(s)\), \(\tau_r(-s)\), \(0\le r<N\), lie inside it uniformly on \(|s|\le R\). Their real endpoints stay strictly between \(-\pi\) and \(\pi\), since
\[
 |\operatorname{Re}\tau_r(\pm s)|
 \le\pi-\frac{\pi(1-2R)}{N}.
 \tag{9}
\]
Their imaginary parts are at most \(2\pi R/N<y\).

Let \(E_{N,s}\) be any raw polynomial, and put
\[
 B_{N,s,j}(\tau)
 =\sin(j\tau)
   \exp\!\left(\frac{i\epsilon N\tau^2}{4\pi}\right)
   E_{N,s}(-2\cos\tau).
 \tag{10}
\]
This function is odd in \(\tau\), even when its coefficients and \(s\) are complex. The exact contour identity is
\[
 \boxed{\displaystyle
 \phi_s(R_s^\epsilon L_jE_{N,s})
 =-\frac{N^2 C_{N,\epsilon}(s)}{2\pi i}
  \int_{\partial\mathcal R_y}
  B_{N,s,j}(\tau)\,
  \frac{e^{iN\tau}}
  {(e^{iN\tau}-\eta e^{2\pi is})
   (e^{iN\tau}-\eta e^{-2\pi is})}\,d\tau .}
 \tag{11}
\]
Here \(R_s^\epsilon\) means the actual full crossing polynomial, including the scalar of (4), raised to the indicated fixed power and interpreted in the original quotient. The product with \(E\) need not be reduced before using (11).

We prove the identity initially at generic \(s\). For \(u=e^{i\tau}\), the derivative at a root is
\[
 P_s'(-u-u^{-1})
 =\frac{2iN\sin2\pi s}{u-u^{-1}}
 =\frac{N\sin2\pi s}{\sin\tau}.
 \tag{12}
\]
Lagrange interpolation, (3), and (8) thus give
\[
 \phi_s(R_s^\epsilon L_jE)
 =\frac{\eta N C_{N,\epsilon}(s)}{\sin2\pi s}
       \sum_{r=0}^{N-1}B_{N,s,j}(\tau_r(s)).
 \tag{13}
\]

Introduce logarithmic-derivative kernels
\[
 K_{\pm s}(\tau)=
 \frac{iN e^{iN\tau}}{e^{iN\tau}-\eta e^{\pm2\pi is}}.
 \tag{14}
\]
Each has residue one at its grid. Since
\(\tau_{d-r}(-s)=-\tau_r(s)\), oddness of \(B\) implies
\[
 \sum_r B(\tau_r(s))
 =\frac1{4\pi i}
   \int_{\partial\mathcal R_y}B(\tau)
                   (K_s(\tau)-K_{-s}(\tau))\,d\tau.
 \tag{15}
\]
The difference is exactly
\[
 K_s-K_{-s}
 =-2\eta N\sin2\pi s\,
   \frac{e^{iN\tau}}
   {(e^{iN\tau}-\eta e^{2\pi is})
    (e^{iN\tau}-\eta e^{-2\pi is})}.
 \tag{16}
\]
Substitution in (13) proves (11), including its sign and its power \(N^2\).

There is no division by \(\sin2\pi s\) left in (11). No pole lies on its contour boundary for \(|s|\le R\), once \(N\) is sufficiently large as in (9). Thus its right side is holomorphic through \(s=0\). The actual crossing polynomial has its established removable complete collision, including the full first normal coefficients. Analytic continuation proves (11) at completeness as well. It does not replace the full Hermite trace by values at a repeated root.

## 3. Uniform estimates for the contour kernel

Write
\[
 \mathcal K_{N,s}(\tau)=
 \frac{e^{iN\tau}}
 {(e^{iN\tau}-\eta e^{2\pi is})
  (e^{iN\tau}-\eta e^{-2\pi is})}.
 \tag{17}
\]
On either horizontal side, with \(\tau=t\pm iy\), the two root constants have moduli in \([e^{-2\pi R},e^{2\pi R}]\), while \(|e^{iN\tau}|=e^{\mp Ny}\). For sufficiently large \(N\),
\[
 |\mathcal K_{N,s}(t\pm iy)|\le C_R e^{-Ny}.
 \tag{18}
\]

On a vertical side \(\tau=\pm\pi+iv\), the exponential is
\(e^{iN\tau}=-\eta e^{-Nv}\). Put \(t=e^{-Nv}>0\). For
\(|\arg(e^{\pm2\pi is})|\le2\pi R<\pi\),
\[
 |t+e^{\pm2\pi is}|
 \ge \cos(\pi R)\bigl(t+|e^{\pm2\pi is}|\bigr)
 \ge c_R(t+1).
 \tag{19}
\]
It follows that
\[
 |\mathcal K_{N,s}(\pm\pi+iv)|
 \le C_R\frac{t}{(1+t)^2}
 \le C_Re^{-N|v|}.
 \tag{20}
\]
This bound includes \(v=0\); no unproved separation of individual roots is required there. The hypothesis \(R<1/2\) is used both in (9) and (19).

## 4. A strict far-color loss

Assume the raw remaining source has the fresh Gaussian bound
\[
 |E_{N,s}(-2\cos(t+iv))|
 \le N^K
 \exp N\{F-c t^2+C v^2+\epsilon_N\},
 \quad |t|\le\pi,\ |v|\le y_0,\ |s|\le R,
 \tag{21}
\]
where \(c>0\), \(C\ge0\), \(\epsilon_N\to0\), and all constants are uniform over the other physical auxiliary colors. A product of a fixed number of canonical outputs with their respective fresh Gaussians satisfies (21) at the sum of their assigned actions; no prior quotient reduction is needed.

The root crossing's Gaussian phase obeys
\[
 \left|\exp\!\left(\frac{i\epsilon N(t+iv)^2}{4\pi}\right)\right|
 =\exp\!\left(-\frac{\epsilon Ntv}{2\pi}\right)
 \le\exp\!\left(\frac{N|t v|}{2\pi}\right),
 \tag{22}
\]
and \(|\sin(j(t+iv))|\le e^{j|v|}\). Fix \(0<\delta<1\) and suppose
\[
 1\le j\le(1-\delta)N.
 \tag{23}
\]
On the horizontal sides of the rectangle, (18), (21), and (22) give exponent at most
\[
 F+\epsilon_N-c t^2+
       \frac{|t|y}{2\pi}+Cy^2-\delta y.
 \tag{24}
\]
Completing the square yields
\[
 -ct^2+\frac{|t|y}{2\pi}\le\frac{y^2}{16\pi^2c}.
 \tag{25}
\]
Set \(C_*=C+(16\pi^2c)^{-1}\), and choose a fixed positive
\[
 y\le y_0,\qquad C_*y^2\le\frac{\delta y}{2}.
 \tag{26}
\]
The horizontal exponent is then at most \(F-\delta y/2+\epsilon_N\).

On the vertical sides \(t=\pm\pi\), (20)--(23) give exponent at most
\[
 F-c\pi^2+C v^2+\frac{|v|}{2}
       -\delta|v|+\epsilon_N
 \le F-c\pi^2+Cy^2+\frac y2+\epsilon_N.
 \tag{27}
\]
Shrink \(y\) further so that
\[
 Cy^2+\frac y2\le\frac{c\pi^2}{2}.
 \tag{28}
\]
This is compatible with (26), since \(y\) is free to be any sufficiently small fixed number. The vertical exponent is then at most \(F-c\pi^2/2+\epsilon_N\).

The contour has bounded length. Its prefactor in (11), the source prefactor in (21), and the bounded scalar in (8) have only polynomial cost. Thus there is \(\gamma>0\), depending on the fixed source parameters, \(R\), and \(\delta\), such that
\[
 \boxed{\displaystyle
 \sup_{\substack{|s|\le R\\1\le j\le(1-\delta)N}}
 |\phi_s(R_s^\epsilon L_jE_{N,s})|
 \le\exp N(F-\gamma),
 \qquad \epsilon=0,\pm1,}
 \tag{29}
\]
for every sufficiently large \(N\), at both parities.

The same proof applies to the opposite-color root relation \(P_0\): use \(\sigma=0\) in the kernel and the complete crossing chirp, retaining the bounded mixed-order monodromy scalar. The actual typed turn ratios used to expose the root are bounded as well. The single primitive main-cut factor \(H_N(s)\) does not change the loss on the disk under consideration.


## 5. Exposing each original circle

### 5.1. The source information used

Fix a strict literal Conway source whose reduced tree has no adjacent bare hubs. A flagged hub has exactly one original flagged leaf; a bare hub has none. The construction, all its ordered maps, its \(m\) labeled original circles, and its retained half-twist pattern \(\epsilon_i\in\{0,\pm1\}\) are fixed. Let \(F_0\) be its original complete action.

Here \(L\) denotes a branch with a rigid boundary profile \(g+c\), and \(A\) denotes a completed product branch with its own optimized boundary profile. These are branch types, distinct from the ordinary character \(L_j\). The profiles and their intrinsic pressures are normalized by
\[
 g(a)=\int_0^{2a}\log(2\sin\pi t)\,dt
       -4\int_0^a\log(2\sin\pi t)\,dt,\qquad
 G_0=g(1/4),\qquad
 \Omega_Q=\max_{0\le a\le1/2}\{g(a)+f_Q(a)\}.
 \tag{R0}
\]
The function \(f_Q(a)\) is the exponential rate of the original positive coefficient at fixed output label \(a\), after optimizing that branch's internal labels. If \(f_B\) is this function for the unturned product of \(B\) ordinary leaves, write
\(\widehat\omega_B=\max_{0\le a\le1/2}\{g(a)+f_B(1-a)\}\).
Every additive constant \(c\) retains the internal action of its branch.

We use the following two proved source bounds, including their fresh Gaussian conclusions:

- an ordinary or decorated outgoing \(L\)-module has its original spectral pressure \(\Omega_L=2G_0+c_L\) and a fresh Gaussian at that pressure;
- an outgoing bare-hub \(A\)-module with \(B\ge2\) incoming \(L\)-cones has original pressure \(\Omega_Q=\widehat\omega_B+\sum c_b\) and a fresh Gaussian there.

These are Sections 1 and 3 of the [source-bound theorem](actual_main_meridian_source_bounds.md). In the second statement the Gaussian follows from the original clean low-coordinate profile and the strictly smaller spectral remainder, not merely from a norm estimate.

The resulting assertion is: for every fixed \(0\le R<1/2\) and \(0<\delta<1\), there is \(\gamma>0\) such that
\[
 \sup_{\substack{|s|\le R,\ 1\le j_i\le N\\
                  \text{some }j_i\le(1-\delta)N}}
 |\mathcal F_{N,\mathbf j}^{\epsilon}(q^s)|
 \le \exp N(F_0-\gamma)
 \tag{R1}
\]
for every sufficiently large \(N\), at both parities. The scalar is the actual reduced auxiliary-colored source, with the prescribed main cut and framing. The argument does not sum auxiliary filling colors.

The contour estimate is proved in Sections 1–4 above. The [original intrinsic-pressure identities](actual_conway_unflagged_probe_geometry.md) and [source recursion](actual_main_meridian_source_bounds.md) fix its absolute action. No additional geometric comparison is assumed.

### 5.2. The actual closing adjunction

In fixed canonical Newton coordinates, the pairing for either actual quotient is
\[
 \langle f,g\rangle=\sum_{n=0}^{N-1} f_n g_{N-1-n}.
 \tag{R2}
\]
Every prescribed typed turn is
\[
 \begin{gathered}
 H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)},\qquad
 W_n(s)=\prod_{r=1}^n
 \left(1-\frac{\sin^2(\pi s/N)}{\sin^2(\pi r/N)}\right),\\
 T_\gamma=\frac{\gamma_N(s)}{H_N(s)}
          \mathbf J\operatorname{diag}(W_n(s)),
 \qquad \mathbf J_{ij}=\mathbf1_{i+j=N-1}.
 \end{gathered}
 \tag{R3}
\]
The removable value \(H_N(0)\) is one, and the prescribed turn scalar
\(\gamma_N(s)\) is \(1\) or \(q^{\pm s^2/2}\), according to its actual domain and codomain.
Consequently
\[
 \langle T_{\gamma_1}f,g\rangle
 =\frac{\gamma_1}{\gamma_2}
       \langle f,T_{\gamma_2}g\rangle.
 \tag{R4}
\]
Both sides are \(\gamma_1H_N^{-1}\sum W_nf_ng_n\). The scalar ratio records the two actual object types. Coherent carriers cancel in the composed pairing; the primitive top moment is the same for either orientation. This is an identity of the original full typed tensor contraction, including the first normal coordinates.

Changing the direction of a finite tree's recursive evaluation uses (R4), associativity within compatible objects, and the exact consecutive-turn identities. It multiplies the scalar only by the recorded bounded phase \(\chi_{i,N}(s)\), which is a fixed product of powers of \(q^{s^2/2}\). The original root crossing and circle pivot stay in their coupons. There is no assertion of an isotopy or of a scalar factorization of an effective branch.

### 5.3. The three possible positions

Choose an original circle \(i\), and orient all subtree evaluations toward its incident hub. Each child subtree remains in the separated-bare-hub class. The same induction supplies its original intrinsic pressure and fresh Gaussian.

#### A flagged leaf

If \(i\) is the marked leaf of a flagged hub, expose its original coupon \(p_i=R_s^{\epsilon_i}L_{j_i}\). Let \(Q_1,\ldots,Q_k\) be the other incident outgoing modules, each of type \(L\) or \(A\). The normalized closing scalar is
\[
 Z_{N,\mathbf j}^{\epsilon}(s)
 =\chi_{i,N}(s)\,
    \phi_\sigma\!\left(R_s^{\epsilon_i}L_{j_i} E_i\right),
 \qquad E_i=\prod_{a=1}^k Q_a,
 \tag{R5}
\]
where the product defining \(E_i\) is retained as a raw polynomial. Each factor is canonical and has its fresh Gaussian at \(\Omega_{Q_a}\). Their product therefore has a fresh Gaussian at \(\sum_a\Omega_{Q_a}=F_0\), by the original flagged-root action identity.

#### An ordinary leaf at a flagged junction

Now \(h_i=T_{\gamma_1}(p_i)\) is ordinary at its hub. That hub has a different marked original coupon \(p_v\), and its remaining branches are \(Q_a\) of type \(L\) or \(A\). Before the closing adjunction the scalar is the pairing of \(T_{\gamma_1}p_i\) with \(p_v\prod_aQ_a\). Transfer the closing turn by (R4). The remaining canonical polynomial is
\[
 E_i=T_{\gamma_2}\!\left(p_v\prod_aQ_a\right).
 \tag{R6}
\]
This is exactly a decorated \(L\)-module, so it has a fresh Gaussian at
\[
 \Omega_{E_i}=2G_0+\sum_a\Omega_{Q_a}.
 \tag{R7}
\]
This rate is the original \(F_0\): using \(v\) as the earlier flagged root gives the same sum, with the selected ordinary leaf contributing its intrinsic pressure \(2G_0\). The scalar again has the form (R5), with its actual phase ratio included in \(\chi_{i,N}\).

#### An ordinary leaf at a bare junction

The selected leaf \(h_i=T_{\gamma_1}p_i\) occupies one incidence of the bare hub. Every other child branch is type \(L\), because adjacent bare hubs are forbidden. There are \(B=d_v-1\ge2\) such branches. Transferring the selected leaf's turn gives
\[
 E_i=T_{\gamma_2}\!\left(\prod_{a=1}^B L_a\right).
 \tag{R8}
\]
This is exactly the whole bare-hub output. It has a fresh Gaussian at
\[
 \Omega_{E_i}=\widehat\omega_B+\sum_ac_a.
 \tag{R9}
\]
The closure with the selected existing ordinary leaf is precisely its defining intrinsic probe, so (R9) equals the original \(F_0\). That leaf was already in the source; it has not been added as a new crossing circle. Equation (R5) again holds with the prescribed typed adjunction scalar.

These alternatives exhaust every original leaf when a hub exists. In the strict two-leaf case, exposing either original coupon leaves the other decorated leaf, with Gaussian budget \(2G_0=F_0\), and the same closing adjunction supplies (R5).

### 5.4. The color gap and the main cut

For each fixed \(i\), the polynomial \(E_i\) in (R5), (R6), or (R8) is independent of \(j_i\). Its Gaussian constants and error are uniform over the other original physical colors. It is either one canonical outgoing polynomial or a product of a fixed number of canonical outgoing polynomials. Its degree is therefore \(O(N)\), though the half-twist contour estimate needs only its polynomial analyticity and Gaussian bound.

In every case its bound has the form
\[
 |E_i(-2\cos(t+iv))|
 \le N^{K_i}
   \exp N\{F_0-c_i t^2+C_i v^2+o(1)\},
 \quad |t|\le\pi,\quad |v|\le y_i,
 \tag{R10}
\]
with \(c_i>0\). The contour estimate (29) applied to (R5) gives a strict loss \(\gamma_i>0\) whenever \(j_i\le(1-\delta)N\). It covers both signs \(\epsilon_i=\pm1\) and the pure case \(\epsilon_i=0\), and also the constant opposite-color relation with its known monodromy scalar.

The original reduced cut is
\[
 \mathcal F_{N,\mathbf j}^{\epsilon}(q^s)
 =H_N(s)\,Z_{N,\mathbf j}^{\epsilon}(s).
 \tag{R11}
\]
There is still only one such boundary factor. It and every \(\chi_{i,N}\) are bounded on the fixed disk and do not change the strict rate. The finite number of original leaves permits \(\gamma\) in (R1) to be chosen smaller than every \(\gamma_i\), while absorbing all uniform \(o(1)\) errors and polynomial factors. This proves (R1).

Under the original strict marked geometry, \(2\pi F_0=\operatorname{Vol}(Y^\epsilon)\). This identifies the action appearing in (R1); it is not a comparison with a newly assembled probe link.

### 5.5. Scope

The estimate is for the auxiliary-colored source before the filling transform, and its reference rate is the augmented complete action. It does not prove the filled knot's lower volume rate or the convergence of the normalized regular main-meridian profile. The radius is fixed below \(1/2\), as required by the chosen unwrapped crossing-root contour. Adjacent bare hubs remain outside this source induction.

The [component extension](actual_main_meridian_component_extension.md) supplies the same argument for adjacent bare junctions satisfying its path condition. The separate [filled-meridian theorem](actual_main_meridian_filled_volume.md) proves the uniform filled-knot volume limit on \(|s|\le R<1\) by a joint crossing-power calculation. The smaller radius here belongs to this auxiliary-color estimate and is not the radius of that filled theorem.


## 6. Finite reproduction

The [reproduction script](../experiments/audit_main_meridian_auxiliary_color_gap.py) constructs the actual canonical crossing from its physical eigenvalues at generic parameters and from its full complete Newton polynomial at \(s=0\). It constructs the inverse crossing in the quotient, keeps the circle pivot, performs ordinary polynomial multiplication and division, and compares the resulting top-coefficient trace with the rectangle integral (11).

The [recorded results](../experiments/main_meridian_auxiliary_color_gap_results.json) contain 24 contour comparisons at levels 2 and 3, with all three half-twist choices, the complete parameter and a complex parameter, and deficient and complete auxiliary colors. At 60-digit working precision the largest scaled discrepancy is less than \(3.2\times10^{-43}\). The complete parameter uses the full Hermite specialization. These finite checks test the exact identities and their normalization. The uniform color loss follows from the contour bounds and the source Gaussian proved above.
