# The general long-twist target at arbitrary fixed plat width

31 October 2026 update. The target remains arbitrary fixed k>=2 and
independently sufficiently long FIXED signed twists, with the knots and
slopes fixed before the quantum level tends to infinity. It remains a
CONJECTURE for a general essential hyperbolic augmented skeleton.

The latest [endpoint theorem](general_fejer_endpoint_source_volume.md)
proves the actual augmented volume for the full positive numerator, with
[odd regularization](actual_fejer_odd_regularized_full_numerator.md) and
a [unique geometric maximum](actual_fejer_unique_geometric_maximizer.md).
This settles the positive endpoint optimization at every certified fixed
width. The whole-period and conditional full-invariant results below now extend this endpoint calculation.

The [full spectral numerator theorem](general_full_spectral_numerator_geometric_packet.md)
now proves a nonzero relative asymptotic on a fixed complex neighborhood
of the geometric endpoint, including every spectral Hermite datum. Its
ordinary-face cycle is the original Cauchy torus. The
[absolute marked action](actual_cross_cofactor_marked_action.md) identifies
the unit-charge filling critical value with the actual filled volume.
The [local charge comparison](general_local_charge_critical_monotonicity.md)
proves strict dominance of the all-unit charge among nearby positive
integer charges, uniformly for independent signed twists with no ratio
condition. These results hold under the supplied simple-white geometric
certificate at arbitrary fixed plat width.

The [localized original-period theorem](general_localized_unit_charge_filling_period.md)
now deforms the actual restricted spectral contour to that saddle,
retains its boundary currents, and proves its coefficient is nonzero.
The finite local charge sector therefore has the actual filled volume
as its normalized logarithmic growth rate, at both level parities.

The [entire CROSS period theorem](general_all_cross_long_filling_volume.md)
now controls every original Fourier charge and the whole spectral contour
for the CROSS sector, with its actual filled-volume rate. The
[complete-radius balance theorem](general_complete_radius_balance_filling_volume.md)
also proves the FULL original invariant limit whenever the actual marked
complete packing satisfies its finite test at every port. A sufficient
[algebraic criterion](actual_triangle_entropy_algebraic_balance.md) is

$$ (x+y+b)(x+y+c)\geq\max\{b^2,c^2\}. $$

The theorem permits every independently long fixed signed twist vector,
with no slope-ratio condition. What remains is broad geometric coverage
of this condition, or a bound for the macroscopic one-sided sectors when
it fails. In particular, arbitrary supplied plat width or a numerical
packing experiment does not by itself prove the desired family coverage.
A separate generic-q normal estimate is unnecessary for this exact
fixed-root route; see the [scope audit](fixed_root_direct_power_scope.md).
The older mixed-color route and its conditions are preserved below as
alternative approaches.

The [one-end layer theorem](general_one_end_layer_long_filling_volume.md)
now proves actual balance for a family at EVERY fixed k>=2, with
3k-3 independently long signed twist regions. An exact packing
recurrence and convex comparison prove its curvature bound uniformly.
The [Fox certificate](actual_fox_coloring_exact_plat_bridge.md) gives
subfamilies of minimal bridge number exactly k. This establishes
genuinely unbounded bridge complexity at every k>=2, but not every
k-bridge diagram. The earlier reduced-layer family remains separately
recorded with its original k>=4 scope.

There is now a whole-source intermediate theorem: the
[original signed augmented source](general_signed_augmented_source_volume.md)
has limit equal to the actual complete volume for every fixed connected
plat with the stated labeled right-angled certificate and any retained
half-twist pattern. Both parities and composite levels are included.
This is an augmented-LINK theorem, including patterns whose main strands
form one component; it is not yet the general long-filled knot theorem.

The proof uses the [exact positive face coefficient](actual_original_marked_face_coefficient.md),
its [global torus saddle](actual_positive_face_coefficient_saddle.md), the
[uniform all-channel bound](actual_positive_face_channel_rate.md), and the
[absolute facet-coning volume](actual_original_boundary_stationary_character.md).
The signed extension derives a uniform relative folded Gaussian from
the original continuants and sums the actual phases to a nonzero leading
coefficient. All original factors and the primitive grid measure remain.
The [fixed complex complete-core theorem](actual_complete_core_complex_packet.md)
now supplies a nonzero asymptotic on a fixed neighborhood in EXTERNAL
crossing-circle colors, for the exact complete-image term of reflection.
The [marked geometric assembly](actual_complete_core_geometric_deformation.md)
now identifies its limiting action, including at the zero faces, with
the actual geometric regulator and its complex boundary correction.
The [whole-source untwisted corridor](general_untwisted_mixed_source_volume_corridor.md)
now transfers this volume identity to the original mixed source when
any chosen set of untwisted ports varies near completeness. The [homogeneous source theorem](actual_homogeneous_casimir_face_source.md)
now gives the exact original coefficient for all Casimir coupons and
a JOINT signed/unsigned corridor under finite shared-radius certificates,
including disconnected subsets. Existence of such signed certificates
for a general class and the combined far-color bound remain open. The current
dependency map is in the [frontier chapter](../book/chapters/frontier.md).

The older source, operator, Fourier and torsor tools are preserved below
with their own scopes. They are not an assertion that the general filling
inputs have now been proved.

## 1. Quantifiers and the actual diagram

Fix k>=2 and an ordered 2k-strand plat diagram with r designated
two-strand twist boxes. Every crossing belongs to one of the boxes;
all other wires, cups and caps are those of this fixed diagram. For
example its braid word can be written

    beta(p)=sigma_(i_1)^(epsilon_1-2p_1) ...
             sigma_(i_r)^(epsilon_r-2p_r),
    epsilon_s in {0,+1,-1}, p_s in Z.

The index word, box ordering, endpoint marking and epsilon are fixed.
Adjacent powers of the same generator are combined before treating
their twist parameters as independent. The fixed upper and lower
pairings together with the permutation of the epsilon word must give
one component. This is a finite permutation/matching test: adding a
full twist does not change it. Thus every p gives a knot with a
k-bridge presentation, so b(K_D(p))<=k; equality is not asserted.

Drill one actual crossing circle around each box, remove the full
twists, and retain its specified half twist. Denote the resulting
marked augmented exterior by Y_D. Require Y_D to be hyperbolic, with
the actual primitive crossing-disk markings retained. This is a
geometric hypothesis on the supplied diagram, not an assertion that
every presentation of a hyperbolic knot has hyperbolic augmentation.

**General long-twist conjecture.** For every such fixed diagram D
there is T(D)<infinity such that, for every fixed integer vector p
with all |p_s|>T(D),

    lim_(N->infinity) (2pi/N) log|K_N(K_D(p))|
                      =Vol(S^3 minus K_D(p)).                 (1)

Here N is the quantum level. Twist numbers are fixed BEFORE this
limit. The conjecture includes both level parities and composite
levels, arbitrary signed twist vectors, and no comparability condition
on their magnitudes. It asks for the volume of the FILLED knot, not
the complete drilled volume or a limit in which p grows with N.
For a partial filling the analogous statement is about the remaining
link exterior with its original single marked normalization.

The quantifier is every fixed k and every admissible fixed skeleton;
there is no proposed universal threshold depending on k alone. We use
T(D) for the required twist length so that it cannot be confused with
the quantum level N. A twist region here is a designated two-strand
box with its essential crossing disk, not an arbitrary tangle with a
large crossing count.

Under an actual positive marked gluing certificate, the
[geometric long-filling corollary](general_augmented_plat_long_filling_quantifiers.md)
now proves a threshold T_geom(D) for complete hyperbolic geometry of
every independently long signed filling. Existence of the quantum
threshold T(D) in (1) is the remaining conjectural assertion for a
general skeleton. These two thresholds must not be conflated.

A [finite sufficient geometric criterion](general_simple_white_plat_class.md)
is now available: the ACTUAL white cellulation of the flat plat is a
simple triangulated sphere. The existing angle optimization and labeled
cut construction then supply its complete right-angled geometry, with
all prescribed half-twist patterns and primitive markings. This class
has explicit examples at every fixed supplied width. It is a sufficient
class for the geometric and endpoint results. Assertion (1) is now proved
in its complete-radius balanced subclass; without that additional test
it remains open.

## 2. Why twist length needs a diagram hypothesis

Raw box counts do not measure geometric twisting. For the actual
crossing operator, including its Cartan factor,

    R^(2p) R^(-2p+2c)=R^(2c).                               (2)

Both displayed blocks can have arbitrarily many crossings while the
diagram remains the fixed bounded-twist diagram on the right. The
identity holds inside ANY 2k-strand source and before its marked cap.
It is an exact algebraic cancellation, not an asymptotic example.
Likewise a nugatory twist can change a presentation without adding an
essential drilled cusp. Thus independent long parameters must refer
to actual essential crossing disks. Certifying Y_D directly is a
uniform way to impose this requirement without restricting k or
assuming that a visually complicated plat is geometrically essential.

## 3. The exact reduction already works for every fixed k

The all-input circle identity gives the original full-twist expansion
on each pair of strands. Let A_(D,N)(h_1,...,h_r) be the actual
augmented source with circle color j_s=N-h_s, including all its
specified half twists, cups, caps, pivots and the exposed first cut.
Then the [general source transfer](general_original_source_long_filling_transfer.md)
has the exact identity

    K_N(K_D(p))=chi_N kappa^(-2 sum_s p_s)
       sum_(j_1,...,j_r=1)^N
       product_s beta_(j_s-1)^(-p_s) A_(D,N)(N-j).            (3)

The source A is defined before the displayed recorded outer factor
chi_N; it is not normalized using the unknown answer. All repeated
Casimir-root normals are part of beta. Multilinearity applies each
substitution in its original operator order. Physical crossings at
different boxes need not commute. Only the independent color-register
functionals commute.

Consequently the long-twist problem does not require a new surgery
formula for each bridge number. The same exact filling map is already
available. What is missing generally is control of its input A_D.

There is also a direct polynomial form, supplied by the homogeneous
source theorem. For N>=3 put d=N-1 and let f_(e,N,p)(Omega) be the ACTUAL root
Casimir polynomial for the whole operator
R^(epsilon_e-2p_e) in the original box, including its repeated-node
Hermite data. If Z_(D,p,N) denotes the original marked contraction
before its recorded exterior framing factor, then exactly

    Z_(D,p,N)=[prod_(ordinary faces f) L_f^d]
                prod_e H_(f_(e,N,p)) |_(L_u=L_v=0).        (3a)

Every local polynomial has degree d; the number of shared face variables
depends only on the fixed skeleton. Thus (3a) is an exact polynomial
form of the full source at arbitrary fixed k, including negative twists.
The known exterior normalization is retained when passing from Z to
K_N. This gives a second route for studying long twists directly at
each box. No sharp long-power estimate for these kernels is being
assumed: their coefficients are complex, and larger p does not by
itself make their shared-face contraction positive. Nor is (3a) being
called the eliminated knot A-polynomial.

These whole-box kernels also compose without introducing an external
circle color. For two Casimir polynomials f,g, exactly

    H_(fg)(x,b,c,y)=[z^d] H_f(x,b,z,y) H_g(x,z,c,y).         (3b)

Indeed the input index j of the left kernel contributes z^(d-j),
while the output index j' of the right kernel contributes z^j'.
Extraction forces j'=j and gives the original matrix composition.
Thus arbitrary positive or negative twist powers admit a layered
coefficient formula using only the literal R or R^-1 kernels, with
all their scalar phases retained. This is an alternative finite
presentation of the same source, not a new asymptotic estimate.

The [direct-power theorem](actual_direct_long_power_source.md) retains
the original phases and proves a limitation of the absolute-value
spectral bound. The [crossing Casimir theorem](actual_crossing_casimir_torus.md)
now solves the local classical transport uniformly in the twist power:
on the generic spectral cover it is multiplication by lambda^n on a
punctured norm torus, with a separate additive parabolic fiber. Its
canonical Hamiltonian agrees with the exact full-Hermite quantum
Gaussian. These facts hold independently of bridge width; they do not
supply the remaining global coefficient estimate or an eliminated
knot A-polynomial.

The [physical meridian transport](actual_crossing_torus_meridian_transport.md)
now gives a further width-independent algebraic result. Differentiating
the original physical kernel, including its half powers and the outer
head derivative, fixes the physical momentum as the reciprocal of the
coefficient momentum. The resulting matrices obey the full signed
Hurwitz relations, not merely conservation of their Casimir trace.
After the literal cup/cap/marked constraints are imposed, every FULL
regular critical point of the layered source defines a representation
of the actual filled diagram group. This is a forward morphism on its
specified regular open scheme; it is not a classification of critical
points after setting protected faces to zero, nor a proof that the
original coefficient cycle selects the geometric representation.

The [full spectral total derivative](actual_spectral_total_derivative_source.md)
and [Gaussian resolvent numerator](actual_gaussian_resolvent_numerator_and_cap.md)
retain both semisimple and nilpotent data of every original pair Casimir.
The numerator is an exact coherent transform of ALL physical colors;
its positive path expansion can be sewn with the same shared face
targets. The closing cap near spectral +2 is controlled at fixed twist
power. The fixed complex shared numerator and entire CROSS spectral
period are now proved. Complete-radius balance also controls the full
one-sided remainder. Without that condition, its macroscopic sectors
remain to be estimated. Long twisting alone does not damp both sides
of a spectral contour.

The [full positive endpoint theorem](general_fejer_endpoint_source_volume.md)
now proves W_D=Vol(Y_D)/(2pi) for the original even numerator under the
labeled right-angled certificate, at every fixed plat width. Its full
local support gives one unrestricted incidence-flow polytope; the older
single-level support test remains useful only for fixed branch patterns.
The [odd regularization](actual_fejer_odd_regularized_full_numerator.md)
has the same rate and supplies explicit bounds for fixed spectral jets.
The [unique-maximizer theorem](actual_fejer_unique_geometric_maximizer.md)
identifies the only endpoint maximum with the original marked complete
geometry and gives a strict gap for its complement, including the entire
one-sided remainder. These are positive-source and spectral statements.
The localized spectral Gaussian unit-charge contribution is now proved.
The entire CROSS period and balanced full remainder are now controlled
as well; unrestricted geometric coverage remains the gap.

## 4. Remaining inputs and preserved alternative routes

For the current direct fixed-root route, the full local numerator packet,
its contributing ordinary-face saddle and the marked filled critical
value are proved by the results linked at the start. The whole-CROSS
period and full balanced-class limit are also proved. The remaining
input is broad coverage of balance or a more general full remainder
estimate. The mixed-color
requirements in this section concern the older alternative route and
must not be added as prerequisites to the direct one.

**Full mixed-color quantum source.** The complete-image term already
has its exact holomorphic packet and a uniform complex asymptotic.
The original mixed source agrees with it exponentially accurately on
the physical integer corridor for all untwisted varied ports, and for
joint signed/unsigned ports satisfying the finite certificates below.
What remains generally is to establish those certificates (or stronger
phase-preserving estimates), and to bound the combined original source
on the ENTIRE physical color complement. This must include opposite-end
aliases, their exact cancellations, and the normal currents used by
the filling transform. The marked multiport Chebyshev/Parseval packet
is exact at every fixed k, but its physical source-to-coefficient
energy is still the quantity to estimate.

For clarity, the new near-complete sufficient condition is finite and
independent of the quantum level. For every nonempty reflected subset
S of the varied ports, choose ONE shared positive weight per original
face such that

    C_S(l)=sum_(e notin S) [F(x_e,b_e,y_e)+F(x_e,c_e,y_e)]
           +sum_(e in S,epsilon_e!=0) G(b_e,x_e,y_e,c_e)
           +sum_(e in S,epsilon_e=0) log max(b_e,c_e)
           -sum_(ordinary faces f) log l_f
             < Vol(Y_D)/(2pi).

Here F is the complete triangle potential and G the exact crossing
coefficient-magnitude potential defined in the
[homogeneous source theorem](actual_homogeneous_casimir_face_source.md).
Different subsets may use different weights. The finite strict margins
give one fixed color corridor for ALL subsets, including disconnected
ones, at arbitrary fixed bridge width. Establishing these inequalities
for a structural class of diagrams is a general theorem problem; it
does not require a separate quantum asymptotic for each knot. Their
validity alone still does not control the far-color complement.

**Actual geometry.** Supply the marked complete augmented exterior
and its absolute volume anchor. A positive ideal gluing certificate
on a triangulation of the actual exterior is one sufficient route.
Another starts from its actual disk/projection cut: the cubic graph
of shaded triangles and its distinguished crossing-circle matching
describe the whole polyhedron, and a positive right-angled realization
supplies the complete metric. A triangulation of an unrelated
manifold or a numerically matching volume does not identify this
labeled topology.

The [general marked gluing certificate](general_marked_positive_gluing_certificate.md)
proves the geometric implication directly. It also proves the
Casson--Rivin equivalence with an interior critical point of the
actual angle-volume function, whose unique maximum is Vol(Y_D).
Positive phases and positive multiplier variables give a finite
algebraic certificate; the selected optimum has algebraic shapes.
None of these geometric facts implies the quantum packet estimate.

**Same selected action.** Prove that the critical source action is
the calibrated primitive on the ACTUAL peripheral branch, retaining
the selected square roots and logarithms. The required equations are

    G=2pi i phi, U_s=-2pi i x_s,
    V_s=-2 partial_s phi,
    Im G(0)=Vol(Y_D).                                      (4)

The filled source saddle then gives the primitive equation
U_s+p_s V_s=-2pi i. The existing geometric completion theorem
constructs the actual smooth filled metric and identifies its volume
with the boundary-corrected source action. It is this last equality,
not an unnamed source volume, that yields the right side of (1).

The already proved long-filling transfer is independent of k once
these inputs are available. It must not be cited as having supplied
them for an arbitrary plat.

The new [critical-scheme equivalence](actual_augmented_plat_critical_scheme.md)
and [marked multi-cusp rigidity](general_marked_multicusp_gluing_rigidity.md)
now supply a nearby geometric stationary branch under an actual positive
gluing certificate. The only magnetic Hessian null directions are the
two framing directions; a transverse slice removes them. The branch
has the actual peripheral differential and absolute volume anchor.
The quantum statement still requires that the original finite source
select and contribute to this branch.

The new [actual local character map](actual_augmented_plat_local_critical_character_map.md)
proves the primitive differential on any correctly marked stationary
branch. The [absolute endpoint regulator theorem](actual_augmented_plat_endpoint_regulator.md)
proves the complete-volume anchor at a regular correctly marked
geometric critical point. A [generic framing theorem](actual_augmented_plat_regular_geometric_phase_chart.md)
supplies a regular unfolded geometric candidate, but does not select
its physical logarithmic sheet or a contributing quantum cycle.
Thus the identities in (4) have a general classical proof with these
hypotheses. Under the stronger labeled right-angled certificate the
complete-image source realization is now proved; its extension to
the full mixed source outside the proved corridors remains part of
the quantum problem.

The [actual channel Hessian](actual_augmented_plat_channel_hessian.md)
also has a general primitive normalization: H_(xi_i,xi_j) is
-delta_ij 4pi i/tau_i, and the channel/magnetic mixed block vanishes.
Its negative real part gives a local channel elimination at the
geometric endpoint, while holding the magnetic variables as parameters.
It supplies no nonzero cycle coefficient or magnetic asymptotic.

## 5. Preserved operator and Fourier routes

The [complete source compiler](actual_augmented_plat_phase_compiler.md)
and [all-color compiler](actual_mixed_augmented_plat_compiler.md)
give explicit finite factorial sums, phases and generic confluence
normals for every fixed plat. Their inverse measures retain their
exponential profiles. No unknown local recoupling inverse remains.
The [entire core function](actual_augmented_plat_entire_core_color_packet.md)
also supplies an exact separately-even finite Fourier interpolation,
including the odd endpoint. It does not supply a uniform complex
asymptotic. If the required nonzero analytic corridor packet exists,
its periodicity mirrors the same rate near the opposite cube face.
The actual physical alias split therefore matters for the global gap.

For each actual local q-Hahn column, the
[negative-root theorem](actual_q_hahn_negative_root_source_polynomial.md)
now proves a canonical slit-plane logarithm, and the
[complex-action theorem](actual_q_hahn_selected_complex_action.md)
proves its actual leading action on the physical Fourier arc. The
[uniform amplitude theorem](actual_q_hahn_uniform_complex_amplitude.md)
adds a nonzero prefactor with relative error O(1/N). The
[magnetic corridor theorem](actual_q_hahn_magnetic_complex_corridor.md)
continues the actual finite kernel in one magnetic variable while
the pair degree and channel stay real and discrete. The subsequent
[joint determinant](actual_q_hahn_joint_accretive_determinant.md) and
[joint amplitude theorem](actual_q_hahn_joint_complex_amplitude.md)
now continue pair degree and magnetic coordinate together on a fixed
central domain, including folded channels, with an explicit selected
local sheet. The channel remains an integer. The
[common-framing criterion](actual_augmented_plat_physical_framing_criterion.md)
states finite strict inequalities for simultaneous use on a plat;
the [right-angled obstruction](actual_right_angled_selected_framing_obstruction.md)
now proves that an all-central selected frame cannot exist for the actual
certified right-angled cut. Generic geometric strip flags localize the
weaker strict physical-support failures to exactly TWO factors, for
arbitrary bridge width. Those facets can be prescribed, including the pair
adjacent to the original marked physical edge. The
[full physical packet](actual_q_hahn_full_physical_complex_packet.md)
and [selected-factor corollary](actual_augmented_plat_selected_factor_localization.md)
now put EVERY other ordinary factor in its actual selected physical
packet, with no central-support hypothesis. The two exceptions can
instead be placed together at one crossing-circle matching edge.
The [selected local certificate](actual_augmented_plat_selected_local_certificate.md)
remains a conditional local theorem; it does not establish a whole-source
cycle or sum estimate. The
[small-channel generic-normal estimate](actual_q_hahn_small_channel_generic_normals.md)
and [exact partner collision](actual_q_hahn_partner_normal_collision.md)
retain the original derivatives. The latter exposes additional individual
normal poles, so a full-domain paired-normal estimate cannot be assumed.
The [physical paired-normal theorem](actual_q_hahn_physical_partner_normal_bound.md)
does prove polynomial relative cost on the whole complete physical grid,
retaining the actual large partner and both parities. The [complex near-fold theorem](actual_q_hahn_near_fold_complex_partner_bound.md)
now supplies subexponential relative cost on a fixed complex compact
when (l-j) log N=o(N). A fixed nonzero scaled channel shift and a
whole-source asymptotic remain open.
Every fixed generic q jet of all physical columns and completed divided
pairs is also controlled by the
[physical generic-jet theorem](actual_q_hahn_physical_generic_jet_bound.md).
Its forward/backward proof does not supply a completed boundary tensor
norm. The full physical packet extends the complex near-fold bound to
all fixed physical compacts, still with a shrinking scaled channel window.
These local results are not a whole-source asymptotic. Outside the
specified marked domain the endpoint quadratic has monodromy, so an unspecified
analytic continuation alone cannot identify the selected geometric
root. A controlled simultaneous continuation and a global cycle
estimate remain necessary.

Choosing the exceptional pair at a crossing-circle matching edge
also gives the [exact marked four-port rewrite](actual_matching_edge_marked_four_port_block.md)
of the COMPLETE-circle source. Its original row measure cancels the
exponential factorial gauge, and the
[positive scalar theorem](actual_matching_edge_racah_positive_scalar.md)
controls every recoupling target and fixed generic jet. The
[completed-projector formula](actual_matching_edge_completed_projector_block.md)
also cancels the target scalar gauge and combines the collision pairs
before taking the first normal, retaining their nilpotent part.
The remaining native projector/complement costs are explicit but not yet sharply
bounded by the geometric action. This is not the general mixed-color
packet required for fixed long fillings.

The [native-projector energy theorem](actual_matching_edge_native_projector_energy.md)
now bounds every fixed generic operator derivative by a polynomial
times its explicit magnetic energy, uniformly at both parities and
all physical degrees. A simple midpoint channel proves that energy
can itself be exponential. The remaining joint variational estimate
must keep the actual shared wire variables and these energy terms;
independent local maxima do not supply it.

The [full folded boundary rate](actual_matching_edge_magnetic_energy_profile.md)
is now computed by exact Plancherel and the actual selected endpoint
polynomial. It remains valid in [all shrinking real fold windows](actual_matching_edge_shrinking_fold_native_energy.md).
For arbitrary fixed skeletons, the
[shared-cycle compiler](actual_matching_graph_shared_cycle_fourier_compiler.md)
gives an exact bounded-flow source with coupled Fourier congruences
and the original one-unit mark. Its
[positive coefficients](actual_q_hahn_fourier_coefficient_variational.md)
have a uniform interior variational rate. These source reductions
retain every shared label and phase. They do not supply the general
mixed-color packet, sharp joint geometric estimate or lower bound
needed for the fixed-long-filling theorem.

The [explicit positive partition](actual_matching_graph_positive_fourier_partition.md)
now gives a polynomial-loss Cauchy upper bound retaining every shared
flow and Fourier charge. Its sharp rate is not yet the hyperbolic
volume: the [conditional radial-frame obstruction](actual_positive_fourier_radial_geometric_obstruction.md)
prevents one proposed all-ordinary geometric reconstruction, without
proving a numerical gap. The exact coherent source and the retained
exceptional matching block remain the objects to estimate.

The [full graph identity](general_matching_graph_full_normal_source.md)
puts all folded labels and normals on the actual matching graph.
The [reflection-double identity](actual_planar_three_port_reflection_double.md)
removes the final gluing cancellation for specified three-port
doubles, retaining the full source. Neither identity already bounds
the internally coherent half-packets for arbitrary graphs.

The [matching-graph geometry](general_augmented_plat_matching_geometry.md)
constructs the actual complete complement and primitive markings
from a labeled positive right-angled certificate. It also constructs
a positive ideal triangulation. The
[geometric endpoint theorem](actual_augmented_plat_geometric_channel_endpoint.md)
locates the complete disk character at c=-2, the folded-channel
endpoint, and retains its marked peripheral square root. This is
necessary geometric information, not a proof of quantum selection.
The [endpoint phase calculation](actual_central_endpoint_magnetic_phase_obstruction.md)
also shows that a universal separate-leg positive normalization
already fails at N=3. It leaves coherent resummation available.

The [source-divisor extension](general_long_filling_source_divisor.md)
allows a nonzero analytic source-density germ to vanish at the
complete point. With the other packet, gap and geometric hypotheses
proved, it yields the filling equality away from an analytic
exceptional divisor, including density one of long slopes in each
signed box. A peripheral monomial times a unit gives EVERY
independently long signed slope. The general nonzero-germ version
does not by itself prove the all-slopes conjecture (1).

These results remove finite-source and geometric ambiguities. The
principal remaining theorem is still a coherent asymptotic with
the required global gap and the actual selected geometric period.

The [arbitrary-width Conway extension](actual_conway_arbitrary_width_seeds.md) is retained as
an application and a calibration of these interfaces. It does not
settle (1) for all k-bridge diagrams. The full cube source, which lies
beyond that grammar, remains one useful branching test, not the
definition of the general target.

## 6. Literature coverage only

Purcell's [highly twisted volume paper](https://research.monash.edu/en/publications/volumes-of-highly-twisted-knots-and-links/)
states hyperbolicity and geometric volume bounds under diagrammatic
hypotheses; those are not an original Kashaev volume-limit theorem.
Van der Veen's [augmented KTG paper](https://arxiv.org/abs/0805.0094)
states a volume conjecture result for its augmented knotted trivalent
graphs and a containing-link corollary. Its abstract does not assert
(1) for all independently long fillings of arbitrary fixed plats.
These are coverage observations, not imported proofs or an exhaustive
novelty claim. The definitions and source normalizations must still
be compared before identifying any covered family.


A further primary-statement coverage check on 31 October 2026 distinguishes
three nearby claims. [Giambrone](https://arxiv.org/abs/1310.8414v3) states
coarse volume bounds for certain plat closures via stable Jones
coefficients. [Lee](https://arxiv.org/abs/2307.09903v2) takes the twist
parameters to infinity to obtain a limiting skein element before studying
its root-of-unity growth. [Shen](https://arxiv.org/abs/2609.11839v3) states
long fixed signed filling results for SO(3) Turaev-Viro and WRT invariants
of fundamental shadow-link fillings along odd levels. These abstract
statements have different invariants or quantifiers from the full
Kashaev knot limit here. This checks stated coverage only: no proof
correctness, equivalence of invariants, or exhaustive novelty conclusion
is inferred, and no proof technique from these papers is used above.
