# Adversarial audit of the source-volume Casson--Rivin argument

29 October 2026. Independent analytical review. The claimed filled-volume
identification is not circular on the proved source family, but it uses
several substantial inputs BEFORE strict concavity. This note separates
them and distinguishes the two volumes in the user's question.

## 1. The two volumes must remain distinct

The notation \(V_s\) is the volume of the COMPLETE AUGMENTED base,
with its crossing-circle cusps UNFILLED. The source limit for the
actual filled link is

\[
 V_{\rm src,s}(\boldsymbol p)=2\pi\operatorname{Re}\mathcal A_s(\boldsymbol p).
\]

The whole-source theorem establishes this number as the original quantum
limit before asserting geometric equality. It is not set equal to \(V_s\).
Indeed [local charge selection](actual_pretzel_long_filling_charge_selection.md),
sections 2--3, gives a strict source action drop for every sufficiently
long finite tuple:

\[
 V_{\rm src,s}(\boldsymbol p)<V_s,\qquad
 V_{\rm src,s}(\boldsymbol p)\longrightarrow V_s
       \quad\text{as }\max_i|p_i|^{-1}\longrightarrow0 .
 \tag{1}
\]

The derivative estimate there, equation (8), proves the strict inequality;
it is stronger than an expansion with an unquantified remainder. For
orientation, its quadratic formula (11) reads

\[
 V_{\rm src,s}(\boldsymbol p)=V_s-
       2\pi^2\operatorname{Im}\tau_s
               \sum_i|1+2p_i\tau_s|^{-2}
       +O_s(\|\boldsymbol p^{-1}\|^4).
 \tag{2}
\]

This is only a local expansion. Equality with the ACTUAL filled
hyperbolic volume requires the further geometric argument below.

## 2. What proves the source has a positive interior angle point

The dependencies in
[the Casson--Rivin note](actual_long_pretzel_casson_rivin_equality.md)
are:

1. **Original source selection, not formal gluing.** Its section 1
   invokes [whole-source survival](actual_long_pretzel_full_source_survival.md),
   sections 1--2. This establishes the exact original invariant's
   nonzero full-sequence asymptotic and hence its rate \(V_{\rm src}\).
   The color complement, all aliases, original normal terms, endpoint
   currents and noncancellation are analytic premises. Concavity does
   not prove them.
2. **An actual marked representation near a known geometric point.**
   [The literal port theorem](actual_pretzel_port_lift_and_geometric_anchor.md),
   sections 1--6, supplies the source-selected \(\rho_z\), its cap order,
   preferred peripheral words, and the COMPLETE geometric anchor
   \(\rho_0\). This uses the explicit augmented geometry. It does not
   assume that a filled \(\rho_{\boldsymbol p}\) is geometric.
3. **A positive chart at the COMPLETE base.** Casson--Rivin section 2
   chooses a fixed positive geometric ideal triangulation of that
   complete manifold. The CURRENT class-specific input is
   [the direct positive ideal-angle certificate](actual_pretzel_positive_ideal_angle_certificate.md),
   sections 1--3: exact homogeneous lifts of the actual polyhedra,
   all original white/shaded half-twist face maps, and finite
   compatible affine subdivision give this triangulation directly.
   Its section 4 also checks the full edge/peripheral tangent rank.
   The former [Ge audit](ge_geometric_triangulation_audit.md),
   sections 1--3, conditional on Epstein--Penner, remains an
   alternative route; it is no longer a dependency for this actual
   class. The direct proof asserts no universal all-ideal existence
   theorem for an arbitrary augmented base, and is not itself a
   quantum source-selection theorem.
4. **Continuity, not an assumed maximizer.** Equivariantly move those
   finitely many ideal vertices using the selected peripheral flags.
   They vary continuously from the complete noncentral parabolic
   flags. Cross-ratios stay in the upper half-plane in one fixed
   neighborhood. Exact representation relations give the complex
   edge equations; their angular lifts remain \(2\pi\).
   The source's inverse-slope implicit-function argument puts every
   sufficiently long independently signed tuple in that neighborhood.
   It follows that the actual source point is in the RELATIVE
   INTERIOR of the prescribed affine angle slice.

Thus the interior critical point is not obtained from the statement
“a concave functional has a maximum.” It is supplied by an actual
source-selected representation which is a small deformation of an
independently identified positive complete geometry. None of these
steps assumes the desired filled-volume equality.

The alternative
[finite-center core construction](actual_long_pretzel_geometric_filling_completion.md),
sections 2--5, and the
[general equivariant averaging construction](general_source_regulator_hyperbolic_equality.md),
sections 2--5, prove the geometric completion without requiring the
all-ideal triangulation input. They are sufficient for final equality
even when one does not use the Casson--Rivin angle presentation.

## 3. The constrained functional is concave and uses FILLED slopes

The actual domain in Casson--Rivin section 3 is the positive angle
polytope with tetrahedral sums \(\pi\), edge sums \(2\pi\), and

\[
 \operatorname{Im}(U_i+p_iV_i)=-2\pi,\qquad
 U_i=-z_i,\quad V_i=-2\ell_i ,
 \tag{3}
\]

on each filled auxiliary cusp. The logarithms are the SMALL centered
PROJECTIVE logs. An old SL longitude sign is not added as a further
geometric rotation. A remaining main cusp has its chosen meridian
angle zero; the source representation in fact has both its peripheral
logs zero. With two main components, the corresponding conditions are
imposed on BOTH unfilled cusps.

Equation (3) is the all-positive unit charge convention. The other
minimal charge signs use their corresponding eigenflag marks.
The existence/noncancellation of the selected contribution was already
proved in the quantum source theorem.

For tetrahedral angles \(\alpha+\beta+\gamma=\pi\), let

\[
 \mathcal V(\theta)=\sum_t
       [\Lambda(\alpha_t)+\Lambda(\beta_t)+\Lambda(\gamma_t)].
\]

In the two free angles its negative Hessian is

\[
 \begin{pmatrix}
 \cot\alpha+\cot\beta&\cot\beta\\
 \cot\beta&\cot\gamma+\cot\beta
 \end{pmatrix}.
 \tag{4}
\]

Its determinant is \(1\), and its first diagonal entry is
\(\sin\gamma/(\sin\alpha\sin\beta)>0\). Therefore the functional is
STRICTLY CONCAVE, not convex, on every affine positive-angle slice.

Maximizing on the old UNFILLED completeness slice would concern
\(V_s\) and would not prove the filled claim. The large signed
integers \(p_i\) belong in the actual affine constraints (3).

## 4. Why stationarity holds for all angle tangents

Casson--Rivin section 4 correctly uses the coisotropic edge reduction,
not a derivative only along the much smaller representation variety.
For \(x=\Log z,\ y=\Log z''\), direct sine-rule differentiation gives

\[
 d\mathcal V(\delta\theta)
        =\sum_t(\operatorname{Re}x_t\,\delta\gamma_t
                       -\operatorname{Re}y_t\,\delta\alpha_t).
\]

The REAL log vector of a complex gluing solution and EVERY tangent
obeying the homogeneous edge-angle constraints lie in the edge
coisotropic space. The audited boundary pairing, independently on
each boundary torus, consequently gives

\[
 d\mathcal V(\delta\theta)=\frac12\sum_i
       [\operatorname{Re}V_i\,\delta\operatorname{Im}U_i
             -\operatorname{Re}U_i\,\delta\operatorname{Im}V_i].
 \tag{5}
\]

There are no cross-torus intersection terms. At the source point the
REAL part of its actual filling equation is
\(\operatorname{Re}U_i+p_i\operatorname{Re}V_i=0\).
Each term of (5) is therefore

\[
 \tfrac12\operatorname{Re}V_i\,
                \delta\operatorname{Im}(U_i+p_iV_i)=0 .
\]

Unfilled cusp terms vanish because both actual logs are zero.
This proves the full KKT criticality on the affine slice, including
variations not arising from nearby complete gluing solutions.
Strict concavity then makes the source point the unique global
maximizer, including comparison with the boundary by continuity.

## 5. Absolute calibration, boundary correction, and smooth completion

The source-to-volume equality is not fixed by a cusp Hessian alone.
[The marked regulator proof](actual_pretzel_marked_regulator_and_filling_action.md),
sections 1--4, uses the SAME group representation, eigenflags,
preferred longitude and COMPLETE anchor to prove

\[
 D_{\rm src}
     =\operatorname{Im}G-\sum_i\operatorname{Re}z_i
                                         \operatorname{Im}\ell_i
     =D(\beta(\rho_z)).
 \tag{6}
\]

Its section 3 defines \(\beta\) by an actual decorated fundamental
chain, not an unproved extension of a unipotent coefficient identity.
The literal spin \(\lambda=-L_H^{-1}\) is retained before the paired
norm. Its exact filling term is

\[
 W=G+\sum_i(z_i-2\pi i m_i)^2/(4p_i).
\]

At stationarity \(\operatorname{Re}z_i=-2p_i\operatorname{Re}\ell_i\),
so \(\operatorname{Im}W=D_{\rm src}\). Thus no unestimated complex
endpoint term is suppressed when passing from the source action to
the volume functional.

Finally Casson--Rivin section 6 invokes independently proved smooth
completion. The
[primitive log theorem](actual_long_pretzel_primitive_filling_angle.md),
sections 2--5, identifies the actual log-link periods BEFORE multiplying
by a large slope. The selected slope period is exactly \(2\pi\) in
absolute angular value, not merely scalar PSL holonomy and not a
\(4\pi\) branched fill. The
[compact log-link and tube proof](long_pretzel_equality_critical_audit.md),
sections 2--5, gives the full tube and degree-one complete filling;
the unfilled cusp or cusps remain complete.

Therefore the regulator value is the volume of a genuine positive
complete hyperbolic metric on the ACTUAL filled topology. Comparing
it to a specified hyperbolic metric via the independently proved
representation-volume inequality in both directions identifies their
volumes without assuming a separate equality-rigidity theorem.

The dependency chain is

\[
 \text{whole source rate}\ \longrightarrow\
 \text{actual marked }\rho_{\boldsymbol p}\ \longrightarrow\
 \text{positive interior angle point and filled-slope KKT}
 \ \longrightarrow\ \max\mathcal V=V_{\rm src}
 \ \longrightarrow\ \text{smooth complete filled volume}.
 \tag{7}
\]

No arrow is justified solely by the previous maximum's numerical
value. In particular neither a KKT equation without the positive
chart/primitive logs nor strict concavity without a verified source
point proves the assertion.

## 6. Current exact quantum scope

The old Casson--Rivin and survival bodies state odd \(s\geq25\).
The subsequent
[width extension](actual_pretzel_all_width_extension.md), sections 5--6,
supplies the missing whole-color gap for every fixed odd \(s\geq9\).
Section 8 of that note separately verifies the parity-independent
source and normalization and gives the ORIGINAL single-cut reduced
two-component link theorem at every fixed even \(s\geq10\).
For even width both unfilled main cusps remain parabolic and complete;
the boundary-pairing and completion arguments are their direct sum.
The even-link statement is not obtained by calling a link a knot or
modifying each component separately.

In both cases all \(|p_i|\) are independently sufficiently large FIXED
integers. Their signs and ratios are unrestricted. The common
threshold may depend on the fixed width, and can be enlarged once to
enter the fixed positive geometric neighborhood. Neither width nor
slopes grow with the quantum level \(N\); both level parities and
composite levels remain included. Widths \(3,5,7\) and even \(4,6,8\)
are not supplied by this current global source estimate.

The general geometric certificate applies far beyond pretzels, but
the actual quantum source survival is not thereby established for
arbitrary graphs or all hyperbolic knots.

**Verdict:** the proved-family equality is noncircular with these
dependencies. Casson--Rivin is a valid concave variational
characterization of the already source-selected point; it is not a
substitute for the source-selection and geometric-existence inputs.
No new computation was used in this audit.
