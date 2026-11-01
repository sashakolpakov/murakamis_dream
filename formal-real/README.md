# Concrete analytic transfer and weighted graph energy

This optional Lean package realizes the elementary analytic interfaces of
[VolumeTransfer](../formal/VolumeLogic/VolumeTransfer.lean) using Mathlib's
complex numbers, complex modulus and real logarithm. It depends on the
existing Std-only package by the relative path `../formal`; its sources are
not copied. The ordinary Std-only check does not need this package or Mathlib.
The package also proves the real finite quadratic-form implication used in
the circle-pattern Hessian argument.

## What is proved

[RealTransfer.lean](RealTransfer.lean) contains two definitions and twenty-two
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
| `complex_residue_packet_volume_transfer` | Allow separate nonzero amplitude limits and complex action limits on every residue class modulo a fixed positive integer `p`. If all limiting actions have the same real part, derive the full integer-level volume limit under the same exact-source, whole-remainder and geometry hypotheses. |
| `complex_parity_packet_volume_transfer` | Give the preceding conclusion directly from the actual subsequences `a_(2n)`, `a_(2n+1)`, `S_(2n)` and `S_(2n+1)`, with independently specified limits. |

Thus the last theorem proves the packet's logarithmic rate rather than
assuming it. The power `k` includes half-integral Gaussian powers. A relative
correction tending to one can remain inside `a_N`. The more general
`complex_volume_transfer` permits a normalization of rate zero even when its
modulus is not one.

The original `complex_packet_volume_transfer` assumes a **common all-level**
nonzero amplitude limit. The residue and parity theorems remove that
requirement without changing the original theorem's API. They use the same
actual sequence on every class. In particular, when `N = p*n+r`, the rate is
`log ‖K_(p*n+r)‖ / (p*n+r)`, not a rate with denominator `n`.

The new assembly proves three steps. First, finitely many residue thresholds
combine into one threshold for all integers, using quotient and remainder.
Second, convergence of each amplitude to its own nonzero value implies
zero logarithmic rate on that class. Third, taking real parts turns the
possibly different complex action limits into one common real limit, so
the exponential packet has that rate at every sufficiently large level.
The explicit even/odd corollary needs both parity hypotheses. The period
`p`, real power `k`, diagram and filling data are fixed before the limit.
The unit carrier `u_N` may vary arbitrarily with the level; no convergence
or finite-period assumption is imposed on it.

This is an application extension, not a correction to the written Morse
period theorem. [Appendix O](../manuscript/sections/O-morse-geometric-contribution.tex),
equations `mca:eq-3` and `mca:eq-4`, asserts a common finite-action and nonzero
amplitude limit after its displayed level factors and `q` phase are removed;
equation `mcg:eq-36` records the parity-sign cancellation. Likewise,
[the recursive filling chapter](../manuscript/sections/08-filling.tex),
equations `eq:final-asymptotic` and `eq:final-amplitude`, isolates the explicit
unit factors and nonzero coefficient. Those exact common-limit statements
can already use the original concrete theorem. Separately normalized
parity packets can instead use the new theorem, provided their stated
convergence hypotheses and common real rate are proved.

These are conditional analytic transfer theorems, not a construction of the
Kashaev or ADO invariant. The exact original source identity, convergence of
the nonzero packet coefficient and finite action, a strict bound for the
entire complementary remainder, and the geometric action-volume equality
remain explicit application inputs. This package does not formalize the
saddle analysis or hyperbolic gluing that supplies those inputs.

## Weighted graph energy

[WeightedGraph.lean](WeightedGraph.lean) contains seven definitions and
nineteen theorems in `VolumeLogic.WeightedGraph`. An edge label `e` has
endpoints `src e` and `dst e`, a real weight `w e`, and a real vertex
function `f`. The constructed energy is

\[
E(f)=\sum_e w_e\bigl(f(\operatorname{src}e)-f(\operatorname{dst}e)\bigr)^2.
\]

Edge labels are retained, so parallel edges are allowed. A loop contributes
zero. Connectivity means that every pair of vertices is joined by a finite
path of actual **positive-weight** edges, expressed by the reflexive
transitive closure of the endpoint relation. It is not an assumption that
the energy already has constant kernel. Ordinary graph connectivity and
strictly positive weights imply this path condition.

The main implications are:

| Theorem | Conclusion and explicit inputs |
| --- | --- |
| `energy_nonneg` | Nonnegative edge weights imply nonnegative energy. |
| `energy_eq_zero_iff` | Under the same hypothesis, energy is zero exactly when `f` agrees across every positive-weight edge. Zero-weight edges impose no equality. |
| `equal_of_positive_path` | Endpoint equality propagates by induction on an actual finite path. |
| `energy_eq_zero_iff_constant` | A connected positive support has exactly the constant functions as its zero-energy functions. |
| `grounded_energy_eq_zero_iff` and `grounded_energy_pos` | If one specified vertex has value zero, then zero energy forces `f = 0`; every nonzero grounded function has strictly positive energy. |
| `laplacian_form` and `laplacian_quadratic` | The explicit matrix `L = BᵀWB`, formed from signed edge incidences `B`, has bilinear form equal to the edge sum, and quadratic form equal to `E(f)`. |
| `grounded_laplacian_pos` | The explicit Laplacian quadratic form is strictly positive on every nonzero grounded function. |

The supporting theorems prove symmetry and linearity of the edge form and
invariance of energy under addition of a constant. The matrix identities
require a finite vertex set as well as a finite edge set; they are proved
by expanding the finite sums.

For the intended application, [the marked circle-pattern proof](../notes/actual_marked_deformed_circle_pattern.md)
identifies its Hessian with this energy. Its vertices are ordinary faces,
and an edge is a triangle together with an unordered pair of its ordinary
corners. If those corners have positive curvatures `w_i,w_j`, their weight is

\[
\kappa^t_{ij}=\frac{w_iw_j}{2\pi D_t(w_i+w_j)},
\qquad
D_t^2=\sum_{\{a,b\}\subset t}w_aw_b,
\]

where the sum is over ordinary corner pairs. A triangle with only one
ordinary corner contributes no edge. Different triangles may supply
parallel edges. The geometric differentiation giving this Hessian formula,
positivity of its conductances, and identification of the connected
ordinary-face graph remain **written inputs**. The actual finite real
quadratic-form implication from those inputs is proved here. This module
does not formalize circle-pattern existence, the rest of the geometric
Jacobian argument, or an implicit function theorem.

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
  Mathlib.Tactic.Linarith \
  Mathlib.Data.Real.Basic \
  Mathlib.Algebra.Order.BigOperators.Group.Finset \
  Mathlib.Algebra.BigOperators.Ring.Finset \
  Mathlib.Logic.Relation \
  Mathlib.Tactic.Ring
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
`RealTransfer.lean` and `WeightedGraph.lean`, and runs
[AxiomAudit.lean](AxiomAudit.lean). Every
definition and theorem must appear exactly once in the audit. Only Lean's
standard foundational axioms `propext`, `Classical.choice` and `Quot.sound`
are permitted; placeholders and additional axioms fail the check.

`summary.json` records every declaration, its axioms, all dependency pins,
and the SHA-256 hashes of the optional package, checker and Std-only sources.
It contains relative paths and omits timestamps so identical inputs produce
the same summary. Ten negative controls check altered pins, missing or
duplicate dependencies, an absolute local dependency, incomplete or
duplicate declaration audits, an omitted graph module or grounded-energy
audit entry, and an unexpected logical axiom. A failed run
removes any old success summary in its output directory.

The optional count is **nine definitions and forty-one theorems**, separate
from the Std-only theorem count: `RealTransfer` has two definitions and
twenty-two theorems, and `WeightedGraph` has seven definitions and nineteen
theorems. The audit checks these proofs and the
listed dependency pins; it does not certify that a particular knot family
satisfies the remaining written analytic and geometric hypotheses.
