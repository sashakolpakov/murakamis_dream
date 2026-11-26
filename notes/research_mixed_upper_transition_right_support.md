# Full-source support beside the upper transition interval

Research corollary, 5 November 2026. This extracts a larger target-height
domain already enclosed by the saved right-core certificate. No new
numerical cover or conditional saddle approximation is used.

## 1. Exact source and target domain

Keep the original finite functions
\[
 P_j=\prod_{k=1}^j(1-r^k),\qquad p_j(X)=\prod_{k=1}^j(1-r^kX),
 \qquad
 C_{\epsilon,N}(X,Y)=\sum_{j=0}^{N-1}
       \frac{X^{-j}p_j(X)p_j(Y)}{P_j^{2+\epsilon}},
 \quad r=e^{-2\pi i/N}.
 \tag{1}
\]
The Fourier polynomial \(d_N\) is the literal one in the
[Fourier-weight theorem](research_mixed_fourier_weight_continuation.md).
For ordered type indicators \((\eta,\epsilon)\), define the allocated
raw absolute source
\[
 \mathscr B_N(z,w)=
 \sum_{j=0}^{N-1}
 \left|\frac{X^{-j}p_j(X)p_j(Y)}{P_j^{2+\epsilon}}\right|
 |d_N(X)X^{-N\sigma_L}|^{\eta/2}
 |d_N(Y)Y^{-N\sigma_R}|^{\epsilon/2},
 \quad X=e^{-2\pi iz},\quad Y=e^{-2\pi iw}.
 \tag{2}
\]
Only square roots of nonnegative moduli occur. Thus (2) also bounds
the corresponding allocated modulus of the coherent kernel.

Fix an actual cyclic critical reference and its original complex
supporting plane \(\Gamma\), as in
[the complete right-half block theorem](research_mixed_right_half_block_bound.md),
equations (2)--(3). This is the actual reference of the fixed word,
including its height terms, rather than arbitrary independent reference
corners.

One target argument is real \(x\in[1/2,1]\). The other is \(y+ih\),
where the following entire independent rectangles are allowed:
\[
 \frac25\le y\le\frac12,\qquad
 \begin{array}{c|c|c}
 \text{moving type}&\text{selection}&h\\ \hline
 3&0&[-3/100,1/50]\\
 4&0&[-57/1000,0]\\
 4&1&[0,7/500].
 \end{array}
 \tag{3}
\]
Either orientation and every permitted selection at the real right
argument are included.

**Corollary 1.** Uniformly on (3), for all sufficiently large integer
levels of either parity,
\[
 \mathscr B_N(z,w)\le C N^A
       \exp N\{\Re\Gamma(z,w)-1/2000\}.
 \tag{4}
\]
The constants may depend on the fixed cyclic word. In particular (4)
holds on the closed upper transition interval \(y\in[9/20,1/2]\)
with every allowed attenuation of its original or selected height.
The independent rectangles in (3) are stronger than this graph
consequence.

## 2. Extraction from the saved profiles

Use the notation \((\epsilon,\beta,c)\) of
[the right-core source theorem](research_mixed_right_core_support.md):
\(\beta\) is the moving type-four indicator, while \(c=1\) when the
moving argument is first. Its six source families are
\[
 (0,0,0),\ (1,1,0),\ (0,0,1),\
 (0,1,1),\ (1,0,1),\ (1,1,1).
 \tag{5}
\]
These include both orientations of every ordered type pair; the
right argument's type only contributes its zero-rate Fourier factor
when it is not otherwise present in (5).

The saved source record contains the following literal fields:

| Moving type | Profile name | Angle interval | Selection | Stored height endpoints |
|---|---|---|---|---|
| 3 | all3 | \([13/100,1/2]\) | 0 | \(-3/100,1/50\) |
| 4 | part4 | \([2/5,1/2]\) | 0 | \(-57/1000,0\) |
| 4 | part4 | \([2/5,1/2]\) | 1 | \(0,7/500\) |

In the last angle interval the old taper has minimum zero, and the
larger taper has maximum one. Consequently its stored enclosing
rectangle is the full height band in (3). The original proof evaluates
its support over the whole angle interval at each listed height;
it does not constrain that height to the value of either taper
at the target angle.

For every fixed \((u,y)\) in the core, the complete envelope, including
both alternatives \(\max(\nu_h(y),2\pi h_+)\) and the selected linear
correction, is convex in \(h\). The raw row-one envelope has the same
property. The geometric plane is affine in the target height.
The original endpoint-height support gap \(1/500\) therefore extends
to every height between the stored endpoints, at each fixed actual
reference. This uses the height-convexity proof in the right-core
theorem and the
[core concavity theorem](research_mixed_right_half_concavity.md).
There is no reference maximum principle with a moving target height.

Thus all the selected profiles give
\[
 E(u,y;h)-\Re\Gamma<-\frac1{500},
 \qquad u\in[1/5,1/2]\cup\{1\},
 \quad (y,h)\text{ as in (3)},
 \tag{6}
\]
at right angle \(1/2\). The original 512 reference products include
all three-vertex words, all external types and all products of
rectangle edges. Their complete 5,546-cell cover already tests
every profile above. The separately holomorphic reference-window
branch and maximum principle are established before this comparison.
Periodic repetition realizes the actual references for cycles of
length one and two as well.

## 3. Every original row and right angle

The [right-angle reduction](research_mixed_right_half_source_reduction.md),
Lemma 1, applies because the actual real slopes lie in
\((-1/5,1/4)\). On \(y\ge2/5\) it holds at the same \(y,h\).
For lower row fractions it absorbs a possible interior right-angle
maximum by moving the row to \(u=1/5\); it does not move the other
angle to \(13/100\). Upper rows are already convex in the right
angle. Hence it is enough to bound right angles \(1/2\) and \(1\).

At right angle \(1/2\), the
[upper-row endpoint reduction](research_mixed_high_row_endpoint_reduction.md)
applies throughout (3): its domain is
\(y\in[13/100,1/2]\), \(|h|\le57/1000\).
It bounds all \(u\in[1/2,1]\) by \(u=1/2\) or \(u=1\), at the
same angle and height. Both endpoints occur in (6).
Thus every original row is covered with the support gap \(1/500\)
at this right endpoint.

At right angle \(1\), the
[all-endpoint theorem](research_mixed_all_endpoint_support.md), together
with its [remaining \((4,3)\) orientation](research_mixed_43_endpoint_support.md),
already gives the raw finite-source gap \(1/2000\) on all the
height bands in (3). More precisely, its proof and saved records
give a raw support gap \(1/1000\) before the Fourier tolerance.
These estimates hold for the sum of absolute rows and retain the
forced Fourier bound at the period seam.

Apply the right-angle reduction to these underlying raw rates first.
Their common support gap is at least \(1/1000\). The uniform
finite-product estimate contributes polynomial factors, and the
actual Fourier upper bounds allow one combined rate tolerance
less than \(1/2000\). This proves (4). Taking a maximum and
summing at most \(N\) rows changes only the polynomial prefactor.
There is no additional tolerance applied to an already finite
endpoint bound.

The right Fourier polynomial is bounded with its zero upper rate;
it is not replaced by an inverse factorial. Its selected monomial
has modulus one at height zero. At the moving argument the actual
Fourier polynomial, both alternatives and the selected half-rate
remain in (2) and (6). Product zeros, the last original row, half-period
endpoints and both level parities are included. All original level
scalars remain as in the source identities; no new normalization
or packet at a right-half argument is asserted.

The [periodic hybrid graph](research_mixed_split_cutoff_hybrid_contour.md)
has an upper transition height equal to an original height, or
\(7/500\) when selected, multiplied by factors in \([0,1]\).
It is therefore contained in (3). This is only a local source
corollary; it does not perform a complete mixed-region assembly.

## 4. Provenance and reproduction

The cheap checker verifies the literal profile endpoints, every required
type and orientation, all stored reference partitions and current source
bindings. It also binds the existing independent source-grid replay
and the original 320-bit reference review, archived byte-identically as
research-mixed-right-core-support-reference-replay.json.
The latter was a fresh run of the original reference checker: its
domains and accepted addresses agree with the 256-bit record.
This extraction does not claim a new numerical run or a new acceptance
test on those boxes.

    python3 experiments/check_mixed_upper_transition_right_support.py
