# A quartic source minimum on the internal Conway edges

21 November 2026. Earlier finals and public manuscripts remain unchanged.

Retaining both inputs of each binary product permits every other
packet to be removed exactly. The reduced objective is still a
polynomial of degree at most four. Its coefficients require only
constant linear-corridor metrics and one scalar root response;
there is no linear solve depending on the trial field.

If there are \(p\ge1\) binary products, this first step leaves exactly
\(2p\) packets and preserves the minimum exactly. Fixing the \(p+1\)
known leaf inputs then leaves only \(p-1\) full packets, one on each
connection between binary products. The latter minimum may change,
but satisfies the same original source comparison. In the literal
Conway compiler all corridor weights are explicit positive scalars.
This is a simplification of the finite variational problem, not a
new geometric lower bound.

## 1. Which original variables are retained

Use the normalized full source from the convex theorem. At level
\(N\), every proper packet belongs to the complete Newton space
\(H_N\cong\mathbb C^N\), including its repeated-Casimir directions.
There are \(s\) proper vertices. A vertex is a prescribed leaf,
a constant linear gate, or a bilinear product. The original
normalized closing is the row \(c\). The energy is
\[
 E(x)=\sum_{v\ {\rm proper}}
       \|\Phi_v((x_j)_{j\text{ child of }v})-x_v\|^2
                                  +|cx_{\rm top}|^2 .
 \tag{1}
\]
Every trial packet lies in its unit ball. Each normalized leaf,
linear or bilinear map and closing row has norm at most
\(\sigma=1/16\). A constant linear gate may depend on \(N\)
and the fixed source data, but not on any trial packet.

The original budgets and their product \(B_{\rm tot}\) are fixed.
The complete source theorem gives
\[
 I\le D_{\mathbb R}^2E\le3I,\qquad
 \left(x-\tfrac12\nabla E(x)\right)_v
                              \in\frac{33}{256}\overline{\mathbb B},
 \tag{2}
\]
and, with \(\gamma=197/196\),
\[
 B_{\rm tot}^2\min E\le |K_N|^2
                         \le\gamma B_{\rm tot}^2\min E .
 \tag{3}
\]
All gradients use the real inner product
\(\operatorname{Re}\sum_vh_v^*k_v\).

Let \(p\) be the number of binary vertices. Retain the output
packet at each of their two immediate child vertices. Call this
list \(u\), and call every other proper packet \(z\).
These \(2p\) child occurrences are distinct: a vertex has exactly
one parent. If a child is itself binary, its output and its
parent's input are the same variable and are counted once.
The top proper packet is never retained. Thus
\[
                     \#u=2p\le s-1\quad(p\ge1).
 \tag{4}
\]
When \(p=0\), retain no variable.

**Theorem.** The exact partial minimum
\[
                      F(u)=\min_{\|z_v\|\le1}E(u,z)
 \tag{5}
\]
is a real polynomial of degree at most four. Its eliminated
minimizer is unique, strictly interior, and polynomial of degree
at most two in the retained real coordinates. On the retained
product of balls,
\[
                 I\le D^2F\le3I .
 \tag{6}
\]
Its half-gradient step stays in the \(33/256\) packet balls
and contracts by \(1/2\). The exact minimum in (3) may be
replaced by \(\min F\).

For \(p=0\), the reduced problem is a constant with no optimization.
The explicit formulas below evaluate \(F\) without a
trial-dependent matrix inverse.

## 2. Why the inner quadratic system has constant coefficients

By construction, both inputs of every bilinear gate are retained.
Thus no omitted variable occurs as an input of a bilinear map.
Every full residual in (1), including the closing component, is
jointly affine in \(z\), with constant coefficient matrix:
\[
                     E(u,z)=\|Az+b(u)\|^2 .
 \tag{7}
\]
The vector \(b\) is polynomial of degree at most two. For example
an omitted binary output contributes its prescribed bilinear
forcing \(\Phi_v(u_L,u_R)\) and minus that output variable.
A retained binary output has the same forcing but its negative
output is already part of \(b\). All remaining gates are linear
or constant.

The principal Hessian bounds in (2) imply
\[
                         \tfrac12I\le A^*A\le\tfrac32I .
 \tag{8}
\]
These bounds hold for the entire unconstrained inner quadratic
problem, because its Hessian is independent of \(z\).
For fixed feasible \(u\), the map
\[
                  z\longmapsto z-\tfrac12\nabla_zE(u,z)
 \tag{9}
\]
sends the omitted product of balls into its strict \(33/256\)
contraction, by the omitted components of (2). Its derivative
has norm at most \(1/2\), by (8). Iteration within those balls
therefore has a unique fixed point. It is stationary for the
unconstrained quadratic, so
\[
               z_*(u)=-(A^*A)^{-1}A^*b(u)
 \tag{10}
\]
is that point and is feasible. This proves the inactive-ball
assertion and its uniform interior margin.

Since \(A\) is constant, \(z_*\) has degree at most two, and
\[
             F(u)=b(u)^*\!
                \left[I-A(A^*A)^{-1}A^*\right]b(u)
 \tag{11}
\]
has degree at most four. Equation (11) proves the degree
claim; it need not be used to assemble a dense projection.

The difference from retaining only one child per product is
important. In that reduction the omitted child enters a product
with a retained child, so the inner matrix depends on the
retained field. Here the inner matrix is constant.

## 3. Constant corridor metrics give an explicit formula

The following description avoids the dense matrix in (11).
Start at each prescribed leaf or binary gate and follow its
output upward through the subsequent linear gates. Stop when
the output is a retained packet, or when the closing root is
reached. Every original residual belongs to exactly one such
block. Distinct blocks share only their retained boundary packets.

At the initial gate let
\[
 f(u)=
 \begin{cases}
 a,&\text{for its prescribed normalized leaf},\\
 \Phi_v(u_L,u_R),&\text{for its binary product}.
 \end{cases}
 \tag{12}
\]
The linear maps above it are \(A_1,\ldots,A_m\), with
\(\|A_i\|\le\sigma\). Write \(x_0\) for the initial
gate output and \(x_i\) for the subsequent linear outputs.

### A block ending at a retained packet

Let \(x_m=y\) be its retained top packet. The block energy is
\[
 \|x_0-f(u)\|^2+
                 \sum_{i=1}^m\|x_i-A_ix_{i-1}\|^2 .
 \tag{13}
\]
For \(m=0\), this means simply \(\|y-f(u)\|^2\);
in particular adjacent binary gates share this one packet.
Define
\[
 P_i=A_mA_{m-1}\cdots A_{i+1},\quad P_m=I,\quad
 P=P_0,\qquad W=\sum_{i=0}^mP_iP_i^* .
 \tag{14}
\]
Its exact eliminated cost is
\[
                    \boxed{\quad
                   (y-Pf(u))^*W^{-1}(y-Pf(u)).
                    \quad}
 \tag{15}
\]
To verify it, put \(r_0=x_0-f(u)\) and
\(r_i=x_i-A_ix_{i-1}\). Then
\(y-Pf(u)=\sum_iP_ir_i\).
The least-norm errors are
\[
                  r_i=P_i^*W^{-1}(y-Pf(u)).
 \tag{16}
\]
They are orthogonal to the kernel of the displayed surjective
error map, since \(P_m=I\). Thus they give the unconstrained
minimum. The omitted balls are inactive by Section 2, so this
is also the original constrained minimum.

The metric is constant and obeys
\[
                       I\le W\le\frac{256}{255}I.
 \tag{17}
\]
This follows from \(\|P_i\|\le\sigma^{m-i}\) and a
geometric series. No inverse of any individual \(A_i\) is used.

### The block ending at the original closing row

There is exactly one root block. Its energy is (13), with
\(x_m\) now omitted, together with \(|cx_m|^2\).
Put
\[
 b_i=cP_i,\qquad
 D=1+\sum_{i=0}^m\|b_i\|^2,\qquad s(u)=cP f(u).
 \tag{18}
\]
The exact root cost is the scalar expression
\[
                           \boxed{\quad |s(u)|^2/D.\quad}
 \tag{19}
\]
Indeed \(cx_m=s(u)+\sum_ib_ir_i\), and minimizing
\(\sum_i\|r_i\|^2+|s(u)+\sum_ib_ir_i|^2\) gives
\[
                           r_i=-b_i^*s(u)/D .
 \tag{20}
\]
Substitution proves (19); inactivity of the balls again
identifies it with the constrained minimum.
The scalar denominator satisfies
\[
                        1\le D\le\frac{256}{255}.
 \tag{21}
\]
Here \(\|b_i\|\le\sigma^{m-i+1}\).
The row \(c\), every \(A_i\), and their original phases
remain in (18). The symbol \(s(u)\) is a known scalar
polynomial computed from this local block; it is not an
unknown invariant inserted into the coefficients.

For \(p\ge1\), the initial gate of the root block is the
highest binary gate, so (19) is a bilinear square with a
constant scalar weight. For \(p=0\), the root block starts
at the sole leaf; (19) evaluates the whole minimum.

Summing (15) over the nonroot blocks and adding (19) is
the desired explicit \(F\). All matrices \(W^{-1}\) and
the scalar \(D^{-1}\) can be computed once per level
from the known linear operators. Evaluating \(F\) at a
trial field then uses only known quadratic forms and the
original linear and bilinear maps. There is no
trial-dependent inner solve.

Each \(f(u)\) in (12) has degree at most two. Thus these
explicit expressions also prove directly that \(F\) is quartic,
even when the original tree contains arbitrarily long linear
corridors. They preserve the same \(B_{\rm tot}\); no new
budget is assigned to \(Pf\).

### In the literal Conway compiler the metrics are scalar

Its only unary operation is the normalized turn \(A_i=J/\beta_i\),
where \(\beta_i\) is its original positive budget. Since \(J\) is
unitary and \(J^2=I\), put
\[
 \rho_i=\prod_{h=i+1}^m\beta_h^{-1},\qquad
 P_i=\rho_iJ^{m-i},\qquad
 w=\sum_{i=0}^m\rho_i^2.
 \tag{21a}
\]
Then \(W=wI\). The costs (15) and (19) become respectively
\[
 \frac{\|y-\rho_0J^mf(u)\|^2}{w},\qquad
 \frac{|c\rho_0J^mf(u)|^2}{1+\|c\|^2w}.
 \tag{21b}
\]
Every denominator is a known positive scalar. Thus the actual
reduced objective is a weighted sum of squared bilinear residuals
and one squared scalar closing. No matrix inverse, even a constant
one, is needed for its corridor coefficients.

## 4. Convexity, the inward step, and the original source

The stationary inner solution (10) is smooth on a neighborhood
of the retained balls. Differentiating its stationary equations
gives the usual real Schur complement
\[
             D^2F=H_{uu}-H_{uz}H_{zz}^{-1}H_{zu},
                 \qquad H=D^2E(u,z_*(u)).
 \tag{22}
\]
For a retained variation \(h\),
\[
 h^{\mathsf T}D^2Fh
       =\min_k(h,k)^{\mathsf T}H(h,k).
 \tag{23}
\]
The lower bound in (2) gives at least \(\|h\|^2\);
choosing \(k=0\) gives at most \(3\|h\|^2\).
This proves (6), including boundary points by the smooth formula.

The inward step needs more than the Schur bound. The envelope
identity, because the omitted gradient is zero, is
\[
                         \nabla F(u)=
                         \nabla_uE(u,z_*(u)).
 \tag{24}
\]
Thus \(u-\nabla F(u)/2\) is exactly the retained component
of the original full half-gradient step at the feasible field
\((u,z_*(u))\). Equation (2) puts every component in its
\(33/256\) ball. Averaging (6) along a segment gives the
same contraction factor \(1/2\) as in the full problem.
Consequently the reduced minimum is unique and interior.

Exact partial minimization and (3) now give
\[
          B_{\rm tot}^2\min F\le |K_N|^2
                         \le\gamma B_{\rm tot}^2\min F .
 \tag{25}
\]
The equality of minima is exact, not merely a comparison by
the corridor metric constants. The constants (17) and (21)
describe the explicit coefficients of the reduced polynomial.

## 5. Only the internal connections need remain free

Suppose \(p\ge1\). Suppress the unary corridors only for counting.
The resulting rooted binary tree has \(p\) binary vertices and
\(p+1\) prescribed leaves. Of its \(2p\) inputs, exactly \(p+1\)
come from a leaf through unary gates; the other \(p-1\) come from
a nontop binary output through unary gates.

For each leaf block, fix its retained endpoint to its known exact
center \(y=Pa\), using (12)--(15). These are prescribed leaf
transports, independent of every free packet. They have norm at
most \(\sigma\), so the restriction is feasible. Each such block
now contributes exactly zero. No output of a binary product is
fixed at its unknown true value.

Let \(\widetilde F\) be this restriction of \(F\), and write
\[
                    e_*=\min E,\qquad
                    \widetilde e_*=\min\widetilde F.
 \tag{26}
\]
It is quartic on precisely \(p-1\) full packets, or \(2N(p-1)\)
real coordinates. Its Hessian remains between \(I\) and \(3I\),
by taking the corresponding principal restriction of (6).
Its free half-gradient components are those of the full step
used in (24), with the leaf inputs fixed. They therefore remain
in their \(33/256\) balls and contract by \(1/2\).

The minima need not be equal. The restricted feasible set gives
\(e_*\le\widetilde e_*\). On the other hand, the true normalized
field satisfies every prescribed leaf transport. Using its
internal connection packets in the restricted problem, and then
minimizing the omitted packets, gives
\[
                   e_*\le\widetilde e_*
                                \le |K_N/B_{\rm tot}|^2.
 \tag{27}
\]
Combining this with (3) yields the unchanged source sandwich
\[
 \boxed{\qquad
 B_{\rm tot}^2\widetilde e_*\le |K_N|^2
                  \le\gamma B_{\rm tot}^2\widetilde e_* .
 \qquad}
 \tag{28}
\]
This includes zeros. The comparison uses the same normalization
budget and the same \(\gamma=197/196\); it does not multiply a
separate loss for each clamped leaf.

For \(p=1\), there is no remaining minimization: the two known
leaf transports enter the sole product, followed by (19).
For \(p=0\), the entire source is the single linear chain
already evaluated by (19). These statements evaluate the stated
finite source expressions; they assert no asymptotic estimate.

## 6. Scope and complete proof sources

Every retained packet is still the full \(H_N\). Omitted
packets were minimized over all their physical coordinates;
their effect remains in (15) and (19). This is not a
semisimple quotient or a deletion of Hermite directions.

The smaller one-child reduction retains \(p\) packets, but
its exact least-squares objective generally has variable
coefficients and is rational. The corresponding unweighted
compressed objective may have degree above four. The present
exact partial minimum retains \(2p\) packets to preserve the
quartic degree and constant corridor metrics. The additional
prescribed-leaf restriction reduces this to \(p-1\) packets
while preserving the source comparison, rather than preserving
the numerical minimum.

All linear maps in the corridors must be independent of
trial packets. A bilinear gate cannot be reclassified by
silently fixing one of its variational inputs at its true
value. Nor does algebraically expanding a crossing power
preserve a previously chosen normalization budget if it
changes the compiler tree.

The reduction evaluates no hyperbolic exponential rate and
supplies no additional geometric lower certificate.
An exponentially small minimum still requires relative
control; uniform conditioning alone does not supply it.
Degree-four exactness of a new sum-of-squares or semidefinite
relaxation is not inferred from the reduced objective's
convexity. The original lifted certificates remain available.

Both complete proof sources were read at the matching pins:

| Source | SHA-256 |
|---|---|
| [Normalized complete source](research_convex_normalized_conway_source.md) | 6b89b4c6a67ef7a32cc41a5966c650f32de65d284ae7b70d94a71bddba21df3c |
| [Connected-block boundary energy](research_connected_conway_block_boundary_energy.md) | 426b0eba0c7f4c502cf2b82052daf4d5a224ad8ec8419b3e2d8a624771f192ae |

The complete matching orthogonal-elimination, compressed-source
and source-normal notes were read for coverage, at pins
aa53b79685296193d5bf7fc66e53f3a3fbe03fc72a36481fb3aee23afe2ae113,
065989bd50a891d1e3a67ce7b556921a8050ac83f019b8ba27360a6386a2189c,
and 36cea2a5e40cc515e0034e91f41eeb23cb75f57d0f4750d5d341f2dcbd9081f3.
The corridor response itself is already in the connected-block
theorem. The additional assembly here is the constant-coefficient
inner system, the \(2p\)-packet quartic formula, its prescribed-leaf
reduction to \(p-1\) packets with the same source comparison,
and the preserved convexity and inward iteration. No novelty
is claimed for least squares or Schur complements.

Only written mathematics and text/hash operations were used. No
mathematical program, numerical experiment, test, build, git
operation or earlier-final edit was performed.
