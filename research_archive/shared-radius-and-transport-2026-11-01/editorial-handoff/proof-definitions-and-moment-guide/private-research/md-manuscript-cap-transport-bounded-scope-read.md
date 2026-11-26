# Bounded manuscript read: source transport, norms, and the central contribution

This is a read-only editorial and source-interface check of the current public manuscript. It covers the openings, source normalizations, concluding implications, and relevant dependency paragraphs of Appendices L, N, and O, together with the manuscript-wide occurrence search for cap moments, Hankel forms, and Gram estimates. It is not an exhaustive reproof of the complete manuscript.

## Findings sent to the parent

1. Appendix O's former description of central paths as “passing through the middle” was ambiguous: a two-step path can skip the central row. The parent has now replaced it by the exact degree conditions at `O-morse-geometric-contribution.tex:61–100`. With \(d=N-1\) and \(h=\lfloor d/2\rfloor\), a path \(j\to i\) contributes \(b^ic^{d-j}\), and central means \(i\le h\), \(d-j\le h\). Left means \(d-j>h\), and right means \(i>h\). These are disjoint and exhaustive at both parities and include the odd central zero-step path exactly once. The current definitions and the new reference from Appendix N are correct.
2. `L-balanced-terminal-fans.tex:1321` says the right polynomial “vanishes exactly when \(b=0\).” Prefer “vanishes identically under the protected specialization \(b=0\).” At an individual spectral node the one-sided polynomial also vanishes with positive \(b\). The proof needs only the stated protected-zero implication, so this is a precision of exposition, not a missing estimate.

## Completed and conditional statements remain separated

Appendix L explicitly constructs strict complete-radius balance before using it. Its restoration argument at approximately lines 1303–1363 uses phase-uniform local bounds on the same shared face torus, the original targets, a finite minimum over the surviving one-sided losses, and a fixed diagram. The strict full-minus-central estimate is therefore supplied there rather than inferred merely from the existence of the geometric saddle. The whole-period comparison retains the independently long fixed signed powers and the original normalization.

Appendix N states its degree-at-most-\(d\) assumptions in each spectral variable and retains repeated-node derivatives. The product-grid subtraction is used only for the actual full-minus-central polynomial, which vanishes on that full grid. Its final volume implication explicitly assumes both a strict shared supremum gap and a separate nonzero geometric asymptotic. The positive Fourier–Hermite Gram norm in lines 295–303 is a different, completed construction; that paragraph explicitly does not supply an exponential geometric estimate of the remaining source energy.

Appendix O proves the central contribution of the original exact source, with the original mark, parity, finite action, nonzero amplitude, whole Fourier period, and primitive geometric completion. Its opening and conclusions expressly leave the full complementary source unbounded in general. The supplied packing used by its analytic part is furnished for the stated simple-sphere class by the separately incorporated initial packing construction; no terminal decoration is silently inserted into the unchanged source.

The current manuscript does not contain the new private protected-moment spectral \(\kappa_N\) estimate, the separated-factor projection obstruction, or a claim that the cap-moment norm controls the original source. No numerical check is presented in the inspected passages as establishing an all-level source or volume estimate. The finite reproduction discussion explicitly limits those computations to their stated identities.

## Checks and changes

No public file was edited and no manuscript or guide build was launched for this read. No scientific rerun was made for the editorial audit. Separately, before freezing the private research, both new exact cyclotomic audit scripts were executed at levels 4–8 and their notes rendered through native MathML without warnings. Their exact paths, hashes, proved scope, and unresolved coupled spectral/source estimates are in `md-protected-transport-spectral-projection-manifest.json`.
