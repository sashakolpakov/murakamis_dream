# Low-terminal right-interface diagnostics

These are bounded floating diagnostics, not certificates. They test the proved
constant-surplus incoming upper bound against a literal three-step incoming
lower value at the opposite endpoint. Ten fixed actual periodic references of
length at most three are used; there is no growing-word search. Every allowed
right-neighbor selection is included. Right angles are fixed at one half by the
separate complete raw-row theorem. The unique lower-row maximum is located by
bisection, without outward rounding.

`diagnose.py` varies the low endpoint over `[.00001,.1]` and the other two real
coordinates over `[.1,.5]`. Its largest trial is `+.2151015768423961`, in the
homogeneous type-four case at the low end `.00001`. This shows that the
constant-surplus relaxation by itself is too weak near zero. It is not a
counterexample to a finite kernel bound, the exact incoming potential, or the
volume asymptotic.

The exact transport theorem in
[`research_mixed_exact_low_transport.md`](../../../notes/research_mixed_exact_low_transport.md)
retains the discarded low-coordinate dependence and proves that the original
common-potential expression is maximized at `.1`. It also removes all deep-low
coordinates from the complete cyclic mixed raw/coherent envelope. Accordingly,
`diagnose_endpoint.py` performs one new bounded test with the low endpoint
fixed at `.1`. Its largest trial is `+.007472804861398806`, again homogeneous
four, with the opposite endpoint `.5` and its inner halo `.1`. Thus this
remaining coarse incoming upper bound is not sufficient even on the reduced
domain. Neither optimizer is used as an upper enclosure.

The exact transport does not claim that the coarse constant-surplus expression
itself is monotone. No auxiliary connector is inserted as a physical source
factor. The scripts retain both true Fourier alternatives, the original chirp,
actual reference tangents and the full raw row envelope. They conservatively
discard the first terminal symbol's occupation and the additional AA endpoint
occupation share, so these formulas are sufficient upper proxies, not claimed
sharp values.

Reproduce from the repository root:

```sh
python3 repro/diagnostics/2026-11-05-low-terminal-right-interfaces/diagnose.py
python3 repro/diagnostics/2026-11-05-low-terminal-right-interfaces/diagnose_endpoint.py
```

Both scripts use the adjacent archived `phase_helpers.py` by a repository-local
path. No `/tmp` import is required. `manifest.json` binds these diagnostic files
and their helper; it does not promote their results to proved source bounds.

## One fixed endpoint follow-up

`diagnose_fixed_worst.py` tests only the preserved homogeneous-four worst
endpoint, without another outer-state search. The literal right incoming
maximum trials at depths three, four and five all equal
`-.09540713683928842` to displayed precision. Thus increasing that depth does
not remove the positive coarse proxy. The explicit acute synchronized upper
from the existing written theorem, evaluated in floating arithmetic, gives an
adjusted value `-.14535813818781707`. A bounded two-variable synchronized-tail
trial gives `-.18788976443593602`; that optimized value is not an upper bound.
The first terminal symbol in this experiment is its reference real part, as
required by that particular acute specialization. This test does not extend it
to arbitrary first terminal symbols. Its runtime was about 2.9 seconds.

```sh
python3 repro/diagnostics/2026-11-05-low-terminal-right-interfaces/diagnose_fixed_worst.py
```
