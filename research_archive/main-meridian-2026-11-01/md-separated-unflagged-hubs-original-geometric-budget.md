# The original geometric budget for trees with separated unflagged hubs

Private derivation, 1 November 2026. No repository source is changed.

This report identifies the scalar budget in the new moving-meridian source induction. The geometry is the already constructed geometry of the original ordered Conway diagram. Its intrinsic probes do not add crossing circles to that diagram. The conclusion concerns the volume of its complete augmented complement, before auxiliary fillings. It does not identify a filled knot's volume from the new upper bound.

## 1. The class and its original complete geometry

Fix a literal ordered cylindrical Conway expression with \(m\ge2\) original leaves and a strict positive reduced state. Keep its actual boundary orders, half-twist signs, auxiliary circles, and marked main cut. At completeness its finite positive source can be organized as a reduced Frobenius tree: collapse internal edges with no turn, retain a turn on each remaining hub-to-hub edge, and mark an original leaf when its edge has odd turn parity. Product hubs have degree at least three. Strictness means that each hub has at most one marked original leaf.

Call a hub flagged if it has this marked leaf, and bare otherwise. Assume that no two bare hubs are adjacent. Equivalently, each nonempty maximal connected region of bare hubs is one hub. There is no bound on a fixed hub's degree, the number of hubs, or the number of ordinary leaves incident to a flagged hub.

This is an organization of the source, not an isotopy assertion about the augmented link. The complete geometry and its marked half-twist extension apply to the original literal expression. They give its original positive action maximum \(F_0\) and
\[
 \operatorname{Vol}(Y^\epsilon)=2\pi F_0,
 \tag{1}
\]
where \(Y^\epsilon\) is the actual complete augmented complement with all auxiliary circles retained. Every admissible retained half-twist pattern has this same complete metric volume.

The existing inputs are the following workspace notes:

- actual_conway_general_strict_mask_geometry.md, especially the complete metric and equation (14);
- actual_conway_general_mask_marked_filling.md, especially the original shaded maps and equation (19);
- actual_conway_rigid_spine_and_flagged_tree_geometry.md, equations (5), (9), and (10);
- actual_conway_unflagged_probe_geometry.md, equations (1), (2), (8), and (9);
- actual_conway_reduced_hub_source_normal_form.md, for strict support and the recursive interface.

All five are in the notes directory. These inputs determine absolute constants, rather than only derivatives of open actions.

## 2. The exact intrinsic recursion

Put
\[
 J(u)=\int_0^u\log(2\sin\pi t)\,dt,\qquad
 g(a)=J(2a)-4J(a),\qquad
 G_0=g(1/4)=\frac{2G}{\pi},
 \tag{2}
\]
where \(G\) is Catalan's constant. On \(0\le a\le1/2\), \(g\) has its unique maximum \(G_0\) at \(a=1/4\), with \(g(0)=g(1/2)=0\).

For a branch \(Q\) of strict type \(L\) or \(A\), let \(f_Q(b)\) be its original positive optimized coefficient action at boundary label \(b\). Its intrinsic pressure is
\[
 \Omega_Q=\max_{0\le b\le1/2}\{g(b)+f_Q(b)\}.
 \tag{3}
\]
The original strict closed positive source supplies an interior maximizer with boundary condition \(X_Q=1\). This is also the state selected when \(Q\) is a satellite of a flagged spine. Thus (3) does not impose an unrelated exterior state.

An ordinary original leaf has \(f_h=g\), constant \(c_h=0\), and
\[
 \Omega_h=2G_0.
 \tag{4}
\]
Every branch of type \(L\) has the rigid profile
\[
 f_L(b)=g(b)+c_L,\qquad \Omega_L=2G_0+c_L.
 \tag{5}
\]

Root the tree at a flagged original leaf, when one exists. At a nonroot flagged hub \(v\), write \(p_v=Th_v\) for its marked coupon and \(Q_1,\ldots,Q_k\) for the other child branches. Their types are \(L\) or \(A\), and \(k=d_v-2\ge1\). Its outgoing branch is
\[
 L_v=T\!\left(p_v\prod_{j=1}^k Q_j\right),\qquad
 c_v=\sum_{j=1}^k\Omega_{Q_j},\qquad
 \Omega_{L_v}=2G_0+\sum_{j=1}^k\Omega_{Q_j}.
 \tag{6}
\]
The absolute normalization can be checked at each attachment. The flagged \(H\)-input and output have parameters \((-u,1,u)\), \((-v,1,v)\), while the selected satellite has parameters \((b,1,b)\). The original unsquared gate equations give
\[
 \frac1u=\frac1v+\frac1b.
 \tag{7}
\]
As the output label \(z\) tends to one, \(v\) tends to infinity, the input tends to the complementary satellite label, and the gate action tends to zero. The new constant is the old constant plus \(g(\beta_Q)+f_Q(\beta_Q)=\Omega_Q\). Iteration proves (6); no integration constant is discarded.

Now consider a bare hub \(v\). Its parent edge leaves \(B_v=d_v-1\ge2\) child branches. All are type \(L\): a child is an ordinary leaf or a flagged hub, because no two bare hubs are adjacent. Write their profiles as \(g+c_1,\ldots,g+c_{B_v}\). For the positive unturned product of \(B\) ordinary leaves define
\[
 \omega_B=\max_{0\le a\le1/2}\{f_B(a)+g(a)\},\qquad
 \widehat\omega_B=\max_{0\le a\le1/2}\{f_B(1-a)+g(a)\}.
 \tag{8}
\]
The unturned product \(A_v=\prod_jL_j\) has profile \(f_{B_v}+\sum_jc_j\). Its outgoing branch \(Q_v=T(A_v)\) therefore has
\[
 \boxed{\displaystyle
 \Omega_{Q_v}=\widehat\omega_{B_v}+\sum_jc_j.}
 \tag{9}
\]
Turning complements the output label, which explains the argument \(1-a\) in (8). At the selected state \(X_{Q_v}=1\), equivalently \(Y_{A_v}=1\). The probe geometry identifies this with the state imposed by its flagged parent.

One must not replace the sum in (9) by \(\sum_j\Omega_{L_j}\). That would add an extra \(2B_vG_0\). The pressure \(\widehat\omega_{B_v}\) already pays for the \(B_v\) effective leaves; only their constants are added.

The complete pressure identities used by the whole-hub estimate are
\[
 \omega_B=2BG_0,\qquad \widehat\omega_2=4G_0,\qquad
 \delta_B:=\widehat\omega_B-2BG_0>0\quad(B\ge3).
 \tag{10}
\]
They are classical identities independent of the moving-meridian estimate. The first follows, for example, from the exact odd-level positive-node evaluation \(h_N(-2)^B=\sum_{r\le M}[e_r]h_N^B\,e_r(-2)\) and its original positive coefficient Laplace principle. The action profiles are parity-independent. For the strict comparison, the unsquared product geometry gives \(f_B'\ge f_2'\), strictly for \(B\ge3\), while \(f_2(a)=f_2(1-a)\). Integrating between \(a\) and \(1-a\) and evaluating at the interior maximizer of the first pressure proves the remaining statements.

Equations (6) and (9) are precisely the proposed analytic recursion. A decorated flagged hub accepts spectral input bounds and produces an \(L\)-coefficient cone with constant equal to their sum. A bare hub accepts these cones and returns a spectral bound at (9). Its next hub is flagged, so no general type-\(A\) branch is reset to a rigid coefficient cone.

## 3. Closing the original source

When a flagged hub exists, expose its original marked leaf \(p_0\). If \(Q_j\) are its other incident branches, the original Frobenius closing scalar and its positive \(H\)-profile are
\[
 \phi\!\left(p_0\prod_jQ_j\right),\qquad
 f_H(z)=g(1-z)+\sum_j\Omega_{Q_j}.
 \tag{11}
\]
The original coefficient-one closing endpoint is \(z=1\). Since \(g(0)=0\), continuity gives
\[
 \boxed{\displaystyle F_0=\sum_j\Omega_{Q_j}.}
 \tag{12}
\]
The closing marked leaf is already included in (11); it is not charged another \(2G_0\). The endpoint belongs to the open-profile computation of the original closed scalar. After its forced closing operation is removed, the original reduced closed state is strict.

If there is no flagged hub and at least one hub, connectedness and separation force there to be exactly one bare hub. It has \(m\ge3\) ordinary leaves. Choose one existing leaf for the closing operation. The original scalar is \(C(hh^{m-1})\), so
\[
 F_0=\widehat\omega_{m-1}.
 \tag{13}
\]
This closing leaf is an original leaf, not a new physical probe. An algebraic change of closing frame for the source bound must retain the actual typed trace and carriers; the classical identity (13) requires no different augmented link.

For the analytic closing-frame change, the fixed-coordinate pairing is especially simple. With \(\mathbf J_{ij}=\mathbf1_{i+j=N-1}\), the exact Frobenius metric is \(\langle f,g\rangle=f^{\mathsf T}\mathbf Jg\) for either quotient relation. Each prescribed physical turn has matrix \(T_\gamma=\gamma H_N^{-1}\mathbf J\operatorname{diag}(W_n)\), so
\[
 \langle T_{\gamma_1}p,A\rangle
 =\frac{\gamma_1}{\gamma_2}\langle p,T_{\gamma_2}A\rangle.
 \tag{13a}
\]
Indeed \(T_\gamma^{\mathsf T}\mathbf J=\mathbf JT_\gamma
=\gamma H_N^{-1}\operatorname{diag}(W_n)\). The two turn types in (13a) are the ones prescribed by the actual paired objects. Their coherent carriers cancel in the composed pairing, and the primitive top moment \(s_x\) is the same for either strand orientation. Thus (13a) retains only the displayed scalar ratio, a bounded power of \(q^{s^2/2}\), with no unrecorded noncentral carrier. This is an adjunction at the actual closing pairing, not arbitrary rearrangement of open physical coupons.

For \(m=2\) there is no hub. The strict reduced source is the \(L/H\) pairing, with
\[
 F_0=\max_{0\le a\le1/2}2g(a)=2G_0.
 \tag{14}
\]
This is the separate two-leaf case. Whether a retained half-twist pattern is a knot is still determined by its actual component test. No one-leaf strict cylindrical source is asserted.

## 4. A root-independent expression

Let \(\mathcal U\) be the set of bare hubs, with degrees \(d_v\), and set \(\delta_2=0\). Then
\[
 \boxed{\displaystyle
 F_0=2G_0(m-1)+\sum_{v\in\mathcal U}\delta_{d_v-1}.}
 \tag{15}
\]
A trivalent bare hub has no excess term. A bare hub of degree at least four has strictly positive excess.

For the count, assume first that a flagged hub exists. Let \(f,u\) count flagged and bare hubs; let \(\ell_f,\ell_u\) count ordinary leaves adjacent to those kinds of hub; and let \(E_{ff},E_{fu}\) count their hub edges. No bare-to-bare edge exists, so
\[
 m=f+\ell_f+\ell_u,\qquad
 E_{ff}+E_{fu}=f+u-1,\qquad
 \sum_{v\in\mathcal U}d_v=E_{fu}+\ell_u.
 \tag{16}
\]
Expand (6), (9), and (12). A leaf adjacent to a flagged hub contributes \(2G_0\), and each flagged-to-flagged edge contributes \(2G_0\). At every bare hub replace \(\widehat\omega_{d_v-1}\) by \(2(d_v-1)G_0+\delta_{d_v-1}\). The total coefficient of \(2G_0\) is
\[
 \ell_f+E_{ff}+\sum_{v\in\mathcal U}(d_v-1)
 =m-1,
 \tag{17}
\]
by (16). All other terms are exactly the excesses in (15). This proves the formula with a flagged root. Equation (13) proves it in the no-flag case, and (14) in the two-leaf case.

Combining (1) and (15) gives
\[
 \operatorname{Vol}(Y^\epsilon)
 =2v_8(m-1)+2\pi\sum_{v\in\mathcal U}\delta_{d_v-1},
 \qquad v_8=4G.
 \tag{18}
\]
This is an equality of the original total action and volume. It is not a cutting of the original manifold into octahedra and independent probe complements.

## 5. What the new upper bound establishes

Assume the two actual typed analytic operations stated after (10), including their specified original closing trace. Induction on the fixed separated-bare-hub tree agrees term by term with (4), (6), and (9). The flagged root has (12), the unflagged single hub has (13), and the two-leaf source has (14). Hence the final exponential upper budget is exactly
\[
 F_0=\frac{\operatorname{Vol}(Y^\epsilon)}{2\pi}.
 \tag{19}
\]
All polynomial costs and the finitely many local \(o(1)\) errors combine into one \(o(1)\) for the fixed tree. This does not discard the six typed turn scalars, the primitive closing trace, or the single final main-cut boundary factor. Their control remains part of the exact analytic compiler. On a fixed disk \(|s|\le R<1\), that retained boundary factor has no resonance zero; its polynomial normalization does not change (19).

Adjacent bare hubs produce a general type-\(A\) intermediate branch, for which this rigid-cone induction is not provided. Also, a uniform upper bound at (19), even with every independent auxiliary color retained, does not identify a filled knot's critical action or prove its moving-meridian localization. Summation of actual filling phases requires further information. No new filled-volume equality is inferred here.
