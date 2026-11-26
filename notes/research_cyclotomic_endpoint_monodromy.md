# The exact spectrum of a crossing-run endpoint block

Research note, 3 November 2026.

The complete endpoint block of a fixed crossing run has a spectrum
independent of the quantum level, after its recorded sign is removed.
This follows from an exact characteristic-polynomial identity at an
arbitrary complex parameter. Together with the original reflection
identity, it gives uniform upper and lower bounds for the entire
endpoint response. It does not replace an off-diagonal source pairing
by a positive diagonal one.

## 1. The cyclic product

Let \(m\ge1\), let \(L_m\) be the lower shift on \(m\) coordinates,
and put \(U_m=L_m^T\). In this note \(\mathsf U_k\) denotes a
Chebyshev polynomial, so that it is distinct from the matrix \(U_m\).
Define
\[
 \begin{split}
 C_m(r)&=(r+r^{-1})I_m-(L_m+U_m)-rE_{11}\\
       &=r^{-1}(I_m-rL_m)(I_m-rU_m),\\
 G_m(r)&=C_m(r)^{-1}
       =r(I_m-rU_m)^{-1}(I_m-rL_m)^{-1}.
 \end{split}                                                   \tag{1}
\]
Here \(r\ne0\). The shifts are nilpotent, so these inverses are
finite polynomial series, and \(\det C_m(r)=r^{-m}\).

Fix \(N\ge2\), a primitive \(N\)-th root \(Q\), and
\(\eta=(-1)^{N-1}\). Keep the indicated order in
\[
 \mathcal R_{m,N}(r)
       =G_m(rQ^{N-1})\cdots G_m(rQ)G_m(r).
 \tag{2}
\]

**Theorem 1.** For every \(r\ne0\),
\[
 \boxed{\quad
 \det(I_m-\lambda\mathcal R_{m,N}(r))
       =\det(I_m-\lambda G_m(\eta r^N))
       \qquad(\lambda\in\mathbb C).
 \quad}                                                        \tag{3}
\]
The statement is equality of characteristic polynomials. It does
not assert equality of the two matrices or choose a similarity
matrix with a controlled norm at arbitrary complex \(r\).

## 2. A quantum oscillator determinant

The following finite algebra calculation supplies the determinant
in (3). Work first over the rational function field in two
independent variables \(r,t\). On \(N\) coordinates let
\[
 B\mathbf e_j=rQ^j\mathbf e_j,\qquad
 E\mathbf e_j=\mathbf e_{j+1\bmod N},\qquad
 A=B^{-1}-tE.
 \tag{4}
\]
The letter \(B\) here denotes this auxiliary diagonal matrix,
not the primitive upper bidiagonal coordinate in the source note.
These matrices satisfy
\[
 BA-QAB=(1-Q)I,\qquad
 B^N=bI,\qquad A^N=aI,\qquad
 b=r^N,\quad a=b^{-1}+(-t)^N.
 \tag{5}
\]
For the last equality, \(E B^{-1}=QB^{-1}E\). The root-of-unity
binomial formula applies: every intermediate Gaussian binomial
coefficient vanishes because \(Q\) is primitive, while its
denominators of orders \(1,\ldots,N-1\) are nonzero.

We will use the rational transformation
\[
             (A,B)\longmapsto(A+B-A^{-1},A^{-1}).        \tag{6}
\]
It preserves the first relation in (5) and the sum \(A+B\).
For example, multiplying the original relation on both sides by
\(A^{-1}\) gives
\(A^{-1}B-QBA^{-1}=(1-Q)A^{-2}\), which verifies the new
relation directly.

Its effect on the central powers is particularly simple:
\[
                       (a,b)\longmapsto(a+b-a^{-1},a^{-1}).
 \tag{7}
\]
To prove (7), put \(C=AB-I\). Then
\[
 CA=QAC,\qquad
 A^NB^N=\prod_{j=0}^{N-1}(I+Q^jC)=I+\eta C^N.
 \tag{8}
\]
The product identity follows either by induction using \(CA=QAC\)
or by multiplying the factors \(1+Q^jz\). The new first matrix
in (6) is \(A+A^{-1}C\), and
\((A^{-1}C)A=QA(A^{-1}C)\). Consequently
\[
 \begin{split}
 (A+A^{-1}C)^N
   &=A^N+(A^{-1}C)^N\\
   &=aI+\eta a^{-1}C^N
     =(a+b-a^{-1})I.
 \end{split}                                                   \tag{9}
\]
Here \(Q^{-N(N-1)/2}=\eta\), and (8) gives
\(\eta C^N=(ab-1)I\). This proves (7), including its sign at
both parities.

Put \(Z=A+B\), and define ordered matrix continuants by
\[
 F_{-1}=B,\qquad F_0=I,\qquad
 F_{k+1}=ZF_k-F_{k-1}.
 \tag{10}
\]
Thus \(F_1=A\), and
\[
 F_k=\mathsf U_k(Z/2)-\mathsf U_{k-1}(Z/2)B,
 \tag{11}
\]
where \(\mathsf U_{-1}=0,\mathsf U_0=1\), and
\(\mathsf U_{k+1}(z/2)=z\mathsf U_k(z/2)-\mathsf U_{k-1}(z/2)\).
The order of the last factor \(B\) is retained.

**Lemma 2.** These continuants have determinant
\[
 \boxed{\quad
 \det F_m=\eta^m
  \left[\mathsf U_m((a+b)/2)
                  -b\mathsf U_{m-1}((a+b)/2)\right].
 \quad}                                                        \tag{12}
\]

*Proof.* On the rational open set where the required inverses exist,
set \(Y_0=B^{-1}\). The pivots
\(Y_k=F_kF_{k-1}^{-1}\), \(k\ge1\), satisfy
\(Y_{k+1}=Z-Y_k^{-1}\), starting at \(Y_1=A\).
The pair \((Y_k,Y_{k-1}^{-1})\) is therefore obtained by the
repeated transformation (6). Its central powers obey the ordinary
scalar recurrence with invariant sum \(a+b\).

More explicitly, put
\[
 p_{-1}=b,\qquad p_0=1,\qquad
 p_{k+1}=(a+b)p_k-p_{k-1}.
 \tag{13}
\]
Equations (7) and (10) give
\(Y_k^N=(p_k/p_{k-1})I\). Hence
\((\det Y_k)/(p_k/p_{k-1})\) is an \(N\)-th root of unity
in the rational function field. It is a constant. At \(t=0\),
one has \(A=B^{-1}\) and every pivot is \(B^{-1}\).
Since \(\det B=\eta b\), this constant is \(\eta\).
Multiplying the pivot determinants gives \(\det F_m=\eta^mp_m\),
which is (12).

The rational open set is nonempty: at \(t=0\) every displayed
pivot and continuant is invertible for every \(r\ne0\).
After clearing denominators, both sides of (12) are Laurent
polynomials in \(r\) and polynomials in \(t\). Thus their identity
extends to every \(r\ne0\) and every \(t\), including values
where an intermediate pivot used in the proof is singular.
No invertibility at such an intermediate specialization is assumed.
\(\square\)

## 3. The cyclic block determinant

Consider \(N\) vectors \(u_j\in\mathbb C^m\) with cyclic index,
and the block matrix of the equations
\[
              C_m(rQ^j)u_j-tu_{j-1}=f_j.
 \tag{14}
\]
Factoring its diagonal blocks and eliminating successively around
the cycle gives
\[
 \det\mathcal D(t)
   =(\eta r^N)^{-m}
                  \det(I_m-t^N\mathcal R_{m,N}(r)).
 \tag{15}
\]
This can also be checked by the Schur complement after removing
one color block. The resulting cyclic product is a cyclic rotation
of (2); its determinant is unchanged, since all the \(G_m(rQ^j)\)
are invertible. The factor outside the determinant is exactly
\(\prod_j\det C_m(rQ^j)=(\eta r^N)^{-m}\).

Now reorder the coordinates by channel rather than color, using
the same permutation for rows and columns. The channel matrix is
block tridiagonal. Its first diagonal block is \(Z-B=A\),
its later diagonal blocks are \(Z\), and its off-diagonal blocks
are \(-I_N\), with precisely the \(A,B\) in (4). Its determinant
is \(\det F_m\), by (10) and successive Schur complements on
the same nonempty rational open set. Polynomial continuation
again removes that intermediate restriction.

Set \(R=\eta r^N=\eta b\). Since
\[
                R+R^{-1}-t^N=\eta(a+b),
 \tag{16}
\]
the parity identity \(\mathsf U_k(-x)=(-1)^k\mathsf U_k(x)\)
and (12) give
\[
 \begin{split}
 \det\mathcal D(t)
 &=\det(C_m(R)-t^NI_m)\\
 &=R^{-m}\det(I_m-t^NG_m(R)).
 \end{split}                                                   \tag{17}
\]
Comparing (15) and (17) proves (3) for \(\lambda=t^N\).
Every complex \(\lambda\) has such a root \(t\), so this proves
Theorem 1.

## 4. The original endpoint has uniform singular values

Return to the original quantum level \(q=e^{\pi i/N}\),
\(Q=q^2\), and put \(r=q\). The
[crossing-run source calculation](research_crossing_run_quantum_continuants.md),
Section 5, proves the full original endpoint identity
\[
 \left((q^{-1}\mathcal A_m)^{-1}\right)_{D,0}
                    =N^2\mathcal R_{m,N}(q),
 \tag{18}
\]
with color blocks of size \(m\). It also proves that
\(H_{m,N}=(-1)^N\mathcal R_{m,N}(q)\) is Hermitian positive
definite, by pairing the original colors \(j\) and \(D-j\).
For odd \(N\), the unpaired color has \(r=-1\) and gives the
required negative definite middle factor. These are finite source
identities, including the endpoint factor \(N^2\).

Here \(\eta q^N=(-1)^N\). The matrices \(C_m(-1)\) and
\(-C_m(1)\) are conjugate by the diagonal sign matrix with
alternating entries. Theorem 1 and the reflection positivity
therefore give the following exact spectrum.

**Corollary 3.** For every \(m\ge1\) and \(N\ge2\), the eigenvalues
of \(H_{m,N}\), including multiplicities, are
\[
 \boxed{\quad
 \frac1{4\sin^2((2k-1)\pi/(4m+2))},
                    \qquad k=1,\ldots,m.
 \quad}                                                        \tag{19}
\]
In particular, with
\[
 a_m=\frac1{4\cos^2(\pi/(2m+1))},\qquad
 b_m=\frac1{4\sin^2(\pi/(4m+2))},
 \tag{20}
\]
one has the uniform operator bounds
\[
                     a_m I_m\le H_{m,N}\le b_m I_m.
 \tag{21}
\]
The complete endpoint block in (18) has smallest and largest
singular values exactly \(N^2a_m\) and \(N^2b_m\).

*Proof.* The eigenvalues of
\(C_m(1)=(I-L_m)(I-U_m)\) are
\(4\sin^2((2k-1)\pi/(4m+2))\). One direct verification
uses the vector with entries \(\cos((j+1/2)\theta)\),
\(j=0,\ldots,m-1\), the boundary conditions
\(v_{-1}=v_0\), \(v_m=0\), and
\(\theta=(2k-1)\pi/(2m+1)\).
Take reciprocals, apply Theorem 1 and the alternating sign
conjugation, and use the already proved Hermitian positivity.
This proves (19)--(21). \(\square\)

This is a uniform noncancellation statement for the full endpoint
map of one original run. For example the original diagonal channel
in equation (29) of the crossing-run note now obeys
\[
 a_m\le
 (-1)^N\frac{q}{N^2}
          (M^{2m}XM^{-2m})_{D,0}
 \le b_m.
 \tag{22}
\]
An arbitrary nonzero vector sent through the whole endpoint map
has output norm at least \(N^2a_m\) times its input norm.
However a prescribed off-diagonal entry or a pairing with an
independent output covector can vanish. In particular the other
run channel \((P_m^{-1})_{D,0}\) is proportional to
\((\mathcal R_{m,N})_{1,m}\), not to a diagonal entry. The
primitive closing minor of a composed word is a further specified
polarized boundary pairing. Neither is replaced by (22).

Thus the entire run's endpoint response is uniformly controlled,
even though individual Schur inverses and intermediate colors can
grow exponentially. A proof for a general short rational word
must still identify and control how its original turns and caps
join these complete endpoint blocks.

The [crossing-run verifier](../experiments/check_crossing_run_quantum_continuants.py)
also checks (3) at an arbitrary complex \(r\), and (19) in the
original level specialization. Its
[saved result](../repro/results/research-crossing-run-quantum-continuants.json)
is supplementary to the all-level algebraic proof above.
