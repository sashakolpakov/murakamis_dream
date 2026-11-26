# Independent check of preferred-cusp continuation in the angular chart

1 November 2026. The full checked draft is `/private/tmp/md-angular-edge-block-preferred-cusp-continuation.md`, SHA256 `1fca7e3e20a518228760c19ea560c5fdaf0257c9ebe724b4ff15293a2b75eb81`. This report is private. No repository or publication files were changed.

## 1. The complete marked representation

The comparison starts only after the ordered page construction has identified the actual augmented exterior and its original peripheral paths. Its regular octahedra produce a complete positive ideal triangulation of that marked exterior. The old strict Conway geometry is another complete geometric realization of the same marked exterior. Orientation-preserving marked conjugacy follows from the existing geometric uniqueness input, or directly from the repository's maximal-volume conjugacy theorem applied to this actual representation after the topological identification. Equality of cell volumes alone is not being used to identify manifolds.

The eight-tetrahedron subdivision per edge introduces no finite vertices. Its ideal vertex links are the actual cusp tori. All complete shapes are positive and all required developed vertex differences are nonzero. These are the hypotheses needed for the next local argument.

## 2. The exact all-cusp rigidity input

I read `notes/general_marked_multicusp_gluing_rigidity.md`, especially Sections 2–3. It already proves the precise statement needed here, including arbitrary primitive peripheral rows rather than only meridians. With \(t\) tetrahedra and \(q\) torus cusps, the edge rows have rank \(t-q\), are isotropic, and their symplectic quotient is the full \(2q\)-dimensional peripheral homology. Choosing one nonzero primitive path on each cusp gives a full rank \(t\)-row Lagrangian system.

Choosing the main meridian and all auxiliary longitudes is therefore legitimate. The paths lie on different tori, so they are isotropic and independent modulo the edge rows. In the draft's convention
\[
 u=\log z,\qquad v=\log(1-z^{-1}),\qquad
 dv/du=1/(z-1),\qquad \Im(dv/du)<0.
\]
This is the alternative quad convention explicitly allowed by the existing theorem. The rows are changed with the quad order. If \((A+B\operatorname{diag}D)a=0\), then \((a,Da)\) lies in the complexification of a real Lagrangian kernel. Its pairing with its conjugate would vanish, whereas the direct pairing is a fixed nonzero imaginary factor times \(\sum\Im D_j|a_j|^2\). This proves the required invertibility.

The same existing theorem supplies the decorated representation/shape equivalence, not merely the numerical shape Jacobian. For the old family, develop each lifted vertex \(gP_v\) as \(\rho(g)\xi_v\) using the selected peripheral flag. The cusp stabilizer fixes that flag, so this is well defined. The new triangulation's cross ratios stay holomorphic and positive near completeness, obey its actual edge equations and chosen peripheral logs, and use the same branches by continuity. Thus the old and new families belong to the same unique marked shape germ modulo one common conjugation. No separate conjugation of individual blocks is used.

The old longitude variables are valid coordinates: the original marked Hessian is diagonal and nonzero at completeness. For an all-circle vertex of degree \(d_v\), the new calculation gives \(\partial U_v/\partial\tau_v=d_v-i\epsilon_v\), also nonzero. This agrees with the old derivative after \(V_v=2i\tau_v\); there is no missing factor two.

## 3. The physical wire variables, not only the characters

I checked the cited original circle action and joint Legendre identities in `actual_main_meridian_regular_circle_trace.md` and `actual_main_meridian_joint_filling_transform.md`. They retain the physical edge indices before eliminating the hidden circle variables. With
\[
 b(x,\theta)=\int_0^x\log(2\cos 2\pi u+2\cos\theta)\,du-2J(x),
\]
the old local selected action is the stationary value of
\(\sum b+i\epsilon\theta^2/(4\pi)+i\chi\theta\). The old peripheral relation is \(V=-2i\theta\), so the angular geometry's convention requires \(\theta=-\tau\). Separate evenness leaves the edge action unchanged.

There are no bare product junctions in this class. Differentiating the two endpoint terms of one edge gives
\[
 (c+\cos\tau_v)(c+\cos\tau_w)=(1-c)^2,
 \qquad c=\cos 2\pi x.
\]
Solving on the branch at \(x=1/4\) yields
\[
 c=\frac{1-\cos\tau_v\cos\tau_w}{2+\cos\tau_v+\cos\tau_w}
  =\frac{y_v^2+y_w^2}{2+y_v^2+y_w^2},
 \qquad
 \tan^2(\pi x)=\frac1{1+y_v^2+y_w^2}.
\]
The derivative of the stationarity equation is nonzero at the complete point. These are therefore the retained old physical wire labels as analytic germs, rather than new coordinates chosen because they have the same complete value.

The angle-stationarity equation also gives
\[
 \chi_v=-i\Psi_{\tau_v}+\frac{\epsilon_v\tau_v}{2\pi},
 \qquad -2\pi i\chi_v=-2\pi\Psi_{\tau_v}-i\epsilon_v\tau_v.
\]
This is exactly the primitive page meridian already established topologically. The sign in \(\theta=-\tau\) is essential and is retained correctly.

## 4. Holomorphic translation and the preferred word

The old preferred-cusp identity is a rational face-map and path identity before imposing filling equations. The preceding two steps transport it to a neighborhood of zero in the new actual angular representation.

Every main meridian stays a nonidentity parabolic in the full angular chart, since it is conjugate to one of the local nontrivial pants meridians. Locally choose trace-two unipotent lifts and write \(M=I+N\), \(L=I+\lambda N\). On any chart with a nonzero entry of \(N\), the ratio defining \(\lambda\) is holomorphic. The ratios agree on overlaps and are invariant under simultaneous conjugation. Thus the unit-meridian translation of the actual longitudinal word is globally holomorphic on the connected angular chart. This is a translation ratio, not a logarithm of the main longitude, so there is no integer logarithm ambiguity.

The identity theorem now extends the old path formula throughout the chart. Its fixed word and endpoint orientations are retained. The self-linking calculation removes \(w_\epsilon\) copies of the main meridian; it is a topological word correction, independent of the representation. This gives the angular preferred augmented longitude with its actual framing.

## 5. Surgery and the endpoint cusp

The original crossing-circle linking data give \([\lambda_v]=\ell_v[\mu_K]\). Killing \(\mu_v+p_v\lambda_v\) therefore changes the preferred main longitude by
\(\mu_K^{\sum p_v\ell_v^2}\). The curve is fixed on the main boundary throughout the charge path; at charge one it is the preferred longitude of the actual smooth filled knot exterior.

With \(o_v=1\) for parallel strands and \(-1\) for antiparallel strands,
\[
 \ell_v^2=2(1+o_v),\qquad
 w_\epsilon=\sum o_v\epsilon_v,\qquad
 n_v=\epsilon_v-2p_v.
\]
Consequently the entire integer correction is
\[
 -\sum\epsilon_v-w_\epsilon+\sum p_v\ell_v^2
       =-\sum n_v-w_{\mathbf n}.
\]
This sign and equality were also checked by direct symbolic expansion. The resulting cusp formula uses the geometric cotangent edge sum and this preferred integer. It does not use the scalar ledger or a quantum first correction to identify the cusp.

## 6. Verdict, dependencies, and scope

The full continuation argument checks as written. No correction is requested. The addition of the direct multicusp rigidity reference makes its exact prerequisite explicit; no mathematical formula changed during that clarification.

The result applies to the actual ordered all-circle geometry on its connected positive angular chart, with one main knot component and the original disk and main peripheral markings. The endpoint conclusion also requires the separately proved charge path and smooth completion. It makes no assertion for unrelated algebraic solutions, arbitrary bare junctions, multiple-main-component preferred-longitude matrices, or arbitrary short fillings. It does not rely on a quantum asymptotic or prove a classical factor of an annihilator.

Hashes of the principal public inputs read:

- `general_marked_multicusp_gluing_rigidity.md`: `f882d2c7d1f723590391d3cc03dcd9bba7a12d13c2e006c6dea570e1b4af1b42`.
- `actual_main_meridian_preferred_cusp.md`: `a11313156ac50cb77e889cddc4e0adf15e0bd4347e6711957516a7e2bc656192`.
- `actual_main_meridian_regular_circle_trace.md`: `d194c95e019b28436dd45823d7eaa477c2278da5d70626e406a746ac512191c7`.
- `actual_main_meridian_joint_filling_transform.md`: `5730431c68356621eb95fd75c23363bc5f9aa120408ad187f3a2d456c45f9438`.
- `actual_fejer_unique_geometric_maximizer.md`: `231c22c5bd4f0c1527a84c4db92d83cc13b7f7b56627c47631644addb98f8ec4`.
