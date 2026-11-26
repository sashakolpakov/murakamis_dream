# A bounded two-edge reset comparison

This tests a sufficient allowance for the pattern E--P--U--R and its
reverse, where E is early, P is in [.22,.45], U is in [.45,.5],
and the R angle has already been set to .5 in the complete mixed raw
upper envelope. This last comparison is legitimate only with the global
right-angle reduction and the original raw labels retained.

Write the P reference as a and the U reference as b. At early slow
fraction ell in [0,1/6], the literal P height is ell*Im(a) when
unselected and 6*ell*.014 when selected. The U height is its prescribed
coefficient times 400(.5-t)^2. These two heights are correlated with
the original reference and the same early coordinate. The tested bound
is

    coherent_PU_defect + complete_raw_UR_defect - q*(Im a)^2 <= 0,

where q=11/2 for E--P--U--R and q=151/20 for R--U--P--E.
The coherent term keeps each selected half-correction
max(Re g(z),-2 pi Im z)/2. The raw term keeps all original rows,
the first-argument chirp, both true Fourier alternatives and the
selected monomial. The full row theorem reduces its maximum at R=.5
to the unique lower-half row; the script finds that row by scalar
bisection and checks that it lies in (.2,.4).

Original critical stationarity cancels the target-U coefficient in
the sum of the two supporting planes. At fixed references and target
reals, branchwise height convexity reduces ell to 0 or 1/6. The
remaining P/U real coordinates are only sampled here, not bounded.

The run uses the sixteen length-four type words, both orientations
and all permitted P/U selections. It checks a fixed grid with at most
seven P reals, three U reals and the two ell endpoints. Actual reference
proposals solve the original cyclic gradients numerically. No real
target optimization, outward arithmetic or parameter cover is used.
The recorded maxima are lower trials for a supremum; their signs do
not prove or disprove the desired uniform comparison.

Run:

    python3 repro/diagnostics/2026-11-05-early-plateau-taper-right/probe.py

Existing frozen proof and source artifacts are only read. The result
records all helper and proof hashes and retains the exact two-edge
source allocation.

## Independent height-corner and saved-cover exploration

`height_corners.py` relaxes the U height to the two endpoints zero and
its prescribed coefficient, independently of its real angle. Its fixed
6,048-point grid has largest value approximately -0.056639. This is
still a floating diagnostic, not a uniform upper bound.

`saved_zero_support.py --restrict-U --zero-type-three` and
`direct-zero-support.json` re-evaluate the original complete 512
reference domains and 5,546 saved cells, with no new subdivision.
The old type-four zero-height tangents are restricted to [.45,.5].
For type three, two rational row trials at y=.45, together with old
trials, bound the zero-height profile by exact concavity. The necessary
full-reset debit is included; for actual P4-U3-R triples, the existing
100/101 conditioned height bounds cap that debit separately before
the reference maximum principle. No reference image is clipped.
All eight typed/orientation ceilings are below -0.00180220.

`saved_selected_upper.py` and `saved-selected-upper.json` re-evaluate
the old selected/reset 128 reference products and 1,023 root witnesses
with the target square enlarged to [.22,.5]^2. The constrained quadratic
upper bound is below -0.00633612. No optimizer, root proposal or new
reference partition is used. These extractions have not been promoted
to a theorem or incorporated into a proof dependency. Their original
source-domain and full branch implications would require a dedicated
review before such use.

The intermediate `saved-zero-support.json` and
`restricted-zero-support.json` record earlier, looser bounds. Their
script hashes refer to development revisions; they are historical
diagnostics, not current replay inputs. The original first script is
preserved as `saved_zero_support_original.py`. Positive intermediate
upper ceilings are inconclusive and are not counterexamples.

The final research route instead uses the completed mixed
selected-height removal and unselected clamping theorems. The separate
[global upper-removal proof](../../../notes/research_mixed_nonlow_upper_transition_removal.md)
derives the actual E-P-U-R allowance and removes all upper coordinates
from the nonlow mixed domain without relying on any diagnostic here.
