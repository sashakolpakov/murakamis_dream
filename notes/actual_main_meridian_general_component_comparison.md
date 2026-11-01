# Main-meridian estimates for arbitrary Conway product regions

1 November 2026.

A fixed Conway construction joins two-string tangles by ordered products and physical quarter-turns. Consecutive products with no turn between them form one product junction. A junction is bare when it carries no original crossing-circle operator. This note treats an arbitrary finite connected region of such junctions: their number and their valences are unrestricted, and both are fixed before the level tends to infinity.

The main meridian moves by an amount of order \(1/N\). That deformation changes the polynomial relation in some orientation types, so a whole-junction trace can acquire terms absent at completeness. A comparison with the complete trace at the same indices is false in general. The proof instead separates the trace difference according to its high indices. With one high index, an exact Fourier bound reflects that index and an exact Frobenius pairing fuses two junctions in a positive comparison tree. With several high indices, a half-label projector supplies a boundary comparison. In each case the full neighboring branches remain coupled, and the comparison pressure is bounded by the pressure of the original construction.

The clean part uses complete bare tensors with the **original deformed edge factors, boundary arrays and typed carriers retained**. It is not the invariant evaluated at the complete meridian. The grouped remainder has a strict exponential loss. Sections 1–7 prove this source statement and its passage through the actual circle operators. Sections 8–10 verify the original wire-packet and filling interfaces. Together with those established proofs, the result removes the bare-component restriction from the [filled meridian-profile and volume theorem](actual_main_meridian_filled_volume.md). All its strictness, knot, framing, fixed-parity and sufficiently-long fixed-twist hypotheses remain.

The fused trees occur only in upper estimates. No isotopy or equality of knot complements is inferred from the fusion identity, and the final volume and preferred cusp always belong to the original filled knot.

## 1. Fixed source, boundary arrays, and the theorem

Let \(\mathcal G\) be a fixed finite tree of actual bare product junctions. Every junction has full valence at least three and every edge between junctions carries an original physical quarter-turn. A higher-valence junction is kept whole in its moving trace. Only its complete positive comparison may be resolved by the original ordered binary products.

Set \(d=N-1\), \(m=\lfloor d/2\rfloor\), and
\[
 c_j=2\cos\frac{(2j+1)\pi}{N},\quad
 S_r=\prod_{j=1}^r2\sin\frac{\pi j}{N},\quad
 e_r(z)=S_r^{-2}\prod_{j<r}(c_j-z).
 \tag{1}
\]
Indices \(r\le m\) are low; the others are high. The actual orientation type uses either \(P_0=\mathcal T_N+2\) or
\[
 P_s=\mathcal T_N+2\cos(2\pi s),\quad
 \Delta_s=2\cos(2\pi s)-2,\quad
 \phi_s(F)=(-1)^dN^2[z^d]\operatorname{rem}_{P_s}F.
 \tag{2}
\]
Both repeated-node values and first normal coordinates remain in this quotient. Equal-color moving junctions are an independent set along physical turn edges. Constant junctions may be adjacent; strict alternation is neither assumed nor needed.

For every external branch, assume its entire canonical coefficient array satisfies
\[
 |f_{i,N,r}(s)|\le e^{N(c_i+\epsilon_N)}
 \begin{cases}e^{Ng(r/d)},&r\le m,\\1,&r>m,\end{cases}
 \qquad \epsilon_N\longrightarrow0,
 \tag{3}
\]
uniformly in its stated physical colors and on each fixed \(|s|\le R<1\). Here
\[
 J(x)=\int_0^x\log(2\sin\pi t)\,dt,
 \qquad g(x)=J(2x)-4J(x),\quad 0\le x\le\tfrac12.
 \tag{4}
\]
The constants \(c_i\) are the original accumulated branch actions, not independently assigned cap volumes. All finite \(r/N\)-to-\(r/d\) changes have uniform cost \(O(\log N)\) in the exponent, including endpoints.

The profile labels describe open branches of the positive complete calculation. A rigid branch, called type \(L\), has output interval \((0,1/2)\) and optimized action \(g(b)+c\). A composite branch of type \(A\) has strict output interval \((0,1)\); it may contain products and turns. The symbol \(C\) denotes the prescribed cylindrical closing trace. In \(C(hA^0)\), the expression \(A^0\) is the positive reference defined below and \(h\) is the pure rigid comparison leaf with profile \(g\). It implements the output norm estimate; it is not an added physical crossing circle.

Expose the component as an unturned product expression \(A\), and put \(Q=T_s(A)\). Let \(A^0\) be the complete positive reference with the same tree and pure rigid boundary profiles. The intrinsic probe action is
\[
           \Omega_Q=\Phi_{C(hA^0)}+\sum_i c_i.
 \tag{5}
\]
The original strict probe geometry identifies this with the pressure of that same branch. Assume the reference has its original strict state; this is automatic for the unturned component with L/A inputs used in the strict reduced-tree induction.

For a canonical polynomial \(F\) of degree less than \(N\), \(\|F\|_{\mathcal J}\) is the maximum of the values \(|F(c_j)|\) at distinct complete nodes and the derivative magnitudes \(|F'(c_j)|\) at double nodes. At odd levels \(-2\) is simple and contributes only its value. This norm retains all first Hermite normal coordinates: a polynomial can vanish at every node while its derivative at a double node remains nonzero.

**Component theorem.** There is a fixed \(\eta>0\) such that
\[
                 \|Q_{N,s}\|_{\mathcal J}
                       \le e^{N(\Omega_Q+o(1))}.
 \tag{6}
\]
There is also an exact decomposition into a clean complete-tensor contraction and a grouped remainder:
\[
 Q_{N,s}=Q^{\mathrm{clean}}_{N,s}+E_{N,s},
 \qquad \|E_{N,s}\|_{\mathcal J}
                    \le e^{N(\Omega_Q-\eta+o(1))}.
 \tag{7}
\]
In \(Q^{\mathrm{clean}}\), all bare tensors use \(\phi_0\), all external component inputs and the output are low, and every original complete-supported internal index is retained. The physical paired edge factors and actual low boundary arrays remain in this contraction. Its coefficientwise absolute value is bounded by a subexponential multiple of the same complete positive reference, with the constants in (5). High original boundary inputs and a high output have the strict loss in (7).

The assertions hold through both parities and on every fixed \(R<1\). The fixed geometric and regular-window losses can be chosen before \(R\); polynomial prefactors and the eventual level threshold may depend on \(R\). An inherited loss in one full boundary array subtracts that loss from every estimate by homogeneity. No internal high index is automatically discarded from the clean complete contraction.

## 2. Three exact local inputs

Write \(V_s(\mathbf n)=\phi_s(\prod e_{n_i})\) and \(\delta V_s=V_s-V_0\). Fixed valence is understood in all polynomial prefactors.

First, for an all-low tuple,
\[
 |V_s(\mathbf n)|+|\delta V_s(\mathbf n)|
                      \le N^{C_R}V_0(\mathbf n).
 \tag{8}
\]
The first bound is the same-level all-parity whole-trace theorem in [source bounds and typed coefficient extractors](actual_main_meridian_source_bounds.md), Section 2; the second follows by the triangle inequality. It keeps all signed Fourier aliases together. On a compact regular all-low window with strictly positive whole-junction support slack,
\[
       |\delta V_s(\mathbf n)|
              \le N^{C_R}e^{-\kappa N}V_0(\mathbf n).
 \tag{9}
\]
This is the regular bare trace theorem, [regular bare-trace estimate](actual_main_meridian_regular_bare_trace.md): the first Fourier alias is independent of \(s\), and the remaining aliases have a strict rate loss. The window requires each incident normalized label in a compact subset of \((0,1/2)\) and the sum of the labels strictly greater than one. A cubic tuple with at most one high index instead has \(\delta V_s=0\) exactly by degree, so no low-window assertion is needed for its half-label exception.

Second, if precisely one index is high, say \(h>m\), and \(F\) is the product of the low factors, set \(r=d-h\). Then
\[
 |\delta\phi_s(e_hF)|
   \le N^{C_R}|\Delta_s|\,\phi_0(e_rF).
 \tag{10}
\]
This is a comparison with a *reflected* complete tensor. It is not a comparison with \(\phi_0(e_hF)\), which can be exponentially smaller. The exact proof is [high-index Fourier reflection](actual_main_meridian_high_fourier_reflection.md), Sections 1–4. Briefly, the high polynomial has two signed Fourier tails and polynomial Laurent norm. Alias one cancels in \(\delta\phi\), so only frequencies at least \(2N-1-h=N+r\) remain. The endpoint coefficient of \(e_r\), the interval-tail lemma and the all-low theorem recover the positive complete trace on the right at the original level, including even parity. When all low factors lie in a fixed compact interval inside \((0,1/2)\) and \(r/N\) is bounded below, the strict convolution-concavity comparison at frequencies \(N+r\) and \(N-1-r\) strengthens (10) to
\[
 |\delta\phi_s(e_hF)|
   \le N^{C_R}|\Delta_s|e^{-\kappa N}\phi_0(e_rF).
 \tag{11}
\]
The estimate includes \(r/N\) near half. If its right side vanishes, (10) already gives exact zero. The exponent \(\kappa\) is fixed before \(R\).

Third, for any tuple, the full spectral-jet estimates and finite-degree Chebyshev folding give
\[
 |V_s(\mathbf n)|
       \le N^{C_R}\exp\left\{N\sum_{i:n_i\le m}g(n_i/d)\right\}.
 \tag{12}
\]
Every high basis polynomial has polynomial full-jet norm; each low one has rate at most \(g\). Quotient multiplication of a fixed number of factors and the trace have polynomial cost. This does not discard high first normals. With at least two high indices, \(V_0=0\) by its pairwise support, so (12) also bounds \(\delta V_s\).

For an old whole junction with at least two half incidences,
\[
 V_D^{\mathrm{action}}(\tfrac12,\tfrac12,x_3,\ldots,x_D)
                              =\sum_{i=3}^Dg(x_i),
                       \quad 0\le x_i\le\tfrac12.
 \tag{13}
\]
Additional half incidences cost zero. The exact calibration at odd \(N=2m+1\) is
\(\phi_0(e_m^2F)=F(-2)\), \(e_m(-2)=1\): the square kills both jets at all double nodes and is the normalized simple-node projector. The parity-independent closed old action gives (13), including zero arms. The complete derivation and the arbitrary-valence simultaneous reassembly are in [component pressure comparison](actual_main_meridian_component_pressure.md).

## 3. Expand differences and retain the sector graph

Expand every moving tensor by the exact identity
\[
                         V_s=V_0+\delta V_s.
 \tag{14}
\]
There are finitely many choices because the original tree is fixed. Then partition its finite label sum into low/high bands. At a selected difference tensor there are three possibilities: no high incidence, one high incidence, or at least two high incidences. Apply (8), (10), or (12), respectively. Unselected tensors and constant-quotient tensors retain their exact complete positive values. A term outside any such complete support is zero.

A selected one-high difference with an internal high incidence meets a constant old vertex. Its moving endpoint has no other high incidence; its old endpoint has at most one high incidence by the complete pairwise support. Therefore the selected internal high edges form a matching. Reflecting the moving endpoint changes their equal-index contraction into the complementary metric contraction. Precisely,
\[
 \sum_{i=0}^d\phi_0(Ae_i)\phi_0(e_{d-i}B)=\phi_0(AB).
 \tag{15}
\]
This is the exact full Frobenius identity; the dual basis is \(e_{d-i}\). It fuses the two adjacent complete product junctions after the selected turn is deleted. The other low incidences remain correlated inside the resulting whole tensor. No low arm is replaced by an independent \(g\) profile in this step.

Call the set of these edges \(S\), and the contracted old tree \(\mathcal G/S\). Its induced ribbon orders are obtained by substituting the child product into its original position. The valence of a fused pair is \(D_1+D_2-2\ge4\). Because \(S\) is a matching, every fused hub has only low exterior incidences in the original sector. The restored complementary index in (15) can be kept as a hidden unturned wire in a prescribed resolution; summing it gives exactly the fused positive tensor. Discarding its band restrictions only enlarges that positive comparison.

![A trace difference is bounded by a reflected complete pairing, which fuses into one product junction.](../book/figures/main-meridian-reflected-turn-fusion.svg)

The drawing records a tree of operations, not a knot diagram. Reflecting one endpoint changes equal covariant labels into complementary labels. The positive sum then fuses the two junctions in their induced order, retaining the other branches. The physical source and its peripheral marking are unchanged; the fused tree is used only to bound its pressure.

The pressure of this full comparison tree satisfies
\[
                         F(\mathcal G/S)\le F(\mathcal G).
 \tag{16}
\]
The proof is [component pressure comparison](actual_main_meridian_component_pressure.md). For one deleted edge the two rooted profiles are actual unturned products with L/A inputs. They obey \(f_X(b)\ge f_X(1-b)\) for \(b\ge1/2\), by derivative domination over the symmetric two-leaf profile. Hence
\[
 \max_b[f_A(b)+f_B(1-b)]\le\max_b[f_A(b)+f_B(b)].
 \tag{17}
\]
The fused tree remains in this old pressure class, so the comparison iterates using its current coupled profiles. The constants never change. Equality can occur, notably when a cut side is the two-leaf product. Thus (16) alone is not a strict error estimate.

If a selected one-high difference instead meets an original external coefficient array, there is no edge to fuse. Change its summation variable from \(h\) to \(r=d-h\). Its coefficient has rate \(c_i\), whereas the low reference coefficient has rate \(g(r/d)+c_i\). This introduces the nonnegative surplus
\[
                                  g(r/d).
 \tag{18}
\]
Keep that surplus for the strict estimate; it is not an altered physical coefficient or a new circle.

## 4. Sectors with several-high tensors or unreflected high boundaries

The selected several-high moving vertices are never fused. They remain pairwise nonadjacent. A fusion in (15) does not create a new high exterior incidence: its endpoints had only the selected high edge. Removing the several-high vertices therefore leaves old regions with at most one high marked incidence at each retained old hub. Their other incidences retain their complete correlations.

At a low arm of a removed several-high vertex, charge its \(g(x)\) from (12) to the adjoining old region as an ordinary free boundary profile. At a high arm mark the adjoining old boundary. Original unreflected high external inputs, including a high output probe, have rate \(c_i\), not \(g(x)+c_i\) at \(x>1/2\); mark those boundaries too. Each old hub still has at most one mark. All original constants are retained exactly once.

The arbitrary-valence old simultaneous-half theorem applies jointly to every marked region. It changes all its high marked labels to half without decreasing its upper comparison pressure. Reinsert each removed vertex by (13), using the low-arm values chosen by the neighboring region optimizers. Its old cardinal action consumes each previously assigned \(g\) once. External low arms keep their own boundary \(g+c_i\) in addition to the cardinal contribution; external high arms become half with \(g(1/2)=0\). Zero arms and all other closed endpoints follow by continuity.

This constructs a feasible state of the same contracted complete tree. At least one pair at a reinserted vertex is saturated, or an original high boundary has become a half leaf. Either is a closed boundary face disjoint from its unique strict maximum. The compact action polytope consequently gives a fixed strict loss below \(F(\mathcal G/S)\), and hence below the original pressure by (16).

If there are no several-high vertices but an original external/probe high remains unreflected, apply the existing complete arbitrary-component high-input/probe theorem to the fused old tree. The same old-half argument marks its high external incidences and yields its strict boundary loss. This step precedes all regular-saddle reasoning. A high original array is never treated as a low pure leaf without its separate comparison.

The finite number of band patterns and possible sets \(S\) permits a common positive loss. Uniform closed factorial errors and all polynomial factors are absorbed into its half, for sufficiently large levels. These arguments also cover sectors with both one-high differences and several-high tensors; the matching property is what preserves the old-region mark hypothesis after fusion.

## 5. Remaining correction sectors near a contracted strict maximum

It remains to treat a nonempty difference sector with no several-high tensor and no unreflected original high boundary. After the comparisons above it is bounded by a complete positive contraction of \(\mathcal G/S\), retaining all restored unturned wires and any reflected external label. The reference maximum is unique and strict. Outside any fixed neighborhood of it, the positive resolved action has a fixed compact gap. It remains to examine that neighborhood, where a mere polynomial comparison would not suffice if (16) is an equality.

If an external one-high difference is present, its reflected label at the strict reference maximum is in \((0,1/2)\). Since \(g\) is positive there, the surplus (18) has a fixed positive lower bound in a small neighborhood. It gives the required exponential loss. Boundary limits of that label are outside the strict maximizing neighborhood and were already covered by compact separation.

Suppose next that an internal one-high difference is present. Then \(S\ne\varnothing\), and the fused tree has a hub of valence at least four. The old complete physical-edge theorem says every remaining physical internal label is strictly below half: its only equality exception is the entire two-trivalent-hub tree, which is impossible here. Ordinary boundary labels are also strictly between zero and half. These statements concern physical edges; hidden unturned wires are not required to be low.

At the selected reflected vertex, every factor other than the reflected one is an exterior incidence of its fused pair. The matching property ensures none of these is another restored unturned edge. Its labels therefore lie in a fixed compact interval inside \((0,1/2)\). Write \(x_r=r/d\) for the normalized restored reflected wire. It is strictly positive at the resolved strict maximum. If that maximum has \(x_r>1/2\), the sector restriction \(r\le m\), equivalently \(x_r\le m/d\), is separated from it and the sector has a compact gap. Otherwise, in its allowed portion of a small neighborhood, \(x_r\) stays bounded below and all the other factors are in the regular low interval. Estimate (11) supplies a fixed exponential loss. It is valid also when the limiting \(x_r\) equals half.

Finally suppose there is no selected one-high difference, internal or external. Then \(S\) is empty, and every selected difference has all incidences low. The comparison is the original old tree. At its strict optimizer all physical labels are strictly low except for the two-trivalent-hub exception. In the nonexceptional case, each selected junction has regular low incident labels and strict whole-hub total slack; (9) supplies a loss. In the exceptional case every bare tensor is cubic, and the selected all-low difference is identically zero by the degree bound. More generally a nonzero all-low difference must occur at a noncubic junction, which itself excludes that exception.

These alternatives exhaust the nonempty difference sectors. At least one strict analytic factor suffices; other selected differences may keep their polynomial old majorants. The uniform finite-angle and radius constants are harmless because the tree is fixed. We obtain
\[
  \sum_{\text{nonempty difference sectors}}
      |Z_{N,\mathrm{sector}}(s)|
                \le e^{N(F(\mathcal G)-\eta+o(1))}.
 \tag{19}
\]
This is an absolute bound after the stated whole-tensor regroupings. It is not a bound on each signed coefficient of a high polynomial or on the absolute sum of an unregrouped crossing-state expansion.

## 6. Norm extraction, clean reference, and inherited errors

The output probe is made explicit by the exact typed turn formula. In the appropriate constant or moving trace,
\[
 [e_r]Q=\frac{\gamma_N(s)W_{d-r}(s)}{H_N(s)}\,
                                  \phi_\sigma(e_rA),
 \qquad
 \|Q\|_{\mathcal J}
     \le C_RN^C\sum_{r=0}^d w_{N,r}|\phi_\sigma(e_rA)|,
 \tag{20}
\]
where \(w_{N,r}=e_r(-2)\) at low indices and \(w_{N,r}=1\) at high indices. The low weight has the same closed rate \(g\) as an ordinary boundary, and the high one has rate zero. Also
\[
 H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)},\qquad
 W_r(s)=\prod_{j=1}^r\left(1-\frac{\sin^2(\pi s/N)}
                                      {\sin^2(\pi j/N)}\right),
 \qquad \gamma_N\in\{1,q^{s^2/2},q^{-s^2/2}\}.
 \tag{21}
\]
The paired factors and their inverses are uniformly bounded on fixed \(R<1\). Apply Sections 3–5 to this probe-closed tree. Its original action is exactly (5), not the pressure of a newly inserted physical crossing circle. The high-probe case is the high-boundary case of Section 4. Summing (20) costs only a polynomial factor and proves (6)–(7).

For the empty difference sector with all external indices low, coefficientwise comparison with the original positive reference follows directly from (3), the positive old product law, and bounded paired factors on the finitely many physical edges. The exact pure complete coefficients have the same closed rate \(g\), with a uniform polynomial ratio. The clean contraction therefore preserves the original full positive low-output profile; it is not reset to \(g+c\) after a bare component. All original complete internal indices remain in this term.

If one full input array improves by \(e^{-N\gamma}\), every multilinear contraction, trace comparison, and positive majorant above improves by that same factor. The constants in every reference profile shift by \(-\gamma\); the stationary labels, deletion comparison, compact gaps, and cardinal identities do not change. There is no extra charge of \(2G_0\) at an internal turn. This proves inherited-error propagation for the whole coefficient array and hence for its converted spectral norm.

An input known only to have a small \(\mathcal J\)-norm is not declared to satisfy (3) by generic coefficient recovery. In the actual reduced-tree induction it first passes through the intervening circle-marked or decorated extractor, including its physical coupon and turn. Equations (D23)–(D24) of [source bounds and typed coefficient extractors](actual_main_meridian_source_bounds.md) give the low-\(g\)/high-zero cone at precisely that interface and propagate the inherited loss. The low trace probe costs \(g\); the high probe has polynomial norm. This conversion is performed once there. No new conversion is needed inside a whole bare component, whose inherited boundary arrays already satisfy the full cone (3). It is not inferred from a pointwise boundary profile or an independent cap budget.

## 7. Fresh Gaussian localization and the global source induction

The clean low output retains the old probe profile
\[
                       f_A(1-u)+g(u)+\sum_i c_i.
 \tag{22}
\]
Its intrinsic maximizer is strictly inside \((0,1/2)\). The original complete probe has a unique strict state and an off-window gap. On a compact interval around that output, the exact low Newton spectral factor has a negative angular quadratic term. Summing the low clean coefficients gives the same fresh Gaussian at its actual \(\Omega_Q\). The grouped error in (7), and every clean output away from the interval, has a fixed rate gap. Canonical Hermite interpolation and the finite-degree Bernstein bound absorb these terms on a sufficiently small complex angular strip. This is precisely the coefficient/profile-to-Gaussian argument in [spectral propagation theorem](actual_conway_mixed_core_spectral_propagation.md), Sections 1–4, with the component cone and high gap now supplied without a valence restriction.

The mutual global induction therefore has the same two genuine interfaces. A circle-marked junction uses the physical decorated-character or fixed-crossing cone, whose input is the actual neighboring spectral budget. A bare component uses the theorem above and retains its original low profile plus a grouped small remainder. The intrinsic rigid/probe geometry accounts for all constants and gives the original root action. No independent cap action is substituted for a shared boundary.

For fixed crossing powers \(R_s^{n_i}\), their physical polynomial norms have polynomial size on fixed \(R<1\); this supplies the same augmented-budget cone, with constants depending on the fixed powers. It does not yet identify the smaller filled exponent. Original auxiliary colors and fixed half-twist choices instead use the existing full-color cone uniformly. Descendant full-array losses propagate as in Section 6. Exposing any original circle by the exact typed adjunction then supplies the same raw spectral Gaussian at the original root pressure. The auxiliary-color contour argument consequently has its original scope \(R<1/2\), without a component-size restriction. The source upper bound itself has scope \(R<1\).

The root with no unturned circle operator uses an existing ordinary leaf and the original typed self-adjoint pairing; it introduces no extra \(2G_0\). The two-leaf case remains the previously treated case with its original knot/pure-leaf qualification. The present component proof does not alter it.

## 8. The original complete wire window and complex angular parameters

For an arbitrary old bare tree with rigid boundary profiles, the strict optimizer has all physical internal labels below half except for the entire two-trivalent-hub component, whose one internal label is half. This follows by cutting an edge: the pressure is \(f_A(1-z)+f_B(1-z)\), and each actual unturned product satisfies \(f_X'\ge f_2'\), strictly unless it is the isolated two-leaf product. Thus its derivative is negative above half and at half except in that one case. This is [component pressure comparison](actual_main_meridian_component_pressure.md).

Consequently every nonexceptional whole bare vertex is in the regular all-low trace window at the original complete state. Its moving trace can be replaced by its complete trace with exponential relative error (9). The exceptional vertices are cubic and have exact moving/complete equality on the entire strict old window, since their raw degree is less than \(2N-1\). Hidden unturned-resolution labels can exceed half and remain in the original bulk domain.

The original ordered positive resolutions supply exactly the previous primitive lattice and all \(d=N-1\) offsets. No turn is deleted from this local physical packet. Deleted/fused trees were only upper comparisons for error sectors. The actual clean packet uses the original tree, original physical edges and original peripheral marks.

The canonical Gamma interpolation for \(H_N/W_r\) is regular on every compact \(0<x<1\), including half. Gate factorial arguments are bulk by strict old support. Circle angular factors require compact low incident labels; those follow from the original rigid/probe geometry. The strict Hessian, midpoint offsets, finite cotangent currents and positive elimination used in [grouped wire packet](actual_main_meridian_grouped_wire_packet.md) are unchanged. The relative conditioning uses the positive complete wire majorant and the nonzero complete signed packet at the same \(N^{3/2}\) scale, not an unregrouped crossing-state total variation.

The grouped errors in Sections 3–6 are estimated in the full physical fixed-power contraction before any circle contour is moved, exactly as in Section 4, equations (18)–(20), of the current grouped-packet proof. They remain an additive scalar error; no analytic angular continuation of an individually discarded sector is required. For the retained finite packet, every circle-incident index lies in its regular low interval. Its exact factors \(e_n(-2\cos\tau)\), canonical Gamma interpolation, and the original angular Gaussian give the same real-spectator and small-complex-strip estimates as Section 7 of that proof. Every circle has an incident edge, so each angular variable retains a strict Gaussian loss. The finite-current and endpoint estimates apply to this clean packet. The structural source gap, the wire box and the packet strip are fixed-tree choices independent of the filling powers. The compact meridian disk changes polynomial constants, not the complete action or the strict geometric/Fourier losses.

## 9. What is needed to pass to the filled invariant

The new component estimate supplies the missing global source error bound. To obtain the filled nonzero asymptotic one must still use all of the established interfaces, in their original order:

1. The regular physical circle trace and its canonical Gamma wire interpolant retain the exact type, Cartan scalar, ordinary-circle normalization and the chosen entire continuation. They are the proofs in [regular physical circle trace](actual_main_meridian_regular_circle_trace.md) and [direct crossing trace](actual_main_meridian_direct_crossing_trace.md).
2. The finite original wire packet, its strict complex saddle, and its real-spectator angular Gaussian use the unchanged local window described in Section 8. All hidden unturned variables and physical-edge insertions remain in that packet.
3. The joint filling transform retains every charge. Its tail truncation has a fixed loss with real spectators, and its componentwise charge comparison treats independently long signed powers without comparing their ratios. A minimum local alias error is not compared with the total filled action drop.
4. The original marked geometry supplies the smooth fillings, the primitive peripheral equation and the absolute filled action. All pressure comparisons in this note end at the original augmented action; no fused comparison diagram contributes a substituted volume.

These hypotheses are exactly those proved in [grouped wire packet](actual_main_meridian_grouped_wire_packet.md) and [joint filling transform](actual_main_meridian_joint_filling_transform.md). Their proofs depend on the component class through the global grouped errors and the regular original window. Sections 6–8 supply those two inputs for every fixed strict bare component. The joint first-charge nonzero coefficient, reflected-sign sum and primitive Hessian are unchanged.

Choose a structural error margin from the finitely many sectors above, together with the unchanged regular packet margin. The original long-filling implicit theorem makes the total action drop smaller than this margin when every fixed signed power is sufficiently long. The joint charge proof then handles arbitrarily unbalanced such powers. As before, the resulting slope threshold is fixed before \(N\) and before the disk radius \(R<1\). The subsequent maximum-principle extension changes starting levels and error constants, not that threshold.

## 10. Exact normalization and the resulting scope

With the interfaces in Section 9, the formulas of [filled meridian-profile and volume theorem](actual_main_meridian_filled_volume.md), equations (5)–(7b), retain their exact meaning for every fixed strict literal Conway tree, without the former singleton/trivalent/path alternative for bare components. In particular the reduced zero-framed scalar has marked meridian \(M=q_N^s\), and the exact factors remain
\[
 H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)},\qquad
 A_N(s)=q_N^{a(D)s^2/2},\qquad
 a(D)=-w(D)-\sum_i n_i.
 \tag{23}
\]
The reduced profile is \(A_NH_N(1+O(N^{-1}))\) on fixed \(R<1\), while the full modified dimension cancels exactly the one factor \(H_N\). The absolute exponent is the volume of the original filled knot complement. The first correction uses the original filled labels and the preferred cusp
\[
                 \tau_K=a(D)+2i\sum_{e\ \mathrm{physical}}
                                      \cot(\pi x_e^{\mathrm{fill}}).
 \tag{24}
\]
No fused edge is removed from this sum; fusion appeared only in upper comparisons. The scalar ledger and the geometric preferred-longitude proof already apply to the full original strict class.

This conclusion retains every other theorem hypothesis: a fixed literal ordered presentation and its strict positive domain; the original one-component/knot and framing conventions; the prescribed parity pattern and signed long powers fixed before the level; the two-leaf pure-leaf qualification; and the original marked filling completion. It does not classify arbitrary link diagrams or remove the need for a strict normalized presentation. A separate topological normalization theorem, if invoked, must still transport the full marked invariant rather than only its complete scalar.

The [local pointwise counterexample](actual_main_meridian_same_index_obstruction.md) is fully compatible with this result. A one-high moving tensor can be exponentially larger than its same-index complete value. The proof bounds its difference by a reflected complete tensor, preserves its correlations by exact fusion, compares the whole fused pressure with the original one, and supplies the missing strict loss at an equality saddle through the Fourier tail. No step restores the disproved pointwise inequality.
