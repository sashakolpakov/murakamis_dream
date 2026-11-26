# Raising the middle interval with permanent raw right labels

Research theorem, 5 November 2026. The completed local derivative bounds
control the remaining middle interval on the nonlow periodic hybrid.
Together with upper-transition removal, they give an absolute finite-source
gap whenever a right coordinate occurs and no coordinate is in the fixed
near-zero collar. The raw labels remain fixed throughout; no raw kernel
is replaced by a coherent conditional saddle.

## 1. The labelled rate and the fixed positions

Fix a cyclic type word of length \(m\ge1\), its actual original
critical reference \(r\), and a permitted selection \(\sigma\).
Put \(c_j=\Im r_j\), \(H=7/500\), and let \(M\) be the real
part of the original critical action. First work on the alphabet
\[
 [.1,.45]\ \cup\ \{.5\text{ with permanent right label}\}.
 \tag{1}
\]
Let \(\mathcal R\) be its nonempty set of right positions.
Every edge incident to \(\mathcal R\) uses the complete original
raw row envelope. Every other edge uses the original coherent
conditional rate. These are precisely the edge allocations of
[upper-transition removal](research_mixed_nonlow_upper_transition_removal.md),
Section 1. Write their sum as \(\mathcal F_\sigma(x)\), retaining
all actual Fourier alternatives and half-weights. In particular, for
an unselected four-type nonright target the factorial upper rate is
\(-\Re g\); a selected vertex contributes the full correction
\(\max\{\Re g(z),-2\pi\Im z\}\), split between its two incidences.
The right targets are real and remain raw even though their value is
now \(.5\).

Use the hybrid height graph with the two row-dependent left cutoffs.
On (1), every nonright own taper is one and every right height is zero.
Define fixed sets from the initial configuration by
\[
 B=\{j\notin\mathcal R:x_j\in[.1,.12]\},\qquad
 I=\{j\notin\mathcal R\cup B:j-1,j+1\in B\},\qquad
 A=\{1,\ldots,m\}\setminus(\mathcal R\cup B\cup I).
 \tag{2}
\]
The two neighbor incidences in (2) have their literal cyclic meaning.
In particular a right position between two early positions is still
right, not a member of \(I\). Keep \(\mathcal R\cup B\cup I\)
fixed, and raise the coordinates in \(A\) that are below \(.22\)
to \(.22\), by the common minimum-level path
\[
                     x_i(t)=\max\{x_i,t\}\quad(i\in A).
 \tag{3}
\]
All other coordinates remain fixed. If there is no such moving
coordinate, (3) is the identity.

## 2. Exact derivative and complete local coverage

At a nonright vertex define \(G_j\) by the sum of its two incident
complex marginals: the original phase partial on a coherent edge,
and the allocated marginal \(K\) at the unique optimizing real row
on a raw edge. The latter is the
[real-stationary marginal](research_mixed_raw_row_stationarity.md),
not a complex stationary-point substitution. Its real directional
contribution is \(\Re(G_j\,dz_j)\).

The selected corrections are constant along (3). A moving selected
coordinate has real part in \([.12,.22]\), constant height in
\([0,H]\), and its true correction is \(-2\pi h_j\), by the
[proved strip inequality](research_mixed_early_selected_transport.md),
equation (5). A nonmoving selected coordinate has both coordinates
fixed. Define
\[
 d_j=\begin{cases}
 c_j,&j\notin\mathcal R,\ \sigma_j=0,\ N(j)\cap B=\varnothing,\\
 0,&\text{otherwise},
 \end{cases}
 \qquad N(j)=\{j-1,j,j+1\}.
 \tag{4}
\]
Every selected height is fixed because all moving fast cutoffs are
already one. Every unselected neighborhood meeting \(B\) is also
fixed, since its early cutoff is no larger than any moving cutoff.
A neighborhood disjoint from \(B\) contains no fixed isolated
position of \(I\): such a position has both neighbors in \(B\).
Thus a responsive height has derivative \(d_j/.12\) exactly when
its neighborhood meets the currently moving set, counted once per
physical vertex.

For a currently moving minimum \(i\in A\), put
\[
 D_i=\Re G_i+
       \sum_{\substack{j\in(i-1,i,i+1)\\j\notin\mathcal R}}
              \min\{-d_j\Im G_j/.12,0\}.
 \tag{5}
\]
The sum in (5) retains cyclic multiplicity. The following list
exhausts the local possibilities.

**No early neighbor of the center.** The center is in one of the old
unselected states \(z_i=t+ic_i\rho(t)\), or is selected with
\(z_i=t+iH\), where \(\rho(t)=(t-.1)/.12\). Each side has
one of these forms:

| Examined side | Completed local input |
|---|---|
| Neighbor right | [Immediate-right half](research_mixed_immediate_right_half.md), Theorem 1. |
| Neighbor nonright with responsive height; its outer neighbor right | [Conditioned distance-two half](research_mixed_distance_two_right_halves.md), lower real piece. |
| Neighbor nonright with zero height velocity because it is selected or fixed by an early outer position | The old [192 unselected](research_mixed_minimum_level_half_stencils.md), [78 selected](research_mixed_constant_selected_height_transport.md) and [50 frozen-height](research_mixed_frozen_outer_half_stencils.md) domains, as appropriate. If its outer position is right, the zero-switch cases of the conditioned distance-two theorem also apply. |
| Neighbor nonright with responsive height; outer neighbor nonright | The same 192/78/50 domains, including a selected or early-frozen outer height. |

Here any responsive nonright neighbor and all its relevant non-early
outer real coordinates are at least \(t\) and at most \(.45\).
A fixed \(I\) position cannot occur in a responsive neighborhood.
The old frozen-height domains include the extra partial selected
heights caused by an early position one step farther out.
These facts verify the full domain hypotheses in the table; the old
half theorem is not extended to a missing upper-taper argument.

Use a **shared** center switch \(\chi\in\{0,1\}\) in both
halves, and separate neighbor switches. The old imaginary gauges
\(\pm i\kappa\), \(\kappa=3/2\), and selected real gauges
\(\pm\sigma_i/10\) cancel at that same switch. Minimizing over
this shared switch and the neighbor switches gives exactly (5).
It would be invalid to minimize the two gauged center contributions
with unrelated switches. Each cited half is positive at every
required switch, so \(D_i\ge0\).

**Exactly one early neighbor.** A moving center has at most one,
since the positions between two early neighbors lie in \(I\).
Its height is fixed in the corresponding band
\[
 [-.005,1/300],\qquad[-.0095,0],\qquad[0,.014]
 \tag{6}
\]
for \(U_3,U_4,S_4\), respectively. Retain the old early half of
[one-early transport](research_mixed_one_early_neighbor_transport.md).
The other half is supplied by that same theorem if the next outer
position is nonright, and by the
[frozen-center distance-two theorem](research_mixed_frozen_center_distance_two_right_halves.md)
if that position is right. In the latter case its 240 complete
domains use the actual compensation of the early half.
If the immediate non-early neighbor itself is right, use instead
Section 4 of the immediate-right note. Its unrounded scalar bounds
for the bare horizontal raw marginal \(O\) are
\[
 O>.37\quad(3),\qquad O>.25\quad(4\text{ unselected}),
 \qquad O>.23\quad(4\text{ selected}).
 \tag{7}
\]
The last bound is equation (16) before subtracting the selected
\(.1\) gauge. All Fourier choices obey it. Consequently these
bare bounds pay the actual early compensation:
\[
 O-.2>.03\quad\text{when the early neighbor is left},\qquad
 O+4|h_i|-.053>.177\quad\text{when it is right},
 \tag{8}
\]
for a four-type center. Type three needs no compensation.
The early and non-early adjustments cancel exactly; the unfrozen
selected \(\pm.1\) gauges are not substituted for them.
This proves \(D_i\ge0\) also with one early neighbor.

All entries above concern actual reference coefficients, with the
conditioned geometry required by the new right-half certificates.
If the same cyclic position appears twice, it is specialized to the
same actual coefficient, not assigned two independent physical
height velocities.

## 3. Ties, repeated incidences and transport

Let \(J(t)\subset A\) be the set moving at level \(t\).
The full envelope is locally Lipschitz and piecewise smooth on this
compact domain. The raw optimizer is unique and smooth on each
relevant target domain. Its real stationarity gives the stated
marginals; selected ties at stationary vertices do not affect the
path derivative. Almost everywhere,
\[
 \frac{d}{dt}\mathcal F_\sigma(x(t))
 =\sum_{i\in J(t)}\Re G_i
  +\sum_{\substack{j\notin\mathcal R:\,N(j)\cap J(t)\ne\varnothing}}
                     -d_j\Im G_j/.12
 \ \ge\ \sum_{i\in J(t)}D_i\ \ge0.
 \tag{9}
\]
Each negative height term on the left is counted at least once on
the right, possibly more often, while positive terms may be omitted.
This proves the inequality even at a repeated neighbor incidence;
it does not count the actual height derivative more than once.
Absolute continuity integrates (9). If \(x^\sharp\) is the
endpoint of (3), then
\[
                \mathcal F_\sigma(x)\le\mathcal F_\sigma(x^\sharp).
 \tag{10}
\]

For \(m=2\), a nonright position with an early neighbor has both
early incidences and belongs to \(I\), so it is fixed. A nonright
position opposite a right one has two immediate raw incidences; the
two distinct edges and their gauges are retained. In a three-cycle
an early position can freeze the other neighbor as well; its zero
velocity uses the old switch-zero domain, never an active raw term.
For \(m=1\) and nonempty \(\mathcal R\), the only position is
right and no transport occurs. These conventions exhaust the short
cycles without adding a four-distinct-position assumption.

## 4. A rate gap at the endpoint

At \(x^\sharp\), all positions in \(A\) lie in
\(P=[.22,.45]\). A fixed position of \(I\) is counted as P
only for the incidence argument. Both of its incident edges meet
\(B\), and its real coordinate remains in \([.12,.45]\).
Thus it has no PP or PR edge. Its two actual early edges are covered
by the stronger early-block theorem, which permits the other real
coordinate throughout \([.1,.45]\). All height bands and the
single-use credit allocation are unchanged.

If \(B\ne\varnothing\), Section 3 and equation (11) of the
[early/plateau/right rate assembly](research_mixed_early_plateau_right_clusters.md)
therefore give
\[
                  \mathcal F_\sigma(x^\sharp)\le M-n_B/1000,
 \tag{11}
\]
where \(n_B\ge1\) counts original edges incident to \(B\).
This uses that note's unrounded rate comparisons, not an inference
from its rounded finite integral bound.

If \(B=\varnothing\), then \(I=\varnothing\) and the endpoint
is the **independent** P/R graph: plateau heights are prescribed,
because a right neighbor has left cutoff one. At right target
\(.5\), the [core source comparison](research_mixed_right_core_support.md),
Theorem 1 and its full-row reductions, gives raw PR/RP defect
at most \(-1/500\). The [two-right comparison](research_mixed_two_right_source_bound.md)
gives raw RR defect at most \(-1/50\). An unselected PP edge
has nonpositive coherent defect by plateau concavity; a selected
PP edge has branch defect below \(-1/100\) by equation (11) of
[the selected-plateau theorem](research_mixed_selected_plateau_support.md).
These are the underlying rate inequalities before Fourier tolerance.
The reset graph of the older plateau/right run theorem is not used.
Since a right position exists, there is at least one right-incident
edge, including an all-right loop. The original complex tangent
terms cancel by cyclic criticality, giving
\[
                  \mathcal F_\sigma(x^\sharp)\le M-1/500.
 \tag{12}
\]
Combining (10)--(12) proves the uniform rate conclusion
\[
                       \boxed{\mathcal F_\sigma(x)\le M-1/1000.}
 \tag{13}
\]

## 5. Original finite source and the remaining collar

**Theorem 1.** For every fixed cyclic three/four word, every permitted
selection and every nonlow hybrid configuration in \([.1,1]^m\)
with a nonempty original right set, its complete mixed upper rate is
at most \(M-1/1000\). Its original allocated finite density, including
the fixed scalar normalization and graph Jacobian at every graph
differentiability point (hence almost everywhere), satisfies an
absolute bound
\[
 C_mN^{A_m}\exp\{N(M-1/2000)\}.\tag{14}
\]
The corresponding restricted integral and the sum over selections
satisfy the same bound, with adjusted prefactors.

Indeed first use upper-transition removal with its permanent right
labels. Its exact rate comparison sends the configuration to (1),
possibly erasing upper selections, without increasing the rate.
Then apply (13). Every coherent edge stays in a completed compact
cap, plateau or right-transition source product; every raw edge
retains all finite rows, both parity cases and its actual Fourier
halves. Use these complete source upper bounds with one total
tolerance strictly below \(1/2000\) over all physical edges.
No previously rounded finite gap is spent again. The powers of
\(N\), finite selections and bounded fixed-contour Jacobian cost
only a prefactor. No lower bound or nonvanishing claim for an
individual raw kernel is used.

**Corollary 2.** Fix any admissible hybrid collar width
\(0<\rho\le.001\), independent of \(N\), below the inherited
endpoint-thickening radius. The same rate bound (13) and finite
bound (14) hold on
\[
 [\rho,1]^m\cap\{\text{at least one original coordinate is in }[.5,1]\}.
 \tag{15}
\]
The [exact low-transport theorem](research_mixed_exact_low_transport.md),
Section 3, first fixes right angles at \(.5\) and raises every
other coordinate in \([\rho,.1]\) to \(.1\), without increasing
the same R-priority rate. All heights are unchanged, both low cutoffs
stay zero, and the underlying complete real source is uniform for
this fixed positive \(\rho\). Apply Theorem 1 to the result.
This is a rate comparison followed by the same single tolerance,
not an additional finite-source loss.

The collar is not sent to zero. Configurations with both an original
right coordinate and some coordinate in \([0,\rho)\) remain outside
this theorem. The closed-half contribution is controlled separately;
no full-period noncancellation, new knot family, or arbitrary-short
filling stability is inferred here.
