# Audit: the actual CROSS geometric action on the new general Morse source

31 October 2026. Independent analytical/source audit for the parent proof.
No public or frozen-source edits. The conclusion concerns the existing
CROSS principal action and its actual geometric marking. It does not
restore the full numerator by the older Fejér/flat-forest argument.

## Hypotheses retained

Use the actual augmented link and fixed coupon frames constructed in
`notes/research_matched_sphere_morse_source.md`. Assume its chosen white
triangulation is simplicial and has the same labeled nondegenerate
positive right-angled certificate required by the existing marked-circle
and complete-source theorems. Choose adjacent MAIN faces u,v as the two
protected faces. The CROSS analytic packet and its complete coefficient
anchor are separate analytic inputs; the root reviewer is auditing those
dependencies. An arbitrary multigraph diagonal choice without such a
certificate is not included in this geometric audit.

## 1. The marked pattern has no constant-headcount hypothesis

`notes/actual_marked_deformed_circle_pattern.md`, sections 1–4, uses only
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
event-incidence proof in `notes/actual_augmented_plat_critical_scheme.md`
already permits arbitrary cup/cap/coupon events and arbitrary graph
cycles; its displayed fixed-width wording is not an extra algebraic
hypothesis. The spanning-tree reconstruction of momenta and the inverse
prefix chart depend on the actual event graph, not on all cups being
below all boxes. Alternatively the reflection formulas above construct
the needed representation directly without choosing a magnetic chart.

## 3. Local action, boundary characters, and the absolute anchor

`notes/actual_cross_cofactor_marked_action.md` proves locally that the
actual full-V cofactor action equals the absolutely normalized triangle
action \(Q_b\), including every allowed one-line/two-line specialization.
Its full head gradients retain the physical factor \((bc)^{-d/2}\),
so they give the same ordered product and primitive collar in section 2.
These statements are port-local and unaffected by an outside Morse turn.

The new source compiler proves the original face character exactly on
the new network. Thus its principal stationary action is precisely
\[
 A_\epsilon(\delta)=\operatorname{crit}_{L_{\rm ordinary}}
 \left\{\sum_e(Q_{b_e}+Q_{c_e})
 -\sum_{f\rm\ ordinary}\Log L_f
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
 U_e=-\Log R_{0,e}-\epsilon_e\Log(-J_e),\qquad
 V_e=2\Log(-J_e)=-4\pi i\delta_e,
 \quad \partial_{\delta_e}A_\epsilon=U_e.
\]
Hence \(d(2\pi iA_\epsilon)=-\frac12\sum U_e,dV_e\), exactly the
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

## Verdict

PASS for the general Morse extension of the CROSS geometric action,
actual group sewing, primitive peripheral normalization and absolute
regulator, under the retained certificate and analytic CROSS inputs.
The source extension requires only replacing the fixed-width slice
notation by its actual variable region sequence. No flat-forest source
restoration, generic-q normal, or scalar word-regulator shortcut is used.
Full-numerator restoration must be supplied by the new non-CROSS gap,
not inferred from this audit.
