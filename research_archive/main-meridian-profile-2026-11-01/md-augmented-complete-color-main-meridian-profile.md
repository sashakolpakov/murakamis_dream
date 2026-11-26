# The complete-auxiliary-color profile of the actual augmented source

This private assembly concerns the reduced quantum source with every original crossing circle colored by \(N\). The circles remain unfilled. It combines the actual local meridian kernels with a global high-label error invariant and the nonzero complete packet. No filling profile is inferred.

The distinction between local coordinates, a contracted scalar, and its framing is kept throughout. In particular the final profile contains one primitive cut factor and the exact recorded scalar ratio of the original framing and mark.

## 1. The class and statement

Fix an ordered strict Conway construction with \(H\ge2\) original circle pieces and half-twist choices \(\epsilon_i\in\{0,1,-1\}\). Retain the knot/component hypotheses of the complete source theorem. For \(H=2\), in particular, a knot pattern contains a pure leaf; the both-odd two-component pattern is not added here.

Collapse consecutive unturned products into product junctions, retaining the actual quarter-turn on every remaining edge. A junction is flagged when it carries one original unturned circle coupon \(R^{\epsilon_i}L_N\), and bare otherwise. Ordinary leaves are represented by their original turned circle coupons. Strictness gives at most one flagged original leaf at a junction. This is the exact reduced source tree, not a claim of a new tangle isotopy.

Every maximal connected component \(\mathcal U\) of bare junctions is required to satisfy one of the following alternatives:

* it consists of one junction, of arbitrary fixed valence at least three;
* writing \(b_v=d_v-\deg_{\mathcal U}(v)\) for its number of boundary incidences, all \(b_v\ge5\), and
\[
 \eta_{\mathcal U}:=2G_0-
 \max_{\mathcal P\text{ simple path in }\mathcal U}
      \sum_{v\in\mathcal P}\varepsilon_{b_v-1}>0,
\tag{1}
\]
where
\[
J(u)=\int_0^u\log(2\sin\pi t)\,dt,\quad
 g(u)=J(2u)-4J(u),\quad G_0=g(1/4),
\]
\[
\varepsilon_k=(k+1)
 \left[J\left(\frac14+\frac1{k+1}\right)
       +J\left(\frac14-\frac1{k+1}\right)-2J(1/4)\right].
\tag{2}
\]
All trees are fixed before the level grows. The already established separated-bare-junction class is the first alternative for every component. A simple sufficient condition for the second is
\(b_v\ge\max(8,4|\mathcal U|)\), since
\(\varepsilon_{b-1}\le\pi\sqrt2/b\) for \(b\ge8\), and its total is strictly less than \(2G_0\). The strict path inequality, not this coarse sufficient count, is the actual hypothesis.

Put \(q_N=e^{\pi i/N}\), \(d=N-1\), and \(M=q_N^s\). Let
\(\mathcal F_{N,\mathbf N}^{\epsilon}(M)\) be the actual reduced source, with all auxiliary colors \(N\), in the specified main-cut and framing convention. The notation \(\mathbf N\) emphasizes that these colors are not being summed. Let \(F_0\) be its original complete action, so under the marked geometric hypotheses
\(2\pi F_0=\operatorname{Vol}(Y^\epsilon)\), where the augmented complement \(Y^\epsilon\) still has all crossing-circle cusps.

The exact compiler supplies a recorded scalar \(\zeta_N(s)\), containing only the original global framing and closing mark not already placed in local tensors. It is specified by that finite diagram and its conventions, not by values of the unknown invariant. Section 2 defines another explicit state-independent local scalar \(\Gamma_N(s)\). Both equal their prescribed complete values at zero; we normalize \(\Gamma_N(0)=1\).

**Theorem.** On every fixed disk \(|s|\le R<1\), through both parities,
\[
\boxed{\displaystyle
\frac{\mathcal F_{N,\mathbf N}^{\epsilon}(q_N^s)}
     {\mathcal F_{N,\mathbf N}^{\epsilon}(1)}
 =\frac{\zeta_N(s)}{\zeta_N(0)}\,
    \Gamma_N(s)\,
    H_N(s)\,[1+O_R(N^{-1})],
\qquad H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)}.}
\tag{3}
\]
The removable value is \(H_N(0)=1\). The error is holomorphic and has the same order for every fixed derivative on smaller disks after dividing out the displayed exact factors. The denominator is nonzero for all sufficiently large levels by the actual complete packet.

This is a complete-auxiliary-color augmented-source profile. The proof neither uses the old filling coefficients at a moving main meridian nor asserts a profile for the filled knot. It also does not replace \(\zeta_N(s)/\zeta_N(0)\) by one without evaluating the original normalization ledger.

## 2. The exact covariant contraction and its scalars

Use the fixed complete Newton basis
\[
 e_r(z)=S_r^{-2}\prod_{a=0}^{r-1}
          \bigl(2\cos((2a+1)\pi/N)-z\bigr),\qquad
 S_r=\prod_{a=1}^r2\sin(\pi a/N),
\]
and put \(m_N=\lfloor d/2\rfloor\). The relation on an equal-color object is
\(P_s=\mathcal T_N+2\cos2\pi s\); on an opposite-color object it is \(P_0\). In either case
\[
\phi_\sigma(F)=(-1)^dN^2[z^d]\operatorname{rem}_{P_\sigma}F,
\qquad \phi_\sigma(e_a e_b)=\mathbf1_{a+b=d}.
\tag{4}
\]
All indices below are lower tensor indices. A bare junction contributes
\[
 V_{v,N,s}(\mathbf n)=\phi_\sigma\left(\prod_{e\sim v}e_{n_e}\right).
\tag{5}
\]
A flagged junction contributes
\[
 V_{v,N,s}^{\epsilon_v}(\mathbf n)
   =\phi_\sigma\left(R_\sigma^{\epsilon_v}L_N
                       \prod_{e\sim v}e_{n_e}\right),
 \qquad L_N=(-1)^dU_d(z/2).
\tag{6}
\]
An ordinary original leaf is a univalent vertex of (6), attached by its original turn. Thus there is exactly one circle vertex for each original circle, whether univalent or absorbed into a junction. Mixed-object polynomial references include their actual carriers and monodromy scalars.

Let \(\mathbf J_{ab}=\mathbf1_{a+b=d}\). The physical turn in fixed coordinates is
\[
T_{e,s}=\frac{\gamma_{e,N}(s)}{H_N(s)}
        \mathbf J\operatorname{diag}(W_n(s)),\qquad
W_n(s)=\prod_{a=1}^n
 \left(1-\frac{\sin^2(\pi s/N)}{\sin^2(\pi a/N)}\right).
\tag{7}
\]
Its scalar \(\gamma_{e,N}(s)\) is the specified \(1\) or \(q_N^{\pm s^2/2}\). Since \(W_nW_{d-n}=H_N^2\), raising the neighboring lower index gives the propagator
\[
 (T_{e,s}\mathbf J)_{ab}
   =\delta_{ab}\,\gamma_{e,N}(s)\frac{H_N(s)}{W_a(s)}.
\tag{8}
\]
Thus the two edge labels are equal. This exact identity, including the order \(T\mathbf J\), is the source convention used in this proof. Resolving a product junction into binary products would introduce complementary-label unturned edges; no high-edge forest inference across such artificial edges is made.

Define the normalized contraction
\[
 S_N^{\epsilon}(s)=\sum_{\mathbf n\in\{0,\ldots,d\}^{E}}
   \prod_v V_{v,N,s}(\mathbf n_v)
   \prod_{e\in E}\gamma_{e,N}(s)\frac{H_N(s)}{W_{n_e}(s)},
\tag{9}
\]
with (6) used at circle vertices. Any recorded root adjunction phase can be put in \(\zeta_N\); this choice is fixed once and does not move a state-dependent factor into the normalization. The primitive closing moment is exactly
\[
\mathcal F_{N,\mathbf N}^{\epsilon}(q_N^s)
      =\zeta_N(s) H_N(s)S_N^{\epsilon}(s).
\tag{10}
\]
There is only one surviving primitive cut factor. Formula (10) is the compiler's pivotal trace identity, not a normalization chosen to obtain a desired limit.

At an equal-color circle vertex the local regular-window ratio has state-independent factor \(q_N^{-\epsilon_v s^2/2}\). At a constant opposite-color circle vertex let \(\rho_{v,N}(s)\) denote its exact scalar reference ratio: the polynomial is the fixed complete crossing/circle polynomial, and the only change is its specified monodromy scalar. In the adopted coherent references these are retained powers of \(q_N^{s^2}\), or one. Define
\[
\Gamma_N(s)=
 \prod_{e\in E}\gamma_{e,N}(s)
 \prod_{v\text{ equal circle}}q_N^{-\epsilon_v s^2/2}
 \prod_{v\text{ opposite circle}}\rho_{v,N}(s).
\tag{11}
\]
This is an explicit finite product from the oriented tree. It is independent of the summed labels. It and its inverse are bounded on every fixed disk, and \(\Gamma_N(s)=1+O_R(N^{-1})\). We nevertheless retain it in (3).

For example the standard ribbon twist of \(V_{d+s}\) is
\[
\theta_{d+s}=q_N^{((d+s)^2-2d(d+s))/2}
            =q_N^{(s^2-d^2)/2}.
\tag{12}
\]
A zero-framing correction of writhe \(w\) therefore has ratio \(q_N^{-ws^2/2}\). This verifies that particular contribution to \(\zeta_N(s)/\zeta_N(0)\); it is not a reason to discard another prescribed closing or mark factor. All normalization choices are evaluated in the actual finite compiler before applying the theorem.

## 3. An exact low-state positive majorant

For a product \(E=\prod_{a=1}^B e_{n_a}\) of low factors, \(n_a\le m_N\), its Laurent coefficients at \(-u-u^{-1}\) are nonnegative. At every complete Casimir node each individual low factor is nonnegative. The complete circle trace is consequently
\[
\phi_0(R_0^\epsilon L_NE)
 =N\sum_{r=0}^{N-1}R_0(c_r)^\epsilon E(c_r),\qquad
\phi_0(L_NE)=N\sum_rE(c_r),
\tag{13}
\]
where the actual full crossing values have modulus one. Therefore
\[
|\phi_0(R_0^\epsilon L_NE)|\le\phi_0(L_NE)
\tag{14}
\]
exactly, at both parities. Its full first-normal data have not been discarded: the complete-color factor \(L_N=(-1)^dP_0'/N\) is precisely why this particular confluent trace equals a node sum.

For moving parameters the all-index circle-junction comparison is
\[
|\phi_\sigma(R_\sigma^\epsilon L_NE)|
 \le C_{B,R}N\,\phi_0(L_NE).
\tag{15}
\]
The exact shifted-grid chirp bounds the left side by \(C N^2E(-2)\). At odd levels \(-2\) is a node; at even levels the nearest node gives
\(e_n(-2\cos(\pi/N))/e_n(-2)\ge(N/2)\tan(\pi/(2N))\ge\pi/4\).
This proves (15) even at the low-index endpoints. The full derivation is Section 9 of the physical-leaf regular-window report.

At a bare vertex the all-parity signed trace theorem gives
\[
|\phi_\sigma(\prod e_{n_a})|
       \le N^{C_B}\phi_0(\prod e_{n_a}).
\tag{16}
\]
The right side is nonnegative by the original positive Newton law. The edge multipliers (8) are uniformly bounded for all indices on \(R<1\). Thus every all-low state of (9) is bounded by a fixed power of \(N\) times the corresponding original complete pure state. At \(s=0\) the stronger exact inequality (14), nonnegative bare tensors and unit edges give
\[
\sum_{\mathbf n\text{ all low}}|w_{N,\mathbf n}^{\epsilon}(0)|
 \le\sum_{\mathbf n\text{ all low}}w_{N,\mathbf n}^{0}(0)
 \le S_N^0(0).
\tag{17}
\]
The final inequality uses nonnegativity of the entire original complete pure contraction, including states outside this low restriction.

## 4. Grouped high-label errors and the component path budget

We explain why the high-label complement of (9) has a strict loss. The conclusion is a bound on its signed, locally contracted sum. It is not a bound on the sum of absolute values of every internal crossing path or individual return term.

For an L branch of original profile \(g+c\), the actual decorated theorem supplies low coefficients of rate \(c+g\), high coefficients of rate \(c\), and intrinsic spectral pressure \(\Omega_L=c+2G_0\). A strict spectral loss \(\eta\) in an input product passes through a decorated operation as a full coefficient-cone loss \(c-\eta\). This last statement follows directly from the linear coefficient extractor; it applies simultaneously to low and high coordinates.

Separate an L branch into a clean part keeping all its edges low, errors inherited from its descendants that have a full cone loss, and a boundary-high term supported on high output indices. The boundary-high term has spectral gap \(2G_0\). For an ordinary leaf there are no inherited errors. At a flagged junction, expansion in the child errors and the actual decorated estimate convert every inherited spectral deficit into a full cone deficit. The all-clean output is split into low and high parts. This is an exact finite decomposition.

For a bare component, the original positive references retain every boundary profile. An L input has comparison polynomial \(e^{Nc}h_N\); a bare output has comparison \(T_0\prod Q_i^0\). These are positive comparison polynomials, not an equality with the physical finite subtrees. Let \(\Omega_i\) be the true child pressures and \(\Omega_v\) the outgoing reflected pressure. The unreflected pressure is exactly \(\sum_i\Omega_i\), and put \(\Delta_v=\Omega_v-\sum_i\Omega_i\). The exact conditional transfer has error gap
\[
\gamma_v\ge
 \min\{\Delta_v,\Delta_v+\gamma_*-2G_0\},
\tag{18}
\]
where \(\gamma_*\) is the smallest child gap. Clean low coordinates are majorized by the original positive reference by (16). All-clean high output has rate at most \(\sum_i\Omega_i\); an input error loses \(\gamma_*\), while low extraction and reconstruction cost at most \(2G_0\). These are the three terms in (18).

If there are \(k\ge4\) rigid L children, a single admissible contribution to the original positive intrinsic probe proves
\[
\Delta_v\ge2G_0-\varepsilon_k.
\tag{19}
\]
Choose a quarter index in those \(k\) children and the existing probe, and let their Laurent indices share total frequency one equally. Put all other children at their own intrinsic maximizing low indices with zero Laurent frequency. The positive odd trace and its interval-tail lower bound retain this actual coupled state. Its loss is exactly (2). No independent cap maxima are added. Hence for \(\gamma_*\le2G_0\), (18) gives \(\gamma_v\ge\gamma_*-\varepsilon_k\).

Orient a component toward any boundary incidence. Every vertex has at least \(b_v-1\) rigid L children. Boundary-high errors start with gap \(2G_0\); the recursive bound therefore gives a gap at least \(\eta_{\mathcal U}\) from (1). This holds for every orientation of the component. A singleton bare component instead uses the already proved whole-hub high-input/high-output gap, including its exceptional two-input support argument.

Inherited cone-loss errors must be distinguished from newly introduced high-coordinate errors. If one boundary L input already has full cone constant \(c_i-\eta\), apply the entire component bound with that reduced constant. The original pressure shifts by exactly \(-\eta\), so that inherited loss crosses the component intact. It is not debited by \(2G_0\) again. Newly created high-coordinate errors use the component's own path budget. On reaching a flagged junction their spectral loss becomes a full cone loss, which is the input needed at the next component. A finite expansion over these tags proves the global induction without accumulating an unjustified loss at each flagged separator.

There are finitely many components, all with a strictly positive margin. At a flagged root the physical coupon and trace have polynomial norm cost, so all propagated errors stay below \(F_0\). If there is no flagged hub, expose an existing ordinary leaf, transfer its closing turn by the exact typed adjunction, and orient the sole bare component toward that boundary. Its path condition covers that direction. The strict two-leaf case is the single decorated-leaf high-output estimate.

Thus for some \(\eta_{\mathrm{hi}}>0\), uniformly on the fixed main disk,
\[
 S_N^\epsilon(s)-
   \sum_{\mathbf n\text{ all low}}w_{N,\mathbf n}^\epsilon(s)
 =O\left(e^{N(F_0-\eta_{\mathrm{hi}})}\right).
\tag{20}
\]
One may choose a smaller fixed fraction of the minimum of the component path margins, singleton-hub margins, and \(2G_0\), after absorbing finite polynomial factors and uniform \(o(1)\) terms. Equation (20) is precisely the signed sum of all states with at least one high retained edge, because the clean recursion projects every retained edge to low indices. It does not project or bound fictitious binary-resolution edges inside a hub.

## 5. The actual optimizer is regular on every retained edge

The original positive wire action has a unique strict complete maximizer. Its exact statements are in `notes/actual_conway_general_core_packet_and_gap.md`, Sections 1–5: the primitive wire dimension is \(2H-3\), the complete state is strict, and the gate Hessian is negative definite on all primitive directions. The source compiler keeps all finite \(d=N-1\) offsets. These facts concern the original construction before any comparison.

For separated bare junctions, the intrinsic L/A probe geometry puts each bare incident label strictly between zero and one half; L/L edges have label \(1/4\). For a bare–bare edge in a nonsingleton component, cut the tree at that edge. The two sides have unturned product profiles \(f_A,f_B\), so its original closed boundary profile is
\[
                     f_A(1-a)+f_B(1-a).
\tag{21}
\]
Every unturned product profile satisfies \(f_A'\ge f_{hh}'\), and the inequality is strict if the product has at least three inputs or an A child. The two-leaf profile is symmetric about \(1/2\), with positive derivative below \(1/2\). Therefore (21) has strictly negative derivative for \(a>1/2\). At \(a=1/2\) it still has negative derivative if either side has at least three inputs. In the present nonsingleton class, each endpoint has at least five rigid boundary incidences, so this strict case applies. Its complete maximizing edge is consequently below \(1/2\). It is positive by strictness of the original state. The other edge types are intrinsic L/A probes or L/L quarter states, as above.

At each bare vertex the sum of its incident normalized labels is strictly greater than one. To see this without assigning an independent vertex state, resolve that original product in its original binary order. The incident degree sum minus the closing degree is the sum of the retained gate slacks \(i+j-r\). At the strict continuous state all these slacks are positive, and a bare vertex has at least three incidences. Hence the incident sum exceeds one. This is only a support identity for the original positive expansion, not a new high-edge argument across complementary-label resolution edges.

It follows that a small compact window \(\mathcal W\) about the projection of the complete optimizer to the retained edge variables satisfies, for a fixed \(\delta>0\),
\[
 \delta\le n_e/N\le1/2-\delta,\qquad
 \sum_{e\sim v}n_e/N\ge1+\delta
                 \quad(v\text{ bare}).
\tag{22}
\]
The finite \(O(1/N)\) offsets are harmless after one fixed shrinking of the window.

Expand the complete pure hub tensors in their original positive binary multiplication and leaf coordinates. This recovers the original positive wire sum with the retained edge indices fixed; only hidden variables have been summed. The original action's unique maximizer projects to one retained assignment. Thus its compact action gap off \(\mathcal W\), together with uniform factorial upper estimates and polynomial state counting, gives an absolute pure gap there. Equations (15),(16) transfer it to the moving all-low sum:
\[
\sum_{\substack{\mathbf n\text{ all low}\\\mathbf n/N\notin\mathcal W}}
 |w_{N,\mathbf n}^\epsilon(s)|
 \le e^{N(F_0-\eta_{\mathrm{out}})}
\tag{23}
\]
for a fixed \(\eta_{\mathrm{out}}>0\) and all sufficiently large levels. This is a genuine absolute bound on the contracted low-state weights. For endpoint comparisons, divide the original finite wire array by \(d\), as in Section 5 of the general core note, and then use uniform continuity of \(J\); no factorial rate is evaluated outside its support.

Combining (20),(23), with \(\eta\) smaller than both gaps,
\[
S_N^\epsilon(s)=
 \sum_{\mathbf n/N\in\mathcal W}w_{N,\mathbf n}^\epsilon(s)
 +O(e^{N(F_0-\eta)}).
\tag{24}
\]
This separates the two different facts: a grouped signed high-sector gap and an absolute all-low outside-window gap.

## 6. Actual local ratios on the regular window

At a bare vertex, write
\(\prod e_{n_a}(-u-u^{-1})=\sum_k a_k u^k\), and
\(d_\ell=a_{\ell N-1}-a_{\ell N+1}\ge0\). The exact Fourier trace is
\[
\phi_s(\prod e_{n_a})=N^2\sum_{\ell\ge1}
 (-1)^{(N-1)(\ell+1)}
 U_{\ell-1}(\cos2\pi s)d_\ell.
\tag{25}
\]
On (22) the one-factor coefficient action has
\[
 b_u''(t)=-\frac{\pi\sin2\pi u}
                  {\sin\pi(u+t)\sin\pi(u-t)}\le-\lambda_\delta<0.
\]
Its fixed-factor convolution is strongly concave. Hence the frequencies \(\ell\ge2\) have a uniform action gap relative to the first coefficient. The finite interval-tail inequality bounds the latter coefficient by a polynomial multiple of \(d_1\). Thus all higher aliases are exponentially smaller than \(d_1\), including at even levels, and
\[
V_{v,N,s}/V_{v,N,0}=1+O_R(e^{-\kappa N})
                         \quad(v\text{ bare}).
\tag{26}
\]
For at most four low factors (26) is exact without the window restriction. The detailed proof is `/private/tmp/md-low-newton-regular-window-higher-alias-gap.md`, Sections 1–4. On an opposite-color object the relation is constant, so its ratio is exact as well.

At an equal-color circle vertex, the actual root grid gives
\[
V_{v,N,s}=N q_N^{\epsilon_v(d^2/4-s^2/2)}
 \sum_{r=0}^{N-1}
 \prod_{e\sim v}e_{n_e}(-2\cos\tau_r(s))
       e^{i\epsilon_vN\tau_r(s)^2/(4\pi)},
\quad \tau_r(s)=\frac{2\pi}{N}(d/2+s-r).
\tag{27}
\]
On the regular window the product has a strict angular Gaussian at zero, with curvature \(\sum_{e\sim v}\tan(\pi n_e/N)>0\). Rectangle quadrature, retaining its endpoint currents, makes the grid shift exponentially invisible. The complete Gaussian anchor is nonzero. Actual holomorphy and the all-index majorant extend the ratio to any fixed \(R<1\) by three-circles. Consequently
\[
V_{v,N,s}/V_{v,N,0}
 =q_N^{-\epsilon_v s^2/2}[1+O_R(e^{-\kappa N})]
                       \quad(v\text{ equal circle}).
\tag{28}
\]
At an opposite-color circle vertex, its constant reference gives exactly \(\rho_{v,N}(s)\). The proofs including both parity endpoints, physical crossing scalars, and analytic wire interpolation are Sections 3–10 of `/private/tmp/md-physical-leaf-main-meridian-regular-window.md`.

Finally, on the same compact interval,
\[
\frac{H_N(s)}{W_{n_e}(s)}
 =1-\frac{\pi s^2}{N}\cot(\pi n_e/N)+O_R(N^{-2}).
\tag{29}
\]
After taking the state-independent factors into (11), the finite product of (26)–(29) gives
\[
w_{N,\mathbf n}^{\epsilon}(s)
 =\Gamma_N(s)w_{N,\mathbf n}^{\epsilon}(0)
       [1+O_R(N^{-1})],\qquad \mathbf n/N\in\mathcal W.
\tag{30}
\]
No coefficientwise approximation of a raw signed return sector is used here.

## 7. Conditioning from the actual complete packet

The complete asymptotic used here is the whole-source statement in `notes/actual_conway_all_strict_tree_long_twist_volume.md`, Section 6, equations (24)–(25). At every original auxiliary color \(N\), the complementary alias is exactly \(h_0^\epsilon=0\). Its nonzero core packet therefore is the actual scalar, with the recorded unit phase:
\[
 S_N^\epsilon(0)
 =\eta_N N^{3/2}a_\epsilon(0)e^{NF_0}
                  [1+O(N^{-1})]
   +O(N^C e^{N(F_0-\eta_0)}),\qquad a_\epsilon(0)\ne0.
\tag{31}
\]
Here \(\eta_N=\exp(i\pi(N-1)\sum_i\epsilon_i/4)\), up to the same recorded source mark on both sides. The exact association with \(S_N\) is the finite compiler (9), not a comparison of independently defined invariants. The quarter-index theorem covers equality of an original leaf label with \(1/4\). The two-leaf knot qualification is exactly the one stated in that source theorem.

For the complete pure source, the same positive Laplace calculation gives
\[
0<S_N^0(0)\le C N^{3/2}e^{NF_0}.
\tag{32}
\]
This is a positive comparison contraction with the half-twist signs set to zero; it does not identify its topology with the signed knot. Its scale can also be checked directly in the original primitive coordinates: \(H\) leaf factors have order \(N^{1/2}\), \(H-2\) strict gates have order \(N^{-3/2}\), and the primitive Gaussian has \(2H-3\) variables. The product of these powers is \(N^{3/2}\). The unique strict optimizer and its negative Hessian, not a raw crossing-path positivity assumption, give the Gaussian bound; the complement has the closed strict gap from the general core theorem, Sections 3–5.

Combine (17), (31), and (32). For all sufficiently large levels,
\[
\boxed{\displaystyle
\sum_{\mathbf n/N\in\mathcal W}
   |w_{N,\mathbf n}^{\epsilon}(0)|
 \le C\,|S_N^\epsilon(0)|.}
\tag{33}
\]
This is the needed conditioning estimate. It is proved for the actual covariant contraction after each physical circle tensor has been contracted. No bounded-total-variation assertion is made before summing the circle's internal signed paths, and no scalar nonzero asymptotic is used as a substitute for the absolute estimate (17).

Summing (30), using (33), and adding the two remainders from (24), gives
\[
S_N^\epsilon(s)
 =\Gamma_N(s)S_N^\epsilon(0)[1+O_R(N^{-1})].
\tag{34}
\]
The exponentially small remainders are negligible relative to (31). Inserting the exact cut identity (10) proves (3).

## 8. Consequences and limits of the conclusion

On every compact \(R<1\), \(H_N\) and its inverse are uniformly bounded and
\[
H_N(s)=\frac{\sin\pi s}{\pi s}+O_R(N^{-2}).
\tag{35}
\]
After dividing out the exact framing/mark ratio and the explicit \(\Gamma_N\), (3) therefore converges locally uniformly to \(\sin(\pi s)/(\pi s)\), with every fixed derivative. In the microscopic coordinate \(z=2\pi i s\), this is \(2\sinh(z/2)/z\). This conclusion is restricted to \(|s|<1\); it makes no assertion through the first ordinary resonance.

If the retained framing/mark ratio and its inverse are uniformly subexponential, as for the fixed finite Cartan and ribbon factors in the stated convention, (3),(31) also give
\[
\sup_{|s|\le R}
 \left|\frac{2\pi}{N}\log
       |\mathcal F_{N,\mathbf N}^{\epsilon}(q_N^s)|
                  -2\pi F_0\right|\longrightarrow0.
\tag{36}
\]
For sufficiently large \(N\) the normalized contraction is nonzero on this disk, since the right side of (34) stays away from zero. Under the original marked geometry the right side of (36) is the volume of the same augmented complement, with all crossing circles unfilled. It is stronger than a supremum statement at those fixed complete auxiliary colors, but is not a filled-knot theorem.

The modified dimension, if included in a full trace, stays separate: its ratio to its complete value is exactly \(1/H_N(s)\). Thus it cancels the single cut factor, not any of the recorded framing or typed phases. No ordinary-color-subtracted regular remainder for a filled knot is identified by this observation.

The proof does not cover arbitrary adjacent bare components without (1), nor does it justify inserting an \(O(N^{-1})\) grid error into a filling transform with a smaller geometric exponent. The small complex auxiliary-deficit and wire interpolants in the local report provide a possible corridor input, but a whole moving filled source requires its own global error and exact operator comparison. The direct filled-coupon approach is a separate proof obligation.

## 9. Precise proof dependencies

The finite compiler, metric, one cut factor, and typed scalar conventions are `notes/actual_main_meridian_newton_compiler.md`, Sections 3–5, and `notes/actual_main_meridian_turn_comparison.md`, Sections 1–4. The original whole-hub low/high bounds are `notes/actual_main_meridian_source_bounds.md`, Sections 1–4. The component extension, coupled pressure witness and path budget are `/private/tmp/md-adjacent-bare-components-many-rigid-boundaries.md`, Sections 1–6. The covariant high-error split for separated components is `/private/tmp/md-complete-color-covariant-localization-and-profile-bridge.md`, Sections 1–4; Section 4 above explains the additional inherited-error distinction needed across general components. The full homogeneous-cone propagation, exact positive-reference projection and complete conditioning are also proved in `/private/tmp/md-complete-color-component-conditioning-and-profile.md`, Sections 2–4 (SHA256 `71e59672059aa82cc6f7eadc99e8a73bc88b32db573e234dc60701ecba96736b`).

The unique strict optimizer, quarter lower bound, closed absolute core gap and Gaussian Hessian are `notes/actual_conway_general_core_packet_and_gap.md`, Sections 1–5. The actual signed nonzero complete packet, including its original unit phase and both level parities, is `notes/actual_conway_all_strict_tree_long_twist_volume.md`, Section 6, equations (24)–(25). The local physical-circle and bare-kernel ratios are the two private proofs named in Section 6. This assembly uses those finite-source results; it does not import a scalar volume limit as a proof of conditioning or change the original geometric action.
