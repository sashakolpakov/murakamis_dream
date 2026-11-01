# Murakami’s Dream

## The question and the knots under consideration

For a knot $K$ and an integer $N\geq2$, Kashaev’s invariant $K_N(K)$ is a complex number obtained by evaluating a finite sum at a root of unity. We use the reduced normalization, in which the unknot has value one. If the knot complement admits a complete hyperbolic metric of finite volume, the volume conjecture predicts that

\[
\lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K)|
=\operatorname{Vol}(S^3\setminus K).
\]

The left side measures exponential growth: a value of the form $N^a e^{NV/(2\pi)}$ has limit $V$, because the polynomial factor disappears after taking the logarithm and dividing by $N$. The right side is the volume of the knot complement. The knot remains removed from the three-sphere.

This project studies the conjecture by cutting knot diagrams into tangles and keeping track of how their finite evaluations compose. The main family consists of **Conway algebraic, or arborescent, knots**. These are built from rational tangles by joining and turning pieces. The theorem below applies to specified constructions in this family, with sufficiently many twists in each designated region.

## How the construction works

A two-string tangle consists of two arcs in a ball, with four specified endpoints on its boundary. Draw the ball as a rectangle with two endpoints at the top and two at the bottom. There are two operations. To stack two tangles, put one above the other and join the adjacent pairs of endpoints without adding crossings. To turn a tangle, rotate its entire diagram through a quarter-turn. The order of the pieces matters.

Start with an elementary box containing two strands with an integer number of half twists, and turn that box through a quarter-turn. Make finitely many such pieces, each with its own integer twist number. Repeated stacking and turning gives larger tangles. Finally, stack two such tangles and close the diagram by connecting the bottom-left endpoint to the top-left endpoint outside the box, and likewise on the right. This is the *cylindrical closure* used here. To decide whether the result is a knot, follow all strand connections and count any circles already closed inside intermediate boxes as well as those formed by the final closure.

The construction can have arbitrarily many pieces and arbitrarily deep nesting. It is recorded by a finite ordered tree: its leaves are the elementary twist pieces, and its internal operations are stacking and turning. A tree in this description records a construction; it is not a drawing of the knot.

The [manuscript guide](manuscript.md) gives drawings, worked examples, and the precise recursive class treated in the paper. The [results chapter](results.md) also explains the larger class covered by the companion theorem.

## The volume theorem and its quantifiers

The [net-twist theorem](../../notes/actual_conway_net_twist_volume.md) first simplifies the actual tangle diagram. Integral twist boxes that can be brought together are combined by adding their signed twist numbers. Moving a twist box past a tangle carries a specified half-turn of that tangle, which the reduction retains. The result is either an elementary two-strand braid closure or a presentation passing the strict angle-feasibility test described in the [results chapter](results.md).

For each fixed input construction $\mathcal E$, the reduction partitions the original pieces into disjoint groups $B_1,\ldots,B_s$. Their surviving twist numbers are

\[
W_j=\sum_{i\in B_j}n_i.
\]

The groups are determined before the integer weights are chosen. The order of some surviving pieces can depend on their parities. There is a finite threshold $B(\mathcal E)$ such that, on a non-elementary output, the conditions

\[
|W_j|>B(\mathcal E)\qquad(1\leq j\leq s)
\]

and the requirement that the actual closed link be a knot imply hyperbolicity and

\[
\lim_{N\to\infty}\frac{2\pi}{N}
\log|K_N(K_{\mathcal E}(\mathbf n))|
=\operatorname{Vol}(S^3\setminus K_{\mathcal E}(\mathbf n)).
\]

The elementary output is the closure of a single two-strand braid, hence a torus link or knot; it is excluded from this positive-volume theorem. On a strict output the different net twists may have independent signs and incomparable magnitudes. Original weights within one group can cancel, so their individual largeness does not suffice. For example, two boxes with weights $a+2m$ and $-2m$ combine to the fixed weight $a$, however large $|m|$ becomes.

Choose the entire construction and all twist integers first; then let $N$ grow through the positive integers. The threshold may depend on the construction, but is uniform over its finitely many parity choices. Neither the tree nor its weights grow with $N$.

This covers arbitrarily large fixed compositions when their reduced twists satisfy the bound. It does not cover arbitrary short twists or classify every arborescent knot up to all possible presentation changes. The TeX manuscript proves an earlier included family; the companion strict-tree estimates and exact tangle reduction give the extension stated here. The [manuscript page](manuscript.md) distinguishes those scopes.

The [closure extension](../../notes/actual_conway_arbitrary_closure_volume.md) also permits cap closures, which join each upper and lower endpoint pair, and twist sums that vanish exactly. Removing these zero sums can split the diagram into connected-sum factors. If the input is hyperbolic and every surviving strict factor has long net twists, the proof shows that just one strict factor remains and all others are unknots. The original knot is isotopic to that covered factor. The [results chapter](results.md#cap-closures-and-exact-cancellations) gives the precise criterion, including a sufficient condition on the original subset sums.

## Why the proof has both an analytic and a geometric part

After the exact tangle reduction, the analytic and geometric proof begins by removing the surviving long twists and placing an auxiliary circle around the two strands in each twist region. The resulting *augmented link* remembers where the twists will be restored. Assigning integer labels, called colors, to these auxiliary circles produces a finite evaluation depending on those labels. The notes call this evaluation the *source*.

At each level $N$, the source is an exact finite sum. Its leading exponential growth is described by a real function of the summation indices divided by $N$. Maximizing that function produces angles for ideal hyperbolic cells. The geometric part of the proof shows that these cells fit together with precisely the face identifications of the augmented link complement. This establishes which manifold supplies the volume.

Restoring the twists requires another finite sum over the auxiliary colors. Its terms have complex phases, so their absolute values alone do not determine its growth. The analytic part proves a nonzero leading contribution and bounds the rest of this whole sum. It also follows the chosen geometric structure through the fillings that restore the twists.

Filling an auxiliary crossing circle means removing that auxiliary cusp by attaching a solid torus with the specified slope. The cusp belonging to the knot is left unfilled. Consequently the final critical value is the volume of the resulting **knot complement**, rather than the volume of the augmented link used at the beginning.

![Exact tangle reduction, finite-sum estimates, and identification of the knot complement volume.](../figures/research-map.png)

The [mechanism chapter](mechanism.md) develops the finite sum and its estimates. The [geometry chapter](geometry.md) explains the ideal cells, peripheral curves, and the volume comparison. These two parts are both needed: constructing a hyperbolic metric does not by itself estimate the quantum invariant, and estimating a finite sum does not by itself identify its exponential rate with the volume of a particular complement.

## The quantum A-polynomial formulation

There is also a recurrence formulation. A quantum A-operator is a finite difference operator annihilating the color-dependent invariant. Its coefficients depend on the quantum parameter and a peripheral variable; a shift changes the color. An operator alone generally has more than one solution. Initial values and the prescribed behavior at singular specializations select the solution corresponding to the knot invariant.

The [pointed quantum A-period theorem](../../notes/actual_conway_pointed_quantum_a_volume.md) gives an exact reconstruction of $K_N(K)$ from this operator and finite initial data, retaining the peripheral factors. For the knots covered above, this reconstructed value therefore has the same hyperbolic volume limit. The theorem also gives a positive determinant expression whose exponential rate is the volume.

A further question is how the classical polynomial obtained from the operator selects the geometric component of the knot’s peripheral character variety. That question remains separate from the exact recurrence reconstruction and its established limit. The [frontier chapter](frontier.md) explains the remaining step.

The actual meridian state imposes a concrete constraint: its complete value has volume growth, but its value one quantum shift away is exactly one. The [nearby-zero theorem](../../notes/actual_ado_complete_meridian_zero_accumulation.md) proves that zeros approach completeness at distance $O(1/N)$. A nonvanishing scalar asymptotic for the unchanged state therefore cannot hold on a fixed neighborhood.

There is now a uniform volume limit on smaller disks of the form \(M=q_N^s\), \(|s|\le R<1\), for long-twist presentations satisfying an additional condition on their multiplication junctions. After the prescribed framing and orientation factors are removed, the ratio to the complete value tends to \(\sin(\pi s)/(\pi s)\). The [moving-meridian theorem](results.md#the-volume-limit-while-the-meridian-varies) explains the class and the proof. It stops before the ordinary-color resonances; extending the subtracted state through those resonances and identifying the selected classical geometric factor remain further questions.

## Reading and checking the arguments

Read the [manuscript](manuscript.md) for a continuous account with definitions, proof details, and illustrations. Use [the results chapter](results.md) to compare the exact families and hypotheses, and [the notation chapter](notation.md) when consulting technical notes. The [reproduction chapter](audits.md) distinguishes the finite rational inequalities checked by the supplied programs from the analytic and geometric arguments proved in writing.

The [research library](../library.html) organizes the supporting notes by question. It retains the Fourier, weighted Cauchy, torsor, cube, and other approaches, including estimates that failed and the explanations of their failure. Those historical routes are useful evidence about the problem; they are not additional prerequisites for reading the main theorem.

The [figure gallery](../figures.md) explains what each diagram represents and links to editable sources. The general volume conjecture remains open.
