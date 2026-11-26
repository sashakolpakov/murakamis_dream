# Direct replacement of a right run: internal loss and two boundary costs

Research deduction, 5 November 2026. This retains the original complete
raw envelope and the original coherent phases. It proves that sufficiently
long right runs have a uniform loss, with an unspecified finite cutoff.
It does not establish the remaining short-run boundary comparisons.
No new numerical cover or finite-kernel lower bound is used.

## 1. Replacement leaves every outside target unchanged

Fix a typed cyclic word, its actual reference \(r\), and a fixed
\(0<\rho\le1/1000\). Use the original periodic
[split-cutoff hybrid contour](research_mixed_split_cutoff_hybrid_contour.md).
In this note every coordinate is in
\[
 A_\rho=[\rho,1/2]\quad\hbox{or}\quad R=[1/2,1].
 \tag{1}
\]
Choose the half-open convention at \(1/2\) when counting runs; all bounds
include the closed endpoints. In particular there is no physical zero
coordinate in this deduction. Permitted selections are arbitrary.

Let \(T\) denote the set of right vertices. Replace every \(x_j\), \(j\in T\),
by \(a_j=\Re r_j\), remove its selection, and recompute the hybrid targets.
Write \(z^\#\) for the resulting targets. Both \(x_j\in R\) and
\(a_j\in(.27,.39)\) have value one in both left cutoffs. Therefore:

* every target and selection outside \(T\) is literally unchanged;
* every AA edge is unchanged, including its two Fourier halfweights;
* the new target at a right vertex has the form
  \(a_j+i\lambda_j\Im r_j\), with \(0\le\lambda_j\le1\).

For a run of length at least two, the fraction at an end depends only on
its outside A neighbor; the other neighbor has left cutoff one.
Interior right vertices are exactly their references. For an isolated
right vertex the fraction is the minimum of the two A-neighbor cutoffs.
These assertions refer to original incidences, so they also cover a
two-cycle. In an all-right cycle every new target is exactly its reference.

The repaired graph lies in the domain of the completed
[deep-half phase theorem](research_mixed_deep_low_half_region.md).
Thus its full selected coherent rate is at most the original critical
rate \(M\). This use is a pointwise phase comparison, not a change of
variables or a lower estimate for an original finite kernel.

## 2. Every internal right edge retains its original loss

Let edge \(j\) join \(j-1,j\), let \(\phi_j\) be the original allocated
phase, and let \(\Gamma_j\) be its full complex tangent at the actual
reference. Define the original raw rate \(\mathscr F_j\) exactly as in
[the interface reduction](research_mixed_nonlow_interface_reduction.md),
equation (3). It retains the entire row interval, first-argument chirp,
both true Fourier alternatives and both selected halfweights. Put
\[
 D_j=\mathscr F_j(z_{j-1},z_j)-\Re\Gamma_j(z_{j-1},z_j),
 \qquad
 W_j^\#=e_j(z_{j-1}^\#,z_j^\#)-\Re\Gamma_j(z_{j-1}^\#,z_j^\#),
 \tag{2}
\]
where \(e_j\) is the full coherent rate including any remaining
selected corrections.

On an RR edge the original source has
\[
 D_j\le-1/50.
 \tag{3}
\]
This is the raw-envelope margin before a finite-source tolerance:
equations (9)--(10) of the
[two-right source theorem](research_mixed_two_right_source_bound.md).
In particular (3) is not inferred from cancellation inside a finite sum.
Selections at original real R coordinates have unit modulus.

On the repaired RR edge both real coordinates equal their reference
real parts and both selections are absent. Write the height displacement
as \(v=(\Im z_{j-1}^\#-\Im r_{j-1},\Im z_j^\#-\Im r_j)\).
The entire straight height segment stays in the unselected products
\(U_3,U_4\). The
[extracted curvature theorem](research_mixed_extracted_plateau_curvature.md)
gives \(A=-\Re\phi_j''\succ I/5\) there. Taylor's formula gives
\[
 W_j^\#
 =\int_0^1(1-t)\,v^T A(r+itv)v\,dt
 \ge\frac1{10}|v|^2\ge0 .
 \tag{4}
\]
The tangent in this identity is the original complex tangent, not a
real-reference supporting plane. Formula (4) includes two partial
height resets at the ends of a length-two run.

Combining (3)--(4), an internal RR edge contributes at most
\[
 D_j-W_j^\#\le-1/50-|v|^2/10 .
 \tag{5}
\]
No AA reset debit occurs: all AA targets stayed unchanged.

## 3. Exact remaining boundary functions

On an RA or AR boundary edge keep the explicit function
\[
 \mathcal B_j=D_j-W_j^\# .
 \tag{6}
\]
It is essential to retain both terms in (6), with their respective
original and repaired arguments. The selected correction at an unchanged
A endpoint is present in both actual rates; it must not be replaced by
an unselected halfweight. Equivalently its literal modulus factor
cancels when comparing the two allocated blocks.

All original tangent terms cancel in the complete comparison:
\[
 \sum_j\Gamma_j(z)=\sum_j\Gamma_j(z^\#)=\sum_j\phi_j(r)=\Phi^*.
 \tag{7}
\]
Indeed their linear coefficients are the original cyclic critical
equations. Because every AA target is unchanged, (7) also gives
cancellation after restricting the difference to right-incident edges.
Consequently the physical raw/coherent upper rate obeys
\[
 \mathcal E_{\rm raw}
 \le M+\sum_{j\in AR\cup RA}\mathcal B_j
       -\frac{n_{RR}}{50}
       -\frac1{10}\sum_{j\in RR}|v_j|^2 .
 \tag{8}
\]
This includes all original rows and true Fourier factors. It is a
different comparison from separately closing the two neighboring A runs.

For a proper right run of length \(k\ge2\), its sufficient remaining
comparison is therefore
\[
 \mathcal B_{\rm left}+\mathcal B_{\rm right}
       <(k-1)/50 .
 \tag{9}
\]
The optional squared-height gains in (8) may strengthen (9). A singleton
has no internal gain and needs the sum of its two boundary functions to
be negative. A two-cycle with a singleton has two physical boundary
edges; the same formulas use them once each.

For fixed \(\rho>0\), the two boundary functions are continuous on a
fixed finite union of compact parameter domains, independent of word
length. One may enlarge the actual reference pairs to their closed typed
rectangles and permit independent cutoff fractions in \([0,1]\) on the
nonlow products, retaining the forced zero heights whenever an A argument
lies below .1.
The raw row maximum is continuous, including product zeros: its integral
primitive is continuous and its row domain is compact. The repaired
conditional phases have their proved original branches on the compact
source products. Deep-low A arguments are real, so the compact real
half-endpoint packet applies there. All remaining products are in the
proved nonlow source polygons.

It follows that the finite number
\[
 B_\rho=\max\{0,\sup\mathcal B_{\rm left},
                         \sup\mathcal B_{\rm right}\}
 \tag{10}
\]
exists. This note does not evaluate it or claim that it is small.
Let
\[
 H_\rho=\max\{2,\lceil200B_\rho+2\rceil\}.
 \tag{11}
\]
If every proper R run has length at least \(H_\rho\), (8) gives a
phase loss at least \(|T|/100\), since
\[
 2B_\rho-(k-1)/50\le-k/100\qquad(k\ge H_\rho).
 \tag{12}
\]
An all-right cycle has the stronger loss \(m/50\). This conclusion
is uniform in word length at the level of these rate comparisons:
the compact domains and \(B_\rho\) do not depend on the word.
For each fixed word, distributing one total finite-source tolerance
less than \(1/200\) gives a complete finite-source and integral bound
with loss at least \(|T|/200\). The fixed-word polynomial powers,
original scalars/carriers and bounded graph Jacobian are retained.
No joint word-length/level asymptotic is asserted.

This is only a reduction to finitely bounded run lengths, with an
unevaluated cutoff. It does not supply (9) for short runs, does not
handle physical zero coordinates adjacent to R by a coherent packet,
and does not prove the full-period asymptotic.

## 4. Why choosing a better single replacement point is insufficient

The already certified
[geometric-replacement obstruction](research_mixed_geometric_right_replacement_obstruction.md)
has neighboring real angles \((.1,.5)\), star types \((4,3,4)\),
and a real right center at \(.5\). All hybrid heights remain zero
when the center is replaced by any real \(t\in[.1,.5]\). A bounded
floating scalar diagnostic gives
\[
 \max_t\{f_{1,0}(.1,t)+f_{0,1}(t,.5)\}
       \simeq1.2300822022,\qquad t\simeq.344134264,
 \tag{13}
\]
while the complete raw two-row maximum is approximately
\(1.2957014382\). Thus the optimized real replacement still has
a positive diagnostic excess about \(.065619236\).

The archived driver also evaluates the original rational rows
\(7/25,23/100\) against a real-concavity tangent at \(t=43/125\).
Its floating excess is above \(.0654\). These new numbers are not
outward certified and are not used in (1)--(12). The bounded driver,
fixed inputs and helper binding are in
[the diagnostic archive](../repro/diagnostics/2026-11-05-optimized-right-center/README.md).

Accordingly, replacing a single R coordinate by a different real center
is not presently a plausible uniform way to eliminate the known
two-edge obstruction. Grouping neighboring coherent edges, or using the
same incoming boundary potential at both ends, is a genuinely different
remaining comparison. Neither its success nor a failure of the original
signed kernel follows from the diagnostic.
