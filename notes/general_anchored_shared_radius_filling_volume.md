# Full original long filling from anchored shared-radius certificates

theorem, 31 October 2026. At most $2R$ finite tests on shared face radii imply the full original independently long-filling volume theorem. These tests strictly extend balance at the complete packing for a fixed marked source. They are not asserted for every certified diagram. The proof makes no exchange of a maximum and an infimum and uses no coefficientwise LEFT comparison.

## 1. The original source and the finite certificate

Fix an original marked flat plat $D$ with $R$ ordered ports $(x_e,b_e,c_e,y_e)$, the original adjacent protected MAIN faces $u,v$, and its labeled simple-white convex right-angled certificate for the complete augmented exterior $Y_D$. Write $\Phi_D=\operatorname{Vol}(Y_D)/(2\pi)$. Every ordinary face variable below is positive; the protected variables remain exactly zero. Each vector $L=(L_f)$ is shared across the entire original face incidence graph. These source variables are curvatures, not Euclidean disk radii.

Let $Q(x,t,y)$ be the absolutely normalized [complete triangle action](actual_cross_cofactor_marked_action.md). Its homogeneity is $Q(\lambda x,\lambda t,\lambda y)=Q(x,t,y)+\tfrac12\log\lambda$. Define

$$
\begin{aligned}
X_e(L)&=Q(x_e,b_e,y_e)+Q(x_e,c_e,y_e),\\
H_e(L)&=\max\bigl(\{X_e(L)\}\cup\{\log b_e:b_e>0\}\cup\{\log c_e:c_e>0\}\bigr).
\end{aligned}\tag{1}
$$

The two possible anchored rates are

$$
\begin{aligned}
A_{e,\mathrm L}(L)&=\max\{\log c_e,Q(x_e,b_e,y_e)+\tfrac12\log c_e\},&&c_e>0,\\
A_{e,\mathrm R}(L)&=\max\{\log b_e,Q(x_e,c_e,y_e)+\tfrac12\log b_e\},&&b_e>0.
\end{aligned}\tag{2}
$$

The labels $\mathrm L,\mathrm R$ mean LEFT and RIGHT; $L_f$ is a shared face variable. If the overloaded middle is protected, that anchor is absent because the exact finite sector is zero. Set

$$
\mathcal C_{e,s}(L)=A_{e,s}(L)+\sum_{f\ne e}H_f(L)
-\sum_{j\ \mathrm{ordinary}}\log L_j.\tag{3}
$$

Here $f\ne e$ in the first sum indexes ports. There are at most $2R$ surviving anchors. Suppose that for **each** surviving anchor there exists a fixed positive ordinary shared vector $L^{e,s}$, with the same protected zeros, satisfying

$$
\mathcal C_{e,s}(L^{e,s})<\Phi_D.\tag{4}
$$

Different anchors may use different whole vectors. Variables shared by several ports are never optimized independently inside one product. Equivalently, $\inf_L\mathcal C_{e,s}(L)<\Phi_D$; even if that infimum escapes, strict inequality supplies a finite positive witness. No minimizer is required. If no anchor survives, the full numerator is already all-CROSS and its existing theorem applies directly.

Then every independently signed, fixed, sufficiently long filling vector in the original parity convention satisfies

$$
\lim_{N\to\infty}\frac{2\pi}{N}\log|K_N|
=\operatorname{Vol}(\text{the actual filled exterior}).\tag{5}
$$

For the prescribed knot parity, this is the actual knot invariant. The threshold depends on $D$ and the witnesses. There is no bound on ratios of the independent twist lengths, no joint growing-twist/level limit, and no uniformity in growing diagram size.

## 2. The source estimate at one shared vector

The [global LEFT theorem](actual_global_left_weighted_spectral_envelope.md) proves (2) as a uniform weighted absolute upper rate at all face phases and all real spectral values. It retains both outside products, both parity partitions, and the shrinking final spectral cap. Reflection gives RIGHT. This is a value bound, not a coefficientwise inequality.

The [exact cofactor interpolation theorem](actual_cross_cofactor_factorization.md), Section 8, bounds CROSS coefficientwise by $C\log^2(N+1)$ times its positive zero-spectral CROSS polynomial on the entire real spectral interval. That polynomial has weighted rate $X_e$, by the original determinant and half-block normalization. This includes a single protected outer face and protected middles. The outer faces cannot both be protected: their original edge is MATCHING, while the protected edge is MAIN. Thus $x_e+y_e>0$ at every witness.

For $t>0$ and $x+y>0$, the actual triangle action satisfies $Q(x,t,y)>\tfrac12\log t$; its nonstrict version already follows from the endpoint monomial. Therefore

$$
A_{e,\mathrm L}\le H_e,\qquad A_{e,\mathrm R}\le H_e.\tag{6}
$$

For example, $Q_b+\tfrac12\log c\le Q_b+Q_c=X_e$. A protected overloaded middle gives an exactly zero sector, rather than an estimate involving $\log0$. Hence $H_f$ bounds CROSS, LEFT and RIGHT at every unanchored port on the same common face Cauchy torus.

Take any exact path sector with a one-sided port, and choose one such port $(e,s)$ as anchor. Evaluate its entire original shared coefficient extraction at $L^{e,s}$, using $H_f$ at the other ports. The original ordinary target is $d=N-1$ at each ordinary face and zero at $u,v$. Replacing $d/N$ by $1$ changes the fixed-radius normalized logarithm by $O(N^{-1})$. If $\gamma$ is smaller than the minimum of the finitely many positive gaps in (4), all sufficiently large $N$ therefore satisfy

$$
|Z_{\mathrm{sector}}(\sigma_1,\ldots,\sigma_R)|
\le e^{N(\Phi_D-\gamma)}\tag{7}
$$

uniformly on the full real spectral cube. All original source scalars and normalization conventions remain those of the homogeneous theorem. Every phase stays inside the original local sector until the valid weighted absolute estimate is taken.

The LEFT/CROSS/RIGHT partition is disjoint at both parities. At even $N=2m$, LEFT has $j\le m-1$, CROSS has $i\le m-1$ and $j\ge m$, and RIGHT has $i\ge m$. At odd $N=2m+1$, LEFT has $j\le m-1$, CROSS has $i\le m\le j$, and RIGHT has $i\ge m+1$; the central zero-step belongs to CROSS once. Their finite sum is the exact full numerator. There are at most $3^R-1$ sectors in full minus CROSS. Assigning an anchor to each proves (7) for that entire difference, with a smaller gap. Only $2R$ witness vectors are needed; no atomwise optimization is performed.

The remainder has spectral degree at most $d$ in every variable. The cosine Bernstein bound for $\sigma_i=-2\cos(2\pi\delta_i)$ extends (7) to a fixed thin complex strip, at cost $\exp[2\pi d\sum_i|\operatorname{Im}\delta_i|]$. Choose its height below the fixed gap and shrink once more for source Cauchy derivatives.

## 3. The entire original Fourier period

Apply the analytic argument in Section 4 of the [whole-domain sector theorem](actual_global_diagonal_spectral_sector_gap.md) to this remainder polynomial. That argument requires the whole-strip bound, polynomial cosine dependence, and the original sine and Gaussian factors; it does not require the polynomial itself to be diagonal. The original sine factor vanishes at each endpoint $\pm\tfrac12$, and its first derivative has equal endpoint values. The source cosine and Gaussian also have equal endpoint values. Three integrations by parts in each coordinate retain the second-derivative boundary current and give charge decay $\prod_i|\ell_i|^{-3}$. After the original weight $\prod_i|\ell_i|$, the whole-domain charge sum converges absolutely. Fixed-strip Cauchy bounds apply only to the source; Gaussian derivatives are taken on the real cube. Thus

$$
|I_{\mathrm{full}}-I_{\mathrm{cross}}|
\le C_D\prod_i(1+|n_i|)^3e^{N(\Phi_D-\gamma')},
\qquad\gamma'>0.\tag{8}
$$

No infinite sharp-cube series has been split. Both endpoints and their actual currents, all nonzero charges, and the original framing phases are retained.

The [whole all-CROSS theorem](general_all_cross_long_filling_volume.md) supplies a nonzero relative asymptotic for fixed independently signed sufficiently long $n_i=\epsilon_i-2p_i$. Its actual filled critical rate tends to $\Phi_D$, with deficit $O_D(\sum_i n_i^{-2})$. Choose every $|p_i|$ above the geometric and analytic thresholds and so that this deficit is less than $\gamma'/2$. Equation (8) is exponentially smaller than the original all-CROSS contribution, giving

$$
\frac{I_{\mathrm{full}}}{I_{\mathrm{cross}}}
=1+O_{\mathbf n}(e^{-c_{\mathbf n}N}).\tag{9}
$$

The original normalizing characters and nonzero polynomial factors do not change the exponential limit. This proves (5). The argument uses spectral identities at the fixed root and imposes no extra generic-$q$ derivative hypothesis.

[Complete-radius balance](general_complete_radius_balance_filling_volume.md) implies (4): use the geometric vector for every anchor. There $H_f=X_f$ at all ports and each surviving $A_{e,s}<X_e$. The following example shows that the converse fails for a fixed marked source.

## 4. An original flat plat failing complete-radius balance

Use three standard adjacent cups and caps with the literal zero-based slot word

$$
(1,3,2,1,3),\tag{10}
$$

marking the first original top cap. Its actual ordered quartets are

$$
(1,0,4,2),\ (2,0,5,3),\ (4,2,6,5),\ (1,4,0,6),\ (6,5,0,3).\tag{11}
$$

The protected faces are $0,1$, and faces $2,\ldots,6$ each retain target $d$. The original compiler gives exactly these data. The ten triangles form a simple sphere with seven vertices and fifteen edges; the protected edge is MAIN. No general Morse-to-flat-plat adapter or isotopy is assumed.

Let $z=\sqrt5$. An exact marked packing has lines $0:Y=0$, $1:Y=2$, and these disks, listed as horizontal center, vertical center, Euclidean radius:

$$
\begin{aligned}
2&=(z-1,1,1),&6&=(1-z,1,1),\\
3&=(0,(3-z)/2,(3-z)/2),\\
4&=(0,(1+z)/2,(3-z)/2),\\
5&=(0,1,z-2).
\end{aligned}\tag{12}
$$

Every graph edge other than the marked line-line contact is an exact tangency; every nonedge pair has strictly disjoint support. These are twenty finite pair checks. The marked lines touch at infinity. The [simple-sphere packing construction](actual_smoothed_source_capacity_blocks.md) supplies the actual labeled right-angled certificate, retaining the original matching and source pairings. The complete curvature vector is

$$
L^{\mathrm{geom}}=
\left(0,0,1,\frac{3+\sqrt5}{2},\frac{3+\sqrt5}{2},2+\sqrt5,1\right).\tag{13}
$$

At the first and fourth ports, complete balance fails. The certified evaluation below gives

$$
-0.10315<X_0(L^{\mathrm{geom}})-\log L^{\mathrm{geom}}_4<-0.10190.\tag{14}
$$

The fourth port has the same value by reflection. Nevertheless, the following rational shared vectors satisfy (4). Each vector lists $(L_2,L_3,L_4,L_5,L_6)$; both protected values stay zero.

| Anchor, with zero-based port index | Shared ordinary vector | Certified gap $\Phi_D-\mathcal C$ |
|---|---|---|
| 0 LEFT | $(3,4,3/2,5,1)$ | $>0.50$ |
| 3 RIGHT | $(1,4,3/2,5,3)$ | $>0.50$ |
| 1 LEFT | $(3/2,5,2,2,1)$ | $>0.71$ |
| 4 RIGHT | $(1,5,2,2,3/2)$ | $>0.71$ |
| 2 LEFT | $(2,6,2,18,1)$ | $>1.35$ |
| 2 RIGHT | $(1,6,2,18,2)$ | $>1.35$ |

These are all six surviving anchors. At the other four sides, the sector vanishes because its overloaded middle is protected. The conservative uniform gap $0.45$ certifies the full-source conclusion.

In conventional braid indexing the word is $\sigma_2,\sigma_4,\sigma_3,\sigma_2,\sigma_4$. Choosing the first two exponents odd and the last three even makes one main component by the original cup/cap permutation. All five sufficiently long fixed parameters remain independent in magnitude and sign. Restricting every full exponent to a multiple of $3$ gives exact bridge number $3$ by the [Fox certificate](actual_fox_coloring_exact_plat_bridge.md); this congruence is not required for the volume statement.

The example proves strict enlargement of the tests for a fixed marked source. It does not prove strict inclusion of the underlying unmarked knot families: another mark or presentation might satisfy the older balance test.

## 5. Rigorous interval evaluation

No floating optimizer enters the certificate. For a nonnegative triangle $w$ with at least two positive entries, set

$$
\begin{aligned}
D&=\sqrt{w_1w_2+w_2w_3+w_3w_1},\qquad a_i=\arctan(w_i/D),\\
Q(w)&=\sum_{w_i>0}\left\{
\frac{\Lambda(a_i)+\Lambda(\pi/2-a_i)}\pi
+\frac{a_i}\pi\log w_i\right\}.
\end{aligned}\tag{15}
$$

For a triangle with just one positive entry, use $Q(w)=\tfrac12\log w_i$ exactly. Formula (15) is the absolutely normalized original source identity, with $\sum_i a_i=\pi/2$. Hence

$$
\Phi_D=\sum_eX_e(L^{\mathrm{geom}})
-\sum_{f=2}^6\log L_f^{\mathrm{geom}}.\tag{16}
$$

The absolutely convergent Fourier series gives, for every real $a$,

$$
\Lambda(a)=\frac12\sum_{n=1}^M\frac{\sin(2na)}{n^2}+r_M(a),
\qquad |r_M(a)|\le\frac1{2M}.\tag{17}
$$

The remainder bound follows from $\sum_{n>M}n^{-2}\le M^{-1}$. The [portable audit](../experiments/audit_general_anchored_shared_radius_filling_volume.py) evaluates the $M=1024$ sum with Arb at 192 bits, then adds this analytic tail ball. Square roots, $\pi$, arctangents, logarithms, maxima and all arithmetic retain enclosing balls. There is no unproved floating solve, rounded optimizer or numerical asymptotic limit. The [saved result](../experiments/general_anchored_shared_radius_filling_volume_results.json) encloses $\Phi_D$ in $(5.17452,5.18696)$, and every table entry has its asserted strictly positive lower bound. The packing checks use exact algebra in $\mathbb Q(\sqrt5)$.

The checks cover five original ports, ten triangles, fifteen edges, twenty exact pair supports, two failed geometric balance tests, and six fixed rational whole-source witnesses. They certify this finite example and its quantitative inequalities; Sections 1–3 prove the general analytic transfer.

## 6. What remains open about general optimized capacities

A fixed shared vector gives a valid Cauchy bound. In contrast, one cannot replace $\inf_L\max\{F_0(L),F_1(L)\}$ by $\max\{\inf_LF_0(L),\inf_LF_1(L)\}$. In particular, the LEFT value envelope is not an exact finite decomposition into an identity polynomial and a half-triangle polynomial.

This distinction has a precise convex-dual form. Let $C(\alpha)$ be the original triangle coefficient entropy on $\alpha_x+\alpha_b+\alpha_y=\tfrac12$. The source identity is

$$
Q(x,b,y)=\max_\alpha\bigl\{C(\alpha)+\alpha_x\log x+\alpha_b\log b+\alpha_y\log y\bigr\}.
$$

Thus the concave entropy associated with the LEFT weighted envelope admits mixtures

$$
q_c=1-\frac t2,\qquad(q_x,q_b,q_y)=t\alpha,
\qquad\text{entropy}=tC(\alpha),\qquad0\le t\le1.\tag{18}
$$

At $t=0$ this is pure $c$; at $t=1$ it is a triangle plus pure half-$c$. Protected input coordinates force their $\alpha$ entries to vanish. This is generally not the actual one-sided entropy $E$. Compact finite-dimensional convex duality converts the optimized envelope into this problem with concave local entropies, including limiting multipliers; it does not remove interior $t$. The unanchored $H$ additionally permits mixtures with complete CROSS and pure-$b$ atoms.

The [identity forest reduction](actual_fejer_diagonal_identity_forest_reduction.md) controls the exact identity endpoint $t=0$. A [fixed-triangle capacity loss](actual_fixed_triangle_boundary_capacity_gap.md) controls $t=1$. At fractional $t$, the positive triangle has a changed row supply. Simply retaining its unscaled geometric angles changes the face stars by $(1-t)(\alpha-e_c/2)$, which need not vanish. The old hybrid representation therefore cannot be reused for an arbitrary mixture without further proof. The present theorem supplies a strictly broader sufficient certificate for marked sources; whether every original certified diagram passes an optimized sector or anchor test remains open.

## 7. Exact certificate checks

The six rational certificates and twenty exact pair checks have smallest certified gap greater than $0.5023$. They use the specified quartets, first mark, exact packing, simple-sphere certificate and six surviving sides. Numerical optimization and finite asymptotic samples are not proof inputs.