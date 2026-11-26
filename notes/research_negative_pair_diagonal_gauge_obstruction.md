# A diagonal-gauge obstruction in a negative two-power source

Research note, 3 November 2026.

The normalized determinant for a rational word suggests looking for
a positive matrix after diagonal rescaling. That mechanism already
fails for the original two-vertex source with distinct negative
powers \(-4,-5\). The obstruction persists at arbitrarily large
levels of both parities. It is an exact local cross ratio of
matrix entries, not a numerical test of determinant signs.

This rules out diagonal row and column gauges to a real matrix.
It does not rule out a coupled block Schur reduction or a contour
proof of the original source.

## 1. The exact source and its closing minor

Use the original Newton matrices \(M,J,Z,L=Z^T\) and the
normalization of
[the rational-word determinant](research_rational_word_normalized_cofactor.md).
Take
\[
 W_N=M^{-5}JM^{-4},\qquad
 F_N=W_N\mathbf e_0,\qquad
 \mathcal Z_N=\mathbf e_D^TF_N
      =\phi_N\!\left(R^{-5}T(R^{-4})\right),
 \quad D=N-1.
 \tag{1}
\]
The actual cap matrix and its closing minor are
\[
 \mathcal D_N=W_N(L-c_0I)W_N^{-1},\qquad
 \mathcal B_N=\mathcal D_N[\{1,\ldots,D\},\{0,\ldots,D-1\}].
 \tag{2}
\]
They retain the full original quotient and both spectral normals.
In particular
\[
                   (-1)^D\det\mathcal B_N=N^2|\mathcal Z_N|^2.
 \tag{3}
\]
There is no added final turn in (1); such a turn would change
the closing functional and could remove the last power.

## 2. A gauge-invariant local ratio

For a matrix \(B\), suppose the four entries in two rows \(r,r+1\)
and two columns \(s,s+1\) are nonzero. Define
\[
 \mathcal R(B;r,s)
   =\frac{B_{r,s}B_{r+1,s+1}}
          {B_{r,s+1}B_{r+1,s}}.
 \tag{4}
\]
Left and right multiplication by arbitrary invertible complex
diagonal matrices leaves (4) unchanged. If such a multiplication
made all four entries real, their ratio would be real.
Consequently a nonreal ratio prevents any diagonal row/column
gauge from making the whole matrix real, and a fortiori from
making it entrywise nonnegative.

This test allows more than phase gauges or positive weights:
the diagonal entries may have arbitrary nonzero modulus and phase.

## 3. The original bulk coefficients

Put \(X=e^{2\pi ix}\), and let \(Y\) record a column offset
from its row. At \(q=1\) the three exact trace generators
have the Laurent symbols
\[
 \begin{split}
 z&=X+X^{-1}+(X+X^{-1}-2)Y^{-1},\\
 l&=X+X^{-1}+(X+X^{-1}-2)Y,\\
 b&=4X-2X^2-(1-X)^2(Y+Y^{-1}).
 \end{split}
 \tag{5}
\]
These are the actual Newton bulk coordinates, not assigned
peripheral variables. Define the finite sequence
\[
 L_0=l,\quad L_1=b,\quad
                   L_{k+1}=8-zL_k-L_{k-1}.
 \tag{6}
\]
For the word (1), its cap symbol is \(U_4-2\), where
\[
 U_0=z,\quad U_1=L_4,\quad
                   U_{k+1}=8-L_5U_k-U_{k-1}.
 \tag{7}
\]
To verify the order, first transport \(L\) by \(M^{-4}\),
giving \(L_4\). A turn substitutes
\((Z,L,L_1)\mapsto(L,Z,L_{-1})\).
The final \(M^{-5}\) then substitutes
\[
                    (Z,L,L_1)\mapsto(L_5,Z,L_4).
 \tag{8}
\]
The exact noncommutative recurrence gives (7) after \(q\to1\).
Thus no independent classical model has been inserted.

At \(X=i\), equations (5) become
\[
 z=-2Y^{-1},\qquad l=-2Y,\qquad
                    b=2+4i+2i(Y+Y^{-1}).
 \tag{9}
\]
The short recurrences (6)--(7), using only Gaussian integers,
give the following three coefficients of \(U_4-2\):
\[
 \begin{array}{c|r}
 \text{offset}&\text{coefficient}\\ \hline
 -19&-524288\\
 -18&-4194304+2097152i\\
 -17&-10092544+16777216i .
 \end{array}
 \tag{10}
\]
They are nonzero, and direct integer arithmetic gives
\[
 \frac{d_{-18}^2}{d_{-19}d_{-17}}
                   =\frac{47552+4864i}{22313}.
 \tag{11}
\]
In particular the imaginary part is strictly positive.

## 4. Passage to the actual finite matrices

The entries of \(\mathcal D_N\) at every fixed bulk offset
are Laurent polynomials in \(q\) and \(Q^j\), where
\(q=e^{\pi i/N}\), \(Q=q^2\), and \(j\) is the row index.
This was proved directly from the three finite-band generators
in the normalized determinant note. At a bounded distance from
the finite endpoints, the same polynomial gives the exact
entry; no asymptotic recurrence solution is used.

Choose \(j_N=\lfloor N/4\rfloor\). For all sufficiently large
\(N\), use rows \(j_N,j_N+1\) and columns
\(j_N-18,j_N-17\) of \(\mathcal D_N\).
These rows and columns belong to the closing minor (2).
Their four entries converge, respectively, to
\[
                         d_{-18},\ d_{-17},\
                         d_{-19},\ d_{-18}.
 \tag{12}
\]
Indeed \(q\to1\), \(Q^{j_N}\to i\), and changing the row
by one does not change this limit. The convergence has error
\(O(N^{-1})\) because the finite Laurent formulas are smooth
near \((q,X)=(1,i)\). In particular the entries are nonzero
for sufficiently large \(N\).

Their gauge-invariant ratio therefore converges to (11).
Its imaginary part remains positive for all sufficiently
large levels, through both parities. By (4), no invertible
complex diagonal row and column rescalings can make
\(\mathcal B_N\) real at those levels.

## 5. Consequence for a positivity approach

The exact positive scalar in (3) is compatible with this
obstruction: positivity of the final determinant does not
make its individual entries positive after local rephasing.
Thus a proof for general negative chains cannot rely on
such a diagonal gauge of their original closing minors.
It would need a coupled block structure, an exact cancellation
identity, or a selected complex cycle. No assertion about
those alternatives is made here.

The [exact symbolic verifier](../experiments/check_negative_pair_diagonal_gauge_obstruction.py)
reconstructs (6)--(10) over the Gaussian integers and proves
(11) by rational arithmetic. Its
[saved result](../repro/results/research-negative-pair-diagonal-gauge-obstruction.json)
records the source hash. This is a finite algebra check of
the displayed coefficients; the passage to all sufficiently
large levels is the Laurent-coefficient argument in Section 4.
