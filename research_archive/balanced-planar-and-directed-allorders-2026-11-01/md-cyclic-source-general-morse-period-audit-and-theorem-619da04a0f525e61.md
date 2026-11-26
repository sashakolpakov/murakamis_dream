# The full long-filling period after balanced terminal decoration

This records the analytic dependency check for the exact source in *md-cyclic-source-terminal-fan-morse-adapter*. The claim concerns the original complete-main-color invariant. It does not extend the moving-main or filtered-characteristic theorems.

## 1. A precise theorem

Let \(D\) be a fixed connected augmented link diagram with the following data.

* Its white triangulation is a simple sphere, with the original perfect matching of dual triangles and four distinct white vertices at each matched quadrilateral.
* Its original projection/crossing-disk cut has the supplied labeled nondegenerate positive right-angled certificate.
* A MAIN edge is marked; the associated two protected white curvatures are zero in the actual marked complete packing.
* The cyclic order, original half-twist frame and disk-framed meridian/longitude at every crossing-circle port are fixed.
* A parity vector for the original boxes makes their filled main strands a knot, with no internally closed extra component.

There is a finite literal terminal decoration \(\widehat D\) of this diagram with even numbers of new terminal pieces on both sides of each original box such that:

1. The original endpoint pairing and knot condition are preserved when each new terminal power is odd.
2. The refined white sphere is simple, has its actual positive cut certificate, and its one marked complete packing satisfies the strict complete-radius balance inequalities at every old and new port.
3. There is a threshold \(T(\widehat D)\) such that, for every fixed integer filling vector \(p\) with all \(|p_e|\ge T(\widehat D)\), independently in sign and size, and the recorded retained half twists \(\epsilon_e\), the actual powers \(n_e=\epsilon_e-2p_e\) produce a hyperbolic knot \(K_p\) and
\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K_p)|
       =\operatorname{Vol}(S^3\setminus K_p).
 \tag{1}
\]
Here \(K_N\) is the original zero-framed reduced complete-color invariant at \(q_N=e^{\pi i/N}\), with its recorded enhanced component convention. Both parities of \(N\) occur. The same logarithmic conclusion holds in the specified full one-cut modified convention after retaining its known polynomial-level conversion.

The diagram, decorations and signed powers are fixed before \(N\). The threshold may depend on the whole decorated diagram; there is no uniform bound over all cores or a growing-diagram limit. The core's original powers are also filled sufficiently long in this theorem. The result is not an assertion for arbitrary short fillings of the core. The decorated knot generally differs from the core knot.

The geometric existence of the decoration is the two-sided construction in *md-cyclic-geometry-balanced-terminal-fans*. The finite source is the orientation-corrected *md-cyclic-source-terminal-fan-morse-adapter*. The latter identifies the new first-side quartet as \((b,y,w,x)\), so its actual homogeneous factor is \(H_g(b,y,x,w)\).

## 2. Source hypotheses which have actually been checked

Write \(R\) for the number of ports of the decorated diagram, \(d=N-1\), and let \(\Phi=\operatorname{Vol}(Y_{\widehat D})/(2\pi)\). The local full spectral numerator has degree at most \(d\) in each spectral argument, and the exact whole source is
\[
 S_N(\boldsymbol\sigma)=
 \left[\prod_{f\ne u,v}L_f^d\right]
 \left.\prod_eH_{V_N(\sigma_e)}\right|_{L_u=L_v=0}.
 \tag{2}
\]
The proof retains actual endpoint zeros before modular reduction, all original port frames, the unrestricted mark until whole-source conservation, the even-level coset, and the \(N^{-1}\) per new coupon cancelled by the new primitive face grid. Thus (2) is not an assumed extension of flat-plat wording.

The exact crossing functional on (2) is the original whole-domain Fourier/Hermite formula. Its outer scalar is
\(q_N^{d^2\sum n_e/4}(-i)^R\), its charge weight is
\(\prod_e\ell_e(-1)^{(N+1)\sum\ell_e}\), and its integrand includes every
\(\sin(2\pi\delta_e)\). The spectral substitution is
\(\sigma_e=-2\cos(2\pi\delta_e)\).
Charge zero is absent by the matrix identity. The external final-diagram framing/component character remains outside this raw period.

Only the full numerator is a physical box object. CROSS is selected afterward by the exact polynomial path partition and linearity of (2). No claim that CROSS is an independent Hopf coupon is used.

## 3. Finite-\(N\) packet and nonzero amplitude

The proof of *research_general_morse_cross_action*, section 4, supplies the exact all-CROSS inputs H1 and H2 for (2), rather than using the older full-numerator restoration. The ordinary graph remains connected after deleting the two adjacent protected vertices. Its active angular rows are primitive differences. Hence the common-phase point is unique after fixing one phase, and no extra lattice multiplier appears.

The positive finite-face Hessian has dimension \(R-1\). The local cofactor identity is the original \(N^2\mathcal B_{e,N}\) at every port, with all forced factors, beta normalizers, midpoint offsets and parity. It gives
\[
 C_N^{\mathrm{raw}}(\delta)=
 \frac{(-1)^{dR}N^{2R}e^{NA_N(\delta)}}
 {(2\pi N)^{(R-1)/2}\sqrt{\det H_N(\delta)}}(1+O(N^{-1})).
 \tag{3}
\]
The phase \(A_N\), not merely its limit, remains in the exponential. It is separately even and real on the real local chart. The selected face saddle is obtained by its unique implicit branch, so these properties survive elimination. On a smaller fixed complex chart,
\[
 \partial_iA_N(\delta)=-2\delta_iB_{i,N}(\delta^2),
 \qquad B_{i,N}\longrightarrow B_i,\qquad B_i(0)=C_i>0 .
 \tag{4}
\]
All fixed derivatives converge. The determinant root is continued from the complete positive Hessian. There is no scalar phase from a newly reset cup frame: those phases were already accounted for in (2).

The proof of *general_localized_unit_charge_filling_period*, sections 2–4, then applies to the actual restricted real cube. For \(t_i=\ell_i/n_i\),
\[
 \delta_i=-\frac{t_i}{1+iB_{i,N}(\delta^2)/(\pi n_i)},
 \qquad
 \Im\delta_i=
 \frac{\ell_i}{\pi n_i^2}
 \frac{\Re B_{i,N}}{|1+iB_{i,N}/(\pi n_i)|^2}>0
 \quad(\ell_i>0).
 \tag{5}
\]
All signs of \(n_i\) are allowed. The exact multiplicative formula avoids an additive error depending on another, shorter slope. Its Hessian has positive real Gaussian part. Translation of the closed real cube retains every side face; those faces are exponentially lower by the source's real Hessian bound and the small scaled charges. The translated saddle has coefficient \(+1\).

For fixed powers and charges, the sine factors at that saddle are nonzero, and both determinant roots are units. The amplitude converges to a nonzero number. The source and spectral integrations contribute exactly
\[
 N^{2R}(2\pi N)^{-(R-1)/2}(2\pi/N)^{R/2}
       =\sqrt{2\pi}\,N^{R+1/2}.
 \tag{6}
\]
Thus no unknown stationary coefficient is being inferred from existence of a critical point.

Reflection of a charge reverses its sine factor and its charge multiplier simultaneously. The exact separately even source and quadratic phase are unchanged. Therefore the \(2^R\) sign-unit contributions are exactly equal before asymptotic approximation. Their parity factor cancels the \((-1)^{dR}\) in (3), because \((N+1)R+dR=2NR\). This is the noncancellation argument at both level parities.

## 4. All charges, including the actual endpoint currents

The global CROSS estimate is a bound for the shared coefficient, uniformly with arbitrary real spectator spectra. It has a strict thin-strip loss whenever one real coordinate is separated from zero. This is the input used by *general_all_cross_long_filling_volume*, not a factorwise norm estimate.

On the original whole interval, the sine factors vanish at both endpoints and the first derivatives match. Three integrations by parts give a second-derivative endpoint difference plus a third-derivative integral. After the original charge weight, every spectator has an absolutely summable \(|\ell_j|^{-2}\) bound. Source derivatives use the fixed strip; Gaussian derivatives are taken on real spectators. This does not introduce \(e^{c|n_j|N}\) from an unnecessarily complex spectator contour.

For a far positive charge, shift only its whole interval by \(i\tau\). The two endpoint currents pair exactly through
\[
 2i\sinh(2\pi v)\sinh(\pi n_iNv)
 e^{\pi i n_iN(1/4-v^2)}C_N(1/2+iv,\delta_{\ne i}).
 \tag{7}
\]
This has a \(v^2\) zero at the bottom. With the actual charge factor, its tail is bounded by
\[
 \operatorname{poly}(N)e^{N(\Phi-\gamma)}
 \prod_{j\ne i}|\ell_j|^{-2}
 \frac{\ell_i}{(\ell_i-|n_i|/2)^3}.
 \tag{8}
\]
The last factor is summable once \(\ell_i>|n_i|/2+D\). The horizontal translate uses the full polynomial Bernstein bound and is geometrically summable beyond the same cutoff, with \(D\) depending on the fixed graph. A union bound handles more than one far coordinate. No infinite sharply localized charge series is introduced.

The remaining charge set is finite after the powers are fixed. A charge with some \(|\ell_i|/|n_i|>a\) has a gap outside a small cube by the global spectral estimate; inside that cube a one-coordinate shift \(b/|n_i|\) gives a fixed loss. Every new side current is retained, and the source Taylor error is quadratic because \(A_N\) is real on the real chart. This estimate imposes no ratio restriction on the slopes.

For the remaining local positive charges, exact envelope differentiation of (5) gives
\[
 \Re S_{N,\mathbf1}-\Re S_{N,\boldsymbol\ell}
 \ge\sum_i\frac{C_i}{2n_i^2}(\ell_i^2-1).
 \tag{9}
\]
Every nonunit vector in that finite set therefore has a strict fixed-power loss. The first-charge action tends to \(\Phi\), with drop
\(O_{\widehat D}(\sum_i n_i^{-2})\). A single diagram-dependent lower threshold makes this drop smaller than the finitely many far-charge, side-current and spectral losses. The full all-CROSS period is consequently its nonzero first-charge asymptotic.

None of these estimates uses a flat-plat ordering. The necessary finite phase, degree, separate evenness, Cauchy measure, shared endpoint gap and original endpoint factors have been supplied above.

## 5. Restoring the full numerator

At the actual complete packing the two-sided fans give strict balance. The original global weighted LEFT and RIGHT estimates therefore have a fixed local loss against the port's complete action. They are uniform over the same face torus and all real spectral arguments. A protected zero kills the corresponding overloaded polynomial exactly.

Extracting the one original target from the product gives a full noncross gap at rate \(\Phi-\gamma\). This uses the same actual face radii at every factor and their calibrated target subtraction. Finite spectral degree extends it to a thin strip. The whole-domain integration-by-parts argument just described bounds the entire noncross Fourier period by
\[
 C_{\widehat D}\prod_i(1+|n_i|)^3
             e^{N(\Phi-\gamma')}.
 \tag{10}
\]
For sufficiently long fixed powers, this is exponentially smaller than the first-charge action. No flat pure-middle forest or identity-smoothed source theorem is used to restore the remainder.

This is why the local coefficient counterexamples to a universal LEFT/CROSS comparison do not obstruct the decorated theorem: the fan construction establishes the actual common-radius strict inequalities, not a false coefficientwise domination for every radius.

## 6. The actual primitive filling and normalization

The geometric extension in *md-cyclic-geometry-cut-and-morse-packet-interface*, section 6, has been checked against *research_general_morse_cross_action*. One common marked circle pattern supplies the white reflections. At an arbitrary Morse slice, the based heads telescope; inserting a cup/cap produces a pair whose product is the identity. Every original ordered coupon retains its local collar. Consequently cycles in the matching graph do not introduce freely selected conjugating frames.

The actual selected peripheral logarithms are
\[
 J_e=-e^{-2\pi i\delta_e},\qquad
 U_e=-\log R_{0,e}-\epsilon_e\log(-J_e),\qquad
 V_e=2\log(-J_e)=-4\pi i\delta_e.
 \tag{11}
\]
The half-twist term appears once. At the source first charge,
\[
 U_e+p_eV_e=-2\pi i,\qquad n_e=\epsilon_e-2p_e .
 \tag{12}
\]
The refined positive certificate anchors the complete representation and its absolute volume. Marked local gluing rigidity identifies the nearby branch; independently sufficiently long fixed fillings give the original smooth primitive filling. The boundary correction in the regulator cancels exactly the Gaussian and linear filling terms. Thus the critical action is the volume of the actual refined filled exterior, not an inferred volume of a formal saddle.

The raw contraction is converted using the final diagram's original framing/component character. For a knot this changes only its recorded unit phase/sign. In the full one-cut modified convention retain the extra \(i^{N+3}/N\); it has zero exponential rate. No extra mark, \(N^R\), quantum dimension, or spectral Jacobian is inserted.

## 7. Remaining limits

At the stated hypotheses no additional analytic or source assumption remains in the complete-main-color long-filling conclusion. The decoration sizes depend on the actual complete packing, and the filling threshold depends on the final fixed diagram. This argument says nothing about cores lacking the supplied simple-white positive certificate, about undecorated cores, about short powers at the core boxes, or about a moving-main-meridian profile. The exact cycle-source and operator obstructions remain relevant to extensions that do not create balance; they are not used as an upper model for this theorem.
