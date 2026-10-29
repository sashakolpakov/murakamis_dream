# The special inner product: what Cauchy proves and what must be constructed

**Whole-support update, 29 October.** The
[actual correlated boundary Gram](actual_whole_support_boundary_gram_envelope.md)
now has polynomial source cost on EVERY supported folded triple,
including saturation boundaries, at both level parities. The
[current generalization strategy](pretzel_to_general_source_strategy.md)
keeps the proved pretzel argument as the main route. Genuine changes
of pairing and the sharp global energy/overlap still need control.
The filled pretzel threshold is now odd s>=9 by the
[whole-color improvement](actual_pretzel_all_width_extension.md);
older threshold and status paragraphs below are historical.

**Full long-pretzel equality, 29 October.** The
[geometric completion theorem](actual_long_pretzel_geometric_filling_completion.md)
and [Casson--Rivin proof](actual_long_pretzel_casson_rivin_equality.md)
now identify the selected full-source rate with the actual filled
hyperbolic volume for fixed odd widths s>=25 and independently
sufficiently long fixed signed twists. The equality uses the separately
proved quantum survival and smooth geometric completion; it is not
inferred from Cauchy's upper inequality. Earlier status paragraphs
below retain their historical scope.

**Current result, 29 October.** The requested inequality is weighted
Cauchy--Schwarz. With the unchanged scalar K=bv and a specified positive
Hermitian G, it is exactly |K|^2<=(b G^(-1)b^*)(v^*Gv). A subexponential
dual norm and an independent geometric estimate of the energy are the
two required bounds. The complete augmented-source Fourier metric below
has both, including all marked normal derivatives. Its lower overlap
estimate is an additional survival theorem, not a consequence of Cauchy.

The [full long-pretzel upper theorem](actual_long_pretzel_sharp_volume_upper_bound.md)
also now bounds the original invariant by the actual filled hyperbolic
volume for fixed odd widths s>=25 and independently sufficiently long
fixed signed twists. It uses the whole-source asymptotic and the actual
representation regulator, not a newly assumed metric-energy estimate
for arbitrary filled sources. Full volume equality and a general-knot
sharp metric theorem remain unproved. Older status paragraphs follow.

**Whole-source update, 29 October.** The
[full original long-pretzel source](actual_long_pretzel_full_source_survival.md)
now has a nonzero asymptotic for fixed odd s>=25 and independently
sufficiently large fixed signed twists. Its proof bounds the entire
color complement and all filling Fourier currents, then evaluates the
surviving coherent charges. Its selected source rate still requires
comparison with the filled hyperbolic volume. Thus the analytic
whole-source survival problem is closed for this class, while the
geometric rate identification remains open; Cauchy alone supplies
neither assertion.

**Complete augmented-base result, 29 October.** For every fixed odd
pretzel width s>=3 the question now has a sharp constructive answer.
Write the original coherent Laurent polynomial z_N(w+w^(-1))^s
as sum a_k w^k, and use G_(kk)=R^(2(k-N)) at the geometric radius
R=exp(2asinh(tan(pi/s))). Its positive energy is the exact finite
Fourier norm Z=sum |a_k|^2R^(2(k-N)). The original marked functional
has squared dual norm at most C_s N^4. Crucially, the
[full-period proof](actual_pretzel_coherent_circle_and_period_asymptotic.md#8-the-requested-special-inner-product-is-an-explicit-fourier-norm)
now independently establishes log Z=N V_s/pi-(1/2)log N+O(1).
The subsequent Gaussian calculation proves original-period survival
as well. The normalized squared Riesz overlap is explicitly asymptotic
to a nonzero constant times N^(-1/2), so the Cauchy estimate loses only
a polynomial factor here; see equations (23)--(24) of that proof.
This is the complete augmented link base with s+1 components;
it does not give the required metric bound for its fixed filled knots.
The arbitrary-source estimates and obstructions below retain that
broader unresolved scope.

**Mixed-source progress, 29 October.** The independently reviewed
[mixed-cusp period proof](actual_pretzel_mixed_cusp_period_survival.md)
now gives a nonzero uniform leading term on a fixed small real-color
corridor for every fixed odd s>=5. Its discrete analytic summation
uses an exact half-grid cotangent contour with all endpoint currents
bounded. The [global low-core bound](actual_pretzel_global_core_spectral_gap.md)
also gives a strict macroscopic-color gap, including repeated roots.
Neither statement controls every macroscopic RP band of the complete
filled source. The [exact filling chirp](actual_coherent_filling_gaussian_chirp.md)
retains those colors and the Fresnel endpoint terms; estimating their
whole coherent contribution remains necessary for fixed filled knots.

**Latest concrete metric, 29 October.** The ORIGINAL complete crossing
circle now supplies a positive semidefinite form on the entire physical
pair: [C=PL_N and H=L_NP](actual_complete_circle_reflection_positive.md).
The ordinary cap has exact squared dual norm 1/(2N^3) in C; the
degree-restricted original marked cap has 1/(2N^5) in H. The
[whole-source degree argument](actual_reflection_marked_boundary_metric.md)
justifies that restriction and gives, at every fixed k-cup width,

    |K_N|^2 <= |chi_N|^2 2^(-k)N^(-(3k+2)) v_N^*G_top v_N,
    G_top=C^(tensor(k-1)) tensor H,  v_N=W p^(tensor k).

This is a proved special-inner-product Cauchy inequality for the actual
source, with every framing/peripheral factor retained. The cap kills
the metric's radical, so the inverse is the Moore--Penrose inverse on
its positive quotient. The unrestricted marked row cannot be substituted
locally. Same-pair twists preserve C; overlapping crossings need not.

For the arbitrary odd-pretzel augmented port graph there is also an
[exact coherent factorization](actual_pretzel_circle_coherent_reflection.md)
into TWO positive source packets, with their retained half twists
unitary between them. Neither result currently bounds its energy by
the geometric Rivin partition. The boundary Cauchy step is complete;
the sharp whole-source energy comparison and a survival/lower bound
remain unproved.

**Direct answer to the Cauchy question.** Yes. For the ORIGINAL row b
and state v, any positive Hermitian G gives

    |bv|^2 <= (b G^(-1) b^*) (v^* G v).

The explicit complete-source metrics below already make the first
factor polynomial. The remaining estimate is an INDEPENDENT bound
of the second factor by the geometric angle partition, including the
original external factors. Calling that second factor Z does not
establish the geometric comparison.

Even a metric specified without knowing the numerical period can
merely repackage it. Indeed G=b^*b+epsilon I gives exactly

    b G^(-1)b^*=||b||^2/(||b||^2+epsilon)<=1,
    v^*Gv=|bv|^2+epsilon ||v||^2.

Thus explicitness and a cheap boundary alone are insufficient. The
useful content must be an independent geometric energy estimate.

The [complete Fourier--Hermite filling metric](actual_filling_fourier_hermite_gram.md)
gives another exact Cauchy realization with ALL normal jets retained:
its dual cost for a full twist 2p is
1+p^2(N^2-1)/(3N^2), independent of N up to the displayed correction.
The same proof gives an actual hyperbolic-knot normalization insertion
on which its energy is excessive. Polynomial dual cost, full rank,
and coherent off-diagonal terms alone therefore do not establish
the sharp geometric comparison; the cancellations required by the
whole source must be reflected in the energy estimate.

**Uniform-gluing test resolved.** The
[actual all-input normalization operator](actual_all_input_normalization_clock_obstruction.md)
has exponentially large first normal jets and exponentially large
norm on every disk whose radius is exp(-o(N)). This is proved using
the [all-parity endpoint Gaussian asymptotic](actual_normalization_endpoint_gaussian_asymptotic.md),
not a numerical trend. The selected scalar disk theorem below remains
valid, but cannot be promoted to a uniform physical-head bound.

**Source-specific energy theorem, 29 October.** The
[actual cup slide](actual_terminal_source_normalization_packet.md)
proves that the fixed terminal-Gram obstruction occurs on a genuine
fixed braid prefix of p, not merely on an arbitrary input. Its closed
scalar is a unit while its recorded full-circle energy is exponential.
The [backward clock Ward estimate](actual_normalization_clock_disk_bound.md)
now repairs this normalization packet: its whole 1/N complex disk
and every fixed normal jet have polynomial bounds, and every shrinking
arc has the sharp zero exponential rate. The cancellation is proved
before taking a norm. Its sampled excess energy instead concentrates
exponentially near clock phase exp(pi*i/3).

The estimate allows [sublinear-band diagonal spectator currents](actual_mesoscopic_clock_packet_currents.md).
It does not cover all physical open-head colors or general crossings,
whose observable degree already equals N-1. The
[actual adjacent-observable filtration](actual_adjacent_observable_source_filtration.md)
makes this distinction exact. A separate
[normalization-current theorem](actual_normalization_boundary_current_quotient.md)
removes zero-pointing boundary currents with operator spectators and
controls their radial normal germs through radius one. The broad
hyperbolic source-energy comparison is still unproved.

**Current quantitative checkpoint, 29 October.** The Cauchy step has
explicit complete-module metrics with polynomial dual cost. A new
[shrinking-arc metric](actual_shrinking_arc_cauchy_metric.md) even has
exact evaluation norm at most N, independent of arc width. Thus the
full Fourier circle is optional. Bounding the energy of these metrics
by the knot's volume remains the substantive missing estimate.

For the existing terminal packet, the
[source-conditioned Green estimate](actual_terminal_green_capacity_bound.md)
now proves |P_t|<=N+4|F_t|^2 at every color. Its coherent composition
with a neighboring bridge has a
[sharp all-input capacity](actual_composed_bridge_capacity.md)
C_*=6.93088659313158<2v_8, with full-source consequences at arbitrary
plat width. This improves a broad bound; C_* is not a knot volume.
The [exact Lyapunov test](actual_terminal_gram_lyapunov_obstruction.md)
also proves that this fixed terminal Gram cannot propagate through
every original crossing at subexponential cost. A source-specific
bound or controlled exponential change of metric is necessary.

The [complete phase kernel](actual_terminal_effective_cartan_kernel_and_graph.md)
retains a second orbital channel. Neither fixed-phase transparency
nor harmlessness on shrinking arcs follows merely from the bounded
classical character. Source normal equations and calibrated actions
remain part of the energy problem.

**Latest test, 29 October.** The fixed complete Casimir/Hermite metric
below is now [proved nonsharp](actual_figure_eight_complete_channel_energy.md)
on the literal original figure-eight. One exact odd-level channel forces
its energy to have lower rate v_8/pi, above Vol(4_1)/pi. Polynomial
boundary costs do not fix that excess. A
[terminal coherent packet Gram](actual_terminal_packet_positive_gram.md)
now gives a constructive sharp metric for the same complete-module
benchmark, using an actual linear map determined by the final cap and
two crossings. Its dual cost is <=N, and its sharp energy follows from
the original row-by-row finite identity. The Cauchy construction extends
to all plat widths; the sharp energy estimate for general prefixes
remains unproved.

The [full terminal matrix](actual_terminal_packet_closed_kernel.md)
is now known on every input column. Its scalar register satisfies
`P_t=(1-Q^t)^2 P_(t-1)+Q^t`; its three-port tensor has squared
norm exactly `N w_d`. The
[open signed bridge reduction](actual_terminal_bridge_operator_reduction.md)
also has an exact coherent composition with this T, contractive
through-head currents, and a uniform octahedral row-energy profile.
The register, exterior metric factors and shared physical degrees
cannot be removed from that composition.

The [phase audit](actual_terminal_phase_coupon_and_ward.md) locates a
specific additional gate: Parseval's recorded color introduces an
effective Cartan coupon M_t with explicit Ward sources. It is not
the existing meridian parameter. The original cap certificate does
not automatically give a knot representation for every critical
contribution of that modified positive energy. Its additional coupling
must be estimated or shown transparent by the complete stationary
equations, rather than assumed harmless.

29 October 2026. The proposed comparison is precisely weighted
Cauchy--Schwarz. Its substantive input is a positive metric on the
ORIGINAL state, with controlled dual source and geometric energy.

Write the unchanged invariant as `K_N=a_N^*v_N`, including its actual
peripheral and normalization factors in this pairing. For any positive
Hermitian matrix G_N,

    |K_N|^2 <= (a_N^*G_N^(-1)a_N)(v_N^*G_Nv_N).       (1)

Indeed `a_N^*v_N=(G_N^(-1/2)a_N)^*(G_N^(1/2)v_N)`.
Thus the requested bound follows from

    a_N^*G_N^(-1)a_N <= exp(o(N)),
    v_N^*G_Nv_N <= exp(o(N)) Z_N.                    (2)

The positive angle partition already has the independently proved
[geometric estimate](positive_angle_supporting_plane_and_defect_bound.md)
`log Z_N=N Vol(M)/pi+O(log N)` for a fixed complete positive ideal
triangulation with the specified bounded true edge defects. Equation
(2) would therefore prove the sharp UPPER bound for the original
invariant. A matching lower bound requires geometric survival as well.

Rescaling G_N by a positive scalar scales the two factors of (1)
reciprocally. It cannot improve their product. Likewise defining a
metric using the unknown complete contracted period does not establish
(2). A useful metric must come from explicit packet, source and
geometric data whose estimates can be checked independently.

## An explicit metric already works on the original figure-eight packet

Put `Q=exp(2pi i/N)`, `F_n=(Q;Q)_n`, and let

    P_(n,k)=[n choose k]_Q, k<=n; otherwise 0,
    H=diag(|F_n|^2), G=P^*HP,
    v_k=(-1)^k Q^(k(k+1)/2), a=P^*F.

The [literal original-source calculation](actual_pascal_coherent_gram.md)
proves `Pv=F` and `K_(4_1),N=a^*v`, with the original turns and
Cartan factors retained. P is invertible and G is positive definite;
its entries depend only on the explicit quantum-factorial packet.
Consequently

    a^*G^(-1)a=N,
    v^*Gv=sum_(n=0)^(N-1)|F_n|^4,
    |K_(4_1),N|^2 <= N sum_n |F_n|^4.               (3)

The last positive sum has logarithm `N Vol(4_1)/pi+O(log N)`.
This is the requested Cauchy mechanism in a specified non-diagonal
inner product. The positive formula for this particular original
period also proves its lower bound. Neither fact alone generalizes
the volume conjecture to other knots.

## What now extends beyond that example

The [complete original multiplicity reduction](actual_complete_source_multiplicity_module.md)
now preserves EVERY signed braid generator on an entire even-plat
invariant space. For a fixed 2k-head plat it gives exactly
`K_N=chi_N lambda B_word w_0`, with

    ||w_0||=N^[3(k-1)/2], ||lambda||=N^[-(k-1)/2].

Thus ordinary Cauchy already gives
`|K_N|^2<=|chi_N|^2 N^[-(k-1)] ||B_word w_0||^2` in that
specified full multiplicity space. The original external factor chi_N
is retained, not assumed small. The representation is complete, so
there is no unresolved preservation assumption for a compressed cap
channel. What remains is the sharp estimate of the coherent norm,
potentially in a different positive metric. The
[full Casimir/Hermite packet](actual_complete_casimir_hermite_packet.md)
supplies all frame and inverse coefficients, including their derivative
normalizers, for constructing and checking such a metric.

For the complete four-strand plat representation, this now gives an
explicit additional positive metric. Let J be the full anti-Pascal
recoupling, V the complete degree-(N-1) Casimir/Hermite frame, and set

    S=V^(-1)J, G=(1/N)S^*S.

Both matrices are invertible and are fixed before the braid is chosen.
The exact original source calculation in Section 4a of the multiplicity
note gives, with n_distinct=ceil(N/2),

    ||ell||_(G^(-1))^2=n_distinct/N<=1,
    ||p||_G^2<=8N^2.

Here the first expression means the dual norm of the row ell. All
Casimir derivative directions and the original full marked closure
are included through the complete invariant-tensor reduction. Thus
for v=chi_N B_word p we have EXACTLY

    |K_N|^2<=||v||_G^2.

This constructs a special inner product and controls its original
dual source on the complete module. However the desired estimate
`||v||_G^2<=exp(o(N)) Z_N` for THIS metric is now disproved even for
the figure-eight, by the exact channel witness linked above. A different
coherent metric is necessary; the terminal packet construction supplies
one with the sharp benchmark rate on this same full module. No smallness
of chi_N or of the whole recoupling matrix is assumed. The all-width
reduction remains available, with general terminal energy still open.

The next source calculation performs an entire contraction coherently.
The [original pivotal cap](actual_pivotal_cap_reassociation_angle_packet.md)
on the actual reassociation `(C'_23)^(-1)C'_12` supplies the finite sum
`sum_r Q^r [b+r choose r]_Q=[N choose b+1]_Q`. It annihilates every
middle input except b=N-1. In the source-fixing quarter metric the
remaining squared coefficient is exactly
`w_N(a,c,N-1-a-c)`, with its full phase retained. The inverse cup
identity is also exact. The unrestricted marked row has its separately
recorded current packet and is not replaced by this ordinary cap.

[Arbitrary binary trees of these original cap packets](actual_cap_tree_angle_energy.md)
now have a complete quantitative contraction theorem. With l active
leaves of degrees a_i and root n=sum a_i, their squared kernel is
`N^(2-l)/[s_(N-1-n) product_i s_(a_i)]`. Their row Gram is exactly
diagonal, with explicitly known entries E_(l,n), and

    log E_(l,n)=(N/pi)[l Lambda(pi*n/(l*N))-Lambda(pi*n/N)]
                    +O_l(log N), uniformly 0<=n<N.

Their normalized coherent overlaps are contractive at arbitrary fixed
width. Actual source phases, separator channels and cap powers remain.
This proves boundary-tree energy control, not preservation of those
packets by a general interior braid.

The [marked Casimir source channel](actual_tame_c0_hermite_source_frame.md)
also now has a quantitative positive frame. Its original cup p and
canonical generalized vector t_N are orthogonal, with

    ||p||^2=N^3, N^3/4<=||t_N||^2<=pi^2 N^3/6,
    condition([p,t_N])<=2.

The proof is an exact finite Fourier--Plancherel calculation. The
original marked and ordinary cap rows are the two dual coordinates,
so each has dual norm one in the Hermite Gram. The full crossing,
including its nilpotent part, has norm at most `1+pi*|ell|` for twist
exponent ell in that frame. This controls the selected degree-d
two-plane, not transitions into other channels on overlapping pairs.

The Pascal matrices are finite Euler polynomials in the original
nilpotent current. The same note factors EVERY original signed
same-color crossing, in every integer total-degree block, into
Pascal matrices, their inverses, explicit factorial diagonals and
Gaussian phases. High-degree blocks and actual marked sources remain.
This supplies a known local packet alphabet for arbitrary braid width.
It does not give a bound on its overlapping recouplings.

Two independent estimates supply controlled interfaces:

- The [source-balanced Fermat metric](phase_ratio_bell_weights_and_source_gram.md)
  `H_a=|L_a|/|P_a|` makes both original source costs the explicit
  chord sum `|1-u| sum_a |1-uQ^a|^(-1)`. At every normalized original
  cap, retaining its exact Gamma factors gives cost
  `O(1+|epsilon|log N)`, uniformly in the cap index.
- The [physical factorial metric](actual_source_fixed_divided_fusion_norm.md)
  controls the retained two-head fusion current and its inverse by
  `1+|t|^N H_floor(N/2)/2`. Fixed words of these adapters, including
  overlapping pairs, therefore cost polynomially when their metric
  interfaces agree and `|t|^N` is polynomially bounded.

There is also a [boundary projector theorem](phase_ratio_corner_sector_metric.md):
on the actual doubled corner sector, the cap metric is scalar for real
cap parameters. All flat orthogonal projectors there are contractive;
through the complex cap disk their norms remain polynomially bounded.
The full regularized cap has other sectors, and interior transport of
this particular sector has not been proved.

These are actual source and current estimates. Larger fused-block
currents carry positive angle energy and cannot simply be declared
tame. Transporting one packet metric through a neighboring packet
also retains its full off-diagonal terms.

For one exact three-head reassociation, the retained matrix entry is
`|[u choose a]_Q|=N w_N(a,u-a,N-1-u)`. Its three nonnegative angle
indices sum to N-1 exactly. Thus an exponential interface cost already
has a concrete geometric weight; its squared norm contains the square
of that weight. The global metric must account for the required power
and the actual edge incidence, as well as the source compensation.

The remaining upper-bound problem is now concrete: compose the
explicit packet alphabet and its dual sources into a positive Gram
whose coherent energy satisfies (2), including the true geometric
edge constraints and retained current channels. There is no proof of
that statement for a broad knot class yet.

The [raw positive path model](actual_closed_pascal_route_energy.md)
obtained by dephasing the shear factors has a uniform excessive closed
route even with the original trace constraints. It is not the target
geometric partition. Complete source and interior packets must be
contracted coherently before a sharp positive comparison is made.

The metric must preserve cancellations across suitable packets.
[Every diagonal metric on the complete figure-eight clock sectors](actual_figure_eight_clock_gram_obstruction.md)
has an excessive Cauchy budget. Even
[arbitrary individual-wire matrix gauges](actual_full_matrix_wire_gauge_optimizer.md)
cannot improve the finest crossing-by-crossing norm bound for the
specified alternating-sign words. These statements leave coupled
packet metrics such as (3) available; they specify why choosing an
inner product separately on each wire is insufficient.

The critical path is therefore the geometric bound on the composed
coherent norm, followed by a lower/survival argument. Cauchy itself
is the final elementary step, not another unproved analytic principle.
