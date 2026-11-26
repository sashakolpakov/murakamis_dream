# Bounds on the regularized source metrics and their penalty

20 November 2026. Research note; previous finals and public manuscripts
remain unchanged.

The regularized source problem has a unique positive matrix minimizer.
The earlier proof did not estimate its regularization penalty. Here we
bound that penalty and the spectra of the optimizing metrics using only
known input tensor norms and the ordinary trivial-color anchor. For a
fixed original braid, the logarithms of the optimizing eigenvalues are
of order at most the quantum level. The penalized minimum itself
therefore has the same leading rate as the actual main-color energy.

This is spectral control. It does not identify the optimizing
eigenvectors or matrix symbols with a hyperbolic angle structure.
That quantum to classical comparison remains necessary.

## 1. An explicit near-minimizer on an anchored tree

Let a finite tree have \(m\ge2\) vertices, edge spaces of dimensions
\(n_e\), and one vector output \(Y\). Use the bilinear contractions
and full edge gauges of
[the regularized source theorem](research_regularized_actual_source_capacity.md).
Assume the known anchor \(\|Y\|\ge1\). Put
\[
 B=\prod_v\max(1,\|T_v\|),\qquad D=\sum_e n_e,\qquad
 A_m(B,D,\eta)=\log(1+2D)
 +(2+2m(m-1))\log B+(m-1)\log\frac m{2\eta}.
\tag{1}
\]
Here \(0<\eta\le1\), the input norms are the original coordinate
norms, and the output vertex is the root. In particular \(B\ge1\)
and \(D\ge1\).

**Theorem 1.** There are full edge metrics, specified by finite
operations on the proper subtree messages, for which
\[
 0\le L(H)-\log\|Y\|\le\eta,\qquad
                   \log Z(H)\le A_m(B,D,\eta).
\tag{2}
\]
No choice in the construction divides by the output \(Y\).

**Proof.** Orient each edge toward the root, with its vector gauge
acting on the child side. Reversing an earlier edge convention replaces
\(H_e\) by \(\overline H_e^{-1}\), preserving both the local norms
and \(Z\), so this choice changes no variational value.
Let \(a_e\) be the ordinary contraction
of the proper subtree below that edge. It is a vector on that edge.
Tree Cauchy gives both
\[
                         B^{-1}\le\|a_e\|\le B.
\tag{3}
\]
The upper bound contracts the subtree. For the lower bound, leave
\(a_e\) uncontracted and apply tree Cauchy to the rest:
\(1\le\|Y\|\le B\|a_e\|\). In particular every such message
is nonzero, using only the known anchor.

Choose an edge gauge \(g_e\) sending \(a_e\) to the first unit
vector \(e_0\), with
\(\|g_e\|,\|g_e^{-1}\|\le B\). One construction first rotates
\(a_e/\|a_e\|\) to \(e_0\), then scales its first coordinate
by \(\|a_e\|^{-1}\). Applying all these gauges at once is
consistent: gauges cancel inside a contracted subtree. Therefore
each proper vertex tensor, when all its child indices are zero,
is exactly \(e_0\) on its parent edge. The corresponding root slice
is exactly \(Y\). All output-excited entries with zero child indices
vanish. The gauged norm of any local tensor is at most
\[
                    \|T_v\|B^{\deg(v)}\le B^m.
\tag{4}
\]

Let the root have depth zero. At an edge whose child has depth \(r\),
apply the further child-side gauge
\(D_e(t)=\operatorname{diag}(1,t^r,\ldots,t^r)\), with \(t\ge1\).
Its inverse transpose acts on the parent's input leg. An excited parent
output at a vertex of depth \(r\), together with \(k\ge1\) excited
child indices, receives exponent
\(r-k(r+1)\le-1\). Without an excited output, any excited child
also gives exponent at most \(-1\). The excluded case of an excited
output and no excited child was already zero. Leaves remain \(e_0\).
Thus every entry outside the zero-index slice is suppressed by at
least \(t^{-1}\).

These entries are orthogonal in the coordinate norm to the unchanged
zero-index slice. Its norm is one at a proper vertex and \(\|Y\|\ge1\)
at the root. By (4) and \(\log(1+x)\le x\),
\[
                  L(H(t))-\log\|Y\|
                        \le\frac{mB^{2m}}{2t^2}.
\tag{5}
\]
The complete edge gauge \(g_e(t)=D_e(t)g_e\) has
\[
 \|g_e(t)\|\le Bt^{m-1},\qquad
                         \|g_e(t)^{-1}\|\le B.
\]
Set \(H_e(t)=g_e(t)^*g_e(t)\). Removing the unitary factors of
these gauges preserves all local norms, as in the direct source.
The trace bound is
\[
 Z(H(t))\le1+2DB^2t^{2(m-1)}
                       \le(1+2D)B^2t^{2(m-1)}.
\tag{6}
\]
Take
\(t=B^m\sqrt{m/(2\eta)}\ge1\). Equations (5)--(6) give (2),
including exactly the constants in (1). \(\square\)

## 2. The penalty at the regularized minimum

Let \(H^{(\varepsilon)}\) minimize
\(J_\varepsilon=L+\varepsilon\log Z\), with \(0<\varepsilon\le1\).
Apply Theorem 1 with \(\eta=\varepsilon\). Since
\(L(H^{(\varepsilon)})\ge\log\|Y\|\), comparison with that explicit
competitor proves
\[
 \boxed{\quad
 \log Z(H^{(\varepsilon)})\le1+A_m(B,D,\varepsilon),
 \qquad
 0\le\min J_\varepsilon-\log\|Y\|
                \le\varepsilon[1+A_m(B,D,\varepsilon)].
 \quad}
\tag{7}
\]
In particular this is a bound for the actual penalty, rather than an
assumption that it disappears. Every optimizing eigenvalue satisfies
\[
 e^{-1-A_m(B,D,\varepsilon)}\le
       \lambda(H_e^{(\varepsilon)})
                         \le e^{1+A_m(B,D,\varepsilon)}.
\tag{8}
\]
Indeed each eigenvalue and its reciprocal are at most \(Z\).
The bounds use no nonvanishing of a selected scalar coefficient.

## 3. Coarse uniform bounds for the actual input matrices

For completeness the input growth needed below follows directly from
the original finite matrices. Let \(q=e^{\pi i/N}\),
\(Q=q^2\), \(\theta=\pi/N\), and
\[
 s_k=\prod_{r=1}^k2\sin(r\theta),\qquad 0\le k<N.
\]
The factorization of \((z^N-1)/(z-1)\) at \(z=1\) gives
\(s_{N-1}=N\). Reflection of the sine factors then gives
\[
 s_ks_{N-1-k}=N,\qquad
                        \frac1{s_k}\le\frac{2^{N-1-k}}N.
\tag{9}
\]
No asymptotic factorial estimate is needed.

At main color \(\alpha=j-1\), \(1\le j\le N\), the original
unrolled module in
[the ADO pointing note](kashaev_ado_pointing.md) has
\[
 E|a\rangle=[a]_q[\alpha-a+1]_q|a-1\rangle,
 \qquad F|a\rangle=|a+1\rangle,
 \qquad [r]_q=\frac{\sin(r\theta)}{\sin\theta}.
\]
Thus \(\|E^k\|\le(\sin\theta)^{-2k}\), and \(\|F^k\|\le1\).
The finite universal crossing in
[the original crossing definition](kashaev_crossing_and_period_lattice.md),
equation (2.1), is a unitary Cartan factor followed by the nilpotent sum
whose coefficient magnitudes are
\(|q-q^{-1}|^k/[k]_q!\). Consequently its \(k\)-th summand has
operator norm at most
\[
 \frac{(2\sin\theta)^k}{[k]_q!}(\sin\theta)^{-2k}
                         =\frac{4^k}{s_k}
                         \le\frac{2^{N-1+k}}N
                         \le\frac{4^{N-1}}N.
\tag{10}
\]
This estimate is uniform in the entire main-color orbit, including
the reducible colors.

The inverse nilpotent sum has coefficients
\((-1)^kq^{-k(k-1)/2}(q-q^{-1})^k/[k]_q!\), of the same magnitudes.
Multiplication with the positive sum gives coefficient zero in degree
\(1\le n<N\) by the finite binomial identity
\(\sum_{k=0}^n(-1)^kQ^{k(k-1)/2}{n\brack k}_Q=(1;Q)_n=0\).
Degree \(N\) and above vanish by nilpotence. The inverse Cartan
factor is unitary too. Each input pair has at most \(N\) possible
transfer indices. Thus the physical \(N^2\)-dimensional crossing has
at most \(N^3\) nonzero entries, each bounded by the last expression
in (10). Both signed crossings consequently obey
\[
                      \|R_\pm\|_{\rm HS}\le\sqrt N\,4^{N-1}.
\tag{11}
\]
Checked permutations, original pivots, and the root-of-unity
zero-framing scalars have unit modulus and add no exponential norm.

For the all-main-color compiler of a fixed braid on \(b\) strands,
tensoring with spectator identities and taking the direct sum over
the \(N\) main colors gives crossing leaf norm at most
\(N^{b/2}4^{N-1}\). Its componentwise matrix multiplication tensor
has \(N^{3b+1}\) unit entries and norm \(N^{(3b+1)/2}\).
Its original root readout has \(N\cdot N^{b-1}\) unit-modulus
entries and norm \(N^{b/2}\). Therefore, for that fixed compiler,
\[
                     \log B_N=O(N),\qquad \log D_N=O(\log N).
\tag{12}
\]
Constants may depend on the fixed word and width. Fixed signed powers
or fixed short pieces may be contracted first; submultiplicativity
gives the same type of bound. No estimate uniform in an unbounded
word length is asserted.

## 4. Spectral compactness and the full variational limit

Take the actual regularized minimizer with
\(\varepsilon_N=1/(m^2N^2)\). For a fixed completed knot assignment,
the number \(m\) is fixed. Equations (7)--(12) yield
\[
 \log Z(H_N)=O(N),\qquad
 \sup_e\|N^{-1}\log H_{e,N}\|_{\rm op}=O(1),
 \qquad \varepsilon_N\log Z(H_N)=O(N^{-1}).
\tag{13}
\]
Thus not only the unpenalized objective but also the entire penalized
minimum recovers the actual energy at that precision:
\[
       0\le\min_H J_{N,\varepsilon_N}(H)
                              -\tfrac12\log E_N=O(N^{-1}).
\tag{14}
\]
For any prescribed positive \(V\), this gives the equivalent target
\[
 \lim_N\frac{2\pi}{N}\log|K_N|=V
 \quad\Longleftrightarrow\quad
 \lim_N\frac{2\pi}{N}\min_HJ_{N,\varepsilon_N}(H)=V.
\tag{15}
\]
The ordinary-color remainder remains the one in the direct source.
No eventual nonvanishing of \(K_N\) is a premise.

The bounded spectra in (13) do not provide compactness of the
eigenvectors in a specified phase-space representation, convergence
of matrix symbols, or the Casson--Rivin functional as a limiting
objective. They also do not permit an unsupported interchange of an
infimum and a limit. Those are the next substantive requirements for
the geometric comparison in (15).

For a fixed short partial assignment, all statements apply to each
completed remaining integer assignment which gives a one-component
knot. The anchor is not asserted for an unfilled auxiliary link.
The algebraic and flow constructions now have controlled metric
spectra on every such completed fixed source. A uniform description
of their classical limits is still required to prove the requested
finite-exception theorem.

## 5. Main-color preserving gauges suffice at the leading scale

One exact restriction of the metric class is available. Suppose a tree
is a direct sum of \(r\) sectors: every local tensor has blocks
\(T_{v,j}\), and a contraction can pair only equal sector labels.
The root output is the orthogonal direct sum of vectors \(Y_j\).
Restrict the edge gauges to preserve the sectors, and denote the
resulting product-norm infimum by \(\mathcal C_{\rm block}\). Then
\[
 \boxed{\quad
 \mathcal C_{\rm block}
                  =\left(\sum_{j=1}^r\|Y_j\|^{2/m}\right)^{m/2}.
 \quad}
\tag{16}
\]

Here is a proof including sectors with zero output. At any finite
choice of sector gauges, let \(a_{v,j}\ge0\) be the local block norms.
Tree Cauchy in each sector and generalized Hölder give
\[
 \prod_v\left(\sum_j a_{v,j}^2\right)^{1/2}
 \ge\left(\sum_j\left(\prod_va_{v,j}\right)^{2/m}\right)^{m/2}
 \ge\left(\sum_j\|Y_j\|^{2/m}\right)^{m/2}.
\]
Conversely, first consider sectors with all local blocks nonzero. The
full tree capacity theorem, applied separately in each such sector,
gives gauges with products \(p_j=\prod_va_{v,j}\) approaching
\(\|Y_j\|\), including zero. Positive scalar edge gauges can make
every vertex norm in sector \(j\) equal \(p_j^{1/m}\): the required
logarithmic vertex rescalings sum to zero, and the incidence map of a
tree maps onto the zero-sum vertex vectors. To verify that last statement,
assign the required scalar at a leaf to its incident edge, remove the
leaf, and repeat. These scalar gauges change neither the sector output
nor its product of norms. The resulting whole product is
\((\sum_j p_j^{2/m})^{m/2}\). If a sector has a zero local block,
its output is zero. Scalar edge gauges can make all its nonzero vertex
norms tend to zero too: prescribe their target logarithmic rescalings,
let one zero vertex absorb the compensating sum, and again use the
incidence map. The zero block remains zero. Thus such sectors contribute
nothing in the limit. This proves (16) in every case without division
by a zero output.

If \(\mathcal C_{\rm full}=\|\bigoplus_jY_j\|\), the elementary
finite-dimensional norm inequalities give
\[
 \mathcal C_{\rm full}\le\mathcal C_{\rm block}
                      \le r^{(m-1)/2}\mathcal C_{\rm full}.
\tag{17}
\]
For the actual all-main-color tree, \(r=N\) and \(Y_j=c_j\).
For fixed \(m\), restricting the infimum to main-color preserving
gauges therefore changes its logarithm by at most
\((m-1)\log N/2\), which has zero volume rate.

This is a statement about infima. It does not assert that the canonical
regularized full-matrix minimizer is block diagonal, or that pinching
an arbitrary individual gauge improves the objective. The exceptional
complete color is still retained as its own sector. A continuous symbol
in the main-color parameter cannot erase it: the adjacent ordinary
colors and the complete color have different source behavior even
when their limiting meridians coincide.

## Complete direct sources

The complete texts below were read for the actual source, matrix
definitions, and the earlier regularized minimizer. The quantitative
normal form and its bounds (1)--(8), and the elementary matrix estimates
above, are proved here.

* [Regularized actual source](research_regularized_actual_source_capacity.md),
  SHA-256 `0cea0d52182eb24b4610538f354dbe5158fa54aa6f9cf7f9fc280c72ab090ff8`.
* [Original unrolled main-color family](kashaev_ado_pointing.md),
  SHA-256 `005ad157ebbf068b71eb80e2ceddc1aa9fccc460a54266756306e5cb54cf4c78`.
* [Finite universal crossing and original normalization](kashaev_crossing_and_period_lattice.md),
  SHA-256 `71e67223742fe905af47d0475435f3a13acc877695bd0cdc321798cf2e608037`.
* [Full tree capacity](research_scalar_tree_full_gauge_capacity.md),
  SHA-256 `2997b732aa73e063c66e81d6487a1d9927509609d61842c1dbb43d9345df1d6d`.

Only written mathematics and text/hash operations were used. No
mathematical program, numerical test, build, git operation, previous-final
edit, or public-document change was performed.
