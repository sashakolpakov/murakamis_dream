# Finite spectral evaluation and uniform filling bounds

[Read the PDF](../../docs/papers/filling-bounds.pdf) · [TeX source](main.tex) · [Dependency graph](https://sashakolpakov.github.io/murakamis_dream/papers/dependencies.html)

The paper connects two descriptions of the same finite knot invariant:
a contraction of crossing matrices, and a coefficient of a polynomial
whose face variables are shared across the diagram. It then bounds the
cost of inserting fixed signed crossing powers into that polynomial.
These are the algebraic foundations used by the later source estimates
and volume arguments.

Its first theorem is the estimate

$$
|\mathcal L_N^n H|\le (1+|n|/2)\|H\|_{[-2,2]},\qquad \deg H<N.
$$

Here $N\ge2$ is the integer level, $n\in\mathbb Z$ is the signed crossing
power, $\|H\|_{[-2,2]}$ is the supremum norm, and $\mathcal L_N^n$ is the
Gaussian Hermite functional defined in Section 1. It retains first
derivatives at the double roots of $2T_N(z/2)+2$, where $T_N$ is the
Chebyshev polynomial. At odd levels, the remaining simple root has its
own value term. The theorem also gives stronger bounds when values
vanish at the nodes, and an exact subtraction for several variables.

The finite matrix calculations establish the Casimir/Fourier identity
and the full crossing polynomial. For a planar diagram obtained from
a matched triangulated sphere, Theorem 9.1 proves the exact marked face
coefficient, and Corollary 9.2 expresses its signed crossing insertions
by these functionals. Theorem 10.1 identifies that evaluation with the
reduced Kashaev invariant, including the framing factor, at every
integer level $N\ge3$. The cups, caps, marked cut, face lattice and both
level parities are part of those proofs. The diagram identity is therefore
a conclusion of this paper, not an unproved companion assumption.

The input is the enhanced ribbon definition of the reduced invariant.
The needed finite interpolation forms are proved here and attributed
to their classical sources. No theorem from the long reference manuscript
is required as a substitute for these proofs. A nonzero asymptotic, a
bound for the entire remaining sum, and its geometric volume comparison
are separate analytic and geometric inputs to later applications.

## Build and finite checks

From the repository root:

```sh
python3 tools/build_papers.py filling-bounds
python3 repro/run_research_checks.py filling-supremum
```

The builder checks references, overflow and the 30-page ceiling. The
finite checks exercise the Hermite formulas and the value/derivative
channels described in the [reproduction guide](../../repro/README.md#uniform-bounds-for-inserting-twists).
They do not prove the uniform norm theorem by sampling, and they do not
supply an asymptotic or a geometric volume identity.
