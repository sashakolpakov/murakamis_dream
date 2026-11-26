### Local rigidity on the retained augmented triangulation

The local uniqueness needed at this endpoint can be proved on the same augmented triangulation. Its auxiliary ends are incomplete, but its tetrahedra are still positive and every developed face triple is distinct. Thus no positive triangulation of the filled manifold is needed here.

Let \(t\) be the number of these tetrahedra and let \(c=R+1\) be the number of original cusps, including the main cusp. In positive quad orders put
\[
 u_j=\log z_j,\qquad v_j=-\log(1-z_j),\qquad
 T_j=\frac{dv_j}{du_j}=\frac{z_j}{1-z_j},\qquad
 \operatorname{Im}T_j>0.
\tag{A2b}
\]
Use the logarithms continued along the original charge path. Their constants need not be small. The edge-rank and peripheral-intersection identities proved in Sections 2--3 of the [marked gluing theorem](general_marked_multicusp_gluing_rigidity.md) are combinatorial statements about this triangulation. They give an isotropic edge-row space of dimension \(t-c\), with symplectic quotient equal to the direct sum of the peripheral homology planes.

Choose the main meridian and, at each auxiliary torus, the original primitive slope \(\sigma_v=\mu_v+p_v\lambda_v\). These are independent modulo the edge rows and pair to zero: each is one nonzero primitive class on a different torus. Append their rows to \(t-c\) independent edge rows. The resulting real matrix \((A\ B)\) satisfies
\[
 \operatorname{rank}(A\ B)=t,\qquad AB^{\mathsf T}=BA^{\mathsf T},
 \qquad J=A+B\operatorname{diag}(T_j).
\tag{A2c}
\]
The Jacobian \(J\) is invertible. Indeed if \(Jx=0\), then \((x,\operatorname{diag}(T_j)x)\) belongs to the complexification of a real Lagrangian space. Its symplectic pairing with its conjugate vanishes, whereas polarization gives, up to the fixed overall sign,
\[
             \sum_j\operatorname{Im}T_j\,|x_j|^2>0
                         \qquad(x\ne0).
\tag{A2d}
\]
This is a contradiction. All dependent edge equations have compatible affine logarithmic constants because the present positive endpoint satisfies them. The proof therefore applies at this incomplete augmented solution, not only at the complete augmented cusp. The implicit-function theorem makes the main meridian logarithm and the auxiliary slope logarithms local coordinates on the shape germ.

This is the whole local decorated representation germ modulo simultaneous conjugation. Normalize one ordered developed triple. Shapes reconstruct face maps by their ordered triples; each edge return fixes two distinct endpoints and has multiplier one, hence is identity. The actual dual two-skeleton then gives a representation of the original augmented group. Conversely, a nearby representation and its selected peripheral flags develop every ideal vertex \(gP_v\) as \(\rho(g)\xi_v\). The distinct triples and quadruples at the endpoint stay distinct nearby, so their cross-ratios recover the shapes and original face maps. These constructions are inverse after the same normalization. Every denominator is a unit at the endpoint, so they remain inverse over local Artin algebras. Faithfulness of the augmented representation and parabolicity of its auxiliary ends are not used.

At the main cusp retain the prescribed eigenvalue and the source \(M^{-1}\) eigenflag. For example, when \(\mu_{12}\ne0\), that flag is represented by \((\mu_{12},M^{-1}-\mu_{11})\), which remains nonzero at the parabolic point. At each auxiliary cusp the retained longitude has distinct eigenvalues. Its eigenspaces therefore split the rank-two module, also over a local Artin algebra, because their difference is a unit. To check strict commutation, choose a local representative of the slope whose residue is the identity. If its projective commutator with the longitude is the scalar \(c_0\), determinants give \(c_0^2=1\), while \(c_0\equiv1\) at the residue point. Since \(c_0+1\) is a unit, \(c_0=1\), also over local Artin rings. This auxiliary scalar normalization does not reset the signs of a separately retained determinant-one group lift. In its eigenbasis a commuting slope matrix is diagonal. A slope eigenvalue ratio of one consequently makes the slope scalar and hence projectively identity.

It follows that imposing the retained equations \(U_v+p_vV_v=-2\pi i\) is exactly imposing the filled-group relations near this endpoint, not merely their eigenvalue consequences. Conversely, a nearby filled representation pulls back to these equations on the continued logarithmic branch; its auxiliary eigenflags are uniquely selected by the longitude branches. Fixing the \(R\) slope coordinates leaves a smooth one-dimensional decorated germ with \(u=\log M\) as coordinate, since the ordered main eigenvalue-ratio logarithm on the source \(M^{-1}\) line is \(-2u\). Its basepoint is the complete filled holonomy already constructed by the positive-cell completion. This proves the required marked geometric meridian germ without changing the triangulation.

When the selected source critical point is nondegenerate, its implicit branch gives holomorphic \(Q_v(M)\) and \(X_e(M)\), retaining (A2). The full ordered reconstruction places this branch in the just-proved filled representation germ, with the same coordinate \(M\) and source eigenflag. Local uniqueness therefore identifies it with that geometric meridian germ. Only the smooth endpoint is used for this filled-group descent; intermediate nonintegral cone charges do not kill their slope words.

Every statement below about a filled geometric longitude retains this original complete/filling anchor. An exponentiated slope equation on a different algebraic branch is insufficient.
