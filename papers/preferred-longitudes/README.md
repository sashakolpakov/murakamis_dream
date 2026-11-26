# Preferred longitudes of Conway tree complements

[Read the PDF](../../docs/papers/preferred-longitudes.pdf) · [TeX source](main.tex) · [Dependency graph](https://sashakolpakov.github.io/murakamis_dream/papers/dependencies.html)

The paper determines the preferred longitude on the geometric
meridian germ of a fixed strict Conway construction with independently
sufficiently long signed fillings:

$$
L_{\mathrm{geom}}(M)=-M^{a(D)}
 \prod_{e\in\mathcal E}\frac{M^2-X_e(M)}{1-M^2X_e(M)},
\qquad a(D)=-w(D)-\sum_v n_v.
$$

Here $M$ is the selected main-meridian eigenvalue, $L_{\mathrm{geom}}$
is the preferred-longitude eigenvalue on the same eigenline, $w(D)$
is the oriented writhe, and $n_v$ is the signed crossing power at
circle $v$. Each $X_e=e^{2\pi i x_e}$ belongs to one original
quarter-turn edge. The complete filled knot fixes the branch and the
minus sign.

The proof first works on the algebraic family of augmented
representations. Boundary isotropy and a constant-field calculation
show that the unknown factor in the squared longitude depends only on
$M$. Regular matrix reconstruction through every nonzero value of $M$
makes this factor a monomial, including at the split trace-zero fibers.
An explicit cusp path determines its exponent after the framing
correction; a Seifert-surface frame calculation determines its sign.
Meridionally filling a newly inserted zero-crossing circle at each bare
junction then proves the same formula for arbitrary strict junctions.
That operation restores the original tangle and its peripheral paths.

The geometric inputs are the ordered representations and their local
peripheral coordinate charts in [Nonparabolic holonomy of trees of
crossing circles](../nonparabolic-tree-geometry/README.md), together
with the strict complete and filling geometry in [Marked geometry of
strict Conway compositions](../strict-conway-geometry/README.md).
The finite Newton trace is used only to identify a classical junction
action and its additive constant. A quantum asymptotic or recurrence
is not a premise. The [meridian-expansion paper](../meridian-expansions/README.md)
uses the result for its separate geometric-factor consequence.

Build from this directory with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

The bounded exact checker requires Python 3 and SymPy. From the repository root:

```sh
python3 -I papers/preferred-longitudes/check.py --output /tmp/preferred-longitudes-check.json
```

The checker verifies rational matrix and differential identities,
including the cusp coordinate changes, and tests integer framing and
lift conventions. The generic-fiber argument, regular reconstruction,
peripheral paths, spin calculation and stationary elimination have
written proofs in the paper. Finite examples do not prove those results.
