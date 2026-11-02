# Proof changes in the combined paper

The combined paper is **Spectral bounds and asymptotics of Casimir sources**, built from the two editions at commit `acd7e7d5`. Its PDF has 25 pages at 11pt on A4 with 30mm margins. The local edition used 30mm margins and the central-source edition used 27mm margins. No proof was shortened by changing type size or margins.

The two subjects share the same finite polynomial, recurrence, entropy, and central cut. The second theorem uses the first paper’s transfer, interpolation, and action results directly. This is the mathematical reason for consolidating them. It does not combine their hypotheses or extend either conclusion.

## Main statements and scope

- The local uniform sector theorem is still Theorem 1.1. Its fixed-zero-pattern hypothesis, positive outer sum, all real spectra, arbitrary face phases, compact uniformity, and both parity conventions are unchanged.
- The shared central-coefficient theorem moves from Theorem 1.1 of the source edition to Theorem 8.1. Its simple sphere, dual matching, protected nonmatching edge, stationary positive radii, fixed diagram, holomorphic asymptotic, raw sign, finite action, Gaussian determinant, negative spectral Hessian, and real-cube/complex-strip gap are unchanged.
- The one-sided sector estimates are value bounds. The central comparison is coefficientwise. The manuscript continues to distinguish these conclusions.
- The local analytic action is defined by the exact polynomial. It is not obtained by differentiating an approximate nodal interpolation.
- The common face integral uses one radius vector and the primitive quotient lattice. No independent local optimization or unproved contour contribution is substituted.
- Section 14 retains the normalized input to the oscillatory filling theorem and its exact parity cancellation. Neither a full complementary-source bound nor an identification with hyperbolic volume is added.

## Definitions stated once

1. The operator `sa:operator` now aliases `lc:banded` in Section 2. The full physical Fourier adapter from the local paper is retained, including transpose, diagonal change of basis, block conventions, and the divided-difference interpretation at singular spectral values.
2. The entropy `sa:entropy` now aliases `lc:entropy` in Section 1. The original zero-load convention and the local paper’s proof of the additive normalization remain.
3. The recurrence `sa:R` now aliases `lc:R-recurrence`. The row-replaced determinant definition and the convention for negative indices remain in Section 2.
4. The original starting-row expansion `sa:path` moves from source Section 2 to combined Section 2. The repeated unnumbered starting-row formula in old local Section 5 and the repeated recurrence in old local Section 3 now refer to this definition.
5. The central identities `sa:even` and `sa:odd` alias `lc:even-factor` and `lc:odd-factor`. Their full cut-and-reflection proof remains. The odd skipped-row contribution and its derivative at zero remain explicit.
6. The source edition called a scalar action function `E_b`, although that symbol already denoted a finite cofactor. The scalar is now `\mathcal E_b`, agreeing with the local edition. No formula changes.

## The only duplicated proof removed

The last paragraph of the source edition’s exact-node lemma proved positivity of the signed interval tail by the recurrence

`q_r = (x+y) q_{r-1} - gamma_r xy q_{r-2}`

and the identity for `q_r - x q_{r-1}`. This is already proved in full in the local edition’s Lemma 3.1, including the trigonometric identity, `0 <= gamma_r <= 1`, coefficientwise positivity, comparison with the all-one-step product, and inclusion of those paths in the zero-spectral cofactor.

The combined exact-node lemma refers to that earlier proof. Its distinct eigenpolynomial, moment, Jacobi-recurrence, Cholesky, positive-determinant, and maximal-fold normalization arguments are unchanged. This removes a second copy of a proof, not a mathematical input.

## Proofs retained without substantive alteration

- Exact local path partition, central factorization, and reflected one-sided sector.
- Nodal comparison and logarithmic interpolation bound, including the physical nodes at both parities.
- Signed slow-transfer upper bound through coincident roots and the initial endpoint, with both unused spectral products.
- Absolutely normalized triangle action, its derivative, all zero-variable cases, and the competing endpoint value.
- The full two-endpoint one-sided envelope proof, including the post-change stationary branch, its logarithmic differentiation, and its spectral derivative sign.
- Continuous real positivity of interval tails and the final spectral cap.
- Positive nodal matrices, exact cofactor/determinant adapter, and both parity normalization factors.
- Interior-start analytic recurrence construction, exponentially accurate summation, contributing contour, and protected-middle transport proof.
- Terminal cofactor ratios and exact central normalization.
- Positive-matrix angular contraction, binary zero-face case, unavailable-node interpolation, and the shared angular complement.
- Ordinary graph connectivity, primitive lattice, grounded Hessian, finite shared saddle, Gaussian coefficient one, and holomorphic relative error.
- Real spectral loss on the same radii and its extension to a fixed complex strip by the Poisson estimate.
- The central filling asymptotic and its exact normalization.

## Exposition and bibliography

The introduction now explains the two questions, the shared finite object, and the distinct analytic outputs before giving the local notation. It names the methods used in the proofs. Standard one-variable summation and saddle formulas are attributed to DLMF §2.10(i) and §2.4(iv); the manuscript retains its own uniformity, contour, and multivariable arguments.

Both original diagrams remain. The local path diagram is extracted unchanged into a separate TikZ source. The tetrahedral diagram is unchanged; its final caption sentence now says directly that its drawn edge lengths do not prescribe variational radii.

All imports of the local companion become internal references. The finite-operator and oscillatory-filling companions remain distinct external inputs. The positive stationary radii are still an analytic hypothesis; a geometric construction of those radii is not imported as a hidden premise.

## Review files

The consolidation review compared fourteen unified source diffs, one
for each resulting section, expanding the extracted local figure in
its comparison. The retained original editions and the combined sources
allow those comparisons to be repeated. `label-migration.json` records
all 97 old labels against the compiled AUX numbers and the new source
lines. `consumer-migration.json` lists every occurrence in the four
affected current papers. `public-integration-report.json` records the
final five PDF builds, source hashes and unchanged earlier editions.

After integration, the registered finite reproduction command ran the
new wrapper, which delegates to both unchanged finite checkers. Its
result is saved in `repro/results/paper-algebra/casimir-source-asymptotics/summary.json`.
The separate mathematical reading is in
[the audit report](../casimir-source/report.md). Neither finite checks
nor this proof-retention comparison replace the written analytic proofs.
