# Planar certificates, triangular insertion and flattening calculus

This record describes bounded reviews of the two extracted papers and the
new real-calculus Lean module. It separates written arguments, checked
finite certificates and formal implications. The accompanying
[hash snapshot](planar-insertion-audit-snapshot.json) identifies the inputs;
it is not an end-to-end proof certificate.

## Shared face estimates and protected gluing

The independent read covered the complete
[planar-certificate paper](../papers/planar-certificates/main.tex), with
particular attention to Sections 3–6. No mathematical correction was found
in the following implications.

- The finite cover keeps every locally allowed central/left/right string,
  including strings whose final coefficient vanishes. Each witness uses
  one modulus for every occurrence of a face. The Cauchy target is exactly
  `N−1` at each ordinary face, and the finite sum bounds the entire real
  spectral cube. The separate spectral degree remains at most `N−1`.
- The triangle entropy and Hessian give a quadratic action cost at the
  stationary complete weights. The supporting tangent gives the linear
  entropy gain. Both branches of each one-sided maximum are controlled;
  the quantitative defect condition also makes the other local losses
  nonnegative. Equality is allowed in the initial weak-balance conditions.
- Protected triangular gluing removes two singleton triangle terms whose
  sum is `log B`. The old target sums count the ordinary face `B` twice
  and the new sum once. This gives the exact correction and the sector
  map `C → (C,C)`, `L → (L,C)`, `R → (C,R)`. A noncentral output has a
  noncentral input. Whole-vector rescaling aligns the single shared
  ordinary weight without changing any input cost.
- The seventeen-region example has fifteen nonempty right-subset branches
  and twenty-five remaining anchors. The separate anchored comparison
  uses mixtures only at regions 2, 4 and 7, with right anchor 12. Its
  excess locates failure of weak balance among `{2,4,7,12}`; it does not
  establish excessive growth of a genuine signed sector. Attachment at
  region 15 preserves those regions and their complete weight ratios.

The paper replaces the earlier entropy-integration route by the direct
convex inequality

\[
Q(\beta q)\ge \beta Q(q)+(1-\beta)
                  \bigl(Q(q)-q\cdot\nabla Q(q)\bigr).
\]

Here `Q` is the actual triangle potential and the last parenthesis is its
entropy at the complete vector. This simplification neither asserts
concavity of a maximum of sectors nor assumes the desired gain. See
`pc:triangle-calculus`, `pc:tangent`, `pc:side-loss` and `pc:weak-balance`.

## Insertion at an ordinary triangular face

The independent read of the
[insertion paper](../papers/triangular-insertion/main.tex) covered Sections
2–7 and its numbered planar imports. The earlier written source review
also covered the strengthened whole-block comparison and the forty-five
branch certificate; see the existing
[triangular-boundary audit](manuscript_audit/triangular-boundary.md).
The new independent paper read did not repeat the all-length construction
and finite example in Section 9, or every foundation proof.

The checked boundary argument includes strict transport feasibility,
coercivity as well as Hessian positivity, development of the disk with
multiplicity one, and the joint limit when two boundary weights vanish.
The optimized disk action is the old triangle potential plus its fixed
constant. The bounded-interstice Soddy comparison is used only at the
conditional central minimizer, not at arbitrary certificate witnesses.

For the ordered quartets `(u,v,c,b)` and `(u,a,v,b)`, put
`T=Q(u,v,b)` and `Delta=2T−log b`. The block adds interior targets and one
comparison target at `b`, but none at the already ordinary `u,v`. Hence
only `b` is duplicated, giving the correction `−Delta`. The final split
uses the **whole inserted string**:

- If the block is central, the bridge is central or left, its defect is
  zero, and its conditional addition `+Delta` cancels exactly.
- If the block is noncentral, its absolute certificate absorbs a bridge
  defect at most `Delta/2`. No ordering of that witness is assumed.

Several insertions may share boundary vertices, but must use distinct
matching pairs and fresh interiors. Each core face still has one target;
the corrections add occurrence by occurrence. The result does not assert
that filled volumes add or that old knot parities automatically survive.

One correction to the compressed description in the original
[Appendix R](../manuscript/sections/R-triangular-boundary-insertion.tex)
is explicit in the new paper: the unchanged non-cap pair has outer
weights **`(2,0)`**, with middle weights `(1,1)`, rather than two positive
outer weights. Quarter loads on the two supported corners give
`Q(2,1,0) ≥ 2g+(log 2)/4`, where `g=e(1/4)`. Consequently
`X ≥ 4g+(log 2)/2`, and each mixed difference is at least
`2g+(log 2)/4`. The paper records these bounds near `ti:eq-28d` and in
the table following `ti:eq-28i`. This repairs the description and its
local justification without weakening the theorem. The historical
appendix hash is retained separately; it was not silently replaced.

## Finite certificate computations

The computations use fixed rational witnesses, exact row and face
margins, and outward interval arithmetic with an explicit Lobachevsky
Fourier tail. They do not call an optimizer to establish an inequality.

| Check | What the finite result establishes |
| --- | --- |
| [Planar checker](../papers/planar-certificates/check.py) and its two imported verifiers | The complete forty-branch cover, a gap greater than `1/25`, a restricted anchored excess greater than `1/40`, and the stated oriented seed and eight finite attachments. |
| [Insertion checker](check_triangular_boundary_certificate.py) | Forty old branches plus five newly allowed overload anchors at the stated fixed boundary ratios; margins greater than `1/50`, fixed core constants, and the listed finite incidence constructions. |

The all-length and arbitrary-iteration conclusions come from the written
induction, curvature-ratio and monotonicity arguments, not from those
finite constructions. The computations do not evaluate the invariant of
the large assembled diagram or prove its asymptotic volume limit.

The planar wrapper also records its NumPy dependency, removes a stale
success summary before replay, and invokes its child checker in isolated
mode. The publication's seven-group replay at the time of this review included both
current checkers and the changed protected-sum helper:

- [Consolidated finite-check record](results/paper-algebra/summary.json).
- [Planar certificate result](results/paper-algebra/planar-certificates/summary.json).
- [Ordinary insertion result](results/paper-algebra/triangular-insertion/summary.json).

I compared the recorded input and result hashes with the current files.
Preparing this audit did not execute the suite again. The fresh execution
is evidence for the finite claims stated by those checkers; it is not a
replay of the written asymptotic or geometric proofs.

## What the new Lean module proves

[Flattening.lean](../formal-real/Flattening.lean) has one definition and
nine theorems. Its hypotheses identify derivatives of actual real
functions on an interval. From `g'(0)=0` and `0≤g''≤E` it derives

\[
0\le g(t)-g(0)\le Et^2/2.
\]

The upper bound follows by applying convexity to the constructed function
`E*x²/2−g(x)`. The module also defines the actual common path
`P((1−t)q)`, proves the supporting-tangent inequality at scale one, handles
both local maximum branches with the constructed balance defect, and
joins these bounds to the existing strict scalar gain criterion.

The executed optional-package replay checked all **60 declarations**
(10 definitions and 50 theorems), including the nine new theorems, with
zero compiler warnings. All nine dependency pins were retained; twelve
negative controls were rejected. The full axiom inventory permits only
Lean's standard foundational axioms. The hashes of that replay are
retained in this review's snapshot. The
[current summary](results/concrete-limits/summary.json) additionally
includes the later transport-coercivity module; its scope is described
in the [tangle and tree review](TANGLE_TREE_AUDIT.md).

Geometric differentiation, the complete stationary point, the directional
Hessian bound, entropy and pure-corner identities, and identification with
the original source remain written inputs. Existing scalar modules check
the gluing/target implications; they do not construct the geometric disks.
Neither Lean count is a claim that all analytic or hyperbolic arguments
have been formalized.

## Foundation and conclusion boundaries

Both papers use the finite paper's original marked source and invariant
normalization; the local paper's all-phase, all-real-spectrum sector
bounds; the source-asymptotics and oscillatory papers' nonzero **whole
central period**; and the marked-fillings paper's primitive metric and
absolute action-volume identification. The exact numbered imports are
listed in the snapshot. The source gap is supplied separately by the
certificate arguments reviewed here.

For the volume conclusion the diagram and every signed filling power
are fixed before the level limit. The filling threshold is enlarged so
that the central action drop is smaller than the proved source gap.
The finite Hermite norm retains first normals and both level parities.
No unrestricted matched-sphere remainder estimate, level-dependent twist
limit, or classification of unmarked knot types is asserted.
