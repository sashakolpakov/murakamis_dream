# A failed extension of an independently released half-stencil box

This folder preserves one fixed outward calculation. It tests the proposed
replacement of the outer coherent edge in the old right half stencil by
the complete raw right-edge derivative, keeping the old imaginary gauge
`kappa=3/2` and independent typed height intervals. It does not test the
whole mixed derivative or any finite kernel.

The local types, from center to neighbor to right vertex, are `(4,3,4)`.
The exact data are

```
t = 21999/100000,    neighbor real = 11/50,
center coefficient = -57/1000,
neighbor coefficient = -3/100,
chi = xi = 1,       right target = 1/2.
```

Set `r=(t-.1)/.12`, `a=t-.057 i r`, and `b=.22-.03 i r`.
The inner coherent block is the original `phi_(1,0)(a,b)`, with
its quadratic cotangent root and original zero logarithmic lift.
The outgoing raw block has own type four and moving first argument `b`.
Its unique maximizing row lies strictly between the rational endpoints
`2577507243/10^10` and `2577507245/10^10`.

Writing `ga=phi_a`, `gb=phi_b` and
`K=g'(b+u)-g'(b)+2 pi i u`, the tested half is exactly

```
Re[(1-.475 i)(ga-1.5 i) - .25 i (gb+K)].
```

The outward terms are approximately

| Term | Value |
|---|---:|
| Gauged center derivative | +.0605539052193 |
| Inner neighbor-height derivative | -.2910736062688 |
| Favorable raw neighbor-height derivative | +.2290662960 |
| Total | -.0014534050 |

The checker proves the total is below `-7/5000`. Thus a favorable raw
height term alone does not justify reusing the old independently
released nonnegative half inequality. It retains the actual raw row;
the failure is not caused by replacing that row by a bracket endpoint.

**Both coefficient choices are excluded by existing actual-reference
geometry.** The already proved
[conditioned three-type table](../../../notes/research_mixed_neighbor_conditioned_critical_boxes.md)
has, in row `101=(4,3,4)`, neighbor height in `(-.025,-.011)` and
first/center height in `(-.053,-.034)`. The displayed choices are below
both intervals. This calculation therefore does not obstruct reuse on
those narrower actual conditioned domains and is not an actual-cycle
counterexample. It supplies no finite-source, whole-flow, integral,
or volume-conjecture counterexample.

The checker is standalone apart from `python-flint` and repository
theorem records. It uses an explicit quadratic root, exact rational
data, outward elementary functions, and strict row-derivative signs.
The polynomial identity fixes the exponential equation; a direct
original-log residual bound excludes every nonzero logarithmic lift.
The inherited strict row concavity and bracket identify the unique
real maximizing row. No root proposal, optimization, or parameter
cover is used.

Run from the repository root:

```sh
python3 repro/diagnostics/2026-11-05-distance-two-raw-half-obstruction/check.py
```

`result.json` binds the current source proofs/checkers/records and this
folder's checker and README. The displayed bound is a certified statement
about the specified released box; the diagnostic classification concerns
its limited relevance to the actual cyclic problem.
