# A relative asymptotic for the original undamped reciprocal source

24 November 2026. Research proof. Earlier finals and manuscripts are unchanged.

The original physical reciprocal integral has relative error tending to
zero, without damping its closing row or changing its budgets. The
additional input is specific to the original source: either closing
after a product has bilinear norm at most \(1/N\). This bounds every
nonlinear residual coefficient more strongly than the generic
bilinear budget does. Fixed leaf degree then controls its Gaussian
moments and the full reciprocal integral.

The antichain expansion and its orthogonality were already available
in [O]. The reciprocal construction and the shrinking physical closing
row were established in [U]. The result below combines these with the
source-specific coefficient estimate, not a geometric evaluation of
the integral or a lower bound for the knot scalar.

## 1. Original physical source and statement

Use the full \(N\)-dimensional physical algebra
\(\mathcal A_N=\mathbb C[\Omega]\), with the inherited matrix
Hilbert--Schmidt norm of [P,H], at every \(N\ge2\).
All double-root derivative directions remain independent.
Fix a literal normalized Conway expression tree \(\mathscr T\),
with \(s\) proper vertices and \(L\ge1\) prescribed leaf occurrences.
Its only internal maps are the actual product and genuine turn,
with exactly [P]'s constant structural budgets \(16\).
Prescribed leaf budgets and the original root budget are also
unchanged. Write their product as \(\mathcal B_N\).

Let \(\Phi_v\) denote the normalized maps, \(c_N\) the original
normalized closing row, and \(D=Ns\). Set
\[
 G_v(x)=\Phi_v((x_j)_{j\ {\rm child\ of}\ v})-x_v,\qquad
 E_N(x)=\|G(x)\|^2+|c_Nx|^2,\qquad
 \mathcal P_N=\frac{D!}{\pi^D}\int_{\mathbb C^D}E_N(x)^{-D-1}\,dx .
 \tag{1}
\]
The integral is extended and nonnegative. Its base is the original
degree-at-most-four objective, with the same full matrices, phases,
turns, mark, framing and external source factors.

The inverse \(H=G^{-1}\) is the triangular polynomial recursion
\[
 H(r)_v=\Phi_v((H(r)_j)_j)-r_v,\qquad
 |\det_{\mathbb R}DH|=1 .
 \tag{2}
\]
Put
\[
 f(r)=c_NH(r)=k+dr+p(r),\qquad
 k=f(0)=K_N/\mathcal B_N,\quad d=Df(0),\quad p(0)=Dp(0)=0 .
 \tag{3}
\]
The true forward field and \(k\) are used only in the proof.
Neither is input to (1).
The actual physical estimates of [U] give, uniformly over all
normalized leaf choices,
\[
                  |k|^2\le N^{-1},\qquad \|d\|^2\le C/N ,
 \tag{4}
\]
with an absolute constant \(C\). The stronger displayed constants
in [U] are unnecessary here.

Define
\[
 \rho_L(N)=
 \begin{cases}
 0,&L=1,\\
 N^{-1},&L=2,\\
 N^{-1}\log(2N),&L=3,\\
 N^{-2/(L-1)},&L\ge4 .
 \end{cases}                                                \tag{5}
\]
**Theorem.** There are constants \(C_{\mathscr T},N_{\mathscr T}\),
independent of the actual normalized leaf packets and their phases,
such that every nonzero original source satisfies
\[
 \boxed{\qquad
       \bigl||k|^2\mathcal P_N-1\bigr|
                           \le C_{\mathscr T}\rho_L(N)
                    \quad(N\ge N_{\mathscr T}).
 \qquad}                                                     \tag{6}
\]
If \(L=1\), the equality \(|k|^2\mathcal P_N=1\) is exact.
At \(K_N=0\), \(\mathcal P_N=+\infty\), as in [U].
The theorem has no parity restriction or prior lower bound on
\(|K_N|\). It is uniform for arbitrary prescribed short-filled
leaf packets in the fixed literal tree.

For nonzero sources, (6) gives the same relative comparison between
\(|K_N|^2\) and \(\mathcal B_N^2/\mathcal P_N\), with error
\(C_{\mathscr T}\rho_L(N)=o(1)\).
No additional normalization factor is restored.

## 2. The two physical closing forms after a product

The original rows of [P,H] satisfy
\[
 \lambda_0(AB)=\lambda_0(A)\lambda_0(B),\qquad
 \|\lambda_0\|_*\le(2N)^{-1/2},\qquad
 \phi(AB)=\frac1N\operatorname{Tr}[(I\otimes g)AB],
 \tag{7}
\]
where \(g\) is the actual unitary pivot. The first identity is
evaluation at the physical Casimir node \(q+q^{-1}\), on the full
algebra, including its derivative directions.
The row bound is proved in [U, Section 2] from the actual pair
characteristic polynomial and multiplicity \(2N\).
The trace identity is [H, (11)].
Matrix Cauchy--Schwarz therefore gives, for either
\(\lambda\in\{\lambda_0,\phi\}\),
\[
                   |\lambda(AB)|
                 \le \frac1N\|A\|_{\rm ph}\|B\|_{\rm ph}.
 \tag{8}
\]
For \(\lambda_0\), (7) in fact gives the constant \(1/(2N)\).
The genuine turn obeys
\(\lambda_0\mathcal T=\phi\), \(\phi\mathcal T=\lambda_0\).
Consequently any top unary corridor carries the original row to
a scalar of modulus at most one times one of these two rows.
Its residual terms are linear.

Thus the first binary gate below that corridor, if one exists,
is observed through the bilinear form (8), with all its normalized
scalar factors having modulus at most one. This is stronger than
estimating multiplication and the closing separately.

## 3. Complete antichain coefficients and their physical saving

An antichain \(A\) is a set of proper vertices with no member an
ancestor of another. The exact recursion (2) gives
\[
 f(r)=k+\sum_{A\ne\varnothing,\ A\ {\rm antichain}}
                  C_A((r_v)_{v\in A}) .
 \tag{9}
\]
Here \(C_A\) is complex multilinear in its \(|A|\) packet inputs;
the signs from the terms \(-r_v\) are included.
To obtain it, replace the subtrees at \(A\) by their free inputs
and evaluate every other branch with the actual normalized maps
and prescribed constants.
This is the antichain expansion already used in [O, (20)].
A choice of a residual stops its subtree, so an admissible set
contributes once. There is no repeated occurrence or hidden
combinatorial multiplicity.
Distinct literal child subtrees have disjoint variables.
An antichain has at most \(L\) members.

For every nonlinear term, with \(a=|A|\ge2\), we claim
\[
                         \|C_A\|_{\rm HS}^2\le N^{a-3}.
 \tag{10}
\]
All coefficient norms here use physical orthonormal packet bases.
After fixing some inputs of an antichain coefficient to unit
basis vectors, each remaining subtree linear slice has norm at
most one. This follows inductively from the normalized product
and turn bounds, and from the forward constants of norm at most
\(1/16\).

Consider the first binary gate below the top unary corridor.
Every nonlinear antichain lies below that gate. If it meets
both children, fix all but one free input in each child.
The resulting scalar bilinear form is (8) composed with two
linear contractions. Its operator norm is at most \(1/N\).
An \(N\)-by-\(N\) coefficient matrix with that operator norm has
squared Hilbert--Schmidt norm at most \(1/N\).
Summing over the \(N^{a-2}\) fixed input choices proves (10).

If the antichain lies in one child only, the other child supplies
its true forward constant, of norm at most one. Formula (8) then
gives a row of norm at most \(1/N\) on the active child.
Fix \(a-1\) inputs. The remaining row still has norm at most
\(1/N\). Summing its squared norm over \(N^{a-1}\) choices again
gives (10). This uses the actual signed constants before any norm;
it is not a positive replacement of the source.
If there is no binary gate, \(f\) is affine and \(p=0\).

## 4. Dimension-independent fixed Gaussian moments

Let \(Z=(Z_v)_v\) be standard complex Gaussian in \(\mathbb C^D\),
with density \(\pi^{-D}e^{-\|Z\|^2}\), in the physical coordinates.
Different antichain terms in (9) are orthogonal in \(L^2\):
a packet variable present in only one term is centered and independent.
For a single antichain,
\[
                 \mathbb E|C_A(Z_A)|^2=\|C_A\|_{\rm HS}^2 .
 \tag{11}
\]
Thus, for \(k\ne0\) and \(u>0\), put
\[
 q_u=dZ/\sqrt u,\qquad b_u=p(kZ/\sqrt u)/k .
 \tag{12}
\]
Equations (4), (9)--(11), and the fixed number of antichains give
\[
 \|q_u\|_{L^4}\le C N^{-1/2}u^{-1/2},\qquad
 \|b_u\|_{L^2}\le
       C_{\mathscr T}N^{-1}(u^{-1}+u^{-L/2}).
 \tag{13}
\]
Indeed the squared contribution of an antichain of size \(a\ge2\)
to the latter norm is at most
\(|k|^{2a-2}u^{-a}N^{a-3}\le N^{-2}u^{-a}\).

The same bound for \(b_u\) holds in \(L^4\), with a new
tree-dependent constant. Here is an elementary Wick justification,
without a dimension-dependent moment estimate.
Write a homogeneous holomorphic Gaussian polynomial of degree \(a\)
using its symmetric coefficient tensor \(T\). Pairing each Gaussian
coordinate with its conjugate gives
\[
 \mathbb E|F(Z)|^2=a!\|T\|^2,\qquad
 \mathbb E|F(Z)|^{2p}
     =(pa)!\|\operatorname{Sym}(T^{\otimes p})\|^2
     \le\frac{(pa)!}{(a!)^p}(\mathbb E|F(Z)|^2)^p .
 \tag{14}
\]
Symmetrization is an orthogonal projection and has norm one.
These identities also follow by expanding Gaussian monomials,
whose moments are \(\mathbb E|Z_i|^{2n}=n!\).
Take \(p=2\), and use the triangle inequality over the finitely
many antichains and degrees, all at most \(L\).
Together with (13) this proves, in particular,
\[
 \mathbb E|b_u|^4\le C_{\mathscr T}N^{-4}u^{-4}
                             \qquad(u\ge1).
 \tag{15}
\]
The linear fourth moment in (13) is the ordinary scalar Gaussian
moment with variance \(\|d\|^2/u\).

## 5. Exact Laplace identity and the three integration ranges

The Jacobian in (2) and Tonelli give the exact identity
\[
 \mathcal P_N=\int_0^\infty
          \mathbb E\exp\{-t|f(Z/\sqrt t)|^2\}\,dt .
 \tag{16}
\]
The scalar formula
\(\int_0^\infty t^D e^{-tE}dt=D!E^{-D-1}\)
fixes its normalization. All integrands are nonnegative.
Substitute \(u=t|k|^2\); rotational invariance of \(Z\) permits
replacing \(|k|Z\) by \(kZ\). Therefore
\[
 |k|^2\mathcal P_N
       =\int_0^\infty
          \mathbb E e^{-u|1+q_u+b_u|^2}\,du .
 \tag{17}
\]
The affine version with \(b_u=0\) integrates to exactly one by
[U, (15)], including its affine slope.

On \(0<u<\alpha\le1\), the difference of the two integrands
has integral at most \(\alpha\), since each lies in \([0,1]\).
On \(\alpha\le u\le1\), the global Lipschitz norm of
\(z\mapsto e^{-u|z|^2}\) is at most \(C\sqrt u\).
The \(L^2\) bound (13) consequently gives
\[
 \int_\alpha^1
 \mathbb E\left|e^{-u|1+q_u+b_u|^2}
                     -e^{-u|1+q_u|^2}\right|du
     \le\frac{C_{\mathscr T}}N
                    \int_\alpha^1u^{-(L-1)/2}\,du .
 \tag{18}
\]

For \(u\ge1\), split off the event
\(\{|q_u|>1/4\}\cup\{|b_u|>1/4\}\).
On its complement every segment \(1+q_u+\theta b_u\),
\(0\le\theta\le1\), has modulus at least \(1/2\).
Its exponential derivative is at most
\(C\sqrt u\,e^{-u/8}\).
The good-event difference is thus bounded by
\(C_{\mathscr T}N^{-1}u^{-1/2}e^{-u/8}\).
On the bad event use the bound one and the fourth moments:
\[
 \mathbb P(|q_u|>1/4)+\mathbb P(|b_u|>1/4)
       \le C_{\mathscr T}(N^{-2}u^{-2}+N^{-4}u^{-4}).
 \tag{19}
\]
Both terms are integrable. Hence the entire \(u\ge1\) difference
is \(O_{\mathscr T}(N^{-1})\).
No small-source tail cutoff or field-size hypothesis was used.

Combining the three ranges proves
\[
 \bigl||k|^2\mathcal P_N-1\bigr|
 \le \alpha+\frac{C_{\mathscr T}}N
                \int_\alpha^1u^{-(L-1)/2}\,du
                         +C_{\mathscr T}N^{-1}.
 \tag{20}
\]
For \(L=2,3\), take \(\alpha=N^{-1}\).
For \(L\ge4\), take \(\alpha=N^{-2/(L-1)}\).
Elementary integration gives exactly (5)--(6).
For \(L=1\), the affine identity is exact.
At \(k=0\) the already proved local radial divergence of [U]
gives \(\mathcal P_N=+\infty\); no division by zero is made above.

## 6. Scope and complete inputs

The theorem uses fixed leaf degree through the antichain expansion
and fixed Wick moments. The closing estimate (8) is essential:
a generic scalar polynomial with small separate operator bounds
does not supply the physical coefficient saving (10).
Neither smallness of a real minimizer nor a Hessian determinant
enters the argument.

This improves the universal constant-error undamped comparison
of [U] to a relative error tending to zero for the unchanged
quartic and budget. It does not evaluate \(\mathcal P_N\), remove
the signed source from its denominator, construct a geometric
trial field, or prove eventual nonvanishing. The arbitrary-short-
filling volume theorem and finite-exception assertion remain open.
No novelty is claimed for Gaussian moments or Laplace integration.

All four complete matching texts were read. Only written mathematics
and text/hash operations were used. No earlier final was edited.

| Label | Complete text | SHA-256 |
| --- | --- | --- |
| P, source, 477 lines | [Original uniform physical compiler](research_conway_uniform_physical_quartic.md) | 39895b430535f565d30133b46ef57f67589207bc83f40597ffe96e2ce79bbda8 |
| H, source, 331 lines | [Actual pair and original closing](actual_pair_casimir_commutant_and_rotated_trace.md) | 00ab946b3eddb61256bdbd8ec487789a15991a80e1a28b4eee53bbb4a00f7666 |
| U, source, 311 lines | [Undamped reciprocal source](research_conway_undamped_reciprocal_source.md) | 4ce9ae44a5ed6f7f54145d96712a7937f2e8c4181e2292aa5f2c44e84ffb3a8a |
| O, coverage, 407 lines | [Antichain expansion and orthogonal errors](research_orthogonal_error_positive_conway_recursion.md) | 5506f489642f2ec118c4fef25cccc0485fecdc32ffccf09c700ac923c9da98dd |
