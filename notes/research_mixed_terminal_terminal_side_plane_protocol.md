# A fixed saved-only terminal-side update of the joined planes

Research protocol, 6 November 2026. This calculation is unrun when frozen.

The [terminal-side marginal enclosure](research_mixed_terminal_terminal_side_marginal_enclosure.md)
gives a second valid upper bound for the one term
\(U=\Delta\Im p_T\). Every other term in the completed whole-disk
and source-cell plane estimates remains valid. This protocol updates
only \(U\), with no new scalar-gain call or analytic evaluation.

## 1. Fixed sources and associations

Use the two \(\beta=1\) canonical families on \(D_4\), both terminal
types, at \(H=1/100\). The exact affine centers and responses are
unchanged. Bind the completed records:

* Whole-disk joined planes, SHA256
  4bfa03e1c61a4e34d9b6d549b5e9d666b15df606078d02258dae340055e3ee88.
* Original source-cell planes, SHA256
  53fd53494b658f5faa76ab9fb185b9e5c492d61eb8942944d9bd8e48b2fbfbbb.
* Quadratic posterior refinement, SHA256
  2834576c2a443c9ffd24032277b5f253d9a85eac17d3f754905812e822a9a331.
* The bound posterior, split-Taylor and correlated affine records in
  that refinement's original provenance chain.

The new [checker](../experiments/check_mixed_terminal_terminal_side_planes.py)
also binds the original integral record and its saved audit, the uniform
face extraction, the passed private-left theorem, all relevant proofs
and checkers, and every inherited current input. Before using values,
it checks the refinement-to-posterior-to-split-to-affine case and
candidate hashes, exact center and response identities, and inclusion
of the refined error radii in the original posterior radii.

Only the saved affine primitive terms \(a\) and \(t+a\) are used.
Their centers, original logarithmic values \(j\), derivatives \(j'\),
full-disk regularity and bounds for \(|g'''|=|j''|\) are retained.
The new whole-tube radii must fit those same multiplier-one full disks.
No derivative is evaluated after clipping a canonical image.

## 2. Exactly one replacement in each existing budget

Form \(P^0_{\mathrm T},D_t,D_a,L_{\mathrm T}\) and the full
Taylor remainder from equations (5)--(10) of the marginal note.
Use exact midpoint anchors \(p_0,L_0\), outward component intervals,
and integer-square-root modulus bounds at a fixed rational mesh
\(2^{-256}\). The complex linear chirp is retained. The center need
not be stationary; no equality with the old ordinary-side center
value is imposed.

Compute the new whole-disk upper \(U_{\mathrm T}\) from equation (11).
If \(U_{\mathrm O}\) is the old saved whole-disk upper, put
\[
 U_{\mathrm{best}}=\min\{U_{\mathrm O},U_{\mathrm T}\}.
 \tag{1}
\]
For every saved whole-disk branch with trial upper \(J_{\mathrm O}\)
and saved vertex gain sums \(G_v\), replace
\[
 J_{\mathrm{best}}=J_{\mathrm O}+U_{\mathrm{best}}-U_{\mathrm O},
 \qquad E_{\mathrm{best}}=\max_v(J_{\mathrm{best}}+G_v).
 \tag{2}
\]
The change is independent of the force vertex. All forces, cubic
costs, center intervals, target intervals and gain witnesses remain
exactly the old ones.

For each of the same 70 original closed source-cell intersections,
compute the new two candidate errors \(\rho_4,\rho_5\) and their
minimum from marginal equation (12). Use the exact coefficient
\(\lambda=L_0/u_a\), requiring \(u_a\ne0\). Equation (13) gives
\(U_{\mathrm T,C}\) by two exact quadratic maximizations, including
clipping the vertex of a concave quadratic. Keep its own new anchors
and error; no old and new midpoint coefficient is interchanged.
Set
\[
 U_{\mathrm{best},C}
   =\min\{U_{\mathrm O,C},U_{\mathrm T,C}\}
 \tag{3}
\]
and apply (2) with that cell's old trial and gain sums. The old
reference-only \(s\)-center narrowing, \(G_H/Q\) refinements and all
force vertices are unchanged. In particular no new scalar
optimization is necessary.

Each old gain upper is checked against the maximum of its stored
branch-value upper endpoints and zero; its force, center, target and
coefficient are checked against the unchanged saved vertex. The old
independent scalar certificates remain inherited. This is a
recombination of their witnesses, not a new verification of the
polynomial optimizer or a gain-helper invocation.

## 3. Coverage, comparisons and preserved outcomes

The two existing covers have 45 and 25 cells. Verify literal cell
and closed-intersection equality with the face extraction, the
saved complete coverage witnesses and all nine source-job associations
per cell. Every new comparison uses the source upper from that same
cell and family. All old and new plane and joined uppers, including
positive bounds and the private-left plane comparison, remain visible.

For each family and Fourier alternative record both complete uniform
routes: the new whole-disk plane plus the old family maximum, and
the maximum of the new cell-plane-plus-same-cell source bounds.
Their minimum is valid, because each bounds the same original
family on the whole reference domain. Record the separate passed
private-left gap \(51/20000\) without replacing or hiding its plane
outcome.

The fixed work is two whole-disk marginal enclosures, 70 existing
cells, 140 exact quadratic endpoint maximizations, 48 inherited
whole-disk vertices and 1,680 inherited cell vertices. There are
3,456 stored gain-witness recombinations and no gain evaluations.
All 1,260 cell family/branch comparisons and 36 uniform family/branch
summaries are retained. There is no root solve, analytic or source
evaluation, new grid, subdivision, optimizer or automatic retry.

An exception or interruption preserves the active cell and every
pending original cell. The fresh output is deterministic gzip with
all witnesses and unchanged-input checks:
repro/results/research-mixed-terminal-terminal-side-planes.json.gz.
A completed calculation is not required to have negative signs.
Source comparisons retain actual \(K_4\) eligibility; the phase
bounds alone hold on \(D_4\). No whole kernel or knot theorem is
claimed by this protocol.
