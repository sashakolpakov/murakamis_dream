# Exact original coordinates for the separated wrapped operators

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The main and wrapped outer coefficients have one common change of
basis to the original crossing operators. A second exact factorization
places the wrapped insertion between the polynomial coefficient matrix
and its Hermitian adjoint. It has rank \(N-1\), despite the nilpotence
of its middle Toeplitz factor. These are full finite-source identities;
they do not supply the missing global mixed-word rate estimate.

## 1. The separated coefficient matrices

Fix \(N\ge2\), \(D=N-1\), \(q=e^{\pi i/N}\), \(r=q^{-2}\), and
\[
 P_a=(r;r)_a,\quad S_a=|P_a|,\quad
 \tau_a=(-1)^a r^{a(a+1)/2},\quad
 p_a(X)=(rX;r)_a,\quad d_N(X)=\sum_{h=0}^{D}d_hX^h.
 \tag{1}
\]
The original weight satisfies \(d_N(r^j)=1/P_j\), and
\(d_D=1/N^2\). Let \(D_P,D_S,\Delta\) denote the diagonal
matrices with entries \(P_a,S_a,\tau_a\). Define
\[
 \begin{split}
 K_0(a,b)&=\frac{[X^b]p_a(X)p_b(X)}{P_a^2},\\
 K_1(a,b)&=\frac{[X^b]p_a(X)p_b(X)d_N(X)}{P_a^3},\\
 W_1(a,b)&=\frac{[X^{N+b}]p_a(X)p_b(X)d_N(X)}{P_a^3}.
 \end{split}
 \tag{2}
\]
These are the separated coefficient matrices for the exact outer
torus. In particular a cyclic word expands into traces of products
of \(K_0\) and \(K_1+W_1\), with scalar
\(\kappa^{m+k}N^{m+k}\). All coefficients in (2) are literal
finite polynomial coefficients, not asymptotic symbols.

## 2. One common original basis

Let \(\mathsf S\) be the basis matrix of the
[exact wire contraction](research_mixed_wire_exact_contraction.md),
so \(\Gamma B_n=\mathsf S A_n\mathsf S^{-1}\) and \(A_n=JM^n\).
Put
\[
                         V=\mathsf S^T D_P^2.
 \tag{3}
\]

**Proposition 1.** At every level,
\[
 K_0=\frac{V^{-1}A_3V}{\kappa N},\qquad
 K_1+W_1=\frac{V^{-1}A_4V}{\kappa^2N^2}.
 \tag{4}
\]
Consequently the wrapped term is the original operator
\[
                  A_4^{\mathrm{wrap}}=\kappa^2N^2VW_1V^{-1}.
 \tag{5}
\]
The same \(V\) applies to every position of every mixed word.

*Proof.* Write \(T_\epsilon^{\mathrm{phys}}\) for the physical
conditional matrix in
[the conditional-leg identity](research_mixed_conditional_leg_sum.md):
\[
 T_\epsilon^{\mathrm{phys}}(a,b)
   =\frac{L_\epsilon(a,b)}{P_a^2P_b^\epsilon},\qquad
 T_\epsilon^{\mathrm{phys}}
   =\frac{\Gamma B_{3+\epsilon}}{\kappa^{1+\epsilon}N^\epsilon}.
\]
Root-of-unity averaging gives
\([X^b]p_ap_b=L_0(b,a)/N\), and the sum of the main and
wrapped coefficients gives \(L_1(b,a)/N\).
Thus the matrix in (2), with both terms included for type four,
is \(D_P^{-2}(T_\epsilon^{\mathrm{phys}})^TD_P^2/N\).
The original relation \(M^T=JMJ\) gives \(A_n^T=A_n\).
Substitution proves (4), including its transpose, scalar, and
common basis. \(\square\)

The identities also retain arbitrary original boundary vectors.
For example the corresponding observed word is obtained by replacing
its left vector \(x\) by \(V^Tx\), and its right vector \(y\) by
\(V^{-1}y\), with the scalar from (4). This applies to whole
ordinary boundary polynomials and to every fixed ordinary derivative.
It supplies no bound for these generally different transformed vectors.

## 3. A polynomial Gram factorization

Let \(T_{ab}=[X^b]p_a(X)\), a lower triangular invertible matrix.
For \(0\le a,b<N\), define
\[
 (D_{\mathrm{main}})_{ab}=
 \begin{cases}d_{b-a},&b\ge a,\\0,&b<a,\end{cases}
 \qquad
 (D_{\mathrm{wrap}})_{ab}=
 \begin{cases}d_{N+b-a},&a>b,\\0,&a\le b.\end{cases}
 \tag{6}
\]
Then the exact coefficient factorizations are
\[
 \begin{split}
 K_0&=D_P^{-2}TT^*\Delta,\\
 K_1&=D_P^{-3}TD_{\mathrm{main}}T^*\Delta,\\
 W_1&=D_P^{-3}TD_{\mathrm{wrap}}T^*\Delta.
 \end{split}
 \tag{7}
\]
Indeed, on the unit circle,
\(X^{-b}p_b(X)=\tau_b\overline{p_b(X)}\).
Taking the constant Fourier coefficient proves (7); the wrapped
term has the additional factor \(X^{-N}\).

Set \(B=D_S\Delta\) and \(L=D_S^{-1}T\). Since
\(P_a^2=\tau_aS_a^2\), (7) is equivalently
\[
 \begin{split}
 BK_0B^{-1}&=LL^*,\\
 BK_1B^{-1}&=D_P^{-1}LD_{\mathrm{main}}L^*,\\
 BW_1B^{-1}&=D_P^{-1}LD_{\mathrm{wrap}}L^*.
 \end{split}
 \tag{8}
\]
Only the first of these matrices is asserted to be positive.
The two type-four insertions retain the complex diagonal \(D_P^{-1}\)
and the full main or wrapped middle factor.

The strict lower triangular matrix \(D_{\mathrm{wrap}}\) has first
subdiagonal \(1/N^2\). Its lower-left square minor of size \(N-1\)
therefore has determinant \(N^{-2(N-1)}\). It follows that
\[
 \operatorname{rank}W_1
 =\operatorname{rank}A_4^{\mathrm{wrap}}=N-1,\qquad
 D_{\mathrm{wrap}}^N=0,\quad D_{\mathrm{wrap}}^{N-1}\ne0.
 \tag{9}
\]
Nilpotence does not pass through the two different outer factors
in (8). Already at \(N=2\),
\(W_1=\begin{pmatrix}0&0\\1/32&1/32\end{pmatrix}\)
has nonzero trace.

## 4. An exact original annihilator and a norm target

The first row of \(W_1\) is zero, since \(p_0p_bd_N\) has
degree at most \(N+b-1\). Put \(u_j=(-q^{-1})^j\).
The original inverse crossing and basis matrix give
\[
 e_0^TV^{-1}=u^T,\qquad
 u^TA_4^{\mathrm{wrap}}=0,\qquad
 e_D^T M A_4^{\mathrm{wrap}}M^{-1}=0.
 \tag{10}
\]
For the last equality use \(u=\kappa M^{-1}e_0\) and
the original braid identity, which imply
\(u^TM^{-1}=\kappa e_D^T\).
This is a specific original null direction. Rank (9) shows that
the wrapped insertion is not the small highest-row block from
the endpoint deletion theorem.

There are exact norm data for the middle factor:
\[
 \|D_{\mathrm{wrap}}\|_F^2
       =\sum_{h=1}^{N-1}h|d_h|^2
       \le\sum_{a=0}^{N-1}S_a^{-2}.
 \tag{11}
\]
The inequality is Parseval for the original interpolation values:
\(\sum_h|d_h|^2=N^{-1}\sum_aS_a^{-2}\).
Moreover, by (4), (8), and the original positive similarity
\(MA_3M^{-1}=\kappa M^*M\),
\(\|L\|_2^2=\|M\|_2^2/N\).
Thus one valid bound in the explicitly specified Gram coordinates is
\[
 \|BW_1B^{-1}\|_2
 \le\left(\max_a S_a^{-1}\right)\frac{\|M\|_2^2}{N}
                 \left(\sum_aS_a^{-2}\right)^{1/2}.
 \tag{12}
\]
This estimate does not exhibit an exponential alias gap. A sharper
bound must retain the interaction of \(L\), the wrapped Toeplitz
matrix, and \(L^*\), or the actual vectors surrounding the insertion.
Neither the middle factor's nilpotence nor the positive type-three
Gram matrix is a substitute for that estimate.

## 5. A Fourier divided difference in the original positive coordinates

Write \(\delta_a=P_a/S_a\), and define two unitary matrices
\[
 \mathcal F_{ab}=N^{-1/2}q^{-Da}Q^{ab},\qquad
 \mathcal U=J\operatorname{diag}((-q)^{-a}\delta_a^{-1}),
 \qquad Q=q^2.
 \tag{13}
\]
The polynomial coefficient matrix has the exact Fourier relation
\[
                 \sqrt N\,\mathcal U L=\kappa M\mathcal F.
 \tag{14}
\]
To check it directly, the finite q-binomial theorem gives
\[
 (M\mathcal F)_{ab}
    =\frac{\kappa(-1)^a q^a}{\sqrt N}(Q^{b+1};Q)_a.
\]
This vanishes when \(a+b\ge N\). Otherwise use
\((Q^{b+1};Q)_a=\overline{P_{a+b}}/\overline{P_b}\),
\(S_{D-a-b}=N/S_{a+b}\), and
\((-q)^{-(D-a)}\delta_{D-a}^{-1}
 =\kappa^2(-1)^a q^a\delta_a^{-1}\).
These give (14) with the same phases on every entry.

Set \(\mathcal R=\mathcal F D_{\mathrm{wrap}}\mathcal F^*\).
It is a unitary transform of the exact strict triangular matrix,
and admits the original-node expression
\[
 \mathcal R_{ab}=
 \begin{cases}
 \displaystyle
 \frac{q^{-D(a-b)}}{N(1-Q^{a-b})}
       \left(\frac1{P_a}-\frac1{P_b}\right),&a\ne b,\\[2mm]
 \displaystyle\frac{r^a d_N'(r^a)}N,&a=b .
 \end{cases}
 \tag{15}
\]
Indeed, put \(j-k=\ell>0\) in the Fourier transform of (6).
For \(a\ne b\), the sum over \(k=0,\ldots,N-1-\ell\)
is a finite geometric progression. The remaining numerator is
\(\sum_{\ell=1}^{N-1}d_{N-\ell}(Q^{a\ell}-Q^{b\ell})
=d_N(r^a)-d_N(r^b)\). The diagonal instead counts \(N-\ell\)
terms and gives the derivative in (15). Thus (15) retains the
original interpolation forcing and its diagonal; it is not a
replacement by an unforced reciprocal-factorial continuation.

**Proposition 2.** In the original coordinates used for the positive
type-three theorem, the separated wrapped insertion is exactly
\[
       M A_4^{\mathrm{wrap}}M^{-1}
          =\kappa^2 M^*
             \operatorname{diag}(\overline{P_a})\,M\mathcal R.
 \tag{16}
\]
The main insertion has the same expression with
\(\mathcal R\) replaced by \(D_P^{-1}-\mathcal R\).

*Proof.* The braid relation and the definition of \(\mathsf S\) give
\(MV B^{-1}=M^*\mathcal U\).
Also
\(\mathcal U D_P^{-1}\mathcal U^*
 =\operatorname{diag}(\overline{P_a})/N\), because
\(P_{D-a}=N/\overline{P_a}\). Substitute these two identities and
(14) into (5), (8); the scalar is exactly \(\kappa^2\).
Finally \(D_{\mathrm{main}}+D_{\mathrm{wrap}}\) is the circulant
matrix with entries \(d_{b-a\bmod N}\), and its transform by
\(\mathcal F\) is \(D_P^{-1}\). This proves both assertions.
\(\square\)

In particular (16) converts the problem to a specified matrix in the
original positive-three coordinates using only a unitary Fourier
transform. It does not assign a small norm to that matrix. For example,
the immediate bound is still only
\[
 \|M A_4^{\mathrm{wrap}}M^{-1}\|_2
 \le \|M\|_2^2\,\max_a S_a\,
             \left(\sum_a S_a^{-2}\right)^{1/2}.
 \tag{17}
\]
A useful exponential estimate must improve this coherent product or
its actual observed word. The off-diagonal differences and the
diagonal derivative in (15) cannot be estimated independently and
then assumed to preserve the original action.

There is a stronger triangular statement for the *relative* insertion.
Define
\[
 \mathcal E=\operatorname{diag}(\overline{P_a})M\mathcal R M^{-1}.
 \qquad
 M A_4^{\mathrm{wrap}}M^{-1}=\kappa^2M^*\mathcal E M .
 \tag{18}
\]
By (14),
\(M\mathcal R M^{-1}
=\mathcal U L D_{\mathrm{wrap}}L^{-1}\mathcal U^*\).
The middle product is strictly lower triangular, while \(\mathcal U\)
reverses the ordering and adds diagonal unit phases. Thus \(\mathcal E\)
is strictly upper triangular, of rank \(N-1\), and has nilpotency
order \(N\). Its first superdiagonal is nonzero because all diagonal
factors and the first subdiagonal of \(D_{\mathrm{wrap}}\) are nonzero.
The complete relative type-four insertion is instead exactly
\(\kappa^{-1}M\); the main part is
\(\kappa^{-1}M-\mathcal E\).

In particular the right null direction left unspecified by (10) is
\[
                 \ker A_4^{\mathrm{wrap}}
                      =\operatorname{span}\{M^{-2}e_0\}.
 \tag{19}
\]
This follows from \(\ker\mathcal E=\operatorname{span}\{e_0\}\)
and (18). It is an identity for the actual full insertion, not a
claim that an arbitrary ordinary boundary vector lies in this kernel.
The nilpotent relative matrix still lies between the different
factors \(M^*,M\). Bounds for its powers alone consequently do not
control a word of original insertions.

## 6. Reproduction

Run:

    python3 experiments/check_mixed_wrapped_operator_factorization.py

The focused exact checks compare the coefficient matrices with the
literal original crossings at both parities, retain the common
similarity and all scalars, and verify (7)--(19). They do not use
finite numerical rates as evidence for a global estimate.
