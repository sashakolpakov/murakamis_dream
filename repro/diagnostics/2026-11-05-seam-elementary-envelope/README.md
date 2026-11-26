# Preliminary test of the general-angle comparison

`diagnose.py` evaluates an explicit upper bound for the cost of replacing
one isolated near-zero coordinate by its geometric reference. It retains
the physical source profiles, the change in both adjoining noncollar edges,
and every permitted endpoint selection. Physical and repaired heights are
enlarged to triangles; acute argument bounds replace the phase gradients.
Concavity supplies a lower bound for the real phase from the previously
certified corner values.

`result.json` records a floating grid with the middle height's actual cutoff
bound. `constant-middle-result.json` records the more conservative test that
discards that cutoff. Both tests found the same worst value, approximately
−0.00331316. Neither grid establishes a uniform inequality.

The subsequent proof uses exact rational Bernstein coefficients on the
whole domain, with no grid premise. Its source and certificate are
[the general-angle note](../../../notes/research_mixed_general_angle_seam_replacement.md)
and [the exact checker](../../../experiments/check_mixed_general_angle_seam_replacement.py).

Run the original floating test with:

```sh
python3 repro/diagnostics/2026-11-05-seam-elementary-envelope/diagnose.py
```

Run the constant-middle variant with:

```sh
python3 repro/diagnostics/2026-11-05-seam-elementary-envelope/diagnose.py --constant-middle
```

It writes `constant-middle-result.json`. The exact checker directly
implements this more conservative comparison.
