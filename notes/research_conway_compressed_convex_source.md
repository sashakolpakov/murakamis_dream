# A convex source minimum without the linear corridor variables

21 November 2026. Research note. Earlier finals and public manuscripts
remain unchanged.

One packet at each binary product is enough for a uniformly convex
minimum representing the original Conway source. The other packets
can be evaluated by forward substitution. The inverse Gram matrix
from exact least-squares elimination can then be omitted: the resulting
unweighted objective is itself strongly convex, has a unique interior
minimum, and admits a projection-free iteration with contraction
factor \(1/4\).

The source comparison keeps the original normalization budget. This
removes linear solves from the reduced optimization; it does not
evaluate its geometric exponential rate.

## 1. The original normalized source and the retained packets

Use the complete normalized source of
[the convex theorem](research_convex_normalized_conway_source.md).
At level \(N\ge2\), every packet belongs to the full Newton space
\(H_N\cong\mathbb C^N\), including all repeated-Casimir directions.
The local normalized leaf, turn, product and original scalar closing
have norm at most
\[
                              \sigma=\frac1{16}.
\]
For a map, the recorded Hilbert--Schmidt budget implies this operator
bound. All phases and source markings are retained. Write
\[
 a_v=\Phi_v((a_c)_c),\qquad
 k=\frac{K_N}{B_{\rm tot}}=La_{\rm top}.
 \tag{1}
\]
Here \(B_{\rm tot}\) is exactly the product of the original local
budgets, not a new geometric normalization. The true packets satisfy
\(\|a_v\|\le\sigma\), and \(\|L\|\le\sigma\).

Let \(p\) be the number of binary product vertices. Choose one child
occurrence at each such vertex and retain that packet as a variable.
Each occurrence has one parent, so this selects \(p\) distinct packets.
Call them \(u=(u_1,\ldots,u_p)\), and call all other proper packets
\(z\). The top packet is eliminated, since its parent is the scalar
closing root.

For each feasible \(u\), meaning \(\|u_i\|\le1\), define \(z_0(u)\)
by solving every eliminated-output gate equation exactly from the
leaves toward the root. A retained packet is a prescribed input when its
parent is evaluated. Every eliminated packet has norm at most
\(\sigma\): the inputs are in their unit balls, and each normalized
gate has norm at most \(\sigma\).

Let \(\Psi(u)\) denote the gate outputs at the retained vertices,
evaluated at \((u,z_0(u))\), and retain the original closing
\[
                   c(u)=L(z_0(u))_{\rm top}.
\]
Thus
\[
 G_o(u)=\Psi(u)-u,\qquad
 F(u)=(G_o(u),c(u)),\qquad
 H(u)=\|F(u)\|^2.
 \tag{2}
\]
In particular \(\|\Psi_i(u)\|\le\sigma\) and
\(|c(u)|\le\sigma^2\). The original scalar is still the last
component of \(F\); it has not been replaced by a norm.

The earlier
[orthogonal elimination theorem](research_conway_orthogonal_linear_elimination.md)
proved
\[
 \frac{|k|^2}{\gamma_{\rm ret}}
       \le \min_{\|u_i\|\le1}H(u)\le |k|^2,\qquad
                  \gamma_{\rm ret}=1+224^{-2}.
 \tag{3}
\]
It did not assert convexity of \(H\). That is the additional
statement proved here.

If \(p=0\), there is no optimization: forward substitution gives
\(H=|k|^2\). Below assume \(p\ge1\).

## 2. First derivatives of the forward substitution

At a feasible field, let \(A_{ij}\) be the block derivative of the
normalized forward maps from variable class \(j\) to output class
\(i\), where \(i,j\in\{u,z\}\). These are derivatives of the forward
maps, before subtracting the output variables.

Every original product has exactly one retained child and one
eliminated child. Consequently each of these four block matrices
has at most one input block in each row and at most one parent
block in each column. Its operator norm is at most \(\sigma\).
The eliminated matrix \(A_{zz}\) is strictly triangular, so
\[
 \begin{split}
 Dz_0&=(I-A_{zz})^{-1}A_{zu},&
               \|Dz_0\|&\le\frac1{15},\\
 D\Psi&=A_{uu}+A_{uz}(I-A_{zz})^{-1}A_{zu},&
               \|D\Psi\|&\le\frac1{15},\\
 &&\|Dc\|&\le\frac1{240}.
 \end{split}
 \tag{4}
\]
The last estimate uses that the top packet is eliminated.
These bounds can also be obtained directly by summing the
attenuated derivatives along the eliminated corridors.
In particular
\[
 \frac{14}{15}\|h\|\le\|DG_o(u)h\|
                         \le\frac{16}{15}\|h\|.
 \tag{5}
\]
The product norm and all differential statements use the real
inner product \(\operatorname{Re}\sum_i h_i^*k_i\).

## 3. A dimension-independent second-variation estimate

The important point is that second variations do not accumulate
with the number or length of corridors.

Fix a retained variation \(h\), put
\(\delta z=Dz_0(u)h\), and differentiate the exact eliminated
gate equations twice along this variation. At a binary gate \(v\),
the direct second-derivative forcing is
\[
          q_v=2\Phi_v(h_{\rm retained\ child},
                              \delta z_{\rm eliminated\ child}).
 \tag{6}
\]
At leaves and linear gates it is zero. The child pairs at distinct
binary gates are disjoint. Cauchy--Schwarz and (4) therefore give
\[
 \sum_{\text{all binary }v}\|q_v\|
 \le2\sigma\|h\|\,\|\delta z\|
 \le\frac1{120}\|h\|^2.
 \tag{7}
\]

Separate this forcing into eliminated-output and remaining-output
rows, with sums of packet norms \(Q_z,Q_o\), respectively.
The scalar closing has no direct second derivative. Write
\(\eta_z=D^2z_0(u)[h,h]\). Differentiating its forward recursion gives
\[
                  \eta_z=A_{zz}\eta_z+q_z.
 \tag{8}
\]
Use the block \(\ell^1\) norm, the sum of the packet norms, just for
this estimate. Each eliminated variable has one parent, so
\(\|A_{zz}\|_{1\to1}\le\sigma\). The derivative from eliminated
packets into the remaining retained-output equations and the scalar
closing also has block \(\ell^1\) norm at most \(\sigma\).
Consequently
\[
 \|\eta_z\|_1\le\frac{Q_z}{1-\sigma},\qquad
 \sum_{\text{remaining rows}}
          \|D^2(\Psi,c)[h,h]\|
       \le Q_o+\frac{\sigma}{1-\sigma}Q_z
       \le Q_o+Q_z.
 \tag{9}
\]
Combining with (7) proves
\[
 \boxed{\quad
 \sum_{\text{remaining rows}}\|D^2F(u)[h,h]\|
                            \le\frac1{120}\|h\|^2.
 \quad}
 \tag{10}
\]
The explicit \(-u\) term has zero second derivative. No factor
depending on \(N\), \(p\), or the corridor lengths occurs.

Since \(\|(G_o)_i\|\le1+\sigma\) and \(|c|\le\sigma^2\),
(10) yields the residual-curvature estimate
\[
 \left|\operatorname{Re}\langle F,D^2F[h,h]\rangle\right|
                     \le\frac{17}{1920}\|h\|^2.
 \tag{11}
\]

## 4. Strong convexity and an interior contracting iteration

**Theorem.** On the product of retained unit balls,
\[
                         \frac32 I\le D^2H\le\frac52 I.
 \tag{12}
\]
The minimum is unique and interior. The iteration
\[
                         u^{(j+1)}
                          =u^{(j)}-\frac12\nabla H(u^{(j)})
 \tag{13}
\]
stays feasible and contracts distances to that minimum by at most
\(1/4\) at every step.

**Proof.** The half-Hessian is
\[
 \tfrac12D^2H[h,h]
       =\|DFh\|^2+\operatorname{Re}\langle F,D^2F[h,h]\rangle.
\]
Equations (4), (5), and (11) bound the full Hessian between
\[
 2\left[\left(\frac{14}{15}\right)^2-\frac{17}{1920}\right]I
 \quad\text{and}\quad
 2\left[\left(\frac{16}{15}\right)^2+
                          \frac1{240^2}+\frac{17}{1920}\right]I.
 \tag{14}
\]
These imply (12).

It remains to check feasibility without projection. A retained input
can affect exactly one remaining output equation: follow its unique
parent path through eliminated vertices until reaching the first
retained output, or the scalar closing. A retained output is prescribed,
so its equation stops that forward influence. There is no cycle and
\(\Psi_i\) is independent of its own \(u_i\).

The derivative into that one downstream row is a product of local
derivative blocks. Its norm is at most \(\sigma\), since the path
has at least one gate. There is no sum over competing paths.
From (2), the \(i\)-th component of the half-gradient step is
\[
 \left(u-\tfrac12\nabla H(u)\right)_i
       =\Psi_i(u)-(D_i(\Psi,c))^*F(u).
 \tag{15}
\]
Only the one downstream row occurs in the adjoint term. Thus
\[
 \left\|\left(u-\tfrac12\nabla H(u)\right)_i\right\|
       \le\sigma+\sigma(1+\sigma)=\frac{33}{256}<1.
 \tag{16}
\]
The scalar-root case has the smaller bound \(|c|\le\sigma^2\).

For two feasible fields, average the Hessian along their segment.
By (12), the operator \(I-\tfrac12\overline{D^2H}\) has norm at
most \(1/4\). Hence (13) is a contraction on the complete product
of closed balls. Its iterates converge to a unique fixed point
\(u_*\), with
\[
              \|u^{(j)}-u_*\|\le4^{-j}\|u^{(0)}-u_*\|.
 \tag{17}
\]
At the fixed point the gradient vanishes. Strong convexity makes it
the unique minimum, and (16) places it in the interior. \(\square\)

Forward substitution and its reverse adjoint pass evaluate \(H\)
and its gradient. The iteration uses neither the inner normal
equations nor an inverse boundary Gram matrix. This does not assert
a cheap implementation of the original tensor contractions.

## 5. The source and its reduced lower certificate

Let \(h_*=\min H\). The original comparison (3) is unchanged:
\[
 B_{\rm tot}^2 h_*\le |K_N|^2
                \le\gamma_{\rm ret}B_{\rm tot}^2h_*.
 \tag{18}
\]
It includes exact zeros. In particular
\(Q_N^{\rm ret}=\gamma_{\rm ret}B_{\rm tot}^2h_*\) differs from
\(|K_N|^2\) by at most the fixed factor \(\gamma_{\rm ret}\).

Strong convexity gives the reduced lower certificate
\[
 D_{\rm ret}(u)=H(u)-\frac13\|\nabla H(u)\|^2,\qquad
              D_{\rm ret}(u)\le h_*\le H(u).
 \tag{19}
\]
Indeed the quadratic minorant with Hessian \(3I/2\) has unrestricted
minimum \(H-\|\nabla H\|^2/3\). At \(u_*\) equality holds, so
\[
                  h_*=\max_{\|u_i\|\le1}D_{\rm ret}(u).
 \tag{20}
\]
The certificate need not be concave. Combining with (18) gives
\[
 B_{\rm tot}^2\max(0,D_{\rm ret}(u))
       \le |K_N|^2
       \le\gamma_{\rm ret}B_{\rm tot}^2H(u).
 \tag{21}
\]
Only the \(2Np\) retained real-coordinate derivatives are needed.
A geometric trial family with
\(\|\nabla H(u_N)\|^2\le3(1-\eta_N)H(u_N)\),
\(0<\eta_N\le1\), and \(\log\eta_N=o(N)\) would have a lower witness
at the same exponential rate as its upper value. Such a family is
not supplied here.

## 6. Degree, scope, and complete proof sources

Every forward expression is multiaffine in the retained packet
groups, meaning affine in each packet separately. A literal tree uses
each occurrence once, and eliminating
a corridor does not duplicate it inside one output expression.
Thus \(H\) is separately quadratic in each retained packet. Its total
real degree is at most \(2\max(1,p)\). This can exceed four.
The original lifted formulation retains degree four; the reduction
trades that degree bound for fewer variables and no inner linear solve.

The correct Gram of exact least-squares elimination has not been
declared equal to the identity. The unweighted objective is a different
minimum with its own proved source comparison and the additional
convexity theorem above. All original normal directions remain in
each retained full packet.

The minimum remains a representation of a coherent quantum scalar.
Uniform convexity, a faster iteration, and fewer packet variables
do not determine its hyperbolic volume rate or the coefficient of a
geometric contribution after arbitrary fixed short partial fillings.
Absolute and relative accuracy for an exponentially small minimum
are different requirements.

Both complete proof texts were read at the matching pins:

| Source | SHA-256 |
|---|---|
| [Normalized complete source](research_convex_normalized_conway_source.md) | 6b89b4c6a67ef7a32cc41a5966c650f32de65d284ae7b70d94a71bddba21df3c |
| [Exact orthogonal elimination](research_conway_orthogonal_linear_elimination.md) | aa53b79685296193d5bf7fc66e53f3a3fbe03fc72a36481fb3aee23afe2ae113 |

Only written mathematics and text/hash operations were used. No
mathematical program, numerical iteration, test, build, git operation
or earlier-final edit was performed.
