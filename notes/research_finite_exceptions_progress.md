# The finite-exception problem: current research status

25 November 2026. The finite-exception theorem is open. This note records
the current question and the general reductions being pursued. The
[papers](../papers/README.md) contain the established volume results;
the research reductions below do not enlarge their hypotheses.

## The established result and the stronger question

Fix one finite strict Conway construction, its crossing circles and a
half-twist pattern whose strand connections give a knot. Write
\(p=(p_1,\ldots,p_b)\in\mathbb Z^b\) for its auxiliary integral filling
coefficients. The [Conway theorem](../papers/conway-asymptotics/README.md)
gives a threshold \(P_0\) such that the volume identity holds whenever
every \(|p_i|>P_0\). All these coefficients are fixed before the quantum
level \(N\) tends to infinity. This covers density one in the assignment
lattice; its complement still contains infinitely many assignments.

The stronger target is:

> After fixing any short partial filling, all sufficiently long fillings
> of the remaining coordinates that produce hyperbolic knots satisfy the
> volume identity, with a threshold allowed to depend on the fixed data.

The [finite-branching argument](research_finite_exceptions_under_partial_fillings.md)
explains how the required statements for successive partial fillings
would imply finitely many exceptional assignments for one template.
The [definitions](research_strict_conway_family_definitions.md) specify
the tangle operations, primitive slopes, component test and quantifiers.

Exact tangle reductions can have infinite fibers: infinitely many
assignments can describe one unresolved core knot. The
[affine-fiber theorem](research_affine_reduction_fibers_and_core_obligation.md)
decides this on each recorded reduction branch. The padding argument in
the finite-branching note shows why the general assignment statement
already entails a volume theorem for every hyperbolic core allowed by
the construction. Redundant assignments cannot simply be discarded.

## What orthogonality changes

For a finite synthesis map \(B\), an expanded state \(Bc\) has energy
\(c^*B^*Bc\). The Gram matrix \(B^*B\) retains exact linear relations;
replacing it by the identity can create spurious energy. The
[conceptual chapter](../manuscript/sections/02-exact-concepts.tex) and its
[formal statements](../repro/PAPER_FORMAL_COVERAGE.md) give this algebra
and its limitations. A norm estimate alone gives no lower bound for a
specified closing functional.

The [normalized finite-source construction](research_convex_normalized_conway_source.md)
encodes the actual packet equations and scalar closing in one residual
energy. Its proof retains the normalization budget that connects this
energy to the original invariant. The
[linear-elimination theorem](research_conway_orthogonal_linear_elimination.md)
then removes every linearly entering packet exactly.

In its notation, retain one child packet \(u\) at each binary product and
call the other packets \(z\). The stacked residual is
\(A(u)z+b(u)\), with \(A(u)\) of full column rank. Minimizing in \(z\)
gives

\[
 z_*(u)=-(A(u)^*A(u))^{-1}A(u)^*b(u),\qquad
 f(u)=\|\Pi(u)b(u)\|^2,
\]

where

\[
 \Pi(u)=I-A(u)(A(u)^*A(u))^{-1}A(u)^*.
\]

Here \(\Pi(u)\) is the orthogonal projection onto
\(\ker A(u)^*\). The proof checks that the eliminated ball constraints
are inactive and retains the original scalar closing. This reduces the
finite problem with its full Gram matrix present.

The [reciprocal-source comparison](research_conway_reciprocal_finite_fiber_lower_bound.md)
uses orthogonal projection on finite fibers. The
[residual-degree reduction](research_conway_logarithmic_reduced_residual_degree.md)
compresses the remaining nonlinear dependence further. These are finite
algebraic or variational comparisons. Neither evaluates the remaining
minimum at the hyperbolic-volume rate.

## The other current source calculations

Two related lines of work retain exact phases and the prescribed source.

- The [coideal Fourier compiler](research_coideal_full_fourier_crossing.md)
  expresses the actual crossing in orthogonal coordinates, with the
  neighboring-height channels and original cup retained. The
  [initialized period](research_coideal_normalized_marked_period.md) and
  [quantum flag source](research_true_cup_quantum_flag_source.md) make the
  corresponding source and marked observation explicit. These identities
  do not supply a lower bound for every closed word.
- The [cyclic Hardy comparison](research_cyclic_atom_hardy_head_comparison.md)
  proves that the physical coefficient projection loses at most a
  polynomial factor in the scalar function norm. It builds on the
  [near-unit-circle estimates](research_cyclic_atom_near_unit_circle.md).
  Gluing these functions and estimating their original marked scalar
  remain separate requirements.

The [Rivin boundary comparison](research_rivin_jones_partial_filling_assessment.md)
keeps the exact matrix presentation distinct from geometric optimization.
Casson--Rivin optimization identifies a geometric action under its
hypotheses; it does not show that its point occurs with a nonzero
coefficient in the original finite sum. A
[filled-cover obstruction](research_filled_cover_slope_length_obstruction.md)
also rules out making a short filling slope long by an unbranched cover
compatible with that filling.

## The remaining theorem

The task is to evaluate the retained finite source at the geometric
exponential rate, including its normalization budget, for arbitrary
fixed short partial fillings. A successful argument must control the
original closing observation and possible cancellation, beyond the
existence of a local geometric critical point or a positive ambient norm.

The previous append-only record mixed these questions with thousands of
earlier case calculations and changing status reports. Its complete
text remains in the
[pre-cleanup snapshot](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_finite_exceptions_progress.md).
Earlier partial cases are not additional premises of the manuscripts.
