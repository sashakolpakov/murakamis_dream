# Occupation loss retained through the full-period comparisons

Research deduction, 5 November 2026. This retains unused losses in
the completed pointwise comparisons. It uses no new source cover.
The resulting rate inequality is also valid for safe compact
perturbations of an actual open reference. It is not a global
open-source asymptotic.

## 1. A penalty preserved by the completed moves

Use the original cyclic reference, or a safe compact perturbation
of an actual open reference as in
[the boundary comparison reduction](research_mixed_open_boundary_comparison_reduction.md).
For a cycle let \(I\) be its full vertex set. In the open case,
let \(I\) be the safe ordinary-symbol interval containing every
nonbaseline symbol; all symbols outside \(I\) remain unchanged.
Write \(a_j=\Re r_j\), so every reference in \(I\) satisfies
\(.27<a_j<.39\), and put
\[
 P=[.22,.45],\qquad
 y_j=\max\{.22,\min\{x_j,.45\}\},\qquad
 p_j=\begin{cases}
 \min\{1,\sigma_j+400(y_j-a_j)^2\},&j\in I,\\
 0,&j\notin I,
 \end{cases}\qquad
 \kappa=\frac1{20000}.                                  \tag{1}
\]
Selections are the original allowed selections. Within \(I\),
\(p_j=1\) whenever a symbol is selected or lies outside \(P\),
and \(p_j=0\) only at the unselected reference symbol.
Indeed the two plateau
endpoint distances are greater than \(.05\) and \(.06\).
In the open case zero penalty outside \(I\) is part of the
definition; it is not inferred from an unrefined private endpoint
rectangle or from a nonexistent ordinary endpoint incidence.

Use the same complete allocated mixed upper envelope as in
[the full cyclic theorem](research_mixed_full_cyclic_period.md):
collar profiles have priority, remaining right-incident edges retain
their absolute row envelopes, and every coherent edge keeps both
true Fourier alternatives. Tangents are always the original
\(\Gamma_j\).

All completed real-coordinate moves preserve \(p_j\): clamping a
right coordinate to \(.5\), raising a nonseam deep low to \(.1\),
clamping an upper transition to \(.45\), and raising a middle
coordinate to \(.22\) do not change its plateau clamp in (1).
Selections are erased in an upper transition only where \(p_j=1\)
already follows from the real coordinate, so this also preserves the
penalty. A fixed coordinate between two early positions is not moved.

The only exception is a seam replacement: its original penalty is one,
and replacement by its unselected reference makes it zero. The
[seam comparison with raw exterior edges](research_mixed_seam_raw_exterior_repair.md)
retains an original rate reserve \(3/1000\) per replaced seam.
The closed-half run argument supplies the same reserve when there is
no raw right label. Therefore this deletion costs at most \(\kappa\)
and leaves positive reserve. No neighboring penalty changes in a seam
replacement; neighboring heights may change, but (1) depends only
on their real coordinates and selections.

## 2. Retain the clean edge losses at the endpoint

After these comparisons, the nonseam configuration consists of early
positions \(E\), prescribed plateau positions \(P\), and permanent
raw right positions at \(.5\). Positions between two early neighbors
may remain fixed off \(P\); both their edges are early edges, as
in the completed minimum-level argument. They play no role in a PP
or PR edge.

Let \(n_E\) count original edges incident to \(E\). Call a
right-incident edge *clean* if it is RR, or is PR/RP and its plateau
endpoint has no early neighbor. Let \(n_C\) be their number.
The [early/plateau/right charge proof](research_mixed_early_plateau_right_clusters.md),
Section 3, retains
\[
 \sum_j w_j\le-\frac{n_E}{1000}-\frac{n_C}{500}
                                      -\sum_{j\in\mathcal P_c}L_j.\tag{2}
\]
Here \(\mathcal P_c\) consists of PP edges with no affected
endpoint, and one may retain any available nonnegative loss \(L_j\)
on them. This strengthened reading spends no credit twice:

* The old incidence calculation already pays every affected PR edge
  and all changed PP endpoints and leaves \(n_E/1000\).
* A clean PR edge has its prescribed selected or unselected height.
  Its complete right-core margin is \(1/500\), as used before
  finite tolerance in Section 4 of
  [middle-interval transport](research_mixed_nonlow_middle_transport.md).
  It receives no early credit.
* Every RR edge has the larger complete raw reserve \(1/50\);
  retaining only \(1/500\) in (2) is safe.
* A clean PP edge has no changed incidence and uses no early credit.
  Its original negative defect was discarded in the older bound and
  can be retained here.

For an unselected clean PP edge which is not identically at baseline,
its safe reference window permits the
[extracted plateau curvature](research_mixed_extracted_plateau_curvature.md)
bound
\[
 L_j\ge\frac1{10}\{(y_{j-1}-a_{j-1})^2+(y_j-a_j)^2\}.
                                                               \tag{3}
\]
If either endpoint is selected, the true selected plateau loss is
at least \(1/100\). In either case a clean PP edge assigned to
its right vertex \(j\) supplies
\[
                              L_j\ge\frac{p_j}{4000}.     \tag{4}
\]
For a selection erased above \(.45\), the final coordinate is
\(.45\), and \(400(.45-a_j)^2>1\); thus (4) still pays its
original penalty one. All other non-early, non-isolated coordinates
end at the original clamp \(y_j\).
Unchanged baseline edges have defect zero and pay a zero assigned
penalty directly; no plateau certificate is applied to an unrefined
open endpoint window.

## 3. A length-independent incidence count

For a set of vertices \(A\), let \(N_d(A)\) mean graph distance
at most \(d\), counting distinct physical vertices. Put
\[
                              Z=N_2(E)\cup N_1(R).         \tag{5}
\]
If \(j\notin Z\) has nonzero penalty, then \(j\in I\)
and its own incoming ordinary edge \(j\) is clean PP.
Its four-symbol height window avoids \(E\), and neither endpoint
is right. It cannot meet a frozen position between two early
neighbors. Assign that edge to \(j\); this is injective.

Every right vertex outside \(N_2(E)\) has two clean right
incidences. Each clean edge accounts for at most two such vertices,
so
\[
 |R\setminus N_2(E)|\le n_C,\qquad
 |R\cap N_2(E)|\le4|E|,\qquad |E|\le n_E.
\]
Consequently
\[
             |R|\le n_C+4n_E,\qquad
             |Z|\le5|E|+3|R|\le17n_E+3n_C.              \tag{6}
\]
These are degree-two incidence statements. A loop has two incidences
but is one edge; parallel edges in a two-cycle remain two original
edges. The inequalities also hold for finite perturbed runs surrounded
by baseline plateau vertices. No periodic reference is needed for
these counts.

Since \(0\le p_j\le1\), the exact rational comparisons
\[
 \frac{17}{20000}<\frac1{1000},\qquad
 \frac3{20000}<\frac1{500},\qquad
 \frac1{20000}<\frac1{4000}                              \tag{7}
\]
show that (2) pays \(\kappa\sum_{j\in Z}p_j\), while the
injectively assigned clean PP edges pay every remaining penalty.
The penalties preserved during transport are the original ones.
Each removed seam penalty is paid separately by its unused
\(3/1000\) reserve.

**Theorem 1.** On the complete periodic hybrid upper envelope,
for every original real configuration and every allowed selection,
\[
             \sum_j w_j\le-\frac1{20000}\sum_j p_j.       \tag{8}
\]
On a cycle the left side is the original complete mixed upper rate
minus its critical action. On a safe compact perturbation of an
actual open reference it is the same tangent-subtracted defect sum.
All original sources, right labels, collar profiles and Fourier
alternatives remain present. Equation (8) is a rate statement; it
does not spend a new finite-source tolerance near the zero of the
penalty.

## 4. Boundary-compatible use

Use the synthetic configuration and exact six-edge closing terms
from the boundary comparison reduction. The theorem gives the
additional lower bound
\[
 D_{p,q}\ge\kappa\sum_{j=p-2}^{q+1}p_j,
 \qquad
 \text{open upper rate}-M_{\mathrm{open}}
 \le\mathcal B_L+\mathcal B_R
                   -\kappa\sum_{j=p-2}^{q+1}p_j.         \tag{9}
\]
The closing constants and the two original tangents in
\(\mathcal B_L,\mathcal B_R\) are unchanged. The sum counts
each physical retained symbol once even when the terminal triples
overlap. On an unselected plateau corridor one can instead retain
the stronger optimized Dirichlet loss already described there.

This carries positive middle loss through the completed full-period
transport without imposing an artificial condition
\(\mathcal B_L\le0\) on each fixed-baseline closure separately.
It supplies the occupation input for a possible full-alphabet finite
message argument. Such a message must still be constructed for the
actual open reference and compared with the literal endpoint sources;
the old periodic potential is not being substituted for it. No sign
for the full right side of (9), global open-source asymptotic, boundary
strip theorem, marked volume identity or short-filling conclusion is
claimed here.
