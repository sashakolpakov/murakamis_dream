# Independent check of the local angular two-octahedron chart

1 November 2026. This report checks the local formulas and their analytic and marked-peripheral consequences. It does not identify a general assembled collection of these blocks with an original Conway exterior.

The checked source is `/private/tmp/md-two-octahedron-angular-edge-block.md`, SHA256 `a87b5b2f1ff39bff15bb2ac6f3ec90ebe3d047e82778d7a660f85c49e1c0d57a`. The original transition and peripheral conventions were checked against `notes/actual_conway_general_mask_marked_filling.md`, equations (11)–(14) and (18), SHA256 `f3d0b91665c0bf62d26f71e4e0fa3368fe8714cdccab7d30b4e04272c61c209d`.

## 1. Actual placement and the complete branch

For the second leaf, its original ordered base has parameter \(R_1=1-R\). The actual turn is \(T(z)=-R/(z-1)\), and the original root identification is \(C(z)=(z-R)/(z-1)\). Consequently
\[
 C(T(z))=\frac{Rz}{z-R_1}.
\]
Both maps are required. At completeness, \(R=1/2\) and \(Z=(1+i)/2\); the turn alone fixes \(Z\), while the composed map sends it to \((1-i)/2\). The second projection apex is \(Z/E\), so its composed image is \(RZ/(Z-ER_1)\). This gives exactly the two rows of the source's apex table. No conjugation of the free complex variables is used.

Write \(y=\tan(\tau/2)\), \(z=\tan(\upsilon/2)\), and \(k=\tan(\pi x)\). The original longitude ratio gives
\[
 \frac{k-\tan\pi t_0}{k+\tan\pi t_0}
 =\frac{1-iy}{1+iy},\qquad \tan\pi t_0=iky,
\]
and likewise for the other leaf. Its base parameter is
\(R=(1-k^2y^2)/(1+k^2)\), hence the stated ordered metric is
\(k^2(1+y^2)/(1-k^2y^2)\). Multiplying the two metrics and imposing the wire equation factors into
\[
 (k^2+1)((1+y^2+z^2)k^2-1)=0.
\]
The branch through \(k=1\) is precisely the source's selected branch. Substitution yields \(R=(1+z^2)/(2+y^2+z^2)\), not its reciprocal or its complement. The source's complete orientations give four cross ratios \(i\) in each projection copy; reversing the last two vertices in the minus copy is essential.

## 2. Explicit positivity on the complex bidisk

The bounds in the source are valid for complex parameters. From \(|y|,|z|<0.005001\), one gets \(|k-1|<0.000026\). The Möbius formula for \(E\) gives \(|E-i|<0.00006\), and
\[
 |H_j-1|\le \frac{2|ky_j|}{1-|ky_j|}<0.0102.
\]
The quotient for \(Z_j\) then gives a bound below \(0.00366\), so the stated \(0.004\) is safe. In either transformed apex denominator the complete modulus is \(1/2\), with perturbation below \(0.0041\). Bounding numerator and denominator separately gives apex displacement below \(0.01\); the stated \(0.02\) is safe. The displacement of \(Z_j/E\) is below \(0.00405\).

Distinct finite vertices in the complete tetrahedra have distance at least \(1/2\). Thus every finite difference changes relatively by less than \(0.08\). For four factors the quotient error is bounded by
\[
 \frac{4(0.08)+2(0.08)^2}{(1-0.08)^2}<0.4.
\]
Factors at infinity only reduce the number of terms. All shapes therefore remain in \(|w-i|<0.4\), with positive imaginary part, and all denominators remain nonzero. The product of the four cross ratios around the apex diagonal telescopes to one. Its angle sum stays \(2\pi\), since it has that value at completeness and cannot change its integer branch in this positive chart.

This validates a local positively oriented tetrahedral subdivision. It does not make the free-complex equator planar. The source explicitly retains triangular boundary pieces and does not infer a planar quadrilateral face from these estimates.

## 3. Full complex seam ratios

The defining relation is \(Z^2-(1+E)Z+ER=0\). Equivalently one may substitute \(R=Z(1+E-Z)/E\). With \(Q=(E-Z)/(Z-1)\), the transported opposite vertices used by the six edges are, in their cyclic order,
\[
 E,\quad Z-E+1,\quad \frac{ER-1}{E-1};
 \qquad
 \frac{R(E-1)}{E-R},\quad \frac{ER}{2E-Z},\quad ER.
\]
The first three are the incoming triangle's opposite vertices; the last three are the outgoing triangle's. Direct rational reduction gives respectively
\[
 -Q^{-1},\quad -Q,\quad -Q^{-1};
 \qquad -Q,\quad -Q^{-1},\quad -Q.
\]
All six identities, together with the formula for \(C\circ T\), were independently reduced symbolically to zero using the displayed quadratic relation. In particular the two entries involving \(W_2^{-1}\) and the outgoing base entry retain their signs.

The parameter substitution gives
\[
 Q=\frac{i-y}{i+y}=\frac{1+iy}{1-iy}=e^{i\tau}.
\]
Thus the table is independent of the other angular endpoint, including its complex shear. The products at the two main punctures are one, while those at the disk apex are \(Q^{-2}\) and \(Q^2\) for the two oriented disk sides. The original marked disk longitude uses \(Q^2\), in agreement with the original word \(W_2^{-1}W_0\).

Under the original ordered matching \((Z,R,0)\mapsto(Z',\infty,1)\), every outgoing ratio is the inverse of its incoming partner. Three ordered ideal vertices normalize one triangle, and the three edge ratios determine the adjacent third vertices. Hence this is a complete complex seam comparison, not a modulus-only comparison. Near completeness choose the logarithms of the negative ratios through \(i\pi\). The paired logarithms sum to \(2\pi i\), so the interior angle and shear branches match. No arbitrary puncture permutation is being used.

The original white completion convention also matters: \(W_1,W_3\) can be completion maps at the open leaf; the actual two-leaf closure supplies them from the neighboring white pieces. The local calculation does not need to turn a virtual completion into an additional invented face.

## 4. The small logarithmic increment

On the branch through zero,
\[
 t_0=\frac{i}{\pi}\operatorname{artanh}(ky),\qquad
 \partial_\tau\psi=it_0
 =-\frac1\pi\operatorname{arsinh}\left(\tan(\tau/2)\cos(\upsilon/2)\right).
\]
The identity follows from \(\operatorname{artanh}(w/\sqrt{1+w^2})=\operatorname{arsinh}(w)\), with all branches fixed at zero. The two first derivatives are integrable: their mixed derivatives agree, and their diagonal second derivatives at zero equal \(-1/(2\pi)\).

The original pure meridian multiplier is \(\rho=Z/(1+E-Z)=H^{-1}\). Its small log is therefore \(-2\pi i t_0=-2\pi\partial_\tau\psi\), exactly as stated. The original odd marking changes this to \(U=-2\pi it-\epsilon V/2\), with \(V=2i\tau\). If the original primitive path is proved to concatenate the proposed local paths, then
\[
 U_v+p_vV_v=-2\pi\sum_{e\sim v}\partial_{\tau_v}\psi_e
                 -i(\epsilon_v-2p_v)\tau_v.
\]
The first-charge critical equation \(\sum_e\partial_{\tau_v}\psi_e+i n_v\tau_v/(2\pi)-i=0\), with \(n_v=\epsilon_v-2p_v\), gives exactly \(U_v+p_vV_v=-2\pi i\). The sign and primitive integer agree with the original filling convention.

## 5. Conclusion and boundary of this check

The local placement, branch choice, explicit positive tetrahedra, complete complex seam ratios, and local logarithmic increment are correct as written. No correction is requested. The remaining global obligation is exactly the one stated in the source: identify the proposed ordered disk-page assembly with the literal augmented exterior and prove that its concatenated paths are the original primitive disk paths. The local identities neither prove that topology nor permit replacing it by equality of volumes or actions.
