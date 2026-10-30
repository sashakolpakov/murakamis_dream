# The current general frontier

The target remains a volume theorem at **every fixed bridge width**, with independently long signed twists. The general filled-knot conjecture is open. There is now a complete-source equality for a broader intermediate class: untwisted augmented links whose actual diagram carries the labeled right-angled polyhedral certificate.

## The class and the order of quantifiers

Fix an essential $2k$-strand plat diagram $D$, $k\geq2$, with a hyperbolic augmented exterior $Y_D$ and its actual primitive cusp markings. The [general target](../../notes/general_augmented_plat_long_twist_target.md) asks for a threshold $T(D)$ such that

$$\min_i |m_i|>T(D)\quad\Longrightarrow\quad
\lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K_{D,\mathbf m})|
=\operatorname{Vol}(S^3\setminus K_{D,\mathbf m}).$$

The diagram and every signed full-twist number $m_i$ are fixed **before** the quantum level $N$ tends to infinity. The prescribed parity pattern must give a knot. The threshold may depend on the diagram; no threshold depending only on $k$ is asserted.

Under a positive marked gluing certificate, the [geometric filling theorem](../../notes/general_augmented_plat_long_filling_quantifiers.md) supplies a geometric threshold for independently long signed fillings. The quantum threshold in the displayed implication remains unproved for general plats.

## A whole-source equality at arbitrary fixed width

The [untwisted augmented-source theorem](../../notes/general_untwisted_augmented_source_volume.md) proves

$$\lim_{N\to\infty}\frac{2\pi}{N}\log|A_{D,N}|
=2\operatorname{Vol}(Q_D)=\operatorname{Vol}(Y_D).$$

Here $A_{D,N}$ is the original marked complete-circle source, with its actual normalization and retained exterior framing factor. The input is a connected original plat projection and a **labeled convex ideal right-angled polyhedron** realizing its actual cut and face pairings. Every retained half-twist exponent is zero. The width and matching graph are arbitrary and fixed; both level parities and composite levels are included.

This is a theorem about complete augmented **links**. In the standard adjacent-cap plat, removing every half twist leaves several main components, which full twists do not join. The result therefore does not supply the requested knot family merely by declaring its filling slopes long. It also does not assert that every reduced plat has the required geometric certificate. Parallel belts producing a white bigon fail this certificate; the [coverage check](../../notes/general_untwisted_augmented_source_literature_coverage.md) explains why their known even-level zeros are compatible with the theorem.

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

For $\epsilon_i=0$, this is a positive sum after removing the common unit phase $\chi_{D,N}$. With half twists, the same coefficients remain positive but their channel phases remain present.

## Why the coefficient has the actual geometric rate

The proof uses one circle-packing radius for each shared white face. It does not independently maximize the tensor factors.

1. The [rank and curvature theorem](../../notes/actual_original_boundary_transverse_rank.md) leaves exactly two flat framing directions. Removing the two marked faces and fixing the common scale gives a positive Hessian of size $N$.
2. The [global coefficient theorem](../../notes/actual_positive_face_coefficient_saddle.md) bounds the entire coefficient torus. A finite positive-matrix contraction gives exponential decay away from its unique angular maximum, followed by a nonzero relative Gaussian asymptotic.
3. The [absolute action calculation](../../notes/actual_original_boundary_stationary_character.md) cones the marked ideal vertex to the actual white and shaded facets. Their Lobachevsky contributions give $2\operatorname{Vol}(Q_D)$, with the additive constant fixed by the original determinant normalization.
4. The [uniform channel-rate theorem](../../notes/actual_positive_face_channel_rate.md) controls every internal label at those same radii. Its circle rate increases strictly to the fold. This bounds the whole source from above; one positive folded coefficient supplies the matching lower bound in the untwisted case.

![The two constant-face directions and the neighboring original physical heads that give a primitive transverse slice.](../figures/face-potential-rank.png)

## How far this is from the requested knot theorem

The complete untwisted source now has a global equality. Two substantial extensions remain for general long-filled knots:

| Required extension | What is available | What still needs proof |
| --- | --- | --- |
| Retained signed half twists | The exact positive coefficients and explicit channel phases; the same sharp global upper bound | Uniform relative estimates in the folded channel window and a nonzero coefficient after summing its phases |
| Independently long fillings | The exact filling transform, primitive peripheral marks and geometric long-filling threshold | A complex packet in the **external** crossing-circle colors and a bound for the whole complementary region and its aliases |

Internal deficits $s_i=N-1-2a_i$ and external filling-color deficits $h_i=N-j_i$ are different variables. The new internal-channel theorem does not provide the missing external-color estimate. Likewise, a leading logarithmic rate does not justify a relative Gaussian estimate in a window of width $\sqrt N$.

The [source-divisor transfer](../../notes/general_long_filling_source_divisor.md) explains the final quantifier: a nonzero analytic amplitude germ gives a result outside an exceptional divisor, while all independently long slopes require the stronger unit or coordinate-monomial condition. Those hypotheses still need to be verified for the general source.

## The exceptional edge now has an exact algebraic description

The previous operator and torsor approaches remain available. The exceptional operator is the original normalized Casimir polynomial, with its [general character relation](../../notes/actual_matching_edge_polynomial_geometric_action.md) and [exact resolvent period](../../notes/actual_matching_edge_continuant_operator_period.md). The original marked transport, genuine quantum normals, odd framing source, logarithmic class and relative boundary currents are preserved in the [source and torsor routes](../library.html). The new coefficient identity resolves the complete untwisted contraction without assigning an arbitrary relative cycle.

The global knot quantum A-operator and its selected period have not been derived from this identity. The coefficients and source relations provide a concrete finite object for that work; they are not being renamed the knot A-polynomial.

## Existing knot results and preserved alternatives

The [results chapter](results.md) retains the internally reviewed pretzel, belt-stack and signed Conway filling theorems with their original hypotheses. They do not exhaust arbitrary plats. The cube, Fourier, weighted-Cauchy, Karamata-inspired and torsor arguments remain in the [research library](../library.html), including failed intermediate estimates and their corrections. The current route adds a general exact coefficient and a whole-source augmented-link result without discarding those ideas.
