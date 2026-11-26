# An unweighted quartic and orthogonal transport of the closing row

21 November 2026. Research note. Earlier final notes and the
public manuscripts remain unchanged.

The branching reduction can be used without its covariance matrices.
Keep the deterministic linear transfers and the original complex closing
row, and form an ordinary sum of squared recursion errors. This gives a
quartic on the same branching packets. Its minimum represents the
original squared invariant within the single factor
\(1+1/32512\), independently of the quantum level and tree size.

The comparison follows from an exact midpoint identity. When the closing
row is transported backward through the tree, successive generations
occupy disjoint packet spaces. Their squared norms therefore add.
No physical boundary channel is removed and no positive formula for the
invariant is assumed.

## 1. The smaller tree and its unweighted objective

Fix a level \(N\ge2\), and put \(\sigma=1/16\). Use the exact
deterministic chains in the branching-certificate note. Prescribed
leaf-to-product transports have already been inserted; no unknown
binary-subtree output is prescribed.

Let \(q\ge1\) count the original products having two internal inputs.
The reduced rooted tree has \(2q\) proper packet slots, \(q+1\)
constant proper gates, \(q-1\) bilinear proper gates, and one scalar
bilinear root. Each packet belongs to the complete positive Newton
space \(H_N\cong\mathbb C^N\), including its repeated-root directions.
Each packet is an input to exactly one parent. Write the proper maps
as \(f_i\), and the scalar root as \(g\).

These maps are computed by composing the known linear transfers along
the eliminated chains. In this note they are **not** multiplied by
inverse covariance square roots, and the scalar root is **not** divided
by its least-squares denominator. Their coefficient bounds are
\[
 \|f_i\|_{\rm HS}\le\sigma\quad\text{at a bilinear gate},\qquad
 \|f_i\|\le\sigma^3\quad\text{at a constant gate},\qquad
 \|g\|_{\rm HS}\le\sigma^2.
 \tag{1}
\]
All original phases and the complete original closing remain in these
maps. Let \(B=B_{\rm tot}>0\) be the unchanged product of the
original compiler budgets. If \(a\) is the actual forward packet
field on this smaller tree, then, literally,
\[
 a_i=f_i((a_j)_{j\text{ child of }i}),\qquad
                    k:=g(a)=K_N/B.
 \tag{2}
\]
The field \(a\) is feasible: induction from the constants using (1)
puts every packet in its unit ball. It is used in the proof, not supplied
as a coefficient of the new objective.

On the product \(\mathcal D\) of these unit balls define
\[
 G_i(w)=f_i((w_j)_{j\text{ child of }i})-w_i,\qquad
 U(w)=\sum_i\|G_i(w)\|^2+|g(w)|^2,\qquad
                    m_U=\min_{w\in\mathcal D}U(w).
 \tag{3}
\]
This is a known real polynomial of degree at most four in \(4Nq\)
real coordinates. Its coefficients need no covariance, inverse Gram
matrix or square root. It is an auxiliary objective with its own
source comparison, rather than an assertion that the earlier weighted
partial minimum has the same numerical value.

## 2. An exact midpoint formula for the source error

For any feasible \(w\), set \(b=(w+a)/2\), and let
\[
                 A=Df(b),\qquad c=Dg(b),\qquad S=I-A.
\]
These are complex-linear derivatives. Order the slots from the leaves
toward the root. Then \(A\) is strictly triangular, so \(S^{-1}\)
is a finite sum of powers of \(A\).

Every map here is constant or homogeneous bilinear. Its difference
between two fields is exactly its derivative at their midpoint applied
to their difference. In particular, with \(e=w-a\),
\[
                   G(w)=-Se,\qquad g(w)-k=ce.
\]
Consequently
\[
             \boxed{\quad k=g(w)+dG(w),\qquad
                              d=cS^{-1}.\quad}
 \tag{4}
\]
This equality retains the complex additions before any norm is taken.
The midpoint and row \(d\) need not be known to evaluate \(U\);
they give a uniform proof of its comparison with the original source.

## 3. Orthogonality between successive tree levels

Give each proper packet its distance from the scalar root. The row
\(c\) is supported on its two inputs, at distance one. The row
\(cA^j\) is supported at distance \(j+1\). A tree has one path
from the root to any packet, so these supports are disjoint for different
\(j\). They are orthogonal in the original direct-sum positive norm.
Thus
\[
                  \|d\|^2=\sum_{j\ge0}\|cA^j\|^2.
 \tag{5}
\]
The sum is finite. This orthogonality concerns packet slots at different
depths, not eigenvectors of a crossing operator.

The midpoint packets have norm at most one. At the scalar root, (1)
therefore gives \(\|c\|^2\le2\sigma^4\). A row arriving at a
proper bilinear gate splits into its two child rows; each has norm at
most \(\sigma\) times the arriving norm. Different gates have disjoint
child slots. Constant gates stop the transport. Induction gives
\[
              \|cA^j\|^2\le2\sigma^4(2\sigma^2)^j.
\]
Combining this with (5) proves
\[
                 \boxed{\quad
                 \|d\|^2\le\frac{2\sigma^4}{1-2\sigma^2}
                                =\frac1{32512}.\quad}
 \tag{6}
\]
There is no factor for the number of levels or packet coordinates.
The finite triangular transport, rather than a diagonalization or
semisimple quotient, preserves every Newton direction.

## 4. Comparison with the original invariant

Cauchy--Schwarz applied once to (4), using (6), gives
\[
                     |k|^2\le\Gamma U(w),\qquad
                              \Gamma=1+\frac1{32512}.
\]
The actual forward field in (2) satisfies \(U(a)=|k|^2\).
Taking the minimum gives the two-sided comparison
\[
          \boxed{\qquad
          B^2m_U\le |K_N|^2\le\Gamma B^2m_U.
          \qquad}
 \tag{7}
\]
This includes exact zeros. In particular, passing to the unweighted
objective introduces one uniform comparison, not a separate loss at
each gate. No normalization factor has been removed from \(K_N\).
The small comparison factor comes from the chosen Hilbert--Schmidt
budgets. It does not give a positive geometric lower bound for either
side of (7).

## 5. Degree-four certificates still suffice

The Hessian sum-of-squares proof applies directly to (3), now with
the original small-tensor bound \(\sigma\). Proper gates have the
usual allowances \(4\sigma+\sigma^2\). The scalar bilinear root
contributes a squared first variation and its self-curvature term;
the latter uses the bilinear Gram identity of the original certificate
proof, with no negative output-curvature term. The sibling pairs are
disjoint, including the root pair. Since
\[
                  2(1-4\sigma-\sigma^2)=\frac{191}{128}>1,
\]
the resulting polynomial Hessian identity is
\[
 h^{\mathsf T}(D^2U-I)h
   =\sum_\nu|L_\nu(w)h|^2+
           \sum_i(1-\|w_i\|^2)h^{\mathsf T}C_i h,
 \tag{8}
\]
with affine \(L_\nu\) and constant \(C_i\succeq0\).
This is an algebraic identity; convexity alone would not imply it.

The minimum is interior. Indeed the \(i\)-th component of
\(w-\nabla U(w)/2\) is \(f_i(w)\) minus the contribution
from its one parent. A proper parent contributes norm at most
\(\sigma(1+\sigma)\); the scalar parent contributes at most
\(\sigma^4\). Thus every component has norm at most
\(\sigma+\sigma(1+\sigma)=33/256<1\). At a minimum a nonzero
gradient would give a feasible strict descent direction along this
step. Therefore the gradient is zero there, and the step's strict
interior bound applies. Equation (8) gives uniqueness.

Gradients and Hessians use real coordinates and the inner product
\(\operatorname{Re}\sum_i h_i^*k_i\). Let \(Q_2\) consist of sums
of squares of polynomials of degree at most two plus the original
packet-ball constraints times sums of squares of linear polynomials.
Integrating (8) along a segment from any fixed feasible trial \(u\)
gives
\[
 U(w)-U(u)-\nabla U(u)\cdot(w-u)-\tfrac12\|w-u\|^2\in Q_2.
\]
The argument is the same finite-degree Taylor integration used in the
branching certificate. It follows that
\[
 m_U=\max\{\lambda:U-\lambda\in Q_2\},\qquad
 d_U(u):=U(u)-\tfrac12\|\nabla U(u)\|^2\le m_U.
 \tag{9}
\]
For each fixed trial, \(U(w)-d_U(u)\) has such a degree-four
certificate. Its coefficients use the known trial and known maps;
the unknown invariant or minimizer is not an input.
Combining (7) and (9) yields
\[
 B^2\max(0,d_U(u))\le |K_N|^2\le\Gamma B^2U(u).
 \tag{10}
\]

## 6. What remains to prove for the filling theorem

For a fixed knot construction, a family of feasible retained fields
\(u_N\) would prove the original volume limit if
\[
 U(u_N)>0,\qquad
 \eta_N=1-\frac{\|\nabla U(u_N)\|^2}{2U(u_N)}>0,\qquad
 \log\eta_N=o(N),
\]
and
\[
 \frac\pi N\log\bigl(B^2U(u_N)\bigr)
                       \longrightarrow\operatorname{Vol}(S^3\setminus K).
 \tag{11}
\]
Equation (10) proves this implication. All derivatives are with respect
to only the retained branching packets. There is no further covariance
estimate or growing-degree moment hierarchy in this criterion.

No such geometric family is constructed here for arbitrary fixed short
partial fillings. Classical gluing equations do not by themselves
establish (11) or the relative gradient inequality. The finite-exception
theorem remains open. Increasing \(N\) still increases the packet
dimension and the accuracy required for an exponentially small minimum.

When \(q=0\), there is no retained packet: the complete reduced source
is a known linear-chain contraction \(g_0\), and take \(U=|g_0|^2\)
as its evaluated constant. Here \(g_0=K_N/B\), giving equality in the left side of (7),
without asserting an asymptotic for that contraction. The original
\(p=0\) case is covered by the same convention.

## Complete proof sources and coverage

The entire matching texts were read:

| Source | SHA-256 |
|---|---|
| [Branching chains and degree-four certificate](research_conway_branching_degree_four_certificate.md) | 84f1b158b63a3fcb9a5cbedc8dcaa4fda1f926f11e6adf0be4920b939ca6cc51 |
| [Original Hessian sum-of-squares identities](research_conway_degree_four_semidefinite_certificate.md) | 8b706c7e08aa124ce5d80c2401511a3be67a09b1878b0adfd4ec989514cf44db |
| [Original deterministic chains, closing and budget](research_conway_binary_skeleton_quartic.md) | 294220039d913fd349b867f9705670215c3ca98f581461c6f406db0dac20c7a3 |

The earlier [compressed convex-source note](research_conway_compressed_convex_source.md) was read completely for
coverage. It already removes residual Gram matrices from a different,
potentially higher-degree problem. The additional assertion here is the
unweighted quartic on the branching tree and the orthogonal-depth
comparison (6)--(7), together with its fixed-degree certificates.
Least squares, midpoint identities and Cauchy--Schwarz are standard
tools; no novelty is claimed for those methods.

Only written mathematics and text/hash operations were used; no mathematical program,
numerical experiment, test, build or earlier-final edit was performed.
