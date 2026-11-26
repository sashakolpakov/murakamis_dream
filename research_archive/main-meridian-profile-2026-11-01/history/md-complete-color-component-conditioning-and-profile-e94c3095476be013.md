# Conditioning the complete-color contraction across bare components

Private proof, 1 November 2026. No repository file is changed.

This proof treats the separated-bare-junction class and its enlargement in `/private/tmp/md-adjacent-bare-components-many-rigid-boundaries.md` (SHA256 `f0283dfb80df2f21a4743772bb3a13956b090338e2b770bfb257126feb066fff`). A nonsingleton maximal bare component must satisfy the path condition there; in particular, the sufficient condition \(b_v\ge\max(8,4|\mathcal U|)\) is allowed. Singleton components retain the published arbitrary-valence theorem. All original auxiliary-circle colors are exactly \(N\).

The exact source and geometry hypotheses are those of the strict Conway theorem, with its original knot/component and two-leaf qualifications when the nonzero packet and volume are used. The conclusion is a complete-auxiliary-color augmented-source profile. It is not a filled-knot profile or a claim about every microscopic ordinary-color subtraction.

The inputs are the published source-bound and auxiliary-color-gap notes, the private component theorem, the proved regular-window higher-alias lemma, the actual physical-leaf/junction report through Section 10, and the exact covariant source identity in the geometry agent's localization report. The local physical-leaf proof used below was independently checked against its canonical Gamma product; no interpolation uniqueness is assumed.

## 1. Exact covariant source and normalization

Put \(d=N-1\), \(M_N=\lfloor d/2\rfloor\), and use the fixed complete Newton basis \(e_n\). All vertex indices are lower indices for the exact metric
\[
 J_{ab}=\phi_\sigma(e_a e_b)=\mathbf1_{a+b=d},
 \qquad \sigma=s\text{ or }0
 \tag{1}
\]
according to the physical orientation type. A bare junction has tensor
\[
 V_{v,s}(\mathbf n)=\phi_\sigma\left(\prod_{a\sim v}e_{n_a}\right).
 \tag{2}
\]
A junction containing one original character has tensor
\[
 V_{v,s}^{\epsilon}(\mathbf n)
 =\phi_\sigma\left(R_\sigma^{\epsilon}L_N
                              \prod_{a\sim v}e_{n_a}\right).
 \tag{3}
\]
An ordinary physical leaf is a univalent vertex of type (3). An originally flagged leaf is retained in its junction as the displayed character and crossing. The products in these formulas are raw products before taking their exact quotient trace.

In this convention the actual turn on an edge is
\[
 (T_\gamma J)_{ab}
 =\mathbf1_{a=b}\frac{\gamma_N(s)H_N(s)}{W_a(s)},
 \qquad
 H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)},
 \tag{4}
\]
where \(W_a\) is the paired sine product and the specified type determines \(\gamma_N\). The factor is \(H_N/W_a\), rather than \(W_a/H_N\), because the lower coefficient vector is raised before applying the turn. All six physical types and their fixed reference scalars are retained.

Write the exact resulting finite contraction as \(Z_N^\epsilon(s)\). A separate scalar \(\zeta_N(s)\) records the original ribbon framing and the closing mark. The reduced primitive main cut has the exact form
\[
 \mathcal F_{N,\mathbf N}^{\epsilon}(q^s)
 =\zeta_N(s)H_N(s)Z_N^\epsilon(s),
 \qquad H_N(0)=1.
 \tag{5}
\]
The scalar \(\zeta_N\) must not be replaced by one. It is nonzero and holomorphic on the fixed microscopic disk, with the recorded elementary bounds; its ratio will remain explicit. In particular the argument below does not silently select a new framing.

The finite source identity follows from the fixed Frobenius metric, the actual typed turn, and the ordered product tensors. It is not a tangle isotopy or a physical insertion of a comparison circle.

## 2. Grouped errors through an entire bare component

A boundary L module of original absolute constant \(c\) has pressure \(\Omega_L=c+2G_0\). The needed coefficient cone is
\[
 |[e_r]L_N|\le e^{N(c+o(1))}
 \begin{cases}
 e^{Ng(r/N)},&r\le M_N,\\
 1,&r>M_N.
 \end{cases}
 \tag{6}
\]
Every inequality is uniform on a fixed \(|s|\le R<1\). Constants may depend on the fixed tree and radius. Polynomial factors are included in the uniform \(o(1)\).

The bare-component theorem is multilinear in its boundary modules and holds for arbitrary arrays in (6), not just physical arrays. Its original action is affine in the constants:
\[
 \Omega_{\mathcal U}(c_1,\ldots,c_b)
 =\Omega_{\mathcal U}(0,\ldots,0)+\sum_{i=1}^b c_i.
 \tag{7}
\]
This follows either from its positive reference polynomial or directly by adding the constants to the constrained source action. Thus, if one boundary input satisfies the entire cone with \(c_i-\eta\), the output spectral rate loses \(\eta\). This is a consequence of the already proved component estimate with shifted constants, not a new independent-cap estimate.

Here is a recursive decomposition that distinguishes this cone loss from a spectral loss. At an outgoing L module write
\[
 L_v=L_v^{\mathrm{clean}}+I_v+H_v.
 \tag{8}
\]
The clean part keeps every edge index in the subtree, including its outgoing index, low. The internal error \(I_v\) has the full coefficient cone with constant \(c_v-\eta_v\), for some fixed positive \(\eta_v\). The boundary-high part \(H_v\) is supported on high outgoing indices and has coefficient rate at most \(c_v\), hence full spectral rate at most
\(c_v=\Omega_v-2G_0\). An ordinary leaf starts this decomposition by its exact low and high projections, with \(I_v=0\).

At a flagged junction, expand the input product in clean parts and errors. Quotient multiplication has polynomial spectral cost. Any term with a child error therefore loses that child's established positive spectral gap. The physical decorated-character extractor maps this spectral loss into the *whole* coefficient cone with its scalar constant decreased by the same gap. These terms form \(I_v\). Apply the same extractor to the all-clean product and split its output: the low part is \(L_v^{\mathrm{clean}}\), and the high part is \(H_v\). This proves (8), retaining all actual signs. In particular a spectral error is not merely declared to be a coefficient error: the proved extractor is the required map between the two estimates.

Now consider a maximal bare component. Expand its boundary modules using (8). A term containing at least one internal error \(I_i\) is controlled by (6)–(7) at a strictly reduced output action. For the remaining terms, use boundary inputs \(L_i^{\mathrm{clean}}+H_i\). Their low parts have the original positive reference majorant, and their high parts have the initial spectral saving \(2G_0\). The component path condition then gives
\[
 Q_{\mathcal U}=Q_{\mathcal U}^{\mathrm{clean}}+E_{\mathcal U},
 \qquad
 \|E_{\mathcal U}\|_{\mathrm J}
 \le e^{N(\Omega_{\mathcal U}-\eta_{\mathcal U}+o(1))},
 \quad\eta_{\mathcal U}>0.
 \tag{9}
\]
Here the clean term keeps all internal component labels, all boundary labels inherited from its clean inputs, and its outgoing label low. For a nonsingleton component one can choose its newly generated gap below
\[
 2G_0-\max_{\mathcal P\subset\mathcal U}
              \sum_{v\in\mathcal P}\varepsilon_{b_v-1}>0;
 \tag{10}
\]
for a singleton the published whole-hub gap applies. Already present internal input deficits are also included in the finite positive minimum defining \(\eta_{\mathcal U}\).

After (9) enters a flagged junction, its gap is converted into a cone deficit in (8). Consequently the next bare component uses (7) and preserves this deficit. It does not charge another \(2G_0\) merely because the error has crossed a separator. This is the reason separate component path budgets suffice; one does not need the sum of all path losses over the entire reduced tree to be below \(2G_0\).

At a flagged closing root the unturned coupon and trace have polynomial spectral cost. Every propagated error is therefore below the original \(F_0\). If no flagged junction exists, expose an existing ordinary leaf and transfer its closing turn by the exact fixed-metric adjunction; the entire remaining bare component is evaluated toward that boundary incidence. Its intrinsic action is the original \(F_0\), and (9) applies because the path condition is independent of the root direction. The strict two-leaf case is the original separate case.

We have proved, for some \(\eta>0\),
\[
 Z_N^\epsilon(s)=Z_{N,\mathrm{all\ low}}^\epsilon(s)
                  +O(e^{N(F_0-\eta)}).
 \tag{11}
\]
This estimates the *summed* contribution of states with a high edge. It does not estimate the absolute value of each return-sector expansion before cancellation. The proof deliberately groups those terms into the controlled module errors.

## 3. The exact pure reference and off-window localization

At completeness, for every low-index product \(E=\prod e_{n_a}\),
\[
 \phi_0(R_0^\epsilon L_NE)
  =N\sum_{r=0}^{N-1}R_0^\epsilon(c_r)E(c_r),
 \qquad E(c_r)\ge0,
 \quad |R_0^\epsilon(c_r)|=1.
 \tag{12}
\]
The full crossing scalar is included. Thus
\[
 \left|\phi_0(R_0^\epsilon L_NE)\right|
                \le\phi_0(L_NE)
 \tag{13}
\]
is an exact same-level inequality. A high basis factor vanishes at every complete node, so the high outgoing coefficients of \(T_0(R_0^\epsilon L_NE)\) are exactly zero at complete auxiliary color. The deformed high terms were nevertheless retained in Section 2.

Bare complete tensors are nonnegative: the complete Newton multiplication coefficients are nonnegative on their original support and vanish on the forbidden product range. Edge weights at \(s=0\) are one. Hence the all-pure covariant contraction is the original nonnegative complete source. Expanding its vertex tensors using the original ordered binary resolution is an exact positive expansion, with all original leaf labels and normal terms retained. Lowering indices merely turns an original wire label into that label or its complement; the normalized complete carriers are the identity. Summing hidden binary-resolution indices therefore gives the covariant pure weights without introducing negative coefficients.

The retained edge assignment is a continuous affine projection of these original complete wire variables. The original positive source action has a unique strict maximizing state. Consequently its projection is the unique maximizing retained assignment: if a compact closed set of retained assignments misses that projection, every original state above it misses the original maximizer. Compactness gives a fixed strict action loss. Uniform factorial bounds and the fixed polynomial number of states turn this into a finite-sum bound. This is localization in the original constrained source; it does not use separately optimized cap sums.

The maximizing retained assignment is regular and low. For a bare–bare edge with covariant label \(a\), cutting the edge gives two unturned product profiles and the closed boundary action
\[
                   f_A(1-a)+f_B(1-a).
 \tag{14}
\]
For \(a>1/2\), the original derivative inequality \(f_A',f_B'\ge f_{hh}'\) makes (14) strictly decreasing. At \(a=1/2\), at least one inequality is strict whenever one side has at least three product inputs or an A child. Every bare–bare edge in the new class has that strictness because the boundary-count condition gives at least five rigid boundary branches at each incident bare vertex. Thus its maximizing label is strictly below one half. It is positive by the original strict state. The other edges are the original strict intrinsic L/A probes, whose indices lie inside \((0,1/2)\), or rigid L/L pairs with index \(1/4\).

At a bare vertex, sum the strict input-minus-output inequalities in its original binary resolution. The internal outputs cancel and give
\[
                   \sum_{e\sim v} a_e-1>0.
 \tag{15}
\]
This proves the total-index hypothesis needed by the regular higher-alias lemma at every bare vertex, including vertices inside a nonsingleton component.

Choose a fixed neighborhood \(\mathcal W\) of the complete retained assignment so small that every edge there has
\(\delta\le n_e/N\le1/2-\delta\) and every bare incident total is at least \(1+\delta\), for a fixed \(\delta>0\). The finite \(d=N-1\) shifts are absorbed by a further fixed shrink. At all low states, the proved same-level bounds give
\[
 |V_{v,s}^\epsilon(\mathbf n)|
       \le N^{C_v}V_{v,0}^{0}(\mathbf n),
 \tag{16}
\]
for both bare and circle vertices. The circle estimate holds for every \(|s|\le R<1\) by the actual shifted-grid proof; the bare estimate is the all-parity low-array comparison. All edge factors are uniformly bounded. The original pure off-window gap therefore implies
\[
 Z_N^\epsilon(s)=
   \sum_{\mathbf n/N\in\mathcal W}w_{N,\mathbf n}^\epsilon(s)
           +O(e^{N(F_0-\eta')})
 \tag{17}
\]
for a smaller \(\eta'>0\), uniformly on the fixed microscopic disk. Section 2 controls the grouped high states separately.

## 4. Uniform conditioning at completeness

Equation (13) is stronger than a heuristic comparison of stationary phases. State by state on the complete all-low contraction,
\[
 |w_{N,\mathbf n}^\epsilon(0)|
                        \le w_{N,\mathbf n}^{0}(0).
\]
Every pure weight is nonnegative, even in the full positive expansion. Therefore
\[
 \sum_{\mathbf n/N\in\mathcal W}|w_{N,\mathbf n}^\epsilon(0)|
 \le Z_{N,\mathrm{all\ low}}^{0}(0)
 \le Z_N^{0}(0).
 \tag{18}
\]
The original positive complete-source Laplace theorem gives
\[
 Z_N^{0}(0)=N^{3/2}e^{NF_0}(a_0+O(N^{-1})),\qquad a_0>0.
 \tag{19}
\]
This is the positive comparison source with half-twist signs set to zero; it is not an assertion that its topology is the signed knot's topology. The same original action and primitive wire count govern it. The actual signed complete core theorem, with the exact complete-color identity and its nonzero amplitude, gives
\[
 |Z_N^{\epsilon}(0)|
     =N^{3/2}e^{NF_0}(|a_\epsilon|+O(N^{-1})),
 \qquad a_\epsilon\ne0.
 \tag{20}
\]
The specified unit phase has modulus one. Both statements hold at both parities, under the original strict and two-leaf qualifications. Combining (18)–(20) proves
\[
 \sum_{\mathbf n/N\in\mathcal W}|w_{N,\mathbf n}^\epsilon(0)|
                 \le C\,|Z_N^\epsilon(0)|
 \tag{21}
\]
with a fixed \(C\). This is the required bounded conditioning of the retained finite contraction. It says nothing about the absolute mass of the original uncontracted crossing-path sum or an unpaired Fourier-current representation.

## 5. Local comparison and the resulting augmented profile

On \(\mathcal W\), the regular-window bare tensor ratio is \(1+O(e^{-cN})\), at both parities. The physical circle-junction ratio is its exact type scalar times \(q^{-\epsilon s^2/2}(1+O(e^{-cN}))\) in the equal-color frame, and the specified scalar counterpart in the opposite-color frame. These statements use the actual full crossing and the concrete shifted-grid/Gamma interpolant; their complete denominators are nonzero on the window by the local Gaussian anchor. Every retained scalar is \(1+O(N^{-1})\). Also
\[
 \gamma_N(s)H_N(s)/W_{n_e}(s)=1+O(N^{-1})
\]
uniformly on the regular edge interval. Since the tree is fixed, the exact local identities imply
\[
 w_{N,\mathbf n}^\epsilon(s)
 =w_{N,\mathbf n}^\epsilon(0)(1+O_R(N^{-1}))
 \quad(\mathbf n/N\in\mathcal W).
 \tag{22}
\]
The error constant is uniform in the state. Now use (17) and (21), rather than summing relative errors without conditioning. It follows that
\[
 \frac{Z_N^\epsilon(s)}{Z_N^\epsilon(0)}=1+O_R(N^{-1}),
 \qquad |s|\le R<1.
 \tag{23}
\]
Finally the exact cut normalization (5) gives
\[
 \boxed{\displaystyle
 \frac{\mathcal F_{N,\mathbf N}^{\epsilon}(q^s)}
      {\mathcal F_{N,\mathbf N}^{\epsilon}(1)}
 =\frac{\zeta_N(s)}{\zeta_N(0)}H_N(s)
                  (1+O_R(N^{-1})).}
 \tag{24}
\]
After dividing out the explicit framing ratio and the nonzero \(H_N\), the errors are holomorphic on every fixed disk strictly inside the first resonance. Cauchy's estimate on a larger such disk gives the same \(O(N^{-1})\) conclusion for every fixed derivative on smaller disks. Since \(H_N(s)\to\sin(\pi s)/(\pi s)\), (24) identifies the unframed leading augmented profile in these coordinates.

This theorem combines a local ratio with a proved grouped error estimate and a bounded conditioned finite contraction. It does not derive normality merely from a nonzero saddle or a source upper bound. It also does not identify the canonical ordinary-color subtraction for every augmented multi-component source, nor does it replace the moving full-twist filling functional by its complete-meridian counterpart. A filled-knot profile requires those additional exact interfaces and the corresponding exponentially accurate parameter-dependent source comparison.
