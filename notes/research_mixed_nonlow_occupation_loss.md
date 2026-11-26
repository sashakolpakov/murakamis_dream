# Additive losses for departures from the geometric plateau

Research deduction, 5 November 2026. All numerical and source inputs
below are already proved. The new step
retains the losses on unaffected edges in the existing early-region
charge argument. No additional interval cover is used.

Use the original periodic word, geometric reference \(r\), true rate
\(\mathcal E_S\), hybrid targets and local residual weights \(w_j\)
from [the open-chain boundary deduction](research_mixed_nonlow_open_chain_boundary.md).
Thus \(\sum_jw_j=\mathcal E_S-M\) exactly on every cycle, with
both selected Fourier alternatives retained. Write
\[
 a_j=\Re r_j,\qquad P=[.22,.45],\qquad
 y_j=\max\{.22,\min\{x_j,.45\}\},\qquad .27<a_j<.39.
                                                               \tag{1}
\]
The clamp in (1) includes both endpoints of the plateau.

## 1. The unselected case without early coordinates

Suppose \(S=\varnothing\) and every \(x_j\in[.12,.5]\).
The completed right-clamping comparison first replaces every coordinate
above .45 by .45, with additive phase gain at least
\(\frac1{10}\sum_j(x_j-.45)_+\). It changes no other row height.
The completed minimum-coordinate inequalities then raise all coordinates
below .22 together, ending exactly at \(y\). This second operation
does not decrease the phase.

Let \(\mu>0\) be the uniform plateau Hessian constant. Stationarity
and fixed-height concavity give the precise bound
\[
 \mathcal E_\varnothing(x)
 \le M-\frac\mu2\sum_j(y_j-a_j)^2
          -\frac1{10}\sum_j(x_j-.45)_+.                     \tag{2}
\]
The [plateau accretivity theorem](research_mixed_plateau_accretivity.md),
equation (12), permits the explicit choice \(\mu=1/2000\).
The transport inequalities used here are the now-completed inputs of
the [full left-region proof](research_mixed_full_left_region.md).
In particular, (2) is a pointwise phase inequality, not an inference
from an integrated bound.

## 2. Losses that remain after the early-region charges

Here and below, an edge \(j\) joins vertices \(j-1,j\). The
full cyclic indexing is retained for lengths one and two.

For an unselected plateau edge at its two reference heights, the
local phase satisfies
\[
 \Re\{\phi_j(u+i\Im r)-\Gamma_j(u+i\Im r)\}
 \le-\frac{(u_{j-1}-a_{j-1})^2+(u_j-a_j)^2}{8000}.
                                                               \tag{3}
\]
To see the constant directly, each of the two triangle forms in the
plateau proof has negative real Hessian at least \(I_2/4000\).
Their sum, with the nonnegative extra factorial terms, gives this
lower bound on both outer directions of the full three-variable
Hessian. The complex Schur identity preserves it on the condensed
outer Hessian. Taylor's formula at the reference, after subtracting
its full tangent, proves (3). The target-reference displacement in
(3) is real, so no curved-contour derivative is being used.

If at least one endpoint is selected at its full height \(H=.014\)
and the other has its prescribed selected or unselected height, the
[selected plateau comparison](research_mixed_selected_plateau_support.md),
equation (11), gives instead
\[
                 \text{true local residual}<-1/100.          \tag{4}
\]
This is the phase comparison before its finite-source tolerance.
It holds separately for each forcing branch.

We will use (3)--(4) without spending any early credit on these edges.
The following strengthened reading of the existing early argument is
therefore needed.

**Lemma 1.** Let \(B\) be a set of early vertices, with their real
coordinates in \([.1,.12]\). Keep the intervening isolated vertices
\[
 I=\{j\notin B:j-1\in B,\ j+1\in B\}
\]
fixed, and suppose all other vertices are on \(P\). Let \(n_B\)
count original edges incident to \(B\). On every plateau edge whose
four-coordinate window \(j-2,\ldots,j+1\) avoids \(B\), retain
any available loss \(L_j\ge0\) from (3) or (4). Then
\[
                \mathcal E_S\le M-\frac{n_B}{1000}
                                      -\sum_j L_j.           \tag{5}
\]
For \(B=\varnothing\), the same conclusion holds with \(n_B=0\).

**Proof.** The
[early/plateau charge proof](research_mixed_early_plateau_clusters.md),
Section 2, assigns each changed plateau incidence a credit from its
unique adjacent early/plateau edge. Each early edge supplies loss
\(1/100\). A doubly changed plateau edge consumes at most the two
credits plus \(33651/2000000\); their number \(d\) satisfies
\(2d\le n_B\). Before discarding any unaffected negative deficits,
that proof therefore gives
\[
 -\frac{n_B}{100}+\frac{33651}{2000000}d
 \le-\frac{6349}{4000000}n_B\le-\frac{n_B}{1000}.             \tag{6}
\]
An edge whose four-coordinate window avoids \(B\) is an unchanged
plateau edge. Neither its own phase loss nor an early credit assigned
to it is used in (6): it has no changed incidence at all. Thus its
additional negative deficit \(-L_j\) can be retained in the sum.
If an isolated vertex in \(I\) is not on the plateau, both its edges
are early; it has no plateau/plateau incidence. This is exactly the
extension in Section 2 of the
[fixed-early transport proof](research_mixed_frozen_early_transport.md).
It changes neither the credits nor (6). Loops and parallel incidences
are treated in that charge proof as original edges, so the conclusion
also holds for lengths one and two. If \(B\) is empty, all edges are
unchanged plateau edges and one sums their direct support inequalities.
\(\square\)

## 3. A uniform occupation penalty for every selection

Define the continuous one-symbol penalty
\[
 p_j(x_j,\sigma_j)
   =\min\{1,\ \sigma_j+400(y_j-a_j)^2\},\qquad
 \kappa=\frac1{3200000},\qquad
 \omega_j=\kappa p_j+\frac1{10}(x_j-.45)_+.                  \tag{7}
\]
Continuity refers to the ordinary real-coordinate topology and the
discrete topology on selections. The penalty vanishes at each
unselected geometric reference symbol. It equals one in its \(p_j\)
part whenever \(\sigma_j=1\) or \(x_j\notin P\): if
\(x_j<.22\), then \(|y_j-a_j|>.05\), while if
\(x_j>.45\), then \(|y_j-a_j|>.06\).

**Theorem 2.** For every finite cyclic word, every real target in
\([.1,.5]^m\), and every original selection,
\[
                  \mathcal E_S(x)\le M-\sum_{j=1}^m\omega_j.
                                                               \tag{8}
\]
The coefficient in (7) is independent of the word and its length.

**Proof.** Apply the selected-height removal at each selected coordinate
above .45 and then the unselected right clamp. These are the completed
pointwise comparisons used in the
[nonlow-half theorem](research_mixed_full_nonlow_half_region.md),
Section 3. They change no other row heights and retain the full gain
\(\frac1{10}\sum_j(x_j-.45)_+\). A selection is removed only
at a coordinate originally above .45.

Put \(B=\{j:x_j\le.12\}\), unchanged by this first operation.
Use the now-proved fixed-early transport, leaving \(B\cup I\)
fixed and raising every other coordinate below .22 to .22. The full
true rate is nondecreasing during this transport. All its local
hypotheses are precisely the completed 192, 78, 50 and 175 families
in the full left-region theorem; no new derivative assertion is used.
If \(B\) is empty, this is the ordinary minimum transport.

Let \(N_2(B)\) be the union of vertices at cyclic graph distance at
most two from \(B\). Count distinct vertices in this union, so
\[
                |N_2(B)|\le5|B|\le5n_B.                    \tag{9}
\]
For \(j\notin N_2(B)\), edge \(j\) has no early vertex in
its four-coordinate window. None of those coordinates is a fixed
isolated vertex either. Its endpoints and both neighboring rows are
therefore at their full plateau heights after transport, and the
center real coordinate is exactly \(y_j\) from (1).

Assign this edge to vertex \(j\). This assignment is injective:
each original edge is assigned at most once, also for a loop or a
two-cycle. If the edge still has a selected endpoint, (4) supplies
loss at least \(p_j/100\ge\kappa p_j\). Otherwise (3) supplies
loss at least \((y_j-a_j)^2/8000\). If the original center was
unselected, then \(p_j\le400(y_j-a_j)^2\), so this also exceeds
\(\kappa p_j\). If it was selected but is now unselected, its
original coordinate was above .45. In that case \(p_j=1\) and
\[
 \frac{(y_j-a_j)^2}{8000}
 >\frac{(.06)^2}{8000}>
                          \frac1{3200000}=\kappa.           \tag{10}
\]
Thus the clean edge assigned to each vertex outside \(N_2(B)\)
provides at least \(\kappa p_j\).

For the remaining vertices, \(p_j\le1\), and (9) gives
\[
 \kappa\sum_{j\in N_2(B)}p_j
       \le5\kappa n_B=\frac{n_B}{640000}
       \le\frac{n_B}{1000}.                                \tag{11}
\]
Lemma 1 retains all assigned clean-edge losses in addition to the
early reserve. Equations (10)--(11) therefore bound the endpoint rate
by \(M-\kappa\sum p_j\). Adding the already retained right-clamp
gain proves (8). Every count uses vertices and original edges with
their literal cyclic multiplicities; (9) is still an upper bound when
indices repeat. This proves the assertion for \(m=1,2\) as well.
\(\square\)

In particular, if
\[
 n_{\rm bad}=\#\{j:\sigma_j=1\ \text{or}\ x_j\notin P\},
\]
then \(\mathcal E_S\le M-\kappa n_{\rm bad}\). Equation (8)
also penalizes unselected plateau coordinates away from their own
geometric real reference; it is stronger than this count alone.

## 4. Weighted open chains and their exact boundary terms

The modified local weights
\(\widehat w_j=w_j+\omega_j(q_j)\) have the same four-symbol
dependence as \(w_j\), are continuous, and vanish on the reference
baseline. Equation (8) says that every closed walk in the layered
state space has nonpositive modified weight. Thus the open-chain
closure and potential theorems apply to \(\widehat w\).

There is a useful exact form using the *original* six boundary terms.
For a path with weights \(j=a,\ldots,b-1\), its prescribed symbol
halo is \(q_{a-2},\ldots,q_b\). The three exit weights add only
\(\omega_b\), and the three entry weights add only
\(\omega_{a-2}+\omega_{a-1}\), since all other centers in those
closing transitions are baseline. Consequently
\[
 \boxed{\quad
 \sum_{j=a}^{b-1}w_j+
        \sum_{j=a-2}^{b}\omega_j(q_j)
             \le-A_a(v)-E_b(v').
 \quad}                                                     \tag{12}
\]
The same explicit six original-phase functions from the boundary note
occur on the right. No extra penalty proportional to the length or
the period was introduced by closing the chain.

The anchored potential \(\widehat{\mathcal H}\) is continuous,
zero at all reference states, and satisfies
\[
 w(v\to v')+\omega_i(q_i)
       \le\widehat{\mathcal H}(v')-\widehat{\mathcal H}(v).
                                                               \tag{13}
\]
Its entry and exit brackets are respectively
\(A_i+\omega_{i-2}+\omega_{i-1}\) and
\(-E_i-\omega_i\). Since the added penalties are nonnegative,
these brackets still imply
\(|\widehat{\mathcal H}|\le3K_*\), with the original compact
constant \(K_*\) from the boundary note.

For example, an open path whose original residual is at least \(-B\)
has, throughout its prescribed halo,
\[
       n_{\rm bad}\le\frac{6K_*+B}{\kappa}.                 \tag{14}
\]
This is a length-independent bound on departures in a near-optimal
path. The constant \(K_*\) has not been numerically evaluated, so
(14) is not an effective small list of configurations. Nor does it
pay a new endpoint factor or prove domination of the unestimated
parts of the full periodic contour.

Finally, the original finite-source upper bound follows from (8) or
(12) with any single prescribed positive tolerance, distributed among
the finitely many blocks. The same complete conditional sources and
actual Fourier polynomials are used. Constants and large-level
thresholds may depend on the fixed chain length. No uniform joint
limit in the word length and level, no open-chain lower asymptotic,
and no new knot-volume theorem are asserted.
