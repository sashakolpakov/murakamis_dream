# A degree-four certificate with constant physical gluing budgets

22 November 2026. Research note. Earlier finals and public manuscripts
remain unchanged.

The uniform physical quartic retains an exact degree-four semidefinite
formulation with its constant structural budgets. No extra power of the
level is needed to normalize multiplication's coefficient tensor.
The reason is specific to actual matrix multiplication: three explicit
matrix sum-of-squares identities replace the earlier small-tensor
estimates. They retain the complete original source, rather than a
distinct-root quotient or a positive substitute for the closing.

## 1. The unchanged physical objective

Use the full physical algebra, metric, literal operations and original
closing of the [uniform physical theorem](research_conway_uniform_physical_quartic.md).
Thus \(\mathcal A_N=\mathbb C[\Omega]\) has dimension \(N\), including
all repeated-root derivative directions, and inherits the
Hilbert--Schmidt norm from physical pair matrices.
Choose its prescribed orthonormal coordinates and regard their real
and imaginary parts as real variables.

There are \(s\) proper vertices. Their normalized maps are prescribed
constants, \(\mathcal T/16\) at turns, and actual multiplication
\(\Phi(X,Y)=XY/16\) at products. Put \(\sigma=1/16\).
The original normalized closing row is \(L\), with \(\|L\|\le\sigma\).
All leaf constants have norm at most \(\sigma\). The total budget is
exactly the earlier one:
\[
 B_{\rm ph}=16^m\max(1,|\eta_N|)
                  \prod_{\rm leaves}\max(1,\|A_j\|_{\rm ph}).
 \tag{1}
\]
Here \(m\) includes the closing root and \(\eta_N\) is its retained
known external scalar. No budget or source coefficient is changed.

Write \(x\) for the full real coordinate field, and define
\[
 g_v(x)=1-\|x_v\|^2,\quad
 \mathcal D=\{x:g_v(x)\ge0\ \hbox{for every proper }v\},
 \quad R_v=\Phi_v((x_c)_c)-x_v,
\]
\[
 E(x)=\sum_v\|R_v(x)\|^2+|Lx_{\rm top}|^2,\qquad
                         e_*=\min_{\mathcal D}E .
 \tag{2}
\]
All norms and adjoints use the uniform physical metric.
The physical theorem proves a unique interior minimizer \(a_*\), and
\[
 B_{\rm ph}^2e_*\le |K_N|^2
                  \le(197/196)B_{\rm ph}^2e_* .
 \tag{3}
\]
We prove that \(E-e_*\) belongs to the degree-four quadratic module
\[
 Q_2(g)=\{s_0+\sum_vg_vs_v:
       s_0\text{ is SOS of degree at most }4,\ 
       s_v\text{ is SOS of degree at most }2\}.
 \tag{4}
\]
Thus the squared polynomials in \(s_0\) have degree at most two;
those in \(s_v\) have degree at most one.

## 2. Three matrix identities

For arbitrary equally sized complex matrices define the Cauchy defect
\[
 \mathfrak C(A,B)=\|A\|_{\rm HS}^2\|B\|_{\rm HS}^2-\|AB\|_{\rm HS}^2.
\]
The row--column Lagrange identity gives the exact polynomial SOS
\[
 \mathfrak C(A,B)=
 \sum_{i,j}\sum_{k<l}
   |A_{ik}\overline{B_{lj}}-A_{il}\overline{B_{kj}}|^2 .
 \tag{5}
\]
Indeed apply the complex two-vector Lagrange identity to each row
of \(A\) and column of \(B\), and sum. Conjugates are real-linear
expressions in the real coordinates, so these are real polynomial
squares. An absolute square counts as two real squares.

Below \(X,Y,W\) are packet matrices and \(U,V,H,K\) are variation
matrices. Every norm is Hilbert--Schmidt and
\(\langle A,B\rangle=\operatorname{Tr}(A^*B)\).
Completing a square proves, for either sign,
\[
 \begin{split}
 &\sigma(\|U\|^2+\|V\|^2)
            \ \pm2\operatorname{Re}\langle U,\sigma XV\rangle\\
 &=\sigma\|U\pm XV\|^2+\sigma\mathfrak C(X,V)
                   +\sigma(1-\|X\|^2)\|V\|^2 .
 \end{split}
 \tag{6}
\]
The right-multiplication version uses \(VX\) and
\(\mathfrak C(V,X)\), with the same ball term.

For self-curvature, cyclicity of trace gives
\(\langle XY,HK\rangle=\langle H^*X,KY^*\rangle\).
Consequently
\[
 \begin{split}
 &\sigma^2(\|H\|^2+\|K\|^2)
                  +2\operatorname{Re}\langle\sigma XY,\sigma HK\rangle\\
 &=\sigma^2\|H^*X+KY^*\|^2
       +\sigma^2\mathfrak C(H^*,X)+\sigma^2\mathfrak C(K,Y^*)\\
 &\quad+\sigma^2(1-\|X\|^2)\|H\|^2
                +\sigma^2(1-\|Y\|^2)\|K\|^2 .
 \end{split}
 \tag{7}
\]
Finally the negative output-curvature term satisfies
\[
 \begin{split}
 &\sigma(\|H\|^2+\|K\|^2)
                   -2\operatorname{Re}\langle W,\sigma HK\rangle\\
 &=\sigma\|H-WK^*\|^2+\sigma\mathfrak C(W,K^*)
                   +\sigma(1-\|W\|^2)\|K\|^2 .
 \end{split}
 \tag{8}
\]
For (8), the real cross term in the square is the required one
by conjugation and cyclicity of trace.

Every SOS term in (6)--(8) is linear over the reals in the variations
and at most linear in packet coordinates before squaring.
The matrices containing adjoints need not belong to \(\mathcal A_N\).
Their entries are still permitted polynomials in its prescribed
coordinates. Neither adjoint closure of this algebra nor a small
Hilbert--Schmidt coefficient norm of multiplication is assumed.

For a constant linear map \(T\) with \(\|T\|_{\rm op}\le\sigma\),
the corresponding mixed-term completion uses the positive matrix
\(\sigma I-\sigma^{-1}T^*T\). This is a constant quadratic SOS.
It applies to the actual turn.

## 3. The Hessian certificate

Let \(h\) be a real variation, written in complex packet coordinates,
and put \(A(x)=D\Phi(x)\). Direct differentiation gives
\[
 \begin{split}
 \tfrac12D^2E(x)[h,h]
 ={}&\|h\|^2-2\operatorname{Re}\sum_v
               \langle h_v,D\Phi_v(x)h\rangle
                   +\|A(x)h\|^2+|Lh_{\rm top}|^2\\
 &+\sum_{\rm products}
 \{2\operatorname{Re}\langle\sigma x_Lx_R,\sigma h_Lh_R\rangle
                  -2\operatorname{Re}\langle x_v,\sigma h_Lh_R\rangle\}.
 \end{split}
 \tag{9}
\]
Apply (6) to the two derivative terms at a product, and the linear
version at a turn. A packet receives at most \(2\sigma\|h_v\|^2\)
from its own two-input row and at most \(\sigma\|h_v\|^2\) from
its one parent. Thus \(3\sigma\|h\|^2\) pays all these terms.
Equations (7) and (8) pay the last line with
\((\sigma^2+\sigma)\|h\|^2\): distinct sibling pairs are disjoint.
All unused allowances and the last two squares in the first line
are SOS. Therefore
\[
 \tfrac12D^2E(x)[h,h]-(1-4\sigma-\sigma^2)\|h\|^2
             =S(x,h)+\sum_vg_v(x)h^{\mathsf T}C_vh ,
 \tag{10}
\]
where \(S\) is SOS, linear in \(h\) and at most linear in \(x\)
before squaring, and the real matrices \(C_v\) are constant PSD.
Since \(1-4\sigma-\sigma^2=191/256>1/2\), this yields
\[
 D^2E(x)[h,h]-\|h\|^2
       =\sum_\nu|W_\nu(x)h|^2+\sum_vg_v(x)h^{\mathsf T}V_vh ,
 \tag{11}
\]
with affine real matrix polynomials \(W_\nu\) and constant
\(V_v\succeq0\). This is the same Hessian-module structure as in
the [earlier certificate](research_conway_degree_four_semidefinite_certificate.md),
now proved for constant-budget physical multiplication.

## 4. Integration and the exact finite problem

Fix any \(u\in\mathcal D\), put \(h=x-u\), and integrate (11) along
\(x_t=u+th\) with weight \(1-t\). Taylor's formula gives
\[
 E(x)-E(u)-\nabla E(u)\cdot(x-u)-\tfrac12\|x-u\|^2
                                                    \in Q_2(g).
 \tag{12}
\]
Here is the degree check. Integrating the positive Gram matrix of
each \(W_\nu(x_t)h\) gives SOS of quadratics in \(x\).
For a ball term use
\[
 g_v(x_t)=(1-t)g_v(u)+tg_v(x)+t(1-t)\|h_v\|^2 .
 \]
Its integral is exactly
\[
 \tfrac13g_v(u)h^{\mathsf T}V_vh
 +\tfrac16g_v(x)h^{\mathsf T}V_vh
 +\tfrac1{12}\|h_v\|^2h^{\mathsf T}V_vh .
 \tag{13}
\]
The first and third terms are SOS and the middle term is an
original ball constraint times SOS of linear polynomials.
No degree increase beyond four occurs.

At the interior minimizer, stationarity in (12) gives
\[
 E-e_*-\tfrac12\|x-a_*\|^2\in Q_2(g),\qquad E-e_*\in Q_2(g).
 \tag{14}
\]
It follows, with attainment, that
\[
 e_*=\max\{\lambda:E-\lambda\in Q_2(g)\}
     =\min_{\mathcal L}\mathcal L(E).
 \tag{15}
\]
The second minimum ranges over degree-four functionals satisfying
\(\mathcal L(1)=1\), \(\mathcal L(p^2)\ge0\) for \(\deg p\le2\),
and \(\mathcal L(g_vp^2)\ge0\) for \(\deg p\le1\).
Nonnegativity on \(\mathcal D\) and (14) prove the SOS equality and
its attainment. For every feasible \(\mathcal L\), (14) gives
\(\mathcal L(E)\ge e_*\); evaluation at \(a_*\) attains equality.
These are the usual order-two moment and localizing PSD matrices.
Their coefficients use only the known physical objective and balls.
The minimizer is used to prove existence, not supplied to the SDP.

There is also a directly computable certificate at a fixed trial \(u\):
put \(d(u)=E(u)-\|\nabla E(u)\|^2/2\). Adding
\(\|x-u+\nabla E(u)\|^2/2\) to (12) gives
\[
                 E(x)-d(u)\in Q_2(g),\qquad
                 B_{\rm ph}^2\max(0,d(u))\le |K_N|^2 .
 \tag{16}
\]
Here \(d(u)\) is a number with \(u\) fixed; it is not asserted to
be a quartic polynomial when the trial itself varies.

The SDP degree is fixed, while its matrix sizes and the precision
needed for a small optimum still grow with \(N\).
A geometric family of positive lower certificates with the required
volume rate is not constructed. No new filling class follows.
No binomial-head estimate or semisimple quotient is used.

## Complete proof sources

The two entire matching proof sources were read:

| Source | SHA-256 |
|---|---|
| [Uniform physical source and constant budgets](research_conway_uniform_physical_quartic.md) | 39895b430535f565d30133b46ef57f67589207bc83f40597ffe96e2ce79bbda8 |
| [Original Hessian certificate and Taylor integration](research_conway_degree_four_semidefinite_certificate.md) | 8b706c7e08aa124ce5d80c2401511a3be67a09b1878b0adfd4ec989514cf44db |

The matrix-specific identities (5)--(8) and their use above are proved
inline. General Gram-matrix and moment terminology has the coverage
recorded in the earlier certificate; none of those external theorems
is needed for the proof here. Only written mathematics and text/hash
operations were used. No mathematical program, test, build, git
operation, or earlier-final edit was performed.
