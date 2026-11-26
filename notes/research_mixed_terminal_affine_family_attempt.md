# Outcome of the first full-disk affine enclosure

Research record, 6 November 2026. The
[fixed affine-family protocol](research_mixed_terminal_affine_family_certificate.md)
was executed once. Its
[saved result](../repro/results/research-mixed-terminal-affine-family.json)
has SHA-256
908232a2fc15d731c13803cd503c7b0d70c579f9cbf1896543f7233df2196370.
The process completed with exit code zero and unchanged inputs.
No family was certified.

The calculation made four inverse/derivative proposals at the already
saved central points. It tested the sixteen prescribed error-radius
vectors, without a new root solve, subdivision, primitive evaluation,
source sum, or precision change. Two of the larger proposed boxes left
the original common coordinate domain. For each of the other fourteen
boxes, the certified upper bound for the weighted derivative norm
exceeded \(9/5\), so it could not prove contraction. Every proposed
inclusion had a negative lower margin in at least one row.

These are insufficient upper bounds. They do not prove that the true
derivative norm is large, that an affine enclosure does not exist, or
that the source comparison fails.

The saved central derivative proposals exhibit the reason to preserve
correlation: the shared coordinate has a proposed derivative modulus
near \(0.09\)–\(0.11\), while the adjacent ordinary coordinate has one
near \(0.39\)–\(0.49\). These proposals alone are not derivative
certificates. The calculation encloses the derivative matrix on an
independent rectangular product, where repeated occurrences of a
logarithmic argument no longer share their dependence on the one
parameter. Its preconditioned residual upper bounds are too large to
close the fixed-point estimate.

The next analytic improvement is therefore to expand each original
logarithm along the common affine parameter before bounding its
remainder. In that form the Hessian is a sum of rank-one terms, and
each repeated argument is bounded once. The present record is retained;
no larger radii, denser parameter grid, or precision retry is part of
this completed protocol.

The critical point still exists and is unique by the earlier analytic
theorem. What remains unproved is the sharper uniform enclosure needed
to transport the source value and force inequalities.
