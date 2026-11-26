# Full original volume limit for every even opposite-offset bipyramid

This is a private independent assembly of the shared-radius estimate with the original finite source and the established general Morse filling theorems. The sphere, matching, crossing disks and protected mark are unchanged. The argument uses a bound for the full source minus its actual CROSS projection; it does not identify the entire source with a positive model.

## 1. Statement and original diagram

Fix an even integer \(m\ge6\). Use pole vertices \(P_+,P_-\), rim vertices \(v_j\), indices modulo \(m\), and oriented triangles
\[
 (P_+,v_j,v_{j+1}),\qquad (P_-,v_{j+1},v_j).
 \tag{A1}
\]
Pair the north triangles across \(P_+v_j\) for odd \(j\), and the south triangles across \(P_-v_j\) for even \(j\). Every triangle belongs to exactly one matched pair. Mark the unmatched edge \(v_0v_1\). This is a simple matched sphere with \(m\) crossing circles and \(m+2\) white faces.

The argument order of its original homogeneous source is \((x,b,c,y)\), while the cyclic quadrilateral order is \((x,b,y,c)\). Thus its actual ordered quartets are
\[
 (P_+,v_{j-1},v_{j+1},v_j)\quad(j\text{ odd}),\qquad
 (P_-,v_{j+1},v_{j-1},v_j)\quad(j\text{ even}).
 \tag{A2}
\]
In particular the south middle variables are reversed. Every use of a scalar symmetry below concerns the triangle rate, not a replacement of this physical frame.

Let the positive generator of a two-strand crossing be the original \(R\). With factors written in the order met by the strands, the actual filled diagram is
\[
 K_{m,\mathbf n}=\widehat{\beta_m(\mathbf n)},\qquad
 \beta_m(\mathbf n)=
 \sigma_2^{n_0}\sigma_1^{n_1}\sigma_2^{n_2}\sigma_1^{n_3}
       \cdots\sigma_2^{n_{m-2}}\sigma_1^{n_{m-1}}.
 \tag{A3}
\]
The axis is not a component of this link. The original crossing circles surround precisely these syllables. The filled main link is a knot exactly when the permutation of this word is a 3-cycle.

**Theorem.** For every fixed even \(m\ge6\) there is a finite number \(B_m\) such that, for every fixed integer tuple \(\mathbf n\) with \(\min_j|n_j|>B_m\) and every knot-producing parity pattern of (A3), the original knot is hyperbolic and
\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K_{m,\mathbf n})|
       =\operatorname{Vol}(S^3\setminus K_{m,\mathbf n}).
 \tag{A4}
\]
Here \(K_N\) is the original reduced enhanced Kashaev normalization, with unknot value one. The limit includes both parity sequences and composite levels. The powers are independently long and may have arbitrary signs and relative sizes. The threshold can depend on \(m\); neither \(m\) nor any power grows with \(N\). There is no moving-main-color conclusion in this theorem.

The literal annular identification can be checked before any source estimate. Number native quadrilateral sides by \(0=xb,1=by,2=yc,3=cx\). Pure pairs are \((0,3),(1,2)\); odd pairs are \((0,2),(1,3)\). The forward input/output sides are
\[
\begin{array}{c|c|c}
 &\text{input, inner then outer}&\text{output, inner then outer}\\ \hline
 j\text{ odd}&(P_+v_{j-1},v_{j-1}v_j)&(P_+v_{j+1},v_jv_{j+1})\\
 j\text{ even}&(v_{j-1}v_j,P_-v_{j-1})&(v_jv_{j+1},P_-v_{j+1}).
\end{array}
 \tag{A5}
\]
These are three concentric tracks, with north boxes on tracks 1,2 and south boxes on tracks 2,3. The south native frame becomes this forward frame by reversing both axes, a planar half-turn. It preserves the overpassing diagonal and a signed crossing; a stack of identical signed crossings retains its exponent. No reflection, single-strand reversal or scalar identity for a quantum turn is invoked. Cutting before box 0 proves (A3), carrying each original disk collar with it. Exactly one odd box of each kind gives a 3-cycle; more generally the original braid permutation tests every parity pattern.

## 2. The exact source and what must be bounded

Put \(q=e^{\pi i/N}\), \(d=N-1\), and
\[
 \chi_N(z)=2T_N(z/2)+2,
 \qquad V_N(z;\Omega)=\chi_N(z)(z-\Omega)^{-1}.
 \tag{A6}
\]
Polynomial division defines the degree-at-most-\(d\) matrix polynomial in (A6), including at every spectral root. It is the original Casimir numerator, not the adjugate of an unrelated matrix. Let \(H_V(x,b,c,y;z)\) be its original homogeneous four-face polynomial.

Writing the pole variables as \(A,B\) and the rim variables as \(z_j\), the full shared spectral polynomial is exactly
\[
\begin{split}
 S_N(\boldsymbol\sigma)
 ={}&[A^dB^d\prod_{j=2}^{m-1}z_j^d]\,
 \left.\prod_{j\,\mathrm{odd}}
 H_V(A,z_{j-1},z_{j+1},z_j;\sigma_j)
 \prod_{j\,\mathrm{even}}
 H_V(B,z_{j+1},z_{j-1},z_j;\sigma_j)
 \right|_{z_0=z_1=0}.
\end{split}
 \tag{A7}
\]
Every local factor has total face degree \(d\) and spectral degree at most \(d\). Let \(S_{N,\mathrm C}\) select the actual central recurrence-path part at every box, by polynomial linearity, and set
\[
                 D_N=S_N-S_{N,\mathrm C}.
 \tag{A8}
\]
The task is a strict real-cube bound on (A8). The complete drilled rate of \(S_N\) alone would not give the smaller fixed-filled rate.

The general Morse compiler proves (A7) on this diagram. In its proof each actual box has factor \(N^{-1}H_V/(bc)^{d/2}\); the physical cups, caps and unrestricted mark leave \(N^{-m-1}\). The primitive face-potential lattice has \(m+1\) independent \(N\)-point grids, canceling that factor. Endpoint support is imposed before specializing those grids. The total numerator degree \(md\) forces the unique nonnegative alias: the two marked targets are zero and every other target is \(d\). This retains all repeated-node normal channels.

At even levels a literal integrated parity cochain is
\[
 t(v_j)=j\pmod2,\qquad t(P_+)=1,\qquad t(P_-)=0.
 \tag{A9}
\]
It agrees across matched spokes and differs across each strand edge; in particular the two protected endpoints differ. The integrated coset character at the unique supported target is one. No extra parity or power of \(N\) multiplies (A7).

The raw filled contraction is
\[
 Z_N(\mathbf n)=
       \left(\bigotimes_{j=0}^{m-1}\mathcal L_N^{n_j}\right)S_N,
 \tag{A10}
\]
where \(\mathcal L_N^n\) is the original full-Hermite functional for the signed power \(R^n\). Its crossing scalar and all first derivatives at double roots are part of its definition. Conversion from (A10) to the specified zero-framed reduced invariant is the original unit-modulus complete-color framing/component character. The separate full one-cut modified convention retains \(i^{N+3}/N\); it also has zero exponential rate.

These exact facts use `research_matched_sphere_morse_source.md`, §§5–6, and `actual_uniform_filling_supremum_bound.md`, §1. They use the displayed Morse diagram itself, not an assumed flat-plat presentation or a scalar tree contraction.

## 3. The spectator envelope is exactly the union of the genuine rates

Use the source-normalized triangle potential
\[
 Q(w_1,w_2,w_3)=
 \max_{\substack{\alpha_i\ge0\\\sum_i\alpha_i=1/2}}
 \left\{\frac1\pi\sum_i
 [\Lambda(\pi\alpha_i)+\Lambda(\pi/2-\pi\alpha_i)]
       +\sum_i\alpha_i\log w_i\right\},
 \qquad \Lambda(t)=-\int_0^t\log|2\sin u|\,du.
 \tag{A11}
\]
At a zero weight restrict its load to zero. For one positive weight it is one half of its logarithm. It is symmetric, nondecreasing, and obeys
\[
 Q(cw)=Q(w)+\tfrac12\log c,
 \qquad Q(x,t,y)\ge\tfrac12\log t\quad(t>0).
 \tag{A12}
\]
The second inequality follows by using the admissible vertex with load \(1/2\) on \(t\). Its entropy is zero since \(\Lambda(0)=\Lambda(\pi/2)=0\). This proves the bound also when either other coordinate is protected.

For a fixed nonnegative face vector with \(x+y>0\), the genuine uniform local upper rates are
\[
\begin{split}
 X&=Q_b+Q_c,\qquad Q_b=Q(x,b,y),\quad Q_c=Q(x,c,y),\\
 A_{\mathrm L}&=\max(\log c,Q_b+\tfrac12\log c)\quad(c>0),\\
 A_{\mathrm R}&=\max(\log b,Q_c+\tfrac12\log b)\quad(b>0).
\end{split}
 \tag{A13}
\]
An overloaded zero middle gives the zero one-sided polynomial and is omitted. From (A12),
\[
 Q_b+\tfrac12\log c\le X,\qquad
 Q_c+\tfrac12\log b\le X,
 \qquad
 \boxed{\max(X,A_{\mathrm L},A_{\mathrm R})
     =H:=\max(X,\{\log b:b>0\},\{\log c:c>0\}).}
 \tag{A14}
\]
Thus the spectator \(H\) used by the three-vector proof is precisely the maximum of the genuine local rate bounds. No mixed term has been lost. This identity is already recorded in `general_actual_sector_cover_filling_volume.md`, equation (4), and in the final paragraph of the global LEFT theorem.

Here “uniform local upper rate” means
\[
 \limsup_{N\to\infty}\frac1N
 \log\sup_{\substack{\sigma\in[-2,2]\\|L_f|=\rho_f}}
 |H_{V,s}(L;\sigma)|\le A_s(\rho),\qquad s=\mathrm C,\mathrm L,\mathrm R.
 \tag{A15}
\]
For CROSS this follows from the cleared-cofactor coefficientwise real-interval interpolation bound and the positive complete triangle factors. For LEFT the original omitted-half product and both unused spectral products remain. The normalized interval continuant has nonnegative face coefficients on \([-2,2\cos(\pi/N)]\); taking face moduli therefore preserves the signed-continuant upper action. Its complete endpoint optimization gives (A13). The remaining real cap has width \(O(N^{-2})\). Since the actual spectral degree is at most \(d\), polynomial exterior comparison costs only
\[
 \exp\left[d\,\operatorname{arcosh}
   \frac{6-2\cos(\pi/N)}{2+2\cos(\pi/N)}\right]=O(1).
 \tag{A16}
\]
This applies to a polynomial with complex coefficients at each fixed face-phase tuple. RIGHT follows by the actual row/middle reversal, with \(b,c\) exchanged in its rate. These are the proofs of `actual_global_left_weighted_spectral_envelope.md`, §§1–4, and `actual_cross_cofactor_factorization.md`, §8. They include both parity conventions and sampled spectral zeros. A polynomial coefficientwise LEFT bound against its complete value is neither asserted nor needed.

In this family the outer pole is always positive, so \(x+y>0\) at every box and every one of the three proposed vectors. The zero-coordinate limits in (A11)–(A15) are therefore within the proved domain.

## 4. Complete packing and the three fixed shared vectors

Let \(\theta=\pi/m\). The complete packing has concentric pole boundaries of radii \(a_0-1,a_0+1\), where \(a_0=\csc\theta\), and unit rim disks centered at \(a_0e^{2ij\theta}\). The south disk is the exterior of its boundary. Adjacent rim disks are tangent and all other rim pairs are disjoint. Invert at the marked rim contact and multiply lengths by two. Both poles then have curvature one, the two protected faces become lines, and the remaining curvatures are
\[
 k_j=\frac{\cos\theta}{\sin^2\theta}
       [\cos\theta-\cos((2j-1)\theta)]
 =\frac{2\cos\theta}{\sin^2\theta}
              \sin(j\theta)\sin((j-1)\theta).
 \tag{A17}
\]
Thus \(k_0=k_1=0\), all other \(k_j>0\), and \(k_2=k_{m-1}=4\cos^2\theta\).

The labeled simple-sphere packing and its positive cut polyhedron identify the original augmented complement. The calibrated complete CROSS action is
\[
 \Phi_m=2\sum_{j=0}^{m-1}Q(1,k_j,k_{j+1})
              -\sum_{j=2}^{m-1}\log k_j
        =\frac{\operatorname{Vol}(Y_m^\epsilon)}{2\pi}.
 \tag{A18}
\]
The equality uses the original marked triangle calibration. It is not a full positive-endpoint source theorem. Deleting the two protected faces leaves a connected ordinary graph, since both poles meet every vertex of the surviving rim path. Thus its face Hessian has only the common-scale kernel, as required by the Morse CROSS theorem. Every matched edge has a positive outer and at least one nonmonomial triangle.

Put
\[
 a=\frac94,\quad C=\frac{27}4,\quad
 \lambda=\frac{a}{k_2}=\frac9{16\cos^2\theta},\quad
 w_j=\lambda k_j,
 \qquad L_{P_+}=L_{P_-}=1.
 \tag{A19}
\]
The whole vector \(W\) has \(w_2=w_{m-1}=a\) and
\[
 c:=w_3=w_{m-2}=a(4\cos^2\theta-1)\in[9/2,C].
 \tag{A20}
\]
Define \(W^{(1)}\) by replacing only \(w_2\) with 1, and \(W^{(0)}\) by replacing only \(w_{m-1}\) with 1. Each shared occurrence of that face is changed at once. Protected weights remain exactly zero.

The surviving one-sided anchors at \(j=0,1\) are LEFT; those at \(j=2,m-1\) are RIGHT. Every other box has both possible one-sided anchors. This follows directly from (A2), not from a reflected physical coupon. Use \(W^{(1)}\) for \(1\mathrm L\), \(W^{(0)}\) for \(0\mathrm L\), and \(W\) for all other anchors.

## 5. Independent all-size verification of the radius inequalities

Write \(F(r)=Q(1,r,0)\). Scale only the ordinary rim coordinates by \(t\in(0,1]\), retaining pole weights one, and let \(P(t)\) denote the complete action at that vector. The pole angle in triangle \(j\) is
\[
 \alpha_j(t)=\arctan\frac1{\sqrt{t(k_j+k_{j+1})+t^2k_jk_{j+1}}},
 \qquad \alpha_0(t)=\frac\pi2.
 \tag{A21}
\]
The complete star gives \(\sum_j\alpha_j(1)=\pi\). For every other triangle, with \(D^2=t(u+v)+t^2uv\),
\[
 -\frac{d\alpha}{d\log t}
 =\frac{t(u+v)+2t^2uv}{2D(1+D^2)}
 \le\sin\alpha\cos\alpha\le\alpha.
 \tag{A22}
\]
Hence \(\alpha_j(t)\le\alpha_j(1)/t\), and differentiation of the entire coupled action gives
\[
 \frac{dP}{d\log t}=2-\frac2\pi\sum_j\alpha_j(t)
       \ge1-\frac1t.
\]
Integrating in the decreasing direction yields
\[
 P(\lambda)-\Phi_m\le\lambda^{-1}-1+\log\lambda
       \le D_0:=\frac{16}9-1+\log\frac9{16}<\frac{203}{1000}.
 \tag{A23}
\]
The bound is independent of the number of triangles; it uses their original complete star, rather than summing independent local distortions.

For \(3\le j\le m-2\), (A17) gives
\[
 \frac13\le\frac{w_{j-1}}{w_j}\le2,
 \qquad \frac13\le\frac{w_{j+1}}{w_j}\le2.
 \tag{A24}
\]
The first ratio is \(\sin((j-2)\theta)/\sin(j\theta)\), increasing with \(j\); the second is \(\sin((j+1)\theta)/\sin((j-1)\theta)\), decreasing. Their extremal bounds use \(\sin3\theta\le3\sin\theta\) and \(\sin4\theta/\sin2\theta=2\cos2\theta\le2\), valid also at \(m=6\).

The logarithmic derivative of \(Q\) in a positive weight lies in \([0,1/2]\). Therefore \(F\) is increasing and \(F(r)-\log r\), \(F(r)-\tfrac12\log r\) are decreasing. Drop the positive pole, scale by the outer rim coordinate, and use (A24). At every interior box,
\[
\begin{split}
 X_j-\log\max(w_{j-1},w_{j+1})
 &\ge F(1/3)+F(2)-\log2=:B_{\mathrm{int}}>43/100,\\
 Q(1,w_{j\pm1},w_j)-\tfrac12\log w_{j\pm1}
 &\ge F(2)-\tfrac12\log2=:C_{\mathrm{int}}>21/50.
\end{split}
 \tag{A25}
\]
At boxes 2 and \(m-1\), the middle weights are \(0,c\) and the outer rim weight is \(a\). The same derivative bounds and \(c\le C\) give
\[
\begin{split}
 X_j-\log c&\ge F(a)+Q(1,C,a)-\log C=:B_{\mathrm{near}}>7/25,\\
 Q(1,c,a)-\tfrac12\log c
       &\ge Q(1,C,a)-\tfrac12\log C=:C_{\mathrm{near}}>21/50.
\end{split}
 \tag{A26}
\]
At boxes 0 and 1, \(X=F(a)>\log a\). Thus every spectator has \(H=X\) at \(W\). An anchored LEFT loss is \(\min(X-\log c,Q_c-\tfrac12\log c)\), and the RIGHT formula is symmetric. Equations (A25)–(A26), less (A23), give a net loss greater than \(7/100\) for every anchor other than \(0\mathrm L,1\mathrm L\). In particular even the weakest coarse comparison gives \(7/25-203/1000=77/1000>7/100\).

For \(1\mathrm L\), use \(W^{(1)}\). Its actual anchored rate is now zero and its complete rate is \(F(1)\). The entire complete-action change from \(W\) is
\[
 T(c)=2[F(1)-F(a)+Q(1,1,c)-Q(1,a,c)]+\log a.
 \tag{A27}
\]
It increases in \(c\): the logarithmic derivative at \(c\) of the first \(Q\) is larger than that of the second. The only possible spectator excess is at box 2,
\[
 E(c)=\max(0,\log c-F(1)-Q(1,1,c))\le E(C).
 \tag{A28}
\]
At box 3, put \(z=w_4\). Here \(z\ge1\), \(z/c\le2\), and \(1/c\ge4/27\), so
\[
 X_3-\log\max(1,z)
 \ge F(4/27)+F(2)-\log2>8/25.
 \tag{A29}
\]
Every other box is unchanged. Therefore the anchored cost at \(W^{(1)}\) is at most
\[
 P(\lambda)+T(C)+E(C)-F(1),
 \qquad S_0:=F(1)-T(C)-E(C)>37/100.
 \tag{A30}
\]
Its saving beyond \(\Phi_m\) exceeds \(37/100-203/1000=167/1000\). Reflection of the scalar weight formulas by \(j\mapsto1-j\), accompanied by exchanging pole labels, proves the same estimate for \(0\mathrm L\) at \(W^{(0)}\). It does not change the ordered quantum data in (A2).

The fixed constants in (A23), (A25), (A26), (A29), (A30) and \(F(a)>\log a\) have rigorous rational interval enclosures. The portable arithmetic argument encloses logarithms, square roots and arctangents, then uses the Euler sine-product expansion for the log-sine integral with an explicit one-sided tail. It checks fixed constants only, with no diagram-size sampling or optimization. The independent record is `md-cyclic-rational-constants-independent-read.md`, with exact output `md-cyclic-rational-constants-independent.json`. The narrowest reported net lower bound is greater than 0.08170. The coarse rational bounds above suffice for the stated \(7/100\) margin.

We have proved, at every surviving anchor \((j,s)\),
\[
 A_{j,s}(L^{j,s})+\sum_{i\ne j}H_i(L^{j,s})
     -\sum_{f\,\mathrm{ordinary}}\log L_f^{j,s}
                        <\Phi_m-7/100.
 \tag{A31}
\]

## 6. From the three vectors to the full shared remainder

Expand (A8) into genuine label strings in \(\{\mathrm C,\mathrm L,\mathrm R\}^m\), omitting zero strings and the all-CROSS string. Each remaining string contains a surviving one-sided anchor. Assign it to one such anchor, and use that anchor’s single whole face vector from §4.

For fixed real spectra, apply the multivariate Cauchy coefficient estimate to (A7) on the ordinary face torus of that vector. The protected variables are already zero and have no integration circle. The local estimates (A15), and the exact spectator identity (A14), give
\[
 \frac1N\log\|D_{N,\text{string}}\|_{[-2,2]^m}
 \le A_{j,s}+\sum_{i\ne j}H_i
       -\frac dN\sum_{f\,\mathrm{ordinary}}\log L_f+o_m(1).
 \tag{A32}
\]
The same face is used everywhere with its same weight. There is no independent local optimization, no exchange of a maximum and an infimum, and no relaxation of the shared demands.

The target difference \(d/N-1=-1/N\) contributes only the fixed number \(N^{-1}\sum_f\log L_f\). For fixed \(m\) there are finitely many vectors and at most \(3^m-1\) strings. Thus summing their absolute values costs \(\log(3^m-1)/N=o_m(1)\), not an extra exponential rate. Equation (A31) proves
\[
 \limsup_{N\to\infty}\frac1N\log\|D_N\|_{[-2,2]^m}
                    \le\Phi_m-7/100.
 \tag{A33}
\]
In particular, for every \(0<\eta<7/100\), the norm is at most \(\exp[N(\Phi_m-\eta)+o_m(N)]\). This statement includes even and odd levels. It requires no phase positivity of the shared source and no strict gap for the all-CROSS term itself on this whole spectral cube.

## 7. Full Hermite insertion introduces no new exponential cost

For \(H\) of degree at most \(d\), the exact finite filling theorem states
\[
 |\mathcal L_N^n H|\le(1+|n|/2)\|H\|_{[-2,2]}.
 \tag{A34}
\]
Its proof is the original midpoint/full-Hermite formula with the physical crossing multiplier, followed by sharp trigonometric Bernstein. It retains value and derivative terms at double roots and the odd simple endpoint. It applies to negative as well as positive powers, without a square-root normalization or omitted Cartan factor.

Both \(D_N\) and \(S_{N,\mathrm C}\) have degree at most \(d\) in each spectral variable. Applying (A34) successively yields
\[
 |Z_N-Z_{N,\mathrm C}|
 \le\prod_{j=0}^{m-1}(1+|n_j|/2)\,
                     \|D_N\|_{[-2,2]^m}.
 \tag{A35}
\]
The polynomial need not factor and its shared targets are unchanged. The stronger bound exploiting product-node vanishing is optional. For each fixed tuple \(\mathbf n\), the product in (A35) is independent of \(N\); hence (A33) is the actual filled scalar remainder rate. No Fourier-tail argument is needed for this remainder.

## 8. The nonzero original Morse contribution and its filled volume

The simple sphere, positive labeled packing, connected ordinary graph, primitive rank-\(m-1\) face quotient, and nonmonomial triangle at each matching edge have been checked in §§1–4. These are precisely the hypotheses of `actual_morse_cross_filling_period.md` and `actual_morse_geometric_contribution.md`. They concern the original all-CROSS projection (A7); they do not require complete-radius balance, a middle forest, a flat sweep or a full positive-endpoint source theorem.

Choose retained \(\epsilon_j\in\{-1,0,1\}\) with the prescribed parities and write \(n_j=\epsilon_j-2p_j\). The raw period has the nonzero asymptotic
\[
\begin{split}
 Z_{N,\mathrm C}={}&q^{d^2\sum_jn_j/4}(-2i)^m\sqrt{2\pi}\,N^{m+1/2}\\
 &\times\frac{\prod_j\sin(2\pi\delta_{N,\mathbf1,j})}
 {\sqrt{\det H_N(\delta_{N,\mathbf1})}\sqrt{\det Q_{N,\mathbf1}}}
 e^{N S_{N,\mathbf1}}
 \left(1+O_{m,\mathbf n}(N^{-1})
           +O_{m,\mathbf n}(e^{-c_{m,\mathbf n}N})\right).
\end{split}
 \tag{A36}
\]
These are the actual finite face/spectral saddles and Gaussian branches of that theorem, including their finite-level phase. The sine factors and determinants do not vanish at the chosen fixed long filling. The first reflected charges have already been paired by the exact finite trace; nonzero amplitude does not follow merely from a formal even phase. The source factor \((-1)^{dm}\) and Fourier factor \((-1)^{(N+1)m}\) cancel exactly. Both level parities therefore have this same nonzero normalization.

The limiting pure action \(A_0\) has \(A_0(0)=\Phi_m\), and the selected first-charge action is
\[
 S_{\mathbf1}=A_0(\boldsymbol\delta)
           +\pi i\sum_jn_j\delta_j^2+2\pi i\sum_j\delta_j.
 \tag{A37}
\]
The actual primitive logs satisfy
\[
 U_j=-\operatorname{Log}R_{0,j}+2\pi i\epsilon_j\delta_j,
 \quad V_j=-4\pi i\delta_j,
 \quad U_j+p_jV_j=-2\pi i.
 \tag{A38}
\]
They are original disk words with the signed half-twist correction once. The source differentiation and the marked regulator identity cancel the peripheral boundary term in (A37). The nearby framed representation, actual logarithmic link periods and the primitive equation in (A38) give a smooth filling of those very circles; the main cusp remains complete. Consequently
\[
 2\pi\operatorname{Re}S_{\mathbf1}
       =\operatorname{Vol}(S^3\setminus K_{m,\mathbf n}),
 \qquad \operatorname{Re}S_{\mathbf1}longrightarrow\Phi_m
 \quad\text{as all }|n_j|\to\infty.
 \tag{A39}
\]
The continuation permits independently long signed powers, with no ratio condition. The marked regulator alone is not being used as a replacement for metric completion.

Fix \(0<\eta<7/100\). Increase the long-filling threshold until both Morse theorems apply and the action drop is less than \(\eta/2\). Equations (A33), (A35) and the nonzero asymptotic (A36) give
\[
 \frac{Z_N-Z_{N,\mathrm C}}{Z_{N,\mathrm C}}
       =O_{m,\mathbf n}(e^{-\kappa_{m,\mathbf n}N})
       \quad\text{for some }\kappa_{m,\mathbf n}>0.
 \tag{A40}
\]
The unit-modulus framing character and the optional single modified factor have no exponential rate. This proves (A4).

There are finitely many retained half-twist patterns for fixed \(m\). Taking the maximum of their thresholds gives \(B_m\) for every knot-producing parity, not only the illustrative pattern with two odd boxes. Any signed odd \(n_j\) may, for example, be represented with \(\epsilon_j=1\) and integer \(p_j=(1-n_j)/2\); positivity of \(n_j\) is not presumed.

## 9. Exact limits of the conclusion

No defect was found in the full-source restoration. The suspected missing spectator estimate is the exact identity (A14). The three-vector argument keeps actual local sectors, all face phases, every spectral value in \([-2,2]\), and both level parities. No newly inserted tangle or invariant is involved.

All uses of finiteness are explicit: face weights may grow with \(m\), the number of strings is exponential in \(m\), and analytic thresholds may depend on \(m\). With \(m\) fixed, each contributes only a constant or an \(o_m(N)\) term. None contributes an omitted term proportional to \(N\) beyond the action already bounded. No assertion concerns a family with \(m=m(N)\), variable twists with \(N\), short powers outside the long threshold, or the moving-main-color profile.

The braid description does not prove the knot types are disjoint from all alternative Conway presentations. The geometric target is the complement of (A3), with its original disks and matching, not the isovolumetric augmented pretzel obtained by another shaded-face pairing. The proof is a volume theorem for this actual family and makes no classification or priority claim.
