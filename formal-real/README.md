# Concrete real and complex volume transfer

This optional Lean package realizes the elementary analytic interfaces of
[VolumeTransfer](../formal/VolumeLogic/VolumeTransfer.lean) using Mathlib's
complex numbers, complex modulus and real logarithm. It depends on the
existing Std-only package by the relative path `../formal`; its sources are
not copied. The ordinary Std-only check does not need this package or Mathlib.

## What is proved

[RealTransfer.lean](RealTransfer.lean) contains two definitions and fourteen
theorems, all in the namespace `VolumeLogic.RealModel`:

- `complexMagnitude` is the actual complex norm. Its nonnegativity,
  definiteness, multiplicativity and triangle inequality are proved.
- `realLogScale.value N x` is `Real.log x / (N : ℝ)`. Its monotonicity,
  product law and fixed-constant limit are proved.
- `eventually_physical_iff` and `real_rateLimit_iff` identify the existing
  epsilon-based level interface with ordinary `Filter.Tendsto` at `atTop`.
  Here a physical level is an integer `N ≥ 2`; removing the initial levels
  does not introduce a prime-level or parity restriction.
- `complex_hasRate_iff` and `complex_hasUpperRate_iff` give the corresponding
  concrete logarithmic rate statements. Eventual nonvanishing is kept
  separate from the totalized value of `Real.log 0`.
- The packet lemmas prove zero rate for unit phases, a complex amplitude
  tending to a nonzero limit, and any fixed real power of the level. They
  prove the rate of `exp(N S_N)` from the convergence of the finite complex
  actions `S_N`.

The main entry points are:

| Theorem | Conclusion and explicit inputs |
| --- | --- |
| `complex_invariant_rate_transfer` | From the exact eventual identity `K_N = u_N (G_N + E_N)`, zero normalization rate, leading rate `a`, and a strictly smaller upper rate for the **whole** remainder `E_N`, derive eventual `K_N ≠ 0` and its rate `a`. |
| `complex_volume_transfer` | From the same inputs and `2πa = volume`, derive the ordinary real limit `(2π/N) log ‖K_N‖ → volume`. |
| `complex_packet_volume_transfer` | Derive the leading rate from the actual packet `N^k a_N exp(N S_N)`, where `k` is any fixed real number, `a_N → a ≠ 0` and `S_N → A`. Restore a unit framing character, use a strict whole-remainder upper rate below `Re A`, and conclude the volume limit from `2π Re A = volume`. |

Thus the last theorem proves the packet's logarithmic rate rather than
assuming it. The power `k` includes half-integral Gaussian powers. A relative
correction tending to one can remain inside `a_N`. The more general
`complex_volume_transfer` permits a normalization of rate zero even when its
modulus is not one.

The packet theorem assumes a **common all-level** nonzero amplitude limit.
If the written expansion instead has distinct even and odd amplitudes, that
particular hypothesis has not been established. Prove the two parity rates
and combine them with the existing level-scope union lemmas before applying
the general transfer theorem. The concrete norm and logarithm interfaces
themselves have no parity restriction.

These are conditional analytic transfer theorems, not a construction of the
Kashaev or ADO invariant. The exact original source identity, convergence of
the nonzero packet coefficient and finite action, a strict bound for the
entire complementary remainder, and the geometric action-volume equality
remain explicit application inputs. This package does not formalize the
saddle analysis or hyperbolic gluing that supplies those inputs.

## Pinned dependencies

- Lean: `leanprover/lean4:v4.32.2`.
- Mathlib: `905b95818eb32af7874a58b427f50c1711a5e96c`.
- [lake-manifest.json](lake-manifest.json) fixes all nine Git dependencies,
  including Mathlib's transitive packages.
- `volumeLogic` is the existing `../formal` path dependency.

The checker validates the complete expected dependency set and every URL and
revision. It also checks each materialized Git checkout's `HEAD` and requires
its tracked sources to be clean. Local cache symlinks may be used inside the
ignored `.lake/` directory; no machine-specific path is part of the package.

## Fresh-checkout setup

Use Git, Python 3.11 or newer, and Elan's `lake` command. Run the following
from the repository root. The first command installs the pinned Lean release
if it is not already present.

```sh
elan toolchain install leanprover/lean4:v4.32.2
cd formal-real
MATHLIB_NO_CACHE_ON_UPDATE=1 lake update volumeLogic mathlib
lake exe cache get \
  Mathlib.Analysis.Complex.Basic \
  Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic \
  Mathlib.Analysis.SpecialFunctions.Pow.Real \
  Mathlib.Analysis.SpecialFunctions.Log.Basic \
  Mathlib.Tactic.Linarith
cd ..
python3 repro/check_concrete_limits.py
```

The environment variable suppresses Mathlib's automatic whole-library cache
download during dependency setup. The explicit `cache get` requests only
the listed modules and their transitive imports, as supported by this pinned
Mathlib's [cache documentation](https://github.com/leanprover-community/mathlib4/blob/905b95818eb32af7874a58b427f50c1711a5e96c/Cache/README.md).
The replay then rejects any dependency drift. Do not update the pins merely
to make a different installed Mathlib version pass.

This remains an optional, heavier check. The full compatible Mathlib cache
used during development occupied about 5.83 GiB, shared locally; that is not
a measurement of the smaller selected download. Cold setup time and the
selected cache size have not been measured. With that cache present, the
bridge itself compiled in seconds. No cache download is part of routine
replay, and a missing dependency produces setup instructions.

## Replay and audit record

From the repository root:

```sh
python3 repro/check_concrete_limits.py --output concrete-limits-output
```

The output directory is caller-chosen. Omit `--output` for a temporary check
whose logs are removed afterward. `--lake` can select a Lake executable;
the executed Lean version must still match the pin.

The checker rebuilds the Std-only path dependency, compiles
`RealTransfer.lean`, and runs [AxiomAudit.lean](AxiomAudit.lean). Every new
definition and theorem must appear exactly once in the audit. Only Lean's
standard foundational axioms `propext`, `Classical.choice` and `Quot.sound`
are permitted; placeholders and additional axioms fail the check.

`summary.json` records every declaration, its axioms, all dependency pins,
and the SHA-256 hashes of the optional package, checker and Std-only sources.
It contains relative paths and omits timestamps so identical inputs produce
the same summary. Eight negative controls check altered pins, missing or
duplicate dependencies, an absolute local dependency, incomplete or
duplicate declaration audits, and an unexpected logical axiom. A failed run
removes any old success summary in its output directory.

The optional count is **two definitions and fourteen theorems**, separate
from the Std-only theorem count. The audit checks these proofs and the
listed dependency pins; it does not certify that a particular knot family
satisfies the remaining written analytic and geometric hypotheses.
