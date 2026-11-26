# A saved alias reserve for the complete terminal-four comparison

Research extraction design, 5 November 2026. The completed terminal-four
replay contains stronger alias bounds than its requested common gap.
This note specifies an exact extraction of that reserve. It changes no
source estimate or geometric domain.

The author record is
[the coupled terminal continuation](../repro/results/research-mixed-terminal-four-source-stage4-attempt01.json),
SHA256 `e3651c4ec370625b6be4b8a93ab000730926c33d4062162c7188d0712d56f5d3`.
Its completed 320-bit
[saved replay](../repro/results/research-mixed-terminal-four-source-replay.json)
has SHA256 `3b38c1f62ee63f537db1ec2209bb9e278cc273b477dec03b7e0f15fb7f57cf79`.
Both retain all 40,131 jobs: twenty-one comparison families on each of
1,911 original own-four endpoint cells.

Only families 8 through 19, numbered from zero, are used here. They
are the four transform single aliases, four private single aliases,
and four double aliases in the
[reduced-current theorem](research_mixed_terminal_four_reduced_currents.md).
Their penalties, free real target intervals, original reference action
and bare supporting plane are unchanged.

**Extraction proposition.** If the accompanying
[exact checker](../experiments/check_mixed_terminal_four_alias_reserve.py)
passes, each of these twelve alias comparisons has strict bare gap
\(1/10\) at every required actual reference of every fixed word of
length at least two.

*Proof.* The completed replay checks every source leaf under the
arithmetic rule that originally accepted it. For a job containing
source leaves, its `maximum_upper` encloses the maximum of their
outward upper bounds. In particular a printed ball with finite
decimal midpoint \(m\) and radius \(r\) gives the exact rational
upper bound \(m+r\). The checker verifies \(m+r<-1/10\).

Some jobs contain only geometric exclusions. Their maximum is null;
this is not a numerical source bound. The completed replay proves
that their original reference rectangles contain no required actual
reference. The checker verifies the absence of source leaves and
the presence of exclusion leaves. It never assigns a numerical
maximum to such a job. More generally, exclusions inside a job with
source leaves remove no actual reference, so the saved source maximum
bounds every required point in that job.

The checker verifies literal equality of the complete author and
replay trees, the summary ordering, all source and exclusion leaf
counts, and all twelve families on all 1,911 cells. Every input and
its recorded current dependencies are hash-bound. Coverage and the
validity of each exclusion are supplied by the completed replay,
not inferred from a missing maximum. Thus every actual reference is
either covered by the stronger source bound or excluded as impossible.

The conclusion is on the necessary actual-reference set of the
[coupled continuation](research_mixed_terminal_four_coupled_source_continuation.md).
It does not assert a stronger comparison on discarded independent
inputs. The maximum is relative to the original bare horizontal plane;
an incoming Fourier weight must still be allocated separately.

The checker uses only exact fractions and saved records. It imports
no source module, proposes no root, subdivides no box and evaluates
no phase. The proposition is conditional until that extraction passes.
