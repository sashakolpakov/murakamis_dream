# Fixed saved-gradient transport to the enlarged contracted central box

Research calculation protocol, 7 November 2026. This is a new
exact rational recombination of the completed nine-face record.
It does not repeat that experiment or change its inconclusive
status. The supporting points, parameter square, function values
and derivatives remain precisely those already saved.

The required analytic premises are proved in
[enlarged-domain accretivity](research_mixed_contracted_pair_enlarged_rectangle.md)
and [the enlarged tail reduction](research_mixed_contracted_pair_enlarged_tail_reduction.md).
Their immutable hashes are recorded below. This protocol does not
infer any new face sign from those analytic proofs alone.

## 1. The new faces and the required analytic premises

The new coherent central box is
\[
 C'=[1/4,1/2]\times[1/5,9/20]
                         \times[1/5,21/50]^2,
 \tag{1}
\]
in the order \((s,t,p,q)\). The required new analytic proofs
are strict concavity of the original rate \(E\) on this entire
box, strict concavity on
\[
 F'_0=\{s=0,\quad t\in[1/5,9/20],\quad
                                 p,q\in[1/5,21/50]\},
 \tag{2}
\]
and the tail-preserving reduction of the entire original physical
complement of \(C'\) to its eight faces, (2), and the already
bounded far region \(2261/1500\). These are source/domain
proofs, not assertions inferred from the saved numerical record.

The fixed face order is
\[
 s=1/4,1/2;\qquad t=1/5,9/20;\qquad
 p=1/5,21/50;\qquad q=1/5,21/50;\qquad s=0.
 \tag{3}
\]
Each uses the old supporting point in the row with the same
coordinate and lower/upper label. Thus the old \(s=9/20\)
row supports the new \(s=1/2\) face, and the old \(t=1/4\)
row supports the new \(t=1/5\) face. Every free coordinate
uses its full new interval in (1) or (2).

The two moved supporting points need not lie on their new faces.
They lie in \(C'\), where full four-variable concavity gives
\[
              E(x)\le E(y)+\sum_{i=1}^4E_i(y)(x_i-y_i).
 \tag{4}
\]
For \(s=0\), both points lie on (2), and only its three
free derivatives are needed. The zero fixed-coordinate displacement
lets the same four-term formula represent that case. Keeping the
fixed-coordinate contributions in (4) is essential for the two
shifted faces.

## 2. Exactly what is recombined

For an old row write its saved rate enclosure as
\([E_-,E_+]\), and its four derivative enclosures as
\([g_i^-,g_i^+]\). Let the corresponding new face have
coordinate intervals \([L_i,U_i]\), with equal endpoints
for its fixed coordinate. Define, using exact rational arithmetic,
\[
 \begin{split}
 b_i&=\max\{g_i^-(L_i-y_i),g_i^-(U_i-y_i),
                 g_i^+(L_i-y_i),g_i^+(U_i-y_i)\},\\
 U_F&=E_++\sum_{i=1}^4b_i.
 \end{split}
 \tag{5}
\]
There is no zero cap on a signed contribution. Formula (5) bounds
the affine functional in (4) for the original reference parameter
and every point of the new face. It uses only the saved outward
intervals; it does not reconstruct the Arb primitives or require
equality with products made from differently rounded old intervals.

The inventory is exactly nine rows, 36 interval-product support
terms, and 144 rational endpoint products. No analytic function,
root, new optimizer, gain helper, subdivision, grid, or numerical
support proposal is called. The strict target is fixed as
\[
                      U_F<\frac{151239}{100000}
                         =\frac{3781}{2500}-\frac1{100000}.
 \tag{6}
\]
All nine rows are reported even if some fail. The overall status
passes only when all nine comparisons pass, the analytic premises
are pinned, and every inherited input is unchanged. In that event
the new tail reduction gives the physical-complement gap
\(1/100000\). Complex nonmain contour currents and a whole-source
conclusion are not part of this calculation.

## 3. Immutable evidence and execution rules

The sole numerical input is
[`research-mixed-contracted-pair-nine-faces.json`](../repro/results/research-mixed-contracted-pair-nine-faces.json),
SHA-256
`174752c3b6f5c026dc4153287e153515d7f94e12959a0188f188d4cbf4d42cbc`.
Its reviewed generating script has SHA
`94b35c6d1877737ca020d128e52a6bde77416ecbebc9d4c6ed01d82c1eb415ac`,
and its original protocol has SHA
`957aadc2dfc00126dd8474d0f3159081001c565326401adeb8f9d69fe43cfa74`.
The checker verifies all 33 source input bindings before and after
recombination, all nine row/face associations, the saved 32-step
proposal inventory, exact rational support membership, both
original inconclusive faces, and all required finite enclosures.
The [saved diagnosis](research_mixed_contracted_pair_nine_faces_diagnosis.md)
and the original failed result are retained without alteration.

The two new analytic inputs are frozen as follows:

| File | SHA-256 |
| --- | --- |
| `notes/research_mixed_contracted_pair_enlarged_rectangle.md` | `597761e942e2956554fe4f25d22de0156838a880e37c04e4fa8fe843e087f0fc` |
| `notes/research_mixed_contracted_pair_enlarged_tail_reduction.md` | `5652cc1d58beabc5929ef6ff9103abfa3415c06a747338ee1bb2b40efa654eda` |

The new checker is
`experiments/check_mixed_contracted_pair_saved_face_transport.py`.
It uses only the Python standard library and opens the fresh output
`repro/results/research-mixed-contracted-pair-saved-face-transport.json`
with mode `x`. It retains the original source status and each
original comparison, the old support point, the new target face,
all 144 products, the nine exact sums, and every success or failure.
Root and a second reviewer must read the complete finalized proof,
protocol and code before the root's single prescribed execution.
No alternate face, threshold, saved support or transport rule is
selected in response to the result.
