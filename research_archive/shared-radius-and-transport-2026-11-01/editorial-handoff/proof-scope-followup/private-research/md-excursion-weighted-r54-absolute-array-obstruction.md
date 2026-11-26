# A protected spectral endpoint forces an oversized absolute shared-array sum

This note proves a limitation of termwise absolute estimates for the original shared source. It strengthens the fixed-sector envelope obstruction: at one fixed real spectral tuple, the sum of absolute values of the actual local-coefficient products already has rate strictly greater than the complete augmented volume rate. It is not merely a large value of a Cauchy envelope.

The absolute value is taken before summing the shared arrays. The signed shared coefficient is a different quantity. Here its remaining cancellation is an explicit alternating sum. We also show that optimizing over every possible positive reference in a weighted Cauchy inequality gives exactly this absolute sum. No choice of a positive reference on the unchanged array partition can repair the resulting rate obstruction.

## 1. The original arrays and the quantity being bounded

Fix a simple matched white sphere with \(R\) crossing regions and its original marked main edge. There are \(R\) ordinary face variables; the two protected face variables are set to zero. Set
\[
 N=2m,\qquad d=N-1,\qquad M=m-1.
 \tag{1}
\]
Here \(M\) is an integer degree, not a meridian eigenvalue. All limits in this note run through even levels.

For a local label \(s_e\in\{\mathrm C,\mathrm L,\mathrm R\}\), let
\[
 H_{e,s_e}(\boldsymbol L;\sigma_e)
   =\sum_{\substack{v_e\ge0\\|v_e|=d}}
                  a_{e,N}(v_e;\sigma_e)\boldsymbol L^{v_e}
 \tag{2}
\]
be the literal central, left, or right path piece of the original full resolvent numerator. Coefficients with an unsupported endpoint are zero. The spectral coordinate is \(\sigma_e\in[-2,2]\). Protected substitutions are imposed on each factor.

Let \(\Gamma_{N,\boldsymbol s}\) be the arrays of local incidence degrees satisfying all original face targets: total \(d\) at every ordinary face and zero at each protected face. Repeated occurrences of a face have the same global label. Define
\[
 \begin{aligned}
 A_{\boldsymbol v}(\boldsymbol\sigma)
   &=\prod_e a_{e,N}(v_e;\sigma_e),\\
 S_{N,\boldsymbol s}(\boldsymbol\sigma)
   &=\sum_{\boldsymbol v\in\Gamma_{N,\boldsymbol s}}
                           A_{\boldsymbol v}(\boldsymbol\sigma),\\
 \mathcal A_{N,\boldsymbol s}(\boldsymbol\sigma)
   &=\sum_{\boldsymbol v\in\Gamma_{N,\boldsymbol s}}
                           |A_{\boldsymbol v}(\boldsymbol\sigma)|.
 \end{aligned}
 \tag{3}
\]
The second line is the actual shared spectral coefficient. The last is the absolute sum of its local-coefficient products. It is also the original target coefficient of the product of the coefficientwise absolute local polynomials. It is not the absolute value of the coefficient after multiplication and cancellation.

These are the raw polynomials in the exact general-Morse source identity. There is no new local mark, face target, factor \(N^R\), or independently normalized contraction. The original filling functionals and exterior framing factors have not been applied.

## 2. A structural transfer from a feasible angle table

Assume the selected string is left at one region \(e_*\), central at all other regions. Write its original ordered quartet as
\[
                   (x,b,z,y),
 \qquad b,y\text{ protected},\quad x,z\text{ ordinary}.
 \tag{4}
\]
The retained triangle of the left envelope has only its \(x\) corner ordinary. The overloaded middle is \(z\).

There are \(2(R-1)\) original spectator triangles. For each such triangle \(t\), let \(I_t\) be its nonempty ordinary support. Suppose numbers \(\alpha_{tf}>0\), for \(f\in I_t\), and \(0<\lambda<1\) obey
\[
 \sum_{f\in I_t}\alpha_{tf}=\frac12,\qquad
 \sum_{t\ni f}\alpha_{tf}
       +\frac{\lambda}{2}\mathbf1_{f=x}
       +\left(1-\frac{\lambda}{2}\right)\mathbf1_{f=z}
       =1
 \quad(f\text{ ordinary}).
 \tag{5}
\]
These are equations on the original incidences. No spectator triangle has a fractional row mass. Assume also that the graph joining ordinary faces occurring in one spectator triangle is connected.

Use the absolutely normalized triangle entropy
\[
 f(a)=\frac{\Lambda(\pi a)+\Lambda(\pi/2-\pi a)}{\pi},
 \qquad
 \Lambda(t)=-\int_0^t\log|2\sin u|\,du,\qquad
 E_{\mathrm{tab}}=\sum_t\sum_{f\in I_t}f(\alpha_{tf}).
 \tag{6}
\]
A singleton triangle has its one load equal to \(1/2\), and contributes zero entropy.

**Theorem.** At the fixed real spectral tuple
\[
             \sigma_{e_*}=+2,\qquad \sigma_e=-2\ (e\ne e_*),
 \tag{7}
\]
the original absolute-array sum satisfies
\[
       \liminf_{\substack{N\to\infty\\N\ \mathrm{even}}}
       \frac1N\log\mathcal A_{N,\boldsymbol s}(\boldsymbol\sigma)
                         \ge E_{\mathrm{tab}}.
 \tag{8}
\]
The table and diagram remain fixed. Rationality is convenient for certification, but the proof only needs positivity, exact balances, and fixed support. It constructs one actual local array at every sufficiently large even level, rather than only a denominator subsequence.

## 3. The protected left coefficient has zero exponential cost at \(+2\)

Put
\[
 c_r=2\cos\frac{(2r+1)\pi}{N},\qquad
 s_r=2\sin\frac{\pi r}{N},\qquad
 S_j=\prod_{r=1}^{j}s_r,\qquad
 T_j=\prod_{r=0}^{j}2\sin\frac{(r+1/2)\pi}{N}.
 \tag{9}
\]
The empty product \(S_0\) is one. At (4), the original left path must end at row zero, and all its lowering steps are one-step \(x\) factors. For \(0\le j\le M\), its coefficient is exactly
\[
 [L_x^jL_z^{d-j}]\,H_{e_*,\mathrm L}(+2)
       =(-1)^j U_{N,j},\qquad
 U_{N,j}=4\frac{S_j^2}{T_j^2}>0.
 \tag{10}
\]
Indeed, the visited rows are \(0,\ldots,j\); every unused row \(j+1,\ldots,d\) contributes \(2-c_r\). The product over all rows is \(\chi_N(2)=4\), where \(\chi_N(\sigma)=2T_N(\sigma/2)+2\). This proves (10) without dividing at a zero.

Pairing factors in the full sine products gives
\[
 S_M^2=m,\qquad T_M^2=2,\qquad U_{N,M}=N.
 \tag{11}
\]
Moreover
\[
 \frac{U_{N,j}}{U_{N,j-1}}
       =\frac{\sin^2(j\pi/N)}{\sin^2((j+1/2)\pi/N)}
       \le1\quad(1\le j\le M).
 \tag{12}
\]
All these angles lie in the increasing half of sine. Consequently
\[
             N\le U_{N,j}\le
             \csc^2\frac{\pi}{2N}\le N^2.
 \tag{13}
\]
The last inequality uses \(\sin t\ge2t/\pi\) on \(0\le t\le\pi/2\). Thus the selected coefficient is nonzero and has logarithm \(o(N)\), uniformly in the entire left range. Its sign \((-1)^j\) is retained.

## 4. Integer arrays approximating the original balanced table

At each central spectator, the exact even-level factorization contains the coefficientwise positive summand
\[
                  s_m^2(L_x+L_y)D_bD_c
                       =4(L_x+L_y)D_bD_c.
 \tag{14}
\]
Here \(D_b,D_c\) are the original cleared lower cofactors of degree \(M\) on their respective triangles. No independent triangle normalization has been inserted.

Choose one ordinary outer face at each spectator for the linear factor in (14). Such a choice exists: the matched outer diagonal cannot be the original nonmatching protected edge in a simple sphere. Let \(c_f\) count the choices, so \(\sum_f c_f=R-1\). Set
\[
 j_N=\lfloor M\lambda\rfloor,\qquad e_N=M\lambda-j_N\in[0,1).
 \tag{15}
\]
The anchor uses \(L_x^{j_N}L_z^{d-j_N}\). The triangle factors must have row degrees \(M\) and column degrees
\[
 b_{f,N}=d-c_f-j_N\mathbf1_{f=x}
                       -(d-j_N)\mathbf1_{f=z}.
 \tag{16}
\]
The preliminary real table \(2M\alpha_{tf}\) has the correct row sums. Equations (5) and (16) show that the required column correction is
\[
 \delta_f=
 \begin{cases}
  1-c_x+e_N,&f=x,\\
  -c_z-e_N,&f=z,\\
  1-c_f,&f\ne x,z.
 \end{cases}
 \qquad
 \sum_f\delta_f=0,\qquad
 \sum_f|\delta_f|<2R+2.
 \tag{17}
\]
Choose a spanning tree in the connected ordinary spectator graph, and for each tree edge choose one original triangle containing its endpoints. Transfer \(\delta\) along this tree: each transfer subtracts from one corner and adds to another corner of that same row. It preserves every row total. An edge transfer has magnitude at most \(\sum_f|\delta_f|\), so each entry changes by at most \((R-1)(2R+2)\), uniformly in \(N\).

The allowed entries \(\alpha_{tf}\) are strictly positive and the table is fixed. The corrected real table is therefore nonnegative for every sufficiently large \(N\). It has integer row and column sums.

Rounding must preserve its limiting loads. Subtract the floor of each entry. The remaining fractional table has integer margins and entries in \([0,1)\). On a cycle of fractional entries in its row-column graph, change alternating entries in opposite directions until one reaches zero or one, staying in \([0,1]\). Margins are unchanged. A nonempty forest of fractional entries is impossible: a leaf would have an integer margin and exactly one fractional entry. Repetition makes the table integral. Adding the floors back changes each corrected entry by at most one.

The resulting integer loads satisfy
\[
 k_{tf,N}=2M\alpha_{tf}+O_D(1),\qquad
 \sum_f k_{tf,N}=M,\qquad
 \sum_t k_{tf,N}=b_{f,N}.
 \tag{18}
\]
Unsupported and protected incidences remain absent; \(k_{tf,N}/N\to\alpha_{tf}\). At each spectator, aggregate the two triangle monomials and its chosen outer unit. Both middle degrees are at most \(M\), so this is an actual central monomial. Together with the anchor these form one array in \(\Gamma_{N,\boldsymbol s}\).

## 5. The lower rate uses actual central coefficients

The uniform closed coefficient theorem for the actual cofactor \(D_t\) gives, on every original supported triangle face,
\[
 \frac1N\log[\boldsymbol L^{k_{t,N}}]D_t
       \longrightarrow\sum_{f\in I_t}f(\alpha_{tf})
 \quad\text{when (18) holds}.
 \tag{19}
\]
The source remains at level \(N\). Its degree is \(M=N/2-1\); the bounded difference from \(N/2\) disappears only after the uniform closed estimate and continuity. No arbitrary exponential normalization is absorbed in (19).

At \(-2\), the original central polynomial differs from its positive path polynomial by the single sign \((-1)^d\). Hence the absolute value of its selected coefficient is at least the positive coefficient from (14). All spectators together contribute at least
\[
                 4^{R-1}\prod_t
                       [\boldsymbol L^{k_{t,N}}]D_t.
 \tag{20}
\]
The anchor adds \(U_{N,j_N}\ge N\). This one original array contributes at least
\[
              N\,4^{R-1}
                 \prod_t[\boldsymbol L^{k_{t,N}}]D_t
 \tag{21}
\]
to (3). Apply (19) to the fixed finite set of rows to prove (8). Neither an asymptotic for the full signed source nor a positive endpoint-volume theorem for arbitrary Morse diagrams enters this argument.

## 6. The certified 54-region instance

Use the actual source of the published singleton-sector obstruction. It has \(R=54\), anchor \(e_*=32\), and
\[
       (x,b,z,y)=(0,50,16,29),\qquad
       \lambda=\frac{548219162717}{10^{12}}.
 \tag{22}
\]
The protected faces are \(29,50\). Its \(106\) central triangle rows obey (5) exactly; their ordinary support graph is connected, and all allowed corner loads are positive. These are properties of the recorded original incidence data.

The rational interval certificate proves
\[
 E_{\mathrm{tab}}>67.8938190642,\qquad
 \Phi<67.6882466366,\qquad E_{\mathrm{tab}}-\Phi>\frac15,
 \tag{23}
\]
where \(2\pi\Phi=\operatorname{Vol}(Y_D)\) is the actual complete augmented volume. The original parity data admit a knot-producing filling pattern. Therefore, at (7),
\[
 \liminf_{\substack{N\to\infty\\N\ \mathrm{even}}}
       \frac1N\log\mathcal A_{N,\boldsymbol s}(\boldsymbol\sigma)
            \ge E_{\mathrm{tab}}>\Phi+\frac15 .
 \tag{24}
\]
The whole absolute-array sum, including all genuine strings, is at least as large. Thus the triangle inequality on every original local-coefficient product cannot give a universal upper bound at rate \(\Phi\), even when restricted to genuine noncentral strings.

Shared positive face gauges cannot change this conclusion. They multiply every feasible array by the same original target monomial; dividing by that monomial cancels it exactly. This remains true for level-dependent gauges.

## 7. Optimizing every positive Cauchy reference gives the same obstruction

For any finite complex array \((A_a)_{a\in I}\),
\[
 \inf_{\substack{w_a>0\\a\in I}}
  \left(\sum_a w_a\right)^{1/2}
  \left(\sum_a\frac{|A_a|^2}{w_a}\right)^{1/2}
                         =\sum_a|A_a|.
 \tag{25}
\]
The lower bound is Cauchy applied to the vectors \(\sqrt{w_a}\) and \(|A_a|/\sqrt{w_a}\). If every \(A_a\ne0\), equality holds for \(w_a=|A_a|\), or any common positive multiple. If some entries vanish, set their weights to a positive parameter tending to zero and use \(w_a=|A_a|\) elsewhere. If all entries vanish, both sides are zero.

Apply (25) to the original array partition in (3), at the fixed mixed spectrum (7). The best possible positive-reference Cauchy bound is exactly \(\mathcal A_{N,\boldsymbol s}\). Thus (24) excludes a universal bound of rate at most \(\Phi\) from this procedure even when the reference is allowed to depend arbitrarily on the level, all spectral coordinates, the diagram, and the full shared array. In particular it excludes every product reference and every positive shared-face reweighting on this unchanged partition.

This is not a statement about all inner products or all regroupings. A non-diagonal Hermitian form can retain off-diagonal phase correlations, and a grouped sum can already contain cancellations before Cauchy is applied. Those are different objects from the positive diagonal reference in (25).

## 8. The signed source remains an alternating shared sum

Let \(B_{N,j}\ge0\) be the shared coefficient of the product of the positive central spectator polynomials, with ordinary targets \(d-j\) at \(x\), \(j\) at \(z\), and \(d\) elsewhere. The protected targets remain zero. Exactly,
\[
 \begin{aligned}
 S_{N,\boldsymbol s}(+2,-2,\ldots,-2)
   &=(-1)^{d(R-1)}
           \sum_{j=0}^{M}(-1)^j U_{N,j}B_{N,j},\\
 \mathcal A_{N,\boldsymbol s}(+2,-2,\ldots,-2)
   &=\sum_{j=0}^{M}U_{N,j}B_{N,j}.
 \end{aligned}
 \tag{26}
\]
The \(+2\) entry is the original anchor \(e_*\). Both lines use the same outside shared coefficients. They neither pair independently chosen local maximizers nor replace the target by a free boundary state.

There are only \(M+1\) terms, but polynomially many terms can still cancel exponentially. Hence (24) supplies no lower bound for the signed source. A full volume proof could still use cancellations across \(j\), across genuine strings, or inside the exact spectral filling functional. None is estimated here.

The localized entropy and Bregman tests remain correct sufficient criteria where their inequalities hold. They cannot universally repair the same fixed envelopes. Equation (24) shows that replacing those envelopes by exact absolute local coefficients is not a universal repair either. Equation (25) extends this obstruction to every positive diagonal Cauchy reference on the original array partition.

## 9. Dependencies and scope

The finite numerator paths and the central factorization are in actual_cross_cofactor_factorization.md, §§1–2. The source normalization and uniform closed triangle entropy are in actual_fejer_half_block_entropy.md, §§4–5, especially (15)–(16). The protected one-path formula is also in actual_protected_outer_spectral_energy.md, §§1–3; its \(+2\) simplification is proved directly above.

The incidence, protected mark, knot parity, positive table, connected support, and interval bounds (23) are the recorded data and certificates of actual_singleton_sector_envelope_obstruction.md, §§2–5. The general-Morse coefficient identity fixes the meaning of (3). Only these finite-source facts are used to transfer the certificate into (24).

This is an even-level obstruction to a universal estimation strategy. It asserts neither the same lower bound at odd levels, nor a signed polynomial asymptotic, a filled scalar lower bound, a moving-meridian theorem, or a violation of knot-volume equality.
