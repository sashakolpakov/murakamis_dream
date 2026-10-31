# A positive comparison for a Conway region without a character operator

A tangle subtree is represented by a polynomial operator. To continue the quantum estimate through a turn, one must control both its values and its first derivatives at the repeated spectral nodes. A general norm bound for the turn has an exponential cost that need not equal the geometric contribution of that particular subtree. This note obtains the sharper, geometry-dependent estimate for a connected region of multiplication operations with no distinguished character operator inside it.

The reduced composition graph calls such a region **unflagged**. Its boundary inputs are actual polynomial operators supplied by adjacent subtrees. They may have complex coefficients and independent physical colors. The proof takes absolute values of their coefficient arrays and closes that positive comparison against a specified polynomial \(W_N\), called the probe. This is a device for an inequality: no additional crossing circle is inserted into the knot.

The theorem proves the norm bound, a strict loss for specified high-index contributions, and a way to transfer a loss from one boundary coefficient to the whole region. The [spectral propagation theorem](actual_conway_mixed_core_spectral_propagation.md) uses these conclusions to control angular decay. Their role in the complete volume argument is stated in the [strict-tree theorem](actual_conway_all_strict_tree_long_twist_volume.md); no independent filling argument is attempted here.

## 1. The algebra, the probe and the input bounds

Fix the level \(N\), put \(d=N-1\), and let \(M=\lfloor d/2\rfloor\). We work in the original pair algebra
\[
 \mathbb C[z]/(P_N(z)),\qquad P_N(z)=2T_N(z/2)+2,
\]
where \(T_N\) is the Chebyshev polynomial. Its Newton basis is
\[
 e_r(z)=\widehat B_r(z)=\frac{\prod_{a=0}^{r-1}(c_a-z)}{s_r^2},\qquad
 c_a=2\cos((2a+1)\pi/N),\qquad
 s_r=\prod_{a=1}^{r}2\sin(\pi a/N),\quad s_0=1.
\]
The physical turn reverses this basis: \(Te_r=e_{d-r}\). The marked closure functional \(\phi\) satisfies \(\phi(e_re_t)=\mathbf1_{r+t=d}\). These are the exact multiplication, turn and pairing conventions of the [reduced-hub source theorem](actual_conway_reduced_hub_source_normal_form.md).

The norm \(\|F\|_{\mathcal J}\) is the maximum of \(|F(c)|+|F'(c)|\) over double nodes, together with \(|F(-2)|\) at the odd simple node when present. It is a norm on the full quotient. For example, a local component proportional to \(z-c\) vanishes at the double node but still has a nonzero derivative there. A value-only norm would miss it. The first derivatives are the first Hermite normals retained by the invariant.

The logarithmic profiles used below are
\[
\begin{gathered}
J(u)=\int_0^u\log(2\sin\pi t)\,dt,\qquad
g(x)=J(2x)-4J(x),\\
\widetilde g(x)=g(\max(x,1/4))\quad(0\le x\le1/2),\\
k(x)=-2J(x/2)\quad(0\le x\le1).
\end{gathered}
\]
We also write \(G_0=g(1/4)\), the maximum of \(g\) on its low-index interval.
The probe assigns the large low-index basis elements their endpoint weights and assigns weight one to the remaining indices:
\[
w_{N,r}=
\begin{cases}
e_r(-2),&0\le r\le M,\\
1,&M<r\le d,
\end{cases}
\qquad W_N=\sum_{r=0}^{d}w_{N,r}e_r.
\tag{1}
\]
All weights are positive. This choice is dictated by the size of the basis elements, not by a positivity assumption on the physical operator. The full value-and-derivative norm satisfies
\[
\|e_r\|_{\mathcal J}\le CN^Cw_{N,r},
\tag{2}
\]
uniformly at both parities, by the
[low-degree interpolation and high-normal estimates](actual_conway_root_star_full_jet_localization.md),
§§2–3. Moreover,
\[
\log w_{N,r}=Ng(r/N)+O(\log N)\qquad(0\le r\le M)
\tag{3}
\]
uniformly on the closed low range. The high weight has zero logarithmic
rate. The comparison coupon \(W_N\) is never inserted into the invariant.

Let \(A\) be the expression obtained by taking one maximal connected unflagged region and viewing its attachment to the rest of the tree as the output. Its boundary has \(n\ge2\) inputs, each supplied by a type-\(L\) module. The type means that its strict complete-positive output labels range between zero and one half, with the corresponding boundary profile; it does not say that the full signed polynomial has only low coefficients. Internal edges carry the turn \(T\), and each multiplication vertex has at least three incident branches, counting its output. The reduced-hub theorem places \(A\) in
the following recursive rule
\[
E\ ::=\ LL\ \mid\ T(E)\ \mid\ EE\ \mid\ LE\ \mid\ EL.
\tag{4}
\]
For example, the smallest component is the product \(A=LL\) of two boundary modules, and its turned output is \(Q=T(LL)\). Larger components may contain turns and further products, exactly as in (4). Every boundary occurrence refers to a distinct original module. Write its
actual coefficient array as
\[
F_{i,N}=\sum_{r=0}^{d}f_{i,N,r}e_r,\qquad 1\le i\le n.
\]
The constants \(c_i\) measure the exponential contributions already accumulated inside those modules. They are not circle curvatures. Assume they are fixed real numbers, with one error \(e_N\to0\), uniform
over the specified physical input parameters, such that
\[
|f_{i,N,r}|\le
\begin{cases}
\exp\{N[c_i+g(r/N)+e_N]\},&r\le M,\\
\exp\{N[c_i+e_N]\},&r>M.
\end{cases}
\tag{5}
\]
These are coefficients of the whole module after its actual operations.
The split at \(M\) is a low/high coordinate split. It is not identified
with that module's physical core/alias decomposition.

Let \(A_N=A(F_{1,N},\ldots,F_{n,N})\) and \(Q_N=T(A_N)\). Let \(A^0\)
denote the same expression with each atomic input replaced by the pure
complete physical \(h_N=T(L_N)\). Set
\[
\Phi_A=\text{complete action of }C(hA^0),\qquad
\Omega=\sum_{i=1}^{n}c_i+\Phi_A.
\tag{6}
\]
The reference \(C(hA^0)\) is flag-free (its effective leaves are ordinary complete leaves, with no separate character attached to a multiplication hub), has \(n+1\ge3\) effective leaves,
and has a strict reduced state. For \(n=2\) it is \(C(hhh)\); for
\(n\ge3\) its source reduces to the earlier rule requiring composite factors on both sides of the closing product
by the exact flag-free adapter. Using this reference does not modify
\(A_N\).

## 2. Why closing against the probe bounds the norm

Replace every input coefficient by its modulus and compile
\(A_N^{\mathrm{abs}}\) from these nonnegative arrays using the same products
and turns. The positive Newton product and exact index reversal imply
coefficientwise
\[
|[e_r]A_N|\le [e_r]A_N^{\mathrm{abs}}.
\tag{7}
\]
The comparison uses the positive multiplication table and the exact reversal of coefficient indices. It does not treat the turn as a multiplicative map or estimate its norm separately. The full pairing extracts each output coefficient:
\[
[e_r]T(A_N)=\phi(e_rA_N).
\]
All basis products and the marked coefficient functional have
nonnegative coefficients in this calculation. Therefore
\[
\begin{aligned}
\|T(A_N)\|_{\mathcal J}
&\le CN^C\sum_{r=0}^{d}w_{N,r}|\phi(e_rA_N)|\\
&\le CN^C\phi(W_NA_N^{\mathrm{abs}}).
\end{aligned}\tag{8}
\]
Every first normal is retained, including high Newton coordinates
invisible at all nodes. The last scalar is nonnegative and its finite
source has only polynomially many index states, because the component
is fixed.

The same estimate holds sectorwise. Split each input into \(r\le M\)
and \(r>M\) arrays, and split \(W_N\) likewise. For each specified input
band assignment and probe band, the positive closed contraction bounds
the corresponding output contribution. In particular the high output
part of \(T(A_N)\) is bounded using the high probe \(W_N^{\mathrm{hi}}\).

## 3. Transferring the scalar inequalities to these arrays

Use the profiles defined in Section 1.
On these domains \(g\le\widetilde g\) and \(k\ge0\). The input bounds
(5) and probe (3) satisfy the earlier leaf upper hypotheses, with the
constants \(c_i\) added in every sector:
\[
\begin{array}{ll}
\text{low coordinates:}&\text{rate}\le g\le\widetilde g,\quad r/N\le1/2,\\
\text{high coordinates:}&\text{rate}\le0\le k.
\end{array}
\tag{9}
\]
The high coordinate range is a subset of the unrestricted range allowed
by the earlier alias inequalities. No physical alias identity or
complementary-color relation is needed for this comparison.

The precise input from those proofs is a scalar variational inequality.
For a fixed closed flag-free expression, put \(\widetilde g\) at each
chosen low leaf, \(k\) at each chosen high leaf, and the actual concave
gate action
\[
\begin{aligned}
m(x,y,z)={}&J(x+y)+J(z)-J(x)-J(y)\\
&-J(z-x)-J(z-y)-J(x+y-z)
\end{aligned}
\]
on its original domain
\[
D=\{x,y\ge0:\max(x,y)\le z\le x+y\le1\}.
\]
For every nonempty chosen high subset, the supremum of the action is
strictly below the pure complete action. The proof uses only the
displayed profiles and domains:

- In an \(A_2\) seed, the uniform block inequalities bound the \(AC\)
  and \(AA\) envelopes by its complete profile tangent minus \(1/100\). Here these two labels mean that one or both leaves use the competing profile \(k\), while the other uses \(\widetilde g\); they do not refer to the component operator \(A_N\).
  They allow the alias coordinate over its whole interval and thus
  also cover the present high band.
- At a single attachment, the exact square certificate and the
  remaining leaf tangent bound \(k+m\) against the child's profile
  tangent with a strict loss. A child loss passes through the pure
  \(\widetilde g+m\) step.
- Turns reverse the output index and tangent sign. Products add the
  concave gate tangent. At the closed root all free linear terms cancel.
- The isolated three-leaf case uses its separate endpoint \(A_2\)
  regrouping and three-alias bound. It covers \(n=2\) here with the
  same pair-sum and total-sum constraints.

These statements are proved in the
[block source argument](actual_conway_two_leaf_block_source_gap.md), §§3–5;
[uniform two-leaf inequality](actual_conway_uniform_two_leaf_block_alias_gap.md);
[single-leaf source induction](actual_conway_single_leaf_source_composition.md),
§§6–7, and its [analytic companion](actual_conway_single_leaf_alias_composition.md);
and the [isolated three-leaf proof](actual_conway_isolated_three_leaf_long_twist_volume.md),
§§1–3.

Their supporting-plane inequalities do not require the leaf arrays
to attain their upper profiles or to arise from a particular physical
color. The finite sums are bounded after taking coefficient magnitudes.
They therefore give the same upper bounds for arbitrary arrays satisfying
(5). The gap is not inferred by comparing two actual source values.

If \(C(W_NA_N^{\mathrm{abs}})\) was not initially parenthesized in the
earlier closed-composite rule, apply the exact flag-free rerooting to each
fixed band assignment. Every external array and its band remain intact.
All intermediate kernels remain positive. The complete pure action is
unchanged by the same exact source identity and its proved coefficient
asymptotics. The isolated case with three effective leaves is handled
separately as above.

Finite support still requires \(i+j\le d\); larger input sums are zero.
Turn and closing relations retain \(d/N=1-1/N\). Uniform factorial rates
have \(O(\log N)\) errors on the whole closed support. The supporting-plane
proof costs only \(O(1)\) under those affine shifts; compact continuity
and uniform closed rates give the same limiting bound. The single uniform
\(e_N\), the fixed number of input arrays, and the polynomial number of
states are absorbed by reducing a fixed positive gap.

## 4. The resulting bound and the contributions with high indices

Under the input hypothesis (5), there is \(\gamma_A>0\), depending on the fixed component but not its
physical input parameters, such that
\[
\phi(W_NA_N^{\mathrm{abs}})
\le \exp\{N[\Omega+o(1)]\},
\tag{10}
\]
and every sector with at least one high input or a high probe satisfies
\[
\text{positive sector}\le \exp\{N(\Omega-\gamma_A)\}
\tag{11}
\]
for all sufficiently large \(N\). Section 3 proves the nonempty high
cases; the all-low sector uses the original pure complete maximum.
Consequently
\[
\|Q_N\|_{\mathcal J}\le\exp\{N[\Omega+o(1)]\},
\tag{12}
\]
and, for a possibly smaller \(\gamma_A'>0\),
\[
\|(Q_N)^{\mathrm{hi}}\|_{\mathcal J}
\le\exp\{N(\Omega-\gamma_A')\}.
\tag{13}
\]
Every contribution containing a high input satisfies the same strict
bound. The superscript in (13) denotes the actual output Newton
coordinates \(r>M\), including their normals.

This is sharp as an action budget, not a lower statement for every
arbitrary input array. For reference arrays \(e^{Nc_i}h_N\), the low
probe is coefficientwise comparable to \(h_N\) within powers of \(N\).
Both positive coefficient families have the uniform closed rate \(g\)
with \(O(\log N)\) error, so
\[
N^{-C}h_N\le W_N^{\mathrm{lo}}\le N^Ch_N
\]
coefficientwise. Positivity gives the same exponential rate \(\Phi_A\)
for the reference low-probe contraction. The high sectors already have
a strict loss. Thus \(\Omega\) is the pure reference action, rather than
the generic bare-turn cost \(2G_0\) added to an existing action.

## 5. Which indices can attain the upper rate

The preceding estimate removes every term with a high input or a high output index. To use the remaining terms in a larger tree, we also need to know where their indices can be concentrated. Let \(y\) denote the original primitive variables of \(C(hA^0)\),
including the scaled probe index \(u=r/N\) and the \(n\) effective
input indices \(a_i\). The all-low comparison has the uniform closed
upper action
\[
\sum_i c_i+g(u)+\sum_i g(a_i)
                      +\sum_{\text{retained gates}}m.
\tag{14}
\]
This upper envelope is the genuine pure complete action of that reference expression. Arbitrary input arrays need not attain it and may even vanish. The
strict-state/compiler theorem gives a unique strict optimizer \(y_*\).
Its probe index \(\beta\) and effective input indices \(a_i^*\) lie in
\((1/4,1/2)\); in the isolated three-leaf case they are
\(\arctan(2)/\pi\). The strict gate and angle Hessian gives local strict
curvature. Hence for each fixed neighborhood \(U\) of \(y_*\), there
is \(\gamma_U>0\) such that
\[
\text{all-low positive sum outside }U
\le\exp\{N(\Omega-\gamma_U)\}.
\tag{15}
\]
The effective parameter range is checked in the
[intrinsic probe geometry](actual_conway_unflagged_probe_geometry.md), §§1–3.
Estimate (15) is uniform under (5), since only upper profiles are used. It is
stated in the original resolution and coordinates of this component,
even if another rooting was used in §3 for the high-sector bound.
No transformed state index is identified with an original physical color.

Only a compact regular low-index window around \(\beta\) can therefore
attain \(\Omega\); the effective input indices lie in compact regular
windows around their own \(a_i^*\). This gives an explicit coefficient
loss-transfer statement. Suppose one fixed compact interval \(I_i\)
contains \(a_i^*\) in its interior, and for a specified physical
parameter subfamily,
\[
|f_{i,N,r}|
\le\exp\{N[c_i+g(r/N)-\delta+e_N]\}
\quad\text{when }r/N\in I_i,\qquad \delta>0.
\tag{16}
\]
Choose \(U\) so its \(i\)-th input coordinate lies in \(I_i\).
The clean sum inside \(U\) loses \(\delta\), its outside loses
\(\gamma_U\), and every high sector loses \(\gamma_A\). By (8),
after reducing the smallest margin,
\[
\|Q_N\|_{\mathcal J}\le\exp\{N(\Omega-\eta)\},
\qquad \eta>0,
\tag{17}
\]
uniformly over that subfamily for all sufficiently large \(N\).
Only coefficient upper bounds enter this proof. It does not infer a
physical-color gap from positivity of the signed source or convergence
of derivatives.

The regular windows and the same finite comparison are also inputs to
canonical spectral localization. That analytic step is separate from
the finite norm and loss-transfer estimates proved here.

## 6. Why this exponent is the required geometric one

A boundary profile gives the optimized complete action of an open subtree as a function of its scaled output label \(b\). Suppose each boundary module has the rigid positive profile
\(f_i(b)=g(b)+c_i\). Independence of its internal optimization at a
fixed boundary label gives
\[
f_A(b)=f_{A^0}(b)+\sum_i c_i,\qquad
f_Q(b)=f_A(1-b),\qquad Q=T(A).
\]
The intrinsic pressure means the maximum obtained by pairing that output profile with one complete leaf. In the geometric boundary coordinates this is the specialization \(X=1\), and it is
\[
\Omega_Q=\max_{0\le b\le1/2}[g(b)+f_Q(b)]
        =\sum_i c_i+\Phi_A=\Omega.
\tag{18}
\]
This is the pressure entering a rigid spine when \(Q\) is a satellite.
The probe in (8) estimates that boundary pressure; it has not added a
physical crossing circle. The absolute constants and pressure
identification use the [intrinsic probe adapter](actual_conway_unflagged_probe_geometry.md), §4,
the [rigid-profile geometry](actual_conway_rigid_spine_and_flagged_tree_geometry.md),
and [complete-mask geometry](actual_conway_general_strict_mask_geometry.md).

Every maximal unflagged component of a strict reduced tree has only
type-\(L\) modules or ordinary leaves on its boundary: adjacent flagged
hubs send type-\(L\) messages, and the remaining original leaf flags
are zero. Its parent-facing root has at least two other branches, so
\(n\ge2\). This is the component scope needed for alternating flagged
and unflagged reduction.

The result does not turn the comparison bands into physical aliases,
assume positivity of actual signed modules, or prove a local packet.
No source equality is promoted to tangle isotopy.

The argument uses the exact earlier rational block certificates without changing their domains. No numerical asymptotic fit enters the norm or loss-transfer proof. The separate geometric adapter supplies the effective parameter range and the equality of pressures used above.
