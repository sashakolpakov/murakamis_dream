# The geometric contribution and all Fourier charges

For a fixed link diagram, the exact finite formula is a coefficient in face variables followed by a linear functional in each crossing variable. Its local polynomial splits into three specified pieces. The central piece, called CROSS in the source formulas, contains paths passing through the middle of the finite recurrence. The other two pieces contain paths restricted to one side. Selecting CROSS at every crossing region gives a contribution to the original invariant; it does not define another topological invariant.

This note proves a nonzero asymptotic for that entire geometric contribution, including all Fourier charges, both level parities, the derivatives at repeated spectral nodes, and the original scalar factors. The diagram may have cups and caps between crossing regions: it need not be a flat plat. Its white triangulation must be a simple sphere with the specified matching and marked strand edge. The local balance inequalities used to bound the other two pieces are not needed here.

The [geometric companion](actual_morse_geometric_contribution.md) constructs the actual complement and identifies the selected action with its hyperbolic volume after sufficiently long fixed signed fillings. A strict estimate for the full contribution minus this geometric term remains a separate requirement for a full-invariant volume theorem.

## 1. Exact assumptions and statement

Fix a finite connected Morse diagram whose actual white triangulation is a simple sphere, with its actual matching, cyclic orders, crossing-disk frames and marked MAIN edge. Let the marked edge join the two protected white faces \(u,v\). The diagram has \(R\) matching edges, \(R+2\) white faces, and \(R\) ordinary face targets. Assume the labeled positive convex right-angled certificate and its marked complete packing are supplied. Set the protected curvatures to zero and retain the same positive finite curvatures \(\rho_f\) at every occurrence of each other face. The geometric existence of this certificate is a separate input to the present analytic argument.

The exact general Morse source identity is the one in [A matched spherical triangulation has the original general Morse source](research_matched_sphere_morse_source.md), §§5–6, equivalently the finite-source part of [Balanced terminal decorations and volume limits beyond tangle-operation trees](actual_balanced_terminal_fan_volume.md), §5. In particular all physical cups, caps, the unrestricted marked row, the integrated even-level coset and the original component/framing factors are retained. With \(N\ge3\), \(d=N-1\), \(q=e^{\pi i/N}\), define
\[
 \begin{split}
 C_N(\boldsymbol\delta)
 &=\left[\prod_{f\ne u,v}L_f^d\right]
       \left.\prod_{e=1}^{R}
       H_{V_N,\mathrm C}(L_{x_e},L_{b_e},L_{c_e},L_{y_e};\sigma_e)
       \right|_{L_u=L_v=0},\\
 \sigma_e&=-2\cos(2\pi\delta_e).
 \end{split}
 \tag{1}
\]
Here CROSS means the literal central-cut path support. It is selected by polynomial linearity after the full physical source has been identified; it is not declared an independent covariant coupon. Write \(P_{\mathrm C}=(-1)^dH_{V_N,\mathrm C}\) for the positive endpoint convention. Thus (1) is the raw coefficient and contains \((-1)^{dR}\).

For fixed nonzero signed crossing powers \(n_e=\epsilon_e-2p_e\), its exact all-CROSS period is
\[
 \begin{split}
 I_{N,\mathbf n}^{\mathrm C}
 ={}&q^{d^2\sum_e n_e/4}(-i)^R
 \sum_{\boldsymbol\ell\in(\mathbb Z\setminus\{0\})^R}
       \left(\prod_e\ell_e\right)
             (-1)^{(N+1)\sum_e\ell_e}\\
 &\quad\times\int_{[-1/2,1/2]^R}
       C_N(\boldsymbol\delta)\prod_e\sin(2\pi\delta_e)
       \exp\left\{N\sum_e
         (\pi i n_e\delta_e^2+2\pi i\ell_e\delta_e)\right\}
                  d\boldsymbol\delta .
 \end{split}
 \tag{2}
\]
No additional power of \(N\), modified dimension, or spectral square-root Jacobian appears. The displayed \(q\) power is the original unwrapped scalar \(\exp(\pi i d^2\sum n_e/(4N))\). An exterior framing/component character multiplies the raw contraction when converting to the specified invariant convention; it has modulus one at complete color. The full one-cut modified convention additionally retains its stated \(i^{N+3}/N\). These conventions are not changed by a CROSS projection.

There is a fixed small complex polydisk and finite holomorphic actions \(A_N\), face Hessians \(H_N\), such that the following two source estimates hold:
\[
 C_N(\delta)=
 \frac{(-1)^{dR}N^{2R}e^{NA_N(\delta)}}
 {(2\pi N)^{(R-1)/2}\sqrt{\det H_N(\delta)}}
                     (1+O(N^{-1})),
 \tag{H1}
\]
uniformly and holomorphically on that polydisk, and, for every \(\eta>0\),
\[
 |C_N(\delta)|\le e^{N(\Phi-\gamma_\eta)}
 \quad\text{if }\max_e|\operatorname{Re}\delta_e|\ge\eta,
 \quad\operatorname{Re}\delta_e\in[-1/2,1/2],
 \quad|\operatorname{Im}\delta_e|\le\tau_\eta,
 \tag{H2}
\]
for some \(\gamma_\eta,\tau_\eta>0\) and all sufficiently large \(N\). All fixed derivatives satisfy the corresponding bound on smaller domains. Here
\[
 A_N\longrightarrow A_0,\qquad A_0(0)=\Phi,\qquad
 A_0''(0)=-2\operatorname{diag}(C_e),\quad C_e>0,
 \tag{3}
\]
with every fixed derivative; \(A_N\) is separately even and real on the real chart. The marked complete action satisfies \(2\pi\Phi=\operatorname{Vol}(Y_D)\) under the supplied geometric certificate and its calibrated source action.

There is a diagram-dependent \(n_0\) such that, for every fixed independently signed vector with \(|n_e|\ge n_0\), the entire period (2) has the relative asymptotic
\[
 \begin{split}
 I_{N,\mathbf n}^{\mathrm C}
 ={}&q^{d^2\sum_e n_e/4}(-2i)^R\sqrt{2\pi}\,N^{R+1/2}\\
 &\times
 \frac{\prod_e\sin(2\pi\delta_{N,\mathbf1,e})}
 {\sqrt{\det H_N(\boldsymbol\delta_{N,\mathbf1})}
       \sqrt{\det Q_{N,\mathbf1}}}
 e^{NS_{N,\mathbf1}}
 \left(1+O_{\mathbf n}(N^{-1})
              +O_{\mathbf n}(e^{-\kappa_{\mathbf n}N})\right).
 \end{split}
 \tag{4}
\]
The quantities in (4) are the finite critical point, critical value and negative Hessian of
\[
 \Phi_{N,\boldsymbol\ell}(\delta)
   =A_N(\delta)+\pi i\sum_e n_e\delta_e^2
                         +2\pi i\sum_e\ell_e\delta_e.
 \tag{5}
\]
The face determinant root is continued from the positive complete Hessian. The spectral root is the Gaussian branch on matrices with positive real part. The coefficient in (4) tends to a nonzero number after the explicit level factors and action are removed. In particular the period is nonzero for all sufficiently large levels of either parity, and
\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log|I_{N,\mathbf n}^{\mathrm C}|
                  =2\pi\operatorname{Re}S_{0,\mathbf1}.
 \tag{6}
\]
All powers are fixed before \(N\to\infty\); no bound on their ratios is required. There is no assertion here that the full invariant differs from (2) by a smaller term.

## 2. The graph facts replacing a flat-plat assumption

Deleting \(u,v\) from a simple triangulated sphere leaves a connected ordinary graph. Indeed reroute a path around the first deleted vertex along its cyclic link, then around the second along its link with the first vertex removed. That remaining link is connected. Every surviving edge belongs to an original shaded triangle with two positive finite-face variables.

No matching edge can have the protected pair as its endpoints: their unique sphere edge is the marked MAIN edge. Consequently every crossing circle has \(x+y>0\). At least one of its two triangles is nonmonomial. If both outers are positive, \(xy>0\); if one outer is protected, at most one middle can be the other protected face, so the other middle is positive. These facts also cover the smallest simple sphere. They require neither complete-radius balance nor a tree in the ordinary graph.

At the actual complete packing, the circle-center angle sums make the common face action stationary. Its Hessian is positive on the common-scale quotient: each nonmonomial triangle detects the differences of its finite logarithmic face radii, and the connected ordinary graph leaves only common scaling in the kernel. The active rows are literal \(+1,-1\) differences. Thus the quotient lattice is primitive, has dimension \(R-1\), and has no additional angular aliases.

This is the content needed from [The positive face coefficient has one global saddle](actual_positive_face_coefficient_saddle.md), §§2–4, and [The original boundary source has exactly two flat face directions](actual_original_boundary_transverse_rank.md), §2. Their proofs use the actual triangle graph and finite determinant matrices. Morse bends introduce no new face coordinate, while the exact source identity has already dealt with their cup/cap and mark factors. The old global theorem's phrase “flat plat” is therefore removed at this specific interface, rather than by an unproved equivalence of presentations.

## 3. Local analytic inputs, including the odd normal

At each original crossing region let \(\mathcal B_{e,N}(\delta_e;L)\) be the exactly anchored even fold interpolation. It retains the actual maximal-channel factor, beta factors, forced products and half-index. In particular its anchor is at \(\delta_{\min}=0\) for odd levels and \(\delta_{\min}=1/(2N)\) for even levels. The local rigidity theorem gives
\[
 P_{\mathrm C,e}(\delta_e;L)
       =N^2\mathcal B_{e,N}(\delta_e;L)
                          (1+O(e^{-cN}))
 \tag{7}
\]
on a fixed complex spectral and face neighborhood, with protected variables still exactly zero. This is [Actual all-CROSS cofactors and the complete-fold interpolant](actual_cross_cofactor_interpolant_rigidity.md), §§1–4, based on [An exponentially accurate analytic interpolation of the actual fold factors](actual_positive_face_exponential_fold_interpolation.md) and the independent complex packets of the actual cofactors.

For precision, the odd central formula has the form
\[
 P_{\mathrm C}=G_bG_c+\omega s_ms_{m+1}xyD_bD_c,
                    \qquad\omega=-4\sin^2(\pi\delta).
 \tag{8}
\]
The second term in (8), including its derivative at \(\omega=0\), is retained. The even formula is its original sum of three central-cut products. Their central factors are analytic units near completeness. The proof of (7) uses the independently bounded complex cofactor ratios and a finite Cauchy–Lagrange formula on both parity grids; it does not differentiate a value-only interpolation. Thus all repeated-node normals and the odd simple node are already in (7). There is no odd regularized surrogate in (1).

The local global-angular theorem applies to each terminal cofactor with row \(N/2+O(1)\). Two positive faces with separated circular phases give a fixed exponential loss, uniformly over the entire real spectral interval and a sufficiently thin complex strip. Its proof retains the exact original node adapter, positive nodal tails, all start rows and the polynomial cost of the finitely omitted terminal nodes. One-variable triangles are exact monomials and impose no angular condition. This local theorem has no global topology or Morse-order hypothesis.

Every summand of the even or odd central formula contains a cofactor from both original triangles. Outside the common ordinary-face phase, a bounded-length path in the connected ordinary graph has a separated edge; one triangle at that edge supplies the exponential loss in every central summand at its crossing region. Every other cofactor has its polynomial endpoint majorant and the fixed strip growth \(e^{O(N|\operatorname{Im}\delta|)}\). There are finitely many crossing regions, so shrink the common strip to absorb the sum of those growth costs. This proves the shared angular complement bound, on the original common radii and with every central prefactor retained.

## 4. H1 from the actual face torus

Fix one ordinary face as the scale reference, and write \(L_f=\rho_f e^{z_f}\) for the others. Define the finite phase
\[
 \Psi_N(z,\delta)=\frac1N\sum_e\operatorname{Log}
     \mathcal B_{e,N}(\delta_e;L(z))
       -\frac dN\sum_{f\ne u,v}\operatorname{Log}L_f(z).
 \tag{9}
\]
Every finite anchor and any \(O(\log N)/N\) term remains in (9); only the explicit \(N^{2R}\) in (7) lies outside. The local theorems give uniform convergence with derivatives to
\[
 \Psi(z,\delta)=\sum_e
       \bigl[Q_{b_e}(\delta_e;L)+Q_{c_e}(\delta_e;L)\bigr]
                         -\sum_{f\ne u,v}\operatorname{Log}L_f.
 \tag{10}
\]
The logarithms are real on the positive complete chart. The positive face Hessian and the holomorphic implicit function theorem give the actual nearby finite saddle \(z_N(\delta)\), uniformly on one fixed polydisk. Put
\(A_N=\Psi_N(z_N,\delta)\) and
\(H_N=\partial_z^2\Psi_N(z_N,\delta)\).

The exact homogeneous numerator degree is \(dR\), equal to the total ordinary target. Hence the common angular variable integrates to one, and the actual Cauchy measure on the quotient is \((2\pi)^{-(R-1)}d\theta\). The integration lattice is primitive by the general Morse face-potential identity; no additional multiplicity is chosen here.

Use (7) near the saddle and the preceding angular gap on its complement. Translating the original Cauchy torus by the small vector \(z_N(\delta)\) crosses no pole: all finite faces remain in their annuli, the numerator is polynomial and the target is its original Laurent monomial. If the translation is localized, its side faces are retained in the fixed angular gap. Uniform positive real Hessian and bounded higher derivatives then give the Gaussian with coefficient one and the determinant in (H1). Shrinking the spectral polydisk makes the absolute cost of its complex perturbation smaller than the exponential precision in (7), so the relative error remains \(O(N^{-1})\), holomorphic with fixed derivative bounds.

Uniqueness of this finite face saddle preserves separate evenness and reality. At zero, the mixed \(z,\delta\) derivatives vanish by evenness, so eliminating \(z\) does not change the diagonal spectral second derivative. Explicitly
\[
 C_e=\frac{\pi(T_{b_e}+T_{c_e})}{x_e+y_e}>0,
 \qquad T_t=\sqrt{(x_e+y_e)t+x_ey_e},
 \tag{11}
\]
at the actual complete packing. Section 2 ensures that at least one summand is positive. Thus (3) holds, and on a smaller fixed complex chart \(\operatorname{Re}A_N''\) is uniformly negative definite. This proves H1 directly for CROSS. The full-numerator restoration in §4 of [The original full spectral numerator has the marked geometric packet](general_full_spectral_numerator_geometric_packet.md) is not used.

## 5. H2 on the entire spectral cube

The needed real-spectral estimate is a value bound, not coefficientwise domination at arbitrary spectral parameters. The exact cleared cofactor has the original start decomposition
\[
 R_j(b,\delta)=\sum_{i=0}^{j}b^i
     \prod_{r<i}\alpha_r(\delta)K_{i,j},\qquad
 \alpha_r=4\cos^2\frac{(r+1/2)\pi}{N}-4\sin^2(\pi\delta).
 \tag{12}
\]
The normalized two-step tail transfer has limiting spectral radius
\[
 \rho(t,\delta)=(x+y)\sin(\pi t)
     +\sqrt{4xy\cos^2(\pi\delta)+(x-y)^2\sin^2(\pi t)},
 \qquad\Lambda=2\sin(\pi t)\rho.
 \tag{13}
\]
The proof in [Global real-spectral gap of the actual all-CROSS source](actual_global_cross_spectral_gap.md), §§1–2, handles the possible repeated transfer root by its Cayley–Hamilton power formula. It uses fixed finite blocks away from \(t=0\), a uniform \(O(\eta\log(1/\eta))\) endpoint allowance, and uniformly integrable truncated logarithms for the exact prefix. It therefore gives a uniform upper bound for every starting row, including in small fixed complex face neighborhoods and a thin spectral strip. No ill-conditioned eigenbasis or lower bound on distance to a physical node is assumed.

The exact maximization of the resulting start action is
\[
 \limsup\frac1N\log|R_j(b,\delta)|
       \le\max\{Q_b(\delta),\tfrac12\log b\};
 \tag{14}
\]
for \(b=0\), only the first branch is present. This comes from its unique pre-sign-change maximum and the final start endpoint; the entire prefix integral is zero. For a nonmonomial triangle,
\(Q_b(0)>\tfrac12\log b\) when that branch is present, and
\(Q_b(\delta)<Q_b(0)\) for \(0<|\delta|\le1/2\).
The derivative formula is strictly negative whenever \(b>0\) or \(xy>0\). The sole exception is the exact one-variable monomial, already excluded from any asserted local gap.

Every crossing region has at least one nonmonomial triangle. Thus a separated \(\delta_e\) supplies a strict loss relative to that crossing region's complete rate; all other crossing regions have their complete upper rates with arbitrarily small prescribed errors. On the small common-face-phase region this estimate and its complex face extension control the original integrand. On the complementary face torus use the angular gap of §3, which is uniform for all real spectral parameters. Combining the two regions on the same original radii proves H2. To make endpoint neighborhoods precise, first use separation \(\eta/2\), then shrink the strip. Cauchy's estimate gives the fixed derivative version. Neither the inequality comparing LEFT/RIGHT rates with complete radii nor a choice of different radii at separate crossing regions occurs in this proof.

## 6. The first packet, its phase, and charge comparison

Write, by evenness,
\[
 \partial_e A_N(\delta)=-2\delta_e B_{e,N}(\delta_1^2,\ldots,\delta_R^2),
 \qquad B_{e,N}\longrightarrow B_e,\quad B_e(0)=C_e.
 \tag{15}
\]
Shrink the chart until \(|B_{e,N}-C_e|\le C_e/8\). Choose first a fixed outer real cube \(K_B=[-B,B]^R\) inside that chart. Choose the scaled charge cutoff \(a>0\) sufficiently small relative to \(B\). Finally choose a separate inner radius \(0<b<a/4\), to be used only for the bounded bad charges in §7. All three constants are fixed from the source before the powers are chosen. For positive real charges with \(\ell_e/|n_e|\le a\), the critical equation is exactly
\[
 \delta_e=-\frac{\ell_e/n_e}
                  {1+i B_{e,N}(\delta^2)/(\pi n_e)}.
 \tag{16}
\]
Uniform contraction on a small polydisk gives its unique solution for all independent signed \(|n_e|\ge n_0\). In particular
\[
 |\delta_e|\le2\ell_e/|n_e|,\qquad
 \operatorname{Im}\delta_e=
 \frac{\ell_e}{\pi n_e^2}
 \frac{\operatorname{Re}B_{e,N}}
 {|1+iB_{e,N}/(\pi n_e)|^2}>0.
 \tag{17}
\]
The imaginary part is positive for either sign of \(n_e\); all coordinates and all sine factors are nonzero.

Translate the outer cube \(K_B\) to the horizontal plane through this critical point. Reality on the real chart gives
\(\operatorname{Re}A_N(x+iv)\le A_N(0)-c|x|^2+C|v|^2\), with no linear imaginary cost. On each actual side face, one \(|x_j|=B\), while \(0\le v_e\le\operatorname{Im}\delta_e\). The quadratic chirps cost at most \(CB\sum_e\ell_e/|n_e|\), and the charge terms have nonpositive real part. The critical real value is at least \(A_N(0)-C\sum_e(\ell_e/|n_e|)^2\). The already chosen \(a\ll B\), followed by sufficiently large \(n_0\), therefore puts every side strictly below that value. Thus the original local contour on \(K_B\) has saddle coefficient \(+1\), with its side currents explicitly smaller. The inner radius \(b\) is not used for this local saddle contour.

On the translated horizontal plane the real Hessian is \(\operatorname{Re}A_N''<0\). Hence the negative spectral Hessian \(Q_{N,\ell}\) has positive real part. The Gaussian determinant branch is fixed even for mixed signs. Applying the spectral Gaussian to H1 contributes \((2\pi/N)^{R/2}\), and the two measures combine exactly as
\[
 N^{2R}(2\pi N)^{-(R-1)/2}(2\pi/N)^{R/2}
                     =\sqrt{2\pi}\,N^{R+1/2}.
 \tag{18}
\]
The holomorphic relative H1 error remains \(O(N^{-1})\); the ordinary cubic Gaussian term integrates to zero, while its square and the quartic term have this same order. Constants may depend on the fixed charges and powers. The limiting prefactor is nonzero by (17) and the determinant units.

Differentiation of the critical value, rather than comparison of independent saddle remainders, gives
\[
 \partial_{\ell_e}\operatorname{Re}S_{N,\ell}
 =-\frac{2\ell_e}{n_e^2}
   \frac{\operatorname{Re}B_{e,N}}
        {|1+iB_{e,N}/(\pi n_e)|^2}.
 \tag{19}
\]
Therefore, throughout the positive local charge box,
\[
 \operatorname{Re}S_{N,\mathbf1}-\operatorname{Re}S_{N,\ell}
       \ge\sum_e\frac{C_e}{2n_e^2}(\ell_e^2-1).
 \tag{20}
\]
This comparison is valid for arbitrarily unbalanced fixed powers. Separate evenness makes every sign choice of the same positive charge magnitudes contribute equally: reflecting a coordinate reverses both its sine integral and its charge factor. For the unit charges the raw sign cancels the parity character,
\((-1)^{dR}(-1)^{(N+1)R}=1\), leaving the exact factor \((-2i)^R\) in (4).

## 7. Whole-domain currents and every other charge

For any entire polynomial in the \(\sigma_e\), multiply it by the original sines and quadratic chirps. In each variable the resulting \(B\) has zero endpoint values and equal first derivatives at \(\pm1/2\). This remains true after spectator derivatives. Three integrations by parts give exactly
\[
 \int_{-1/2}^{1/2}B(t)e^{2\pi iN\ell t}\,dt
 =(2\pi iN\ell)^{-3}
 \left\{[B''(t)e^{2\pi iN\ell t}]_{-1/2}^{1/2}
       -\int_{-1/2}^{1/2}B'''(t)e^{2\pi iN\ell t}\,dt\right\}.
 \tag{21}
\]
The second-derivative current is retained. With the original charge weight this yields summable \(|\ell|^{-2}\) at fixed \(N,\mathbf n\). Nothing about this step assumes a plat.

H1 and H2 first imply the shared real supremum \(e^{N(\Phi+o(1))}\). Since the degree in each cosine variable is at most \(d\), the elementary polynomial exterior bound gives
\[
 |C_N(\delta)|\le
       e^{N(\Phi+o(1))+2\pi d\sum_e|\operatorname{Im}\delta_e|}.
 \tag{22}
\]
This is a bound for the whole shared coefficient. Source derivatives are estimated by Cauchy, while spectator chirps are differentiated on their real intervals, so no exponentially large spectator-slope cost is inserted.

For a positive far charge in coordinate \(i\), shift its whole interval upward by a fixed small height \(\tau\). Both endpoint sides are kept together. Their exact difference, with spectator factors suppressed, is
\[
 \begin{split}
 B_i(1/2+iv)-B_i(-1/2+iv)
 ={}&2i\sinh(2\pi v)\sinh(\pi n_iNv)\\
 &\times e^{\pi i n_iN(1/4-v^2)}
           C_N(1/2+iv,\delta_{\mathrm{other}}).
 \end{split}
 \tag{23}
\]
The endpoint Fourier phase combined with the original parity is \((-1)^{\ell_i}\), of modulus one. H2 gives a fixed gap at these separated endpoints. Applying (21) in all spectator coordinates bounds the weighted vertical term by
\[
 C_{\mathbf n}|n_i|N\ell_i\,
    e^{N(\Phi-\gamma_e)}\prod_{j\ne i}|\ell_j|^{-2}
       \int_0^\tau v^2e^{-2\pi N(\ell_i-|n_i|/2)v}\,dv.
 \tag{24}
\]
For \(\ell_i>|n_i|/2+D\), its integral is bounded by
\(C/[N^3(\ell_i-|n_i|/2)^3]\), and the resulting sum converges. The horizontal interval uses (22) and has exponential rate at most
\(\Phi+o(1)+2\pi R\tau-2\pi\tau(\ell_i-|n_i|/2)\).
Choose fixed \(D\) large enough to make this uniformly smaller than \(\Phi\). The union over any far coordinate, summed with all spectators on their entire real intervals, has a fixed exponential gap. Negative charges obey the same bound by reflection. No infinite series restricted to a sharp small cube has been introduced.

The remaining charges satisfy \(|\ell_i|\le\lceil|n_i|/2+D\rceil\), a finite set after the powers are fixed. Consider first a bounded bad charge for which one ratio \(|\ell_i|/|n_i|>a\). Outside the inner cube \(K_b\), H2 supplies a fixed gap. Inside \(K_b\), reflect the chosen charge to positive sign and shift only that coordinate by \(ib/|n_i|\). Since \(0<b<a/4\), the horizontal charge loss is at least \(2\pi b(a-b)>0\); the complex-source error is \(O(b^2/n_i^2)\). On each actual vertical side \(|x_i|=b\), the fixed real quadratic loss persists, and the chirp plus charge has nonpositive real part. This proves a fixed gap for these bounded bad charges, independently of power ratios.

For the remaining finite local charge box, with all ratios at most \(a\), use H2 outside the outer cube \(K_B\), and the actual translated \(K_B\) contour and comparison (20) inside. Every nonunit magnitude has a positive fixed-\(\mathbf n\) gap. The unit drop from \(\Phi\) is \(O_D(\sum_e n_e^{-2})\). Enlarge the common diagram-dependent threshold until this drop is smaller than the previously fixed endpoint, far-charge, bounded-bad and outer-cube-complement gaps. Also ensure \(a n_0\ge1\). All complementary contributions are then exponentially smaller than the nonzero unit packet. This proves (4)–(6) for the whole all-CROSS period.

## 8. The geometric interface and the precise remaining problem

The analytic proof retains the untwisted selected action \(A_0\) and the original half twists exactly once. Put
\[
 A_{\epsilon}=A_0+\pi i\sum_e\epsilon_e\delta_e^2,
 \qquad U_{\epsilon,e}=\partial_{\delta_e}A_{\epsilon},
 \qquad V_e=-4\pi i\delta_e.
 \tag{25}
\]
The actual stationary equation of (5), with \(n_e=\epsilon_e-2p_e\), is
\[
                  U_{\epsilon,e}+p_eV_e=-2\pi i\ell_e.
 \tag{26}
\]
Once the original ordered Morse diagram has the marked action/primitive collar adapter and smooth long-filling completion, its regulator boundary term cancels the Gaussian terms at \(\ell_e=1\). Then \(2\pi\operatorname{Re}S_{0,\mathbf1}\) is the actual filled exterior's hyperbolic volume. This identifies the asymptotic of the sector (2), not automatically that of the full invariant.

The independent issue remains a bound or cancellation statement for the entire original LEFT/RIGHT remainder. Complete-radius balance is one sufficient mechanism in the terminal-fan theorem. The present proof does not assume it and supplies no replacement. In particular a nonzero sector with the correct geometric rate can still be canceled by another sector unless that remainder is controlled.

## 9. Proof dependencies and scope

The following table records the inputs and the hypotheses used in each part of the proof.

| Input | Part used here | Dependence on a flat plat or balance |
| --- | --- | --- |
| [A matched spherical triangulation has the original general Morse source](research_matched_sphere_morse_source.md) §§5–6 | Exact coefficient, primitive integer face grid, both parity cosets, mark and whole Hermite functional | Proved for the actual general Morse construction; no balance |
| [An exponentially accurate analytic interpolation of the actual fold factors](actual_positive_face_exponential_fold_interpolation.md) §§1–6 | Exact finite anchor and exponential interpolation in fixed complex face neighborhoods | Local actual triangles and protected-zero patterns only |
| [Actual all-CROSS cofactors and the complete-fold interpolant](actual_cross_cofactor_interpolant_rigidity.md) §§1–4 | Actual off-node CROSS polynomial, including odd derivative term | Independent actual cofactor growth plus interpolation; local only |
| [A global angular gap for the actual cleared cross cofactors](actual_cross_cofactor_global_angular_gap.md) §§1–4 | Whole real-spectral angular gap and omitted-terminal-node interpolation | Local positive finite matrices and physical recurrences only |
| [The positive face coefficient has one global saddle](actual_positive_face_coefficient_saddle.md) §§2–4 | Positive Hessian, primitive phase constraints and coefficient Gaussian | Actual connected ordinary triangle graph; no flat gap forest |
| [The original boundary source has exactly two flat face directions](actual_original_boundary_transverse_rank.md) §2 | Ordinary graph connectivity after the protected pair is removed | Simple sphere and marked MAIN edge |
| [Global real-spectral gap of the actual all-CROSS source](actual_global_cross_spectral_gap.md) §§1–4 | Uniform start-row/tail estimates, strict real-spectral decrease and shared strip gap | Local recurrences plus the same ordinary graph and complete radii |
| [The original full spectral numerator has the marked geometric packet](general_full_spectral_numerator_geometric_packet.md) §§1–3 | Finite phase, exact quotient measure and actual Cauchy contour | Reproved above with the Morse source; its full restoration §4 is unused |
| [The original localized spectral period has a nonzero unit-charge filling contribution](general_localized_unit_charge_filling_period.md) §§2–5 | Fixed independent signed saddle, actual side currents, nonzero first packet | H1 and exact scalar/evenness only; the old flat-plat opening is not used |
| [The entire original all-CROSS Fourier period from its local packet and global spectral gap](general_all_cross_long_filling_volume.md) §§2–5 | Whole-domain charge tails and finite bad-charge separation | H1, H2 and entire polynomial degree only |
| [Balanced terminal decorations and volume limits beyond tangle-operation trees](actual_balanced_terminal_fan_volume.md) §§6–8 | Explicit existing Morse version of these same analytic steps | Balance is used in §9 for the omitted full remainder, not in §§6–8 |

No new analytic hypothesis is imposed on a certified simple-sphere Morse source beyond these literal inputs. The original presentation's physical normalization and its marked geometric applicability must still be supplied, as stated in §1. There is no full undeformed simple-sphere volume theorem in this note.
