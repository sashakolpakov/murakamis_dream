# One fixed last-row height-chord diagnostic

This is a **double-precision diagnostic**, not a certificate. It follows
the separately certified untrimmed auxiliary example in
[the research note](../../../notes/research_mixed_last_row_auxiliary_obstruction.md).
No optimization, grid, parameter cover, or actual open word is used here.

Take the right intersections of the reduced input circles with the
weakest attached height bounds:

\[
 a=.30+\sqrt{.060^2-.056^2}-.108i,\qquad
 c=.35+\sqrt{.083^2-.062^2}-.072i.
\]

Use the original own-type-three two-leg map with external order
\((a,c)\), and retain both original logarithmic equations. The first
external leg has type four. At the horizontal target \((.45,.45)\),
the calculation retains its factorial halfweight and the exact signed
revived-row carrier. The result is approximately

- \(a=.32154065923-.108i\), \(c=.40518151865-.072i\);
- \(s=.39890315788+.02398890643i\),
  \(b=.33572077244+.01740047644i\);
- last-row deficit from the affine-quadratic plane:
  \(+.0023770011\).

This suggests that cutting the auxiliary disks only by the weakest
open-leg **height** bounds still leaves an unfavorable region. It is
not evidence for an actual-word obstruction. The type-three input
\(c\) fails the joint actual geometry in every possible role:

- It cannot be an ordinary type-three leg, since \(-.072<-.065\).
- It cannot be an attached type-three leg, since
  \(.40518>.391\), even if equality at the limiting attached height
  were admitted in a compact closure.
- It cannot be a private type-three leg, whose imaginary part exceeds
  \(-.019\).

These are the existing
[ordinary image bounds](../../../notes/research_mixed_cyclic_critical_height_bounds.md),
[open inheritance](../../../notes/research_mixed_open_local_factor_coverage.md),
and [endpoint rectangles](../../../notes/research_mixed_open_word_endpoint_rectangles.md).
The first type-four input also lies below the ordinary bound \(-.102\).
The next uniform domain should retain the correct ordinary or attached
rectangle at each incidence, rather than just the union of their height
intervals.

The single local constrained diagnostic with the stricter ordinary
height bounds \(h_4\ge-.102,h_3\ge-.065\) instead gave deficit
about \(-.012385895\) at the two right chord intersections. That
one local calculation is also not a proof of the trimmed domain.
It is not rerun by the script here.

Reproduce this one fixed point with:

```sh
python3 repro/diagnostics/2026-11-05-last-row-height-chords/diagnose.py
```

The result binds the helper used for the original-log numerical solve.
Small residuals and a positive floating deficit are diagnostic only;
no outward root enclosure or finite-kernel lower bound is claimed.
