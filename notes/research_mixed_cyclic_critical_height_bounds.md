# Sharper critical domains from universal open windows

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The completed universal localization theorem already supplies a
holomorphic two-leg root map on every full product of typed disks.
Only after that existence theorem is available may a distinguished
boundary reduce image estimates to two real angular parameters.
Both estimates below have passed their author and independent replays.
In particular, every type-four critical leg in every finite cyclic
word lies in the fixed rectangle \((.27,.33)+i(-.057,-.001)\).
The conclusion concerns the original zero-lift critical point; a full
mixed-word finite-sum estimate remains separate.

## 1. A legitimate distinguished-boundary reduction

Use the disks \(D_3,D_4\), box \(Q\), and zero-lift root map
\(B_\epsilon(a,b)=(s(a,b),t(a,b))\) from
[the universal localization theorem](research_mixed_cyclic_critical_localization.md).
That theorem establishes holomorphy on a neighborhood of the
**entire closed bidisk** before any boundary maximum principle is
used here. Its existence proof was the full four-real-parameter
cover, followed by the original Brouwer construction.

For a holomorphic scalar component \(f\), successive harmonic
maximum/minimum principles give its real and imaginary extrema
on the product of the two boundary circles. Successive maximum
modulus principles do the same for \(|f-c|\). Thus write
\[
 a=c_{n_-}+r_{n_-}e^{2\pi i\theta},\qquad
 b=c_{n_+}+r_{n_+}e^{2\pi i\eta},\qquad
                         (\theta,\eta)\in[0,1]^2.
 \tag{1}
\]
This argument would have been circular as a proof of the original
bidisk root existence. Here it estimates a holomorphic map whose
existence and branch were proved independently.

**Proposition 1.** At the critical point of every finite cyclic
word in three and four, both legs at a three-vertex satisfy
\[
 |z-(7/20-i/100)|<83/1000,\qquad
                         -13/200<\Im z<17/250,
 \tag{2}
\]
and both legs at a four-vertex satisfy
\[
 |z-(3/10-13i/250)|<3/50,\qquad
                         -51/500<\Im z<-1/1000.
 \tag{3}
\]

*Proof.* The six universal type cases in (1) are covered by 6,994
exact dyadic angle rectangles. For each rectangle, the original
localization self-map test is evaluated on the two complex arc
rectangles. It certifies an affine parameter root enclosure
\(z=z_0+D(p-p_0)+w\), \(|w_i|\le R_i\), with the original
zero logarithmic lift. The entire certified image obeys (2) or
(3). Uniqueness in \(Q^2\) identifies this local zero with the
already-existing bidisk branch.

An independent sine/cotangent replay passed all 6,994 angle cells
at 256 bits without refinements, including the exact binary cover.
The author used 192 bits. The six accepted counts are
\(1613,1425,1089,1849,546,472\), in the same type order as the
localization certificate. Applying the maximum principles above
extends every strict bound to each full input disk product.
At an actual cyclic critical point the two-leg map is at its
fixed point, so these image inequalities apply to every leg.
\(\square\)

## 2. Arbitrary finite open windows have global root branches

Let \(\epsilon_1,\ldots,\epsilon_k\in\{0,1\}\), and fix two
external legs \(a,b\) in arbitrary typed disks. Put
\(g(z)=J(z)+i\pi(z-z^2)/2\). Define the open-window potential
\[
 \begin{split}
 \mathcal W={}&\sum_{v=1}^k g(s_v+t_v)
   +\sum_{v=1}^{k-1}g(t_v+s_{v+1})+g(a+s_1)+g(t_k+b)\\
 &-\sum_{v=1}^k(2+\epsilon_v)\{g(s_v)+g(t_v)\}\\
 &+2\pi i\left(as_1+\sum_{v=1}^{k-1}t_vs_{v+1}+bt_k\right).
 \end{split}
 \tag{4}
\]
Its gradient is the literal zero-lift cyclic gradient on the window,
with its two external neighbors held fixed. No phase constant is
needed for this critical-domain statement.

**Lemma 2.** For every fixed finite window and every pair of external
typed disks, \(\nabla\mathcal W=0\) has a unique solution in
\(Q^{2k}\). Every leg lies strictly inside its original typed disk.
The solution is holomorphic on a neighborhood of the full external
bidisk. Uniformly in the length and type pattern,
\[
                         -\Re\mathcal W''\succ(\pi/4)I_{2k}.
 \tag{5}
\]

*Proof.* Update the two legs at each vertex with the established
local map, retaining the fixed external values at the two ends.
This is a continuous self-map of the product of the original typed
closed disks. Brouwer gives a fixed point. It solves exactly the
gradient of (4).

The negative real Hessian is the same sum of pair forms as in the
localization proof. There are \(k\) internal pairs, \(k-1\)
shared pairs and two end pairs. A boundary pair contributes its
one-variable principal submatrix when its external leg is fixed.
Every active leg still has exactly two pair incidences; the extra
type-four single-leg terms are positive. Each pair contributes
more than \(\pi/8\) per active coordinate, so (5) follows.
Complex-gradient injectivity gives uniqueness throughout the
convex chamber. The implicit function theorem and uniqueness glue
the local roots over the closed external bidisk. Compactness gives
a neighborhood of that full bidisk. \(\square\)

The type pattern need not be homogeneous. This lemma is an open
critical-point statement, not a theorem about an open finite source.
It retains the marked logarithmic equations of the actual contracted
phase and supplies the global branch needed before applying a
boundary maximum principle to any of its coordinates.

## 3. A fixed five-vertex test controls all cyclic lengths

**Theorem 3.**
Every leg at a four-vertex of every finite cyclic word satisfies
\[
             27/100<\Re z<33/100,\qquad
                    -57/1000<\Im z<-1/1000.
 \tag{6}
\]

The lower-height computation uses five-vertex windows with the
middle vertex of type four. There are sixteen choices of the
remaining four types and four choices of the external disk types.
Reflection exchanges the two external disks and reverses the
window and the order of its legs. After this exact symmetry,
there are 36 universal cases. In each case the selected root map
exists on the full external bidisk by Lemma 2. Its two middle-leg
coordinates are holomorphic there, so their real/imaginary bounds
reduce to (1).

For each exact angle rectangle, the author proposes a rational
center \(z_0\in\mathbb C^{10}\), a rational approximate inverse
\(Y\), and a rational external response matrix \(D\in\mathbb C^{10\times2}\).
They carry no validity claim until the outward test proves
\[
 \begin{split}
 b_i&\ge\sup_p|(Y\nabla\mathcal W(z_0+D(p-p_0),p))_i|,\\
 E_{ij}&\ge\sup_{p,\,|w_j|\le R_j}
 |(I-Y\mathcal W''(z_0+D(p-p_0)+w,p))_{ij}|,\\
                         b_i+\sum_jE_{ij}R_j&<R_i.
 \end{split}
 \tag{7}
\]
The entire root rectangle lies in \(Q^{10}\), and both middle
imaginary parts exceed \(-57/1000\). A point test
\(\|I-Y\mathcal W''(z_0,p_0)\|_\infty<1/4\) ensures that \(Y\)
is invertible. Thus (7) is a genuine Banach self-map for every
external point in the whole angle rectangle.

The residual retains its external linearization and bounds the
quadratic remainders of the exact logarithms. The Jacobian is
tridiagonal in the ordering \(s_1,t_1,\ldots,s_5,t_5\). Its
variation is assembled from exact rational exponential differences;
constant imaginary chirp entries have zero variation. The
independent replay instead uses sine logarithms, cotangent
differences, and \(J'''=-\pi^2\csc^2\pi z\). It additionally
checks the two real-part bounds in (6). Both implementations
retain every dyadic rectangle and its endpoints.

The 160-bit author certificate passed all 36 cases with 28,899
accepted angle rectangles, after 57,762 visits. The independent
256-bit replay passed all 28,899 rectangles with no refinements.
It separately verifies the full list of 36 reflection representatives,
the prefix-free dyadic cover of each angle square, both middle-leg
real bounds, and the lower-height bound. The eight reflection-fixed
configurations give \((64+8)/2=36\) representatives.

To apply the universal window statement to a cyclic word, first
repeat its period until the five-vertex window and its two external
neighbors are distinct positions. The repeated original critical
point still solves exactly the same local zero-lift equations.
Center a window at the desired four-vertex. Its two external legs
belong to their original typed disks. Uniqueness from Lemma 2
identifies the restricted cyclic point with the certified window
branch. This proves the real bounds and lower-height bound in
(6), for every cyclic length, including one and two. The upper
negative bound is Proposition 1. No enumeration of whole cyclic
words is involved.

## 4. Correlated witnesses and scope

The separate correlated-image artifact extracts the witnesses from
the original accepted four-real-parameter cover, without repeating
its adaptive search. A row contains
\[
           (\text{address},z_0,D,R),\qquad
              z(p)\in z_0+D(p-p_0)+\{|w_i|\le R_i\}.
 \tag{8}
\]
The address and typed disks determine the exact parameter box and
its midpoint. Keeping, for example, \((a,t(a,b))\) in this form
preserves the input/output correlation required by conditional
source estimates. Independent bounding rectangles may discard
useful information. The extractor rechecks the frozen self-map
inequalities on every accepted address; it modifies none of the
completed localization artifacts.

These bounds improve the domain available for subsequent alias
and conditional-source contour work. They assert neither a
whole-cycle finite-sum bound nor a nonzero mixed-word source
coefficient. No knot or marked-volume identification is inferred
from a critical-domain estimate alone.

The complete records are the [first image certificate](../repro/results/research-mixed-cyclic-block-boundary-images.json),
[its independent replay](../repro/results/research-mixed-cyclic-block-boundary-images-replay.json),
[the five-window certificate](../repro/results/research-mixed-cyclic-window-heights.json),
and [its independent replay](../repro/results/research-mixed-cyclic-window-heights-replay.json).
A proof-only provenance refresh attaches this final note to the completed
computations and retains their former record and script hashes. It does
not represent another numerical run. All original localization records
remain unchanged.

Reproduction paths:

```sh
python3 experiments/certify_mixed_cyclic_block_boundary_images.py --precision 192
python3 experiments/replay_mixed_cyclic_block_boundary_images.py --precision 256
python3 experiments/certify_mixed_cyclic_window_heights.py --precision 160
python3 experiments/replay_mixed_cyclic_window_heights.py --precision 256
python3 experiments/extract_mixed_cyclic_block_images.py --precision 192 --responses
```
