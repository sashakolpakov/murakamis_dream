# The remaining real terminal cuts and entropy comparison

The fixed direct-cut calculation proves six uniform negative comparisons at
\(H=1/100\) on the canonical actual input domain \(K_4\). Each has raw gap
greater than \(1/160\):

| Terminal type | Original profile | Alternatives covered |
|---|---|---|
| Three | Real transform right cut | Factorial and forced |
| Three | Physical entropy | Factorial and forced |
| Four | Real transform left cut | Factorial and forced |

Four of these comparisons were unresolved after the
[terminal-side update](research_mixed_terminal_terminal_side_plane_outcome.md).
The other two strengthen already proved signs. The six comparisons together
with that update cover all 36 real-face/entropy alternatives across the two
terminal types. Their common raw gap is \(1/2600\); the limiting comparison
remains the type-four factorial entropy profile.

The independent saved-data audit and exact 36-comparison merge completed
successfully. All 563 input bindings remained unchanged; every comparison
has the strict gap asserted above. The completed analytic run and all
previous records are unchanged.

## Why the direct comparison closes the cuts

For a real transform cut \(\tau\), its dependence on the selected leg separates:
\[
T_\tau(a;y)=\Re\Xi_\tau(a)+E(y),\qquad
\Xi_\tau(a)=g(\tau+a)-g(a)+2\pi i\tau a.
\tag{1}
\]
The entropy profile has the same dependence with \(\tau=1/2\).
The original source estimate at the actual reference \(a_*\) supplies a
uniform upper \(U\) for all private or entropy targets \(y\). Consequently
\[
T_\tau(a;y)
\le \Re P_\epsilon(a_*)+U+
       \Re\{\Xi_\tau(a)-\Xi_\tau(a_*)\}.
\tag{2}
\]
This eliminates those targets while retaining their original domains and
source normalization. It neither places a real cut at the main height nor
assumes the cut is stationary.

The [direct-cut theorem](research_mixed_terminal_real_transform_cut_budget.md)
retains the exact height correction and the changed selected force in (2).
The common incoming marginal remains the original complex marginal.
The terminal-index scalar gain disappears because the terminal targets have
been eliminated by the original source bound. Two costs remain: coefficient
2 on the ordinary index and coefficient
\[
\nu+\frac{13}{6}\quad(\tau=1/2),\qquad
\nu+\frac{11}{10}\quad(\tau=3/20)
\tag{3}
\]
on the selected leg, where \(\nu=1\) and \(0\) denote the factorial and forced
alternatives. Both alternatives keep the full selected target
\(P=[.22,.45]\). No new private action or optimizing reference is needed.

## Completed finite calculation

The [fixed protocol](research_mixed_terminal_real_transform_cut_protocol.md)
uses exactly the two cases \((\epsilon,\tau)=(0,1/2)\) and \((1,3/20)\),
with the already certified correlated reference families. The
[completed record](../repro/results/research-mixed-terminal-real-transform-cut-budget.json.gz)
has SHA-256
6f526c7a5b9c5f0f3b23a23a79ada4c5670966b7518959600e0a02b1caeea8cb.
All 528 input bindings were unchanged.

The run retained 32 new height-slab cotangent enclosures, two center
cotangents, four sines, two logarithms, 192 force vertices, and 384 scalar
gains with independent exact witness checks. It made no root, private-action,
source-replay, subdivision, or retry calls. The existing \(a\) and \(s+a\)
cotangent enclosures and their exact source associations were reused.

All six joined upper bounds are strictly less than \(-1/160\). The smallest
new gap is approximately \(0.006497258983331\), attained by the type-four
real left cut in the factorial alternative. The earlier positive upper
bounds remain in their original records; the direct comparisons supersede
them without interpreting them as counterexamples.

The new [saved-record checker](../experiments/check_mixed_terminal_real_transform_cut_record.py)
reconstructs the literal difference \(D_\tau\), its derivatives, the signed
height product, every slab support and integral weight, all 192 force
vertices, all 384 saved cubic witnesses, and the six source sums using exact
rational arithmetic. Original elementary enclosures are inherited from the
reviewed run. The only imported checker is the frozen stdlib-only cubic
witness checker; no gain generator or analytic evaluator is called.

The completed
[compact audit](../repro/results/research-mixed-terminal-real-transform-cut-saved-audit.json)
also merges the six bounds with the preceding audited 36-row inventory.
It retains every earlier comparison, including positive plane bounds and the
separate private-left theorem. Its SHA-256 is
29d1edc0a516e44ceac16f3c9fe9868bfee0e8c3268134819f05bbd21067306e.
It verifies 36 paid comparisons and no unresolved ones. The largest new
direct-cut upper, rounded upward to twelve decimal places, is
\(-0.006497258983\). Reproduction uses a fresh output path:

    python3 experiments/check_mixed_terminal_real_transform_cut_record.py \
      --output /tmp/terminal-real-transform-cut-audit-fresh.json

## Complete local consequence and its scope

The preceding audit already proves 32 of the 36 real-face/entropy comparisons
with gap greater than \(1/2600\). The new six comparisons include all four
missing ones, and \(1/160>1/2600\). Thus all 36 have common raw gap
\[
\delta=\frac1{2600}.
\tag{4}
\]
The independently proved main, penalized-alias, and constant profiles have
larger reserves. The private-left face keeps its separate direct transfer
with gap \(51/20000\); its plane bounds are not used to establish its sign.

The [complete local kernel theorem](research_mixed_terminal_uniform_kernel_completion.md)
assembles these comparisons with the original terminal envelope and
ordinary-label domination. It gives raw gap \(1/2600\), and finite-source
rate gap \(1/5200\) for sufficiently large levels, for the original selected
ordinary-plus-terminal kernel on the actual canonical \(K_4\) family, with
unselected incoming leg. The original integer weight, modulus halfweight,
complex incoming marginal, independent plateau targets, ordinary-color
neighborhoods and fixed jets, and both parities are retained.

The containing phase domain \(D_4\) does not enlarge the finite-source
domain \(K_4\). This is a uniform local kernel comparison, not a whole-word
asymptotic, an outside-color estimate, or a finite-exceptions knot theorem.
