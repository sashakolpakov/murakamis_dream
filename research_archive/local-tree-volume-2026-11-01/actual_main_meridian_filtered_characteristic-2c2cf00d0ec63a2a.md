# A classical characteristic selected by the microscopic meridian state

The reduced ADO invariant is a function of a marked meridian eigenvalue \(M\). Its exact quantum recurrence compares the values at \(M,qM,q^2M,\ldots\). We prove that, for the knot classes specified below, the complete asymptotic expansion on the scale \(M=q_N^s\) selects one analytic curve in the classical symbol of every such recurrence. The curve is determined by the actual finite invariant and its original normalization.

The selected curve passes through \((M,L)=(1,-1)\), has the preferred cusp shape as its logarithmic tangent, and is invariant under \((M,L)\mapsto(M^{-1},L^{-1})\). We also give a rational formula for its longitude coordinate in the original internal variables. These conclusions do not yet identify the entire curve with the geometric component of the knot's classical A-polynomial. Section 7 states the remaining comparison with the actual nonparabolic representation equations.

Fix a knot admitting one of the following presentations, with its original endpoint orders, orientations and peripheral markings:

* a strict ordered Conway presentation with independently long fixed filling powers, under the hypotheses of the [filled-meridian theorem](actual_main_meridian_filled_volume.md);
* an ordered all-circle tree satisfying the [summed degree-and-twist criterion](actual_all_circle_quantitative_volume.md), \(\sum_v d_v/(d_v^2+n_v^2)\le2^{-25}\);
* an ordered all-circle tree satisfying the [local degree-and-twist criterion](actual_all_circle_local_message_volume.md), \(\max_v d_v/(d_v^2+n_v^2)\le2^{-120}\).

In the last two cases \(d_v\) is the number of edges incident to vertex \(v\), and \(n_v\) is its signed integer crossing power. The construction must give one knot, with no additional component closed inside a tangle. The diagram, powers and compact parameter sets are fixed before the level tends to infinity. Both level parities are retained.

Those theorems supply an actual finite-sum representation with a nonzero, nondegenerate joint first Fourier contribution and fixed exponential bounds for all discarded terms. The proof here extends that representation to the finitely many translated microscopic regions needed by an arbitrary fixed-order recurrence, then uses every order of its canonical factorial expansion. A leading volume limit or a finite cusp jet alone would not suffice.

## 1. Exact finite inputs and the new issue

Write
\[
 q_N=e^{\pi i/N},\qquad M=q_N^s,\qquad
 F_N(1)=K_N,\qquad
 H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)}.
 \tag{1}
\]
Here \(F_N\) is the actual zero-framed reduced ADO state in the marked coordinate \(M=-qx\), where \(x\) is the raw highest-weight parameter. The [normalization and pointing](kashaev_ado_pointing.md) fix \(K_N=F_N(1)\), the Kashaev value. The full modified-trace state is \(d_N(M)F_N(M)\), with
\[
 d_N(M)=\eta_N\frac{M-M^{-1}}{M^N-M^{-N}},\qquad
 d_N(1)=\frac{\eta_N}{N}.
 \tag{2}
\]
Here \(\eta_N=i^{N+3}\) in the fixed normalization. All these factors remain in the argument.

The finite-source theorem, with the [exact scalar calculation](actual_main_meridian_exact_scalar.md), gives a local integral or finite-contour expression whose main-parameter dependence, after the exponentially smaller errors have been removed, is exactly
\[
 A_N(s)\prod_{e\in E}\mathcal I_N(x_e,s),\qquad
 A_N(s)=\exp\!\left(\frac{\pi i\,a(D)s^2}{2N}\right),
 \quad a(D)=-w(D)-\sum_v n_v,
 \tag{3}
\]
\[
 \mathcal I_N(x,s)=
 \frac{G_N(Nx)^2}{G_N(Nx-s)G_N(Nx+s)}.
 \tag{4}
\]
The integer \(w(D)\) is the oriented writhe of the original filled diagram, and \(n_v\) are its original signed crossing powers. The variables \(x_e\) are the normalized Newton indices on its physical quarter-turn edges. They are internal summation variables, distinct from the raw color \(x\) in \(M=-qx\). The single reduced-cut factor \(H_N(s)\) is outside this expression. The base phase and its exact interpolation do not depend on \(s\). Hidden edges introduced solely to resolve a product into binary multiplications are not added to (3).

The function \(G_N\) is the fixed interpolation of the sine factorial, not an arbitrary solution of its difference equation:
\[
 G_N(z)=\left(\frac{2\pi}{N}\right)^z\Gamma(z+1)
 \prod_{k\ge1}
 \frac{\Gamma(Nk+z+1)}
      {\Gamma(Nk-z)(Nk)^{2z+1}},\qquad -1<\Re z<N.
 \tag{4a}
\]
Positive-base powers have their real logarithms. The [exact interpolation theorem](exact_factorial_interpolation_and_complex_contours.md), Sections 1--2, proves local convergence, nonvanishing, \(G_N(0)=1\), and
\(G_N(z+1)/G_N(z)=2\sin(\pi(z+1)/N)\). Its exact reflection identity fixes every endpoint normalization.

Equations (3)--(4) are the [grouped-wire identities](actual_main_meridian_grouped_wire_packet.md), (25)--(27), (34a)--(36), together with the scalar theorem. The [general component comparison](actual_main_meridian_general_component_comparison.md) supplies the discarded-source error on a fixed strict tree. The [joint filling transform](actual_main_meridian_joint_filling_transform.md) supplies the nonzero first joint charge and its fixed gap. For the quantitative all-circle classes, the [summed estimate](actual_all_circle_curvature_filling_limit.md) or the [local tree recursion](actual_all_circle_local_message_volume.md) supplies the corresponding contour and nonzero-source bounds. The exact edge insertion is the same in all cases.

The published profile on \(|s|<1\) alone is not enough to insert an arbitrary order-\(d\) operator: its equation uses \(s,s+1,\ldots,s+d\). Section 2 addresses those charts from the exact source. No principle of analytic continuation of an asymptotic expansion is substituted for that argument.

## 2. Fixed translated charts away from the resonances

Let \(K\) be a compact subset of the open upper half-plane. It may have arbitrarily large but fixed real extent. Actual orientation types use the moving parameters \(s\) or \(-s\), or the constant parameter zero. The moving compacts \(K\cup(-K)\) avoid every real integer and half-integer collision. The constant type keeps its original derivative data at the repeated nodes. The following checks extend the actual source bounds to \(K\), with constants depending on \(K\). They do not extend a uniform theorem across an ordinary resonance.

First, the crossing interpolation in the [source-bound theorem](actual_main_meridian_source_bounds.md), equation (D14), is the exact rational expression
\[
 r_{N,s}^{[n]}(z)=
 -\frac1{N(U-U^{-1})}
 \sum_{j=0}^{N-1}\lambda_j(s)^n(t_j-t_j^{-1})
              \frac{P_s(z)}{z-c_j(s)},\qquad U=e^{2\pi i s}.
 \tag{5}
\]
Here \(t_j=q_N^{-2j-1+2s}\), \(c_j=t_j+t_j^{-1}\), and \(P_s(z)=T_N(z)+2\cos(2\pi s)\), where \(T_0=2,T_1=z,T_{k+1}=zT_k-T_{k-1}\). The number \(\lambda_j(s)\) is the actual crossing eigenvalue at this node, with its full scalar. On \(K\), \(|U-U^{-1}|\) has a positive lower bound. The nodes remain in an ellipse of height \(O_K(N^{-1})\), and the same divided-difference estimates give a polynomial bound for the canonical polynomial, including its values and first derivatives at the repeated complete nodes. This holds for every fixed positive or negative crossing power. The common full crossing scalar and mixed-order reference factors are bounded on \(K\); their exact ratios are still retained. The removable-collision maximum principle used on the unit disk is unnecessary here.

Second, Euler's product writes
\[
 W_k(s)=\prod_{\substack{1\le r\le k\\j\in\mathbb Z}}
             \left(1-\frac{s^2}{(r+jN)^2}\right),
       \qquad 0\le k<N.
 \tag{6}
\]
The indicated integers are distinct and nonzero. For \(s\in K\), the product over the finitely many small integers stays uniformly away from zero. The product of \(\min(1,|1-s^2/m^2|)\) over the remaining integers is bounded below by a positive constant, because its logarithmic tail is bounded by \(C_K\sum m^{-2}\). The corresponding product of maxima gives an upper bound. Every subset in (6) therefore has uniform upper and inverse bounds. The same is true of \(H_N(s)\), which converges uniformly to the nonzero function \(\sin(\pi s)/(\pi s)\) on \(K\).

Third, the complete-basis Newton envelopes and Hermite interpolation bounds do not involve \(s\). Chebyshev folding depends only on the bounded number \(\cos(2\pi s)\) and the fixed raw polynomial degree divided by \(N\). The all-parity whole-trace estimates and the [reflected high-index difference](actual_main_meridian_high_fourier_reflection.md) use finitely many polynomials \(U_{\ell-1}(\cos2\pi s)\) at each fixed-valence junction. Here \(U_\ell\) is the Chebyshev polynomial defined by \(U_0=1,U_1=2z,U_{\ell+1}=2zU_\ell-U_{\ell-1}\). Their bounds remain uniform on \(K\). The same complete geometric action and strict component gaps consequently give the grouped discarded-source estimates. This uses the whole trace comparison; it does not compare a separated additional coefficient with an old tensor.

The same point applies to the [regular bare trace](actual_main_meridian_regular_bare_trace.md): its first Fourier alias has coefficient one, and every higher alias has a strict regular-window frequency gap. Replacing the unit disk by \(K\) changes only the bounded coefficients of these finitely many aliases. Its comparison to the complete bare tensor remains exponentially accurate.

Finally, use the exact translated grids in the [direct crossing trace](actual_main_meridian_direct_crossing_trace.md), Sections 2--4. A bounded \(s\), regardless of its real part, changes their interval endpoints by \(O_K(N^{-1})\). Use translated single-grid rectangles, retaining their endpoint currents. If a common paired rectangle is used instead, it can include or exclude a bounded number of periodic copies near the endpoints; their residues must be restored explicitly. Every such residue has angular position \(\pm\pi+O_K(N^{-1})\), so the established endpoint estimate, with the other angular variables real, gives the same fixed exponential loss. This point matters because the chirp is not periodic.

In particular, for the only extension needed below, \(s\mapsto s+j\) with a fixed integer \(j\), the grid is shifted by exactly \(j\) spacings and the Casimir relation is unchanged. Reindex its central \(N-|j|\) entries and retain the at most \(|j|\) wrapped entries at each endpoint. Their nonperiodic chirp factors are explicit and bounded on the fixed parameter compact; the raw Newton factor supplies the endpoint gap. Thus the local comparison is proved by finite reindexing and its retained endpoint residues, not by treating the two unwrapped grids as identical. The exact paired-grid Fourier coefficients are
\[
 (-1)^{(N-1)(\ell-1)}U_{\ell-1}(\cos2\pi\sigma),
 \qquad \sigma=s,-s,0.
 \tag{7}
\]
For the moving types on \(K\), no division by a vanishing sine occurs. The constant type is the already proved full-normal limit. The coefficient bound
\[
 |U_{\ell-1}(\cos2\pi\sigma)|
       \le \ell e^{2\pi |\operatorname{Im}\sigma|(\ell-1)}
 \tag{8}
\]
is absorbed by the same \(e^{-N\ell y}\) tails for sufficiently large \(N\). The real-spectator telescoping and the common joint angular saddle are unchanged. Fixed-power discarded errors are bounded before these angular contours, as required by the grouped-source interface.

Thus the original nonzero first-charge packet and its exact scalars hold uniformly on \(K\), with the same action and fixed exponential gaps. For the local tree criterion the same checks apply at each normalized subtree; Section 4.1 gives its all-order induction. The threshold on the fixed filling powers, or the stated quantitative criterion, is unchanged; constants and starting levels may depend on \(K\). This extension is needed only on a finite union of small disks with positive imaginary part. It asserts no uniform result on a compact meeting a nonzero integer.

## 3. All-order canonical interpolation

The exact factorial product admits, on any fixed complex bulk compact, its expansion to every prescribed order:
\[
 \log G_N(Nx)=N J(x)+\tfrac12\log(2N\sin\pi x)
            +\sum_{j=1}^{L}N^{-j}b_j(x)+O_L(N^{-L-1}).
 \tag{9}
\]
The \(b_j\) are holomorphic and have the original logarithm marks; some of them vanish. The expansion and every fixed derivative are uniform on a smaller compact.

This follows by repeating Section 4 of the [exact factorial interpolation theorem](exact_factorial_interpolation_and_complex_contours.md) with the finite Stirling expansion to the desired order. Its remainder follows from the finite periodic-Bernoulli integral formula. On a fixed complex bulk compact, the arguments \(N(k+x)\) and \(N(k-x)\) stay in a common right-half-plane sector. Taking sufficiently many Stirling terms bounds the remainder in the \(k\)-th factor by \(C_LN^{-L-1}k^{-L-1}\), with the first finitely many factors treated in the same sector. For a low requested order one may first take more terms so that the tail is summable. Summation preserves the desired uniform order, and Cauchy's estimate supplies fixed derivatives. The leading function remains the fixed primitive
\[
 J'(x)=\log(2\sin\pi x),
 \tag{10}
\]
and the half-logarithm in (9) is fixed by the exact lattice normalization. No periodic interpolation factor is introduced.

Set \(\delta=N^{-1}\), \(t=\delta s\), and define
\[
 K(x,t)=2J(x)-J(x+t)-J(x-t).
 \tag{11}
\]
Using (9) in (4), formally to any specified order, gives
\[
 \log\mathcal I_N(x,s)=
  \delta^{-1}K(x,t)+B_0(x,t)
                  +\sum_{j\ge1}\delta^j B_j(x,t).
 \tag{12}
\]
Each \(B_j\) is holomorphic near \(t=0\), even in \(t\), and vanishes at \(t=0\). In particular the \(\log N\) terms cancel. Equation (12) means a formal two-parameter construction whose substitution \(t=\delta s\) agrees with the actual fixed-\(s\) asymptotic expansion. It is not an assertion of a physical fixed-\(t\) asymptotic theorem.

The complete bare factorials, the circle Newton factors and all Gaussian amplitudes have analogous all-order bulk expansions. Exact integer offsets remain in the calculation. If \(x=\ell(X)+\delta c\), then expansion of \(\delta^{-1}K(\ell+\delta c,t)\) contributes \(cK_x(\ell,t)\) to \(B_0\), and further holomorphic terms to the \(B_j\). It changes no term of the leading phase. The same observation retains the midpoint offsets from \(N-1\). The finite lattice currents and the other Fourier charges have a fixed exponential loss, so they do not contribute to any coefficient of these expansions.

## 4. The filtered action theorem

Let \(X\) collect the original retained wire variables and the joint angular variables. Write \(\Phi(X)\) for the original first-charge filled phase at \(s=0\). Its critical point \(X_0\) is nondegenerate and has the original normalization. Define the analytic phase family
\[
 \Phi_t(X)=\Phi(X)+\sum_{e\in E}K(x_e,t)
                         +\frac{\pi i\,a(D)}2t^2,
 \qquad
 S(t)=\Phi_t(X_*(t)),
 \tag{13}
\]
where \(X_*(t)\) is the analytic critical point through \(X_0\). The implicit-function theorem supplies it on a fixed neighborhood of zero. This is a local analytic definition; its use does not require taking \(s=Nt\) in the physical invariant.

Formal stationary phase with the all-order analytic amplitude of Section 3 gives
\[
 \log\frac{F_N(q_N^s)}{K_N H_N(s)}
 \sim N\{S(t)-S(0)\}
             +\sum_{j\ge0}N^{-j}\{C_j(t)-C_j(0)\},
 \qquad t=s/N.
 \tag{14}
\]
Here the \(C_j\) are holomorphic germs. The leading amplitude is nonzero, so its logarithm is fixed by the ratio at \(t=0\). Possible residue-class dependence of lower amplitudes can be treated separately; the phase \(S\) is the same. The original powers of \(N\) and the scalar independent of \(s\) cancel in the displayed ratio.

For an explicit justification, perform formal Gaussian expansion of the local phase \(\Phi_t\), uniformly for small \(t\). Every coefficient is a finite polynomial in derivatives of the phase and amplitude and in the inverse Hessian. These derivatives are holomorphic in \(t\), and the Hessian stays invertible. Substitute \(t=\delta s\), Taylor-expand the resulting analytic coefficient functions, and truncate at any chosen power of \(\delta\). The uniform contour remainder and the exponentially small discarded terms prove the same fixed-\(s\) asymptotic coefficient. This argument applies on the original disk and on the translated compacts of Section 2.

Consequently, writing the logarithm as
\[
 \log\frac{F_N(q_N^s)}{K_N H_N(s)}
       \sim\sum_{r\ge1}N^{-r}p_r(s),
 \tag{15}
\]
each \(p_r\) is a polynomial of degree at most \(r+1\). More precisely, its coefficient of \(s^{r+1}\) is exactly the coefficient of \(t^{r+1}\) in \(S(t)-S(0)\). Terms from the \(C_j\) have degree at most \(r\) and cannot contribute to this top diagonal. This proves the filtration, rather than inferring it from a few low-order coefficients.

The phase is even in \(t\). At its base critical point the first mixed derivatives in \(X,t\) vanish, so
\[
 S'(0)=0,\qquad
 S''(0)=-2\pi\sum_e\cot(\pi x_e^{\mathrm{fill}})
                                      +\pi i\,a(D)
        =\pi i\,\tau_K.
 \tag{16}
\]
The last equality uses the [preferred-cusp formula](actual_main_meridian_preferred_cusp.md), with its [all-circle continuation](actual_all_circle_preferred_cusp.md) in the two quantitative classes. Higher derivatives of \(S\) are fixed by (13), not by the cusp tangent alone.

### 4.1. All orders for the local tree criterion

The local criterion requires a separate justification: its initial relative \(O(N^{-1})\) theorem does not by itself supply all the coefficients above.

The [local recursion](actual_all_circle_local_message_volume.md), Sections 2--6, retains the exact full edge kernel and the exact polynomial passed from each subtree to its parent. Denote that polynomial by \(M_{v,N}(z)\), where \(z\) is the unevaluated parent angle. Its high-index estimate, real bound, finite-degree strip estimate and crossing-trace tail estimate depend exponentially only on the original complete kernel and the stated local criterion. On \(K\cup(-K)\), Section 2 changes only their prefactors. The constant orientation type retains its independent derivative limit. Thus the same fixed local exponential margins and nonzero conditional first charge remain available.

For any prescribed order \(L\), strengthen the induction to
\[
 \frac{M_{v,N}(z)}{M_{v,N}(0)}
 =e^{Nh_v(z)}\frac{\alpha_v(z)}{\alpha_v(0)}
 \left(1+\sum_{j=1}^{L}N^{-j}a_{v,j}(z,s)
                    +O_K(N^{-L-1})\right)
 \tag{16a}
\]
on a fixed smaller parent disk. Here \(h_v(0)=0\), the leading amplitude \(\alpha_v\) is nonzero, and the coefficients and remainder are holomorphic in the parent variable. The exact scalar \(M_{v,N}(0)\), independent of \(z\), is divided out; no convergence of this unnormalized subtree scalar is assumed.

For a terminal subtree, the all-order factorial expansion and finite translated first-charge contour prove (16a). Suppose it holds for the children of a vertex. Their finite product has an expansion to every prescribed relative order. Since its normalized leading amplitude has no zero, its logarithm with value zero at the parent origin has the same property. The exact logarithm differs from its truncation by \(O_K(N^{-L-1})\), with fixed derivatives on a smaller disk.

Evaluate the next trace using the exact child polynomials. The original conditional real and strip estimates continue to bound its tails and connecting contours. On the first-charge contour its leading phase has a nondegenerate Gaussian and its amplitude is nonzero. The absolute local Gaussian integral is bounded by a constant times its leading magnitude, uniformly on a smaller parent disk. A holomorphic relative remainder of order \(N^{-L-1}\) therefore stays of that order after integration. Any extra finite derivative orders are obtained by starting the child expansion at higher order. The nonminimal charges and endpoint errors remain exponentially smaller than this conditional first charge. This proves (16a) at the next vertex.

The tree is fixed and finite, so this induction proves every order without claiming constants uniform in the tree's size or depth. In particular it does not compare an early local discard with the accumulated action decrease over the entire tree.

To identify the phase, perform the same induction on the auxiliary local integrals formed with the exact bulk arguments \(N(x\pm t)\). Their stationary equations are the original wire and angular equations with \(\sum_eK(x_e,t)\) added. Eliminating a child is ordinary stationary elimination with the invertible block Hessian supplied by the local proof. The resulting Schur complements give the same joint critical branch \(X_*(t)\) in (13). Constants subtracted when normalizing a child are restored by its exact \(M_{v,N}(0)\), so no action is discarded.

The formal Gaussian coefficients also compose in this order. Gaussian integration with an invertible block Hessian is associative, and expansion to a fixed order involves only finitely many Gaussian moments. Repeated integration therefore gives the same coefficients as the joint local integral. At the root restore the original single cut factor and scalar (3). This proves (14)--(16) for the local criterion, with exactly the original physical edge set.

## 5. Exact operator compatibility on the shifted charts

Let
\[
 P(q,M,T)=\sum_{j=0}^{d}a_j(q,M)T^j,\qquad TM=qMT,
 \tag{17}
\]
be any specified nonzero actual all-level reduced-state annihilator. This means that the displayed fixed rational-coefficient operator annihilates the whole meridian function \(F_N(M)\) at every sufficiently large root level. Its existence is the separate [finite-sum annihilator theorem](finite_sum_annihilator.md), not a definition obtained by fitting the values in (1). Clear its fixed rational denominators and remove its common \(q-1\) valuation. Denote its first nonzero classical symbol by \(P_0(M,L)\). No geometric factor is appended.

The exact reduced/full ratio in (2) satisfies
\[
 \frac{d_N(q_N^jM)}{d_N(M)}
    =(-1)^j\frac{q_N^jM-q_N^{-j}M^{-1}}{M-M^{-1}}.
 \tag{18}
\]
Thus, with \(f(M)=M-M^{-1}\), the same normalized function on the left of (15) obeys the actual root equation obtained from
\[
 \widetilde P
  =\sum_{j=0}^{d}a_j(q,M)(-1)^j
                      \frac{f(M)}{f(q^jM)}T^j.
 \tag{19}
\]
This is a fixed rational Ore operator. It retains the meridian divisor and sign character. Multiplying it on the left by \(\prod_{j=1}^{d}f(q^jM)\) clears its additional denominators. Its first classical symbol is
\[
                  f(M)^d P_0(M,-L).
 \tag{20}
\]
The displayed meridian factor is recorded, not removed by a normalization convention.

Choose a small open disk \(D\) in the upper half-plane and put \(K=\bigcup_{j=0}^{d}(\overline D+j)\). Section 2 supplies the same all-order expansion at every argument in this exact equation. Division by the nonzero normalized state at \(s\in D\) and comparison of every asymptotic coefficient therefore gives its formal difference equation. All coefficient functions vanish on \(D\), hence identically as their polynomial or meromorphic functions of \(s\).

This is the required compatibility step. Exact ordinary-color values alone would not have supplied these shifted neighborhoods, and a formal expansion restricted to \(|s|<1\) would not have justified it for arbitrary operator order.

## 6. Diagonal extraction forces a classical characteristic germ

Now write \(h=\log q\), \(u=\log M\), so \(u=hs\), and put
\[
 \mathcal S(u)=\pi i\{S(u/(\pi i))-S(0)\}.
 \tag{21}
\]
The degree filtration in Section 4 regrades the formal logarithm uniquely as
\[
             h^{-1}\mathcal S(u)+\sum_{j\ge0}h^j A_j(u).
 \tag{22}
\]
Indeed a monomial \(h^rs^k\) becomes \(h^{r-k}u^k\), and \(k\le r+1\) permits only the single negative power \(h^{-1}\). For each exponent of \(h\), its coefficient is a formal series in \(u\).

Under the \(j\)-fold shift \(s\mapsto s+j\), the ratio of these formal periods belongs to \(\mathbb C[[h,u]]\), with constant \(h\)-coefficient
\[
                           e^{j\mathcal S'(u)}.
 \tag{23}
\]
The \(h^{-1}\) cancels in the finite difference \(\mathcal S(u+jh)-\mathcal S(u)\). All the \(A_j\) contribute zero to the constant coefficient of that difference.

The substitution \(\mathbb C[[h,u]]\to\mathbb C[s][[h]]\), \(u\mapsto hs\), is injective: distinct monomials \(h^au^b\) yield the distinct monomials \(h^{a+b}s^b\). Consequently the formal compatibility from Section 5 is an identity before this substitution. Taking its constant \(h\)-coefficient and using (20) gives
\[
 f(e^u)^d\,P_0(e^u,-e^{\mathcal S'(u)})=0.
 \tag{24}
\]
The first factor is a nonzero formal series. The formal series ring is a domain, so
\[
                  P_0(e^u,-e^{\mathcal S'(u)})=0.
 \tag{25}
\]
This deduction retains the factor in the operator and cancels it only in a domain identity. It does not silently discard a peripheral component.

The analytic germ
\[
                    M=e^u,\qquad L=-e^{\mathcal S'(u)}
 \tag{26}
\]
therefore lies on the first nonzero classical symbol of every actual all-level annihilator. Its \(M\) coordinate is nonconstant, so the kernel of the map from the Laurent polynomial ring in \(M,L\) to this analytic germ is a height-one prime. It is generated by an irreducible Laurent polynomial, and that polynomial divides every such \(P_0\). The marked reduced sign is \(L(0)=-1\), and
\[
             \left.\frac{d\log(-L)}{du}\right|_{u=0}
                 =\mathcal S''(0)=\tau_K.
 \tag{27}
\]
This is an actual source-selected characteristic, derived from the given operator and its selected microscopic family. A nonminimal left multiple does not create a choice in (26): the phase was fixed by the physical source, and (25) also applies to a minimal annihilator if one is specified.

### 6.1. Reciprocity of the selected factor

Evenness of the phase in (13) and uniqueness of its critical point imply \(S(-t)=S(t)\). Hence \(\mathcal S\) is even and \(\mathcal S'\) is odd. Formula (26) gives the exact germ identity
\[
 L_{\mathrm{eff}}(M^{-1})
                    =L_{\mathrm{eff}}(M)^{-1}.
 \tag{27a}
\]
The minus sign is consistent on both sides: the inverse of \(-e^{\mathcal S'(u)}\) is \(-e^{-\mathcal S'(u)}\).

Let \(Q_{\mathrm{sel}}(M,L)\) generate the height-one prime of this germ. Inversion preserves that prime by (27a). The Laurent polynomial ring is a unique factorization domain, so its two irreducible generators are associates:
\[
 Q_{\mathrm{sel}}(M^{-1},L^{-1})
        =cM^\alpha L^\beta Q_{\mathrm{sel}}(M,L),
 \quad c\in\mathbb C^\times,\quad \alpha,\beta\in\mathbb Z.
 \tag{27b}
\]
This is reciprocity of the irreducible factor selected by the actual state. It does not identify it with a geometric factor by imposing reciprocity as an extra condition.

## 7. Exact remaining geometric identification and limitations

Equations (13), (21), and (26) construct a complete analytic germ, not just its first cusp jet. The proof above does not yet establish that this germ is the marked preferred-longitude eigenvalue of a nonparabolic representation of the filled knot group. The published Conway face family keeps the main cusp parabolic; its preferred-cusp calculation proves (16), not that additional nonparabolic identification.

### 7.1. A finite rational peripheral map for the new action

There is a concrete algebraic form of the proposed comparison. Retain the original logarithm of each sine near the selected filled wire, and put
\[
 E_e=e^{2\pi i x_e},\qquad M=e^{\pi i t}.
 \tag{28}
\]
Every filled wire lies in its original regular complex chart. Thus the sines in (11) are nonzero for sufficiently small \(t\), with their logarithms fixed by continuation from \(t=0\). Direct differentiation gives
\[
 \begin{aligned}
 K_x(x,t)
 &=\log\frac{\sin^2(\pi x)}
                 {\sin(\pi(x+t))\sin(\pi(x-t))},\\
 K_t(x,t)
 &=\log\frac{\sin(\pi(x-t))}{\sin(\pi(x+t))}.
 \end{aligned}
 \tag{29}
\]
Both logarithms vanish at \(t=0\). The elementary exponential formula for sine now yields the exact identities
\[
 \exp K_x=
 \frac{(1-E)^2}{(1-EM^2)(1-E/M^2)},\qquad
 \exp K_t=\frac{M^2-E}{1-M^2E}.
 \tag{30}
\]
For the second identity, for example, the factors \(e^{-\pi i(x-t)}\) and \(e^{-\pi i(x+t)}\) contribute \(M^2\), which gives
\[
 M^2\frac{E/M^2-1}{EM^2-1}
                =\frac{M^2-E}{1-M^2E}.
\]
This calculation fixes the factors and the sign without taking an unmarked square root of a shape monomial. Although a ratio in (30) might have other logarithms away from the chosen chart, its logarithm here is exactly the one in (29), since both vanish at \(t=0\).

In coordinates where the physical edge \(x_e\) is an independent primitive wire, its old logarithmic critical equation is therefore changed by adding \(K_x(x_e,t)\); its exponentiated equation is multiplied by the first ratio in (30). Hidden resolution wires receive no such term. In another integral primitive coordinate system the chain rule gives the product of these ratios to the corresponding signed incidence powers. Angular critical equations receive no direct insertion, because the added \(K\) terms depend only on their edge wires. They still change indirectly through the coupled solution \(X_*(t)\). The original flattening integers and the original finite cover used for the exponential coordinates remain fixed.

The derivative of a critical value has no derivative-of-critical-point term. Equations (13), (21), and (29) thus imply
\[
 \begin{aligned}
 S'(t)
   &=\pi i\,a(D)t+\sum_e K_t(x_e(t),t),\\
 L_{\mathrm{eff}}(M)
   &=-M^{a(D)}
       \prod_{e\in E}\frac{M^2-E_e(M)}{1-M^2E_e(M)}.
 \end{aligned}
 \tag{31}
\]
This is exactly the characteristic in (26), with the marked reduced-state sign retained. It is a finite rational peripheral expression on the modified critical scheme, not an expression inferred from a cusp approximation. All its denominators are units at the selected filled point. In particular \(L_{\mathrm{eff}}(1)=-1\).

The inserted phase is even in \(t\), so uniqueness of the critical point gives \(X_*(t)=X_*(-t)\). Consequently the derivatives of the \(E_e\) contribute nothing to the first derivative of (31) at \(M=1\). With \(u=\log M\),
\[
 \left.\frac{d}{du}
 \log\frac{e^{2u}-E_e(u)}{1-e^{2u}E_e(u)}
 \right|_{u=0}
   =2\frac{1+E_e(0)}{1-E_e(0)}
   =2i\cot(\pi x_e^{\mathrm{fill}}).
 \tag{32}
\]
Equation (32) recovers \(a(D)+2i\sum_e\cot(\pi x_e^{\mathrm{fill}})=\tau_K\), and also checks the orientation of the candidate longitude. Every higher derivative is specified by the coupled modified equations and (31); none is supplied by this first-derivative check.

### 7.2. Explicit equations for an all-circle tree

For the all-circle construction, there are no bare product vertices to resolve, so the modified critical equations have a particularly short finite form. Let \(e=vw\) be an original tree edge, with wire \(x_e\), and let \(\tau_v\) be the angular variable of the crossing trace at vertex \(v\). Define
\[
 \begin{aligned}
 b(x,\tau)
   &=\int_0^x\log(2\cos(2\pi r)+2\cos\tau)\,dr-2J(x),\\
 E_e&=e^{2\pi i x_e},\qquad Q_v=e^{i\tau_v}.
 \end{aligned}
 \tag{33}
\]
The logarithm is initially the real one for \(0<x<1/2\), \(\tau=0\), and is continued on the selected regular chart. This is exactly the circle-incidence action from the [grouped packet](actual_main_meridian_grouped_wire_packet.md), (23)--(24), and the [all-circle edge calculation](actual_all_circle_curvature_filling_limit.md), Section 4.

Up to a fixed additive constant independent of \(t\), the first-charge phase before stationary elimination is
\[
 \Phi_t(\mathbf x,\boldsymbol\tau)=
 \sum_{e=vw}\bigl[b(x_e,\tau_v)+b(x_e,\tau_w)+K(x_e,t)\bigr]
 +\sum_v\left(\frac{i n_v\tau_v^2}{4\pi}-i\tau_v\right)
 +\frac{\pi i\,a(D)}2t^2.
 \tag{34}
\]
The linear term \(-i\tau_v\) is the retained first Fourier charge. It must remain when selecting the logarithmic branch, although it will disappear from the exponentiated equations.

Differentiating (33) first in \(x\) gives
\[
 \exp b_x
 =\frac{2\cos(2\pi x)+2\cos\tau}{4\sin^2(\pi x)}
 =-\frac{(E+Q)(E+Q^{-1})}{(E-1)^2}.
 \tag{35}
\]
For the angular derivative, the change of variable \(y=\tan(\pi r)\) gives
\[
 b_\tau=-\frac1\pi
  \operatorname{artanh}\!\left(\tan(\tau/2)\tan(\pi x)\right),
 \qquad
 \exp(-2\pi b_\tau)=\frac{Q+E}{1+QE}.
 \tag{36}
\]
The branch of \(\operatorname{artanh}\) is zero at \(\tau=0\). To verify the second identity without a sign choice, substitute
\(\tan(\tau/2)=-i(Q-1)/(Q+1)\) and
\(\tan(\pi x)=-i(E-1)/(E+1)\) into
\(\exp(2\operatorname{artanh}z)=(1+z)/(1-z)\).

The wire equation is \(b_x(x_e,\tau_v)+b_x(x_e,\tau_w)+K_x(x_e,t)=0\). The two minus signs in (35) cancel. Using (30) therefore gives
\[
 \begin{aligned}
 &(E_e+Q_v)(E_e+Q_v^{-1})
   (E_e+Q_w)(E_e+Q_w^{-1})\\
 &\quad=(E_e-1)^2(1-E_eM^2)(1-E_e/M^2).
 \end{aligned}
 \tag{37}
\]
The edge equation is linear in the trace of its internal variable.
Put
\[
 Z_e=E_e+E_e^{-1},\qquad B_v=Q_v+Q_v^{-1},\qquad
 D_M=M^2+M^{-2}.
 \tag{37a}
\]
Dividing (37) by \(E_e^2\) gives
\[
 (Z_e+B_v)(Z_e+B_w)=(Z_e-2)(Z_e-D_M).
\]
The quadratic terms cancel, leaving
\[
 Z_e=\frac{2D_M-B_vB_w}{B_v+B_w+D_M+2}.
 \tag{37b}
\]
The denominator is eight at the complete point and remains nonzero
on the selected small-filling chart. The equation
\(E_e^2-Z_eE_e+1=0\), with its chosen branch through \(E_e=i\)
at completeness, recovers the original edge variable. This determines the internal variable by a quadratic equation
with its original branch retained.

The angular equation, with its first-charge mark, is
\[
 \sum_{e\ni v}b_\tau(x_e,\tau_v)
          +\frac{i n_v\tau_v}{2\pi}-i=0.
 \tag{38}
\]
Multiplication by \(-2\pi\) and exponentiation give
\[
 \prod_{e\ni v}\frac{Q_v+E_e}{1+Q_vE_e}=Q_v^{n_v}.
 \tag{39}
\]
In obtaining (39), the additive term \(-2\pi i\) has exponent one. Equation (38), rather than (39) alone, retains which Fourier charge was used.

Equations (37), (39), and the longitude expression (31) are a finite rational system with parameter \(M\). Work on the original chart where their denominators are units, or equivalently clear denominators and saturate by those factors before taking the selected germ. The nondegenerate critical point and the continued logarithms choose one analytic solution through the original filled point. Exponentiation has other branches and cannot replace that choice. Eliminating the \(E_e,Q_v\) on this chosen germ gives the same \(L_{\mathrm{eff}}\) as (26), not a separately normalized polynomial curve.

This explicit system is a concrete target for a main-meridian geometric construction: one would need actual marked nonparabolic edge blocks satisfying these equations and carrying (31) as their preferred longitude. The equations alone do not assert that such blocks have already been constructed.

### 7.3. What the existing geometric inputs actually provide

The [marked Conway deformation](actual_conway_general_mask_marked_filling.md), Section 3, has a leaf function
\[
 g(x,t)=J(2x)-2J(x)-J(x-t)-J(x+t),
 \qquad K(x,t)=g(x,t)-g(x,0).
 \tag{40}
\]
That equality of scalar functions does not identify their peripheral uses. In the existing leaf construction \(t\) is the hidden auxiliary-circle parameter. Section 5 of that note proves that every actual main meridian remains parabolic identically: the two adjacent white maps have the same derivative at their common corner. The [primitive collar calculation](actual_deformed_circle_primitive_collar.md) likewise identifies an auxiliary meridian and disk longitude. The preferred-cusp theorem computes a translation in their parabolic main peripheral commutant. None of these statements gives a main meridian with eigenvalue \(e^{\pi it}\) simply by substituting this \(t\) into its existing cells.

The original marked braid source supplies a different nonparabolic construction. The [critical-correspondence theorem](marked_braid_holonomy.md), Sections 4--6, identifies its regular exponential critical scheme with framed knot representations with actual meridian eigenvalue \(M\). The [longitude-insertion theorem](quantum_longitude_and_regulator_action.md), Sections 1--4, identifies its preferred longitude, full meridian gauge, and logarithmic action differential. The [actual geometric normal-period theorem](actual_geometric_normal_period.md), Sections 3--5, constructs the local geometric formal block of that braid scheme. Those results do not yet identify the grouped modified equations (30) with that particular critical block.

A sufficient next step is an exact classical adapter: identify the stationary equations of (13), with \(t=u/(\pi i)\), with the original regular geometric critical scheme of the full marked braid source, retaining its cut flag, framing and preferred longitude insertion. The existing marked braid holonomy theorem identifies that latter scheme with framed knot representations and supplies its rational inverse. An identification of these equations on the complete geometric germ would therefore identify (26) with the geometric eigenvalue germ and prove the desired geometric factor by (25). Agreement of their tangent alone is not sufficient.

The argument also does not claim a physical asymptotic formula for fixed \(M\ne1\), or for \(s\) growing with \(N\). The variable \(t\) in Section 4 is an auxiliary analytic parameter used to organize all fixed-\(s\) coefficients. The ordinary-color divisors remain in (2), (18)–(20). The translated charts in Section 2 stay away from those divisors; no uniform nonvanishing state across ordinary-color resonances has been asserted.

The curve selected here is therefore a proved classical characteristic of the actual annihilator, with its reciprocal symmetry, explicit peripheral expression and geometric cusp tangent. Its identification with the entire classical geometric eigenvalue germ is the remaining statement.
