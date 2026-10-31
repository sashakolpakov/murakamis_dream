# Independently long integer twists on weighted Conway trees

31 October 2026. The class is specified
by literal ordered tangle operations. Every finite rooted ordered tree
with at least two vertices gives such a presentation; its branching,
valence and depth are unrestricted. A fixed knot-producing parity pattern
and sufficiently large independent integer weights give the original
invariant's hyperbolic knot complement volume limit. General arborescent
coverage and mixed flagged/unflagged source trees remain separate.

## 1. The weighted tangle presentation and theorem

Let \(\mathcal T\) be a finite rooted ordered tree with \(H\ge2\)
vertices, numbered with root \(0\). There is one integer twist box at
each vertex. Write \(T\) for the original ordered quarter-turn and
\(R^n\) for the original integral two-strand twist tangle. For each
nonroot vertex define recursively
\[
 Q_v(\mathbf n)=T\!\left(R^{n_v}\prod_{w\text{ child of }v}
                                      Q_w(\mathbf n)\right),
 \tag{1}
\]
where the product keeps the given child order and an empty product is
one. At the root retain the literal cylindrical closure
\[
 K_{\mathcal T}(\mathbf n)
 =C\!\left(T(R^{n_0})\,
       T\!\left(\prod_{w\text{ child of }0}Q_w(\mathbf n)\right)\right).
 \tag{2}
\]
![A weighted Conway composition tree with branching and a unary chain; this specifies syntax, not a knot projection.](../book/figures/weighted-conway-tree.png)

The marked one-cut convention, terminal order and disk framings are
part of (1)–(2). These are Conway tangle operations on integral rational
pieces, so a one-component result is an arborescent knot. No conventional
plumbing or numerator-closure isotopy is required by this definition.

**Weighted-tree theorem.** For every fixed \(\mathcal T\) there is a
finite \(B(\mathcal T)\) such that, for every fixed tuple of integers
\(\mathbf n\) with \(|n_v|>B(\mathcal T)\), if the literal pairing in
(1)–(2) has one component and no internal closed component, its complement
is hyperbolic and
\[
 \lim_{N\to\infty}\frac{2\pi}{N}
 \log\left|K_N(K_{\mathcal T}(\mathbf n))\right|
       =\operatorname{Vol}(S^3\setminus K_{\mathcal T}(\mathbf n)).
 \tag{3}
\]
The original reduced enhanced Kashaev evaluation is denoted by \(K_N\).
Both parities and all composite levels occur in the limit. The signs
and magnitudes of the weights are independent; no ratio bound is imposed.
The tree and all integer weights are fixed before \(N\) tends to infinity.
The threshold is allowed to depend on the whole tree.

Every tree in this statement has knot-producing parity choices. This is
the constructive terminal-pairing conclusion of the [general marked-mask
geometry theorem](actual_conway_general_mask_marked_filling.md), applied to the literal expression below. It does not
say that every parity choice makes a knot. Full twists preserve the pairing.

Equivalently, first fix \(\epsilon_v\in\{0,\pm1\}\) giving a knot and
write \(n_v=\epsilon_v-2p_v\). There is \(P(\mathcal T,\epsilon)\)
such that (3) holds for all independently fixed signed integers
\(|p_v|>P(\mathcal T,\epsilon)\). Taking a maximum over the finitely
many knot-producing parity patterns, and increasing the integer threshold,
gives the displayed formulation in terms of \(|n_v|\).

## 2. The exact colored source and its strict geometry

Before filling, vertex \(v\) carries the original auxiliary character
\(P_v=R^{\epsilon_v}L_{j_v}\), with independent \(1\le j_v\le N\).
Set
\[
 h_v=T(P_v),\qquad
 D_v[E]=T(P_vE),\qquad
 Q_v=D_v\!\left[\prod_wQ_w\right],\qquad
 E_0=\prod_{w\text{ child of }0}Q_w.
 \tag{4}
\]
The original scalar is exactly
\[
 Z_N(\mathbf j)=\phi(h_0T(E_0))=\phi(P_0E_0).
 \tag{5}
\]
The equality is the full Frobenius turn identity. No normal direction,
physical color, framing character or additional dimension factor is
removed. In the literal h/T/product language a nonterminal \(Q_v\)
is \(T[(T h_v)\prod_wQ_w]\); a terminal \(Q_v\) is \(h_v\).

Each \(Q_v\) has strict type L. Inductively, a nonempty product of its
children has type L or A, so its product with \(T h_v\), of type H,
has type H and its final turn has type L. At the root, \(E_0\) is L or
A, and \(h_0T(E_0)\) has a strict complementary root pair. Thus the
[strict-source compiler](actual_conway_single_leaf_source_composition.md) and [marked-mask theorem](actual_conway_general_mask_marked_filling.md) apply without an additional
geometric test for this class.

Put \(G_0=g(1/4)=2\mathrm{Catalan}/\pi\), with
\(g(a)=J(2a)-4J(a)\) and
\(J(u)=\int_0^u\log(2\sin\pi t)\,dt\).
The [exact complete-character kernel](actual_conway_reduced_hub_source_normal_form.md), or independently the [rigid-spine
action formula](actual_conway_rigid_spine_and_flagged_tree_geometry.md), gives
\[
 F_0=\lim_N\frac1N\log Z_N^0(N,\ldots,N)=2G_0(H-1),
 \qquad
 \operatorname{Vol}(Y_{\mathcal T}^{\epsilon})=2v_{\mathrm{oct}}(H-1),
 \quad v_{\mathrm{oct}}=4\mathrm{Catalan}.
 \tag{6}
\]
Here \(Z_N^0\) has all signs zero, and \(Y_{\mathcal T}^{\epsilon}\)
is the actual complete augmented exterior with the retained signs.
Equation (6) is an absolute calibration, not a norm budget chosen for
convenience. Its rightmost volume belongs to the unfilled augmented link;
the knot volume in (3) is the distinct filled critical value in §5.

## 3. A global estimate closed under arbitrary branching

Use the faithful full-Hermite norm \(\|\cdot\|_{\mathcal J}\), recording
values and first derivatives at every double Casimir node and the value
at the odd simple node. The [decorated-character theorem](actual_conway_decorated_character_spectral_closure.md) proves, for the
actual turn and all physical signs and colors,
\[
 \|D_j^\epsilon[E]\|_{\mathcal J}
   \le \operatorname{poly}(N)e^{2NG_0}\|E\|_{\mathcal J}.
 \tag{7}
\]
The input norm also yields a Gaussian angular envelope for the canonical
output, localized at \(z=-2\). Multiplication preserves both the norm
bound and the envelope. The [exact root-character Fourier theorem](actual_conway_root_character_fourier_contraction.md) gives
a strict loss whenever the newly inserted character has a macroscopic
color deficit. A deficit in a descendant already gives a norm loss,
which (7) preserves.

There are exactly \(H-1\) decorated turns below the closing character.
The latter has polynomial norm in the original closure. Hence the
induction gives, for every fixed \(\delta>0\), some
\(\gamma_\delta>0\) and all sufficiently large \(N\),
\[
 \max_{\substack{1\le j_v\le N\ \text{for all }v\\
                   \max_v(N-j_v)\ge\delta N}}
       |Z_N(\mathbf j)|
       \le e^{N(F_0-\gamma_\delta)}.
 \tag{8}
\]
It also gives a uniform whole-cube upper rate \(F_0+o(1)\).
The complete positive kernel supplies a matching lower rate in (6).
Thus no oversized bound has been substituted for the complete action.

The Fourier input to this induction retains the normal terms. Their
weights cancel the folded frequency that would otherwise destroy (8)
near the smallest physical colors. The estimate concerns the original
whole source, before any asymptotic replacement or filling sum.

## 4. A general complementary-color principle for all alias sectors

This step is independent of the shape of \(\mathcal T\). Let any fixed
multilinear original source have \(H\) physical leaves \(h_j^\epsilon\).
For \(j>N/2\), its [exact original split](actual_conway_two_leaf_block_source_gap.md), §1, is
\[
 h_j^\epsilon=C_j^\epsilon+A_j^\epsilon,
 \qquad A_j^\epsilon=(-1)^N h_{N-j}^\epsilon,
 \qquad h_0^\epsilon=0.
 \tag{9}
\]
For \(j\le N/2\), the core is zero. These are identities in the full
repeated-root algebra; the physical half-twist transport is linear and
preserves (9).

Assume that the whole source has a strict gap whenever any color is
at most \(N/2\), uniformly over all other physical colors. If all
\(j_v>N/2\), multilinearity gives
\[
 Z_N^{\mathrm{core}}(\mathbf j)
 =\sum_{S\subseteq\{0,\ldots,H-1\}}
       (-1)^{|S|}(-1)^{N|S|}Z_N(\mathbf j^{,S}),
 \qquad
 j_v^{,S}=\begin{cases}N-j_v,&v\in S,\\j_v,&v\notin S.
                  \end{cases}
 \tag{10}
\]
Every nonempty subset inserts at least one small color. A zero color
makes that whole term zero. There are only \(2^H-1\) such terms, with
\(H\) fixed. If some original \(j_v\le N/2\), the all-core source
is zero and the assumed gap applies directly to \(Z_N\). Consequently
\[
 \sup_{\text{physical }\mathbf j}
 |Z_N(\mathbf j)-Z_N^{\mathrm{core}}(\mathbf j)|
       \le \operatorname{poly}(N)e^{N(F_0-\gamma)}
 \tag{11}
\]
for some \(\gamma>0\). This controls the total nonempty-alias contribution
without estimating its separately expanded signed coefficients.

Applying (8) with \(\delta=1/2\) proves (11) for every weighted tree.
The [general core theorem](actual_conway_general_core_packet_and_gap.md) now supplies an exact finite, separately even
holomorphic window \(\mathcal C_N\) with
\[
 \mathcal C_N(\chi)=N^{3/2}a_\epsilon(\chi)
           e^{N\Phi_\epsilon(\chi)}(1+O(N^{-1})),
 \quad a_\epsilon(0)\ne0,\quad \Phi_\epsilon(0)=F_0,
 \tag{12}
\]
For physical deficits \(h_v=N-j_v\) in a fixed small corridor,
\[
 |Z_N(\mathbf N-\mathbf h)-\eta_N\mathcal C_N(\mathbf h/N)|
       \le \operatorname{poly}(N)e^{N(F_0-\gamma)},\qquad
 \eta_N=\exp\!\left(\frac{i\pi(N-1)}4\sum_v\epsilon_v\right).
 \tag{12a}
\]
The packet expansion holds on a fixed complex neighborhood,
retaining every original integer offset, unit phase and interpolation
error. Every complete leaf is at least quarter index. For \(H\ge3\)
the gate Hessians supply full primitive rank; for the two-leaf knot case,
a pure leaf supplies the needed curvature. Both-odd two-leaf patterns
have two main components and are not among the knots in (3).

The diagonal color Hessian has entries
\[
 \partial_v\partial_w\Phi_\epsilon(0)
 =-\frac{2\pi c_v}{1-\epsilon_vi c_v}\delta_{vw},
 \qquad c_v=\cot(\pi a_v)>0.
 \tag{13}
\]
Its real part is negative definite. Equations (8), (11) and (12) verify
all global and local hypotheses of the original-source filling transfer.

## 5. The selected filled action is the actual knot complement volume

For the integral filling slopes \(p_v\), so the physical power is
\(R^{\epsilon_v-2p_v}\). The full Fourier–Hermite circle-basis identity
substitutes those powers exactly into the original diagram. Its coefficient
mass is at most \(2N(1+|p_v|)\) per port. Thus (8) and (11) remain
exponentially negligible after filling for each fixed slope tuple.
The [entire filling theorem](general_original_source_long_filling_transfer.md) retains all endpoint currents and nonzero
charges and proves a nonzero asymptotic with selected exponent
\[
 S_{\epsilon,\mathbf p}(\chi_*)=
 \Phi_\epsilon(\chi_*)+\frac{\pi i}{2}
                   \sum_v\frac{(\chi_{*,v}-1)^2}{p_v},
 \qquad dS_{\epsilon,\mathbf p}(\chi_*)=0.
 \tag{14}
\]
Its leading amplitude is nonzero for all independently sufficiently long
fixed signed slopes. This controls the whole invariant, not merely one
formal stationary term.

For the same literal strict tree, the [general marked-mask theorem](actual_conway_general_mask_marked_filling.md) gives
an actual nearby representation of the original augmented-link group,
with primitive logs and absolutely calibrated regulator
\[
 U_v=-2\pi i\chi_v,\qquad V_v=-2\partial_v\Phi_\epsilon,
 \qquad G=2\pi i\Phi_\epsilon,
 \quad
 \operatorname{Vol}(\rho_\chi)=\Im G-\frac12\sum_v\Re U_v\Im V_v.
 \tag{15}
\]
The stationary equations in (14) are exactly
\(U_v+p_vV_v=-2\pi i\). The framed metric-completion theorem then
gives a smooth complete finite-volume metric on the actual disk-filled
manifold, with primitive angular turn \(2\pi\). All auxiliary crossing
circles are filled; the main knot cusp remains unfilled. On that solution,
\[
 2\pi\Re S_{\epsilon,\mathbf p}(\chi_*)
          =\operatorname{Vol}(S^3\setminus K_{\mathcal T}(\mathbf n)).
 \tag{16}
\]
One fixed reciprocal-slope neighborhood works for the finitely many
ports. Taking a common analytic and geometric threshold proves (3).
The [original normalization](actual_complete_augmented_source_normalization.md) changes the retained scalar by a unit framing
character, or by the recorded single polynomial one-cut factor in the
modified convention; neither changes the logarithmic limit.

## 6. More general presentations and the remaining boundary

The same conclusion holds for any fixed original strict h/T/product
expression whose reduced Frobenius hub tree has exactly one flagged
original leaf at every hub, and whose actual endpoint pairing gives a
knot. The [reduced-hub theorem](actual_conway_reduced_hub_source_normal_form.md) is an exact identity for all independent
physical colors and first normals. It transfers (8) to the original
expression. Principle (9)–(11) then restores that expression's own core
packet, and its own marked geometry proves (16). No tangle isotopy or
peripheral identification between rearranged expressions is needed.

For arbitrary strict syntax the exact reduced-hub criterion is at most
one flagged leaf per hub. The no-flag case reduces to the already proved
completed grammar; the present argument treats the all-hubs-flagged case.
Mixtures still contain genuine turns without an adjacent original physical
character. The full-Hermite turn norm has exponential rate \(2G_0\);
charging that cost to an invented leaf would exceed the known geometric
action. A sharp estimate for such mixed trees remains open.

The weighted-tree theorem permits arbitrary finite branching and unary
continued-fraction chains, but uses the displayed literal closure. It is
not a classification of all arborescent knot presentations, a uniform
threshold over growing trees, or a generic main-meridian quantum
A-polynomial theorem. Those broader parts of the active goal remain open.

## Coverage and scope

The [repository comparison](actual_conway_root_star_prior_source_coverage.md)
identifies the earlier outer-kernel cancellation and the one-hub all-odd
overlap with the belt source. The [belt construction](actual_balanced_octahedral_belt_stack_volume.md)
explicitly leaves branched multi-belt graphs outside its source argument.
The new ingredient here is closure under nested \(T(R^\epsilon L_jE)\)
with distinct original characters, together with the complementary-color
principle.

For literature coverage, [van der Veen's Whitehead-chain paper](https://arxiv.org/abs/math/0611181)
states a volume-conjecture theorem for an infinite family of links.
It is a relevant comparator; no equivalence of its knot types with all
presentations (1)–(2), or novelty classification, is proved here. Its
proof is not an input to this argument.
