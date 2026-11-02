# Directed tree estimates and the quarter-index recurrence

This review accompanies two papers extracted from the retained arguments,
and the formal differentiation of the actual supported triangle potential.
The 374-page reference manuscript and its mathematical sources remain
unchanged. The new papers have 15 and 11 pages. Their statements do not
enlarge the diagram classes covered by the arguments they import.

## Directed circle trees

[Local degree and twist bounds for circle-tree volume limits](../papers/directed-tree-asymptotics/main.tex)
proves a finite directed criterion for a fixed ordered tree with a crossing
circle at every vertex. Endpoint tracing must give one knot, with no
internally closed extra main component. The diagram, degrees and all
signed powers are fixed before the quantum level tends to infinity.

The analytic imports are unconditional edge estimates, not the companion
paper's summed volume theorem. The new proof retains the full Newton
kernel, including the indices and repeated-root derivatives outside its
central range. On a complex parent rectangle its exponential bound uses
the actual conditional phase. For large real child angles, the proof
first estimates a positive finite sum at the real parent angle and then
bounds its vertical change. Near zero it uses the actual complex edge
asymptotic. Replacing the conditional phase by a coarse bound at the
complete point would spend the margin needed in the induction.

Each child polynomial is divided by its exact value at zero. The proof
establishes that value's nonvanishing and keeps its complex scalar
throughout the recursion. The charge calculation retains the zero-mode
endpoint currents and all other connectors. Errors for nonminimal
charges are additive errors measured from the conditional complete
action; the proof does not assert a relative approximation at an
arbitrarily lower critical value. A new outgoing real-domain estimate
closes the induction. It is imposed only at nonroot vertices, since the
root sends no polynomial onward.

Restoring the child constants recovers the original joint stationary
action. The existing positive-octahedra theorem then supplies the
primitive filling, complete main cusp and absolute volume. Its weaker
geometric threshold is checked from the directed certificate.

The mixed consequence permits, at each vertex, either degree at least
\(2^{28}\) or absolute signed power at least \(2^{27}\). The earlier
condition \(\max_v d_v/(d_v^2+n_v^2)\le2^{-120}\) implies that
alternative and is now a corollary. Its separate tiny-disk induction is
unnecessary in this paper. The summed theorem's sharper second-order
meridian remainder is not claimed here.

The reproduction combines 34 rational comparisons, eight exact endpoint
pairings and 48 high-precision finite recursion cases covering 180 root
choices. The latter compare quotient evaluation with complete value and
first-normal contractions; they are numerical finite checks, not a proof
of the analytic induction. Negative controls distinguish an outgoing
bound incorrectly imposed at the root and an odd stack substituted for
the required even stack.

## The quarter-index coefficient

[Asymptotics of signed Newton coefficients near the quarter index](../papers/quarter-index-asymptotics/main.tex)
proves a local estimate for the original finite coefficient. At quarter,
its two characteristic roots are distinct but have equal modulus.
The high-index contraction alone does not control passage through this
point.

The analytic matrix reduction is performed on a fixed complex domain.
Its exact backward conjugation has a quadratic diagonal correction,
so repeated reduction preserves the eigenvalue gap and leaves an
exponentially small off-diagonal remainder. Only then is a shorter
propagation interval chosen. The cumulative competing action is negative
at every target, while the absolute relative action at every intermediate
position stays below the reduction's exponential margin.

Both coefficients at the anchor are taken from the actual finite sum.
The selected coefficient is nonzero and the competing one is retained.
The interaction identity controls conversion between them along the
entire interval. Analytic Euler–Maclaurin summation then produces an
explicit holomorphic interpolation with exponentially small error on
the physical integer grid. Its endpoint factors recover the same
amplitude and action as the high-index normalization.

The signed coefficient retains its chirp and absolute shear constant.
The local finite-window consequence keeps the original affine lattice
offsets and bounds interpolation errors before deforming a contour.
It assumes a strict real stationary point and a negative definite wire
Hessian. It does not bound the global complementary source, continue
through colliding roots or prove a further whole-invariant volume limit.

The exact checker compares the literal finite factorial sum with its
recurrence at 34 level/prime pairs, comprising 268 recurrence positions
and 102 terminal rows. Twelve rational matrix examples check the shifted
backward conjugation, and four ordered products retain two nonzero input
components. These checks supplement the written uniform proof.

## The actual triangle potential in Lean

[TrianglePotential.lean](../formal-real/TrianglePotential.lean) starts with
the Lobachevsky integral and the supported supremum printed in the
planar paper. It proves entropy continuity and concavity, shows that the
explicit arctangent loads are feasible and maximize the objective, and
derives the derivative of that maximum. The common multiplier cancels
the derivatives of the loads through their proved mass conservation.
No entropy-gradient identity is introduced as a hypothesis.

The singleton case uses the same supported supremum and has its unique
feasible load, affine value and zero second derivative. The shared-sum
theorems keep one variable at each common vertex and count the linear
demand once. Mixed rows may be singletons or have positive radicand;
their first and second derivatives are proved along the actual affine
path. Singleton rows contribute zero graph weights.

The geometric incidence map, positivity and connectivity of its support,
the Hall inequalities supplying a transport table, and changes of support
under degeneration remain written application arguments. The new module
does not formalize contour deformation, quantum source dominance or
hyperbolic metric completion.

## Scope of the records

The [companion snapshot](directed-quarter-audit-snapshot.json) records the exact sources read, the finite replay,
the formal replay and the separate proof-reading reports. The dependency
graph now separates the finite edge kernel from its analytic estimates,
and records the old local condition as a consequence of the directed
theorem. Graph checks establish consistency of the declared dependencies,
not correctness of the proofs at their vertices.

The broader strict-Conway construction still needs its remaining
normal-form, boundary comparison and marked-geometry accounts. All-orders
meridian expansions and preferred-longitude conclusions also remain
separate extraction and review tasks. They are not inferred from the
local quarter-index theorem or from the directed leading asymptotic.
