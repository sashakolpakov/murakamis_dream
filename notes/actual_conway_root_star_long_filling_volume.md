# Root-star compositions and the knot complement volume

31 October 2026. Internally reviewed assembly. This note concerns the
literal composition \(C(h_0T(h_1\cdots h_s))\), with \(s\ge2\).
The analytic argument treats the correlated root character together with
its child. It does not replace the original signed source by a positive
alias envelope. The theorem records all physical pure/odd patterns in this literal
presentation. Its all-odd source overlaps an existing belt-stack theorem;
no new knot isotopy classification is asserted. The published completed-root manuscript is unchanged.

## 1. Statement and original normalization

Each \(h_i=T(R^{\epsilon_i}L_{j_i})\) is an original turned circle coupon,
with its own color \(1\le j_i\le N\), physical half-twist sign
\(\epsilon_i\in\{0,\pm1\}\), and disk framing. Products and \(T\) are
the actual ordered tangle operations. Retain the original cylindrical
closure and one-cut mark. Fix a half-twist pattern whose literal terminal
pairings have one main component and no internal closed component.
Such patterns exist by the endpoint-pairing construction in the
[general marked geometry theorem](actual_conway_general_mask_marked_filling.md), §7.

At leaf \(i\), insert a fixed signed full twist \(R^{-2p_i}\). Filling
that circle replaces the leaf by the rational tangle
\(T(R^{\epsilon_i-2p_i})\). Write \(K_{s,\epsilon}(\mathbf p)\) for
the resulting knot in this retained presentation.

**Theorem.** For every fixed \(s\ge2\) and knot half-twist pattern
there is \(P(s,\epsilon)<\infty\) such that, for all fixed signed
integers \(|p_i|>P(s,\epsilon)\), the knot complement is hyperbolic and
\[
 \lim_{N\to\infty}\frac{2\pi}{N}
 \log\left|K_N(K_{s,\epsilon}(\mathbf p))\right|
 =\operatorname{Vol}(S^3\setminus K_{s,\epsilon}(\mathbf p)).
 \tag{1}
\]
The level runs through both parities and all composite levels. The
\(s+1\) slopes are independently chosen, with no restriction on their
relative signs or magnitudes. They and the expression are fixed before
the limit; the threshold is allowed to depend on that expression and
half-twist pattern.

Here \(K_N\) is the original reduced enhanced invariant. The
[normalization comparison](actual_complete_augmented_source_normalization.md)
keeps its outer framing character of modulus one. In the full modified
one-cut convention there is instead the recorded single nonzero factor
of modulus \(1/N\). Either convention gives (1). This factor is applied
once to the whole original diagram, not once per auxiliary register.

## 2. The complete action and the all-core packet

Set
\[
 J(u)=\int_0^u\log(2\sin\pi t)\,dt,\qquad
 g(a)=J(2a)-4J(a),\qquad G_0=g(1/4).
\]
The complete port of a prefix of \(r\) children is
\((B,X,Y)=(1/r,1,1/r)\). Thus the inner leaves have label \(1/4\),
the outer root leaf has label \(\arctan(s)/\pi\), and every retained
product gate is strict. There are \(H=s+1\) leaves, \(H-2\) retained
gates, and \(2H-3\) primitive free wires. Only the final forced gate
is removed, retaining its exact \(N-1\) complement relation.

The [full-jet child proof](actual_conway_root_star_full_jet_localization.md)
and [root contraction proof](actual_conway_root_character_fourier_contraction.md)
give, with \(h_N=h_N^0=T(L_N)\), the every-level positive complete reference
\[
 \phi(L_Nh_N^s)=N\sum_{k=0}^{N-1} h_N(c_k)^s>0,\qquad
 F_0=\lim_N N^{-1}\log\phi(L_Nh_N^s)=2sG_0.
 \tag{2}
\]
Here \(c_k=2\cos((2k+1)\pi/N)\); the sum counts repeated nodes with their grid multiplicities. This is the action of the original complete source. Its equality to
the geometric action also follows from the strict wire variational
formula and the actual complete geometry; it is not a freely chosen
comparison rate.

The [general core theorem](actual_conway_general_core_packet_and_gap.md)
applies since \(H\ge3\). It gives a separately even finite holomorphic
window \(\mathcal C_N(\chi)\), retaining the original offsets,
\[
 \mathcal C_N(\chi)=N^{3/2}a_\epsilon(\chi)
 e^{N\Phi_\epsilon(\chi)}(1+O(N^{-1})),\qquad
 a_\epsilon(0)\ne0,\quad \Phi_\epsilon(0)=F_0.
 \tag{3}
\]
Its approximation to the all-core source is exponentially accurate in
a fixed small physical color corridor after the explicit unit phase
\(\eta_N=\exp(i\pi(N-1)\sum_i\epsilon_i/4)\) is restored. The
all-core complement has a strict gap over the whole physical color cube.
The high-index and quarter-index packets supply (3) on a fixed complex
neighborhood, including their exponential index-interpolation errors.
The diagonal color Hessian is
\[
 \Phi_{ij}(0)=-\frac{2\pi c_i}{1-\epsilon_i i c_i}\delta_{ij},
 \qquad c_0=1/s,\quad c_i=1\ (1\le i\le s).
 \tag{4}
\]
Its real part is negative definite. Consequently (3) has the fixed
complex Gaussian envelope needed for the full filling transfer.

## 3. Restoring the whole physical source

Write the literal scalar using exact rerooting:
\[
 Z_N=\phi\bigl(T(R^{\epsilon_0}L_{j_0})T(E_N)\bigr)
     =\phi(R^{\epsilon_0}L_{j_0}E_N),\qquad
 E_N=\prod_{i=1}^sT(R^{\epsilon_i}L_{j_i}).
 \tag{5}
\]
This is a scalar equality in the original repeated-root algebra. It
retains all normal coefficients and does not assert a tangle isotopy.

The child proof bounds a physical leaf in the full value-and-normal
norm at rate \(2G_0\), with a uniform strict loss for an alias or a
macroscopic color deficit. The norm is submultiplicative. The unturned
root functional has only polynomial norm, uniformly in its physical
color. Hence any child alias or far color loses a fixed amount below
\(F_0=2sG_0\) after the actual root contraction.

For the remaining root terms, the child product has a fixed angular
strip bound at exactly \(F_0\), with quadratic localization about
\(\theta=\pi\). The root contraction theorem keeps the actual half-twist
chirp in both values and normals. Its Fourier formula has weights
\((-1)^m(m+1)\) at frequencies \(h+mN\); the potentially dangerous
\(m=-1\) frequency has weight zero. The endpoint repair and both vertical
joining currents have a separate strict gap. This proves a uniform
root far-color estimate. The complementary color in a root alias is
macroscopic, so the same estimate controls the whole correlated root
alias without a separate positive root envelope.

For completeness, the exact telescoping split is
\[
 Z_N-Z_N^{\mathrm{core}}
 =\phi\bigl(A_0T(E_N)\bigr)
  +\phi\bigl(C_0T(E_N-E_N^{\mathrm{core}})\bigr),
 \tag{6}
\]
where \(C_0,A_0\) are the original turned root core and alias.
The first term has the correlated root gap. In the second, \(TC_0\)
is the difference of the two physical root coupons, so still defines
a polynomially bounded functional on the child's full-jet norm.
There is no norm estimate for an arbitrary turn hidden in this step.
Thus for some \(\gamma>0\), uniformly in all physical colors,
\[
 |Z_N-Z_N^{\mathrm{core}}|\le N^C e^{N(F_0-\gamma)}.
 \tag{7}
\]
Together with the core theorem, this supplies both the full physical
color-complement gap and the exponentially accurate comparison with
(3). All hypotheses of the
[original-source filling transfer](general_original_source_long_filling_transfer.md)
are now verified for this literal source.

## 4. Filling and the actual hyperbolic volume

The exact circle-basis identity substitutes each \(R^{-2p_i}\) in the
original diagram. Its full Fourier–Hermite coefficients have total
variation at most \(2N(1+|p_i|)\). Hence the global errors in (7) remain
exponentially small after filling with any fixed slope tuple.
The transfer theorem retains the nonzero charges, all endpoint currents
and the nonzero leading amplitude. For independently sufficiently long
fixed signed slopes its selected action can be written
\[
 S_{\epsilon,\mathbf p}(\chi)=\Phi_\epsilon(\chi)
  +\frac{\pi i}{2}\sum_{i=0}^s\frac{(\chi_i-1)^2}{p_i},
 \qquad dS_{\epsilon,\mathbf p}(\chi_*)=0.
 \tag{8}
\]
Indeed its Fourier variables obey
\(\partial_i\Phi+2\pi iz_i=0\) and
\(\chi_i-2p_iz_i-1=0\); eliminating \(z_i\) gives (8).
The resulting asymptotic has a nonzero coefficient and exponent
\(N S_{\epsilon,\mathbf p}(\chi_*)\), up to the recorded unit phases
and polynomial normalization. Its logarithmic rate is therefore
\(2\pi\Re S_{\epsilon,\mathbf p}(\chi_*)\).

The [general marked-mask theorem](actual_conway_general_mask_marked_filling.md)
applies to this strict tree and these exact physical signs. It constructs
the actual signed augmented-link group representation, with primitive
auxiliary logarithms
\[
 U_i=-2\pi i\chi_i,\qquad V_i=-2\partial_i\Phi_\epsilon,
 \qquad G=2\pi i\Phi_\epsilon.
 \tag{9}
\]
The original fundamental-chain regulator is calibrated at the complete
metric, and its volume is
\(\Im G-\tfrac12\sum_i\Re U_i\Im V_i\).
Equations (8) are precisely
\(U_i+p_iV_i=-2\pi i\), with primitive angle \(2\pi\).
The proved framed metric completion yields a smooth complete metric on
the actual disk-filled topology for all slopes in one fixed reciprocal
polydisk. Its volume is exactly
\[
 2\pi\Re S_{\epsilon,\mathbf p}(\chi_*)
   =\operatorname{Vol}(S^3\setminus K_{s,\epsilon}(\mathbf p)).
 \tag{10}
\]
Take a common threshold for the analytic and geometric neighborhoods.
Only the auxiliary crossing circles are filled; the main knot cusp
remains unfilled. Equations (7)–(10) prove (1).

## 5. What this adds and what remains open

The root-star expression has a bare root leaf and is outside the literal
completed-root grammar of the published manuscript. This is a statement
about that grammar, not a claim that its knot types were previously
unknown or cannot admit another covered presentation. The [prior-source coverage comparison](actual_conway_root_star_prior_source_coverage.md)
records two concrete overlaps. The missing Fourier mode already appears
in the [outer squared-kernel theorem](actual_outer_color_squared_kernel.md).
When every inner sign is nonzero, the entire mixed-color scalar (5)
is the earlier octahedral-belt scalar with outer power
\(a=\epsilon_0+n_+-n_-\). Its full source estimate was already available.
The present child argument also allows inner \(\epsilon_i=0\), outside
that recorded two-type belt alphabet. A source identity alone supplies
no isotopy or correspondence of peripheral curves. The marked-mask proof
in §4 establishes the geometry of the actual current presentation
independently. The ordinary pretzel source has no outer \(L_j\) and is
not the same literal source.

For arbitrary strict closed trees, the core estimate and actual marked
filling calibration are now available. The remaining source requirement
is a nonempty-alias bound at the complete geometric rate, or an equally
sufficient bound after exact filling. The present Fourier theorem gives
such a bound when the turned child is a product of physical leaves.
It does not prove the necessary spectral localization for an arbitrary
child with internal turns. Presentation coverage and a generic
main-meridian quantum A-operator theorem remain separate open tasks.


## Internal review and verification scope

The source-transport and coherent-source reviewers independently read
all five sections, including the whole alias split, exact original
normalization, fixed complex packet and full filling transfer. The
marked-geometry reviewer independently checked the actual topology,
primitive slopes, absolute regulator and smooth metric completion.
The primary reviewer checked those interfaces and the comparison with
prior source results. All analytical reviews passed after the stated
notation and coverage clarifications. These are internal reviews, not
external peer review or formal verification. Native rendering and link
checks preserve the written proof; no finite numerical experiment is
used to establish the asymptotic theorem.
