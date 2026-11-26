# Five remaining comparisons for the selected first two blocks

Research deduction, 6 November 2026.

For a chain beginning with a four-twist block and then a three-twist
block, the complete finite expression at its first selected coordinate
now reduces to five comparisons. This note states that reduction
precisely. It does not assign a negative sign to the five remaining
quantities.

## 1. The exact expression and the contributions already bounded

Keep every convention of the
[finite two-block reduction](research_mixed_selected_four_three_finite_reduction.md).
The chain has length at least three. Its original geometric critical
point determines the heights \(h_e,h_s,c,h_b\), the real geometric
action \(M\), and the outgoing affine term \(\ell_b(v)\). The incoming
coordinate is moved to \(z=y+iH\), with \(H=7/625\), while
\(b=v+ih_b\) and \(y,v\in P=[.22,.45]\).

The finite expression being bounded is
\[
 \mathcal K_N(w;X,Y)
 =U_{1,N}(w,X)C_{0,N}(X,Y)d_N(X)X^{-N},
 \quad X=e^{-2\pi iz},\quad Y=e^{-2\pi ib}.
 \tag{1}
\]
The first factor contains its entire private sum and the original
endpoint coefficient. The second contains its entire ordinary sum.
The last two factors are the complete Fourier polynomial and the
selected monomial; neither is replaced by a value at the critical
point.

For the cap, \(A_0\) is the maximum on the original horizontal
private contour, \(A_L,A_R\) are its real endpoint values, and
\(A_-,A_+\) are the two other horizontal Fourier-contour rates,
including their penalties. For the ordinary block, \(B_0\) is the
maximum on its original horizontal contour; \(B_L,B_R\) are the
real-index values at \(3/20,1/2\), and \(B_1\) bounds its last
rows. Their formulas are (6) and (14) of the cited reduction.
The two rates bounding the same complete selected Fourier factor are
\[
 W_{\rm fac}(y)=-\Re g(y+iH)-2\pi H,\qquad W_{\rm force}(y)=0.
 \tag{2}
\]

The following comparisons are proved on this whole target domain:

| Contributions | Proved comparison | Source |
|---|---|---|
| Both original horizontal contours | \(A_0+B_0+W_\sigma<M+\ell_b-1/500\) | [Central comparison](research_mixed_first_four_next_three_central_gap.md) |
| Any cap contribution and the last ordinary rows | \(A_i+B_1+W_\sigma<M+\ell_b-3/100\) | [Last-row estimate](research_mixed_selected_four_three_last_rows.md) |
| Additional cap Fourier contours | \(A_-<A_0-1/4,\quad A_+<A_0-1/50\) | [Cap contour comparison](research_mixed_selected_cap_alias_transport.md) |
| Small ordinary indices | \(B_L<B_0-1/125\) | [Left-row comparison](research_mixed_selected_three_left_rows.md) |

Every line retains the same original reference and boundary targets.
In the first two lines \(\sigma\) can be either alternative in (2).
The last two lines can consequently be added to any of the other
factor's rates without maximizing their reference data separately.

## 2. The five quantities still to be bounded

Set
\[
 \mathcal I_5=\{(0,R),(L,0),(R,0),(L,R),(R,R)\}
 \tag{3}
\]
and define the real defect
\[
 D_5(y,v)=
 \max_{\substack{(i,j)\in\mathcal I_5\\
                  \sigma\in\{\mathrm{fac},\mathrm{force}\}}}
 \{A_i(y)+B_j(y,v)+W_\sigma(y)-M-\ell_b(v)\}.
 \tag{4}
\]
Thus three quantities involve the ordinary real index \(1/2\):
one uses the cap's original contour and two use its real endpoints.
The other two involve a cap endpoint and the ordinary original
contour. Each has two Fourier alternatives.

**Proposition 1.** For every \(\tau>0\) and fixed ordinary-color
derivative order \(k\), the exact expression (1) satisfies
\[
 |\partial_w^k\mathcal K_N(w;X,Y)|
 \le C_{\tau,k}N^{B_{\tau,k}}
  \exp N\left\{M+\ell_b(v)
           +\max\{-1/500,D_5(y,v)\}+\tau\right\}.
 \tag{5}
\]
The estimate holds for both parities of \(N\), uniformly on \(P^2\)
and a sufficiently small fixed ordinary-color disk.

*Proof.* The complete finite reduction bounds the product by the
maximum of all five cap rates plus all four ordinary rates and either
full Fourier rate. First remove every pair with \(B_1\), using the
last-row comparison. Replace \(B_L\) by \(B_0\) wherever it occurs.
Replace either cap Fourier-contour rate by \(A_0\).
The only remaining pairs are \(i\in\{0,L,R\}\),
\(j\in\{0,R\}\). The pair \((0,0)\) has its established
gap \(1/500\); the other five are exactly (3).
Each discarded rate is pointwise bounded above by its replacement.
The same finite reduction
already includes polynomial prefactors, contour joins, half-grid
rounding, and the color dependence of the complete endpoint
coefficient. Allocate its arbitrarily small rate tolerances to sum to
\(\tau\). This proves (5). \(\square\)

It follows that a bound
\[
 D_5(y,v)\le-\delta,\qquad \delta>0,
 \tag{6}
\]
uniform on the actual references and \(P^2\), would give a gap
\(\min(\delta,1/500)\) for the whole expression (1).
Equation (6) remains unproved.

The three half-row quantities have
[explicit scalar upper bounds](research_mixed_selected_four_three_half_row_majorant.md).
That proof maximizes the outgoing real coordinate exactly and uses
concavity to bound the remaining real targets. Their six resulting
sign tests are still open. The two cap-endpoint/ordinary-contour
quantities need their own estimate.

## 3. What has been settled without those five signs

The first line of the table and the left-row comparison already give
gap \(1/100\) for the cap's main contour paired with the lower
ordinary tail. Replacing the cap main contour by either of its
additional Fourier contours improves this gap. The two additional
cap contours paired with the ordinary main contour are also below
the geometric rate.

In contrast, replacing a cap endpoint paired with \(B_L\) by that
same endpoint paired with \(B_0\) only reduces it to one of the
open tests. Similarly, a cap Fourier contour paired with \(B_R\)
reduces to the still-open \((0,R)\) test. These are eliminations of
independent comparisons, not additional conclusions about their
absolute geometric rates.

Even proving (6) would settle this specified boundary expression,
not the complete volume conjecture. Other selections near the ends,
noncentral integration regions, the separate length-two case, and
arbitrary fixed short fillings remain outside this proposition.
