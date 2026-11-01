# Bounded audit of the recursive filling argument

This report concerns the recursive completed-root theorem in manuscript Chapters 05, 06, and 08, with the corresponding finite and analytic appendices. It is an independent literal read of the current formulas and their analytic interfaces. It is not a proof audit of every later volume family, a formal verification of the manuscript, or a fresh reconstruction of its marked hyperbolic metric.

The inspected publication checkout began at commit c5d9c851c672b941bdbbec51da50d8f1a5c2cf12. Source hashes and the exact reading boundary are recorded separately. No public file was edited by this audit.

## 1. Outcome and two contour clarifications

I found no unresolved fatal error in the analytic transfer from the stated exact corridor packet and whole-source gaps to the nonzero long-filling asymptotic. The proof keeps the original finite sum, handles the infinite charge tails before using the local saddle, retains endpoint currents, and permits independently unequal positive or negative fixed slopes. The action obtained at the first charge is algebraically the marked action of Chapter 07.

Two compressed contour statements needed explicit justification.

1. The opening of the filling-contour section originally explained persistence of a real Fourier gap in a complex strip by the cost of an imaginary displacement on the physical support. A bound on an already canceled real sum does not by itself imply that conclusion. Rerunning the exact cotangent rectangle with a complex Fourier parameter does imply it. I supplied the complete replacement argument; the root has integrated it into the public manuscript.
2. The local connector paragraph did not explicitly distinguish an outer source box from the smaller charge-ratio box. The needed choice order is: first choose the outer Fourier-packet box, then a much smaller ratio radius, then the reciprocal-slope bound. The joining faces have a uniform absolute loss below \(F_0\). Only the first-charge integral needs a relative asymptotic; for a higher local charge, its saddle term plus a separate exponentially small absolute connector error suffices. The precise replacement paragraph is now integrated. The root also added the required real Fourier estimate outside the outer box; the chirps have modulus one on that unshifted real complement.

Neither clarification requires a new source estimate or a comparison between different slopes. Both can be proved directly from the existing fixed-domain holomorphic packet and exact finite Fourier polynomial.

The new transfer proposition in Chapter 09 is correct. When using it here, its subexponential factor \(a_N\) must absorb the first-charge relative factor \(1+O_{\mathbf p}(N^{-1})\). That relative correction has the same exponential rate as the first charge and must not be put into the exponentially smaller remainder \(E_N\). The proposition's statement allows precisely this choice.

## 2. What was read, and what remains an input

I read all of:

- Chapter 05, the core/alias coefficient envelopes, block and attachment estimates, whole-tree tangent induction, and physical-color gap.
- Chapter 06, the exact finite corridor definition, selected shear, lattice offsets and normalization, nonzero amplitude, and complex Gaussian bound.
- Appendix B1, including the canonical Gamma product, exact finite signed sum and endpoint recurrence, continued-fraction interpolation, optimal Euler–Maclaurin comparison, action/shear identification, and primitive finite-lattice saddle.
- Appendix B2, including the global recurrence, spectral ellipse, collision-safe frozen-block estimate, singular lower endpoint, and macroscopic-color loss.
- All of Chapter 08 and the filling-contour section of Appendix B.
- The Fourier–Hermite portion of Appendix A and the exact-filling portion of Chapter 02.
- Chapter 07's action and peripheral formulas, for consistency of the final analytic identification.
- The new transfer proposition and dependency explanation in Chapter 09.
- The statement and construction scope of the recursive theorem in Chapter 01.

This read checks how the hypotheses are supplied and used. It does not independently replay the 288- and 880-inequality alias certificates, rederive every rational \(q\)-identity in B1 from scratch, or reconstruct all diagrammatic source/cup/pivot identities. Those remain the named finite-source and arithmetic inputs. It does not independently prove the strict complete optimizer and port bounds from the geometric construction, or the full marked completion and regulator theorem of Appendix D. The final volume identification is conditional on those written geometric proofs in exactly the way stated in Chapter 09.

The recursive proof continues to require a completed root on both sides of the closure and high complete leaf indices in a compact subinterval of \((1/4,1/2)\). Nothing read here licenses changing that grammar or importing a later circle-tree criterion into this proof. The separate isolated three-leaf calibration keeps its own source argument.

## 3. Whole-source removal and the order of limits

The exact Hermite expansion is
\[
 R^{-2p}=\kappa^{-2p}\sum_{j=1}^N\beta_{j-1}^{-p}L_j,
 \qquad \sum_j|\beta_{j-1}^{-p}|\le2N(1+|p|).
\]
For a fixed number of circles and a fixed signed filling tuple, applying this expansion to the source comparison multiplies an absolute error only by a polynomial in \(N\). The constants may depend on the fixed slopes. No uniform statement as the slopes vary with \(N\) is needed or obtained.

The global errors in Chapters 05 and 06 are at rate \(F_0-\gamma\), whereas the selected filling action is slightly below \(F_0\). Thus those source bounds alone do not prove the filled result. The proof correctly postpones the comparison until the first-charge action is known and then increases the fixed lower bound on each \(|p_i|\). Analyticity in the independent reciprocal slopes gives uniform convergence of the selected real action to \(F_0\) on a small product box, which justifies one threshold with no ratio restriction.

The core envelope in Chapter 05 is an exponential-rate bound with a uniform \(o(1)\), not a polynomial-prefactor bound through all recurrence collisions. B2 fixes the positive block loss first and only then absorbs that uniform \(o(1)\). This is the correct order. A polynomial number of states and a fixed number of alias subsets do not erase a fixed exponential margin.

The source is compared with the corridor before an even extension is introduced. In particular an alias is never assumed to be even in a complementary color. This distinction is necessary for the exact folded Fourier identity.

## 4. The local source input is strong enough for two oscillatory transforms

The exact corridor is a finite sum on one fixed rectangular primitive wire window. The continued color factors retain the literal finite signed sum and their prescribed quadratic phases; the gate factors remain exact on the integer wire grid.

The continued fraction in B1 is used to construct an index interpolant with exponential grid error. Its selected root has a fixed modulus separation on the high interval. At the physical terminal row the exact zero in the second recurrence coefficient erases the arbitrary analytic tail of the continued fraction. This is the reason the interpolant represents the actual finite source rather than an unrelated homogeneous recurrence solution.

The subsequent Euler–Maclaurin construction truncates at order proportional to \(N\) while retaining a fixed complex derivative margin. Its exponential error is compared with the source before any oscillatory cancellation. The separate leading expansion of that holomorphic interpolant is then used for stationary phase. These are distinct steps; the manuscript does not substitute a pointwise \(1+O(N^{-1})\) grid approximation for an exponentially accurate interpolation.

The wire lattice has primitive integer coordinates and fixed offsets from \(d=N-1\). Its count is \(K=2H-3\), and the summand power is \(N^{3-H}\). Thus its Gaussian gives \(N^{3-H+K/2}=N^{3/2}\). Offsets enter the amplitude at the moved critical point. The complete signed multiplier is explicitly nonzero, so shrinking the color polydisk makes the leading amplitude nonzero throughout it.

The exact corridor therefore has a holomorphic relative expansion
\[
 C_N(t)=N^\mu a(t)e^{N\varphi(t)}(1+r_N(t)),
 \qquad \mu=\tfrac32,\qquad r_N=O(N^{-1})
\]
on a fixed complex neighborhood, with \(a\ne0\). The error is holomorphic there, and Cauchy estimates on a smaller domain bound its derivatives. This is sufficient to carry the same remainder through both the color Fourier saddle and the later filling saddle. A real-grid relative estimate would not have been sufficient.

Separate evenness is exact for the finite corridor and for its leading action. It forces the color-wire mixed Hessian at completeness to vanish and gives
\[
 \varphi''(0)=2\pi i\,\operatorname{diag}(\tau_i),\qquad
 \tau_i=\frac{iX_i}{1-\epsilon_i iX_i},\qquad \Im\tau_i>0.
\]
These entries are nonzero and have negative real part after multiplication by \(2\pi i\). They supply both the local inverse and the real Gaussian decay.

## 5. Finite Fourier contours and complex strips

The Fourier polynomial
\[
 \mathcal F_N(z)=\sum_{|h_i|\le H_N}C_N(h/N)e^{2\pi i h\cdot z}
\]
is finite and periodic at every level. The noncentral bound uses the unscaled half-grid rectangle and the kernel
\[
 \pi\cot(\pi w)-i\pi=\frac{2\pi i}{e^{2\pi i w}-1}.
\]
The upper and lower sides are paired with respectively \(\phi\) and \(2\pi-\phi\); on a vertical half-integer line the kernel is bounded and the fixed real boundary of the color window supplies a source loss. Choosing the height small relative to both horizontal and real-boundary losses yields an exponential gap. Fixed powers of \(h\) only affect polynomial factors.

For the required complex Fourier coordinate \(z_i=x_i+iv\), use the same contour with \(\phi\) replaced by \(\phi+2\pi iv\). The extra modulus is
\[
 |e^{-2\pi v w}|
 \le e^{2\pi(\delta N+1/2)|v|}
\]
everywhere on that unscaled rectangle. A sufficiently small fixed \(|v|\) therefore preserves half the real gap. The contour in the color variable remains within the given holomorphic source tube. Other Fourier variables stay real, so summing their finite colors and differentiating a fixed number of times costs only powers of \(N\).

This direct contour proof is the corrected justification for the strip statement. It is important that no estimate is inferred by multiplying the modulus of a canceled real Fourier sum by a coefficient envelope.

For the central Fourier packet, the finite cotangent formula yields the ordinary finite integral plus exponentially small nonconstant modes and boundaries. The stationary point solves
\[
 \nabla\varphi(\xi)+2\pi iz=0.
\]
Its Legendre transform has
\[
 \Psi(z)=\varphi(\xi(z))+2\pi i\xi(z)\cdot z,\qquad
 \Psi(z)=F_0-\pi i\sum_i z_i^2/\tau_i+O(\|z\|^4).
\]
The second statement follows by solving the linearized critical equation; separate evenness eliminates cubic terms. Shrinking the \(z\)-polydisk makes the selected action lie above every fixed boundary error. The exact holomorphic source, rather than a real approximation to it, is integrated. This gives the stated \(N^{\mu+b/2}\) Fourier power and nonzero amplitude \(B\).

## 6. Poisson charges, endpoint currents, and tails

The Hermite derivative and value terms form the displayed sampled derivative of
\[
 U_N(z)=e^{2\pi iPNz^2}\sinh(2\pi iz)\mathcal F_N(z).
\]
Its values at both endpoints vanish, and its first derivatives agree there. Thus the periodic extension of \(U_N'\) has sufficiently decaying Fourier coefficients for the finite-level Fourier selection. The midpoint selection factor is
\[
 e^{2\pi i mN((k+1/2)/N-1/2)}=(-1)^{m(N-1)}.
\]
Integration by parts produces the factor \(m\); the zero charge vanishes exactly from the endpoint values. No normal term is discarded.

I checked the boundary-current mechanism directly. Periodicity gives the exact identity
\[
 U_N(1/2-iv)-U_N(-1/2-iv)
 =-2e^{2\pi iPN(1/4-v^2)}
       \sinh(2\pi v)\sinh(2\pi PNv)\mathcal F_N(1/2-iv).
\]
It has a double zero at \(v=0\), including \(P=0\), where it vanishes identically. The fixed-strip Fourier loss consequently gives
\[
 |V_N(v)|\le\operatorname{poly}(N,P)v^2
 e^{N(F_0-g_1)+2\pi|P|Nv}.
\]
After the charge factor \(e^{-2\pi mNv}\) is included, the Laplace integral of \(v^2\) yields the summable bound proportional to
\[
 \frac{m}{N^3(m-|P|)^3}e^{N(F_0-g_1)}.
\]
The horizontal shift has exponent
\[
 F_0-2\pi\sigma(m-|P|-\delta).
\]
Both statements are uniform once the source strip is fixed. Individual vertical sides are not zero; pairing them is essential.

The multivariable telescoping product leaves every other filling functional on real grids or real finite integrals. Its chirps have modulus one there. Fixed derivatives of the source obey the same noncentral gap with polynomial losses. Therefore no tail estimate incurs \(e^{N|p_j|}\) from an unrelated cusp. The remaining number of charges depends on the fixed slopes but not on \(N\).

The Cartan ledger is consistent: inserting \(P_i=-p_i\) into the sampled derivative contributes \(\kappa^{p_i}\), which combines with the original \(\kappa^{-2p_i}\) to give \(\kappa^{-p_i}\) in the full charge formula. The retained \(\chi_N,\eta_N\) remain external unit factors.

## 7. Local charges with unequal signed slopes

Put \(e_i=1/p_i\) and \(t_i=m_i/p_i\). The equations
\[
 z_i=-\frac{t_i}{2}+\frac{e_i\Psi_i(z)}{4\pi i}
\]
have derivative equal to the identity at \(e=0\). They have one holomorphic branch on a fixed product neighborhood of \((t,e)=(0,0)\).

Completing the square writes the critical action as
\[
 T_m(z_m)=\frac{\pi i}{2}\sum_i\frac{t_i^2}{e_i}
              +\widehat B(t_1^2,\ldots,t_b^2,e).
\]
The apparently singular first term is purely imaginary for real signed slopes. The remainder is holomorphic at every \(e_i=0\), because \(z_i+t_i/2\) is divisible by \(e_i\). Separate evenness makes it even in each \(t_i\). Its derivative in \(t_i^2\) at the origin is
\[
 -\frac{b_i}{4},\qquad b_i=\frac{\pi\Im\tau_i}{|\tau_i|^2}>0.
\]
Continuity on a smaller real product box gives the upper bound \(-b_i/8\). Integrating from the first-charge squared coordinate \(e_i^2\) to \(m_i^2e_i^2\) proves the manuscript's charge gap. This uses no expansion whose error is compared with a smallest slope, and no ratio of distinct slopes.

The exact factorization
\[
 z_i=-\frac{t_i}{2(1-e_iQ_i(z)/(4\pi i))}
\]
shows that a nonzero local charge has \(z_i\ne0\). On the small neighborhood it also has \(\sinh(2\pi iz_i)\ne0\). The Hessian on the translated real tangent space has
\[
 \Re T_m''(z_m)=\Re\Psi''(z_m),
\]
because the real signed \(p_i\) occur only in the imaginary diagonal chirp. This remains negative definite on a fixed source neighborhood. Consequently the local Gaussian is nondegenerate for every choice of signs.

For completeness, the rigorous local connector choice is the following. Choose an outer box \([-a,a]^b\) with a fixed complex thickening in the Fourier-packet domain. Next choose \(t_0\ll a\), and then restrict every \(|e_i|\). Every joining face of its translation to the critical point has some \(|x_i|\ge a/2\), and
\[
 |y_i|\le C|e_it_i|,\qquad |p_iy_i|\le C|t_i|,
 \qquad |m_iy_i|\le Ct_i^2.
\]
The source quadratic bound and the exact real chirp therefore give
\[
 \Re T_m(x+iy)\le F_0-c\|x\|^2+
          C_1\|x\|\|t\|+C_2\|t\|^2\le F_0-g_a.
\]
This holds on intermediate joining faces in coordinatewise translation as well. On the translated real box, the exact critical equation and negative real Hessian give a strict Gaussian centered at \(z_m\).

A higher local-charge integral is therefore its local saddle contribution plus a separate absolute connector error at rate \(F_0-g_a\). It is unnecessary to assert that each such error lies below that higher saddle. The first-charge action tends to \(F_0\), so one common threshold puts it above the connector error. The other local saddles lie below it by the exact squared-charge comparison. For a fixed filling tuple their smallest positive gap is still fixed as \(N\) tends to infinity.

## 8. Nonlocal finite charges

If \(|m_i/p_i|\ge t_0\), on \(|x_i|\le t_0/4\) the quantity \(m_i+2p_ix_i\) has constant sign and absolute value at least \(|p_i|t_0/2\). Choosing the imaginary displacement with the opposite sign makes the real filling exponent decrease at rate at least \(\pi |p_i|t_0\) per unit height.

The finite source on this displaced interval costs at most \(e^{2\pi\delta N|v|}\) before cancellation. For sufficiently large \(|p_i|\), the chirp decrease dominates that cost. At the two joining segments, the real Fourier coordinate is a fixed distance from an integer, and the corrected complex-strip estimate supplies a fixed source loss. The chirp decreases on those joins too. Outside this small interval the real noncentral Fourier bound applies without any deformation.

All spectator coordinates stay real in this argument. Thus it gives a fixed absolute loss for every nonlocal charge, with no uncontrolled dependence on another slope. Only finitely many such charges remain after the already proved tails. Increasing the threshold puts the first-charge action above this fixed error level.

## 9. Noncancellation, normalization, and action

For each coordinate, reversing \((m_i,z_i)\) to \((-m_i,-z_i)\) preserves the exact integral with its factor \(m_i\sinh(2\pi iz_i)\). The separate evenness of the exact Fourier polynomial is used here. Thus the \(2^b\) first charges are equal as complex numbers before taking asymptotics. They add; they are not merely asserted to have equal moduli.

The parity factor is also exact:
\[
 (-1)^{bd+d\sum_i m_i}=1\qquad(|m_i|=1),
\]
since \(\sum_i m_i\equiv b\pmod 2\). There is no parity subsequence cancellation.

The second Gaussian contributes \(N^{-b/2}\) to the Fourier power \(N^{3/2+b/2}\), leaving \(N^{3/2}\). Its amplitude has the displayed factors \(2^b\), \(B(z_*)\), the nonzero hyperbolic sines, and the nonzero determinant. The Gaussian square roots are determined by the actual translated real contours; arbitrary square-root choices are not available.

Finally
\[
 \Psi_i=2\pi i\xi_i,\qquad
 \xi_i=1+2p_i z_{*,i}
\]
at the first-charge saddle. Direct substitution gives
\[
 T_{\mathbf1}(z_*)=
 \varphi(\xi)+\frac{\pi i}{2}\sum_i\frac{(\xi_i-1)^2}{p_i}.
\]
With Chapter 07's \(U_i=-2\pi i\xi_i\) and \(V_i=-2\partial_i\varphi\), its critical equation is exactly \(U_i+p_iV_i=-2\pi i\). This verifies the analytic-to-marked-action algebra, including its sign and factor of two.

The remaining equality of this action's real part with the intended knot-complement volume uses the separately proved marked representation, primitive collar, additive regulator normalization, and smooth completion. Those are essential geometric inputs, not consequences of the present saddle audit.

## 10. Chapter 09 transfer proposition

The proposition's hypotheses are sufficient as written. If \(G_N=a_Ne^{N\mathcal A}\), \(a_N\ne0\), and \(N^{-1}\log|a_N|\to0\), while the entire remaining error has a strictly smaller upper rate, then the reverse triangle inequality proves eventual nonvanishing and the stated logarithmic limit. The small parameter choice \(\eta<\Delta/3\) is adequate.

For Chapter 08, take \(G_N\) to contain the complete first-charge local integral, including its relative \(1+O_{\mathbf p}(N^{-1})\) correction. Take \(E_N\) to contain other charges, connector terms, Fourier interpolation boundaries, and source restoration errors. The preceding estimates give a strictly smaller rate for this \(E_N\), after the common long-slope threshold is fixed. The unit framing factors may be placed in \(u_N\).

The Chapter 09 dependency map does not use a local geometric contribution as if it were the whole invariant. Its separate weak-balance discussion likewise explicitly requires a full real-cube remainder estimate before applying the finite filling norm and transfer proposition. I found no mismatch in those newly added analytic statements.

## 11. Explicit limits of this audit

- No claim here formally verifies the infinite-dimensional analytic arguments in Lean.
- No new numerical test is being used as evidence for a saddle or an exponential gap.
- The alias certificates and exact source identities remain proof dependencies rather than silently being replaced by this read.
- The geometric optimizer, marked representation, regulator, and primitive filling completion remain separately checked geometric inputs.
- The independent long-slope claim means one fixed threshold and then fixed signed integers; it does not mean estimates uniform when slopes vary with the level.
- Nothing here proves a new volume class or extends the recursive grammar.

The two saved contour paragraphs are local proof clarifications, both now integrated. Chapter 09 now explicitly keeps the relative first-saddle correction inside \(a_N\). The final hash record states the exact manuscript versions read.
