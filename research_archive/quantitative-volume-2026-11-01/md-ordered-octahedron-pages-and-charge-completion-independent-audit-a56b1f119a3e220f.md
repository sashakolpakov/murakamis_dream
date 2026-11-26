# Independent check of ordered octahedral pages and charge-path completion

1 November 2026. This is a read-only mathematical audit of the actual ordered cut, its peripheral marking, and the ensuing geometric completion. No repository or publication files were changed.

The checked drafts are:

- `/private/tmp/md-all-circle-ordered-octahedron-page-decomposition.md`, SHA256 `9932021d795d4955b2ac6e556e50f1d08cd525a30db00217babdb94cc778dd18`.
- `/private/tmp/md-angular-edge-block-charge-path-completion.md`, SHA256 `913e44b8d07b89e02ddf8496e7a9b9579c8b184d3d5f1dedeeeb4711d4af6a53`.
- `/private/tmp/md-two-octahedron-angular-edge-block.md`, SHA256 `a87b5b2f1ff39bff15bb2ac6f3ec90ebe3d047e82778d7a660f85c49e1c0d57a`.

The last draft already has the separate full local audit `/private/tmp/md-two-octahedron-angular-edge-block-independent-audit.md`, SHA256 `f563e9e8789492b321e18011a1ffd1819b3facf0254c401ce2da9c3900a27072`. The present audit additionally reread the original bowtie cut, the actual closed-turn collar moves, and the marked leaf words.

## 1. The physical root and the local frames

The original root adapter is a physical closed-collar isotopy:
\[
 C((TP_0)T(E))\simeq C(P_0T^2(E))=C(P_0\tau(E)).
\]
Here \(\tau\) is the actual planar half-turn. It reverses product order and transports all children, their four endpoint labels, their disk sides and their marks. The proof does not replace it by the identity merely because the complete source turn squares to the identity. The cited closed-turn isotopy uses the original empty four-arc gluing collar; it applies to the actual tangle balls, including their auxiliary circles.

At a local junction, the exact physical inverse relation is \(P_v=T^{-1}h_v\). If \(h_v\) has ordered endpoints \((v_0,v_1,v_2,v_3)\), then \(P_v\) has endpoints \((v_3,v_0,v_1,v_2)\). This is the correct tuple for the subsequent insertion argument. It avoids using an involutive turn on an arbitrary physical child.

The final draft also retains a circle operator in the middle of its two ordered child lists. This matters: cyclicity is available only at a closed root. The two-sided insertion construction below proves coverage without commuting an internal circle past arbitrary children.

## 2. Direct check of both terminal substitutions

The original stack rule joins the lower factor's endpoint 2 to the upper factor's endpoint 1, and lower 3 to upper 0.

For insertion immediately after \(P_v\), these are precisely
\[
 v_1-w_1,\qquad v_2-w_0.
\]
The new output endpoints \(w_2,w_3\) take over the previous external matches of \(v_1,v_2\). This gives the draft's (5) for arbitrary external partners \(x_1,x_2\); those partners need not belong to one unrotated child leaf.

For insertion immediately before \(P_v\), the same stack rule gives
\[
 w_2-v_0,\qquad w_3-v_3.
\]
The new input endpoints \(w_0,w_1\) inherit the old external matches of \(v_3,v_0\), respectively. This is exactly (7a). Both substitutions follow from the physical endpoint tuples, with no polynomial or scalar identity.

For the right insertion, the old shaded face is \((O_v,C,B)\). The new octahedron has equator \((A,B,C,D)\); its attaching face \((O_v,B,C)\) has the opposite orientation. The three remaining shaded faces are
\[
 (O_v,D,A),\quad(O_w,D,C),\quad(O_w,B,A).
\]
They are exactly the replaced \(v\) face and the two new \(w\) faces after the stack substitution. At the attaching face's vertices, removing its shaded sectors and concatenating the remaining sectors gives the literal planar ribbon order. The adjacent white pieces therefore merge into the original white facial walks. This verifies the full colored boundary identification, beyond the numerical face count.

The left insertion performs the same construction on the other original shaded face. Applying a genuine child-ball rotation to the entire local picture transports this verification, including projection-copy labels; it does not require fixing the rotated child tangle pointwise.

## 3. Coverage and the actual quotient

At each junction, insert children to the right in reverse final order, always immediately next to the circle operator. Insert children on the left in their final order, again next to the circle operator. These two procedures construct the prescribed final lists exactly. Descendant insertions occur within the already placed child ball. A retained quarter-turn, half-turn or input/output reversal carries all of those insertions with the ball. Thus the induction covers the original ordered fully circled tree, including unary chains and a circle operator between nonempty child lists.

Choose a terminal vertex as the root by the actual closed-collar moves, and start with its unique edge. This prevents an existing child from occupying the middle of a list that is to be built by insertion; all subsequent left and right lists start empty. Starting with this genuine two-circle edge block, each step adds one octahedral ball along one triangular disk in each projection copy. Consequently the projection copies remain balls, with exactly \(E\) octahedra and \(E-1\) attachments. The remaining shaded count \(4E-2(E-1)=2(E+1)\) is consistent, but the stronger content is the preceding identification of every shaded sector and every white cycle.

The original reversible projection/disk cut identifies the resulting boundary spheres and all their white and disk-face pairings with those of the actual link exterior. Extending the label-preserving boundary maps over the balls therefore gives the actual exterior. No open quadrilateral is being misidentified with a physical four-punctured sphere, and no equality of source values or volumes is used for topology.

## 4. The pages, the original paths, and the half twist

An added triangular interface and its partner in the other projection copy form the two triangles of a disk-side pair of pants. Its three ends are the same original auxiliary circle and its two actual main punctures. The insertion order supplies the consecutive pages at that circle. The corresponding cusp torus is divided into annular sectors, one per incident edge block.

The longitude along the boundary of every page is the same primitive disk longitude. Adding a terminal block subdivides one transverse meridian passage into two consecutive passages. It does not add a second circuit around the torus. The new interface coordinate changes cancel in consecutive inverse pairs, so after forgetting the subdivision the path is the original primitive meridian.

There is exactly one distinguished original disk seam at each circle. All new page attachments are untwisted; the original pure or signed odd disk map is applied once at that distinguished seam. In particular a positive and negative retained half twist have the same puncture permutation but different marked meridian words. The old multipliers are \(\rho Q\) for the actual negative crossing and \(\rho/Q\) for the actual positive crossing. With \(Q=e^{i\tau_v}\), their correction is exactly \(-i\epsilon_v\tau_v\), not an additional correction at every page.

Using the independently checked local increments, the concatenation therefore gives
\[
 U_v=-2\pi\sum_{e\sim v}\partial_{\tau_v}\psi_e-i\epsilon_v\tau_v,
 \qquad V_v=2i\tau_v.
\]
The coordinate changes between pages telescope in \(d\log(z-q_v)\). The equality concerns the continued path integral, not the principal logarithm of the final multiplier. With \(n_v=\epsilon_v-2p_v\), the charge equation gives \(U_v+p_vV_v=-2\pi ic\) in the original primitive basis.

## 5. The positive metric and the auxiliary log plane

The local eight-tetrahedron blocks remain positive in the explicit angular bidisk. The ordered outgoing/incoming seam ratios are inverse as complex numbers with the continued angle branches. Thus both shears and angle returns agree; the glued metric is nonsingular at ordinary points and at finite edges. At completeness the regular cells and their labeled face maps give the original complete cusp sections.

At the distinguished odd seam I independently checked the additional explicit \(A,B\) matrices, rather than deducing the odd gluing from the pure seam table. Their maps on the three ordered vertices are exactly the stated cross-copy maps. Direct matrix multiplication gives
\[
 W_0^{-1}BW_2^{-1}A=(-R/E)I,\qquad
 W_2^{-1}BW_0^{-1}A=(-R/E)I,\qquad
 W_1^{-1}BW_3^{-1}A=((R-1)/E)I.
\]
The scalar multiples are units in the selected chart, hence these are the asserted projective identity returns. Both apex images reduce to \(Z/E\) under the defining quadratic. Since the entire ordered two-triangle pants chart depends only on \(Q\), transporting it between incident blocks with different other endpoints preserves this specific odd gluing. Its puncture exchange is the actual one fixed by \(A,B\). This explicitly verifies the distinguished odd seam as well as the untwisted seams.

The cusp links are nonsingular similarity tori. A main puncture is represented by its local nontrivial parabolic word, so the corresponding peripheral group is a translation group and its compact Euclidean link is complete.

For an auxiliary cusp at positive charge, \(\Re V_v=-2\Im\tau_v>0\). The peripheral similarities therefore have a second common fixed point \(q_v\). The invariant vector field \((z-q_v)\partial_z\) pulls back to a vector field on the link. Any zero has index \(+1\), whereas the torus has Euler characteristic zero; hence the development misses \(q_v\). Its logarithm on the simply connected link cover has nonzero derivative, and \(|df_v|^2\) descends to a complete Euclidean metric on the compact link. The resulting developing local isometry covers the plane and is a diffeomorphism. Its two primitive periods form a real rank-two lattice.

This argument gives the required log plane from the actual positive metric. It does not assume discreteness of the incomplete cone holonomy.

## 6. Integer periods and cone completion

The actual period differences \(P_\mu-U\) and \(P_\lambda-V\) lie in \(2\pi i\mathbb Z\) and vary continuously for positive charge. The revised draft fixes their initial integers directly. In a peripheral frame continuous at completeness, the longitude is \(z\mapsto e^V z+b\), with \(b(0)\ne0\). Its second fixed point \(q=b/(1-e^V)\) escapes to infinity. Each fixed generator path has bounded developed position and length for this fixed finite tree, so
\[
 |P_\gamma|\le L/(|q|-B)\longrightarrow0.
\]
Both candidate logarithms also tend to zero. The two integers vanish near zero and thus throughout the connected charge path. No globally small representation norm is required at charge one.

The ordered pair \((\mu+p\lambda,\lambda)\) is a primitive integral basis. Its first period is \(-2\pi ic\); its second has real part \(\ell=\Re V>0\). Thus \(\lambda\), the complementary primitive curve itself, represents the oriented core generator.

The cylindrical coordinate change
\[
 r=y/|z|,\quad R=\operatorname{arsinh}(1/r),\quad
 \theta=\Im f,\quad X=\Re f+\tfrac12\log(1+r^2)
\]
gives \(dR^2+\cosh^2R\,dX^2+\sinh^2R\,d\theta^2\). Compactness of the actual similarity link gives a whole sufficiently small punctured tube. Adding its axis produces angle \(2\pi c\), and at charge one an ordinary smooth solid torus with the original filling meridian. The other ends remain complete main cusps and the middle is compact. This proves completeness on the actual filled topology, conditional only on the already separately supplied analytic charge path.

## 7. Absolute action and volume

I recomputed the action normalization independently. With \(U^0=-2\pi\Psi_\tau\),
\[
 G^0=2\pi i(\Psi-\tau\cdot\Psi_\tau),\qquad
 dG^0=\tfrac12\sum V\,dU^0.
\]
The one retained half twist contributes \(-\epsilon V^2/8\), giving the draft's exact \(G\). At the stationary charge point, writing \(\Phi=G/(2\pi i)\),
\[
 \Phi-\mathcal C(c)=-\frac{i}{2\pi}\sum p_v\tau_v^2,
 \qquad
 \frac12\Re U_v\Im V_v=p_v\Im(\tau_v^2).
\]
These two terms cancel in the actual marked regulator. Its complete constant is fixed by the regular two-octahedron blocks. Hence \(\operatorname{Vol}_c=2\pi\Re\mathcal C(c)\). Differentiation gives \(2\pi\sum\Im\tau_v\), which agrees with the cone Schläfli expression \(-\tfrac12\sum\ell_v\,d(2\pi c)\). The factor, sign, and complementary primitive curve are consistent.

## 8. Verdict and exact scope

The ordered topological proof and the charge-path geometric completion check in full in the versions identified above. No mathematical correction is requested. Together with the previously checked local chart, they supply the actual disk-page topology and primitive path input that was left conditional in the local calculation.

The conclusion concerns finite ordered fully circled trees, with every inherited frame, projection label and distinguished signed disk seam retained. It does not extend the decomposition to arbitrary tensor networks, bare product junctions, graphs with cycles, or arbitrary changes of puncture matching. The analytic existence and dominance of the charge path remain the separate short-twist analytic certificate. No geometric conclusion was inferred from a source identity, and no general all-short-filling claim is made.

Original reference hashes retained in this audit:

- `notes/actual_conway_bowtie_projection_cut.md`: `d111390b82a56ed52e9afe9ffb99070762286b72df81fbe9e34d7050ceabaccc`.
- `notes/actual_conway_net_twist_volume.md`: `cd76d2d1f9b0ce2961308343d80098ec3336dd367248fbe36ee811e959fbcfa2`.
- `notes/actual_conway_general_mask_marked_filling.md`: `f3d0b91665c0bf62d26f71e4e0fa3368fe8714cdccab7d30b4e04272c61c209d`.
