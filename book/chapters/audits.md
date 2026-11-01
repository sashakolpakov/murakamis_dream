# Checking the formulas and reproducing the calculations

## Following the proof's dependencies

The manuscript's final step is an explicit implication. Write the exact
invariant as \(K_N=u_N(G_N+E_N)\), where \(u_N\) is the recorded
normalization, \(G_N=a_Ne^{N\mathcal A}\) is the selected contribution,
and \(E_N\) is everything else. To obtain the action as the growth rate,
one needs

\[
 \frac{\log|u_N|}{N}\longrightarrow0,\qquad
 \frac{\log|a_N|}{N}\longrightarrow0,\qquad
 \limsup_{N\to\infty}\frac{\log|E_N|}{N}
       <\operatorname{Re}\mathcal A.
\]

The reverse triangle inequality then prevents cancellation of the leading
contribution. A separate geometric argument identifies
\(2\pi\operatorname{Re}\mathcal A\) with the volume of the intended knot
complement. The reproduction chapter gives the complete elementary
argument and records which earlier results supply each hypothesis.
A critical point, a norm bound, or a representation with the right
peripheral equations supplies only part of this chain.

The [manuscript audit](../../repro/MANUSCRIPT_AUDIT.md) records the
current review. It led to an explicit comparison between the regulator's
fundamental chain and the filled metric in Appendix D, and a more precise
complex-contour estimate in Appendix B. It also made the multidegree
hypothesis explicit in the standalone tensor norm statement. The review
does not certify every theorem in the manuscript; its scope and remaining
dependencies are stated in that record.

The later review follows the directed-tree induction and the all-orders
recurrence argument separately. In the former, the child values used to
normalize a subtree are exact complex numbers, and the bounds retain the
whole remainder at both level parities. In the latter, the conclusion
requires every finite expansion order on all parameter translates used
by the operator. The coefficient substitution then gives a geometric
factor of its classical symbol. It does not identify the full
A-polynomial. Appendix F now also spells out why its regulator and its
completed metric compute the volume of the same oriented cell chain.
The geometric-germ argument in Appendix I now works directly on the
retained positive augmented triangulation at the filling endpoint.
Its primitive slope equations define the projective filled-group germ,
with the main meridian as local coordinate. This avoids a separate
existence theorem for a positive triangulation of the filled manifold
in this part of the proof.

A further reading follows the restricted source estimates separately
from the general central-contribution theorem. It found no circular
use of the unresolved general remainder bound in the inspected
restricted-family proofs. The [source coverage record](../../repro/manuscript_audit/source-coverage-followup.md)
lists those dependencies and their parity restrictions. The
[geometry record](../../repro/manuscript_audit/retained-geometry-followup.md)
states the assumptions used to identify the filled metric and its
deformation germ. These are bounded reading records, not a complete
verification of every imported lemma.

The later [finite source and filling reading](../../repro/manuscript_audit/finite-source-and-filling-followup.md)
separates the local functional, the whole central period and the
completed metric. The [marked-source reading](../../repro/manuscript_audit/marked-source-adapter-followup.md)
checks the original face lattice, the cup and cap scalars, and the
passage from the grid average to one coefficient. Neither record
substitutes a source identity for the required remainder estimate.

The stopping point is the manuscript's stated restricted theorems,
including ordinary triangular insertion. Each full-invariant conclusion
must have its own exact source, nonzero leading term, whole remainder
bound, primitive metric completion and absolute volume identity, with
matching hypotheses and level scope. The open general matched-sphere
remainder cannot serve as a premise for one of those conclusions.
A missing step must be repaired or the affected claim narrowed.
Once these requirements, the reproducible certificates and the
exposition checks are complete, a new family or a smaller constant is
further research rather than a condition for finishing this release.

Two wording changes make the all-orders argument more precise. Its
annihilator has fixed order \(r_P\), independent of the quantum level;
the separate spectral degree is \(N-1\). Its norm comparison applies
to the reduced polynomial of degree less than \(N\). A higher-degree
product is reduced before that comparison is used.

## Checking finite implications in Lean

The current audit also records a machine-readable dependency map for
Appendices N–R. Run:

~~~sh
python3 repro/check_manuscript_logic.py --output repro/results/manuscript-logic
~~~

The map keeps six premises attached to each full volume conclusion:
the exact invariant, a nonzero leading contribution, a bound for the
whole remainder, the specified completed metric, the absolute volume
identity, and the final rate comparison. It records the packing or
certificate assumption for each restricted family. The unrestricted
matched-sphere route still has an open remainder premise.

The checker detects missing premises, circular dependencies and changes
of level scope. Ten deliberately invalid versions are also tested,
including a substitution of an odd-level bound into an all-level
argument. This checks the consistency of the written dependency map;
it does not verify the mathematical claims assigned to its vertices.
The saved report identifies the current source files by their hashes.

Two corrections from the latest reading concern the mathematical text.
In Appendix Q, face labels \(11,14\) are now distinguished from their
weights \(e^{q_{11}},e^{q_{14}}\) in the triangle potential. In Appendix O,
the even-action coefficient converges to a holomorphic function
\(B_{e,0}(\delta^2)\), with \(B_{e,0}(0)=C_e>0\). It need not converge
to the constant \(C_e\) away from zero. Continuity on a smaller fixed
chart gives the positive real part used in the charge estimate.

With the pinned Lean toolchain installed, run:

~~~sh
python3 repro/check_proof_logic.py --output repro/results/proof-logic
~~~

The [formal project](../../formal/README.md) proves finite lemmas about
the exact parity cutoffs, polynomial and Hermite identities,
tensor subtraction, and scalar rate comparisons. It also constructs
division by a split monic polynomial on coefficient lists and proves
that the remainder's top coefficient is the iterated divided difference.
Repeated roots are retained without division by their differences.
The constructed operations are proved linear and independent of
trailing zero coefficients. Adding a multiple of the monic modulus
leaves the remainder and its top-coefficient functional unchanged.
The remainder is also proved unique under its coefficientwise degree
bound, and independent of the order of the roots. These statements
allow repeated roots and padded coefficient lists. Appendix N now
explains this construction before specializing to the spectral
polynomial. A further formal theorem characterizes the functional by
additivity, vanishing on multiples of the modulus, and its values in
low degree. Those are explicit hypotheses on a candidate functional.
The resolvent identity below supplies a direct algebraic application
once the actual Casimir annihilating relation is known.
The runner compiles
the proofs and separately checks their logical assumptions. It rejects
admitted proof steps. These declarations retain their mathematical
hypotheses: they do not formally prove the analytic source estimates,
the diagram-to-invariant identity, or hyperbolic completion.

For example, the tensor identity subtracts the term that uses evaluation
at every coordinate. It retains all terms with one or more derivatives,
as required at repeated spectral roots. Proving that the actual source
has the claimed degree and vanishes on the specified product grid is a
separate part of Appendix N. This distinction is recorded in the formal
project's explanation of every declaration.

The new product module proves

\[
 \operatorname{rem}_p(fg)=
 \operatorname{rem}_p\bigl(\operatorname{rem}_p(f)
                              \operatorname{rem}_p(g)\bigr).
\]

It constructs multiplication from coefficient lists and proves the
identity, rather than assuming that multiplication respects reduction.
Thus a long product may be reduced after each step. At a repeated root
\(r\), it retains the derivative
\(f'(r)g(r)+f(r)g'(r)\), including when the modulus has further roots.
The scalar coefficient functional is not asserted to be multiplicative.

A further module proves how this functional recovers an operator
without diagonalizing it. Let \(p\) be a split monic polynomial of degree
\(m\ge1\), and let \(w\) belong to a commutative ring with \(p(w)=0\).
Synthetic division constructs the polynomial

\[
 \begin{aligned}
 V_w(X)&=\frac{p(X)-p(w)}{X-w},\\
 \ell_p(fV_w)&=f(w).
 \end{aligned}
\]

Here the fraction denotes a polynomial identity, not an inverse;
\(\ell_p\) takes the coefficient of \(X^{m-1}\) in the remainder
modulo \(p\). The multiplier \(f\) has arbitrary degree. The proof
uses \((X-w)V_w=p\), the value \(\ell_p(V_w)=1\), and linearity.
It therefore retains repeated roots and nilpotent parts of \(w\).
For one Casimir matrix \(\Omega\), the commutative ring is the algebra
generated by \(\Omega\) and scalar matrices. Appendix N now derives
\(\chi_N(\Omega)=0\) from the original pair matrices by a finite
Fourier transform. On each residue class of the total color, the
transform gives the same triangular polynomial operator. Its
characteristic polynomial is the required Chebyshev polynomial,
with its repeated roots. The calculation also derives the local
face polynomial and its factor \(1/N\). At even levels the integer
displacement in its phase cannot be replaced by an arbitrary
residue. The proof keeps the physical endpoints before applying
the transform. This calculation and the separate crossing-power
comparison are written proofs, rather than new Lean declarations.
Matrices at different boxes need not commute.

The finite adapter check can be run with:

~~~sh
python3 repro/check_local_face_fourier.py
~~~

It constructs the pair matrix from the coproduct and the polynomial
operator separately. Its finite-field examples test both parities,
including an incorrect phase convention that must fail at even
levels. These checks help detect transcription errors; the displayed
matrix identity in Appendix N proves the assertion for every level.

The other new module checks the face-grid support argument in Appendix O.
Put \(d=N-1\). There are \(R\) ordinary face variables and two protected
ones. If a monomial survives the ordinary \(N\)-point grids, each of its
ordinary nonnegative exponents is congruent to \(d\) modulo \(N\),
hence at least \(d\). The original numerator has total degree \(Rd\).
Those minima exhaust its degree: every ordinary exponent is exactly
\(d\), and both protected exponents are zero. This also forces the
exterior protected exponent to vanish even though that variable is fixed,
not averaged. The surviving character is one for the translated
even-level grids as well. Lean proves the exponent statements;
finite character orthogonality, the primitive physical grid, and the
original cup, cap and mark normalization remain written proofs.

Another module checks the formal substitution used in the recurrence
argument. If \(B(h,u)=\sum B_{a,b}h^au^b\), then

\[
 B_{a,b}=[h^{a+b}s^b]B(h,hs).
\]

Every coefficient is recoverable, so equality after substitution implies
equality before substitution. Agreement through order \(h^L\), however,
only recovers coefficients with \(a+b\le L\). The module also constructs
a nonzero series invisible through any prescribed finite order. This
explains why the manuscript requires an expansion to every order for
the recurrence conclusion. Lean verifies this coefficient calculation;
the analytic existence of that expansion and the longitude identification
remain written proofs.

Together, the project now has 193 compiled declarations with inspected
axiom dependencies: the latest additions are six face-support lemmas
and seven resolvent lemmas. The count describes the formal statements,
not how much of the volume proof has been verified. In particular,
Appendix O's positive radius Hessian, complex cofactor estimates,
charge comparison, paired endpoint currents and filled metric are
written arguments. The current analytic reading retains both level
parities and independently sufficiently long fixed signed powers.
Its nonzero central contribution still needs the separate full
remainder estimate supplied by the applicable restricted-family theorem.

## Joining certified diagrams

The protected triangular-sum argument has a separate
[dependency audit](../../repro/manuscript_audit/protected-sum.md).
Two removed triangles each contribute one half of the joining weight's
logarithm. At the same time, their two copies of the ordinary coefficient
target become one. Keeping both changes gives the exact cancellation
needed to compare the full shared coefficient bounds.

The new Lean module constructs the three local rate functions and the
map from a new sector to its two input sectors. It proves the comparison
for both branches of each maximum, the target cancellation, and the
positive-gap implication. The written proof must still establish that
the actual diagrams supply these functions and that their certificate
vectors can be normalized to agree. In particular the input cover must
include every locally allowed noncentral string; a string is not omitted
just because its old global coefficient vanishes.

A single reproduction command checks the two interval certificates for
the seventeen-region input and constructs eight finite tetrahedral
attachments:

~~~sh
python3 repro/check_protected_sums.py --output repro/results/protected-sums
~~~

This command requires `python-flint`. It verifies the input's full branch
cover and rational loads, then checks the new spheres' incidence, cyclic
vertex links, matchings and original target counts. It also checks that
the four regions containing a possible balance failure are untouched.
The argument for arbitrarily many attachments is the induction in
Appendix Q. The finite examples do not replace that proof.

## Checking insertion at an ordinary triangular face

The [ordinary-boundary audit](../../repro/manuscript_audit/triangular-boundary.md)
follows the new disk minimum and its coefficient targets separately.
The comparison subtracts \(\Delta=2Q(u,v,b)-\log b\), where
\(u,v,b\) are the attaching curvatures. A wholly central inserted
piece contributes exactly that correction. A noncentral piece uses
an absolute strict bound, which absorbs the possible bridge error.
The case distinction concerns every label in the inserted piece.

The nine new Lean declarations verify this scalar argument with its
explicit hypotheses. They do not prove the conditional packing,
extension of the witnesses, or hyperbolic completion. The current full
Lean runner compiles 193 declarations and inspects their axiom
dependencies; no admitted proofs are accepted.

Run the explicit finite certificate with:

~~~sh
python3 repro/check_triangular_boundary_certificate.py --output repro/results/triangular-boundary
~~~

The command requires `python-flint` and NumPy. It replays the original
seventeen-region cover and the newly allowed terms at the stated
positive boundary weights. It also checks the finite oriented
constructions and the rational obstruction used to retain a balance
failure. The formulas for every even chain length, the conditional
disk identity and the final volume transfer are proved in Appendix R.
The program does not build or evaluate the invariant of the large
explicit example.

## The uniform cap estimate

Run the exact topology, response, pressure and entropy certificates with:

~~~sh
python3 repro/check_cap_response.py --output repro/results/cap-response
~~~

This standard-library command recomputes each input before using it in a
later check. It verifies the 54-region sphere and its original marked
coefficient problem, localizes the positive exterior stationary point,
and proves the two pressure comparisons by rational intervals. It also
checks the alternating partial-sum inequalities on finite rational examples.
With SymPy installed, adding `--algebra` checks the spectral products and
matrix divided differences in exact cyclotomic fields.

The [written theorem](../../notes/research_cap_uniform_spectral_gap.md)
provides the uniform estimate and its asymptotic consequences. The
certificate controls one cap at odd levels, with all other spectra fixed.
The geometric meaning of the complete action, the all-level limiting
estimates, and the unresolved full remainder are listed separately in
each result record.

## Uniform bounds for inserting twists

With SymPy and NumPy installed, run:

~~~sh
python3 repro/run_research_checks.py filling-supremum
~~~

The program checks the finite derivative interpolation formula in
cyclotomic fields, the repeated and simple Chebyshev residues, and the
reconstruction of positive and negative powers of the original crossing
matrices. It also checks the lower-block numerator derivatives against
the corresponding spectral projectors. The [proof](../../notes/actual_uniform_filling_supremum_bound.md)
establishes the norm bounds for every level. The finite checks do not
estimate a volume limit.

## The planar terminal decoration

Run the finite checks with one command:

~~~sh
python3 repro/run_research_checks.py balanced-terminal-fans
~~~

The script uses integer and rational arithmetic. It verifies the closed
curvature recurrence and the rational lower bound in the analytic balance
proof. It also constructs oriented stellar subdivisions, derives their
new ordered quadrilaterals, checks the matching and even-level parity
extension, and follows the endpoint pairings of even stacks of odd
terminal tangles.

These checks do not estimate a quantum limit or certify a numerical
packing. The [written theorem](../../notes/actual_balanced_terminal_fan_volume.md)
proves the packing, the exact full coefficient, the uniform estimates
and the smooth primitive metric completion. The script checks the finite
identities used by that argument.


The repository contains written proofs, exact finite certificates, numerical checks and recorded outputs. They answer different questions. This chapter explains which calculations support which steps, and how to rerun them without treating a successful sample as a theorem.

An exact symbolic calculation can establish an identity in formal variables. A rigorously bounded interval calculation can establish an inequality over an entire stated parameter domain. A finite counterexample can disprove a proposed identity. By contrast, checking many quantum levels or plotting a growth rate does not prove a uniform limit as \(N\to\infty\). The scope of each script must be read together with the mathematical argument that uses it.

The current [strict Conway tree theorem](../../notes/actual_conway_all_strict_tree_long_twist_volume.md) includes bounds for the full quantum sum, a nonzero selected contribution, the original normalization and the actual marked filling geometry. Its proof is not waiting for a theorem about all knots. The more specialized general-plat calculations catalogued below retain their own hypotheses and limitations.

## The directed degree and twist bound

Run the new exact rational comparisons with one command:

~~~sh
python3 repro/run_research_checks.py directed-tree-fillings
~~~

This uses only Python's standard library. It checks the inequalities in the [directed criterion](../../notes/actual_all_circle_directed_volume.md), including the uniform twist bound and the star whose center has power two. The comparisons use rational upper and lower bounds rather than decimal estimates. The written proof supplies the uniform kernel estimate, induction, noncancellation and identification with the actual hyperbolic volume. The program does not estimate a quantum limit.

## Inserting a circle at an unmarked junction

With SymPy installed, run:

~~~sh
python3 repro/run_research_checks.py strict-tree-geometry
~~~

The program checks local rational identities in the [strict-tree longitude proof](../../notes/actual_strict_tree_geometric_characteristic.md): the normalization of the white face maps, the primitive disk longitude, the two incident radius formulas, and the response at a possible half-angle fold. The based meridian paths, ordered boundary gluing and stationary elimination are proved in the text. They cannot be verified merely by equality of matrix traces.

## Reproducing the local tree argument

This group requires Python and mpmath. Run it using one command:

~~~sh
python3 repro/run_research_checks.py local-tree-fillings
~~~

The first two programs check 21 analytic and eight geometric
constant comparisons by exact rational arithmetic. The third
compares the polynomial subtree recursion with a separate
spectral or first-derivative trace calculation in 48 finite cases,
using 180 choices of root at 80-digit precision. The examples
include both level parities, zero and signed powers, moving
parameters, and constant channels with repeated spectral roots.
All \(N\) edge indices are retained; removing the high indices
changes every tested value.

These checks verify the constants and finite identities used by
the argument. The written proof supplies the induction for all
finite trees, the contour bounds, noncancellation, and the metric
completion. The scripts do not test the asymptotic conclusion
by extrapolating finite levels.

## Checking the geometric longitude formulas

With Python and SymPy installed, run the four exact-algebra programs
through one command:

~~~sh
python3 repro/run_research_checks.py geometric-characteristic
~~~

The programs check the nonparabolic face maps and peripheral words,
the four-puncture character matrices, the two eigenline choices in a
half twist, and the differential and discriminant identities used by
the rigidity argument. They compare rational functions symbolically,
rather than sampling hyperbolic knots. The written proof establishes
the ordered gluing, boundary pairing, constant field and regularity
over every nonzero main meridian value. Those global arguments are
not replaced by the script results.

## Checks for the quantitative volume theorem

The [quantitative theorem](../../notes/actual_all_circle_quantitative_volume.md)
has one reproduction command:

```sh
python3 repro/run_research_checks.py curvature-fillings
```

Python, SymPy and mpmath are required. The group runs three programs.
The first checks four edge-action identities symbolically and 990
complex Gaussian samples at 70-digit precision, at levels 160 through
256. The second verifies 46 rational identities for the actual
octahedra, including the odd half-twist face returns, and seven bounds
used in the positive angular chart. The third compares the literal
tangle strand compiler with an octahedral attachment construction on
128 finite trees. It checks 448 left or right attachments, the
resulting colored face cycles and signed disk pairings, and 28 symbolic
peripheral and regulator identities.

The saved outputs are the [analytic checks](../../experiments/all_circle_curvature_packet_results.json),
[local geometric checks](../../experiments/two_octahedron_angular_edge_block_results.json)
and [ordered attachment checks](../../experiments/ordered_octahedron_pages_results.json).
Each records its finite scope. The arbitrary-tree induction, the
metric completion and the uniform asymptotic estimates are written
proofs; finite samples do not establish those conclusions. The
[geometric chapter](geometry.md#the-geometric-proof-for-the-explicit-degree-and-twist-bound)
explains how the proof identifies the original knot complement.

## Arbitrary multiplication regions

The [general component theorem](../../notes/actual_main_meridian_general_component_comparison.md) permits connected groups of product junctions of any fixed size and valence. Its new finite identities can be checked with one command:

```sh
python3 repro/run_research_checks.py general-components
```

The program constructs each Newton polynomial over an exact cyclotomic number field. It compares its Laurent coefficients with the formula in the [Fourier reflection proof](../../notes/actual_main_meridian_high_fourier_reflection.md), and independently divides products by the deformed polynomial relation. Subtracting the complete trace must cancel the first Fourier term. A further calculation verifies fusion in the full quotient algebra, including inputs whose values at repeated roots vanish but whose derivative contributions remain nonzero.

The [recorded results](../../experiments/high_fourier_reflection_results.json) cover levels two through twelve, including both parities: 36 high-index polynomials, 721 trace differences and 33 fusion identities. These are exact finite algebra checks. The uniform Fourier loss, comparison of positive maxima and passage to the filled knot complement are proved in the three companion notes; the finite checks do not establish those analytical or geometric conclusions.

## Trivalent multiplication regions

The [component theorem](../../notes/actual_main_meridian_trivalent_component_bound.md) has one reproduction command:

```sh
python3 repro/run_research_checks.py trivalent-components
```

The script constructs the Newton polynomials and performs division by the deformed polynomial relation in exact cyclotomic fields. It checks every cubic index triple through level ten, using symmetry to avoid repeated calculations. This includes internal indices above one half, zero and half endpoints, both parities, and the actual turn types. It also checks the elementary identities used in the simultaneous boundary comparison.

The script uses Python and SymPy and has no numerical approximations. It checks the finite algebra; the proof supplies the concavity argument, the uniform gap, and the complex estimates needed for the [filled-knot theorem](../../notes/actual_main_meridian_trivalent_filled_volume.md).

## The preferred cusp correction

The exact crossing and framing calculation and the geometric longitude calculation can be reproduced together:

```sh
python3 repro/run_research_checks.py meridian-cusp
```

The scalar program composes signed crossing words and compatible typed products from their local formulas, retaining negative powers and both orders of opposite colors. It also checks the shifted-grid phase algebra. The geometric program verifies the rational meridian frames, the product and turn coordinate maps, the two half-twist signs, and the longitude correction under surgery. Python and SymPy are sufficient.

The [scalar proof](../../notes/actual_main_meridian_exact_scalar.md) and [longitude proof](../../notes/actual_main_meridian_preferred_cusp.md) explain the global conclusions. The programs check their local identities; the identification of the preferred peripheral curves and the uniform large-level estimate are arguments in those proofs.

## Running a named group

The [research-check runner](../../repro/run_research_checks.py) executes a selected group serially. The [group manifest](../../repro/research_check_groups.json) contains every command in its recorded order. Listing and previewing groups do not run a scientific calculation:

    python3 repro/run_research_checks.py --list
    python3 repro/run_research_checks.py general-plat --dry-run

To run one group, omit the dry-run option. The runner saves a separate combined output log for every command and a JSON summary containing exit codes and durations. It continues after a failed check so the summary records the whole selected group, then returns a nonzero exit code if any command failed. It does not run unselected groups. The individual scientific scripts keep their existing behavior, including any result files they normally write.

By default, logs go in a timestamped directory under the system temporary directory. To retain them in a chosen location, use:

    python3 repro/run_research_checks.py pointed-a --log-dir /path/to/check-logs

The runner uses the Python interpreter that launched it. Select another interpreter with the `--python` option if the chosen group needs a different environment. The manifest replaces the former long command block; it preserves those commands rather than silently adding them to every build.

## The moving-meridian filling calculation

The [moving-meridian theorem](../../notes/actual_main_meridian_filled_volume.md) has a focused reproduction group:

    python3 repro/run_research_checks.py moving-meridian-fillings

It compares 380 finite evaluations at 80-digit precision. One calculation raises the full crossing polynomial to its signed integer power in the quotient algebra. The other uses the root-grid trace, including the derivative term at repeated roots. The cases include both level parities, negative crossing powers, and displaced complex meridians. A separate exact rational calculation checks 18 quadratic Fourier comparisons with signed twist numbers of different sizes.

The [recorded output](../../experiments/main_meridian_direct_fillings_results.json) gives the precision and errors. These calculations test finite identities and normalization choices. The uniform contour estimates, the nonzero leading term and the identification with knot-complement volume are proved in the linked notes. The optional profile scan in the individual script is a numerical diagnostic, not a proof of the limit.

## Where to start for the current theorem

The proof has three kinds of inputs. Exact source identities retain every color, repeated-node derivative and scalar factor. Analytical estimates control the large-\(N\) limit uniformly on the domains used by the proof. Geometric constructions identify the cells, face maps, cusp markings and filling slopes of the actual complement. A finite algebra script can check an identity used in any of these arguments, but it cannot replace the uniform estimate or the topological construction.

The [two-leaf block inequality](../../notes/actual_conway_uniform_two_leaf_block_alias_gap.md) and [single-leaf attachment inequality](../../notes/actual_conway_single_leaf_alias_composition.md) have finite rational certificates. They bound the competing alias expressions over their whole slope domains. Their verification uses exact interval arithmetic, explicit remainder bounds and finitely many vertices of fixed polytopes. Candidate points may help find a certificate; the verifier proves the displayed inequalities without trusting an optimizer.

From the repository root, their principal verifiers are:

    python3 repro/run_research_checks.py conway-certificates

The [unflagged-region probe estimate](../../notes/actual_conway_unflagged_core_probe_bound.md) applies those scalar inequalities to arbitrary coefficient arrays with the stated bounds. The [spectral propagation proof](../../notes/actual_conway_mixed_core_spectral_propagation.md) then carries the estimates through turns and products, at the actual geometric action. These are written analytical arguments. They do not infer their conclusions from a longer list of sampled levels.

The [general marked geometry](../../notes/actual_conway_general_mask_marked_filling.md) follows the original diagram's face pairings and primitive cusp paths. Its completeness and smooth-filling arguments are also mathematical proofs rather than numerical manifold recognition. The theorem uses the original literal diagram for topology even when a different algebraic expression is useful for an estimate.

## Checks for the pointed quantum \(A\)-period

The [operator-period corollary](../../notes/actual_conway_pointed_quantum_a_volume.md) combines the exact ADO annihilator and finite-pointing theorems with the already proved knot-volume limit. It does not estimate the invariant by replacing a signed companion-matrix product with its norm. Its constant-term formula is exactly the original scalar.

The relevant scripts are:

    python3 repro/run_research_checks.py pointed-a

The first checks the generic finite crossing lift, finite-boundary identities and the repairs used when an elimination relation vanishes after summation or root specialization. The second checks moving-\(q\) germs, including singular recurrence steps and their bounded derivative budgets. The third checks the coefficient ratio of the banded Gram determinants against the actual finite vector of color values. The general existence, uniqueness and asymptotic statements still rest on the corresponding proofs. The recorded outputs specify exactly which finite cases were run.

## Installing dependencies and reading a result file

For the core symbolic and numerical scripts, install the recorded dependencies in a suitable Python environment:

    python3 -m pip install -r requirements-core.txt

A result file's scope field explains what a successful check means. Some scripts verify exact algebra; others compare an exact expression with an asymptotic approximation at selected parameters. Optional geometry checks may require SnapPy, Regina, Sage or packages named by that script. There is no claim that every historical diagnostic is one application-wide passing test suite.

The remainder is a topic-by-topic map of the earlier calculations. It retains their check counts and limitations so that a reader can reproduce an argument without confusing evidence for one formula with proof of a broader theorem.

## Coefficient regions in the general-plat method

In this group of notes, a degree records how much of a face variable occurs in a polynomial coefficient. The labels central, left and right name regions of those degree inequalities; they are not new types of knot crossing. A protected variable is one fixed by the marked coefficient extraction. A seam is a boundary shared by two such degree regions. These definitions explain why a theorem on one region need not control the whole coefficient sum.

### Sharp bounds and boundary arguments

The [closed-domain upper theorem](../../notes/research_global_sharp_coefficient_limsup_majorant.md), [full-fiber activation](../../notes/research_full_fiber_sharp_boundary_activation.md) and [stationary classification](../../notes/research_full_fiber_sharp_stationary_classification.md) prove the corresponding boundary and stationary statements. Their arguments establish the directional entropy gains, free-spectrum retuning and protected cap exclusions directly. The [odd main-strand cycle theorem](../../notes/research_stationary_noncross_main_cycle_obstruction.md) uses exact source characters and original face demands; the [flat-cap limitation](../../notes/research_flat_cap_no_local_exponential_angular_gap.md) is an exact alternating-sum inequality.

The [seam theorem](../../notes/research_sharp_cross_degree_domination_and_seam_gap.md) concerns the boundary between two degree regions of the original coefficient sum. Its moving cosine-log integral and pointwise tail comparison prove all-spectrum central-degree domination; exact latent-triangle strong concavity gives the explicit gap $\gamma_D=\pi a_D^2/2$. The existing whole-domain integration-by-parts theorem retains all charge currents and gives seam-period negligibility for fixed long fillings. These conclusions are analytical. For this general-plat route, the remaining macroscopic noncentral part is not controlled by the seam theorem alone.

The four-state and window audits below support the retained finite source factors and indices; they do not establish the analytic majorant, classify its maxima, or prove a global volume comparison. Each linked note states the domain and hypotheses of its proof.

## Exact transfers supporting the phase estimate

The analytic phase argument has two focused finite checks:

    python3 repro/run_research_checks.py phase-transfer

The [four-state audit](../../experiments/audit_research_original_four_state_transfer.py) checks 196 recurrence/path comparisons and 85 exact omitted-half scalar identities across ten levels and both parities. The [window audit](../../experiments/audit_research_regular_spectral_window_phase_exclusion.py) checks 402 exact restricted matrix/path identities for half and full rows, including sampled spectral zeros and zero outer weights. Its equality is sign-adjusted on both sides; the common raw sign is established in the source proof.

These validate finite indexing and retained factors. The original physical-matrix interface is inherited from the stated original numerator formula. The positive transfer, analytic gauge, strict boundary gaps and shared-torus phase exclusion are proved analytically; these finite checks do not prove their exponential estimates or a global volume bound.

The [protected-window and mixed-cycle extensions](../../notes/research_mixed_cross_window_cycle_packing.md) combine local transfer identities with a finite packing of graph cycles. The outer-zero proof specializes the exact transfer; the middle-zero proof retains the actual initial seed and proves its output reflection by finite tilings. The whole-central input uses the central factorization and cofactor angular theorem. Fractional cycle packing is a finite combinatorial argument. Those consequences use no extrapolation of numerical rates; the stated global majorant comparison remains conditional.

## A focused starting set

With the dependencies above installed, these four scripts are a smaller entry point into the local recoupling and positive variational calculations:

    python3 repro/run_research_checks.py local-foundations

Read the corresponding result's `scope` field before interpreting its reported outcome.

The arbitrary-plat advance has a separate focused set:

    python3 repro/run_research_checks.py general-plat

The root, complex-action and amplitude notes contain their analytical proofs; root finding and large-level comparisons are regressions. The magnetic audit also tests the original finite Casimir equation and the exact joint rational formula, retaining the difference between Gaussian and positive sine binomials. The character and regulator audits check exact rational identities in formal variables. The marked gluing audit uses an actual three-cusp triangulation; the critical-scheme audit checks local inverses and 24 incidence graphs. The reflection and graph audits replay actual finite sources. None of these checks proves the missing general global asymptotic.

The joint determinant audit checks the source polynomial before continuation, its three-term recurrence and positive principal minors. The joint amplitude audit compares the literal finite sum with its determinant and asymptotic, including both derivative corrections at folded channels. The framing audit verifies the stated equivalences and local construction; it does not search for or prove a favorable common frame for every plat.

The generic-normal audits compare the original generic columns and derivatives, including the exact large-partner collision tail and nonzero extra-pole residues. The right-angled obstruction audit checks reflection signs, polarization identities and exact two-facet examples. Its general conclusion rests on the separate proof of the literal Morse-prefix dictionary and convex incidence, not on extrapolating those examples.

## The exceptional-period checks

The matching-edge contour method has focused audits for the generic Casimir polynomial, its root location and positive endpoint convolution, the actual inverse-turn character relation, and the full resolvent with its normal poles. The strict-prefix and Green-action audits check original matrix entries and selected logarithms. The rectangle audit verifies the actual primitive words for all three half-twist cases. Each note links its script and recorded output.

The endpoint resolvent proof uses a unitary congruence and exact Schur denominator; it does not claim a Hermitian similarity or a polynomial bound for individual spectral projectors. Numerical rate samples supplement the written asymptotic proofs. None of these local or endpoint checks establishes a contributing contour or the general source asymptotic.

## Rebuilding this guide and its figures

The guide is generated from `book/chapters/` and the published notes. Its static HTML uses native MathML and local CSS and JavaScript; reading it requires no account or external math service.

```sh
python3 tools/build_book.py
python3 tools/check_book.py
python3 -m http.server 8000 --directory docs
```

The build requires Pandoc. TikZ sources and their compiled PNG/PDF figures are retained in `book/figures/`. To regenerate the figures, install a TeX distribution with TikZ and the optional Python package PyMuPDF, then run:

```sh
python3 tools/render_figures.py
python3 tools/build_book.py
```

The guide explains the argument, while the linked technical notes contain the detailed proofs. Existing note paths and audit imports remain stable.

The physical paired-normal audit checks the original Casimir entries, weighted Dirichlet identity, double-node reflection and actual generic derivative. Its polynomial estimate is proved on the physical grid; it is not a complex-neighborhood or whole-source theorem.

The near-fold complex audit retains the full large generic source and checks the resonant recurrence on a small complex circle. Its subexponential theorem requires shrinking scaled channel windows. The matching-edge audits reconstruct the actual generic matrices on four external representation factors, pivotal signs, root first jets and original row measure. They retain unequal partner derivatives and do not infer a completed positive matrix norm from the scalar formula.

The full physical packet audit tests the cone determinant, finite boundary zeros, generic matrix lifts and actual amplitudes outside the old central wedge. The physical generic-jet audit retains both forward and backward q recurrences and nonzero higher divided-pair jets. The localization audit checks the exact low/high flag formulas; its general conclusion is the written continuation and geometric argument. None establishes a contributing global cycle.

The completed-projector audit checks the categorical norm, full generic operator identities, actual cyclic turn, paired cluster jets and complete original-measure cancellation. It retains the nilpotent contribution and unequal scalar derivatives. Its finite checks support the written identities; they do not bound the native projectors or establish a global volume limit.

The native-energy audit checks the actual generic high-degree adapter, dual measures, residue and completed-projector jets, and exact rank-one norms. The exponential midpoint-energy rate has a written Riemann-sum proof; its numerical sequence only illustrates that proof. The theorem retains the energy rather than asserting polynomial projector norms.

The energy-profile audit checks actual Fourier norms, vanished unused nodes, canonical midpoints, both-parity endpoint source formulas and the selected dilogarithm constant. Its even finite full-norm samples concern the nilpotent operator; the completed projector's rate follows from the separate polynomial comparison. The local geometry audit checks original phases, measures, parity factors and all four tetrahedron shapes, without inferring global phase matching.

The shrinking-fold audit checks the actual source formula outside complete support as well as its endpoint and measures. The coefficient audit checks log-concavity, tilted modes, literal complex-radius normalization and interior coefficient rates. The shared-cycle audit compares against original Morse contractions, including the first-failure zeros, both-parity carrier cancellation, exact Kirchhoff support and marked charge. The resulting global Cauchy comparison remains an upper bound.

The positive-partition audit reconstructs the original endpoint and white scalars, the high-degree Chevalley adapter, and full phase-bearing sums before checking their Cauchy bound. The radial-obstruction audit checks the finite phase derivatives, adapters and cup/mark relation; its general geometric conclusion uses the separately proved common-frame obstruction. Neither audit claims a global rate gap or volume equality.


## The full positive endpoint volume theorem

The half-block audit compares the original numerator coefficients, the positive path recurrence, negative roots, exact extreme coefficients, and the finite Lobachevsky formula. Its finite rate profiles remain diagnostics; the uniform closed-domain limit has a written proof.

The earlier shared-source audit checks 228 original coefficients, 4590 support patterns, 748302 affine-cut conditions, 118 one-level support certificates and 236 eventual-flow tests. Those tests remain relevant to fixed half-label patterns. The full-kernel theorem instead uses every degree-$N-1$ monomial, continuous entropy on the full simplex, and unrestricted integral flow rounding. A separate transfer audit checks 39599 Laurent coefficient comparisons and the path injection used in the central corridor.

The [general endpoint theorem](../../notes/general_fejer_endpoint_source_volume.md) proves the geometric upper bound as well. Its [structural audit](../../experiments/audit_general_fejer_endpoint_source_volume.py) constructs actual Morse faces at widths two, three and four, retains edge identities through genuine identity smoothing, and finds digon disks from the dual graph independently of the Hall subsets. It checks 41 loopless smoothings, 918 hybrid patterns, 121004 Hall cuts, 716 tight sets and 816 independent positive-arc max-flow tests. The general Hall classification, source reduction and volume comparison have separate written proofs.

The [signed-chain audit](../../experiments/audit_actual_fejer_hybrid_piece_representation.py) checks 270 signed cyclic fans, four repeated-contact fans, 24 actual circle/line tangencies, eight contact triangles and two oriented strip chains. These validate the volume formulas; the original group pairings, degree-one relative chain and compatible cut-disk collapse are analytical arguments. The [serial audit](../../experiments/audit_actual_fejer_serial_coupon_bound.py) compares 3960 original physical entries, including 1290 illegal-total zeros, and 3120 independent coefficient bounds for literal powers of the same ordered-pair coupon.

The [odd regularization audit](../../experiments/audit_actual_fejer_odd_regularized_full_numerator.py) checks the original spectral derivative and the positive comparison used for the odd coupon $V_N(-2)-N^{-2}V_N'(-2)$. The resulting whole-source spectral-jet bound is exact at both parities. These are spectral derivatives at the fixed root, not genuine-$q$ normals. Recorded replays accompany the formulas; finite fixtures do not establish a selected Gaussian cycle, a complementary phase estimate or the general filled-knot asymptotic.


## The full spectral numerator packet

The [full packet theorem](../../notes/general_full_spectral_numerator_geometric_packet.md) is an analytical assembly of exact source identities, relative complex cofactor estimates, a global angular gap and the original shared Cauchy coefficient. Its finite tests are scoped to those inputs; samples do not prove the uniform asymptotic or select the later spectral Gaussian contour.

The [factorization note](../../notes/actual_cross_cofactor_factorization.md) compares the central formulas with the original unused-row path polynomial and retains both parity endpoints and the odd central-skipping term. The [interior adapter audit](../../notes/actual_cross_cofactor_interior_packet.md) checks 1056 row-replaced determinants, 352 independently constructed original q-Hahn matrix node values, 352 sine-product scalars and 960 tail factorizations at 85 digits. The analytic proof separately supplies the exponential interpolation error and discrete saddle estimate for all physical starting rows.

The [protected-middle angular audit](../../notes/actual_cross_cofactor_protected_angular_gap.md) checks 4636 coefficient bounds, 486 complex angular inequalities, 432 actual three-step matrix entries and 16 exact monomer cases. The [marked-action audit](../../notes/actual_cross_cofactor_marked_action.md) compares 24 independent source/cofactor integrals, 17 integral derivatives and 12 literal whole Gauss/collar configurations, together with polarization and Gaussian boundary cancellations. Independent fresh replays reproduce those checks.

The protected-middle relative packet, [nodal rigidity](../../notes/actual_cross_cofactor_interpolant_rigidity.md), [global local-angle theorem](../../notes/actual_cross_cofactor_global_angular_gap.md) and the whole-source assembly have analytical proofs. The finite Cauchy--Lagrange and original face-torus arguments carry the asymptotic conclusions. The [direct-power scope](../../notes/fixed_root_direct_power_scope.md) retains all fixed-root spectral derivatives while keeping genuine-$q$ normals separate. Those input audits do not establish global charge dominance or the general filled-knot limit. The later localized contribution is proved by the analytical argument below.


## The localized original filling period

The [localized unit-charge theorem](../../notes/general_localized_unit_charge_filling_period.md) retains the original marked prefactor, finite-level action, both determinant branches and every boundary term when the integration cube is translated. Its proof gives a nonzero relative Gaussian coefficient at both level parities. The [charge comparison](../../notes/general_local_charge_critical_monotonicity.md), applied to that same finite action, bounds the other charges in a fixed finite local box.

The exact remainder keeps the finitely many selected charges outside the cube and all other charges on their whole original domains; it does not separately sum remote sharp-cube pieces. The proof does not bound this global remainder or establish the general filled-knot volume limit.

## Whole-domain bounds and the balanced full invariant

The [large-charge audit](../../notes/actual_whole_domain_large_charge_tail.md) checks original operator entries, both signed Gaussian exponents, and paired endpoint currents. The [diagonal-sector audit](../../notes/actual_global_diagonal_spectral_sector_gap.md) includes removable physical nodes, exact path partitions and sewn polynomial integration-by-parts checks. The [central audit](../../notes/actual_global_cross_spectral_gap.md) checks the start decomposition, rescaled transfer matrices and finite characteristic formulas. Their recorded finite checks support the exact formulas. The uniform bounds are established by the written proofs.

The [whole-central period](../../notes/general_all_cross_long_filling_volume.md), [all-angle left envelope](../../notes/actual_global_left_weighted_spectral_envelope.md), and [complete-radius balance theorem](../../notes/general_complete_radius_balance_filling_volume.md) prove the stated conditional full-invariant result. Their arguments retain entire-domain remote charge sums and endpoint currents, including both level parities. The elementary [entropy lemma](../../notes/actual_triangle_entropy_algebraic_balance.md) checks the absolute half-degree normalization and all protected-zero cases. These arguments prove a full invariant theorem under the stated balance hypothesis. Those conditional arguments alone do not prove realization. The uniform family construction below supplies it, without treating numerical experiments as a proof.

## Uniform width and exact bridge number

The [family theorem](../../notes/general_one_end_layer_long_filling_volume.md) checks the literal incidences, packing reflection, both recurrence branches and endpoints, then proves the required convex comparison. That proof covers every $k\geq2$; finite packing samples do not justify its coverage. The [zero-middle lemma](../../notes/actual_zero_middle_nine_quarter_balance.md) uses an exact rational lower bound. The [Fox certificate](../../notes/actual_fox_coloring_exact_plat_bridge.md) proves the signed crossing identity, invariance, exact plat count and bridge bound directly. No numerical asymptotic or coverage audit is claimed for these proofs.

The two focused family audits supplement these proofs: the reduced-source audit checks 38 literal widths and the rational comparison seed; the one-end-source audit checks 39 literal widths, the changed linear boundary, and all circle contacts and noncontacts in the exact width-two and width-three packings. These finite checks do not replace the uniform convex comparison.

## Shared-radius certificates beyond complete-packing balance

The [anchored theorem](../../notes/general_anchored_shared_radius_filling_volume.md) retains common-face Cauchy bounds, both parity partitions, a fixed complex strip and the entire Fourier remainder. Its explicit example uses six stated rational vectors. Arb interval arithmetic evaluates finite Lobachevsky sums with an explicit uniform tail bound; exact algebra checks the original golden-ratio packing. The resulting strict inequalities certify this example, not universal coverage of the criterion.

The [fixed-triangle capacity lemma](../../notes/actual_fixed_triangle_boundary_capacity_gap.md) is analytical: closed strong concavity gives the explicit squared-distance loss, and finite convex separation proves the shared dual formula even without attained positive multipliers. It does not assert the same comparison for fractional identity mixtures.

## A structural extension at arbitrary fixed depth

The [unit-chain theorem](../../notes/general_marked_unit_chain_filling_volume.md) proves the literal prefix dictionary and an exact extension into the empty marked gap. Its proof preserves every old disk and checks every added crossing-circle block analytically; depth is arbitrary. The focused audit checks 56 original source charts and 12 exact small seed extensions, including 1,084 circle/line support pairs. These finite checks support the source dictionary and geometry, while the proof establishes the unbounded-depth statement.

## Simultaneous insertions at every initial bridge gap

The [simultaneous theorem](../../notes/general_simultaneous_bridge_gap_filling_volume.md) has an analytical proof and a finite audit. The audit checks 413 nonuniform-depth source charts, seven exact symbolic transport/ratio identities, and 25 joint small packings with 2,333 support checks. The analytical proof establishes the general source induction, disjoint-gap construction, curvature order and every local block bound. The extended diagram retains its own full normalization; no equality of its framing scalar with the core's scalar is asserted.


## Refined sector covers and a rigorous obstruction

The [general finite-cover theorem](../../notes/general_actual_sector_cover_filling_volume.md) partitions the source and transfers the entire Fourier remainder using the original shared face targets and both level parities.

The [separation verifier](../../experiments/audit_actual_shared_radius_certificate_separation.py) checks that both certificates use exactly the same original expression with seventeen crossing-circle blocks and the same mark. An 84-variable rational flow rules out one anchored test by more than $0.025$; an 83-variable complete flow and forty rational radius vectors certify the refined cover by more than $0.04$. All face equations are exact, and Arb evaluations include explicit Fourier-series tails. The public scripts contain no numerical optimizer or private diagnostic inputs.

The [undivided positive-capacity obstruction](../../notes/actual_complete_source_cauchy_capacity_gap.md) is analytical. Its proof establishes coercivity, rules out escaping level-dependent radii, and distinguishes the bound's exponential loss from the actual coefficient's correct volume rate. The proof retains the finite positive-source normalization and the pure-face entropy values.


## Uniform coefficient energy and rearrangement

The [protected-outer audit](../../experiments/audit_actual_protected_outer_spectral_energy.py) constructs the physical coproduct Casimir and extracts coefficients by the original finite Fourier transform. It verifies both parity reference factors and exact spectral sampling nodes. Symbolic identities and fixed integral checks supplement the analytical uniform boundary proof.

The [general one-sided audit](../../experiments/audit_actual_one_sided_relative_spectral_energy.py) separately verifies the nonnegative parameter expansion, signed-parameter Cauchy inequalities, interior original coefficients, and the rearrangement identities. The uniform transfer estimate and compact finite-tilt argument are proved analytically, rather than inferred from sampled large levels. The local theorem and its shared-flow consequence have their stated hypotheses; the audit does not establish a stronger global entropy inequality.

Four earlier audit consumers now import the physical `Local` class from its defining public module. The lightweight face compiler remains independent of quantum-only imports. Its tensor-contraction helper is now included explicitly and imported by the ten published consumers. The existing small-circle audit replays with results exactly matching its recorded output.

## Reproducing the fixed-sector obstruction

Run both exact checks with one command:

```sh
python3 repro/run_research_checks.py singleton-envelope
```

The [obstruction proof](../../notes/actual_singleton_sector_envelope_obstruction.md)
explains the two independent computations. The first checks exact rational
loads on the original shared faces and a strict entropy excess. The
second checks the oriented sphere, dual matching, mark, and one-component
strand pairing. The proof of nonzero support is written separately from
the envelope inequality. The resulting obstruction concerns that
particular coefficient bound; it gives no lower bound for the signed
invariant. Both programs require only Python’s standard library.
