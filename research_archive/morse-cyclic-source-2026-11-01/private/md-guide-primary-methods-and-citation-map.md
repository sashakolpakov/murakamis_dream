# Primary references and method definitions for the illustrated guide

Checked 1 November 2026. This is a private editorial and coverage map, not an imported proof of any result in the project. The public checkout inspected is `/private/tmp/murakamis_dream-publication`. No public file was changed.

The guide should explain a method, cite the precise external statement or definition, then identify the additional argument supplied locally. The research library may retain unsuccessful approaches and counterexamples. A manuscript theorem should refer only to completed arguments with their hypotheses. A citation is neither a substitute for a missing source estimate nor a reason to suppress an independently proved argument.

## 1. What the present bibliography covers

`manuscript/references.bib` currently contains five entries: Kashaev (1995), Kashaev (1997), Murakami–Murakami (2001), Rivin (1994), and Menal-Ferrer–Porti (2012). Their metadata agree with the primary records inspected. This list does not yet cover most of the guide's named analytic and algebraic methods.

The relevant guide passages occur in `book/chapters/geometry.md` (positive angle structures, regulators, scale torsors), `mechanism.md` (finite Fourier transforms, energy, shared constraints), `frontier.md` (recurrences, boundary factors, torsors, surviving cancellation problems), and `results.md` (weighted Cauchy, positive partitions, completed source theorems and their limits). Local coverage paragraphs already exist in the following notes and should be connected to the guide rather than replaced:

- `general_marked_positive_gluing_certificate.md`, especially §9;
- `finite_sum_annihilator.md`, opening coverage paragraph;
- `regulator_majorization_and_source_energy.md`;
- `actual_fourier_energy_tauberian_criterion.md`;
- `research_routes_and_preserved_ideas.md`;
- `factorial_source_torsor.md`, §10.

The larger `structural_literature_delta.md` is a useful archive of coverage searches. Some entries there explicitly record only an abstract read; those entries should not be promoted to a claim that a complete proof was checked.

## 2. Angle structures and Casson–Rivin optimization

### A definition the guide can use

An angle structure assigns a positive dihedral angle to each opposite-edge pair of every ideal tetrahedron. The three angles of a tetrahedron sum to \(\pi\), and the angles around every internal edge sum to \(2\pi\). These linear equations define an open convex polytope. Its volume function is the sum of the ideal tetrahedron volumes. A critical point means that the derivative of this function vanishes along every allowed infinitesimal angle change.

**Precise primary coverage:** David Futer and François Guéritaud, *From angled triangulations to hyperbolic structures* (2010), [author paper](https://arxiv.org/abs/1004.0440), [full text](https://arxiv.org/pdf/1004.0440). Definition 3.1 defines angle structures; Theorem 1.2 states the Casson–Rivin critical-point criterion for an ideal triangulation of an orientable 3-manifold with torus boundary. The volume and strict concavity are discussed in §5, with the relevant tangent directions constructed in §4. This is the most direct reference for the exact statement used in the guide.

**Historical reference already present:** Igor Rivin, *Euclidean Structures on Simplicial Surfaces and Hyperbolic Volume*, Annals of Mathematics 139 (1994), 553–580, [publisher record](https://annals.math.princeton.edu/1994/139-3/p02), DOI 10.2307/2118572. Publisher metadata were verified; this audit does not claim a new full reading of that paper. It should not be the only reference attached to a more general precisely formulated torus-boundary theorem.

**Local contribution and limit:** `general_marked_positive_gluing_certificate.md` independently proves the marked criterion needed here. An angle structure is not automatically an interior critical point of the chosen volume functional: the maximum can reach the boundary. Nor does a volume maximum prove a lower bound for a signed quantum sum. The guide should identify separately the positive geometric realization, the selected source saddle, and the noncancellation estimate.

**Useful illustration:** an angle polytope with its interior critical point and a separate boundary maximum. Label the latter as the reason that positivity of the domain alone is insufficient.

## 3. Majorization, convexity, and the two different Karamata theorems

### 3.1 Convex majorization

For real vectors with decreasing rearrangements, \(x\prec y\) means
\[
\sum_{i=1}^k x_i^\downarrow\leq\sum_{i=1}^k y_i^\downarrow
\quad(1\leq k<r),\qquad
\sum_i x_i=\sum_i y_i.
\]
Karamata's inequality says that a convex function \(\varphi\) then satisfies
\(\sum_i\varphi(x_i)\leq\sum_i\varphi(y_i)\). The equal-total condition and the direction of convexity must be stated. Weak majorization is a different hypothesis and usually requires an additional monotonicity condition on the test function.

**Original reference:** Jovan Karamata, *Sur une inégalité relative aux fonctions convexes*, Publications Mathématiques de l'Université de Belgrade 1 (1932), 145–148. The [original archive link](https://elib.mi.sanu.ac.rs/files/journals/publ/1/11.pdf) was located, but repeated retrieval failed with a gateway error. It is a bibliographic pointer, not a full-text verification in this audit.

**Verified textbook record for reader definitions:** Albert W. Marshall, Ingram Olkin, and Barry C. Arnold, *Inequalities: Theory of Majorization and Its Applications*, second edition (2011), [publisher](https://link.springer.com/book/10.1007/978-0-387-68276-1). Use this as background reading; no specific unchecked theorem number is needed.

The local note `regulator_majorization_and_source_energy.md` proves the needed finite convex inequality directly. Its application to singular values first proves a logarithmic majorization statement by exterior powers. This is a legitimate independent proof; it should not be called a new general majorization theorem.

### 3.2 Product singular values: one actual attribution correction

Alfred Horn, *On the singular values of a product of completely continuous operators*, Proceedings of the National Academy of Sciences 36 (1950), 374–375, DOI [10.1073/pnas.36.7.374](https://doi.org/10.1073/pnas.36.7.374), is the original product-singular-value reference. The [primary archive](https://pmc.ncbi.nlm.nih.gov/articles/PMC1063207/) and article metadata were checked; the archived first-page text was available, though subsequent PDF access was intermittent.

The linked contemporary paper is **J. Tao, J. Jeong, and M. Seetharama Gowda**, *Some log and weak majorization inequalities in Euclidean Jordan algebras* (2020), [author PDF](https://userpages.umbc.edu/~gowda/papers/trGOW20-02.pdf). Its introduction, equation (1), states the matrix log-majorization and attributes it to Horn; the paper develops Jordan-algebra analogues.

**Correction:** the local link label “Gowda, Some log and weak majorization inequalities” omits two authors and truncates the distinguishing title. Replace it with the full authors and title. Do not attribute the original matrix product inequality to that 2020 paper.

**Application limit:** convex inequalities compare quantities after the relevant vectors or operators have been supplied. They do not construct an insertion-compatible quantum transport, or show that a regulator-preserving positive channel is the actual channel of the knot source. Those are explicitly separate obligations in the local note.

### 3.3 Tauberian Karamata is a different method

For a positive measure \(\mu\) on \([0,\infty)\), a power-law singularity of its Laplace transform can determine the growth of the cumulative mass. Michael Taylor's author lecture note, *Karamata's Tauberian Theorem*, [PDF](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2020/07/karamata.pdf), §1, gives the implication
\[
\int e^{-t x}\,d\mu(x)\sim A t^{-\alpha}
\quad\Longrightarrow\quad
\mu([0,X])\sim \frac{A X^\alpha}{\Gamma(\alpha+1)}
\]
for \(A>0\) and \(\alpha>0\). The indexed first-page statement was verified; direct retrieval was intermittent. This is an author exposition, not the original historical paper.

In `actual_fourier_energy_tauberian_criterion.md`, the positive measure comes from Fourier energies. The local proof supplies this cumulative conclusion independently. An abscissa of convergence gives a limsup, and a cumulative asymptotic does not by itself give the same limit at every quantum level. The note's additional cross-level transport hypothesis is essential.

**Editorial rule:** use “Karamata's convex-majorization inequality” and “Karamata's Tauberian theorem,” not the unqualified word “Karamata” for both. A diagram of partial sums belongs to the first; a Laplace transform and cumulative measure belong to the second.

## 4. Fourier transforms, Plancherel, and weighted Cauchy

For the unitary discrete transform
\[
\widehat a_j=N^{-1/2}\sum_{k=0}^{N-1}a_k e^{-2\pi i jk/N},
\]
finite character orthogonality gives \(\sum_j|\widehat a_j|^2=\sum_k|a_k|^2\). This identity is elementary and can be proved in two lines in the guide. The transform convention should appear beside the formula: an unnormalized transform changes the factor \(N\).

**Verified reader reference:** Audrey Terras, *Fourier Analysis on Finite Groups and Applications*, London Mathematical Society Student Texts 43, Cambridge University Press (1999), [publisher front matter](https://www.cambridge.org/core/books/abs/fourier-analysis-on-finite-groups-and-applications/frontmatter/7898F7935FE41A36DA3AF66E3960C346), [publisher excerpt](https://assets.cambridge.org/97805214/57187/excerpt/9780521457187_excerpt.pdf), DOI 10.1017/CBO9780511626265. The publisher confirms the title, author, year, and finite abelian/nonabelian organization. This is a background reference; no unchecked page-specific theorem is asserted here.

Weighted Cauchy–Schwarz is the finite identity-level tool
\[
\left|\sum_k a_k\right|^2
\leq\left(\sum_k w_k\right)\left(\sum_k\frac{|a_k|^2}{w_k}\right),
\qquad w_k>0.
\]
For a positive definite Gram matrix \(G\), its matrix form is
\[
|\ell^*v|^2\leq(v^*Gv)(\ell^*G^{-1}\ell).
\]
These formulas need no claim of novelty or obscure historical attribution. Explain the weight or metric actually used.

**What is specific to this project:** the physical range of magnetic indices; vanishing at unused Fourier nodes; coupled integer flows; the marked charge; the bilinear measure; and the exponential cost of the dual functional. These are proved in `actual_matching_edge_magnetic_energy_profile.md`, `actual_matching_graph_shared_cycle_fourier_compiler.md`, `actual_matching_graph_positive_fourier_partition.md`, and `actual_filling_fourier_hermite_gram.md\).

**Limit:** Parseval preserves energy, not the phase of a signed contraction. Weighted Cauchy gives an upper bound, not a nonzero leading coefficient. Independent local norms may discard the shared constraints that make the original geometric rate sharp. The finite filling norms and the new exact one-exception obstruction reinforce this distinction; they are not new volume theorems.

**Useful illustration:** the same complex arrows before and after a unitary transform, next to a separate diagram showing how replacing arrows by their lengths loses cancellation.

## 5. Recurrences, quantum operators, and the classical A-curve

A recurrence is an exact equation for a sequence or color-dependent function. If \(M f_n=q^n f_n\) and \(L f_n=f_{n+1}\), then \(LM=qML\). A \(q\)-difference operator is a finite polynomial in these noncommuting operations, with specified coefficient ring. “All-level” means the same operator works before specializing the quantum parameter to each root of unity.

**Primary colored-Jones coverage:** Stavros Garoufalidis and Thang T. Q. Lê, *The colored Jones function is q-holonomic*, Geometry & Topology 9 (2005), 1253–1293, [paper](https://arxiv.org/abs/math/0309214), DOI 10.2140/gt.2005.9.1253. It proves q-holonomicity for the colored Jones function using its multisum structure. Their [*A survey of q-holonomic functions*](https://arxiv.org/abs/1601.07487) is a suitable definitions/closure reference. These are not, by themselves, proofs of the ADO normalization or of a classical geometric-factor statement.

**Primary ADO coverage:** Jennifer Brown, Tudor Dimofte, Stavros Garoufalidis, and Nathan Geer, *The ADO Invariants are a q-Holonomic Family*, [paper](https://arxiv.org/abs/2005.08176), [full text](https://arxiv.org/pdf/2005.08176). Theorem 4.3 gives the q-holonomic family statement. Theorem 4.4 relates an ADO annihilator to the colored-Jones recurrence with the explicit substitution \(A(q^{-1}x,(-1)^{f+1}y;q)\), where \(f\) is framing. Its colored Jones normalization is stated in the theorem. The reverse ideal comparison mentioned in the introduction also uses Willetts's separate result; do not attribute both directions to this paper alone.

**Algorithmic background:** Herbert S. Wilf and Doron Zeilberger, *An algorithmic proof theory for hypergeometric (ordinary and “q”) multisum/integral identities*, Inventiones Mathematicae 108 (1992), 575–633, [author publication page](https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimhtml/multiwz.html), DOI 10.1007/BF02100618. This supplies coverage for creative telescoping of proper hypergeometric multisums. It does not automatically retain the root-specialization boundary terms or the normal data in the present source.

The local `finite_sum_annihilator.md` gives its own finite-boundary and filtered-dimension argument. It should cite prior q-holonomicity plainly while explaining what its exact source construction keeps.

### The classical curve is a separate object

Daryl Cooper, Marc Culler, Henri Gillet, D. D. Long, and Peter B. Shalen, *Plane curves associated to character varieties of 3-manifolds*, Inventiones Mathematicae 118 (1994), 47–84, [author PDF](https://homepages.math.uic.edu/~culler/papers/PlaneCurves/curves.pdf), DOI 10.1007/BF01231526, defines the peripheral eigenvalue curve of representations after choosing a meridian–longitude basis. It is the natural primary reference for the classical A-polynomial.

Stavros Garoufalidis, *On the characteristic and deformation varieties of a knot*, [paper](https://arxiv.org/abs/math/0306230), Geometry & Topology Monographs 7 (2004), 291–309, formulates the comparison of the recurrence characteristic variety with the classical deformation variety as a conjecture and studies examples. Cite it as the origin of that proposed relation, not as a general AJ theorem.

In the guide, distinguish: existence of an annihilator; a selected solution with its starting data; a first nonzero classical symbol; divisibility by one selected complex geometric factor; and equality of complete operator ideals. The locally completed filtered-source theorem proves its explicitly scoped factor conclusion with gauges retained. It does not establish the full A-polynomial with multiplicities, the whole annihilator ideal, or general AJ equality.

**Useful illustration:** a recurrence with several solutions, one highlighted by initial/pointing data, followed by the selected component of the classical curve. This makes clear why the operator alone does not choose the invariant.

## 6. Peripheral potentials, regulators, and torsors

Walter D. Neumann and Don Zagier, *Volumes of hyperbolic three-manifolds*, Topology 24 (1985), 307–332, [author-hosted full text](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1016/0040-9383(85)90004-7/fulltext.pdf), DOI 10.1016/0040-9383(85)90004-7. Theorem 3 and equations (7)–(8) give the symmetry of the peripheral logarithmic derivatives and a local potential; §5, especially equations (46)–(50), relates peripheral differentials to volume. These are local marked deformation statements. A guide citation must retain the meridian/longitude convention and distinguish eigenvalues from eigenvalue ratios; it cannot silently import the project's filling signs or primitive period.

Walter D. Neumann, *Extended Bloch group and the Cheeger–Chern–Simons class*, Geometry & Topology 8 (2004), 413–474, [paper](https://arxiv.org/abs/math/0307092), [author PDF](https://www.math.columbia.edu/department/neumann/preprints/extbloch04.pdf), DOI 10.2140/gt.2004.8.413. Definition 1.1 introduces the pre-Bloch group through the five-term relation. The extended group retains logarithmic data and gives the Cheeger–Chern–Simons class through a Rogers-dilogarithm construction. Ordinary Bloch–Wigner volume and a lifted complex regulator should not be conflated.

For teaching purposes, a torsor is a nonempty space on which a group acts freely and transitively: differences between two points are meaningful, but there is no preferred zero until a point is chosen. In algebraic families the base, group scheme, and topology of local triviality must also be specified. [Stacks Project, §39.11, tag 0497](https://stacks.math.columbia.edu/tag/0497), Definitions 39.11.1 and 39.11.3 and Lemma 39.11.2, gives precise scheme-theoretic definitions and the relation between a section and triviality.

Pere Menal-Ferrer and Joan Porti, *Twisted Cohomology for Hyperbolic Three Manifolds*, Osaka Journal of Mathematics 49 (2012), 741–769, [primary record](https://arxiv.org/abs/1001.2242), is already in the bibliography. Its stated results concern twisted-cohomology vanishing for representations obtained from a lifted complete hyperbolic holonomy, with applications to local rigidity. This audit verified the abstract and bibliographic record, not every theorem hypothesis. It should support the specifically cited rigidity input, not an unspecified global continuation or quantum noncancellation claim.

The guide has several different torsors: positive horosphere scales, algebraic norm-one coordinates, and a proposed period-selection object. They should not be identified merely because the same word applies. A classical regulator or a trivialized algebraic torsor does not determine a finite quantum cycle, its endpoint conditions, or its normalization. The local counterexamples and boundary-factor results are part of the explanation.

**Root-of-unity phase coverage:** Ivan Chi-Ho Ip and Masahito Yamazaki, *Quantum Dilogarithm Identities at Root of Unity*, [paper](https://arxiv.org/abs/1412.5777), IMRN (2016), DOI 10.1093/imrn/rnv141, treats cyclic quantum-dilogarithm identities associated with quiver mutations. The local factorial-source note already points to Definition 3.3 with a normalization qualification. Tsukasa Ishibashi's [*Phases in the cyclic quantum dilogarithm: correction to “Cyclic quantum Teichmüller theory”*](https://arxiv.org/abs/2610.23572), submitted 16 October 2026, is a real primary record: its abstract explicitly adds lifting data and possible root-of-unity phase factors, with a strict-lift locus restoring the stated identities. This audit verified that abstract and date, not the complete correction proof. It is relevant caution about phase data, not a substitute for the project's exact carrier ledger.

## 7. State sums, local asymptotics, and whole-period estimates

A state sum is an exact finite sum over labels satisfying the diagram's incidence constraints. An asymptotic packet is a local expansion near a selected critical point, including a nonzero leading amplitude and uniform error. A period is the original contour or finite Fourier reconstruction. Equality of exponential actions does not identify those three objects.

**Foundational quantum-invariant references already in the bibliography:**

- R. M. Kashaev, *A Link Invariant from Quantum Dilogarithm* (1995), [paper](https://arxiv.org/abs/q-alg/9504020), DOI 10.1142/S0217732395001526: the quantum-dilogarithm link invariant and its R-matrix construction.
- R. M. Kashaev, *The Hyperbolic Volume of Knots from the Quantum Dilogarithm* (1997), [paper](https://arxiv.org/abs/q-alg/9601025), DOI 10.1023/A:1007364912784: evidence from particular knot asymptotics for the volume relation, not a general proof.
- Hitoshi Murakami and Jun Murakami, *The Colored Jones Polynomials and the Simplicial Volume of a Knot* (2001), [paper](https://arxiv.org/abs/math/9905075), DOI 10.1007/BF02392716: the relation between the Kashaev and colored-Jones viewpoints and the volume-conjecture formulation, not the unrestricted conjecture's proof.

**A precise all-orders comparison reference:** Stavros Garoufalidis and Don Zagier, *Asymptotics of Nahm sums at roots of unity*, [paper](https://arxiv.org/abs/1812.07690), [full text](https://arxiv.org/pdf/1812.07690), Ramanujan Journal 55 (2021), 219–238, DOI 10.1007/s11139-020-00266-x. Lemma 2.1 gives a q-Pochhammer expansion; Theorem 3.1 gives radial all-orders asymptotics for the stated positive-definite Nahm-sum data; §4.3 handles congruence classes and summation. This is a useful methodological comparison. Its fixed-root radial limit is not automatically the growing-root-order finite knot sum. The paper explicitly describes the matching knot formal series as conjectural in that comparison.

Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, [publisher edition](https://link.springer.com/book/10.1007/978-3-642-61497-2), Classics in Mathematics (2003), is appropriate background for Fourier analysis and local stationary-phase methods. The publisher metadata were verified; no page-specific theorem was checked here. Do not attach a theorem number from this book to the different 1963 book *Linear Partial Differential Operators*.

The project's source proofs must still verify: the actual lattice and measure; analytic interpolation rather than an arbitrary interpolant; nondegenerate complex saddles; contour endpoints; every Fourier charge; both level parities and normal terms; and a nonzero contribution after summing. The newly completed general-Morse geometric contribution concerns the original CROSS sector. Its unproved full LEFT/RIGHT remainder estimate must remain visible. None of the references above supplies that missing comparison by authority.

## 8. Concrete editorial corrections and scope checks

| Location or proposed phrase | Correction or qualification |
|---|---|
| “Gowda, Some log and weak majorization inequalities” | Use Tao–Jeong–Gowda and the full Jordan-algebra title; distinguish Horn's original matrix result. |
| “Karamata's theorem” without context | State convex-majorization or positive-measure Tauberian theorem. Their inputs and conclusions differ. |
| Rivin 1994 as sole support for a general marked critical-point theorem | Add Futer–Guéritaud Theorem 1.2, then cite the independently proved local marked version for this source. |
| “Positive angle structures give the selected geometric maximum” | An interior critical point of the chosen functional is an additional requirement. |
| “Plancherel/weighted Cauchy proves the volume rate” | It proves the stated energy identity/upper bound. Shared constraints and cancellation require the separate local source theorem. |
| “q-holonomicity proves the geometric A-polynomial” | Keep recurrence existence, selected branch, classical factor, and full ideal equality distinct; retain framing and variable substitutions. |
| “A regulator/torsor selects the quantum state” | Specify the action, reference, boundary conditions, and actual cycle map. This implication is not automatic. |
| “Nahm-sum asymptotics prove the knot state-sum asymptotics” | Different objects and limiting regimes; an exact source adapter is required. |
| Ishibashi correction listed as hypothetical or unverified metadata | The primary 16 October 2026 record is verified; only its abstract, not its full proof, was checked here. |
| General-Morse CROSS theorem described as the full invariant | Retain the explicit remainder problem. The exact one-exception counterexample excludes a proposed automatic support argument but is not a knot-volume counterexample. |

The currently inspected guide already makes many of these distinctions correctly. Apart from the incomplete Tao–Jeong–Gowda attribution, the table primarily identifies phrases to avoid when expanding the lecture-note explanations; it is not a claim that every misleading phrase is currently present.

## 9. A compact teaching order and citation policy

1. Define the exact state sum and its shared labels.
2. Explain the positive geometric optimization and its angle constraints.
3. Explain Fourier energy and weighted inequalities, including what is lost by taking absolute values.
4. Explain local saddle expansions and the separate whole-period problem.
5. Introduce recurrence operators, initial data, and the selected classical component.
6. Introduce peripheral logarithms, regulator branches, and the several torsors only after their concrete objects have appeared.

For each method, a small panel can state “standard tool,” “what is proved here,” and “what this does not settle.” The guide can keep all the attempted routes with this scope. The manuscript should state only completed proofs and clearly identified external background. References should be placed beside the claim they support, with authors, full title, and a primary or author-hosted link; a bibliography alone does not explain which statement is being attributed.

No novelty priority claim has been assessed. No external proof technique was substituted for a local argument during this coverage audit.
