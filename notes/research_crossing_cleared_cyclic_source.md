# A cleared cyclic product formula for the original crossing source

Written research proof, 22 November 2026.

The full crossing source is an explicit sum of \(N\) products of
quadratic factors. The formula has no cyclic-norm or source-forcing
denominator. Its apparent factor \(C^{-N}\) is removable as a
polynomial identity, including at every resonance. A separate
cyclic-rotation argument proves that divisibility directly.

This is an exact formula for the original scalar and its full
coherent tensor. It does not prove a saddle contribution, a
noncancellation estimate, or a general Conway-gluing theorem.

## 1. The original source and its cleared equation

Fix
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 p=Q^{-1},\quad \eta=(-1)^d .
 \tag{1}
\]
Use the full source algebra and centered basis of [T, Section 1]:
\[
 U_x=\sum_{j=0}^d x^j f_j,\qquad
 \phi(f_i f_j)=\delta_{ij},\qquad f_0f_d=N^{-1}1.
 \tag{2}
\]
These identities hold in the complete nonreduced algebra, including
its repeated-root derivative coordinates. In the original phases put
\[
 \Phi(C,H,K)=\phi(f_0U_{-C}U_{-H}U_{-K}),\qquad
 J=\frac{\eta}{N}
       [2+C^N+H^N+K^N-(CHK)^N].
 \tag{3}
\]
The source is symmetric and separately of degree at most \(d\).
The entire proof of [T] gives the polynomial equation
\[
 (1-C/q)^2\Phi(pC,H,K)
       -(1-CH)(1-CK)\Phi(C,H,K)=CJ .
 \tag{4}
\]
Only this exact algebraic equation, the source definition, and
the full-basis identities are imported. None of [T]'s analytic
normalization or asymptotic estimates is used here.

For \(0\le r<N\) define
\[
 A_r=(1-Cq^{-1}p^r)^2,\qquad
 B_r=(1-CHp^r)(1-CKp^r),\qquad
 \Phi_r=\Phi(Cp^r,H,K).
 \tag{5}
\]
Thus \(A_r\Phi_{r+1}-B_r\Phi_r=Cp^rJ\),
\(\Phi_N=\Phi_0\), and \(J\) is unchanged around this cycle.

## 2. The finite product formula

Empty products below equal one. Put
\[
 T_r=Cp^r
          \prod_{s<r}A_s\prod_{s>r}B_s,\qquad
 \mathscr S_N=\sum_{r=0}^{N-1}T_r ,
 \tag{6}
\]
where both products have indices in \(\{0,\ldots,N-1\}\).

**Theorem 1.** In the polynomial ring \(\mathbb C[C,H,K]\),
\[
 \boxed{\qquad C^N\Phi(C,H,K)=\frac{\eta}{N}\mathscr S_N(C,H,K).
                                                        \qquad}
 \tag{7}
\]
In particular \(C^N\) divides \(\mathscr S_N\), and
\[
 \boxed{\qquad
 \Phi(C,H,K)=\frac{\eta}{N}
           \left(\mathscr S_N(C,H,K)/C^N\right).
                                                        \qquad}
 \tag{8}
\]
The quotient in (8) means polynomial division, including at \(C=0\).
It has degree at most \(d\) in each boundary variable. No individual
\(A_r,B_r\), central forcing \(J\), or cyclic-norm difference
is divided by at any specialization.

**Proof.** Multiply the \(r\)-th equation following (5) by
\(\prod_{s<r}A_s\prod_{s>r}B_s\), and sum. Consecutive
\(\Phi_r\)-terms cancel in their actual order, giving
\[
 \left(\prod_r A_r-\prod_r B_r\right)\Phi=J\mathscr S_N .
 \tag{9}
\]
Since \(p\) is primitive of order \(N\) and \(q^{-N}=-1\),
\[
 \begin{split}
 \alpha:=\prod_r A_r&=(1+C^N)^2,\\
 \beta:=\prod_r B_r&=[1-(CH)^N][1-(CK)^N],\\
 \alpha-\beta&=\frac N\eta C^N J .
 \end{split}
 \tag{10}
\]
The polynomial \(J\) is not the zero polynomial. Cancellation in
the polynomial integral domain proves (7); this is not pointwise
division by its specialized value. Therefore (7) holds also when
\(J=0\), \(\alpha=\beta\), or some individual factor vanishes.
The degree of \(\mathscr S_N\) in \(C\) is at most \(2N-1\).
Its degrees in \(H,K\) are at most \(N-1\). Division in (7)
proves the stated bounds. \(\square\)

No root factorial, square root, or choice of logarithm enters this
formula. The original scalar normalization is the one in (3)--(4);
no additional carrier or framing scalar has been inserted.

## 3. Independent divisibility and polynomial selection

The cancellation in the proof can be supplemented by a construction
that proves divisibility without knowing \(\Phi\). Define
\[
 \mathsf T(C)=
   \begin{pmatrix}A_0(C)&C\\0&B_0(C)\end{pmatrix},\qquad
 \mathsf P(C)=\mathsf T(C)\mathsf T(pC)\cdots\mathsf T(p^{N-1}C).
 \tag{11}
\]
Its diagonal entries are \(\alpha,\beta\), and its upper entry is
exactly \(\mathscr S_N\), with the prefix and suffix in (6).
Both diagonal entries depend only on \(C^N\). Cyclic rotation,
without inverting any matrix, gives
\[
 \mathsf T(C)\mathsf P(pC)=\mathsf P(C)\mathsf T(C),
 \quad
 A_0\mathscr S_N(pC)-B_0\mathscr S_N(C)=C(\alpha-\beta).
 \tag{12}
\]
Work over \(\mathbb C[H,K][C]\). One has \(\mathscr S_N(0)=0\).
If its first nonzero coefficient had degree \(m\) with \(1\le m<N\),
the degree-\(m\) coefficient on the left of (12) would be
\((p^m-1)[C^m]\mathscr S_N\), which is nonzero. The right side
is divisible by \(C^{N+1}\), by (10). This contradiction proves
\[
                         C^N\mid\mathscr S_N .
 \tag{13}
\]
Set \(\Psi=(\eta/N)\mathscr S_N/C^N\). Dividing the polynomial
identity (12) by \(C^N\), and using \(p^N=1\), shows that
\(\Psi\) satisfies (4).

There is at most one rational solution of (4). Indeed a difference
\(Y\) of two solutions satisfies the homogeneous cleared equation.
The same telescoping over its full cycle gives
\((\alpha-\beta)Y=0\). Since \(\alpha-\beta\) is not identically
zero, \(Y=0\) over the rational function field. Hence \(\Psi=\Phi\).
At resonant parameter values the selected solution is the polynomial
family (8), not an independently chosen homogeneous specialization.
All its parameter derivatives follow by differentiating that family.
For example its exact endpoint value is
\[
                  \Phi(0,H,K)=\frac{\eta}{N}[C^N]\mathscr S_N .
 \tag{14}
\]

## 4. The complete coherent tensor remains present

Formula (8) computes the whole polynomial, not just values at
Casimir nodes. Its coefficients are the actual weighted tensor:
\[
 \phi(f_0 f_i f_j f_k)
    =(-1)^{i+j+k}[C^iH^jK^k]\Phi .
 \tag{15}
\]
Multiplication by \(f_0\) is invertible on the full algebra, with
inverse multiplication by \(v=Nf_d\), by (2).
For arbitrary packets \(x,y\), form the coefficient column
\(b_i=\phi(f_0f_i xy)\). Bilinear duality gives
\(b=M_{f_0}(xy)\), so the complete output is \(xy=M_v b\).
Thus no physical boundary dimension or derivative direction has
been removed.

Equivalently use the \(N\) distinct activities
\(C_i=q^{-1}Q^{-i}\) and their cardinal polynomials
\[
 L_i(C)=\frac1N\sum_{a=0}^d(C/C_i)^a .
 \tag{16}
\]
Finite character orthogonality proves \(L_i(C_j)=\delta_{ij}\).
The separate degree bounds therefore give exactly
\[
 \Phi(C,H,K)=\sum_{i,j,k=0}^d
       \Phi(C_i,C_j,C_k)L_i(C)L_j(H)L_k(K).
 \tag{17}
\]
This is ordinary full-basis interpolation. Together with (15)
and the unit \(f_0^{-1}\), it preserves the original open
Newton/Hermite multiplication tensor. It is not a semisimple
evaluation quotient or a two-channel physical replacement.

## 5. Summand transport and the classical symbol

The adjacent terms in the literal finite sum obey the cleared relation
\[
 B_{r+1}T_{r+1}=pA_rT_r\qquad(0\le r<N-1).
 \tag{18}
\]
Generically their ratio is \(pA_r/B_{r+1}\). This is an interior
ratio only: the first and last terms are the actual products
\(T_0=C\prod_{s=1}^{d}B_s\) and
\(T_d=Cp^d\prod_{s=0}^{d-1}A_s\).
There is no periodically extended summand or omitted endpoint.

Writing \(s=Cp^r\), the formal leading ratio as \(p,q\to1\) is
\[
 \frac{(1-s)^2}{(1-Hs)(1-Ks)}.
 \tag{19}
\]
Its stationary-symbol equation is
\[
 (1-s)^2-(1-Hs)(1-Ks)
       =s[(H+K-2)+(1-HK)s]=0.
 \tag{20}
\]
Away from the displayed degeneracies the nonzero root is
\(s_*=(2-H-K)/(1-HK)\).
These are algebraic symbol calculations only. They do not locate
an accessible saddle or estimate its original coefficient.

## Proof source and scope

The sole complete proof source is [T],
[full-parameter source transport](research_crossing_full_parameter_transport.md),
504 lines, SHA-256
e0fc1e954b5906b4b3e7656112b9773ce4c1c1a97e2a6edeacc8b45f801df5a3.
It was read in its entirety at this renewed matching pin.

The balanced affine monodromy in the
[earlier Gamma-source note](research_crossing_exact_gamma_source_extension.md),
Section 5, already has the finite forced-cycle sum and generic rational
selection. Those elementary methods are not claimed as new here.
The present assertion is the cleared unbalanced product formula,
its independent root-of-unity divisibility, and its identification
with the full original tensor. It removes source-norm denominators,
but does not make the summands positive or prevent cancellation.
General inverse pairings, turns and the original Conway closing
still require their scalar analytic estimate.

Only written algebra and text/hash inspection were used. No
mathematical program, numerical experiment, test, build, git action,
or earlier-final file edit was performed.
