# The current general frontier

The target remains a volume theorem at **every fixed bridge width**, with independently long signed twists. The general filled-knot conjecture is open. There is now a complete-source equality for a broader intermediate class: augmented links with any fixed retained half-twist pattern whose actual diagram carries the labeled right-angled polyhedral certificate.

## The class and the order of quantifiers

Fix an essential $2k$-strand plat diagram $D$, $k\geq2$, with a hyperbolic augmented exterior $Y_D$ and its actual primitive cusp markings. The [general target](../../notes/general_augmented_plat_long_twist_target.md) asks for a threshold $T(D)$ such that

$$\min_i |m_i|>T(D)\quad\Longrightarrow\quad
\lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K_{D,\mathbf m})|
=\operatorname{Vol}(S^3\setminus K_{D,\mathbf m}).$$

The diagram and every signed full-twist number $m_i$ are fixed **before** the quantum level $N$ tends to infinity. The prescribed parity pattern must give a knot. The threshold may depend on the diagram; no threshold depending only on $k$ is asserted.

Under a positive marked gluing certificate, the [geometric filling theorem](../../notes/general_augmented_plat_long_filling_quantifiers.md) supplies a geometric threshold for independently long signed fillings. The quantum threshold in the displayed implication remains unproved for general plats.

## A whole-source equality at arbitrary fixed width

The [signed augmented-source theorem](../../notes/general_signed_augmented_source_volume.md) proves

$$\lim_{N\to\infty}\frac{2\pi}{N}\log|A_{D,N}|
=2\operatorname{Vol}(Q_D)=\operatorname{Vol}(Y_D).$$

Here $A_{D,N}$ is the original marked complete-circle source, with its actual normalization and retained exterior framing factor. The input is a connected original plat projection and a **labeled convex ideal right-angled polyhedron** realizing its actual cut and face pairings. Each retained half-twist exponent may independently be $0,+1,-1$. The width and matching graph are arbitrary and fixed; both level parities and composite levels are included.

This is a theorem about complete augmented **links**, including patterns whose main strands form one component. Filling their crossing circles still requires the external-color estimates below. The theorem does not assert that every reduced plat has the required geometric certificate. Parallel belts producing a white bigon fail this certificate; the [coverage check](../../notes/general_untwisted_augmented_source_literature_coverage.md) explains why their known even-level zeros are compatible with the theorem.

The proof is recorded and independently reviewed within this project. That is distinct from external peer review.

## The exact coefficient that makes the global proof possible

Let $R$ be the number of crossing circles, $d=N-1$, and $a_i$ the original internal channel labels. At each circle, the [literal source identity](../../notes/actual_complete_circle_positive_face_polynomial.md) gives two determinant polynomials and one forced-zero polynomial:

$$D_a(x,b,y)=\det\!\left[bI+\frac{x}{2}H_-+\frac{y}{2}H_+\right],\qquad
\widetilde P_s(x,y)=\sum_{j=0}^{s}\frac{S_s}{S_jS_{s-j}}x^{s-j}y^j,
\quad s=d-2a.$$

The matrices are the original positive Hermitian matrices, and $S_j=\prod_{r=1}^j2\sin(\pi r/N)$. These polynomials have nonnegative coefficients for **every** folded label. Their combined degree at a circle is $2a+s=d$.

The [exact marked coefficient theorem](../../notes/actual_original_marked_face_coefficient.md) then converts the actual finite head sum into one coefficient:

$$A_{D,N}=\chi_{D,N}N^R\sum_{\mathbf a}
\left(\prod_i k_{a_i}\beta_{a_i}^2\omega_{a_i}^{\epsilon_i}\right)
\left[\prod_{f\ne u,v}L_f^d\right]
\left.\prod_i D_{a_i,\mathrm{in}}D_{a_i,\mathrm{out}}
\widetilde P_{s_i}\right|_{L_u=L_v=0}.$$

Every scalar is specified by the original source. The mark removes exactly the two face exponents $u,v$. The other $R$ target exponents already use the entire degree $dR$, so there is no additional Fourier alias. Local polynomial zeros enforce the original unwrapped support; the primitive face grid supplies the exact power $N^R$. Even-level carries cancel only after the whole marked expression is assembled.

For $\epsilon_i=0$, this is a positive sum after removing the common unit phase $\chi_{D,N}$. With half twists, the same coefficients remain positive and their channel phases are summed explicitly by the signed theorem.

## Why the coefficient has the actual geometric rate

The proof uses one circle-packing radius for each shared white face. It does not independently maximize the tensor factors.

1. The [rank and curvature theorem](../../notes/actual_original_boundary_transverse_rank.md) leaves exactly two flat framing directions. Removing the two marked faces and fixing the common scale gives a positive Hessian of size $N$.
2. The [global coefficient theorem](../../notes/actual_positive_face_coefficient_saddle.md) bounds the entire coefficient torus. A finite positive-matrix contraction gives exponential decay away from its unique angular maximum, followed by a nonzero relative Gaussian asymptotic.
3. The [absolute action calculation](../../notes/actual_original_boundary_stationary_character.md) cones the marked ideal vertex to the actual white and shaded facets. Their Lobachevsky contributions give $2\operatorname{Vol}(Q_D)$, with the additive constant fixed by the original determinant normalization.
4. The [uniform channel-rate theorem](../../notes/actual_positive_face_channel_rate.md) controls every internal label at those same radii. Its circle rate increases strictly to the fold. This bounds the whole source from above; one positive folded coefficient supplies the matching lower bound in the untwisted case.
5. The [signed extension](../../notes/general_signed_augmented_source_volume.md) proves a uniform relative Gaussian estimate from the original finite continuants. It sums the actual half-twist phases and bounds all remaining labels. Its leading coefficient is nonzero at both level parities.

More precisely, put $M=\lfloor(N-1)/2\rfloor$, $s_0=N-1-2M$ and $t_i=M-a_i$. If $F_N(\mathbf a)$ denotes the positive sector coefficient including its $\beta$ factors, the actual shared-radius saddle gives

$$\frac{F_N(\mathbf M-\mathbf t)}{F_N(\mathbf M)}
=\exp\!\left[-\sum_i C_{i,N}\frac{t_i(t_i+s_0)}{N}\right](1+o(1)),\qquad C_{i,N}>0.$$

The exact phase ratio is $\omega_{M-t}/\omega_M=\exp[\pi i t(t+s_0)/N]$. Retaining the original multiplicities, the channel sum therefore contributes

$$ (\pi N)^{R/2}\prod_i(C_{i,N}-\pi i\epsilon_i)^{-1/2}(1+o(1)). $$

Here $C_{i,N}$ is evaluated at the exact finite critical radius and tends to a positive geometric value $C_i$. The factor cannot vanish. The estimate is relative throughout a window wider than $\sqrt N$, and the proof controls both its intermediate and macroscopic tails.

![The two constant-face directions and the neighboring original physical heads that give a primitive transverse slice.](../figures/face-potential-rank.png)

## How far this is from the requested knot theorem

The complete signed source now has a global equality. The remaining general problem is passage to independently long fillings:

| Required extension | What is available | What still needs proof |
| --- | --- | --- |
| Local deformed source | The whole original source has the geometric volume limit in a near-complete corridor at any set of untwisted ports; one varied signed port is covered by an explicit local curvature test | Interacting signed ports and their disconnected reflection subsets |
| Whole filling transform | Exact filling transform and geometric long-filling threshold | A bound for the entire complementary color region and its aliases, retaining all small-color terms |

Internal deficits $s_i=N-1-2a_i$ and external filling-color deficits $h_i=N-j_i$ are different variables. The [fixed complex core theorem](../../notes/actual_complete_core_complex_packet.md) now controls the complete-image term with $\boldsymbol\chi=\mathbf h/N$ in a fixed complex neighborhood:

$$\frac{F_N(N\boldsymbol\chi)}{F_N(0)}
=e^{N(S_N(\boldsymbol\chi)-S_N(0))}
\sqrt{\frac{\det K_N(0)}{\det K_N(\boldsymbol\chi)}}
\bigl(1+O(N^{-1})\bigr).$$

Here $S_N$ is the selected joint critical action and $K_N$ its nonsingular Hessian. The square root is fixed at $\boldsymbol\chi=0$. The theorem proves nonvanishing uniformly and $S_N\to S$ holomorphically. The [geometric deformation theorem](../../notes/actual_complete_core_geometric_deformation.md) identifies this limiting action on the actual marked peripheral branch:

$$2\pi\operatorname{Re}S(\boldsymbol\chi)
=\operatorname{Vol}(\rho_{\boldsymbol\chi})
+\frac12\sum_i\operatorname{Re}U_i\operatorname{Im}V_i,
\qquad U_i=-2\pi i\chi_i.$$

Thus for small **real** $\boldsymbol\chi$, the exact complete-core polynomial has rate $\operatorname{Vol}(\rho_{\boldsymbol\chi})$. At zero this is the complete augmented-link volume. For complex meridians the displayed boundary correction is necessary. The relative asymptotic still retains $S_N$; convergence alone does not justify substituting $S$ in its exponential. The [finite-level action transfer](../../notes/general_long_filling_varying_action_transfer.md) now proves that the filling calculation can retain $S_N$ throughout and take its limit at the end. Its remaining hypotheses are the full mixed-source estimates.

The [external reflection theorem](../../notes/actual_external_circle_reflection_and_cusp.md) gives an exact interface. An original color $N-h$ circle is a cosine-weighted complete circle plus a literal color $h$ circle. The complete term has a proved Fourier limit for $h=z\sqrt N$, and its coefficient matches the primitive cusp shape:

$$\frac{F_N(\sqrt N\,\mathbf z)}{A_{D,N}^{\boldsymbol\epsilon}}
=\exp\!\left[-\sum_i\frac{\pi^2z_i^2}{Z_i}\right](1+o(1)),
\qquad \tau_{\mathrm{geom},i}=\frac{2\pi i}{Z_i},\quad Z_i=C_i-\pi i\epsilon_i.$$

This holds uniformly for bounded complex $\mathbf z$, with fixed derivatives. It is a theorem about the specified complete term. The full mixed source also contains small-color terms, and the complete term has a full-size opposite-end alias. At that endpoint the small-color term cancels it exactly. A proof for the filling transform must retain this cancellation and control the entire combined source.

![Two actual cusp rectangles fix the primitive longitude factor of two and the normalization of the mesoscopic Fourier Gaussian.](../figures/cusp-gaussian.png)

The [source-divisor transfer](../../notes/general_long_filling_source_divisor.md) explains the final quantifier: a nonzero analytic amplitude germ gives a result outside an exceptional divisor, while all independently long slopes require the stronger unit or coordinate-monomial condition. The established complete core has a unit amplitude. To use it for the original filled invariant, the other terms and the color complement must still have a proved gap.

## The exceptional edge now has an exact algebraic description

The [finite Fourier-period theorem](../../notes/actual_positive_face_fixed_fold_packet.md) gives an exact four-component difference equation for the original complete-circle core. Its shift range is bounded independently of $N$. It retains the actual finite polynomial solution, both fold endpoints, the Fourier gauge and the full classical determinant factors. Its selected local characteristic is an explicit palindromic quartic. After the shared-face extraction, the equation couples neighboring face coefficients; a scalar equation for the whole knot has not yet been derived.

The [exponential interpolation theorem](../../notes/actual_positive_face_exponential_fold_interpolation.md) improves the original fixed-real estimate to an exponentially accurate comparison on the actual channel grid, uniformly for complex face radii. Analytic iterations on nested disks and contraction of the actual finite recurrence establish that comparison. The complete-core theorem then converts the finite channel grid by exact cotangent contours and evaluates the joint saddle. This closes the fixed-neighborhood analytic step for the complete term.

The [coupled polynomial system](../../notes/actual_whole_source_coupled_face_difference_system.md) retains every shared-face coefficient and the exact fold-selection relation. It matches the ordered classical momenta on regular charts. At a triangle with two marked zero faces the local quadratic has a double root. The [marked circle-pattern theorem](../../notes/actual_marked_deformed_circle_pattern.md) recovers the shared strip, all source-stationary face radii, and selected eigenline germs directly from a nonsingular finite geometric system. The [primitive collar calculation](../../notes/actual_deformed_circle_primitive_collar.md) then fixes the actual disk word, half-twist shear and line-face limit. Its single side pairing has multiplier $E_bE_c/D$; the double-reflection word has its square. Keeping that distinction and the actual eigenflag lets the global theorem verify every group relation and the regulator differential.

## What the remaining small-color terms now reduce to

The [exact small-circle operator](../../notes/actual_small_circle_polynomial_face_insertion.md) preserves the face polynomial ring after summing all original paths. Its apparent negative powers cancel because the physical endpoint coefficients vanish. The original total-degree argument then excludes every whole-level Fourier alias. At fixed positive radii, a color $h$ insertion costs at most $C^{h-1}$ in the weighted coefficient norm.

The [simultaneous correspondence](../../notes/actual_simultaneous_small_circle_face_correspondence.md) now covers **every untwisted subset with connected identity smoothing**, including protected outgoing faces and cyclic dependencies between operators. Its proof checks polynomiality separately in each merged-face component, while retaining all other formal path choices. It needs no global elimination order. The earlier [ordered construction](../../notes/actual_ordered_small_circle_face_insertions.md) remains a useful special case.

Disconnected identity smoothings have a different exact conclusion. If the inserted colors satisfy

$$2\sum_{i\in J}(h_i-1)<N-1,$$

their entire original subset contribution is **zero**. The ordinary face targets require more degree than the retained Laurent terms can supply. This includes the mesoscopic window at both level parities, with every remaining complete-circle phase retained. Deleted ports carrying a half twist are still outside these results.

For the required geometric gap, the [smoothing-capacity theorem](../../notes/actual_matching_smoothing_angle_capacity.md) supplies a sufficient angle-flow and entropy condition when an untwisted color-one circle is deleted. The polynomial operator carries any compatible strict gap to small colors, at the stated $C^{h-1}$ cost. It does not supply the gap itself.

The [fixed-radius criterion](../../notes/actual_smoothing_fixed_radius_gap.md) gives another sufficient bound without requiring a regular smoothed minimizer. Its explicit certified matched-graph family shows that the corresponding capacity test can fail when only the merged face varies. A source-coverage correction distinguishes that functional example from an original flat-plat source counterexample: the latter would need a presentation adapter that has not been proved. The graph geometry and capacity calculation remain valid.

The [capacity decomposition](../../notes/actual_smoothed_source_capacity_blocks.md) now handles those boundary limits. Compact angle duality remains exact even when the positive-radius infimum is not attained. Loops give an infeasible angle problem; separating two-edge cycles split the capacity into an additive sum. Each nontrivial simple block has a constructed circle packing and an actual convex ideal right-angled polyhedron, with

$$\Phi_{\mathrm{smoothed}}=\sum_B\frac{\operatorname{Vol}(Q_B)}{\pi}.$$

Double-triangle blocks contribute zero. The formula is independent of each block's adjacent marked pair; it does not move the quantum mark or factor the finite quantum source.

The [strict representation-volume theorem](../../notes/general_representation_volume_kernel_strictness.md) supplies the strict comparison when the smoothed source is itself certified hyperbolic. Its actual filling quotient kills an essential meridian. An independently checked natural-map argument proves that a representation with such a kernel has strictly smaller absolute volume. Thus the connected regular smoothing has a strict capacity gap, and the simultaneous operator estimate transfers it to small colors. A simple smoothed white triangulation supplies its required polyhedron by the block construction.

The [actual block representation](../../notes/actual_smoothed_block_representation_volume.md) now closes the nonzero degenerate-block case. It retains the original cuts and face pairings, including matching cuts whose shaded pairings run between blocks. Compatible finite horospherical corners and a uniform short-edge tetrahedron bound identify the regulator with the sum of block volumes. The representation kills the deleted meridians, so the strict-volume theorem applies. No geometric decomposition of the whole smoothed exterior or finite quantum factorization is assumed.

Combining that strict gap with the exact subset identities proves a **general untwisted color corridor**. For any fixed set $E$ of untwisted varied ports, the other ports staying complete with their original signs, there are $\delta(D),\gamma(D)>0$ such that

$$\left|A_N(N-\mathbf h_E,N_{\mathrm{else}})-F_N^E(\mathbf h)\right|
\leq N^{K(D)}e^{N(\operatorname{Vol}(Y_D)/(2\pi)-\gamma(D))},
\qquad 0\leq h_i\leq\delta(D)N.$$

The [whole-source corollary](../../notes/general_untwisted_mixed_source_volume_corridor.md) combines this gap with the zero-free core. After shrinking the corridor, their ratio is $1+O(e^{-cN})$. Consequently, for any physical integer sequence $\mathbf h_N/N\to\boldsymbol\chi$ in that corridor,

$$\lim_{N\to\infty}\frac{2\pi}{N}\log\left|A_N(N-\mathbf h_{N,E},N_{\mathrm{else}})\right|=\operatorname{Vol}(\rho_{\boldsymbol\chi}).$$

This is a limit for the **whole original mixed source**, with the actual marked geometric representation on the right. It holds at arbitrary fixed width and both level parities. A complete metric on a filled knot is a further assertion, and the full filling transform still needs its complementary-color estimates.

For a signed varied port, the [exact crossing kernel](../../notes/actual_signed_small_circle_face_kernel.md) preserves the original confluent Casimir data. Its weighted coefficient norm can grow exponentially even at color one. The same calculation nevertheless gives a sufficient one-port criterion at the original packing:

$$g_i=F(x_i,b_i,y_i)+F(x_i,c_i,y_i)-G(b_i,x_i,y_i,c_i)>0.$$

Here $F$ is the original triangle potential and $G$ is the explicit four-variable entropy maximum in that note. The criterion assumes connected identity smoothing and four positive, suitably unmarked face curvatures. It gives a signed one-port corridor with every other port complete and its sign retained. A curvature ratio below $2.807257219\ldots$ is one sufficient local test. This is an inequality on the local curvature data; it is not a claim that every such quadruple occurs in a rigid labeled packing. Interacting signed ports require a separate simultaneous estimate.

![A schematic slice of external colors: the untwisted corridor, the sufficient signed one-port estimate, and the remaining full color complement.](../figures/external-color-corridor.png)

The [positive Newton calculation](../../notes/actual_positive_newton_capacity_obstruction.md) explains why the far-color problem cannot be reduced to a presumed universal entropy comparison on all certified matched graphs. Its exact local kernel has nonnegative coefficients, but an explicit shared-face feasible state gives a capacity above the geometric complete value. The coefficient lower bound retains the true Newton weights. The graph family has not yet been adapted to the original flat-plat compiler, so this remains a polynomial-capacity obstruction, not a claimed flat-plat source counterexample. In the actual alternating expansion the omitted sign changes a critical equation. A proof using that expansion must retain the sign.

The remaining general source problems are interacting signed near-complete terms and the entire complementary color region, including their combined opposite-end aliases.

The [near-maximal-volume theorem](../../notes/general_representation_volume_peripheral_gap.md) gives a general geometric criterion for the latter problem. For a fixed finite list of marked peripheral words, keeping any $|\operatorname{tr}^2\rho(\mu_i)-4|$ bounded away from zero forces a uniform positive volume gap. Its proof derives convergence to the marked complete representation from near-maximal volume. Using this criterion for the quantum source still requires a bound on the actual full period; a characteristic equation or the complete-image term alone does not provide that bound.

The previous operator and torsor approaches remain available. The exceptional operator is the original normalized Casimir polynomial, with its [general character relation](../../notes/actual_matching_edge_polynomial_geometric_action.md) and [exact resolvent period](../../notes/actual_matching_edge_continuant_operator_period.md). The original marked transport, genuine quantum normals, odd framing source, logarithmic class and relative boundary currents are preserved in the [source and torsor routes](../library.html). The new coefficient identity and signed Gaussian resolve the complete contraction without assigning an arbitrary relative cycle.

The global knot quantum A-operator and its selected period have not been derived from this identity. The coefficients and source relations provide a concrete finite object for that work; they are not being renamed the knot A-polynomial.

## Existing knot results and preserved alternatives

The [results chapter](results.md) retains the internally reviewed pretzel, belt-stack and signed Conway filling theorems with their original hypotheses. They do not exhaust arbitrary plats. The cube, Fourier, weighted-Cauchy, Karamata-inspired and torsor arguments remain in the [research library](../library.html), including failed intermediate estimates and their corrections. The current route adds a general exact coefficient and a whole-source augmented-link result without discarding those ideas.
