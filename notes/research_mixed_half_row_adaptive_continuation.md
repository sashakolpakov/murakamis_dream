# One adaptive continuation of the weak half-row face

Research pilot design, 5 November 2026. This implements the single
change proposed in the
[saved performance diagnosis](../repro/diagnostics/2026-11-05-optimized-half-row-performance/README.md).
The original acceptance inequalities are unchanged. No new pilot
or uniform sign is asserted by this design.

## 1. Immutable accepted work

The input is the
[optimized 511-node partial record](../repro/diagnostics/2026-11-05-optimized-half-row-support-pilot/result-partial.json),
with SHA256
16e0ffe2e8b2ad6d33ecefbf34f1c6f01523d49102072d06ecf145ac20cec145.
It concerns only own flag zero, external flags \((1,1)\), first
input on its circle and second in its disk. Both conditional
orientations and the full target square were tested.

The exact input tree has 249 accepted leaves, resolved volume
\(535/262144\), and fourteen pending boxes. The continuation
reconstructs this entire tree and requires exact equality with the
saved frontier. It leaves all 511 existing nodes, rational witnesses
and target pairs unchanged. Their root/source evaluations and
proposals are not repeated. The input record, its proof and checker,
and all inherited dependencies are hash-bound.

Only pending boxes are processed. New leaves use the existing
[optimized-envelope rule](research_mixed_optimized_half_row_support.md),
with curvature \(c=14/5-2/2500000\), midpoint-only target gains,
and whole-cell gradients over the interval optimizer boxes.
The original phase, logarithmic lifts, both halfweights and the
coupled-root response remain unchanged.

## 2. An adaptive split is a coverage decision

Suppose a new box has a validated original root enclosure and finite
source bounds, but one or both orientations fail their upper test.
Evaluate both orientations before selecting a split. For parameter
halfwidth \(h_j\) and the envelope-gradient enclosure
\({\cal G}_{s,j}\) of orientation \(s\), use the scores
\[
 E_j=\max_{\substack{s\in\{0,1\}\\
                    \text{upper test for }s\text{ fails}}}
                  \bigl(h_j\sup|{\cal G}_{s,j}|\bigr),
                         \qquad j=0,1,2.
 \tag{1}
\]
Choose an axis with largest outward score, retaining the lower
index at a tie. The code uses interval upper endpoints, not
floating estimates. A rigorous trial point above the requested
threshold stops the pilot; it is not treated as a reason to split.

If the original root enclosure or finite source/gradient enclosures
are unavailable, use the original fallback \(j=\mathrm{depth}\bmod3\).
The choice affects efficiency only. Every accepted leaf still
passes the same strict bound \(V<-1/2000\).

For any exact rational parent box \(Q\) and any chosen axis \(j\),
the midpoint children satisfy
\[
        Q=Q_j^-\cup Q_j^+,\qquad
        \operatorname{vol}(Q_j^\pm)
                         =\tfrac12\operatorname{vol}(Q).
 \tag{2}
\]
Consequently arbitrary stored axes preserve complete coverage by
induction. A depth-\(d\) box still has volume \(2^{-d}\), regardless
of how often each axis has been chosen. The optimized-envelope
mean-value proof uses the actual three halfwidths and therefore
already applies to these nonuniform rectangular boxes.

The tree records each chosen axis explicitly. The original prefix
must retain its cyclic axes; appended split nodes may use any
integer axis in \(\{0,1,2\}\). A structural validator reconstructs
every box from those recorded axes, checks exact equality with the
reported frontier, and checks
\[
       \sum_{\text{accepted leaves}}\operatorname{vol}(Q)
       +\sum_{\text{pending boxes}}\operatorname{vol}(Q)=1.
 \tag{3}
\]
Any later numerical replay must follow the stored axes rather than
recompute the heuristic at another precision. It must revalidate
each leaf by its bound and rational witness. No numerical replay
or complete certificate is supplied by this bounded continuation.

## 3. Driver, limits and result interpretation

The new driver is
[continue_mixed_optimized_half_row_pilot.py](../experiments/continue_mixed_optimized_half_row_pilot.py).
Its source formulas are copied from the frozen optimized checker;
the only source-control change is to defer an inconclusive interval
return until both orientations and their scores have been evaluated.
The driver records the reason and scores for every adaptive split.

The pilot has fixed limits of **511 additional attempted nodes**,
60 seconds including setup, and depth 45. It has no option to
increase these limits or to start a twelve-face run. A root proposal
is made only for a newly visited pending box. Failed or nonfinite
proposals do not accept a cell.

Limits are checked between node evaluations. At a budget stop the
complete accepted prefix and pending frontier are saved. At a
point or depth stop, the attempted but uncommitted box is restored
to the frontier and recorded separately. This distinguishes the
number of attempted nodes from committed tree nodes without losing
any parameter region. Final provenance checks and serialization do
not resume the search.

The result reports both initial and additional counts, exact
resolved/pending volumes, recorded axis policies, and current
bindings. Finishing all pending boxes would prove only this single
ordinary face with its two orientations. An incomplete result gives
no uniform sign on its unresolved region. All older proofs,
checkers and records remain unchanged.
