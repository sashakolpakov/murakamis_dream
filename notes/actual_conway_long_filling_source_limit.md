# Long-full-twist volume equality for every retained robust Conway factor

29 October 2026. The complete quantum hypotheses of the general
long-filling transfer theorem now hold for EVERY retained cylindrical
robust Conway factor. This gives a full original-source limit after
independently sufficiently long fixed signed integral full twists,
with a nonzero leading coefficient and both level parities retained.

Its rate is the ACTUAL hyperbolic volume of the correctly marked
filled link complement. The [marked deformation theorem](actual_conway_marked_peripheral_deformation.md)
constructs the required representation and fixes its absolute regulator.
These pure robust sources remain LINKS after the indicated fillings;
they do not give a new knot family.

## 1. Exact scope and source normalization

Let C(E) be C(A), A=h^3, or C(FG) with F,G robust expressions generated
by A, the actual quarter-turn and actual product. Fix the entire
compiled diagram, its retained auxiliary circles and original mark.
Choose a subset I of the auxiliary circles. At each i in I substitute
the original full twist R^(-2p_i) through its exact Fourier--Hermite
auxiliary-color kernel. Unfilled colors stay at their complete value;
they are not assigned p_i=0.

Let K_(E,N)(p) denote this actual scalar with its separately recorded
original enhancement/framing factor chi_N, where log|chi_N|=o(N)
and chi_N is nonzero. The result applies first to the literal raw
one-cut source and then to any stated normalization with this property.
No new normalization depending on the unknown completed invariant is
introduced.

The principal analytic inputs are now proved:

* The [mixed-leaf identity](actual_pure_conway_auxiliary_color_leaf.md)
  retains the full repeated-root algebra, positive core and signed
  square-zero radical.
* The [uniform whole-source gap](actual_conway_uniform_mixed_source_gap.md)
  bounds every propagated alias and the ENTIRE complementary physical
  color cube after arbitrary finite turns and branching.
* The [finite complex packet](actual_conway_complex_window_laplace.md)
  has a uniform, separately-even, nonzero asymptotic on a fixed complex
  neighborhood, with its actual integer lattice and D=N-1 offsets.

These facts supply hypotheses (2)--(5) of the
[general original-source transfer theorem](general_original_source_long_filling_transfer.md).
Its already proved exact contour and charge argument therefore applies.
No source assumption is inferred merely from geometric existence.

## 2. The actual packet and its selected action

Use chi_i=(N-j_i)/N for each chosen auxiliary color. Let y denote the
free wire coordinates of the reduced strict source problem. Define

    f_E(y,chi)=sum_leaves g_(chi_l)(x_l(y))
                           +sum_retained_products m(x,y,z),
    g_chi(x)=J(2x)-2J(x)-J(x-chi)-J(x+chi),
    J(x)=integral_0^x Log(2sin(pi t))dt,                       (1)

where chi_l=0 for unfilled circles, the source marks are continued from
the positive complete chamber, and all true product/turn relations
remain in the affine wire maps.

There is a unique holomorphic critical branch y_*(chi) near the strict
complete optimizer. Put

    phi(chi)=f_E(y_*(chi),chi).
                                                               (2)

The exact finite packet has asymptotic
N^(3/2) a_E(chi) exp[N phi(chi)](1+O(N^-1)), with a_E nonzero and
a_E(0)>0, uniformly in a fixed complex polydisk. Both phi and a_E are
separately even. If x_(i,*) is the complete maximizing leaf label, then

    phi(0)=max V_E/pi,
    phi''(0)=-2pi diag(cot(pi x_(i,*))).                       (3)

Thus the transfer theorem's parameters are
tau_packet,i=i cot(pi x_(i,*)), with positive imaginary part.
They are HALF the actual complete geometric cusp ratios
tau_geom,i=2i cot(pi x_(i,*)); this factor is required by the recorded
full-twist/peripheral convention.

## 3. The unconditional original-source limit

For independently sufficiently large fixed signed integers p_i,
let chi_*(p) be the unique small solution of

    partial_i phi(chi)+(pi i/p_i)(chi_i-1)=0
                                                    for i in I. (4)

Existence and uniqueness follow by the implicit-function theorem in
the small independent parameters 1/p_i. Define

    S_p(chi)=phi(chi)+(pi i/2)sum_(i in I)(chi_i-1)^2/p_i.
                                                               (5)

Then the FULL original invariant has a nonzero asymptotic of the form

    K_(E,N)(p)=chi_N kappa^(-sum_i p_i)
       N^(3/2) D_E(p) exp[N S_p(chi_*(p))](1+O_p(N^-1)),
    D_E(p)!=0,                                                (6)

with the explicit retained unit Cartan/framing factors of the transfer
theorem. In the pure positive mixed-circle chart its packet phase
eta_N is one. In particular

    lim_N (2pi/N)log|K_(E,N)(p)|
               =2pi Re S_p(chi_*(p)).                         (7)

To check (4)--(5) directly against the transfer conventions, its
Fourier critical equations are

    partial_i phi(chi)+2pi i z_i=0,
    chi_i-2p_i z_i=1.

Thus z_i=(chi_i-1)/(2p_i); substituting into
phi(chi)+2pi i chi.z-2pi i sum(p_i z_i^2+z_i) gives exactly (5).
The nonzero prefactor and the addition of the minimal signed charge
sectors are those proved in the transfer theorem, not an inference
from a positive real maximum before filling.

All ordinary auxiliary colors, projective normals, paired endpoints
and nonminimal Fourier charges are accounted for by that theorem and
the whole-source gap. There is no prime-level, odd-level, equal-slope
or same-sign restriction. The number of circles and every slope are
fixed before N tends to infinity.

## 4. The actual filled hyperbolic volume

At zero inverse slope the source anchor is

    2pi phi(0)=2max V_E=Vol(S^3 minus L_E),                    (8)

by the complete geometry and its
[corrected closed projection cut](actual_conway_bowtie_projection_cut.md).
The source rate in (7) tends to this actual complete volume as all
|p_i| tend to infinity. For example its quadratic decrease is

    2pi Re S_p(chi_*)
       =2pi phi(0)-sum_i pi^2/[2p_i^2 cot(pi x_(i,*))]
                         +O(||p^(-1)||^3).                   (9)

This follows by inserting
chi_*,i=-i/[2p_i cot(pi x_(i,*))]+O(||p^(-1)||^2)
in (5). Its geometric interpretation uses the full marked construction
below, not merely agreement with the complete cusp Hessian.

The [marked deformation proof](actual_conway_marked_peripheral_deformation.md)
now supplies an actual bounded framed representation near the complete
one, with the original peripheral marking and full action differential. Here U,V are logarithms of
projective similarity multipliers, equivalently squared SL(2,C)
peripheral eigenvalues:

    G=2pi i phi+recorded real constant,
    U_i=-2pi i chi_i,  V_i=-2 partial_i phi.                  (10)

All white and shaded edge words are pointwise identities, every main
cusp stays parabolic, and the auxiliary paths are the primitive disk
meridian and longitude. With the complete regulator anchor, (4) gives

    U_i+p_i V_i=-2pi i

exactly. Unfilled auxiliary cusps also remain parabolic. The existing
general geometric completion theorem therefore applies, and the
absolute regulator identity proves

    lim_N (2pi/N)log|K_(E,N)(p)|=Vol(S^3 minus L_E(p)).       (11)

This uses the actual group representation and every peripheral mark;
it does not infer geometry just from matching open-port cross ratios.

## 5. These fillings do not produce knots

If E contains S robust seeds, it already contains at least 2S internal
main circles. Closing its exposed strands adds at least one more.
Full twists have even endpoint permutation and preserve these
components. The [literal component theorem](actual_conway_full_filling_component_obstruction.md)
therefore gives at least 2S+1 main components after filling every
auxiliary circle.

Consequently (11) is a broad actual LINK volume equality, with arbitrary fixed
branching and turn depth. A new knot theorem needs different source
connectivity, such as suitable retained odd half-twist coupons, with
its own phase and source estimates. The filled-volume identification does not remove that requirement.

The subsequent marked deformation supplies the geometric interface used in the final theorem.

The marked representation, primitive unit filling equation, and absolute regulator establish (11). They are the geometric inputs needed in addition to the quantum argument (1)–(7).

The later [signed half-twist extension](actual_odd_conway_long_filling_volume.md) changes the original leaf connectivity and proves its separately selected source and peripheral geometry. For C(FG) with robust children it gives long-filled knot and link families at arbitrary fixed diagram branching and turn depth. The pure component obstruction in section 5 remains unchanged.
