# Exact Schur systems for a fixed run of original crossings

Research note, 3 November 2026.

Every fixed signed crossing run has a sparse block realization for
its conjugation of the Newton clock coordinate. All Schur pivots are
invertible at every level, including both parities, and their
determinants are explicit units. The construction uses the original
crossing matrix and preserves the full repeated-root source algebra.

The blocks are complex matrices, not positive energies. Their first
nontrivial inverse already has exponential growth. Thus this is an
exact local construction for coherent transport, with its endpoint
forcing retained; it is not a lower bound for a rational-word source.

## 1. Original matrices and the sparse coordinate

Let \(N\ge2\), \(D=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\),
and \(\eta=(-1)^D\). Use the original Newton multiplication
matrix \(Z\), crossing matrix \(M\), and cyclic matrices \(X,E\)
from the
[elementary cap calculation](research_elementary_cap_path_laplacian.md):
\[
 X\mathbf e_j=Q^j\mathbf e_j,\qquad
 E\mathbf e_j=\mathbf e_{j+1\bmod N},\qquad XE=QEX.
 \tag{1}
\]
The original scalar \(\kappa=q^{D^2/2}\) remains in \(M\).
It cancels from conjugation identities, which does not
authorize dropping it when the resulting operators are
attached to an actual source.

The more general closed coordinate substitutions, including
the turn, are proved in
[the primitive quantum-cap note](research_quantum_cap_primitive_source.md).
The present calculation gives explicit continuants and Schur
pivots for a whole crossing run.

Set
\[
                K=-q^{-1}X^{-1}+(I-X^{-1})E.
 \tag{2}
\]
Its wrap entry is zero. It is lower bidiagonal, has diagonal
\(-q^{-1}Q^{-j}\), and has determinant one. In particular
every occurrence of \(K^{-1}\) below is a genuine finite
inverse, not division by a zero scalar coordinate.

The required exact identities are
\[
 \begin{split}
 M X^{-1}M^{-1}&=-qK,\\
 M^{-1}XM&=X+q^{-1}(X-I)E,\\
 XK-QKX&=(q-q^{-1})I,\\
 Z&=qX+q^{-1}I+(X-I)K,\\
 MKM^{-1}&=qX-Z.
 \end{split}
 \tag{3}
\]
Here \(M\) commutes with \(Z\), since it is multiplication
by the original crossing polynomial in \(z\).

For a direct proof of the first identity, the original
all-entry crossing formula is
\[
 M_{ij}=\kappa\,\nu_j(-q)^{i-j}{i\brack j}_Q,\qquad
 \nu_j=(-1)^jq^{j(j+1)},\quad 0\le j\le i<N.
 \tag{4}
\]
Its row ratio gives
\[
 (1-Q^{i-j})M_{ij}
                    =-q(1-Q^i)M_{i-1,j}.
 \tag{5}
\]
At \(i=0\), the wrap term is killed by \(1-Q^i\); the
triangular boundary \(i=j\) also satisfies (5). Written
as a matrix equation, (5) is
\(M-XMX^{-1}=-q(I-X)EM\), which proves the first line
of (3).

The original identity \(\overline M=M^{-1}\), with
entrywise conjugation in the real Newton basis, gives the
second line by conjugation. The third and fourth follow
by expanding (1)--(2). For clarity, the last line can be
derived without inverting \(X-I\). Write the second line as
\[
            M^{-1}XM=X+q^{-1}XK+q^{-2}I.
 \tag{6}
\]
Conjugate (6) by \(M\), insert
\(MXM^{-1}=-q^{-1}K^{-1}\), and multiply on the left
by \(q^2K\). The third line of (3) gives
\[
 MKM^{-1}=(I-X)K-q^{-1}I=qX-Z.
 \tag{7}
\]
No spectral value or first normal has been discarded.

## 2. Even and odd quantum continuants

It follows at once that
\[
                 M^2X^{-1}M^{-2}=qZ-q^2X.
 \tag{8}
\]
Let \(\mathsf U_m=U_m(Z/2)\), where \(U_m\) is the
Chebyshev polynomial of the second kind. Equivalently
\[
 \mathsf U_{-1}=0,\quad \mathsf U_0=I,\quad
              \mathsf U_{m+1}=Z\mathsf U_m-\mathsf U_{m-1}.
 \tag{9}
\]
Use also \(\mathsf U_{-2}=-I\) in the initial formulas.
Define
\[
 \begin{split}
 P_m&=q^m(\mathsf U_m-q\mathsf U_{m-1}X),
       &P_{-1}&=X,\quad P_0=I,\\
 C_m&=q^m(\mathsf U_mK+\mathsf U_{m-1}),
       &C_{-1}&=-q^{-1}I,\quad C_0=K.
 \end{split}
 \tag{10}
\]
The order of \(X\) and \(K\) on the right in (10) matters.
Both sequences satisfy the same left recurrence
\[
            A_{m+1}=qZA_m-q^2A_{m-1}.
 \tag{11}
\]

**Theorem 1.** For every \(m\ge0\) and every level,
\[
 \boxed{\begin{split}
 M^{2m}X^{-1}M^{-2m}&=P_mP_{m-1}^{-1},\\
 M^{2m+1}X^{-1}M^{-2m-1}&=C_mC_{m-1}^{-1}.
 \end{split}}
 \tag{12}
\]
All denominators are invertible. More precisely,
\[
 \begin{split}
 (P_m)_{jj}&=Q^{-mj},&
       \det P_m&=\eta^m,\\
 (C_m)_{jj}&=-q^{-1}Q^{-(m+1)j},&
       \det C_m&=\eta^m.
 \end{split}
 \tag{13}
\]
Their lower bandwidths are at most \(m\) and \(m+1\),
respectively, with the usual truncation at \(N-1\).

*Proof.* Put \(Y_m=M^{2m}X^{-1}M^{-2m}\). Conjugating
(8) by \(M^{2m}\), and using \(MZ=ZM\), gives
\[
              Y_{m+1}=qZ-q^2Y_m^{-1},\qquad Y_0=X^{-1}.
 \tag{14}
\]
Substituting \(Y_m=P_mP_{m-1}^{-1}\) into (14) gives
exactly (11), in the displayed noncommutative order.

For the odd sequence the same recurrence starts at
\(-qK=C_0C_{-1}^{-1}\), by (3). This proves (12)
once invertibility is checked.

Every matrix in (10) is lower triangular. At coordinate
\(j\), put \(r=qQ^j\), so \(Z_{jj}=r+r^{-1}\).
The polynomial identity
\[
       U_m((r+r^{-1})/2)-rU_{m-1}((r+r^{-1})/2)=r^{-m}
 \tag{15}
\]
also holds at \(r=\pm1\), by continuity or the recurrence.
For \(P_m\), it gives the first diagonal in (13).
For \(C_m\), use \(K_{jj}=-r^{-1}\), giving the second.
They are all nonzero. Taking their products and using
\(Q^{N(N-1)/2}=\eta\) gives both determinants in (13).
The degree bounds in (9) prove the bandwidth assertion.
\(\square\)

Negative powers are obtained without a new branch choice:
\[
 \begin{split}
 M^{-2m}X^{-1}M^{2m}
       &=\overline{P_{m-1}}\,\overline{P_m}^{-1},\\
 M^{-(2m+1)}X^{-1}M^{2m+1}
       &=\overline{C_{m-1}}\,\overline{C_m}^{-1}.
 \end{split}
 \tag{16}
\]
Indeed conjugate (12), using
\(\overline M=M^{-1}\), \(\overline X=X^{-1}\),
and then invert. Entrywise conjugation does not reverse
matrix order; inversion does.

## 3. A sparse Schur realization, including its final response

For \(m\ge1\), form an \(m\times m\) block tridiagonal
matrix \(\mathcal A_m\), each block of size \(N\).
Its first diagonal block is \(qZ-q^2X\); every later
diagonal block is \(qZ\); both off-diagonal blocks are
\(-qI\). Successive leading Schur pivots are
\[
      P_1P_0^{-1},\ P_2P_1^{-1},\ldots,P_mP_{m-1}^{-1}.
 \tag{17}
\]
Thus the last pivot is the original even response in
(12), and
\[
                         \det\mathcal A_m=\eta^m.
 \tag{18}
\]
All eliminations are valid at every level by (13).

For the odd response with exponent \(2m+1\), use \(m+1\)
blocks, first diagonal \(-qK\), later diagonals \(qZ\),
and the same off-diagonals. Its successive pivots are
\(C_jC_{j-1}^{-1}\), for \(j=0,\ldots,m\), so
\[
                         \det\mathcal A^{\mathrm{odd}}_m
                                      =\eta^{m+1}.
 \tag{19}
\]
The \(m=0\) odd case is its single block \(-qK\).

The inverse of the last pivot is also an exact block
response: it is the last diagonal block of the inverse
of the whole tridiagonal system. Conjugation and (16)
therefore give a sparse realization for negative powers
as well. If an ordinary Schur complement is preferred
for an inverse response, border the last block with
off-diagonals \(I,I\) and final diagonal zero; its
complement is minus that inverse response.

These are finite systems for the literal original
operators. Their block entries have bounds independent
of the level: for example \(\|Z\|\le6\),
\(\|X\|=1\), and \(\|K\|\le3\).
They can be attached to the original free-boundary
evaluation vectors before contraction. Exact matrix
equality then preserves values and all mixed normal
derivatives of those boundary polynomials.

The block systems are generally not Hermitian. Unit
determinants in (18)--(19) do not imply small inverse
norms, and the next section gives an actual failure of
that implication in the first Schur step.

## 4. The retained endpoint forcing can grow exponentially

Write
\[
      S_j=\prod_{r=1}^{j}2\sin(r\pi/N),\qquad S_0=1.
 \tag{20}
\]
The first even denominator \(P_1=qZ-q^2X\) is lower
bidiagonal, with diagonal \(Q^{-j}\) and subdiagonal
\(-q\,4\sin^2(j\pi/N)\). Its forced inverse is exactly
\[
 \boxed{\qquad
       (P_1^{-1}\mathbf e_0)_j=q^{j(j+2)}S_j^2,
                    \quad 0\le j<N.
 \qquad}
 \tag{21}
\]
The first row fixes the zeroth entry to one. Each later
row multiplies the preceding entry by
\(qQ^j\,4\sin^2(j\pi/N)\), which proves (21).
In particular the last entry has modulus \(N^2\),
whereas intermediate entries can be exponentially larger.

Let
\[
             c_*=-\int_0^{1/6}\log(2\sin\pi x)\,dx>0.
 \tag{22}
\]
For \(j_N=\lfloor5N/6\rfloor<N\), the elementary
logarithmic Riemann-sum estimate gives
\[
                  \log S_{j_N}=Nc_*+O(\log N).
 \tag{23}
\]
One can verify the sign and interval directly from
\(S_jS_{D-j}=N\): the complementary index is
\(N/6+O(1)\), where the integral of the logarithm is
\(-c_*\). The logarithmic endpoint at zero costs only
\(O(\log N)\).

Consequently, at both parities,
\[
 \|P_1^{-1}\|\ge \exp(2Nc_*+O(\log N)),\qquad
 s_{\min}(P_1)\le\exp(-2Nc_*+O(\log N)).
 \tag{24}
\]
This is a response of the original negative crossing,
since (16) gives
\[
                  M^{-2}X^{-1}M^2=\overline{P_1}^{-1}.
 \tag{25}
\]
No replacement of the original full source by an
absolute-value state sum was used.

Moreover \(P_1\) is the first pivot of every longer even
system in Section 3, including the systems used for
four negative crossings. Thus estimating each pivot
inverse by a polynomial or a subexponential constant
cannot prove controlled composition. A proof must
retain the specific forcing and cancellation between
the responses; the harmless final modulus \(N^2\) in
(21) already shows why a whole inverse norm is too
coarse for that purpose.

## 5. Reflection positivity of the complete endpoint block

The block system has more structure than its separate pivots.
Divide the even system \(\mathcal A_m\) by \(q\), then order
its coordinates by Newton color first and block position
second. Let \(T_m\) be the adjacency matrix of the path on
\(m\) vertices, and let \(E_{11}\) be its first-coordinate
projection. The diagonal color blocks are
\[
 \mathcal C_j=\mathcal C_m(r_j)
   =(r_j+r_j^{-1})I_m-T_m-r_jE_{11},
       \qquad r_j=qQ^j,
 \tag{26}
\]
and the subdiagonal color blocks are
\(-p_{j-1}I_m\), with \(p_{j-1}=4\sin^2(j\pi/N)\).
Thus the exact color equations are
\[
              \mathcal C_j u_j-p_{j-1}u_{j-1}=f_j.
 \tag{27}
\]
The \(j=0\) equation has no preceding color.

Every \(\mathcal C_m(r)\) is invertible for \(r\ne0\).
Its determinant is \(r^{-m}\), as follows by its scalar
tridiagonal recurrence. If \(\mathcal G_j=\mathcal C_j^{-1}\),
the full endpoint block of the inverse is consequently
\[
 \left((q^{-1}\mathcal A_m)^{-1}\right)_{D,0}
        =N^2\mathcal R_{m,N},\qquad
            \mathcal R_{m,N}=\mathcal G_D\cdots\mathcal G_0.
 \tag{28}
\]
The subscript \(D,0\) in (28) selects color blocks, each of
size \(m\). The product of the intervening \(p_j\) is
exactly \(N^2\); no endpoint factor is suppressed.

**Theorem 2.** The matrix \((-1)^N\mathcal R_{m,N}\)
is Hermitian positive definite at every level. In particular,
for every \(m\ge1\),
\[
 \boxed{\quad
 (-1)^N\,\frac{q}{N^2}
       (P_{m-1}P_m^{-1})_{D,0}
       =(-1)^N(\mathcal R_{m,N})_{m,m}>0.
 \quad}
 \tag{29}
\]
This is a nonvanishing statement for the actual original
coordinate response
\(P_{m-1}P_m^{-1}=M^{2m}XM^{-2m}\).

*Proof.* Since \(r_{D-j}=\overline{r_j}\), and
\(\mathcal C_m(r)\) is complex symmetric,
\[
                  \mathcal G_{D-j}=\mathcal G_j^\dagger.
 \tag{30}
\]
If \(N=2h\), put
\(\mathcal V=\mathcal G_{h-1}\cdots\mathcal G_0\).
The full product in (28) is exactly
\(\mathcal V^\dagger\mathcal V\).
If \(N=2h+1\), the same product is
\(\mathcal V^\dagger\mathcal G_h\mathcal V\), where
\(r_h=-1\). The matrix
\[
          \mathcal C_m(-1)=-2I_m-T_m+E_{11}
 \tag{31}
\]
is real negative definite. Indeed minus (31) is diagonally
unitarily similar to \(2I_m-T_m-E_{11}\), which equals
\((I-L_m)(I-U_m)\), where \(U_m=L_m^T\) are the
nilpotent upper and lower path shifts. This is positive
definite because \(I-L_m\) is invertible and
\((I-U_m)=(I-L_m)^\dagger\).
Thus \(\mathcal G_h\) is negative definite. This proves
the first assertion at both parities.

The last stage block of \(\mathcal A_m^{-1}\) is the
inverse of its final Schur pivot,
\(P_{m-1}P_m^{-1}\). Its \((D,0)\) color entry is,
by (28), \(q^{-1}N^2(\mathcal R_{m,N})_{m,m}\).
This proves (29), with the stated scalar. \(\square\)

This complete endpoint estimate does not follow by
estimating the individual Schur inverses. For example,
the explicit scalar inverse formula, for \(1\le a\le b\le m\),
is
\[
 (\mathcal C_m(r)^{-1})_{ab}
       =r^{m-a+1}U_{m-b}((r+r^{-1})/2).
 \tag{32}
\]
It is symmetric in the indices. For \(|r|=1\) it gives
\(\|\mathcal C_m(r)^{-1}\|\le m^2\), while
\(\|\mathcal C_m(r)\|\le5\).
Together with (30)--(31) these supply the coarse but
uniform bounds
\[
        5^{-N}I_m\ \le\ (-1)^N\mathcal R_{m,N}\
                                      \le\ m^{2N}I_m .
 \tag{33}
\]
The middle odd block has inverse eigenvalues of absolute
value at least \(1/4\), which is sufficient for the
left bound. These bounds do not identify a geometric
exponential rate.

The channel selection is essential. The opposite stage
corner of the block inverse is
\[
          (\mathcal A_m^{-1})_{1,m}=q^{m-1}P_m^{-1}.
 \tag{34}
\]
This follows by multiplying the successive inverse Schur
pivots in their actual order, which telescopes.
Consequently
\[
                (P_m^{-1})_{D,0}
                        =q^{-m}N^2(\mathcal R_{m,N})_{1,m}.
 \tag{35}
\]
For \(m>1\), this is an off-diagonal entry of a positive
matrix after the sign correction, and positivity alone
gives it no nonzero lower bound. In particular (29) is
not a statement about every forced channel of the run,
or about the primitive closing cofactor of a composed
rational word.

The [cyclotomic monodromy theorem](research_cyclotomic_endpoint_monodromy.md)
now determines the spectrum of the complete product in (28),
without estimating its separate factors. Its proof uses an exact
quantum-oscillator determinant and applies first at arbitrary
complex \(r\), then at the original \(r=q\). Combined with
Theorem 2, it gives the sharper statement below.

**Corollary 3.** Put
\[
 a_m=\frac1{4\cos^2(\pi/(2m+1))},\qquad
 b_m=\frac1{4\sin^2(\pi/(4m+2))}.
 \tag{36}
\]
At every level,
\[
 \begin{split}
 a_m I_m&\le(-1)^N\mathcal R_{m,N}\le b_m I_m,\\
 a_m&\le(-1)^N\frac q{N^2}
                 (M^{2m}XM^{-2m})_{D,0}\le b_m,\\
 |(P_m^{-1})_{D,0}|&\le N^2b_m.
 \end{split}
 \tag{37}
\]
The first two inequalities give genuine nonzero lower bounds.
The last is an upper bound only: it is the off-diagonal
channel (35). Complex conjugation supplies the corresponding
bounds for the negative even-run coordinate
\(M^{-2m}X^{-1}M^{2m}\).

Thus the complete endpoint response has a condition number
bounded in terms of the fixed run length \(m\), independently
of \(N\), even though (24) proves exponential growth inside
the same Schur construction. The actual primitive closing
cofactor of a general word is a specified polarized pairing;
it is not automatically the positive diagonal in (37).

## 6. Scope and reproduction

The construction replaces a dense conjugated clock
coordinate by an exact finite local system with known
nonzero pivots and determinants. Its full even-run
endpoint block has the genuine reflection positivity in
(29) and uniform bounds (37). It gives no asymptotic
for the original rational-word closing scalar and no
claim that the Schur response is positive. The
[normalized cofactor](research_rational_word_normalized_cofactor.md)
still fixes the actual boundary selection, and the
[elementary positive cap energy](research_elementary_cap_path_laplacian.md)
does not by itself control its transport through these
complex block systems.

The [original-matrix verifier](../experiments/check_crossing_run_quantum_continuants.py)
checks the signed identities (12), (16), their triangular
diagonals and determinants, the block Schur response,
the complete forced column (21), the endpoint spectrum,
and the arbitrary-parameter characteristic identity
underlying (37), at both parities.
The [saved result](../repro/results/research-crossing-run-quantum-continuants.json)
records hashes and precision. These finite checks
diagnose phases and endpoint normalization; the
all-level statements are proved above.
