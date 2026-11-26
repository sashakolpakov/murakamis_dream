# How the full quantum invariant acquires the knot volume

This chapter follows the completed proof and then explains the local tools used in other presentations. The [methods chapter](methods.md) gives the definitions, elementary examples, and literature references for those tools. The [notation chapter](notation.md) records the conventions needed to compare their formulas.

The main result concerns a particular, already defined knot invariant. For a knot \(K\) and an integer level \(N\), write \(K_N(K)\) for its reduced Kashaev invariant, normalized to be \(1\) on the unknot. The quantum parameter is \(q_N=e^{\pi i/N}\). A diagram computes \(K_N\) by multiplying crossing matrices, joining their indices along strands, and summing the remaining indices. Cups, caps and the marked cut specify how the strands close. In the technical notes, this entire prescribed expression is called the **source**. It includes its scalar factors and derivatives, not just the part that seems largest.

The [strict Conway tree theorem](../../notes/actual_conway_all_strict_tree_long_twist_volume.md) proves
\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K)|
   =\operatorname{Vol}(S^3\setminus K)
\]
for every fixed literal expression satisfying its finite compatibility test, once all independent signed twist weights are sufficiently long and the endpoint pairing gives a knot. A literal expression records the actual order of tangle products and quarter-turns; algebraically equal scalar formulas are not silently treated as isotopic diagrams. The tree and its integer weights stay fixed as \(N\) grows. This is a theorem for the stated class, not a claim that every arborescent knot has such a presentation.

## Why retaining the full expression matters

A color is a representation label on a strand or an auxiliary crossing circle. At a root of unity, two spectral labels can have the same eigenvalue. The value at that eigenvalue then fails to determine the operator: its first derivative in the transverse spectral direction can also contribute. The notes call these derivative terms **normals**. Derivatives in the generic quantum parameter are another kind of normal, so the variable of differentiation must always be specified. Let \(\zeta\) denote the generic quantum parameter before specialization. For example, a factor \([2N]_\zeta\) vanishes when \(\zeta=q_N\) but can have a nonzero derivative there. Deleting it before differentiating changes the prescribed expression.

The full invariant is a signed, generally complex sum. A large term or a large positive upper comparison does not prove that the sum has that size. Two requirements must be met together: the geometric contribution has a nonzero coefficient, and everything omitted from its neighborhood is uniformly smaller. A **packet** in this guide means a local asymptotic formula with its action, nonzero prefactor and controlled error. A **whole-source bound** means a bound on the entire original quantum sum, including all colors and derivative terms.

These requirements have now been proved for the strict-tree class. The older local methods later in this chapter remain useful for other presentations. Their unresolved steps are not unresolved steps in the strict-tree theorem.

## The completed proof for strict trees

The exact tangle recursion supplies the starting point. A physical leaf is a quarter-turned twist operator. Multiplication stacks two tangles in their recorded order, while a turn changes which two boundary strands are regarded as inputs. Expanding these operations in a fixed finite basis gives exact formulas and exact inequalities on the integer indices. After the forced closing index is removed, the remaining indices form a primitive integer lattice: there is no hidden multiplicity from using only a sublattice. This is what permits a local lattice sum to be compared with an integral without losing its normalization.

At complete colors, the factorial weights have a real limiting action: the logarithm of a weight, divided by \(N\), has that limit. The action is a function of the scaled leaf and product indices, subject to the original compatibility equations. It must be maximized with those equations still imposed. Strictness ensures that the maximum occurs where the relevant cell angles are positive. The geometry chapter explains why the resulting cells reconstruct the actual augmented exterior, rather than merely a collection of tetrahedra of the correct total volume.

The local analysis then permits the auxiliary colors to vary slightly in a complex neighborhood. The [general core theorem](../../notes/actual_conway_general_core_packet_and_gap.md) and the [quarter-index theorem](../../notes/actual_conway_quarter_index_color_packet.md) retain the exact recurrence, its boundary data and the original phases. They give a nonzero analytic contribution near the geometric critical point. The quarter-index case is needed because some strict diagrams have a limiting scaled leaf index exactly \(1/4\); it is an equal-modulus boundary for two transfer roots, not a collision of those roots. The proof controls their accumulated contributions instead of inferring dominance from their distinctness.

The remaining difficulty is global: a pointwise estimate on each factor can be too large after the factors are joined. The solution uses two compatible estimates for parts of the tree. A product carrying an actual character operator is controlled by the [decorated-character theorem](../../notes/actual_conway_decorated_character_spectral_closure.md). A connected product region without such an operator is closed against an auxiliary positive comparison polynomial. The [probe theorem](../../notes/actual_conway_unflagged_core_probe_bound.md) bounds that comparison at the region's actual geometric boundary action. The comparison polynomial is used only in the inequality; it does not replace a physical coupon in the invariant.

The [spectral propagation theorem](../../notes/actual_conway_mixed_core_spectral_propagation.md) shows that these estimates survive the next turn and product. Here a spectral norm records both values and first derivatives at repeated spectral nodes. The proof keeps a neighborhood of the unique maximizing indices separate from its complement. In the neighborhood, the actual polynomial factors give angular decay and a local loss when a physical color is far from complete. Outside it, a fixed exponential gap absorbs the polynomial interpolation costs. Induction over the finite tree therefore controls the full expression at the correct action, without assigning the same cost to every turn.

This yields two global facts. Every physical color tuple obeys the required upper bound, and any tuple with at least one color a fixed fraction away from complete has a strict exponential loss. The difference between a full leaf and its chosen local expression is an explicit complementary-color term, called an **alias**. Expanding these differences turns every unwanted term into an actual full quantum evaluation with at least one small color. The global color bound suppresses them. This is why the argument controls all aliases at once; it does not assume that individual absolute-value estimates preserve the cancellations.

Finally, an exact finite Fourier identity inserts the prescribed integer twists into the original leaf frames. The local packet produces a nonzero saddle contribution. Estimates on the whole Fourier domain, including its boundary terms, make the remaining part exponentially smaller. The [marked filling theorem](../../notes/actual_conway_general_mask_marked_filling.md) identifies the resulting action with the volume of the actual knot complement. Only auxiliary crossing-circle cusps are filled. The main knot cusp remains complete and unfilled.

## Subtree estimates with a uniform twist threshold

For the ordered tree construction with at least one edge
and an integer braid at every junction, the [directed subtree theorem](../../notes/actual_all_circle_directed_volume.md)
uses an exact finite recursion with one attaching angle left
free. Its outgoing polynomial always has degree at most
\(N-1\), even for a large subtree. The proof establishes
nonvanishing at angle zero, then divides by that exact value,
retaining its phases and framing factors.

The ratio has a real decay estimate and a complex estimate
on a fixed rectangle. These bounds control the next finite
crossing trace, including its Fourier endpoint terms.
Its first contribution has coefficient one at both level
parities, and the other contributions are strictly smaller.
Different subtrees may use different decay constants. The
last vertex needs no outgoing estimate because its value
is the final scalar.

This gives a finite numerical criterion and, in particular,
the sufficient condition
\[
                  |n_v|\ge2^{27}\quad\text{or}\quad d_v\ge2^{28}
\]
at each vertex independently. Here \(n_v\) is the signed
crossing power and \(d_v\) the number of incident tree edges.
The original strand pairing must form a knot. The theorem
controls its actual invariant and identifies the limit with
its complement volume. The tree and all powers are fixed
before \(N\) grows. This numerical result complements the
strict-tree long-filling proof; it does not narrow that
proof to circle trees.

## The same limit written through a quantum \(A\)-operator

A quantum \(A\)-operator is a finite difference operator in a meridian variable. It is more data than a classical algebraic curve, but an equation alone can still have several solutions. The actual solution is selected here by its original quantum-group definition and finitely many fixed small-color values.

Write \(x=q_N^\alpha\) for the raw representation coordinate and \(M=-q_Nx\) for the marked meridian coordinate. If \(F_N(M)\) is the reduced ADO family in this coordinate, then
\[
 F_N(1)=K_N(K),\qquad F_N(-q_N^j)=C_j(q_N).
\]
The complete point is \(M=1\); \(C_j(q)\) is the ordinary reduced \(j\)-color period. These identities include the original framing and quotient-color conventions.

The [finite cut-state proof](../../notes/finite_sum_annihilator.md) supplies a genuine level-independent annihilator
\[
 P(q,M,T)=\sum_{i=0}^{d}a_i(q,M)T^i,\qquad TM=qMT.
\]
Here \(d\) is the fixed operator order, the \(a_i\) are rational coefficient functions, and \((TF)(M)=F(qM)\). The operator is obtained from the finite quantum formula before evaluating the invariant. It is not defined by a ratio of already known values. The [finite-pointing theorem](../../notes/all_level_a_period.md) then expresses the exact scalar as
\[
 K_N(K)=\operatorname{CT}_{t=0}
 \bigl[r_N(q_N(1+t))\,c_0(q_N(1+t))\bigr].
\]
Here \(c_0\) is a fixed vector of small-color Laurent polynomials, \(r_N\) is the ordered companion-matrix product prescribed by \(P\), and \(\operatorname{CT}\) means the constant term of the whole Laurent expansion. Singular intermediate steps are retained. Only a fixed number of derivatives of \(c_0\) is required, independent of \(N\).

The [pointed quantum \(A\)-volume corollary](../../notes/actual_conway_pointed_quantum_a_volume.md) proves that this exact signed scalar has the knot-volume limit above. It also gives a positive ratio of coefficients of Gram determinants, equal to a sum of squared color periods, with the corresponding volume limit. The signed scalar is not replaced by a matrix norm or by a sum of absolute values. The full ADO normalization is retained as a rational factor whose whole value at \(M=1\) is \(i^{N+3}/N\).

The [strict-tree geometric longitude theorem](../../notes/actual_strict_tree_geometric_characteristic.md) identifies the selected curve with the preferred-longitude deformation for every covered strict long-filling presentation, including arbitrary product junctions without crossing circles. The full microscopic expansion then forces the selected geometric irreducible factor to divide the first nonzero classical symbol of every genuine all-level reduced annihilator. The corresponding earlier circle-tree theorem retains its summed condition or its local bound \(2^{-120}\). These operator conclusions require estimates for the whole expansion on shifted parameter neighborhoods; the leading profile of a new numerical criterion alone is not a substitute. Full quantum-module or recurrence-ideal equality remains a separate problem.

## Other local tools, and their different scope

The rest of this chapter explains methods developed for general augmented plat diagrams. A plat is a braid diagram closed by fixed cups and caps; its bridge width counts the chosen bridges. These results often hold at every fixed width, but some routes below still need a global estimate for unrestricted plats. This limitation concerns that route and class. It does not undo the complete proof just described.

A few recurring names have a concrete role. A **channel** is an intermediate representation label in a change of basis. A **Casimir matrix** is the operator whose eigenspaces label those channels. A **\(q\)-Hahn polynomial** is a finite polynomial appearing in an actual matrix column; its root locations can control cancellation. A **resolvent** is \((zI-\Omega)^{-1}\) for such a matrix \(\Omega\). A **Ward identity** is an exact relation between shifted or differentiated terms of the original sum. These objects are used to keep track of the full contraction, not to introduce another knot invariant.

Several notes also use the word **completed** for an operator that combines two colliding spectral channels with their value and derivative terms. It does not mean “a proof has been completed.” A **fold** is the midpoint where the paired channel labels meet. A complex **tube** is a fixed neighborhood of the real parameter region; an estimate on the integer samples alone is not an estimate throughout that tube.

## A finite function of the auxiliary colors

For this subsection, fix one augmented plat diagram. It has \(b\) auxiliary crossing circles, each surrounding two strands in a specified part of the diagram. The auxiliary color \(n_i\), an integer between \(1\) and \(N\), chooses the representation on the \(i\)th circle. Complete color means \(n_i=N\). Its deficit is \(h_i=N-n_i\). The [complete-color formula](../../notes/actual_augmented_plat_phase_compiler.md) and [all-color formula](../../notes/actual_mixed_augmented_plat_compiler.md) compute the original marked scalar from the same crossing matrices, cups and caps for every fixed plat width.

A specified function of noninteger colors is needed because a filling formula is a finite Fourier sum in the physical integer colors. To estimate that sum by stationary phase, one needs a specified analytic function near those samples. An arbitrary interpolation would change the saddle. The [entire color function](../../notes/actual_augmented_plat_entire_core_color_packet.md) constructs the needed finite function directly from the spectral decomposition of the complete-circle operator.

Put \(M_N=\lfloor(N-1)/2\rfloor\). The distinct spectral channels are numbered \(j=0,\ldots,M_N\), with eigenvalues \(c_j=2\cos((2j+1)\pi/N)\). Let \(L_{N,j}\) denote the actual component of the complete-circle operator at channel \(j\), including the derivative-derived term when the node is repeated. For a tuple \(\mathbf j=(j_1,\ldots,j_b)\), define \(A_N(\mathbf j)\) by inserting \(L_{N,j_i}\) at each auxiliary circle and carrying out the original matrix contraction. The fixed half twists, cups, caps, marked trace and external scalar all remain in this coefficient.

Now let \(\chi=(\chi_1,\ldots,\chi_b)\) be a complex vector and set
\[
 \begin{aligned}
 m_j&=N-2j-1,\\
 C_N(\chi)&=
 \sum_{j_1=0}^{M_N}\cdots\sum_{j_b=0}^{M_N}
 A_N(j_1,\ldots,j_b)
 \prod_{i=1}^{b}\cos\!\bigl(\pi m_{j_i}\chi_i\bigr).
 \end{aligned}
\]
Every index and coefficient is therefore fixed by the original diagram. The function is entire because it is a finite sum of cosines. It is even in each variable. When \(N\) is odd, the final frequency is zero and its cosine is exactly \(1\); that endpoint is included.

At physical high colors, substitute \(\chi_i=h_i/N\). The value of \(C_N\) is exactly the term obtained by keeping the complete-circle part of each color identity. This term is called the **core**. The same exact color identity also has a complementary small-color term, called an **alias**. Expanding the product gives \(C_N(h/N)\) plus one explicit term for every nonempty subset of alias choices. This is an identity of full operators, including their repeated-node derivatives. It does not say the aliases are small. At complete colors \(h_i=0\), they vanish, so \(C_N(0)\) is the full complete-color scalar.

Finite Fourier orthogonality recovers every coefficient \(A_N(\mathbf j)\) from the values of \(C_N\) on the grid \(h_i/N\), \(0\le h_i<N\). Parseval's identity then controls a weighted sum of \(|A_N(\mathbf j)|^2\). It does not control cancellation in their signed sum. For unrestricted plats, this finite formula alone does not prove the required complex asymptotic or suppress the alias terms. For the strict Conway class, the later whole-sum argument described above supplies precisely those additional estimates.

## The finite polynomials select a local complex action

After its forced zero is removed, every actual physical q-Hahn polynomial has simple negative real roots. The [proof](../../notes/actual_q_hahn_negative_root_source_polynomial.md) uses an exact sine recurrence, interlacing and sine coefficient operators; the numerical root checks only test the implementation.

Consequently its logarithm, real on the positive axis, is holomorphic on the slit plane. Real factorial estimates first identify its strictly concave positive-axis variational limit. Uniform bounds from the negative roots and the identity theorem then continue the limit to a [uniquely selected holomorphic action](../../notes/actual_q_hahn_selected_complex_action.md). On the physical Fourier arc, the corresponding continued saddle is nondegenerate. This proves the actual local exponential rate while retaining its cancellations.

The [actual amplitude theorem](../../notes/actual_q_hahn_uniform_complex_amplitude.md) now strengthens this to a nonzero prefactor and uniform relative error $O(N^{-1})$. Its proof uses the exact finite difference equation and a real normalization, retaining both original integer offsets. The scaled parameters are the actual values at level $N$, so no rate of convergence of those parameters is assumed.

The [fixed-degree magnetic corridor](../../notes/actual_q_hahn_magnetic_complex_corridor.md) places every magnetic zero outside the physical strip. The new [joint determinant theorem](../../notes/actual_q_hahn_joint_accretive_determinant.md) goes further: the local polynomial is an explicitly normalized determinant $\det(zI+cD+K)$. Here $z,c$ are its scalar variables, $D$ is positive definite and the matrix $K$ is skew-Hermitian, $K^*=-K$. Its positive Hermitian part excludes zeros in a fixed joint domain, including at folded channels.

The [joint amplitude theorem](../../notes/actual_q_hahn_joint_complex_amplitude.md) therefore permits the pair degree and magnetic coordinate to vary together complexly. Exact normalization removes sampling aliases; two original finite shift equations control both derivatives and fix a nonzero amplitude with relative error $O(N^{-1})$. The channel stays an integer. An explicit principal-square-root test identifies the selected local sheet on the central domain.

The [full physical packet theorem](../../notes/actual_q_hahn_full_physical_complex_packet.md) now removes the central-domain restriction on fixed physical compacts. A second determinant uses two positive Hermitian matrices to put its zeros in an angular cone outside the physical sector. This supplies uniform inverse and logarithmic bounds. The source characteristic stays simple, so the same exact two-shift proof gives the selected action and nonzero amplitude throughout the full tube. The necessary finite-level boundary correction is retained.

![The joint domain in the real parts of the two physical wire coordinates, with its degree seam excluded.](../figures/joint-kernel-domain.png)

The [small-channel normal theorem](../../notes/actual_q_hahn_small_channel_generic_normals.md) retains the original generic source and bounds every fixed derivative by a polynomial times its root value. The [large-partner collision theorem](../../notes/actual_q_hahn_partner_normal_collision.md) expresses the actual paired first normal as a transverse derivative, with its full finite tail. That tail has extra poles, so the ordinary-column domain does not automatically serve the paired normal. The [near-fold complex theorem](../../notes/actual_q_hahn_near_fold_complex_partner_bound.md) now gives subexponential relative cost on a fixed complex compact for $(l-j)\log N=o(N)$. It includes the actual large-channel tail. Fixed nonzero scaled channel shifts and a nonzero normal amplitude remain unresolved.

On the physical integer grid, the [paired-normal bound](../../notes/actual_q_hahn_physical_partner_normal_bound.md) is now proved for every complete double channel: $|w/C|\leq N^6/256+N^2/8$, with $O(N^4)$ cost when the scaled degree stays away from one. This includes the original large-channel contribution. The proof uses a positive imaginary part and the exact double-node reflection; integer samples alone do not extend the bound to a fixed complex neighborhood.

The [physical generic-jet theorem](../../notes/actual_q_hahn_physical_generic_jet_bound.md) controls every fixed q derivative of all admissible physical columns and genuine divided pairs. It uses the actual forward and backward generic recurrences, retaining their distinct offdiagonal coefficients. This supplies higher physical jets without differentiating a root-only identity. It is separate from the complex-domain theorem and from a completed target tensor norm.

The [common-framing criterion](../../notes/actual_augmented_plat_physical_framing_criterion.md) gives finite inequalities for one rank-one projector. The new [right-angled obstruction](../../notes/actual_right_angled_selected_framing_obstruction.md) rules out an all-central selected frame for the certified right-angled decomposition. Generic oriented-strip flags localize the weaker physical-support failures to any two prescribed distinct factors, at any bridge width, including the pair adjacent to the original mark. The [selected-factor localization](../../notes/actual_augmented_plat_selected_factor_localization.md) now puts every other ordinary factor on the selected full physical packet. For an unrestricted plat, this localization still does not identify a contributing integration contour or give a sharp bound on the completed contraction.

Choosing the exceptional pair at one crossing-circle edge gives four external physical representation factors. The [matching-edge scalar](../../notes/actual_matching_edge_racah_positive_scalar.md) is then positive for every target channel, including high partners. The complete-circle [typed block identity](../../notes/actual_matching_edge_marked_four_port_block.md) keeps the original cup, turn, circle measure and marked trace normal. The circle measure cancels its exponential row factor exactly. Only Taylor orders through two are needed after clearing the simple poles.

The [completed-projector identity](../../notes/actual_matching_edge_completed_projector_block.md) now cancels the remaining target scalar normalization exactly. It combines colliding channels before specialization, retaining both their regular projector and nilpotent term. Only first derivatives of these completed operators and the complement remain; the scalar divided difference still includes the necessary second derivatives of the original weights.

The resulting upper estimate is a positive scalar sum weighted by the native completed-projector and complementary-network costs. These costs are not assumed to be subexponential. This makes the remaining norm problem explicit without supplying a lower bound or changing the selected period.

The [native-energy theorem](../../notes/actual_matching_edge_native_projector_energy.md) expresses the first of these costs through original columns and their exact bilinear measures. Every fixed derivative adds only a polynomial factor. The energy itself can grow exponentially: the degree-$t=m$ block of the simple midpoint projector at odd level $N=2m+1$ has rate $v_8/(2\pi)$. The full operator combines its physical degrees in one maximum or square sum; the wire constraints must remain shared when these operators are joined. This rules out dropping the energy as a normalization cost.

The [full matching-graph identity](../../notes/general_matching_graph_full_normal_source.md) is a complementary exact assembly tool: all folded sectors form one generic network with the original physical trace normal retained. It holds at both parities and uses the graph of the actual crossing-disk cut. No vanishing channel norm is inverted.

## The exceptional block is an actual operator period

The [generic polynomial theorem](../../notes/actual_matching_edge_geometric_target_polynomial.md) writes the completed block as $D_a^{-1}p_a(\Omega)$ before taking derivatives. Here $a$ is the retained channel index, $D_a$ is its explicit scalar normalization, $p_a$ is a finite polynomial and $\Omega$ is the actual target Casimir matrix. Its [zeros are all above two](../../notes/actual_matching_edge_racah_root_location.md), so the finite polynomial selects a canonical logarithm and scalar action. The [general generating relation](../../notes/actual_matching_edge_polynomial_geometric_action.md) matches the actual four-parabolic character equation, including the inverse-turn sign and the source's additive scalar anchor.

The spectral parameter of this polynomial is fixed by a specific word in the original meridians. Let \(B_{\mathrm{in}}\) be the determinant-one holonomy matrix of the incoming meridian, with its original basepath, and let \(B_{\mathrm{out}}\) be the corresponding transported outgoing meridian. Let \(c=\cot(\pi x)>0\) be the side ratio of the crossing-circle rectangle in its disk-framed normalization; \(x\) is the rectangle parameter. The inverse cup bend makes the relevant trace
\[
 z=\operatorname{Tr}\!\left(B_{\mathrm{in}}^{-1}B_{\mathrm{out}}\right)
   =2-\frac{4}{c^2}.
\]
This is an ordered group word, not an independently chosen scalar target. The [marked-word theorem](../../notes/actual_matching_circle_rectangle_bound.md) proves \(0<c\le1\) when the rectangle occurs in the actual certified complete manifold, including both half-twist signs. Therefore \(c<1\) gives \(z<-2\), while \(c=1\) gives a genuine parabolic endpoint \(z=-2\). An abstract rectangle with \(c>1\) is algebraically possible, but it cannot realize that marked complete quotient.

A polynomial of degree proportional to $N$ still cannot be replaced by its scalar value inside a contraction. The [exact period](../../notes/actual_matching_edge_continuant_operator_period.md) is

$$p_a(\Omega)=\frac{1}{2\pi i}\oint_\Gamma p_a(z)(zI-\Omega)^{-1}\,dz.$$

Its original Green entries retain both continuants and the full characteristic denominator. The [strict-support theorem](../../notes/actual_matching_edge_cross_central_green_action.md) proves their selected leading action and bounds every fixed generic derivative when the two physical rows straddle the midpoint and $z$ lies in the stated common prefix domain, including fixed compact real intervals below $-2$. On the anti-diagonal they are exactly negative for real $z<-2$. The actual surrounding state is not thereby a positive functional or a continuant eigenstate.

The [finite-propagation identity](../../notes/actual_matching_edge_polynomial_finite_propagation.md) does give exact scalar action on a forward continuant in rows $u\leq t-a$, and on a backward continuant in rows $u\geq a$. These precise windows can leave a central gap. The environment and any complex magnetic continuation remain additional input.

Separate [polynomial](../../notes/actual_matching_edge_polynomial_endpoint_control.md) and [full-resolvent](../../notes/actual_casimir_endpoint_resolvent_bound.md) bounds control the closing point $+2$ and its genuine normals on shrinking neighborhoods. They do not settle the possible geometric parabolic target $-2$, or the contour between the endpoint neighborhood and the candidate saddle. In this general-plat method, one must still estimate that actual contour integral and join it to the surrounding quantum sum without discarding its phases.

## Exact shifts transport finite quantum jets

The [moving-period factorial](../../notes/actual_moving_period_factorial_normals.md) is a specified meromorphic function that equals the original quantum factorial at every supported integer index. With $P=\pi i/\log\zeta$, it satisfies two exact equations:

$$\widehat F_P(z+1)=(1-e^{2\pi i(z+1)/P})\widehat F_P(z),\qquad
\widehat F_P(z+P)=(1-e^{2\pi i z})\widehat F_P(z).$$

At $P=N$, the second equation is also the cyclotomic product of the first $N$ shifts. Their multipliers satisfy the commuting-shift identity. The Gamma product fixes the actual section and its logarithmic marks; the shift equations alone are not a uniqueness theorem.

Put $\Delta=N-P$ and $c(z)=1-e^{2\pi i z}$. The exact fixed-$N$ transport is

$$\widehat F_P(z+N)=e^{\Delta\partial_z}\bigl(c(z)\widehat F_P(z)\bigr).$$

Fix a derivative order $J\ge0$. Modulo the $(J+1)$st power of the quantum deformation parameter, this exponential stops after $J$ derivatives. Away from $c=0$, conjugating by $c$ gives a unipotent operator whose difference from the identity has nilpotence index at most $J+1$. The connection has explicit poles at the integers. They account for genuine normal residues and cannot be removed by root specialization.

The [specified exceptional lift](../../notes/actual_matching_edge_generic_deficient_operator_lift.md) uses this same factorial and the original large white numerators to bound the full generic operator near the actual complex geometric frame. The [boundary theorem](../../notes/actual_matching_edge_degree_cycle_boundary.md) computes what is added when its contour crosses the channel poles. These statements organize the exact source transport; this method still needs a proof that its geometric contribution survives in the unrestricted plat integral.

The [tensor-source connection](../../notes/actual_tensor_source_finite_jet_connection.md) gives a rational gauge for the assembled summand itself. Put $g(z)=e^{2\pi iz}/(1-e^{2\pi iz})$. Its shift ratio is exactly the nonconstant cup multiplier. Products of $g$ and its inverse at the actual ordered cup and cap arguments give a specified gauge $G$. On a primitive free head lattice, the transport in direction $b$ is

$$T_b=\chi(b)\,G\,e^{(N-P)D_b}\,G^{-1},$$

where $\chi$ is the retained parity character and $D_b$ is the directional derivative. These operators commute. On order-$J$ jets, every product of $J+1$ normalized differences from the identity vanishes. Constant head arguments require no gauge factor. The source remains undivided in its original period integral: $G$ can have zeros or poles on the physical lattice, whose boundary terms must still be computed.

The [adjoint connection on the actual period](../../notes/actual_tensor_source_translated_cycle_normals.md) follows by finite-order integration by parts on that unchanged closed cycle. It acts on the original cotangent density multiplied by $G$, producing the required finite-part and double-pole terms. It is an exact relation between specified translated periods, with no claim that a translated head lies in the physical basis or that a geometric contour has been reached.

The [complete local marked-density theorem](../../notes/actual_augmented_plat_local_marked_density.md) then assembles the selected factors with the original unrestricted mark. Their absolute normalization gives a nonzero fixed-channel density. At the complete geometric point, the channel Hessian is diagonal with entries $-4\pi i/\tau_i$, where $\tau_i$ are the actual primitive cusp shapes. After retaining the exact integer characters, the local sum over the original folded nodes is a nonzero Gaussian at both level parities. This establishes a local complete-source coefficient; the framing integral and its appearance in the original global cycle remain to be proved.

The [braided change of cut](../../notes/actual_braided_two_cut_source_adapter.md) keeps this global question within the original source. Transporting a matrix-unit insertion by the recorded braid gives an exact second functional extracting the same marked scalar, with its genuine generic pivot and every derivative retained. The construction is independent of bridge width and permits different Morse levels. It does not eliminate the remaining two-cut array or evaluate the framing integral.

Two further calculations specify that remaining integral. The [local source Ward theorem](../../notes/actual_augmented_plat_framing_density_source_ward.md) proves that its framing density is $-c_D\,dr\wedge ds/[s(1+s)]$, with a nonzero framing-independent coefficient and the original mark retained. The [finite residual-current theorem](../../notes/actual_braided_residual_framing_current.md) supplies the corresponding source-defined off-diagonal bands and exact interval boundary terms. These are distinct results: transporting the actual finite chain to the geometric relative boundary, and evaluating its coefficient there, is still required.

The [common charged head chart](../../notes/actual_matching_graph_common_band_ward_current.md) now constructs the Ward currents meromorphically before contraction, retaining the distinct band-support cycles. At the resonant boundary, [factorial estimates for growing head indices](../../notes/actual_moving_period_factorial_logarithmic_escape.md), [root polynomial packets](../../notes/actual_q_hahn_resonant_hard_edge.md), and the [genuine moving-parameter packet](../../notes/actual_q_hahn_generic_resonant_hard_edge.md) give controlled pieces of the required matching calculation. Their scope is explicit: these pieces have not by themselves evaluated the unrestricted plat integral on its original contour.

## Exact recoupling exposes a local geometric scalar

Four external objects can be paired in two ways. The actual change of basis is computed before root specialization, with its genuine pivotal turn.

![The two pairings of four external representation labels. The internal labels E and G are summed in the actual basis change.](../figures/four-port.png)

The resulting finite Racah sum admits a positive, face-normalized scalar on the supported folded chamber. Its logarithmic rate is the volume of a specific hyperideal tetrahedron. This closes a local algebra-to-geometry step.

It does not yet bound every entry of the completed physical transport in the required metric. A source normalization can have poles or zeros at the root, and complementary channels carry additional normal currents. The [scalar and normal theorem](../../notes/actual_supported_racah_common_phase_and_normal_metric.md) states what is controlled and what remains.

An [exact partner-reflection theorem](../../notes/actual_racah_partner_reflection_identity.md) now proves that all 64 complementary color choices have the same normalized root value. It uses the actual reciprocal source coefficients and residues of channel projectors on a regular invariant lattice. The same work gives an exact counterexample to equality of first normal derivatives. Root-value symmetry therefore helps organize the source without removing the normal-transport problem.

The [all-partner first-normal theorem](../../notes/actual_all_partner_first_normal_bound.md) now controls every supported reflected branch. A positive finite presentation of the complete generic source, combined with the exact Ward and Fourier identities, gives $|K'_B(q)|\leq C N^2(1+\log N)W_N^2$ for the branch-dependent generic tail $K_B$ and its positive normalized scalar $W_N$. It also gives a logarithmic relative bound for the coherent tail itself. The earlier two-current obstruction remains valid for those earlier relations alone; the new source presentation supplies the missing information. General higher normal orders and the completed physical transport metric remain open.

## Weighted Cauchy needs the right energy

For a single complete physical column, write $C_j(t,u)$ for its entry at channel $j$, total degree $t$, and magnetic index $u=0,\ldots,t$. Let $\widehat f$ denote the finite Fourier transform specified by that column. The [exact Plancherel theorem](../../notes/actual_matching_edge_magnetic_energy_profile.md) now proves

$$\frac{N}{j+1}|\widehat f(t/2)|^2\leq\sum_{u=0}^t|C_j(t,u)|^2\leq N|\widehat f(t/2)|^2.$$

The unused Fourier nodes vanish in the original polynomial, so the full discrete Fourier norm equals the actual physical norm. This works at both parities, including a half-integral midpoint. Combined with the exact bilinear measure, it gives the complete-channel energy profile and the full folded operator rate $5v_3/\pi$. Shared magnetic sums and phases remain when these operators are joined.

The [shrinking-fold theorem](../../notes/actual_matching_edge_shrinking_fold_native_energy.md) extends that full real operator rate to every integer sequence $j/N\to1/2$. Fixed generic derivatives add only polynomial cost. This real norm statement permits a wider channel window than the separate complex-normal theorem; it supplies no complex confluent amplitude.

There is also an exact [Fourier compiler for the complete-circle matching source](../../notes/actual_matching_graph_shared_cycle_fourier_compiler.md). Its matching magnetic indices are bounded integral Kirchhoff flows on the graph of physical cycles. The actual cups and caps make every cycle frequency even at both level parities, so its Fourier sums impose coupled congruences. The original mark supplies a one-unit charge. All source phases remain in this finite formula. Cauchy then gives a joint positive comparison of coherent cycle periods with the matching labels still shared.

For a degree-$j$ polynomial $P(w)=\sum_k p_k w^k$ with the positive Fourier coefficients in question, the [coefficient-duality theorem](../../notes/actual_q_hahn_fourier_coefficient_variational.md) compares a coefficient with the best positive-radius bound. Their log-concavity gives

$$p_k\leq\inf_{w>0}P(w)w^{-k}\leq(j+1)p_k.$$

The actual selected source action supplies the corresponding coefficient rate and an explicit positive minimizing radius on compact interior slope families. This is a two-sided local estimate. To use it globally, the actions must be joined on the compiler's flow and charge constraints, with its remaining phases retained.

The [positive Fourier partition](../../notes/actual_matching_graph_positive_fourier_partition.md) now supplies an explicit full-source comparison. Let $R$ be the number of matching circles, $C$ the number of restored physical cycles, and $A_{D,N}$ the original scalar for the fixed diagram $D$. The partition $Z_F(N)$, defined by the exact positive weights of that construction, satisfies

$$|A_{D,N}|^2\leq N^{4R+2C-2}Z_F(N).$$

Every Kirchhoff equation, Fourier congruence and the original marked charge remains in $Z_F$. Its summands are products of positive coefficients and explicit sine-factorial weights. The equality before Cauchy retains all phases; this upper bound does not establish their survival.

The [radial reconstruction obstruction](../../notes/actual_positive_fourier_radial_geometric_obstruction.md) explains a remaining difficulty. At a strict positive radial saddle, all ordinary source factors would lie in the central selected domain. They therefore cannot all assemble into the complete geometric representation of the certified right-angled cut in one frame. This is a conditional geometric obstruction, with no asserted numerical rate gap. The exact phases and the exceptional matching-block route remain essential to investigate.

A useful inequality has the form

$$|K_N|^2\leq e^{o(N)}Z_N.$$

Weighted Cauchy can prove such an estimate once the inner product, original source cost, and dual cost are explicit. Choosing a positive form alone does not make those costs small. The repository contains exact counterexamples to proposed unmarked norms and to replacing a full magnetic tensor by its scalar rate.

The whole-support boundary Gram theorem gives polynomial costs on each supported local cell. To obtain a theorem by this particular method, one must also control how those norms behave when cells are joined. Correlated seam labels must remain shared; maximizing local factors independently can change the answer.

For the specified planar reflection doubles with three boundary representation labels, there is now a stronger [exact full-source identity](../../notes/actual_planar_three_port_reflection_double.md):

$$Z_N^{\mathrm{double}}=\sum_{\mathbf a\in\mathcal D_N}\frac{|Z_N^{\mathrm{half}}(\mathbf a)|^2}{\theta_N(\mathbf a)}\geq0.$$

Here $\mathcal D_N$ is the allowed set of boundary triples, and $\theta_N$ is the original positive boundary measure. Every interior color is already summed, with its phases retained, inside the half-packet. This includes the actual normals at both level parities. Since there are at most $N^3$ boundary triples, the doubled source differs from its largest squared weighted packet by at most that polynomial factor. Its asymptotic is therefore reduced to estimating the half-packets, whose internal cancellations have not disappeared. Positivity here allows zeros and is not a nonvanishing theorem for arbitrary plats.

The retained Fourier phase now has an [exact integer quadratic form](../../notes/actual_matching_graph_centered_fourier_phase.md). The [holomorphic Legendre transport](../../notes/actual_q_hahn_holomorphic_fourier_legendre_transport.md) restores that phase and the original winding characters in the selected ordinary action. Its [global chart](../../notes/actual_q_hahn_global_fourier_legendre_chart.md) is one-to-one on the full physical tube. These are action and coordinate theorems; they do not analytically continue individual finite Fourier coefficients or select the global source cycle.

## What the local estimates can and cannot conclude

For sources with phases, a matching lower bound requires survival of the geometric contribution. A large positive comparison partition does not exclude cancellation in the original invariant.

The [local energy geometry](../../notes/actual_native_magnetic_energy_local_geometry.md) makes this distinction explicit. The highest-weight block at the fold has the volume action of a variable ideal octahedron. Away from the fold, its actual measure forces a signed boundary term. Even at the real energy maximum, the marked complex phase need not be stationary. A global argument must use the original incidence and peripheral conditions to address those phases.

The earlier positive-only Conway theorem used a different route, which is worth distinguishing from the current signed theorem. Exact support is an additive integer semigroup, which approximates a maximizing configuration along every sufficiently large level. Uniform factorial estimates prove the whole-source variational limit. The new geometric argument then proves that the reduced maximum is strict, matches the actual quadrilateral faces, and reconstructs the complete complement of every retained cylindrical factor. The new mixed-color proof supplies the additional filling estimates: exact leaf aliases lie in a square-zero radical, a strict seed-level gap survives arbitrary positive composition, and a finite complex lattice window has a nonzero Gaussian amplitude. This proves the long-full-twist source limit. The separate exact face-map and peripheral construction now identifies its rate with actual filled volume. The unchanged pure grammar still cannot produce knots by those fillings.

Signed half twists change that source and its connectivity. The new [supporting-plane argument](../../notes/actual_odd_conway_uniform_mixed_source_gap.md) bounds any number of propagated aliases by adding tangents to the same global action; the linear terms cancel under the actual wire constraints. A separately checked finite complex packet supplies the nonzero contribution. That earlier result applies to a fixed expression $C(FG)$ whose two children belong to its stated seed-generated grammar. Its marked geometry gives the corresponding filled knot and link equality. The strict-tree theorem at the start of this chapter removes that grammar restriction by the later character/probe induction, while retaining its explicit strictness and knot-pairing tests.

The next boundary pieces now use the same original geometry: [literal prefix signs](../../notes/actual_right_angled_resonant_prefix_signs.md), [generic complemented heads and the outgoing determinant](../../notes/actual_q_hahn_complementary_hard_edge.md), and the [finite negative-clock boundary rate](../../notes/actual_q_hahn_negative_clock_boundary.md). The finite-current theorem also supplies an exact family of band weights that extracts the original root scalar after explicit bounded normalization. At the complete root this functional reduces to the existing coherent cut after a parameter change, so the residual framing freedom remains. This boundary-current route still lacks its unrestricted global internal-period comparison; the strict-tree theorem uses the different global argument explained above.
