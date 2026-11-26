# Short right-interface connectors: diagnostic only

These are bounded floating calculations at two already preserved
alternating-reference singleton configurations. They are not interval
certificates, complete parameter covers, or proofs of an interface sign.
No growing family of words is searched.

`diagnose.py` solves the original alternating critical reference and
checks its cyclic gradient numerically. It then retains the complete
raw row rate on both right-incident edges: both Fourier alternatives,
the first-argument chirp, all row fractions from zero to one, and all
selected factors. The row maxima use a scalar grid with local searches.
Every allowed selection of the free symbols in depth-three, four and
five incoming and exit paths is included. The two endpoint
configurations are the old exact endpoint witness and its previously
saved strict-interior perturbation; there is no outer-state optimizer.

The local helper `phase_helpers.py` is copied byte-identically from
`../2026-11-05-seam-attenuation-vertices/phase_helpers.py`. It uses
floating cotangent roots and the original calibrated phase formulas.
No `/tmp` dependency is used. This root selection is not an independent
outward certificate of the reference or its phase.

For theta=1/2, `results.json` records the quantities

```
raw + A_h(left exit) - A_h(right entry) - theta*endpoint_occupation/2
raw - E_h(left exit) - A_h(right entry) - theta*endpoint_occupation/2
```

and the second expression minus the outgoing `(1-theta)*Psi` reserve.
The states have at least two A symbols on either side of the R singleton,
so the displayed endpoint occupation halves are available. The first
expression is a difference of lower optimizer trials, not an upper
bound. The second would become an upper bound if its raw maximum and
explicit connector values were rigorously evaluated; the current
arithmetic is floating. Increasing h from three to five does not repair
the positive independent-entry/exit proxy: it stays approximately
`+0.06321`. The same-incoming trial is approximately `-0.18233`.

`diagnose_synchronized_upper.py` tests a different finite expression:

```
B(v) = max_u [ C_3(u,v) - C_3(u,baseline) ].
```

The analytic deduction `H(v) <= B(v)` is proved in
`../../../notes/research_mixed_synchronized_incoming_bounds.md`.
Only two predecessor reals and one selection matter at these particular
terminal states. All choices of that selection are retained; the
predecessor maximum still uses a bounded floating search, so its recorded
value is a lower trial for B, not a certified upper bound for H.
The observed value near `-0.094676` leaves the adjusted diagnostic near
`-0.18204`. This is a reason to investigate the finite bound, not a
universal conclusion.

`summarize.py` evaluates the separate, proved acute formula from
Proposition 2 of that note at the same floating reference. Its value is
about `-0.086088`. The formula itself bounds every admitted predecessor
history; the decimal is still diagnostic because no outward arithmetic
was used here. `summary.json` retains this distinction explicitly.

All new output is local to this directory. `manifest.json` records byte
hashes of the drivers, helpers, results and logs. The original archived
counterexample and all completed theorem/certificate files are unchanged.
