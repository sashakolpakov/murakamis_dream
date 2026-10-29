# Coverage audit for the hyperbolic-knot target

**29 October: fixed long fillings.** A further primary-source coverage
check distinguished our fixed-twist, N-to-infinity statement from
[Lee, 2307.09903](https://arxiv.org/abs/2307.09903): its abstract first
passes to a skein/categorical limit as twist counts tend to infinity
and then relates the limiting evaluation to octahedral volumes.
The abstract of [Galakhov et al.](https://doi.org/10.1016/j.physletb.2015.02.029)
concerns a conjectured explicit formula for colored polynomials of
arbitrary pretzels. [1101.2844](https://arxiv.org/abs/1101.2844)
concerns noncommutative A-polynomial computations for the restricted
(-2,3,n) family and numerical volume-conjecture work. These scope
checks supply no proof premise to the present full-source estimates
or marked representation-volume comparison. They also do not justify
a claim of novelty or an exhaustive absence of overlapping results.

**29 October: augmented-base coverage check.** The new
[complete augmented pretzel period proof](actual_pretzel_coherent_circle_and_period_asymptotic.md)
is an independent original-source calculation, not a novelty claim.
The abstract of van der Veen's
[augmented knotted trivalent graph paper](https://arxiv.org/abs/0805.0094)
states volume-conjecture coverage for augmented KTGs and an arithmetic
containing-link corollary. The abstract and introductory scope of
[Ibarra--McQuire--Purcell](https://arxiv.org/abs/2506.09296)
concern OCTAHEDRAL fully augmented links and a Turaev--Viro result
without half twists; the published introduction also records earlier
Kashaev coverage for octahedral fully augmented links. These are
coverage statements, not proof inputs to the new finite-source,
recurrence or Gaussian arguments. They do not by themselves classify
the exact overlap with every non-octahedral s-antiprism base here.
No claim that this base family was previously uncovered is made.
Its complete augmented links must also be distinguished from the
fixed-slope filled knots, which the new base theorem does not settle.

Research record, 25 October 2026. Hyperbolicity is a standing assumption.
The user permits an unbounded, sufficiently broad knot class, and requests
literature checks for coverage rather than proof techniques. Accordingly,
the external statements below are not hypotheses accepted on the authority
of their proofs. No proof section of these papers is needed for this audit.

## 1. Keep the quantum object fixed

The target is Kashaev's original invariant and volume conjecture,
approached through a literature-defined quantum A-module and its
distinguished period. The later Andersen--Kashaev meridian state and
Andersen--Malusa b-shift annihilator are comparison objects. An
annihilating equation alone does not select a solution or its
normalization. An AK volume theorem does not settle the original
conjecture without the corresponding comparison.

The independent local and analytic arguments in the existing notes may
duplicate stated literature coverage. That is independent verification,
not evidence of a new theorem about previously uncovered knots.

## 2. Checked coverage statements

| Source and statement checked | Stated scope | Consequence for this project |
| --- | --- | --- |
| Ben Aribi--Wong, [2410.10776v2](https://arxiv.org/abs/2410.10776v2), abstract and introductory theorems | Jones-function existence for FAMED one-cusped hyperbolic manifolds with H2=0; geometricity adds the AK volume asymptotic. The paper includes all hyperbolic twist knots. | Our twist-family theorem and positive FAMED saddle theorem overlap this coverage. They remain useful as independently audited arguments. |
| Ben Aribi--Guilloux--Wong, [2512.17437v1](https://arxiv.org/abs/2512.17437v1), abstract | FAMED geometric realizations for more than 42,000 knot complements, including the stated crossing and tetrahedron census ranges. | Additional isolated small-knot certificates do not establish an unbounded new class. The census claim is not a uniform membership theorem. |
| Wong, [2512.23198v1](https://arxiv.org/abs/2512.23198v1), Definitions 1.1 and 1.5, Theorems 1.11 and 1.14, Corollary 1.16 | A full-tensor theorem for generalized FAMED semi-geometric triangulations; the Jones-function theorem imposes additional longitude/meridian conditions. Definition 1.5(2) excludes a longitude-dependent affine shape plane. Definition 1.5(3) prescribes a meridian without a longitude shear. | The generalized singular reduction already has substantial stated overlap. Our moving-plane Fourier construction removes a condition appearing in this particular statement, but this alone is not new knot-family coverage. |
| Wong, [2609.33922v2](https://arxiv.org/html/2609.33922v2#S1.SS2), Theorems 1.1 and 1.4, Remark 1.2 | A KLV volume/torsion theorem for geometric triangulations; an RT-type function for angle-supporting triangulations with a suitable quad type; a weighted squared-norm factorization. Agreement of the RT-type function with the AK Jones function is asserted on FAMED data. The remark defines an AK analogue more generally. | This is close to our Fourier constructions. Its stated general KLV theorem does not by itself identify the original AK meridian state or its quantum A-operator. The introduction also explicitly leaves full invariance unresolved. |
| Liu--Ming--Sun--Wu--Yang, [2608.16560v1](https://arxiv.org/abs/2608.16560), abstract | Cusped modular-double Turaev--Viro-type invariants with an exponential volume law. | A broad volume theorem for this literature object is already claimed. Equivalence with our selected AK state would still require a precise map and normalization. |
| Ge, [2609.27635v1](https://arxiv.org/abs/2609.27635v1), Theorem 1.1 and Sections 2--4 | Every finite-volume cusped hyperbolic 3-manifold admits a finite geometric ideal triangulation realizing completeness. | At the user's subsequent request, the affine-subdivision argument was independently audited, with exact stress tests. See the separate audit. A global branching and the quantum cycle comparison are additional requirements. |

The last three entries are recent coverage changes. They must be retained
when assessing the scope of any proposed theorem here. The user separately
authorized a proof audit of Ge's geometric result; that authorization
does not extend to importing the quantum papers' proof techniques.

For the principal algebraic direction, Guilloux--Marche,
[1804.01395](https://arxiv.org/abs/1804.01395), already studies exact
polynomials, a class containing knot A-polynomials, and their volume
functions. Its definitions and stated coverage identify classical
regulator exactness as existing theory. A quantum theorem still has to
identify the distinguished period and its normalization. The
[intrinsic norm-torsor note](intrinsic_quantum_a_norm_torsor.md)
reconstructs the required elementary descent arguments independently.

### All-level state and torsor coverage

The following are definitions and stated scope, not imported proofs:

* Murakami--Murakami, [math/9905075](https://arxiv.org/abs/math/9905075),
  states the Kashaev/colored-Jones comparison for all levels. Our
  crossing note reconstructs the needed matrix and period identities
  directly. This is independent verification of known coverage.
* Baseilhac--Benedetti, [1101.1851](https://arxiv.org/abs/1101.1851),
  states an odd-level quantum-hyperbolic/Kashaev comparison. Its link
  specialization uses the trivial ambient character. It must not be
  silently replaced by a fixed hyperbolic character of the complement.
* Willetts, [2003.09854](https://arxiv.org/abs/2003.09854), states an
  all-knot completion unifying ADO and colored Jones, with the Alexander
  factor retained. That unification and its recursion-ideal theorem
  have not been adopted here. Our modified-dimension gauge is proved
  from the defining finite matrices instead.
  The later [Frobenius Verma calculation](frobenius_verma_period.md)
  independently proves the stated root normalization ADO/Delta by
  untruncated crossing coefficients and the polynomial-block trace.
  It also proves equality of the actual root annihilator ideals
  under this central factor. It does not identify the generic
  completion or adopt a colored-Jones recursion comparison.
* Garoufalidis--Scholze--Wheeler--Zagier,
  [2412.04241v2](https://arxiv.org/abs/2412.04241v2), introduces proposed
  K3-graded Habiro modules. The user subsequently requested a separate
  [independent audit](gswz_printed_definition_audit.md). It confirms
  counterexamples to the printed unrestricted Theorems 1 and 2:
  the local span need not be finitely generated, and the global set
  need not be additive. It also verifies formula errors in (114)
  and (165). Theorem 5 restricts to specified good root orders; the
  supplied examples do not directly refute its restricted membership
  conclusion, which remains independently unverified here. No theorem
  from this paper is a premise of the A-curve torsor construction or
  its requested volume comparison.

The direct [ADO pointing proof](kashaev_ado_pointing.md) also identifies
a structural limitation of a fixed-level approach: rational root states
have a central shift sector v=1. Retaining the original quantum family
and its pointing is necessary before comparing with the geometric
classical A-curve. A finite splitting torsor alone is insufficient.

The subsequent [finite cut-state proof](finite_sum_annihilator.md)
now independently establishes a nonzero actual all-level meridian
annihilator for every knot. It does not adopt the literature
holonomicity or recursion-ideal comparison theorems. The
[triangulation bridge](triangulation_regulator_bridge.md) specifies
the remaining geometric-symbol, relative-source, and regulator-norm
comparison. These existence results do not establish the volume
conjecture for a broad knot class.

## 3. What alternatingness supplies and what it does not

Menasco's diagrammatic checkerboard decomposition is useful combinatorial
data. It must not be identified automatically with a decomposition into
right-angled cells in the complete hyperbolic metric.

Gan, [2005.07904v3](https://arxiv.org/abs/2005.07904), classifies alternating
links with both checkerboard surfaces totally geodesic as three links,
with octahedral, cuboctahedral and icosidodecahedral projection graphs,
and characterizes them as right-angled completely realisable. Thus the
strong geometric interpretation is highly restrictive. This coverage
statement does not invalidate the combinatorial Menasco decomposition.

An augmented link and a knot obtained by filling its crossing circles
are also different manifolds. A right-angled augmented-link realization,
or a TV volume theorem for it, cannot be transferred to the filled knot
without a separate quantum filling argument.

## 4. What would count as closing a broad class here

The present independent theorem covers every globally branched complete
strictly positive geometric knot triangulation, for its specifically
normalized tensor-derived meridian state. The remaining requirements
are not additional finite rank scans:

1. Uniform membership of a stated unbounded knot class in the hypotheses,
   established independently if a literature existence proof is not used.
2. Identification of the selected literature state across the required
   realizations, with its peripheral functions, phase and cycle retained.
3. Application of the independently proved volume and annihilator
   results to this same state.

Hyperbolic two-bridge knots beyond twist knots and suitable highly twisted
alternating families are possible class targets. The sources checked here
do not state an unconditional all-two-bridge or all-alternating AK theorem.
This search result is not a claim that no such theorem exists elsewhere.
Selecting a new matrix condition on knots already in a stated census does
not satisfy the uniform-class requirement.

## 5. Subsequent steering

The user explicitly rejected further reduction of the main objective to
FAMED or other chart-by-chart AK hypotheses. The principal direction is
the intrinsic period torsor and general algebraic properties of the
A-polynomial. The geometric existence input is audited separately in
[ge_geometric_triangulation_audit.md](ge_geometric_triangulation_audit.md).
