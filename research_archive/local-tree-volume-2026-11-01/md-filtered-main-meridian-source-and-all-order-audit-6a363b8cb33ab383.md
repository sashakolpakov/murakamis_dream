# Source audit of the filtered microscopic action

Private independent derivation, 1 November 2026.

The source statements below concern a fixed original ordered diagram and fixed crossing powers. The graph never grows with the level. The reference publication is commit d8ff75be41f307c34867046445c530a6251ec5cf. The additional local-message input is /private/tmp/md-all-circle-local-message-filling-criterion.md, SHA256 8ab57537769d7d8ff1865811b8b9d6de737f7701c0c94183b07d53513c87c81b.

I read Sections 1–6 of /private/tmp/md-main-meridian-all-order-filtered-action-and-operator.md, then its added rational peripheral formulas. I reopened the actual source estimates, rather than using a microscopic profile as an analytic-continuation principle. The source extension and the filtered all-order conclusion hold for the full published long-filled strict-tree class and the published summed all-circle class. They also hold for the new local-message class, by the finite induction in Section 5 below. No new identification with the classical geometric eigenvalue curve follows from this source argument.

## 1. Exact dependencies and the scope of the parameter extension

The dependencies read in the current publication checkout were:

* actual_main_meridian_source_bounds.md, (D2)–(D24): fixed quotient, full Hermite norm, crossing interpolation, mixed carriers, and actual decorated extraction;
* actual_main_meridian_general_component_comparison.md, Sections 2–9: whole-component comparisons and grouped errors in the actual fixed-power contraction;
* actual_main_meridian_high_fourier_reflection.md, (14)–(28): finite alias identity, reflected difference, and its strict regular-window loss;
* actual_main_meridian_grouped_wire_packet.md, (2)–(8), (21)–(36): exact physical edge factors, canonical interpolation, finite currents, and the source-to-packet error;
* actual_main_meridian_direct_crossing_trace.md, (10)–(18): the translated single-grid rectangle with its original endpoint currents;
* actual_main_meridian_joint_filling_transform.md, Sections 1–4: actual scalar ledger, real-spectator telescoping, fixed tail losses, and nonminimal charges;
* exact_factorial_interpolation_and_complex_contours.md, Sections 1–4: the chosen Gamma product, exact reflection, and summable Stirling remainder.

Let \(K\Subset\{\operatorname{Im}s>0\}\) be fixed. In an actual typed contraction the moving grid parameters range over \(K\), \(-K\), or the constant value zero. Thus a single compact in the upper half-plane is not silently substituted for every grid parameter. The moving compacts avoid all real integer and half-integer collisions. The constant type still uses its original full-normal trace.

The extension is a direct estimate of these finite formulas. It does not assert uniformity across a nonzero ordinary-color resonance, or for \(s\) increasing with \(N\).

## 2. Why the full component proof extends

### 2.1. Fixed physical powers and every normal coordinate

At a moving equal-color vertex, (D14) is
\[
 r^{[n]}_{N,s}(z)=
 -\frac{1}{N(U-U^{-1})}\sum_{j=0}^{N-1}
 \lambda_j(s)^n(t_j-t_j^{-1})
 \frac{P_s(z)}{z-c_j(s)},\qquad U=e^{2\pi is}.
 \tag{1}
\]
For \(s\in K\cup(-K)\), its scalar denominator is bounded away from zero. The nodes have imaginary angular height \(O_K(N^{-1})\). The same Chebyshev divided-difference estimates used in (D14) give polynomial bounds for the canonical polynomial and its derivative on the complete real interval. Negative fixed powers obey the same estimate because every \(\lambda_j\) is nonzero and both \(|\lambda_j|\) and its inverse are bounded uniformly in \(j,N\) on this compact.

This controls full Hermite coordinates by polynomial norm equivalence. It is not merely a simple-node value estimate. The common physical crossing scalar has bounded modulus and inverse on the fixed compact; it remains explicitly in the scalar ledger. The mixed reference relation (D17) is algebraic and retains its exact \(q^{-s^2}\) factor. Its fixed crossing polynomials have the same polynomial bounds.

### 2.2. Physical turns do not require the small spectral-comparison disk

For the fixed Newton coordinates the turn factors are the exact diagonal weights
\[
 \gamma_N(s)\frac{W_{d-k}(s)}{H_N(s)},\qquad
 W_k(s)=\prod_{\substack{1\le r\le k\\j\in\mathbb Z}}
       \left(1-\frac{s^2}{(r+jN)^2}\right).
 \tag{2}
\]
The integers \(r+jN\) in this product are distinct and nonzero. A fixed finite set of their possible small values stays a positive distance from the zeros of every factor on \(K\cup(-K)\). For the remaining integers,
\[
 \left|\log\left|1-\frac{s^2}{m^2}\right|\right|
 \le C_Km^{-2}.
 \tag{3}
\]
The sum is convergent. Products of the factorwise minima with one bound all subset products below; products of the maxima bound them above. Consequently \(W_k\), \(W_k^{-1}\), \(H_N\), and \(H_N^{-1}\) are uniformly bounded for all \(k<N\) and all sufficiently large \(N\). The finitely many smaller levels cause no problem on this nonreal compact.

The needed physical coefficient estimate is therefore still exactly (D23)–(D24). The separate full-\(\mathcal J\) comparison theorem on \(|s|\le1/16\) is not an input here. A generic polynomial of small \(\mathcal J\)-norm is converted to the low/high coefficient cone only through the actual decorated/turned extractor, as in the original component induction.

### 2.3. Component gaps remain the original gaps

Chebyshev folding of a fixed-degree raw product depends on the bounded number \(\cos(2\pi s)\). All-low whole-junction estimates and one-high reflected differences involve only finitely many \(U_{\ell-1}(\cos2\pi s)\) at each fixed valence. These are bounded on the compact. In particular the strict one-high Fourier loss in (28) of the reflection note is independent of this parameter bound.

The multiple-high comparison is a geometric complete-pressure comparison after a full canonical norm estimate, and hence also changes only its prefactor. The finite collection of band, contraction, and half-boundary patterns has the same positive minimum loss. The clean old tensors retain the original deformed edge weights; they are not equated with the complete physical invariant.

It follows that the full arbitrary-component induction, including inherited full-array losses and fresh probe Gaussians, extends to the stated compacts. Its scalar discarded error is still estimated after the actual fixed-power traces and before moving angular contours. This argument does not require a new angular estimate on individually discarded sectors.

## 3. Exact translated contours and the unchanged first packet

For a generic grid parameter \(\sigma\), the exact functional is
\[
 \mathcal D_{n,\sigma,N}[f]=
 \frac{\eta NC_{N,n}(\sigma)}{\sin(2\pi\sigma)}
 \sum_{r=0}^{N-1}\sin\tau_r(\sigma)\,
 f(\tau_r(\sigma))e^{inN\tau_r(\sigma)^2/(4\pi)}.
 \tag{4}
\]
Use the original single-grid rectangle translated by \(2\pi\sigma/N\). Its vertical kernel is exactly
\[
 K_\sigma(\pm\pi+iv+2\pi\sigma/N)
       =\frac{iNe^{-Nv}}{1+e^{-Nv}}.
 \tag{5}
\]
This formula has no parameter-dependent pole-separation problem. Any bounded real extent of \(K\) changes endpoints by \(O_K(N^{-1})\), not by a macroscopic distance. Moving the horizontal expansions to the fixed interval retains their short endpoint connectors.

At an integer translate \(s+j\), one may instead reindex the central entries and restore the bounded number of wrapped endpoint entries. The chirp is not periodic. At those endpoints its extra multiplier has bounded modulus, because their imaginary displacement is \(O_K(N^{-1})\) and \(n,j\) are fixed. The raw angular endpoint gap remains the one in the packet theorem.

The exact two-side coefficient is
\[
 c_{\ell,N}(\sigma)=
 (-1)^{(N-1)(\ell-1)}U_{\ell-1}(\cos2\pi\sigma),\qquad
 c_{1,N}=1.
 \tag{6}
\]
Its bound \(\ell e^{2\pi|\operatorname{Im}\sigma|(\ell-1)}\) is absorbed by the same geometric charge tail for all sufficiently large \(N\). A finite retained charge set changes only fixed prefactors. The strict charge ordering and all classical actions are unchanged.

For actual constant-type vertices one can retain the original small formal parameter circle used to take the full-normal limit, independently of the compact containing the physical main parameter \(s\). The retained packet is uniformly bounded on the product of these parameter sets. This supplies the same maximum-principle argument for \(\sigma=0\), without attempting to continue a nonremovable resonance.

Thus the exact first-charge coefficient remains one at both parities and in every type. After the exponential errors, all remaining \(s\)-dependence is exactly the single reduced-cut factor, the original scalar ledger, and
\[
 \prod_e\frac{G_N(Nx_e)^2}
                 {G_N(Nx_e-s)G_N(Nx_e+s)}.
 \tag{7}
\]
The product is over original physical edges. Hidden unturned resolution edges are absent. The fixed framing/crossing/carrier product is exactly \(A_N(s)\), not a newly chosen gauge.

## 4. All-order expansion and the degree filtration

The all-order claim is supported by the actual Gamma product, not just by an interpolation recurrence. Apply a finite Stirling expansion with a periodic-Bernoulli remainder to its \(k\)-th factor. On a fixed complex bulk compact, the two arguments \(N(k+x)\), \(N(k-x)\) lie in a common right-half-plane sector, uniformly in \(k\). A remainder of order \(N^{-L}\) is bounded by \(C_LN^{-L}k^{-L}\) once the expansion is taken sufficiently far. The finitely many initial factors are treated in the same sector; the tail is summable. This gives an expansion to every prescribed order with fixed derivatives by Cauchy.

The exact lattice normalization fixes the half logarithm and the reflection phase. No periodic interpolation multiplier is permitted. In particular
\[
 \log G_N(Nx)=NJ(x)+\tfrac12\log(2N\sin\pi x)
                    +\sum_{j\ge1}N^{-j}b_j(x)
 \tag{8}
\]
is an asymptotic expansion with a holomorphic remainder of any requested finite order.

Write \(\delta=N^{-1}\) and introduce an independent auxiliary variable \(t\). The ratio in (7), with \(s=t/\delta\) only as an algebraic organization of its interpolant, has the expansion
\[
 \delta^{-1}\{2J(x)-J(x+t)-J(x-t)\}
       +B_0(x,t)+\sum_{j\ge1}\delta^jB_j(x,t)
 \tag{9}
\]
for its logarithm. Every \(B_j\) is even in \(t\) and zero at \(t=0\). The \(\log N\) terms cancel.

Exact integer offsets are retained here. If an edge argument is
\(x=\ell(X)+\delta c\), Taylor expansion of
\(\delta^{-1}K(\ell+\delta c,t)\) contributes \(cK_x\) to \(B_0\) and further holomorphic terms to the \(B_j\). It changes no coefficient of the leading action. The same statement applies to every original \(d=N-1\) offset in a complete gate or circle factor.

One can make the two-parameter organization concrete on the fixed local contour: substitute the exact Gamma ratios with arguments \(N(x\pm t)\), keep the same original small wire-and-angle neighborhood, and take \(t\) sufficiently small that all arguments remain bulk and the nondegenerate saddle persists. This defines an auxiliary analytic integral. It is not a physical claim at \(s=Nt\). Its specialization \(t=\delta s\) has precisely the actual fixed-\(s\) coefficients, because the physical discarded terms have already been controlled exponentially.

All-order analytic stationary phase for that local integral gives the action and amplitude germs in (13)–(14) of the report. A direct finite Gaussian expansion suffices: coefficients are finite polynomials in derivatives of the phase and amplitude and the inverse Hessian; the contour remainder is uniform on a smaller parameter neighborhood. Any possible residue-class scalar is retained until it cancels in the normalized ratio.

The coefficient at \(\delta^r\) in the logarithmic ratio is a polynomial in \(s\) of degree at most \(r+1\). Only the leading action \(\delta^{-1}[S(t)-S(0)]\) can contribute degree \(r+1\). Every amplitude term has an extra nonnegative power of \(\delta\) and hence degree at most \(r\). This establishes the stated top-diagonal filtration at all orders.

## 5. The new local-message theorem also has this all-order interface

This requires an additional argument; an \(O(N^{-1})\) profile alone would not suffice.

The local proof retains the exact full edge kernel and the exact messages. Its conditional high-index gap, real bound, finite-degree strip estimate, and trace-tail estimate depend exponentially only on the original complete kernel and the local condition
\[
 \max_v\frac{d_v}{d_v^2+n_v^2}\le2^{-120}.
 \tag{10}
\]
On \(K\cup(-K)\), the factors in Section 2 change only prefactors. The generic trace proof from Section 3 applies directly to moving types; the constant type retains its independent full-normal continuation. The fixed local exponential margins and local first-charge loss remain unchanged. There is no sum over the tree in this argument.

For an arbitrary prescribed order \(L\), strengthen the local induction to
\[
 \frac{M_{v,N}(u)}{M_{v,N}(0)}
 =e^{Nh_v(u)}\frac{\alpha_v(u)}{\alpha_v(0)}
 \left(1+\sum_{j=1}^{L}N^{-j}a_{v,j}(u,s)
                         +O_K(N^{-L-1})\right)
 \tag{11}
\]
on a fixed smaller parent disk. The exact angular-independent subtree scalar is cancelled by this ratio, rather than assumed to converge. The coefficients and remainder are holomorphic in the parent variable, uniformly on the fixed main-parameter compact. The leading amplitude is nonzero.

For a terminal subtree, the all-order edge expansion in Section 4 and the finite translated first-charge contour prove (11). Suppose it holds for each child. Multiplication preserves an arbitrary finite relative order. Because the normalized leading amplitude has no zero, its logarithm, with value zero at the parent origin, also has an all-order expansion. The exact logarithm differs from the truncated expansion by \(O(N^{-L-1})\), with every fixed derivative on a smaller disk.

The next trace is evaluated using these exact child messages. The local proof's conditional real and strip bounds continue to control its tails and connectors. On the selected first-charge contour the leading phase has a nondegenerate Gaussian and the product amplitude is nonzero. Its absolute local Gaussian integral is bounded by a constant times its leading magnitude on a smaller parent disk. Therefore a holomorphic relative remainder of order \(N^{-L-1}\) remains of that order after integration. If derivative bookkeeping calls for extra finite orders, start the child induction at those orders; all such orders exist. The nonminimal retained charges and the endpoint errors remain exponentially small relative to the first conditional charge.

This proves (11) for the next vertex. The graph is fixed and finite, so the induction establishes every prescribed order without a depth-uniform amplitude constant. It uses exactly the permitted subtree-dependent constants and starting levels. Its exponential estimates remain the local ones.

To identify the action and not merely the existence of expansions, apply the same induction to the auxiliary two-parameter local integrals from Section 4. Their stationary equations are the original edge-wire and angular equations with \(\sum_eK(x_e,t)\) added. Eliminating a child variable is ordinary stationary elimination. The Hessian at each step is the nonzero Schur complement proved in the local-message argument. Repeating the eliminations therefore gives the same joint critical branch through the original first-charge point. Constants subtracted in normalizing a child message are restored by its exact \(M_{v,N}(0)\); they telescope rather than discard any action.

The formal Gaussian coefficients also compose in this order: finite Gaussian integration with an invertible block Hessian is associative, and its Wick coefficients agree with those of the original joint integral. Thus the resulting \(S(t)\) is precisely the report's joint action (13), with the original physical edge set, and the same filtration follows. This is stronger than postulating that a normalized cavity phase has the desired Taylor series.

Finally the root has the original reduced cut factor and the exact scalar ledger. The argument does not substitute an unsigned kernel norm for a full invariant, nor assume a global first-charge dominance independently of the local proof.

## 6. Operator and peripheral bookkeeping

The operator normalization in (18)–(20) is consistent. Since
\(d_N(q_N^s)=\eta_N/[NH_N(s)]\), the normalized period in the report is proportional to the full modified-trace state, while \(P\) annihilates the reduced state. Its shift ratio is exactly
\[
 \frac{H_N(s+j)}{H_N(s)}
 =(-1)^j\frac{M-M^{-1}}{q^jM-q^{-j}M^{-1}}.
 \tag{12}
\]
This is the displayed rational Ore gauge. Clearing it yields the recorded classical factor \(f(M)^dP_0(M,-L)\); it is not legitimate to omit the factor before taking the formal identity.

The translated compacts supply all shifts \(s,\ldots,s+d\) of one actual operator equation. After the finite source estimates above, the all-order coefficient comparison is valid on that open set. The regrading into \(h^{-1}\mathcal S(u)\) and nonnegative powers of \(h\) is legitimate because the degree filtration forbids any lower \(h\)-power. The substitution \(u=hs\) is injective on the nonnegative double power-series ring. This verifies the formal extraction used in Sections 5–6 of the report.

I also checked the added rational insertion:
\[
 e^{K_x}=\frac{(1-E)^2}{(1-EM^2)(1-E/M^2)},\qquad
 e^{K_t}=\frac{M^2-E}{1-M^2E}.
 \tag{13}
\]
It gives
\[
 L_{\mathrm{eff}}=-M^{a(D)}
       \prod_e\frac{M^2-E_e(M)}{1-M^2E_e(M)}
 \tag{14}
\]
with the stated reduced sign. Its derivative at completeness is
\(a(D)+2i\sum_e\cot(\pi x_e^{\mathrm{fill}})\), agreeing with the existing preferred-cusp calculation. This is a check of the exact phase-derived formula, not an identification with a nonparabolic representation curve. That identification remains the separate missing classical adapter stated in the report.

No mathematical correction to Sections 1–6 is required by this audit. The local-message class may be added with the explicit all-order induction in Section 5 above; omitting that argument and citing only its first-order profile would be insufficient.
