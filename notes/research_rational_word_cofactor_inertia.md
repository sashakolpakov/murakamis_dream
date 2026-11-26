# The inertia of the original rational-word cofactor

Private written proof, 15 November 2026.

The Hermitian matrix underlying the exact rational-word determinant has
both positive and negative directions at every sufficiently large level.
Its signature is independent of the signed word. If the original closing
scalar is nonzero, its closing principal minor has exactly that same
nonzero signature. Thus positivity of the normalized adjugate does not
make this minor positive semidefinite.

This concerns the specified original matrices. It does not exclude a
different determinant representation obtained by a new source identity.

## 1. The original matrices and the closing minor

Let (N\ge2), (D=N-1), and put
\[
 c_j=2\cos((2j+1)\pi/N),\qquad
 b_j=-4\sin^2(j\pi/N),\qquad
 J_{ij}=\mathbf1_{i+j=D}.
\]
In the full Newton basis, multiplication by the spectral coordinate is
the lower bidiagonal matrix (Z) with diagonal (c_j) and subdiagonal
(b_j). Set (L=Z^{\mathsf T}=JZJ). Let (M) be multiplication by
the original positive crossing, including its Cartan scalar, and let
(W) be any word in (J) and signed powers of (M). All repeated-root
normals are retained. The exact source identities are
\[
 W^*JW=J,\qquad f=W\mathbf e_0,\qquad
 D_W=W(L-c_0I)W^{-1},\qquad
 \operatorname{adj}(D_W)J=N^2ff^*.
 \tag{1}
\]
These are the identities of the pinned normalized-cofactor source.
The actual closing scalar is (K=f_D), before its recorded external
unit framing factor.

The fixed-band matrix is (D_W); it is generally not Hermitian.
The matrix
\[
                         H_W=JD_W
 \tag{2}
\]
is Hermitian, but the row reversal usually makes it anti-banded.
Write (I=\{0,\ldots,D-1\}) and
\[
                         C_W=H_W[I,I].
 \tag{3}
\]
This is the Hermitian principal minor associated with the original
closing row. If (B_W=D_W[\{1,\ldots,D\},I]) is the fixed-band
minor used in the source theorem, then (C_W) is its row reversal.
In particular they have the same singular values. The source identity
gives
\[
                  \det C_W=\det(J)N^2|K|^2.
 \tag{4}
\]
The known sign in (4) does not determine the signs of individual
eigenvalues.

## 2. Exact inertia, independently of the word

For a Hermitian matrix write its inertia as the triple of positive,
negative and zero eigenvalue counts. Put
\[
             p=\lfloor D/2\rfloor,\qquad q=\lceil D/2\rceil.
\]

**Theorem 1.** At every level and for every signed word,
\[
                         \operatorname{In}(H_W)=(p,q,1).
 \tag{5}
\]

**Proof.** From (1),
\[
 H_W=(W^{-1})^*H_0W^{-1},\qquad H_0=J(L-c_0I).
 \tag{6}
\]
It suffices to compute the inertia of this original untransported
matrix. Its row and column indexed by zero vanish. On the remaining
indices (1\le j,k\le D), its entries are
\[
 (H_0)_{jk}=b_j\mathbf1_{j+k=N}
                  +(c_j-c_0)\mathbf1_{j+k=N-1}.
 \tag{7}
\]
The identities (b_{N-j}=b_j) and (c_{D-j}=c_j) make (7)
symmetric. Multiply its second anti-diagonal by a real parameter
(\lambda\in[0,1]). Reversing the columns of the resulting
(D\)-dimensional block makes it upper bidiagonal, with diagonal
(b_1,\ldots,b_D). Its determinant never vanishes, because every
(b_j<0). Thus its inertia is unchanged along this deformation.

At (\lambda=0), the block splits into pairs
\(\left(\begin{smallmatrix}0&b_j\\b_j&0\end{smallmatrix}\right)),
each with one positive and one negative eigenvalue. When (D) is odd
there is one additional middle entry, (b_{N/2}=-4). The inertia of
the block is therefore ((p,q,0)). Restoring the zero row and column,
then applying the nonsingular congruence (6), proves (5). \(\square\)

**Corollary 2.** If (K\ne0), then
\[
                         \operatorname{In}(C_W)=(p,q,0).
 \tag{8}
\]
Without any assumption on (K), the matrix (C_W) has at least
(p-1) positive and (q-1) negative eigenvalues. Consequently it
is indefinite for every (N\ge5), even at a level where the original
scalar vanishes. If (K\ne0), it is already indefinite for every
(N\ge3).

**Proof.** The radical of (H_W) is the line spanned by (f).
When (f_D\ne0), the coordinate hyperplane (x_D=0) is a complement
to that radical. Restricting the form to any such complement preserves
all its nonzero inertia, proving (8). In general a positive subspace
of dimension (p), and a negative subspace of dimension (q), meet
this hyperplane in dimensions at least (p-1) and (q-1), respectively.
This proves the remaining assertions. \(\square\)

The positive rank-one update that encodes the closing determinant is
also explicit. If (K\ne0),
\[
             \operatorname{In}(H_W+\mathbf e_D\mathbf e_D^*)
                                =(p+1,q,0).
 \tag{9}
\]
To verify this, choose a basis ending in a vector spanning the radical.
The update has a nonzero component in that last direction because
(\mathbf e_D^*f\ne0). Taking the Schur complement of its positive
last diagonal entry leaves exactly the old nonsingular block: the
other part of the rank-one update cancels in this Schur complement.
Thus the update adds one positive direction and removes no negative
direction.

## 3. What a Laplacian representation would have to change

Equations (5) and (8) exclude turning these Hermitian matrices into a
positive graph Laplacian or a positive definite Laplacian minor by
invertible congruence, including diagonal changes of metric. Multiplying
an indefinite matrix by minus one does not fix this obstruction.
The small-level qualifications for a possibly zero closing scalar are
exactly those in Corollary 2.

There is a separate obstruction for (D_W) itself. Its zero eigenvalue
has algebraic multiplicity two, because (c_0=c_D) is a double root
of the original Chebyshev relation, and geometric multiplicity one,
because (L-c_0I) has rank (N-1). Thus (D_W) is not similar to
any Hermitian matrix at any level (N\ge2).

Nor can either choice of its overall sign be diagonally similar to a
nonnegative directed graph Laplacian. For such a Laplacian (\mathcal L),
the matrices (e^{-t\mathcal L}), (t\ge0), have nonnegative entries
and row sums one, so are bounded in the row-sum norm. One proof is to
choose (a\) at least the largest diagonal entry and write
\(e^{-t\mathcal L}=e^{-at}\exp(t(aI-\mathcal L))\).
A nontrivial Jordan block at zero would produce polynomial growth of
this exponential, a contradiction. Transposing handles the column-sum
convention. Similarity preserves the nontrivial zero Jordan block of
(D_W).

These conclusions concern congruence or similarity of the specified
matrices. They do not exclude independent left/right operations, a
larger auxiliary determinant, or a distinct combinatorial source
identity whose summands have controlled signs. Such a construction
would require its own exact equality with the original closing scalar.

## 4. The existing symbol bound remains an upper bound

The pinned cofactor note already proves a singular-value distribution
for the fixed-band minor (B_W), by expanding fixed moments as finite
closed walks. It gives an explicit logarithmic-symbol upper bound for
the original scalar. The reverse implication requires uniform
integrability of the logarithms of the small singular values.

That condition is not automatic for these actual source matrices:
the same note treats the literal word (W=JM^2), whose closing scalar
has modulus one while its bulk logarithmic mean is strictly positive.
An exponentially small singular value of its closing minor is proved
there. No new spectral limit or volume identification is asserted here.

## Direct sources

* `notes/research_rational_word_normalized_cofactor.md`, SHA256
  `aaf154606af22a74b11500e9ada7affdfa903bec16b0b715a61dcfd445522c92`:
  exact source matrices, normalization (1), closing minor, full endpoint
  rank and multiplicity, fixed bandwidth, and the symbol/small-value
  statements used only in Section 4.
* `notes/actual_newton_turn_positive_gram.md`, SHA256
  `d8b21fa8db909120035e86e997a0e02cb84f8dce2dcf6fb244bb5c85c17e28a3`:
  original full-Hermite Frobenius pairing, turn reversal, and actual
  crossing adjoint underlying the source congruence.

Only written reasoning, source-text reads and file hashes were used.
No mathematical code, tests, numerical calculation or compilation was
run. Frozen and public files were not changed.
