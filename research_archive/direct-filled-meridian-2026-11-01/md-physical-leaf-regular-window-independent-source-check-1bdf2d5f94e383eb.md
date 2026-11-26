# Independent check of the physical leaf regular-window proof

Private report, 1 November 2026. The checked source is `/private/tmp/md-physical-leaf-main-meridian-regular-window.md`, SHA256 `ff202a7c08b410a618e2211584b4380cd6f2580821d4e4b04c6154dcdfe05c56`. I read Sections 1–10, including (28a), against the actual fixed-frame turn and the canonical factorial product in `notes/exact_factorial_interpolation_and_complex_contours.md`. No repository source was changed. I found no mathematical or source-normalization defect.

## Exact physical identities

The coefficient extractor is the full fixed-metric identity
\[
 [e_r]T_sF=\gamma_N(s)\frac{W_{d-r}(s)}{H_N(s)}\phi_s(e_rF)
 =\gamma_N(s)\frac{H_N(s)}{W_r(s)}\phi_s(e_rF).
\]
The second equality uses the exact paired reflection, not an asymptotic. For a pure physical circle, degree at most \(2N-2\) makes the single quotient correction have degree at most \(N-2\). Hence it cannot affect the closing top coefficient. This proves the pure identity even when its complete coefficient is zero.

At a moving root \(z=-2\cos\tau_a\), direct differentiation gives
\[
 P_s'(z)=(-1)^dN\frac{\sin(N\tau_a)}{\sin\tau_a}.
\]
The actual ordinary pivot gives \(L_j(z)=\sin(j\tau_a)/\sin\tau_a\). Thus the generic-root trace is
\[
 \phi_s(e_rR_s^\epsilon L_j)
 =N\sum_a e_r(-2\cos\tau_a)(\kappa_s\lambda_a)^\epsilon
       \frac{\sin(j\tau_a)}{\sin(N\tau_a)}.
\]
For \(j=N\), this is exactly (11). The full crossing exponent completes the square to (10), including \(q^{\epsilon(d^2/4-s^2/2)}\). The repeated-root assertion follows from this holomorphic identity; it does not discard first normals. The same argument permits a raw product of any fixed number of low Newton factors inside the trace.

For a physical deficit \(h=N-j\), the displayed sine subtraction gives exactly (24). At \(s=0\) the grid is symmetric and its sine sum is odd, so the apparent cotangent singularity is removable. The off-integer continuation is explicitly chosen and is not identified with another interpolation by its integer values.

## Contour and local saddle

On the rectangle in Section 4, the single-grid kernel has residue one, is exponentially small on the upper side, and is \(iN\) plus an exponentially small term on the lower side. When \(|s|<1/2\), the vertical-side denominator stays away from the opposite ray uniformly; this is the needed restriction for this particular unwrapped contour. The raw chirp is not made periodic. Its horizontal modulus costs \(\exp(N|ty|/(2\pi))\), absorbed by the angular quadratic and sufficiently small fixed height. Both vertical currents retain the strict Newton angular loss.

The logarithmic Hessian is
\[
 -\tfrac12\sum_{a<r}\sec^2((a+1/2)\pi/N)
 =-\frac{N}{2\pi}\tan(\pi r/N)+O(N^{-1}).
\]
Together with the chirp it gives the Gaussian denominator \(\sqrt{\tan\pi x-i\epsilon}\) in (18), with the stated factor \(\sqrt N\). The saddle is nonzero uniformly on every compact regular low-index interval. A small complex deficit shifts this saddle analytically; the two cosine exponentials give equal integrals by the evenness of the Newton/chirp factor, rather than two uncontrolled competing actions.

The complete source scalar and the typed-turn scalar both survive the local ratio. The first correction is therefore
\[
 -\pi s^2\cot(\pi x)/N+i\pi(\alpha-\epsilon)s^2/(2N),
\]
not just the paired-factor contribution. The amplitude phase in (30) agrees with removing the old unit phase: the remaining exact scalar is \(e^{-i\epsilon\pi/4}(1+O(N^{-1}))\).

The larger-disk extension is a legitimate three-circles argument applied to a holomorphic normalized error of the actual physical coefficient. At fixed integer color the already proved coefficient cone bounds it polynomially for complete color, and by \(\operatorname{poly}(N)e^{Ct_0^2N}\) for small physical deficit. The lower complete saddle is uniform. Consequently (28a) is negative after choosing the deficit neighborhood small enough. This does not analytically continue the off-integer cotangent formula through its additional half-integer resonances.

## Whole low junction and parity

The global comparison (38) is valid with the retained full physical crossing. Positive Laurent coefficients bound each shifted-grid factor by \(e^{\pi R}e_n(-2)\); the chirp is bounded on this microscopic shift. At odd levels the complete positive trace contains the exact negative endpoint. At even levels the ratio to the closest node telescopes as stated to
\[
 (N/2)\tan(\pi/(2N))\ge\pi/4.
\]
Thus the complete pure tensor controls the product of negative-endpoint values with only the stated polynomial factor. This is a same-level positive comparison and does not assume a lower bound for a signed sum. The regular product-window Gaussian has the summed positive curvature, proving (47). Its multilinear use is correctly restricted to an absolute majorant unless a separate noncancellation comparison is available.

## Canonical wire interpolation

The function in (48) is the previously fixed Gamma product, with no free periodic factor. Its two numerator-to-denominator ratios in (49), at \(Nx=r\), equal the exact products of
\(2\cos((a+1/2)\pi/N\mp\tau/2)\), proving the physical Newton identity. The \(-1/2\) midpoint shifts are essential: the complex bulk expansion then has prefactor \(1/(2N\sin\pi x)\), independent of \(\tau\) to leading order. All arguments remain in fixed regular complex bulk strips after shrinking the neighborhoods.

The endpoint normalization is independently forced term by term:
\[
 G_N(s)G_N(-s)
 =\Gamma(1+s)\Gamma(1-s)
   \prod_{k\ge1}\frac{(Nk+s)(Nk-s)}{(Nk)^2}
 =\frac1{H_N(s)}.
\]
It follows that the turn factor is exactly the three-bulk-factorial ratio (50b). In particular neither a periodic normalization nor an endpoint amplitude is left undetermined.

The short integral (51) is an explicit jointly holomorphic interpolant. At the physical wire rows, the earlier contour formula and the angular tail estimate compare it exponentially accurately to the finite source; the complex saddle lower bound makes that error relative. Its exact meridian ratio (53) follows because its integrand is independent of \(s\) and all \(s\)-dependence was retained outside. For main radii beyond one half, comparison is asserted only on physical integer-deficit rows and follows from (28a), as written. There is no uniqueness claim for arbitrary off-grid continuations.

## Scope

The proof supplies exact pure coefficients, local half-twisted physical coefficients, and explicit analytic wire interpolants with the correct action, amplitude, and meridian correction. It preserves both parities and the specified orientation scalars. It does not yet establish the required conditioned whole-source signed contraction or its off-window estimate, and it does not by itself give a filled-knot microscopic profile. The report states these limits correctly.
