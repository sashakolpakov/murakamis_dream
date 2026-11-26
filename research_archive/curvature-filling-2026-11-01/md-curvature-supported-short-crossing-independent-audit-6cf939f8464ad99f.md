# Independent audit of the curvature-supported short-crossing certificate

1 November 2026. Private read-only mathematical record.

Audited input:
`/private/tmp/md-curvature-supported-short-crossing-analytic-certificate.md`,
SHA256 `6599adb7a79290201c5d39faaa0c4d8f32e2a2788bf79c37adbcebfc908e534c`.

Independent elementary comparison:
`/private/tmp/md-all-circle-uniform-gaussian-check.md`,
SHA256 `78735dbb13dce9ace4b0a6f780418d9f0b48b3aa0dd4bc396dac8092e1012c09`.

The written analytic proof checks. It concerns a fixed actual all-circle operation tree, with the original typed composition, knot qualification and zero framing. Its graph and integer crossing powers are fixed before the level tends to infinity. No uniform starting level or polynomial prefactor over growing graphs is claimed. The conclusion is an analytic first-packet/profile theorem under the displayed numerical condition; actual hyperbolic volume identification remains conditional on the separate geometric completion certificate.

## 1. Actual source and uniform discarded-state loss

At each actual circle vertex, the fixed-power crossing polynomial and its inverse have polynomial full Hermite norm on every fixed disk |s|≤R<1. This is precisely the fixed-power input in `actual_main_meridian_source_bounds`, Section 1.3; it includes negative and zero powers, both same and opposite color types, and their retained reference scalars. Canonical quotient multiplication has polynomial cost for each fixed valence by its exact Chebyshev folding lemma. Top-coefficient trace extraction has polynomial cost in that same full norm.

Consequently the physical trace of an arbitrary incident index assignment has rate at most the sum of g over its low incidences; high Newton polynomials have polynomial full-normal norm. This step does not use a same-index comparison with a complete trace and is unaffected by the valence-nine obstruction. Each edge is present twice, so the full absolute exponent is bounded by 2 sum g, and its maximum is exactly 2|E|G0 for this graph class. The paired edge scalar H/W and its inverse are uniformly bounded on a fixed pre-resonance disk, at every basis index.

From g''≤−4π and g'(1/4)=0, a low edge outside [1/5,3/10] loses at least π/100. A high edge loses at least 2G0≥π/4. Closed sine-factorial bounds and the polynomial count of states preserve any smaller fixed loss; π/200 is valid. The number of edges affects polynomial powers and constants, but not this exponential loss. Scalar closing, framing and mixed-reference factors remain bounded normalized factors and are not silently reset.

## 2. Exact edge action and finite complex wire packet

I independently derived the stationary equation by writing C=cos(2πx). It is
(C+cos t)(C+cos u)=(1−C)^2, hence the displayed formulas (10). With p=tan(t/2), q=tan(u/2), tan²(πx)=(1+p²+q²)⁻¹. Differentiating the actual integral gives
ψ_t=−π⁻¹ asinh(tan(t/2)cos(u/2)). Its Hessian is the one in (12), and its determinant is 1/(4π²). Summing over edges gives precisely the degree-weighted diagonal curvature a_v=d_v/(2π), not a constant curvature per vertex.

The numerical inequalities in Section 5 have sufficient room. On the stated complex x strip, Re sin(2πx)>0.95, |Im sin(2πx)|<0.040, Re cot(πx)>0.72, and the denominator of the first fraction has real part above 0.655, imaginary magnitude below 0.159 and modulus below 1.37. These imply Re A_xx<−12; the modulus bound 44 is conservative. The selected x lies within 0.003 of 1/4. Finite integer-endpoint displacements are O(1/N) and fit the strict numerical margins for sufficiently large N.

For the finite cotangent rectangle, the vertical estimate at |X|≥0.047, |Y|≤0.005 is at most −0.002364. The horizontal maximum is (308/3)Y²≤77/30000, smaller than the nonconstant mode penalty π/250. Constant-mode translation therefore has a strict endpoint margin, while the real tangent at the selected saddle has strictly negative real Hessian. The canonical G_N arguments remain in fixed regular bulk strips. This supplies an actual holomorphic finite-sum expansion, not an extrapolation from values on the integer grid. Midpoint offsets and the original interpolation normalization are retained.

## 3. The real and complex global Gaussian

Both supplied proofs establish the displayed weighted global Gaussian.

In the direct-factor proof, the normalized factors are |1-u/c| with u=sin²(t/2). For the first floor(N/5) factors c≥cos²(π/5), the chord majorant is 1−(2√5−4)u. For the remaining factors c≥cos²(3π/10), it is 1+(2√5/5)u. Both follow by the endpoints of the two linear pieces of the absolute value. Their net exponent is −αN u, α=(9√5−20)/25>1/250, and rounding costs less than e².

For complex displacement |y|≤1, the real part of a normalized factor changes by at most (3/2)y², the imaginary part has magnitude at most 3|y|, and the real factor has absolute value below two. Its squared modulus therefore increases by at most 18y². The real majorants are at least one half, so the extra multiplicative cost exp(36y²) is valid. With at most 3N/10 factors this is bounded by exp(11Ny²).

The independent paired-factor proof is also valid. Negative reciprocal-quadratic factors pair with disjoint positive ones to give nonnegative symmetric Laurent coefficients. The reserved floor(N/32) factors provide angular damping. This yields stronger constants than those actually used. Neither proof assumes termwise Laurent positivity for an unpaired negative factor.

After incidence summation, 2α/π>1/400 and 22π<70 give (20). The Gaussian weights are a_v. O(1/N) translated grid endpoints change only fixed-graph prefactors. No tree-size loss is hidden in these constants.

## 4. Degree-weighted nonlinear contraction and charge ordering

The complex Hessian estimates give the symmetric row bounds in (16). Symmetry matters: from |E_vw|=|E_wv| and 2|z_v z_w|≤|z_v|²+|z_w|², their quadratic bound is ε sum a_v|z_v|². There is no multiplication by the number of vertices.

Since a_v/|D_v|≤1, division by D_v makes the fixed-point map Lipschitz with constant at most ε=1/25. Its image radius is at most 1/16+(1/50)/4<1/4. This proves the selected branch for every retained charge, including zero crossing powers. The quotient Q_v=E_v/τ_v extends because the action is separately even; |Q_v|≤δa_v.

For τ_v=−iℓ_v/(D_v−Q_v), the real part of the denominator lies between (1±δ)a_v and its modulus lies between (1±δ)|D_v|. This proves (25), including the sign of Im τ_v. Differentiation of the stationary action gives ∂ℓ_v Re C=Im τ_v. Integrating these estimates gives (26) and β=πγ_+ S, with no ratio restrictions on the signed n_v.

The stationary sine factors cannot vanish: every positive charge has Im τ_v<0 and |τ_v|<1/(16(1−δ))<π/2. The Hessian's real part on real tangent vectors is bounded above by −(1−ε)diag(a_v). Its associated Hermitian real part is also negative, so the complex determinant is nonzero. The product leading amplitude is nonzero for each fixed tree.

## 5. Tails, endpoints and the decisive connector estimate

With y=A0 t0 a/|D|, the positive quadratic cost after maximizing the real coordinate is at most 100|D|²y²/a. The first omitted charge exceeds t0|D|. For A0=1/400, the net coefficient is at most −(3/4)A0 t0²a; the weaker displayed half is valid. Since a≥1/(2π), the loss is at least 1/(409600π). All further charges have the stated geometric decay. Their Chebyshev factors grow only with the fixed charge index and parameter radius, and are absorbed when N is sufficiently large for the fixed graph and fixed powers.

The original endpoint loss π²a/400 dominates the three stated chirp/finite-charge/imaginary costs. Real-spectator telescoping is essential here and is retained: no estimate takes the absolute size of all spectators on their separate complex filling contours.

For the finite charge contours, the real-box complement loses 1/(51200π). The translation connectors are controlled by (32), derived from the weighted error bound and Young's inequality. The exact potentially dangerous constant is

    γ_+·2/(3−4ε)=127500/170471<3/4.

The other entry in the maximum is smaller. Therefore every spectator's quadratic imaginary cost is absorbed by its own negative Fourier term. A connector face loses at least aρ²/8≥1/(1024π), independently of the number or degrees of the other vertices. This is the step that prevents a hidden total-charge or graph-degree constant.

The current draft correctly states the resulting error additively. A nonminimal original contour equals its local saddle term plus O(poly(N)exp(N(F0−η))). The connector is not claimed to lie below every nonminimal critical action. Only the first charge requires a relative asymptotic; all additive errors lie below it. This distinction was made explicit during the audit and is sufficient for the stated conclusion.

## 6. Threshold, normalization and scope

With η=1/(819200π),

    β≤π(2550/2401)2⁻²⁵<η/2.

The source, real-box, tail, connector and finite-wire losses exceed this chosen η. The retained nonminimal charges are compared directly with the first joint action using (26); fixed absolute errors are compared with F0−β. This separates the two comparisons correctly.

The first Fourier coefficient equals one for both parities. The maximum principle is applied to the whole holomorphic difference, not to separately divided currents at σ=0 or ±1/2. There is one H_N from the reduced cut. All original typed scalars, mixed-reference factors, fixed crossings and writhe corrections remain in A_N. The edge count and one Gaussian per circle give the original N^(3/2) final power.

The S threshold can permit short or zero powers only at sufficiently high-degree vertices while the rest of the weighted sum remains small. It does not allow a graph or a power to grow with N. Its nonvacuity examples preserve the original knot/parity qualification and make no topology claim.

The normalized slope identity (37a) is consistent with the recorded primitive auxiliary cusp: c=1/d and n=ε−2p give L²=(d²+n²)/(2d), hence S=(1/2)sum L⁻². This translates the analytic condition; it does not supply metric completion by itself. I did not independently re-prove the separate short-filling geometric certificate in this audit. The analytic action must not be called the actual knot-complement volume until that certificate, or another proved geometric identification, is supplied for the branch in question.

No repository file was edited in this audit. The preserved A-interface report was not changed.
