# Meridian profiles and volume with arbitrary trivalent Conway regions

1 November 2026.

This theorem allows arbitrarily large connected regions of trivalent products in the moving-meridian calculation for a Conway knot. The construction is fixed; its twist integers can be chosen independently, with either sign, once their absolute values exceed a fixed threshold. The resulting reduced ADO invariant has a nonzero microscopic meridian profile, and its exponential growth is the volume of the actual knot complement after the auxiliary circles have been filled.

Begin with two-string tangles with four ordered endpoints. Their products are the prescribed stacking operations, their turns are physical quarter-turns, and their final closure is the prescribed cylindrical matching. Keep the original crossing circles, each bounding its twice-punctured crossing disk, and its retained half twist \(\epsilon_i\in\{0,\pm1\}\). The main strands must form one knot component with no additional internal circle. Assume the [strict source condition](actual_conway_all_strict_tree_long_twist_volume.md): there is an assignment of original leaf angles in \((0,1/2)\) for which every retained multiplication gate satisfies
\[
                     \max(x,y)<z<x+y<1.
\tag{V1}
\]
The forced final flat gate is removed with its exact complementary-index relation. For a strict two-leaf construction, retain the knot-producing parity pattern containing a pure leaf; the two-odd-leaf link pattern is excluded.

Collect consecutive products with no intervening physical turn into a product junction. A junction containing an original crossing-circle operator is a circle vertex; an ordinary original leaf is a circle vertex of valence one. A junction without such an operator is bare. The reduced graph is a tree of source operations, with an actual quarter-turn along every edge. This description preserves the ordered tangle construction; it does not assert that arbitrary tangles commute.

For every maximal connected component \(\mathcal U\) of bare junctions, assume at least one of the following:

- \(\mathcal U\) consists of one junction, of any allowed valence;
- every junction of \(\mathcal U\) is trivalent in the full reduced tree, counting branches attached outside \(\mathcal U\) as well as its internal edges;
- \(\mathcal U\) satisfies the component path condition below.

![Two possible trivalent bare components, with all outside attachments included in the degree count.](../book/figures/trivalent-bare-components.svg)

There is no size bound on the second type of component. A higher-valence junction cannot be made trivalent by an artificial binary drawing: the newly drawn edges would be unturned, whereas the proof requires the original physical turns.

For completeness, the third alternative retains the previous larger-valence class. Let \(b_v\) be the number of branches at vertex \(v\) leaving \(\mathcal U\), put
\[
\begin{gathered}
 J(x)=\int_0^x\log(2\sin\pi u)\,du,\qquad
 g(x)=J(2x)-4J(x),\qquad G_0=g(1/4),\\
 \varepsilon_k=(k+1)\left[
 J\left(\tfrac14+\tfrac1{k+1}\right)
 +J\left(\tfrac14-\tfrac1{k+1}\right)-2J(\tfrac14)\right].
\end{gathered}
\tag{V2}
\]
The condition is \(b_v\ge5\) and
\[
 \max_{\mathcal P\text{ a simple path in }\mathcal U}
                 \sum_{v\in\mathcal P}\varepsilon_{b_v-1}<2G_0.
\tag{V3}
\]
The sufficient condition \(b_v\ge\max(8,4|\mathcal U|)\) may be used. Neither (V3) nor this sufficient condition is imposed on a trivalent component. The proof of the path condition is the [component extension](actual_main_meridian_component_extension.md).

## The profile, volume and cusp formulas

Fill every auxiliary circle with its original integer disk slope \(p_i\), so the remaining checked-crossing power is
\[
                            n_i=\epsilon_i-2p_i.
\tag{V4}
\]
The main knot cusp remains unfilled. Denote the resulting knot by \(K_{\mathbf n}\). There is a constant \(B\), depending on the fixed presentation and its parity and component data, such that the statements below hold whenever all independently chosen fixed signed integers satisfy \(|n_i|\ge B\). The threshold is independent of the ratios between their absolute values and independent of the later choice of radius \(R<1\). The integers and the presentation are fixed before the level tends to infinity.

Let \(q_N=e^{\pi i/N}\), and let \(F_N(M)\) be the actual zero-framed reduced ADO invariant of \(K_{\mathbf n}\), normalized to be one on the unknot. Its color is \(\alpha=N-1+s\), and its marked meridian is \(M=-q_Nq_N^\alpha=q_N^s\). If \(w(D)\) is the oriented writhe of the filled diagram in the same checked-braid convention as the integers \(n_i\), set
\[
 a(D)=-w(D)-\sum_i n_i,
 \qquad A_N(s)=q_N^{a(D)s^2/2},
 \qquad H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)},\quad H_N(0)=1.
\tag{V5}
\]
The exact scalar ledger is proved in [the framing and crossing calculation](actual_main_meridian_exact_scalar.md). It includes the physical crossings, the ordered mixed carriers, the turn phases, the primitive cut and the zero-framing correction.

**Theorem.** For the threshold just specified, the filled knot complement is complete hyperbolic. For every fixed \(0\le R<1\), uniformly on \(|s|\le R\) and through both even and odd levels,
\[
 \boxed{\displaystyle
 \frac{F_N(q_N^s)}{F_N(1)}
          =A_N(s)H_N(s)\bigl(1+O_{\mathbf n,R}(N^{-1})\bigr).}
\tag{V6}
\]
The denominator is nonzero for all sufficiently large levels. The whole numerator is uniformly nonzero on this disk for all sufficiently large levels, and
\[
 \boxed{\displaystyle
 \sup_{|s|\le R}
 \left|\frac{2\pi}{N}\log|F_N(q_N^s)|
             -\operatorname{Vol}(S^3\setminus K_{\mathbf n})\right|
                            \longrightarrow0.}
\tag{V7}
\]
The volume is that of the knot complement after all auxiliary fillings, not the larger augmented exterior.

Let \(x_e^{\mathrm{fill}}\) be the generally complex normalized label of physical turn edge \(e\) at the selected filled joint saddle. Then the first correction is
\[
 \frac{F_N(q_N^s)}{F_N(1)A_N(s)H_N(s)}
   =1-\frac{\pi s^2}{N}
                \sum_{e\text{ physical}}\cot(\pi x_e^{\mathrm{fill}})
                   +O_{\mathbf n,R}(N^{-2}).
\tag{V8}
\]
Artificial edges used to resolve a higher-valence product are not in this sum. These are the filled labels, not the complete augmented labels. The [preferred-cusp theorem](actual_main_meridian_preferred_cusp.md) uses the meridian of translation one and the linking-zero preferred longitude; in that marking it gives
\[
                  \tau_K=a(D)+2i\sum_{e\text{ physical}}
                                  \cot(\pi x_e^{\mathrm{fill}}).
\tag{V9}
\]
Consequently
\[
 \boxed{\displaystyle
 \frac{F_N(q_N^s)}{F_N(1)H_N(s)}
             =1+\frac{\pi i s^2\tau_K}{2N}
                            +O_{\mathbf n,R}(N^{-2}).}
\tag{V10}
\]
The geometric cusp calculation applies to the broader strict class. The analytic conclusions here retain the component hypotheses above.

For clarity about the normalization, the full modified-trace invariant is \(\mathcal N_N(M)=d_N(M)F_N(M)\), where
\[
 d_N(M)=i^{N+3}\frac{M-M^{-1}}{M^N-M^{-N}},
 \qquad d_N(1)=\frac{i^{N+3}}N,
 \qquad \frac{d_N(q_N^s)}{d_N(1)}=\frac1{H_N(s)}.
\tag{V11}
\]
Thus (V10) is also the normalized profile of the full invariant. The values at completeness are whole-germ values. No numerator and denominator are separately set to zero.

The proof has two global inputs. The [trivalent component estimate](actual_main_meridian_trivalent_component_bound.md) controls the additional trace terms created by moving the meridian, while retaining all original internal labels. The existing positive source then supplies a conditioned complex wire packet. The final joint Fourier calculation keeps all filling charges together, which is essential when the independently long twists have very different sizes. The sections below verify these interfaces rather than inferring a filled-volume theorem from a component norm estimate.

## 1. Boundary modules and the original action

Write \(F_0\) for the original complete positive action. The original marked geometry gives
\[
                    2\pi F_0=\operatorname{Vol}(Y^\epsilon),
\tag{1}
\]
where the auxiliary circles of \(Y^\epsilon\) are still unfilled. All pressures below refer to that original source. They are not independent cap volumes.

For an effective boundary module with rigid profile \(g+c_i\), retain its full low/high coefficient cone
\[
 |f_{i,N,r}(s)|\le e^{N(c_i+e_N)}
 \begin{cases}
       w_{N,r},&0\le r\le M_N,\\
       1,&M_N<r\le d,
 \end{cases}
 \qquad e_N\longrightarrow0,
\tag{2}
\]
where \(d=N-1\), \(M_N=\lfloor d/2\rfloor\), \(w_{N,r}=e_r(-2)\) on the low range, and \(\log w_{N,r}=Ng(r/N)+O(\log N)\). The cone is uniform over all physical auxiliary colors and every fixed disk \(|s|\le R<1\). The full norm \(\|\cdot\|_{\mathcal J}\) includes values and first normals at the complete Casimir nodes; the high coordinates are never discarded merely because their values vanish there.

For a bare component \(A\) viewed from one boundary output, let \(Q=T(A)\). Its intrinsic pressure is
\[
 \Omega_Q=\Phi_{C(hA^0)}+\sum_i c_i,
\tag{3}
\]
where \(A^0\) is the same complete component with pure effective boundary leaves. The scalar probe \(h\) in (3) determines this intrinsic pressure; it is not a new physical circle. These definitions and the exact coefficient probe are in [the complete coefficient-probe theorem](actual_conway_unflagged_core_probe_bound.md), Sections 1–2, and the action identity is in [the intrinsic-probe geometry](actual_conway_unflagged_probe_geometry.md), Section 4.

## 2. The full component invariant

In fixed Newton coordinates the unchanged pairing is
\(\phi_\sigma(e_re_t)=\mathbf1_{r+t=d}\). A prescribed typed turn is
\[
 T_\gamma=\frac{\gamma_N(s)}{H_N(s)}
                 \mathbf J\operatorname{diag}(W_r(s)),
 \quad
 H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)},
 \quad
 W_r(s)=\prod_{a=1}^{r}
  \left(1-\frac{\sin^2(\pi s/N)}{\sin^2(\pi a/N)}\right).
\tag{4}
\]
Here \(\gamma_N\) is the prescribed \(1\) or \(q^{\pm s^2/2}\), and the quotient parameter \(\sigma\) is \(s,-s\) or zero according to the actual object. In lower-index convention the physical edge is diagonal:
\[
                 (T_\gamma\mathbf J)_{ab}
       =\mathbf1_{a=b}\,\gamma_N(s)\frac{H_N(s)}{W_a(s)}.
\tag{5}
\]
For \(|s|\le R<1\), these weights and their inverses are bounded uniformly over every index and level. Thus a fixed collection of edges has bounded coefficientwise cost against its positive complete majorant. This is stronger and more specific than invoking a norm bound for an arbitrary turn.

For a trivalent component, expand each moving cubic trace into its complete tensor and the additional trace term defined in the component theorem (also called its return tensor); constant-relation vertices have only the complete tensor. The orientation table makes the moving vertices an independent set along physical-turn edges. The [trivalent component theorem](actual_main_meridian_trivalent_component_bound.md), Sections 4–6, proves a fixed \(\delta_{\mathcal U}>0\), independent of the compact disk radius, such that the sum of the absolute values of all terms containing a return, after closing against the full low/high probe, is
\[
            O_R\!\left(e^{N(\Omega_Q-\delta_{\mathcal U}+o(1))}\right).
\tag{6}
\]
The probe and the boundary inputs obey (2); the return comparison is homogeneous in every constant \(c_i\). Finite-state rates use the exact \(d\)-normalized support and uniform \(O(\log N)\) factorial errors. Factors \(\Delta_s\), \(\gamma_N\), and \(H_N/W_r\) alter the constants, not the geometric gap.

In the no-return part, every cubic is the original nonnegative tensor. Equation (5) bounds that part termwise by a constant times the original positive circuit. The complete probe theorem therefore supplies:

- a fixed gap whenever a boundary input or the output probe is high;
- the original positive clean action and its unique strict maximizing state;
- a fixed gap outside any fixed neighborhood of that state.

The probe index at the maximum, denoted \(\beta_Q\), and all effective input indices belong strictly to \((0,1/2)\). **No low restriction is imposed on internal bare–bare edges.** Those edges retain their entire complete support in both the positive reference and the no-return circuit. In particular a complete internal maximum at index one half is allowed.

This gives an exact decomposition
\[
                       Q_{N,s}=C_{N,s}+E_{N,s},
\tag{7}
\]
where \(C\) contains no returns, has low effective boundary indices and low output index, and retains all complete-supported internal labels. If \(Q_N^0\) is the original positive reference polynomial with the boundary constants included, then
\[
 |[e_r]C_{N,s}|\le e^{No(1)}[e_r]Q_N^0\quad(r\le M_N),
 \qquad
 \|E_{N,s}\|_{\mathcal J}
             \le e^{N(\Omega_Q-\delta_Q+o(1))}
\tag{8}
\]
for a fixed \(\delta_Q>0\). The second estimate is an estimate of grouped terms, not a claim about the absolute sum of arbitrary crossing-path expansions. The no-return positive cubic expansion and the absolute return estimate are the specific expansions in which the bounds hold.

The same comparison and error estimates (7)–(8) for a singleton or a path-admissible component are already supplied by [the source-bound theorem](actual_main_meridian_source_bounds.md), Sections 2–4, and [the component path theorem](actual_main_meridian_component_extension.md), Sections 3 and 6. Their stronger all-low internal choice may be retained within those components. Their clean terms still contain the moving low-input higher-valence traces, bounded by the same-level whole-hub comparison; they are not redefined as return-free cubic terms. The new trivalent components use the full-label, return-free clean part just defined.

If a boundary module has an inherited full coefficient-cone loss \(\eta\), replacing \(c_i\) by \(c_i-\eta\) lowers every term of the component probe by the same amount. It lowers both (6) and its no-return majorant. There is no new \(2G_0\) debit. At an intervening circle-decorated module an input full-\(\mathcal J\) loss becomes precisely such a full coefficient-cone loss by the physical coefficient extractor in the source-bound theorem, Section 1, or component extension, Section 6. Multilinearity and a finite telescoping expansion therefore propagate inherited errors across the whole fixed tree.

## 3. Fresh Gaussians, physical colors and exact action accounting

The component invariant gives a fresh Gaussian at \(\Omega_Q\), not merely its norm rate. Choose \(I\Subset(0,1/2)\) around \(\beta_Q\). The clean positive probe localization bounds the weighted coefficient sum with output outside \(I\) by a strict deficit; add it to \(E\). On \(I\), the canonical Newton factors satisfy
\[
 |e_r(-2\cos(t+iy))|
 \le w_{N,r}\exp N\{-c_I t^2+C_I y^2+o(1)\},
\tag{9}
\]
for \(|t|\le\pi\) and a fixed small strip. The probe already contains the factor \(w_{N,r}\), so reconstruction adds no exponential cost. For the remaining canonical polynomial, full Hermite interpolation gives
\[
 |E(-2\cos(t+iy))|
        \le N^C e^{N|y|}\|E\|_{\mathcal J}.
\tag{10}
\]
Shrink the strip and the Gaussian constant so the fixed deficit absorbs \(|y|\) and \(ct^2\). This proves
\[
 |Q_{N,s}(-2\cos(t+iy))|
  \le e^{N\{\Omega_Q-c_Qt^2+C_Qy^2+o(1)\}}.
\tag{11}
\]
This is the argument of [the spectral propagation theorem](actual_conway_mixed_core_spectral_propagation.md), Section 3, now with (6) supplying the extra moving-return error. It uses only regularity of the output probe index; it never needs low internal bare indices.

At a circle-decorated module, actual fixed \(R_s^\epsilon L_j\) and its physical coefficient extractor give (2), with the sum of the children's assigned pressures as its constant. Its fresh Gaussian follows from the corresponding low-index reconstruction. A fixed crossing power \(R_s^n\), positive or negative, has polynomial canonical norm on \(|s|\le R<1\), so exactly the same cone estimate holds, with constants allowed to depend on the fixed \(n\). This fixed-power input is proved in the component extension, Section 6, and the direct crossing trace, Section 7. The exponent assigned to the module does not grow with \(n\).

The mutual induction alternates circle-decorated modules with whole maximal bare components. Every boundary input of a maximal bare component is an ordinary or decorated rigid module; an adjacent bare output is not reset to \(g+c\), because the entire connected component has already been grouped. At a decorated junction the rigid constant is the sum of the actual child pressures. At a bare component (3) is its original coupled intrinsic action. The root identity
\[
                             F_0=\sum_a\Omega_{Q_a}
\tag{12}
\]
when exposed at a marked circle is the original rigid-profile identity, not an independent sum of capped components. It is [the intrinsic-probe geometry](actual_conway_unflagged_probe_geometry.md), Section 4, equations (8)–(9).

The source upper bound on every \(R<1\) follows with this exact action. The auxiliary-color gap on every \(R<1/2\) also follows. To expose an original circle, use the exact typed adjunction
\[
 \langle T_{\gamma_1}f,g\rangle
       =\frac{\gamma_1}{\gamma_2}
                    \langle f,T_{\gamma_2}g\rangle,
\tag{13}
\]
which retains all normal coordinates and all prescribed scalar ratios. The three cases in [the auxiliary-color gap theorem](actual_main_meridian_auxiliary_color_gap.md), Section 5.3, remain exhaustive. For an ordinary leaf at a bare junction, the remaining output is now the whole maximal bare component, not necessarily a single junction. Its pressure is the original closure with that existing leaf, and (11) supplies its fresh Gaussian. Reorienting the recursive evaluation does not change the trivalent condition or the path criterion, and does not add a physical probe leaf.

For a marked circle, the remaining raw polynomial is a product of canonical branches satisfying (11), so its pressure is (12). For an ordinary leaf at a marked junction it is one decorated module with the same original budget. Thus the paired-grid contour in that note, Sections 1–4, applies unchanged to every original physical color, uniformly over the other colors. The radius restriction \(R<1/2\) belongs to that unwrapped auxiliary-color contour. It is not needed for the direct joint filling argument below. The single primitive main-cut factor and the exact framing/adjunction phases remain outside; they do not change these exponential losses.

## 4. The clean complete window has two kinds of edge regularity

Now retain fixed crossing powers \(n_v\) at all original circle vertices. The original positive complete source has a unique strict maximizer. Its positive expansion first contracts each complete circle trace and then resolves each bare tensor, exactly as in [the grouped wire-packet theorem](actual_main_meridian_grouped_wire_packet.md), Sections 2–3. At a circle vertex the incidence indices are low, and its node formula has nonnegative summands:
\[
 \phi_0\left(L_N\prod_{e\sim v}e_{n_e}\right)
       =N\sum_{r=0}^{N-1}\prod_{e\sim v}e_{n_e}(c_r),
\tag{14}
\]
with the same-level comparison to the value at \(-2\) in that note, equations (14)–(15). This is an exact positive expansion of the original pure source, including both parities. At its strict optimum all circle-incidence labels are in a fixed compact interval in \((0,1/2)\): equivalently their boundary profiles are the original \(g\), whose endpoint atoms exclude both endpoints. Conditional elimination of the hidden circle variables is strict and analytic, with phase \(\sum_{e\sim v}g(x_e)\).

For bare–bare edges only the following is needed:
\[
                    x_e^*\in(0,1).
\tag{15}
\]
Strict gate inequalities give this and all bulk factorial arguments. An internal label may equal or exceed one half. The two-adjacent-trivalent example already has a maximum at half, so imposing a strict low window there would remove part of the leading source.

At a trivalent bare vertex, strict complete pair support gives
\[
 x_1+x_2<1,\quad x_1+x_3<1,\quad x_2+x_3<1,
 \qquad x_1+x_2+x_3<\tfrac32.
\tag{16}
\]
Choose the fixed regular window small enough to preserve these inequalities with a margin. Then the raw degree of \(F=e_{n_1}e_{n_2}e_{n_3}\) is less than \(2N-1\) for all large \(N\). Divide once:
\[
                F=P_0Q+R_0,\qquad \deg Q\le N-2.
\]
In the moving quotient \(P_\sigma=P_0+\Delta_\sigma\), its remainder is \(R_0-\Delta_\sigma Q\), whose coefficient of degree \(d=N-1\) is unchanged. Therefore
\[
          \phi_\sigma(e_{n_1}e_{n_2}e_{n_3})
             =\phi_0(e_{n_1}e_{n_2}e_{n_3})
\tag{17}
\]
**exactly** throughout this physical window, for every parameter, including all normal specializations. This replaces the all-low bare trace lemma at every new trivalent vertex. No angular variable occurs in this equality. For singleton higher-valence components and path-admissible components use their existing regular low-window trace comparison; their exponentially small errors remain as before.

The global reduction has the following order. First discard the grouped component errors from Sections 2–3. In the remaining contraction, compare each fixed circle trace against its same-level complete positive circle trace by the bound in the grouped-packet note, Section 4, equation (18). Within each new trivalent component, return-free bare tensors are already complete and positive. Within a previously treated higher-valence component, the same-level whole-hub trace comparison supplies the corresponding positive domination before its regular moving-to-complete replacement; its low-input return terms have not been silently discarded. The original unique strict positive state gives a fixed gap outside its retained-edge neighborhood. On that neighborhood apply (17), or the existing higher-valence regular trace comparison where relevant. Finally expand the complete bare tensors in their original positive binary resolution and discard the complement of the primitive regular box. Positivity and strict compactness bound this last projection, including all hidden coordinates. The result is an absolute error
\[
       O_{R,\mathbf n}\!\left(N^A e^{N(F_0-\eta_0)}\right),
                  \qquad\eta_0>0.
\tag{18}
\]
The loss may be chosen independently of \(R<1\) and of the sizes of the fixed \(n_v\). Return losses, complete high-boundary/probe losses, and original compact-complement losses are geometric. The disk, the fixed powers, and the scalar factors affect the constants and the starting level. The comparison with the filled exponent is made only after the joint Fourier calculation in Section 6.

## 5. Primitive lattice and complex angular packet

Use the original ordered positive binary resolution at a bare vertex of valence \(D\). It has \(D-3\) hidden variables and \(D-2\) nontrivial gates. Thus the exact primitive lattice dimension and number of gates remain
\[
 K=E+\sum_{v\text{ bare}}(D_v-3),\qquad
 G=\sum_{v\text{ bare}}(D_v-2).
\tag{19}
\]
At a trivalent vertex there is no hidden variable and one gate. Its third covariant label gives the exact output \(d-n_3\); the offset \(-1\) is retained. Allowing a physical edge across half changes neither the lattice nor its index offsets. The regular window is an entire integer box inside the original strict support, at both parities.

The exact finite packet is the same expression as the grouped-packet note, equation (4): complete positive gate coefficients, circle-incidence factors \(e_{n_e}(-2\cos\tau_v)\), and diagonal physical edge factors \(\gamma_eH_N/W_{n_e}\). The only change is that its box allows full-bulk bare–bare labels. Its zero-angle phase is
\[
 \mathcal A(\mathbf y,0)
   =\sum_{g\text{ bare}}m(x_g,y_g,z_g)
       +\sum_{v\text{ circle}}\sum_{e\sim v}g(x_e).
\tag{20}
\]
The exact positive conditional elimination proves that its maximum is the original \(F_0\). Every free variable belongs either to a circle-incidence \(g\) term or to a strict bare gate. The gate Hessian is negative definite in its three coordinates. The resulting Hessian on the primitive variables is negative definite. The proof is the original one in [the complete strict packet theorem](actual_conway_general_core_packet_and_gap.md), Sections 1 and 3–5, and the grouped-packet note, Section 3; it does not require all physical edge labels to be low.

The canonical factorial function \(G_N\) supplies every strict gate, with the unchanged affine arguments. Circle-incidence factors use the canonical formula in the grouped-packet note, equation (23). Those factors alone require \(x_e\in(0,1/2)\), and all of them satisfy it. Bare–bare edges enter the physical insertion
\[
 \mathcal I_N(x,s)
  =\frac{G_N(Nx)^2}{G_N(Nx-s)G_N(Nx+s)}
  =1-\frac{\pi s^2}{N}\cot(\pi x)+O_R(N^{-2}).
\tag{21}
\]
This is uniformly holomorphic for \(x\) in any fixed bulk complex tube over \((0,1)\). In particular it is regular at \(x=1/2\), where the displayed first correction vanishes. The exact physical identity \(\mathcal I_N(n/N,s)=H_N/W_n\) is unchanged.

It follows that the interpolated summand is holomorphic on a fixed wire tube and a fixed small angular polydisk, with nonzero analytic amplitude and an \(s\)-independent phase. The tubes are determined by the original strict factorial arguments and the low circle-incidence intervals. They can be fixed independently of \(R<1\); for each such \(R\), the starting level and uniform constants may depend on it. All fixed derivatives obey the same estimates on smaller tubes. In particular, the extension is a complex interpolation statement for exact rows, not an inference from a real-grid ratio.

The finite cotangent contours, their endpoint currents, and the wire saddle deformation in the grouped-packet note, Section 6, therefore apply without change. They give the same nonzero local packet with power \(N^{3(1-H)/2}\), the same separate angular evenness, and
\[
 \Psi(0)=F_0,\qquad
 \Psi_{\tau_v\tau_w}(0)
   =-\frac{\mathbf1_{v=w}}{2\pi}
                        \sum_{e\sim v}\tan(\pi x_e^*).
\tag{22}
\]
Only circle-incidence edges occur in this sum, so every diagonal curvature is strictly positive even if another edge is at or above half. The mixed wire-angle derivatives vanish at zero by exact evenness, so wire elimination adds no hidden term to (22).

For the global strip bound, apply the regular Newton angular estimate only to the same circle-incidence factors. Their coefficients multiply nonnegative complete bare gates and bounded edge weights. The positive zero-angle sum has the original rate \(F_0\). Every circle has at least one incidence, so the result is
\[
 |B_N(\mathbf t+i\mathbf y,s)|
 \le N^A\exp N\{F_0-c\|\mathbf t\|^2+C\|\mathbf y\|^2\}
\tag{23}
\]
on the same fixed small strip around the whole real angular cube, including physical endpoint shifts of order \(1/N\). Cauchy gives every fixed angular derivative on a smaller strip. Bare–bare labels never enter an angular Newton factor, so their crossing half causes neither an angular zero nor a lost Gaussian. This verifies the real-spectator bound used by the joint contour, as well as the local complex saddle expansion.

Finally, the finite Gaussian insertion argument applied to (21) retains
\[
 \frac{B_N(\boldsymbol\tau,s)}
 {\Gamma_{\mathrm{edge},N}(s)B_N(\boldsymbol\tau,0)}
 =1-\frac{\pi s^2}{N}
           \sum_{e\text{ physical}}\cot(\pi x_e(\boldsymbol\tau))
                     +O_R(N^{-2}).
\tag{24}
\]
The sum now explicitly includes any regular high bare–bare edge. The analytic cotangent is finite there. No first coefficient is dropped when passing through half.

## 6. The joint filling transform and its threshold

The input of [the joint filling transform](actual_main_meridian_joint_filling_transform.md), Sections 1–2, is precisely (18), the local packet and (23). Its exact crossing-power contour, finite-charge tail truncation with real spectators, and charge comparison depend on these analytic properties, not on whether a non-circle edge is below half.

For independently long fixed signed \(n_v\), retain all Fourier charges jointly. The proof chooses \(L_v=\lfloor t_0|n_v|\rfloor\), \(y_v=A_0t_0/|n_v|\). The resulting omitted-charge loss is a fixed geometric number; it is not the minimum local \(1/n_v^2\) loss compared with the sum of all filling drops. The exact spectator telescope is unchanged. After the common wire saddle is integrated, the selected joint first charge has a nonzero Gaussian and dominates every other retained charge by the componentwise comparison in that note, Section 4. No local first-alias errors are multiplied before this step.

Here is the radius-uniformity check. The geometric phase \(\Psi\), the wire/angular tubes, the positive curvatures in (22), and the source loss \(\eta_0\) are independent of the chosen compact disk \(R<1\). For formal quotient parameters \(\sigma_v\), the trace proof first works on larger circles \(R<R'<1\) avoiding the isolated sine zeros, then uses the maximum principle on the whole holomorphic trace difference. The coefficients obey
\[
 |U_{\ell-1}(\cos2\pi\sigma_v)|
          \le \ell e^{2\pi R'(\ell-1)}\le\ell e^{2\pi(\ell-1)}.
\tag{25}
\]
Thus increasing \(R\) only changes finite constants and the starting level; it does not change the geometric smallness requirements on \(t_0,A_0\), or on \(1/|n_v|\). The fixed \(\eta_0\) in (18) is absorbed by choosing the slope threshold so the total selected action drop, uniformly \(O(\sum_v|n_v|^{-2})\), is less than \(\eta_0/2\). Because the tree has finitely many circles, a single threshold for every \(|n_v|\) suffices, independently of their ratios and independently of \(R\).

The same marked deformation identifies the selected action with the original smoothly filled knot complement. None of the new estimates changes the primitive signs \(n_v=\epsilon_v-2p_v\), the main cusp, the original cut, or the peripheral framing. The exact outside factor remains
\[
 \widehat\zeta_N=\zeta_{\mathrm{closing},N}\prod_v\rho_{v,N},
 \qquad \Gamma_{\mathrm{edge},N}=\prod_e\gamma_{e,N},
\tag{26}
\]
and the equal-color crossing constants remain separate. The current scalar ledger and preferred-longitude calculation in [the preceding filled-meridian theorem](actual_main_meridian_filled_volume.md), Sections 2 and 7, depend on the actual types and marked edges, not the component path test. They therefore apply to this enlarged class with the same exact scalar \(A_N(s)\), one reduced-cut factor \(H_N(s)\), and the same filled-saddle cotangent correction.

Consequently all hypotheses used to obtain the filled profile, nonzero denominator and volume limit in that note have now been supplied for the class stated above: the complete geometric source, global grouped errors, conditioned complex packet, joint independent-slope transform, and exact geometric/scalar identification. The conclusion is the same fixed-tree, both-parity theorem on every compact \(|s|\le R<1\), with a long-slope threshold independent of \(R\). This completes the proof of the theorem stated above.

## 7. Exact boundary of this extension

No estimate here applies the trivalent return argument to an artificial binary resolution of a higher-valence hub. Such a resolution has unturned complementary-index edges, and adjacent moving returns can occur. The independent-return hypothesis and the low-arm allocation would then fail. Mixed-valence adjacent components outside the path condition remain untreated by this argument.

Nor does (6) assert that every complete internal high-label sector is negligible. Some are leading, and the clean packet deliberately retains them. The small remainder consists of nonempty additional-term sectors, boundary/probe-high sectors, and the actual compact complement of the original strict window. This distinction is required both for the absolute source comparison and for the complex packet.

All constants are allowed to depend on the fixed presentation, its orientation/parity data, and the chosen compact disk where appropriate. Nothing is uniform for trees or filling slopes growing with the level. No source commutativity has been used to infer a tangle isotopy or a different knot complement.
