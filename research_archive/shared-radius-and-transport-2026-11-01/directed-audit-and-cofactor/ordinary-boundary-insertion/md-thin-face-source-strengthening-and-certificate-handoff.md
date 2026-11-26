# Ordinary triangular insertion: strengthened source proof and certificate handoff

This addendum preserves the stronger argument after the first independent thin-face report. The earlier report remains a historical proof with unnecessary middle-order assumptions. The present argument removes those assumptions. The public runner checks only the finite inequalities and incidences stated below; it does not replace the source, geometric, or asymptotic arguments.

## Exact sector comparison and target correction

Write the two original ordered quartets as
\[
e_D=(u,v,c,b),\qquad e_B=(u,a,v,b),
\]
with oppositely oriented removed triangles \((u,v,b)\) and \((u,b,v)\). The surviving pair is \((u,a,c,b)\). Put
\[
T=Q(u,v,b),\quad Q_a=Q(u,a,b),\quad Q_c=Q(u,c,b),\quad
\Delta=2T-\log b\ge0.
\]
The block expression subtracts its interior targets and one target at \(b\), but no targets at \(u,v\). The core supplies the sole targets at \(u,v\). Thus adding the two input expressions duplicates precisely the target at \(b\), while the triangle sum includes the two removed triangles. The correction is exactly \(-\Delta\).

The actual label map is
\[
C\mapsto(C,C),\qquad L\mapsto(L,C),\qquad R\mapsto(C,R).
\]
For the left label, subtracting the two removed triangle actions gives
\[
\max\{\log c+Q_a-T,\;Q_a+\tfrac12\log c\}.
\]
The output left rate is \(\max\{\log c,Q_a+\frac12\log c\}\), so the loss is at most \((T-Q_a)_+\). The right calculation exchanges \(a,c\). Hence
\[
\varepsilon_C=0,\qquad \varepsilon_L=(T-Q_a)_+,\qquad
\varepsilon_R=(T-Q_c)_+\le\Delta/2,
\]
where the last bound for both sides uses the vertex allocation \(Q_a,Q_c\ge\frac12\log b\).

Now classify the **entire induced block string**, not only its root. If that string is central, its conditional packing has value \(\Phi_B+\Delta\). Every interior packing disk lies in the bounded interstice of the three boundary disks, so its curvature is at least
\[
u+v+b+2\sqrt{uv+ub+vb}>v.
\]
In particular \(a>v\), giving \(Q_a\ge T\). The central block root allows only a central or left output bridge; both then have zero defect. Its \(+\Delta\) cancels the correction exactly.

If the induced whole block string is noncentral, use a witness of value at most \(\Phi_B-\Gamma_B\). Its possible bridge error is at most \(\Delta/2\). After correction its total is therefore at most \(\Phi_B-\Gamma_B-\Delta/2\). There is no condition on \(a\) at this witness, and no condition on the core middle \(c\).

Every noncentral output induces a noncentral core or block string. The assembled gap is at least the minimum of their certified gaps. This proof adds for any fixed finite number of insertions at distinct matching pairs. Boundary vertices may be shared: every duplicated \(b\)-target has its own cancellation, whereas each core coordinate still has only one actual target. Fresh block interiors are disjoint.

## Forty old branches and five new anchors

The old seventeen-region source has protected vertices \(0,16\), ordinary root boundary \(17\), and root quartet \((16,14,0,17)\). Normalize each of its forty rational witness vectors by its own weight at vertex 17. Set
\[
w_{16}=2/b_n,\qquad w_0=1/b_n,\qquad w_{17}=1,
\quad b_n=3n^2+4\sqrt2\,n+2.
\]
All old interior coordinates remain the same rational positive numbers.

For positive weights, the vertex allocation implies
\[
A_L\le\max(X,\log c),\quad A_R\le\max(X,\log b).
\]
Consequently \(H=\max(X,\log b,\log c)\) bounds every genuine local label, and \(\max(X,\log c)\) bounds labels \(C,L\). These are exactly the spectator bounds used by the old branches. The first fifteen branches choose the nonempty subset of right labels among regions \(2,4,7,12\). The remaining twenty-five branches choose a surviving one-sided anchor when none of those four right labels occurs. The runner reconstructs this list symbolically and compares it with the stored certificate.

Deprotection additionally permits precisely
\[
(0,R,0),\quad(1,R,0),\quad(12,L,16),\quad(15,L,0),\quad(16,L,0),
\]
where each triple records the region, label, and newly positive overloaded vertex. For each of these five possibilities use the first normalized old witness, retain its selected one-sided rate, and bound every other local factor by \(H\). A newly allowed string either uses only old allowed labels and belongs to the forty old branches, or contains one of these five anchors. This covers every locally allowed noncentral string, including strings with globally vanishing coefficients. It is not an enumeration only of sectors observed at finitely many levels.

At \(n=2^{20}\), outward interval arithmetic verifies every one of these forty-five costs is less than the rational feasible complete entropy minus \(0.02\). The feasible entropy is a lower bound for the exact protected complete action \(\Phi_B\), so the same gap holds relative to \(\Phi_B\). No numerical packing solve is used.

Every witness rate is nondecreasing in each boundary weight: the triangle rates, logarithms, and their maxima have that property. There is no negative block target term at either boundary vertex. Since \(b_n\) increases, the certificate consequently holds for **every larger even \(n\)**. This conclusion uses monotonicity, not a finite chain-length sweep.

## Uniform core gap

The explicit even zigzag has the exact curvature formula above and decreasing ratios \(b_j/b_{j-1}\). Put \(g=f(1/4)\), \(b_1=5+4\sqrt2\), and \(b_2=14+8\sqrt2\). The three pure-middle margins are bounded below by
\[
2g-\tfrac34\log2,
\]
\[
2f(1/12)+f(1/3)+2f(1/5)+f(1/10)
 +\tfrac{17}{30}\log2-\tfrac23\log b_1,
\]
\[
4g-\tfrac14\log\frac{b_2^3}{2b_1^2}.
\]
All exceed \(0.06\); the last two exceed \(0.25\) and \(0.09\), respectively. The terminal pure margin is at least \(2g\).

To pass from pure margins to actual one-sided labels, use
\[
X-A_L=\min\{X-\log c,\ Q_c-\tfrac12\log c\},
\]
and its right analogue. Quarter allocations and vertex allocations give, according to the region,
\[
2g-\tfrac14\log2,\qquad
2g+\tfrac14\log(2/b_1),\qquad
2g-\tfrac14\log(b_2/b_1),\qquad
\tfrac12\log2,\qquad 2g.
\]
All exceed \(0.06\). The ratio monotonicity makes these bounds independent of the chain length. Hence the one complete vector certifies **every** noncentral core string with gap greater than \(0.06\), at every positive even length. Protected joins of finitely many such cores retain the minimum gap by their exact protected-sum comparison.

Combining this with the forty-five block bounds and the whole-block split gives assembled source gap greater than \(0.02\), for any fixed finite list of these attachments. No gap is divided by the number of blocks.

## Persistence of failure of weak balance

The old restricted dual table has zero load at protected vertices \(0,16\). Its spectator mixtures occur only in regions \(2,4,7\), with right anchor 12. The same table remains feasible when those two vertices have positive weights but no block demands. It therefore gives
\[
\widehat G_{\rm restricted}>\Phi_B+0.025
\]
for every positive interior block vector with \(b=1\).

If all four regions \(2,4,7,12\) satisfied weak balance at the conditional complete vector, their full/mixed rates would be bounded by their complete rates. Thus
\[
\widehat G_{\rm restricted}\le\widehat P_B=\Phi_B+\Delta.
\]
The independently checked bound \(\Delta<0.025\) contradicts this. All four quartets survive the crossing-15 insertion unchanged. This is an exact dual obstruction, not a continuity claim about an unknown numerical minimizer.

The correction is nonnegative by a vertex allocation. Its finite Fourier enclosure can have a negative lower endpoint, which has no bearing on the required upper bound. The analytic estimate
\[
\Delta\le\frac4\pi\sqrt{3/b_n}+\frac{2\sqrt2}{\pi b_n}
\le\frac4{3n}+\frac1{3n^2}<\frac1{40}\quad(n\ge64)
\]
also proves the needed bound for the chosen length and all larger lengths.

## Executed checks and limits

The public runner is `repro/check_triangular_boundary_certificate.py`. Its frozen reference is `repro/triangular-boundary-insertion/summary.json`; fresh runs default to `repro/results/triangular-boundary/summary.json`. It requires python-flint and NumPy through the original source compiler. It rejects optimized Python because all imported exact checks use assertions.

The runner freshly verifies the original rational complete flow and the original restricted-dual certificate. It checks all forty-five source costs with the stated Fourier tail and precision, all eight fixed core margins, and the correction upper bound. It constructs the oriented cores at lengths 2, 4, 8, 16, then actually attaches the seventeen-region block at each terminal triangle. Independent oriented face, sphere, matching, protected-mark, surviving-region, and target-count checks follow each construction. These finite incidence tests supplement, rather than prove, the all-length stellar construction.

The finite topology checks do not choose a particular final knot parity. The written inverse-cut spanning-tree pairing construction supplies a one-component choice; the volume theorem still quantifies over retained patterns passing that actual one-component test. The runner does not calculate a knot invariant, prove an asymptotic saddle theorem, or certify a hyperbolic filling by sampling.

The original full-source local estimates, finite Hermite norm, nonzero Morse central period, and marked geometric completion are explicit separate inputs. With them, the new positive source gap makes the complementary filled contribution exponentially smaller for independently sufficiently long fixed final powers. It is the final original knot complement, with its primitive crossing-disk surgery, whose volume appears. Every finite diagram and integer is fixed before the quantum level tends to infinity.

The first diagnostic at length 4096 failed the chosen branch-38 witness; it is not an obstruction to all possible witnesses at that length. A successful earlier run at length \(2^{24}\) remains archived. No further threshold optimization was attempted after the successful \(2^{20}\) run was selected.
