# Stronger plateau curvature from the completed reset certificate

Research deduction, 5 November 2026. This note extracts a quantitative
lower bound already computed on every cell of the completed full-reset
certificate and its independent replay. It performs no new numerical
cover and changes none of the earlier source or phase theorems.

## 1. The actual stored whole-cell lower bounds

Use the original condensed allocated phase \(\phi_{\eta\epsilon}(a,b)\)
of [the full-height reset theorem](research_mixed_full_height_reset.md),
with its original logarithmic root and absolute additive constant. Its
closed unselected parameter rectangles are

\[
 U_3=[.22,.50]+i[-.03,.02],\qquad
 U_4=[.22,.50]+i[-.057,0].
 \tag{1}
\]

Write \(A=-\Re\phi''\), a real symmetric two-by-two matrix.
The original author certificate at 256 bits and its independently run
320-bit saved-witness replay both checked all 64 ordered boundary
products and all 36,325 original cells. Their recorded lower minima are
respectively the following exact dyadic numbers, printed in decimal:

\[
 d_{256}=0.20212584175169467926025390625,\qquad
 d_{320}=0.2021258436143398284912109375.
 \tag{2}
\]

These are not sampled eigenvalues. In the original `test` function,
the affine Newton packet supplies a root enclosure over the **whole**
parameter cell. That full root enclosure and both full parameter balls
are passed to `core.phase`. If its real negative Hessian is enclosed by
entries \(A_{00},A_{01},A_{11}\), the checker first requires positive
diagonals and determinant and then computes

\[
 d_{\rm cell}
 =\operatorname{lower}\!\left(
    \frac{A_{00}A_{11}-A_{01}^{2}}{A_{00}+A_{11}}\right).
 \tag{3}
\]

The `.lower()` result is an exact outward endpoint. The running minimum
is taken over these endpoints on every accepted leaf. The saved replay
uses every same leaf and root witness; it does not replace the boxes
by their midpoints or omit the wider cells. The newly archived replay
is byte-identical to that previously completed 320-bit review. The
focused checker below validates both current provenance chains, the
complete exact partitions, the identical rational witnesses, and (2).
It does not claim to rerun those numerical inequalities.

For a positive two-by-two matrix with eigenvalues
\(0<\lambda_1\le\lambda_2\),
\(\det A/\operatorname{tr}A=\lambda_1\lambda_2/(\lambda_1+\lambda_2)
<\lambda_1\). Thus each stored bound is a lower bound for the
least eigenvalue of every actual matrix in its cell. Both numbers
in (2) exceed \(1/5\).

## 2. Harmonic extension and the cyclic Hessian

**Theorem 1.** On every full product of the typed rectangles (1),

\[
                         -\Re\phi''>\frac15 I_2.
 \tag{4}
\]

Indeed, for a fixed real vector \(v\), the function
\(-\Re[v^T\phi''v]\) is harmonic separately in the two complex
parameters. The established original source branch is holomorphic on
a neighborhood of the closed products. The two minimum principles
therefore extend the uniform boundary lower bound in (2) throughout
the product. This argument uses fixed quadratic forms, not harmonicity
of an eigenvalue or determinant quotient.

For an original cyclic word let \(\Phi=\sum_j\phi_j\) be its
condensed outer action. Every vertex belongs to two original edge
incidences. Summing (4) consequently gives

\[
                        -\Re\Phi''>\frac25 I_m.
 \tag{5}
\]

This includes a one-cycle: its one block is evaluated on the diagonal,
so the input direction is \((v,v)\) and its squared norm is
\(2|v|^2\). The two edges of a two-cycle remain distinct. No
change of the original phase allocation or scalar normalization is made.

In particular, at fixed unselected reference heights on the plateau
\(P=[.22,.45]\), the individual real supporting-plane loss is

\[
 \Re\{\phi_j(z)-\Gamma_j(z)\}
 \le-\frac1{10}\left[
 (\Re z_{j-1}-\Re r_{j-1})^2+(\Re z_j-\Re r_j)^2\right].
 \tag{6}
\]

This is the straight-segment Taylor formula with (4); the displacement
is real and the segment stays in (1). The sharper cyclic constant
\(\mu=2/5\) is therefore available wherever the earlier arguments
used the weaker plateau constant \(1/2000\). The original full-reset
upper estimate \(A+B A^{-1}B<20I\) remains unchanged. No selected
positive-height Hessian bound is inferred from (4).

## 3. A stronger additive occupation constant

Keep the exact clamp, symbols and hybrid contour of
[the occupation theorem](research_mixed_nonlow_occupation_loss.md).
Thus \(y_j=\max\{.22,\min\{x_j,.45\}\}\),
\(a_j=\Re r_j\), and

\[
 p_j=\min\{1,\sigma_j+400(y_j-a_j)^2\},\qquad
 \kappa_*=\frac1{4000},\qquad
 \omega_j^*=\kappa_*p_j+\frac{(x_j-.45)_+}{10}.
 \tag{7}
\]

**Corollary 2.** For every fixed cyclic word, all original selections
and all targets in \([.1,.5]^m\), its true upper phase obeys

\[
                  \mathcal E_S\le M-\sum_j\omega_j^*.
 \tag{8}
\]

Only three constants in the existing occupation proof need to be
strengthened; all its transport and incidence steps remain the same.
For an unchanged unselected edge, (6) supplies at least
\((y_j-a_j)^2/10\) to its assigned center. Since
\(p_j\le400(y_j-a_j)^2\) when that center was unselected,
this pays \(p_j/4000\). An unchanged edge with a retained selected
endpoint instead has the existing phase loss \(1/100>1/4000\).
If the selected center was removed by right clamping, then
\(y_j=.45\), \(a_j<.39\), and
\((.06)^2/10=.00036>1/4000\), which pays its original
penalty \(p_j=1\).

For early vertices, retain the exact reserve already proved before its
rounding to \(n_B/1000\):

\[
 \frac{n_B}{100}-\frac{33651}{2000000}d
 \ge\frac{6349}{4000000}n_B
 >\frac{5}{4000}n_B,
 \qquad 2d\le n_B.
 \tag{9}
\]

The radius-two neighborhood contains at most \(5n_B\) distinct
vertices, each with \(p_j\le1\), so (9) pays all its new
penalties. The unused reserve is \(1349n_B/4000000>0\) when
\(n_B>0\). Clean edges outside that neighborhood are still assigned
injectively and retain their losses independently of the early charges.
The original right-clamp gain is unchanged. These observations prove
(8), with the same loop and parallel-edge treatment as the occupation
proof.

The continuous anchored-potential construction applies to
\(w_j+\omega_j^*\) exactly as before. Consequently the
[weighted-transfer support estimate](research_mixed_nonlow_weighted_transfer.md),
equation (13), holds with the new potential and \(\omega_j^*\).
This sharpens its support-loss coefficient by a factor of 800. It remains
an upper estimate for the stated finite kernels, not a spectral gap,
an almost-invariant vector, or a nonzero matrix coefficient. No joint
word-length/level uniformity is asserted for the finite prefactors.

```sh
python3 experiments/check_mixed_extracted_plateau_curvature.py
```

The focused checker performs exact extraction and provenance checks
only. It neither samples a new domain nor reinterprets floating
diagnostics as certificate inputs. All earlier proof files remain
unchanged.
