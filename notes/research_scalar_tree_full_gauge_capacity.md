# A positive variational formula for an actual source on a tree

20 November 2026. Research note; the public manuscripts remain frozen.

A scalar contraction on a tree is the infimum of a product of positive
local norms, after allowing full matrix changes of basis on its internal
edges. The same statement holds for the norm of a vector-valued output.
There is no replacement of the original closing functional in this
formula. That functional is one of the tensors being optimized.

The infimum is generally approached by increasingly singular changes of
basis. Existence of the formula therefore gives neither a geometric
minimizer nor a volume asymptotic. A second result gives a useful way to
certify near optimality: on a fixed tree, matching the full reduced density
matrices across every edge approximately forces the contraction norm to
be close to the product of the local norms. The estimate is independent
of the dimensions of the edge spaces. Matching only their diagonal
entries is insufficient.

These facts apply to the complete Conway compiler. They also apply
directly to the actual all-main-color energy, by treating multiplication
of the original physical braid operators as a tree of linear maps.
The latter application retains the main-color cap projector and does not
identify that energy with an auxiliary-color or unfilled covariance norm.

## 1. Tensors, pairings, and the permitted gauges

Let \(\mathcal T\) be a finite connected tree, with vertex set \(V\)
and internal edge set \(E\). At each edge \(e\), fix a finite-dimensional
complex coordinate space \(H_e\), with its Euclidean Hermitian norm.
Choose one endpoint as its positive end. A tensor at that end has an
\(H_e\) factor; the tensor at the other end has an \(H_e^*\) factor.
The edge contraction is the complex bilinear evaluation pairing.

One distinguished vertex may also have an uncontracted output in a
finite-dimensional Hilbert space \(F\). All other tensor factors are
contracted along the tree. Denote the resulting output by
\[
                         Y=\operatorname{Contr}(T_v:v\in V)\in F.
\tag{1}
\]
The scalar case is \(F=\mathbb C\). Each local tensor has its ordinary
coefficient Hilbert--Schmidt norm, denoted by \(\|T_v\|\). The dual
coordinate factors have the corresponding Euclidean norm.

An edge gauge is an invertible matrix \(g_e\in\mathrm{GL}(H_e)\).
It acts by \(g_e\) at the positive end and by \(g_e^{-\mathsf T}\)
at the negative end. These two actions preserve the bilinear evaluation.
Consequently the gauged tensors \(T_v(g)\) have exactly the same output
\(Y\), with its complex phases. Define
\[
 \mathcal C(T)=\inf_{g_e\in\mathrm{GL}(H_e)}
                          \prod_{v\in V}\|T_v(g)\|.
\tag{2}
\]
Every matrix and norm in this definition is specified before the output
is evaluated. No factor contains a division by \(Y\).

The original source must be included among the tensors. For example,
a linear closing row is a one-leg tensor at the root. Leaving it out
and optimizing an open network is a different problem. A retained
external scalar can be put into that root tensor or kept as its known
absolute multiplier.

## 2. The exact variational identity

**Theorem 1.** For every network in Section 1, including a zero output,
\[
                              \boxed{\mathcal C(T)=\|Y\|.}
\tag{3}
\]
There is no dimension factor in (3).

**Proof.** Contracting a leaf vector into its neighbor has operator norm
at most the norm of that vector. Repeated Cauchy--Schwarz along the tree
therefore gives
\[
                           \|Y\|\le\prod_v\|T_v(g)\|
\tag{4}
\]
for every gauge. This proves one inequality in (3). The bilinear
functional associated with a vector has the same Euclidean norm as
that vector; complex conjugation in its Riesz vector changes no norm.
In particular no norm of an unnormalized Bell vector is inserted in (4).

For the reverse inequality, use induction on the number of vertices.
For one vertex, its tensor is precisely the output, and the assertion
is immediate. Otherwise choose a leaf different from the output vertex.
If its vector is zero, every product in (2) and the output are zero.
Suppose its vector is nonzero. By interchanging the two edge conventions
if necessary, regard it as a vector \(a\in H_e\). Choose an invertible
edge gauge sending \(a\) to the first unit vector \(e_0\).
Write the transformed neighboring tensor as
\[
                           \sum_i e_i^*\otimes A_i.
\]
The remaining factors in \(A_i\) can include the output space \(F\).
The reduced tree obtained by contracting the leaf has neighboring
tensor \(A_0\), and its output is still \(Y\).

Apply the further gauge \(D_t=\operatorname{diag}(1,t,\ldots,t)\)
at the leaf end of this edge, with \(t\to+\infty\). The leaf remains
\(e_0\), of norm one; its neighbor becomes
\[
                 e_0^*\otimes A_0+t^{-1}\sum_{i>0}e_i^*\otimes A_i.
\]
Its norm tends to \(\|A_0\|\). Fix any gauges on the other edges
before taking this limit. Their actions commute with this edge action,
so the limiting product is exactly the corresponding product for the
reduced tree. Taking its infimum proves
\(\mathcal C(T)\le\mathcal C(T_{\rm reduced})\).
Induction and (4) give (3). If \(A_0=0\), the same limit gives zero;
thus this argument also covers a zero output without a continuity
assumption on the infimum. \(\square\)

This proof is an exact contraction argument, rather than an assertion
that a metric chosen from the unknown answer exists. It also explains
why unbounded condition numbers are permitted in (2). The diagonal
matrices \(D_t\) used in the proof become singular in the limit.

The tree hypothesis concerns the contraction graph used in this theorem.
A physical diagram with cycles may be compiled into a tree by bundling
all live indices into a larger matrix index. The resulting gauge acts
on that whole bundled space. It is not then a product of gauges on the
original individual physical wires.

## 3. Positive matrices and geodesic convexity

Full complex gauges can be replaced by positive Hermitian matrices.
Indeed write \(g_e=U_eP_e\), where \(U_e\) is unitary and \(P_e>0\).
At the two ends, the actions are
\[
                    U_eP_e,\qquad \overline U_eP_e^{-\mathsf T}.
\]
The two unitary factors do not change their local tensor norms.
Removing all of them shows that positive gauges have the same infimum.

It is convenient to use \(H_e=P_e^2=g_e^*g_e>0\) as variable. The
squared local norm is
\[
 \|T_v\|_H^2=
 \left\langle T_v,
 \left(\bigotimes_{e\text{ positive at }v}H_e\right)
 \otimes
 \left(\bigotimes_{e\text{ negative at }v}\overline H_e^{-1}\right)
 \otimes I_F\,T_v\right\rangle.
\tag{5}
\]
The \(I_F\) factor is present only at the output vertex. Assume for
this paragraph that each local tensor is nonzero. The objective is
\[
                           L(H)=\sum_v\log\|T_v\|_H.
\tag{6}
\]

**Proposition 2.** The function (6) is convex along simultaneous
positive-matrix geodesics
\[
 H_e(t)=H_e(0)^{1/2}\exp(tX_e)H_e(0)^{1/2},
                            \qquad X_e=X_e^*.
\tag{7}
\]

**Proof.** In (5), pull the fixed factors \(H_e(0)^{1/2}\), or their
conjugate inverses, into the tensor. Diagonalize each Hermitian \(X_e\).
On a negative end the corresponding generator is
\(-\overline X_e\). The remaining tensor factors act on different
legs and commute. Thus the squared norm at a vertex has the form
\[
                             \sum_\alpha c_\alpha e^{t\ell_\alpha},
                    \qquad c_\alpha\ge0,
\]
with real \(\ell_\alpha\). The second derivative of its logarithm is
the variance of these real numbers for their normalized positive
weights. It is nonnegative. Sum the resulting convex functions and
divide by two. \(\square\)

Convexity does not assert attainment. Even when \(Y\ne0\), the
minimizing matrices can escape to infinity in the positive cone.
Restricting (2) to diagonal gauges, prescribed tensor-product gauges,
or a bounded condition number generally gives only an upper bound
on \(\|Y\|\).

## 4. A dimension-independent certificate from full edge marginals

There is a local condition which certifies that a specified set of
gauges is already close to the infimum. It uses full reduced density
matrices, including their off-diagonal entries.

Fix gauges and suppose all gauged local tensors are nonzero. Normalize
them to unit vectors \(\tau_v=T_v(g)/\|T_v(g)\|\). For an internal
edge, let \(\rho_{v,e}\) be the reduced density matrix of \(\tau_v\)
on that coordinate factor; trace over all its other factors, including
\(F\) when appropriate. Each density matrix is positive with trace one.
Because the contraction is bilinear, the two endpoint matrices are
compared with a transpose:
\[
             \delta_e=\|\rho_{v,e}-\rho_{w,e}^{\mathsf T}\|_1,
                    \qquad \delta=\max_e\delta_e.
\tag{8}
\]
Here \(\|\cdot\|_1\) is the trace norm. Transposition leaves this
norm unchanged, so (8) is independent of the chosen endpoint order.

**Theorem 3.** Let \(m=|V|\ge2\), put
\(S=\sum_{e\in E}\delta_e\), and write \([a]_+=\max(a,0)\). Then
\[
 \boxed{\quad
 \frac{\|Y\|}{\prod_v\|T_v(g)\|}
                  \ge[1-4m\sqrt S-5mS]_+.
 \quad}
\tag{9}
\]
The estimate has no dependence on any edge dimension.

**Proof.** Work first with the normalized local tensors. For a density
matrix put \(L(\rho)=1-\operatorname{tr}(\rho^2)\). Two elementary
properties control the errors without a dependence on tree depth.
For a bipartite density matrix,
\[
                         L(\rho_{AB})\le L(\rho_A)+L(\rho_B).
\tag{10}
\]
Indeed the commuting swaps \(F_A,F_B\) on two copies satisfy
\((I-F_A)(I-F_B)\ge0\). Taking its trace against
\(\rho_{AB}\otimes\rho_{AB}\) gives (10). Also
\[
 |L(\rho)-L(\sigma)|
 \le\|\rho-\sigma\|_1\|\rho+\sigma\|_{\rm op}
 \le2\|\rho-\sigma\|_1.
\tag{11}
\]

Orient the tree toward its output vertex. A nonroot vertex tensor is
pure on its parent leg and all its child legs together. Their two
reduced density matrices have the same nonzero eigenvalues, by the
singular-value decomposition. Its parent-leg linear entropy is therefore
at most the sum of its child-leg linear entropies, by repeated use of
(10). At a leaf that entropy is zero. Across each edge, (11) costs at
most \(2\delta_e\). Induction from the leaves shows that the linear
entropy on every half-edge is at most \(2S\). The output space at
the root causes no change: the root is not used for a parent-leg
induction.

Choose a top unit eigenvector \(a_{v,e}\) of each half-edge density
matrix, and let \(\eta_{v,e}=1-\lambda_{\max}(\rho_{v,e})\).
Since \(\operatorname{tr}\rho^2\le\lambda_{\max}(\rho)\),
\(\eta_{v,e}\le2S\). The tensor product of these rank-one
projectors at a vertex has probability
\[
                     p_v\ge1-\sum_{e\ni v}\eta_{v,e}
                          \ge1-2\deg(v)S.
\tag{12}
\]
The projectors act on different legs and commute, so this is the
elementary union bound for their complementary projections.

Suppose temporarily that \(S<1/(16m^2)\), so every \(p_v\) is
positive. Normalize the projected vertex tensor, and call the result
\(\varphi_v\). At a nonroot it is a product of its chosen half-edge
vectors, with the scalar phase fixed by the projection of \(\tau_v\).
At the root it is their product tensored with a unit output vector
in \(F\), again with that phase retained. Consequently
\[
 \|\tau_v-\varphi_v\|^2=2-2\sqrt{p_v}
                  \le2(1-p_v)\le4\deg(v)S.
\tag{13}
\]

The vectors at the ends of an edge are nearly paired. Write
\(\rho=\rho_{v,e}\), \(\sigma=\rho_{w,e}^{\mathsf T}\), and let
\(P,Q\) be their top rank-one eigenprojections. A trace-zero Hermitian
matrix tested against a projection has absolute trace at most half
its trace norm; its positive and negative parts have equal trace.
Hence
\[
 1-\eta_{v,e}-\delta_e/2\le\operatorname{tr}(P\sigma)
                       \le\operatorname{tr}(PQ)+\eta_{w,e}.
\]
The last inequality splits \(\sigma\) into its top eigenspace and
its positive remainder of trace \(\eta_{w,e}\). The bilinear edge
overlap \(t_e=|a_{v,e}^{\mathsf T}a_{w,e}|\) therefore satisfies
\[
                              t_e^2\ge1-\tfrac92 S.
\tag{14}
\]
The product network \((\varphi_v)\) has output norm \(\prod_e t_e\),
at least \(1-\tfrac92(m-1)S\): use \(\sqrt{1-a}\ge1-a\)
and multiply the resulting bounds. The tree Cauchy estimate (4) and
a multilinear telescoping sum give
\[
 \begin{split}
 \|\operatorname{Contr}(\tau_v)\|
 &\ge1-\tfrac92(m-1)S-\sum_v\|\tau_v-\varphi_v\|\\
 &\ge1-\tfrac92(m-1)S-2\sqrt{2m(m-1)S}.
 \end{split}
\tag{15}
\]
Here \(\sum_v\deg(v)=2(m-1)\) and Cauchy--Schwarz were used.
This proves the weaker lower bound (9) when \(S<1/(16m^2)\).
If \(S\ge1/(16m^2)\), its bracket is nonpositive, so (9) follows
from nonnegativity of a norm. Restoring the local norms proves the
assertion. \(\square\)

In particular, for a fixed tree and a sequence of levels, the condition
\(\delta_N\to0\) implies
\[
                \frac{\|Y_N\|}{\prod_v\|T_{v,N}(g_N)\|}\longrightarrow1.
\tag{16}
\]
This criterion involves only local tensors, their prescribed gauges,
and their reduced density matrices. It does not assume a lower bound
for the unknown output. It also handles growing trees: since
\(S\le(m-1)\delta\), the condition \(\delta=o(m^{-3})\)
suffices for the ratio in (16) to tend to one. No optimal numerical
constants or dependence on \(m\) are claimed.

The same matrices are the full gauge derivative. Vary one edge gauge
by \(g_e(s)=e^{sX}g_e\), with \(X=X^*\). Direct differentiation gives
\[
 \left.\frac{d}{ds}\right|_{s=0}\sum_v\log\|T_v(g(s))\|
        =\operatorname{tr}X
                    (\rho_{v,e}-\rho_{w,e}^{\mathsf T}).
\tag{17}
\]
Exact full matrix balance is therefore the stationary condition. On
a tree it saturates (4). A pure leaf marginal then forces its neighbor
to factor across that edge; removing it propagates this factorization.
Thus a finite exactly balanced gauge is a restrictive condition. The
limits used in Theorem 1 need not provide such a finite gauge.

Diagonal or classical moment balance is weaker. On a single edge,
the unit vectors \((1,1)/\sqrt2\) and \((1,-1)/\sqrt2\) have the same
diagonal probabilities but zero bilinear pairing. Their full density
matrices, compared as in (8), differ. Theorem 3 cannot be invoked after
discarding that difference.

## 5. The actual Conway source and the actual main-color energy

The complete Conway compiler in
[Orthogonal boundary packets under Conway composition](research_conway_full_boundary_quotient_gram.md)
uses the full Newton boundary space, the actual multiplication tensor,
the actual turn, arbitrary full leaf packets, and the original closing
row. Its expression graph, with that row included, is a tree of the
kind above. Theorem 1 therefore gives an exact positive variational
formula for its original scalar. All repeated-root derivative channels
and the original leaf phases remain in the tensors.

There is also a direct application to the whole main-color energy,
without using a complete-color Conway space for ordinary main colors.
Fix a braid on \(b\) strands and use the original \(N\)-dimensional
physical modules at each of its \(N\) main-color orbit points. Set
\[
                 A_N=\bigoplus_{j=1}^N\operatorname{End}(V_{j,N}^{\otimes b}),
                    \qquad \dim A_N=N^{2b+1}.
\tag{18}
\]
Equip this space with its coordinate Hilbert--Schmidt norm. Each signed
crossing of the fixed word supplies one known vector in \(A_N\).
Componentwise matrix multiplication supplies a fixed bilinear tensor.
Compile the word as any finite multiplication tree. Its output is the
tuple of the original physical braid operators.

At the root use the explicit linear map which takes the prescribed
\((0,0)\) partial pivotal trace in each color, with its zero-framing
factor. Thus the uncontracted output is exactly
\[
                              Y_N=(c_1,\ldots,c_N).
\tag{19}
\]
The map is given by the original pivot matrices and selected cut entry;
it is not defined from the evaluated numbers \(c_j\). The
[main-color cap-projection theorem](research_main_color_cap_projection_energy.md)
proves, with precisely these original conventions,
\[
 \|Y_N\|^2=E_N=|K_N|^2+R_N,
                  \qquad 0\le R_N\le(N-1)(N/2)^{2b-2}.
\tag{20}
\]
In particular all the cap coherence in that theorem remains inside
the root tensor in the present construction. It has not been replaced
by an independent product window or an identity projector.

For this concrete tree, Theorem 1 says
\[
 \boxed{\quad
 \frac{\pi}{N}\log E_N
 =\inf_{H_e>0}\frac{2\pi}{N}
                              \sum_v\log\|T_{v,N}\|_H.
 \quad}
\tag{21}
\]
The left side is finite: the ordinary trivial main color is one.
The internal gauges in (21) are full matrices on the bundled space
(18). The claim does not make the original physical crossing diagram
acyclic, or make these gauges tensor products of single-wire metrics.

The diagonal physical-gauge hierarchy in
[the weighted plat-energy note](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_weighted_fourier_plat_energy.md)
is a useful restricted upper-bound problem. The equality here uses
the full edge matrix gauges of a compiled tree. Restricting those
gauges again would require a separate argument for equality.

## 6. A concrete geometric certificate and the remaining theorem

Suppose the original knot is hyperbolic and its complement volume is
\(V>0\). A sufficient certificate for its volume identity is now:

1. Specify positive full edge metrics for the actual tree in (18)--(19),
   independently of the unknown output.
2. Prove that their full marginal defects (8) tend to zero.
3. Prove that their local norm objective tends to the geometric value:
   \[
        \frac{2\pi}{N}\sum_v\log\|T_{v,N}\|_{H_N}\longrightarrow V.
   \]

Equivalently, if
\(F_N=\prod_v\|T_{v,N}\|_{H_N}
      =\exp(NV/(2\pi)+o(N))\)
and \(S_N=\sum_e\delta_{e,N}\to0\) for this fixed tree, Theorem 3
gives (16). These statements imply
\(\pi N^{-1}\log E_N\to V\). The polynomial remainder in (20)
then gives the original Kashaev volume identity. Eventual nonvanishing
is a consequence, rather than a premise.

This replaces a global closing-angle estimate by a local full-matrix
balance certificate. It does not show that the classical angle equations
already provide that certificate. Their scalar or diagonal balance must
still be connected to the full matrices in (8), including their phases.
The local Gaussian covariance of actual crossing kernels is one possible
input to such a construction; no such global construction is proved here.

Nor may an infimum and a large-level limit simply be interchanged in
(21). Candidate geometric metrics give upper bounds on the infimum.
Theorem 3 supplies a lower comparison only when their full defects are
controlled. Unknown escaping metric sequences are otherwise still allowed.

For the finite-exception problem, the certificate would have to survive
every required fixed short partial filling. Its constants can depend on
that fixed partial assignment; the filling coefficients remain fixed
before \(N\) tends to infinity. One must prove the certificate for all
sufficiently long remaining assignments that give hyperbolic knots, and
repeat it on the finitely many short-coordinate branches. Theorem 1 is
valid on every such branch, but does not supply its geometric metrics.
Exact reductions which leave a fixed hyperbolic core in an infinite
assignment fiber still require a volume proof for that core. The
variational reformulation does not remove that obligation.

## Direct texts and proof scope

The linear-algebra proofs above are self-contained. The following complete
texts were read for the actual-source applications and comparison with
the existing gauge construction:

| Direct text | SHA-256 |
|---|---|
| [Complete Conway compiler](research_conway_full_boundary_quotient_gram.md) | `debe56dbad8151b90d44d0fccbf0dcf33dafb780370e01c8acdadbd2939dc077` |
| [Actual main-color cap projection](research_main_color_cap_projection_energy.md) | `79856f4581e099a1e8a16cdd76ab4578377070e2b3dbaa1a7bed1d5dbb358968` |
| [Weighted physical-source gauges](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_weighted_fourier_plat_energy.md) | `69757cb8ab3b857b690d9da8d3d7a46e4a42df4f0ab47a6bb85816aa9efc38b2` |

No mathematical program, numerical test, build, git operation, or public
document change was used. The capacity identity is elementary tensor
linear algebra, not a novelty claim about general tensor scaling. Its
purpose here is an exact formulation for the original source and the
dimension-independent full-marginal certificate, with the remaining
geometric construction stated explicitly.
