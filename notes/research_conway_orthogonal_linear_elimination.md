# Orthogonal elimination of the linear Conway packet variables

21 November 2026. Research note. Earlier final notes and public
manuscripts remain unchanged.

After retaining one child packet at each binary gate, every other packet
can be eliminated by an unconstrained, uniformly positive definite linear
solve. The original unit-ball constraints on those variables are
automatically inactive. The resulting objective is the norm of a genuine
orthogonal projection, with its full Gram matrix retained.

A second form uses only the retained gate equations and the original
scalar closing row. Its boundary Gram matrix lies between \(I\) and
\((226/225)I\), uniformly in the level and tree size. This is a
reduction of the actual finite variational problem, not a geometric
evaluation of its minimum.

## 1. The original energy and the variables to retain

Use the complete normalized compiler of the
[convex source theorem](research_convex_normalized_conway_source.md).
At level \(N\), there are \(s\) proper packet variables in the full
complex Newton space \(H_N\), including the repeated-root directions.
Each prescribed leaf, linear turn and bilinear product has recorded
Hilbert--Schmidt norm at most \(\sigma=1/16\). The original normalized
closing row is \(L\), with \(\|L\|\le\sigma\). The energy is
\[
 E(x)=\sum_{v\text{ proper}}\|\Phi_v((x_c)_c)-x_v\|^2
                                          +|Lx_{\rm top}|^2.
 \tag{1}
\]
Its feasible set is the product of unit packet balls. Its real Hessian
lies between \(I\) and \(3I\). The complete original marked source
satisfies
\[
 B_{\rm tot}^2e_*\le |K_N|^2
               \le\gamma B_{\rm tot}^2e_*,\qquad
 e_*:=\min E,\quad\gamma=197/196.
 \tag{2}
\]
The normalization budget \(B_{\rm tot}\) is retained throughout.

Let \(p\) be the number of binary product gates. At each such gate
choose exactly one of its two child occurrences. Retain the packets at
the chosen occurrences and call their list \(u\). Distinct gates choose
distinct variables, because every proper variable has one parent.
There are exactly \(p\) retained packets. The top packet is never
chosen: its parent is the scalar closing root. Call the other
\(q=s-p\) packets \(z\).

Fix \(u\) in its product of unit balls. At each product, one child
is retained and the other is eliminated. Therefore the stacked vector
of **all** proper residuals, together with the original scalar closing
term, has the form
\[
            \mathcal R(u,z)=A(u)z+b(u)
                   \in H_N^{\oplus s}\oplus\mathbb C.
 \tag{3}
\]
The matrix \(A(u)\) is complex linear in \(z\); both \(A\) and
\(b\) are affine functions of the complex retained coordinates.
Indeed a product contributes a term bilinear in its retained child and
its eliminated child, and its output contributes either \(-z_v\) or
\(-u_v\). Leaves and turns are affine, and the closing component is
the original row \(Lz_{\rm top}\). Thus
\[
                              E(u,z)=\|A(u)z+b(u)\|^2.
 \tag{4}
\]
Every complex phase remains in these coefficients.

## 2. The eliminated ball constraints are inactive

In real coordinates, the \(z\)-Hessian of (4) is twice the real form
of \(A^*A\). The principal Hessian bounds for (1) imply
\[
                    \tfrac12I\le A(u)^*A(u)\le\tfrac32I.
 \tag{5}
\]
For fixed \(u\), this Hessian is independent of \(z\), so these
bounds hold for the entire unconstrained quadratic problem.

It remains to show that its unconstrained solution lies in the original
balls. The half-gradient map of the full source theorem obeys
\[
 x-\tfrac12\nabla E(x)\in\tfrac{33}{256}\mathcal D
 \tag{6}
\]
whenever \(x\) is feasible. Freeze the retained variables and apply
only its eliminated components:
\[
               T_u(z)=z-\tfrac12\nabla_zE(u,z).
 \tag{7}
\]
This map sends the eliminated product balls into their strict
\(33/256\) contraction. Its derivative is the real form of
\(I-A^*A\), whose norm is at most \(1/2\) by (5). Thus its iterates
converge to a unique fixed point in those balls. The stationary equation
there is the unconstrained normal equation. Consequently
\[
 \boxed{\quad z_*(u)=-(A(u)^*A(u))^{-1}A(u)^*b(u),\quad}
 \qquad \|(z_*(u))_v\|\le33/256.
 \tag{8}
\]
There are no active-ball cases in this inner problem.

Define \(f(u)=E(u,z_*(u))\). The exact reduction of the original
minimum is
\[
                         e_*=\min_{\|u_v\|\le1}f(u).
 \tag{9}
\]
Only \(2Np\) outer real variables remain. For \(p=0\), there is
no outer minimization and (8) evaluates the entire quadratic minimum.

## 3. The correct orthogonal projection

The matrix
\[
 \Pi(u)=I-A(u)(A(u)^*A(u))^{-1}A(u)^*
 \tag{10}
\]
is Hermitian and satisfies \(\Pi^2=\Pi\). It is the orthogonal
projection onto \(\ker A(u)^*\) in the stacked residual space of
(3). Equations (8)--(10) give
\[
                  \boxed{\quad f(u)=\|\Pi(u)b(u)\|^2.\quad}
 \tag{11}
\]
Because \(A\) has full column rank \(Nq\), this projection has
complex rank
\[
                              Ns+1-Nq=Np+1.
 \tag{12}
\]
In particular the original scalar closing component is retained in
this orthogonal complement. Squaring arbitrary coefficients in a
different spanning family would not give (11); the inverse Gram matrix
\((A^*A)^{-1}\) is required.

The function \(f\) is a real rational function of the retained
coordinates, smooth on a neighborhood of their closed product of balls.
Its real Hessian still satisfies
\[
                              I\le D^2f\le3I.
 \tag{13}
\]
To prove this, differentiate the stationary equation in (8). The
Hessian of \(f\) is the Schur complement
\[
 D^2f=H_{uu}-H_{uz}H_{zz}^{-1}H_{zu}
 \tag{14}
\]
of the Hessian of \(E\) at \((u,z_*(u))\). For a retained variation
\(h\), its quadratic form is
\[
 h^{\mathsf T}D^2f h
   =\min_k (h,k)^{\mathsf T}D^2E(h,k).
\]
The lower bound is at least \(\|h\|^2\). Choosing \(k=0\) gives
the upper bound \(3\|h\|^2\). This proves (13), including at boundary
points by the smooth formula (8). It does not assert that the reduced
rational function is a polynomial of degree four.

For a feasible retained trial field there is also the smaller gradient
certificate
\[
 f(u)-\tfrac12\|\nabla_u f(u)\|^2\le e_*\le f(u).
 \tag{14a}
\]
Complete the square in the lower Hessian inequality (13), exactly as
for the original energy. At \((u,z_*(u))\) the eliminated gradient
is zero, and \(\nabla_u f=\nabla_u E\), so only the retained
\(2Np\) real derivatives are required. The witness after elimination
is rational; evaluating it in the original lifted variables recovers
the original degree-six expression.

## 4. A smaller boundary Gram matrix

There is another exact form of (11) that displays the retained
equations explicitly. Split the residual rows into those whose gate
outputs are eliminated and all the other rows:
\[
 r_z=T(u)z+b_z(u),\qquad
 r_o=C(u)z+b_o(u).
 \tag{15}
\]
The second list contains the \(p\) retained gate equations and the
original scalar closing row. The first square matrix has form
\[
                            T=-I+A_{zz}.
 \tag{16}
\]
Order vertices by ancestry. Then \(A_{zz}\) is strictly triangular.
Every row has at most one eliminated child, and every column occurs
in at most one parent row. Each block has norm at most \(\sigma\),
so
\[
       \|A_{zz}\|\le\sigma,\qquad
       T^{-1}=-\sum_{j=0}^{q-1}A_{zz}^{j},\qquad
       \|T^{-1}\|\le16/15.
 \tag{17}
\]
Likewise every row of \(C\) has at most one eliminated child. Its
columns occur in at most one such row, counting the closing row as the
top packet's unique parent. Hence \(\|C\|\le\sigma\).

Set
\[
             D=CT^{-1},\qquad F=b_o-CT^{-1}b_z.
 \tag{18}
\]
Then \(\|D\|\le1/15\). Changing variables from \(z\) to \(r_z\)
in the unconstrained quadratic problem gives
\[
 f(u)=\min_r\{\|r\|^2+\|Dr+F\|^2\}
             =F(u)^*(I+D(u)D(u)^*)^{-1}F(u).
 \tag{19}
\]
For example, the minimizing residuals are
\(r= -D^*(I+DD^*)^{-1}F\) and
\(r_o=(I+DD^*)^{-1}F\). Thus
\[
 \boxed{\quad
 \frac{225}{226}\|F(u)\|^2\le f(u)\le\|F(u)\|^2.
 \quad}
 \tag{20}
\]
This is the boundary Gram matrix for the residual elimination. Its
size is \(Np+1\), its spectrum lies in \([1,226/225]\), and its
conditioning does not grow with the length of an eliminated corridor.

The vector \(F\) has a direct meaning. Put
\[
                           z_0(u)=-T(u)^{-1}b_z(u).
 \tag{21}
\]
It solves every eliminated gate equation exactly, by the original
forward recursion with the retained packets prescribed. Each of its
packets has norm at most \(\sigma\). The remaining residuals and
the original closing value at this field are exactly \(F(u)\).
The finite triangular inverse in (17) makes \(z_0\), and hence \(F\),
polynomial in \(u\). Their degrees can grow with the fixed expression;
their evaluation is still a finite sequence of the original local
operations.

## 5. An unweighted retained-packet comparison

One can compare \(\|F\|^2\) directly with the source with a smaller
constant than follows by combining (2) and (20). Split the derivative
of the forward maps at \((u,z_0(u))\) into its retained and eliminated
blocks \(A_{uu},A_{uz},A_{zu},A_{zz}\). Each of these four block
matrices has at most one input block in each row and one parent block
in each column. Thus all four have norm at most \(\sigma\).
Implicit differentiation of the gate-exact equations in (21) gives
\[
 z_0'(u)=(I-A_{zz})^{-1}A_{zu},\qquad
                         \|z_0'(u)\|\le1/15.
 \tag{22}
\]
Write \(F=(G_o,c)\), where \(G_o\) is the list of retained gate
residuals and \(c(u)=L(z_0(u))_{\rm top}\) is the original scalar
closing component. Then
\[
 \begin{split}
 DG_o&=-I+A_{uu}+A_{uz}(I-A_{zz})^{-1}A_{zu},\\
 \|DG_o+I\|&\le1/15,\qquad \|Dc\|\le1/240.
 \end{split}
 \tag{23}
\]
The last bound uses the fact that the top proper packet is always
eliminated. These bounds hold on the whole retained product of balls:
the forward recursion in (21) keeps all eliminated packets feasible.

Let \(a\) be the true normalized packet field, let \(u_a\) be its
retained coordinates, and put \(k=K_N/B_{\rm tot}\). We have
\(G_o(u_a)=0\) and \(c(u_a)=k\). Integrating (23) along a feasible
segment gives
\[
 \|G_o(u)-G_o(u_a)\|\ge\tfrac{14}{15}\|u-u_a\|,
 \qquad
                  |c(u)-k|\le\tfrac1{224}\|G_o(u)\|.
 \tag{24}
\]
Consequently Cauchy--Schwarz, followed by the competitor \(u_a\),
proves the direct comparison
\[
 \boxed{\quad
 \frac{|k|^2}{1+224^{-2}}
       \le\min_{\|u_v\|\le1}\|F(u)\|^2\le|k|^2.
 \quad}
 \tag{25}
\]
It includes source zeros. When there are no retained variables,
\(F\) is simply the scalar \(k\), so the unweighted value is exactly
\(|k|^2\). For a fixed tree, restoring \(B_{\rm tot}^2\) in (25)
gives the same exponential rate as the original source, with no
uncontrolled Gram loss. This does not assert convexity or degree four
for the compressed polynomial \(\|F(u)\|^2\).

## 6. Scope of the simplification

The exact reduced minimum in (9) satisfies the unchanged source bounds
(2). Equation (20) also permits replacing its boundary Gram by the
identity with an explicitly proved constant comparison. That step is
valid because (17)--(20) control this particular Gram matrix. It is
not a rule for discarding arbitrary quantum boundary metrics.

This construction concerns the budget-normalized recursion errors.
It is distinct from a quotient metric on the physical tangle synthesis
map, which can have exponential condition number. All original
normalization factors remain in \(B_{\rm tot}\). No actual crossing
or product is asserted to be unitary in an unscaled physical metric.

Elimination has removed the inner constrained optimization, exposed a
true orthogonal projection and reduced the number of nonlinear packet
variables. It has not supplied a positive geometric trial value at the
volume rate. The original coherent closing remains one component of
\(F\), and exact source cancellation remains possible. The finite
degree-four formulation can be retained by keeping the linear
variables and the original gate equations; explicit elimination instead
produces the rational function (11), or the higher-degree polynomial
vector in (18). Neither representation alone gives the missing
hyperbolic lower bound after arbitrary fixed partial fillings.

## Complete proof source and coverage

The sole complete proof source was read at the matching version:

| Source | SHA-256 |
|---|---|
| [Complete normalized Conway source](research_convex_normalized_conway_source.md) | 6b89b4c6a67ef7a32cc41a5966c650f32de65d284ae7b70d94a71bddba21df3c |

Projecting out variables that enter linearly is the established
variable-projection method; see the primary record of
[Golub--Pereyra (1973)](https://epubs.siam.org/doi/10.1137/0710036).
Its proof is not used here. The source-specific assertions proved above
are the inactive packet balls, uniform Gram bounds, exact retained
closing component and full-Hermite reduction for the actual tree.
No novelty is claimed for least squares or orthogonal projection.

Only written mathematics and text/hash operations were used. No
mathematical program, numerical optimization, test, build, git operation
or earlier-final edit was performed.
