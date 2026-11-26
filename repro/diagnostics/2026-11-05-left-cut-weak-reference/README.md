# One auxiliary left-cut investigation

The two diagnostic drivers use only the own-four/external-three-four
family. diagnose.py reads the 406 old accepted leaves in that family
to select a weak midpoint, then optimizes only its two horizontal
target coordinates. It revalidates that saved original-log witness;
it proposes no root and finds a negative excess near -0.0018381.

local_variation.py performs one local two-angle optimization from
that midpoint, with the target coordinates still optimized by strict
scalar concavity. It takes seven iterations and 24 objective calls.
It proposes and validates one final original-log point witness,
finding a positive excess near 0.00137712. The external reference
is not known to occur in any actual finite open word.

Both outputs and drivers are preserved. Their floating searches are
not mathematical acceptance conditions. The separate focused checker
experiments/check_mixed_left_cut_independent_reference_obstruction.py
uses only the final fixed rational angles, targets, and saved point
witness. It proves the strict excess greater than 1/1000, and its
saved replay has no proposals or optimization. The corresponding
research note states the narrow obstruction and its limitations.

No old source record, root cover, or accepted proof was modified.
