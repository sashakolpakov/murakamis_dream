# Fresh bounded audit of Appendix O's analytic half

This report reads publication HEAD `164cb2c31ed788aa7375b18f2c3561cc445e6e2a`, Appendix O lines 1–630 and 1249–end. It follows the actual local cofactor, interpolation, face-torus and charge proofs listed below; it does not use earlier approval messages as mathematical premises. No public file was edited and no exploratory research result is used.

**Conclusion.** I found no concrete failure of the claimed nonzero whole central period for a fixed certified simple-sphere Morse source and independently sufficiently long fixed signed powers. The most delicate charge derivative, contour-side estimates, endpoint pairing and summable far tail can be rederived from the stated source estimates with the original scalars. There is one normalization-wording correction, described first. The theorem remains a sector theorem; the full invariant still requires a separate complementary-source bound.

## 1. One precise wording correction

At line 1276, in the paragraph after `mcg:eq-31`, replace

> The local cofactor interpolation retains the odd simple-node derivative,

by

> The local cofactor interpolation retains the double-node derivatives and the odd simple-node value,

The actual polynomial has a derivative at a simple node too, but the original full-Hermite functional uses only its value there. This sentence is not a formula error: the first analytic half already retains the exact odd simple node and the independent odd skipping-term derivative correctly. The parent plans to make this correction after this snapshot is frozen.

## 2. Exact object and normalization

The central projection in `mca:sec-1` uses the original monomial exponents: both middle exponents are at most floor((N−1)/2). The two one-sided supports are its disjoint complement because the sum of the middle exponents is at most N−1. This includes a path that skips the middle row and includes the odd central zero-step path once. It is a linear projection of the actual local numerator, not a claim that the projected sector alone is a topological invariant.

The cofactor factorization keeps the odd term `u s_m s_(m+1) xy D_b D_c` and its derivative at u=0; at odd level the two sine factors coincide. The even three-term cut is also retained. No inference of normal data from nodal values is used in H1: the off-node packet and the exponentially accurate Cauchy–Lagrange rigidity are separate inputs.

I rechecked the Fourier conversion from the exact spectral total-derivative identity. With phi=pi+2pi delta, the factors are: the midpoint character (-1)^ell, the Fourier translation (-1)^(N ell), the sine minus sign, and the charge reversal ell↦−ell. The resulting one-variable prefactor is exactly -i times the original `q^(n d²/4)`, with character (-1)^((N+1)ell). Tensoring gives `mca:eq-2`. Charge zero is absent by the exact derivative, not deleted asymptotically. The odd simple node has the original half multiplicity in the full midpoint grid. Exterior component/framing factors and the optional one-cut i^(N+3)/N factor stay outside the raw period as stated.

The face Gaussian has dimension R−1 and measure (2pi)^−(R−1), after one common scale is fixed. Thus the two Gaussian integrations give exactly

    N^(2R) (2pi N)^(-(R-1)/2) (2pi/N)^(R/2)
      = sqrt(2pi) N^(R+1/2).

The finite action contains all anchor, beta, forced-product and logarithmic level terms. Replacing it by its limit inside a relative asymptotic would be unjustified, but O does not do so.

## 3. The local packet and fixed strip are actual source estimates

I read the following arguments, rather than only their theorem statements:

* `actual_cross_cofactor_interior_packet.md`, sections 1–5: the original row-replaced determinant and starting-row recurrence; strict interior starting saddle when the middle is positive; dominant-tail recurrence with no division by the smaller eigenvalue; exponentially accurate discrete primitives; retained vertical currents in the cotangent rectangle; fixed complex parameter neighborhoods.
* `actual_cross_cofactor_protected_packet.md`, sections 1–4: the actual protected-middle recurrence, the algebraic eigenvalue gap despite equal moduli at the lower endpoint, its off-diagonal normal form, the retained initial negative branch, and the exact one-variable monomial exception.
* `actual_positive_face_exponential_fold_interpolation.md`, sections 2–6: removable squared-fold equation, the single analytic-radius loss, contraction on nested domains, positive actual-pivot matching in a fixed complex face neighborhood, and the discrete primitive anchored at the actual parity endpoint.
* `actual_cross_cofactor_interpolant_rigidity.md`, sections 2–4: the central factor is a holomorphic unit; actual and interpolated normalized logarithms agree; exact node spacing bounds the noisy Lagrange part; the fixed outer circle bounds the remainder. Its fixed derivative version follows on smaller disks. This uses off-node source growth, not values alone.

The protected-zero pattern is fixed throughout. Every other radius lies in a fixed positive compact belonging to the particular diagram. No uniformity as a supported radius tends to zero, or as the diagram grows, is required.

For the shared face saddle I read `actual_positive_face_coefficient_saddle.md`, sections 2–4, and the integral rank argument in `actual_original_boundary_transverse_rank.md`, sections 1–2. The PSD compression identity gives an actual determinant modulus bound; pair-trace lower bounds give a factor proportional to N. The ordinary graph is connected after deleting the protected adjacent pair. Its literal differences have integral coefficients +1,−1, so the only angular maximum is common phase and there is no extra alias multiplicity. The even forced factor has nonnegative coefficients and cannot worsen that angular bound.

Appendix O reassembles H1 directly from the central polynomial. It does **not** use the full-numerator restoration in `general_full_spectral_numerator_geometric_packet.md`, section 4. Hence it does not assume a noncentral gap to prove the central period. The older localized theorem's full-source/flat-plat opening is not imported as an extra premise; its contour proof applies to the H1 proved in O.

For H2 I read `actual_global_cross_spectral_gap.md`, sections 1–4, and the local global-angular proof. The slow-transfer estimate is valid even at a repeated transfer eigenvalue: Cayley–Hamilton bounds a fixed matrix power by C(k+1)rho^k, then fixed long blocks are used before N is sent to infinity. The small t interval has a separately controlled eta log(1/eta) allowance. Truncated logarithms give a uniform prefix upper even at sampled zeros. The starting-row maximum is exactly max(Q_b(delta), log(b)/2), with its sole-start version when b=0. Every actual crossing has a nonmonomial triangle and thus supplies a strict real-spectral loss when its delta is separated. The angular complement and the small-phase complex-face estimate are combined on the same original radii.

The resulting H2 is uniform in all real spectator spectra, on a fixed thin complex strip chosen after the separation eta. This stronger shared estimate is what the far-charge argument needs. Polynomial periodicity handles a Cauchy neighborhood crossing the chosen real endpoint representatives. No arbitrary-face coefficientwise domination or independently optimized local weights are assumed.

## 4. Independent derivation of the critical-value comparison

Write the separately even finite action as

    partial_e A_N = -2 delta_e B_(e,N)(delta²).

On one smaller fixed chart, `|B_(e,N)-C_e| <= C_e/8`, with C_e>0, for all sufficiently large N. The actual critical equations are

    delta_e = -(ell_e/n_e)/(1+i B_(e,N)/(pi n_e)).

Contraction is uniform when all ell_e/|n_e| are at most a fixed small a and all |n_e| exceed one common n0. No ratio of powers enters the derivative bound for this map. For positive charges, direct complex division gives

    Im delta_e = ell_e Re B_(e,N)
                 / (pi n_e² |1+i B_(e,N)/(pi n_e)|²) > 0.

This holds for either sign of n_e. Differentiating the critical value uses stationarity to remove derivatives of the critical point:

    partial_(ell_e) Re S_(N,ell)
      = Re(2pi i delta_e)
      = -2 ell_e Re B_(e,N)
        / (n_e² |1+i B_(e,N)/(pi n_e)|²).

After increasing n0, the quotient involving B is at least C_e/2. Integrate along a coordinatewise monotone path from the unit vector to ell, entirely inside the scaled local charge box. This gives exactly

    Re S_(N,1) - Re S_(N,ell)
       >= sum_e C_e (ell_e²-1)/(2 n_e²).

The comparison therefore survives arbitrarily unequal fixed powers. It does not compare independent saddle-error estimates. Its smallest nonunit loss may depend on the fixed power vector; only positivity is required before taking N to infinity.

## 5. Actual contour and nonzero coefficient

The correct order is: fix an outer cube of radius B inside the source chart; choose a sufficiently small relative to B; then choose a separate inner radius b<a/4. Only afterward enlarge n0. The outer and inner cubes have different tasks.

For a local charge, the outer cube is translated by the critical imaginary vector y*>0, coordinate by coordinate. On an actual side, one real coordinate has modulus B. Reality on the real chart gives

    Re A_N(x+iv) <= A_N(0) - c|x|² + C|v|².

The linear imaginary perturbation contributes no real term. Moreover 0<=v_e<=C ell_e/n_e², so the chirp costs at most C B sum(ell_e/|n_e|), while the charge part is nonpositive. The critical real value is at least A_N(0)-C sum(ell_e/|n_e|)². Choosing a much smaller than B makes all actual sides strictly lower than this critical value, uniformly in power ratios. This proves contour coefficient +1; no arbitrary steepest-descent coefficient is assigned.

On the translated real plane, the negative Hessian has positive real part because the chirp Hessian is purely imaginary. The Gaussian square root therefore has the stated unique branch on the accretive symmetric matrices. Strict real concavity controls the whole translated cube; the critical point stays away from its boundary. The amplitude is a holomorphic unit except for the sine factors, and every critical imaginary coordinate is strictly positive. Those sines are nonzero and have a nonzero limit for each fixed sufficiently long power vector. Cubic Gaussian terms integrate to zero, giving the relative O(N^-1) error with finite action retained.

Reflecting one charge sign changes both its sine integral and its charge weight. Hence all 2^R unit-sign contributions agree, rather than merely having the same modulus. The raw source sign and midpoint parity cancel:

    (-1)^(dR) (-1)^((N+1)R) = 1.

This leaves precisely (-2i)^R and the unwrapped q phase. Neither even levels nor mixed signs of the fixed powers force cancellation of this leading packet.

## 6. Independent endpoint-current and whole-tail check

For an entire polynomial in the spectral variables, let B(t) include the sine, the quadratic chirp and the remaining source. At t=±1/2 it has B=0. Its first derivative there is just -2pi times the same spectral value times the same chirp value, so the first derivatives agree, also after spectator differentiation. Three integrations by parts yield

    integral B(t)e^(k t)dt
       = k^-3 ([B''(t)e^(k t)] - integral B'''(t)e^(k t)dt),
    k=2pi i N ell.

The sign in O is correct. The second-derivative boundary current is not zero and is retained. With the original ell weight, the resulting ell^-2 decay makes the whole-domain series absolutely convergent at each fixed N. This does not assert uniform-in-N constants yet.

For the shifted bad coordinate t=±1/2+iv, the source values coincide by periodicity, and the two sines are both -i sinh(2pi v). Subtracting the quadratic chirps gives exactly

    B(1/2+iv)-B(-1/2+iv)
      = 2i sinh(2pi v) sinh(pi n N v)
        exp(pi i n N(1/4-v²)) C_N(1/2+iv,...).

The endpoint Fourier phases are equal, and the midpoint character changes their common sign to (-1)^ell. The absolute paired factor is at most C|n|N v² exp(pi|n|Nv). Thus the original charge weight and H2 bound give the vertical majorant

    C_n |n|N ell exp(N(Phi-gamma))
      product_(spectators) |ell_j|^-2
      integral_0^tau v² exp(-2pi N(ell-|n|/2)v)dv.

For ell>|n|/2+D the integral is bounded by C/[N³(ell-|n|/2)³]. The remaining ell series is summable. Spectator integrations by parts are on their entire real intervals. Gaussian derivatives there cost polynomial powers of N and fixed n; they create no exponential cost proportional to an unbounded spectator power. Source derivatives use H2 on smaller fixed strips. This is why the pair must be combined before estimating and why the real-spectator H2 scope matters.

For the shifted horizontal interval, the shared real supremum and the degree-d cosine bound give exponent at most Phi+o(1)+2pi R tau−2pi tau(ell−|n|/2). A fixed D>R with sufficient margin removes the whole infinite far-charge union, independently of power ratios. All other coordinates can be summed by the spectator ell_j^-2 factors. No infinite sharp-cube series is ever introduced.

The remaining charge set is finite for fixed powers. If one ratio ell_i/|n_i| exceeds a, use the inner cube and shift only that coordinate by ib/|n_i|. The horizontal chirp-plus-charge loss is at least 2pi b(a−b). On its vertical sides the same chirp-plus-charge real part is nonpositive and the source has a fixed real quadratic loss. The source complex error Cb²/n_i² is absorbed by increasing n0. Outside the inner cube H2 applies on the original real domain.

Finally use the outer cube for the finite local charges. The critical-value derivative above separates every nonunit magnitude. The limiting unit loss from Phi is O(sum n_e^-2), so n0 can be enlarged until it is smaller than all previously fixed exterior, far, bounded-bad and connector losses. All constants are chosen in this order before N tends to infinity. This proves the nonzero whole-period asymptotic under H1/H2 with the claimed fixed signed-power scope.

## 7. Exact limits of this audit

This is an analytic implication and dependency audit, not a new proof of the original coproduct/Casimir identities or the labeled metric certificate. Their actual source forms were read and retained. The source-grid adapter is being audited by the parent, Appendix N by another agent, and the marked metric/volume half of O by the geometry agent. I checked their analytic interfaces without replacing those tasks.

The imported positive q-Hahn pair-trace theorem and absolute geometric action calibration remain earlier written inputs. I read how they enter the finite determinant/graph and phase proofs; I did not newly rederive every matrix entry or every facet-coning identity in this pass. The new charge argument is independently derived above, and its use of the whole shared strip and exact current is explicit.

No full source estimate for arbitrary unchanged matched spheres follows from O. The correct output is a nonzero all-central contribution at the actual filled action. An independent strict complementary-source estimate is still necessary to prevent cancellation in the full invariant. There is no growing-diagram, growing-power-with-level, fixed short-power, or general moving-meridian theorem asserted by this audit.
