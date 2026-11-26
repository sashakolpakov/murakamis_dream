# A moving-meridian source bound when bare hubs are separated by flagged hubs

Private derivation, 1 November 2026. This file does not change a repository source.

The purpose of this result is to close a genuine recursive class of physical sources under the two estimates already proved: the decorated-character coefficient cone and the all-parity whole-hub bound. The exponential constant is the complete augmented action of the original fixed tangle construction. It is not the volume of a subsequently filled knot. No lower bound or strict auxiliary-color loss is asserted.

The analytic inputs are the complete proofs in `/private/tmp/md-deformed-decorated-leaf-coefficient-envelope.md`, `/private/tmp/md-all-parity-unturned-hub-full-cone-and-probe-budget.md`, and `/private/tmp/md-even-level-low-newton-hub-trace-comparison.md`. The original action identities are in `notes/actual_conway_rigid_spine_and_flagged_tree_geometry.md` and `notes/actual_conway_unflagged_probe_geometry.md`. The exact typed source and its cut normalization are in `notes/actual_main_meridian_newton_compiler.md` and `notes/actual_main_meridian_turn_comparison.md`.

## 1. The fixed construction and the statement

Fix a literal strict Conway construction with separately labeled physical leaves, prescribed half-twists, ordered tangle endpoints, and its original reduced cut. A physical leaf is
\[
 p_i=R^{\epsilon_i}L_{j_i},\qquad h_i=T(p_i),\qquad
 1\le j_i\le N,\qquad \epsilon_i\in\{0,\pm1\}.
 \tag{1}
\]
The color tuple is allowed to vary over its entire finite cube. The construction and the half-twist choices are fixed before the level tends to infinity.

Use the reduced product-hub tree of the original construction. A hub is a maximal product junction after internal edges without a turn have been contracted. Every remaining hub-to-hub edge carries a physical quarter-turn. An unflagged external leaf is \(h_i\); a flagged external leaf is its turn, namely the original unturned coupon \(p_i\), with the typed dual identification retained. Strictness gives at most one flagged leaf at each hub. The hubs have degree at least three; the two-leaf case is treated separately below.

Assume the following additional combinatorial condition:

> No edge joins two unflagged hubs.

Equivalently, every maximal connected component of hubs without a flagged leaf consists of a single hub. A hub without a flag is called bare below. Its degree is arbitrary but fixed. A tree may have arbitrarily many bare hubs, and a flagged hub may have arbitrarily many bare-hub descendants. The restriction concerns adjacent bare hubs, not the size or branching of the construction.

Let \(F_0\) be the original complete positive action of the construction, with all original shared-wire constraints and additive constants. In the geometric hypotheses of the strict Conway theorem, the complete augmented exterior satisfies
\[
                    2\pi F_0=\operatorname{Vol}(M_{\mathrm{aug}}).
 \tag{2}
\]
No geometric interpretation is needed for the algebraic bound if only the action is being considered.

Write \(q=e^{\pi i/N}\), \(d=N-1\), and deform the main meridian by \(M=q^s\). Let \(\mathcal F_{N,\mathbf j}^{\epsilon}(q^s)\) denote the actual reduced cut scalar of this auxiliary-colored source, with the prescribed framing and all repeated-root normal data. For every fixed \(R<1\),
\[
 \sup_{|s|\le R}\ \sup_{\mathbf j\in\{1,\ldots,N\}^{H}}
 \left|\mathcal F_{N,\mathbf j}^{\epsilon}(q^s)\right|
 \le \exp\{N(F_0+o(1))\}.
 \tag{3}
\]
The error is uniform over the displayed disk and color cube and over any fixed finite set of half-twist choices. The limit runs through both parities, without a primality restriction. The full modified dimension is not included in this reduced scalar. In the retained normalization it has removable value \(\eta_N/N\) at completeness; its ordinary-color poles occur outside the pre-resonance disk considered here.

## 2. Exact typed algebra needed for the recursion

Let \(\mathsf T_N(z)\) be determined by
\(\mathsf T_N(u+u^{-1})=u^N+u^{-N}\). The equal-color and opposite-color polynomial relations are respectively
\[
 P_s(z)=\mathsf T_N(z)+2\cos(2\pi s),\qquad
 P_0(z)=\mathsf T_N(z)+2.
 \tag{4}
\]
Every coupon is represented by its canonical polynomial of degree less than \(N\), in its specified oriented Hom space. The normalized mixed reference carriers are retained. Serial composition in a fixed compatible type is multiplication followed by reduction modulo its relation in (4).

Use the fixed complete Newton basis
\[
 e_n(z)=\frac{\prod_{r=0}^{n-1}(c_r-z)}{S_n^2},\qquad
 c_r=2\cos\frac{(2r+1)\pi}{N},\qquad
 S_n=\prod_{r=1}^n2\sin\frac{\pi r}{N}.
 \tag{5}
\]
For either relation define
\[
 \phi_\sigma(F)=(-1)^dN^2[z^d]\operatorname{rem}_{P_\sigma}F,
 \qquad \sigma\in\{0,s\}.
 \tag{6}
\]
The exact pairing is unchanged by the moving relation:
\[
 \phi_\sigma(e_i e_j)=\mathbf1_{i+j=d},\qquad
 \langle f,g\rangle:=\phi_\sigma(fg)
     =\sum_{n=0}^df_n g_{d-n}.
 \tag{7}
\]
This identity includes all first normal coefficients, rather than only evaluation at distinct nodes.

Put
\[
 H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)},\qquad
 W_n(s)=\prod_{r=1}^n
       \left(1-\frac{\sin^2(\pi s/N)}{\sin^2(\pi r/N)}\right).
 \tag{8}
\]
The value at zero is removable. If \(J e_n=e_{d-n}\), every physical turn in fixed polynomial coordinates is
\[
 \mathscr T_\gamma=\frac{\gamma_N(s)}{H_N(s)}
                      J\operatorname{diag}(W_n(s)).
 \tag{9}
\]
The scalar is \(q^{-s^2/2}\) on \(\operatorname{End}(++)\to\operatorname{Hom}(-+,+-)\), \(q^{s^2/2}\) on its next forward turn to \(\operatorname{End}(--)\), \(q^{s^2/2}\) on \(\operatorname{End}(--)\to\operatorname{Hom}(+-,-+)\), and \(q^{-s^2/2}\) on its next forward turn to \(\operatorname{End}(++)\). It is one on the two opposite-color endomorphism turns. These are physical types, not six independently chosen scalar algebras.

The identity \(W_nW_{d-n}=H_N^2\) shows that successive turns cancel their paired factors; the corresponding successive \(\gamma\)'s also cancel. The resulting dual endomorphism is the same polynomial in the dual Casimir. This is the typed meaning of canceling a double turn in the reduced source. It does not assert an isotopy of the underlying tangles.

There is also an exact pairing identity, useful at the root. Because the matrix of (7) is \(J\), (9) is self-adjoint for (7). For any two applicable turn types,
\[
 \langle\mathscr T_{\gamma_1}f,g\rangle
   =\frac{\gamma_1(s)}{\gamma_2(s)}
        \langle f,\mathscr T_{\gamma_2}g\rangle.
 \tag{10}
\]
Indeed both sides, after their displayed scalar, equal
\(H_N^{-1}\sum_nW_n f_n g_n\). Thus an exposed closing turn can be transferred across the pairing without discarding its scalar. Associativity inside compatible carrier coordinates, cancellation of successive typed turns, and (10) perform the source regrouping. Any resulting root scalar \(\chi_N(s)\) is the product of the explicitly specified turn ratios. It and its inverse are bounded uniformly on every \(|s|\le R<1\), because the tree has fixed size. The unturned physical coupons retain their own crossing scalar, loop pivot, and local framing throughout.

This justifies the use of the same reduced labeled tree for the deformed source. Internal products and turns still use their actual types and carriers. We do not replace the physical quarter-turn by an algebra automorphism, and we do not infer any tangle isotopy from the scalar rearrangement.

## 3. The two analytic invariants

Let \(\|\cdot\|_{\mathrm J}\) be the complete spectral norm recording values at every distinct root of \(P_0\) and first derivatives at its double roots. Canonical sup, Chebyshev-coefficient, and full spectral norms are polynomially equivalent at degree less than \(N\). For a fixed number of factors, exact Chebyshev folding gives
\[
 \left\|\operatorname{rem}_{P_\sigma}\prod_aF_a\right\|_{\mathrm J}
       \le C_RN^C\prod_a\|F_a\|_{\mathrm J},\qquad
 |\phi_\sigma(F)|\le C_RN^C\|F\|_{\mathrm J}.
 \tag{11}
\]
The second bound is for a canonical polynomial, and reduction is included by the first when needed. These statements preserve the signed polynomial product, including its return terms. They are not absolute estimates on individual moving multiplication coefficients.

Define
\[
 J_0(u)=\int_0^u\log(2\sin\pi v)\,dv,\qquad
 g(u)=J_0(2u)-4J_0(u),\qquad G_0=g(1/4).
 \tag{12}
\]
The use of \(J_0\) here avoids confusing this scalar function with the reversal matrix. A type-L module is assigned a constant \(c\) when its actual coefficients satisfy
\[
 |[e_r]L_N(s)|\le
 \begin{cases}
 \exp\{N(c+g(r/N)+o(1))\},&0\le r\le\lfloor d/2\rfloor,\\
 \exp\{N(c+o(1))\},&\lfloor d/2\rfloor<r<N.
 \end{cases}
 \tag{13}
\]
Its accompanying spectral budget is
\[
                 \|L_N(s)\|_{\mathrm J}
                  \le\exp\{N(c+2G_0+o(1))\}.
 \tag{14}
\]
A type-A module needs only its intrinsic spectral budget
\[
                 \|Q_N(s)\|_{\mathrm J}
                  \le\exp\{N(\Omega_Q+o(1))\}.
 \tag{15}
\]
We do not assert (13) for a general A module.

The first input theorem is the decorated-character estimate. The physical \(p_i=R_s^{\epsilon_i}L_{j_i}\) has polynomial canonical norm, uniformly over \(j_i\), \(|s|\le R<1\), and the fixed half-twists. If \(\|E_N\|_{\mathrm J}\le\exp\{N(c+o(1))\}\), then
\[
            D_i[E_N]=\mathscr T\bigl(p_i*_\sigma E_N\bigr)
 \tag{16}
\]
satisfies (13) and (14) with this same \(c\). The exact coefficient is
\(\gamma_NW_{d-r}H_N^{-1}\phi_\sigma(e_rp_iE_N)\). Thus the theorem uses the actual loop, crossing, carrier, and paired turn, not a formal replacement of a high coordinate by an alias. In particular an ordinary leaf \(h_i=D_i[1]\) has \(c=0\) and \(\Omega_{h_i}=2G_0\).

The second input theorem applies to one bare hub with \(B\ge2\) L-type children. Let \(f_B\) be the original positive coefficient action of the unturned product \(h^B\), and put
\[
 \widehat\omega_B=max_{0\le u\le1/2}
                      \{g(u)+f_B(1-u)\}.
 \tag{17}
\]
If the children have constants \(c_1,\ldots,c_B\) in (13), then
\[
 Q=\mathscr T\bigl(L_1*_\sigma\cdots *_\sigma L_B\bigr),
 \qquad \|Q\|_{\mathrm J}
 \le\exp\left\{N\left(\sum_bc_b+\widehat\omega_B+o(1)\right)\right\}.
 \tag{18}
\]
This is the whole-hub theorem at both parities. Its low-input, low-output part has the old positive probe majorant, and every other sector has a strict deficit. The proof keeps the signed hub intact before taking absolute values. It includes the special \(B=2\) cases, where one high input and a high output can have a return term. The strict pressure inequality for \(B\ge3\) and the old two-input high-sector estimates are part of that theorem. No extra estimate on a physical auxiliary-color deficit is inferred here.

## 4. Finite recursion and exact action accounting

First assume that there is a flagged hub, and choose its flagged physical leaf as the root. Direct every other hub edge toward that root. Ordinary leaves send their coupons \(h_i\) to their incident hub. Every nonroot flagged hub sends
\[
                  L_v=D_{i(v)}\left[\prod_{w\in\mathcal C(v)}Q_w\right].
 \tag{19}
\]
The children \(Q_w\) can be ordinary L leaves, other flagged L modules, or bare-hub A modules. Assign
\[
             c_v=\sum_{w\in\mathcal C(v)}\Omega_w,
             \qquad \Omega_v=c_v+2G_0.
 \tag{20}
\]
Equations (11) and (16) prove (13)--(14) for this outgoing module whenever the children satisfy their spectral budgets. This step requires no coefficient-profile hypothesis on an A child.

A nonroot bare hub of degree \(d_v\) has \(B=d_v-1\ge2\) children. The separation hypothesis ensures that all these children are ordinary L leaves or flagged L modules. In particular every child has the coefficient cone (13), with a specified constant \(c_w\). Its outgoing module is
\[
 Q_v=\mathscr T\left(\prod_{w\in\mathcal C(v)}L_w\right),\qquad
 \Omega_v=\sum_{w\in\mathcal C(v)}c_w+\widehat\omega_{d_v-1}.
 \tag{21}
\]
Equation (18) proves its spectral budget (15). We do not apply (13) to this A output; when it reaches its flagged parent, (19) creates a new L cone from the spectral budget.

This is a terminating induction: every input in (19) or (21) belongs to a strictly smaller rooted subtree, and the finite tree ends at ordinary leaves. The errors and polynomial losses remain uniform because the number of hubs, their valences, and all fixed twist powers are independent of \(N\). Thus (13)--(15) hold for all modules in the tree, uniformly over all physical color tuples.

These same constants have their original geometric meaning. The rigid-profile theorem gives
\[
 f_{L_v}(b)=g(b)+c_v,\qquad
 \Omega_{L_v}=\max_{0\le b\le1/2}\{g(b)+f_{L_v}(b)\}=c_v+2G_0.
 \tag{22}
\]
Its absolute constant is precisely the sum (20), not a free normalization. At a bare hub the children have the original profiles \(g+c_w\). Optimizing their internal states therefore gives
\[
 f_{A_v}(z)=f_{d_v-1}(z)+\sum_wc_w,
 \quad f_{Q_v}(u)=f_{A_v}(1-u),
 \quad \Omega_{Q_v}=\sum_wc_w+\widehat\omega_{d_v-1}.
 \tag{23}
\]
These are identities of the original positive action with its fixed output. They do not replace the signed child coupons by physical bare leaves. The intrinsic probe in (17) computes an action constant; no new crossing circle or auxiliary color has been inserted.

At the selected flagged root, the exact typed scalar has the form
\[
 Z_{N,\mathbf j}^{\epsilon}(s)
   =\chi_N(s)\,\phi_\sigma\left(
               p_0\prod_{w\in\mathcal C(0)}Q_w\right).
 \tag{24}
\]
The products and the root type are those determined by the compiler; \(\chi_N\) records (10) if root transfers were needed. The root coupon has polynomial norm. Equations (11), (14), and (15) give
\[
 |Z_{N,\mathbf j}^{\epsilon}(s)|
      \le\exp\left\{N\left(\sum_{w\in\mathcal C(0)}\Omega_w+o(1)\right)\right\}.
 \tag{25}
\]
The original root H-profile is
\(g(1-z)+\sum_w\Omega_w\). Its coefficient-one closing endpoint is \(z=1\), at which \(g(0)=0\). The intrinsic probe geometry therefore gives exactly
\[
                         F_0=\sum_{w\in\mathcal C(0)}\Omega_w.
 \tag{26}
\]
There is no additional charge for the distinguished root leaf. Equations (25)--(26) are the required upper bound at the original coupled action.

## 5. The cases without a flagged root

If the reduced tree has hubs but none is flagged, the separation condition forces it to have one hub only. Let its degree be \(m\ge3\), so its source is the closure of the product of its \(m\) original ordinary leaves. Choose one of those existing leaves, \(h_0=\mathscr T_{\gamma_1}p_0\), as the closing leaf. Write \(A=\prod_{i=1}^{m-1}h_i\). Equation (10), with the actual compatible turn type on \(A\), gives
\[
 \phi_\sigma(h_0 A)
   =\frac{\gamma_1}{\gamma_2}\,
     \phi_{\sigma'}\left(p_0\,\mathscr T_{\gamma_2}A\right).
 \tag{27}
\]
The right pairing is taken in the transferred typed frame; its coefficient pairing is still (7). The scalar ratio is retained. No external leaf is added, and no unproved norm for the general turn is used.

Each input of \(A\) has the cone with \(c_i=0\). The whole-hub theorem with \(B=m-1\), followed by the polynomial root coupon and trace bounds, yields
\[
             |\phi_\sigma(h_0A)|
                   \le\exp\{N(\widehat\omega_{m-1}+o(1))\}.
 \tag{28}
\]
The original closure is precisely the probe defining this constant, so \(F_0=\widehat\omega_{m-1}\). This handles the isolated three-leaf case \(m=3\) with \(\widehat\omega_2=4G_0\), as well as every fixed larger valence. The comparison has not added a \(2G_0\) norm cost for its closing leaf.

For two physical leaves there is no reduced hub. The strict edge parity is one. The exact Frobenius transfer exposes one unturned physical coupon and one decorated leaf, up to its specified typed scalar. The same estimate gives action \(2G_0\). When a volume interpretation is asserted, retain the separate two-leaf knot and framing hypotheses of the original strict theorem; in particular the source estimate does not turn a multicomponent parity choice into a knot. The main statement may instead be restricted to \(H\ge3\) without using this exceptional case.

As an optional check on constants, expansion of the recursive identities gives the root-independent formula
\[
 F_0=2G_0(H-1)+
   \sum_{v\ \mathrm{bare}}
     \left(\widehat\omega_{d_v-1}-2(d_v-1)G_0\right).
 \tag{29}
\]
Each nonroot flagged distinguished leaf and each ordinary leaf contributes one \(2G_0\); the chosen root leaf contributes none. A bare hub replaces the sum of its \(d_v-1\) child L budgets by (21), producing the displayed correction. In the unflagged single-hub case, the same formula reduces to (28). Equation (29) is action accounting, not a decomposition of a hyperbolic manifold into pieces with these volumes.

## 6. The main cut and the limits of the conclusion

The primitive partial-trace formula for the actual reduced cut gives exactly
\[
 \mathcal F_{N,\mathbf j}^{\epsilon}(q^s)
    =\frac{s_x}{s_0}\,Z_{N,\mathbf j}^{\epsilon}(s),\qquad
                    \frac{s_x}{s_0}=H_N(s).
 \tag{30}
\]
The common complete normalization \(s_0\), the prescribed pivot and all physical crossing and framing phases are the ones already present in the source compiler. Switching the orientation of the exposed main strand replaces \(s\) by \(-s\), and \(H_N\) is even. This does not introduce an untracked modified dimension. On \(|s|\le R<1\), \(H_N\) is uniformly bounded and nonzero, so (25) or (28) proves (3). The exact root scalar in (24) and (27) is bounded as well and has already been retained.

Under the original strict geometric assumptions, substitution of (2) states the upper bound as
\[
 \limsup_{N\to\infty}\frac{2\pi}{N}
    \log\sup_{|s|\le R,\,\mathbf j}
      |\mathcal F_{N,\mathbf j}^{\epsilon}(q^s)|
       \le\operatorname{Vol}(M_{\mathrm{aug}}).
 \tag{31}
\]
If an individual supremum is zero, its logarithm is interpreted as \(-\infty\). Holomorphy and Cauchy's estimate give the same exponential upper rate for every fixed derivative in \(s\) on a smaller disk. They give no asymptotic lower bound.

The separation condition is essential to this proof's recursive invariant. A general adjacent bare hub receives an A module whose low coefficient profile is not \(g+c\); a small spectral remainder also need not retain the full saving required by the next bare hub. Nothing above resets that module for free. Conversely, every bare hub in the stated class is fed only L modules, so this missing step is never used.

Finally, (31) concerns the unsummed auxiliary-colored source at the complete augmented action. It does not supply a deformed far-color loss, a cancellation-preserving filling contour, a lower bound for a filled invariant, or a bound at the generally smaller filled-knot volume. It also does not prove convergence of the ordinary-color-subtracted microscopic meridian profile. Those statements require additional control of the whole signed contraction or filling transform.
