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
| Local deformed source | Exact all-color formulas, the complete signed source and primitive peripheral marks | A uniform complex packet in the **external** crossing-circle colors, with its actual marked geometric action |
| Whole filling transform | Exact filling transform and geometric long-filling threshold | A bound for the entire complementary color region and its aliases, retaining all small-color terms |

Internal deficits $s_i=N-1-2a_i$ and external filling-color deficits $h_i=N-j_i$ are different variables. The new internal-channel theorem does not provide the missing external-color estimate. Fixed nonzero external parameters require control beyond the internal $\sqrt N$ window.

The [external reflection theorem](../../notes/actual_external_circle_reflection_and_cusp.md) gives an exact interface. An original color $N-h$ circle is a cosine-weighted complete circle plus a literal color $h$ circle. The complete term has a proved Fourier limit for $h=z\sqrt N$, and its coefficient matches the primitive cusp shape:

$$\frac{F_N(\sqrt N\,\mathbf z)}{A_{D,N}^{\boldsymbol\epsilon}}
=\exp\!\left[-\sum_i\frac{\pi^2z_i^2}{Z_i}\right](1+o(1)),
\qquad \tau_{\mathrm{geom},i}=\frac{2\pi i}{Z_i},\quad Z_i=C_i-\pi i\epsilon_i.$$

This holds uniformly for bounded complex $\mathbf z$, with fixed derivatives. It is a theorem about the specified complete term. The full mixed source also contains small-color terms, and the complete term has a full-size opposite-end alias. At that endpoint the small-color term cancels it exactly. A proof for the filling transform must retain this cancellation and control the entire combined source.

![Two actual cusp rectangles fix the primitive longitude factor of two and the normalization of the mesoscopic Fourier Gaussian.](../figures/cusp-gaussian.png)

The [source-divisor transfer](../../notes/general_long_filling_source_divisor.md) explains the final quantifier: a nonzero analytic amplitude germ gives a result outside an exceptional divisor, while all independently long slopes require the stronger unit or coordinate-monomial condition. Those hypotheses still need to be verified for the general source.

## The exceptional edge now has an exact algebraic description

The [finite Fourier-period theorem](../../notes/actual_positive_face_fixed_fold_packet.md) gives an exact four-component difference equation for the original complete-circle core. Its shift range is bounded independently of $N$. It retains the actual finite polynomial solution, both fold endpoints, the Fourier gauge and the full classical determinant factors. Its selected local characteristic is an explicit palindromic quartic. After the shared-face extraction, the equation couples neighboring face coefficients; a scalar equation for the whole knot has not yet been derived.

The same theorem improves the relative internal-channel estimate to $O(N^{-1})$ on a fixed **real** interval, with an even analytic action and an explicit amplitude. This error is not exponentially small and therefore does not justify replacing the exact source in a Fourier transform at frequencies of order $N$. The exact difference equation provides an additional way to study that remaining problem.

The previous operator and torsor approaches remain available. The exceptional operator is the original normalized Casimir polynomial, with its [general character relation](../../notes/actual_matching_edge_polynomial_geometric_action.md) and [exact resolvent period](../../notes/actual_matching_edge_continuant_operator_period.md). The original marked transport, genuine quantum normals, odd framing source, logarithmic class and relative boundary currents are preserved in the [source and torsor routes](../library.html). The new coefficient identity and signed Gaussian resolve the complete contraction without assigning an arbitrary relative cycle.

The global knot quantum A-operator and its selected period have not been derived from this identity. The coefficients and source relations provide a concrete finite object for that work; they are not being renamed the knot A-polynomial.

## Existing knot results and preserved alternatives

The [results chapter](results.md) retains the internally reviewed pretzel, belt-stack and signed Conway filling theorems with their original hypotheses. They do not exhaust arbitrary plats. The cube, Fourier, weighted-Cauchy, Karamata-inspired and torsor arguments remain in the [research library](../library.html), including failed intermediate estimates and their corrections. The current route adds a general exact coefficient and a whole-source augmented-link result without discarding those ideas.
