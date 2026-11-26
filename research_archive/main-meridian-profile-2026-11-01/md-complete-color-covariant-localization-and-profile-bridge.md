# Complete-color covariant localization and the main-meridian profile

Private derivation, 1 November 2026. No repository source is changed.

This report concerns a fixed strict Conway source whose reduced hub tree has no adjacent bare hubs. All original auxiliary colors are \(N\). It identifies the exact finite contraction, proves a global old-positive majorant on its low-index part, and explains why high-index sectors and the complement of the selected regular window have a strict gap. The local ratios needed for the leading profile are stated separately from the localization proof. The last section records why the existing filling transfer still needs its actual parameter-dependent operator kernel.

## 1. Lower indices and the actual turn on an internal edge

Use the fixed canonical Newton basis \(e_0,\ldots,e_d\), \(d=N-1\), and put \(M_N=\lfloor d/2\rfloor\). Let
\[
 \mathbf J_{ab}=\mathbf1_{a+b=d},\qquad
 \phi_\sigma(e_a e_b)=\mathbf J_{ab},
 \quad
 \sigma=s\text{ for an equal-color pair, or }0\text{ otherwise}.
 \tag{1}
\]
Every vertex tensor below has lower indices. At a bare vertex it is
\[
 V_{v,s}(\mathbf n)=\phi_\sigma\!\left(\prod_{a\sim v}e_{n_a}\right).
 \tag{2}
\]
At a vertex carrying one original crossing-circle operator it is
\[
 V_{v,s}^{\epsilon}(\mathbf n)=
 \phi_\sigma\!\left(R_\sigma^\epsilon L_N
                         \prod_{a\sim v}e_{n_a}\right).
 \tag{3}
\]
All crossings include their full scalar and their actual mixed-order reference factor. An ordinary original leaf can be represented as a univalent vertex of type (3), attached by its original quarter-turn. An original flagged leaf is already absorbed into its incident hub as (3). Every remaining edge of this finite tree therefore carries a physical turn.

In fixed polynomial coordinates the turn is
\[
 T_\gamma=\frac{\gamma_N(s)}{H_N(s)}
       \mathbf J\operatorname{diag}(W_n(s)),\qquad
 W_nW_{d-n}=H_N^2.
 \tag{4}
\]
Raising a lower vertex index first uses \(\mathbf J\), so the propagator between lower tensors is
\[
 (T_\gamma\mathbf J)_{ab}
 =\delta_{ab}\frac{\gamma_N(s)W_{d-a}(s)}{H_N(s)}
 =\delta_{ab}\frac{\gamma_N(s)H_N(s)}{W_a(s)}.
 \tag{5}
\]
This proves equality of the two edge labels and fixes which paired factor occurs. It would be incorrect to substitute \(\mathbf JT_\gamma\) without changing the index convention. The actual type of the edge determines \(\gamma_N\); reversing its evaluation direction uses the already established self-adjoint pairing identity and retains its scalar ratio.

Consequently the original normalized closed scalar is a finite sum over these edge labels of the vertex tensors (2)--(3) and propagators (5), times its recorded bounded root phase. The reduced main cut multiplies it by exactly one \(H_N(s)\). A separate scalar \(\zeta_N(s)\) records the original ribbon framing and closing mark; it is not absorbed into the local turn factors. No auxiliary source is replaced by a scalar function, and no tangle isotopy is used.

On every disk \(|s|\le R<1\), the edge factors and their inverses are uniformly bounded for every index. On a fixed bulk interval \(\delta\le n/N\le1/2-\delta\),
\[
 \frac{\gamma_N(s)H_N(s)}{W_n(s)}
 =1+O_R(N^{-1}).
 \tag{6}
\]
These are the proved paired-turn estimates, including their actual phases.

## 2. A global all-low majorant at every circle vertex

Take a fixed number \(b\ge1\) of low indices \(0\le n_a\le M_N\) and put \(E=\prod_{a=1}^b e_{n_a}\). Each Laurent expansion \(e_n(-u-u^{-1})\) has nonnegative coefficients, so
\[
 |E(-2\cos(t+iv))|
 \le e^{D|v|}E(-2),\qquad D=\sum_a n_a\le bN/2.
 \tag{7}
\]
For the exact root grid
\(\tau_r=2\pi(d/2+s-r)/N\), the complete auxiliary color simplifies the physical trace to
\[
 \phi_s(R_s^\epsilon L_NE)
 =N q^{\epsilon(d^2/4-s^2/2)}
    \sum_{r=0}^{N-1}
        e^{i\epsilon N\tau_r^2/(4\pi)}
        E(-2\cos\tau_r).
 \tag{8}
\]
This follows from the exact chirp and
\(\sin(N\tau_r)=(-1)^{N-1}\sin2\pi s\). Both sides continue with their full normals at \(s=0\). On a fixed disk \(R<1/2\), (7), the grid height \(2\pi|\operatorname{Im}s|/N\), and the bounded chirp on that height yield
\[
 |\phi_s(R_s^\epsilon L_NE)|\le C_{R,b}N^2 E(-2).
 \tag{9}
\]
The opposite-color order has the same bound with its constant grid and its recorded bounded scalar.

The complete pure circle tensor is positive and controls the right side. Indeed
\[
 \phi_0(L_NE)=N\sum_{r=0}^{N-1}E(c_r),
 \qquad c_r=2\cos((2r+1)\pi/N),
 \tag{10}
\]
and every value in this sum is nonnegative for low Newton products. At odd levels the simple node \(-2\) gives the lower bound \(NE(-2)\).

For even \(N=2L\), choose the nearest node \(c_*=-2\cos(\pi/N)\). Write \(\theta=\pi/N\). For \(n\le L-1\),
\[
 \frac{e_n(c_*)}{e_n(-2)}
 =\prod_{r=0}^{n-1}
 \frac{\cos(r\theta)\cos((r+1)\theta)}
      {\cos^2((r+1/2)\theta)}.
 \tag{11}
\]
Each factor lies in \((0,1]\), so this product decreases with \(n\). At \(n=L-1\), the elementary sine and cosine products give
\[
 \frac{e_{L-1}(c_*)}{e_{L-1}(-2)}
 =L\tan(\theta/2)\ge\frac\pi4.
 \tag{12}
\]
For example, the numerator product in (11) is
\(L/(2^{2L-2}\sin\theta)\), while its denominator is
\(2^{1-2L}/\sin^2(\theta/2)\), giving (12). Thus (10) is at least \(N(\pi/4)^bE(-2)\). Combining this with (9) proves the global pointwise comparison
\[
 \boxed{\displaystyle
 |\phi_\sigma(R_\sigma^\epsilon L_N\prod_a e_{n_a})|
 \le C_{R,b}N\,\phi_0(L_N\prod_a e_{n_a})}
 \tag{13}
\]
for all low indices, both parities, and every \(\epsilon=0,\pm1\), with actual type scalars retained. No regular-window assumption enters (13).

At a bare vertex the separately proved all-parity whole-low-hub theorem supplies
\[
 |\phi_\sigma(\prod_a e_{n_a})|
 \le N^{C_b}\phi_0(\prod_a e_{n_a}).
 \tag{14}
\]
All terms on the right sides of (13)--(14) are the original complete pure tensors. Together with the bounded factors (5), they majorize the entire all-low contraction, state by state, by a polynomial multiple of the original positive complete contraction.

## 3. High labels have a strict global gap

Here is an error decomposition that retains the distinction between a coefficient-cone gap and a spectral gap. Root first at a flagged original leaf, if one exists. Write \(P_{\mathrm{lo}}\) for restriction of the outgoing coefficient index to \(0,\ldots,M_N\).

For an outgoing type-\(L\) module of original constant \(c_v\), decompose it as
\[
 L_v=L_v^{\mathrm{clean}}+E_v^{\mathrm{int}}+E_v^{\mathrm{hi}}.
 \tag{15}
\]
The clean term keeps every edge label in its subtree, including the outgoing label, low. The internal error has the coefficient cone with a strict constant loss \(c_v-\eta_v\), for some fixed \(\eta_v>0\), and hence spectral rate \(\Omega_v-\eta_v\). The boundary-high term is supported on high outgoing indices and has the original high coefficient bound \(e^{N(c_v+o(1))}\), hence spectral rate \(c_v=\Omega_v-2G_0\). Empty internal errors need no \(\eta_v\).

For an ordinary leaf, take its exact low projection as the clean term and its exact high projection as the boundary-high term; the decorated estimate proves (15). There is no internal error.

For a nonroot flagged hub, expand its child product using the children's clean and error parts. Every term with a child error has a strict spectral loss: an \(A\)-child error has its recorded spectral gap, an \(L\)-internal error has its cone gap, and an \(L\)-boundary-high error saves \(2G_0\). The actual decorated turn converts that spectral loss into a coefficient-cone loss at the output. Their finite sum is \(E_v^{\mathrm{int}}\). Apply the original cone estimate to the all-clean child product, and split its output into low and high coordinates. These are \(L_v^{\mathrm{clean}}\) and \(E_v^{\mathrm{hi}}\), respectively. This proves (15) inductively at flagged hubs without treating a spectral error as a coefficient cone for free.

For a bare hub, all children are type \(L\). Terms containing an \(L\)-internal error are bounded by the whole-hub theorem with that child's reduced cone constant, so they have a strict output spectral gap. Of the remaining terms, any with a boundary-high child falls in an actual high-input sector of the whole-hub theorem, which also has a strict spectral gap, including the exceptional two-input cases. Finally, with all children clean, the high-output part has the whole-hub high-output gap. Thus
\[
 Q_v=Q_v^{\mathrm{clean}}+E_v,\qquad
 \|E_v\|_{\mathrm{J}}\le e^{N(\Omega_v-\eta_v)}
 \tag{16}
\]
for a smaller positive \(\eta_v\), after absorbing finite errors. The clean term keeps all descendant and outgoing indices low. This \(A\)-error next enters a flagged hub, where it is converted to the cone loss required by (15). Separation of bare hubs is exactly the hypothesis that makes this step available.

The tree is fixed, so there are finitely many losses and band choices; their positive minimum remains positive after absorbing all polynomial factors and \(o(1)\) errors. At the flagged root the coupon has polynomial spectral norm, so every error term has rate below \(F_0\). When there is no flagged hub, there is one bare hub only; transfer an existing root leaf's turn, apply (16), and close with its polynomial root coupon. The strict two-leaf case uses the high-output saving of its one remaining decorated leaf.

Therefore the total summed contribution of states with at least one high edge label has a uniform strict exponential gap below \(F_0\). This argument sums the actual local return contributions in the proved hub bounds. It is not a bound on their separate absolute Newton expansion.

## 4. The selected geometric state is in a regular all-low window

Every bare hub receives rigid \(L\)-profiles \(g+c_a\). At its intrinsic closing state its outgoing \(Q=T(A)\) has \(X_Q=1\), and the unturned product has \((B_A,X_A,Y_A)=(-x,x,1)\), with \(1/2\le x<1\). All its effective \(L\) children share \(X=x\). Thus all incident covariant labels of that bare hub lie in
\[
 \frac14<a\le\frac{\arctan2}{\pi}<\frac12.
 \tag{17}
\]
The outgoing covariant label is the complementary product output, so it has the same positive cotangent \(x\). Constants \(c_a\) do not alter these parameters. The original strict hub support also gives
\[
 \sum_{a\sim v}a>1.
 \tag{18}
\]
The strict three-leg case has \(a=\arctan2/\pi\); it is not the flat value \(1/3\).

At an edge joining two flagged junctions, or joining an ordinary univalent circle vertex to a flagged junction, the rigid satellite is at its intrinsic \(X=1\) state and the edge label is \(1/4\). These statements include every remaining edge because bare junctions are separated.

For the fixed tree, choose a small compact neighborhood \(\mathcal W\) of the actual complete maximizing edge assignment. There is a fixed \(\delta>0\) such that every edge in this neighborhood has
\[
 \delta\le n_e/N\le1/2-\delta,
 \tag{19}
\]
and every bare vertex has incident total at least \(1+\delta\). The original finite \(d=N-1\) constraints cause only \(O(1/N)\) shifts; shrink the neighborhood once to retain these inequalities.

The original complete positive action has a unique strict maximum. Contracting the hidden positive leaf and binary-resolution variables preserves its maximum and gives a unique maximizing assignment of the retained edge coordinates. Uniform complete factorial upper bounds and polynomial state counting therefore give a strict rate gap off \(\mathcal W\). The pointwise all-low majorant (13)--(14) transfers this gap to the actual moving source. Section 3 supplies the high-edge gap. We obtain
\[
 Z_N^\epsilon(s)=
    \sum_{\mathbf n/N\in\mathcal W} w_{N,\mathbf n}^\epsilon(s)
      +O\!\left(e^{N(F_0-\eta)}\right)
 \tag{20}
\]
uniformly on the fixed microscopic disk, with original types and every internal turn factor retained.

## 5. The leading local comparison and the conditioning obligation

On \(\mathcal W\), the bare regular-window lemma gives
\[
 \frac{\phi_\sigma(\prod e_{n_a})}
      {\phi_0(\prod e_{n_a})}
 =1+O(e^{-\kappa N}).
 \tag{21}
\]
For up to four low factors this equality is exact; for larger fixed valence, (18)--(19) are precisely the hypotheses of the higher-alias gap.

The separate physical-circle-star lemma states, uniformly for its fixed number of regular low incident indices,
\[
 \frac{\phi_\sigma(R_\sigma^\epsilon L_N\prod e_{n_a})}
      {\phi_0(R_0^\epsilon L_N\prod e_{n_a})}
 =q^{-\epsilon s^2/2}\bigl(1+O(e^{-\kappa N})\bigr)
 \tag{22}
\]
in the equal-color frame, with the specified analogous bounded reference scalar in the mixed frame. The pure case is the exact or exponentially stable shifted-grid sum; the signed case uses the nonzero Gaussian anchor for the actual quadratic phase. Its denominator is therefore nonzero for large \(N\) on the regular window. Univalent physical leaves are the one-factor case.

Equations (6), (21), and (22) imply the fixed-state comparison
\[
 w_{N,\mathbf n}^\epsilon(s)
 =w_{N,\mathbf n}^\epsilon(0)
       \bigl(1+O_R(N^{-1})\bigr)
 \quad(\mathbf n/N\in\mathcal W).
 \tag{23}
\]
All retained reference phases are included; there are only finitely many vertices and edges.

To pass from (23) to a relative scalar statement one still uses the old complete-source conditioning:
\[
 \sum_{\mathbf n/N\in\mathcal W}
       |w_{N,\mathbf n}^\epsilon(0)|
 \le C\,|Z_N^\epsilon(0)|,\qquad
 |Z_N^\epsilon(0)|=N^{3/2}e^{NF_0}(c_\epsilon+o(1)),
 \quad c_\epsilon\ne0,
 \tag{24}
\]
up to the recorded unit phase. The complete core theorem supplies the nonzero asymptotic for the original strict knot patterns. Its contracted leaf coefficients have a real action at completeness, a nonzero smooth amplitude in a fixed strict window, and a negative real wire Hessian. These give the local bounded-total-variation estimate. The covariant grouping is obtained by summing retained internal indices with the exact complete positive multiplication tensors; the triangle inequality cannot increase the original contracted-wire total variation. Equivalently, the regular circle-star Gaussian anchor yields the same nonzero smooth amplitude directly in this grouping. No total-variation assertion is made for the uncontracted internal crossing paths.

With (22) and the applicable complete core theorem independently established, (20), (23), and (24) give
\[
 \frac{Z_N^\epsilon(s)}{Z_N^\epsilon(0)}
       =1+O_R(N^{-1}),\qquad
 \frac{\mathcal F_{N,\mathbf N}^{\epsilon}(q^s)}
      {\mathcal F_{N,\mathbf N}^{\epsilon}(1)}
       =\frac{\zeta_N(s)}{\zeta_N(0)}
          H_N(s)\bigl(1+O_R(N^{-1})\bigr).
 \tag{25}
\]
The full cut has exactly one \(H_N\). The explicit framing ratio is retained: it need not tend to one. For the logarithmic rate, uniform subexponential bounds for this ratio and its inverse suffice. Holomorphy on a slightly larger fixed disk gives the corresponding fixed-derivative statements on smaller disks after this ratio is divided out. This is a complete-auxiliary-color augmented-source statement. It is not yet the main-meridian profile of a filled knot.

## 6. What the old filling transfer additionally requires

The existing long-filling transfer has two separate kinds of input: an exact finite full-twist expansion in the original circle basis, including its endpoint/normal currents, and a nonzero holomorphic auxiliary-color packet on a fixed complex corridor. The latter must be exponentially accurate before the Fourier contour is moved. A real complete-color ratio such as (25), or an \(O(N^{-1})\) grid error at the augmented exponent, cannot be substituted into the filling sum: the filled saddle has a smaller exponent.

For a moving main meridian, the packet must be jointly holomorphic in the auxiliary deficits \(\chi_i=(N-j_i)/N\) and \(s\), with the same fixed domains, actual finite action and nonzero amplitude, uniform exponential comparison to the original source, and the reflected endpoint identities required by the exact filling transform. The new far-color theorem supplies its physical-color complement gap, not the whole joint packet.

There is also an exact algebraic kernel issue. The old filling coefficients interpolate the full twist modulo \(P_0\) on complete main targets. At an equal-color moving box, the relation is \(P_s\) and the crossing is \(R_s\). Its expansion in the still valid polynomial basis \(L_1,\ldots,L_N\) has parameter-dependent coefficients. The fixed-power crossing bound gives polynomial coefficient mass on compact pre-resonance disks, but does not prove that these coefficients are the old complete ones or that their full Fourier endpoint proof is unchanged.

For example, at \(N=2\), \(q=i\), \(P_0=z^2\), and the full complete crossing is
\[
 R_0=e^{i\pi/4}(1+iz/4),\qquad
 R_0^2=i-z/2\pmod{P_0}.
 \tag{26}
\]
At the moving node \(z_0(s)=2\sin\pi s\), the actual full square has value
\[
 R_s^2(z_0(s))=e^{i\pi(1+s)^2/2},
 \tag{27}
\]
whereas the old canonical full-square polynomial evaluates to \(i-\sin\pi s\). They differ for generic \(s\). Even allowing the changed common Cartan scalar does not repair the old stripped coefficients: the old stripped square \(1+iz/2\) evaluates to \(1+i\sin\pi s\), while the actual stripped value at this node is one.

Thus an exact moving filling functional, or an equivalent insertion-compatible comparison preserving all paired currents, remains a required input. In an opposite-color order the reference relation and crossing are constant up to the known bounded scalar, but a general diagram can also contain equal-color boxes. They cannot be silently excluded.

If both the joint corridor packet and the actual moving filling functional are proved, the old small-slope saddle analysis can be made uniform in the microscopic parameter. Its limiting exponent at \(s=0\) is already the original marked filled hyperbolic volume. That identification must be inherited with its actual primitive slopes and normalization; neither (25) nor a supremum bound proves it for a new moving filled scalar by itself.
