# Signed original-source diagnostic on the marked six-rim bipyramid

The finite evaluations below give no contrary hint to the proposed strict
remainder gap. They do not prove that gap, estimate the continuous
spectral supremum, or provide a filled-invariant asymptotic. All values
are signed contractions of the original raw spectral numerator.

## Source and implementation

The equator has size \(m=6\), north spokes are matched at odd indices,
and south spokes at even indices. The protected faces are the north
face and \(z_0\). At quantum level \(N\), write \(d=N-1\).
The coefficient extracted is
\[
 [S^dz_1^d\cdots z_5^d]\prod_{j=0}^5F_j,
 \qquad
 F_j=
 \begin{cases}
 H_{V_N(\sigma_j)}(0,z_{j-1},z_{j+1},z_j),&j\text{ odd},\\
 H_{V_N(\sigma_j)}(S,z_{j+1},z_{j-1},z_j),&j\text{ even}.
 \end{cases}
 \tag{1}
\]
Here \(z_0=0\), all indices are cyclic, and
\(\chi_N(\sigma)=2T_N(\sigma/2)+2\). The local numerator is the
full polynomial \(V_N=(\chi_N(\sigma)-\chi_N(C))/(\sigma-C)\).
It is built from the original upper-band matrix before any path
restriction. With \(c_j=2\cos((2j+1)\pi/N)\) and
\(s_j=2\sin(j\pi/N)\), its division-free path recurrence is
\[
 P_{ii}=1,\qquad
 P_{ij}=-s_j^2(1+S)P_{i,j-1}
       -s_js_{j-1}S(\sigma-c_{j-1})P_{i,j-2},
 \tag{2}
\]
with the absent second term omitted at the first step. Multiply by
every unused prefix and suffix factor to obtain \(V_{ij}\).
The NORTH rows use \(S=0\). SOUTH rows retain each coefficient in
the single common \(S\), with its original rim degree. No matrix
inverse or division by a vanishing spectral factor is used.

CROSS means \(i\le\lfloor d/2\rfloor\) and
\(j\ge\lceil d/2\rceil\); this includes the odd central row.
The cyclic transfer retains two pending rim degrees. Its marked step
raises their sum by \(d\), and each south step lowers it by its
actual \(S\)-degree. Closed paths therefore have total south degree
exactly \(d\). Evaluating the assembled trace at the common
\(S=1\) is legitimate by this homogeneity; the individual south
coefficients have not been summed independently.

The output contains FULL, CROSS and their signed difference
\(D_N=\mathrm{FULL}-\mathrm{CROSS}\), the trace diagonal, and the
largest stored partial transfer entry. It does not replace either
trace by absolute local coefficients. No filling functional, framing
phase or modified-dimension factor is applied. No power of \(N\)
has been divided out of this raw source.

## Calibrated comparison and sample values

The original marked packing uses rim curvatures
\((0,1,3,4,3,1)\) and south curvature \(4/3\). The north
curvature is zero. For each original triangle with curvatures
\(x,b,y\), put \(\Delta=\sqrt{xb+by+yx}\) and
\(\theta_j=2\arctan(a_j/\Delta)\), where
\((a_1,a_2,a_3)=(x,b,y)\). The calibrated complete action is
\[
 F(x,b,y)=\frac{1}{2\pi}
 \left\{
 2\sum_j\left[\Lambda(\theta_j/2)
       +\Lambda((\pi-\theta_j)/2)\right]
       +\sum_{a_j>0}\theta_j\log a_j
 \right\},
 \tag{3}
\]
with \(F(x,0,0)=\tfrac12\log x\). Summing the twelve original
triangle actions and subtracting each ordinary face logarithm once
gives
\[
 \Phi=6.4613189443890102818727302144761278814448368156\ldots,
 \qquad 2\pi\Phi=40.59766425638614500084810217098081143767\ldots.
 \tag{4}
\]
This uses the absolute normalization of
`actual_original_boundary_stationary_character.md`, equation (11),
and the original shared action in
`actual_balanced_terminal_fan_volume.md`, equation (A8).
It is the drilled complete action, not a filled volume.

The primary run covers all 64 endpoint tuples in \(\{-2,2\}^6\),
plus one recorded interior tuple, at every \(N=3,\ldots,12\).
Selected extensions reach \(N=32\). There are 679 distinct tuples
in the saved combined data. The table shows
\(N^{-1}\log|D_N|-\Phi\); a blank asymptotic conclusion is intentional.

| Level | All \(-2\) | North \(+2\), south \(-2\) | Only \(\sigma_5=+2\), others \(-2\) |
|---:|---:|---:|---:|
| 12 | −0.2362133041 | −2.2264365716 | saved in full endpoint data |
| 16 | −0.2310863668 | −2.2598436612 | not sampled |
| 24 | −0.2498506151 | −2.3170522515 | not sampled |
| 25 | exactly zero remainder | −2.3252012597 | −0.3080134842 |
| 32 | −0.2725428873 | −2.3591148249 | −0.3090039772 |

For example, at \(N=32\) with north \(+2\), south \(-2\),
the FULL rate relative to \(\Phi\) is approximately
\(-5.564199644\), whereas CROSS and the difference both have
rate approximately \(-2.359114825\). Thus substantial cancellation
occurs between CROSS and the other sectors. The smallest full answer
is about 49 decimal orders below the largest stored intermediate
entry in that contraction. That ratio is a cancellation diagnostic,
not a rigorous condition number.

## Independent checks and precision

The primary 160-digit run checks 4,080 polynomial coefficients of
\((\sigma I-C(S))V=\chi_N(\sigma)I\), at three spectral values
per level. Its largest normalized residual is below
\(10^{-160}\). At levels 3–6 the path numerator is also compared
with direct matrix powers and polynomial division.

Eight full multivariate coefficient checks at levels 3 and 4 construct
the actual homogeneous matrix \(C(x,y)\) directly in the global
face variables. They do not use the cyclic transfer's south-degree
index map. At level 3, direct integer polynomial multiplication
independently checks all 128 FULL/CROSS endpoint values, using
\(V_3=C^2+\sigma C+(\sigma^2-3)I\).

Across the primary 100- and 160-digit runs, all 1,939 nonzero quantities
agree at all 80 stored significant digits. The eleven zero entries are
recorded separately: ten follow from the odd support identity below,
and the remaining level-3 zero is checked by the integer construction.
Twenty-seven overlapping quantities from the selected 160/220-digit
runs likewise agree at all 80 stored digits. This is a precision
comparison, not an interval-arithmetic certificate.

The separate exact support proof
`md-undecorated-cancellation-bipyramid-odd-one-exception.md` shows, for
every odd level and every even equator size in the stated source, that
\(D_N(\sigma_0,-2,\ldots,-2)=0\) identically in \(\sigma_0\).
It retains the odd central row and the two protected endpoint degrees.
It does not apply to a regularized derivative reference numerator.

A further independent integer check confirms the full level-3 source
at \((2,0,2,2,2,2)\) is 910845, and replacing positions 1 or 2
by the identity coupon gives 115587 or 243. The corresponding sewn
four-band current is exactly \(-2051892\), so an automatic global
current cancellation cannot be assumed. This is separate from the
remainder-gap question.

## Reproduction

All runners are portable Python files in this directory. The diagnostic
requires `mpmath`; the exact sewn-current check uses only the standard
library. The main commands are:

```sh
python3 md-undecorated-cancellation-bipyramid-diagnostic.py --all-endpoints --precision 160 --output md-undecorated-cancellation-bipyramid-final-results.json
python3 md-undecorated-cancellation-bipyramid-diagnostic.py --levels 14,16,20,24,32 --precision 160 --cases all_minus,north_plus_south_minus,north_minus_south_plus,interior --output md-undecorated-cancellation-bipyramid-final-extended-results.json
python3 md-undecorated-cancellation-bipyramid-diagnostic.py --levels 12,25,32 --precision 220 --all-endpoints --cases all_minus,north_plus_south_minus,endpoint_mmmmmp,interior --output md-undecorated-cancellation-bipyramid-final-220-results.json
python3 md-undecorated-cancellation-bipyramid-exact-sewn-current.py
python3 md-undecorated-cancellation-bipyramid-precision-summary.py
```

The summary also reads the preserved 100-digit primary replay and the
selected odd-level extension. Their exact commands and all input and
output hashes are retained in the accompanying manifest. Earlier
temporary runs remain preserved. No repository source was changed.
