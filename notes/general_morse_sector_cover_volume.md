# Full long-filling volume from finite shared-curvature covers on a matched sphere

## 1. The diagram, its source, and the statement

Let \(\mathcal T\) be a fixed finite simple triangulation of the oriented sphere with at least four vertices. Choose a perfect matching of its cubic dual. The \(R\) matched pairs consist of \(2R\) triangles and have \(R+2\) white vertices. A matching pair has an ordered quadrilateral
\[
 (x_e,b_e,y_e,c_e),\qquad e=1,\ldots,R,
 \tag{1}
\]
whose common diagonal is \(x_ey_e\). The actual four-face polynomial is written in the order \(H_e(x_e,b_e,c_e,y_e)\): its input and output middle variables are \(b_e,c_e\). This distinction between the cyclic order and the polynomial argument order is retained throughout.

Use either an actual augmented diagram with this labeled cut, or the inverse-cut construction of [the general Morse source theorem](research_matched_sphere_morse_source.md), §§1–4. It produces a link in \(S^3\), with the recorded crossing disks and their primitive peripheral bases. Choose a nonmatching white edge \(uv\) as the original main-strand mark. Its two protected face variables remain exactly zero. There are \(R\) ordinary face variables. The matching diagonal cannot join the protected pair: their unique edge in the simple sphere is the marked nonmatching edge. In particular every actual quadrilateral satisfies \(x_e+y_e>0\) when all ordinary variables are positive.

Fix the retained signed half twists \(\varepsilon_e\in\{-1,0,1\}\), and require the literal outside connections and local parity pairings to give one main knot component. Filling the original auxiliary circles with disk-framed integers \(p_e\) inserts precisely
\[
 n_e=\varepsilon_e-2p_e.
 \tag{2}
\]
signed half twists. No crossing circle or terminal tangle is added by this criterion. All data, including the eventual integer powers, are fixed before the quantum level varies.

Write \(Y_D\) for this actual augmented exterior. The constructive simple-sphere packing and original cut give
\[
 \Phi_D=\frac{\operatorname{Vol}(Y_D)}{2\pi}.
 \tag{3}
\]
The geometry used here is the one proved in [the Morse geometric-contribution theorem](actual_morse_geometric_contribution.md), §§1–2. The simple-sphere packing is constructed before any terminal decoration. A supplied positive labeled cut certificate would suffice instead. Neither the source nor the geometry is obtained by asserting that a Morse diagram is a flat plat.

We define below three explicit local weighted rates \(A_{e,\mathrm C}\), \(A_{e,\mathrm L}\), \(A_{e,\mathrm R}\), and a finite set \(\Sigma\) of genuine noncentral label strings. Let \(\mathscr B\) be any finite collection of nonempty subsets of \(\Sigma\) whose union is \(\Sigma\). For each \(B\in\mathscr B\), choose one fixed positive vector \(L^B\) on all ordinary faces, with the original protected zeros. A face shared by several quadrilaterals has one common coordinate in this vector. Define
\[
 G_B(L)=\max_{\boldsymbol s\in B}
          \sum_{e=1}^R A_{e,s_e}(L)
             -\sum_{f\ne u,v}\log L_f.
 \tag{4}
\]
The subsets \(B\) need not be Cartesian products of allowed local labels. If \(\Sigma\) is empty, the remainder is exactly zero; in that case no witnesses or condition (5) are required, and the conclusion follows directly from the Morse all-CROSS theorem.

**Finite-cover theorem.** Suppose
\[
 g:=\min_{B\in\mathscr B}\{\Phi_D-G_B(L^B)\}>0.
 \tag{5}
\]
Then there is a finite threshold \(T\), depending on the fixed diagram, parity pattern and witnesses, such that every fixed signed filling vector with \(\min_e|n_e|>T\) gives a hyperbolic knot \(K_D(\boldsymbol p)\) and
\[
 \lim_{N\to\infty}\frac{2\pi}{N}
       \log|\langle K_D(\boldsymbol p)\rangle_N|
   =\operatorname{Vol}(S^3\setminus K_D(\boldsymbol p)).
 \tag{6}
\]
Here the invariant is the original reduced, zero-framed enhanced Kashaev invariant with unknot value one. The limit is through all integer levels. The signs and relative magnitudes of the sufficiently long powers are unrestricted. There is no estimate uniform in a growing diagram or in powers growing with \(N\).

More precisely, if \(Z_{N,\mathrm C}\) is the all-CROSS contribution in the original raw normalization and \(Z_N\) is the whole raw contraction, then for these powers
\[
 Z_N/Z_{N,\mathrm C}=1+O_{\boldsymbol n}(e^{-cN})
 \tag{7}
\]
for some \(c>0\). Thus the theorem supplies both the upper bound and the nonzero lower bound for the full invariant. Its criterion is not asserted for every matched sphere.

## 2. The original finite partition and every source factor

Put \(N\ge3\), \(d=N-1\), \(q=e^{\pi i/N}\), and
\[
 \chi_N(z)=2T_N(z/2)+2,\qquad
 V_N(z;\Omega)=\chi_N(z)(z-\Omega)^{-1},
 \tag{8}
\]
where \(T_N\) is the usual Chebyshev polynomial. The right side is the matrix polynomial obtained by division using \(\chi_N(\Omega)=0\); it includes the nilpotent directions at the double roots. It is not a determinant adjugate of the full tensor matrix.

The actual homogeneous numerator has paths from row \(j\) down to row \(i\), with \(0\le i\le j\le d\). Such a path carries \(b^ic^{d-j}\), the one- and two-step outer factors, and the spectral factors of every unused row. Its total face degree is exactly \(d\), and its spectral degree is at most \(d\). Define its disjoint three-part partition as follows:

| Level | LEFT | CROSS | RIGHT |
|---|---|---|---|
| \(N=2m\) | \(j\le m-1\) | \(i\le m-1,\ j\ge m\) | \(i\ge m\) |
| \(N=2m+1\) | \(j\le m-1\) | \(i\le m\le j\) | \(i\ge m+1\) |

At odd levels the central zero-step path belongs to CROSS once. Let \(H_{e,s}\) denote these literal pieces of the original local polynomial, for \(s\in\{\mathrm C,\mathrm L,\mathrm R\}\). If \(c_e\) is protected, LEFT vanishes identically: its \(c_e\) exponent exceeds \(\lfloor d/2\rfloor\). If \(b_e\) is protected, RIGHT similarly vanishes. Omit exactly those local labels. Let \(S_e\) be the remaining local label set, always containing CROSS, and put
\[
 \Sigma=\left(\prod_e S_e\right)\setminus\{\mathrm C^R\}.
 \tag{9}
\]
A string in \(\Sigma\) can still have identically zero shared coefficient because of its ordinary face targets; keeping such strings in a cover is harmless. They may be omitted if an exact source-support proof establishes their vanishing at every sufficiently large level of both parities. An envelope atom inside a local maximum is not a new label and is not an admissible way of splitting a string.

For a string \(\boldsymbol s\), use the single original coefficient extraction
\[
 S_{N,\boldsymbol s}(\boldsymbol\sigma)=
 \left[\prod_{f\ne u,v}L_f^d\right]
 \left.\prod_e H_{e,s_e}(L_{x_e},L_{b_e},L_{c_e},L_{y_e};\sigma_e)
                   \right|_{L_u=L_v=0}.
 \tag{10}
\]
Then, exactly,
\[
 S_{N,\mathrm{full}}=\sum_{\boldsymbol s\in\prod S_e}S_{N,\boldsymbol s},
 \quad C_N=S_{N,\mathrm C^R},\quad
 D_N=S_{N,\mathrm{full}}-C_N
             =\sum_{\boldsymbol s\in\Sigma}S_{N,\boldsymbol s}.
 \tag{11}
\]
Every polynomial here has degree at most \(d\) in each \(\sigma_e\). The number of strings is fixed, at most \(3^R\), and does not grow with \(N\). This is a decomposition of the original evaluation, not a family of new topological invariants.

For clarity, the Morse identity used in (10) retains all normalization data. Each box contributes the original adapter \(N^{-1}H_e/(b_ec_e)^{d/2}\). The face winding identity is \(M_f-T_f=2\) on bounded faces and \(-2\) on the exterior face. The unrestricted marked cap, after whole-source conservation, replaces its ordinary cap by \(N^{-1}(L_v/L_u)^d\). The resulting summand is
\[
 N^{-R-1}\frac{\prod_e H_e}{\prod_{f\ne u,v}L_f^d}.
 \tag{12}
\]
The primitive face-potential lattice has \(R+1\) independent \(N\)-point grids after the exterior gauge is fixed. Their count cancels \(N^{-R-1}\). At even levels its integrated parity coset is retained; it is trivial on the surviving coefficient. Canonical physical head support is imposed before root reduction, and nonnegative face degrees of total \(Rd\) force exactly the ordinary targets \(d\) and the two protected targets zero. This is the proof in the Morse source theorem, §5; it uses neither a flat gap forest nor a middle-edge forest.

## 3. The explicit triangle potential and local rates

Define the Lobachevsky function by
\[
 \Lambda(a)=-\int_0^a\log(2\sin t)\,dt,
                    \qquad 0\le a\le\pi/2.
 \tag{13}
\]
For a nonnegative triple \(w=(w_1,w_2,w_3)\) with at least two positive entries, put
\[
 D_w=\sqrt{w_1w_2+w_2w_3+w_3w_1},\qquad
 a_j=\arctan(w_j/D_w),\qquad \sum_ja_j=\pi/2,
\]
\[
 Q(w)=\frac1\pi\sum_{w_j>0}
       \{\Lambda(a_j)+\Lambda(\pi/2-a_j)+a_j\log w_j\}.
 \tag{14}
\]
If only \(w_j>0\), set \(Q(w)=\tfrac12\log w_j\). Zero terms in (14) are their continuous limits. Every triangle here has at least one positive entry, since its outer pair cannot both be protected. This is the absolutely normalized complete triangle action of [the marked cofactor action](actual_cross_cofactor_marked_action.md), not an action specified only up to a constant.

It obeys
\[
 Q(\lambda w)=Q(w)+\tfrac12\log\lambda,
 \qquad Q(x,t,y)\ge\tfrac12\log t\quad(t>0).
 \tag{15}
\]
For example, these follow from the exact variational identity
\[
 Q(w)=\max_{\substack{\alpha_j\ge0,\ \sum_j\alpha_j=1/2\
                         \alpha_j=0\text{ if }w_j=0}}
 \left\{\mathcal E(\alpha)+\sum_{w_j>0}\alpha_j\log w_j\right\},
 \quad
 \mathcal E(\alpha)=\frac1\pi\sum_j
       [\Lambda(\pi\alpha_j)+\Lambda(\pi/2-\pi\alpha_j)].
 \tag{16}
\]
The summand is strictly concave on \((0,1/2)\), with derivative \(\log\cot(\pi\alpha_j)\). Its Lagrange equation gives \(\tan(\pi\alpha_j)=w_j/D_w\), proving (14)–(16), including boundary cases by continuity. The pure allocation on the middle coordinate proves the inequality in (15). It is strict when \(x+y>0\) and \(t>0\).

At one actual quadrilateral set
\[
 \begin{aligned}
 A_{e,\mathrm C}(L)=X_e(L)
       &=Q(x_e,b_e,y_e)+Q(x_e,c_e,y_e),\\
 A_{e,\mathrm L}(L)
       &=\max\{\log c_e,Q(x_e,b_e,y_e)+\tfrac12\log c_e\},
                                      &&c_e>0,\\
 A_{e,\mathrm R}(L)
       &=\max\{\log b_e,Q(x_e,c_e,y_e)+\tfrac12\log b_e\},
                                      &&b_e>0.
 \end{aligned}
 \tag{17}
\]
Only surviving one-sided labels require a rate. Protected logarithms are not taken.

For every fixed positive ordinary vector \(L\), every retained label has the uniform estimate
\[
 \sup_{\substack{\sigma\in[-2,2]\\
                   |Z_f|=L_f\ (f\ne u,v),\ Z_u=Z_v=0}}
 |H_{e,s}(Z_{x_e},Z_{b_e},Z_{c_e},Z_{y_e};\sigma)|
       \le \exp\{N[A_{e,s}(L)+o(1)]\}.
 \tag{18}
\]
The error tends to zero along both parity sequences and is uniform over the whole indicated real spectral interval and face torus. The vector is fixed; no uniformity as its positive entries tend to zero or infinity is needed.

Here are the precise finite inputs behind (18).

**CROSS.** Section 8 of [the exact cofactor factorization](actual_cross_cofactor_factorization.md) proves coefficientwise
\[
 |H_{e,\mathrm C}(\sigma)|_{\mathrm{coef}}
       \le C\log^2(N+1)\,P_{e,\mathrm C}(-2),
                 \qquad -2\le\sigma\le2,
 \tag{19}
\]
where \(P_{e,\mathrm C}=(-1)^dH_{e,\mathrm C}\) has positive face coefficients at \(-2\). This follows by exact interpolation of the cleared lower cofactors on the actual cosine nodes, not by interpolation of the full resolvent from its values. At odd levels the central-skipping term and its first derivative are retained. Evaluating the positive right side at \(L\), its two triangle factors have rate \(X_e(L)\), with all beta, sine, half-index and polynomial \(N\) factors retained in their finite expressions. The complete triangle normalization is (14). Taking absolute values of face phases after the coefficientwise bound proves (18) for CROSS. This is only a local positive polynomial statement; it imports no full shared positive endpoint theorem.

**LEFT.** The global weighted theorem keeps the entire unused prefix, unused suffix and omitted upper half. With
\[
 \sigma=-2\cos(2\pi\delta),\quad
 \alpha_j=4\cos^2\frac{\pi(j+1/2)}N-4\sin^2(\pi\delta),
 \quad s_j=2\sin\frac{\pi j}N,
\]
the interval tail satisfies
\[
 K_{i,j}=s_j^2(x+y)K_{i,j-1}
              +s_js_{j-1}\alpha_{j-1}xyK_{i,j-2}.
 \tag{20}
\]
After dividing by its nonzero sine product, the recurrence has second coefficient \(\beta_j=\alpha_{j-1}/(s_js_{j-1})\), used only from its second step. The identity
\[
 \alpha_{j-1}+s_js_{j-1}
       =4\cos^2(\pi\delta)-4\sin^2\frac{\pi}{2N}
 \tag{21}
\]
shows \(\beta_j\ge-1\) for \(\sigma\in[-2,2\cos(\pi/N)]\). The induction
\[
 Q_r-xQ_{r-1}
 =y(Q_{r-1}-xQ_{r-2})+(1+\beta_j)xyQ_{r-2}
 \tag{22}
\]
proves that the normalized tail has nonnegative coefficients there. Thus arbitrary outer phases are bounded by positive outer moduli, without replacing a signed tail recurrence by an absolute recurrence. Middle phases are bounded by their moduli after the original start/end sum. The omitted-half factor has modulus at most \(2\) for even \(N\), and at most \(4N\) for odd \(N\). Both unused scalar products remain.

The uniform start/end transfer bound and exact endpoint optimization in [the weighted LEFT theorem](actual_global_left_weighted_spectral_envelope.md), §§1–3, then give precisely the LEFT rate in (17). Its proof uses no finite division by a sampled zero of \(\alpha_j\): the logarithms are introduced only after the original outside products have been estimated. At \(b=0\) only the first start row remains; at \(c=0\) LEFT is exactly zero.

Finally fix all face phases. The actual LEFT polynomial has degree at most \(d\) in \(\sigma\). Its bound on \([-2,b_N]\), \(b_N=2\cos(\pi/N)\), extends to the omitted cap by
\[
 \sup_{b_N\le\sigma\le2}|H_{e,\mathrm L}(\sigma)|
 \le \sup_{-2\le\sigma\le b_N}|H_{e,\mathrm L}(\sigma)|
    \exp\left\{d\operatorname{arcosh}
                   \frac{6-b_N}{2+b_N}\right\}.
 \tag{23}
\]
The last factor is bounded independently of \(N\), since \(2-b_N=O(N^{-2})\). The polynomial exterior-circle argument applies to complex coefficients, so the estimate is uniform over the same face phases. It is not a real-coefficient extremal assertion. This proves LEFT on the full interval. Literal row and middle reflection gives RIGHT in its recorded frame.

These facts prove (18) while preserving every unused spectral factor. The known exponentially large individual-coefficient comparison against \(-2\) does not contradict (18): LEFT is a weighted value estimate on a common face torus, not coefficientwise domination.

## 4. Any finite cover gives the strict shared source bound

Fix a genuine string \(\boldsymbol s\) in a cover member \(B\). Apply the ordinary multivariate Cauchy coefficient formula to (10), after the protected zero substitutions, on the single torus \(|Z_f|=L_f^B\). It gives
\[
 \begin{aligned}
 |S_{N,\boldsymbol s}(\boldsymbol\sigma)|
 &\le \prod_{f\ne u,v}(L_f^B)^{-d}
         \prod_e\sup_{\text{same face torus}}
                        |H_{e,s_e}(Z;\sigma_e)|,\\
 \limsup_{N\to\infty}\frac1N
    \log\|S_{N,\boldsymbol s}\|_{[-2,2]^R}
 &\le \sum_e A_{e,s_e}(L^B)
                 -\sum_{f\ne u,v}\log L_f^B
 \le G_B(L^B).
 \end{aligned}
 \tag{24}
\]
The difference between \(d/N\) and \(1\) costs only \(N^{-1}\sum_f\log L_f^B\), since all witness coordinates are fixed. Repeated incidences of an ordinary face use its same modulus and phase; (24) makes no independent choice at separate boxes.

Assign each string to one cover member containing it. There are finitely many strings, witnesses and local labels, so (18) and (24) are simultaneous. The triangle inequality is used only after these genuine sector polynomials have each been estimated. Equations (5), (11) give
\[
 \limsup_{N\to\infty}\frac1N
                  \log\|D_N\|_{[-2,2]^R}\le\Phi_D-g.
 \tag{25}
\]
In particular, for every \(0<\eta<g\), all sufficiently large \(N\) satisfy \(\|D_N\|\le e^{N(\Phi_D-\eta)}\). Both parity subsequences are included. Overlap of cover members causes no problem; assignment is made once. There is no exchange of a radius infimum with a sector maximum.

If \(B=\prod_e S_{B,e}\) is Cartesian and excludes the all-CROSS string, then (4) becomes
\[
 G_B(L)=\sum_e\max_{s\in S_{B,e}}A_{e,s}(L)
                        -\sum_{f\ne u,v}\log L_f.
 \tag{26}
\]
For a non-Cartesian \(B\), the maximum in (4) retains its correlations and can be smaller than (26) for its Cartesian hull. This generality uses only finite label strings, not an invented splitting of a local envelope.

## 5. Finite Hermite transfer, without a new charge-tail argument

Let \(\mathcal L_N^n\) be the original full-Hermite functional inserting \(R^n\). For a polynomial \(H\) of degree at most \(d\), put \(P(\phi)=H(2\cos\phi)\), \(\phi_k=(2k+1)\pi/N\). Its exact formula is
\[
 \mathcal L_N^nH=-\frac1{N^2}\sum_{k=0}^{N-1}
    [\cos\phi_k f_kP_k+\sin\phi_k f'_kP_k
                                 +\sin\phi_k f_kP'_k],
 \tag{27}
\]
where primes denote derivatives in \(\phi\), and
\[
 f_n(2\cos\phi)=q^{nd^2/4}
        \exp\!\left(\frac{inN(\phi-\pi)^2}{4\pi}\right),
 \quad |f_n|=1,\quad |f_n'|\le |n|N/2.
 \tag{28}
\]
The Cartan scalar is present in (28), with its original lift \(q^a=e^{\pi ia/N}\). Paired roots occur twice in the midpoint grid. At odd \(N\), the grid contains \(\phi=\pi\) once; the derivative of the sine in (27) gives exactly the simple-root value. Thus this formula includes both value and first-normal terms of the actual finite matrix. It is not an approximation of a generic spectral integral.

The exact trigonometric derivative inequality \(\|P'\|\le d\|P\|\), proved by the finite Riesz interpolation in [the uniform filling norm theorem](actual_uniform_filling_supremum_bound.md), §§2–4, gives
\[
 |\mathcal L_N^nH|\le(1+|n|/2)\|H\|_{[-2,2]}.
 \tag{29}
\]
This works for complex polynomials. Applying it successively to the degree-\(d\) polynomial in each variable proves
\[
 \left|\left(\bigotimes_e\mathcal L_N^{n_e}\right)D_N\right|
 \le \prod_e(1+|n_e|/2)\,\|D_N\|_{[-2,2]^R}.
 \tag{30}
\]
There is no dimension factor: after applying one functional, take the supremum over the remaining real variables before continuing.

One can retain the sharper exact constant. The full local numerator equals CROSS at every spectral node, by the original complete-node identity in the cofactor factorization, §3. Hence \(D_N\) vanishes on the whole product node grid, though not necessarily on each node hyperplane. Expanding (27) in all variables, its all-value term vanishes. Iterated derivative estimates give
\[
 \left|\left(\bigotimes_e\mathcal L_N^{n_e}\right)D_N\right|
 \le\left[\prod_e(1+|n_e|/2)
          -\prod_e(1/N+|n_e|/2)\right]\|D_N\|.
 \tag{31}
\]
Either (30) or (31) is sufficient. In particular the argument does not depend on claiming that all normal data vanish. For fixed powers their costs have zero exponential rate.

Multilinearity of the original source gives exactly
\[
 Z_N=\left(\bigotimes_e\mathcal L_N^{n_e}\right)S_{N,\mathrm{full}},
 \qquad
 Z_{N,\mathrm C}=\left(\bigotimes_e\mathcal L_N^{n_e}\right)C_N.
 \tag{32}
\]
There is no further \(N^R\) or color average in (32); the grid cancellation was (12). Consequently (25) proves a strict augmented-action remainder estimate for the actual filled contraction. No complex strip, discarded-cube Fourier series, or new estimate of infinitely many charges is needed for this remainder.

## 6. The nonzero geometric contribution and the smaller filled volume

The analytic input here is [the full Morse all-CROSS period](actual_morse_cross_filling_period.md), not the old theorem limited in its opening to flat plats. Its H1 and H2 hold for the exact coefficient (10) with \(\boldsymbol s=\mathrm C^R\), on the actual marked simple sphere. The proof uses the connected ordinary triangle graph and its primitive face lattice, the local cleared-cofactor interpolation including the odd central derivative, and the full spectral polynomial degree. A complete-radius balance inequality and a middle-edge forest are not among its hypotheses.

For fixed independently signed sufficiently long powers it gives a nonzero asymptotic
\[
 Z_{N,\mathrm C}=a_{N,\boldsymbol n}\exp(N\mathcal A_{\boldsymbol n}),
 \qquad \frac1N\log|a_{N,\boldsymbol n}|\longrightarrow0,
\]
\[
 \operatorname{Re}\mathcal A_{\boldsymbol n}
     =\Phi_D-O_D\!\left(\sum_e n_e^{-2}\right),\qquad
 2\pi\operatorname{Re}\mathcal A_{\boldsymbol n}
     =\operatorname{Vol}(S^3\setminus K_D(\boldsymbol p)).
 \tag{33}
\]
The finite phase can equivalently remain in the exponent, as in that theorem; its difference from the limiting phase is absorbed in \(a_{N,\boldsymbol n}\) only at this exponential-rate statement. We do not discard its exact scalar in an identity of invariants.

For normalization, the relative asymptotic in the cited theorem retains the factor
\[
 q^{d^2\sum_e n_e/4}(-2i)^R\sqrt{2\pi}\,N^{R+1/2}
 \frac{\prod_e\sin(2\pi\delta_{N,\boldsymbol1,e})}
 {\sqrt{\det H_N(\boldsymbol\delta_{N,\boldsymbol1})}
                         \sqrt{\det Q_{N,\boldsymbol1}}}
 \exp(NS_{N,\boldsymbol1}).
 \tag{34}
\]
The two determinant roots have the original Gaussian branches. Its sine and determinant coefficient tends to a nonzero value for every fixed sufficiently long tuple. The raw source sign \((-1)^{dR}\) and Fourier parity character \((-1)^{(N+1)R}\) multiply to one. Opposite unit-charge signs agree by the exact trace parity identity, and all other charges and endpoint currents have already been bounded in that theorem. This is the source of the nonzero lower bound, not a positivity assertion about the final oscillatory sum.

The geometric equality in (33) is [the Morse geometric theorem](actual_morse_geometric_contribution.md), §§4–9. It retains the actual primitive slope \(\mu_e+p_e\lambda_e\), the original \(n_e=\varepsilon_e-2p_e\), and the log-link periods before multiplication by \(p_e\). The positive cut and near-complete deformation give the original compact core, and the primitive period gives its smooth solid-torus completion. The main cusp remains complete. Thus the right side of (33) is the original filled knot complement, not a comparison manifold or only a representation regulator.

Choose \(\eta\in(0,g)\). Increase the common long-filling threshold until all analytic and geometric hypotheses just cited hold and the action drop in (33) is less than \(\eta/2\). This is possible for independent signs and arbitrarily unbalanced magnitudes: the drop is bounded by a fixed constant times \(\sum_en_e^{-2}\). From (25), (30) and the nonzero lower in (33), the filled remainder divided by \(Z_{N,\mathrm C}\) is exponentially small. This proves (7), hence (6).

The original reduced contraction differs from the chosen zero-framed enhanced Kashaev value only by its recorded component/framing character of modulus one at complete color; for a knot the enhanced component sign is one. If the full one-cut modified convention is used instead, its additional factor is \(i^{N+3}/N\). Both statements are the source normalization, not new choices made after taking a limit. They do not change (6).

## 7. Anchors, Cartesian branches, and finite verification

The identities in (15) imply
\[
 \begin{aligned}
 H_e(L)&:=\max_{s\in S_e}A_{e,s}(L)
       =\max\bigl(\{X_e(L)\}\cup\{\log b_e:b_e>0\}
                                  \cup\{\log c_e:c_e>0\}\bigr),\\
 \max(A_{e,\mathrm C},A_{e,\mathrm L})&=\max(X_e,\log c_e),\\
 \max(A_{e,\mathrm C},A_{e,\mathrm R})&=\max(X_e,\log b_e),
 \end{aligned}
 \tag{35}
\]
where the last two formulas are used only when that one-sided label survives. In particular an anchored branch fixes one surviving LEFT or RIGHT at \(e\) and allows all labels elsewhere. Its cost is
\[
 A_{e,s}(L)+\sum_{a\ne e}H_a(L)
                           -\sum_{f\ne u,v}\log L_f.
 \tag{36}
\]
The at most \(2R\) surviving anchors cover every noncentral string. Thus strict inequalities (36) below \(\Phi_D\), each at its own shared vector, are a sufficient special case of the theorem. Further branching is legitimate only on genuine labels. It can lower the maximum in (4), and each resulting branch may use a different shared vector.

A certificate can avoid a numerical solution of the complete packing. For each original triangle choose nonnegative corner numbers \(\alpha_{T,f}\) such that
\[
 \sum_{f\in T}\alpha_{T,f}=\tfrac12,\qquad
 \sum_{T\ni f}\alpha_{T,f}=1\ (f\ne u,v),\qquad
 \alpha_{T,u}=\alpha_{T,v}=0.
 \tag{37}
\]
By (16), after summing triangles all logarithmic face terms cancel. Evaluating at the actual complete packing \(L^{\mathrm{geom}}\) gives
\[
 \sum_T\mathcal E(\alpha_T)
 \le\sum_eX_e(L^{\mathrm{geom}})-\sum_{f\ne u,v}\log L_f^{\mathrm{geom}}
 =\Phi_D.
 \tag{38}
\]
The last equality is the calibrated complete action in the Morse geometry theorem. It uses no full positive-endpoint asymptotic. Exact feasible corner data therefore supply a lower bound for the number on the right of (5).

The combinatorial cover, positive shared witnesses, equations (37), and strict interval inequalities
\[
 G_B(L^B)<\sum_T\mathcal E(\alpha_T)
                       \qquad(B\in\mathscr B)
 \tag{39}
\]
form one fully finite certificate. Alternatively use any independently certified lower bound for \(\Phi_D\). Strict witnesses may be made rational because all ordinary coordinates are positive and the rates are continuous there; protected coordinates remain exactly zero. The numerical task is an enclosing evaluation of explicit functions at fixed data, not a sample-based asymptotic proof.

## 8. Dependency boundary

The transfer is now closed at the stated criterion. Its inputs are the exact general Morse coefficient and normalizations; the phase-uniform real-spectral local CROSS/LEFT/RIGHT bounds; and the proved Morse all-CROSS analytic and geometric theorems. The finite norm theorem supplies the remainder transfer directly. No flat-plat isotopy, full shared positive endpoint theorem with an additional forest hypothesis, or new Fourier-tail theorem is used.

What remains a separate mathematical problem is whether a given original marked sphere admits the strict finite cover witnesses. This theorem neither asserts universal feasibility nor treats the fractional comparison atoms of a LEFT envelope as exact source pieces. It also makes no moving-main-meridian, shifted-chart, operator, or short-filling claim for these new planar applications.
