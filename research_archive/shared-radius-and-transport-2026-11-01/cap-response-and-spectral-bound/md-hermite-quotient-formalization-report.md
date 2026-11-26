# A finite algebraic bridge toward the Hermite functional

The next step is feasible in the existing Std-only project. The private copy at `/private/tmp/md-hermite-quotient-formal` now contains `VolumeLogic/MonicRemainder.lean`, with 37 new theorems. The library and the complete 55-theorem axiom inspection compile without warnings. Every theorem uses at most `propext`, `Classical.choice`, and `Quot.sound`. The publication checkout was only read.

The frozen new module has SHA256 `f6781dba17c7677adcfe2aec41d31f8742004fc38a45be9732c24ce98b65dbfd`. The full file hashes, read-input hashes, declaration list and axiom dependencies are in `/private/tmp/md-hermite-quotient-verification.json`; raw compiler axiom output is `/private/tmp/md-hermite-quotient-axioms.txt`.

## What is constructed

Let R be an arbitrary commutative ring, let `roots=[r₀,…,rₙ₋₁]`, and put

\[
p(X)=\prod_{i=0}^{n-1}(X-r_i).
\]

Repeated entries are permitted. No field, order, topology, distinct-root assumption, inverse root difference, or hypothesized quotient identity is used. As in the existing project, polynomial lists contain coefficients in ascending powers. Equality is equality of every formal coefficient, with trailing zeros ignored; it is not inferred from equality of polynomial values over R.

`timesLinear r f` implements multiplication by X−r. `synthetic r f` is the polynomial quotient

\[
D_rf(X)=\frac{f(X)-f(r)}{X-r},
\]

where the expression is implemented recursively without division in R. The reconstruction is proved as a literal list equality for a nonempty coefficient list, and coefficientwise also for the empty representation of zero. Its Horner value is proved equal to the pre-existing division-free `dividedDifference f r z`.

The repeated synthetic quotient and Newton remainder are then constructed by

\[
Q_{r::s}(f)=Q_s(D_rf),\qquad
R_{r::s}(f)=f(r)+(X-r)R_s(D_rf),
\]

with Q_empty(f)=f and R_empty(f)=0. The main division theorem proves, coefficient by coefficient,

\[
f=pQ_{\mathrm{roots}}(f)+R_{\mathrm{roots}}(f).
\]

The implementation separately proves that the modulus is monic, the remainder has no coefficient in degree at least n, and a polynomial represented with at most n coefficients is unchanged by taking the remainder. Thus the remainder degree and the quotient relation are consequences of the definitions, not theorem parameters.

## The top coefficient and repeated roots

Define the iterated Newton functional recursively by

\[
T_{[r]}(f)=f(r),\qquad
T_{r::s}(f)=T_s(D_rf)\quad(s\ne\varnothing).
\]

The main functional identity is

\[
[X^{n-1}]R_{\mathrm{roots}}(f)=T_{\mathrm{roots}}(f).
\]

At two nodes it specializes to the existing divided difference, including coincident nodes. Formal differentiation is defined by the algebraic Horner rule. Lean proves the entire twofold-root remainder

\[
R_{[r,r]}(f)
 =f(r)-rf'(r)+Xf'(r),
\]

and hence its top coefficient is f′(r). This retains the first normal term instead of replacing a repeated root by its value.

There is also an exact ideal-annihilation result. Synthetic division of `(X-r)f` returns f as a literal coefficient list. Induction therefore proves

\[
R_{\mathrm{roots}}(pq)=0,
\qquad
T_{\mathrm{roots}}(pq)=0
\]

for every coefficient list q. Full R-linearity, uniqueness of the Euclidean remainder, and an abstract quotient-ring instance have not been separately formalized. The proved statements concern the explicit division algorithm and its coefficient functional; they should not be described as a formal construction of the whole quotient-ring API.

## Dependencies of the principal results

| Formal theorem | Content and proof inputs |
| --- | --- |
| `synthetic_reconstruct` | Exact formal-coefficient division by X−r; list induction and ring identities. |
| `monic_division_identity` | The full split-monic division identity; the preceding reconstruction and compatibility of coefficient equality with linear multiplication. |
| `monic_remainder_degree_bound` | The constructed remainder has exactly n coefficient slots and vanishes above them. |
| `top_coefficient_is_newton` | Top-coefficient extraction equals iterated synthetic divided difference; degree bound and induction on the root list. |
| `monicRemainder_of_degree_lt` | Below-degree inputs are unchanged; quotient length, division identity and zero-product identity. |
| `monicRemainder_annihilates_multiple` | Explicit multiples have zero remainder; exact cancellation of each linear factor. |
| `two_node_top_coefficient` | The coefficient trace equals the existing divided difference, without distinctness. |
| `double_root_remainder` | Both coefficients modulo (X−r)², using the formal Horner derivative. |

All 37 new helpers are included in `AxiomAudit.lean`, including those carrying `@[simp]`. Attributes are on separate lines, so the earlier scanner also sees them. The theorem declarations assume only the ring structure and their displayed finite data, except for explicit elementary degree hypotheses in the two below-degree normalization theorems.

## Relation to Appendix N

Appendix N uses the monic polynomial

\[
\chi_N(X)=2T_N(X/2)+2
\]

and the polynomial resolvent numerator V_N. Once the stated factorization of χ_N into double nodes and its possible odd simple node is supplied, the new algorithm applies to precisely that root list. It formalizes the algebraic operation of reducing a scalar polynomial h modulo that split monic polynomial and extracting its highest permitted coefficient.

It does not yet prove the general confluent root-sum formula

\[
[X^{N-1}](h\bmod\chi_N)
 =\sum_{c\text{ double}}
 \left(\frac{h'(c)}{g_c(c)}-
       \frac{g_c'(c)h(c)}{g_c(c)^2}\right)
 +\sum_{r\text{ simple}}\frac{h(r)}{\chi_N'(r)},
\qquad g_c(X)=\frac{\chi_N(X)}{(X-c)^2}.
\]

That formula requires the finite interpolation/partial-fraction assembly across distinct root blocks, with the required differences or denominators proved invertible. The existing `double_root_jet_identity` is a denominator-cleared local identity, while the new `double_root_remainder` establishes the actual polynomial remainder for a single repeated block. Together they supply concrete algebraic inputs for that next assembly; they are not a proof of it.

The remaining application inputs are also separate: the Chebyshev factorization and derivative values, χ_N(Ω)=0 for the original crossing representation, the identification of V_N with the polynomial divided-difference numerator, and the conversion from the resulting scalar trace to f(Ω). No trigonometric root theorem, analytic derivative, Hermite norm, source estimate, stationary phase argument, filling theorem, or volume statement is established here.

## Files for integration

Only these three files differ from the copied formal project and are intended for integration:

- `VolumeLogic/MonicRemainder.lean`: the new 37-theorem module.
- `VolumeLogic.lean`: one additional import.
- `AxiomAudit.lean`: all 37 additional theorem inspections.

The project continues to use the unchanged Lean 4.32.2 toolchain and Std-only Lake configuration. No publication build, commit, or source edit was performed.
