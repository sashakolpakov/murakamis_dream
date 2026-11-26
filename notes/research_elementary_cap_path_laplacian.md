# An exact path Laplacian in the original crossing algebra

Research note, 3 November 2026.

One elementary conjugate of the original cap operator is a weighted
path Laplacian after multiplication by explicit unitary matrices.
This gives its complete finite normalization, an explicit Green
matrix, and a polynomial lower bound for every nonzero singular
value. The identities hold at both parities and retain the original
repeated-root algebra.

This is a statement about one trace generator. The closing minor
of the negative two-power word already has a
[diagonal-gauge obstruction](research_negative_pair_diagonal_gauge_obstruction.md).
The positive energy below therefore cannot be iterated by assuming
that every rational-word cap has the same diagonal gauge.

## 1. The finite matrices and the endpoint

Let \(N\ge2\), \(D=N-1\), \(q=e^{\pi i/N}\), and \(Q=q^2\).
All coordinate indices run from \(0\) to \(D\). Let \(M\) be the
original crossing matrix in the normalized Newton basis,
\(Z\) multiplication by \(z\), and \(L=Z^T\). Thus
\[
 Z_{jj}=qQ^j+q^{-1}Q^{-j},\qquad
 Z_{j+1,j}=-4\sin^2((j+1)\pi/N),\qquad
 c_0=q+q^{-1}.
 \tag{1}
\]
These are the full matrices of
\(\mathbb C[z]/(2T_N(z/2)+2)\), not their reductions to distinct
spectral values. Set
\[
                       L_1=M^{-1}LM.
 \tag{2}
\]
The [original trace-algebra calculation](research_rational_word_normalized_cofactor.md)
gives
\[
 \begin{split}
 (L_1)_{jj}&=4qQ^j-q(1+Q)Q^{2j},\\
 (L_1)_{j,j+1}&=(L_1)_{j+1,j}=-(1-Q^{j+1})^2 .
 \end{split}
 \tag{3}
\]
Formula (3) is valid also at \(N=2\); no division by
\(q^2-q^{-2}\) is used.

Introduce the unitary cyclic matrices
\[
 X\mathbf e_j=Q^j\mathbf e_j,\qquad
 E\mathbf e_j=\mathbf e_{j+1\bmod N},\qquad XE=QEX.
 \tag{4}
\]
For example the exact finite Newton matrices are
\[
 \begin{split}
 Z&=qX+q^{-1}X^{-1}+(X+X^{-1}-2)E,\\
 L&=qX+q^{-1}X^{-1}+(QX+Q^{-1}X^{-1}-2)E^{-1}.
 \end{split}
 \tag{5}
\]
The apparent wrap entries in (5) vanish. Thus the cyclic notation
does not replace the original finite endpoint by a periodic
boundary condition.

## 2. The quantum factor and its positive form

Put
\[
 A=I+qE,\qquad
 P=(I-QX)^\dagger(I-QX)
       =2I-QX-Q^{-1}X^{-1}.
 \tag{6}
\]
Its diagonal entries are
\[
       p_j=4\sin^2((j+1)\pi/N),\quad 0\le j<D,
       \qquad p_D=0.
 \tag{7}
\]

**Theorem 1.** The original operator has the exact factorization
\[
 \boxed{\quad
 L_1-c_0I=-q^{-1}(I+qE)(I-QX)^2(I+qE^{-1})
                   =q\,A P A^\dagger X .
 \quad}
 \tag{8}
\]
In particular \(H=q^{-1}(L_1-c_0I)X^{-1}=APA^\dagger\)
is Hermitian positive semidefinite.

*Proof.* Since \(Ef(X)=f(Q^{-1}X)E\), expansion of the
first product in (8) has lower and upper diagonals
\(-(I-X)^2E\) and \(-(I-QX)^2E^{-1}\). Its diagonal is
\[
 -q^{-1}(I-QX)^2-q(I-X)^2
       =4qX-q(1+Q)X^2-c_0I.
 \tag{9}
\]
This is (3), including the zero wrap entries. Next
\[
 (I-QX)^2=-QXP,\qquad
 I+qE^{-1}=X^{-1}A^\dagger X.
 \tag{10}
\]
Substitution in the first expression gives the second. \(\square\)

The separate factors in the first formula must not be inverted
without checking parity:
\[
 \det(I+qE)=\det(I+qE^{-1})=1+(-1)^N.
 \tag{11}
\]
For odd \(N\) both have rank \(N-1\). The middle factor has
rank \(N-1\) at every level. The product nevertheless has
exactly rank \(N-1\), as the next calculation proves without
dividing by any of these factors.

## 3. The weighted path, with its actual endpoints

Let \(U\) be the diagonal unitary matrix
\[
                         U_{jj}=(-q)^j.
 \tag{12}
\]
Because \(p_D=0\), the last cyclic column of \(A\) has no
contribution to \(APA^\dagger\). For \(0\le j<D\),
\[
 U^\dagger A\mathbf e_j
                  =(-q)^{-j}(\mathbf e_j-\mathbf e_{j+1}).
 \tag{13}
\]
Consequently
\[
 \boxed{\quad
 \Delta_N:=U^\dagger H U
       =\sum_{j=0}^{D-1}
          p_j(\mathbf e_j-\mathbf e_{j+1})
              (\mathbf e_j-\mathbf e_{j+1})^\dagger .
 \quad}
 \tag{14}
\]
This is the path with vertices \(0,\ldots,D\), and with
conductance \(p_j\) on edge \((j,j+1)\). In particular there
is no edge \((D,0)\).

All \(D\) conductances in (14) are strictly positive. Therefore
\[
 \operatorname{rank}\Delta_N=N-1,\quad
 \ker\Delta_N=\mathbb C\mathbf1,\quad
 \ker H=\mathbb C v,\qquad
                       v_j=\frac{(-q)^j}{\sqrt N}.
 \tag{15}
\]
The phases in \(v\) apply to both parities. At odd levels
\(A^\dagger v=0\); at even levels \(A^\dagger v\) is a
multiple of the last coordinate, which \(P\) kills.

The passage from \(L_1-c_0I\) to \(H\) is a unitary
right multiplication and scalar multiplication, **not**
a similarity. It preserves singular values, but does not
assert that the original double zero eigenvalue becomes
semisimple in the quotient. Indeed
\[
 \ker(L_1-c_0I)=\mathbb C X^{-1}v,\qquad
 \operatorname{im}(L_1-c_0I)=v^\perp,\qquad
                       v^\dagger X^{-1}v=0.
 \tag{16}
\]
Thus the original kernel still lies in the image, as required
by its endpoint Jordan block.

## 4. Exact cofactors and Green matrix

Deleting any one row and the same column of \(\Delta_N\)
gives determinant
\[
       \prod_{j=0}^{D-1}p_j
       =\left|\prod_{r=1}^{N-1}(1-Q^r)\right|^2=N^2.
 \tag{17}
\]
For a direct proof of the first equality, write (14) as
an incidence matrix times \(\operatorname{diag}(p_j)\)
times its transpose. Deleting one vertex leaves a square
path incidence matrix with determinant \(1\) or \(-1\).
The second equality follows by evaluating
\((x^N-1)/(x-1)\) at \(x=1\).

The product of the \(N-1\) positive eigenvalues is therefore
\[
                    \operatorname{pdet}H
                    =\operatorname{pdet}\Delta_N=N^3.
 \tag{18}
\]
Indeed the coefficient of the linear term in
\(\det(\Delta_N+tI)\) is the sum of its \(N\) principal
cofactors. Equivalently,
\[
             \operatorname{adj}(H)=N^3vv^\dagger.
 \tag{19}
\]
These constants agree with the original normalized cofactor
identity for \(W=M^{-1}\), since all \(N\) Newton
coefficients of \(R^{-1}\) have modulus one.

Pin vertex \(0\), and let \(\Delta_N^{[0]}\) denote the
remaining \(D\times D\) principal matrix. Its inverse is
explicit:
\[
 \boxed{\quad
 (\Delta_N^{[0]})^{-1}_{ab}
       =\sum_{j=0}^{\min(a,b)-1}\frac1{p_j},
             \qquad 1\le a,b\le D.
 \quad}
 \tag{20}
\]
To check (20), the difference across edge \(j\) is \(1/p_j\)
until the source vertex \(b\), and zero afterwards.
The weighted discrete divergence is consequently the
coordinate source at \(b\), with value zero at vertex \(0\)
and zero outgoing flux at \(D\).

The total endpoint resistance is
\[
 R_N=\sum_{j=0}^{D-1}\frac1{p_j}
                        =\frac{N^2-1}{12}.
 \tag{21}
\]
For completeness, differentiate
\(\sum_{r=0}^{N-1}\cot(x+r\pi/N)=N\cot(Nx)\)
and compare constant terms at \(x=0\). This gives
\(\sum_{r=1}^{N-1}\csc^2(r\pi/N)=(N^2-1)/3\), which is
(21). Thus every entry of (20) is positive and at most
\((N^2-1)/12\).

## 5. A uniform polynomial spectral gap

**Corollary 2.** Every nonzero singular value of the original
operator \(L_1-c_0I\) lies in
\[
 \left[
   \max\left\{\frac{48}{N(N^2-1)},\frac8{3N^2}\right\},\,16
 \right].
 \tag{22}
\]
In particular its Moore--Penrose inverse satisfies
\[
                \|(L_1-c_0I)^+\|
           \le\min\left\{\frac{N(N^2-1)}{48},\frac{3N^2}{8}\right\}.
 \tag{23}
\]

*Proof.* Its singular values equal the eigenvalues of \(H\)
by (8), and hence those of \(\Delta_N\). The upper bound
follows from \(\|A\|\le2\), \(\|P\|\le4\).
For \(\sum_j x_j=0\), write
\(\mathcal E=\sum_j p_j|x_{j+1}-x_j|^2\). Weighted
Cauchy--Schwarz along the subpath from \(a\) to \(b\) gives
\[
 |x_b-x_a|^2\le
       \left(\sum_{j=a}^{b-1}p_j^{-1}\right)\mathcal E.
 \tag{24}
\]
The exact variance identity and a count of the pairs using
each edge give
\[
 \begin{split}
 \|x\|^2
 &=\frac1N\sum_{a<b}|x_b-x_a|^2\\
 &\le\frac{\mathcal E}{N}
       \sum_{j=0}^{D-1}\frac{(j+1)(N-j-1)}{p_j}\\
 &\le\frac{N R_N}{4}\mathcal E
       =\frac{N(N^2-1)}{48}\mathcal E .
 \end{split}
 \tag{25}
\]
This proves the first lower bound, including \(N=2\).

For the second, put \(m=\lfloor N/2\rfloor\) and
\(d_k=x_{k+1}-x_k\). For \(j<m\), weighted
Cauchy--Schwarz and a decreasing-integrand comparison give
\[
 \begin{split}
 |x_j-x_m|^2
 &\le
 \left(\sum_{k=j}^{m-1}(k+1)^{-3/2}\right)
 \left(\sum_{k=j}^{m-1}(k+1)^{3/2}|d_k|^2\right)\\
 &\le\frac3{\sqrt{j+1}}
          \sum_{k=j}^{m-1}(k+1)^{3/2}|d_k|^2 .
 \end{split}
 \tag{26}
\]
Summing in \(j\) and using
\(\sum_{j=0}^{k}(j+1)^{-1/2}\le2\sqrt{k+1}\) yields
\[
             \sum_{j<m}|x_j-x_m|^2
                  \le6\sum_{k<m}(k+1)^2|d_k|^2.
 \tag{27}
\]
Reflection gives the analogous bound on the right with
weight \((N-k-1)^2\). The elementary sine bound gives
\[
 p_k\ge\frac{16}{N^2}
              \min\{k+1,N-k-1\}^2 .
 \tag{28}
\]
The smaller weight is \(k+1\) on the left of \(m\), and
\(N-k-1\) on its right, at either parity. Combining
(27)--(28), and using that the mean minimizes the squared
distance to a constant, gives
\[
       \|x\|^2\le\sum_j|x_j-x_m|^2
                         \le\frac{3N^2}{8}\mathcal E .
 \tag{29}
\]
This proves the second bound. \(\square\)

One can also obtain a weaker \(64/N^4\) bound by comparison
with the unweighted path. Equations (25) and (29) retain,
respectively, the exact endpoint resistance and its
distribution along the path. None of these arguments
discards an odd-level kernel of an individual factor.

## 6. What this controls in the source problem

Equations (20)--(23) give a complete, polynomially conditioned
Green problem for this elementary original cap. They do not
supply a lower bound for a general rational-word closing
minor. Transporting the cap by another original word is a
nonunitary similarity, and its source-selected minor is not
the positive principal minor in (17).

The distinction is concrete: the
[negative \((-4,-5)\) source](research_negative_pair_diagonal_gauge_obstruction.md)
has a nonreal, diagonal-gauge-invariant entry ratio at large
levels. Also the actual \(JM^2\) closing minor has an
[exponentially small singular value](research_rational_word_normalized_cofactor.md),
despite the polynomial elementary gap proved here. A
general proof must control the transported boundary
selection and its cancellations, rather than multiply
elementary spectral gaps.

The [finite original-matrix check](../experiments/check_elementary_cap_path_laplacian.py)
compares (8) and (14) with \(M^{-1}LM-c_0I\), checks the
cofactors and pinned Green matrix independently, and tests
the singular-value bounds at both parities. The
[saved result](../repro/results/research-elementary-cap-path-laplacian.json)
records the script and dependency hashes. It is a
normalization diagnostic; the all-level statements are
proved above.
The [150-digit replay](../repro/results/research-elementary-cap-path-laplacian-root.json)
checks nineteen levels and 219 principal cofactors, with maximum
relative error below \(2.5\cdot10^{-146}\).
