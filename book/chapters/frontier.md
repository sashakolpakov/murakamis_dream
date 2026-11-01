# What remains to be proved

This chapter keeps completed constructions and exploratory methods in
one place while recording what each method still needs. A geometric
metric, an exact finite quantum formula and a bound selecting its leading
contribution are three different inputs. When all three have been proved
for a stated class, the volume limit is a theorem for that class even if
another route to it remains incomplete.

The first sections describe the covered knot families and their remaining
parameter restrictions. The later sections follow alternative
representations of the invariant: shared face coefficients, external
colors, smoothing, Fourier periods and local operator curves.
Each link leads to the precise hypotheses and normalization used by that
approach. The [notation chapter](notation.md) fixes the level, color,
meridian and twist conventions.

## The planar decoration result and the remaining general problem

The [balanced decoration theorem](../../notes/actual_balanced_terminal_fan_volume.md)
now gives a full invariant equality for a class without a tangle-tree
hypothesis. Start with any simple triangulated sphere and a chosen
perfect matching of its dual. The proof constructs its actual augmented
link, circle packing, and a finite two-sided terminal decoration. Every
original and added region can then receive independently sufficiently
long signed twists. With the chosen knot parity, the resulting knot has
the hyperbolic volume limit through all integer levels.

This settles the full complementary-source estimate for those decorated
diagrams: one shared complete packing satisfies the strict local
inequalities, which give an exponential bound for the entire remainder.
The geometric leading term is nonzero, and primitive completion identifies
its action with the actual knot-complement volume. The proof includes
general Morse diagrams, where cups and caps may occur between boxes.

For the unchanged simple matched sphere, the [geometric contribution](../../notes/actual_morse_geometric_contribution.md) is now established directly from the original Morse source. Its [entire Fourier period](../../notes/actual_morse_cross_filling_period.md) is nonzero at sufficiently large levels of both parities, and its exponential rate is the volume of the original complement after independently sufficiently long fixed signed fillings. This statement concerns the central recurrence-path contribution, called central in the finite formula; it is not a new invariant or a full-invariant volume theorem.

The undecorated problem is the strict bound for the full source minus
that geometric contribution. A simple white sphere alone does not yet
supply this bound, and adding tangles generally changes the knot.
There is now an unchanged-diagram sufficient condition:
[weak balance in the complete packing](../../notes/general_weak_balance_volume.md)
permits equality in the local comparisons and still proves the full
volume limit. The condition and the mechanism are explained below.
Arbitrary short fillings, cores with loops or repeated white edges, and
the general volume conjecture remain outside the planar result. This
result is at the complete main meridian; extending its full meridian
family and operator consequences is also separate work.


One part of that spectral problem is now settled more broadly. After all
other face coefficients have been extracted, the
[uniform cap estimate](../../notes/research_cap_uniform_spectral_gap.md)
controls one signed contribution for every value of its cap parameter in
\([-2,2]\). For the recorded 54-region source, exact rational certificates
put it strictly below the augmented volume rate. A
[general response criterion](../../notes/research_cap_dirichlet_response_region.md)
proves the same type of bound for exteriors satisfying its explicit
inequality. Both results use odd levels and hold the other spectral
parameters at \(-2\). Thus they settle a restricted term of the remainder;
they do not supply the full supremum required below.


### What remains after the finite filling estimate

The [uniform filling estimate](../../notes/actual_uniform_filling_supremum_bound.md)
separates two parts of the calculation. After taking the common face
coefficient, let \(S_N(\sigma_1,\ldots,\sigma_r)\) be the resulting
spectral polynomial. Applying the original twist functionals gives
\[
 |Z_N(\boldsymbol n)|
 \le \prod_{e=1}^r(1+|n_e|/2)\,
                       \|S_N\|_{[-2,2]^r}.
\]
The diagram and twist powers are fixed, so this factor adds no
exponential growth as \(N\) increases. The proof retains derivatives
at double spectral roots and the simple endpoint at odd levels.

For a term containing a one-sided local factor, that coordinate costs
at most \((N-1)/N\), independently of its twist power. The full
complementary polynomial vanishes on the product of the spectral
node sets. This yields a bound without first taking the absolute
value of each local path.

The missing estimate concerns the supremum of that shared
complementary polynomial: it must lie strictly below the augmented
geometric rate. Such a gap would make it negligible beside a
separately established nonzero geometric term for sufficiently long
fixed fillings. The full spectral polynomial is independent of the
twists; bounding it at the augmented volume alone cannot prove the
smaller filled volume. Thus the finite norm result simplifies the
remaining estimate without adding a new knot family to the volume
theorems.

More explicitly, let \(C_N\) be the contribution obtained by selecting
the central recurrence paths at every crossing region, and put
\(\mathcal D_N=S_N-C_N\). A sufficient estimate is
\[
 \limsup_{N\to\infty}\frac1N
    \log\|\mathcal D_N\|_{[-2,2]^r}
       \le \Phi_D-\eta,\qquad \eta>0,
 \qquad \Phi_D=\frac{\operatorname{Vol}(Y_D)}{2\pi}.
\]
The finite functional bound then controls the filled remainder.
The nonzero central contribution has a rate tending to \(\Phi_D\)
as all fixed twists become long. Choosing their threshold so that
its volume drop is less than \(\eta\) gives the full invariant
limit. This is the precise use of an augmented-source gap in a
filled-volume theorem. A direct estimate of the filled remainder
could also suffice; a uniform spectral supremum bound is a method,
not part of the volume conjecture itself.


## The completed recursive constructions

The volume limit is proved for fixed ordered cylindrical tangle compositions whose reduced net twists are sufficiently long and whose closed diagram is a knot, with elementary two-strand braid closures excluded. The [results chapter](results.md#arbitrarily-many-tangles-with-sufficiently-long-net-twists) defines the reduction and its size condition. For this class, the theorem concerns the full invariant and the volume of the actual knot complement.

The remaining questions include short net twists outside the explicit criteria below, knot families outside these constructions, and identification of the full recurrence ideal beyond the selected geometric factor. The alternative plat methods below have their own open hypotheses. Those hypotheses are not missing steps in the proved Conway theorem.

## The boundary of the current Conway theorem

The [net-twist theorem](../../notes/actual_conway_net_twist_volume.md) removes the requirement that the original written expression pass the strict type test. Its explicit isotopies bring integral twist boxes together, retaining the half-turns of intervening tangles. The resulting groups of twist numbers are fixed by the original expression. The output is either a strict template or an elementary braid closure. The large-twist hypothesis applies to the sums in those groups.

The analytic inputs now include both the [complete-value strict-tree theorem](../../notes/actual_conway_all_strict_tree_long_twist_volume.md) and the [moving-meridian theorem](../../notes/actual_main_meridian_filled_volume.md) for every fixed strict tree. The topological reduction transfers the whole zero-framed meridian family to the same filled knot in its original presentation. It carries the meridian and preferred longitude as well, so the intrinsic volume and cusp expansion transfer with the invariant. The lower bounds on twist length still apply to the surviving sums.

A small nonzero surviving twist remains outside this long-net-twist theorem; the quantitative circle-tree theorem below covers some such cases. Making the original written exponents large by inserting opposite twist pairs cannot remove it. Exact zero sums can be treated by a further topological reduction: the [closure extension](../../notes/actual_conway_arbitrary_closure_volume.md) permits cap closures and the resulting connected-sum factors. When the input is hyperbolic and every surviving strict weight is long, the input is isotopic to one covered strict knot. This strengthens the criterion for presentations; it adds no short-twist estimate. For this reduction theorem the threshold depends on the fixed construction. The separate circle-tree criterion below has a twist threshold independent of the tree, but still requires each diagram to be fixed before the quantum limit. Nor does the reduction classify all presentations of a given knot.

There is also a precise operator question. A genuine all-level recurrence for the ADO invariant and finite initial data selecting its solution are already available. The [pointed quantum A-period theorem](../../notes/actual_conway_pointed_quantum_a_volume.md) reconstructs the Kashaev invariant from that data, including the derivatives required at singular steps, and gives its volume limit for the covered knots. The [selected classical geometric factor](../../notes/actual_strict_tree_geometric_characteristic.md) is now identified for every covered strict long-filling presentation, including its bare junctions, and for the circle-tree sources under the summed condition, the local bound \(2^{-120}\), or any [directed certificate](../../notes/actual_all_circle_directed_all_orders.md). Identifying the full quantum module carrying the marked logarithmic regulator remains a further problem. A scalar limit at the complete meridian does not by itself control the invariant as that meridian varies.

## What the actual meridian state requires

The [nearby-zero theorem](../../notes/actual_ado_complete_meridian_zero_accumulation.md) makes the obstruction more precise. For the reduced ADO state in the marked meridian coordinate, the exact values are

$$
F_N(1)=K_N(K),\qquad F_N(q_N)=1,\qquad q_N=e^{\pi i/N}.
$$

The first value has positive exponential growth for the knots covered above. The second point is only order $1/N$ from the first. The crossing formulas give a Laurent degree bound of order $N$; factoring that polynomial then proves that actual zeros approach $M=1$ within distance $O(1/N)$. Consequently the unchanged state cannot have a holomorphic, nonvanishing branch asymptotic on a fixed neighborhood of completeness.

The same ordinary-color values force a boundary factor in every polynomial annihilator. In the squared coordinate $Y=M^2$, write the shift as $\mathsf S Y=q^2Y\mathsf S$. The [peripheral normal-period theorem](../../notes/peripheral_normal_period.md) gives

$$
P=B(Y-1).
$$

Its formerly conditional positive-growth hypothesis is now satisfied for the covered knots. Removing the factor changes the state: $B$ annihilates $(Y-1)F_N$, which vanishes at completeness, and the original invariant is recovered from its normal derivative. Localizing the meridian to rational functions discards the corresponding boundary quotient. That quotient and the derivative data must be retained when interpreting the operator geometrically.

An exact regularization is already available. Interpolate the ordinary colors by a polynomial $P_N^{\mathrm{ord}}(Y)$ of degree at most $N-2$, and subtract it before dividing by $S_N(Y)=1+Y+\cdots+Y^{N-1}$. The resulting Laurent polynomial has the same complete exponential rate and satisfies an affine recurrence with a polynomially bounded source. Its shifted values involve derivatives of the original state, so the obstruction above does not apply to it automatically.

For the figure-eight knot, the [meridian profile theorem](../../notes/actual_paired_factor_meridian_profile.md) now controls this regular remainder on the scale $Y=e^{z/N}$ for every fixed compact set of complex $z$. Its centered profile satisfies $\rho_N\to1$, including the ordinary-color resonances and every fixed derivative. The first correction is

$$
N(\rho_N(z)-1)\longrightarrow\frac{\tau}{8\pi i}z^2,
\qquad \tau=2\sqrt3\,i.
$$

Here $\tau$ is the cusp shape computed from the preferred meridian and longitude. The proof obtains the coefficient directly from the finite sum; a separate matrix calculation fixes its geometric interpretation and sign.

The figure-eight result includes all fixed complex \(z\)-disks, including the ordinary-color resonances, and identifies its correction with the preferred cusp shape. For every fixed strict Conway presentation with sufficiently long signed twists, a separate argument proves the actual reduced ADO profile on \(|s|\le R<1\), where \(M=q_N^s\). This disk stops before the first ordinary-color resonances.

## The filled moving-meridian theorem and its remaining limits

The [filled-meridian theorem](../../notes/actual_main_meridian_filled_volume.md) proves

\[
\sup_{|s|\le R}
\left|\frac{2\pi}{N}\log|F_N(q_N^s)|
 -\operatorname{Vol}(S^3\setminus K)\right|\longrightarrow0,
\qquad R<1,
\]

for every fixed strict Conway tree with independently sufficiently long fixed signed twists and the original knot and framing conditions. A bare junction is a product junction containing no crossing-circle operator. Its valence, adjacency to other bare junctions, and the size of its component impose no additional restriction. The [general component proof](../../notes/actual_main_meridian_general_component_comparison.md) controls the whole signed calculation. The earlier separated-junction, path and trivalent proofs remain valid special cases.

The invariant is nonzero throughout the stated disk for sufficiently large $N$. If $A_N(s)$ is the exact crossing-and-framing scalar specified by the finite source, its normalized profile is

\[
\frac{F_N(q_N^s)}{F_N(1)A_N(s)}
 =H_N(s)\bigl(1+O(N^{-1})\bigr),\qquad
 H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)}.
\]

The lower bound comes from a nonzero term in the joint Fourier calculation. All Fourier indices are compared with the same filled critical action, so the fixed twist magnitudes need not be comparable. One presentation-dependent threshold works before choosing $R<1$; the starting quantum level may depend on the chosen twists and radius.

The [longitude calculation](../../notes/actual_main_meridian_preferred_cusp.md) identifies the first correction with the preferred cusp shape $\tau_K$:

\[
 \frac{F_N(q_N^s)}{F_N(1)H_N(s)}
 =1+\frac{\pi i s^2\tau_K}{2N}+O(N^{-2}).
\]

The [exact scalar calculation](../../notes/actual_main_meridian_exact_scalar.md) retains the integer framing term, and the geometric proof determines the preferred longitude after the auxiliary surgeries. Both the geometric identity and this asymptotic now cover the same strict-tree class. The [net-twist and closure corollary](../../notes/actual_main_meridian_filled_volume.md#net-twists-and-other-conway-closures) transfers the intrinsic formulas to their reduced-knot presentations under the stated hypotheses on twist length and topology. It uses ambient isotopy of the zero-framed knot and its preferred peripheral curves; it does not identify different augmented links.

The remaining limits are substantial. The disk shrinks like $1/N$ in the meridian coordinate and stops before $s=\pm1$, the first ordinary-color resonances. The general ordinary-color-subtracted state has not been continued through those resonances with the asserted profile. Short surviving twists outside the criteria below, trees or twist numbers growing with $N$, and a classification of all arborescent knots under arbitrary presentation changes remain outside the present results. Arbitrary bare-junction valence and adjacency impose no additional restriction on the strict long-filling volume, profile or selected geometric-factor theorems.

## A local bound independent of the number of tangles

For ordered circle trees with at least one edge, the [directed subtree theorem](../../notes/actual_all_circle_directed_volume.md)
proves the actual knot-volume equality if, at every vertex,
\[
                    |n_v|\ge2^{27}\quad\text{or}\quad d_v\ge2^{28}.
\]
Here \(n_v\) is its signed crossing power and \(d_v\) is the
number of incident edges. The choice is independent at
different vertices. The original strand pairing must give
one knot without an internal closed component. The tree and
all its powers remain fixed as the level grows.

The full criterion is more flexible than these two displayed
bounds. It assigns separate decay estimates to the exact
polynomials obtained from subtrees and allows any vertex to
be evaluated last. The final scalar needs no outgoing bound.
Nonvanishing and the error estimates are proved for the actual
finite traces, including all Fourier endpoint terms. The
selected action is identified with the volume of the original
knot complement through the marked positive filling path.

At a sufficiently high-degree vertex the crossing power can
be short or zero. One may also attach an even stack of long
odd terminal pieces at each vertex of an arbitrary fixed
core with a knot pairing. The [results chapter](results.md#one-twist-threshold-for-arbitrarily-many-tangles)
explains the exact construction. It preserves the endpoint
pairing but generally changes the knot, so it supplies
covered enlarged knots rather than a theorem for the
unchanged short-twist core.

The earlier local condition
\(\max_v d_v/(d_v^2+n_v^2)\le2^{-120}\) remains valid, and
the summed theorem below remains useful for individual
diagrams. A weaker [geometric condition](../../notes/actual_all_circle_vertexwise_geometry.md),
\(\sqrt{d_v^2+n_v^2}\ge630\) at each vertex, already constructs
a positive path and smooth completion. That condition alone
does not prove the quantum volume limit.

The outstanding analytic problem is to cover more of this
geometric region and other short-twist constructions. For cyclic
interaction graphs, the planar decoration theorem and the
unchanged-diagram balance or finite-sector criteria have their
own long-filling hypotheses; the tree induction does not apply
to them automatically. Diagrams
growing with \(N\) remain outside both proofs. The
[directed all-orders extension](../../notes/actual_all_circle_directed_all_orders.md)
now supplies the shifted-chart estimates for every directed certificate;
a leading profile alone would not have supplied that conclusion.

## Short twists covered by the quantitative theorem

For the ordered tree construction in which every junction carries a
crossing circle, the [quantitative theorem](../../notes/actual_all_circle_quantitative_volume.md)
now proves both the finite-sum asymptotic and its geometric volume
interpretation under

\[
 \sum_v\frac{d_v}{d_v^2+n_v^2}\le2^{-25}.
\]

Here \(d_v\) is the number of branches at the circle and \(n_v\) is
its fixed signed crossing power. The original strand pairing must
give a knot. A large degree can compensate for a short or zero power;
the [results chapter](results.md#an-explicit-bound-that-also-permits-some-short-twists)
gives concrete sufficient bounds and the construction in words.

The earlier analytic proof left one geometric issue: its small angular
coordinates did not force the accumulated primitive meridian logs to
be small. That issue is resolved for this class. The original ordered
cut gives two octahedra per tree edge. Their positive deformations
retain the complete face maps and the primitive periods throughout a
cone-angle path from zero to \(2\pi\). Its endpoint is a smooth metric
on the original knot complement. The calibrated action is its volume.
The preferred main-cusp calculation also continues along this path,
so the first meridian correction has the same geometric meaning.

The remaining question is to enlarge this numerical region and the
class of constructions. The bound is conservative, arbitrary short
coefficients need not satisfy it, and the proof does not cover graphs
with cycles or growing trees. The selected classical geometric factor is now identified for these
circle trees; comparison of the full quantum modules remains separate. No missing
global source theorem is being assumed for the knots that do satisfy
the displayed criterion.

## What the full expansion now forces on the recurrence

A knot-group representation assigns determinant-one complex matrices
to based loops. Restricting it to the boundary torus gives commuting
meridian and longitude matrices. Their eigenvalues on one common line
are denoted \(M,L\). The algebraic curve obtained from these peripheral
eigenvalues is the classical curve of
[Cooper, Culler, Gillet, Long and Shalen](https://web.math.ucsb.edu/~cooper/14.pdf);
the A-polynomial records its one-dimensional image in the chosen
peripheral coordinates. A selected geometric factor refers to the
irreducible component through the marked hyperbolic representation.

An all-level annihilator is instead an operator identity for the quantum
invariant as its color or meridian changes. Its shift and multiplication
operators do not commute. The *first nonzero classical symbol* is the
commutative polynomial obtained at the first nonvanishing order after
the classical specialization. Proving that the geometric factor divides
this polynomial is weaker than identifying the entire recurrence ideal,
its multiplicities, or every component of the A-polynomial.

The [filtered characteristic theorem](../../notes/actual_main_meridian_filtered_characteristic.md)
uses the whole microscopic expansion, with estimates on the shifted
parameter neighborhoods required by the recurrence. Its highest
polynomial terms determine an analytic action \(\mathcal S(u)\),
where \(u=\log M\). For any specified genuine all-level annihilator
with first nonzero classical symbol \(P_0(M,L)\), it proves
\[
                   P_0(e^u,-e^{\mathcal S'(u)})=0.
\]
Thus the source selects a whole classical curve germ, rather than
only a tangent at completeness. The selected irreducible factor is
reciprocal under \((M,L)\mapsto(M^{-1},L^{-1})\).

There is also an explicit rational longitude expression:
\[
 L_{\mathrm{eff}}(M)
 =-M^{a(D)}\prod_e\frac{M^2-E_e(M)}{1-M^2E_e(M)},
 \qquad E_e=e^{2\pi i x_e}.
\]
Here the product runs over physical quarter-turn edges of the
original tangle tree, and \(x_e\) is the corresponding scaled internal
index. The integer \(a(D)=-w(D)-\sum_i n_i\) retains the oriented writhe
and signed twist powers in the prescribed framing. The \(x_e\) are
determined by the modified stationary equations in the theorem. For the
circle trees the note writes those equations as a finite rational
system. The denominator factors and the first-charge logarithms
are retained.

The [strict-tree geometric longitude theorem](../../notes/actual_strict_tree_geometric_characteristic.md)
identifies this entire curve for covered strict long fillings,
including bare product junctions. The circle-tree proof also
applies under the earlier summed condition, the local
bound \(2^{-120}\), and now every directed certificate by its full
shifted-chart expansion. The construction permits a nonparabolic
main meridian and retains the original puncture paths under
half twists. Its proof rules out an
extra rational function of \(M\), including at the trace-zero values
\(M=\pm i\), before using the cusp tangent to fix the framing exponent.
The complete negative longitude lift fixes the remaining sign.

At a bare junction, an added zero-crossing circle is removed
by meridian filling. The proof retains the ordered based
puncture loops and identifies the stationary elimination
with the original product action, even at a possible
half-edge fold. This supplies the actual knot-group
interpretation required for the strict-tree extension.

The selected complex geometric irreducible factor therefore
divides the first nonzero classical symbol of each genuine
all-level reduced annihilator in those source classes.
The conclusion passes through the covered marked net-twist
and closure isotopies, which preserve the full invariant
family and preferred peripheral curves. It does not identify
the full A-polynomial, factor multiplicities or the entire
quantum module. Extensions to knots outside these classes, including the newly decorated planar families, require their own moving-meridian and operator proofs.

## The moving-meridian growth already established

The [source-growth theorem](../../notes/actual_main_meridian_source_bounds.md), extended by the [general component comparison](../../notes/actual_main_meridian_general_component_comparison.md), controls every fixed strict Conway tree before its auxiliary crossing circles are filled. It retains the full ranges of their independent colors and the original component hypotheses. Its early separated-junction examples illustrate one included case, not a current adjacency condition.

Write $Y^\epsilon$ for the augmented complement with its crossing circles unfilled, and \(\mathcal F_{N,\mathbf j}^{\epsilon}(M)\) for its reduced scalar with auxiliary colors \(1\le j_i\le N\). For \(q_N=e^{\pi i/N}\) and every fixed \(0\le R<1\),

\[
\lim_{N\to\infty}\frac{2\pi}{N}
 \log\sup_{\substack{|s|\le R\\\mathbf j\in\{1,\ldots,N\}^{H}}}
 |\mathcal F_{N,\mathbf j}^{\epsilon}(q_N^s)|
 =\operatorname{Vol}(Y^\epsilon).
\]

The upper bound is uniform in the meridian disk and all auxiliary colors. Its matching lower bound uses the nonzero complete value at \(s=0\), \(j_i=N\); it does not assert nonvanishing at every point of this color cube. Both even and odd levels are included. The two-piece case retains its original knot-pattern and pure-leaf qualifications.

The [auxiliary-color gap](../../notes/actual_main_meridian_auxiliary_color_gap.md) also extends to every such tree. If some \(j_i\le(1-\delta)N\), with fixed \(0<\delta<1\), the scalar has a strictly smaller rate than \(\operatorname{Vol}(Y^\epsilon)/(2\pi)\), uniformly over the other colors and both parities on \(|s|\le R<1/2\). This smaller disk is the scope of that strict color estimate, while the source supremum theorem holds for \(R<1\).

The reference volume here is still the augmented volume. The filled theorem uses the additional joint Fourier argument and the marked filling geometry to obtain the volume of the original filled knot complement. An upper bound for the augmented source alone would not supply that conclusion.

## What is now exact when the main meridian moves

The [oriented tangle calculation](../../notes/actual_main_meridian_newton_compiler.md)
now keeps the two strand directions throughout a Conway construction.
A strand and its reverse carry the dual colors \(V_+\) and \(V_-\).
Pairs of equally directed strands have a moving Casimir polynomial;
pairs with opposite directions have a constant one. Turns connect
these different spaces through the original evaluation and
coevaluation maps. Treating every pair as one unchanged algebra
would lose that distinction.

Several parts of this calculation are proved uniformly in the level.
Changing the normalized Newton basis costs at most a polynomial in
\(N\) on each bounded microscopic meridian disk, and the inverse
change has the same property. An exact trace pairing recovers every
coefficient of the physical tangle. Although repeated turns can
produce higher apparent poles during a recursive calculation, every
final coefficient has at most a simple ordinary-color pole.
The primitive closing trace supplies exactly
\(H_N(z)=\sinh(z/2)/(N\sinh(z/(2N)))\). The prescribed ordinary-color
subtraction remains necessary at its zeros.

The [physical quarter-turn comparison](../../notes/actual_main_meridian_turn_comparison.md)
now controls all six orientation types. With the complete Newton
polynomials kept fixed, a turn applies a paired sine-product
multiplier and then reverses the coefficients. The multiplier and its inverse are
uniformly bounded on every disk \(|s|\le R<1\). A positive kernel
on the distinct Casimir nodes, combined with the exact trace
pairing at the repeated nodes, also proves a full spectral-jet
comparison on \(|s|\le1/16\): the deformed turn and the complete
turn of the same polynomial differ in norm by at most polynomial
factors in \(N\). The formula is exactly even in \(s\), with an
explicit first \(N^{-1}\) correction for indices away from both
ends.

The [multiplication formula](../../notes/actual_main_meridian_newton_multiplication.md)
shows exactly how this algebra changes. At completeness a product
of Newton basis elements with indices \(i+j\ge N\) vanishes.
Moving the meridian generally makes it nonzero. The formula gives
the signs of the resulting coefficients and their exponential
rates when the normalized indices stay away from the boundary.

Their nonzero first derivatives have a precise explanation: the
Newton basis itself moves. Keep the complete basis fixed instead.
The relation defining the algebra then changes only by
\[
\Delta_s=2\cos(2\pi s)-2.
\]
Since \(\Delta'_0=0\), multiplication in these fixed coordinates has
zero first derivative. Multiplication by the Casimir changes by
one matrix entry, of magnitude \(|\Delta_s|/N^2\).
This simplifies the algebraic deformation, but additional multiplication terms still occur. The general component proof estimates their signed whole traces. In a trace difference, the first Fourier term cancels; with one high index the remaining terms admit a reflected complete-tensor bound. Complementary pairing then fuses junctions in a positive comparison tree, whose maximum rate cannot exceed that of the original tree. A separate half-boundary argument handles several high indices. These are bounds on complete contractions, not isotopies, and the original geometric volume remains the target. A local norm estimate alone would not suffice: for a radical polynomial whose node derivatives are supported at one end, the second color derivative of the paired multiplier has a derivative of polynomial size at the other end. Localized node data alone therefore do not imply the analytic localization needed in the source proof.

There is a second route through the recurrence. The
[finite matrix criterion](../../notes/actual_main_meridian_finite_matrix_criterion.md)
retains the whole finite-cut operator before root specialization,
including its first derivative in the quantum parameter. In the
central variable \(U=Y^N\), the minors used to describe its kernel
have bounded Laurent degree. The original finite sum separately
bounds the degree of the selected state's free coordinates.
Their normal equation therefore becomes a linear system whose
number of unknown coefficients is independent of \(N\).

Uniform conditioning of that system, together with the stated
reconstruction bounds, would prove a volume limit on a fixed small
disk in \(z\), hence on a meridian disk of radius \(O(1/N)\).
For the covered knots, the right side would remain the volume of
the same knot complement. The criterion is proved; its conditioning
hypotheses have not been verified for a general Conway family.
The filled-meridian theorem above reaches a uniform volume limit and normalized profile by a direct finite-sum argument. It does not establish the conditioning hypotheses of this alternative matrix criterion. Proving those hypotheses would provide an operator-based proof and could address further meridian or knot regimes; it is not needed to remove a bare-component restriction from the finite-sum theorem.

## What the Fourier transform preserves

The Fourier transform gives an exact algebraic correspondence, but one must keep the equations produced by the starting point of the color sequence. Write $Q=q^2$, let $T$ shift the color, and let $S_Xg(X)=g(QX)$. The substitution

$$
Y\longmapsto S_X,\qquad T\longmapsto X^{-1}
$$

preserves the quantum-torus relation $TY=QYT$. Applied to the finite-start generating series $Z(q,X)=\sum_{n\ge n_0}C_n(q)X^n$, an annihilator produces an inhomogeneous equation $AZ=\mathcal B$. The nonzero term $\mathcal B$ is fixed by finitely many initial colors. It is part of the transformed equation.

The [Fourier and boundary-factor note](../../notes/actual_mellin_boundary_multiplicity.md) proves two restrictions on using this correspondence. At a root of unity, rational meridian functions satisfy $T^N=1$, whereas rational Mellin functions satisfy $S_X^N=1$. Under the substitution above, these give different equations on the center. Their finite orbit fibres meet at $Y^N=T^N=1$, where the discrete Fourier transform matches the meridian values with the Mellin residue numerator. This finite transform alone does not identify either function as its parameter varies. A finite matrix lift through the quantum parameter is impossible: the relation would force $Q^N=1$ even to first order away from the root.

There is also a specific multiplicity obstruction for the covered positive-volume knots. Their factorization $P=B(Y-1)$ becomes $A=\Phi(B)(S_X-1)$, so $A$ kills constants. Homogenizing the actual sourced equation therefore leaves two independent rational solutions: the constant function and $Z_N$. The associated monodromy has an eigenvalue-one eigenspace of dimension at least two. A simple eigenvalue cannot be the hypothesis used to select the invariant in this presentation.

The source still distinguishes the two solutions: $A(1)/\mathcal B=0$ and $AZ_N/\mathcal B=1$. The prescribed series also starts at degree $n_0>0$, which excludes the added constant. These are exact selection data. The remaining geometric comparison must preserve them, the regular meridian data, and the functional giving $K_N$. The finite Fourier identity and its norm identity alone do not supply that comparison.

## Language used in the alternative routes

The remaining sections concern several exact representations of the invariant. A **source** is a finite polynomial, tensor contraction or sum that equals the specified invariant after its indices are contracted. A **coupon** is one local operator in that contraction, usually attached to a crossing circle or twist box. A **color** is an integer representation label in the finite calculation.

A **shared-face coefficient** is obtained by assigning a variable to each face of a diagram, multiplying the local polynomials, and extracting the prescribed power of every ordinary face variable. The same face has one variable wherever it occurs. Taking separate local maxima would discard this constraint. The two faces at the mark are protected: their variables are set to zero in the appropriate coefficient formula.

A **spectral parameter** is a variable in the polynomial functional calculus of a local operator. Repeated spectral nodes require values and derivatives; the first derivative data are often called normal terms. A derivative in this spectral variable is different from a derivative in the quantum parameter $q$.

An **action** is the function whose value gives an exponential rate, usually in an expression of the form $e^{N A}$. A **local packet** includes that exponential, a nonzero leading coefficient and a uniform error near a selected critical point. A **period** is the contour or finite Fourier expression used to reconstruct the invariant. Showing that one packet exists does not prove that its period dominates every other term.

A **sector** fixes one piece of the exact local path partition at
each crossing region. The central piece is denoted \(C\), or central
in the technical formulas; \(L,R\) denote the two one-sided pieces.
A genuine sector retains one such choice at every region. An
**envelope** is an upper bound for its absolute value. Replacing
several alternatives by their maximum can make the envelope larger
than the original sum. A lower bound for that optimized envelope
therefore does not give a lower bound for the signed source.

## The general plat target and its quantifiers

A $2k$-strand plat is a braid closed by pairing neighboring endpoints at the top and bottom. Fix a diagram $D$, its crossing-circle augmentation $Y_D$, and the actual meridian-longitude markings. The [general plat target](../../notes/general_augmented_plat_long_twist_target.md) asks for a threshold $T(D)$ such that every knot-producing fixed signed twist tuple with $\min_i|m_i|>T(D)$ satisfies

$$
\lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K_{D,\mathbf m})|
=\operatorname{Vol}(S^3\setminus K_{D,\mathbf m}).
$$

The diagram and twist tuple are fixed before $N$ grows. The threshold is allowed to depend on the diagram, not merely on the number of strands. The [geometric filling theorem](../../notes/general_augmented_plat_long_filling_quantifiers.md) supplies the geometric part under its positive marked gluing hypothesis. A quantum source estimate is a further requirement.

One finite geometric certificate is the [simple-white criterion](../../notes/general_simple_white_plat_class.md): the actual white cellulation must be a simple triangulated sphere with the specified matching. It allows separating triangles and arbitrary fixed width. It supplies a labeled convex ideal right-angled polyhedron for the cut diagram. It does not assert that every hyperbolic plat passes the test or that the presentation is minimal.

Several explicit families already satisfy the required source estimates. The [one-end layer family](../../notes/general_one_end_layer_long_filling_volume.md) works at every fixed width $k\ge2$. The [bridge-gap extension](../../notes/general_simultaneous_bridge_gap_filling_volume.md) permits independent fixed insertion depths, and the [marked unit-chain operation](../../notes/general_marked_unit_chain_filling_volume.md) adds arbitrarily many regions to its specified cores. Their constructions and thresholds are explained in the results chapter. The [Fox-coloring argument](../../notes/actual_fox_coloring_exact_plat_bridge.md) gives exact bridge number under an additional congruence; the [earlier reduced-layer theorem](../../notes/general_reduced_layer_long_filling_volume.md) is a separate included family. These are not classifications of all plats at those widths.

![A comparison packing used in the explicit family at arbitrary fixed width.](../figures/symmetric-plat-balance-seed.png)

![Independent circle-chain insertions in the first-layer bridge gaps.](../figures/each-bridge-gap-chain.png)

![The marked unit-chain extension preserves the original core packing.](../figures/marked-unit-chain-extension.png)

## The complete augmented source is understood

Before the crossing circles are filled, the [signed augmented-source theorem](../../notes/general_signed_augmented_source_volume.md) proves the complete-link equality

$$
\lim_{N\to\infty}\frac{2\pi}{N}\log|A_{D,N}|
=2\operatorname{Vol}(Q_D)=\operatorname{Vol}(Y_D).
$$

Here $Q_D$ is the labeled ideal right-angled polyhedron for the cut diagram, and $A_{D,N}$ is the marked complete-circle source with its framing normalization. Retained half-twists may independently have sign $0,+1,-1$. Both level parities and composite levels are included. The theorem does not manufacture the geometric certificate for an arbitrary diagram. The [coverage comparison](../../notes/general_untwisted_augmented_source_literature_coverage.md) explains prior overlaps and why parallel belts with a white bigon fall outside this certificate.

The algebra behind the result is useful more generally. The [homogeneous source theorem](../../notes/actual_homogeneous_casimir_face_source.md) assigns to every Casimir-polynomial coupon $f_e$ a homogeneous polynomial $H_{f_e}$ of degree $d=N-1$ in its four face variables. The exact marked contraction is

$$
Z_N=\left[\prod_{f\ \mathrm{ordinary}}L_f^d\right]
\left.\prod_e H_{f_e}\right|_{L_u=L_v=0}.
$$

The bracket means coefficient extraction, and $u,v$ are the two marked faces. The identity keeps the cup, cap, mark, parity and endpoint factors. The finite face grid and total degree rule out extra whole-level aliases; one does not choose an order for eliminating interacting operators.

![Local four-face polynomials are joined by one coefficient extraction with shared face variables.](../figures/homogeneous-face-source.png)

For a complete circle, the [positive face-polynomial formula](../../notes/actual_complete_circle_positive_face_polynomial.md) uses

$$
D_a(x,b,y)=\det\!\left[bI+\frac{x}{2}H_-+\frac{y}{2}H_+\right],\qquad
\widetilde P_s(x,y)=\sum_{j=0}^s\frac{S_s}{S_jS_{s-j}}x^{s-j}y^j,
$$

where $H_\pm$ are the specified positive Hermitian matrices, $S_j=\prod_{r=1}^j2\sin(\pi r/N)$, and $s=d-2a$. Their coefficients are nonnegative and their combined degree is $d$. The [marked coefficient theorem](../../notes/actual_original_marked_face_coefficient.md) gives the entire source as the sum over folded labels $a$ of these shared coefficients, multiplied by the explicit source scalars, multiplicities and half-twist phases. The normalization includes the factor $N^R$ for $R$ crossing circles. Even-level carries cancel only in the whole marked expression.

The geometric rate follows from a sequence of global results. The [transverse rank theorem](../../notes/actual_original_boundary_transverse_rank.md) removes the two framing directions and fixes the common scale. The [positive coefficient saddle theorem](../../notes/actual_positive_face_coefficient_saddle.md) controls the entire coefficient torus and gives a nonzero Gaussian contribution. The [absolute action calculation](../../notes/actual_original_boundary_stationary_character.md) cones the actual facets and fixes the additive volume constant. The [uniform channel-rate theorem](../../notes/actual_positive_face_channel_rate.md) controls all folded labels at the same radii.

Near the maximal folded label $M=\lfloor(N-1)/2\rfloor$, write $a_i=M-t_i$ and $s_0=N-1-2M$. The sector ratio has the relative form

$$
\frac{F_N(\mathbf M-\mathbf t)}{F_N(\mathbf M)}
=\exp\!\left[-\sum_i C_{i,N}\frac{t_i(t_i+s_0)}N\right](1+o(1)),
\qquad C_{i,N}>0.
$$

The exact half-twist phases sum to the nonzero factor $(\pi N)^{R/2}\prod_i(C_{i,N}-\pi i\epsilon_i)^{-1/2}$. Thus the signed conclusion does not follow by discarding phases from the positive proof. The estimates control the intermediate and macroscopic tails as well as this central window.

![The face directions and marked transverse slice used in the coefficient saddle.](../figures/face-potential-rank.png)

## The positive endpoint and its unique geometric maximum

Another useful comparison source is the positive spectral endpoint.
This paragraph retains the theorem's certified original flat-plat
scope. The general Morse source identity alone does not extend its
forest reduction to an arbitrary matched sphere.
For even $N$, the [endpoint theorem](../../notes/general_fejer_endpoint_source_volume.md) gives rate

$$
W_D=\frac{\operatorname{Vol}(Y_D)}{2\pi}
$$

for the marked source with $P_N=-V_N(-2)=4(2+\Omega_N)^{-1}$ at every crossing region. Here $\Omega_N$ is the Casimir operator and $V_N$ its polynomial resolvent numerator. This comparison source is not the filled knot invariant.

The [closed half-block estimates](../../notes/actual_fejer_half_block_entropy.md)
and [full-kernel identity](../../notes/actual_fejer_full_kernel_entropy_identity_reduction.md)
give a continuous local entropy \(h(\boldsymbol a_e)\). The vector
\(\boldsymbol a_e\) records the four face exponents at region \(e\),
divided by \(N\); their limiting sum is one. Entropy here means the
limiting logarithm of a positive coefficient divided by \(N\).
Every degree-\((N-1)\) monomial occurs in the full positive kernel,
so the global rate is the maximum of \(\sum_eh(\boldsymbol a_e)\)
subject to the original shared-face demands. At an ordinary face
the incident loads sum to one, and at a protected face they are
zero. If individual central and one-sided patterns are retained,
the [finite-level support test](../../notes/actual_fejer_shared_entropy_variational.md)
also checks the integer offsets that the limiting polytope can miss.

Several reductions prove that this maximum is geometric. [Identity-forest contraction](../../notes/actual_fejer_diagonal_identity_forest_reduction.md) removes pure-middle identity coupons without changing targets. The [hybrid Hall reduction](../../notes/actual_fejer_hybrid_tight_cut_reduction.md) keeps cross factors as two triangle rows and one-sided factors as single rows. [Boundary regularity](../../notes/actual_fejer_nondiagonal_maximizer_regularity.md) recovers positive shared multipliers on the resulting pieces. The [representation assembly](../../notes/actual_fejer_hybrid_piece_representation.md) then constructs a representation of the original augmented-link group with relative volume $2\pi W_D$.

That volume calculation uses the [signed cut-ball regulator chain](../../notes/actual_fejer_signed_cut_ball_regulator.md). It does not assume that an open regulator remains unchanged when its reference flag is reset. The previously found fixed-degree convexity counterexample is also not used as a false shortcut. The [unique-maximizer theorem](../../notes/actual_fejer_unique_geometric_maximizer.md) identifies the only maximizing flow with the marked complete geometry. Compactness gives a strict gap outside every fixed neighborhood, but not a gap uniform over all diagrams.

Identity insertions have a strictly lower rate or give zero, because the resulting representation kills an essential meridian. The [serial-coupon estimate](../../notes/actual_fejer_serial_coupon_bound.md) separately shows that a fixed literal chain on one ordered pair changes the positive source by at most a polynomial factor. It does not justify replacing arbitrary separating cuts by serial chains.

Odd levels need the independent spectral derivative. The [odd regularization theorem](../../notes/actual_fejer_odd_regularized_full_numerator.md) uses

$$
F_N=\begin{cases}
-V_N(-2),&N\text{ even},\\
V_N(-2)-N^{-2}\partial_\sigma V_N(-2),&N\text{ odd}.
\end{cases}
$$

It has the same local entropy and global rate. If $S_N$ is the shared contraction of the numerators, then

$$
|\partial_{\boldsymbol\sigma}^{\alpha}S_N(-2,\ldots,-2)|
\le e^R\alpha!N^{2|\alpha|}Z_{D,N;F_N}.
$$

This derivative is in the spectral parameter, not in $q$. Positive path estimates also control shrinking complex disks. The [spectral complement theorem](../../notes/actual_fejer_spectral_polydisk_complement.md) carries the strict one-sided gap to a small fixed neighborhood, with explicit cost $\sum_e\operatorname{arcosh}(1+r_e/2)$ for disk radii $r_e$.

## From a local packet to a whole filling period

For the same certified original flat plats, the
[full spectral packet theorem](../../notes/general_full_spectral_numerator_geometric_packet.md)
gives a nonzero asymptotic for the entire numerator on a fixed
complex neighborhood of \(\sigma_e=-2\). For general simple-sphere
Morse diagrams, the [proved packet](../../notes/actual_morse_cross_filling_period.md)
at this stage concerns its central contribution. Keeping this
distinction, the full flat-plat packet has the following form,
with \(\sigma_e=-2\cos(2\pi\delta_e)\):

$$
S_N(\boldsymbol\sigma(\boldsymbol\delta))
=(-1)^{(N-1)R}
\frac{N^{2R}e^{N A_N(\boldsymbol\delta)}}
{(2\pi N)^{(R-1)/2}\sqrt{\det H_N(\boldsymbol\delta)}}
\bigl(1+O(N^{-1})\bigr).
$$

The finite action $A_N$ and normalized Hessian $H_N$ come from the one shared-face saddle, with the original parity offsets and mark. The square root is continued from its positive value. Convergence of $A_N$ alone would not justify replacing it by its limit inside an exponential; the proof keeps the finite action until the end.

The local inputs are the [exact cofactor factorization](../../notes/actual_cross_cofactor_factorization.md), [ordinary-middle packet](../../notes/actual_cross_cofactor_interior_packet.md), and [protected-middle packet](../../notes/actual_cross_cofactor_protected_packet.md). [Interpolation rigidity](../../notes/actual_cross_cofactor_interpolant_rigidity.md) proves exponential accuracy for the actual off-node polynomial, rather than for an arbitrary interpolation of repeated-node values. The [global angular estimate](../../notes/actual_cross_cofactor_global_angular_gap.md), with its separate [protected-middle proof](../../notes/actual_cross_cofactor_protected_angular_gap.md), bounds the rest of the coefficient torus.

The [marked-action theorem](../../notes/actual_cross_cofactor_marked_action.md) fixes the peripheral normalization. Restoring half-twists gives

$$A_{\boldsymbol\epsilon}=A_0+\pi i\sum_e\epsilon_e\delta_e^2,
\qquad U_e=\partial_{\delta_e}A_{\boldsymbol\epsilon},\qquad V_e=-4\pi i\delta_e.$$

Here $U_e,V_e$ are the chosen logarithmic meridian and longitude variables. For crossing exponent $n_e=\epsilon_e-2p_e$ and Fourier charge $\ell_e$, the critical equation is $U_e+p_eV_e=-2\pi i\ell_e$. At the unit-charge long-filling branch, the boundary correction cancels the Gaussian terms and gives the actual filled volume.

The [local charge comparison](../../notes/general_local_charge_critical_monotonicity.md) makes the unit charge strictly largest in a fixed scaled box, with a lower gap proportional to $\sum_i(\ell_i^2-1)/n_i^2$. This compares critical values only. The [localized-period theorem](../../notes/general_localized_unit_charge_filling_period.md) additionally moves the original cube to the finite saddle, keeps all joining currents, and proves a nonzero Gaussian coefficient. All $2^R$ unit-charge signs contribute equally. Neither local statement by itself controls remote charges.

The [whole cross-period theorem](../../notes/general_all_cross_long_filling_volume.md) supplies that global control for the central source sector. The [complete-radius balance theorem](../../notes/general_complete_radius_balance_filling_volume.md) then controls the entire complementary source when its hypothesis holds. Its algebraic sufficient test is

$$ (x+y+b)(x+y+c)\ge\max(b^2,c^2), $$

using the four curvatures from one common complete packing. The [triangle balance lemma](../../notes/actual_triangle_entropy_algebraic_balance.md) proves this test, while the sharper [zero-middle $9/4$ estimate](../../notes/actual_zero_middle_nine_quarter_balance.md) covers the explicit every-width family even when the simpler product test fails. The [global one-sided estimate](../../notes/actual_global_left_weighted_spectral_envelope.md) is uniform over the phases of that shared coefficient torus.

For arbitrary certified plats, the unresolved issue is a replacement for balance when it fails. It is not a missing local geometric coefficient. The [fixed-root scope note](../../notes/fixed_root_direct_power_scope.md) also explains that this route does not require a generic-$q$ normal theorem.

### Weak balance and a shared change of weights

The [weak-balance theorem](../../notes/general_weak_balance_volume.md)
applies directly to the original simple-sphere Morse diagram.
At each crossing region let \(x,b,c,y\) be its complete curvatures
and let
\[
 X_e=Q(x,b,y)+Q(x,c,y).
\]
The source-normalized triangle potential \(Q\) is the angle
maximization defined in the [notation chapter](notation.md#circle-packings-shapes-and-geometric-actions).
The hypothesis is \(X_e\ge\log b\) and \(X_e\ge\log c\) for
positive middles; a protected zero middle has no one-sided term.
This condition permits equality.

The proof changes only the weights in Cauchy's coefficient estimate.
Write \(q_f=\log w_f^*\) for the positive complete curvatures and
replace them by \(e^{(1-t)q_f}\), with \(0<t<1\). The protected
weights stay zero. The complete shared action
\[
 P(q)=\sum_{\text{triangles }a}Q_a(q)-\sum_fq_f
\]
is stationary at \(q\), so its change is quadratic in \(t\).
The entropy of the triangle containing an overloaded middle is
strictly positive, giving a linear loss for each surviving
one-sided choice. For a sufficiently small common \(t\), the
linear loss exceeds the entire quadratic cost. Every genuine
noncentral sector is then below \(\Phi_D\) on the same weight
vector. The finite filling estimate and the nonzero general-Morse
central period give the volume of the original filled knot.

The changed weights need not form a packing. They are parameters
of an estimate and do not change the diagram, its metric or its
peripheral curves. The theorem also gives an explicit tolerance
for a small positive balance defect. It does not assert that some
choice of mark makes every diagram weakly balanced.

![The cross period has the filled-volume rate. A bound for the whole complementary source is needed beyond the diagrams satisfying balance.](../figures/shared-entropy-frontier.png)

## The classified global upper problem

The [global sharp majorant](../../notes/research_global_sharp_coefficient_limsup_majorant.md)
controls every allowed degree and real spectral parameter.
Let \(\boldsymbol a\) record the normalized face loads just
described, and let \(\mathcal P_D\) be their compact feasible
polytope. Write \(H_\delta(\boldsymbol a_e)\) for the upper rate
of a coefficient at region \(e\), with spectral variable
\(\sigma_e=-2\cos(2\pi\delta_e)\). Then

$$
\sup_{\boldsymbol\delta}|S_N(\boldsymbol\delta)|\le e^{N(M_D+o(1))},\qquad
M_D=\max_{\boldsymbol a\in\mathcal P_D,\;\boldsymbol\delta\in[0,1/2]^R}
\sum_eH_{\delta_e}(\boldsymbol a_e).
$$

The source path decomposition names the central part the cross sector and the two one-sided parts the left and right sectors. In normalized degrees, cross means that both middle loads are at most $1/2$. A seam is their boundary; a non-cross load overloads one middle face. Exceptional cap corners meet both protected faces.

[Boundary activation](../../notes/research_full_fiber_sharp_boundary_activation.md) and [stationary classification](../../notes/research_full_fiber_sharp_stationary_classification.md) leave only complete cross factors, strict straddling one-sided factors and at most two marked caps at a maximizing configuration. The [seam theorem](../../notes/research_sharp_cross_degree_domination_and_seam_gap.md) proves $H_\delta\le h$ on all cross degrees. If $a_D$ is the smallest geometric middle deficit, its seam gap is $\pi a_D^2/2$. The entire seam-neighborhood filling period is exponentially negligible relative to the nonzero cross period for fixed sufficiently long fillings.

Consequently, a competing one-sided maximum at or above the geometric
rate \(\Phi_D\) must exceed a middle load of \(1/2\) by a fixed
positive amount. The [odd-cycle obstruction](../../notes/research_stationary_noncross_main_cycle_obstruction.md)
prevents all local phases from being aligned there: a shared face
has one phase, so the separate phase choices preferred by different
crossing regions can be incompatible around a cycle. This does not
give the size of the resulting loss. The
[flat-cap example](../../notes/research_flat_cap_no_local_exponential_angular_gap.md)
also shows why a uniform local exponential phase gap is unavailable.
The remaining estimate must bring the absolute rate below
\(\Phi_D\); a relative improvement over a larger envelope is
insufficient. The [results discussion](results.md#a-global-source-upper-bound-and-the-classification-of-its-maxima)
retains the exact hypotheses of this classification.

## Phase estimates, energy bounds and finite covers

A regular source window restricts local starting and stopping rows away from singular endpoints. The [four-state transfer identity](../../notes/research_original_one_sided_four_state_transfer.md) keeps a before state, an active two-state block and an after state, including the direct diagonal path. The [positive active transfer](../../notes/research_positive_eta_word_transfer.md) controls an outer phase mismatch. The [analytic switching theorem](../../notes/research_analytic_switching_suppression.md) controls a middle mismatch while retaining both boundary terms. The [regular-window theorem](../../notes/research_regular_spectral_window_phase_exclusion.md) supplies the strict endpoint losses needed to use that identity.

![The exact transfer, its boundary terms and the regular-window phase loss.](../figures/analytic-source-switching.png)

The [mixed cycle criterion](../../notes/research_mixed_cross_window_cycle_packing.md) permits supported single-protected-face windows and entire cross coupons. Only nonzero incidences have phases. Fractionally packing incompatible cycles yields a shared loss $e^{-\kappa N}$. Its scope is summarized with the local extensions in [the results chapter](results.md#phase-cancellation-on-regular-source-windows). To prove a general invariant bound, the positive majorant rate minus $\kappa$ must still be below $\Phi_D$, and the decomposition must cover the whole source.

A different route uses [one-sided relative energy](../../notes/actual_one_sided_relative_spectral_energy.md). For a coefficient $a_N(q;\sigma)$ and its positive endpoint reference $p_N(q)$, weighted Cauchy bounds the exponential rate of $|a_N|^2/p_N$ by a triangle entropy. The folded-angle rearrangement is uniform through both parities and degree boundaries. The [protected-outer theorem](../../notes/actual_protected_outer_spectral_energy.md) identifies its sharp local value.

The [shared-flow criterion](../../notes/general_endpoint_conditioned_source_energy.md) combines this energy $g$ with endpoint entropy $h$ and another envelope $h_{\mathrm{env}}$, using $\min\{h_{\mathrm{env}},(h+g)/2\}$ on the same feasible flow. A strict maximum below $\Phi_D$ on the non-cross set implies the full filling theorem. Its universal validity remains open in the original flat-plat class. The extension to every matched-sphere Morse diagram is false: the fifty-four-region example below also exceeds the volume rate for this refined score.

![A local energy estimate must still be combined with the shared face demands.](../figures/spectral-energy-rearrangement.png)

The [finite-sector cover theorem](../../notes/general_actual_sector_cover_filling_volume.md) is another sufficient condition. It allows finitely many genuine cross/left/right branches, each with one common weight per face and a strict bound below the geometric rate. It extends the [anchored criterion](../../notes/general_anchored_shared_radius_filling_volume.md). On a fixed seventeen-region marked source, the [separation theorem](../../notes/actual_shared_radius_certificate_separation.md) proves that every choice of shared weights fails one required anchored bound by more than $0.025$, while forty refined branches pass with gap greater than $0.04$. This establishes a strict extension of certificate classes, not a classification of unmarked knots under all possible presentations.

The [undivided-capacity result](../../notes/actual_complete_source_cauchy_capacity_gap.md) explains why a single optimized positive torus can lose exponential accuracy. The [fixed-triangle boundary gap](../../notes/actual_fixed_triangle_boundary_capacity_gap.md) settles certain endpoints, not all fractional mixtures.

There is also a limit to refinement by the three genuine labels.
For a different fixed simple-sphere Morse source with fifty-four
crossing regions, the [singleton obstruction](../../notes/actual_singleton_sector_envelope_obstruction.md)
selects left at region \(32\) and central at every other region.
The shared coefficient of this sector is nonzero at every sufficiently
large even level, so it cannot be discarded for lack of support.
Nevertheless its optimized envelope satisfies
\[
             \inf_{L>0}G_\sigma(L)>\Phi_D+\frac15 .
\]
Here \(L\) is one shared positive weight per ordinary face, the two
protected variables stay zero, and \(G_\sigma\) is the sum of the
selected local envelopes minus the original face demands.
Any branch containing this singleton has at least this cost.
Thus further subdivision only by central, left and right cannot
produce the required bound for this source and mark.

The lower bound is for the envelope, not for the signed coefficient.
It leaves open bounds using its cancellations, a different mark or
presentation, or a direct estimate after filling. It also does not
place the example in the narrower original flat-plat class merely
by realizing it as a Morse diagram. The general source estimate
therefore remains a separate question.

The [absolute-source obstruction](../../notes/research_absolute_source_cancellation_obstruction.md)
shows that the loss survives replacement of these envelopes by the exact
local coefficients. Set the selected spectral variable to \(+2\), and
all the others to \(-2\). At both level parities, the sum of the
absolute values of the original shared-array terms has exponential
rate greater than \(\Phi_D+1/5\). The terms obey every original face
demand. Optimizing arbitrary positive weights in Cauchy's inequality
gives exactly that absolute sum, so changing those weights cannot
recover the lost exponential accuracy.

There is a corresponding positive result about cancellation. On the
same odd levels and at the same spectral tuple, the previously proved
signed cap estimate lies strictly below \(\Phi_D\). Thus summing with
the signs retained removes an exponential amount. This estimate treats
one noncentral region with its neighbors at their endpoint spectra;
it does not control several such regions or the full filling transform.

![Refinement succeeds for the seventeen-region source shown above. The last panel concerns a different fifty-four-region simple-sphere source: one genuine nonzero sector already exceeds the geometric rate in this envelope method. Neither envelope comparison is a lower bound for a signed knot invariant.](../figures/sector-certificate-separation.png)

## The external-color route and its exact cancellations

The external-color method changes the colors of the crossing circles before filling. It must distinguish internal folded-label deficits from external color deficits. The [complete complex-core theorem](../../notes/actual_complete_core_complex_packet.md) gives a nonzero relative asymptotic on a fixed complex color neighborhood. Its finite action $S_N$ and Hessian remain in the formula. The [geometric deformation theorem](../../notes/actual_complete_core_geometric_deformation.md) identifies the limiting action by

$$
2\pi\operatorname{Re}S(\boldsymbol\chi)
=\operatorname{Vol}(\rho_{\boldsymbol\chi})
+\frac12\sum_i\operatorname{Re}U_i\operatorname{Im}V_i,
\qquad U_i=-2\pi i\chi_i.
$$

For real small color parameters $\chi_i$, the boundary correction vanishes and the rate is the representation volume. Complex parameters require the correction. The [varying-action transfer](../../notes/general_long_filling_varying_action_transfer.md) permits the filling calculation to keep $S_N$ until its limit is taken.

The [external reflection identity](../../notes/actual_external_circle_reflection_and_cusp.md) writes a color $N-h$ circle as a cosine-weighted complete term plus the literal color $h$ circle. In the window $h=z\sqrt N$, the complete term has a Gaussian limit fixed by the primitive cusp shape. At the opposite endpoint it has a full-size alias, canceled exactly by the small-color term. A bound for only the complete term would miss this cancellation.

![The cusp rectangles fix the peripheral normalization in the external-color Gaussian.](../figures/cusp-gaussian.png)

The [source-divisor theorem](../../notes/general_long_filling_source_divisor.md) explains why nonzero leading amplitude at one point is not enough for every long slope tuple. A nonzero analytic germ allows an exceptional divisor; an amplitude that is a unit, or a specified coordinate monomial, gives the stronger uniform conclusion. The established complete core has a unit amplitude. The remaining source terms still need their own gap before that conclusion transfers to the invariant.

The finite local equation is also known. The [fixed-fold Fourier period](../../notes/actual_positive_face_fixed_fold_packet.md) gives a four-component difference equation of bounded shift range with its actual finite polynomial solution and characteristic factors. [Exponential fold interpolation](../../notes/actual_positive_face_exponential_fold_interpolation.md) controls the complex extension on the original grid. After face extraction, the equation couples neighboring coefficients; this particular local equation has not been reduced to a scalar knot equation by that elimination alone.

The [coupled face system](../../notes/actual_whole_source_coupled_face_difference_system.md) preserves the shared coefficients and selected fold relation. At a marked double root, the [deformed circle-pattern theorem](../../notes/actual_marked_deformed_circle_pattern.md) recovers the geometric radii and eigenline germs from a nonsingular finite system. The [primitive collar calculation](../../notes/actual_deformed_circle_primitive_collar.md) then fixes the actual disk word and half-twist shear. Its one-side multiplier and the square from a double reflection must not be interchanged.

## Small-circle insertions and smoothing

The [small-circle operator](../../notes/actual_small_circle_polynomial_face_insertion.md) preserves the polynomial ring after all original paths are summed. Apparent negative powers cancel at the physical endpoints, and total degree excludes extra whole-level aliases. A color $h$ insertion costs at most $C^{h-1}$ in the stated weighted norm.

The [simultaneous insertion theorem](../../notes/actual_simultaneous_small_circle_face_correspondence.md) treats every untwisted subset with connected identity smoothing, even with cyclic dependencies or protected outgoing faces. It does not require a global elimination order; the [ordered construction](../../notes/actual_ordered_small_circle_face_insertions.md) is a special case. For disconnected smoothings, the subset contribution is exactly zero when $2\sum_{i\in J}(h_i-1)<N-1$. The demanded face degree exceeds the available degree. Deleted crossing circles carrying a half-twist are outside that untwisted statement.

A geometric gap can be supplied by the [smoothing-capacity condition](../../notes/actual_matching_smoothing_angle_capacity.md) or the [fixed-radius criterion](../../notes/actual_smoothing_fixed_radius_gap.md). A capacity is the optimized exponential bound from the positive angle/weight problem. The latter note includes a matched-graph example where its restricted test fails, but there is no proved adapter making it a counterexample for an original flat plat.

The [capacity decomposition](../../notes/actual_smoothed_source_capacity_blocks.md) handles unattained positive-radius infima. Loops are infeasible, separating two-edge cycles split the capacity additively, and nontrivial simple blocks carry actual right-angled polyhedra. Double-triangle blocks have zero contribution. This decomposition does not move the quantum mark or assert a finite quantum factorization.

The [representation-volume strictness theorem](../../notes/general_representation_volume_kernel_strictness.md) proves a strict gap when the reconstructed representation kills an essential meridian. The [block representation construction](../../notes/actual_smoothed_block_representation_volume.md) extends the argument to degenerate blocks, keeping the original cuts and shaded pairings. It identifies the regulator with the sum of block volumes without claiming that the whole exterior splits geometrically into those blocks.

These ingredients give the [untwisted color corridor](../../notes/general_untwisted_mixed_source_volume_corridor.md): for all sufficiently small normalized deficits on any fixed untwisted subset, the whole mixed source differs from its geometric core by an exponentially small relative error. Both parities are included. Its limit is the volume of the selected marked representation. A complete filled knot metric and a bound on the full complementary color region are further requirements.

For signed replacements, the homogeneous source theorem gives a finite shared-radius certificate. Each unchanged circle contributes its two-triangle potential; each replaced signed circle contributes its four-angle potential, while an unsigned replacement has the sharper $\log\max(b,c)$ bound. Every nonempty reflected subset must have a common face-weight choice whose total rate, after subtracting the demanded face powers, is below the complete rate. These finitely many strict margins absorb the insertion costs on one color cube. Existence of the certificates is not automatic. The [single-circle signed theorem](../../notes/actual_signed_small_circle_face_kernel.md) gives useful special cases and explicit curvature tests.

![The proved small-color corridors and the complementary color region still to be controlled in the general plat route.](../figures/external-color-corridor.png)

The [positive Newton obstruction](../../notes/actual_positive_newton_capacity_obstruction.md) shows that a positive local kernel can have shared capacity above the complete geometric value. Its graph example is not asserted to come from the original flat-plat compiler. The [resummed small-circle kernel](../../notes/actual_resummed_small_circle_face_kernel.md) also has a unique-path coefficient exponentially larger than its crossing reference, even after Newton cancellations. These are obstructions to local norm shortcuts, not counterexamples to a bound after the full signed extraction.

The [peripheral volume-gap theorem](../../notes/general_representation_volume_peripheral_gap.md) gives another geometric tool: keeping a fixed peripheral trace square away from the parabolic value forces a uniform volume loss. Applying it to the quantum source still requires a bound for the whole period, including its finite endpoints and signs.

## Direct twist transport and the classical operator question

The [direct-power identity](../../notes/actual_direct_long_power_source.md) keeps a signed twist power inside its original box. Two kernels on the same pair compose by one coefficient extraction. This retains repeated-node derivative data and avoids introducing an external-color expansion.

The local variables in the next formula are face coordinates, not
the knot's meridian and longitude. Fix the two outer face weights
\(x,y\), and let \(b,z\) be successive middle coordinates in a regular
classical crossing layer. The pair \((b,z)\) is the positive-crossing
companion chart; a negative crossing acts by its inverse, rather than
using the same forward neighboring coordinate. Put \(A=x+y\) and
\(P=xy\). The conserved
parameter \(\sigma\) is the symbol of the original pair Casimir, the
operator on the two representation factors meeting at that crossing.
The [Casimir conic theorem](../../notes/actual_crossing_casimir_torus.md) derives

$$
\sigma=2+\frac{(b+z+A)^2}{P-bz},\qquad
b_{j+1}+\sigma b_j+b_{j-1}+2A=0.
$$

The denominator \(P-bz\) and the other source divisors in the
theorem must be nonzero. On such a regular generic fiber, adjoining a
root of \(\lambda^2+\sigma\lambda+1=0\) diagonalizes the companion
transport on successive middle coordinates. In the resulting multiplicative coordinate, \(n\) crossings
act by multiplication by \(\lambda^n\). Changing the reference point
rescales that coordinate. This is the torsor structure: the group action
is specified, but no point is designated as its identity before making
a reference choice.

At \(\sigma=-2\) the transport has an additive limit. At \(\sigma=2\)
the conic becomes a double line, so its polynomial equation retains a
nilpotent transverse direction. Treating either fiber as an ordinary
generic torus would lose part of the finite source. Neither the symbol
\(\lambda\) here nor a point on this conic is automatically the preferred
longitude eigenvalue \(L\) of a closed knot.

![Generic multiplicative transport and its degenerate endpoint fibers, with the quantum Gaussian retained.](../figures/casimir-twist-transport.png)

The [physical meridian theorem](../../notes/actual_crossing_torus_meridian_transport.md) identifies the local map with the actual crossing move $(A,B)\mapsto(A^{-1}BA,A)$, preserving $BA$, and gives the inverse for a negative crossing. With the cup, cap and mark phases included, every regular layered critical point produces a representation of the filled knot group. This forward construction does not prove that every root of a cleared equation lifts to the regular chart, classify escaping or singular points, or give a nonzero finite-sum coefficient for the geometric branch.

Taking absolute values of all Hermite spectral terms gives an envelope at least as large as the drilled volume. It cannot prove the smaller filled-volume rate. The [spectral total-derivative identity](../../notes/actual_spectral_total_derivative_source.md) therefore keeps the full polynomial numerator, both the ordinary and nilpotent terms at repeated nodes, all nonzero Fourier charges and endpoint currents. Its zero charge vanishes identically.

The [Gaussian numerator formula](../../notes/actual_gaussian_resolvent_numerator_and_cap.md) is

$$
(-1)^{N-1}V_N(-2\cosh w)
=L_N+2\sum_{h=1}^{N-1}\cosh((N-h)w)L_h.
$$

The $L_h$ are the physical-color coupons. This is a polynomial identity, not just an equality of sampled values. It gives a positive majorant near the negative endpoint, and a subexponential closing-cap cost near the other endpoint on a shrinking cap for fixed twists.

The [even cross/one-sided reduction](../../notes/actual_fejer_cross_half_source_reduction.md) partitions the positive numerator into paths crossing the middle rows and paths staying on one side. The crossing part lies between $N H_M/2$ and $3N H_M/2$, coefficientwise, for the maximal complete-channel polynomial $H_M$. The remaining one-sided factors form a rooted forest under the stated diagram hypothesis. They need not vanish, and their half-sized blocks still have level $N$. The [global cross gap](../../notes/actual_global_cross_spectral_gap.md) and whole-period theorem control the cross contribution; a general bound for the macroscopic one-sided complement remains the issue beyond the sufficient criteria above.

The earlier [matching-edge character relation](../../notes/actual_matching_edge_polynomial_geometric_action.md) and [continuant operator period](../../notes/actual_matching_edge_continuant_operator_period.md) remain exact inputs. The [retained alternating Newton equations](../../notes/actual_alternating_newton_peripheral_branch.md) match the primitive-collar trace relation after the specified elimination and rational change of variables. The [local action comparison](../../notes/actual_newton_complete_local_action.md) identifies the selected reciprocal logarithmic action with the complete-core action up to $\pi i$. Its continued critical point lies outside the terminating low-color range, so this germ identity does not select a contributing finite-sum cycle.

For an unrestricted planar diagram, these local comparisons still
need a proof that the ordered closed network selects the geometric
peripheral curve. For the covered strict-tree and circle-tree classes,
that additional identification is supplied by the geometric-longitude
and filtered-characteristic theorems described above. Their proof
retains the based peripheral words, the complete filled representation
and the negative longitude lift. The [source and torsor library](../library.html) retains the different operator, regulator and relative-cycle approaches, including their counterexamples and corrections.

## How the alternatives fit together

For strict Conway trees, the full source estimate and marked filling
argument prove the knot-volume limit. For certified original flat
plats, the positive endpoint and the full local packet are also
established. For general simple-sphere Morse diagrams, the complete
geometry and nonzero central period are established without a balance
assumption. Strict or weak balance, and the stated finite-sector or
shared-flow criteria, supply full-invariant conclusions where their
hypotheses hold. The unrestricted complementary-source estimate is
still a separate problem.

The pretzel, belt, signed Conway, Fourier, weighted-Cauchy, cube and other constructions remain in the [results chapter](results.md) and [research library](../library.html). Their narrower hypotheses should be kept when using them. In particular, a local norm obstruction, a projected cube calculation or an equality of classical actions is not a counterexample to the volume conjecture, and it is not by itself a proof of the full invariant limit.
