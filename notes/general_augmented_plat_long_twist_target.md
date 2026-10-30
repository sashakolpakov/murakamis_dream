# The general long-twist target at arbitrary bridge number

30 October 2026. The target is an original Kashaev volume equality for
arbitrary fixed bridge number and arbitrary fixed essential twist
skeleton. A Conway seed grammar is an established application, not the
definition of the intended general class. The statement below remains
a CONJECTURE until the full source estimates and selection of the
geometric period are proved for its general skeleton.

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
k-bridge presentation; k need not be its minimal bridge number.

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
there is no proposed universal threshold depending on k alone.

Under an actual positive marked gluing certificate, the
[geometric long-filling corollary](general_augmented_plat_long_filling_quantifiers.md)
now proves a threshold T_geom(D) for complete hyperbolic geometry of
every independently long signed filling. Existence of the quantum
threshold T(D) in (1) is the remaining conjectural assertion for a
general skeleton. These two thresholds must not be conflated.

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
substitution in its ORIGINAL operator order. Physical crossings at
different boxes need not commute. Only the independent color-register
functionals commute.

Consequently the long-twist problem does not require a new surgery
formula for each bridge number. The same exact filling map is already
available. What is missing generally is control of its input A_D.

## 4. The three tasks on a general augmented skeleton

**Full quantum source.** Establish an exact holomorphic color packet
for A_D near the complete colors, with a uniform complex asymptotic,
and an exponential gap on the ENTIRE physical color complement.
The estimate must include all aliases and normal currents. A bound
for one positive sector or for independently maximized vertices does
not give this input. The marked multiport Chebyshev/Parseval packet
is exact at every fixed k, but its physical source-to-coefficient
energy is still the quantity to estimate.

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
hypotheses; their realization by the actual selected source remains
part of the quantum problem.

The [actual channel Hessian](actual_augmented_plat_channel_hessian.md)
also has a general primitive normalization: H_(xi_i,xi_j) is
-delta_ij 4pi i/tau_i, and the channel/magnetic mixed block vanishes.
Its negative real part gives a local channel elimination at the
geometric endpoint, while holding the magnetic variables as parameters.
It supplies no nonzero cycle coefficient or magnetic asymptotic.

## 5. What the current general work is changing

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
adjacent to the original marked physical edge. The other factors need not lie in the central
domain. Thus continuation or coherent resummation is required.
The [selected local certificate](actual_augmented_plat_selected_local_certificate.md)
remains a conditional local theorem; it does not establish a whole-source
cycle or sum estimate. The
[small-channel generic-normal estimate](actual_q_hahn_small_channel_generic_normals.md)
and [exact partner collision](actual_q_hahn_partner_normal_collision.md)
retain the original derivatives. The latter exposes additional individual
normal poles, so a full-domain paired-normal estimate cannot be assumed.
The [physical paired-normal theorem](actual_q_hahn_physical_partner_normal_bound.md)
does prove polynomial relative cost on the whole complete physical grid,
retaining the actual large partner and both parities. A complex corridor
for that normal and a whole-source estimate still require proof.
These local results are not a whole-source asymptotic. Outside the
specified marked domain the endpoint quadratic has monodromy, so an unspecified
analytic continuation alone cannot identify the selected geometric
root. A controlled simultaneous continuation and a global cycle
estimate remain necessary.

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
