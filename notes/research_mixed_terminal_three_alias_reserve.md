# An exact saved alias reserve for terminal type three

Research extraction design, 5 November 2026. This strengthens only the
reserve in the completed [alias certificate](research_mixed_terminal_three_alias_certificate.md).
No root, target, contour, parameter box or source bound is reevaluated.

The completed [author](../repro/results/research-mixed-terminal-three-aliases-attempt01.json)
has SHA256 fc04d56f297524fc252dd0e0f131db11000d7490ec77a3b5300811cebb8e41cf.
Its independent 320-bit [replay](../repro/results/research-mixed-terminal-three-aliases-replay.json)
has SHA256 3b2b017023020d8ea2dce6ff7e5a429f87a0871a339467a2f0734454af4523f5.

For each of 3,347 original endpoint cells and twelve alias families, the
replay stores a maximum_upper field in its replay_summaries list. The
replay code takes the maximum of outward upper endpoints returned by
check_face over all source leaves in that job. The printed Arb ball
still encloses that maximum. A display \([m\mathbin{+/-}r]\) therefore
gives the exact rational upper bound \(m+r\), interpreting finite
decimal strings literally.

The twelve families are the eight single aliases
\((\pm.12,0),(\pm.12,h_u^*),(0,\pm.12),(h_t^*,\pm.12)\)
and four double aliases \((\pm.12,\pm.12)\), with original penalties
and all free real targets unchanged. The bare defect is measured
against \(B_0\).

**Extraction proposition.** If the accompanying
[exact checker](../experiments/check_mixed_terminal_three_alias_reserve.py)
passes, all twelve inequalities have the stronger gap \(1/10\), on
both entire original input disks.

The checker binds both immutable records and their current dependencies,
checks literal tree/target/family identity, and checks all 40,164 saved
upper bounds against \(-1/10\) using exact fractions. It checks summary
order and source-leaf counts. It imports no source certifier and uses
no floating arithmetic. The largest exact upper and its job are saved.

*Proof.* The completed replay establishes that each saved maximum
bounds its full source family. The decoded rational upper is no smaller
than that maximum. Its strict comparison supplies the stronger reserve.
Coverage, branches, allocation and scope remain those of the completed
certificate. No inference is made from a rounded global summary alone.

Before this separate checker is executed, the extraction proposition
is conditional. It does not assert a new source computation.

