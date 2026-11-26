# Adjacent bare components with many rigid boundary branches

Private theorem and proof, 1 November 2026. No repository source is changed. The conclusion enlarges a moving-main-meridian source estimate under an explicit finite structural condition; it does not assert a limiting microscopic profile or a displaced-meridian filled-knot theorem.

The new step is a quantitative lower bound for the original reflection surplus at a product junction. It uses one admissible contribution to the original coupled positive probe. It does not add independent cap budgets. Combined with the exact conditional propagation estimate, this closes bare components of arbitrary finite shape when their rigid boundary branches are sufficiently numerous.

The exact inputs are the authoritative workspace notes `actual_main_meridian_source_bounds.md` and `actual_main_meridian_auxiliary_color_gap.md`, published in the c7f758a state, together with the original strict profile and geometry theorems linked there. The conditional transfer is written in `/private/tmp/md-adjacent-bare-hub-conditional-error-propagation.md`. All private paths below are proof inputs, not publication links.

## 1. Positive references and the error invariant

Put \(d=N-1\), \(M=\lfloor d/2\rfloor\), and use the fixed complete Newton basis \(e_r\), full spectral-jet norm \(\|\cdot\|_{\mathrm J}\), and typed relations \(P_s\) or \(P_0\) of the source-bound theorem. Let
\[
 J(u)=\int_0^u\log(2\sin\pi t)\,dt,\qquad
 g(u)=J(2u)-4J(u),\qquad G_0=g(1/4).
 \tag{1}
\]
An original positive branch profile \(f_Q\) has intrinsic pressure
\[
 \Omega_Q=\max_{0\le u\le1/2}\{f_Q(u)+g(u)\}.
 \tag{2}
\]
Every absolute constant accumulated inside the branch is included in \(f_Q\).

We use positive comparison polynomials with these original profiles. For an L branch with rigid profile \(g+c\), choose
\[
 Q^0_N=e^{Nc}h_N,\qquad
 h_N=\sum_{r\le M}\frac{N^2S_{2r}}{S_r^4}e_r.
 \tag{3}
\]
For a bare output, define its reference recursively by the original complete product and reversal,
\[
                  Q^0_{v,N}=T_0\prod_i^{*_0}Q^0_{i,N}.
 \tag{4}
\]
These are nonnegative-coefficient comparison polynomials. They are not asserted to be identical to the finite physical subtree coupons. Their coefficient actions are the original boundary profiles: (3) is the rigid-profile identity with its absolute constant, and the positive Newton Laplace principle makes (4) the original constrained product action followed by output complementation. In particular every reference has the correct intrinsic pressure (2). The usual strict interior lattice rounding supplies the coefficient lower rate at any fixed interior output used below. This reference choice avoids an unsupported pointwise comparison to a physical endpoint coefficient that may vanish at one parity.

The invariant for an actual module is an exact decomposition
\[
 Q_{N,s}=C_{N,s}+E_{N,s},\qquad
 [e_r]C_{N,s}=0\ (r>M),
 \tag{5}
\]
with
\[
 |[e_r]C_{N,s}|\le e^{No(1)}[e_r]Q_N^0\quad(r\le M),
 \qquad
 \|E_{N,s}\|_{\mathrm J}
       \le e^{N(\Omega_Q-\gamma_Q+o(1))},\quad\gamma_Q>0.
 \tag{6}
\]
All bounds are uniform on \(|s|\le R<1\), over the original finite auxiliary-color cube, and over fixed half-twist choices. The comparison keeps the original low-coordinate profile, rather than replacing an A branch by a rigid leaf.

For every decorated L branch the invariant starts with the rate gap \(2G_0\). Indeed, if its input has spectral rate \(c\), the actual decorated theorem gives low coefficients at most \(e^{N(c+g+o(1))}\) and high coefficients at most \(e^{N(c+o(1))}\). Take \(C\) to be its low-coordinate part. Equation (3)'s sine-factorial rate gives the first inequality in (6). Every high basis element has polynomial full-jet norm, so the high-coordinate remainder has rate at most \(c=\Omega_L-2G_0\). Thus
\[
                         \gamma_L=2G_0
 \tag{7}
\]
is valid as a rate statement, with a uniform \(o(1)\). This also applies to an ordinary original leaf. A flagged junction can therefore restore (7) after accepting arbitrary already-established spectral input budgets.

## 2. The exact pressure surplus and its conditional use

Let a bare junction have children with original profiles \(f_i\) and pressures \(\Omega_i\). Write \(A=\prod_iQ_i\) for its unturned product, \(Q_v=T(A)\), and define
\[
 \Omega_A=\max_{u\le1/2}\{f_A(u)+g(u)\},\qquad
 \Omega_v=\max_{u\le1/2}\{f_A(1-u)+g(u)\},\qquad
 \Delta_v=\Omega_v-\sum_i\Omega_i.
 \tag{8}
\]
The positive references satisfy the exact odd-node identity
\(A_N^0(-2)=\prod_iQ_{i,N}^0(-2)\). High Newton factors vanish there, low factors are positive, and their weighted positive sums have rates \(\Omega_A\) and \(\Omega_i\). Hence
\[
                       \Omega_A=\sum_i\Omega_i.
 \tag{9}
\]
This is an identity at the common intrinsic probe of this unturned product. It does not assert additivity at an arbitrary boundary cut of a closed diagram.

The original unsquared product equations give \(f_A'\ge f_{hh}'\), strictly when the last product has an A child. Since \(f_{hh}(u)=f_{hh}(1-u)\), integration shows \(\Delta_v\ge0\), with strictness if an A child is present or the junction has at least three inputs. The two-L-input exception has \(\Delta_v=0\).

For completeness, the precise transfer of (6) is as follows. Define
\[
 C_v=\Pi_{\mathrm{lo}}\mathscr T_s\prod_i^{*_\sigma}C_i,
 \qquad E_v=Q_v-C_v.
\]
The all-parity low-array Fourier comparison preserves the reference majorant in (6). The high output of the all-clean product has spectral rate at most \(\sum_i\Omega_i\). If a nonempty set \(S\) of inputs is replaced by errors, signed quotient folding gives raw rate at most \(\sum_i\Omega_i-\sum_{i\in S}\gamma_i\). High-output extraction has only polynomial cost; low-output extraction and reconstruction together cost at most \(2G_0\). Consequently, if \(\gamma_*\) is the smallest child gap,
\[
 \|E_v\|_{\mathrm J}
 \le\exp N\left\{\Omega_v-
       \min(\Delta_v,\Delta_v+\gamma_*-2G_0)+o(1)\right\}.
 \tag{10}
\]
Every retained type scalar is bounded on the disk. This proves the conditional inequality without assuming that a positive child gap automatically pays for the next turn.

## 3. A quantitative coupled-source lower bound

Suppose the bare junction has at least \(k\ge4\) L-type children, with profiles \(g+c_1,\ldots,g+c_k\). Other children may have arbitrary fixed strict L/A profiles and their own intrinsic pressures. Put \(m=k+1\), and define
\[
 \varepsilon_k=m\left[
 J\left(\frac14+\frac1m\right)+
 J\left(\frac14-\frac1m\right)-2J\left(\frac14\right)\right].
 \tag{11}
\]
Then the original pressure satisfies
\[
                  \boxed{\quad \Delta_v\ge2G_0-\varepsilon_k.\quad}
 \tag{12}
\]
The lower bound is independent of the other children's profiles and sizes. Their intrinsic constants are retained on both sides.

Here is a finite-source proof. The pressure \(\Omega_v\) is the rate of the original positive intrinsic probe
\[
                    \phi_0\left(h_N\prod_iQ^0_{i,N}\right).
 \tag{13}
\]
Work along odd levels to prove an identity or inequality of the parity-independent classical actions. In (13), choose one Newton term with index nearest \(N/4\) from each of the \(k\) indicated L references and from the one intrinsic probe leaf. The latter is a device already present in the definition of \(\Omega_v\); it is not an added physical component. From every remaining child choose a low index nearest one of its intrinsic maximizers \(\beta_i\in(0,1/2)\). Such an interior index is available by the original strict probe geometry. The reference coefficient there has rate \(f_i(\beta_i)\), while a quarter-index coefficient in an L reference has rate \(c_i+G_0\).

All chosen indices are low. Their pair sums are less than \(N\) for sufficiently large levels, and the \(m\) quarter indices alone have total larger than \(N\), since \(m\ge5\). They therefore lie in the original positive closed-hub support. The whole contraction at this boundary tuple retains its internal state constraints.

To lower-bound its exact trace, expand the selected Newton product at \(z=-u-u^{-1}\). A low factor of index \(n\) has Laurent coefficient at exponent \(r\)
\[
 a_r^{(n)}=\frac{S_{2n}}{S_n^2S_{n+r}S_{n-r}},
 \qquad
 \frac1N\log a_r^{(n)}
 =b_{n/N}(r/N)+O(\log N/N),
 \tag{14}
\]
where
\[
 b_u(t)=J(2u)-2J(u)-J(u+t)-J(u-t),\qquad b_u(0)=g(u).
 \tag{15}
\]
All these Laurent coefficients are nonnegative, symmetric and unimodal. Let \(a_r\) be their convolution. At odd levels the exact Fourier trace has nonnegative alias contributions, so the interval-tail inequality gives
\[
 \phi_0\left(\prod e_{n_i}\right)
    \ge N^2(a_{N-1}-a_{N+1})
    \ge N^{2-B'}a_{N-1},
 \tag{16}
\]
where \(B'\) is the fixed total number of incident factors, including the probe. No asymptotic derivative of a coefficient is being assumed.

In the positive convolution coefficient \(a_{N-1}\), distribute the exponent \(N-1\) as equally as possible among the \(m\) quarter-index factors and put exponent zero on every other factor. Since \(1/m<1/4\), this gives legitimate integer exponents for large \(N\). Formula (14) then gives the trace lower rate
\[
 m\,b_{1/4}(1/m)+\sum_{i\ \mathrm{other}}g(\beta_i).
\]
Including the previously chosen reference coefficients in (13) gives
\[
 \Omega_v\ge
 \sum_{i=1}^{k}c_i+
 \sum_{i\ \mathrm{other}}\Omega_i+
 m\bigl[G_0+b_{1/4}(1/m)\bigr].
 \tag{17}
\]
Subtract \(\sum_i\Omega_i=\sum_{i=1}^k(c_i+2G_0)+\sum_{\mathrm{other}}\Omega_i\). Because \(m=k+1\), the difference is exactly \(2G_0-\varepsilon_k\), proving (12).

This construction is a single valid lower contribution to the coupled positive probe. It has not independently optimized incompatible shared boundary states. In particular (17) does not contradict the earlier warning against arbitrary additive cap budgets.

On \((0,1/2)\), \(J''(x)=\pi\cot(\pi x)>0\). Thus \(\varepsilon_k>0\), and Taylor expansion gives
\[
                     \varepsilon_k=\frac\pi{k+1}+O((k+1)^{-3}).
 \tag{18}
\]
An explicit bound, requiring no asymptotic estimate, is
\[
 \varepsilon_k\le
 \frac{\pi\sec(2\pi/(k+1))}{k+1},\qquad k\ge4.
 \tag{19}
\]
Indeed, the central second difference is the integral of \(J''\) against the symmetric triangular kernel of total mass \((k+1)^{-2}\), and
\[
 \frac{J''(1/4+t)+J''(1/4-t)}2=\pi\sec(2\pi t).
\]
The right side is increasing for \(0\le t\le1/(k+1)<1/4\). In particular, if \(k+1\ge8\),
\[
                 \varepsilon_k\le\frac{\pi\sqrt2}{k+1}.
 \tag{20}
\]

## 4. A stable error rate along a bare component

Cap every maintained child gap at \(2G_0\); this only weakens an upper estimate. Suppose a bare vertex has \(k\ge4\) L children and its children obey (6) with smallest gap \(0<\gamma_*\le2G_0\). Combining (10) and (12) gives
\[
          \min(\Delta_v,\Delta_v+\gamma_*-2G_0)
                         \ge\gamma_*-\varepsilon_k.
 \tag{21}
\]
Thus, whenever the right side is positive, the original low profile and a strictly smaller spectral remainder pass through the next bare junction. The loss of gap is at most \(\varepsilon_k\); it is not an uncontrolled \(2G_0\).

Consider a maximal connected component \(\mathcal U\) of bare hubs in a fixed reduced tree. For a vertex \(v\), let
\[
 b_v=d_v-\deg_{\mathcal U}(v)
 \tag{22}
\]
be its number of boundary incidences. Each incidence is an ordinary original leaf or an edge to a flagged hub. In a rooted evaluation toward any boundary incidence of the component, these supply L-type children, except for at most the one incidence used as the parent of the component root. Hence every vertex has at least
\(k_v=b_v-1\) L children, uniformly over the possible choices of closing root. Nonroot vertices generally have one additional L child; it is simply left among the other children in (12).

Assume \(b_v\ge5\) and the finite path condition
\[
 \max_{\substack{\mathcal P\text{ a simple path}\\\text{in }\mathcal U}}
                 \sum_{v\in\mathcal P}\varepsilon_{b_v-1}<2G_0.
 \tag{23}
\]
Boundary L modules enter with gap \(2G_0\) by (7). Inducting toward the chosen root with (21) proves that an outgoing module at \(v\) has gap at least
\[
 2G_0-\max_{\substack{\mathcal P\text{ a directed path}\\
                        \text{from }v\text{ to its descendants}}}
                  \sum_{w\in\mathcal P}\varepsilon_{b_w-1}>0.
 \tag{24}
\]
Every such directed path is a simple path of the component, so (23) works for every root direction. The coefficient reference at each step is precisely (4), with the original profile. The component is finite, so all polynomial costs and uniform errors remain \(e^{No(1)}\).

A simpler sufficient condition is
\[
                      \sum_{v\in\mathcal U}\varepsilon_{b_v-1}<2G_0.
 \tag{25}
\]
There is also a deliberately coarse integer condition. If \(m=|\mathcal U|\) and
\[
                        b_v\ge\max(8,4m)\quad(v\in\mathcal U),
 \tag{26}
\]
then (20), \(\pi<22/7\), and \(\sqrt2<10/7\) give
\[
 \sum_v\varepsilon_{b_v-1}
 <\frac{220m}{49\max(8,4m)}\le\frac{55}{49}.
 \tag{27}
\]
Catalan's alternating series gives \(G>1-1/9=8/9\). Therefore
\[
 2G_0=\frac{4G}{\pi}>\frac{112}{99}>\frac{55}{49},
 \qquad \frac{112}{99}-\frac{55}{49}=\frac{43}{4851}>0.
 \tag{28}
\]
This proves (25) with an explicit positive margin. It works for a component of arbitrary finite shape and size. It is a sufficient structural condition, not a sharp classification.

A component consisting of a single bare hub need not satisfy (23) or (26): the already proved whole-hub theorem covers every valence at least three. Different components are separated by flagged hubs, which accept the established spectral budgets and restore the L cone and gap (7). Thus each maximal bare component may be either a singleton covered by the published theorem or a component satisfying (23).

## 5. The original geometric rate and the source upper bound

Use the hypotheses of the original strict ordered Conway theorem, including its knot/component and marked framing conditions when a volume interpretation is made. Assume every nonsingleton bare component satisfies (23). At a flagged hub the original action identities are
\[
 f_L(u)=g(u)+c,\qquad c=\sum_i\Omega_i,
 \qquad \Omega_L=c+2G_0.
 \tag{29}
\]
At every bare hub, (4) and the positive compiler give its original profile \(f_Q(u)=f_A(1-u)\) and pressure (8), without replacing that profile by \(g+c\). Equations (6), (21), and (24) therefore give the actual spectral bound at exactly that intrinsic pressure.

A flagged root has normalized source \(\phi_\sigma(p_0\prod_iQ_i)\), with its prescribed typed scalar. The physical coupon \(p_0=R_s^{\epsilon_0}L_{j_0}\), the fixed-valence quotient product, and the trace have polynomial norm cost. The original root action identity is \(F_0=\sum_i\Omega_i\). If no flagged hub exists, expose an existing ordinary leaf and transfer its closing turn by the exact Frobenius adjunction. The remaining outgoing component is controlled in the direction selected by that boundary incidence, and its intrinsic probe is the original \(F_0\). No additional leaf or exponential budget is introduced.

The fixed-metric adjunction and all six physical turn scalars are those of the published compiler. They change a recursively exposed scalar only by recorded bounded factors on \(|s|\le R<1\). The primitive cut still supplies exactly one factor \(H_N(s)\). Consequently, for every fixed \(R<1\),
\[
 \sup_{|s|\le R,\,1\le j_i\le N}
        |\mathcal F_{N,\mathbf j}^{\epsilon}(q^s)|
                 \le\exp\{N(F_0+o(1))\}.
 \tag{30}
\]
All original auxiliary colors and fixed half-twist signs are retained. The bound holds at both parities. The complete-color witness at \(s=0\), \(\mathbf j=(N,\ldots,N)\), is the previously proved nonzero actual packet. Under the same original geometric and two-leaf qualifications, it supplies the matching lower rate. Thus the logarithmic supremum in (30) has limit
\[
                              2\pi F_0=\operatorname{Vol}(Y^\epsilon),
 \tag{31}
\]
where \(Y^\epsilon\) is the original augmented complement with the crossing circles unfilled. This conclusion uses the existing complete lower theorem; it does not establish a lower bound at a displaced main meridian.

## 6. Gaussian localization and what remains separate

The invariant also supplies a fresh canonical angular Gaussian. For an A output, its clean low coefficients are majorized by the original positive reference. The old intrinsic probe has a unique strict interior maximizer \(\beta\in(0,1/2)\) of \(f_Q(u)+g(u)\). On a small fixed interval about \(\beta\), the low Newton strip bound has a uniform quadratic angular loss; on the complementary low-index set the original positive probe has a strict compactness gap. The spectral remainder in (6) has its own strict gap. Canonical Hermite interpolation bounds that remainder on a strip by its J norm times \(\operatorname{poly}(N)e^{N|y|}\), which its gap absorbs after shrinking the fixed strip. Thus
\[
 |Q_{N,s}(2\cos(\vartheta+iy))|
 \le\exp N\{\Omega_Q-c(\vartheta-\pi)^2+Cy^2+o(1)\}
 \tag{32}
\]
for fixed positive \(c,C,y_0\) and \(|y|\le y_0\). This is the same reconstruction proof as the published general-profile Gaussian lemma; it uses the original profile majorant, not a claim that an arbitrary turn preserves a Gaussian. L outputs have their published fresh Gaussian directly.

Condition (23) is independent of the chosen root direction. Therefore each original physical circle can be exposed using the same three typed cases as in the published auxiliary-color gap theorem. In the ordinary-leaf-at-bare case, the remaining canonical output is now an entire bare component controlled by (24), rather than just one hub. It has (32) at its original intrinsic pressure. The root contour then gives the same strict auxiliary-color deficit on every fixed \(|s|\le R<1/2\), at the original augmented action. This is a consequence of the uniform all-root invariant; it does not require reordering open tangles or changing the main cut.

Arbitrary components with too few rigid boundary branches are not settled by this argument. Nor does the source upper bound or auxiliary-color deficit identify a limiting regular main-meridian profile or the smaller volume of a filled knot at displaced meridian. Those require the literal main-color leaf asymptotics and conditioned whole-source or filling analysis. No such extension is inferred here.
