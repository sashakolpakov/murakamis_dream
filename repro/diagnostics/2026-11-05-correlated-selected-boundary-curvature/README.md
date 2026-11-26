# Correlated selected-boundary curvature: one bounded diagnostic

This is floating exploratory evidence only. It proves neither an interval
curvature bound nor that a necessarily feasible input is realized by an open
word. No source certifier is imported or replayed.

The fixed budget is 25 prescribed inputs: 20 next-three inputs on
`{.31,.34,.37,.40} × {−.05,−.025,0,.025,.05}`, followed by five next-four
inputs `(.28,−.065),(.295,−.055),(.31,−.045),(.325,−.035),(.34,−.025)`.
An input rejected by any filter is retained in the record and never replaced.

Each original first-four endpoint root starts from the containing leaf of
the saved, fully replayed original endpoint map. At most 12 local Newton
steps stay inside that inherited witness disk. Its original logarithmic
residual and canonical inner branch are checked numerically. The reconstructed
ordinary output and next external input must satisfy their original zero-lift
equations and the typed necessary domains. The rational parametrization from
the endpoint auxiliary exponential is an independent consistency check.

For each retained reference, the eight fixed height nodes are seven equally
spaced points from its actual attached height to zero, followed by `.01`. The four real variables stay in the original horizontal
box. A bounded Newton/KKT continuation uses analytic first and second
derivatives, the actual fixed index heights, and the original outgoing
tangent. Each height permits at most 40 iterations and 20 backtracks per
iteration; the whole program has a 120-second time budget. It does not
assert a global optimizer from a small KKT residual. Both the matrix and
tree-Schur expressions for the effective curvature are recorded/compared.

The program refuses to overwrite `result.json`; there is no automatic retry
or continuation. Its output binds the script and all mathematical/reference
inputs and records every filter rejection and incomplete optimization.

The proposed bound is `K_eff/pi <= 6`; a numerical pass at these points
alone cannot establish it on a reference domain or a height interval.

## Sole execution

The prescribed run completed on 5 November 2026 in about 0.13 seconds.
All 25 inputs were processed, with no replacement or retry. Twenty-two
failed one or more necessary filters. The remaining three produced all
24 requested KKT candidates, each strictly inside the original box.
There was no optimizer failure, active face, or nonpositive computed
Hessian. The largest projected-gradient residual was about `9.8e-13`;
the smallest computed eigenvalue of `A/pi` was about `0.75791`.
These are floating values, not outward bounds.

| Next type | Input `s2` | Original first height | Initial `K/pi` | Largest sampled `K/pi` |
|---|---|---:|---:|---:|
| 3 | `.37 − .025i` | `−.05095936135` | `4.510491329` | `4.919252634` |
| 3 | `.37` | `−.05642656521` | `4.383149109` | `4.833998559` |
| 4 | `.31 − .045i` | `−.06734541517` | `3.865256303` | `4.656435956` |

For all three sampled paths the curvature increased at each recorded
height, attaining its sampled maximum at `.01`. The recorded real
private coordinate `e` and outgoing coordinate `b` increased, whereas
`s`, `z`, and `s+z` decreased. No monotonicity between samples follows.
At the final height the optimized factorial-rate excesses over the
original reference were approximately `−.03597005`, `−.03176064`, and
`−.02450558`, respectively. The forced branch was not optimized.

The surviving next-external coordinates lie respectively in
`O4 ∩ A4`, `O3 ∩ A3`, and `O3`. This verifies only the prescribed
necessary local filters. No sample is asserted to be realized by an
entire open word. In particular these three paths neither cover the
feasible reference region nor reach the proved worst first-height
floors. The observed margins support the correlated curvature target
as a plausible next certificate, without establishing its truth.

The exact records are:

* `diagnose.py`: SHA256 `0a29325198d59f544ca61aa93b620f85555d7810a139862677f36a56b46534af`.
* `result.json`: SHA256 `74e5504e08b5abd9e3ae16e7636f3ca2be7a9a3ceef44d255c1a8b3c04c2f41e`.

All eight input hashes and the script hash matched after execution and
again during the static result audit. The working envelope note is
also preserved verbatim under `inputs/`, with its original
`aff8665e…` binding recorded in `input_snapshots.json`; later analytic
additions to the repository copy do not alter that historical input.
No second numerical run, higher-precision claim, or parameter-cover
computation was performed for this diagnostic.
