# Proposed fixed terminal budget on the whole type-three input disk

Research protocol for review, 6 November 2026. No implementation or
evaluation is authorized or performed by this note. The proposed
single pass uses the two existing canonical families over \(D_3\),
their saved refined affine errors, and the original source-cell
extractions. It evaluates common main, plane and direct-cut
criteria without a parameter cover. Every failure remains visible.

## 1. Exact scope and fixed inventory

Set \(\beta=0\), keep the preceding ordinary own flag one, and
take \(\epsilon=0,1\). The external parameter is
\[
 b=b_0+\delta,\qquad b_0=.35-.01i,\qquad |\delta|\le r=.09.
\tag{1}
\]
All analytic enclosures cover the entire auxiliary disk \(D_3\).
Finite-source conclusions are restricted to its actual reduced
domain \(K_3\), with the source eligibility proved in
[the incoming-type theorem](research_mixed_terminal_incoming_type_transfer.md).
There is no incoming modulus halfweight. The action and marginal
are exactly \(M_0,p_0\) in that theorem's (5).

The selected height is \(H=.01\). Both complete-weight choices
\(\nu=1,0\) retain all of \(P=[.22,.45]\). Targets for the
ordinary and terminal main indices are respectively \([.22,.5]\)
and \([.22,.4]\), justified by the already proved barriers.
The private main targets retain their original full intervals.

For each of the two cases perform exactly:

* Sixteen height slabs \([j/16,(j+1)/16]\), \(0\le j<16\),
  for each of the arguments \(a_\theta,s_*+a_\theta,t_*+a_\theta\).
* The same sixteen slabs for each of \(\tau+a_\theta\),
  with both fixed real cuts \(\tau=.15,.5\).
* One center logarithm, center cotangent and full-tube curvature
  bound for each new cut argument \(\tau+a^0\).
* Shared-force vertex upper bounds for main, joined plane, and
  both direct cuts, at both Fourier alternatives.
* The fixed recombination of all 54 terminal/branch labels from
  the existing raw source bounds for that case.

The new analytic calls are limited to 256-bit enclosures of
164 cotangents, ten sines, nine logarithms, two cosines, one
exponential, and one \(\pi\). There are no dilogarithms, private
actions, reference proposals, roots, target optimizers, subdivisions,
new centers, alternative heights or precision retries. Rational
cubic maximization uses the existing closed formulas.

## 2. Existing data and associations

Use only the \((0,0)\) and \((0,1)\) entries of the completed
[quadratic refinement](research_mixed_terminal_quadratic_residual_refinement.md),
whose record is
research-mixed-terminal-quadratic-residual-refinement.json,
SHA256 2834576c2a443c9ffd24032277b5f253d9a85eac17d3f754905812e822a9a331.
It supplies exact \(q^0,u\), with \(q=(e,\xi,t,a,s)\), and
the new error bounds
\[
 q_i(b)=q_i^0+u_i\delta+\zeta_i(b),\qquad |\zeta_i|\le\eta_i.
\tag{2}
\]
The parameter center, radius, original branches and exact affine
coefficients must match the saved source chain:

* All-input posterior record e04521450e1973658cbd602aa0a8f54d4c7d40c968b4b90d65374d570981c617.
* Split inclusion record a25587e526dc753306eb690b76f1f07d0d05410be315c6675023bd87ae42e202.
* Correlated analytic record 51b702aa6ea44aa5891bc1146a7d5c0d22686cd814f9bbe5d9c4c63b9a16f9e1.

The posterior case/candidate hashes point first to the split
record, then to the original correlated record. The chosen
\(\beta=0\) candidate has radius multiplier two. Its original
center logarithms, cotangents and full-tube curvature bounds for
\(a,s+a,t+a\) may be reused after checking exact containment of
the refined tubes in their original certified tubes.

The complete real-face extraction is
research-mixed-terminal-uniform-face-reserves.json,
SHA256 37fc3676a9919525e16b214db0fedebd3e13b980150f5f01ec0d0b28141a07d3.
The complete alias extraction is
research-mixed-terminal-uniform-alias-reserves.json,
SHA256 142f424a414174fc8ee8ba0fd4ee69b6c8c6ffd5c954bbba9211771536b9bd87.
Their \(\beta=0\) cases retain respectively 72 and 49 closed
source cells. Use their exact family maxima and original job
associations unchanged. This initial protocol makes no new
source-cell subdivision or per-cell analytic evaluation.

Before an implementation is frozen, all cited proofs, independent
gain checkers, these records and their inherited inputs must receive
literal SHA256 pins. All input hashes must be checked before and
after execution. Old certificates and their source jobs are not
rerun.

## 3. Correlated height arguments and full-domain guards

Put \(a_\theta=\Re a_*+i((1-\theta)\Im a_*+\theta H)\).
For \(z=s,t\), the real and imaginary supports derived from (2)
are
\[
 \begin{split}
 \Re(z_*+a_\theta)&\in
 \Re(z^0+a^0)\ \mathbin{\pm}
                  \bigl(r|u_z+u_a|+\eta_z+\eta_a\bigr),\\
 \Im(z_*+a_\theta)&\in
 \Im z^0+(1-\theta)\Im a^0+\theta H\
 \mathbin{\pm}
       \bigl(r|u_z+(1-\theta)u_a|+\eta_z+(1-\theta)\eta_a\bigr).
 \end{split}
\tag{3}
\]
For \(a_\theta\), omit the \(z\) terms; for a cut add the real
constant \(\tau\). Retain the summed complex coefficients before
taking their moduli.

For each fixed \(b\), these imaginary arguments are affine in
\(\theta\). Therefore the hull of their two endpoint enclosures
covers a whole slab. The real supports are independent of
\(\theta\). All rectangles supplied to cotangent evaluation must
strictly remain in \(0<\Re z<1\), before and after their outward
Arb conversion.

The proved typed coordinate ranges may tighten enclosures used
only for values on the actual canonical family, including reference
center intervals in scalar gains. Likewise, the endpoint hull can
be intersected with independently proved typed bounds for the
same argument. Every intersection must retain an explicit
necessary-range witness; an empty intersection is an error, not
an unexplained source exclusion.

No such intersection may replace the full correlated tube used
in a Taylor derivative bound. All center-to-reference segments
for the Taylor bounds below must lie in the original regular
strip and the saved full derivative domain, including the affine
errors before any typed clipping.

Let \(C_z+iI_z\) denote the enclosed cotangent at each node.
The unweighted means use exact weight \(1/16\). Weighted real
means use
\[
 \omega_j=\int_{j/16}^{(j+1)/16}(1-\theta)\,d\theta
                  =\frac{31-2j}{512}.
\tag{4}
\]
Save every endpoint support, full slab rectangle, outward
cotangent components and exact integral contribution.

## 4. Values, forces and two signed marginal products

Use the common formulas (12)--(18) of the incoming-type theorem.
Write \(\kappa=\pi\Delta\), where
\(\Delta=H-\Im a_*>0\), and let \(I_a,I_s,I_t,I_\tau\)
now denote the corresponding unweighted mean imaginary
cotangents. Let \(Q=\Re g'(A+iH)\), and let \(G_H^+\) be
the same upper chord bound for \(\Re g(A+iH)\) used in the
[original integral protocol](research_mixed_terminal_four_input_integral_budget.md).
Its logarithmic and trigonometric domains must be checked at the
new case's reference interval; its old numerical value is not reused.

The three main forces and value upper are
\[
 \begin{split}
 F_s&=\kappa(1-I_s),\\
 F_t&=-\kappa(1+I_t),\\
 F_{a,\nu}&=\kappa(3I_a-I_s-I_t-1)+(1-\nu)Q,\\
 T_\nu^+&=
 \bigl[\pi\Delta^2\!\int_0^1(1-\theta)(3C_a-C_s-C_t)d\theta\bigr]^+
 +(1-\nu)G_H^+-2\pi_{\rm lower}\nu H .
 \end{split}
\tag{5}
\]
Here brackets denote an outward upper endpoint, with signed
interval multiplication retained.

The joined-plane function is
\(P_T(s,a)=\tfrac32g'(a)-g'(s+a)\).
The direct-cut function can be evaluated on the original family as
\[
 D_\tau^*(s,a)=g'(\tau+a)+g'(s+a)-3g'(a)+2\pi i\tau.
\tag{6}
\]
Equation (11) of the incoming-type theorem proves that (6) equals
the required \(D_\tau(a_*)\) at the actual reference. For Taylor
enclosure, define (6) as a holomorphic function on the full
regular tube and evaluate that function at the center. Do not
assert equality with its \(t\)-dependent expression at a
nonstationary center.

For either function \(F=P_T,D_\tau^*\), construct
\[
 F(q_*)=F_0+L_F\delta+\varepsilon_F,\qquad
 L_F=F_s(q^0)u_s+F_a(q^0)u_a,\qquad
 |\varepsilon_F|\le\rho_F.
\tag{7}
\]
Keep the original \(g''=\pi\cot-i\pi\), including its imaginary
constant in the derivatives. With
\(w_a=r|u_a|+\eta_a\) and
\(w_{sa}=r|u_s+u_a|+\eta_s+\eta_a\), valid errors are
\[
 \begin{split}
 \rho_P={}&|P_s^0|\eta_s+|P_a^0|\eta_a
              +\tfrac12(\tfrac32m_aw_a^2+m_{sa}w_{sa}^2),\\
 \rho_D={}&|D_s^0|\eta_s+|D_a^0|\eta_a
              +\tfrac12(m_\tau w_a^2+m_{sa}w_{sa}^2+3m_aw_a^2).
 \end{split}
\tag{8}
\]
The saved \(m_a,m_{sa}\) bound \(|g'''|=|j''|\) on the
original full tubes. For the new cut use
\[
 m_\tau=\pi_{\rm upper}^2/\sin^2(\pi d_\tau),\qquad
 0<d_\tau\le
 \min\{\Re(\tau+a^0)-w_a,\ 1-\Re(\tau+a^0)-w_a\}.
\tag{9}
\]
The new center primitive is \(j(\tau+a^0)=\Log(2\sin\pi(\tau+a^0))\).
Its full real strip ensures the original logarithmic branch;
save that guard and the center cotangent. All other center data
in (7)--(8) are reused from the matching saved case.

Set \(\Delta_0=H-\Im a^0\), \(p_0=\Im P_0\),
\(d_0=\Im D_0\). The fixed common-parameter upper bounds are
\[
 \begin{split}
 [\Delta\Im P_T]^+\le{}&
 \Delta_0p_0+r|\Delta_0L_P-p_0u_a|
 +\tfrac{r^2}{2}(|u_a||L_P|-\Re(u_a\overline{L_P}))\\
 &+\Delta_{\rm hi}\rho_P+\eta_a(|p_0|+r|L_P|),\\
 [-\Delta\Im D_\tau^*]^+\le{}&
 -\Delta_0d_0+r|\Delta_0L_D-d_0u_a|
 +\tfrac{r^2}{2}(|u_a||L_D|+\Re(u_a\overline{L_D}))\\
 &+\Delta_{\rm hi}\rho_D+\eta_a(|d_0|+r|L_D|).
 \end{split}
\tag{10}
\]
The opposite signs of the two dot products are required.
For interval center coefficients all displayed arithmetic is
outward; an interval must not be substituted by a favorable endpoint
before its sign has been accounted for.

The plane values use (10), the weighted real combination
\(\tfrac32C_a-C_s\), and the halfweight constants from (17)--(18)
of the incoming-type theorem. Its forces are
\[
 G_s=\kappa(1-I_s),\qquad
 G_{a,\nu}=\kappa(\tfrac32I_a-I_s-\tfrac12)
                                      +\tfrac{1-\nu}{2}Q .
\tag{11}
\]
The direct-cut values instead use the second line of (10), the
weighted combination \(3C_a-C_s-C_\tau\), and the complete
selected constants in (5). Their forces are
\[
 F_s=\kappa(1-I_s),\qquad
 F_{a,\nu}^{\tau}=\Re D_\tau^*(s_*,a_*)
       +\kappa(3I_a-I_s-I_\tau-1)+(1-\nu)Q.
\tag{12}
\]
These formulas cancel the old \(t_*+a_*\) remainder before
bounding. No private action value or imaginary critical lift is
reconstructed.

## 5. Fixed force vertices and all source comparisons

Use the convex moving-center cubic majorants from
[the shared-force theorem](research_mixed_terminal_shared_force_vertices.md).
Each is a supremum of affine functions of its force on fixed
displacement intervals. Each force map is multiaffine in the
listed scalar parameters. Thus its sum is bounded by the
maximum over their endpoint vertices, before numerical rounding.

For each family use the following complete vertex sets:

| Budget | Factorial parameters | Forced extra parameter | Vertices per case |
|---|---|---|---:|
| Main | \(\kappa,I_a,I_s,I_t\) | \(Q\) | \(16+32\) |
| Plane | \(\kappa,I_a,I_s\) | \(Q\) | \(8+16\) |
| Each real cut | \(\kappa,I_a,I_s,I_\tau,\Re D_\tau^*\) | \(Q\) | \(32+64\) |

All target-center intervals contain their actual centers inside
the full target intervals. No forced interval is shortened in
this protocol. The original cubic coefficients are precisely
those of (13), (16), and (18) of the incoming-type theorem.
There are 528 vertices and 1,152 rational cubic gains, with
1,152 independent exact checks. Save each force tuple, every
clipped-gain witness, its sum, and every final maximum.

The fixed source recombination covers all 108 terminal/branch
labels across the two terminal types:

* Four main inequalities use (5) and their three-gain maxima.
* Sixty-four alias-label inequalities use the saved twelve-family
  maxima with the unchanged .041 debit and the 12-to-16 mapping.
* Four constant inequalities use
  \(\rho_C=.111+.44c_{\min}\), with the new case's proved
  negative shared-height floor and the original bare plane \(>.99\).
* Thirty-six real-face/entropy inequalities start with the plane
  upper plus their own saved \(U_f\).

For each of the six fixed-transform real faces and the entropy
family, also retain its direct upper with the same \(U_f\);
this gives 28 additional comparisons. The final family bound
may use the minimum of these independently valid uppers. Every
positive constituent upper remains in the output.

For terminal type four only, a private-left improvement is
permitted if the already proved exact guards in
[the uniform force theorem](research_mixed_terminal_four_input_private_left_force.md)
hold on the complete saved \(\beta=0\) reference image, including
its private-coordinate guard for \(d_L>0\).
Check those same guard constants once, without changing them.
The symmetric private-left index barrier already has the full
original height scope. If all force guards hold, the two extra
uppers are the corresponding main bound plus the bare private-left
\(U_f\). If any guard fails, record that optional route as
unavailable; it is not a source exclusion or an invitation to
choose new guards. No new analytic calls are added for this route.

The predeclared target is a common raw gap \(1/10000\).
Record separately whether every final upper is negative and
whether every upper is below \(-1/10000\). A positive or zero
upper is inconclusive, not a positive phase value. The overlap
theorem may be reported as already known, but it does not remove
any part of the whole-\(D_3\) analytic enclosure in this pass.

## 6. Failure handling and the decision before execution

The implementation must retain both cases and all their expected
labels. An unsuccessful domain or finite-enclosure guard records
the exact failed operands and the remaining unvisited operations.
A failed comparison never triggers a new interval, trial, radius,
height, precision or subdivision. Unexpected errors stop and archive
the partial record. The output is a fresh exclusive file; all
frozen inputs remain unchanged.

The root and peer reviewers must approve this concrete protocol
and any future implementation before one analytic pass. In
particular they should assess whether the whole-disk supports in
(3) and the conservative scalar maximizations are sufficiently
informative to warrant the work. This document supplies a finite
reviewable test, not evidence that its scalar bounds will pass.
The incoming-type transfer proves why a successful test suffices.
Only after all required signs are checked could one assemble a
full \(K_3\) local finite kernel, with original normals, parities,
color jets and the same conditional outer-plateau scope. No
whole-source partial-filling or cofinite conclusion is made.
