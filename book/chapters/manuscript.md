# The Conway composition manuscript

The paper presents the volume identity for knots built from a specified
class of finite Conway tangle compositions. It starts with the invariant
and tangle conventions, develops the finite source and its geometric
optimization, and follows the selected complex action through the
crossing-circle fillings.

[Read the PDF](../../manuscript/build/main.pdf) ·
[TeX sources and build instructions](../../manuscript/README.md) ·
[Sphinx edition](https://sashakolpakov.github.io/murakamis_dream/sphinx/)

## The theorem's scope

Starting with a two-leaf block $hh$, completed tangles may be turned,
stacked, or extended by a single leaf on either side:

$$E::=hh\mid T(E)\mid E_1E_2\mid hE\mid Eh.$$

The cylindrical closure has two completed children. Choose a fixed
half-twist pattern giving a knot. For every fixed finite expression,
independently sufficiently long signed full twists give

$$\lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K)|
  =\operatorname{Vol}(S^3\setminus K).$$

The expression and twists are fixed before $N$ tends to infinity.
Both parities and composite levels are included. The threshold may
depend on the expression. Earlier isolated seed closures of width at
least three are treated separately.

The right side is the knot complement volume. Filling the auxiliary
crossing circles inserts twists, and leaves the knot cusp unfilled.
The paper does not claim coverage of every arborescent presentation.

## Reading the proof

The finite source uses the full Newton algebra, including repeated-root
directions. The same leaf and multiplication weights define a concave
angle problem. Its unique strict optimizer supplies the complete
augmented-link geometry and the local quantum action.

A separate estimate controls every alias and the physical colors away
from completeness. The key composition step combines one leaf with its
gate and the completed child's output tangent. The complex packet and
the full Fourier filling calculation then give a nonzero leading term.
The marked peripheral equations identify its real exponent with the
volume of the resulting knot complement.

![The new leaf and completed child's output tangent enter the same Newton gate; the parent retains the inherited and new alias losses.](../../manuscript/build/figures/attachment-tangents.png)

[Vector PDF](../../manuscript/build/figures/attachment-tangents.pdf) ·
[Editable TikZ](../../manuscript/figures/attachment-tangents.tex)

## Reproduction

```sh
python3 repro/verify.py --list
python3 repro/verify.py --output repro/results
```

The suite replays the exact two-leaf, single-leaf and endpoint
certificates, and checks their stored rational results. The
[reproduction guide](../../repro/README.md) explains the arithmetic;
the [proof-input map](../../repro/PROOF_INPUTS.md) distinguishes the
finite checks from the analytic, geometric and topological proofs.

The older research routes remain accessible through the library.
The paper provides a continuous argument for its stated composition
class; the archive preserves the calculations and alternative approaches.
