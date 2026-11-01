# Audit of insertion at an ordinary triangular face

This record concerns Appendix R and the scalar implications formalized in
`formal/VolumeLogic/TriangularBoundary.lean`. It distinguishes the new
argument from the analytic and geometric results it imports. The source
hashes in the accompanying snapshot identify the versions read.

## What the argument must establish

The input consists of fixed marked matched spheres. Each inserted piece
has a strict certificate for every locally allowed noncentral string,
including strings whose old global coefficient vanishes. The core has
such a certificate as well. At each selected ordinary triangle, both
boundary ratios must be sufficiently small at every chosen core witness
and at the complete vector. These are hypotheses on finite weight
vectors, not assumptions of the desired final remainder bound.

The review checked the following transitions directly.

1. The conditional disk action has a minimizer. Strict transport
   inequalities imply coercivity, and the grounded Hessian gives
   uniqueness. Strict convexity alone would not establish existence.
2. Its developed center triangles fill the boundary triangle once.
   Boundary derivatives therefore agree with the original triangle
   potential. The jointly controlled limit to two zero boundary weights
   determines the constant with the original normalization.
3. The conditional root circle lies in the bounded interstice. Maximizing
   the empty radius and using the three tangency equations selects the
   positive Soddy curvature. This supplies the middle-weight comparison
   only where it is needed: at the wholly central conditional minimizer.
4. Every old noncentral certificate extends to small positive boundary
   weights. The newly allowed protected-overload terms tend to minus
   infinity. Finiteness makes the chosen threshold common to all strings.
5. The bridge comparison retains the original targets. The core alone
   supplies the demands at the two deprotected vertices. Only the third
   boundary target is duplicated in the two input expressions.
6. The case distinction uses the entire inserted block. If it is central,
   its conditional action correction cancels exactly and the bridge has
   zero error. Otherwise its absolute certificate absorbs the error,
   bounded by half the boundary correction. No ordering condition on a
   noncentral witness or on the core's opposite middle is needed.
7. Several insertions may share boundary vertices, but use distinct
   matching pairs and fresh interior vertices. Their corrections add
   with one retained core target at each shared ordinary vertex.

The exact even-chain curvature recurrence supplies thin boundaries for
any fixed finite list of pieces. Its all-length inequalities are proved
from decreasing curvature ratios. The finite interval calculation only
checks the fixed constants appearing in those inequalities.

## The explicit seventeen-region insertion

The portable command is:

```sh
python3 repro/check_triangular_boundary_certificate.py \
  --output repro/results/triangular-boundary
```

It requires `python-flint` and NumPy. It checks the original marked source,
its rational complete flow, the forty-branch cover, and the five newly
allowed overload anchors at chain length `2**20`. The branch margins
exceed `0.02`. The written monotonicity argument extends these same
witnesses to every larger even length. The script also checks the finite
incidence constructions and the earlier rational obstruction used to
retain a failure of weak balance. Its report states the precise checks
performed; it does not evaluate a million-region knot invariant.

The small-boundary condition for persistence of the balance failure and
the condition for extending the source certificate are separate. The
former follows already at length 64 from an elementary bound on the
boundary correction. The exhibited source witnesses require a much
larger length. Neither integer is a bound on the eventual crossing
powers. Those powers have their own long-filling threshold after the
whole diagram is fixed.

## What Lean verifies

The nine new declarations construct the local comparison from the same
three maxima as the protected-sum module. Every rate and gap is doubled.
The variable `t` is twice the removed triangle potential, and `b` is the
boundary logarithm; `t-b` is the undoubled correction. The duplicated
target is `2*b`. The final Boolean test includes noncentral labels away
from the attaching region, so it cannot confuse a central root with a
central block.

The declarations retain the triangle lower bounds, the conditional
central value, and the noncentral certificates as explicit hypotheses.
Their compilation proves the resulting scalar implications. It does not
prove existence of the weight vectors, disk development, or the volume
conclusion.

## From the source bound to the knot complement

Appendix R supplies the strict estimate for the whole complementary
source polynomial. Appendix N supplies the exact finite filling norm
with its canonical degree restriction. Appendix O supplies the nonzero
central period, smooth completion along the final original primitive
slopes, and comparison of its action with the volume of that same
completed metric. The final argument chooses the fixed filling threshold
so that the action drop is smaller than the source gap.

The complete augmented actions add under insertion. Filled volumes are
not asserted to add. The final crossing circles belong to the assembled
diagram, and the final strand connections must themselves give a knot.
The main cusp remains complete. The conclusion includes both parities
and composite levels; the diagram and the signed powers are fixed before
the level limit.

This reading found no correction to the strengthened whole-block
argument. It is not a new end-to-end verification of every result
imported from Appendices L, N and O. The dependency map keeps those
written inputs explicit and leaves the unrestricted matched-sphere
remainder problem open.
