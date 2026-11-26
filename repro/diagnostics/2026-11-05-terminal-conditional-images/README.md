# Terminal conditional source at existing endpoint proposals

This is a bounded diagnostic, not a certificate. The driver reads the
132 archived open-word endpoint proposals, with no new root solve,
optimization, or word search. It evaluates the original conditional
phase at (a,e(a)) with critical row t(a).

The old source inputs already prove curvature and left-tail monotonicity
on these domains. The outstanding tests are the two cut gaps, the
full revived-last-row gap, both entire horizontal aliases, and the
right-tail quartic/sextic. This diagnostic samples those quantities
only. The phase input roots are floating proposals, not validated
roots for this new comparison.

Across the 132 proposals the smallest sampled left and right cut gaps
are approximately 0.0265102 and 0.0426267; the revived-last-row gap is
approximately 0.0437917. The two alias grids have gap at least 0.7430649,
and the sampled tail polynomial is at most 0.1585654. These figures
are evidence for a bounded outward test, not a uniform sign statement.
The two old one-vertex proposals are also displayed for comparison;
the one-cap source at length one has no conditional factor and needs
no such new source family.

The result.json file binds the original proposal record, source/domain
notes, and this driver. Both level parities, original chirp, and both
revived endpoint growth factors are retained in the formulas.

Run from the repository root:

    python3 repro/diagnostics/2026-11-05-terminal-conditional-images/diagnose.py
