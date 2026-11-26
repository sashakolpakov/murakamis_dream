# Local meridian rigidity from the retained positive augmented cells

This is a bounded replacement for the filled-triangulation import in Appendix M §7 and the geometric-characteristic note §5. It uses the original triangulation already constructed in Appendix F. It does not require a positive ideal triangulation of the filled manifold, Ge's existence theorem, or an external local deformation-rigidity theorem.

## 1. Precisely the available point

Let \(Y\) be the original augmented exterior of a fixed literal all-circle tree, with one main component and \(R\) auxiliary circles. The original ordered cut and apical subdivisions give an ideal triangulation \(\mathcal T\) of \(Y\), with \(c=R+1\) torus vertex links. At the endpoint \(c_{\rm charge}=1\) of Appendix F's positive charge path, all its tetrahedral shapes have positive imaginary part. Every face triple and every tetrahedron's four developed flags are distinct. The edge returns are identity and their continued total angles are \(2\pi\).

These facts hold for the original augmented cells at the filled endpoint, although their auxiliary ends are incomplete. They are explicit in Appendix F, lines 367, 480--497. The topology, including each original primitive basis \((\mu_v,\lambda_v)\), is unchanged. The same appendix, lines 501--558, proves that the endpoint completes to the original smooth filled knot exterior \(Y(\boldsymbol\sigma)\), where
\[
 \sigma_v=\mu_v+p_v\lambda_v,\qquad
 U_v+p_vV_v=-2\pi i,\qquad V_v=2i\tau_v.
\tag{1}
\]
Moreover \(\operatorname{Im}\tau_v<0\), so the auxiliary longitude has two distinct eigenvalues and nonunit eigenvalue ratio \(e^{V_v}\). The main meridian is noncentral parabolic. The complete filled metric identifies the endpoint representation with its geometric holonomy, by the metric completion and universal-development argument, before using any local rigidity assertion.

The required topological row identities are the edge-rank and normal-curve intersection calculations reproduced in `general_marked_multicusp_gluing_rigidity.md`, §2. They concern the same ideal triangulation of \(Y\); completeness of a shape solution is not a hypothesis of those combinatorial identities.

## 2. The positive Jacobian at an incomplete solution

Let \(t\) be the number of tetrahedra. In positive quad orders use
\[
 u_j=\log z_j,\qquad v_j=-\log(1-z_j),\qquad
 T_j=\frac{dv_j}{du_j}=\frac{z_j}{1-z_j},\qquad
 \operatorname{Im}T_j>0.
\tag{2}
\]
All logarithms are the ones continued along the original charge path. Their constants need not be small.

The real edge-row space \(E\) has dimension \(t-c\), is isotropic, and the symplectic quotient \(E^\perp/E\) is the direct sum of the \(c\) peripheral homology planes. The alternating pairing of peripheral rows is the fixed nonzero multiple of their oriented intersection number. Choose on these different tori the main meridian and the original filling slopes \(\sigma_v\). Each is a nonzero primitive class; for \(\sigma_v\) this follows from its coordinates \((1,p_v)\). Their rows are independent modulo \(E\) and pair to zero. Thus \(t-c\) independent edge rows together with these \(c\) peripheral rows form a full-rank real Lagrangian system \((A\ B)\).

Its logarithmic Jacobian is
\[
                    J=A+B\operatorname{diag}(T_j).
\tag{3}
\]
If \(Jx=0\), then \((x,\operatorname{diag}(T_j)x)\) belongs to the complexification of a real Lagrangian space. Its symplectic pairing with its conjugate is zero, whereas polarization gives, up to the fixed sign convention,
\[
            \sum_j\operatorname{Im}T_j\,|x_j|^2>0
                  \quad\text{for }x\ne0.
\tag{4}
\]
Hence \(J\) is invertible. This is exactly the written positive-Jacobian proof, evaluated at the present positive solution, rather than at a complete auxiliary cusp.

The edge equations are affine linear in the logarithmic quad variables. All row dependencies have compatible constants because the present point satisfies every edge equation. Consequently solving the selected independent rows solves all nearby edge equations. No assumption that the auxiliary peripheral logs vanish is used here. The implicit-function theorem proves that the decorated shape germ has dimension \(c\) and that the logarithms of the selected main meridian and auxiliary slopes are local coordinates.

Equivalently one may first use the main meridian and auxiliary longitudes as coordinates. Both sets are primitive one-per-torus systems, so both Jacobians are invertible. The transition between these coordinate systems is invertible; at fixed main meridian its auxiliary block \(\partial(U+pV)/\partial V\) is invertible. Thus the direct slope-row proof also supplies the geometric Schur assertion contemplated in the audit request, without substituting a source Hessian for representation rigidity.

## 3. This chart covers the local representations

The representation/shape inverse uses distinct flags, not peripheral parabolicity. Normalize an ordered developed triple. Given nearby shapes, develop across each face by its unique three-point transformation. An edge-return transformation fixes two distinct developed endpoints and its multiplier is the edge shape product. The edge equation therefore makes it identity. These face generators and edge relations are the dual two-skeleton presentation of the same augmented exterior, so they reconstruct a representation with its recorded peripheral flags.

Conversely, take any nearby representation of \(\pi_1(Y)\) with those peripheral eigenflags and characters. For an ideal vertex represented by a coset \(gP_v\), use \(\rho(g)\xi_v\), where \(\xi_v\) is its selected peripheral flag. This is independent of the coset representative. The complete filled endpoint pulled back to \(Y\) need not be faithful; this causes no problem, since the finitely many developed triples and quadruples used by \(\mathcal T\) are distinct at the endpoint. Their determinants stay units nearby. Taking cross-ratios reconstructs the shapes and the original face transformations. The two constructions are inverse after the same triple normalization.

They also remain inverse over local Artin algebras because every denominator is a unit at the basepoint. Retain the exact chosen meridian eigenvalue, not merely an unspecified invariant flag at the main parabolic. If an off-diagonal entry of that meridian is a unit, its prescribed eigenline is given by \((\mu_{12},M^{-1}-\mu_{11})\). This remains a nonzero holomorphic section when the two eigenvalues coalesce. Auxiliary eigenlines are unique on their selected branches because their longitude eigenvalues are distinct. The locally constant signs of determinant-one lifts are retained.

This proves surjectivity onto the local decorated representation germ modulo simultaneous conjugation, not merely construction of some representations from shapes.

## 4. The slope constraints are the filled group relations

At the endpoint, and on a sufficiently small neighborhood, the original auxiliary longitude remains semisimple with distinct eigenvalues. Its two eigenspaces split the local rank-two module; the eigenvalue difference is a unit, also over local Artin rings. In this eigenbasis every peripheral matrix preserving the selected flag and commuting with the longitude is diagonal. Choose a local slope representative whose residue is the identity. Its projective commutator scalar \(c_0\) has \(c_0^2=1\) by determinants and \(c_0\equiv1\) at the residue point. Thus \(c_0+1\) is a unit and \(c_0=1\), also over Artin rings. This auxiliary scalar normalization does not reset the signs of any separately retained determinant-one group lift. Thus a primitive slope whose eigenvalue ratio is one is scalar, hence identity in \(\mathrm{PGL}_2\).

Conversely, an actual representation of the filled group pulls back to a representation of \(Y\) in which each slope is identity. Its logarithmic slope lies on the retained constant branch \(-2\pi i\). The longitude eigenflag is uniquely determined on the chosen branch; no extra auxiliary decoration remains free.

Therefore imposing the \(R\) equations (1) on the shape/representation chart is exactly imposing the filled-group relations, locally and infinitesimally. It leaves a one-dimensional smooth decorated germ, with \(u=\log M\) as coordinate (the ordered eigenvalue-ratio logarithm on the source \(M^{-1}\) line is \(-2u\), a nonzero constant change). The basepoint is the actual complete filled holonomy. This is the marked geometric meridian germ required in Appendix M, obtained without changing the triangulation.

Only the endpoint \(c_{\rm charge}=1\) is used for group descent. Intermediate nonintegral cone charges need not kill their slope words and are not asserted to be representations of the smooth filled group.

## 5. Identification of the source branch

The source's joint nondegenerate critical point is a separate input, proved by its wire Hessians and successive angular Schur complements. It supplies a holomorphic implicit branch in \(M=e^{\pi i t}\). Its critical equations are precisely the rational edge equations and the original primitive slope equations; the following identities make that bridge explicit. Write \(X=e^{2\pi i x}\), \(Q=e^{i\tau}\), and \(m=M^2\). For the original edge action \(b\) and insertion \(\mathcal K\),
\[
 e^{b_x(x,\tau)}=-\frac{(X+Q)(X+Q^{-1})}{(X-1)^2},\qquad
 e^{\mathcal K_x(x,t)}=
       \frac{(X-1)^2}{(1-Xm)(1-X/m)}.
\tag{5}
\]
Multiplying the two incidence factors and the insertion factor gives the full geometric edge equation. In addition, on the continued local logs,
\[
 -2\pi b_\tau(x,\tau)=\log\frac{Q+X}{1+QX}.
\tag{6}
\]
One verifies (6) by differentiation in \(x\) and the value zero at \(x=0\); the identity then continues to the retained chart. Since \(\mathcal K\) has no angular dependence, the circle stationarity is exactly
\[
 \sum_{e\ni v}\log\rho_{v,e}=in_v\tau_v-2\pi i,
 \qquad
 U_v+p_vV_v=-2\pi i.
\tag{7}
\]
The full ordered generator gluing of the geometric-characteristic note reconstructs the original augmented representation from these equations. At \(M=1\) it is the actual positive filled holonomy by the charge-path anchor. On a neighborhood it belongs to the filled germ just proved and has the prescribed coordinate \(M\). Uniqueness in that germ identifies the source branch with its geometric meridian family.

The exact preferred-longitude word formula is already proved separately by boundary isotropy, the source constant field, regular units, the independent parabolic cusp marking, surgery homology and the Seifert-frame sign. The present lemma supplies its precise geometric-branch interpretation; it does not derive that formula from a cusp tangent or a formal quantum period.

## Scope and imports

The lemma uses: the literal ideal triangulation of the augmented exterior; its positive nondegenerate endpoint and actual complete filling; the combinatorial edge-rank/peripheral-intersection identities; finite-dimensional polarization and the holomorphic implicit-function theorem; the explicit representation/shape inverse; and the already established source reconstruction. It uses no new triangulation of the filled manifold and no general existence theorem for positive triangulations. The integral edge/peripheral row proofs are existing local mathematical inputs, not consequences of finite symbolic tests.
