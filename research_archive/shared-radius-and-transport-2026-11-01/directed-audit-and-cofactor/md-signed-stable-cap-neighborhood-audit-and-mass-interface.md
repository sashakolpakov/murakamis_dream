# Audit of the signed stable cap criterion and its actual source mass

1 November 2026. This is a private mathematical audit of the combined criterion `signed-stable-cap-neighborhood-criterion.md`. The companion JSON records the exact files read. It separates a proved conditional norm estimate from the remaining construction for the varying original source. No public file is changed.

## 1. Verdict and precise scope

Equations (15)--(17) of the criterion are correct under their stated hypotheses. The current version explicitly requires a nonzero homogeneous real-stable endpoint polynomial with nonnegative coefficients, degree \(d=N-1\), a fixed \(T\ge1\), and finite real pressures \(F_0,F_T\). Those hypotheses remove the two initial exposition ambiguities. No further correction is needed in the finite bound or order of limits.

The result is conditional on one exact decomposition satisfying **both** the root-count condition and its absolute positive-mass estimate. The actual source already has a useful unsigned Taylor-mass estimate, proved below. This is not automatically the mass of a signed stable decomposition. A positive monomial decomposition attains the unsigned mass but need not have the required root-count control. These are distinct obligations, not an obstruction to every possible construction.

The finite functional estimates hold at both parities. Applying them to the presently proved stable determinant exterior restricts the conclusion to odd levels. This audit makes no even-level, whole-spectral-cube, full-remainder, or volume assertion.

## 2. The original cap functional and the cutoff

Put \(d=N-1\), \(M=\lfloor N/2\rfloor-1\), and \(\theta=\pi/N\). The actual protected functional is
\[
 S_N(\sigma;Q)=\sum_{j=0}^{M}v_j(\sigma)q_j,
 \qquad Q(A,C)=\sum_{j=0}^{d}q_jA^jC^{d-j},
 \qquad
 v_j(\sigma)=(-1)^jS_j^2\prod_{r=j+1}^{d}(\sigma-c_r),
 \tag{A1}
\]
where \(S_j=\prod_{r=1}^{j}2\sin(r\theta)\) and \(c_r=2\cos((2r+1)\theta)\). Thus all unused spectral rows remain present. The exact original extraction has no additional target or coefficient reversal beyond the convention in (A1).

For \(a_j=(-1)^jq_j\), the sine-Cauchy Gram form is
\[
 \|\mathcal T_NQ\|_{C_N}^2
 =\sum_{i,j=0}^{M}\overline{a_i}(C_N)_{ij}a_j
 =\frac{N\sin\theta}{\pi}\int_0^\infty
       \frac{|\sum_{j=0}^{M}a_jt^j|^2}{1+t^N}\,dt.
 \tag{A2}
\]
Here \(2M=N-2\) at even levels and \(2M=N-3\) at odd levels. The moment integral is therefore finite; no full-degree squared polynomial has been substituted. The spectral dual estimate of `research_cap_uniform_spectral_gap.md`, equations (6)--(10), applies to arbitrary complex \(q_j\): it is ordinary Hermitian Cauchy--Schwarz with the real vector \(g_j=(-1)^jv_j/U_0\), where \(U_0=\csc^2(\theta/2)\). Consequently
\[
 \sup_{\sigma\in[-2,2]}|S_N(\sigma;Q)|
 \le \frac{\pi^{5/2}}4\csc^2(\theta/2)(M+1)
                  \|\mathcal T_NQ\|_{C_N}.
 \tag{A3}
\]
The constant is polynomial in \(N\). The entire signed deformed exterior is a legitimate input to (A3), by linearity of (A1). It need not be positive or stable. Positivity and stability are used only when estimating its component polynomials before the norm triangle inequality.

Every diagonal entry \((C_N)_{jj}\), \(j\le M\), is at most one. Thus for a polynomial with nonnegative coefficients,
\[
 \|\mathcal T_NQ\|_{C_N}
 \le\sum_{j=0}^{M}q_j\sqrt{(C_N)_{jj}}
 \le Q(1,1).
 \tag{A4}
\]
This is the high-order estimate in the criterion, with no hidden moment above degree \(2M\).

## 3. Root-count estimates and the finite split

For two degree-\(d\) stable positive binary polynomials, use normalized factors \((1-\lambda)C+\lambda A\), \(0\le\lambda\le1\). Atoms at zero and one retain the factors \(C\) and \(A\). A bound \(r\) on the difference of their cumulative root counts gives
\[
 \left|\sum g(\mu_j)-\sum g(\lambda_j)\right|
 \le r\int_0^1|g'(s)|\,ds.
 \tag{A5}
\]
It follows by integration by parts for two measures of equal total mass, including their endpoint atoms. The four functions defining \(R_T\) have variations \(1,1,2,T+T^{-1}\). The logarithmic tilt has variation \(\log T\). Hence the criterion's (8) and (9) have the correct constants and direction.

The finite alternating-section lemma in the original cap note bounds the cutoff terms by
\[
 \max\{Q(T,1)T^{-M},(d+1)q_M\}+q_M
 \le(d+2)Q(T,1)T^{-M}.
 \tag{A6}
\]
This proves the simplification used in (10). It remains valid when some endpoint coefficients vanish, by continuity or directly from the nonnegative-coefficient inequality.

In an exact expansion \(\sum_\alpha c_\alpha\boldsymbol u^{\beta_\alpha}Q_\alpha\), set \(k_\alpha=|\beta_\alpha|\). The complex-polydisk estimate \(|\boldsymbol u^{\beta_\alpha}|\le\varepsilon^{k_\alpha}\) is exact. Terms of order \(k_\alpha\le\delta N\) have root-count distance at most \(J\delta N\). Their normalized root statistics and tilt therefore have precisely the costs in the first two terms of (15). For the remaining terms,
\[
 \varepsilon^{k_\alpha}
 \le v^{k_\alpha}(\varepsilon/v)^{\delta N},
 \qquad 0<\varepsilon<v,
 \tag{A7}
\]
and (A4) gives the last term of (15). Every term, including order zero, enters the mass \(W_N\). The number of terms introduces no unrecorded factor.

The constant \(J\) measures root-count change per spectral order, not per name assigned to a local perturbation. In particular the original odd term \(u s_m^2xyD_bD_c\) has spectral order one and two lower cofactors. It cannot be assigned rank one solely because it contains one power of \(u\). The criterion correctly allows a fixed \(J\), such as two if a source construction justifies it.

## 4. Limits and uniformity

Keep \(\delta>0\), \(v>0\), and \(T\ge1\) fixed first. Take the upper limit along the specified level set. Then let \(\varepsilon\downarrow0\). The high-order rate is
\[
 F_0-\delta\log(v/\varepsilon)+\omega(v),
 \tag{A8}
\]
which tends to minus infinity. The low-order rates have \(\omega(\varepsilon)\to0\). Finally let \(\delta\downarrow0\). Since \(R_T\ge1/4\), this last logarithmic passage is continuous. Neither a uniform-in-\(v\) version of the mass limsup nor an exchange of the \(N\) and \(\varepsilon\) limits is used.

The resulting upper bound is uniform over every complex deformation vector in the stated polydisk and over the actual cap spectrum \(\sigma\in[-2,2]\). The level-set restriction is inherited throughout. The notation \(F_T\) in this criterion is \(\lim N^{-1}\log P_N(T,1)\); it is not the normalized tilted pressure used in some earlier notes. The term \(-\tfrac12\log T\) is applied exactly once.

If the limiting upper bound is strictly below a specified complete action \(\Phi\), the monotonicity of the supremum as the polydisk shrinks gives a fixed positive radius and a strict large-\(N\) margin. This is an upper estimate for the selected source sector; it does not assert a nonzero lower asymptotic or identify a full filled invariant.

## 5. What the actual odd source majorant does prove

Now restrict to the actual odd source \(N=2m+1\ge3\). Write
\[
 a_r=4\cos^2((r+\tfrac12)\theta),\quad
 s_r=2\sin(r\theta),\quad \sigma=-2-u.
 \tag{A9}
\]
For \(0\le j\le m\), the original cleared lower cofactors satisfy
\[
 \begin{aligned}
 R_0(b;u)&=1,\\
 R_j(b;u)&=b^j\prod_{r<j}(a_r+u)
       +s_j^2(x+y)R_{j-1}(b;u)
       +s_js_{j-1}(a_{j-1}+u)xyR_{j-2}(b;u).
 \end{aligned}
 \tag{A10}
\]
The last term is absent at \(j=1\). All \(a_r\), \(r<m\), are positive. Each path contains a product of distinct unused-row factors \(a_r+u\). Thus every coefficient of \(R_j\) in its face variables and \(u\) is nonnegative. Set \(G_b=R_m(b;u)\), \(D_b=R_{m-1}(b;u)\). The exact central numerator, with the original normalization, is
\[
 P_C(u)=G_b(u)G_c(u)+u s_m^2xyD_b(u)D_c(u).
 \tag{A11}
\]
This is equations (2)--(5) of `actual_cross_cofactor_factorization.md`. In particular no skipping-row normal has been discarded. At odd levels \((-1)^d=1\); all original \(N\)-dependent scalar factors remain in these cofactors.

For \(v\ge0\), define
\[
 K_N(v)=\prod_{r=0}^{m-1}\left(1+\frac{v}{a_r}\right)
 =\frac{\sinh(N\alpha)}{N\sinh\alpha},
 \qquad \alpha=\operatorname{arsinh}(\sqrt v/2).
 \tag{A12}
\]
The value at zero is understood by continuity. The product identity follows by pairing the roots in the elementary factorization of \(\sinh(N\alpha)/\sinh\alpha\): the unordered \(a_r\) equal \(4\sin^2(k\pi/N)\), \(1\le k\le m\), and their product is \(N\). Each individual unused-row subset has ratio at most \(K_N(v)\). Therefore, coefficientwise in the original faces,
\[
 G_b(v)\le K_N(v)G_b(0),\qquad
 D_b(v)\le K_N(v)D_b(0).
 \tag{A13}
\]
Moreover (A10) gives \(G_b(0)\ge s_m^2(x+y)D_b(0)\), whence
\[
 G_b(0)G_c(0)\ge2s_m^4xyD_b(0)D_c(0).
 \tag{A14}
\]
Combining these inequalities retains the second term in (A11):
\[
 \begin{split}
 P_C(v)&\le_{\mathrm{coef}}
       \left(1+\frac{v}{2s_m^2}\right)K_N(v)^2P_C(0)\\
 &\le_{\mathrm{coef}}(1+v/6)e^{N\sqrt v}P_C(0).
 \end{split}
 \tag{A15}
\]
Indeed \(s_m^2\ge3\), and the finite geometric sum for \(\sinh(N\alpha)/\sinh\alpha\) gives \(K_N(v)\le e^{(N-1)\alpha}\), while \(2\alpha\le\sqrt v\). The coefficientwise bound is already preserved in the odd-neighbor handoff; the use here is its exact consequence for the proposed mass hypothesis.

Take a fixed number \(L\) of original central coupons, with their original identifications, protected zero targets, and the one shared face coefficient extraction leaving a binary exterior of degree \(d\). Keep all other exterior coupons at the positive endpoint. These operations preserve coefficientwise nonnegativity. Consequently
\[
 \widetilde P_N(\boldsymbol u;A,C)
   =\sum_\beta B_{N,\beta}(A,C)\boldsymbol u^\beta,
 \qquad B_{N,\beta}\ge_{\mathrm{coef}}0,
 \qquad B_{N,0}=P_N.
 \tag{A16}
\]
For a nonzero endpoint exterior,
\[
 \begin{split}
 E_N(v)
 &:=\frac{\sum_\beta v^{|\beta|}B_{N,\beta}(1,1)}{P_N(1,1)}
 =\frac{\widetilde P_N(v,\ldots,v;1,1)}{P_N(1,1)}\\
 &\le(1+v/6)^L e^{LN\sqrt v},
 \qquad
 \limsup_{N\to\infty,\ N\ \mathrm{odd}}\frac{\log E_N(v)}N
       \le L\sqrt v.
 \end{split}
 \tag{A17}
\]
Any fixed endpoint scalar common to numerator and denominator cancels; none is removed from the original source before extraction. The evaluation at positive \(u=v\) is an algebraic majorant outside the physical interval. It is not a claim about a filled representation there. Nonnegative Taylor coefficients also majorize every complex \(|u_e|\le v\).

## 6. Why this is not yet the signed stable mass

Suppose a proposed stable expansion has, for each Taylor multiindex,
\[
 B_{N,\beta}=\sum_{\alpha:\,\beta_\alpha=\beta}c_{N,\alpha}Q_{N,\alpha}.
 \tag{A18}
\]
Taking the value at \((1,1)\) and using the triangle inequality gives
\[
 E_N(v)\le W_N(v).
 \tag{A19}
\]
This direction cannot turn the upper bound (A17) into an upper bound for \(W_N\). If all the coefficients in (A18) are nonnegative, equality holds and (A17) supplies the mass assumption with \(\omega(v)=L\sqrt v\). An exact construction must still supply the root-count/order condition for those same pieces.

There is always a positive stable decomposition of each \(B_{N,\beta}\) into its binary monomials, keeping \(B_{N,0}=P_N\) as one endpoint term. It gives exactly \(W_N=E_N\), but its rank cost need not be bounded by the spectral order. This failure can already be seen in the original local source, with no invented Taylor polynomial. Identify its faces by \(x=y=A\), \(b=c=C\). At the endpoint,
\[
 P_C(0;A,C)=N^2\det(CI+A J_m)^2,
 \qquad J_m=(H_-+H_+)/2>0.
 \tag{A20}
\]
Every normalized root parameter is strictly between zero and one. By (A10), the coefficient of \(b^m\) in \(G_b(u)\) is \(A_m(u)=\prod_{r<m}(a_r+u)\), and \(A_m(0)=N\). Hence
\[
 [u]\,P_C(u;A,C)
 =2N^2\left(\sum_{r<m}\frac1{a_r}\right)C^{2m}
       +\text{terms divisible by }A.
 \tag{A21}
\]
The skipping term has a factor \(A^2\) and does not alter this coefficient. The monomial piece \(C^{2m}\) has all \(d=2m\) root parameters at zero. Its root-count distance from (A20) is therefore exactly \(d\), already at spectral order one. This proves that the straightforward positive monomial expansion does not satisfy a fixed \(J\). It is a local source test of that construction, not a claim that this monomial survives any specified global face extraction, and not a proof that another stable decomposition is impossible.

Conversely, root-count control alone cannot bound the absolute mass of an unspecified signed decomposition: adding the identically canceling pair \(e^{cN}uP_N-e^{cN}uP_N\) leaves the same original source and has root-count distance zero, but increases \(W_N(v)\) by \(2ve^{cN}\). This elementary observation only clarifies why the mass is a property of a chosen construction, not an invariant of its summed polynomial.

The remaining source problem is consequently precise: construct stable pieces satisfying the root-count/order bound and a mass estimate simultaneously, after the same original shared extraction. The endpoint coefficientwise bounds, the local nonstability result, and the present audit neither supply nor rule out that construction.
