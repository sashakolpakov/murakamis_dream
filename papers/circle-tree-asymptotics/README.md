# Degree and twist estimates for circle-tree invariants

This paper proves the full reduced invariant asymptotic for a fixed literal
ordered tree of crossing circles whose original closure is a knot. Every
product junction carries a crossing circle. The diagram, orientations,
physical turns and signed crossing powers are fixed before the level tends
to infinity.

The sufficient condition is

\[
\sum_{v\in V}\frac{d_v}{d_v^2+n_v^2}\le 2^{-25},
\]

where \(d_v\) is the graph degree and \(n_v\in\mathbb Z\) is the signed
crossing power in the original disk frame. Zero powers are allowed when
the degree and the other terms permit this inequality. The condition does
not replace the requirement that the literal endpoint tracing gives one
main component and no internal closed component.

## Results

- **Theorem 1.1 (`cta:main`)** gives the nonzero leading asymptotic of the
  whole reduced, zero-framed invariant through both level parities,
  including its exact unit scalar and power \(N^{3/2}\). Its exponential
  rate is the volume of the original hyperbolic filled knot complement.
- **Theorem 1.2 (`cta:profile`)** gives the centered profile at
  \(M=q_N^s\), uniformly for \(|s|\le R<1\), with error \(O_R(N^{-2})\)
  after retaining the explicit framing scalar and sine quotient. It also
  proves eventual nonvanishing on that disk.

The paper proves the full-index remainder estimate, complex edge packet,
whole Fourier-period reduction and nonzero first-charge contribution. It
does not assert the directed criterion, a larger bare-junction Conway
grammar, a fixed meridian neighborhood, or an all-orders operator result.

## Exact inputs

| Companion | Statement | Use |
| --- | --- | --- |
| [Exact Newton calculus for tangles with a moving meridian](../meridian-tangles/main.tex) | Proposition 6.1 (`mt:crossing`) and equation (6.4) (`mt:trace-grid`) | Actual crossing powers, full collision normals and translated-grid trace. |
| Same companion | Theorem 7.1 (`mt:tree`) | Original full tree contraction, physical turns and closure. |
| Same companion | Proposition 8.1 (`mt:scalar`) | Exact main-meridian scalar ledger, including mixed signed words. |
| [Holomorphic source asymptotics and volume limits for Conway closures](../conway-asymptotics/factorial.tex) | Lemma 2.1 (`ca:factorial`) | Canonical factorial interpolation, exact reflections and uniform complex bulk expansion. The midpoint and edge-contour applications are proved here. |
| [Circle-tree geometry](../circle-tree-geometry/main.tex) | Theorem 1.1 (`ctg:main`) | Original primitive smooth filling and absolute action-volume identity when \(\sqrt{d_v^2+n_v^2}\ge630\). The summed condition implies this bound and places the selected saddle in the same geometric chart. |

The independently long-twist theorem in the oscillatory-fillings companion
is not used to cover zero-power vertices. The degree-sensitive Fourier
argument needed here is written in [joint-filling.tex](joint-filling.tex).

## Finite reproduction

From the repository root, with Python, SymPy and mpmath installed:

```sh
python3 papers/circle-tree-asymptotics/check.py \
    --output /tmp/circle-tree-check.json
```

The JSON record pins the checked sources. The checker verifies four exact
edge identities, fifteen inequalities with rigorous rational bounds and
990 finite complex-product samples; it also includes altered-threshold
negative controls. These checks do not prove the uniform contour estimates,
Gaussian asymptotics, topological identification or imported geometric
theorem. Those arguments and their hypotheses are stated in the paper.

The mathematical source begins in [main.tex](main.tex); the native contour
figure is [figures/joint-contour.tex](figures/joint-contour.tex).
