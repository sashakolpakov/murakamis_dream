# A primitive quantum cap with its original boundary source

Research note, 3 November 2026.

The square in the classical rational-word cap has a finite quantum
counterpart. Three invertible bidiagonal or diagonal matrices carry
the original crossing and turn actions by rational substitutions.
One factor of the transported cap has a simple kernel. Its closing
minor is an exactly normalized product of two neighboring original
sources. The other factor restores the full repeated-root cap.

These identities give a sparse block formulation of the boundary
problem. They do not make that block matrix positive or bound its
inverse. An explicit forced first-order equation for the terminal
two-crossing source shows why those further estimates matter.

## 1. Three finite coordinates

Let \(N\ge2\), \(D=N-1\), \(q=e^{\pi i/N}\),
\(Q=q^2\), \(\eta=(-1)^D\), and
\(\kappa=q^{D^2/2}\). Retain the original Newton matrices
\(M,J,Z,L=Z^T\) of the
[normalized cofactor theorem](research_rational_word_normalized_cofactor.md).
In particular \(M\) includes its scalar \(\kappa\), and \(J\)
reverses the coefficient coordinates. Write
\[
 X\mathbf e_j=Q^j\mathbf e_j,\qquad
 E\mathbf e_j=\mathbf e_{j+1\bmod N},\qquad XE=QEX.
 \tag{1}
\]
Define
\[
 \begin{split}
 K&=-q^{-1}X^{-1}+(I-X^{-1})E,\\
 B&=JKJ=-qX+(I-QX)E^{-1}.
 \end{split} \tag{2}
\]
The wrap entries in both matrices vanish. Thus \(K\) is lower
bidiagonal and \(B\) is upper bidiagonal in the original finite
interval, not in an altered periodic source.

Their diagonal entries are respectively \(-q^{-1}Q^{-j}\) and
\(-qQ^j\). These are distinct, so
\[
 K^N=B^N=\eta I,\qquad \det K=\det B=1,
 \qquad \det X=\eta.                                  \tag{3}
\]
In particular all three coordinates are invertible at both parities.
Direct multiplication gives
\[
 XK-QKX=(q-q^{-1})I,\qquad
 Z=qX+q^{-1}I+(X-I)K.                                  \tag{4}
\]
If \(c_0=q+q^{-1}\), the two original caps factor as
\[
 \boxed{\quad
 Z-c_0I=(X-I)(K+qI),\qquad
 L-c_0I=(Q^{-1}X^{-1}-I)(B+qI).
 \quad}                                                \tag{5}
\]
These are ordered products. They retain the original endpoint
normal; their factors must not be replaced by their distinct-root
values.

## 2. The actual crossing and turn substitutions

For \(\Phi_G(A)=GAG^{-1}\), the exact substitutions are
\[
 \begin{array}{c|ccc}
 &X&K&B\\ \hline
 \Phi_M&-q^{-1}K^{-1}&(I-X)K-q^{-1}I&
 -Q^{-1}X^{-1}B-q^{-1}(I+X^{-1})\\[2pt]
 \Phi_{M^{-1}}&A&-q^{-1}X^{-1}&-QAB-q(A+I)\\[2pt]
 \Phi_J&Q^{-1}X^{-1}&B&K,
 \end{array}                                           \tag{6}
\]
where, only in the second row,
\[
                  A=X+q^{-1}XK+q^{-2}I.                \tag{7}
\]

Here is a proof using the original matrices, rather than the
commutative trace surface. Their crossing coefficients are
\[
 M_{kj}=\kappa(-1)^kq^{k(j+1)}
                  \frac{S_k}{S_jS_{k-j}},\qquad
 S_k=\prod_{r=1}^k2\sin(r\pi/N),\quad j\le k.
 \tag{8}
\]
Taking consecutive-column ratios in (8), including the first and
last columns, proves
\[
 M^{-1}XM=X+q^{-1}(X-I)E,\qquad
 MX^{-1}M^{-1}=-qK.                                    \tag{9}
\]
For example the subdiagonal coefficient in the first identity is
\(q^{-1}(Q^j-1)\) in row \(j\). There is no wrap correction.
The first formula equals (7) by (4). Inverting the second gives
\(\Phi_M(X)\); conjugating (4), using \(MZ=ZM\), gives
\(\Phi_M(K)=qX-Z=(I-X)K-q^{-1}I\).

The original braid identity is
\(MJM=\kappa JM^{-1}J\); it follows equivalently from
equation (6) of the
[full two-boundary chain identity](research_internal_two_crossing_chain.md).
Together with \(JX^{-1}J=QX\), it gives
\[
 \Phi_M(B)=-qJ(M^{-1}XM)J
   =-q^{-1}X^{-1}+(I-Q^{-1}X^{-1})E^{-1}=K^T.            \tag{10}
\]
The last expression equals the first row's formula in (6).
Solving that identity after applying \(\Phi_{M^{-1}}\) gives
\(-QAB-q(A+I)\), with the displayed order. The other inverse
formula follows directly from (9). The turn row follows from (1)--(2).
This proves all of (6) at every level, including \(N=2\).

For a word \(W\), apply these rules from left to right, appending
each new letter on the right: \(\Phi_{WG}=\Phi_W\circ\Phi_G\).
Denote the resulting coordinates by \(X_W,K_W,B_W\).
Every inverse in this procedure is of an invertible conjugate of
\(X\), \(K\), or \(B\). There is no division by
\(X-I\), \(I-QX\), a vanishing cap eigenvalue, or a selected
boundary value.

## 3. A simple cap and its polarized normalization

Put \(f_W=W\mathbf e_0\), and let \(F_W(z)\) be its full
Newton polynomial. Define
\[
 G_W=B_W+qI,\qquad
 T_W=Q^{-1}X_W^{-1}-I,\qquad D_W=T_WG_W.
 \tag{11}
\]
By (5), \(D_W=W(L-c_0I)W^{-1}\), exactly the operator in the
normalized cofactor theorem. The matrix \(G_W\) has a simple
zero eigenvalue and
\[
                         \ker G_W=\mathbb C f_W.       \tag{12}
\]
This assertion does not discard the repeated-root algebra:
\(T_W\) remains present in the original cap \(D_W\).

**Theorem 1.** At every level and for every original rational word,
\[
 \boxed{\quad
 \operatorname{adj}(G_W)J
       =Nq^D\kappa\,f_W f_{WM^{-1}}^\dagger.
 \quad}                                                \tag{13}
\]
In particular the primitive closing minor satisfies
\[
 \boxed{\quad
 (-1)^D\det G_W[\{1,\ldots,D\},\{0,\ldots,D-1\}]
 =Nq^D\kappa\,
       \phi_N(F_W)\overline{\phi_N(F_{WM^{-1}})}.
 \quad}                                                \tag{14}
\]
Thus it is a product of two neighboring original sources, with
its scalar retained. It is not in general a modulus square.
For example, when \(W=M\), its right side is zero because
\(\phi_N(1)=0\), whereas \(\phi_N(R)=\kappa^{-1}\ne0\).
Thus the primitive closing minor alone cannot replace the full
cap, even when the original closing scalar is nonzero.

*Proof.* For \(G=B+qI\), a right nullvector is \(\mathbf e_0\)
and a left nullvector with first coordinate one is
\[
                  \alpha_j=(-q^{-1})^j.                 \tag{15}
\]
The product of the nonzero eigenvalues is
\(\prod_{j=1}^D q(1-Q^j)=Nq^D\). Hence
\(\operatorname{adj}(G)=Nq^D\mathbf e_0\alpha^T\).
The last row of (8) gives exactly
\[
                    \alpha^T=\kappa\mathbf e_D^TM.     \tag{16}
\]
Indeed \(\kappa^2\eta q^D=1\). All original words satisfy
\(W^\dagger JW=J\). With \(V=WM^{-1}\), it follows that
\[
 \alpha^TW^{-1}J
   =\kappa\mathbf e_D^TV^{-1}J
   =\kappa(V\mathbf e_0)^\dagger.
\]
Conjugating the base adjugate proves (13), and its \((D,D)\)
entry proves (14). No source scalar was divided out. \(\square\)

Equation (13) also gives the full polarized boundary polynomial
by contraction with the Newton evaluation vectors. In particular
it retains first normals at repeated roots in either free boundary.

The second cap factor restores the familiar square with its exact
normalization. At the base point,
\[
 \operatorname{adj}(Q^{-1}X^{-1}-I)
                 =\eta N\mathbf e_D\mathbf e_D^T,
 \qquad \alpha_D=\eta q^{-D}.
 \tag{17}
\]
Using \(\operatorname{adj}(T G)=\operatorname{adj}(G)
\operatorname{adj}(T)\), and conjugating, therefore gives
\[
              \operatorname{adj}(D_W)J=N^2f_Wf_W^\dagger.
 \tag{18}
\]
This recovers the full original source rather than postulating
the scale of a kernel vector.

The recursion (6) has a finite block realization independent of
the level in its number of blocks. To see this constructively,
introduce an auxiliary vector for each addition, multiplication,
or inverse application in the rational expression. An inverse
application \(y=C^{-1}x\) is represented by the equation \(Cy=x\).
Products are represented by consecutive such equations. Equivalently
\(A+BC^{-1}D\) is the Schur complement of
\(\left(\begin{smallmatrix}A&B\\-D&C\end{smallmatrix}\right)\).
The starting blocks \(I,X,K,B\) have fixed bandwidth. Each inverted
coordinate is an actual conjugate from (6), with determinant of
modulus one by (3); hence the Schur eliminations introduce no
unrecorded exponential determinant factor. This is an exact sparse
block formulation, not a bound on the inverse or a positive energy.

## 4. An explicit forced quantum square

The first nontrivial example shows the role of the endpoint.
For \(W=JM^2\),
\[
 \boxed{\quad D_{JM^2}=B(Z-c_0I)B.\quad}                \tag{19}
\]
There is no adjoint in this product. For an algebraic verification,
the original trace recurrence and turn identities give
\[
 D_{JM^2}=(8q^{-1}-c_0)I-q^{-1}LL_1-q^{-2}Z,
 \qquad L_1=M^{-1}LM.
 \tag{20}
\]
Substituting the tridiagonal formula for \(L_1\) from the cofactor
note and (2), (5) into (20) gives (19), using
\(E^{-1}f(X)=f(QX)E^{-1}\). This is a formal quantum-torus
identity; its wrap entries vanish in the finite matrices.

The exact original two-crossing formula gives
\[
 (f_{JM^2})_j=\frac{Nq^{j^2}}{(Q;Q)_j}.
 \tag{21}
\]
Its consecutive ratios imply the finite forced equation
\[
                       B f_{JM^2}=\eta\mathbf e_D.     \tag{22}
\]
All rows below \(D\) cancel. The last row is
\(-qQ^D\kappa^2=\eta\), since \(\kappa^2=q^{D^2}\).
This is precisely the row that would be lost by replacing the
finite interval with an interior homogeneous recurrence.

The inverse is explicit. For \(0\le j\le k\le D\),
\[
 (B^{-1})_{jk}
 =-q^{-(k-j+1)}Q^{-\sum_{r=j}^k r}
                 \prod_{r=j+1}^k(1-Q^r),
 \qquad (B^{-1})_{jk}=0\quad(j>k).
 \tag{23}
\]
It follows by solving the upper bidiagonal system; it includes the
empty product when \(j=k\). Although \(\det B=1\) and its
diagonal entries all have modulus one, its inverse has exponentially
large entries. For example, choose \(j/N\to1/6\),
\(k/N\to5/6\) in (23). Then
\[
 \lim_{N\to\infty}\frac1N\log|(B^{-1})_{jk}|
       =\int_{1/6}^{5/6}\log(2\sin\pi x)\,dx>0.       \tag{24}
\]
The integrand is positive on the open interval and continuous on
this compact interval. Thus even an exact quantum square with
unit determinant factors does not have a polynomially conditioned
boundary problem.

Equation (22), on the other hand, determines the original source
without ambiguity. Its last component is \(\kappa^2\), so
\(|\phi_N(F_{JM^2})|=1\), while other components have exponential
growth. This is the same original-source discrepancy seen in the
[bulk square factorization](research_rational_word_cap_square_factorization.md),
now resolved by a literal endpoint-forced Green equation.

## 5. The remaining analytic question

The substitutions, cap factorization, and adjugate normalization
above are exact for arbitrary fixed signed words. They make the
primitive boundary problem explicit and preserve the original
source rather than merely its characteristic curve. A proof of
noncancellation for a general short negative word still has to
control the corresponding forced block inverse or the closing
minor (14). Neither its unit determinant denominators nor the
positive elementary cap energy supplies that control.

The [original-matrix check](../experiments/check_quantum_cap_primitive_source.py)
tests the substitutions, both cap factors, the polarized adjugate,
and the forced two-crossing equation. Its
[saved result](../repro/results/research-quantum-cap-primitive-source.json)
is a normalization diagnostic, not an asymptotic estimate.
