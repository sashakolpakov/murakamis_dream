# Adjacent product junctions in the main-meridian source bound

1 November 2026.

The [main-meridian source bound](actual_main_meridian_source_bounds.md) allows a product junction with no crossing-circle operator only when the neighboring product junctions carry such operators. This note gives a sufficient condition that permits several junctions without an operator to be adjacent. The condition counts the branches attached to each connected group of these junctions. More attached branches provide a quantitative margin that controls the error introduced by the next turn.

The comparison uses the positive complete-color calculation for the same tangle construction. Every boundary variable remains constrained by its original product and closing equations. In particular, the proof retains the additive constants in the boundary profiles; independently optimized pieces are not assigned a common boundary value after the fact.

The result applies to a fixed finite tree. It includes a bound on the summed contribution of high Newton indices, which is needed when the crossing-circle operators are replaced by fixed crossing powers. That bound remains a comparison with the augmented action. A theorem for the smaller filled-knot exponent requires the additional contour and stationary-phase analysis of the filled source.

## 1. The tree and the sufficient condition

Start with a strict ordered Conway construction in the sense of the [general strict-tree theorem](actual_conway_all_strict_tree_long_twist_volume.md), Sections 1–3. Its leaves represent the prescribed rational pieces. Before auxiliary filling, the corresponding local operators are
\[
 p_i=R_s^{\epsilon_i}L_{j_i},\qquad h_i=T_s(p_i),
 \qquad \epsilon_i\in\{0,\pm1\},\quad 1\le j_i\le N.
 \tag{1}
\]
Here \(R_s\) is the physical crossing operator, \(L_{j_i}\) is the ordinary operator associated with crossing circle \(i\), and \(T_s\) is the physical quarter-turn. The parameter \(s\) changes the main meridian to \(M=q^s\), where \(q=e^{\pi i/N}\). Each operation uses its specified orientation and polynomial coordinates.

Group consecutive products that have no intervening turn into a single product junction. The resulting [reduced source tree](actual_conway_reduced_hub_source_normal_form.md) has a quarter-turn on every edge joining two junctions. A junction is **bare** if it contains no unturned operator \(p_i\). It is **flagged** if it contains one. Strictness permits at most one such operator at a junction. An ordinary external leaf remains a turned operator \(h_i\). Junctions have valence at least three; the two-leaf construction is a separate case already included in the source-bound theorem.

Let \(\mathcal U\) be a maximal connected component of bare junctions. If \(D_v\) is the full valence of a vertex \(v\), define
\[
 b_v=D_v-\deg_{\mathcal U}(v).
 \tag{2}
\]
Thus \(b_v\) counts the incidences that leave this component at \(v\): ordinary external leaves and edges to flagged junctions. It does not count the edges joining bare vertices inside \(\mathcal U\).

The constants in the criterion come from the sine-factorial action
\[
 J(u)=\int_0^u\log(2\sin\pi t)\,dt,\qquad
 g(u)=J(2u)-4J(u),\qquad
 G_0=g(1/4)=\frac{2G}{\pi},
 \tag{3}
\]
where \(G=\sum_{r\ge0}(-1)^r/(2r+1)^2\) is Catalan's constant. For \(k\ge4\), put
\[
 \varepsilon_k=(k+1)\left[
 J\left(\frac14+\frac1{k+1}\right)
 +J\left(\frac14-\frac1{k+1}\right)-2J(1/4)\right].
 \tag{4}
\]

**Component criterion.** Each maximal bare component must satisfy one of the following alternatives:

- It consists of one junction, of arbitrary fixed valence at least three.
- Every \(b_v\ge5\), and
\[
 \eta_{\mathcal U}:=2G_0-
 \max_{\mathcal P\text{ a simple path in }\mathcal U}
                \sum_{v\in\mathcal P}\varepsilon_{b_v-1}>0.
 \tag{5}
\]

Paths consisting of one vertex are included. Condition (5) is independent of the choice of root used to evaluate the tree. A simpler sufficient condition, proved below, is
\[
 b_v\ge\max(8,4m)\quad\text{for every }v\in\mathcal U,
 \qquad m=|\mathcal U|.
 \tag{6}
\]
The first alternative needs neither (5) nor (6): it is the existing whole-junction theorem.

Under this criterion, the source bound extends to the whole construction, uniformly over its original auxiliary colors and on every fixed disk \(|s|\le R<1\). More precisely, the proof preserves each branch's original positive low-index profile and a remainder with a strictly smaller spectral rate. After closing, the total contribution of states with a high retained edge index has a strict exponential loss. Section 7 states the resulting source and volume consequences, and distinguishes them from the separate requirements for a filled invariant.

## 2. Polynomial coordinates, norms, and boundary profiles

Write \(d=N-1\) and \(m_N=\lfloor d/2\rfloor\). The fixed complete Newton basis is
\[
 S_r=\prod_{a=1}^r2\sin\frac{\pi a}{N},\qquad
 c_a=2\cos\frac{(2a+1)\pi}{N},\qquad
 e_r(z)=S_r^{-2}\prod_{a=0}^{r-1}(c_a-z),\quad 0\le r<N.
 \tag{7}
\]
Empty products are one. An index is low when \(r\le m_N\), and high otherwise. These are coefficient ranges used in the proof, not a change to the physical colors.

The same-color polynomial relation is
\(P_s(z)=\mathsf T_N(z)+2\cos(2\pi s)\), where
\(\mathsf T_N(u+u^{-1})=u^N+u^{-N}\). Opposite-color objects use \(P_0\). A canonical polynomial has degree less than \(N\). Its norm is
\[
 \|F\|_{\mathrm J}=
 \max\left\{|F(c_a)|:0\le a\le m_N;       |F'(c_a)|:c_a\text{ is a double root of }P_0\right\}.
 \tag{8}
\]
The derivative entries retain the first normal information at repeated roots. At odd levels the final node \(-2\) is simple and has no derivative entry. Full Hermite interpolation makes (8) polynomially equivalent to the canonical sup norm on \([-2,2]\). It is therefore a norm on the complete polynomial, not merely on its values at distinct nodes.

For the relation appropriate to the input, define
\[
 \phi_\sigma(F)=(-1)^dN^2[z^d]\operatorname{rem}_{P_\sigma}F,
 \qquad \sigma=s\text{ or }0.
 \tag{9}
\]
The fixed metric is exactly
\(\phi_\sigma(e_i e_j)=\mathbf1_{i+j=d}\). The [physical turn theorem](actual_main_meridian_turn_comparison.md) gives
\[
 T_s=\frac{\gamma_N(s)}{H_N(s)}\mathcal R\operatorname{diag}(W_r(s)),
 \qquad \mathcal R e_r=e_{d-r},
\]
\[
 H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)},\qquad
 W_r(s)=\prod_{a=1}^r
  \left(1-\frac{\sin^2(\pi s/N)}{\sin^2(\pi a/N)}\right).
 \tag{10}
\]
The actual orientation determines the scalar \(\gamma_N(s)\in\{1,q^{s^2/2},q^{-s^2/2}\}\). Formula (10) is used in that orientation, with its prescribed carrier. The factors, their inverses, and \(H_N\) are uniformly bounded on each \(|s|\le R<1\).

Three estimates from the [source-bound theorem](actual_main_meridian_source_bounds.md), Sections 1.1–1.4, will be used repeatedly. Quotient multiplication of a fixed number of canonical polynomials has polynomial norm cost; the trace (9) has polynomial cost; and
\[
 \|e_r\|_{\mathrm J}\le N^C
 \begin{cases}
 \exp\{Ng(r/N)+O(\log N)\},&r\le m_N,\\
 1,&r>m_N.
 \end{cases}
 \tag{11}
\]
The constants may depend on the fixed construction and parameter disk, but not on the level or physical colors. These statements keep the full quotient multiplication, including terms that vanish at completeness and reappear when \(s\ne0\).

A branch has a **boundary profile** \(f_Q(u)\): fix its normalized output at \(u\), and maximize its positive complete source action over the remaining variables. Every additive constant accumulated inside the branch is part of this profile. Its intrinsic spectral pressure is
\[
 \Omega_Q=\max_{0\le u\le1/2}\{f_Q(u)+g(u)\}.
 \tag{12}
\]
This pressure is the exponential rate obtained by coupling the branch to the positive Newton norm comparison. The additional test factor in that comparison is not a physical crossing circle.

The [rigid-profile theorem](actual_conway_rigid_spine_and_flagged_tree_geometry.md), Sections 2–3, identifies a class of branches, called type \(L\), whose profiles have the form \(g+c\). Ordinary leaves and branches emerging from a flagged junction have this type. Their pressure is \(c+2G_0\). A turned product emerging from a bare junction has type \(A\); its profile is kept as a function of its output and is not replaced by \(g+c\).

Positive reference polynomials realize these same profiles. For an L branch choose
\[
 Q_N^0=e^{Nc}h_N,\qquad
 h_N=\sum_{r\le m_N}\frac{N^2S_{2r}}{S_r^4}e_r.
 \tag{13}
\]
For a bare output use the complete product and reversal,
\[
                         Q_{v,N}^0=T_0\prod_i^{*_0}Q_{i,N}^0.
 \tag{14}
\]
Their Newton coefficients are nonnegative. The positive source variational principle gives the original boundary profile at every strict interior output, with the usual lattice approximation providing the lower rate. These are comparison polynomials; they need not equal the finite physical branch. This distinction also avoids comparing to a physical endpoint coefficient that can vanish at one parity.

## 3. The local error estimate

Maintain an exact decomposition of an actual branch into a low part and an error,
\[
 Q_{N,s}=C_{N,s}+E_{N,s},\qquad [e_r]C_{N,s}=0\quad(r>m_N),
\]
\[
 |[e_r]C_{N,s}|\le e^{No(1)}[e_r]Q_N^0\quad(r\le m_N),
 \qquad
 \|E_{N,s}\|_{\mathrm J}
       \le e^{N(\Omega_Q-\gamma_Q+o(1))},\quad\gamma_Q>0.
 \tag{15}
\]
All errors are uniform on the fixed disk and physical-color cube. Because the tree is fixed, a finite number of polynomial factors is included in the displayed \(o(1)\).

The physical coefficient extractor for a turn preceded by a circle operator is
\[
 [e_r]T_s(R_s^\epsilon L_jE)
 =\frac{\gamma_N(s)W_{d-r}(s)}{H_N(s)}
       \phi_\sigma(e_rR_s^\epsilon L_jE).
 \tag{16}
\]
The polynomial norm bounds for \(R_s^\epsilon L_j\), quotient multiplication, and (11) give the full coefficient bounds
\[
 |[e_r]T_s(R_s^\epsilon L_jE)|
 \le e^{N(c+o(1))}
 \begin{cases}e^{Ng(r/N)},&r\le m_N,\\1,&r>m_N,
 \end{cases}
 \quad\text{if }\|E\|_{\mathrm J}\le e^{N(c+o(1))}.
 \tag{17}
\]
Thus an L branch starts (15) with \(\gamma_L=2G_0\): its high part has rate at most \(c\), while its pressure is \(c+2G_0\). A spectral deficit in the input of (16) decreases the scalar constant in both lines of (17) by exactly that deficit. This last fact will be important when errors pass from one bare component to another.

Now consider a bare junction with children \(Q_i\). Let \(A=\prod_iQ_i\) be its unturned product and \(Q_v=T(A)\). The two relevant pressures are
\[
 \Omega_A=\max_{u\le1/2}\{f_A(u)+g(u)\},\qquad
 \Omega_v=\max_{u\le1/2}\{f_A(1-u)+g(u)\}.
 \tag{18}
\]
At odd levels \(-2\) is an actual complete node. High Newton factors vanish there and low factors are positive. The exact identity
\(A_N^0(-2)=\prod_iQ_{i,N}^0(-2)\), followed by the positive Laplace principle, gives
\[
 \Omega_A=\sum_i\Omega_i,
 \qquad \Delta_v:=\Omega_v-\sum_i\Omega_i.
 \tag{19}
\]
The equality is between parity-independent classical actions. It does not imply additivity at an arbitrary cut of a closed diagram. The derivative inequality in the [probe geometry](actual_conway_unflagged_probe_geometry.md), Appendix A.2–A.4, gives \(\Delta_v\ge0\). It is strict if the last product has an A child, or if there are at least three inputs. The two-L-input product has \(\Delta_v=0\).

Define the outgoing low part by
\[
 C_v=\Pi_{\mathrm{lo}}T_s\prod_i^{*_\sigma}C_i,
 \qquad E_v=Q_v-C_v.
 \tag{20}
\]
The all-parity low-array comparison in the [source-bound theorem](actual_main_meridian_source_bounds.md), Section 2.5, preserves its positive reference majorant (14). There are two remaining kinds of contribution. The high output of the all-low product has spectral rate at most \(\sum_i\Omega_i\), because extraction against a high \(e_r\) costs only a power of \(N\). If a nonempty set of inputs is replaced by errors, quotient multiplication gives raw rate at most \(\sum_i\Omega_i-\sum_{i\in S}\gamma_i\). High output still costs only a power of \(N\). For low output, extraction and reconstruction use two low Newton factors, and cost at most \(2G_0\), since \(\max g=G_0\). Therefore, with \(\gamma_*\) the smallest child gap,
\[
 \|E_v\|_{\mathrm J}\le
 \exp N\left\{\Omega_v-
       \min\bigl(\Delta_v,\Delta_v+\gamma_*-2G_0\bigr)+o(1)\right\}.
 \tag{21}
\]
This proves the conditional propagation estimate, including the possible cost of the next turn. A positive child gap alone would not suffice.

## 4. A coupled pressure bound from rigid boundary branches

Suppose the bare junction has at least \(k\ge4\) L children with profiles \(g+c_1,\ldots,g+c_k\). The other children may have any fixed strict L or A profiles. Then
\[
                         \Delta_v\ge2G_0-\varepsilon_k.
 \tag{22}
\]
The proof supplies one admissible contribution to the full coupled positive sum. It keeps the other children's intrinsic constants and boundary constraints.

The pressure \(\Omega_v\) is the rate of
\[
                         \phi_0\left(h_N\prod_iQ_{i,N}^0\right).
 \tag{23}
\]
Work along odd levels to prove this inequality of classical actions. Choose the Newton index nearest \(N/4\) in each of the \(k\) indicated L references and in the existing comparison factor \(h_N\). There are \(k+1\) such factors. In every other child choose a low index nearest an intrinsic maximizing index \(\beta_i\in(0,1/2)\). The strict probe theorem supplies this interior index and the positive coefficient lower rate there.

All selected indices are low and their pair sums are less than \(N\) for large levels. The \(k+1\ge5\) quarter indices alone have total greater than \(N\), so the tuple is inside the original positive closing support. No inconsistent boundary assignment has been introduced.

For a low Newton factor, its Laurent expansion at \(z=-u-u^{-1}\) has coefficients
\[
 e_n(-u-u^{-1})=\sum_{r=-n}^{n}a_r^{(n)}u^r,
 \qquad
 a_r^{(n)}=\frac{S_{2n}}{S_n^2S_{n+r}S_{n-r}}.
 \tag{24}
\]
They are nonnegative, symmetric, and unimodal. Their uniform exponential rate is
\[
 \frac1N\log a_r^{(n)}
 =b_{n/N}(r/N)+O(\log N/N),
\]
\[
 b_u(t)=J(2u)-2J(u)-J(u+t)-J(u-t),\qquad b_u(0)=g(u).
 \tag{25}
\]
Let \(a_r\) denote the convolution for the selected product, containing a fixed total of \(B\) factors. The exact odd Fourier trace and the interval-tail estimate of the [source-bound theorem](actual_main_meridian_source_bounds.md), Sections 2.1 and 2.3, imply
\[
 \phi_0\left(\prod e_{n_i}\right)
       \ge N^2(a_{N-1}-a_{N+1})
       \ge N^{2-B}a_{N-1}.
 \tag{26}
\]
This is a finite positive coefficient inequality; it does not approximate the difference by a derivative.

In \(a_{N-1}\), distribute the exponent \(N-1\) equally, up to integer rounding, among the \(k+1\) quarter-index factors. Give exponent zero to every other factor. The assignment is allowed because \(1/(k+1)<1/4\). Combining (25) with the chosen reference coefficients yields
\[
 \Omega_v\ge
 \sum_{i=1}^k c_i+\sum_{i\ \mathrm{other}}\Omega_i
 +(k+1)\left[G_0+b_{1/4}\left(\frac1{k+1}\right)\right].
 \tag{27}
\]
Subtracting \(\sum_i\Omega_i=\sum_{i=1}^k(c_i+2G_0)+\sum_{\mathrm{other}}\Omega_i\) gives exactly (22). This lower bound uses a single feasible contribution to (23). In particular, it does not assume that separately optimized cap values can be added at a shared boundary.

The size of the loss is explicit. Since \(J''(u)=\pi\cot(\pi u)\),
\[
 \frac{J''(1/4+t)+J''(1/4-t)}2=\pi\sec(2\pi t).
 \tag{28}
\]
Integrate this identity against the symmetric triangular kernel for the central second difference. It gives
\[
 0<\varepsilon_k\le
 \frac{\pi\sec(2\pi/(k+1))}{k+1},\qquad
 \varepsilon_k=\frac{\pi}{k+1}+O((k+1)^{-3}).
 \tag{29}
\]
In particular,
\[
                       \varepsilon_{b-1}\le\frac{\pi\sqrt2}{b}
                       \quad(b\ge8).
 \tag{30}
\]

## 5. Propagation along every path in a component

Decrease each maintained gap to at most \(2G_0\), if necessary. Combining (21) and (22) gives
\[
 \min\bigl(\Delta_v,\Delta_v+\gamma_*-2G_0\bigr)
                         \ge\gamma_*-\varepsilon_k.
 \tag{31}
\]
Thus enough rigid inputs allow an adjacent bare junction to pass on the original low profile while losing at most \(\varepsilon_k\) of its error gap.

Orient a maximal bare component toward any one of its boundary incidences. Every nonroot vertex receives all its boundary incidences as L children. At the component root at most one of these incidences is used as the parent. Hence every vertex has at least \(b_v-1\) L children, irrespective of the chosen root. Apply (31) with that number of selected children; any additional boundary child is left among the other inputs in (27).

Boundary L modules begin with gap \(2G_0\). Induction toward the component root gives an outgoing gap at least
\[
 2G_0-
 \max_{\mathcal P\text{ a directed descendant path from }v}
               \sum_{w\in\mathcal P}\varepsilon_{b_w-1}.
 \tag{32}
\]
Every directed path is a simple path of \(\mathcal U\), so (5) makes this positive for every root direction. The component is fixed and finite; its polynomial costs remain \(e^{No(1)}\).

Condition (6) is an elementary sufficient test. If \(m=|\mathcal U|\), then (30), \(\pi<22/7\), and \(\sqrt2<10/7\) give
\[
 \sum_{v\in\mathcal U}\varepsilon_{b_v-1}
 <\frac{220m}{49\max(8,4m)}\le\frac{55}{49}.
 \tag{33}
\]
The alternating series for Catalan's constant gives \(G>8/9\), so
\[
 2G_0=\frac{4G}{\pi}>\frac{112}{99}>\frac{55}{49},
 \qquad \frac{112}{99}-\frac{55}{49}=\frac{43}{4851}>0.
 \tag{34}
\]
This proves the criterion with a definite margin. The path test can be substantially weaker than this convenient valence bound.

For a singleton component, the [whole-junction theorem](actual_main_meridian_source_bounds.md), Sections 3.3–3.4, supplies its positive high-input and high-output gaps. Its two-input exception is covered by the exact cubic support argument there. Thus a singleton requires no boundary-count restriction beyond its original valence and strictness.

## 6. Grouped high-index errors and fixed crossing powers

The preceding norm estimate must be refined to distinguish inherited errors from newly created high indices. This distinction prevents an error from being charged another \(2G_0\) every time it crosses a flagged junction.

For an outgoing L module of constant \(c_v\), use an exact decomposition
\[
 L_v=L_v^{\mathrm{low}}+I_v+H_v.
 \tag{35}
\]
The first term retains only low indices on every retained edge of its subtree, including its outgoing edge. The inherited error \(I_v\) satisfies the full coefficient bounds (17) with \(c_v\) replaced by \(c_v-\eta_v\), for some \(\eta_v>0\). The term \(H_v\) has high outgoing support and coefficient rate at most \(c_v\); by (11), its spectral rate is \(c_v=\Omega_v-2G_0\). At an ordinary leaf there is no inherited error: use its exact low and high projections.

At a flagged junction, expand the input product using the corresponding decompositions. A term with a child error has a strictly smaller spectral rate, because quotient multiplication has polynomial cost. Formula (16) converts that spectral loss into a full coefficient loss in both ranges of (17). These terms form \(I_v\). Apply the same formula to the all-low input term and split its output into low and high ranges, giving \(L_v^{\mathrm{low}}\) and \(H_v\). This supplies (35) without treating a spectral estimate as a coefficient estimate without proof.

Now evaluate an entire bare component. Its estimate is multilinear in its boundary arrays and applies to arbitrary arrays obeying (17). Its original pressure is affine in their scalar constants:
\[
 \Omega_{\mathcal U}(c_1,\ldots,c_b)
       =\Omega_{\mathcal U}(0,\ldots,0)+\sum_{i=1}^b c_i.
 \tag{36}
\]
This follows from the positive reference recursion: multiplying one boundary array by \(e^{Nc_i}\) adds precisely \(c_i\) to every constrained source action. If one input is an inherited error with constant \(c_i-\eta_i\), the whole component estimate therefore loses \(\eta_i\). It is not necessary to subtract \(2G_0\) again.

For the remaining boundary terms, the low parts have the original profile majorants and the high parts begin with gap \(2G_0\). The path proof gives
\[
 Q_{\mathcal U}=Q_{\mathcal U}^{\mathrm{low}}+E_{\mathcal U},
 \qquad
 \|E_{\mathcal U}\|_{\mathrm J}
      \le e^{N(\Omega_{\mathcal U}-\eta_{\mathcal U}'+o(1))},
 \qquad\eta_{\mathcal U}'>0.
 \tag{37}
\]
Here the low term keeps every boundary, internal, and outgoing retained edge low. A newly generated gap may be chosen below (5), or below the singleton gap. Previously inherited losses enter through (36). At the next flagged junction, (16) changes (37) back into the coefficient form required in (35). Since there are finitely many components, a positive minimum remains after all polynomial factors are absorbed.

At the closing root, the coupon and trace have polynomial norm cost. If no flagged junction exists, expose an existing ordinary leaf and use the exact Frobenius adjunction for its turn. The component is then evaluated toward that boundary incidence, which (5) already permits. No new comparison leaf or geometric constant is inserted. The two-leaf case remains the separate source-bound case. It follows that the exact scalar satisfies
\[
 Z_{N,s}=Z_{N,s}^{\mathrm{all\ low}}
                   +O\bigl(e^{N(F_0-\eta)}\bigr),
 \qquad \eta>0,
 \tag{38}
\]
where \(F_0\) is the original augmented complete action. The error is the summed contribution of states with at least one high retained edge. It is not the sum of absolute values of every internal crossing path or every separate return term.

The same argument applies if a circle coupon is replaced by a fixed composable power \(R_s^{n_i}\), for example \(n_i=\epsilon_i-2p_i\). The [fixed-power bound](actual_main_meridian_source_bounds.md), Section 1.3, gives polynomial canonical norm for every such power on \(|s|\le R<1\), retaining its Cartan factor and orientation. Therefore (16)–(17) remain valid with that coupon. Equations (35)–(38) then use the same augmented comparison profiles and the same positive structural margins. Polynomial exponents and the level from which the bounds hold may depend on the fixed integers \(n_i\); the exponential gaps do not require their sizes to be comparable.

For these filled coupons, \(F_0\) in (38) is still the action of the original augmented comparison. The argument has not identified the filled critical action, proved a nonzero filled contribution, or compared this gap with the complete-to-filled volume change. Those are additional steps in a filled-source theorem.

## 7. The source bound, geometric constants, and remaining scope

For the unfilled physical source (1), a flagged branch has
\[
 f_L(u)=g(u)+c,\qquad c=\sum_i\Omega_i,
 \qquad\Omega_L=c+2G_0.
 \tag{39}
\]
A bare branch retains \(f_Q(u)=f_A(1-u)\) and (18). These are the original profile identities, including their absolute constants, from the [rigid-spine geometry](actual_conway_rigid_spine_and_flagged_tree_geometry.md) and [probe geometry](actual_conway_unflagged_probe_geometry.md). At a flagged root, \(F_0=\sum_i\Omega_i\). In the absence of a flagged root, the existing-leaf adjunction gives the original intrinsic probe action. These are coupled source identities, not a volume decomposition into independent pieces.

The exact main-cut normalization supplies one factor \(H_N(s)\), together with the recorded framing and type scalars. Their bounds on each fixed \(R<1\) do not change the exponential rate. Consequently
\[
 \sup_{|s|\le R,\,1\le j_i\le N}
          |\mathcal F_{N,\mathbf j}^{\epsilon}(q^s)|
                    \le e^{N(F_0+o(1))}.
 \tag{40}
\]
Under the original knot, absence-of-internal-component, and marked-geometry hypotheses, the complete-color value at \(s=0\) has the nonzero asymptotic stated in the [source-bound theorem](actual_main_meridian_source_bounds.md), Section 4.6, (T32). The whole source equals its selected core there because the complementary color is zero. This supplies the lower rate in the supremum, so
\[
 \lim_{N\to\infty}\frac{2\pi}{N}
  \log\sup_{|s|\le R,\,1\le j_i\le N}
      |\mathcal F_{N,\mathbf j}^{\epsilon}(q^s)|
       =2\pi F_0=\operatorname{Vol}(Y^\epsilon).
 \tag{41}
\]
The complement \(Y^\epsilon\) is the augmented complement, with the crossing circles unfilled. Both parities are included. For two leaves the same pure-leaf qualification as in that complete source theorem is retained.

The original profile also gives a fresh angular Gaussian for each outgoing A branch. Its low reference has a unique strict interior maximizer \(\beta\) of \(f_Q(u)+g(u)\). Near \((\beta,\pi)\), the low Newton angular action has a strict quadratic maximum; away from it the positive profile has a fixed gap. The remainder in (15) has a spectral gap, which absorbs the polynomial Hermite interpolation cost and its \(e^{N|y|}\) strip growth after the strip is narrowed. Thus
\[
 |Q_{N,s}(2\cos(\vartheta+iy))|
 \le\exp N\{\Omega_Q-c(\vartheta-\pi)^2+Cy^2+o(1)\}
 \tag{42}
\]
for suitable fixed positive constants. This is the reconstruction argument of the [source-bound theorem](actual_main_meridian_source_bounds.md), Section 3.5, using the retained profile. It is not a claim that an arbitrary turn preserves a Gaussian.

Because (5) works for every root direction, one can expose any original auxiliary circle and use the exact three cases in the [auxiliary-color gap theorem](actual_main_meridian_auxiliary_color_gap.md). When the circle is an ordinary leaf at a bare component, the outgoing object is now the entire component controlled above. Its action and Gaussian are still the original ones. The same root contour therefore yields a strict auxiliary-color deficit on every fixed \(|s|\le R<1/2\).

The path condition is sufficient, not a classification of all adjacent bare components. The tree, colors' roles, framing, and every fixed crossing power are fixed before the level tends to infinity. Neither (38) nor (41) alone gives a filled-knot theorem or a limiting main-meridian profile at a displaced parameter. Those conclusions require a conditioned local contraction and, for fillings, the actual parameter-dependent crossing-power contour with its endpoint currents.

## 8. Finite reproduction

The accompanying [direct-crossing reproduction script](../experiments/audit_main_meridian_direct_fillings.py) compares powers of the full polynomial crossing, reduced modulo the physical relation, with the generic root-grid trace and the analytic complete first-normal trace. It includes negative powers and parameter values on both sides of the half-integer collision. A separate rational calculation checks the quadratic joint-charge comparison for unequal signed slopes. These finite checks do not prove the component pressure inequality or an asymptotic source theorem.

With Python and `mpmath` installed, run from the repository root:

```bash
python3 experiments/audit_main_meridian_direct_fillings.py
```

The default output is [the reproduction record](../experiments/main_meridian_direct_fillings_results.json). Use `--output` to choose another location. The optional `--profile-diagnostic` flag repeats the archived local profile scan; it is numerical evidence and is kept separate from the finite identities and exact rational checks.
