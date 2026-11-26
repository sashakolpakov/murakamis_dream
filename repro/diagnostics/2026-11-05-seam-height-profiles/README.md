# Applying the proved height profiles to saved seam witnesses

This directory evaluates only the 29 witnesses already archived in
`../2026-11-05-seam-actual-plane/`. It runs no optimization or interval cover.
The exact profile knots come from the current canonical
`research-mixed-height-resolved-seam-sources.json` extraction record.
The output binds that record, both prior diagnostic inputs, and this driver.

At the previously largest positive A3 witness, the physical heights are
approximately `(9.33e-9, -1.87e-18)`. The source ceiling decreases from
`.963539` to `.90227196394`. With the actual geometric plane, full fixed
collar cost and unchanged endpoint occupation, the comparison changes from
`+.00943229006` to `-.05183474600`. All 29 saved A3 values become negative;
this is the largest of those saved values.

At the same single witness, the previously computed A4/A5 estimates become
`-.06704800147` and `-.06735662740`. No incoming optimization was repeated.

These are floating substitutions at a finite set of saved points. They give
no upper bound over physical parameters or actual references. A3 is not the
incoming supremum or a proved subaction. A4/A5 remain differences of lower
maximum estimates and cannot be interpreted as rigorous upper bounds. The
height-profile theorem is established separately; these potential comparisons
are diagnostic only.

The driver refuses to overwrite its result. To reproduce in a separate copy,
remove or redirect only that copy's `saved-case-evaluation.json` output.
