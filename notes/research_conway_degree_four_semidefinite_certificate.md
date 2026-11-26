# An exact degree-four certificate for the Conway source minimum

21 November 2026. Research note. Earlier final notes and the public
manuscripts remain unchanged.

The normalized Conway energy has an exact semidefinite formulation at
degree four. Increasing the quantum level enlarges the matrices but does
not increase the degree of the certificate. The argument uses the
Hilbert--Schmidt normalization of the actual tensors, not convexity alone.
Every complex coefficient and every repeated-root boundary direction is
retained.

This reformulates the finite-level minimum. It does not evaluate its
exponential rate or prove a new knot volume theorem.

## 1. The original energy and the proposed certificate

Use the complete normalized compiler of
[the convex source theorem](research_convex_normalized_conway_source.md).
There are \(s\) proper vertices. At level \(N\), the packet at each
vertex belongs to the full complex Newton space \(H_N\) of dimension
\(N\). A local map \(\Phi_v\) is a prescribed constant, a complex
linear map, or a complex bilinear map with two distinct child inputs.
Each child has at most one parent. The closing root is the original
complex row \(L\), applied at the top proper vertex.

The budgets in that theorem give, with \(\sigma=1/16\),
\[
 \|\Phi_v\|_{\rm HS}\le\sigma,\qquad \|L\|\le\sigma.
 \tag{1}
\]
For a bilinear map, its Hilbert--Schmidt norm is the Euclidean norm
of its three-index coefficient array in the prescribed orthonormal
Newton coordinates. Constant maps use their vector norm. Multiplication
by the known per-subtree budgets has already been recorded; their total
product is \(B_{\rm tot}\).

Regard all real and imaginary packet coefficients as coordinates
\(x\in\mathbb R^n\), where \(n=2Ns\). Put
\[
 g_v(x)=1-\|x_v\|^2,\qquad
 \mathcal D=\{x:g_v(x)\ge0\text{ for all }v\},
\]
\[
 G_v(x)=\Phi_v((x_c)_c)-x_v,\qquad
 E(x)=\sum_v\|G_v(x)\|^2+|Lx_{\rm top}|^2,
 \qquad e_* =\min_{\mathcal D}E.
 \tag{2}
\]
The source theorem proves that the minimizer \(a_*\) is unique and
interior, with \(\nabla E(a_*)=0\), and that
\[
 B_{\rm tot}^2 e_*\le |K_N|^2
       \le\frac{197}{196}B_{\rm tot}^2 e_*.
 \tag{3}
\]
In particular this minimum is zero exactly when the original invariant
is zero.

A real polynomial is a sum of squares if it is a finite sum of squared
real polynomials. Absolute squares of complex polynomials count as two
real squares. Define the degree-four quadratic module
\[
 Q_2(g)=\left\{s_0+\sum_v g_v s_v:
 \begin{array}{l}
 s_0\text{ is a sum of squares of polynomials of degree at most }2,\\
 s_v\text{ is a sum of squares of polynomials of degree at most }1
 \end{array}\right\}.
 \tag{4}
\]
Every member is nonnegative on \(\mathcal D\). The main assertion is
\[
                         E-e_*\in Q_2(g).               \tag{5}
\]
The coefficients of this particular existence certificate can depend
on \(a_*\). The optimization problem which searches over (4) uses
only the known coefficients of \(E\) and \(g_v\); it is not given
the unknown minimizer or invariant as input.

## 2. Two algebraic estimates for a small tensor

The following facts establish polynomial identities, rather than just
pointwise inequalities on the balls. In this section \(h\) denotes
variation variables. Every polynomial being squared is linear in
\(h\), though it may also depend linearly on a packet variable or
its conjugate.

Let \(T(x,v)\) be a complex bilinear map with coefficient norm at
most \(\sigma\). For either sign,
\[
 \sigma(\|u\|^2+\|v\|^2)
                   \mathbin\pm2\operatorname{Re}\langle u,T(x,v)\rangle
   = S(x,u,v)+\sigma(1-\|x\|^2)\|v\|^2,             \tag{6}
\]
where \(S\) is a sum of absolute squares of polynomials linear in
\((u,v)\).
To see this, complete the square
\(\|\sqrt\sigma u\pm\sigma^{-1/2}T(x,v)\|^2\).
The remaining expression, apart from the displayed ball term, is
\[
 \sigma^{-1}\{\sigma^2\|x\|^2\|v\|^2-\|T(x,v)\|^2\}.
\]
It is a sum of squares because the matrix of \(T\), acting on
\(x\otimes v\), has operator norm at most its coefficient norm
\(\sigma\). A positive semidefinite constant Gram matrix factors
as a square. Conjugating any of the displayed variables does not change
this real polynomial conclusion. For a linear map of norm at most
\(\sigma\), the corresponding expression without the packet \(x\)
is a nonnegative constant quadratic form, hence a sum of squares.

Next let \(B\) be a complex bilinear map with coefficient norm at
most \(\sigma\). Then
\[
 \begin{split}
 &\sigma^2(\|h_1\|^2+\|h_2\|^2)
       +2\operatorname{Re}\langle B(x_1,x_2),B(h_1,h_2)\rangle\\
 &\qquad=S_B(x,h)
   +\sigma^2(1-\|x_1\|^2)\|h_1\|^2
   +\sigma^2(1-\|x_2\|^2)\|h_2\|^2,                 \tag{7}
 \end{split}
\]
with \(S_B\) a sum of squares of polynomials linear in \(h\)
and linear in \(x\). Here is a coefficient proof of the required positivity.
Write \(B_{iab}\) for the tensor and set
\[
 C_{(a,a'),(b,b')}=\sum_i\overline{B_{iab}}B_{ia'b'},\quad
 U=x_1\otimes\overline{h_1},\quad
 V=\overline{x_2}\otimes h_2.
\]
Then \(U^*CV=\langle B(x_1,x_2),B(h_1,h_2)\rangle\).
The matrix \(C\) is a reshuffling of the Gram matrix of the flattened
tensor. Thus
\[
 \|C\|_{\rm op}\le\|C\|_{\rm HS}
     \le\|B\|_{\rm HS}^2\le\sigma^2.
\]
Consequently
\(\sigma^2(\|U\|^2+\|V\|^2)+2\operatorname{Re}U^*CV\)
is a positive semidefinite constant quadratic form in \((U,V)\).
Factoring it and adding the two displayed ball terms proves (7).

One further use of (6) gives
\[
 \sigma(\|h_1\|^2+\|h_2\|^2)
            -2\operatorname{Re}\langle x_0,B(h_1,h_2)\rangle
 =S_0(x_0,h)+\sigma(1-\|x_0\|^2)\|h_2\|^2.         \tag{8}
\]
Indeed reshape the same tensor to the map
\(T(\overline{x_0},h_2)_a=\sum_{i,b}\overline{x_{0,i}}B_{iab}h_{2,b}\)
and use \(u=\overline{h_1}\) in (6). Reshuffling preserves its
coefficient norm.

## 3. A degree-two matrix certificate for the Hessian

Let \(H(x)=D^2E(x)\) be the real Hessian, and let \(h\) be a real
variation, identified with complex packet variations. Write \(A=D\Phi\)
for the derivative of the full local recursion. Direct differentiation
of (2) gives
\[
 \begin{split}
 \tfrac12h^{\mathsf T}H(x)h
 ={}&\|h\|^2
   -2\operatorname{Re}\sum_v\langle h_v,D\Phi_v(x)h\rangle
   +\|A(x)h\|^2+|Lh_{\rm top}|^2\\
 &+\sum_{v\text{ product}}\left\{
 2\operatorname{Re}\langle B_v(x_L,x_R),B_v(h_L,h_R)\rangle
 -2\operatorname{Re}\langle x_v,B_v(h_L,h_R)\rangle\right\}.
 \tag{9}
 \end{split}
\]
For a product,
\(D\Phi_vh=B_v(h_L,x_R)+B_v(x_L,h_R)\).
Apply (6) to each term in the second term of (9); use its constant
linear-map version at turns. The required constant allowance is at
most \(3\sigma\|h\|^2\): a parent contributes at most twice,
and a given child occurs in at most one parent. The unused part of
this allowance is itself a nonnegative diagonal quadratic form.

Apply (7) and (8) at each product to the last line of (9). Their
constant allowances sum to at most
\((\sigma^2+\sigma)\|h\|^2\), because the sibling pairs at
distinct products are disjoint. All remaining terms in (9) are already
squared norms. We have therefore proved an identity
\[
 \tfrac12h^{\mathsf T}H(x)h
 -(1-4\sigma-\sigma^2)\|h\|^2
       = S(x,h)+\sum_v g_v(x)h^{\mathsf T}C_vh,         \tag{10}
\]
where \(S\) is a sum of squares of polynomials linear in \(h\)
and of degree at most one in \(x\), and the \(C_v\) are constant positive
semidefinite real matrices. In particular, the expression on the right
has degree at most two in \(x\). All factorization statements hold
in real coordinates; none requires the Casimir operator to be Hermitian.

Since \(1-4\sigma-\sigma^2=191/256>1/2\), (10) implies
\[
 h^{\mathsf T}(H(x)-I)h
       =\sum_\nu |W_\nu(x)h|^2
          +\sum_v g_v(x)h^{\mathsf T}V_vh,             \tag{11}
\]
with \(W_\nu\) affine matrix polynomials and constant
\(V_v\succeq0\). This is stronger than a numerical Hessian bound:
it records a polynomial certificate with a fixed degree.

## 4. Integrating the certificate without increasing its degree

Set \(h=x-a_*\) and \(x(t)=a_*+th\). Taylor's integral formula
and interior stationarity give
\[
 E(x)-e_* =\int_0^1(1-t)h^{\mathsf T}H(x(t))h\,dt.
 \tag{12}
\]
The \(I\) term of (11) contributes \(\|h\|^2/2\).
The integral of every squared term in (11) is a sum of squares of
polynomials of degree at most two in \(x\): expand in the finite
monomial vector and integrate its positive semidefinite Gram matrix.

For the constraint terms use the exact identity
\[
 g_v(x(t))=(1-t)g_v(a_*)+t g_v(x)+t(1-t)\|h_v\|^2.
\]
Since \(V_v\) is constant, its contribution in (12) is
\[
 \frac{g_v(a_*)}{3}h^{\mathsf T}V_vh
 +\frac{g_v(x)}6h^{\mathsf T}V_vh
 +\frac{\|h_v\|^2}{12}h^{\mathsf T}V_vh.               \tag{13}
\]
The first and third terms are sums of squares; the first uses
\(g_v(a_*)>0\). The middle term is the constraint \(g_v(x)\)
times a sum of squares of linear polynomials. This proves (5), with
the additional explicit squared term \(\|x-a_*\|^2/2\).
No theorem asserting that every convex quartic is a sum of squares has
been used.

## 5. The exact finite semidefinite problem

For a real polynomial \(p\), a Gram representation
\(p=m_r(x)^{\mathsf T}Qm_r(x)\), \(Q\succeq0\), is a
sum-of-squares representation of degree at most \(2r\).
Here \(m_r\) is the vector of all monomials of degree at most \(r\).
Coefficient matching is linear in the entries of \(Q\).
It follows directly from (5) and nonnegativity on \(\mathcal D\) that
\[
 e_* =\max\{\lambda:E-\lambda\in Q_2(g)\}.            \tag{14}
\]
The maximum is attained. The largest Gram block has size
\(\binom{n+2}{2}\); each constraint block has size \(n+1\).
These are upper bounds using dense monomial vectors, not a claim of
optimal sparsity.

For completeness the matching moment formulation is also exact.
A truncated functional \(\mathcal L\) on polynomials of degree at
most four is feasible when
\[
 \mathcal L(1)=1,\quad \mathcal L(p^2)\ge0\ (\deg p\le2),\quad
 \mathcal L(g_v p^2)\ge0\ (\deg p\le1).
 \tag{15}
\]
These are precisely positive semidefinite moment and localizing matrix
constraints. Equation (5) gives \(\mathcal L(E)\ge e_*\) for
every feasible functional. Evaluation at \(a_*\) is feasible and
attains equality. Thus
\[
                    e_* =\min_{\mathcal L\text{ satisfying }(15)}
                                                    \mathcal L(E).       \tag{16}
\]
This proves equality and attainment on both sides without appealing
to a constraint qualification for abstract conic duality.
Moreover any optimal \(\mathcal L\) has
\(\mathcal L(\|x-a_*\|^2)=0\), by the extra square following
(13). Positivity and Cauchy--Schwarz then recover its first moments
as \(\mathcal L(x)=a_*\).

## 6. Consequences and the remaining volume estimate

The normalized source minimum has one exact degree-four semidefinite
formulation at every level. There is no relaxation-degree error to
control and no need to increase a moment hierarchy to reach this
particular minimum. Fixed connected short components can still be
absorbed by the separate boundary-energy theorem. If its higher-degree
compressed maps are used instead, (14) is not automatically a degree-four
statement about that new objective; retaining the original local gates
preserves the result proved here.

An explicit feasible certificate \(E-\lambda\in Q_2(g)\) gives
\[
                       |K_N|^2\ge B_{\rm tot}^2\lambda.
 \tag{17}
\]
For a volume lower bound one still needs certificates with
\[
 \frac\pi N\log(B_{\rm tot}^2\lambda_N)
                  \longrightarrow\operatorname{Vol}(S^3\setminus K),
 \qquad \lambda_N>0,
\]
together with the matching upper bound. Neither (5) nor (14) constructs
such a geometric family. The source phases remain in the coefficients
of the semidefinite problem, so exact cancellations remain possible.
The result supplies a fixed-degree algebraic form of the missing lower
bound, not that lower bound itself. Matrix size and the accuracy needed
to resolve an exponentially small optimum still grow with the level.

## Sources and coverage

The sole direct proof source was read in full at the matching pin:

| Source | SHA-256 |
|---|---|
| [Normalized original Conway source](research_convex_normalized_conway_source.md) | 6b89b4c6a67ef7a32cc41a5966c650f32de65d284ae7b70d94a71bddba21df3c |

The identities (6)--(13) and the exact semidefinite formulations are
proved above. General connections between convexity, Hessian certificates
and semidefinite representations are established literature; see
[Helton--Nie](https://arxiv.org/abs/0705.4068),
[Lasserre](https://arxiv.org/abs/0806.3784), and
[Kriel--Schweighofer](https://arxiv.org/abs/1704.07231).
Their stated coverage was checked from the primary records; none of
their proofs or finite-order exactness assertions is an assumption here.
The specific assertion proved here is the degree-four certificate for
the normalized physical tree energy. No novelty is claimed for the
general sum-of-squares or moment methods.

Only written mathematics, literature lookup, and text/hash operations
were used. No mathematical program, test, numerical optimization, build,
git operation or earlier-final edit was performed.
