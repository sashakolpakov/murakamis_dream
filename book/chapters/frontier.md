# The current general frontier

The target is a theorem at **every fixed bridge width**, with independently long signed twists. The general volume equality remains open. Exact source formulas, the marked geometric action, and much of the local analysis are now available; the unresolved step is the global quantum period.

## The class and the order of quantifiers

Fix an essential $2k$-strand plat diagram $D$, $k\geq2$, with a hyperbolic augmented exterior $Y_D$ and its actual primitive cusp markings. The [general target](../../notes/general_augmented_plat_long_twist_target.md) asks for a threshold $T(D)$ such that

$$\min_i |m_i|>T(D)\quad\Longrightarrow\quad
\lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K_{D,\mathbf m})|
=\operatorname{Vol}(S^3\setminus K_{D,\mathbf m}).$$

The diagram and every signed twist number $m_i$ are fixed **before** the quantum level $N$ tends to infinity. The prescribed parity pattern must give a knot. Hyperbolicity of a knot does not automatically certify every chosen augmentation.

Under the actual positive marked gluing certificate, the [geometric filling theorem](../../notes/general_augmented_plat_long_filling_quantifiers.md) already supplies a geometric threshold, including independently long partial fillings. It is the quantum threshold in the displayed implication that remains unproved for general plats.

## What is established on this path

| Step | Current conclusion | Remaining limitation |
| --- | --- | --- |
| Original finite source | Exact all-color formulas at arbitrary fixed width; shared Kirchhoff flows, Fourier charges and all required normals retained | An exact formula alone does not estimate its coherent sum |
| Ordinary local factors | Selected action and nonzero amplitude on full physical complex compacts; a global Legendre chart for that selected action | The channel remains a genuine discrete color; normal bounds have their stated domains |
| Actual geometry | A positive marked certificate gives the complete geometry, its nearby stationary branch and the absolute hyperbolic-volume anchor | Existence of the geometric critical point does not prove quantum contribution |
| Exceptional matching edge | Exact entire root kernel and a selected nonzero relative packet near the actual geometric frame, jointly in complex degree and magnetic coordinates | A local packet does not determine its coefficient in the original period |
| Endpoint and normals | Closing-arc bounds and a specified full generic operator lift with subexponential derivative cost near the fold | Individual derivative amplitudes and the remaining contour are separate questions |
| Complete local source | Nonzero marked density and local folded-channel Gaussian at both level parities | The framing orbit and the coefficient in the original global cycle remain uncomputed |
| Framing dependence | The actual local density is a nonzero constant times $-dr\wedge ds/[s(1+s)]$ | Its relative boundary pairing with the original source cycle remains unproved |
| Common boundary chart | All six original numerator types and their literal duals fit one marked chart; the complete uncontracted product has controlled genuine jets | Requires the labeled right-angled certificate; no estimate of the contracted sum follows |
| Boundary first-normal defect | Two explicit root-channel insertions determine it, with an $O(N^2)$ Hilbert–Schmidt norm bound by finite Plancherel | The scalar derivative is separate; the full root-channel norm still needs a geometric estimate |
| Odd framing source | An exact normalized difference of the two adjacent physical bands recovers the original invariant at every fixed width | Its local logarithmic residue does not yet determine the original global cycle coefficient |
| General long fillings | A conditional source-to-filling theorem with the correct independent-slope quantifiers | Its general complex packet, nonzero density germ and whole-source gap still need proof |

The [common boundary chart](../../notes/actual_original_network_resonant_boundary_chart.md) and [network envelope](../../notes/actual_original_network_resonant_source_envelope.md) assemble the local estimates on the original marked network, retaining both folded parities, every cup, and the actual generic dual. They require the labeled convex ideal right-angled polyhedron, its original cut and its white-reflection prefix dictionary; a positive triangulation alone does not supply these data. Their shrinking deficits $s_i=N-1-2a_i$ are **internal Casimir labels**. They are not the external filling-color defects $h_i=N-j_i$; a bound in the former variables does not supply the latter's complex packet or alias gap.

The [explicit normal adapter](../../notes/actual_explicit_root_channel_normal_adapter.md) gives a general algebraic reduction. Write $\mathcal A=C_0-z_0\operatorname{Id}$ for the full root channel with its scalar part removed, and put $H_{ss}=2N\sum_{j=1}^s(1-e^{2\pi i j/N})^{-1}$. For the actual Toeplitz insertion $X(p)_{rs}=p^{r-s}/N$, define $\Delta_\epsilon(p)=C_\epsilon(X(p))-z(\epsilon)X(p)$. Then

$$\Delta'_0(p)=\eta X(p)-\mathcal A(X(p)H),\qquad \eta I=\mathcal A(H).$$

This retains the genuine derivative of the defect using two specified root insertions; it does not determine $z'_0$ from $C_0$. Centering $H$ and applying finite Plancherel gives $\|\Delta'_0(p)\|_{\mathrm{HS}}\leq C_A N^2\|C_0\|_{\mathrm{HS}\to\mathrm{HS}}$ when $|\log|p||\leq A/N$. On $\operatorname{span}\{I,H\}$, every such channel acts by $\left(\begin{smallmatrix}z_0&\eta\\0&z_0\end{smallmatrix}\right)$, so the additional part is square-zero. Arbitrary braid coupons have not thereby been decomposed into such channels. The geometric cycle coefficient and the full mixed-color estimate remain the two global tasks.

The [root-insertion transport theorem](../../notes/actual_root_channel_H_period_transport.md) now gives these two insertions an exact rational-clock formula with a retained logarithmic head. It equals the specified Gamma continuation by a proved shift, divisor and growth argument. On the controlled head charts its size is $O(N^2\log N)$, and it gives exactly the original finite root periods. Changing from the literal clock polynomial to this representative changes the continued boundary currents: every integer carry has an explicit residue involving both the surrounding source and its head derivative. These terms are retained. The theorem provides the insertion and its transport law; the deformation of the original cycle and evaluation of its relative ends remain to be proved.

The [odd framing source theorem](../../notes/actual_source_preserving_odd_framing_period.md) closes a further algebraic gap. Let $T_1,T_{-1}$ be the two adjacent unwrapped physical bands and $q_0=e^{\pi i/N}$. For the original routed channel $C_0$ and coherent cut $e_t$,

$$z_0=\frac{\operatorname{Tr}[e_t C_0(T_1-q_0T_{-1})]}{\kappa_N(t)},\qquad
\kappa_N(t)=1-q_0-t^{N-1}+q_0(1-t)^{N-1}.$$

For real $0\leq t\leq1$, $|\kappa_N(t)|\geq N^{-1}$ at every level. This is the unchanged original scalar, with its original factors and both support cycles. On the certified geometric chart the underlying odd form has a nonzero logarithmic residue. The coherent base weight $N\beta_a(t)/\kappa_N(t)$ remains explicit; the residue alone is not the weighted global period. At $r\sim N$, the two classical band symbols cancel to order $N^{-1}$, so the joint quantum error must be controlled before dividing by $\kappa_N$. The boundary estimate for the contracted period and the actual cycle's winding are still required.

The [marked logarithmic class](../../notes/actual_odd_framing_logarithmic_class.md) makes one part of this task algebraic. On a closed geometric two-cycle, the underlying finite-$q_0$ form has period $(2\pi i)^2c_D(n_1+q_0n_0)$ for two integer winding numbers. A nonzero pair gives $|n_1+q_0n_0|\geq\sin(\pi/N)\geq2/N$, even when $n_1+n_0=0$. Thus a classical cancellation can survive the quantum normalization with nonzero size. The original source's winding pair and its weighted quantum realization still have to be proved; the theorem does not assign them by selecting a convenient cycle.

The [correlated band-ratio theorem](../../notes/actual_correlated_boundary_band_ratio.md) now controls the normalization error for the original uncontracted products on the six-type boundary chart. The adjacent bands share one holomorphic relative remainder of size $O(N^{-1})$ on a head disk of radius proportional to $N$. Cauchy's estimate makes their difference $O(N^{-2})$. Keeping the exact cup characters and all finite model factors then gives

$$\frac{S_N(+1)-q_0S_N(-1)}{\kappa_N S_N(-1)}
=\frac{B_N(+1)/B_N(-1)-q_0}{\kappa_N}+O(N^{-1}).$$

Here $S_N$ is the actual charged product with its exposed scalar cap removed, and $B_N$ is the specified model evaluated at the finite clocks and channel labels. Its quotient has not been replaced by the classical symbol or proved to have a nonzero limit. This theorem does not yet pass through the internal sums or Gaussian integration, and it does not cover extra routed factors outside the six controlled types.

The [selected-factor theorem](../../notes/actual_augmented_plat_selected_factor_localization.md) is useful here: for the certified right-angled cut, exactly two physical-support failures can be placed at the ends of one chosen crossing-circle edge. Every other ordinary factor is on the selected physical packet. An all-central selected common frame **cannot exist**; moving all factors into that domain is therefore not an available shortcut.

## The exceptional edge now has an exact algebraic description

Its completed operator is the original normalized polynomial

$$E_a=D_a^{-1}p_a(\Omega).$$

This is a generic identity before root specialization, so it retains the colliding channels and their true normal derivatives. The [source polynomial theorem](../../notes/actual_matching_edge_geometric_target_polynomial.md) also fixes which geometric target is required: $z=\operatorname{Tr}(B_{\rm in}^{-1}B_{\rm out})=2-4/c^2$, with the actual primitive rectangle ratio $c$.

The [marked-word bound](../../notes/actual_matching_circle_rectangle_bound.md) proves $0<c\leq1$ for every circle in the certified complete class, including retained half twists. Otherwise that actual holonomy word would be elliptic in a freely acting complete-manifold group. Thus the actual target is at most $-2$; equality is a genuine parabolic case.

Every zero of $p_a$ is above $2$. Its canonical logarithm selects a scalar action on the slit plane, without inventing a complex finite color. The [generating-action theorem](../../notes/actual_matching_edge_polynomial_geometric_action.md) proves the general local character relation

$$R+R^{-1}=2-(2-\lambda_{\rm in})\frac{z+2}{z-2},$$

with the branch and additive scalar normalization fixed by the original source. This is a general local A-structure result. It is not yet the global knot quantum A-operator or its selected period.

![The exact polynomial-resolvent period, the geometric target and spectral endpoint, and the remaining global contribution problem.](../figures/exceptional-period.png)

The [exact operator period](../../notes/actual_matching_edge_continuant_operator_period.md) keeps the distinction explicit:

$$p_a(\Omega)=\frac{1}{2\pi i}\oint_\Gamma p_a(z)(zI-\Omega)^{-1}\,dz.$$

Its Green entries have original forward and backward continuants and the full characteristic denominator. Their [selected action and generic-normal bounds](../../notes/actual_matching_edge_cross_central_green_action.md) hold when the two actual physical rows are strictly on opposite sides of the midpoint on the stated common spectral domain, which includes every fixed compact real interval below $-2$. On the anti-diagonal, the Green entry is exactly negative for real $z<-2$. Neither this sign nor the scalar action proves that the geometric saddle contributes to the contour.

The endpoint $2$ also has separate polynomial and full resolvent estimates. Their [closing-region assembly](../../notes/actual_casimir_closing_region_bound.md) now controls the **whole original integrand**, including fixed generic derivatives, on shrinking arcs in each fixed slit cone. Its cost is subexponential for any radius tending to zero. This does not control the remaining contour. The closing point $+2$ is distinct from the possible geometric target $-2$, which is outside the current off-spectrum Green theorem.

## The geometric point lies across an exact support boundary

The [actual operator kernel](../../notes/actual_matching_edge_antidiagonal_operator_packet.md) has a nonzero relative amplitude on its full strict physical complex tube. Its anti-diagonal entries are positive squares. But the [geometric support calculation](../../notes/actual_matching_edge_geometric_support_zero_chamber.md) shows precisely why that result does not yet suffice: in the prescribed-pair frame, both exceptional ordinary factors have normalized total $0<\operatorname{Re}\sigma<1/2$. The actual change of pairing gives a row separation $\delta=1-\sigma$, so $\operatorname{Re}\delta>1/2$. All the other kernel-domain inequalities hold; the bandwidth inequality fails.

This is an exact source constraint. At finite level, $p_a(\Omega)$ has bandwidth $a$, and its physical entries with $h>a$ vanish, including their genuine generic derivatives. Allowing complex coordinates inside the old tube, or assembling more copies of that same packet, does not reach this geometric chamber.

There is now an [entire finite continuation](../../notes/actual_matching_edge_entire_operator_kernel.md) across the boundary:

$$\mathcal K_{N,a}(h,u,l)=\frac{\beta_a^2}{N}
\prod_{r=a+1}^{N-1-a}2\sin\frac{\pi(h+r)}{N}
R_a(z_1;c_h)R_a(z_2;c_h).$$

Here $\beta_a=s_{2a}/s_a^2$, $s_n=\prod_{r=1}^{n}2\sin(\pi r/N)$, $\sigma_N=N-1-h$, $z_1=q^{-\sigma_N+2u}$, $z_2=q^{\sigma_N-2l}$, and $c_h=\cos(\pi h/N)$. This polynomial parameter differs from the cusp rectangle ratio above. The polynomials $R_a$ are the original finite determinant polynomials. Every apparent denominator and monomial phase cancels **before** taking a limit. The formula matches the whole physical grid: its residual sine product or its polynomial factors retain the forbidden-entry zeros. At the maximal folded channel the residual product is empty for odd levels and has one factor for even levels.

The [explicit global frame](../../notes/actual_augmented_plat_real_deficient_frame.md) makes the geometric test uniform: on every certified matching cut, the exceptional normalized degree can be set to the real value $\sigma=1/6$. Both magnetic rows are complex, and all other ordinary factors remain selected and physical. Exact formulas identify the geometric upper and lower characteristic branches against the reflected source anchor.

The [deficient-degree factorization](../../notes/actual_q_hahn_deficient_degree_packet.md) now separates the forced lattice zeros from a Jacobi determinant with positive roots. The [joint deficient packet](../../notes/actual_q_hahn_joint_deficient_degree_packet.md) then gives a selected action, a nonzero amplitude and relative error $O(N^{-1})$ near this actual geometric frame, with both degree and magnetic coordinates complex. A positive tail, a bounded low block and their exact Schur complement supply the zero-free domain. The absolute anchor is an exact reflection of the original source.

![The entire root kernel reaches a controlled complex geometric packet across the limiting support boundary; the original global period contribution remains open.](../figures/support-wall.png)

The [generic boundary-source theorem](../../notes/actual_generic_boundary_gauge_and_source.md) retains the actual large compiler channel $m=N-1-a$. The large and small channels coincide at the root but have different quantum derivatives. The [full generic lift](../../notes/actual_matching_edge_generic_deficient_operator_lift.md) now also includes every boundary factor, using the specified moving-period factorial. On a slightly nonreal geometric degree chart, every fixed genuine derivative has subexponential relative cost when $(N-1-2a)\log N=o(N)$. This is the literal generic polynomial operator, with its original moving scalar. The upper estimate does not prove a nonzero leading normal amplitude.

The [absolute regulator comparison](../../notes/actual_matching_edge_deficient_packet_regulator.md) proves that the normalized degree reflection has scalar one and preserves the actual Bloch regulator. The literal cups and turn supply a winding character, which is one on the lattice but must remain in the continued action. The specified generic lift has the opposite root character; restoring its actual turn therefore gives the normalized circle coefficient exactly. With the original marks and **full stationary equations**, the critical action gives the actual augmented-link volume. No uncomputed regulator constant remains at this local anchor.

The [complete local marked-density theorem](../../notes/actual_augmented_plat_local_marked_density.md) now proves more than nonzero separate factors. Each fully normalized circle has an $N^{-1}$ relative packet with nonzero amplitude, and the actual marked boundary contributes another $N^{-1}$. The original paired-circle normal is already included in this root compiler. Summing the local folded-channel window gives a nonzero Gaussian coefficient at both parities, using the actual discrete nodes, weights and signed half twists. A transverse magnetic Gaussian is also nonzero per unit framing volume. This is a complete-color local theorem; it does not integrate the framing orbit, prove a global source contribution, or supply a mixed-color filling packet.

The [source Ward calculation](../../notes/actual_augmented_plat_framing_density_source_ward.md) now determines that local framing density itself. Independent complex-head identities for the actual large polynomials, the original mark, and Gaussian transport with its full Jacobian give

$$\Omega_{\mathrm{src}}=c_D\frac{-dr\wedge ds}{s(1+s)},\qquad c_D\ne0.$$

The coefficient $c_D$ is independent of the framing point and retains the source's fixed phases and normalization. With $A_{\mathrm{cut}}=(1+s)^{-1}$ fixed, the residual differential is $c_D\,d(r/s)$, with the recorded orientation. It is exact on this affine chart. The required contribution therefore depends on the actual relative ends and excluded divisors; the local formula does not assign a nonzero value to their pairing.

The dense forbidden lattice zeros still rule out a uniform nowhere-zero single-term asymptotic on a neighborhood containing an open real forbidden region. The new packet is in a complex chart. At a fixed forbidden integer separation, the whole original physical slice is zero. Deforming only its magnetic variables cannot turn the local nonzero packet into a nonzero slice period.

## Exact transport retains the boundary terms

The [moving-period theorem](../../notes/actual_moving_period_factorial_normals.md) gives two exact shift equations for the original factorial function, including their scalar normalizations. The [source connection](../../notes/actual_tensor_source_finite_jet_connection.md) goes further: the actual white tensors and cups have an explicit rational gauge, assembled from $g(z)=e^{2\pi iz}/(1-e^{2\pi iz})$. After imposing the original integral head constraints, this conjugates their transport to commuting translations, with the original parity character retained. At any fixed quantum-jet order the normalized operators are unipotent. The gauge's integer divisors remain in the source; its algebraic trivialization does not determine a global integration cycle.

The [degree-cycle boundary theorem](../../notes/actual_matching_edge_degree_cycle_boundary.md) now permits a precise enlargement of the original finite-sum cycle. At a forbidden physical point both large white numerators vanish generically. Their product has enough vanishing to make the ordered cotangent residue zero, even though the continued integrand may have a pole. Such points can be added as zero periods whenever the surrounding factors are regular and the degree varies on the actual free lattice chart.

Moving this enlarged cycle requires the computed channel-pole residues and cotangent finite parts, with the actual lattice step and every other crossed divisor retained. An isolated late-wall first-normal residue, divided by the original trace normal, has coefficient $\pm N\sin(\pi/N)/\pi$ times the root density. Its magnitude tends to one. This is a nonzero local boundary coefficient; the complete cotangent correction also involves the derivative of the actual surrounding source.

The [adjoint period connection](../../notes/actual_tensor_source_translated_cycle_normals.md) carries the same transport through the original closed cotangent integral. It differentiates the retained measure as well as $G$, giving explicit double-pole corrections. A literal physical cup has a nonzero translated first-normal correction, so these identities do not make the finite physical sum periodic.

The [braided two-cut identity](../../notes/actual_braided_two_cut_source_adapter.md) now supplies an exact change of exposed cut at arbitrary width, including cuts at different Morse levels. If $z$ is the original marked scalar, $J^U$ is the two-cut array with its actual braid transport, and $g$ is the genuine generic pivotal vector, then

$$J^U\mathbf 1=z\mathbf 1,\qquad g^{\mathsf T}J^U=z g^{\mathsf T}.$$

Thus either cut gives a specified functional extracting the same whole scalar. The second functional retains its braid bands and pivotal weights; its clock is the transported first-head clock. The array still has an $(N-1)^2$-dimensional undetermined part. These identities therefore provide a source-preserving way to study the remaining framing direction, without asserting that both head indices can be fixed independently or that the geometric contribution survives.

The [actual residual current](../../notes/actual_braided_residual_framing_current.md) uses the two neighboring off-diagonal bands of that transported tensor. It gives an exact finite difference equation and integration by parts on every physical subinterval, retaining both ends and all genuine quantum derivatives. At completeness its Fourier current is supported on three neighboring nodes, with coefficient equal to the unknown whole scalar $z$. The conservation equation does not determine $z$.

The [common charged-current construction](../../notes/actual_matching_graph_common_band_ward_current.md) now gives the corresponding meromorphic equations before the finite sums. A spanning tree supplies one primitive lattice for the neighboring charged bands; cutting and reclosing its remaining edges constructs explicit difference currents from the actual tensor identities. Disconnected graphs require charge balance in every component. Each band keeps its own original support cycle, so the construction does not equate their periods or compute the pushforward to the geometric relative boundary.

## The original source at the resonant boundary

At the actual resonant cut, $r\sim N$ can send coupled magnetic indices to imaginary size $N\log N$. The [moving-factorial estimate](../../notes/actual_moving_period_factorial_logarithmic_escape.md) controls relative genuine quantum derivatives on these growing domains. It retains the factorials' absolute values and characters; it does not cross their zero or pole divisors.

For the original white polynomials, the [root boundary calculation](../../notes/actual_q_hahn_resonant_hard_edge.md) retains exact Newton endpoint normalizations and proves uniform Bessel packets when one clock grows like $N^2$ or the other shrinks like $N^{-2}$. In a marked puncture configuration the limiting factor is an $I_0$ function with a proved zero-free domain. When the two clocks escape in opposite directions, the result retains a whole polynomial and all forced partner zeros, with a relative estimate on its stated complex domain. For the actual right-angled cut, the original white-reflection prefixes force the limiting total onto the positive ray, so this domain contains the genuine mixed boundary configuration without a change of marking.

The [genuine quantum boundary packet](../../notes/actual_q_hahn_generic_resonant_hard_edge.md) keeps $t=N^2\epsilon$ before specialization. Its normalized limit is

$$\sum_{\ell\ge0}\frac{(-K)^\ell}{\ell!\,(1-t/(\pi i))_\ell}.$$

At $t=0$ this is the root Bessel series. Its parameter derivatives give the actual normalized quantum jets; differentiating a root-only formula would miss them. The exact original normalization, including its possible powers of $N$, stays in the result. These are boundary-factor theorems, not a whole-operator estimate or a proof that the geometric component contributes to the original cycle.

The [literal prefix-sign theorem](../../notes/actual_right_angled_resonant_prefix_signs.md) now fixes the boundary domains from the original outward face normals. All nonzero lower-left prefix entries have one common phase and positive coefficients. Consequently the finite clocks in the 022/220 regimes and both clocks in 222 are negative, while the 202 total is positive. These statements preserve the marked first cut and all retained half twists. When there is one main component, primitive meridian conjugacy also forces every original 200/002 box into the proved Bessel calibration, with both orientations included.

The [complemented-head identity](../../notes/actual_q_hahn_complementary_hard_edge.md) is exact before root specialization, so it transports genuine quantum derivatives to the small-second-clock regime. A separate positive-matrix comparison gives the outgoing 220 root packet through the fold. For two finite negative clocks, the [boundary determinant theorem](../../notes/actual_q_hahn_negative_clock_boundary.md) proves a leading logarithmic rate and uniform relative transport. Its first trace correction can be order one and is retained. The exact scalar and large-partner factors remain present; the new determinant result does not assert generic quantum-normal limits.

There is also a source-defined way to impose the boundary weights. The [finite-current theorem](../../notes/actual_braided_residual_framing_current.md) now uses **unwrapped integer charge conservation** to prove, for the literal rank-one insertion $X(p)_{rs}=p^{r-s}/N$,

$$\operatorname{Tr}[e_t\,\mathcal C(X(p))]=z\,b_N(t,p),\qquad
b_N(t,p)=\frac{1-p^N}{N(1-p)}(1-t+t/p)^{N-1}.$$

Here $z$ is the original root scalar. At $p=1-1/(N\rho+c_0)$ the explicit factor tends to $\rho(1-e^{-1/\rho})e^{t/\rho}$. Away from its known zeros, dividing this specified functional by $b_N$ extracts the same invariant at bounded cost. At the complete root, this normalized functional can also be absorbed into the existing coherent cut, with effective position $t_{\mathrm{eff}}=t/[p(1-t)+t]$. It therefore leaves the residual framing freedom in place. Its genuine quantum derivative has additional nonzero terms. The explicit boundary factor is a matching test; computing the internal geometric period and proving a nonzero contribution remain necessary.

## How far this is from the general conjecture

**The main gap remains a substantial global theorem.** There are two concrete tasks:

1. Compute the framing contribution and transport the original degree and magnetic cycles to the geometric chart with a nonzero controlled coefficient, using the exact boundary corrections. The nonzero local marked density and folded Gaussian do not establish survival of the whole coherent contribution.
2. Control the remaining physical regions and aliases uniformly in the auxiliary colors, and obtain the full source's complex color packet, so the general long-filling transfer applies.

The Fourier route is still useful. Its exact positive partition gives a weighted-Cauchy upper bound with all flow and charge constraints retained. Its radial optimizer cannot simply be declared geometric: the [radial-frame obstruction](../../notes/actual_positive_fourier_radial_geometric_obstruction.md) prevents assembling all strict ordinary radial saddles into the certified complete representation. No numerical rate gap follows from that obstruction.

Likewise, taking independent local projector maxima pays a genuine exponential boundary cost. The computed folded rate is $5v_3/\pi$ at both parities. The joint contraction must account for that cost rather than discard it as a normalization.

## Existing equality results and preserved alternatives

The [results chapter](results.md) states the internally reviewed equality theorems for the specified pretzel, belt-stack and signed robust Conway families. The latter permit arbitrary fixed branching and seed widths within their grammar, with independently sufficiently long fixed signed fillings. They do not exhaust arbitrary plats. The minimal isolated $C(h^3)$ mixed-color filling case and arbitrary short fillings remain outside the stated general filling theorem.

The [source-divisor transfer](../../notes/general_long_filling_source_divisor.md) can tolerate a leading density that vanishes at completeness if its analytic germ is nonzero. With the other hypotheses supplied, it gives equality outside an analytic exceptional divisor and density one of long slopes in signed boxes; a monomial times a unit gives all independently long slopes. This is still conditional for general plats.

The cube, Fourier, Karamata-inspired estimates, positive sewing and pointed torsor approaches remain in the [research library](../library.html). Their detailed arguments and failed intermediate estimates are preserved in the technical archive. This chapter records the current dependencies rather than requiring the reader to traverse every historical note.
