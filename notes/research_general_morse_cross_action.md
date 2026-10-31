# The actual CROSS geometric action on a general Morse source

31 October 2026. Independent analytical/source extension. The conclusion concerns the existing
CROSS principal action, actual geometric marking, local packet, and global spectral gap. It does not
restore the full numerator by the older Fejér/flat-forest argument.

## Hypotheses retained

Use the actual augmented link and fixed coupon frames constructed in
[general Morse source realization](research_matched_sphere_morse_source.md). Assume its chosen white
triangulation is simplicial and has the same labeled nondegenerate
positive right-angled certificate required by the existing marked-circle
and complete-source theorems. Choose adjacent MAIN faces u,v as the two
protected faces. The original local cofactor estimates and complete
coefficient anchor are the analytic inputs; section 4 checks their
shared-source assembly independently of full-numerator restoration.
An arbitrary multigraph diagonal choice without such a
certificate is not included in this geometric audit.

## 1. The marked pattern has no constant-headcount hypothesis

[marked deformed circle pattern](actual_marked_deformed_circle_pattern.md), sections 1–4, uses only
the labeled simplicial sphere, its MAIN/matching edge types, the two
adjacent protected lines, and the positive finite-face Hessian. Its
equations for finite centers/radii and signed line sides are unchanged.
The rank proof deletes the two triangles incident to uv and propagates
one infinitesimal motion through the remaining triangulated disk. It
does not use the flat-plat gap forest or the placement of cups/caps.
Thus the same common analytic line-circle family realizes the stationary
CROSS radii in the new diagram, including the common strip at the two
protected triangles. All local selected eigenlines are retained.

## 2. Variable-headcount group sewing is literal

At a regular horizontal level of the new Morse diagram let
\(F_0,\ldots,F_{m(t)}\) be the actual region sequence from left to right.
Here \(m(t)\) varies at extrema and is even; the exterior regions are
\(F_0=F_{m(t)}=u\). With the same globally defined white reflections as
the existing complete-core proof, set
\[
 Q_j=R_{F_j}^+R_u^-,\qquad
 H_j=R_{F_j}^+R_{F_{j-1}}^-.
\]
Since \(R_f^-R_f^+=I\), one has exactly
\(H_j\cdots H_1=Q_j\). Inserting or deleting a cup/cap replaces one
region occurrence F by F,G,F. Its two heads multiply to
\(R_F^+R_G^-R_G^+R_F^-=I\). Every prefix after the pair is unchanged.
Every unchanged physical wire retains its two ordered adjacent faces,
so it retains its based head. No independent frame is introduced at a
new level or at a change in the number of heads.

At a coupon its exterior regions are unchanged; the two-head product
is the same original \(P\) before and after it. The already proved
primitive collar \(C\), in that fixed local frame, transports the
ordered pair and commutes with \(P\). The local formula
\[
 M=mR_0(J^{-1}-1)^{-\epsilon}
       C^{-1}(P^{-1}-I)^\epsilon,
 \qquad \det M=m^2R_0(-J)^\epsilon
\]
therefore has exactly the same selected eigenvalue and threading word.
No term in it depends on \(m(t)\). The original disk-framed longitude,
half-twist shear, and the unit at \(J=-1\) are unchanged.

These are all the van Kampen relations of this newly constructed link:
identity wires, cups/caps, and each original crossing-disk box. The
event-incidence proof in [actual Morse critical scheme](actual_augmented_plat_critical_scheme.md)
already permits arbitrary cup/cap/coupon events and arbitrary graph
cycles; its displayed fixed-width wording is not an extra algebraic
hypothesis. The spanning-tree reconstruction of momenta and the inverse
prefix chart depend on the actual event graph, not on all cups being
below all boxes. Alternatively the reflection formulas above construct
the needed representation directly without choosing a magnetic chart.

## 3. Local action, boundary characters, and the absolute anchor

[absolutely normalized cofactor action](actual_cross_cofactor_marked_action.md) proves locally that the
actual full-V cofactor action equals the absolutely normalized triangle
action \(Q_b\), including every allowed one-line/two-line specialization.
Its full head gradients retain the physical factor \((bc)^{-d/2}\),
so they give the same ordered product and primitive collar in section 2.
These statements are port-local and unaffected by an outside Morse turn.

The new source compiler proves the original face character exactly on
the new network. Thus its principal stationary action is precisely
\[
 A_\epsilon(\delta)=\operatorname{crit}_{L_{\mathrm{ordinary}}}
 \left\{\sum_e(Q_{b_e}+Q_{c_e})
 -\sum_{f\ \mathrm{ordinary}}\operatorname{Log} L_f
 +\pi i\sum_e\epsilon_e\delta_e^2\right\}.
\]
No additional delta-dependent turn term appears: the four original
turns have already combined by the general face-winding identity into
the displayed ordinary target. The unrestricted mark was restricted
only after whole-source degree conservation, as in the finite theorem.
Spectral-independent framing and parity characters remain outside this
principal action, with their original values.

The primitive collar and selected longitude give, in the existing
conventions,
\[
 J_e=-e^{-2\pi i\delta_e},\qquad
 U_e=-\operatorname{Log} R_{0,e}-\epsilon_e\operatorname{Log}(-J_e),\qquad
 V_e=2\operatorname{Log}(-J_e)=-4\pi i\delta_e,
 \quad \partial_{\delta_e}A_\epsilon=U_e.
\]
Hence \(d(2\pi iA_\epsilon)=-\frac12\sum U_e\,dV_e\), exactly the
same longitude polarization. The complete positive coefficient anchor
is \(2\pi\Re A_\epsilon(0)=\operatorname{Vol}(Y)\), with the actual
two-ball geometry. This anchor and the actual marked geometric germ
give the existing absolute regulator formula
\[
 2\pi\Re A_\epsilon(\delta)
   =\operatorname{Vol}(\rho_\delta)
      -\frac12\sum_e\Im U_e\Re V_e.
\]
The geometric germ is identified by the same positive marked gluing
rigidity, which depends on the complete hyperbolic certificate and
peripheral marking, not on a constant number of heads.

Finally the exact local Fourier functional of the new source has
\(n_e=\epsilon_e-2p_e\). Its charge phase therefore gives
\(U_e+p_eV_e=-2\pi i\ell_e\), without another half-twist contribution.
At the original unit charge the already calibrated primitive smooth
filling equation and critical-value regulator equality are unchanged.
This is an identification of the geometric action and marking, not a
statement that a charge contributes or that its complement is small.

## 4. The CROSS local packet and global spectral gap

The following dependency extension concerns the **all-CROSS** coefficient.
It does not use section 4 of the older full-numerator packet theorem,
whose restoration argument had separate hypotheses. The graph and its
Morse presentation are fixed before the level tends to infinity.

Write \(C_N^{\mathrm{raw}}\) for the original all-CROSS marked coefficient,
including its sign \((-1)^{dR}\), where \(d=N-1\). The new source has
\(R+2\) faces and exactly \(R\) original degree-\(d\) ordinary targets.
Simplicity and the protected MAIN edge imply that no matching edge has
both protected endpoints. Hence every local outer sum \(x+y\) is
positive. The remaining zero patterns, including a one-variable triangle,
are precisely those already treated in the actual local cofactor proofs.

The [local interpolant rigidity theorem](actual_cross_cofactor_interpolant_rigidity.md)
and its [exactly anchored interpolation](actual_positive_face_exponential_fold_interpolation.md)
therefore apply to every unchanged local polynomial:
\[
 P_{\mathrm{cross},e}
   =N^2\mathcal B_{e,N}
       \bigl(1+O(e^{-\kappa N})\bigr).                 \tag{1}
\]
This is uniform on a fixed small complex spectral and face neighborhood.
The original maximal-fold anchor, beta factors, forced products,
half-index, and even/odd central formulas are retained. These theorems
are local finite recurrences and interpolation statements; they have
no hypothesis about the number or order of global Morse events.

For the shared angular complement, deleting the two marked vertices
from a simple triangulated sphere leaves a connected ordinary graph.
The elementary link-rerouting argument in the
[original rank theorem](actual_original_boundary_transverse_rank.md)
proves this without a flat-plat assumption. Every surviving edge lies
in an actual triangle with two nonzero face variables. The
[global cofactor angular theorem](actual_cross_cofactor_global_angular_gap.md)
then detects every nonconstant ordinary phase. A one-variable triangle
is retained as a monomial and contributes no false angular constraint.
All other cofactors have their global polynomial endpoint majorant;
the exact central sums cost only polynomial factors. After fixing one
ordinary phase, the common-phase point is the only angular zero.
The active edge rows are primitive \(+1,-1\) differences, so no
additional angular alias is introduced.

The [positive coefficient saddle theorem](actual_positive_face_coefficient_saddle.md),
sections 2–4, uses this same ordinary graph, the exact determinant
pair-trace bounds, and the complete circle angle-force equation. Its
face Hessian is positive definite on the \(R-1\) dimensional common-scale
quotient. The complete exponent is
\(\Phi=\operatorname{Vol}(Y)/(2\pi)\), with the exact source anchor.
No flat gap forest or constant intermediate headcount enters that proof.

Define the finite phase on that original quotient by
\[
 \Psi_N(z,\delta)=\frac1N\sum_e\operatorname{Log}
       \mathcal B_{e,N}(\delta_e;L(z))
     -\frac dN\sum_{f\ \mathrm{ordinary}}\operatorname{Log}L_f(z).
 \tag{2}
\]
Uniform local convergence and the positive complete Hessian give its
holomorphic saddle, critical value \(A_N\), and face Hessian \(H_N\).
The new finite compiler gives exactly the original Cauchy measure;
the simultaneous phase integrates to one, leaving
\((2\pi)^{-(R-1)}d\theta\). Deforming that actual torus in its annulus,
with local side faces in the angular gap, gives
\[
 C_N^{\mathrm{raw}}(\delta)=
 \frac{(-1)^{dR}N^{2R}e^{NA_N(\delta)}}
 {(2\pi N)^{(R-1)/2}\sqrt{\det H_N(\delta)}}
 \bigl(1+O(N^{-1})\bigr).                            \tag{H1}
\]
This repeats only sections 1–3 of the
[original shared packet proof](general_full_spectral_numerator_geometric_packet.md).
All finite normalization factors remain in (2), and the determinant
branch is continued from the positive real Hessian. The estimate is
relative on one fixed complex polydisk and controls all fixed derivatives
on smaller polydisks. It has a nonzero actual source amplitude.

The finite actions are separately even and real on the real chart.
Their limit is the untwisted action \(A_0\) of sections 1–3, with
\[
 A_0(0)=\Phi,\qquad
 A_0''(0)=-2\operatorname{diag}(C_e),\qquad
 C_e=\frac{\pi(T_{b_e}+T_{c_e})}{x_e+y_e}>0.           \tag{3}
\]
At least one triangle at every port is nonmonomial: either both
outers are positive, or one protected outer leaves at least one
positive middle. Thus (3) is strict at every port. Shrinking the fixed
chart gives the uniform negative real Hessian required by the spectral
Gaussian argument. Half twists are added only through the original
\(n=\epsilon-2p\) functional, as in section 3 above.

For the global spectral bound, sections 1–3 of the
[global CROSS theorem](actual_global_cross_spectral_gap.md)
use the signed normalized transfer, all starting rows, and a uniform
upper bound on the original unused logarithmic products. Their local
upper action is
\(\max\{Q_b(\delta),\tfrac12\log b\}\), omitting the second branch
when \(b=0\). It decreases strictly away from \(\delta=0\) except for
the stated exact monomial. Every separated spectral port therefore
has a strict loss in the product of its two triangle cofactors.
The even/odd central sums keep both triangles in each term.

Outside the common ordinary phase neighborhood, the global cofactor
angular bound supplies a gap uniformly for all real spectra. Inside
that neighborhood, the signed transfer proof supplies its fixed complex
face extension: one separated port gives a strict loss, while all
others stay below their endpoint rates plus arbitrarily small errors.
The graph has finitely many ports, so choose the errors and strip
small enough that their total is less than that loss. This gives,
for every \(\eta>0\), some \(\tau,\gamma>0\) such that
\[
 |C_N^{\mathrm{raw}}(\delta)|\le e^{N(\Phi-\gamma)}
 \quad\text{if}\quad
 \max_e|\operatorname{Re}\delta_e|\ge\eta,
 \qquad |\operatorname{Im}\delta_e|\le\tau,            \tag{H2}
\]
on the centered real cube for all sufficiently large \(N\).
Every fixed derivative has the same strict rate on a smaller strip.
This is the shared Cauchy sewing of the global CROSS theorem, with
one set of face radii and the original targets throughout.

Thus H1 and H2 extend to the new certified simple-white general Morse
source. Constants depend on the fixed graph, complete radii, and zero
patterns; no prescribed flat-plat width is required. For a full-source
filling conclusion, the **new** global non-CROSS gap must restore the
full numerator. No old Fejér smoothing, pure-middle forest, or flat
full-packet restoration was used here.

## Verdict

The extension retains the original positive certificate and local analytic hypotheses. It supplies the general Morse action and the two stated spectral estimates. Restoring the full source requires the new non-CROSS gap, rather than the earlier flat-forest argument.

The unchanged local collar and global regulator inputs are the
[primitive collar](actual_deformed_circle_primitive_collar.md),
[complete-core group and regulator assembly](actual_complete_core_geometric_deformation.md),
[marked gluing rigidity](general_marked_multicusp_gluing_rigidity.md), and
[peripheral action boundary correction](complex_peripheral_action_and_conversion_bound.md). This dependency extension does not assert full-numerator restoration or a global period bound for the full source.