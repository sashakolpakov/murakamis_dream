# Long-twist volume equality for every strict Conway composition tree

31 October 2026. Internally reviewed research theorem.
The statement concerns a specified literal presentation and its original
marked invariant. It includes arbitrary mixtures of flagged and unflagged
source junctions. The new ingredient is an estimate for an unflagged
component at its actual geometric boundary action. No classification of
all arborescent knot presentations is asserted.

## 1. The presentation and the theorem

Fix a finite ordered expression
\[
                         \tau=C(FG)
\tag{1}
\]
in distinct leaves \(h_1,\ldots,h_H\), ordered products and the original
quarter-turn \(T\). Retain the original cylindrical closure, terminal order,
one-cut mark and disk framings. There are \(H\ge2\) leaves. The filled leaf
is the integral rational tangle
\[
                         h_i(n_i)=T(R^{n_i}).
\tag{2}
\]
Write \(K_\tau(\mathbf n)\) for the literal filled diagram.

The following finite type test is the hypothesis on \(\tau\).
A leaf has type \(L\); a turn exchanges \(L,H\) and preserves \(A\).
The nonempty product rules, including reversed orders, are
\[
 LL,LA,AA\longmapsto A,\qquad
 HL,HA\longmapsto H,\qquad HH\longmapsto\varnothing.
\tag{3}
\]
The root pair in (1) must be one of \(AA,AL,AH,LH\), in either order.
Call such a presentation **strict**. The
[source compiler](actual_conway_single_leaf_source_composition.md) proves
that this test is equivalent to the existence of a strict state in the
original reduced wire polytope. In particular, it is a test on the
specified finite syntax, not a conjectural property of an optimizer.

**Theorem.** For every fixed strict presentation \(\tau\), there is a finite
number \(B(\tau)\) such that, for every fixed tuple of integers \(\mathbf n\)
with \(|n_i|>B(\tau)\), if its literal endpoint pairing has one component
and no internal closed component, \(K_\tau(\mathbf n)\) is a hyperbolic
knot and
\[
 \boxed{\quad
 \lim_{N\to\infty}\frac{2\pi}{N}
       \log|K_N(K_\tau(\mathbf n))|
       =\operatorname{Vol}(S^3\setminus K_\tau(\mathbf n)).
 \quad}
\tag{4}
\]
Here \(K_N\) is the original reduced enhanced Kashaev evaluation, with the
normalization used throughout the source construction. The limit runs
through all positive integer levels, including both parities and composite
levels. The integer weights have independent signs and magnitudes.
The expression and all its weights are fixed before \(N\) tends to infinity.
The threshold may depend on the entire expression.

Every strict presentation has knot-producing pairing choices, by the
[constructive pairing theorem](actual_conway_general_mask_marked_filling.md),
§7. The theorem does not say that every parity choice produces a knot.
Equivalently, fix a knot-producing choice
\(\epsilon_i\in\{0,\pm1\}\), write \(n_i=\epsilon_i-2p_i\), and take all
independent fixed signed integers \(|p_i|\) sufficiently large.
A maximum over the finitely many relevant parity choices gives \(B(\tau)\).

The knots in (4) are Conway algebraic, or arborescent: (2), the ordered
products and turns are the actual Conway operations on rational pieces.
Strictness and the pairing test are substantive hypotheses. This theorem
does not identify every arborescent knot with a strict long-weight
presentation.

## 2. What remains fixed from the original source

Before filling, replace (2) by the actual colored leaf
\[
 P_i=R^{\epsilon_i}L_{j_i},\qquad
 h_i=T(P_i),\qquad 1\le j_i\le N.
\tag{5}
\]
Let \(Z_N^\epsilon(\mathbf j)\) be the original scalar of (1).
All physical colors, full first normal coefficients at double nodes,
unit framing phases and peripheral marks are retained.

The complete positive action of this literal expression is
\[
 F_0=\max_{y\in P_\tau}
 \left\{\sum_{i=1}^H g(a_i(y))
              +\sum_{v=1}^{H-2}m(x_v(y),y_v(y),z_v(y))\right\},
\tag{6}
\]
where
\[
 \begin{aligned}
 J(t)&=\int_0^t\log(2\sin\pi u)\,du,\\
 g(a)&=J(2a)-4J(a),\\
 m(x,y,z)&=J(x+y)+J(z)-J(x)-J(y)\\
 &\quad-J(z-x)-J(z-y)-J(x+y-z).
 \end{aligned}
\tag{7}
\]
The final forced product has coefficient one and is deleted; its original
complementary relation is retained. Every remaining product has
\(\max(x,y)\le z\le x+y\le1\). The compiler gives a primitive lattice of
dimension \(2H-3\), and strictness gives a unique interior maximum.

The [general core theorem](actual_conway_general_core_packet_and_gap.md)
and [marked geometric theorem](actual_conway_general_mask_marked_filling.md)
already apply to this full strict class. They identify \(2\pi F_0\) with
the actual complete augmented exterior volume and provide its selected
deformation, primitive peripheral logs and local source packet.
The missing global estimate was
\[
 \begin{aligned}
 \sup_{\mathbf j}|Z_N^\epsilon(\mathbf j)|
       &\le \exp N(F_0+o(1)),\\
 \max_i(N-j_i)\ge\delta N
 \quad&\Longrightarrow\quad
 |Z_N^\epsilon(\mathbf j)|
       \le \exp N(F_0-\gamma_\delta)
 \end{aligned}
\tag{8}
\]
for every fixed \(0<\delta<1\), with \(\gamma_\delta>0\).
Sections 3–5 establish (8) for every strict presentation.

## 3. Exact source decomposition and its boundary actions

Use the [reduced-hub normal form](actual_conway_reduced_hub_source_normal_form.md).
It is an identity of full colored source tensors. Internal edges between
reduced product hubs carry \(T\); an ordinary external leaf is \(h_i\),
and a flagged external leaf is \(Th_i=P_i\).
Strictness is equivalent to at most one flagged leaf at each hub.
No relative-boundary tangle isotopy is inferred from this source identity.

For \(H\ge3\), if no hub is flagged, the scalar reduces to the already proved
completed/completed-root grammar, or to the isolated three-leaf closure.
If \(H=2\), the strict two-leaf knot case is already included in the
[weighted-tree theorem](actual_conway_weighted_tree_long_twist_volume.md).
Thus consider \(H\ge3\) and at least one flagged hub.
Root the source at one flagged leaf \(P_0\).

A flagged descendant sends a type-\(L\) module
\[
 D_i[E]=T(P_iE),\qquad E=\prod_j Q_j,
\tag{9}
\]
where the satellite coupons \(Q_j\) have type \(L\) or \(A\).
An ordinary physical leaf is the case \(E=1\).
Group each maximal connected set of unflagged hubs into one component.
Its outgoing coupon has the form
\[
                         Q=T(A(F_1,\ldots,F_s)),\qquad s\ge2,
\tag{10}
\]
where the output of \(A\) is an unturned product and all boundary modules
\(F_i\) have type \(L\). Inside this component there are only completed
products and turns. The source tree is finite, so (9) and (10) give a
well-founded induction.

For any satellite \(Q\), let \(f_Q\) be its original optimized positive
output profile, and define
\[
 \Omega_Q=\max_{0\le b\le1/2}\{g(b)+f_Q(b)\},\qquad
 G_0=g(1/4)=\frac{2\,\mathrm{Catalan}}{\pi}.
\tag{11}
\]
The [rigid-profile theorem](actual_conway_rigid_spine_and_flagged_tree_geometry.md)
fixes the absolute constant of (9):
\[
 f_{D_i[E]}(b)=g(b)+c_i,\qquad
 c_i=\sum_j\Omega_{Q_j},\qquad
 \Omega_{D_i[E]}=c_i+2G_0.
\tag{12}
\]
For (10), if \(f_{F_i}=g+c_i\), then
\[
 \Omega_Q=\sum_i c_i+
     F_{\mathrm{probe}}\bigl(C(hA(h,\ldots,h))\bigr).
\tag{13}
\]
Here \(F_{\mathrm{probe}}\) denotes the complete positive action of the
displayed reference expression. Formula (13) is a boundary variational
identity, not a physical insertion into the original diagram.
The [probe geometry](actual_conway_unflagged_probe_geometry.md) proves it
with the original unsquared port equations.

At the flagged root the exact source is
\[
                         Z_N^\epsilon=\phi(P_0\prod_jQ_j).
\tag{14}
\]
The original complete action satisfies
\[
                              F_0=\sum_j\Omega_{Q_j}.
\tag{15}
\]
Indeed the corresponding \(H\)-profile is
\(g(1-z)+\sum_j\Omega_{Q_j}\). At its coefficient-one closing endpoint
\(z=1\), its action is (15). Equivalently, the original complementary
root relation gives the same maximum. Thus every boundary constant used
below is charged to the actual complete action in (6).

## 4. The estimate for an unflagged component

Put \(d=N-1\), \(M=\lfloor d/2\rfloor\), and write \(e_r=\widehat B_r\)
for the normalized Newton basis of the original repeated-root algebra.
Its exact turn and full Frobenius pairing are
\[
 Te_r=e_{d-r},\qquad \phi(e_re_s)=\mathbf1_{r+s=d}.
\tag{16}
\]
The faithful norm \(\|\cdot\|_{\mathcal J}\) records values and first
derivatives at every double node, and the value at the odd simple node.
Define the positive comparison weights
\[
 w_{N,r}=
 \begin{cases}e_r(-2),&r\le M,\\1,&r>M,\end{cases}
 \qquad W_N=\sum_{r=0}^d w_{N,r}e_r.
\tag{17}
\]
They obey \(\|e_r\|_{\mathcal J}\le N^Cw_{N,r}\) and
\(\log w_{N,r}=Ng(r/N)+O(\log N)\) on the low range.

The [positive probe theorem](actual_conway_unflagged_core_probe_bound.md)
has an arbitrary-array hypothesis:
\[
 |[e_r]F_i|\le \exp N(c_i+o(1))
 \begin{cases}w_{N,r},&r\le M,\\1,&r>M.\end{cases}
\tag{18}
\]
Let \(A^{\mathrm{abs}}\) be the same circuit with the absolute values of
these boundary coefficients. Positive Newton multiplication and exact
index reversal give
\[
 \|T(A)\|_{\mathcal J}
 \le N^C\sum_r w_{N,r}|[e_{d-r}]A|
 \le N^C\phi(W_NA^{\mathrm{abs}}).
\tag{19}
\]
This includes every high Newton normal direction.

![A mixed source component and its separate positive norm comparison. The probe does not add a crossing circle to the original diagram.](../book/figures/mixed-conway-probe.png)

The right side is estimated by the existing scalar block inequalities.
Its low input and probe bands have profile \(g\); their high bands have
profile \(0\). These are bounded by the certified profiles
\[
 \widetilde g(x)=g(\max(x,1/4)),\qquad k(x)=-2J(x/2),
\tag{20}
\]
respectively. The closed comparison has no flags. It is either the
isolated effective three-leaf closure or an exact source regrouping of
the completed-root grammar. The two-leaf block and single-attachment
inequalities apply to arbitrary arrays satisfying these upper profiles:
their proofs use positive multiplication, true support, concave tangents
and stationary cancellation, rather than the provenance of a color.

Consequently (19) has upper rate \(\Omega_Q\) from (13). Every sector
with a high boundary index or high probe index has a strict exponential
gap. The all-low action has the original unique strict maximum; outside
any fixed neighborhood of that maximum it also has a strict gap.
The finite \(N-1\) offsets, both parities and polynomial numbers of
states are retained in this assertion. These comparison bands are not
declared to be the original physical core and alias bands.

The [spectral propagation theorem](actual_conway_mixed_core_spectral_propagation.md)
now proves two further consequences:
\[
 \begin{aligned}
 \|Q_N\|_{\mathcal J}&\le \exp N(\Omega_Q+o(1)),\\
 |Q_N(2\cos(\theta+iy))|
 &\le \exp N\{\Omega_Q-c(\theta-\pi)^2+Cy^2+o(1)\}.
 \end{aligned}
\tag{21}
\]
The second estimate uses the canonical representative and a fixed small
strip; \(c>0\). Near the clean probe index, the low Newton polynomial has
a strict angular Gaussian at \(-2\). The remaining output is a canonical
polynomial with a fixed norm gap, so the Hermite interpolation cost
\(\exp(N|y|)\) is absorbed by taking a smaller strip.

Finally, a fixed coefficient loss in any boundary module on a compact
window around its actual clean index gives a strict loss in
\(\|Q_N\|_{\mathcal J}\). Outside that window the clean action already has
a gap, and high-band sectors are already gapped. This is the mechanism
that transports physical color deficits through an unflagged component.
No uniform bound on an arbitrary turn's norm at this smaller action
is asserted.

## 5. Mutual induction and the whole physical color cube

The [decorated-character estimate](actual_conway_decorated_character_spectral_closure.md)
gives, for an actual input \(E\) with norm upper rate \(c\),
\[
 |[e_r]D_j^\epsilon[E]|\le N^C\|E\|_{\mathcal J}
 \begin{cases}w_{N,r},&r\le M,\\1,&r>M.\end{cases}
\tag{22}
\]
Its norm rate is at most \(c+2G_0\), and its canonical output has an
angular Gaussian at that rate. An existing input norm loss is preserved
at every output coefficient.

For the newly inserted physical character, the exact root-character
Fourier theorem gives, on every fixed compact \(I\subset(0,1/2)\),
\[
 N-j\ge\delta N,\quad r/N\in I
 \quad\Longrightarrow\quad
 |[e_r]D_j^\epsilon[E]|
       \le \exp N\{c+g(r/N)-\eta_{\delta,I}\},
 \qquad \eta_{\delta,I}>0,
\tag{23}
\]
provided \(E\) has the inherited strip envelope. The empty input is
allowed. The extension to every such compact interval is proved in the
spectral propagation theorem; it is essential because an effective leaf
of an unflagged component need not be at the quarter index.
The Fourier estimate retains the original normal terms and folded
frequency cancellation.

Proceed from the leaves toward the flagged root. Products add norm
rates and multiply actual strip envelopes. At (9), equations (22)–(23)
give the coefficient bounds needed at the next component, with the
absolute constant \(c_i\) in (12). At (10), equations (19)–(21) give
a fresh norm and Gaussian estimate at the intrinsic action (13).
A deficit in a descendant passes through the norm estimate; a deficit
in the distinguished character of a boundary module passes through
(23) and clean-state localization. Every original physical color is
therefore accounted for.

At (14), the root character has polynomial norm in the marked functional.
A far descendant is controlled by its norm loss. If the root character
is far, apply the exact Fourier theorem to the product of the satellite
representatives, which has the inherited Gaussian envelope. Formula (15)
identifies the resulting reference exponent with \(F_0\). This proves
(8). There are finitely many original colors, so a common positive
\(\gamma_\delta\) is obtained by taking the minimum of their margins.

The no-flag cases cited in §3 already satisfy (8). The two-leaf knot case
does also. Hence (8) holds for every presentation in the theorem.

## 6. Recovering the original packet and filling the crossing circles

The exact complementary-color identity for every original leaf is
\[
 h_j^\epsilon=C_j^\epsilon+(-1)^Nh_{N-j}^\epsilon
 \quad(j>N/2),\qquad h_0^\epsilon=0.
\tag{24}
\]
For \(j\le N/2\), its core is zero. Multilinearity expands the all-core
scalar into the whole source plus finitely many terms having at least
one color at most \(N/2\). Equation (8), with \(\delta=1/2\), gives a
uniform exponential bound for their total. This is the
[complementary-color principle](actual_conway_weighted_tree_long_twist_volume.md),
§4, applied to the original physical leaves, rather than the comparison
bands in §4 above.

The general core theorem now gives the full source packet near complete
colors:
\[
 \begin{aligned}
 \mathcal C_N(\chi)
   &=N^{3/2}a_\epsilon(\chi)e^{N\Phi_\epsilon(\chi)}
                        (1+O(N^{-1})),\\
 a_\epsilon(0)&\ne0,\qquad \Phi_\epsilon(0)=F_0,\\
 Z_N^\epsilon(\mathbf N-\mathbf h)
   &=\eta_N\mathcal C_N(\mathbf h/N)
        +O\!\left(N^Ce^{N(F_0-\gamma)}\right),\\
 \eta_N&=\exp\!\left(\frac{i\pi(N-1)}4\sum_i\epsilon_i\right).
 \end{aligned}
\tag{25}
\]
The packet is separately even and holomorphic on a fixed neighborhood.
The physical source identity is asserted at the actual integer colors.
Its diagonal color Hessian is
\[
 \partial_i\partial_j\Phi_\epsilon(0)
       =-\frac{2\pi \nu_i}{1-\epsilon_i i \nu_i}\delta_{ij},
 \qquad \nu_i=\cot(\pi a_i)>0.
\tag{26}
\]
Its real part is negative definite.
Every original complete leaf is at least quarter index, so the proved
high and quarter packet estimates cover it. For \(H=2\), both-odd
patterns have two main components; the knot patterns have the pure leaf
required by the two-leaf core theorem.

The [original-source long-filling transfer](general_original_source_long_filling_transfer.md)
applies to (8) and (25). Its exact Fourier–Hermite circle-basis identity
inserts \(R^{\epsilon_i-2p_i}\) in the original leaf frame, producing
the turned rational leaf \(h_i(n_i)=T(R^{n_i})\).
For each fixed slope tuple the coefficient mass is polynomial in \(N\),
so the global error remains exponentially negligible.
For independently sufficiently long fixed signed slopes, the full
filled invariant has nonzero leading amplitude and selected exponent
\[
 S_{\epsilon,\mathbf p}(\chi_*)
 =\Phi_\epsilon(\chi_*)+
          \frac{\pi i}{2}\sum_i\frac{(\chi_{*,i}-1)^2}{p_i},
 \qquad dS_{\epsilon,\mathbf p}(\chi_*)=0.
\tag{27}
\]
This is the whole-source transfer, including endpoint currents and
nonzero charges, rather than an isolated formal saddle contribution.

## 7. The selected value is the knot complement volume

Apply the marked geometric theorem to the original literal presentation,
not to a rearranged comparison source. It provides the actual nearby
representation of its augmented-link group with primitive logarithms
and an absolutely calibrated regulator:
\[
 U_i=-2\pi i\chi_i,\qquad V_i=-2\partial_i\Phi_\epsilon,\qquad
 G=2\pi i\Phi_\epsilon,\qquad
 \operatorname{Vol}(\rho_\chi)=
       \Im G-\frac12\sum_i\Re U_i\Im V_i.
\tag{28}
\]
The stationary equations (27) are precisely
\[
                              U_i+p_iV_i=-2\pi i.
\tag{29}
\]
The original framed metric completion gives primitive angular turn
\(2\pi\) and a smooth complete finite-volume metric on the actual
disk-filled exterior. All auxiliary crossing-circle cusps are filled
to insert the twists. The main knot cusp stays unfilled. At this solution,
\[
 2\pi\Re S_{\epsilon,\mathbf p}(\chi_*)
       =\operatorname{Vol}(S^3\setminus K_\tau(\mathbf n)).
\tag{30}
\]
A common reciprocal-slope neighborhood exists for the finitely many
ports. Combining its threshold with the analytic transfer threshold
proves (4). The [original one-cut normalization](actual_complete_augmented_source_normalization.md) contributes only its
recorded polynomial factor and unit framing character, which do not
alter the logarithmic limit.

## 8. Scope and proof dependencies

The new conclusion includes the previous completed-root and weighted-tree
classes and all their strict mixed compositions. The finite admissibility
test is (3), or equivalently at most one flagged original leaf per reduced
hub. Branching, valence and depth are unrestricted finite quantities.
The new estimate does not require every hub to carry a character.

The earlier manuscript retains its stated completed-root theorem.
This companion establishes the larger class without silently changing
that manuscript or its proof scope. The new proof uses the existing
exact two-leaf and single-attachment certificates unchanged, together
with the new probe and spectral arguments linked above. No numerical
asymptotic or external proof technique is an input to this extension.

The [pointed quantum \(A\)-period corollary](actual_conway_pointed_quantum_a_volume.md)
combines (4) with the existing all-level ADO annihilator and finite-pointing
theorems. It expresses the same limit directly through a genuine quantum
\(A\)-operator's companion product and bounded-order quantum-parameter
jets. Operator existence and that selected period's volume limit are
therefore available for the covered knots.

There is still no classification of every arborescent presentation by
this strict grammar, no threshold uniform over growing trees, and no
short-twist theorem. Identifying the selected classical main-meridian
geometric factor and its quantum module with the original marked
regulator germ is a separate stronger task. The source identities used
for estimates do not assert tangle
isotopies; the original expression supplies its own packet and marked
geometry in §§6–7.

The primary reviewer and three independent source, analytic and geometric
reviewers checked all eight assembly sections. The checks included the
exact literal-source reduction, noncircular mutual induction, regular-index
color losses, full normal data, absolute boundary constants, two-leaf knot
case, original packet and phase, independently signed thresholds, and
the original primitive marked completion. All passed after notation and
leaf-frame clarifications. The three new proof companions received
independent full reviews as well.

Native mathematical rendering, relative links and control bytes were
checked. The diagram was compiled from TikZ and visually inspected; it
depicts source syntax and an inequality. These are internal analytical
and reproduction checks, not external peer review or formal verification
of the entire theorem.
