# Reusing the complete prefix reference banks for the terminal window

Research deduction and fixed saved-data projection, 6 November 2026.
The seven-variable reference of the two-selected terminal window is
exactly an already certified canonical prefix with its coordinate
order reversed. The two compact boundary banks therefore contain
its original references on the complete boundaries of \(K_3,K_4\).
Scalar harmonic bounds extend these data to the whole domains.
This reuses original gradient equations, not a reversal of finite
contour currents. No new root, analytic value or gain is evaluated.

## 1. Exact gradient permutation

Use \(j=J'=\operatorname{Log}(2\sin\pi z)\) with the original
regular-strip branch. In the
[canonical prefix](research_mixed_prefix_residual_localization.md),
write the original coordinates with a superscript \(o\):
\[
 (e^o,\xi^o,a^o,u^o,z^o,v^o,b^o;c^o),\qquad
                   (\alpha,\text{second flag},\beta)=(\epsilon,1,1).
 \tag{1}
\]
Define new terminal-window coordinates by
\[
 (e,\xi,t,a,s,b,r;c)
             =(e^o,\xi^o,a^o,u^o,z^o,v^o,b^o;c^o).
 \tag{2}
\]
The external type \(3+\gamma\) is the type of \(c\);
it is not the old flag \(\beta\), which is fixed to one.

Under (2), the seven original prefix gradients are exactly
\[
 \begin{split}
 f_e={}&-j(e-\xi)+j(e+t)-\epsilon j(e)
                         +i\pi[\xi-t+\epsilon(e-1/2)],\\
 f_\xi={}&2\Log\cos\pi\xi+\Log\sin\pi(e-\xi)
                                  -3\Log\sin\pi\xi+i\pi e,\\
 f_t={}&j(e+t)+j(t+a)-(2+\epsilon)j(t)
                         +i\pi[a-e+\epsilon(t-1/2)],\\
 f_a={}&j(a+s)+j(t+a)-3j(a)+i\pi[t-s+a-1/2],\\
 f_s={}&j(a+s)+j(s+b)-3j(s)+i\pi[b-a+s-1/2],\\
 f_b={}&j(b+r)+j(s+b)-3j(b)+i\pi[s-r+b-1/2],\\
 f_r={}&j(b+r)+j(r+c)-3j(r)+i\pi[c-b+r-1/2].
 \end{split}
 \tag{3}
\]
The auxiliary row is unscaled. Since
\(g'(z)=j(z)+i\pi(1/2-z)\), the final two rows are precisely
\[
 g'(r+b)+g'(s+b)-3g'(b)+2\pi is,\qquad
 g'(r+c)+g'(r+b)-3g'(r)+2\pi ic.
 \tag{4}
\]
The first five are the already used terminal family \(q_\epsilon(b)\).

One can also check the original action itself. After (2), the
prefix action is
\[
 \begin{split}
 F={}&B(e,\xi)+J(e+t)-\epsilon[J(e)+J(t)]\\
 &+J(a+s)-J(a)-J(s)+J(b+r)-J(b)-J(r)\\
 &+J(t+a)-2J(t)-2J(a)+J(s+b)-2J(s)-2J(b)\\
 &+J(r+c)-2J(r)+i\pi Q,\\
 Q={}&e\xi-et+ta-as+sb-br+rc\\
 &+\tfrac\epsilon2(e^2+t^2-e-t)
       +\tfrac12(a^2+s^2-a-s)+\tfrac12(b^2+r^2-b-r).
 \end{split}
 \tag{5}
\]
Here \(B(e,\xi)=-2J(1/2-\xi)-3J(\xi)-J(e-\xi)\).
Equation (5) is the original right-end length-four restriction;
the omitted external \(-2J(c)\) and inactive first-end terms
depend only on fixed coordinates. Thus its seven active gradients,
branches and Hessian are identical, not merely their exponentials.

**Proposition 1.** For each \(\epsilon,\gamma\), the old prefix
branch with \(\alpha=\epsilon,\beta=1,c\in K_{3+\gamma}\)
is exactly the canonical reference of
[the two-selected reconstruction](research_mixed_terminal_two_selected_reference_reconstruction.md)
under (2).

*Proof.* Both branches solve (3) in the same convex product
\(E\times U\times Q^5\). Original existence is known on a
neighborhood of each full \(D_3,D_4\); the common principal
Hessian has negative real part greater than \((6\pi/49)I\).
Original uniqueness therefore identifies them. The actual-suffix
coverage, including attached \(c\) at length four, follows from
the reconstruction theorem. \(\square\)

This proposition transfers references and their enclosures. It
does not transpose a finite cap, transport a selected contour
backward, identify old central scalar budgets with new budgets,
or discard a \(c\)-dependent constant in a source comparison.
The original incoming marginal and source allocation in the
two-selected window remain unchanged.

## 2. The complete boundary data already available

The compact banks are:

* For \(\epsilon=1\),
  [the first-four bank](../repro/results/research-mixed-second-selected-boundary-reference-bank.json),
  SHA256 3e6e227ac78afcf214844376f7f0069259a4c3f0e7a9a755a6a57a8081a24bbb.
* For \(\epsilon=0\),
  [the first-three bank](../repro/results/research-mixed-second-selected-first-three-boundary-reference-bank.json.gz),
  SHA256 4b0bfa3cb2bfb68b622487c390879312b7d0832a056f03c3675a38cedeb8c323.

Select only old \(\beta=1\). The completed inventories are
\[
 \begin{array}{c|r|r|r|r}
 \epsilon&K_3\text{ accepted}&K_4\text{ accepted}
             &\text{geometry exclusions}&\text{total leaves}\\ \hline
 0&310&327&55&692\\
 1&316&330&56&702.
 \end{array}
 \tag{6}
\]
For each row the five \(K_3\) charts and four \(K_4\) charts
have complete prefix-free dyadic partitions of normalized mass one.
There are no pending leaves or reference exclusions in these slices.
Every excluded interval has its original strict geometric witness.
The [exact chart theorem](research_mixed_second_selected_external_boundary_charts.md)
covers all circle arcs, clipping chords, oblique \(K_3\) edges
and junctions.

The inherited saved audits are
[first four](../repro/results/research-mixed-second-selected-external-boundary-saved-audit.json),
SHA256 38971e851765e3a9df8be5aed447bf036110e7dc0a34e5c4885e5f59f3825f23,
and
[first three](../repro/results/research-mixed-second-selected-first-three-external-boundary-saved-audit.json),
SHA256 88d8f8177a439f4268980e7467fffc576b558776c22f2a6067361d0ab8b6a047.
Their original reference providers certify the canonical branch
for every actual \(c\) in the saved cell intersected with its
typed \(K\), not merely for finite-word references.
The compact extractors preserve each coordinate box and its
source-node, reference-certificate and external-cell association.
The full source records need not be parsed again to use this
already audited projection.

## 3. What extends harmonically, and what does not

For any fixed complex coefficients \(\lambda_j\), each component
of the canonical vector \(q(c)\), and hence
\[
                      f(c)=\sum_j\lambda_jq_j(c),
 \tag{7}
\]
is holomorphic near \(D_{3+\gamma}\).
The set \(K_{3+\gamma}\) is a compact convex disk/half-plane
intersection with nonempty interior. The real and imaginary
parts of (7) are harmonic on a neighborhood of it.

**Proposition 2.** Form an interval enclosure of \(\Re f\) or
\(\Im f\) separately on each accepted boundary reference cell,
using that cell's original coordinate boxes. Then take the
minimum lower endpoint and maximum upper endpoint over all
accepted cells of the fixed \((\epsilon,\gamma)\) slice.
The resulting interval encloses that scalar component everywhere
on \(K_{3+\gamma}\).

*Proof.* Geometric exclusions remove no point of this boundary;
the accepted cells therefore cover every boundary point. Each
point uses the canonical branch by Proposition 1 and the original
provider scope. Apply the harmonic maximum and minimum principles
to the scalar component. \(\square\)

Sums must be formed within the same saved cell before taking global
extrema. The statement also applies to any specified real linear
combination of real and imaginary coordinate components. It does
not transport a boundary cell's entire joint reference box to an
interior cell with the same parameter label. Nor does it bound an
arbitrary nonlinear phase by its boundary values.

In particular the stored old-\(v\) height extrema are exactly
new-\(b\) height bounds; old-\(b\) gives new-\(r\), and
old-\(z\) gives new-\(s\). The existing old-\(v\) decimal displays
suggest the common strict rational enclosure
\[
                         -77/1250<\Im b<-211/5000.
 \tag{8}
\]
The decimals are not proof criteria: the fixed saved projection
below must compare (8) with the original exact endpoints before
this new rational summary is used in a budget. No new budget sign
follows merely from (8).

## 4. Fixed height-integral boxes without another parameter cover

Let \(H=1/100\), and let \(\theta\in[0,1]\). The four
fixed arguments for the ordinary lift and its shared-index debit are
\[
 r+b+i\theta(H-\Im b),\qquad
 s+b+i\theta(H-\Im b),\qquad
 b+i\theta(H-\Im b),\qquad
 s+a+i\theta(H-\Im a).
 \tag{9}
\]
Their real parts are respectively
\(\Re(r+b),\Re(s+b),\Re b,\Re(s+a)\), independent of \(\theta\).
Their imaginary parts are
\[
 \Im r+(1-\theta)\Im b+\theta H,\quad
 \Im s+(1-\theta)\Im b+\theta H,\quad
 (1-\theta)\Im b+\theta H,\quad
 \Im s+(1-\theta)\Im a+\theta H.
 \tag{10}
\]
For a fixed \(\theta\), every real part described after (9)
and every expression in (10) is a scalar harmonic function of \(c\).
The complex lifted
arguments themselves need not be holomorphic in \(c\).
Only their separate scalar components are used here.

Fix the original sixteen intervals
\([j/16,(j+1)/16]\), \(0\le j<16\).
On each accepted boundary cell, enclose the real parts above and
each imaginary expression at both endpoints of its \(\theta\)
interval. Their hull contains the entire slab because (10) is
affine in \(\theta\) at a fixed reference. Proposition 2 at the
two endpoints then proves the same containing rectangle for every
interior reference and every \(\theta\) in that slab.

First keep separate \((\epsilon,\gamma)\) boxes. Taking a union
over \(\gamma\) for fixed \(\epsilon\) gives, if desired, precisely
\[
                         2\cdot16\cdot4=128
 \tag{11}
\]
argument rectangles for a later fixed height-integral calculation.
This is an exact projection of old boundary data, not a new
subdivision of a parameter domain. It evaluates no cotangent.
Retaining the two external types separately is also legitimate
and may give tighter bounds, but changes no reference branch.

## 5. Fixed saved-only extraction obligations

A standalone projection may read the two banks and their existing
audits, with all files pinned before and after. It must:

* Verify the banks' original source/audit/extractor associations,
  unchanged inherited bindings, and accepted payload hashes.
* Retain exactly the old-\(\beta=1\) slices (6), all nine chart
  trees per \(\epsilon\), and every original geometric exclusion.
  Reject pending, unresolved or reference-excluded leaves.
* Verify each selected accepted record's external-cell association,
  then rename coordinates by (2). Recompute global coordinate
  extrema and the specified linear sums from exact rational
  enclosure endpoints, grouping by \((\epsilon,\gamma)\).
* Recheck the existing old-\(v\), old-\(b\) height summaries from
  the selected cells, and compare the proposed rational guard (8)
  only with exact endpoints.
* Construct only the prescribed sixteen slabs and four arguments
  of (9), retaining per-domain and optional union boxes, together
  with extremizing source-node identifiers and the original bank
  associations.

The standalone extractor is
[extract_mixed_terminal_two_selected_references.py](../experiments/extract_mixed_terminal_two_selected_references.py).
It must write only to a fresh specified path; the prescribed result is
[research-mixed-terminal-two-selected-reference-projection.json](../repro/results/research-mixed-terminal-two-selected-reference-projection.json).
The output has status passed only after every saved-data check and
the final input-binding verification succeed. It records the proof,
extractor and inherited source hashes, all selected source-node
associations, the eighteen complete selected chart trees, and
the exact endpoint witnesses. A failure record retains its reason
and any completed projection, without asserting the proposed guard.

The fixed union output has two cases in order \(\epsilon=0,1\).
Each has four coordinate enclosures named \(r,b,s,a\), and
sixteen slab records with exact theta endpoints and argument keys
\(b,rb,sb,sa\). Every real/imaginary interval stores its exact
rational endpoints; the separate four external-domain cases and
their witnesses remain in the record. The guard (8) is checked
against all four exact old-\(v\) extrema. The extractor inherits
the original audits' analytic reference and geometric-exclusion
proofs; it independently checks the saved payload associations,
dyadic partitions, original height summaries and all new linear
endpoint combinations. It does not claim a new analytic replay.

No root, rational backward-shape evaluation, analytic primitive,
scalar gain, new source estimate or new parameter cell is required
by this projection. Its eventual record must distinguish newly
checked rational summaries from inherited analytic certificates.
The larger-window two-budget signs remain the quantitative task;
this deduction supplies their original reference domain and a
way to reuse sharper correlated boundary enclosures.
