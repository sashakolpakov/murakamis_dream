# All orders of the meridian profile under the directed criterion

The directed degree-and-twist criterion gives more than a leading volume limit. For every fixed knot presentation satisfying that criterion, the actual meridian state has an asymptotic expansion to every finite order on the microscopic scale \(M=q_N^s\). Its coefficients have a precise polynomial degree bound. This bound allows an exact quantum recurrence to select the preferred geometric meridian–longitude curve of the original knot complement.

The proof expands the actual normalized subtree integrals, retaining their full normal data and endpoint terms. It also works on the fixed translated parameter regions used by the recurrence. These are separate estimates from the previously established first-order profile.

The extension has an operator consequence. For every knot satisfying the directed certificate, the first nonzero classical symbol of every genuine fixed all-level reduced ADO annihilator contains the selected complex geometric meridian–longitude factor. The statement is about that factor, not the full A-polynomial, its multiplicity, or the entire operator ideal.

## 1. Fixed data and statement

Fix one literal ordered all-circle tree with at least one edge, the original endpoint and orientation types, and its fixed signed powers \(n_v\). Its cylindrical closure is required to be one knot, with no component already closed inside a tangle. Fix a root and numbers \(0<c_v<2^{-16}\) at nonroot vertices satisfying equations (3), (8), and (9) of [the directed theorem](actual_all_circle_directed_volume.md). All this data is independent of the level. There is no new smallness condition on these data in this note.

In particular the result covers the sufficient alternative
\[
 d_v\ge 2^{28}\quad\text{or}\quad |n_v|\ge2^{27}
 \quad\text{separately at every vertex},
 \tag{1}
\]
and also the certificates allowed by the more general directed inequalities. The original knot and parity qualifications are unchanged. Both level parities are included.

Use the actual zero-framed reduced state and its pointing:
\[
 q_N=e^{\pi i/N},\qquad M=-q_Nx=q_N^s,\qquad
 K_N=F_N(1),\qquad
 H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)}.
 \tag{2}
\]
Here \(x\) is the raw highest-weight parameter; internal wire variables will instead be denoted \(x_e\). Define the normalized full state
\[
 \mathcal Z_N(s)=\frac{F_N(q_N^s)}{K_NH_N(s)}.
 \tag{3}
\]
The directed theorem gives \(K_N\ne0\) for every sufficiently large level. The one factor \(H_N\) is exactly the conversion between the reduced and full trace, not a freely chosen regularization.

**All-order statement.** Let \(K\) be any compact subset of the open upper half-plane. It can have any fixed real extent and can be a finite union of compact disks. For every finite \(L\),
\[
 \log\mathcal Z_N(s)
   =\sum_{r=1}^{L}N^{-r}p_r(s)+O_{K,L}(N^{-L-1}),
 \qquad \deg p_r\le r+1,
 \tag{4}
\]
uniformly on \(K\), with every prescribed finite number of derivatives on smaller compacts. The same polynomials occur on each original compact \(|s|\le R<1\). If a lower amplitude requires separating the two level parities, (4) is understood on each parity subsequence; its top diagonal is identical for both. The logarithm is the branch tending to zero, which is well defined for all sufficiently large levels on each such compact.

The polynomials are selected by the original joint phase, including its first-charge mark. Put
\[
 \begin{aligned}
 J'(x)&=\log(2\sin\pi x),\qquad J(0)=0,\\
 \mathcal K(x,t)&=2J(x)-J(x+t)-J(x-t),\\
 \Phi_t(X)&=\Phi(X)+\sum_{e\in\mathcal E_T}\mathcal K(x_e,t)
                         +\frac{\pi i\,a(D)}2t^2,\\
 a(D)&=-w(D)-\sum_v n_v,\qquad
 S(t)=\Phi_t(X_*(t)).
 \end{aligned}
 \tag{5}
\]
The set \(\mathcal E_T\) is the set of original physical quarter-turn edges, \(X\) comprises their wire variables and the original circle angles, and \(X_*(t)\) is the critical point continued from the selected filled point at \(t=0\). The base phase is
\[
 \Phi(X)=\sum_{e=vw}\{b(x_e,\tau_v)+b(x_e,\tau_w)\}
       +\frac{i}{4\pi}\sum_v n_v\tau_v^2-i\sum_v\tau_v,
 \tag{6}
\]
with the logarithms fixed by the original complete chart and first-charge continuation. The top coefficient of \(p_r\) is precisely the coefficient of \(t^{r+1}\) in \(S(t)-S(0)\). The last term in (6) must not be omitted.

All constants and starting levels may depend on the fixed tree, signed powers, certificate, compact, derivative order and expansion order. This dependence does not change the finite directed certificate. No uniformity over an unbounded collection of diagrams is asserted.

## 2. The strict margins that the higher-order proof uses

Retain the notation \(a_v,b_v,D_v,A_v,B_v,C_v,y_v,\beta_v,\eta_v\) of directed equations (4)–(7). Its proof supplies the following facts about the actual finite recurrence.

The full edge kernel, including high indices, is
\[
 \mathscr K_N(t,u;s)=\sum_{k=0}^{N-1}
 e_k(-2\cos t)e_k(-2\cos u)\frac{H_N(s)}{W_k(s)}.
 \tag{7}
\]
It has exact trigonometric degree at most \(N-1\) in either angle. There is no discarded term in this definition.

At a nonroot vertex the actual message is the full physical trace of the parent kernel times the child messages, with its original edge scalar. At the root the parent kernel is absent. This is directed (25)–(26), an ordering of a finite contraction, not a new topological rerooting.

The conditional first-charge saddle is nondegenerate on the parent rectangle. The local exponent has second derivative with real part at most \(-(19/20)a_v\), and its complex second derivative has modulus at least \((19/20)|D_v|\). Its physical sine amplitude is nonzero.

Relative to the conditional first charge, all original tail, endpoint, truncation and connector errors have a positive margin at least \(\eta_v-\beta_v>0\). Every retained charge \(\ell\ge2\) has the additional margin
\[
 \frac{190}{441}\frac{a_v}{|D_v|^2}(\ell^2-1)>0.
 \tag{8}
\]
The first Fourier coefficient is exactly one, at both parities.

The outgoing real-envelope regeneration has the strictly positive margin \((2^{-16}-c_v)\chi-\beta_v\) whenever an outgoing edge exists. There is no such requirement at the root.

Here the complete basis is \(e_k(z)=S_k^{-2}\prod_{j<k}(c_j-z)\), with \(S_k=\prod_{r=1}^{k}2\sin(\pi r/N)\), \(c_j=2\cos((2j+1)\pi/N)\), and \(0\le k<N\). The paired factor is \(W_k(s)=\prod_{r=1}^{k}[1-\sin^2(\pi s/N)/\sin^2(\pi r/N)]\). These are the [physical fixed-basis coordinates](actual_main_meridian_turn_comparison.md), including their repeated-node data.

For the fixed finite tree, the minimum of any finite list of these positive margins and the one-edge wire-contour margins is positive. When necessary it may be reduced by a fixed factor, leaving room for the \(O(N^{-1})\) shifts of endpoints and for slightly nested compact contours. Polynomial factors in \(N\) do not use up that margin. The tail contains infinitely many Fourier charges, but its original estimate is a geometric series with ratio bounded by a constant times \(e^{-Ny_v}\); it does not require taking a minimum over infinitely many unrelated errors.

The proof of these facts is in directed §§2–6, from its actual full kernel, its normalized real and strip bounds, and the exact translated-grid trace. In particular it does not assume a relative estimate at a very small nonminimal saddle. Each such charge is its local saddle contribution plus an additive error already below the first charge. That distinction remains in the higher-order argument.

## 3. The same margins on fixed translated charts

Fix a compact \(K\subset\{\operatorname{Im}s>0\}\). The actual moving orientation types use \(s\) or \(-s\); the opposite-order constant type uses its original parameter zero and full normal functional. Only bounded prefactors change in passing from the original disk to these compacts.

### 3.1. The paired turn factors

Euler's product gives the exact identity
\[
 W_k(s)=\prod_{\substack{1\le r\le k\\j\in\mathbb Z}}
                  \left(1-\frac{s^2}{(r+jN)^2}\right),
                 \qquad 0\le k<N.
 \tag{9}
\]
All integers in this product are distinct and nonzero. For bounded \(s\), the logarithms of the factors with sufficiently large integer modulus are bounded in absolute value by \(C_K/m^2\). The product over the finitely many remaining integers has a positive lower bound on \(K\cup(-K)\), since no integer lies there. Consequently every subset product in (9), and its inverse, is bounded uniformly in \(k,N\). Also \(H_N\) and its inverse are bounded there for all sufficiently large \(N\), since \(H_N\) tends uniformly to the nonzero function \(\sin(\pi s)/(\pi s)\).

The proof of the directed rectangle bound uses these factors only through their absolute bounds. Its positivity argument is applied to the complete Newton factors at real angles before this bounded multiplier is inserted. Thus no positivity in \(s\) is required. The conditional constant remains the same \(\operatorname{Re}\psi(0,u)\), and the real/angular losses and the high-index complement loss are unchanged.

### 3.2. The actual fixed-power trace and its normal channels

The canonical stripped fixed-power crossing polynomial has the exact interpolation of source-bound (D14):
\[
 r_{N,\sigma}^{[n]}(z)=
 -\frac1{N(U-U^{-1})}
 \sum_{j=0}^{N-1}\lambda_j(\sigma)^n(t_j-t_j^{-1})
                       \frac{P_\sigma(z)}{z-c_j(\sigma)},
 \quad U=e^{2\pi i\sigma}.
 \tag{10}
\]
Here \(t_j=q_N^{-2j-1+2\sigma}\), \(c_j(\sigma)=t_j+t_j^{-1}\), and \(P_\sigma(z)=\mathcal T_N(z)+2\cos(2\pi\sigma)\), where \(\mathcal T_N(t+t^{-1})=t^N+t^{-N}\). The quantity \(\lambda_j(\sigma)=(-1)^j q_N^{j(j+1)}(q_N^2)^{-\sigma j}\) is the stripped spectral value. The full physical representative is \(\kappa_\sigma^n r_{N,\sigma}^{[n]}\), where \(\kappa_\sigma=q_N^{(N-1+\sigma)^2/2}\). This common Cartan scalar is retained in the exact ledger, together with the prescribed mixed references.

On \(K\cup(-K)\), \(|U-U^{-1}|\) has a positive lower bound. The nodes lie in an ellipse of height \(O_K(N^{-1})\), and the divided-difference estimates used in the original full-polynomial norm proof are polynomial in \(N\) there. The full eigenvalue and carrier scalars have bounded modulus for each fixed signed power, including negative powers. This proves the same polynomial norm bound used in outgoing-envelope regeneration, with its complete Hermite derivatives retained.

For the constant channel \(\sigma=0\), use its original full trace, rather than evaluating an isolated singular summand of (10). Equivalently carry a small independent formal \(\sigma\) around zero, prove the estimate on a fixed parameter circle avoiding collisions, and apply the maximum principle to the **whole finite trace minus its first-charge expression**. All Fourier coefficients are entire in \(\sigma\), and the original physical trace has the proved removable normal value. Cauchy's formula also retains any fixed normal derivative required by the actual channel. The edge parameter \(s\) remains independent of this formal normal parameter during this argument. Nothing identifies a constant opposite-color channel with a moving same-color one.

The full complete Hermite norm is the maximum of the values at the distinct complete Casimir nodes and the first derivatives at their double nodes. At odd levels the final node \(-2\) is simple and has no derivative coordinate. This norm, the canonical polynomial sup norm and the Chebyshev coefficient norm differ by polynomial factors in the fixed degree range. Chebyshev folding involves a fixed number of folds at a vertex, and \(\cos(2\pi\sigma)\) is bounded on the chosen parameter compacts. Thus directed (43) and the real-envelope patch remain valid. Their powers of \(N\) and constants can increase, but their exponential terms do not.

### 3.3. Grid translations, endpoint currents and tails

Use the exact single-grid contour from the direct-crossing trace, not a periodic version of its chirp. A fixed \(\sigma\) shifts the grid and its endpoint rectangle by \(2\pi\sigma/N\). The latter displacement is \(O_K(N^{-1})\). At a translated vertical side the exact grid kernel is the same elementary expression
\[
 \frac{iN e^{-Nv}}{1+e^{-Nv}}.
 \tag{11}
\]
Thus the existing endpoint estimate applies there with at most a bounded exponential prefactor. The real interval and the retained local contours can be returned to the original ones with their connecting currents kept. Their locations are within \(O_K(N^{-1})\) of the original endpoint or fixed local connector and hence retain a fixed part of the original gap.

For \(s\mapsto s+j\), reindex the central entries and explicitly retain the bounded number of wrapped entries near \(\pm\pi\). The chirp is not periodic; its wrapped values cannot be discarded by declaring the grids identical. Their exact factors are bounded on the fixed compact and the original endpoint action loss applies.

The paired charges have coefficients
\[
 c_{\ell,N}(\sigma)=(-1)^{(N-1)(\ell-1)}
          U_{\ell-1}(\cos2\pi\sigma),\qquad c_{1,N}=1,
 \quad
 |c_{\ell,N}(\sigma)|\le
       \ell e^{2\pi|\operatorname{Im}\sigma|(\ell-1)}.
 \tag{12}
\]
For each vertex, the extra fixed exponential in \(\ell\) is absorbed in \(e^{-N\ell y_v}\) once \(N\) is large. The finite set of retained charges remains subject to (8). The endpoint and zero-mode currents are those of the original finite trace. All the bounds are conditional on the parent angle on its compact rectangle, not only at its eventual saddle.

It follows by the exact same normalized subtree induction that the directed first-order theorem, its nonzero conditional first charge, its real/strip envelopes and all the fixed exponential errors hold on \(K\), with unchanged certificate. This statement follows from the finite source on \(K\). It is not analytic continuation of an asymptotic estimate proved elsewhere.

## 4. Arbitrary-order edge and conditional saddle expansions

The canonical interpolation is
\[
 G_N(z)=\left(\frac{2\pi}{N}\right)^z\Gamma(z+1)
    \prod_{j\ge1}
     \frac{\Gamma(Nj+z+1)}{\Gamma(Nj-z)(Nj)^{2z+1}}.
 \tag{13}
\]
It satisfies, with the fixed normalization,
\[
 G_N(k)=S_k,\qquad
 G_N(z)G_N(N-1-z)=N,\qquad
 G_N(s)G_N(-s)=H_N(s)^{-1}.
 \tag{14}
\]
The midpoint \((N-1)/2\), rather than \(N/2\), remains in the exact Newton interpolation. In the bulk, every prescribed finite Stirling expansion gives
\[
 \log G_N(Nx)=NJ(x)+\tfrac12\log(2N\sin\pi x)
       +\sum_{j=1}^{L}N^{-j}b_j(x)+O(N^{-L-1}).
 \tag{15}
\]
This holds with any fixed number of derivatives on smaller complex bulk compacts. To justify summation in (13), take sufficiently many terms in the finite periodic-Bernoulli remainder for the Gamma factors. On a fixed bulk compact their arguments remain in a common right-half-plane sector. The remainder of the \(j\)-th product factor is bounded by \(C_LN^{-L-1}j^{-L-1}\), taking extra terms first when necessary for summability. The remaining finite number of factors is controlled in the same sector. Cauchy estimates give the derivatives. This proves every requested finite order; it assumes no convergence of the asymptotic series.

The exact circle Newton interpolant is
\[
 \mathcal E_N(x,\tau)=
 \frac{G_N(d/2+u)G_N(d/2-u)}
      {G_N(d/2-Nx+u)G_N(d/2-Nx-u)G_N(Nx)^2},
 \qquad d=N-1,\quad u=\frac{N\tau}{2\pi}.
 \tag{16}
\]
At \(x=k/N\), this equals \(e_k(-2\cos\tau)\). The exact edge multiplier is
\[
 \frac{H_N(s)}{W_k(s)}
       =\frac{G_N(k)^2}{G_N(k-s)G_N(k+s)}.
 \tag{17}
\]
The reflection and the factor \(H_N^{-1}\) in (14) fix the normalization in (17). Inverting that relation would insert an incorrect extra cut factor.

On the directed local angle rectangle the edge critical wire remains in a fixed complex neighborhood of the real interval \((1/5,3/10)\), away from every factorial endpoint. Equations (15)–(17), the exact primitive wire contour and its endpoint currents therefore give an all-order version of directed (24):
\[
 \mathscr K_N(t,u;s)=N^{-3/2}e^{N\psi(t,u)}a_e(t,u)
       \left[1+\sum_{j=1}^{L}N^{-j}k_{e,j}(t,u,s)
                         +O_{K,L}(N^{-L-1})\right].
 \tag{18}
\]
The leading \(a_e\) is the original nonzero amplitude and is independent of \(s\). The coefficients and remainder are holomorphic in both angle variables and \(s\), with fixed derivative estimates on smaller compacts. The complementary wires, finite lattice currents and local-contour endpoints have the same fixed exponential losses as before; they are smaller than every requested relative power after comparison with the local saddle.

For clarity, the all-order step in (18) can be carried out without citing a formal stationary-phase principle as an estimate. On the deformed local contour the real part of the exponent falls quadratically away from the selected saddle. Restrict to a fixed neighborhood, use the analytic Taylor series of the phase and amplitude to any desired finite order, put the centered variable equal to \(N^{-1/2}\) times a new variable, and integrate the resulting Gaussian moments. Split that neighborhood at a shrinking radius \(N^{-\epsilon}\), choosing sufficiently many Taylor terms for the requested order. Outside the shrinking neighborhood the quadratic bound is exponentially small; inside, the analytic Taylor remainder is dominated by an integrable Gaussian times its required power. Odd Gaussian moments vanish and the common half-power is already displayed in \(N^{-3/2}\). The same proof with the one-dimensional physical trace contour gives its \(N^{3/2}\) factor and all relative orders. All these estimates are uniform on the fixed parameter compacts, because the saddle, inverse Hessian and nonzero leading amplitude remain on compact sets.

The integral of the absolute local Gaussian amplitude divided by the absolute value of its leading complex Gaussian integral is bounded uniformly on such compacts. The bound can depend on the fixed degree and signed twist. It is not asserted to be a universal constant across all trees. This is sufficient to integrate a uniform relative remainder without amplifying it by an exponential factor.

## 5. All-order normalized message induction

We strengthen directed (28), keeping the same limiting phase and leading amplitude. For every requested \(L\), at every nonroot vertex,
\[
 \frac{M_{v,N}(u;s)}{M_{v,N}(0;s)}
  =e^{Nh_v(u)}\frac{\alpha_v(u)}{\alpha_v(0)}
      \left[1+\sum_{j=1}^{L}N^{-j}a_{v,j}(u,s)
                         +O_{K,L}(N^{-L-1})\right].
 \tag{19}
\]
The coefficients may and do have zero normalized value at \(u=0\). The remainder and any prescribed finite derivative are uniform on smaller parent compacts. The exact complex denominator is retained; it is not replaced by an absolute estimate or by a presumed asymptotic scalar. The leading amplitude is nonzero and independent of \(s\) after the exact outside physical scalars have been separated.

For a terminal vertex, insert (18) into its exact full trace. The first charge has coefficient one by (12); its sine and Gaussian factors are nonzero. Expand that conditional first-charge integral to the requested order. The estimates in §2–3 bound the entire remainder of the trace below the first charge by a fixed exponential factor. Evaluating also at \(u=0\) and dividing the two expansions proves (19), and proves nonvanishing of the exact denominator for sufficiently large levels.

Suppose (19) holds for the children of \(v\). Divide each exact child by its exact value at zero in the actual recurrence before making any approximation. The finite product of their expansions has every prescribed relative order. Its normalized leading amplitude has no zero, so the logarithm of this product, with the normalization fixed at zero, has an expansion of the same order. This is an ordinary finite algebraic operation on asymptotic series with a uniformly invertible leading term.

In the conditional first-charge integral retain the limiting child phases in \(A_v^{\mathrm{loc}}\); place all higher logarithmic terms in the analytic amplitude. Equivalently one can perturb the conditional saddle by \(O(N^{-1})\), but no such perturbation is needed to estimate the remainder. The local absolute-to-leading Gaussian bound proved above shows that a uniform relative \(O(N^{-L-1})\) input error contributes a relative \(O(N^{-L-1})\) output error. Expand the new local amplitude and phase to a sufficiently high finite order and integrate. Division by the expansion at parent angle zero gives (19) at \(v\).

Outside that conditional saddle, do not insert a truncated child expansion. Use the exact normalized real and strip estimates already proved on \(K\) in §3. They are precisely what controls the full charge tail, original endpoint currents and complementary contour portions. This prevents a local asymptotic remainder from being used as a global source bound. The finitely many nonminimal charges need only their existing bound below the first charge; expanding them to every order is unnecessary.

All fixed derivatives are obtained on nested rectangles by Cauchy estimates, or by starting with sufficiently many orders and differentiating the local integral. Since the tree is fixed and every inequality has a strict margin, a finite nested system of slightly larger local compacts can be chosen. The real/strip bounds used for tails are those of the exact messages; they do not shrink with the order. Possible large constants in the coefficients only increase the level from which the estimate holds. They do not change any certificate inequality.

At the root the same induction applies with no parent kernel and no outgoing envelope. Restore the exact child values at zero recursively. Their actions add at their selected conditional saddles, giving the original joint action (6); they are not separately replaced by subtree volumes. The scalar restoration is the original exact ledger
\[
 A_N(s)=q_N^{a(D)s^2/2},\qquad a(D)=-w(D)-\sum_v n_v,
 \tag{20}
\]
with the single reduced cut \(H_N\) left outside. Same-color chirps, opposite-order references, turn gammas, closing and writhe factors are each counted once, as in the exact-scalar theorem. All \(s\)-independent phases and powers of \(N\) cancel in the ratio (3). In particular there is no unspecified \(s\)-dependent oscillating subtree constant in (19).

Every complete edge contributes \(N^{-3/2}\) and every trace contributes \(N^{3/2}\); the tree relation leaves the same total \(N^{3/2}\). The leading coefficient is nonzero. Thus the actual normalized whole source has an all-order expansion on the original disk and on \(K\). This proves existence and uniform remainder estimates; the next section identifies the polynomial degree filtration, which does not follow merely from existence.

## 6. Why the coefficients have the required degree filtration

At a retained physical edge the only remaining microscopic dependence, apart from (20), is the exact factor (17). Put \(\delta=N^{-1}\) and introduce an auxiliary independent parameter \(t\). Applying (15) to (17), before substituting \(t=\delta s\), gives
\[
 \log\mathcal I_N(x,s)
 =\delta^{-1}\mathcal K(x,t)+B_0(x,t)
       +\sum_{j=1}^{L}\delta^jB_j(x,t)+O(\delta^{L+1}),
               \qquad t=\delta s.
 \tag{21}
\]
The \(B_j\) are holomorphic near \(t=0\), are even in \(t\), and vanish there. Terms in \(\log N\) cancel. An original offset \(x=\ell(X)+\delta c\), including the midpoint offsets from \(d=N-1\), contributes \(c\mathcal K_x\) to \(B_0\) and holomorphic further terms to the lower amplitudes; it does not change the leading phase in (5).

To organize all orders, replace (17) in the **local first-charge integral** by its canonical interpolation with \(s=Nt\), for sufficiently small independent \(t\). All its factorial arguments then remain in the same complex bulk domain. This defines a local analytic family whose phase is exactly \(\Phi_t\) in (5). It is not an assertion about the physical source with \(s\) growing like \(N\): no global or tail estimate for that regime is used. Global errors have already been controlled for bounded physical \(s\). The auxiliary family organizes the local coefficients, and its restriction \(t=s/N\) reproduces the actual local source exactly.

The full Hessian of \(\Phi\) is invertible. Indeed the wire Hessians in each edge contour are invertible. After eliminating them, each successive angular conditional Hessian is invertible by the bound in §2. The determinant identity for a block Schur complement therefore gives invertibility of the original joint Hessian. This also identifies the joint critical point and the phase independently of the order of finite contractions. The analytic implicit-function theorem gives \(X_*(t)\) for small \(t\), with all logarithms and first-charge marks retained.

Expansion of this local analytic family to arbitrary finite order gives holomorphic coefficient germs \(C_j(t)\) such that
\[
 \log\mathcal Z_N(s)\sim
 N\{S(s/N)-S(0)\}
       +\sum_{j\ge0}N^{-j}\{C_j(s/N)-C_j(0)\}.
 \tag{22}
\]
One may perform the Gaussian expansions edge by edge and vertex by vertex, as in §5, or jointly. These are the same coefficients: at any finite order they are finite Gaussian moments of the same Taylor polynomial; iterated Gaussian integration and Schur complementation give the same moments. Absolute Gaussian domination justifies the uniform remainders in either computation. Thus (22) identifies the coefficients of the actual normalized induction, not those of an independently postulated effective phase.

For each fixed truncation order, Taylor-expand the holomorphic functions in (22) in \(t\), then put \(t=s/N\). Terms from \(N(S-S(0))\) have degree \(r+1\) at order \(N^{-r}\); terms from all \(C_j-C_j(0)\) have degree at most \(r\). The even phase has \(S'(0)=0\), so no order-zero nonconstant term occurs. This proves (4) and its top-diagonal assertion, with uniform remainders on every fixed \(K\). Since every discarded term has a fixed exponential gap, its polynomial prefactor and any fixed derivative are smaller than the requested \(N^{-L-1}\) order.

This argument also shows that the expansions on the disk and on all translated compacts have the same coefficients. They come from the same canonical local family and original scalar, not from continuing an asymptotic estimate across the resonances. Since \(\mathcal Z_N(s)\to1\) uniformly on each compact, its logarithm tending to zero is uniquely fixed for large \(N\).

## 7. The actual marked geometric germ for the new certificates

The analytic extension does not replace the geometric part of the directed theorem. Its certificate gives
\[
 \sqrt{d_v^2+n_v^2}=2\pi|D_v|\ge2\pi\,2^{15}>630
 \tag{23}
\]
at every vertex. The [vertexwise geometric theorem](actual_all_circle_vertexwise_geometry.md) supplies the positive ordered charge path with the original odd seams, primitive disk curves and the original main cusp unfilled. Back-substitution of the conditional first-charge roots places every angle in the common small-angular uniqueness polydisk; it is therefore the same path's endpoint, not merely a solution of exponentiated equations. This is directed §7, including its explicit backwards restoration.

With \(Q_v=e^{i\tau_v}\), the primitive equations are
\[
 U_v+p_vV_v=-2\pi i,\qquad V_v=2\log Q_v,
 \qquad n_v=\epsilon_v-2p_v.
 \tag{24}
\]
Along the continued charge path the constant on the right is \(-2\pi ic\). It is the linear term in (6). The positive endpoint has \(\operatorname{Im}\tau_v<0\), so \(Q_v^2\ne1\). A filling word commutes with this semisimple longitude; its eigenvalue ratio is one by (24), so it is projectively the identity. The representation therefore factors through the actual filled knot group on a neighborhood of the selected point.

The [local rational reconstruction and longitude theorem](actual_all_circle_geometric_characteristic.md) are algebraic statements on the full source branch; they do not require the old summed or maximum-based analytic inequality. The new directed case supplies exactly their required anchor: the actual positive filled holonomy at \(M=1\), the continued primitive logarithms, and the nondegenerate source critical point. The implicit branch of (5) consequently reconstructs a meridian-varying branch of representations of the filled group. Marked geometric rigidity identifies that branch with the geometric meridian germ of the actual knot. The negative longitude lift at its complete point is fixed by the once-bordered Seifert-frame calculation, not by a cusp tangent or a quantum normalization guess.

For this branch the exact identity is
\[
 L_{\mathrm{geom}}(M)
   =-M^{a(D)}\prod_{e\in\mathcal E_T}
               \frac{M^2-X_e(M)}{1-M^2X_e(M)},
       \qquad X_e=e^{2\pi ix_e},
 \tag{25}
\]
on the preferred longitude and the declared \(M\) eigenline, equivalently the inverse value on the source \(M^{-1}\) line. This is the geometric theorem's complete filled-germ statement; it does not require extending positive ideal tetrahedra through every algebraic value of \(M\).

Differentiating a stationary value differentiates only the explicit parameter. The sine identity in (5), with its logarithm zero at \(t=0\), gives
\[
 e^{\mathcal K_t(x,t)}=\frac{M^2-X}{1-M^2X},
                  \qquad M=e^{\pi it}.
 \tag{26}
\]
Set \(h=\log q\), \(u=\log M\), and
\[
 \mathcal S(u)=\pi i\{S(u/(\pi i))-S(0)\}.
 \tag{27}
\]
Then (25)–(26) give \(-e^{\mathcal S'(u)}=L_{\mathrm{geom}}(e^u)\) as an identity of holomorphic germs, not just to second order. The original first-charge and filling mark select this germ among the solutions of the rational edge and vertex equations.

### The preferred-cusp first correction

The analytic family in (5) is even in \(t\). Its selected critical point is therefore even, by uniqueness of the analytic implicit branch. The exact interpolated edge amplitude and scalar are even as well. Every stationary coefficient \(C_j(t)\) can consequently be chosen even. At order \(N^{-1}\), (22) has only
\[
 p_1(s)=\tfrac12 S''(0)s^2:
 \tag{27a}
\]
normalization eliminates a constant, the evenness eliminates the possible linear contribution \(C_0'(0)s\), and all other lower amplitudes begin at order \(N^{-2}\). Thus this coefficient is not identified merely by its highest polynomial degree.

On the preferred geometric germ, the cusp shape is
\(\tau_K=\left.\frac{d}{du}\log[-L_{\mathrm{geom}}(e^u)]\right|_{u=0}\).
Equations (25)–(27) give \(S''(0)=\pi i\tau_K\). Restoring the exact original framing, already included in \(a(D)\), yields for every directed case
\[
 \frac{F_N(q_N^s)}{K_NH_N(s)}
    =1+\frac{\pi i\,\tau_K s^2}{2N}
                         +O_K(N^{-2}).
 \tag{27b}
\]
This is uniform on each fixed compact used above and on each \(|s|\le R<1\), with the same geometric cusp shape of the original filled knot complement. In particular no additional unrecorded linear or constant scalar is left in the first correction. The exponential passage from the logarithm changes only order \(N^{-2}\) and higher.

## 8. Consequence for every genuine all-level annihilator

Let
\[
 P(q,M,T)=\sum_{j=0}^{d}a_j(q,M)T^j,
       \qquad TM=qMT,
 \tag{28}
\]
be a specified nonzero fixed operator with coefficients in \(\mathbb C(q,M)\) which annihilates the actual whole reduced function \(F_N(M)\) at every sufficiently large level. Negative shifts can first be removed by multiplying by a power of \(T\). Clear fixed rational denominators and remove the common \(q-1\) valuation. Let \(P_0(M,L)\ne0\) be the resulting first classical symbol. This hypothesis is the genuine all-level source equation; an equation fitted to complete values or to finitely many jets is not enough. The existence of such fixed operators is proved by the [finite-sum annihilator theorem](finite_sum_annihilator.md), with its boundary terms retained.

The full modified dimension is
\[
 d_N(M)=\eta_N\frac{M-M^{-1}}{M^N-M^{-N}},\qquad
 d_N(1)=\eta_N/N,\qquad \eta_N=i^{N+3}.
 \tag{29}
\]
It satisfies \(d_N(q_N^s)/d_N(1)=H_N(s)^{-1}\). For \(f(M)=M-M^{-1}\), the exact reduced-to-full gauge is
\[
 \widetilde P=\sum_{j=0}^{d}
 a_j(q,M)(-1)^j\frac{f(M)}{f(q^jM)}T^j.
 \tag{30}
\]
Indeed \(H_N(s+j)/H_N(s)=(-1)^j f(M)/f(q_N^jM)\). After multiplying on the left by \(\prod_{j=1}^{d}f(q^jM)\), its first classical symbol is
\[
                         f(M)^dP_0(M,-L).
 \tag{31}
\]
The meridian divisor and sign character remain in the calculation.

Choose a small upper-half-plane disk \(D\) and apply (4) to the compact union of the required translates \(D,D+1,\ldots,D+d\), slightly enlarged for coefficient estimates. The exact root equation (30), after division by the nonzero \(\mathcal Z_N\), makes every coefficient of its asymptotic expansion vanish on \(D\). Clearing denominators as above makes these coefficient identities polynomial in \(s\); they therefore hold identically.

Regrade the filtered series using \(u=hs\). The inequality \(\deg p_r\le r+1\) gives exactly
\[
 \log\mathcal Z\ \longleftrightarrow
 h^{-1}\mathcal S(u)+\sum_{j\ge0}h^j A_j(u),
 \tag{32}
\]
with no other negative power of \(h\). The finite difference under \(u\mapsto u+jh\) has no negative power; its constant coefficient is \(j\mathcal S'(u)\). Thus the formal shift ratio has constant term \(e^{j\mathcal S'(u)}\).

The substitution \(\mathbb C[[h,u]]\to\mathbb C[s][[h]]\), \(u\mapsto hs\), is injective: distinct monomials \(h^au^b\) have distinct images \(h^{a+b}s^b\). Lifting the exact coefficient identity before substitution and taking its constant \(h\)-coefficient yields
\[
 f(e^u)^dP_0(e^u,-e^{\mathcal S'(u)})=0.
 \tag{33}
\]
The formal series ring is a domain and \(f(e^u)^d\) is nonzero, so it can be canceled in this proved identity. This does not discard a peripheral component from the original operator. Equations (25)–(27) identify the remaining germ as the actual geometric eigenvalue germ.

Evaluation on that germ defines a nonzero prime in \(\mathbb C[M^{\pm1},L^{\pm1}]\), since it contains \(P_0\). It contains no nonzero polynomial in \(M\) alone because the meridian varies on an open disk. Hence it has height one and is generated by one irreducible Laurent polynomial \(A_{\mathrm{geom},\mathbb C}\). Consequently
\[
 A_{\mathrm{geom},\mathbb C}(M,L)\mid P_0(M,L).
 \tag{34}
\]
For an operator over \(\mathbb Q(q,M)\), contract the same prime to \(\mathbb Q[M^{\pm1},L^{\pm1}]\). It is again a nonzero height-one prime, with an irreducible generator dividing \(P_0\) over \(\mathbb Q\). Its complex factorization contains the selected component and whatever conjugate components the rational field requires. This does not assert that the selected complex component is itself defined over \(\mathbb Q\).

The evenness of the selected phase also gives the same reciprocal selected germ as in the existing filtered theorem. No new statement about multiplicities, equality with the full A-polynomial, or equality of operator ideals follows. There is no uniform nonvanishing claim across ordinary resonances and no physical fixed-\(M\ne1\) quantum asymptotic obtained by replacing bounded \(s\) by a quantity of order \(N\).

## 9. Proof dependencies and scope

The [directed finite-source theorem](actual_all_circle_directed_volume.md) supplies the following inputs:

1. Equations (N1)–(N4), (13), (25)–(26): actual basis, full Frobenius functional, complete metric, physical turn, and exact finite recurrence. These fix types, normals and the outside scalar.
2. Equations (14)–(24): full edge complement, conditional rectangle estimate, actual local wire contour and nonzero leading edge amplitude. Extending the compact changes only bounded \(H/W\) factors.
3. Equations (27)–(37): normalized conditional phase, its Hessian and Schur complement, first-charge drop and strict separation of retained charges.
4. Equations (38)–(43): actual full-input strip estimate, exact charge coefficient, tail/endpoint/current bounds, and outgoing-envelope regeneration. These estimates are applied to exact messages outside the local saddle at every asymptotic order.
5. Equations (44)–(46): backward restoration of the same joint critical point, common small-angular charge-path anchor and actual filled geometry.

The [exact interpolation theorem](exact_factorial_interpolation_and_complex_contours.md) and [regular-circle calculation](actual_main_meridian_regular_circle_trace.md), §10, fix (13)–(17), including all midpoint and reflection factors. The [direct-crossing trace](actual_main_meridian_direct_crossing_trace.md), §§2–4, fixes the finite translated grids and their endpoint currents. The [full source bounds](actual_main_meridian_source_bounds.md), (D9)–(D14), supply the full polynomial norm used in regeneration, including constant normal channels; the extension to compact nonreal parameters is checked in §3 above. The [exact scalar calculation](actual_main_meridian_exact_scalar.md) fixes (20) and the one reduced cut.

The [filtered characteristic theorem](actual_main_meridian_filtered_characteristic.md) supplies the algebraic organization of the canonical insertion and the Ore gauge. Its analytic hypotheses for the directed certificate are proved here: §§3–5 give every finite asymptotic order on the required charts with a uniform remainder, and §6 identifies those actual coefficients with the joint two-parameter insertion. The published first-order profile alone is not used as a substitute for either step.

Finally the [geometric-characteristic theorem](actual_all_circle_geometric_characteristic.md), §§5–10, supplies the marked reconstructed branch and the preferred longitude, with §5's complete filled-point anchor checked in §7 above for the new certificate. The positive geometric path depends on (23), not on the older summed or maximum-based source criterion. Thus no old analytic class restriction is silently used to identify the new source branch.

All work in this note is for the actual fixed finite tree. It does not give a multi-boundary replacement theorem for arbitrary short-power islands, nor an automatic result for a graph with cycles. Those would require their own conditional source estimates.
