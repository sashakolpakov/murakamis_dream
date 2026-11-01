# Uniform bounds for finite Hermite filling functionals

The standalone article proves the finite bound

$$
|\mathcal L_N^n H|\le (1+|n|/2)\|H\|_{[-2,2]},\qquad \deg H<N,
$$

with the explicit Gaussian multiplier and all repeated-root derivatives. It includes the node-vanishing improvement, the joint-product-grid subtraction, canonical polynomial remainders and resolvent reproduction, the local Casimir/Fourier identity, and the finite crossing polynomial with its normal derivatives. The finite proofs work at every $N\ge2$, including both parities and composite levels.

The shared-diagram application is conditional on its stated exact marked-source identity. That companion input must retain the original cups, caps, mark, grids, framing, and shared coefficient targets. This article does not prove a full knot-volume limit.

`main.tex` is a standalone `article`, using standard LaTeX packages and its own bibliography. It has no inputs from the long manuscript. The main mathematical source is Appendix N, with the crossing-normal proof expanded from `notes/casimir_braiding_and_recoupling_lattice.md`, Section 3. Hermite interpolation and the Riesz/Bernstein inequality are classical tools; their needed finite forms are proved in the text and attributed to primary references.

Build from this directory with `latexmk -pdf main.tex`, or use the repository's manuscript builder. The common builder enforces the 30-page limit and checks references and overflow.
