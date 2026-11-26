# Raising left coordinates beside a right coordinate: diagnostic only

This bounded calculation tests a proposed increase of the complete
raw/coherent upper rate as nonright coordinates below a level in
`[.12,.22]` are raised to that level. It uses four fixed actual references,
right angles `.5`, `.7`, `.9`, and two selection patterns, for 72 cases.
The original hybrid heights are recomputed at every level. The two
right-incident blocks use a 2,049-point row grid; their recorded maxima
are floating lower trials, not certified upper bounds.

The minimum sampled increments are positive at right angles `.5` and
`.7`, but negative at `.9`. Consequently this experiment does not justify
minimum transport at arbitrary right angles. The later analytic right-angle
reduction in
[the research proof](../../../notes/research_mixed_complex_right_row_reduction.md)
allows a different approach: first bound every right angle by `.5`, then
study transport of that upper envelope. The positive samples at `.5`
remain evidence only; no continuous derivative sign is proved here.

Run from the repository root:

```sh
python3 repro/diagnostics/2026-11-05-right-minimum-transport/diagnose.py
```

The original input file has been copied byte for byte into
`reference_inputs.json`. The driver has no temporary-file dependency.
The saved numerical output predates this path-only change; its dependency
hashes have been checked against the local copies, and its numerical
values have not been altered. A new invocation records the current
driver and repository-relative input paths.
