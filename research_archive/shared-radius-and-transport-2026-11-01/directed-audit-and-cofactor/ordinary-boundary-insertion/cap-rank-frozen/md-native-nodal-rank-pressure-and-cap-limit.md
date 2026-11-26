# Source-exact Gaussian rank pressure, and its limitation for the protected cap

The original maximal-fold stable-atom expansion has more structure than a polynomial total-mass bound. At a positive nonsingleton face triple its rank distribution has a Gaussian upper bound. This estimate passes through the original shared coefficient extraction by using that same exterior's finite positive saddle. The cost is quadratic in a rank fugacity near zero; it is not a cost that tends to zero merely because the physical spectral neighborhood shrinks. The physical first normals already have strictly positive rank pressure.

The resulting cap comparison is a sufficient theorem about actual source atoms, rather than a hypothesis on an arbitrary signed decomposition. It gives a positive coherent cancellation margin relative to the cap exterior capacity. The final section proves that the particular combination of independent local Gaussian bounds and the worst root-count estimate is insufficient to pay the recorded R54 capacity excess. No full spectral-cube or full-volume theorem is claimed.

## 1. Exact finite rank polynomials

Use the original notation of `md-physical-fold-nodal-stable-jets-and-mass.md`:
\[
 N\ge3,\quad d=N-1,\quad J=\lfloor d/2\rfloor,\quad e=d-2J,
 \quad u_a=-a_a,\quad u_*=u_J,\quad F_b^*=R_J(b;u_*).
 \tag{1}
\]
For \(a=J-k\), the exact factorization is
\[
 R_J(b;u_a)=S_{2a}\Delta_a(x,b,y)K_{a,J}(x,y),\qquad
 K_{a,J}\preceq\left(\prod_{v=a+1}^J s_v^2\right)(x+y)^k.
 \tag{2}
\]
All coefficients of \(K\) are nonnegative. Expanding it into monomials gives stable atoms with principal deletion rank \(k\), without changing level or face variables.

Let \(L_a\) be the exact degree-\(J\) physical-node cardinal polynomials and \(T_a^{\mathrm{low}}\) the degree-\(J-1\) cardinals excluding \(u_*\), as constructed in that note. For a selected physical spectral value \(u_b\) and derivative order \(h\in\{0,1\}\), define the positive rank polynomials
\[
 \begin{split}
 Z_{N,F}^{[h]}(z;u_b)&=
    \sum_{a=0}^{J}|L_a^{(h)}(u_b)|z^{J-a}R_J(u_a),\\
 Z_{N,E}^{[h]}(z;u_b)&=
    \sum_{a=0}^{J-1}|(T_a^{\mathrm{low}})^{(h)}(u_b)|
                      z^{J-a}R_{J-1}(u_a).
 \end{split}\tag{3}
\]
Their coefficients are nonnegative in \(z\) and in the original face variables. They are exactly the absolute masses of the specified signed nodal atom lists; the rank is recorded before the common face extraction. They are not original quantum source polynomials and are not being substituted for the coherently signed numerator.

At a one-variable protected face triple \((x,0,0)\) or \((0,0,y)\), use instead the exact monomial \(R_j=S_j^2x^j\) or \(S_j^2y^j\), independent of \(u\). Its value has rank zero and its first normal is zero. Artificially interpolating this monomial would introduce unnecessary large ranks. In an original central port the accompanying \(xy\) correction then vanishes. The forbidden pattern with both outer variables protected does not occur at an actual MAIN mark on a simple matched sphere.

## 2. An exact comparison to the complete folded packet

Fix positive weights on a compact set of one supported face pattern, with at least two supported coordinates and \(A=x+y>0\). Put \(T_b=\sqrt{bA+xy}>0\). For a diagonal pair with \(c=b\), write the actual positive complete-node factor as
\[
 B_{N,a}=\beta_a^2\Delta_a(x,b,y)^2P_{d-2a}(x,y),\qquad
 \beta_a=S_{2a}/S_a^2.\tag{4}
\]
The original full central polynomial at \(u_a\) equals \(N^2B_{N,a}\). At odd levels its skipping term is nonpositive, and at even levels its two-step cut terms are nonpositive, since \(u_a\le u_*\). The cofactor values in those terms are nonnegative. Comparison with the value at \(u_*\) gives the lower inequality below. The upper inequality follows from (2), with every scalar retained:
\[
 \boxed{\quad
 \frac{B_{N,a}}{B_{N,J}}
 \le\left(\frac{R_J(b;u_a)}{F_b^*}\right)^2
 \le\frac{B_{N,a}}{B_{N,J}}
       \frac{A^{2k+e}}{P_{2k+e}(x,y)}.
 \quad}\tag{5}
\]
For the scalar cancellation in the upper bound, use
\(K_{a,J}^2\le(S_J/S_a)^4A^{2k}\) and
\(B_{N,J}=(F_b^*)^2A^e/S_J^4\). Thus no factor depending exponentially on \(a\) has been discarded.

The last ratio in (5) is explicit. At odd levels the positive forced factors occur in pairs with offsets \((l-1/2)/N\), \(1\le l\le k\), from the midpoint. At even levels they have offsets \(l/N\), with an additional central factor \(A\). In both cases
\[
 \log\frac{A^{2k+e}}{P_{2k+e}(x,y)}
 =\sum_{l=1}^k-\log\left(1-\frac{4xy}{A^2}
                       \sin^2(\pi t_l)\right),
 \quad 0<t_l\le k/N.\tag{6}
\]
For \(k/N\le1/4\), the inequality \(-\log(1-v)\le2v\) for \(0\le v\le1/2\) gives
\[
 0\le\log\frac{A^{2k+e}}{P_{2k+e}(x,y)}
             \le2\pi^2 k^3/N^2.\tag{7}
\]

The actual fixed-fold theorem, including its \(\beta\) and forced factors, supplies uniformly on a small real folded interval
\[
 \frac{B_{N,a}}{B_{N,J}}
 =a_N(\delta_a)\exp\{-N[V(\delta_a)-V(\delta_*)]\}
          (1+O(N^{-1})),\qquad
 \delta_a=\frac{k+e/2}{N},\quad\delta_*=\frac e{2N}.\tag{8}
\]
The positive amplitude and its inverse are uniformly bounded on a smaller interval. The phase is even analytic, \(V(0)=V'(0)=0\), and
\[
                         V''(0)=4\pi T_b/A>0.\tag{9}
\]
These are actual real-node statements, sufficient here; no differentiation of a value-only interpolation is being used.

Choose a small fixed \(\delta_0\). Equations (5)–(9) give, after shrinking it if necessary,
\[
 R_J(b;u_a)\le C\exp(-c k^2/N)F_b^*
                         \qquad(k/N\le\delta_0).\tag{10}
\]
Indeed the quadratic loss in \(V/2\) dominates the cubic error (7). The even offset \(e/(2N)\) is retained in the difference in (8); positive curvature bounds that difference below by a constant times \(k^2/N^2\).

For \(k/N\ge\delta_0\), the original global cofactor theorem gives a fixed loss \(e^{-\gamma N}\) relative to \(R_J(b;0)\). The exact even path comparison
\[
 R_J(b;0)\preceq\frac{2\cot(\pi/(2N))}{N}F_b^*<2F_b^*
 \tag{11}
\]
changes the reference by a bounded factor; at odd levels it is the same reference. Since \(k\le N/2\), decreasing \(c\) extends (10) to every node. All constants are uniform on the chosen positive compact and fixed supported pattern. No claim of a diagram-independent \(c\) is made.

For the lower cofactor, the positive normalized tail obeys both \(k_n\succeq xk_{n-1}\) and \(k_n\succeq yk_{n-1}\). Hence for \(a<J\),
\[
 R_{J-1}(b;u_a)\le\frac{2}{s_J^2A}R_J(b;u_a).\tag{12}
\]
This is a pointwise consequence of the coefficientwise inequality \(2k_n\succeq A k_{n-1}\). There is no inversion of an unstable lower cofactor.

## 3. Quadratic rank pressure for the actual central jets

The sums of absolute cardinal weights and their first derivatives are polynomial in \(N\), uniformly over the full real interval; this was proved by the finite cosine formula. Combining that fact with (10) and (12), and completing the square,
\[
 \tau k-c k^2/N\le\tau^2N/(4c),
\]
gives, for every fixed \(\tau\ge0\),
\[
 Z_{N,F}^{[h]}(e^\tau;u_b)\le C N^K e^{\tau^2N/(4c)}F_b^*,\qquad
 Z_{N,E}^{[h]}(e^\tau;u_b)\le
       \frac{C N^K}{s_J^2A}e^{\tau^2N/(4c)}F_b^*.
 \tag{13}
\]
The bounds are uniform over every selected physical node \(b\) and \(h=0,1\). Fixed first-normal coefficients, rather than growing derivative orders, are essential to the polynomial prefactor.

Insert these exact signed expansions into the original both-parity central polynomial or its first derivative. At an odd port the deletion rank is \(2J-a-a'\). At an even port its leading term retains \(x+y\) and has that rank; each cut correction removes that one-dimensional baseline factor and has rank \(2J-a-a'+1\). Its extra factor \(e^\tau\) is independent of \(N\). The fixed scalar \(a_J+u\), the physical \(xy\), and the derivative of \(a_J+u\) are all retained. Dividing the positive evaluations by the actual maximal-node reference yields (13) with the sum of the two cofactor constants and a polynomial factor. For \(xy=0\) the corresponding cut/skipping correction is exactly absent.

Thus, for a fixed set of spectator ports, arbitrary physical node choices and a value or first normal at each port, there is a source-exact signed stable expansion with the original monomial degree at every port. Denote its extracted nonzero binary atoms by \(Q_{N,\alpha}\), scalar coefficients by \(c_{N,\alpha}\), and total deletion ranks by \(r_{N,\alpha}\). All atoms use the same original face coefficient and have the same binary degree \(d\).

## 4. The estimate survives the common extraction

Let \(P_N^*(A,C)\) be the actual maximal-fold exterior from the both-parity cap note. Assume its strict connected exterior saddle. Define the finite positive rank polynomial after the common extraction by
\[
 \mathfrak P_N(z;A,C)=
       \sum_\alpha |c_{N,\alpha}|z^{r_{N,\alpha}}Q_{N,\alpha}(A,C).
 \tag{14}
\]
This is a finite sum, with ranks and all original face targets explicit. The unweighted coefficientwise comparison from the stable-jet theorem gives
\[
                  \mathfrak P_N(1;A,C)\preceq C N^K P_N^*(A,C).
 \tag{15}
\]

For the weighted bound, fix positive boundary values near \((1,1)\), and use the actual finite stationary radii of \(P_N^*\) for the extracted faces. They remain in a common positive compact. Apply (13) at those same radii and then the positive Cauchy coefficient upper. The baseline coefficient has the independently proved relative Gaussian asymptotic at precisely these radii, so division loses only a polynomial. Consequently
\[
 \boxed{\quad
 \mathfrak P_N(e^\tau;A,C)
       \le C_\tau N^K e^{C_*\tau^2N}P_N^*(A,C).
 \quad}\tag{16}
\]
One can take \(C_*\) to be the sum of \(1/(4c_t)\) over the nonsingleton cofactor incidences in (10); pure monomials contribute zero. The extra even ranks affect \(C_\tau\), not the exponent. The constants are uniform over the node/first-normal choices. This argument uses the actual shared extraction and its matching baseline lower asymptotic; it does not divide a coefficient Cauchy upper by another unrelated upper bound.

## 5. A resulting coherent cap criterion

The monotone coefficient-path theorem gives root-count distance at most \(r_{N,\alpha}\) between every nonzero stable binary atom and the original stable baseline. With the baseline root parameters \(\nu_N,\kappa_N\), fix \(T>1\) and write
\[
 R_T=\max\{1-\nu-\kappa,\nu-\kappa,1-4\kappa,
      (1-\nu-\kappa)/T+(\nu-\kappa)T-2\kappa\},\qquad
 c_T=T+T^{-1}.\tag{17}
\]
The finite root-count estimate bounds the atom's corresponding quantity by the baseline quantity plus \(c_T r/d\). For ranks at most \(\delta d\), apply the finite alternating-section inequality. Its first term costs \((R_T+c_T\delta+o(1))^{d/2}\). Sum its tilted and cutoff terms using the coefficientwise comparison (15); this retains the original baseline tilted coefficient and \(p_{N,M}^*\), rather than paying a spurious \(T^r\) for these two terms.

For ranks larger than \(\delta d\), use the actual sine-Cauchy bound \(\|\sum_{j\le M}(-1)^jq_jt^j\|_C\le Q(1,1)\), since every diagonal Gram entry through the cutoff is at most one. Equation (16) and the exponential Markov inequality give their total relative rate at most \(-\delta^2/(4C_*)\), by taking \(\tau=\delta/(2C_*)\). The case \(C_*=0\) has no positive-rank mass and is interpreted directly.

Let \(F_0=\lim N^{-1}\log P_N^*(1,1)\), let \(F_T\) be the original tilted upper, and let \(\Phi-\gamma_D\) bound the original cutoff coefficient as in the both-parity cap theorem. Uniformly in the selected neighboring physical values and first normals, the exact cap contraction satisfies
\[
 \begin{split}
 \limsup_N N^{-1}\log\sup_{\sigma\in[-2,2]}|S_N^{\mathrm{jets}}(\sigma)|
 \le\max\{&F_0+\tfrac12\log(R_T+c_T\delta),\
           &F_0-\delta^2/(4C_*),\ F_T,\ \Phi-\gamma_D\},
 \qquad 0<\delta<(1-R_T)/c_T.
 \end{split}\tag{18}
\]
All neighboring scalar signs and cap phases are retained until applying the displayed positive norm to the already extracted stable atoms. The number of ports is fixed. The original full-Hermite insertion in those central ports is a polynomial-cost finite combination of their value and first-normal data, so the same rate upper applies to their fixed signed-power insertion. This is one original protected noncentral sector with all other ports central, not a bound on the sum of all sectors.

Equation (18) yields a strict cancellation loss relative to \(F_0\) whenever the tilted and cutoff rates are also below \(F_0\). To obtain a bound below \(\Phi\), its first two losses must exceed \(F_0-\Phi\). This comparison is an additional quantitative requirement; it is not implied by \(C_*<\infty\).

## 6. Physical first normals already have positive rank pressure

The failure of an automatic small-window cost can be quantified for the particular nodal expansion. Consider first odd levels and the actual nearest double node \(u_{J-1}=-4\sin^2\theta\), rather than the simple maximal node. For \(a=J-k\), \(k>1\), its cardinal derivative has exactly
\[
 |L_a'(u_{J-1})|=
 \frac{\cos(k\theta)}{4\cos\theta\,[\sin^2(k\theta)-\sin^2\theta]}.
 \tag{19}
\]
To derive it, the full nodal polynomial is \(u\prod_{k=1}^J(u+4\sin^2(k\theta))\); differentiate its product cardinal formula at the other node. At even levels the maximal node is double. Since the distinct \(z_a=\cos((2a+1)\theta)\) are zeros of \(T_{N/2}\),
\[
 |L_a'(u_*)|=
 \frac{\sin((2a+1)\theta)}
      {\sin\theta\,|u_*-u_a|},\qquad a<J.\tag{20}
\]
For \(k/N\to\delta\in(0,\delta_0)\), these weights and their inverses have zero exponential rate at both parities.

The lower half of (5) and the actual packet (8) therefore show that the absolute rank polynomial of these physical first normals satisfies
\[
 \liminf_N\frac1N\log\frac{Z_{N,F}^{[1]}(e^\tau;u_{\mathrm{normal}})}{F_b^*}
 \ge \sup_{0<\delta<\delta_0}\{\tau\delta-\tfrac12V(\delta)\}>0
                                      \quad(\tau>0).\tag{21}
\]
As \(\tau\downarrow0\), this lower bound is
\[
                   \frac{A}{4\pi T_b}\tau^2+O(\tau^4).\tag{22}
\]
The nodes in (19) and (20) approach the maximal fold. Thus shrinking a physical spectral neighborhood does not make this expansion's rank pressure vanish at fixed \(\tau\). This is an obstruction for this absolute atom partition, not for all coherent representations of a first normal.

## 7. Why this local-Gaussian/root-count combination does not certify R54

There is a concrete lower limit on the constant produced by summing independent local Gaussian bounds in (16). The original R54 spectator region 1 has quartet \((7,29,26,51)\). Face 29 is protected, so its input cofactor has middle weight zero and two positive outer weights. In (22), \(T_b=\sqrt{xy}\) and
\[
                    \frac{x+y}{4\pi\sqrt{xy}}\ge\frac1{2\pi}.
 \tag{23}
\]
Any pointwise local Gaussian constant valid for its first-normal rank mass must be at least this lower pressure coefficient. Therefore the \(C_*\) obtained by summing such constants is at least \(1/(2\pi)\).

For the already certified choice \(T=17/5\), one has \(c_T=314/85>3\). Any admissible \(\delta\) in (18) is smaller than \(1/c_T<1/3\), so the high-rank loss of this estimate is bounded by
\[
 \frac{\delta^2}{4C_*}<\frac\pi{18}<\frac15.\tag{24}
\]
The capacity excess here has a certified **lower** bound. In `md-singleton-obstruction-certified-results.json`, the field `dual_entropy_lower_and_upper[0]` is a feasible-flow entropy lower for the protected-singleton capacity, while `complete_action_upper_witness_bounds[1]` is a positive-radius Cauchy upper for the complete action. The protected retained triangle is a single supported face and contributes zero entropy. Removing that triangle leaves exactly the same exterior interior-face demands and leaves its two boundary loads free. Thus its feasible flow also gives a lower bound for the exterior pressure \(F_0\) used in (18). Subtracting the two recorded rational endpoints gives exactly
\[
 F_0-\Phi\ \ge\
 \frac{205572427687494348607257752733876626883}{10^{39}}
 >\frac15.
 \tag{25}
\]
For shorter rational bounds one may use \(F_0\ge678938190642/10^{10}\) and \(\Phi\le676882466366/10^{10}\), whose difference is \(2055724276/10^{10}>1/5\). These are outward bounds from the same certificate. In particular this is not inferred from the separate response estimate \(F_0\le67.894\) and complete-flow lower \(\Phi\ge67.687\), which give only an upper bound on the excess. Thus no choice of \(\delta\) makes this particular independent-local-Gaussian plus worst-root-count estimate prove the needed R54 geometric gap. This conclusion is analytic, not a sample of levels or a failed numerical optimization.

It does not rule out a smaller pressure after optimizing the joint shared coefficient directly, stronger root-moment control than the worst CDF estimate, or coherent regrouping before taking absolute atomic masses. In particular the positive-pressure lower above is local; it is not asserted to be a lower bound for every extracted joint pressure. The exact all-parity maximal-node cap gap remains valid. Extending it to neighboring normals and fillings at the geometric rate remains the missing comparison.

## 8. Inputs and status

The nodal factorization, both-parity mass, actual ranks and cardinal bounds are preserved in `md-physical-fold-nodal-stable-jets-and-mass.md`. The packet used in (8) is `actual_positive_face_fixed_fold_packet.md`, section 3, with all beta and forced factors; the far-node estimate is `actual_cross_cofactor_global_angular_gap.md`, section 2. The coefficient saddle and the all-level maximal-node cap theorem are detailed in `md-native-maximal-fold-cap-gap-both-parities.md`. The root-count theorem is `md-odd-neighbor-spectrum-matroid-path-and-cap-cost.md`; despite its original application title, its finite PSD determinant and coefficient-path theorem has no parity premise. The finite sine-Cauchy and section inequalities are `research_cap_uniform_spectral_gap.md`.

These are exact finite constructions and analytic estimates for the original targets. They add no new topology or volume identification. The theorem (18) is an actual-source sufficient rate criterion; section 7 records a rigorous limitation of the derived local constants in the principal diagnostic case, rather than claiming the general signed-source problem solved.
