# Height-dependent source ceilings at the zero seam

Research proof, 5 November 2026. This note extracts stronger bounds from
completed endpoint certificates. It introduces no new interval cover and
does not compare a boundary potential or prove a whole-period estimate.

## 1. Literal endpoint rows and their allocation

Use the original root of unity \(r_N=e^{-2\pi i/N}\),
\(p_j(X)=(r_NX;r_N)_j\), \(P_j=(r_N;r_N)_j\), and the original
Fourier interpolator \(d_N\). For \(0\le j<N\), \(P_j\ne0\).
The canonical conditional kernel is
\[
 C_{e,N}(X,Y)=\sum_{j=0}^{N-1}
       X^{-j}\frac{p_j(X)p_j(Y)}{P_j^{2+e}}.
 \tag{1}
\]
Put the zero seam in argument \(c\), numbering the arguments zero and
one. Since \(p_j(1)=P_j\), the moving row is exactly
\[
 R^{(c)}_{e,j}(X)=X^{-cj}\frac{p_j(X)}{P_j^{1+e}}.
 \tag{2}
\]
Thus \(c=1\) retains the nonunit complex-first-argument chirp. Let
\(d\in\{0,1\}\) be the moving leg's type indicator and
\(\sigma\in\{0,1\}\), with \(\sigma=0\) if \(d=0\). The allocated
absolute row sum is
\[
 T^{(c)}_{e,d,\sigma,N}(X)
 =\sum_{j=0}^{N-1}|R^{(c)}_{e,j}(X)|
                  |d_N(X)X^{-N\sigma}|^{d/2}.
 \tag{3}
\]
There is no chosen square root of \(d_N\). For \(c=1\), the required
families have arbitrary \(e,d\); for \(c=0\), the moving type is
\(d=e\). The physical height bands are
\[
 \begin{array}{c|c|c}
 d&\sigma&h\\\hline
 0&0&[-.03,.02]\\
 1&0&[-.057,0]\\
 1&1&[0,.014].
 \end{array}
 \tag{4}
\]
All real moving angles \(x\in[0,1]\) are retained, with
\(X=e^{-2\pi i(x+ih)}\).

## 2. Exact extraction of the height knots

The following decimals are exact terminating rationals, extracted from
the \(\kappa=0\) entries of the completed
[endpoint support grid](research_mixed_endpoint_support_grid.md) and
[all-endpoint grid](research_mixed_all_endpoint_support.md).
Each entry bounds the full row and angle square, with both alternatives
of the actual Fourier envelope. Define \(A_{e,d}\) for \(c=1\), and
\(B_e\) for \((c,d)=(0,e)\).

| Profile | Height knots, in increasing order | Certified upper values |
| --- | --- | --- |
| \(A_{0,0}\) | \(-.03,0,.02\) | \(.360050,.325066,.305497\) |
| \(A_{1,0}\) | \(-.03,0,.02\) | \(.485081,.460764,.446493\) |
| \(B_0\) | \(-.03,0,.02\) | \(.296665,.325066,.347548\) |
| \(A_{0,1}\) | \(-.057,-.02,0,.014\) | \(.447948,.404270,.386681,.332579\) |
| \(A_{1,1}\) | \(-.057,0,.014\) | \(.551147,.515591,.465875\) |
| \(B_1\) | \(-.057,0,.014\) | \(.461406,.515591,.487806\) |

At negative type-four heights the saved selection is zero; at \(.014\)
it is one. At height zero the two selected normalizations have identical
modulus, so the same zero-height entry applies to either choice. No
positive-height unselected or negative-height selected claim is made.

On each adjacent knot interval, define the displayed profile by affine
interpolation of its two rational values. For type four use only the
intervals belonging to the corresponding band (4). In particular, the
extra \(-.02\) knot improves the negative \(A_{0,1}\) chord; no such
extra knot is assumed for the other profiles.

**Theorem 1.** For every fixed \(\delta>0\), uniformly in all levels
\(N\ge2\), all angles, and the allowed height and selection bands,
there are constants \(C,K\) such that
\[
 \begin{split}
 T^{(1)}_{e,d,\sigma,N}(e^{-2\pi i(x+ih)})
     &\le C N^K e^{N(A_{e,d}(h)+\delta)},\\
 T^{(0)}_{e,e,\sigma,N}(e^{-2\pi i(x+ih)})
     &\le C N^K e^{N(B_e(h)+\delta)}.
 \end{split}
 \tag{5}
\]
The same bounds hold for the modulus of the corresponding complete
kernel with its moving halfweight. No rows, parity classes, zeros,
selected factors, or forced Fourier terms are removed.

To prove the interpolation, for each fixed row use the actual Laurent
function
\[
 F_{e,d,c,\sigma,j,N}(X)
   =\bigl(R^{(c)}_{e,j}(X)\bigr)^2
          d_N(X)^d X^{-Nd\sigma}.
 \tag{6}
\]
Its modulus is the square of that row's allocated modulus in (3).
It is holomorphic on every closed annulus under consideration. The
completed source estimates at two knots \(h_0<h_1\) give, uniformly
in \(j\), polynomial times \(e^{2N(U_k+\delta)}\) upper bounds
on \(|X|=e^{2\pi h_k}\). Hadamard's three-circles inequality gives
their geometric interpolation. Since \(\log|X|=2\pi h\), its
exponent is precisely the affine interpolation in height. Taking
square roots and summing the \(N\) rows changes only the polynomial
factor. Constants can be enlarged for the finitely many small levels.
This is an argument for finite Laurent functions, not a claim of
global convexity of an individually chosen dilogarithm branch.

The resulting band maxima include the useful selection-dependent bounds
\[
 \begin{array}{c|cc}
 &\sigma=0&\sigma=1\\\hline
 A_{0,1}&.447948&.386681\\
 A_{1,1}&.551147&.515591\\
 B_1&.515591&.515591.
 \end{array}
 \tag{7}
\]
The full affine profiles are sharper when the actual height is known.

## 3. A real seam collar with independent neighbor heights

Let a type star have indicators \((\alpha,\beta,\gamma)\), and let
the real middle coordinate lie in \([0,\ell]\), where
\(0<\ell\le1/1000\) is fixed independently of \(N\). Put
\[
 \nu_\ell=-J(\ell),\qquad
 \Delta_\ell=\ell\log2-J(\ell).
 \tag{8}
\]
The complete [zero-collar bounds](research_mixed_real_zero_collar.md)
give \(|p_j(e^{-2\pi ix})/P_j|\le C N^K e^{N\Delta_\ell}\)
and \(|d_N(e^{-2\pi ix})|\le C N^K e^{N\nu_\ell}\), uniformly
through \(x=0\), every original row, and every product zero.
Apply these separately to the two incident kernels, retaining their
literal chirps. The complex-first chirp is unchanged; the real first
chirp in the other block has modulus one. The middle halfweights
recombine into power \(\beta\), and a middle selected factor has
modulus one. Consequently the product of the two allocated kernel
moduli, and also the product of their absolute row sums, has upper rate
\[
 A_{\beta,\alpha}(h_L)+B_\gamma(h_R)
       +2\Delta_\ell+\beta\nu_\ell+2\delta.
 \tag{9}
\]
The two physical neighbor heights and selections may be independent
within (4). Thus (9) applies to their actual hybrid attenuations without
replacing either height by a reference height or a common fraction.

At a cyclic critical reference, the sum of the original two tangent
planes equals \(\Re(C+P_Lz_L+P_Rz_R)\), independently of the real
middle coordinate, as proved in the
[grouped seam reduction](research_mixed_hybrid_zero_pair_reduction.md).
Subtract that actual plane directly from (9) for a source defect. An
exterior reset cost may be included only if needed by a separate
assembly. In particular the older universal \(G+Q\) gap is not an
additional cost to subtract from this actual-plane comparison.

## 4. Reproduction and scope

The focused checker verifies all 225 original grid keys, their complete
binary covers, all selection labels, and both saved independent replay
bindings and per-grid source counts. It extracts the 19 zero-slope
knots, checks all 13 affine segments and the band maxima (7), and binds
the unchanged collar and source proofs. It does not recompute the old
outward cells, introduce a new cover, or optimize a geometric defect.

```sh
python3 experiments/check_mixed_height_resolved_seam_sources.py
```

These are complete finite-source upper bounds. A boundary-potential
comparison, a uniform seam gap, and whole-period noncancellation remain
separate questions.
