# Bounded manuscript logic audit: central contribution and full-volume transfer

Date: 1 November 2026. Checkout: `/private/tmp/murakamis_dream-publication`, HEAD `021e6482b99f8456b4a34912e9f97969fc546a69`. This is a read-only review. No public source, generated artifact, or formal module was changed; no numerical experiment, compiler, or manuscript build was run for this review. The companion JSON records hashes of the inspected sources.

## Conclusion and limits

I found no mathematical correction required in the examined implication chain. In particular, Appendix O's fixed-complex relative interpolation, equation `mca:eq-7`, and its separated-spectral estimate `mca:eq-H2` have arguments for the actual finite cofactors, not merely matching values at spectral nodes. They retain the odd skipping summand, the even native anchor, and the norms needed before applying Cauchy estimates to repeated-node derivatives.

Appendix O establishes the central contribution only. Appendices P and Q obtain a full-invariant statement by supplying a separate bound for the entire complementary source and then using Appendix N. The present versions do not infer that bound from the existence of the central saddle, from a complete positive endpoint, or from finite numerical checks.

This is not an exhaustive validation of the manuscript. I freshly read Appendix Q, Appendix P, the analytic part of O and its local interpolation/angular/spectral dependencies, and O's regulator-to-metric completion. I checked N's source normalization and norm interface, the main theorem scopes, and the relevant existing audit/dependency records. I did not rederive every quantum-group identity, the complete packing-existence theorem, the entire marked representation construction, or the separate characteristic-polynomial chapters. Earlier reports were used to locate dependencies, not as substitutes for the local proofs read here.

The only concrete documentation omission found is `repro/PROOF_INPUTS.md`: its result table at lines 8–18 and subsequent sections omit the now included Appendix Q. A useful correction is to add the protected triangular-sum theorem with its **unabridged finite sector-certificate hypothesis**, referring to Q's exact coefficient transfer and N/O. This omission does not change the theorem proved in Q.

## 1. The exact source is identified before any estimate

Appendix O, lines 42–103 (`mca:sec-1`, `mca:eq-1`), starts from the original matched-sphere Morse source. The four-face polynomial has total face degree `d=N-1`; a path from j to i has middle powers `b^i c^(d-j)`. The central piece is the actual support `i<=floor(d/2)` and `d-j<=floor(d/2)`. A two-step path skipping the middle is therefore still central, and the odd zero-step path occurs once. This definition is essential: “passes through the middle row” would be false for the actual odd source, but the current text does not make that substitution.

The marked faces remain exactly zero, every ordinary face has its original degree-d demand, and the mark, cup/cap factors, even coset, and framing conventions are imported from the stated exact Morse compiler. This is the algebraic input to O and Q; no planar-tree factorization is used. The Q source in lines 292–320 is the same polynomial, including repeated roots of the Chebyshev polynomial.

Appendix N, lines 22–72 and 81–135 (`uf:eq-1`–`uf:eq-7`), requires spectral degree at most d in **each** variable. The physical functional is the full weighted Hermite functional for the actual signed crossing power, not merely the untwisted top-coefficient functional. Equations `uf:eq-12`–`uf:eq-20` retain the original phase and its derivative, including the odd simple node; they yield the norm `1+|n|/2`. Its tensor version applies after shared face extraction. Q uses this weaker full norm and consequently does not depend on the optional product-grid vanishing improvement.

## 2. Why O's complex interpolation is more than nodal interpolation

The critical manuscript passage is O lines 219–250, `mca:eq-7`–`mca:eq-8`. Its supporting proof is `actual_cross_cofactor_interpolant_rigidity.md`, sections 1–4, with three genuinely necessary inputs.

First, `actual_cross_cofactor_interior_packet.md`, sections 2–5, proves a relative packet on a fixed complex spectral disk and fixed complex positive-face neighborhood when the middle face is positive. It works with the actual start-row sum. The dominant transfer root stays a unit, including where the smaller terminal root vanishes. Nested-domain Riccati iteration controls the tail; the exact initial projection is a nonzero analytic unit; analytic finite-product interpolation is anchored at the actual endpoints. Starts outside the strict saddle window are bounded with the original unused-row products before deforming the finite start sum. Thus the complex bound is not extracted from real nodal values.

Second, `actual_cross_cofactor_protected_packet.md`, sections 1–4, handles a zero middle face and both positive outer faces. Its first-order normal form retains the initial negative branch and proves its suppression; it does not discard it. The one-positive-outer degeneracy is an exact monomial. These are precisely the protected patterns needed by the simple marked sphere. An outer pair consisting of both protected faces is excluded by the actual nonmatching marked edge, not by a positivity assertion about an arbitrary four-variable polynomial.

Third, `actual_positive_face_exponential_fold_interpolation.md`, sections 3–6, constructs the anchored fold interpolation with exponentially small errors on **all relevant nodes at fixed complex face radii**. The complex face radius is chosen after the real damping rate, so the accumulated multiplier perturbation cannot erase that rate. The even anchor is at `1/(2N)` and the odd anchor at zero; forced factors and half-indices remain.

The rigidity note then checks the complete finite central factor. For even levels its ratio to the two D cofactors tends to `4 sqrt(A^2+u xy)`. At odd levels the ratio to the two G cofactors is

`1 + u s_m s_(m+1) xy D_b D_c/(G_b G_c)`,

which tends to `2S/(A+S)`, with `S=sqrt(A^2+u xy)`. In particular the skipping term and its u-derivative have not been dropped. Both ratios are units on a sufficiently small fixed neighborhood.

Uniform normalized logarithms of the independently controlled actual cofactors and the anchored interpolant therefore agree on the dense real node set and then holomorphically. This supplies a subexponential outer-circle bound for their ratio. Only **after this bound** is the finite Cauchy–Lagrange formula used. The reflected grid has spacing `1/N` at both parities. The noisy-node contribution costs `exp((2a log(3e)+o(1))N)`; the contour remainder costs `[2a/(R-a)]^(2aN+O(1)) exp(o(N))`. Choosing a fixed inner radius sufficiently small preserves exponential accuracy. Cauchy estimates then supply the actual fixed derivatives. This addresses the precise value-versus-normal ambiguity.

There is no claim of generic off-endpoint real stability, no claim that every analytic interpolation with those node values agrees, and no inference from a numerical test of the cofactor recurrence. The later private lower-cofactor instability findings do not contradict this local positive-face complex chart.

## 3. The angular and spectral estimates really cover H2

O lines 252–273 and 327–375 use two different estimates; neither can replace the other.

`actual_cross_cofactor_global_angular_gap.md`, sections 1–4, supplies the angular estimate. At a physical node the original cofactor factors as an actual PSD determinant times a positive tail. The tail positivity is proved by its exact recurrence, despite the negative recurrence coefficient. Far nodes have an independent strict value loss from unused positive paths or, with one outer zero, a first-order starting-row comparison. Near nodes use the original determinant phase contraction and order-N pair traces/variance; the required range is `a>=a0 N`, not an unsupported extension of a vanishing-deficit estimate.

The native node handling is explicit. For a terminal row `j=J-k`, with fixed k, the unavailable nodes with a>j are not evaluated through a fictitious determinant adapter. Multiplying by their omitted factors gives a degree-J polynomial zero at those nodes. Full Chebyshev-root/even or Chebyshev-Radau/odd interpolation has logarithmic norm; division by the fixed number of endpoint factors costs only a polynomial in N. Polynomial Bernstein growth then extends the whole-real-interval estimate to a fixed thin complex spectral strip. Thus H2 is not obtained from pointwise nodal bounds without an interpolation norm.

`actual_global_cross_spectral_gap.md`, sections 1–4, supplies separated real spectral loss at nearly common face phase. Its transfer bound retains the signed second-order recurrence. At the repeated-root line it uses the finite Cayley–Hamilton power formula, not a singular eigenbasis. Fixed blocks, uniform endpoint allowances, and truncated prefix logarithms give a uniform bound for all start rows, also after a sufficiently small fixed complex perturbation. The start maximum is `max(Q_b(delta), (1/2)log b)`; both branches are strictly below the complete nonmonomial rate away from delta=0. The exact one-variable monomial is explicitly exempt.

The simple marked-sphere graph facts ensure that every crossing has a nonmonomial triangle and that deleting the two protected vertices leaves the ordinary phase graph connected (O lines 181–217). Therefore the angular complement is controlled on the **same radii and original targets**, and the separated spectral estimate controls its small-phase complement. The total number of factors is fixed; the strip is shrunk after summing their finite growth costs. Cauchy estimates on smaller domains then establish H2's derivative version. No independent absolute estimate at each face, no changed coefficient demands, and no full positive endpoint theorem requiring a middle forest enter this step.

## 4. Nonzero contribution and geometric volume are separate implications

O lines 378–522 do not infer noncancellation from a formal critical point. The finite actions are separately even; their Hessian has the stated sign on one fixed chart. An actual outer cube is translated with all side currents below its critical value. The first charge has positive imaginary spectral coordinates for either sign of the fixed powers, so its sine factor is nonzero and the Gaussian determinant branch is fixed.

The sign-related charges are paired in the exact integrand: both sine and charge weight change sign. The raw parity cancels the original charge character, leaving the displayed `(-2i)^R`, not an assumed positive saddle amplitude. Infinite far charges are removed on whole intervals with real spectators and paired endpoint currents; bounded bad charges use a separate smaller cube. Only after these source gaps are fixed is the filling threshold increased so that the first-charge loss from the complete action is smaller. This order permits independently unbalanced fixed powers.

O lines 1031–1203 then identify the phase with **the actual smooth filled metric**, not merely a representation volume. The half-twist correction and primitive equation `U+pV=-2pi i` are retained. The regulator boundary term cancels the explicit phase correction. The framed representation lies near the original complete one; its longitude multiplier has nonunit modulus. The constructed affine cusp development avoids the second fixed point, and its actual logarithmic periods equal the small marked logs before multiplication by p. The primitive angle is exactly 2pi and the complementary period has nonzero axial component, so the tube closes smoothly. The main cusp stays complete. The same-chain comparison and original crossing-disk surgery identify the volume and topology. This is the extra step that an exponentiated peripheral relation alone would not prove.

I checked this implication and its matching hypotheses in O; the complete quantum compiler and complete marked-cell construction remain the expressly cited upstream results. No finite matrix or interval certificate is used as a substitute for them.

## 5. Full-volume closure and fixed-data quantifiers

Appendix P, especially lines 203–307 and 322–375, proves a shared-radius bound for every surviving noncentral sector from its weak-balance/positive-energy condition. The full spectrum and all phases are included before applying N and O. It does not promote weak balance to an unconditional theorem for every simple sphere.

Appendix Q, especially lines 101–124 and 258–383, requires an **unabridged** cover of every locally allowed noncentral string; globally zero old strings cannot silently be omitted. Its joined witness respects the same two protected coordinates and the one common ordinary face. The central and one-sided local identities produce a strict full complementary-source norm bound. The weaker finite Hermite norm then transfers that bound with zero exponential cost. Finally the selected filled action approaches the drilled action, and the powers are chosen long enough that this fixed source gap dominates the filling loss. The actual volume identification is imported only at this final point.

The new graph, its knot parity, its certificate vectors, and all integer powers are fixed before N tends to infinity. The proofs do not supply a uniform threshold for growing diagrams or permit an N-dependent sector cover. The finite number of sectors and the polynomial prefactors consequently contribute only o(N). These qualifications are present in the current statements.

## 6. Dependency skeleton suitable for formalization

A faithful decomposition should retain the following distinct propositions, rather than encode “the desired saddle dominates” as an input:

1. Exact Morse source: source equals the original normalized ribbon contraction; degree and protected target identities.
2. Exact local support: central/left/right partition, odd skipping term, even three-term cut, and physical node identities.
3. Analytic local packets plus anchored interpolation: fixed complex units and uniform errors.
4. Finite interpolation lemma: noisy grid plus independently controlled outer norm implies an exponential relative error; derivative consequence needs a smaller analytic domain.
5. Angular and separated-spectral lemmas: uniformity on the whole real spectral cube, followed by a thin-strip extension.
6. Connected ordinary graph and primitive lattice: unique face saddle and no extra phase aliases.
7. Whole-period theorem: exact charge signs, contour currents, summable infinite tails, nonzero unit contribution.
8. Marked geometric completion: original representation, actual log periods, smooth primitive filling, and calibrated volume.
9. Independent complementary-source certificate: a full real-spectral supremum gap at the original shared demands.
10. Finite weighted Hermite norm, then the elementary rate comparison transferring 9 and 7–8 to the full invariant.

Existing Lean finite-algebra/rate kernels can address parts of 1–2, 4, 9–10 after their stated objects are supplied. They do not themselves establish complex cofactor estimates, positivity/rank of the actual geometric matrices, the quantum compiler, contour noncancellation, or smooth hyperbolic completion. No statement in this audit counts compilation or finite experiments as proofs of those analytic and geometric inputs.

## Private research freeze

The current signed nodal-compression record remains private in `md-odd-nodal-signed-compression.md` with its exact runner, result, and manifest. Its exact weights and positive-atom comparison do not construct the requested constant Hermitian adjugate matrix, do not control all atom rank deficits, and prove no new spectral-neighborhood/full-volume theorem. The published global-angular note already contains the nodal-tail positivity and endpoint domination; those parts of the private record are not new theorem claims.
