# The actual mixed source action is the marked geometric regulator

29 October 2026. This gives the regulator comparison needed AFTER an
actual representation/port lift has been established. It retains the
ordinary-circle spin, both preferred peripheral flags, and the exact
filling charge. The comparison is by an elementary differential identity
and the already calibrated complete geometric anchor, rather than by
matching cusp Hessians or naming a source action a volume.

## 1. Inputs and the specific branch under comparison

Fix an odd s>=5 and the selected analytic mixed-source branch near
complete auxiliary colors. The source construction supplies the
holomorphic function Phi_s and its NONZERO amplitude. Put

    z_i=Log H_i, ell_i=Log L_(H_i),
    G(z)=2pi i Phi_s(z/(2i))+C_real,
    partial_(z_i)G=ell_i, G(0) has imaginary part V_s.

Here C_real is the recorded real Cartan/quarter-turn phase constant.
For example the original exp(-is pi(N-1)/4) leading character contributes
s pi^2/2. Such constants are kept in a complex-period equality and do
not change its regulator norm.

The following geometric inputs concern the SAME selected branch,
as established in
[the literal global-port and geometric-anchor theorem](actual_pretzel_port_lift_and_geometric_anchor.md):

1. The literal mixed Hurwitz/quarter-turn port and global source
   equations lift it to representations rho_z of the ACTUAL augmented
   link group, with main meridian fixed complete. The
   [source-selected local lift](actual_pretzel_mixed_regular_character_lift.md)
   supplies its explicit auxiliary C and disk product P; a mere
   trace equation would not replace global port gluing.
2. At z=0 that representation is the positively oriented geometric
   one of the original half-twisted augmented diagram. The explicit
   white-face/port anchor and the absolute auxiliary translations
   C=W(1+ic), P=2icW, rather than just a cusp derivative, fix this
   comparison. The local lift records those matrices in section6;
   the complete geometric volume is V_s.

The statements below use these proved inputs explicitly. Neither
global port gluing nor the absolute anchor is replaced by formal
saddle equations or by a coincident peripheral trace alone.

The [literal mixed longitude certificate](actual_mixed_crossing_circle_preferred_longitude.md)
now fixes the actual preferred eigenvalues on the positive meridian flag:

    M_i=H_i^(-1/2), lambda_i=-L_(H_i)^(-1).

The minus comes from g_j=(-1)^(j-1)K_j and the literal typed loop
[2,1,1,2]. Its disk word has zero self-writhe. There is no additional
lambda->M^k lambda framing change hidden in these coordinates.

## 2. Retain the spin before taking a regulator norm

Continue logarithms from completeness as

    u_i=Log M_i=-z_i/2,
    v_i=Log lambda_i=pi i-ell_i,
    Gbar=G-pi i sum_i z_i.

Then EXACTLY

\[
 d\overline G=2\sum_i v_i\,du_i.                       \tag{1}
\]

Thus the preferred connection is the same one derived directly from
the actual mixed universal crossings. The spin is a specified physical
character, not an identically one change of the source. Its marked norm
is

\[
 \boxed{D_{\rm src}(z)
   =\operatorname{Im}\overline G
                   -2\sum_i\operatorname{Re}u_i\operatorname{Im}v_i
   =\operatorname{Im}G
                   -\sum_i\operatorname{Re}z_i\operatorname{Im}\ell_i.}
                                                               \tag{2}
\]

Indeed Im(Gbar)=ImG-pi sum Re z_i, while
2 Reu_i Imv_i=-pi Re z_i+Re z_i Im ell_i. The central terms cancel
IN THIS PAIRED EXPRESSION. They were not removed from the separate
action or kernel. The squared geometric peripheral logarithms retain
their corresponding 2pi i deck shift.

Writing z_i=x_i+i y_i and ell_i=a_i+i b_i, direct differentiation
gives

\[
 dD_{\rm src}=\sum_i(a_i\,dy_i-x_i\,db_i)
       =2\sum_i(\operatorname{Re}v_i\,d\operatorname{Im}u_i
                         -\operatorname{Re}u_i\,d\operatorname{Im}v_i).
                                                               \tag{3}
\]

This is the actual half-meridian-step factor two. It is not inferred
from a classical polynomial normalization.

## 3. The geometric regulator has the SAME derivative and absolute anchor

For the actual representation rho_z, define beta(rho_z) by a FIXED
finite oriented fundamental triangulation/idealized relative chain
of the augmented-link complement. Decorate each lifted cusp with its
specified peripheral eigenflag and develop its tetrahedra using the
ACTUAL matrices of the port theorem. Internal faces cancel and the
orientation and peripheral marking are those of that same diagram.
This is the topological fundamental-chain construction in
[the actual fundamental-cycle theorem](crossing_fundamental_cycle.md),
not its additional identification of a unipotent five-dilogarithm
COEFFICIENT with the shadow chain. That coefficient identity uses
unipotence and is NOT being extended to semisimple auxiliary meridians.

Use the audited coisotropic boundary pairing of
[the Bloch boundary calculation](bloch_lift_and_boundary_torsor.md),
section2, on this developed chain. For several boundary tori the same
calculation is their direct sum: peripheral rows on distinct tori
have zero intersection pairing, and the meridian/longitude rows on
each torus have the same pairing -2. The resulting identity uses
the group/eigenflag gluing equations, not parabolicity of those
peripheral matrices. In the full squared peripheral coordinates it
is delta beta=-(1/2)sum m_i wedge l_i. Equivalently,

    delta beta=-2 sum_i M_i wedge lambda_i.

Here m_i=M_i^2 and l_i=lambda_i^2; using unsquared coordinates
without their factor two would be incorrect. The main-component
contribution is constant because its meridian is fixed at one.
Work first where the developed shapes are regular. A sufficiently
small neighborhood of the explicitly identified complete anchor has
such a fixed finite chain; any normalized degenerate summands and
their regulator limits are handled by the already proved five-point
chain invariance and continuity. No equality with the transformed
source dilogarithm list is assumed in this definition of beta.

For a shape t, the elementary Bloch--Wigner differential is

    dD(t)=log|t| dArg(1-t)-log|1-t| dArg(t).

Applying it to the displayed boundary identity gives

    dD(beta)=2 sum_i[Re v_i dIm u_i-Re u_i dIm v_i],

which is exactly (3). This is the same calculation as
[the actual preferred action/regulator identity](quantum_longitude_and_regulator_action.md),
sections5--6, and
[its complex peripheral continuation](complex_peripheral_action_and_conversion_bound.md),
section1. Those proofs use local logarithmic identities and face
cancellation, so no assumption of equal component meridians enters.

At the complete anchor, D(beta(rho_0))=V_s=ImG(0) and all Re z_i
are zero. Consequently the two functions with equal differential have
the SAME absolute constant on this connected regular branch:

\[
 \boxed{D_{\rm src}(z)=D(\beta(\rho_z)).}                \tag{4}
\]

Use a simply connected sufficiently small marked parameter
neighborhood. The explicit auxiliary C has a regular noncentral
parabolic limit, so a diagonalizing-frame singularity at completeness
does not invalidate this comparison. The identity extends through
that removable limit. It does not splice distinct character components
at a coincident peripheral point or reset logarithms independently.

This proof needs neither an assumed equality of unmarked primitives
nor a new theorem imported from the literature. Actual port gluing,
preferred peripheral coordinates, and the COMPLETE geometric anchor
are the explicit inputs that prevent an arbitrary additive volume.

## 4. The actual chirp's stationary action is precisely this regulator

For independently signed nonzero fixed fillings and integer charges m_i,
the original full-normal centered Gaussian kernel supplies the holomorphic
action

    W(z)=G(z)+sum_i (z_i-2pi i m_i)^2/(4p_i),
    z_i+2p_i ell_i=2pi i m_i at stationarity.            (5)

All real Cartan constants and the retained normal amplitude can be kept
beside this leading action. At a stationary point the second term in W
is sum p_i ell_i^2. The real part of the stationary equation is
Re z_i=-2p_i Re ell_i, so

\[
 \boxed{\operatorname{Im}W(z_*)
   =\operatorname{Im}G(z_*)
                       +2\sum_i p_i\operatorname{Re}\ell_i
                                           \operatorname{Im}\ell_i
   =D_{\rm src}(z_*)=D(\beta(\rho_{z_*})).}            \tag{6}
\]

In particular there is no unestimated complex endpoint correction left
at the filling saddle. It is canceled by the ACTUAL filling quadratic,
not deleted by replacing a boundary holonomy with a unit value.

The same conclusion matches the source Fourier action used in the
proved whole-source asymptotic. If zeta denotes its frequency variable,

    ell_i=-2pi i zeta_i,
    z_i=2i chi_i,
    A=Phi_s(chi)+2i sum chi_i zeta_i
                     -2pi i sum(p_i zeta_i^2+m_i zeta_i).

At its critical point direct substitution gives

    2pi i A=G+sum p_i ell_i^2

up to the already recorded REAL Cartan constants. Therefore

    2pi Re A=Im W=D(beta(rho_(z_*))).                   (7)

This checks the source normalization rather than identifying exponents
only up to an unknown scalar or a factor of two.

## 5. The actual filled slope and the remaining geometric distinction

The preferred-spin relation gives

    M_i lambda_i^(p_i)=(-1)^(p_i+m_i).

At the selected long-filling point these peripheral matrices are
regular semisimple, not nontrivial unipotents with an accidentally
unit eigenvalue. Indeed the local all-unit charge saddle has every
color coordinate nonzero; the separately even analytic source has
nonzero linear longitude derivative there. Both coordinates remain
in a small neighborhood of zero, so their distinct reciprocal
eigenvalues cannot acquire a nonzero full period. The explicit C
and P commute and use the specified COMMON eigenflag. Thus their
matrix product C_i P_i^(p_i) is the displayed scalar +/-I.

Hence the PSL2 representation kills the primitive disk-framed slope
mu_i+p_i lambda_i and extends over the corresponding filled manifold.
The central sign is not assumed to be +I in a preassigned SL2 lift.
The representation-volume straightening and smearing proofs use only
the actual PSL2 isometric action, so they apply to this descended
representation directly.
The original retained negative half twist belongs to the base meridian;
it was not replaced by a p_i+1 slope. In the geometric cusp anchor that
base meridian is the primitive positive diagonal, not just its length.

Here is a compatible FINITE-chain proof of invariance under the
filling. It is not enough to put only the new vertices at one ideal
flag while leaving unrelated old boundary data unchanged. At a filled
cusp the peripheral image is cyclic and preserves a target geodesic
axis. First replace the OLD augmented ideal-cusp development by the
axis-valued cusp map of
[the general-peripheral volume proof](general_peripheral_representation_volume_bound.md),
sections1--2. Its explicit face-compatible conical comparison (4a)
and homotopy have boundary volume O(Y^(-2)) in (4b). Hence this
replacement preserves the absolutely normalized AUGMENTED regulator
as the cutoff Y tends to infinity; it is not an assumed zero-volume
homotopy on an arbitrary old boundary.

Fix a finite cusp cutoff and a common finite triangulation on its
boundary. The OLD boundary map is now on the preserved axis. Because
the filling slope is killed, its equivariant vertex assignment factors
through the solid torus group Z. Extend the SAME boundary assignment
to the new solid-torus vertices equivariantly on that axis. Axis
contractibility provides the face-compatible extension, and every new
straight tetrahedron is collinear and has zero volume. Thus the
finite compact CORE PLUS FILLING chain computes the filled
representation volume with no new contribution. The unfilled main
cusp retains its original parabolic end convention.

Taking Y to infinity, the controlled old-cusp comparison proves that
the value in (6) is the regulator of the EXTENDED filled representation,
with the same orientation, primitive marking, and absolute constant.

It follows, using the independently proved representation-volume bound,
that the selected source exponent is at most the filled manifold's
hyperbolic volume whenever that manifold is hyperbolic. To replace this
upper bound by EQUALITY one must additionally prove that this extended
representation is its positive geometric Dehn-filling representation.
A correctly glued positive near-complete geometric deformation with
primitive 2pi filling supplies that fact; it is not inferred merely
from (4) or a cusp Hessian. The present note does not substitute for
that geometric extension proof.

[Audit](../experiments/audit_actual_mixed_crossing_circle_preferred_longitude.py)
includes exact symbolic checks of (2),(6), alongside the original
mixed-R/pivot/framing certificate. The representation lift and absolute
anchor are separately checked geometric inputs, not consequences of
those elementary scalar checks.
