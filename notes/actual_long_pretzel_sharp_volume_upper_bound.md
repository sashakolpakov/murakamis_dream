# The hyperbolic-volume upper bound for the full original long-pretzel invariant

**Subsequent equality, 29 October.** The [geometric completion proof](actual_long_pretzel_geometric_filling_completion.md)
now proves rho_p is the holonomy of a complete positively oriented
metric on the actual filled knot. The upper inequality below is
therefore an equality on the SAME sufficiently long fixed signed
class. See the [Casson--Rivin equality proof](actual_long_pretzel_casson_rivin_equality.md)
and [full completion audit](long_pretzel_volume_equality_completion_audit.md).
This note retains the intermediate upper-bound argument as a dependency.

29 October 2026. This assembles the whole-source asymptotic, the
literal representation/peripheral lift, and the marked regulator
comparison. The upper bound uses the ACTUAL filled hyperbolic volume,
with coefficient one. The equality required by the full volume
conjecture is distinguished explicitly below.

## 1. Statement and scope

For every fixed odd integer s>=25 there is an integer p_s>0 with
the following property. Let p_1,...,p_s be independently chosen
fixed signed integers satisfying |p_i|>=p_s, and let K be the
original odd pretzel knot with boxes R^(-(2p_i+1)). Assume its
complement is hyperbolic, as in the standing project hypothesis.
Then the ORIGINAL normalized Kashaev invariant satisfies

    lim_(N->infinity) (2pi/N)log|<K>_N|
        =Vol(rho_p) <= Vol(S^3 minus K).                  (1)

Here rho_p is an explicitly constructed boundary-parabolic PSL2(C)
representation of the ACTUAL filled knot group. The limit exists,
and its leading source coefficient is nonzero. Both level parities
and all composite levels are included. The fixed slopes need not
have comparable sizes or the same signs.

The class has no upper bound on its number of twist regions, and
each sufficiently long twist parameter varies independently. It is
not a fixed-width twist family or a finite list of tested knots.
No assertion for small widths or short slopes is inferred from (1).

The hyperbolicity assumption is explicit. The proof below does not
use an unproved claim that every displayed diagram is hyperbolic,
or require a faithfulness theorem for rho_p in order to establish
the upper bound.

## 2. The full original source supplies a nonzero limit

The [whole-source survival theorem](actual_long_pretzel_full_source_survival.md)
proves, including the ENTIRE original color cube,

    Kraw_N=N^(3/2) exp[-i s pi(N-1)/4]
            kappa^(-sum p_i) D_s(p) exp[N A_s(p)]
                                   (1+O_(s,p)(1/N)),
    D_s(p)!=0.                                          (2)

Its global bound includes all ordinary color bands, the even middle
color, and every Casimir normal derivative. Its coherent filling
estimate retains the zero-charge cancellation, all nonzero charges,
paired endpoint currents and the exact original half-color weights.
The unit charges add rather than being assigned an assumed cycle
coefficient. All these statements are quantitative source estimates,
not consequences inferred from classical stationary equations.

The actual framing/cut normalization gives |<K>_N|=|Kraw_N|.
The optional full one-cut modified convention contributes the kept
factor i^(N+3)/N, with the same exponential rate. It follows that
the left side of (1) exists and equals 2pi Re A_s(p).

## 3. Its selected point is an actual filled-knot representation

The [source-selected mixed lift](actual_pretzel_mixed_regular_character_lift.md)
derives the regular internal coordinates from the literal finite
recurrence and verifies their stationary rational identities.
The [full port and geometric-anchor theorem](actual_pretzel_port_lift_and_geometric_anchor.md)
then constructs actual parabolic main meridians and auxiliary
matrices C_i,P_i, with

    [C_i,P_i]=1,
    M_i=H_i^(-1/2), lambda_i=-L_i^(-1)

on the same eigenflag. It verifies every original cap in the actual
right-to-left multiplication order. The common w and the outer
equation product_i U_i=1 close the full original diagram. This is
a representation of that diagram's group, not a trace variety
introduced independently of the source.

The [preferred-longitude certificate](actual_mixed_crossing_circle_preferred_longitude.md)
proves that P_i is the disk-framed longitude, with no unrecorded
meridian power. The minus in lambda_i is forced by the original
auxiliary pivot. With continuous z_i=Log H_i and ell_i=Log L_i,
the actual unit-charge filling equation is

    z_i+2p_i ell_i=2pi i.

It gives C_i P_i^(p_i)=(-1)^(p_i-1)I, as a MATRIX identity on
the regular nearby branch. Thus it kills the primitive filled
slope in PSL2 and defines rho_p on the actual knot group. A
particular SL2 lift may require a mod-two character change; no
SL2 descent is needed for the PSL2 representation-volume bound.
The main meridian remains noncentral parabolic, so its commuting
peripheral image is boundary-parabolic.

At the complete augmented point the same representation agrees
with every white and shaded face pairing of the four-antiprism
geometric construction. The absolute auxiliary translations also
match the primitive disk longitude and positive diagonal meridian.
The reversed cap traversal is accounted for by an explicit
orientation-preserving holomorphic isometry, not by taking a mirror.
This supplies the oriented geometric anchor V_s.

## 4. The source action is the absolute regulator of rho_p

The [marked regulator comparison](actual_pretzel_marked_regulator_and_filling_action.md)
keeps the preferred SL sign before centering. If G is the source
action with G_(z_i)=ell_i, put

    u_i=-z_i/2, v_i=pi i-ell_i,
    Gbar=G-pi i sum_i z_i.

Then dGbar=2 sum v_i du_i, and the marked regulator is

    Dsrc=ImGbar-2 sum Reu_i Imv_i
        =ImG-sum Rez_i Imell_i.                          (3)

The actual fundamental Bloch boundary is -2 sum M_i wedge lambda_i.
Its elementary differential agrees with (3), and the complete
geometric anchor fixes their SAME absolute constant V_s. Thus Dsrc
is the regulator of the representation constructed above throughout
the selected connected local branch.

The ORIGINAL Gaussian filling action is

    W=G+sum_i (z_i-2pi i)^2/(4p_i).

At its critical point, Re z_i=-2p_i Re ell_i. Consequently

    2pi Re A_s(p)=ImW
       =ImG+2 sum_i p_i Reell_i Imell_i
       =Dsrc.                                           (4)

No peripheral or endpoint correction is omitted in (4): the
quadratic is precisely the one in the source-preserving filling
formula, and the spin terms cancel only in their complete paired
regulator expression.

Finally compare the augmented and filled fundamental chains using
one finite compatible triangulation of the truncated core and the
attached solid tori. The proved axis-cusp homotopy first replaces
the OLD filled-boundary data by an axis-valued map without changing
the augmented regulator. Assign those boundary vertices and every
new solid-torus vertex equivariantly to that SAME invariant axis.
The killed primitive slope makes the assignment descend through
the solid-torus fundamental group. Every added tetrahedron is
collinear and has zero volume. The core plus solid-torus chain
therefore computes the filled boundary-parabolic representation
volume with no new constant. This proves

    2pi Re A_s(p)=Vol(rho_p).                            (5)

The boundary replacement uses the explicit O(Y^(-2)) homotopy
estimate in [the general peripheral volume proof](general_peripheral_representation_volume_bound.md),
sections1--2. Merely assigning NEW vertices an axis flag while
leaving arbitrary old boundary data would not justify (5).

## 5. Apply the independent sharp representation-volume estimate

For an oriented complete finite-volume hyperbolic manifold X and
a boundary-parabolic representation rho, the independently proved
[representation-volume theorem](regular_critical_values_and_representation_volume_bound.md)
gives

    |Vol(rho)|<=Vol(X).                                 (6)

Its proof averages finite regular tetrahedra, cancels all four
face-homotopy errors by Haar invariance, and lets their volumes
increase to the maximal ideal-tetrahedron volume. It does not
assume a quantum volume conjecture or faithfulness of rho.
Apply it to the actual hyperbolic filled complement and rho_p.
Equations (2),(5),(6) prove (1).

Thus the requested sharp full-original-source UPPER-BOUND milestone
holds for the stated broad class. Equality in (1), and hence the
full volume conjecture for that class, additionally requires proving
that rho_p is the positive geometric Dehn-filling representation
(or an equivalent equality argument). This theorem does not count
that remaining geometric completion as already proved. It also
makes no assertion for all hyperbolic or all alternating knots.
