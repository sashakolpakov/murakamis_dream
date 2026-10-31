# Long-twist volume equality for every strict Conway composition tree

31 October 2026.

A knot can be built by stacking and turning two-strand tangles, then joining their outside endpoints. This note proves the volume conjecture for every fixed construction of this kind that satisfies the strictness test below, once each of its signed twist counts is sufficiently large. The test is finite and depends on the specified construction. It does not assert that every arborescent knot has such a presentation.

The proof has two parts that must be kept together. The finite quantum source is estimated without discarding the cancellations between its terms. Its selected asymptotic is then identified with the hyperbolic geometry of the same marked tangle construction. Rearranging a source for an estimate is not used as a substitute for an isotopy of tangles.

## 1. The tangle construction and the theorem

A two-strand tangle is placed in a box with four ordered boundary endpoints. Let \(R^n\) be the standard two-strand braid with \(n\) signed half-twists. Positive and negative integers give the two crossing directions. The operation \(T\) turns a box through a quarter-turn, with the fixed endpoint convention of the source construction. Multiplication \(FG\) stacks two boxes in order, and \(C\) is the prescribed cylindrical closure of the four remaining endpoints.

Fix a finite expression

\[
                         \tau=C(FG)
\tag{1}
\]

built from these operations and \(H\ge2\) separately labeled basic pieces. Each piece occurs once and has its own integer weight. After the auxiliary fillings, the \(i\)th piece is the rational tangle

\[
                         h_i(n_i)=T(R^{n_i}).
\tag{2}
\]

The number of pieces is denoted by \(H\); the type label \(H\) introduced below is a separate use of that letter. Write \(K_\tau(\mathbf n)\) for the diagram obtained from this literal construction. Its endpoint order, local disk framings and cylindrical closure are fixed. The invariant also keeps the one-cut mark used to define the reduced evaluation: one component is cut at the specified place before the enhanced scalar is taken.

### The finite strictness test

The source calculation associates a normalized output state to every open subexpression. There are three possible intervals of strict output states. Type \(L\) has interval \((0,1/2)\), type \(H\) has interval \((1/2,1)\), and type \(A\) has interval \((0,1)\). These are state variables in the finite-sum and angle calculation, not twist counts.

Start with type \(L\) on each basic piece. A turn exchanges \(L\) and \(H\) and preserves \(A\). At a product use

\[
 LL,LA,AA\longmapsto A,\qquad
 HL,HA\longmapsto H,\qquad HH\longmapsto\varnothing.
\tag{3}
\]

where either order of the two input types is allowed. The symbol \(\varnothing\) means that there is no strict state. At the final closure in (1), the root pair must be \(AA,AL,AH\) or \(LH\), again in either order. Call a presentation passing these checks **strict**.

For example, a stack of two basic pieces has type \(A\), so the closure of two such stacks passes the test. The isolated closure of two basic pieces has root pair \(LL\) and fails. Failure is a limitation of this theorem for that presentation, not a counterexample to the volume conjecture.

The [source compiler](actual_conway_single_leaf_source_composition.md) proves that this recursive test is equivalent to a strict state in the reduced wire polytope: the set of normalized internal indices satisfying all product and closure constraints. Thus strictness is checked on the finite construction; it is not an assumption that an unspecified critical point behaves well.

**Theorem.** For every fixed strict presentation \(\tau\), there is a finite number \(B(\tau)\) with the following property. Choose a fixed tuple of integers \(\mathbf n\) with \(|n_i|>B(\tau)\) for every piece. If following the endpoints of the literal diagram gives one component and no internal closed component, then \(K_\tau(\mathbf n)\) is a hyperbolic knot and

\[
 \boxed{\quad
 \lim_{N\to\infty}\frac{2\pi}{N}
       \log|K_N(K_\tau(\mathbf n))|
       =\operatorname{Vol}(S^3\setminus K_\tau(\mathbf n)).
 \quad}
\tag{4}
\]

Here \(K_N\) is the reduced enhanced Kashaev evaluation in the normalization of the source construction. The limit runs through all positive integer levels, including even, odd and composite levels. The signs and relative magnitudes of the integers are unrestricted. The presentation and all twist integers are fixed before \(N\) tends to infinity, and the threshold may depend on the entire presentation.

The [constructive pairing theorem](actual_conway_general_mask_marked_filling.md), §7, supplies knot-producing parity choices for every strict presentation. It does not say that every parity choice gives a knot. One can equivalently fix a knot-producing pattern \(\epsilon_i\in\{0,\pm1\}\), write \(n_i=\epsilon_i-2p_i\), and require the independently signed integers \(|p_i|\) to be sufficiently large. Taking the maximum over the finitely many parity choices gives the stated \(B(\tau)\).

These knots are Conway algebraic, or arborescent, because the pieces (2), their ordered products and their turns are actual Conway tangle operations. The theorem concerns the stated class of presentations and long weights. It does not classify all arborescent knots or all their possible presentations.

## 2. The finite source and its geometric exponential rate

Before filling, each twist region is represented by an auxiliary crossing circle and an integer color. A color is a representation label in the invariant, not another component of the final knot. The local operator, also called a coupon, is

\[
 P_i=R^{\epsilon_i}L_{j_i},\qquad
 h_i=T(P_i),\qquad 1\le j_i\le N.
\tag{5}
\]

Here \(L_{j_i}\) is the crossing-circle operator of color \(j_i\), and \(R^{\epsilon_i}\) retains the prescribed half-twist. Applying the tangle operations to these operators and then closing gives the scalar \(Z_N^\epsilon(\mathbf j)\), called the source of (1).

The local spectral algebra can have repeated roots. A polynomial operator at a double root is determined by both its value and its first derivative there. These derivative coefficients are the first normal terms. They are retained in \(Z_N^\epsilon\), together with every color, unit framing phase and peripheral mark. Keeping only values at the spectral nodes would change the source.

The positive complete-color calculation has exponential rate

\[
 F_0=\max_{y\in P_\tau}
 \left\{\sum_{i=1}^H g(a_i(y))
              +\sum_{v=1}^{H-2}m(x_v(y),y_v(y),z_v(y))\right\},
\tag{6}
\]

with local functions

\[
 \begin{aligned}
 J(t)&=\int_0^t\log(2\sin\pi u)\,du,\\
 g(a)&=J(2a)-4J(a),\\
 m(x,y,z)&=J(x+y)+J(z)-J(x)-J(y)\\
 &\quad-J(z-x)-J(z-y)-J(x+y-z).
 \end{aligned}
\tag{7}
\]

The function \(J\) is the integrated log-sine function. The leaf term \(g\) and product term \(m\) arise from the exact sine-factorial coefficients. The variables \(a_i\) are normalized leaf indices, while \(x_v,y_v,z_v\) are the two inputs and output at a product. The polytope \(P_\tau\) retains their common wire constraints, so adjacent products cannot optimize their shared index independently. The symbol \(y\) in the maximum denotes the full vector of independent state variables.

At the closing product, the coefficient is exactly one. That factor is removed from the action, while its complementary-index relation is kept. Every remaining product satisfies \(\max(x,y)\le z\le x+y\le1\). The compiler produces a primitive integer lattice of dimension \(2H-3\): after choosing free coordinates, there is no further hidden congruence restricting the admissible grid. Strictness gives the interior geometric maximum in the knot cases of the theorem.

The [general core theorem](actual_conway_general_core_packet_and_gap.md) and [marked geometric theorem](actual_conway_general_mask_marked_filling.md) identify \(2\pi F_0\) with the volume of the complete augmented exterior. They also give a nearby geometric deformation and a nonzero local asymptotic. A local asymptotic alone does not bound the rest of a signed sum. The global estimate needed here is

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

for each fixed \(0<\delta<1\), with \(\gamma_\delta>0\). The first line bounds every physical color tuple. The second gives a strict loss whenever at least one color stays a fixed positive fraction away from the complete color \(N\). Sections 3–5 prove this estimate for the whole strict class.

## 3. Decomposing the source and keeping its boundary constants

The [reduced-hub normal form](actual_conway_reduced_hub_source_normal_form.md) rewrites the full colored contraction as a finite tree of product junctions. A *hub* is one such junction after adjacent products without a turn between them have been combined. An internal edge between hubs carries \(T\). An ordinary external leaf carries \(h_i\); a *flagged* leaf carries its turn \(Th_i=P_i\). The flag records this algebraic position of the turn, not an additional feature added to the knot.

In this form strictness is equivalent to at most one flagged leaf per hub. The equality is an identity of colored tensors, including their first normal terms. It does not assert an isotopy relative to the tangle boundary.

For \(H\ge3\), a tree with no flagged hub reduces to the previously proved class whose final two boxes are both constructed from two-piece stacks by turns, products and single-piece attachments, or to the isolated three-leaf closure. For \(H=2\), the strict two-leaf knot case is covered by the [weighted-tree theorem](actual_conway_weighted_tree_long_twist_volume.md). It therefore suffices to consider \(H\ge3\) with at least one flag and choose a flagged leaf \(P_0\) as the root of the contraction.

A flagged descendant sends the subtree operator

\[
 D_i[E]=T(P_iE),\qquad E=\prod_j Q_j,
\tag{9}
\]

to the next junction. The factors \(Q_j\) are the attached subtrees and have type \(L\) or \(A\). The output \(D_i[E]\) has type \(L\); an ordinary physical leaf is the case \(E=1\). We call these subtree operators boundary modules because they carry the data that must be passed to the rest of the contraction.

Now group every maximal connected set of unflagged hubs into one component. Its outgoing operator is

\[
                         Q=T(A(F_1,\ldots,F_s)),\qquad s\ge2,
\tag{10}
\]

where \(A\) ends in an unturned product and the boundary inputs \(F_i\) all have type \(L\). Within the component there are only the completed products and turns of the earlier construction. Equations (9) and (10) alternate along a finite tree. Each step depends only on smaller subtrees, which is why the induction below terminates.

To keep track of exponential constants, let \(f_Q(b)\) be the optimized positive action of a subtree \(Q\) when its output is fixed at \(b\). This is its boundary profile. Define

\[
 \Omega_Q=\max_{0\le b\le1/2}\{g(b)+f_Q(b)\},\qquad
 G_0=g(1/4)=\frac{2\,\mathrm{Catalan}}{\pi}.
\tag{11}
\]

where Catalan denotes Catalan's constant. The maximization in \(\Omega_Q\) closes that profile against one leaf action. It supplies the boundary rate to be used for the whole subtree, rather than a freely chosen norm budget.

The [rigid-profile theorem](actual_conway_rigid_spine_and_flagged_tree_geometry.md) proves

\[
 f_{D_i[E]}(b)=g(b)+c_i,\qquad
 c_i=\sum_j\Omega_{Q_j},\qquad
 \Omega_{D_i[E]}=c_i+2G_0.
\tag{12}
\]

for the module (9). In particular, it fixes the additive constant \(c_i\) from its attached subtrees. For an unflagged component (10), if \(f_{F_i}=g+c_i\), then

\[
 \Omega_Q=\sum_i c_i+
     F_{\mathrm{probe}}\bigl(C(hA(h,\ldots,h))\bigr).
\tag{13}
\]

The quantity \(F_{\mathrm{probe}}\) is the complete positive action of the displayed reference expression. This extra reference leaf is a tool for a variational comparison; it is not a crossing circle inserted into the original knot. The [probe geometry](actual_conway_unflagged_probe_geometry.md) proves (13) from the boundary equations with their signs retained before squaring.

At the chosen root, the source and its complete action are

\[
                         Z_N^\epsilon=\phi(P_0\prod_jQ_j).
\tag{14}
\]

and

\[
                              F_0=\sum_j\Omega_{Q_j}.
\tag{15}
\]

Here \(\phi\) is the linear closing functional of the finite tangle algebra. To see the action identity, the corresponding type-\(H\) profile is \(g(1-z)+\sum_j\Omega_{Q_j}\). The coefficient-one closing endpoint is \(z=1\), which gives (15); the complementary root relation gives the same maximum directly. Thus every rate used for a subtree is accounted for in the original \(F_0\), rather than being added to an unrelated upper envelope.

## 4. A positive comparison for an unflagged component

Set \(d=N-1\) and \(M=\lfloor d/2\rfloor\). Let \(e_r=\widehat B_r\) be the normalized Newton basis of the repeated-root algebra. Its turn and its closing pairing satisfy the exact identities

\[
 Te_r=e_{d-r},\qquad \phi(e_re_s)=\mathbf1_{r+s=d}.
\tag{16}
\]

The notation \([e_r]F\) means the coefficient of \(e_r\) in \(F\). The norm \(\|F\|_{\mathcal J}\) records all spectral values and first derivatives at double nodes, and the value at the odd simple node. It therefore controls the full operator data required by the source. Introduce

\[
 w_{N,r}=
 \begin{cases}e_r(-2),&r\le M,\\1,&r>M,\end{cases}
 \qquad W_N=\sum_{r=0}^d w_{N,r}e_r.
\tag{17}
\]

These weights satisfy \(\|e_r\|_{\mathcal J}\le N^Cw_{N,r}\), with low-degree rate \(\log w_{N,r}=Ng(r/N)+O(\log N)\). In this section, “low” means \(r\le M\) and “high” means \(r>M\). These are basis-degree ranges, not yet the physical core and alias terms of a colored leaf.

The [positive probe theorem](actual_conway_unflagged_core_probe_bound.md) applies to arbitrary arrays of boundary coefficients satisfying

\[
 |[e_r]F_i|\le \exp N(c_i+o(1))
 \begin{cases}w_{N,r},&r\le M,\\1,&r>M.\end{cases}
\tag{18}
\]

The errors are uniform over the ranges in question. Replace the boundary coefficients by their absolute values and use the same circuit; call the result \(A^{\mathrm{abs}}\). Newton multiplication has nonnegative structure constants. Together with the exact reversal in (16), this gives

\[
 \|T(A)\|_{\mathcal J}
 \le N^C\sum_r w_{N,r}|[e_{d-r}]A|
 \le N^C\phi(W_NA^{\mathrm{abs}}).
\tag{19}
\]

Every high-degree normal direction is included. The final scalar is nonnegative and retains the original support and closing target, so the comparison does not amount to independently maximizing the factors.

![A source component and its separate positive norm comparison. The probe belongs to the estimate and does not add a crossing circle to the knot.](../book/figures/mixed-conway-probe.png)

The low input and probe coefficients on the right of (19) have profile \(g\); the high coefficients have profile zero. They are bounded by the profiles

\[
 \widetilde g(x)=g(\max(x,1/4)),\qquad k(x)=-2J(x/2),
\tag{20}
\]

used in the earlier block estimates. The closed comparison has no flagged junction. It is either the isolated effective three-leaf closure or a regrouping of the completed-root source. The two-leaf and single-attachment inequalities can be applied to these arbitrary arrays because their proofs use only the upper profiles, positive multiplication, the exact support inequalities and cancellation of the supporting tangents at the stationary state. They do not require that the arrays themselves came from a particular physical color.

It follows that (19) has upper rate \(\Omega_Q\) from (13). A high boundary index or a high probe index has a strict exponential loss. If all indices are low, the action has the original unique strict maximum, so the complement of any fixed neighborhood also has a loss. The finite \(N-1\) offsets, both parities and the polynomial number of summands are included. No physical alias identity has been asserted for these artificial comparison bands.

The [spectral propagation theorem](actual_conway_mixed_core_spectral_propagation.md) strengthens the norm bound to

\[
 \begin{aligned}
 \|Q_N\|_{\mathcal J}&\le \exp N(\Omega_Q+o(1)),\\
 |Q_N(2\cos(\theta+iy))|
 &\le \exp N\{\Omega_Q-c(\theta-\pi)^2+Cy^2+o(1)\}.
 \end{aligned}
\tag{21}
\]

on a fixed small strip in the complex angular variable. The canonical representative is the specified polynomial representative of the finite algebra. The point \(\theta=\pi\) corresponds to spectral value \(-2\); the negative quadratic term measures localization there. Near the all-low maximizing probe index, the Newton polynomial has this strict angular Gaussian. The rest already has a norm gap, which absorbs the Hermite interpolation cost \(\exp(N|y|)\) after shrinking the strip.

There is also a loss-transfer statement. Suppose a boundary module has a fixed coefficient deficit on a compact interval around its index in the all-low maximizing state. That deficit gives a strict loss in \(\|Q_N\|_{\mathcal J}\). Outside the interval, the all-low action already has a gap, and high sectors have their separate gap. This is how a physical color deficit can pass through the unflagged component. The argument does not assert a uniform estimate at this smaller rate for an arbitrary turn applied to an arbitrary polynomial.

## 5. Induction over the tree and all physical colors

The other induction step is supplied by the [decorated-character theorem](actual_conway_decorated_character_spectral_closure.md). A character is the crossing-circle operator \(L_j\), and “decorated” means that the actual input \(E\) is attached before the turn. If \(E\) has norm upper rate \(c\), then

\[
 |[e_r]D_j^\epsilon[E]|\le N^C\|E\|_{\mathcal J}
 \begin{cases}w_{N,r},&r\le M,\\1,&r>M.\end{cases}
\tag{22}
\]

The output norm has rate at most \(c+2G_0\) and its canonical polynomial has the corresponding angular Gaussian. A norm deficit already present in \(E\) passes to every output coefficient.

One must also control the color \(j\) of the newly introduced character. The exact root-character Fourier estimate gives, on every fixed compact interval \(I\subset(0,1/2)\),

\[
 N-j\ge\delta N,\quad r/N\in I
 \quad\Longrightarrow\quad
 |[e_r]D_j^\epsilon[E]|
       \le \exp N\{c+g(r/N)-\eta_{\delta,I}\},
 \qquad \eta_{\delta,I}>0,
\tag{23}
\]

when \(E\) has the inherited strip envelope; \(E=1\) is allowed. This estimate keeps the normal terms and the exact cancellation of the folded Fourier frequency. Its validity on every such compact interval, rather than just near \(1/4\), matters because a boundary module of an unflagged component need not have quarter index in the effective maximizing state.

We can now proceed from the leaves to the flagged root. Products add the established norm rates and multiply the strip envelopes. A flagged step (9) uses (22)–(23) and the absolute constant in (12). An unflagged step (10) uses (19)–(21) and the intrinsic action (13). A deficit in an older descendant travels by its norm loss. A deficit in the distinguished character of a boundary module travels first by (23), then by the all-low localization from §4. This accounts for each physical color of the original expression.

At the root (14), the unturned character has only polynomial cost in the closing functional. A far descendant is handled by its propagated norm loss. If the root color itself is far from \(N\), apply the exact Fourier theorem to the product of the attached representatives, which has the inherited angular envelope. Equation (15) identifies the reference rate with \(F_0\). There are finitely many original colors, so taking the minimum of their positive margins gives one \(\gamma_\delta>0\). This proves (8).

The flag-free cases and the strict two-leaf knot case were already covered by the inputs stated in §3. Therefore (8) holds for every presentation in the theorem, including arbitrary mixtures of flagged and unflagged junctions.

## 6. Restoring the selected packet and performing the fillings

The comparison bands used in §4 are now replaced by the exact physical identity at each original leaf:

\[
 h_j^\epsilon=C_j^\epsilon+(-1)^Nh_{N-j}^\epsilon
 \quad(j>N/2),\qquad h_0^\epsilon=0.
\tag{24}
\]

The term \(C_j^\epsilon\) is the selected core; it is zero for \(j\le N/2\). By multilinearity, the all-core contraction differs from the whole source by finitely many terms with at least one color at most \(N/2\). Estimate (8) with \(\delta=1/2\) makes their total exponentially smaller. This is the [complementary-color principle](actual_conway_weighted_tree_long_twist_volume.md), §4, applied to the physical leaves, not to the auxiliary coefficient bands.

The general core theorem consequently gives

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

A packet is this uniform local asymptotic: a holomorphic exponential action, a nonzero leading amplitude and a controlled error. The action is separately even in the color deficits, and the packet is defined on a fixed complex neighborhood. Its comparison with \(Z_N^\epsilon\) is asserted at the actual integer colors \(\mathbf N-\mathbf h\); the unit phase \(\eta_N\) has not been dropped.

The color Hessian is

\[
 \partial_i\partial_j\Phi_\epsilon(0)
       =-\frac{2\pi \nu_i}{1-\epsilon_i i \nu_i}\delta_{ij},
 \qquad \nu_i=\cot(\pi a_i)>0.
\tag{26}
\]

where \(a_i\) is the complete normalized index of leaf \(i\). Its real part is negative definite. Every such leaf has \(a_i\ge1/4\), so the established high-index and quarter-index packet estimates cover all leaves. For \(H=2\), the both-odd patterns have two main components; the knot patterns contain the pure leaf required by the two-leaf core theorem.

The [source long-filling transfer](general_original_source_long_filling_transfer.md) applies to (8) and (25). Its exact Fourier–Hermite circle-basis identity inserts \(R^{\epsilon_i-2p_i}\) in the same leaf frame, giving the rational tangle (2). For each fixed filling tuple the coefficient mass is polynomial in \(N\), so the global exponential error remains negligible.

For independently sufficiently long fixed signed slopes, the transfer gives a nonzero leading amplitude with selected exponent

\[
 S_{\epsilon,\mathbf p}(\chi_*)
 =\Phi_\epsilon(\chi_*)+
          \frac{\pi i}{2}\sum_i\frac{(\chi_{*,i}-1)^2}{p_i},
 \qquad dS_{\epsilon,\mathbf p}(\chi_*)=0.
\tag{27}
\]

The point \(\chi_*\) is the critical point of the displayed filling action. The theorem controls the whole transform, including endpoint currents and nonzero Fourier charges; it does not assign a contribution to a formal saddle without checking its contour.

## 7. Identifying the exponent with the knot complement volume

The geometric identification uses the original tangle presentation, not a rearranged comparison circuit. The marked geometric theorem constructs its nearby augmented-link representation with primitive peripheral logarithms and the calibrated complex-volume primitive

\[
 U_i=-2\pi i\chi_i,\qquad V_i=-2\partial_i\Phi_\epsilon,\qquad
 G=2\pi i\Phi_\epsilon,\qquad
 \operatorname{Vol}(\rho_\chi)=
       \Im G-\frac12\sum_i\Re U_i\Im V_i.
\tag{28}
\]

Here \(U_i,V_i\) are the meridian and longitude logarithms in the stated convention. The function \(G\) is the regulator primitive; its imaginary part, with the displayed boundary correction, is the representation volume. The stationary equations in (27) become

\[
                              U_i+p_iV_i=-2\pi i.
\tag{29}
\]

The marked metric completion gives a primitive angular turn of \(2\pi\) and hence a smooth complete finite-volume metric on the exterior obtained by these disk fillings. Every auxiliary crossing-circle cusp is filled to insert its twists. The main knot cusp stays unfilled. At this solution,

\[
 2\pi\Re S_{\epsilon,\mathbf p}(\chi_*)
       =\operatorname{Vol}(S^3\setminus K_\tau(\mathbf n)).
\tag{30}
\]

There are finitely many auxiliary cusps, so one common neighborhood in the reciprocal filling slopes suffices. Combining its geometric threshold with the analytic transfer threshold proves (4). The [one-cut normalization](actual_complete_augmented_source_normalization.md) contributes its specified polynomial factor and unit framing character, neither of which changes the logarithmic limit.

## 8. Scope of the conclusion

The theorem includes the earlier completed-root and weighted-tree families and all strict mixtures of their source junctions. The finite test is (3), equivalently at most one flagged leaf per reduced hub. Branching, valence and depth may be arbitrary finite quantities. The argument does not require a character at every hub.

The earlier manuscript retains its stated completed-root theorem. This extension uses the existing exact two-leaf and single-attachment certificates together with the probe and spectral propagation arguments above. It does not replace their proofs by numerical asymptotics. The linked notes provide the detailed local estimates used in the assembly.

The [pointed quantum \(A\)-period corollary](actual_conway_pointed_quantum_a_volume.md) combines (4) with the all-level ADO annihilator and finite-pointing theorems. It expresses the same limit through a genuine recurrence operator, its fixed initial data and bounded-order derivatives in the quantum parameter.

The result does not classify every arborescent presentation, provide a threshold uniform over growing trees, or establish a short-twist theorem. Identifying the selected classical main-meridian geometric factor and its quantum module with the marked regulator germ is a further problem. The source identities used for estimates do not assert tangle isotopies: the original expression supplies its own packet and marked geometry in §§6–7.
