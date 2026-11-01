# Volume limits from planar tangles

[Read the manuscript (PDF)](build/main.pdf).

The manuscript contains completed proofs, including partial results with narrower conclusions. [The introduction](sections/01-introduction.tex) lists the statements and their hypotheses. The illustrated guide's [methods chapter](../book/chapters/methods.md) retains exploratory constructions and unsuccessful comparisons, with their definitions, references and limitations.

The proofs retain their named dependencies on earlier finite-source and geometric lemmas. Those citations are part of the argument; the PDF does not reproduce every calculation in the technical library. [The proof-input map](../repro/PROOF_INPUTS.md) separates these written inputs from executable checks.

The [manuscript audit](../repro/MANUSCRIPT_AUDIT.md) records the current
checks of those implications and the corrections they required. The
reproduction chapter now states the final rate-transfer argument with
all its hypotheses. A [small Lean project](../formal/README.md) checks
finite algebraic steps; it does not formally verify the volume theorems.
Appendix N now proves the uniqueness of polynomial reduction and its
independence of root order, including repeated roots. These statements
also have Lean proofs. The separate geometric and analytic reviews
record their hypotheses and the earlier results they use.
The resolvent identity now proves how this coefficient functional
recovers evaluation at one annihilating operator, including its
nilpotent part. Appendix O also gives the exact root-grid coefficient
selection and the complete circle-pattern Hessian calculation. The
formal proofs cover the finite resolvent and exponent arguments.
Appendix N now supplies a direct finite Fourier proof of the original
Casimir's annihilating relation and the homogeneous face adapter,
including its factor \(1/N\) and the even-level displacement phase.
That calculation, the crossing comparison, analytic estimates and
metric construction remain written proofs.
The product extension proves that factors may be reduced before each
multiplication while retaining repeated-root derivatives. Appendix M
also explains the formally checked coefficient recovery under
\(u=hs\), and why it needs all expansion orders. The dependency check
for Appendices N–R keeps the full remainder premise distinct from the
geometric contribution; it does not certify the proofs at its vertices.

The paper proves volume limits for finite decorations of planar tangle diagrams and for specified ordered-tree constructions. The planar theorem starts from a simple triangulated sphere with a chosen matching, constructs its complete circle packing, and adds terminal tangles until a strict shared-radius inequality holds. Independently sufficiently long signed twists at every original and added crossing circle then give the volume equality for the resulting knot. The tree theorems have separate explicit degree and twist bounds. Chapter 1 distinguishes these families and their quantifiers.

The recursive tangle theorem permits independently chosen positive or negative twist numbers beyond a construction-dependent threshold. For a finite ordered tree with at least one edge and a crossing circle at every vertex, the paper also proves explicit sufficient conditions. Write $d_v$ for a vertex degree and $n_v$ for its signed half-twist power. One such condition is

$$
 \sum_v\frac{d_v}{d_v^2+n_v^2}\le2^{-25}.
$$

A different argument proves the volume identity whenever each vertex satisfies

$$
                d_v\ge2^{28}\qquad\text{or}\qquad |n_v|\ge2^{27}.
$$

Thus $2^{27}$ half twists suffice independently of the number of tangles. The degree alternative permits any fixed short or zero powers at sufficiently large-degree vertices. The full directed criterion is more flexible than this simple consequence: it assigns a separate decay constant to each subtree and distinguishes the vertex evaluated last. The summed test remains useful, for example when $|n_v|\ge8192\sqrt E$ on a tree with $E$ edges.

In every theorem the actual strand connections must give one knot, with no internally closed extra component. The diagram and all integer powers are fixed while the root-of-unity level tends to infinity. The limit is the volume of the original knot complement. Only auxiliary crossing circles are filled; the main knot cusp remains complete.

## Reading the proof

Chapters 2–8 develop the first construction. They define the finite invariant, build the augmented hyperbolic metric, control the signed color terms and analyze the oscillatory filling sum. Appendices A–D supply its detailed algebra, estimates, geometry and rational certificates.

Chapters 9–11 treat the quantitative tree conditions. The geometric construction attaches two octahedra per tree edge in the original order and follows their positive deformation to smooth filling. The quantum argument evaluates a subtree as an exact polynomial, retains its value at zero and estimates the polynomial left on the attaching edge. Chapter 11 proves the stronger directed condition and the bound $2^{27}$. Appendices E–G and K contain the full finite-sum, geometric and recursive proofs. The separate metric condition $\sqrt{d_v^2+n_v^2}\ge630$ constructs a hyperbolic metric but does not alone prove a quantum limit.

The [geometric-longitude chapter](sections/08c-geometric-characteristic.tex) first treats circle trees, then inserts and fills a zero-power crossing circle at an unmarked product junction. Keeping the based boundary maps proves that this operation recovers the original representation. Appendices H–J give the full source expansion, algebraic rigidity and junction arguments. If a fixed nonzero operator annihilates the actual reduced sequence at every sufficiently large level, the selected geometric factor divides its first nonzero classical symbol. This implication assumes the annihilator; it proves neither its existence nor equality with the entire A-polynomial or recurrence ideal. [The all-orders chapter](sections/08f-directed-all-orders.tex) and Appendix M prove the expansion on shifted meridian charts for every directed certificate, so those cases also have the selected-factor conclusion.

The [planar-decoration chapter](sections/08e-balanced-terminal-fans.tex) and Appendix L include the packing construction, the oriented finite source, the full Fourier estimate and smooth primitive filling. The [reproduction chapter](sections/09-reproduction.tex) explains the role of each finite check. The technical notes provide separately readable versions of the proofs. The older local numerical condition remains in Chapter 10 as an intermediate theorem, with its improvement stated explicitly.

The [net-twist companion theorem](../notes/actual_conway_net_twist_volume.md) treats a broader class of ordered tangle expressions using exact tangle reductions and the strict-tree estimates. Its hypothesis concerns the combined twist numbers left after reduction. The subsequent [closure theorem](../notes/actual_conway_arbitrary_closure_volume.md) also handles cap closures and exact zero sums under its long-surviving-weight condition. These companion results are described in the [results chapter](../book/chapters/results.md); they are distinct from the construction classes developed in this PDF.

[Appendix N](sections/N-uniform-filling-bound.tex) proves a level-independent finite bound for inserting fixed twist powers. Its transfer to a further volume theorem explicitly assumes an exponential estimate for the shared source. [Appendix O](sections/O-morse-geometric-contribution.tex) proves that the specified geometric contribution for an unchanged matched spherical diagram is nonzero and has the volume rate of its actual long-filled complement. This is a contribution to the original exact invariant, not a new topological invariant. A general bound on its complementary signed contribution is not asserted. These appendices do not enlarge the full-invariant claims.

[Appendix P](sections/P-weak-balance.tex) supplies a full-invariant
theorem for an unchanged matched sphere whose complete packing satisfies
weak balance. Equality in the local condition is allowed. The proof
derives the entropy and Hessian estimates, chooses one shared coefficient
weight, and uses Appendices N and O to bound the full remainder and
identify the surviving action. A quantified variant permits small
balance defects. No assertion that every diagram satisfies either test
is part of this theorem.

## Build the paper

From the repository root, run:

```sh
python3 tools/build_manuscript.py
```

The result is `manuscript/build/main.pdf`. The build also produces standalone previews of the native TikZ figures and a manifest of the TeX, bibliography and PDF hashes. It requires TeX Live or MacTeX with `latexmk` and the packages listed in `main.tex`. Building the paper does not execute the mathematical certificates.

## Check the finite certificates

Run:

```sh
python3 repro/verify.py --output repro/results
```

The verifier checks the rational supporting inequalities and their exact domain coverage. It does not use numerical optimization or numerical sampling as a proof. See [the reproduction instructions](../repro/README.md) and [the proof-input map](../repro/PROOF_INPUTS.md) for the inputs and the separate role of optional finite checks. The continuum estimates and geometric arguments are proved in the manuscript.

For the quantitative circle-tree result, run:

```sh
python3 repro/run_research_checks.py curvature-fillings
```

This group checks symbolic edge identities, finite complex-parameter bounds, and the labeled octahedron attachments and peripheral words. Its finite computations supplement the uniform estimates and topological proofs; they do not replace them.

For the local condition and its geometric criterion, run:

```sh
python3 repro/run_research_checks.py local-tree-fillings
```

This group checks 29 rational constant margins and 48 finite recursion cases. The finite cases compare the exact subtree evaluation with the corresponding finite contraction. They supplement the analytic induction and geometric completion proved in Chapter 10 and Appendix G.

For the stronger directed condition, run:

~~~sh
python3 repro/run_research_checks.py directed-tree-fillings
~~~

This checks exact rational constant inequalities. The uniform estimates and induction are proved in Appendix K.

For the unmarked-junction formulas, run:

~~~sh
python3 repro/run_research_checks.py strict-tree-geometry
~~~

This requires SymPy and checks the local algebra. The based paths and full representation gluing are proved in Appendix J.

## Build the illustrated guide

The guide build is separate from the paper build:

```sh
python3 tools/build_book.py
python3 tools/check_book.py
```

The guide is written to `docs/`, with the paper copied to `docs/papers/conway-composition.pdf`. Building it does not execute research scripts. Pandoc converts its mathematical displays to native MathML; the checker verifies the rendered formulas and local links.

The illustrated guide is the maintained web text. The former Sphinx routes redirect to it; there is no separate Sphinx proof source to build.


Appendix Q gives a further constructive closure theorem. Two marked
spheres with certificates covering every locally allowed noncentral
sector can be joined along triangles incident to their protected edges.
The new source retains a strict gap. Repeating this operation gives an
explicit sequence with \(17+r\) crossing regions outside weak balance at
the retained mark. The argument, its inherited analytic and geometric
inputs, and the finite reproduction command are recorded in the
[protected-sum audit](../repro/manuscript_audit/protected-sum.md).

Appendix R treats insertion along an ordinary triangular face. It proves
the conditional disk minimum for every positive boundary triple,
extends the finite source certificates to sufficiently small positive
boundary ratios, and keeps the original coefficient targets when the
pieces are joined. Explicit even chains provide suitable boundaries
for any fixed finite list of certified pieces. The nine corresponding
Lean declarations check the scalar comparison and the distinction
between a wholly central block and a block with a noncentral term.
The packing construction and the analytic and geometric inputs remain
written proofs; their role is recorded in the
[ordinary-boundary audit](../repro/manuscript_audit/triangular-boundary.md).
